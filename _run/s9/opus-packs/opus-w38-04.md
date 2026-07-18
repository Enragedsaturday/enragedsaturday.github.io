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

## GROUP: content/cases/Michigan Dept. of State Police v. Sitz.md  (`case`, 5 assertions)

### content_page

```
---
title: "Michigan Dept. of State Police v. Sitz"
type: case
citation: "496 U.S. 444 (1990)"
parallel_cite: "110 S. Ct. 2481; 110 L. Ed. 2d 412; 58 U.S.L.W. 4781"
neutral_cite: 1990 U.S. LEXIS 3144
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1990
date_decided: 1990-06-14
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1990-06-14
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Michigan Dept. of State Police v. Sitz
  varies_by_point: false
  scope_note: Distinguished by City of Indianapolis v. Edmond for checkpoints whose primary purpose is general crime control.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112459/michigan-department-of-state-police-v-sitz/"
  cluster_id: 112459
  opinion_id: 9432063
  identity_checked: true
homes:
  - page: "[[Checkpoints and Roadblocks]]"
    role: "Key — Anchor"
related: ["[[City of Indianapolis v. Edmond]]", "[[Delaware v. Prouse]]", "[[Camara v. Municipal Court]]"]
aliases: ["Michigan Department of State Police v. Sitz"]
tags: ["case", "fourth-amendment", "checkpoint", "special-needs", "dui", "seizure"]
holding: "Suspicionless sobriety (DUI) checkpoints are constitutional; the state's interest in combating drunk driving and the checkpoint's…"
lake:
  record_id: Michigan Dept. of State Police v. Sitz
  status: verified
  projected_at: 2026-07-06
---

# Michigan Dept. of State Police v. Sitz

*496 U.S. 444 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
The Michigan State Police operated a highway sobriety-checkpoint program under which all passing cars were briefly stopped and drivers showing signs of intoxication were directed aside for field sobriety testing. Licensed Michigan drivers challenged the suspicionless stops as a violation of the Fourth Amendment, and the state courts held the program unconstitutional.

## Issue
Whether a State's use of suspicionless highway sobriety checkpoints to detect and deter drunk driving violates the Fourth Amendment.

## Rule
No. Weighing the State's interest, the program's effectiveness, and the intrusion on motorists: "In sum, the balance of the State's interest in preventing drunken driving, the extent to which this system can reasonably be said to advance that interest, and the degree of intrusion upon individual motorists who are briefly stopped, weighs in favor of the state program. We therefore hold that it is consistent with the Fourth Amendment." — 496 U.S. at 455. ^pin-455

## Application
The brief checkpoint stop was a Fourth Amendment seizure, but Michigan's substantial interest in combating drunk driving, the empirical support for checkpoints, and the slight, standardized intrusion on each briefly stopped motorist made the program reasonable. No individualized suspicion was required for the initial stop.

## Conclusion
Reversed; the suspicionless sobriety-checkpoint program is consistent with the Fourth Amendment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Sitz* remains good law for sobriety checkpoints but is **distinguished by** [[City of Indianapolis v. Edmond]], which held unconstitutional checkpoints whose **primary purpose** is detecting ordinary criminal wrongdoing (general crime control) rather than highway safety.

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *Michigan Dept. of State Police v. Sitz*, 496 U.S. 444 (1990) — https://www.courtlistener.com/opinion/112459/michigan-department-of-state-police-v-sitz/ — pinpoint: 455.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "afca0085b13129cf", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "496 U.S. 444 (1990)", "court": "U.S. Supreme Court", "neutral_cite": "1990 U.S. LEXIS 3144", "official_citation_present": true, "parallel_cite": "110 S. Ct. 2481; 110 L. Ed. 2d 412; 58 U.S.L.W. 4781", "title": "Michigan Dept. of State Police v. Sitz", "year": "1990"}}
{"assertion_id": "a18a3e23d807f64b", "dimension": "support", "kind": "home_role", "locator": {"home": "Checkpoints and Roadblocks"}, "payload": {"home": "Checkpoints and Roadblocks", "role": "Key — Anchor", "title": "Michigan Dept. of State Police v. Sitz"}}
{"assertion_id": "f3e68dd326155815", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Suspicionless sobriety (DUI) checkpoints are constitutional; the state's interest in combating drunk driving and the checkpoint's…", "title": "Michigan Dept. of State Police v. Sitz"}}
{"assertion_id": "371db5e3bc3605df", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1990-06-14", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Michigan Dept. of State Police v. Sitz", "field_i_validity": "good_law", "scope_note": "Distinguished by City of Indianapolis v. Edmond for checkpoints whose primary purpose is general crime control.", "title": "Michigan Dept. of State Police v. Sitz", "varies_by_point": "false"}}
{"assertion_id": "4599be637eda5cb5", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Michigan Dept. of State Police v. Sitz"}}
```

### lake record — Michigan Dept. of State Police v. Sitz

```json
{
  "schema_version": "s2.v1",
  "record_id": "Michigan Dept. of State Police v. Sitz",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Michigan Department of State Police v. Sitz",
    "case_name_short": "Sitz",
    "case_name_full": "MICHIGAN DEPARTMENT OF STATE POLICE Et Al. v. SITZ Et Al.",
    "input_case_name": "Michigan Dept. of State Police v. Sitz",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-06-14",
    "year": 1990,
    "docket": null,
    "cluster_id": 112459,
    "lead_opinion_id": 9432063,
    "sibling_ids": [
      112459,
      9432063,
      9432064,
      9432065,
      9432066
    ],
    "absolute_url": "/opinion/112459/michigan-department-of-state-police-v-sitz/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "496 U.S. 444",
      "volume": "496",
      "reporter": "U.S.",
      "page": "444",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "110 S. Ct. 2481",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "2481",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 L. Ed. 2d 412",
        "volume": "110",
        "reporter": "L. Ed. 2d",
        "page": "412",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 U.S.L.W. 4781",
        "volume": "58",
        "reporter": "U.S.L.W.",
        "page": "4781",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 3144",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "3144",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "496 U.S. 444",
        "volume": "496",
        "reporter": "U.S.",
        "page": "444",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 S. Ct. 2481",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "2481",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 L. Ed. 2d 412",
        "volume": "110",
        "reporter": "L. Ed. 2d",
        "page": "412",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 3144",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "3144",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 U.S.L.W. 4781",
        "volume": "58",
        "reporter": "U.S.L.W.",
        "page": "4781",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "496 U.S. 444",
    "official_selection": {
      "court_class": "scotus",
      "selected": "496 U.S. 444",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-455",
      "page": null,
      "quote": "--- # Michigan Dept. of State Police v. Sitz *496 U.S. 444 (1990)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background The Michigan State Police operated a highway sobriety-checkpoint program under which all passing cars were briefly stopped and drivers showing signs of intoxication were directed aside for field sobriety testing. Licensed Michigan drivers challenged the suspicionless stops as a violation of the Fourth Amendment, and the state courts held the program unconstitutional. ## Issue Whether a State's use of suspicionless highway sobriety checkpoints to detect and deter drunk driving violates the Fourth Amendment. ## Rule No. Weighing the State's interest, the program's effectiveness, and the intrusion on motorists:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1990-06-14",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Michigan Dept. of State Police v. Sitz",
    "varies_by_point": false,
    "scope_note": "Distinguished by City of Indianapolis v. Edmond for checkpoints whose primary purpose is general crime control.",
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane1_negative"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane1_negative"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane1_negative"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane1_negative"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Rodriguez",
          "cluster_id": 2969172,
          "cite": [
            "472 Mass. 767",
            "37 N.E.3d 611"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jonathan Albert Leal v. State",
          "cluster_id": 2751234,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane1_negative"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane1_negative"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Williams",
          "cluster_id": 3997962,
          "cite": [
            "909 N.E.2d 667",
            "181 Ohio App. 3d 472",
            "2009 Ohio 970"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane1_negative"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane1_negative"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vernonia School District 47J v. Acton",
          "cluster_id": 117964,
          "cite": [
            "132 L. Ed. 2d 564",
            "115 S. Ct. 2386",
            "515 U.S. 646",
            "1995 U.S. LEXIS 4275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Begay v. United States",
          "cluster_id": 145815,
          "cite": [
            "170 L. Ed. 2d 490",
            "128 S. Ct. 1581",
            "553 U.S. 137",
            "2008 U.S. LEXIS 3474"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cook",
          "cluster_id": 1628034,
          "cite": [
            "674 So. 2d 957",
            "1996 WL 292130"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe v. Poritz",
          "cluster_id": 1473573,
          "cite": [
            "662 A.2d 367",
            "142 N.J. 1",
            "36 A.L.R. 5th 711",
            "1995 N.J. LEXIS 519"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Alvarez",
          "cluster_id": 1160457,
          "cite": [
            "14 Cal. 4th 155",
            "926 P.2d 365",
            "96 Cal. Daily Op. Serv. 8805",
            "58 Cal. Rptr. 2d 385",
            "96 Daily Journal DAR 14567",
            "1996 Cal. LEXIS 6514"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chandler v. Miller",
          "cluster_id": 118100,
          "cite": [
            "137 L. Ed. 2d 513",
            "117 S. Ct. 1295",
            "520 U.S. 305",
            "1997 U.S. LEXIS 2505"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chew v. Gates",
          "cluster_id": 7029311,
          "cite": [
            "27 F.3d 1432",
            "94 Cal. Daily Op. Serv. 4853",
            "94 Daily Journal DAR 9043",
            "1994 U.S. App. LEXIS 16020",
            "1994 WL 280292"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cyril Korte v. HHS",
          "cluster_id": 2709178,
          "cite": [
            "735 F.3d 654",
            "2013 WL 5960692"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jordan v. Gardner",
          "cluster_id": 601474,
          "cite": [
            "986 F.2d 1521",
            "93 Cal. Daily Op. Serv. 1354",
            "1993 U.S. App. LEXIS 3065",
            "1993 WL 46630"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Carlson",
          "cluster_id": 4012041,
          "cite": [
            "657 N.E.2d 591",
            "102 Ohio App. 3d 585",
            "1995 Ohio App. LEXIS 1642"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
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
        "journal_ref": "Michigan Dept. of State Police v. Sitz:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112459 OR 9432063 OR 9432064 OR 9432065 OR 9432066) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTg3MzA4ODAwMDAwJnM9MTA1Nzg0NyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112459+OR+9432063+OR+9432064+OR+9432065+OR+9432066%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 12,
        "triage_snippet_classified": 188
      },
      "lane2_top_cited": {
        "query": "cites:(112459 OR 9432063 OR 9432064 OR 9432065 OR 9432066)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xODUmcz01ODI1NjQmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112459+OR+9432063+OR+9432064+OR+9432065+OR+9432066%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112459 OR 9432063 OR 9432064 OR 9432065 OR 9432066)",
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
    "complete_query": "cites:(112459 OR 9432063 OR 9432064 OR 9432065 OR 9432066)",
    "indexed_citing_opinions": 812,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112459,
        "count": 735,
        "count_source": "search"
      },
      {
        "opinion_id": 9432063,
        "count": 102,
        "count_source": "search"
      },
      {
        "opinion_id": 9432064,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9432065,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9432066,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1275,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/michigan-dept-of-state-police-v-sitz.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc3NjkyNzYmcz02NDcyOTkxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112459+OR+9432063+OR+9432064+OR+9432065+OR+9432066%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112459,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 105456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 108223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 108282,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 108350,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 109510,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 110832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 111252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 111504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 112218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 112220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 1259470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 1845032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 2038264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 2102798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 2234088,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 2604190,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112459,
        "cited_id": 2618916,
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
    "date_created": "2026-07-05T13:09:17Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:09:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:09:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:12:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:09:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Michigan Dept. of State Police v. Sitz

```
<opinion type="majority">
<author id="b489-4"><page-number citation-index="1" label="447">*447</page-number>Chief Justice Rehnquist</author>
<p id="A-q">delivered the opinion of the Court.</p>
<p id="b489-5">This case poses the question whether a State’s use of highway sobriety checkpoints violates the Fourth and Fourteenth Amendments to the United States Constitution. We hold that it does not and therefore reverse the contrary holding of the Court of Appeals of Michigan.</p>
<p id="b489-6">Petitioners, the Michigan Department of State Police and its director, established a sobriety checkpoint pilot program in early 1986. The director appointed a Sobriety Checkpoint Advisory Committee comprising representatives of the State Police force, local police forces, state prosecutors, and the University of Michigan Transportation Research Institute. Pursuant to its charge, the advisory committee created guidelines setting forth procedures governing checkpoint operations, site selection, and publicity.</p>
<p id="b489-7">Under the guidelines, checkpoints would be set up at selected sites along state roads. All vehicles passing through a checkpoint would be stopped and their drivers briefly examined for signs of intoxication. In cases where a checkpoint officer detected signs of intoxication, the motorist would be directed to a location out of the traffic flow where an officer would check the motorist’s driver’s license and car registration and, if warranted, conduct further sobriety tests. Should the field tests and the officer’s observations suggest that the driver was intoxicated, an arrest would be made. All other drivers would be permitted to resume their journey immediately.</p>
<p id="b490-4"><page-number citation-index="1" label="448">*448</page-number>The first—and to date the only—sobriety checkpoint operated under the program was conducted in Saginaw County with the assistance of the Saginaw County Sheriff’s Department. During the 75-minute duration of the checkpoint’s operation, 126 vehicles passed through the checkpoint. The average delay for each vehicle was approximately 25 seconds. Two drivers were detained for field sobriety testing, and one of the two was arrested for driving under the influence of alcohol. A third driver who drove through without stopping was pulled over by an officer in an observation vehicle and arrested for driving under the influence.</p>
<p id="b490-5">On the day before the operation of the Saginaw County checkpoint, respondents filed a complaint in the Circuit Court of Wayne County seeking declaratory and injunctive relief from potential subjection to the checkpoints. Each of the respondents “is a licensed driver in the State of Michigan . . . who regularly travels throughout the State in his automobile.” See Complaint, App. 3a-4a. During pretrial proceedings, petitioners agreed to delay further implementation of the checkpoint program pending the outcome of this litigation.</p>
<p id="b490-6">After the trial, at which the court heard extensive testimony concerning, <em>inter alia, </em>the “effectiveness” of highway sobriety checkpoint programs, the court ruled that the Michigan program violated the Fourth Amendment and Art. 1, § 11, of the Michigan Constitution. App. to Pet. for Cert. 132a. On appeal, the Michigan Court of Appeals affirmed the holding that the program violated the Fourth Amendment and, for that reason, did not consider whether the program violated the Michigan Constitution. <span class="citation" data-id="1845032"><a href="/opinion/1845032/sitz-v-department-of-state-police/#445" aria-description="Citation for case: Sitz v. Department of State Police">170 Mich. App. 433, 445</a></span>, <span class="citation" data-id="1845032"><a href="/opinion/1845032/sitz-v-department-of-state-police/#185" aria-description="Citation for case: Sitz v. Department of State Police">429 N. W. 2d 180, 185</a></span> (1988). After the Michigan Supreme Court denied petitioners’ application for leave to appeal, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./493/806/">493 U. S. 806</a></span> (1989).</p>
<p id="b490-7">To decide this case the trial court performed a balancing test derived from our opinion in <em>Brown </em>v. <em>Texas, </em><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">443 U. S. 47</a></span> (1979). As described by the Court of Appeals, the test in<page-number citation-index="1" label="449">*449</page-number>volved “balancing the state’s interest in preventing accidents caused by drunk drivers, the effectiveness of sobriety checkpoints in achieving that goal, and the level of intrusion on an individual’s privacy caused by the checkpoints.” <span class="citation" data-id="1845032"><a href="/opinion/1845032/sitz-v-department-of-state-police/#439" aria-description="Citation for case: Sitz v. Department of State Police">170 Mich. App., at 439</a></span>, <span class="citation" data-id="1845032"><a href="/opinion/1845032/sitz-v-department-of-state-police/" aria-description="Citation for case: Sitz v. Department of State Police">429 N. W. 2d, at 182</a></span> (citing <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#50" aria-description="Citation for case: Brown v. Texas"><em>Brown, supra, </em>at 50-51</a></span>). The Court of Appeals agreed that “the <em><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Brown</a></span> </em>three-prong balancing test was the correct test to be used to determine the constitutionality of the sobriety checkpoint plan.” <span class="citation" data-id="1845032"><a href="/opinion/1845032/sitz-v-department-of-state-police/#439" aria-description="Citation for case: Sitz v. Department of State Police">170 Mich. App., at 439</a></span>, <span class="citation" data-id="1845032"><a href="/opinion/1845032/sitz-v-department-of-state-police/#182" aria-description="Citation for case: Sitz v. Department of State Police">429 N. W. 2d, at 182</a></span>.</p>
<p id="b491-4">As characterized by the Court of Appeals, the trial court’s findings with respect to the balancing factors were that the State has “a grave and legitimate” interest in curbing drunken driving; that sobriety checkpoint programs are generally “ineffective” and, therefore, do not significantly further that interest; and that the checkpoints’ “subjective intrusion” on individual liberties is substantial. <span class="citation" data-id="1845032"><a href="/opinion/1845032/sitz-v-department-of-state-police/#439" aria-description="Citation for case: Sitz v. Department of State Police"><em>Id., </em>at 439, 440</a></span>, <span class="citation" data-id="1845032"><a href="/opinion/1845032/sitz-v-department-of-state-police/#183" aria-description="Citation for case: Sitz v. Department of State Police">429 N. W. 2d, at 183, 184</a></span>. According to the court, the record disclosed no basis for disturbing the trial court’s findings, which were made within the context of an analytical framework prescribed by this Court for determining the constitutionality of seizures less intrusive than traditional arrests. <span class="citation" data-id="1845032"><a href="/opinion/1845032/sitz-v-department-of-state-police/#445" aria-description="Citation for case: Sitz v. Department of State Police"><em>Id., </em>at 445</a></span>, <span class="citation" data-id="1845032"><a href="/opinion/1845032/sitz-v-department-of-state-police/#185" aria-description="Citation for case: Sitz v. Department of State Police">429 N. W. 2d, at 185</a></span>.</p>
<p id="b491-5">In this Court respondents seek to defend the judgment in their favor by insisting that the balancing test derived from <em>Brown </em>v. <em><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Texas, supra,</a></span> </em>was not the proper method of analysis. Respondents maintain that the analysis must proceed from a basis of probable cause or reasonable suspicion, and rely for support on language from our decision last Term in <em>Treasury Employees </em>v. <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656</a></span> (1989). We said in <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span>:</em></p>
<blockquote id="b491-6">“[W]here a Fourth Amendment intrusion serves special governmental needs, beyond the normal need for law enforcement, it is necessary to balance the individual’s privacy expectations against the Government’s interests to determine whether it is impractical to require a warrant <page-number citation-index="1" label="450">*450</page-number>or some level of individualized suspicion in the particular context.” <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#665" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><em>Id., </em>at 665-666</a></span>.</blockquote>
<p id="b492-5">Respondents argue that there must be a showing of some special governmental need “beyond the normal need” for criminal law enforcement before a balancing analysis is appropriate, and that petitioners have demonstrated no such special need.</p>
<p id="b492-6">But it is perfectly plain from a reading of <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span>, </em>which cited and discussed with approval our earlier decision in <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976), that it was in no way designed to repudiate our prior cases dealing with police stops of motorists on public highways. <em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte, supra,</a></span> </em>which utilized a balancing analysis in approving highway checkpoints for detecting illegal aliens, and <em>Brown </em>v. <em><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Texas, supra,</a></span> </em>are the relevant authorities here.</p>
<p id="b492-7">Petitioners concede, correctly in our view, that a Fourth Amendment “seizure” occurs when a vehicle is stopped at a checkpoint. Tr. of Oral Arg. 11; see <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte"><em>Martinez-Fuerte, supra, </em>at 556</a></span> (“It is agreed that checkpoint stops are ‘seizures’ within the meaning of the Fourth Amendment”); <em>Brower </em>v. <em>County of Inyo, </em><span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/#597" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo">489 U. S. 593, 597</a></span> (1989) (Fourth Amendment seizure occurs “when there is a governmental termination of freedom of movement <em>through means intentionally applied” </em>(emphasis in original)). The question thus becomes whether such seizures are “reasonable” under the Fourth Amendment.</p>
<p id="b492-8">It is important to recognize what our inquiry is <em>not </em>about. No allegations are before us of unreasonable treatment of any person after an actual detention at a particular checkpoint. See <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#559" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 559</a></span> (“[C]laim that a particular exercise of discretion in locating or operating a checkpoint is unreasonable is subject to post-stop judicial review”). As pursued in the lower courts, the instant action challenges only the use of sobriety checkpoints generally. We address only the initial stop of each motorist passing through a checkpoint and the associated preliminary questioning and ob<page-number citation-index="1" label="451">*451</page-number>servation by checkpoint officers. Detention of particular motorists for more extensive field sobriety testing may require satisfaction of an individualized suspicion standard. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#567" aria-description="Citation for case: United States v. Martinez-Fuerte"><em>Id., </em>at 567</a></span>.</p>
<p id="b493-5">No one can seriously dispute the magnitude of the drunken driving problem or the States’ interest in eradicating it. Media reports of alcohol-related death and mutilation on the Nation’s roads are legion. The anecdotal is confirmed by the statistical. “Drunk drivers cause an annual death toll of over 25,000 [ <footnotemark>*</footnotemark> ] and in the same time span cause nearly one million personal injuries and more than five billion dollars in property damage.” 4 W. LaFave, Search and Seizure: A Treatise on the Fourth Amendment § 10.8(d), p. 71 (2d ed. 1987). For decades, this Court has “repeatedly lamented the tragedy.” <em>South Dakota </em>v. <em>Neville, </em><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/#558" aria-description="Citation for case: South Dakota v. Neville">459 U. S. 553, 558</a></span> (1983); see <em>Breithaupt </em>v. <em>Abram, </em><span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#439" aria-description="Citation for case: Breithaupt v. Abram">352 U. S. 432, 439</a></span> (1957) (“The increasing slaughter on our highways . . . now reaches the astounding figures only heard of on the battlefield”).</p>
<p id="b493-6">Conversely, the weight bearing on the other scale—the measure of the intrusion on motorists stopped briefly at sobriety checkpoints—is slight. We reached a similar conclusion as to the intrusion on motorists subjected to a brief stop at a highway checkpoint for detecting illegal aliens. See <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#558" aria-description="Citation for case: United States v. Martinez-Fuerte"><em>Martinez-Fuerte, supra, </em>at 558</a></span>. We see virtually no difference between the levels of intrusion on law-abiding motorists <page-number citation-index="1" label="452">*452</page-number>from the brief stops necessary to the effectuation of these two types of checkpoints, which to the average motorist would seem identical save for the nature of the questions the checkpoint officers might ask. The trial court and the Court of Appeals, thus, accurately gauged the “objective” intrusion, measured by the duration of the seizure and the intensity of the investigation, as minimal. See <span class="citation" data-id="1845032"><a href="/opinion/1845032/sitz-v-department-of-state-police/#444" aria-description="Citation for case: Sitz v. Department of State Police">170 Mich. App., at 444</a></span>, <span class="citation" data-id="1845032"><a href="/opinion/1845032/sitz-v-department-of-state-police/#184" aria-description="Citation for case: Sitz v. Department of State Police">429 N. W. 2d, at 184</a></span>.</p>
<p id="b494-5">With respect to what it perceived to be the “subjective” intrusion on motorists, however, the Court of Appeals found such intrusion substantial. See <em>supra, </em>at 449. The court first affirmed the trial court's finding that the guidelines governing checkpoint operation minimize the discretion of the officers on the scene. But the court also agreed with the trial court’s conclusion that the checkpoints have the potential to generate fear and surprise in motorists. This was so because the record failed to demonstrate that approaching motorists would be aware of their option to make U-turns or turnoffs to avoid the checkpoints. On that basis, the court deemed the subjective intrusion from the checkpoints unreasonable. <em>Id., </em>at 443-444, <span class="citation" data-id="1845032"><a href="/opinion/1845032/sitz-v-department-of-state-police/#184" aria-description="Citation for case: Sitz v. Department of State Police">429 N. W. 2d, at 184-185</a></span>.</p>
<p id="b494-6">We believe the Michigan courts misread our cases concerning the degree of “subjective intrusion” and the potential for generating fear and surprise. The “fear and surprise” to be considered are not the natural fear of one who has been drinking over the prospect of being stopped at a sobriety checkpoint but, rather, the fear and surprise engendered in law-abiding motorists by the nature of the stop. This was made clear in <em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>. </em>Comparing checkpoint stops to roving patrol stops considered in prior cases, we said:</p>
<blockquote id="b494-7">“[W]e view checkpoint stops in a different light because the subjective intrusion—the generating of concern or even fright on the part of lawful travelers—is appreciably less in the case of a checkpoint stop. In <em>[United States </em>v.] <em>Ortiz, </em>[<span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891</a></span> (1975),] we noted:</blockquote>
<blockquote id="b495-4"><page-number citation-index="1" label="453">*453</page-number>“‘[T]he circumstances surrounding a checkpoint stop and search are far less intrusive than those attending a roving-patrol stop. Roving patrols often operate at night on seldom-traveled roads, and their approach may frighten motorists. At traffic checkpoints the motorist can see that other vehicles are being stopped, he can see visible signs of the officers’ authority, and he is much less likely to be frightened or annoyed by the intrusion. <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#894" aria-description="Citation for case: United States v. Ortiz">422 U. S., at 894-895</a></span>.’” <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#558" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 558</a></span>.</blockquote>
<p id="b495-5">See also <em>id, </em>at 559. Here, checkpoints are selected pursuant to the guidelines, and uniformed police officers stop every approaching vehicle. The intrusion resulting from the brief stop at the sobriety checkpoint is for constitutional purposes indistinguishable from the checkpoint stops we upheld in <em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>.</em></p>
<p id="b495-6">The Court of Appeals went on to consider as part of the balancing analysis the “effectiveness” of the proposed checkpoint program. Based on extensive testimony in the trial record, the court concluded that the checkpoint program failed the “effectiveness” part of the test, and that this failure materially discounted petitioners’ strong interest in implementing the program. We think the Court of Appeals was wrong on this point as well.</p>
<p id="b495-7">The actual language from <em>Brown </em>v. <em><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Texas</a></span>, </em>upon which the Michigan courts based their evaluation of “effectiveness,” describes the balancing factor as “the degree to which the seizure advances the public interest.” <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas">443 U. S., at 51</a></span>. This passage from <em><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Brown</a></span> </em>was not meant to transfer from politically accountable officials to the courts the decision as to which among reasonable alternative law enforcement techniques should be employed to deal with a serious public danger. Experts in police science might disagree over which of several methods of apprehending drunken drivers is preferrable as an ideal. But for purposes of Fourth Amendment analysis, the choice among such reasonable alternatives <page-number citation-index="1" label="454">*454</page-number>remains with the governmental officials who have a unique understanding of, and a responsibility for, limited public resources, including a finite number of police officers. Brown’s rather general reference to “the degree to which the seizure advances the public interest” was derived, as the opinion makes clear, from the line of cases culminating in <em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte, supra.</a></span> </em>Neither <em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span> </em>nor <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648</a></span> (1979), however, the two cases cited by the Court of Appeals as providing the basis for its “effectiveness” review, see <span class="citation" data-id="1845032"><a href="/opinion/1845032/sitz-v-department-of-state-police/#442" aria-description="Citation for case: Sitz v. Department of State Police">170 Mich. App., at 442</a></span>, <span class="citation" data-id="1845032"><a href="/opinion/1845032/sitz-v-department-of-state-police/#183" aria-description="Citation for case: Sitz v. Department of State Police">429 N. W. 2d, at 183</a></span>, supports the searching examination of “effectiveness” undertaken by the Michigan court.</p>
<p id="b496-5">In <em>Delaware </em>v. <em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse, supra,</a></span> </em>we disapproved random stops made by Delaware Highway Patrol officers in an effort to apprehend unlicensed drivers and unsafe vehicles. We observed that <em>no </em>empirical evidence indicated that such stops would be an effective means of promoting roadway safety and said that “[i]t seems common sense that the percentage of all drivers on the road who are driving without a license is very small and that the number of licensed drivers who will be stopped in order to find one unlicensed operator will be large indeed.” <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#659" aria-description="Citation for case: Delaware v. Prouse"><em>Id., </em>at 659-660</a></span>. We observed that the random stops involved the “kind of standardless and unconstrained discretion [which] is the evil the Court has discerned when in previous cases it has insisted that the discretion of the official in the field be circumscribed, at least to some extent.” <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#661" aria-description="Citation for case: Delaware v. Prouse"><em>Id., </em>at 661</a></span>. We went on to state that our holding did not “cast doubt on the permissibility of roadside truck weigh-stations and inspection checkpoints, at which some vehicles may be subject to further detention for safety and regulatory inspection than are others.” <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse"><em>Id., </em>at 663, n. 26</a></span>.</p>
<p id="b496-6">Unlike <em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span>, </em>this case involves neither a complete absence of empirical data nor a challenge to random highway stops. During the operation of the Saginaw County checkpoint, the detention of the 126 vehicles that entered the checkpoint resulted in the arrest of two drunken drivers. <page-number citation-index="1" label="455">*455</page-number>Stated as a percentage, approximately 1.6 percent of the drivers passing through the checkpoint were arrested for alcohol impairment. In addition, an expert witness testified at the trial that experience in other States demonstrated that, on the whole, sobriety checkpoints resulted in drunken driving arrests of around 1 percent of all motorists stopped. <span class="citation" data-id="1845032"><a href="/opinion/1845032/sitz-v-department-of-state-police/#441" aria-description="Citation for case: Sitz v. Department of State Police">170 Mich. App., at 441</a></span>, <span class="citation" data-id="1845032"><a href="/opinion/1845032/sitz-v-department-of-state-police/#183" aria-description="Citation for case: Sitz v. Department of State Police">429 N. W. 2d, at 183</a></span>. By way of comparison, the record from one of the consolidated cases in <em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span> </em>showed that in the associated checkpoint, illegal aliens were found in only 0.12 percent of the vehicles passing through the checkpoint. See <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#554" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 554</a></span>. The ratio of illegal aliens detected to vehicles stopped (considering that on occasion two or more illegal aliens were found in a single vehicle) was approximately 0.5 percent. See <em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">ibid.</a></span> </em>We concluded that this “record . . . provides a rather complete picture of the effectiveness of the San Clemente checkpoint,” ibid., and we sustained its constitutionality. We see no justification for a different conclusion here.</p>
<p id="b497-5">In sum, the balance of the State’s interest in preventing drunken driving, the extent to which this system can reasonably be said to advance that interest, and the degree of intrusion upon individual motorists who are briefly stopped, weighs in favor of the state program. We therefore hold that it is consistent with the Fourth Amendment. The judgment of the Michigan Court of Appeals is accordingly reversed, and the cause is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b497-6">
<em>It is so ordered.</em>
</p>
<footnote label="*">
<p id="b493-7">Statistical evidence incorporated in Justice Stevens’ dissent suggests that this figure declined between 1982 and 1988. See <em>post, </em>at 460-461, n. 2, and 467-468, n. 7 (citing U. S. Dept, of Transportation, National Highway Traffic Safety Administration, Fatal Accident Reporting System 1988). It was during this same period that police departments experimented with sobriety checkpoint systems. Petitioners, for instance, operated their checkpoint in May 1986, see App. to Pet. for Cert. 6a, and the Maryland State Police checkpoint program, about which much testimony was given before the trial court, began in December 1982. See <em>id, </em>at 84a. Indeed, it is quite possible that jurisdictions which have recently decided to implement sobriety checkpoint systems have relied on such data from the 1980’s in assessing the likely utility of such checkpoints.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Michigan v. Summers.md  (`case`, 6 assertions)

