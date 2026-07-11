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

## GROUP: _overhaul2/lake/cases/United States v. Wade.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Wade"
type: case
citation: "388 U.S. 218 (1967)"
parallel_cite: "87 S. Ct. 1926; 18 L. Ed. 2d 1149"
neutral_cite: 1967 U.S. LEXIS 1085
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-06-12
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-06-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Wade
  varies_by_point: false
  scope_note: "Right-to-counsel reach later limited by Kirby v. Illinois (post-charge only) and United States v. Ash (no counsel at photo arrays)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107486/united-states-v-wade/"
  cluster_id: 107486
  opinion_id: 9423472
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Anchor"
related: ["[[Gilbert v. California]]", "[[Kirby v. Illinois]]", "[[United States v. Ash]]", "[[Stovall v. Denno]]"]
aliases: []
tags: ["case", "sixth-amendment", "eyewitness-identification", "lineup", "right-to-counsel", "critical-stage"]
holding: "A post-indictment lineup is a critical stage of the prosecution at which the accused has a Sixth Amendment right to counsel; counsel's…"
lake:
  record_id: United States v. Wade
  status: verified
  projected_at: 2026-07-06
---

# United States v. Wade

*388 U.S. 218 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Wade was indicted for bank robbery and counsel was appointed. Without notifying counsel, an FBI agent had Wade and other prisoners stand in a lineup — wearing strips of tape on their faces and repeating words used by the robber — so two bank employees could identify him. At trial, the two employees identified Wade in the courtroom, and on cross-examination it emerged that they had also identified him at the lineup. Wade argued that the uncounseled lineup violated his Fifth and Sixth Amendment rights.

## Issue
Whether a post-indictment lineup is a critical stage of the prosecution at which the accused has a Sixth Amendment right to counsel, and what remedy applies to an in-court identification that followed an uncounseled lineup.

## Rule
A post-indictment lineup is a critical stage at which the accused is entitled to counsel: "there can be little doubt that for Wade the post-indictment lineup was a critical stage of the prosecution at which he was 'as much entitled to such aid [of counsel] . . . as at the trial itself.'" — 388 U.S. at 237. ^pin-237

