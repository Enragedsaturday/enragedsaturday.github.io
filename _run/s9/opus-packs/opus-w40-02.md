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

## GROUP: content/cases/Tennessee v. Garner.md  (`case`, 5 assertions)

### content_page

```
---
title: "Tennessee v. Garner"
type: case
citation: "471 U.S. 1 (1985)"
parallel_cite: "105 S. Ct. 1694; 85 L. Ed. 2d 1; 53 U.S.L.W. 4410"
neutral_cite: 1985 U.S. LEXIS 195
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-03-27
docket: 83-1035
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-03-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Tennessee v. Garner
  varies_by_point: false
  scope_note: "Clarified (not limited) by Scott v. Harris: Garner is an application of Graham reasonableness, not a rigid on/off switch."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111397/tennessee-v-garner/"
  cluster_id: 111397
  opinion_id: 9429990
  identity_checked: true
homes:
  - page: "[[Use of Force]]"
    role: "Key — Anchor"
related: ["[[Graham v. Connor]]", "[[Scott v. Harris]]"]
aliases: []
tags: ["case", "fourth-amendment", "use-of-force", "deadly-force", "seizure"]
holding: "Deadly force against an apparently unarmed, non-dangerous fleeing suspect is an unreasonable seizure; deadly force needs PC to believe the suspect poses a significant threat of death or serious injury."
lake:
  record_id: Tennessee v. Garner
  status: verified
  projected_at: 2026-07-06
---

# Tennessee v. Garner

*471 U.S. 1 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Memphis officer Elton Hymon shot 15-year-old Edward Garner in the back of the head as Garner—an apparently unarmed suspect whom Hymon was "reasonably sure" was unarmed—climbed a fence to flee a nighttime house burglary. A Tennessee statute authorized deadly force against any fleeing felon. Garner's father sued under 42 U.S.C. § 1983.

## Issue
Whether the Fourth Amendment permits the use of deadly force to prevent the escape of an apparently unarmed, non-dangerous fleeing felon.

## Rule
Deadly force to seize a fleeing suspect is constitutionally constrained. "We conclude that such force may not be used unless it is necessary to prevent the escape and the officer has probable cause to believe that the suspect poses a significant threat of death or serious physical injury to the officer or others." — 471 U.S. at 3. ^pin-3

Thus "[a] police officer may not seize an unarmed, nondangerous suspect by shooting him dead." — *Id.* at 11. ^pin-11

But "[w]here the officer has probable cause to believe that the suspect poses a threat of serious physical harm, either to the officer or to others, it is not constitutionally unreasonable to prevent escape by using deadly force." — *Id.* ^pin-11a

## Application
Hymon shot Garner although he was reasonably sure Garner was unarmed and posed no immediate threat; a nighttime burglary alone did not make Garner dangerous. Seizing the unarmed, non-dangerous Garner by deadly force was therefore unreasonable, and the Tennessee statute was unconstitutional insofar as it authorized deadly force against such fleeing suspects.

## Conclusion
The use of deadly force against the unarmed, non-dangerous Garner was an unreasonable seizure; the statute was unconstitutional as applied, and the case was [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- [[Scott v. Harris]] later clarified that *Garner* "did not establish a magical on/off switch" but is an application of the [[Graham v. Connor]] objective-reasonableness standard. This is a clarification, not negative treatment; *Garner* remains binding.

## Appears on
- [[Use of Force]] — *Key — Anchor*

## Sources
- *Tennessee v. Garner*, 471 U.S. 1 (1985) — https://www.courtlistener.com/opinion/111397/tennessee-v-garner/ — pinpoints: 3, 11.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "46261df298eb5101", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "471 U.S. 1 (1985)", "court": "U.S. Supreme Court", "neutral_cite": "1985 U.S. LEXIS 195", "official_citation_present": true, "parallel_cite": "105 S. Ct. 1694; 85 L. Ed. 2d 1; 53 U.S.L.W. 4410", "title": "Tennessee v. Garner", "year": "1985"}}
{"assertion_id": "12e8df496382abce", "dimension": "support", "kind": "home_role", "locator": {"home": "Use of Force"}, "payload": {"home": "Use of Force", "role": "Key — Anchor", "title": "Tennessee v. Garner"}}
{"assertion_id": "91e507baa774bdd5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Deadly force against an apparently unarmed, non-dangerous fleeing suspect is an unreasonable seizure; deadly force needs PC to believe the suspect poses a significant threat of death or serious injury.", "title": "Tennessee v. Garner"}}
{"assertion_id": "a1ee9b98c182ecc8", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Tennessee v. Garner"}}
{"assertion_id": "e08df167ed75476a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1985-03-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Tennessee v. Garner", "field_i_validity": "good_law", "scope_note": "Clarified (not limited) by Scott v. Harris: Garner is an application of Graham reasonableness, not a rigid on/off switch.", "title": "Tennessee v. Garner", "varies_by_point": "false"}}
```

### lake record — Tennessee v. Garner