### content_page

```
---
title: "Michigan v. Summers"
type: case
citation: "452 U.S. 692 (1981)"
parallel_cite: "101 S. Ct. 2587; 69 L. Ed. 2d 340; 49 U.S.L.W. 4776"
neutral_cite: 1981 U.S. LEXIS 118
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1981
date_decided: 1981-06-22
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1981-06-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Michigan v. Summers
  varies_by_point: false
  scope_note: "Spatial limit set by Bailey v. United States (immediate vicinity of the premises)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110534/michigan-v-summers/"
  cluster_id: 110534
  opinion_id: 9428436
  identity_checked: true
homes:
  - page: "[[Detention and Search of Persons at the Scene]]"
    role: "Key — Anchor"
  - page: "[[Securing the Scene]]"
    role: "Related (scene-securing overlap)"
related: ["[[Bailey v. United States]]", "[[Muehler v. Mena]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-warrant", "detention", "securing-the-scene"]
holding: "A warrant to search premises for contraband, founded on probable cause, implicitly carries the limited authority to detain the occupants…"
lake:
  record_id: Michigan v. Summers
  status: verified
  projected_at: 2026-07-06
---

# Michigan v. Summers

*452 U.S. 692 (1981)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
As officers arrived to execute a warrant to search Summers's house for narcotics, they encountered him descending the front steps. They detained him while they conducted the search, found narcotics in the house, arrested him, and in a search incident to the arrest found drugs on his person.

## Issue
Whether officers executing a warrant to search premises for contraband may detain the occupants of the premises during the search.

## Rule
Yes. "Thus, for Fourth Amendment purposes, we hold that a warrant to search for contraband founded on probable cause implicitly carries with it the limited authority to detain the occupants of the premises while a proper search is conducted." — 452 U.S. at 705. ^pin-705

## Application
Because the officers held a warrant to search Summers's home for contraband founded on probable cause, they had limited authority to detain him while they conducted the search. His detention was therefore lawful, and once the search produced evidence giving probable cause to arrest, his arrest and the search incident to it were valid.

## Conclusion
Reversed; the detention of Summers during execution of the warrant was constitutional.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Summers* remains good law, but its detention authority was **spatially limited by** [[Bailey v. United States]], which held that the authority to detain occupants extends only to the **immediate vicinity** of the premises being searched.

## Appears on
- [[Securing the Scene]] — *Key — Anchor*

## Sources
- *Michigan v. Summers*, 452 U.S. 692 (1981) — https://www.courtlistener.com/opinion/110534/michigan-v-summers/ — pinpoint: 705.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4aa327397777da4f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "452 U.S. 692 (1981)", "court": "U.S. Supreme Court", "neutral_cite": "1981 U.S. LEXIS 118", "official_citation_present": true, "parallel_cite": "101 S. Ct. 2587; 69 L. Ed. 2d 340; 49 U.S.L.W. 4776", "title": "Michigan v. Summers", "year": "1981"}}
{"assertion_id": "21506909997386c8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A warrant to search premises for contraband, founded on probable cause, implicitly carries the limited authority to detain the occupants…", "title": "Michigan v. Summers"}}
{"assertion_id": "74e5347b49205c31", "dimension": "support", "kind": "home_role", "locator": {"home": "Securing the Scene"}, "payload": {"home": "Securing the Scene", "role": "Related (scene-securing overlap)", "title": "Michigan v. Summers"}}
{"assertion_id": "e6835c1c2adccd8d", "dimension": "support", "kind": "home_role", "locator": {"home": "Detention and Search of Persons at the Scene"}, "payload": {"home": "Detention and Search of Persons at the Scene", "role": "Key — Anchor", "title": "Michigan v. Summers"}}
{"assertion_id": "782b29d455d8ce20", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Michigan v. Summers"}}
{"assertion_id": "cb69688f995ae4dd", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1981-06-22", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Michigan v. Summers", "field_i_validity": "good_law", "scope_note": "Spatial limit set by Bailey v. United States (immediate vicinity of the premises).", "title": "Michigan v. Summers", "varies_by_point": "false"}}
```

### lake record — Michigan v. Summers

