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

## GROUP: content/cases/Ornelas v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Ornelas v. United States"
type: case
citation: "517 U.S. 690 (1996)"
parallel_cite: "116 S. Ct. 1657; 134 L. Ed. 2d 911"
neutral_cite: 1996 U.S. LEXIS 3391
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1996
date_decided: 1996-06-10
docket: 95-5257
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1996-06-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Ornelas v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118030/ornelas-v-united-states/"
  cluster_id: 118030
  opinion_id: 118030
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Key — Progeny / Refinement"
related: ["[[Illinois v. Gates]]", "[[Brinegar v. United States]]", "[[Terry v. Ohio]]", "[[Devenpeck v. Alford]]"]
aliases: []
tags: ["case", "fourth-amendment", "probable-cause", "reasonable-suspicion", "standard-of-review", "de-novo"]
holding: "Appellate review of determinations of reasonable suspicion and probable cause to make a warrantless search/stop is de novo (historical…"
lake:
  record_id: Ornelas v. United States
  status: verified
  projected_at: 2026-07-09
---

# Ornelas v. United States

*517 U.S. 690 (1996)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A 20-year veteran detective conducting drug-interdiction surveillance in Milwaukee noticed a car with California plates and, after a records check, stopped and questioned Ornelas and a companion. The detective searched the car and found two kilograms of cocaine behind a loose interior panel. The District Court found reasonable suspicion for the stop and probable cause for the search and denied suppression; the Seventh Circuit reviewed those determinations "deferentially," for "clear error."

## Issue
What standard of review applies on appeal to a trial court's determinations of reasonable suspicion to make a stop and probable cause to conduct a warrantless search.

