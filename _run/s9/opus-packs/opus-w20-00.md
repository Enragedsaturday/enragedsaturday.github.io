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

## GROUP: _overhaul2/lake/cases/United States v. Sharpe.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Sharpe"
type: case
citation: "470 U.S. 675 (1985)"
parallel_cite: "105 S. Ct. 1568; 84 L. Ed. 2d 605; 53 U.S.L.W. 4346"
neutral_cite: 1985 U.S. LEXIS 74
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-03-20
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-03-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Sharpe
  varies_by_point: false
  scope_note: "Good law; the diligence test for the permissible duration of a Terry stop (no rigid time limit) remains controlling and underlies Rodriguez v. United States."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111378/united-states-v-sharpe/"
  cluster_id: 111378
  opinion_id: 9429956
  identity_checked: true
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Progeny (duration)"
related: ["[[Terry v. Ohio]]", "[[United States v. Place]]", "[[Florida v. Royer]]", "[[United States v. Hensley]]", "[[Rodriguez v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure", "terry-stop", "duration", "investigative-detention"]
holding: "There is no rigid time limit for a Terry stop; a 20-minute investigative detention was reasonable where police diligently pursued an investigation likely to confirm or dispel suspicion quickly."
lake:
  record_id: United States v. Sharpe
  status: verified
  projected_at: 2026-07-09
---

# United States v. Sharpe

*470 U.S. 675 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A DEA agent and a state patrolman, suspecting drug trafficking, tried to stop a Pontiac and an overloaded pickup traveling in tandem. The pickup's driver, Savage, evaded the patrolman and was stopped about half a mile ahead. The agent stayed with Sharpe (the Pontiac) and then drove to Savage's truck; Savage was detained roughly 20 minutes while the agent coordinated with the patrolman, after which the agent smelled marijuana and discovered bales in the truck. The Court of Appeals held the 20-minute detention too long to be a *[[Terry v. Ohio|Terry]]* stop.