```json
{
  "schema_version": "s2.v1",
  "record_id": "Tennessee v. Garner",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Tennessee v. Garner",
    "case_name_short": "Garner",
    "case_name_full": "TENNESSEE v. GARNER Et Al.",
    "input_case_name": "Tennessee v. Garner",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-03-27",
    "year": 1985,
    "docket": "83-1035",
    "cluster_id": 111397,
    "lead_opinion_id": 9429990,
    "sibling_ids": [
      111397,
      9429990,
      9429991
    ],
    "absolute_url": "/opinion/111397/tennessee-v-garner/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "471 U.S. 1",
      "volume": "471",
      "reporter": "U.S.",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 1694",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 L. Ed. 2d 1",
        "volume": "85",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4410",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4410",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 195",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "195",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "471 U.S. 1",
        "volume": "471",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 1694",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 L. Ed. 2d 1",
        "volume": "85",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 195",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "195",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4410",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4410",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "471 U.S. 1",
    "official_selection": {
      "court_class": "scotus",
      "selected": "471 U.S. 1",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-3",
      "page": null,
      "quote": "was unarmed\u2014climbed a fence to flee a nighttime house burglary. A Tennessee statute authorized deadly force against any fleeing felon. Garner's father sued under 42 U.S.C. \u00a7 1983. ## Issue Whether the Fourth Amendment permits the use of deadly force to prevent the escape of an apparently unarmed, non-dangerous fleeing felon. ## Rule Deadly force to seize a fleeing suspect is constitutionally constrained.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-11",
      "page": null,
      "quote": "[a] police officer may not seize an unarmed, nondangerous suspect by shooting him dead.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-11a",
      "page": null,
      "quote": "[w]here the officer has probable cause to believe that the suspect poses a threat of serious physical harm, either to the officer or to others, it is not constitutionally unreasonable to prevent escape by using deadly force.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-03-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Tennessee v. Garner",
    "varies_by_point": false,
    "scope_note": "Clarified (not limited) by Scott v. Harris: Garner is an application of Graham reasonableness, not a rigid on/off switch.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Krystal Wagner, Individually and as Administrator of the Estate of Shane Jensen v. State of Iowa and William L. Spece a/k/a Bill L. Spece",
          "cluster_id": 4844322,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Booker",
          "cluster_id": 137739,
          "cite": [
            "160 L. Ed. 2d 621",
            "125 S. Ct. 738",
            "543 U.S. 220",
            "2005 U.S. LEXIS 628"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. Harris",
          "cluster_id": 145738,
          "cite": [
            "167 L. Ed. 2d 686",
            "127 S. Ct. 1769",
            "550 U.S. 372",
            "2007 U.S. LEXIS 4748"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kentucky v. Graham",
          "cluster_id": 111500,
          "cite": [
            "87 L. Ed. 2d 114",
            "105 S. Ct. 3099",
            "473 U.S. 159",
            "1985 U.S. LEXIS 86",
            "53 U.S.L.W. 4966"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Canton v. Harris",
          "cluster_id": 112209,
          "cite": [
            "103 L. Ed. 2d 412",
            "109 S. Ct. 1197",
            "489 U.S. 378",
            "1989 U.S. LEXIS 1200",
            "57 U.S.L.W. 4270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whren v. United States",
          "cluster_id": 118036,
          "cite": [
            "135 L. Ed. 2d 89",
            "116 S. Ct. 1769",
            "517 U.S. 806",
            "1996 U.S. LEXIS 3720"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Allen King v. Eric Taylor",
          "cluster_id": 808337,
          "cite": [
            "694 F.3d 650",
            "2012 WL 3968371",
            "2012 U.S. App. LEXIS 19109"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hamdi v. Rumsfeld",
          "cluster_id": 137001,
          "cite": [
            "159 L. Ed. 2d 578",
            "124 S. Ct. 2633",
            "542 U.S. 507",
            "2004 U.S. LEXIS 4761"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. United States",
          "cluster_id": 1732,
          "cite": [
            "176 L. Ed. 2d 1",
            "130 S. Ct. 1265",
            "559 U.S. 133",
            "2010 U.S. LEXIS 2201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Atwater v. City of Lago Vista",
          "cluster_id": 2620702,
          "cite": [
            "149 L. Ed. 2d 549",
            "121 S. Ct. 1536",
            "532 U.S. 318",
            "2001 U.S. LEXIS 3366",
            "2001 Daily Journal DAR 3953",
            "2001 Colo. J. C.A.R. 2069",
            "14 Fla. L. Weekly Fed. S 193",
            "69 U.S.L.W. 4262",
            "2001 Cal. Daily Op. Serv. 3203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "National Treasury Employees Union v. Von Raab",
          "cluster_id": 112220,
          "cite": [
            "103 L. Ed. 2d 685",
            "109 S. Ct. 1384",
            "489 U.S. 656",
            "1989 U.S. LEXIS 6033",
            "1989 CCH OSHD 28,589",
            "4 I.E.R. Cas. (BNA) 246",
            "57 U.S.L.W. 4338",
            "49 Empl. Prac. Dec. (CCH) 38,792"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gibson v. County of Washoe, Nevada",
          "cluster_id": 777732,
          "cite": [
            "290 F.3d 1175",
            "2002 Cal. Daily Op. Serv. 4392",
            "2002 Daily Journal DAR 5649",
            "2002 U.S. App. LEXIS 9604"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111397 OR 9429990 OR 9429991) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTk1Mzc2MDAwMDAwJnM9NDc2OTgyMSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111397+OR+9429990+OR+9429991%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111397 OR 9429990 OR 9429991)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NDMmcz03ODM4NjEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111397+OR+9429990+OR+9429991%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111397 OR 9429990 OR 9429991)",
        "reviewed": 128,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 128,
        "triage_read": 0,
        "triage_snippet_classified": 128
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111397 OR 9429990 OR 9429991)",
    "indexed_citing_opinions": 2005,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111397,
        "count": 1666,
        "count_source": "search"
      },
      {
        "opinion_id": 9429990,
        "count": 371,
        "count_source": "search"
      },
      {
        "opinion_id": 9429991,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4292,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/tennessee-v-garner.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MzcwNjYmcz0xMDYyNjgyNiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111397+OR+9429990+OR+9429991%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111397,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 109657,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 109731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110132,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110236,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110916,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 111000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 111250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 111380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 111382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 326345,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 332062,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 341835,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 342570,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 366970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 420737,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 1215610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 1572528,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 1800197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 1802731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 1868014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 2038641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 2045742,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 2130642,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 2151033,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 2169808,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 2215247,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 2380557,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 2609526,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 3662921,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 3895566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 4004205,
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
    "date_created": "2026-07-05T21:21:13Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:21:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:21:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:24:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:21:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Tennessee v. Garner

```
<opinion type="majority">
<author id="b73-5">Justice White</author>
<p id="Ad">delivered the opinion of the Court.</p>
<p id="b73-6">This case requires us to determine the constitutionality of the use of deadly force to prevent the escape of an apparently unarmed suspected felon. We conclude that such force may not be used unless it is necessary to prevent the escape and the officer has probable cause to believe that the suspect poses a significant threat of death or serious physical injury to the officer or others.</p>
<p id="b73-10">HH</p>
<p id="b73-7">At about 10:45 p. m. on October 3, 1974, Memphis Police Officers Elton Hymon and Leslie Wright were dispatched to answer a “prowler inside call.” Upon arriving at the scene they saw a woman standing on her porch and gesturing toward the adjacent house.<footnotemark>1</footnotemark> She told them she had heard glass breaking and that “they” or “someone” was breaking in next door. While Wright radioed the dispatcher to say that they were on the scene, Hymon went behind the house. He heard a door slam and saw someone run across the backyard. The fleeing suspect, who was appellee-respondent’s decedent, Edward Garner, stopped at a 6-feet-high chain link fence at the edge of the yard. With the aid of a flashlight, Hymon was able to see Garner’s face and hands. He saw no sign of a weapon, and, though not certain, was “reasonably sure” and “figured” that Garner was unarmed. App. 41, 56; Record 219. He thought Garner was 17 or 18 years old and <page-number citation-index="1" label="4">*4</page-number>about 5' 5" <em>or 5' </em>7" tall.<footnotemark>2</footnotemark> While Garner was crouched at the base of the fence, Hymon called out “police, halt” and took a few steps toward him. Garner then began to climb over the fence. Convinced that if Garner made it over the fence he would elude capture,<footnotemark>3</footnotemark> Hymon shot him. The bullet hit Garner in the back of the head. Garner was taken by ambulance to a hospital, where he died on the operating table. Ten dollars and a purse taken from the house were found on his body.<footnotemark>4</footnotemark></p>
<p id="b74-5">In using deadly force to prevent the escape, Hymon was acting under the authority of a Tennessee statute and pursuant to Police Department policy. The statute provides that “[i]f, after notice of the intention to arrest the defendant, he either flee or forcibly resist, the officer may use all the necessary means to effect the arrest.” <span class="citation no-link">Tenn. Code Ann. <page-number citation-index="1" label="5">*5</page-number>§40-7-108</span> (1982).<footnotemark>5</footnotemark> The Department policy was slightly more restrictive than the statute, but still allowed the use of deadly force in cases of burglary. App. 140-144. The incident was reviewed by the Memphis Police Firearm’s Review Board and presented to a grand jury. Neither took any action. <span class="citation no-link"><em>Id., </em>at 57</span>.</p>
<p id="b75-5">Garner’s father then brought this action in the Federal District Court for the Western District of Tennessee, seeking damages under <span class="citation no-link">42 U. S. C. § 1983</span> for asserted violations of Garner’s constitutional rights. The complaint alleged that the shooting violated the Fourth, Fifth, Sixth, Eighth, and Fourteenth Amendments of the United States Constitution. It named as defendants Officer Hymon, the Police Department, its Director, and the Mayor and city of Memphis. After a 3-day bench trial, the District Court entered judgment for all defendants. It dismissed the claims against the Mayor and the Director for lack of evidence. It then concluded that Hymon’s actions were authorized by the Tennessee statute, which in turn was constitutional. Hymon had employed the only reasonable and practicable means of preventing Garner’s escape. Garner had “recklessly and heedlessly attempted to vault over the fence to escape, thereby assuming the risk of being fired upon.” App. to Pet. for Cert. A10.</p>
<p id="b75-6">The Court of Appeals for the Sixth Circuit affirmed with regard to Hymon, finding that he had acted in good-faith reliance on the Tennessee statute and was therefore within the scope of his qualified immunity. <span class="citation multiple-matches"><a href="/c/F.%202d/600/52/">600 F. 2d 52</a></span> (1979). It remanded for reconsideration of the possible liability of the city, however, in light of <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span> (1978), which had come down after the District Court’s decision. The District Court was <page-number citation-index="1" label="6">*6</page-number>directed to consider whether a city enjoyed a qualified immunity, whether the use of deadly force and hollow point bullets in these circumstances was constitutional, and whether any unconstitutional municipal conduct flowed from a “policy or custom” as required for liability under <em>Monell. </em>600 F. 2d, at 54-55.</p>
<p id="b76-5">The District Court concluded that <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>did not affect its decision. While acknowledging some doubt as to the possible immunity of the city, it found that the statute, and Hymon’s actions, were constitutional. Given this conclusion, it declined to consider the “policy or custom” question. App. to Pet. for Cert. A37-A39.</p>
<p id="b76-6">The Court of Appeals reversed and remanded. <span class="citation" data-id="420737"><a href="/opinion/420737/cleamtee-garner-v-memphis-police-department/" aria-description="Citation for case: Cleamtee Garner v. Memphis Police Department">710 F. 2d 240</a></span> (1983). It reasoned that the killing of a fleeing suspect is a “seizure” under the Fourth Amendment,<footnotemark>6</footnotemark> and is therefore constitutional only if “reasonable.” The Tennessee statute failed as applied to this case because it did not adequately limit the use of deadly force by distinguishing between felonies of different magnitudes — “the facts, as found, did not justify the use of deadly force under the Fourth Amendment.” <span class="citation" data-id="420737"><a href="/opinion/420737/cleamtee-garner-v-memphis-police-department/#246" aria-description="Citation for case: Cleamtee Garner v. Memphis Police Department"><em>Id., </em>at 246</a></span>. Officers cannot resort to deadly force unless they “have probable cause ... to believe that the suspect [has committed a felony and] poses a threat to the safety of the officers or a danger to the community if left at large.” <em><span class="citation" data-id="420737"><a href="/opinion/420737/cleamtee-garner-v-memphis-police-department/" aria-description="Citation for case: Cleamtee Garner v. Memphis Police Department">Ibid.</a></span></em><footnotemark><em>7</em></footnotemark></p>
<p id="b77-4"><page-number citation-index="1" label="7">*7</page-number>The State of Tennessee, which had intervened to defend the statute, see <span class="citation no-link">28 U. S. C. § 2403</span>(b), appealed to this Court. The city filed a petition for certiorari. We noted probable jurisdiction in the appeal and granted the petition. <span class="citation multiple-matches"><a href="/c/U.%20S./465/1098/">465 U. S. 1098</a></span> (1984).</p>
<p id="b77-5">II</p>
<p id="b77-6">Whenever an officer restrains the freedom of a person to walk away, he has seized that person. <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975). While it is not always clear just when minimal police interference becomes a seizure, see <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544</a></span> (1980), there can be no question that apprehension by the use of deadly force is a seizure subject to the reasonableness requirement of the Fourth Amendment.</p>
<p id="b77-7">A</p>
<p id="b77-8">A police officer may arrest a person if he has probable cause to believe that person committed a crime. <em>E. g., United States </em>v. <em>Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976). Petitioners and appellant argue that if this requirement is satisfied the Fourth Amendment has nothing to say about <em>how </em>that seizure is made. This submission ignores the many cases in which this Court, by balancing the extent of the intrusion against the need for it, has examined the reasonableness of <page-number citation-index="1" label="8">*8</page-number>the manner in which a search or seizure is conducted. To determine the constitutionality of a seizure “[w]e must balance the nature and quality of the intrusion on the individual’s Fourth Amendment interests against the importance of the governmental interests alleged to justify the intrusion.” <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place">462 U. S. 696, 703</a></span> (1983); see <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979); <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#555" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 555</a></span> (1976). We have described “the balancing of competing interests” as “the key principle of the Fourth Amendment.” <em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#700" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 700, n. 12</a></span> (1981). See also <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#536" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 536-537</a></span> (1967). Because one of the factors is the extent of the intrusion, it is plain that reasonableness depends on not only when a seizure is made, but also how it is carried out. <em>United States </em>v. <em>Ortiz, </em><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#895" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891, 895</a></span> (1975); <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#28" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 28-29</a></span> (1968).</p>
<p id="b78-5">Applying these principles to particular facts, the Court has held that governmental interests did not support a lengthy detention of luggage, <em>United States </em>v. <em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place, supra,</a></span> </em>an airport seizure not “carefully tailored to its underlying justification,” <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 500</a></span> (1983) (plurality-opinion), surgery under general anesthesia to obtain evidence, <em>Winston </em>v. <em>Lee, </em><span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/" aria-description="Citation for case: Winston v. Lee">470 U. S. 753</a></span> (1985), or detention for fingerprinting without probable cause, <em>Davis </em>v. <em>Mississippi, </em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969); <em>Hayes </em>v. <em>Florida, </em><span class="citation" data-id="9429967"><a href="/opinion/111382/hayes-v-florida/" aria-description="Citation for case: Hayes v. Florida">470 U. S. 811</a></span> (1985). On the other hand, under the same approach it has upheld the taking of fingernail scrapings from a suspect, <em>Cupp </em>v. <em>Murphy, </em><span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291</a></span> (1973), an unannounced entry into a home to prevent the destruction of evidence, <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963), administrative housing inspections without probable cause to believe that a code violation will be found, <em>Camara </em>v. <em>Municipal <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Court, supra,</a></span> </em>and a blood test of a drunken-driving suspect, <em>Schmerber </em>v. <em>California, 384 </em>U. S. 757 (1966). In each of these cases, the question was whether <page-number citation-index="1" label="9">*9</page-number>the totality of the circumstances justified a particular sort of search or seizure.</p>
<p id="b79-5">B</p>
<p id="b79-6">The same balancing process applied in the cases cited above demonstrates that, notwithstanding probable cause to seize a suspect, an officer may not always do so by killing him. The intrusiveness of a seizure by means of deadly force is unmatched. The suspect’s fundamental interest in his own life need not be elaborated upon. The use of deadly force also frustrates the interest of the individual, and of society, in judicial determination of guilt and punishment. Against these interests are ranged governmental interests in effective law enforcement.<footnotemark>8</footnotemark> It is argued that overall violence will be reduced by encouraging the peaceful submission of suspects who know that they may be shot if they flee. Effectiveness in making arrests requires the resort to deadly <page-number citation-index="1" label="10">*10</page-number>force, or at least the meaningful threat thereof. “Being able to arrest such individuals is a condition precedent to the state’s entire system of law enforcement.” Brief for Petitioners 14.</p>
<p id="b80-5">Without in any way disparaging the importance of these goals, we are not convinced that the use of deadly force is a sufficiently productive means of accomplishing them to justify the killing of nonviolent suspects. Cf. <em>Delaware </em>v. <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#659" aria-description="Citation for case: Delaware v. Prouse"><em>Prouse, supra, </em>at 659</a></span>. The use of deadly force is a self-defeating way of apprehending a suspect and so setting the criminal justice mechanism in motion. If successful, it guarantees that that mechanism will not be set in motion. And while the meaningful threat of deadly force might be thought to lead to the arrest of more live suspects by discouraging escape attempts,<footnotemark>9</footnotemark> the presently available evidence does not support this thesis.<footnotemark>10</footnotemark> The fact is that a majority of police de<page-number citation-index="1" label="11">*11</page-number>partments in this country have forbidden the use of deadly force against nonviolent suspects. See <em>infra, </em>at 18-19. If those charged with the enforcement of the criminal law have abjured the use of deadly force in arresting nondangerous felons, there is a substantial basis for doubting that the use of such force is an essential attribute of the arrest power in all felony cases. See <em>Schumann </em>v. <em>McGinn, </em><span class="citation" data-id="9738314"><a href="/opinion/2215247/schumann-v-mcginn/#472" aria-description="Citation for case: Schumann v. McGinn">307 Minn. 446, 472</a></span>, <span class="citation" data-id="9738314"><a href="/opinion/2215247/schumann-v-mcginn/#540" aria-description="Citation for case: Schumann v. McGinn">240 N. W. 2d 525, 540</a></span> (1976) (Rogosheske, J., dissenting in part). Petitioners and appellant have not persuaded us that shooting nondangerous fleeing suspects is so vital as to outweigh the suspect’s interest in his own life.</p>
<p id="b81-5">The use of deadly force to prevent the escape of all felony suspects, whatever the circumstances, is constitutionally unreasonable. It is not better that all felony suspects die than that they escape. Where the suspect poses no immediate threat to the officer and no threat to others, the harm resulting from failing to apprehend him does not justify the use of deadly force to do so. It is no doubt unfortunate when a suspect who is in sight escapes, but the fact that the police arrive a little late or are a little slower afoot does not always justify killing the suspect. A police officer may not seize an unarmed, nondangerous suspect by shooting him dead. The Tennessee statute is unconstitutional insofar as it authorizes the use of deadly force against such fleeing suspects.</p>
<p id="b81-6">It is not, however, unconstitutional on its face. Where the officer has probable cause to believe that the suspect poses a threat of serious physical harm, either to the officer or to others, it is not constitutionally unreasonable to prevent escape by using deadly force. Thus, if the suspect threatens the officer with a weapon or there is probable cause to believe that he has committed a crime involving the infliction or threatened infliction of serious physical harm, deadly force may be used if necessary to prevent escape, and if, where <page-number citation-index="1" label="12">*12</page-number>feasible, some warning has been given. As applied in such circumstances, the Tennessee statute would pass constitutional muster.</p>
<p id="b82-5">Ill</p>
<p id="b82-6">A</p>
<p id="b82-7">It is insisted that the Fourth Amendment must be construed in light of the common-law rule, which allowed the use of whatever force was necessary to effect the arrest of a fleeing felon, though not a misdemeanant. As stated in Hale’s posthumously published Pleas of the Crown:</p>
<blockquote id="b82-8">“[I]f persons that are pursued by these officers for felony or the just suspicion thereof . . . shall not yield themselves to these officers, but shall either resist or fly before they are apprehended or being apprehended shall rescue themselves and resist or fly, so that they cannot be otherwise apprehended, and are upon necessity slain therein, because they cannot be otherwise taken, it is no felony.” 2 M. Hale, Historia Placitorum Coronae 85 (1736).</blockquote>
<p id="b82-9">See also 4 W. Blackstone, Commentaries *289. Most American jurisdictions also imposed a flat prohibition against the use of deadly force to stop a fleeing misdemeanant, coupled with a general privilege <em>to </em>use such force to stop a fleeing felon. <em>E. g., Holloway </em>v. <em>Moser, </em><span class="citation" data-id="3662921"><a href="/opinion/3916545/holloway-v-moser/" aria-description="Citation for case: Holloway v. . Moser">193 N. C. 185</a></span>, <span class="citation" data-id="3662921"><a href="/opinion/3916545/holloway-v-moser/" aria-description="Citation for case: Holloway v. . Moser">136 S. E. 375</a></span> (1927); <em>State </em>v. <em>Smith, </em><span class="citation" data-id="7111483"><a href="/opinion/7200219/state-v-smith/#535" aria-description="Citation for case: State v. Smith">127 Iowa 534, 535</a></span>, <span class="citation no-link">103 N. W. 944</span>, 945 (1905); <em>Reneau </em>v. <em>State, </em><span class="citation" data-id="8296393"><a href="/opinion/8328603/reneau-v-state/" aria-description="Citation for case: Reneau v. State">70 Tenn. 720</a></span> (1879); <em>Brooks </em>v. <em>Commonwealth, </em><span class="citation" data-id="6233531"><a href="/opinion/6364699/brooks-v-commonwealth/" aria-description="Citation for case: Brooks v. Commonwealth">61 Pa. 352</a></span> (1869); <em>Roberts </em>v. <em>State, </em><span class="citation" data-id="7998579"><a href="/opinion/8042047/roberts-v-state/" aria-description="Citation for case: Roberts v. State">14 Mo. 138</a></span> (1851); see generally R. Perkins &amp; R. Boyce, Criminal Law 1098-1102 (3d ed. 1982); Day, Shooting the Fleeing Felon: State of the Law, <span class="citation no-link">14 Crim. L. Bull. 285</span>, 286-287 (1978); Wilgus, Arrest Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 798</span>, 807-816 (1924). But see <em>Storey </em>v. <em>State, </em><span class="citation" data-id="6511386"><a href="/opinion/6634820/storey-v-state/" aria-description="Citation for case: Storey v. State">71 Ala. 329</a></span> (1882); <em>State </em>v. <em>Bryant, </em><span class="citation" data-id="3649744"><a href="/opinion/3903667/state-v-bryant/#328" aria-description="Citation for case: State v. . Bryant">65 N. C. 327, 328</a></span> (1871); <em>Caldwell </em>v. <em>State, </em><span class="citation" data-id="4892115"><a href="/opinion/5076532/caldwell-v-state/" aria-description="Citation for case: Caldwell v. State">41 Tex. 86</a></span> (1874).</p>
<p id="b83-4"><page-number citation-index="1" label="13">*13</page-number>The State and city argue that because this was the prevailing rule at the time of the adoption of the Fourth Amendment and for some time thereafter, and is still in force in some States, use of deadly force against a fleeing felon must be “reasonable.” It is true that this Court has often looked to the common law in evaluating the reasonableness, for Fourth Amendment purposes, of police activity. See, <em>e. g., United States </em>v. <em>Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#418" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 418-419</a></span> (1976); <em>Gerstein </em>v. <em>Pugh, </em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#111" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 111, 114</a></span> (1975); <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 149-153</a></span> (1925). On the other hand, it “has not simply frozen into constitutional law those law enforcement practices that existed at the time of the Fourth Amendment’s passage.” <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#591" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 591, n. 33</a></span> (1980). Because of sweeping change in the legal and technological context, reliance on the common-law rule in this case would be a mistaken literalism that ignores the purposes of a historical inquiry.</p>
<p id="b83-5">B</p>
<p id="b83-6">It has been pointed out many times that the common-law rule is best understood in light of the fact that it arose at a time when virtually all felonies were punishable by death.<footnotemark>11</footnotemark> “Though effected without the protections and formalities of an orderly trial and conviction, the killing of a resisting or <page-number citation-index="1" label="14">*14</page-number>fleeing felon resulted in no greater consequences than those authorized for punishment of the felony of which the individual was charged or suspected.” American Law Institute, Model Penal Code §3.07, Comment 3, p. 56 (Tentative Draft No. 8, 1958) (hereinafter Model Penal Code Comment). Courts have also justified the common-law rule by emphasizing the relative dangerousness of felons. See, <em>e. g., Schumann </em>v. <em>McGinn, </em><span class="citation" data-id="9738314"><a href="/opinion/2215247/schumann-v-mcginn/#458" aria-description="Citation for case: Schumann v. McGinn">307 Minn., at 458</a></span>, <span class="citation" data-id="9738314"><a href="/opinion/2215247/schumann-v-mcginn/#533" aria-description="Citation for case: Schumann v. McGinn">240 N. W. 2d, at 533</a></span>; <em>Holloway </em>v. <span class="citation" data-id="3662921"><a href="/opinion/3916545/holloway-v-moser/#187" aria-description="Citation for case: Holloway v. . Moser"><em>Moser, supra, </em>at 187</a></span>, <span class="citation" data-id="3662921"><a href="/opinion/3916545/holloway-v-moser/#376" aria-description="Citation for case: Holloway v. . Moser">136 S. E., at 376</a></span> (1927).</p>
<p id="b84-5">Neither of these justifications makes sense today. Almost all crimes formerly punishable by death no longer are or can be. See, <em>e. g., Enmund </em>v. <em>Florida, </em><span class="citation" data-id="9428940"><a href="/opinion/110795/enmund-v-florida/" aria-description="Citation for case: Enmund v. Florida">458 U. S. 782</a></span> (1982); <em>Coker </em>v. <em>Georgia, </em><span class="citation" data-id="9426971"><a href="/opinion/109731/coker-v-georgia/" aria-description="Citation for case: Coker v. Georgia">433 U. S. 584</a></span> (1977). And while in earlier times “the gulf between the felonies and the minor offences was broad and deep,” 2 Pollock &amp; Maitland 467, n. 3; <em>Carroll </em>v. <em>United States, supra, </em>at 158, today the distinction is minor and often arbitrary. Many crimes classified as misdemeanors, or nonexistent, at common law are now felonies. Wilgus, 22 Mich. L. Rev., at 572-573. These changes have undermined the concept, which was questionable to begin with, that use of deadly force against a fleeing felon is merely a speedier execution of someone who has already forfeited his life. They have also made the assumption that a “felon” is more dangerous than a misdemeanant untenable. Indeed, numerous misdemeanors involve conduct more dangerous than many felonies.<footnotemark>12</footnotemark></p>
<p id="b84-6">There is an additional reason why the common-law rule cannot be directly translated to the present day. The common-law rule developed at a time when weapons were rudimentary. Deadly force could be inflicted almost solely in a hand-to-hand struggle during which, necessarily, the safety <page-number citation-index="1" label="15">*15</page-number>of the arresting officer was at risk. Handguns were not carried by police officers until the latter half of the last century. L. Kennett &amp; J. Anderson, The Gun in America 150-151 (1975). Only then did it become possible to use deadly force from a distance as a means of apprehension. As a practical matter, the use of deadly force under the standard articulation of the common-law rule has an altogether different meaning — and harsher consequences — now than in past centuries. See Wechsler &amp; Michael, A Rationale for the Law of Homicide: I, <span class="citation no-link">37 Colum. L. Rev. 701</span>, 741 (1937).<footnotemark>13</footnotemark></p>
<p id="b85-5">One other aspect of the common-law rule bears emphasis. It forbids the use of deadly force to apprehend a misde-meanant, condemning such action as disproportionately severe. See <em>Holloway </em>v. <em>Moser, </em><span class="citation" data-id="3662921"><a href="/opinion/3916545/holloway-v-moser/#187" aria-description="Citation for case: Holloway v. . Moser">193 N. C., at 187</a></span>, <span class="citation" data-id="3662921"><a href="/opinion/3916545/holloway-v-moser/#376" aria-description="Citation for case: Holloway v. . Moser">136 S. E., at 376</a></span>; <em>State </em>v. <em>Smith, </em><span class="citation" data-id="7111483"><a href="/opinion/7200219/state-v-smith/#535" aria-description="Citation for case: State v. Smith">127 Iowa, at 535</a></span>, 103 N. W., at 945. See generally Annot., 83 A. L. R. 3d 238 (1978).</p>
<p id="b85-6">In short, though the common-law pedigree of Tennessee’s rule is pure on its face, changes in the legal and technological context mean the rule is distorted almost beyond recognition when literally applied.</p>
<p id="b85-7">C</p>
<p id="b85-8">In evaluating the reasonableness of police procedures under the Fourth Amendment, we have also looked to pre<page-number citation-index="1" label="16">*16</page-number>vailing rules in individual jurisdictions. See, <em>e. g., United States </em>v. <em>Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#421" aria-description="Citation for case: United States v. Watson">423 U. S., at 421-422</a></span>. The rules in the States are varied. See generally Comment, <span class="citation no-link">18 Ga. L. Rev. 137</span>, 140-144 (1983). Some 19 States have codified the common-law rule,<footnotemark>14</footnotemark> though in two of these the courts have significantly limited the statute.<footnotemark>15</footnotemark> Four States, though without a relevant statute, apparently retain the common-law rule.<footnotemark>16</footnotemark> Two States have adopted the Model Penal Code’s <page-number citation-index="1" label="17">*17</page-number>provision verbatim.<footnotemark>17</footnotemark> Eighteen others allow, in slightly varying language, the use of deadly force only if the suspect has committed a felony involving the use or threat of physical or deadly force, or is escaping with a deadly weapon, or is likely to endanger life or inflict serious physical injury if not arrested.<footnotemark>18</footnotemark> Louisiana and Vermont, though without statutes or case law on point, do forbid the use of deadly force to prevent any but violent felonies.<footnotemark>19</footnotemark> The remaining States either have no relevant statute or case law, or have positions that are unclear.<footnotemark>20</footnotemark></p>
<p id="b88-4"><page-number citation-index="1" label="18">*18</page-number>It cannot be said that there is a constant or overwhelming trend away from the common-law rule. In recent years, some States have reviewed their laws and expressly rejected abandonment of the common-law rule.<footnotemark>21</footnotemark> Nonetheless, the long-term movement has been away from the rule that deadly force may be used against any fleeing felon, and that remains the rule in less than half the States.</p>
<p id="b88-5">This trend is more evident and impressive when viewed in light of the policies adopted by the police departments themselves. Overwhelmingly, these are more restrictive than the common-law rule. C. Milton, J. Halleck, J. Lardner, &amp; G. Abrecht, Police Use of Deadly Force 45-46 (1977). The Federal Bureau of Investigation and the New York City Police Department, for example, both forbid the use of firearms except when necessary to prevent death or grievous bodily harm. <span class="citation no-link"><em>Id., </em>at 40-41</span>; App. 88. For accreditation by the Commission on Accreditation for Law Enforcement Agencies, a department must restrict the use of deadly force to situations where “the officer reasonably believes that the action is in defense of human life ... or in defense of any person in immediate danger of serious physical injury.” Commission on Accreditation for Law Enforcement Agencies, Inc., Standards for Law Enforcement Agencies 1-2 (1983) (italics deleted). A 1974 study reported that the police department regulations in a majority of the large cities of the United States allowed the firing of a weapon only when a <page-number citation-index="1" label="19">*19</page-number>felon presented a threat of death or serious bodily harm. Boston Police Department, Planning &amp; Research Division, The Use of Deadly Force by Boston Police Personnel (1974), cited in <em>Mattis </em>v. <em>Schnarr, </em><span class="citation" data-id="341835"><a href="/opinion/341835/robert-dean-mattis-md-v-richard-r-schnarr-and-robert-marek-v-john-c/#1016" aria-description="Citation for case: Robert Dean Mattis, M.D. v. Richard R. Schnarr and Robert...">547 F. 2d 1007, 1016, n. 19</a></span> (CA8 1976), vacated as moot <em>sub nom. Ashcroft </em>v. Mattis, <span class="citation" data-id="109657"><a href="/opinion/109657/ashcroft-v-mattis/" aria-description="Citation for case: Ashcroft v. Mattis">431 U. S. 171</a></span> (1977). Overall, only 7.5% of departmental and municipal policies explicitly permit the use of deadly force against any felon; 86.8% explicitly do not. K. Matulia, A Balance of Forces: A Report of the International Association of Chiefs of Police 161 (1982) (table). See also Record 1108-1368 (written policies of 44 departments). See generally W. Geller &amp; K. Karales, Split-Second Decisions 33-42 (1981); Brief for Police Foundation et al. as <em>Amici Curiae. </em>In light of the rules adopted by those who must actually administer them, the older and fading common-law view is a dubious indicium of the constitutionality of the Tennessee statute now before us.</p>
<p id="b89-5">D</p>
<p id="b89-6">Actual departmental policies are important for an additional reason. We would hesitate to declare a police practice of long standing “unreasonable” if doing so would severely hamper effective law enforcement. But the indications are to the contrary. There has been no suggestion that crime has worsened in any way in jurisdictions that have adopted, by legislation or departmental policy, rules similar to that announced today. <em>Amici </em>note that “[a]fter extensive research and consideration, [they] have concluded that laws permitting police officers to use deadly force to apprehend unarmed, non-violent fleeing felony suspects actually do not protect citizens or law enforcement officers, do not deter crime or alleviate problems caused by crime, and do not improve the crime-fighting ability of law enforcement agencies.” <em>Id., </em>at 11. The submission is that the obvious state interests in apprehension are not sufficiently served to warrant the use of lethal weapons against all fleeing felons. See <em>supra, </em>at 10-11, and n. 10.</p>
<p id="b90-4"><page-number citation-index="1" label="20">*20</page-number>Nor do we agree with petitioners and appellant that the rule we have adopted requires the police to make impossible, split-second evaluations of unknowable facts. See Brief for Petitioners 25; Brief for Appellant 11. We do not deny the practical difficulties of attempting to assess the suspect’s dangerousness. However, similarly difficult judgments must be made by the police in equally uncertain circumstances. See, <em>e. g., Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20, 27</a></span>. Nor is there any indication that in States that allow the use of deadly force only against dangerous suspects, see nn. 15, 17-19, <em>supra, </em>the standard has been difficult to apply or has led to a rash of litigation involving inappropriate second-guessing of police officers’ split-second decisions. Moreover, the highly technical felony/misdemeanor distinction is equally, if not more, difficult to apply in the field. An officer is in no position to know, for example, the precise value of property stolen, or whether the crime was a first or second offense. Finally, as noted above, this claim must be viewed with suspicion in light of the similar self-imposed limitations of so many police departments.</p>
<p id="b90-5">IV</p>
<p id="b90-6">The District Court concluded that Hymon was justified in shooting Garner because state law allows, and the Federal Constitution does not forbid, the use of deadly force to prevent the escape of a fleeing felony suspect if no alternative means of apprehension is available. See App. to Pet. for Cert. A9-A11, A38. This conclusion made a determination of Garner’s apparent dangerousness unnecessary. The court did find, however, that Garner appeared to be unarmed, though Hymon could not be certain that was the case. <em>Id., </em>at A4, A23. See also App. 41, 56; Record 219. Restated in Fourth Amendment terms, this means Hymon had no articu-lable basis to think Garner was armed.</p>
<p id="b90-7">In reversing, the Court of Appeals accepted the District Court’s factual conclusions and held that “the facts, as found, did not justify the use of deadly force.” <span class="citation" data-id="420737"><a href="/opinion/420737/cleamtee-garner-v-memphis-police-department/#246" aria-description="Citation for case: Cleamtee Garner v. Memphis Police Department">710 F. 2d, at 246</a></span>. <page-number citation-index="1" label="21">*21</page-number>We agree. Officer Hymon could not reasonably have believed that Garner — young, slight, and unarmed — posed any threat. Indeed, Hymon never attempted to justify his actions on any basis other than the need to prevent an escape. The District Court stated in passing that “[t]he facts of this case did not indicate to Officer Hymon that Garner was ‘non-danger ous.’ ” App. to Pet. for Cert. A34. This conclusion is not explained, and seems to be based solely on the fact that Garner had broken into a house at night. However, the fact that Garner was a suspected burglar could not, without regard to the other circumstances, automatically justify the use of deadly force. Hymon did not have probable cause to believe that Garner, whom he correctly believed to be unarmed, posed any physical danger to himself or others.</p>
<p id="b91-5">The dissent argues that the shooting was justified by the fact that Officer Hymon had probable cause to believe that Garner had committed a nighttime burglary. <em>Post, </em>at 29, 32. While we agree that burglary is a serious crime, we cannot agree that it is so dangerous as automatically to justify the use of deadly force. The FBI classifies burglary as a “property” rather than a “violent” crime. See Federal Bureau of Investigation, Uniform Crime Reports, Crime in the United States 1 (1984).<footnotemark>22</footnotemark> Although the armed burglar would present a different situation, the fact that an unarmed suspect has broken into a dwelling at night does not automatically mean he is physically dangerous. This case demonstrates as much. See also <em>Solem </em>v. <em>Helm, </em><span class="citation" data-id="9429310"><a href="/opinion/111000/solem-v-helm/#296" aria-description="Citation for case: Solem v. Helm">463 U. S. 277, 296-297</a></span>, and nn. 22-23 (1983). In fact, the available statistics demonstrate that burglaries only rarely involve physical violence. During the 10-year period from 1973-1982, only 3.8% of all burglaries involved violent crime. Bureau of Justice Statistics, House<page-number citation-index="1" label="22">*22</page-number>hold Burglary 4 (1985).<footnotemark>23</footnotemark> See also T. Reppetto, Residential Crime 17, 105 (1974); Conklin &amp; Bittner, Burglary in a Suburb, 11 Criminology 208, 214 (1973).</p>
<p id="b92-5">V</p>
<p id="b92-6">We wish to make clear what our holding means in the context of this case. The complaint has been dismissed as to all the individual defendants. The State is a party only by virtue of <span class="citation no-link">28 U. S. C. § 2403</span>(b) and is not subject to liability. The possible liability of the remaining defendants — the Police Department and the city of Memphis — hinges on <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span> (1978), and is left for remand. We hold that the statute is invalid insofar as it purported to give Hymon the authority to act as he did. As for the policy of the Police Department, the absence of any discussion of this issue by the courts below, and the uncertain state of the record, preclude any consideration of its validity.</p>
<p id="b92-7">The judgment of the Court of Appeals is affirmed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b92-8">
<em>So ordered.</em>
</p>
<footnote label="1">
<p id="b73-9"> The owner of the house testified that no lights were on in the house, but that a back door light was on. Record 160. Officer Hymon, though uncertain, stated in his deposition that there were lights on in the house. <em>Id., </em>at 209.</p>
</footnote>
<footnote label="2">
<p id="b74-6"> In fact, Garner, an eighth-grader, was 15. He was 5' 4" tall and weighed somewhere around 100 or 110 pounds. App. to Pet. for Cert. A5.</p>
</footnote>
<footnote label="3">
<p id="b74-7"> When asked at trial why he fired, Hymon stated:</p>
<blockquote id="b74-8">“Well, first of all it was apparent to me from the little bit that I knew about the area at the time that he was going to get away because, number 1, I couldn’t get to him. My partner then couldn’t find where he was because, you know, he was late coming around. He didn’t know where I was talking about. I couldn’t get to him because of the fence here, I couldn’t have jumped this fence and come up, consequently jumped this fence and caught him before he got away because he was already up on the fence, just one leap and he was already over the fence, and so there is no way that I could have caught him.” App. 52.</blockquote>
<p id="b74-9">He also stated that the area beyond the fence was dark, that he could not have gotten over the fence easily because he was carrying a lot of equipment and wearing heavy boots, and that Garner, being younger and more energetic, could have outrun him. <em>Id., </em>at 53-54.</p>
</footnote>
<footnote label="4">
<p id="b74-10"> Garner had rummaged through one room in the house, in which, in the words of the owner, “[a]ll the stuff was out on the floors, all the drawers was pulled out, and stuff was scattered all over.” <em>Id., </em>at 34. The owner testified that his valuables were untouched but that, in addition to the purse and the 10 dollars, one of his wife’s rings was missing. The ring was not recovered. <em>Id., </em>at 34-35.</p>
</footnote>
<footnote label="5">
<p id="b75-7"> Although the statute does not say so explicitly, Tennessee law forbids the use of deadly force in the arrest of a misdemeanant. See <em>Johnson </em>v. <em>State, </em><span class="citation" data-id="3895566"><a href="/opinion/4132874/johnson-v-state/" aria-description="Citation for case: Johnson v. State">173 Tenn. 134</a></span>, <span class="citation" data-id="3895566"><a href="/opinion/4132874/johnson-v-state/" aria-description="Citation for case: Johnson v. State">114 S. W. 2d 819</a></span> (1938).</p>
</footnote>
<footnote label="6">
<p id="b76-7"> “The right of the people to be secure in their persons . . . against unreasonable searches and seizures, shall not be violated . . . .” U. S. Const., Arndt. 4.</p>
</footnote>
<footnote label="7">
<p id="b76-8"> The Court of Appeals concluded that the rule set out in the Model Penal Code “accurately states Fourth Amendment limitations on the use of deadly force against fleeing felons.” <span class="citation" data-id="420737"><a href="/opinion/420737/cleamtee-garner-v-memphis-police-department/#247" aria-description="Citation for case: Cleamtee Garner v. Memphis Police Department">710 F. 2d, at 247</a></span>. The relevant portion of the Model Penal Code provides:</p>
<blockquote id="b76-9">“The use of deadly force is not justifiable . . . unless (i) the arrest is for a felony; and (ii) the person effecting the arrest is authorized to act as a peace officer or is assisting a person whom he believes to be authorized to act as a peace officer; and (iii) the actor believes that the force employed creates no substantial risk of injury to innocent persons; and (iv) the actor believes <page-number citation-index="1" label="7">*7</page-number>that (1) the crime for which the arrest is made involved conduct including the use or threatened use of deadly force; or (2) there is a substantial risk that the person to be arrested will cause death or serious bodily harm if his apprehension is delayed.” American Law Institute, Model Penal Code §3.07(2)(b) (Proposed Official Draft 1962).</blockquote>
<p id="b77-10">The court also found that “[a]n analysis of the facts of this case under the Due Process Clause” required the same result, because the statute was not narrowly drawn to further a compelling state interest. <span class="citation" data-id="420737"><a href="/opinion/420737/cleamtee-garner-v-memphis-police-department/#246" aria-description="Citation for case: Cleamtee Garner v. Memphis Police Department">710 F. 2d, at 246-247</a></span>. The court considered the generalized interest in effective law enforcement sufficiently compelling only when the the suspect is dangerous. Finally, the court held, relying on <em>Owen </em>v. <em>City of Independence, </em><span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/" aria-description="Citation for case: Owen v. City of Independence">445 U. S. 622</a></span> (1980), that the city was not immune.</p>
</footnote>
<footnote label="8">
<p id="b79-7"> The dissent emphasizes that subsequent investigation cannot replace immediate apprehension. We recognize that this is so, see n. 13, <em>infra; </em>indeed, that is the reason why there is any dispute. If subsequent arrest were assured, no one would argue that use of deadly force was justified. Thus, we proceed on the assumption that subsequent arrest is not likely. Nonetheless, it should be remembered that failure to apprehend at the scene does not necessarily mean that the suspect will never be caught.</p>
<p id="b79-8">In lamenting the inadequacy of later investigation, the dissent relies on the report of the President’s Commission on Law Enforcement and Administration of Justice. It is worth noting that, notwithstanding its awareness of this problem, the Commission itself proposed a policy for use of deadly force arguably even more stringent than the formulation we adopt today. See President’s Commission on Law Enforcement and Administration of Justice, Task Force Report: The Police 189 (1967). The Commission proposed that deadly force be used only to apprehend “perpetrators who, in the course of their crime threatened the use of deadly force, or if the officer believes there is a substantial risk that the person whose arrest is sought will cause death or serious bodily harm if his apprehension is delayed.” In addition, the officer would have “to know, as a virtual certainty, that the suspect committed an offense for which the use of deadly force is permissible.” <em><span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/" aria-description="Citation for case: Owen v. City of Independence">Ibid.</a></span></em></p>
</footnote>
<footnote label="9">
<p id="b80-6"> We note that the usual manner of deterring illegal conduct — through punishment — has been largely ignored in connection with flight from arrest. Arkansas, for example, specifically excepts flight from arrest from the offense of “obstruction of governmental operations.” The commentary notes that this “reflects the basic policy judgment that, absent the use of force or violence, a mere attempt to avoid apprehension by a law enforcement officer does not give rise to an independent offense.” Ark. Stat. Ann. § 41-2802(3)(a) (1977) and commentary. In the few States that do outlaw flight from an arresting officer, the crime is only a misdemeanor. See, <em>e. </em>g., <span class="citation no-link">Ind. Code § 35-44-3-3</span> (1982). Even forceful resistance, though generally a separate offense, is classified as a misdemeanor. <em>E. g., </em>Ill. Rev. Stat., ch. 38, ¶31-1 (1984); <span class="citation no-link">Mont. Code Ann. §45-7-301</span> (1984); N. H. Rev. Stat. Ann. §642:2 (Supp. 1983); Ore. Rev. Stat. §162.315 (1983).</p>
<p id="b80-7">This lenient approach does avoid the anomaly of automatically transforming every fleeing misdemeanant into a fleeing felon — subject, under the common-law rule, to apprehension by deadly force — solely by virtue of his flight. However, it is in real tension with the harsh consequences of flight in cases where deadly force is employed. For example, Tennessee does not outlaw fleeing from arrest. The Memphis City Code does, §22-34.1 (Supp. 17, 1971), subjecting the offender to a maximum fine of $50, § 1-8 (1967). Thus, Garner’s attempted escape subjected him to (a) a $50 fine, and (b) being shot.</p>
</footnote>
<footnote label="10">
<p id="b80-8"> See Sherman, Reducing Police Gun Use, in Control in the Police Organization 98, 120-123 (M. Punch ed. 1983); Fyfe, Observations on Police <page-number citation-index="1" label="11">*11</page-number>Deadly Force, 27 Crime &amp; Delinquency 376, 378-381 (1981); W. Geller &amp; K. Karales, Split-Second Decisions 67 (1981); App. 84 (affidavit of William Bracey, Chief of Patrol, New York City Police Department). See generally Brief for Police Foundation et al. as <em>Amici Curiae.</em></p>
</footnote>
<footnote label="11">
<p id="b83-7"> The roots of the concept of a “felony” lie not in capital punishment but in forfeiture. 2 F. Pollock &amp; F. Maitland, The History of English Law 465 (2d ed. 1909) (hereinafter Pollock &amp; Maitland). Not all felonies were always punishable by death. See <em>id., </em>at 466-467, n. 3. Nonetheless, the link was profound. Blackstone was able to write: “The idea of felony is indeed so generally connected with that of capital punishment, that we find it hard to separate them; and to this usage the interpretations of the law do now conform. And therefore if a statute makes any new offence felony, the law implies that is shall be punished with death, <em>viz. </em>by hanging, as well as with forfeiture . . . .” 4 W. Blackstone, Commentaries *98. See also R. Perkins &amp; R. Boyce, Criminal Law 14-15 (3d ed. 1982); 2 Pollock &amp; Maitland 511.</p>
</footnote>
<footnote label="12">
<p id="b84-7"> White-collar crime, for example, poses a less significant physical threat than, say, drunken driving. See <em>Welsh </em>v. <em>Wisconsin, </em><span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740</a></span> (1984); <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#755" aria-description="Citation for case: Welsh v. Wisconsin"><em>id., </em>at 755</a></span> (Blackmun, J., concurring). See Model Penal Code Comment, at 57.</p>
</footnote>
<footnote label="13">
<p id="b85-9"> It has been argued that sophisticated techniques of apprehension and increased communication between the police in different jurisdictions have made it more likely that an escapee will be caught than was once the case, and that this change has also reduced the “reasonableness” of the use of deadly force to prevent escape. <em>E. g., </em>Sherman, Execution Without Trial: Police Homicide and the Constitution, <span class="citation no-link">33 Vand. L. Rev. 71</span>, 76 (1980). We are unaware of any data that would permit sensible evaluation of this claim. Current arrest rates are sufficiently low, however, that we have some doubt whether in past centuries the failure to arrest at the scene meant that the police had missed their only chance in a way that is not presently the case. In 1983, 21% of the offenses in the Federal Bureau of Investigation crime index were cleared by arrest. Federal Bureau of Investigation, Uniform Crime Reports, Crime in the United States 159 (1984). The clearance rate for burglary was 15%. <em><span class="citation no-link">Ibid.</span></em></p>
</footnote>
<footnote label="14">
<p id="b86-5"> Ala. Code § 13A-3-27 (1982); Ark. Stat. Ann. § 41-510 (1977); Cal. Penal Code Ann. § 196 (West 1970); Conn. Gen. Stat. § 53a-22 (1972); <span class="citation no-link">Fla. Stat. § 776.05</span> (1983); <span class="citation no-link">Idaho Code § 19-610</span> (1979); <span class="citation no-link">Ind. Code § 35-41-3-3</span> (1982); <span class="citation no-link">Kan. Stat. Ann. § 21-3215</span> (1981); <span class="citation no-link">Miss. Code Ann. § 97-3-15</span>(d) (Supp. 1984); <span class="citation no-link">Mo. Rev. Stat. § 563.046</span> (1979); <span class="citation no-link">Nev. Rev. Stat. § 200.140</span> (1983); N. M. Stat. Ann. § 30-2-6 (1984); Okla. Stat., Tit. 21, §732 (1981); R. I. Gen. Laws § 12-7-9 (1981); S. D. Codified Laws §§ 22-16-32, 22-16-33 (1979); <em>Term. </em>Code Ann. § 40-7-108 (1982); Wash. Rev. Code § 9A. 16.040(3) (1977). Oregon limits use of deadly force to violent felons, but also allows its use against any felon if “necessary.” Ore. Rev. Stat. § 161.239 (1983). Wisconsin’s statute is ambiguous, but should probably be added to this list. <span class="citation no-link">Wis. Stat. § 939.45</span>(4) (1981-1982) (officer may use force necessary for “a reasonable accomplishment of a lawful arrest”). But see <em>Clark </em>v. <em>Ziedonis, </em><span class="citation" data-id="1802731"><a href="/opinion/1802731/clark-v-ziedonis/" aria-description="Citation for case: Clark v. Ziedonis">368 F. Supp. 544</a></span> (ED Wis. 1973), aff’d on other grounds, <span class="citation multiple-matches"><a href="/c/F.%202d/513/79/">513 F. 2d 79</a></span> (CA7 1975).</p>
</footnote>
<footnote label="15">
<p id="b86-6"> In California, the police may use deadly force to arrest only if the crime for which the arrest is sought was “a forcible and atrocious one which threatens death or serious bodily harm,” or there is a substantial risk that the person whose arrest is sought will cause death or serious bodily harm if apprehension is delayed. <em>Kortum </em>v. <em>Alkire, </em><span class="citation" data-id="2169808"><a href="/opinion/2169808/kortum-v-alkire/#333" aria-description="Citation for case: Kortum v. Alkire">69 Cal. App. 3d 325, 333</a></span>,<span class="citation" data-id="2169808"><a href="/opinion/2169808/kortum-v-alkire/#30" aria-description="Citation for case: Kortum v. Alkire">138 Cal. Rptr. 26, 30-31</a></span> (1977). See also <em>People </em>v. <em>Ceballos, </em><span class="citation" data-id="2609526"><a href="/opinion/2609526/people-v-ceballos/#476" aria-description="Citation for case: People v. Ceballos">12 Cal. 3d 470, 476-484</a></span>, <span class="citation" data-id="2609526"><a href="/opinion/2609526/people-v-ceballos/#245" aria-description="Citation for case: People v. Ceballos">526 P. 2d 241, 245-250</a></span> (1974); <em>Long Beach Police Officers Assn. </em>v. <em>Long Beach, </em><span class="citation" data-id="2130642"><a href="/opinion/2130642/long-beach-police-officers-assn-v-city-of-long-beach/#373" aria-description="Citation for case: Long Beach Police Officers Ass&#x27;n v. City of Long Beach">61 Cal. App. 3d 364, 373-374</a></span>, <span class="citation" data-id="2130642"><a href="/opinion/2130642/long-beach-police-officers-assn-v-city-of-long-beach/#353" aria-description="Citation for case: Long Beach Police Officers Ass&#x27;n v. City of Long Beach">132 Cal. Rptr. 348, 353-354</a></span> (1976). In Indiana, deadly force may be used only to prevent injury, the imminent danger of injury or force, or the threat of force. It is not permitted simply to prevent escape. <em>Rose </em>v. <em>State, </em><span class="citation" data-id="2038641"><a href="/opinion/2038641/rose-v-state/" aria-description="Citation for case: Rose v. State">431 N. E. 2d 521</a></span> (Ind. App. 1982).</p>
</footnote>
<footnote label="16">
<p id="b86-7"> These are Michigan, Ohio, Virginia, and West Virginia. <em>Werner </em>v. <em>Hartfelder, </em><span class="citation" data-id="9684994"><a href="/opinion/1800197/werner-v-hartfelder/" aria-description="Citation for case: Werner v. Hartfelder">113 Mich. App. 747</a></span>, <span class="citation" data-id="9684994"><a href="/opinion/1800197/werner-v-hartfelder/" aria-description="Citation for case: Werner v. Hartfelder">318 N. W. 2d 825</a></span> (1982); <em>State </em>v. <em>Foster, </em><span class="citation" data-id="9311644"><a href="/opinion/9316356/state-v-foster/#59" aria-description="Citation for case: State v. Foster">60 Ohio Misc. 46, 59-66</a></span>, <span class="citation" data-id="9311644"><a href="/opinion/9316356/state-v-foster/#255" aria-description="Citation for case: State v. Foster">396 N. E. 2d 246, 255-258</a></span> (Com. Pl. 1979) (citing cases); <em>Berry </em>v. <em>Hamman, </em><span class="citation" data-id="1215610"><a href="/opinion/1215610/berry-v-hamman/" aria-description="Citation for case: Berry v. Hamman">203 Va. 596</a></span>, <span class="citation" data-id="1215610"><a href="/opinion/1215610/berry-v-hamman/" aria-description="Citation for case: Berry v. Hamman">125 S. E. 2d 851</a></span> (1962); <em>Thompson </em>v. <em>Norfolk &amp; W. R. Co., </em><span class="citation" data-id="4004205"><a href="/opinion/4227643/thompson-v-norfolk-western-railway-co/#711" aria-description="Citation for case: Thompson v. Norfolk &amp; Western Railway Co.">116 W. Va. 705, 711-712</a></span>, <span class="citation" data-id="4004205"><a href="/opinion/4227643/thompson-v-norfolk-western-railway-co/#883" aria-description="Citation for case: Thompson v. Norfolk &amp; Western Railway Co.">182 S. E. 880, 883-884</a></span> (1935).</p>
</footnote>
<footnote label="17">
<p id="b87-5"> <span class="citation no-link">Haw. Rev. Stat. §703-307</span> (1976); <span class="citation no-link">Neb. Rev. Stat. §28-1412</span> (1979). Massachusetts probably belongs in this category. Though it once rejected distinctions between felonies, <em>Uraneck </em>v. <em>Lima, </em><span class="citation" data-id="6448649"><a href="/opinion/6574887/uraneck-v-lima/#750" aria-description="Citation for case: Uraneck v. Lima">359 Mass. 749, 750</a></span>, <span class="citation" data-id="6448649"><a href="/opinion/6574887/uraneck-v-lima/#671" aria-description="Citation for case: Uraneck v. Lima">269 N. E. 2d 670, 671</a></span> (1971), it has since adopted the Model Penal Code limitations with regard to private citizens, <em>Commonwealth </em>v. <em>Klein, </em><span class="citation" data-id="2045742"><a href="/opinion/2045742/commonwealth-v-klein/" aria-description="Citation for case: Commonwealth v. Klein">372 Mass. 823</a></span>, <span class="citation" data-id="2045742"><a href="/opinion/2045742/commonwealth-v-klein/" aria-description="Citation for case: Commonwealth v. Klein">363 N. E. 2d 1313</a></span> (1977), and seems to have extended that decision to police officers, <em>Julian </em>v. <em>Randazzo, </em><span class="citation" data-id="2151033"><a href="/opinion/2151033/julian-v-randazzo/" aria-description="Citation for case: Julian v. Randazzo">380 Mass. 391</a></span>, <span class="citation" data-id="2151033"><a href="/opinion/2151033/julian-v-randazzo/" aria-description="Citation for case: Julian v. Randazzo">403 N. E. 2d 931</a></span> (1980).</p>
</footnote>
<footnote label="18">
<p id="b87-6"> <span class="citation no-link">Alaska Stat. Ann. § 11.81.370</span>(a) (1983); <span class="citation no-link">Ariz. Rev. Stat. Ann. § 13-410</span> (1978); <span class="citation no-link">Colo. Rev. Stat. § 18-1-707</span> (1978); Del. Code Ann., Tit. 11, §467 (1979) (felony involving physical force <em>and </em>a substantial risk that the suspect will cause death or serious bodily injury <em>or </em>will never be recaptured); Ga. Code § 16-3-21(a) (1984); Ill. Rev. Stat., ch. 38, ¶7-5 (1984); <span class="citation no-link">Iowa Code § 804.8</span> (1983) (suspect has used or threatened deadly force in commission of a felony, or would use deadly force if not caught); Ky. Rev. Stat. § 503.090 (1984) (suspect committed felony involving use or threat of physical force likely to cause death or serious injury, <em>and </em>is likely to endanger life unless apprehended without delay); Me. Rev. Stat. Ann., Tit. 17-A, § 107 (1983) (commentary notes that deadly force may be used only “where the person to be arrested poses a threat to human life”); <span class="citation no-link">Minn. Stat. § 609.066</span> (1984); N. H. Rev. Stat. Ann. § 627:5(II) (Supp. 1983); N. J. Stat. Ann. § 2C-3-7 (West 1982); N. Y. Penal Law § 35.30 (McKinney Supp. 1984-1985); N. C. Gen. Stat. § 15A-401 (1983); N. D. Cent. Code § 12.1-05-07.2.d (1976); <span class="citation no-link">18 Pa. Cons. Stat. §508</span> (1982); <span class="citation no-link">Tex. Penal Code Ann. § 9.51</span>(c) (1974); <span class="citation no-link">Utah Code Ann. § 76-2-404</span> (1978).</p>
</footnote>
<footnote label="19">
<p id="b87-7"> See La. Rev. Stat. Ann. § 14:20(2) (West 1974); Vt. Stat. Ann., Tit. 13, § 2305 (1974 and Supp. 1984). A Federal District Court has interpreted the Louisiana statute to limit the use of deadly force against fleeing suspects to situations where “life itself is endangered or great bodily harm is threatened.” <em>Sauls </em>v. <em>Hutto, </em><span class="citation" data-id="1868014"><a href="/opinion/1868014/sauls-v-hutto/#132" aria-description="Citation for case: Sauls v. Hutto">304 F. Supp. 124, 132</a></span> (ED La. 1969).</p>
</footnote>
<footnote label="20">
<p id="b87-8"> These are Maryland, Montana, South Carolina, and Wyoming. A Maryland appellate court has indicated, however, that deadly force may not be used against a felon who “was in the process of fleeing and, at the <page-number citation-index="1" label="18">*18</page-number>time, presented no immediate danger to . . . anyone . . . <em>Giant Food, Inc. </em>v. <em>Scherry, </em><span class="citation" data-id="2380557"><a href="/opinion/2380557/giant-food-inc-v-scherry/#589" aria-description="Citation for case: Giant Food, Inc. v. Scherry">51 Md. App. 586, 589, 596</a></span>, <span class="citation" data-id="2380557"><a href="/opinion/2380557/giant-food-inc-v-scherry/#486" aria-description="Citation for case: Giant Food, Inc. v. Scherry">444 A. 2d 483, 486, 489</a></span> (1982).</p>
</footnote>
<footnote label="21">
<p id="b88-7"> In adopting its current statute in 1979, for example, Alabama expressly chose the common-law rule over more restrictive provisions. Ala. Code § 13A-3-27, Commentary, pp. 67-63 (1982). Missouri likewise considered but rejected a proposal akin to the Model Penal Code rule. See <em>Mattis </em>v. <em>Schnarr, </em><span class="citation" data-id="341835"><a href="/opinion/341835/robert-dean-mattis-md-v-richard-r-schnarr-and-robert-marek-v-john-c/#1022" aria-description="Citation for case: Robert Dean Mattis, M.D. v. Richard R. Schnarr and Robert...">547 F. 2d 1007, 1022</a></span> (CA8 1976) (Gibson, C. J., dissenting), vacated as moot <em>sub nom. Ashcroft </em>v. <em>Mattis, </em><span class="citation" data-id="109657"><a href="/opinion/109657/ashcroft-v-mattis/" aria-description="Citation for case: Ashcroft v. Mattis">431 U. S. 171</a></span> (1977). Idaho, whose current statute codifies the common-law rule, adopted the Model Penal Code in 1971, but abandoned it in 1972.</p>
</footnote>
<footnote label="22">
<p id="b91-6"> In a recent report, the Department of Corrections of the District of Columbia also noted that “there is nothing inherently dangerous or violent about the offense,” which is a crime against property. D. C. Department of Corrections, Prisoner Screening Project 2 (1985).</p>
</footnote>
<footnote label="23">
<p id="b92-11"> The dissent points out that three-fifths of all rapes in the home, three-fifths of all home robberies, and about a third of home assaults are committed by burglars. <em>Post, </em>at 26-27. These figures mean only that if one knows that a suspect committed a rape in the home, there is a good chance that the suspect is also a burglar. That has nothing to do with the question here, which is whether the fact that someone has committed a burglary indicates that he has committed, or might commit, a violent crime.</p>
<p id="b92-12">The dissent also points out that this 3.8% adds up to 2.8 million violent crimes over a 10-year period, as if to imply that today’s holding will let loose 2.8 million violent burglars. The relevant universe is, of course, far smaller. At issue is only that tiny fraction of cases where violence has <page-number citation-index="1" label="23">*23</page-number>taken place and an officer who has no other means of apprehending the suspect is unaware of its occurrence.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Terry v. Ohio.md  (`case`, 7 assertions)

