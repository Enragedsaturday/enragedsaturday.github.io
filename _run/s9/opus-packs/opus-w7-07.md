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

## GROUP: _overhaul2/lake/cases/Michigan Dept. of State Police v. Sitz.json  (`lake-record`, 3 assertions)

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
{"assertion_id": "9472f2ca6ddddb65", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Michigan Dept. of State Police v. Sitz"}, "payload": {"all": [{"cite": "496 U.S. 444", "page": "444", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "496"}, {"cite": "110 S. Ct. 2481", "page": "2481", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "110"}, {"cite": "110 L. Ed. 2d 412", "page": "412", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "110"}, {"cite": "1990 U.S. LEXIS 3144", "page": "3144", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1990"}, {"cite": "58 U.S.L.W. 4781", "page": "4781", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "58"}], "display": "496 U.S. 444", "official": {"cite": "496 U.S. 444", "page": "444", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "496"}, "official_selection_present": true, "record_id": "Michigan Dept. of State Police v. Sitz"}}
{"assertion_id": "781c029356f37aef", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-455", "record_id": "Michigan Dept. of State Police v. Sitz"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-455", "pinpoint_status": "slip-only", "quote": "--- # Michigan Dept. of State Police v. Sitz *496 U.S. 444 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background The Michigan State Police operated a highway sobriety-checkpoint program under which all passing cars were briefly stopped and drivers showing signs of intoxication were directed aside for field sobriety testing. Licensed Michigan drivers challenged the suspicionless stops as a violation of the Fourth Amendment, and the state courts held the program unconstitutional. ## Issue Whether a State's use of suspicionless highway sobriety checkpoints to detect and deter drunk driving violates the Fourth Amendment. ## Rule No. Weighing the State's interest, the program's effectiveness, and the intrusion on motorists:", "quote_fidelity": "mismatch", "record_id": "Michigan Dept. of State Police v. Sitz", "star_marker": null}}
{"assertion_id": "5ed336b0c37807b8", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Michigan Dept. of State Police v. Sitz"}, "payload": {"as_of_content": "1990-06-14", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Michigan Dept. of State Police v. Sitz", "scope_note": "Distinguished by City of Indianapolis v. Edmond for checkpoints whose primary purpose is general crime control.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/Michigan v. Chesternut.json  (`lake-record`, 7 assertions)

### content_page

```
---
title: "Michigan v. Chesternut"
type: case
citation: "486 U.S. 567 (1988)"
parallel_cite: "108 S. Ct. 1975; 100 L. Ed. 2d 565; 56 U.S.L.W. 4558"
neutral_cite: 1988 U.S. LEXIS 2582
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1988
date_decided: 1988-06-13
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1988-06-13
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Michigan v. Chesternut
  varies_by_point: false
  scope_note: "Good law. Police pursuit, without more, is not a seizure; whether a seizure occurred is judged by the Mendenhall objective test (would a reasonable person have believed he was not free to leave). California v. Hodari D. (1991) later refined the show-of-authority branch to require submission."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112095/michigan-v-chesternut/"
  cluster_id: 112095
  opinion_id: 9431339
  identity_checked: true
homes:
  - page: "[[Seizure of the Person]]"
    role: "Progeny"
related: ["[[United States v. Mendenhall]]", "[[California v. Hodari D.]]", "[[Florida v. Bostick]]", "[[United States v. Knotts]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure", "pursuit", "free-to-leave", "abandonment"]
holding: "Police pursuit, standing alone, is not a Fourth Amendment seizure; whether police conduct is a seizure is determined by the Mendenhall objective test — whether, in all the circumstances, a reasonable person would have believed he was not free to leave."
lake:
  record_id: Michigan v. Chesternut
  status: verified
  projected_at: 2026-07-09
---

# Michigan v. Chesternut

*486 U.S. 567 (1988)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers in a patrol car on routine patrol saw Chesternut standing on a corner; when he saw the cruiser approach, he ran. The officers drove alongside him for a short distance "to see where he was going." They did not activate a siren or flashers, command him to halt, display weapons, or drive aggressively to block his path. As the cruiser drove parallel to him, Chesternut discarded several packets, which the officers retrieved and (believing them to be narcotics) seized; he was then arrested. He moved to suppress the packets as the fruit of an unlawful seizure.

## Issue
Whether the officers' pursuit — driving alongside a fleeing pedestrian — was a Fourth Amendment "seizure," such that the packets Chesternut discarded during the pursuit were the fruit of that seizure.

## Rule
Whether police conduct is a seizure is governed by the objective Mendenhall test: "The test provides that the police can be said to have seized an individual 'only if, in view of all of the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave.'" — 486 U.S. at 573 (quoting *United States v. Mendenhall*). ^pin-573

"The test is necessarily imprecise, because it is designed to assess the coercive effect of police conduct, taken as a whole, rather than to focus on particular details of that conduct in isolation." — [*Id.*](https://www.courtlistener.com/opinion/112095/michigan-v-chesternut/#:~:text=The%20test%20is%20necessarily%20imprecise%2C) ^pin-573b

Applying it, the Court held: "we conclude that respondent was not seized by the police before he discarded the packets containing the controlled substance." — [*Id.* at 574](https://www.courtlistener.com/opinion/112095/michigan-v-chesternut/#:~:text=we%20conclude%20that%20respondent%20was). ^pin-574

## Application
Although an officer called the conduct a "chase," that label did not make it a seizure: "the police conduct involved here would not have communicated to the reasonable person an attempt to capture or otherwise intrude upon respondent's freedom of movement. The record does not reflect that the police activated a siren or flashers; or that they commanded respondent to halt, or displayed any weapons; or that they operated the car in an aggressive manner to block respondent's course or otherwise control the direction or speed of his movement." — *Id.* at 575. ^pin-575

"While the very presence of a police car driving parallel to a running pedestrian could be somewhat intimidating, this kind of police presence does not, standing alone, constitute a seizure." — [*Id.* at 575–576](https://www.courtlistener.com/opinion/112095/michigan-v-chesternut/#:~:text=While%20the%20very%20presence%20of). ^pin-575b

Because Chesternut had not been seized when he abandoned the packets, they were not the fruit of any seizure.

## Conclusion
The pursuit was not a seizure under the Mendenhall test, so the abandoned packets were admissible; the judgment suppressing them was reversed. Police pursuit, without a show of authority that would make a reasonable person believe he was not free to leave, is not a Fourth Amendment seizure.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Chesternut* applies the [[United States v. Mendenhall]] "free to leave" test to pursuits. [[California v. Hodari D.]] (1991) later clarified that, when a seizure is asserted on a *show of authority*, no seizure occurs until the suspect submits — reinforcing that mere pursuit is not a seizure. Compare [[Florida v. Bostick]] (free-to-leave adapted to confined settings).

## Appears on
- [[Seizure of the Person]] — *Progeny*

## Sources
- *Michigan v. Chesternut*, 486 U.S. 567 (1988) — https://www.courtlistener.com/opinion/112095/michigan-v-chesternut/ — pinpoints: 573, 574, 575–576.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "200caa35f7413122", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Michigan v. Chesternut"}, "payload": {"all": [{"cite": "486 U.S. 567", "page": "567", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "486"}, {"cite": "108 S. Ct. 1975", "page": "1975", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "108"}, {"cite": "100 L. Ed. 2d 565", "page": "565", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "100"}, {"cite": "1988 U.S. LEXIS 2582", "page": "2582", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1988"}, {"cite": "56 U.S.L.W. 4558", "page": "4558", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "56"}], "display": "486 U.S. 567", "official": {"cite": "486 U.S. 567", "page": "567", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "486"}, "official_selection_present": true, "record_id": "Michigan v. Chesternut"}}
{"assertion_id": "1d8e97d723e51bc5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-573b", "record_id": "Michigan v. Chesternut"}, "payload": {"fragment": "#:~:text=The%20test%20is%20necessarily%20imprecise%2C", "page": null, "pin_id": "pin-573b", "pinpoint_status": "star-verified", "quote": "The test is necessarily imprecise, because it is designed to assess the coercive effect of police conduct, taken as a whole, rather than to focus on particular details of that conduct in isolation.", "quote_fidelity": "matched", "record_id": "Michigan v. Chesternut", "star_marker": "573"}}
{"assertion_id": "1ecd692c3d4da0bc", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-575", "record_id": "Michigan v. Chesternut"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-575", "pinpoint_status": "slip-only", "quote": "that label did not make it a seizure:", "quote_fidelity": "mismatch", "record_id": "Michigan v. Chesternut", "star_marker": null}}
{"assertion_id": "6f1855e5752d3f05", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-575b", "record_id": "Michigan v. Chesternut"}, "payload": {"fragment": "#:~:text=While%20the%20very%20presence%20of", "page": null, "pin_id": "pin-575b", "pinpoint_status": "star-verified", "quote": "While the very presence of a police car driving parallel to a running pedestrian could be somewhat intimidating, this kind of police presence does not, standing alone, constitute a seizure.", "quote_fidelity": "matched", "record_id": "Michigan v. Chesternut", "star_marker": "575"}}
{"assertion_id": "c34370d1913634cd", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-574", "record_id": "Michigan v. Chesternut"}, "payload": {"fragment": "#:~:text=we%20conclude%20that%20respondent%20was", "page": null, "pin_id": "pin-574", "pinpoint_status": "star-verified", "quote": "we conclude that respondent was not seized by the police before he discarded the packets containing the controlled substance.", "quote_fidelity": "matched", "record_id": "Michigan v. Chesternut", "star_marker": "574"}}
{"assertion_id": "e66a9584cc8b0a13", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-573", "record_id": "Michigan v. Chesternut"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-573", "pinpoint_status": "slip-only", "quote": "such that the packets Chesternut discarded during the pursuit were the fruit of that seizure. ## Rule Whether police conduct is a seizure is governed by the objective Mendenhall test:", "quote_fidelity": "mismatch", "record_id": "Michigan v. Chesternut", "star_marker": null}}
{"assertion_id": "a55134edea11a2b3", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Michigan v. Chesternut"}, "payload": {"as_of_content": "1988-06-13", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Michigan v. Chesternut", "scope_note": "Good law. Police pursuit, without more, is not a seizure; whether a seizure occurred is judged by the Mendenhall objective test (would a reasonable person have believed he was not free to leave). California v. Hodari D. (1991) later refined the show-of-authority branch to require submission.", "varies_by_point": false}}
```

### lake record — Michigan v. Chesternut

```json
{
  "schema_version": "s2.v1",
  "record_id": "Michigan v. Chesternut",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Michigan v. Chesternut",
    "case_name_short": "Chesternut",
    "case_name_full": "Michigan v. Chesternut",
    "input_case_name": "Michigan v. Chesternut",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1988-06-13",
    "year": 1988,
    "docket": null,
    "cluster_id": 112095,
    "lead_opinion_id": 9431339,
    "sibling_ids": [
      112095,
      9431339,
      9431340
    ],
    "absolute_url": "/opinion/112095/michigan-v-chesternut/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "486 U.S. 567",
      "volume": "486",
      "reporter": "U.S.",
      "page": "567",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "108 S. Ct. 1975",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "1975",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 L. Ed. 2d 565",
        "volume": "100",
        "reporter": "L. Ed. 2d",
        "page": "565",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 U.S.L.W. 4558",
        "volume": "56",
        "reporter": "U.S.L.W.",
        "page": "4558",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1988 U.S. LEXIS 2582",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "2582",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "486 U.S. 567",
        "volume": "486",
        "reporter": "U.S.",
        "page": "567",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "108 S. Ct. 1975",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "1975",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 L. Ed. 2d 565",
        "volume": "100",
        "reporter": "L. Ed. 2d",
        "page": "565",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 U.S. LEXIS 2582",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "2582",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 U.S.L.W. 4558",
        "volume": "56",
        "reporter": "U.S.L.W.",
        "page": "4558",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "486 U.S. 567",
    "official_selection": {
      "court_class": "scotus",
      "selected": "486 U.S. 567",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-573",
      "page": null,
      "quote": "such that the packets Chesternut discarded during the pursuit were the fruit of that seizure. ## Rule Whether police conduct is a seizure is governed by the objective Mendenhall test:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-573b",
      "page": null,
      "quote": "The test is necessarily imprecise, because it is designed to assess the coercive effect of police conduct, taken as a whole, rather than to focus on particular details of that conduct in isolation.",
      "star_marker": "573",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 11700,
      "fragment": "#:~:text=The%20test%20is%20necessarily%20imprecise%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-574",
      "page": null,
      "quote": "we conclude that respondent was not seized by the police before he discarded the packets containing the controlled substance.",
      "star_marker": "574",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 13830,
      "fragment": "#:~:text=we%20conclude%20that%20respondent%20was",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-575",
      "page": null,
      "quote": "that label did not make it a seizure:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-575b",
      "page": null,
      "quote": "While the very presence of a police car driving parallel to a running pedestrian could be somewhat intimidating, this kind of police presence does not, standing alone, constitute a seizure.",
      "star_marker": "575",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 14988,
      "fragment": "#:~:text=While%20the%20very%20presence%20of",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1988-06-13",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Michigan v. Chesternut",
    "varies_by_point": false,
    "scope_note": "Good law. Police pursuit, without more, is not a seizure; whether a seizure occurred is judged by the Mendenhall objective test (would a reasonable person have believed he was not free to leave). California v. Hodari D. (1991) later refined the show-of-authority branch to require submission.",
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
        "journal_ref": "Michigan v. Chesternut:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Evelyn",
          "cluster_id": 4786331,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane1_negative"
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
        "journal_ref": "Michigan v. Chesternut:lane1_negative"
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
        "journal_ref": "Michigan v. Chesternut:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Shane S., a juvenile",
          "cluster_id": 4429246,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fields",
          "cluster_id": 3203547,
          "cite": [
            "823 F.3d 20",
            "2016 U.S. App. LEXIS 8834",
            "2016 WL 2821485"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pyon v. State",
          "cluster_id": 2791489,
          "cite": [
            "222 Md. App. 412",
            "112 A.3d 1130",
            "2015 Md. App. LEXIS 50"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Amy Lyons",
          "cluster_id": 3069968,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Florida v. Bostick",
          "cluster_id": 112631,
          "cite": [
            "115 L. Ed. 2d 389",
            "111 S. Ct. 2382",
            "501 U.S. 429",
            "1991 U.S. LEXIS 3625",
            "59 U.S.L.W. 4708",
            "91 Daily Journal DAR 7328",
            "91 Cal. Daily Op. Serv. 4671",
            "1991 WL 105224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. Reed",
          "cluster_id": 112205,
          "cite": [
            "103 L. Ed. 2d 308",
            "109 S. Ct. 1038",
            "489 U.S. 255",
            "1989 U.S. LEXIS 1044",
            "57 U.S.L.W. 4224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Drayton",
          "cluster_id": 121153,
          "cite": [
            "153 L. Ed. 2d 242",
            "122 S. Ct. 2105",
            "536 U.S. 194",
            "2002 U.S. LEXIS 4420"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lanman v. Hinson",
          "cluster_id": 1455879,
          "cite": [
            "529 F.3d 673",
            "2008 U.S. App. LEXIS 12682",
            "2008 WL 2415926"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hollman",
          "cluster_id": 5690698,
          "cite": [
            "79 N.Y.2d 181"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crain v. State",
          "cluster_id": 2353970,
          "cite": [
            "315 S.W.3d 43",
            "2010 Tex. Crim. App. LEXIS 794",
            "2010 WL 2595077"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ehly",
          "cluster_id": 1448102,
          "cite": [
            "854 P.2d 421",
            "317 Or. 66",
            "1993 Ore. LEXIS 91"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cindy Abbott v. Sangamon County",
          "cluster_id": 816250,
          "cite": [
            "705 F.3d 706",
            "2013 WL 322920",
            "2013 U.S. App. LEXIS 1963"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Luedemann",
          "cluster_id": 2008176,
          "cite": [
            "857 N.E.2d 187",
            "222 Ill. 2d 530",
            "306 Ill. Dec. 94",
            "2006 Ill. LEXIS 1641"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 1676406,
          "cite": [
            "912 S.W.2d 227",
            "1995 Tex. Crim. App. LEXIS 115",
            "1995 WL 675559"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Strickler",
          "cluster_id": 2156861,
          "cite": [
            "757 A.2d 884",
            "563 Pa. 47",
            "2000 Pa. LEXIS 2114"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Daniel",
          "cluster_id": 1060655,
          "cite": [
            "12 S.W.3d 420",
            "2000 Tenn. LEXIS 52",
            "2000 WL 100069"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Emil Ewolski v. City of Brunswick",
          "cluster_id": 777338,
          "cite": [
            "287 F.3d 492",
            "2002 U.S. App. LEXIS 7129",
            "2002 WL 571329"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. Madrid",
          "cluster_id": 4867542,
          "cite": [
            "592 U.S. 306",
            "141 S. Ct. 989",
            "209 L. Ed. 2d 190"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112095 OR 9431339 OR 9431340) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjYzNDI3MjAwMDAwJnM9MjI3MDg3NCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112095+OR+9431339+OR+9431340%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112095 OR 9431339 OR 9431340)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMjkmcz03MDIyOTcmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112095+OR+9431339+OR+9431340%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112095 OR 9431339 OR 9431340)",
        "reviewed": 23,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 23,
        "triage_read": 1,
        "triage_snippet_classified": 22
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112095 OR 9431339 OR 9431340)",
    "indexed_citing_opinions": 919,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112095,
        "count": 826,
        "count_source": "search"
      },
      {
        "opinion_id": 9431339,
        "count": 107,
        "count_source": "search"
      },
      {
        "opinion_id": 9431340,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1501,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/michigan-v-chesternut.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgwNjEyMDQmcz05MzU0MDA2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112095+OR+9431339+OR+9431340%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112095,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 1243152,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 1853429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 2189647,
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
    "date_created": "2026-07-05T13:12:47Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:13:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:13:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:17:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:13:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Michigan v. Chesternut

```
<opinion type="majority">
<author id="b627-4"><page-number citation-index="1" label="569">*569</page-number>Justice Blackmun</author>
<p id="A7l">delivered the opinion of the Court.</p>
<p id="b627-5">In this case we review a determination by the Michigan Court of Appeals that any “investigatory pursuit” of a person undertaken by the police necessarily constitutes a seizure under the Fourth Amendment of the Constitution. We conclude that the police conduct in this case did not amount to a seizure, for it would not have communicated to a reasonable person that he was not at liberty to ignore the police presence and go about his business.</p>
<p id="b627-6">I</p>
<p id="b627-7">Early on the afternoon of December 19, 1984, four officers riding in a marked police cruiser were engaged in routine patrol duties in Metropolitan Detroit. As the cruiser came to an intersection, one of the officers observed a car pull over to the curb. A man got out of the car and approached respondent Michael Mose Chesternut, who was standing alone on the corner. When respondent saw the patrol car nearing the comer where he stood, he turned and began to run. As Officer Peltier, one of those in the car, later testified, the patrol car followed respondent around the corner “to see where he was going.” App. 25. The cruiser quickly caught up with respondent and drove alongside him for a short distance. As they drove beside him, the officers observed respondent discard a number of packets he pulled from his right-hand pocket. Officer Peltier got out of the cruiser to examine the packets. He discovered that they contained pills. While Peltier was engaged in this inspection, respondent, who had run only a few paces farther, stopped. Surmising on the basis of his experience as a paramedic that the pills contained codeine, Officer Peltier arrested respondent for the possession of narcotics and took him to the station house. During an ensuing search, the police discovered in respondent’s hatband another packet of pills, a packet containing heroin, and a hypodermic needle. Respondent was charged with knowingly and intentionally possessing heroin, tablets <page-number citation-index="1" label="570">*570</page-number>containing codeine, and tablets containing diazepam, all in violation of <span class="citation no-link">Mich. Comp. Laws §333.7403</span>(2) (1980).</p>
<p id="b628-4">At a preliminary hearing, at. which Officer Peltier was the only witness, respondent moved to dismiss the charges on the ground that he had been unlawfully seized during the police pursuit preceding his disposal of the packets. The presiding Magistrate granted the motion and dismissed the complaint.<footnotemark>1</footnotemark> Relying on <em>People </em>v. <em>Terrell, </em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">77 Mich. App. 676</a></span>, <span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">259 N. W. 2d 187</a></span> (1977),<footnotemark>2</footnotemark> the Magistrate ruled from the bench that a police “chase” like the one involved in this case implicated Fourth Amendment protections and could not be justified by the mere fact that the suspect ran at the sight of the police. App. 31-35. Applying a clearly-erroneous standard to the Magistrate’s ruling, the trial court upheld the dismissal order. <em>Id., </em>at 2-10.</p>
<p id="b628-5">The Michigan Court of Appeals “reluctantly” affirmed, <span class="citation" data-id="1853429"><a href="/opinion/1853429/people-v-chesternut/#184" aria-description="Citation for case: People v. Chesternut">157 Mich. App. 181, 184</a></span>, <span class="citation" data-id="1853429"><a href="/opinion/1853429/people-v-chesternut/#76" aria-description="Citation for case: People v. Chesternut">403 N. W. 2d 74, 76</a></span> (1986), noting that “although we find the result unfortunate, we cannot say that the lower court’s ruling was clearly erroneous under the present law or the facts presented.” <span class="citation" data-id="1853429"><a href="/opinion/1853429/people-v-chesternut/#183" aria-description="Citation for case: People v. Chesternut"><em>Id., </em>at 183</a></span>, <span class="citation" data-id="1853429"><a href="/opinion/1853429/people-v-chesternut/#75" aria-description="Citation for case: People v. Chesternut">403 N. W. <page-number citation-index="1" label="571">*571</page-number>2d, at 75</a></span>. Like the courts below it, the Court of Appeals rested its ruling on state precedents interpreting the Fourth Amendment.<footnotemark>3</footnotemark> The court determined, first, that any “investigatory pursuit” amounts to a seizure under <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). “As soon as the officers began their pursuit,” the court explained, “defendant’s freedom was restricted.” <span class="citation" data-id="1853429"><a href="/opinion/1853429/people-v-chesternut/#183" aria-description="Citation for case: People v. Chesternut">157 Mich. App., at 183</a></span>, <span class="citation" data-id="1853429"><a href="/opinion/1853429/people-v-chesternut/#75" aria-description="Citation for case: People v. Chesternut">403 N. W. 2d, at 75</a></span>. The court went on to conclude that respondent’s flight from the police was insufficient, by itself, to give rise to the particularized suspicion necessary to justify this kind of seizure. Because “the police saw [respondent] do absolutely nothing illegal nor did they observe other suspicious activity,” the court determined that the investigatory pursuit had violated the Fourth Amendment’s prohibition against unreasonable seizures. <span class="citation" data-id="1853429"><a href="/opinion/1853429/people-v-chesternut/#184" aria-description="Citation for case: People v. Chesternut"><em>Id., </em>at 184</a></span>, <span class="citation" data-id="1853429"><a href="/opinion/1853429/people-v-chesternut/#76" aria-description="Citation for case: People v. Chesternut">403 N. W. 2d, at 76</a></span>.</p>
<p id="b630-7"><page-number citation-index="1" label="572">*572</page-number>After the Michigan Supreme Court denied petitioner leave to appeal,<footnotemark>4</footnotemark> App. to Pet. for Cert. 9a, petitioner sought review here. We granted a 'writ of certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./484/895/">484 U. S. 895</a></span> (1987), to consider whether the officers’ pursuit of respondent constituted a seizure implicating Fourth Amendment protections, and, if so, whether the act of fleeing, by itself, was sufficient to constitute reasonable suspicion justifying that seizure. Because we conclude that the officers’ conduct did not constitute a seizure, we need not reach the second question.</p>
<p id="b630-8">h — I i</p>
<p id="Aov">A</p>
<p id="AMQ3">Petitioner argues that the Fourth Amendment is never implicated until an individual stops in response to the police’s show of authority. Thus, petitioner would have us rule that a lack of objective and particularized suspicion would not poison police conduct, no matter how coercive, as long as the police did not succeed in actually apprehending the individual. Respondent contends, in sharp contrast, that any and all police “chases” are Fourth Amendment seizures. Respondent would have us rule that the police may never pursue an individual absent a particularized and objective basis for suspecting that he is engaged in criminal activity.</p>
<p id="AHX2">Both petitioner and respondent, it seems to us, in their attempts to fashion a bright-line rule applicable to all investigatory pursuits, have failed to heed this Court’s clear direction that any assessment as to whether police conduct amounts to a seizure implicating the Fourth Amendment must take into account “ ‘all of the circumstances surrounding the incident’ ” in each individual case. <em>INS </em>v. <em>Delgado, </em><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#215" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 215</a></span> (1984), quoting <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 554</a></span> (1980) (opinion of Stewart, J.). Rather than adopting either rule proposed by the parties and determining that an investigatory pursuit is or is not <em>necessarily </em>a <page-number citation-index="1" label="573">*573</page-number>seizure under the Fourth Amendment, we adhere to our traditional contextual approach, and determine only that, in this particular case, the police conduct in question did not amount to a seizure.</p>
<p id="b631-5">B</p>
<p id="b631-6">In <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio</a></span>, </em>the Court noted:</p>
<blockquote id="b631-7">“Obviously, not all personal intercourse between policemen and citizens involves ‘seizures’ of persons. Only when the officer, by means of physical force or show of authority, has in some way restrained the liberty of a citizen may we conclude that a ‘seizure’ has occurred.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 19, n. 16</a></span>.</blockquote>
<p id="b631-8">A decade later in <em>United States </em>v. <em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span>, </em>Justice Stewart, writing for himself and then Justice Rehnquist, first transposed this analysis into a test to be applied in determining whether “a person has been ‘seized’ within the meaning of the Fourth Amendment.” <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S., at 554</a></span>.<footnotemark>5</footnotemark> The test provides that the police can be said to have seized an individual “only if, in view of all of the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave.” <em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Ibid.</a></span> </em>The Court has since embraced this test. See <em>INS </em>v. <em>Delgado, </em><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#215" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S., at 215</a></span>. See also <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#502" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 502</a></span> (1983) (plurality opinion); <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#514" aria-description="Citation for case: Florida v. Royer"><em>id., </em>at 514</a></span> (Blackmun, J., dissenting).</p>
<p id="b631-9">The test is necessarily imprecise, because it is designed to assess the coercive effect of police conduct, taken as a whole, rather than to focus on particular details of that conduct in isolation. Moreover, what constitutes a restraint on liberty prompting a person to conclude that he is not free to “leave” will vary, not only with the particular police conduct at issue, but also with the setting in which the conduct occurs. Compare <em>United States </em>v. <em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall, supra</a></span> </em>(consid<page-number citation-index="1" label="574">*574</page-number>ering whether police request to see identification and ticket of individual who stopped upon police’s approach constituted seizure), with <em>INS </em>v. <em><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado, supra</a></span> </em>(considering whether INS “factory survey” conducted while employees continued to move about constituted seizure of entire work force).</p>
<p id="b632-5">While the test is flexible enough to be applied to the whole range of police conduct in an equally broad range of settings, it calls for consistent application from one police encounter to the next, regardless of the particular individual’s response to the actions of the police. The test’s objective standard-looking to the reasonable man’s interpretation of the conduct in question — allows the police to determine in advance whether the conduct contemplated will implicate the Fourth Amendment. 3 W. LaFave, Search and Seizure § 9.2(h), pp. 407-408 (2d ed. 1987 and Supp. 1988). This “reasonable person” standard also ensures that the scope of Fourth Amendment protection does not vary with the state of mind of the particular individual being approached.</p>
<p id="b632-6">C</p>
<p id="b632-7">Applying the Court’s test to the facts of this case, we conclude that respondent was not seized by the police before he discarded the packets containing the controlled substance. Although Officer Peltier referred to the police conduct as a “chase,” and the Magistrate who originally dismissed the complaint was impressed by this description,<footnotemark>6</footnotemark> the characterization is not enough, standing alone, to implicate Fourth Amendment protections. Contrary to respondent’s assertion that a chase necessarily communicates that detention is <page-number citation-index="1" label="575">*575</page-number>intended and imminent, Brief for Respondent 9, the police conduct involved here would not have communicated to the reasonable person an attempt to capture or otherwise intrude upon respondent’s freedom of movement.<footnotemark>7</footnotemark> The record does not reflect that the police activated a siren or flashers; or that they commanded respondent to halt, or displayed any weapons; or that they operated the car in an aggressive manner to block respondent’s course or otherwise control the direction or speed of his movement. Tr. of Oral Arg. 2, 11, 20.<footnotemark>8</footnotemark> While the very presence of a police car driving parallel to a running pedestrian could be somewhat intimidating, this kind of police presence does not, standing alone, constitute a seizure.<footnotemark>9</footnotemark> Cf. <em>United States </em>v. <em>Knotts, </em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">460 U. S. 276</a></span> (1983) <page-number citation-index="1" label="576">*576</page-number>(holding that continuous surveillance on public thoroughfares by visual observation and electronic “beeper” does not constitute seizure); <em>Florida </em>v. Royer, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#497" aria-description="Citation for case: Florida v. Royer">460 U. S., at 497</a></span> (plurality opinion) (noting that mere approach by law enforcement officers, identified as such, does not constitute seizure). Without more, the police conduct here — a brief acceleration to catch up with respondent, followed by a short drive alongside him — was not “so intimidating” that respondent could reasonably have believed that he was not free to disregard the police presence and go about his business. <em>INS </em>v. <em>Delgado, </em><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#216" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S., at 216</a></span>. The police therefore were not required to have “a particularized and objective basis for suspecting [respondent] of criminal activity,” in order to pursue him. <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 417-418</a></span> (1981).</p>
<p id="b634-9">J-H HH</p>
<p id="b634-1">Because respondent was not unlawfully seized during the initial police pursuit, we conclude that charges against him were improperly dismissed. Accordingly, we reverse the judgment of the Michigan Court of Appeals, and remand the case to that court for further proceedings not inconsistent with this opinion.</p>
<p id="b634-2">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b628-6"> The Magistrate did not independently consider whether the codeine pills, if lawfully seized, established probable cause justifying respondent’s arrest. The Fourth Amendment issue before us is therefore limited to the police conduct preceding and including respondent’s disposal of the packets.</p>
</footnote>
<footnote label="2">
<p id="b628-7"> In <em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">Terrell</a></span>, </em>a police officer got out of his unmarked car and “gave chase” on foot after allegedly observing the defendant stick his hand in his pocket and run at the sight of the officer. <span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/#678" aria-description="Citation for case: People v. Terrell">77 Mich. App., at 678</a></span>, <span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/#188" aria-description="Citation for case: People v. Terrell">259 N. W. 2d, at 188</a></span>. According to the officer, the defendant ran into an apartment building where the officer observed him drop a clear envelope containing a brown powdery substance. Having determined that the package might contain heroin, the officer arrested the defendant. At a pretrial hearing, the trial court granted the defendant’s motion to suppress the envelope and its contents. The Michigan Court of Appeals affirmed, finding that the police “investigatory pursuit” constituted a seizure that was unjustified by any particularized suspicion that the defendant was engaged in criminal activity. <span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/#679" aria-description="Citation for case: People v. Terrell"><em>Id., </em>at 679-680</a></span>, <span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/#188" aria-description="Citation for case: People v. Terrell">259 N. W. 2d, at 188-189</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b629-5"> The Michigan Court of Appeals rested its holding on <em>People </em>v. <em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">Terrell, supra,</a></span> </em>and <em>People </em>v. <em>Shabaz, </em><span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/" aria-description="Citation for case: People v. Shabaz">424 Mich. 42</a></span>, <span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/" aria-description="Citation for case: People v. Shabaz">378 N. W. 2d 451</a></span> (1985), cert. dism’d (in view of that respondent’s death), <span class="citation multiple-matches"><a href="/c/U.%20S./478/1017/">478 U. S. 1017</a></span> (1986), both of which were to the effect that the defendant in question had been seized in violation of the Fourth Amendment of the United States Constitution. In <em>Shabaz, </em>the Michigan Supreme Court quoted “Michigan’s analogous [constitutional] provision,” without elaboration, in a footnote following a recitation of the Fourth Amendment. <span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/#52" aria-description="Citation for case: People v. Shabaz">424 Mich., at 52, n. 4</a></span>, <span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/#455" aria-description="Citation for case: People v. Shabaz">378 N. W. 2d, at 455, n. 4</a></span>. The Supreme Court said nothing to suggest that the Michigan Constitution’s seizure provision provided an independent source of relief, and the court’s entire analysis rested expressly on the Fourth Amendment and federal cases. Similarly, in <em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">Terrell</a></span>, </em>the Michigan Court of Appeals stated that the suppression of evidence and dismissal of charges against the defendant “was soundly based on existing law, state and Federal,” but made clear that the scope of the right in question was defined “by the Fourth Amendment’s general proscription against unreasonable searches and seizures.” <span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/#679" aria-description="Citation for case: People v. Terrell">77 Mich. App., at 679</a></span>, <span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/#188" aria-description="Citation for case: People v. Terrell">259 N. W. 2d, at 188</a></span>, citing <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20</a></span> (1968). In light of the bases for the courts’ decisions in <em>Shabaz </em>and <em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">Terrell</a></span>, </em>we readily conclude that the decision below likewise rests on the Michigan courts’ interpretation of the Federal Constitution and not on any adequate and independent state ground. See <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983). The defense in effect concedes this. See Tr. of Oral Arg. 38-39.</p>
</footnote>
<footnote label="4">
<p id="AJ6"> Two justices of the Michigan Supreme Court would have granted leave to appeal. See App. to Pet. for Cert. 10a.</p>
</footnote>
<footnote label="5">
<p id="b631-10"> Three other Justices, otherwise in the majority, chose not to reach the question whether the federal officers had seized respondent. <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#560" aria-description="Citation for case: United States v. Mendenhall">446 U. S., at 560</a></span> (opinion concurring in part and concurring in the judgment).</p>
</footnote>
<footnote label="6">
<p id="b632-8"> At the preliminary hearing, the Magistrate interrupted the State’s attorney, who was asserting that the police were simply performing routine patrolling duties, with the following:</p>
<blockquote id="b632-9">“That would be fine until the Officer said we were chasing him in the car, otherwise I would agree with you. My ears picked up when the Officer said that, you know. He said we went around. I asked him why were you chasing him in the car, why were you chasing him and he said because he was running and we wanted to see where he was going.” App. 29-30.</blockquote>
</footnote>
<footnote label="7">
<p id="b633-5"> As Officer Peltier explained, the goal of the “chase” was not to capture respondent, but “to see where he was going.” <em>Id., </em>at 25. Of course, the subjective intent of the officers is relevant to an assessment of the Fourth Amendment implications of police conduct only to the extent that that intent has been conveyed to the person confronted. <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S., at 554, n. 6</a></span> (opinion of Stewart, J.). See also 3 W. LaFave, Search and Seizure § 9.2(h), p. 407 (2d ed. 1987 and Supp. 1988) (uncommunicated intent of police irrelevant to determination of whether seizure occurred).</p>
</footnote>
<footnote label="8">
<p id="b633-6"> The facts of this case are not identical to the facts involved in both <em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">Terrell</a></span> </em>and <em>Shabaz, </em>upon which the Michigan courts relied in finding a seizure in this case. In both <em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">Terrell</a></span> </em>and <em>Shabaz, </em>a police officer got out of the car to chase the pedestrian suspect on foot, after which the defendant abandoned the inculpatory evidence. <em>People </em>v. <em>Terrell, </em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/#678" aria-description="Citation for case: People v. Terrell">77 Mich. App., at 678</a></span>, <span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/#188" aria-description="Citation for case: People v. Terrell">259 N. W. 2d, at 188</a></span>; <em>People </em>v. <em>Shabaz, </em><span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/#47" aria-description="Citation for case: People v. Shabaz">424 Mich., at 47-48</a></span>, <span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/#453" aria-description="Citation for case: People v. Shabaz">378 N. W. 2d, at 453</a></span>. In <em>Shabaz, </em>the State appears to have stipulated that the chase, whose clear object was to apprehend the defendant, constituted a seizure. <em>Id., </em>at 52, <span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/#455" aria-description="Citation for case: People v. Shabaz">378 N. W. 2d, at 455</a></span>. While no similar stipulation was entered in <em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">Terrell</a></span>, </em>the goal of that chase appears to have been equally clear. We, of course, intimate no view as to the federal constitutional correctness of either of those Michigan state-court cases.</p>
</footnote>
<footnote label="9">
<p id="b633-7"> The United States, which has submitted a brief as <em>amicus curiae, </em>suggests that, in some circumstances, police pursuit “will amount to a stop from the outset or from an early point in the chase, if the police command the person to halt and indicate that he is not free to go.” Brief for United States as <em>Amicus Curiae </em>13. Of course, such circumstances are not before <page-number citation-index="1" label="576">*576</page-number>us in this case. We therefore leave to another day the determination of the circumstances in which police pursuit could amount to a seizure under the Fourth Amendment.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Michigan v. Clifford.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Michigan v. Clifford"
type: case
citation: "464 U.S. 287 (1984)"
parallel_cite: "104 S. Ct. 641; 78 L. Ed. 2d 477; 52 U.S.L.W. 4056"
neutral_cite: 1984 U.S. LEXIS 14
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-01-11
docket: 82-357
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-01-11
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Michigan v. Clifford
  varies_by_point: false
  scope_note: "Plurality opinion (Powell, J., joined by Brennan, White, Marshall; Stevens, J., concurring in the judgment supplied the fifth vote on the result). The administrative-warrant / criminal-warrant framework for post-fire searches is the controlling teaching and is good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111057/michigan-v-clifford/"
  cluster_id: 111057
  opinion_id: 9429413
  identity_checked: true