## Issue
Whether a roughly 20-minute investigative detention exceeded the permissible bounds of a *[[Terry v. Ohio|Terry]]* stop and became a [[Common Legal Terms#de-facto|de facto]] arrest requiring probable cause.

## Rule
There is no fixed durational ceiling on a *[[Terry v. Ohio|Terry]]* stop: "But our cases impose no rigid time limitation on *Terry* stops." — 470 U.S. at 685. ^pin-685

The test is diligence, not the clock: "In assessing whether a detention is too long in duration to be justified as an investigative stop, we consider it appropriate to examine whether the police diligently pursued a means of investigation that was likely to confirm or dispel their suspicions quickly, during which time it was necessary to detain the defendant." — [*Id.* at 686](https://www.courtlistener.com/opinion/111378/united-states-v-sharpe/#:~:text=In%20assessing%20whether%20a%20detention). ^pin-686

## Application
The agent pursued his investigation diligently: during most of Savage's 20-minute detention he was attempting to reach the patrolman, and once they joined he proceeded expeditiously — checking documents, requesting consent, confirming the truck was overloaded, and detecting marijuana. Critically, much of the delay was attributable to Savage's own evasive driving, not to any dilatoriness by police. Because the officers acted reasonably and did not unnecessarily prolong the stop, the 20-minute detention was a valid investigative stop, not a [[Common Legal Terms#de-facto|de facto]] arrest; a *[[Common Legal Terms#per-se|per se]]* 20-minute rule would be at odds with the Court's flexible approach.

## Conclusion
The 20-minute detention was reasonable; the Court of Appeals erred in adopting an effective *[[Common Legal Terms#per-se|per se]]* time limit. *Sharpe* governs the duration of *[[Terry v. Ohio|Terry]]* stops through a diligence-and-necessity inquiry rather than a bright-line clock.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Develops the duration analysis of [[United States v. Place]] and distinguishes the de-facto-arrest findings of [[Florida v. Royer]]; the diligence principle underlies [[Rodriguez v. United States]] (a stop may not be prolonged beyond its traffic mission absent reasonable suspicion). See also [[United States v. Hensley]].

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Progeny (duration)*

## Sources
- *United States v. Sharpe*, 470 U.S. 675 (1985) — https://www.courtlistener.com/opinion/111378/united-states-v-sharpe/ — pinpoints: 685, 686.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3196e434725f9455", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Sharpe"}, "payload": {"all": [{"cite": "470 U.S. 675", "page": "675", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "470"}, {"cite": "105 S. Ct. 1568", "page": "1568", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "105"}, {"cite": "84 L. Ed. 2d 605", "page": "605", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "84"}, {"cite": "1985 U.S. LEXIS 74", "page": "74", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1985"}, {"cite": "53 U.S.L.W. 4346", "page": "4346", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "53"}], "display": "470 U.S. 675", "official": {"cite": "470 U.S. 675", "page": "675", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "470"}, "official_selection_present": true, "record_id": "United States v. Sharpe"}}
{"assertion_id": "a8f635007c674d92", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-686", "record_id": "United States v. Sharpe"}, "payload": {"fragment": "#:~:text=In%20assessing%20whether%20a%20detention", "page": null, "pin_id": "pin-686", "pinpoint_status": "star-verified", "quote": "In assessing whether a detention is too long in duration to be justified as an investigative stop, we consider it appropriate to examine whether the police diligently pursued a means of investigation that was likely to confirm or dispel their suspicions quickly, during which time it was necessary to detain the defendant.", "quote_fidelity": "matched", "record_id": "United States v. Sharpe", "star_marker": "686"}}
{"assertion_id": "d7bdf0972e9ace86", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-685", "record_id": "United States v. Sharpe"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-685", "pinpoint_status": "slip-only", "quote": "--- # United States v. Sharpe *470 U.S. 675 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A DEA agent and a state patrolman, suspecting drug trafficking, tried to stop a Pontiac and an overloaded pickup traveling in tandem. The pickup's driver, Savage, evaded the patrolman and was stopped about half a mile ahead. The agent stayed with Sharpe (the Pontiac) and then drove to Savage's truck; Savage was detained roughly 20 minutes while the agent coordinated with the patrolman, after which the agent smelled marijuana and discovered bales in the truck. The Court of Appeals held the 20-minute detention too long to be a *Terry* stop. ## Issue Whether a roughly 20-minute investigative detention exceeded the permissible bounds of a *Terry* stop and became a de facto arrest requiring probable cause. ## Rule There is no fixed durational ceiling on a *Terry* stop:", "quote_fidelity": "mismatch", "record_id": "United States v. Sharpe", "star_marker": null}}
{"assertion_id": "adad7bc13ce2a42e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Sharpe"}, "payload": {"as_of_content": "1985-03-20", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Sharpe", "scope_note": "Good law; the diligence test for the permissible duration of a Terry stop (no rigid time limit) remains controlling and underlies Rodriguez v. United States.", "varies_by_point": false}}
```

### lake record — United States v. Sharpe

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Sharpe",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Sharpe",
    "case_name_short": "Sharpe",
    "case_name_full": "UNITED STATES v. SHARPE Et Al.",
    "input_case_name": "United States v. Sharpe",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-03-20",
    "year": 1985,
    "docket": null,
    "cluster_id": 111378,
    "lead_opinion_id": 9429956,
    "sibling_ids": [
      111378,
      9429956,
      9429957,
      9429958,
      9429959,
      9429960
    ],
    "absolute_url": "/opinion/111378/united-states-v-sharpe/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "470 U.S. 675",
      "volume": "470",
      "reporter": "U.S.",
      "page": "675",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 1568",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1568",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 2d 605",
        "volume": "84",
        "reporter": "L. Ed. 2d",
        "page": "605",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4346",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4346",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 74",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "74",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "470 U.S. 675",
        "volume": "470",
        "reporter": "U.S.",
        "page": "675",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 1568",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1568",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 2d 605",
        "volume": "84",
        "reporter": "L. Ed. 2d",
        "page": "605",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 74",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "74",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4346",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4346",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "470 U.S. 675",
    "official_selection": {
      "court_class": "scotus",
      "selected": "470 U.S. 675",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-685",
      "page": null,
      "quote": "--- # United States v. Sharpe *470 U.S. 675 (1985)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A DEA agent and a state patrolman, suspecting drug trafficking, tried to stop a Pontiac and an overloaded pickup traveling in tandem. The pickup's driver, Savage, evaded the patrolman and was stopped about half a mile ahead. The agent stayed with Sharpe (the Pontiac) and then drove to Savage's truck; Savage was detained roughly 20 minutes while the agent coordinated with the patrolman, after which the agent smelled marijuana and discovered bales in the truck. The Court of Appeals held the 20-minute detention too long to be a *Terry* stop. ## Issue Whether a roughly 20-minute investigative detention exceeded the permissible bounds of a *Terry* stop and became a de facto arrest requiring probable cause. ## Rule There is no fixed durational ceiling on a *Terry* stop:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-686",
      "page": null,
      "quote": "In assessing whether a detention is too long in duration to be justified as an investigative stop, we consider it appropriate to examine whether the police diligently pursued a means of investigation that was likely to confirm or dispel their suspicions quickly, during which time it was necessary to detain the defendant.",
      "star_marker": "686",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 28085,
      "fragment": "#:~:text=In%20assessing%20whether%20a%20detention",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-03-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Sharpe",
    "varies_by_point": false,
    "scope_note": "Good law; the diligence test for the permissible duration of a Terry stop (no rigid time limit) remains controlling and underlies Rodriguez v. United States.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 9352593,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6620965,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6478743,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Soriano-Lara",
          "cluster_id": 4881582,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Reed",
          "cluster_id": 10018647,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Reed",
          "cluster_id": 4731165,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Sokolow",
          "cluster_id": 112239,
          "cite": [
            "104 L. Ed. 2d 1",
            "109 S. Ct. 1581",
            "490 U.S. 1",
            "1989 U.S. LEXIS 1694",
            "57 U.S.L.W. 4401"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
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
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
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
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ohio v. Robinette",
          "cluster_id": 118066,
          "cite": [
            "136 L. Ed. 2d 347",
            "117 S. Ct. 417",
            "519 U.S. 33",
            "1996 U.S. LEXIS 6971"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
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
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Carney",
          "cluster_id": 111423,
          "cite": [
            "85 L. Ed. 2d 406",
            "105 S. Ct. 2066",
            "471 U.S. 386",
            "1985 U.S. LEXIS 8",
            "53 U.S.L.W. 4521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. State",
          "cluster_id": 2419717,
          "cite": [
            "947 S.W.2d 240",
            "1997 Tex. Crim. App. LEXIS 43",
            "1997 WL 292676"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Montoya De Hernandez",
          "cluster_id": 111509,
          "cite": [
            "87 L. Ed. 2d 381",
            "105 S. Ct. 3304",
            "473 U.S. 531",
            "1985 U.S. LEXIS 120",
            "53 U.S.L.W. 5048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kothe v. State",
          "cluster_id": 1504839,
          "cite": [
            "152 S.W.3d 54",
            "2004 Tex. Crim. App. LEXIS 1749",
            "2004 WL 2347781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.",
          "cluster_id": 136990,
          "cite": [
            "159 L. Ed. 2d 292",
            "124 S. Ct. 2451",
            "542 U.S. 177",
            "2004 U.S. LEXIS 4385",
            "17 Fla. L. Weekly Fed. S 406",
            "72 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Balentine v. State",
          "cluster_id": 1662103,
          "cite": [
            "71 S.W.3d 763",
            "2002 WL 496960"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
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
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
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
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scroggins",
          "cluster_id": 71470,
          "cite": [
            "599 F.3d 433",
            "2010 U.S. App. LEXIS 4551",
            "2010 WL 724688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Amores v. State",
          "cluster_id": 1670855,
          "cite": [
            "816 S.W.2d 407",
            "1991 Tex. Crim. App. LEXIS 183",
            "1991 WL 183121"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Foote v. Spiegel",
          "cluster_id": 155036,
          "cite": [
            "118 F.3d 1416",
            "1997 U.S. App. LEXIS 16800",
            "1997 WL 374158"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hicks",
          "cluster_id": 5688381,
          "cite": [
            "68 N.Y.2d 234",
            "508 N.Y.S.2d 163",
            "500 N.E.2d 861",
            "1986 N.Y. LEXIS 21211"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mateen Yusuf Shabazz, A/K/A Edward L. Eberhart, A/K/A Edward Wallace, and Keith Lamar Parker",
          "cluster_id": 606689,
          "cite": [
            "993 F.2d 431",
            "1993 U.S. App. LEXIS 13132",
            "1993 WL 187994"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
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
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Degen v. United States",
          "cluster_id": 2621067,
          "cite": [
            "135 L. Ed. 2d 102",
            "116 S. Ct. 1777",
            "517 U.S. 820",
            "1996 U.S. LEXIS 3719"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gregory B. Bloomfield, Also Known as Earl Marcum Johnson",
          "cluster_id": 682770,
          "cite": [
            "40 F.3d 910",
            "1994 U.S. App. LEXIS 32273",
            "1994 WL 643872"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ortega-Rodriguez v. United States",
          "cluster_id": 112829,
          "cite": [
            "122 L. Ed. 2d 581",
            "113 S. Ct. 1199",
            "507 U.S. 234",
            "1993 U.S. LEXIS 1949"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
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
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Luis Guzman and Sonia Cruz-Lazo",
          "cluster_id": 516479,
          "cite": [
            "864 F.2d 1512",
            "1988 U.S. App. LEXIS 17681",
            "1988 WL 138644"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cady, Davy v. Sheahan, Michael",
          "cluster_id": 2999846,
          "cite": [
            "467 F.3d 1057",
            "2006 WL 3113670"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sharpe:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111378 OR 9429956 OR 9429957 OR 9429958 OR 9429959 OR 9429960) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTMzMTY4MDAwMDAwJnM9NDUyMzg4OSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111378+OR+9429956+OR+9429957+OR+9429958+OR+9429959+OR+9429960%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111378 OR 9429956 OR 9429957 OR 9429958 OR 9429959 OR 9429960)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNzAmcz0yMTkyODEwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111378+OR+9429956+OR+9429957+OR+9429958+OR+9429959+OR+9429960%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111378 OR 9429956 OR 9429957 OR 9429958 OR 9429959 OR 9429960)",
        "reviewed": 77,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 77,
        "triage_read": 0,
        "triage_snippet_classified": 77
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111378 OR 9429956 OR 9429957 OR 9429958 OR 9429959 OR 9429960)",
    "indexed_citing_opinions": 1882,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111378,
        "count": 1607,
        "count_source": "search"
      },
      {
        "opinion_id": 9429956,
        "count": 307,
        "count_source": "search"
      },
      {
        "opinion_id": 9429957,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429958,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429959,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429960,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2971,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-sharpe.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNDEzNDMmcz0xMDM0OTQxNiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111378+OR+9429956+OR+9429957+OR+9429958+OR+9429959+OR+9429960%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111378,
        "cited_id": 89440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 92216,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 96198,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 104029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 104442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 104717,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 104822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 108028,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 108419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 109213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 111157,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 111226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 111280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 111305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 335159,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 383730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 395186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 399391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 405243,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 407760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 421705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 1930576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 2040129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 2090628,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 2107294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111378,
        "cited_id": 2293646,
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
    "date_created": "2026-07-06T02:59:39Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:00:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:00:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:04:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:00:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Sharpe

```
<opinion type="majority">
<author id="b732-10">Chief Justice Burger</author>
<p id="Ajg">delivered the opinion of the Court.</p>
<p id="b732-11">We granted certiorari to decide whether an individual reasonably suspected of engaging in criminal activity may be <page-number citation-index="1" label="677">*677</page-number>detained for a period of 20 minutes, when the detention is necessary for law enforcement officers to conduct a limited investigation of the suspected criminal activity.</p>
<p id="ATs">I — I</p>
<p id="AqP">&lt;1</p>
<p id="AboI">On the morning of June 9, 1978, Agent Cooke of the Drug Enforcement Administration (DEA) was on patrol in an unmarked vehicle on a coastal road near Sunset Beach, North Carolina, an area under surveillance for suspected drug trafficking. At approximately 6:30 a. m., Cooke noticed a blue pickup truck with an attached camper shell traveling on the highway in tandem with a blue Pontiac Bonneville. Respondent Savage was driving the pickup, and respondent Sharpe was driving the Pontiac. The Pontiac also carried a passenger, Davis, the charges against whom were later dropped. Observing that the truck was riding low in the rear and that the camper did not bounce or sway appreciably when the truck drove over bumps or around curves, Agent Cooke concluded that it was heavily loaded. A quilted material covered the rear and side windows of the camper.</p>
<p id="Asq">Cooke’s suspicions were sufficiently aroused to follow the two vehicles for approximately 20 miles as they proceeded south into South Carolina. He then decided to make an “investigative stop” and radioed the State Highway Patrol for assistance. Officer Thrasher, driving a marked patrol car, responded to the call. Almost immediately after Thrasher caught up with the procession, the Pontiac and the pickup turned off the highway and onto a campground road.<footnotemark>1</footnotemark> Cooke and Thrasher followed the two vehicles as the latter drove along the road at 55 to 60 miles an hour, exceeding the speed limit of 35 miles an hour. The road eventually looped back to <page-number citation-index="1" label="678">*678</page-number>the highway, onto which Savage and Sharpe turned and continued to drive south.</p>
<p id="b734-5">At this point, all four vehicles were in the middle lane of the three right-hand lanes of the highway. Agent Cooke asked Officer Thrasher to signal both vehicles to stop. Thrasher pulled alongside the Pontiac, which was in the lead, turned on his flashing light, and motioned for the driver of the Pontiac to stop. As Sharpe moved the Pontiac into the right lane, the pickup truck cut between the Pontiac and Thrasher’s patrol car, nearly hitting the patrol car, and continued down the highway. Thrasher pursued the truck while Cooke pulled up behind the Pontiac.</p>
<p id="b734-6">Cooke approached the Pontiac and identified himself. He requested identification, and Sharpe produced a Georgia driver’s license bearing the name of Raymond J. Pavlo-vich. Cooke then attempted to radio Thrasher to determine whether he had been successful in stopping the pickup truck, but he was unable to make contact for several minutes, apparently because Thrasher was not in his patrol car. Cooke radioed the local police for assistance, and two officers from the Myrtle Beach Police Department arrived about 10 minutes later. Asking the two officers to “maintain the situation,” Cooke left to join Thrasher.</p>
<p id="b734-7">In the meantime, Thrasher had stopped the pickup truck about one-half mile down the road. After stopping the truck, Thrasher had approached it with his revolver drawn, ordered the driver, Savage, to get out and assume a “spread eagled” position against the side of the truck, and patted him down. Thrasher then holstered his gun and asked Savage for his driver’s license and the truck’s vehicle registration. Savage produced his own Florida driver’s license and a bill of sale for the truck bearing the name of Pavlovich. In response to questions from Thrasher concerning the ownership of the truck, Savage said that the truck belonged to a friend and that he was taking it to have its shock absorbers repaired. When Thrasher told Savage that he would be held <page-number citation-index="1" label="679">*679</page-number>until the arrival of Cooke, whom Thrasher identified as a DEA agent, Savage became nervous, said that he wanted to leave, and requested the return of his driver’s license. Thrasher replied that Savage was not free to leave at that time.</p>
<p id="b735-5">Agent Cooke arrived at the scene approximately 15 minutes after the truck had been stopped. Thrasher handed Cooke Savage’s license and the bill of sale for the truck; Cooke noted that the bill of sale bore the same name as Sharpe’s license. Cooke identified himself to Savage as a DEA agent and said that he thought the truck was loaded with marihuana. Cooke twice sought permission to search the camper, but Savage declined to give it, explaining that he was not the owner of the truck. Cooke then stepped on the rear of the truck and, observing that it did not sink any lower, confirmed his suspicion that it was probably overloaded. He put his nose against the rear window, which was covered from the inside, and reported that he could smell marihuana. Without seeking Savage’s permission, Cooke removed the keys from the ignition, opened the rear of the camper, and observed a large number of burlap-wrapped bales resembling bales of marihuana that Cooke had seen in previous investigations. Agent Cooke then placed Savage under arrest and left him with Thrasher.</p>
<p id="b735-6">Cooke returned to the Pontiac and arrested Sharpe and Davis. Approximately 30 to 40 minutes had elapsed between the time Cooke stopped the Pontiac and the time he returned to arrest Sharpe and Davis. Cooke assembled the various parties and vehicles and led them to the Myrtle Beach police station. That evening, DEA agents took the truck to the Federal Building in Charleston, South Carolina. Several days later, Cooke supervised the unloading of the truck, which contained 43 bales weighing a total of 2,629 pounds. Acting without a search warrant, Cooke had eight randomly selected bales opened and sampled. Chemical tests showed that the samples were marihuana.</p>
<p id="b736-4"><page-number citation-index="1" label="680">*680</page-number>B</p>
<p id="b736-5">Sharpe and Savage were charged with possession of a controlled substance with intent to distribute it in violation of <span class="citation no-link">21 U. S. C. § 841</span>(a)(1) and <span class="citation no-link">18 U. S. C. §2</span>. The United States District Court for the District of South Carolina denied respondents’ motion to suppress the contraband, and respondents were convicted.</p>
<p id="b736-6">A divided panel of the Court of Appeals for the Fourth Circuit reversed the convictions. <em>Sharpe </em>v. <em>United States, </em><span class="citation" data-id="9468447"><a href="/opinion/395186/william-harris-sharpe-v-united-states-of-america-donald-davis-savage-v/" aria-description="Citation for case: William Harris Sharpe v. United States of America, Donald...">660 F. 2d 967</a></span> (1981). The majority assumed that Cooke “had an articulable and reasonable suspicion that Sharpe and Savage were engaged in marijuana trafficking when he and Thrasher stopped the Pontiac and the truck.” <span class="citation" data-id="9468447"><a href="/opinion/395186/william-harris-sharpe-v-united-states-of-america-donald-davis-savage-v/#970" aria-description="Citation for case: William Harris Sharpe v. United States of America, Donald..."><em>Id., </em>at 970</a></span>. But the court held the investigative stops unlawful because they “failed to meet the requirement of brevity” thought to govern detentions on less than probable cause. <em><span class="citation" data-id="9468447"><a href="/opinion/395186/william-harris-sharpe-v-united-states-of-america-donald-davis-savage-v/" aria-description="Citation for case: William Harris Sharpe v. United States of America, Donald...">Ibid.</a></span> </em>Basing its decision solely on the duration of the respondents’ detentions, the majority concluded that “the length of the detentions effectively transformed them into de facto arrests without bases in probable cause, unreasonable seizures under the Fourth Amendment.” <em><span class="citation" data-id="9468447"><a href="/opinion/395186/william-harris-sharpe-v-united-states-of-america-donald-davis-savage-v/" aria-description="Citation for case: William Harris Sharpe v. United States of America, Donald...">Ibid.</a></span> </em>The majority then determined that the samples of marihuana should have been suppressed as the fruit of respondents’ unlawful seizures. <span class="citation" data-id="9468447"><a href="/opinion/395186/william-harris-sharpe-v-united-states-of-america-donald-davis-savage-v/#971" aria-description="Citation for case: William Harris Sharpe v. United States of America, Donald..."><em>Id., </em>at 971</a></span>. As an:alternative basis for its decision, the majority held that the warrantless search of the bales taken from the pickup violated <em>Robbins </em>v. <em>California, </em><span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/" aria-description="Citation for case: Robbins v. California">453 U. S. 420</a></span> (1981). Judge Russell dissented as to both grounds of the majority’s decision.</p>
<p id="b736-7">The Government petitioned for certiorari, asking this Court to review both of the alternative grounds held by the Court of Appeals to justify suppression. We granted the petition, vacated the judgment of the Court of Appeals, and remanded the case for further consideration in the light of the intervening decision in <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982). <em>United States </em>v. <em>Sharpe, </em><span class="citation" data-id="9032980"><a href="/opinion/9039645/united-states-v-sharpe/" aria-description="Citation for case: United States v. Sharpe">457 U. S. 1127</a></span> (1982).</p>
<p id="b737-4"><page-number citation-index="1" label="681">*681</page-number>On remand, a divided panel of the Court of Appeals again reversed the convictions. <span class="citation" data-id="9470889"><a href="/opinion/421705/william-harris-sharpe-v-united-states-of-america-donald-davis-savage-v/" aria-description="Citation for case: William Harris Sharpe v. United States of America, Donald...">712 F. 2d 65</a></span> (1983). The majority concluded that, in the light of <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>, </em>it was required to “disavow” its alternative holding disapproving the warrant-less search of the marihuana bales. But, “[fjinding that <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>does not adversely affect our primary holding” that the detentions of the two defendants constituted illegal seizures, the court readopted the prior opinion as modified. <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ibid.</a></span> </em>The majority declined “to reexamine our principal holding or to reargue the same issues that were addressed in detail in the original majority and dissenting opinions,” reasoning that its action complied with this Court’s mandate. The panel assumed that “[h]ad [this] Court felt that a reversal was in order, it could and would have said so.” <em>Id., </em>at 65, n. 1. Judge Russell again dissented.</p>
<p id="b737-5">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./467/1250/">467 U. S. 1250</a></span> (1984), and we reverse.<footnotemark>2</footnotemark></p>
<p id="b738-3"><page-number citation-index="1" label="682">*682</page-number>) — 1</p>
<p id="AK7q">A</p>
<p id="A0l">The Fourth Amendment is not, of course, a guarantee against <em>all </em>searches and seizures, but only against <em>unreasonable </em>searches and seizures. The authority and limits of the Amendment apply to investigative stops of vehicles such as occurred here. <em>United States </em>v. <em>Hensley, </em><span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/#226" aria-description="Citation for case: United States v. Hensley">469 U. S. 221, 226</a></span> (1985); <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 417</a></span> (1981); <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 663</a></span> (1979); <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878, 880</a></span> (1975). In <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), we adopted a dual inquiry for evaluating the reasonableness of an investigative stop. Under this approach, we examine</p>
<blockquote id="A4U">“whether the officer’s action was justified at its inception, and whether it was reasonably related in scope to the circumstances which justified the interference in the first place.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 20</a></span>.</blockquote>
<p id="AlzC">As to the first part of this inquiry, the Court of Appeals assumed that the police had an articulable and reasonable suspicion that Sharpe and Savage were engaged in marihuana trafficking, given the setting and all the circumstances when the police attempted to stop the Pontiac and the pickup. <span class="citation" data-id="9468447"><a href="/opinion/395186/william-harris-sharpe-v-united-states-of-america-donald-davis-savage-v/#970" aria-description="Citation for case: William Harris Sharpe v. United States of America, Donald...">660 F. 2d, at 970</a></span>. That assumption is abundantly supported by the record.<footnotemark>3</footnotemark> As to the second part of the in<page-number citation-index="1" label="683">*683</page-number>quiry, however, the court concluded that the 30- to 40-minute detention of Sharpe and the 20-minute detention of Savage “failed to meet the [Fourth Amendment’s] requirement of brevity.” <em><span class="citation" data-id="9468447"><a href="/opinion/395186/william-harris-sharpe-v-united-states-of-america-donald-davis-savage-v/" aria-description="Citation for case: William Harris Sharpe v. United States of America, Donald...">Ibid.</a></span></em></p>
<p id="b739-4">It is not necessary for us to decide whether the length of Sharpe’s detention was unreasonable, because that detention bears no causal relation to Agent Cooke’s discovery of the marihuana. The marihuana was in Savage’s pickup, not in Sharpe’s Pontiac; the contraband introduced at respondents’ trial cannot logically be considered the “fruit” of Sharpe’s detention. The only issue in this case, then, is whether it was reasonable under the circumstances facing Agent Cooke and Officer Thrasher to detain Savage, whose vehicle contained the challenged evidence, for approximately 20 minutes. We conclude that the detention of Savage clearly meets the Fourth Amendment’s standard of reasonableness.</p>
<p id="b739-5">The Court of Appeals did not question the reasonableness of Officer Thrasher’s or Agent Cooke’s conduct during their detention of Savage. Rather, the court concluded that the length of the detention alone transformed it from a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop into a <em>defacto </em>arrest. Counsel for respondents, as <em>ami-cus curiae, </em>assert that conclusion as their principal argument before this Court, relying particularly upon our decisions in <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979); <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U. S. 491</a></span> (1983); and <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983). That reliance is misplaced.</p>
<p id="b739-6">In <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>, </em>the police picked up a murder suspect from a neighbor’s home and brought him to the police station, where, after being interrogated for an hour, he confessed. <page-number citation-index="1" label="684">*684</page-number>The State conceded that the police lacked probable cause when they picked up the suspect, but sought to justify the warrantless detention and interrogation as an investigative stop. The Court rejected this argument, concluding that the defendant’s detention was “in important respects indistinguishable from a traditional arrest.” <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#212" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 212</a></span>. <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span> </em>is simply inapposite here: the Court was not concerned with the length of the defendant’s detention, but with .events occurring during the detention.<footnotemark>4</footnotemark></p>
<p id="b740-5">In <em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span>, </em>government agents stopped the defendant in an airport, seized his luggage, and took him to a small room used for questioning, where a search of the luggage revealed narcotics. The Court held that the defendant’s detention constituted an arrest. See <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#503" aria-description="Citation for case: Florida v. Royer">460 U. S., at 503</a></span> (plurality opinion); <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#509" aria-description="Citation for case: Florida v. Royer"><em>id., </em>at 509</a></span> (Powell, J., concurring); <em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">ibid.</a></span> </em>(Brennan, J., concurring in result). As in <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>, </em>though, the focus was primarily on facts other than the duration of the defendant’s detention — particularly the fact that the police confined the defendant in a small airport room for questioning.</p>
<p id="b740-6">The plurality in <em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span> </em>did note that “an investigative detention must be temporary and last no longer than is necessary to effectuate the purpose of the stop.” <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer">460 U. S., at 500</a></span>. The Court followed a similar approach in <em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>. </em>In that case, law enforcement agents stopped the defendant after his arrival in an airport and seized his luggage for 90 minutes to take it to a narcotics detection dog for a “sniff test.” We decided that an investigative seizure of personal property could be justified under the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>doctrine, but that “[t]he length of the detention of respondent’s luggage alone precludes the conclusion that the seizure was reasonable in the absence of probable cause.” <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place">462 U. S., at 709</a></span>. However, the rationale underlying that conclusion was premised on the fact that the police knew of respondent’s arrival time <page-number citation-index="1" label="685">*685</page-number>for several hours beforehand, and the Court assumed that the police could have arranged for a trained narcotics dog in advance and thus avoided the necessity of holding respondent’s luggage for 90 minutes. “[I]n assessing the effect of the length of the detention, we take into account whether the police diligently pursue their investigation.” <em>Ibid.; </em>see also <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer"><em>Royer, supra, </em>at 500</a></span>.</p>
<p id="b741-5">Here, the Court of Appeals did not conclude that the police acted less than diligently, or that they <em>unnecessarily </em>prolonged Savage’s detention. <em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span> </em>and <em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span> </em>thus provide no support for the Court of Appeals’ analysis.</p>
<p id="b741-6">Admittedly, <em>Terry, Dunaway, Royer, </em>and <em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>, </em>considered together, may in some instances create difficult line-drawing problems in distinguishing an investigative stop from a <em>de facto </em>arrest. Obviously, if an investigative stop continues indefinitely, at some point it can no longer be justified as an investigative stop. But our cases impose no rigid time limitation on <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stops. While it is clear that “the brevity of the invasion of the individual’s Fourth Amendment interests is an important factor in determining whether the seizure is so minimally intrusive as to be justifiable on reasonable suspicion,” <em>United States </em>v. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place"><em>Place, supra, </em>at 709</a></span>, we have emphasized the need to consider the law enforcement purposes to be served by the stop as well as the time reasonably needed to effectuate those purposes. <em>United States </em>v. <em>Hensley, </em><span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/#228" aria-description="Citation for case: United States v. Hensley">469 U. S., at 228-229, 234-235</a></span>; <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place"><em>Place, supra, </em>at 703-704, 709</a></span>; <em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#700" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 700</a></span>, and n. 12 (1981) (quoting 3 W. LaFave, Search and Seizure § 9.2, pp. 36-37 (1978)). Much as a “bright line” rule would be desirable, in evaluating whether an investigative detention is unreasonable, common sense and ordinary human experience must govern over rigid criteria.</p>
<p id="b741-7">We sought to make this clear in <em>Michigan </em>v. <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers, supra:</a></span></em></p>
<blockquote id="b741-8">“If the purpose underlying a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop — investigating possible criminal activity — is to be served, the police must under certain circumstances be able to detain the <page-number citation-index="1" label="686">*686</page-number>individual for longer than the brief time period involved in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>and <em>Adams </em>[v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span> (1972)].” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#700" aria-description="Citation for case: Michigan v. Summers">452 U. S., at 700, n. 12</a></span>.</blockquote>
<p id="b742-5">Later, in <em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>, </em>we expressly rejected the suggestion that we adopt a hard-and-fast time limit for a permissible <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop:</p>
<blockquote id="b742-6">“We understand the desirability of providing law enforcement authorities with a clear rule to guide their conduct. Nevertheless, we question the wisdom of a rigid time limitation. Such a limit would undermine the equally important need to allow authorities to graduate their responses to the demands of any particular situation.” <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place">462 U. S., at 709, n. 10</a></span>.</blockquote>
<p id="b742-7">The Court of Appeals’ decision would effectively establish a <em>per se </em>rule that a 20-minute detention is too long to be justified under the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>doctrine. Such a result is clearly and fundamentally at odds with our approach in this area.</p>
<p id="b742-8">B</p>
<p id="b742-9">In assessing whether a detention is too long in duration to be justified as an investigative stop, we consider it appropriate to examine whether the police diligently pursued a means of investigation that was likely to confirm or dispel their suspicions quickly, during which time it was necessary to detain the defendant. See <em>Michigan </em>v. <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#701" aria-description="Citation for case: Michigan v. Summers"><em>Summers, supra, </em>at 701</a></span>, n. 14 (quoting 3 W. LaFave, Search and Seizure § 9.2, p. 40 (1978)); see also <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place">462 U. S., at 709</a></span>; <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer">460 U. S., at 500</a></span>. A court making this assessment should take care to consider whether the police are acting in a swiftly developing situation, and in such cases the court should not indulge in unrealistic second-guessing. See generally <em>post, </em>at 712-716 (Brennan, J., dissenting). A creative judge engaged in <em>post hoc </em>evaluation of police conduct can almost always imagine <page-number citation-index="1" label="687">*687</page-number>some alternative means by which the objectives of the police might have been accomplished. But “[t]he fact that the protection of the public might, in the abstract, have been accomplished by ‘less intrusive’ means does not, by itself, render the search unreasonable.” <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#447" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 447</a></span> (1973); see also <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#557" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 557, n. 12</a></span> (1976). The question is not simply whether some other alternative was available, but whether the police acted unreasonably in failing to recognize or to pursue it.</p>
<p id="b743-5">We readily conclude that, given the circumstances facing him, Agent Cooke pursued his investigation in a diligent and reasonable manner. During most of Savage’s 20-minute detention, Cooke was attempting to contact Thrasher and enlisting the help of the local police who remained with Sharpe while Cooke left to pursue Officer Thrasher and the pickup. Once Cooke reached Officer Thrasher and Savage,<footnotemark>5</footnotemark> he proceeded expeditiously: within the space of a few minutes, he examined Savage’s driver’s license and the truck’s bill of sale, requested (and was denied) permission to search the truck, stepped on the rear bumper and noted that the truck did not move, confirming his suspicion that it was probably overloaded. He then detected the odor of marihuana.</p>
<p id="b743-6">Clearly this case does not involve any delay unnecessary to the legitimate investigation of the law enforcement officers. Respondents presented no evidence that the officers were dilatory in their investigation. The delay in this case was <page-number citation-index="1" label="688">*688</page-number>attributable almost entirely to the evasive actions of Savage, who sought to elude the police as Sharpe moved his Pontiac to the side of the road.<footnotemark>6</footnotemark> Except for Savage’s maneuvers, only a short and certainly permissible pre-arrest detention would likely have taken place. The somewhat longer detention was simply the result of a “graduate[d] . . . respons[e] to the demands of [the] particular situation,” <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place"><em>Place, supra, </em>at 709, n. 10</a></span>.</p>
<p id="b744-4">We reject the contention that a 20-minute stop is unreasonable when the police have acted diligently and a suspect’s actions contribute to the added delay about which he complains. The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b744-5">
<em>Reversed and remanded.</em>
</p>
<footnote label="1">
<p id="A2Y"> Officer Thrasher testified that the respondents’ vehicles turned off the highway “[a]bout one minute” after he joined the procession. 4 Record 141. <page-number citation-index="1" label="682">*682</page-number>principle is wholly irrelevant when the defendant has had his conviction nullified and the government seeks review here. Thus, when confronted with precisely this situation in <em>Florida </em>v. <em>Rodriguez, </em><span class="citation" data-id="9429786"><a href="/opinion/111280/florida-v-rodriguez/" aria-description="Citation for case: Florida v. Rodriguez">469 U. S. 1</a></span> (1984) <em>(per curiam), </em>we did not hesitate to reach and decide the merits of the case; had we thought that we should decline to reach every constitutional issue that <em>might </em>become moot, we would have denied certiorari. Cf. <em>Eisler </em>v. <em>United States, </em><span class="citation" data-id="9420393"><a href="/opinion/104717/eisler-v-united-states/#194" aria-description="Citation for case: Eisler v. United States">338 U. S. 189, 194</a></span> (1949) (Murphy, J., dissenting) (“That the ease may become moot if a defendant does not return does not distinguish it from any other case we decide. For subsequent events may render any decision nugatory”).</p>
</footnote>
<footnote label="2">
<p id="b737-6"> We granted certiorari on June 18, 1984. On August 27, counsel for respondents notified the Court that respondents had become fugitives. On October 1, we directed counsel for respondents to file a brief as <em>amicus curiae </em>in support of affirmance of the Court of Appeals’ judgment. Because our reversal of the Court of Appeals’ judgment may lead to the reinstatement of respondents’ convictions, respondents’ fugitive status does not render this case moot. See <em>United States </em>v. <em>Villamonte-Marquez, </em><span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/#581" aria-description="Citation for case: United States v. Villamonte-Marquez">462 U. S. 579, 581-582, n. 2</a></span> (1983); <em>Molinaro </em>v. <em>New Jersey, </em><span class="citation" data-id="108028"><a href="/opinion/108028/molinaro-v-new-jersey/#366" aria-description="Citation for case: Molinaro v. New Jersey">396 U. S. 365, 366</a></span> (1970) <em>(per curiam).</em></p>
<p id="b737-7">Justice Stevens would have this Court adopt a rule that, whenever a respondent or appellee before the Court becomes a fugitive before we render a decision, we must vacate the judgment under review and remand with directions to dismiss the appeal. This theory is not supported by our precedents, and indeed would be a break with a recent decision. The line of authority upon which the dissent relies concerns the situation in which a fugitive defendant is the party seeking review here. In those very different cases, dismissal of the petition or appeal is based on the equitable principle that a fugitive from justice is “disentitled” to call upon this Court for a review of his conviction. See <em>United States </em>v. <em>Campos-Serrano, </em><span class="citation" data-id="9424706"><a href="/opinion/108419/united-states-v-campos-serrano/#294" aria-description="Citation for case: United States v. Campos-Serrano">404 U. S. 293, 294-295, n. 2</a></span> (1971); <span class="citation" data-id="108028"><a href="/opinion/108028/molinaro-v-new-jersey/#366" aria-description="Citation for case: Molinaro v. New Jersey"><em>Molinaro, supra, </em>at 366</a></span>; see also <em>Estelle </em>v. <em>Dorrough, </em><span class="citation" data-id="9426020"><a href="/opinion/109213/estelle-v-dorrough/#541" aria-description="Citation for case: Estelle v. Dorrough">420 U. S. 534, 541-542</a></span> (1975) <em>(per curiam). </em>This equitable</p>
</footnote>
<footnote label="3">
<p id="AT5"> Agent Cooke had observed the vehicles traveling in tandem for 20 miles in an area near the coast known to be frequented by drug traffickers. Cooke testified that pickup trucks with camper shells were' often used to <page-number citation-index="1" label="683">*683</page-number>transport large quantities of marihuana. App. 10. Savage’s pickup truck appeared to be heavily loaded, and the windows of the camper were covered with a quilted bed-sheet material rather than curtains. Finally, both vehicles took evasive actions and started speeding as soon as Officer Thrasher began following them in his marked car. See n. 1, <em>supra. </em>Perhaps none of these facts, standing alone, would give rise to a reasonable suspicion; but taken together as appraised by an experienced law enforcement officer, they provided clear justification to stop the vehicles and pursue a limited investigation.</p>
</footnote>
<footnote label="4">
<p id="b740-7"> The pertinent facts relied on by the Court in <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span> </em>were that (1) the defendant was taken from a private dwelling; (2) he was transported unwillingly to the police station; and (3) he there was subjected to custodial interrogation resulting in a confession. See <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#212" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 212</a></span>.</p>
</footnote>
<footnote label="5">
<p id="b743-7"> It was appropriate for Officer Thrasher to hold Savage for the brief period pending Cooke’s arrival. Thrasher could not be certain that he was aware of all of the facts that had aroused Cooke’s suspicions; and, as a highway patrolman, he lacked Cooke’s training and experience in dealing with narcotics investigations. In this situation, it cannot realistically be said that Thrasher, a state patrolman called in to assist a federal agent in making a stop, acted unreasonably because he did not release Savage based solely on his own limited investigation of the situation and without the consent of Agent Cooke.</p>
</footnote>
<footnote label="6">
<p id="b744-11"> Even if it could be inferred that Savage was not attempting to elude the police when he drove his car <em>between </em>Thrasher’s patrol car and Sharpe’s Pontiac — in the process nearly hitting the patrol car, see App. 17, 37 — such an assumption would not alter our analysis or our conclusion. The significance of Savage’s actions is that, whether innocent or purposeful, they made it necessary for Thrasher and Cooke to split up, placed Thrasher and Cooke out of contact with each other, and required Cooke to enlist the assistance of local police before he could join Thrasher and Savage.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Small.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Small
type: case
citation: "944 F.3d 490 (2019)"
parallel_cite: ""
neutral_cite: ""
court: 4th Cir.
court_level: coa
circuit: ca4
year: 2019
date_decided: 2019-12-06
docket: 18-4327
authority_weight: "Binding in-circuit — 4th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4684957/united-states-v-dontae-small/"
  cluster_id: 4684957
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Small
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Abandonment]]"
    role: Key
related:
  - "[[Abandonment]]"
  - "[[California v. Greenwood]]"
  - "[[Abel v. United States]]"
  - "[[Riley v. California]]"
  - "[[Katz v. United States]]"
tags:
  - case
  - fourth-amendment
  - abandonment
  - reasonable-expectation-of-privacy
  - cell-phone
  - digital-privacy
  - fourth-circuit
holding: "A person who intentionally discards property to evade capture abandons any reasonable expectation of privacy in it, and abandonment is assessed on the objective information available to officers at the time of the search, so where Small crashed through a security gate, fled on foot, and threw down his cell phone along with other belongings, the warrantless searches of the phone did not violate the Fourth Amendment and Riley did not preserve the phone's digital contents once the physical device was abandoned."
aliases:
  - United States v. Small
  - "United States v. Small (4th Cir. 2019)"
---

# United States v. Small

*944 F.3d 490 (4th Cir. 2019)* (No. 18-4327) · U.S. Court of Appeals for the Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4684957 → lead opinion 4462210 (944 F.3d 490, decided 2019-12-06); Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — the CL opinion text is slip/paragraph-paginated). S9 promotes. -->

## Background
After crashing a vehicle through the gates of the National Security Agency at Fort Meade, Dontae Small fled on foot as the facility went into lockdown. During the ensuing manhunt, search personnel found items strewn along his path: a bloody shirt and hat near the crashed car, and — several hours later, around 5:00 a.m. — a cell phone lying about fifty yards away in a grassy area, not where a person would ordinarily set a phone down. Officers conducted warrantless searches of the phone, recovering location data and text messages later used against Small. He moved to suppress, arguing the searches violated the Fourth Amendment; the district court denied the motion, finding that Small had abandoned the phone, and he was convicted.

## Issue
Whether a fleeing suspect who discards his cell phone during flight retains a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the device — and in its digital contents — such that the warrantless searches of the phone violated the Fourth Amendment.

## Rule
Abandonment is an exception to the warrant requirement, and it turns not on formal property law but on whether the person retained a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the thing said to be abandoned, judged from the objective facts known to officers when they searched. As the panel put it: "A finding of abandonment is based 'not [on] whether all formal property rights have been relinquished, but whether the complaining party retains a reasonable expectation of privacy in the articles alleged to be abandoned.'" — 944 F.3d 490, slip op. at 18. ^pin-op18

## Application
The objective circumstances made the district court's abandonment finding sensible: Small fled from police after crashing through a secure gate where he had no right to be, leaving behind his car, a shirt, and a hat, and then his phone turned up nearby in a grassy area rather than somewhere a person's phone would ordinarily rest. A fleeing suspect has an obvious motive to ditch a phone whose GPS could lead officers to him, and shirts and hats do not fall off by accident at the same moments a car is abandoned. On those facts, known to the searchers at the time, Small no longer had a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the phone. Invoking Riley, Small argued that even if he abandoned the physical device he did not abandon its digital contents, but the court rejected the distinction: Riley itself recognized that case-specific exceptions may still justify a warrantless search of a phone, and abandonment is such an exception.

## Conclusion
The denial of suppression was **affirmed**: by deliberately discarding his phone during flight, Small relinquished his [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in both the device and its contents.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Small* carries the classic *[[Abandonment]]* doctrine — property discarded in flight loses Fourth Amendment protection (*[[California v. Greenwood|Greenwood]]*, *[[Abel v. United States|Abel]]*) — into the digital age: abandoning a **phone** abandons the expectation of privacy in its **data**, and *[[Riley v. California|Riley]]*'s warrant rule for [[Search Incident to Arrest|searches incident to arrest]] does not resurrect that expectation. Teach the objective, time-of-search inquiry and the physical-device-versus-digital-contents argument the court rejected.

## Appears on
- [[Abandonment]] — *Key*

## Sources
- [*United States v. Small*, 944 F.3d 490 (4th Cir. 2019)](https://www.courtlistener.com/opinion/4684957/united-states-v-dontae-small/) — pinpoint: slip op. at 18 (abandonment turns on retained expectation of privacy, judged on objective facts at the time of search; the CL opinion text carries slip/paragraph pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3e98a92f0be21689", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Small"}, "payload": {"all": [{"cite": "944 F.3d 490", "page": "490", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "944"}], "display": "944 F.3d 490", "official": {"cite": "944 F.3d 490", "page": "490", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "944"}, "official_selection_present": true, "record_id": "United States v. Small"}}
{"assertion_id": "b7831b08c9a0491f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Small"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Small", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Small

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Small",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Dontae Small",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Small",
    "court": "4th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca4",
    "state": null,
    "date_decided": "2019-12-06",
    "year": 2019,
    "docket": "18-4327",
    "cluster_id": 4684957,
    "lead_opinion_id": 4462210,
    "sibling_ids": [],
    "absolute_url": "/opinion/4684957/united-states-v-dontae-small/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "944 F.3d 490",
      "volume": "944",
      "reporter": "F.3d",
      "page": "490",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "944 F.3d 490",
        "volume": "944",
        "reporter": "F.3d",
        "page": "490",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "944 F.3d 490",
    "official_selection": {
      "court_class": "coa",
      "selected": "944 F.3d 490",
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
    "date_created": "2026-07-07T18:17:58Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:17:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:17:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:17:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:17:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-small--4684957",
      "to_record_id": "United States v. Small",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Small

```
                                     PUBLISHED

                      UNITED STATES COURT OF APPEALS
                          FOR THE FOURTH CIRCUIT


                                     No. 18-4327


UNITED STATES OF AMERICA,

            Plaintiff – Appellee,

v.

DONTAE SMALL,

            Defendant – Appellant.



Appeal from the United States District Court for the District of Maryland, at Baltimore.
James K. Bredar, Chief District Judge. (1:16-cr-00086-JKB-1)


Argued: October 31, 2019                                   Decided: December 6, 2019


Before WILKINSON, KING, and HARRIS, Circuit Judges.


Affirmed by published opinion. Judge Wilkinson wrote the opinion, in which Judge King
and Judge Harris joined.


ARGUED: Brandon Lee Boxler, GIBSON, DUNN & CRUTCHER LLP, Washington,
D.C., for Appellant. Sandra Wilkinson, OFFICE OF THE UNITED STATES
ATTORNEY, Baltimore, Maryland, for Appellee. ON BRIEF: Paresh S. Patel, OFFICE
OF THE FEDERAL PUBLIC DEFENDER, Greenbelt, Maryland; David J. Debold, Travis
S. Andrews, Raymond D. Moss Jr., GIBSON, DUNN & CRUTCHER LLP, Washington,
D.C., for Appellant. Robert K. Hur, United States Attorney, Paul A. Riley, Assistant
United States Attorney, Charles Kassir, Law Clerk, OFFICE OF THE UNITED STATES
ATTORNEY, Baltimore, Maryland, for Appellee.




                                       2
WILKINSON, Circuit Judge:

       Following a six-day trial, a jury in the United States District Court for the District

of Maryland found defendant-appellant Dontae Small guilty of federal carjacking, in

violation of 18 U.S.C. § 2119(1); conspiracy to commit carjacking, in violation of 18

U.S.C. § 371; and destruction of government property, in violation of 18 U.S.C. § 1361.

       In the proceedings below, Small made several motions relevant to the instant appeal,

all of which were denied by the district court: (1) a motion for judgment of acquittal on the

carjacking and conspiracy charges; (2) a motion to suppress evidence related to a cell phone

search; and (3) a motion to excuse and question two jurors on Sixth Amendment grounds.

Small now appeals these denials and requests that we vacate his convictions. Because we

conclude that the district court did not err in denying these motions, Small’s convictions

are affirmed.

                                             I.

                                             A.

       On October 4, 2015, Baltimore resident Brandon Rowe turned around and saw “a

gun in my face.” J.A. 181. Rowe and his fiancée had just returned from vacation to their

house in Baltimore’s Federal Hill neighborhood. It was after 10:00 pm, and there were no

open parking spots in front of their home. They double-parked and quickly unloaded their

car, a silver Acura TSX. Then Rowe drove off alone in search of parking while his fiancée

went into the house. He parked the car in a spot roughly a block away and began walking

back. Within a minute, Rowe was confronted by three masked men, one armed with a “gray

silver gun.” J.A. 182. The gunman demanded that Rowe hand over everything he had.

                                             3
Rowe responded that he had only two sets of keys on him, his car keys and house keys. He

handed over his car keys but told his assailants that he wasn’t giving them his house keys.

The men patted Rowe down and felt his pockets to confirm that he had nothing else of

value. Throughout this entire interaction, the gun remained pointed at Rowe’s face.

       After taking Rowe’s car keys, the gunman ordered Rowe to follow his assailants,

who were walking toward the parked car. Rowe refused and instead turned around and

walked home. His assailants did not pursue him. Rowe called 911 after arriving home, and

officers responded rapidly. Later that night, Rowe was driven past the spot where he had

parked his Acura. The car was gone.

       Shortly before Rowe was confronted by his three masked assailants, an armed

robbery took place in the same neighborhood. Around 10:00 pm, Hannah Caswell and Joe

Dougherty were walking home from dinner. As Caswell and Dougherty were passing a

white minivan parked on the street, a masked man holding a silver gun stepped out in front

of them and blocked their path. He held the gun to Caswell’s head and demanded that

Caswell and Dougherty empty their pockets. When Dougherty refused to hand anything

over “until the gunmen took the gun out of [Caswell’s] face,” J.A. 238, a second man came

from behind the minivan and ripped open Dougherty’s pocket, causing his cell phone to

fall to the ground. The gunman picked up the phone and both assailants took off running.

The white minivan pulled out of its parking spot and followed. Dougherty and Caswell

used a neighbor’s phone to call the police. Their descriptions of the silver gun and the

assailants were consistent with Rowe’s.

                                            B.

                                            4
       On October 7, 2015, three days after the armed robbery and carjacking, a man later

identified as Dontae Small drove a silver Acura into the Arundel Mills Mall parking lot

shortly after 8:00 pm. Security cameras on the premises scanned the car’s license plate,

which revealed that it was Rowe’s stolen Acura. Police were called, and officers from the

Anne Arundel County Police Department set up a perimeter around the parked car and

waited for its driver to return. Small returned to the parking lot at approximately 8:50 pm,

unlocked the Acura, and got into the driver’s seat. At this point, one of the officers pulled

his marked squad car behind the Acura and activated his emergency equipment.

       Rather than surrender, Small drove the Acura over a curb and fled the scene.

Numerous officers followed in pursuit, and a high-speed chase ensued. After driving for

nearly five miles, Small sped through the outbound gate at Fort Meade. Once inside Fort

Meade, and with law enforcement still in pursuit, Small drove through a fence surrounding

the National Security Agency (“NSA”) facility and crashed down an embankment. Though

officers arrived at the scene of the crash “within [a] minute,” Small had disappeared. J.A.

63. Small would not be found until he emerged from a nearby sewer around 10:00 am the

following morning.

       Unable to immediately locate the driver of the Acura, police called for backup and

began to set up a perimeter. Beginning at around 10:00 pm and continuing for over twelve

hours, approximately 200 state and federal officers conducted an extensive search of the

area. Appellant’s Opening Br. at 9. During this time, the NSA was put “on a lock down”

until authorities could locate the driver. Appellee’s Br. at 28 (quoting Aff. in Supp. Search

Warrant, Dist. Ct. Docket #25, Ex. A).

                                             5
         Though the authorities did not immediately locate Small, they did find several items

of interest while searching the NSA grounds. At 1:45 am, officers found a black hat and a

white t-shirt stained with blood near the crash site. Later, at 4:52 am, search personnel

discovered a cell phone on the ground approximately fifty yards from the bloody shirt and

hat. J.A. 30, 32-33. Detective William Bailey of the Baltimore City Police Department, the

lead investigator on Rowe’s carjacking, retrieved the phone and took it to a “floating

command center.” J.A. 30-31.

         At the command center, NSA Special Agent Kristel Massengale observed that the

cell phone was receiving calls from a person identified on the screen as “Sincere my Wife.”

J.A. 167-68. At 5:18 am, without obtaining a warrant, Agent Massengale used the phone

to call “Sincere” back. Sincere, whose real name is Kimberly Duckfield, informed Agent

Massengale that the phone belonged to her husband, Dontae Small. Police quickly obtained

a photo of Small and found it matched security footage of the driver from the Arundel Mills

Mall. Based on this evidence, police concluded that Small was likely the driver of the stolen

Acura.

         Throughout the early morning hours, officers used the cell phone three more times

without obtaining a warrant. First, at 7:24 am, Detective Bailey called Duckfield and

inquired into whether Small had returned home. Duckfield said no. Next, at 8:21 am,

Duckfield called Small’s phone. Bailey answered and informed Duckfield that police were

looking for Small. Finally, Bailey removed the phone’s back casing and battery to locate

its serial number and other identifying information.



                                              6
       At approximately 10:00 am, Small emerged from the sewer system through a

manhole “a little bit” away from the locations of the crash and scattered items. J.A. 42.

Soon after, Small was spotted by NSA Police Officer Hugh McCall, who asked him to

identify himself. Small responded by fleeing on foot. After a brief chase, Officer McCall

caught Small and placed him under arrest.

       In the weeks following Small’s arrest, the government obtained three search

warrants relating to his cell phone. The warrant applications contained Small’s name and

the phone’s serial number—information that the government had learned from its use of

the phone during the manhunt. The warrants authorized the government to collect: (1) the

call history, text messages, internet browsing history, contacts, and deleted data from

Small’s phone; (2) the historical cell site location data for Small’s phone; and (3) records

of outgoing and incoming calls for a second cell phone that Small’s phone had called on

the day of the robberies. The government relied on evidence obtained pursuant to these

warrants at Small’s trial.

                                            C.

       After his arrest, Small was charged with the carjacking of Rowe’s Acura, in

violation of 18 U.S.C. § 2119(1); conspiracy to commit carjacking, in violation of 18

U.S.C. § 371; and destruction of government property for crashing through the NSA fence,

in violation of 18 U.S.C. § 1361.

       The district court empaneled a jury on October 16, 2017, with Small’s trial set to

begin the following day. The next morning, before proceedings began, jurors 5 and 11

approached the Courtroom Deputy to share their concerns that several individuals had been

                                             7
“watching” them as they exited the jury room the previous evening. J.A. 49. The jurors

noted that at least one of these individuals was carrying a cell phone, though they could not

tell if any videos or photographs were taken. The Courtroom Deputy relayed these concerns

to the district judge.

       In response, the district judge took two steps. First, he ensured that court security

officers (“CSOs”) were posted outside both the courtroom and the jury room. Second, he

directed the Courtroom Deputy to inform jurors 5 and 11 of the additional security

measures and that any further concerns should be brought to the attention of the CSOs or

the Courtroom Deputy. The district judge did not disclose the extra security precautions to

the rest of the jurors, nor did he inform them of jurors 5 and 11’s concerns. He believed

that doing so could cause “more harm than good” by drawing attention to concerns that

were “of a pretty vague nature” and possibly based on “misperceptions.” J.A. 51-52.

Immediately before opening statements, the district judge informed the parties of this

situation. Small’s counsel had no immediate objection to the remedial steps taken by the

district judge.

       Small’s trial commenced as scheduled on October 17. The government presented

testimony from Rowe, Caswell, Dougherty, law enforcement officers involved in the

manhunt at the NSA, a forensic expert in cellular data analysis, and others. Much of this

evidence sought to link Small to Rowe’s carjacking. A friend of Small’s, Jamia Butler,

testified that Small had borrowed a white minivan from her on the day of the carjacking

and armed robbery. She stated that Small told her he would be using the van to give his

associate, Ronald Hall, a ride, and that she saw Small and Hall drive off together that day.

                                             8
Caswell and Dougherty testified about the white minivan present during their robbery. The

government later presented evidence that Hall resembled the gunman who accosted Rowe.

       An expert in cellular analysis testified that Small and Hall’s cell phones were used

in the Federal Hill neighborhood around the time of the carjacking and robbery. Call data

showed that the two were in constant communication that night, exchanging multiple calls

and text messages. Shortly before masked assailants approached Rowe, Small sent Hall a

text message that read: “Get da dude cpming down da st.i parked on . . . .” J.A. 599. The

government also introduced incriminating excerpts from nine calls that Small made from

state custody in 2016. J.A. 458; see, e.g., J.A. 579-80 (“They said it was three people. All

of them had on masks. . . . It was four individuals babe. . . . I was the driver.”). On October

25, 2017, after the trial concluded, the jury found Small guilty of all three counts. He was

sentenced to 324 months in prison.

                                              D.

       During the course of proceedings before the district court, Small made three motions

relevant to the instant appeal. First, at the close of evidence, Small made a motion for a

judgment of acquittal on the carjacking and conspiracy charges on the grounds that the

government had failed to offer evidence sufficient to establish the mens rea element of

carjacking under 18 U.S.C. § 2119. Specifically, he asserted that no reasonable juror could

conclude that he or his coconspirators possessed § 2119’s requisite “intent to cause death

or serious bodily harm” during Rowe’s carjacking. The district court denied Small’s

motion, finding that the government’s evidence with respect to intent was sufficient to send

the question to the jury.

                                              9
       Second, prior to trial, Small filed a motion to suppress evidence derived from or

related to his cell phone. He asserted that the four warrantless searches of his phone violated

the Fourth Amendment, rendering all evidence stemming from those searches—including

his cell phone location data and text messages—inadmissible. 1 The district court denied

Small’s motion, concluding that no warrant was required for the searches because Small

had abandoned his phone.

       Third, shortly after trial began, Small moved to excuse and question jurors 5 and 11,

based on concerns that the incident outside the jury room “would influence their verdicts

in such a way that they would no longer be . . . fair and impartial jurors . . . .” J.A. 87-88.

The district court declined to take either step, finding that the defendant’s requested relief

was not warranted based on the sparse information presented.

       Small now appeals the district court’s denial of these three motions.

                                              II.

                                              A.

       Under 18 U.S.C. § 2119, a person commits the crime of federal carjacking if he or

she, “(1) with intent to cause death or serious bodily harm (2) took a motor vehicle (3) that

had been transported, shipped or received in interstate or foreign commerce (4) from the

person or presence of another (5) by force and violence or intimidation.” United States v.


       1
        At times, the government implies that its limited uses of Small’s phone prior to
obtaining a warrant did not qualify as searches for Fourth Amendment purposes. See
Appellee’s Br. at 14, 26-28. Because this issue was not fully briefed and ultimately does
not impact our holding, we will simply assume for the purposes of our analysis that four
warrantless searches of Small’s phone occurred. Infra Section III.

                                              10
Foster, 507 F.3d 233, 246-47 (4th Cir. 2007) (quoting United States v. Applewhaite, 195

F.3d 679, 685 (3d Cir. 1999)).

       Section 2119’s mens rea component, a specific intent requirement, is satisfied

whether the defendant unconditionally or conditionally “inten[ded] to cause death or

serious bodily harm,” 18 U.S.C. § 2119, during a carjacking. Holloway v. United States,

526 U.S. 1, 8, 12 (1999). That is, the government need not prove that the defendant intended

to cause death or serious harm “if unnecessary to steal the car,” so long as it shows that “at

the moment the defendant demanded or took control over the driver’s automobile the

defendant possessed the intent to seriously harm or kill the driver if necessary to steal the

car . . . .” Id. at 12 (emphasis added).

       To establish conditional intent, the government must provide evidence above and

beyond “an empty threat, or intimidating bluff” made by the defendant during the

carjacking. Holloway, 526 U.S. at 11. Section 2119’s “by force and violence or by

intimidation” actus reus requirement remains distinct from its mens rea requirement: an

empty threat would satisfy the former but not the latter. Id. at 11-12. If the defendant were

unwilling to follow through on an intimidating bluff, then he would lack the intent “to

seriously harm or kill the driver if that action had been necessary to complete the taking of

the car.” Id. With these points in mind, we turn to the facts of the case at hand.

                                              B.

       Small claims that there is insufficient evidence to sustain his conspiracy and

carjacking convictions, and that the district court erred in denying his motion to this effect.

Specifically, Small contends that the government failed to present sufficient evidence for

                                              11
a reasonable juror to find that he or his coconspirators acted with “intent to cause death or

serious bodily harm” as required by 18 U.S.C. § 2119.

       A defendant who challenges the sufficiency of the evidence “faces a heavy burden.”

Foster, 507 F.3d at 245. A jury verdict will be sustained so long as “there is substantial

evidence in the record to support it.” United States v. Wilson, 198 F.3d 467, 470 (4th Cir.

1999). When evaluating the sufficiency of the evidence, “we view the evidence in the light

most favorable to the government,” id., and ask whether “any rational trier of fact could

have found the essential elements of the crime beyond a reasonable doubt,” Jackson v.

Virginia, 443 U.S. 307, 319 (1979) (emphasis in original).

       Small fails to carry his burden. There is substantial evidence in the record from

which a reasonable juror could conclude that Small or his coconspirators intended to

seriously harm or kill Rowe if necessary to steal his vehicle. The facts of this case are

chilling: no ordinary vehicle theft took place here. Rowe was walking alone at night on a

deserted street. He was accosted by three men—wearing masks—one of whom was holding

a gun. The armed assailant demanded everything Rowe had while pointing the gun “in [his]

face.” J.A. 181. The gun would remain trained on Rowe, only a foot from his head,

throughout the entire interaction. Furthermore, the assailants made physical contact with

their victim; when Rowe said he had only keys on him, they “patted [him] down” and “felt

in [his] pockets.” J.A. 182-83. Even after Rowe’s assailants had his car keys, they tried to

make him follow them to another location. All of this evidence allowed the jury to infer

that Small or his coconspirators possessed the intent to seriously harm or kill Rowe if

necessary to steal his car.

                                             12
       Although juries evaluating intent are entitled to consider the entirety of the

circumstances surrounding a carjacking, see United States v. Fekete, 535 F.3d 471, 481

(6th Cir. 2008), two facts are of particular note in the case at hand: (1) an assailant pointed

a gun at Rowe; and (2) an assailant made physical contact with Rowe. First and foremost,

an assailant’s wielding a gun provides a strong indication of intent to inflict bodily harm if

met with resistance, particularly when “the perpetrator[] did not merely display a

gun . . . but rather pointed the gun at the [victim] in demanding car keys and other

possessions.” United States v. Franklin, 545 F. App’x 243, 249 (4th Cir. 2013); see also

United States v. Robinson, 855 F.3d 265, 269 (4th Cir. 2017) (finding “plenty of evidence

of . . . intent” when the defendant pointed a gun at the carjacking victim’s head and

threatened her); Foster, 507 F.3d at 247 (finding element of intent satisfied when the

defendant held a gun to the victim’s head, ordered him out of the car, and refused him

reentry).

       In addition, an assailant’s physical touching of a victim during a carjacking—

whether by hand or with a weapon—supports a jury’s finding of intent. See Franklin, 545

F. App’x at 249 (finding that a defendant’s “‘grop[ing]’ [of] one of the vehicle’s passengers

[while] searching for items to steal” supported the jury’s finding of intent); Fekete, 535

F.3d at 478 (noting that courts often look to “whether there was physical violence or

touching” to determine whether § 2119’s intent requirement is satisfied). And while the

gunman here did not touch his weapon to Rowe’s head, he very nearly did so by pointing

it from only a foot away. See United States v. Adams, 265 F.3d 420, 425 (6th Cir. 2001)

(adopting a general rule that “physically touching a victim with a weapon, standing

                                              13
alone, . . . indicates an intent on the part of the defendant to act violently” as required by

§ 2119); cf. United States v. Bailey, 819 F.3d 92, 97-98 (4th Cir. 2016) (declining to find

§ 2119’s intent element satisfied when the defendant held an object to the victim’s neck

but there was no evidence that it was a weapon).

          Small attempts to undermine the jury’s finding by noting several characteristics of

the carjacking at hand: first, Rowe’s assailants did not verbally threaten him; second, the

government did not present proof that the gun was loaded; and third, Rowe’s assailants did

not harm him when he failed to follow certain instructions. While it is true that these factors

are relevant to intent, none are dispositive. They speak to evidentiary weight, a matter that

belongs with the jury. Jackson, 443 U.S. at 318-19 (“Th[e] [sufficiency of the evidence]

standard gives full play to the responsibility of the trier of fact . . . to weigh the evidence,

and to draw reasonable inferences from basic facts to ultimate facts.”); Robinson, 855 F.3d

at 269.

          Take the lack of verbal threats. While verbally threatening the victim can certainly

help establish intent, see Robinson, 855 F.3d at 269, there is no bar to finding intent in

cases that lack verbal threats, see Foster, 507 F.3d at 247. Indeed, it is difficult to imagine

a more effective threat than holding a gun to someone’s head. A reasonable juror in the

case at hand could well conclude that Rowe’s assailants were letting the gun do the talking.

          Nor does the lack of proof that the gun was loaded decide this case. Fekete, 535

F.3d at 478 (“[T]he issue of whether a carjacker’s firearm was loaded has generally not

been treated by the courts as outcome-dispositive. Rather, the courts have looked at the

totality of the relevant circumstances . . . .”). The carjacking statute does not require the

                                               14
use of a loaded gun; it requires that a defendant have the “intent to cause death or serious

bodily harm.” 18 U.S.C. § 2119; see also Fekete, 535 F.3d at 480. Here, the government

presented testimony from gun owner Caswell and military veteran Dougherty indicating

that their masked assailant’s weapon was real. Rowe believed so as well. And as too many

crime victims know, even an unloaded firearm is capable of causing harm. See Fekete, 535

F.3d at 480 (noting the danger of pistol-whipping). Based on the evidence presented here,

a reasonable juror could conclude that—even if Rowe’s assailants carried an unloaded

gun—“[they] nonetheless had the requisite conditional intent to cause death or serious

bodily harm by other means (e.g., pistol-whipping or brute force),” id.

       Finally, Small alludes to the fact that Rowe’s assailants did not harm him when he

failed to follow their instructions. But this is not persuasive. Under § 2119, the defendant’s

intent is examined as of “the precise moment he demanded or took control over the car.”

Holloway, 526 U.S. at 8 (emphasis added). Although Rowe refused to give his assailants

his house keys, likely to avoid endangering his fiancée, he turned over his car keys instantly

and without protest. A reasonable juror could conclude that this scenario would have

played out differently, even tragically, if Rowe had also refused to turn over his car keys.

Similarly, while Rowe refused to follow his assailants to an unknown location, this

occurred after he had already handed over his car keys. A reasonable juror could conclude

that Rowe’s assailants felt no need to harm him at that point because they already had

something of value—his car keys.

       Small next argues that a finding of intent in the case at hand would place our circuit

in conflict with others. As Small notes, two circuits have held that merely brandishing a

                                             15
gun is insufficient as a matter of law to demonstrate an “intent to cause death or serious

bodily harm,” 18 U.S.C. § 2119. Fekete, 535 F.3d at 480-81 (“[I]n the absence of a physical

touching or direct proof that the firearm was loaded, the government must establish

‘brandishing-plus’ in order to satisfy § 2119’s specific intent element.”); United States v.

Randolph, 93 F.3d 656, 664 (9th Cir. 1996) (“We conclude that the brandishing of a

weapon, without more, does not support an inference of specific intent under § 2119.”),

abrogated by Holloway, 526 U.S. 1 (1999).

       As an initial matter, it is unclear that our holding conflicts with those of our sister

circuits. To the extent that “more” than brandishing is required to establish intent, Rowe’s

assailants did not merely “brandish” a gun. They pointed and trained it at his head. They

physically touched Rowe during the carjacking, when they patted him down. As such, the

“brandishing-plus” test from Fekete would not apply: it is used “in the absence of a physical

touching” of the victim. Fekete, 535 F.3d at 478, 480-81. If we have any disagreement with

our sister circuits—and it is not clear we do—it is limited to precisely when the question

of intent switches from one of fact for the jury, see Robinson, 855 F.3d at 269, to one of

law for the courts. Put another way, after a jury has found § 2119’s specific intent

requirement satisfied and returned a verdict of guilty under unexceptional instructions,

when can a court step in and proclaim that no reasonable jury could have reached that very

conclusion? Jurors excel in cases such as this, where they are asked to apply their common

sense to the factual scenario before them. Thus, we have cautioned that “[c]ourts must resist

invading the jury’s province by transforming questions of fact into matters of law.”

Robinson, 855 F.3d at 269. We decline to invade the jury’s province here. The carjacking

                                             16
and conspiracy charges against Small were properly submitted to the jury, and the jury

returned a verdict of guilty.

       Jury verdicts are entitled to respect. The jury here found that Small or his

coconspirators possessed the “intent to cause death or serious bodily harm,” 18 U.S.C.

§ 2119, when in the course of taking his car they demanded at gunpoint that Rowe hand

over everything he had. We decline to overturn the jury’s conclusion on this question of

fact, since “it is clearly the jury’s duty, not ours, to decide it.” Robinson, 855 F.3d at 269.

                                              III.

                                              A.

       We next address Small’s Fourth Amendment challenge. The Fourth Amendment

protects “[t]he right of the people to be secure in their persons, houses, papers, and effects,

against unreasonable searches and seizures.” U.S. Const. amend. IV. To safeguard this

right, courts apply an exclusionary rule, which dictates that “evidence obtained in violation

of the Fourth Amendment cannot be used in a criminal proceeding against the victim of

the illegal search and seizure.” United States v. Calandra, 414 U.S. 338, 347-48 (1974).

Although warrantless searches are generally considered “per se unreasonable under the

Fourth Amendment,” this generality is subject “to a few specifically established and well-

delineated exceptions.” Arizona v. Gant, 556 U.S. 332, 338 (2009) (quoting Katz v. United

States, 389 U.S. 347, 357 (1967)). One such exception is abandonment. Abel v. United

States, 362 U.S. 217, 241 (1960) (“There can be nothing unlawful in the Government’s

appropriation of . . . abandoned property.”); United States v. Leshuk, 65 F.3d 1105, 1111

(4th Cir. 1995) (“The law is well established that a person who voluntarily abandons

                                              17
property . . . is consequently precluded from seeking to suppress evidence seized from the

property.”).

       A finding of abandonment is based “not [on] whether all formal property rights have

been relinquished, but whether the complaining party retains a reasonable expectation of

privacy in the articles alleged to be abandoned.” United States v. Haynie, 637 F.2d 227,

237 (4th Cir. 1980) (quoting United States v. Wilson, 472 F.2d 901, 902 (9th Cir. 1973)).

To determine whether the defendant maintains a reasonable expectation of privacy in an

item, the court performs “an objective analysis” which considers the defendant’s actions

and intentions. United States v. Davis, 657 F. Supp. 2d 630, 647-48 (D. Md. 2009), aff’d,

690 F.3d 226 (4th Cir. 2012). “Intent [to abandon] may be inferred from words spoken,

acts done, and other objective facts.” Id. at 648 (quoting United States v. Hoey, 983 F.2d

890, 892 (8th Cir. 1993)).

                                             B.

       Small contends that the district court erred in denying his motion to suppress the

fruits of the warrantless searches of his cell phone. Specifically, Small alleges that there

was insufficient evidence for the court to conclude that the phone was abandoned and that

no warrant was required for the initial searches.

       In reviewing a district court’s denial of a motion to suppress, we review legal

determinations de novo and factual findings for clear error. United States v. Lull, 824 F.3d

109, 114 (4th Cir. 2016). The government bears the burden of proving the admissibility of

evidence obtained pursuant to a warrantless search by a preponderance of evidence. See



                                             18
United States v. Matlock, 415 U.S. 164, 178 n.14 (1974); United States v. Helms, 703 F.2d

759, 763-64, 766 (4th Cir. 1983).

       In determining whether this standard is met, we may consider both the evidence

before the district court at the suppression hearing and “evidence adduced at trial that

support[ed] the district judge’s ruling.” United States v. Han, 74 F.3d 537, 539 (4th Cir.

1996); see also Carroll v. United States, 267 U.S. 132, 162 (1925). Still, there are temporal

limitations on evidence used in our analysis: we evaluate whether the defendant intended

to abandon an item using only objective information available to officers at the time they

performed the warrantless search. United States v. Nowak, 825 F.3d 946, 948 (8th Cir.

2016) (per curiam); Bond v. United States, 77 F.3d 1009, 1013 (7th Cir. 1996). As the

Supreme Court has noted, the reasonableness of a search is evaluated based on “the facts

known to the police” at the time. United States v. Banks, 540 U.S. 31, 39-40 (2003). A

Fourth Amendment search “is good or bad when it starts.” United States v. Di Re, 332 U.S.

581, 595 (1948).

       Abandonment should not be casually inferred. People lose or misplace their cell

phones all the time. But the simple loss of a cell phone does not entail the loss of a

reasonable expectation of privacy. Thus, such ordinary mishaps do not constitute

“abandonments.” Rather, as the district court noted, “[t]here has to be some voluntary

aspect to the circumstances that lead to the phone being what could be called abandoned.”

J.A. 41. Here there clearly was.

       The evidence before the district court depicts a fleeing suspect tossing aside

personal items while attempting to evade capture. Small fled on foot after crashing through

                                             19
the NSA gates, leaving his vehicle and its contents behind. Search personnel would

continue to find Small’s personal items strewn about during the manhunt. At 1:45 am,

officers located a bloody shirt and hat in the vicinity of the crashed car. The obvious

conclusion is that these items—or, at the very least, the shirt—were purposefully removed

and tossed aside. Several hours later, around 5:00 am, officers located a cell phone only

fifty yards from the shirt and hat. The phone was found in a grassy area, not on a sidewalk

or “a place where [someone] normally might be.” J.A. 43.

       Based on these circumstances, the district court’s inference that Small abandoned

the phone seems sensible. Because a cell phone’s GPS tracking can “lead you to a

defendant,” J.A. 39, it is credible that a fleeing suspect might intentionally discard his

phone. And while phones occasionally slip out of pockets, shirts do not accidentally fall

off their wearers—at the exact same moments as hats—and cars do not ditch themselves

after a crash. The fleeing suspect’s relinquishment of the car, the hat, and the shirt near

where the cell phone was found support the district court’s finding of abandonment.

       The district court relied heavily on these circumstances to reach its conclusion that

Small no longer had a “reasonable expectation of privacy in th[e] phone.” J.A. 42-43. Small

“is fleeing from the police, he crashes through a gate in a place where he is not supposed

to be. He’s clearly left the car. Items are being left behind, the bloody shirt and hat being




                                             20
one of them.” J.A. 42. Further, the court noted that there was no evidence Small attempted

to retrieve his phone at any point, even though it wasn’t password protected. 2

       Evidence gleaned from trial testimony points in the same direction. This testimony

demonstrates why search personnel could reasonably conclude at the time of the search

that the phone belonged to the suspect-at-large. While the government briefly noted at the

suppression hearing that the NSA went on “lockdown” when Small crashed through the

fence, J.A. 27, trial testimony from several search personnel gave a more complete picture

of the scope of the manhunt. The testimony suggests that few people besides the suspect

and search personnel were out-and-about in the hours before the phone was found.

       As trial testimony established, the cell phone was found in a large crime scene, not

in a crowded public area. An Anne Arundel police officer radioed during the car chase for

“aviation assets” and “K-9 assets.” J.A. 74. After Small entered Fort Meade but before he

crashed through the NSA fence, an Army sergeant locked the Fort Meade gates and only

reopened them to allow entry by search personnel. After the crash, an NSA police captain

established a perimeter within the NSA and led a thorough, methodical search for the

suspect. Search personnel could well believe that this phone—located during the early




       2
         Citing Riley v. California, 134 S. Ct. 2473 (2014), Small contends that even if he
abandoned his physical phone, he did not abandon its digital contents. Appellant’s Opening
Br. at 44-45. We do not find this argument persuasive. While Riley held that “the search
incident to arrest exception does not apply to [digital information stored on] cell phones,”
it emphasized that “other case-specific exceptions may still justify a warrantless search of
a particular phone.” 134 S. Ct. at 2493-94. For the reasons noted, this is such a case.

                                            21
morning hours in a grassy area in a facility on lockdown—belonged to the fleeing suspect

who deliberately abandoned it during flight.

       When Small discarded the phone, he ran the risk that complete and total strangers

would come upon it. In tossing his phone, he relinquished his reasonable expectation of

privacy in it as well. The district court’s decision to deny suppression shall be affirmed.

                                             IV.

                                             A.

       The Sixth Amendment guarantees a criminal defendant the right to be tried before

an impartial jury. U.S. Const. amend. VI. In order to safeguard this right, the Supreme

Court has held that “[i]n a criminal case, any private communication, contact, or tampering,

directly or indirectly, with a juror during a trial about the matter pending before the jury

is . . . deemed presumptively prejudicial.” Remmer v. United States, 347 U.S. 227, 229

(1954). If the Remmer presumption is met, the defendant is entitled to an evidentiary

hearing in which the government bears the burden of showing “that such contact . . . was

harmless to the defendant.” Id. at 229-30; Haley v. Blue Ridge Transfer Co., 802 F.2d 1532,

1535 (4th Cir. 1986).

       Because it is difficult to fully shield juries from the outside world, see Smith v.

Phillips, 455 U.S. 209, 217 (1982), we tolerate certain instances of extrajudicial contact

that “amount to nothing more than innocuous interventions that simply could not justify a

presumption of prejudicial effect,” Haley, 802 F.2d at 1537 n.9; see also Stockton v.

Virginia, 852 F.2d 740, 747 (4th Cir. 1988). Thus, in order to trigger Remmer’s

presumption of prejudice, “the defendant must first establish both that an unauthorized

                                             22
contact was made and that it was of such a character as to reasonably draw into question

the integrity of the verdict.” Stockton, 852 F.2d at 743.

       To determine whether a contact was innocuous, we “turn to the [five] factors the

Supreme Court deemed important” in Remmer: “(1) any private communication; (2) any

private contact; (3) any tampering; (4) directly or indirectly with a juror during trial; (5)

about the matter before the jury.” United States v. Cheek, 94 F.3d 136, 141 (4th Cir. 1996).

                                              B.

       The day Small’s trial began, jurors 5 and 11 approached the Courtroom Deputy with

concerns that individuals outside the jury room had been “watching” them when they left

the courthouse the previous evening. J.A. 49. The jurors did not indicate much else. Small

contends that his Sixth Amendment right to an impartial jury was violated by the district

court’s failure to excuse and question jurors 5 and 11. For this reason, he requests that his

convictions be vacated and his case remanded for a new trial.

       We review the district court’s decision not to question or excuse jurors after

allegations of improper contact under “a ‘somewhat narrowed,’ modified abuse of

discretion standard” that allows the appellate court “more latitude to review the trial court’s

conclusion” on the potential for prejudice. Cheek, 94 F.3d at 140 (quoting Haley, 802 F.2d

at 1537 n.11-12); see also United States v. Basham, 561 F.3d 302, 319 (4th Cir. 2009).

       Under this standard, we see nothing problematic about the district court’s denial of

Small’s motion to voir dire and excuse jurors 5 and 11. To invoke the Remmer presumption

and the right to an evidentiary hearing, Small bore the initial burden of “introducing

competent evidence that the extrajudicial communications or contacts were ‘more than

                                              23
innocuous interventions.’” Cheek, 94 F.3d at 141 (quoting Haley, 802 F.2d at 1537 n.9).

He has failed to do so.

       As an initial matter, it is hardly clear that a vague report of “watching,” without

more, constitutes evidence of “extrajudicial communications or contacts,” Cheek, 94 F.3d

at 141; see also United States v. Baptiste, 596 F.3d 214, 220-21 (4th Cir. 2010) (declining

to reach the question of whether stares from a crowd constituted unauthorized contact). We

are unaware of any case where a defendant attempted to invoke the Remmer presumption

based on “watching” alone. “Watching” can hardly be described as “communication” or

“contact,” both of which imply an active exchange of information of some sort.

Unsurprisingly, most precedent discussing extrajudicial contact involves spoken words.

See, e.g., Basham, 561 F.3d at 316, 320 (juror called local news outlets about the trial

before the jury reached a verdict); Stockton, 852 F.2d at 742-43, 746 (local business owner

told the jurors that “they ought to fry the son of a bitch” in a death penalty case). Watching

may be done passively and, unless context indicates otherwise, conveys little information.

       Of course, “watching” may take on an extreme and sinister character, but here there

is no evidence that it was anything “more than [an] innocuous intervention[],” Cheek, 94

F.3d at 141. The episode occurred in a common area of a busy courthouse. There was no

reason for the jurors to associate the unknown individuals with Small. Indeed, there was

no indication that the incident was in any way related to Small’s case, “the matter before

the jury,” Cheek, 94 F.3d at 141.

       “The trial court must be afforded wide discretion in handling matters relating

to . . . the integrity of the jury.” United States v. Johnson, 657 F.2d 604, 606 (4th Cir. 1981).

                                               24
Here the district judge took reasonable steps based on the jurors’ reports. He did not dismiss

or trivialize their concerns. Instead, he increased security around the jury room. Further, he

ensured that jurors 5 and 11 were aware of where to find security personnel, encouraged

them to report any further concerns, and provided clear instructions on how to do so.

       The district judge had good reason to be wary of a more searching inquiry. As he

later noted:

       Stopping a trial to separately voir dire particular jurors about potential
       improper influence has its own potentially deleterious impact. Just that
       questioning process could plant in jurors’ minds the notion that perhaps
       something untoward is afoot. . . . In this case, the totality of the information
       presented to the [c]ourt did not warrant th[is] sort of inquiry . . . .

J.A. 765. We agree. The judge took a measured, thoughtful approach to the jurors’

concerns. These modest steps were proportionate to what the situation required. We find

that the district court did not abuse its discretion by declining to question and excuse jurors

5 and 11.

                                              V.

       For the foregoing reasons, we reject Small’s challenges to the proceedings below

and affirm his convictions.

                                                                                AFFIRMED




                                              25

```

---

## GROUP: _overhaul2/lake/cases/United States v. Smith (2024).json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "United States v. Smith (2024)"
type: case
citation: "110 F.4th 817 (2024)"
parallel_cite: ""
neutral_cite: ""
court: U.S. Court of Appeals for the Fifth Circuit
court_level: coa
circuit: 5th
year: 2024
date_decided: 2024-08-09
docket: 23-60321
authority_weight: "Binding in-circuit — 5th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2026-07-03
  as_of_treatment: 2026-07-03
  composite_basis: principal-holding
  composite_basis_ref: search.digital.geofence-threshold
  varies_by_point: true
  scope_note: "Composite reflects the search-threshold holding (geofence acquisition IS a search), confirmed by Chatrie v. United States (2026). The categorical general-warrant holding is the point that varies — binding in the Fifth Circuit, not adopted by SCOTUS."
  point_overrides:
    - point: search.warrant.geofence-general-warrant
      point_label: Geofence warrants are categorically unconstitutional general warrants
      field_i_validity: caution
      as_of_treatment: 2026-07-03
      s3_binding_status: bound
      by:
        - name: Chatrie v. United States
          cluster_id: 10881683
          cite: "609 U.S. ___ (2026)"
          field_ii: limited
      scope_note: "Binding in the Fifth Circuit; SCOTUS in Chatrie expressly declined to adopt the categorical rule — the probable-cause/particularity of geofence warrants is the live question on Chatrie's remand."
lake:
  record_id: "United States v. Smith (2024)"
  status: verified
  projected_at: 2026-07-06
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10036119/united-states-v-smith/"
  cluster_id: 10036119
  opinion_id: 10502720
  identity_checked: true
homes:
  - page: "[[Reverse-Keyword and Geofence Warrants]]"
    role: "Key — Circuit anchor (geofence)"
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Related (cross-ref — umbrella)"
related: ["[[Chatrie v. United States]]", "[[Carpenter v. United States]]", "[[United States v. Leon]]", "[[The Warrant Requirement]]", "[[The Exclusionary Rule]]"]
aliases: ["United States v. Smith", "United States v. Smith (5th Cir. 2024)"]
tags: ["case", "fourth-amendment", "search", "digital-privacy", "geofence", "location-history", "good-faith-exception"]
holding: "Acquiring Google Location History through a geofence warrant is a Fourth Amendment search under Carpenter, and geofence warrants — which identify everyone in an area rather than a particularized suspect — are modern-day general warrants, unconstitutional under the Fourth Amendment; suppression was nonetheless denied under the Leon good-faith exception given the technology's novelty."
---

# United States v. Smith (2024)

*110 F.4th 817 (5th Cir. 2024)* (No. 23-60321) · U.S. Court of Appeals for the Fifth Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **Good law — varies by point**
<!-- header line; TreatmentBadge + weight render here, degrading to the text above. CL-verified 2026-07-03: cluster 10036119 → opinion 10502720 — see frontmatter/Sources. -->

## Background
On February 5, 2018, three men robbed Sylvester Cobbs, a contract route driver for the U.S. Postal Service, of registered mail bags containing over $60,000 as he arrived at the Lake Cormorant, Mississippi post office. Surveillance video showed the assailant apparently using a cell phone before and after the robbery, but nine months of investigation produced no suspect. Postal inspectors then obtained a **geofence warrant** directing Google to disclose Location History for every device within a roughly 98,000-square-meter box around the post office during the robbery window. The returns led to Jamarr Smith and Gilbert McThunel, and follow-up investigation identified Thomas Iroko Ayodele. A jury convicted all three of robbery and conspiracy; they appealed the denial of their motion to suppress the geofence-derived evidence.

## Issue
Whether obtaining Google Location History through a geofence warrant is a Fourth Amendment search, and whether a warrant that identifies everyone within a geographic area — rather than a particularized suspect — satisfies the Fourth Amendment.

## Rule
Acquiring geofence Location History is a **search** under *[[Carpenter v. United States|Carpenter]]* — the comprehensive, automatically generated record of a phone's movements invades a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] even though Google holds the data. And because a geofence warrant works backwards — identifying every person in an area on the chance one is the suspect, rather than searching a particularized target — the panel held it fails the Fourth Amendment at the threshold: "We hold that geofence warrants are modern-day general warrants and are unconstitutional under the Fourth Amendment. However, considering law enforcement's reasonable conduct in this case in light of the novelty of this type of warrant, we uphold the district court's determination that suppression was unwarranted under the good-faith exception." — 110 F.4th at 838. ^pin-838

## Application
The geofence returns exposed the private movements of everyone near the Lake Cormorant post office, not just the eventual defendants — the inverted, dragnet character the panel found indistinguishable from a general warrant. But the inspectors had consulted prosecutors, obtained a magistrate's authorization, and navigated a genuinely novel technology with no controlling precedent; on those facts the court applied *[[United States v. Leon|Leon]]* good faith rather than the exclusionary rule.

## Conclusion
Convictions **affirmed**: the geofence warrant was unconstitutional, but suppression was unwarranted under the [[The Good-Faith Exception|good-faith exception]]. King, J., wrote for the panel (King, Ho, Engelhardt, JJ.).

## Treatment & subsequent history

**Composite: Good law — treatment varies by point.** *Smith*'s two holdings have diverged: the search-threshold holding is now nationally settled in its favor; the categorical general-warrant holding remains binding only in the Fifth Circuit.

| Point of law | Status | Controlling authority |
|---|---|---|
| Acquiring geofence Location History is a Fourth Amendment search | **Good law** | Confirmed by *[[Chatrie v. United States]]*, 609 U.S. ___ (2026) — SCOTUS reached the same result, applying and extending *[[Carpenter v. United States\|Carpenter]]* |
| Geofence warrants are categorically unconstitutional general warrants | **Caution** | *[[Chatrie v. United States\|Chatrie]]* expressly declined to adopt the categorical rule; the probable-cause/[[Particularity\|particularity]] question is live on *[[Chatrie v. United States\|Chatrie]]*'s remand. Binding in the Fifth Circuit; the persuasive minority position elsewhere |

The Supreme Court's 2026 *[[Chatrie v. United States|Chatrie]]* decision resolved the circuit split *Smith* anchored: acquiring geofence Location History **is** a search, as *Smith* held (and the Fourth Circuit's [[Reading and Citing Cases#en-banc|en banc]] *[[Chatrie v. United States|Chatrie]]* had fractured over). But the Court stopped at the threshold — it did not decide whether any geofence warrant can satisfy probable cause and [[Particularity|particularity]], so *Smith*'s stronger point remains the minority answer to a question SCOTUS left open.

## Appears on
- [[Reverse-Keyword and Geofence Warrants]] — *Key — Circuit anchor (geofence)*
- [[Third-Party Doctrine & CSLI]] — *Related (cross-ref — umbrella)*

## Sources
- [*United States v. Smith*, 110 F.4th 817 (5th Cir. 2024)](https://www.courtlistener.com/opinion/10036119/united-states-v-smith/) — pinpoint: 838 (general-warrant holding + good-faith disposition; quote string-matched against the CL opinion text 2026-07-03).
- [*Chatrie v. United States*, 609 U.S. ___ (2026)](https://www.courtlistener.com/opinion/10881683/chatrie-v-united-states/) — the search-threshold confirmation and the reserved probable-cause/particularity question.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "29dfcadbb182454c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Smith (2024)"}, "payload": {"all": [{"cite": "110 F.4th 817", "page": "817", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "110"}], "display": "110 F.4th 817", "official": {"cite": "110 F.4th 817", "page": "817", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "110"}, "official_selection_present": true, "record_id": "United States v. Smith (2024)"}}
{"assertion_id": "0778d72697459adf", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-838", "record_id": "United States v. Smith (2024)"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-838", "pinpoint_status": "slip-only", "quote": "--- # United States v. Smith (2024) *110 F.4th 817 (5th Cir. 2024)* (No. 23-60321) · U.S. Court of Appeals for the Fifth Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **Good law — varies by point** <!-- header line; TreatmentBadge + weight render here, degrading to the text above. CL-verified 2026-07-03: cluster 10036119 → opinion 10502720 — see frontmatter/Sources. --> ## Background On February 5, 2018, three men robbed Sylvester Cobbs, a contract route driver for the U.S. Postal Service, of registered mail bags containing over $60,000 as he arrived at the Lake Cormorant, Mississippi post office. Surveillance video showed the assailant apparently using a cell phone before and after the robbery, but nine months of investigation produced no suspect. Postal inspectors then obtained a **geofence warrant** directing Google to disclose Location History for every device within a roughly 98,000-square-meter box around the post office during the robbery window. The returns led to Jamarr Smith and Gilbert McThunel, and follow-up investigation identified Thomas Iroko Ayodele. A jury convicted all three of robbery and conspiracy; they appealed the denial of their motion to suppress the geofence-derived evidence. ## Issue Whether obtaining Google Location History through a geofence warrant is a Fourth Amendment search, and whether a warrant that identifies everyone within a geographic area — rather than a particularized suspect — satisfies the Fourth Amendment. ## Rule Acquiring geofence Location History is a **search** under *[[Carpenter v. United States|Carpenter]]* — the comprehensive, automatically generated record of a phone's movements invades a reasonable expectation of privacy even though Google holds the data. And because a geofence warrant works backwards — identifying every person in an area on the chance one is the suspect, rather than searching a particularized target — the panel held it fails the Fourth Amendment at the threshold:", "quote_fidelity": "mismatch", "record_id": "United States v. Smith (2024)", "star_marker": null}}
{"assertion_id": "a4d07ad2599378b0", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Smith (2024)"}, "payload": {"as_of_content": "2026-07-03", "as_of_treatment": "2026-07-03", "field_i_validity": "good_law", "record_id": "United States v. Smith (2024)", "scope_note": "Composite reflects the search-threshold holding (geofence acquisition IS a search), confirmed by Chatrie v. United States (2026). The categorical general-warrant holding is the point that varies — binding in the Fifth Circuit, not adopted by SCOTUS.", "varies_by_point": true}}
```

### lake record — United States v. Smith (2024)

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Smith (2024)",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Smith",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Smith (2024)",
    "court": "U.S. Court of Appeals for the Fifth Circuit",
    "court_id": "ca5",
    "court_level": "coa",
    "circuit": "5th",
    "state": null,
    "date_decided": "2024-08-09",
    "year": 2024,
    "docket": "23-60321",
    "cluster_id": 10036119,
    "lead_opinion_id": 10502720,
    "sibling_ids": [
      10502720
    ],
    "absolute_url": "/opinion/10036119/united-states-v-smith/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "110 F.4th 817",
      "volume": "110",
      "reporter": "F.4th",
      "page": "817",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "110 F.4th 817",
        "volume": "110",
        "reporter": "F.4th",
        "page": "817",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "110 F.4th 817",
    "official_selection": {
      "court_class": "coa",
      "selected": "110 F.4th 817",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-838",
      "page": null,
      "quote": "--- # United States v. Smith (2024) *110 F.4th 817 (5th Cir. 2024)* (No. 23-60321) \u00b7 U.S. Court of Appeals for the Fifth Circuit \u00b7 **Binding in-circuit \u2014 5th Cir.** \u00b7 Treatment: **Good law \u2014 varies by point** <!-- header line; TreatmentBadge + weight render here, degrading to the text above. CL-verified 2026-07-03: cluster 10036119 \u2192 opinion 10502720 \u2014 see frontmatter/Sources. --> ## Background On February 5, 2018, three men robbed Sylvester Cobbs, a contract route driver for the U.S. Postal Service, of registered mail bags containing over $60,000 as he arrived at the Lake Cormorant, Mississippi post office. Surveillance video showed the assailant apparently using a cell phone before and after the robbery, but nine months of investigation produced no suspect. Postal inspectors then obtained a **geofence warrant** directing Google to disclose Location History for every device within a roughly 98,000-square-meter box around the post office during the robbery window. The returns led to Jamarr Smith and Gilbert McThunel, and follow-up investigation identified Thomas Iroko Ayodele. A jury convicted all three of robbery and conspiracy; they appealed the denial of their motion to suppress the geofence-derived evidence. ## Issue Whether obtaining Google Location History through a geofence warrant is a Fourth Amendment search, and whether a warrant that identifies everyone within a geographic area \u2014 rather than a particularized suspect \u2014 satisfies the Fourth Amendment. ## Rule Acquiring geofence Location History is a **search** under *[[Carpenter v. United States|Carpenter]]* \u2014 the comprehensive, automatically generated record of a phone's movements invades a reasonable expectation of privacy even though Google holds the data. And because a geofence warrant works backwards \u2014 identifying every person in an area on the chance one is the suspect, rather than searching a particularized target \u2014 the panel held it fails the Fourth Amendment at the threshold:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2026-07-03",
    "as_of_treatment": "2026-07-03",
    "composite_basis": "principal-holding",
    "composite_basis_ref": "search.digital.geofence-threshold",
    "varies_by_point": true,
    "scope_note": "Composite reflects the search-threshold holding (geofence acquisition IS a search), confirmed by Chatrie v. United States (2026). The categorical general-warrant holding is the point that varies \u2014 binding in the Fifth Circuit, not adopted by SCOTUS.",
    "point_overrides": [
      {
        "point": "search.warrant.geofence-general-warrant",
        "point_label": "Geofence warrants are categorically unconstitutional general warrants",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-07-03",
        "s3_binding_status": "bound",
        "by": [
          {
            "name": "Chatrie v. United States",
            "cluster_id": 10881683,
            "cite": "609 U.S. ___ (2026)",
            "field_ii": "limited"
          }
        ],
        "scope_note": "Binding in the Fifth Circuit; SCOTUS in Chatrie expressly declined to adopt the categorical rule \u2014 the probable-cause/particularity of geofence warrants is the live question on Chatrie's remand."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "State of Minnesota v. Ivan Contreras-Sanchez",
          "cluster_id": 10851595,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Pennington",
          "cluster_id": 10812356,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Porter",
          "cluster_id": 10810059,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Com. v. Walker, J.",
          "cluster_id": 10750016,
          "cite": [
            "2025 Pa. Super. 271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 10680498,
          "cite": [
            "321 Ga. 137"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Com. v. Choice, K.",
          "cluster_id": 10673715,
          "cite": [
            "2025 Pa. Super. 209"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joseph Angel Alvarez v. the State of Texas",
          "cluster_id": 10653315,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "WELLS, AARON RAYSHAN v. the State of Texas",
          "cluster_id": 10373456,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joseph Angel Alvarez v. the State of Texas",
          "cluster_id": 10266245,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Smith (2024):lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(10502720) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca5)",
        "reviewed": 1,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 1,
        "triage_read": 0,
        "triage_snippet_classified": 1
      },
      "lane2_top_cited": {
        "query": "cites:(10502720)",
        "reviewed": 9,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 9,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(10502720)",
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
    "complete_query": "cites:(10502720)",
    "indexed_citing_opinions": 9,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 10502720,
        "count": 9,
        "count_source": "search"
      }
    ],
    "citation_count": 11,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-smith-2024.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 9,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 10502720,
        "cited_id": 12977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 49000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 612472,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 821120,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 4089523,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 4239377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 4256321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 4274911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 4287285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 6943812,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 7268856,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 8408910,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9409113,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9423459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9423552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9424643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9427321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9427638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9428299,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9429558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9429766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9432890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9434540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9434934,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9436658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10502720,
        "cited_id": 9895717,
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
    "date_created": "2026-07-06T03:04:09Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "pre-seeded new-schema treatment (planning-time projection); R6 derivation to confirm",
      "controlling case has no official cite in lake; cite omitted",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:04:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "pre-seeded new-schema treatment (planning-time projection); R6 derivation to confirm",
        "at": "2026-07-06T03:04:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:04:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Smith (2024)

```
Case: 23-60321       Document: 113-1         Page: 1   Date Filed: 08/09/2024




        United States Court of Appeals
             for the Fifth Circuit
                             ____________
                                                                  United States Court of Appeals
                                                                           Fifth Circuit
                               No. 23-60321
                             ____________                                FILED
                                                                    August 9, 2024
United States of America,                                           Lyle W. Cayce
                                                                         Clerk
                                                          Plaintiff—Appellee,

                                    versus

Jamarr Smith; Thomas Iroko Ayodele; Gilbert
McThunel, II,

                                       Defendants—Appellants.
               ______________________________

               Appeal from the United States District Court
                 for the Northern District of Mississippi
                        USDC No. 3:21-CR-107-1
               ______________________________

Before King, Ho, and Engelhardt, Circuit Judges.
King, Circuit Judge:
       A jury found Appellants guilty of robbery and conspiracy to commit
robbery based on evidence obtained through a geofence warrant. On appeal,
Appellants challenge the constitutionality of this novel type of warrant under
the Fourth Amendment and maintain that the district court erred by failing
to suppress all evidence derived therefrom.
       We hold that the use of geofence warrants—at least as described
herein—is unconstitutional under the Fourth Amendment. In doing so, we
part ways with our esteemed colleagues on the Fourth Circuit. See United
Case: 23-60321       Document: 113-1       Page: 2     Date Filed: 08/09/2024




                                  No. 23-60321


States v. Chatrie, 107 F.4th 319 (4th Cir. 2024). With that said, we agree with
the district court that, here, law enforcement acted in good faith in relying on
this type of warrant. Accordingly, we AFFIRM the district court’s denial of
Appellants’ motion to suppress.
                   I. Factual & Procedural Background
                           A. Underlying Offense
       On February 5, 2018, three individuals acting in concert robbed
Sylvester Cobbs, a Contract Route Driver with the United States Postal
Service. As a Route Driver, Cobbs delivered and picked up mail from five
rural post offices in DeSoto County and Tunica County, Mississippi. At the
time of the robbery, Cobbs was headed to Lake Cormorant, the fourth of five
stops he would make along his route.
       The mail that Cobbs collected included registered mail bags, which
contained cash receipts collected by the Postal Service from the sale of items
such as money orders and stamps. By the time that Cobbs arrived at Lake
Cormorant, he had already collected registered mail bags from three other
post offices along his route.
       At approximately 5:20 p.m., Cobbs arrived at the Lake Cormorant
Post Office. As he normally would, Cobbs backed his mail truck up to the
back door, where he would retrieve mail bags waiting for him inside the post
office. Before Cobbs could open the back door to the post office, however, an
unknown assailant—later determined to be Defendant-Appellant Gilbert
McThunel—sprayed Cobbs with pepper spray, struck Cobbs multiple times
with a handgun, threatened to kill him, and grabbed the registered mail bags
from Cobbs’s truck. The mail bags contained $60,706. Thereafter, the
assailant fled, and Cobbs drove his truck to the front of the post office and
called 911.




                                           2
Case: 23-60321       Document: 113-1      Page: 3     Date Filed: 08/09/2024




                                 No. 23-60321


       No suspect was arrested in connection to the robbery on the day of the
occurrence. However, around three days after the robbery, Postal Inspector
Stephen Mathews began his investigation and was able to locate a video of
the incident taken from a camera located at a farm office across the street
from the post office. The video showed a red Hyundai and a large white SUV
in the area. The video revealed the assailant getting out of the SUV before
the robbery, walking behind the building, and waiting for Cobbs to arrive.
While behind the building, the assailant had his “hand up to his ear and
elbow[] out” for multiple minutes, consistent with talking on a cell phone.
However, the video does not show an actual cell phone. Later, after assaulting
Cobbs, the assailant went back behind the building, squatted down, and began
“looking at something in his hand” which appeared “indicative of” cell
phone use. Although not visible on video, it is inferred that the suspect got
back into the SUV before fleeing the scene. Based upon his examination of
the video, Mathews surmised that three suspects were involved.
       Sometime after obtaining the video footage, but prior to applying for
any warrants, Mathews located a witness, Forrest Coffman, who lived across
the street. Coffman had seen the red Hyundai “circling the area back and
forth,” and he decided to ask the driver if he was lost. The driver stated that
he was looking for the highway. Coffman gave the driver directions, turned
around, and went back inside his house. A “few moments later,” Coffman
heard a “bunch of commotion,” stepped outside, and saw officers at the post
office. Coffman walked over and spoke with law enforcement, where he
described the person in the red Hyundai as a black male with a reddish color
goatee. After meeting with law enforcement on the day of the incident,
Coffman had no further involvement with the matter for approximately
fifteen months.
       By November 2018, nine months after the robbery, the Postal
Inspection Service had not been able to identify any suspects from video



                                          3
Case: 23-60321         Document: 113-1          Page: 4      Date Filed: 08/09/2024




                                     No. 23-60321


footage or witness interviews, and Postal Inspector Todd Matney testified
that they “were having a problem identifying the individuals.” However,
during the course of their investigation, Matney and Mathews learned about
“a new type of search warrant”—a “geofence warrant”—designed to
“identify who might be present at the scene of a robbery.” Believing that this
warrant could help them rekindle their investigation, on November 8, 2018,
Matney and Mathews applied for a geofence warrant seeking information
from Google to locate potential suspects and witnesses in connection to the
robbery.
                        B. Geofence Warrants: A Primer
        As a relic of their novelty, “[t]here is a relative dearth of case law
addressing geofence warrants.” United States v. Chatrie, 590 F. Supp. 3d 901,
906 (E.D. Va. 2022) [hereinafter Chatrie (Dist.)]. As such, we provide a brief
history of geofence warrants, as well as a description of law enforcement’s
process for obtaining them. 1
        Google received its first geofence warrant request in 2016. 2 Id. at 914;
United States v. Chatrie, 107 F.4th 319, 323 (4th Cir. 2024) [hereinafter


        _____________________
        1
          Congress has not yet taken a stance on law enforcement’s use of geofence
warrants. However, members have expressed their marked disapproval. In July 2020,
Alphabet (Google’s parent company) CEO Sundar Pichai appeared before the House
Judiciary Subcommittee on Antitrust, Commercial, and Administrative Law. See C-SPAN,
CEOs Mark Zuckerberg, Tim Cook, Jeff Bezos & Sundar Pichai Testify Before House Judiciary
Cmte, YouTube (July 29, 2020), https://perma.cc/7K5T-ACHJ (discussion at 1:45:17-
1:47:50). During the hearing, Representative Kelly Armstrong called geofence warrants
“the single most important issue” before the Subcommittee and contended that geofence
warrants violate the Fourth Amendment. Id. In particular, Representative Armstrong
believed that “people would be terrified to know that law enforcement can grab general
warrants and get everybody’s information anywhere.” Id.
        2
         Companies such as Apple, Lyft, Snapchat, and Uber have all received geofence
warrant requests, but Google is the most common recipient and “the only one known to




                                               4
Case: 23-60321        Document: 113-1         Page: 5     Date Filed: 08/09/2024




                                    No. 23-60321


Chatrie (App.)]. Since then, requests for geofence warrants have
“skyrocketed in number.” Chatrie (App.), 107 F.4th at 323–24. From 2017 to
2018 alone, requests to Google for geofence warrants increased over 1,500%.
Id.; Brian L. Owsley, The Best Offense Is a Good Defense: Fourth Amendment
Implications of Geofence Warrants, 50 Hofstra L. Rev. 829, 834 (2022).
In 2019, Google was receiving about 180 geofence warrant requests per week
from law enforcement around the country, amounting to about 9,000
geofence requests for that year. Owsley, Best Offense, supra at 834; Chatrie
(Dist.), 590 F. Supp. 3d at 914. By 2020, that number went up to 11,500
geofence warrant requests. Owsley, Best Offense, supra at 834. By 2021,
geofence warrants comprised more than 25% of all warrant requests Google
received in the United States. See Google, Supplemental
Information on Geofence Warrants in the United States
1, https://perma.cc/XEU3-KEXJ; Haley Amster & Brett Diehl, Note,
Against Geofences, 74 Stan. L. Rev. 385, 389 & n.11 (2022). Moreover, the
use of these warrants has not been limited to egregious or violent crimes. Law
enforcement officials have obtained geofence warrants for investigations into
stolen pickup trucks and smashed car windows. Amster & Diehl, Against
Geofences, supra at 396; see also In re Search of Info. Stored at Premises Controlled
by Google, as Further Described in Attachment A, No. 20 M 297, 2020 WL
5491763, at *8 (N.D. Ill. July 8, 2020) (“The government’s undisciplined and
overuse of this investigative technique in run-of-the-mill cases that present
no urgency or imminent danger poses concerns to our collective sense of
privacy and trust in law enforcement officials.”).
       “Unlike a warrant authorizing surveillance of a known suspect,
geofencing is a technique law enforcement has increasingly utilized when the
       _____________________
respond.” Note, Geofence Warrants and the Fourth Amendment, 134 HARV. L. REV. 2508,
2512–13 (2021).




                                             5
Case: 23-60321          Document: 113-1           Page: 6      Date Filed: 08/09/2024




                                       No. 23-60321


crime location is known but the identities of suspects [are] not.” United
States v. Rhine, 652 F. Supp. 3d 38, 66 (D.D.C. 2023). Thus, geofence
warrants effectively “work in reverse” from traditional search warrants.
Amster & Diehl, Against Geofences, supra at 388 (internal quotation omitted).
In requesting a geofence warrant, “[l]aw enforcement simply specifies a
location and period of time, and, after judicial approval, companies conduct
sweeping searches of their location databases and provide a list of cell phones
and affiliated users found at or near a specific area during a given timeframe,
both defined by law enforcement.” Geofence Warrants and the Fourth
Amendment, supra at 2509.
        So far, Google has been the primary recipient of geofence warrants, in
large part due to its extensive Location History database, known as the
“Sensorvault.” 3 Amster & Diehl, Against Geofences, supra at 389. Google

        _____________________
        3
          In December 2023, Google authored a blog post where it announced its intent to
modify how and where it stores Location History data. See Marlo McGriff, Updates to
Location History and New Controls Coming Soon to Maps, Google: The Keyword (Dec.
12, 2023), https://perma.cc/DN4Z-7CTA; see also Cyrus Farivar & Thomas Brewster,
Google Just Killed Warrants that Give Police Access to Location Data, Forbes (Dec. 14,
2023, 5:43 PM EST), https://perma.cc/WM83-DAXM. Google’s decision should make it
“impossible for the company to access” Location History data in a move made “explicitly
[to] bring an end to . . . dragnet location searches.” Farivar & Brester, Google Just Killed
Warrants that Give Police Access to Location Data, supra. In other words, these changes, in
theory, “will eventually render the company unable to fulfill geofence warrants.” Prathi
Chowdri, Emerging Tech and Law Enforcement: What Are Geofences and How Do They Work?,
Lexipol (Jan. 4, 2024) (internal quotation omitted), https://perma.cc/DNL3-XC56.
        However, Google has not fully implemented its new storage methods; the
migration will only be complete within “the next several months.” See Stan Kaminsky,
Google Location History Is Now Stored Offline . . . Or Maybe Not, Kaspersky Daily (Mar.
1, 2024), https://perma.cc/ZM6X-92JZ. In fact, the Government concedes that it “is still
seeking Google geofences,” and that even after Google changes its storage techniques,
“the United States . . . may in the future seek geofence warrants from sources other than
Google.” Regardless, these facts do not affect this court’s Fourth Amendment analysis
regarding the constitutionality of the practice itself.




                                                 6
Case: 23-60321        Document: 113-1       Page: 7     Date Filed: 08/09/2024




                                  No. 23-60321


collects data from accounts of users who opt in to Google’s Location History
service. Location History is disabled by default. Chatrie (App.), 107 F.4th at
322. For Location History to collect data, a user must make sure that the
device-location setting is activated, and that Location Reporting is enabled.
This is not to say, however, that enabling Location Reporting is a difficult
task. Users are often asked to opt in to Location History “multiple times
across multiple apps.” Id. at 358 n.9 (Wynn, J., dissenting) (quoting Chatrie
(Dist.), 590 F. Supp. 3d at 908–09). In fact, “manually deactivating all
[Location History] sharing remains difficult and discouraged.” Amster &
Diehl, Against Geofences, supra at 396–97 (“In 2018, an internal Google email
explained that ‘[t]he current [user interface] feels like it is designed to make
[limiting Location History collection] possible, yet [it is] difficult enough that
people won’t figure it out.’” (internal citation omitted)); see also In re Search
of Info. Stored at Premises Controlled by Google, 481 F. Supp. 3d 730, 737 n.3
(N.D. Ill. 2020) (“Published reports have indicated that many Google
services on Android and Apple devices store the device users’ location data
even if the users seek to opt out of being tracked by activating a privacy setting
that says it will prevent Google from storing the location data.”).
       Google’s Android cell phones, which “comprise about 74% of the total
number of smartphones worldwide,” “automatically have an Android
operating system, as well as various Google apps that could potentially store
a user’s location.” Owsley, Best Offense, supra at 834. Apple, which makes
approximately 23% of the world’s smartphones, does not keep location data
associated with its phones, but its phones still “often have various apps
that . . . provide Google with a specific device’s location.” Id. at 834–35. In
October 2018, Google estimated that approximately 592 million—or roughly
one-third—of Google’s users had Location History enabled.
       Once a person enables Location History, Google begins to “log[] [the]
device’s location [into the Sensorvault], on average, every two minutes” by



                                            7
Case: 23-60321       Document: 113-1       Page: 8     Date Filed: 08/09/2024




                                  No. 23-60321


“track[ing] [the] user’s location across every app and every device associated
with the user’s account.” Chatrie (Dist.), 590 F. Supp. 3d at 908–09; see also
Chatrie (App.), 107 F.4th at 323 n.6. In other words, “‘[o]nce a user opts into
Location History, Google is always collecting data and storing all of that data’
in the Sensorvault.” Rhine, 652 F. Supp. 3d at 67 (quoting Chatrie (Dist.), 590
F. Supp. 3d at 909). Location History is stored within the Sensorvault for at
least eighteen months, but users may also request that the information be
deleted themselves. Amster & Diehl, Against Geofences, supra at 394; Rhine,
652 F. Supp. 3d at 67.
       Moreover, not only is the volume of data comprehensive, so is the
quality. “Location History appears to be the most sweeping, granular, and
comprehensive tool—to a significant degree—when it comes to collecting
and storing location data.” Chatrie (App.), 107 F.4th at 349 (Wynn, J.,
dissenting) (quoting Chatrie (Dist.), 590 F. Supp. 3d at 907). The data is
“considerably more precise than other kinds of location data, including cell-
site location information because [Location History] is determined based on
multiple inputs, including GPS signals, signals from nearby Wi-Fi networks,
Bluetooth beacons, and cell towers.” Rhine, 652 F. Supp. 3d at 67 (internal
quotations omitted). Google refers collectively to this data, regardless of its
source, as “Location History.” Amster & Diehl, Against Geofences, supra at
394. Location History data allows Google to “potentially locate an individual
within about sixty feet or less,” and in certain circumstances, down to three
meters. Owsley, Best Offense, supra at 835; Chatrie (Dist.), 590 F. Supp. 3d at
909. In fact, Location History data can “even discern elevation, locating the
specific floor in a building where a person might be.” Chatrie (App.), 107 F.4th
at 349 (Wynn, J., dissenting); see also Chatrie (Dist.), 590 F. Supp. 3d at 908
(noting that Location History data can “determine if you are on the second
[or first] floor of [a] mall”). However, Location History cannot estimate a
device’s location with absolute precision. Instead, when Google reports a




                                           8
Case: 23-60321       Document: 113-1      Page: 9    Date Filed: 08/09/2024




                                 No. 23-60321


device’s location, it includes both the source from which the specific
datapoint was derived, and a “confidence interval” indicating Google’s
confidence in that estimated location. The smaller the radius, the more
confident Google is in that phone’s exact location. According to Google, it
“aims to accurately capture roughly 68 percent of users within [its]
confidence intervals.” Chatrie (Dist.), 590 F. Supp. 3d at 909 (internal
quotation omitted); Chatrie (App.), 107 F.4th at 323. “[I]n other words, there
[is] a 68 percent likelihood that a user is somewhere inside the confidence
interval.” Chatrie (Dist.), 590 F. Supp. 3d at 909 (internal quotation
omitted); Chatrie (App.), 107 F.4th at 323.
       Using the raw data that it collects, Google builds “aggregate models”
using a “proprietary, and therefore un-reviewed, algorithm” that transforms
the data to assist with improving Google’s services, including, for example,
“decision-making in Google Maps.” Wells v. State, 675 S.W.3d 814, 830
(Tex. App.—Dallas 2023, pet. granted); Chatrie (Dist.), 590 F. Supp. 3d at
908; Chatrie (App.), 107 F.4th at 323. It also uses the data to analyze “[its]
customers[’] . . . travel patterns, their history patterns, to make
recommendations and sell advertising.” In short, Google does not store this
data for the purpose of law enforcement, but rather for commercial purposes.
Wells, 675 S.W.3d at 830.
       But, if you build it, they will come. See Geofence Warrants and the
Fourth Amendment, supra at 2508. Early on, when law enforcement officials
first started requesting geofence warrants, they would simply ask Google to
identify all users who were in a geographic area during a given time frame.
However, Google began taking issue with these early warrants, believing
them to be a “potential threat to user privacy.” Chatrie (App.), 107 F.4th at
324. Thus, Google developed an internal procedure on how to respond to
geofence warrants. Id. This procedure is divided into three steps.




                                          9
Case: 23-60321      Document: 113-1       Page: 10     Date Filed: 08/09/2024




                                  No. 23-60321


                                    Step 1
       At Step 1, law enforcement provides Google with the geographical and
temporal parameters around the time and place where the alleged crime
occurred. Following, Google searches its Sensorvault for all users who had
Location History enabled during the law enforcement-provided timeframe.
Chatrie (Dist.), 590 F. Supp. 3d at 914–15. Google is not capable of storing
data in a way that enables it to search a specific area, nor does Google know
which users have saved their Location History prior to its search. Id. at 915.
Thus, for every single geofence warrant Google responds to, it must search
each account in its entire Sensorvault—all 592 million—to find responsive
user records. It cannot just look at individual accounts. See Chatrie (App.),
107 F.4th at 324 (“Google does not keep any lists like this on-hand. So it must
first comb through its entire Location History repository to identify users
who were present in the geofence.”).
       After Google searches its Sensorvault, it determines which accounts
were within the geographic parameters of the warrant and lists each of those
accounts with an anonymized device ID. Google also includes the date and
time, the latitude and longitude, the geolocation source used, and the map
display radius (i.e., the confidence interval). The volume of geofence data
produced “depends on the size and nature of the geographic area and length
of time covered by the geofence request.” Chatrie (Dist.), 590 F. Supp. 3d at
915. “Google does not impose specific, objective restraints on the size of the
geofence, the length of the relevant timeframe, or the number of users for
which it will produce data.” Id. Rather, a Google Legal Investigation
Specialist employee reviews the geofence warrant, consults with legal
counsel, and works with law enforcement to assuage any of Google’s
concerns before turning the data over and moving on to Step 2. Id. at 907,
915–16; see also Chatrie (App.), 107 F.4th at 324.




                                          10
Case: 23-60321      Document: 113-1       Page: 11     Date Filed: 08/09/2024




                                 No. 23-60321


                                    Step 2
       At Step 2, law enforcement contextualizes and narrows the data.
During this step, law enforcement reviews the anonymized list provided by
Google and determines which IDs are relevant. As part of this review, “[i]f
law enforcement needs additional de-identified location information for a
certain device to determine whether that device is actually relevant to the
investigation, law enforcement . . . can compel Google to provide
additional . . . location coordinates beyond the time and geographic scope of
the original request.” Chatrie (Dist.), 590 F. Supp. 3d at 916 (cleaned up);
Chatrie (App.), 107 F.4th at 324. The purpose of this additional data is to
assist law enforcement in eliminating devices that are, for example, “not in
the target location for enough time to be of interest, [or] were moving through
the target location in a manner inconsistent with other evidence.” Chatrie
(Dist.), 590 F. Supp. 3d at 916. As a general matter, “Google imposes no
geographical limits on this Step 2 data.” Id. (internal quotation omitted);
Chatrie (App.), 107 F.4th at 324. “Google does, however, typically require
law enforcement to narrow the number of users for which it requests Step 2
data so that the Government cannot . . . simply seek geographically
unrestricted data for all users within the geofence.” Chatrie (Dist.), 590 F.
Supp. 3d at 916; Chatrie (App.), 107 F.4th at 324.
                                    Step 3
       Finally, at Step 3, law enforcement compels Google to provide
account-identifying information for the users that they determine are
“relevant to the investigation.” Chatrie (App.), 107 F.4th at 324. This
identifying information includes the names and emails associated with the
listed device IDs. Using this information, law enforcement can then pursue
further investigative techniques, such as cell phone tracking, or sending out
additional warrants tailored to the specific information received.




                                          11
Case: 23-60321          Document: 113-1           Page: 12       Date Filed: 08/09/2024




                                         No. 23-60321


                                     *        *         *
        As a final note, even given the vast amount of data Google has, and the
unprecedented precision of Google’s Location History, the results are not
always spectacular. First, “[m]any geofence warrants do not lead to arrests.”
Geofence Warrants and the Fourth Amendment, supra at 2520. Moreover,
“[m]any are rendered useless due to Google’s slow response time, which can
take as long as six months because of the Sensorvault’s size and the large
number of warrants that Google receives.” Id. Second, as to warrants that are
issued, the data Google returns is not always perfect, and sometimes contains
false positives. In fact, there are already documented accounts of innocent
bystanders being swept into geofence warrants based solely on their
proximity to a crime. 4 In short, while false negatives appear to be “more
extremely rare”—given the accuracy of Google’s data—false positives are
still an area of concern.
                C. Geofence Application and Warrant at Issue
        Returning to the matter at hand, the warrant here, like any other
warrant, began with an Application for a Search Warrant. That application
contained an attached affidavit from Matney, which Mathews helped write.

        _____________________
        4
          For example, Zachary McCoy, an avid bike rider, was swept into a geofence
search because on the day of a burglary, he biked past the victim’s house three times within
an hour. Jon Schuppe, Google Tracked His Bike Ride Past a Burglarized Home. That Made
Him a Suspect., NBC News (Mar. 7, 2020, 5:22 AM CST), https://perma.cc/9WJK-
67TW. In another case, based on a Google geofence warrant, Arizona police officers jailed
Jorge Molina for six days on suspicion of murder. Meg O’Connor, Avondale Man Sues After
Google Data Leads to Wrongful Arrest for Murder, Phx. New Times (Jan. 16, 2020),
https://perma.cc/GLJ8-AHP9. As it turns out, Molina’s stepfather—the man ultimately
arrested for the murder—had been using one of Molina’s old cell phones, which
inadvertently remained logged in to Molina’s email and social media accounts. Id. As a
result, Molina lost his job, was unable to pass a background check, and even lost title to his
vehicle because police impounded his car during the investigation. Id.




                                                  12
Case: 23-60321      Document: 113-1       Page: 13     Date Filed: 08/09/2024




                                 No. 23-60321


Because this type of warrant was new, particularly to Mathews, the Postal
Inspectors consulted with other law enforcement agencies when writing the
application. Additionally, the Inspectors used several different “go-bys”—
or form documents—to ensure that their application had all the necessary
“technical language.” Finally, the Inspectors also consulted with the U.S.
Attorney’s Office prior to seeking their warrant.
       The affidavit stated that “there is probable cause to believe that the
Google accounts identified in Section I of Attachment A, associated with a
particular specified location at a particular specified time, contain evidence,
fruits and instrumentalities of a violation of 18 U.S.C. section 2114(a),
Robbery of a U.S. Postal Service Employee.” However, as with any geofence
warrant, no specific Google accounts were identified in Section I of
Attachment A; rather, the Attachment only specified specific coordinates
around the Lake Cormorant Post Office. The box created by those
coordinates covered approximately 98,192 square meters.
       The affidavit also provided a specific Probable Cause Statement. In
that statement, the Inspectors detailed the two vehicles implicated in the
robbery, Cobbs’s description of the assailant, and a statement that, through
a review of the video surveillance footage, “it appears the robbery suspect
[was] possibly using a cellular device both before and after the robbery
occur[ed].” Finally, the Inspectors included language in the application
stating, in regard to Step 2 outlined above, that law enforcement “will seek
any additional information regarding [relevant] devices through further legal
process.”
       The application and affidavit were submitted to a U.S. magistrate
judge, who issued the warrant on November 8, 2018. The language of the
warrant largely tracked Google’s three-step process outlined above:




                                          13
Case: 23-60321     Document: 113-1       Page: 14     Date Filed: 08/09/2024




                                No. 23-60321


      To the extent within the Provider’s possession, custody, or
      control, the Provider is directed to produce the following
      information associated with the Subject Accounts, which will
      be reviewed by law enforcement personnel (who may include,
      in addition to law enforcement officers and agents, attorneys
      for the government, attorney support staff, agency personnel
      assisting the government in this investigation, and outside
      technical experts under government control) are authorized to
      review the records produced by the Provider in order to locate
      any evidence, fruits, and instrumentalities of 18 U.S.C. section
      2114(a), Robbery of a U.S. Postal Service Employee.
             1.     Location information. All location data, whether
      derived from Global Positioning System (GPS) data, cell
      site/cell tower triangulation/trilateration, and precision
      measurement information such as timing advance or per call
      measurement data, and Wi-Fi location, including the GPS
      coordinates, estimated radius, and the dates and times of all
      location recordings, between 5:00 p.m. CT and 6:00 p.m. CT
      on February 5, 2018;
              2.    Any user and each device corresponding to the
      location data to be provided by the “Provider” will be
      identified only by a numerical identifier, without any further
      content or information identifying the user of a particular
      device. Law enforcement will analyze this location data to
      identify users who may have witnessed or participated in the
      Subject Offenses and will seek any additional information
      regarding those devices through further legal process.
              3.      For those accounts identified as relevant to the
      ongoing investigation through an analysis of provided records,
      and upon demand, the “Provider” shall provide additional
      location history outside of the predefined area for those
      relevant accounts to determine the path of travel. This
      additional location history shall not exceed 60 minutes plus or
      minus the first and last timestamp associated with the account
      in the initial dataset. (The purpose of path of travel/contextual




                                         14
Case: 23-60321     Document: 113-1      Page: 15     Date Filed: 08/09/2024




                                No. 23-60321


      location points is to eliminate outlier points where, from the
      surrounding data, it becomes clear the reported point(s) are not
      indicative of the device actually being within the scope of the
      warrant.)
             4.    For those accounts identified as relevant to the
      ongoing investigation through an analysis of provided records,
      and upon demand, the “Provider” shall provide the
      subscriber’s information for those relevant accounts to
      include, subscriber’s name, email addresses, services
      subscribed to, last 6 months of IP history, SMS account
      number, and registration IP.
In summary, as to Step 1, the warrant authorized an hour-long search from
5:00 p.m. to 6:00 p.m. on February 5, 2018, within a geofence covering
approximately 98,192 square meters around the Lake Cormorant Post Office.
As to Step 2, the warrant authorized law enforcement to obtain additional
Location History for a registered device identified as relevant within “60
minutes plus or minus the first and last timestamp associated with the
account in the initial dataset.” However, prior to reaching Step 2, law
enforcement was required to conduct “further legal process.”
      Google returned the Step 1 data in April 2019. Notably, Google’s
search was much broader than that specifically sought by the warrant,
producing data from a circular area that was approximately 378,278 square
meters, not 98,192 square meters. The search of Google’s 592 million




                                        15
Case: 23-60321      Document: 113-1      Page: 16     Date Filed: 08/09/2024




                                 No. 23-60321


accounts returned three anonymous device IDs within the requested
parameters:




Inspector Matney testified that after receiving this data, he reviewed the
devices to ensure that they fell within the geofence coordinates.
       However, prior to submitting Step 2, neither Matney nor Mathews
applied for another warrant. Instead, Matney and Mathews decided
themselves which device IDs were relevant and requested additional de-
anonymized information for all three devices. The Inspectors determined
that all three devices were relevant to their Step 2 inquiry because devices
1091610859 and 1577088768 registered multiple times within the geofence,
and the third device—1353630479—could have been a potential witness. The
Step 2 request was placed in May 2019, and the expanded information was
received on May 30. However, no new devices were added through the
information gained at Step 2.
       Again, without seeking any new warrants, Matney and Mathews sent
off their Step 3 request for all three devices on June 7, 2019. They received
the de-anonymized information from Google on June 10, 2019. The following
files were returned:
       •       2165781.Key.cvs
       •       bleek2004.AccountInfo.txt
       •       jamarrsmith33.AcountInfo.txt
       •       permanentwavesrecords.AccountInfo.txt




                                         16
Case: 23-60321     Document: 113-1       Page: 17    Date Filed: 08/09/2024




                                No. 23-60321


       Through these files, Mathews was able to determine that
“jamarrsmith33.AcountInfo.txt” was Jamarr Smith’s email account and
“bleek2004.AcountInfo.txt” was Gilbert McThunel’s email account. The
third email account associated with “permanentwavesrecords.AccountInfo.
txt” was deemed irrelevant to the investigation.
       Now, no longer devoid of leads, Mathews and Matney took “[a]
bunch of investigative steps” related to Smith and McThunel, including
sending additional non-geofence warrants to Google regarding Smith and
McThunel’s Google accounts, accessing their CLEAR database profiles,
investigating cell tower data related to Smith and McThunel, and sending
non-geofence warrants to phone companies for Smith and McThunel’s
account information. These additional steps revealed multiple phone calls
between Smith and McThunel during the time of the robbery, and allowed
for further geolocation of Appellants using historical cell phone record
analysis.
       Additionally, through a search of Smith’s phone records and his
friends on Facebook, the Inspectors were able to identify Thomas Iroko
Ayodele as a suspect. Finally, on July 1, 2019, Postal Inspector Dwayne
Martin reapproached witness Forrest Coffman and asked him to participate
in a photo lineup. Although Coffman was unable to identify McThunel or
Ayodele in their respective lines, Coffman did identify Smith as the person
he saw driving the red Hyundai. In sum, all evidence connecting Appellants
to this crime was derived from information obtained from Google pursuant
to the geofence warrant.
                       D. Pretrial & Trial Posture
       The Government initiated the instant action by issuing an indictment
on October 27, 2021. Count I of the indictment alleged that Appellants had a
conspiracy to rob the Lake Cormorant Post Office, and Count II alleged the




                                        17
Case: 23-60321      Document: 113-1      Page: 18     Date Filed: 08/09/2024




                                 No. 23-60321


actual robbery. On November 4, 2022, Smith filed a Motion to Suppress—
which the other Appellants joined—seeking to suppress all evidence derived
from the November 2018 geofence warrant which was used to identify them
as suspects.
       Appellants raised multiple arguments related to the constitutionality
of the geofence warrant. First, Appellants contended that they had a
reasonable expectation of privacy in their Google Location History data, and
that this geofence warrant violated that privacy interest as a categorically
unconstitutional general warrant. Second, Appellants argued that the specific
warrant at issue was invalid from its inception because it lacked probable
cause and particularity. Third, Appellants argued that even if the warrant was
valid, the Government did not undertake “further legal process” to obtain
additional information from Google as required by the warrant, making Step
2 and Step 3 of the search warrantless and illegal. Finally, Appellants
maintained that the good-faith exception set forth in United States v. Leon,
468 U.S. 897 (1984), did not excuse the defects of the warrant, especially in
light of the fact that the affidavit in support of the warrant contained a
knowing and intentionally false statement—specifically, that “it appear[ed]
the robbery suspect [was] possibly using a cellular device both before and
after the robbery occur[ed]”—making the warrant invalid pursuant to Franks
v. Delaware, 438 U.S. 154, 164–65 (1978). As such, Appellants concluded, the
exclusionary rule should apply, and all the evidence seized should be
suppressed as fruit of the poisonous tree.
       On January 31, 2023, the district court conducted a hearing on
Appellants’ Motion to Suppress. At the hearing, the Government called its
two Investigators, Matney and Mathews, and Appellants called an expert,
Spencer McInvaille. In relevant part, Matney and Mathews testified as to:
their unfamiliarity with geofence warrants; the steps they took to request a
geofence warrant and receive information from Google; their consultation



                                         18
Case: 23-60321       Document: 113-1       Page: 19     Date Filed: 08/09/2024




                                  No. 23-60321


with the U.S. Attorney’s Office; their review of surveillance footage
purporting to show the robbery suspect acting consistently with cell phone
usage (e.g., holding his hand up to his ear); and their understanding that the
language in the warrant requiring “further legal process” at Steps 2 and 3
meant the process of law enforcement “demand[ing]” information from
Google, not the process of law enforcement seeking any additional warrants
from the court.
       McInvaille provided expert testimony to the court about digital
forensics and geolocation analysis, including, in relevant part, Google
Location History data. McInvaille explained to the district court that
warrants submitted to Google are typically used to seek information about
suspects when law enforcement knows the suspect has a Google account. In
contrast, law enforcement utilizes geofence warrants and Google Location
History when they do not have any leads, but nevertheless want to search
through Google’s data (i.e., the Sensorvault) to find suspects. McInvaille
outlined the three-step geofence warrant process described supra, and
explained that as part of that process, Google is required to search every
Google account with Location History enabled. Finally, McInvaille testified
that, given his experience in other cases, the language requiring “further legal
process” in this warrant would have required additional warrants at each step
of the geofence process.
       On February 10, 2023, after considering the parties’ briefing and the
evidence presented at the hearing, the district court denied Appellants’
motion to suppress. Trial commenced on February 21, 2023. After a four-day
trial, the jury returned a guilty verdict against all three Appellants as to both
counts. Appellants were sentenced on June 13, 2023, to prison terms ranging
from 121 to 136 months. Following, Appellants filed a Motion for New Trial
and Motion for Judgment of Acquittal. The district court denied the motion.
Appellants timely appealed.



                                           19
Case: 23-60321      Document: 113-1       Page: 20     Date Filed: 08/09/2024




                                 No. 23-60321


                           II. Standard of Review
       “When reviewing the denial of a motion to suppress evidence, this
court reviews the district court’s factual findings for clear error and the
district court’s conclusions regarding the sufficiency of the warrant and the
constitutionality of law enforcement action de novo.” United States v. Perez,
484 F.3d 735, 739 (5th Cir. 2007). We view the evidence in the light most
favorable to the prevailing party below—here, the Government. See United
States v. Pack, 612 F.3d 341, 347 (5th Cir. 2010).
                                III. Analysis
       The Fourth Amendment guarantees individuals the right “to be
secure in their persons, houses, papers, and effects, against unreasonable
searches and seizures.” U.S. Const. amend IV. The “basic purpose of
this Amendment . . . is to safeguard the privacy and security of individuals
against arbitrary invasions by governmental officials.” Carpenter v. United
States, 585 U.S. 296, 303 (2018) (quoting Camara v. Mun. Ct. of City and
Cnty. of S.F., 387 U.S. 523, 528 (1967)). Moreover, the Supreme Court has
established that “the Fourth Amendment protects people, not places,” and
the Court has “expanded [its] conception of the Amendment to protect
certain expectations of privacy as well.” Id. at 304 (quoting Katz v. United
States, 389 U.S. 347, 351 (1967)). “When an individual ‘seeks to preserve
something as private,’ and his expectation of privacy is ‘one that society is
prepared to recognize as reasonable,’ [the Court] ha[s] held that official
intrusion into that private sphere generally qualifies as a search and requires
a warrant supported by probable cause.” Id. (quoting Smith v. Maryland, 442
U.S. 735, 740 (1979)). Evidence seized in violation of the Constitution is
subject to suppression. See Hudson v. Michigan, 547 U.S. 586, 590 (2006).




                                          20
Case: 23-60321          Document: 113-1          Page: 21       Date Filed: 08/09/2024




                                       No. 23-60321


                      A. Reasonable Expectation of Privacy
        The threshold question posed by this case is whether geofencing is a
search under the Fourth Amendment. “A Fourth Amendment privacy
interest is infringed when the government physically intrudes on a
constitutionally protected area or when the government violates a person’s
‘reasonable expectation of privacy.’” United States v. Turner, 839 F.3d 429,
434 (5th Cir. 2016) (quoting United States v. Jones, 565 U.S. 400, 406 (2012)).
To assess whether a “reasonable expectation of privacy” exists, the Supreme
Court has applied Justice Harlan’s two-fold approach as explained in his
concurrence in Katz v. United States, 389 U.S. 347. See Jones, 565 U.S. at 406.
Specifically, for Fourth Amendment protections to attach to a person’s
privacy interest, the person first must “have exhibited an actual (subjective)
expectation of privacy.” Katz, 389 U.S. at 361 (Harlan, J., concurring).
Second, that expectation must “be one that society is prepared to recognize
as ‘reasonable.’” Id. (Harlan, J., concurring).
        Smith and McThunel contend that they have a reasonable expectation
of privacy in their respective location information retrieved in response to a
geofence warrant. 5 This argument is rooted in the application of Carpenter v.


        _____________________
        5
          Ayodele also attempts to join Smith and McThunel’s arguments. However, as
noted above, Ayodele’s information was never retrieved in response to a geofence
warrant—his involvement in this robbery was deduced through a search of Smith’s phone
records and Smith’s friends on Facebook performed after the geofence search. As such,
Ayodele may lack Fourth Amendment standing to join Smith and McThunel because even
if he has an expectation of privacy in his own Google Location History data, he may not
have an expectation of privacy in the Google Location History data of an unrelated third-
party. See United States v. Davis, No. 23-10184, 2024 WL 3573478, at *5–7 (11th Cir. 2024)
(concluding that a defendant lacked Fourth Amendment standing to challenge a geofence
warrant that produced his girlfriend’s Google Location History data because “[e]ven if a
person has a privacy interest in the data on his own phone, he does not have that interest in
the data on someone else’s phone.”).




                                                 21
Case: 23-60321          Document: 113-1          Page: 22       Date Filed: 08/09/2024




                                       No. 23-60321


United States, 585 U.S. 296, arguably the most relevant Supreme Court
precedent addressing law enforcement’s investigatory use of cellular
consumer data. See Amster & Diehl, Against Geofences, supra at 406. In
Carpenter, prosecutors, without a warrant supported by probable cause,
received from a criminal defendant’s wireless carriers cell-site location
information (“CSLI”) that tracked the defendant’s whereabouts over the
course of several days. 6 585 U.S. at 302. From this data, prosecutors were
able to produce maps that placed the defendant’s phone near four robberies.
Id. at 302–03. The court of appeals affirmed the defendant’s convictions,
concluding that the defendant’s privacy interest in CSLI was not entitled to
Fourth Amendment protection because “cell phone users voluntarily convey
cell-site data to their carriers as a means of establishing communication.” Id.
at 303 (internal quotation omitted).
        The Supreme Court reversed. Id. at 321. As a starting point, the Court
acknowledged that a majority of the Court had “already recognized that
individuals have a reasonable expectation of privacy in the whole of their
physical movements.” Id. at 310; see Jones, 565 U.S. at 430 (Alito, J.,
concurring in the judgment) (“[T]he use of longer term GPS monitoring in
investigations of most offenses impinges on expectations of privacy.”);
Jones, 565 U.S. at 415 (Sotomayor, J., concurring). The Court then expressed

        _____________________
        Regardless, we do not and need not answer this question today—as discussed
further infra, Smith and McThunel do have Fourth Amendment standing to bring their
respective constitutional challenges, and our ultimate disposition as to all three Appellants
hinges on the good faith exception. See Byrd v. United States, 584 U.S. 395, 411 (2018)
(“Because Fourth Amendment standing is subsumed under substantive Fourth
Amendment doctrine, it is not a jurisdictional question and hence need not be addressed
before addressing other aspects of the merits of a Fourth Amendment claim.”).
        6
          As the Supreme Court in Carpenter explained, CSLI is the time-stamped record
that is generated each time a phone connects to “cell sites,” the network of radio antennas
that provide signal to cell phones. 585 U.S. at 300–01.




                                                 22
Case: 23-60321      Document: 113-1       Page: 23     Date Filed: 08/09/2024




                                 No. 23-60321


concern with the government having unfettered access to CSLI, noting that
this data provides “an intimate window into a person’s life, revealing not
only his particular movements, but through them his ‘familial, political,
professional, religious, and sexual associations.’” Carpenter, 585 U.S. at 311
(quoting Jones, 565 U.S. at 415 (Sotomayor, J., concurring)). The Court
further expressed concern that this precise, sensitive data could be accessed
by the government “[w]ith just the click of a button.” Id. And, in contrast to
a GPS device attached to a person’s car, a cell phone “faithfully follows its
owner beyond public thoroughfares and into private residences, doctor’s
offices, political headquarters, and other potentially revealing locales.” Id.
“Accordingly, when the Government tracks the location of a cell phone it
achieves near perfect surveillance, as if it had attached an ankle monitor to
the phone’s user.” Id. at 311–12. The Court concluded that the criminal
defendant had a “reasonable expectation of privacy in the whole of his
physical movements.” Id. at 313.
       The Court then addressed the third-party doctrine, which provides
that generally, “a person has no legitimate expectation of privacy in
information he voluntarily turns over to third parties.” Id. at 308 (quoting
Smith, 442 U.S. at 743–44). The Court declined to apply the third-party
doctrine to the collection of CSLI, notwithstanding the fact that this data is
technically voluntarily provided from users to private wireless carriers. As
the Court noted, there is a “world of difference between the limited types of
personal information” addressed in the Court’s prior third-party doctrine
precedent “and the exhaustive chronicle of location information casually
collected by wireless carriers today.” Id. at 314. Furthermore, the Court
found the notion that users “voluntarily” provide this information to private
entities dubious. Carrying a cell phone is “indispensable to participation in
modern society,” and, “[a]part from disconnecting the phone from the
network, there is no way to avoid leaving behind a trail of location data.” Id.




                                          23
Case: 23-60321       Document: 113-1       Page: 24     Date Filed: 08/09/2024




                                  No. 23-60321


at 315. “As a result, in no meaningful sense does the user voluntarily
‘assume[] the risk’ of turning over a comprehensive dossier of his physical
movements.” Id. (quoting Smith, 442 U.S. at 745).
       Chief Justice Roberts’s majority opinion in Carpenter speaks at length
about the privacy interests inherent in location data, and it expresses grave
concern with the government being able to comprehensively track a person’s
movement with relative ease due to the ubiquity of cell phone possession.
The Court acknowledged “some basic guideposts” in resolving questions
related to the Fourth Amendment’s protections of privacy interests,
including securing “the privacies of life against arbitrary power,” and placing
“obstacles in the way of a too permeating police surveillance.” Carpenter,
585 U.S. at 305 (internal quotations omitted). The Court also recognized the
necessity of applying the Fourth Amendment to systems of advanced
technology, expressing concern that CSLI is approaching “GPS-level
precision,” with wireless carriers having the capability to “pinpoint a
phone’s location within 50 meters.” Id. at 313; see also Riley v. California, 573
U.S. 373, 396 (2014) (acknowledging the privacy concerns implicated by cell
phone location data that “can reconstruct someone’s specific movements
down to the minute, not only around town but also within a particular
building”).
       Many of the concerns expressed by Chief Justice Roberts in his
Carpenter opinion are highly salient in the context of geofence warrants.
Perhaps the most alarming aspect of geofences is the potential for
“permeating police surveillance.” As Chief Justice Roberts explained,
modern cell phones enable the government to achieve “near perfect
surveillance”; carrying one of these devices is essentially a prerequisite to
participation in modern society, and users “compulsively carry cell phones
with them all the time.” Id. at 311–12, 315. Geofences also exemplify the
Court’s concern with pinpoint location data—this technology provides more



                                           24
Case: 23-60321         Document: 113-1           Page: 25       Date Filed: 08/09/2024




                                       No. 23-60321


precise location data than either CSLI or GPS. Geofence Warrants and the
Fourth Amendment, supra at 2510. Furthermore, obtaining data through
geofences, like obtaining data through CSLI, is “remarkably cheap, easy,
and efficient compared to traditional investigative tools.” Carpenter, 585
U.S. at 311. With “just the click of a button,” the government can search the
pinpoint locations of over half a billion people with Location History enabled.
See id.
          But while we see the parallels between CSLI and Location History
data, our colleagues on the Fourth Circuit—the first federal Circuit to
address whether geofencing is a “search” subject to the Fourth
Amendment—saw Location History data differently. See Chatrie (App.), 107
F.4th at 330. Characterizing Location History data as nothing more than a
“record of a person’s single, brief trip,” the Fourth Circuit found that
geofencing does not contravene a person’s “reasonable expectation of
privacy” because the data implicated by geofences is “far less revealing than
that obtained in Jones[ or] Carpenter.” Id. at 330–31. 7 With great respect to
our colleagues on the Fourth Circuit, we disagree. While it is true that
geofences tend to be limited temporally, the potential intrusiveness of even a
snapshot of precise location data should not be understated. As two
commentators noted:

          _____________________
          7
           In United States v. Davis, the Eleventh Circuit appeared to agree with the Fourth
Circuit that geofence warrants “do[] not implicate the same privacy concerns raised in
Carpenter.” See 2024 WL 3573478, at *6. However, Davis ultimately concerned a
defendant’s Fourth Amendment standing to challenge a geofence warrant that obtained his
girlfriend’s Google Location History data, not his own data. Id. at *6. Thus, the Eleventh
Circuit’s discussion of the intrusiveness of Google Location History data ultimately does
not appear to have been dispositive to its holding. See id. at *6–7 (“Because the geofence
revealed the location of an open program that was not [the defendant’s] and was not on a
phone in his exclusive possession or control, he cannot argue that he had a privacy interest
in this data that gives him Fourth Amendment standing to challenge the search.”).




                                                25
Case: 23-60321         Document: 113-1           Page: 26       Date Filed: 08/09/2024




                                       No. 23-60321


        [E]ven a brief snapshot can expose highly sensitive
        information—think a visit to “the psychiatrist, the plastic
        surgeon, the abortion clinic, the AIDS treatment center, the
        strip club, the criminal defense attorney, the by-the-hour-
        motel, the union meeting, the mosque, synagogue or church,
        [or] the gay bar,” or a location other than home during a
        COVID-19 shelter-in-place order.
Amster & Diehl, Against Geofences, supra at 408 (quoting Jones, 565 U.S. at
415 (Sotomayor, J., concurring)). Plus, such location tracking can easily
follow an individual into areas normally considered some of the most private
and intimate, particularly residences. As another commentator described:
        Even a geofence warrant that limits itself to a single day could
        follow a person from the interior of their home, among the
        rooms of their dwelling, to the location of a crime, then to a
        place of worship, then perhaps to a new home, such as that of
        a relative or friend, and among the rooms of that second
        dwelling.
A. Reed McLeod, Note, Geofence Warrants: Geolocating the Fourth
Amendment, 30 Wm. & Mary Bill Rts. J. 531, 549 (2021). 8 In short,

        _____________________
        8
           The Fourth Circuit acknowledged and dismissed these considerations because,
inter alia, the defendant—like the defendants in the case at bar—“d[id] not contend that
the warrant revealed his own movements within his own constitutionally protected space,”
and thus the defendant lacked Fourth Amendment standing to challenge geofencing on
those grounds. See Chatrie (App.), 107 F.4th at 330 n.17, 337 n.26. We disagree—this
conclusion directly conflicts with Carpenter.
         In Carpenter, the Supreme Court’s analysis of whether the government’s access of
the defendant’s CSLI impeded his reasonable expectation of privacy was not based on a
review of the specific results of the search in that case. See generally 585 U.S. at 309–13.
Rather, the Supreme Court analyzed the general capabilities of CSLI, and asked whether
the ability for CSLI “to chronicle a person’s past movements through the record of his cell
phone signals” created an expectation of privacy. Id. at 309. In other words, it did not
matter whether that defendant happened to stay outside of a constitutionally protected area
during a search or not. The question was whether the technology utilized by law




                                                26
Case: 23-60321           Document: 113-1           Page: 27        Date Filed: 08/09/2024




                                        No. 23-60321


geofence location data is invasive for Fourth Amendment purposes. Of
particular concern is the fact that a geofence will retroactively track anyone
with Location History enabled, regardless of whether a particular individual
is suspicious or moving within an area that is typically granted Fourth
Amendment protection. 9
        Moreover, Carpenter’s application to the third-party doctrine in this
case is straightforward. As the Court in Carpenter explained, while cell phone
data is held by private corporations, on a practical level, it is unreasonable to
think of cell phone users as voluntarily assuming the risk of turning over
        _____________________
enforcement had the capability of providing data that offered “an all-encompassing record
of [a person’s] whereabouts,” regardless of whether that person actually entered spaces
that are traditionally considered protected under the Fourth Amendment. Id. at 311. And,
when a person has a “reasonable expectation of privacy in the place or thing searched or
seized,” he or she has Fourth Amendment standing. See United States v. Gaulden, 73 F.4th
390, 392 (5th Cir. 2023).
         Here, the analysis is no different. The question is whether Location History data
has the capability of revealing intimate, private details about a person’s life, thus conferring
a “reasonable expectation of privacy.” This is general inquiry, not a retroactive, post-hoc
examination based on the results of the search in our case. A conclusion to the contrary
would be enigmatic. See Chatrie (App.), 107 F.4th at 351 (Wynn, J., dissenting) (“The
government . . . cannot circumvent the Constitution merely because, by sheer luck, its
target did not stray from the safe zone.”).
        9
            Some have argued that the privacy concerns presented by geofences are
ameliorated by the fact that information sent to law enforcement is, at first, anonymized.
See, e.g., In re Search of Info. Stored at Premises Controlled by Google, No. 2:22-MJ-01325,
2023 WL 2236493, at *8 (S.D. Tex. Feb. 14, 2023). However, it is undisputed that the data
is eventually de-anonymized. And, even setting that point aside, the effectiveness of data
anonymization has been called into question by researchers, given that anonymous data can
be cross-referenced to reveal identities. See Amster & Diehl, Against Geofences, supra at
409; see also Charlie Warzel & Stuart A. Thompson, They Stormed the Capitol. Their Apps
Tracked Them., N.Y. Times (Feb. 5, 2021), https://perma.cc/KMP3-3QSV (detailing
journalists’ efforts to identify individuals contained in anonymized datasets of smartphone
locations); Gina Kolata, Your Data Were ‘Anonymized’? These Scientists Can Still Identify
You, N.Y. Times (July 23, 2019), https://perma.cc/L5DL-MPZM. Thus, we find this
argument wanting.




                                                   27
Case: 23-60321      Document: 113-1       Page: 28     Date Filed: 08/09/2024




                                  No. 23-60321


comprehensive dossiers of their physical movements to third parties.
Carpenter, 585 U.S. at 315. In a way, Carpenter acknowledged that, at least in
some instances, the third-party doctrine is “ill suited to the digital age, in
which people reveal a great deal of information about themselves to third
parties in the course of carrying out mundane tasks.” Jones, 565 U.S. at 417
(Sotomayor, J., concurring). Given the ubiquity—and necessity—in the
digital age of entrusting corporations like Google, Microsoft, and Apple with
highly sensitive information, the notion that users voluntarily relinquish their
right to privacy and “assume[] the risk” of this information being divulged
to law enforcement is dubious. See Smith, 442 U.S. at 745.
       It is true that this case is slightly distinguishable from Carpenter;
namely, that users opt in to having their Location History monitored. Indeed,
this was the other consideration that persuaded the Fourth Circuit that
geofencing is not a “search” subject to the Fourth Amendment. See Chatrie
(App.), 107 F.4th at 331–32. Again, with great respect, we are not convinced.
       As anyone with a smartphone can attest, electronic opt-in processes
are hardly informed and, in many instances, may not even be voluntary. See
Daniel J. Solove, Privacy Self-Management and the Consent Dilemma, 126
Harv. L. Rev. 1880, 1884–88 (2013). See generally Hannah J. Hutton &
David A. Ellis, Exploring User Motivations Behind iOS App Tracking
Transparency Decisions, Proc. of the 2023 CHI Conf. on Hum.
Factors in Computing Sys., Apr. 2023, at 1, 7–8, 10 (detailing
general “confusion” with, and “misconceptions” about, Apple’s data-
tracking opt-in prompts due, in part, to those prompts’ “lack of clarity”).
Google’s Location History opt-in process is no different. As described above,
users are bombarded multiple times with requests to opt in across multiple
apps. See Chatrie (Dist.), 590 F. Supp. 3d at 908–09. These requests typically
innocuously promise app optimization, rather than reveal the fact that users’
locations will be comprehensively stored in a “Sensorvault,” providing



                                          28
Case: 23-60321       Document: 113-1       Page: 29     Date Filed: 08/09/2024




                                  No. 23-60321


Google the means to access this data and share it with the government. See
Chatrie (App.), 107 F.4th at 359–60 (Wynn, J., dissenting); see also Defendant
Okello Chatrie’s Supplemental Motion to Suppress Evidence Obtained from
a “Geofence” General Warrant at 15–17, United States v. Chatrie, No. 19-cr-
00130 (E.D. Va. May 22, 2020), 2020 WL 4551093, ECF No. 104. Even
Google’s own employees have indicated that deactivating Location History
data based on Google’s “limited and partially hidden” warnings is “difficult
enough that people won’t figure it out.” Chatrie (App.), 107 F.4th at 360, 367
(Wynn, J., dissenting) (quoting Chatrie (Dist.), 590 F. Supp. 3d at 913, 936);
Amster & Diehl, Against Geofences, supra at 396–97.
       But you don’t have to take our word for it—others have similarly
questioned the “voluntary” nature of Google’s opt-in process. See, e.g., In re
Search of Info. Stored at Premises Controlled by Google, 481 F. Supp. 3d at 737
& n.3 (“The Court finds it difficult to imagine that users of electronic devices
would affirmatively realize, at the time they begin using the device, that they
are providing their location information to Google in a way that will result in
the government’s ability to obtain—easily, quickly and cheaply—their
precise geographical location at virtually any point in the history of their use
of the device.”); McLeod, Geolocating the Fourth Amendment, supra at 543
(“[C]onsider a Google user’s consent to Location History . . . . [u]sers either
opt in with less than explicit notice given to them, or even with good notice,
without a full realization of the potential consequences to their privacy if they
opt in. Second, users may understand the notice they have been given, but
misunderstand the accuracy of the movement patterns as expressed in the
location data collected by tech companies.”); Chatrie (Dist.), 590 F. Supp. 3d
at 935 (acknowledging that users take “some affirmative steps to enable
location history,” yet concluding that “those steps likely do not constitute a
full assumption of the attendant risk of permanently disclosing one’s
whereabouts during almost every minute of every hour of every day”); see




                                           29
Case: 23-60321         Document: 113-1          Page: 30      Date Filed: 08/09/2024




                                       No. 23-60321


also Chatrie (App.), 107 F.4th at 356–61 (Wynn, J., dissenting); Amster &
Diehl, Against Geofences, supra at 396–97, 409–10.
        Not to mention, the fact that approximately 592 million people have
“opted in” to comprehensive tracking of their locations itself calls into
question the “voluntary” nature of this process. In short, “a user simply
cannot forfeit the protections of the Fourth Amendment for years of precise
location information by selecting ‘YES, I’M IN’ at midnight while setting up
Google Assistant, even if some text offered warning along the way.” Chatrie
(Dist.), 590 F. Supp. 3d at 936.
                                   *        *         *
        To conclude, we hold that law enforcement in this case did conduct a
search when it sought Location History data from Google. Given the
intrusiveness and ubiquity of Location History data, Smith and McThunel
correctly contend that they have a “reasonable expectation of privacy” in
their respective data. Additionally, per Carpenter, the third-party doctrine
does not apply.
                          B. General Constitutionality
        Having concluded that the acquisition of Location History data via a
geofence is a search, it follows that the government must generally obtain a
warrant supported by probable cause and particularity before requesting such
information. Carpenter, 585 U.S. at 316. Accordingly, we turn to the issue of
whether geofence warrants satisfy this mandate, addressing Appellants’
argument that these novel warrants resemble unconstitutional general
warrants prohibited by the Fourth Amendment. 10


        _____________________
        10
         Because the Fourth Circuit concluded that law enforcement did not conduct a
search when it sought Location History data from Google, it did not reach the question of




                                                30
Case: 23-60321       Document: 113-1      Page: 31     Date Filed: 08/09/2024




                                  No. 23-60321


       “[T]he Fourth Amendment was the founding generation’s response
to the reviled ‘general warrants’ and ‘writs of assistance’ of the colonial era,
which allowed British officers to rummage through homes in an unrestrained
search for evidence of criminal activity.” Riley, 573 U.S. at 403. “General
warrants” are warrants that “specif[y] only an offense,” leaving “to the
discretion of the executing officials the decision as to which persons should
be arrested and which places should be searched.” Steagald v. United States,
451 U.S. 204, 220 (1981); Geofence Warrants and the Fourth Amendment, supra
at 2518.
       It is undeniable that general warrants are plainly unconstitutional.
Indeed, “it would be a needless exercise in pedantry to review again the
detailed history of the use of general warrants as instruments of oppression
from the time of the Tudors, through the Star Chamber, the Long
Parliament, the Restoration, and beyond.” Stanford v. Texas, 379 U.S. 476,
482 (1965). Thus, courts have recognized that no warrant “can authorize the
search of everything or everyone in sight.” Geofence Warrants and the Fourth
Amendment, supra at 2518; cf. Marks v. Clarke, 102 F.3d 1012, 1029 (9th Cir.
1996) (“[A] warrant to search ‘all persons present’ for evidence of a crime
may only be obtained when there is reason to believe that all those present
will be participants in the suspected criminal activity.”); Owens ex rel. Owens
v. Lott, 372 F.3d 267, 276 (4th Cir. 2004) (“[A]n ‘all persons’ warrant can
pass constitutional muster if the affidavit and information provided to the
magistrate supply enough detailed information to establish probable cause to
believe that all persons on the premises at the time of the search are involved
in the criminal activity.”).


       _____________________
whether geofence warrants pass muster under the Fourth Amendment’s warrant
requirement.




                                          31
Case: 23-60321         Document: 113-1          Page: 32      Date Filed: 08/09/2024




                                      No. 23-60321


        When law enforcement submits a geofence warrant to Google, Step 1
forces the company to search through its entire database to provide a new
dataset that is derived from its entire Sensorvault. In other words, law
enforcement cannot obtain its requested location data unless Google searches
through the entirety of its Sensorvault—all 592 million individual accounts—
for all of their locations at a given point in time. Moreover, this search is
occurring while law enforcement officials have no idea who they are looking
for, or whether the search will even turn up a result. Indeed, the
quintessential problem with these warrants is that they never include a
specific user to be identified, only a temporal and geographic location where
any given user may turn up post-search. 11 That is constitutionally insufficient.
        Geofence warrants present the exact sort of “general, exploratory
rummaging” that the Fourth Amendment was designed to prevent. Coolidge
v. New Hampshire, 403 U.S. 443, 467 (1971); see also Riley, 573 U.S. at 403;
Geofence Warrants and the Fourth Amendment, supra at 2519. In fact, Google
Maps creator Brian McClendon has called these warrants “fishing
expedition[s],” and explained that Google employees originally assumed law
enforcement would only seek Location History data on specific people—a
reality that did not come true. Jennifer Valentino-DeVries, Tracking Phones,

        _____________________
        11
           As Professor Stephen Henderson explains in his discussion of CSLI, focusing
probable cause on the group rather than the individual “would mean that a larger database
is always preferred” by law enforcement, because “by definition there will be evidence of
crime in that larger set.” Stephen E. Henderson, Response, A Rose by Any Other Name:
Regulating Law Enforcement Bulk Metadata Collection, 94 Tex. L. Rev. See Also 28, 40–
41 (2016). Doing so leads to an “absurd” understanding of probable cause: “[A] prosecutor
confident that a bank customer is committing tax fraud could access the combined records
of all customers of that bank because, somewhere in there, she is very sure is evidence of
crime.” Id. at 41. Henderson argues, in the context of CSLI, it must be the case that
probable cause is required for “each person’s obtained records,” meaning here “each
phone number contained within the dump.” Id. The same argument applies with full force
to Google accounts containing Location History data.




                                               32
Case: 23-60321           Document: 113-1           Page: 33        Date Filed: 08/09/2024




                                        No. 23-60321


Google Is a Dragnet for the Police, N.Y. Times (Apr. 13, 2019),
https://perma.cc/NCF3-H5DP. “Awareness that the government may be
watching chills associational and expressive freedoms.” Jones, 565 U.S. at
416 (Sotomayor, J., concurring.). And, when these core rights are at issue,
the warrant requirement must “be accorded the most scrupulous
exactitude.” See Stanford, 379 U.S. at 485.
        Here, the Government contends that geofence warrants are not
general warrants because they are “limited to specified information directly
tied to a particular [crime] at a particular place and time.” This argument
misses the mark. While the results of a geofence warrant may be narrowly
tailored, the search itself is not. A general warrant cannot be saved simply by
arguing that, after the search has been performed, the information received
was narrowly tailored to the crime being investigated. These geofence
warrants fail at Step 1—they allow law enforcement to rummage through
troves of location data from hundreds of millions of Google users without any
description of the particular suspect or suspects to be found. 12

        _____________________
        12
            The Fourth Circuit—albeit in the context of determining whether law
enforcement’s acquisition of Location History data qualified as a “search” under the
Fourth Amendment—appeared to contend that Google’s search at Step 1 is irrelevant to
our inquiry because Google, rather than law enforcement, conducts that search. See Chatrie
(App.), 107 F.4th at 330 n.16. Instead, the Fourth Circuit concluded that “the proper focus
of our inquiry [should be] . . . the government’s access of two hours’ worth of [defendant’s]
Location History data,” i.e., Step 2, because “a search only occurs once the government
accesses the requested information.” Id.
         This proposition is breathtaking. In essence, the Fourth Circuit appears to
conclude that law enforcement may flaunt the Fourth Amendment by simply offloading
their act of “searching” on to a third party, and waiting to see if that third party’s search
produces any fruit before applying for a warrant. Moreover, by implication, if the third
party’s search produces zero evidence, law enforcement never conducted any search at all.
         But the Supreme Court has clearly stated that the Fourth Amendment protects
against both searches and seizures “effected by a private party . . . if the private party acted
as an instrument or agent of the Government.” Skinner v. Ry. Lab. Execs.’ Ass’n, 489 U.S.




                                                   33
Case: 23-60321         Document: 113-1          Page: 34       Date Filed: 08/09/2024




                                      No. 23-60321


        In sum, geofence warrants are “[e]mblematic of general warrants”
and are “highly suspect per se.” Geofence Warrants and the Fourth
Amendment, supra at 2520; Amster & Diehl, Against Geofences, supra at 433–
34; Chad Marlow & Jennifer Stisa Granick, Celebrating an Important Victory
in the Ongoing Fight Against Reverse Warrants, ACLU (Jan. 29, 2024),
https://perma.cc/SC2R-S7PJ (“The constitutionality of reverse warrants is
highly suspect because, like general warrants that are prohibited by the
Fourth Amendment, they permit searches of vast quantities of private,
personal information without identifying any particular criminal suspects or
demonstrating probable cause to believe evidence will be located in the
corporate databases they search.”); Chatrie (App.), 107 F.4th at 353 (Wynn,
J., dissenting) (“[A] [geofence] warrant is uncomfortably akin to the sort of
‘reviled’ general warrants used by English authorities that the Framers
intended the Fourth Amendment to forbid.”).
        This court “cannot forgive the requirements of the Fourth
Amendment in the name of law enforcement.” Berger v. New York, 388 U.S.
41, 62 (1967). Accordingly, we hold that geofence warrants are general
warrants categorically prohibited by the Fourth Amendment. We now move
on to suppression and the good-faith exception to the warrant requirement.
                             C. Good-Faith Exception
        In United States v. Leon, 468 U.S. 897, 913 (1984), the Supreme Court
evaluated the Fourth Amendment exclusionary rule, and opined that
        _____________________
602, 613–14 (1989). And, here, all of Google’s actions, including at Step 1, are “conducted
in response to legal compulsion and ‘with the participation or knowledge of [a]
governmental official.’” Geofence Warrants and the Fourth Amendment, supra at 2516
(quoting United States v. Jacobsen, 466 U.S. 109, 113 (1984)). Accordingly, law enforcement
must abide by the Fourth Amendment not only when Google provides them with a final list
of names, but also when they instruct Google to search its entire Sensorvault to produce
those names. Id. Put differently, the proper focus of our inquiry does include Step 1.




                                                34
Case: 23-60321          Document: 113-1          Page: 35       Date Filed: 08/09/2024




                                       No. 23-60321


evidence seized by officers reasonably relying on a warrant issued by a
detached and neutral magistrate judge should be admissible. 13 However, the
Court articulated four circumstances where this “good faith” exception does
not apply:
        (1) when the issuing magistrate was misled by information in an
        affidavit that the affiant knew or reasonably should have known
        was false; (2) when the issuing magistrate wholly abandoned
        his judicial role; (3) when the warrant affidavit is so lacking in
        indicia of probable cause as to render official belief in its
        existence unreasonable; and (4) when the warrant is so facially
        deficient in failing to particularize the place to be searched or
        the things to be seized that executing officers cannot
        reasonably presume it to be valid.
United States v. Woerner, 709 F.3d 527, 533–34 (5th Cir. 2013) (citing Leon,
468 U.S. at 921–25).
        Appellants argue that three of the Leon circumstances apply in this
case. First, Appellants contend that Inspectors knowingly or recklessly
included a false statement in the warrant affidavit, specifically, the statement
that “it appear[ed] the robbery suspect [was] possibly using a cellular device

        _____________________
        13
           Appellants argue that “[t]here is no such thing as relying on a general warrant in
good-faith,” and that an application of Leon is categorically unnecessary. Their argument
is well taken, but we decline to adopt that stance today. Appellants point the court to Groh
v. Ramirez, 540 U.S. 551, 558, 563 (2004), which held that “no reasonable officer could
believe that a warrant that plainly did not comply with [the particularity] requirement was
valid,” and which cited Leon even though the issue in Groh was ultimately about qualified
immunity. However, Groh did not involve a novel advancement in law enforcement
technology—in fact, Groh involved an essentially run-of-the-mill warrant to search for guns
in a house. Id. at 554–57. Given the novelty and complexity of geofence warrants, as well as
the dearth of legal authority on the topic of geofence warrants to guide law enforcement,
Groh is distinguishable on its facts. Moreover, the other cases cited by Appellants are also
unavailing, as a majority were decided prior to Leon. Accordingly, we hold that Leon applies
to our analysis.




                                                 35
Case: 23-60321       Document: 113-1       Page: 36      Date Filed: 08/09/2024




                                  No. 23-60321


both before and after the robbery occur[ed].” Appellants maintain that
Matney and Mathew’s use of a “go-by” is indicative of the fact that they had
no idea whether a cell phone was used, and that this is “by definition reckless
at best.” We disagree. As the district court noted, video evidence of the
assailant appears to show body language consistent with cell phone use.
Mathews and Matney reviewed this video footage in addition to using a “go-
by.” In essence, Appellants ask this court to ignore Matney’s testimony that
the Inspectors based their probable cause statement in the warrant affidavit,
in part, on this footage. Because this court is highly deferential to the district
court’s factfinding, and because the court reviews evidence in the light most
favorable to the Government, see Pack, 612 F.3d at 347, Appellants’ argument
fails.
         Appellants’ second and third Leon arguments pertain to probable
cause and particularity—i.e., that the warrant was “completely devoid” of
probable cause, or that it was “facially deficient” in particularity, rendering
the Inspectors’ conclusions unreasonable. Again, we disagree. Here, we find
the rationale behind the Fourth Circuit’s opinion in United States v. McLamb,
880 F.3d 685 (4th Cir. 2018), persuasive. In McLamb, the Fourth Circuit
declined to suppress evidence when officers were utilizing “cutting edge
investigative techniques” and consulted with attorneys from the Department
of Justice. Id. at 690–91. Here, the Inspectors likewise had conversations with
other law enforcement officials and the U.S. Attorney’s Office prior to
submitting their warrant. To this end, we, like the district court “struggle[]
to see any wrongful conduct to deter,” because “the conduct of law
enforcement in this case seem[ed] reasonable and appropriate when
considering the specific circumstances with which the investigators were
faced.”
         At bottom, “but-for causality is only a necessary, not a sufficient,
condition for suppression.” Hudson, 547 U.S. at 592. This court must also



                                           36
Case: 23-60321          Document: 113-1           Page: 37        Date Filed: 08/09/2024




                                        No. 23-60321


weigh the “substantial social costs” of exclusion against “deterrence
benefits,” the “existence of which [is also] a necessary condition for
exclusion.” Id. at 594–96 (internal quotations omitted). Here, the social costs
of exclusion are admittedly considerable, including the consequences “that
exclusion of relevant incriminating evidence always entails (viz., the risk of
releasing dangerous criminals into society).” Id. at 595. Additionally, the
deterrence benefits here are not clear. The Inspectors were utilizing a
cutting-edge investigative technique with which neither Inspector had
personal experience. To that end, the Inspectors diligently attempted to
make sure that their warrant comported with the Fourth Amendment by
communicating with other law enforcement agencies and the U.S.
Attorney’s Office, and the Inspectors exhibited no malicious intent through
the actions that they took. Thus, we cannot fault law enforcement’s actions
considering the novelty of the technique and the dearth of court precedent to
follow. 14 Accordingly, none of Leon’s circumstances apply, and the district
court correctly declined to suppress evidence under the good-faith exception
to the warrant requirement. 15


        _____________________
        14
            For the same reasons, we agree with the district court that the Inspectors’
mistaken belief regarding the meaning of the phrase “further legal process,” and their
failure to apply for additional warrants at Steps 2 and 3, do not preclude the applicability of
the good faith exception.
        15
           Appellants also argue that the district court erred by failing to exclude the
Government’s expert witness, Christopher Moody, at trial as unreliable under Daubert v.
Merrell Dow Pharmaceuticals, Inc., 509 U.S. 579 (1993). We disagree. “District courts enjoy
wide latitude in determining the admissibility of expert testimony, and the discretion of the
trial judge and his or her decision will not be disturbed on appeal unless manifestly
erroneous.” Watkins v. Telsmith, Inc., 121 F.3d 984, 988 (5th Cir. 1997) (internal quotation
omitted). “‘Manifest error’ is one that is ‘plain and indisputable, and that amounts to a
complete disregard of the controlling law.’” Kim v. Am. Honda Motor Co., 86 F.4th 150,
159 (5th Cir. 2023) (quoting Bear Ranch, L.L.C. v. Heartbrand Beef, Inc., 885 F.3d 794, 802
(5th Cir. 2018)).




                                                  37
Case: 23-60321         Document: 113-1          Page: 38       Date Filed: 08/09/2024




                                      No. 23-60321


                                   IV. Conclusion
        We hold that geofence warrants are modern-day general warrants and
are unconstitutional under the Fourth Amendment. However, considering
law enforcement’s reasonable conduct in this case in light of the novelty of
this type of warrant, we uphold the district court’s determination that
suppression was unwarranted under the good-faith exception.
        AFFIRMED.




        _____________________
         Here, Moody testified about two technological areas: (1) CSLI; and (2) Google
Location History. First, Appellants acknowledge that this court has accepted historical
cellular site analysis in the past as the subject of expert testimony. See United States v.
Schaffer, 439 F. App’x 344, 347 (5th Cir. 2011). Second, it is undisputed that Google
Location History is a collection of data that is itself derived from a combination of three
forms of geolocation—CSLI, GPS, and Wi-Fi. Thus, Moody’s extensive knowledge, skill,
experience, training, and education in historically reliable forms of geolocation, such as
CSLI, GPS, and Wi-Fi, allowed him to discuss Google Location History data, which is
itself derived from those very sources. At bottom, the district court did not commit error,
let alone manifest error, by allowing Moody to testify.




                                                38
Case: 23-60321      Document: 113-1       Page: 39   Date Filed: 08/09/2024




                                No. 23-60321


James C. Ho, Circuit Judge, concurring:
      Geofence warrants are powerful tools for investigating and deterring
crime. The defendants here engaged in a violent robbery—and likely would
have gotten away with it, but for this new technology. So I fully recognize
that our panel decision today will inevitably hamper legitimate law
enforcement interests.
      But hamstringing the government is the whole point of our
Constitution. Our Founders recognized that the government will not always
be comprised of publicly-spirited officers—and that even good faith actors
can be overcome by the zealous pursuit of legitimate public interests. “If
men were angels, no government would be necessary.” The Federalist
No. 51, at 349 (J. Cooke ed. 1961). “If angels were to govern men, neither
external nor internal controls on government would be necessary.” Id. But
“experience has taught mankind the necessity of auxiliary precautions.” Id.
It’s because of “human nature” that it’s “necessary to control the abuses of
government.” Id.
       Our decision today is not costless. But our rights are priceless.
Reasonable minds can differ, of course, over the proper balance to strike
between public interests and individual rights. Time and again, modern
technology has proven to be a blessing as well as a curse. Our panel decision
today endeavors to apply our Founding charter to the realities of modern
technology, consistent with governing precedent. I concur in that decision.




                                     39

```

---

## GROUP: _overhaul2/lake/cases/United States v. Sokolow.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Sokolow"
type: case
citation: "490 U.S. 1 (1989)"
parallel_cite: "109 S. Ct. 1581; 104 L. Ed. 2d 1; 57 U.S.L.W. 4401"
neutral_cite: 1989 U.S. LEXIS 1694
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1989
date_decided: 1989-04-03
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1989-04-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Sokolow
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112239/united-states-v-sokolow/"
  cluster_id: 112239
  opinion_id: 112239
  identity_checked: true
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Reasonable Suspicion]]"
    role: "Key — Progeny / Refinement"
related: ["[[Terry v. Ohio]]", "[[United States v. Cortez]]", "[[United States v. Arvizu]]", "[[Illinois v. Wardlow]]"]
aliases: []
tags: ["case", "fourth-amendment", "terry-stop", "reasonable-suspicion", "totality-of-the-circumstances", "drug-courier-profile"]
holding: "Factors each individually consistent with innocence can, taken together, amount to reasonable suspicion."
lake:
  record_id: United States v. Sokolow
  status: verified
  projected_at: 2026-07-09
---

# United States v. Sokolow

*490 U.S. 1 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
DEA agents stopped Andrew Sokolow at Honolulu International Airport. He had paid $2,100 in cash for two airline tickets from a roll of $20 bills containing roughly twice that amount, appeared to be traveling under a name that did not match his telephone listing, flew to Miami (a source city) and stayed only 48 hours despite a 20-hour round-trip flight, and checked no luggage. After the stop, a trained dog alerted to his bags, a warrant issued, and cocaine was found. He moved to suppress, and the Ninth Circuit held the stop was not supported by reasonable suspicion.

## Issue
Whether a set of factors, each individually consistent with innocent travel, can together furnish the reasonable suspicion needed for an investigative *[[Terry v. Ohio|Terry]]* stop.

## Rule
Reasonable suspicion is judged by the whole picture, not a divide-and-conquer of innocent explanations: "In evaluating the validity of a stop such as this, we must consider 'the totality of the circumstances — the whole picture.'" — 490 U.S. at 8. ^pin-8

Factors innocent in isolation can combine into reasonable suspicion: "Any one of these factors is not by itself proof of any illegal conduct and is quite consistent with innocent travel. But we think taken together they amount to reasonable suspicion." — [490 U.S. at 9](https://www.courtlistener.com/opinion/112239/united-states-v-sokolow/#:~:text=Any%20one%20of%20these%20factors). ^pin-9

## Application
Sokolow's large cash payment from a roll of $20 bills, his apparent travel under an alias, and his brief 48-hour trip to a source city after a 20-hour round-trip flight were each consistent with innocent travel standing alone. Taken together, however, they gave the agents the minimal objective justification — less than probable cause — needed to stop him. The Ninth Circuit's attempt to sort the evidence into "ongoing criminal activity" versus "probabilistic" categories was rejected.

## Conclusion
The investigative stop was supported by reasonable suspicion under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]; the Supreme Court reversed the Ninth Circuit.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Sokolow* confirms the totality-of-the-circumstances approach to reasonable suspicion drawn from [[United States v. Cortez]] and [[Terry v. Ohio]], and rejects mechanical sorting of factors — an approach reaffirmed in [[United States v. Arvizu]].

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Key — Progeny / Refinement*
- [[Reasonable Suspicion]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Sokolow*, 490 U.S. 1 (1989) — https://www.courtlistener.com/opinion/112239/united-states-v-sokolow/ — pinpoints: 8, 9 (parallel 109 S. Ct. 1581).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6a0afcbf3eed2625", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Sokolow"}, "payload": {"all": [{"cite": "490 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "490"}, {"cite": "109 S. Ct. 1581", "page": "1581", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "109"}, {"cite": "104 L. Ed. 2d 1", "page": "1", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "104"}, {"cite": "1989 U.S. LEXIS 1694", "page": "1694", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1989"}, {"cite": "57 U.S.L.W. 4401", "page": "4401", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "57"}], "display": "490 U.S. 1", "official": {"cite": "490 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "490"}, "official_selection_present": true, "record_id": "United States v. Sokolow"}}
{"assertion_id": "8e64e5f8cac5e144", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-9", "record_id": "United States v. Sokolow"}, "payload": {"fragment": "#:~:text=Any%20one%20of%20these%20factors", "page": null, "pin_id": "pin-9", "pinpoint_status": "star-verified", "quote": "Any one of these factors is not by itself proof of any illegal conduct and is quite consistent with innocent travel. But we think taken together they amount to reasonable suspicion.", "quote_fidelity": "matched", "record_id": "United States v. Sokolow", "star_marker": "9"}}
{"assertion_id": "95243062da7bcefe", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-8", "record_id": "United States v. Sokolow"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-8", "pinpoint_status": "slip-only", "quote": "--- # United States v. Sokolow *490 U.S. 1 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background DEA agents stopped Andrew Sokolow at Honolulu International Airport. He had paid $2,100 in cash for two airline tickets from a roll of $20 bills containing roughly twice that amount, appeared to be traveling under a name that did not match his telephone listing, flew to Miami (a source city) and stayed only 48 hours despite a 20-hour round-trip flight, and checked no luggage. After the stop, a trained dog alerted to his bags, a warrant issued, and cocaine was found. He moved to suppress, and the Ninth Circuit held the stop was not supported by reasonable suspicion. ## Issue Whether a set of factors, each individually consistent with innocent travel, can together furnish the reasonable suspicion needed for an investigative *Terry* stop. ## Rule Reasonable suspicion is judged by the whole picture, not a divide-and-conquer of innocent explanations:", "quote_fidelity": "mismatch", "record_id": "United States v. Sokolow", "star_marker": null}}
{"assertion_id": "9ede94a380d51024", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Sokolow"}, "payload": {"as_of_content": "1989-04-03", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Sokolow", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Sokolow

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Sokolow",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Sokolow",
    "case_name_short": "Sokolow",
    "case_name_full": "United States v. Sokolow",
    "input_case_name": "United States v. Sokolow",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1989-04-03",
    "year": 1989,
    "docket": null,
    "cluster_id": 112239,
    "lead_opinion_id": 112239,
    "sibling_ids": [
      112239,
      9431641,
      9431642
    ],
    "absolute_url": "/opinion/112239/united-states-v-sokolow/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "490 U.S. 1",
      "volume": "490",
      "reporter": "U.S.",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 1581",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1581",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 L. Ed. 2d 1",
        "volume": "104",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4401",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4401",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1989 U.S. LEXIS 1694",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "1694",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "490 U.S. 1",
        "volume": "490",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 1581",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1581",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 L. Ed. 2d 1",
        "volume": "104",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 U.S. LEXIS 1694",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "1694",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4401",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4401",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "490 U.S. 1",
    "official_selection": {
      "court_class": "scotus",
      "selected": "490 U.S. 1",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-8",
      "page": null,
      "quote": "--- # United States v. Sokolow *490 U.S. 1 (1989)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background DEA agents stopped Andrew Sokolow at Honolulu International Airport. He had paid $2,100 in cash for two airline tickets from a roll of $20 bills containing roughly twice that amount, appeared to be traveling under a name that did not match his telephone listing, flew to Miami (a source city) and stayed only 48 hours despite a 20-hour round-trip flight, and checked no luggage. After the stop, a trained dog alerted to his bags, a warrant issued, and cocaine was found. He moved to suppress, and the Ninth Circuit held the stop was not supported by reasonable suspicion. ## Issue Whether a set of factors, each individually consistent with innocent travel, can together furnish the reasonable suspicion needed for an investigative *Terry* stop. ## Rule Reasonable suspicion is judged by the whole picture, not a divide-and-conquer of innocent explanations:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-9",
      "page": null,
      "quote": "Any one of these factors is not by itself proof of any illegal conduct and is quite consistent with innocent travel. But we think taken together they amount to reasonable suspicion.",
      "star_marker": "9",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15785,
      "fragment": "#:~:text=Any%20one%20of%20these%20factors",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1989-04-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Sokolow",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Louisiana v. K.B.",
          "cluster_id": 10581696,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Marlon Juan Lall v. the State of Texas",
          "cluster_id": 10046849,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane1_negative"
      },
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
        "journal_ref": "United States v. Sokolow:lane1_negative"
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
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
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
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alabama v. White",
          "cluster_id": 112454,
          "cite": [
            "110 L. Ed. 2d 301",
            "110 S. Ct. 2412",
            "496 U.S. 325",
            "1990 U.S. LEXIS 3053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
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
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
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
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Pringle",
          "cluster_id": 131150,
          "cite": [
            "157 L. Ed. 2d 769",
            "124 S. Ct. 795",
            "540 U.S. 366",
            "2003 U.S. LEXIS 9198"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Prado Navarette v. California",
          "cluster_id": 2670795,
          "cite": [
            "188 L. Ed. 2d 680",
            "134 S. Ct. 1683",
            "2014 U.S. LEXIS 2930",
            "82 U.S.L.W. 4282",
            "572 U.S. 393",
            "24 Fla. L. Weekly Fed. S 690",
            "2014 WL 1577513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Woods v. State",
          "cluster_id": 1628737,
          "cite": [
            "956 S.W.2d 33",
            "1997 Tex. Crim. App. LEXIS 90",
            "1997 WL 685978"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Balentine v. State",
          "cluster_id": 1662103,
          "cite": [
            "71 S.W.3d 763",
            "2002 WL 496960"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
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
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
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
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Long",
          "cluster_id": 3950093,
          "cite": [
            "713 N.E.2d 1",
            "127 Ohio App. 3d 328"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Derichsweiler v. State",
          "cluster_id": 2539048,
          "cite": [
            "348 S.W.3d 906",
            "2011 Tex. Crim. App. LEXIS 112",
            "2011 WL 255299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scroggins",
          "cluster_id": 71470,
          "cite": [
            "599 F.3d 433",
            "2010 U.S. App. LEXIS 4551",
            "2010 WL 724688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Letner and Tobin",
          "cluster_id": 2630926,
          "cite": [
            "235 P.3d 62",
            "50 Cal. 4th 99",
            "112 Cal. Rptr. 3d 746",
            "2010 Cal. LEXIS 7290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
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
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kikumura, Yu",
          "cluster_id": 551486,
          "cite": [
            "918 F.2d 1084",
            "1990 WL 166030"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Christopher Lee Davis",
          "cluster_id": 1043997,
          "cite": [
            "354 S.W.3d 718",
            "2011 Tenn. LEXIS 962"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Miguel Sandoval",
          "cluster_id": 673938,
          "cite": [
            "29 F.3d 537",
            "1994 U.S. App. LEXIS 16788",
            "1994 WL 321653"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Kevin Gamble (071234)",
          "cluster_id": 2686119,
          "cite": [
            "218 N.J. 412",
            "95 A.3d 188",
            "2014 WL 3858497",
            "2014 N.J. LEXIS 801"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
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
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
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
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
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
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Terry L. Wood",
          "cluster_id": 735391,
          "cite": [
            "106 F.3d 942",
            "1997 U.S. App. LEXIS 2071",
            "1997 WL 49935"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Sokolow:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112239 OR 9431641 OR 9431642) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTk0NzcxMjAwMDAwJnM9NDc2ODE5NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112239+OR+9431641+OR+9431642%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112239 OR 9431641 OR 9431642)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNzYmcz0xMDQxNjY4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112239+OR+9431641+OR+9431642%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112239 OR 9431641 OR 9431642)",
        "reviewed": 112,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 112,
        "triage_read": 2,
        "triage_snippet_classified": 110
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112239 OR 9431641 OR 9431642)",
    "indexed_citing_opinions": 2702,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112239,
        "count": 2400,
        "count_source": "search"
      },
      {
        "opinion_id": 9431641,
        "count": 346,
        "count_source": "search"
      },
      {
        "opinion_id": 9431642,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4656,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-sokolow.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0ODE3MTkmcz0xMDY1MDQxMiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28112239+OR+9431641+OR+9431642%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112239,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 110336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 111280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 111378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 111380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 344185,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 344429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 345525,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 355301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 367117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 374672,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 379013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 380029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 393858,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 402393,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 481401,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112239,
        "cited_id": 496618,
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
    "date_created": "2026-07-06T03:05:35Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:05:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:05:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:08:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:05:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Sokolow

```
<div>
<center><b><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">490 U.S. 1</a></span> (1989)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
SOKOLOW</h1></center>
<center>No. 87-1295.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 10, 1989</center>
<center>Decided April 3, 1989</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
<p><span class="star-pagination">*3</span> <i>Paul J. Larkin, Jr.,</i> argued the cause for the United States. With him on the briefs were <i>Solicitor General Fried, Acting Assistant Attorney General Dennis, Deputy Solicitor General Bryson,</i> and <i>Patty Merkamp Stemler.</i></p>
<p><i>Robert P. Goldberg</i> argued the cause and filed a brief for respondent.</p>
<p>CHIEF JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>Respondent Andrew Sokolow was stopped by Drug Enforcement Administration (DEA) agents upon his arrival at Honolulu International Airport. The agents found 1,063 grams of cocaine in his carry-on luggage. When respondent was stopped, the agents knew, <i>inter alia,</i> that (1) he paid $2,100 for two airplane tickets from a roll of $20 bills; (2) he traveled under a name that did not match the name under which his telephone number was listed; (3) his original destination was Miami, a source city for illicit drugs; (4) he stayed in Miami for only 48 hours, even though a round-trip flight from Honolulu to Miami takes 20 hours; (5) he appeared nervous during his trip; and (6) he checked none of his luggage. A divided panel of the United States Court of Appeals for the Ninth Circuit held that the DEA agents did not have a reasonable suspicion to stop respondent, as required by the Fourth Amendment. <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/" aria-description="Citation for case: United States v. Andrew Sokolow">831 F. 2d 1413</a></span> (1987). We take the contrary view.</p>
<p><span class="star-pagination">*4</span> This case involves a typical attempt to smuggle drugs through one of the Nation's airports.<sup>[1]</sup> On a Sunday in July 1984, respondent went to the United Airlines ticket counter at Honolulu Airport, where he purchased two round-trip tickets for a flight to Miami leaving later that day. The tickets were purchased in the names of "Andrew Kray" and "Janet Norian" and had open return dates. Respondent paid $2,100 for the tickets from a large roll of $20 bills, which appeared to contain a total of $4,000. He also gave the ticket agent his home telephone number. The ticket agent noticed that respondent seemed nervous; he was about 25 years old; he was dressed in a black jumpsuit and wore gold jewelry; and he was accompanied by a woman, who turned out to be Janet Norian. Neither respondent nor his companion checked any of their four pieces of luggage.</p>
<p>After the couple left for their flight, the ticket agent informed Officer John McCarthy of the Honolulu Police Department of respondent's cash purchase of tickets to Miami. Officer McCarthy determined that the telephone number respondent gave to the ticket agent was subscribed to a "Karl Herman," who resided at 348-A Royal Hawaiian Avenue in Honolulu. Unbeknownst to McCarthy (and later to the DEA agents), respondent was Herman's roommate. The ticket agent identified respondent's voice on the answering machine at Herman's number. Officer McCarthy was unable to find any listing under the name "Andrew Kray" in Hawaii. McCarthy subsequently learned that return reservations from Miami to Honolulu had been made in the names of Kray and Norian, with their arrival scheduled for July 25, three days after respondent and his companion had left. He also learned that Kray and Norian were scheduled to make stopovers in Denver and Los Angeles.</p>
<p><span class="star-pagination">*5</span> On July 25, during the stopover in Los Angeles, DEA agents identified respondent. He "appeared to be very nervous and was looking all around the waiting area." App. 43-44. Later that day, at 6:30 p. m., respondent and Norian arrived in Honolulu. As before, they had not checked their luggage. Respondent was still wearing a black jumpsuit and gold jewelry. The couple proceeded directly to the street and tried to hail a cab, where Agent Richard Kempshall and three other DEA agents approached them. Kempshall displayed his credentials, grabbed respondent by the arm, and moved him back onto the sidewalk. Kempshall asked respondent for his airline ticket and identification; respondent said that he had neither. He told the agents that his name was "Sokolow," but that he was traveling under his mother's maiden name, "Kray."</p>
<p>Respondent and Norian were escorted to the DEA office at the airport. There, the couple's luggage was examined by "Donker," a narcotics detector dog, which alerted on respondent's brown shoulder bag. The agents arrested respondent. He was advised of his constitutional rights and declined to make any statements. The agents obtained a warrant to search the shoulder bag. They found no illicit drugs, but the bag did contain several suspicious documents indicating respondent's involvement in drug trafficking. The agents had Donker reexamine the remaining luggage, and this time the dog alerted on a medium-sized Louis Vuitton bag. By now, it was 9:30 p. m., too late for the agents to obtain a second warrant. They allowed respondent to leave for the night, but kept his luggage. The next morning, after a second dog confirmed Donker's alert, the agents obtained a warrant and found 1,063 grams of cocaine inside the bag.</p>
<p>Respondent was indicted for possession with the intent to distribute cocaine in violation of <span class="citation no-link">21 U. S. C. § 841</span>(a)(1). The United States District Court for Hawaii denied his motion to suppress the cocaine and other evidence seized from his luggage, finding that the DEA agents had a reasonable suspicion <span class="star-pagination">*6</span> that he was involved in drug trafficking when they stopped him at the airport. Respondent then entered a conditional plea of guilty to the offense charged.</p>
<p>The United States Court of Appeals for the Ninth Circuit reversed respondent's conviction by a divided vote, holding that the DEA agents did not have a reasonable suspicion to justify the stop. <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/#1423" aria-description="Citation for case: United States v. Andrew Sokolow">831 F. 2d, at 1423</a></span>.<sup>[2]</sup> The majority divided the facts bearing on reasonable suspicion into two categories. In the first category, the majority placed facts describing "ongoing criminal activity," such as the use of an alias or evasive movement through an airport; the majority believed that at least one such factor was always needed to support a finding of reasonable suspicion. <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/#1419" aria-description="Citation for case: United States v. Andrew Sokolow"><i>Id.,</i> at 1419</a></span>. In the second category, it placed facts describing "personal characteristics" of drug couriers, such as the cash payment for tickets, a short trip to a major source city for drugs, nervousness, type of attire, and unchecked luggage. <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/#1420" aria-description="Citation for case: United States v. Andrew Sokolow"><i>Id.,</i> at 1420</a></span>. The majority believed that such characteristics, "shared by drug couriers and the public at large," were only relevant if there was evidence of ongoing criminal behavior and the Government offered "[e]mpirical documentation" that the combination of facts at issue did not describe the behavior of "significant numbers of innocent persons." <i><span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/" aria-description="Citation for case: United States v. Andrew Sokolow">Ibid.</a></span></i> Applying this two-part test to the facts of this case, the majority found that there was no evidence of ongoing criminal behavior, and thus that the agents' stop was impermissible. The dissenting judge took the view that the majority's approach was "overly mechanistic" and "contrary to the case-by-case determination of reasonable articulable suspicion based on <i>all</i> the facts." <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/#1426" aria-description="Citation for case: United States v. Andrew Sokolow"><i>Id.,</i> at 1426</a></span>.</p>
<p><span class="star-pagination">*7</span> We granted certiorari to review the decision of the Court of Appeals, <span class="citation multiple-matches"><a href="/c/U.%20S./486/1042/">486 U. S. 1042</a></span> (1988), because of its serious implications for the enforcement of the federal narcotics laws. We now reverse.</p>
<p>The Court of Appeals held that the DEA agents seized respondent when they grabbed him by the arm and moved him back onto the sidewalk. <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/#1416" aria-description="Citation for case: United States v. Andrew Sokolow">831 F. 2d, at 1416</a></span>. The Government does not challenge that conclusion, and we assume  without deciding  that a stop occurred here. Our decision, then, turns on whether the agents had a reasonable suspicion that respondent was engaged in wrongdoing when they encountered him on the sidewalk. In <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 30</a></span> (1968), we held that the police can stop and briefly detain a person for investigative purposes if the officer has a reasonable suspicion supported by articulable facts that criminal activity "may be afoot," even if the officer lacks probable cause.</p>
<p>The officer, of course, must be able to articulate something more than an "inchoate and unparticularized suspicion or `hunch.' " <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 27</a></span>. The Fourth Amendment requires "some minimal level of objective justification" for making the stop. <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#217" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 217</a></span> (1984). That level of suspicion is considerably less than proof of wrongdoing by a preponderance of the evidence. We have held that probable cause means "a fair probability that contraband or evidence of a crime will be found," <i>Illinois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#238" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 238</a></span> (1983), and the level of suspicion required for a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop is obviously less demanding than that for probable cause, see <i>United States</i> v. <i>Montoya de Hernandez,</i> <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#541" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S. 531, 541, 544</a></span> (1985).</p>
<p>The concept of reasonable suspicion, like probable cause, is not "readily, or even usefully, reduced to a neat set of legal rules." <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#232" aria-description="Citation for case: Illinois v. Gates"><i>Gates, supra,</i> at 232</a></span>. We think the Court of Appeals' effort to refine and elaborate the requirements of "reasonable suspicion" in this case creates unnecessary difficulty in dealing with one of the relatively simple concepts embodied <span class="star-pagination">*8</span> in the Fourth Amendment. In evaluating the validity of a stop such as this, we must consider "the totality of the circumstances  the whole picture." <i>United States</i> v. <i>Cortez,</i> <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 417</a></span> (1981). As we said in <i><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">Cortez</a></span>:</i></p>
<blockquote>"The process does not deal with hard certainties, but with probabilities. Long before the law of probabilities was articulated as such, practical people formulated certain common-sense conclusions about human behavior; jurors as factfinders are permitted to do the same  and so are law enforcement officers." <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#418" aria-description="Citation for case: United States v. Cortez"><i>Id.,</i> at 418</a></span>.</blockquote>
<p>The rule enunciated by the Court of Appeals, in which evidence available to an officer is divided into evidence of "ongoing criminal behavior," on the one hand, and "probabilistic" evidence, on the other, is not in keeping with the quoted statements from our decisions. It also seems to us to draw a sharp line between types of evidence, the probative value of which varies only in degree. The Court of Appeals classified evidence of traveling under an alias, or evidence that the suspect took an evasive or erratic path through an airport, as meeting the test for showing "ongoing criminal activity." But certainly instances are conceivable in which traveling under an alias would not reflect ongoing criminal activity: for example, a person who wished to travel to a hospital or clinic for an operation and wished to conceal that fact. One taking an evasive path through an airport might be seeking to avoid a confrontation with an angry acquaintance or with a creditor. This is not to say that each of these types of evidence is not highly probative, but they do not have the sort of ironclad significance attributed to them by the Court of Appeals.</p>
<p>On the other hand, the factors in this case that the Court of Appeals treated as merely "probabilistic" also have probative significance. Paying $2,100 in cash for two airplane tickets is out of the ordinary, and it is even more out of the ordinary to pay that sum from a roll of $20 bills containing nearly twice that amount of cash. Most business travelers, we feel confident, purchase airline tickets by credit card or check so as to <span class="star-pagination">*9</span> have a record for tax or business purposes, and few vacationers carry with them thousands of dollars in $20 bills. We also think the agents had a reasonable ground to believe that respondent was traveling under an alias; the evidence was by no means conclusive, but it was sufficient to warrant consideration.<sup>[3]</sup> While a trip from Honolulu to Miami, standing alone, is not a cause for any sort of suspicion, here there was more: surely few residents of Honolulu travel from that city for 20 hours to spend 48 hours in Miami during the month of July.</p>
<p>Any one of these factors is not by itself proof of any illegal conduct and is quite consistent with innocent travel. But we think taken together they amount to reasonable suspicion. See <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#502" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 502</a></span> (1983) (opinion of WHITE, J.); <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#515" aria-description="Citation for case: Florida v. Royer"><i>id.,</i> at 515-516</a></span> (BLACKMUN, J., dissenting); <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#523" aria-description="Citation for case: Florida v. Royer"><i>id.,</i> at 523-524</a></span> (REHNQUIST, J., dissenting).<sup>[4]</sup> We said in <i>Reid</i> v. <i>Georgia,</i> <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">448 U. S. 438</a></span> (1980) <i>(per curiam)</i><i>,</i> "there could, of course, be circumstances in which wholly lawful conduct might justify the suspicion that criminal activity was afoot." <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#441" aria-description="Citation for case: Reid v. Georgia"><i>Id.,</i> at 441</a></span>.<sup>[5]</sup> Indeed, <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> itself involved "a series of acts, <span class="star-pagination">*10</span> each of them perhaps innocent" if viewed separately, "but which taken together warranted further investigation." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 22</a></span>; see also <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez"><i>Cortez, supra,</i> at 417-419</a></span>. We noted in <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#243" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 243-244, n. 13</a></span>, that "innocent behavior will frequently provide the basis for a showing of probable cause," and that "[i]n making a determination of probable cause the relevant inquiry is not whether particular conduct is `innocent' or `guilty,' but the degree of suspicion that attaches to particular types of noncriminal acts." That principle applies equally well to the reasonable suspicion inquiry.</p>
<p>We do not agree with respondent that our analysis is somehow changed by the agents' belief that his behavior was consistent with one of the DEA's "drug courier profiles."<sup>[6]</sup> Brief for Respondent 14-21. A court sitting to determine the existence of reasonable suspicion must require the agent to articulate the factors leading to that conclusion, but the fact that these factors may be set forth in a "profile" does not somehow detract from their evidentiary significance as seen by a trained agent.</p>
<p>Respondent also contends that the agents were obligated to use the least intrusive means available to verify or dispel their suspicions that he was smuggling narcotics. <i>Id.,</i> at 12-13, 21-23. In respondent's view, the agents should have simply approached and spoken with him, rather than forcibly detaining him. He points to the statement in <i>Florida</i> v. <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer"><i>Royer, supra,</i> at 500</a></span> (opinion of WHITE, J.), that "the investigative <span class="star-pagination">*11</span> methods employed should be the least intrusive means reasonably available to verify or dispel the officer's suspicion in a short period of time." That statement, however, was directed at the length of the investigative stop, not at whether the police had a less intrusive means to verify their suspicions before stopping Royer. The reasonableness of the officer's decision to stop a suspect does not turn on the availability of less intrusive investigatory techniques. Such a rule would unduly hamper the police's ability to make swift, on-the-spot decisions  here, respondent was about to get into a taxicab  and it would require courts to "indulge in `unrealistic second-guessing.' " <i>Montoya de Hernandez,</i> <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#542" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S., at 542</a></span>, quoting <i>United States</i> v. <i>Sharpe,</i> <span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#686" aria-description="Citation for case: United States v. Sharpe">470 U. S. 675, 686, 687</a></span> (1985).</p>
<p>We hold that the agents had a reasonable basis to suspect that respondent was transporting illegal drugs on these facts. The judgment of the Court of Appeals is therefore reversed, and the case is remanded for further proceedings consistent with our decision.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE MARSHALL, with whom JUSTICE BRENNAN joins, dissenting.</p>
<p>Because the strongest advocates of Fourth Amendment rights are frequently criminals, it is easy to forget that our interpretations of such rights apply to the innocent and the guilty alike. <i>Illinois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#290" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 290</a></span> (1983) (BRENNAN, J., dissenting). In the present case, the chain of events set in motion when respondent Andrew Sokolow was stopped by Drug Enforcement Administration (DEA) agents at Honolulu International Airport led to the discovery of cocaine and, ultimately, to Sokolow's conviction for drug trafficking. But in sustaining this conviction on the ground that the agents reasonably suspected Sokolow of ongoing criminal activity, the Court diminishes the rights of <i>all</i> citizens "to be secure in their persons," U. S. Const., Amdt. 4, as they <span class="star-pagination">*12</span> traverse the Nation's airports. Finding this result constitutionally impermissible, I dissent.</p>
<p>The Fourth Amendment cabins government's authority to intrude on personal privacy and security by requiring that searches and seizures usually be supported by a showing of probable cause. The reasonable-suspicion standard is a derivation of the probable-cause command, applicable only to those brief detentions which fall short of being full-scale searches and seizures and which are necessitated by law enforcement exigencies such as the need to stop ongoing crimes, to prevent imminent crimes, and to protect law enforcement officers in highly charged situations. <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 30</a></span> (1968). By requiring reasonable suspicion as a prerequisite to such seizures, the Fourth Amendment protects innocent persons from being subjected to "overbearing or harassing" police conduct carried out solely on the basis of imprecise stereotypes of what criminals look like, or on the basis of irrelevant personal characteristics such as race. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#14" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 14-15</a></span>, and n. 11 (citation omitted).</p>
<p>To deter such egregious police behavior, we have held that a suspicion is not reasonable unless officers have based it on "specific and articulable facts." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 21</a></span>; see also <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#880" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 880</a></span> (1975). It is not enough to suspect that an individual has committed crimes in the past, harbors unconsummated criminal designs, or has the propensity to commit crimes. On the contrary, before detaining an individual, law enforcement officers must reasonably suspect that he is engaged in, or poised to commit, a criminal act <i>at that moment.</i> See, <i>e. g., </i><i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 51</a></span> (1979) (to detain, officers must "have a reasonable suspicion, based on objective facts, that the individual is involved in criminal activity"); <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 30</a></span> (reasonable suspicion exists only where policeman reasonably concludes, <i>inter alia,</i> "that criminal activity may be afoot"). The rationale for permitting brief, warrantless seizures is, after all, that it is impractical to demand strict compliance <span class="star-pagination">*13</span> with the Fourth Amendment's ordinary probable-cause requirement in the face of ongoing or imminent criminal activity demanding "swift action predicated upon the on-the-spot observations of the officer on the beat." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 20</a></span>. Observations raising suspicions of past criminality demand no such immediate action, but instead should appropriately trigger routine police investigation, which may ultimately generate sufficient information to blossom into probable cause.</p>
<p>Evaluated against this standard, the facts about Andrew Sokolow known to the DEA agents at the time they stopped him fall short of reasonably indicating that he was engaged at the time in criminal activity. It is highly significant that the DEA agents stopped Sokolow because he matched one of the DEA's "profiles" of a paradigmatic drug courier. In my view, a law enforcement officer's mechanistic application of a formula of personal and behavioral traits in deciding whom to detain can only dull the officer's ability and determination to make sensitive and fact-specific inferences "in light of his experience," <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 27</a></span>, particularly in ambiguous or borderline cases. Reflexive reliance on a profile of drug courier characteristics runs a far greater risk than does ordinary, case-by-case police work of subjecting innocent individuals to unwarranted police harassment and detention. This risk is enhanced by the profile's "chameleon-like way of adapting to any particular set of observation." <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/#1418" aria-description="Citation for case: United States v. Andrew Sokolow">831 F. 2d 1413, 1418</a></span> (CA9 1987). Compare, <i>e. g., </i><i>United States</i> v. <i>Moore,</i> <span class="citation" data-id="402393"><a href="/opinion/402393/united-states-v-ronnie-d-moore/#803" aria-description="Citation for case: United States v. Ronnie D. Moore">675 F. 2d 802, 803</a></span> (CA6 1982) (suspect was first to deplane), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./460/1068/">460 U. S. 1068</a></span> (1983), with <i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#564" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 564</a></span> (1980) (last to deplane), with <i>United States</i> v. <i>Buenaventura-Ariza,</i> <span class="citation" data-id="374672"><a href="/opinion/374672/united-states-v-jorge-buenaventura-ariza-and-delores-quiroz-santi/#31" aria-description="Citation for case: United States v. Jorge Buenaventura-Ariza and Delores...">615 F. 2d 29, 31</a></span> (CA2 1980) (deplaned from middle); <i>United States</i> v. <i>Sullivan,</i> <span class="citation" data-id="380029"><a href="/opinion/380029/united-states-v-diann-pansey-sullivan-aka-brenda-rowe-kathy-ruth/#12" aria-description="Citation for case: United States v. Diann Pansey Sullivan, A/K/A Brenda...">625 F. 2d 9, 12</a></span> (CA4 1980) (one-way tickets), with <i>United States</i> v. <i>Craemer,</i> <span class="citation" data-id="345525"><a href="/opinion/345525/united-states-v-james-mitchell-craemer/#595" aria-description="Citation for case: United States v. James Mitchell Craemer">555 F. 2d 594, 595</a></span> (CA6 1977) (round-trip tickets), with <i>United States</i> v. <i>McCaleb,</i> <span class="citation" data-id="344429"><a href="/opinion/344429/united-states-v-robert-ross-mccaleb-and-brenda-page/#720" aria-description="Citation for case: United States v. Robert Ross McCaleb and Brenda Page">552 F. 2d 717, 720</a></span> (CA6 1977) (nonstop flight), with <i>United States</i> v. <i>Sokolow,</i> <span class="citation" data-id="9475720"><a href="/opinion/481401/united-states-v-andrew-sokolow/#1370" aria-description="Citation for case: United States v. Andrew Sokolow">808 F. 2d 1366, 1370</a></span> (CA9), vacated, 831 F. 2d 1413 <span class="star-pagination">*14</span> (1987) (case below) (changed planes); <span class="citation" data-id="345525"><a href="/opinion/345525/united-states-v-james-mitchell-craemer/#595" aria-description="Citation for case: United States v. James Mitchell Craemer"><i>Craemer, supra,</i> at 595</a></span> (no luggage), with <i>United States</i> v. <i>Sanford,</i> <span class="citation" data-id="9468329"><a href="/opinion/393858/united-states-v-jesse-lee-sanford/#343" aria-description="Citation for case: United States v. Jesse Lee Sanford">658 F. 2d 342, 343</a></span> (CA5 1981) (gym bag), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./455/991/">455 U. S. 991</a></span> (1982), with <span class="citation" data-id="380029"><a href="/opinion/380029/united-states-v-diann-pansey-sullivan-aka-brenda-rowe-kathy-ruth/#12" aria-description="Citation for case: United States v. Diann Pansey Sullivan, A/K/A Brenda..."><i>Sullivan, supra,</i> at 12</a></span> (new suitcases); <i>United States</i> v. <i>Smith,</i> <span class="citation" data-id="9464735"><a href="/opinion/355301/united-states-v-erma-smith/#883" aria-description="Citation for case: United States v. Erma Smith">574 F. 2d 882, 883</a></span> (CA6 1978) (traveling alone), with <i>United States</i> v. <i>Fry,</i> <span class="citation" data-id="379013"><a href="/opinion/379013/united-states-v-william-monroe-fry-jr/#1219" aria-description="Citation for case: United States v. William Monroe Fry, Jr.">622 F. 2d 1218, 1219</a></span> (CA5 1980) (traveling with companion); <i>United States</i> v. <i>Andrews,</i> <span class="citation" data-id="367117"><a href="/opinion/367117/united-states-v-tallice-andrews/#566" aria-description="Citation for case: United States v. Tallice Andrews">600 F. 2d 563, 566</a></span> (CA6 1979) (acted nervously), cert. denied <i>sub nom. </i><i>Brooks</i> v. <i>United States,</i> <span class="citation" data-id="9017003"><a href="/opinion/9023762/brooks-v-united-states/" aria-description="Citation for case: Brooks v. United States">444 U. S. 878</a></span> (1979), with <i>United States</i> v. <i>Himmelwright,</i> <span class="citation" data-id="344185"><a href="/opinion/344185/united-states-v-mary-ann-himmelwright/#992" aria-description="Citation for case: United States v. Mary Ann Himmelwright">551 F. 2d 991, 992</a></span> (CA5) (acted too calmly), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./434/902/">434 U. S. 902</a></span> (1977). In asserting that it is not "somehow" relevant that the agents who stopped Sokolow did so in reliance on a prefabricated profile of criminal characteristics, <i>ante,</i> at 10, the majority thus ducks serious issues relating to a questionable law enforcement practice, to address the validity of which we granted certiorari in this case.<sup>[1]</sup></p>
<p>That the factors comprising the drug courier profile relied on in this case are especially dubious indices of ongoing criminal activity is underscored by <i>Reid</i> v. <i>Georgia,</i> <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">448 U. S. 438</a></span> (1980), a strikingly similar case. There, four facts, encoded in a drug courier profile, were alleged in support of the DEA's detention of a suspect at the Atlanta Airport. First, Reid had arrived from Fort Lauderdale, Florida, a source city for cocaine. Second, he arrived in the early morning, when law enforcement activity is diminished. Third, he and his companion appeared to have no luggage other than their shoulder bags. And fourth, he and his companion appeared to be trying to conceal the fact that they were traveling together. <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#440" aria-description="Citation for case: Reid v. Georgia"><i>Id.,</i> at 440-441</a></span>.</p>
<p>This collection of facts, we held, was inadequate to support a finding of reasonable suspicion. All but the last of these facts, we observed, "describe a very large category of presumably <span class="star-pagination">*15</span> innocent travelers, who would be subject to virtually random seizures were the Court to conclude that as little foundation as there was in this case could justify a seizure." <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#441" aria-description="Citation for case: Reid v. Georgia"><i>Id.,</i> at 441</a></span>. The sole fact that suggested criminal activity was that Reid "preceded another person and occasionally looked backward at him as they proceeded through the concourse." <i><span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">Ibid.</a></span></i> This observation did not of itself provide a reasonable basis for suspecting wrongdoing, for inferring criminal activity from such evidence reflected no more than an " `inchoate and unparticularized suspicion or "hunch." ' " <i>Ibid.,</i> quoting <i>Terry,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 27</a></span>.<sup>[2]</sup></p>
<p>The facts known to the DEA agents at the time they detained the traveler in this case are scarcely more suggestive of ongoing criminal activity than those in <i><span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">Reid</a></span>.</i> Unlike traveler Reid, who sought to conceal the fact that he was traveling with a companion, and who even attempted to run away after being approached by a DEA agent, <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#439" aria-description="Citation for case: Reid v. Georgia">448 U. S., at 439</a></span>, traveler Sokolow gave no indications of evasive activity. On the contrary, the sole behavioral detail about Sokolow noted by the DEA agents was that he was nervous. With news accounts proliferating of plane crashes, near collisions, and air terrorism, there are manifold and good reasons for being agitated while awaiting a flight, reasons that have nothing to do with one's involvement in a criminal endeavor.</p>
<p>The remaining circumstantial facts known about Sokolow, considered either singly or together, are scarcely indicative of criminal activity. Like the information disavowed in <i><span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">Reid</a></span></i> as nonprobative, the fact that Sokolow took a brief trip to a <span class="star-pagination">*16</span> resort city for which he brought only carry-on luggage also "describe[s] a very large category of presumably innocent travelers." <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#441" aria-description="Citation for case: Reid v. Georgia"><i>Id.,</i> at 441</a></span>. That Sokolow embarked from Miami, "a source city for illicit drugs," <i>ante,</i> at 3, is no more suggestive of illegality; thousands of innocent persons travel from "source cities" every day and, judging from the DEA's testimony in past cases, nearly every major city in the country may be characterized as a source or distribution city. See, <i>e. g., </i><i>Buenaventura-Ariza,</i> <span class="citation" data-id="374672"><a href="/opinion/374672/united-states-v-jorge-buenaventura-ariza-and-delores-quiroz-santi/#31" aria-description="Citation for case: United States v. Jorge Buenaventura-Ariza and Delores...">615 F. 2d, at 31, n. 5</a></span>. That Sokolow had his phone listed in another person's name also does not support the majority's assertion that the DEA agents reasonably believed Sokolow was using an alias; it is commonplace to have one's phone registered in the name of a roommate, which, it later turned out, was precisely what Sokolow had done.<sup>[3]</sup> That Sokolow was dressed in a black jumpsuit and wore gold jewelry also provides no grounds for suspecting wrongdoing, the majority's repeated and unexplained allusions to Sokolow's style of dress notwithstanding. <i>Ante,</i> at 4, 5. For law enforcement officers to base a search, even in part, on a "pop" guess that persons dressed in a particular fashion are likely to commit crimes not only stretches the concept of reasonable suspicion beyond recognition, but also is inimical to the self-expression which the choice of wardrobe may provide.</p>
<p>Finally, that Sokolow paid for his tickets in cash indicates no imminent or ongoing criminal activity. The majority "feel[s] confident" that "[m]ost business travelers . . . purchase airline tickets by credit card or check." <i>Ante,</i> at 8. Why the majority confines its focus only to "business travelers" I do not know, but I would not so lightly infer ongoing crime from the use of legal tender. Making major cash purchases, while surely less common today, may simply reflect the traveler's aversion to, or inability to obtain, plastic <span class="star-pagination">*17</span> money. Conceivably, a person who spends large amounts of cash may be trying to launder his proceeds from <i>past</i> criminal enterprises by converting them into goods and services. But, as I have noted, investigating completed episodes of crime goes beyond the appropriately limited purview of the brief, <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i>-style seizure. Moreover, it is unreasonable to suggest that, had Sokolow left the airport, he would have been gone forever and thus immune from subsequent investigation. <i>Ante,</i> at 11. Sokolow, after all, had given the airline his phone number, and the DEA, having ascertained that it was indeed Sokolow's voice on the answering machine at that number, could have learned from that information where Sokolow resided.</p>
<p>The fact is that, unlike the taking of patently evasive action, <i>Florida</i> v. <i>Rodriguez,</i> <span class="citation" data-id="9429786"><a href="/opinion/111280/florida-v-rodriguez/#6" aria-description="Citation for case: Florida v. Rodriguez">469 U. S. 1, 6</a></span> (1984), the use of an alias, <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#502" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 502</a></span> (1983), the casing of a store, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#6" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 6</a></span>, or the provision of a reliable report from an informant that wrongdoing is imminent, <i>Illinois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#225" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 225-227</a></span>, nothing about the characteristics shown by airport traveler Sokolow reasonably suggests that criminal activity is afoot. The majority's hasty conclusion to the contrary serves only to indicate its willingness, when drug crimes or antidrug policies are at issue, to give short shrift to constitutional rights. See, <i>e. g., </i><i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#636" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602, 636</a></span> (1989) (MARSHALL, J., dissenting).<sup>[4]</sup> In requiring that seizures be based on at least some evidence of criminal conduct, <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/#1419" aria-description="Citation for case: United States v. Andrew Sokolow">831 F. 2d, at 1419</a></span>, the Court of Appeals was faithful to the Fourth Amendment principle that law enforcement officers <span class="star-pagination">*18</span> must reasonably suspect a person of criminal activity before they can detain him. Because today's decision, though limited to its facts, <i>ante,</i> at 11, disobeys this important constitutional command, I dissent.</p>
<h2>NOTES</h2>
<p>[1]  The facts in this case were developed at suppression hearings held in the District Court over three separate days. The parties also stipulated to certain facts.</p>
<p>[2]  In an earlier decision, the Court of Appeals also reversed the District Court, but on the basis of different reasoning. <span class="citation" data-id="9475720"><a href="/opinion/481401/united-states-v-andrew-sokolow/" aria-description="Citation for case: United States v. Andrew Sokolow">808 F. 2d 1366</a></span>, vacated, <span class="citation" data-id="9476856"><a href="/opinion/496618/united-states-v-andrew-sokolow/" aria-description="Citation for case: United States v. Andrew Sokolow">831 F. 2d 1413</a></span> (1987). The Court of Appeals' second decision was issued after the Government petitioned for rehearing on the ground that the court had erred in considering each of the facts known to the agents separately rather than in terms of the totality of the circumstances.</p>
<p>[3]  Respondent also claims that the agents should have conducted a further inquiry to resolve the inconsistency between the name he gave the airline and the name, "Karl Herman," under which his telephone number was listed. Brief for Respondent 26. This argument avails respondent nothing; had the agents done further checking, they would have discovered not only that respondent was Herman's roommate but also that his name was "Sokolow" and not "Kray," the name listed on his ticket.</p>
<p>[4]  In <i><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span>,</i> the police were aware, <i>inter alia,</i> that (1) Royer was traveling under an assumed name; (2) he paid for his ticket in cash with a number of small bills; (3) he was traveling from Miami to New York; (4) he put only his name and not an address on his checked luggage; and (5) he seemed nervous while walking through Miami airport. <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#493" aria-description="Citation for case: Florida v. Royer">460 U. S., at 493, n. 2, 502</a></span> (opinion of WHITE, J.).</p>
<p>[5]  In <i><span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">Reid</a></span>,</i> the Court held that a DEA agent stopped the defendant without reasonable suspicion. At the time of the stop, the agent knew that (1) the defendant flew into Atlanta from Fort Lauderdale, a source city for cocaine; (2) he arrived early in the morning, when police activity was believed to be at a low ebb; (3) he did not check his luggage; and (4) the defendant and his companion appeared to be attempting to hide the fact that they were together. The Court held that the first three of these facts were not sufficient to supply reasonable suspicion, because they "describe a very large category of presumably innocent travelers," while the last fact was insufficient on the facts of that case to establish reasonable suspicion. <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#441" aria-description="Citation for case: Reid v. Georgia">448 U. S., at 441</a></span>.</p>
<p>[6]  Agent Kempshall testified that respondent's behavior "had all the classic aspects of a drug courier." App. 59. Since 1974, the DEA has trained narcotics officers to identify drug smugglers on the basis of the sort of circumstantial evidence at issue here.</p>
<p>[1]  Even if such profiles had reliable predictive value, their utility would be short lived, for drug couriers will adapt their behavior to sidestep detection from profile-focused officers.</p>
<p>[2]  Nor was <i><span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">Reid</a></span></i> a close case: eight Members of the Court found the challenged detention insupportable, five of whom saw fit to dispose of the case by reversing the court below in a <i>per curiam</i> opinion. In a separate concurrence, Justice Powell, joined by Chief Justice Burger and JUSTICE BLACKMUN, agreed that "the fragmentary facts apparently relied on by the DEA agents" provided "no justification" for Reid's detention. <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#442" aria-description="Citation for case: Reid v. Georgia">448 U. S., at 442, n. 1</a></span>. Only then-JUSTICE REHNQUIST, the author of today's majority opinion, dissented, on the ground that the police conduct involved did not implicate Reid's constitutional rights. <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#442" aria-description="Citation for case: Reid v. Georgia"><i>Id.,</i> at 442</a></span>.</p>
<p>[3]  That Sokolow was, in fact, using an alias was not known to the DEA agents until <i>after</i> they detained him. Thus, it cannot legitimately be considered as a basis for the seizure in this case.</p>
<p>[4]  The majority also contends that it is not relevant that the DEA agents, in forcibly stopping Sokolow rather than simply speaking with him, did not "use the least intrusive means available." <i>Ante,</i> at 10. On the contrary, the manner in which a search is carried out  and particularly whether law enforcement officers have taken needlessly intrusive steps  is a highly important index of reasonableness under Fourth Amendment doctrine. See, <i>e. g., </i><i>Winston</i> v. <i>Lee,</i> <span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/#760" aria-description="Citation for case: Winston v. Lee">470 U. S. 753, 760-761</a></span> (1985).</p>

</div>
```

---