```json
{
  "schema_version": "s2.v1",
  "record_id": "Michigan v. Summers",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Michigan v. Summers",
    "case_name_short": "Summers",
    "case_name_full": "Michigan v. Summers",
    "input_case_name": "Michigan v. Summers",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1981-06-22",
    "year": 1981,
    "docket": null,
    "cluster_id": 110534,
    "lead_opinion_id": 9428436,
    "sibling_ids": [
      110534,
      9428436,
      9428437
    ],
    "absolute_url": "/opinion/110534/michigan-v-summers/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9030936,
        "score": 20,
        "case_name": "Michigan v. Summers"
      },
      {
        "cluster_id": 9030154,
        "score": 20,
        "case_name": "Michigan v. Summers"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "452 U.S. 692",
      "volume": "452",
      "reporter": "U.S.",
      "page": "692",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "101 S. Ct. 2587",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2587",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 340",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "340",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 U.S.L.W. 4776",
        "volume": "49",
        "reporter": "U.S.L.W.",
        "page": "4776",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1981 U.S. LEXIS 118",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "118",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "452 U.S. 692",
        "volume": "452",
        "reporter": "U.S.",
        "page": "692",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 S. Ct. 2587",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2587",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 340",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "340",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1981 U.S. LEXIS 118",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "118",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 U.S.L.W. 4776",
        "volume": "49",
        "reporter": "U.S.L.W.",
        "page": "4776",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "452 U.S. 692",
    "official_selection": {
      "court_class": "scotus",
      "selected": "452 U.S. 692",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-705",
      "page": null,
      "quote": "--- # Michigan v. Summers *452 U.S. 692 (1981)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background As officers arrived to execute a warrant to search Summers's house for narcotics, they encountered him descending the front steps. They detained him while they conducted the search, found narcotics in the house, arrested him, and in a search incident to the arrest found drugs on his person. ## Issue Whether officers executing a warrant to search premises for contraband may detain the occupants of the premises during the search. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1981-06-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Michigan v. Summers",
    "varies_by_point": false,
    "scope_note": "Spatial limit set by Bailey v. United States (immediate vicinity of the premises).",
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
        "journal_ref": "Michigan v. Summers:lane1_negative"
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
        "journal_ref": "Michigan v. Summers:lane1_negative"
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
        "journal_ref": "Michigan v. Summers:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Halley v. Huckaby",
          "cluster_id": 4530346,
          "cite": [
            "902 F.3d 1136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Summers:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Daniel J. Glasgow v. State of Indiana",
          "cluster_id": 4482193,
          "cite": [
            "99 N.E.3d 251"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Summers:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Muldrow",
          "cluster_id": 4448772,
          "cite": [
            "2017 Ohio 8839",
            "100 N.E.3d 1093"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Summers:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Harte v. Board Comm'rs Cnty of Johnson",
          "cluster_id": 4411980,
          "cite": [
            "864 F.3d 1154",
            "2017 WL 3138494"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Summers:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Paul Stephens v. Nick Degiovanni, individually",
          "cluster_id": 4379656,
          "cite": [
            "852 F.3d 1298",
            "2017 U.S. App. LEXIS 5548",
            "2017 WL 1174381"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Summers:lane1_negative"
      },
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
        "journal_ref": "Michigan v. Summers:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Chase Duncan",
          "cluster_id": 3073098,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Summers:lane1_negative"
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
        "journal_ref": "Michigan v. Summers:lane1_negative"
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
        "journal_ref": "Michigan v. Summers:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Werra",
          "cluster_id": 212993,
          "cite": [
            "638 F.3d 326",
            "2011 U.S. App. LEXIS 5741",
            "2011 WL 982384"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Summers:lane1_negative"
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
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
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
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
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
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Hodari D.",
          "cluster_id": 112579,
          "cite": [
            "113 L. Ed. 2d 690",
            "111 S. Ct. 1547",
            "499 U.S. 621",
            "1991 U.S. LEXIS 2397",
            "91 Cal. Daily Op. Serv. 2893",
            "59 U.S.L.W. 4335",
            "91 Daily Journal DAR 4665"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
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
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kolender v. Lawson",
          "cluster_id": 110926,
          "cite": [
            "75 L. Ed. 2d 903",
            "103 S. Ct. 1855",
            "461 U.S. 352",
            "1983 U.S. LEXIS 159",
            "51 U.S.L.W. 4532"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
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
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sharpe",
          "cluster_id": 111378,
          "cite": [
            "84 L. Ed. 2d 605",
            "105 S. Ct. 1568",
            "470 U.S. 675",
            "1985 U.S. LEXIS 74",
            "53 U.S.L.W. 4346"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
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
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Layne",
          "cluster_id": 118289,
          "cite": [
            "143 L. Ed. 2d 818",
            "119 S. Ct. 1692",
            "526 U.S. 603",
            "1999 U.S. LEXIS 3633"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hensley",
          "cluster_id": 111294,
          "cite": [
            "83 L. Ed. 2d 604",
            "105 S. Ct. 675",
            "469 U.S. 221",
            "1985 U.S. LEXIS 34",
            "53 U.S.L.W. 4053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
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
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
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
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. Delgado",
          "cluster_id": 111148,
          "cite": [
            "80 L. Ed. 2d 247",
            "104 S. Ct. 1758",
            "466 U.S. 210",
            "1984 U.S. LEXIS 57",
            "52 U.S.L.W. 4436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Johnson",
          "cluster_id": 145912,
          "cite": [
            "172 L. Ed. 2d 694",
            "129 S. Ct. 781",
            "555 U.S. 323",
            "2009 U.S. LEXIS 868"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
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
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brendlin v. California",
          "cluster_id": 145712,
          "cite": [
            "168 L. Ed. 2d 132",
            "127 S. Ct. 2400",
            "551 U.S. 249",
            "2007 U.S. LEXIS 7897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
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
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richards v. Wisconsin",
          "cluster_id": 118103,
          "cite": [
            "137 L. Ed. 2d 615",
            "117 S. Ct. 1416",
            "520 U.S. 385",
            "1997 U.S. LEXIS 2794"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
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
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
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
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
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
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
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
        "journal_ref": "Michigan v. Summers:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110534 OR 9428436 OR 9428437) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjY5OTkzNjAwMDAwJnM9MjI5MTM0OSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110534+OR+9428436+OR+9428437%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110534 OR 9428436 OR 9428437)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yOTEmcz02OTIyODMmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110534+OR+9428436+OR+9428437%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110534 OR 9428436 OR 9428437)",
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
    "complete_query": "cites:(110534 OR 9428436 OR 9428437)",
    "indexed_citing_opinions": 1173,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110534,
        "count": 1053,
        "count_source": "search"
      },
      {
        "opinion_id": 9428436,
        "count": 131,
        "count_source": "search"
      },
      {
        "opinion_id": 9428437,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2038,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/michigan-v-summers.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1NDI3OCZzPTk0NDMzMzgmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28110534+OR+9428436+OR+9428437%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110534,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 109876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 110158,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 1311155,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 1650768,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110534,
        "cited_id": 2018459,
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
    "date_created": "2026-07-05T13:38:36Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:39:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:39:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:41:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:39:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Michigan v. Summers

```
<opinion type="majority">
<author id="b739-6">Justice Stevens</author>
<p id="Ae5">delivered the opinion of the Court.</p>
<p id="b739-7">As Detroit police officers were about to execute a warrant to search a house for narcotics, they encountered respondent descending the front steps. They requested his assistance in gaining entry and detained him while they searched the premises. After finding narcotics in the basement and ascertaining that respondent owned the house, the police arrested him, searched his person, and found in his coat pocket an envelope containing 8.5 grams of heroin.<footnotemark>1</footnotemark></p>
<p id="b740-4"><page-number citation-index="1" label="694">*694</page-number>Respondent was charged with possession of the heroin found on his person. He moved to suppress the heroin as the product of an illegal search in violation of the Fourth Amendment,<footnotemark>2</footnotemark> and the trial judge granted the motion and quashed the information. That order was affirmed by a divided panel of the Michigan Court of Appeals, <span class="citation" data-id="9573541"><a href="/opinion/1311155/people-v-summers/" aria-description="Citation for case: People v. Summers">68 Mich. App. 571</a></span>, <span class="citation" data-id="9573541"><a href="/opinion/1311155/people-v-summers/" aria-description="Citation for case: People v. Summers">243 N. W. 2d 689</a></span>, and by the Michigan Supreme Court over the dissent of three of its justices. <span class="citation" data-id="2018459"><a href="/opinion/2018459/people-v-summers/" aria-description="Citation for case: People v. Summers">407 Mich. 432</a></span>, <span class="citation" data-id="2018459"><a href="/opinion/2018459/people-v-summers/" aria-description="Citation for case: People v. Summers">286 N. W. 2d 226</a></span>. We granted the State’s petition for certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./449/898/">449 U. S. 898</a></span>, and now reverse.</p>
<p id="b740-5">I</p>
<p id="b740-6">The dispositive question in this case is whether the initial detention of respondent violated his constitutional right to be secure against an unreasonable seizure of his person. The State attempts to justify the eventual search of respondent’s person by arguing that the authority to search premises granted by the warrant implicitly included the authority to search persons on those premises, just as that authority included an authorization to search furniture and containers in which the particular things described might be concealed. But as the Michigan Court of Appeals correctly noted, even if otherwise acceptable, this argument could not justify the initial detention of respondent outside the premises described in the warrant. See <span class="citation" data-id="9573541"><a href="/opinion/1311155/people-v-summers/#578" aria-description="Citation for case: People v. Summers">68 Mich. App., at 578-580</a></span>, <span class="citation" data-id="9573541"><a href="/opinion/1311155/people-v-summers/#692" aria-description="Citation for case: People v. Summers">243 N. W. <page-number citation-index="1" label="695">*695</page-number>2d, at 692-693</a></span>. If that detention was permissible, there is no need to reach the question whether a search warrant for premises includes the right to search persons found there, because when the police searched respondent, they had probable cause to arrest him and had done so.<footnotemark>3</footnotemark> Our appraisal of the validity of the search of respondent’s person therefore depends upon a determination whether the officers had the authority to require him to re-enter the house and to remain there while they conducted their search.<footnotemark>4</footnotemark></p>
<p id="b742-4"><page-number citation-index="1" label="696">*696</page-number>II</p>
<p id="b742-5">In assessing the validity of respondent’s initial detention, we note first that it constituted a “seizure” within the meaning of the Fourth Amendment.<footnotemark>5</footnotemark> The State does not contend otherwise, and the record demonstrates that respondent was not free to leave the premises while the officers were searching his home. It is also clear that respondent was not formally arrested until after the search was completed. The dispute therefore involves only the constitutionality of a pre-arrest “seizure” which we assume was unsupported by probable cause.</p>
<p id="b742-6">In <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span>, the Court reaffirmed the general rule that an official seizure of the person must be supported by probable cause, even if no formal arrest is made. In that case police officers located a murder suspect at a neighbor’s house, took him into custody, and transported him to the police station, where interrogation ultimately produced a confession. Because the suspect was not arrested until after he had confessed, and because he presumably would have been set free if probable cause had not been established during his questioning, the State argued that the pre-arrest detention should not be equated with an arrest and should be upheld as “reasonable” in view of the serious character of the crime and the fact that the police had an articulable basis for suspecting that Dunaway was involved. <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#207" aria-description="Citation for case: Dunaway v. New York"><em>Id., </em>at 207</a></span>. The Court firmly rejected the State’s argument, noting that “the detention of petitioner was in <page-number citation-index="1" label="697">*697</page-number>important respects indistinguishable from a traditional arrest.” <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#212" aria-description="Citation for case: Dunaway v. New York"><em>Id., </em>at 212</a></span>.<footnotemark>6</footnotemark> We stated:</p>
<blockquote id="b743-5">“Indeed, any ‘exception’ that could cover a seizure as intrusive as that in this case would threaten to swallow the general rule that Fourth Amendment seizures are ‘reasonable’ only if based on probable cause.</blockquote>
<blockquote id="b743-6">“The central importance of the probable-cause requirement to the protection of a citizen’s privacy afforded by the Fourth Amendment’s guarantees cannot be compromised in this fashion. ‘The requirement of probable cause has roots that are deep in our history.’ <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#100" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 100</a></span> (1959). Hostility to seizures based on mere suspicion was a prime motivation for the adoption of the Fourth Amendment, and decisions immediately after its adoption affirmed that ‘common rumor or report, suspicion, or even “strong reason to suspect” was not adequate to support a warrant for arrest.’ <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#101" aria-description="Citation for case: Henry v. United States"><em>Id., </em>at 101</a></span> (footnotes omitted). The familiar threshold standard of probable cause for Fourth Amendment seizures reflects the benefit of extensive experience accommodating the factors relevant to the ‘reasonableness’ requirement of the Fourth Amendment, and provides the relative simplicity and clarity necessary to the implementation of a workable rule. See <em>Brinegar </em>v. <em>United States, </em>[338 U. S., at 175-176].” <em>Id., </em>at 213.</blockquote>
<p id="b743-7">Although we refused in <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span> </em>to find an exception that would swallow the general rule, our opinion recognized that some seizures significantly less intrusive than an arrest have withstood scrutiny under the reasonableness standard embodied in the Fourth Amendment. In these cases the intru<page-number citation-index="1" label="698">*698</page-number>sion on the citizen’s privacy “was so much less severe” than that involved in a traditional arrest that “the opposing interests in crime prevention and detection and in the police officer’s safety” could support the seizure as reasonable. <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#209" aria-description="Citation for case: Dunaway v. New York"><em>Id., </em>at 209</a></span>.</p>
<p id="b744-5">In the first such case, <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span>, the Court recognized the narrow authority of police officers who suspect criminal activity to make limited intrusions on an individual’s personal security based on less than probable cause. The Court approved a “frisk” for weapons as a justifiable response to an officer’s reasonable belief that he was dealing with a possibly armed and dangerous suspect.<footnotemark>7</footnotemark> In the second such case, <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span>, the Court relied on <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>to hold that an officer could forcibly stop a suspect to investigate an informant’s tip that the suspect was armed and carrying narcotics.<footnotemark>8</footnotemark> And in <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span>, the Court held that the special enforcement problems confronted by roving Border Patrol agents, though not sufficient to justify random stops of vehi<page-number citation-index="1" label="699">*699</page-number>cles near the Mexican border to question their occupants about their citizenship, <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#882" aria-description="Citation for case: United States v. Brignoni-Ponce"><em>id., </em>at 882-884</a></span>,<footnotemark>9</footnotemark> were adequate to support vehicle stops based on the agents’ awareness of specific articulable facts indicating that the vehicle contained illegal aliens. The Court reasoned that the difficulty in patrolling the long Mexican border and the interest in controlling the influx of illegal aliens justified the limited intrusion, usually lasting no more than a minute, involved in the stop. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce"><em>Id., </em>at 878-880</a></span>.<footnotemark>10</footnotemark> See also <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">449 U. S. 411</a></span>.</p>
<p id="b745-5">These cases recognize that some seizures admittedly covered by the Fourth Amendment constitute such limited intrusions on the personal security of those detained and are justified by such substantial law enforcement interests that they may be made on less than probable cause, so long as police have an articulable basis for suspecting criminal activity. In these cases, as in <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>, </em>the Court was applying the ultimate standard of reasonableness embodied in the <page-number citation-index="1" label="700">*700</page-number>Fourth Amendment.<footnotemark>11</footnotemark> They are consistent with the general rule that every arrest, and every seizure having the essential attributes of a formal arrest, is unreasonable unless it is supported by probable cause. But they demonstrate that the exception for limited intrusions that may be justified by special law enforcement interests is not confined to the momentary, on-the-street detention accompanied by a frisk for weapons involved in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>and <em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">Adams</a></span>.</em><footnotemark><em>12</em></footnotemark><em> </em>Therefore, in <page-number citation-index="1" label="701">*701</page-number>order to decide whether this case is controlled by the general rule, it is necessary to examine both the character of the official intrusion and its justification.</p>
<p id="b747-5">Ill</p>
<p id="b747-6">Of prime importance in assessing the intrusion is the fact that the police had obtained a warrant to search respondent’s house for contraband. A neutral and detached magistrate had found probable cause to believe that the law was being violated in that house and had authorized a substantial invasion of the privacy of the persons who resided there. The detention of one of the residents while the premises were searched, although admittedly a significant restraint on his liberty, was surely less intrusive than the search itself.<footnotemark>13</footnotemark> Indeed, we may safely assume that most citizens- — unless they intend flight to avoid arrest — -would elect to remain in order to observe the search of their possessions. Furthermore, the type of detention imposed here is not likely to be exploited by the officer or unduly prolonged in order to gain more information, because the information the officers seek normally will be obtained through the search and not through the detention.<footnotemark>14</footnotemark> <page-number citation-index="1" label="702">*702</page-number>Moreover, because the detention in this case was in respondent’s own residence, it could add only minimally to the public stigma associated with the search itself and would involve neither the inconvenience nor the indignity associated with a compelled visit to the police station.<footnotemark>15</footnotemark> In sharp contrast to the custodial interrogation in <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>, </em>the detention of this respondent was “substantially less intrusive” than an arrest. <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#210" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 210</a></span>.<footnotemark>16</footnotemark></p>
<p id="b748-5">In assessing the justification for the detention of an occupant of premises being searched for contraband pursuant to a valid warrant, both the law enforcement interest and the nature of the “articulable facts” supporting the detention are relevant. Most obvious is the legitimate law enforcement interest in preventing flight in the event that incriminating evidence is found. Less obvious, but sometimes of greater importance, is the interest in minimizing the risk of harm to the officers. Although no special danger to the police is suggested by the evidence in this record, the execution of a warrant to search for narcotics is the kind of transaction that may give rise to sudden violence or frantic efforts to conceal or destroy evidence.<footnotemark>17</footnotemark> The risk of harm to both the <page-number citation-index="1" label="703">*703</page-number>police and the occupants is minimized if the officers routinely exercise unquestioned command of the situation. Cf. 2 W. LaFave, Search and Seizure §4.9, pp. 150-151 (1978). Finally, the orderly completion of the search may be facilitated if the occupants of the premises are present. Their self-interest may induce them to open locked doors or locked containers to avoid the use of force that is not only damaging to property but may also delay the completion of the task at hand.</p>
<p id="b749-5">It is also appropriate to consider the nature of the articu-lable and individualized suspicion on which the police base the detention of the occupant of a home subject to a search warrant. We have already noted that the detention represents only an incremental intrusion on personal liberty when the search of a home has been authorized by a valid warrant. The existence of a search warrant, however, also provides an objective justification for the detention. A judicial officer has determined that police have probable cause to believe that someone in the home is committing a crime. Thus a neutral magistrate rather than an officer in the field has made the critical determination that the police should be given a special authorization to thrust themselves into the privacy of a home.<footnotemark>18</footnotemark> The connection of an occupant to that home <page-number citation-index="1" label="704">*704</page-number>gives the police officer an easily identifiable and certain basis for determining that suspicion of criminal activity justifies a detention of that occupant.</p>
<p id="b750-5">In <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span>, we held that police officers may not enter a private residence to make a routine felony arrest without first obtaining a warrant. In that case we rejected the suggestion that only a search warrant could adequately protect the privacy interests at stake, noting that the distinction between a search warrant and an arrest warrant was far less significant than the interposition of the magistrate’s determination of probable cause between the zealous officer and the citizen:</p>
<blockquote id="b750-6">“It is true that an arrest warrant requirement may afford less protection than a search warrant requirement, but it will suffice to interpose the magistrate’s determination of probable cause between the zealous officer and the citizen. If there is sufficient evidence of a citizen’s participation in a felony to persuade a judicial officer that his arrest is justified, it is constitutionally reasonable to require him to open his doors to the officers of the law. Thus, for Fourth Amendment purposes, an arrest warrant founded on probable cause implicitly carries with it the limited authority to enter a dwelling in which the suspect lives when there is reason to believe the suspect is within.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#602" aria-description="Citation for case: Payton v. New York"><em>Id., </em>at 602-603</a></span>.</blockquote>
<p id="b750-7">That holding is relevant today. If the evidence that a citizen’s residence is harboring contraband is sufficient to per<page-number citation-index="1" label="705">*705</page-number>suade a judicial officer that an invasion of the citizen’s privacy is justified, it is constitutionally reasonable to require that citizen to remain while officers of the law execute a valid warrant to search his home.<footnotemark>19</footnotemark> Thus, for Fourth Amendment purposes, we hold that a warrant to search for contraband<footnotemark>20</footnotemark> founded on probable cause implicitly carries with it the limited authority to detain the occupants of the premises while a proper search is conducted.<footnotemark>21</footnotemark></p>
<p id="b751-4">Because it was lawful to require respondent to re-enter and to remain in the house until evidence establishing probable cause to arrest him was found, his arrest and the search incident thereto were constitutionally permissible. The judg<page-number citation-index="1" label="706">*706</page-number>ment of the Supreme Court of Michigan must therefore be reversed.</p>
<p id="b752-4">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b739-9">The execution of the warrant is described in greater detail in Justice Moody’s opinion for the Michigan Supreme Court:</p>
<blockquote id="b739-10">“Upon arriving at the named address, Oflieer Roger Lehman saw the defendant go out the front door of the house and proceed across the porch and down the steps. When defendant was asked to open the door he replied that he could not because he left his keys inside, but he could ring someone over the intercom. Dwight Calhoun came to the door, but did not admit the police officers. As a result, the officers obtained entrance to the premises by forcing open the front door. Once admittance had been gained Officer Lehman instructed Officer Conant, previously stationed along the side of the house, to bring the defendant, still on the porch, into the house.</blockquote>
<blockquote id="b739-11">“After the eight occupants of the house were detained, a search of the premises revealed two plastic bags of suspected narcotics under the bar in the basement. After finding the suspected narcotics in the basement and upon determining that the defendant was the owner of the house, Officer Conant formally arrested the defendant for violation of the Controlled Substances Act of 1971. MCL 336.341 (4) (a); MSA 18.1070 (41) (4) (a). A custodial search conducted by Officer Conant revealed a plastic bag containing suspected heroin in the defendant’s jacket pocket. It is this heroin, discovered on the person of the defendant, that forms the basis <page-number citation-index="1" label="694">*694</page-number>of the instant possession charge.” <span class="citation" data-id="2018459"><a href="/opinion/2018459/people-v-summers/#441" aria-description="Citation for case: People v. Summers">407 Mich. 432, 441</a></span>, <span class="citation" data-id="2018459"><a href="/opinion/2018459/people-v-summers/#226" aria-description="Citation for case: People v. Summers">286 N. W. 2d 226, 226-227</a></span>.</blockquote>
</footnote>
<footnote label="2">
<p id="b740-8"> The Fourth Amendment to the United States Constitution provides:</p>
<blockquote id="b740-9">“The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”</blockquote>
<p id="b740-10">The Fourteenth Amendment requires the several States to secure these rights. See <em>Payton </em>v. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#576" aria-description="Citation for case: Payton v. New York"><em>New York, 445 </em>U. S. 573, 576</a></span>; <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#207" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 207</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b741-5"> Because there were several other occupants of the house, under Michigan law the evidence that narcotics had been found in the basement of respondent’s house would apparently be insufficient to support a conviction. See <em>People </em>v. <em>Davenport, </em><span class="citation" data-id="1650768"><a href="/opinion/1650768/people-v-davenport/" aria-description="Citation for case: People v. Davenport">39 Mich. App. 252</a></span>, <span class="citation" data-id="1650768"><a href="/opinion/1650768/people-v-davenport/" aria-description="Citation for case: People v. Davenport">197 N. W. 2d 521</a></span> (1972). The Michigan Court of Appeals relied on <em><span class="citation" data-id="1650768"><a href="/opinion/1650768/people-v-davenport/" aria-description="Citation for case: People v. Davenport">Davenport</a></span> </em>to conclude that the officers did not have probable cause to arrest or search respondent even though he was the owner of a house in which contraband was found. <span class="citation" data-id="9573541"><a href="/opinion/1311155/people-v-summers/#580" aria-description="Citation for case: People v. Summers">68 Mich. App., at 580-582</a></span>, <span class="citation" data-id="9573541"><a href="/opinion/1311155/people-v-summers/#692" aria-description="Citation for case: People v. Summers">243 N. W. 2d, at 692-693</a></span>. Judge Bashara, dissenting in the Court of Appeals, <span class="citation" data-id="9573541"><a href="/opinion/1311155/people-v-summers/#585" aria-description="Citation for case: People v. Summers"><em>id., </em>at 585</a></span>, <span class="citation" data-id="9573541"><a href="/opinion/1311155/people-v-summers/#695" aria-description="Citation for case: People v. Summers">243 N. W. 2d, at 695</a></span>, and the three dissenting justices of the Michigan Supreme Court, <span class="citation" data-id="2018459"><a href="/opinion/2018459/people-v-summers/#450" aria-description="Citation for case: People v. Summers">407 Mich., at 450, 463-464</a></span>, <span class="citation" data-id="2018459"><a href="/opinion/2018459/people-v-summers/#231" aria-description="Citation for case: People v. Summers">286 N. W. 2d, at 231, 237</a></span>, pointed out that <em><span class="citation" data-id="1650768"><a href="/opinion/1650768/people-v-davenport/" aria-description="Citation for case: People v. Davenport">Davenport</a></span>, </em>which concerns the proof necessary to support a conviction, is not dispositive of the question whether the police had probable cause to arrest. See <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#174" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 174-176</a></span>. Regardless of whether the police had probable cause to arrest respondent under Michigan law, probable cause within the meaning of the Fourth Amendment is not at issue here. Respondent does not challenge the conclusion that the evidence found in his home established probable cause to arrest him. See Brief for Respondent 17.</p>
</footnote>
<footnote label="4">
<p id="b741-6"> The “seizure” issue in this case should not be confused with the “search” issue presented in <em>Ybarra </em>v. <em>Illinois, </em><span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85</a></span>. In <em><span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">Ybarra</a></span> </em>the police executing a search warrant <em>for </em>a public tavern detained and searched all of the customers who happened to be present. No question concerning the legitimacy of the detention was raised. Rather, the Court concluded that the search of Ybarra was invalid because the police had no reason to believe he had any special connection with the premises, and the police had no other basis for suspecting that he was armed or in possession of contraband. See <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/#90" aria-description="Citation for case: Ybarra v. Illinois"><em>id., </em>at 90-93</a></span>. In this case, only the detention is at issue. The police knew respondent lived in the house, and <page-number citation-index="1" label="696">*696</page-number>they did not search him until after they had probable cause to arrest and had done so.</p>
</footnote>
<footnote label="5">
<p id="b742-9"> “It is quite plain that the Fourth Amendment governs ‘seizures’ of the person which do not eventuate in a trip to the station house and prosecution for crime — ‘arrests’ in traditional terminology. It must be recognized that whenever a police officer accosts an individual and restrains his freedom to walk away, he has ‘seized’ that person.” <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 16</a></span>.</p>
</footnote>
<footnote label="6">
<p id="b743-8"> The Court noted that Dunaway was “taken from a neighbor’s home fo a police car, transported to a police station, and placed in an interrogation room.” He was not informed that he was free to leave; he would not have been free to leave and would have been physically restrained had he attempted to do so. <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#212" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 212</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b744-6"> In upholding the “frisk” employed by the officer in that case, the Court assumed, without explicitly stating, that the Fourth Amendment does not prohibit forcible stops when the officer has a reasonable suspicion that a crime has been or is being committed. See <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#32" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 32-33</a></span> (Harlan, J., concurring); <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#34" aria-description="Citation for case: Terry v. Ohio"><em>id., </em>at 34</a></span> (White, J., concurring). In <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S., at 146</a></span>, the Court made explicit what was implicit in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</em></p>
<p id="b744-7">“A brief stop of a suspicious individual, in order to determine his identity or to maintain the status quo momentarily while obtaining more information, may be most reasonable in light of the facts known to the officer at the time.”</p>
<p id="b744-8">See also <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span>; <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">449 U. S. 411</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b744-9"> The Court noted that the informant’s tip was insufficient to justify an arrest or search based on probable cause under <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span>, and <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span>, but the information “carried enough indicia of reliability to justify the officer’s forcible stop of Williams.” <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#147" aria-description="Citation for case: Adams v. Williams">407 U. S., at 147</a></span>.</p>
</footnote>
<footnote label="9">
<p id="b745-6"> In several cases, the Court has concluded that the absence of any articulable facts available to the officer rendered a detention unreasonable. In <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 663</a></span>, the Court held that police could not make random stops of vehicles in order to check drivers’ licenses and vehicle registrations in the absence of “articulable and reasonable suspicion” that the motorist was unlicensed or the ear unregistered. In <em>Brown </em>v. <em>Texas, </em><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">443 U. S. 47</a></span>, we held that a statute requiring individuals to identify themselves was unconstitutional as applied because the police did not have any reasonable suspicion that the petitioner had committed or was committing a crime. Finally, in <em>Ybarra </em>v. <em>Illinois, </em><span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85</a></span>, we held that police executing a search warrant at a tavern could not invoke <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>to frisk a patron unless the officers had individualized suspicion that the patron might be armed or dangerous.</p>
</footnote>
<footnote label="10">
<p id="b745-7"> The detention approved in <em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span> </em>did not encompass a search of the vehicle. The Court had held in <em>Almeida-Sanchez </em>v. <em>United States, </em><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span>, that such a search must be supported by probable cause. In <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span>, the Court held that stops at permanent checkpoints involved even less intrusion to a motorist than the detention by the roving patrol, and thus a stop at such a checkpoint need not even be based on any individualized suspicion.</p>
</footnote>
<footnote label="11">
<p id="b746-5"> In his opinion for the Court in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>Chief Justice Warren identified “the central inquiry under the Fourth Amendment” as “the reasonableness in all the circumstances of the particular governmental invasion of a citizen’s personal security.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 19</a></span>. Before analyzing the specific stop and frisk involved in that case, he stated:</p>
<blockquote id="b746-6">“The scheme of the Fourth Amendment becomes meaningful only when it is assured that at some point the conduct of those charged with enforcing the laws can be subjected to the more detached, neutral scrutiny of a judge who must evaluate the reasonableness of a particular search or seizure in light of the particular circumstances. And in making that assessment it is imperative that the facts be judged against an objective standard: would the facts available to the officer at the moment of the seizure or the search 'warrant a man of reasonable caution in the belief’ that the action taken was appropriate? Cf. <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925); <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 96-97</a></span> (1964).” <em>Id., </em>at 21-22 (footnotes omitted).</blockquote>
</footnote>
<footnote label="12">
<p id="b746-7"> Justice White, concurring in <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>, </em>noted that <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>is not “an almost unique exception to a hard-and-fast standard of probable cause.” Rather, “the key principle of the Fourth Amendment is reasonableness — the balancing of competing interests.” <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#219" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 219</a></span>. If the purpose underlying a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop — investigating possible criminal activity — is to be served, the police must under certain' circumstances be able to detain the individual for longer than the brief time period involved in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>and <em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">Adams</a></span>. </em>As one commentator observed:</p>
<blockquote id="b746-8">“It is clear that there are several investigative techniques which may be utilized effectively in the course of a Terry-type stop. The most common is interrogation, which may include both a request for identification and inquiry concerning the suspicious conduct of the person detained. Sometimes the officer will communicate with others, either police or private citizens, in an effort to verify the explanation tendered or to confirm the identification or determine whether a person of that identity is otherwise wanted. Or, the suspect may be detained while it is determined if in fact <page-number citation-index="1" label="701">*701</page-number>an offense has occurred in the area, a process which might involve checking certain premises, locating and examining objects abandoned by the suspect, or talking with other people. If it is known that an offense has occurred in the area, the suspect may be viewed by witnesses to the crime. There is no reason to conclude that any investigative methods of the type just listed are inherently objectionable; they might cast doubt upon the reasonableness of the detention, however, if their use makes the period of detention unduly long or involves moving the suspect to another locale.” 3 W. LaFave, Search and Seizure § 9.2, pp. 36-37 (1978).</blockquote>
</footnote>
<footnote label="13">
<p id="b747-8"><em> </em>“As the Court reiterated just a few years ago, the 'physical entry of the home is the chief evil against which the wording of the Fourth Amendment is directed.’ <em>United States </em>v. <em>United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span>. And we have long adhered to the view that the warrant procedure minimizes the danger of needless intrusions of that sort.” <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#585" aria-description="Citation for case: Payton v. New York">445 U. S., at 585-586</a></span>.</p>
</footnote>
<footnote label="14">
<p id="b747-9"> Professor LaFave has noted that the reasonableness of a detention may be determined in part by “whether the police are diligently pur<page-number citation-index="1" label="702">*702</page-number>suing a means of investigation which is likely to resolve the matter one way or another very soon 3 W. LaFave, Search and Seizure § 9.2, p. 40 (1978).</p>
</footnote>
<footnote label="15">
<p id="b748-8"> Moreover, unlike the seizure in <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>, </em>which was designed to provide an opportunity for interrogation and did lead to Dunaway’s confession, the seizure in this case is not likely to have coercive aspects likely to induce self-incrimination.</p>
</footnote>
<footnote label="16">
<p id="b748-9"> We do not view the fact that respondent was leaving his house when the officers arrived to be of constitutional significance. The seizure of respondent on the sidewalk outside was no more intrusive than the detention of those residents of the house whom the police found inside.</p>
</footnote>
<footnote label="17">
<p id="b748-10"> The fact that our holding today deals with a case in which the police had a warrant does not, of course, preclude the possibility that comparable police conduct may be justified by exigent circumstances in the absence of a warrant. No such question, however, is presented by this case.</p>
</footnote>
<footnote label="18">
<p id="b749-6"> Justice Jackson recognized the significance of this determination in <em>Johnson </em>v. <em>United </em>States, <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, 13-14:</p>
<blockquote id="b749-7">“The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime. Any assumption that evidence sufficient to support a magistrate’s disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people’s homes secure only in the discretion of police officers. Crime, even in the privacy of one’s own quarters, is, of course, of grave concern <page-number citation-index="1" label="704">*704</page-number>to society, and the law allows such crime to be reached on proper showing. The right of officers to thrust themselves into a home is also a grave concern, not only to the individual but to a society which chooses to dwell in reasonable security and freedom from surveillance. When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent.” (Footnotes omitted.)</blockquote>
</footnote>
<footnote label="19">
<p id="b751-5"> In refusing to approve seizures based on less than probable cause, the <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span> </em>Court declined to adopt a “multifactor balancing test of 'reasonable police conduct under the circumstances’ to cover all seizures that do not amount to technical arrests.” The Court noted:</p>
<blockquote id="b751-6">“[T]he protections intended by the Framers could all too easily disappear in the consideration and balancing of the multifarious circumstances presented by different cases, especially when that balancing may be done in the first instance by police officers engaged in the 'often competitive enterprise of ferreting out crime.’ ” <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#213" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 213</a></span>.</blockquote>
<p id="b751-7">As Justice White noted in his concurrence in <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>, </em>if police are to have workable rules, the balancing of the competing interests inherent in the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>principle “must in large part be done on a categorical basis— not in an ad hoc, case-by-case fashion by individual police officers.” <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#219" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 219-220</a></span>. The rule we adopt today does not depend upon such an ad hoc determination, because the officer is not required to evaluate either the quantum of proofo justifying detention or the extent of the intrusion to be imposed by the seizure.</p>
</footnote>
<footnote label="20">
<p id="b751-8"> We do not decide whether the same result would be justified if the search warrant merely authorized a search for evidence. Cf. <em>Zurcher </em>v. <em>Stanford Daily, </em><span class="citation" data-id="9427224"><a href="/opinion/109876/zurcher-v-stanford-daily/#560" aria-description="Citation for case: Zurcher v. Stanford Daily">436 U. S. 547, 560</a></span>. See also <span class="citation" data-id="9427224"><a href="/opinion/109876/zurcher-v-stanford-daily/#581" aria-description="Citation for case: Zurcher v. Stanford Daily"><em>id., </em>at 581</a></span> (Stevens, J., dissenting).</p>
</footnote>
<footnote label="21">
<p id="b751-9"> Although special circumstances, or possibly a prolonged detention, might lead to a different conclusion in an unusual case, we are persuaded that this routine detention of residents of a house while it was being searched for contraband pursuant to a valid warrant is not such a case.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Miranda v. Arizona.md  (`case`, 5 assertions)

### content_page

```
---
title: "Miranda v. Arizona"
type: case
citation: "384 U.S. 436 (1966)"
parallel_cite: "86 S. Ct. 1602; 16 L. Ed. 2d 694; 10 Ohio Misc. 9; 36 Ohio Op. 2d 237; 10 A.L.R. 3d 974"
neutral_cite: 1966 U.S. LEXIS 2817
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1966
date_decided: 1966-06-13
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1966-06-13
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Miranda v. Arizona
  varies_by_point: false
  scope_note: Reaffirmed as a constitutional rule in Dickerson v. United States.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107252/miranda-v-arizona/"
  cluster_id: 107252
  opinion_id: 9423233
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Anchor"
related: ["[[Dickerson v. United States]]", "[[Berkemer v. McCarty]]", "[[Berghuis v. Thompkins]]", "[[Edwards v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "custodial-interrogation", "warnings", "self-incrimination"]
holding: "Statements from custodial interrogation are inadmissible unless police first gave the warnings and the suspect knowingly, voluntarily…"
lake:
  record_id: Miranda v. Arizona
  status: verified
  projected_at: 2026-07-09
---

# Miranda v. Arizona

*384 U.S. 436 (1966)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In four consolidated cases, suspects were questioned in police custody without being advised of their rights and made incriminating statements used to convict them. Miranda himself was interrogated and signed a written confession without being told he had a right to remain silent or to the assistance of counsel.

## Issue
What safeguards the prosecution must show were used before statements obtained from custodial interrogation may be admitted against a defendant.

## Rule
"the prosecution may not use statements, whether exculpatory or inculpatory, stemming from custodial interrogation of the defendant unless it demonstrates the use of procedural safeguards effective to secure the privilege against self-incrimination." — 384 U.S. at 444. ^pin-444

"By custodial interrogation, we mean questioning initiated by law enforcement officers after a person has been taken into custody or otherwise deprived of his freedom of action in any significant way." — [*Id.*](https://www.courtlistener.com/opinion/107252/miranda-v-arizona/#:~:text=By%20custodial%20interrogation%2C%20we%20mean) ^pin-444a

Absent other effective safeguards, before any custodial questioning the person must be warned that he has the right to remain silent, that anything he says may be used against him, and that he has the right to retained or appointed counsel.

## Application
Miranda was interrogated in police custody and signed a confession without being advised of his right to remain silent or to counsel. Because the prosecution could not show that the required procedural safeguards were used to protect his privilege against self-incrimination, his confession was inadmissible against him.

## Conclusion
Reversed; the confession obtained without the now-required warnings could not be used.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Miranda* was **reaffirmed** as a constitutional rule that Congress may not supersede by statute in [[Dickerson v. United States]]. It applies to all custodial interrogation regardless of offense severity ([[Berkemer v. McCarty]]), and its invocation/waiver doctrine was developed in cases such as [[Edwards v. Arizona]] and [[Berghuis v. Thompkins]].

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Anchor*

## Sources
- *Miranda v. Arizona*, 384 U.S. 436 (1966) — https://www.courtlistener.com/opinion/107252/miranda-v-arizona/ — pinpoint: 444.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d08fead36e74747d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "384 U.S. 436 (1966)", "court": "U.S. Supreme Court", "neutral_cite": "1966 U.S. LEXIS 2817", "official_citation_present": true, "parallel_cite": "86 S. Ct. 1602; 16 L. Ed. 2d 694; 10 Ohio Misc. 9; 36 Ohio Op. 2d 237; 10 A.L.R. 3d 974", "title": "Miranda v. Arizona", "year": "1966"}}
{"assertion_id": "617b176980d391ab", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Anchor", "title": "Miranda v. Arizona"}}
{"assertion_id": "c3fafb73647503c9", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Statements from custodial interrogation are inadmissible unless police first gave the warnings and the suspect knowingly, voluntarily…", "title": "Miranda v. Arizona"}}
{"assertion_id": "0924d62a2a1d4ca9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1966-06-13", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Miranda v. Arizona", "field_i_validity": "good_law", "scope_note": "Reaffirmed as a constitutional rule in Dickerson v. United States.", "title": "Miranda v. Arizona", "varies_by_point": "false"}}
{"assertion_id": "cd013d4e2889cfb5", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Miranda v. Arizona"}}
```

### lake record — Miranda v. Arizona