homes:
  - page: "[[Emergency Aid]]"
    role: "Key — Limiting"
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Related (cross-doctrine)"
related: ["[[Michigan v. Tyler]]", "[[Camara v. Municipal Court]]", "[[Mincey v. Arizona]]", "[[Coolidge v. New Hampshire]]"]
aliases: []
tags: ["case", "fourth-amendment", "fire", "administrative-warrant", "exigent-circumstances", "privacy-interests"]
holding: "Where reasonable privacy interests remain in fire-damaged property, a post-fire investigative search after the blaze is out and the scene is secured requires a warrant absent consent or a new exigency; an administrative warrant suffices to determine cause and origin, but a search whose primary object is to gather evidence of crime requires a criminal warrant on probable cause."
lake:
  record_id: Michigan v. Clifford
  status: verified
  projected_at: 2026-07-09
---

# Michigan v. Clifford

*464 U.S. 287 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A fire damaged the Cliffords' home in the early morning while they were away. Hours after the blaze was out and firefighters had left, an arson investigator and his partner arrived, entered the secured, uninhabitable house without a warrant or consent, and searched the basement (finding evidence of arson) and then the upstairs living areas. The Cliffords had arranged to have the house boarded up, and personal belongings remained inside.

## Issue
Whether a warrantless, nonconsensual post-fire investigative search of a private home — conducted after the fire is extinguished and officials have left the scene — violates the Fourth Amendment, and what kind of warrant such a search requires.