### content_page

```
---
title: "Terry v. Ohio"
type: case
citation: "392 U.S. 1 (1968)"
parallel_cite: "88 S. Ct. 1868; 20 L. Ed. 2d 889; 44 Ohio Op. 2d 383"
neutral_cite: 1968 U.S. LEXIS 1345
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1968
date_decided: 1968-06-10
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1968-06-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Terry v. Ohio
  varies_by_point: false
  scope_note: "Foundational stop-and-frisk authority; repeatedly reaffirmed and refined (Cortez, Arvizu, Wardlow)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107729/terry-v-ohio/"
  cluster_id: 107729
  opinion_id: 9423752
  identity_checked: true
homes:
  - page: "[[Reasonable Suspicion]]"
    role: "Key — Anchor"
  - page: "[[Traffic Stops]]"
    role: "Related (cross-doctrine)"
  - page: "[[The Proof Ladder]]"
    role: "Key — rung anchor"
related: ["[[United States v. Cortez]]", "[[United States v. Arvizu]]", "[[Illinois v. Wardlow]]", "[[Florida v. J.L.]]", "[[Hiibel v. Sixth Judicial Dist. Court]]"]
aliases: []
tags: ["case", "fourth-amendment", "terry-stop", "reasonable-suspicion"]
holding: "An investigative stop and protective frisk require reasonable, articulable suspicion grounded in specific facts and rational inferences…"
lake:
  record_id: Terry v. Ohio
  status: verified
  projected_at: 2026-07-09
---

# Terry v. Ohio

*392 U.S. 1 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A veteran Cleveland detective watched two men repeatedly walk past and peer into a store window, conferring between passes — conduct he took to be casing the store for a daytime robbery. He approached, identified himself, asked their names, and when they "mumbled" he spun Terry around and patted down the outside of his clothing, feeling a pistol. Terry was charged with carrying a concealed weapon and moved to suppress the gun.

## Issue
Whether a police officer who lacks probable cause to arrest may, consistent with the Fourth Amendment, stop a person to investigate suspicious conduct and conduct a limited pat-down of the outer clothing for weapons.

## Rule
A brief investigative stop must rest on specific, objective facts, not a hunch: "in justifying the particular intrusion the police officer must be able to point to specific and articulable facts which, taken together with rational inferences from those facts, reasonably warrant that intrusion." — 392 U.S. at 21. ^pin-21

A protective frisk is permitted where the officer reasonably fears for safety: "the issue is whether a reasonably prudent man in the circumstances would be warranted in the belief that his safety or that of others was in danger." — [*Id.* at 27](https://www.courtlistener.com/opinion/107729/terry-v-ohio/#:~:text=the%20issue%20is%20whether%20a). ^pin-27

The Court held that "where a police officer observes unusual conduct which leads him reasonably to conclude in light of his experience that criminal activity may be afoot and that the persons with whom he is dealing may be armed and presently dangerous, where in the course of investigating this behavior he identifies himself as a policeman and makes reasonable inquiries, and where nothing in the initial stages of the encounter serves to dispel his reasonable fear for his own or others' safety, he is entitled for the protection of himself and others in the area to conduct a carefully limited search of the outer clothing of such persons in an attempt to discover weapons which might be used to assault him." — *Id.* at 30. ^pin-30

## Application
On these facts the detective's observations — two men taking turns walking the same route and staring into the store window roughly a dozen times, then conferring — supplied specific, articulable facts warranting a brief stop and supporting a reasonable belief the men were contemplating a daylight robbery and were armed. Because that belief was reasonable, the limited pat-down of the outer clothing that produced Terry's pistol was a reasonable search, and the weapon was properly admitted.

## Conclusion
The stop and protective frisk were reasonable under the Fourth Amendment; Terry's conviction was affirmed. A weapons pat-down on reasonable suspicion is permissible without probable cause to arrest.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The reasonable-suspicion standard was elaborated in [[United States v. Cortez]] ("particularized and objective basis"; "whole picture") and [[United States v. Arvizu]] ([[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]; no "divide-and-conquer"), and applied to flight in [[Illinois v. Wardlow]] and anonymous tips in [[Florida v. J.L.]].

## Appears on
- [[Reasonable Suspicion]] — *Key — Anchor*
- [[Traffic Stops]] — *Related (cross-doctrine)*
- [[The Proof Ladder]] — *Key — rung anchor*

## Sources
- *Terry v. Ohio*, 392 U.S. 1 (1968) — https://www.courtlistener.com/opinion/107729/terry-v-ohio/ — pinpoints: 21, 27, 30.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "88874b49d2f849d6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "392 U.S. 1 (1968)", "court": "U.S. Supreme Court", "neutral_cite": "1968 U.S. LEXIS 1345", "official_citation_present": true, "parallel_cite": "88 S. Ct. 1868; 20 L. Ed. 2d 889; 44 Ohio Op. 2d 383", "title": "Terry v. Ohio", "year": "1968"}}
{"assertion_id": "07ba859eabd30266", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An investigative stop and protective frisk require reasonable, articulable suspicion grounded in specific facts and rational inferences…", "title": "Terry v. Ohio"}}
{"assertion_id": "3b154a50a1ebbe85", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Suspicion"}, "payload": {"home": "Reasonable Suspicion", "role": "Key — Anchor", "title": "Terry v. Ohio"}}
{"assertion_id": "4d3380d12812635f", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Related (cross-doctrine)", "title": "Terry v. Ohio"}}
{"assertion_id": "5a93cd4677cb97d6", "dimension": "support", "kind": "home_role", "locator": {"home": "The Proof Ladder"}, "payload": {"home": "The Proof Ladder", "role": "Key — rung anchor", "title": "Terry v. Ohio"}}
{"assertion_id": "5eea274acc0e195e", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1968-06-10", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Terry v. Ohio", "field_i_validity": "good_law", "scope_note": "Foundational stop-and-frisk authority; repeatedly reaffirmed and refined (Cortez, Arvizu, Wardlow).", "title": "Terry v. Ohio", "varies_by_point": "false"}}
{"assertion_id": "f7ccffc312c2265f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Terry v. Ohio"}}
```

### lake record — Terry v. Ohio