```json
{
  "schema_version": "s2.v1",
  "record_id": "Miranda v. Arizona",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Miranda v. Arizona",
    "case_name_short": "Miranda",
    "case_name_full": "Miranda v. Arizona",
    "input_case_name": "Miranda v. Arizona",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1966-06-13",
    "year": 1966,
    "docket": null,
    "cluster_id": 107252,
    "lead_opinion_id": 9423233,
    "sibling_ids": [
      107252,
      9423233,
      9423234,
      9423235
    ],
    "absolute_url": "/opinion/107252/miranda-v-arizona/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "384 U.S. 436",
      "volume": "384",
      "reporter": "U.S.",
      "page": "436",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "86 S. Ct. 1602",
        "volume": "86",
        "reporter": "S. Ct.",
        "page": "1602",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 L. Ed. 2d 694",
        "volume": "16",
        "reporter": "L. Ed. 2d",
        "page": "694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 Ohio Misc. 9",
        "volume": "10",
        "reporter": "Ohio Misc.",
        "page": "9",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "36 Ohio Op. 2d 237",
        "volume": "36",
        "reporter": "Ohio Op. 2d",
        "page": "237",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 A.L.R. 3d 974",
        "volume": "10",
        "reporter": "A.L.R. 3d",
        "page": "974",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1966 U.S. LEXIS 2817",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "2817",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "384 U.S. 436",
        "volume": "384",
        "reporter": "U.S.",
        "page": "436",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "86 S. Ct. 1602",
        "volume": "86",
        "reporter": "S. Ct.",
        "page": "1602",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 L. Ed. 2d 694",
        "volume": "16",
        "reporter": "L. Ed. 2d",
        "page": "694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1966 U.S. LEXIS 2817",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "2817",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 Ohio Misc. 9",
        "volume": "10",
        "reporter": "Ohio Misc.",
        "page": "9",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "36 Ohio Op. 2d 237",
        "volume": "36",
        "reporter": "Ohio Op. 2d",
        "page": "237",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 A.L.R. 3d 974",
        "volume": "10",
        "reporter": "A.L.R. 3d",
        "page": "974",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "384 U.S. 436",
    "official_selection": {
      "court_class": "scotus",
      "selected": "384 U.S. 436",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-444",
      "page": null,
      "quote": "--- # Miranda v. Arizona *384 U.S. 436 (1966)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In four consolidated cases, suspects were questioned in police custody without being advised of their rights and made incriminating statements used to convict them. Miranda himself was interrogated and signed a written confession without being told he had a right to remain silent or to the assistance of counsel. ## Issue What safeguards the prosecution must show were used before statements obtained from custodial interrogation may be admitted against a defendant. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-444a",
      "page": null,
      "quote": "By custodial interrogation, we mean questioning initiated by law enforcement officers after a person has been taken into custody or otherwise deprived of his freedom of action in any significant way.",
      "star_marker": "444",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 9263,
      "fragment": "#:~:text=By%20custodial%20interrogation%2C%20we%20mean",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1966-06-13",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Miranda v. Arizona",
    "varies_by_point": false,
    "scope_note": "Reaffirmed as a constitutional rule in Dickerson v. United States.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "AJAY (AJAY) v. STATE (CRIMINAL)",
          "cluster_id": 10774936,
          "cite": [
            "142 Nev. Adv. Op. No. 4"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane1_negative"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barker v. Wingo",
          "cluster_id": 108590,
          "cite": [
            "33 L. Ed. 2d 101",
            "92 S. Ct. 2182",
            "407 U.S. 514",
            "1972 U.S. LEXIS 34"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bruton v. United States",
          "cluster_id": 107684,
          "cite": [
            "20 L. Ed. 2d 476",
            "88 S. Ct. 1620",
            "391 U.S. 123",
            "1968 U.S. LEXIS 1630"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gregg v. Georgia",
          "cluster_id": 109532,
          "cite": [
            "49 L. Ed. 2d 859",
            "96 S. Ct. 2909",
            "428 U.S. 153",
            "1976 U.S. LEXIS 82"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rose v. Lee",
          "cluster_id": 773551,
          "cite": [
            "252 F.3d 676",
            "2001 U.S. App. LEXIS 10698",
            "2001 WL 558079"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brecht v. Abrahamson",
          "cluster_id": 112845,
          "cite": [
            "123 L. Ed. 2d 353",
            "113 S. Ct. 1710",
            "507 U.S. 619",
            "1993 U.S. LEXIS 2981"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edwards v. Arizona",
          "cluster_id": 110475,
          "cite": [
            "68 L. Ed. 2d 378",
            "101 S. Ct. 1880",
            "451 U.S. 477",
            "1981 U.S. LEXIS 96"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'Sullivan v. Boerckel",
          "cluster_id": 118296,
          "cite": [
            "144 L. Ed. 2d 1",
            "119 S. Ct. 1728",
            "526 U.S. 838",
            "1999 U.S. LEXIS 4003"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Teague v. Lane",
          "cluster_id": 112206,
          "cite": [
            "103 L. Ed. 2d 334",
            "109 S. Ct. 1060",
            "489 U.S. 288",
            "1989 U.S. LEXIS 1043"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rose v. Lundy",
          "cluster_id": 110662,
          "cite": [
            "71 L. Ed. 2d 379",
            "102 S. Ct. 1198",
            "455 U.S. 509",
            "1982 U.S. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clewis v. State",
          "cluster_id": 2462780,
          "cite": [
            "922 S.W.2d 126",
            "1996 Tex. Crim. App. LEXIS 11",
            "1996 WL 37908"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baker v. McCollan",
          "cluster_id": 110132,
          "cite": [
            "61 L. Ed. 2d 433",
            "99 S. Ct. 2689",
            "443 U.S. 137",
            "1979 U.S. LEXIS 141"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rhode Island v. Innis",
          "cluster_id": 110254,
          "cite": [
            "64 L. Ed. 2d 297",
            "100 S. Ct. 1682",
            "446 U.S. 291",
            "1980 U.S. LEXIS 94"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re GAULT",
          "cluster_id": 107439,
          "cite": [
            "18 L. Ed. 2d 527",
            "87 S. Ct. 1428",
            "387 U.S. 1",
            "1967 U.S. LEXIS 1478",
            "40 Ohio Op. 2d 378"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Furman v. Georgia",
          "cluster_id": 108605,
          "cite": [
            "33 L. Ed. 2d 346",
            "92 S. Ct. 2726",
            "408 U.S. 238",
            "1972 U.S. LEXIS 169"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107252 OR 9423233 OR 9423234 OR 9423235) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzYwNTcyODAwMDAwJnM9MTA3MDYyNzUmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107252+OR+9423233+OR+9423234+OR+9423235%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107252 OR 9423233 OR 9423234 OR 9423235)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMzQwJnM9MTExNjE0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107252+OR+9423233+OR+9423234+OR+9423235%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107252 OR 9423233 OR 9423234 OR 9423235)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzY1NDExMjAwMDAwJnM9MTA3NTMzNzMmdD1vJmQ9MjAyNi0wNy0wNiZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107252+OR+9423233+OR+9423234+OR+9423235%29&type=o",
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
    "complete_query": "cites:(107252 OR 9423233 OR 9423234 OR 9423235)",
    "indexed_citing_opinions": 34147,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107252,
        "count": 30407,
        "count_source": "search"
      },
      {
        "opinion_id": 9423233,
        "count": 4367,
        "count_source": "search"
      },
      {
        "opinion_id": 9423234,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423235,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 58315,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/miranda-v-arizona.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yLjc3Nzc1ODQmcz04NzI3NjQyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107252+OR+9423233+OR+9423234+OR+9423235%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 9423235,
        "cited_id": 91057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 94082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 94327,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 94454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 97552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 103855,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 103974,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 104931,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 105149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 106512,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 107116,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 270056,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 270206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 270413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 1177527,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 2189589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 2402399,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 85330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 91057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 94454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 97242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 101320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103792,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 104849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 104890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 104931,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105449,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105508,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 107014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 107085,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 236744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 244463,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 264658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 265586,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 267168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 268400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 268701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 269239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 269286,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 270022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 1167454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 1177555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 1297557,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 1393125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 1429077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 1544343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 2045374,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 2221754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 2608355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 3314077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 5516029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 5520716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 5521593,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 5521618,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 6751647,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 6913112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 8144042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 8155149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 8156474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 8571803,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 8571939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 9419181,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 9422869,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 9423096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 9549155,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 91057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 94327,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 94454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 97552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 100776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 102189,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 103792,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 103833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 104010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 104931,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 104997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 105095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 105149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106512,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 265095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 265525,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 265586,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 266372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 267167,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 267168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 268701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 270054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 1177555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 1177616,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 1484800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 1512810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 1513064,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 1738732,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 1789370,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 2106318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 2138506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 2221754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 2398929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 2402413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 2619836,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 5521591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 9421842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 9444722,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 85330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 91057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 94082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 94327,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 94454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 97242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 97552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 100776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 101320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 102189,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103792,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103855,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103974,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104931,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105449,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105508,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106512,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 107014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 107085,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 107116,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 236744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 244463,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 264658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 265095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 265525,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 265586,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 266372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 267167,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 267168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 268400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 268701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 269239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 269286,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 270022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 270054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 270056,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 270206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 270413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1167454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1177527,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1177555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1177616,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1297557,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1393125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1429077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1484800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1512810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1513064,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1544343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1738732,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1789370,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2045374,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2106318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2138506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2189589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2221754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2398929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2402399,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2402413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2608355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2619836,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 3314077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 5516029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 5520716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 5521591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 5521593,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 5521618,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 6751647,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 6913112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 8144042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 8155149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 8156474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 8571803,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 8571939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 9419181,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 9421842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 9422869,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 9423096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 9423233,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 9444722,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 9549155,
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
    "date_created": "2026-07-05T14:09:29Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:09:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:09:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:13:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:09:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Miranda v. Arizona (truncated)

```
<opinion type="majority">
<author id="b537-7">Mr. Chief Justice Warren</author>
<p id="AMNy">delivered the opinion of the Court.</p>
<p id="b537-8">The cases before us raise questions which go to the roots of our concepts of American criminal jurisprudence: the restraints society must observe consistent with the Federal Constitution in prosecuting individuals for crime. More specifically, we deal with the admissibility of statements obtained from an individual who is subjected to custodial police interrogation and the necessity for procedures which assure that the individual is accorded his privilege under the Fifth Amendment to the Constitution not to be compelled to incriminate himself.</p>
<p id="b538-5"><page-number citation-index="1" label="440">*440</page-number>We dealt with certain phases of this problem recently in <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964). There, as in the four cases before us, law enforcement officials took the defendant into custody and interrogated him in a police station for the purpose of obtaining a confession. The police did not effectively advise him of his right to remain silent or of his right to consult with his attorney. Rather, they confronted him with an alleged accomplice who accused him of having perpetrated a murder. When the defendant denied the accusation and said “I didn’t shoot Manuel, you did it,” they handcuffed him and took him to an interrogation room. There, while handcuffed and standing, he was questioned for four hours until he confessed. During this interrogation, the police denied his request to speak to his attorney, and they prevented his retained attorney, who had come to the police station, from consulting with him. At his trial, the State, over his objection, introduced the confession against him. We held that the statements thus made were constitutionally inadmissible.</p>
<p id="b538-6">This case has been the subject of judicial interpretation and spirited legal debate since it was decided two years ago. Both state and federal courts, in assessing its implications, have arrived at varying conclusions.<footnotemark>1</footnotemark> A wealth of scholarly material has been written tracing its ramifications and underpinnings.<footnotemark>2</footnotemark> Police and prose<page-number citation-index="1" label="441">*441</page-number>cutor have speculated on its range and desirability.<footnotemark>3</footnotemark> We granted certiorari in these cases, <span class="citation multiple-matches"><a href="/c/U.%20S./382/924/">382 U. S. 924</a></span>, 925, 937, in order further to explore some facets of the problems, thus exposed, of applying the privilege against self-incrimination to in-custody interrogation, and to give <page-number citation-index="1" label="442">*442</page-number>concrete constitutional guidelines for law enforcement agencies and courts to follow.</p>
<p id="b540-6">We start here, as we did in <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>, </em>with the premise that our holding is not an innovation in our jurisprudence, but is an application of principles long recognized and applied in other settings. We have undertaken a thorough re-examination of the <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>decision and the principles it announced, and we reaffirm it. That case was but an explication of basic rights that are enshrined in our Constitution — that “No person . . . shall be compelled in any criminal case to be a witness against himself,” and that “the accused shall . . . have the Assistance of Counsel” — rights which were put in jeopardy in that case through official overbearing. These precious rights were fixed in our Constitution only after centuries of persecution and struggle. And in the words of Chief Justice Marshall, they were secured “for ages to come, and . . . designed to approach immortality as nearly as human institutions can approach it,” <em>Cohens </em>v. <em>Virginia, </em><span class="citation" data-id="85330"><a href="/opinion/85330/cohens-v-virginia/#387" aria-description="Citation for case: Cohens v. Virginia">6 Wheat. 264, 387</a></span> (1821).</p>
<p id="b540-7">Over 70 years ago, our predecessors on this Court eloquently stated:</p>
<blockquote id="b540-8">“The maxim <em>nemo tenetur seipsum acensare </em>had its origin in a protest against the inquisitorial and manifestly unjust methods of- interrogating accused persons, which [have] long obtained in the continental system, and, until the expulsion of the Stuarts from the British throne in 1688, and the erection of additional barriers for the protection of the people against the exercise of arbitrary power, [were] not uncommon even in England. While the admissions or confessions of the prisoner, when voluntarily and freely made, have always ranked high in the scale of incriminating evidence, if an accused person be asked to explain his apparent connection with a crime under investigation, the ease with which the <page-number citation-index="1" label="443">*443</page-number>questions put to him may assume an inquisitorial character, the temptation to press the witness unduly, to browbeat him if he be timid or reluctant, to push him into a corner, and to entrap him into fatal contradictions, which is so painfully evident in many of the earlier state trials, notably in those of Sir Nicholas Throckmorton, and Udal, the Puritan minister, made the system so odious as to give rise to a demand for its total abolition. The change in the English criminal procedure in that particular seems to be founded upon no statute and no judicial opinion, but upon a general and silent acquiescence of the courts in a popular demand. But, however adopted, it has become firmly embedded in English, as well as in American jurisprudence. So deeply did the iniquities of the ancient system impress themselves upon the minds of the American colonists that the States, with one accord, made a denial of the right to question an accused person a part of their fundamental law, so that a maxim, which in England was a mere rule of evidence, became clothed in this country with the impregnability of a constitutional enactment.” <em>Brown </em>v. <em>Walker, </em><span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#596" aria-description="Citation for case: Brown v. Walker">161 U. S. 591, 596-597</a></span> (1896).</blockquote>
<p id="b541-5">In stating the obligation of the judiciary to apply these constitutional rights, this Court declared in <em>Weems </em>v. <em>United States, </em><span class="citation" data-id="9418181"><a href="/opinion/97242/weems-v-united-states/#373" aria-description="Citation for case: Weems v. United States">217 U. S. 349, 373</a></span> (1910):</p>
<blockquote id="b541-8"><em>. </em>. our contemplation cannot be only of what has been but of what may be. Under any other rule a constitution would indeed be as easy of application as it would be deficient in efficacy and power. Its general principles would have little value and be converted by precedent into impotent and lifeless formulas. Rights declared in words might be lost in reality. And this has been recognized. The <page-number citation-index="1" label="444">*444</page-number>meaning and vitality of the Constitution have developed against narrow and restrictive construction.”</blockquote>
<p id="b542-6">This was the spirit in which we delineated, in meaningful language, the manner in which the constitutional rights of the individual could be enforced against overzealous police practices. It was necessary in <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>, </em>as here, to insure that what was proclaimed in the Constitution had not become but a “form of words,” <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span> (1920), in the hands of government officials. And it is in this spirit, consistent with our role as judges, that we adhere to the principles of <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>today.</p>
<p id="b542-7">Our holding will be spelled out with some specificity in the pages which follow but briefly stated it is this: the prosecution may not use statements, whether exculpatory or inculpatory, stemming from custodial interrogation of the defendant unless it demonstrates the use of procedural safeguards effective to secure the privilege against self-incrimination. By custodial interrogation, we mean questioning initiated by law enforcement officers after a person has been taken into custody or otherwise deprived of his freedom of action in any significant way.<footnotemark>4</footnotemark> As for the procedural safeguards to be employed, unless other fully effective means are devised to inform accused persons of their right of silence and to assure a continuous opportunity to exercise it, the following measures are required. Prior to any questioning, the person must be warned that he has a right to remain silent, that any statement he does make may be used as evidence against him, and that he has a right to the presence of an attorney, either retained or appointed. The defendant may waive effectuation of these rights, provided the waiver is made voluntarily, knowingly and intelligently. If, however, he indicates in any manner and at any stage of the <page-number citation-index="1" label="445">*445</page-number>process that he wishes to consult with an attorney before speaking there can be no questioning. Likewise, if the individual is alone and indicates in any manner that he does not wish to be interrogated, the police may not question him. The mere fact that he may have answered some questions or volunteered some statements on his own does not deprive him of the right to refrain from answering any further inquiries until he has consulted with an attorney and thereafter consents to be questioned.</p>
<p id="b543-5">I.</p>
<p id="b543-6">The constitutional issue we decide in each of these cases is the admissibility of statements obtained from a defendant questioned while in custody or otherwise deprived of his freedom of action in any significant way. In each, the defendant was questioned by police officers, detectives, or a prosecuting attorney in a room in which he was cut off from the outside world. In none of these cases was the defendant given a full and effective warning of his rights at the outset of the interrogation process. In all the cases, the questioning elicited oral admissions, and in three of them, signed statements as well which were admitted at their trials. They all thus share salient features— incommunicado interrogation of individuals in a police-dominated atmosphere, resulting in self-incriminating statements without full warnings of constitutional rights.</p>
<p id="b543-7">An understanding of the nature and setting of this in-custody interrogation is essential to our decisions today. The difficulty in depicting what transpires at such interrogations stems from the fact that in this country they have largely taken place incommunicado. From extensive factual studies undertaken in the early 1930’s, including the famous Wickersham Report to Congress by a Presidential Commission, it is clear that police violence and the “third degree” flourished at that time.<footnotemark>5</footnotemark> <page-number citation-index="1" label="446">*446</page-number>In a series of cases decided by this Court long after these studies, the police resorted to physical brutality — beating, hanging, whipping — and to sustained and protracted questioning incommunicado in order to extort confessions.<footnotemark>6</footnotemark> The Commission on Civil Rights in 1961 found much evidence to indicate that “some policemen still resort to physical force to obtain confessions,” 1961 Comm’n on Civil Rights Rep., Justice, pt. 5, 17. The use of physical brutality and violence is not, unfortunately, relegated to the past or to any part of the country. Only recently in Kings County, New York, the police brutally beat, kicked and placed lighted cigarette butts on the back of a potential witness under interrogation for the purpose of securing a statement incriminating a third party. <em>People </em>v. <em>Portelli, </em>15 N. Y. 2d 235, <span class="citation" data-id="5521593"><a href="/opinion/5674064/people-v-portelli/" aria-description="Citation for case: People v. Portelli">205 N. E. 2d 857</a></span>, 257 N. Y. S. 2d 931 (1965).<footnotemark>7</footnotemark></p>
<p id="b545-4"><page-number citation-index="1" label="447">*447</page-number>The examples given above are undoubtedly the exception now, but they are sufficiently widespread to be the object of concern. Unless a proper limitation upon custodial interrogation is achieved — such as these decisions will advance — -there can be no assurance that practices of this nature will be eradicated in the foreseeable future. The conclusion of the Wickersham Commission Report, made over 30 years ago, is still pertinent:</p>
<blockquote id="b545-5">“To the contention that the third degree is necessary to get the facts, the reporters aptly reply in the language of the present Lord Chancellor of England (Lord Sankey): ‘It is not admissible to do a great right by doing a little wrong. ... It is not sufficient to do justice by obtaining a proper result by irregular or improper means.’ Not only does the use of the third degree involve a flagrant violation of law by the officers of the law, but it involves also the dangers of false confessions, and it tends to make police and prosecutors less zealous in the search for objective evidence. As the New York prosecutor quoted in the report said, <em>‘It </em>is a short cut and makes the police lazy and unenterprising.’ Or, as another official quoted remarked: Tf you use your fists, you <page-number citation-index="1" label="448">*448</page-number>are not so likely to use your wits.’ We agree with the conclusion expressed in the report, that ‘The third degree brutalizes the police, hardens the prisoner against society, and lowers the esteem in which the administration of justice is held by the public.’ ” IV National Commission on Law Observance and Enforcement, Report on Lawlessness in Law Enforcement 5 (1931).</blockquote>
<p id="b546-6">Again we stress that the modern practice of in-custody interrogation is psychologically rather than physically oriented. As we have stated before, “Since <em>Chambers </em>v. <em>Florida, </em><span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span>, this Court has recognized that coercion can be mental as well as physical, and that the blood of the accused is not the only hallmark of an unconstitutional inquisition.” <em>Blackburn </em>v. <em>Alabama, </em><span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 206</a></span> (1960). Interrogation still takes place in privacy. Privacy results in secrecy and this in turn results in a gap in our knowledge as to what in fact goes on in the interrogation rooms. A valuable source of information about present police practices, however, may be found in various police manuals and texts which document procedures employed with success in the past, and which recommend various other effective tactics.<footnotemark>8</footnotemark> These <page-number citation-index="1" label="449">*449</page-number>texts are used by law enforcement agencies themselves as guides.<footnotemark>9</footnotemark> It should be noted that these texts professedly present the most enlightened and effective means presently used to obtain statements through custodial interrogation. By considering these texts and other data, it is possible to describe procedures observed and noted around the country.</p>
<p id="b547-5">The officers are told by the manuals that the “principal psychological factor contributing to a successful interrogation is <em>privacy </em>— being alone with the person under interrogation.” <footnotemark>10</footnotemark> The efficacy of this tactic has been explained as follows:</p>
<blockquote id="b547-6">“If at all practicable, the interrogation should take place in the investigator’s office or at least in a room of his own choice. The subject should be deprived of every psychological advantage. In his own home he may be confident, indignant, or recalcitrant. He is more keenly aware of his rights and <page-number citation-index="1" label="450">*450</page-number>more reluctant to tell of his indiscretions or criminal behavior within the walls of his home. Moreover his family and other friends are nearby, their presence lending moral support. In his own office, the investigator possesses all the advantages. The atmosphere suggests the invincibility of the forces of the law.” <footnotemark>11</footnotemark></blockquote>
<p id="b548-6">To highlight the isolation and unfamiliar surroundings, the manuals instruct the police to display an air of confidence in the suspect’s guilt and from outward appearance to maintain only an interest in confirming certain details. The guilt of the subject is to be posited as a fact. The interrogator should direct his comments toward the reasons why the subject committed the act, rather than court failure by asking the subject whether he did it. Like other men, perhaps the subject has had a bad family life, had an unhappy childhood, had too much to drink, had an unrequited desire for women. The officers are instructed to minimize the moral seriousness of the offense,<footnotemark>12</footnotemark> to cast blame on the victim or on society.<footnotemark>13</footnotemark> These tactics are designed to put the subject in a psychological state where his story is but an elaboration of what the police purport to know already— that he is guilty. Explanations to the contrary are dismissed and discouraged.</p>
<p id="b548-7">The texts thus stress that the major qualities an interrogator should possess are patience and perseverance. <page-number citation-index="1" label="451">*451</page-number>One writer describes the efficacy of these characteristics in this manner:</p>
<blockquote id="b549-5">“In the preceding paragraphs emphasis has been placed on kindness and stratagems. The investigator will, however, encounter many situations where the sheer weight of his personality will be the deciding factor. Where emotional appeals and tricks are employed to no avail, he must rely on an oppressive atmosphere of dogged persistence. He must interrogate steadily and without relent, leaving the subject no prospect of surcease. He must dominate his subject and overwhelm him with his inexorable will to obtain the truth. He should interrogate for a spell of several hours pausing only for the subject’s necessities in acknowledgment of the need to avoid a charge of duress that can be technically substantiated. In a serious case, the interrogation may continue for days, with the required intervals for food and sleep, but with no respite from the atmosphere of domination. It is possible in this way to induce the subject to talk without resorting to duress or coercion. The method should be used only when the guilt of the subject appears highly probable.” <footnotemark>14</footnotemark></blockquote>
<p id="b549-6">The manuals suggest that the suspect be offered legal excuses for his actions in order to obtain an initial admission of guilt. Where there is a suspected revenge-killing, for example, the interrogator may say:</p>
<blockquote id="b549-7">“Joe, you probably didn’t go out looking for this fellow with the purpose of shooting him. My guess is, however, that you expected something from him and that’s why you carried a gun — for your own protection. You knew him for what he was, no good. Then when you met him he probably started using foul, abusive language and he gave some indi<page-number citation-index="1" label="452">*452</page-number>cation that he was about to pull a gun on you, and that’s when you had to act to save your own life. That’s about it, isn’t it, Joe?” <footnotemark>15</footnotemark></blockquote>
<p id="ABc">Having then obtained the admission of shooting, the interrogator is advised to refer to circumstantial evidence which negates the self-defense explanation. This should enable him to secure the entire story. One text notes that “Even if he fails to do so, the inconsistency between the subject’s original denial of the shooting and his present admission of at least doing the shooting will serve to deprive him of a self-defense ‘out’ at the time of trial.” <footnotemark>16</footnotemark></p>
<p id="b550-6">When the techniques described above prove unavailing, the texts recommend they be alternated with a show of some hostility. One ploy often used has been termed the “friendly-unfriendly” or the “Mutt and Jeff” act:</p>
<blockquote id="b550-7">“. . . In this technique, two agents are employed. Mutt, the relentless investigator, who knows the subject is guilty and is not going , to waste any time. He’s sent a dozen men away for this crime and he’s going to send the subject away for the full term. Jeff, on the other hand, is obviously a kindhearted man. He has a family himself. He has a brother who was involved in a little scrape like this. He disapproves of Mutt and his tactics and will arrange to get him off the case if the subject will cooperate. He can’t hold Mutt off for very long. The subject would be wise to make a quick decision. The technique is applied by having both investigators present while Mutt acts out his role. Jeff may stand by quietly and demur at some of Mutt’s tactics. When Jeff makes his plea for cooperation, Mutt is not present in the room.” <footnotemark>17</footnotemark></blockquote>
<p id="b551-4"><page-number citation-index="1" label="453">*453</page-number>The interrogators sometimes are instructed to induce a confession out of trickery. The technique here is quite effective in crimes which require identification or which run in series. In the identification situation, the interrogator may take a break in his questioning to place the subject among a group of men in a line-up. “The witness or complainant (previously coached, if necessary) studies the line-up and confidently points out the subject as the guilty party.” <footnotemark>18</footnotemark> Then the questioning resumes “as though there were now no doubt about the guilt of the subject.” A variation on this technique is called the “reverse line-up”:</p>
<blockquote id="b551-5">“The accused is placed in a line-up, but this time he is identified by several fictitious witnesses or victims who associated him with different offenses. It is expected that the subject will become desperate and confess to the offense under investigation in order to escape from the false accusations.” <footnotemark>19</footnotemark></blockquote>
<p id="b551-6">The manuals also contain instructions for police on how to handle the individual who refuses to discuss the matter entirely, or who asks for an attorney or relatives. The examiner is to concede him the right to remain silent. “This usually has a very undermining effect. First of all, he is disappointed in his expectation of an unfavorable reaction on the part of the interrogator. Secondly, a concession of this right to remain silent im<page-number citation-index="1" label="454">*454</page-number>presses the subject with the apparent fairness of his interrogator.”<footnotemark>20</footnotemark> After this psychological conditioning, however, the officer is told to point out the incriminating significance of the suspect’s refusal to talk:</p>
<blockquote id="b552-6">“Joe, you have a right to remain silent. That’s your privilege and I’m the last person in the world who’ll try to take it away from you. If that’s the way you want to leave this, O. K. But let me ask you this. Suppose you were in my shoes and I were in yours and you called me in to ask me about this and I told you, T don’t want to answer any of your questions.’ You’d think I had something to hide, and you’d probably be right in thinking that. That’s exactly what I’ll have to think about you, and so will everybody else. So let’s sit here and talk this whole thing over.” <footnotemark>21</footnotemark></blockquote>
<p id="b552-7">New will persist in their initial refusal to talk, it is said, if this monologue is employed correctly.</p>
<p id="b552-8">In the event that the subject wishes to speak to a relative or an attorney, the following advice is tendered:</p>
<blockquote id="b552-9">“[T]he interrogator should respond by suggesting that the subject first tell the truth to the interrogator himself rather than get anyone else involved in the matter. If the request is for an attorney, the interrogator may suggest that the subject save himself or his family the expense of any such professional service, particularly if he is innocent of the offense under investigation. The interrogator may also add, ‘Joe, I’m only looking for the truth, and if you’re telling the truth, that’s it. You can handle this by yourself.’ ” <footnotemark>22</footnotemark></blockquote>
<p id="b553-4"><page-number citation-index="1" label="455">*455</page-number>From these representative samples of interrogation techniques, the setting prescribed by the manuals and observed in practice becomes clear. In essence, it is this: To be alone with the subject is essential to prevent distraction and to deprive him of any outside support. The aura of confidence in his guilt undermines his will to resist. He merely confirms the preconceived story the police seek to have him describe. Patience and persistence, at times relentless questioning, are employed. To obtain a confession, the interrogator must “patiently maneuver himself or his quarry into a position from which the desired objective may be attained.” <footnotemark>23</footnotemark> When normal procedures fail to produce the needed result, the police may resort to deceptive stratagems such as giving false legal advice. It is important to keep the subject off balance, for example, by trading on his insecurity about himself or his surroundings. The police then persuade, trick, or cajole him out of exercising his constitutional rights.</p>
<p id="b553-5">Even without employing brutality, the “third degree” or the specific stratagems described above, the very fact of custodial interrogation exacts a heavy toll on individual liberty and trades on the weakness of individuals.<footnotemark>24</footnotemark> <page-number citation-index="1" label="456">*456</page-number>This fact may be illustrated simply by referring to three confession cases decided by this Court in the Term immediately preceding our <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>decision. In <em>Townsend </em>v. <em>Sain, </em><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">372 U. S. 293</a></span> (1963), the defendant was a 19-year-old heroin addict, described as a “near mental defective,” <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/#307" aria-description="Citation for case: Townsend v. Sain"><em>id., </em>at 307-310</a></span>. The defendant in <em>Lynumn </em>v. <em>Illinois, </em><span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528</a></span> (1963), was a woman who confessed to the arresting officer after being importuned to “cooperate” in order to prevent her children from being taken by relief authorities. This Court as in those cases reversed the conviction of a defendant in <em>Haynes </em>v. <em>Washington, </em><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span> (1963), whose persistent request during his interrogation was to phone his wife or attorney.<footnotemark>25</footnotemark> In other settings, these individuals might have exercised their constitutional rights. In the incommunicado police-dominated atmosphere, they succumbed.</p>
<p id="b554-6">In the cases before us today, given this background, we concern ourselves primarily with this interrogation atmosphere and the evils it can bring. In No. 759, <em>Miranda </em>v. <em>Arizona, </em>the police arrested the defendant and took him to a special interrogation room where they secured a confession. In No. 760, <em>Vignera </em>v. <em>New York, </em>the defendant made oral admissions to the police after interrogation in the afternoop, and then signed an inculpatory statement upon being questioned by an assistant district attorney later the same evening. In No. 761, <em>Westover </em>v. <em>United States, </em>the defendant was handed over to the Federal Bureau of Investigation by <page-number citation-index="1" label="457">*457</page-number>local authorities after they had detained and interrogated him for a lengthy period, both at night and the following morning. After some two hours of questioning, the federal officers had obtained signed statements from the defendant. Lastly, in No. 584, <em>California </em>v. <em>Stewart, </em>the local police held the defendant five days in the station and interrogated him on nine separate occasions before they secured his inculpatory statement.</p>
<p id="b555-5">In these cases, we might not find the defendants’ statements to have been involuntary in traditional terms. Our concern for adequate safeguards to protect precious Fifth Amendment rights is, of course, not lessened in the slightest. In each of the cases, the defendant was thrust into an unfamiliar atmosphere and run through menacing police interrogation procedures. The potentiality for compulsion is forcefully apparent, for example, in <em>Miranda, </em>where the indigent Mexican defendant was a seriously disturbed individual with pronounced sexual fantasies, and in <em>Stewart, </em>in which the defendant was an indigent Los Angeles Negro who had dropped out of school in the sixth grade. To be sure, the records do not evince overt physical coercion or patent psychological ploys. The fact remains that in none of these cases did the officers undertake to afford appropriate safeguards at the outset of the interrogation to insure that the statements were truly the product of free choice.</p>
<p id="b555-6">It is obvious that such an interrogation environment is created for no purpose other than to subjugate the individual to the will of his examiner. This atmosphere carries its own badge of intimidation. To be sure, this is not physical intimidation, but it is equally destructive of human dignity.<footnotemark>26</footnotemark> The current practice of incommunicado interrogation is at odds with one of our <page-number citation-index="1" label="458">*458</page-number>Nation’s most cherished principles — that the individual may not be compelled to incriminate himself. Unless adequate protective devices are employed to dispel the compulsion inherent in custodial surroundings, no statement obtained from the defendant can truly be the product of his free choice.</p>
<p id="b556-6">From the foregoing, we can readily perceive an intimate connection between the privilege against self-incrimination and police custodial questioning. It is fitting to turn to history and precedent underlying the Self-Incrimination Clause to determine its applicability in this situation.</p>
<p id="b556-7">II.</p>
<p id="b556-8">We sometimes forget how long it has taken to establish the privilege against self-incrimination, the sources from which it came and the fervor with which it was defended. Its roots go back into ancient times.<footnotemark>27</footnotemark> Per<page-number citation-index="1" label="459">*459</page-number>haps the critical historical event shedding light on its origins and evolution was the trial of one John Lilburn, a vocal anti-Stuart Leveller, who was made to take the Star Chamber Oath in 1637. The oath would have bound him to answer to all questions posed to him on any subject. The Trial of John Lilburn and John Wharton, 3 How. St. Tr. 1315 (1637). He resisted the oath and declaimed the proceedings, stating:</p>
<blockquote id="b557-5">“Another fundamental right I then contended for, was, that no man’s conscience ought to be racked by oaths imposed, to answer to questions concerning himself in matters criminal, or pretended to be so.” Haller &amp; Davies, The Leveller Tracts 1647-1653, p. 454 (1944).</blockquote>
<p id="b557-6">On account of the Lilburn Trial, Parliament abolished the inquisitorial Court of Star Chamber and went further in giving him generous reparation. The lofty principles to which Lilburn had appealed during his trial gained popular acceptance in England.<footnotemark>28</footnotemark> These sentiments worked their way over to the Colonies and were implanted after great struggle into the Bill of Rights.<footnotemark>29</footnotemark> Those who framed our Constitution and the Bill of Rights were ever aware of subtle encroachments on individual liberty. They knew that “illegitimate and unconstitutional practices get their first footing ... by silent approaches and slight deviations from legal modes of procedure.” <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 635</a></span> (1886). The privilege was elevated to constitutional status and has always been “as broad as the mischief <page-number citation-index="1" label="460">*460</page-number>against which it seeks to guard.” <em>Counselman </em>v. <em>Hitchcock, </em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#562" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 562</a></span> (1892). We cannot depart from this noble heritage.</p>
<p id="b558-6">Thus we may view the historical development of the privilege as one which groped for the proper scope of governmental power over the citizen. As a “noble principle often transcends its origins,” the privilege has come rightfully to be recognized in part as an individual’s substantive right, a “right to a private enclave where he may lead a private life. That right is the hallmark of our democracy.” <em>United States </em>v. <em>Grunewald, </em><span class="citation" data-id="6913112"><a href="/opinion/7012574/united-states-v-grunewald/#579" aria-description="Citation for case: United States v. Grunewald">233 F. 2d 556, 579, 581-582</a></span> (Frank, J., dissenting), rev’d, <span class="citation" data-id="9421440"><a href="/opinion/105508/grunewald-v-united-states/" aria-description="Citation for case: Grunewald v. United States">353 U. S. 391</a></span> (1957). We have recently noted that the privilege against self-incrimination — the essential mainstay of our adversary system — is founded on a complex of values, <em>Murphy </em>v. <em>Waterfront Comm’n, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#55" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 55-57, n. 5</a></span> (1964); <em>Tehan </em>v. <em>Shott, </em><span class="citation" data-id="6751647"><a href="/opinion/6862154/tehan-v-united-states-ex-rel-shott/#414" aria-description="Citation for case: Tehan v. United States ex rel. Shott">382 U. S. 406, 414-415, n. 12</a></span> (1966). All these policies point to one overriding thought: the constitutional foundation underlying the privilege is the respect a government — state or federal— must accord to the dignity and integrity of its citizens. To maintain a “fair state-individual balance,” to require the government “to shoulder the entire load,” 8 Wigmore, Evidence 317 (McNaughton rev. 1961), to respect the inviolability of the human personality, our accusatory system of criminal justice demands that the government seeking to punish an individual produce the evidence against him by its own independent labors, rather than by the cruel, simple expedient of compelling it from his own mouth. <em>Chambers </em>v. <em>Florida, </em><span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#235" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227, 235-238</a></span> (1940). In sum, the privilege is fulfilled only when the person is guaranteed the right “to remain silent unless he chooses to speak in the unfettered exercise of his own will.” <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#8" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 8</a></span> (1964).</p>
<p id="b558-7">The question in these cases is whether the privilege is fully applicable during a period of custodial interroga<page-number citation-index="1" label="461">*461</page-number>tion. In this Court, the privilege has consistently been accorded a liberal construction. <em>Albertson </em>v. <em>SACB, </em><span class="citation" data-id="9423096"><a href="/opinion/107110/albertson-v-subversive-activities-control-board/#81" aria-description="Citation for case: Albertson v. Subversive Activities Control Board">382 U. S. 70, 81</a></span> (1965); <em>Hoffman </em>v. <em>United States, </em>341 U. S.. 479, 486 (1951); <em>Arndstein </em>v. <em>McCarthy, </em><span class="citation" data-id="8144042"><a href="/opinion/8182123/arndstein-v-mccarthy/#72" aria-description="Citation for case: Arndstein v. McCarthy">254 U. S. 71, 72-73</a></span> (1920); <em>Counselman </em>v. <em>Hitchock, </em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#562" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 562</a></span> (1892). We are satisfied that all the principles embodied in the privilege apply to informal compulsion exerted by law-enforcement officers during in-custody questioning. An individual swept from familiar surroundings into police custody, surrounded by antagonistic forces, and subjected to the techniques of persuasion described above cannot be otherwise than under compulsion to speak. As a practical matter, the compulsion to speak in the isolated setting of the police station may well be greater than in courts or other official investigations, where there are often impartial observers to guard against intimidation or trickery.<footnotemark>30</footnotemark></p>
<p id="b559-5">This question, in fact, could have been taken as settled in federal courts almost 70 years ago, when, in <em>Bram </em>v. <em>United States, </em><span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#542" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 542</a></span> (1897), this Court held:</p>
<blockquote id="b559-6">“In criminal trials, in the courts of the United States, wherever a question arises whether a confession is incompetent because not voluntary, the issue is controlled by that portion of the Fifth Amendment . . . commanding that no person ‘shall be compelled in any criminal case to be a witness against himself.’ ”</blockquote>
<p id="b559-7">In <em><span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">Bram</a></span>, </em>the Court reviewed the British and American history and case law and set down the Fifth Amendment standard for compulsion which we implement today:</p>
<blockquote id="AVB-">“Much of the confusion which has resulted from the effort to deduce from the adjudged cases what <page-number citation-index="1" label="462">*462</page-number>would be a sufficient quantum of proof to show that a confession was or was not voluntary, has arisen from a misconception of the subject to which the proof must address itself. The rule is not that in order to render a statement admissible the proof must be adequate to establish that the particular communications contained in a statement were voluntarily made, but it must be sufficient to establish that the making of the statement was voluntary; that is to say, that from the causes, which the law treats as legally sufficient to engender in the mind of the accused hope or fear in respect to the crime charged, the accused was not involuntarily impelled to make a statement, when but for the improper influences he would have remained silent. . . .” <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#549" aria-description="Citation for case: Bram v. United States">168 U. S., at 549</a></span>. And see, <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#542" aria-description="Citation for case: Bram v. United States"><em>id., </em>at 542</a></span>.</blockquote>
<p id="b560-6">The Court has adhered to this reasoning. In 1924, Mr. Justice Brandéis wrote for a unanimous Court in reversing a conviction resting on a compelled confession, <em>Wan </em>v. <em>United States, </em><span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/" aria-description="Citation for case: Ziang Sung Wan v. United States">266 U. S. 1</a></span>. He stated:</p>
<blockquote id="b560-7">“In the federal courts, the requisite of voluntariness is not satisfied by establishing merely that the confession was not induced by a promise or a threat. A confession is voluntary in law if, and only if, it was, in fact, voluntarily made. A confession may have been given voluntarily, although it was made to police officers, while in custody, and in answer to an examination conducted by them. But a confession obtained by compulsion must be excluded whatever may have been the character of the compulsion, and whether the compulsion was applied in a judicial proceeding or otherwise. <em>Bram </em>v. <em>United States, </em><span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">168 U. S. 532</a></span>.” <span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/#14" aria-description="Citation for case: Ziang Sung Wan v. United States">266 U. S., at 14-15</a></span>.</blockquote>
<p id="b560-8">In addition to the expansive historical development of the privilege and the sound policies which have nurtured <page-number citation-index="1" label="463">*463</page-number>its evolution, judicial precedent thus clearly establishes its application to incommunicado interrogation. In fact, the Government concedes this point as well established in No. 761, <em>Westover </em>v. <em>United States, </em>stating: “We have no doubt . . . that it is possible for a suspect’s Fifth Amendment right to be violated during in-custody questioning by a law-enforcement officer.” <footnotemark>31</footnotemark></p>
<p id="b561-5">Because of the adoption by Congress of Rule 5 (a) of the Federal Rules of Criminal Procedure, and this Court’s effectuation of that Rule in <em>McNabb </em>v. <em>United States, </em><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U. S. 332</a></span> (1943), and <em>Mallory </em>v. <em>United States, </em><span class="citation" data-id="105545"><a href="/opinion/105545/mallory-v-united-states/" aria-description="Citation for case: Mallory v. United States">354 U. S. 449</a></span> (1957), we have had little occasion in the past quarter century to reach the constitutional issues in dealing with federal interrogations. These supervisory rules, requiring production of an arrested person before a commissioner “without unnecessary delay” and excluding evidence obtained in default of that statutory obligation, were nonetheless responsive to the same considerations of Fifth Amendment policy that unavoidably face us now as to the States. In <em>McNabb, </em><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#343" aria-description="Citation for case: McNabb v. United States">318 U. S., at 343-344</a></span>, and in <em>Mallory, </em><span class="citation" data-id="105545"><a href="/opinion/105545/mallory-v-united-states/#455" aria-description="Citation for case: Mallory v. United States">354 U. S., at 455-456</a></span>, we recognized both the dangers of interrogation and the appropriateness of prophylaxis stemming from the very fact of interrogation itself.<footnotemark>32</footnotemark></p>
<p id="b561-6">Our decision in <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964), necessitates an examination of the scope of the privilege in state cases as well. In <em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Malloy</a></span>, </em>we squarely held the <page-number citation-index="1" label="464">*464</page-number>privilege applicable to the States, and held that the substantive standards underlying the privilege applied with full force to state court proceedings. There, as in <em>Murphy </em>v. <em>Waterfront Comm’n, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52</a></span> (1964), and <em>Griffin </em>v. <em>California, </em><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">380 U. S. 609</a></span> (1965), we applied the existing Fifth Amendment standards to the case before us. Aside from the holding itself, the reasoning in <em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Malloy</a></span> </em>made clear what had already become apparent — that the substantive and procedural safeguards surrounding admissibility of confessions in state cases had become exceedingly exacting, reflecting all the policies embedded in the privilege, 378 U. S., at 7-8.<footnotemark>33</footnotemark> The voluntariness doctrine in the state cases, as <em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Malloy</a></span> </em>indicates, encompasses all interrogation practices which are likely to exert such pressure upon an individual as to disable him from <page-number citation-index="1" label="465">*465</page-number>making a free and rational choice.<footnotemark>34</footnotemark> The implications of this proposition were elaborated in our decision in <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span>, decided one week after <em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Malloy</a></span> </em>applied the privilege to the States.</p>
<p id="b563-5">Our holding there stressed the fact that the police had not advised the defendant of his constitutional privilege to remain silent at the outset of the interrogation, and we drew attention to that fact at several points in the decision, 378 U. S., at 483, 485, 491. This was no isolated factor, but an essential ingredient in our decision. The entire thrust of police interrogation there, as in all the cases today, was to put the defendant in such an emotional state as to impair his capacity for rational judgment. The abdication of the constitutional privilege— the choice on his part to speak to the police — was not made knowingly or competently because of the failure to apprise him of his rights; the compelling atmosphere of the in-custody interrogation, and not an independent decision on his part, caused the defendant to speak.</p>
<p id="b563-6">A different phase of the <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>decision was significant in its attention to the absence of counsel during the questioning. There, as in the cases today, we sought a protective device to dispel the compelling atmosphere of the interrogation. In <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>, </em>however, the police did not relieve the defendant of the anxieties which they had created in the interrogation rooms. Rather, they denied his request for the assistance of counsel, 378 U. S., at 481, 488, 491.<footnotemark>35</footnotemark> This heightened his dilemma, and <page-number citation-index="1" label="466">*466</page-number>made his later statements the product of this compulsion. Cf. <em>Haynes </em>v. <em>Washington, </em><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#514" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503, 514</a></span> (1963). The denial of the defendant’s request for his attorney thus undermined his ability to exercise the privilege— to remain silent if he chose or to speak without any intimidation, blatant or subtle. The presence of counsel, in all the cases before us today, would be the adequate protective device necessary to make the process of police interrogation conform to the dictates of the privilege. His presence would insure that statements made in the government-established atmosphere are not the product of compulsion.</p>
<p id="b564-6">It was in this manner that <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>explicated another facet of the pre-trial privilege, noted in many of the Court’s prior decisions: the protection of rights at trial.<footnotemark>36</footnotemark> That counsel is present when statements are taken from an individual during interrogation obviously enhances the integrity of the fact-finding processes in court. The presence of an attorney, and the warnings delivered to the individual, enable the defendant under otherwise compelling circumstances to tell his story without fear, effectively, and in a way that eliminates the evils in the interrogation process. Without the protections flowing from adequate warnings and the rights of counsel, “all the careful safeguards erected around the giving of testimony, whether by an accused or any other witness, would become empty formalities in a procedure where the most compelling possible evidence of guilt, a confession, would have already been obtained at the unsupervised pleasure of the police.” <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#685" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 685</a></span> (1961) (Harlan, J., dissenting). Cf. <em>Pointer </em>v. <em>Texas, </em><span class="citation" data-id="9422988"><a href="/opinion/107014/pointer-v-texas/" aria-description="Citation for case: Pointer v. Texas">380 U. S. 400</a></span> (1965).</p>
<p id="b565-4"><page-number citation-index="1" label="467">*467</page-number>III.</p>
<p id="b565-5">Today, then, there can be no doubt that the Fifth Amendment privilege is available outside of criminal court proceedings and serves to protect persons in all settings in which their freedom of action is curtailed in any significant way from being compelled to incriminate themselves. We have concluded that without proper safeguards the process of in-custody interrogation of persons suspected or accused of crime contains inherently compelling pressures which work to undermine the individual’s will to resist and to compel him to speak where he would not otherwise do so freely. In order, to combat these pressures and to permit a full opportunity to exercise the privilege against self-incrimination, the accused must be adequately and effectively apprised of his rights and the exercise of those rights must be fully honored.</p>
<p id="b565-6">It is impossible for us to foresee the potential alternatives for protecting the privilege which might be devised by Congress or the States in the exercise of their creative rule-making capacities. Therefore we cannot say that the Constitution necessarily requires adherence to any particular solution for the inherent compulsions of the interrogation process as it is presently conducted. Our decision in no way creates a constitutional straitjacket which will handicap sound efforts at reform, nor is it intended to have this effect. We encourage Congress and the States to continue their laudable search for increasingly effective ways of protecting the rights of the individual while promoting efficient enforcement of our criminal laws. However, unless we are shown other procedures which are at least as effective in apprising accused persons of their right of silence and in assuring a continuous opportunity to exercise it, the following safeguards must be observed.</p>
<p id="b565-7">At the outset, if a person in custody is to be subjected to interrogation, he must first be informed in clear and <page-number citation-index="1" label="468">*468</page-number>unequivocal terms that he has the right to remain silent. For those unaware of the privilege, the warning is needed simply to make them aware of it — the threshold requirement for an intelligent decision as to its exercise. More important, such a warning is an absolute prerequisite in overcoming the inherent pressures of the interrogation atmosphere. It is not just the subnormal or woefully ignorant who succumb to an interrogator’s imprecations, whether implied or expressly stated, that the interrogation will continue until a confession is obtained or that silence in the face of accusation is itself damning and will bode ill when presented to a jury.<footnotemark>37</footnotemark> Further, the warning will show the individual that his interrogators are prepared to recognize his privilege should he choose to exercise it.</p>
<p id="b566-6">The Fifth Amendment privilege is so fundamental to our system of constitutional rule and the expedient of giving an adequate warning as to the availability of the privilege so simple, we will not pause to inquire in individual cases whether the defendant was aware of his rights without a warning being given. Assessments of the knowledge the defendant possessed, based on infor<page-number citation-index="1" label="469">*469</page-number>mation as to his age, education, intelligence, or prior contact with authorities, can never be more than speculation; <footnotemark>38</footnotemark> a warning is a clearcut fact. More important, whatever the background of the person interrogated, a warning at the time of the interrogation is indispensable to overcome its pressures and to insure that the individual knows he is free to exercise the privilege at that point in time.</p>
<p id="b567-4">The warning of the right to remain silent must be accompanied by the explanation that anything said can and will be used against the individual in court. This warning is needed in order to make him aware not only of the privilege, but also of the consequences of forgoing it. It is only through an awareness of these consequences that there can be any assurance of real understanding and intelligent exercise of the privilege. Moreover, this warning may serve to make the individual more acutely aware that he is faced with a phase of the adversary system — -that he is not in the presence of persons acting solely in his interest.</p>
<p id="b567-5">The circumstances surrounding in-custody interrogation can operate very quickly to overbear the will of one merely made aware of his privilege by his interrogators. Therefore, the right to have counsel present at the interrogation is indispensable to the protection of the Fifth Amendment privilege under the system we delineate today. Our aim is to assure that the individual’s right to choose between silence and speech remains unfettered throughout the interrogation process. A once-stated warning, delivered by those who will conduct the interrogation, cannot itself suffice to that end among those who most require knowledge of their rights. A mere <page-number citation-index="1" label="470">*470</page-number>warning given by the interrogators is not alone sufficient to accomplish that end. Prosecutors themselves claim that the admonishment of the right to remain silent without more “will benefit only the recidivist and the professional.” Brief for the National District Attorneys Association as <em>amicus curiae, </em>p. 14. Even preliminary advice given to the accused by his own attorney can be swiftly overcome by the secret interrogation process. Cf. <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#485" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478, 485, n. 5</a></span>. Thus, the need for counsel to protect the Fifth Amendment privilege comprehends not merely a right to consult with counsel prior to questioning, but also to have counsel present during any questioning if the defendant so desires.</p>
<p id="b568-6">The presence of counsel at the interrogation may serve several significant subsidiary functions as well. If the accused decides to talk to his interrogators, the assistance of counsel can mitigate the dangers of untrustworthiness. With a lawyer present the likelihood that the police will practice coercion is reduced, and if coercion is nevertheless exercised the lawyer can testify to it in court. The presence of a lawyer can also help to guarantee that the accused gives a fully accurate statement to the police and that the statement is rightly reported by the prosecution at trial. See <em>Crooker </em>v. <em>California, </em><span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/#443" aria-description="Citation for case: Crooker v. California">357 U. S. 433, 443-448</a></span> (1958) (Douglas, J., dissenting).</p>
<p id="b568-7">An individual need not make a pre-interrogation request for a lawyer. While such request affirmatively secures his right to have one, his failure to ask for a lawyer does not constitute a waiver. No effective waiver of the right to counsel during interrogation can be recognized unless specifically made after the warnings we here delineate have been given. The accused who does not know his rights and therefore does not make a request <page-number citation-index="1" label="471">*471</page-number>may be the person who most needs counsel. As the California Supreme Court has aptly put it:</p>
<blockquote id="b569-5">“Finally, we must recognize that the imposition of the requirement for the request would discriminate against the defendant who does not know his rights. The defendant who does not ask for counsel is the very defendant who most needs counsel. We cannot penalize a defendant who, not understanding his constitutional rights, does not make the formal request and by such failure demonstrates his helplessness. To require the request would be to favor the defendant whose sophistication or status had fortuitously prompted him to make it.” <em>People </em>v. <em>Dorado, </em><span class="citation" data-id="9549155"><a href="/opinion/1177555/people-v-dorado/#351" aria-description="Citation for case: People v. Dorado">62 Cal. 2d 338, 351</a></span>, <span class="citation" data-id="9549155"><a href="/opinion/1177555/people-v-dorado/#369" aria-description="Citation for case: People v. Dorado">398 P. 2d 361, 369-370</a></span>, <span class="citation" data-id="9549155"><a href="/opinion/1177555/people-v-dorado/#177" aria-description="Citation for case: People v. Dorado">42 Cal. Rptr. 169, 177-178</a></span> (1965) (Tobriner, J.).</blockquote>
<p id="b569-6">In <em>Carnley </em>v. <em>Cochran, </em><span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/#513" aria-description="Citation for case: Carnley v. Cochran">369 U. S. 506, 513</a></span> (1962), we stated: “[I]t is settled that where the assistance of counsel is a constitutional requisite, the right to be furnished counsel does not depend on a request.” This proposition applies with equal force in the context of providing counsel to protect an accused’s Fifth Amendment privilege in the face of interrogation.<footnotemark>39</footnotemark> Although the role of counsel at trial differs from the role during interrogation, the differences are not relevant to the question whether a request is a prerequisite.</p>
<p id="b569-7">Accordingly we hold that an individual held for interrogation must be clearly informed that he has the right to consult with a lawyer and to have the lawyer with him during interrogation under the system for protecting the privilege we delineate today. As with the warnings of the right to remain silent and that anything stated can be used in evidence against him, this warning is an absolute prerequisite to interrogation. No amount of <page-number citation-index="1" label="472">*472</page-number>circumstantial evidence that the person may have been aware of this right will suffice to stand in its stead. Only through such a warning is there ascertainable assurance that the accused was aware of this right.</p>
<p id="b570-6">If an individual indicates that he wishes the assistance of counsel before any interrogation occurs, the authorities cannot rationally ignore or deny his request on the basis that the individual does not have or cannot afford a retained attorney. The financial ability of the individual has no relationship to the scope of the rights involved here. The privilege against self-incrimination secured by the Constitution applies to all individuals. The need for counsel in order to protect the privilege exists for the indigent as well as the affluent. In fact, were we to limit these constitutional rights to those who can retain an attorney, our decisions today would be of little significance. The cases before us as well as the vast majority of confession cases with which we have dealt in the past involve those unable to retain counsel.<footnotemark>40</footnotemark> While authorities are not required to relieve the accused of his poverty, they have the obligation not to take advantage of indigence in the administration of justice.<footnotemark>41</footnotemark> Denial <page-number citation-index="1" label="473">*473</page-number>of counsel to the indigent at the time of interrogation while allowing an attorney to those who can afford one would be no more supportable by reason or logic than the similar situation at trial and on appeal struck down in <em>Gideon </em>v. <em>Wainwright, </em><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span> (1963), and <em>Douglas </em>v. <em>California, </em><span class="citation" data-id="9422548"><a href="/opinion/106546/douglas-v-california/" aria-description="Citation for case: Douglas v. California">372 U. S. 353</a></span> (1963).</p>
<p id="b571-5">In order fully to apprise a person interrogated of the extent of his rights under this system then, it is necessary to warn him not only that he has the right to consult with an attorney, but also that if he is indigent a lawyer will be appointed to represent him. Without this additional warning, the admonition of the right to consult with counsel would often be understood as meaning only that he can consult with a lawyer if he has one or has the funds to obtain one. The warning of a right to counsel would be hollow if not couched in terms that would convey to the indigent — the person most often subjected to interrogation — the knowledge that he too has a right to have counsel present.<footnotemark>42</footnotemark> As with the warnings of the right to remain silent and of the general right to counsel, only by effective and express explanation to the indigent of this right can there be assurance that he was truly in a position to exercise it.<footnotemark>43</footnotemark></p>
<p id="b571-6">Once warnings have been given, the subsequent procedure is clear. If the individual indicates in any man-<page-number citation-index="1" label="474">*474</page-number>hén, at any time prior to or during questioning, that he wishes to remain silent, the interrogation must cease.<footnotemark>44</footnotemark> At this point he has shown that he intends to exercise his Fifth Amendment privilege; any statement taken after the person invokes his privilege cannot be other than the product of compulsion, subtle or otherwise. Without the right to cut off questioning, the setting of in-custody interrogation operates on the individual to overcome free choice in producing a statement after the privilege has been once invoked. If the individual states that he wants an attorney, the interrogation must cease until an attorney is present. At that time, the individual must have an opportunity to confer with the attorney and to have him present during any subsequent questioning. If the individual cannot obtain an attorney and he indicates that he wants one before speaking to police, they must respect his decision to remain silent.</p>
<p id="b572-4">This does not mean, as some have suggested, that each police station must have a “station house lawyer” present at all times to advise prisoners. It does mean, however, that if police propose to interrogate a person they must make known to him that he is entitled to a lawyer and that if he cannot afford one, a lawyer will be provided for him prior to any interrogation. If authorities conclude that they will not provide counsel during a reasonable period of time in which investigation in the field is carried out, they may refrain from doing so without violating the person’s Fifth Amendment privilege so long as they do not question him during that time.</p>
<p id="b573-4"><page-number citation-index="1" label="475">*475</page-number>If the interrogation continues without the presence of an attorney and a statement is taken, a heavy burden rests on the government to demonstrate that the defendant knowingly and intelligently waived his privilege against self-incrimination and his right to retained or appointed counsel. <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#490" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478, 490, n. 14</a></span>. This Court has always set high standards of proof for the waiver of constitutional rights, <em>Johnson </em>v. <em>Zerbst, </em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458</a></span> (1938), and we re-assert these standards as applied to in-custody interrogation. Since the State is responsible for establishing the isolated circumstances under which the interrogation takes place and has the only means of making available corroborated evidence of warnings given during incommunicado interrogation, the burden is rightly on its shoulders.</p>
<p id="b573-5">An express statement that the individual is willing to make a statement and does not want an attorney followed closely by a statement could constitute a waiver. But a valid waiver will not be presumed simply from the silence of the accused after warnings are given or simply from the fact that a confession was in fact eventually obtained. A statement we made in <em>Carnley </em>v. <em>Cochran, </em><span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/#516" aria-description="Citation for case: Carnley v. Cochran">369 U. S. 506, 516</a></span> (1962), is applicable here:</p>
<blockquote id="b573-6">“Presuming waiver from a silent record is impermissible. The record must show, or there must be an allegation and evidence which show, that an accused was offered counsel but intelligently and understanding^ rejected the offer. Anything less is not waiver.”</blockquote>
<p id="b573-7">See also <em>Glasser </em>v. <em>United States, </em><span class="citation" data-id="103597"><a href="/opinion/103597/glasser-v-united-states/" aria-description="Citation for case: Glasser v. United States">315 U. S. 60</a></span> (1942). Moreover, where in-custody interrogation is involved, there is no room for the contention that the privilege is waived if the individual answers some questions or gives <page-number citation-index="1" label="476">*476</page-number>some information on his own prior to invoking his right to remain silent when interrogated.<footnotemark>45</footnotemark></p>
<p id="b574-5">Whatever the testimony of the authorities as to waiver of rights by an accused, the fact of lengthy interrogation or incommunicado incarceration before a statement is made is strong evidence that the accused did not validly waive his rights. In these circumstances the fact that the individual eventually made a statement is consistent with the conclusion that the compelling influence of the interrogation finally forced him to do so. It is inconsistent with any notion of a voluntary relinquishment of the privilege. Moreover, any evidence that the accused was threatened, tricked, or cajoled into a waiver will, of course, show that the defendant did not voluntarily waive his privilege. The requirement of warnings and waiver of rights is a fundamental with respect to the Fifth Amendment privilege and not simply a preliminary ritual to existing methods of interrogation.</p>
<p id="b574-6">The warnings required and the waiver necessary in accordance with our opinion today are, in the absence of a fully effective equivalent, prerequisites to the admissibility of any statement made by a defendant. No distinction can be drawn between statements which are direct confessions and statements which amount to “admissions” of part or all of an offense. The privilege against self-incrimination protects the individual from being compelled to incriminate himself in any manner; it does not distinguish degrees of incrimination. Sim<page-number citation-index="1" label="477">*477</page-number>ilarly, for precisely the same reason, no distinction may be drawn between inculpatory statements and statements alleged to be merely “exculpatory.” If a statement made were in fact truly exculpatory it would, of course, never be used by the prosecution. In fact, statements merely intended to be exculpatory by the defendant are often used to impeach his testimony at trial or to demonstrate untruths in the statement given under interrogation and thus to prove guilt by implication. These statements are incriminating in any meaningful sense of the word and may not be used without the full warnings and effective waiver required for any other statement. In <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>itself, the defendant fully intended his accusation of another as the slayer to be exculpatory as to himself.</p>
<p id="b575-5">The principles announced today deal with the protection which must be given to the privilege against self-incrimination when the individual is first subjected to police interrogation while in custody at the station or otherwise deprived of his freedom of action in any significant way. It is at this point that our adversary system of criminal proceedings commences, distinguishing itself at the outset from the inquisitorial system recognized in some countries. Under the system of warnings we delineate today or under any other system which may be devised and found effective, the safeguards to be erected about the privilege must come into play at this point.</p>
<p id="b575-6">Our decision is not intended to hamper the traditional function of police officers in investigating crime. See <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#492" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478, 492</a></span>. When an individual is in custody on probable cause, the police may, of course, seek out evidence in the field to be used at trial against him. Such investigation may include inquiry of persons not under restraint. General on-the-scene questioning as to facts surrounding a crime or other general questioning of citizens in the fact-finding process is not affected by our holding. It is an act of <page-number citation-index="1" label="478">*478</page-number>responsible citizenship for individuals to give whatever information they may have to aid in law enforcement. In such situations the compelling atmosphere inherent in the process of in-custody interrogation is not necessarily present.<footnotemark>46</footnotemark></p>
<p id="b576-6">In dealing with statements obtained through interrogation, we do not purport to find all confessions inadmissible. Confessions remain a proper element in. law enforcement. Any statement given freely and voluntarily without any compelling influences is, of course, admissible in evidence. The fundamental import of the privilege while an individual is in custody is not whether he is allowed to talk to the police without the benefit of warnings and counsel, but whether he can be interrogated. There is no requirement that police, stop a person who enters a police station and states that he wishes to confess to a crime,<footnotemark>47</footnotemark> or a person who calls the police to offer a confession or any other statement he desires to make. Volunteered statements of any kind are not barred by the Fifth Amendment and their admissibility is not affected by our holding today. '</p>
<p id="b576-7">To summarize, we hold that when an individual is taken into custody or otherwise deprived of his freedom by the authorities in any significant way and is subjected to questioning, the privilege against self-incrimination is jeopardized. Procedural safeguards must be employed to <page-number citation-index="1" label="479">*479</page-number>protect the privilege, and unless other fully effective means are adopted to notify the person of his right of silence and to assure that the exercise of the right will be scrupulously honored, the following measures are required. He must be warned prior to any questioning that he has the right to remain silent, that anything he says can be used against him in a court of law, that he has the right to the presence of an attorney, and that if he cannot afford an attorney one will be appointed for him prior to any questioning if he so desires. Opportunity to exercise these rights must be afforded to him throughout the interrogation. After such warnings have been given, and such opportunity afforded him, the individual may knowingly and intelligently waive these rights and agree to answer questions or make a statement. But unless and until such warnings and waiver are demonstrated by the prosecution at trial, no evidence obtained as a result of interrogation can be used against him.<footnotemark>48</footnotemark></p>
<p id="b577-5">IV.</p>
<p id="b577-6">A recurrent argument made in these cases is that' society’s need for interrogation outweighs the privilege. This argument is not unfamiliar to this Court. See, <em>e. g., Chambers </em>v. <em>Florida, </em><span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#240" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227, 240-241</a></span> (1940). The whole thrust of our foregoing discussion demonstrates that the Constitution has prescribed the rights of the individual when confronted with the power of government when it provided in the Fifth Amendment that an individual cannot be compelled to be a witness against himself. That right cannot be abridged. As Mr. Justice Brandéis once observed:</p>
<blockquote id="b577-7">“Decency, security and liberty alike demand that government officials shall be subjected to the same <page-number citation-index="1" label="480">*480</page-number>rules of conduct that are commands to the citizen. In a government of laws, existence of the government will be imperilled if it fails to observe the law scrupulously. Our Government is the potent, the omnipresent teacher. For good or' for ill, it teaches the whole people by its example. Crime is contagious. If the Government becomes a lawbreaker, it breeds contempt for law; it invites every man to become a law unto himself; it invites anarchy. To declare that in the administration of the criminal law the end justifies the means . . . would bring terrible retribution. Against that pernicious doctrine this Court should resolutely set its face.” <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#485" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 485</a></span> (1928) (dissenting opinion) ,<footnotemark>49</footnotemark></blockquote>
<p id="b578-5">In this connection, one of our country’s distinguished jurists has pointed out: “The quality of a nation’s civilization can be largely measured by the methods it uses in the enforcement of its criminal law.” <footnotemark>50</footnotemark></p>
<p id="b578-6">If the individual desires to exercise his privilege, he has the right to do so. This is not for the authorities to decide. An attorney may advise his client not to talk to police until he has had an opportunity to investigate the case, or he may wish to be present with his client during any police questioning. In doing so an attorney is merely exercising the good professional judgment he has been, taught. This is not cause for considering the attorney a menace to law enforcement. He is merely carrying out what he is sworn to do under his oáth— to protect to the extent of his ability the rights of his <page-number citation-index="1" label="481">*481</page-number>client. In fulfilling this responsibility the attorney plays a vital role in the administration of criminal justice under our Constitution.</p>
<p id="b579-5">In announcing these principles, we are not unmindful of the burdens which law enforcement officials must bear, often under trying circumstances. We also fully recognize the obligation of all citizens to aid in enforcing the criminal laws. This- Court, while protecting individual rights, has always given ample latitude to law enforcement agencies in the legitimate exercise of their duties. The limits we have placed on the interrogation process should not constitute an undue interference with a proper system of law enforcement. As we have noted, our decision does not in any way preclude police from carrying out their traditional investigatory functions. Although confessions may play an important role in some convictions, the cases before us present graphic examples of the overstatement of the “need” for confessions. In each case authorities conducted interrogations ranging up to five days in duration despite the presence, through standard investigating practices, of considerable evidence against each defendant.<footnotemark>51</footnotemark> Further examples are chronicled in our prior cases. See, <em>e. g., Haynes </em>v. <em>Washington, </em><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#518" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503, 518-519</a></span> (1963); <em>Rogers </em>v. <em>Richmond, </em><span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#541" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 541</a></span> (1961); <em>Malinski </em>v. <em>New York, </em><span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#402" aria-description="Citation for case: Malinski v. New York">324 U. S. 401, 402</a></span> (1945).<footnotemark>52</footnotemark></p>
<p id="b580-4"><page-number citation-index="1" label="482">*482</page-number>It is also urged that an unfettered right to detention for interrogation should be allowed because it will often redound to the benefit of the person questioned. When police inquiry determines that there is no reason to believe that the person has committed any crime, it is said, he will be released without need for further formal procedures. The person who has committed no offense, however, will be better able to clear himself after warnings with counsel present than without. It can be assumed that in such circumstances a lawyer would advise his client to talk freely to police in order to clear himself.</p>
<p id="b580-5">Custodial interrogation, by contrast, does not necessarily afford the innocent an opportunity to clear themselves. A serious consequence of the present practice of the interrogation alleged to be beneficial for the innocent is that many arrests “for investigation” subject large numbers of innocent persons to detention and interrogation. In one of the cases before us, No. 584, <em>California </em>v. <em>Stewart, </em>police held four persons, who were in the defendant’s house at the time of the arrest, in jail for five days until defendant confessed. At that time they were finally released. Police stated that there was “no evidence to connect them with any crime.” Available statistics on the extent of this practice where it is condoned indicate that these four are far from alone in being subjected to arrest, prolonged detention, and interrogation without the requisite probable cause.<footnotemark>53</footnotemark></p>
<p id="b581-5"><page-number citation-index="1" label="483">*483</page-number>Over the years the Federal Bureau of Investigation has compiled an exemplary record of effective law enforcement while advising any suspect or arrested person, at the outset of an interview, that he is not required to make a statement, that any statement may be used against him in court, that the individual may obtain the services of an attorney of his own choice and, more recently, that he has a right to free counsel if he is unable to pay.<footnotemark>54</footnotemark> A letter received from the Solicitor General in response to a question from the Bench makes it clear that the present pattern of warnings and respect for the <page-number citation-index="1" label="484">*484</page-number>rights of the individual followed as a practice by the FBI is consistent with the procedure which we delineate today. It states:</p>
<blockquote id="b582-4">“At the oral argument of the above cause, Mr. Justice Fortas asked whether I could provide certain information as to the practices followed by the Federal Bureau of Investigation. I have directed these questions to the attention of the Director of the Federal Bureau of Investigation and am submitting herewith a statement of the questions and of the answers which we have received.</blockquote>
<blockquote id="b582-5">“ ‘(1) When an individual is interviewed by agents of the Bureau, what warning is given to him?</blockquote>
<blockquote id="b582-6">“ 'The standard warning long given by Special Agents of the FBI to both suspects and persons under arrest is that the person has a right to say nothing and a right to counsel, and that any statement he does make may be used against him in court. Examples of this warning are to be found in the <em>Westover </em>case at <span class="citation" data-id="267168"><a href="/opinion/267168/carl-calvin-westover-v-united-states/" aria-description="Citation for case: Carl Calvin Westover v. United States">342 F. 2d 684</a></span> (1965), and <em>Jackson </em>v. <em>U. S., </em><span class="citation" data-id="9450314"><a href="/opinion/265586/john-w-jackson-jr-v-united-states/" aria-description="Citation for case: John W. Jackson, Jr. v. United States">337 F. 2d 136</a></span> (1964), cert. den. <span class="citation multiple-matches"><a href="/c/U.%20S./380/935/">380 U. S. 935</a></span>.</blockquote>
<blockquote id="b582-7">“ 'After passage of the Criminal Justice Act of 1964, which provides free counsel for Federal defendants unable to pay, we added to our instructions to Special Agents the requirement that any person who is under arrest for an offense under FBI jurisdiction, or whose arrest is contemplated following the interview, must also be advised of his right to free counsel if he is unable to pay, and the fact that such counsel will be assigned by the Judge. At the same time, we broadened the right to counsel warn<page-number citation-index="1" label="485">*485</page-number>ing to read counsel of his own choice, or anyone else with whom he might wish to speak.</blockquote>
<blockquote id="b583-5">“ ‘(2) When is the warning given?</blockquote>
<blockquote id="b583-6">“ ‘The FBI warning is given to a suspect at the very outset of the interview, as shown in the <em>West-over </em>case, cited above. The warning may be given to a person arrested as soon as practicable after the arrest, as shown in the <em>Jackson </em>case, also cited above, and in <em>U. S. </em>v. <em>Konigsberg, </em><span class="citation multiple-matches"><a href="/c/F.%202d/336/844/">336 F. 2d 844</a></span> (1964), cert. den. <span class="citation" data-id="8951108"><a href="/opinion/8959978/konigsberg-v-united-states/" aria-description="Citation for case: Konigsberg v. United States">379 U. S. 933</a></span>, but in any event it must precede the interview with the person for a confession or admission of his own guilt.</blockquote>
<blockquote id="b583-7">“ ‘(3) What is the Bureau’s practice in the event that (a) the individual requests counsel and (b) counsel appears?</blockquote>
<blockquote id="b583-8">“ ‘When the person who has been warned of his right to counsel decides that he wishes to consult with counsel before making a statement, the interview is terminated at that point, <em>Shultz </em>v. <em>U. S., </em><span class="citation" data-id="269239"><a href="/opinion/269239/clayman-clifford-shultz-v-united-states/" aria-description="Citation for case: Clayman Clifford Shultz v. United States">351 F. 2d 287</a></span> (1965). It may be continued, however, as to all matters <em>other </em>than the person’s own guilt or innocence. If he is indecisive in his request for counsel, there may be some question on whether he did or did not waive counsel. Situations of this kind must necessarily be left to the judgment of the interviewing Agent. For example, in <em>Hiram </em>v. <em>U. S., </em><span class="citation" data-id="270022"><a href="/opinion/270022/randolph-k-hiram-v-united-states/" aria-description="Citation for case: Randolph K. Hiram v. United States">354 F. 2d 4</a></span> (1965), the Agent’s conclusion that the person arrested had waived his right to counsel was upheld by the courts.</blockquote>
<blockquote id="b583-9">“ ‘A person being interviewed and desiring to consult counsel by telephone must be permitted to do so, as shown in <em>Caldwell </em>v. <em>U. S., </em><span class="citation" data-id="269286"><a href="/opinion/269286/william-ambrose-caldwell-v-united-states/" aria-description="Citation for case: William Ambrose Caldwell v. United States">351 F. 2d 459</a></span> (1965). When counsel appears in person, he is permitted to confer with his client in private.</blockquote>
<blockquote id="b584-5"><page-number citation-index="1" label="486">*486</page-number>“ ‘(4) What is the Bureau’s practice if the individual requests counsel, but cannot afford to retain an attorney?</blockquote>
<blockquote id="b584-6">. “ Tf any person being interviewed after warning of counsel decides that he wishes to consult with counsel before proceeding further the interview is terminated, as shown above. FBI Agents do not pass judgment on the ability of the person to pay for counsel. They do, however, advise those who have been arrested for an offense under FBI jurisdiction, or whose arrest is contemplated following the interview, of a right to free counsel <em>if </em>they are unable to pay, and the availability of such counsel from the Judge.’ ”<footnotemark>55</footnotemark></blockquote>
<p id="b584-7">The practice of the FBI can readily be emulated by state and local enforcement agencies. The argument that the FBI deals with different crimes than are dealt with by state authorities does not mitigate the significance of the FBI experience.<footnotemark>56</footnotemark></p>
<p id="b584-8">The experience in some other countries also suggests that the danger to law enforcement in curbs on interrogation is overplayed. The English procedure since 1912 under the Judges’ Rules is significant. As recently <page-number citation-index="1" label="487">*487</page-number>strengthened, the Rules require that a cautionary warning be given an accused by a police officer as soon as he has evidence that affords reasonable grounds for suspicion; they also require that any statement made be given by the accused without questioning by police.<footnotemark>57</footnotemark> <page-number citation-index="1" label="488">*488</page-number>The right of the individual to consult with an attorney during this period is expressly recognized.<footnotemark>58</footnotemark></p>
<p id="b586-6">The safeguards present under Scottish law may be even greater than in England. Scottish judicial decisions bar use in evidence of most confessions obtained through police interrogation.<footnotemark>59</footnotemark> In India, confessions made to police not in the presence of a magistrate have been ex-<page-number citation-index="1" label="489">*489</page-number>eluded by rule of evidence since 1872, at a time when it operated under British law.<footnotemark>60</footnotemark> Identical provisions appear in the Evidence Ordinance of Ceylon, enacted in 1895.<footnotemark>61</footnotemark> Similarly, in our country the Uniform Code of Military Justice has long provided that no suspect may be interrogated without first being warned of his right not to make a statement and that any statement he makes may be used against him.<footnotemark>62</footnotemark> Denial of the right to consult counsel during interrogation has also been proscribed by military tribunals.<footnotemark>63</footnotemark> There appears to have been no marked detrimental effect on criminal law enforcement in these jurisdictions as a result of these rules. Conditions of law enforcement in our country are sufficiently similar to permit reference to this experience as assurance that lawlessness will not result from warning an individual of his rights or allowing him to exercise them. Moreover, it is consistent with our legal system that we give at least as much protection to these rights as is given in the jurisdictions described. We deal in our country with rights grounded in a specific requirement of the Fifth Amendment of the Constitution, <page-number citation-index="1" label="490">*490</page-number>whereas other jurisdictions arrived at their conclusions on the basis of principles of justice not so specifically defined.<footnotemark>64</footnotemark></p>
<p id="b588-6">It is also urged upon us that we withhold decision on this issue until state legislative bodies and advisory groups have had an opportunity to deal with these problems by rule making.<footnotemark>65</footnotemark> We have already pointed out that the Constitution does not require any specific code of procedures for protecting the privilege against self-incrimination during custodial interrogation. Congress and the States are free to develop their own safeguards for the privilege, so long as they are fully as effective as those described above in informing accused persons of their right of silence and in affording a continuous opportunity to exercise it. In any event, however, the issues presented are of constitutional dimensions and must be determined by the courts. The admissibility of a statement in the face of a claim that it was obtained in violation of the defendant’s constitutional rights is an issue the resolution of which has long since been undertaken by this Court. See <em>Hopt </em>v. <em>Utah, </em><span class="citation" data-id="91057"><a href="/opinion/91057/hopt-v-people-of-territory-of-utah/" aria-description="Citation for case: Hopt v. People of Territory of Utah">110 U. S. 574</a></span> (1884). Judicial solutions to problems of constitutional dimension have evolved decade by decade. As courts have been presented with the need to enforce constitutional rights, they have found means of doing so. That was our responsibility when <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>was before us and it is our <page-number citation-index="1" label="491">*491</page-number>responsibility today. Where rights secured by the Constitution are involved, there can be no rule making or legislation which would abrogate them.</p>
<p id="b589-5">V.</p>
<p id="b589-6">Because of the nature of the problem and because of its recurrent significance in numerous cases, we have to this point discussed the relationship of the Fifth Amendment privilege to police interrogation without specific concentration on the facts of the cases before us. We turn now to these facts to consider the application to these cases of the constitutional principles discussed above. In each instance, we have concluded that statements were obtained from the defendant under circumstances that did not meet constitutional standards for protection of the privilege.</p>
<p id="b589-7">No. 759. <em>Miranda </em>v. <em>Arizona.</em></p>
<p id="b589-8">On March 13, 1963, petitioner, Ernesto Miranda, was arrested at his home and taken in custody to a Phoenix police station. He was there identified by the complaining witness. The police then took him to “Interrogation Room No. <em>2” </em>of the detective bureau. There he was questioned by two police officers. The officers admitted at trial that Miranda was not advised that he had a right to have an attorney present.<footnotemark>66</footnotemark> Two hours later, the <page-number citation-index="1" label="492">*492</page-number>officers emerged from the interrogation room with a written confession signed by Miranda. At the top of the statement was a typed paragraph stating that the confession was made voluntarily, without threats or promises of immunity and “with full knowledge of my legal rights, understanding any statement I make may be used against me.” <footnotemark>67</footnotemark></p>
<p id="b590-6">At his trial before a jury, the written confession was admitted into evidence over the objection of defense counsel, and the officers testified to the prior oral confession made by Miranda during the interrogation. Miranda was found guilty of kidnapping and rape. He was sentenced to 20 to 30 years’ imprisonment on each count, the sentences to run concurrently. On appeal, the Supreme Court of Arizona held that Miranda’s constitutional rights were not violated in obtaining the confession and affirmed the conviction. <span class="citation" data-id="1297557"><a href="/opinion/1297557/state-v-miranda/" aria-description="Citation for case: State v. Miranda">98 Ariz. 18</a></span>, <span class="citation" data-id="1297557"><a href="/opinion/1297557/state-v-miranda/" aria-description="Citation for case: State v. Miranda">401 P. 2d 721</a></span>. In reaching its decision, the court emphasized heavily the fact that Miranda did not specifically request counsel.</p>
<p id="b590-7">We reverse. From the testimony of the officers and by the admission of respondent, it is clear that Miranda was not in any way apprised of his right to consult with an attorney and to have one present during the interrogation, nor was his right not to be compelled to incriminate himself effectively protected in any other manner. Without these warnings the statements were inadmissible. The mere fact that he signed a statement which contained a typed-in clause stating that he had “full knowledge” of his “legal rights” does not approach the knowing and intelligent waiver required to relinquish constitutional rights. Cf. <em>Haynes </em>v. <em>Washington, </em><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#512" aria-description="Citation for case: Haynes v. Washington">373 U. S. <page-number citation-index="1" label="493">*493</page-number>503, 512-513</a></span> (1963); <em>Haley </em>v. <em>Ohio, </em><span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/#601" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596, 601</a></span> (1948) (opinion of Mr. Justice Douglas).</p>
<p id="b591-5">No. 760. <em>Vignera </em>v. <em><span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">New York</a></span>.</em></p>
<p id="b591-6">Petitioner, Michael Vignera, was picked up by New York police on October 14, 1960, in connection with the robbery three days earlier of a Brooklyn dress shop. They took him to the 17th Detective Squad headquarters in Manhattan. Sometime thereafter he was taken to the 66th Detective Squad. There a detective questioned Vignera with respect to the robbery. Vignera orally admitted the robbery to the detective. The detective was asked on cross-examination at trial by defense counsel whether Vignera was warned of his right to counsel before being interrogated. The prosecution objected to the question and the trial judge sustained the objection. Thus, the defense was precluded from making any showing that warnings had not been given. While at the 66th Detective Squad, Vignera was identified by the s'tore owner and a saleslady as the man who robbed the dress shop. At about 3 p. m. he was formally arrested. The police then transported him to still another station, the 70th Precinct in Brooklyn, “for detention.” At 11 p. m. Vignera was questioned by an assistant district attorney in the presence of a hearing reporter who transcribed the questions and Vignera’s answers. This verbatim account of these proceedings contains no statement of any warnings given by the assistant district attorney. At Vignera’s trial on a charge of first degree robbery, the detective testified as to the oral confession. The transcription of the statement taken was also introduced in evidence. At the conclusion of the testimony, the trial judge charged the jury in part as follows:</p>
<blockquote id="b591-7">“The law doesn’t say that the confession is void or invalidated because the police officer didn’t advise the defendant as to his rights. Did you hear what <page-number citation-index="1" label="494">*494</page-number>I said? I am telling you what the law of the State of New York is.”</blockquote>
<p id="b592-6">Yignera was found guilty of first degree robbery. He was subsequently adjudged a third-felony offender and sentenced to 30 to 60 years’ imprisonment.<footnotemark>68</footnotemark> The conviction was affirmed without opinion by the Appellate Division, Second Department, 21 App. Div. 2d 752, 252 N. Y. S. 2d 19, and by the Court of Appeals, also without opinion, 15 N. Y. 2d 970, <span class="citation multiple-matches"><a href="/c/N.%20E.%202d/207/527/">207 N. E. 2d 527</a></span>, 259 N. Y. S. 2d 857, remittitur amended, 16 N. Y. 2d 614, <span class="citation multiple-matches"><a href="/c/N.%20E.%202d/209/110/">209 N. E. 2d 110</a></span>, 261 N. Y. S. 2d 65. In argument to the Court of Appeals, the State contended that Vignera had no constitutional right to be advised of his right to counsel or his privilege against self-incrimination.</p>
<p id="b592-7">We reverse. The foregoing indicates that Vignera was not warned of any of his rights before the questioning by the detective and by the assistant district attorney. No other steps were taken to protect these rights. Thus he was not effectively apprised of his Fifth Amendment privilege or of his right to have counsel present and his statements are inadmissible.</p>
<p id="b592-8">No. 761. <em>Westover </em>v. <em>United States.</em></p>
<p id="b592-9">At approximately 9:45 p. m. on March 20, 1963, petitioner, Carl Calvin Westover, was arrested by local police in Kansas City as a suspect in two Kansas City robberies. A report was also received from the FBI that he was wanted on a felony charge in California. The local authorities took him to a police station and placed him in a line-up on the local charges, and at about 11:45 p. m. he was booked. Kansas City police interrogated West-<page-number citation-index="1" label="495">*495</page-number>over on the night of his arrest. He denied any knowledge of criminal activities. The next day local officers interrogated him again throughout the morning. Shortly before noon they informed the FBI that they were through interrogating Westover and that the FBI could proceed to interrogate him. There is nothing in the record to indicate that Westover was ever given any warning as to his rights by local police. At noon, three special agents of the FBI continued the interrogation in a private interview room of the Kansas City Police Department, this time with respect to the robbery of a savings and loan association and a bank in Sacramento, California. After two or two and one-half hours, West-over signed separate confessions to each of these two robberies which had been prepared by one of the agents during the interrogation. At trial one of the agents testified, and a paragraph on each of the statements states, that the agents advised Westover that he did not have to make a statement, that any statement he made could be used against him, and that he had the right to see an attorney.</p>
<p id="b593-5">Westover was tried by a jury in federal court and convicted of the California robberies. His statements were introduced at trial. He was sentenced to 15 years’ imprisonment on each count, the sentences to run consecutively. On appeal, the conviction was affirmed by the Court of Appeals for the Ninth Circuit. <span class="citation" data-id="267168"><a href="/opinion/267168/carl-calvin-westover-v-united-states/" aria-description="Citation for case: Carl Calvin Westover v. United States">342 F. 2d 684</a></span>.</p>
<p id="b593-6">We reverse. On the facts of this case we cannot find that Westover knowingly and intelligently waived his right to remain silent and his right to consult with counsel prior to the time he made the statement.<footnotemark>69</footnotemark> At the <page-number citation-index="1" label="496">*496</page-number>time the FBI agents began questioning Westover, he had been in custody for over 14 hours and had been interrogated at length during that period. The FBI interrogation began immediately upon the conclusion of the interrogation by Kansas City police and was conducted in local police headquarters. Although the two law enforcement authorities are legally distinct and the crimes for which they interrogated Westover were different, the impact on him was that of a continuous period of questioning. There is no evidence of any warning given prior to the FBI interrogation nor is there any evidence of an articulated waiver of rights after the FBI commenced its interrogation. The record simply shows that the defendant did in fact confess a short time after being turned over to the FBI following interrogation by local police. Despite the fact that the FBI agents gave warnings at the outset of their interview, from West-over’s point of view the warnings came at the end of the interrogation process. In these circumstances an intelligent waiver of constitutional rights cannot be assumed.</p>
<p id="b594-6">We do not suggest that law enforcement authorities are precluded from questioning any individual who has been held for a period of time by other authorities and interrogated by them without appropriate warnings. A different case would be presented if an accused were taken into custody by the second authority, removed both in time and place from his original surroundings, and then adequately advised of his rights and given an opportunity to exercise them. But here the FBI interrogation was conducted immediately following the state interrogation in the same police station — in the same compelling surroundings. Thus, in obtaining a confession from West-<page-number citation-index="1" label="497">*497</page-number>over the federal authorities were the beneficiaries of the pressure applied by the local in-custody interrogation. In these circumstances the giving of warnings alone was not sufficient to protect the privilege.</p>
<p id="b595-5">No. 584. <em>California </em>v. <em>Stewart.</em></p>
<p id="b595-6">In the course of investigating a series of purse-snatch robberies in which one of the victims had died of injuries inflicted by her assailant, respondent, Roy Allen Stewart, was pointed out to Los Angeles police as the endorser of dividend checks taken in one of the robberies. At about 7:15 p. m., January 31, 1963, police officers went to Stewart’s house and arrested him. One of the officers asked Stewart if they could search the house, to which he replied, “Go ahead.” The search turned up various items taken from the five robbery victims. At the time of Stewart’s arrest, police also arrested Stewart’s wife and three other persons who were visiting him. These four were jailed along with Stewart and were interrogated. Stewart was taken to the University Station of the Los Angeles Police Department where he was placed in a cell. During the next five days, police interrogated Stewart on nine different occasions. Except during the first interrogation session, when he was confronted with an accusing witness, Stewart was isolated with his interrogators.</p>
<p id="b595-7">During the ninth interrogation session, Stewart admitted that he had robbed the deceased and stated that he had not meant to hurt her. Police then brought Stewart before a magistrate for the first time. Since there was no evidence to connect them with any crime, the police then released the other four persons arrested with him.</p>
<p id="b595-8">Nothing in the record specifically indicates whether Stewart was or was not advised of his right to remain silent or his right to counsel. In a number of instances, <page-number citation-index="1" label="498">*498</page-number>however, the interrogating officers were asked to recount everything that was said during the interrogations. None indicated that Stewart was ever advised of his rights.</p>
<p id="b596-6">Stewart was charged with kidnapping to commit robbery, rape, and murder. At his trial, transcripts of the first interrogation and the confession at the last interrogation were introduced in evidence. The jury found Stewart guilty of robbery and first degree murder and fixed the penalty as death. On appeal, the Supreme Court of California reversed. <span class="citation" data-id="9791096"><a href="/opinion/2608355/people-v-stewart/" aria-description="Citation for case: People v. Stewart">62 Cal. 2d 571</a></span>, <span class="citation" data-id="9791096"><a href="/opinion/2608355/people-v-stewart/" aria-description="Citation for case: People v. Stewart">400 P. 2d 97</a></span>, <span class="citation" data-id="9791096"><a href="/opinion/2608355/people-v-stewart/" aria-description="Citation for case: People v. Stewart">43 Cal. Rptr. 201</a></span>. It held that under this Court’s decision in <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>, </em>Stewart should have been advised of his right to remain silent and of his right to counsel and that it would not presume in the face of a silent record that the police advised Stewart of his rights.<footnotemark>70</footnotemark></p>
<p id="b596-7">We affirm.<footnotemark>71</footnotemark> In dealing with custodial interrogation, we will not presume that a defendant has been effectively apprised of his rights and that his privilege against self-incrimination has been adequately safeguarded on a record that does not show that any warnings have been given or that any effective alternative has been employed. Nor can a knowing and intelligent waiver of <page-number citation-index="1" label="499">*499</page-number>these rights be assumed on a silent record. Furthermore, Stewart’s steadfast denial of the alleged offenses through eight of the nine interrogations over a period of five days is subject to no other construction than that he was compelled by persistent interrogation to forgo his Fifth Amendment privilege.</p>
<p id="b597-4">Therefore, in accordance with the foregoing, the judgments of the Supreme Court of Arizona in No. 759, of the New York Court of Appeals in No. 760, and of the Court of Appeals for the Ninth Circuit in No. 761 are reversed. The judgment of the Supreme Court of California in No. 584 is affirmed.</p>
<p id="b597-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b538-7"> Compare <em>United States </em>v. <em>Childress, </em><span class="citation" data-id="268400"><a href="/opinion/268400/united-states-v-freddie-lee-childress/" aria-description="Citation for case: United States v. Freddie Lee Childress">347 F. 2d 448</a></span> (C. A. 7th Cir. 1965), with <em>Collins </em>v. <em>Beto, </em><span class="citation" data-id="9450950"><a href="/opinion/268701/clarence-collins-v-george-j-beto-director-texas-department-of/" aria-description="Citation for case: Clarence Collins v. George J. Beto, Director, Texas...">348 F. 2d 823</a></span> (C. A. 5th Cir. 1965). Compare <em>People </em>v. <em>Dorado, </em><span class="citation" data-id="9549155"><a href="/opinion/1177555/people-v-dorado/" aria-description="Citation for case: People v. Dorado">62 Cal. 2d 338</a></span>, <span class="citation" data-id="9549155"><a href="/opinion/1177555/people-v-dorado/" aria-description="Citation for case: People v. Dorado">398 P. 2d 361</a></span>, <span class="citation" data-id="9549155"><a href="/opinion/1177555/people-v-dorado/" aria-description="Citation for case: People v. Dorado">42 Cal. Rptr. 169</a></span> (1964) with <em>People </em>v. <em>Hartgraves, </em><span class="citation" data-id="2221754"><a href="/opinion/2221754/the-people-v-hartgraves/" aria-description="Citation for case: The People v. Hartgraves">31 Ill. 2d 375</a></span>, <span class="citation" data-id="2221754"><a href="/opinion/2221754/the-people-v-hartgraves/" aria-description="Citation for case: The People v. Hartgraves">202 N. E. 2d 33</a></span> (1964).</p>
</footnote>
<footnote label="2">
<p id="b538-8"> See, <em>e. g., </em>Enker <em>&amp; </em>Elsen, Counsel for the Suspect: <em>Massiah </em>v. <em>United States </em>and <em>Escobedo </em>v. <em>Illinois, </em><span class="citation no-link">49 Minn. L. Rev. 47</span> (1964); Herman, The Supreme Court and Restrictions on Police Interrogation, 25 Ohio St. L. J. 449 (1964); Kamisar, Equal Justice in the Gatehouses and Mansions of American Criminal Procedure, in Criminal Justice in Our Time 1 (1965); Dowling, Escobedo and <page-number citation-index="1" label="441">*441</page-number>Beyond: The Need for a Fourteenth Amendment Code of Criminal Procedure, 56 J. Crim. L., C. &amp; P. S. 143, 156 (1965).</p>
<p id="b539-6">The complex problems also prompted discussions by jurists. Compare Bazelon, Law, Morality, and Civil Liberties, 12 U. C. L. A. L. Rev. 13 (1964), with Friendly, The Bill of Rights as a Code of Criminal Procedure, <span class="citation no-link">53 Calif. L. Rev. 929</span> (1965).</p>
</footnote>
<footnote label="3">
<p id="b539-7"> For example, the Los Angeles Police Chief stated that “If the police are required . . . to . . . establish that the defendant was apprised of his constitutional guarantees of silence and legal counsel prior to the uttering of any admission or confession, and that he intelligently waived these guarantees ... a whole Pandora’s box is opened as to under what circumstances . . . can a defendant intelligently waive these rights. . . . Allegations that modern criminal investigation can compensate for the lack of a confession or admission in every criminal case is totally absurd!” Parker, 40 L. A. Bar Bull. 603, 607, 642 (1965). His prosecutorial counterpart, District Attorney Younger, stated that “[I]t begins to appear that many of these seemingly restrictive decisions are going to contribute directly to a more effective, efficient and professional level of law enforcement.” L. A. Times, Oct. 2, 1965, p. 1. The former Police Commissioner of New York, Michael J. Murphy, stated of <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>: </em>“What the Court is doing is akin to requiring one boxer to fight by Marquis of Queensbury rules while permitting the other to butt, gouge and bite.” N. Y. Times, May 14, 1965, p. 39. The former United States Attorney for the District of Columbia, David C. Acheson, who is presently Special Assistant to the Secretary of the Treasury (for Enforcement), and directly in charge of the Secret Service and the Bureau of Narcotics, observed that “Prosecution procedure has, at most, only the most remote causal connection with crime. Changes in court decisions and prosecution procedure would have about the same effect on the crime rate as an aspirin would have on a tumor of the brain.” Quoted in Herman, <em>supra, </em>n. 2, at 500, n. 270. Other views on the subject in general are collected in Weisberg, Police Interrogation of Arrested Persons: A Skeptical View, 52 J. Crim. L., C. &amp; P. S. 21 (1961).</p>
</footnote>
<footnote label="4">
<p id="b542-8"> This is what we meant in <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>when we spoke of an investigation which had focused on an accused.</p>
</footnote>
<footnote label="5">
<p id="b543-8"> See, for example, IV' National Commission on Law Observance and Enforcement, Report on Lawlessness in Law Enforcement (1931) <page-number citation-index="1" label="446">*446</page-number>[Wickersham Report]; Booth, Confessions, and Methods Employed in Procuring Them, 4 So. Calif. L. Rev. 83 (1930); Kauper, Judicial Examination of the Accused — A Remedy for the Third Degree, <span class="citation no-link">30 Mich. L. Rev. 1224</span> (1932). It is significant that instances of third-degree treatment of prisoners almost invariably took place during the period between arrest and preliminary examination. Wicker-sham Report, at 169; Hall, The Law of Arrest in Relation to Contemporary Social Problems, <span class="citation no-link">3 U. Chi. L. Rev. 345</span>, 357 (1936). See also Foote, Law and Police Practice: Safeguards in the Law of Arrest, <span class="citation no-link">52 Nw. U. L. Rev. 16</span> (1957).</p>
</footnote>
<footnote label="6">
<p id="b544-11"> <em>Brown </em>v. <em>Mississippi, </em><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936); <em>Chambers </em>v. <em>Florida, </em><span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span> (1940); <em>Canty </em>v. <em>Alabama, </em><span class="citation" data-id="8155149"><a href="/opinion/8193214/canty-v-alabama/" aria-description="Citation for case: Canty v. Alabama">309 U. S. 629</a></span> (1940); <em>White </em>v. <em>Texas, </em><span class="citation" data-id="103368"><a href="/opinion/103368/white-v-texas/" aria-description="Citation for case: White v. Texas">310 U. S. 530</a></span> (1940); <em>Vernon </em>v. <em>Alabama, </em><span class="citation" data-id="8156474"><a href="/opinion/8194539/vernon-v-alabama/" aria-description="Citation for case: Vernon v. Alabama">313 U. S. 547</a></span> (1941); <em>Ward </em>v. <em>Texas, </em><span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/" aria-description="Citation for case: Ward v. Texas">316 U. S. 547</a></span> (1942); <em>Ashcraft </em>v. <em>Tennessee, </em><span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span> (1944); <em>Malinski </em>v. <em>New York, </em><span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span> (1945); <em>Leyra </em>v. <em>Denno, </em><span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556</a></span> (1954). See also <em>Williams </em>v. <em>United States, </em><span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/" aria-description="Citation for case: Williams v. United States">341 U. S. 97</a></span> (1951).</p>
</footnote>
<footnote label="7">
<p id="b544-12"> In addition, see <em>People </em>v. <em>Wakat, </em><span class="citation" data-id="2045374"><a href="/opinion/2045374/people-v-wakat/" aria-description="Citation for case: People v. Wakat">415 Ill. 610</a></span>, <span class="citation" data-id="2045374"><a href="/opinion/2045374/people-v-wakat/" aria-description="Citation for case: People v. Wakat">114 N. E. 2d 706</a></span> (1953); <em>Wa