The remedy is not automatic exclusion of the in-court identification; the in-court identification is admissible only if it has a source independent of the tainted lineup. The Court [[Reading and Citing Cases#vacated|vacated]] the conviction "pending a hearing to determine whether the in-court identifications had an independent source." — 388 U.S. at 242. ^pin-242

## Application
Wade had been indicted and had counsel when the FBI conducted the lineup without notifying his lawyer; the lineup was therefore an uncounseled critical stage, violating Wade's Sixth Amendment right. Because the two bank employees' in-court identifications might have been tainted by that lineup, the proper course was to vacate the conviction and remand so the District Court could determine whether those identifications rested on an [[Inevitable Discovery and Independent Source|independent source]] (or whether their admission was harmless).

## Conclusion
The post-indictment lineup was a critical stage requiring counsel; the judgment of the Court of Appeals was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]] to determine whether the in-court identifications had an [[Inevitable Discovery and Independent Source|independent source]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The right recognized in *Wade* was later **limited** by [[Kirby v. Illinois]] (the right to counsel attaches only after the initiation of adversary judicial proceedings — no counsel at pre-charge lineups) and by [[United States v. Ash]] (no right to counsel at a photographic array). Within its domain — post-charge corporeal lineups — *Wade* remains good law, alongside its companion [[Gilbert v. California]].

## Appears on
- [[Eyewitness Identification]] — *Key — Anchor*

## Sources
- *United States v. Wade*, 388 U.S. 218 (1967) — https://www.courtlistener.com/opinion/107486/united-states-v-wade/ — pinpoints: 237, 242 (parallel 87 S. Ct. 1926).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3f2fb5d19fb2847f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Wade"}, "payload": {"all": [{"cite": "388 U.S. 218", "page": "218", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "388"}, {"cite": "87 S. Ct. 1926", "page": "1926", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "87"}, {"cite": "18 L. Ed. 2d 1149", "page": "1149", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "18"}, {"cite": "1967 U.S. LEXIS 1085", "page": "1085", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1967"}], "display": "388 U.S. 218", "official": {"cite": "388 U.S. 218", "page": "218", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "388"}, "official_selection_present": true, "record_id": "United States v. Wade"}}
{"assertion_id": "0b6b4ca01d560acf", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-242", "record_id": "United States v. Wade"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-242", "pinpoint_status": "slip-only", "quote": "pending a hearing to determine whether the in-court identifications had an independent source.", "quote_fidelity": "mismatch", "record_id": "United States v. Wade", "star_marker": null}}
{"assertion_id": "a098d7c8725bed3f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-237", "record_id": "United States v. Wade"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-237", "pinpoint_status": "slip-only", "quote": "--- # United States v. Wade *388 U.S. 218 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Wade was indicted for bank robbery and counsel was appointed. Without notifying counsel, an FBI agent had Wade and other prisoners stand in a lineup — wearing strips of tape on their faces and repeating words used by the robber — so two bank employees could identify him. At trial, the two employees identified Wade in the courtroom, and on cross-examination it emerged that they had also identified him at the lineup. Wade argued that the uncounseled lineup violated his Fifth and Sixth Amendment rights. ## Issue Whether a post-indictment lineup is a critical stage of the prosecution at which the accused has a Sixth Amendment right to counsel, and what remedy applies to an in-court identification that followed an uncounseled lineup. ## Rule A post-indictment lineup is a critical stage at which the accused is entitled to counsel:", "quote_fidelity": "mismatch", "record_id": "United States v. Wade", "star_marker": null}}
{"assertion_id": "3a38e10b60bb143f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Wade"}, "payload": {"as_of_content": "1967-06-12", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Wade", "scope_note": "Right-to-counsel reach later limited by Kirby v. Illinois (post-charge only) and United States v. Ash (no counsel at photo arrays).", "varies_by_point": false}}
```

### lake record — United States v. Wade

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Wade",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Wade",
    "case_name_short": "Wade",
    "case_name_full": "United States v. Wade",
    "input_case_name": "United States v. Wade",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-06-12",
    "year": 1967,
    "docket": null,
    "cluster_id": 107486,
    "lead_opinion_id": 9423472,
    "sibling_ids": [
      107486,
      9423472,
      9423473,
      9423474,
      9423475,
      9423476
    ],
    "absolute_url": "/opinion/107486/united-states-v-wade/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "388 U.S. 218",
      "volume": "388",
      "reporter": "U.S.",
      "page": "218",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 1926",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1926",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 1149",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "1149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 1085",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1085",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "388 U.S. 218",
        "volume": "388",
        "reporter": "U.S.",
        "page": "218",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 1926",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1926",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 1149",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "1149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 1085",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1085",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "388 U.S. 218",
    "official_selection": {
      "court_class": "scotus",
      "selected": "388 U.S. 218",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-237",
      "page": null,
      "quote": "--- # United States v. Wade *388 U.S. 218 (1967)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Wade was indicted for bank robbery and counsel was appointed. Without notifying counsel, an FBI agent had Wade and other prisoners stand in a lineup \u2014 wearing strips of tape on their faces and repeating words used by the robber \u2014 so two bank employees could identify him. At trial, the two employees identified Wade in the courtroom, and on cross-examination it emerged that they had also identified him at the lineup. Wade argued that the uncounseled lineup violated his Fifth and Sixth Amendment rights. ## Issue Whether a post-indictment lineup is a critical stage of the prosecution at which the accused has a Sixth Amendment right to counsel, and what remedy applies to an in-court identification that followed an uncounseled lineup. ## Rule A post-indictment lineup is a critical stage at which the accused is entitled to counsel:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-242",
      "page": null,
      "quote": "pending a hearing to determine whether the in-court identifications had an independent source.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1967-06-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Wade",
    "varies_by_point": false,
    "scope_note": "Right-to-counsel reach later limited by Kirby v. Illinois (post-charge only) and United States v. Ash (no counsel at photo arrays).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Red Kettle",
          "cluster_id": 4536563,
          "cite": [
            "2018 SD 66",
            "918 N.W.2d 393"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Turner v. United States",
          "cluster_id": 4480399,
          "cite": [
            "885 F.3d 949"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Dwight Smith",
          "cluster_id": 4452817,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane1_negative"
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
        "journal_ref": "United States v. Wade:lane2_top_cited"
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
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Simmons v. United States",
          "cluster_id": 107636,
          "cite": [
            "19 L. Ed. 2d 1247",
            "88 S. Ct. 967",
            "390 U.S. 377",
            "1968 U.S. LEXIS 2167"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
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
        "journal_ref": "United States v. Wade:lane2_top_cited"
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
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manson v. Brathwaite",
          "cluster_id": 109693,
          "cite": [
            "53 L. Ed. 2d 140",
            "97 S. Ct. 2243",
            "432 U.S. 98",
            "1977 U.S. LEXIS 116"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Padilla v. Kentucky",
          "cluster_id": 1723,
          "cite": [
            "176 L. Ed. 2d 284",
            "130 S. Ct. 1473",
            "559 U.S. 356",
            "2010 U.S. LEXIS 2928"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Young",
          "cluster_id": 111353,
          "cite": [
            "84 L. Ed. 2d 1",
            "105 S. Ct. 1038",
            "470 U.S. 1",
            "1985 U.S. LEXIS 49",
            "53 U.S.L.W. 4159"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
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
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Connelly",
          "cluster_id": 111779,
          "cite": [
            "93 L. Ed. 2d 473",
            "107 S. Ct. 515",
            "479 U.S. 157",
            "1986 U.S. LEXIS 23",
            "55 U.S.L.W. 4043"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baxter v. Rose",
          "cluster_id": 1769614,
          "cite": [
            "523 S.W.2d 930",
            "1975 Tenn. LEXIS 605"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
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
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moran v. Burbine",
          "cluster_id": 111614,
          "cite": [
            "89 L. Ed. 2d 410",
            "106 S. Ct. 1135",
            "475 U.S. 412",
            "1986 U.S. LEXIS 32",
            "54 U.S.L.W. 4265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lafler v. Cooper",
          "cluster_id": 625833,
          "cite": [
            "182 L. Ed. 2d 398",
            "132 S. Ct. 1376",
            "566 U.S. 156",
            "2012 U.S. LEXIS 2322"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nix v. Williams",
          "cluster_id": 111204,
          "cite": [
            "81 L. Ed. 2d 377",
            "104 S. Ct. 2501",
            "467 U.S. 431",
            "1984 U.S. LEXIS 101",
            "52 U.S.L.W. 4732"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kirby v. Illinois",
          "cluster_id": 108554,
          "cite": [
            "32 L. Ed. 2d 411",
            "92 S. Ct. 1877",
            "406 U.S. 682",
            "1972 U.S. LEXIS 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harrington v. California",
          "cluster_id": 107952,
          "cite": [
            "23 L. Ed. 2d 284",
            "89 S. Ct. 1726",
            "395 U.S. 250",
            "1969 U.S. LEXIS 1435"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brewer v. Williams",
          "cluster_id": 109624,
          "cite": [
            "51 L. Ed. 2d 424",
            "97 S. Ct. 1232",
            "430 U.S. 387",
            "1977 U.S. LEXIS 64"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Ritchie",
          "cluster_id": 111822,
          "cite": [
            "94 L. Ed. 2d 40",
            "107 S. Ct. 989",
            "480 U.S. 39",
            "1987 U.S. LEXIS 558",
            "55 U.S.L.W. 4180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
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
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. Frye",
          "cluster_id": 626055,
          "cite": [
            "182 L. Ed. 2d 379",
            "132 S. Ct. 1399",
            "566 U.S. 134",
            "2012 U.S. LEXIS 2321"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estelle v. Smith",
          "cluster_id": 110474,
          "cite": [
            "68 L. Ed. 2d 359",
            "101 S. Ct. 1866",
            "451 U.S. 454",
            "1981 U.S. LEXIS 95",
            "49 U.S.L.W. 4490"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
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
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hasting",
          "cluster_id": 110933,
          "cite": [
            "76 L. Ed. 2d 96",
            "103 S. Ct. 1974",
            "461 U.S. 499",
            "1983 U.S. LEXIS 31",
            "51 U.S.L.W. 4572"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
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
        "journal_ref": "United States v. Wade:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107486 OR 9423472 OR 9423473 OR 9423474 OR 9423475 OR 9423476) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTEwODc2ODAwMDAwJnM9NjIzOTE4NyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107486+OR+9423472+OR+9423473+OR+9423474+OR+9423475+OR+9423476%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107486 OR 9423472 OR 9423473 OR 9423474 OR 9423475 OR 9423476)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTU1JnM9MTEwMjMwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107486+OR+9423472+OR+9423473+OR+9423474+OR+9423475+OR+9423476%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107486 OR 9423472 OR 9423473 OR 9423474 OR 9423475 OR 9423476)",
        "reviewed": 68,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 68,
        "triage_read": 0,
        "triage_snippet_classified": 68
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107486 OR 9423472 OR 9423473 OR 9423474 OR 9423475 OR 9423476)",
    "indexed_citing_opinions": 5655,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107486,
        "count": 5272,
        "count_source": "search"
      },
      {
        "opinion_id": 9423472,
        "count": 545,
        "count_source": "search"
      },
      {
        "opinion_id": 9423473,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423474,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423475,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423476,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 8444,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-wade.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwNjQzNiZzPTEwMjcwNjI1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107486+OR+9423472+OR+9423473+OR+9423474+OR+9423475+OR+9423476%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107486,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 97290,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 102436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 103272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 103663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 103727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 105449,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 105566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 105597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107342,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107361,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 247981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 270482,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 271227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 273233,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 1143352,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 1176636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 1192333,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 1512648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 1550414,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 1748367,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 1780007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2023100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2023137,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2063045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2122471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2144553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2241740,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2340930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2609203,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2619179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 3416298,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 3484258,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 3609080,
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
    "date_created": "2026-07-06T03:26:40Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:27:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:27:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:30:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:27:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Wade

```
<opinion type="majority">
<author id="b255-11">Mr. Justice Brennan</author>
<p id="ARz">delivered the opinion of the Court.</p>
<p id="b255-12">The question here is whether courtroom identifications of an accused at trial are to be excluded from evidence because the accused was exhibited to the witnesses before trial at a post-indictment lineup conducted for <page-number citation-index="1" label="220">*220</page-number>identification purposes without notice to and in the absence of the accused’s appointed counsel.</p>
<p id="b256-5">The federally insured bank in Eustace, Texas, was robbed on September 21, 1964. A man with a small strip of tape on each side of his face entered the bank, pointed a pistol at the female cashier and the vice president, the only persons in the bank at the time, and forced them to fill a pillowcase with the bank’s money. The man then drove away with an accomplice who had been waiting in a stolen car outside the bank. On March 23, 1965, an indictment was returned against respondent, Wade, and two others for conspiring to rob the bank, and against Wade and the accomplice for the robbery itself. Wade was arrested on April 2, and counsel was appointed to represent him on April 26. Fifteen days later an FBI agent, without notice to Wade’s lawyer, arranged to have the two bank employees observe a lineup made up of Wade and five or six other prisoners and conducted in a courtroom of the local county courthouse. Each person in the line wore strips of tape such as allegedly worn by the robber and upon direction each said something like "put the money in the bag,” the words allegedly uttered by the robber. Both bank employees identified Wade in the lineup as the bank robber.</p>
<p id="b256-6">At trial, the two employees, when asked on direct examination if the robber was in the courtroom, pointed to Wade. The prior lineup identification was then elicited from both employees on cross-examination. At the close of testimony, Wade’s counsel moved for a judgment of acquittal or, alternatively, to strike the bank officials’ courtroom identifications on the ground that conduct of the lineup, without notice to and in the absence of his appointed counsel, violated his Fifth Amendment privilege against self-incrimination and his Sixth Amendment right to the assistance of counsel. The motion was denied, and Wade was convicted. The <page-number citation-index="1" label="221">*221</page-number>Court of Appeals for the Fifth Circuit reversed the conviction and ordered a new trial at which the in-court identification evidence was to be excluded, holding that, though the lineup did not violate Wade’s Fifth Amendment rights, “the lineup, held as it was, in the absence of counsel, already chosen to represent appellant, was a violation of his Sixth Amendment rights . . . .” <span class="citation" data-id="9451495"><a href="/opinion/271227/billy-joe-wade-v-united-states/#560" aria-description="Citation for case: Billy Joe Wade v. United States">358 F. 2d 557, 560</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./385/811/">385 U. S. 811</a></span>, and set the case for oral argument with No. 223, <em>Gilbert </em>v. <em>California, post, </em>p. 263, and No. 254, <em>Stovall </em>v. <em>Denno, post, </em>p. 293, which present similar questions. We reverse the judgment of the Court of Appeals and remand to that court with direction to enter a new judgment vacating the conviction and remanding the case to the District Court for further proceedings consistent with this opinion.</p>
<p id="b257-6">I.</p>
<p id="b257-7">Neither the lineup itself nor anything shown by this record that'Wade was required to do in the lineup violated his privilege against self-incrimination. We have only recently reaffirmed that the privilege “protects an accused only from being compelled to testify against himself, or otherwise provide the State with evidence of a testimonial or communicative nature ....” <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#761" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 761</a></span>. We there held that compelling a suspect to submit to a withdrawal of a sample of his blood for analysis for alcohol content and the admission in evidence of the analysis report were not compulsion to those ends. That holding was supported by the opinion in <em>Holt </em>v. <em>United States, </em><span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/" aria-description="Citation for case: Holt v. United States">218 U. S. 245</a></span>, in which case a question arose as to whether a blouse belonged to the defendant. A witness testified at trial that the defendant put on the blouse and it had fit him. The defendant argued that the admission of the testimony was error because compelling him to put on the blouse was a violation of his privilege. The Court <page-number citation-index="1" label="222">*222</page-number>rejected the claim as “an extravagant extension of the Fifth Amendment,” Mr. Justice Holmes saying for the Court:</p>
<blockquote id="b258-6">“[T]he prohibition of compelling a man in a criminal court to be witness against himself is a prohibition of the use of physical or moral compulsion to extort communications from him, not an exclusion of his body as evidence when it may be material.” <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/#252" aria-description="Citation for case: Holt v. United States">218 U. S., at 252-253</a></span>.</blockquote>
<p id="b258-7">The Court in <em><span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/" aria-description="Citation for case: Holt v. United States">Holt</a></span>, </em>however, put aside any constitutional questions which might be involved in compelling an accused, as here, to exhibit himself before victims of or witnesses to an alleged crime; the Court stated, “we need not consider how far a court would go in compelling a man to exhibit himself.” <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/#253" aria-description="Citation for case: Holt v. United States"><em>Id., </em>at 253</a></span>.<footnotemark>1</footnotemark></p>
<p id="b258-8">We have no doubt that compelling the accused merely to exhibit his person for observation by a prosecution witness prior to trial involves no compulsion of the accused to give evidence having testimonial significance. It is compulsion of the accused to exhibit his physical characteristics, not compulsion to disclose any knowledge he might have. It is no different from compelling Schmerber to provide a blood sample or Holt to wear the blouse, and, as in those instances, is not within the cover of the privilege. Similarly, compelling Wade to speak within hearing distance of the witnesses, even to utter words purportedly uttered by the robber, was not compulsion to utter statements of a “testimonial” nature; he was required to use his voice as an identifying <page-number citation-index="1" label="223">*223</page-number>physical characteristic, not to speak his guilt. We held in <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#761" aria-description="Citation for case: Schmerber v. California"><em>Schmerber, supra, </em>at 761</a></span>, that the distinction to be drawn under the Fifth Amendment privilege against self-incrimination is one between an accused’s “communications” in whatever form, vocal or physical, and “compulsion which makes a suspect or accused the source of ‘real or physical evidence,’ ” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#764" aria-description="Citation for case: Schmerber v. California"><em>Schmerber, supra, </em>at 764</a></span>. We recognized that “both federal and state courts have usually held that . . . [the privilege] offers no protection against compulsion to submit to' fingerprinting, photography, or measurements, to write or speak for identification, to appear in court, to stand, to assume a stance, to walk, or to make a particular gesture.” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#764" aria-description="Citation for case: Schmerber v. California"><em>Id., </em>at 764</a></span>. None of these activities becomes testimonial within the scope of the privilege because required of the accused in a pretrial lineup.</p>
<p id="b259-5">Moreover, it deserves emphasis that this case presents no question of the admissibility in evidence of anything Wade said or did at the lineup which implicates his privilege. The Government offered no such evidence as part of its case, and what came out about the lineup proceedings on Wade’s cross-examination of the bank employees involved no violation of Wade’s privilege.</p>
<p id="b259-6">II.</p>
<p id="b259-7">The fact that the lineup involved no violation of Wade’s privilege against self-incrimination does not, however, dispose of his contention that the courtroom identifications should have been excluded because the lineup was conducted without notice to and in the absence of his counsel. Our rejection of the right to counsel claim in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>rested on our conclusion in that case that “[n]o issue of counsel’s ability to assist petitioner in respect of any rights he did possess is presented.” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#766" aria-description="Citation for case: Schmerber v. California">384 U. S., at 766</a></span>. In contrast, in this case it is urged that the assistance of counsel at the lineup was indispensable <page-number citation-index="1" label="224">*224</page-number>to protect Wade’s most basic right as a criminal defendant — his right- to a fair trial at which the witnesses against him might be meaningfully cross-examined.</p>
<p id="b260-4">The Framers of the Bill of Rights envisaged a broader role for counsel than under the practice then prevailing in England of merely advising his client in “matters of law,” and eschewing any responsibility for “matters of fact.” <footnotemark>2</footnotemark> The constitutions in at least 11 of the 13 States expressly or impliedly abolished this distinction. <em>Powell </em>v. <em>Alabama, </em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#60" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45, 60-65</a></span>; Note, 73 Yale L. J. 1000, 1030-1033 (1964). “Though the colonial provisions about counsel were in accord on few things, they agreed on the necessity of abolishing the facts-law distinction; the colonists appreciated that if a defendant were forced to stand alone against the state, his case was foredoomed.” 73 Yale L. <span class="citation" data-id="9451495"><a href="/opinion/271227/billy-joe-wade-v-united-states/#1033" aria-description="Citation for case: Billy Joe Wade v. United States">J., <em>supra, </em>at 1033-1034</a></span>. This background is reflected in the scope given by our decisions to the Sixth Amendment’s guarantee to an accused of the assistance of counsel for his defense. When the Bill of Rights was adopted, there were no organized police forces as we know them today.<footnotemark>3</footnotemark> The accused confronted the prosecutor and the witnesses against him, and the evidence was marshalled, largely at the trial itself. In contrast, today’s law enforcement machinery involves critical confrontations of the accused by the prosecution at pretrial proceedings where the results might well settle the accused’s fate and reduce the trial itself to a mere formality. In recognition of these realities of modern criminal prosecution, our cases have construed the Sixth Amendment guarantee to apply to “critical” stages of the proceedings. The guarantee reads: “In all criminal <page-number citation-index="1" label="225">*225</page-number>prosecutions, the accused shall enjoy the right ... to have the Assistance of Counsel <em>for his defence.” </em>(Emphasis supplied.) The plain wording of this guarantee thus encompasses counsel’s assistance whenever necessary to assure a meaningful “defence.”</p>
<p id="b261-5">As early as <em>Powell </em>v. <em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">Alabama, supra,</a></span> </em>we recognized that the period from arraignment to trial was “perhaps the most critical period of the proceedings . . . ,” <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#57" aria-description="Citation for case: Powell v. Alabama"><em>id., </em>at 57</a></span>, during which the accused “requires the guiding hand of counsel. . .,” <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#69" aria-description="Citation for case: Powell v. Alabama"><em>id., </em>at 69</a></span>, if the guarantee is not to prove an empty right. That principle has since been applied to require the assistance of counsel at the type of arraignment — for example, that provided by Alabama — where certain rights might be sacrificed or lost: “What happens there may affect the whole trial. Available defenses may be irretrievably lost, if not then and there asserted . . . .” <em>Hamilton </em>v. <em>Alabama, </em><span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/#54" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52, 54</a></span>. See <em>White </em>v. <em>Maryland, </em><span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span>. The principle was also applied in <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span>, where we held that incriminating statements of the defendant should have been excluded from evidence when it appeared that they were overheard by federal agents who, without notice to the defendant’s lawyer, arranged a meeting between the defendant and an accomplice turned informant. We said, quoting a concurring opinion in <em>Spano </em>v. <em>New York, </em><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#326" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 326</a></span>, that “[a]nything less . . . might deny a defendant ‘effective representation by counsel at the only stage when legal aid and advice would help him.’ ” <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#204" aria-description="Citation for case: Massiah v. United States">377 U. S., at 204</a></span>.</p>
<p id="b261-6">In <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span>, we drew upon the rationale of <em><span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">Hamilton</a></span> </em>and <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>in holding that the right to counsel was guaranteed at the point where the accused, prior to arraignment, was subjected to secret interrogation despite repeated requests to see his lawyer. We again noted the necessity of counsel’s pres<page-number citation-index="1" label="226">*226</page-number>ence if the accused was to have a fair opportunity to present a defense at the trial itself:</p>
<blockquote id="b262-6">“The rule sought by the State here, however, would make the trial no more than an appeal from the interrogation; and the ‘right to use counsel at the formal trial [would be] a very hollow thing [if], for all practical purposes, the conviction is already assured by pretrial examination’.... ‘One can imagine a cynical prosecutor saying: “Let them have the most illustrious counsel, now. They can’t escape the noose. There is nothing that counsel can do for them at the trial.” ’ ” <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#487" aria-description="Citation for case: Escobedo v. Illinois">378 U. S., at 487-488</a></span>.</blockquote>
<p id="b262-7">Finally in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, the rules established for custodial interrogation included the right to the presence of counsel. The result was rested on our finding that this and the other rules were necessary to safeguard the privilege against self-incrimination from being jeopardized by such interrogation.</p>
<p id="b262-8">Of course, nothing decided or said in the opinions in the cited cases links the right to counsel only to protection of Fifth Amendment rights. Rather those decisions “no more than reflect a constitutional principle established as long ago as <em>Powell </em>v. <em>Alabama </em>. . . .” <em>Massiah </em>v. <em>United States, supra, </em>at 205. It is central to that principle that in addition to counsel’s presence at trial,<footnotemark>4</footnotemark> the accused is guaranteed that he need not stand alone against the State at any stage of the prosecution, formal or informal, in court or out, where counsel’s absence might derogate from the accused’s right to a fair trial.<footnotemark>5</footnotemark> The security of that right is as much the aim of the right to counsel as it is of the other guarantees of the <page-number citation-index="1" label="227">*227</page-number>Sixth Amendment — the right of the accused to a speedy and public trial by an impartial jury, his right to be informed of the nature and cause of the accusation, and his right to be confronted with the witnesses against him and to have compulsory process for obtaining witnesses in his favor. The presence of counsel at such critical confrontations, as at the trial itself, operates to assure that the accused’s interests will be protected consistently with our adversary theory of criminal prosecution. Cf. <em>Pointer </em>v. <em>Texas, </em><span class="citation" data-id="9422988"><a href="/opinion/107014/pointer-v-texas/" aria-description="Citation for case: Pointer v. Texas">380 U. S. 400</a></span>.</p>
<p id="b263-6">In sum, the principle of <em>Powell </em>v. <em>Alabama </em>and succeeding cases requires that we scrutinize <em>any </em>pretrial confrontation of the accused to determine whether the presence of his counsel is necessary to preserve the defendant’s basic right to a fair trial as affected by his right meaningfully to cross-examine the witnesses against him and to have effective assistance of counsel at the trial itself. It calls upon us to analyze whether potential substantial prejudice to defendant’s rights inheres in the particular confrontation and the ability of counsel to help avoid that prejudice.</p>
<p id="b263-7">III.</p>
<p id="b263-8">The Government characterizes the lineup as a mere preparatory step in the gathering of the prosecution’s evidence, not different — for Sixth Amendment purposes — from various other preparatory steps, such as systematized or scientific analyzing of the accused’s fingerprints, blood sample, clothing, hair, and the like. We think there are differences which preclude such stages being characterized as critical stages at which the accused has the right to the presence of his counsel. Knowledge of the techniques of science and technology is sufficiently available, and the variables in techniques few enough, that the accused has the opportunity for a meaningful confrontation of the Government’s case at <page-number citation-index="1" label="228">*228</page-number>trial through the ordinary processes of cross-examination of the Government's expert witnesses and the presentation of the evidence of his own experts. The denial of a right to have his counsel present at such analyses does not therefore violate the Sixth Amendment; they are not critical stages since there is minimal risk that his counsel's absence at such stages might derogate from his right to a fair trial.</p>
<p id="b264-5">IV.</p>
<p id="b264-6">But the confrontation compelled by the State between the accused and the victim or witnesses to a crime to elicit identification evidence is peculiarly riddled with innumerable dangers and variable factors which might seriously, even crucially, derogate from a fair trial. The vagaries of eyewitness identification are well-known; the annals of criminal law are rife with instances of mistaken identification.<footnotemark>6</footnotemark> Mr. Justice Frankfurter once said: “What is the worth of identification testimony even when uncontradicted? The identification of strangers is proverbially untrustworthy. The hazards of such testimony are established by a formidable number of instances in the records of English and American trials. These instances are recent — not due to the brutalities of ancient criminal procedure.” The Case of Sacco and Vanzetti 30 (1927). A major factor contributing to the high incidence of miscarriage of justice from mistaken identification has been the degree of suggestion inherent in the manner in which the prosecution presents the suspect to witnesses for pretrial identification. A commenta<page-number citation-index="1" label="229">*229</page-number>tor has observed that “[t]he influence of improper suggestion upon identifying witnesses probably accounts for more miscarriages of justice than any other single factor — ■ perhaps it is responsible for more such errors than all other factors combined.” Wall, Eye-Witness Identification in Criminal Cases 26. Suggestion can be created intentionally or unintentionally in many subtle ways.<footnotemark>7</footnotemark> And the dangers for the suspect are particularly grave when the witness’ opportunity for observation was insubstantial, and thus his susceptibility to suggestion the greatest.</p>
<p id="b265-5">Moreover, “[i]t is a matter of common experience that, once a witness has picked out the accused at the line-up, he is not likely to go back on his word later on, so that in practice the issue of identity may (in the absence of other relevant evidence) for all practical purposes be determined there and then, before the trial.” <footnotemark>8</footnotemark></p>
<p id="b265-6">The pretrial confrontation for purpose of identification may take the form of a lineup, also known as an “identification parade” or “showup,” as in the present case, or presentation of the suspect alone to the witness, as in <em>Stovall </em>v. <em>Denno, supra. </em>It is obvious that risks of suggestion attend either form of confrontation and increase the dangers inhering in eyewitness identification.<footnotemark>9</footnotemark> But <page-number citation-index="1" label="230">*230</page-number>as is the case with secret interrogations, there is serious difficulty in depicting what transpires at lineups and other forms of identification confrontations. “Privacy results in secrecy and this in turn results in a gap in our knowledge as to what in fact goes on . . . .” <em>Miranda </em>v. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#448" aria-description="Citation for case: Miranda v. Arizona"><em>Arizona, supra, </em>at 448</a></span>. For the same reasons, the defense can seldom reconstruct the manner and mode of lineup identification for judge or jury at trial. Those participating in a lineup with the accused may often be police officers;<footnotemark>10</footnotemark> in any event, the participants’ names are rarely recorded or divulged at trial.<footnotemark>11</footnotemark> The impediments to an objective observation are increased when the victim is the witness. Lineups are prevalent in rape and robbery prosecutions and present a particular hazard that a victim’s understandable outrage may excite vengeful or spiteful motives.<footnotemark>12</footnotemark> In any event, neither witnesses nor lineup participants are apt to be alert for conditions prejudicial to the suspect. And if they were, it would likely be of scant benefit to the suspect since neither witnesses nor lineup participants are likely to be schooled in the detection of suggestive influences.<footnotemark>13</footnotemark> Improper in<page-number citation-index="1" label="231">*231</page-number>fluences may go undetected by a suspect, guilty or not, who experiences the emotional tension which we might expect in one being confronted with potential accusers.<footnotemark>14</footnotemark> Even when he does observe abuse, if he has a criminal record he may be reluctant to take the stand and open up the admission of prior convictions. Moreover, any protestations by the suspect of the fairness of the lineup made at trial are likely to be in vain;<footnotemark>15</footnotemark> the jury’s choice is between the accused’s unsupported version and that of the police officers present.<footnotemark>16</footnotemark> In short, the accused’s <page-number citation-index="1" label="232">*232</page-number>inability effectively to reconstruct at trial any unfairness that occurred at the lineup may deprive him of his only opportunity meaningfully to attack the credibility of the witness’ courtroom identification.</p>
<p id="b268-6">What facts have been disclosed in specific cases about the conduct of pretrial confrontations for identification illustrate both the potential for substantial prejudice to the accused at that stage and the need for its revelation at trial. A commentator provides some striking examples:</p>
<blockquote id="b268-7">“In a Canadian case . . . the defendant had been picked out of a line-up of six men, of which he was the only Oriental. In other cases, a black-haired suspect was placed among a group of light-haired persons, tall suspects have been made to stand with short non-suspects, and, in a case where the perpetrator of the crime was known to be a youth, a suspect under twenty was placed in a line-up with five other persons, all of whom were forty or over.” <footnotemark>17</footnotemark></blockquote>
<p id="b268-8">Similarly state reports, in the course of describing prior identifications admitted as evidence of guilt, reveal <page-number citation-index="1" label="233">*233</page-number>numerous instances of suggestive procedures, for example, that all in the lineup but the suspect were known to the identifying witness,<footnotemark>18</footnotemark> that the other participants in a lineup were grossly dissimilar in appearance to the suspect,<footnotemark>19</footnotemark> that only the suspect was required to wear distinctive clothing which the culprit allegedly wore,<footnotemark>20</footnotemark> that the witness is told by the police that they have caught the culprit after which the defendant is brought before the witness alone or is viewed in jail,<footnotemark>21</footnotemark> that the suspect is pointed out before or during a lineup,<footnotemark>22</footnotemark> and that the participants in the lineup are asked to try on an article of clothing which fits only the suspect.<footnotemark>23</footnotemark></p>
<p id="b269-5">The potential for improper influence is illustrated by the circumstances, insofar as they appear, surrounding the prior identifications in the three cases we decide today. In the present case, the testimony of the identi<page-number citation-index="1" label="234">*234</page-number>fying witnesses elicited on cross-examination revealed that those witnesses were taken to the courthouse and seated in the courtroom to await assembly of the lineup. The courtroom faced on a hallway observable to the witnesses through an open door. The cashier testified that she saw Wade “standing in the hall” within sight of an FBI agent. Five or six other prisoners later appeared in the hall. The vice president testified that he saw a person in the hall in the custody of the agent who “resembled the person that we identified as the one that had entered the bank.” <footnotemark>24</footnotemark></p>
<p id="b270-6">The lineup in <em>Gilbert, supra, </em>was conducted in an auditorium in which some 100 witnesses to several alleged state and federal robberies charged to Gilbert made wholesale identifications of Gilbert as the robber in each other’s presence, a procedure said to be fraught with dangers of suggestion.<footnotemark>25</footnotemark> And the vice of suggestion created by the identification in <em>Stovall, supra, </em>was the presentation to the witness of the suspect alone handcuffed to police officers. It is hard to imagine a situation more clearly conveying the suggestion to the witness that the one presented is believed guilty by the police. See Frankfurter, The Case of Sacco and Vanzetti 31-32.</p>
<p id="b270-7">The few cases that have surfaced therefore reveal the existence of a process attended with hazards of serious unfairness to the criminal accused and strongly suggest the plight of the more numerous defendants who are unable to ferret out suggestive influences in the <page-number citation-index="1" label="235">*235</page-number>secrecy of the confrontation. We do not assume that these risks are the result of police procedures intentionally designed to prejudice an accused. Rather we assume they derive from the dangers inherent in eyewitness identification and the suggestibility inherent in the context of the pretrial identification. Williams &amp; Hammelmann, in one of the most comprehensive studies of such forms of identification, said, “[T]he fact that the police themselves have, in a given case, little or no doubt that the man put up for identification has committed the offense, and that their chief pre-occupation is with the problem of getting sufficient proof, because he has not 'come clean,’ involves a danger that this persuasion may communicate itself even in a doubtful case to the witness in some way . . . .” Identification Parades, Part I, [1963] Crim. L. Rev. 479, 483.</p>
<p id="b271-5">Insofar as the accused’s conviction may rest on a courtroom identification in fact the fruit of a suspect pretrial identification which the accused is helpless to subject to effective scrutiny at trial, the accused is deprived of that right of cross-examination which is an essential safeguard to his right to confront the witnesses against him. <em>Pointer </em>v. <em>Texas, </em><span class="citation" data-id="9422988"><a href="/opinion/107014/pointer-v-texas/" aria-description="Citation for case: Pointer v. Texas">380 U. S. 400</a></span>. And even though cross-examination is a precious safeguard to a fair trial, it cannot be viewed as an absolute assurance of accuracy and reliability. Thus in the present context, where so many variables and pitfalls exist, the first line of defense must be the prevention of unfairness and the lessening of the hazards of eyewitness identification at the lineup itself. The trial which might determine the accused’s fate may well not be that in the courtroom but that at the pretrial confrontation, with the State aligned against the accused, the witness the sole jury, and the accused unprotected against the overreaching, intentional or unintentional, and with little or no <page-number citation-index="1" label="236">*236</page-number>effective appeal from the judgment there rendered by the witness — “that’s the man.”</p>
<p id="b272-6">Since it appears that there is grave potential for prejudice, intentional or not, in the pretrial lineup, which may not be capable of reconstruction at trial, and since presence of counsel itself can often avert prejudice and assure a meaningful confrontation at trial,<footnotemark>26</footnotemark> there can be <page-number citation-index="1" label="237">*237</page-number>little doubt that for Wade the post-indictment lineup was a critical stage of the prosecution at which he was “as much entitled to such aid [of counsel] ... as at the trial itself.” <em>Powell </em>v. <em>Alabama, </em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#57" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45, 57</a></span>. Thus both Wade and his counsel should have been notified of the impending lineup, and counsel’s presence should have been a requisite to conduct of the lineup, absent an “intelligent waiver.” See <em>Carnley </em>v. <em>Cochran, </em><span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/" aria-description="Citation for case: Carnley v. Cochran">369 U. S. 506</a></span>. No substantial countervailing policy considerations have been advanced against the requirement of the presence of counsel. Concern is expressed that the requirement will forestall prompt identifications and result in obstruction of the confrontations. As for the first, we note that in the two cases in which the right to counsel is today held to apply, counsel had already been appointed and no argument is made in either case that notice to counsel would have prejudicially delayed the confrontations. Moreover, we leave open the question whether the presence of substitute counsel might not suffice where notification and presence of the suspect’s own counsel would result in prejudicial delay.<footnotemark>27</footnotemark> And to refuse to recognize the right to counsel for fear that counsel will obstruct the course of justice is contrary to the <page-number citation-index="1" label="238">*238</page-number>basic assumptions upon which this Court has operated in Sixth Amendment cases. We rejected similar logic in <em>Miranda </em>v. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona</a></span> </em>concerning presence of counsel during custodial interrogation, 384 U. S., at 480-481:</p>
<blockquote id="b274-4">“[A]n attorney is merely exercising the good professional judgment he has been taught. This is not cause for considering the attorney a menace to law enforcement. He is merely carrying out what he is sworn to do under his oath — to protect to the extent of his ability the rights of his client. In fulfilling this responsibility the attorney plays a vital role in the administration of criminal justice under our Constitution.”</blockquote>
<p id="b274-5">In our view counsel can hardly impede legitimate law enforcement; on the contrary, for the reasons expressed, law enforcement may be assisted by preventing the infiltration, of taint in the prosecution’s identification evidence.<footnotemark>28</footnotemark> That result cannot help the guilty avoid conviction but can only help assure that the right man has been brought to justice.<footnotemark>29</footnotemark></p>
<p id="b275-3"><page-number citation-index="1" label="239">*239</page-number>Legislative or other regulations, such as those of local police departments, which eliminate the risks of abuse and unintentional suggestion at lineup proceedings and the impediments to meaningful confrontation at trial may also remove the basis for regarding the stage as “critical.”<footnotemark>30</footnotemark> But neither Congress nor the federal authorities have seen fit to provide a solution. What we hold today “in no way creates a constitutional straitjacket which will handicap sound efforts at reform, nor is it intended to have this effect.” <em>Miranda </em>v. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><em>Arizona, supra, </em>at 467</a></span>.</p>
<p id="b275-4">V.</p>
<p id="b275-5">We come now to the question whether the denial of Wade’s motion to strike the courtroom identification by the bank witnesses at trial because of the absence of his counsel at the lineup required, as the Court of Appeals held, the grant of a new trial at which such evidence is <page-number citation-index="1" label="240">*240</page-number>to be excluded. We do not think this disposition can be justified without first giving the Government the opportunity to establish by clear and convincing evidence that the in-court identifications were based upon observations of the suspect other than the lineup identification. See <em>Murphy </em>v. <em>Waterfront Commission, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#79" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 79, n. 18</a></span>.<footnotemark>31</footnotemark> Where, as here, the admissibility of evidence of the lineup identification itself is not involved, a <em>per se </em>rule of exclusion of courtroom identification would be unjustified.<footnotemark>32</footnotemark> See <em>Nardone </em>v. <em>United States, </em><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span>. A rule limited solely to the exclusion of testimony concerning identification at the lineup itself, without regard to admissibility of the courtroom identification, would render the right to counsel an empty one. The lineup is most often used, as in the present case, to crystallize the witnesses’ identification of the defendant for future reference. We have already noted that the lineup identification will have that effect. The State may then rest upon the witnesses’ unequivocal courtroom identification, and not mention the pretrial identification as part of the State’s case at trial. Counsel is then in the predicament in which Wade’s counsel found himself — realizing that possible unfairness at the lineup may be the sole means of attack upon the unequivocal courtroom identification, and having to probe in the dark <page-number citation-index="1" label="241">*241</page-number>in an attempt to discover and reveal unfairness, whde bolstering the government witness’ courtroom identification by bringing out and dwelling upon his prior identification. Since counsel’s presence at the lineup would equip him to attack not only the lineup identification but the courtroom identification as well, limiting the impact of violation of the right to counsel to exclusion of evidence only of identification at the lineup itself disregards a critical element of that right.</p>
<p id="b277-3">We think it follows that the proper test to be applied in these situations is that quoted in <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 488</a></span>, “ ‘[W]hether, granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint." Maguire, Evidence of Guilt 221 (1959).” See also <em>Hoffa </em>v. <em>United States, </em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#309" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 309</a></span>. Application of this test in the present context requires consideration of various factors; for example, the prior opportunity to observe the alleged criminal act, the existence of any discrepancy between any pre-lineup description and the defendant’s actual description, any identification prior to lineup of another person, the identification by picture of the defendant prior to the lineup, failure to identify the defendant on a prior occasion, and the lapse of time between the alleged act and the lineup identification. It is also relevant to consider those facts which, despite the absence of counsel, are disclosed concerning the conduct of the lineup.<footnotemark>33</footnotemark></p>
<p id="b278-4"><page-number citation-index="1" label="242">*242</page-number>We doubt that the Court of Appeals applied the prop'er test for exclusion of the in-court identification of the two witnesses. The court stated that “it cannot be said with any certainty that they would have recognized appellant at the time of trial if this intervening lineup had not occurred,” and that the testimony of the two witnesses “may well have been colored by the illegal procedure [and] was prejudicial.” <span class="citation" data-id="9451495"><a href="/opinion/271227/billy-joe-wade-v-united-states/#560" aria-description="Citation for case: Billy Joe Wade v. United States">358 F. 2d, at 560</a></span>. Moreover, the court was persuaded, in part, by the “compulsory verbal responses made by Wade at the instance of the Special Agent.” <em><span class="citation" data-id="9451495"><a href="/opinion/271227/billy-joe-wade-v-united-states/" aria-description="Citation for case: Billy Joe Wade v. United States">Ibid.</a></span> </em>This implies the erroneous holding that Wade’s privilege against self-incrimination was violated so that the denial of counsel required exclusion.</p>
<p id="b278-5">On the record now before us we cannot make the determination whether the in-court identifications had an independent origin. This was not an issue at trial, although there is some evidence relevant to a determination. That inquiry is most properly made in the District Court. We therefore think the appropriate procedure to be followed is to vacate the conviction pending a hearing to determine whether the in-court identifications had an independent source, or whether, in any event, the introduction of the evidence was harmless error, <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span>, and for the District Court to reinstate the conviction or order a new trial, as may be proper. See <em>United States </em>v. <em>Shotwell Mfg. Co., </em><span class="citation" data-id="9421525"><a href="/opinion/105597/united-states-v-shotwell-manufacturing-co/#245" aria-description="Citation for case: United States v. Shotwell Manufacturing Co.">355 U. S. 233, 245-246</a></span>.</p>
<p id="b279-4"><page-number citation-index="1" label="243">*243</page-number>The judgment of the Court of Appeals is vacated and the case is remanded to that court with direction to enter a new judgment vacating the conviction and remanding the case to the District Court for further proceedings consistent with this opinion.</p>
<p id="b279-5">
<em>It is so ordered.</em>
</p>
<judges id="b279-6">The Chief Justice joins the opinion of the Court except for Part I, from which he dissents for the reasons expressed in the opinion of Mr. Justice Foutas.</judges>
<judges id="b279-7">Mr. Justice Douglas joins the opinion of the Court except for Part I. On that phase of the case he adheres to the dissenting views in <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#772" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 772-779</a></span>, since he believes that compulsory lineup violates the privilege against self-incrimination contained in the Fifth Amendment.</judges>
<footnote label="1">
<p id="b258-9"><em> <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/" aria-description="Citation for case: Holt v. United States">Holt</a></span> </em>was decided before <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, fashioned the rule excluding illegally obtained evidence in a federal prosecution. The Court therefore followed <em>Adams </em>v. <em>New York, </em><span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U. S. <em>585, </em></a></span>in holding that, in any event, “when he is exhibited, whether voluntarily or by order, and even if the order goes too far, the evidence, if material,'is competent.” <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/#253" aria-description="Citation for case: Holt v. United States">218 U. S., at 253</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b260-5"> See <em>Powell </em>v. <em>Alabama, </em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#60" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45, 60-65</a></span>; Beaney, Right to Counsel in American Courts 8-26.</p>
</footnote>
<footnote label="3">
<p id="b260-6"> See Note, 73 Yale L. J. 1000, 1040-1042 (1964); Comment, <span class="citation no-link">53 Calif. L. Rev. 337</span>, 347-348 (1965).</p>
</footnote>
<footnote label="4">
<p id="b262-9"> See, <em>e. g., Powell </em>v. <em>Alabama, </em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>; <em>Hamilton </em>v. <em>Alabama, </em><span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span>; <em>White </em>v. <span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland"><em>Maryland, 373 </em>U. S. 59</a></span>; <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span>; <em>Massiah </em>v. <em>United States, 377 </em>U. S. 201.</p>
</footnote>
<footnote label="5">
<p id="b262-10"> See cases cited n. 4, <em>supra; Avery </em>v. <em>Alabama, </em><span class="citation" data-id="103272"><a href="/opinion/103272/avery-v-alabama/#446" aria-description="Citation for case: Avery v. Alabama">308 U. S. 444, 446</a></span>.</p>
</footnote>
<footnote label="6">
<p id="b264-7"> Borchard, Convicting the Innocent; Frank &amp; Frank, Not Guilty; Wall, Eye-Witness Identification in Criminal Cases; 3 Wigmore, Evidence § 786a (3d ed. 1940); Rolph, Personal Identity; Gross, Criminal Investigation 47-54 (Jackson ed. 1962); Williams, Proof of Guilt 83-98 (1955); Wills, Circumstantial Evidence 192-205 (7th ed. 1937); Wigmore, The Science of Judicial Proof §§ 250-253 (3d ed. 1937).</p>
</footnote>
<footnote label="7">
<p id="b265-7"> See Wall, <em>supra, </em>n. 6, at 26-65; Murray, The Criminal Lineup at Home and Abroad, <span class="citation no-link">1966 Utah L. Rev. 610</span>; Napley, Problems of Effecting the Presentation of the Case for a Defendant, 66 Col. L. Rev. 94, 98-99 (1966); Williams, Identification Parades, [1955] Crim. L. Rev. (Eng.) 525; Paul, Identification of Accused Persons, 12 Austl. L. J. 42 (1938); Houts, From Evidence to Proof 25; Williams &amp; Hammelmann, Identification Parades, Parts I &amp; II, [1963] Crim. L. Rev. 479-490, 545-555; Gorphe, Showing Prisoners to Witnesses for Identification, 1 Am. J. Police Sci. 79 (1930); Wigmore, The Science of Judicial Proof, <em>supra, </em>n. 6, at §253; Devlin, The Criminal Prosecution in England 70; Williams, Proof of Guilt 95-97.</p>
</footnote>
<footnote label="8">
<p id="b265-8"> Williams &amp; Hammelmann, Identification Parades, Part I, [1963] Crim. L. Rev. 479, 482.</p>
</footnote>
<footnote label="9">
<p id="b265-9"> Williams &amp; Hammelmann, Identification Parades, Part <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#7" aria-description="Citation for case: Escobedo v. Illinois">I, <em>supra, </em>n. 7</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b266-6"> See Wall, <em>supra, </em>n. 6, at 57-59; see, <em>e. g., People </em>v. <em>Boney, </em><span class="citation" data-id="2023100"><a href="/opinion/2023100/the-people-v-boney/" aria-description="Citation for case: The People v. Boney">28 Ill. 2d 505</a></span>, <span class="citation" data-id="2023100"><a href="/opinion/2023100/the-people-v-boney/" aria-description="Citation for case: The People v. Boney">192 N. E. 2d 920</a></span> (1963); <em>People </em>v. <em>James, </em><span class="citation" data-id="2215593"><a href="/opinion/2215593/people-v-james/" aria-description="Citation for case: People v. James">218 Cal. App. 2d 166</a></span>, <span class="citation" data-id="2215593"><a href="/opinion/2215593/people-v-james/" aria-description="Citation for case: People v. James">32 Cal. Rptr. 283</a></span> (1963).</p>
</footnote>
<footnote label="11">
<p id="b266-7"> See Rolph, Personal Identity 50: “The bright burden of identity, at these parades, is lifted from the innocent participants to hover about the suspect, leaving the rest featureless and unknown and without interest.”</p>
</footnote>
<footnote label="12">
<p id="b266-8"> See Williams &amp; Hammelmann, Identification Parades, Part II, [1963] Crim. L. Rev. 545, 546; Borchard, Convicting the Innocent 367.</p>
</footnote>
<footnote label="13">
<p id="b266-9"> An additional impediment to the detection of such influences by participants, including the suspect, is the physical conditions often surrounding the conduct of the lineup. In many, lights shine on the stage in such a way that the suspect cannot see the witness. See <em>Gilbert </em>v. <em>United States, </em><span class="citation" data-id="9452205"><a href="/opinion/273233/jesse-james-gilbert-v-united-states/" aria-description="Citation for case: Jesse James Gilbert v. United States">366 F. 2d 923</a></span> (C. A. 9th Cir. 1966). In some a one-way mirror is used and what is said on the witness’ <page-number citation-index="1" label="231">*231</page-number>side cannot be heard. See <em>Rigney </em>v. <em>Hendrick, </em><span class="citation" data-id="8874911"><a href="/opinion/8888781/rigney-v-hendrick/#711" aria-description="Citation for case: Rigney v. Hendrick">355 F. 2d 710, 711, n. 2</a></span> (C. A. 3d Cir. 1965); <em>Aaron </em>v. <em>State, </em><span class="citation" data-id="1143352"><a href="/opinion/1143352/aaron-v-state/" aria-description="Citation for case: Aaron v. State">273 Ala. 337</a></span>, <span class="citation" data-id="1143352"><a href="/opinion/1143352/aaron-v-state/" aria-description="Citation for case: Aaron v. State">139 So. 2d 309</a></span> (1961).</p>
</footnote>
<footnote label="14">
<p id="b267-6"> Williams &amp; Hammelmann, Part <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#7" aria-description="Citation for case: Escobedo v. Illinois">I, <em>supra, </em>n. 7</a></span>, at 489; Napley, <em>supra, </em>n. 7, at 99.</p>
</footnote>
<footnote label="15">
<p id="b267-7"> See <em>In re Groban, </em><span class="citation" data-id="9421372"><a href="/opinion/105449/in-re-groban/#340" aria-description="Citation for case: In Re Groban">352 U. S. 330, 340</a></span> (Black, J., dissenting). The difficult position of defendants in attempting to protest the manner of pretrial identification is illustrated by the many state court eases in which contentions of blatant abuse rested on their unsupportable allegations, usually controverted by the police officers present. See, e. <em>g., People </em>v. <em>Shields, </em><span class="citation" data-id="1170096"><a href="/opinion/1170096/people-v-shields/#634" aria-description="Citation for case: People v. Shields">70 Cal. App. 2d 628, 634-635</a></span>, <span class="citation" data-id="1170096"><a href="/opinion/1170096/people-v-shields/#478" aria-description="Citation for case: People v. Shields">161 P. 2d 475, 478-479</a></span> (1945); <em>People </em>v. <em>Hicks, </em><span class="citation" data-id="2122471"><a href="/opinion/2122471/the-people-v-hicks/" aria-description="Citation for case: The People v. Hicks">22 Ill. 2d 364</a></span>, <span class="citation" data-id="2122471"><a href="/opinion/2122471/the-people-v-hicks/" aria-description="Citation for case: The People v. Hicks">176 N. E. 2d 810</a></span> (1961); <em>State </em>v. <em>Hill, </em><span class="citation" data-id="9794721"><a href="/opinion/2619179/state-v-hill/" aria-description="Citation for case: State v. Hill">193 Kan. 512</a></span>, <span class="citation" data-id="9794721"><a href="/opinion/2619179/state-v-hill/" aria-description="Citation for case: State v. Hill">394 P. 2d 106</a></span> (1964); <em>Redmon </em>v. <em>Commonwealth, </em><span class="citation" data-id="2371331"><a href="/opinion/2371331/redmon-v-commonwealth/" aria-description="Citation for case: Redmon v. Commonwealth">321 S. W. 2d 397</a></span> (Ky. Ct. App. 1959); <em>Lubinski </em>v. <em>State, </em><span class="citation" data-id="3484258"><a href="/opinion/3486372/lubinski-v-state/#8" aria-description="Citation for case: Lubinski v. State">180 Md. 1, 8</a></span>, <span class="citation" data-id="3484258"><a href="/opinion/3486372/lubinski-v-state/#459" aria-description="Citation for case: Lubinski v. State">22 A. 2d 455, 459</a></span> (1941). For a striking case in which hardly anyone agreed upon what occurred at the lineup, including who identified whom, see <em>Johnson </em>v. <em>State, </em><span class="citation" data-id="1512648"><a href="/opinion/1512648/johnson-v-state/" aria-description="Citation for case: Johnson v. State">237 Md. 283</a></span>, <span class="citation" data-id="1512648"><a href="/opinion/1512648/johnson-v-state/" aria-description="Citation for case: Johnson v. State">206 A. 2d 138</a></span> (1965).</p>
</footnote>
<footnote label="16">
<p id="b267-8"> An instructive example of the defendant’s predicament may be found in <em>Proctor </em>v. <em>State, </em><span class="citation" data-id="1550414"><a href="/opinion/1550414/proctor-v-state/" aria-description="Citation for case: Proctor v. State">223 Md. 394</a></span>, <span class="citation" data-id="1550414"><a href="/opinion/1550414/proctor-v-state/" aria-description="Citation for case: Proctor v. State">164 A. 2d 708</a></span> (1960). A prior identification is admissible in Maryland only under the salutary rule that it cannot have been made “under conditions of unfairness or unreliability.” <span class="citation" data-id="1550414"><a href="/opinion/1550414/proctor-v-state/#401" aria-description="Citation for case: Proctor v. State"><em>Id., </em>at 401</a></span>, <span class="citation" data-id="1550414"><a href="/opinion/1550414/proctor-v-state/#712" aria-description="Citation for case: Proctor v. State">164 A. 2d, at 712</a></span>. Against the defendant’s contention that these conditions had not been met, the Court stated:</p>
<blockquote id="b267-9">“In the instant case, there are no such facts as, in our judgment, would call for a finding that the identification . . . was made under conditions of unfairness or unreliability. The relatively large number of persons put into the room together for [the victim] to look at <page-number citation-index="1" label="232">*232</page-number>is one circumstance indicating fairness, and the fact that the police officer was unable to remember the appearances of the others and could not recall if they had physical characteristics similar to [the defendant’s] or not is at least suggestive that they were not of any one type or that they all differed markedly in looks from the defendant. There is no evidence that the Police Sergeant gave the complaining witness any indication as to which of the thirteen men was the defendant; the Sergeant’s testimony is simply that he asked [the victim] if he could identify [the defendant] after having put the thirteen men in the courtroom.”</blockquote>
</footnote>
<footnote label="17">
<p id="b268-10"> Wall, Eye-Witness Identification in Criminal Cases 53. For other such examples see Houts, From Evidence to Proof 25; Frankfurter, The Case of Sacco and Vanzetti 12-14, 30-32; 3 Wigmore, Evidence § 786a, at 164, n. 2 (3d ed. 1940); Paul, Identification of Accused Persons, 12 Austl. L. J. 42, 44 (1938); Rolph, Personal Identity 34-43.</p>
</footnote>
<footnote label="18">
<p id="b269-6"> See <em>People </em>v. <em>James, </em><span class="citation" data-id="2215593"><a href="/opinion/2215593/people-v-james/#170" aria-description="Citation for case: People v. James">218 Cal. App. 2d 166, 170-171</a></span>, <span class="citation" data-id="2215593"><a href="/opinion/2215593/people-v-james/#286" aria-description="Citation for case: People v. James">32 Cal. Rptr. 283, 286</a></span> (1963); <em>People </em>v. <em>Boney, </em><span class="citation" data-id="2023100"><a href="/opinion/2023100/the-people-v-boney/" aria-description="Citation for case: The People v. Boney">28 Ill. 2d 505</a></span>, <span class="citation" data-id="2023100"><a href="/opinion/2023100/the-people-v-boney/" aria-description="Citation for case: The People v. Boney">192 N. E. 2d 920</a></span> (1963).</p>
</footnote>
<footnote label="19">
<p id="b269-9"> See <em>Fredericksen </em>v. <em>United States, </em>105 U. S. App. D. C. 262, <span class="citation" data-id="247981"><a href="/opinion/247981/charles-d-fredericksen-v-united-states/" aria-description="Citation for case: Charles D. Fredericksen v. United States">266 F. 2d 463</a></span> (1959); <em>People </em>v. <em>Adell, </em><span class="citation" data-id="2144553"><a href="/opinion/2144553/people-v-adell/" aria-description="Citation for case: People v. Adell">75 Ill. App. 2d 385</a></span>, <span class="citation" data-id="2144553"><a href="/opinion/2144553/people-v-adell/" aria-description="Citation for case: People v. Adell">221 N. E. 2d 72</a></span> (1966); <em>State </em>v. <em>Hill, </em><span class="citation" data-id="9794721"><a href="/opinion/2619179/state-v-hill/" aria-description="Citation for case: State v. Hill">193 Kan. 512</a></span>, <span class="citation" data-id="9794721"><a href="/opinion/2619179/state-v-hill/" aria-description="Citation for case: State v. Hill">394 P. 2d 106</a></span> (1964); <em>People </em>v. <em>Seppi, </em><span class="citation" data-id="3609080"><a href="/opinion/3626126/people-v-seppi/" aria-description="Citation for case: People v. . Seppi">221 N. Y. 62</a></span>, <span class="citation" data-id="3609080"><a href="/opinion/3626126/people-v-seppi/" aria-description="Citation for case: People v. . Seppi">116 N. E. 793</a></span> (1917); <em>State </em>v. <em>Duggan, </em><span class="citation" data-id="1299385"><a href="/opinion/1299385/state-v-duggan/#162" aria-description="Citation for case: State v. Duggan">215 Ore. 151, 162</a></span>, <span class="citation" data-id="1299385"><a href="/opinion/1299385/state-v-duggan/#912" aria-description="Citation for case: State v. Duggan">333 P. 2d 907, 912</a></span> (1958).</p>
</footnote>
<footnote label="20">
<p id="b269-10"> See <em>People </em>v. <em>Crenshaw, </em><span class="citation" data-id="2063045"><a href="/opinion/2063045/the-people-v-crenshaw/#460" aria-description="Citation for case: The PEOPLE v. Crenshaw">15 Ill. 2d 458, 460</a></span>, <span class="citation" data-id="2063045"><a href="/opinion/2063045/the-people-v-crenshaw/#602" aria-description="Citation for case: The PEOPLE v. Crenshaw">155 N. E. 2d 599, 602</a></span> (1959); <em>Presley </em>v. <em>State, </em><span class="citation" data-id="2340930"><a href="/opinion/2340930/presley-v-state/" aria-description="Citation for case: Presley v. State">224 Md. 550</a></span>, <span class="citation" data-id="2340930"><a href="/opinion/2340930/presley-v-state/" aria-description="Citation for case: Presley v. State">168 A. 2d 510</a></span> (1961); <em>State </em>v. <em>Ramirez, </em>76 N. M. 72, <span class="citation" data-id="1176636"><a href="/opinion/1176636/state-v-ramirez/" aria-description="Citation for case: State v. Ramirez">412 P. 2d 246</a></span> (1966); <em>State </em>v. <em>Bazemore, </em><span class="citation" data-id="3674765"><a href="/opinion/3928137/state-v-bazemore/" aria-description="Citation for case: State v. . Bazemore">193 N. C. 336</a></span>, <span class="citation no-link">137 S. E. 172</span> (1927); <em>Barrett </em>v. <em>State, </em><span class="citation" data-id="1780007"><a href="/opinion/1780007/barrett-v-state/" aria-description="Citation for case: Barrett v. State">190 Tenn. 366</a></span>, <span class="citation" data-id="1780007"><a href="/opinion/1780007/barrett-v-state/" aria-description="Citation for case: Barrett v. State">229 S. W. 2d 516</a></span> (1950).</p>
</footnote>
<footnote label="21">
<p id="b269-14"> See <em>Aaron </em>v. <em>State, </em><span class="citation" data-id="1143352"><a href="/opinion/1143352/aaron-v-state/" aria-description="Citation for case: Aaron v. State">273 Ala. 337</a></span>, <span class="citation" data-id="1143352"><a href="/opinion/1143352/aaron-v-state/" aria-description="Citation for case: Aaron v. State">139 So. 2d 309</a></span> (1961); <em>Bishop </em>v. <em>State, </em><span class="citation" data-id="1748367"><a href="/opinion/1748367/bishop-v-state/" aria-description="Citation for case: Bishop v. State">236 Ark. 12</a></span>, <span class="citation" data-id="1748367"><a href="/opinion/1748367/bishop-v-state/" aria-description="Citation for case: Bishop v. State">364 S. W. 2d 676</a></span> (1963); <em>People </em>v. <em>Thompson, </em><span class="citation" data-id="2241740"><a href="/opinion/2241740/people-v-thompson/" aria-description="Citation for case: People v. Thompson">406 Ill. 555</a></span>, <span class="citation" data-id="2241740"><a href="/opinion/2241740/people-v-thompson/" aria-description="Citation for case: People v. Thompson">94 N. E. 2d 349</a></span> (1950); <em>People </em>v. <em>Berne, </em><span class="citation" data-id="3416298"><a href="/opinion/3419836/the-people-v-berne/" aria-description="Citation for case: The People v. Berne">384 Ill. 334</a></span>, <span class="citation" data-id="3416298"><a href="/opinion/3419836/the-people-v-berne/" aria-description="Citation for case: The People v. Berne">51 N. E. 2d 578</a></span> (1943); <em>People </em>v. <em>Martin, </em><span class="citation" data-id="6980660"><a href="/opinion/7075921/people-v-martin/" aria-description="Citation for case: People v. Martin">304 Ill. 494</a></span>, <span class="citation" data-id="6980660"><a href="/opinion/7075921/people-v-martin/" aria-description="Citation for case: People v. Martin">136 N. E. 711</a></span> (1922); <em>Barrett </em>v. <em>State, </em><span class="citation" data-id="1780007"><a href="/opinion/1780007/barrett-v-state/" aria-description="Citation for case: Barrett v. State">190 Tenn. 366</a></span>, <span class="citation" data-id="1780007"><a href="/opinion/1780007/barrett-v-state/" aria-description="Citation for case: Barrett v. State">229 S. W. 2d 516</a></span> (1950).</p>
</footnote>
<footnote label="22">
<p id="b269-15"> See <em>People </em>v. <em>Clark, </em><span class="citation" data-id="2023137"><a href="/opinion/2023137/the-people-v-clark/" aria-description="Citation for case: The PEOPLE v. Clark">28 Ill. 2d 423</a></span>, <span class="citation" data-id="2023137"><a href="/opinion/2023137/the-people-v-clark/" aria-description="Citation for case: The PEOPLE v. Clark">192 N. E. 2d 851</a></span> (1963); <em>Gillespie </em>v. <em>State, </em><span class="citation" data-id="1192333"><a href="/opinion/1192333/gillespie-v-state/#454" aria-description="Citation for case: Gillespie v. State">355 P. 2d 451, 454</a></span> (Okla. Cr. 1960).</p>
</footnote>
<footnote label="23">
<p id="b269-16"> See <em>People </em>v. <em>Parham, </em><span class="citation" data-id="2609203"><a href="/opinion/2609203/people-v-parham/" aria-description="Citation for case: People v. Parham">60 Cal. 2d 378</a></span>, <span class="citation" data-id="2609203"><a href="/opinion/2609203/people-v-parham/" aria-description="Citation for case: People v. Parham">384 P. 2d 1001</a></span> (1963).</p>
</footnote>
<footnote label="24">
<p id="b270-8"> See Wall, <em>supra, </em>n. 6, at 48; Napley, <em>supra, </em>n. 7, at 99: “[W]hile many identification parades are conducted by the police with scrupulous regard for fairness, it is not unknown for the identifying witness to be placed in a position where he can see the suspect before the parade forms . . . .”</p>
</footnote>
<footnote label="25">
<p id="b270-9"> Williams &amp; Hammelmann, Part I, <em>supra, </em>n. 7, at 486; Burtt, Applied Psychology 254-255.</p>
</footnote>
<footnote label="26">
<p id="b272-7"> One commentator proposes a model statute providing not only for counsel, but other safeguards as well:</p>
<blockquote id="b272-8">“Most, if not all, of the attacks on the lineup process could be averted by a uniform statute modeled upon the best features of the civilian codes. Any proposed statute should provide for the right to counsel during any lineup or during any confrontation. Provision should be made that any person, whether a victim or a witness, must give a description of the suspect before he views any arrested person. A written record of this description should be required, and the witness should be made to sign it. This written record would be available for inspection by defense counsel for copying before the trial and for use at the trial in testing the accuracy of the identification made during the lineup and during the trial.</blockquote>
<blockquote id="b272-9">“This ideal statute would require at least six persons in addition to the accused in a lineup, and these persons would have to be of approximately the same height, weight, coloration of hair and skin, and bodily types as the suspect. In addition, all of these men should, as nearly as possible, be dressed alike. If distinctive garb was used during the crime, the suspect should not be forced to wear similar clothing in the lineup unless all of the other persons are similarly garbed. A complete written report of the names, addresses, descriptive details of the other persons in the lineup, and of everything which transpired during the identification would be mandatory. This report would include everything stated by the identifying witness during this step, including any reasons given by him as to what features, etc., have sparked his recognition.</blockquote>
<blockquote id="b272-10">“This statute should permit voice identification tests by having each person in the lineup repeat identical innocuous phrases, and it would be impermissible to force the use of words allegedly used during a criminal act.</blockquote>
<blockquote id="b272-11">“The statute would enjoin the police from suggesting to any viewer that one or more persons in the lineup had been arrested as a suspect. If more than one witness is to make an identification, each <page-number citation-index="1" label="237">*237</page-number>witness should be required to do so separately and should be forbidden to speak to another witness until all of them have completed the process.</blockquote>
<blockquote id="b273-6">“The statute could require the use of movie cameras and tape recorders to record the lineup process in those states which are financially able to afford these devices. Finally, the statute should provide that any evidence obtained as the result of a violation of this statute would be inadmissible.” Murray, The Criminal Lineup at Home and Abroad, <span class="citation no-link">1966 Utah L. Rev. 610</span>, 627-628.</blockquote>
</footnote>
<footnote label="27">
<p id="b273-7"><em> </em>Although the right to counsel usually means a right to the suspect’s own counsel, provision for substitute counsel may be justified on the ground that the substitute counsel’s presence may eliminate the hazards which render the lineup a critical stage for the presence of the suspect’s <em>own </em>counsel.</p>
</footnote>
<footnote label="28">
<p id="b274-6"> Concern is also expressed that the presence of counsel will force divulgence of the identity of government witnesses whose identity the Government may want to conceal. To the extent that this is a valid or significant state interest there are police practices commonly used to effect concealment, for example, masking the face.</p>
</footnote>
<footnote label="29">
<p id="b274-7"> Many other nations surround the lineup with safeguards against prejudice to the suspect. In England the suspect must be allowed the presence of his solicitor or a friend, Napley, <em>supra, </em>n. 7, at 98-99; Germany requires the presence of retained counsel; France forbids the confrontation of the suspect in the absence of his counsel; Spain, Mexico, and Italy provide detailed procedures prescribing the conditions under which confrontation must occur under the supervision of a judicial officer who sees to it that the proceedings are officially recorded to assure adequate scrutiny at trial. Murray, The Criminal Lineup at Home and Abroad, <span class="citation no-link">1966 Utah L. Rev. 610</span>, 621-627.</p>
</footnote>
<footnote label="30">
<p id="b275-6"> Thirty years ago Wigmore suggested a “scientific method” of pretrial identification “to reduce the risk of error hitherto inherent in such proceedings.” Wigmore, The Science of Judicial Proof 541 (3d ed. 1937). Under this approach, at least 100 talking films would be prepared of men from various occupations, races, etc. Each would be photographed in a number of stock movements, with and without hat and coat, and would read aloud a standard passage. The suspect would be filmed in the same manner. Some 25 of the films would be shown in succession in a special projection room in which each witness would be provided an electric button which would activate a board backstage when pressed to indicate that the witness had identified a given person. Provision would be made for the degree of hesitancy in the identification to be indicated by the number of presses. <em>Id., </em>at 540-541. Of course, the more systematic and scientific a process or proceeding, including one for purposes of identification, the less the impediment to reconstruction of the conditions bearing upon the reliability of that process or proceeding at trial. See discussion of fingerprint and like tests, Part III, <em>supra, </em>and of handwriting exemplars in <em>Gilbert </em>v. <em>California, supra.</em></p>
</footnote>
<footnote label="31">
<p id="b276-5"> See <em>Goldstein </em>v. <em>United States, </em><span class="citation" data-id="9419243"><a href="/opinion/103663/goldstein-v-united-states/#124" aria-description="Citation for case: Goldstein v. United States">316 U. S. 114, 124, n. 1</a></span> (Murphy, J., dissenting). “[A]fter an accused sustains the initial burden, imposed by <em>Nardone </em>v. <em>United States, </em><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">308 U. S. 338</a></span>, of proving to the satisfaction of the trial judge in the preliminary hearing that wire-tapping was unlawfully employed, as petitioners did here, it is only fair that the burden should then shift to the Government to convince the trial judge that its proof had an independent origin.”</p>
</footnote>
<footnote label="32">
<p id="b276-6"> We reach a contrary conclusion in <em>Gilbert </em>v. <em>California, supra, </em>as to the admissibility of the witness’ testimony that he also identified the accused at the lineup.</p>
</footnote>
<footnote label="33">
<p id="b277-4"> Thus it is not the case that “[i]t matters not how well the witness knows the suspect, whether the witness is the suspect’s mother, brother, or long-time associate, and no matter how long or well the witness observed the perpetrator at the scene of the crime.” Such factors will have an important bearing upon the true basis of <page-number citation-index="1" label="242">*242</page-number>the witness’ in-court identification. Moreover, the State’s inability to bolster the witness’ courtroom identification by introduction of the lineup identification.itself, see <em>Gilbert </em>v. <em>California, supra, </em>will become less significant the more the evidence of other opportunities of the witness to observe the defendant. Thus where the witness is a “kidnap victim who has lived for days with his abductor” the value to the State of admission of the lineup identification is indeed marginal, and such identification would be a mere formality.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Walker.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Walker"
type: case
citation: "799 F.3d 1361 (2015)"
parallel_cite: ""
neutral_cite: 2015 WL 5157456
court: "U.S. Court of Appeals, 11th Circuit"
court_level: coa
circuit: 11th
year: 2015
date_decided: 2015-09-03
docket: ""
authority_weight: "Binding in-circuit — 11th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2015-09-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Walker
  varies_by_point: false
  scope_note: "Good law. Per curiam; applies Florida v. Jardines and United States v. Taylor to the geographic scope of the knock-and-talk implied license."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2844024/united-states-v-wayne-walker/"
  cluster_id: 2844024
  opinion_id: 2844024
  identity_checked: true
homes:
  - page: "[[Knock and Talk]]"
    role: "Recent development (role-based)"
related: ["[[Florida v. Jardines]]", "[[French v. Merrill]]", "[[United States v. Lundin]]", "[[United States v. Carloss]]", "[[Kentucky v. King]]"]
aliases: ["United States v. Wayne Walker", "United States v. Walker (11th Cir. 2015)"]
tags: ["case", "fourth-amendment", "knock-and-talk", "implied-license", "curtilage", "eleventh-circuit"]
holding: "A 'small departure' from the front door — here, approaching the occupant's car parked in an open-sided carport beside the house when seeking to contact him — stays within the geographic scope of the knock-and-talk implied license, and a pre-dawn (5:04 a.m.) knock and talk is not a search and needs no exigent circumstances where the surrounding circumstances make the approach reasonable."
lake:
  record_id: United States v. Walker
  status: verified
  projected_at: 2026-07-06
---

# United States v. Walker

*799 F.3d 1361 (11th Cir. 2015)* · U.S. Court of Appeals, 11th Circuit · **Binding in-circuit — 11th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers looking for Michael Upshaw — who had an outstanding warrant and was reportedly staying at Wayne Walker's house in Macon, Georgia — went to the house twice on the night of February 28, knocking at the main door and a second door each time with no answer; on the second visit they noticed a Honda Civic newly parked in Walker's open-sided carport. A little after 5:00 a.m. they drove past again, saw lights on in the house and the car's dome light on, and approached the car, where they saw a person resting his head on the steering wheel. Sergeant Douglas knocked on the car window, asked if the person was alright, and asked him to step out; it was Walker. Walker said Upshaw was not there and volunteered that the officers "were more than welcome" to come in and look; inside, an officer saw counterfeit $100 bills in plain view. Walker entered a conditional guilty plea to manufacturing counterfeit currency (18 U.S.C. § 471) and appealed the denial of his suppression motion.

## Issue
Whether officers exceeded the [[Knock and Talk|knock-and-talk]] exception when, instead of going to the front door, they approached the occupant's car parked in an open-sided carport, and whether doing so at 5:04 a.m. was unreasonable.

## Rule
The [[Knock and Talk|knock-and-talk]] exception rests on the implied license to approach and knock, and "[t]he scope of the knock and talk exception is limited in two respects. First, it ceases where an officer's behavior 'objectively reveals a purpose to conduct a search.' . . . Second, the exception is geographically limited to the front door or a 'minor departure' from it." — 799 F.3d at 1363. ^pin-1363

A small movement from the front door to reach the occupant stays within that geographic limit: "approaching Walker's vehicle parked inside of his open-sided carport, instead of going to his front door, did not exceed the geographic limit on the knock and talk exception. A 'small departure from the front door . . . when seeking to contact the occupants' is permissible." — [799 F.3d at 1364](https://www.courtlistener.com/opinion/2844024/united-states-v-wayne-walker/#:~:text=did%20not%20exceed%20the%20geographic%20limit%20on%20the%20knock%20and%20talk%20exception) (quoting *United States v. Taylor*, 458 F.3d 1201, 1205 (11th Cir. 2006)). ^pin-1364

The court also held that a pre-dawn knock and talk is reasonable on these circumstances and that an early-morning knock and talk "is not considered a search," so it requires no [[Exigent Circumstances and Hot Pursuit|exigent circumstances]]. — *Id.* (& n.1). ^pin-1364a

## Application
On these facts the officers did not exceed the exception. Their purpose was investigatory only in the sense of finding someone to talk to about Upshaw, not to "discover[] incriminating evidence," so their conduct did not objectively reveal a search. And approaching the open-sided carport — located right next to the house, where the lit dome light gave them reason to believe the occupant was sitting in the car — was a permissible small departure from the front door, not an intrusion into a constitutionally protected enclosed space. The 5:04 a.m. timing was reasonable given the two earlier visits and the lights indicating someone was inside; because a knock and talk is not a search, no [[Exigent Circumstances and Hot Pursuit|exigency]] was required.

## Conclusion
The officers' approach fell within the [[Knock and Talk|knock-and-talk]] exception and was reasonable; the Eleventh Circuit affirmed the denial of Walker's motion to suppress the counterfeit currency.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 11th Cir.**
- *Walker* applies the implied-license framework of [[Florida v. Jardines]] (and the Eleventh Circuit's *Taylor* "minor departure" rule) to hold that a small departure from the front door to reach the occupant stays within the [[Knock and Talk|knock-and-talk]] license. Contrast the time-plus-purpose analysis in [[United States v. Lundin]] (9th Cir.), where a pre-dawn approach undertaken to arrest the occupant exceeded the implied license.

## Appears on
- [[Knock and Talk]] — *Recent development (role-based)*

## Sources
- *United States v. Walker*, 799 F.3d 1361 (11th Cir. 2015) — https://www.courtlistener.com/opinion/2844024/united-states-v-wayne-walker/ — pinpoints: 1363, 1364.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "763e3b67b70d058d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Walker"}, "payload": {"all": [{"cite": "799 F.3d 1361", "page": "1361", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "799"}, {"cite": "2015 WL 5157456", "page": "5157456", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2015"}], "display": "799 F.3d 1361", "official": {"cite": "799 F.3d 1361", "page": "1361", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "799"}, "official_selection_present": true, "record_id": "United States v. Walker"}}
{"assertion_id": "4db17fb5d6a91248", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1364", "record_id": "United States v. Walker"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1364", "pinpoint_status": "slip-only", "quote": "approaching Walker's vehicle parked inside of his open-sided carport, instead of going to his front door, did not exceed the geographic limit on the knock and talk exception. A 'small departure from the front door . . . when seeking to contact the occupants' is permissible.", "quote_fidelity": "mismatch", "record_id": "United States v. Walker", "star_marker": null}}
{"assertion_id": "7aff2fc25e90dd30", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1364a", "record_id": "United States v. Walker"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1364a", "pinpoint_status": "slip-only", "quote": "is not considered a search,", "quote_fidelity": "mismatch", "record_id": "United States v. Walker", "star_marker": null}}
{"assertion_id": "b84f2557dee0e416", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1363", "record_id": "United States v. Walker"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1363", "pinpoint_status": "slip-only", "quote": "to come in and look; inside, an officer saw counterfeit $100 bills in plain view. Walker entered a conditional guilty plea to manufacturing counterfeit currency (18 U.S.C. § 471) and appealed the denial of his suppression motion. ## Issue Whether officers exceeded the knock-and-talk exception when, instead of going to the front door, they approached the occupant's car parked in an open-sided carport, and whether doing so at 5:04 a.m. was unreasonable. ## Rule The knock-and-talk exception rests on the implied license to approach and knock, and", "quote_fidelity": "mismatch", "record_id": "United States v. Walker", "star_marker": null}}
{"assertion_id": "06f891d089718947", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Walker"}, "payload": {"as_of_content": "2015-09-03", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Walker", "scope_note": "Good law. Per curiam; applies Florida v. Jardines and United States v. Taylor to the geographic scope of the knock-and-talk implied license.", "varies_by_point": false}}
```

### lake record — United States v. Walker

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Walker",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Wayne Walker",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Wayne WALKER, Defendant-Appellant",
    "input_case_name": "United States v. Walker",
    "court": "U.S. Court of Appeals, 11th Circuit",
    "court_id": "ca11",
    "court_level": "coa",
    "circuit": "11th",
    "state": null,
    "date_decided": "2015-09-03",
    "year": 2015,
    "docket": null,
    "cluster_id": 2844024,
    "lead_opinion_id": 2844024,
    "sibling_ids": [
      2844024
    ],
    "absolute_url": "/opinion/2844024/united-states-v-wayne-walker/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "799 F.3d 1361",
      "volume": "799",
      "reporter": "F.3d",
      "page": "1361",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2015 WL 5157456",
        "volume": "2015",
        "reporter": "WL",
        "page": "5157456",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "799 F.3d 1361",
        "volume": "799",
        "reporter": "F.3d",
        "page": "1361",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 WL 5157456",
        "volume": "2015",
        "reporter": "WL",
        "page": "5157456",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "799 F.3d 1361",
    "official_selection": {
      "court_class": "coa",
      "selected": "799 F.3d 1361",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1363",
      "page": null,
      "quote": "to come in and look; inside, an officer saw counterfeit $100 bills in plain view. Walker entered a conditional guilty plea to manufacturing counterfeit currency (18 U.S.C. \u00a7 471) and appealed the denial of his suppression motion. ## Issue Whether officers exceeded the knock-and-talk exception when, instead of going to the front door, they approached the occupant's car parked in an open-sided carport, and whether doing so at 5:04 a.m. was unreasonable. ## Rule The knock-and-talk exception rests on the implied license to approach and knock, and",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1364",
      "page": null,
      "quote": "approaching Walker's vehicle parked inside of his open-sided carport, instead of going to his front door, did not exceed the geographic limit on the knock and talk exception. A 'small departure from the front door . . . when seeking to contact the occupants' is permissible.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1364a",
      "page": null,
      "quote": "is not considered a search,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2015-09-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Walker",
    "varies_by_point": false,
    "scope_note": "Good law. Per curiam; applies Florida v. Jardines and United States v. Taylor to the geographic scope of the knock-and-talk implied license.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "French v. Merrill",
          "cluster_id": 5273192,
          "cite": [
            "15 F.4th 116"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Walker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "KEMP v. THE STATE (Three Cases)",
          "cluster_id": 10366887,
          "cite": [
            "303 Ga. 385"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Walker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Reginald Graham",
          "cluster_id": 10286306,
          "cite": [
            "123 F.4th 1197"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Walker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Falls",
          "cluster_id": 10019104,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Walker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Doe v. Samford University",
          "cluster_id": 6454512,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Walker:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2844024) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca11)",
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
        "query": "cites:(2844024)",
        "reviewed": 5,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 5,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(2844024)",
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
    "complete_query": "cites:(2844024)",
    "indexed_citing_opinions": 5,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2844024,
        "count": 5,
        "count_source": "search"
      }
    ],
    "citation_count": 38,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-walker.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 5,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2844024,
        "cited_id": 77385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2844024,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2844024,
        "cited_id": 626016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2844024,
        "cited_id": 856347,
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
    "date_created": "2026-07-06T03:30:51Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:31:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:31:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:32:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:31:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Walker

```
           Case: 15-10710   Date Filed: 09/03/2015   Page: 1 of 7


                                                                    [PUBLISH]



            IN THE UNITED STATES COURT OF APPEALS

                    FOR THE ELEVENTH CIRCUIT
                      ________________________

                            No. 15-10710
                        Non-Argument Calendar
                      ________________________

              D.C. Docket No. 5:14-cr-00055-MTT-CHW-1