## Rule
If reasonable privacy interests remain, a warrant is required: "If reasonable privacy interests remain in the fire-damaged property, the warrant requirement applies, and any official entry must be made pursuant to a warrant in the absence of consent or exigent circumstances." — 464 U.S. at 293 (plurality). ^pin-293

The object of the search sets the type of warrant: "If the primary object is to determine the cause and origin of a recent fire, an administrative warrant will suffice. . . . If the primary object of the search is to gather evidence of criminal activity, a criminal search warrant may be obtained only on a showing of probable cause." — *Id.* at 294. ^pin-294

Applied to a home: "we hold that the Cliffords retained reasonable privacy interests in their fire-damaged residence and that the postfire investigations were subject to the warrant requirement." — [*Id.* at 295](https://www.courtlistener.com/opinion/111057/michigan-v-clifford/#:~:text=we%20hold%20that%20the%20Cliffords). ^pin-295

## Application
Although the home was fire-damaged and uninhabitable, the exterior and some upstairs rooms were largely intact, personal belongings remained, and the Cliffords had secured the house against intrusion — so, given the strong privacy expectations in a home, reasonable privacy interests survived. The blaze was long out, officials had left, and the State claimed no [[Exigent Circumstances and Hot Pursuit|exigency]], so the later warrantless basement and upstairs searches were subject to the warrant requirement; because they were conducted without a warrant or consent, they were unconstitutional.

## Conclusion
The post-fire warrantless searches violated the Fourth Amendment. *Clifford* refines *[[Michigan v. Tyler|Tyler]]*: once the fire is out and the scene is no longer an emergency, further investigation of premises in which privacy interests remain requires a warrant — administrative for cause-and-origin, criminal (on probable cause) for evidence of arson.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (plurality; Stevens, J., concurred in the judgment).
- **Refines** [[Michigan v. Tyler]] by drawing the line at the end of the fire-fighting [[Exigent Circumstances and Hot Pursuit|exigency]] and dividing post-fire searches into administrative (cause/origin) and criminal (evidence) warrant tracks. Parallels the no-crime-scene-exception rule of [[Mincey v. Arizona]]; the administrative-warrant standard traces to [[Camara v. Municipal Court]].

## Appears on
- [[Emergency Aid]] — *Key — Limiting*
- [[Special Needs and Administrative Searches]] — *Related (cross-doctrine)*

## Sources
- *Michigan v. Clifford*, 464 U.S. 287 (1984) — https://www.courtlistener.com/opinion/111057/michigan-v-clifford/ — pinpoints: 293, 294, 295.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d3695a425a41704f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Michigan v. Clifford"}, "payload": {"all": [{"cite": "464 U.S. 287", "page": "287", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "464"}, {"cite": "104 S. Ct. 641", "page": "641", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "104"}, {"cite": "78 L. Ed. 2d 477", "page": "477", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "78"}, {"cite": "1984 U.S. LEXIS 14", "page": "14", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1984"}, {"cite": "52 U.S.L.W. 4056", "page": "4056", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "52"}], "display": "464 U.S. 287", "official": {"cite": "464 U.S. 287", "page": "287", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "464"}, "official_selection_present": true, "record_id": "Michigan v. Clifford"}}
{"assertion_id": "432c5ac310be53bc", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-295", "record_id": "Michigan v. Clifford"}, "payload": {"fragment": "#:~:text=we%20hold%20that%20the%20Cliffords", "page": null, "pin_id": "pin-295", "pinpoint_status": "star-verified", "quote": "we hold that the Cliffords retained reasonable privacy interests in their fire-damaged residence and that the postfire investigations were subject to the warrant requirement.", "quote_fidelity": "matched", "record_id": "Michigan v. Clifford", "star_marker": "295"}}
{"assertion_id": "b2c0cfb0f7dcdf81", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-294", "record_id": "Michigan v. Clifford"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-294", "pinpoint_status": "slip-only", "quote": "If the primary object is to determine the cause and origin of a recent fire, an administrative warrant will suffice. . . . If the primary object of the search is to gather evidence of criminal activity, a criminal search warrant may be obtained only on a showing of probable cause.", "quote_fidelity": "mismatch", "record_id": "Michigan v. Clifford", "star_marker": null}}
{"assertion_id": "f8e710335bc0ce12", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-293", "record_id": "Michigan v. Clifford"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-293", "pinpoint_status": "slip-only", "quote": "--- # Michigan v. Clifford *464 U.S. 287 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A fire damaged the Cliffords' home in the early morning while they were away. Hours after the blaze was out and firefighters had left, an arson investigator and his partner arrived, entered the secured, uninhabitable house without a warrant or consent, and searched the basement (finding evidence of arson) and then the upstairs living areas. The Cliffords had arranged to have the house boarded up, and personal belongings remained inside. ## Issue Whether a warrantless, nonconsensual post-fire investigative search of a private home — conducted after the fire is extinguished and officials have left the scene — violates the Fourth Amendment, and what kind of warrant such a search requires. ## Rule If reasonable privacy interests remain, a warrant is required:", "quote_fidelity": "mismatch", "record_id": "Michigan v. Clifford", "star_marker": null}}
{"assertion_id": "c1bdcfc36e85a6ca", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Michigan v. Clifford"}, "payload": {"as_of_content": "1984-01-11", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Michigan v. Clifford", "scope_note": "Plurality opinion (Powell, J., joined by Brennan, White, Marshall; Stevens, J., concurring in the judgment supplied the fifth vote on the result). The administrative-warrant / criminal-warrant framework for post-fire searches is the controlling teaching and is good law.", "varies_by_point": false}}
```

### lake record — Michigan v. Clifford

```json
{
  "schema_version": "s2.v1",
  "record_id": "Michigan v. Clifford",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Michigan v. Clifford",
    "case_name_short": "",
    "case_name_full": "MICHIGAN v. CLIFFORD Et Al.",
    "input_case_name": "Michigan v. Clifford",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-01-11",
    "year": 1984,
    "docket": "82-357",
    "cluster_id": 111057,
    "lead_opinion_id": 9429413,
    "sibling_ids": [
      111057,
      9429413,
      9429414,
      9429415
    ],
    "absolute_url": "/opinion/111057/michigan-v-clifford/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9350257,
        "score": 20,
        "case_name": "Michigan v. Clifford"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "464 U.S. 287",
      "volume": "464",
      "reporter": "U.S.",
      "page": "287",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 641",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "641",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "78 L. Ed. 2d 477",
        "volume": "78",
        "reporter": "L. Ed. 2d",
        "page": "477",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4056",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4056",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 14",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "14",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "464 U.S. 287",
        "volume": "464",
        "reporter": "U.S.",
        "page": "287",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 641",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "641",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "78 L. Ed. 2d 477",
        "volume": "78",
        "reporter": "L. Ed. 2d",
        "page": "477",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 14",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "14",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4056",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4056",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "464 U.S. 287",
    "official_selection": {
      "court_class": "scotus",
      "selected": "464 U.S. 287",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-293",
      "page": null,
      "quote": "--- # Michigan v. Clifford *464 U.S. 287 (1984)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A fire damaged the Cliffords' home in the early morning while they were away. Hours after the blaze was out and firefighters had left, an arson investigator and his partner arrived, entered the secured, uninhabitable house without a warrant or consent, and searched the basement (finding evidence of arson) and then the upstairs living areas. The Cliffords had arranged to have the house boarded up, and personal belongings remained inside. ## Issue Whether a warrantless, nonconsensual post-fire investigative search of a private home \u2014 conducted after the fire is extinguished and officials have left the scene \u2014 violates the Fourth Amendment, and what kind of warrant such a search requires. ## Rule If reasonable privacy interests remain, a warrant is required:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-294",
      "page": null,
      "quote": "If the primary object is to determine the cause and origin of a recent fire, an administrative warrant will suffice. . . . If the primary object of the search is to gather evidence of criminal activity, a criminal search warrant may be obtained only on a showing of probable cause.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-295",
      "page": null,
      "quote": "we hold that the Cliffords retained reasonable privacy interests in their fire-damaged residence and that the postfire investigations were subject to the warrant requirement.",
      "star_marker": "295",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 14913,
      "fragment": "#:~:text=we%20hold%20that%20the%20Cliffords",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-01-11",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Michigan v. Clifford",
    "varies_by_point": false,
    "scope_note": "Plurality opinion (Powell, J., joined by Brennan, White, Marshall; Stevens, J., concurring in the judgment supplied the fifth vote on the result). The administrative-warrant / criminal-warrant framework for post-fire searches is the controlling teaching and is good law.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Michigan v. Clifford:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Bodie Witzlib",
          "cluster_id": 2825238,
          "cite": [
            "796 F.3d 799",
            "2015 U.S. App. LEXIS 13811",
            "2015 WL 4664340"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Leland Earl Dart",
          "cluster_id": 443977,
          "cite": [
            "747 F.2d 263",
            "1984 U.S. App. LEXIS 17111"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane1_negative"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oliver v. United States",
          "cluster_id": 111146,
          "cite": [
            "80 L. Ed. 2d 214",
            "104 S. Ct. 1735",
            "466 U.S. 170",
            "1984 U.S. LEXIS 55",
            "52 U.S.L.W. 4425"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Burger",
          "cluster_id": 111927,
          "cite": [
            "96 L. Ed. 2d 601",
            "107 S. Ct. 2636",
            "482 U.S. 691",
            "1987 U.S. LEXIS 2725",
            "55 U.S.L.W. 4890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Wharton",
          "cluster_id": 1196421,
          "cite": [
            "809 P.2d 290",
            "53 Cal. 3d 522",
            "280 Cal. Rptr. 631",
            "91 Daily Journal DAR 4957",
            "91 Cal. Daily Op. Serv. 3426",
            "1991 Cal. LEXIS 1608"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Silvers",
          "cluster_id": 2014870,
          "cite": [
            "587 N.W.2d 325",
            "255 Neb. 702",
            "1998 Neb. LEXIS 230"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Woods",
          "cluster_id": 5607944,
          "cite": [
            "21 Cal. 4th 668",
            "99 Cal. Daily Op. Serv. 6990",
            "99 Daily Journal DAR 8867",
            "981 P.2d 1019",
            "88 Cal. Rptr. 2d 88",
            "1999 Cal. LEXIS 5534"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Donald P. Rohrig",
          "cluster_id": 728738,
          "cite": [
            "98 F.3d 1506",
            "1996 U.S. App. LEXIS 28274",
            "1996 WL 627521"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Woods",
          "cluster_id": 1160907,
          "cite": [
            "981 P.2d 1019",
            "88 Cal. Rptr. 2d 88",
            "21 Cal. 4th 668"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Scott",
          "cluster_id": 5690717,
          "cite": [
            "79 N.Y.2d 474"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Rooney",
          "cluster_id": 111943,
          "cite": [
            "97 L. Ed. 2d 258",
            "107 S. Ct. 2852",
            "483 U.S. 307",
            "1987 U.S. LEXIS 2870"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul Palmieri v. Pamela Lynch, AKA Pam Lynch, John Doe 1",
          "cluster_id": 788624,
          "cite": [
            "392 F.3d 73",
            "2004 U.S. App. LEXIS 25468",
            "2004 WL 2827676"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doering v. State",
          "cluster_id": 1525226,
          "cite": [
            "545 A.2d 1281",
            "313 Md. 384",
            "1988 Md. LEXIS 115"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alexander v. City And County Of San Francisco",
          "cluster_id": 674655,
          "cite": [
            "29 F.3d 1355",
            "94 Cal. Daily Op. Serv. 5278",
            "94 Daily Journal DAR 9698",
            "1994 U.S. App. LEXIS 16752"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111057 OR 9429413 OR 9429414 OR 9429415) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 181,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 181,
        "triage_read": 4,
        "triage_snippet_classified": 177
      },
      "lane2_top_cited": {
        "query": "cites:(111057 OR 9429413 OR 9429414 OR 9429415)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NSZzPTEzNTU2NTQmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111057+OR+9429413+OR+9429414+OR+9429415%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111057 OR 9429413 OR 9429414 OR 9429415)",
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
    "complete_query": "cites:(111057 OR 9429413 OR 9429414 OR 9429415)",
    "indexed_citing_opinions": 233,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111057,
        "count": 212,
        "count_source": "search"
      },
      {
        "opinion_id": 9429413,
        "count": 24,
        "count_source": "search"
      },
      {
        "opinion_id": 9429414,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429415,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 346,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/michigan-v-clifford.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU1Mjk2MDUmcz03MzI3MDE1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111057+OR+9429413+OR+9429414+OR+9429415%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111057,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 109876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 110530,
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
    "date_created": "2026-07-05T13:17:01Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:17:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:17:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:21:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:17:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Michigan v. Clifford

```
<opinion type="majority">
<author id="b400-10">Justice Powell</author>
<p id="Akt">announced the judgment of the Court and delivered an opinion,</p>
<judges id="AL8">in which Justice Brennan, Justice White, and Justice Marshall joined.</judges>
<p id="b400-11">This case presents questions as to the authority of arson investigators, in the absence of exigent circumstances or consent, to enter a private residence without a warrant to investigate the cause of a recent fire.</p>
<p id="b401-3"><page-number citation-index="1" label="289">*289</page-number>Respondents, Raymond and Emma Jean Clifford, were arrested and charged with arson in connection with a fire at their private residence. At the preliminary examination held to establish probable cause for the alleged offense, the State introduced various pieces of physical evidence, most of which was obtained through a warrantless and nonconsensual search of the Cliffords’ fire-damaged home. Respondents moved to suppress this evidence on the ground that it was obtained in violation of their rights under the Fourth and Fourteenth Amendments. That motion was denied and respondents were bound over for trial. Before trial, they again moved to suppress the evidence obtained during the search. The trial court conducted an evidentiary hearing and denied the motion on the ground that exigent circumstances justified the search. The court certified its eviden-tiary ruling for interlocutory appeal and the Michigan Court of Appeals reversed.</p>
<p id="b401-4">That court held that there were no exigent circumstances justifying the search. Instead, it found that the warrantless entry and search of the Clifford residence were conducted pursuant to a policy of the Arson Division of the Detroit Fire Department that sanctioned such searches as long as the owner was not present, the premises were open to trespass, and the search occurred within a reasonable time of the fire. The Court of Appeals held that this policy was inconsistent with <em>Michigan </em>v. <em>Tyler, </em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499</a></span> (1978), and that the warrantless nonconsensual search of the Cliffords’ residence violated their rights under the Fourth and Fourteenth Amendments. We granted certiorari to clarify doubt that appears to exist as to the application of our decision in <em>Tyler. </em><span class="citation multiple-matches"><a href="/c/U.%20S./459/1168/">459 U. S. 1168</a></span> (1983).</p>
<p id="b401-5">II</p>
<p id="b401-6">In the early morning hours of October 18, 1980, a fire erupted at the Clifford home. The Cliffords were out of town on a camping trip at the time. The fire was reported to the Detroit Fire Department, and fire units arrived on the <page-number citation-index="1" label="290">*290</page-number>scene about 5:40 a. m. The fire was extinguished and all fire officials and police left the premises at 7:04 a. m.</p>
<p id="b402-5">At 8 o’clock on the morning of the fire, Lieutenant Beyer, a fire investigator with the arson section of the Detroit Fire Department, received instructions to investigate the Clifford fire. He was informed that the Fire Department suspected arson. Because he had other assignments, Lieutenant Beyer did not proceed immediately to the Clifford residence. He and his partner finally arrived at the scene of the fire about 1 p. m. on October 18.</p>
<p id="b402-6">When they arrived, they found a work crew on the scene. The crew was boarding up the house and pumping some six inches of water out of the basement. A neighbor told the investigators that he had called Mr. Clifford and had been instructed to request the Cliffords’ insurance agent to send a boarding crew out to secure the house. The neighbor also advised that the Cliffords did not plan to return that day. While the investigators waited for the water to be pumped out, they found a Coleman fuel can in the driveway that was seized and marked as evidence.<footnotemark>1</footnotemark></p>
<p id="b402-7">By 1:30 p. m., the water had been pumped out of the basement and Lieutenant Beyer and his partner, without obtaining consent or an administrative warrant, entered the Clifford residence and began their investigation into the cause of the fire. Their search began in the basement and they quickly confirmed that the fire had originated there beneath the basement stairway. They detected a strong odor of fuel throughout the basement, and found two more Coleman fuel cans beneath the stairway. As they dug through the debris, the investigators also found a crock pot with attached wires leading to an electrical timer that was plugged into an outlet <page-number citation-index="1" label="291">*291</page-number>a few feet away. The timer was set to turn on at approximately 3:45 a. m. and to turn back off at approximately 9 a. m. It had stopped somewhere between 4 and 4:30 a. m. All of this evidence was seized and marked.</p>
<p id="b403-5">After determining that the fire had originated in the basement, Lieutenant Beyer and his partner searched the remainder of the house. The warrantless search that followed was extensive and thorough. The investigators called in a photographer to take pictures throughout the house. They searched through drawers and closets and found them full of old clothes. They inspected the rooms and noted that there were nails on the walls but no pictures. They found wiring and cassettes for a video tape machine but no machine.</p>
<p id="b403-6">Respondents moved to exclude all exhibits and testimony based on the basement and upstairs searches on the ground that they were searches to gather evidence of arson, that they were conducted without a warrant, consent, or exigent circumstances, and that they therefore were <em>per se </em>unreasonable under the Fourth and Fourteenth Amendments. Petitioner, on the other hand, argues that the entire search was reasonable and should be exempt from the warrant requirement.</p>
<p id="b403-7">Ill</p>
<p id="b403-8">In its petition for certiorari, the State does not challenge the state court’s finding that there were no exigent circumstances justifying the search of the Clifford home. Instead, it asks us to exempt from the warrant requirement all administrative investigations into the cause and origin of a fire. We decline to do so.</p>
<p id="b403-9">In <em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">Tyler</a></span>, </em>we restated the Court’s position that administrative searches generally require warrants. <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#504" aria-description="Citation for case: Michigan v. Tyler">436 U. S., at 504-508</a></span>. See <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307</a></span> (1978); <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967); <em>See </em>v. <em>City of Seattle, </em><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967). We reaffirm that view again today. Except in certain carefully defined <page-number citation-index="1" label="292">*292</page-number>classes of cases,<footnotemark>2</footnotemark> the nonconsensual entry and search of property are governed by the warrant requirement of the Fourth and Fourteenth Amendments. The constitutionality of warrantless and nonconsensual entries onto fire-damaged premises, therefore, normally turns on several factors: whether there are legitimate privacy interests in the fire-damaged property that are protected by the Fourth Amendment; whether exigent circumstances justify the government intrusion regardless of any reasonable expectations of privacy; and, whether the object of the search is to determine the cause of fire or to gather evidence of criminal activity.</p>
<p id="b404-5">A</p>
<p id="b404-6">We observed in <em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">Tyler</a></span> </em>that reasonable privacy expectations may remain in fire-damaged premises. “People may go on living in their homes or working in their offices after a fire. Even when that is impossible, private effects often remain on the fire-damaged premises.” <em>Tyler, </em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#505" aria-description="Citation for case: Michigan v. Tyler">436 U. S., at 505</a></span>. Privacy expectations will vary with the type of property, the amount of fire damage, the prior and continued use of the premises, and in some cases the owner’s efforts to secure it against intruders. Some fires may be so devastating that no reasonable privacy interests remain in the ash and ruins, regardless of the owner’s subjective expectations. The test essentially is an objective one: whether “the expectation [is] one that society is prepared to recognize as ‘reasonable.’” <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 361</a></span> (1967) (Harlan, J., concurring). See also <em>Smith </em>v. <em>Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#739" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735, 739-741</a></span> (1979). If reasonable privacy interests remain in <page-number citation-index="1" label="293">*293</page-number>the fire-damaged property, the warrant requirement applies, and any official entry must be made pursuant to a warrant in the absence of consent or exigent circumstances.</p>
<p id="b405-5">B</p>
<p id="b405-6">A burning building of course creates an exigency that justifies a warrantless entry by fire officials to fight the blaze. Moreover, in <em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">Tyler</a></span> </em>we held that once in the building, officials need no warrant to remain<footnotemark>3</footnotemark> for “a reasonable time to investigate the cause of a blaze after it has been extinguished.” 436 U. S., at 510. Where, however, reasonable expectations of privacy remain in the fire-damaged property, additional investigations begun after the fire has been extinguished and fire and police officials have left the scene, generally must be made pursuant to a warrant or the identification of.some new exigency.</p>
<p id="b405-7">The aftermath of a fire often presents exigencies that will not tolerate the delay necessary to obtain a warrant or to secure the owner’s consent to inspect fire-damaged premises.<footnotemark>4</footnotemark> Because determining the cause and origin of a fire serves a compelling public interest, the warrant requirement does not apply in such cases.</p>
<p id="b406-4"><page-number citation-index="1" label="294">*294</page-number>c</p>
<p id="b406-5">If a warrant is necessary, the object of the search determines the type of warrant required. If the primary object is to determine the cause and origin of a recent fire, an administrative warrant will suffice.<footnotemark>6</footnotemark> To obtain such a warrant, fire officials need show only that a fire of undetermined origin has occurred on the premises, that the scope of the proposed search is reasonable and will not intrude unnecessarily on the fire victim’s privacy, and that the search will be executed at a reasonable and convenient time.</p>
<p id="b406-6">If the primary object of the search is to gather evidence of criminal activity, a criminal search warrant may be obtained only on a showing of probable cause to believe that relevant evidence will be found in the place to be searched. If evidence of criminal activity is discovered during the course of a valid administrative search, it may be seized under the “plain view” doctrine. <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#465" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 465-466</a></span> (1971). This evidence then may be used to establish probable cause to obtain a criminal search warrant. Fire officials may not, however, rely on this evidence to expand the scope of their administrative search without first making a successful showing of probable cause to an independent judicial officer.</p>
<p id="b406-7">The object of the search is important even if exigent circumstances exist. Circumstances that justify a warrantless search for the cause of a fire may not justify a search to gather evidence of criminal activity once that cause has been determined. If, for example, the administrative search is justified by the immediate need to ensure against rekindling, the scope of the search may be no broader than reasonably <page-number citation-index="1" label="295">*295</page-number>necessary to achieve its end. A search to gather evidence of criminal activity not in plain view must be made pursuant to a criminal warrant upon a traditional showing of probable cause.<footnotemark>6</footnotemark></p>
<p id="b407-5">The searches of the Clifford home, at least arguably, can be viewed as two separate ones: the delayed search of the basement area, followed by the extensive search of the residential portion of the house. We now apply the principles outlined above to each of these searches.</p>
<p id="b407-6">IV</p>
<p id="b407-7">The Clifford home was a two-and-one-half story brick and frame residence. Although there was extensive damage to the lower interior structure, the exterior of the house and some of the upstairs rooms were largely undamaged by the fire, although there was some smoke damage. The firemen had broken out one of the doors and most of the windows in fighting the blaze. At the time Lieutenant Beyer and his partner arrived, the home was uninhabitable. But personal belongings remained, and the Cliffords had arranged to have the house secured against intrusion in their absence. Under these circumstances, and in light of the strong expectations of privacy associated with a home, we hold that the Cliffords retained reasonable privacy interests in their fire-damaged residence and that the postfire investigations were subject to the warrant requirement. Thus, the warrantless and non-consensual searches of both the basement and the upstairs areas of the house would have been valid only if exigent circumstances had justified the object and the scope of each.</p>
<p id="b408-4"><page-number citation-index="1" label="296">*296</page-number>A</p>
<p id="b408-5">As noted, the State does not claim that exigent circumstances justified its postfire searches. It argues that we either should exempt postfire searches from the warrant requirement or modify <em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">Tyler</a></span> </em>to justify the warrantless searches in this case. We have rejected the State’s first argument and turn now to its second.</p>
<p id="b408-6">In <em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">Tyler</a></span> </em>we upheld a warrantless postfire search of a furniture store, despite the absence of exigent circumstances, on the ground that it was a continuation of a valid search begun immediately after the fire. The investigation was begun as the last flames were being doused, but could not be completed because of smoke and darkness. The search was resumed promptly after the smoke cleared and daylight dawned. Because the postfire search was interrupted for reasons that were evident, we held that the early morning search was “no more than an actual continuation of the first, and the lack of a warrant thus did not invalidate the resulting seizure of evidence.” 436 U. S., at 511.</p>
<p id="b408-7">As the State conceded at oral argument, this case is distinguishable for several reasons. First, the challenged search was not a continuation of an earlier search. Between the time the firefighters had extinguished the blaze and left the scene and the arson investigators first arrived about 1 p. m. to begin their investigation, the Cliffords had taken steps to secure the privacy interests that remained in their residence against further intrusion. These efforts separate the entry made to extinguish the blaze from that made later by different officers to investigate its origin. Second, the privacy interests in the residence — particularly after the Cliffords had acted — were significantly greater than those in the fire-damaged furniture store, making the delay between the fire and the midday search unreasonable absent a warrant, consent, or exigent circumstances. We frequently have noted that privacy interests are especially strong in a private resi-<page-number citation-index="1" label="297">*297</page-number>deuce.<footnotemark>7</footnotemark> These facts — the interim efforts to secure the burned-out premises and the heightened privacy interests in the home — distinguish this case from <em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">Tyler</a></span>. </em>At least where a homeowner has made a reasonable effort to secure his fire-damaged home after the blaze has been extinguished and the fire and police units have left the scene, we hold that a subsequent postfire search must be conducted pursuant to a warrant, consent, or the identification of some new exigency.<footnotemark>8</footnotemark> So long as the primary purpose is to ascertain the cause of the fire, an administrative warrant will suffice.</p>
<p id="b409-5">B</p>
<p id="b409-6">Because the cause of the fire was then known, the search of the upper portions of the house, described above, could only have been a search to gather evidence of the crime of arson. Absent exigent circumstances, such a search requires a criminal warrant.</p>
<p id="b409-7">Even if the midday basement search had been a valid administrative search, it would not have justified the upstairs search. The scope of such a search is limited to that reasonably necessary to determine the cause and origin of a fire and to ensure against rekindling. As soon as the investigators determined that the fire had originated in the basement and had been caused by the crock pot and timer found beneath <page-number citation-index="1" label="298">*298</page-number>the basement stairs, the scope of their search was limited to the basement area. Although the investigators could have used whatever evidence they discovered in the basement to establish probable cause to search the remainder of the house, they could not lawfully undertake that search without a prior judicial determination that a successful showing of probable cause had been made. Because there were no exigent circumstances justifying the upstairs search, and it was undertaken without a prior showing of probable cause before an independent judicial officer, we hold that this search of a home was unreasonable under the Fourth and Fourteenth Amendments, regardless of the validity of the basement search.<footnotemark>9</footnotemark></p>
<p id="b410-5">The warrantless intrusion into the upstairs regions of the Clifford house presents a telling illustration of the importance of prior judicial review of proposed administrative searches. If an administrative warrant had been obtained in this case, it presumably would have limited the scope of the proposed investigation and would have prevented the warrantless intrusion into the upper rooms of the Clifford home. An administrative search into the cause of a recent fire does not give fire officials license to roam freely through the fire victim’s private residence.</p>
<p id="b410-6">V</p>
<p id="b410-7">The only pieces of physical evidence that have been challenged on this interlocutory appeal are the three empty fuel <page-number citation-index="1" label="299">*299</page-number>cans, the electric crock pot, and the timer and attached cord. Respondents also have challenged the testimony of the investigators concerning the warrantless search of both the basement and the upstairs portions of the Clifford home. The discovery of two of the fuel cans, the crock pot, the timer and cord — as well as the investigators’ related testimony — were the product of the unconstitutional postfire search of the Cliffords’ residence. Thus, we affirm that portion of the judgment of the Michigan Court of Appeals that excluded that evidence. One of the fuel cans was discovered in plain view in the Cliffords’ driveway. This can was seen in plain view during the initial investigation by the firefighters. It would have been admissible whether it had been seized in the basement by the firefighters or in the driveway by the arson investigators. Exclusion of this evidence should be reversed.</p>
<p id="b411-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b402-8"> The can had been found in the basement by the fire officials who had fought the blaze. The firemen removed the can and put it by the side door where Lieutenant Beyer discovered it on his arrival.</p>
</footnote>
<footnote label="2">
<p id="b404-7"> See, <em>e. g., Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">452 U. S. 594</a></span> (1981) (heavily regulated business); <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972) (same); <em>Colonnade Corp. </em>v. <em>United States, </em><span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970) (same). The exceptions to the warrant requirement recognized in these cases are not applicable to the warrantless search in this case.</p>
</footnote>
<footnote label="3">
<p id="b405-8"> We do not suggest that firemen fighting a fire normally remain within a building. The circumstances, of course, vary. In many situations actual entry may be too hazardous until the fire has been wholly extinguished, and even then the danger of collapsing walls may exist. Thus, the effort to ascertain the cause of a fire may extend over a period of time with entry and reentry. The critical inquiry is whether reasonable expectations of privacy exist in the fire-damaged premises at a particular time, and if so, whether exigencies justify the reentries.</p>
</footnote>
<footnote label="4">
<p id="b405-9"> For example, an immediate threat that the blaze might rekindle presents an exigency that would justify a warrantless and nonconsensual postfire investigation. “Immediate investigation may also be necessary to preserve evidence from intentional or accidental destruction.” See <em>Michigan </em>v. <em>Tyler, </em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#510" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 510</a></span> (1978).</p>
</footnote>
<footnote label="5">
<p id="b406-8"> Probable cause to issue an administrative warrant exists if reasonable legislative, administrative, or judicially prescribed standards for conducting an inspection are satisfied with respect to a particular dwelling. See particularly <em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">Tyler, supra;</a></span> </em>see also <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#538" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 538</a></span> (1967).</p>
</footnote>
<footnote label="6">
<p id="b407-8"> The plain-view doctrine must be applied in light of the special circumstances that frequently accompany fire damage. In searching solely to ascertain the cause, firemen customarily must remove rubble or search other areas where the cause of fires is likely to be found. An object that comes into view during such a search may be preserved without a warrant.</p>
</footnote>
<footnote label="7">
<p id="b409-8"> See, <em>e. g., Payton </em>v. <em>New York, </em><span class="citation multiple-matches"><a href="/c/U.%20S./445/578/">445 U. S. 578</a></span>, 589-590 (1980); <em>United States </em>v. <em>United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span> (1972). Reasonable expectations of privacy in fire-damaged premises will vary depending particularly on the type and use of the building involved. Expectations of privacy are particularly strong in private residences and offices. There may be, depending upon the circumstances, diminished privacy expectations in commercial premises.</p>
</footnote>
<footnote label="8">
<p id="b409-9"> This is not to suggest that individual expectations of privacy may prevail over interests of public safety. For example, when fire breaks out in an apartment unit of an apartment complex, the exigency exception may allow warrantless postfire investigations where necessary to ensure against any immediate danger of future fire hazard.</p>
</footnote>
<footnote label="9">
<p id="b410-8"> In many cases, there will be no bright line separating the firefighters’ investigation into the cause of a fire from a search for evidence of arson. The distinction will vary with the circumstances of the particular fire and generally will involve more than the lapse of time or the number of entries and reentries. For example, once the cause of a fire in a single-family dwelling is determined, the administrative search should end, and any broader investigation should be made pursuant to a criminal warrant. A fire in an apartment, on the other hand, may present complexities that make it necessary for officials to conduct more expansive searches, to remain on the premises for longer periods of time, and to make repeated entries and reentries into the building. See <em>Tyler, </em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#510" aria-description="Citation for case: Michigan v. Tyler">436 U. S., at 510, n. 6</a></span>.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Michigan v. DeFillippo.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Michigan v. DeFillippo"
type: case
citation: "443 U.S. 31 (1979)"
parallel_cite: "99 S. Ct. 2627; 61 L. Ed. 2d 343"
neutral_cite: 1979 U.S. LEXIS 135
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-06-25
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1979-06-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Michigan v. DeFillippo
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110127/michigan-v-defillippo/"
  cluster_id: 110127
  opinion_id: 110127
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Leon]]", "[[Illinois v. Krull]]", "[[Herring v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "probable-cause", "arrest", "good-faith"]
holding: "An arrest based on a presumptively valid ordinance later declared unconstitutional was valid (supported by probable cause at the time),…"
lake:
  record_id: Michigan v. DeFillippo
  status: verified
  projected_at: 2026-07-06
---

# Michigan v. DeFillippo

*443 U.S. 31 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Detroit ordinance made it a crime for a person to refuse to identify himself to police under certain circumstances. Officers found DeFillippo in an alley with a woman, and when he repeatedly refused to identify himself they arrested him under the ordinance; a search incident to that arrest turned up drugs. The identification ordinance was later held unconstitutionally vague.

## Issue
Whether evidence seized in a search incident to an arrest under a presumptively valid ordinance must be suppressed once the ordinance is later declared unconstitutional.

## Rule
No. "The subsequently determined invalidity of the Detroit ordinance on vagueness grounds does not undermine the validity of the arrest made for violation of that ordinance, and the evidence discovered in the search of respondent should not have been suppressed." — 443 U.S. at 40. ^pin-40

At the time of the arrest the officers had probable cause to believe DeFillippo was violating a presumptively valid ordinance; police are charged to enforce ordinances until they are judicially declared invalid.

## Application
When the officers arrested DeFillippo, the identification ordinance had not yet been declared unconstitutional, so his refusal to identify himself gave them probable cause to arrest under a presumptively valid law. The search that produced the drugs was incident to that lawful arrest, and the ordinance's later invalidation did not retroactively render the arrest or search unlawful; the evidence should not have been suppressed.

## Conclusion
Reversed; suppression of the evidence was unwarranted.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *DeFillippo* anticipates the good-faith line of [[United States v. Leon]] and the reliance-on-a-statute analysis of [[Illinois v. Krull]].

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *Michigan v. DeFillippo*, 443 U.S. 31 (1979) — https://www.courtlistener.com/opinion/110127/michigan-v-defillippo/ — pinpoint: 40.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5bb33466756497a0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Michigan v. DeFillippo"}, "payload": {"all": [{"cite": "443 U.S. 31", "page": "31", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "443"}, {"cite": "99 S. Ct. 2627", "page": "2627", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "99"}, {"cite": "61 L. Ed. 2d 343", "page": "343", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "61"}, {"cite": "1979 U.S. LEXIS 135", "page": "135", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1979"}], "display": "443 U.S. 31", "official": {"cite": "443 U.S. 31", "page": "31", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "443"}, "official_selection_present": true, "record_id": "Michigan v. DeFillippo"}}
{"assertion_id": "9094fae5afdc4bc4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-40", "record_id": "Michigan v. DeFillippo"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-40", "pinpoint_status": "slip-only", "quote": "--- # Michigan v. DeFillippo *443 U.S. 31 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Detroit ordinance made it a crime for a person to refuse to identify himself to police under certain circumstances. Officers found DeFillippo in an alley with a woman, and when he repeatedly refused to identify himself they arrested him under the ordinance; a search incident to that arrest turned up drugs. The identification ordinance was later held unconstitutionally vague. ## Issue Whether evidence seized in a search incident to an arrest under a presumptively valid ordinance must be suppressed once the ordinance is later declared unconstitutional. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "Michigan v. DeFillippo", "star_marker": null}}
{"assertion_id": "2a7570a0be9bc4f9", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Michigan v. DeFillippo"}, "payload": {"as_of_content": "1979-06-25", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Michigan v. DeFillippo", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Michigan v. DeFillippo

```json
{
  "schema_version": "s2.v1",
  "record_id": "Michigan v. DeFillippo",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Michigan v. DeFillippo",
    "case_name_short": "DeFillippo",
    "case_name_full": "MICHIGAN v. DeFILLIPPO",
    "input_case_name": "Michigan v. DeFillippo",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-06-25",
    "year": 1979,
    "docket": null,
    "cluster_id": 110127,
    "lead_opinion_id": 110127,
    "sibling_ids": [
      110127,
      9427654,
      9427655,
      9427656
    ],
    "absolute_url": "/opinion/110127/michigan-v-defillippo/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "443 U.S. 31",
      "volume": "443",
      "reporter": "U.S.",
      "page": "31",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 2627",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2627",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 343",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "343",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 135",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "135",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "443 U.S. 31",
        "volume": "443",
        "reporter": "U.S.",
        "page": "31",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 2627",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2627",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 343",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "343",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 135",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "135",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "443 U.S. 31",
    "official_selection": {
      "court_class": "scotus",
      "selected": "443 U.S. 31",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-40",
      "page": null,
      "quote": "--- # Michigan v. DeFillippo *443 U.S. 31 (1979)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Detroit ordinance made it a crime for a person to refuse to identify himself to police under certain circumstances. Officers found DeFillippo in an alley with a woman, and when he repeatedly refused to identify himself they arrested him under the ordinance; a search incident to that arrest turned up drugs. The identification ordinance was later held unconstitutionally vague. ## Issue Whether evidence seized in a search incident to an arrest under a presumptively valid ordinance must be suppressed once the ordinance is later declared unconstitutional. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1979-06-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Michigan v. DeFillippo",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Mickel",
          "cluster_id": 10680424,
          "cite": [
            "321 Ga. 751"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pat Reed, Commissioner of the WV DMV v. Joseph M. Winesburg",
          "cluster_id": 4597286,
          "cite": [
            "825 S.E.2d 85"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Marlow Humbert v. Mayor and City Council of Baltimore City",
          "cluster_id": 4416687,
          "cite": [
            "866 F.3d 546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lauren Graham v. C. Gagnon",
          "cluster_id": 4242146,
          "cite": [
            "831 F.3d 176",
            "2016 U.S. App. LEXIS 13672",
            "2016 WL 4011156"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Glenda Smith v. City of Wyoming",
          "cluster_id": 3194781,
          "cite": [
            "821 F.3d 697",
            "2016 FED App. 0094P",
            "2016 U.S. App. LEXIS 6833",
            "2016 WL 1533998"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Arredondo",
          "cluster_id": 6238731,
          "cite": [
            "199 Cal. Rptr. 3d 563",
            "245 Cal. App. 4th 186",
            "2016 Cal. App. LEXIS 153"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mocek v. City of Albuquerque",
          "cluster_id": 3164764,
          "cite": [
            "813 F.3d 912",
            "2015 U.S. App. LEXIS 22435",
            "2015 WL 9298662"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Cahaly v. Paul LaRosa, III",
          "cluster_id": 2823574,
          "cite": [
            "796 F.3d 399",
            "2015 WL 4646922"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
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
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fadul",
          "cluster_id": 7306139,
          "cite": [
            "16 F. Supp. 3d 270",
            "2014 WL 1584044"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Hogan v. City of Corpus Christi, Texas",
          "cluster_id": 1033766,
          "cite": [
            "722 F.3d 725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane1_negative"
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
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
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
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennhurst State School and Hospital v. Halderman",
          "cluster_id": 111094,
          "cite": [
            "79 L. Ed. 2d 67",
            "104 S. Ct. 900",
            "465 U.S. 89",
            "1984 U.S. LEXIS 4",
            "52 U.S.L.W. 4155"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
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
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
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
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kim D. Lee v. Luis Ferraro",
          "cluster_id": 75789,
          "cite": [
            "284 F.3d 1188",
            "2002 U.S. App. LEXIS 3438",
            "2002 WL 340670"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Krull",
          "cluster_id": 111835,
          "cite": [
            "94 L. Ed. 2d 364",
            "107 S. Ct. 1160",
            "480 U.S. 340",
            "1987 U.S. LEXIS 1061",
            "55 U.S.L.W. 4291"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
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
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Howard",
          "cluster_id": 5684310,
          "cite": [
            "50 N.Y.2d 583",
            "408 N.E.2d 908",
            "430 N.Y.S.2d 578",
            "1980 N.Y. LEXIS 2454"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
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
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cindy Abbott v. Sangamon County",
          "cluster_id": 816250,
          "cite": [
            "705 F.3d 706",
            "2013 WL 322920",
            "2013 U.S. App. LEXIS 1963"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Katherine Gardenhire and Walter Gardenhire v. Donald Schubert, in His Individual and Official Capacity as Chief of Police",
          "cluster_id": 767858,
          "cite": [
            "205 F.3d 303",
            "2000 U.S. App. LEXIS 3126",
            "2000 WL 232311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wheeler v. Lawson",
          "cluster_id": 1427057,
          "cite": [
            "539 F.3d 629",
            "2008 U.S. App. LEXIS 17792",
            "2008 WL 3866950"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
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
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James N. Gramenos v. Jewel Companies, Inc.",
          "cluster_id": 474259,
          "cite": [
            "797 F.2d 432"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. White",
          "cluster_id": 1194272,
          "cite": [
            "640 P.2d 1061",
            "97 Wash. 2d 92",
            "1982 Wash. LEXIS 1262"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 1104481,
          "cite": [
            "461 So. 2d 686"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
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
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
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
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicole Schneyder v. Gina Smith",
          "cluster_id": 222150,
          "cite": [
            "653 F.3d 313",
            "2011 U.S. App. LEXIS 15831",
            "2011 WL 3211504"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Peterson Novelties, Inc v. City of Berkley",
          "cluster_id": 2179551,
          "cite": [
            "672 N.W.2d 351",
            "259 Mich. App. 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gonzalez v. City of Elgin",
          "cluster_id": 1456587,
          "cite": [
            "578 F.3d 526",
            "2009 U.S. App. LEXIS 18724",
            "2009 WL 2525565"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark A. Criss v. The City of Kent Rick Haury, Officer, Kent City Police Department",
          "cluster_id": 518124,
          "cite": [
            "867 F.2d 259",
            "1988 U.S. App. LEXIS 17645",
            "1988 WL 146871"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gaetano Modica",
          "cluster_id": 396890,
          "cite": [
            "663 F.2d 1173",
            "1981 U.S. App. LEXIS 16444"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. DeFillippo:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110127 OR 9427654 OR 9427655 OR 9427656) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjU5ODg0ODAwMDAwJnM9MTg3NDkzJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110127+OR+9427654+OR+9427655+OR+9427656%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110127 OR 9427654 OR 9427655 OR 9427656)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMTImcz02ODI3NTImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110127+OR+9427654+OR+9427655+OR+9427656%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110127 OR 9427654 OR 9427655 OR 9427656)",
        "reviewed": 35,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 35,
        "triage_read": 1,
        "triage_snippet_classified": 34
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110127 OR 9427654 OR 9427655 OR 9427656)",
    "indexed_citing_opinions": 840,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110127,
        "count": 747,
        "count_source": "search"
      },
      {
        "opinion_id": 9427654,
        "count": 102,
        "count_source": "search"
      },
      {
        "opinion_id": 9427655,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427656,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1695,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/michigan-v-defillippo.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3MzA1NzUmcz05NDg4OTE4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110127+OR+9427654+OR+9427655+OR+9427656%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110127,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107607,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 108348,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 108894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 297732,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 332469,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 1284752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110127,
        "cited_id": 2620876,
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
    "date_created": "2026-07-05T13:21:37Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:21:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:21:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:24:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:21:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Michigan v. DeFillippo

```
<div>
<center><b><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">443 U.S. 31</a></span> (1979)</b></center>
<center><h1>MICHIGAN<br>
v.<br>
DEFILLIPPO.</h1></center>
<center>No. 77-1680.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 21, 1979.</center>
<center>Decided June 25, 1979.</center>
CERTIORARI TO THE COURT OF APPEALS OF MICHIGAN.
<p><span class="star-pagination">*32</span> <i>Timothy A. Baughman</i> argued the cause for petitioner. with him on the briefs was <i>William L. Cahalan.</i></p>
<p><i>James C. Howarth,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./439/976/">439 U. S. 976</a></span>, argued the cause and filed a brief for respondent.<sup>[*]</sup></p>
<p><span class="star-pagination">*33</span> MR. CHIEF JUSTICE BURGER delivered the opinion of the Court.</p>
<p>The question presented by this case is whether an arrest made in good-faith reliance on an ordinance, which at the time had not been declared unconstitutional, is valid regardless of a subsequent judicial determination of its unconstitutionality.</p>
<p></p>
<h2>I</h2>
<p>At approximately 10 p. m. on September 14, 1976, Detroit police officers on duty in a patrol car received a radio call to investigate two persons reportedly appearing to be intoxicated in an alley. When they arrived at the alley, they found respondent and a young woman. The woman was in the process of lowering her slacks. One of the officers asked what they were doing, and the woman replied that she was about to relieve herself. The officer then asked respondent for identification; respondent asserted that he was Sergeant Mash, of the Detroit Police Department; he also purported to give his badge number, but the officer was unable to hear it. When respondent again was asked for identification, he changed his answer and said either that he worked for or that he knew Sergeant Mash. Respondent did not appear to be intoxicated.</p>
<p>Section 39-1-52.3 of the Code of the City of Detroit provides that a police officer may stop and question an individual if he has reasonable cause to believe that the individual's behavior warrants further investigation for criminal activity. In 1976 the Detroit Common Council amended § 39-1-52.3 to provide that it should be unlawful for any person stopped pursuant thereto to refuse to identify himself and produce evidence of his identity.<sup>[1]</sup></p>
<p><span class="star-pagination">*34</span> When he failed to identify himself, respondent was taken into custody for violation of § 39-1-52.3;<sup>[2]</sup> he was searched by one of the officers who found a package of marihuana in one of respondent's shirt pockets, and a tinfoil packet secreted inside a cigarette package in the other. The tinfoil packet subsequently was opened at the station; an analysis established that it contained phencyclidine, another controlled substance.</p>
<p>Respondent was charged with possession of the controlled substance phencyclidine. At the preliminary examination, he moved to suppress the evidence obtained in the search following the arrest; the trial court denied the motion. The Michigan Court of Appeals allowed an interlocutory appeal and reversed. It held that the Detroit ordinance, § 39-1-52.3, was unconstitutionally vague and concluded that since respondent had been arrested pursuant to that ordinance, both the arrest and the search were invalid.</p>
<p>The court expressly rejected the contention that an arrest made in good-faith reliance on a presumptively valid ordinance is valid regardless of whether the ordinance subsequently is declared unconstitutional. Accordingly, the Michigan Court of Appeals remanded with instructions to suppress the evidence <span class="star-pagination">*35</span> and quash the information. <span class="citation" data-id="1284752"><a href="/opinion/1284752/people-v-defillippo/" aria-description="Citation for case: People v. DeFillippo">80 Mich. App. 197</a></span>, <span class="citation" data-id="1284752"><a href="/opinion/1284752/people-v-defillippo/" aria-description="Citation for case: People v. DeFillippo">262 N. W. 2d 921</a></span> (1977).</p>
<p>The Michigan Supreme Court denied leave to appeal. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./439/816/">439 U. S. 816</a></span> (1978), to review the Michigan court's holding that evidence should be suppressed on federal constitutional grounds, although it was obtained as a result of an arrest pursuant to a presumptively valid ordinance. That holding was contrary to the holdings of the United States Court of Appeals for the Fifth Circuit that such arrests are valid. See <i>United States</i> v. <i>Carden,</i> <span class="citation" data-id="332469"><a href="/opinion/332469/united-states-v-roy-eugene-carden-winfred-eugene-carden-and-robert-lee/" aria-description="Citation for case: United States v. Roy Eugene Carden, Winfred Eugene...">529 F. 2d 443</a></span> (1976); <i>United States</i> v. <i>Kilgen,</i> <span class="citation" data-id="297732"><a href="/opinion/297732/united-states-v-robert-h-kilgen-jr/" aria-description="Citation for case: United States v. Robert H. Kilgen, Jr.">445 F. 2d 287</a></span> (1971).</p>
<p></p>
<h2>II</h2>
<p>Respondent was not charged with or tried for violation of the Detroit ordinance. The State contends that because of the violation of the ordinance, <i>i. e.,</i> refusal to identify himself, which respondent committed in the presence of the officers, respondent was subject to a valid arrest. The search that followed being incidental to that arrest, the State argues that it was equally valid and the drugs found should not have been suppressed. Respondent contends that since the ordinance which he was arrested for violating has been found unconstitutionally vague on its face, the arrest and search were invalid as violative of his rights under the Fourth and Fourteenth Amendments. Accordingly, he contends the drugs found in the search were correctly suppressed.</p>
<p>Under the Fourth and Fourteenth Amendments, an arresting officer may, without a warrant, search a person validly arrested. <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973); <i>Gustafson</i> v. <i>Florida,</i> <span class="citation" data-id="9425477"><a href="/opinion/108894/gustafson-v-florida/" aria-description="Citation for case: Gustafson v. Florida">414 U. S. 260</a></span> (1973). The constitutionality of a search incident to an arrest does not depend on whether there is any indication that the person arrested possesses weapons or evidence. The fact of a lawful arrest, standing alone, authorizes a search. <i>United States</i> v. <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#235" aria-description="Citation for case: United States v. Robinson"><i>Robinson, supra,</i> at 235</a></span>. Here the officer effected the arrest of respondent <span class="star-pagination">*36</span> for his refusal to identify himself; contraband drugs were found as a result of the search of respondent's person incidental to that arrest. If the arrest was valid when made, the search was valid and the illegal drugs are admissible in evidence.</p>
<p>Whether an officer is authorized to make an arrest ordinarily depends, in the first instance, on state law. <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#37" aria-description="Citation for case: Ker v. California">374 U. S. 23, 37</a></span> (1963); <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#15" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 15</a></span>, and n. 5 (1948). Respondent does not contend, however, that the arrest was not authorized by Michigan law. See <span class="citation no-link">Mich. Comp. Laws § 764.15</span> (1970). His sole contention is that since the arrest was for allegedly violating a Detroit ordinance later held unconstitutional, the search was likewise invalid.</p>
<p></p>
<h2>III</h2>
<p>It is not disputed that the Constitution permits an officer to arrest a suspect without a warrant if there is probable cause to believe that the suspect has committed or is committing an offense. <i>Adams</i> v. <i>Williams,</i> <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#148" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 148-149</a></span> (1972); <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#91" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 91</a></span> (1964). The validity of the arrest does not depend on whether the suspect actually committed a crime; the mere fact that the suspect is later acquitted of the offense for which he is arrested is irrelevant to the validity of the arrest. We have made clear that the kinds and degree of proof and the procedural requirements necessary for a conviction are not prerequisites to a valid arrest. See <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#119" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 119-123</a></span> (1975); <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#174" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 174-176</a></span> (1949).</p>
<p>When the officer arrested respondent, he had abundant probable cause to believe that respondent's conduct violated the terms of the ordinance. The ordinance provides that a person commits an offense if (a) an officer has reasonable cause to believe that given behavior warrants further investigation, (b) the officer stops him, and (c) the suspect refuses to identify himself. The offense is then complete.</p>
<p><span class="star-pagination">*37</span> Respondent's presence with a woman, in the circumstances described, in an alley at 10 p. m. was clearly, in the words of the ordinance, "behavior. . . warrant[ing] further investigation." Respondent's inconsistent and evasive responses to the officer's request that he identify himself, stating first that he was Sergeant Mash of the Detroit Police Department and then that he worked for or knew Sergeant Mash, constituted a refusal by respondent to identify himself as the ordinance required. Assuming, <i>arguendo,</i> that a person may not constitutionally be required to answer questions put by an officer in some circumstances, the false identification violated the plain language of the Detroit ordinance.</p>
<p>The remaining question, then, is whether, in these circumstances, it can be said that the officer lacked probable cause to believe that the conduct he observed and the words spoken constituted a violation of law simply because he should have known the ordinance was invalid and would be judicially declared unconstitutional. The answer is clearly negative.</p>
<p>This Court repeatedly has explained that "probable cause" to justify an arrest means facts and circumstances within the officer's knowledge that are sufficient to warrant a prudent person, or one of reasonable caution, in believing, in the circumstances shown, that the suspect has committed, is committing, or is about to commit an offense. See <i>Gerstein</i> v. <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#111" aria-description="Citation for case: Gerstein v. Pugh"><i>Pugh, supra,</i> at 111</a></span>; <i>Adams</i> v. <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#148" aria-description="Citation for case: Adams v. Williams"><i>Williams, supra,</i> at 148</a></span>; <i>Beck</i> v. <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#91" aria-description="Citation for case: Beck v. Ohio"><i>Ohio, supra,</i> at 91</a></span>; <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#313" aria-description="Citation for case: Draper v. United States">358 U. S. 307, 313</a></span> (1959); <i>Brinegar</i> v. <i>United States, supra,</i> at 175-176; <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#162" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 162</a></span> (1925).</p>
<p>On this record there was abundant probable cause to satisfy the constitutional prerequisite for an arrest. At that time, of course, there was no controlling precedent that this ordinance was or was not constitutional, and hence the conduct observed violated a presumptively valid ordinance. A prudent officer, in the course of determining whether respondent had committed an offense under all the circumstances shown <span class="star-pagination">*38</span> by this record, should not have been required to anticipate that a court would later hold the ordinance unconstitutional.</p>
<p>Police are charged to enforce laws until and unless they are declared unconstitutional. The enactment of a law forecloses speculation by enforcement officers concerning its constitutionality with the possible exception of a law so grossly and flagrantly unconstitutional that any person of reasonable prudence would be bound to see its flaws. Society would be ill-served if its police officers took it upon themselves to determine which laws are and which are not constitutionally entitled to enforcement.</p>
<p>In <i>Pierson</i> v. <i>Ray,</i> <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547</a></span> (1967), persons who had been arrested for violating a statute later declared unconstitutional by this Court sought damages for false arrest under state law and for violation of the Fourteenth Amendment under <span class="citation no-link">42 U. S. C. § 1983</span>. Mr. Chief Justice Warren speaking for the Court, in holding that police action based on a presumptively valid law was subject to a valid defense of good faith, observed: "A policeman's lot is not so unhappy that he must choose between being charged with dereliction of duty if he does not arrest when he has probable cause, and being mulcted in damages if he does." <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#555" aria-description="Citation for case: Pierson v. Ray">386 U. S., at 555</a></span>. The Court held that "the defense of good faith and probable cause, which the Court of Appeals found available to the officers in the common-law action for false arrest and imprisonment, is also available to them in the action under § 1983." <i>Id.,</i> at 557. Here, the police were not required to risk "being charged with dereliction of duty if [they did] not arrest when [they had] probable cause" on the basis of the conduct observed.<sup>[3]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*39</span> IV</h2>
<p>We have held that the exclusionary rule required suppression of evidence obtained in searches carried out pursuant to statutes, not previously declared unconstitutional, which purported to authorize the searches in question without probable cause and without a valid warrant. See, <i>e. g., </i><i>Torres</i> v. <i>Puerto Rico,</i> <span class="citation" data-id="9795098"><a href="/opinion/2620876/torres-v-puerto-rico/" aria-description="Citation for case: Torres v. Puerto Rico">442 U. S. 465</a></span> (1979); <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973); <i>Sibron</i> v. <i>New York,</i> <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span> (1968); <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967). Our holding today is not inconsistent with these decisions; the statutes involved in those cases bore a different relationship to the challenged searches than did the Detroit ordinance to respondent's arrest and search.</p>
<p>Those decisions involved statutes which, by their own terms, authorized searches under circumstances which did not satisfy the traditional warrant and probable-cause requirements of the Fourth Amendment. For example, in <i>Almeida-Sanchez</i> v. <i>United States, supra</i><i>,</i> we held invalid a search pursuant to a federal statute which authorized the Border Patrol to search any vehicle within a "reasonable distance" of the border, without a warrant or probable cause. The Attorney General, by regulation, fixed 100 miles as a "reasonable distance" from the border. <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#268" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S., at 268</a></span>. We held a search so distant from the point of entry was unreasonable under the Constitution. In <i>Berger</i> v. <i>New York</i> we struck down a statute authorizing searches under warrants which did not "particularly describ[e] the place to be searched, and the persons or things to be seized," as required by the Fourth and Fourteenth Amendments. <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#55" aria-description="Citation for case: Berger v. New York">388 U. S., at 55-56</a></span>.</p>
<p>In contrast, the ordinance here declared it a misdemeanor for one stopped for "investigation" to "refuse to identify himself"; it did not directly authorize the arrest or search.<sup>[4]</sup> Once <span class="star-pagination">*40</span> respondent refused to identify himself as the presumptively valid ordinance required, the officer had probable cause to believe respondent was committing an offense in his presence, and Michigan's general arrest statute, <span class="citation no-link">Mich. Comp. Laws § 764.15</span> (1970), authorized the arrest of respondent, independent of the ordinance. The search which followed was valid because it was incidental to that arrest. The ordinance is relevant to the validity of the arrest and search only as it pertains to the "facts and circumstances" we hold constituted probable cause for arrest.</p>
<p>The subsequently determined invalidity of the Detroit ordinance on vagueness grounds does not undermine the validity of the arrest made for violation of that ordinance, and the evidence discovered in the search of respondent should not have been suppressed. Accordingly, the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>Reversed and remanded.</i></p>
<p>MR. JUSTICE BLACKMUN, concurring.</p>
<p>I join the Court's opinion, but add a few words about the concern so evident in MR. JUSTICE BRENNAN'S dissenting opinion that today's decision will allow States and municipalities to circumvent the probable-cause requirement of the Fourth Amendment. There is some danger, I acknowledge, that the police will use a stop-and-identify ordinance to arrest persons for improper identification; that they will then conduct a search pursuant to the arrest; that if they discover contraband or other evidence of crime, the arrestee will be charged with some other offense; and that if they do not discover contraband or other evidence of crime, the arrestee will be released. In this manner, if the arrest for violation of the stop-and-identify <span class="star-pagination">*41</span> ordinance is not open to challenge, the ordinance itself could perpetually evade constitutional review.</p>
<p>There is no evidence in this case, however, that the Detroit ordinance is being used in such a pretextual manner. See Tr. of Oral Arg. 8. If a defendant in a proper case showed that the police habitually arrest, but do not prosecute, under a stop-and-identify ordinance, then I think this would suffice to rebut any claim that the police were acting in reasonable, good-faith reliance on the constitutionality of the ordinance. The arrestee could then challenge the validity of the ordinance, and, if the court concluded it was unconstitutional, could have the evidence obtained in the search incident to the arrest suppressed.</p>
<p>MR. JUSTICE BRENNAN, with whom MR. JUSTICE MARSHALL and MR. JUSTICE STEVENS join, dissenting.</p>
<p>I disagree with the Court's conclusion that the Detroit police had constitutional authority to arrest and search respondent because respondent refused to identify himself in violation of the Detroit ordinance. In my view, the police conduct, whether or not authorized by state law, exceeded the bounds set by the Constitution and violated respondent's Fourth Amendment rights.</p>
<p>At the time of respondent's arrest, Detroit City Code § 39-1-52.3 (1976) read as follows:</p>
<blockquote>"When a police officer has reasonable cause to believe that the behavior of an individual warrants further investigation for criminal activity, the officer may stop and question such person. It shall be unlawful for any person stopped pursuant to this section to refuse to identify himself, and to produce verifiable documents or other evidence of such identification. In the event that such person is unable to provide reasonable evidence of his true identity, the police officer may transport him to the nearest precinct in order to ascertain his identity."</blockquote>
<p><span class="star-pagination">*42</span> Detroit police, acting purely on suspicion, stopped respondent Gary DeFillippo on the authority of this ordinance and demanded that he identify himself and furnish proof of his identity. When respondent rebuffed their inquiries the police arrested him for violation of the ordinance. Thereafter, police searched respondent and discovered drugs.</p>
<p>Respondent challenges the constitutionality of the ordinance and his arrest and search pursuant to it. The Court assumes the unconstitutionality of the ordinance but upholds respondent's arrest nonetheless. The Court reasons that the police had probable cause to believe that respondent's actions violated the ordinance, that the police could not have been expected to know that the ordinance was unconstitutional, and that the police actions were therefore reasonable.</p>
<p>The Court errs, in my view, in focusing on the good faith of the arresting officers and on whether they were entitled to rely upon the validity of the Detroit ordinance. For the dispute in this case is not between the arresting officers and respondent. Cf. <i>Pierson</i> v. <i>Ray,</i> <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547</a></span> (1967).<sup>[1]</sup> The dispute is between respondent and the State of Michigan. <span class="star-pagination">*43</span> The ultimate issue is whether the State gathered evidence against respondent through unconstitutional means. Since the State is responsible for the actions of its legislative bodies as well as for the actions of its police, the State can hardly defend against this charge of unconstitutional conduct by arguing that the constitutional defect was the product of legislative action and that the police were merely executing the laws in good faith. See <i>Torres</i> v. <i>Puerto Rico,</i> <span class="citation" data-id="9795098"><a href="/opinion/2620876/torres-v-puerto-rico/" aria-description="Citation for case: Torres v. Puerto Rico">442 U. S. 465</a></span> (1979); <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973); <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967). States "may not . . . authorize police conduct which trenches upon Fourth Amendment rights, regardless of the labels which it attaches to such conduct. The question in this Court upon review of a state-approved search or seizure `is not whether the search [or seizure] was authorized by state law. The question is rather whether the search [or seizure] was reasonable under the Fourth Amendment.'" <i>Sibron</i> v. <i>New York,</i> <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#61" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 61</a></span> (1968), quoting in part from <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 61</a></span> (1967).</p>
<p>If the Court's inquiry were so directed and had not asked whether the arresting officers faithfully applied state law, invalidation of respondent's arrest and search would have been inescapable. For the Court's assumption that the Detroit ordinance is unconstitutional is well founded; the ordinance is indeed unconstitutional and patently so. And if the reasons for that constitutional infirmity had only been explored, rather than simply assumed, it would have been obvious that the application of the ordinance to respondent by Detroit police in this case trenched upon respondent's Fourth Amendment rights and resulted in an unreasonable search and seizure.</p>
<p>The touchstone of the Fourth Amendment's protection of privacy interests and prohibition against unreasonable police searches and seizures is the requirement that such police intrusions be based upon probable cause"`the best compromise that has been found for accommodating [the] often <span class="star-pagination">*44</span> opposing interests' in `safeguard[ing] citizens from rash and unreasonable interferences with privacy' and in `seek[ing] to give fair leeway for enforcing the law in the community's protection.'" <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#208" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 208</a></span> (1979), quoting from <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span> (1949).</p>
<p>Because of this requirement and the constitutional policies underlying it, the authority of police to accost citizens on the basis of suspicion is "narrowly drawn," <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 27</a></span> (1968), and carefully circumscribed. See <i>Dunaway</i> v. <i>New York, supra</i><i>.</i> Police may not conduct searches when acting on less than probable cause. Even weapons frisks in these circumstances are permissible only if the police have reason to believe that they are dealing with an armed and dangerous individual. See <i>Terry</i> v. <i>Ohio, supra,</i> at 24. Furthermore, while a person may be briefly detained against his will on the basis of reasonable suspicion "while pertinent questions are directed to him . . . the person stopped is not obliged to answer, answers may not be compelled, and refusal to answer furnishes no basis for an arrest . . . ." <i>Terry</i> v. <i>Ohio, supra,</i> at 34 (WHITE, J., concurring). In the context of criminal investigation, the privacy interest in remaining silent simply cannot be overcome at the whim of any suspicious police officer.<sup>[2]</sup> "[W]hile the police have the right to request citizens to answer voluntarily questions concerning unsolved crimes they have no right to compel them to answer." <span class="star-pagination">*45</span> <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span>, 727 n. 6 (1969).</p>
<p>In sum then, individuals accosted by police on the basis merely of reasonable suspicion have a right not to be searched, a right to remain silent, and, as a corollary, a right not to be searched if they choose to remain silent.</p>
<p>It is plain that the Detroit ordinance and the police conduct that it purports to authorize abridge these rights and their concomitant limitations upon police authority. The ordinance authorizes police, acting on the basis of suspicion, to demand answers from suspects and authorizes arrest, search, and conviction for those who refuse to comply. The ordinance therefore commands that which the Constitution denies the State power to command and makes "a crime out of what under the Constitution cannot be a crime." <i>Coates</i> v. <i>Cincinnati,</i> <span class="citation" data-id="9424583"><a href="/opinion/108348/coates-v-city-of-cincinnati/#616" aria-description="Citation for case: Coates v. City of Cincinnati">402 U. S. 611, 616</a></span> (1971). Furthermore, the ordinance, by means of a transparent expedientmaking the constitutionally protected refusal to answer itself a substantive offensesanctions circumvention by the police of the Court's holding that refusal to answer police inquiries during a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop furnishes no basis for a full-scale search and seizure. Clearly, this is a sheer piece of legislative legerdemain not to be countenanced. See <i>Davis</i> v. <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#726" aria-description="Citation for case: Davis v. Mississippi"><i>Mississippi, supra,</i> at 726-727</a></span>; <i>Sibron</i> v. <i>New York, supra</i><i>.</i></p>
<p>The Court does not dispute this analysis. Rather, it assumes that respondent had a constitutional right to refuse to cooperate with the police inquiries, that the ordinance is unconstitutional, and that henceforward the ordinance shall be regarded as null and void. Yet, the Court holds that arrests and searches pursuant to the ordinance prior to its invalidation by the Michigan Court of Appeals are constitutionally valid. Given the Court's assumptions concerning the invalidity of the ordinance, its conclusion must rest on the tacit assumption that the defects requiring invalidation of the ordinance and of convictions entered pursuant to it do not also require the invalidation of arrests pursuant to the ordinance. But only a brief reflection upon the pervasiveness of the ordinance's <span class="star-pagination">*46</span> constitutional infirmities demonstrates the fallacy of that assumption.</p>
<p>A major constitutional defect of the ordinance is that it forces individuals accosted by police solely on the basis of suspicion to choose between forgoing their right to remain silent and forgoing their right not to be searched if they choose to remain silent. Clearly, a constitutional prohibition merely against prosecutions under the ordinance and not against arrests under the ordinance as well would not solve this dilemma. For the fact would remain that individuals who chose to remain silent would be forced to relinquish their right not to be searched (and indeed would risk conviction on the basis of any evidence seized from them), while those who chose not to be searched would be forced to forgo their constitutional right to remain silent. This Hobson's choice can be avoided only by invalidating such police intrusions whether or not authorized by ordinance and holding fast to the rule of <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> and its progeny: that police acting on less than probable cause may not search, compel answers, or search those who refuse to answer their questions.<sup>[3]</sup></p>
<p>The conduct of Detroit police in this case plainly violated Fourth Amendment limitations. The police commanded respondent to relinquish his constitutional right to remain silent and then arrested and searched him when he refused to do so. The Detroit ordinance does not validate that constitutionally impermissible conduct. Accordingly, I would affirm the judgment of the Michigan Court of Appeals invalidating respondent's arrest and suppressing its fruits.</p>
<h2>NOTES</h2>
<p>[*]  Briefs of <i>amici curiae</i> urging reversal were filed by <i>Frank Carrington, Wayne W. Schmidt, Glen R. Murphy, Thomas Hendrickson, James P. Costello,</i> and <i>Richard F. Mayer</i> for Americans for Effective Law Enforcement, Inc., et al.; and by <i>Evelle J. Younger,</i> Attorney General, <i>Jack R. Winkler,</i> Chief Assistant Attorney General, <i>Daniel J. Kremer,</i> Assistant Attorney General, and <i>Harley D. Mayfield</i> and <i>Karl Phaler,</i> Deputy Attorneys General, for the State of California.
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed by <i>Edward M. Wise</i> for the American Civil Liberties Union Fund of Michigan; and by <i>John J. Cleary</i> for California Attorneys for Criminal Justice et al.</p>
<p><i>Laurance S. Smith</i> filed a brief for the National Legal Aid and Defender Association as <i>amicus curiae.</i></p>
<p>[1]  As amended, Code of the City of Detroit § 39-1-52.3 provided:
</p>
<p>"When a police officer has reasonable cause to believe that the behavior of an individual warrants further investigation for criminal activity, the officer may stop and question such person. It shall be unlawful for any person stopped pursuant to this section to refuse to identify himself, and to produce verifiable documents or other evidence of such identification. In the event that such person is unable to provide reasonable evidence of his true identity, the police officer may transport him to the nearest precinct in order to ascertain his identity."</p>
<p>While holding the ordinance unconstitutional, the Michigan Court of Appeals construed the ordinance to make refusal to identify oneself a crime meriting arrest. <span class="citation" data-id="1284752"><a href="/opinion/1284752/people-v-defillippo/" aria-description="Citation for case: People v. DeFillippo">80 Mich. App. 197</a></span>, 201 n. 1, <span class="citation" data-id="1284752"><a href="/opinion/1284752/people-v-defillippo/" aria-description="Citation for case: People v. DeFillippo">262 N. W. 2d 921</a></span>, 923 n. 1 (1977).</p>
<p>The preamble to the amendment indicates that it was enacted in response to an emergency caused by a marked increase in crime, particularly street crime by gangs of juveniles.</p>
<p>[2]  The woman was arrested on a charge of disorderly conduct; she is not involved in this case.</p>
<p>[3]  The purpose of the exclusionary rule is to deter unlawful police action. No conceivable purpose of deterrence would be served by suppressing evidence which, at the time it was found on the person of the respondent, was the product of a lawful arrest and a lawful search. To deter police from enforcing a presumptively valid statute was never remotely in the contemplation of even the most zealous advocate of the exclusionary rule.</p>
<p>[4]  In terms of the ordinance, § 39-1-52.3 authorizes officers to detain an individual who is "unable to provide reasonable evidence of his true identity." However, the State disclaims reliance on this provision to authorize the arrest of a person who, like respondent, "refuse[s] to identify himself." Tr. of Oral Arg. 5.</p>
<p>[1]  The Court's reliance upon <i>Pierson</i> v. <i>Ray,</i> <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#555" aria-description="Citation for case: Pierson v. Ray">386 U. S., at 555</a></span>, exposes the fallacy of its constitutional analysis. The Court assumes that respondent had a constitutional right to refuse to answer the questions put to him by the police, see <i>ante,</i> at 37, but nonetheless, relying upon <i>Pierson</i> v. <i><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Ray</a></span></i><i>,</i> upholds respondent's arrest and search for exercising this constitutional right. But <i><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Pierson</a></span></i> involved an action for damages against individual police officers and held only that it would be unfair to penalize those officers for actions undertaken in a good-faith, though mistaken, interpretation of the Constitution. Since the officer who arrested respondent in this case is not being mulcted for damages or penalized in any way for his actions, <i><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Pierson</a></span></i> does not support the Court's position. Rather, since respondent is the one who is being penalized for the exercise of what he reasonably believed to be his constitutional rights, <i><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Pierson</a></span></i> counsels for invalidation of respondent's arrest and not for its validation. For if it is unfair to penalize a police officer for actions undertaken pursuant to a good-faith, though mistaken, interpretation of the Constitution, then surely it is unfair to penalize respondent for actions undertaken pursuant to a good-faith and <i>correct</i> interpretation of the Constitution.</p>
<p>[2]  In addition to the Fourth Amendment, see <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), the right to remain silent when detained by police on the basis of suspicion may find its source in the Fifth Amendment's privilege against self-incrimination see <i>Haynes</i> v. <i>United States,</i> <span class="citation" data-id="9423609"><a href="/opinion/107608/haynes-v-united-states/" aria-description="Citation for case: Haynes v. United States">390 U. S. 85</a></span> (1968); <i>Grosso</i> v. <i>United States,</i> <span class="citation" data-id="9423605"><a href="/opinion/107607/grosso-v-united-states/" aria-description="Citation for case: Grosso v. United States">390 U. S. 62</a></span> (1968); <i>Albertson</i> v. <i>SACB,</i> <span class="citation" data-id="9423096"><a href="/opinion/107110/albertson-v-subversive-activities-control-board/" aria-description="Citation for case: Albertson v. Subversive Activities Control Board">382 U. S. 70</a></span> (1965), or, more generally, in "the right to be let alonethe most comprehensive of rights and the right most valued by civilized men." <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#478" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 478</a></span> (1928) (Brandeis, J., dissenting). See also <i>Griswold</i> v. <i>Connecticut,</i> <span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/#494" aria-description="Citation for case: Griswold v. Connecticut">381 U. S. 479, 494</a></span> (1965) (Goldberg, J., concurring).</p>
<p>[3]  There is also the risk that if stop-and-identify ordinances cannot be challenged in collateral proceedings they may never be presented for judicial review. Jurisdictions so minded may avoid prosecuting under them and use them merely as investigative tools to gather evidence of other crimes through pretextual arrests and searches. The possibility of such evasion is yet another reason that demonstrates the constitutional error of the Court's approval of respondent's arrest.</p>

</div>
```

---