```json
{
  "schema_version": "s2.v1",
  "record_id": "Terry v. Ohio",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Terry v. Ohio",
    "case_name_short": "Terry",
    "case_name_full": "Terry v. Ohio",
    "input_case_name": "Terry v. Ohio",
    "court": "U.S. Supreme Court",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-06-10",
    "year": 1968,
    "docket": null,
    "cluster_id": 107729,
    "lead_opinion_id": 9423752,
    "sibling_ids": [
      107729,
      9423752,
      9423753,
      9423754,
      9423755
    ],
    "absolute_url": "/opinion/107729/terry-v-ohio/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "392 U.S. 1",
      "volume": "392",
      "reporter": "U.S.",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 1868",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1868",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 889",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "889",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "44 Ohio Op. 2d 383",
        "volume": "44",
        "reporter": "Ohio Op. 2d",
        "page": "383",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 1345",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1345",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "392 U.S. 1",
        "volume": "392",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 1868",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1868",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 889",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "889",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 1345",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1345",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "44 Ohio Op. 2d 383",
        "volume": "44",
        "reporter": "Ohio Op. 2d",
        "page": "383",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "392 U.S. 1",
    "official_selection": {
      "court_class": "scotus",
      "selected": "392 U.S. 1",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-21",
      "page": null,
      "quote": "he spun Terry around and patted down the outside of his clothing, feeling a pistol. Terry was charged with carrying a concealed weapon and moved to suppress the gun. ## Issue Whether a police officer who lacks probable cause to arrest may, consistent with the Fourth Amendment, stop a person to investigate suspicious conduct and conduct a limited pat-down of the outer clothing for weapons. ## Rule A brief investigative stop must rest on specific, objective facts, not a hunch:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-27",
      "page": null,
      "quote": "the issue is whether a reasonably prudent man in the circumstances would be warranted in the belief that his safety or that of others was in danger.",
      "star_marker": "27",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 43222,
      "fragment": "#:~:text=the%20issue%20is%20whether%20a",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-30",
      "page": null,
      "quote": "where a police officer observes unusual conduct which leads him reasonably to conclude in light of his experience that criminal activity may be afoot and that the persons with whom he is dealing may be armed and presently dangerous, where in the course of investigating this behavior he identifies himself as a policeman and makes reasonable inquiries, and where nothing in the initial stages of the encounter serves to dispel his reasonable fear for his own or others' safety, he is entitled for the protection of himself and others in the area to conduct a carefully limited search of the outer clothing of such persons in an attempt to discover weapons which might be used to assault him.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1968-06-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Terry v. Ohio",
    "varies_by_point": false,
    "scope_note": "Foundational stop-and-frisk authority; repeatedly reaffirmed and refined (Cortez, Arvizu, Wardlow).",
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
        "journal_ref": "Terry v. Ohio:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bivens v. Six Unknown Named Agents of Federal Bureau of Narcotics",
          "cluster_id": 108375,
          "cite": [
            "29 L. Ed. 2d 619",
            "91 S. Ct. 1999",
            "403 U.S. 388",
            "1971 U.S. LEXIS 23"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bell v. Wolfish",
          "cluster_id": 110075,
          "cite": [
            "60 L. Ed. 2d 447",
            "99 S. Ct. 1861",
            "441 U.S. 520",
            "1979 U.S. LEXIS 100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mendenhall",
          "cluster_id": 110264,
          "cite": [
            "64 L. Ed. 2d 497",
            "100 S. Ct. 1870",
            "446 U.S. 544",
            "1980 U.S. LEXIS 102"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cortez",
          "cluster_id": 110377,
          "cite": [
            "66 L. Ed. 2d 621",
            "101 S. Ct. 690",
            "449 U.S. 411",
            "1981 U.S. LEXIS 58",
            "49 U.S.L.W. 4099"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roe v. Wade",
          "cluster_id": 108713,
          "cite": [
            "35 L. Ed. 2d 147",
            "93 S. Ct. 705",
            "410 U.S. 113",
            "1973 U.S. LEXIS 159"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Delaware v. Prouse",
          "cluster_id": 110045,
          "cite": [
            "59 L. Ed. 2d 660",
            "99 S. Ct. 1391",
            "440 U.S. 648",
            "1979 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adams v. Williams",
          "cluster_id": 108571,
          "cite": [
            "32 L. Ed. 2d 612",
            "92 S. Ct. 1921",
            "407 U.S. 143",
            "1972 U.S. LEXIS 2206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul v. Davis",
          "cluster_id": 109402,
          "cite": [
            "47 L. Ed. 2d 405",
            "96 S. Ct. 1155",
            "424 U.S. 693",
            "1976 U.S. LEXIS 112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Illinois",
          "cluster_id": 109304,
          "cite": [
            "45 L. Ed. 2d 416",
            "95 S. Ct. 2254",
            "422 U.S. 590",
            "1975 U.S. LEXIS 82"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Atweri",
          "cluster_id": 10807071,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane3_recency"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107729 OR 9423752 OR 9423753 OR 9423754 OR 9423755) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzQ2NjYyNDAwMDAwJnM9MTA1NzMxMzgmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107729+OR+9423752+OR+9423753+OR+9423754+OR+9423755%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 100,
        "triage_read": 1,
        "triage_snippet_classified": 99
      },
      "lane2_top_cited": {
        "query": "cites:(107729 OR 9423752 OR 9423753 OR 9423754 OR 9423755)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNDE1JnM9MTA4ODk4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107729+OR+9423752+OR+9423753+OR+9423754+OR+9423755%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107729 OR 9423752 OR 9423753 OR 9423754 OR 9423755)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzU0MDA2NDAwMDAwJnM9MTA2NDYyNjQmdD1vJmQ9MjAyNi0wNy0wNiZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107729+OR+9423752+OR+9423753+OR+9423754+OR+9423755%29&type=o",
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
    "complete_query": "cites:(107729 OR 9423752 OR 9423753 OR 9423754 OR 9423755)",
    "indexed_citing_opinions": 22182,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107729,
        "count": 19711,
        "count_source": "search"
      },
      {
        "opinion_id": 9423752,
        "count": 2968,
        "count_source": "search"
      },
      {
        "opinion_id": 9423753,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423754,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423755,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 37960,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/terry-v-ohio.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yLjYyMDg3MyZzPTIyMDM1NiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28107729+OR+9423752+OR+9423753+OR+9423754+OR+9423755%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LRU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-04T14:57:50Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T14:57:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T14:57:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:24:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T14:57:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Terry v. Ohio

```
<opinion type="majority">
<author id="b46-9">Mr. Chief Justice Warren</author>
<p id="Ao">delivered the opinion of the Court.</p>
<p id="b46-10">This case presents serious questions concerning the role of the Fourth Amendment in the confrontation on the street between the citizen and the policeman investigating suspicious circumstances.</p>
<p id="b46-11">Petitioner Terry was convicted of carrying a concealed weapon and sentenced to the statutorily prescribed term of one to three years in the penitentiary.<footnotemark>1</footnotemark> Following <page-number citation-index="1" label="5">*5</page-number>the denial of a pretrial motion to suppress, the prosecution introduced in evidence two revolvers and a number of bullets seized from Terry and a codefendant, Richard Chilton,<footnotemark>2</footnotemark> by Cleveland Police Detective Martin McFadden. At the hearing on the motion to suppress this evidence, Officer McFadden testified that while he was patrolling in plain clothes in downtown Cleveland at approximately 2:30 in the afternoon of October 31, 1963, his attention was attracted by two men, Chilton and Terry, standing on the corner of Huron Road and Euclid Avenue. He had never seen the two men before, and he was unable to say precisely what first drew his eye to them. However, he testified that he had been a policeman for 39 years and a detective for 35 and that he had been assigned to patrol this vicinity of downtown Cleveland for shoplifters and pickpockets for 30 years. He explained that he had developed routine habits of observation over the years and that he would “stand and watch people or walk and watch people at many intervals of the day.” He added: “Now, in this case when I looked over they didn’t look right to me at the time.”</p>
<p id="b47-5">His interest aroused, Officer McFadden took up a post of observation in the entrance to a store 300 to 400 feet <page-number citation-index="1" label="6">*6</page-number>away from the two men. “I get more purpose to watch them when I seen their movements,” he testified. He saw one of the men leave the other one and walk southwest on Huron Road, past some stores. The man paused for a moment and looked in a store window, then walked on a short distance, turned around and walked back toward the corner, pausing once again to look in the same store window. He rejoined his companion at the comer, and the two conferred briefly. Then the second man went through the same series of motions, strolling down Huron Road, looking in the same window, walking on a short distance, turning back, peering in the store window again, and returning to confer with the first man at the corner. The two men repeated this ritual alternately between five and six times apiece — in all, roughly a dozen trips. At one point, while the two were standing together on the corner, a third man approached them and engaged them briefly in conversation. This man then left the two others and walked west on Euclid Avenue. Chilton and Terry resumed their measured pacing, peering, and conferring. After this had gone on for 10 to 12 minutes, the two men walked off together, heading west on Euclid Avenue, following the path taken earlier by the third man.</p>
<p id="b48-5">By this time Officer McFadden had become thoroughly suspicious. He testified that after observing their elaborately casual and oft-repeated reconnaissance of the store window on Huron Road, he suspected the two men of “casing a job, a stick-up,” and that he considered it his duty as a police officer to investigate further. He added that he feared “they may have a gun.” Thus, Officer McEadden followed Chilton and Terry and saw them stop in front of Zucker’s store to talk to the same man who had conferred with them earlier on the street corner. Deciding that the situation was ripe for direct action, Officer McFadden approached the three men, iden<page-number citation-index="1" label="7">*7</page-number>tified himself as a police officer and asked for their names. At this point his knowledge was confined to what he had observed. He was not acquainted with any of the three men by name or by sight, and he had received no information concerning them from any other source. When the men “mumbled something” in response to his inquiries, Officer McFadden grabbed petitioner Terry, spun him around so that they were facing the other two, with Terry between McFadden and the others, and patted down the outside of his clothing. In the left breast pocket of Terry’s overcoat Officer McFadden felt a pistol. He reached inside the overcoat pocket, but was unable to remove the gun. At this point, keeping Terry between himself and the others, the officer ordered all three men to enter Zucker’s store. As they went in, he removed Terry’s overcoat completely, removed a .38-caliber revolver from the pocket and ordered all three men to face the wall with their hands raised. Officer McFadden proceeded to pat down the outer clothing of Chilton and the third man, Katz. He discovered another revolver in the outer pocket of Chilton’s overcoat, but no weapons were found on Katz. The officer testified that he only patted the men down to see whether they had weapons, and that he did not put his hands beneath the outer garments of either Terry or Chilton until he felt their guns. So far as appears from the record, he never placed his hands beneath Katz’ outer garments. Officer McFadden seized Chilton’s gun, asked the proprietor of the store to call a police wagon, and took all three men to the station, where Chilton and Terry were formally charged with carrying concealed weapons.</p>
<p id="b49-5">On the motion to suppress the guns the prosecution took the position that they had been seized following a search incident to a lawful arrest. The trial court rejected this theory, stating that it “would be stretching the facts beyond reasonable comprehension” to find that Officer <page-number citation-index="1" label="8">*8</page-number>McFadden had had probable cause to arrest the men before he patted them down for weapons. However, the court denied the defendants’ motion on the ground that Officer McFadden, on the basis of his experience, “had reasonable cause to believe . . . that the defendants were conducting themselves suspiciously, and some interrogation should be made of their action.” Purely for his own protection, the court held, the officer had the right to pat down the outer clothing of these men, who he had reasonable cause to believe might be armed. The court distinguished between an investigatory “stop” and an arrest, and between a “frisk” of the outer clothing for weapons and a full-blown search for evidence of crime. The frisk, it held, was essential to the proper performance of the officer’s investigatory duties, for without it “the answer to the police officer may be a bullet, and a loaded pistol discovered during the frisk is admissible.”</p>
<p id="b50-5">After the court denied their motion to suppress, Chilton and Terry waived jury trial and pleaded not guilty. The court adjudged them guilty, and the Court of Appeals for the Eighth Judicial District, Cuyahoga County, affirmed. <em>State </em>v. <em>Terry, </em><span class="citation" data-id="3704293"><a href="/opinion/3954963/state-v-terry/" aria-description="Citation for case: State v. Terry">5 Ohio App. 2d 122</a></span>, <span class="citation" data-id="3704293"><a href="/opinion/3954963/state-v-terry/" aria-description="Citation for case: State v. Terry">214 N. E. 2d 114</a></span> (1966). The Supreme Court of Ohio dismissed their appeal on the ground that no “substantial constitutional question” was involved. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./387/929/">387 U. S. 929</a></span> (1967), to determine whether the admission of the revolvers in evidence violated petitioner’s rights under the Fourth Amendment, made applicable to the States by the Fourteenth. <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961). We affirm the conviction.</p>
<p id="b50-6">I.</p>
<p id="b50-7">The Fourth Amendment provides that “the right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated . . . .” This inestimable right of <page-number citation-index="1" label="9">*9</page-number>personal security belongs as much to the citizen on the streets of our cities as to the homeowner closeted in his study to dispose of his secret affairs. For, as this Court has always recognized,</p>
<blockquote id="b51-5">“No right is held more sacred, or is more carefully guarded, by the common law, than the right of every individual to the possession and control of his own person, free from all restraint or interference of others, unless by clear and unquestionable authority of law.” <em>Union Pac. R. Co. </em>v. <em>Botsford, </em><span class="citation" data-id="93149"><a href="/opinion/93149/union-pacific-railway-co-v-botsford/#251" aria-description="Citation for case: Union Pacific Railway Co. v. Botsford">141 U. S. 250, 251</a></span> (1891).</blockquote>
<p id="b51-6">We have recently held that “the Fourth Amendment protects people, not places,” <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967), and wherever an individual may harbor a reasonable “expectation of privacy,” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States"><em>id., </em>at 361</a></span> (Mr. Justice Harlan, concurring), he is entitled to be free from unreasonable governmental intrusion. Of course, the specific content and incidents of this right must be shaped by the context in which it is asserted. For “what the Constitution forbids is not all searches and seizures, but unreasonable searches and seizures.” <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#222" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 222</a></span> (1960). Unquestionably petitioner was entitled to the protection of the Fourth Amendment as he walked down the street in Cleveland. <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span> (1964); <em>Rios </em>v. <em>United States, </em><span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/" aria-description="Citation for case: Rios v. United States">364 U. S. 253</a></span> (1960); <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span> (1959); <em>United States </em>v. <em>Di Re, </em><span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/" aria-description="Citation for case: United States v. Di Re">332 U. S. 581</a></span> (1948); <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925). The question is whether in all the circumstances of this on-the-street encounter, his right to personal security was violated by an unreasonable search and seizure.</p>
<p id="b51-7">We would be less than candid if we did not acknowledge that this question thrusts to the fore difficult and troublesome issues regarding a sensitive area of police activity — issues which have never before been squarely <page-number citation-index="1" label="10">*10</page-number>presented to this Court. Reflective of the tensions involved are the practical and constitutional arguments pressed with great vigor on both sides of the public debate over the power of the police to “stop and frisk”— as it is sometimes euphemistically termed — suspicious persons.</p>
<p id="b52-4">On the one hand, it is frequently argued that in dealing with the rapidly unfolding and often dangerous situations on city streets the police are in need of an escalating set of flexible responses, graduated in relation to the amount of information they possess. For this purpose it is urged that distinctions should be made between a “stop” and an “arrest” (or a “seizure” of a person), and between a “frisk” and a “search.” <footnotemark>3</footnotemark> Thus, it is argued, the police should be allowed to “stop” a person and detain him briefly for questioning upon suspicion that he may be connected with criminal activity. Upon suspicion that the person may be armed, the police should have the power to “frisk” him for weapons. If the “stop” and the “frisk” give rise to probable cause to believe that the suspect has committed a crime, then the police should be empowered to make a formal “arrest,” and a full incident “search” of the person. This scheme is justified in part upon the notion that a “stop” and a “frisk” amount to a mere “minor inconvenience and petty indignity,” <footnotemark>4</footnotemark> which can properly be imposed upon the <page-number citation-index="1" label="11">*11</page-number>citizen in the interest of effective law enforcement on the basis of a police officer's suspicion.<footnotemark>5</footnotemark></p>
<p id="b53-5">On the other side the argument is made that the authority of the police must be strictly circumscribed by the law of arrest and search as it has developed to date in the traditional jurisprudence of the Fourth Amendment.<footnotemark>6</footnotemark> It is contended with some force that there is not — and cannot be — a variety of police activity which does not depend solely upon the voluntary cooperation of the citizen and yet which stops short of an arrest based upon probable cause to make such an arrest. The heart of the Fourth Amendment, the argument runs, is a severe requirement of specific justification for any intrusion upon protected personal security, coupled with á highly developed system of judicial controls to enforce upon the agents of the State the commands of the Constitution. Acquiescence by the courts in the compulsion inherent <page-number citation-index="1" label="12">*12</page-number>in the field interrogation practices at issue here, it is urged, would constitute an abdication of judicial control over, and indeed an encouragement of, substantial interference with liberty and personal security by police officers whose judgment is necessarily colored by their primary involvement in “the often competitive enterprise of ferreting out crime.” <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). This, it is argued, can only serve to exacerbate police-community tensions in the crowded centers of our Nation’s cities.<footnotemark>7</footnotemark></p>
<p id="b54-6">In this context we approach the issues in this case mindful of the limitations of the judicial function in controlling the myriad daily situations in which policemen and citizens confront each other on the street. The State has characterized the issue here as “the right of a police officer ... to make an on-the-street stop, interrogate and pat down for weapons (known in street vernacular as ‘stop and frisk’).”<footnotemark>8</footnotemark> But this is only partly accurate. For the issue is not the abstract propriety of the police conduct, but the admissibility against petitioner of the evidence uncovered by the search and seizure. Ever since its inception, the rule excluding evidence seized in violation of the Fourth Amendment has been recognized as a principal mode of discouraging lawless police conduct. See <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#391" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 391-393</a></span> (1914). Thus its major thrust is a deterrent one, see <em>Linkletter </em>v. <em>Walker, </em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#629" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 629-635</a></span> (1965), and experience has taught that it is the only effective deterrent to police misconduct in the criminal context, and that without it the constitutional guarantee against unreasonable searches and seizures would be a mere “form of words.” <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#655" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 655</a></span> (1961). The rule also serves another vital function — “the imperative of judicial integrity.” <em>Elkins </em><page-number citation-index="1" label="13">*13</page-number>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#222" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 222</a></span> (1960). Courts which sit under our Constitution cannot and will not be made party to lawless invasions of the constitutional rights of citizens by permitting unhindered governmental use of the fruits of such invasions. Thus in our system evidentiary rulings provide the context in which the judicial process of inclusion and exclusion approves some conduct as comporting with constitutional guarantees and disapproves other actions by state agents. A ruling admitting evidence in a criminal trial, we recognize, has the necessary effect of legitimizing the conduct which produced the evidence, while an application of the exclusionary rule withholds the constitutional imprimatur.</p>
<p id="b55-5">The exclusionary rule has its limitations, however, as a tool of judicial control. It cannot properly be invoked to exclude the products of legitimate police investigative techniques on the ground that much conduct which is closely similar involves unwarranted intrusions upon constitutional protections. Moreover, in some contexts the rule is ineffective as a deterrent. Street encounters between citizens and police officers are incredibly rich in diversity. They range from wholly friendly exchanges of pleasantries or mutually useful information to hostile confrontations of armed men involving arrests, or injuries, or loss of life. Moreover, hostile confrontations are not all of a piece. Some of them begin in a friendly enough manner, only to take a different turn upon the injection of some unexpected element into the conversation. Encounters are initiated by the police for a wide variety of purposes, some of which are wholly unrelated to a desire to prosecute for crime.<footnotemark>9</footnotemark> Doubtless some <page-number citation-index="1" label="14">*14</page-number>police “field interrogation” conduct violates the Fourth Amendment. But a stern refusal by this Court to condone such activity does not necessarily render it responsive to the exclusionary rule. Regardless of how effective the rule may be where obtaining convictions is an important objective of the police,<footnotemark>10</footnotemark> it is powerless to deter invasions of constitutionally guaranteed rights where the police either have no interest in prosecuting or are willing to forgo successful prosecution in the interest of serving some other goal.</p>
<p id="b56-6">Proper adjudication of cases in which the exclusionary rule is invoked demands a constant awareness of these limitations. The wholesale harassment by certain elements of the police community, of which minority groups, particularly Negroes, frequently complain,<footnotemark>11</footnotemark> will not be <page-number citation-index="1" label="15">*15</page-number>stopped by the exclusion of any evidence from any criminal trial. Yet a rigid and unthinking application of the exclusionary rule, in futile protest against practices which it can never be used effectively to control, may exact a high toll in human injury and frustration of efforts to prevent crime. No judicial opinion can comprehend the protean variety of the street encounter, and we can only judge the facts of the case before us. Nothing we say today is to be taken as indicating approval of police conduct outside the legitimate investigative sphere. Under our decision, courts still retain their traditional responsibility to guard against police conduct which is overbearing or harassing, or which trenches upon personal security without the objective evidentiary justification which the Constitution requires. When such conduct is identified, it must be condemned by the judiciary and its fruits must be excluded from evidence in criminal trials. And, of course, our approval of legitimate and restrained investigative conduct undertaken on the basis of ample factual justification should in no way discourage the employment of other remedies than the exclusionary rule to curtail abuses for which that sanction may prove inappropriate.</p>
<p id="b57-5">Having thus roughly sketched the perimeters of the constitutional debate over the limits on police investigative conduct in general and the background against which this case presents itself, we turn our attention to the quite narrow question posed by the facts before us: whether it is always unreasonable for a policeman to seize a person and subject him to a limited search for weapons unless there is probable cause for an arrest. <page-number citation-index="1" label="16">*16</page-number>Given the narrowness of this question, we have no occasion to canvass in detail the constitutional limitations upon the scope of a policeman’s power when he confronts a citizen without probable cause to arrest him.</p>
<p id="b58-6">II.</p>
<p id="b58-7">Our first task is to establish at what point in this encounter the Fourth Amendment becomes relevant. That is, we must decide whether and when Officer McFadden “seized” Terry and whether and when he conducted a “search.” There is some suggestion in the use of such terms as “stop” and “frisk” that such police conduct is outside the purview of the Fourth Amendment because neither action rises to the level of a “search” or “seizure” within the meaning of the Constitution.<footnotemark>12</footnotemark> We emphatically reject this notion. It is quite plain that the Fourth Amendment governs “seizures” of the person which do not eventuate in a trip to the station house and prosecution for crime — “arrests” in traditional terminology. It must be recognized that whenever a police officer accosts an individual and restrains his freedom to walk away, he has “seized” that person. And it is nothing less than sheer torture of the English language to suggest that a careful exploration of the outer surfaces of a person’s clothing all over his or her body in an attempt to find weapons is not a “search.” Moreover, it is simply fantastic to urge that such a procedure <page-number citation-index="1" label="17">*17</page-number>performed in public by a policeman while the citizen stands helpless, perhaps facing a wall with his hands raised, is a “petty indignity.” <footnotemark>13</footnotemark> It is a serious intrusion upon the sanctity of the person, which may inflict great indignity and arouse strong resentment, and it is not to be undertaken lightly.<footnotemark>14</footnotemark></p>
<p id="b59-5">The danger in the logic which proceeds upon distinctions between a “stop” and an “arrest,” or “seizure” of the person, and between a “frisk” and a “search” is twofold. It seeks to isolate from constitutional scrutiny the initial stages of the contact beween the policeman and the citizen. And by suggesting a rigid all-or-nothing model of justification and regulation under the Amendment, it obscures the utility of limitations upon the scope, as well as the initiation, of police action as a means of constitutional regulation.<footnotemark>15</footnotemark> This Court has held in <page-number citation-index="1" label="18">*18</page-number>the past that a search which is reasonable at its inception may violate the Fourth Amendment by virtue of its intolerable intensity and scope. <em>Kremen </em>v. <em>United States, </em><span class="citation" data-id="8931353"><a href="/opinion/8940894/kremen-v-united-states/" aria-description="Citation for case: Kremen v. United States">353 U. S. 346</a></span> (1957); <em>Go-Bart Importing Co. </em>v. <page-number citation-index="1" label="19">*19</page-number><em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#356" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 356-358</a></span> (1931); see <em>United States </em>v. <em>Di Re, </em><span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#586" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 586-587</a></span> (1948). The scope of the search must be “strictly tied to and justified by” the circumstances which rendered its initiation permissible. <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#310" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 310</a></span> (1967) (Mr. Justice Fortas, concurring); see, <em>e. g., Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367-368</a></span> (1964); <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30-31</a></span> (1925).</p>
<p id="b61-5">The distinctions of classical “stop-and-frisk” theory thus serve to divert attention from the central inquiry under the Fourth Amendment — the reasonableness in all the circumstances of the particular governmental invasion of a citizen’s personal security. “Search” and “seizure” are not talismans. We therefore reject the notions that the Fourth Amendment does not come into play at all as a limitation upon police conduct if the officers stop short of something called a “technical arrest” or a “full-blown search.”</p>
<p id="b61-6">In this case there can be no question, then, that Officer McFadden “seized” petitioner and subjected him to a “search” when he took hold of him and patted down the outer surfaces of his clothing. We must decide whether at that point it was reasonable for Officer McFadden to have interfered with petitioner’s personal security as he did.<footnotemark>16</footnotemark> And in determining whether the seizure and search were “unreasonable” our inquiry <page-number citation-index="1" label="20">*20</page-number>is a dual one — whether the officer's action was justified at its inception, and whether it was reasonably related in scope to the circumstances which justified the interference in the first place.</p>
<p id="b62-4">III.</p>
<p id="b62-5">If this case involved police conduct subject to the Warrant Clause of the Fourth Amendment, we would have to ascertain whether “probable cause” existed to justify the search and seizure which took place. However, that is not the case. We do not retreat from our holdings that the police must, whenever practicable, obtain advance judicial approval of searches and seizures through the warrant procedure, see, <em>e. g., Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967); <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 96</a></span> (1964); <em>Chapman </em>v. <em>United States, </em><span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span> (1961), or that in most instances failure to comply with the warrant requirement can only be excused by exigent circumstances, see, <em>e. g., Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967) (hot pursuit); cf. <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367-368</a></span> (1964). But we deal here with an entire rubric of police conduct — necessarily swift action predicated upon the on-the-spot observations of the officer on the beat — which historically has not been, and as a practical matter could not be, subjected to the warrant procedure. Instead, the conduct involved in this case must be tested by the Fourth Amendment's general proscription against unreasonable searches and seizures.<footnotemark>17</footnotemark></p>
<p id="b62-6">Nonetheless, the notions which underlie both the warrant procedure and the requirement of probable cause remain fully relevant in this context. In order to assess the reasonableness of Officer McFadden’s conduct as a general proposition, it is necessary “first to focus upon <page-number citation-index="1" label="21">*21</page-number>the governmental interest which allegedly justifies official intrusion upon the constitutionally protected interests of the private citizen,” for there is “no ready test for determining reasonableness other than by balancing the need to search [or seize] against the invasion which the search [or seizure] entails.” <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 534-535, 536-537</a></span> (1967). And in justifying the particular intrusion the police officer must be able to point to specific and articulable facts which, taken together with rational inferences from those facts, reasonably warrant that intrusion.<footnotemark>18</footnotemark> The scheme of the Fourth Amendment becomes meaningful only when it is assured that at some point the conduct of those charged with enforcing the laws can be subjected to the more detached, neutral scrutiny of a judge who must evaluate the reasonableness of a particular search or seizure in light of the particular circumstances.<footnotemark>19</footnotemark> And in making that assessment it is imperative that the facts be judged against an objective standard: would the facts <page-number citation-index="1" label="22">*22</page-number>available to the officer at the moment of the seizure or the search “warrant a man of reasonable caution in the belief” that the action taken was appropriate? Cf. <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925); <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 96-97</a></span> (1964).<footnotemark>20</footnotemark> Anything less would invite intrusions upon constitutionally guaranteed rights based on nothing more substantia] than inarticulate hunches, a result this Court has. consistently refused to sanction. See, <em>e. g., Beck </em>v. <em>Ohio, supra; Rios </em>v. <em>United States, </em><span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/" aria-description="Citation for case: Rios v. United States">364 U. S. 253</a></span> (1960); <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span> (1959). And simple “'good faith on the part of the arresting officer is not enough.’ ... If subjective good faith alone were the test, the protections of the Fourth Amendment would evaporate, and the people would be 'secure in their persons, houses, papers, and effects,’ only in the discretion of the police.” <em>Beck </em>v. <em>Ohio, supra, </em>at 97.</p>
<p id="b64-5">Applying these principles to this case, we consider first the nature and extent of the governmental interests involved. One general interest is of course that of effective crime prevention and detection; it is this interest which underlies the recognition that a police officer may in appropriate circumstances and in an appropriate manner approach a person for purposes of investigating possibly criminal behavior even though there is no probable cause to make an arrest. It was this legitimate investigative function Officer McFadden was discharging when he decided to approach petitioner and his companions. He had observed Terry, Chilton, and Katz go through a series of acts, each of them perhaps innocent in itself, but which taken together warranted further investigation. There is nothing unusual in two men standing together on a street corner, perhaps waiting for someone. Nor is there anything suspicious about people <page-number citation-index="1" label="23">*23</page-number>in such circumstances strolling up and down the street, singly or in pairs. Store windows, moreover, are made to be looked in. But the story is quite different where, as here, two men hover about a street corner for an extended period of time, at the end of which it becomes apparent that they are not waiting for anyone or anything ; where these men pace alternately along an identical route, pausing to stare in the same store window roughly 24 times; where each completion of this route is followed immediately by a conference between the two men on the corner; where they are joined in one of these conferences by a third man who leaves swiftly; and where the two men finally follow the third and rejoin him a couple of blocks away. It would have been poor police work indeed for an officer of 30 years’ experience in the detection of thievery from stores in this same neighborhood to have failed to investigate this behavior further.</p>
<p id="b65-5">The crux of this case, however, is not the propriety of Officer McFadden’s taking steps to investigate petitioner’s suspicious behavior, but rather, whether there was justification for McFadden’s invasion of Terry’s personal security by searching him for weapons in the course of that investigation. We are now concerned with more than the governmental interest in investigating crime; in addition, there is the more immediate interest of the police officer in taking steps to assure himself that the person with whom he is dealing is not armed with a weapon that could unexpectedly and fatally be used against him. Certainly it would be unreasonable to require that police officers take unnecessary risks in the performance of their duties. American criminals have a long tradition of armed violence, and every year in this country many law enforcement officers are killed in the line of duty, and thousands more are wounded. <page-number citation-index="1" label="24">*24</page-number>Virtually all of these deaths and a substantial portion of the injuries are inflicted with guns and knives.<footnotemark>21</footnotemark></p>
<p id="b66-6">In view of these facts, we cannot blind ourselves to the need for law enforcement officers to protect themselves and other prospective victims of violence in situations where they may lack probable cause for an arrest. When an officer is justified in believing that the individual whose suspicious behavior he is investigating at close range is armed and presently dangerous to the officer or to others, it would appear to be clearly unreasonable to deny the officer the power to take necessary measures to determine whether the person is in fact carrying a weapon and to neutralize the threat of physical harm.</p>
<p id="b66-7">We must still consider, however, the nature and quality of the intrusion on individual rights which must be accepted if police officers are to be conceded the right to search for weapons in situations where probable cause to arrest for crime is lacking. Even a limited search of the outer clothing for weapons constitutes a severe, <page-number citation-index="1" label="25">*25</page-number>though brief, intrusion upon cherished personal security, and it must surely be an annoying, frightening, and perhaps humiliating experience. Petitioner contends that such an intrusion is permissible only incident to a lawful arrest, either for a crime involving the possession of weapons or for a crime the commission of which led the officer to investigate in the first place. However, this argument must be closely examined.</p>
<p id="b67-5">Petitioner does not argue that a police officer should refrain from making any investigation of suspicious circumstances until such time as he has probable cause to make an arrest; nor does he deny that police officers in properly discharging their investigative function may find themselves confronting persons who might well be armed and dangerous. Moreover, he does not say that an officer is always unjustified in searching a suspect to discover weapons. Rather, he says it is unreasonable for the policeman to take that step until such time as the situation evolves to a point where there is probable cause to make an arrest. When that point has been reached, petitioner would concede the officer’s right to conduct a search of the suspect for weapons, fruits or instrumentalities of the crime, or “mere” evidence, incident to the arrest.</p>
<p id="b67-6">There are two weaknesses in this line of reasoning, however. First, it fails to take account of traditional limitations upon the scope of searches, and thus recognizes no distinction in purpose, character, and extent between a search incident to an arrest and a limited search for weapons. The former, although justified in part by the acknowledged necessity to protect the arresting officer from assault with a concealed weapon, <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964), is also justified on other grounds, <em>ibid., </em>and can therefore involve a relatively extensive exploration of the person. A search for weapons in the absence of probable cause to <page-number citation-index="1" label="26">*26</page-number>arrest, however, must, like any other search, be strictly circumscribed by the exigencies which justify its initiation. <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#310" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 310</a></span> (1967) (Mr. Justice Fortas, concurring). Thus it must be limited to that which is necessary for the discovery of weapons which might be used to harm the officer or others nearby, and may realistically be characterized as something less than a “full” search, even though it remains a serious intrusion.</p>
<p id="b68-6">A second, and related, objection to petitioner’s argument is that it assumes that the law of arrest has already worked out the balance between the particular interests involved here — the neutralization of danger to the policeman in the investigative circumstance and the sanctity of the individual. But this is not so. An arrest is a wholly different kind of intrusion upon individual freedom from a limited search for weapons, and the interests each is designed to serve are likewise quite different. An arrest is the initial stage of a criminal prosecution. It is intended to vindicate society’s interest in having its laws obeyed, and it is inevitably accompanied by future interference with the individual’s freedom of movement, whether or not trial or conviction ultimately follows.<footnotemark>22</footnotemark> The protective search for weapons, on the other hand, constitutes a brief, though far from inconsiderable, intrusion upon the sanctity of the person. It does not follow that because an officer may lawfully arrest a person only when he is apprised of facts sufficient to warrant a belief that the person has committed or is committing a crime, the officer is equally unjustified, absent that kind of evidence, in making any intrusions short of an arrest. Moreover, a perfectly reasonable apprehension of danger may arise long before the officer is possessed of adequate information to justify taking a person into custody for <page-number citation-index="1" label="27">*27</page-number>the purpose of prosecuting him for a crime. Petitioner’s reliance on cases which have worked out standards of reasonableness with regard to “seizures” constituting arrests and searches incident thereto is thus misplaced. It assumes that the interests sought to be vindicated and the invasions of personal security may be equated in the two cases, and thereby ignores a vital aspect of the analysis of the reasonableness of particular types of conduct under the Fourth Amendment. See <em>Camara </em>v. <em>Municipal <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Court, supra.</a></span></em></p>
<p id="b69-5">Our evaluation of the proper balance that has to be struck in this type of case leads us to conclude that there must be a narrowly drawn authority to permit a reasonable search for weapons for the protection of the police officer, where he has reason to believe that he is dealing with an armed and dangerous individual, regardless of whether he has probable cause to arrest the individual for a crime. The officer need not be absolutely certain that the individual is armed; the issue is whether a reasonably prudent man in the circumstances would be warranted in the belief that his safety or that of others was in danger. Cf. <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#91" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 91</a></span> <em>(1964); Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#174" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 174-176</a></span> (1949); <em>Stacey </em>v. <em>Emery, </em><span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/#645" aria-description="Citation for case: Stacey v. Emery">97 U. S. 642, 645</a></span> (1878).<footnotemark>23</footnotemark> And in determining whether the officer acted reasonably in such circumstances, due weight must be given, not to his inchoate and unparticularized suspicion or “hunch,” but to the specific reasonable inferences which he is entitled to draw from the facts in light of his experience. Cf. <em>Brinegar </em>v. <em>United States supra.</em></p>
<p id="b69-6">IY.</p>
<p id="b69-7">We must now examine the conduct of Officer McFadden in this case to determine whether his search and seizure of petitioner were reasonable, both at their in<page-number citation-index="1" label="28">*28</page-number>ception and as conducted. He had observed Terry, together with Chilton and another man, acting in a manner he took to be preface to a “stick-up.” We think on the facts and circumstances Officer McFadden detailed before the trial judge a reasonably prudent man would have been warranted in believing petitioner was armed and thus presented a threat to the officer’s safety while he was investigating his suspicious behavior. The actions of Terry and Chilton were consistent with McFadden’s hypothesis that these men were contemplating a daylight robbery — which, it is reasonable to assume, would be likely to involve the use of weapons — and nothing in their conduct from the time he first noticed them until the time he confronted them and identified himself as a police officer gave him sufficient reason to negate that hypothesis. Although the trio had departed the original scene, there was nothing to indicate abandonment of an intent to commit a robbery at some point. Thus, when Officer McFadden approached the three men gathered before the display window at Zucker’s store he had observed enough to make it quite reasonable to fear that they were armed; and nothing in their response to his hailing them, identifying himself as a police officer, and asking their names served to dispel that reasonable belief. We cannot say his decision at that point to seize Terry and pat his clothing for weapons was the product of a volatile or inventive imagination, or was undertaken simply as an act of harassment; the record evidences the tempered act of a policeman who in the course of an investigation had to make a quick decision as to how to protect himself and others from possible danger, and took limited steps to do so.</p>
<p id="b70-5">The manner in which the seizure and search were conducted is, of course, as vital a part of the inquiry as whether they were warranted at all. The Fourth Amendment proceeds as much by limitations upon the <page-number citation-index="1" label="29">*29</page-number>scope of governmental action as by imposing preconditions upon its initiation. Compare <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#354" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 354-356</a></span> (1967). The entire deterrent purpose of the rule excluding evidence seized in violation of the Fourth Amendment rests on the assumption that “limitations upon the fruit to be gathered tend to limit the quest itself.” <em>United States </em>v. <em>Poller, </em><span class="citation" data-id="1476321"><a href="/opinion/1476321/united-states-v-poller/#914" aria-description="Citation for case: United States v. Poller">43 F. 2d 911, 914</a></span> (C. A. 2d Cir. 1930); see, <em>e. g., Linkletter </em>v. <em>Walker, </em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#629" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 629-635</a></span> (1965); <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961); <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#216" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 216-221</a></span> (1960). Thus, evidence may not be introduced if it was discovered by means of a seizure and search which were not reasonably related in scope to the justification for their initiation. <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#310" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 310</a></span> (1967) (Mr. Justice Fortas, concurring).</p>
<p id="b71-5">We need not develop at length in this case, however, the limitations which the Fourth Amendment places upon a protective seizure and search for weapons. These limitations will have to be developed in the concrete factual circumstances of individual cases. See <em>Sibron </em>v. <em>New York, post, </em>p. 40, decided today. Suffice it to note that such a search, unlike a search without a warrant incident to a lawful arrest, is not justified by any need to prevent the disappearance or destruction of evidence of crime. See <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964). The sole justification of the search in the present situation is the protection of the police officer and others nearby, and it must therefore be confined in scope to an intrusion reasonably designed to discover guns, knives, clubs, or other hidden instruments for the assault of the police officer.</p>
<p id="b71-6">The scope of the search in this case presents no serious problem in light of these standards. Officer McFadden patted down the outer clothing of petitioner and his two companions. He did not place his hands in their pockets or under the outer surface of their garments until he had <page-number citation-index="1" label="30">*30</page-number>felt weapons, and then he merely reached for and removed the guns. He never did invade Katz’ person beyond the outer surfaces of his clothes, since he discovered nothing in his pat-down which might have been a weapon. Officer McFadden confined his search strictly to what was minimally necessary to learn whether the men were armed and to disarm them once he discovered the weapons. He did not conduct a general exploratory search for whatever evidence of criminal activity he might find.</p>
<p id="b72-4">V.</p>
<p id="b72-5">We conclude that the revolver seized from Terry was properly admitted in evidence against him. At the time he seized petitioner and searched him for weapons, Officer McFadden had reasonable grounds to believe that petitioner was armed and dangerous, and it was necessary for the protection of himself and others to take swift measures to discover the true facts and neutralize the threat of harm if it materialized. The policeman carefully restricted his search to what was appropriate to the discovery of the particular items which he sought. Each case of this sort will, of course, have to be decided on its own facts. We merely hold today that where a police officer observes unusual conduct which leads him reasonably to conclude in light of his experience that criminal activity may be afoot and that the persons with whom he is dealing may be armed and presently dangerous, where in the course of investigating this behavior he identifies himself as a policeman and makes reasonable inquiries, and where nothing in the initial stages of the encounter serves to dispel his reasonable fear for his own or others’ safety, he is entitled for the protection of himself and others in the area to conduct a carefully limited search of the outer clothing of such persons in an attempt to discover weapons which might be used to assault him. <page-number citation-index="1" label="31">*31</page-number>Such a search is a reasonable search under the Fourth Amendment, and any weapons seized may properly be introduced in evidence against the person from whom they were taken. <em>Affirmed.</em></p>
<judges id="b73-5">Mr. Justice Black concurs in the judgment and the opinion except where the opinion quotes from and relies upon this Court’s opinion in <em>Katz </em>v. <em>United States </em>and the concurring opinion in <em>Warden </em>v. <em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden</a></span>.</em></judges>
<footnote label="1">
<p id="b46-12"> Ohio Rev. Code §2923.01 (1953) provides in part that “[n]o person shall carry a pistol, bowie knife, dirk, or other dangerous weapon concealed on or about his person.” An exception is made for properly authorized law enforcement officers.</p>
</footnote>
<footnote label="2">
<p id="b47-6"> Terry and Chilton were arrested, indicted, tried, and convicted together. They were represented by the same attorney, and they made a joint motion to suppress the guns. After the motion was denied, evidence was taken in the case against Chilton. This evidence consisted of the testimony of the arresting officer and of Chilton. It was then stipulated that this testimony would be applied to the ease against Terry, and no further evidence was introduced in that case. The trial judge considered the two eases together, rendered the decisions at the same time and sentenced the two men at the same time. They prosecuted their state court appeals together through the same attorney, and they petitioned this Court for cer-tiorari together. Following the grant of the writ upon this joint petition, Chilton died. Thus, only Terry’s conviction is here for review.</p>
</footnote>
<footnote label="3">
<p id="b52-5"> Both the trial court and the Ohio Court of Appeals in this case relied upon such a distinction. <em>State </em>v. <em>Terry, </em><span class="citation" data-id="3704293"><a href="/opinion/3954963/state-v-terry/#125" aria-description="Citation for case: State v. Terry">5 Ohio App. 2d 122, 125-130</a></span>, <span class="citation" data-id="3704293"><a href="/opinion/3954963/state-v-terry/#117" aria-description="Citation for case: State v. Terry">214 N. E. 2d 114, 117-120</a></span> (1966). See also, e. <em>g., People </em>v. <em>Rivera, </em>14 N. Y. 2d 441, <span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/" aria-description="Citation for case: People v. Rivera">201 N. E. 2d 32</a></span>, 252 N. Y. S. 2d 458 (1964), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./379/978/">379 U. S. 978</a></span> (1965); Aspen, Arrest and Arrest Alternatives: Recent Trends, 1966 U. Ill. L. F. 241, 249-254; Warner, The Uniform Arrest Act, <span class="citation no-link">28 Va. L. Rev. 315</span> (1942); Note, Stop and Frisk in California, 18 Hastings L. J. 623, 629-632 (1967).</p>
</footnote>
<footnote label="4">
<p id="b52-6"> <em>People </em>v. <span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/#3" aria-description="Citation for case: People v. Rivera"><em>Rivera, supra, </em>n. 3</a></span>, at 447, <span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/#36" aria-description="Citation for case: People v. Rivera">201 N. E. 2d, at 36</a></span>, 252 N. Y. S. 2d, at 464.</p>
</footnote>
<footnote label="5">
<p id="b53-6"> The theory is well laid out in the <em><span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/" aria-description="Citation for case: People v. Rivera">Rivera</a></span> </em>opinion:</p>
<blockquote id="b53-7">“[T]he evidence needed to make the inquiry is not of the same degree of conclusiveness as that required for an arrest. The stopping of the individual to inquire is not an arrest and the ground upon which the police may make the inquiry may be less incriminating than the ground for an arrest for a crime known to have been committed. . . .</blockquote>
<blockquote id="b53-8">“And as the right to stop and inquire is to be justified for a cause less conclusive than that which would sustain an arrest, so the right to frisk may be justified as an incident to inquiry upon grounds of elemental safety and precaution which might not initially sustain a search. Ultimately the validity of the frisk narrows down to whether there is or is not a right by the police to touch the person questioned. The sense of exterior touch here involved is not very far different from the sense of sight or hearing — senses upon which police customarily act.” <em>People </em>v. <em>Rivera, </em>14 N. Y. 2d 441, 445, 447, <span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/#34" aria-description="Citation for case: People v. Rivera">201 N. E. 2d 32, 34, 35</a></span>, 252 N. Y. S. 2d 458, 461, 463 (1964), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./379/978/">379 U. S. 978</a></span> (1965).</blockquote>
</footnote>
<footnote label="6">
<p id="b53-9"> See, <em>e. g., </em>Foote, The Fourth Amendment: Obstacle or Necessity in the Law of Arrest?, 51 J. Crim. L. C. &amp; P. S. 402 (1960).</p>
</footnote>
<footnote label="7">
<p id="b54-7"> See n. 11, <em>infra.</em></p>
</footnote>
<footnote label="8">
<p id="b54-8"><em> </em>Brief for Respondent 2.</p>
</footnote>
<footnote label="9">
<p id="b55-6"> See L. Tiffany, D. McIntyre <em>&amp; </em>D. Rotenberg, Detection of Crime: Stopping and Questioning, Search and Seizure, Encouragement and Entrapment 18-56 (1967). This sort of police conduct may, for example, be designed simply to help an intoxicated person find his way home, with no intention of arresting him unless he becomes obstreperous. Or the police may be seeking to mediate a domestic <page-number citation-index="1" label="14">*14</page-number>quarrel which threatens to erupt into violence. They may accost a woman in an area known for prostitution as part of a harassment campaign designed to drive prostitutes away without the considerable difficulty involved in prosecuting them. Or they may be conducting a dragnet search of all teenagers in a particular section of the city for weapons because they have heard rumors of an impending gang fight.</p>
</footnote>
<footnote label="10">
<p id="b56-8"> See Tiffany, McIntyre &amp; Rotenberg, <em>supra, </em>n. 9, at 100-101; Comment, <span class="citation no-link">47 Nw. U. L. Rev. 493</span>, 497-499 (1952).</p>
</footnote>
<footnote label="11">
<p id="b56-9"> The President’s Commission on Law Enforcement and Administration of Justice found that “[i]n many communities, field interrogations are a major source of friction between the police and minority groups.” President’s Commission on Law Enforcement and Administration of Justice, Task Force Report: The Police 183 (1967). It was reported that the friction caused by “[mjisuse of field interrogations” increases “as more police departments adopt ‘aggressive patrol’ in which officers are encouraged routinely to stop and question persons on the street who are unknown to them, who are suspicious, or whose purpose for being abroad is not readily evident.” <em>Id., </em>at 184. While the frequency with which “frisking” forms a part of field interrogation practice varies tremendously with the locale, the objective of the interrogation, and the particular officer, see Tiffany, McIntyre &amp; Rotenberg, <em>supra, </em>n. 9, at 47-48, it cannot help but be a severely exacerbating factor in police-community ten<page-number citation-index="1" label="15">*15</page-number>sions. This is particularly true in situations where the “stop and frisk” of youths or minority group members is “motivated by the officers’ perceived need to maintain the power image of the beat officer, an aim sometimes accomplished by humiliating anyone who attempts to undermine police control of the streets.” <em>Ibid.</em></p>
</footnote>
<footnote label="12">
<p id="b58-8"> In this case, for example, the Ohio Court of Appeals stated that “we must be careful to distinguish that the ‘frisk’ authorized herein includes only a ‘frisk’ for a dangerous weapon. It by no means authorizes a search for contraband, evidentiary material, or anything else in the absence of reasonable grounds to arrest. Such a search is controlled by the requirements of the Fourth Amendment, and probable cause is essential.” <em>State </em>v. <em>Terry, </em><span class="citation" data-id="3704293"><a href="/opinion/3954963/state-v-terry/#130" aria-description="Citation for case: State v. Terry">5 Ohio App. 2d 122, 130</a></span>, <span class="citation" data-id="3704293"><a href="/opinion/3954963/state-v-terry/#120" aria-description="Citation for case: State v. Terry">214 N. E. 2d 114, 120</a></span> (1966). See also, <em>e. g., Ellis </em>v. <em>United States, </em>105 U. S. App. D. C. <span class="citation" data-id="9446660"><a href="/opinion/247468/edward-j-ellis-v-united-states/#374" aria-description="Citation for case: Edward J. Ellis v. United States"><em>86, 88, 264 F. 2d </em>372, 374</a></span> (1959); Comment, 65 Col. L. Rev. 848, 860, and n. 81 (1965).</p>
</footnote>
<footnote label="13">
<p id="b59-6"> Consider the following apt description:</p>
<blockquote id="b59-7">“[T]he officer must feel with sensitive fingers every portion of the prisoner’s body. A thorough search must be made of the prisoner’s arms and armpits, waistline and .back, the groin and area about the testicles, and entire surface of the legs down to the feet.” Priar &amp; Martin, Searching and Disarming Criminals, 45 J. Crim. L. C. &amp; P. S. 481 (1954).</blockquote>
</footnote>
<footnote label="14">
<p id="b59-8"> See n. 11, <em>supra, </em>and accompanying text.</p>
<p id="b59-9">We have noted that the abusive practices which play a major, though by no means exclusive, role in creating this friction are not susceptible of control by means of the exclusionary rule, and cannot properly dictate our decision with respect to the powers of the police in genuine investigative and preventive situations. However, the degree of community resentment aroused by particular practices is clearly relevant to an assessment of the quality of the intrusion upon reasonable expectations of personal security caused by those practices.</p>
</footnote>
<footnote label="15">
<p id="b59-10"> These dangers are illustrated in part by the course of adjudication in the Court of Appeals of New York. Although its first decision in this area, <em>People </em>v. <em>Rivera, </em>14 N. Y. 2d 441, <span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/" aria-description="Citation for case: People v. Rivera">201 N. E. 2d 32</a></span>, 252 N. Y. S. 2d 458 (1964), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./379/978/">379 U. S. 978</a></span> (1965), rested squarely on the notion that a “frisk” was not a “search,” see nn. 3-5, <em>supra, </em>it was compelled to recognize in <em>People </em>v. <em>Taggart, </em><page-number citation-index="1" label="18">*18</page-number>20 N. Y. 2d 335, 342, <span class="citation" data-id="5523803"><a href="/opinion/5676096/people-v-taggart/#586" aria-description="Citation for case: People v. Taggart">229 N. E. 2d 581, 586</a></span>, 283 N. Y. S. 2d 1, 8 (1967), that what it had actually authorized in <em><span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/" aria-description="Citation for case: People v. Rivera">Rivera</a></span> </em>and subsequent decisions, see, e. <em>g., People </em>v. <em>Pugach, </em>15 N. Y. 2d 65, <span class="citation" data-id="5521569"><a href="/opinion/5674047/people-v-pugach/" aria-description="Citation for case: People v. Pugach">204 N. E. 2d 176</a></span>, 255 N. Y. S. 2d 833 (1964), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./380/936/">380 U. S. 936</a></span> (1965), was a "search” upon less than probable cause. However, in acknowledging that no valid distinction could be maintained on the basis of its cases, the Court of Appeals continued to distinguish between the two in theory. It still defined “search” as it had in <em><span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/" aria-description="Citation for case: People v. Rivera">Rivera</a></span> </em>— as an essentially unlimited examination of the person for any and all seizable items — and merely noted that the cases had upheld police intrusions which went far beyond the original limited conception of a “frisk.” Thus, principally because it failed to consider limitations upon the scope of searches in individual cases as a potential mode of regulation, the Court of Appeals in three short years arrived at the position that the Constitution must, in the name of necessity, be held to permit unrestrained rummaging about a person and his effects upon mere suspicion. It did apparently limit its holding to “cases involving serious personal injury or grave irreparable property damage,” thus excluding those involving “the enforcement of sumptuary laws, such as gambling, and laws of limited public consequence, such as narcotics violations, prostitution, larcenies of the ordinary kind, and the like.” <em>People </em>v. <span class="citation" data-id="5523803"><a href="/opinion/5676096/people-v-taggart/#340" aria-description="Citation for case: People v. Taggart"><em>Taggart, supra, </em>at 340</a></span>, <span class="citation" data-id="3704293"><a href="/opinion/3954963/state-v-terry/#584" aria-description="Citation for case: State v. Terry">214 N. E. 2d, at 584</a></span>, 283 N. Y. S. 2d, at 6.</p>
<p id="AI">In our view the sounder course is to recognize that the Eourth Amendment governs all intrusions by agents of the public upon personal security, and to make the scope of the particular intrusion, in light of all the exigencies of the case, a central element in the analysis of reasonableness. Cf. <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#183" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 183</a></span> (1949) (Mr. Justice Jackson, dissenting). Compare <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#537" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 537</a></span> (1967). This seems preferable to an approach which attributes too much significance to an overly technical definition of “search,” and which turns in part upon a judge-made hierarchy of legislative enactments in the criminal sphere. Focusing the inquiry squarely on the dangers and demands of the particular situation also seems more likely to produce rules which are intelligible to the police and the public alike than requiring the officer in the heat of an unfolding encounter on the street to make a judgment as to which laws are "of limited public consequence.”</p>
</footnote>
<footnote label="16">
<p id="b61-7"> We thus decide nothing today concerning the constitutional propriety of an investigative “seizure” upon less than probable cause for purposes of “detention” and/or interrogation. Obviously, not all personal intercourse between policemen and citizens involves “seizures” of persons. Only when the officer, by means of physical force or show of authority, has in some way restrained the liberty of a citizen may we conclude that a “seizure” has occurred. We cannot tell with any certainty upon this record whether any such “seizure” took place here prior to Officer McPadden’s initiation of physical contact for purposes of searching Terry for weapons, and we thus may assume that up to that point no intrusion upon constitutionally protected rights had occurred.</p>
</footnote>
<footnote label="17">
<p id="b62-7"> See generally Leagre, The Fourth Amendment and the Law of Arrest, 54 J. Crim. L. C. &amp; P. S. 393, 396-403 (1963).</p>
</footnote>
<footnote label="18">
<p id="b63-5"> This demand for specificity in the information upon which police action is predicated is the central teaching of this Court’s Fourth Amendment jurisprudence. See <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 96-97</a></span> (1964); <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#34" aria-description="Citation for case: Ker v. California">374 U. S. 23, 34-37</a></span> (1963); <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#479" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 479-484</a></span> (1963); <em>Rios </em>v. <em>United States, </em><span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/#261" aria-description="Citation for case: Rios v. United States">364 U. S. 253, 261-262</a></span> (1960); <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#100" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 100-102</a></span> (1959); <em>Draper </em>v. <em>United States, </em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#312" aria-description="Citation for case: Draper v. United States">358 U. S. 307, 312-314</a></span> (1959); <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175-178</a></span> (1949); <em>Johnson v. United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#15" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 15-17</a></span> (1948); <em>United States </em>v. <em>Di Re, </em><span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#593" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 593-595</a></span> (1948); <em>Husty </em>v. <em>United States, </em><span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/#700" aria-description="Citation for case: Husty v. United States">282 U. S. 694, 700-701</a></span> (1931); <em>Dumbra </em>v. <em>United States, </em><span class="citation" data-id="100685"><a href="/opinion/100685/dumbra-v-united-states/#441" aria-description="Citation for case: Dumbra v. United States">268 U. S. 435, 441</a></span> (1925); <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#159" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 159-162</a></span> (1925); <em>Stacey </em>v. <em>Emery, </em><span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/#645" aria-description="Citation for case: Stacey v. Emery">97 U. S. 642, 645</a></span> (1878).</p>
</footnote>
<footnote label="19">
<p id="b63-6"> See, e. <em>g., Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#354" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 354-357</a></span> (1967) ; <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#54" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 54-60</a></span> (1967); <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-15</a></span> (1948); cf. <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#479" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 479-480</a></span> (1963). See also <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#110" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108, 110-115</a></span> (1964).</p>
</footnote>
<footnote label="20">
<p id="b64-6"> See also cases cited in n. 18, <em>supra.</em></p>
</footnote>
<footnote label="21">
<p id="b66-8"> Fifty-seven law enforcement officers were killed in the line of duty in this country in 1966, bringing the total to 335 for the seven-year period beginning with 1960. Also in 1966, there were 23,851 assaults on police officers, 9,113 of which resulted in injuries to the policemen. Fifty-five of the 57 officers killed in 1966 died from gunshot wounds, 41 of them inflicted by handguns easily secreted about the person. The remaining two murders were perpetrated by knives. See Federal Bureau of Investigation, Uniform Crime Reports for the United States — 1966, at 45-48, 152 and Table 51.</p>
<p id="b66-9">The easy availability of firearms to potential criminals in this country is well known and has provoked much debate. See, <em>e. g., </em>President’s Commission on Law Enforcement and Administration of Justice, The Challenge of Crime in a Free Society 239-243 (1967). Whatever the merits of gun-control proposals, this fact is relevant to an assessment of the need for some form of self-protective search power.</p>
</footnote>
<footnote label="22">
<p id="b68-7"> See generally <em>W. </em>LaFave, Arrest — The Decision to Take a Suspect into Custody 1-13 (1965).</p>
</footnote>
<footnote label="23">
<p id="b69-8"> See also cases cited in n. 18, <em>supra.</em></p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Timbs v. Indiana.md  (`case`, 5 assertions)

### content_page

```
---
title: Timbs v. Indiana
type: case
citation: "586 U.S. 146 (2019)"
parallel_cite: "139 S. Ct. 682; 203 L. Ed. 2d 11"
neutral_cite: 2019 U.S. LEXIS 1350
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2019
date_decided: 2019-02-20
docket: No. 17-1091
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
  opinion_url: "https://www.courtlistener.com/opinion/4591916/timbs-v-indiana/"
  cluster_id: 4591916
  opinion_id: 9888039
  identity_checked: true
lake:
  record_id: Timbs v. Indiana
  status: under_review
  projected_at: 2026-07-09
homes:
  - page: "[[Civil Asset Forfeiture]]"
    role: Anchor
related:
  - "[[Civil Asset Forfeiture]]"
  - "[[Austin v. United States]]"
  - "[[United States v. Bajakajian]]"
tags:
  - case
  - eighth-amendment
  - excessive-fines
  - civil-forfeiture
  - incorporation
  - fourteenth-amendment
  - in-rem
holding: "The Eighth Amendment's Excessive Fines Clause is an incorporated protection applicable to the States under the Fourteenth Amendment's Due Process Clause; the safeguard against excessive fines is fundamental to our scheme of ordered liberty and deeply rooted in this Nation's history and tradition, and it reaches civil in rem forfeitures that are at least partly punitive."
aliases:
  - Timbs v. Indiana
  - "Timbs v. Indiana (2019)"
---

# Timbs v. Indiana

*586 U.S. 146 (2019)* (No. 17-1091) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4591916 → majority opinion 9888039 (Ginsburg, J., for a unanimous Court; 586 U.S. 146 / 139 S. Ct. 682, argued Nov. 28, 2018, decided Feb. 20, 2019). Rule quote string-matched to the CL opinion text 2026-07-07; the CL text is paginated to the West S. Ct. reporter (parallel cite), so the pin is `139 S. Ct. at 687` (page-label `*687`) — the official U.S. Reports pagination is not present in the CL text. S9 promotes. -->

## Background
Tyson Timbs pleaded guilty in Indiana state court to dealing in a controlled substance and conspiracy to commit theft. He was sentenced to home detention and probation and ordered to pay roughly $1,203 in fees and costs; the maximum monetary fine for his drug offense was $10,000. When he was arrested, police seized his Land Rover SUV, which he had bought for about $42,000 using money from a life-insurance policy paid on his father's death. The State engaged a private law firm to bring a civil *in rem* forfeiture action against the vehicle. The trial court denied forfeiture as grossly disproportionate to the gravity of the offense — the vehicle was worth more than four times the maximum fine — and the Court of Appeals of Indiana affirmed, but the Indiana Supreme Court reversed, holding that the Excessive Fines Clause constrains only the Federal Government and does not apply to the States.

## Issue
Whether the Eighth Amendment's Excessive Fines Clause is an "incorporated" protection applicable to the States under the Fourteenth Amendment's Due Process Clause.

## Rule
The Court applied its settled incorporation framework: a Bill of Rights guarantee binds the States if it is "fundamental to our scheme of ordered liberty" or "deeply rooted in this Nation's history and tradition." The protection against excessive fines is both — it has a lineage from Magna Carta through the English Bill of Rights to the founding, and it guards against the government's temptation to use fines to raise revenue, chill opponents, and pursue vindictive ends. On that basis the Court held: "The Excessive Fines Clause is therefore incorporated by the Due Process Clause of the Fourteenth Amendment." — 139 S. Ct. at 687. ^pin-687

## Application
Indiana's argument that the Clause does not reach civil *in rem* forfeitures did not change the incorporation analysis. Whether or not the *application* of the Clause to a particular class of forfeitures is itself deeply rooted, the *right* the Clause secures is incorporated; the scope question is distinct from the threshold question of whether the guarantee binds the States at all. Because the Excessive Fines Clause applies to Indiana, the Indiana Supreme Court's contrary premise could not stand, and the excessiveness of this forfeiture remained to be resolved below.

## Conclusion
The judgment of the Indiana Supreme Court was **[[Reading and Citing Cases#vacated|vacated]]** and the case [[Reading and Citing Cases#on-remand|remanded]]. Ginsburg, J., delivered the opinion of a unanimous Court. Gorsuch, J., concurred; Thomas, J., concurred in the judgment (arguing the right is better secured through the Fourteenth Amendment's Privileges or Immunities Clause).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Timbs* completes the Excessive Fines line for state and local forfeitures: *[[Austin v. United States]]* (1993) held that punitive civil forfeitures are subject to the Clause, *[[United States v. Bajakajian]]* (1998) supplied the "grossly disproportional" excessiveness standard, and *Timbs* makes the Clause enforceable against the States. Teach it as the doctrine's reach — the guarantee that a state or municipal forfeiture, not just a federal one, can be challenged as an excessive fine.

## Appears on
- [[Civil Asset Forfeiture]] — *Anchor*

## Sources
- [*Timbs v. Indiana*, 586 U.S. 146 (2019)](https://www.courtlistener.com/opinion/4591916/timbs-v-indiana/) — pinpoint: 139 S. Ct. at 687 (Ginsburg, J., for a unanimous Court; the CL opinion text is paginated to the West S. Ct. reporter and carries the page-label `*687` in the paragraph stating the incorporation holding). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ec122108034d79a4", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "586 U.S. 146 (2019)", "court": "U.S. Supreme Court", "neutral_cite": "2019 U.S. LEXIS 1350", "official_citation_present": true, "parallel_cite": "139 S. Ct. 682; 203 L. Ed. 2d 11", "title": "Timbs v. Indiana", "year": "2019"}}
{"assertion_id": "928f11b75f0fba63", "dimension": "support", "kind": "home_role", "locator": {"home": "Civil Asset Forfeiture"}, "payload": {"home": "Civil Asset Forfeiture", "role": "Anchor", "title": "Timbs v. Indiana"}}
{"assertion_id": "cc70452449f30cc5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Eighth Amendment's Excessive Fines Clause is an incorporated protection applicable to the States under the Fourteenth Amendment's Due Process Clause; the safeguard against excessive fines is fundamental to our scheme of ordered liberty and deeply rooted in this Nation's history and tradition, and it reaches civil in rem forfeitures that are at least partly punitive.", "title": "Timbs v. Indiana"}}
{"assertion_id": "5f771e0f88bf98aa", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Timbs v. Indiana", "varies_by_point": "false"}}
{"assertion_id": "d4aab473a6333963", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Timbs v. Indiana"}}
```

### lake record — Timbs v. Indiana

```json
{
  "schema_version": "s2.v1",
  "record_id": "Timbs v. Indiana",
  "status": "under_review",
  "identity": {
    "case_name": "Timbs v. Indiana",
    "case_name_short": "Timbs",
    "case_name_full": "Tyson TIMBS, Petitioner v. INDIANA",
    "input_case_name": "Timbs v. Indiana",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2019-02-20",
    "year": 2019,
    "docket": "No. 17-1091",
    "cluster_id": 4591916,
    "lead_opinion_id": 9888039,
    "sibling_ids": [],
    "absolute_url": "/opinion/4591916/timbs-v-indiana/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "586 U.S. 146",
      "volume": "586",
      "reporter": "U.S.",
      "page": "146",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "139 S. Ct. 682",
        "volume": "139",
        "reporter": "S. Ct.",
        "page": "682",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "203 L. Ed. 2d 11",
        "volume": "203",
        "reporter": "L. Ed. 2d",
        "page": "11",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2019 U.S. LEXIS 1350",
        "volume": "2019",
        "reporter": "U.S. LEXIS",
        "page": "1350",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "586 U.S. 146",
        "volume": "586",
        "reporter": "U.S.",
        "page": "146",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "139 S. Ct. 682",
        "volume": "139",
        "reporter": "S. Ct.",
        "page": "682",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2019 U.S. LEXIS 1350",
        "volume": "2019",
        "reporter": "U.S. LEXIS",
        "page": "1350",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "203 L. Ed. 2d 11",
        "volume": "203",
        "reporter": "L. Ed. 2d",
        "page": "11",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "586 U.S. 146",
    "official_selection": {
      "court_class": "scotus",
      "selected": "586 U.S. 146",
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
    "date_created": "2026-07-06T13:41:50Z",
    "date_modified": "2026-07-09T23:29:56Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:41:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:41:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "timbs-v-indiana--4591916",
      "to_record_id": "Timbs v. Indiana",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Timbs v. Indiana

```
<opinion type="majority">
<author id="p-9">Justice GINSBURG delivered the opinion of the Court.</author>
<p id="p-10"><a class="page-label" data-citation-index="1" data-label="686" href="#p686" id="p686">*686</a>Tyson Timbs pleaded guilty in Indiana state court to dealing in a controlled substance and conspiracy to commit theft. The trial court sentenced him to one year of home detention and five years of probation, which included a court-supervised addiction-treatment program. The sentence also required Timbs to pay fees and costs totaling $ 1,203. At the time of Timbs's arrest, the police seized his vehicle, a Land Rover SUV Timbs had purchased for about $ 42,000. Timbs paid for the vehicle with money he received from an insurance policy when his father died.</p>
<p id="p-11">The State engaged a private law firm to bring a civil suit for forfeiture of Timbs's Land Rover, charging that the vehicle had been used to transport heroin. After Timbs's guilty plea in the criminal case, the trial court held a hearing on the forfeiture demand. Although finding that Timbs's vehicle had been used to facilitate violation of a criminal statute, the court denied the requested forfeiture, observing that Timbs had recently purchased the vehicle for $ 42,000, more than four times the maximum $ 10,000 monetary fine assessable against him for his drug conviction. Forfeiture of the Land Rover, the court determined, would be grossly disproportionate to the gravity of Timbs's offense, hence unconstitutional under the Eighth Amendment's Excessive Fines Clause. The Court of Appeals of Indiana affirmed that determination, but the Indiana Supreme Court reversed. <extracted-citation case-ids="12331536" index="0" url="https://cite.case.law/ne3d/84/1179/"><span class="citation" data-id="4217247"><a href="/opinion/4439994/state-of-indiana-v-tyson-timbs/" aria-description="Citation for case: State of Indiana v. Tyson Timbs">84 N.E.3d 1179</a></span></extracted-citation> (2017). The Indiana Supreme Court did not decide whether the forfeiture would be excessive. Instead, it held that the Excessive Fines Clause constrains only federal action and is inapplicable to state impositions. We granted certiorari. 585 U.S. ----, <extracted-citation case-ids="12613687,12613688,12613689,12613690,12613691,12613692" index="1" url="https://cite.case.law/s-ct/138/2650/"><span class="citation multiple-matches"><a href="/c/S.Ct./138/2650/">138 S.Ct. 2650</a></span></extracted-citation>, <extracted-citation index="2" url="https://cite.case.law/citations/?q=201%20L.%20Ed.%202d%201049"><span class="citation no-link">201 L.Ed.2d 1049</span></extracted-citation> (2018).</p>
<p id="p-12">The question presented: Is the Eighth Amendment's Excessive Fines Clause an "incorporated" protection applicable to the States under the Fourteenth Amendment's Due Process Clause? Like the Eighth Amendment's proscriptions of "cruel and unusual punishment" and "[e]xcessive bail," the protection against excessive fines guards against abuses of government's punitive or criminal-law-enforcement authority. This safeguard, we hold, is "fundamental to our scheme of ordered liberty," with "dee[p] root[s] in <a class="page-label" data-citation-index="1" data-label="687" href="#p687" id="p687">*687</a>[our] history and tradition." <em>McDonald</em> v. <em>Chicago</em> , <extracted-citation case-ids="12455289,3644508" index="3" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">561 U.S. 742</a></span></extracted-citation>, 767, <extracted-citation case-ids="12455289,3644508" index="4" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">130 S.Ct. 3020</a></span></extracted-citation>, <extracted-citation case-ids="12455289,3644508" index="5" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">177 L.Ed.2d 894</a></span></extracted-citation> (2010) (internal quotation marks omitted; emphasis deleted). The Excessive Fines Clause is therefore incorporated by the Due Process Clause of the Fourteenth Amendment.</p>
<p id="p-13">I</p>
<p id="p-14">A</p>
<p id="p-15">When ratified in 1791, the Bill of Rights applied only to the Federal Government. <em>Barron ex rel. Tiernan</em> v<em>. Mayor of Baltimore</em> , <extracted-citation case-ids="1436167" index="6" url="https://cite.case.law/us/32/243/"><span class="citation" data-id="85827"><a href="/opinion/85827/barron-ex-rel-tiernan-v-mayor-of-baltimore/" aria-description="Citation for case: Barron Ex Rel. Tiernan v. Mayor of Baltimore">7 Pet. 243</a></span></extracted-citation>, <extracted-citation case-ids="1436167" index="7" url="https://cite.case.law/us/32/243/"><span class="citation" data-id="85827"><a href="/opinion/85827/barron-ex-rel-tiernan-v-mayor-of-baltimore/" aria-description="Citation for case: Barron Ex Rel. Tiernan v. Mayor of Baltimore">8 L.Ed. 672</a></span></extracted-citation> (1833). "The constitutional Amendments adopted in the aftermath of the Civil War," however, "fundamentally altered our country's federal system." <em>McDonald</em> , <extracted-citation case-ids="12455289,3644508" index="8" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">561 U.S., at 754</a></span></extracted-citation>, <extracted-citation case-ids="12455289,3644508" index="9" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">130 S.Ct. 3020</a></span></extracted-citation>. With only "a handful" of exceptions, this Court has held that the Fourteenth Amendment's Due Process Clause incorporates the protections contained in the Bill of Rights, rendering them applicable to the States. <em><extracted-citation case-ids="12455289,3644508" index="10" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">Id.</a></span></extracted-citation></em> , at 764-765, and nn. 12-13, <extracted-citation case-ids="12455289,3644508" index="11" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">130 S.Ct. 3020</a></span></extracted-citation>. A Bill of Rights protection is incorporated, we have explained, if it is "fundamental to our scheme of ordered liberty," or "deeply rooted in this Nation's history and tradition." <em><extracted-citation case-ids="12455289,3644508" index="12" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="12455289,3644508" index="12" url="https://cite.case.law/us/561/742/"> at 767</extracted-citation>, <extracted-citation case-ids="12455289,3644508" index="13" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">130 S.Ct. 3020</a></span></extracted-citation> (internal quotation marks omitted; emphasis deleted).</p>
<p id="p-16">Incorporated Bill of Rights guarantees are "enforced against the States under the Fourteenth Amendment according to the same standards that protect those personal rights against federal encroachment." <em><extracted-citation case-ids="12455289,3644508" index="14" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="12455289,3644508" index="14" url="https://cite.case.law/us/561/742/"> at 765</extracted-citation>, <extracted-citation case-ids="12455289,3644508" index="15" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">130 S.Ct. 3020</a></span></extracted-citation> (internal quotation marks omitted). Thus, if a Bill of Rights protection is incorporated, there is no daylight between the federal and state conduct it prohibits or requires.<footnotemark>1</footnotemark></p>
<p id="p-17">B</p>
<p id="p-18">Under the Eighth Amendment, "[e]xcessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted." Taken together, these Clauses place "parallel limitations" on "the power of those entrusted with the criminal-law function of government." <em>Browning-Ferris Industries of Vt., Inc.</em> v. <em>Kelco Disposal, Inc.</em> , <extracted-citation case-ids="6214309" index="16" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U.S. 257</a></span></extracted-citation>, 263, <extracted-citation case-ids="6214309" index="17" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">109 S.Ct. 2909</a></span></extracted-citation>, <extracted-citation case-ids="6214309" index="18" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">106 L.Ed.2d 219</a></span></extracted-citation> (1989) (quoting <em>Ingraham</em> v. <em>Wright</em> , <extracted-citation case-ids="12126861" index="19" url="https://cite.case.law/us/430/651/#p664"><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">430 U.S. 651</a></span></extracted-citation>, 664, <extracted-citation case-ids="12126861" index="20" url="https://cite.case.law/us/430/651/#p664"><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">97 S.Ct. 1401</a></span></extracted-citation>, <extracted-citation case-ids="12126861" index="21" url="https://cite.case.law/us/430/651/#p664"><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">51 L.Ed.2d 711</a></span></extracted-citation> (1977) ). Directly at issue here is the phrase "nor excessive fines imposed," which "limits the government's power to extract payments, whether in cash or in kind, 'as punishment for some offense.' " <em>United States</em> v<em>. Bajakajian</em> , <extracted-citation case-ids="11182447" index="22" url="https://cite.case.law/us/524/321/#p327"><span class="citation" data-id="9433683"><a href="/opinion/118234/united-states-v-bajakajian/" aria-description="Citation for case: United States v. Bajakajian">524 U.S. 321</a></span></extracted-citation>, 327-328, <extracted-citation case-ids="11182447" index="23" url="https://cite.case.law/us/524/321/#p327"><span class="citation" data-id="9433683"><a href="/opinion/118234/united-states-v-bajakajian/" aria-description="Citation for case: United States v. Bajakajian">118 S.Ct. 2028</a></span></extracted-citation>, <extracted-citation case-ids="11182447" index="24" url="https://cite.case.law/us/524/321/#p327"><span class="citation" data-id="9433683"><a href="/opinion/118234/united-states-v-bajakajian/" aria-description="Citation for case: United States v. Bajakajian">141 L.Ed.2d 314</a></span></extracted-citation> (1998) (quoting <em>Austin</em> v. <em>United States</em> , <extracted-citation case-ids="355668" index="25" url="https://cite.case.law/us/509/602/#p609"><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">509 U.S. 602</a></span></extracted-citation>, 609-610, <extracted-citation case-ids="355668" index="26" url="https://cite.case.law/us/509/602/#p609"><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">113 S.Ct. 2801</a></span></extracted-citation>, <extracted-citation case-ids="355668" index="27" url="https://cite.case.law/us/509/602/#p609"><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">125 L.Ed.2d 488</a></span></extracted-citation> (1993) ). The Fourteenth Amendment, we hold, incorporates this protection.</p>
<p id="p-19">The Excessive Fines Clause traces its venerable lineage back to at least 1215, when Magna Carta guaranteed that "[a] Free-man shall not be amerced for a small fault, but after the manner of the fault; and for a great fault after the greatness thereof, saving to him his contenement ...." § 20, 9 Hen. III, ch. 14, in 1 Eng.</p>
<p id="p-20"><a class="page-label" data-citation-index="1" data-label="688" href="#p688" id="p688">*688</a>Stat. at Large 5 (1225).<footnotemark>2</footnotemark> As relevant here, Magna Carta required that economic sanctions "be proportioned to the wrong" and "not be so large as to deprive [an offender] of his livelihood." <em>Browning-Ferris</em> , <extracted-citation case-ids="6214309" index="28" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U.S., at 271</a></span></extracted-citation>, <extracted-citation case-ids="6214309" index="29" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">109 S.Ct. 2909</a></span></extracted-citation>. See also 4 W. Blackstone, Commentaries on the Laws of England 372 (1769) ("[N]o man shall have a larger amercement imposed upon him, than his circumstances or personal estate will bear ...."). But cf. <em>Bajakajian</em> , <extracted-citation case-ids="11182447" index="30" url="https://cite.case.law/us/524/321/#p327"><span class="citation" data-id="9433683"><a href="/opinion/118234/united-states-v-bajakajian/#340" aria-description="Citation for case: United States v. Bajakajian">524 U.S., at 340</a></span>, n. 15</extracted-citation>, <extracted-citation case-ids="11182447" index="31" url="https://cite.case.law/us/524/321/#p327"><span class="citation" data-id="9433683"><a href="/opinion/118234/united-states-v-bajakajian/" aria-description="Citation for case: United States v. Bajakajian">118 S.Ct. 2028</a></span></extracted-citation> (taking no position on the question whether a person's income and wealth are relevant considerations in judging the excessiveness of a fine).</p>
<p id="p-21">Despite Magna Carta, imposition of excessive fines persisted. The 17th century Stuart kings, in particular, were criticized for using large fines to raise revenue, harass their political foes, and indefinitely detain those unable to pay. <em>E.g.</em> , The Grand Remonstrance ¶¶17, 34 (1641), in The Constitutional Documents of the Puritan Revolution 1625-1660, pp. 210, 212 (S. Gardiner ed., 3d ed. rev. 1906); <em>Browning-Ferris</em> , <extracted-citation case-ids="6214309" index="32" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U.S., at 267</a></span></extracted-citation>, <extracted-citation case-ids="6214309" index="33" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">109 S.Ct. 2909</a></span></extracted-citation>. When James II was overthrown in the Glorious Revolution, the attendant English Bill of Rights reaffirmed Magna Carta's guarantee by providing that "excessive Bail ought not to be required, nor excessive Fines imposed; nor cruel and unusual Punishments inflicted." 1 Wm. &amp; Mary, ch. 2, § 10, in 3 Eng. Stat. at Large 441 (1689).</p>
<p id="p-22">Across the Atlantic, this familiar language was adopted almost verbatim, first in the Virginia Declaration of Rights, then in the Eighth Amendment, which states: "Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted."</p>
<p id="p-23">Adoption of the Excessive Fines Clause was in tune not only with English law; the Clause resonated as well with similar colonial-era provisions. See, <em>e.g.</em> , Pa. Frame of Govt., Laws Agreed Upon in England, Art. XVIII (1682), in 5 Federal and State Constitutions 3061 (F. Thorpe ed. 1909) ("[A]ll fines shall be moderate, and saving men's contenements, merchandize, or wainage."). In 1787, the constitutions of eight States-accounting for 70% of the U.S. population-forbade excessive fines. Calabresi, Agudo, &amp; Dore, State Bills of Rights in 1787 and 1791, <extracted-citation index="34" url="https://cite.case.law/citations/?q=85%20S.%20Cal.%20L.%20Rev.%201451"><span class="citation no-link">85 S. Cal. L. Rev. 1451</span></extracted-citation>, 1517 (2012).</p>
<p id="p-24">An even broader consensus obtained in 1868 upon ratification of the Fourteenth Amendment. By then, the constitutions of 35 of the 37 States-accounting for over 90% of the U.S. population-expressly prohibited excessive fines. Calabresi &amp; Agudo, Individual Rights Under State Constitutions When the Fourteenth Amendment Was Ratified in 1868, <extracted-citation index="35" url="https://cite.case.law/citations/?q=87%20Tex.%20L.%20Rev.%207">87 Texas L. Rev. 7</extracted-citation>, 82 (2008).</p>
<p id="p-25">Notwithstanding the States' apparent agreement that the right guaranteed by the Excessive Fines Clause was fundamental, abuses continued. Following the Civil War, Southern States enacted Black Codes to subjugate newly freed slaves and maintain the prewar racial hierarchy. Among these laws' provisions were draconian fines for violating broad proscriptions on "vagrancy" and other dubious offenses. See, <em>e.g.</em> , Mississippi Vagrant Law, Laws of Miss. § 2 (1865), in 1 W. Fleming, Documentary <a class="page-label" data-citation-index="1" data-label="689" href="#p689" id="p689">*689</a>History of Reconstruction 283-285 (1950). When newly freed slaves were unable to pay imposed fines, States often demanded involuntary labor instead. <em>E.g.</em> , <em><extracted-citation index="36" url="https://cite.case.law/citations/?q=87%20Tex.%20L.%20Rev.%207">id.</extracted-citation></em> § 5; see Finkelman, John Bingham and the Background to the Fourteenth Amendment, <extracted-citation index="37" url="https://cite.case.law/citations/?q=36%20Akron%20L.%20Rev.%20671">36 Akron L. Rev 671</extracted-citation>, 681-685 (2003) (describing Black Codes' use of fines and other methods to "replicate, as much as possible, a system of involuntary servitude"). Congressional debates over the Civil Rights Act of 1866, the joint resolution that became the Fourteenth Amendment, and similar measures repeatedly mentioned the use of fines to coerce involuntary labor. See, <em>e.g.</em> , Cong. Globe, 39th Cong., 1st Sess., 443 (1866); <em>id.,</em> at 1123-1124.</p>
<p id="p-26">Today, acknowledgment of the right's fundamental nature remains widespread. As Indiana itself reports, all 50 States have a constitutional provision prohibiting the imposition of excessive fines either directly or by requiring proportionality. Brief in Opposition 8-9. Indeed, Indiana explains that its own Supreme Court has held that the Indiana Constitution should be interpreted to impose the same restrictions as the Eighth Amendment. <em>Id.</em> , at 9 (citing <em>Norris</em> v. <em>State</em> , <extracted-citation case-ids="1823589" index="38" url="https://cite.case.law/ind/271/568/#p576"><span class="citation" data-id="2045779"><a href="/opinion/2045779/norris-v-state/" aria-description="Citation for case: Norris v. State">271 Ind. 568</a></span></extracted-citation>, 576, <extracted-citation case-ids="11067811" index="39" url="https://cite.case.law/ne2d/394/144/#p150"><span class="citation" data-id="2045779"><a href="/opinion/2045779/norris-v-state/" aria-description="Citation for case: Norris v. State">394 N.E.2d 144</a></span></extracted-citation>, 150 (1979) ).</p>
<p id="p-27">For good reason, the protection against excessive fines has been a constant shield throughout Anglo-American history: Exorbitant tolls undermine other constitutional liberties. Excessive fines can be used, for example, to retaliate against or chill the speech of political enemies, as the Stuarts' critics learned several centuries ago. See <em>Browning-Ferris</em> , <extracted-citation case-ids="6214309" index="40" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U.S., at 267</a></span></extracted-citation>, <extracted-citation case-ids="6214309" index="41" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">109 S.Ct. 2909</a></span></extracted-citation>. Even absent a political motive, fines may be employed "in a measure out of accord with the penal goals of retribution and deterrence," for "fines are a source of revenue," while other forms of punishment "cost a State money." <em>Harmelin</em> v. <em>Michigan</em> , <extracted-citation case-ids="1107767" index="42" url="https://cite.case.law/us/501/957/#p979"><span class="citation" data-id="9432400"><a href="/opinion/112646/harmelin-v-michigan/" aria-description="Citation for case: Harmelin v. Michigan">501 U.S. 957</a></span></extracted-citation>, 979, n. 9, <extracted-citation case-ids="1107767" index="43" url="https://cite.case.law/us/501/957/#p979"><span class="citation" data-id="9432400"><a href="/opinion/112646/harmelin-v-michigan/" aria-description="Citation for case: Harmelin v. Michigan">111 S.Ct. 2680</a></span></extracted-citation>, <extracted-citation case-ids="1107767" index="44" url="https://cite.case.law/us/501/957/#p979"><span class="citation" data-id="9432400"><a href="/opinion/112646/harmelin-v-michigan/" aria-description="Citation for case: Harmelin v. Michigan">115 L.Ed.2d 836</a></span></extracted-citation> (1991) (opinion of Scalia, J.) ("it makes sense to scrutinize governmental action more closely when the State stands to benefit"). This concern is scarcely hypothetical. See Brief for American Civil Liberties Union et al. as <em>Amici Curiae</em> 7 ("Perhaps because they are politically easier to impose than generally applicable taxes, state and local governments nationwide increasingly depend heavily on fines and fees as a source of general revenue.").</p>
<p id="p-28">In short, the historical and logical case for concluding that the Fourteenth Amendment incorporates the Excessive Fines Clause is overwhelming. Protection against excessive punitive economic sanctions secured by the Clause is, to repeat, both "fundamental to our scheme of ordered liberty" and "deeply rooted in this Nation's history and tradition." <em>McDonald</em> , <extracted-citation case-ids="12455289,3644508" index="45" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">561 U.S., at 767</a></span></extracted-citation>, <extracted-citation case-ids="12455289,3644508" index="46" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">130 S.Ct. 3020</a></span></extracted-citation> (internal quotation marks omitted; emphasis deleted).</p>
<p id="p-29">II</p>
<p id="p-30">The State of Indiana does not meaningfully challenge the case for incorporating the Excessive Fines Clause as a general matter. Instead, the State argues that the Clause does not apply to its use of civil <em>in rem</em> forfeitures because, the State says, the Clause's specific application to such forfeitures is neither fundamental nor deeply rooted.</p>
<p id="p-31">In <em>Austin</em> v<em>. United States</em> , <extracted-citation case-ids="355668" index="47" url="https://cite.case.law/us/509/602/#p609"><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">509 U.S. 602</a></span></extracted-citation>, <extracted-citation case-ids="355668" index="48" url="https://cite.case.law/us/509/602/#p609"><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">113 S.Ct. 2801</a></span></extracted-citation>, <extracted-citation case-ids="355668" index="49" url="https://cite.case.law/us/509/602/#p609"><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">125 L.Ed.2d 488</a></span></extracted-citation> (1993), however, this Court held that civil <em>in rem</em> forfeitures fall within the Clause's protection when they are at least partially punitive. <em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">Austin</a></span></em> arose in the federal context. But when a Bill of Rights protection is incorporated, the protection applies "identically to both the Federal Government and the States."</p>
<p id="p-32"><a class="page-label" data-citation-index="1" data-label="690" href="#p690" id="p690">*690</a><em>McDonald</em> , <extracted-citation case-ids="12455289,3644508" index="50" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/#766" aria-description="Citation for case: McDonald v. City of Chicago">561 U.S., at 766</a></span>, n. 14</extracted-citation>, <extracted-citation case-ids="12455289,3644508" index="51" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">130 S.Ct. 3020</a></span></extracted-citation>. Accordingly, to prevail, Indiana must persuade us either to overrule our decision in <em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">Austin</a></span></em> or to hold that, in light of <em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">Austin</a></span></em> , the Excessive Fines Clause is not incorporated because the Clause's application to civil <em>in rem</em> forfeitures is neither fundamental nor deeply rooted. The first argument is not properly before us, and the second misapprehends the nature of our incorporation inquiry.</p>
<p id="p-33">A</p>
<p id="p-34">In the Indiana Supreme Court, the State argued that forfeiture of Timbs's SUV would not be excessive. See Brief in Opposition 5. It never argued, however, that civil <em>in rem</em> forfeitures were categorically beyond the reach of the Excessive Fines Clause. The Indiana Supreme Court, for its part, held that the Clause did not apply to the States at all, and it nowhere addressed the Clause's application to civil <em>in rem</em> forfeitures. See <extracted-citation case-ids="12331536" index="52" url="https://cite.case.law/ne3d/84/1179/"><span class="citation" data-id="4217247"><a href="/opinion/4439994/state-of-indiana-v-tyson-timbs/" aria-description="Citation for case: State of Indiana v. Tyson Timbs">84 N.E.3d 1179</a></span></extracted-citation>. Accordingly, Timbs sought our review of the question "[w]hether the Eighth Amendment's Excessive Fines Clause is incorporated against the States under the Fourteenth Amendment." Pet. for Cert. i. In opposing review, Indiana attempted to reformulate the question to ask "[w]hether the Eighth Amendment's Excessive Fines Clause restricts States' use of civil asset forfeitures." Brief in Opposition i. And on the merits, Indiana has argued not only that the Clause is not incorporated, but also that <em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">Austin</a></span></em> was wrongly decided. Respondents' "right, in their brief in opposition, to restate the questions presented," however, "does not give them the power to expand [those] questions." <em>Bray</em> v. <em>Alexandria Women's Health Clinic</em> , <extracted-citation case-ids="11925246" index="53" url="https://cite.case.law/us/506/263/#p279"><span class="citation" data-id="9432717"><a href="/opinion/112805/bray-v-alexandria-womens-health-clinic/" aria-description="Citation for case: Bray v. Alexandria Women&#x27;s Health Clinic">506 U.S. 263</a></span></extracted-citation>, 279, n. 10, <extracted-citation case-ids="11925246" index="54" url="https://cite.case.law/us/506/263/#p279"><span class="citation" data-id="9432717"><a href="/opinion/112805/bray-v-alexandria-womens-health-clinic/" aria-description="Citation for case: Bray v. Alexandria Women&#x27;s Health Clinic">113 S.Ct. 753</a></span></extracted-citation>, <extracted-citation case-ids="11925246" index="55" url="https://cite.case.law/us/506/263/#p279"><span class="citation" data-id="9432717"><a href="/opinion/112805/bray-v-alexandria-womens-health-clinic/" aria-description="Citation for case: Bray v. Alexandria Women&#x27;s Health Clinic">122 L.Ed.2d 34</a></span></extracted-citation> (1993) (emphasis deleted). That is particularly the case where, as here, a respondent's reformulation would lead us to address a question neither pressed nor passed upon below. Cf. <em>Cutter</em> v<em>. Wilkinson</em> , <extracted-citation case-ids="5868782" index="56" url="https://cite.case.law/us/544/709/#p718"><span class="citation" data-id="9434809"><a href="/opinion/142900/cutter-v-wilkinson/" aria-description="Citation for case: Cutter v. Wilkinson">544 U.S. 709</a></span></extracted-citation>, 718, n. 7, <extracted-citation case-ids="5868782" index="57" url="https://cite.case.law/us/544/709/#p718"><span class="citation" data-id="9434809"><a href="/opinion/142900/cutter-v-wilkinson/" aria-description="Citation for case: Cutter v. Wilkinson">125 S.Ct. 2113</a></span></extracted-citation>, <extracted-citation case-ids="5868782" index="58" url="https://cite.case.law/us/544/709/#p718"><span class="citation" data-id="9434809"><a href="/opinion/142900/cutter-v-wilkinson/" aria-description="Citation for case: Cutter v. Wilkinson">161 L.Ed.2d 1020</a></span></extracted-citation> (2005) ("[W]e are a court of review, not of first view ...."). We thus decline the State's invitation to reconsider our unanimous judgment in <em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">Austin</a></span></em> that civil <em>in rem</em> forfeitures are fines for purposes of the Eighth Amendment when they are at least partially punitive.</p>
<p id="p-35">B</p>
<p id="p-36">As a fallback, Indiana argues that the Excessive Fines Clause cannot be incorporated if it applies to civil <em>in rem</em> forfeitures. We disagree. In considering whether the Fourteenth Amendment incorporates a protection contained in the Bill of Rights, we ask whether the right guaranteed-not each and every particular application of that right-is fundamental or deeply rooted.</p>
<p id="p-37">Indiana's suggestion to the contrary is inconsistent with the approach we have taken in cases concerning novel applications of rights already deemed incorporated. For example, in <em>Packingham</em> v. <em>North Carolina</em> , 582 U.S. ----, <extracted-citation case-ids="12604756" index="59" url="https://cite.case.law/s-ct/137/1730/"><span class="citation" data-id="4181058"><a href="/opinion/4403805/packingham-v-north-carolina/" aria-description="Citation for case: Packingham v. North Carolina">137 S.Ct. 1730</a></span></extracted-citation>, <extracted-citation case-ids="12604756" index="60" url="https://cite.case.law/s-ct/137/1730/"><span class="citation" data-id="4181058"><a href="/opinion/4403805/packingham-v-north-carolina/" aria-description="Citation for case: Packingham v. North Carolina">198 L.Ed.2d 273</a></span></extracted-citation> (2017), we held that a North Carolina statute prohibiting registered sex offenders from accessing certain commonplace social media websites violated the First Amendment right to freedom of speech. In reaching this conclusion, we noted that the First Amendment's Free Speech Clause was "applicable to the States under the Due Process Clause of the Fourteenth Amendment." <em><extracted-citation case-ids="12604756" index="61" url="https://cite.case.law/s-ct/137/1730/"><span class="citation" data-id="4181058"><a href="/opinion/4403805/packingham-v-north-carolina/" aria-description="Citation for case: Packingham v. North Carolina">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12604756" index="62" url="https://cite.case.law/s-ct/137/1730/"><span class="citation" data-id="4181058"><a href="/opinion/4403805/packingham-v-north-carolina/" aria-description="Citation for case: Packingham v. North Carolina">137 S.Ct., at 1733</a></span></extracted-citation>. We did not, however, inquire whether the Free Speech Clause's application specifically to social media websites was fundamental or deeply rooted. See also, <em>e.g.</em> , <em>Riley</em> v<em>. California</em> , <extracted-citation index="63" url="https://cite.case.law/citations/?q=573%20U.S.%20373"><span class="citation no-link">573 U.S. 373</span></extracted-citation>, <extracted-citation case-ids="12581677" index="64" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. 2473</a></span></extracted-citation>, <extracted-citation case-ids="12581677" index="65" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">189 L.Ed.2d 430</a></span></extracted-citation> (2014) (holding, without separately considering incorporation, that States' warrantless <a class="page-label" data-citation-index="1" data-label="691" href="#p691" id="p691">*691</a>search of digital information stored on cell phones ordinarily violates the Fourth Amendment). Similarly here, regardless of whether application of the Excessive Fines Clause to civil <em>in rem</em> forfeitures is itself fundamental or deeply rooted, our conclusion that the Clause is incorporated remains unchanged.</p>
<p id="p-38">* * *</p>
<p id="p-39">For the reasons stated, the judgment of the Indiana Supreme Court is vacated, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="p-40">It is so ordered.</p>
<footnote label="1">
<p id="p-81">The sole exception is our holding that the Sixth Amendment requires jury unanimity in federal, but not state, criminal proceedings. <em>Apodaca</em> v. <em>Oregon</em> , <extracted-citation case-ids="6171091" index="66" url="https://cite.case.law/us/406/404/"><span class="citation" data-id="9424885"><a href="/opinion/108539/apodaca-v-oregon/" aria-description="Citation for case: Apodaca v. Oregon">406 U.S. 404</a></span></extracted-citation>, <extracted-citation case-ids="6171091" index="67" url="https://cite.case.law/us/406/404/"><span class="citation" data-id="9424885"><a href="/opinion/108539/apodaca-v-oregon/" aria-description="Citation for case: Apodaca v. Oregon">92 S.Ct. 1628</a></span></extracted-citation>, <extracted-citation case-ids="6171091" index="68" url="https://cite.case.law/us/406/404/"><span class="citation" data-id="9424885"><a href="/opinion/108539/apodaca-v-oregon/" aria-description="Citation for case: Apodaca v. Oregon">32 L.Ed.2d 184</a></span></extracted-citation> (1972). As we have explained, that "exception to th[e] general rule ... was the result of an unusual division among the Justices," and it "does not undermine the well-established rule that incorporated Bill of Rights protections apply identically to the States and the Federal Government." <em>McDonald</em> , <extracted-citation case-ids="12455289,3644508" index="69" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/#766" aria-description="Citation for case: McDonald v. City of Chicago">561 U.S., at 766</a></span>, n. 14</extracted-citation>, <extracted-citation case-ids="12455289,3644508" index="70" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">130 S.Ct. 3020</a></span></extracted-citation>.</p>
</footnote>
<footnote label="2">
<p id="p-82">"Amercements were payments to the Crown, and were required of individuals who were 'in the King's mercy,' because of some act offensive to the Crown." <em>Browning-Ferris</em> , <extracted-citation case-ids="6214309" index="71" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U.S., at 269</a></span></extracted-citation>, <extracted-citation case-ids="6214309" index="72" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">109 S.Ct. 2909</a></span></extracted-citation>. "[T]hough fines and amercements had distinct historical antecedents, they served fundamentally similar purposes-and, by the seventeenth and eighteenth centuries, the terms were often used interchangeably." Brief for Eighth Amendment Scholars as <em>Amici Curiae</em> 12.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. $8,850 in Currency.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. $8,850 in Currency"
type: case
citation: "461 U.S. 555 (1983)"
parallel_cite: "103 S. Ct. 2005; 76 L. Ed. 2d 143; 51 U.S.L.W. 4587"
neutral_cite: 1983 U.S. LEXIS 34
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-05-23
docket: No. 81-1062
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
  opinion_url: "https://www.courtlistener.com/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/"
  cluster_id: 110936
  opinion_id: null
  identity_checked: true
lake:
  record_id: "United States v. $8,850 in Currency"
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Civil Asset Forfeiture]]"
    role: Anchor
related:
  - "[[Civil Asset Forfeiture]]"
  - "[[United States v. James Daniel Good Real Property]]"
tags:
  - case
  - civil-forfeiture
  - due-process
  - delay
  - customs
  - currency-reporting
holding: "An 18-month delay between the customs seizure of currency and the Government's filing of a civil forfeiture action did not deny the claimant due process; whether a delay in instituting a forfeiture proceeding is reasonable is measured by the four-factor balancing test of Barker v. Wingo — the length of the delay, the reason for it, the claimant's assertion of the right to a hearing, and prejudice to the claimant."
aliases:
  - "United States v. $8,850 in Currency"
  - "United States v. $8,850"
  - United States v. Eight Thousand Eight Hundred and Fifty Dollars
---

# United States v. $8,850 in Currency

*461 U.S. 555 (1983)* (No. 81-1062) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 110936 → combined opinion 110936 (O'Connor, J.; 461 U.S. 555, argued Jan. 18, 1983, decided May 23, 1983). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star: the quoted opening holding sits between `*556` and `*557`, i.e., on page 556; internal citation to *Barker* elided). S9 promotes. -->

## Background
On September 10, 1975, Mary Josephine Vasquez arrived at Los Angeles International Airport after a short trip to Canada and declared to customs that she was not carrying more than $5,000; an inspector nonetheless found and seized $8,850 in currency she had failed to report under the Bank Secrecy Act. Vasquez petitioned the Customs Service for remission or mitigation, and a parallel criminal prosecution followed. The Government did not file a civil action to forfeit the currency until roughly 18 months after the seizure. The District Court found the delay reasonable and declared the currency forfeited, but a divided panel of the Ninth Circuit reversed, holding the delay violated due process.

## Issue
Whether the Government's 18-month delay between seizing the currency and filing a civil forfeiture proceeding deprived the claimant of property without due process of law.

## Rule
The Court held that the question is not answered by a fixed limitations period but by a contextual balancing borrowed from the speedy-trial setting, because a claimant's core complaint about forfeiture delay — being kept from a hearing at a meaningful time — mirrors the concern behind the right to a speedy trial. It therefore held: "We conclude that the four-factor balancing test of *Barker* v. *Wingo* ... provides the relevant framework for determining whether the delay in filing a forfeiture action was reasonable." — 461 U.S. at 556. The four *Barker* factors are the length of the delay, the reason for the delay, the claimant's assertion of the right to a hearing, and prejudice to the claimant. ^pin-556

## Application
Weighing those factors, the Court found no unreasonable delay. Much of the elapsed time was attributable to the claimant's own pending administrative petition for remission and to a parallel criminal proceeding whose outcome the Government could reasonably await; the reasons for the delay were legitimate rather than a tactic to gain advantage. Critically, Vasquez had not asserted a right to an earlier judicial hearing — she could have forced the issue but did not — and she neither claimed nor showed that the delay prejudiced her ability to defend the forfeiture. On balance, the delay did not deny due process.

## Conclusion
The judgment of the Court of Appeals for the Ninth Circuit was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]]. O'Connor, J., delivered the opinion of the Court. Stevens, J., dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *$8,850* is the timing anchor for civil forfeiture: the Government's delay in commencing a forfeiture action is tested under the *Barker v. Wingo* balancing factors rather than a rigid deadline, with the claimant's failure to demand a prompt hearing and the absence of prejudice weighing heavily. Teach it with *[[United States v. James Daniel Good Real Property]]* (1993), which governs the distinct question of *pre*-deprivation notice and hearing before the Government seizes real property.