UNITED STATES OF AMERICA,

                                                              Plaintiff-Appellee,

                                 versus

WAYNE WALKER,

                                                         Defendant-Appellant.

                      ________________________

               Appeal from the United States District Court
                   for the Middle District of Georgia
                     ________________________

                            (September 3, 2015)

Before ED CARNES, Chief Judge, MARCUS, and WILLIAM PRYOR, Circuit
Judges.

PER CURIAM:
                Case: 15-10710    Date Filed: 09/03/2015   Page: 2 of 7


         Wayne Walker entered a conditional guilty plea to one count of

manufacturing counterfeit United States currency in violation of 18 U.S.C. § 471.

He appeals the district court’s denial of his motion to suppress. He contends that

the officers who found counterfeit bills in his home did not comply with the

“knock and talk” exception to the Fourth Amendment’s warrant requirement and

acted unreasonably by going to his house at 5:04 a.m.

                                          I.

         Officer Jason Douglas and Sergeant Travis Douglas were working the night

shift on February 28, 2014. Because Officer Douglas had received information

that Michael Upshaw, who had an outstanding warrant, could be found at Walker’s

house, the two officers visited it that night and again in the early hours of March 1.

         Walker’s house is located at the corner of Georgia Highway 49 and 111

Moore Place in Macon, Georgia. The back of the house faces Highway 49 while

the side of the house faces Moore Place (another road). The house sits about 100

feet from Moore Place. A gravel driveway runs from Moore Place and goes

directly under a metal carport that sits about 30 feet from the main door to the

house (there is also a second door to the house). The carport is entirely open on all

sides but covered by a metal roof. It is supported by five poles on each of two

sides.




                                          2
              Case: 15-10710     Date Filed: 09/03/2015    Page: 3 of 7


      The officers first went to Walker’s house at 9:00 p.m. on February 28. They

knocked at the main door and the other door but no one answered. They left and

returned at 11:00 p.m. Again they knocked and again no one answered. The

officers noticed that parked in the open-sided carport was a Honda Civic that had

not been there when they were at the house earlier.

      The officers drove past the house again a little after 5:00 a.m. the following

morning. They noticed that some house lights were on and the dome light inside

the Honda Civic was now on. As they approached the car they saw a person inside

with his head resting on the steering wheel. The officers testified that they were

trying to figure out who was in the car and whether the person was alright.

Sergeant Douglas therefore knocked on the car window, asked the person whether

he was alright, and then asked him to step out of the car. The person in the car

turned out to be Walker. The officers told Walker that they were looking for

Upshaw. Walker said that Upshaw was not at the house and, without being asked,

told the officers that they “were more than welcome” to come in and look for him.

Upon entering the house, Officer Douglas began searching for Upshaw. He saw

counterfeit $100 bills printed on white sheets of paper sitting on a shelf in plain

view. The officers did not find Upshaw, but they did decide that they had probable

cause to arrest Walker for the counterfeit currency.

                                          II.


                                           3
               Case: 15-10710     Date Filed: 09/03/2015     Page: 4 of 7


        Walker contends that the district court should have suppressed the evidence

of counterfeit money that the officers found in his home because their search was

illegal. “A motion to suppress evidence presents a mixed question of law and

fact.” United States v. Lewis, 674 F.3d 1298, 1302 (11th Cir. 2012). We review

the district court’s factfindings for clear error and its “application of the law to the

facts de novo.” Id. at 1302–03. We construe all facts in the light most favorable to

the party who prevailed in the district court and give “substantial deference to the

factfinder’s credibility determinations, both explicit and implicit.” Id. at 1303.

        The “ultimate touchstone of the Fourth Amendment is reasonableness.”

Brigham City v. Stuart, 547 U.S. 398, 403, 126 S. Ct. 1943, 1947 (2006). Because

the home and the curtilage surrounding it is a “constitutionally protected area,”

Florida v. Jardines, ___ U.S. ___, 133 S. Ct. 1409, 1415–16 (2013), it is

“presumptively unreasonable” to search a home or its curtilage without a warrant.

Under the “knock and talk” exception, however, a “police officer not armed with a

warrant may approach a home and knock, precisely because that is no more than

any private citizen may do.” Id. at 1416 (quotation marks omitted). That

exception is based on the “implicit license” that all individuals (including police

officers) have to “approach [a] home by the front path, knock promptly, wait

briefly to be received, and then (absent invitation to linger longer) leave.” Id. at

1415.


                                            4
              Case: 15-10710      Date Filed: 09/03/2015   Page: 5 of 7


      The scope of the knock and talk exception is limited in two respects. First, it

ceases where an officer’s behavior “objectively reveals a purpose to conduct a

search.” Id. at 1416–17 (holding that using a police dog to sniff for drugs on the

front porch “in hopes of discovering incriminating evidence” exceeds the scope of

the knock and talk exception). Second, the exception is geographically limited to

the front door or a “minor departure” from it. United States v. Taylor, 458 F.3d

1201, 1204–05 (11th Cir. 2006).

      Walker contends that the officers exceeded the scope of the knock and talk

exception because they conducted an investigatory search when they approached

his vehicle. They did not, for two reasons. First, the officers’ behavior did not

objectively reveal a purpose to search. As their earlier visits to the house

indicated, the officers were trying to find someone to talk to about Upshaw’s

whereabouts. The officers did not approach Walker with the purpose of

“discovering incriminating evidence” — just to speak with the homeowner, which

is conduct that falls squarely within the scope of the knock and talk exception.

Jardines, 131 S. Ct. at 1416. Walker asserts that the officers were engaged in a

search because they did not know that he was in the vehicle when they approached

it. They knew, however, that a dome light was on, which indicated that a person

might well be inside, and that fact was confirmed when they approached the car.

An officer may not know that a homeowner is inside a home when knocking on the


                                          5
              Case: 15-10710        Date Filed: 09/03/2015   Page: 6 of 7


door, but the knock and talk exception permits knocking on the door to find out.

See Jardines, 131 S. Ct. at 1415.

      Second, approaching Walker’s vehicle parked inside of his open-sided

carport, instead of going to his front door, did not exceed the geographic limit on

the knock and talk exception. A “small departure from the front door . . . when

seeking to contact the occupants” is permissible. Taylor, 458 F.3d 1205 (citation

and quotation marks omitted); cf. Coffin v. Brandau, 642 F.3d 999, 1012 (11th Cir.

2011) (contrasting a garage attached to a home and enclosed by three walls and a

door with a carport that is open and exposed to the public in deciding whether an

officer’s entry into the garage violated the Fourth Amendment). The carport was

located right next to the house and the officers entered it because they had reason

to believe the house’s occupant was sitting in the car parked inside. They did not

exceed the scope of the knock and talk exception.

      Walker also contends that going to someone’s house before sunrise to knock

on the door is unreasonable and exceeds the implied invitation that underlies the

knock and talk exception. That contention fails in light of all the circumstances

surrounding the officers’ actions. They had already visited the house twice to

speak with its owner. When they arrived the third time at 5:04 a.m. and saw a light

on inside the vehicle, it was not unreasonable to think that someone was inside it.

Although many people might normally be asleep at that early hour, the light on in


                                            6
                Case: 15-10710       Date Filed: 09/03/2015       Page: 7 of 7


the car indicated otherwise. The officers also saw lights on in the house. They did

not act unreasonably by approaching the vehicle, tapping on the window, and

asking Walker to step out. 1 Because their conduct was reasonable, the officers

complied with the Fourth Amendment. See Brigham City, 547 U.S. at 403, 406–

07, 126 S. Ct. at 1947, 1949. The district court therefore did not err in denying

Walker’s motion to suppress the evidence of counterfeit currency found in the

home.

        AFFIRMED.




        1
         Walker argues that under Brigham City v. Stuart, 547 U.S. 398, 126 S. Ct. 1943 (2006),
any warrantless entry into the home or curtilage that occurs in the wee hours of the morning must
be accompanied by exigent circumstances. That decision held that police officers’ warrantless
search of a home at 3:00 a.m. was reasonable because exigent circumstances existed. Id. at 403–
07, 126 S. Ct. at 1947–49. It did not hold, however, that exigent circumstances must exist for a
warrantless early morning knock and talk, which is not considered a search.
                                               7

```

---

## GROUP: _overhaul2/lake/cases/United States v. Warshak.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Warshak
type: case
citation: "631 F.3d 266 (2010)"
parallel_cite: ""
neutral_cite: "2010 U.S. App. LEXIS 25415; 2010 WL 5071766"
court: "U.S. Court of Appeals, 6th Cir."
court_level: coa
circuit: ca6
year: 2010
date_decided: ""
docket: No. 08-3997
authority_weight: "Binding in-circuit — 6th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/181032/united-states-v-warshak/"
  cluster_id: 181032
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Warshak
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Lower-court development (content/metadata line)"
related:
  - "[[Third-Party Doctrine & CSLI]]"
  - "[[Katz v. United States]]"
  - "[[United States v. Jacobsen]]"
  - "[[Carpenter v. United States]]"
tags:
  - case
  - fourth-amendment
  - email
  - third-party-doctrine
  - stored-communications-act
  - digital-privacy
  - warrant-requirement
holding: "A subscriber has a reasonable expectation of privacy in the contents of emails stored with, sent, or received through a commercial ISP; the government therefore may not compel an ISP to turn over the contents of a subscriber's emails without first obtaining a warrant based on probable cause, and to the extent the Stored Communications Act permits warrantless compelled disclosure of email contents it is unconstitutional. Because the agents relied in good faith on the SCA, however, the exclusionary rule did not require suppression."
aliases:
  - United States v. Warshak
  - "United States v. Warshak (6th Cir. 2010)"
---

# United States v. Warshak

*631 F.3d 266 (6th Cir. 2010)* (No. 08-3997) · U.S. Court of Appeals for the Sixth Circuit · **Binding in-circuit — 6th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 181032 → combined opinion 181032 (Boggs, Circuit Judge, for the court; McKeague, J., joined; Keith, J., concurred in the result; 631 F.3d 266, argued June 16, 2010, decided Dec. 14, 2010). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*288`). S9 promotes. -->

## Background
Steven Warshak ran Berkeley Premium Nutraceuticals, the company behind the "male enhancement" supplement Enzyte, and was convicted with others of a large mail-, wire-, and bank-fraud and money-laundering scheme built on deceptive billing of customers. In building its case, the government obtained roughly 27,000 of Warshak's emails from his Internet service provider, NuVox, not with a warrant but under provisions of the Stored Communications Act (SCA) allowing compelled disclosure on less than probable cause. Warshak argued on appeal that acquiring his email contents this way violated the Fourth Amendment and that the emails should have been suppressed.