## Rule
The ultimate determinations are reviewed [[Common Legal Terms#de-novo|de novo]]. "We hold that the ultimate questions of reasonable suspicion and probable cause to make a warrantless search should be reviewed *de novo*." — 517 U.S. at 691. ^pin-691

"We therefore hold that as a general matter determinations of reasonable suspicion and probable cause should be reviewed *de novo* on appeal." — 517 U.S. at 699. ^pin-699

At the same time, "a reviewing court should take care both to review findings of historical fact only for clear error and to give due weight to inferences drawn from those facts by resident judges and local law enforcement officers." — [*Id.* at 699–700](https://www.courtlistener.com/opinion/118030/ornelas-v-united-states/#:~:text=a%20reviewing%20court%20should%20take). ^pin-699a

## Application
The Seventh Circuit had reviewed the reasonable-suspicion and probable-cause rulings only for [[Common Legal Terms#clear-error|clear error]]. Because the ultimate mixed questions of reasonable suspicion and probable cause must instead be reviewed [[Common Legal Terms#de-novo|de novo]] — while the historical facts (here, the officer's observations and the loose panel) are reviewed for [[Common Legal Terms#clear-error|clear error]] with due weight to his experience-based inferences — the Court [[Reading and Citing Cases#vacated|vacated]] the judgment and [[Reading and Citing Cases#on-remand|remanded]] for the Court of Appeals to review those determinations [[Common Legal Terms#de-novo|de novo]].

## Conclusion
Reasonable-suspicion and probable-cause determinations get independent, [[Common Legal Terms#de-novo|de novo]] appellate review (with clear-error review of the underlying historical facts); the judgment was [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. The [[Common Legal Terms#de-novo|de novo]] standard for reviewing reasonable suspicion and probable cause remains controlling.

## Appears on
- [[Probable Cause]] — *Key — Progeny / Refinement*

## Sources
- *Ornelas v. United States*, 517 U.S. 690 (1996) — https://www.courtlistener.com/opinion/118030/ornelas-v-united-states/ — pinpoints: 691, 699–700.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e5bca037877308e1", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "517 U.S. 690 (1996)", "court": "U.S. Supreme Court", "neutral_cite": "1996 U.S. LEXIS 3391", "official_citation_present": true, "parallel_cite": "116 S. Ct. 1657; 134 L. Ed. 2d 911", "title": "Ornelas v. United States", "year": "1996"}}
{"assertion_id": "9409324855c75e38", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Appellate review of determinations of reasonable suspicion and probable cause to make a warrantless search/stop is de novo (historical…", "title": "Ornelas v. United States"}}
{"assertion_id": "94d1dcc75040637a", "dimension": "support", "kind": "home_role", "locator": {"home": "Probable Cause"}, "payload": {"home": "Probable Cause", "role": "Key — Progeny / Refinement", "title": "Ornelas v. United States"}}
{"assertion_id": "8aeeb098101e1916", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1996-06-10", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Ornelas v. United States", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Ornelas v. United States", "varies_by_point": "false"}}
{"assertion_id": "d20ca7e1e8785a85", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Ornelas v. United States"}}
```

### lake record — Ornelas v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Ornelas v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Ornelas v. United States",
    "case_name_short": "Ornelas",
    "case_name_full": "ORNELAS Et Al. v. UNITED STATES",
    "input_case_name": "Ornelas v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1996-06-10",
    "year": 1996,
    "docket": "95-5257",
    "cluster_id": 118030,
    "lead_opinion_id": 118030,
    "sibling_ids": [
      118030,
      9433305,
      9433306
    ],
    "absolute_url": "/opinion/118030/ornelas-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9283005,
        "score": 20,
        "case_name": "Ornelas-Martinez v. United States"
      },
      {
        "cluster_id": 9273679,
        "score": 20,
        "case_name": "Ornelas v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "517 U.S. 690",
      "volume": "517",
      "reporter": "U.S.",
      "page": "690",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "116 S. Ct. 1657",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "1657",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "134 L. Ed. 2d 911",
        "volume": "134",
        "reporter": "L. Ed. 2d",
        "page": "911",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1996 U.S. LEXIS 3391",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "3391",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "517 U.S. 690",
        "volume": "517",
        "reporter": "U.S.",
        "page": "690",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "116 S. Ct. 1657",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "1657",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "134 L. Ed. 2d 911",
        "volume": "134",
        "reporter": "L. Ed. 2d",
        "page": "911",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1996 U.S. LEXIS 3391",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "3391",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "517 U.S. 690",
    "official_selection": {
      "court_class": "scotus",
      "selected": "517 U.S. 690",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-691",
      "page": null,
      "quote": "## Issue What standard of review applies on appeal to a trial court's determinations of reasonable suspicion to make a stop and probable cause to conduct a warrantless search. ## Rule The ultimate determinations are reviewed de novo.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-699",
      "page": null,
      "quote": "We therefore hold that as a general matter determinations of reasonable suspicion and probable cause should be reviewed *de novo* on appeal.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-699a",
      "page": null,
      "quote": "a reviewing court should take care both to review findings of historical fact only for clear error and to give due weight to inferences drawn from those facts by resident judges and local law enforcement officers.",
      "star_marker": "699",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 24571,
      "fragment": "#:~:text=a%20reviewing%20court%20should%20take",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1996-06-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Ornelas v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Wright",
          "cluster_id": 10658752,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane1_negative"
      },
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
        "journal_ref": "Ornelas v. United States:lane1_negative"
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
        "journal_ref": "Ornelas v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Guzman v. State",
          "cluster_id": 2449770,
          "cite": [
            "955 S.W.2d 85",
            "1997 Tex. Crim. App. LEXIS 72",
            "1997 WL 587024"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edward H. Phillips v. Awh Corporation, Hopeman Brothers, Inc., and Lofton Corporation, Defendants-Cross",
          "cluster_id": 791122,
          "cite": [
            "415 F.3d 1303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460854,
          "cite": [
            "583 U.S. 48",
            "138 S. Ct. 577",
            "199 L. Ed. 2d 453",
            "2018 U.S. LEXIS 760"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gasperini v. Center for Humanities, Inc.",
          "cluster_id": 2528498,
          "cite": [
            "135 L. Ed. 2d 659",
            "116 S. Ct. 2211",
            "518 U.S. 415",
            "1996 U.S. LEXIS 4051",
            "64 U.S.L.W. 4607",
            "96 Cal. Daily Op. Serv. 4548",
            "10 Fla. L. Weekly Fed. S 26",
            "96 Daily Journal DAR 7338"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herring v. United States",
          "cluster_id": 145922,
          "cite": [
            "172 L. Ed. 2d 496",
            "129 S. Ct. 695",
            "555 U.S. 135",
            "2009 U.S. LEXIS 581"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bajakajian",
          "cluster_id": 118234,
          "cite": [
            "141 L. Ed. 2d 314",
            "118 S. Ct. 2028",
            "524 U.S. 321",
            "1998 U.S. LEXIS 4172"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nicholas Omar Midgette",
          "cluster_id": 796984,
          "cite": [
            "478 F.3d 616",
            "2007 U.S. App. LEXIS 4153",
            "2007 WL 572127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Chicago v. Morales",
          "cluster_id": 118299,
          "cite": [
            "144 L. Ed. 2d 67",
            "119 S. Ct. 1849",
            "527 U.S. 41",
            "1999 U.S. LEXIS 4005"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lilly v. Virginia",
          "cluster_id": 118300,
          "cite": [
            "144 L. Ed. 2d 117",
            "119 S. Ct. 1887",
            "527 U.S. 116",
            "1999 U.S. LEXIS 4006"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Muehler v. Mena",
          "cluster_id": 142878,
          "cite": [
            "161 L. Ed. 2d 299",
            "125 S. Ct. 1465",
            "544 U.S. 93",
            "2005 U.S. LEXIS 2755"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cooper Industries, Inc. v. Leatherman Tool Group, Inc.",
          "cluster_id": 118424,
          "cite": [
            "149 L. Ed. 2d 674",
            "121 S. Ct. 1678",
            "532 U.S. 424",
            "2001 U.S. LEXIS 3520",
            "2001 Cal. Daily Op. Serv. 3820",
            "69 U.S.L.W. 4299",
            "58 U.S.P.Q. 2d (BNA) 1641",
            "2001 Daily Journal DAR 4673",
            "2001 Colo. J. C.A.R. 2407",
            "14 Fla. L. Weekly Fed. S 223"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Messerschmidt v. Millender",
          "cluster_id": 623242,
          "cite": [
            "182 L. Ed. 2d 47",
            "132 S. Ct. 1235",
            "565 U.S. 535",
            "2012 U.S. LEXIS 1687"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garcia v. State",
          "cluster_id": 1382816,
          "cite": [
            "43 S.W.3d 527",
            "2001 Tex. Crim. App. LEXIS 30",
            "2001 WL 387433"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460811,
          "cite": [
            "583 U.S. 48"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael B. Smith v. Douglas Lamz and the Village of Algonquin, a Municipal Corporation",
          "cluster_id": 781088,
          "cite": [
            "321 F.3d 680",
            "2003 U.S. App. LEXIS 3888",
            "2003 WL 730093"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118030 OR 9433305 OR 9433306) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjgxODYyNDAwMDAwJnM9OTM5MjY5OCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118030+OR+9433305+OR+9433306%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118030 OR 9433305 OR 9433306)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MDAmcz03OTA0ODUmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118030+OR+9433305+OR+9433306%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118030 OR 9433305 OR 9433306)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjk2MjA0ODAwMDAwJnM9OTQzMDcwNiZ0PW8mZD0yMDI2LTA3LTA2JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118030+OR+9433305+OR+9433306%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118030 OR 9433305 OR 9433306)",
    "indexed_citing_opinions": 4083,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118030,
        "count": 3455,
        "count_source": "search"
      },
      {
        "opinion_id": 9433305,
        "count": 699,
        "count_source": "search"
      },
      {
        "opinion_id": 9433306,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 7200,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/ornelas-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0Nzg2MzYmcz0xMDY0ODY0NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118030+OR+9433305+OR+9433306%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118030,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 106071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 110336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 110698,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 111373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 111542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 112137,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 112239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 112454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 112457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 112564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 112608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 117937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 117982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 537758,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 538805,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 561395,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 583951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 597487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 663109,
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
    "date_created": "2026-07-05T16:25:07Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:25:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:25:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:28:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:25:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Ornelas v. United States

```
<div>
<center><b><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/" aria-description="Citation for case: Ornelas v. United States">517 U.S. 690</a></span> (1996)</b></center>
<center><h1>ORNELAS et al.<br>
v.<br>
UNITED STATES</h1></center>
<center>No. 95-5257.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued March 26, 1996.</center>
<center>Decided May 28, 1996.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SEVENTH CIRCUIT
<p>Rehnquist, C. J., delivered the opinion of the Court, in which Stevens, O'Connor, Kennedy, Souter, Thomas, Ginsburg, and Breyer, JJ., joined. Scalia, J., filed a dissenting opinion, <i>post,</i> p. 700.</p>
<p><span class="star-pagination">*692</span> <i>Robert G. LeBell</i> argued the cause for petitioners. With him on the briefs was <i>Brian W. Gleason.</i> </p>
<p><i>Cornelia T. L. Pillard</i> argued the cause for the United States. With her on the brief were <i>Solicitor General Days, Acting Assistant Attorney General Keeney, Deputy Solicitor General Dreeben,</i> and <i>Joel M. Gershowitz.</i> </p>
<p><i>Peter D. Isakoff,</i> by invitation of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./516/1008/">516 U. S. 1008</a></span>, argued the cause and filed a brief as <i>amicus curiae</i> in support of the judgment below.<sup>[*]</sup></p>
<p>Chief Justice Rehnquist delivered the opinion of the Court.</p>
<p>Petitioners each pleaded guilty to possession of cocaine with intent to distribute. They reserved their right to appeal the District Court's denial of their motion to suppress the cocaine found in their car. The District Court had found reasonable suspicion to stop and question petitioners as they entered their car, and probable cause to remove one of the interior panels where a package containing two kilograms of cocaine was found. The Court of Appeals opined that the findings of reasonable suspicion to stop, and probable cause to search, should be reviewed "deferentially," and "for clear error." We hold that the ultimate questions of reasonable suspicion and probable cause to make a warrantless search should be reviewed <i>de novo.</i> </p>
<p>The facts are not disputed. In the early morning of a December day in 1992, Detective Michael Pautz, a 20-year veteran of the Milwaukee County Sheriff's Department with 2 years specializing in drug enforcement, was conducting drug-interdiction surveillance in downtown Milwaukee. <span class="star-pagination">*692</span> Pautz noticed a 1981 two-door Oldsmobile with California license plates in a motel parking lot. The car attracted Pautz's attention for two reasons: because older model, twodoor General Motors cars are a favorite with drug couriers because it is easy to hide things in them; and because California is a "source State" for drugs. Detective Pautz radioed his dispatcher to inquire about the car's registration. The dispatcher informed Pautz that the owner was either Miguel Ledesma Ornelas or Miguel Ornelas Ledesma from San Jose, California; Pautz was unsure which name the dispatcher gave. Detective Pautz checked the motel registry and learned that an Ismael Ornelas accompanied by a second man had registered at 4 a.m., without reservations.</p>
<p>Pautz called for his partner, Donald Hurrle, a detective with approximately 25 years of law enforcement experience, assigned for the past 6 years to the drug enforcement unit. When Hurrle arrived at the scene, the officers contacted the local office of the Drug Enforcement Administration (DEA) and asked DEA personnel to run the names Miguel Ledesma Ornelas and Ismael Ornelas through the Narcotics and Dangerous Drugs Information System (NADDIS), a federal database of known and suspected drug traffickers. Both names appeared in NADDIS. The NADDIS report identified Miguel Ledesma Ornelas as a heroin dealer from El Centro, California, and Ismael Ornelas, Jr., as a cocaine dealer from Tucson, Arizona. The officers then summoned Deputy Luedke and the department's drug-sniffing dog, Merlin. Upon their arrival, Detective Pautz left for another assignment. Detective Hurrle informed Luedke of what they knew and together they waited.</p>
<p>Sometime later, petitioners emerged from the motel and got into the Oldsmobile. Detective Hurrle approached the car, identified himself as a police officer, and inquired whether they had any illegal drugs or contraband. Petitioners answered "No." Hurrle then asked for identification and was given two California driver's licenses bearing the names <span class="star-pagination">*693</span> Saul Ornelas and Ismael Ornelas. Hurrle asked them if he could search the car and petitioners consented. The men appeared calm, but Ismael was shaking somewhat. Deputy Luedke, who over the past nine years had searched approximately 2,000 cars for narcotics, searched the Oldsmobile's interior. He noticed that a panel above the right rear passenger armrest felt somewhat loose and suspected that the panel might have been removed and contraband hidden inside. Luedke would testify later that a screw in the doorjam adjacent to the loose panel was rusty, which to him meant that the screw had been removed at some time. Luedke dismantled the panel and discovered two kilograms of cocaine. Petitioners were arrested.</p>
<p>Petitioners filed pretrial motions to suppress, alleging that the police officers violated their Fourth Amendment rights when the officers detained them in the parking lot and when Deputy Luedke searched inside the panel without a warrant.<sup>[1]</sup> The Government conceded in the court below that when the officers approached petitioners in the parking lot, a reasonable person would not have felt free to leave, so the encounter was an investigatory stop. See <span class="citation" data-id="663109"><a href="/opinion/663109/united-states-v-ismael-ornelas-ledesma-and-saul-ornelas/#716" aria-description="Citation for case: United States v. Ismael Ornelas-Ledesma and Saul Ornelas">16 F. 3d 714, 716</a></span> (CA7 1994). An investigatory stop is permissible under the Fourth Amendment if supported by reasonable suspicion, <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), and a warrantless search of a car is valid if based on probable cause, <i>California</i> v. <i>Acevedo,</i> <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/#569" aria-description="Citation for case: California v. Acevedo">500 U. S. 565, 569-570</a></span> (1991).</p>
<p><span class="star-pagination">*694</span> After conducting an evidentiary hearing, the Magistrate Judge concluded that the circumstances gave the officers reasonable suspicion, but not probable cause. The Magistrate found, as a finding of fact, that there was no rust on the screw and hence concluded that Deputy Luedke had an insufficient basis to conclude that drugs would be found within the panel. The Magistrate nonetheless recommended that the District Court deny the suppression motions because he thought, given the presence of the drug-sniffing dog, that the officers would have found the cocaine by lawful means eventually and therefore the drugs were admissible under the inevitable discovery doctrine. See <i>Nix</i> v. <i>Williams,</i> <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">467 U. S. 431</a></span> (1984).</p>
<p>The District Court adopted the Magistrate's recommendation with respect to reasonable suspicion, but not its reasoning as to probable cause. The District Court thought that the model, age, and source-State origin of the car, and the fact that two men traveling together checked into a motel at 4 o'clock in the morning without reservations, formed a drug-courier profile and that this profile together with the NADDIS reports gave rise to reasonable suspicion of drugtrafficking activity; in the court's view, reasonable suspicion became probable cause when Deputy Luedke found the loose panel. Accordingly, the court ruled that the cocaine need not be excluded.<sup>[2]</sup></p>
<p>The Court of Appeals reviewed deferentially the District Court's determinations of reasonable suspicion and probable cause; it would reverse only upon a finding of "clear error."<sup>[3]</sup><span class="star-pagination">*695</span> <span class="citation" data-id="663109"><a href="/opinion/663109/united-states-v-ismael-ornelas-ledesma-and-saul-ornelas/#719" aria-description="Citation for case: United States v. Ismael Ornelas-Ledesma and Saul Ornelas">16 F. 3d, at 719</a></span>. The court found no clear error in the reasonable-suspicion analysis and affirmed that determination. <i><span class="citation" data-id="663109"><a href="/opinion/663109/united-states-v-ismael-ornelas-ledesma-and-saul-ornelas/" aria-description="Citation for case: United States v. Ismael Ornelas-Ledesma and Saul Ornelas">Ibid.</a></span></i> With respect to the probable-cause finding, however, the court remanded the case for a determination on whether Luedke was credible when testifying about the loose panel. <span class="citation" data-id="663109"><a href="/opinion/663109/united-states-v-ismael-ornelas-ledesma-and-saul-ornelas/#721" aria-description="Citation for case: United States v. Ismael Ornelas-Ledesma and Saul Ornelas"><i>Id.,</i> at 721-722</a></span>.</p>
<p>On remand, the Magistrate Judge expressly found the testimony credible. The District Court accepted the finding, and once again ruled that probable cause supported the search. The Seventh Circuit held that determination not clearly erroneous. Judgt. order reported at <span class="citation multiple-matches"><a href="/c/F.%203d/52/328/">52 F. 3d 328</a></span> (1995).</p>
<p>We granted certiorari to resolve the conflict among the Circuits over the applicable standard of appellate review. <span class="citation multiple-matches"><a href="/c/U.%20S./516/963/">516 U. S. 963</a></span> (1996).<sup>[4]</sup></p>
<p>Articulating precisely what "reasonable suspicion" and "probable cause" mean is not possible. They are commonsense, nontechnical conceptions that deal with "`the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act.' " <i>Illinois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#231" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 231</a></span> (1983) (quoting <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175</a></span> (1949)); see <i>United States</i> v. <i>Sokolow,</i> <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#7" aria-description="Citation for case: United States v. Sokolow">490 U. S. 1, 7-8</a></span> (1989). As such, the standards are "not readily, or even usefully, reduced to a neat set of legal <span class="star-pagination">*696</span> rules." <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#232" aria-description="Citation for case: Illinois v. Gates"><i>Gates, supra,</i> at 232</a></span>. We have described reasonable suspicion simply as "a particularized and objective basis" for suspecting the person stopped of criminal activity, <i>United States</i> v. <i>Cortez,</i> <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 417-418</a></span> (1981), and probable cause to search as existing where the known facts and circumstances are sufficient to warrant a man of reasonable prudence in the belief that contraband or evidence of a crime will be found, see <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States"><i>Brinegar, supra,</i> at 175-176</a></span>; <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#238" aria-description="Citation for case: Illinois v. Gates"><i>Gates, supra,</i> at 238</a></span>. We have cautioned that these two legal principles are not "finely-tuned standards," comparable to the standards of proof beyond a reasonable doubt or of proof by a preponderance of the evidence. <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#235" aria-description="Citation for case: Illinois v. Gates"><i>Gates, supra,</i> at 235</a></span>. They are instead fluid concepts that take their substantive content from the particular contexts in which the standards are being assessed. <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#232" aria-description="Citation for case: Illinois v. Gates"><i>Gates, supra,</i> at 232</a></span>; <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States"><i>Brinegar, supra,</i>  at 175</a></span> ("The standard of proof [for probable cause] is . . . correlative to what must be proved"); <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#33" aria-description="Citation for case: Ker v. California">374 U. S. 23, 33</a></span> (1963) ("This Cour[t] [has a] long-established recognition that standards of reasonableness under the Fourth Amendment are not susceptible of Procrustean application"; "[e]ach case is to be decided on its own facts and circumstances" (internal quotation marks omitted)); <i>Terry</i> v. <i>Ohio,</i>  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 29</a></span> (the limitations imposed by the Fourth Amendment "will have to be developed in the concrete factual circumstances of individual cases").</p>
<p>The principal components of a determination of reasonable suspicion or probable cause will be the events which occurred leading up to the stop or search, and then the decision whether these historical facts, viewed from the standpoint of an objectively reasonable police officer, amount to reasonable suspicion or to probable cause. The first part of the analysis involves only a determination of historical facts, but the second is a mixed question of law and fact: "[T]he historical facts are admitted or established, the rule of law is undisputed, and the issue is whether the facts satisfy the [relevant] statutory [or constitutional] standard, or to put it another <span class="star-pagination">*697</span> way, whether the rule of law as applied to the established facts is or is not violated." <i>Pullman-Standard</i> v. <i>Swint,</i> <span class="citation" data-id="9428745"><a href="/opinion/110698/pullman-standard-v-swint/#289" aria-description="Citation for case: Pullman-Standard v. Swint">456 U. S. 273, 289, n. 19</a></span> (1982).</p>
<p>We think independent appellate review of these ultimate determinations of reasonable suspicion and probable cause is consistent with the position we have taken in past cases. We have never, when reviewing a probable-cause or reasonable-suspicion determination ourselves, expressly deferred to the trial court's determination. See, <i>e. g., </i><i><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar, supra</a></span></i> (rejecting District Court's conclusion that the police lacked probable cause); <i>Alabama</i> v. <i>White,</i> <span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/" aria-description="Citation for case: Alabama v. White">496 U. S. 325</a></span> (1990) (conducting independent review and finding reasonable suspicion). A policy of sweeping deference would permit, "[i]n the absence of any significant difference in the facts," "the Fourth Amendment's incidence [to] tur[n] on whether different trial judges draw general conclusions that the facts are sufficient or insufficient to constitute probable cause." <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#171" aria-description="Citation for case: Brinegar v. United States"><i>Brinegar, supra,</i> at 171</a></span>. Such varied results would be inconsistent with the idea of a unitary system of law. This, if a matter-of-course, would be unacceptable.</p>
<p>In addition, the legal rules for probable cause and reasonable suspicion acquire content only through application. Independent review is therefore necessary if appellate courts are to maintain control of, and to clarify, the legal principles. See <i>Miller</i> v. <i>Fenton,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#114" aria-description="Citation for case: Miller v. Fenton">474 U. S. 104, 114</a></span> (1985) (where the "relevant legal principle can be given meaning only through its application to the particular circumstances of a case, the Court has been reluctant to give the trier of fact's conclusions presumptive force and, in so doing, strip a federal appellate court of its primary function as an expositor of law").</p>
<p>Finally, <i>de novo</i> review tends to unify precedent and will come closer to providing law enforcement officers with a defined "`set of rules which, in most instances, makes it possible to reach a correct determination beforehand as to whether an invasion of privacy is justified in the interest of <span class="star-pagination">*698</span> law enforcement.' " <i>New York</i> v. <i>Belton,</i> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#458" aria-description="Citation for case: New York v. Belton">453 U. S. 454, 458</a></span> (1981); see also <i>Thompson</i> v. <i>Keohane,</i> <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/#115" aria-description="Citation for case: Thompson v. Keohane">516 U. S. 99, 115</a></span> (1995) ("[T]he law declaration aspect of independent review potentially may guide police, unify precedent, and stabilize the law," and those effects "serve legitimate law enforcement interests").</p>
<p>It is true that because the mosaic which is analyzed for a reasonable-suspicion or probable-cause inquiry is multifaceted, "one determination will seldom be a useful `precedent' for another," <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#238" aria-description="Citation for case: Illinois v. Gates"><i>Gates, supra,</i> at 238, n. 11</a></span>. But there are exceptions. For instance, the circumstances in <i>Brinegar</i> , <i>supra,</i> and <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), were so alike that we concluded that reversing the Court of Appeals' decision in <i><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span></i> was necessary to be faithful to <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>. </i><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#178" aria-description="Citation for case: Brinegar v. United States"><i>Brinegar, supra,</i> at 178</a></span> ("Nor . . . can we find in the present facts any substantial basis for distinguishing this case from the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case"). We likewise recognized the similarity of facts in <i>United States</i> v. <i><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">Sokolow, supra</a></span></i><i>,</i> and <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U. S. 491</a></span> (1983) (in both cases, the defendant traveled under an assumed name; paid for an airline ticket in cash with a number of small bills; traveled from Miami, a source city for illicit drugs; and appeared nervous in the airport). The same was true both in <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982), and <i>California</i> v. <i>Acevedo,</i> <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/" aria-description="Citation for case: California v. Acevedo">500 U. S. 565</a></span> (1991), see <i><span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/" aria-description="Citation for case: California v. Acevedo">id.</a></span></i> , at 572 ("The facts in this case closely resemble the facts in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> "); and in <i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544</a></span> (1980), and <i>Reid</i> v. <i>Georgia,</i> <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">448 U. S. 438</a></span> (1980), see <i><span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">id.</a></span></i> , at 443 (Powell, J., concurring) ("facts [in <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span></i> ] [are] remarkably similar to those in the present case"). And even where one case may not squarely control another one, the two decisions when viewed together may usefully add to the body of law on the subject.</p>
<p>The Court of Appeals, in adopting its deferential standard of review here, reasoned that <i>de novo</i> review for warrantless searches would be inconsistent with the "`great deference' " paid when reviewing a decision to issue a warrant, see <i>Illi-</i>  <span class="star-pagination">*699</span> <i>nois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213</a></span> (1983). See <i>United States</i> v. <i>Spears,</i> <span class="citation" data-id="9482988"><a href="/opinion/583951/united-states-v-charles-j-spears-also-known-as-blackie-and-donald/#269" aria-description="Citation for case: United States v. Charles J. Spears, Also Known as...">965 F. 2d 262, 269-271</a></span> (CA7 1992). We cannot agree. The Fourth Amendment demonstrates a "strong preference for searches conducted pursuant to a warrant," <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#236" aria-description="Citation for case: Illinois v. Gates"><i>Gates, supra,</i>  at 236</a></span>, and the police are more likely to use the warrant process if the scrutiny applied to a magistrate's probablecause determination to issue a warrant is less than that for warrantless searches. Were we to eliminate this distinction, we would eliminate the incentive.</p>
<p>We therefore hold that as a general matter determinations of reasonable suspicion and probable cause should be reviewed <i>de novo</i> on appeal. Having said this, we hasten to point out that a reviewing court should take care both to review findings of historical fact only for clear error and to give due weight to inferences drawn from those facts by resident judges and local law enforcement officers.</p>
<p>A trial judge views the facts of a particular case in light of the distinctive features and events of the community; likewise, a police officer views the facts through the lens of his police experience and expertise. The background facts provide a context for the historical facts, and when seen together yield inferences that deserve deference. For example, what may not amount to reasonable suspicion at a motel located alongside a transcontinental highway at the height of the summer tourist season may rise to that level in December in Milwaukee. That city is unlikely to have been an overnight stop selected at the last minute by a traveler coming from California to points east. The 85-mile width of Lake Michigan blocks any further eastward progress. And while the city's salubrious summer climate and seasonal attractions bring many tourists at that time of year, the same is not true in December. Milwaukee's average daily high temperature in that month is 31 degrees and its average daily low is 17 degrees; the percentage of possible sunshine is only 38 percent. It is a reasonable inference that a Californian stopping in Milwaukee in December is either there <span class="star-pagination">*700</span> to transact business or to visit family or friends. The background facts, though rarely the subject of explicit findings, inform the judge's assessment of the historical facts.</p>
<p>In a similar vein, our cases have recognized that a police officer may draw inferences based on his own experience in deciding whether probable cause exists. See, <i>e. g., </i><i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#897" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891, 897</a></span> (1975). To a layman the sort of loose panel below the back seat armrest in the automobile involved in this case may suggest only wear and tear, but to Officer Luedke, who had searched roughly 2,000 cars for narcotics, it suggested that drugs may be secreted inside the panel. An appeals court should give due weight to a trial court's finding that the officer was credible and the inference was reasonable.</p>
<p>We vacate the judgments and remand the case to the Court of Appeals to review <i>de novo</i> the District Court's determinations that the officer had reasonable suspicion and probable cause in this case.</p>
<p><i>It is so ordered.</i> </p>
<p>Justice Scalia, dissenting.</p>
<p>The Court today decides that a district court's determinations whether there was probable cause to justify a warrantless search and reasonable suspicion to make an investigatory stop should be reviewed <i>de novo.</i> We have in the past reviewed some mixed questions of law and fact on a <i>de novo</i>  basis, and others on a deferential basis, depending upon essentially practical considerations. Because, with respect to the questions at issue here, the purpose of the determination and its extremely fact-bound nature will cause <i>de novo</i> review to have relatively little benefit, it is in my view unwise to require courts of appeals to undertake the searching inquiry that standard requires. I would affirm the judgment of the Court of Appeals.</p>
<p>As the Court recognizes, determinations of probable cause and reasonable suspicion involve a two-step process. First, <span class="star-pagination">*701</span> a court must identify all of the relevant historical facts known to the officer at the time of the stop or search; and second, it must decide whether, under a standard of objective reasonableness, those facts would give rise to a reasonable suspicion justifying a stop or probable cause to search. See <i>ante,</i> at 696-697. Because this second step requires application of an objective legal standard to the facts, it is properly characterized as a mixed question of law and fact. See <i>ibid.; </i><i>Pullman-Standard</i> v. <i>Swint,</i> <span class="citation" data-id="9428745"><a href="/opinion/110698/pullman-standard-v-swint/#289" aria-description="Citation for case: Pullman-Standard v. Swint">456 U. S. 273, 289, n. 19</a></span> (1982).</p>
<p>Merely labeling the issues "mixed questions," however, does not establish that they receive <i>de novo</i> review. While it is well settled that appellate courts "accep[t] findings of fact that are not `clearly erroneous' but decid[e] questions of law <i>de novo,</i> " <i>First Options of Chicago, Inc.</i> v. <i>Kaplan,</i> <span class="citation" data-id="117937"><a href="/opinion/117937/first-options-of-chicago-inc-v-kaplan/#948" aria-description="Citation for case: First Options of Chicago, Inc. v. Kaplan">514 U. S. 938, 948</a></span> (1995), there is no rigid rule with respect to mixed questions. We have said that "deferential review of mixed questions of law and fact is warranted when it appears that the district court is `better positioned' than the appellate court to decide the issue in question or that probing appellate scrutiny will not contribute to the clarity of legal doctrine." <i>Salve Regina College</i> v. <i>Russell,</i> <span class="citation" data-id="9432235"><a href="/opinion/112564/salve-regina-college-v-russell/#233" aria-description="Citation for case: Salve Regina College v. Russell">499 U. S. 225, 233</a></span> (1991) (citing <i>Miller</i> v. <i>Fenton,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#114" aria-description="Citation for case: Miller v. Fenton">474 U. S. 104, 114</a></span> (1985)).</p>
<p>These primary factors that counsel in favor of deferential review of some mixed questions of law and factexpertise of the district court and lack of law-clarifying value in the appellate decisionare ordinarily present with respect to determinations of reasonable suspicion and probable cause. The factual details bearing upon those determinations are often numerous and (even when supported by uncontroverted police testimony) subject to credibility determinations. An appellate court never has the benefit of the district court's intimate familiarity with the details of the casenor the full benefit of its hearing of the live testimony, unless the district court makes specific findings on the "totality of the circumstances" bearing upon the stop or search. <span class="star-pagination">*702</span> As we recognized in <i>Cooter &amp; Gell</i> v. <i>Hartmarx Corp.,</i> <span class="citation" data-id="9432057"><a href="/opinion/112457/cooter-gell-v-hartmarx-corp/" aria-description="Citation for case: Cooter &amp; Gell v. Hartmarx Corp.">496 U. S. 384</a></span> (1990), a case holding that deferential (abuseof-discretion) review should be applied to a district court's Federal Rule of Civil Procedure 11 determination that an attorney did not conduct a reasonable inquiry or entertain a "substantiated belief" regarding the nonfrivolousness of the complaint, see <i><span class="citation" data-id="9432057"><a href="/opinion/112457/cooter-gell-v-hartmarx-corp/" aria-description="Citation for case: Cooter &amp; Gell v. Hartmarx Corp.">id.,</a></span></i> at 393: A district court, "[f]amiliar with the issues and litigants . . . is better situated than the court of appeals to marshal the pertinent facts and apply the factdependent legal standard . . . ." <span class="citation" data-id="9432057"><a href="/opinion/112457/cooter-gell-v-hartmarx-corp/#402" aria-description="Citation for case: Cooter &amp; Gell v. Hartmarx Corp."><i>Id.,</i> at 402</a></span>.</p>
<p>Moreover, as the Court acknowledges, "reasonable suspicion" and "probable cause" are "commonsense, nontechnical conceptions that deal with ` "the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act."` " <i>Ante,</i> at 695 (quoting <i>Illinois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#231" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 231</a></span> (1983) (quoting <i>Brinegar</i>  v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175</a></span> (1949))). Where a trial court makes such commonsense determinations based on the totality of circumstances, it is ordinarily accorded deference. What we said in a case concerning the question whether certain payments were a "gift" excludable from income under the Internal Revenue Code is equally pertinent here.</p>
<blockquote>"Decision of the issue presented in these cases must be based ultimately on the application of the fact-finding tribunal's experience with the mainsprings of human conduct to the totality of the facts of each case. The nontechnical nature of the . . . standard, the close relationship of it to the data of practical human experience, and the multiplicity of relevant factual elements, with their various combinations, creating the necessity of ascribing the proper force to each, confirm us in our conclusion that primary weight in this area must be given to the conclusions of the trier of fact." <i>Commissioner</i>  v. <i>Duberstein,</i> <span class="citation" data-id="9422005"><a href="/opinion/106071/commissioner-v-duberstein/#289" aria-description="Citation for case: Commissioner v. Duberstein">363 U. S. 278, 289</a></span> (1960).</blockquote>
<p><span class="star-pagination">*703</span> With respect to the second factor counseling in favor of deferential review, level of law-clarifying value in the appellate decision: Law clarification requires generalization, and some issues lend themselves to generalization much more than others. Thus, in <i>Pierce</i> v. <i>Underwood,</i> <span class="citation" data-id="9431437"><a href="/opinion/112137/pierce-v-underwood/#562" aria-description="Citation for case: Pierce v. Underwood">487 U. S. 552, 562</a></span> (1988), a principal basis for our applying an abuse-ofdiscretion standard to a district court's determination that the United States' litigating position was "substantially justified" within the meaning of the Equal Access to Justice Act, <span class="citation no-link">28 U. S. C. § 2412</span>(d), was that the question was "a multifarious and novel question, little susceptible, for the time being at least, of useful generalization." <span class="citation" data-id="9431437"><a href="/opinion/112137/pierce-v-underwood/#562" aria-description="Citation for case: Pierce v. Underwood">487 U. S., at 562</a></span>. Probable-cause and reasonable-suspicion determinations are similarly resistant to generalization. As the Court recognizes, these are "fluid concepts," "`not readily, or even usefully, reduced to a neat set of legal rules' "; and "because the mosaic which is analyzed for a reasonable-suspicion or probable-cause inquiry is multifaceted, `one determination will seldom be a useful "precedent" for another.' " <i>Ante,</i> at 695-696, 698 (quoting <i>Illinois</i> v. <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#232" aria-description="Citation for case: Illinois v. Gates"><i>Gates, supra,</i> at 232, 238, n. 11</a></span>). The Court maintains that there will be exceptions to thisthat fact patterns will occasionally repeat themselves, so that a prior <i>de novo</i> appellate decision will provide useful guidance in a similar case. <i>Ante,</i> at 698. I do not dispute that, but I do not understand why we should allow the exception to frame the rule. Here, as in <i>Anderson</i> v. <i>Bessemer City,</i> <span class="citation" data-id="9429949"><a href="/opinion/111373/anderson-v-city-of-bessemer-city/#574" aria-description="Citation for case: Anderson v. City of Bessemer City">470 U. S. 564, 574-575</a></span> (1985), "[d]uplication of the trial judge's efforts in the court of appeals would very likely contribute only negligibly to the accuracy of fact determination at a huge cost in diversion of judicial resources."</p>
<p>The facts of this very case illustrate the futility of attempting to craft useful precedent from the fact-intensive review demanded by determinations of probable cause and reasonable suspicion. On remand, in conducting <i>de novo</i> review, the Seventh Circuit might consider, <i>inter alia,</i> the following <span class="star-pagination">*704</span> factors relevant to its determination whether there was probable cause to conduct a warrantless search and reasonable suspicion justifying the investigatory stop: (i) the two NADDIS tips; (ii) that the car was a 1981 two-door General Motors product; (iii) that the car was from California, a source State; (iv) that the car was in Milwaukee; (v) that it was December; (vi) that one suspect checked into the hotel at 4 a.m.; (vii) that he did not have reservations; (viii) that he had one traveling companion; (ix) that one suspect appeared calm but shaking; and (x) that there was a loose panel in the car door. If the Seventh Circuit were to find that this unique confluence of factors supported probable cause and reasonable suspicion, the absence of any one of these factors in the next case would render the precedent inapplicable.</p>
<p>Of course, even when all of the factors <i>are</i> replicated, use of a <i>de novo</i> standard as opposed to a deferential standard will provide greater clarity only where the latter would not suffice to set the trial court's conclusion aside. For where the appellate court holds, on the basis of deferential review, that it <i>was</i> reversible error for a district court to find probable cause or reasonable suspicion in light of certain facts, it advances the clarity of the law just as much as if it had reversed the district court after conducting plenary review.</p>
<p>In the present case, an additional factor counseling against <i>de novo</i> review must be mentioned: The prime benefit of <i>de novo</i> appellate review in criminal cases is, of course, to prevent a miscarriage of justice that might result from permitting the verdict of guilty to rest upon the legal determinations of a single judge. But the issue in these probablecause and reasonable-suspicion cases is not innocence but deterrence of unlawful police conduct. That deterrence will not be <i>at all</i> lessened if the trial judge's determination, right or wrong, is subjected to only deferential review.</p>
<p>The Court is wrong in its assertion, <i>ante,</i> at 698-699, that unless there is a dual standard of reviewdeferential review of a magistrate's decision to issue a warrant, and <i>de novo</i>  <span class="star-pagination">*705</span> review of a district court's <i>ex post facto</i> approval of a warrantless searchthe incentive to obtain a warrant would be eliminated. In <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#913" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 913</a></span> (1984), we held that "reliable physical evidence seized by officers reasonably relying on a warrant issued by a detached and neutral magistrate . . . should be admissible in the prosecutor's case in chief." Only a warrant can provide this assurance that the fruits of even a technically improper search will be admissible. Law enforcement officers would still have ample incentive to proceed by warrant.</p>
<p>Finally, I must observe that the Court does not appear to have the courage of its conclusions. In an apparent effort to reduce the unproductive burden today's decision imposes upon appellate courts, or perhaps to salvage some of the trial court's superior familiarity with the facts that it has cast aside, the Court suggests that an appellate court should give "due weight" to a trial court's finding that an officer's inference of wrongdoing (<i>i. e.,</i> his assessment of probable cause to search) was reasonable. <i>Ante,</i> at 700. The Court cannot have it both ways. This finding of "reasonableness" is precisely what it has told us the appellate court must review <i>de novo;</i> and in <i>de novo</i> review, the "weight due" to a trial court's finding is zero. In the last analysis, therefore, the Court's opinion seems to me not only wrong but contradictory.</p>
<p></p>
<h2>* * *</h2>
<p>I would affirm the judgment of the Seventh Circuit on the ground that it correctly applied a deferential standard of review to the District Court's findings of probable cause and reasonable suspicion.</p>
<h2>NOTES</h2>
<p>[*]   <i>Tracey Maclin, Steven R. Shapiro,</i> and <i>Barbara E. Bergman</i> filed a brief for the American Civil Liberties Union et al.as <i>amici curiae</i>  urging reversal.
</p>
<p><i>Fred E. Inbau, Wayne W. Schmidt, James P. Manak,</i> and <i>Bernard J. Farber</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging affirmance.</p>
<p>[1]  Petitioners also alleged that they had not given their consent to search the interior of the car. The Magistrate Judge rejected this claim, finding that the record "clearly establishe[d] consent to search the Oldsmobile" and that "neither [petitioner] placed any restrictions on the areas the officers could search." App. 21. The Magistrate ruled that this consent did not give the officers authority to search inside the panel, however, because under Seventh Circuit precedent the police may not dismantle the car body during an otherwise valid search unless the police have probable cause to believe the car's panels contain narcotics. See <i>United States</i> v. <i>Garcia,</i>  <span class="citation" data-id="537758"><a href="/opinion/537758/united-states-v-carlos-garcia-and-jose-luis-garcia/#1419" aria-description="Citation for case: United States v. Carlos Garcia and Jose Luis Garcia">897 F. 2d 1413, 1419-1420</a></span> (1990). We assume correct the Circuit's limitation on the scope of consent only for purposes of this decision.</p>
<p>[2]  The District Court emphasized twice that it did not reject the Magistrate's recommendation with respect to the inevitable discovery doctrine. App. 30-31, and n. 2; <i>id.,</i> at 43-44. But on appeal the Government did not defend the seizure on this alternative ground and the Seventh Circuit considered the argument waived. <i>Id.,</i> at 71-72.</p>
<p>[3]  While the Seventh Circuit uses the term "clear error" to denote the deferential standard applied when reviewing determinations of reasonable suspicion or probable cause, we think the preferable term is "abuse of discretion." See <i>Pierce</i> v. <i>Underwood,</i> <span class="citation" data-id="9431437"><a href="/opinion/112137/pierce-v-underwood/#558" aria-description="Citation for case: Pierce v. Underwood">487 U. S. 552, 558</a></span> (1988). "Clear error" is aterm of art derived from Rule 52(a) of the Federal Rules of Civil Procedure, and applies when reviewing questions of fact.</p>
<p>[4]  Compare, <i>e. g., </i><i>United States</i> v. <i>Puerta,</i> <span class="citation" data-id="597487"><a href="/opinion/597487/united-states-v-antonio-medina-puerta/#1300" aria-description="Citation for case: United States v. Antonio Medina Puerta">982 F. 2d 1297, 1300</a></span> (CA9 1992) (<i>de novo</i> review); <i>United States</i> v. <i>Ramos,</i> <span class="citation" data-id="561395"><a href="/opinion/561395/united-states-v-armando-balbino-ramos-evaristo-ramos/#972" aria-description="Citation for case: United States v. Armando Balbino Ramos, Evaristo Ramos">933 F. 2d 968, 972</a></span> (CA11 1991) (same), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./503/908/">503 U. S. 908</a></span> (1992); <i>United States</i> v. <i>Patrick,</i>  <span class="citation" data-id="9480132"><a href="/opinion/538805/united-states-v-christopher-patrick-linda-taylor-and-christopher-patrick/#171" aria-description="Citation for case: United States v. Christopher Patrick, Linda Taylor and...">899 F. 2d 169, 171</a></span> (CA2 1990) (same), with <i>United States</i> v. <i>Spears,</i> <span class="citation" data-id="9482988"><a href="/opinion/583951/united-states-v-charles-j-spears-also-known-as-blackie-and-donald/#268" aria-description="Citation for case: United States v. Charles J. Spears, Also Known as...">965 F. 2d 262, 268-271</a></span> (CA7 1992) (clear error).
</p>
<p>The United States, in accord with petitioners, contends that a <i>de novo</i>  standard of review should apply to determinations of probable cause and reasonable suspicion. We therefore invited Peter D. Isakoff to brief and argue this case as <i>amicus curiae</i> in support of the judgment below. <span class="citation multiple-matches"><a href="/c/U.%20S./516/1008/">516 U. S. 1008</a></span> (1996). Mr. Isakoff accepted the appointment and has well fulfilled his assigned responsibility.</p>

</div>
```

---

## GROUP: content/cases/Orozco v. Texas.md  (`case`, 5 assertions)

### content_page

```
---
title: "Orozco v. Texas"
type: case
citation: "394 U.S. 324 (1969)"
parallel_cite: "89 S. Ct. 1095; 22 L. Ed. 2d 311"
neutral_cite: 1969 U.S. LEXIS 2154
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1969
date_decided: 1969-03-25
docket: 641
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1969-03-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Orozco v. Texas
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107883/orozco-v-texas/"
  cluster_id: 107883
  opinion_id: 107883
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[Berkemer v. McCarty]]", "[[Howes v. Fields]]", "[[Rhode Island v. Innis]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "custody", "custodial-interrogation"]
holding: "Miranda warnings were required where four officers questioned a suspect under arrest in his own bedroom in the early morning; custody…"
lake:
  record_id: Orozco v. Texas
  status: verified
  projected_at: 2026-07-06
---

# Orozco v. Texas

*394 U.S. 324 (1969)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
At about 4 a.m., four police officers entered Orozco's boardinghouse bedroom while he slept and questioned him about a fatal shooting. From the moment he gave his name, an officer testified, Orozco "was not free to go where he pleased but was 'under arrest.'" Without any [[Miranda and Custodial Interrogation|Miranda warnings]], the officers questioned him; he admitted owning a pistol and said it was in a washing machine, where it was found and matched by ballistics to the fatal shot.

## Issue
Whether [[Miranda and Custodial Interrogation|Miranda warnings]] were required before custodial questioning that occurred in the suspect's own bedroom rather than at a police station.

## Rule
Yes. "We disagree and hold that the use of these admissions obtained in the absence of the required warnings was a flat violation of the Self-Incrimination Clause of the Fifth Amendment as construed in *Miranda*." — 394 U.S. at 326. ^pin-326

Miranda's warnings are required wherever a person is interrogated while "in custody at the station *or otherwise deprived of his freedom of action in any significant way*." — 394 U.S. at 327 (quoting *Miranda v. Arizona*, 384 U.S. at 477). ^pin-327

## Application
According to the officers' own testimony, Orozco "was under arrest and not free to leave when he was questioned in his bedroom in the early hours of the morning." Because he was therefore in custody, the warnings were required despite the familiar surroundings of his own home; their omission made the use of his statements about the pistol a violation of the Fifth Amendment.

## Conclusion
The unwarned, in-custody bedroom questioning violated the Self-Incrimination Clause; the judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Orozco* remains a leading illustration that Miranda custody is not confined to the station house.

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Orozco v. Texas*, 394 U.S. 324 (1969) — https://www.courtlistener.com/opinion/107883/orozco-v-texas/ — pinpoints: 326, 327.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2df90521eff1e803", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "394 U.S. 324 (1969)", "court": "U.S. Supreme Court", "neutral_cite": "1969 U.S. LEXIS 2154", "official_citation_present": true, "parallel_cite": "89 S. Ct. 1095; 22 L. Ed. 2d 311", "title": "Orozco v. Texas", "year": "1969"}}
{"assertion_id": "29ad8cdf4b9fc743", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Miranda warnings were required where four officers questioned a suspect under arrest in his own bedroom in the early morning; custody…", "title": "Orozco v. Texas"}}
{"assertion_id": "bf9948c4a7235aa6", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Progeny / Refinement", "title": "Orozco v. Texas"}}
{"assertion_id": "c475eda138ccc7d3", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Orozco v. Texas"}}
{"assertion_id": "e2e65faf848fd611", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1969-03-25", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Orozco v. Texas", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Orozco v. Texas", "varies_by_point": "false"}}
```

### lake record — Orozco v. Texas

```json
{
  "schema_version": "s2.v1",
  "record_id": "Orozco v. Texas",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Orozco v. Texas",
    "case_name_short": "Orozco",
    "case_name_full": "Orozco v. Texas",
    "input_case_name": "Orozco v. Texas",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1969-03-25",
    "year": 1969,
    "docket": "641",
    "cluster_id": 107883,
    "lead_opinion_id": 107883,
    "sibling_ids": [
      107883,
      9423964,
      9423965,
      9423966
    ],
    "absolute_url": "/opinion/107883/orozco-v-texas/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "394 U.S. 324",
      "volume": "394",
      "reporter": "U.S.",
      "page": "324",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "89 S. Ct. 1095",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "1095",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 311",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "311",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1969 U.S. LEXIS 2154",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "2154",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "394 U.S. 324",
        "volume": "394",
        "reporter": "U.S.",
        "page": "324",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 S. Ct. 1095",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "1095",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 311",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "311",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1969 U.S. LEXIS 2154",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "2154",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "394 U.S. 324",
    "official_selection": {
      "court_class": "scotus",
      "selected": "394 U.S. 324",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-326",
      "page": null,
      "quote": "Without any Miranda warnings, the officers questioned him; he admitted owning a pistol and said it was in a washing machine, where it was found and matched by ballistics to the fatal shot. ## Issue Whether Miranda warnings were required before custodial questioning that occurred in the suspect's own bedroom rather than at a police station. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-327",
      "page": null,
      "quote": "in custody at the station *or otherwise deprived of his freedom of action in any significant way*.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1969-03-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Orozco v. Texas",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Faux",
          "cluster_id": 7312636,
          "cite": [
            "94 F. Supp. 3d 258",
            "2015 U.S. Dist. LEXIS 37051",
            "2015 WL 1347041"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hughes",
          "cluster_id": 214334,
          "cite": [
            "640 F.3d 428",
            "2011 U.S. App. LEXIS 7338",
            "2011 WL 1332061"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Fiedler v. State",
          "cluster_id": 1533838,
          "cite": [
            "991 S.W.2d 70",
            "1998 WL 1058889"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald Wayne Davis",
          "cluster_id": 471603,
          "cite": [
            "792 F.2d 1299",
            "20 Fed. R. Serv. 762",
            "1986 U.S. App. LEXIS 24794"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jerry Rorex",
          "cluster_id": 437540,
          "cite": [
            "737 F.2d 753",
            "1984 U.S. App. LEXIS 21056"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Larson",
          "cluster_id": 2080732,
          "cite": [
            "346 N.W.2d 199",
            "1984 Minn. App. LEXIS 3051"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Greathouse",
          "cluster_id": 1669864,
          "cite": [
            "627 S.W.2d 592"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wilder v. State",
          "cluster_id": 2463525,
          "cite": [
            "583 S.W.2d 349",
            "1979 Tex. Crim. App. LEXIS 1817"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane1_negative"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Mathiason",
          "cluster_id": 109587,
          "cite": [
            "50 L. Ed. 2d 714",
            "97 S. Ct. 711",
            "429 U.S. 492",
            "1977 U.S. LEXIS 38"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coleman v. Alabama",
          "cluster_id": 108182,
          "cite": [
            "26 L. Ed. 2d 387",
            "90 S. Ct. 1999",
            "399 U.S. 1",
            "1970 U.S. LEXIS 17"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Tucker",
          "cluster_id": 109063,
          "cite": [
            "41 L. Ed. 2d 182",
            "94 S. Ct. 2357",
            "417 U.S. 433",
            "1974 U.S. LEXIS 71"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Boys Markets, Inc. v. Retail Clerks Union, Local 770",
          "cluster_id": 108154,
          "cite": [
            "26 L. Ed. 2d 199",
            "90 S. Ct. 1583",
            "398 U.S. 235",
            "1970 U.S. LEXIS 79",
            "74 L.R.R.M. (BNA) 2257"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beckwith v. United States",
          "cluster_id": 109430,
          "cite": [
            "48 L. Ed. 2d 1",
            "96 S. Ct. 1612",
            "425 U.S. 341",
            "1976 U.S. LEXIS 147",
            "37 A.F.T.R.2d (RIA) 1232"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Duckworth v. Eagan",
          "cluster_id": 112322,
          "cite": [
            "106 L. Ed. 2d 166",
            "109 S. Ct. 2875",
            "492 U.S. 195",
            "1989 U.S. LEXIS 3196",
            "57 U.S.L.W. 4942"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hopfer",
          "cluster_id": 3941316,
          "cite": [
            "679 N.E.2d 321",
            "112 Ohio App. 3d 521"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coleman v. Commonwealth",
          "cluster_id": 1227505,
          "cite": [
            "307 S.E.2d 864",
            "226 Va. 31",
            "1983 Va. LEXIS 266"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adams v. Illinois",
          "cluster_id": 108480,
          "cite": [
            "31 L. Ed. 2d 202",
            "92 S. Ct. 916",
            "405 U.S. 278",
            "1972 U.S. LEXIS 81"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Leonard David Griffin",
          "cluster_id": 553880,
          "cite": [
            "922 F.2d 1343",
            "1990 U.S. App. LEXIS 22396",
            "1990 WL 212298"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Fioravanti, Nicholas Panaccione, and Angelo Pepe, Nicholas Panaccione",
          "cluster_id": 285356,
          "cite": [
            "412 F.2d 407"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wicker v. State",
          "cluster_id": 1655134,
          "cite": [
            "740 S.W.2d 779",
            "1987 Tex. Crim. App. LEXIS 671",
            "1987 WL 1000"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cannon v. State",
          "cluster_id": 1564923,
          "cite": [
            "691 S.W.2d 664",
            "1985 Tex. Crim. App. LEXIS 1371"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107883 OR 9423964 OR 9423965 OR 9423966) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNjY0NTc2MDAwMDAmcz0xNDEyNzQ3JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107883+OR+9423964+OR+9423965+OR+9423966%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107883 OR 9423964 OR 9423965 OR 9423966)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzUmcz0xNDUzMjk4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107883+OR+9423964+OR+9423965+OR+9423966%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107883 OR 9423964 OR 9423965 OR 9423966)",
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
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107883 OR 9423964 OR 9423965 OR 9423966)",
    "indexed_citing_opinions": 447,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107883,
        "count": 424,
        "count_source": "search"
      },
      {
        "opinion_id": 9423964,
        "count": 34,
        "count_source": "search"
      },
      {
        "opinion_id": 9423965,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423966,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 661,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/orozco-v-texas.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQ4OTQ3MTYmcz03MzE4NjgxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107883+OR+9423964+OR+9423965+OR+9423966%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107883,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107883,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107883,
        "cited_id": 107676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107883,
        "cited_id": 1527140,
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
    "date_created": "2026-07-05T16:28:19Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:28:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:28:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:31:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:28:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Orozco v. Texas

```
<div>
<center><b><span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">394 U.S. 324</a></span> (1969)</b></center>
<center><h1>OROZCO<br>
v.<br>
TEXAS.</h1></center>
<center>No. 641.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 26, 1969.</center>
<center>Decided March 25, 1969.</center>
CERTIORARI TO THE COURT OF CRIMINAL APPEALS OF TEXAS.
<p><i>Charles W. Tessmer</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Lonny F. Zwiener,</i> Assistant Attorney General of Texas, argued the cause for respondent. With him on the brief were <i>Crawford C. Martin,</i> Attorney General, <i>Nola White,</i> First Assistant Attorney General, <i>Hawthorne Phillips,</i> Executive Assistant Attorney General, <i>Robert C. Flowers,</i> Assistant Attorney General, and <i>W. V. Geppert.</i></p>
<p>MR. JUSTICE BLACK delivered the opinion of the Court.</p>
<p>The petitioner, Reyes Arias Orozco, was convicted in the Criminal District Court of Dallas County, Texas, of murder without malice and was sentenced to serve in the state prison not less than two nor more than 10 years. The Court of Criminal Appeals of Texas affirmed the conviction, rejecting petitioner's contention that a material part of the evidence against him was obtained in violation of the provision of the Fifth Amendment to the United States Constitution, made applicable to the States by the Fourteenth Amendment, that: "No person <span class="star-pagination">*325</span>. . . shall be compelled in any criminal case to be a witness against himself."<sup>[1]</sup></p>
<p>The evidence introduced at trial showed that petitioner and the deceased had quarreled outside the El Farleto Cafe in Dallas shortly before midnight on the date of the shooting. The deceased had apparently spoken to petitioner's female companion inside the restaurant. In the heat of the quarrel outside, the deceased is said to have beaten petitioner about the face and called him "Mexican Grease." A shot was fired killing the deceased. Petitioner left the scene and returned to his boardinghouse to sleep. At about 4 a. m. four police officers arrived at petitioner's boardinghouse, were admitted by an unidentified woman, and were told that petitioner was asleep in the bedroom. All four officers entered the bedroom and began to question petitioner. From the moment he gave his name, according to the testimony of one of the officers, petitioner was not free to go where he pleased but was "under arrest." The officers asked him if he had been to the El Farleto restaurant that night and when he answered "yes" he was asked if he owned a pistol. Petitioner admitted owning one. After being asked a second time where the pistol was located, he admitted that it was in the washing machine in a backroom of the boardinghouse. Ballistics tests indicated that the gun found in the washing machine was the gun that fired the fatal shot. At petitioner's trial, held after the effective date<sup>[2]</sup> of this Court's decision in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), the trial court allowed one of the officers, <span class="star-pagination">*326</span> over the objection of petitioner's lawyer,<sup>[3]</sup> to relate the statements made by petitioner concerning the gun and petitioner's presence at the scene of the shooting. The trial testimony clearly shows that the officers questioned petitioner about incriminating facts without first informing him of his right to remain silent, his right to have the advice of a lawyer before making any statement, and his right to have a lawyer appointed to assist him if he could not afford to hire one. The Texas Court of Criminal Appeals held, with one judge dissenting, that the admission of testimony concerning the statements petitioner had made without the above warnings was not precluded by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> We disagree and hold that the use of these admissions obtained in the absence of the required warnings was a flat violation of the Self-Incrimination Clause of the Fifth Amendment as construed in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i></p>
<p>The State has argued here that since petitioner was interrogated on his own bed, in familiar surroundings, our <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> holding should not apply. It is true that the Court did say in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> that "compulsion to speak in the isolated setting of the police station may well be greater than in courts or other official investigations, where there are often impartial observers to guard against intimidation or trickery." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#461" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 461</a></span>. But the opinion iterated and reiterated the absolute necessity for officers interrogating people "in custody" to give the described warnings. See <i>Mathis</i> v. <i>United States,</i> 391 U. S. 1 <span class="star-pagination">*327</span> (1968). According to the officer's testimony, petitioner was under arrest and not free to leave when he was questioned in his bedroom in the early hours of the morning. The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion declared that the warnings were required when the person being interrogated was "in custody at the station <i>or otherwise deprived of his freedom of action in any significant way.</i>" <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#477" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 477</a></span>. (Emphasis supplied.) The decision of this Court in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was reached after careful consideration and lengthy opinions were announced by both the majority and dissenting Justices. There is no need to canvass those arguments again. We do not, as the dissent implies, expand or extend to the slightest extent our <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> decision. We do adhere to our well-considered holding in that case and therefore reverse<sup>[4]</sup> the conviction below.</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE FORTAS took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE HARLAN, concurring.</p>
<p>The passage of time has not made the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> case any more palatable to me than it was when the case was decided. See my dissenting opinion, and that of MR. JUSTICE WHITE, in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#504" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 504, 526</a></span> (1966).</p>
<p>Yet, despite my strong inclination to join in the dissent of my Brother WHITE, I can find no acceptable avenue of escape from <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in judging this case, especially in light of <i>Mathis</i> v. <i>United States,</i> <span class="citation" data-id="9423682"><a href="/opinion/107676/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">391 U. S. 1</a></span> (1968), which has already extended the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rules beyond the <span class="star-pagination">*328</span> police station, over the protest of JUSTICE STEWART, WHITE, and myself, <i>id.,</i> at 5-8. Therefore, and purely out of respect for <i>stare decisis,</i> I reluctantly feel compelled to acquiesce in today's decision of the Court, at the same time observing that the constitutional condemnation of this perfectly understandable, sensible, proper, and indeed commendable piece of police work highlights the unsoundness of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i></p>
<p>MR. JUSTICE WHITE, with whom MR. JUSTICE STEWART joins, dissenting.</p>
<p>This decision carries the rule of <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), to a new and unwarranted extreme. I continue to believe that the original rule amounted to a "constitutional straitjacket" on law enforcement which was justified neither by the words or history of the Constitution, nor by any reasonable view of the likely benefits of the rule as against its disadvantages. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#526" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 526</a></span>. Even accepting <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the Court extends the rule here and draws the straitjacket even tighter.</p>
<p>The opinion of the Court in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was devoted in large part to an elaborate discussion of the subtle forms of psychological pressure which could be brought to bear when an accused person is interrogated at length in unfamiliar surroundings. The "salient features" of the cases decided in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> were "incommunicado interrogation of individuals in a police-dominated atmosphere." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#445" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 445</a></span>. The danger was that in such circumstances the confidence of the prisoner could be eroded by techniques such as successive interrogations by police acting out friendly or unfriendly roles. These techniques are best developed in "isolation and unfamiliar surroundings," <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#450" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 450</a></span>. And they take time: "the major qualities an interrogator should possess are patience and perseverance." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> The techniques <span class="star-pagination">*329</span> of an extended period of isolation, repeated interrogation, cajolery, and trickery often enough produced admissions which were actually coerced in the traditional sense so that new safeguards were deemed essential.</p>
<p>It is difficult to believe that the requirements there laid down were essential to prevent compulsion in every conceivable case of station house interrogation. Where the defendant himself as a lawyer, policeman, professional criminal, or otherwise has become aware of what his right to silence is, it is sheer fancy to assert that his answer to every question asked him is compelled unless he is advised of those rights with which he is already intimately familiar. If there is any warrant to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> at all, it rests on the likelihood that in a sufficient number of cases exposure to station house practices will result in compelled confessions and that additional safeguards should be imposed in all cases to prevent possible erosion of Fifth Amendment values. Hence, the detailed ritual which <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> fashioned.</p>
<p>The Court now extends the same rules to all instances of in-custody questioning outside the station house. Once arrest occurs, the application of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is automatic. The rule is simple but it ignores the purpose of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to guard against what was thought to be the corrosive influence of practices which station house interrogation makes feasible. The Court wholly ignores the question whether similar hazards exist or even are possible when police arrest and interrogate on the spot, whether it be on the street corner or in the home, as in this case. No predicate is laid for believing that practices outside the station house are normally prolonged, carried out in isolation, or often productive of the physical or psychological coercion made so much of in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> It is difficult to imagine the police duplicating in a person's home or on the street those conditions and practices <span class="star-pagination">*330</span> which the Court found prevalent in the station house and which were thought so threatening to the right to silence. Without such a demonstration, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> hardly reaches this case or any cases similar to it.</p>
<p>Here, there was no prolonged interrogation, no unfamiliar surroundings, no opportunity for the police to invoke those procedures which moved the majority in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> In fact, the conversation was by all accounts a very brief one. According to uncontradicted testimony, petitioner was awake when the officers entered his room, and they asked him four questions: his name, whether he had been at the El Farleto, whether he owned a pistol, and where it was. He gave his name, said he had been at the El Farleto, and admitted he owned a pistol without hesitation. He was slow in telling where the pistol was, and the question was repeated. He then took the police to the nearby washing machine where the gun was hidden.</p>
<p>It is unquestioned that this sequence of events in their totality would not constitute coercion in the traditional sense or lead any court to view the admissions as involuntary within the meaning of the rules by which we even now adjudicate claims of coercion relating to pre-<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> trials. And, realistically, had Orozco refused to answer the questions asked of him, it seems most unlikely that prolonged interrogation would have followed in petitioner's own quarters; nothing similar to the station house model invoked by the court would have occurred here. The police had petitioner's name and description, had ample evidence that he had been at the night club and suspected that he had a gun. Surely had he refused to give his name or answer any other questions, they would have arrested him anyway, searched the house and found the gun, which would have been clearly admissible under all relevant authorities. But the Court insists that this case be reversed for failure to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings.</p>
<p>I cannot accept the dilution of the custody requirements of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to this level, where the hazards to the <span class="star-pagination">*331</span> right to silence are so equivocal and unsupported by experience in a recurring number of cases. Orozco was apprehended in the most familiar quarters, the questioning was brief, and no admissions were made which were not backed up by other evidence. This case does not involve the confession of an innocent man, or even of a guilty man from whom a confession has been wrung by physical abuse or the modern psychological methods discussed in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> These are simply the terse remarks of a man who has been caught, almost in the act. Even if there were reason to encourage suspects to consult lawyers to tell them to be silent before quizzing at the station house, there is no reason why police in the field should have to preface every casual question of a suspect with the full panoply of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. The same danger of coercion is simply not present in such circumstances, and the answers to the questions may as often clear a suspect as help convict him. If the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings have their intended effect, and the police are able to get no answers from suspects, innocent or guilty, without arresting them, then a great many more innocent men will be making unnecessary trips to the station house. Ultimately it may be necessary to arrest a man, bring him to the police station, and provide a lawyer, just to discover his name. Even if the man is innocent the process will be an unpleasant one.</p>
<p>Since the Court's extension of <i>Miranda's</i> rule takes it into territory where even what rationale there originally was disappears, I dissent.</p>
<p>Memorandum of MR. JUSTICE STEWART.</p>
<p>Although there is much to be said for MR. JUSTICE HARLAN'S position, I join my Brother WHITE in dissent. It seems to me that those of us who dissented in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, remain free not only to express our continuing disagreement with that decision, but also to oppose any broadening of its impact.</p>
<h2>NOTES</h2>
<p>[1]  The state court also rejected a contention that use of the evidence also violated the Fourth Amendment's provision against unreasonable searches and seizures. Our holding makes it unnecessary for us to consider that contention.</p>
<p>[2]  See <i>Johnson</i> v. <i>New Jersey,</i> <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719</a></span> (1966).</p>
<p>[3]  The State appears to urge that petitioner's <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> claim is unreviewable in this Court because the objection made by trial counsel to the officer's testimony was not sufficiently "specific." We fail to perceive how this could be an adequate state ground in view of the fact that the Texas Court of Criminal Appeals specifically decided that the introduction of petitioner's statement made to the officers "was not precluded under Miranda v. State of Arizona," <span class="citation" data-id="9647819"><a href="/opinion/1527140/orozco-v-state/#672" aria-description="Citation for case: Orozco v. State">428 S. W. 2d 666, 672</a></span>, while the dissenting judge thought that it was.</p>
<p>[4]  In light of some apparent misunderstanding on this point, it is perhaps appropriate to point out once again that a reversal by this Court of a conviction based in part on unconstitutional evidence leaves the State free to retry the defendant without the tainted evidence.</p>

</div>
```

---

## GROUP: content/cases/Patterson v. Illinois.md  (`case`, 5 assertions)

### content_page

```
---
title: "Patterson v. Illinois"
type: case
citation: "487 U.S. 285 (1988)"
parallel_cite: "108 S. Ct. 2389; 101 L. Ed. 2d 261; 56 U.S.L.W. 4733"
neutral_cite: 1988 U.S. LEXIS 2876
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1988
date_decided: 1988-06-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1988-06-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Patterson v. Illinois
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112127/patterson-v-illinois/"
  cluster_id: 112127
  opinion_id: 9431404
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brewer v. Williams]]", "[[Rothgery v. Gillespie County]]", "[[Michigan v. Jackson]]", "[[Edwards v. Arizona]]", "[[Montejo v. Louisiana]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "waiver", "post-indictment", "miranda"]
holding: "An accused may knowingly and intelligently waive the Sixth Amendment right to counsel for post-indictment questioning through the…"
lake:
  record_id: Patterson v. Illinois
  status: verified
  projected_at: 2026-07-06
---

# Patterson v. Illinois

*487 U.S. 285 (1988)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After Patterson was indicted for a gang-related murder, and before he had retained or requested counsel, an officer informed him he had been formally charged, administered the *[[Miranda v. Arizona|Miranda]]* warnings, and questioned him. Patterson waived his rights and made incriminating statements, which were used at his trial.

## Issue
Whether an accused may waive his Sixth Amendment right to counsel for post-indictment questioning on the strength of the *[[Miranda v. Arizona|Miranda]]* warnings, where he has not retained or requested counsel.

## Rule
Yes. "As a general matter, then, an accused who is admonished with the warnings prescribed by this Court in *Miranda* . . . has been sufficiently apprised of the nature of his Sixth Amendment rights, and of the consequences of abandoning those rights, so that his waiver on this basis will be considered a knowing and intelligent one." — 487 U.S. at 296. ^pin-296

## Application
Patterson was given the *[[Miranda v. Arizona|Miranda]]* warnings, which informed him of his right to have counsel present during questioning and of the consequences of proceeding without one; under close questioning he could identify no additional information he should have received before deciding to waive. Because he had not retained or requested a lawyer, the warnings sufficiently apprised him of his Sixth Amendment rights, and his post-indictment waiver was knowing and intelligent. His statements were admissible.

## Conclusion
A *[[Miranda v. Arizona|Miranda]]*-warned waiver was a valid waiver of the Sixth Amendment right to counsel for post-indictment questioning on these facts; the conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Patterson* remains good law; [[Montejo v. Louisiana]] later relied on it in overruling [[Michigan v. Jackson]], leaving *Patterson*'s waiver rule intact.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny / Refinement*

## Sources
- *Patterson v. Illinois*, 487 U.S. 285 (1988) — https://www.courtlistener.com/opinion/112127/patterson-v-illinois/ — pinpoint: 296.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "eb933f387e9be5c0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "487 U.S. 285 (1988)", "court": "U.S. Supreme Court", "neutral_cite": "1988 U.S. LEXIS 2876", "official_citation_present": true, "parallel_cite": "108 S. Ct. 2389; 101 L. Ed. 2d 261; 56 U.S.L.W. 4733", "title": "Patterson v. Illinois", "year": "1988"}}
{"assertion_id": "a071a4461b14140b", "dimension": "support", "kind": "home_role", "locator": {"home": "Sixth Amendment Right to Counsel"}, "payload": {"home": "Sixth Amendment Right to Counsel", "role": "Key — Progeny / Refinement", "title": "Patterson v. Illinois"}}
{"assertion_id": "a992a444fb2752e2", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An accused may knowingly and intelligently waive the Sixth Amendment right to counsel for post-indictment questioning through the…", "title": "Patterson v. Illinois"}}
{"assertion_id": "9adda10bb706b90e", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Patterson v. Illinois"}}
{"assertion_id": "dcf649599fa6a243", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1988-06-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Patterson v. Illinois", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Patterson v. Illinois", "varies_by_point": "false"}}
```

### lake record — Patterson v. Illinois

```json
{
  "schema_version": "s2.v1",
  "record_id": "Patterson v. Illinois",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Patterson v. Illinois",
    "case_name_short": "Patterson",
    "case_name_full": "Patterson v. Illinois",
    "input_case_name": "Patterson v. Illinois",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1988-06-24",
    "year": 1988,
    "docket": null,
    "cluster_id": 112127,
    "lead_opinion_id": 9431404,
    "sibling_ids": [
      112127,
      9431404,
      9431405,
      9431406
    ],
    "absolute_url": "/opinion/112127/patterson-v-illinois/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9074851,
        "score": 20,
        "case_name": "Patterson v. Illinois"
      },
      {
        "cluster_id": 9074850,
        "score": 20,
        "case_name": "Patterson v. Illinois"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "487 U.S. 285",
      "volume": "487",
      "reporter": "U.S.",
      "page": "285",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "108 S. Ct. 2389",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "2389",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 L. Ed. 2d 261",
        "volume": "101",
        "reporter": "L. Ed. 2d",
        "page": "261",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 U.S.L.W. 4733",
        "volume": "56",
        "reporter": "U.S.L.W.",
        "page": "4733",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1988 U.S. LEXIS 2876",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "2876",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "487 U.S. 285",
        "volume": "487",
        "reporter": "U.S.",
        "page": "285",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "108 S. Ct. 2389",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "2389",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 L. Ed. 2d 261",
        "volume": "101",
        "reporter": "L. Ed. 2d",
        "page": "261",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 U.S. LEXIS 2876",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "2876",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 U.S.L.W. 4733",
        "volume": "56",
        "reporter": "U.S.L.W.",
        "page": "4733",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "487 U.S. 285",
    "official_selection": {
      "court_class": "scotus",
      "selected": "487 U.S. 285",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-296",
      "page": null,
      "quote": "--- # Patterson v. Illinois *487 U.S. 285 (1988)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After Patterson was indicted for a gang-related murder, and before he had retained or requested counsel, an officer informed him he had been formally charged, administered the *Miranda* warnings, and questioned him. Patterson waived his rights and made incriminating statements, which were used at his trial. ## Issue Whether an accused may waive his Sixth Amendment right to counsel for post-indictment questioning on the strength of the *Miranda* warnings, where he has not retained or requested counsel. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1988-06-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Patterson v. Illinois",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Jones v. Stephens",
          "cluster_id": 7317930,
          "cite": [
            "157 F. Supp. 3d 623",
            "2016 U.S. Dist. LEXIS 3888",
            "2016 WL 147919"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Savino Braxton",
          "cluster_id": 2797003,
          "cite": [
            "784 F.3d 240",
            "2015 U.S. App. LEXIS 6990",
            "2015 WL 1905882"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth, Aplt v. Hill, E.",
          "cluster_id": 2754405,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Leonard Kidd v. Michael Lemke",
          "cluster_id": 2709205,
          "cite": [
            "734 F.3d 696",
            "2013 WL 5855718",
            "2013 U.S. App. LEXIS 22303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hodson v. State",
          "cluster_id": 2542781,
          "cite": [
            "350 S.W.3d 169",
            "2011 WL 1796088"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Crampe",
          "cluster_id": 5641118,
          "cite": [
            "17 N.Y.3d 469",
            "957 N.E.2d 255"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane1_negative"
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
        "journal_ref": "Patterson v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Flores v. State",
          "cluster_id": 1871985,
          "cite": [
            "299 S.W.3d 843",
            "2009 WL 3466009"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kansas v. Ventris",
          "cluster_id": 145880,
          "cite": [
            "173 L. Ed. 2d 801",
            "129 S. Ct. 1841",
            "556 U.S. 586",
            "2009 U.S. LEXIS 3299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane1_negative"
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
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Martinez v. Court of Appeal of California, Fourth Appellate District",
          "cluster_id": 118328,
          "cite": [
            "145 L. Ed. 2d 597",
            "120 S. Ct. 684",
            "528 U.S. 152",
            "2000 U.S. LEXIS 502"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Frye",
          "cluster_id": 5607916,
          "cite": [
            "18 Cal. 4th 894",
            "98 Cal. Daily Op. Serv. 5949",
            "959 P.2d 183",
            "98 Daily Journal DAR 8259",
            "77 Cal. Rptr. 2d 25",
            "1998 Cal. LEXIS 4688"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Iowa v. Tovar",
          "cluster_id": 134725,
          "cite": [
            "158 L. Ed. 2d 209",
            "124 S. Ct. 1379",
            "541 U.S. 77",
            "2004 U.S. LEXIS 1837"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Harvey",
          "cluster_id": 112385,
          "cite": [
            "108 L. Ed. 2d 293",
            "110 S. Ct. 1176",
            "494 U.S. 344",
            "1990 U.S. LEXIS 1229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marvin Berkowitz",
          "cluster_id": 557342,
          "cite": [
            "927 F.2d 1376",
            "1991 U.S. App. LEXIS 4135",
            "1991 WL 33079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
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
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
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
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Cobb",
          "cluster_id": 118417,
          "cite": [
            "149 L. Ed. 2d 321",
            "121 S. Ct. 1335",
            "532 U.S. 162",
            "2001 U.S. LEXIS 2696"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fuller v. State",
          "cluster_id": 1575568,
          "cite": [
            "829 S.W.2d 191",
            "1992 Tex. Crim. App. LEXIS 62",
            "1992 WL 55274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rothgery v. Gillespie County",
          "cluster_id": 145785,
          "cite": [
            "171 L. Ed. 2d 366",
            "128 S. Ct. 2578",
            "554 U.S. 191",
            "2008 U.S. LEXIS 5057",
            "21 Fla. L. Weekly Fed. S 429",
            "76 U.S.L.W. 4520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yousef",
          "cluster_id": 781722,
          "cite": [
            "327 F.3d 56",
            "61 Fed. R. Serv. 251",
            "2003 U.S. App. LEXIS 6437"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Briggs",
          "cluster_id": 2550075,
          "cite": [
            "12 A.3d 291",
            "608 Pa. 430",
            "2011 Pa. LEXIS 107"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
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
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Carter",
          "cluster_id": 2639408,
          "cite": [
            "70 P.3d 981",
            "135 Cal. Rptr. 2d 553",
            "30 Cal. 4th 1166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Willie v. State",
          "cluster_id": 1706565,
          "cite": [
            "585 So. 2d 660",
            "1991 WL 142136"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
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
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rigoberto Moya-Gomez Celestino Orlando Estevez Amado Raphael Leon Adalberto Herrera and Menelao Orlando Estevez",
          "cluster_id": 513458,
          "cite": [
            "860 F.2d 706"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Conway",
          "cluster_id": 6894227,
          "cite": [
            "108 Ohio St. 3d 214"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Collins",
          "cluster_id": 2518032,
          "cite": [
            "232 P.3d 32",
            "49 Cal. 4th 175",
            "110 Cal. Rptr. 3d 384",
            "2010 Cal. LEXIS 5032"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Sully",
          "cluster_id": 1386747,
          "cite": [
            "812 P.2d 163",
            "53 Cal. 3d 1195",
            "283 Cal. Rptr. 144",
            "91 Cal. Daily Op. Serv. 5489",
            "1991 Cal. LEXIS 2977"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Posada-Rios",
          "cluster_id": 16117,
          "cite": [
            "158 F.3d 832",
            "1998 WL 736317"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Guerrero, Ex Parte Marcelino",
          "cluster_id": 2948089,
          "cite": [
            "400 S.W.3d 576",
            "2013 WL 2419595",
            "2013 Tex. Crim. App. LEXIS 820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Posada-Rios",
          "cluster_id": 758679,
          "cite": [
            "158 F.3d 832",
            "1998 WL 736317"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yousef",
          "cluster_id": 8437415,
          "cite": [
            "327 F.3d 56"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112127 OR 9431404 OR 9431405 OR 9431406) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjEzNTc0NDAwMDAwJnM9MzE0Njk5NyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112127+OR+9431404+OR+9431405+OR+9431406%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 10,
        "triage_snippet_classified": 190
      },
      "lane2_top_cited": {
        "query": "cites:(112127 OR 9431404 OR 9431405 OR 9431406)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzkmcz0xNDU4ODAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112127+OR+9431404+OR+9431405+OR+9431406%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112127 OR 9431404 OR 9431405 OR 9431406)",
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
    "complete_query": "cites:(112127 OR 9431404 OR 9431405 OR 9431406)",
    "indexed_citing_opinions": 643,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112127,
        "count": 574,
        "count_source": "search"
      },
      {
        "opinion_id": 9431404,
        "count": 86,
        "count_source": "search"
      },
      {
        "opinion_id": 9431405,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431406,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1013,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/patterson-v-illinois.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyMjIwNTgmcz05MzkxNTQwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112127+OR+9431404+OR+9431405+OR+9431406%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112127,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 104496,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 105449,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 108846,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 109309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 109492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 110300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 110809,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 111193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 111546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 112074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 112100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 374894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 379999,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 418052,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 437719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 454503,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 1653387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 1875896,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 2037100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 2043878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 2140351,
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
    "date_created": "2026-07-05T16:31:32Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:32:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:32:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:36:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:32:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Patterson v. Illinois

```
<opinion type="majority">
<author id="b339-8">Justice White</author>
<p id="Anm">delivered the opinion of the Court.</p>
<p id="b339-9">In this case, we are called on to determine whether the interrogation of petitioner after his indictment violated his Sixth Amendment right to counsel.</p>
<p id="AGdq">I</p>
<p id="b339-3">Before dawn on August 21, 1983, petitioner and other members of the “Vice Lords” street gang became involved in a fight with members of a rival gang, the “Black Mobsters.” Some time after the. fight, a former member of the Black Mobsters, James Jackson, went to the home where the Vice Lords had fled. A second fight broke out there, with petitioner and three other Vice Lords beating Jackson severely. The Vice Lords then put Jackson into a car, drove to the end of a nearby street, and left him face down in a puddle of water. Later that morning, police discovered Jackson, dead, where he had been left.</p>
<p id="b339-4">That afternoon, local police officers obtained warrants for the arrest of the Vice Lords, on charges of battery and mob action, in connection with the first fight. One of the gang members who was arrested gave the police a statement concerning the first fight; the statement also implicated several of the Vice Lords (including petitioner) in Jackson’s murder. A few hours later, petitioner was apprehended. Petitioner was informed of his rights under <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), and volunteered to answer questions put to him by the police. Petitioner gave a statement concerning the initial fight between the rival gangs, but denied knowing anything <page-number citation-index="1" label="288">*288</page-number>about Jackson’s death. Petitioner was held in custody the following day, August 22, as law enforcement authorities completed their investigation of the Jackson murder.</p>
<p id="b340-5">On August 23, a Cook County grand jury indicted petitioner and two other gang members for the murder of James Jackson. Police Officer Michael Gresham, who had questioned petitioner earlier, removed him from the lockup where he was being held, and told petitioner that because he had been indicted he was being transferred to the Cook County jail. Petitioner asked Gresham which of the gang members had been charged with Jackson’s murder, and upon learning that one particular Vice Lord had been omitted from the indictments, asked: “[W]hy wasn’t he indicted, he did everything.” App. 7. Petitioner also began to explain that there was a witness who would support his account of the crime.</p>
<p id="b340-6">At this point, Gresham interrupted petitioner, and handed him a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver form. The form contained five specific warnings, as suggested by this Court’s <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>decision, to make petitioner aware of his right to counsel and of the consequences of any statement he might make to police.<footnotemark>1</footnotemark> Gresham read the warnings aloud, as petitioner read along with him. Petitioner initialed each of the five warnings, and signed the waiver form. Petitioner then gave a lengthy statement to police officers concerning the Jackson murder; petitioner’s statement described in detail the role of each of the Vice Lords — including himself — in the murder of James Jackson.</p>
<p id="b340-7">Later that day, petitioner confessed involvement in the murder for a second time. This confession came in an inter<page-number citation-index="1" label="289">*289</page-number>view with Assistant State’s Attorney (ASA) George Smith. At the outset of the interview, Smith reviewed with petitioner the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver he had previously signed, and petitioner confirmed that he had signed the waiver and understood his rights. Smith went through the waiver procedure once again: reading petitioner his rights, having petitioner initial each one, and sign a waiver form. In addition, Smith informed petitioner that he was a lawyer working with the police investigating the Jackson case. Petitioner then gave another inculpatory statement concerning the crime.</p>
<p id="b341-5">Before trial, petitioner moved to suppress his statements, arguing that they were obtained in a manner at odds with various constitutional guarantees. The trial court denied these motions, and the statements were used against petitioner at his trial. The jury found petitioner guilty of murder, and petitioner was sentenced to a 24-year prison term.</p>
<p id="b341-6">On appeal, petitioner argued that he had not “knowingly and intelligently” waived his Sixth Amendment right to counsel before he gave his uncounseled postindictment confessions. Petitioner contended that the warnings he received, while adequate for the purposes of protecting his <em>Fifth </em>Amendment rights as guaranteed by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>did not adequately inform him of his <em>Sixth </em>Amendment right to counsel. The Illinois Supreme Court, however, rejected this theory, applying its previous decision in <em>People </em>v. <em>Owens, </em><span class="citation" data-id="9724847"><a href="/opinion/2140351/people-v-owens/" aria-description="Citation for case: People v. Owens">102 Ill. 2d 88</a></span>, <span class="citation" data-id="9724847"><a href="/opinion/2140351/people-v-owens/" aria-description="Citation for case: People v. Owens">464 N. E. 2d 261</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./469/963/">469 U. S. 963</a></span> (1984), which had held that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings were sufficient to make a defendant aware of his Sixth Amendment right to counsel during postindictment questioning. <em>People </em>v. <em>Thomas, </em><span class="citation" data-id="2043878"><a href="/opinion/2043878/people-v-thomas/#298" aria-description="Citation for case: People v. Thomas">116 Ill. 2d 290, 298-300</a></span>, <span class="citation" data-id="2043878"><a href="/opinion/2043878/people-v-thomas/#846" aria-description="Citation for case: People v. Thomas">507 N. E. 2d 843, 846-847</a></span> (1987).</p>
<p id="b341-7">In reaching this conclusion, the Illinois Supreme Court noted that this Court had reserved decision on this question on several previous occasions<footnotemark>2</footnotemark> and that the lower courts are <page-number citation-index="1" label="290">*290</page-number>divided on the issue. <span class="citation" data-id="2043878"><a href="/opinion/2043878/people-v-thomas/#299" aria-description="Citation for case: People v. Thomas"><em>Id., </em>at 299</a></span>, <span class="citation" data-id="2043878"><a href="/opinion/2043878/people-v-thomas/#846" aria-description="Citation for case: People v. Thomas">507 N. E. 2d, at 846</a></span>. We granted this petition for certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./484/895/">484 U. S. 895</a></span> (1987), to resolve this split of authority and to address the issues we had previously left open.</p>
<p id="b342-5">II</p>
<p id="b342-6">There can be no doubt that petitioner had the right to have the assistance of counsel at his postindictment interviews with law enforcement authorities. Our cases make it plain that the Sixth Amendment guarantees this right to criminal defendants. <em>Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#629" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625, 629-630</a></span> (1986); <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#398" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387, 398-401</a></span> (1977); <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#205" aria-description="Citation for case: Massiah v. United States">377 U. S. 201, 205-207</a></span> (1964).<footnotemark>3</footnotemark> Petitioner asserts that the questioning that produced his incriminating statements violated his Sixth Amendment right to counsel in two ways.</p>
<p id="b342-7">A</p>
<p id="b342-8">Petitioner’s first claim is that because his Sixth Amendment right to counsel arose with his indictment, the police were thereafter barred from initiating a meeting with him. See Brief for Petitioner 30-31; Tr. of Oral Arg. 2, 9, 11, 17. He equates himself with a preindictment suspect who, while being interrogated, asserts his Fifth Amendment right to counsel; under <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981), such a suspect may not be questioned again unless he initiates the meeting.</p>
<p id="b342-9">Petitioner, however, at no time sought to exercise his right to have counsel present. The fact that petitioner’s Sixth <page-number citation-index="1" label="291">*291</page-number>Amendment right came into existence with his indictment, <em>i. e., </em>that he had such a right at the time of his questioning, does not distinguish him from the preindictment interrogatee whose right to counsel is in existence and available for his exercise while he is questioned. Had petitioner indicated he wanted the assistance of counsel, the authorities’ interview with him would have stopped, and further questioning would have been forbidden (unless petitioner called for such a meeting). This was our holding in <em>Michigan </em>v. <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson, supra,</a></span> </em>which applied <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>to the Sixth Amendment context. We observe that the analysis in <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>is rendered wholly unnecessary if petitioner’s position is correct: under petitioner’s theory, the officers in <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>would have been completely barred from approaching the accused in that case unless he called for them. Our decision in <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span>, </em>however, turned on the fact that the accused “ha[d] asked for the help of a lawyer” in dealing with the police. <span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#631" aria-description="Citation for case: Michigan v. Jackson"><em>Jackson, supra, </em>at 631, 633-635</a></span>.</p>
<p id="b343-5">At bottom, petitioner’s theory cannot be squared with our rationale in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>, </em>the case he relies on for support. <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rested on the view that once “an accused . . . ha[s] expressed his desire to deal with the police only through counsel” he should “not [be] subject to further interrogation by the authorities until counsel has been made available to him, unless the accused himself initiates further communication.” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona"><em>Edwards, supra, </em>at 484-485</a></span>; cf. also <em>Michigan </em>v. <em>Mosley, </em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#104" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 104, n. 10</a></span> (1975). Preserving the integrity of an accused’s choice to communicate with police only through counsel is the essence of <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>and its progeny— not barring an accused from making an <em>initial </em>election as to whether he will face the State’s officers during questioning with the aid of counsel, or go it alone. If an accused “knowingly and intelligently” pursues the latter course, we see no reason why the uncounseled statements he then makes must be excluded at his trial.</p>
<p id="b344-4"><page-number citation-index="1" label="292">*292</page-number>B</p>
<p id="b344-5">Petitioner’s principal and more substantial claim is that questioning him without counsel present violated the Sixth Amendment because he did not validly waive his right to have counsel present during the interviews. Since it is clear that after the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings were given to petitioner, he not only voluntarily answered questions without claiming his right to silence or his right to have a lawyer present to advise him but also executed a written waiver of his right to counsel during questioning, the specific issue posed here is whether this waiver was a “knowing and intelligent” waiver of his Sixth Amendment right.<footnotemark>4</footnotemark> See <em>Brewer </em>v. <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#401" aria-description="Citation for case: Brewer v. Williams"><em>Williams, supra, </em>at 401, 404</a></span>; <em>Johnson </em>v. <em>Zerbst, </em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 464-465</a></span> (1938).</p>
<p id="b344-6">In the past, this Court has held that a waiver of the Sixth Amendment right to. counsel is valid only when it reflects “an intentional relinquishment or abandonment of a known right or privilege.” <em>Johnson </em>v. <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst"><em>Zerbst, supra, </em>at 464</a></span>. In other words, the accused must “kno[w] what he is doing” so that “his choice is made with eyes open.” <em>Adams </em>v. <em>United States ex rel. McCann, </em><span class="citation" data-id="9419274"><a href="/opinion/103735/adams-v-united-states-ex-rel-mccann/#279" aria-description="Citation for case: Adams v. United States Ex Rel. McCann">317 U. S. 269, 279</a></span> (1942). In a case arising under the Fifth Amendment, we described this requirement as “a full awareness of both the nature of the right being abandoned and the consequences of the decision to abandon it.” <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#421" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 421</a></span> (1986). Whichever of these formulations is used, the key inquiry in a case such as this one must be: Was the accused, who waived his Sixth Amendment rights during postindictment questioning, made sufficiently aware of his right to have counsel present during the questioning, and of the possible conse<page-number citation-index="1" label="293">*293</page-number>quences of a decision to forgo the aid of counsel? In this case, we are convinced that by admonishing petitioner with the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, respondent has met this burden and that petitioner’s waiver of his right to counsel at the questioning was valid.<footnotemark>5</footnotemark></p>
<p id="b345-5">First, the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings given petitioner made him aware of his right to have counsel present during the questioning. By telling petitioner that he had a right to consult with an attorney, to have a lawyer present while he was questioned, and even to have a lawyer appointed for him if he could not afford to retain one on his own, Officer Gresham and ASA Smith conveyed to petitioner the sum and substance of the rights that the Sixth Amendment provided him. “Indeed, it seems self-evident that one who is told he” has such rights to counsel “is in a curious posture to later complain” that his waiver of these rights was unknowing. Cf. <em>United States </em>v. <em>Washington, </em><span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#188" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 188</a></span> (1977). There is little more petitioner could have possibly been told in an effort to satisfy this portion of the waiver inquiry.</p>
<p id="b345-6">Second, the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings also served to make petitioner aware of the consequences of a decision by him to waive his Sixth Amendment rights during postindictment questioning. Petitioner knew that any statement that he made could be used against him in subsequent criminal proceedings. This is the ultimate adverse consequence petitioner could have suffered by virtue of his choice to make <page-number citation-index="1" label="294">*294</page-number>uncounseled admissions to the authorities. This warning also sufficed — contrary to petitioner’s claim here, see Tr. of Oral Arg. 7-8 — to let petitioner know what a lawyer could “do for him” during the postindictment questioning: namely, advise petitioner to refrain from making any such statements.<footnotemark>6</footnotemark> By knowing what could be done with any statements he might make, and therefore, what benefit could be obtained by having the aid of counsel while making such statements, petitioner was essentially informed of the possible consequences of going without counsel during questioning. If petitioner nonetheless lacked “a full and complete appreciation of all of the consequences flowing” from his waiver, it does not defeat the State’s showing that the information it provided to him satisfied the constitutional minimum. Cf. <em>Oregon </em>v. <em>Elstad, </em><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#316" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 316-317</a></span> (1985).</p>
<p id="b346-5">Our conclusion is supported by petitioner’s inability, in the proceedings before this Court, to articulate with precision what additional information should have been provided to him before he would have been competent to waive his right to counsel. All that petitioner’s brief and reply brief suggest is petitioner-should have been made aware of his “right under the Sixth Amendment to the broad protection of counsel” — a rather nebulous suggestion — and the “gravity of [his] situation.” Reply Brief for Petitioner 13; see Brief for Petitioner 30-31. But surely this latter “requirement” (if it is one) was met when Officer Gresham informed petitioner that he had been formally charged with the murder of James Jackson. <page-number citation-index="1" label="295">*295</page-number>See n. 8, <em>infra. </em>Under close questioning on this same point at argument, petitioner likewise failed to suggest any meaningful additional information that he should have been, but was not, provided in advance of his decision to waive his right to counsel.<footnotemark>7</footnotemark> The discussions found in favorable court decisions, on which petitioner relies, are similarly lacking.<footnotemark>8</footnotemark></p>
<p id="b348-4"><page-number citation-index="1" label="296">*296</page-number>As a general matter, then, an accused who is admonished with the warnings prescribed by this Court in <em>Miranda, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 479</a></span>, has been sufficiently apprised of the nature of his Sixth Amendment rights, and of the consequences of abandoning those rights, so that his waiver on this basis will be considered a knowing and intelligent one.<footnotemark>9</footnotemark> We feel that <page-number citation-index="1" label="297">*297</page-number>our conclusion in a recent Fifth Amendment case is equally apposite here: “Once it is determined that a suspect's decision not to rely on his rights was uncoerced, that he at all times knew he could stand mute and request a lawyer, and that he was aware of the State’s intention to use his statements to secure a conviction, the analysis is complete and the waiver is valid as a matter of law.” See <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#422" aria-description="Citation for case: Moran v. Burbine">475 U. S., at 422-423</a></span>.</p>
<p id="b349-5">C</p>
<p id="b349-6">We consequently reject petitioner’s argument, which has some acceptance from courts and commentators,<footnotemark>10</footnotemark> that since “the sixth amendment right [to counsel] is far superior to that of the fifth amendment right” and since “[t]he greater the right the greater the loss from a waiver of that right,” waiver of an accused’s Sixth Amendment right to counsel should be “more difficult” to effectuate than waiver of a suspect’s Fifth Amendment rights. Brief for Petitioner 23. While our cases have recognized a “difference” between the Fifth Amendment and Sixth Amendment rights to counsel, and the “policies” behind these constitutional guarantees,<footnotemark>11</footnotemark> we have never suggested that one right is “superior” or “greater” than the other, nor is there any support in our cases for the notion that be<page-number citation-index="1" label="298">*298</page-number>cause a Sixth Amendment right may be involved, it is more difficult to waive than the Fifth Amendment counterpart.</p>
<p id="b350-5">Instead, we have taken a more pragmatic approach to the waiver question — asking what purposes a lawyer can serve at the particular stage of the proceedings in question, and what assistance he could provide to an accused at that stage — to determine the scope of the Sixth Amendment right to counsel, and the type of warnings and procedures that should be required before a waiver of that right will be recognized.</p>
<p id="b350-6">At one end of the spectrum, we have concluded there is no Sixth Amendment right to counsel whatsoever at a postin-dictment photographic display identification, because this procedure is not one at which the accused “require[s] aid in coping with legal problems or assistance in meeting his adversary.” See <em>United States </em>v. <em>Ash, </em><span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/#313" aria-description="Citation for case: United States v. Ash">413 U. S. 300, 313-320</a></span> (1973). At the other extreme, recognizing the enormous importance and role that an attorney plays at a criminal trial, we have imposed the most rigorous restrictions on the information that must be conveyed to a defendant, and the procedures that must be observed, before permitting him to waive his right to counsel at trial. See <em>Faretta </em>v. <em>California, </em><span class="citation" data-id="9426191"><a href="/opinion/109309/faretta-v-california/#835" aria-description="Citation for case: Faretta v. California">422 U. S. 806, 835-836</a></span> (1975); cf. <em>Von Moltke </em>v. <em>Gillies, </em><span class="citation" data-id="9420085"><a href="/opinion/104496/von-moltke-v-gillies/#723" aria-description="Citation for case: Von Moltke v. Gillies">332 U. S. 708, 723-724</a></span> (1948). In these extreme cases, and in others that fall between these two poles, we have defined the scope of the right to counsel by a pragmatic assessment of the usefulness of counsel to the accused at the particular proceeding, and the dangers to the accused of proceeding without counsel. An accused’s waiver of his right to counsel is “knowing” when he is made aware of these basic facts.</p>
<p id="b350-7">Applying this approach, it is our view that whatever warnings suffice for <em>Miranda’s </em>purposes will also be sufficient in the context of postindictment questioning. The State’s decision to take an additional step and commence formal adversarial proceedings against the accused does not substantially increase the value of counsel to the accused at questioning, or expand the limited purpose that an attorney serves when the <page-number citation-index="1" label="299">*299</page-number>accused is questioned by authorities. With respect to this inquiry, we do not discern a substantial difference between the usefulness of a lawyer to a suspect during custodial interrogation, and his value to an accused at postindictment questioning.<footnotemark>12</footnotemark></p>
<p id="b351-5">Thus, we require a more searching or formal inquiry before permitting an accused to waive his right to counsel at trial than we require for a Sixth Amendment waiver during post-indictment <em>questioning </em>— not because postindictment questioning is “less important” than a trial (the analysis that petitioner’s “hierarchical” approach would suggest) — but because the full “dangers and disadvantages of self-representation,” <span class="citation" data-id="9426191"><a href="/opinion/109309/faretta-v-california/#835" aria-description="Citation for case: Faretta v. California"><em>Faretta, supra, </em>at 835</a></span>, during questioning are less substantial and more obvious to an accused than they are at trial.<footnotemark>13</footnotemark> Because the role of counsel at questioning is relatively simple and limited, we see no problem in having a waiver procedure at that stage which is likewise simple and limited. So long as the accused is made aware of the “dangers and disadvantages <page-number citation-index="1" label="300">*300</page-number>of self-representation” during postindictment questioning, by use of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, his waiver of his Sixth Amendment right to counsel at such questioning is “knowing and intelligent.”</p>
<p id="b352-5">Ill</p>
<p id="b352-6">Before confessing to the murder of James Jackson, petitioner was meticulously informed by authorities of his right to counsel, and of the consequences of any choice not to exercise that right. On two separate occasions, petitioner elected to forgo the assistance of counsel, and speak directly to officials concerning his role in the murder. Because we believe that petitioner’s waiver of his Sixth Amendment rights was “knowing and intelligent,” we find no error in the decision of the trial court to permit petitioner’s confessions to be used against him. Consequently, the judgment of the Illinois Supreme Court is</p>
<p id="b352-7">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b340-8"> Although the signed waiver form does not appear in the record or the appendix, petitioner concedes that he was informed of his right to counsel to the extent required by our decision in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Brief for Petitioner 3; Tr. of Oral Arg. 6-8.</p>
<p id="b340-9">This apparently included informing petitioner that he had a right to remain silent; that anything he might say could be used against him; that he had a right to consult with an attorney; that he had a right to have an attorney present during interrogation; and that, as an indigent, the State would provide him with a lawyer if he so desired.</p>
</footnote>
<footnote label="2">
<p id="b341-8">See, <em>e. g., Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#635" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625, 635-636, n. 10</a></span> (1986); <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#428" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 428, n. 2</a></span> (1986); <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#405" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387, 405-406</a></span> (1977).</p>
</footnote>
<footnote label="3">
<p id="b342-10"> We note as a matter of some significance that petitioner had not retained, or accepted by appointment, a lawyer to represent him at the time he was questioned by authorities. Once an accused has a lawyer, a distinct set of constitutional safeguards aimed at preserving the sanctity of the attorney-client relationship takes effect. See <em>Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#176" aria-description="Citation for case: Maine v. Moulton">474 U. S. 159, 176</a></span> (1985). The State conceded as much at argument. See Tr. of Oral Arg. 28.</p>
<p id="b342-11">Indeed, the analysis changes markedly once an accused even <em>requests </em>the assistance of counsel. See <em>Michigan </em>v. <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson, supra;</a></span> </em>Part II-A, <em>infra.</em></p>
</footnote>
<footnote label="4">
<p id="b344-7"> Of course, we also require that any such waiver must be voluntary. Petitioner contested, the voluntariness of his confession in the trial court and in the intermediate appellate courts, which rejected petitioner’s claim that his confessions were coerced. See <span class="citation" data-id="2037100"><a href="/opinion/2037100/people-v-patterson/#425" aria-description="Citation for case: People v. Patterson">140 Ill. App. 3d 421, 425-426</a></span>, <span class="citation" data-id="2037100"><a href="/opinion/2037100/people-v-patterson/#1287" aria-description="Citation for case: People v. Patterson">488 N. E. 2d 1283, 1287</a></span> (1986).</p>
<p id="b344-8">Petitioner does not appear to have maintained this contention before the Illinois Supreme Court, and in any event, he does not press this argument here. Thus, the “yoluntariness” of petitioner’s confessions is not before us.</p>
</footnote>
<footnote label="5">
<p id="b345-7"> We emphasize the significance of the fact that petitioner’s waiver of counsel was only for this limited aspect of the criminal proceedings against him — only for postindictment questioning. Our decision on the validity of petitioner’s waiver extends only so far.</p>
<p id="b345-8">Moreover, even within this limited context, we note that petitioner’s waiver was binding on him <em>only </em>so long as he wished it to be. Under this Court’s precedents, at any time during the questioning petitioner could have changed his mind, elected to have the assistance of counsel, and immediately dissolve the effectiveness of his waiver with respect to any subsequent statements. See, <em>e. g., Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#631" aria-description="Citation for case: Michigan v. Jackson">475 U. S., at 631-635</a></span>; Part II-A, <em>supra. </em>Our decision today does nothing to change this rule.</p>
</footnote>
<footnote label="6">
<p id="b346-6"> An important basis for our analysis is our understanding that an attorney’s role at postindictment questioning is rather limited, and substantially different from the attorney’s role in later phases of criminal proceedings. At trial, an accused needs an attorney to perform several varied functions —some of which are entirely beyond even the most intelligent layman. Yet during postindictment questioning, a lawyer’s role is rather unidimen-sional: largely limited to advising his client as to what questions to answer and which ones to decline to answer.</p>
<p id="b346-7">We discuss this point in greater detail below. See Part II-C, <em>infra.</em></p>
</footnote>
<footnote label="7">
<p id="b347-5"> Representative excerpts from the relevant portions of argument include the following:</p>
<p id="b347-6">“QUESTION: [Petitioner] . . . was told that he had a right to counsel.</p>
<p id="b347-7">“MR. HONCHELL [petitioner’s counsel]: He was told — the word ‘counsel’ was used. He was told he had a right to counsel. But not through information by which it would become meaningful to him, because the method that was used was not designed to alert the accused to the Sixth Amendment rights to counsel. . . .</p>
<p id="b347-8">“QUESTION: . . . You mean they should have said you have a Sixth Amendment right to counsel instead of just, you have a right to counsel?</p>
<p id="b347-9">“He knew he had a right to have counsel present before [he] made the confession. Now, what in addition did he have to know to make the waiver an intelligent one?</p>
<p id="b347-10">“MR. HONCHELL: He had to meaningfully know he had a Sixth Amendment right to counsel present because—</p>
<p id="b347-11">“QUESTION: What is the difference between meaningfully knowing and knowing?</p>
<p id="b347-12">“MR. HONCHELL: Because the warning here used did not convey or express what counsel was intended to do for him after indictment.</p>
<p id="b347-13">“QUESTION: So then you say . . . [that] he would have had to be told more about what counsel would do for him after indictment before he could intelligently waive?</p>
<p id="b347-14">“MR. HONCHELL: That there is a right to counsel who would act on his behalf and represent him. '</p>
<p id="b347-15">“QUESTION: Well, okay. So it should have said, in addition to saying counsel, counsel who would act on your behalf and represent you? That would have been the magic solution?</p>
<p id="b347-16">“MR. HONCHELL: That is a possible method, yes.” Tr. of Oral Arg. 7-8.</p>
<p id="b347-17">We do not believe that adding the words “who would act on your behalf and represent you” in Sixth Amendment cases would provide any meaningful improvement in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. Cf. <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#435" aria-description="Citation for case: Brewer v. Williams">430 U. S., at 435-436, n. 5</a></span> (White, J., dissenting).</p>
</footnote>
<footnote label="8">
<p id="b347-18"> Even those lower court cases which have suggested that something beyond <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings is —or may be — required before a Sixth Amend<page-number citation-index="1" label="296">*296</page-number>ment waiver can be considered “knowing and intelligent” have failed to suggest just what this “something more” should be. See, e. <em>g., Felder </em>v. <em>McCotter, </em><span class="citation" data-id="454503"><a href="/opinion/454503/sammie-felder-jr-v-ol-mccotter-director-texas-department-of/#1250" aria-description="Citation for case: Sammie Felder, Jr. v. O.L. McCotter Director, Texas...">765 F. 2d 1245, 1250</a></span> (CA5 1985); <em>Robinson </em>v. <em>Percy, </em><span class="citation" data-id="437719"><a href="/opinion/437719/eric-robinson-v-donald-e-percy-secretary-department-of-health-and/#222" aria-description="Citation for case: Eric Robinson v. Donald E. Percy, Secretary, Department...">738 F. 2d 214, 222</a></span> (CA7 1984); <em>Fields </em>v. <em>Wyrick, </em><span class="citation" data-id="418052"><a href="/opinion/418052/edward-fields-v-donald-wyrick/#880" aria-description="Citation for case: Edward Fields v. Donald Wyrick">706 F. 2d 879, 880-881</a></span> (CA8 1983).</p>
<p id="b348-9">An exception to this is the occasional suggestion that, in addition to the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, an accused should be informed that he has been indicted before a postindictment waiver is sought. See, <em>e. g., United States </em>v. <em>Mohabir, </em><span class="citation" data-id="379999"><a href="/opinion/379999/united-states-v-lionel-mohabir/#1150" aria-description="Citation for case: United States v. Lionel Mohabir">624 F. 2d 1140, 1150</a></span> (CA2 1980); <em>United States </em>v. <em>Payton, </em><span class="citation" data-id="374894"><a href="/opinion/374894/united-states-v-william-charles-payton/#924" aria-description="Citation for case: United States v. William Charles Payton">615 F. 2d 922, 924-925</a></span> (CA1), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./446/969/">446 U. S. 969</a></span> (1980). Because, in this case, petitioner concedes that he was so informed, see Brief for Petitioner 3, we do not address the question whether or not an accused must be told that he has been indicted before a postindictment Sixth Amendment waiver will be valid. Nor do we even pass on the desirability of so informing the accused — a matter that can be reasonably debated. See, <em>e. g., </em>Tr. of Oral Arg. 24.</p>
<p id="b348-12">Beyond this, only one Court of Appeals —the Second Circuit —has adopted substantive or procedural requirements (in addition to <em>Miranda) </em>that must be completed before a Sixth Amendment waiver can be effectuated for postindictment questioning. See <em>United States </em>v. <em>Mohabir, </em><span class="citation" data-id="379999"><a href="/opinion/379999/united-states-v-lionel-mohabir/#1150" aria-description="Citation for case: United States v. Lionel Mohabir">624 F. 2d, at 1150-1153</a></span>. As have a majority of the Courts of Appeals, we reject <em>Moha-</em>bifs holding that some “additional” warnings or discussions with an accused are required in this situation, or that any waiver in this context can only properly be made before a “neutral . . . judicial officer.” <em><span class="citation" data-id="379999"><a href="/opinion/379999/united-states-v-lionel-mohabir/" aria-description="Citation for case: United States v. Lionel Mohabir">Ibid.</a></span></em></p>
</footnote>
<footnote label="9">
<p id="b348-13"> This does not mean, of course, that all Sixth Amendment challenges to the conduct of postindictment questioning will fail whenever the challenged practice would pass constitutional muster under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>For example, we have permitted a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver to stand where a suspect was not told that his lawyer was trying to reach him during questioning; in the Sixth Amendment context, this waiver would not be valid. See <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#424" aria-description="Citation for case: Moran v. Burbine">475 U. S., at 424, 428</a></span>. Likewise a surreptitious conversation between an undercover police officer and an unindieted suspect would not give rise to any <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>violation as long as the “interrogation” was not in a custodial setting, see <em>Miranda, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 475</a></span>; however, once the <page-number citation-index="1" label="297">*297</page-number>accused is indicted, such questioning would be prohibited. See <em>United States </em>v. <em>Henry, </em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#273" aria-description="Citation for case: United States v. Henry">447 U. S. 264, 273, 274-275</a></span> (1980).</p>
<p id="b349-8">Thus, because the Sixth Amendment’s protection of the attorney-client relationship — “the right to rely on counsel as a ‘medium’ between [the accused] and the State” — extends beyond <em>Miranda's </em>protection of the Fifth Amendment right to counsel, see <em>Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#176" aria-description="Citation for case: Maine v. Moulton">474 U. S., at 176</a></span>, there will be cases where a waiver which would be valid under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>will not suffice for-Sixth Amendment purposes. See also <em>Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#632" aria-description="Citation for case: Michigan v. Jackson">475 U. S., at 632</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b349-9">See, <em>e. g., United States </em>v. <span class="citation" data-id="379999"><a href="/opinion/379999/united-states-v-lionel-mohabir/#1149" aria-description="Citation for case: United States v. Lionel Mohabir"><em>Mohabir, supra, </em>at 1149-1152</a></span>; Note, Proposed Requirements for Waiver of the Sixth Amendment Right to Counsel, 82 Colum. L.- Rev. 363, 372 (1982).</p>
</footnote>
<footnote label="11">
<p id="b349-10">See, e. <em>g., Michigan </em>v. <span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#633" aria-description="Citation for case: Michigan v. Jackson"><em>Jackson, supra, </em>at 633, n. 7</a></span>; <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#300" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 300, n. 4</a></span> (1980).</p>
</footnote>
<footnote label="12">
<p id="b351-6"> We note, incidentally, that in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>decision itself, the analysis and disposition of the waiver question relied on this Court's decision in <em>Johnson </em>v. <em>Zerbst, </em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458</a></span> (1938) — a <em>Sixth </em>Amendment waiver case. See <em>Miranda, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 475</a></span>.</p>
<p id="b351-7">From the outset, then, this Court has recognized that the waiver inquiry focuses more on the lawyer’s role during such questioning, rather than the particular constitutional guarantee that gives rise to the right to counsel at that proceeding. See <em>ibid.; </em>see also <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#421" aria-description="Citation for case: Moran v. Burbine">475 U. S., at 421</a></span>. Thus, it should be no surprise that we now find a strong similarity between the level of knowledge a defendant must have to waive his Fifth Amendment right to counsel, and the protection accorded to Sixth Amendment rights. See Comment, Constitutional Law — Right to Counsel, <span class="citation no-link">49 Geo. Wash. L. Rev. 399</span>, 409 (1981).</p>
</footnote>
<footnote label="13">
<p id="b351-8"> As discussed above, see n. 6, <em>supra, </em>an attorney’s role at questioning is relatively limited. But at trial, counsel is required to help even the most gifted layman adhere to the rules of procedure and evidence, comprehend the subtleties of <em>voir dire, </em>examine and cross-examine witnesses effectively (including the accused), object to improper prosecution questions, and much more. Cf., <em>e. g., </em>1 Bench Book for United States District Court Judges 1.02-2 — 1.02-5 (3d ed. 1986); <em>McDowell </em>v. <em>United States, </em><span class="citation" data-id="9431199"><a href="/opinion/112002/mcdowell-v-united-states/" aria-description="Citation for case: McDowell v. United States">484 U. S. 980</a></span> (1987) (White, J., dissenting from denial of certiorari).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Pearson v. Callahan.md  (`case`, 5 assertions)

### content_page

```
---
title: "Pearson v. Callahan"
type: case
citation: "555 U.S. 223 (2009)"
parallel_cite: "129 S. Ct. 808; 172 L. Ed. 2d 565"
neutral_cite: 2009 U.S. LEXIS 591
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2009
date_decided: 2009-01-21
docket: 07-751
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2009-01-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Pearson v. Callahan
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145918/pearson-v-callahan/"
  cluster_id: 145918
  opinion_id: 145918
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Saucier v. Katz]]", "[[Harlow v. Fitzgerald]]", "[[Graham v. Connor]]", "[[Rivas-Villegas v. Cortesluna]]"]
aliases: []
tags: ["case", "qualified-immunity", "section-1983", "saucier-sequence", "clearly-established"]
holding: "The Saucier two-step sequence, while often appropriate, is NO LONGER MANDATORY. Lower courts may exercise discretion over which prong…"
lake:
  record_id: Pearson v. Callahan
  status: verified
  projected_at: 2026-07-06
---

# Pearson v. Callahan

*555 U.S. 223 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers conducted a warrantless search of Callahan's home after an informant completed a controlled drug buy inside (a "consent-once-removed" theory). Callahan sued under § 1983. Applying the then-mandatory two-step sequence of [[Saucier v. Katz]], the Tenth Circuit held the search unconstitutional and the right clearly established, denying [[Qualified Immunity|qualified immunity]].

## Issue
Whether courts must always follow *Saucier*'s rigid two-step sequence — first deciding whether a constitutional violation occurred, then whether the right was clearly established.

## Rule
No. "On reconsidering the procedure required in *Saucier*, we conclude that, while the sequence set forth there is often appropriate, it should no longer be regarded as mandatory. The judges of the district courts and the courts of appeals should be permitted to exercise their sound discretion in deciding which of the two prongs of the qualified immunity analysis should be addressed first in light of the circumstances in the particular case at hand." — 555 U.S. at 236. ^pin-236

## Application
Exercising the discretion it announced, the Court bypassed the merits of the Fourth Amendment question and resolved the case on the "clearly established" prong: because the "consent-once-removed" doctrine had been accepted by two state supreme courts and three federal circuits when the officers acted, they could reasonably have believed their conduct was lawful, so the right was not clearly established and the officers were entitled to [[Qualified Immunity|qualified immunity]].

## Conclusion
The *Saucier* two-step sequence is no longer mandatory; reversing on the clearly-established prong, the Court held the officers were entitled to [[Qualified Immunity|qualified immunity]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Pearson* freed lower courts to address the qualified-immunity prongs in either order; it **limited** [[Saucier v. Katz]] by removing the mandatory sequencing while preserving *Saucier*'s two-part test.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *Pearson v. Callahan*, 555 U.S. 223 (2009) — https://www.courtlistener.com/opinion/145918/pearson-v-callahan/ — pinpoint: 236.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "85177e54d56bf353", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "555 U.S. 223 (2009)", "court": "U.S. Supreme Court", "neutral_cite": "2009 U.S. LEXIS 591", "official_citation_present": true, "parallel_cite": "129 S. Ct. 808; 172 L. Ed. 2d 565", "title": "Pearson v. Callahan", "year": "2009"}}
{"assertion_id": "5751bd90911a26ab", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Saucier two-step sequence, while often appropriate, is NO LONGER MANDATORY. Lower courts may exercise discretion over which prong…", "title": "Pearson v. Callahan"}}
{"assertion_id": "f6427e9295f454ca", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Key — Progeny / Refinement", "title": "Pearson v. Callahan"}}
{"assertion_id": "56f953ba9671d0e3", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Pearson v. Callahan"}}
{"assertion_id": "95613ba89a60638b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2009-01-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Pearson v. Callahan", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Pearson v. Callahan", "varies_by_point": "false"}}
```

### lake record — Pearson v. Callahan

```json
{
  "schema_version": "s2.v1",
  "record_id": "Pearson v. Callahan",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Pearson v. Callahan",
    "case_name_short": "Pearson",
    "case_name_full": "PEARSON Et Al. v. CALLAHAN",
    "input_case_name": "Pearson v. Callahan",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2009-01-21",
    "year": 2009,
    "docket": "07-751",
    "cluster_id": 145918,
    "lead_opinion_id": 145918,
    "sibling_ids": [
      145918
    ],
    "absolute_url": "/opinion/145918/pearson-v-callahan/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "555 U.S. 223",
      "volume": "555",
      "reporter": "U.S.",
      "page": "223",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "129 S. Ct. 808",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "808",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "172 L. Ed. 2d 565",
        "volume": "172",
        "reporter": "L. Ed. 2d",
        "page": "565",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. LEXIS 591",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "591",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "555 U.S. 223",
        "volume": "555",
        "reporter": "U.S.",
        "page": "223",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 S. Ct. 808",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "808",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "172 L. Ed. 2d 565",
        "volume": "172",
        "reporter": "L. Ed. 2d",
        "page": "565",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. LEXIS 591",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "591",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "555 U.S. 223",
    "official_selection": {
      "court_class": "scotus",
      "selected": "555 U.S. 223",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-236",
      "page": null,
      "quote": "theory). Callahan sued under \u00a7 1983. Applying the then-mandatory two-step sequence of [[Saucier v. Katz]], the Tenth Circuit held the search unconstitutional and the right clearly established, denying qualified immunity. ## Issue Whether courts must always follow *Saucier*'s rigid two-step sequence \u2014 first deciding whether a constitutional violation occurred, then whether the right was clearly established. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2009-01-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Pearson v. Callahan",
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
        "journal_ref": "Pearson v. Callahan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ashcroft v. Iqbal",
          "cluster_id": 145875,
          "cite": [
            "173 L. Ed. 2d 868",
            "129 S. Ct. 1937",
            "556 U.S. 662",
            "2009 U.S. LEXIS 3472"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael Lacey v. Joseph Arpaio",
          "cluster_id": 807646,
          "cite": [
            "693 F.3d 896"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
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
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
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
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moss v. U.S. Secret Service",
          "cluster_id": 1450162,
          "cite": [
            "572 F.3d 962",
            "2009 U.S. App. LEXIS 15694",
            "2009 WL 2052985"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walker v. Schult",
          "cluster_id": 868764,
          "cite": [
            "717 F.3d 119",
            "2013 U.S. App. LEXIS 10397",
            "2013 WL 2249159"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Padgett v. Wright",
          "cluster_id": 1345341,
          "cite": [
            "587 F.3d 983",
            "2009 U.S. App. LEXIS 25614",
            "2009 WL 3925042"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ziglar v. Abbasi",
          "cluster_id": 4403804,
          "cite": [
            "582 U.S. 120",
            "2017 U.S. LEXIS 3874",
            "137 S. Ct. 1843",
            "198 L. Ed. 2d 290",
            "26 Fla. L. Weekly Fed. S 655",
            "85 U.S.L.W. 4360",
            "2017 WL 2621317"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reichle v. Howards",
          "cluster_id": 801500,
          "cite": [
            "182 L. Ed. 2d 985",
            "132 S. Ct. 2088",
            "566 U.S. 658",
            "2012 U.S. LEXIS 4132"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
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
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "White v. Pauly",
          "cluster_id": 4374579,
          "cite": [
            "580 U.S. 73",
            "196 L. Ed. 2d 463",
            "2017 U.S. LEXIS 5",
            "137 S. Ct. 548",
            "26 Fla. L. Weekly Fed. S 409",
            "85 U.S.L.W. 4027",
            "2017 WL 69170"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
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
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tracy v. Freshwater",
          "cluster_id": 177179,
          "cite": [
            "623 F.3d 90",
            "2010 U.S. App. LEXIS 21238",
            "2010 WL 4008747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Plumhoff v. Rickard",
          "cluster_id": 2675750,
          "cite": [
            "188 L. Ed. 2d 1056",
            "134 S. Ct. 2012",
            "2014 U.S. LEXIS 3816",
            "82 U.S.L.W. 4394",
            "572 U.S. 765",
            "24 Fla. L. Weekly Fed. S 790",
            "2014 WL 2178335"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Citizens United v. Federal Election Commission",
          "cluster_id": 1741,
          "cite": [
            "175 L. Ed. 2d 753",
            "130 S. Ct. 876",
            "558 U.S. 310",
            "2010 U.S. LEXIS 766",
            "22 Fla. L. Weekly Fed. S 73",
            "78 U.S.L.W. 4078",
            "187 L.R.R.M. (BNA) 2961",
            "159 Lab. Cas. (CCH) 10,166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
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
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramos v. Louisiana",
          "cluster_id": 9231323,
          "cite": [
            "140 S. Ct. 1390",
            "206 L. Ed. 2d 583"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony Martin v. Susan Duffy",
          "cluster_id": 4396964,
          "cite": [
            "858 F.3d 239",
            "2017 WL 2366997"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lucas Burgess v. Gene Fischer",
          "cluster_id": 2641010,
          "cite": [
            "735 F.3d 462",
            "2013 WL 5873323",
            "2013 U.S. App. LEXIS 22279"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
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
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
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
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kisor v. Wilkie",
          "cluster_id": 4632953,
          "cite": [
            "588 U.S. 558",
            "139 S. Ct. 2400",
            "204 L. Ed. 2d 841",
            "2019 U.S. LEXIS 4397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City and County of San Francisco v. Sheehan",
          "cluster_id": 2801435,
          "cite": [
            "575 U.S. 600",
            "135 S. Ct. 1765",
            "191 L. Ed. 2d 856",
            "2015 U.S. LEXIS 3200",
            "83 U.S.L.W. 4303",
            "25 Fla. L. Weekly Fed. S 254"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Atherton v. District of Columbia Office of the Mayor",
          "cluster_id": 187408,
          "cite": [
            "567 F.3d 672",
            "386 U.S. App. D.C. 144",
            "2009 U.S. App. LEXIS 11734",
            "2009 WL 1515373"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145918) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzIzNDIwODAwMDAwJnM9MTAwMzgyNTImdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145918%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(145918)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NzAmcz00Mzg3MjI3JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28145918%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145918)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzM3NTkwNDAwMDAwJnM9MTAzMTk5ODgmdD1vJmQ9MjAyNi0wNy0wNiZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145918%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145918)",
    "indexed_citing_opinions": 3408,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145918,
        "count": 3408,
        "count_source": "search"
      }
    ],
    "citation_count": 14077,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/pearson-v-callahan.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0Nzg2MzYmcz0xMDY0OTA1NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145918%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145918,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 104029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 109680,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 109932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 111481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 112643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 112671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 117958,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 118149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 121169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 131161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 134724,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 136067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 137736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 145669,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 145707,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 145738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 200739,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 481056,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 766110,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 769027,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 769072,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 770728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 771767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 781742,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 783639,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 784028,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 786761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 789303,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 791266,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 792791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 796788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 1190202,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 1384819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 1425860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 1457999,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 2197206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 2337194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 2581092,
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
    "date_created": "2026-07-05T16:40:00Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:40:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:40:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:42:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:40:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Pearson v. Callahan

```
(Slip Opinion)              OCTOBER TERM, 2008                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                   PEARSON ET AL. v. CALLAHAN

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                 THE TENTH CIRCUIT

   No. 07–751.      Argued October 14, 2008—Decided January 21, 2009
After the Utah Court of Appeals vacated respondent’s conviction for
  possession and distribution of drugs, which he sold to an undercover
  informant he had voluntarily admitted into his house, he brought
  this 42 U. S. C. §1983 damages action in federal court, alleging that
  petitioners, the officers who supervised and conducted the war
  rantless search of the premises that led to his arrest after the sale,
  had violated the Fourth Amendment. The District Court granted
  summary judgment in favor of the officers. Noting that other courts
  had adopted the “consent-once-removed” doctrine—which permits a
  warrantless police entry into a home when consent to enter has al
  ready been granted to an undercover officer who has observed con
  traband in plain view—the court concluded that the officers were en
  titled to qualified immunity because they could reasonably have
  believed that the doctrine authorized their conduct. Following the
  procedure mandated in Saucier v. Katz, 533 U. S. 194, the Tenth Cir
  cuit held that petitioners were not entitled to qualified immunity.
  The court disapproved broadening the consent-once-removed doctrine
  to situations in which the person granted initial consent was not an
  undercover officer, but merely an informant. It further held that the
  Fourth Amendment right to be free in one’s home from unreasonable
  searches and arrests was clearly established at the time of respon
  dent’s arrest, and determined that, under this Court’s clearly estab
  lished precedents, warrantless entries into a home are per se unrea
  sonable unless they satisfy one of the two established exceptions for
  consent and exigent circumstances. The court concluded that peti
  tioners could not reasonably have believed that their conduct was
  lawful because they knew that (1) they had no warrant; (2) respon
  dent had not consented to their entry; and (3) his consent to the entry
2                      PEARSON v. CALLAHAN

                                 Syllabus

    of an informant could not reasonably be interpreted to extend to
    them. In granting certiorari, this Court directed the parties to ad
    dress whether Saucier should be overruled in light of widespread
    criticism directed at it.
Held:
    1. The Saucier procedure should not be regarded as an inflexible
 requirement. Pp. 5–19.
       (a) Saucier mandated, see 533 U. S., at 194, a two-step sequence
 for resolving government officials’ qualified immunity claims: A court
 must decide (1) whether the facts alleged or shown by the plaintiff
 make out a violation of a constitutional right, and (2) if so, whether
 that right was “clearly established” at the time of the defendant’s al
 leged misconduct, id., at 201. Qualified immunity applies unless the
 official's conduct violated such a right. Anderson v. Creighton, 483
 U. S. 635, 640. Pp. 5–7.
       (b) Stare decisis does not prevent this Court from determining
 whether the Saucier procedure should be modified or abandoned.
 Revisiting precedent is particularly appropriate where, as here, a de
 parture would not upset settled expectations, see, e.g., United States
 v. Gaudin, 515 U. S. 506, 521; the precedent consists of a rule that is
 judge-made and adopted to improve court operations, not a statute
 promulgated by Congress, see, e.g., State Oil Co. v. Khan, 522 U. S. 3,
 20; and the precedent has “been questioned by Members of th[is]
 Court in later decisions, and [has] defied consistent application by
 the lower courts,” Payne v. Tennessee, 501 U. S. 808, 829–830. Re
 spondent’s argument that Saucier should not be reconsidered unless
 the Court concludes that it was “badly reasoned” or that its rule has
 proved “unworkable,” see Payne, supra, at 827, is rejected. Those
 standards are out of place in the present context, where a consider
 able body of new experience supports a determination that a manda
 tory, two-step rule for resolving all qualified immunity claims should
 not be retained. Pp. 7–10.
       (c) Reconsideration of the Saucier procedure demonstrates that,
 while the sequence set forth therein is often appropriate, it should no
 longer be regarded as mandatory in all cases. Pp. 10–19.
          (i) The Court continues to recognize that the Saucier protocol is
 often beneficial. In some cases, a discussion of why the relevant facts
 do not violate clearly established law may make it apparent that in
 fact the relevant facts do not make out a constitutional violation at
 all. And Saucier was correct in noting that the two-step procedure
 promotes the development of constitutional precedent and is espe
 cially valuable for questions that do not frequently arise in cases in
 which a qualified immunity defense is unavailable. See 533 U. S., at
 194. Pp. 10–11.
                   Cite as: 555 U. S. ____ (2009)                     3

                              Syllabus

        (ii) Nevertheless, experience in this Court and the lower fed
eral courts has pointed out the rigid Saucier procedure’s shortcom
ings. For example, it may result in a substantial expenditure of
scarce judicial resources on difficult questions that have no effect on
the case’s outcome, and waste the parties’ resources by forcing them
to assume the costs of litigating constitutional questions and endure
delays attributable to resolving those questions when the suit other
wise could be disposed of more readily. Moreover, although the
procedure’s first prong is intended to further the development of
constitutional precedent, opinions following that procedure often fail
to make a meaningful contribution to such development. Further,
when qualified immunity is asserted at the pleading stage, the
answer to whether there was a violation may depend on a kalei
doscope of facts not yet fully developed. And the first step may create
a risk of bad decisionmaking, as where the briefing of constitutional
questions is woefully inadequate. Application of the Saucier rule also
may make it hard for affected parties to obtain appellate review of
constitutional decisions having a serious prospective effect on their
operations. For example, where a court holds that a defendant has
committed a constitutional violation, but then holds that the viola
tion was not clearly established, the defendant, as the winning party,
may have his right to appeal the adverse constitutional holding chal
lenged. Because rigid adherence to Saucier departs from the general
rule of constitutional avoidance, cf., e.g., Scott v. Harris, 550 U. S.
372, 388, the Court may appropriately decline to mandate the order
of decision that the lower courts must follow, see, e.g., Strickland v.
Washington, 466 U. S. 668, 697. This flexibility properly reflects the
Court’s respect for the lower federal courts. Because the two-step
Saucier procedure is often, but not always, advantageous, those
judges are in the best position to determine the order of decisionmak
ing that will best facilitate the fair and efficient disposition of each
case. Pp. 11–17.
        (iii) Misgivings concerning today’s decision are unwarranted.
It does not prevent the lower courts from following Saucier; it simply
recognizes that they should have the discretion to decide whether
that procedure is worthwhile in particular cases. Moreover, it will
not retard the development of constitutional law, result in a prolif
eration of damages claims against local governments, or spawn new
litigation over the standards for deciding whether to reach the par
ticular case’s merits. Pp. 17–19.
   2. Petitioners are entitled to qualified immunity because it was not
clearly established at the time of the search that their conduct was
unconstitutional.      When the entry occurred, the consent-once
4                       PEARSON v. CALLAHAN

                                 Syllabus

    removed doctrine had been accepted by two State Supreme Courts
    and three Federal Courts of Appeals, and not one of the latter had is
    sued a contrary decision. Petitioners were entitled to rely on these
    cases, even though their own Federal Circuit had not yet ruled on
    consent-once-removed entries. See Wilson v. Layne, 526 U. S. 603,
    618. Pp. 19–20.
494 F. 3d 891, reversed.

    ALITO, J., delivered the opinion for a unanimous Court.
                       Cite as: 555 U. S. ____ (2009)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 07–751
                                  _________________


CORDELL PEARSON, ET AL., PETITIONERS v. AFTON
               CALLAHAN
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE TENTH CIRCUIT
                              [January 21, 2009]

  JUSTICE ALITO delivered the opinion of the Court.
   This is an action brought by respondent under Rev.
Stat. §1979, 42 U. S. C. §1983, against state law enforce
ment officers who conducted a warrantless search of his
house incident to his arrest for the sale of methampheta
mine to an undercover informant whom he had voluntarily
admitted to the premises. The Court of Appeals held that
petitioners were not entitled to summary judgment on
qualified immunity grounds. Following the procedure we
mandated in Saucier v. Katz, 533 U. S. 194 (2001), the
Court of Appeals held, first, that respondent adduced facts
sufficient to make out a violation of the Fourth Amend
ment and, second, that the unconstitutionality of the
officers’ conduct was clearly established. In granting
review, we required the parties to address the additional
question whether the mandatory procedure set out in
Saucier should be retained.
   We now hold that the Saucier procedure should not be
regarded as an inflexible requirement and that petitioners
are entitled to qualified immunity on the ground that it
was not clearly established at the time of the search that
2                 PEARSON v. CALLAHAN

                    Opinion of the Court

their conduct was unconstitutional. We therefore reverse.
                             I

                            A

  The Central Utah Narcotics Task Force is charged with
investigating illegal drug use and sales. In 2002, Brian
Bartholomew, who became an informant for the task force
after having been charged with the unlawful possession of
methamphetamine, informed Officer Jeffrey Whatcott that
respondent Afton Callahan had arranged to sell Bar
tholomew methamphetamine later that day.
  That evening, Bartholomew arrived at respondent’s
residence at about 8 p.m. Once there, Bartholomew went
inside and confirmed that respondent had methampheta
mine available for sale. Bartholomew then told respon
dent that he needed to obtain money to make his purchase
and left.
  Bartholomew met with members of the task force at
about 9 p.m. and told them that he would be able to buy a
gram of methamphetamine for $100. After concluding
that Bartholomew was capable of completing the planned
purchase, the officers searched him, determined that he
had no controlled substances on his person, gave him a
marked $100 bill and a concealed electronic transmitter to
monitor his conversations, and agreed on a signal that he
would give after completing the purchase.
  The officers drove Bartholomew to respondent’s trailer
home, and respondent’s daughter let him inside. Respon
dent then retrieved a large bag containing methampheta
mine from his freezer and sold Bartholomew a gram of
methamphetamine, which he put into a small plastic bag.
Bartholomew gave the arrest signal to the officers who
were monitoring the conversation, and they entered the
trailer through a porch door. In the enclosed porch, the
officers encountered Bartholomew, respondent, and two
other persons, and they saw respondent drop a plastic bag,
                 Cite as: 555 U. S. ____ (2009)          3

                     Opinion of the Court

which they later determined contained methampheta
mine. The officers then conducted a protective sweep
of the premises. In addition to the large bag of meth-
amphetamine, the officers recovered the marked bill
from respondent and a small bag containing meth-
amphetamine from Bartholomew, and they found drug
syringes in the residence. As a result, respondent was
charged with the unlawful possession and distribution of
methamphetamine.
                              B
  The trial court held that the warrantless arrest and
search were supported by exigent circumstances. On
respondent’s appeal from his conviction, the Utah attorney
general conceded the absence of exigent circumstances,
but urged that the inevitable discovery doctrine justified
introduction of the fruits of the warrantless search. The
Utah Court of Appeals disagreed and vacated respondent’s
conviction. See State v. Callahan, 2004 LIT App. 164, 93
P. 3d 103. Respondent then brought this damages action
under 42 U. S. C. §1983 in the United States District
Court for the District of Utah, alleging that the officers
had violated the Fourth Amendment by entering his home
without a warrant. See Callahan v. Millard Cty., No.
2:04–CV–00952, 2006 WL 1409130 (2006).
  In granting the officers’ motion for summary judgment,
the District Court noted that other courts had adopted the
“consent-once-removed” doctrine, which permits a war
rantless entry by police officers into a home when consent
to enter has already been granted to an undercover officer
or informant who has observed contraband in plain view.
Believing that this doctrine was in tension with our inter
vening decision in Georgia v. Randolph, 547 U. S. 103
(2006), the District Court concluded that “the simplest
approach is to assume that the Supreme Court will ulti
mately reject the [consent-once-removed] doctrine and find
4                 PEARSON v. CALLAHAN

                     Opinion of the Court

that searches such as the one in this case are not reason
able under the Fourth Amendment.” 2006 WL 1409130,
at *8. The Court then held that the officers were entitled
to qualified immunity because they could reasonably have
believed that the consent-once-removed doctrine author
ized their conduct.
   On appeal, a divided panel of the Tenth Circuit held
that petitioners’ conduct violated respondent’s Fourth
Amendment rights. Callahan v. Millard Cty., 494 F. 3d
891, 895–899 (2007). The panel majority stated that “[t]he
‘consent-once-removed’ doctrine applies when an under
cover officer enters a house at the express invitation of
someone with authority to consent, establishes probable
cause to arrest or search, and then immediately summons
other officers for assistance.” Id., at 896. The majority
took no issue with application of the doctrine when the
initial consent was granted to an undercover law enforce
ment officer, but the majority disagreed with decisions
that “broade[n] this doctrine to grant informants the same
capabilities as undercover officers.” Ibid.
   The Tenth Circuit panel further held that the Fourth
Amendment right that it recognized was clearly estab
lished at the time of respondent’s arrest. Id., at 898–899.
“In this case,” the majority stated, “the relevant right is
the right to be free in one’s home from unreasonable
searches and arrests.” Id., at 898. The Court determined
that, under the clearly established precedents of this
Court and the Tenth Circuit, “warrantless entries into a
home are per se unreasonable unless they satisfy the
established exceptions.” Id., at 898–899. In the panel’s
words, “the Supreme Court and the Tenth Circuit have
clearly established that to allow police entry into a home,
the only two exceptions to the warrant requirement are
consent and exigent circumstances.” Id., at 899. Against
that backdrop, the panel concluded, petitioners could not
reasonably have believed that their conduct was lawful
                 Cite as: 555 U. S. ____ (2009)            5

                     Opinion of the Court

because petitioners “knew (1) they had no warrant; (2)
[respondent] had not consented to their entry; and (3)
[respondent’s] consent to the entry of an informant could
not reasonably be interpreted to extend to them.” Ibid.
  In dissent, Judge Kelly argued that “no constitutional
violation occurred in this case” because, by inviting Bar
tholomew into his house and participating in a narcotics
transaction there, respondent had compromised the pri
vacy of the residence and had assumed the risk that Bar
tholomew would reveal their dealings to the police. Id., at
903. Judge Kelly further concluded that, even if petition
ers’ conduct had been unlawful, they were nevertheless
entitled to qualified immunity because the constitutional
right at issue—“the right to be free from the warrantless
entry of police officers into one’s home to effectuate an
arrest after one has granted voluntary, consensual entry
to a confidential informant and undertaken criminal
activity giving rise to probable cause”—was not “clearly
established” at the time of the events in question. Id., at
903–904.
  As noted, the Court of Appeals followed the Saucier
procedure. The Saucier procedure has been criticized by
Members of this Court and by lower court judges, who
have been required to apply the procedure in a great
variety of cases and thus have much firsthand experience
bearing on its advantages and disadvantages. Accord
ingly, in granting certiorari, we directed the parties to
address the question whether Saucier should be overruled.
552 U. S. ___ (2008).
                               II 

                               A

  The doctrine of qualified immunity protects government
officials “from liability for civil damages insofar as their
conduct does not violate clearly established statutory or
constitutional rights of which a reasonable person would
6                  PEARSON v. CALLAHAN

                      Opinion of the Court

have known.” Harlow v. Fitzgerald, 457 U. S. 800, 818
(1982). Qualified immunity balances two important inter
ests—the need to hold public officials accountable when
they exercise power irresponsibly and the need to shield
officials from harassment, distraction, and liability when
they perform their duties reasonably. The protection of
qualified immunity applies regardless of whether the
government official’s error is “a mistake of law, a mistake
of fact, or a mistake based on mixed questions of law and
fact.”    Groh v. Ramirez, 540 U. S. 551, 567 (2004)
(KENNEDY, J., dissenting) (citing Butz v. Economou, 438
U. S. 478, 507 (1978) (noting that qualified immunity
covers “mere mistakes in judgment, whether the mistake
is one of fact or one of law”)).
   Because qualified immunity is “an immunity from suit
rather than a mere defense to liability . . . it is effectively
lost if a case is erroneously permitted to go to trial.”
Mitchell v. Forsyth, 472 U. S. 511, 526 (1985) (emphasis
deleted). Indeed, we have made clear that the “driving
force” behind creation of the qualified immunity doctrine
was a desire to ensure that “ ‘insubstantial claims’ against
government officials [will] be resolved prior to discovery.”
Anderson v. Creighton, 483 U. S. 635, 640, n. 2 (1987).
Accordingly, “we repeatedly have stressed the importance
of resolving immunity questions at the earliest possible
stage in litigation.” Hunter v. Bryant, 502 U. S. 224, 227
(1991) (per curiam).
   In Saucier, 533 U. S. 194, this Court mandated a two
step sequence for resolving government officials’ qualified
immunity claims. First, a court must decide whether the
facts that a plaintiff has alleged (see Fed. Rules Civ. Proc.
12(b)(6), (c)) or shown (see Rules 50, 56) make out a viola
tion of a constitutional right. 533 U. S., at 201. Second, if
the plaintiff has satisfied this first step, the court must
decide whether the right at issue was “clearly established”
at the time of defendant’s alleged misconduct. Ibid.
                 Cite as: 555 U. S. ____ (2009)            7

                     Opinion of the Court

Qualified immunity is applicable unless the official’s
conduct violated a clearly established constitutional right.
Anderson, supra, at 640.
    Our decisions prior to Saucier had held that “the better
approach to resolving cases in which the defense of quali
fied immunity is raised is to determine first whether the
plaintiff has alleged a deprivation of a constitutional right
at all.” County of Sacramento v. Lewis, 523 U. S. 833, 841,
n. 5 (1998). Saucier made that suggestion a mandate. For
the first time, we held that whether “the facts alleged
show the officer’s conduct violated a constitutional right
. . . must be the initial inquiry” in every qualified immu
nity case. 533 U. S., at 20 (emphasis added). Only after
completing this first step, we said, may a court turn to
“the next, sequential step,” namely, “whether the right
was clearly established.” Ibid.
    This two-step procedure, the Saucier Court reasoned, is
necessary to support the Constitution’s “elaboration from
case to case” and to prevent constitutional stagnation.
Ibid. “The law might be deprived of this explanation were
a court simply to skip ahead to the question whether the
law clearly established that the officer's conduct was
unlawful in the circumstances of the case.” Ibid.
                              B
  In considering whether the Saucier procedure should be
modified or abandoned, we must begin with the doctrine of
stare decisis. Stare decisis “promotes the evenhanded,
predictable, and consistent development of legal princi
ples, fosters reliance on judicial decisions, and contributes
to the actual and perceived integrity of the judicial proc
ess.” Payne v. Tennessee, 501 U. S. 808, 827 (1991). Al
though “[w]e approach the reconsideration of [our] deci
sions . . . with the utmost caution,” “[s]tare decisis is not
an inexorable command.” State Oil Co. v. Khan, 522 U. S.
3, 20 (1997) (internal quotation marks omitted). Revisit
8                  PEARSON v. CALLAHAN

                     Opinion of the Court

ing precedent is particularly appropriate where, as here, a
departure would not upset expectations, the precedent
consists of a judge-made rule that was recently adopted to
improve the operation of the courts, and experience has
pointed up the precedent’s shortcomings.
   “Considerations in favor of stare decisis are at their
acme in cases involving property and contract rights,
where reliance interests are involved; the opposite is true
in cases . . . involving procedural and evidentiary rules”
that do not produce such reliance. Payne, supra, at 828
(citations omitted). Like rules governing procedures and
the admission of evidence in the trial courts, Saucier’s
two-step protocol does not affect the way in which parties
order their affairs. Withdrawing from Saucier’s categori
cal rule would not upset settled expectations on anyone’s
part. See United States v. Gaudin, 515 U. S. 506, 521
(1995).
   Nor does this matter implicate “the general presumption
that legislative changes should be left to Congress.” Khan,
supra, at 20. We recognize that “considerations of stare
decisis weigh heavily in the area of statutory construction,
where Congress is free to change this Court’s interpreta
tion of its legislation.” Illinois Brick Co. v. Illinois, 431
U. S. 720, 736 (1977). But the Saucier rule is judge made
and implicates an important matter involving internal
Judicial Branch operations. Any change should come from
this Court, not Congress.
   Respondent argues that the Saucier procedure should
not be reconsidered unless we conclude that its justifica
tion was “badly reasoned” or that the rule has proved to be
“unworkable,” see Payne, supra, at 827, but those stan
dards, which are appropriate when a constitutional or
statutory precedent is challenged, are out of place in the
present context. Because of the basis and the nature of
the Saucier two-step protocol, it is sufficient that we now
have a considerable body of new experience to consider
                  Cite as: 555 U. S. ____ (2009)            9

                      Opinion of the Court

regarding the consequences of requiring adherence to this
inflexible procedure. This experience supports our present
determination that a mandatory, two-step rule for resolv
ing all qualified immunity claims should not be retained.
   Lower court judges, who have had the task of applying
the Saucier rule on a regular basis for the past eight
years, have not been reticent in their criticism of Saucier’s
“rigid order of battle.” See, e.g., Purtell v. Mason, 527
F. 3d 615, 622 (CA7 2008) (“This ‘rigid order of battle’ has
been criticized on practical, procedural, and substantive
grounds”); Leval, Judging Under the Constitution: Dicta
About Dicta, 81 N. Y. U. L. Rev. 1249, 1275, 1277 (2006)
(referring to Saucier’s mandatory two-step framework as
“a new and mischievous rule” that amounts to “a puzzling
misadventure in constitutional dictum”). And application
of the rule has not always been enthusiastic. See Higazy
v. Templeton, 505 F. 3d 161, 179, n. 19 (CA2 2007) (“We do
not reach the issue of whether [plaintiff’s] Sixth Amend
ment rights were violated, because principles of judicial
restraint caution us to avoid reaching constitutional ques
tions when they are unnecessary to the disposition of a
case”); Cherrington v. Skeeter, 344 F. 3d 631, 640 (CA6
2003) (“[I]t ultimately is unnecessary for us to decide
whether the individual Defendants did or did not heed the
Fourth Amendment command . . . because they are enti
tled to qualified immunity in any event”); Pearson v.
Ramos, 237 F. 3d 881, 884 (CA7 2001) (“Whether [the
Saucier] rule is absolute may be doubted”).
   Members of this Court have also voiced criticism of the
Saucier rule. See Morse v. Frederick, 551 U. S. ___, ___
(2007) (slip op., at 8) (BREYER, J., concurring in judgment
in part and dissenting in part) (“I would end the failed
Saucier experiment now”); Bunting v. Mellen, 541 U. S.
1019 (2004) (STEVENS, J., joined by GINSBURG and
BREYER, JJ., respecting denial of certiorari) (criticizing the
“unwise judge-made rule under which courts must decide
10                 PEARSON v. CALLAHAN

                     Opinion of the Court

whether the plaintiff has alleged a constitutional violation
before addressing the question whether the defendant
state actor is entitled to qualified immunity”); Id., at 1025
(SCALIA, J., joined by Rehnquist, C. J., dissenting from
denial of certiorari) (“We should either make clear that
constitutional determinations are not insulated from our
review . . . or else drop any pretense at requiring the
ordering in every case” (emphasis in original)); Brosseau v.
Haugen, 543 U. S. 194, 201–202 (2004) (BREYER, J., joined
by SCALIA and GINSBURG, JJ., concurring) (urging Court
to reconsider Saucier’s “rigid ‘order of battle,’ ” which
“requires courts unnecessarily to decide difficult constitu
tional questions when there is available an easier basis for
the decision (e.g., qualified immunity) that will satisfacto
rily resolve the case before the court”); Saucier, 533 U. S.,
at 210 (GINSBURG, J., concurring in judgment) (“The two
part test today’s decision imposes holds large potential to
confuse”).
   Where a decision has “been questioned by Members of
the Court in later decisions and [has] defied consistent
application by the lower courts,” these factors weigh in
favor of reconsideration. Payne, 501 U. S., at 829–830; see
also Crawford v. Washington, 541 U. S. 36, 60 (2004).
Collectively, the factors we have noted make our present
reevaluation of the Saucier two-step protocol appropriate.
                            III
   On reconsidering the procedure required in Saucier, we
conclude that, while the sequence set forth there is often
appropriate, it should no longer be regarded as manda
tory. The judges of the district courts and the courts of
appeals should be permitted to exercise their sound discre
tion in deciding which of the two prongs of the qualified
immunity analysis should be addressed first in light of the
circumstances in the particular case at hand.
                 Cite as: 555 U. S. ____ (2009) 
         11

                     Opinion of the Court 


                              A

   Although we now hold that the Saucier protocol should
not be regarded as mandatory in all cases, we continue to
recognize that it is often beneficial. For one thing, there
are cases in which there would be little if any conservation
of judicial resources to be had by beginning and ending
with a discussion of the “clearly established” prong. “[I]t
often may be difficult to decide whether a right is clearly
established without deciding precisely what the constitu
tional right happens to be.” Lyons v. Xenia, 417 F. 3d 565,
581 (CA6 2005) (Sutton, J., concurring). In some cases, a
discussion of why the relevant facts do not violate clearly
established law may make it apparent that in fact the
relevant facts do not make out a constitutional violation at
all. In addition, the Saucier Court was certainly correct in
noting that the two-step procedure promotes the develop
ment of constitutional precedent and is especially valu-
able with respect to questions that do not frequently
arise in cases in which a qualified immunity defense is
unavailable.
                              B
   At the same time, however, the rigid Saucier procedure
comes with a price. The procedure sometimes results in a
substantial expenditure of scarce judicial resources on
difficult questions that have no effect on the outcome of
the case. There are cases in which it is plain that a consti
tutional right is not clearly established but far from obvi
ous whether in fact there is such a right. District courts
and courts of appeals with heavy caseloads are often
understandably unenthusiastic about what may seem to
be an essentially academic exercise.
   Unnecessary litigation of constitutional issues also
wastes the parties’ resources. Qualified immunity is “an
immunity from suit rather than a mere defense to liabil
ity.” Mitchell, 472 U. S., at 526 (emphasis deleted). Sau
12                    PEARSON v. CALLAHAN

                         Opinion of the Court

cier’s two-step protocol “disserve[s] the purpose of quali
fied immunity” when it “forces the parties to endure addi
tional burdens of suit—such as the costs of litigating
constitutional questions and delays attributable to resolv
ing them—when the suit otherwise could be disposed of
more readily.” Brief for Nat. Assn. of Criminal Defense
Lawyers as Amicus Curiae 30.
   Although the first prong of the Saucier procedure is
intended to further the development of constitutional
precedent, opinions following that procedure often fail to
make a meaningful contribution to such development. For
one thing, there are cases in which the constitutional
question is so fact-bound that the decision provides little
guidance for future cases. See Scott v. Harris, 550 U. S.
372, 388 (2007) (BREYER, J., concurring) (counseling
against the Saucier two-step protocol where the question
is “so fact dependent that the result will be confusion
rather than clarity”); Buchanan v. Maine, 469 F. 3d 158,
168 (CA1 2006) (“We do not think the law elaboration
purpose will be well served here, where the Fourth
Amendment inquiry involves a reasonableness question
which is highly idiosyncratic and heavily dependent on the
facts”).
   A decision on the underlying constitutional question in a
§1983 damages action or a Bivens v. Six Unknown Fed.
Narcotics Agents, 403 U. S. 388 (1971),1 action may have
scant value when it appears that the question will soon be
decided by a higher court. When presented with a consti
tutional question on which this Court had just granted
certiorari, the Ninth Circuit elected to “bypass Saucier’s
first step and decide only whether [the alleged right] was

——————
  1 See  Harlow v. Fitzgerald, 457 U. S. 800, 818, and n. 30 (1982) (not
ing that the Court’s decisions equate the qualified immunity of state
officials sued under 42 U. S. C. §1983 with the immunity of federal
officers sued directly under the Constitution).
                 Cite as: 555 U. S. ____ (2009)           13

                     Opinion of the Court

clearly established.” Motley v. Parks, 432 F. 3d 1072,
1078, and n. 5 (2005) (en banc). Similar considerations
may come into play when a court of appeals panel con
fronts a constitutional question that is pending before the
court en banc or when a district court encounters a consti
tutional question that is before the court of appeals.
   A constitutional decision resting on an uncertain inter
pretation of state law is also of doubtful precedential
importance. As a result, several courts have identified an
“exception” to the Saucier rule for cases in which resolu
tion of the constitutional question requires clarification of
an ambiguous state statute. Egolf v. Witmer, 526 F. 3d
104, 109–111 (CA3 2008); accord, Tremblay v. McClellan,
350 F. 3d 195, 200 (CA1 2003); Ehrlich v. Glastonbury,
348 F. 3d 48, 57–60 (CA2 2003). Justifying the decision to
grant qualified immunity to the defendant without first
resolving, under Saucier’s first prong, whether the defen
dant’s conduct violated the Constitution, these courts have
observed that Saucier’s “underlying principle” of encourag
ing federal courts to decide unclear legal questions in
order to clarify the law for the future “is not meaningfully
advanced . . . when the definition of constitutional rights
depends on a federal court’s uncertain assumptions about
state law.” Egolf, supra, at 110; accord, Tremblay, supra,
at 200; Ehrlich, supra, at 58.
   When qualified immunity is asserted at the pleading
stage, the precise factual basis for the plaintiff’s claim or
claims may be hard to identify. See Lyons, supra, at 582
(Sutton, J., concurring); Kwai Fun Wong v. United States,
373 F. 3d 952, 957 (CA9 2004); Mollica v. Volker, 229 F. 3d
366, 374 (CA2 2000). Accordingly, several courts have
recognized that the two-step inquiry “is an uncomfortable
exercise where . . . the answer [to] whether there was a
violation may depend on a kaleidoscope of facts not yet
fully developed” and have suggested that “[i]t may be that
Saucier was not strictly intended to cover” this situation.
14                PEARSON v. CALLAHAN

                     Opinion of the Court

Dirrane v. Brookline Police Dept., 315 F. 3d 65, 69–70
(CA1 2002); see also Robinette v. Jones, 476 F. 3d 585, 592,
n. 8 (CA8 2007) (declining to follow Saucier because “the
parties have provided very few facts to define and limit
any holding” on the constitutional question).
   There are circumstances in which the first step of the
Saucier procedure may create a risk of bad decisionmak
ing. The lower courts sometimes encounter cases in which
the briefing of constitutional questions is woefully inade
quate. See Lyons, 417 F. 3d, at 582 (Sutton, J., concur
ring) (noting the “risk that constitutional questions may
be prematurely and incorrectly decided in cases where
they are not well presented”); Mollica, supra, at 374.
   Although the Saucier rule prescribes the sequence in
which the issues must be discussed by a court in its opin
ion, the rule does not—and obviously cannot—specify the
sequence in which judges reach their conclusions in their
own internal thought processes. Thus, there will be cases
in which a court will rather quickly and easily decide that
there was no violation of clearly established law before
turning to the more difficult question whether the relevant
facts make out a constitutional question at all. In such
situations, there is a risk that a court may not devote as
much care as it would in other circumstances to the deci
sion of the constitutional issue. See Horne v. Coughlin,
191 F. 3d, 244, 247 (CA2 1999) (“Judges risk being insuffi
ciently thoughtful and cautious in uttering pronounce
ments that play no role in their adjudication”); Leval
1278–1279.
   Rigid adherence to the Saucier rule may make it hard
for affected parties to obtain appellate review of constitu
tional decisions that may have a serious prospective effect
on their operations. Where a court holds that a defendant
committed a constitutional violation but that the violation
was not clearly established, the defendant may face a
difficult situation. As the winning party, the defendant’s
                      Cite as: 555 U. S. ____ (2009)                    15

                          Opinion of the Court

right to appeal the adverse holding on the constitutional
question may be contested. See Bunting, 541 U. S., at
1025 (SCALIA, J., dissenting from denial of certiorari)
(“The perception of unreviewability undermines adherence
to the sequencing rule we . . . created” in Saucier);2 see
also Kalka v. Hawk, 215 F. 3d 90, 96, n. 9 (CADC 2000)
(noting that “[n]ormally, a party may not appeal from a
favorable judgment” and that the Supreme Court “has
apparently never granted the certiorari petition of a party
who prevailed in the appellate court”). In cases like Bun
ting, the “prevailing” defendant faces an unenviable
choice: “compl[y] with the lower court’s advisory dictum
without opportunity to seek appellate [or certiorari] re
view,” or “def[y] the views of the lower court, adher[e] to
practices that have been declared illegal, and thus invit[e]
new suits” and potential “punitive damages.” Horne,
supra, at 247–248.
   Adherence to Saucier’s two-step protocol departs from
the general rule of constitutional avoidance and runs
counter to the “older, wiser judicial counsel ‘not to pass on
questions of constitutionality . . . unless such adjudication
is unavoidable.’ ” Scott, 550 U. S., at 388 (BREYER, J.,

——————
  2 In Bunting, the Court of Appeals followed the Saucier two-step pro

tocol and first held that the Virginia Military Institute’s use of the word
“God” in a “supper roll call” ceremony violated the Establishment
Clause, but then granted the defendants qualified immunity because
the law was not clearly established at the relevant time. Mellen v.
Bunting, 327 F. 3d 355, 365–376 (CA4 2003), cert. denied, 541 U. S.
1019 (2004). Although they had a judgment in their favor below, the
defendants asked this Court to review the adverse constitutional
ruling. Dissenting from the denial of certiorari, JUSTICE SCALIA, joined
by Chief Justice Rehnquist, criticized “a perceived procedural tangle of
the Court’s own making.” 541 U. S., at 1022. The “tangle” arose from
the Court’s “ ‘settled refusal’ to entertain an appeal by a party on an
issue as to which he prevailed” below, a practice that insulates from
review adverse merits decisions that are “locked inside” favorable
qualified immunity rulings. Id., at 1023, 1024.
16                 PEARSON v. CALLAHAN

                      Opinion of the Court

concurring) (quoting Spector Motor Service, Inc. v.
McLaughlin, 323 U. S. 101, 105 (1944)); see Ashwander v.
TVA, 297 U. S. 288, 347 (1936) (Brandeis, J., concurring)
(“The Court will not pass upon a constitutional question
although properly presented by the record, if there is also
present some other ground upon which the case may be
disposed of ”).
   In other analogous contexts, we have appropriately
declined to mandate the order of decision that the lower
courts must follow. For example, in Strickland v. Wash
ington, 466 U. S. 668 (1984), we recognized a two-part test
for determining whether a criminal defendant was denied
the effective assistance of counsel: The defendant must
demonstrate (1) that his counsel’s performance fell below
what could be expected of a reasonably competent practi
tioner; and (2) that he was prejudiced by that substandard
performance. Id., at 687. After setting forth and applying
the analytical framework that courts must use in evaluat
ing claims of ineffective assistance of counsel, we left it to
the sound discretion of lower courts to determine the order
of decision. Id., at 697 (“Although we have discussed the
performance component of an ineffectiveness claim prior
to the prejudice component, there is no reason for a court
deciding an ineffective assistance claim to approach the
inquiry in the same order or even to address both compo
nents of the inquiry if the defendant makes an insufficient
showing on one”).
   In United States v. Leon, 468 U. S. 897 (1984), we cre
ated an exception to the exclusionary rule when officers
reasonably rely on a facially valid search warrant. Id., at
913. In that context, we recognized that a defendant
challenging a search will lose if either: (1) the warrant
issued was supported by probable cause; or (2) it was not,
but the officers executing it reasonably believed that it
was. Again, after setting forth and applying the analytical
framework that courts must use in evaluating the good
                  Cite as: 555 U. S. ____ (2009)            17

                      Opinion of the Court

faith exception to the Fourth Amendment warrant re
quirement, we left it to the sound discretion of the lower
courts to determine the order of decision. Id., at 924, 925
(“There is no need for courts to adopt the inflexible prac
tice of always deciding whether the officers’ conduct mani
fested objective good faith before turning to the question
whether the Fourth Amendment has been violated”).
   This flexibility properly reflects our respect for the lower
federal courts that bear the brunt of adjudicating these
cases. Because the two-step Saucier procedure is often,
but not always, advantageous, the judges of the district
courts and the courts of appeals are in the best position to
determine the order of decisionmaking will best facilitate
the fair and efficient disposition of each case.
                               C
   Any misgivings concerning our decision to withdraw
from the mandate set forth in Saucier are unwarranted.
Our decision does not prevent the lower courts from fol
lowing the Saucier procedure; it simply recognizes that
those courts should have the discretion to decide whether
that procedure is worthwhile in particular cases. More
over, the development of constitutional law is by no means
entirely dependent on cases in which the defendant may
seek qualified immunity. Most of the constitutional issues
that are presented in §1983 damages actions and Bivens
cases also arise in cases in which that defense is not avail
able, such as criminal cases and §1983 cases against a
municipality, as well as §1983 cases against individuals
where injunctive relief is sought instead of or in addition
to damages. See Lewis, 523 U. S., at 841, n. 5 (noting that
qualified immunity is unavailable “in a suit to enjoin
future conduct, in an action against a municipality, or in
litigating a suppression motion”).
   We also do not think that relaxation of Saucier’s man
date is likely to result in a proliferation of damages claims
18                  PEARSON v. CALLAHAN

                      Opinion of the Court

against local governments. Compare Brief for Nat. Assn.
of Counties et al., as Amici Curiae 29, 30 (“[T]o the extent
that a rule permitting courts to bypass the merits makes it
more difficult for civil rights plaintiffs to pursue novel
claims, they will have greater reason to press custom,
policy, or practice [damages] claims against local govern
ments”). It is hard to see how the Saucier procedure could
have a significant effect on a civil rights plaintiff’s decision
whether to seek damages only from a municipal employee
or also from the municipality. Whether the Saucier proce
dure is mandatory or discretionary, the plaintiff will pre
sumably take into account the possibility that the individ
ual defendant will be held to have qualified immunity, and
presumably the plaintiff will seek damages from the mu
nicipality as well as the individual employee if the benefits
of doing so (any increase in the likelihood of recovery or
collection of damages) outweigh the litigation costs.
   Nor do we think that allowing the lower courts to exer
cise their discretion with respect to the Saucier procedure
will spawn “a new cottage industry of litigation . . . over
the standards for deciding whether to reach the merits in
a given case.” Brief for Nat. Assn. of Counties et al. as
Amici Curiae 29, 30. It does not appear that such a “cot
tage industry” developed prior to Saucier, and we see no
reason why our decision today should produce such a
result.
                             IV
  Turning to the conduct of the officers here, we hold that
petitioners are entitled to qualified immunity because the
entry did not violate clearly established law. An officer
conducting a search is entitled to qualified immunity
where clearly established law does not show that the
search violated the Fourth Amendment. See Anderson,
483 U. S., at 641. This inquiry turns on the “objective
legal reasonableness of the action, assessed in light of the
                  Cite as: 555 U. S. ____ (2009)           19

                      Opinion of the Court

legal rules that were clearly established at the time it was
taken.” Wilson v. Layne, 526 U. S. 603, 614 (1999) (inter
nal quotation marks omitted); see Hope v. Pelzer, 536 U. S.
730, 739 (2002) (“[Q]ualified immunity operates to ensure
that before they are subjected to suit, officers are on notice
their conduct is unlawful” (internal quotation marks
omitted)).
   When the entry at issue here occurred in 2002, the
“consent-once-removed” doctrine had gained acceptance in
the lower courts. This doctrine had been considered by
three Federal Courts of Appeals and two State Supreme
Courts starting in the early 1980’s. See, e.g., United
States v. Diaz, 814 F. 2d 454, 459 (CA7), cert. denied, 484
U. S. 857 (1987); United States v. Bramble, 103 F. 3d 1475
(CA9 1996); United States v. Pollard, 215 F. 3d 643, 648–
649 (CA6), cert. denied, 531 U. S. 999 (2000); State v.
Henry, 133 N. J. 104, 627 A. 2d 125 (1993); State v. Johns
ton, 184 Wis. 2d 794, 518 N. W. 2d 759 (1994). It had been
accepted by every one of those courts. Moreover, the
Seventh Circuit had approved the doctrine’s application to
cases involving consensual entries by private citizens
acting as confidential informants. See United States v.
Paul, 808 F. 2d, 645, 648 (1986). The Sixth Circuit
reached the same conclusion after the events that gave
rise to respondent’s suit, see United States v. Yoon, 398
F. 3d 802, 806–808, cert. denied, 546 U. S. 977 (2005), and
prior to the Tenth Circuit’s decision in the present case, no
court of appeals had issued a contrary decision.
   The officers here were entitled to rely on these cases,
even though their own Federal Circuit had not yet ruled
on “consent-once-removed” entries. The principles of
qualified immunity shield an officer from personal liability
when an officer reasonably believes that his or her conduct
complies with the law. Police officers are entitled to rely
on existing lower court cases without facing personal
liability for their actions. In Wilson, we explained that a
20                 PEARSON v. CALLAHAN

                      Opinion of the Court

Circuit split on the relevant issue had developed after the
events that gave rise to suit and concluded that “[i]f judges
thus disagree on a constitutional question, it is unfair to
subject police to money damages for picking the losing side
of the controversy.” 526 U. S., at 618. Likewise, here,
where the divergence of views on the consent-once
removed doctrine was created by the decision of the Court
of Appeals in this case, it is improper to subject petitioners
to money damages for their conduct.
   Because the unlawfulness of the officers’ conduct in this
case was not clearly established, petitioners are entitled to
qualified immunity. We therefore reverse the judgment of
the Court of Appeals.
                                              It is so ordered.

```

---