## Appears on
- [[Civil Asset Forfeiture]] — *Anchor*

## Sources
- [*United States v. $8,850 in Currency*, 461 U.S. 555 (1983)](https://www.courtlistener.com/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/) — pinpoint: 556 (O'Connor, J., for the Court; the CL opinion text places the quoted opening holding between the reporter stars `*556` and `*557`, i.e., on page 556). Rule quote string-matched to the CL opinion text 2026-07-07 (the internal citation to *Barker v. Wingo* is elided).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "265e5c97f94cf452", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "461 U.S. 555 (1983)", "court": "U.S. Supreme Court", "neutral_cite": "1983 U.S. LEXIS 34", "official_citation_present": true, "parallel_cite": "103 S. Ct. 2005; 76 L. Ed. 2d 143; 51 U.S.L.W. 4587", "title": "United States v. $8,850 in Currency", "year": "1983"}}
{"assertion_id": "d574a1b488d2b043", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An 18-month delay between the customs seizure of currency and the Government's filing of a civil forfeiture action did not deny the claimant due process; whether a delay in instituting a forfeiture proceeding is reasonable is measured by the four-factor balancing test of Barker v. Wingo — the length of the delay, the reason for it, the claimant's assertion of the right to a hearing, and prejudice to the claimant.", "title": "United States v. $8,850 in Currency"}}
{"assertion_id": "e19c5c0593139a7b", "dimension": "support", "kind": "home_role", "locator": {"home": "Civil Asset Forfeiture"}, "payload": {"home": "Civil Asset Forfeiture", "role": "Anchor", "title": "United States v. $8,850 in Currency"}}
{"assertion_id": "3caffa7c9449f9fd", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. $8,850 in Currency"}}
{"assertion_id": "8db97f1a07dec926", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. $8,850 in Currency", "varies_by_point": "false"}}
```

### lake record — United States v. $8,850 in Currency

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. $8,850 in Currency",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Eight Thousand Eight Hundred & Fifty Dollars",
    "case_name_short": "$8,850",
    "case_name_full": "United States v. Eight Thousand Eight Hundred and Fifty Dollars ($8,850) in United States Currency",
    "input_case_name": "United States v. $8,850 in Currency",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-05-23",
    "year": 1983,
    "docket": "No. 81-1062",
    "cluster_id": 110936,
    "lead_opinion_id": 9429199,
    "sibling_ids": [],
    "absolute_url": "/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "461 U.S. 555",
      "volume": "461",
      "reporter": "U.S.",
      "page": "555",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 2005",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2005",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "76 L. Ed. 2d 143",
        "volume": "76",
        "reporter": "L. Ed. 2d",
        "page": "143",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4587",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4587",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 34",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "34",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "461 U.S. 555",
        "volume": "461",
        "reporter": "U.S.",
        "page": "555",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 2005",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2005",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "76 L. Ed. 2d 143",
        "volume": "76",
        "reporter": "L. Ed. 2d",
        "page": "143",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 34",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "34",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4587",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4587",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "461 U.S. 555",
    "official_selection": {
      "court_class": "scotus",
      "selected": "461 U.S. 555",
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
    "date_created": "2026-07-06T13:41:57Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:42:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:42:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:42:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:42:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-8-850-in-currency--110936",
      "to_record_id": "United States v. $8,850 in Currency",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. $8,850 in Currency

```
<opinion type="majority">
<author id="b614-10">Justice O’Connor</author>
<p id="A8h">delivered the opinion of the Court.</p>
<p id="Aeo">United States Customs officials seized $8,850 in currency from the claimant as she passed through customs at Los Angeles International Airport. The question in this case is whether the Government’s 18-month delay in filing a civil proceeding for forfeiture of the currency violates the claimant’s right to due process of law. We conclude that the four-factor balancing test of <em>Barker </em>v. <em>Wingo, </em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">407 U. S. 514</a></span> (1972), provides the relevant framework for determining whether the delay in filing a forfeiture action was reasonable. Applying the <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>test to the circumstances of this case, we find no unreasonable delay.</p>
<p id="AkG"><page-number citation-index="1" label="557">*557</page-number>I</p>
<p id="A2q">A</p>
<p id="Avp">Section 231 of the Bank Secrecy Act of 1970, <span class="citation no-link">84 Stat. 1122</span>, <span class="citation no-link">31 U. S. C. § 1101</span>, requires persons knowingly transporting monetary instruments exceeding $5,000 into the United States to file a report with the Customs Service declaring the amount being transported. Congress has authorized the Government to seize and forfeit any monetary instruments for which a required report was not filed. <span class="citation no-link">31 U. S. C. § 1102</span>(a). Since the Bank Secrecy Act does not specify the procedures to be followed in seizing monetary instruments, the Customs Service generally follows the procedures governing forfeitures for violations of the customs laws, as set forth in <span class="citation no-link">19 U. S. C. § 1602</span> <em>et seq. </em>(1976 ed. and Supp. V), and the implementing regulations. Under these procedures, the Customs Service notifies any person who appears to have an interest in the seized property of the property’s liability to forfeiture and of the claimant’s right to petition the Secretary of the Treasury for remission or mitigation of the forfeiture.<footnotemark>1</footnotemark> See <span class="citation no-link">19 CFR § 162.31</span>(a) (1982). The regulations require a claimant to file the petition within 60 days. <span class="citation no-link">19 CFR § 171.12</span>(b) (1982).</p>
<p id="Asa">If the claimant does not file a petition, or if the decision on a petition makes legal proceedings appear necessary,<footnotemark>2</footnotemark> the appropriate customs officer must prepare a full report of the <page-number citation-index="1" label="558">*558</page-number>seizure for the United States Attorney. <span class="citation no-link">19 U. S. C. § 1603</span> (1976 ed., Supp. V).<footnotemark>3</footnotemark> Upon receipt of a report, the United States Attorney is required “immediately to inquire into the facts” and, if it appears probable that a forfeiture has been incurred, “forthwith to cause the proper proceedings to be commenced and prosecuted, without delay.” <span class="citation no-link">19 U. S. C. § 1604</span> (1976 ed., Supp. V). After a case is reported to the United States Attorney for institution of legal proceedings, no administrative action may be taken on any petition for remission or mitigation. <span class="citation no-link">19 CFR § 171.2</span>(a) (1982).</p>
<p id="b616-5">The Customs Service processes over 50,000 noncontra-band forfeitures per year. U. S. Customs Service, Customs U. S. A. 36 (1982). In 90% of all seizures, the claimant files an administrative petition for remission or mitigation. Brief for United States 7. The Secretary in turn grants at least partial relief for an estimated 75% of the petitions. <em><span class="citation no-link">Ibid.</span> </em>Typically, this relief terminates the dispute without the filing of a forfeiture action in district court.</p>
<p id="b616-6">B</p>
<p id="b616-7">On September 10, 1975, claimant Mary Josephine Vasquez and a companion arrived at Los Angeles International Airport after a short visit to Canada. During customs processing, Vasquez declared that she was not carrying more than $5,000 in currency. Nevertheless, a customs inspector discovered and seized $8,850 in United States currency from her. On September 18, 1975, the Customs Service officially informed Vasquez by letter that the seized currency was subject to forfeiture and that she had the right to petition for re<page-number citation-index="1" label="559">*559</page-number>mission or mitigation. A week later, Vasquez filed a petition for remission or mitigation,<footnotemark>4</footnotemark> asserting that the violation was unintentional because she had mistakenly believed she was required to declare only funds that had been obtained in another country and that she had brought the seized funds with her from the United States.</p>
<p id="b617-5">On October 20, 1975, the Customs Office of Investigation assigned Special Agent Pompeo to investigate the petition. Within a few days, Agent Pompeo had interviewed the customs inspectors at the airport who were involved in the seizure. After several unsuccessful attempts to contact him, in mid-November Agent Pompeo contacted Vasquez’ attorney to arrange an interview with Vasquez. The attorney was unable to meet at that time, and he desired to be present during the interview with his client. Around this time, Agent Pompeo also opened a criminal file because she suspected Vasquez of smuggling drugs. From November 1975 until April 1976, Agent Pompeo contacted various state, federal, and Canadian law enforcement officials to determine whether the seized currency was part of a narcotics transaction.<footnotemark>5</footnotemark></p>
<p id="b617-6">In January 1976, Vasquez’ attorney inquired about the status of the petition, and was informed it was still under investigation. On March 2, 1976, Agent Pompeo again contacted the attorney regarding an interview with Vasquez, and an interview took place three days later. On April 26, 1976, the attorney again inquired about the status of the petition and requested that it be acted on as soon as possible. Also in April 1976, Agent Pompeo received final reports from the law enforcement agencies. From these reports, Agent <page-number citation-index="1" label="560">*560</page-number>Pompeo concluded there was no evidence to support a charge of narcotics violations.</p>
<p id="b618-5">In May 1976, Agent Pompeo submitted a report to the United States Attorney, recommending prosecution of Vasquez for the reporting violation. After Agent Pompeo re-interviewed the customs agents and reported her findings, the United States Attorney submitted the case to the grand jury. On June 15, 1976, a grand jury returned an indictment charging Vasquez with the felony of knowingly and willfully making false statements to a United States Customs officer, in violation of <span class="citation no-link">18 U. S. C. § 1001</span>; and with the misdemeanor of knowingly and willfully transporting $8,850 into the United States without filing a report, in violation of <span class="citation no-link">31 U. S. C. §§ 1058</span> and 1101. The indictment sought forfeiture of the currency as part of the misdemeanor count.</p>
<p id="b618-6">In August 1976, Agent Pompeo recommended that disposition of the remission petition be withheld until the currency was no longer needed as evidence at the criminal trial. On December 24, 1976, Vasquez was convicted on the felony count but acquitted on the misdemeanor charge of willfully failing to file a currency report.<footnotemark>6</footnotemark> Four days after the criminal trial was completed, Vasquez' attorney again inquired whether there would be any further delay in acting on the petition.</p>
<p id="b618-7">On March 10,1977, the Customs Service informed Vasquez that the claim of forfeiture had been referred to the United States Attorney. Within two weeks, a complaint seeking forfeiture under <span class="citation no-link">31 U. S. C. § 1102</span> was filed in Federal District Court.<footnotemark>7</footnotemark> In answer to the complaint, Vasquez admitted the factual allegations but asserted as one of several affirma<page-number citation-index="1" label="561">*561</page-number>tive defenses that the Government’s “dilatory processing” of her petition for remission or mitigation and “dilatory” commencement of the civil forfeiture action violated her right to due process. The District Court, after a 2-day bench trial held in January 1978, determined that the time which had elapsed was reasonable under the circumstances and therefore declared the currency forfeited under <span class="citation no-link">31 U. S. C. § 1102</span>.</p>
<p id="b619-4">A divided panel of the Court of Appeals for the Ninth Circuit reversed. <span class="citation" data-id="9467783"><a href="/opinion/389222/united-states-v-eight-thousand-eight-hundred-fifty-dollars-885000-in/" aria-description="Citation for case: United States v. Eight Thousand Eight Hundred Fifty...">645 F. 2d 836</a></span> (1981). Proceeding from the premise that the Government must bring forfeiture actions promptly because seizures infringe upon property rights, the Court of Appeals concluded that the Government’s 18-month delay in filing its forfeiture action was unjustified. The Court of Appeals specifically held that pending administrative or criminal investigations cannot justify the delay when the necessary elements for a forfeiture were established at the time of the seizure and when the claimant seeks a speedy resolution of the claim. The Court of Appeals likewise rejected the Government’s argument that the claimant should be required to show that the delay prejudiced her ability to present a defense to the forfeiture action. As a remedy for the due process violation, the Court of Appeals ordered dismissal of the Government’s forfeiture action.<footnotemark>8</footnotemark></p>
<p id="b619-5">Since other Circuits have determined that pending criminal<footnotemark>9</footnotemark> or administrative<footnotemark>10</footnotemark> investigations and prejudice to the claimant<footnotemark>11</footnotemark> are relevant considerations in determining <page-number citation-index="1" label="562">*562</page-number>whether a delay in instituting forfeiture proceedings violates due process, we granted certiorari to resolve the conflict. <span class="citation multiple-matches"><a href="/c/U.%20S./455/1015/">455 U. S. 1015</a></span> (1982). We reverse.</p>
<p id="b620-3">II</p>
<p id="A8V">The due process issue presented here is a narrow one. Vasquez concedes that the Government could constitutionally seize her property without a prior hearing.<footnotemark>12</footnotemark> Nor does Vasquez challenge the sufficiency of the judicial hearing that was eventually held. She argues only that the Government’s delay in filing a civil forfeiture proceeding violated her due process right to a hearing “‘at a meaningful time,”’ <em>Fuentes </em>v. <em>Shevin, </em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#80" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67, 80</a></span> (1972), quoting <em>Armstrong </em>v. <em>Manzo, </em><span class="citation" data-id="107034"><a href="/opinion/107034/armstrong-v-manzo/#552" aria-description="Citation for case: Armstrong v. Manzo">380 U. S. 545, 552</a></span> (1965). Unlike the situation where due process requires a prior hearing, there is no obvious bright line dictating when a postseizure hearing must occur. Because our prior cases in this area have wrestled with whether due process requires a preseizure hearing, we have not previously determined when a postseizure delay may be<page-number citation-index="1" label="563">*563</page-number>come so prolonged that the dispossessed property owner has been deprived of a meaningful hearing at a meaningful time.<footnotemark>13</footnotemark></p>
<p id="b621-5">The Government argues that there is no general due process requirement of prompt postseizure filing of a judicial forfeiture action. Rather, the Government urges that the standard for assessing the timeliness of the suit be the same as that employed for due process challenges to delay in instituting criminal prosecutions. As articulated in <em>United States </em>v. <em>Lovasco, </em><span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/" aria-description="Citation for case: United States v. Lovasco">431 U. S. 783</a></span> (1977), such claims can prevail only upon a showing that the Government delayed seeking an indictment in a deliberate attempt to gain an unfair tactical advantage over the defendant or in reckless disregard of its probable prejudicial impact upon the defendant’s ability to defend against the charges. The Government argues that in the absence of unfair conduct of this sort, the timeliness of the suit is controlled only by the applicable statute of limitations. Here, Congress has required the Government to institute forfeiture proceedings within five years. <span class="citation no-link">19 U. S. C. §1621</span> (1976 ed., Supp. V).</p>
<p id="b621-6">We reject the Government’s suggestion that <em><span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/" aria-description="Citation for case: United States v. Lovasco">Lovasco</a></span> </em>provides the appropriate test for determining whether the delay violates the due process command. <em><span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/" aria-description="Citation for case: United States v. Lovasco">Lovasco</a></span> </em>recognized that the interests of the suspect and society are better served if, absent bad faith or extreme prejudice to the defendant, the prosecutor is allowed sufficient time to weigh and sift evidence to ensure that an indictment is well founded. While the <page-number citation-index="1" label="564">*564</page-number>value of allowing the Government time to pursue its investigation applies to the civil forfeiture situation as well as the criminal proceeding, a major distinction exists. A suspect who has not been indicted retains his liberty; a claimant whose property has been seized, however, has been entirely deprived of the use of the property.</p>
<p id="b622-5">A more apt analogy is to a defendant’s right to a speedy trial once an indictment or other formal process has issued. In that situation, the defendant no longer retains his complete liberty. Even if he is allowed to post bail, his liberty is subject to the conditions required by his bail agreement. In <em>Barker </em>v. <em>Wingo, </em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">407 U. S. 514</a></span> (1972), we developed a test to determine when Government delay has abridged the right to a speedy trial. The <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>test involves a weighing of four factors: length of delay, the reason for the delay, the defendant’s assertion of his right, and prejudice to the defendant. <span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/#530" aria-description="Citation for case: Barker v. Wingo"><em>Id., </em>at 530</a></span>.</p>
<p id="b622-6">Of course, <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>dealt with the Sixth Amendment right to a speedy trial rather than the Fifth Amendment right against deprivation of property without due process of law. Nevertheless, the Fifth Amendment claim here — which challenges only the length of time between the seizure and the initiation of the forfeiture trial — mirrors the concern of undue delay encompassed in the right to a speedy trial. The <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>balancing inquiry provides an appropriate framework for determining whether the delay here violated the due process right to be heard at a meaningful time. We have often repeated the seminal statement from <em>Morrissey </em>v. <em>Brewer, </em><span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#481" aria-description="Citation for case: Morrissey v. Brewer">408 U. S. 471, 481</a></span> (1972), that “due process is flexible and calls for such procedural protections as the particular situation demands.” <em>E. g., Schweiker </em>v. <em>McClure, </em><span class="citation" data-id="110694"><a href="/opinion/110694/schweiker-v-mcclure/#200" aria-description="Citation for case: Schweiker v. McClure">456 U. S. 188, 200</a></span> (1982); <em>Memphis Light, Gas &amp; Water Division </em>v. <em>Craft, </em><span class="citation" data-id="9427172"><a href="/opinion/109855/memphis-light-gas-water-division-v-craft/#14" aria-description="Citation for case: Memphis Light, Gas &amp; Water Division v. Craft">436 U. S. 1, 14-15, n. 15</a></span> (1978). The flexible approach of <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span>, </em>which “necessarily compels courts to approach speedy trial cases on an <em>ad hoc </em>basis,” 407 U. S., at 530, is thus an appropriate inquiry for determining whether <page-number citation-index="1" label="565">*565</page-number>the flexible requirements of due process have been met. As we stressed in <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span>, </em>none of these factors is a necessary or sufficient condition for finding unreasonable delay. Rather, these elements are guides in balancing the interests of the claimant and the Government to assess whether the basic due process requirement of fairness has been satisfied in a particular case.<footnotemark>14</footnotemark></p>
<p id="b623-5">III</p>
<p id="b623-6">In applying the <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>balancing test to this situation, the overarching factor is the length of the delay. As we said in <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span>, </em>the length of the delay “is to some extent a triggering mechanism.” <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Ibid.</a></span> </em>Little can be said on when a delay becomes presumptively improper, for the determination necessarily depends on the facts of the particular case. Our inquiry is the constitutional one of due process; we are not establishing a statute of limitations. Obviously, short delays — of perhaps a month or so — need less justification than longer delays. We regard the delay here — some 18 months— as quite significant. Being deprived of this substantial sum of money for a year and a half is undoubtedly a significant burden.</p>
<p id="b623-7">Closely related to the length of the delay is the reason the Government assigns to justify the delay. <span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/#531" aria-description="Citation for case: Barker v. Wingo"><em>Id., </em>at 531</a></span>. The Government must be allowed some time to decide whether to institute forfeiture proceedings. The customs official’s decision to seize property is of necessity a hasty one. Both the Government and the claimant have an interest in a rule that allows the Government some time to investigate the situation in order to determine whether the facts entitle the Government to forfeiture so that, if not, the Government may return the money without formal proceedings. Cf. <span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#791" aria-description="Citation for case: United States v. Lovasco"><em>Lovasco, supra, </em><page-number citation-index="1" label="566">*566</page-number>at 791</a></span>. Normally, investigating officials can make such a determination fairly quickly, so that this reason alone could only rarely justify a lengthy delay.</p>
<p id="b624-5">An important justification for delaying the initiation of forfeiture proceedings is to see whether the Secretary’s decision on the petition for remission will obviate the need for judicial proceedings. This delay can favor both the claimant and the Government. Cf. <span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/#521" aria-description="Citation for case: Barker v. Wingo"><em>Barker, supra, </em>at 521</a></span>; <span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#794" aria-description="Citation for case: United States v. Lovasco"><em>Lovasco, supra, </em>at 794-795</a></span>. In many cases, the Government’s entitlement to the property is clear, and the claimant’s only prospect for reacquiring the property is that the Secretary will favorably exercise his discretion and allow remission or mitigation. If the Government were forced to initiate judicial proceedings without regard to administrative proceedings, the claimant would lose this benefit. Further, administrative proceedings are less formal and expensive than judicial forfeiture proceedings. Given the great percentage of successful petitions, allowing the Government to wait for action on administrative petitions eliminates unnecessary and burdensome court proceedings. Finally, a system whereby the judicial proceeding occurs after administrative action spares litigants and the Government from the burden of simultaneously participating in two forums.<footnotemark>15</footnotemark></p>
<p id="b624-6">The Government takes the extreme position, however, that a pending administrative petition should completely toll the requirement of filing a judicial proceeding. Nothing in the statutory scheme or in our cases supports this argument. A claimant need not waive his right to a prompt judicial hearing simply because he seeks the additional remedy of an administrative petition for mitigation.<footnotemark>16</footnotemark> Unreasonable delay <page-number citation-index="1" label="567">*567</page-number>in processing the administrative petition cannot justify prolonged seizure of his property without a judicial hearing. Rather, the pendency of an administrative petition is simply a weighty factor in the flexible balancing inquiry.</p>
<p id="b625-5">Pending criminal proceedings present similar justifications for delay in instituting civil forfeiture proceedings. A prior or contemporaneous civil proceeding could substantially hamper the criminal proceeding, which — as here — may often include forfeiture as part of the sentence. A prior civil suit might serve to estop later criminal proceedings and may provide improper opportunities for the claimant to discover the details of a contemplated or pending criminal prosecution. Compare Federal Rule of Civil Procedure 26(b) with Federal Rule of Criminal Procedure 16. In some circumstances, a civil forfeiture proceeding would prejudice the claimant’s ability to raise an inconsistent defense in a contemporaneous criminal proceeding. See, <em>e. g., United States </em>v. <em>U. S. Currency, </em><span class="citation" data-id="9466912"><a href="/opinion/380368/united-states-v-u-s-currency/" aria-description="Citation for case: United States v. U. S. Currency">626 F. 2d 11</a></span> (CA6 1980). Again, however, the pendency of criminal proceedings is only an element to be considered in determining whether delay is unreasonable. Although federal criminal proceedings are generally fairly rapid since the advent of the Speedy Trial Act of 1974, <span class="citation no-link">18 U. S. C. § 3161</span> <em>et seq. </em>(1976 ed. and Supp. V), the pendency of a trial does not automatically toll the time for instituting a forfeiture proceeding.</p>
<p id="b625-6">In this case the Government relies on both a pending petition for mitigation or remission and a pending criminal proceeding to justify the delay in filing civil forfeiture proceedings. During the initial seven months after the seizure the Customs Service was determining whether to grant the petition. This investigation required responses to inquiries to state, federal, and Canadian law enforcement officers. Such an investigation inherently is time consuming, and there is no <page-number citation-index="1" label="568">*568</page-number>indication that it was not pursued with diligence. The Customs Service then referred the matter to the United States Attorney, who obtained criminal indictments within two months. Importantly, one count of the indictment sought forfeiture as part of the sentence. If the Government had prevailed, a civil forfeiture would have been rendered unnecessary. There is no evidence in the record that the Government was responsible for the slow pace of the criminal proceedings, which reached a verdict five months later. After the criminal trial ended, the Secretary of the Treasury made a final decision within three months to deny the petition, and the United States Attorney promptly filed a civil forfeiture proceeding.</p>
<p id="b626-5">We are impressed by the assessment made by the District Court that the Goverment had acted with all due speed. Indeed, in an oral colloquy during trial the District Judge commented:</p>
<blockquote id="b626-6">“I have been anxious to see in this case whether there has been a lot of dilitory <em>[sic] </em>conduct that the government has really not done what it should do in order to push this thing with all reasonable speed, and, frankly, I don’t see any point in which the government has been lax.</blockquote>
<blockquote id="b626-7"><em>“If </em>I had found such, and I found it an unreasonable length of time, I would have been happy to so hold ....</blockquote>
<blockquote id="b626-8">“But, in view of the evidence here, I just cannot see any way in which this Court can say that the government has not pursued their claim in all reasonable diligence.” App. 77.</blockquote>
<p id="b626-9">In sum, the Government’s diligent pursuit of pending administrative and criminal proceedings indicates strongly that the reasons for its delay in filing a civil forfeiture proceeding were substantial.</p>
<p id="b626-10">The third element to be considered in the due process balance is the claimant’s assertion of the right to a judicial hear<page-number citation-index="1" label="569">*569</page-number>ing. A claimant is able to trigger rapid filing of a forfeiture action if he desires it. First, the claimant can file an equitable action seeking an order compelling the filing of the forfeiture action or return of the seized property. See <em>Slocum, </em>v. <em>Mayberry, </em><span class="citation" data-id="85171"><a href="/opinion/85171/slocum-v-mayberry/#10" aria-description="Citation for case: Slocum v. Mayberry">2 Wheat. 1, 10</a></span> (1817) (Marshall, C. J.). Less formally, the claimant could simply request that the Customs Service refer the matter to the United States Attorney. If the claimant believes the initial seizure was improper, he could file a motion under Federal Rule of Criminal Procedure 41(e) for a return of the seized property. Yasquez did none of these things and only occasionally inquired about the result of the petition for mitigation or remission and asked that the Secretary reach a decision promptly. The failure to use these remedies can be taken as some indication that Yasquez did not desire an early judicial hearing.</p>
<p id="b627-5">The final element is whether the claimant has been prejudiced by the delay. The primary inquiry here is whether the delay has hampered the claimant in presenting a defense on the merits, through, for example, the loss of witnesses or other important evidence. Such prejudice could be a weighty factor indicating that the delay was unreasonable. Here, Vasquez has never alleged or shown that the delay affected her ability to defend against the impropriety of the forfeiture on the merits. On the contrary, Vasquez conceded that the elements necessary for a forfeiture under § 1102(a) were present in her case.</p>
<p id="b627-6">IV</p>
<p id="b627-7">In this case, the balance of factors indicates that the Government’s delay in instituting civil forfeiture proceedings was reasonable. Although the 18-month delay was a substantial period of time, it was justified by the Government’s diligent efforts in processing the petition for mitigation or remission and in pursuing related criminal proceedings. Vasquez never indicated that she desired early commencement of a civil forfeiture proceeding, and she has not asserted or shown <page-number citation-index="1" label="570">*570</page-number>that the delay prejudiced her ability to defend against the forfeiture. Therefore, the claimant was not denied due process of law. The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b628-5">
<em>So ordered.</em>
</p>
<footnote label="1">
<p id="AK4"> In addition to the general remission provisions of Title IV, Title II of the Bank Secrecy Act contains its own remission provision, <span class="citation no-link">31 U. S. C. § 1104</span>: “The Secretary may in his discretion remit any forfeiture or penalty under this subchapter in whole or in part upon such terms and conditions as he deems reasonable and just.”</p>
</footnote>
<footnote label="2">
<p id="AGqz"> At the time of the seizure in this case, a customs officer could institute nonjudicial, summary forfeiture proceedings if the value of the seized merchandise was not more than $2,500. See <span class="citation no-link">19 U. S. C. §§ 1607-1609</span>. Congress has since raised this limit to $10,000. <span class="citation no-link">19 U. S. C. § 1607</span> (1976 ed., Supp. V). Even for a seizure of property appraised at less than $10,000, the claimant has a right to a judicial determination upon posting a $250 bond to cover costs. <span class="citation no-link">19 U. S. C. § 1608</span>.</p>
</footnote>
<footnote label="3">
<p id="b616-8"> At the time of the seizure of the currency from Vasquez, <span class="citation no-link">19 U. S. C. § 1603</span> contained no requirement of a prompt report of a seizure by the Customs Service to the United States Attorney for purposes of instituting forfeiture proceedings. As amended in 1978, § 1603 now requires the appropriate customs officer “to report promptly” to the United States Attorney whenever legal proceedings “in connection with such seizure or discovery are required.” <span class="citation no-link">19 U. S. C. § 1603</span> (1976 ed., Supp. V).</p>
</footnote>
<footnote label="4">
<p id="b617-7"> On September 11, 1975, the day after the seizure, Vasquez’ counsel had written an informal letter to the District Director of Customs, explaining why she had not declared the money.</p>
</footnote>
<footnote label="5">
<p id="b617-9"> This inquiry was relevant to the reporting violation. A currency reporting violation is normally a misdemeanor, but a reporting violation committed in furtherance of any other federal offense is a felony. Compare <span class="citation no-link">31 U. S. C. § 1058</span> with <span class="citation no-link">31 U. S. C. § 1059</span>.</p>
</footnote>
<footnote label="6">
<p id="b618-8"> The conviction on the felony count was subsequently reversed because court files were left in the jury room during deliberations. <em>United States </em>v. <em>Vasquez, </em><span class="citation" data-id="365698"><a href="/opinion/365698/united-states-v-mary-josephine-vasquez/" aria-description="Citation for case: United States v. Mary Josephine Vasquez">597 F. 2d 192</a></span> (CA9 1979).</p>
</footnote>
<footnote label="7">
<p id="b618-9"> On March 28, 1977, the Customs Service officially notified Vasquez that her petition had been denied.</p>
</footnote>
<footnote label="8">
<p id="b619-6"> Because we find no violation of due process, we do not decide whether dismissal of the forfeiture action with prejudice would be an appropriate remedy for undue delay.</p>
</footnote>
<footnote label="9">
<p id="b619-7"><em> E. g., White </em>v. <em>Acree, </em><span class="citation" data-id="364740"><a href="/opinion/364740/lincoln-c-white-john-b-ford-intervenor-appellee-v-vernon-d-acree/" aria-description="Citation for case: Lincoln C. White, John B. Ford, Intervenor-Appellee v....">594 F. 2d 1385</a></span> (CA10 1979).</p>
</footnote>
<footnote label="10">
<p id="b619-8"> <em>E. g., United States </em>v. <em>Thirty-Six Thousand One Hundred &amp; Twenty-Five Dollars in U. S. Currency, </em><span class="citation multiple-matches"><a href="/c/F.%202d/642/1211/">642 F. 2d 1211</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./454/835/">454 U. S. 835</a></span> (1981) (aff’g <span class="citation" data-id="1980791"><a href="/opinion/1980791/united-states-v-thirty-six-thousand-one-hundred-twenty-five-dollars/" aria-description="Citation for case: United States v. Thirty-Six Thousand, One Hundred &amp;...">510 F. Supp. 303</a></span> (ED La. 1980)).</p>
</footnote>
<footnote label="11">
<p id="b619-9"><em> E. g., United States </em>v. <em>Various Pieces of Semiconductor Manufacturing Equipment, </em><span class="citation" data-id="390531"><a href="/opinion/390531/united-states-v-various-pieces-of-semiconductor-manufacturing-equipment/" aria-description="Citation for case: United States v. Various Pieces of Semiconductor...">649 F. 2d 606</a></span> (CA8 1981); <em>United States </em>v. <em>One 1976 Mercedes 450 SLC, </em><span class="citation" data-id="8914520"><a href="/opinion/8925059/united-states-v-one-1976-mercedes-450-slc/" aria-description="Citation for case: United States v. One 1976 Mercedes 450 SLC">667 F. 2d 1171</a></span> (CA5 1982).</p>
</footnote>
<footnote label="12">
<p id="b620-4"> The general rule, of course, is that absent an “extraordinary situation” a party cannot invoke the power of the state to seize a person’s property without a <em>prior </em>judicial determination that the seizure is justified. <em>Boddie </em>v. <em>Connecticut, </em><span class="citation" data-id="9424471"><a href="/opinion/108281/boddie-v-connecticut/#378" aria-description="Citation for case: Boddie v. Connecticut">401 U. S. 371, 378-379</a></span> (1971). See also <em>North Georgia Finishing, Inc. </em>v. <em>Di-Chem, Inc., </em><span class="citation" data-id="9425911"><a href="/opinion/109137/north-georgia-finishing-inc-v-di-chem-inc/" aria-description="Citation for case: North Georgia Finishing, Inc. v. Di-Chem, Inc.">419 U. S. 601</a></span> (1975); <em>Fuentes </em>v. <em>Shevin, </em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67</a></span> (1972); <em>Sniadach </em>v. <em>Family Finance Corp., </em><span class="citation" data-id="9424067"><a href="/opinion/107960/sniadach-v-family-finance-corp-of-bay-view/" aria-description="Citation for case: Sniadach v. Family Finance Corp. of Bay View">395 U. S. 337</a></span> (1969); cf. <em>Mitchell </em>v. <em>W. T. Grant Co., </em><span class="citation" data-id="9425706"><a href="/opinion/109023/mitchell-v-w-t-grant-co/" aria-description="Citation for case: Mitchell v. W. T. Grant Co.">416 U. S. 600</a></span> (1974). But we have previously held that such an extraordinary situation exists when the government seizes items subject to forfeiture. In <em>Calero-Toledo </em>v. <em>Pearson Yacht Leasing Co., </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S. 663</a></span> (1974), the Court upheld a Puerto Rico statute modeled after a federal forfeiture statute, <span class="citation no-link">21 U. S. C. § 881</span>(a), which allowed Puerto Rican authorities to seize, without prior notice or hearing, a yacht suspected of importing marihuana. <em>Pearson Yacht </em>clearly indicates that due process does not require federal customs officials to conduct a hearing before seizing items subject to forfeiture. Such a requirement would make customs processing entirely unworkable. The government interests found decisive in <em>Pearson Yacht </em>are equally present in this situation: the seizure serves important governmental purposes; a pre-seizure notice might frustrate the statutory purpose; and the seizure was made by government officials rather than self-motivated private parties.</p>
</footnote>
<footnote label="13">
<p id="b621-7"> In <em>United States </em>v. <em>Thirty-seven </em>Photographs, <span class="citation" data-id="9424558"><a href="/opinion/108332/united-states-v-thirty-seven-37-photographs/" aria-description="Citation for case: United States v. Thirty-Seven (37) Photographs">402 U. S. 363</a></span> (1971), we construed a statute allowing customs officials to seize obscene material as requiring a postseizure filing within 14 days and completion of the hearing in an additional 60 days. That case interpreted the statute so as to avoid possible First Amendment problems of prior restraint. The case did not involve, and thus we had no occasion to address, the time restraints imposed by the Due Process Clause. Even if we'were inclined to interpret the statutes here in such a way as to avoid any due process question, it would be impossible to read into the statutory scheme, as we did in <em>Thirty-seven Photographs, </em>a short statute of limitations, since <span class="citation no-link">19 U. S. C. § 1621</span> (1976 ed., Supp. V) expressly allows the Government to bring a civil forfeiture proceeding within five years.</p>
</footnote>
<footnote label="14">
<p id="b623-8"> The deprivation in <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>— loss of liberty — may well be more grievous than the deprivation of one’s use of property at issue here. Thus, the balance of the interests, which depends so heavily on the context of the particular situation, may differ from a situation involving the right to a speedy trial.</p>
</footnote>
<footnote label="15">
<p id="b624-7"> By regulation, the Secretary is not allowed to process any petition for remission or mitigation while a civil forfeiture proceeding is pending. <span class="citation no-link">19 CFR § 171.2</span>(a) (1982).</p>
</footnote>
<footnote label="16">
<p id="b624-8"> Under the 1978 revisions to <span class="citation no-link">19 CFR § 162.31</span>(a), the Customs Service is now required to warn claimants that unless they agree to defer judicial forfeiture proceedings until completion of the administrative process, the case <page-number citation-index="1" label="567">*567</page-number>will be referred promptly to the United States Attorney for institution of judicial proceedings, or summary forfeiture proceedings will be begun.</p>
</footnote>
</opinion>
```

---