[...TRUNCATED 44991 of 164991 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/Mooney v. Holohan.md  (`case`, 5 assertions)

### content_page

```
---
title: "Mooney v. Holohan"
type: case
citation: "294 U.S. 103 (1935)"
parallel_cite: "55 S. Ct. 340; 79 L. Ed. 791; 98 A.L.R. 406"
neutral_cite: 1935 U.S. LEXIS 40
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1935
date_decided: 1935-01-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1935-01-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Mooney v. Holohan
  varies_by_point: false
  scope_note: "Good law as to its core due-process principle — the precursor of the Napue/Giglio knowing-perjury line and the Brady disclosure line. (Its procedural holding remitting the petitioner to state habeas reflects 1935 exhaustion practice.)"
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/102372/mooney-v-holohan/"
  cluster_id: 102372
  opinion_id: 102372
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Anchor (historical origin)"
related: ["[[Napue v. Illinois]]", "[[Giglio v. United States]]", "[[Brady v. Maryland]]", "[[Banks v. Dretke]]", "[[Glossip v. Oklahoma]]"]
aliases: []
tags: ["case", "brady", "giglio", "napue", "perjured-testimony", "prosecutorial-misconduct", "due-process", "historical"]
holding: "The knowing use of perjured testimony by the prosecution to obtain a conviction violates Fourteenth Amendment due process — a 'deliberate deception of court and jury' is as inconsistent with justice as obtaining a conviction by intimidation. (Leave to file the original habeas petition was denied for failure to exhaust state remedies.)"
lake:
  record_id: Mooney v. Holohan
  status: under_review
  projected_at: 2026-07-06
---

# Mooney v. Holohan

*294 U.S. 103 (1935)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Tom Mooney, convicted in California in connection with the 1916 San Francisco Preparedness Day bombing, sought leave to file an original petition for a writ of [[Common Legal Terms#habeas-corpus|habeas corpus]] in the Supreme Court. He alleged that the State had knowingly used perjured testimony to obtain his conviction and had deliberately suppressed evidence that would have impeached that testimony, in violation of the Fourteenth Amendment.

## Issue
Whether the knowing use of perjured testimony (and suppression of impeaching evidence) by state prosecutors to procure a conviction violates due process — and whether the petitioner could pursue that claim by an original [[Common Legal Terms#habeas-corpus|habeas]] petition in the Supreme Court without first exhausting state remedies.

## Rule
Knowing use of perjured testimony violates due process. The Fourteenth Amendment "is a requirement that cannot be deemed to be satisfied by mere notice and hearing if a State has contrived a conviction through the pretense of a trial which in truth is but used as a means of depriving a defendant of liberty through a deliberate deception of court and jury by the presentation of testimony known to be perjured. Such a contrivance by a State to procure the conviction and imprisonment of a defendant is as inconsistent with the rudimentary demands of justice as is the obtaining of a like result by intimidation." — 294 U.S. at 112. ^pin-112

The Court also confirmed that prosecutorial conduct counts as state action: "the action of prosecuting officers on behalf of the State … may constitute state action within the purview of the Fourteenth Amendment." — *Id.*

## Application
The Court accepted that the alleged conduct — if proven — would violate due process, articulating the principle that a conviction obtained through testimony the State knows to be perjured cannot stand. But it did not reach the truth of Mooney's allegations. Because relief by [[Common Legal Terms#habeas-corpus|habeas corpus]] appeared to be available in the California courts and Mooney had not shown that the State afforded no corrective judicial process, the Court held it should not entertain an original petition; leave to file was denied without prejudice to an application to the state courts.

## Conclusion
Leave to file the original [[Common Legal Terms#habeas-corpus|habeas]] petition was denied for failure to exhaust available state remedies. The decision is foundational not for its procedural disposition but for its due-process holding: a state may not knowingly use perjured testimony to obtain a conviction.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- *Mooney* is the **historical origin** of the prosecutorial-honesty line in due process. Its knowing-perjury rule was extended and refined by [[Napue v. Illinois]] (duty to correct false testimony) and [[Giglio v. United States]] (applies to impeachment of cooperating witnesses), applied most recently in [[Glossip v. Oklahoma]] (2025), and runs alongside the affirmative-disclosure duty of [[Brady v. Maryland]] and [[Banks v. Dretke]]. The core principle remains good law.

## Appears on
- [[Brady and Giglio]] — *Key — Anchor (historical origin)*

## Sources
- *Mooney v. Holohan*, 294 U.S. 103 (1935) (per curiam) — https://www.courtlistener.com/opinion/102372/mooney-v-holohan/ — pinpoint: 112.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8c136b723a43488a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "294 U.S. 103 (1935)", "court": "U.S. Supreme Court", "neutral_cite": "1935 U.S. LEXIS 40", "official_citation_present": true, "parallel_cite": "55 S. Ct. 340; 79 L. Ed. 791; 98 A.L.R. 406", "title": "Mooney v. Holohan", "year": "1935"}}
{"assertion_id": "7a20610e2be81180", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Key — Anchor (historical origin)", "title": "Mooney v. Holohan"}}
{"assertion_id": "9bd8ef0356adf74e", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The knowing use of perjured testimony by the prosecution to obtain a conviction violates Fourteenth Amendment due process — a 'deliberate deception of court and jury' is as inconsistent with justice as obtaining a conviction by intimidation. (Leave to file the original habeas petition was denied for failure to exhaust state remedies.)", "title": "Mooney v. Holohan"}}
{"assertion_id": "e377461c3f74a920", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1935-01-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Mooney v. Holohan", "field_i_validity": "good_law", "scope_note": "Good law as to its core due-process principle — the precursor of the Napue/Giglio knowing-perjury line and the Brady disclosure line. (Its procedural holding remitting the petitioner to state habeas reflects 1935 exhaustion practice.)", "title": "Mooney v. Holohan", "varies_by_point": "false"}}
{"assertion_id": "efa792f35b831bcd", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Mooney v. Holohan"}}
```

### lake record — Mooney v. Holohan

```json
{
  "schema_version": "s2.v1",
  "record_id": "Mooney v. Holohan",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Mooney v. Holohan",
    "case_name_short": "Mooney",
    "case_name_full": "Mooney v. Holohan, Warden",
    "input_case_name": "Mooney v. Holohan",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1935-01-21",
    "year": 1935,
    "docket": null,
    "cluster_id": 102372,
    "lead_opinion_id": 102372,
    "sibling_ids": [
      102372
    ],
    "absolute_url": "/opinion/102372/mooney-v-holohan/",
    "identity_method": "pending",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "294 U.S. 103",
      "volume": "294",
      "reporter": "U.S.",
      "page": "103",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "55 S. Ct. 340",
        "volume": "55",
        "reporter": "S. Ct.",
        "page": "340",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 L. Ed. 791",
        "volume": "79",
        "reporter": "L. Ed.",
        "page": "791",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 A.L.R. 406",
        "volume": "98",
        "reporter": "A.L.R.",
        "page": "406",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1935 U.S. LEXIS 40",
        "volume": "1935",
        "reporter": "U.S. LEXIS",
        "page": "40",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "294 U.S. 103",
        "volume": "294",
        "reporter": "U.S.",
        "page": "103",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 S. Ct. 340",
        "volume": "55",
        "reporter": "S. Ct.",
        "page": "340",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 L. Ed. 791",
        "volume": "79",
        "reporter": "L. Ed.",
        "page": "791",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1935 U.S. LEXIS 40",
        "volume": "1935",
        "reporter": "U.S. LEXIS",
        "page": "40",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 A.L.R. 406",
        "volume": "98",
        "reporter": "A.L.R.",
        "page": "406",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "294 U.S. 103",
    "official_selection": {
      "court_class": "scotus",
      "selected": "294 U.S. 103",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-112",
      "page": null,
      "quote": "--- # Mooney v. Holohan *294 U.S. 103 (1935)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Tom Mooney, convicted in California in connection with the 1916 San Francisco Preparedness Day bombing, sought leave to file an original petition for a writ of habeas corpus in the Supreme Court. He alleged that the State had knowingly used perjured testimony to obtain his conviction and had deliberately suppressed evidence that would have impeached that testimony, in violation of the Fourteenth Amendment. ## Issue Whether the knowing use of perjured testimony (and suppression of impeaching evidence) by state prosecutors to procure a conviction violates due process \u2014 and whether the petitioner could pursue that claim by an original habeas petition in the Supreme Court without first exhausting state remedies. ## Rule Knowing use of perjured testimony violates due process. The Fourteenth Amendment",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1935-01-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Mooney v. Holohan",
    "varies_by_point": false,
    "scope_note": "Good law as to its core due-process principle \u2014 the precursor of the Napue/Giglio knowing-perjury line and the Brady disclosure line. (Its procedural holding remitting the petitioner to state habeas reflects 1935 exhaustion practice.)",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Antonio Smith v. State of Indiana",
          "cluster_id": 2812363,
          "cite": [
            "34 N.E.3d 1211",
            "2015 Ind. LEXIS 567",
            "2015 WL 3929923"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Guzman v. Secretary, Department of Corrections",
          "cluster_id": 618520,
          "cite": [
            "663 F.3d 1336",
            "2011 U.S. App. LEXIS 24465",
            "2011 WL 6061337"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Napper, Ex Parte Lawrence James",
          "cluster_id": 2943007,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Krizan-Wilson",
          "cluster_id": 2275981,
          "cite": [
            "321 S.W.3d 619",
            "2010 WL 2483784"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Carolyn Sue Krizan-Wilson",
          "cluster_id": 2992921,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "McKithen v. Brown",
          "cluster_id": 1458192,
          "cite": [
            "565 F. Supp. 2d 440",
            "2008 U.S. Dist. LEXIS 55094",
            "2008 WL 2791852"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brady v. Maryland",
          "cluster_id": 106598,
          "cite": [
            "10 L. Ed. 2d 215",
            "83 S. Ct. 1194",
            "373 U.S. 83",
            "1963 U.S. LEXIS 1615"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. Zerbst",
          "cluster_id": 103050,
          "cite": [
            "304 U.S. 458",
            "58 S. Ct. 1019",
            "82 L. Ed. 1461",
            "1938 U.S. LEXIS 896"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bagley",
          "cluster_id": 111514,
          "cite": [
            "87 L. Ed. 2d 481",
            "105 S. Ct. 3375",
            "473 U.S. 667",
            "1985 U.S. LEXIS 130",
            "53 U.S.L.W. 5084"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
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
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Imbler v. Pachtman",
          "cluster_id": 109387,
          "cite": [
            "47 L. Ed. 2d 128",
            "96 S. Ct. 984",
            "424 U.S. 409",
            "1976 U.S. LEXIS 25"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albright v. Oliver",
          "cluster_id": 112924,
          "cite": [
            "127 L. Ed. 2d 114",
            "114 S. Ct. 807",
            "510 U.S. 266",
            "1994 U.S. LEXIS 1319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Giglio v. United States",
          "cluster_id": 108471,
          "cite": [
            "31 L. Ed. 2d 104",
            "92 S. Ct. 763",
            "405 U.S. 150",
            "1972 U.S. LEXIS 83"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Agurs",
          "cluster_id": 109506,
          "cite": [
            "49 L. Ed. 2d 342",
            "96 S. Ct. 2392",
            "427 U.S. 97",
            "1976 U.S. LEXIS 72"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
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
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyles v. Whitley",
          "cluster_id": 117923,
          "cite": [
            "131 L. Ed. 2d 490",
            "115 S. Ct. 1555",
            "514 U.S. 419",
            "1995 U.S. LEXIS 2845"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rose v. Lundy",
          "cluster_id": 110662,
          "cite": [
            "71 L. Ed. 2d 379",
            "102 S. Ct. 1198",
            "455 U.S. 509",
            "1982 U.S. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Santobello v. New York",
          "cluster_id": 108416,
          "cite": [
            "30 L. Ed. 2d 427",
            "92 S. Ct. 495",
            "404 U.S. 257",
            "1971 U.S. LEXIS 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Strickler v. Greene",
          "cluster_id": 118307,
          "cite": [
            "144 L. Ed. 2d 286",
            "119 S. Ct. 1936",
            "527 U.S. 263",
            "1999 U.S. LEXIS 4191"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Napue v. Illinois",
          "cluster_id": 105912,
          "cite": [
            "3 L. Ed. 2d 1217",
            "79 S. Ct. 1173",
            "360 U.S. 264",
            "1959 U.S. LEXIS 811"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fay v. Noia",
          "cluster_id": 106548,
          "cite": [
            "9 L. Ed. 2d 837",
            "83 S. Ct. 822",
            "372 U.S. 391",
            "1963 U.S. LEXIS 1945",
            "24 Ohio Op. 2d 12"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donnelly v. DeChristoforo",
          "cluster_id": 109024,
          "cite": [
            "40 L. Ed. 2d 431",
            "94 S. Ct. 1868",
            "416 U.S. 637",
            "1974 U.S. LEXIS 138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malloy v. Hogan",
          "cluster_id": 106862,
          "cite": [
            "12 L. Ed. 2d 653",
            "84 S. Ct. 1489",
            "378 U.S. 1",
            "1964 U.S. LEXIS 993"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Trombetta",
          "cluster_id": 111206,
          "cite": [
            "81 L. Ed. 2d 413",
            "104 S. Ct. 2528",
            "467 U.S. 479",
            "1984 U.S. LEXIS 103",
            "52 U.S.L.W. 4744"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Youngblood",
          "cluster_id": 112156,
          "cite": [
            "102 L. Ed. 2d 281",
            "109 S. Ct. 333",
            "488 U.S. 51",
            "1988 U.S. LEXIS 5404"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Green",
          "cluster_id": 108189,
          "cite": [
            "26 L. Ed. 2d 489",
            "90 S. Ct. 1930",
            "399 U.S. 149",
            "1970 U.S. LEXIS 14"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Allen",
          "cluster_id": 108110,
          "cite": [
            "25 L. Ed. 2d 353",
            "90 S. Ct. 1057",
            "397 U.S. 337",
            "1970 U.S. LEXIS 55"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Buckley v. Fitzsimmons",
          "cluster_id": 112894,
          "cite": [
            "125 L. Ed. 2d 209",
            "113 S. Ct. 2606",
            "509 U.S. 259",
            "1993 U.S. LEXIS 4400"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
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
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haguer v. Committee for Industrial Organization",
          "cluster_id": 103226,
          "cite": [
            "307 U.S. 496",
            "59 S. Ct. 954",
            "83 L. Ed. 1423",
            "1939 U.S. LEXIS 1067",
            "4 L.R.R.M. (BNA) 501"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
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
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(102372) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjAxMDQ2NDAwMDAwJnM9MTI3MjQyNiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28102372%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 6,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(102372)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05ODQmcz0xMTE2MDMmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28102372%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(102372)",
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
    "complete_query": "cites:(102372)",
    "indexed_citing_opinions": 1195,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 102372,
        "count": 1195,
        "count_source": "search"
      }
    ],
    "citation_count": 1838,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mooney-v-holohan.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc1MzMyNTYmcz01MzA0MTMwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28102372%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 102372,
        "cited_id": 91149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 94648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 95255,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 95368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 95992,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 98441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 100122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 100710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 100929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 101335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 2620727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 3302184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 3303533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 3308686,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 3309150,
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
    "date_created": "2026-07-05T14:36:03Z",
    "date_modified": "2026-07-06T08:25:38Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:36:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:36:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:39:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:36:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Mooney v. Holohan

```
<?xml version="1.0" encoding="utf-8"?>
<opinion data-order="7" data-type="opinion" id="x999-1" type="majority">
<author id="b159-8">
<span citation-index="1" class="star-pagination" label="109"> 
   *109
   </span>
  Per Curiam.
 </author>
<p id="b159-9">
  Thomas J. Mooney asks leave to file petition for an original writ of
  <em>
   habeas corpus.
  </em>
  He states that he is unlawfully restrained of his liberty by the State of California under a commitment pursuant to a conviction, in February, 1917, of murder in the first degree and sentence of death subsequently commuted to life imprisonment. He submits the record of proceedings set forth in his petition for a writ of
  <em>
   habeas corpus
  </em>
  presented to the District
  <span citation-index="1" class="star-pagination" label="110"> 
   *110
   </span>
  Court of the United States for the Northern District of California and dismissed upon the ground that the petitioner had not exhausted his legal remedies in the state court. Applications to the Judges of the Circuit Court of Appeals for the Ninth Circuit for allowance of an appeal to that Court from the judgment of dismissal have severally been denied.
 </p>
<p id="b160-6">
  Petitioner charges that the State holds him in confinement without due process of law in violation of the Fourteenth Amendment of the Constitution of the United States. The grounds of his charge are, in substance, that the sole basis of his conviction was perjured testimony, which was knowingly used by the prosecuting authorities in order to obtain that conviction, and also that these authorities deliberately suppressed evidence which would have impeached and refuted the testimony thus given against him. He alleges that he could not by reasonable diligence have discovered prior to the denial of his motion for a new trial, and his appeal to the Supreme Court of the State, the evidence which was subsequently developed and which proved the testimony against him to have been perjured. Petitioner urges that the
  <em>
   “
  </em>
  knowing use ” by the State of perjured testimony to obtain the conviction and the deliberate suppression of evidence to impeach that testimony constituted a denial of due process of law. Petitioner further contends that the State deprives him of his liberty without due process of law by its failure, in the circumstances set forth, to provide any corrective judicial process by which a conviction so obtained may be set aside.
 </p>
<p id="b160-7">
  In support of his serious charges, petitioner submits a •chronological history of the trials, appeals and other judicial proceedings connected with his conviction, and of his applications for executive clemency. He sets forth the evidence which, as he contends, proves the perjury
  <span citation-index="1" class="star-pagination" label="111"> 
   *111
   </span>
  of the witnesses upon whose testimony he was convicted and the knowledge on the part of the prosecuting authorities of that perjury and the suppression by those authorities of impeaching evidence at their command. He also submits what he insists are admissions by the State that the testimony offered against him was perjured and that his conviction was unjustified. In amplification of these statements, he asks leave to incorporate in his petition, by reference, the voluminous details of the various proceedings as they were presented with his petition to the District Court.
 </p>
<p id="b161-6">
  In response to our rule to show cause why leave to file the petition should not be granted, the respondent has made return by the Attorney General of the State. With this return, he submits an appendix of exhibits setting forth the consent filed by the Attorney General with the Supreme Court of the State on July 30, 1917, that the judgment of conviction be reversed and the cause remanded for a new trial, the subsequent opinions of that Court upon the cases presented to it, the statements of Governors of the State on applications for executive clemency made on behalf of this petitioner and of one Billings (who had been jointly indicted with petitioner and was separately tried and convicted), and the reports of Justices of the Supreme Court of the State, and communications addressed by them, to the Governors of the State in connection with such applications.
 </p>
<p id="b161-7">
  The return does not put in issue any of the facts alleged in the petition. The return is in the nature of a demurrer. It submits that the petitioner “ has failed, to raise a Federal question and that, consequently, leave to file the petition should be denied.” Reviewing decisions relating to due process, the Attorney General insists that the petitioner’s argument is vitiated by the fallacy “ that the acts or omissions of- a prosecuting- attorney can ever,
  <span citation-index="1" class="star-pagination" label="112"> 
   *112
   </span>
<em>
   in and by themselves,
  </em>
  amount either to due process of law or to a denial of due process of law.” The Attorney-General states that if the acts or omissions of a prosecuting attorney “have the effect of withholding from a defendant the notice which must be accorded him under the due process clause, or if they have the effect of preventing a defendant from presenting such evidence as he possesses in defense of the accusation against him, then such acts or omissions of the prosecuting attorney may be regarded as
  <em>
   resulting
  </em>
  in a denial of due process of law.” And, “ conversely,” the Attorney General contends that “ it is only where an act or omission operates so as to deprive a defendant of notice or so as to deprive him of an opportunity to present such evidence as he has, that it can be said that due process of law has been denied.”
 </p>
<p id="A9S">
  Without attempting at this time to deal with the question at length, we deem it sufficient for the present purpose to say that we are unable to approve this narrow view of the requirement of due process. That requirement, in safeguarding the liberty of the citizen against deprivation through the action of the State, embodies the fundamental conceptions of justice which lie at the base of our civil and political institutions.
  <em>
   Hebert
  </em>
  v.
  <em>
   Louisiana,
  </em>
  <span class="citation" data-id="100929"><a href="/opinion/100929/hebert-v-louisiana/#316" aria-description="Citation for case: Hebert v. Louisiana">272 U. S. 312, 316, 317</a></span>. It is a requirement that cannot be deemed tó be satisfied by mere notice and hearing if a State has contrived a conviction through the pretense of a trial which in truth is but used as a means of depriving a defendant of liberty through a deliberate deception of court and jury by the presentation of testimony known to be perjured. Such a contrivance by a State to procure the conviction and imprisonment of a defendant is as inconsistent with the rudimentary demands of justice as is the obtaining of a like result by intimidation. And the action of prosecuting officers on behalf of the State, like that of adminis
  <span citation-index="1" class="star-pagination" label="113"> 
   *113
   </span>
  trative officers in the execution of its laws, may constitute state action within the purview of the Fourteenth Amendment. That Amendment governs any action of a State, “ whether through its legislature, through its courts, or through its executive or administrative officers.”
  <em>
   Carter
  </em>
  v.
  <em>
   Texas,
  </em>
  <span class="citation" data-id="95255"><a href="/opinion/95255/carter-v-texas/#447" aria-description="Citation for case: Carter v. Texas">177 U. S. 442, 447</a></span>;
  <em>
   Rogers
  </em>
  v.
  <em>
   Alabama,
  </em>
  <span class="citation" data-id="95992"><a href="/opinion/95992/rogers-v-alabama/#231" aria-description="Citation for case: Rogers v. Alabama">192 U. S. 226, 231</a></span>;
  <em>
   Chicago, Burlington &amp; Quincy R. Co.
  </em>
  v.
  <em>
   Chicago,
  </em>
  <span class="citation" data-id="9417760"><a href="/opinion/94648/chicago-burlington-quincy-railroad-v-chicago/#233" aria-description="Citation for case: Chicago, Burlington &amp; Quincy Railroad v. Chicago">166 U. S. 226, 233, 234</a></span>.
 </p>
<p id="b163-6">
  Reasoning from the premise that the petitioner has failed to show a denial of due process in the circumstances set forth in his petition, the Attorney General urges that the State was not required to afford any corrective judicial process to remedy the alleged wrong. The argument falls with the premise.
  <em>
   Frank
  </em>
  v.
  <em>
   Mangum,
  </em>
  <span class="citation" data-id="9418283"><a href="/opinion/98441/frank-v-mangum/#335" aria-description="Citation for case: Frank v. Mangum">237 U. S. 309, 335</a></span>;
  <em>
   Moore
  </em>
  v.
  <em>
   Dempsey,
  </em>
  <span class="citation" data-id="9418497"><a href="/opinion/100122/moore-v-dempsey/#90" aria-description="Citation for case: Moore v. Dempsey">261 U. S. 86, 90, 91</a></span>.
 </p>
<p id="b163-7">
  We are not satisfied, however, that the State of California has failed to provide such corrective judicial process. The prerogative writ of
  <em>
   habeas corpus
  </em>
  is available in that State. Constitution of California, Art. I, § 5; Art. VI, § 4. No decision of the Supreme Court of California has been brought to our attention holding that the state court is without power to issue this historic remedial process when it appears that one is deprived of his liberty without due process of law in violation of the Constitution of the United States. Upon the state courts, equally with the courts of the Union, rests the obligation to guard and enforce every right secured by that Constitution.
  <em>
   Robb
  </em>
  v.
  <em>
   Connolly,
  </em>
  <span class="citation" data-id="91149"><a href="/opinion/91149/robb-v-connolly/#637" aria-description="Citation for case: Robb v. Connolly">111 U. S. 624, 637</a></span>. In view of the dominant requirement of the Fourteenth Amendment, we are not at liberty to assume that the State has denied to its court jurisdiction to redress the prohibited wrong upon a proper showing and in an appropriate proceeding for that purpose.
 </p>
<p id="b163-8">
  The decisions of the Supreme Court of California in relation to petitioner’s conviction have dealt with the ques
  <span citation-index="1" class="star-pagination" label="114"> 
   *114
   </span>
  tions presented to that Court within the limitations of particular appellate procedure. When there was submitted to that Court the consent of the Attorney General to the reversal of the judgment against petitioner and to the granting of a new trial, the Court pointed out that no motion had been made by the defendant and that his appeal was awaiting hearing.
  <em>
   People
  </em>
  v. Mooney, <span class="citation" data-id="3302184"><a href="/opinion/3302906/people-v-mooney/" aria-description="Citation for case: People v. Mooney">175 Cal. 666</a></span>; <span class="citation" data-id="3302184"><a href="/opinion/3302906/people-v-mooney/" aria-description="Citation for case: People v. Mooney">166 Pac. 999</a></span>. When, again in advance of the hearing of his appeal, the defendant made his motion solely upon the ground of the Attorney General’s consent, the Court held that its jurisdiction on appeal was limited to a determination whether there had been any error of law in the proceedings of the trial court and that the Court was confined to the record sent to it by the court below.
  <em>
   People
  </em>
  v.
  <em>
   Mooney,
  </em>
  <span class="citation" data-id="3303533"><a href="/opinion/3304127/people-v-mooney/" aria-description="Citation for case: People v. Mooney">176 Cal. 105</a></span>; <span class="citation" data-id="3303533"><a href="/opinion/3304127/people-v-mooney/" aria-description="Citation for case: People v. Mooney">167 Pac. 696</a></span>. On the appeal, the Court thus dealing with the record before it, found that the verdict was supported by the testimony presented and that no ground appeared for reversal.
  <em>
   People
  </em>
  v.
  <em>
   Mooney,
  </em>
  <span class="citation" data-id="3308686"><a href="/opinion/3308670/people-v-mooney/" aria-description="Citation for case: People v. Mooney">177 Cal. 642</a></span>; <span class="citation" data-id="3308686"><a href="/opinion/3308670/people-v-mooney/" aria-description="Citation for case: People v. Mooney">171 Pac. 690</a></span>. When, later, the defendant moved to set aside the judgment, and sought a certificate of probable cause on his appeal from an order denying his motion, the Court held that the general averments against the fairness of the trial were insufficient, but the Court did not place its denial of the application entirely upon that ground. The Court concluded that the proceeding by way of motion to set aside the judgment after it had become final and a motion for a new trial had been denied, and the time therefor had expired, was “in the nature of an application for a writ of
  <em>
   cor cm nobis,
  </em>
  at common law.” The Court thought that such a writ did not lie to correct any error in the judgment of the Court nor to contradict or put in issue any fact directly passed upon and affirmed by the judgment itself. The Court, adopting the opinion of the court below, concluded that the judgment could not be set aside because it was predicated upon
  <span citation-index="1" class="star-pagination" label="115"> 
   *115
   </span>
  perjured testimony or because material evidence was concealed or suppressed; that the fraud in such a case was not such fraud as was
  <em>
   “
  </em>
  extrinsic to the record ” and that it was only in cases of extrinsic fraud that the relief sought could be had. It was apparently in relation to such an application that the Court said that the injured party was “ without remedy.”
  <em>
   People
  </em>
  v.
  <em>
   Mooney,
  </em>
  <span class="citation" data-id="3309150"><a href="/opinion/3309089/people-v-mooney/" aria-description="Citation for case: People v. Mooney">178 Cal. 525</a></span>; <span class="citation" data-id="3309150"><a href="/opinion/3309089/people-v-mooney/" aria-description="Citation for case: People v. Mooney">174 Pac. 325</a></span>. And it was with respect to that proceeding, that the writ of certiorari was denied by this Court.
  <em>
   Mooney
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="8143670"><a href="/opinion/8181751/mooney-v-california/" aria-description="Citation for case: Mooney v. California">248 U. S. 579</a></span>. The subsequent communications from the Justices of the Supreme Court in connection with applications for executive clemency were of an advisory character and were not judicial judgments under the requirements of the Constitution of the United States.
 </p>
<p id="b165-6">
  We do not find that petitioner has applied to the state court for a writ of
  <em>
   habeas corpus
  </em>
  upon the grounds stated in his petition here. That corrective judicial process has not been invoked and it is not shown to be unavailable. Despite the many proceedings taken on behalf of the petitioner, an application for the prerogative writ now asserted to be peculiarly suited to the circumstances disclosed by his petition has not been made to the state court. Orderly procedure, governed by principles we have repeatedly announced, requires that before this Court is asked to issue a writ of
  <em>
   habeas corpus,
  </em>
  in the case of a person held under a state commitment, recourse should be had to whatever judicial remedy afforded by the State may still remain open.
  <em>
   Davis
  </em>
  v.
  <em>
   Burke,
  </em>
  <span class="citation" data-id="95368"><a href="/opinion/95368/davis-v-burke/#402" aria-description="Citation for case: Davis v. Burke">179 U. S. 399, 402</a></span>;
  <em>
   Urquhart
  </em>
  v.
  <em>
   Brown,
  </em>
  <span class="citation" data-id="2620727"><a href="/opinion/2620727/urquhart-v-brown/#181" aria-description="Citation for case: Urquhart v. Brown">205 U. S. 179, 181, 182</a></span>;
  <em>
   U. S. ex rel. Kennedy
  </em>
  v.
  <em>
   Tyler,
  </em>
  <span class="citation" data-id="100710"><a href="/opinion/100710/united-states-ex-rel-kennedy-v-tyler/#17" aria-description="Citation for case: United States Ex Rel. Kennedy v. Tyler">269 U. S. 13, 17</a></span>. See, also,
  <em>
   Bryant
  </em>
  v.
  <em>
   Zimmerman,
  </em>
  <span class="citation" data-id="101335"><a href="/opinion/101335/new-york-ex-rel-bryant-v-zimmerman/#70" aria-description="Citation for case: New York Ex Rel. Bryant v. Zimmerman">278 U. S. 63, 70</a></span>.
 </p>
<p id="b165-7">
  Accordingly, leave to file the petition is denied, but without prejudice.
 </p>
<p id="b165-8">
<em>
   Leave denied.
  </em>
</p>
</opinion>
```

---