## Issue
Whether a subscriber has a Fourth Amendment [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the contents of emails held by a commercial ISP, such that the government must obtain a warrant before compelling the ISP to disclose them — and, if so, whether the exclusionary rule requires suppression.

## Rule
Analogizing email to a sealed letter or a telephone call routed through an intermediary, the court held that using an ISP as a conduit does not surrender the privacy of the message's contents; the ISP is the functional equivalent of a post office or phone company. It therefore held: "The government may not compel a commercial ISP to turn over the contents of a subscriber's emails without first obtaining a warrant based on probable cause." — 631 F.3d at 288. Because the agents obtained Warshak's emails without a warrant, they violated the Fourth Amendment, and to the extent the SCA authorizes such warrantless compelled disclosure of email contents, it is unconstitutional. ^pin-288

## Application
The court distinguished the third-party-doctrine cases: unlike the bank records in *[[United States v. Miller]]*, emails are confidential communications entrusted to an ISP as a mere intermediary, not information voluntarily conveyed to the recipient for use in the ordinary course of business — so a provider's contractual ability to access emails in limited circumstances did not extinguish the subscriber's expectation of privacy. Even so, the emails were not suppressed: relying on *[[Illinois v. Krull]]*, the court held the agents had acted in objectively good-faith reliance on the SCA, whose unconstitutionality was not then apparent, so the deterrence rationale of the exclusionary rule did not warrant suppression. The convictions were affirmed on this ground.

## Conclusion
The court held the warrantless acquisition of Warshak's emails **violated the Fourth Amendment**, but declined to suppress the emails under the [[The Good-Faith Exception|good-faith exception]]; the challenged convictions were **affirmed** on the email-privacy issue. Boggs, Circuit Judge, wrote for the court (McKeague, J., joined); Keith, J., concurred in the result.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Warshak* is the anchor circuit decision extending Fourth Amendment protection to the *contents* of emails held by a third-party ISP — a landmark limiting the third-party doctrine in the digital context and a widely followed precursor to the Supreme Court's *[[Carpenter v. United States]]* (2018). Teach it in the *[[Katz v. United States|Katz]]*/*[[United States v. Jacobsen|Jacobsen]]* line as the case that treats an ISP like a post office, while noting its in-circuit (6th Cir.) authority and the good-faith limit on suppression.

## Appears on
- [[Third-Party Doctrine & CSLI]] — *Lower-court development (content/metadata line)*

## Sources
- [*United States v. Warshak*, 631 F.3d 266 (6th Cir. 2010)](https://www.courtlistener.com/opinion/181032/united-states-v-warshak/) — pinpoint: 288 (Boggs, J., for the court; the CL opinion text carries the reporter star `*288` in the *Miller* discussion immediately before the quoted holding paragraph, which sits on page 288). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "59898af87e41b027", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Warshak"}, "payload": {"all": [{"cite": "631 F.3d 266", "page": "266", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "631"}, {"cite": "2010 U.S. App. LEXIS 25415", "page": "25415", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2010"}, {"cite": "2010 WL 5071766", "page": "5071766", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2010"}], "display": "631 F.3d 266", "official": {"cite": "631 F.3d 266", "page": "266", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "631"}, "official_selection_present": true, "record_id": "United States v. Warshak"}}
{"assertion_id": "abac611150140ad5", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Warshak"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Warshak", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Warshak

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Warshak",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Warshak",
    "case_name_short": "Warshak",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Steven WARSHAK (08-3997/4085; 09-3176); Harriet Warshak (08-3997/4087/4429); TCI Media, Inc. (08-3997/4212), Defendants-Appellants",
    "input_case_name": "United States v. Warshak",
    "court": "U.S. Court of Appeals, 6th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca6",
    "state": null,
    "date_decided": null,
    "year": 2010,
    "docket": "No. 08-3997",
    "cluster_id": 181032,
    "lead_opinion_id": 9438755,
    "sibling_ids": [],
    "absolute_url": "/opinion/181032/united-states-v-warshak/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "631 F.3d 266",
      "volume": "631",
      "reporter": "F.3d",
      "page": "266",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2010 U.S. App. LEXIS 25415",
        "volume": "2010",
        "reporter": "U.S. App. LEXIS",
        "page": "25415",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 WL 5071766",
        "volume": "2010",
        "reporter": "WL",
        "page": "5071766",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "631 F.3d 266",
        "volume": "631",
        "reporter": "F.3d",
        "page": "266",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 U.S. App. LEXIS 25415",
        "volume": "2010",
        "reporter": "U.S. App. LEXIS",
        "page": "25415",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 WL 5071766",
        "volume": "2010",
        "reporter": "WL",
        "page": "5071766",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "631 F.3d 266",
    "official_selection": {
      "court_class": "coa",
      "selected": "631 F.3d 266",
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
    "date_created": "2026-07-06T13:11:36Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:11:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:11:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:11:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:11:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-warshak--181032",
      "to_record_id": "United States v. Warshak",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Warshak (truncated)

```
<opinion type="majority">
<p id="b300-5">BOGGS, J., delivered the opinion of the court, in which McKEAGUE, J., joined. KEITH, J. (pp. 333-36), delivered a separate opinion concurring in the result.</p>
<p id="b300-6">OPINION</p>
<author id="b300-7">BOGGS, Circuit Judge.</author>
<p id="b300-8">Berkeley Premium Nutraceuticals, Inc., was an incredibly profitable company that served as the distributor of Enzyte, an herbal supplement purported to enhance male sexual performance. In this appeal, defendants Steven Warshak (“Warshak”), Harriet Warshak (“Harriet”), and TCI Media, Inc. (“TCI”), challenge their convictions stemming from a massive scheme to defraud Berkeley’s customers. Warshak and Harriet also challenge their sentences, as well as two forfeiture judgments.</p>
<p id="b300-9">Given the volume and complexity of the issues presented, we provide the following summary of our holdings:</p>
<p id="b300-10">(1) Warshak enjoyed a reasonable expectation of privacy in his emails vis-a-vis NuVox, his Internet Service Provider. <em>See Katz v. United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U.S. 347</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L.Ed.2d 576</a></span> (1967). Thus, government agents violated his Fourth Amendment rights by compelling NuVox to turn over the emails without first obtaining a warrant based on probable cause. However, because the agents relied in good faith on provisions of the Stored Communications Act, the exclusionary rule does not apply in this instance. <em>See Illinois v. Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">480 U.S. 340</a></span>, <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">107 S.Ct. 1160</a></span>, <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">94 L.Ed.2d 364</a></span> (1987).</p>
<p id="b300-12">(2) The district court did not err in refusing to hold a full-fledged hearing under <em>Kastigar v. United States, </em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">406 U.S. 441</a></span>, <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">92 S.Ct. 1653</a></span>, <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">32 L.Ed.2d 212</a></span> (1972), when determining whether government agents had improperly used privileged materials seized during a valid search of Berkeley’s headquarters. <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>does not apply with full force outside the context of compelled testimony. <em>See United States v. Squillacote, </em><span class="citation" data-id="2967273"><a href="/opinion/2967273/united-states-v-squillacote/" aria-description="Citation for case: United States v. Squillacote">221 F.3d 542</a></span> (4th Cir.2000).</p>
<p id="b300-13">(3) The district court did not abuse its discretion by failing to order the government to provide discovery in a different format, as Federal Rule of Criminal Procedure 16 is silent on the issue of the form that discovery must take. Moreover, the government did not duck its obligations under <em>Brady v. Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U.S. 83</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">83 S.Ct. 1194</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">10 L.Ed.2d 215</a></span> (1963), by providing the defendants with massive quantities of discovery. <em>See United States v. Skilling, </em><span class="citation" data-id="64496"><a href="/opinion/64496/united-states-v-skilling/" aria-description="Citation for case: United States v. Skilling">554 F.3d 529</a></span> (5th Cir.2009), <em>vacated in part on other grounds, </em>— U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./130/2896/">130 S.Ct. 2896</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/177/619/">177 L.Ed.2d 619</a></span> (2010). Finally, the district court did not err in refusing to grant the defendants a continuance so that they could continue examining the discovery materials turned over by the government.</p>
<p id="b300-16">(4) The district court did not err in refusing to grant Warshak a new trial based on an alleged <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation, as the purportedly exculpatory material did not rise <page-number citation-index="1" label="275">*275</page-number>to the level of materiality. <em>See Kyles v. Whitley, </em><span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">514 U.S. 419</a></span>, <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">115 S.Ct. 1555</a></span>, <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">131 L.Ed.2d 490</a></span> (1995).</p>
<p id="b301-5">(5) The district court did not err in refusing to grant the defendants a new trial on the basis of prosecutorial misconduct. Though the prosecution did make a number of improper remarks during its rebuttal argument, the remarks were not flagrant. <em>See United States v. Carter, </em><span class="citation" data-id="771624"><a href="/opinion/771624/united-states-v-roquel-allen-carter/" aria-description="Citation for case: United States v. Roquel Allen Carter">236 F.3d 777</a></span> (6th Cir.2001).</p>
<p id="b301-6">(6) The evidence was sufficient to support Warshak’s and Harriet’s respective convictions for conspiracy to commit mail, wire, and bank fraud, in violation of <span class="citation no-link">18 U.S.C. § 1349</span>. <em>See Jackson v. Virginia, </em><span class="citation" data-id="9427680"><a href="/opinion/110138/jackson-v-virginia/" aria-description="Citation for case: Jackson v. Virginia">443 U.S. 307</a></span>, <span class="citation" data-id="9427680"><a href="/opinion/110138/jackson-v-virginia/" aria-description="Citation for case: Jackson v. Virginia">99 S.Ct. 2781</a></span>, <span class="citation" data-id="9427680"><a href="/opinion/110138/jackson-v-virginia/" aria-description="Citation for case: Jackson v. Virginia">61 L.Ed.2d 560</a></span> (1979). Those convictions are therefore sustained.</p>
<p id="b301-7">(7) The evidence was sufficient to support Warshak’s convictions for mail fraud, in violation of <span class="citation no-link">18 U.S.C. § 1341</span>. Those convictions are therefore sustained.</p>
<p id="b301-8">(8) The evidence was sufficient to support Warshak’s and Harriet’s respective convictions for bank fraud, in violation of <span class="citation no-link">18 U.S.C. § 1344</span>. Furthermore, the district court did not err in instructing the jury that, under certain circumstances, the government may prove specific intent to defraud a bank by showing specific intent to defraud a third party. <em>See United States v. Reaume, </em><span class="citation" data-id="782971"><a href="/opinion/782971/united-states-v-scott-a-reaume/" aria-description="Citation for case: United States v. Scott A. Reaume">338 F.3d 577</a></span> (6th Cir.2003). Those convictions are therefore sustained.</p>
<p id="b301-9">(9) The evidence was sufficient to support Warshak’s conviction for conspiracy to commit access-device fraud, in violation of <span class="citation no-link">18 U.S.C. § 1029</span>. That conviction is sustained.</p>
<p id="b301-10">(10) The evidence was sufficient to support Warshak’s and TCI’s respective convictions for money laundering, in violation of <span class="citation no-link">18 U.S.C. §§ 1956</span>, 1957. Those convictions are affirmed. By contrast, the evidence was insufficient to support Harriet’s money-laundering convictions. Those convictions are therefore reversed.</p>
<p id="b301-12">(11) The evidence was sufficient to support Warshak’s conviction for conspiracy to obstruct an FTC proceeding, in violation of <span class="citation no-link">18 U.S.C. §§ 371</span>, 1505. As a consequence, that conviction is sustained.</p>
<p id="b301-13">(12) The district court did not err in refusing to order the government to reveal whether or not it had conducted any additional surreptitious searches of Warshak’s emails or communications. The discovery afforded by Federal Rule of Criminal Procedure 16 is limited to the evidence referred to in its express provisions, <em>United States v. Presser, </em><span class="citation" data-id="504674"><a href="/opinion/504674/united-states-v-jackie-presser-harold-friedman-and-anthony-hughes/#1285" aria-description="Citation for case: United States v. Jackie Presser Harold Friedman and...">844 F.2d 1275, 1285</a></span> (6th Cir.1988), and those provisions do not encompass the information sought by the defendants.</p>
<p id="b301-14">(13) The district court failed to provide an adequate explanation of its determination that the defendants should be held accountable for $411 million in losses. <em>See </em>Fed.R.Crim.P. 32(i)(3)(B); <em>United States v. White, </em><span class="citation" data-id="9632037"><a href="/opinion/1446782/united-states-v-white/#415" aria-description="Citation for case: United States v. White">492 F.3d 380, 415</a></span> (6th Cir.2007). We therefore vacate Warshak’s sentence and remand.</p>
<p id="b301-15">(14) The district court did not abuse its discretion in refusing to admit certain evidence during the forfeiture phase of the trial. Furthermore, the evidence was sufficient to support the proceeds-money and money-laundering forfeiture judgments against Warshak. In addition, the evidence was sufficient to support the proceeds-money forfeiture judgment against Harriet, but it was insufficient to support the money-laundering forfeiture judgment against her. Therefore, the proceeds-money forfeiture judgment is affirmed with respect to both Warshak and Harriet, and the money-laundering money judgment is affirmed with respect to Warshak, but reversed with respect to Harriet.</p>
<p id="b302-3"><page-number citation-index="1" label="276">*276</page-number>I. STATEMENT OF THE FACTS</p>
<p id="Adx">A. Factual Background</p>
<p id="b302-4">In 2001, Steven Warshak (“Warshak”) owned and operated a number of small businesses in the Cincinnati area. One of his businesses was TCI Media, Inc. (“TCI”), which sold advertisements in sporting venues. Warshak also owned a handful of companies that offered a modest line of so-called “nutraceuticals,” or herbal supplements.<footnotemark>1</footnotemark> While the companies bore different names and sold different products, they appear to have been run as a single business, and they were later aggregated to form Berkeley Premium Nutraceuticals, Inc. (“Berkeley”).<footnotemark>2</footnotemark> In Berkeley’s early days, the company’s workforce was relatively minute; the company employed approximately 12 to 15 people, nearly all of whom were Warshak’s friends and family. Among them was his mother, Harriet Warshak (“Harriet”), who processed credit-card payments.</p>
<p id="b302-5">As the company grew, Warshak brought on additional employees to facilitate expansion, but he remained extremely “hands-on” with respect to the company’s operations. In 2001, he hired James Teegarden, who eventually became Berkeley’s Chief Operating Officer. Warshak also hired Shelley Kinmon to oversee the company’s sales, later elevating her to the role of Vice-President. In 2002, Sue and Greg Cossman, Warshak’s sister and brother-in-law, joined the company. Sue worked in Customer Care, where she dealt with customer complaints. Greg came in as the President of the company and thereafter functioned in various other capacities. That year also saw the hiring of Sam Grote, who was brought on board to work in the marketing department.</p>
<p id="b302-10">To sell its products, Berkeley took orders over the phone, but it also made sales through the mail and over the Internet. Customers purchased products with their credit cards, and their credit-card numbers were entered into a database along with other information. During sales calls, representatives would read from sales scripts,<footnotemark>3</footnotemark> which listed the major points to cover during the transaction. Shelley Kinmon testified that Warshak had the final word on the content of the scripts. Often, the scripts would include a description of the desired product, as well as language intended to persuade more pliant customers to make additional purchases.</p>
<p id="b302-11">In the latter half of 2001, Berkeley launched Enzyte, its flagship product. At the time of its launch, Enzyte was purported to increase the size of a man’s erection. The product proved tremendously popular, and business rose sharply. By 2004, demand for Berkeley’s products had grown so dramatically that the company employed 1500 people, and the call center remained open throughout the night, taking orders at breakneck speed. Berkeley’s line of supplements also expanded, ballooning from approximately four products to around thirteen. By year’s end, Berkeley’s annual sales topped out at around $250 million, largely on the strength of Enzyte.</p>
<p id="b303-4"><page-number citation-index="1" label="277">*277</page-number>1. <em>Advertising</em></p>
<p id="b303-5">The popularity of Enzyte appears to have been due in large part to Berkeley’s aggressive advertising campaigns. The vast majority of the advertising — approximately 98% — was conducted through television spots. Around 2004, network television was saturated with Enzyte advertisements featuring a character called “Smilin’ Bob,” whose trademark exaggerated smile was presumably the result of Enzyte’s efficacy. The “Smilin’ Bob” commercials were rife with innuendo and implied that users of Enzyte would become the envy of the neighborhood.</p>
<p id="b303-6">In addition to the television commercials, however, there were also advertisements in other media, such as print and radio. In 2001, just after Enzyte’s premiere, advertisements appeared in a number of men’s interest magazines. At Warshak’s direction, those advertisements cited a 2001 independent customer study, which purported to show that, over a three-month period, 100 English-speaking men who took Enzyte experienced a 12 to 31% increase in the size of their penises. The 2001 study was also referenced in radio advertisements and appeared on the company’s website, as well as in brochures and sales calls. James Teegarden later testified that the survey was bogus. He stated that, prior to the appearance of the advertisements, Warshak instructed him to create a spreadsheet and to fill it with fabricated data. Teegarden testified that he plucked the numbers out of the air and generated the spreadsheet over a twenty-four hour period.</p>
<p id="b303-7">A number of advertisements also indicated that Enzyte boasted a 96% customer satisfaction rating. Teegarden testified that that statistic, too, was totally spurious. Before the claim began showing up in Berkeley’s literature, Warshak had asked him to harvest 500 names from the customer database and to “mark an ‘X’ by either satisfied or very satisfied on say 475 of those.” As for the remaining 25, Tee-garden “was to put not satisfied.” Thereafter, the customer-satisfaction statistic cropped up in Berkeley’s print advertisements and in the “sales pitches, brochures, [and on the] Internet.”</p>
<p id="b303-11">Finally, numerous print and radio advertisements boasted that Enzyte was the brainchild of reputable doctors with impressive educational pedigrees. According to the ads, “Enzyte was developed by Dr. Fredrick Thomkins, a physician with a biology degree from Stanford and Dr. Michael Moore, a leading urologist from Harvard.” The ads also stated that the doctors had collaborated for thirteen years in developing a supplement designed to “stretch and elongate.” In reality, the doctors were just as fictitious as “Smilin’ Bob.” Investigators who contacted Stanford and Harvard learned that neither man existed.</p>
<p id="b303-12">2. <em>The Auto-Ship Program</em></p>
<p id="b303-13">The “life blood” of the business was its auto-ship program, which was instituted in 2001, shortly before Enzyte hit the market.<footnotemark>4</footnotemark> The auto-ship program was a continuity or negative-option program, in which a customer would order a free trial of a product and then continue to receive additional shipments of that product until he opted out. Before each new continuity shipment arrived on the customer’s doorstep, a corresponding charge would appear on his credit-card statement. The shipments and charges would continue until the customer decided to withdraw from the <page-number citation-index="1" label="278">*278</page-number>program, which required the customer to notify the company.</p>
<p id="b304-4">In the early days of the auto-ship program, customers who ordered products over the phone were not told that they were being enrolled.<footnotemark>5</footnotemark> From August 2001 to at least the end of December 2002,<footnotemark>6</footnotemark> customers were simply added to the program at the time of the initial sale without any indication that they would be on the hook for additional charges. Apparently, products were shipped with literature explaining the program, but no authorization was sought in advance of the shipment. According to Teegarden, Warshak explained that the auto-ship program was never mentioned because “nobody would sign up.” If nobody signed up, “you couldn’t make revenue.”</p>
<p id="b304-5">This policy resulted in a substantial volume of complaints, both to Berkeley and to outside organizations. In October 2002, the Better Business Bureau (“BBB”) contacted Berkeley and indicated that more than 1,500 customers had called to voice their consternation. Because of the complaints, Berkeley’s sales scripts and website began to include some language disclosing the auto-ship program.<footnotemark>7</footnotemark> A number of internal emails indicate that sales representatives were required to read the disclosure language and faced punishment if they failed to do so. To monitor the interactions between representatives and customers, Berkeley installed a recording system for all incoming calls.</p>
<p id="b304-12">However, as a number of Berkeley insiders testified, the compulsory disclosure language was not always read, and it was designed not to work. Shelley Kinmon testified that the disclosure of the continuity shipments was only made <em>after </em>the customer had placed his order. In other words, the sales representative had already taken the customer’s credit-card information when auto-ship was mentioned. Also, the disclosures were deliberately made with haste, and they were placed after unrelated language that was intended to divert or deaden the customer’s attention. In the case of Enzyte, sales reps were instructed to lead into the disclosure language by stating that “the product is not a contraceptive nor will it prevent or treat any sexually transmitted disease.”<footnotemark>8</footnotemark> According to Teegarden, the thinking was that, “if we started off with a statement about a contraceptive, something other than what it was, that people wouldn’t really listen to what we were disclosing to them.”</p>
<p id="b305-4"><page-number citation-index="1" label="279">*279</page-number>Moreover, disclosure of the auto-ship program was sometimes irrelevant. For example, in November 2003, Berkeley hired a company called West to handle “sales calls that were from ... Avlimil or Enzyte advertisements.” During the calls, West’s representatives asked customers if they wanted to be enrolled in the auto-ship program, and over 80% of customers declined. When Warshak learned what was happening, he issued instructions to “take those customers, even if they decline[d], even if they said no to the Auto-Ship program, go ahead and put them on the Auto-Ship program.” A subsequent email between Berkeley employees indicated that “all [West] customers, whether they know it or not, are going on [auto-ship].” As a result, numerous telephone orders resulted in unauthorized continuity shipments.</p>
<p id="b305-5">However, not all of Berkeley’s auto-ship issues related to the telephone. Many Berkeley sales were the result of orders placed on the Internet, where disclosure of the auto-ship program was inconsistent. In 2001, when Berkeley was in its infancy, the company’s websites contained no indication that customers would be enrolled in the program. Thereafter, disclosures were placed on the websites, but the disclosures would “appear[ ], disappear[ ], and chang[e].” In 2003, for instance, disclosure language that had been added to Berkeley’s Avlimil website was removed because sales had been “drastically affected.” Additionally, the language that did appear was often confusing and contained non sequiturs.</p>
<p id="b305-6">By July 2004, the complaints arising from Berkeley’s auto-ship program had not slowed, so the President of the BBB reached out to Berkeley, sending a letter directly to Warshak. The purpose of the letter was to express “serious concerns about the number of complaints that [the BBB] had received.” The complaints “related to a single issue, which was the [auto-ship] program.” According to the President of the BBB, the organization “had asked on numerous occasions that [Berkeley] consider dropping [the program], and got no positive response.”</p>
<p id="b305-10">3. <em>The Merchant Banks</em></p>
<p id="b305-11">In order for Berkeley’s business to operate, it was essential that the company be able to accept credit cards as a form of payment.<footnotemark>9</footnotemark> To process credit-card transactions, Berkeley obtained lines of credit from several merchant banks. The relationships between Berkeley and the merchant banks involved intermediaries known as credit-card processors. Often, the processors had contractual agreements with the merchant banks, and the processors were the ones who set up the credit-card processing arrangements with Berkeley. Nonetheless, when Berkeley applied for a merchant account with a given processor, the applications were passed along to the banks. Furthermore, either the banks or the processors could terminate Berkeley’s merchant accounts.</p>
<p id="b305-12">In early 2002, Warshak’s merchant account at the Bank of Kentucky was terminated for excessive “chargebacks.” A chargeback occurs when a customer calls the credit card company directly and contests or disputes a charge. Merchant banks — and credit-card processors — will generally not do business with merchants that experience high volumes of charge-backs, as those merchants present a greater financial risk. In determining whether <page-number citation-index="1" label="280">*280</page-number>a merchant is experiencing excessive chargebacks, the banks refer to a figure known as the chargeback ratio, which is simply the percentage of transactions in a given 30-day period that result in a chargeback. For example, if a company conducts 100 credit-card transactions and one chargeback results, the company will have a chargeback ratio of 1%. Typically, if a merchant experiences more than one chargeback per hundred transactions, its chargeback ratio is deemed too high, resulting in fines and, eventually, termination of its accounts, either by the merchant bank or the credit-card processor.</p>
<p id="b306-4">Following the termination of the merchant account at the Bank of Kentucky, the company applied for merchant accounts with a number of other banks. In some instances, the applications, which often bore Harriet’s signature, falsely listed her as the CEO and 100% owner of the company. In other instances, Warshak would complete the applications in his own name but falsely claim that he had never had a merchant account terminated. These prevarications were included in the applications because the prior termination would likely diminish Berkeley’s chances of securing the services of other processors.</p>
<p id="b306-5">Despite its history with the Bank of Kentucky, Berkeley was able to land (or retain) merchant accounts with several processors. However, due to the auto-ship program and an extremely onerous refund policy,<footnotemark>10</footnotemark> Berkeley was repeatedly at risk of crossing the critical 1% chargeback threshold.<footnotemark>11</footnotemark> At company meetings, the chargeback ratio was a frequent topic of discussion, as was the possibility that Berkeley’s accounts would be terminated. To prevent that from happening, a number of strategies were devised to artificially inflate the number of sales transactions and thus the denominator of the charge-back ratio, reducing that crucial ratio. One strategy was called “double-dinging.” That practice involved splitting a single transaction into two, thereby driving up the number of transactions and diminishing the chargeback ratio. A double-ding might entail carving a $59.95 charge into a $54.95 charge for the product itself and a $5.00 charge for shipping. Warshak directed that virtually all sales be double-dinged, and by 2003, triple-dinging was initiated.</p>
<p id="b306-8">Another way the company depressed the chargeback ratio was to make numerous charges to Warshak’s personal credit cards. At Warshak’s behest, Berkeley employees would ring up $1.00 charges on each of his credit cards until their limits were reached. Apparently, the thinking <page-number citation-index="1" label="281">*281</page-number>was that this torrent of additional transactions would dilute the number of charge-backs and keep the ratio under 1%. The same thinking led the company to charge and then refund the credit cards of randomly selected customers. The charges were made without authorization, and if anyone complained about the odd activity on his card, he was told that it was the result of a computer glitch. Through the use of these techniques and others, the company was able to stave off termination of its merchant-bank accounts.</p>
<p id="b307-5">B. Procedural History</p>
<p id="b307-6">In September 2006, a grand jury sitting-in the Southern District of Ohio returned a 112-count indictment charging Warshak, Harriet, TCI, and several others with various crimes related to Berkeley’s business. Warshak was charged with conspiracy to commit mail, wire, and bank fraud (Count 1); mail fraud (Counts 2-13); making false statements to banks (Counts 14,16-22, 24-26, 28); bank fraud (Counts 15, 23, 27); conspiracy to commit and attempt to commit access-device fraud (Count 29); conspiracy to commit money laundering (Count 34); money laundering (Counts 32-98, 102-106, 108); conspiracy to commit misbranding (Count 109); misbranding (Count 110); and, lastly, conspiracy to obstruct a Federal Trade Commission (“FTC”) proceeding (Count 112). Harriet was charged with conspiracy to commit mail, wire, and bank fraud (Count 1); bank fraud (Count 27); making false statements to a bank (Count 28); conspiracy to commit money laundering (Counts 30-31); and money laundering (Counts 99-101, 107). TCI was charged with money laundering (Counts 57-58, 60-73, 79, 83, 91-93).</p>
<p id="b307-7">Before trial, numerous motions were filed. First, Warshak moved to exclude thousands of emails that the government obtained from his Internet Service Providers. That motion was denied. Warshak also moved to bar the government from using any evidence “derived through improper access to privileged attorney-client communications.” Appellant’s Br. at 42. Following a <em>“Kastigar-like” </em>evidentiary hearing at which governmental inspectors testified that they did not make use of any privileged materials, the district court denied the motion. In addition, the defendants requested a continuance, which was denied.</p>
<p id="b307-9">Over fifteen months later, in January 2008, the case proceeded to trial. Approximately six weeks later, the trial ended and the defendants were convicted of the majority of the charges. Warshak was acquitted of Counts 14-22, 24-26, and 28, which charged him with making false statements to banks, and he was also acquitted of Counts 109-110, which charged him with misbranding offenses. Harriet was acquitted of Count 28, which alleged that she made false statements to a bank. She was convicted on Counts 27, 30-31, 99-101, and 107.</p>
<p id="b307-10">As soon as the trial was over, a forfeiture hearing was held, during which the jury heard additional evidence. At the hearing, the defendants attempted to introduce certain evidence that many of Berkeley’s sales were legitimate, but the district court ruled that the evidence was irrelevant. When the hearing concluded, the jury found that the government had established the requisite nexus between certain assets and the crimes of both fraud and money laundering.</p>
<p id="b307-11">On August 27, 2008, the defendants were sentenced. Warshak received a sentence of 25 years of imprisonment. He was also ordered to pay a fine of $93,000 and a special assessment of $9,300. In addition, he was ordered to surrender $459,540,000 in proceeds-money-judgment forfeiture and $44,876,781.68 in money-laundering-<page-number citation-index="1" label="282">*282</page-number>judgment forfeiture. Harriet was sentenced to 24 months of imprisonment, ordered to pay a special assessment of $800, and held jointly and severally liable for the forfeiture judgments. TCI was sentenced to five years of probation and ordered to pay a fine of $160,000 and a special assessment of $6,400.</p>
<p id="b308-4">Following a series of unsuccessful post-trial motions, the defendants timely appealed.</p>
<p id="b308-5">II. ANALYSIS</p>
<p id="b308-6">A. The Search &amp; Seizure of Warshak’s Emails</p>
<p id="b308-7">Warshak argues that the government’s warrantless, <em>ex parte </em>seizure of approximately 27,000 of his private emails constituted a violation of the Fourth Amendment’s prohibition on unreasonable searches and seizures.<footnotemark>12</footnotemark> The government counters that, even if government agents violated the Fourth Amendment in obtaining the emails, they relied in good faith on the Stored Communications Act (“SCA”), <span class="citation no-link">18 U.S.C. §§ 2701</span> et seq., a statute that allows the government to obtain certain electronic communications without procuring a warrant. The government also argues that any hypothetical Fourth Amendment violation was harmless. We find that the government <em>did </em>violate Warshak’s Fourth Amendment rights by compelling his Internet Service Provider (“ISP”) to turn over the contents of his emails. However, we agree that agents relied on the SCA in good faith, and therefore hold that reversal is unwarranted.<footnotemark>13</footnotemark></p>
<p id="b308-11">1. <em>The Stored Communications Act</em></p>
<p id="b308-12">The Stored Communications Act (“SCA”), <span class="citation no-link">18 U.S.C. §§ 2701</span> et seq., “permits a ‘governmental entity’ to compel a service provider to disclose the contents of [electronic] communications in certain circumstances.” <em>Warshak II, </em>532 F.3d at 523. As this court explained in <em>Warshak II:</em></p>
<blockquote id="b308-13">Three relevant definitions bear on the meaning of the compelled-diselosure provisions of the Act. “[Electronic communication service[s]” permit “users ... to send or receive wire or electronic communications,” [18 U.S.C.] § 2510(15), a definition that covers basic e-mail services, <em>see </em>Patricia L. Bellia et ah, <em>Cyberlaw: Problems of Policy and Jurisprudence in the Information Age 584 </em>(2d ed. 2004). “[Electronic storage” is “any temporary, intermediate storage of a wire or electronic communication ... and ... any storage of such communication by an electronic communication ser<page-number citation-index="1" label="283">*283</page-number>vice for purposes of backup protection of such communication.” <span class="citation no-link">18 U.S.C. § 2510</span>(17). “[RJemote computing serviced” provide “computer storage or processing services” to customers, <em><span class="citation no-link">id.</span> </em>§ 2711(2), and are designed for longer-term storage, <em>see </em>Orín S. Kerr, <em>A User’s Guide to the Stored Communications Act, and a Legislator’s Guide to Amending It, </em>72 Geo. Wash. L.Rev. 1208, 1216 (2004).</blockquote>
<blockquote id="b309-5">The compelled-disclosure provisions give different levels of privacy protection based on whether the e-mail is held with an electronic communication service or a remote computing service and based on how long the e-mail has been in electronic storage. The government may obtain the contents of e-mails that are “in electronic storage” with an electronic communication service for 180 days or less “only pursuant to a warrant.” <span class="citation no-link">18 U.S.C. § 2703</span>(a). The government has three options for obtaining communications stored with a remote computing service and communications that have been in electronic storage with an electronic service provider for more than 180 days: (1) obtain a warrant; (2) use an administrative subpoena; or (3) obtain a court order under § 2703(d). <em>Id. </em>§ 2703(a), (b).</blockquote>
<p id="b309-6">532 F.3d at 523-24 (some alterations in original).</p>
<p id="b309-7">2. <em>Factual Background</em></p>
<p id="b309-8">Email was a critical form of communication among Berkeley personnel. As a consequence, Warshak had a number of email accounts with various ISPs, including an account with NuVox Communications. In October 2004, the government formally requested that NuVox prospectively preserve the contents of any emails to or from Warshak’s email account. The request was made pursuant to <span class="citation no-link">18 U.S.C. § 2703</span>(f) and it instructed NuVox to preserve all future messages.<footnotemark>14</footnotemark> NuVox acceded to the government’s request and began preserving copies of Warshak’s incoming and outgoing emails — copies that would not have existed absent the prospective preservation request. Per the government’s instructions, Warshak was not informed that his messages were being archived.</p>
<p id="b309-11">In January 2005, the government obtained a subpoena under § 2703(b) and compelled NuVox to turn over the emails that it had begun preserving the previous year. In May 2005, the government served NuVox with an <em>ex parte </em>court order under § 2703(d) that required NuVox to surrender any additional email messages in Warshak’s account. In all, the government compelled NuVox to reveal the contents of approximately 27,000 emails. Warshak did not receive notice of either the subpoena or the order until May 2006.</p>
<p id="b309-12">3. <em>The Fourth Amendment</em></p>
<p id="b309-13">The Fourth Amendment provides that “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause.... ” U.S. Const, amend. IV. The fundamental purpose of the Fourth Amendment “is to safeguard the privacy and security of individuals against arbitrary invasions by government officials.” <em>Camara v. Mun. Ct., </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U.S. 523, 528</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">87 S.Ct. 1727</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">18 L.Ed.2d 930</a></span> (1967); <em>see Skinner v. Ry. Labor Execs.’ Ass’n, </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#613" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U.S. 602, 613-14</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">109 S.Ct. 1402</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">103 L.Ed.2d 639</a></span> (1989) (“The [Fourth] Amend<page-number citation-index="1" label="284">*284</page-number>ment guarantees the privacy, dignity, and security of persons against certain arbitrary and invasive acts by officers of the Government or those acting at their direction.”).</p>
<p id="b310-4">Not all government actions are invasive enough to implicate the Fourth Amendment. “The Fourth Amendment’s protections hinge on the occurrence of a ‘search,’ a legal term of art whose history is riddled with complexity.” <em>Widgren v. Maple Grove Twp., </em><span class="citation" data-id="792467"><a href="/opinion/792467/kenneth-d-widgren-jr-and-kenneth-d-widgren-sr-v-maple-grove-township/#578" aria-description="Citation for case: Kenneth D. Widgren, Jr. And Kenneth D. Widgren, Sr. v....">429 F.3d 575, 578</a></span> (6th Cir.2005). A “search” occurs when the government infringes upon “an expectation of privacy that society is prepared to consider reasonable.” <em>United States v. Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U.S. 109, 113</a></span>, <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">104 S.Ct. 1652</a></span>, <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">80 L.Ed.2d 85</a></span> (1984). This standard breaks down into two discrete inquiries: “first, has the [target of the investigation] manifested a subjective expectation of privacy in the object of the challenged search? Second, is society willing to recognize that expectation as reasonable?” <em>California v. Ciraolo, </em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#211" aria-description="Citation for case: California v. Ciraolo">476 U.S. 207, 211</a></span>, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">106 S.Ct. 1809</a></span>, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">90 L.Ed.2d 210</a></span> (1986) (citing <em>Smith v. Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#740" aria-description="Citation for case: Smith v. Maryland">442 U.S. 735, 740</a></span>, <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">99 S.Ct. 2577</a></span>, <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">61 L.Ed.2d 220</a></span> (1979)).</p>
<p id="b310-5">Turning first to the subjective component of the test, we find that Warshak plainly manifested an expectation that his emails would be shielded from outside scrutiny. As he notes in his brief, his “entire business and personal life was contained within the ... emails seized.” Appellant’s Br. at 39-40. Given the often sensitive and sometimes damning substance of his emails,<footnotemark>15</footnotemark> we think it highly unlikely that Warshak expected them to be made public, for people seldom unfurl their dirty laundry in plain view. <em>See, e.g., United States v. Maxwell, </em><span class="citation" data-id="7269941"><a href="/opinion/7351719/united-states-v-maxwell/#417" aria-description="Citation for case: United States v. Maxwell">45 M.J. 406, 417</a></span> (C.A.A.F.1996) (“[T]he tenor and content of e-mail conversations between appellant and his correspondent, ‘Launehboy,’ reveal a[n] ... expectation that the conversations were private.”). Therefore, we conclude that Warshak had a subjective expectation of privacy in the contents of his emails.</p>
<p id="b310-8">The next question is whether society is prepared to recognize that expectation as reasonable. <em>See Smith, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#740" aria-description="Citation for case: Smith v. Maryland">442 U.S. at 740</a></span>, <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">99 S.Ct. 2577</a></span>. This question is one of grave import and enduring consequence, given the prominent role that email has assumed in modern communication. <em>Cf. Katz, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U.S. at 352</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span> (suggesting that the Constitution must be read to account for “the vital role that the public telephone has come to play in private communication”). Since the advent of email, the telephone call and the letter have waned in importance, and an explosion of Internet-based communication has taken place. People are now able to send sensitive and intimate information, instantaneously, to friends, family, and colleagues half a world away. Lovers exchange sweet nothings, and businessmen swap ambitious plans, all with the click of a mouse button. Commerce has also taken hold in email. Online purchases are often documented in email accounts, and email is frequently used to remind patients and clients of imminent appointments. In short, “account” is an apt word for the conglomeration of stored messages that comprises an email account, as it provides an account of its owner’s life. By obtaining access to someone’s email, government agents gain the ability to peer deeply into his activities. Much hinges, therefore, on whether the government is permitted to request that a commercial ISP turn over the contents of a subscriber’s emails without triggering the machinery of the Fourth Amendment.</p>
<p id="b311-4"><page-number citation-index="1" label="285">*285</page-number>In confronting this question, we take note of two bedrock principles. First, the very fact that information is being passed through a communications network is a paramount Fourth Amendment consideration. <em>See ibid.; United States v. U.S. Dist. Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U.S. 297, 313</a></span>, <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">92 S.Ct. 2125</a></span>, <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">32 L.Ed.2d 752</a></span> (1972) (“[T]he broad and unsuspected governmental incursions into conversational privacy which electronic surveillance entails necessitate the application of Fourth Amendment safeguards.”). Second, the Fourth Amendment must keep pace with the inexorable march of technological progress, or its guarantees will wither and perish. <em>See Kyllo v. United States, </em><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/#34" aria-description="Citation for case: Kyllo v. United States">533 U.S. 27, 34</a></span>, <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">121 S.Ct. 2038</a></span>, <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">150 L.Ed.2d 94</a></span> (2001) (noting that evolving technology must not be permitted to “erode the privacy guaranteed by the Fourth Amendment”); <em>see also </em>Orín S. Kerr, <em>Applying the Fourth Amendment to the Internet: A General Approach, </em>62 Stan. L.Rev. 1005, 1007 (2010) (arguing that “the differences between the facts of physical space and the facts of the Internet require courts to identify new Fourth Amendment distinctions to maintain the function of Fourth Amendment rules in an online environment”).</p>
<p id="b311-5">With those principles in mind, we begin our analysis by considering the manner in which the Fourth Amendment protects traditional forms of communication. In <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>the Supreme Court was asked to determine how the Fourth Amendment applied in the context of the telephone. There, government agents had affixed an electronic listening device to the exterior of a public phone booth, and had used the device to intercept and record several phone conversations. <em>See </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#348" aria-description="Citation for case: Katz v. United States">389 U.S. at 348</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span>. The Supreme Court held that this constituted a search under the Fourth Amendment, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States"><em>see id. </em>at 353</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span>, notwithstanding the fact that the telephone company had the capacity to monitor and record the calls, <em>see Smith, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#746" aria-description="Citation for case: Smith v. Maryland">442 U.S. at 746-47</a></span>, <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">99 S.Ct. 2577</a></span> (Stewart, J., dissenting). In the eyes of the Court, the caller was “surely entitled to assume that the words he utter[ed] into the mouthpiece w[ould] not be broadcast to the world.” <em>Katz, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U.S. at 352</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span>. The Court’s holding in <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>has since come to stand for the broad proposition that, in many contexts, the government infringes a reasonable expectation of privacy when it surreptitiously intercepts a telephone call through electronic means. <em>Smith, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#746" aria-description="Citation for case: Smith v. Maryland">442 U.S. at 746</a></span>, <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">99 S.Ct. 2577</a></span> (Stewart, J., dissenting) (“[S]ince <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>it has been abundantly clear that telephone conversations are fully protected by the Fourth and Fourteenth Amendments.”).</p>
<p id="b311-7">Letters receive similar protection. <em>See Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#114" aria-description="Citation for case: United States v. Jacobsen">466 U.S. at 114</a></span>, <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">104 S.Ct. 1652</a></span> (“Letters and other sealed packages are in the general class of effects in which the public at large has a legitimate expectation of privacy[.]”); <em>Ex Parte Jackson, </em><span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U.S. 727, 733</a></span>, <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/" aria-description="Citation for case: Ex Parte Jackson">24 L.Ed. 877</a></span> (1877). While a letter is in the mail, the police may not intercept it and examine its contents unless they first obtain a warrant based on probable cause. <em><span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/" aria-description="Citation for case: Ex Parte Jackson">Ibid.</a></span> </em>This is true despite the fact that sealed letters are handed over to perhaps dozens of mail carriers, any one of whom could tear open the thin paper envelopes that separate the private words from the world outside. Put another way, trusting a letter to an intermediary does not necessarily defeat a reasonable expectation that the letter will remain private. <em>See Katz, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U.S. at 351</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span> (“[W]hat [a person] seeks to preserve as private, even in an area accessible to the public, may be constitutionally protected.”).</p>
<p id="b311-8">Given the fundamental similarities between email and traditional forms of communication, it would defy common sense <page-number citation-index="1" label="286">*286</page-number>to afford emails lesser Fourth Amendment protection. <em>See </em>Patricia L. Bellia &amp; Susan Freiwald, <em>Fourth Amendment Protection for Stored E-Mail, </em><span class="citation no-link">2008 U. Chi. Legal F. 121</span>, 135 (2008) (recognizing the need to “eliminate the strangely disparate treatment of mailed and telephonic communications on the one hand and electronic communications on the other”); <em>City of Ontario v. Quon, </em>— U.S. -, <span class="citation" data-id="6681698"><a href="/opinion/6796843/city-of-ontario-v-quon/#2631" aria-description="Citation for case: City of Ontario v. Quon">130 S.Ct. 2619, 2631</a></span>, <span class="citation" data-id="6681698"><a href="/opinion/6796843/city-of-ontario-v-quon/" aria-description="Citation for case: City of Ontario v. Quon">177 L.Ed.2d 216</a></span> (2010) (implying that “a search of [an individual’s] personal e-mail account” would be just as intrusive as “a wiretap on his home phone line”); <em>United States v. Forrester, </em><span class="citation" data-id="1445123"><a href="/opinion/1445123/united-states-v-forrester/#511" aria-description="Citation for case: United States v. Forrester">512 F.3d 500, 511</a></span> (9th Cir.2008) (holding that “[t]he privacy interests in [mail and email] are identical”). Email is the technological scion of tangible mail, and it plays an indispensable part in the Information Age. Over the last decade, email has become “so pervasive that some persons may consider [it] to be [an] essential means or necessary instrument! ] for self-expression, even self-identification.” <em>Quon, </em><span class="citation" data-id="6681698"><a href="/opinion/6796843/city-of-ontario-v-quon/#2630" aria-description="Citation for case: City of Ontario v. Quon">130 S.Ct. at 2630</a></span>. It follows that email requires strong protection under the Fourth Amendment; otherwise, the Fourth Amendment would prove an ineffective guardian of private communication, an essential purpose it has long been recognized to serve. <em>See U.S. Dist. Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U.S. at 313</a></span>, <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">92 S.Ct. 2125</a></span>; <em>United States v. Waller, </em><span class="citation" data-id="358724"><a href="/opinion/358724/united-states-v-irvin-j-waller/#587" aria-description="Citation for case: United States v. Irvin J. Waller">581 F.2d 585, 587</a></span> (6th Cir.1978) (noting the Fourth Amendment’s role in protecting “private communications”). As some forms of communication begin to diminish, the Fourth Amendment must recognize and protect nascent ones that arise. <em>See Warshak I, </em>490 F.3d at 473 (“It goes without saying that like the telephone earlier in our history, e-mail is an ever-increasing mode of private communication, and protecting shared communications through this medium is as important to Fourth Amendment principles today as protecting telephone conversations has been in the past.”).</p>
<p id="b312-7">If we accept that an email is analogous to a letter or a phone call, it is manifest that agents of the government cannot compel a commercial ISP to turn over the contents of an email without triggering the Fourth Amendment. An ISP is the intermediary that makes email communication possible. Emails must pass through an ISP’s servers to reach their intended recipient. Thus, the ISP is the functional equivalent of a post office or a telephone company. As we have discussed above, the police may not storm the post office and intercept a letter, and they are likewise forbidden from using the phone system to make a clandestine recording of a telephone call — unless they get a warrant, that is. <em>See Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#114" aria-description="Citation for case: United States v. Jacobsen">466 U.S. at 114</a></span>, <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">104 S.Ct. 1652</a></span>; <em>Katz, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States">389 U.S. at 353</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span>. It only stands to reason that, if government agents compel an ISP to surrender the contents of a subscriber’s emails, those agents have thereby conducted a Fourth Amendment search, which necessitates compliance with the warrant requirement absent some exception.</p>
<p id="b312-8">In <em>Warshak I, </em>the government argued that this conclusion was improper, pointing to the fact that NuVox contractually reserved the right to access Warshak’s emails for certain purposes. While we acknowledge that a subscriber agreement might, in some cases, be sweeping enough to defeat a reasonable expectation of privacy in the contents of an email account, <em>see Warshak I, </em>490 F.3d at 473; <em>Warshak II, </em>532 F.3d at 526-27, we doubt that will be the case in most situations, and it is certainly not the case here.</p>
<p id="b312-9">As an initial matter, it must be observed that the mere <em>ability </em>of a third-party intermediary to access the contents of a communication cannot be sufficient to extinguish a reasonable expectation of priva<page-number citation-index="1" label="287">*287</page-number>cy. In <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>the Supreme Court found it reasonable to expect privacy during a telephone call despite the ability of an operator to listen in. <em>See Smith, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#746" aria-description="Citation for case: Smith v. Maryland">442 U.S. at 746-47</a></span>, <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">99 S.Ct. 2577</a></span> (Stewart, J., dissenting). Similarly, the ability of a rogue mail handler to rip open a letter does not make it unreasonable to assume that sealed mail will remain private on its journey across the country. Therefore, the threat or possibility of access is not decisive when it comes to the reasonableness of an expectation of privacy.</p>
<p id="b313-5">Nor is the <em>right </em>of access. As the Electronic Frontier Foundation points out in its <em>amicus </em>brief, at the time <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>was decided, telephone companies had a right to monitor calls in certain situations. Specifically, telephone companies could listen in when reasonably necessary to “protect themselves and their properties against the improper and illegal use of their facilities.” <em>Bubis v. United States, </em><span class="citation" data-id="277548"><a href="/opinion/277548/alvin-bubis-v-united-states/#648" aria-description="Citation for case: Alvin Bubis v. United States">384 F.2d 643, 648</a></span> (9th Cir.1967). In this case, the NuVox subscriber agreement tracks that language, indicating that “NuVox <em>may </em>access and use individual Subscriber information in the operation of the Service and as necessary to protect the Service.” Acceptable Use Policy, <em>available at </em>http:// business.windstream.com/Legal/acceptable Use.htm (last visited Aug. 12, 2010). Thus, under <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>the degree of access granted to NuVox does not dimmish the reasonableness of Warshak’s trust in the privacy of his emails.<footnotemark>16</footnotemark></p>
<p id="b313-6">Our conclusion finds additional support in the application of Fourth Amendment doctrine to rented space. Hotel guests, for example, have a reasonable expectation of privacy in their rooms. <em>See United States v. Allen, </em><span class="citation" data-id="735355"><a href="/opinion/735355/united-states-v-russell-b-allen/#699" aria-description="Citation for case: United States v. Russell B. Allen">106 F.3d 695, 699</a></span> (6th Cir.1997). This is so even though maids routinely enter hotel rooms to replace the towels and tidy the furniture. Similarly, tenants have a legitimate expectation of privacy in their apartments. <em>See United States v. Washington, </em><span class="citation" data-id="1448043"><a href="/opinion/1448043/united-states-v-washington/#284" aria-description="Citation for case: United States v. Washington">573 F.3d 279, 284</a></span> (6th Cir.2009). That expectation persists, regardless of the incursions of handymen to fix leaky faucets. Consequently, we are convinced that some degree of routine access is hardly dispositive with respect to the privacy question.</p>
<p id="b313-9">Again, however, we are unwilling to hold that a subscriber agreement will <em>never </em>be broad enough to snuff out a reasonable expectation of privacy. As the panel noted in <em>Warshak I, </em>if the ISP expresses an intention to “audit, inspect, and monitor” its subscriber’s emails, that might be enough to render an expectation of privacy unreasonable. <em>See </em>490 F.3d at 472-73 (quoting <em>United States v. Simons, </em><span class="citation" data-id="767973"><a href="/opinion/767973/united-states-v-mark-l-simons/#398" aria-description="Citation for case: United States v. Mark L. Simons">206 F.3d 392, 398</a></span> (4th Cir.2000)). But where, as here, there is no such statement, the ISP’s “control over the [emails] and ability to access them under certain limited circumstances will not be enough to overcome an expectation of privacy.” <span class="citation" data-id="767973"><a href="/opinion/767973/united-states-v-mark-l-simons/#473" aria-description="Citation for case: United States v. Mark L. Simons"><em>Id. </em>at 473</a></span>.</p>
<p id="b313-10">We recognize that our conclusion may be attacked in light of the Supreme Court’s decision in <em>United States v. Miller, </em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">425 U.S. 435</a></span>, <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">96 S.Ct. 1619</a></span>, <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">48 L.Ed.2d 71</a></span> (1976). In <em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Miller</a></span>, </em>the Supreme Court held that a bank depositor does not have a reasonable expectation of privacy in the contents of bank records, checks, and deposit slips. <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#442" aria-description="Citation for case: United States v. Miller"><em>Id. </em>at 442</a></span>, <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">96 S.Ct. 1619</a></span>. The Court’s holding in <em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Miller</a></span> </em>was based on the fact that bank documents, “including financial statements and deposit slips, contain <page-number citation-index="1" label="288">*288</page-number>only information voluntarily conveyed to the banks and exposed to their employees in the ordinary course of business.” <em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Ibid.</a></span> </em>The Court noted,</p>
<blockquote id="b314-4">The depositor takes the risk, in revealing his affairs to another, that the information will be conveyed by that person to the Government.... [T]he Fourth Amendment does not prohibit the obtaining of information revealed to a third party and conveyed by him to Government authorities, even if the information is revealed on the assumption that it will be used only for a limited purpose and the confidence placed in the third party will not be betrayed.</blockquote>
<p id="b314-5"><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#443" aria-description="Citation for case: United States v. Miller"><em>Id. </em>at 443</a></span>, <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">96 S.Ct. 1619</a></span> (citations omitted).</p>
<p id="b314-6">But <em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Miller</a></span> </em>is distinguishable. First, <em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Miller</a></span> </em>involved simple business records, as opposed to the potentially unlimited variety of “confidential communications” at issue here. <em>See <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">ibid.</a></span> </em>Second, the bank depositor in <em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Miller</a></span> </em>conveyed information to the bank so that the bank could put the information to use “in the ordinary course of business.” <em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Ibid.</a></span> </em>By contrast, Warshak received his emails through NuVox. NuVox was an <em>intermediary, </em>not the intended recipient of the emails. <em>See </em>Bellia &amp; Freiwald, <em>Stored E-Mail, </em>2008 U. Chi. Legal F. at 165 (“[W]e view the best analogy for this scenario as the cases in which a third party carries, transports, or stores property for another. In these cases, as in the stored e-mail case, the customer grants access to the ISP because it is essential to the customer’s interests.”). Thus, <em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Miller</a></span> </em>is not controlling.</p>
<p id="b314-7">Accordingly, we hold that a subscriber enjoys a reasonable expectation of privacy in the contents of emails “that are stored with, or sent or received through, a commercial ISP.” <em>Warshak I, </em>490 F.3d at 473; <em>see Forrester, </em><span class="citation" data-id="1445123"><a href="/opinion/1445123/united-states-v-forrester/#511" aria-description="Citation for case: United States v. Forrester">512 F.3d at 511</a></span> (suggesting that “[t]he contents [of email messages] may deserve Fourth Amendment protection”). The government may not compel a commercial ISP to turn over the contents of a subscriber’s emails without first obtaining a warrant based on probable cause. Therefore, because they did not obtain a warrant, the government agents violated the Fourth Amendment when they obtained the contents of Warshak’s emails. Moreover, to the extent that the SCA purports to permit the government to obtain such emails warrantlessly, the SCA is unconstitutional.</p>
<p id="b314-9">4. <em>Good-Faith Reliance</em></p>
<p id="b314-10">Even though the government’s search of Warshak’s emails violated the Fourth Amendment, the emails are not subject to the exclusionary remedy if the officers relied in good faith on the SCA to obtain them. <em>See Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#349" aria-description="Citation for case: Illinois v. Krull">480 U.S. at 349-50</a></span>, <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">107 S.Ct. 1160</a></span>. In <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull</a></span>, </em>the Supreme Court noted that the exclusionary rule’s purpose of deterring law enforcement officers from engaging in unconstitutional conduct would not be furthered by holding officers accountable for mistakes of the legislature. <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Ibid.</a></span> </em>Thus, even if a statute is later found to be unconstitutional, an officer “cannot be expected to question the judgment of the legislature.” <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Ibid.</a></span> </em>However, an officer cannot “be said to have acted in good-faith reliance upon a statute if its provisions are such that a reasonable officer should have known that the statute was unconstitutional.” <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#355" aria-description="Citation for case: Illinois v. Krull"><em>Id. </em>at 355</a></span>, 107 5. Ct. 1160.</p>
<p id="b314-12">Naturally, Warshak argues that the provisions of the SCA at issue in this case were plainly unconstitutional. He argues that any reasonable law enforcement officer would have understood that a warrant based on probable cause would be required to compel the production of private emails. In making this argument, he leans heavily on <em>Warshak I, </em>which opined that the SCA permits agents to engage in searches “that <page-number citation-index="1" label="289">*289</page-number>clearly do not comport with the Fourth Amendment.” 490 F.3d at 477.</p>
<p id="b315-5">However, we disagree that the SCA is so conspicuously unconstitutional as to preclude good-faith reliance. As we noted in <em>Warshak II, </em>“[t]he Stored Communications Act has been in existence since 1986 and to our knowledge has not been the subject of any successful Fourth Amendment challenges, in any context, whether to § 2703(d) or to any other provision.” 532 F.3d at 531. Furthermore, given the complicated thicket of issues that we were required to navigate when passing on the constitutionality of the SCA, it was not plain or obvious that the SCA was unconstitutional, and it was therefore reasonable for the government to rely upon the SCA in seeking to obtain the contents of Warshak’s emails.<footnotemark>17</footnotemark></p>
<p id="b315-6">But the good-faith reliance inquiry does not end with the facial validity of the statute at issue. In <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull</a></span>, </em>the Supreme Court hinted that the good-faith exception does not apply if the government acted “outside the scope of the statute” on which it purported to rely. <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">480 U.S. at 360</a></span> n. 17, <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">107 S.Ct. 1160</a></span>. It should be noted that this portion of the <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull</a></span> </em>Court’s opinion was merely dicta, and it appears that we have yet to pass on the question. However, it seems evident that an officer’s failure to adhere to the boundaries of a given statute should preclude him from relying upon it in the face of a constitutional challenge.<footnotemark>18</footnotemark> Once the officer steps outside the scope of an unconstitutional statute, the mistake is no longer the legislature’s, but the officer’s. <em>See <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">ibid.</a></span> </em>(“In that context, the relevant actors are not legislators or magistrates, but police officers who concededly are engaged in the often competitive enterprise of ferreting out crime.” (citation and internal quotation marks omitted)). Therefore, use of the exclusionary rule is once again efficacious in deterring officers from engaging in conduct that violates the Constitution. <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Ibid.</a></span></em></p>
<p id="b315-10">Warshak argues that the government violated several provisions of the SCA and should therefore be precluded from arguing good-faith reliance. First, Warshak argues that the government violated the SCA’s notice provisions. Under § 2703(b)(1)(B), the government must provide notice to an account holder if it seeks to compel the disclosure of his emails through either a § 2703(b) subpoena or a § 2703(d) order. However, § 2705 permits the government to delay notification in certain situations. The initial period of delay is 90 days, but the government may seek to extend that period in 90-day increments. In this case, the government issued both a § 2703(b) subpoena and a § 2703(d) order to NuVox, seeking disclosure of Warshak’s emails. At the time, the government made the. requisite showing that notice should be delayed. However, the government did not seek to renew the period of delay. In all, the government failed to inform Warshak of either the subpoena or the order for over a year.</p>
<p id="b315-11">Conceding that it violated the notice provisions, the government argues that such violations are irrelevant to the issue of whether it reasonably relied on the <page-number citation-index="1" label="290">*290</page-number>SCA in <em>obtaining </em>the contents of Warshak’s emails. We agree. As the government notes, the violations occurred <em>after </em>the emails had been obtained. Thus, the mistakes at issue had no bearing on the constitutional violations. Because the exclusionary rule was designed to deter constitutional violations, we decline to invoke it in this situation.</p>
<p id="b316-4">But Warshak does not hang his hat exclusively on the government’s violations of the SCA’s notice provisions. He also argues that the government exceeded its authority under another SCA provision— § 2703(f) — by requesting NuVox to engage in <em>prospective </em>preservation of his future emails.<footnotemark>19</footnotemark> Under § 2703(f), “[a] provider of wire or electronic communication services or a remote computing service, upon the request of a governmental entity, shall take all necessary steps to <em>preserve </em>records and other evidence <em>in its possession </em>pending the issuance of a court order or other process.” <span class="citation no-link">18 U.S.C. § 2703</span>(f) (emphasis added). Warshak argues that this statute permits only <em>retrospective </em>preservation — in other words, preservation of emails already in existence. He notes that the Department of Justice (“DOJ”) generally agrees with his construction of the statute, pointing to the DOJ’s own computer-surveillance manual, which states: “[Section] 2703(f) letters should not be used prospectively to order providers to preserve records not yet created. If agents want providers to record information about future electronic communications, they should comply with the [Wiretap Act and the Pen/Trap statute].”<footnotemark>20</footnotemark></p>
<p id="b316-8">Ultimately, however, this statutory violation, whether it occurred or not,<footnotemark>21</footnotemark> is irrelevant to the issue of good-faith reliance. The question here is whether the government relied in good faith on § 2703(b) and § 2703(d) to <em>obtain </em>copies of Warshak’s emails. True, the government might not have been able to gain access to the emails without the prospective preservation request, as it was NuYox’s practice to delete all emails once they were downloaded to the account holder’s computer. Thus, in a sense, the government’s use of § 2703© was a but-for cause of the constitutional violation. But the actual violation at issue was obtaining the emails, and the government did not rely on § 2703® specifically to do that. Instead, the government relied on § 2703(b) and § 2703(d). The proper inquiry, therefore, is whether the government violated either of <em>those </em>provisions, and the preservation request is of no consequence to that inquiry.</p>
<p id="b316-9">Warshak’s next argument is that the government violated § 2703(d) by failing to provide any particularized factual basis <page-number citation-index="1" label="291">*291</page-number>when seeking an order for disclosure. Under § 2703(d), such an order “shall issue only if the governmental entity offers specific and articulable facts showing that there are reasonable grounds to believe that the contents of a wire or electronic communication ... are relevant and material to an ongoing criminal investigation.”</p>
<p id="b317-5">To the extent that he is arguing that the government’s application was insufficient, Warshak is wrong. The government’s application indicated that it was “investigating a complex, large-scale mail and wire fraud operation based in Cincinnati, Ohio.” The application also indicated that “interviews of current and former employees of the target company suggest that electronic mail is a vital communication tool that has been used to perpetuate the fraudulent conduct.” Additionally, the application observed that “various sources [have verified] that NuVox provides electronic communications services to certain individual(s) [under] investigation.” In light of these statements, it is clear that the application was, in fact, supported by specific and articulable facts, especially given the diminished standard that applies to § 2703(d) applications. <em>See United States v. Perrine, </em><span class="citation" data-id="170424"><a href="/opinion/170424/united-states-v-perrine/#1202" aria-description="Citation for case: United States v. Perrine">518 F.3d 1196, 1202</a></span> (10th Cir.2008) (noting that “the ‘specific and articulable facts’ standard derives from the Supreme Court’s decision in <em>Terry </em>”); <em>Warshak I, </em>490 F.3d at 463 (“The parties agree that the standard of proof for a court order — ‘specific and articulable facts showing that there are reasonable grounds to believe that the contents ... or records ... are relevant and material to an ongoing criminal investigation’ — falls short of probable cause.”).</p>
<p id="b317-6">Finally, Warshak argues that a finding of good-faith reliance is improper because the government presented the magistrate with an erroneous definition of the term “electronic storage.” As noted above, if an email is in electronic storage for less than 180 days, the government may not compel its disclosure without a warrant. <span class="citation no-link">18 U.S.C. § 2703</span>(a). In applying for the subpoena and the order that eventually resulted in the disclosure of Warshak’s NuVox emails, the government suggested to the magistrate that an email is not in electronic storage if it has already been “accessed, viewed, or downloaded.” Warshak argues that this definition of electronic storage does not comport with the Ninth Circuit’s decision in <em>Theofel v. Farey-Jones, </em><span class="citation" data-id="8408646"><a href="/opinion/8438109/theofel-v-farey-jones/#1071" aria-description="Citation for case: Theofel v. Farey-Jones">359 F.3d 1066, 1071</a></span> (9th Cir.2004), which held that “prior access is irrelevant to whether the [emails] at issue were in electronic storage.” Warshak further argues that, because the government failed to mention the Ninth Circuit’s definition, it “usurped the court’s function to determine whether an email ... [is] in ‘electronic storage[.]’ ” Appellant’s Br. at 38.</p>
<p id="b317-8">As an initial matter, it is manifest that the decisions of the Ninth Circuit are not binding on courts in this circuit. It therefore cannot be said that the government somehow violated § 2703 by failing to cite an out-of-circuit decision that it thought to be wrongly decided. Incidentally, the government is not alone in thinking that the Ninth Circuit’s definition of electronic storage is incorrect. One commentator has noted that <em>“Theofel </em>is quite implausible and hard to square with the statutory test.” Kerr, <em>A User’s Guide to the Stored Communications Act, </em>72 Geo. Wash. L.Rev. at 1217; <em>see also United States v. Weaver, </em><span class="citation" data-id="1758661"><a href="/opinion/1758661/united-states-v-weaver/#773" aria-description="Citation for case: United States v. Weaver">636 F.Supp.2d 769, 773</a></span> (C.D.Ill.2009) (“Previously opened emails stored by Microsoft for Hotmail users are not in electronic storage, and the Government can obtain copies of such emails using a trial subpoena.”).</p>
<p id="b317-9">Furthermore, it does a disservice to the magistrate judge to suggest that the government usurped the role of the court. <page-number citation-index="1" label="292">*292</page-number>The government’s application did include a proposed definition of the term “electronic storage.” That does not mean, however, that the magistrate judge unhesitatingly received that definition, and, as the government notes, the magistrate “presumably [had] the opportunity to consider and review relevant precedent.” Appellee’s Br. at 117.</p>
<p id="b318-4">Consequently, we find that, although the government violated the Fourth Amendment, the exclusionary rule does not apply, as the government relied in good faith on § 2703(b) and § 2703(d) to access the contents of Warshak’s emails.<footnotemark>22</footnotemark></p>
<p id="b318-5">B. The Kastigar-Like Hearing</p>
<p id="b318-6">1. <em>Background</em></p>
<p id="b318-7">During the government’s investigation of Berkeley, case agents came into possession of myriad documents that were ostensibly subject to the attorney-client privilege. Many of the documents were obtained during a March 16, 2005 search of Berkeley’s headquarters, in which agents copied the contents of over 90 computers. Other documents were procured earlier through the subpoena and court order issued to NuVox, which granted investigators access to the contents of Warshak’s email accounts. In all, case agents had access to approximately “60,000 email communications from or to attorneys representing Berkeley and Warshak, communications facially and presumptively protected by the attorney-client privilege.” Appellant’s Br. at 41.</p>
<p id="b318-9">On July 5, 2007, Warshak filed a “motion to bar the government from using the evidence obtained in violation of the defendants’ attorney-client and work product privileges and to dismiss the indictment since privileged material was used to secure it.” <em>United States v. Warshak, </em>No. 1:06-CR-00111, <span class="citation no-link">2007 WL 3306603</span>, at *1 (S.D.Ohio Nov.5, 2007). In the motion, the defendants requested that the district court hold a hearing “in the framework of <em>Kastigar v. United States, </em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">406 U.S. 441</a></span>, <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">92 S.Ct. 1653</a></span>, <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">32 L.Ed.2d 212</a></span> (1972), at which the government would bear the burden of establishing that its case was untainted by attorney-client and work product privileged materials.” <em>Warshak, </em><span class="citation no-link">2007 WL 3306603</span>, at *1. To an extent, the district court granted the motion, setting a <em>“Kasti</em>par-like” hearing with the “narrow purpose of eliciting the sworn testimony of government agents as to their handling of evidence.” <em><span class="citation no-link">Ibid.</span> </em>In ordering the hearing, the district court “found that [the] [defendants had raised enough of a question about the amount of time U.S. Postal Inspector Alejandro Almaguer (‘Almaguer’) possessed privileged data, as well as the government’s methodology in screening data for privileged information, to merit a response.” <em><span class="citation no-link">Ibid.</span></em></p>
<p id="b318-10">The hearing was held on September 27 and 28, 2007. During the hearing, “the government proffered evidence and the testimony of Almaguer, the [defendants were afforded [an] opportunity to cross-examine Almaguer and examine other agents on direct, and the parties argued their respective positions concerning the <page-number citation-index="1" label="293">*293</page-number>propriety of the government action in this case.” <em><span class="citation no-link">Ibid.</span> </em>In addition, the defendants called Peter Horstmann, an expert witness “who used software to analyze the electronic documents the government produced to [the] [defendants.” <em><span class="citation no-link">Ibid.</span></em></p>
<p id="b319-5">After the hearing, the district court held that the government had satisfied its burden, stating as follows:</p>
<blockquote id="b319-6">The [c]ourt’s original concerns that triggered the grant of the <em>“Kastigar-kke” </em>evidentiary hearing were rooted in the amount of time that Almaguer allegedly had access to privileged materials, and in the fact the government had proffered no sworn statements backing its contention that it did not use privileged materials to obtain witness proffers. The government has completely allayed the [c]ourt’s concerns. The United States has met its burden to demonstrate its agents have acted properly and that its case is untainted by privileged information.</blockquote>
<p id="b319-7"><span class="citation no-link"><em>Id. </em>at *8</span>.</p>
<p id="b319-8">2. <em>The Adequacy of the Government’s Presentation</em></p>
<p id="b319-9">Warshak argues that the <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span></em>like hearing was inadequate. More precisely, he argues that the district court failed to “hold[] the government to the burden prescribed by <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>and subsequent cases applying it.” Appellant’s Br. at 48. He complains that the district court “simply accepted the government’s blanket denials that it used privileged materials in preparing its case against defendants, and shifted the burden to [him] to show that privileged materials contributed to the return of the indictment.” <em>Ibid, </em>(internal citations omitted). In short, he argues that the district court improperly loosened the stringent demands of <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span>.</em></p>
<p id="b319-10">In <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span>, </em>the Supreme Court held that when a witness is compelled to give incriminating testimony under a grant of statutory immunity and is thereafter prosecuted for any matter related to the compelled testimony, the government must shoulder the “heavy burden of proving that all of the evidence it proposes to use was derived from legitimate independent sources.” <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#461" aria-description="Citation for case: Kastigar v. United States">406 U.S. at 461-62</a></span>, <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">92 S.Ct. 1653</a></span>; <em>see also United States v. Turner, </em><span class="citation" data-id="563258"><a href="/opinion/563258/united-states-v-diane-turner-90-1546-edwin-leon-turner-90-1547/#224" aria-description="Citation for case: United States v. Diane Turner (90-1546), Edwin Leon...">936 F.2d 221, 224</a></span> (6th Cir.1991). “This burden of proof ... is not limited to a negation of taint; rather, it imposes on the prosecution the affirmative duty to prove that the evidence it proposes to use is derived from a legitimate source wholly independent of the compelled testimony.” <em>Kastigar, </em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#460" aria-description="Citation for case: Kastigar v. United States">406 U.S. at 460</a></span>, <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">92 S.Ct. 1653</a></span>.</p>
<p id="b319-12">While <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>is clearly concerned with the use of testimony obtained despite an assertion of the Fifth Amendment privilege against self-incrimination, this court has suggested that <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>concerns may arise in the context of other privileges, such as the privilege accorded to attorney-client communications. Specifically, this court has hinted, in dicta, that “the leaking of privileged materials to investigators would raise the spectre of Kastigar-like evidentiary hearings.” <em>In re Grand Jury Subpoenas, </em><span class="citation" data-id="794974"><a href="/opinion/794974/in-re-grand-jury-subpoenas-04-124-03-04-124-05/#517" aria-description="Citation for case: In Re Grand Jury Subpoenas 04-124-03 &amp; 04-124-05">454 F.3d 511, 517</a></span> (6th Cir.2006). However, no other appellate court appears to have joined us in suggesting that <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>is implicated whenever investigators come into possession of materials subject to the attorney-client privilege.</p>
<p id="b319-13">One circuit, the Fourth, has engaged in a fairly lengthy analysis of Kastigar’s applicability in the arena of non-constitutional privileges. In <em>United States v. Squillacote, </em><span class="citation" data-id="2967273"><a href="/opinion/2967273/united-states-v-squillacote/" aria-description="Citation for case: United States v. Squillacote">221 F.3d 542</a></span> (4th Cir.2000), the Fourth Circuit was faced with a scenario in which government investigators had legally conducted electronic surveillance on several defendants pursuant to the Foreign <page-number citation-index="1" label="294">*294</page-number>Intelligence Surveillance Act.<footnotemark>23</footnotemark> During the surveillance, the agents heard and recorded a number of conversations between one of the defendants and her psychotherapists. Subsequently, the defendants “moved to suppress any evidence derived from the privileged communications,” arguing that “they were entitled to a hearing to vindicate the principles set forth by the Supreme Court in <em>[Kastigar </em>].” <span class="citation" data-id="2967273"><a href="/opinion/2967273/united-states-v-squillacote/#558" aria-description="Citation for case: United States v. Squillacote"><em>Id. </em>at 558</a></span>. Ultimately, the court determined that <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>was “simply ... not applicable.” <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Ibid.</a></span></em></p>
<p id="b320-4">In so holding, the <em><span class="citation" data-id="2967273"><a href="/opinion/2967273/united-states-v-squillacote/" aria-description="Citation for case: United States v. Squillacote">Squillacote</a></span> </em>court began by conceding that the conversations at issue, which the government had obtained during surveillance, were privileged. According to the court, “[t]he question, then, [was] whether the mere existence of this privileged information br[ought] to bear the full weight of <em>Kastigar.” Id. </em>at 559. The court held that it did not, finding that “a <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>analysis is not triggered by the existence of evidence protected by a privilege, but instead by the government’s <em>effort to compel </em>a witness to testify over the witness’s claim of privilege.” <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Ibid.</a></span> </em>(emphasis added). However, the court also opined “that <em>Kastigar-\Ske </em>protections may be required in cases involving testimony compelled over the assertion of a non-constitutional privilege.” <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Ibid.</a></span> </em>Nonetheless, in concluding its analysis, the court reiterated that “because the government’s right to compel testimony in the face of a claim of privilege is the issue at the heart of <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span>, </em>its protections do not apply in cases where there is privileged evidence, but no compelled testimony.” <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#560" aria-description="Citation for case: Kastigar v. United States"><em>Id. </em>at 560</a></span>. We agree, and hold that, absent compelled testimony, the full protections of <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>are inapplicable.</p>
<p id="b320-6">As further justification for its holding in <em><span class="citation" data-id="2967273"><a href="/opinion/2967273/united-states-v-squillacote/" aria-description="Citation for case: United States v. Squillacote">Squillacote</a></span>, </em>the Fourth Circuit observed that “suppression of any evidence derived from the privileged conversations would be [im]proper in this case, given that the privilege is a testimonial or evidentiary one, and not constitutionally-based.” <em><span class="citation" data-id="2967273"><a href="/opinion/2967273/united-states-v-squillacote/" aria-description="Citation for case: United States v. Squillacote">Ibid.</a></span> </em>In making this assertion, the court observed that, as of the year 2000, no court had applied the fruit-of-the-poisonous-tree doctrine to derivative evidence obtained as a result of improper access to materials covered by a non-constitutional privilege. <em>Ibid, </em>(quoting <em>United States v. Marashi, </em><span class="citation" data-id="547559"><a href="/opinion/547559/united-states-v-s-mohammad-marashi/" aria-description="Citation for case: United States v. S. Mohammad Marashi">913 F.2d 724</a></span>, 731 n. 11 (9th Cir.1990)); <em>see also Nickel v. Hannigan, </em><span class="citation" data-id="727279"><a href="/opinion/727279/willie-w-nickel-v-robert-d-hannigan-warden-hutchinson-correctional/#409" aria-description="Citation for case: Willie W. Nickel v. Robert D. Hannigan, Warden,...">97 F.3d 403, 409</a></span> (10th Cir.1996) (“[W]e decline to apply the ‘fruit of the poisonous tree’ doctrine to the possible breach of attorney-client privilege in this case.”). We have found no subsequent authority indicating that such derivative evidence is subject to suppression, and we agree that it is unwise to extend the fruit-of-the-poisonous-tree doctrine beyond the context of constitutional violations. <em>See Trammel v. United States, </em><span class="citation" data-id="9427810"><a href="/opinion/110212/trammel-v-united-states/#51" aria-description="Citation for case: Trammel v. United States">445 U.S. 40, 51</a></span>, <span class="citation" data-id="9427810"><a href="/opinion/110212/trammel-v-united-states/" aria-description="Citation for case: Trammel v. United States">100 S.Ct. 906</a></span>, <span class="citation" data-id="9427810"><a href="/opinion/110212/trammel-v-united-states/" aria-description="Citation for case: Trammel v. United States">63 L.Ed.2d 186</a></span> (1980) (indicating that testimonial privileges must be balanced against “the need for probative evidence in the administration of criminal justice”).</p>
<p id="b320-7">In the present case, the privileged materials were not obtained from Warshak as a result of compelled testimony. Instead, they were garnered pursuant to a subpoena, a court order, and a search warrant, much like the psychotherapist-patient conversations at issue in <em><span class="citation" data-id="2967273"><a href="/opinion/2967273/united-states-v-squillacote/" aria-description="Citation for case: United States v. Squillacote">Squillacote</a></span>. </em>Thus, because the documents were not the product of compelled testimony, a full <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>hearing was not required. Moreover, there is no indication that the government made any direct use of the privileged com<page-number citation-index="1" label="295">*295</page-number>munications, either at trial or before the grand jury. Consequently, given the fact that evidence derived from a violation of the attorney-client privilege is not fruit of the poisonous tree, Warshak’s argument withers.</p>
<p id="b321-5">C. Volume &amp; Format of Discovery</p>
<p id="b321-6">The volume of discovery in the present case was prodigious. Indeed, the government turned over millions of pages of discovery, but that discovery appears to have come from relatively few sources. Most of the discovery came from Berkeley itself, when, in March 2005, inspectors executed a search warrant and “imaged” (i.e., copied) the electronic contents of the company’s computers and servers. After the search, the computers and servers remained on Berkeley’s premises, except for several laptops, which were taken offsite and returned two days later. All told, the electronic evidence originating at Berkeley filled three “tera-drives” and numbered 17 million pages. In addition to the electronic evidence, agents seized approximately 506,000 pages of hard-copy documents, all of which the defendants were eventually permitted to copy. On top of the evidence obtained at Berkeley, discovery included 275 discs of material gathered by the grand jury and 13 discs of potential trial exhibits compiled by the government.</p>
<p id="b321-7">The defendants make three arguments with respect to the immense volume of discovery in this case. First, they argue that the district court abused its discretion and violated their right to a fair trial by allowing the government to turn over stupendous quantities of evidence in a disorganized and unsearchable format. Next, they argue that the government was improperly permitted to “abdicate” its <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>obligations by producing gargantuan “haystacks” of discovery that swallowed any “needles” of exculpatory information. Appellant’s Br. at 52. Finally, the defendants argue that the district court erroneously denied a 90-day continuance, which was requested to enable the defendants to continue sifting through the mountains of discovery furnished by the government. Ultimately, none of these arguments is persuasive.<footnotemark>24</footnotemark></p>
<p id="b321-10">1. <em>The Manner in Which the Government Produced Discovery</em></p>
<p id="ArIc">The defendants’ first argument is that the district court erroneously permitted the government to produce titanic amounts of electronic discovery in formats that were simultaneously disorganized and unsearchable. Specifically, the defendants assert that the electronic images of the Berkeley computers and the discs of potential trial exhibits were difficult to search. The defendants further contend that the government’s failure to supplement the discovery materials with indices was prejudicial to the preparation of an adequate defense.<footnotemark>25</footnotemark> In making this argument, the defendants lean heavily on Federal Rule of <em>Civil </em>Procedure 34(b)(2)(E)(i), which requires a party to “produce [discovery materials] as they are kept in the usual course of business or [to] organize and label them to correspond to the categories in the request.” The defendants acknowledge that there is no corresponding provision in Federal Rule of <em>Criminal </em>Proce<page-number citation-index="1" label="296">*296</page-number>dure 16, which governs criminal discovery, but they argue that due process mandates enforcement of the civil rule in the criminal context.</p>
<p id="b322-4">A district court’s decision on a discovery matter is reviewed for abuse of discretion. <em>United States v. Gray, </em><span class="citation" data-id="1302101"><a href="/opinion/1302101/united-states-v-gray/#529" aria-description="Citation for case: United States v. Gray">521 F.3d 514, 529</a></span> (6th Cir.2008) (citing <em>United States v. $174,206.00 in U.S. Currency, </em><span class="citation" data-id="780971"><a href="/opinion/780971/united-states-v-17420600-in-us-currency-thomas-richard-dacia-love/#663" aria-description="Citation for case: United States v. $174,206.00 in U.S. Currency, Thomas...">320 F.3d 658, 663</a></span> (6th Cir.2003)); <em>see United States v. Maples, </em><span class="citation" data-id="9488302"><a href="/opinion/699570/united-states-v-roger-d-maples/#246" aria-description="Citation for case: United States v. Roger D. Maples">60 F.3d 244, 246</a></span> (6th Cir.1995) (“It is well settled that a district court has considerable discretion under Rule 16....”).</p>
<p id="b322-5">As an initial matter, it must be noted that the defendants cite scant authority suggesting that a district court must order the government to produce electronic discovery in a particular fashion.<footnotemark>26</footnotemark> Furthermore, it bears noting that Federal Rule of Criminal Procedure 16, which governs discovery in criminal cases, is entirely silent on the issue of the form that discovery must take; it contains no indication that documents must be organized or indexed. Thus, if we are to find that the district court abused its discretion, we must do so despite a pronounced dearth of precedent suggesting that the district court was wrong.</p>
<p id="b322-6">There are a number of factors that counsel against such a finding. First, the overwhelming majority of the discovery at issue was taken directly from Berkeley’s computers, which means the defendants had ready access to that information. It also means that the defendants had access to the documents “as they [were] kept in the usual course of business.” Fed.R.Civ.P. 34(b)(2)(E)(i). Thus, any difficulty that the defendants had in accessing the copies is arguably immaterial.<footnotemark>27</footnotemark></p>
<p id="b322-9">Furthermore, there is reason to believe that the defendants were experiencing little difficulty in accessing the contents of the electronic discovery. Though the defendants claim that they were provided with data that had been rendered in unsearchable formats, they were citing discovery material to the district court in their motions, leading the district court to observe that the “[defendants’ motion[s] demonstrate^] [that] they [were] capably navigating discovery.” Additionally, at the Kastigar-like hearing held before the district court, an expert witness who testified for the defense indicated that, with the use of certain software, he could perform “very quick and thorough” searches of the electronic discovery. Consequently, it does not appear that the discovery materials were nearly as unsearchable as the defense purports.</p>
<p id="b322-10">Lastly, it should be observed that the government did provide the defense with something of a guide to the electronic discovery. In response to the defense’s discovery request, the government furnished the defendants with “a detailed room-by-room inventory of all items seized from the company, including a listing of the various <page-number citation-index="1" label="297">*297</page-number>computers that were imaged.” Appellee’s Br. at 127. That listing surely offered the defendants some aid in identifying and marshaling the documents relevant to the litigation. Accordingly, we decline to hold that the district court abused its discretion in failing to order the government to produce discovery in a different form.</p>
<p id="b323-5">2. <em>The Abdication of </em>Brady</p>
<p id="b323-6">The defendants next argue that the government shrugged off its obligations under <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>by simply handing over millions of pages of evidence and forcing the defense to find any exculpatory information contained therein. In essence, the defendants contend that the government was obliged to sift fastidiously through the evidence— the vast majority of which came from Berkeley itself — in an attempt to locate anything favorable to the defense. This argument comes up empty.</p>
<p id="b323-7">In <em>United States v. Skilling, </em><span class="citation" data-id="64496"><a href="/opinion/64496/united-states-v-skilling/" aria-description="Citation for case: United States v. Skilling">554 F.3d 529</a></span> (5th Cir.2009), <em>vacated in part on other grounds, </em>— U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./130/2896/">130 S.Ct. 2896</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/177/619/">177 L.Ed.2d 619</a></span> (2010), the Fifth Circuit confronted and rejected a nearly identical argument. There, disgraced Enron CEO Jeffrey K. Skilling advanced the following contentions:</p>
<blockquote id="b323-9">Skilling ... asserts that the government’s use of an open file failed to satisfy its <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>obligation to disclose material evidence. Skilling contends that the government’s open file, which consisted of several hundred million pages of documents, “resulted in the effective concealment of a huge quantity of exculpatory evidence.” As the government never directed Skilling to a single <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>document contained in the open file, Skilling argues that the government suppressed evidence in violation of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>.</em></blockquote>
<p id="b323-12"><em>Id. </em>at 576.</p>
<p id="b323-13">, In dismissing Skilling’s argument, the Fifth Circuit noted that, “[a]s a general rule, the government is under no duty to direct a defendant to exculpatory evidence within a larger mass of disclosed evidence.” <em>Ibid, </em>(citing <em>United States v. Mulderig, </em><span class="citation" data-id="12936"><a href="/opinion/12936/united-states-v-mulderig/#541" aria-description="Citation for case: United States v. Mulderig">120 F.3d 534, 541</a></span> (5th Cir.1997)). However, the <em>Skilling </em>court added a caveat:</p>
<blockquote id="b323-14">We do not hold that the use of a voluminous open file can never violate <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>. </em>For instance, evidence that the government “padded” an open file with pointless or superfluous information to frustrate a defendant’s review of the file might raise serious <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>issues. Creating a voluminous file that is unduly onerous to access might raise similar concerns. And it should go without saying that the government may not hide <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>material of which it is actually aware in a huge open file in the hope that the defendant will never find it. These scenarios would indicate that the government was acting in bad faith in performing its obligations under <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>.</em></blockquote>
<p id="Acl"><em>Id. </em>at 577.</p>
<p id="b323-15">Here, the government did not engage in any conduct indicating that it performed its <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>obligations in bad faith. First, there is no proof that the government larded its production with entirely irrelevant documents.<footnotemark>28</footnotemark> Furthermore, it cannot be said that the government made access to the documents <em>unduly </em>onerous. While ac<page-number citation-index="1" label="298">*298</page-number>cess to the documents may have been somewhat hampered due to the format in which they were transferred, the district court noted that the defendants’ motion practice “demonstrate[d] they [were] capably navigating the discovery, which primarily all came from [the] [defendants in the first place.”<footnotemark>29</footnotemark> Finally, there is no indication that the government deliberately concealed any exculpatory evidence in the information it turned over to the defense.<footnotemark>30</footnotemark> Consequently, the government has not “abdicated” its duties under <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>.</em></p>
<p id="b324-4">3. <em>The Denial of a Continuance</em></p>
<p id="ACG">On December 28, 2007, the defendants requested a 90-day continuance, which would have pushed the commencement of the trial from January 8, 2008 to April 8, 2008. In making the request, the defendants contended that they had been afforded insufficient opportunity to review the evidence, stating: “[i]t is as if the government has pointed the defendants to the Earth’s oceans, saying ‘there is your discovery.’ ” The district court declined to grant the request, noting that “[c]ounsel for [the] [defendants outnumber counsel for the government, and have all been working on this case for a substantial amount of time.”<footnotemark>31</footnotemark> The defendants now argue that the district court’s denial of their request for a continuance was error.</p>
<p id="b324-7">The district court’s denial of a motion for a continuance is reviewed for abuse of discretion. <em>United States v. Crossley, </em><span class="citation" data-id="770181"><a href="/opinion/770181/united-states-v-rebecca-k-crossley-99-4076-starla-grubich/#854" aria-description="Citation for case: United States v. Rebecca K. Crossley (99-4076) Starla...">224 F.3d 847, 854</a></span> (6th Cir.2000). “Denial amounts to a constitutional violation only if there is an unreasoning and arbitrary ‘insistence upon expeditiousness in the face of a justifiable request for delay.’ To demonstrate reversible error, the defendant must show that the denial resulted in actual prejudice to his defense.” <em>United States v. Gallo, </em><span class="citation" data-id="453322"><a href="/opinion/453322/united-states-v-joseph-c-gallo-frederick-graewe-hartmut-graewe-kevin/#1523" aria-description="Citation for case: United States v. Joseph C. Gallo Frederick Graewe Hartmut...">763 F.2d 1504, 1523</a></span> (6th Cir.1985) (quoting <em>United States v. Mitchell, </em><span class="citation" data-id="442038"><a href="/opinion/442038/united-states-v-walter-l-mitchell-jr/#704" aria-description="Citation for case: United States v. Walter L. Mitchell, Jr.">744 F.2d 701, 704</a></span> (9th Cir.1984)). “The defendant demonstrates ‘actual prejudice’ by showing that a continuance would have made relevant witnesses available or added something to the defense.” <em>United States v. King, </em><span class="citation" data-id="9490697"><a href="/opinion/747179/united-states-of-america-plaintiff-appellee-v-kenneth-king-kewin-king/#487" aria-description="Citation for case: United States of America, Plaintiff-Appellee v. Kenneth...">127 F.3d 483, 487</a></span> (6th Cir.1997); <em>see also United States v. Faulkner, </em><span class="citation" data-id="337637"><a href="/opinion/337637/united-states-v-donald-d-faulkner-united-states-of-america-v-william-e/#729" aria-description="Citation for case: United States v. Donald D. Faulkner, United States of...">538 F.2d 724, 729</a></span> (6th Cir.1976) (“No absolute rule can be articulated as to the minimum amount of time required for an adequate preparation for trial of a criminal case.”).</p>
<p id="b324-8">The defendants argue that they were prejudiced in two ways. First, they argue that “their counsel could not satisfy their constitutional obligation to review all the evidence in the government’s possession, custody, or control.”<footnotemark>32</footnotemark> Appellant’s Br. at 60. In making this argument, they allege that “the entirety of the government’s <page-number citation-index="1" label="299">*299</page-number>360,000 pages of trial exhibits ... were largely disclosed on November 29, 2007, only six weeks before trial.” <em>Id. </em>at 59. Second, the defendants argue that “[t]he defense simply did not have sufficient time to locate and then utilize material and exculpatory evidence that was hidden within the millions of pages of discovery.” <em>Id. </em>at 60.</p>
<p id="b325-5">These arguments lead nowhere. With respect to the first, it must be noted that more than a year elapsed between the time the indictment was handed down and the time the trial began, affording the defendants ample opportunity to construct a defense.<footnotemark>33</footnotemark> Additionally, the discovery time line does not indicate that the defendants were shortchanged with respect to preparation time. The bulk of the documents in question were in the company’s possession as early as April 2005.<footnotemark>34</footnotemark> Furthermore, the entirety of the discovery material in the case was in the defendants’ hands by June 2007, more than six months in advance of the trial. While the government did not provide the defense with thirteen discs of potential trial exhibits until November 29, 2007 — approximately six weeks before trial was to begin — those exhibits were ostensibly culled from the discovery material that the government had already provided.<footnotemark>35</footnotemark> It is true that this case involved millions of pages of documents, but there is no dispute that the defendants were given months to comb through the bulk of them. As a result, it cannot be said that the district court’s unwillingness to postpone the trial was the product of an undue insistence on haste.</p>
<p id="b325-10">The defendants’ second argument — that they were not given enough time to mine exculpatory evidence from the mountains of discovery dumped at their feet — similarly fails. As an initial matter, it should be noted that this argument assumes that exculpatory evidence exists. In the absence of such evidence, the lack of time to look for it would be harmless. In other words, it would not be prejudicial if the defendants were denied the chance to excavate in a mine that contained no ore. On that score, the most the defendants can say is tha

[...TRUNCATED 194596 of 314596 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/United States v. Watson.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Watson"
type: case
citation: "423 U.S. 411 (1976)"
parallel_cite: "96 S. Ct. 820; 46 L. Ed. 2d 598"
neutral_cite: 1976 U.S. LEXIS 121
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-01-26
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-01-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Watson
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109352/united-states-v-watson/"
  cluster_id: 109352
  opinion_id: 109352
  identity_checked: true
homes:
  - page: "[[Arrest and Arrest Warrants]]"
    role: "Key — Anchor (warrantless public arrest on probable cause)"
  - page: "[[Consent Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Schneckloth v. Bustamonte]]", "[[United States v. Drayton]]", "[[United States v. Mendenhall]]", "[[United States v. Santana]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent-search", "voluntariness", "custody", "warrantless-arrest"]
holding: "Custody alone does not render consent involuntary. The fact of being under arrest / in custody is ONE factor in the…"
lake:
  record_id: United States v. Watson
  status: verified
  projected_at: 2026-07-10
---

# United States v. Watson

*423 U.S. 411 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Acting on a reliable informant's tip — corroborated when the informant showed the inspector stolen credit cards Watson had supplied — a postal inspector arrested Watson without a warrant in a restaurant. After the arrest and *[[Miranda v. Arizona|Miranda]]* warnings, the inspector asked to search Watson's nearby car; Watson said "Go ahead," and stolen credit cards were found inside. Watson moved to suppress. The Ninth Circuit held the warrantless arrest invalid and the consent therefore tainted.

## Issue
Whether Watson's consent to search, given after a custodial arrest, was voluntary — and whether the fact of being in custody renders consent involuntary.

## Rule
First, the warrantless arrest was lawful — a warrantless felony arrest in public on probable cause does not violate the Fourth Amendment — so the consent was not the product of an illegal arrest. Second, consent given in custody is judged by the *[[Schneckloth v. Bustamonte|Schneckloth]]* [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], and custody alone does not make it involuntary: "He had been arrested and was in custody, but his consent was given while on a public street, not in the confines of the police station. Moreover, the fact of custody alone has never been enough in itself to demonstrate a coerced confession or consent to search." — 423 U.S. at 424. ^pin-424

Nor is the suspect's ignorance of the right to refuse controlling — the absence of such proof "may be a factor in the overall judgment," but "is not to be given controlling significance." — [*Id.*](https://www.courtlistener.com/opinion/109352/united-states-v-watson/#:~:text=may%20be%20a%20factor%20in) ^pin-424a

## Application
Because Watson's arrest was valid, his consent was not tainted by any illegality. There was no overt act or threat of force, no promises, and no subtle coercion; Watson consented on a public street rather than at the station house. That he was under arrest, and any lack of proof that he knew he could refuse, did not by themselves overbear his will. Under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] his consent was his own free choice, and the stolen credit cards found in the car were admissible.

## Conclusion
The warrantless public arrest was lawful and Watson's consent to the search was voluntary; the Supreme Court reversed the Court of Appeals.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Watson* applies the [[Schneckloth v. Bustamonte]] totality-of-the-circumstances voluntariness test to a custodial setting: being under arrest is one factor, not a disqualifier, and the suspect need not be told he may refuse. *Watson*'s separate holding — that a warrantless felony arrest in public on probable cause is reasonable — also remains good law and informs [[United States v. Santana]].

## Appears on
- [[Arrest and Arrest Warrants]] — *Key — Anchor*
- [[Consent Searches]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Watson*, 423 U.S. 411 (1976) — https://www.courtlistener.com/opinion/109352/united-states-v-watson/ — pinpoint: 424 (parallel 96 S. Ct. 820).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "39a71084251bcf5a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Watson"}, "payload": {"all": [{"cite": "423 U.S. 411", "page": "411", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "423"}, {"cite": "96 S. Ct. 820", "page": "820", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "96"}, {"cite": "46 L. Ed. 2d 598", "page": "598", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "46"}, {"cite": "1976 U.S. LEXIS 121", "page": "121", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1976"}], "display": "423 U.S. 411", "official": {"cite": "423 U.S. 411", "page": "411", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "423"}, "official_selection_present": true, "record_id": "United States v. Watson"}}
{"assertion_id": "247761c91e0b5a81", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-424", "record_id": "United States v. Watson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-424", "pinpoint_status": "slip-only", "quote": "and stolen credit cards were found inside. Watson moved to suppress. The Ninth Circuit held the warrantless arrest invalid and the consent therefore tainted. ## Issue Whether Watson's consent to search, given after a custodial arrest, was voluntary — and whether the fact of being in custody renders consent involuntary. ## Rule First, the warrantless arrest was lawful — a warrantless felony arrest in public on probable cause does not violate the Fourth Amendment — so the consent was not the product of an illegal arrest. Second, consent given in custody is judged by the *Schneckloth* totality of the circumstances, and custody alone does not make it involuntary:", "quote_fidelity": "mismatch", "record_id": "United States v. Watson", "star_marker": null}}
{"assertion_id": "c00db297c5db9ec8", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-424a", "record_id": "United States v. Watson"}, "payload": {"fragment": "#:~:text=may%20be%20a%20factor%20in", "page": null, "pin_id": "pin-424a", "pinpoint_status": "star-verified", "quote": "may be a factor in the overall judgment,", "quote_fidelity": "matched", "record_id": "United States v. Watson", "star_marker": "424"}}
{"assertion_id": "b1504a4c9757045d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Watson"}, "payload": {"as_of_content": "1976-01-26", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Watson", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Watson

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Watson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Watson",
    "case_name_short": "Watson",
    "case_name_full": "United States v. Watson",
    "input_case_name": "United States v. Watson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-01-26",
    "year": 1976,
    "docket": null,
    "cluster_id": 109352,
    "lead_opinion_id": 109352,
    "sibling_ids": [
      109352,
      9426247,
      9426248,
      9426249,
      9426250
    ],
    "absolute_url": "/opinion/109352/united-states-v-watson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "423 U.S. 411",
      "volume": "423",
      "reporter": "U.S.",
      "page": "411",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 820",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "820",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "46 L. Ed. 2d 598",
        "volume": "46",
        "reporter": "L. Ed. 2d",
        "page": "598",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 121",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "121",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "423 U.S. 411",
        "volume": "423",
        "reporter": "U.S.",
        "page": "411",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 820",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "820",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "46 L. Ed. 2d 598",
        "volume": "46",
        "reporter": "L. Ed. 2d",
        "page": "598",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 121",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "121",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "423 U.S. 411",
    "official_selection": {
      "court_class": "scotus",
      "selected": "423 U.S. 411",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-424",
      "page": null,
      "quote": "and stolen credit cards were found inside. Watson moved to suppress. The Ninth Circuit held the warrantless arrest invalid and the consent therefore tainted. ## Issue Whether Watson's consent to search, given after a custodial arrest, was voluntary \u2014 and whether the fact of being in custody renders consent involuntary. ## Rule First, the warrantless arrest was lawful \u2014 a warrantless felony arrest in public on probable cause does not violate the Fourth Amendment \u2014 so the consent was not the product of an illegal arrest. Second, consent given in custody is judged by the *Schneckloth* totality of the circumstances, and custody alone does not make it involuntary:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-424a",
      "page": null,
      "quote": "may be a factor in the overall judgment,",
      "star_marker": "424",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 23606,
      "fragment": "#:~:text=may%20be%20a%20factor%20in",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-01-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Watson",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "United States v. Watson:lane1_negative"
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
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bartlett v. State",
          "cluster_id": 1449101,
          "cite": [
            "249 S.W.3d 658",
            "2008 WL 480174"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bickel, 2006-Coa-034 (7-10-2007)",
          "cluster_id": 3949285,
          "cite": [
            "2007 Ohio 3517"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Winston",
          "cluster_id": 202176,
          "cite": [
            "444 F.3d 115",
            "2006 U.S. App. LEXIS 10038",
            "2006 WL 1044180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Keith Forbes",
          "cluster_id": 764880,
          "cite": [
            "181 F.3d 1",
            "1999 WL 315796"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Sandoval v. State",
          "cluster_id": 1575995,
          "cite": [
            "35 S.W.3d 763",
            "2000 WL 1863674"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Atwater v. City of Lago Vista",
          "cluster_id": 7076046,
          "cite": [
            "165 F.3d 380",
            "1999 U.S. App. LEXIS 1639",
            "1999 WL 13050"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. La Fontaine",
          "cluster_id": 6144105,
          "cite": [
            "235 A.D.2d 93",
            "664 N.Y.S.2d 587",
            "1997 N.Y. App. Div. LEXIS 11046"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Glia",
          "cluster_id": 6134935,
          "cite": [
            "226 A.D.2d 66",
            "651 N.Y.S.2d 967",
            "1996 N.Y. App. Div. LEXIS 12576"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Mourning",
          "cluster_id": 8913620,
          "cite": [
            "716 F. Supp. 279",
            "1989 U.S. Dist. LEXIS 7281",
            "1989 WL 71233"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Leal v. State",
          "cluster_id": 5244283,
          "cite": [
            "736 S.W.2d 903"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
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
        "journal_ref": "United States v. Watson:lane2_top_cited"
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
        "journal_ref": "United States v. Watson:lane2_top_cited"
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
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Phillips",
          "cluster_id": 8924874,
          "cite": [
            "664 F.2d 971",
            "9 Fed. R. Serv. 970"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ramey",
          "cluster_id": 1185860,
          "cite": [
            "545 P.2d 1333",
            "16 Cal. 3d 263",
            "127 Cal. Rptr. 629",
            "1976 Cal. LEXIS 220"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gonzalez",
          "cluster_id": 5681980,
          "cite": [
            "39 N.Y.2d 122",
            "347 N.E.2d 575",
            "383 N.Y.S.2d 215",
            "1976 N.Y. LEXIS 2389"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patrick Bell, Sr., Etc. v. City of Milwaukee, Howard Johnson and Edwin Shaffer, Patrick Bell, Sr., Etc. v. Thomas Grady, Jr., Patrick Bell, Sr., Etc. v. City of Milwaukee",
          "cluster_id": 443256,
          "cite": [
            "746 F.2d 1205",
            "16 Fed. R. Serv. 279",
            "1984 U.S. App. LEXIS 18950"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. James",
          "cluster_id": 1433510,
          "cite": [
            "561 P.2d 1135",
            "19 Cal. 3d 99",
            "137 Cal. Rptr. 447"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ervine",
          "cluster_id": 2527109,
          "cite": [
            "47 Cal. 4th 745",
            "220 P.3d 820",
            "102 Cal. Rptr. 3d 786",
            "2009 Cal. LEXIS 12406"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Meekins v. State",
          "cluster_id": 2544137,
          "cite": [
            "340 S.W.3d 454",
            "2011 Tex. Crim. App. LEXIS 592",
            "2011 WL 1663151"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hulit v. State",
          "cluster_id": 2452885,
          "cite": [
            "982 S.W.2d 431",
            "1998 Tex. Crim. App. LEXIS 174",
            "1998 WL 870923"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jackie David Miller",
          "cluster_id": 362441,
          "cite": [
            "589 F.2d 1117",
            "3 Fed. R. Serv. 1418",
            "1978 U.S. App. LEXIS 7704"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Saundra Prescott",
          "cluster_id": 358848,
          "cite": [
            "581 F.2d 1343",
            "1978 U.S. App. LEXIS 9041"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Monterroso",
          "cluster_id": 2507854,
          "cite": [
            "101 P.3d 956",
            "22 Cal. Rptr. 3d 1",
            "34 Cal. 4th 743",
            "2004 Daily Journal DAR 14707",
            "2004 Cal. Daily Op. Serv. 10899",
            "2004 Cal. LEXIS 11763"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Orlando Vasquez, Carlos Sanchez, Fernando Eugenio Medina, Amparo Valencia Medina, Clara Inez Mesa and Hernando Mesa",
          "cluster_id": 386016,
          "cite": [
            "638 F.2d 507",
            "1980 U.S. App. LEXIS 11022"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Walker",
          "cluster_id": 2005731,
          "cite": [
            "350 N.E.2d 678",
            "370 Mass. 548",
            "1976 Mass. LEXIS 1011"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Juarez v. State",
          "cluster_id": 1562920,
          "cite": [
            "758 S.W.2d 772",
            "1988 Tex. Crim. App. LEXIS 172",
            "1988 WL 98938"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nancy Reed and Morris Goldsmith, A/K/A \"Marlowe,\"",
          "cluster_id": 354014,
          "cite": [
            "572 F.2d 412",
            "3 Fed. R. Serv. 155",
            "1978 U.S. App. LEXIS 11727"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arcila v. State",
          "cluster_id": 1495036,
          "cite": [
            "834 S.W.2d 357",
            "1992 Tex. Crim. App. LEXIS 160",
            "1992 WL 139308"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bacigalupo",
          "cluster_id": 1386250,
          "cite": [
            "820 P.2d 559",
            "1 Cal. 4th 103",
            "2 Cal. Rptr. 2d 335",
            "91 Daily Journal DAR 15109",
            "1991 Cal. LEXIS 5500"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Reginald Glover",
          "cluster_id": 578612,
          "cite": [
            "957 F.2d 1004",
            "1992 U.S. App. LEXIS 2799",
            "1992 WL 29046"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Deunte L. Humphries",
          "cluster_id": 786633,
          "cite": [
            "372 F.3d 653",
            "2004 U.S. App. LEXIS 11898",
            "2004 WL 1351562"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dyar v. State",
          "cluster_id": 1384792,
          "cite": [
            "125 S.W.3d 460",
            "2003 Tex. Crim. App. LEXIS 74",
            "2003 WL 1917729"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Richard Wiener",
          "cluster_id": 334863,
          "cite": [
            "534 F.2d 15",
            "1976 U.S. App. LEXIS 12212"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Avalos",
          "cluster_id": 2269454,
          "cite": [
            "47 Cal. App. 4th 1569",
            "55 Cal. Rptr. 2d 450",
            "96 Cal. Daily Op. Serv. 5718",
            "96 Daily Journal DAR 9266",
            "1996 Cal. App. LEXIS 740"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109352 OR 9426247 OR 9426248 OR 9426249 OR 9426250) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NTcxMDcyMDAwMDAmcz0xNjIxMTI5JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109352+OR+9426247+OR+9426248+OR+9426249+OR+9426250%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 12,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 12,
        "triage_snippet_classified": 188
      },
      "lane2_top_cited": {
        "query": "cites:(109352 OR 9426247 OR 9426248 OR 9426249 OR 9426250)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDYmcz0zODkyNTAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109352+OR+9426247+OR+9426248+OR+9426249+OR+9426250%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109352 OR 9426247 OR 9426248 OR 9426249 OR 9426250)",
        "reviewed": 30,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 30,
        "triage_read": 0,
        "triage_snippet_classified": 30
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109352 OR 9426247 OR 9426248 OR 9426249 OR 9426250)",
    "indexed_citing_opinions": 508,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109352,
        "count": 191,
        "count_source": "search"
      },
      {
        "opinion_id": 9426247,
        "count": 329,
        "count_source": "search"
      },
      {
        "opinion_id": 9426248,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426249,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426250,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2263,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-watson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwMDg3NyZzPTEwMTI3OTAzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109352+OR+9426247+OR+9426248+OR+9426249+OR+9426250%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109352,
        "cited_id": 84759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 84827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 91385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 91470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 95265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 101970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 106850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 226125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 227607,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 227881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 241496,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 260271,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 262538,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 267195,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 267556,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 269642,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 271327,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 273438,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 275790,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 277223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 278957,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 286516,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 291586,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 293653,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 299839,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 305071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 305803,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 305873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 306113,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 322384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 1606693,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 1939307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 1978640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 2114928,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 2292926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 2304502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 2614205,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 3238539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 5513252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 5554010,
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
    "date_created": "2026-07-06T03:32:02Z",
    "date_modified": "2026-07-10T00:12:42Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:32:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:32:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:39:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:32:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Watson (truncated)

```
<div>
<center><b><span class="citation no-link">423 U.S. 411</span> (1976)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
WATSON.</h1></center>
<center>No. 74-538.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 8, 1975.</center>
<center>Decided January 26, 1976.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><span class="star-pagination">*412</span> <i>Deputy Solicitor General Frey</i> argued the cause for the United States. With him on the briefs were <i>Solicitor General Bork, Acting Assistant Attorney General Keeney,</i> and <i>Peter M. Shannon, Jr.</i></p>
<p><i>Michael D. Nasatir,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./421/997/">421 U. S. 997</a></span>. argued the cause for respondent. With him on the brief was <i>Donald M. Re.</i></p>
<p>MR. JUSTICE WHITE delivered the opinion of the Court.</p>
<p>This case presents questions under the Fourth Amendment as to the legality of a warrantless arrest and of an ensuing search of the arrestee's automobile carried out with his purported consent.</p>
<p></p>
<h2>I</h2>
<p>The relevant events began on August 17, 1972, when an informant, one Khoury, telephoned a postal inspector informing him that respondent Watson was in possession of a stolen credit card and had asked Khoury to cooperate in using the card to their mutual advantage. On five to 10 previous occasions Khoury had provided the inspector with reliable information on postal inspection matters, some involving Watson. Later that day <span class="star-pagination">*413</span> Khoury delivered the card to the inspector. On learning that Watson had agreed to furnish additional cards, the inspector asked Khoury to arrange to meet with Watson. Khoury did so, a meeting being scheduled for August 22.<sup>[1]</sup> Watson canceled that engagement, but at noon on August 23, Khoury met with Watson at a restaurant designated by the latter. Khoury had been instructed that if Watson had additional stolen credit cards, Khoury was to give a designated signal. The signal was given, the officers closed in, and Watson was forthwith arrested. He was removed from the restaurant to the street where he was given the warnings required by <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). A search having revealed that Watson had no credit cards on his person, the inspector asked if he could look inside Watson's car, which was standing within view. Watson said, "Go ahead," and repeated these words when the inspector cautioned that "[i]f I find anything, it is going to go against you." Using keys furnished by Watson, the inspector entered the car and found under the floor mat an envelope containing two credit cards in the names of other persons. These cards were the basis for two counts of a four-count indictment charging Watson with possessing stolen mail in violation of <span class="citation no-link">18 U. S. C. § 1708</span>.<sup>[2]</sup></p>
<p>Prior to trial, Watson moved to suppress the cards, claiming that his arrest was illegal for want of probable cause and an arrest warrant and that his consent to search the car was involuntary and ineffective because he had not been told that he could withhold consent. <span class="star-pagination">*414</span> The motion was denied, and Watson was convicted of illegally possessing the two cards seized from his car.<sup>[3]</sup></p>
<p>A divided panel of the Court of Appeals for the Ninth Circuit reversed, <span class="citation" data-id="9461128"><a href="/opinion/322384/united-states-v-henry-ogle-watson/" aria-description="Citation for case: United States v. Henry Ogle Watson">504 F. 2d 849</a></span> (1974), ruling that the admission in evidence of the two credit cards found in the car was prohibited by the Fourth Amendment. In reaching this judgment, the court decided two issues in Watson's favor. First, notwithstanding its agreement with the District Court that Khoury was reliable and that there was probable cause for arresting Watson, the court held the arrest unconstitutional because the postal inspector had failed to secure an arrest warrant although he concededly had time to do so. Second, based on the totality of the circumstances, one of which was the illegality of the arrest, the court held Watson's consent to search had been coerced and hence was not a valid ground for the warrantless search of the automobile. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./420/924/">420 U. S. 924</a></span> (1975).</p>
<p></p>
<h2>II</h2>
<p>A major part of the Court of Appeals' opinion was its holding that Watson's warrantless arrest violated the Fourth Amendment. Although it did not expressly do so, it may have intended to overturn the conviction on the independent ground that the two credit cards were the inadmissible fruits of an unconstitutional arrest. Cf. <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975). However that may be, the Court of Appeals treated the illegality of Watson's arrest as an important factor in determining the voluntariness of his consent to search his car. We therefore deal first with the arrest issue.</p>
<p>Contrary to the Court of Appeals' view, Watson's arrest was not invalid because executed without a warrant. <span class="star-pagination">*415</span> Title <span class="citation no-link">18 U. S. C. § 3061</span> (a) (3) expressly empowers the Board of Governors of the Postal Service to authorize Postal Service officers and employees "performing duties related to the inspection of postal matters" to</p>
<blockquote>"make arrests without warrant for felonies cognizable under the laws of the United States if they have reasonable grounds to believe that the person to be arrested has committed or is committing such a felony."</blockquote>
<p>By regulation, <span class="citation no-link">39 CFR § 232.5</span> (a) (3) (1975), and in identical language, the Board of Governors has exercised that power and authorized warrantless arrests. Because there was probable cause in this case to believe that Watson had violated § 1708, the inspector and his subordinates, in arresting Watson, were acting strictly in accordance with the governing statute and regulations. The effect of the judgment of the Court of Appeals was to invalidate the statute as applied in this case and as applied to all the situations where a court fails to find exigent circumstances justifying a warrantless arrest. We reverse that judgment.</p>
<p>Under the Fourth Amendment, the people are to be "secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, . . . and no Warrants shall issue, but upon probable cause . . . ." Section 3061 represents a judgment by Congress that it is not unreasonable under the Fourth Amendment for postal inspectors to arrest without a warrant provided they have probable cause to do so.<sup>[4]</sup> This was not an <span class="star-pagination">*416</span> isolated or quixotic judgment of the legislative branch. Other federal law enforcement officers have been expressly authorized by statute for many years to make felony arrests on probable cause but without a warrant. This is true of United States marshals, <span class="citation no-link">18 U. S. C. § 3053</span>, and of agents of the Federal Bureau of Investigation, <span class="citation no-link">18 U. S. C. § 3052</span>; the Drug Enforcement Administration, <span class="citation no-link">84 Stat. 1273</span>, <span class="citation no-link">21 U. S. C. § 878</span>; the Secret Service, <span class="citation no-link">18 U. S. C. § 3056</span> (a); and the Customs Service, <span class="citation no-link">26 U. S. C. § 7607</span>.<sup>[5]</sup></p>
<p>Because there is a "strong presumption of constitutionality due to an Act of Congress, especially when it turns on what is `reasonable,' " "[o]bviously the Court should be reluctant to decide that a search thus authorized by Congress was unreasonable and that the Act was therefore unconstitutional." <i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#585" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 585</a></span> (1948). Moreover, there is nothing in the Court's prior cases indicating that under the <span class="star-pagination">*417</span> Fourth Amendment a warrant is required to make a valid arrest for a felony. Indeed, the relevant prior decisions are uniformly to the contrary.</p>
<p>"The usual rule is that a police officer may arrest without warrant one believed by the officer upon reasonable cause to have been guilty of a felony . . . ." <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 156</a></span> (1925). In <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span> (1959), the Court dealt with an FBI agent's warrantless arrest under <span class="citation no-link">18 U. S. C. § 3052</span>, which authorizes a warrantless arrest where there are reasonable grounds to believe that the person to be arrested has committed a felony. The Court declared that "[t]he statute states the constitutional standard. . . ." <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#100" aria-description="Citation for case: Henry v. United States">361 U. S., at 100</a></span>. The necessary inquiry, therefore, was not whether there was a warrant or whether there was time to get one, but whether there was probable cause for the arrest. In <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#232" aria-description="Citation for case: Abel v. United States">362 U. S. 217, 232</a></span> (1960), the Court sustained an administrative arrest made without "a judicial warrant within the scope of the Fourth Amendment." The crucial question in <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959), was whether there was probable cause for the warrantless arrest. If there was, the Court said, "the arrest, though without a warrant, was lawful . . . ." <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#310" aria-description="Citation for case: Draper v. United States"><i>Id.,</i> at 310</a></span>. <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#34" aria-description="Citation for case: Ker v. California">374 U. S. 23, 34-35</a></span> (1963) (opinion of Clark, J.), reiterated the rule that "[t]he lawfulness of the arrest without warrant, in turn, must be based upon probable cause . . ." and went on to sustain the warrantless arrest over other claims going to the mode of entry. Just last Term, while recognizing that maximum protection of individual rights could be assured by requiring a magistrate's review of the factual justification prior to any arrest, we stated that "such a requirement would constitute an intolerable handicap for legitimate law enforcement" and noted that the Court "has never invalidated an arrest supported by probable cause solely <span class="star-pagination">*418</span> because the officers failed to secure a warrant." <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#113" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 113</a></span> (1975).<sup>[6]</sup></p>
<p>The cases construing the Fourth Amendment thus reflect the ancient common-law rule that a peace officer was permitted to arrest without a warrant for a misdemeanor or felony committed in his presence as well as for a felony not committed in his presence if there was reasonable ground for making the arrest. 10 Halsbury's Laws of England 344-345 (3d ed. 1955); 4 W. Blackstone, Commentaries *292; 1 J. Stephen, A History of the Criminal Law of England 193 (1883); 2 M. Hale, Pleas of the Crown *72-74; Wilgus, Arrest Without a Warrant <span class="citation no-link">22 Mich. L. Rev. 541</span>, 547-550, 686-688 (1924); <span class="star-pagination">*419</span> <i>Samuel</i> v. <i>Payne,</i> <span class="citation" data-id="6629715"><a href="/opinion/6747612/green-v-graves/" aria-description="Citation for case: Green v. Graves">1 Doug. 359</a></span>, 99 Eng. Rep. 230 (K. B. 1780); <i>Beckwith</i> v. <i>Philby,</i> 6 Barn. &amp; Cress. 635, 108 Eng. Rep. 585 (K. B. 1827). This has also been the prevailing rule under state constitutions and statutes. "The rule of the common law, that a peace officer or a private citizen may arrest a felon without a warrant, has been generally held by the courts of the several States to be in force in cases of felony punishable by the civil tribunals." <i>Kurtz</i> v. <i>Moffitt,</i> <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/#504" aria-description="Citation for case: Kurtz v. Moffitt">115 U. S. 487, 504</a></span> (1885).</p>
<p>In <i>Rohan</i> v. <i>Sawin,</i> <span class="citation no-link">59 Mass. 281</span> (1850), a false-arrest case, the Supreme Judicial Court of Massachusetts held that the common-law rule obtained in that State. Given probable cause to arrest, "[t]he authority of a constable, to arrest without warrant, in cases of felony, is most fully established by the elementary books, and adjudicated cases." <i>Id.,</i> at 284. In reaching this judgment the court observed:</p>
<blockquote>"It has been sometimes contended, that an arrest of this character, without a warrant, was a violation of the great fundamental principles of our national and state constitutions, forbidding unreasonable searches and arrests, except by warrant founded upon a complaint made under oath. Those provisions doubtless had another and different purpose, being in restraint of general warrants to make searches, and requiring warrants to issue only upon a complaint made under oath. They do not conflict with the authority of constables or other peace-officers, or private persons under proper limitations, to arrest without warrant those who have committed felonies. The public safety, and the due apprehension of criminals, charged with heinous offences, imperiously require that such arrests should be made without warrant by officers of the law." <i>Id.,</i> at 284-285.</blockquote>
<p><span class="star-pagination">*420</span> Also rejected, <i>id.,</i> at 285-286, was the trial court's view that to justify a warrantless arrest, the State must show "an immediate necessity therefor, arising from the danger, that the plaintiff would otherwise escape, or secrete the stolen property, before a warrant could be procured against him." The Supreme Judicial Court ruled that there was no "authority for thus restricting a constable in the exercise of his authority to arrest for a felony without a warrant." <i>Id.,</i> at 286. Other early cases to similar effect were <i>Wakely</i> v. <i>Hart,</i> <span class="citation" data-id="6313783"><a href="/opinion/6441697/wakely-v-hart/" aria-description="Citation for case: Wakely v. Hart">6 Binn. 316</a></span> (Pa. 1814); <i>Tolley</i> v. <i>Mix,</i> <span class="citation" data-id="5513252"><a href="/opinion/5666272/holley-v-mix/" aria-description="Citation for case: Holley v. Mix">3 Wend. 350</a></span> (N. Y. Sup. Ct. 1829); <i>State</i> v. <i>Brown,</i> <span class="citation multiple-matches"><a href="/c/Del./5/505/">5 Del. 505</a></span> (Ct. Gen. Sess. 1853); <i>Johnson</i> v. <i>State,</i> <span class="citation" data-id="5554010"><a href="/opinion/5704309/johnson-v-state/" aria-description="Citation for case: Johnson v. State">30 Ga. 426</a></span> (1860); <i>Wade</i> v. <i>Chaffee,</i> 8 R. I. 224 (1865). See <i>Reuck</i> v. <i>McGregor,</i> 32 N. J. L. 70, 74 (Sup. Ct. 1866); <i>Baltimore &amp; O. R. Co.</i> v. <i>Cain,</i> <span class="citation" data-id="7899354"><a href="/opinion/7948364/baltimore-ohio-railroad-v-cain/#100" aria-description="Citation for case: Baltimore &amp; Ohio Railroad v. Cain">81 Md. 87, 100, 102</a></span>, <span class="citation" data-id="7899354"><a href="/opinion/7948364/baltimore-ohio-railroad-v-cain/#803" aria-description="Citation for case: Baltimore &amp; Ohio Railroad v. Cain">31 A. 801, 803, 804</a></span> (1895).<sup>[7]</sup></p>
<p>Because the common-law rule authorizing arrests without a warrant generally prevailed in the States, it is important for present purposes to note that in 1792 Congress invested United States marshals and their deputies with "the same powers in executing the laws of the United States, as sheriffs and their deputies in the several states have by law, in executing the laws of their respective states." Act of May 2, 1792, c. 28, § 9, <span class="citation no-link">1 Stat. 265</span>. The Second Congress thus saw no inconsistency between the Fourth Amendment and legislation giving United States marshals the same power as local peace officers to arrest for a felony without a warrant.<sup>[8]</sup> This provision equating the power of federal marshals <span class="star-pagination">*421</span> with those of local sheriffs was several times reenacted<sup>[9]</sup> and is today § 570 of Title 28 of the United States Code. That provision, however, was supplemented in 1935 by § 504a of the Judicial Code,<sup>[10]</sup> which in its essential elements is now <span class="citation no-link">18 U. S. C. § 3053</span> and which expressly empowered marshals to make felony arrests without warrant and on probable cause. It was enacted to furnish a federal standard independent of the vagaries of state laws, the Committee Report remarking that under existing law a "marshal or deputy marshal may make an arrest without a warrant within his district in all cases where the sheriff might do so under the State statutes." H. R. Rep. No. 283, 74th Cong., 1st Sess., 1 (1935). See <i>United States</i> v. <i>Riggs,</i> <span class="citation" data-id="308790"><a href="/opinion/308790/united-states-v-fairh-riggs/#702" aria-description="Citation for case: United States v. Fairh Riggs">474 F. 2d 699, 702-703, n. 2</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/820/">414 U. S. 820</a></span> (1973).</p>
<p>The balance struck by the common law in generally authorizing felony arrests on probable cause, but without a warrant, has survived substantially intact. It appears <span class="star-pagination">*422</span> in almost all of the States in the form of express statutory authorization. In 1963, the American Law Institute undertook the task of formulating a model statute governing police powers and practice in criminal law enforcement and related aspects of pretrial procedure. In 1975, after years of discussion, A Model Code of Pre-arraignment Procedure was proposed. Among its provisions was § 120.1 which authorizes an officer to take a person into custody if the officer has reasonable cause to believe that the person to be arrested has committed a felony, or has committed a misdemeanor or petty misdemeanor in his presence.<sup>[11]</sup> The commentary to this section said: "The Code thus adopts the traditional and almost universal standard for arrest without a warrant."<sup>[12]</sup></p>
<p><span class="star-pagination">*423</span> This is the rule Congress has long directed its principal law enforcement officers to follow. Congress has plainly decided against conditioning warrantless arrest power on proof of exigent circumstances.<sup>[13]</sup> Law enforcement officers may find it wise to seek arrest warrants where practicable to do so, and their judgments about probable cause may be more readily accepted where backed by a warrant issued by a magistrate. See <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#106" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 106</a></span> (1965); <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#111" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108, 111</a></span> (1964); <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#479" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 479-480</a></span> (1963). But we decline to transform this judicial preference into a constitutional rule when the judgment of the Nation and Congress has for so long been to authorize warrantless public arrests on probable cause rather than to encumber criminal prosecutions with endless litigation with respect to the existence of exigent circumstances, whether it was practicable <span class="star-pagination">*424</span> to get a warrant, whether the suspect was about to flee, and the like.</p>
<p>Watson's arrest did not violate the Fourth Amendment, and the Court of Appeals erred in holding to the contrary.</p>
<p></p>
<h2>III</h2>
<p>Because our judgment is that Watson's arrest comported with the Fourth Amendment, Watson's consent to the search of his car was not the product of an illegal arrest. To the extent that the issue of the voluntariness of Watson's consent was resolved on the premise that his arrest was illegal, the Court of Appeals was also in error.</p>
<p>We are satisfied in addition that the remaining factors relied upon by the Court of Appeals to invalidate Watson's consent are inadequate to demonstrate that, in the totality of the circumstances, Watson's consent was not his own "essentially free and unconstrained choice" because his "will ha[d] been overborne and his capacity for self-determination critically impaired." <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#225" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 225</a></span> (1973). There was no overt act or threat of force against Watson proved or claimed. There were no promises made to him and no indication of more subtle forms of coercion that might flaw his judgment. He had been arrested and was in custody, but his consent was given while on a public street, not in the confines of the police station. Moreover, the fact of custody alone has never been enough in itself to demonstrate a coerced confession or consent to search. Similarly, under <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span>,</i> the absence of proof that Watson knew he could withhold his consent, though it may be a factor in the overall judgment, is not to be given controlling significance. There is no indication in this record that Watson was a newcomer <span class="star-pagination">*425</span> to the law,<sup>[14]</sup> mentally deficient, or unable in the face of a custodial arrest to exercise a free choice. He was given <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and was further cautioned that the results of the search of his car could be used against him. He persisted in his consent.</p>
<p>In these circumstances, to hold that illegal coercion is made out from the fact of arrest and the failure to inform the arrestee that he could withhold consent would not be consistent with <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span></i> and would distort the voluntariness standard that we reaffirmed in that case.</p>
<p>In consequence, we reverse the judgment of the Court of Appeals.</p>
<p><i>So ordered.</i></p>
<p>MR. JUSTICE STEVENS took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE POWELL, concurring.</p>
<p>Although I concur in the opinion of the Court, I write to express additional views. I note at the outset that the case could be disposed of on the ground that respondent's consent to the search was plainly voluntary. <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973). Indeed, the evidence that his consent was the product of free will is so overwhelming that I would have held the consent voluntary even on the assumption that the preceding warrantless arrest was unconstitutional, and that the doctrine of <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), therefore was applicable. See <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975). The Court's different route to <span class="star-pagination">*426</span> the same result requires, however, an inquiry into the validity of the arrest itself.</p>
<p></p>
<h2>I</h2>
<p>Respondent was arrested without a warrant in a public restaurant six days after postal inspectors learned from a reliable source that he possessed stolen credit cards in violation of <span class="citation no-link">18 U. S. C. § 1708</span>. The Government made no effort to show that circumstances precluded the obtaining of a warrant, relying instead for the validity of the arrest solely upon the showing of probable cause to believe that respondent had committed a felony. Respondent contends, and the Court of Appeals held, that the absence of any exigency justifying the failure to procure a warrant renders this arrest violative of the Fourth Amendment.</p>
<p>In reversing the Court of Appeals, the Court concludes that nothing in our previous cases involving warrantless arrests supports the position of respondent and the Court of Appeals. See, <i>e. g., </i><i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#113" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 113</a></span> (1975). But it is fair to say, I think, that the prior decisions of the Court have assumed the validity of such arrests without addressing in a reasoned way the analysis advanced by respondent.<sup>[1]</sup> Today's decision is <span class="star-pagination">*427</span> the first square holding that the Fourth Amendment permits a duly authorized law enforcement officer to make a warrantless arrest in a public place even though he had adequate opportunity to procure a warrant after developing probable cause for arrest.</p>
<p>On its face, our decision today creates a certain anomaly. There is no more basic constitutional rule in the Fourth Amendment area than that which makes a warrantless search unreasonable except in a few "jealously and carefully drawn" exceptional circumstances. <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499</a></span> (1958); see <i>Almeida-Sanchez</i> v. <i>United States</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#279" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 279-280</a></span> (1973) (POWELL, J., concurring); <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#314" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 314-321</a></span> (1972); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#454" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 454-455</a></span> (1971). On more than one occasion this Court has rejected an argument that a law enforcement officer's own probable cause to search a private place for contraband or evidence of crime should excuse his otherwise unexplained failure to procure a warrant beforehand. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#450" aria-description="Citation for case: Coolidge v. New Hampshire"><i>Id.,</i> at 450</a></span>; <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span>, 356-358 <span class="star-pagination">*428</span> (1967). In short, the course of judicial development of the Fourth Amendment with respect to searches has remained true to the principles so well expressed by Mr. Justice Jackson:</p>
<blockquote>"Any assumption that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers. . . . When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948).</blockquote>
<p>Since the Fourth Amendment speaks equally to both searches and seizures, and since an arrest, the taking hold of one's person, is quintessentially a seizure, it would seem that the constitutional provision should impose the same limitations upon arrests that it does upon searches. Indeed, as an abstract matter an argument can be made that the restrictions upon arrest perhaps should be greater. A search may cause only annoyance and temporary inconvenience to the law-abiding citizen, assuming more serious dimension only when it turns up evidence of criminality. An arrest, however, is a serious personal intrusion regardless of whether the person seized is guilty or innocent. Although an arrestee cannot be held for a significant period without some neutral determination that there are grounds to do so, see <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein, supra,</a></span></i> no decision that he should go free can come quickly enough to erase the invasion of his privacy that already will have occurred. See <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#776" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 776</a></span> (1969) (WHITE, J., dissenting); cf. <i>United States</i> v. <span class="star-pagination">*429</span> <i>Robinson,</i> 414 U. S. 218, 237-238 (1973) (POWELL, J., concurring). Logic therefore would seem to dictate that arrests be subject to the warrant requirement at least to the same extent as searches.</p>
<p>But logic sometimes must defer to history and experience. The Court's opinion emphasizes the historical sanction accorded warrantless felony arrests. In the early days of the common law most felony arrests were made upon personal knowledge and without warrants. So established were such arrests as the usual practice that Lord Coke seriously questioned whether a justice of the peace, receiving his information secondhand instead of from personal knowledge, even could authorize an arrest by warrant. 4 E. Coke, Institutes 177 (6th ed. 1681). By the late 18th century it had been firmly established by Blackstone, with an intervening assist from Sir Matthew Hale, that magistrates could issue arrest warrants upon information supplied by others. 4 W. Blackstone, Commentaries *290; see 2 M. Hale, Pleas of the Crown *108-110. But recognition of the warrant power cast no doubt upon the validity of warrantless felony arrests, which continued to be practiced and upheld as before. 4 W. Blackstone, <i>supra,</i> at *282; 1 J. Chitty, Criminal Law *14-15. There is no historical evidence that the Framers or proponents of the Fourth Amendment, outspokenly opposed to the infamous general warrants and writs of assistance, were at all concerned about warrantless arrests by local constables and other peace officers. See N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 79-105 (1937); cf. <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#114" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 114-116</a></span>. As the Court today notes, the Second Congress' passage of an Act authorizing such arrests<sup>[2]</sup> so soon after the adoption of the Fourth Amendment <span class="star-pagination">*430</span> itself underscores the probability that the constitutional provision was intended to restrict entirely different practices.</p>
<p>The historical momentum for acceptance of warrantless arrests, already strong at the adoption of the Fourth Amendment, has gained strength during the ensuing two centuries. Both the judiciary and the legislative bodies of this Nation repeatedly have placed their imprimaturs upon the practice and, as the Government emphasizes, law enforcement agencies have developed their investigative and arrest procedures upon an assumption that warrantless arrests were valid so long as based upon probable cause. The decision of the Court of Appeals in this case was virtually unprecedented.<sup>[3]</sup> Of course, no practice that is inconsistent with constitutional protections can be saved merely by appeal to previous uncritical acceptance. But the warrantless felony arrest, long preferred at common law and unimpeached at the passage of the Fourth Amendment, is not such a practice. Given the revolutionary implications of such a holding, a declaration at this late date that warrantless felony arrests are constitutionally infirm would have to rest upon reasons more substantial than a desire to harmonize the rules for arrest with those governing searches. Cf. <i>United States</i> v. <i>Robinson, supra,</i> at 230.</p>
<p><span class="star-pagination">*431</span> Moreover, a constitutional rule permitting felony arrests only with a warrant or in exigent circumstances could severely hamper effective law enforcement. Good police practice often requires postponing an arrest, even after probable cause has been established, in order to place the suspect under surveillance or otherwise develop further evidence necessary to prove guilt to a jury.<sup>[4]</sup> Under the holding of the Court of Appeals such additional investigative work could imperil the entire prosecution. Should the officers fail to obtain a warrant initially, and later be required by unforeseen circumstances to arrest immediately with no chance to procure a lastminute warrant, they would risk a court decision that the subsequent exigency did not excuse their failure to get a warrant in the interim since they first developed probable cause. If the officers attempted to meet such a contingency <span class="star-pagination">*432</span> by procuring a warrant as soon as they had probable cause and then merely held it during their subsequent investigation, they would risk a court decision that the warrant had grown stale by the time it was used.<sup>[5]</sup> Law enforcement personnel caught in this squeeze could ensure validity of their arrests only by obtaining a warrant and arresting as soon as probable cause existed, thereby foreclosing the possibility of gathering vital additional evidence from the suspect's continued actions.</p>
<p>In sum, the historical and policy reasons sketched above fully justify the Court's sustaining of a warrantless arrest upon probable cause, despite the resulting divergence between the constitutional rule governing searches and that now held applicable to seizures of the person.<sup>[6]</sup></p>
<p></p>
<h2>II</h2>
<p>Finally, I share the view expressed in the opinion of MR. JUSTICE STEWART. It makes clear that we do not today consider or decide whether or under what circumstances <span class="star-pagination">*433</span> an officer lawfully may make a warrantless arrest in a private home or other place where the person has a reasonable expectation of privacy.<sup>[7]</sup></p>
<p>MR. JUSTICE STEWART, concurring in the result.</p>
<p>The arrest in this case was made upon probable cause in a public place in broad daylight. The Court holds that this arrest did not violate the Fourth Amendment, and I agree. The Court does <i>not</i> decide, nor could it decide in this case, whether or under what circumstances an officer must obtain a warrant before he may lawfully enter a private place to effect an arrest. See <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span>, 113 n. 13; <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#474" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 474-481</a></span>; <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#728" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 728</a></span>; <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499-500</a></span>.</p>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE BRENNAN joins, dissenting.</p>
<p>By granting police broad powers to make warrantless arrests, the Court today sharply reverses the course of our modern decisions construing the Warrant Clause of the Fourth Amendment. The Court turns next to the consent-to-search question last dealt with in <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span></i> <span class="star-pagination">*434</span> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973). Without acknowledgment or analysis, the Court extends the scope of that decision to the situation expressly reserved in <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span>,</i> and creates a rule inconsistent with <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span></i>'s own analysis. The Court takes both steps with a remarkable lack of consideration of either the facts of this case or the constitutional questions it is deciding. That is unfortunate not only because, in my view, the Court decides the constitutional questions wrongly, but also because consideration would have shown that the first question decided today is not raised by the facts before us, and that the second question should not be resolved here, given the present posture of this case. I respectfully dissent.</p>
<p></p>
<h2>I</h2>
<p>Before addressing what the Court does today, I note what it does not do. It does not decide this case on the narrow question that is presented. That is unfortunate for this is, fundamentally, a simple case.</p>
<p>On the afternoon of August 23, 1972, Awad Khoury, an informant of proved reliability, met with respondent Watson at a public restaurant under the surveillance of two postal inspectors. Khoury was under instructions to light a cigarette as a signal to the watching agents if Watson was in possession of stolen credit cards. Khoury lit a cigarette, and the postal inspectors moved in, made the arrest, and, ultimately, discovered under the floor mat of Watson's automobile the stolen credit cards that formed the basis of Watson's conviction and this appeal.</p>
<p>The signal of the reliable informant that Watson was in possession of stolen credit cards gave the postal inspectors probable cause to make the arrest. This probable cause was separate and distinct from the probable cause relating to the offense six days earlier, and provided an <span class="star-pagination">*435</span> adequate independent basis for the arrest. Whether or not a warrant ordinarily is required prior to making an arrest, no warrant is required when exigent circumstances are present. When law enforcement officers have probable cause to believe that an offense is taking place in their presence and that the suspect is at that moment in possession of the evidence, exigent circumstances exist. Delay could cause the escape of the suspect or the destruction of the evidence. Accordingly, Watson's warrantless arrest was valid under the recognized exigent-circumstances exception to the warrant requirement, and the Court has no occasion to consider whether a warrant would otherwise be necessary.<sup>[1]</sup></p>
<p>This conclusion should properly dispose of the case before us. As the Court observes, <i>ante,</i> at 414, the Court of Appeals relied heavily on the supposed illegality of Watson's arrest in ruling that his consent to the search of his car was coerced. Neither the opinion of the Court of Appeals nor the briefs of the parties here address the remaining issue of the circumstances under which consent to search given by a suspect <i>lawfully</i> in custody may be deemed coerced. Since that issue is both complex and <span class="star-pagination">*436</span> expressly reserved in <i>Schneckloth</i> v. <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Bustamonte, supra</a></span></i><i>,</i> I think it inappropriate for resolution without the benefit of the views of the parties and the Court of Appeals. Accordingly, I would reverse the Court of Appeals on the legality of the arrest, vacate its judgment, and remand the case to that court for further proceedings.</p>
<p></p>
<h2>II</h2>
<p>Since, for reasons it leaves unexpressed, the Court does not take this traditional course, I am constrained to express my views on the issues it unnecessarily decides. The Court reaches its conclusion that a warrant is not necessary for a police officer to make an arrest in a public place, so long as he has probable cause to believe a felony has been committed, on the basis of its views of precedent and history. As my Brother POWELL correctly observes, <i>ante,</i> at 426-427, n. 1 (concurring), the precedent is spurious. None of the cases cited by the Court squarely confronted the issue decided today. Moreover, an examination of the history relied on by the Court shows that it does not support the conclusion laid upon it. After showing why, in my view, the Court's rationale does not support today's result, I shall examine the relevant decisions and suggest what I believe to be the proper rule for arrests.</p>
<p>The Fourth Amendment provides:</p>
<blockquote>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</blockquote>
<p>There is no doubt that by the reference to the seizure of persons, the Fourth Amendment was intended to <span class="star-pagination">*437</span> apply to arrests. <i>Ex parte Burford,</i> <span class="citation" data-id="84827"><a href="/opinion/84827/ex-parte-burford/" aria-description="Citation for case: Ex Parte Burford">3 Cranch 448</a></span> (1806). See generally N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 79-82 (1937). Indeed, we have often considered whether arrests were made in conformity with the Fourth Amendment. <i>E. g., </i><i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span> (1964); <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963); <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959); <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span> (1958). Admittedly, as the Court observes, some of our decisions make passing reference to the common-law rule on arrests. <i>E. g., </i><i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 156</a></span> (1925); <i>Bad Elk</i> v. <i>United States,</i> <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/#534" aria-description="Citation for case: Bad Elk v. United States">177 U. S. 529, 534</a></span> (1900); <i>Kurtz</i> v. <i>Moffitt,</i> <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/#498" aria-description="Citation for case: Kurtz v. Moffitt">115 U. S. 487, 498-499</a></span> (1885). However, none of the cases cited by the Court, nor any other warrantless arrest case in this Court, mandates the decision announced today. Frequently exigent circumstances were present, so that the warrantless arrest was proper even if a warrant ordinarily may be required. <i>Ker</i> v. <i>California, supra</i><i>; </i><i>Draper</i> v. <i>United States, supra</i><i>; </i><i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/" aria-description="Citation for case: United States v. Di Re">332 U. S. 581</a></span> (1948). Many cases have invalidated arrests as not based on probable cause, thereby bypassing the need to reach the warrant question. <i>E. g., </i><i>Beck</i> v. <i>Ohio, supra</i><i>; </i><i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span> (1959). Elsewhere the Court has simply assumed the propriety of the arrest and resolved the case before it on other grounds. <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969). Cf. <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#476" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 476</a></span> (1971). And in other cases, the Court noted, but did not reach, the warrantless-arrest issue, <i>E. g., </i><i>Giordenello</i> v. <i>United States, supra</i><i>.</i> In sum, as the case-by-case analysis undertaken by my Brother POWELL demonstrates, the dicta relied upon by the Court in support of its decision today are just thatdicta. See <i>ante,</i> at 426-427, n. 1 (concurring). They are no substitute <span class="star-pagination">*438</span> for reasoned analysis of the relationship between the warrant requirement and the law of arrest.</p>
<p>The Court next turns to history. It relies on the English common-law rule of arrest and the many state and federal statutes following it. There are two serious flaws in this approach. First, as a matter of factual analysis, the substance of the ancient common-law rule provides no support for the far-reaching modern rule that the Court fashions on its model. Second, as a matter of doctrine, the longstanding existence of a Government practice does not immunize the practice from scrutiny under the mandate of our Constitution.</p>
<p>The common-law rule was indeed as the Court states it:</p>
<blockquote>"[A] peace officer was permitted to arrest without a warrant for a misdemeanor or felony committed in his presence as well as for a felony not committed in his presence if there was reasonable ground for making the arrest." <i>Ante,</i> at 418, and sources cited.</blockquote>
<p>See also <i>Kurtz</i> v. <i><span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/" aria-description="Citation for case: Kurtz v. Moffitt">Moffitt, supra</a></span></i><i>; </i><i>Bad Elk</i> v. <i>United States, supra</i><i>.</i> To apply the rule blindly today, however, makes as much sense as attempting to interpret Hamlet's admonition to Ophelia, "Get thee to a nunnery, go,"<sup>[2]</sup> without understanding the meaning of Hamlet's words in the context of their age.<sup>[3]</sup> For the fact is that a felony at common law and a felony today bear only slight resemblance, with the result that the relevance of the common-law rule of arrest to the modern interpretation of our Constitution is minimal.</p>
<p>Both at common law and today, felonies find definition in the penal consequences of crime rather than the <span class="star-pagination">*439</span> nature of the crime itself. At common law, as this Court has several times recognized,</p>
<blockquote>"No crime was considered a felony which did not occasion a total forfeiture of the offender's lands, or goods, or both." <i>Kurtz</i> v. <i>Moffitt,</i> <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/#499" aria-description="Citation for case: Kurtz v. Moffitt">115 U. S., at 499</a></span>.</blockquote>
<p>See also <i>Ex parte Wilson,</i> <span class="citation" data-id="91385"><a href="/opinion/91385/ex-parte-wilson/#423" aria-description="Citation for case: Ex Parte Wilson">114 U. S. 417, 423</a></span> (1885); 4 W. Blackstone, Commentaries *95.<sup>[4]</sup> At present, on the other hand,</p>
<blockquote>"Any offense punishable by death or imprisonment for a term exceeding one year is a felony." <span class="citation no-link">18 U. S. C. § 1</span> (1).<sup>[5]</sup></blockquote>
<p>This difference reflects more than changing notions of penology. It reflects a substantive change in the kinds of crimes called felonies. <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S., at 158</a></span>.<sup>[6]</sup> Only the most serious crimes were felonies at common law, and many crimes now classified <span class="star-pagination">*440</span> as felonies under federal or state law were treated as misdemeanors. Professor Wilgus has summarized and documented the cases:</p>
<blockquote>"At common law an assault was a misdemeanor and it was still only such even if made with the intent to rob, murder, or rape. Affrays, abortion, barratry, bribing voters, challenging to fight, compounding felonies, cheating by false weights or measures, escaping from lawful arrest, eavesdropping, forgery, false imprisonment, forcible and violent entry, forestalling, kidnapping, libel, mayhem, maliciously killing valuable animals, obstructing justice, public nuisance, perjury, riots and routs, etc. were misdemeanors. . . ." Wilgus, Arrest Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 541</span>, 572-573 (1924) (footnotes omitted).</blockquote>
<p>See also 9 Halsbury's Laws of England 450-793 (1909).<sup>[7]</sup> To make an arrest for any of these crimes at common law, the police officer was required to obtain a warrant, unless the crime was committed in his presence.<sup>[8]</sup> Since many of these same crimes are commonly classified as felonies today,<sup>[9]</sup> however, under the Court's holding a <span class="star-pagination">*441</span> warrant is no longer needed to make such arrests, a result in contravention of the common law.</p>
<p>Thus the lesson of the common law, and those courts in this country that have accepted its rule, is an ambiguous one. Applied in its original context, the common-law rule would allow the warrantless arrest of some, but not all, of those we call felons today. Accordingly, the Court is simply historically wrong when it tells us that "[t]he balance struck by the common law in generally authorizing felony arrests on probable cause, but without a warrant, has survived substantially intact." <i>Ante,</i> at 421. As a matter of substance, the balance struck by the <span class="star-pagination">*442</span> common law in accommodating the public need for the most certain and immediate arrest of criminal suspects with the requirement of magisterial oversight to protect against mistaken insults to privacy decreed that only in the most serious of cases could the warrant be dispensed with. This balance is not recognized when the common-law rule is unthinkingly transposed to our present classifications of criminal offenses. Indeed, the only clear lesson of history is contrary to the one the Court draws: the common law considered the arrest warrant far more important than today's decision leaves it.</p>
<p>I do not mean by this that a modern warrant requirement should apply only to arrests precisely analogous to common-law misdemeanors, and be inapplicable to analogous of common-law felonies. Rather, the point is simply that the Court's unblinking literalism cannot replace analysis of the constitutional interests involved. While we can learn from the common law, the ancient rule does not provide a simple answer directly transferable to our system. Thus, in considering the applicability of the common-law rule to our present constitutional scheme, we must consider <i>both</i> of the rule's two opposing constructs: the presumption favoring warrants, as well as the exception allowing immediate arrests of the most dangerous criminals. The Court's failure to do so, indeed its failure to recognize any tension in the common-law rule at all, drains all validity from its historical analysis.</p>
<p>Lastly, the Court relies on the numerous state and federal statutes codifying the common-law rule. But this, too, is no substitute for reasoned analysis. True enough, the national and state legislatures have steadily ratified the drift of the balance struck by the common-law rule past the bounds of its original intent. And it is true as well, as the Court observes, that a presumption of constitutionality attaches to every Act of Congress. But neither observation is determinative of the constitutional issue, <span class="star-pagination">*443</span> and the doctrine of deference that the Court invokes is contrary to the principles of constitutional analysis practiced since <i>Marbury</i> v. <i>Madison,</i> <span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/" aria-description="Citation for case: Marbury v. Madison">1 Cranch 137</a></span> (1803). The Court's error on this score is far more dangerous than its misreading of history, for it is well settled that the mere existence of statutes or practice, even of long standing, is no defense to an unconstitutional practice. "[N]o one acquires a vested or protected right in violation of the Constitution by long use, even when that span of time covers our entire national existence and indeed predates it." <i>Walz</i> v. <i>Tax Comm'n,</i> <span class="citation" data-id="9841980"><a href="/opinion/108135/walz-v-tax-commn-of-city-of-new-york/#678" aria-description="Citation for case: Walz v. Tax Comm&#x27;n of City of New York">397 U. S. 664, 678</a></span> (1970). See also <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973); <i>Roe</i> v. <i>Wade,</i> <span class="citation" data-id="9425157"><a href="/opinion/108713/roe-v-wade/" aria-description="Citation for case: Roe v. Wade">410 U. S. 113</a></span> (1973); <i>Furman</i> v. <i>Georgia,</i> <span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/" aria-description="Citation for case: Furman v. Georgia">408 U. S. 238</a></span> (1972); <i>Reynolds</i> v. <i>Sims,</i> <span class="citation" data-id="9422829"><a href="/opinion/106850/reynolds-v-sims/" aria-description="Citation for case: Reynolds v. Sims">377 U. S. 533</a></span> (1964).<sup>[10]</sup> Our function in constitutional cases is weightier than the Court today suggests: where reasoned analysis shows a practice to be constitutionally deficient, our obligation is to the Constitution, not the Congress.</p>
<p>In sum, the Court's opinion is without foundation. It relies on precedents that are not precedents. It relies on history that offers no clear rule to impose, but only conflicting interests to balance. It relies on statutes that constitute, at best, no more than an aid to construction. The Court never grapples with the warrant requirement of the Fourth Amendment and the cases construing it. It simply announces, by <i>ipse dixit,</i> a rule squarely rejecting the warrant requirement we have favored for so long.</p>
<p></p>
<h2>III</h2>
<p>My Brother POWELL concludes: "Logic . . . would seem to dictate that arrests be subject to the warrant <span class="star-pagination">*444</span> requirement at least to the same extent as searches." <i>Ante,</i> at 429 (concurring). I agree.</p>
<p>One of the few absolutes of our law is the requirement that, absent the presence of one of a few "jealously and carefully drawn" exceptions, <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499</a></span> (1958), a warrant be obtained prior to any search.<sup>[11]</sup> "[E]xcept in certain carefully defined classes of cases, a search of private property without proper consent is `unreasonable' [within the meaning of the Fourth Amendment] unless it has been authorized by a valid search warrant." <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528-529</a></span> (1967). See <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#439" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 439</a></span> (1973); <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#315" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 315-316, 318</a></span> (1972); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#454" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 454-455</a></span>; <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California">395 U. S., at 762</a></span>; <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968); <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (1967).</p>
<p>The rule the Court announces today for arrests is the reverse of this approach. It is, in essence, the <i>Rabinowitz</i> rule: "The relevant test is not whether it is reasonable to procure [an arrest] warrant, but whether the [arrest] was reasonable." <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 66</a></span> (1950). In the search context, <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> has been overruled, <i>Chimel</i> v. <i>California, supra,</i> at 764-768, and thoroughly discredited, see, <i>e. g., </i><i>United States</i> v. <i>United States District Court, supra,</i> at 315, and n. 16. The <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> approach simply does not provide adequate protection for the important personal privacy interests codified in the <span class="star-pagination">*445</span> Fourth Amendment. Given "[t]he history of the use, and not infrequent abuse, of the power to arrest," <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#479" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 479</a></span> (1963), and the fact that arrests are, in terms, as fully governed by the Fourth Amendment as searches, the logical presumption is that arrests and searches should be treated equally under the Fourth Amendment. Analysis of the interests involved confirms this supposition.</p>
<p>The Court has typically engaged in a two-part analysis in deciding whether the presumption favoring a warrant should be given effect in situations where a warrant has not previously been clearly required. Utilizing that approach we must now consider (1) whether the privacy of our citizens will be better protected by ordinarily requiring a warrant to be issued before they may be arrested; and (2) whether a warrant requirement would unduly burden legitimate governmental interests. <i>United States</i> v. <i>United States District Court, supra,</i> at 315; <i>Camara</i> v. <i>Municipal Court, supra,</i> at 533.</p>
<p>The first question is easily answered. Of course, the privacy of our citizens will be better protected by a warrant requirement. We have recognized that "the Fourth Amendment protects people, not places." <i>Katz</i> v. <i>United States, supra,</i> at 351. Indeed, the privacy guaranteed by the Fourth Amendment is quintessentially personal. Cf. <i>Roe</i> v. <i><span class="citation" data-id="9425157"><a href="/opinion/108713/roe-v-wade/" aria-description="Citation for case: Roe v. Wade">Wade, supra</a></span></i><i>; </i><i>Doe</i> v. <i>Bolton,</i> <span class="citation" data-id="9425160"><a href="/opinion/108714/doe-v-bolton/" aria-description="Citation for case: Doe v. Bolton">410 U. S. 179</a></span> (1973); <i>Griswold</i> v. <i>Connecticut,</i> <span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/" aria-description="Citation for case: Griswold v. Connecticut">381 U. S. 479</a></span> (1965). Thus a warrant is required in search situations not because of some high regard for property, but because of our regard for the individual, and <i>his</i> interest in his possessions and person.</p>
<blockquote>"It is not the breaking of his doors, and the rummaging of his drawers, that constitutes the essence of the offense; but it is the invasion of his indefeasible right of personal security, personal liberty and <span class="star-pagination">*446</span> private property, where that right has never been forfeited by his conviction of some public offense, it is the invasion of this sacred right which underlies and constitutes the essence of Lord Camden's judgment [in the classic English warrant case of <i>Entick</i> v. <i>Carrington,</i> 19 How. St. Tr. 1029, 95 Eng. Rep. 807 (1765)]." <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span> (1886).</blockquote>
<p>Not only is the Fourth Amendment directly addressed to the privacy of our citizens, but it speaks in indistinguishable terms about the freedom of both persons and property from unreasonable seizures. A warrant is required in the search situation to protect the privacy of the individual, but there can be no less invasion of privacy when the individual himself, rather than his property, is searched and seized. Indeed, an unjustified arrest that forces the individual temporarily to forfeit his right to control his person and movements and interrupts the course of his daily business may be more intrusive than an unjustified search.</p>
<blockquote>"Being arrested and held by the police, even if for a few hours, is, for most persons, awesome and frightening. Unlike other occasions on which one may be authoritatively required to be somewhere or do something, an arrest abruptly subjects a person to constraint, and removes him to unfamiliar and threatening surroundings. Moreover, this exercise of control over the person depends not just on his willingness to comply with an impersonal directive, such as a summons or subpoena, but on an order which a policeman issues on the spot and stands ready then and there to back up with force. The security of the individual requires that so abrupt and intrusive an authority be granted to public officials only on a guarded basis." ALI, Model Code <span class="star-pagination">*447</span> of Pre-arraignment Procedure, Commentary 290-291 (1975).</blockquote>
<p>A warrant requirement for arrests would, of course, minimize the possibility that such an intrusion into the individual's sacred sphere of personal privacy would occur on less than probable cause. Primarily for this reason, a warrant is required for searches. Surely there is no reason to place greater trust in the partisan assessment of a police officer that there is probable cause for an arrest than in his determination that probable cause exists for a search.<sup>[12]</sup> Last Term the Court unanimously recognized <span class="star-pagination">*448</span> that detention of a person cannot be prolonged without judicial oversight of the probable-cause determination. <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span> (1975). But while <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> may provide the best protection possible against less-than-probable-cause warrantless arrests based on exigent circumstances, it does not fully protect the Fourth Amendment rights at stake here. A less-than-probable-cause arrest followed by a <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> release is as offensive to the Fourth Amendment as a less-than-probable-cause search that fails to uncover the evidence sought, and the requirement of a warrant is as instrumental in protecting against the one as the other. Indeed, the Court's opinion in <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> expressly recognizes that maximum protection of individual rights can only be realized "by requiring a magistrate's review of the factual justification prior to any arrest . . . ." <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#113" aria-description="Citation for case: Gerstein v. Pugh"><i>Id.,</i> at 113</a></span>.</p>
<p>We come then to the second part of the warrant test: whether a warrant requirement would unduly burden legitimate law enforcement interests. Dicta in <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> answer this question in the affirmative, and these concerns are somewhat amplified in the concurrence of my Brother POWELL. <i>Ante,</i> at 431-432. I believe, however, that the suggested concerns are wholly illusory. Indeed, the argument that a warrant requirement for arrests would be an onerous chore for the police seems somewhat anomalous in light of the Government's concession that "it is the standard practice of the Federal Bureau of Investigation [FBI] to present its evidence to the United States Attorney, and to obtain a warrant, before making an arrest." Brief for United States 26 n. 15. In the past, the practice and experience of the FBI have been taken as a substantial indication that no intolerable burden would be presented by a proposed rule of procedure. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#483" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 483-486</a></span> (1966). <span class="star-pagination">*449</span> There is no reason to accord less deference to the FBI practice here.<sup>[13]</sup></p>
<p>The Government's assertion that a warrant requirement would impose an intolerable burden stems, in large part, from the specious supposition that procurement of an arrest warrant would be necessary as soon as probable cause ripens. Brief for United States 22-24. There is no requirement that a search warrant be obtained the moment police have probable cause to search. The rule is only that present probable cause be shown and a warrant obtained before a search is undertaken.<sup>[14]</sup> Fed. Rule Crim. Proc. 41. Cf. <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#59" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 59</a></span> (1967). The same rule should obtain for arrest warrants, where it may even make more sense. Certainly, there is less need for prompt procurement of a warrant in the arrest situation. Unlike probable cause to search, probable cause to arrest, once formed, will continue to exist for the indefinite future, at least if no intervening exculpatory facts come to light. See <i>Wilson</i> v. <i>United States,</i> 117 U. S. App. D. C. 28, <span class="citation" data-id="262538"><a href="/opinion/262538/percy-e-wilson-v-united-states/" aria-description="Citation for case: Percy E. Wilson v. United States">325 F. 2d 224</a></span> (1963), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./377/1005/">377 U. S. 1005</a></span> (1964), and <span class="star-pagination">*450</span> <i>United States</i> v. <i>Wilson,</i> <span class="citation" data-id="267195"><a href="/opinion/267195/united-states-v-percy-wilson/" aria-description="Citation for case: United States v. Percy Wilson">342 F. 2d 782</a></span> (CA2 1965) (both upholding delay of 16 months between formation of probable cause and issuance of arrest warrant). Cf. <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#310" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 310</a></span> (1966).</p>
<p>This sensible approach obviates most of the difficulties that have been suggested with an arrest warrant rule. Police would not have to cut their investigation short the moment they obtain probable cause to arrest, nor would undercover agents be forced suddenly to terminate their work and forfeit their covers. <i>Godfrey</i> v. <i>United States,</i> 123 U. S. App. D. C. 219, <span class="citation" data-id="271327"><a href="/opinion/271327/larry-c-godfrey-v-united-states/" aria-description="Citation for case: Larry C. Godfrey v. United States">358 F. 2d 850</a></span> (1966). Moreover, if in the course of the continued police investigation exigent circumstances develop that demand an immediate arrest, the arrest may be made without fear of unconstitutionality, so long as the exigency was unanticipated and not used to avoid the arrest warrant requirement. Cf. <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#469" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 469-471</a></span> (evidence may be seized if in plain view only if its discovery is inadvertent). Likewise, if in the course of the continued investigation police uncover evidence tying the suspect to another crime, they may immediately arrest him for that crime if exigency demands it, and still be in full conformity with the warrant rule. This is why the arrest in this case was not improper.<sup>[15]</sup> Other than where police attempt to evade the warrant requirement, the rule would invalidate an arrest only in the obvious situation: where police, with probable cause but without exigent circumstances, set out to arrest a suspect. Such an arrest must be void, even if exigency develops in the course of the arrest that <span class="star-pagination">*451</span> would ordinarily validate it; otherwise the warrant requirement would be reduced to a toothless prescription.</p>
<p>In sum, the requirement that officers about to arrest a suspect ordinarily obtain a warrant before they do so does not seem unduly burdensome, at least no more burdensome than any other requirement that law enforcement officials undertake a new procedure in order to comply with the dictates of the Constitution. Cf. <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span> (1975); <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967); <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967); <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona, supra</a></span></i><i>; </i><i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span> (1963).</p>
<p>It is suggested, however, that even if application of this rule does not require police to secure a warrant as soon as they obtain probable cause, the confused officer would nonetheless be prone to do so. If so, police "would risk a court decision that the warrant had grown stale by the time it was used." <i>Ante,</i> at 432 (POWELL, J., concurring) (footnote omitted). This fear is groundless. First, as suggested above, the requirement that police procure a warrant before an arrest is made is rather simple of application. Thus, there is no need for the police to find themselves in this "squeeze." Second, the "squeeze" is nonexistent. Just as it is virtually impossible for probable cause for an arrest to grow stale between the time of formation and the time a warrant is procured, it is virtually impossible for probable cause to become stale between procurement and arrest.<sup>[16]</sup> Delay by law enforcement officers in executing an arrest warrant does not ordinarily affect the legality of the arrest.<sup>[17]</sup><span class="star-pagination">*452</span> <i>United States</i> v. <i>Wilson, supra</i><i>; </i><i>Wilson</i> v. <i>United States, supra</i><i>; </i><i>Carlo</i> v. <i>United States,</i> <span class="citation" data-id="9447739"><a href="/opinion/253075/john-carlo-v-united-states/#846" aria-description="Citation for case: John Carlo v. United States">286 F. 2d 841, 846</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./366/944/">366 U. S. 944</a></span> (1961); <i>United States</i> v. <i>Joines,</i> <span class="citation" data-id="245925"><a href="/opinion/245925/united-states-v-j-paul-joines-and-john-robert-joines-appeal-of-john/" aria-description="Citation for case: United States v. J. Paul Joines and John Robert Joines....">258 F. 2d 471</a></span> (CA3), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./358/880/">358 U. S. 880</a></span> (1958); <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9445492"><a href="/opinion/241496/veto-giordenello-v-united-states/" aria-description="Citation for case: Veto Giordenello v. United States">241 F. 2d 575</a></span> (CA5 1957), rev'd on other grounds, <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span> (1958). In short, staleness should be the least of an arresting officer's worries.<sup>[18]</sup></p>
<p>Thus, the practical reasons marshaled against an arrest warrant requirement are unimpressive.<sup>[19]</sup> If anything, the virtual nonexistence of a staleness problem suggests that such a requirement would be less burdensome for police than the search warrant rule. And given the significant protection our citizens will gain from a warrant requirement, accepted Fourth Amendment <span class="star-pagination">*453</span> analysis dictates that a warrant rule be imposed. This conclusion, then, answers the questions posed by analysis of the common-law rule on arrest. In choosing between the common law's prescription that a warrant ordinarily be obtained for the arrest of persons suspected of committing less serious crimes, and the common-law exception allowing warrantless arrests of suspects in more serious offenses, the intervention of our Fourth Amendment and the cases developing its application necessarily favor the former approach. Thus, I believe the proper result is application of the warrant requirement, as it has developed in the search context, to all arrests.</p>
<p></p>
<h2>IV</h2>
<p>Accordingly, I dissent from the Court's contrary holding. It is always disheartening when the Court ignores a relevant body of precedent and eschews any considered analysis. It is more so when the result of such an approach is a rule that "leave[s] law-abiding citizens at the mercy of the officers' whim or caprice," <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span> (1949), and renders the constitutional protection of our "persons" a nullity. The consequences of the Court's casually adopted rationale are clear.</p>
<p>First, the opinion all but answers the question raised in <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#480" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 480-481</a></span>, namely, "whether and under what circumstances an officer may enter a suspect's home to make a warrantless arrest." <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 113</a></span> n. 13.<sup>[20]</sup><span class="star-pagination">*454</span> Admittedly, my Brothers STEWART and POWELL do not read the opinion to resolve that issue and, indeed, the Court purports to leave it open. <i>Ante,</i> at 418 n. 6. But the mode of analysis utilized herereliance on the common law and federal and state statutesprovides a ready answer, as indeed the Court hints by its extended discussion of § 120.6 of the ALI Model Code of Prearraignment Procedure and its relevant commentary. <i>Ante,</i> at 418 n. 6. See also Wilgus, 22 Mich. L. Rev., at 800 ("For a felony . . . one may break into the dwelling house to take the felon . . ."); <i>id.,</i> at 558, 803; 9 Halsbury's Laws of England 307 (1909); 1 J. Chitty, Criminal Law *23; 4 W. Blackstone, Commentaries *292. Unless the approach of this opinion is to be fundamentally rejected, it will be difficult, if not impossible, to follow these sources to any but one conclusionthat entry to effect a warrantless arrest is permissible.</p>
<p>Second, by paying no attention whatever to the substance of the offense, and considering only whether it is labeled "felony," the Court, in the guise of "constitutionalizing" the common-law rule, actually does away with it altogether, replacing it with the rule that the police may, consistent with the Constitution, arrest on probable cause anyone who they believe has committed any sort of crime at all. Certainly this rule would follow <span class="star-pagination">*455</span> if the legislatures redenominated all crimes as "felonies." As a matter of substance, it would seem to follow in any event from the holding of this case, for the Court surely does not intend to accord constitutional status to a distinction that can be readily changed by legislative fiat.<sup>[21]</sup></p>
<p>Lastly, the Court surrenders the opportunity to put teeth in our oft-expressed preference for the use of arrest warrants. <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S., at 96</a></span>; <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#479" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 479-482</a></span>. While some incentives for police to obtain arrest warrants remain,<sup>[22]</sup><span class="star-pagination">*456</span> they are only indirect and have proved ineffective in the past in assuring routine application for arrest warrants when the circumstances permit it. By our holding today, the preference for an arrest warrant, which the Court has conceded is the optimal method to protect our citizens from the affront of an unlawful arrest, will remain only an ideal, one that the Court will espouse but not enforce.</p>
<p></p>
<h2>V</h2>
<p>Having disposed of the suggestion that the Fourth Amendment requires a warrant of arrest before the police may seize our persons, the Court turns its attention, briefly, to whether Watson voluntarily consented to the search of his automobile. I have suggested above that because this issue is of some complexity and has not been thoroughly briefed for us I would remand this case for initial consideration of the question by the Court of Appeals. The Court, however, finds the question simplicity itself. It applies the "totality of the circumstances" test established in <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973), and treats the question as merely requiring the application of settled law to the facts before us.</p>
<p>That is not the case. Watson was in custody when his consent was obtained. The lack of custody was of decisional importance in <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span>,</i> which repeatedly distinguished the case before it from one involving a suspect in custody. <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#232" aria-description="Citation for case: Schneckloth v. Bustamonte"><i>Id.,</i> at 232, 240-241</a></span>, and n. 29, 246-248, and n. 36. The Court held:</p>
<blockquote>"Our decision today is a narrow one. We hold only that <i>when the subject of a search is not in custody</i> and the State attempts to justify a search on the basis of his consent, the Fourth and Fourteenth <span class="star-pagination">*457</span> Amendments require that it demonstrate that the consent was in fact voluntarily given, and not the result of duress or coercion, express or implied." <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#248" aria-description="Citation for case: Schneckloth v. Bustamonte"><i>Id.,</i> at 248</a></span> (emphasis added).</blockquote>
<p>Not once, but twice, the question the Court today treats as settled was expressly reserved:</p>
<blockquote>"[T]he present case does not require a determination of the proper standard to be applied in assessing the validity of a search authorized solely by an alleged consent that is obtained from a person after he has been placed in custody." <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Id.,</a></span></i> at 241 n. 29.</blockquote>
<p>See also <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">id.,</a></span></i> at 247 n. 36.</p>
<p>I adhere to the views expressed in my dissent in <i>Schneckloth, id.,</i> at 277, and therefore believe that the Government must always show that a person who consented to a search did so knowing he had the right to refuse. But even short of this position, there are valid reasons for application of such a rule to consents procured from suspects held in custody. It was, apparently, the force of those reasons that prompted the Court in <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span></i> to reserve the question. Most significantly, we have previously accorded constitutional recognition to the distinction between custodial and noncustodial police contacts. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#477" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 477-478</a></span>. Indeed, <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span></i> directly relied on <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s articulation of that distinction to reach its conclusion. <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#232" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., at 232</a></span>. Thus, while custodial interrogation is inherently coercive, and any consent thereby obtained necessarily suspect, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> (and <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span></i>) expressly reject the notion that there is anything inherently coercive about general noncustodial interrogation. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#477" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 477-478</a></span>; <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#247" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., at 247</a></span>. For this reason it is entirely appropriate to place a substantially greater burden on the Government <span class="star-pagination">*458</span> to validate a consent obtained from a suspect following custodial interrogation, however brief. Indeed, it is difficult, if not impossible, to square a contrary conclusion with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> A substantially greater burden on the Government means, quite obviously, that the fact of custody is not merely another factor to be considered in the "totality of the circumstances."<sup>[23]</sup> And, in my view, it means that the Government must show that the suspect knew he was not obligated to consent to the search.</p>
<p>Whether after due consideration the Court would accept this view or not, it is a surrender of our judicial task altogether to ignore the question. And, equally disturbing, it is a distortion of our precedent to pretend that what seemed a difficult and complex problem three years ago is no problem at all today.</p>
<p>I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[1]  In the meantime the inspector had verified that the card was stolen.</p>
<p>[2]  Title <span class="citation no-link">18 U. S. C. § 1708</span> punishes the theft of mail as well as the possession of stolen mail. The punishment is a fine of not more than $2,000 or imprisonment for not more than five years, or both.</p>
<p>[3]  Watson was acquitted on the second count. The fourth was dismissed prior to trial.</p>
<p>[4]  At least since approval of the Act of June 10, 1955, c. 137, § 203, <span class="citation no-link">69 Stat. 106</span>, <span class="citation no-link">39 U. S. C. § 3523</span> (a) (2) (K) (1964 ed.), postal inspectors' duties have been thought to permit arrest without a warrant upon probable cause. Compare <i>United States</i> v. <i>Helbock,</i> <span class="citation" data-id="2304502"><a href="/opinion/2304502/united-states-v-helbock/" aria-description="Citation for case: United States v. Helbock">76 F. Supp. 985</a></span> (Ore. 1948), with <i>United States</i> v. <i>Alexander,</i> <span class="citation" data-id="286516"><a href="/opinion/286516/united-states-v-orlando-c-alexander/" aria-description="Citation for case: United States v. Orlando C. Alexander">415 F. 2d 1352</a></span> (CA7 1969), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./397/1014/">397 U. S. 1014</a></span> (1970); <i>Kelley</i> v. <i>Dunne,</i> <span class="citation" data-id="9450633"><a href="/opinion/267556/john-j-kelley-v-raymond-j-dunne-two-cases-elizabeth-ann-kelley-v/" aria-description="Citation for case: John J. Kelley v. Raymond J. Dunne, (Two Cases)....">344 F. 2d 129</a></span> (CA1 1965); and <i>United States</i> v. <i>Bell,</i> <span class="citation" data-id="8769475"><a href="/opinion/8785630/united-states-v-bell/" aria-description="Citation for case: United States v. Bell">294 F. Supp. 1314</a></span> (ND Ill. 1968). The Court of Appeals for the Ninth Circuit held, however, that § 3523 (a) (2) (K) did not give the necessary express power to arrest, but that a warrantless arrest by a postal inspector could be upheld by resort to a citizen's power to arrest. <i>United States</i> v. <i>DeCatur,</i> <span class="citation" data-id="291586"><a href="/opinion/291586/united-states-v-arthur-ronald-decatur/" aria-description="Citation for case: United States v. Arthur Ronald Decatur">430 F. 2d 365</a></span> (1970); <i>Neggo</i> v. <i>United States,</i> <span class="citation" data-id="279069"><a href="/opinion/279069/rein-neggo-jr-v-united-states/" aria-description="Citation for case: Rein Neggo, Jr. v. United States">390 F. 2d 609</a></span> (1968); <i>Ward</i> v. <i>United States,</i> <span class="citation" data-id="260271"><a href="/opinion/260271/james-vernon-ward-v-united-states/" aria-description="Citation for case: James Vernon Ward v. United States">316 F. 2d 113</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./375/862/">375 U. S. 862</a></span> (1963).
</p>
<p>In 1968 in the face of confusion generated by these decisions and two others striking down warrantless arrests by postal inspectors as not authorized by federal statute or by state law, <i>Alexander</i> v. <i>United States,</i> <span class="citation" data-id="278957"><a href="/opinion/278957/rodney-leon-alexander-v-united-states/" aria-description="Citation for case: Rodney Leon Alexander v. United States">390 F. 2d 101</a></span> (CA5 1968); <i>United States</i> v. <i>Moderacki,</i> <span class="citation" data-id="1607433"><a href="/opinion/1607433/united-states-v-moderacki/" aria-description="Citation for case: United States v. Moderacki">280 F. Supp. 633</a></span> (Del. 1968), the Congress enacted <span class="citation no-link">18 U. S. C. § 3061</span> to make clear that postal inspectors are empowered to arrest without warrant upon probable cause. <span class="citation no-link">Pub. L. 90-560, § 5</span> (a), <span class="citation no-link">82 Stat. 998</span>; H. R. Conf. Rep. No. 1918, 90th Cong., 2d Sess., 6 (1968); H. R. Rep. No. 1725, 90th Cong., 2d Sess. (1968); 114 Cong. Rec. 20914-20915, 26928, 28864-28865 (1968).</p>
<p>[5]  There are other federal officers subject to a more restrictive statutory standard. See, <i>e. g.,</i> <span class="citation no-link">18 U. S. C. § 3050</span>, with respect to employees of the Bureau of Prisons.</p>
<p>[6]  In the case before us the Court of Appeals relied heavily, but mistakenly, on <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#480" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 480-481</a></span> (1971), for as we noted in <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 113</a></span> n. 13, the still unsettled question posed in that part of the <i><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span></i> opinion was "whether and under what circumstances an officer may enter a suspect's home to make a warrantless arrest." Watson's midday public arrest does not present that question.
</p>
<p>In its proposed Model Code of Pre-arraignment Procedure, the American Law Institute has addressed the question and recommends that an officer who is empowered to make an arrest and has probable cause to believe the person to be arrested is on private premises be authorized to demand entry to such premises and thereupon to enter to make an arrest. ALI, Model Code of Pre-arraignment Procedure § 120.6 (1) (1975). In certain cases of necessity, however, notification and demand are not required. § 120.6 (2). Authority to make nighttime arrests on private premises is restricted to arrests with warrants authorizing nighttime execution and to certain cases of necessity. § 120.6 (3). The commentary states that 24 States (and the District of Columbia) authorize forcible entry whenever there is authority to arrest, six whenever the arrest is under a warrant or for a felony, six whenever the arrest is under a warrant, and two whenever the arrest is for a felony. <i>Id.,</i> at 310, 696-697. Of these jurisdictions all but three have prior-notice requirements for entries to make an arrest similar to those <span class="citation no-link">18 U. S. C. § 3109</span> imposes on entries to execute a search warrant. ALI Model Code, <i>supra,</i> at 310-313.</p>
<p>[7]  As Professor Wilgus observed in his article Arrest Without A Warrant, <span class="citation no-link">22 Mich. L. Rev. 541</span>, 549-550 (1924) (footnote omitted), "[i]t was early argued that similar provisions [to the Fourth Amendment of the Constitution] in state constitutions forbade arrests without a warrant; it was ruled otherwise as to arrests by officers and private persons according to the common law."</p>
<p>[8]  Of equal import is the rule recognized by this Court that even in the absence of a federal statute granting or restricting the authority of federal law enforcement officers, "the law of the state where an arrest without warrant takes place determines its validity." <i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#589" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 589</a></span> (1948). Accord, <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#305" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 305</a></span> (1958); <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, 15 n. 5 (1948); <i>Bad Elk</i> v. <i>United States,</i> <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/#535" aria-description="Citation for case: Bad Elk v. United States">177 U. S. 529, 535</a></span> (1900). This rule is consistent with the express statutory authority of United States marshals discussed in the text, as well as with the Act of Sept. 24, 1789, c. 20, § 33, <span class="citation no-link">1 Stat. 91</span>, providing that for any offense against the United States the offender may be arrested by any judge or justice of the United States "agreeably to the usual mode of process against offenders in such state" as he might be found. See <i>United States</i> v. <i>Di Re, supra,</i> at 589 n. 8.</p>
<p>[9]  Act of Feb. 28, 1795, c. 36, § 9, <span class="citation no-link">1 Stat. 425</span>; Act of July 29, 1861, c. 25, § 7, <span class="citation no-link">12 Stat. 282</span>; Rev. Stat. § 788 (1874); Judicial Code of 1948, § 549, <span class="citation no-link">62 Stat. 912</span>.</p>
<p>[10]  Act of June 15, 1935, c. 259, § 2, <span class="citation no-link">49 Stat. 378</span>.</p>
<p>[11]  Section 120.1 of the Model Code provides, in pertinent part:
</p>
<p>"(1) <i>Authority to Arrest Without a Warrant.</i> A law enforcement officer may arrest a person without a warrant if the officer has reasonable cause to believe that such person has committed</p>
<p>"(a) a felony;</p>
<p>"(b) a misdemeanor, and the officer has reasonable cause to believe that such person</p>
<p>"(i) will not be apprehended unless immediately arrested; or</p>
<p>"(ii) may cause injury to himself or others or damage to property unless immediately arrested; or</p>
<p>"(c) a misdemeanor or petty misdemeanor in the officer's presence."</p>
<p>[12]  <i>Id.,</i> at 289 (footnote omitted). The commentary goes on to say with respect to § 120.1:
</p>
<p>"This Section does not require an officer to arrest under a warrant even if a reasonable opportunity to obtain a warrant exists. As to arrests on the street such a requirement would be entirely novel. Moreover the need for it is not urgent, and the subsequent inquiry such a requirement would authorize would be indeterminate and difficult." <i>Id.,</i> at 303 (footnotes omitted).</p>
<p>As the commentary notes, <i>id.,</i> at 289 n. 1, a statute in the State of Georgia is more restrictive of the arrest power than the general standard. <span class="citation no-link">Ga. Code Ann. § 27-207</span> (a) (Supp. 1975). See also <span class="citation no-link">Colo. Rev. Stat. Ann. § 16-3-102</span> (1973), which provides that an arrest warrant should be obtained "when practicable," and Mont. Rev. Codes Ann. § 95-608 (d) (1969) which authorizes a warrantless arrest if "existing circumstances require" it. A North Carolina statute, N. C. Gen. Stat. § 15-41 (1965), similar to the Georgia statute, was replaced in 1975 by a provision permitting warrantless felony arrests on probable cause. N. C. Gen. Stat. § 15A-401 (b) (2) (1975).</p>
<p>[13]  Until 1951, <span class="citation no-link">18 U. S. C. § 3052</span> conditioned the warrantless arrest powers of the agents of the Federal Bureau of Investigation on there being reasonable grounds to believe that the person would escape before a warrant could be obtained. The Act of Jan. 10, 1951, c. 1221, § 1, <span class="citation no-link">64 Stat. 1239</span>, eliminated this condition. The House Report explained the purpose of the amendment, H. R. Rep. No. 3228, 81st Cong., 2d Sess., 1-2 (1950), and the amendment was given effect by the courts in accordance with its terms. Compare <i>United States</i> v. <i>Coplon,</i> <span class="citation" data-id="226125"><a href="/opinion/226125/united-states-v-coplon/#633" aria-description="Citation for case: United States v. Coplon">185 F. 2d 629, 633-636</a></span> (CA2 1950), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./342/920/">342 U. S. 920</a></span> (1952), with <i>Coplon</i> v. <i>United States,</i> 89 U. S. App. D. C. 103, 108-109, <span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/#753" aria-description="Citation for case: Coplon v. United States (Two Cases)">191 F. 2d 749, 753-754</a></span> (1951), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./342/926/">342 U. S. 926</a></span> (1952).</p>
<p>[14]  On the contrary, the inspector making the arrest in this case had arrested Watson in 1971 for mail theft. Those charges were dropped when Watson cooperated with the prosecution. During the ensuing two years he also furnished information to the authorities.</p>
<p>[1]  None of the decisions cited by the Court today squarely faced the issue. In <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span> (1959), for example, the Court declared that <span class="citation no-link">18 U. S. C. § 3052</span>, which authorizes an FBI agent to make a warrantless arrest when he has reasonable grounds to believe that a person has committed a felony, "states the constitutional standard." <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#100" aria-description="Citation for case: Henry v. United States">361 U. S., at 100</a></span>. But that declaration was made without discussion, and the issue actually presented to and addressed by the Court was whether there was in fact probable cause for the arrest in that case. Similarly, <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959), stands only for the validity of a warrantless arrest made with probable cause to believe that the arrestee had committed an offense in the arresting officer's presence. See <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#313" aria-description="Citation for case: Draper v. United States"><i>id.,</i> at 313</a></span>. As this Court had noted in an earlier case, such an arrest presents no danger that an innocent person might be ensnared, since the officer observes both the crime and the culprit with his own eyes; there thus would be no reason to require a warrant in that particular situation even if there might be in others. <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/#705" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699, 705</a></span> (1948). Another case cited by the Court, <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), involved no challenge to an arrest. Nor did <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span> (1960), in which the Court refused to consider petitioner's challenge to his arrest under less than a judicial warrant because of his failure to raise the issue in the lower courts. See <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#230" aria-description="Citation for case: Abel v. United States"><i>id.,</i> at 230-232</a></span>. Finally, in <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963), the Court addressed only the questions of whether there was probable cause for arrest and whether the method of entry for the purpose of arrest was reasonable; no issue arose as to whether a warrant was necessary for either the arrest or the entry.</p>
<p>[2]  Act of May 2, 1792, c. 18, § 9, <span class="citation no-link">1 Stat. 265</span>; see <span class="citation no-link">28 U. S. C. § 570</span>.</p>
<p>[3]  Respondent has cited no other decision, state or federal, in support of the Court of Appeals' result in this case. The Government stated in its petition that the decision below was the first of which it was aware that required a warrant for an arrest in a public place. The Court of Appeals relied upon part of this Court's discussion in <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#480" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 480-481</a></span> (1971), but as other courts have recognized that discussion had nothing to do with warrantless arrests in public places. See, <i>e. g., </i><i>United States</i> v. <i>Miles,</i> <span class="citation" data-id="306113"><a href="/opinion/306113/united-states-v-jerry-edgar-miles-appeal-of-george-kirby/#486" aria-description="Citation for case: United States v. Jerry Edgar Miles Appeal of George Kirby">468 F. 2d 482, 486-487</a></span>, and n. 6 (CA3 1972); <i>United States</i> v. <i>Bazinet,</i> <span class="citation" data-id="304301"><a href="/opinion/304301/the-united-states-v-michael-bazinet-the-united-states-v-george-knox/#987" aria-description="Citation for case: The United States v. Michael Bazinet, the United States...">462 F. 2d 982, 987</a></span> (CA8), cert. denied <i>sub nom. Knox</i> v. <i>United States,</i> <span class="citation" data-id="8982985"><a href="/opinion/8990812/knox-v-united-states/" aria-description="Citation for case: Knox v. United States">409 U. S. 1010</a></span> (1972).</p>
<p>[4]  This Court has not attempted a more precise definition of probable cause than the one in <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#161" aria-description="Citation for case: Carroll v. United States">267 U. S., at 161</a></span>, where the standard was affirmed as "facts and circumstances. . . such as to warrant a man of [reasonable] prudence and caution in believing that the offense has been committed" and, of course, that the person to be arrested was the offender. See generally <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#100" aria-description="Citation for case: Henry v. United States">361 U. S., at 100-102</a></span>. Whatever evidence may be necessary to establish probable cause in a given case, however, it is clear that it never need rise to the level required to prove guilt beyond a reasonable doubt. <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#102" aria-description="Citation for case: Henry v. United States"><i>Id.,</i> at 102</a></span>; <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#311" aria-description="Citation for case: Draper v. United States">358 U. S., at 311-312</a></span>, and n. 4. The different standards for arrest and conviction reflect a recognition of society's valid interest in the earliest detention of suspected criminals that is consistent with the individual's interest in freedom from arbitrary interference with his liberty. See <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span> (1949). But society's equally valid interest in ultimate conviction of the guilty requires the police sometimes to continue their investigation after establishing probable cause to arrest, even if doing so means they have to leave a suspect at large pending such investigation. See generally ALI, A Model Code of Pre-arraignment Procedure § 120.1, Commentary, pp. 289, 292-296 (1975).</p>
<p>[5]  The probable cause to support issuance of an arrest warrant normally would not grow stale as easily as that which supports a warrant to search a particular place for particular objects. This is true because once there is probable cause to believe that someone is a felon the passage of time often will bring new supporting evidence. But in some cases the original grounds supporting the warrant could be disproved by subsequent investigation that at the same time turns up wholly new evidence supporting probable cause on a different theory. In those cases the warrant could be stale because based upon discredited information.</p>
<p>[6]  I do not understand today's decision to suggest any retreat from our longstanding position that such an arrest should receive careful judicial scrutiny if challenged. "An arrest without a warrant bypasses the safeguards provided by an objective determination of probable cause, and substitutes instead the far less reliable procedure of an after-the-event justification for the arrest . . . , too likely to be subtly influenced by the familiar shortcomings of hindsight judgment." <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 96</a></span> (1964).</p>
<p>[7]  Compare <i>Dorman</i> v. <i>United States,</i> 140 U. S. App. D. C. 313, 318-319, <span class="citation" data-id="9456306"><a href="/opinion/293653/harold-b-dorman-v-united-states/#390" aria-description="Citation for case: Harold B. Dorman v. United States">435 F. 2d 385, 390-391</a></span> (1970) (en banc) (warrant required, absent exigent circumstances, for entry into a suspect's home for purpose of arrest), with <i>People</i> v. <i>Eddington,</i> <span class="citation" data-id="1939307"><a href="/opinion/1939307/people-v-eddington/" aria-description="Citation for case: People v. Eddington">23 Mich. App. 210</a></span>, <span class="citation" data-id="1939307"><a href="/opinion/1939307/people-v-eddington/" aria-description="Citation for case: People v. Eddington">178 N. W. 2d 686</a></span> (1970), aff'd, <span class="citation" data-id="9704090"><a href="/opinion/1978640/people-v-eddington/" aria-description="Citation for case: People v. Eddington">387 Mich. 551</a></span>, <span class="citation" data-id="9704090"><a href="/opinion/1978640/people-v-eddington/" aria-description="Citation for case: People v. Eddington">198 N. W. 2d 297</a></span> (1972) (only probable cause to arrest needed to enter suspect's home if there is a reasonable belief that he is there). Compare <i>England</i> v. <i>State,</i> <span class="citation" data-id="2614205"><a href="/opinion/2614205/england-v-state/" aria-description="Citation for case: England v. State">488 P. 2d 1347</a></span> (Okla. Crim. 1971) (search warrant needed to enter residence of third party to arrest suspect), with <i>United States</i> v. <i>Brown,</i> 151 U. S. App. D. C. 365, 369, <span class="citation" data-id="305803"><a href="/opinion/305803/united-states-v-roland-w-brown/#423" aria-description="Citation for case: United States v. Roland W. Brown">467 F. 2d 419, 423</a></span> (1972) (only an arrest warrant, plus reasonable belief that the suspect is present, necessary to support entry onto third party's premises).</p>
<p>[1]  The Court of Appeals did not recognize this independent probable cause to arrest petitioner, perhaps because one of the arresting officers testified that the arrest was made for the earlier, rather than the contemporaneous, offense. App. 23-24. That testimony should not limit the inquiry into contemporaneous probable cause. Where the good faith of the arresting officers is not at issue, and where the crime for which a suspect is arrested and that for which the officers have probable cause are closely related, courts typically use an objective rather than subjective measure of probable cause. <i>Ramirez</i> v. <i>Rodriguez,</i> <span class="citation" data-id="305873"><a href="/opinion/305873/henry-ramirez-v-felix-rodriguez-warden/" aria-description="Citation for case: Henry Ramirez v. Felix Rodriguez, Warden">467 F. 2d 822</a></span> (CA10 1972); <i>United States</i> v. <i>Martinez,</i> <span class="citation" data-id="305071"><a href="/opinion/305071/united-states-v-nestor-martinez/" aria-description="Citation for case: United States v. Nestor Martinez">465 F. 2d 79</a></span> (CA2 1972); <i>United States</i> v. <i>Atkinson,</i> <span class="citation" data-id="9457517"><a href="/opinion/299839/united-states-v-james-william-atkinson-aka-walter-j-atkinson/#838" aria-description="Citation for case: United States v. James William Atkinson, A/K/A Walter J....">450 F. 2d 835, 838</a></span> (CA5 1971). Since the objective facts demonstrably show probable cause as to the contemporaneous offense as well as the earlier offense, Watson's arrest is properly justified by reference to those facts.</p>
<p>[2]  W. Shakespeare, Hamlet, act iii, sc. 1, line 142.</p>
<p>[3]  Nunnery was Elizabethan slang for house of prostitution. 7 Oxford English Dictionary 264 (1933).</p>
<p>[4]  Professor Wilgus has defined felonies at common law as
</p>
<p>"those bootless crimes, prosecuted by an appeal with an offer of trial by battle, the felon's lands to go to his lord or the king, his chattels confiscated, and life and members forfeited, if guilty, and if he fled he became an outlaw . . . ." Wilgus, Arrest Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 541</span>, 569 (1924).</p>
<p>[5]  In the States the most common rule is that any crime punishable by death or imprisonment in the state prison is a felony. See <i>id.,</i> at 571. See also, <i>e. g.,</i> Ark. Stat. Ann. § 41-103 (1964); 22 <span class="citation no-link">Fla. Stat. Ann. § 775.08</span> (Supp. 1975); Ill. Ann. Stat. § 2-7 (Supp. 1975); <span class="citation no-link">Ky. Rev. Stat. Ann. § 431.060</span> (1970); Mass. Gen. Laws Ann., c. 274, § 1 (1970); Okla. Stat. Ann., Tit. 21, § 5 (1958); <span class="citation no-link">Wash. Rev. Code § 9.01.020</span> (1974).</p>
<p>[6]  "In England at the common law the difference in punishment between felonies and misdemeanors was very great. Under our present federal statutes, it is much less important and Congress may exercise a relatively wide discretion in classing particular offenses as felonies or misdemeanors." <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S., at 158</a></span>.</p>
<p>[7]  Indeed, by statute, it was no more than a high misdemeanor wilfully to discharge or attempt to discharge a pistol at or near the King of England. 9 Halsbury's Laws of <span class="citation" data-id="2614205"><a href="/opinion/2614205/england-v-state/#459" aria-description="Citation for case: England v. State">England 459</a></span> (1909). Cf. <span class="citation no-link">18 U. S. C. § 871</span> (felony to make threats against President of United States); § 1751 (felony to assault President of United States).</p>
<p>[8]  This exception was essentially a narrowly drawn exigent-circumstances exception. See <i>Carroll</i> v. <i>United States, supra,</i> at 157.</p>
<p>[9]  For example, under federal law these are some of the commonlaw misdemeanors, or their modern equivalents, now considered felonies: assault, <span class="citation no-link">18 U. S. C. §§ 111-112</span>; assault with intent to commit murder, rape or any other felony, § 113; forging securities of the United States, § 471; bribing voters, § 597; escape, § 751; kidnaping, § 1201; obstruction 

[...TRUNCATED 16711 of 136711 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
