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

## GROUP: _overhaul2/lake/cases/Missouri v. Seibert.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Missouri v. Seibert"
type: case
citation: "542 U.S. 600 (2004)"
parallel_cite: "124 S. Ct. 2601; 159 L. Ed. 2d 643"
neutral_cite: 2004 U.S. LEXIS 4578
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-06-28
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2004-06-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Missouri v. Seibert
  varies_by_point: false
  scope_note: "Plurality opinion; Justice Kennedy's concurrence in the judgment is generally treated as controlling."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/137002/missouri-v-seibert/"
  cluster_id: 137002
  opinion_id: 137002
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Oregon v. Elstad]]", "[[Miranda v. Arizona]]", "[[Dickerson v. United States]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "two-step", "question-first", "waiver"]
holding: "A deliberate \"question-first, warn-later\" two-step interrogation is invalid."
lake:
  record_id: Missouri v. Seibert
  status: verified
  projected_at: 2026-07-06
---

# Missouri v. Seibert

*542 U.S. 600 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Following a deliberate department protocol, officers interrogated Seibert without *[[Miranda v. Arizona|Miranda]]* warnings until she confessed to involvement in a fire that killed a man, then gave her the warnings and led her to repeat the same confession. Both statements were obtained in a single, continuous interrogation.

## Issue
Whether a confession repeated after *[[Miranda v. Arizona|Miranda]]* warnings is admissible when officers deliberately used a two-step "question-first, warn-later" interrogation technique.

## Rule
No (plurality). "Because this midstream recitation of warnings after interrogation and unwarned confession could not effectively comply with *Miranda*'s constitutional requirement, we hold that a statement repeated after a warning in such circumstances is inadmissible." — 542 U.S. at 604 (plurality opinion). ^pin-604

Justice Kennedy, concurring in the judgment on the narrower ground generally treated as controlling, would suppress the postwarning statement where a two-step interrogation was used deliberately to undermine *[[Miranda v. Arizona|Miranda]]*, unless curative measures were taken.

## Application
The officers here followed a deliberate protocol of questioning Seibert until she confessed and only then administering the warnings before having her repeat the confession. Because the midstream warnings came only after she had already confessed under unwarned interrogation, they could not function effectively, and her repeated, postwarning confession was inadmissible.

## Conclusion
Affirmed; the postwarning statement was suppressed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (plurality; Kennedy's concurrence controlling).
- No negative treatment. *Seibert* is distinguished from the good-faith, non-deliberate two-step sequence approved in [[Oregon v. Elstad]].

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *Missouri v. Seibert*, 542 U.S. 600 (2004) — https://www.courtlistener.com/opinion/137002/missouri-v-seibert/ — pinpoint: 604 (plurality opinion).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "fc3f6b3c9d6e53e8", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Missouri v. Seibert"}, "payload": {"all": [{"cite": "542 U.S. 600", "page": "600", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "542"}, {"cite": "124 S. Ct. 2601", "page": "2601", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "124"}, {"cite": "159 L. Ed. 2d 643", "page": "643", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "159"}, {"cite": "2004 U.S. LEXIS 4578", "page": "4578", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2004"}], "display": "542 U.S. 600", "official": {"cite": "542 U.S. 600", "page": "600", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "542"}, "official_selection_present": true, "record_id": "Missouri v. Seibert"}}
{"assertion_id": "69a5215735f6c6e2", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-604", "record_id": "Missouri v. Seibert"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-604", "pinpoint_status": "slip-only", "quote": "interrogation technique. ## Rule No (plurality).", "quote_fidelity": "mismatch", "record_id": "Missouri v. Seibert", "star_marker": null}}
{"assertion_id": "ae971fa7744f6928", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Missouri v. Seibert"}, "payload": {"as_of_content": "2004-06-28", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Missouri v. Seibert", "scope_note": "Plurality opinion; Justice Kennedy's concurrence in the judgment is generally treated as controlling.", "varies_by_point": false}}
```

### lake record — Missouri v. Seibert

```json
{
  "schema_version": "s2.v1",
  "record_id": "Missouri v. Seibert",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Missouri v. Seibert",
    "case_name_short": "Seibert",
    "case_name_full": "Missouri v. Seibert",
    "input_case_name": "Missouri v. Seibert",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-06-28",
    "year": 2004,
    "docket": null,
    "cluster_id": 137002,
    "lead_opinion_id": 137002,
    "sibling_ids": [
      137002,
      9434682,
      9434683,
      9434684,
      9434685
    ],
    "absolute_url": "/opinion/137002/missouri-v-seibert/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "542 U.S. 600",
      "volume": "542",
      "reporter": "U.S.",
      "page": "600",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "124 S. Ct. 2601",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2601",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "159 L. Ed. 2d 643",
        "volume": "159",
        "reporter": "L. Ed. 2d",
        "page": "643",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 4578",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "4578",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "542 U.S. 600",
        "volume": "542",
        "reporter": "U.S.",
        "page": "600",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 2601",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2601",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "159 L. Ed. 2d 643",
        "volume": "159",
        "reporter": "L. Ed. 2d",
        "page": "643",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 4578",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "4578",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "542 U.S. 600",
    "official_selection": {
      "court_class": "scotus",
      "selected": "542 U.S. 600",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-604",
      "page": null,
      "quote": "interrogation technique. ## Rule No (plurality).",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2004-06-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Missouri v. Seibert",
    "varies_by_point": false,
    "scope_note": "Plurality opinion; Justice Kennedy's concurrence in the judgment is generally treated as controlling.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Yaeger",
          "cluster_id": 10134256,
          "cite": [
            "311 Or. App. 626",
            "492 P.3d 668"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chhay Lim",
          "cluster_id": 4522500,
          "cite": [
            "897 F.3d 673"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Abbott",
          "cluster_id": 10366844,
          "cite": [
            "303 Ga. 297"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kasey A. Smith",
          "cluster_id": 4442984,
          "cite": [
            "162 Idaho 878",
            "406 P.3d 890"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Phillips v. People",
          "cluster_id": 4636609,
          "cite": [
            "2019 CO 72",
            "443 P.3d 1016"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
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
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
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
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lam Thanh Nguyen",
          "cluster_id": 2827119,
          "cite": [
            "61 Cal. 4th 1015",
            "354 P.3d 90",
            "191 Cal. Rptr. 3d 182",
            "2015 Cal. LEXIS 5407"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hale",
          "cluster_id": 6897940,
          "cite": [
            "119 Ohio St. 3d 118",
            "892 N.E.2d 864"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
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
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Scott",
          "cluster_id": 844257,
          "cite": [
            "257 P.3d 703",
            "52 Cal. 4th 452",
            "129 Cal. Rptr. 3d 91",
            "2011 Cal. LEXIS 8086"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. San Nicolas",
          "cluster_id": 2507905,
          "cite": [
            "101 P.3d 509",
            "21 Cal. Rptr. 3d 612",
            "34 Cal. 4th 614",
            "2004 Daily Journal DAR 14410",
            "2004 Cal. Daily Op. Serv. 10643",
            "2004 Cal. LEXIS 11655"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bobby v. Dixon",
          "cluster_id": 616807,
          "cite": [
            "181 L. Ed. 2d 328",
            "132 S. Ct. 26",
            "565 U.S. 23",
            "2011 U.S. LEXIS 7926"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Meier Jason Brown",
          "cluster_id": 77264,
          "cite": [
            "441 F.3d 1330",
            "69 Fed. R. Serv. 738",
            "2006 U.S. App. LEXIS 6052",
            "2006 WL 587875"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Eichinger",
          "cluster_id": 2091853,
          "cite": [
            "915 A.2d 1122",
            "591 Pa. 1",
            "2007 Pa. LEXIS 357"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Paulman",
          "cluster_id": 2021621,
          "cite": [
            "833 N.E.2d 239",
            "5 N.Y.3d 122",
            "800 N.Y.S.2d 96",
            "2005 NY Slip Op 5452",
            "2005 N.Y. LEXIS 1459"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tashiri Wayne Williams",
          "cluster_id": 793121,
          "cite": [
            "435 F.3d 1148",
            "2006 U.S. App. LEXIS 2235",
            "2006 WL 213852"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lopez",
          "cluster_id": 2060903,
          "cite": [
            "892 N.E.2d 1047",
            "229 Ill. 2d 322",
            "323 Ill. Dec. 55",
            "2008 Ill. LEXIS 630"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Unkart, Rodney Gale",
          "cluster_id": 2948085,
          "cite": [
            "400 S.W.3d 94",
            "2013 WL 2419497",
            "2013 Tex. Crim. App. LEXIS 818"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hoffner v. Bradshaw",
          "cluster_id": 175794,
          "cite": [
            "622 F.3d 487",
            "2010 U.S. App. LEXIS 19747",
            "2010 WL 3724790"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Blank",
          "cluster_id": 1620393,
          "cite": [
            "955 So. 2d 90",
            "2007 WL 1108842"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Hillary Lee Tyler",
          "cluster_id": 2812907,
          "cite": [
            "867 N.W.2d 136",
            "2015 Iowa Sup. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
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
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Antonio Rodriguez-Preciado, AKA Tony Rodriguez-Preciado",
          "cluster_id": 789441,
          "cite": [
            "399 F.3d 1118",
            "2005 U.S. App. LEXIS 3634",
            "2005 WL 502860"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Antwion Thompson v. D. Runnel",
          "cluster_id": 815924,
          "cite": [
            "705 F.3d 1089",
            "2013 WL 263909",
            "2013 U.S. App. LEXIS 1585"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stanley Street",
          "cluster_id": 77537,
          "cite": [
            "472 F.3d 1298",
            "2006 WL 3734533"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicole Harris v. Sheryl Thompson",
          "cluster_id": 810477,
          "cite": [
            "698 F.3d 609",
            "2012 WL 4944325",
            "2012 U.S. App. LEXIS 21727"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Knapp",
          "cluster_id": 1713730,
          "cite": [
            "2005 WI 127",
            "700 N.W.2d 899",
            "285 Wis. 2d 86",
            "2005 Wisc. LEXIS 395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Dupree",
          "cluster_id": 3192634,
          "cite": [
            "304 Kan. 43",
            "371 P.3d 862",
            "2016 WL 1391917",
            "2016 Kan. LEXIS 154"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(137002 OR 9434682 OR 9434683 OR 9434684 OR 9434685) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDQzNDg0ODAwMDAwJnM9MzAwNTU4NCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28137002+OR+9434682+OR+9434683+OR+9434684+OR+9434685%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 4,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      },
      "lane2_top_cited": {
        "query": "cites:(137002 OR 9434682 OR 9434683 OR 9434684 OR 9434685)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05OSZzPTc5ODA2MyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28137002+OR+9434682+OR+9434683+OR+9434684+OR+9434685%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(137002 OR 9434682 OR 9434683 OR 9434684 OR 9434685)",
        "reviewed": 42,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 42,
        "triage_read": 0,
        "triage_snippet_classified": 42
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(137002 OR 9434682 OR 9434683 OR 9434684 OR 9434685)",
    "indexed_citing_opinions": 863,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 137002,
        "count": 742,
        "count_source": "search"
      },
      {
        "opinion_id": 9434682,
        "count": 130,
        "count_source": "search"
      },
      {
        "opinion_id": 9434683,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434684,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434685,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1541,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/missouri-v-seibert.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4OTUxNTMmcz0xMDU4MTUwNyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28137002+OR+9434682+OR+9434683+OR+9434684+OR+9434685%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 137002,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 107577,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 108429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 110556,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 110760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 111779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 112322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 117843,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 118380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 127927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 198872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 528515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 575188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 583447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 766929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 775079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 1173989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 1378981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 1890935,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 2499246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 2588587,
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
    "date_created": "2026-07-05T14:17:00Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:17:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:17:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:21:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:17:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Missouri v. Seibert

```
<div>
<center><b><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">542 U.S. 600</a></span> (2004)</b></center>
<center><h1>MISSOURI<br>
v.<br>
SEIBERT.</h1></center>
<center>No. 02-1371.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 9, 2003.</center>
<center>Decided June 28, 2004.</center>
CERTIORARI TO THE SUPREME COURT OF MISSOURI.
<p><span class="star-pagination">*601</span> <span class="star-pagination">*602</span> <span class="star-pagination">*603</span> SOUTER, J., announced the judgment of the Court and delivered an opinion, in which STEVENS, GINSBURG, and BREYER, JJ., joined. BREYER, J., filed a concurring opinion, <i>post,</i> p. 617. KENNEDY, J., filed an opinion concurring in the judgment, <i>post,</i> p. 618. O'CONNOR, J., filed a dissenting opinion, in which REHNQUIST, C. J., and SCALIA and THOMAS, JJ., joined, <i>post,</i> p. 622.</p>
<p><i>Karen K. Mitchell,</i> Chief Deputy Attorney General of Missouri, argued the cause for petitioner. With her on the briefs were <i>Jeremiah W. (Jay) Nixon,</i> Attorney General, <i>James R. Layton,</i> State Solicitor, and <i>Shaun J. Mackelprang</i> and <i>Karen P. Hess,</i> Assistant Attorneys General.</p>
<p><i>Irving L. Gornstein</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Olson, Acting Assistant Attorney General Wray, Deputy Solicitor General Dreeben,</i> and <i>Jonathan L. Marcus.</i></p>
<p><i>Amy M. Bartholow</i> argued the cause and filed a brief for respondent.<sup>[*]</sup></p>
<p><span class="star-pagination">*604</span> JUSTICE SOUTER announced the judgment of the Court and delivered an opinion, in which JUSTICE STEVENS, JUSTICE GINSBURG, and JUSTICE BREYER join.</p>
<p>This case tests a police protocol for custodial interrogation that calls for giving no warnings of the rights to silence and counsel until interrogation has produced a confession. Although such a statement is generally inadmissible, since taken in violation of <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), the interrogating officer follows it with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and then leads the suspect to cover the same ground a second time. The question here is the admissibility of the repeated statement. Because this midstream recitation of warnings after interrogation and unwarned confession could not effectively comply with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s constitutional requirement, we hold that a statement repeated after a warning in such circumstances is inadmissible.</p>
<p></p>
<h2>I</h2>
<p>Respondent Patrice Seibert's 12-year-old son Jonathan had cerebral palsy, and when he died in his sleep she feared charges of neglect because of bedsores on his body. In her presence, two of her teenage sons and two of their friends devised a plan to conceal the facts surrounding Jonathan's death by incinerating his body in the course of burning the family's mobile home, in which they planned to leave Donald Rector, a mentally ill teenager living with the family, to avoid any appearance that Jonathan had been unattended. Seibert's son Darian and a friend set the fire, and Donald died.</p>
<p>Five days later, the police awakened Seibert at 3 a.m. at a hospital where Darian was being treated for burns. In arresting her, Officer Kevin Clinton followed instructions from Rolla, Missouri, Officer Richard Hanrahan that he refrain from giving <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. After Seibert had been taken to the police station and left alone in an interview room for 15 to 20 minutes, Officer Hanrahan questioned her <span class="star-pagination">*605</span> without <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings for 30 to 40 minutes, squeezing her arm and repeating "Donald was also to die in his sleep." App. 59 (internal quotation marks omitted). After Seibert finally admitted she knew Donald was meant to die in the fire, she was given a 20-minute coffee and cigarette break. Officer Hanrahan then turned on a tape recorder, gave Seibert the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, and obtained a signed waiver of rights from her. He resumed the questioning with "Ok, 'trice, we've been talking for a little while about what happened on Wednesday the twelfth, haven't we?," App. 66, and confronted her with her prewarning statements:</p>
<blockquote>Hanrahan: "Now, in discussion you told us, you told us that there was a[n] understanding about Donald."</blockquote>
<blockquote>Seibert: "Yes."</blockquote>
<blockquote>Hanrahan: "Did that take place earlier that morning?"</blockquote>
<blockquote>Seibert: "Yes."</blockquote>
<blockquote>Hanrahan: "And what was the understanding about Donald?"</blockquote>
<blockquote>Seibert: "If they could get him out of the trailer, to take him out of the trailer."</blockquote>
<blockquote>Hanrahan: "And if they couldn't?"</blockquote>
<blockquote>Seibert: "I, I never even thought about it. I just figured they would."</blockquote>
<blockquote>Hanrahan: "`Trice, didn't you tell me that he was supposed to die in his sleep?"</blockquote>
<blockquote>Seibert: "If that would happen, 'cause he was on that new medicine, you know. . . ."</blockquote>
<blockquote>Hanrahan: "The Prozac? And it makes him sleepy. So he was supposed to die in his sleep?"</blockquote>
<blockquote>Seibert: "Yes." <i>Id.,</i> at 70.</blockquote>
<p>After being charged with first-degree murder for her role in Donald's death, Seibert sought to exclude both her prewarning and postwarning statements. At the suppression hearing, Officer Hanrahan testified that he made a "conscious <span class="star-pagination">*606</span> decision" to withhold <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, thus resorting to an interrogation technique he had been taught: question first, then give the warnings, and then repeat the question "until I get the answer that she's already provided once." App. 31-34. He acknowledged that Seibert's ultimate statement was "largely a repeat of information . . . obtained" prior to the warning. <i>Id.,</i> at 30.</p>
<p>The trial court suppressed the prewarning statement but admitted the responses given after the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> recitation. A jury convicted Seibert of second-degree murder. On appeal, the Missouri Court of Appeals affirmed, treating this case as indistinguishable from <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985). No. 23729, <span class="citation no-link">2002 WL 114804</span> (Jan. 30, 2002) (not released for publication).</p>
<p>The Supreme Court of Missouri reversed, holding that "[i]n the circumstances here, where the interrogation was nearly continuous, . . . the second statement, clearly the product of the invalid first statement, should have been suppressed." <span class="citation" data-id="9692268"><a href="/opinion/1890935/state-v-seibert/#701" aria-description="Citation for case: State v. Seibert">93 S. W. 3d 700, 701</a></span> (2002) (en banc). The court distinguished <i>Elstad</i> on the ground that warnings had not intentionally been withheld there, <span class="citation" data-id="9692268"><a href="/opinion/1890935/state-v-seibert/#704" aria-description="Citation for case: State v. Seibert">93 S. W. 3d, at 704</a></span>, and reasoned that "Officer Hanrahan's intentional omission of a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning was intended to deprive Seibert of the opportunity knowingly and intelligently to waive her <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights," <i>id.,</i> at 706. Since there were "no circumstances that would seem to dispel the effect of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation," the court held that the postwarning confession was involuntary and therefore inadmissible. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> To allow the police to achieve an "end run" around <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the court explained, would encourage <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violations and diminish <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s role in protecting the privilege against self-incrimination. <span class="citation" data-id="9692268"><a href="/opinion/1890935/state-v-seibert/#706" aria-description="Citation for case: State v. Seibert">93 S. W. 3d, at 706-707</a></span>. Three judges dissented, taking the view that <i>Elstad</i> applied even though the police intentionally withheld <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings before the initial statement, and believing that "Seibert's unwarned responses to Officer Hanrahan's questioning did not prevent <span class="star-pagination">*607</span> her from waiving her rights and confessing." <span class="citation" data-id="9692268"><a href="/opinion/1890935/state-v-seibert/#708" aria-description="Citation for case: State v. Seibert">93 S. W. 3d, at 708</a></span> (opinion of Benton, J.).</p>
<p>We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./538/1031/">538 U. S. 1031</a></span> (2003), to resolve a split in the Courts of Appeals. Compare <i>United States</i> v. <i>Gale,</i> <span class="citation" data-id="575188"><a href="/opinion/575188/united-states-v-theodore-k-gale/#1418" aria-description="Citation for case: United States v. Theodore K. Gale">952 F. 2d 1412, 1418</a></span> (CADC 1992) (while "deliberate `end run' around <i>Miranda</i>" would provide cause for suppression, case involved no conduct of that order); <i>United States</i> v. <i>Carter,</i> <span class="citation" data-id="9479453"><a href="/opinion/528515/united-states-v-terry-gene-carter/#373" aria-description="Citation for case: United States v. Terry Gene Carter">884 F. 2d 368, 373</a></span> (CA8 1989) ("<i>Elstad</i> did not go so far as to fashion a rule permitting this sort of end run around <i>Miranda</i>"), with <i>United States</i> v. <i>Orso,</i> <span class="citation" data-id="9494408"><a href="/opinion/775079/united-states-v-jody-myesha-orso/#1034" aria-description="Citation for case: United States v. Jody Myesha Orso">266 F. 3d 1030, 1034-1039</a></span> (CA9 2001) (en banc) (rejecting argument that "tainted fruit" analysis applies because deliberate withholding of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings constitutes an "improper tactic"); <i>United States</i> v. <i>Esquilin,</i> <span class="citation" data-id="198872"><a href="/opinion/198872/united-states-v-esquilin/#319" aria-description="Citation for case: United States v. Esquilin">208 F. 3d 315, 319-321</a></span> (CA1 2000) (similar). We now affirm.</p>
<p></p>
<h2>II</h2>
<p>"In criminal trials, in the courts of the United States, wherever a question arises whether a confession is incompetent because not voluntary, the issue is controlled by that portion of the Fifth Amendment . . . commanding that no person `shall be compelled in any criminal case to be a witness against himself.'" <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#542" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 542</a></span> (1897). A parallel rule governing the admissibility of confessions in state courts emerged from the Due Process Clause of the Fourteenth Amendment, see, <i>e. g., </i><i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936), which governed state cases until we concluded in <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#8" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 8</a></span> (1964), that "[t]he Fourteenth Amendment secures against state invasion the same privilege that the Fifth Amendment guarantees against federal infringementthe right of a person to remain silent unless he chooses to speak in the unfettered exercise of his own will, and to suffer no penalty . . . for such silence." In unifying the Fifth and Fourteenth Amendment voluntariness tests, <i><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Malloy</a></span></i> "made clear what had already become apparentthat the substantive and procedural safeguards <span class="star-pagination">*608</span> surrounding admissibility of confessions in state cases had become exceedingly exacting, reflecting all the policies embedded in the privilege" against self-incrimination. <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#464" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 464</a></span>.</p>
<p>In <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> we explained that the "voluntariness doctrine in the state cases . . . encompasses all interrogation practices which are likely to exert such pressure upon an individual as to disable him from making a free and rational choice," <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#464" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 464-465</a></span>. We appreciated the difficulty of judicial enquiry <i>post hoc</i> into the circumstances of a police interrogation, <i>Dickerson</i> v. <i>United States,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#444" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428, 444</a></span> (2000), and recognized that "the coercion inherent in custodial interrogation blurs the line between voluntary and involuntary statements, and thus heightens the risk" that the privilege against self-incrimination will not be observed, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#435" aria-description="Citation for case: Dickerson v. United States"><i>id.,</i> at 435</a></span>. Hence our concern that the "traditional totality-of-the-circumstances" test posed an "unacceptably great" risk that involuntary custodial confessions would escape detection. <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#442" aria-description="Citation for case: Dickerson v. United States"><i>Id.,</i> at 442</a></span>.</p>
<p>Accordingly, "to reduce the risk of a coerced confession and to implement the Self-Incrimination Clause," <i>Chavez</i> v. <i>Martinez,</i> <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#790" aria-description="Citation for case: Chavez v. Martinez">538 U. S. 760, 790</a></span> (2003) (KENNEDY, J., concurring in part and dissenting in part), this Court in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> concluded that "the accused must be adequately and effectively apprised of his rights and the exercise of those rights must be fully honored," <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 467</a></span>. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> conditioned the admissibility at trial of any custodial confession on warning a suspect of his rights: failure to give the prescribed warnings and obtain a waiver of rights before custodial questioning generally requires exclusion of any statements obtained.<sup>[1]</sup> Conversely, giving the warnings and getting a <span class="star-pagination">*609</span> waiver has generally produced a virtual ticket of admissibility; maintaining that a statement is involuntary even though given after warnings and voluntary waiver of rights requires unusual stamina, and litigation over voluntariness tends to end with the finding of a valid waiver. See <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#433" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 433, n. 20</a></span> (1984) ("[C]ases in which a defendant can make a colorable argument that a self-incriminating statement was `compelled' despite the fact that the law enforcement authorities adhered to the dictates of <i>Miranda</i> are rare"). To point out the obvious, this common consequence would not be common at all were it not that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are customarily given under circumstances allowing for a real choice between talking and remaining silent.</p>
<p></p>
<h2>III</h2>
<p>There are those, of course, who preferred the old way of doing things, giving no warnings and litigating the voluntariness of any statement in nearly every instance. In the aftermath of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> Congress even passed a statute seeking to restore that old regime, <span class="citation no-link">18 U. S. C. § 3501</span>, although the Act lay dormant for years until finally invoked and challenged in <i>Dickerson</i> v. <i>United States, supra</i><i>. Dickerson</i> reaffirmed <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and held that its constitutional character prevailed against the statute.</p>
<p>The technique of interrogating in successive, unwarned and warned phases raises a new challenge to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> Although we have no statistics on the frequency of this practice, it is not confined to Rolla, Missouri. An officer of that police department testified that the strategy of withholding <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings until after interrogating and drawing out a confession was promoted not only by his own department, but by a national police training organization and other departments in which he had worked. App. 31-32. Consistently with the officer's testimony, the Police Law Institute, for example, instructs that "officers may conduct a two-stage interrogation. . . . At any point during the pre-<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> interrogation, <span class="star-pagination">*610</span> usually after arrestees have confessed, officers may then read the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and ask for a waiver. If the arrestees waive their <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, officers will be able to repeat any <i>subsequent</i> incriminating statements later in court." Police Law Institute, Illinois Police Law Manual 83 (Jan. 2001-Dec. 2003) (available in Clerk of Court's case file) (hereinafter Police Law Manual) (emphasis in original).<sup>[2]</sup><span class="star-pagination">*611</span> The upshot of all this advice is a question-first practice of some popularity, as one can see from the reported cases describing its use, sometimes in obedience to departmental policy.<sup>[3]</sup></p>
<p></p>
<h2>IV</h2>
<p>When a confession so obtained is offered and challenged, attention must be paid to the conflicting objects of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and question-first. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> addressed "interrogation practices . . . likely . . . to disable [an individual] from making a free and rational choice" about speaking, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#464" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 464-465</a></span>, and held that a suspect must be "adequately and effectively" advised of the choice the Constitution guarantees, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 467</a></span>. The object of question-first is to render <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings ineffective by waiting for a particularly opportune time to give them, after the suspect has already confessed.</p>
<p>Just as "no talismanic incantation [is] required to satisfy [<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span>'s] strictures," <i>California</i> v. <i>Prysock,</i> <span class="citation" data-id="9428478"><a href="/opinion/110556/california-v-prysock/#359" aria-description="Citation for case: California v. Prysock">453 U. S. 355, 359</a></span> (1981) <i>(per curiam)</i><i>,</i> it would be absurd to think that mere recitation of the litany suffices to satisfy <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in every conceivable circumstance. "The inquiry is simply whether the warnings reasonably `conve[y] to [a suspect] his rights as required by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i>'" <i>Duckworth</i> v. <i>Eagan,</i> <span class="citation" data-id="9431819"><a href="/opinion/112322/duckworth-v-eagan/#203" aria-description="Citation for case: Duckworth v. Eagan">492 U. S. 195, 203</a></span> (1989) (quoting <span class="citation" data-id="9428478"><a href="/opinion/110556/california-v-prysock/#361" aria-description="Citation for case: California v. Prysock"><i>Prysock, supra,</i> at 361</a></span>). The threshold issue when interrogators question first and warn later is thus whether it would be reasonable to find that in these circumstances the warnings could function "effectively" <span class="star-pagination">*612</span> as <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires. Could the warnings effectively advise the suspect that he had a real choice about giving an admissible statement at that juncture? Could they reasonably convey that he could choose to stop talking even if he had talked earlier? For unless the warnings could place a suspect who has just been interrogated in a position to make such an informed choice, there is no practical justification for accepting the formal warnings as compliance with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> or for treating the second stage of interrogation as distinct from the first, unwarned and inadmissible segment.<sup>[4]</sup></p>
<p>There is no doubt about the answer that proponents of question-first give to this question about the effectiveness of <span class="star-pagination">*613</span> warnings given only after successful interrogation, and we think their answer is correct. By any objective measure, applied to circumstances exemplified here, it is likely that if the interrogators employ the technique of withholding warnings until after interrogation succeeds in eliciting a confession, the warnings will be ineffective in preparing the suspect for successive interrogation, close in time and similar in content. After all, the reason that question-first is catching on is as obvious as its manifest purpose, which is to get a confession the suspect would not make if he understood his rights at the outset; the sensible underlying assumption is that with one confession in hand before the warnings, the interrogator can count on getting its duplicate, with trifling additional trouble. Upon hearing warnings only in the aftermath of interrogation and just after making a confession, a suspect would hardly think he had a genuine right to remain silent, let alone persist in so believing once the police began to lead him over the same ground again.<sup>[5]</sup> A more likely reaction on a suspect's part would be perplexity about the reason for discussing rights at that point, bewilderment being an unpromising frame of mind for knowledgeable decision. What is worse, telling a suspect that "anything you say can and will be used against you," without expressly excepting the statement just given, could lead to an entirely reasonable inference that what he has just said will be used, with subsequent silence being of no avail. Thus, when <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are inserted in the midst of coordinated and continuing interrogation, they are likely to mislead and "depriv[e] <span class="star-pagination">*614</span> a defendant of knowledge essential to his ability to understand the nature of his rights and the consequences of abandoning them." <i>Moran</i> v. <i>Burbine,</i> <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#424" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 424</a></span> (1986). By the same token, it would ordinarily be unrealistic to treat two spates of integrated and proximately conducted questioning as independent interrogations subject to independent evaluation simply because <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings formally punctuate them in the middle.</p>
<p></p>
<h2>V</h2>
<p>Missouri argues that a confession repeated at the end of an interrogation sequence envisioned in a question-first strategy is admissible on the authority of <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), but the argument disfigures that case. In <i>Elstad,</i> the police went to the young suspect's house to take him into custody on a charge of burglary. Before the arrest, one officer spoke with the suspect's mother, while the other one joined the suspect in a "brief stop in the living room," <i>id.,</i> at 315, where the officer said he "felt" the young man was involved in a burglary, <i>id.,</i> at 301 (internal quotation marks omitted). The suspect acknowledged he had been at the scene. <i>Ibid.</i> This Court noted that the pause in the living room "was not to interrogate the suspect but to notify his mother of the reason for his arrest," <i>id.,</i> at 315, and described the incident as having "none of the earmarks of coercion," <i>id.,</i> at 316. The Court, indeed, took care to mention that the officer's initial failure to warn was an "oversight" that "may have been the result of confusion as to whether the brief exchange qualified as `custodial interrogation' or . . . may simply have reflected . . . reluctance to initiate an alarming police procedure before [an officer] had spoken with respondent's mother." <i>Id.,</i> at 315-316. At the outset of a later and systematic station house interrogation going well beyond the scope of the laconic prior admission, the suspect was given <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and made a full confession. <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#301" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 301, 314-315</a></span>. In holding the <span class="star-pagination">*615</span> second statement admissible and voluntary, <i>Elstad</i> rejected the "cat out of the bag" theory that any short, earlier admission, obtained in arguably innocent neglect of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> determined the character of the later, warned confession, <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#311" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 311-314</a></span>; on the facts of that case, the Court thought any causal connection between the first and second responses to the police was "speculative and attenuated," <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#313" aria-description="Citation for case: Oregon v. Elstad"><i>id.,</i> at 313</a></span>. Although the <i>Elstad</i> Court expressed no explicit conclusion about either officer's state of mind, it is fair to read <i>Elstad</i> as treating the living room conversation as a good-faith <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> mistake, not only open to correction by careful warnings before systematic questioning in that particular case, but posing no threat to warn-first practice generally. See <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#309" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 309</a></span> (characterizing the officers' omission of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings as "a simple failure to administer the warnings, unaccompanied by any actual coercion or other circumstances calculated to undermine the suspect's ability to exercise his free will"); <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#318" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 318, n. 5</a></span> (Justice Brennan's concern in dissent that <i>Elstad</i> would invite question-first practice "distorts the reasoning and holding of our decision, but, worse, invites trial courts and prosecutors to do the same").</p>
<p>The contrast between <i>Elstad</i> and this case reveals a series of relevant facts that bear on whether <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings delivered midstream could be effective enough to accomplish their object: the completeness and detail of the questions and answers in the first round of interrogation, the overlapping content of the two statements, the timing and setting of the first and the second, the continuity of police personnel, and the degree to which the interrogator's questions treated the second round as continuous with the first. In <i>Elstad,</i> it was not unreasonable to see the occasion for questioning at the station house as presenting a markedly different experience from the short conversation at home; since a reasonable person in the suspect's shoes could have seen the station house questioning as a new and distinct experience, the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> <span class="star-pagination">*616</span> warnings could have made sense as presenting a genuine choice whether to follow up on the earlier admission.</p>
<p>At the opposite extreme are the facts here, which by any objective measure reveal a police strategy adapted to undermine the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings.<sup>[6]</sup> The unwarned interrogation was conducted in the station house, and the questioning was systematic, exhaustive, and managed with psychological skill. When the police were finished there was little, if anything, of incriminating potential left unsaid. The warned phase of questioning proceeded after a pause of only 15 to 20 minutes, in the same place as the unwarned segment. When the same officer who had conducted the first phase recited the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, he said nothing to counter the probable misimpression that the advice that anything Seibert said could be used against her also applied to the details of the inculpatory statement previously elicited. In particular, the police did not advise that her prior statement could not be used.<sup>[7]</sup> Nothing was said or done to dispel the oddity of warning about legal rights to silence and counsel right after the police had led her through a systematic interrogation, and any uncertainty on her part about a right to stop talking about matters previously discussed would only have been aggravated by the way Officer Hanrahan set the scene by saying "we've been talking for a little while about what happened on Wednesday the twelfth, haven't we?" App. 66. The impression that the further questioning was a mere continuation of the earlier questions and responses was fostered by references back to the confession already given. It <span class="star-pagination">*617</span> would have been reasonable to regard the two sessions as parts of a continuum, in which it would have been unnatural to refuse to repeat at the second stage what had been said before. These circumstances must be seen as challenging the comprehensibility and efficacy of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings to the point that a reasonable person in the suspect's shoes would not have understood them to convey a message that she retained a choice about continuing to talk.<sup>[8]</sup></p>
<p></p>
<h2>VI</h2>
<p>Strategists dedicated to draining the substance out of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> cannot accomplish by training instructions what <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span></i> held Congress could not do by statute. Because the question-first tactic effectively threatens to thwart <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s purpose of reducing the risk that a coerced confession would be admitted, and because the facts here do not reasonably support a conclusion that the warnings given could have served their purpose, Seibert's postwarning statements are inadmissible. The judgment of the Supreme Court of Missouri is affirmed.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE BREYER, concurring.</p>
<p>In my view, the following simple rule should apply to the two-stage interrogation technique: Courts should exclude the "fruits" of the initial unwarned questioning unless the failure to warn was in good faith. Cf. <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#309" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 309, 318, n. 5</a></span> (1985); <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U. S. 897</a></span> (1984). I believe this is a sound and workable approach to the problem this case presents. Prosecutors and judges have long understood how to apply the "fruits" approach, which they use in other areas of law. See <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963). And in the workaday <span class="star-pagination">*618</span> world of criminal law enforcement the administrative simplicity of the familiar has significant advantages over a more complex exclusionary rule. Cf. <i>post,</i> at 628-629 (O'CONNOR, J., dissenting).</p>
<p>I believe the plurality's approach in practice will function as a "fruits" test. The truly "effective" <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings on which the plurality insists, <i>ante,</i> at 615, will occur only when certain circumstances  a lapse in time, a change in location or interrogating officer, or a shift in the focus of the questioning  intervene between the unwarned questioning and any postwarning statement. Cf. <i>Taylor</i> v. <i>Alabama,</i> <span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/#690" aria-description="Citation for case: Taylor v. Alabama">457 U. S. 687, 690</a></span> (1982) (evidence obtained subsequent to a constitutional violation must be suppressed as "fruit of the poisonous tree" unless "intervening events break the causal connection").</p>
<p>I consequently join the plurality's opinion in full. I also agree with JUSTICE KENNEDY'S opinion insofar as it is consistent with this approach and makes clear that a good-faith exception applies. See <i>post,</i> at 622 (opinion concurring in judgment).</p>
<p>JUSTICE KENNEDY, concurring in the judgment.</p>
<p>The interrogation technique used in this case is designed to circumvent <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). It undermines the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning and obscures its meaning. The plurality opinion is correct to conclude that statements obtained through the use of this technique are inadmissible. Although I agree with much in the careful and convincing opinion for the plurality, my approach does differ in some respects, requiring this separate statement.</p>
<p>The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule has become an important and accepted element of the criminal justice system. See <i>Dickerson</i> v. <i>United States,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428</a></span> (2000). At the same time, not every violation of the rule requires suppression of the evidence obtained. Evidence is admissible when the central <span class="star-pagination">*619</span> concerns of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> are not likely to be implicated and when other objectives of the criminal justice system are best served by its introduction. Thus, we have held that statements obtained in violation of the rule can be used for impeachment, so that the truth-finding function of the trial is not distorted by the defense, see <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971); that there is an exception to protect countervailing concerns of public safety, see <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U. S. 649</a></span> (1984); and that physical evidence obtained in reliance on statements taken in violation of the rule is admissible, see <i>United States</i> v. <i>Patane, post,</i> p. 630. These cases, in my view, are correct. They recognize that admission of evidence is proper when it would further important objectives without compromising <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s central concerns. Under these precedents, the scope of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> suppression remedy depends on a consideration of those legitimate interests and on whether admission of the evidence under the circumstances would frustrate <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s central concerns and objectives.</p>
<p><i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), reflects this approach. In <i>Elstad,</i> a suspect made an initial incriminating statement at his home. The suspect had not received a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning before making the statement, apparently because it was not clear whether the suspect was in custody at the time. The suspect was taken to the station house, where he received a proper warning, waived his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, and made a second statement. He later argued that the postwarning statement should be suppressed because it was related to the unwarned first statement, and likely induced or caused by it. The Court held that, although a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation made the first statement inadmissible, the postwarning statements could be introduced against the accused because "neither the general goal of deterring improper police conduct nor the Fifth Amendment goal of assuring trustworthy evidence would be served by suppression" <span class="star-pagination">*620</span> given the facts of that case. <i><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad, supra,</a></span></i> at 308 (citing <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#445" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 445</a></span> (1974)).</p>
<p>In my view, <i>Elstad</i> was correct in its reasoning and its result. <i>Elstad</i> reflects a balanced and pragmatic approach to enforcement of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning. An officer may not realize that a suspect is in custody and warnings are required. The officer may not plan to question the suspect or may be waiting for a more appropriate time. Skilled investigators often interview suspects multiple times, and good police work may involve referring to prior statements to test their veracity or to refresh recollection. In light of these realities it would be extravagant to treat the presence of one statement that cannot be admitted under <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> as sufficient reason to prohibit subsequent statements preceded by a proper warning. See <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#309" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 309</a></span> ("It is an unwarranted extension of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to hold that a simple failure to administer the warnings . . . so taints the investigatory process that a subsequent voluntary and informed waiver is ineffective for some indeterminate period"). That approach would serve "neither the general goal of deterring improper police conduct nor the Fifth Amendment goal of assuring trustworthy evidence would be served by suppression of the . . . testimony." <i>Id.,</i> at 308.</p>
<p>This case presents different considerations. The police used a two-step questioning technique based on a deliberate violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning was withheld to obscure both the practical and legal significance of the admonition when finally given. As JUSTICE SOUTER points out, the two-step technique permits the accused to conclude that the right not to respond did not exist when the earlier incriminating statements were made. The strategy is based on the assumption that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings will tend to mean less when recited midinterrogation, after inculpatory statements have already been obtained. This tactic relies on an intentional misrepresentation of the protection that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> <span class="star-pagination">*621</span> offers and does not serve any legitimate objectives that might otherwise justify its use.</p>
<p>Further, the interrogating officer here relied on the defendant's prewarning statement to obtain the postwarning statement used against her at trial. The postwarning interview resembled a cross-examination. The officer confronted the defendant with her inadmissible prewarning statements and pushed her to acknowledge them. See App. 70 ("`Trice, didn't you tell me that he was supposed to die in his sleep?"). This shows the temptations for abuse inherent in the two-step technique. Reference to the prewarning statement was an implicit suggestion that the mere repetition of the earlier statement was not independently incriminating. The implicit suggestion was false.</p>
<p>The technique used in this case distorts the meaning of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and furthers no legitimate countervailing interest. The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule would be frustrated were we to allow police to undermine its meaning and effect. The technique simply creates too high a risk that postwarning statements will be obtained when a suspect was deprived of "knowledge essential to his ability to understand the nature of his rights and the consequences of abandoning them." <i>Moran</i> v. <i>Burbine,</i> <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#423" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 423-424</a></span> (1986). When an interrogator uses this deliberate, two-step strategy, predicated upon violating <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> during an extended interview, postwarning statements that are related to the substance of prewarning statements must be excluded absent specific, curative steps.</p>
<p>The plurality concludes that whenever a two-stage interview occurs, admissibility of the postwarning statement should depend on "whether [the] <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings delivered midstream could have been effective enough to accomplish their object" given the specific facts of the case. <i>Ante,</i> at 615. This test envisions an objective inquiry from the perspective of the suspect, and applies in the case of both intentional and unintentional two-stage interrogations. <span class="star-pagination">*622</span> <i>Ante,</i> at 615-617. In my view, this test cuts too broadly. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s clarity is one of its strengths, and a multifactor test that applies to every two-stage interrogation may serve to undermine that clarity. Cf. <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#430" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 430</a></span> (1984). I would apply a narrower test applicable only in the infrequent case, such as we have here, in which the two-step interrogation technique was used in a calculated way to undermine the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning.</p>
<p>The admissibility of postwarning statements should continue to be governed by the principles of <i>Elstad</i> unless the deliberate two-step strategy was employed. If the deliberate two-step strategy has been used, postwarning statements that are related to the substance of prewarning statements must be excluded unless curative measures are taken before the postwarning statement is made. Curative measures should be designed to ensure that a reasonable person in the suspect's situation would understand the import and effect of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning and of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> waiver. For example, a substantial break in time and circumstances between the prewarning statement and the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning may suffice in most circumstances, as it allows the accused to distinguish the two contexts and appreciate that the interrogation has taken a new turn. Cf. <i>Westover</i> v. <i>United States,</i> decided with <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Alternatively, an additional warning that explains the likely inadmissibility of the prewarning custodial statement may be sufficient. No curative steps were taken in this case, however, so the postwarning statements are inadmissible and the conviction cannot stand.</p>
<p>For these reasons, I concur in the judgment of the Court.</p>
<p>JUSTICE O'CONNOR, with whom THE CHIEF JUSTICE, JUSTICE SCALIA, and JUSTICE THOMAS join, dissenting.</p>
<p>The plurality devours <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), even as it accuses petitioner's argument of "disfigur[ing]" that decision. <i>Ante,</i> at 614. I believe that we <span class="star-pagination">*623</span> are bound by <i>Elstad</i> to reach a different result, and I would vacate the judgment of the Supreme Court of Missouri.</p>
<p></p>
<h2>I</h2>
<p>On two preliminary questions I am in full agreement with the plurality. First, the plurality appropriately follows <i>Elstad</i> in concluding that Seibert's statement cannot be held inadmissible under a "fruit of the poisonous tree" theory. <i>Ante,</i> at 612, n. 4 (internal quotation marks omitted). Second, the plurality correctly declines to focus its analysis on the subjective intent of the interrogating officer.</p>
<p></p>
<h2>A</h2>
<p>This Court has made clear that there simply is no place for a robust deterrence doctrine with regard to violations of <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). See <i>Dickerson</i> v. <i>United States,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#441" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428, 441</a></span> (2000) ("Our decision in <i>[Elstad]</i>  refusing to apply the traditional `fruits' doctrine developed in Fourth Amendment cases  . . . simply recognizes the fact that unreasonable searches under the Fourth Amendment are different from unwarned interrogation under the Fifth Amendment"); <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#306" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 306</a></span> (unlike the Fourth Amendment exclusionary rule, the "<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> exclusionary rule . . . serves the Fifth Amendment and sweeps more broadly than the Fifth Amendment itself"); see also <i>United States</i> v. <i>Patane, post,</i> at 644-645 (KENNEDY, J., concurring in judgment) (refusal to suppress evidence obtained following an unwarned confession in <i>Elstad, New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U. S. 649</a></span> (1984), and <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971), was based on "our recognition that the concerns underlying the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> . . . rule must be accommodated to other objectives of the criminal justice system"). Consistent with that view, the Court today refuses to apply the traditional "fruits" analysis to the physical fruit of a claimed <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation. <i>Patane, post,</i> p. 630. The plurality <span class="star-pagination">*624</span> correctly refuses to apply a similar analysis to testimonial fruits.</p>
<p>Although the analysis the plurality ultimately espouses examines the same facts and circumstances that a "fruits" analysis would consider (such as the lapse of time between the two interrogations and change of questioner or location), it does so for entirely different reasons. The fruits analysis would examine those factors because they are relevant to the balance of deterrence value versus the "drastic and socially costly course" of excluding reliable evidence. <i>Nix</i> v. <i>Williams,</i> <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#442" aria-description="Citation for case: Nix v. Williams">467 U. S. 431, 442-443</a></span> (1984). The plurality, by contrast, looks to those factors to inform the <i>psychological</i> judgment regarding whether the suspect has been informed effectively of her right to remain silent. The analytical underpinnings of the two approaches are thus entirely distinct, and they should not be conflated just because they function similarly in practice. Cf. <i>ante,</i> at 617-618 (BREYER, J., concurring).</p>
<p></p>
<h2>B</h2>
<p>The plurality's rejection of an intent-based test is also, in my view, correct. Freedom from compulsion lies at the heart of the Fifth Amendment, and requires us to assess whether a suspect's decision to speak truly was voluntary. Because voluntariness is a matter of the suspect's state of mind, we focus our analysis on the way in which suspects experience interrogation. See generally <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#455" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 455</a></span> (summarizing psychological tactics used by police that "undermin[e]" the suspect's "will to resist," and noting that "the very fact of custodial interrogation . . . trades on the weakness of individuals"); <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 467</a></span> ("[I]n-custody interrogation of persons suspected or accused of crime contains inherently compelling pressures which work to undermine the individual's will to resist and to compel him to speak where he would not otherwise do so freely").</p>
<p>Thoughts kept inside a police officer's head cannot affect that experience. See <i>Moran</i> v. <i>Burbine,</i> <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412</a></span>, 422 <span class="star-pagination">*625</span> (1986) ("Events occurring outside of the presence of the suspect and entirely unknown to him surely can have no bearing on the capacity to comprehend and knowingly relinquish a constitutional right"). In <i><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">Moran</a></span>,</i> an attorney hired by the suspect's sister had been trying to contact the suspect and was told by the police, falsely, that they would not begin an interrogation that night. <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#416" aria-description="Citation for case: Moran v. Burbine"><i>Id.,</i> at 416-418</a></span>. The suspect was not aware that an attorney had been hired for him. <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#417" aria-description="Citation for case: Moran v. Burbine"><i>Id.,</i> at 417</a></span>. We rejected an analysis under which a different result would obtain for "the same defendant, armed with the same information and confronted with precisely the same police conduct" if something not known to the defendant  such as the fact that an attorney was attempting to contact him  had been different. <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#422" aria-description="Citation for case: Moran v. Burbine"><i>Id.,</i> at 422</a></span>. The same principle applies here. A suspect who experienced the exact same interrogation as Seibert, save for a difference in the undivulged, subjective intent of the interrogating officer when he failed to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, would not experience the interrogation any differently. "[W]hether intentional or inadvertent, the state of mind of the police is irrelevant to the question of the intelligence and voluntariness of respondent's election to abandon his rights. Although highly inappropriate, even deliberate deception of an attorney could not possibly affect a suspect's decision to waive his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights unless he were at least aware of the incident." <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#423" aria-description="Citation for case: Moran v. Burbine">475 U. S., at 423</a></span>. Cf. <i>Stansbury</i> v. <i>California,</i> <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#324" aria-description="Citation for case: Stansbury v. California">511 U. S. 318, 324-325</a></span> (1994) <i>(per curiam)</i> (police officer's subjective intent is irrelevant to whether suspect is in custody for <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> purposes; "one cannot expect the person under interrogation to probe the officer's innermost thoughts").</p>
<p>Because the isolated fact of Officer Hanrahan's intent could not have had any bearing on Seibert's "capacity to comprehend and knowingly relinquish" her right to remain silent, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#422" aria-description="Citation for case: Moran v. Burbine"><i>Moran, supra,</i> at 422</a></span>, it could not by itself affect the voluntariness of her confession. Moreover, recognizing an exception to <i>Elstad</i> for intentional violations would require focusing <span class="star-pagination">*626</span> constitutional analysis on a police officer's subjective intent, an unattractive proposition that we all but uniformly avoid. In general, "we believe that `sending state and federal courts on an expedition into the minds of police officers would produce a grave and fruitless misallocation of judicial resources.'" <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 922, n. 23</a></span> (1984) (quoting <i>Massachusetts</i> v. <i>Painten,</i> <span class="citation" data-id="9423573"><a href="/opinion/107577/massachusetts-v-painten/#565" aria-description="Citation for case: Massachusetts v. Painten">389 U. S. 560, 565</a></span> (1968) <i>(per curiam)</i> (White, J., dissenting)). This case presents the uncommonly straightforward circumstance of an officer openly admitting that the violation was intentional. But the inquiry will be complicated in other situations probably more likely to occur. For example, different officers involved in an interrogation might claim different states of mind regarding the failure to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. Even in the simple case of a single officer who claims that a failure to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings was inadvertent, the likelihood of error will be high. See W. LaFave, Search and Seizure § 1.4(e), p. 124 (3d ed. 1996) ("[T]here is no reason to believe that courts can with any degree of success determine in which instances the police had an ulterior motive").</p>
<p>These evidentiary difficulties have led us to reject an intent-based test in several criminal procedure contexts. For example, in <i>New York</i> v. <i><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">Quarles, supra</a></span></i><i>,</i> one of the factors that led us to reject an inquiry into the subjective intent of the police officer in crafting a test for the "public safety" exception to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was that officers' motives will be "largely unverifiable." 467 U. S., at 656. Similarly, our opinion in <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#813" aria-description="Citation for case: Whren v. United States">517 U. S. 806, 813-814</a></span> (1996), made clear that "the evidentiary difficulty of establishing subjective intent" was one of the reasons (albeit not the principal one) for refusing to consider intent in Fourth Amendment challenges generally.</p>
<p>For these reasons, I believe that the approach espoused by JUSTICE KENNEDY is ill advised. JUSTICE KENNEDY would extend <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s exclusionary rule to any case in which the use of the "two-step interrogation technique" was "deliberate" <span class="star-pagination">*627</span> or "calculated." <i>Ante,</i> at 622 (opinion concurring in judgment). This approach untethers the analysis from facts knowable to, and therefore having any potential directly to affect, the suspect. Far from promoting "clarity," <i>ibid.,</i> the approach will add a third step to the suppression inquiry. In virtually every two-stage interrogation case, in addition to addressing the standard <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and voluntariness questions, courts will be forced to conduct the kind of difficult, state-of-mind inquiry that we normally take pains to avoid.</p>
<p></p>
<h2>II</h2>
<p>The plurality's adherence to <i>Elstad,</i> and mine to the plurality, end there. Our decision in <i>Elstad</i> rejected two lines of argument advanced in favor of suppression. The first was based on the "fruit of the poisonous tree" doctrine, discussed above. The second was the argument that the "lingering compulsion" inherent in a defendant's having let the "cat out of the bag" required suppression. <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#311" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 311</a></span>. The Court of Appeals of Oregon, in accepting the latter argument, had endorsed a theory indistinguishable from the one today's plurality adopts: "[T]he coercive impact of the unconstitutionally obtained statement remains, because in a defendant's mind it has sealed his fate. It is this impact that must be dissipated in order to make a subsequent confession admissible." <i>State</i> v. <i>Elstad,</i> <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#677" aria-description="Citation for case: State v. Elstad">61 Ore. App. 673, 677</a></span>, <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#554" aria-description="Citation for case: State v. Elstad">658 P.2d 552, 554</a></span> (1983).</p>
<p>We rejected this theory outright. We did so not because we refused to recognize the "psychological impact of the suspect's conviction that he has let the cat out of the bag," but because we refused to "endo[w]" those "psychological effects" with "constitutional implications." <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#311" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 311</a></span>. To do so, we said, would "effectively immuniz[e] a suspect who responds to pre-<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> warning questions from the consequences of his subsequent informed waiver," an immunity that "comes at a high cost to legitimate law enforcement activity, while adding little desirable protection to the individual's <span class="star-pagination">*628</span> interest in not being <i>compelled</i> to testify against himself." <i>Id.,</i> at 312. The plurality might very well think that we struck the balance between Fifth Amendment rights and law enforcement interests incorrectly in <i>Elstad;</i> but that is not normally a sufficient reason for ignoring the dictates of <i>stare decisis.</i></p>
<p>I would analyze the two-step interrogation procedure under the voluntariness standards central to the Fifth Amendment and reiterated in <i>Elstad. Elstad</i> commands that if Seibert's first statement is shown to have been involuntary, the court must examine whether the taint dissipated through the passing of time or a change in circumstances: "When a prior statement is actually coerced, the time that passes between confessions, the change in place of interrogations, and the change in identity of the interrogators all bear on whether that coercion has carried over into the second confession." <i>Id.,</i> at 310 (citing <i>Westover</i> v. <i>United States,</i> decided with <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#494" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 494</a></span>). In addition, Seibert's second statement should be suppressed if she showed that it was involuntary despite the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. <i>Elstad, supra,</i> at 318 ("The relevant inquiry is whether, in fact, the second statement was also voluntarily made. As in any such inquiry, the finder of fact must examine the surrounding circumstances and the entire course of police conduct with respect to the suspect in evaluating the voluntariness of his statements"). Although I would leave this analysis for the Missouri courts to conduct on remand, I note that, unlike the officers in <i>Elstad,</i> Officer Hanrahan referred to Seibert's unwarned statement during the second part of the interrogation when she made a statement at odds with her unwarned confession. App. 70 ("`Trice, didn't you tell me that he was supposed to die in his sleep?"); cf. <i>Elstad, supra,</i> at 316 (officers did not "exploit the unwarned admission to pressure respondent into waiving his right to remain silent"). Such a tactic may bear on the voluntariness inquiry. Cf. <i>Frazier</i> v. <i>Cupp,</i> <span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#739" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 739</a></span> (1969) (fact that police had falsely <span class="star-pagination">*629</span> told a suspect that his accomplice had already confessed was "relevant" to the voluntariness inquiry); <i>Moran,</i> <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#423" aria-description="Citation for case: Moran v. Burbine">475 U. S., at 423-424</a></span> (in discussing police deception, stating that simply withholding information is "relevant to the constitutional validity of a waiver if it deprives a defendant of knowledge essential to his ability to understand the nature of his rights and the consequences of abandoning them"); <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#476" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda, supra,</i> at 476</a></span>.</p>
<p></p>
<h2>*   *   *</h2>
<p>Because I believe that the plurality gives insufficient deference to <i>Elstad</i> and that JUSTICE KENNEDY places improper weight on subjective intent, I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging affirmance were filed for the American Civil Liberties Union et al. by <i>Jonathan L. Abram, Christopher T. Handman, William H. Johnson, Steven R. Shapiro,</i> and <i>Lisa Kemler;</i> and for Michael R. Bromwich et al. by <i>George A. Cumming, Jr., Charles D. Weisselberg, Stephen J. Schulhofer, Kirsten D. Levingston, Frederick A. O. Schwarz, Jr.,</i> and <i>Tom Gerety.</i></p>
<p>[1]  "[T]he burden of showing admissibility rests, of course, on the prosecution." <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590, 604</a></span> (1975). The prosecution bears the burden of proving, at least by a preponderance of the evidence, the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> waiver, <i>Colorado</i> v. <i>Connelly,</i> <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/#169" aria-description="Citation for case: Colorado v. Connelly">479 U. S. 157, 169</a></span> (1986), and the voluntariness of the confession, <i>Lego</i> v. <i>Twomey,</i> <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#489" aria-description="Citation for case: Lego v. Twomey">404 U. S. 477, 489</a></span> (1972).</p>
<p>[2]  Emphasizing the impeachment exception to the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule approved by this Court, <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971), some training programs advise officers to omit <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings altogether or to continue questioning after the suspect invokes his rights. See, <i>e. g.,</i> Police Law Manual 83 ("There is no need to give a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning before asking questions if . . . the answers given . . . will not be required by the prosecutor during the prosecution's case-in-chief"); California Commission on Peace Officer Standards and Training, Video Training Programs for California Law Enforcement, Miranda: Post-Invocation Questioning (broadcast July 11, 1996) ("We . . . have been encouraging you to continue to question a suspect after they've invoked their <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights"); D. Zulawski &amp; D. Wicklander, Practical Aspects of Interview and Interrogation 50-51 (2d ed. 2002) (describing the practice of "[b]eachheading" as useful for impeachment purpose (emphasis deleted)); see also Weisselberg, Saving <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> <span class="citation no-link">84 Cornell L. Rev. 109</span>, 110, 132-139 (1998) (collecting California training materials encouraging questioning "outside <i>Miranda</i>"). This training is reflected in the reported cases involving deliberate questioning after invocation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. See, <i>e. g., </i><i>California Attorneys for Criminal Justice</i> v. <i>Butts,</i> <span class="citation" data-id="6984365"><a href="/opinion/7079352/california-attorneys-for-criminal-justice-v-butts/#1042" aria-description="Citation for case: California Attorneys for Criminal Justice v. Butts">195 F. 3d 1039, 1042-1044</a></span> (CA9 1999); <i>Henry</i> v. <i>Kernan,</i> <span class="citation" data-id="766929"><a href="/opinion/766929/bobby-henry-v-peggy-kernan-warden-daniel-e-lungren-attorney-general/#1026" aria-description="Citation for case: Bobby Henry v. Peggy Kernan, Warden Daniel E. Lungren,...">197 F. 3d 1021, 1026</a></span> (CA9 1999); <i>People</i> v. <i>Neal,</i> <span class="citation" data-id="9787381"><a href="/opinion/2588587/people-v-neal/#68" aria-description="Citation for case: People v. Neal">31 Cal. 4th 63, 68</a></span>, <span class="citation" data-id="9787381"><a href="/opinion/2588587/people-v-neal/#282" aria-description="Citation for case: People v. Neal">72 P. 3d 280, 282</a></span> (2003); <i>People</i> v. <i>Peevy,</i> <span class="citation" data-id="9609905"><a href="/opinion/1378981/people-v-peevy/#1189" aria-description="Citation for case: People v. Peevy">17 Cal. 4th 1184, 1189</a></span>, <span class="citation" data-id="9609905"><a href="/opinion/1378981/people-v-peevy/#1215" aria-description="Citation for case: People v. Peevy">953 P. 2d 1212, 1215</a></span> (1998). Scholars have noted the growing trend of such practices. See, <i>e. g.,</i> Leo, Questioning the Relevance of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in the Twenty-First Century, <span class="citation no-link">99 Mich. L. Rev. 1000</span>, 1010 (2001); Weisselberg, In the Stationhouse After <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span>,</i> <span class="citation no-link">99 Mich. L. Rev. 1121</span>, 1123-1154 (2001).
</p>
<p>It is not the case, of course, that law enforcement educators en masse are urging that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> be honored only in the breach. See, <i>e. g.,</i> C. O'Hara &amp; G. O'Hara, Fundamentals of Criminal Investigation 133 (7th ed. 2003) (instructing police to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings before conducting custodial interrogation); F. Inbau, J. Reid, &amp; J. Buckley, Criminal Interrogation and Confessions 221 (3d ed. 1986) (hereinafter Inbau, Reid, &amp; Buckley) (same); John Reid &amp; Associates, Interviewing &amp; Interrogation: The Reid Technique 61 (1991) (same). Most police manuals do not advocate the question-first tactic, because they understand that <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), involved an officer's good-faith failure to warn. See, <i>e. g.,</i> Inbau, Reid, &amp; Buckley 241 (<i>Elstad</i>'s "facts as well as [its] specific holding" instruct that "where an interrogator has failed to administer the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings in the mistaken belief that, under the circumstances of the particular case, the warnings were not required, . . . corrective measures . . . salvage an interrogation opportunity").</p>
<p>[3]  See, <i>e. g., </i><i>United States</i> v. <i>Orso,</i> <span class="citation" data-id="9494408"><a href="/opinion/775079/united-states-v-jody-myesha-orso/#1032" aria-description="Citation for case: United States v. Jody Myesha Orso">266 F. 3d 1030, 1032-1033</a></span> (CA9 2001) (en banc); <i>Pope</i> v. <i>Zenon,</i> <span class="citation" data-id="707574"><a href="/opinion/707574/charles-s-pope-petitioner-appellant-v-carl-zenon-superintendent-osci/#1023" aria-description="Citation for case: Charles S. POPE, Petitioner-Appellant, v. Carl ZENON,...">69 F. 3d 1018, 1023-1024</a></span> (CA9 1995), overruled by <i><span class="citation" data-id="9494408"><a href="/opinion/775079/united-states-v-jody-myesha-orso/" aria-description="Citation for case: United States v. Jody Myesha Orso">Orso, supra;</a></span> </i><i>Cooper</i> v. <i>Dupnik,</i> <span class="citation" data-id="9000842"><a href="/opinion/9008075/cooper-v-dupnik/#1224" aria-description="Citation for case: Cooper v. Dupnik">963 F. 2d 1220, 1224-1227, 1249</a></span> (CA9 1992) (en banc); <i>United States</i> v. <i>Carter,</i> <span class="citation" data-id="9479453"><a href="/opinion/528515/united-states-v-terry-gene-carter/#373" aria-description="Citation for case: United States v. Terry Gene Carter">884 F. 2d 368, 373</a></span> (CA9 1989); <i>United States</i> v. <i>Esquilin,</i> <span class="citation" data-id="198872"><a href="/opinion/198872/united-states-v-esquilin/#317" aria-description="Citation for case: United States v. Esquilin">208 F. 3d 315, 317</a></span> (CA1 2000); <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9694229"><a href="/opinion/1907111/davis-v-united-states/#1165" aria-description="Citation for case: Davis v. United States">724 A. 2d 1163, 1165-1166</a></span> (D. C. App. 1998).</p>
<p>[4]  Respondent Seibert argues that her second confession should be excluded from evidence under the doctrine known by the metaphor of the "fruit of the poisonous tree," developed in the Fourth Amendment context in <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963): evidence otherwise admissible but discovered as a result of an earlier violation is excluded as tainted, lest the law encourage future violations. But the Court in <i>Elstad</i> rejected the <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> fruits doctrine for analyzing the admissibility of a subsequent warned confession following "an initial failure . . . to administer the warnings required by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i>" <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#300" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 300</a></span>. In <i>Elstad,</i> "a simple failure to administer the warnings, unaccompanied by any actual coercion or other circumstances calculated to undermine the suspect's ability to exercise his free will," did not "so tain[t] the investigatory process that a subsequent voluntary and informed waiver is ineffective for some indeterminate period. Though <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires that the unwarned admission must be suppressed, the admissibility of any subsequent statement should turn in these circumstances solely on whether it is knowingly and voluntarily made." <i>Id.,</i> at 309. <i>Elstad</i> held that "a suspect who has once responded to unwarned yet uncoercive questioning is not thereby disabled from waiving his rights and confessing after he has been given the requisite <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings." <i>Id.,</i> at 318. In a sequential confession case, clarity is served if the later confession is approached by asking whether in the circumstances the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings given could reasonably be found effective. If yes, a court can take up the standard issues of voluntary waiver and voluntary statement; if no, the subsequent statement is inadmissible for want of adequate <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, because the earlier and later statements are realistically seen as parts of a single, unwarned sequence of questioning.</p>
<p>[5]  It bears emphasizing that the effectiveness <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> assumes the warnings can have must potentially extend through the repeated interrogation, since a suspect has a right to stop at any time. It seems highly unlikely that a suspect could retain any such understanding when the interrogator leads him a second time through a line of questioning the suspect has already answered fully. The point is not that a later unknowing or involuntary confession cancels out an earlier, adequate warning; the point is that the warning is unlikely to be effective in the question-first sequence we have described.</p>
<p>[6]  Because the intent of the officer will rarely be as candidly admitted as it was here (even as it is likely to determine the conduct of the interrogation), the focus is on facts apart from intent that show the question-first tactic at work.</p>
<p>[7]  We do not hold that a formal addendum warning that a previous statement could not be used would be sufficient to change the character of the question-first procedure to the point of rendering an ensuing statement admissible, but its absence is clearly a factor that blunts the efficacy of the warnings and points to a continuing, not a new, interrogation.</p>
<p>[8]  Because we find that the warnings were inadequate, there is no need to assess the actual voluntariness of the statement.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Mitchell v. Wisconsin.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Mitchell v. Wisconsin"
type: case
citation: "588 U.S. 840 (2019)"
parallel_cite: "139 S. Ct. 2525; 204 L. Ed. 2d 1040"
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2019
date_decided: 2019-06-27
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2019-06-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Mitchell v. Wisconsin
  varies_by_point: false
  scope_note: "Plurality opinion (Alito, J.); judgment supported by Thomas, J., concurring in the judgment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/9231242/mitchell-v-wisconsin/"
  cluster_id: 9231242
  opinion_id: 9226047
  identity_checked: true
homes:
  - page: "[[Destruction of Evidence]]"
    role: "Key — Progeny / Refinement"
  - page: "[[SIA Alcohol Tests]]"
    role: "Related (cross-doctrine)"
related: ["[[Missouri v. McNeely]]", "[[Schmerber v. California]]", "[[Birchfield v. North Dakota]]"]
aliases: []
tags: ["case", "fourth-amendment", "exigent-circumstances", "blood-draw", "dui", "unconscious-driver"]
holding: "When police have probable cause for DUI and the driver's unconsciousness/stupor forces hospitalization before a breath test can be…"
lake:
  record_id: Mitchell v. Wisconsin
  status: verified
  projected_at: 2026-07-06
---

# Mitchell v. Wisconsin

*588 U.S. 840 (2019)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Mitchell was arrested for drunk driving and grew too lethargic for a breath test, so officers took him to a hospital, where he became unconscious. Without a warrant, the officers directed a blood draw, which showed a blood-alcohol concentration well above the legal limit.

## Issue
Whether police may conduct a warrantless blood draw on an unconscious drunk-driving suspect who cannot be given a breath test.

## Rule
Generally yes (plurality). "When police have probable cause to believe a person has committed a drunk-driving offense and the driver's unconsciousness or stupor requires him to be taken to the hospital or similar facility before police have a reasonable opportunity to administer a standard evidentiary breath test, they may almost always order a warrantless blood test to measure the driver's BAC without offending the Fourth Amendment." — 139 S. Ct. at 2539 (plurality opinion). ^pin-2539

## Application
Mitchell was unconscious and so could not take a breath test, and his condition required hospitalization; the officers had probable cause to believe he had driven drunk. Under the plurality's rule, the [[Exigent Circumstances and Hot Pursuit|exigencies]] attending an unconscious driver almost always justify a warrantless blood draw. Because Mitchell had not had a chance to show that his was the unusual case in which a warrant would not have interfered with other pressing duties, the Court [[Reading and Citing Cases#on-remand|remanded]] for that purpose.

## Conclusion
[[Reading and Citing Cases#vacated|Vacated]] and [[Reading and Citing Cases#on-remand|remanded]]; the warrantless blood draw was generally permissible, subject to Mitchell's opportunity to show that his was an unusual case.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (Alito plurality; Thomas, J., concurring in the judgment).
- No negative treatment. *Mitchell* builds on the [[Exigent Circumstances and Hot Pursuit|exigency]] analysis of [[Missouri v. McNeely]] and [[Schmerber v. California]] for the unconscious-driver context.

## Appears on
- [[Exigent Circumstances and Hot Pursuit]] — *Key — Progeny / Refinement*
- [[SIA Alcohol Tests]] — *Related (cross-doctrine)*

## Sources
- *Mitchell v. Wisconsin*, 588 U.S. 840 (2019) — https://www.courtlistener.com/opinion/9231242/mitchell-v-wisconsin/ — pinpoint: 139 S. Ct. 2539 (plurality, Part IV). (CL carries the official reporter text; cluster 9231242 → lead opinion 9226047. The pinpoint uses the S. Ct. reporter page carried in the CL text.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "70d3208d4faffe49", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Mitchell v. Wisconsin"}, "payload": {"all": [{"cite": "588 U.S. 840", "page": "840", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "588"}, {"cite": "139 S. Ct. 2525", "page": "2525", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "139"}, {"cite": "204 L. Ed. 2d 1040", "page": "1040", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "204"}], "display": "588 U.S. 840", "official": {"cite": "588 U.S. 840", "page": "840", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "588"}, "official_selection_present": true, "record_id": "Mitchell v. Wisconsin"}}
{"assertion_id": "7fd4c17ad5babe55", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-2539", "record_id": "Mitchell v. Wisconsin"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-2539", "pinpoint_status": "slip-only", "quote": "--- # Mitchell v. Wisconsin *588 U.S. 840 (2019)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Mitchell was arrested for drunk driving and grew too lethargic for a breath test, so officers took him to a hospital, where he became unconscious. Without a warrant, the officers directed a blood draw, which showed a blood-alcohol concentration well above the legal limit. ## Issue Whether police may conduct a warrantless blood draw on an unconscious drunk-driving suspect who cannot be given a breath test. ## Rule Generally yes (plurality).", "quote_fidelity": "mismatch", "record_id": "Mitchell v. Wisconsin", "star_marker": null}}
{"assertion_id": "7e0def19a5104494", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Mitchell v. Wisconsin"}, "payload": {"as_of_content": "2019-06-27", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Mitchell v. Wisconsin", "scope_note": "Plurality opinion (Alito, J.); judgment supported by Thomas, J., concurring in the judgment.", "varies_by_point": false}}
```

### lake record — Mitchell v. Wisconsin

```json
{
  "schema_version": "s2.v1",
  "record_id": "Mitchell v. Wisconsin",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Mitchell v. Wisconsin",
    "case_name_short": "",
    "case_name_full": "Gerald P. MITCHELL v. WISCONSIN",
    "input_case_name": "Mitchell v. Wisconsin",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2019-06-27",
    "year": 2019,
    "docket": null,
    "cluster_id": 9231242,
    "lead_opinion_id": 9226047,
    "sibling_ids": [
      9226047,
      9226048
    ],
    "absolute_url": "/opinion/9231242/mitchell-v-wisconsin/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 4633470,
        "score": 120,
        "case_name": "Mitchell v. Wisconsin"
      },
      {
        "cluster_id": 9339798,
        "score": 20,
        "case_name": "Mitchell v. Wisconsin"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "588 U.S. 840",
      "volume": "588",
      "reporter": "U.S.",
      "page": "840",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "139 S. Ct. 2525",
        "volume": "139",
        "reporter": "S. Ct.",
        "page": "2525",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "204 L. Ed. 2d 1040",
        "volume": "204",
        "reporter": "L. Ed. 2d",
        "page": "1040",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "588 U.S. 840",
        "volume": "588",
        "reporter": "U.S.",
        "page": "840",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "139 S. Ct. 2525",
        "volume": "139",
        "reporter": "S. Ct.",
        "page": "2525",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "204 L. Ed. 2d 1040",
        "volume": "204",
        "reporter": "L. Ed. 2d",
        "page": "1040",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "588 U.S. 840",
    "official_selection": {
      "court_class": "scotus",
      "selected": "588 U.S. 840",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-2539",
      "page": null,
      "quote": "--- # Mitchell v. Wisconsin *588 U.S. 840 (2019)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Mitchell was arrested for drunk driving and grew too lethargic for a breath test, so officers took him to a hospital, where he became unconscious. Without a warrant, the officers directed a blood draw, which showed a blood-alcohol concentration well above the legal limit. ## Issue Whether police may conduct a warrantless blood draw on an unconscious drunk-driving suspect who cannot be given a breath test. ## Rule Generally yes (plurality).",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2019-06-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Mitchell v. Wisconsin",
    "varies_by_point": false,
    "scope_note": "Plurality opinion (Alito, J.); judgment supported by Thomas, J., concurring in the judgment.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Portulano",
          "cluster_id": 10135231,
          "cite": [
            "320 Or. App. 335",
            "514 P.3d 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dawn M. Prado",
          "cluster_id": 4893130,
          "cite": [
            "960 N.W.2d 869",
            "2021 WI 64"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Miller",
          "cluster_id": 8248921,
          "cite": [
            "978 N.W.2d 19",
            "312 Neb. 17"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fuld v. Palestine Liberation Organization",
          "cluster_id": 9425200,
          "cite": [
            "82 F.4th 74"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Nelson",
          "cluster_id": 9508065,
          "cite": [
            "970 N.W.2d 814",
            "2022 S.D. 12"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "L.B. v. United States",
          "cluster_id": 7857259,
          "cite": [
            "515 P.3d 818",
            "409 Mont. 505",
            "2022 MT 166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Randall J. Weddle",
          "cluster_id": 4721814,
          "cite": [
            "224 A.3d 1035",
            "2020 ME 12"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jonathan Anderson",
          "cluster_id": 9498858,
          "cite": [
            "101 F.4th 586"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Yancy Kevin Dieter",
          "cluster_id": 10109472,
          "cite": [
            "948 N.W.2d 431",
            "393 Wis. 2d 796",
            "2020 WI App 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Manubolu",
          "cluster_id": 5093549,
          "cite": [
            "13 F.4th 57"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joshua Parks v. State of Arkansas",
          "cluster_id": 10607297,
          "cite": [
            "599 S.W.3d 382",
            "2020 Ark. App. 267"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gerald P. Mitchell",
          "cluster_id": 10110635,
          "cite": [
            "978 N.W.2d 231",
            "404 Wis. 2d 103",
            "2022 WI App 31"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The PEOPLE of the State of Colorado v. Glen Gary MONTOYA",
          "cluster_id": 10613799,
          "cite": [
            "546 P.3d 605"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Donnie Gene Richards",
          "cluster_id": 10109475,
          "cite": [
            "948 N.W.2d 359",
            "393 Wis. 2d 772",
            "2020 WI App 48"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Castro",
          "cluster_id": 10883712,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Valencia",
          "cluster_id": 10806666,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Denham",
          "cluster_id": 10797878,
          "cite": [
            "197 Wash. 2d 759",
            "489 P.3d 1138"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Indiana v. Dennis R Poland, Jr.",
          "cluster_id": 10681794,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Forrest R. Stewart v. State of Arkansas",
          "cluster_id": 10607993,
          "cite": [
            "611 S.W.3d 720",
            "2020 Ark. App. 515"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Louisiana v. Joseph W. Miller",
          "cluster_id": 10580798,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(9226047 OR 9226048) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 36,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 36,
        "triage_read": 1,
        "triage_snippet_classified": 35
      },
      "lane2_top_cited": {
        "query": "cites:(9226047 OR 9226048)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0wJnM9NjQ0OTA2OSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%289226047+OR+9226048%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 20,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(9226047 OR 9226048)",
        "reviewed": 14,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 14,
        "triage_read": 0,
        "triage_snippet_classified": 14
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(9226047 OR 9226048)",
    "indexed_citing_opinions": 46,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 9226047,
        "count": 46,
        "count_source": "search"
      },
      {
        "opinion_id": 9226048,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 153,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mitchell-v-wisconsin.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc2NTg0MTQmcz02NDQ5MDY5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%289226047+OR+9226048%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T14:21:08Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:21:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:21:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:24:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:21:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Mitchell v. Wisconsin (truncated)

```
<opinion type="majority">
<p id="p-12">I</p>
<p id="p-13">A</p>
<p id="p-14">In <em>Birchfield</em> v. <em>North Dakota</em> , 579 U.S. ----, <extracted-citation case-ids="12597986" index="0" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct. 2160</a></span></extracted-citation>, <extracted-citation case-ids="12597986" index="1" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">195 L.Ed.2d 560</a></span></extracted-citation> (2016), we recounted the country's efforts over the years to address the terrible problem of drunk driving. Today, "all States have laws that prohibit motorists from driving with a [BAC] that exceeds a specified level." <em><extracted-citation case-ids="12597986" index="2" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Id.</a></span></extracted-citation></em> , at ----, <extracted-citation case-ids="12597986" index="3" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2166</a></span></extracted-citation>. And to help enforce BAC limits, every State has passed what are popularly called implied-consent laws. <em><extracted-citation case-ids="12597986" index="4" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Ibid.</a></span></extracted-citation></em> As "a condition of the privilege of" using the public roads, these laws require that drivers submit to BAC testing "when there is sufficient reason to believe they are violating the State's drunk-driving laws." <em><extracted-citation case-ids="12597986" index="5" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Id.</a></span></extracted-citation></em> , at ----, ----, <extracted-citation case-ids="12597986" index="6" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/#2166" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2166</a></span>, 2169</extracted-citation>).</p>
<p id="p-15">Wisconsin's implied-consent law is much like those of the other 49 States and the District of Columbia. It deems drivers to have consented to breath or blood tests if an officer has reason to believe they have committed one of several drug- or alcohol-related offenses.<footnotemark>1</footnotemark> See <extracted-citation index="7" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305"><span class="citation no-link">Wis. Stat. §§ 343.305</span></extracted-citation>(2), (3). Officers seeking to conduct a BAC test must read aloud a statement declaring their intent to administer the test and advising drivers of their options and the implications of their choice. § 343.305(4). If a driver's BAC level proves too high, his license will be suspended; but if he refuses testing, his license will be <em>revoked</em> and his refusal may be used against him in court. See <em>ibid</em> . No <a class="page-label" data-citation-index="1" data-label="2532" href="#p2532" id="p2532">*2532</a>test will be administered if a driver refuses-or, as the State would put it, "withdraws" his statutorily presumed consent. But "[a] person who is unconscious or otherwise not capable of withdrawing consent is presumed not to have" withdrawn it. § 343.305(3)(b). See also §§ 343.305(3)(ar) 1-2. More than half the States have provisions like this one regarding unconscious drivers.</p>
<p id="p-16">B</p>
<p id="p-17">The sequence of events that gave rise to this case began when Officer Alexander Jaeger of the Sheboygan Police Department received a report that petitioner Gerald Mitchell, appearing to be very drunk, had climbed into a van and driven off. Jaeger soon found Mitchell wandering near a lake. Stumbling and slurring his words, Mitchell could hardly stand without the support of two officers. Jaeger judged a field sobriety test hopeless, if not dangerous, and gave Mitchell a preliminary breath test. It registered a BAC level of 0.24%, triple the legal limit for driving in Wisconsin. Jaeger arrested Mitchell for operating a vehicle while intoxicated and, as is standard practice, drove him to a police station for a more reliable breath test using better equipment.</p>
<p id="p-18">On the way, Mitchell's condition continued to deteriorate-so much so that by the time the squad car had reached the station, he was too lethargic even for a breath test. Jaeger therefore drove Mitchell to a nearby hospital for a blood test; Mitchell lost consciousness on the ride over and had to be wheeled in. Even so, Jaeger read aloud to a slumped Mitchell the standard statement giving drivers a chance to refuse BAC testing. Hearing no response, Jaeger asked hospital staff to draw a blood sample. Mitchell remained unconscious while the sample was taken, and analysis of his blood showed that his BAC, about 90 minutes after his arrest, was 0.222%.</p>
<p id="p-19">Mitchell was charged with violating two related drunk-driving provisions. See §§ 346.63(1)(a), (b). He moved to suppress the results of the blood test on the ground that it violated his Fourth Amendment right against "unreasonable searches" because it was conducted without a warrant. Wisconsin chose to rest its response on the notion that its implied-consent law (together with Mitchell's free choice to drive on its highways) rendered the blood test a consensual one, thus curing any Fourth Amendment problem. In the end, the trial court denied Mitchell's motion to suppress, and a jury found him guilty of the charged offenses. The intermediate appellate court certified two questions to the Wisconsin Supreme Court: first, whether compliance with the State's implied-consent law was sufficient to show that Mitchell's test was consistent with the Fourth Amendment and, second, whether a warrantless blood draw from an unconscious person violates the Fourth Amendment. See <extracted-citation case-ids="12556993" index="8" url="https://cite.case.law/nw2d/914/151/"><span class="citation" data-id="9886762"><a href="/opinion/4513691/state-v-gerald-p-mitchell/" aria-description="Citation for case: State v. Gerald P. Mitchell">2018 WI 84</a></span></extracted-citation>, ¶15, <extracted-citation case-ids="12556993" index="9" url="https://cite.case.law/nw2d/914/151/"><span class="citation" data-id="9886762"><a href="/opinion/4513691/state-v-gerald-p-mitchell/" aria-description="Citation for case: State v. Gerald P. Mitchell">383 Wis.2d 192</a></span></extracted-citation>, 202-203, <extracted-citation case-ids="12556993" index="10" url="https://cite.case.law/nw2d/914/151/"><span class="citation" data-id="9886762"><a href="/opinion/4513691/state-v-gerald-p-mitchell/" aria-description="Citation for case: State v. Gerald P. Mitchell">914 N.W.2d 151</a></span></extracted-citation>, 155-156 (2018). The Wisconsin Supreme Court affirmed Mitchell's convictions, and we granted certiorari, 586 U.S. ----, <extracted-citation case-ids="12624625,12624626,12624627,12624628,12624629,12624630" index="11" url="https://cite.case.law/s-ct/139/915/"><span class="citation" data-id="9335135"><a href="/opinion/9339797/simply-wireless-inc-v-t-mobile-us-inc/" aria-description="Citation for case: Simply Wireless, Inc. v. T-Mobile U.S., Inc.">139 S.Ct. 915</a></span></extracted-citation>, <extracted-citation case-ids="12624626" index="12" url="https://cite.case.law/s-ct/139/915/12624626/"><span class="citation" data-id="9335136"><a href="/opinion/9339798/mitchell-v-wisconsin/" aria-description="Citation for case: Mitchell v. Wisconsin">202 L.Ed.2d 642</a></span></extracted-citation> (2019), to decide "[w]hether a statute authorizing a blood draw from an unconscious motorist provides an exception to the Fourth Amendment warrant requirement," Pet. for Cert. ii.</p>
<p id="p-20">II</p>
<p id="p-21">In considering Wisconsin's implied-consent law, we do not write on a blank slate. "Our prior opinions have referred approvingly to the general concept of implied-consent laws that impose civil penalties and evidentiary consequences on motorists who refuse to comply." <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , 579 U.S., at ----, <extracted-citation case-ids="12597986" index="13" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2185</a></span></extracted-citation>. But <a class="page-label" data-citation-index="1" data-label="2533" href="#p2533" id="p2533">*2533</a>our decisions have not rested on the idea that these laws do what their popular name might seem to suggest-that is, create actual consent to all the searches they authorize. Instead, we have based our decisions on the precedent regarding the specific constitutional claims in each case, while keeping in mind the wider regulatory scheme developed over the years to combat drunk driving. That scheme is centered on legally specified BAC limits for drivers-limits enforced by the BAC tests promoted by implied-consent laws.</p>
<p id="p-22">Over the last 50 years, we have approved many of the defining elements of this scheme. We have held that forcing drunk-driving suspects to undergo a blood test does not violate their constitutional right against self-incrimination. See <em>Schmerber v. California</em> , <extracted-citation case-ids="12047531" index="14" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S. 757</a></span></extracted-citation>, 765, <extracted-citation case-ids="12047531" index="15" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>, <extracted-citation case-ids="12047531" index="16" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">16 L.Ed.2d 908</a></span></extracted-citation> (1966). Nor does using their refusal against them in court. See <em>South Dakota v. Neville</em> , <extracted-citation case-ids="6200055" index="17" url="https://cite.case.law/us/459/553/#p563"><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">459 U.S. 553</a></span></extracted-citation>, 563, <extracted-citation case-ids="6200055" index="18" url="https://cite.case.law/us/459/553/#p563"><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">103 S.Ct. 916</a></span></extracted-citation>, <extracted-citation case-ids="6200055" index="19" url="https://cite.case.law/us/459/553/#p563"><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">74 L.Ed.2d 748</a></span></extracted-citation> (1983). And punishing that refusal with automatic license revocation does not violate drivers' due process rights if they have been arrested upon probable cause, <em>Mackey v. Montrym</em> , <extracted-citation case-ids="6179408" index="20" url="https://cite.case.law/us/443/1/"><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/" aria-description="Citation for case: MacKey v. Montrym">443 U.S. 1</a></span></extracted-citation>, <extracted-citation case-ids="6179408" index="21" url="https://cite.case.law/us/443/1/"><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/" aria-description="Citation for case: MacKey v. Montrym">99 S.Ct. 2612</a></span></extracted-citation>, <extracted-citation case-ids="6179408" index="22" url="https://cite.case.law/us/443/1/"><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/" aria-description="Citation for case: MacKey v. Montrym">61 L.Ed.2d 321</a></span></extracted-citation> (1979) ; on the contrary, this kind of summary penalty is "unquestionably legitimate." <em>Neville</em> , <em>supra</em> , at 560, <extracted-citation case-ids="6200055" index="23" url="https://cite.case.law/us/459/553/#p563"><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">103 S.Ct. 916</a></span></extracted-citation>.</p>
<p id="p-23">These cases generally concerned the Fifth and Fourteenth Amendments, but motorists charged with drunk driving have also invoked the Fourth Amendment's ban on "unreasonable searches" since BAC tests are "searches." See <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , 579 U.S., at ----, <extracted-citation case-ids="12597986" index="24" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2173</a></span></extracted-citation>. Though our precedent normally requires a warrant for a lawful search, there are well-defined exceptions to this rule. In <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , we applied precedent on the "search-incident-to-arrest" exception to BAC testing of conscious drunk-driving suspects. We held that their drunk-driving arrests, taken alone, justify warrantless breath tests but not blood tests, since breath tests are less intrusive, just as informative, and (in the case of conscious suspects) readily available. <em><extracted-citation case-ids="12597986" index="25" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12597986" index="26" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2184</a></span>-85</extracted-citation>.</p>
<p id="p-24">We have also reviewed BAC tests under the "exigent circumstances" exception-which, as noted, allows warrantless searches "to prevent the imminent destruction of evidence." <em>Missouri v. McNeely</em> , <extracted-citation case-ids="12697040" index="27" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S. 141</a></span></extracted-citation>, 149, <extracted-citation case-ids="12697040" index="28" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="29" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">185 L.Ed.2d 696</a></span></extracted-citation> (2013). In <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> , we were asked if this exception covers BAC testing of drunk-driving suspects in light of the fact that blood-alcohol evidence is always dissipating due to "natural metabolic processes." <em><extracted-citation case-ids="12697040" index="30" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">Id.</a></span></extracted-citation></em> , at 152, <extracted-citation case-ids="12697040" index="31" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>. We answered that the fleeting quality of BAC evidence alone is not enough. <em><extracted-citation case-ids="12697040" index="32" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">Id.</a></span></extracted-citation></em> , at 156, <extracted-citation case-ids="12697040" index="33" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>. But in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> it <em>did</em> justify a blood test of a drunk driver who had gotten into a car accident that gave police other pressing duties, for then the "<em>further</em> delay" caused by a warrant application really "<em>would</em> have threatened the destruction of evidence." <em>McNeely</em> , <em>supra</em> , at 152, <extracted-citation case-ids="12697040" index="34" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (emphasis added).</p>
<p id="p-25">Like <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> , this case sits much higher than <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> on the exigency spectrum. <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> was about the minimum degree of urgency common to all drunk-driving cases. In <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> , a car accident heightened that urgency. And here Mitchell's medical condition did just the same.</p>
<p id="p-26">Mitchell's stupor and eventual unconsciousness also deprived officials of a reasonable opportunity to administer a breath test. To be sure, Officer Jaeger managed to conduct "a preliminary breath test" using a portable machine when he first encountered Mitchell at the lake. App. to Pet.</p>
<p id="p-27"><a class="page-label" data-citation-index="1" data-label="2534" href="#p2534" id="p2534">*2534</a>for Cert. 60a. But he had no reasonable opportunity to give Mitchell a breath test using "evidence-grade breath testing machinery." <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , 579 U.S., at ----, <extracted-citation case-ids="12597986" index="35" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/#2192" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2192</a></span></extracted-citation> (SOTOMAYOR, J., concurring in part and dissenting in part). As a result, it was reasonable for Jaeger to seek a better breath test at the station; he acted with reasonable dispatch to procure one; and when Mitchell's condition got in the way, it was reasonable for Jaeger to pursue a blood test. As Justice SOTOMAYOR explained in her partial dissent in <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> :</p>
<blockquote id="p-28">"There is a common misconception that breath tests are conducted roadside, immediately after a driver is arrested. While some preliminary testing is conducted roadside, reliability concerns with roadside tests confine their use in most circumstances to establishing probable cause for an arrest.... The standard evidentiary breath test is conducted after a motorist is arrested and transported to a police station, governmental building, or mobile testing facility where officers can access reliable, evidence-grade breath testing machinery." <em><extracted-citation case-ids="12597986" index="36" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12597986" index="37" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2192</a></span></extracted-citation>.</blockquote>
<p id="p-29">Because the "standard evidentiary breath test is conducted after a motorist is arrested and transported to a police station" or another appropriate facility, <em><extracted-citation case-ids="12597986" index="38" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">ibid.</a></span></extracted-citation></em> , the important question here is what officers may do when a driver's unconsciousness (or stupor) eliminates any reasonable opportunity for <em>that</em> kind of breath test.</p>
<p id="p-30">III</p>
<p id="p-31">The Fourth Amendment guards the "right of the people to be secure in their persons ... against unreasonable searches" and provides that "no Warrants shall issue, but upon probable cause." A blood draw is a search of the person, so we must determine if its administration here without a warrant was reasonable. See <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , 579 U.S. at ----, <extracted-citation case-ids="12597986" index="39" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2174</a></span></extracted-citation>. Though we have held that a warrant is normally required, we have also "made it clear that there are exceptions to the warrant requirement." <em>Illinois v. McArthur</em> , <extracted-citation case-ids="9505639" index="40" url="https://cite.case.law/us/531/326/#p330"><span class="citation" data-id="9434039"><a href="/opinion/118405/illinois-v-mcarthur/" aria-description="Citation for case: Illinois v. McArthur">531 U.S. 326</a></span></extracted-citation>, 330, <extracted-citation case-ids="9505639" index="41" url="https://cite.case.law/us/531/326/#p330"><span class="citation" data-id="9434039"><a href="/opinion/118405/illinois-v-mcarthur/" aria-description="Citation for case: Illinois v. McArthur">121 S.Ct. 946</a></span></extracted-citation>, <extracted-citation case-ids="9505639" index="42" url="https://cite.case.law/us/531/326/#p330"><span class="citation" data-id="9434039"><a href="/opinion/118405/illinois-v-mcarthur/" aria-description="Citation for case: Illinois v. McArthur">148 L.Ed.2d 838</a></span></extracted-citation> (2001). And under the exception for exigent circumstances, a warrantless search is allowed when " 'there is compelling need for official action and no time to secure a warrant.' " <em>McNeely</em> , <em>supra</em> , at 149, <extracted-citation case-ids="12697040" index="43" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (quoting <em>Michigan v. Tyler</em> , <extracted-citation case-ids="1490288" index="44" url="https://cite.case.law/us/436/499/#p509"><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">436 U.S. 499</a></span></extracted-citation>, 509, <extracted-citation case-ids="1490288" index="45" url="https://cite.case.law/us/436/499/#p509"><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">98 S.Ct. 1942</a></span></extracted-citation>, <extracted-citation case-ids="1490288" index="46" url="https://cite.case.law/us/436/499/#p509"><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">56 L.Ed.2d 486</a></span></extracted-citation> (1978) ). In <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> , we considered how the exigent-circumstances exception applies to the broad category of cases in which a police officer has probable cause to believe that a motorist was driving under the influence of alcohol, and we do not revisit that question. Nor do we settle whether the exigent-circumstances exception covers the specific facts of this case.<footnotemark>2</footnotemark> Instead, we address how the exception <a class="page-label" data-citation-index="1" data-label="2535" href="#p2535" id="p2535">*2535</a>bears on the category of cases encompassed by the question on which we granted certiorari-those involving unconscious drivers.<footnotemark>3</footnotemark> In those cases, the need for a blood test is compelling, and an officer's duty to attend to more pressing needs may leave no time to seek a warrant.</p>
<p id="p-32">A</p>
<p id="p-33">The importance of the needs served by BAC testing is hard to overstate. The bottom line is that BAC tests are needed for enforcing laws that save lives. The specifics, in short, are these: Highway safety is critical; it is served by laws that criminalize driving with a certain BAC level; and enforcing these legal BAC limits requires efficient testing to obtain BAC evidence, which naturally dissipates. So BAC tests are crucial links in a chain on which vital interests hang. And when a breath test is unavailable to advance those aims, a blood test becomes essential. Here we add a word about each of these points.</p>
<p id="p-34"><em>First</em> , highway safety is a vital public interest. For decades, we have strained our vocal chords to give adequate expression to the stakes. We have called highway safety a "compelling interest," <em>Mackey</em> , <extracted-citation case-ids="6179408" index="47" url="https://cite.case.law/us/443/1/"><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/" aria-description="Citation for case: MacKey v. Montrym">443 U.S., at 19</a></span></extracted-citation>, <extracted-citation case-ids="6179408" index="48" url="https://cite.case.law/us/443/1/"><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/" aria-description="Citation for case: MacKey v. Montrym">99 S.Ct. 2612</a></span></extracted-citation> ; we have called it "paramount," <em><extracted-citation case-ids="6179408" index="49" url="https://cite.case.law/us/443/1/"><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/" aria-description="Citation for case: MacKey v. Montrym">id.</a></span></extracted-citation></em> , at 17, <extracted-citation case-ids="6179408" index="50" url="https://cite.case.law/us/443/1/"><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/" aria-description="Citation for case: MacKey v. Montrym">99 S.Ct. 2612</a></span></extracted-citation>. Twice we have referred to the effects of irresponsible driving as "slaughter" comparable to the ravages of war. <em>Breithaupt v. Abram</em> , <extracted-citation case-ids="6161761" index="51" url="https://cite.case.law/us/352/432/#p439"><span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/" aria-description="Citation for case: Breithaupt v. Abram">352 U.S. 432</a></span></extracted-citation>, 439, <extracted-citation case-ids="6161761" index="52" url="https://cite.case.law/us/352/432/#p439"><span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/" aria-description="Citation for case: Breithaupt v. Abram">77 S.Ct. 408</a></span></extracted-citation>, <extracted-citation case-ids="6161761" index="53" url="https://cite.case.law/us/352/432/#p439"><span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/" aria-description="Citation for case: Breithaupt v. Abram">1 L.Ed.2d 448</a></span></extracted-citation> (1957) ; <em>Perez v. Campbell</em> , <extracted-citation case-ids="11735156" index="54" url="https://cite.case.law/us/402/637/#p657"><span class="citation" data-id="9424589"><a href="/opinion/108350/perez-v-campbell/" aria-description="Citation for case: Perez. v. Campbell">402 U.S. 637</a></span></extracted-citation>, 657, 672, <extracted-citation case-ids="11735156" index="55" url="https://cite.case.law/us/402/637/#p657"><span class="citation" data-id="9424589"><a href="/opinion/108350/perez-v-campbell/" aria-description="Citation for case: Perez. v. Campbell">91 S.Ct. 1704</a></span></extracted-citation>, <extracted-citation case-ids="11735156" index="56" url="https://cite.case.law/us/402/637/#p657"><span class="citation" data-id="9424589"><a href="/opinion/108350/perez-v-campbell/" aria-description="Citation for case: Perez. v. Campbell">29 L.Ed.2d 233</a></span></extracted-citation> (1971) (Blackmun, J., concurring in result in part and dissenting in part). We have spoken of "carnage," <em>Neville</em> , <extracted-citation case-ids="6200055" index="57" url="https://cite.case.law/us/459/553/#p563"><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">459 U.S., at 558</a></span>-559</extracted-citation>, <extracted-citation case-ids="6200055" index="58" url="https://cite.case.law/us/459/553/#p563"><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">103 S.Ct. 916</a></span></extracted-citation>, and even "frightful carnage," <em>Tate v. Short</em> , <extracted-citation case-ids="11712570" index="59" url="https://cite.case.law/us/401/395/#p401"><span class="citation" data-id="9424475"><a href="/opinion/108282/tate-v-short/" aria-description="Citation for case: Tate v. Short">401 U.S. 395</a></span></extracted-citation>, 401, <extracted-citation case-ids="11712570" index="60" url="https://cite.case.law/us/401/395/#p401"><span class="citation" data-id="9424475"><a href="/opinion/108282/tate-v-short/" aria-description="Citation for case: Tate v. Short">91 S.Ct. 668</a></span></extracted-citation>, <extracted-citation case-ids="11712570" index="61" url="https://cite.case.law/us/401/395/#p401"><span class="citation" data-id="9424475"><a href="/opinion/108282/tate-v-short/" aria-description="Citation for case: Tate v. Short">28 L.Ed.2d 130</a></span></extracted-citation> (1971) (Blackmun, J., concurring). The frequency of preventable collisions, we have said, is "tragic," <em>Neville</em> , <em>supra</em> , at 558, <extracted-citation case-ids="6200055" index="62" url="https://cite.case.law/us/459/553/#p563"><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">103 S.Ct. 916</a></span></extracted-citation>, and "astounding,"</p>
<p id="p-35"><a class="page-label" data-citation-index="1" data-label="2536" href="#p2536" id="p2536">*2536</a><em>Breithaupt</em> , <em>supra</em> , at 439, <extracted-citation case-ids="6161761" index="63" url="https://cite.case.law/us/352/432/#p439"><span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/" aria-description="Citation for case: Breithaupt v. Abram">77 S.Ct. 408</a></span></extracted-citation>. And behind this fervent language lie chilling figures, all captured in the fact that from 1982 to 2016, alcohol-related accidents took roughly 10,000 to 20,000 lives in this Nation <em>every single year</em> . See National Highway Traffic Safety Admin. (NHTSA), Traffic Safety Facts 2016, p. 40 (May 2018). In the best years, that would add up to more than one fatality per hour.</p>
<p id="p-36"><em>Second</em> , when it comes to fighting these harms and promoting highway safety, federal and state lawmakers have long been convinced that specified BAC limits make a big difference. States resorted to these limits when earlier laws that included no "statistical definition of intoxication" proved ineffectual or hard to enforce. See <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , 579 U.S., at ---- - ----, <extracted-citation case-ids="12597986" index="64" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2167</a></span></extracted-citation>. The maximum permissible BAC, initially set at 0.15%, was first lowered to 0.10% and then to 0.08%. <em><extracted-citation case-ids="12597986" index="65" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Id.</a></span></extracted-citation></em> , at ----, ---- - ----, <extracted-citation case-ids="12597986" index="66" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/#2167" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2167</a></span>, 2168-69</extracted-citation>. Congress encouraged this process by conditioning the award of federal highway funds on the establishment of a BAC limit of 0.08%, see 23 U.S. C. § 163(a) ; <extracted-citation index="67" url="https://cite.case.law/citations/?q=23%20C.F.R.%20%C2%A7%201225.1"><span class="citation no-link">23 CFR § 1225.1</span></extracted-citation> (2012), and every State has adopted this limit.<footnotemark>4</footnotemark> Not only that, many States, including Wisconsin, have passed laws imposing increased penalties for recidivists or for drivers with a BAC level that exceeds a higher threshold. See <extracted-citation index="68" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%20346.65"><span class="citation no-link">Wis. Stat. § 346.65</span></extracted-citation>(2)(am) ; <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , 579 U.S., at ----, <extracted-citation case-ids="12597986" index="69" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2169</a></span></extracted-citation>.</p>
<p id="p-37">There is good reason to think this strategy has worked. As we noted in <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , these tougher measures corresponded with a dramatic drop in highway deaths and injuries: From the mid-1970's to the mid-1980's, "the number of annual fatalities averaged 25,000; by 2014 ..., the number had fallen to below 10,000." <em><extracted-citation case-ids="12597986" index="70" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Id.</a></span></extracted-citation></em> , at ----, <extracted-citation case-ids="12597986" index="71" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2169</a></span></extracted-citation>.</p>
<p id="p-38"><em>Third</em> , enforcing BAC limits obviously requires a test that is accurate enough to stand up in court, <em><extracted-citation case-ids="12597986" index="72" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">id.</a></span></extracted-citation></em> , at ---- - ----, <extracted-citation case-ids="12597986" index="73" url="https://cite.case.law/s-ct/136/2160/">136 S.Ct., at </extracted-citation>2167-68 ; see also <em>McNeely</em> , <extracted-citation case-ids="12697040" index="74" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 159</a></span>-160</extracted-citation>, <extracted-citation case-ids="12697040" index="75" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (plurality opinion). And we have recognized that "[e]xtraction of blood samples for testing is a highly effective means of" measuring "the influence of alcohol." <em>Schmerber</em> , <extracted-citation case-ids="12047531" index="76" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S., at 771</a></span></extracted-citation>, <extracted-citation case-ids="12047531" index="77" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>.</p>
<p id="p-39">Enforcement of BAC limits also requires prompt testing because it is "a biological certainty" that "[a]lcohol dissipates from the bloodstream at a rate of 0.01 percent to 0.025 percent per hour.... Evidence is literally disappearing by the minute." <em>McNeely</em> , <extracted-citation case-ids="12697040" index="78" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 169</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="79" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (opinion of ROBERTS, C.J.). As noted, the ephemeral nature of BAC was "essential to our holding in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> ," which itself allowed a warrantless blood test for BAC. <em><extracted-citation case-ids="12697040" index="80" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Id.</a></span></extracted-citation></em> , at 152, <extracted-citation case-ids="12697040" index="81" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (opinion of the Court). And even when we later held that the exigent-circumstances exception would not permit a warrantless blood draw in <em>every</em> drunk-driving case, we acknowledged that delays in BAC testing can "raise questions about ... accuracy." <em><extracted-citation case-ids="12697040" index="82" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">Id.</a></span></extracted-citation></em> , at 156, <extracted-citation case-ids="12697040" index="83" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>.</p>
<p id="p-40">It is no wonder, then, that the implied-consent laws that incentivize prompt BAC testing have been with us for 65 years and now exist in all 50 States. <em>Birchfield</em> , <em>supra</em> , at ----, <extracted-citation case-ids="12597986" index="84" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2169</a></span></extracted-citation>. These laws and the BAC tests they require are tightly linked to a regulatory scheme that serves the most pressing of interests.</p>
<p id="p-41">Finally, when a breath test is unavailable to promote those interests, "a blood draw becomes necessary."</p>
<p id="p-42"><a class="page-label" data-citation-index="1" data-label="2537" href="#p2537" id="p2537">*2537</a><em>McNeely</em> , <extracted-citation case-ids="12697040" index="85" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 170</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="86" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (opinion of ROBERTS, C.J.). Thus, in the case of unconscious drivers, who cannot blow into a breathalyzer, blood tests are essential for achieving the compelling interests described above.</p>
<p id="p-43">Indeed, not only is the link to pressing interests here tighter; the interests themselves are greater: Drivers who are drunk enough to pass out at the wheel or soon afterward pose a much greater risk. It would be perverse if the more wanton behavior were rewarded-if the more harrowing threat were harder to punish.</p>
<p id="p-44">For these reasons, there clearly is a "compelling need" for a blood test of drunk-driving suspects whose condition deprives officials of a reasonable opportunity to conduct a breath test. <em><extracted-citation case-ids="12697040" index="87" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="12697040" index="87" url="https://cite.case.law/us/569/141/#p149"> at 149</extracted-citation>, <extracted-citation case-ids="12697040" index="88" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (opinion of the Court) (internal quotation marks omitted). The only question left, under our exigency doctrine, is whether this compelling need justifies a warrantless search because there is, furthermore, " 'no time to secure a warrant.' " <em><extracted-citation case-ids="12697040" index="89" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">Ibid.</a></span></extracted-citation></em></p>
<p id="p-45">B</p>
<p id="p-46">We held that there was no time to secure a warrant before a blood test of a drunk-driving suspect in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> because the officer there could "reasonably have believed that he was confronted with an emergency, in which the delay necessary to obtain a warrant, under the circumstances, threatened the destruction of evidence." <extracted-citation case-ids="12047531" index="90" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S., at 770</a></span></extracted-citation>, <extracted-citation case-ids="12047531" index="91" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation> (internal quotation marks omitted). So even if the constant dissipation of BAC evidence <em>alone</em> does not create an exigency, see <em>McNeely</em> , <em>supra</em> , at 150-151, <extracted-citation case-ids="12697040" index="92" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>, <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> shows that it does so when combined with other pressing needs:</p>
<blockquote id="p-47">"We are told that [1] the percentage of alcohol in the blood begins to diminish shortly after drinking stops, as the body functions to eliminate it from the system. Particularly in a case such as this, where [2] time had to be taken to bring the accused to a hospital and to investigate the scene of the accident, there was no time to seek out a magistrate and secure a warrant. Given these special facts, we conclude that the attempt to secure evidence of blood-alcohol content in this case [without a warrant] was ... appropriate ...." <extracted-citation case-ids="12047531" index="93" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S., at 770</a></span>-771</extracted-citation>, <extracted-citation case-ids="12047531" index="94" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>.</blockquote>
<p id="p-48">Thus, exigency exists when (1) BAC evidence is dissipating and (2) some other factor creates pressing health, safety, or law enforcement needs that would take priority over a warrant application. Both conditions are met when a drunk-driving suspect is unconscious, so <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> controls: With such suspects, too, a warrantless blood draw is lawful.</p>
<p id="p-49">1</p>
<p id="p-50">In <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> , the extra factor giving rise to urgent needs that would only add to the delay caused by a warrant application was a car accident; here it is the driver's unconsciousness. Indeed, unconsciousness does not just create pressing needs; it is <em>itself</em> a medical emergency.<footnotemark>5</footnotemark> It means that the suspect will have to be rushed to the hospital or similar facility not just for the blood test itself but for urgent medical care.<footnotemark>6</footnotemark> Police can reasonably anticipate that such a driver might require monitoring, <a class="page-label" data-citation-index="1" data-label="2538" href="#p2538" id="p2538">*2538</a>positioning, and support on the way to the hospital;<footnotemark>7</footnotemark> that his blood may be drawn anyway, for diagnostic purposes, immediately on arrival;<footnotemark>8</footnotemark> and that immediate medical treatment could delay (or otherwise distort the results of) a blood draw conducted later, upon receipt of a warrant, thus reducing its evidentiary value. See <em>McNeely</em> , <em>supra</em> , at 156, <extracted-citation case-ids="12697040" index="95" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (plurality opinion). All of that sets this case apart from the uncomplicated drunk-driving scenarios addressed in <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> . Just as the ramifications of a car accident pushed <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> over the line into exigency, so does the condition of an unconscious driver bring his blood draw under the exception. In such a case, as in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> , an officer could "reasonably have believed that he was confronted with an emergency." <extracted-citation case-ids="12047531" index="96" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S., at 770</a></span></extracted-citation>, <extracted-citation case-ids="12047531" index="97" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>.</p>
<p id="p-51">Indeed, in many unconscious-driver cases, the exigency will be <em>more</em> acute, as elaborated in the briefing and argument in this case. A driver so drunk as to lose consciousness is quite likely to crash, especially if he passes out before managing to park. And then the accident might give officers a slew of urgent tasks beyond that of securing (and working around) medical care for the suspect. Police may have to ensure that others who are injured receive prompt medical attention; they may have to provide first aid themselves until medical personnel arrive at the scene. In some cases, they may have to deal with fatalities. They may have to preserve evidence at the scene and block or redirect traffic to prevent further accidents. These pressing matters, too, would require responsible officers to put off applying for a warrant, and that would only exacerbate the delay-and imprecision-of any subsequent BAC test.</p>
<p id="p-52">In sum, all these rival priorities would put officers, who must often engage in a form of triage, to a dilemma. It would force them to choose between prioritizing a warrant application, to the detriment of critical health and safety needs, and delaying the warrant application, and thus the BAC test, to the detriment of its evidentiary value and all the compelling interests served by BAC limits. This is just the kind of scenario for which the exigency rule was born-just the kind of grim dilemma it lives to dissolve.</p>
<p id="p-53">2</p>
<p id="p-54">Mitchell objects that a warrantless search is unnecessary in cases involving unconscious drivers because warrants these days can be obtained faster and <a class="page-label" data-citation-index="1" data-label="2539" href="#p2539" id="p2539">*2539</a>more easily. But even in our age of rapid communication,</p>
<blockquote id="p-55">"[w]arrants inevitably take some time for police officers or prosecutors to complete and for magistrate judges to review. Telephonic and electronic warrants may still require officers to follow time-consuming formalities designed to create an adequate record, such as preparing a duplicate warrant before calling the magistrate judge.... And improvements in communications technology do not guarantee that a magistrate judge will be available when an officer needs a warrant after making a late-night arrest." <em>McNeely</em> , <extracted-citation case-ids="12697040" index="98" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 155</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="99" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>.</blockquote>
<p id="p-56">In other words, with better technology, the time required has shrunk, but it has not disappeared. In the emergency scenarios created by unconscious drivers, forcing police to put off other tasks for even a relatively short period of time may have terrible collateral costs. That is just what it means for these situations to <em>be</em> emergencies.</p>
<p id="p-57">IV</p>
<p id="p-58">When police have probable cause to believe a person has committed a drunk-driving offense and the driver's unconsciousness or stupor requires him to be taken to the hospital or similar facility before police have a reasonable opportunity to administer a standard evidentiary breath test, they may almost always order a warrantless blood test to measure the driver's BAC without offending the Fourth Amendment. We do not rule out the possibility that in an unusual case a defendant would be able to show that his blood would not have been drawn if police had not been seeking BAC information, and that police could not have reasonably judged that a warrant application would interfere with other pressing needs or duties. Because Mitchell did not have a chance to attempt to make that showing, a remand for that purpose is necessary.</p>
<p id="p-59">* * *</p>
<p id="p-60">The judgment of the Supreme Court of Wisconsin is vacated, and the case is remanded for further proceedings.</p>
<p id="p-61">It is so ordered.</p>
<p id="p-62">Justice THOMAS, concurring in the judgment.</p>
<p id="p-63">Today, the plurality adopts a difficult-to-administer rule: Exigent circumstances are generally present when police encounter a person suspected of drunk driving-except when they aren't. Compare <em>ante</em> , at 2537, with <em>ante</em> , at 2539. The plurality's presumption will rarely be rebutted, but it will nevertheless burden both officers and courts who must attempt to apply it. "The better (and far simpler) way to resolve" this case is to apply "the <em>per se</em> rule" I proposed in <em>Missouri v. McNeely</em> , <extracted-citation case-ids="12697040" index="100" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S. 141</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="101" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="102" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">185 L.Ed.2d 696</a></span></extracted-citation> (2013) (dissenting opinion). <em>Birchfield</em> v. <em>North Dakota</em> , 579 U.S. ----, ----, <extracted-citation case-ids="12597986" index="103" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct. 2160</a></span></extracted-citation>, 2197, <extracted-citation case-ids="12597986" index="104" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">195 L.Ed.2d 560</a></span></extracted-citation> (2016) (THOMAS, J., concurring in judgment in part and dissenting in part). Under that rule, the natural metabolization of alcohol in the blood stream " 'creates an exigency once police have probable cause to believe the driver is drunk,' " regardless of whether the driver is conscious. <em><extracted-citation case-ids="12597986" index="105" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12597986" index="106" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2198</a></span></extracted-citation>. Because I am of the view that the Wisconsin Supreme Court should apply that rule on remand, I concur only in the judgment.</p>
<p id="p-64">I</p>
<p id="p-65">The Fourth Amendment provides that "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated." Although the Fourth Amendment does not, by its text, <a class="page-label" data-citation-index="1" data-label="2540" href="#p2540" id="p2540">*2540</a>require that searches be supported by a warrant, see <em>Groh v. Ramirez</em> , <extracted-citation case-ids="8897610" index="107" url="https://cite.case.law/us/540/551/#p571"><span class="citation" data-id="9434540"><a href="/opinion/131161/groh-v-ramirez/" aria-description="Citation for case: Groh v. Ramirez">540 U.S. 551</a></span></extracted-citation>, 571-573, <extracted-citation case-ids="8897610" index="108" url="https://cite.case.law/us/540/551/#p571"><span class="citation" data-id="9434540"><a href="/opinion/131161/groh-v-ramirez/" aria-description="Citation for case: Groh v. Ramirez">124 S.Ct. 1284</a></span></extracted-citation>, <extracted-citation case-ids="8897610" index="109" url="https://cite.case.law/us/540/551/#p571"><span class="citation" data-id="9434540"><a href="/opinion/131161/groh-v-ramirez/" aria-description="Citation for case: Groh v. Ramirez">157 L.Ed.2d 1068</a></span></extracted-citation> (2004) (THOMAS, J., dissenting), "this Court has inferred that a warrant must generally be secured" for a search to comply with the Fourth Amendment, <em>Kentucky v. King</em> , <extracted-citation case-ids="5911971,12458997" index="110" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">563 U.S. 452</a></span></extracted-citation>, 459, <extracted-citation case-ids="5911971,12458997" index="111" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">131 S.Ct. 1849</a></span></extracted-citation>, <extracted-citation case-ids="5911971,12458997" index="112" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">179 L.Ed.2d 865</a></span></extracted-citation> (2011). We have also recognized, however, that this warrant presumption "may be overcome in some circumstances because '[t]he ultimate touchstone of the Fourth Amendment is "reasonableness." ' " <em><extracted-citation case-ids="5911971,12458997" index="113" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">Ibid.</a></span></extracted-citation></em> Accordingly, we have held that "the warrant requirement is subject to certain reasonable exceptions." <em><extracted-citation case-ids="5911971,12458997" index="114" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">Ibid.</a></span></extracted-citation></em></p>
<p id="p-66">In recent years, this Court has twice considered whether warrantless blood draws fall within an exception to the warrant requirement. First, in <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> , a divided court held that the natural metabolization of alcohol in the bloodstream does not present a <em>per se</em> exigency that justifies an exception to the Fourth Amendment's warrant requirement. <extracted-citation case-ids="12697040" index="115" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 145</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="116" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>. Then, in <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , we held that blood draws may not be administered as a search incident to a lawful arrest for drunk driving. 579 U.S., at ----, <extracted-citation case-ids="12597986" index="117" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2184</a></span>-85</extracted-citation>. The question we face in this case is whether the blood draw here fell within one of the "reasonable exceptions" to the warrant requirement.</p>
<p id="p-67">II</p>
<p id="p-68">The "exigent circumstances" exception applies when "the needs of law enforcement [are] so compelling that [a] warrantless search is objectively reasonable under the Fourth Amendment." <em>King</em> , <extracted-citation case-ids="5911971,12458997" index="118" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">563 U.S., at 460</a></span></extracted-citation>, <extracted-citation case-ids="5911971,12458997" index="119" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">131 S.Ct. 1849</a></span></extracted-citation> (internal quotation marks omitted). Applying this doctrine, the Court has held that officers may conduct a warrantless search when failure to act would result in "the imminent destruction of evidence." <em><extracted-citation case-ids="5911971,12458997" index="120" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">Ibid.</a></span></extracted-citation></em> (internal quotation marks omitted).</p>
<p id="p-69">As I have explained before, "the imminent destruction of evidence" is a risk in every drunk-driving arrest and thus "implicates the exigent-circumstances doctrine." <em>McNeely</em> , <extracted-citation case-ids="12697040" index="121" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 178</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="122" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>. "Once police arrest a suspect for drunk driving, each passing minute eliminates probative evidence of the crime" as alcohol dissipates from the bloodstream. <em><extracted-citation case-ids="12697040" index="123" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">Id.</a></span></extracted-citation></em> , at 177, <extracted-citation case-ids="12697040" index="124" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>. In many States, this "rapid destruction of evidence," <em><extracted-citation case-ids="12697040" index="125" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">id.,</a></span></extracted-citation></em><extracted-citation case-ids="12697040" index="125" url="https://cite.case.law/us/569/141/#p149"> at 178</extracted-citation>, <extracted-citation case-ids="12697040" index="126" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>, is particularly problematic because the penalty for drunk driving depends in part on the driver's blood alcohol concentration, see <em>ante</em> , at 2536. Because the provisions of Wisconsin law at issue here allow blood draws only when the driver is suspected of impaired driving, <em>ante</em> , at 2531 - 2532, they fit easily within the exigency exception to the warrant requirement.</p>
<p id="p-70">Instead of adopting this straightforward rule, the plurality makes a flawed distinction between ordinary drunk-driving cases in which blood alcohol concentration evidence "is dissipating" and those that also include "some other [pressing] factor." <em>Ante</em> , at 2533, 2537, 2539. But whether "some other factor creates pressing health, safety, or law-enforcement needs that would take priority over a warrant application" is irrelevant. <em>Ante</em> , at 2537. When police have probable cause to conclude that an individual was driving drunk, probative evidence is dissipating by the minute. And that evidence dissipates regardless of whether police had another reason to draw the driver's blood or whether "a warrant application would interfere with other pressing needs or duties." <em>Ante</em> , at 2539. The destruction of evidence alone is sufficient to justify a warrantless search based on exigent circumstances. See generally <a class="page-label" data-citation-index="1" data-label="2541" href="#p2541" id="p2541">*2541</a><em>McNeely</em> , <extracted-citation case-ids="12697040" index="127" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 176</a></span>-179</extracted-citation>, <extracted-citation case-ids="12697040" index="128" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (opinion of THOMAS, J.).</p>
<p id="p-71">Presumably, the plurality draws these lines to avoid overturning <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> . See <em><extracted-citation case-ids="12697040" index="129" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">id.</a></span></extracted-citation></em> , at 156, <extracted-citation case-ids="12697040" index="130" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (majority opinion) (holding that "the natural dissipation of alcohol in the blood" does not "categorically" support a finding of exigency). But <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> was wrongly decided, see <em><extracted-citation case-ids="12697040" index="131" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">id.</a></span></extracted-citation></em> , at 176-183, <extracted-citation case-ids="12697040" index="132" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (opinion of THOMAS, J.), and our decision in <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> has already undermined its rationale. Specifically, the Court determined in <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> that "[t]he context of blood testing is different in critical respects from other destruction-of-evidence cases in which the police are truly confronted with a now or never situation." <extracted-citation case-ids="12697040" index="133" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 153</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="134" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (majority opinion) (internal quotation marks omitted). But the Court stated in <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> that a distinction between "an arrestee's active destruction of evidence and the loss of evidence due to a natural process makes little sense." 579 U.S., at ----, <extracted-citation case-ids="12597986" index="135" url="https://cite.case.law/s-ct/136/2160/">136 S.Ct., at </extracted-citation>2182 ; see also <em>ante</em> , at 2536 - 2537. Moreover, to the extent <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> was grounded in the belief that a <em>per se</em> rule was inconsistent with the "case by case," "totality of the circumstances" analysis ordinarily applied in exigent-circumstances cases, see <extracted-citation case-ids="12697040" index="136" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 156</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="137" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>, that rationale was suspect from the start. That the exigent-circumstances exception might ordinarily require "an evaluation of the particular facts of each case," <em>Birchfield</em> , <em>supra</em> , at ----, <extracted-citation case-ids="12597986" index="138" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2183</a></span></extracted-citation>, does not foreclose us from recognizing that a certain, dispositive fact is always present in some categories of cases. In other words, acknowledging that destruction of evidence is at issue in every drunk-driving case does not undermine the general totality-of-the-circumstances approach that <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> and <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> endorsed. Cf. <em>ante</em> , at 2535, n. 3.</p>
<p id="p-72">* * *</p>
<p id="p-73">The Court has consistently held that police officers may perform searches without a warrant when destruction of evidence is a risk. <em>United States v. Banks</em> , <extracted-citation case-ids="8896811" index="139" url="https://cite.case.law/us/540/31/#p38"><span class="citation" data-id="131146"><a href="/opinion/131146/united-states-v-banks/" aria-description="Citation for case: United States v. Banks">540 U.S. 31</a></span></extracted-citation>, 38, <extracted-citation case-ids="8896811" index="140" url="https://cite.case.law/us/540/31/#p38"><span class="citation" data-id="131146"><a href="/opinion/131146/united-states-v-banks/" aria-description="Citation for case: United States v. Banks">124 S.Ct. 521</a></span></extracted-citation>, <extracted-citation case-ids="8896811" index="141" url="https://cite.case.law/us/540/31/#p38"><span class="citation" data-id="131146"><a href="/opinion/131146/united-states-v-banks/" aria-description="Citation for case: United States v. Banks">157 L.Ed.2d 343</a></span></extracted-citation> (2003) ; <em>Richards v. Wisconsin</em> , <extracted-citation case-ids="11652004" index="142" url="https://cite.case.law/us/520/385/#p395"><span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">520 U.S. 385</a></span></extracted-citation>, 395, <extracted-citation case-ids="11652004" index="143" url="https://cite.case.law/us/520/385/#p395"><span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">117 S.Ct. 1416</a></span></extracted-citation>, <extracted-citation case-ids="11652004" index="144" url="https://cite.case.law/us/520/385/#p395"><span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">137 L.Ed.2d 615</a></span></extracted-citation> (1997) ; <em>Cupp v. Murphy</em> , <extracted-citation case-ids="6172131" index="145" url="https://cite.case.law/us/412/291/#p295"><span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/" aria-description="Citation for case: Cupp v. Murphy">412 U.S. 291</a></span></extracted-citation>, 295-296, <extracted-citation case-ids="6172131" index="146" url="https://cite.case.law/us/412/291/#p295"><span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/" aria-description="Citation for case: Cupp v. Murphy">93 S.Ct. 2000</a></span></extracted-citation>, <extracted-citation case-ids="6172131" index="147" url="https://cite.case.law/us/412/291/#p295"><span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/" aria-description="Citation for case: Cupp v. Murphy">36 L.Ed.2d 900</a></span></extracted-citation> (1973) ; <em>Schmerber v. California</em> , <extracted-citation case-ids="12047531" index="148" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S. 757</a></span></extracted-citation>, 770-772, <extracted-citation case-ids="12047531" index="149" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>, <extracted-citation case-ids="12047531" index="150" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">16 L.Ed.2d 908</a></span></extracted-citation> (1966). The rule should be no different in drunk-driving cases. Because the plurality instead adopts a rule more likely to confuse than clarify, I concur only in the judgment.</p>
<p id="p-74">Justice SOTOMAYOR, with whom Justice GINSBURG and Justice KAGAN join, dissenting.</p>
<p id="p-75">The plurality's decision rests on the false premise that today's holding is necessary to spare law enforcement from a choice between attending to emergency situations and securing evidence used to enforce state drunk-driving laws. Not so. To be sure, drunk driving poses significant dangers that Wisconsin and other States must be able to curb. But the question here is narrow: What must police do before ordering a blood draw of a person suspected of drunk driving who has become unconscious? Under the Fourth Amendment, the answer is clear: If there is time, get a warrant.</p>
<p id="p-76">The State of Wisconsin conceded in the state courts that it had time to get a warrant to draw Gerald Mitchell's blood, and that should be the end of the matter. Because the plurality needlessly casts aside the established protections of the warrant requirement in favor of a brand new presumption of exigent circumstances that Wisconsin does not urge, that the state courts did not consider, and that <a class="page-label" data-citation-index="1" data-label="2542" href="#p2542" id="p2542">*2542</a>contravenes this Court's precedent, I respectfully dissent.</p>
<p id="p-77">I</p>
<p id="p-78">In May 2013, Wisconsin police received a report that Gerald Mitchell, seemingly intoxicated, had driven away from his apartment building. A police officer later found Mitchell walking near a lake, slurring his speech and walking with difficulty. His van was parked nearby. The officer administered a preliminary breath test, which revealed a blood-alcohol concentration (BAC) of 0.24%. The officer arrested Mitchell for operating a vehicle while intoxicated.</p>
<p id="p-79">Once at the police station, the officer placed Mitchell in a holding cell, where Mitchell began to drift into either sleep or unconsciousness. At that point, the officer decided against administering a more definitive breath test and instead took Mitchell to the hospital for a blood test. Mitchell became fully unconscious on the way. At the hospital, the officer read Mitchell a notice, required by Wisconsin's so-called "implied consent" law, which gave him the opportunity to refuse BAC testing. See <extracted-citation index="151" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305"><span class="citation no-link">Wis. Stat. § 343.305</span></extracted-citation> (2016). But Mitchell was too incapacitated to respond. The officer then asked the hospital to test Mitchell's blood. Mitchell's blood was drawn about 90 minutes after his arrest, and the test revealed a BAC of 0.22%<footnotemark>1</footnotemark> At no point did the officer attempt to secure a warrant.</p>
<p id="p-80">Mitchell was charged with violating two Wisconsin drunk-driving laws. See §§ 346.63(1)(a), (b). He moved to suppress the blood-test results, arguing that the warrantless blood draw was an unreasonable search under the Fourth Amendment. In response, Wisconsin conceded that exigent circumstances did not justify the warrantless blood draw. As the State's attorney told the trial court, "There is nothing to suggest that this is a blood draw on a[n] exigent circumstances situation when there has been a concern for exigency. This is not that case." App. 134. Instead, Wisconsin argued that the warrantless blood draw was lawful because of Wisconsin's implied-consent statute. <em><extracted-citation index="152" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305">Id.,</extracted-citation></em><extracted-citation index="152" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305"> at 133</extracted-citation>.</p>
<p id="p-81">The trial court denied Mitchell's motion to suppress, and a jury convicted him of the charged offenses. On appeal, the State Court of Appeals noted that Wisconsin had "expressly disclaimed that it was relying on exigent circumstances to justify the draw," <em><extracted-citation index="153" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305">id.,</extracted-citation></em><extracted-citation index="153" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305"> at 64</extracted-citation>, and that this case offered a chance to clarify the law on implied consent because the case "is not susceptible to resolution on the ground of exigent circumstances," <em><extracted-citation index="154" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305">id.,</extracted-citation></em><extracted-citation index="154" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305"> at 66</extracted-citation>. The Court of Appeals then certified the appeal to the Wisconsin Supreme Court, identifying the sole issue on appeal as "whether the warrantless blood draw of an unconscious motorist pursuant to Wisconsin's implied consent law, where no exigent circumstances exist or have been argued, violates the Fourth Amendment." <em><extracted-citation index="155" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305">Id.,</extracted-citation></em><extracted-citation index="155" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305"> at 61</extracted-citation>.</p>
<p id="p-82">On certification from the state appellate court, the Supreme Court of Wisconsin upheld the search.<footnotemark>2</footnotemark> The Court granted certiorari to decide whether a statute like Wisconsin's, which allows police to draw <a class="page-label" data-citation-index="1" data-label="2543" href="#p2543" id="p2543">*2543</a>blood from an unconscious drunk-driving suspect, provides an exception to the Fourth Amendment's warrant requirement.</p>
<p id="p-83">II</p>
<p id="p-84">The Fourth Amendment guarantees "[t]he right of the people to be secure in their persons ... against unreasonable searches and seizures." When the aim of a search is to uncover evidence of a crime, the Fourth Amendment generally requires police to obtain a warrant. <em>Vernonia School Dist. 47J v. Acton</em> , <extracted-citation case-ids="1564392" index="156" url="https://cite.case.law/us/515/646/#p653"><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U.S. 646</a></span></extracted-citation>, 653, <extracted-citation case-ids="1564392" index="157" url="https://cite.case.law/us/515/646/#p653"><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">115 S.Ct. 2386</a></span></extracted-citation>, <extracted-citation case-ids="1564392" index="158" url="https://cite.case.law/us/515/646/#p653"><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">132 L.Ed.2d 564</a></span></extracted-citation> (1995).</p>
<p id="p-85">The warrant requirement is not a mere formality; it ensures that necessary judgment calls are made " 'by a neutral and detached magistrate,' " not " 'by the officer engaged in the often competitive enterprise of ferreting out crime.' " <em>Schmerber v. California</em> , <extracted-citation case-ids="12047531" index="159" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S. 757</a></span></extracted-citation>, 770, <extracted-citation case-ids="12047531" index="160" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>, <extracted-citation case-ids="12047531" index="161" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">16 L.Ed.2d 908</a></span></extracted-citation> (1966). A warrant thus serves as a check against searches that violate the Fourth Amendment by ensuring that a police officer is not made the sole interpreter of the Constitution's protections. Accordingly, a search conducted without a warrant is "<em>per se</em> unreasonable under the Fourth Amendment-subject only to a few specifically established and well-delineated exceptions." <em>Katz v. United States</em> , <extracted-citation case-ids="11339173" index="162" url="https://cite.case.law/us/389/347/#p357"><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U.S. 347</a></span></extracted-citation>, 357, <extracted-citation case-ids="11339173" index="163" url="https://cite.case.law/us/389/347/#p357"><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span></extracted-citation>, <extracted-citation case-ids="11339173" index="164" url="https://cite.case.law/us/389/347/#p357"><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L.Ed.2d 576</a></span></extracted-citation> (1967) (footnote omitted); see <em>Riley v. California</em> , <extracted-citation index="165" url="https://cite.case.law/citations/?q=573%20U.S.%20373"><span class="citation no-link">573 U.S. 373</span></extracted-citation>, 382, <extracted-citation case-ids="12581677" index="166" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. 2473</a></span></extracted-citation>, <extracted-citation case-ids="12581677" index="167" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">189 L.Ed.2d 430</a></span></extracted-citation> (2014) ("In the absence of a warrant, a search is reasonable only if it falls within a specific exception to the warrant requirement").</p>
<p id="p-86">The carefully circumscribed exceptions to the warrant requirement, as relevant here, include the exigent-circumstances exception, which applies when " 'the exigencies of the situation' make the needs of law enforcement so compelling that [a] warrantless search is objectively reasonable," <em>Kentucky v. King</em> , <extracted-citation case-ids="5911971,12458997" index="168" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">563 U.S. 452</a></span></extracted-citation>, 460, <extracted-citation case-ids="5911971,12458997" index="169" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">131 S.Ct. 1849</a></span></extracted-citation>, <extracted-citation case-ids="5911971,12458997" index="170" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">179 L.Ed.2d 865</a></span></extracted-citation> (2011) (some internal quotation marks omitted); the consent exception for cases where voluntary consent is given to the search, see, <em>e.g.,</em> <em>Georgia v. Randolph</em> , <extracted-citation case-ids="3275967" index="171" url="https://cite.case.law/us/547/103/#p109"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">547 U.S. 103</a></span></extracted-citation>, 109, <extracted-citation case-ids="3275967" index="172" url="https://cite.case.law/us/547/103/#p109"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation>, <extracted-citation case-ids="3275967" index="173" url="https://cite.case.law/us/547/103/#p109"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">164 L.Ed.2d 208</a></span></extracted-citation> (2006) ; and the exception for "searches incident to arrest," see, <em>e.g.,</em> <em>Riley</em> , <extracted-citation index="174" url="https://cite.case.law/citations/?q=573%20U.S.%20373">573 U.S., at 382</extracted-citation>, <extracted-citation case-ids="12581677" index="175" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. 2473</a></span></extracted-citation>.</p>
<p id="p-87">A</p>
<p id="p-88">Blood draws are "searches" under the Fourth Amendment. The act of drawing a person's blood, whether or not he is unconscious, "involve[s] a compelled physical intrusion beneath [the] skin and into [a person's] veins," all for the purpose of extracting evidence for a criminal investigation. <em>Missouri v. McNeely</em> , <extracted-citation case-ids="12697040" index="176" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S. 141</a></span></extracted-citation>, 148, <extracted-citation case-ids="12697040" index="177" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="178" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">185 L.Ed.2d 696</a></span></extracted-citation> (2013). The blood draw also "places in the hands of law enforcement authorities a sample that can be preserved and from which it is possible to extract information beyond a simple BAC reading," <em>Birchfield</em> v. <em>North Dakota</em> , 579 U.S. ----, ----, <extracted-citation case-ids="12597986" index="179" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct. 2160</a></span></extracted-citation>, 2178, <extracted-citation case-ids="12597986" index="180" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">195 L.Ed.2d 560</a></span></extracted-citation> (2016), such as whether a person is pregnant, is taking certain medications, or suffers from an illness. That "invasion of bodily integrity" disturbs "an individual's 'most personal and deep-rooted expectations of privacy.' " <em>McNeely</em> , <extracted-citation case-ids="12697040" index="181" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 148</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="182" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>.</p>
<p id="p-89">For decades, this Court has stayed true to the Fourth Amendment's warrant requirement and the narrowness of its exceptions, even in the face of attempts categorically to exempt blood testing from its protections. In <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> , a man was hospitalized following a car accident. <extracted-citation case-ids="12047531" index="183" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S., at 758</a></span></extracted-citation>, <extracted-citation case-ids="12047531" index="184" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>. At the scene of the accident and later at the hospital, a police officer noticed signs of intoxication, and he arrested Schmerber for drunk driving.</p>
<p id="p-90"><a class="page-label" data-citation-index="1" data-label="2544" href="#p2544" id="p2544">*2544</a><em><extracted-citation case-ids="12047531" index="185" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="12047531" index="185" url="https://cite.case.law/us/384/757/#p765"> at 768-769</extracted-citation>, <extracted-citation case-ids="12047531" index="186" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>. Without obtaining a warrant, the officer ordered a blood draw to measure Schmerber's BAC, and Schmerber later challenged the blood test as an unreasonable search under the Fourth Amendment. <em><extracted-citation case-ids="12047531" index="187" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="12047531" index="187" url="https://cite.case.law/us/384/757/#p765"> at 758-759</extracted-citation>, <extracted-citation case-ids="12047531" index="188" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>. The Court reinforced that search warrants are "ordinarily required ... where intrusions into the human body are concerned," <em><extracted-citation case-ids="12047531" index="189" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">id.,</a></span></extracted-citation></em><extracted-citation case-ids="12047531" index="189" url="https://cite.case.law/us/384/757/#p765"> at 770</extracted-citation>, <extracted-citation case-ids="12047531" index="190" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>, but it ultimately held that exigent circumstances justified the particular search at issue because certain "special facts"-namely, an unusual delay caused by the investigation at the scene and the subsequent hospital trip-left the police with "no time to seek out a magistrate and secure a warrant" before losing the evidence. <em><extracted-citation case-ids="12047531" index="191" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="12047531" index="191" url="https://cite.case.law/us/384/757/#p765"> at 770-771</extracted-citation>, <extracted-citation case-ids="12047531" index="192" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>.</p>
<p id="p-91">More recently, in <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> , the Court held that blood tests are not categorically exempt from the warrant requirement, explaining that exigency "must be determined case by case based on the totality of the circumstances." <extracted-citation case-ids="12697040" index="193" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 156</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="194" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>. "[T]he natural dissipation of alcohol in the blood may support a finding of exigency in a specific case," but "it does not do so categorically." <em>Ibid</em> . If officers "can reasonably obtain a warrant before a blood sample can be drawn without significantly undermining the efficacy of the search," the Court made clear, "the Fourth Amendment mandates that they do so." <em><extracted-citation case-ids="12697040" index="195" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="12697040" index="195" url="https://cite.case.law/us/569/141/#p149"> at 152</extracted-citation>, <extracted-citation case-ids="12697040" index="196" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> ; see <em><extracted-citation case-ids="12697040" index="197" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">id.,</a></span></extracted-citation></em><extracted-citation case-ids="12697040" index="197" url="https://cite.case.law/us/569/141/#p149"> at 167</extracted-citation>, <extracted-citation case-ids="12697040" index="198" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (ROBERTS, C.J., concurring in part and dissenting in part) ("The natural dissipation of alcohol in the bloodstream ... would qualify as an exigent circumstance, except that there may be time to secure a warrant before blood can be drawn. If there is, an officer must seek a warrant").</p>
<p id="p-92">In <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , the Court rejected another attempt categorically to exempt blood draws from the warrant requirement. 579 U.S., at ----, <extracted-citation case-ids="12597986" index="199" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2184</a></span></extracted-citation>. The Court considered whether warrantless breath and blood tests to determine a person's BAC level were permissible as searches incident to arrest. The Court held that warrantless breath tests were permitted because they are insufficiently intrusive to outweigh the State's need for BAC testing. See <em><extracted-citation case-ids="12597986" index="200" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">ibid.</a></span></extracted-citation></em> As to blood tests, however, the Court held the opposite: Because they are significantly more intrusive than breath tests, the warrant requirement applies unless particular exigent circumstances prevent officers from obtaining a warrant. <em><extracted-citation case-ids="12597986" index="201" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Ibid.</a></span></extracted-citation></em> ; see <em><extracted-citation case-ids="12597986" index="202" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">id.</a></span></extracted-citation></em> , at ----, <extracted-citation case-ids="12597986" index="203" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/#2184" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2184</a></span></extracted-citation> ("Nothing prevents the police from seeking a warrant for a blood test when there is sufficient time to do so in the particular circumstances or from relying on the exigent circumstances exception ... when there is not").<footnotemark>3</footnotemark></p>
<p id="p-93">B</p>
<p id="p-94">Those cases resolve this one. <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> and <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> establish that there is no categorical exigency exception for blood draws, although exigent circumstances might justify a warrantless blood draw on the facts of a particular case. And from <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , we know that warrantless blood draws cannot be justified as searches incident to arrest. The lesson is straightforward: Unless there is too little time to do so, police officers must get a warrant before <a class="page-label" data-citation-index="1" data-label="2545" href="#p2545" id="p2545">*2545</a>ordering a blood draw. See 579 U.S., at ----, <extracted-citation case-ids="12597986" index="204" url="https://cite.case.law/s-ct/136/2160/">136 S.Ct., at </extracted-citation>2184 ; <em>McNeely</em> , <extracted-citation case-ids="12697040" index="205" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 152</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="206" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>.</p>
<p id="p-95">Against this precedential backdrop, Wisconsin's primary argument has always been that Mitchell consented to the blood draw through the State's "implied-consent law." Under that statute, a motorist who drives on the State's roads is "deemed" to have consented to a blood draw, breath test, and urine test, and that supposed consent allows a warrantless blood draw from an unconscious motorist as long as the police have probable cause to believe that the motorist has violated one of the State's impaired driving statutes. See <extracted-citation index="207" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305"><span class="citation no-link">Wis. Stat. § 343.305</span></extracted-citation>.</p>
<p id="p-96">The plurality does not rely on the consent exception here. See <em>ante</em> , at 2532. With that sliver of the plurality's reasoning I agree. I would go further and hold that the state statute, however phrased, cannot itself create the actual and informed consent that the Fourth Amendment requires. See <em>Randolph</em> , <extracted-citation case-ids="3275967" index="208" url="https://cite.case.law/us/547/103/#p109"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">547 U.S., at 109</a></span></extracted-citation>, <extracted-citation case-ids="3275967" index="209" url="https://cite.case.law/us/547/103/#p109"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation> (describing the "voluntary consent" exception to the warrant requirement as " 'jealously and carefully drawn' "); <em>Bumper v. North Carolina</em> , <extracted-citation case-ids="1767611" index="210" url="https://cite.case.law/us/391/543/#p548"><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">391 U.S. 543</a></span></extracted-citation>, 548, <extracted-citation case-ids="1767611" index="211" url="https://cite.case.law/us/391/543/#p548"><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">88 S.Ct. 1788</a></span></extracted-citation>, <extracted-citation case-ids="1767611" index="212" url="https://cite.case.law/us/391/543/#p548"><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">20 L.Ed.2d 797</a></span></extracted-citation> (1968) (stating that consent must be "freely and voluntarily given"); see also <em>Schneckloth v. Bustamonte</em> , <extracted-citation case-ids="6172008" index="213" url="https://cite.case.law/us/412/218/#p226"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218</a></span></extracted-citation>, 226-227, <extracted-citation case-ids="6172008" index="214" url="https://cite.case.law/us/412/218/#p226"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041</a></span></extracted-citation>, <extracted-citation case-ids="6172008" index="215" url="https://cite.case.law/us/412/218/#p226"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L.Ed.2d 854</a></span></extracted-citation> (1973) (explaining that the existence of consent must "be determined from the totality of all the circumstances"). That should be the end of this case.</p>
<p id="p-97">III</p>
<p id="p-98">Rather than simply applying this Court's precedents to address-and reject-Wisconsin's implied-consent theory, the plurality today takes the extraordinary step of relying on an issue, exigency, that Wisconsin has affirmatively waived.<footnotemark>4</footnotemark> Wisconsin has not once, in any of its briefing before this Court or the state courts, argued that exigent circumstances were present here. In fact, in the state proceedings, Wisconsin "conceded" that the exigency exception does not justify the warrantless blood draw in this case. App. 66; see <extracted-citation case-ids="12556993" index="216" url="https://cite.case.law/nw2d/914/151/"><span class="citation" data-id="9886762"><a href="/opinion/4513691/state-v-gerald-p-mitchell/" aria-description="Citation for case: State v. Gerald P. Mitchell">2018 WI 84</a></span></extracted-citation>, ¶12, <extracted-citation case-ids="12556993" index="217" url="https://cite.case.law/nw2d/914/151/"><span class="citation" data-id="9886762"><a href="/opinion/4513691/state-v-gerald-p-mitchell/" aria-description="Citation for case: State v. Gerald P. Mitchell">383 Wis.2d 192</a></span></extracted-citation>, 202, <extracted-citation case-ids="12556993" index="218" url="https://cite.case.law/nw2d/914/151/"><span class="citation" data-id="9886762"><a href="/opinion/4513691/state-v-gerald-p-mitchell/" aria-description="Citation for case: State v. Gerald P. Mitchell">914 N.W.2d 151</a></span></extracted-citation>, 155 ("The State expressly stated that it was not relying on exigent circumstances to justify the blood draw"). Accordingly, the state courts proceeded on the acknowledgment that no exigency is at issue here. As the Wisconsin Court of Appeals put it:</p>
<blockquote id="p-99">"In particular, this case is not susceptible to resolution on the ground of exigent circumstances. No testimony was received that would support the conclusion that exigent circumstances justified the warrantless blood draw. [The officer] expressed agnosticism as to how long it would have taken to obtain a warrant, and he never once testified (or even implied) that there was no time to get a warrant." App. 66.</blockquote>
<p id="p-100">The exigency issue is therefore waived-that is, knowingly and intentionally abandoned, <a class="page-label" data-citation-index="1" data-label="2546" href="#p2546" id="p2546">*2546</a>see <em>Wood v. Milyard</em> , <extracted-citation case-ids="12189545" index="219" url="https://cite.case.law/us/566/463/#p474"><span class="citation" data-id="9499833"><a href="/opinion/798510/wood-v-milyard/" aria-description="Citation for case: Wood v. Milyard">566 U.S. 463</a></span></extracted-citation>, 474, <extracted-citation case-ids="12189545" index="220" url="https://cite.case.law/us/566/463/#p474"><span class="citation" data-id="9499833"><a href="/opinion/798510/wood-v-milyard/" aria-description="Citation for case: Wood v. Milyard">132 S.Ct. 1826</a></span></extracted-citation>, <extracted-citation case-ids="12189545" index="221" url="https://cite.case.law/us/566/463/#p474"><span class="citation" data-id="9499833"><a href="/opinion/798510/wood-v-milyard/" aria-description="Citation for case: Wood v. Milyard">182 L.Ed.2d 733</a></span></extracted-citation> (2012) -and the Court should not have considered it. See, <em>e.g.,</em> <em>Heckler v. Campbell</em> , <extracted-citation case-ids="11298743" index="222" url="https://cite.

[...TRUNCATED 77939 of 197939 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Monell v. Department of Social Services.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Monell v. Department of Social Services"
type: case
citation: "436 U.S. 658 (1978)"
parallel_cite: "98 S. Ct. 2018; 56 L. Ed. 2d 611; 16 Empl. Prac. Dec. (CCH) 8345; 17 Fair Empl. Prac. Cas. (BNA) 873"
neutral_cite: 1978 U.S. LEXIS 100
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1978
date_decided: 1978-06-06
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1978-06-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Monell v. Department of Social Services
  varies_by_point: false
  scope_note: "Overruled Monroe v. Pape in part (municipal immunity from § 1983 suit)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109881/monell-v-new-york-city-dept-of-social-servs/"
  cluster_id: 109881
  opinion_id: 109881
  identity_checked: true
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Monroe v. Pape]]", "[[City of Canton v. Harris]]", "[[Pembaur v. City of Cincinnati]]"]
aliases: ["Monell v. New York City Dept. of Social Servs.", "Monell v. Department of Social Services of the City of New York"]
tags: ["case", "section-1983", "municipal-liability", "policy-or-custom", "respondeat-superior"]
holding: "Local governments ARE 'persons' suable under § 1983, but ONLY when the constitutional injury is caused by the execution of an official…"
lake:
  record_id: Monell v. Department of Social Services
  status: verified
  projected_at: 2026-07-06
---

# Monell v. Department of Social Services

*436 U.S. 658 (1978)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
New York City employees challenged an official policy that compelled pregnant employees to take unpaid leave before it was medically necessary, suing the city and its officials under § 1983. The lower courts held the municipal defendants immune under *[[Monroe v. Pape]]*.

## Issue
Whether local governments are "persons" subject to suit under § 1983, and on what basis they may be held liable.

## Rule
Local governments are suable "persons" under § 1983, but only for their own official policies or customs — not vicariously. "the touchstone of the § 1983 action against a government body is an allegation that official policy is responsible for a deprivation of rights protected by the Constitution"; "local governments, like every other § 1983 'person,' by the very terms of the statute, may be sued for constitutional deprivations visited pursuant to governmental 'custom' even though such a custom has not received formal approval through the body's official decisionmaking channels." — 436 U.S. at 690-691. ^pin-690

At the same time, "a municipality cannot be held liable ... under § 1983 on a *respondeat superior* theory." — *Id.* at 691. ^pin-691

## Application
The challenged compulsory-leave rule was an official municipal policy "officially adopted and promulgated by that body's officers," not merely the act of an individual employee. Because the constitutional injury was inflicted through execution of the city's own policy, the city was a suable "person" under § 1983 and could be held liable for that policy — though not for an employee's tort on a vicarious-liability theory.

## Conclusion
Reversed in relevant part; municipalities are § 1983 "persons" liable for their official policies or customs, and *[[Monroe v. Pape]]* was overruled insofar as it held otherwise.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Monell* **overruled** [[Monroe v. Pape]] in part — its holding that municipalities are wholly immune from § 1983 suit. *Monell*'s policy-or-custom requirement was later elaborated by cases such as [[Pembaur v. City of Cincinnati]] and [[City of Canton v. Harris]].

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *Monell v. Department of Social Services*, 436 U.S. 658 (1978) — https://www.courtlistener.com/opinion/109881/monell-v-new-york-city-dept-of-social-servs/ — pinpoints: 690, 691.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "731dc9d9da39e38b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Monell v. Department of Social Services"}, "payload": {"all": [{"cite": "436 U.S. 658", "page": "658", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "436"}, {"cite": "98 S. Ct. 2018", "page": "2018", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "98"}, {"cite": "56 L. Ed. 2d 611", "page": "611", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "56"}, {"cite": "1978 U.S. LEXIS 100", "page": "100", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1978"}, {"cite": "16 Empl. Prac. Dec. (CCH) 8345", "page": "8345", "reporter": "Empl. Prac. Dec. (CCH)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "16"}, {"cite": "17 Fair Empl. Prac. Cas. (BNA) 873", "page": "873", "reporter": "Fair Empl. Prac. Cas. (BNA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "17"}], "display": "436 U.S. 658", "official": {"cite": "436 U.S. 658", "page": "658", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "436"}, "official_selection_present": true, "record_id": "Monell v. Department of Social Services"}}
{"assertion_id": "633f05131022eeff", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-690", "record_id": "Monell v. Department of Social Services"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-690", "pinpoint_status": "slip-only", "quote": "subject to suit under § 1983, and on what basis they may be held liable. ## Rule Local governments are suable", "quote_fidelity": "mismatch", "record_id": "Monell v. Department of Social Services", "star_marker": null}}
{"assertion_id": "995bae8f98a12386", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-691", "record_id": "Monell v. Department of Social Services"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-691", "pinpoint_status": "slip-only", "quote": "a municipality cannot be held liable ... under § 1983 on a *respondeat superior* theory.", "quote_fidelity": "mismatch", "record_id": "Monell v. Department of Social Services", "star_marker": null}}
{"assertion_id": "cc9e3add9004952d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Monell v. Department of Social Services"}, "payload": {"as_of_content": "1978-06-06", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Monell v. Department of Social Services", "scope_note": "Overruled Monroe v. Pape in part (municipal immunity from § 1983 suit).", "varies_by_point": false}}
```

### lake record — Monell v. Department of Social Services

```json
{
  "schema_version": "s2.v1",
  "record_id": "Monell v. Department of Social Services",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Monell v. New York City Dept. of Social Servs.",
    "case_name_short": "Monell",
    "case_name_full": "MONELL Et Al. v. DEPARTMENT OF SOCIAL SERVICES OF THE CITY OF NEW YORK Et Al.",
    "input_case_name": "Monell v. Department of Social Services",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1978-06-06",
    "year": 1978,
    "docket": null,
    "cluster_id": 109881,
    "lead_opinion_id": 109881,
    "sibling_ids": [
      109881,
      9427232,
      9427233,
      9427234,
      9427235
    ],
    "absolute_url": "/opinion/109881/monell-v-new-york-city-dept-of-social-servs/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9018437,
        "score": 20,
        "case_name": "Vinson v. Richmond Police Department"
      },
      {
        "cluster_id": 109930,
        "score": 20,
        "case_name": "Regents of the University of California v. Bakke"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "436 U.S. 658",
      "volume": "436",
      "reporter": "U.S.",
      "page": "658",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "98 S. Ct. 2018",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "2018",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 L. Ed. 2d 611",
        "volume": "56",
        "reporter": "L. Ed. 2d",
        "page": "611",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 Empl. Prac. Dec. (CCH) 8345",
        "volume": "16",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "8345",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fair Empl. Prac. Cas. (BNA) 873",
        "volume": "17",
        "reporter": "Fair Empl. Prac. Cas. (BNA)",
        "page": "873",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1978 U.S. LEXIS 100",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "100",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "436 U.S. 658",
        "volume": "436",
        "reporter": "U.S.",
        "page": "658",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 S. Ct. 2018",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "2018",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 L. Ed. 2d 611",
        "volume": "56",
        "reporter": "L. Ed. 2d",
        "page": "611",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1978 U.S. LEXIS 100",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "100",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 Empl. Prac. Dec. (CCH) 8345",
        "volume": "16",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "8345",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fair Empl. Prac. Cas. (BNA) 873",
        "volume": "17",
        "reporter": "Fair Empl. Prac. Cas. (BNA)",
        "page": "873",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "436 U.S. 658",
    "official_selection": {
      "court_class": "scotus",
      "selected": "436 U.S. 658",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-690",
      "page": null,
      "quote": "subject to suit under \u00a7 1983, and on what basis they may be held liable. ## Rule Local governments are suable",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-691",
      "page": null,
      "quote": "a municipality cannot be held liable ... under \u00a7 1983 on a *respondeat superior* theory.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1978-06-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Monell v. Department of Social Services",
    "varies_by_point": false,
    "scope_note": "Overruled Monroe v. Pape in part (municipal immunity from \u00a7 1983 suit).",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Monell v. New York City Dept. of Social Servs.",
          "cluster_id": 109881,
          "cite": [
            "56 L. Ed. 2d 611",
            "98 S. Ct. 2018",
            "436 U.S. 658",
            "1978 U.S. LEXIS 100",
            "16 Empl. Prac. Dec. (CCH) 8345",
            "17 Fair Empl. Prac. Cas. (BNA) 873"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "West v. Atkins",
          "cluster_id": 112116,
          "cite": [
            "101 L. Ed. 2d 40",
            "108 S. Ct. 2250",
            "487 U.S. 42",
            "1988 U.S. LEXIS 2744",
            "56 U.S.L.W. 4664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
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
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heck v. Humphrey",
          "cluster_id": 117864,
          "cite": [
            "129 L. Ed. 2d 383",
            "114 S. Ct. 2364",
            "512 U.S. 477",
            "1994 U.S. LEXIS 4824"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Will v. Michigan Department of State Police",
          "cluster_id": 112293,
          "cite": [
            "105 L. Ed. 2d 45",
            "109 S. Ct. 2304",
            "491 U.S. 58",
            "1989 U.S. LEXIS 2975",
            "57 U.S.L.W. 4677",
            "50 Empl. Prac. Dec. (CCH) 39,067",
            "49 Fair Empl. Prac. Cas. (BNA) 1664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
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
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
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
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillips v. County of Allegheny",
          "cluster_id": 1387268,
          "cite": [
            "515 F.3d 224",
            "2008 U.S. App. LEXIS 2513",
            "2008 WL 305025"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of the County Commissioners of Bryan County v. Brown",
          "cluster_id": 118104,
          "cite": [
            "137 L. Ed. 2d 626",
            "117 S. Ct. 1382",
            "520 U.S. 397",
            "1997 U.S. LEXIS 2793",
            "65 U.S.L.W. 4286",
            "10 Fla. L. Weekly Fed. S 405",
            "12 I.E.R. Cas. (BNA) 1217",
            "97 Cal. Daily Op. Serv. 3033",
            "97 Daily Journal DAR 5311"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
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
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parratt v. Taylor",
          "cluster_id": 110478,
          "cite": [
            "68 L. Ed. 2d 420",
            "101 S. Ct. 1908",
            "451 U.S. 527",
            "1981 U.S. LEXIS 99",
            "49 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
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
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County of Sacramento v. Lewis",
          "cluster_id": 118214,
          "cite": [
            "140 L. Ed. 2d 1043",
            "118 S. Ct. 1708",
            "523 U.S. 833",
            "1998 U.S. LEXIS 3404"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
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
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Los Angeles v. Lyons",
          "cluster_id": 110916,
          "cite": [
            "75 L. Ed. 2d 675",
            "103 S. Ct. 1660",
            "461 U.S. 95",
            "1983 U.S. LEXIS 152",
            "51 U.S.L.W. 4424"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Polk County v. Dodson",
          "cluster_id": 110589,
          "cite": [
            "70 L. Ed. 2d 509",
            "102 S. Ct. 445",
            "454 U.S. 312",
            "1981 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Allen v. McCurry",
          "cluster_id": 110360,
          "cite": [
            "66 L. Ed. 2d 308",
            "101 S. Ct. 411",
            "449 U.S. 90",
            "1980 U.S. LEXIS 156",
            "49 U.S.L.W. 4015"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
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
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "DeShaney v. Winnebago County Department of Social Services",
          "cluster_id": 112202,
          "cite": [
            "103 L. Ed. 2d 249",
            "109 S. Ct. 998",
            "489 U.S. 189",
            "1989 U.S. LEXIS 1039",
            "57 U.S.L.W. 4218"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
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
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Quern v. Jordan",
          "cluster_id": 110031,
          "cite": [
            "59 L. Ed. 2d 358",
            "99 S. Ct. 1139",
            "440 U.S. 332",
            "1979 U.S. LEXIS 67"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hafer v. Melo",
          "cluster_id": 112657,
          "cite": [
            "116 L. Ed. 2d 301",
            "112 S. Ct. 358",
            "502 U.S. 21",
            "1991 U.S. LEXIS 6502",
            "57 Empl. Prac. Dec. (CCH) 41,059"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Oklahoma v. Tuttle",
          "cluster_id": 111441,
          "cite": [
            "85 L. Ed. 2d 791",
            "105 S. Ct. 2427",
            "471 U.S. 808",
            "1985 U.S. LEXIS 26"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
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
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109881 OR 9427232 OR 9427233 OR 9427234 OR 9427235) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzE0MzQ4ODAwMDAwJnM9OTQ5Nzc2MCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109881+OR+9427232+OR+9427233+OR+9427234+OR+9427235%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 0,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 0,
        "triage_snippet_classified": 200
      },
      "lane2_top_cited": {
        "query": "cites:(109881 OR 9427232 OR 9427233 OR 9427234 OR 9427235)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMjUxJnM9NDI0NzA4MSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109881+OR+9427232+OR+9427233+OR+9427234+OR+9427235%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109881 OR 9427232 OR 9427233 OR 9427234 OR 9427235)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzM5OTIzMjAwMDAwJnM9MTAzMzU1MTkmdD1vJmQ9MjAyNi0wNy0wNiZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109881+OR+9427232+OR+9427233+OR+9427234+OR+9427235%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 0,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 0,
        "triage_snippet_classified": 200
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109881 OR 9427232 OR 9427233 OR 9427234 OR 9427235)",
    "indexed_citing_opinions": 11909,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109881,
        "count": 10324,
        "count_source": "search"
      },
      {
        "opinion_id": 9427232,
        "count": 1585,
        "count_source": "search"
      },
      {
        "opinion_id": 9427233,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427234,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427235,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 42009,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/monell-v-department-of-social-services.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zLjA1MzIyNjImcz03MzIzNjg4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109881+OR+9427232+OR+9427233+OR+9427234+OR+9427235%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 9427233,
        "cited_id": 84759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 96537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 96819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 101894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 104285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 104614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 107705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 107841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 108154,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 108362,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 108730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 108782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 108810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 108913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 108990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109199,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109503,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109508,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109574,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 249412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 334135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 1460310,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 84759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 84894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 85272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 85827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 86231,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 86293,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87371,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87903,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 88010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 88079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 88174,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 88308,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 90041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 90262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 92688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 96537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 96819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 97779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 101894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 103172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 103360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 103531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 103833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 104135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 104272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 104285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 104455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 104614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 105221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 106440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 106629,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 106630,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 106658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 107685,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 107705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 107706,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 107707,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 107841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 107971,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 107993,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108154,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108316,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108362,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108844,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109009,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109027,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109199,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109349,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109499,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109503,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109508,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109520,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109574,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 249412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 282871,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 334135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 1415269,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 1460310,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 1480162,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 1490664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 3876939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 6507289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 6599360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 6607492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 6633878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 7036523,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 7037170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 7652067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 8632804,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 8639091,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 8822445,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 8903338,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 8939977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 9004895,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 9299595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 9300237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 9301445,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 9427232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 84894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 85272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 85827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 86231,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 86293,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87371,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87903,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 88010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 88174,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 88308,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 90041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 90262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 92688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 97779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 101894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 103172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 103360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 103833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 104285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 105221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 106440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 106629,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 106630,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 106658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 107705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 107706,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 107707,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 107841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 107971,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 107993,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108316,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108844,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109009,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109027,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109349,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109499,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109503,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109520,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109574,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 334135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 1415269,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 1480162,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 1490664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 6507289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 6599360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 6633878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 7036523,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 7037170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 7652067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 8639091,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 8939977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 9004895,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 9299595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 9300237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 9301445,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 84759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 84894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 86293,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 87989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 88079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 96819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 101894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 103531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 103833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 104135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 104272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 104455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 107685,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 108782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 108813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 108987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 108990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 109503,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 109509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 109520,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 109574,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 282871,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 334135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 3876939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 6607492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 8632804,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 8822445,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 8903338,
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
    "date_created": "2026-07-05T14:24:17Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:24:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:24:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:27:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:24:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Monell v. Department of Social Services (truncated)

```
<div>
<center><b><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U.S. 658</a></span> (1978)</b></center>
<center><h1>MONELL ET AL.<br>
v.<br>
DEPARTMENT OF SOCIAL SERVICES OF THE CITY OF NEW YORK ET AL.</h1></center>
<center>No. 75-1914.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued November 2, 1977.</center>
<center>Decided June 6, 1978.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT
<p><span class="star-pagination">*660</span> <i>Oscar Chase</i> argued the cause for petitioners. With him on the briefs were <i>Nancy Stearns, Jack Greenberg,</i> and <i>Eric Schnapper.</i></p>
<p><i>L. Kevin Sheridan</i> argued the cause for respondents. With him on the brief was <i>W. Bernard Richland.</i><sup>[*]</sup></p>
<p>MR. JUSTICE BRENNAN delivered the opinion of the Court.</p>
<p>Petitioners, a class of female employees of the Department of Social Services and of the Board of Education of the city of New York, commenced this action under <span class="citation no-link">42 U. S. C. § 1983</span> in July 1971.<sup>[1]</sup> The gravamen of the complaint was that the <span class="star-pagination">*661</span> Board and the Department had as a matter of official policy compelled pregnant employees to take unpaid leaves of absence before such leaves were required for medical reasons.<sup>[2]</sup> Cf. <i>Cleveland Board of Education</i> v. <i>LaFleur,</i> <span class="citation" data-id="9425515"><a href="/opinion/108913/cleveland-board-of-education-v-lafleur/" aria-description="Citation for case: Cleveland Board of Education v. LaFleur">414 U. S. 632</a></span> (1974). The suit sought injunctive relief and backpay for periods of unlawful forced leave. Named as defendants in the action were the Department and its Commissioner, the Board and its Chancellor, and the city of New York and its Mayor. In each case, the individual defendants were sued solely in their official capacities.<sup>[3]</sup></p>
<p>On cross-motions for summary judgment, the District Court for the Southern District of New York held moot petitioners' claims for injunctive and declaratory relief since the city of New York and the Board, after the filing of the complaint, had changed their policies relating to maternity leaves so that no pregnant employee would have to take leave unless she was medically unable to continue to perform her job. <span class="citation" data-id="1415269"><a href="/opinion/1415269/monell-v-deptartment-of-social-services-of-new-york/#855" aria-description="Citation for case: Monell v. Deptartment of Social Services of New York">394 F. Supp. 853, 855</a></span> (1975). No one now challenges this conclusion. <span class="star-pagination">*662</span> The court did conclude, however, that the acts complained of were unconstitutional under <i><span class="citation" data-id="9425515"><a href="/opinion/108913/cleveland-board-of-education-v-lafleur/" aria-description="Citation for case: Cleveland Board of Education v. LaFleur">LaFleur, supra.</a></span></i> <span class="citation" data-id="1415269"><a href="/opinion/1415269/monell-v-deptartment-of-social-services-of-new-york/#855" aria-description="Citation for case: Monell v. Deptartment of Social Services of New York">394 F. Supp., at 855</a></span>. Nonetheless plaintiffs' prayers for backpay were denied because any such damages would come ultimately from the city of New York and, therefore, to hold otherwise would be to "circumven[t]" the immunity conferred on municipalities by <i>Monroe</i> v. <i>Pape,</i> <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167</a></span> (1961). See <span class="citation" data-id="1415269"><a href="/opinion/1415269/monell-v-deptartment-of-social-services-of-new-york/#855" aria-description="Citation for case: Monell v. Deptartment of Social Services of New York">394 F. Supp., at 855</a></span>.</p>
<p>On appeal, petitioners renewed their arguments that the Board of Education<sup>[4]</sup> was not a "municipality" within the meaning of <i>Monroe</i> v. <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Pape, supra</a></span></i><i>,</i> and that, in any event, the District Court had erred in barring a damages award against the individual defendants. The Court of Appeals for the Second Circuit rejected both contentions. The court first held that the Board of Education was not a "person" under § 1983 because "it performs a vital governmental function . . ., and, significantly, while it has the right to determine how the funds appropriated to it shall be spent . . ., it has no final say in deciding what its appropriations shall be." <span class="citation" data-id="334135"><a href="/opinion/334135/12-fair-emplpraccas-836-11-empl-prac-dec-p-10755-jane-monell-v/#263" aria-description="Citation for case: 12 Fair empl.prac.cas. 836, 11 Empl. Prac. Dec. P 10,755...">532 F. 2d 259, 263</a></span> (1976). The individual defendants, however, were "persons" under § 1983, even when sued solely in their official capacities. <span class="citation" data-id="334135"><a href="/opinion/334135/12-fair-emplpraccas-836-11-empl-prac-dec-p-10755-jane-monell-v/#264" aria-description="Citation for case: 12 Fair empl.prac.cas. 836, 11 Empl. Prac. Dec. P 10,755...">532 F. 2d, at 264</a></span>. Yet, because a damages award would "have to be paid by a city that was held not to be amenable to such an action in <i>Monroe</i> v. <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Pape</a></span></i><i>,</i>" a damages action against officials sued in their official capacities could not proceed. <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#265" aria-description="Citation for case: Monroe v. Pape"><i>Id.,</i> at 265</a></span>.</p>
<p>We granted certiorari in this case, <span class="citation multiple-matches"><a href="/c/U.%20S./429/1071/">429 U. S. 1071</a></span>, to consider</p>
<blockquote>"Whether local governmental officials and/or local independent school boards are `persons' within the meaning of <span class="citation no-link">42 U. S. C. § 1983</span> when equitable relief in the nature of back pay is sought against them in their official capacities?" Pet. for Cert. 8. <span class="star-pagination">*663</span> Although, after plenary consideration, we have decided the merits of over a score of cases brought under § 1983 in which the principal defendant was a school board<sup>[5]</sup>and, indeed, in some of which § 1983 and its jurisdictional counterpart, <span class="citation no-link">28 U. S. C. § 1343</span>, provided the only basis for jurisdiction<sup>[6]</sup>we indicated in <i>Mt. Healthy City Board of Education</i> v. <i>Doyle,</i> <span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/#279" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">429 U. S. 274, 279</a></span> (1977), last Term that the question presented here was open and would be decided "another day." That other day has come and we now overrule <i>Monroe</i> v. <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Pape, supra</a></span></i><i>,</i> insofar as it holds that local governments are wholly immune from suit under § 1983.<sup>[7]</sup></blockquote>
<p></p>
<h2>
<span class="star-pagination">*664</span> I</h2>
<p>In <i>Monroe</i> v. <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Pape</a></span></i><i>,</i> we held that "Congress did not undertake to bring municipal corporations within the ambit of [§ 1983]." <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#187" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 187</a></span>. The sole basis for this conclusion was an inference drawn from Congress' rejection of the "Sherman amendment" to the bill which became the Civil Rights Act of 1871, <span class="citation no-link">17 Stat. 13</span>, the precursor of § 1983. The amendment would have held a municipal corporation liable for damage done to the person or property of its inhabitants by <i>private</i> persons "riotously and tumultuously assembled."<sup>[8]</sup> Cong. Globe, 42d Cong., 1st Sess., 749 (1871) (hereinafter Globe). Although the Sherman amendment did not seek to amend § 1 of the Act, which is now § 1983, and although the nature of the obligation created by that amendment was vastly different from that created by § 1, the Court nonetheless concluded in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> that Congress must have meant to exclude municipal corporations from the coverage of § 1 because "`the House [in voting against the Sherman amendment] had solemnly decided that in their judgment Congress had no constitutional power to impose any <i>obligation</i> upon county and town organizations, the mere instrumentality for the administration of state law.'" <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#190" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 190</a></span> (emphasis added), quoting Globe 804 (Rep. Poland). This statement, we thought, showed that Congress doubted its "constitutional power . . . to impose <i>civil liability</i> on municipalities," <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#190" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 190</a></span> (emphasis added), and that such doubt would have extended to any type of civil liability.<sup>[9]</sup></p>
<p><span class="star-pagination">*665</span> A fresh analysis of the debate on the Civil Rights Act of 1871, and particularly of the case law which each side mustered in its support, shows, however, that <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> incorrectly equated the "obligation" of which Representative Poland spoke with "civil liability."</p>
<p></p>
<h2>A. An Overview</h2>
<p>There are three distinct stages in the legislative consideration of the bill which became the Civil Rights Act of 1871. On March 28, 1871, Representative Shellabarger, acting for a House select committee, reported H. R. 320, a bill "to enforce the provisions of the fourteenth amendment to the Constitution of the United States, and for other purposes." H. R. 320 contained four sections. Section 1, now codified as <span class="citation no-link">42 U. S. C. § 1983</span>, was the subject of only limited debate and was passed without amendment.<sup>[10]</sup> Sections 2 through 4 dealt primarily with the "other purpose" of suppressing Ku Klux Klan violence in the Southern States.<sup>[11]</sup> The wisdom and constitutionality of these sectionsnot § 1, now § 1983were the subject of almost all congressional debate and each of these sections was amended. The House finished its initial debates on H. R. 320 on April 7, 1871, and one week later the Senate also voted out a bill.<sup>[12]</sup> Again, debate on § 1 of the bill was limited and that section was passed as introduced.</p>
<p><span class="star-pagination">*666</span> Immediately prior to the vote on H. R. 320 in the Senate, Senator Sherman introduced his amendment.<sup>[13]</sup> This was <i>not</i> an amendment to § 1 of the bill, but was to be added as § 7 at the end of the bill. Under the Senate rules, no discussion of the amendment was allowed and, although attempts were made to amend the amendment, it was passed as introduced. In this form, the amendment did <i>not</i> place liability on municipal corporations, but made any inhabitant of a municipality liable for damage inflicted by persons "riotously and tumultuously assembled."<sup>[14]</sup></p>
<p>The House refused to acquiesce in a number of amendments made by the Senate, including the Sherman amendment, and the respective versions of H. R. 320 were therefore sent to a conference committee. Section 1 of the bill, however, was not a subject of this conference since, as noted, it was passed verbatim as introduced in both Houses of Congress.</p>
<p>On April 18, 1871, the first conference committee completed its work on H. R. 320. The main features of the conference committee draft of the Sherman amendment were these:<sup>[15]</sup> First, a cause of action was given to persons injured by</p>
<blockquote>"any persons riotously and tumultuously assembled together . . . with intent to deprive any person of any right conferred upon him by the Constitution and laws of the United States, or to deter him or punish him for exercising such right, or by reason of his race, color, or previous condition of servitude . . . ." <span class="star-pagination">*667</span> Second, the bill provided that the action would be against the county, city, or parish in which the riot had occurred and that it could be maintained by either the person injured or his legal representative. Third, unlike the amendment as proposed, the conference substitute made the government defendant liable on the judgment if it was not satisfied against individual defendants who had committed the violence. If a municipality were liable, the judgment against it could be collected</blockquote>
<blockquote>"by execution, attachment, mandamus, garnishment, or any other proceeding in aid of execution or applicable to the enforcement of judgments against municipal corporations; and such judgment [would become] a lien as well upon all moneys in the treasury of such county, city, or parish, as upon the other property thereof."</blockquote>
<p>In the ensuing debate on the first conference report, which was the first debate of any kind on the Sherman amendment, Senator Sherman explained that the purpose of his amendment was to enlist the aid of persons of property in the enforcement of the civil rights laws by making their property "responsible" for Ku Klux Klan damage.<sup>[16]</sup> Statutes drafted on a similar theory, he stated, had long been in force in England and were in force in 1871 in a number of States.<sup>[17]</sup><span class="star-pagination">*668</span> Nonetheless there were critical differences between the conference substitute and extant state and English statutes: The conference substitute, unlike most state riot statutes, lacked a short statute of limitations and imposed liability on the government defendant whether or not it had notice of the impending riot, whether or not the municipality was authorized to exercise a police power, whether or not it exerted all reasonable efforts to stop the riot, and whether or not the rioters were caught and punished.<sup>[18]</sup></p>
<p>The first conference substitute passed the Senate but was rejected by the House. House opponents, within whose ranks were some who had supported § 1, thought the Federal Government could not, consistent with the Constitution, obligate municipal corporations to keep the peace if those corporations were neither so obligated nor so authorized by their state charters. And, because of this constitutional objection, opponents of the Sherman amendment were unwilling to impose damages liability for nonperformance of a duty which Congress could not require municipalities to perform. This position is reflected in Representative Poland's statement that is quoted in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>.</i><sup>[19]</sup></p>
<p>Because the House rejected the first conference report a second conference was called and it duly issued its report. The second conference substitute for the Sherman amendment abandoned municipal liability and, instead, made "any person <span class="star-pagination">*669</span> or persons having knowledge [that a conspiracy to violate civil rights was afoot], and having power to prevent or aid in preventing the same," who did not attempt to stop the same, liable to any person injured by the conspiracy.<sup>[20]</sup> The amendment in this form was adopted by both Houses of Congress and is now codified as <span class="citation no-link">42 U. S. C. § 1986</span>.</p>
<p>The meaning of the legislative history sketched above can most readily be developed by first considering the debate on the report of the first conference committee. This debate shows conclusively that the constitutional objections raised against the Sherman amendmenton which our holding in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> was based, see <i>supra,</i> at 664would not have prohibited congressional creation of a civil remedy against state municipal corporations that infringed federal rights. Because § 1 of the Civil Rights Act does not state expressly that municipal corporations come within its ambit, it is finally necessary to interpret § 1 to confirm that such corporations were indeed intended to be included within the "persons" to whom that section applies.</p>
<p></p>
<h2>B. Debate on the First Conference Report</h2>
<p>The style of argument adopted by both proponents and opponents of the Sherman amendment in both Houses of Congress was largely legal, with frequent references to cases decided by this Court and the Supreme Courts of the several States. Proponents of the Sherman amendment did not, however, discuss in detail the argument in favor of its constitutionality. Nonetheless, it is possible to piece together such an argument from the debates on the first conference report and those on § 2 of the civil rights bill, which, because it allowed the Federal Government to prosecute crimes "in the States," had also raised questions of federal power. The account of Representative Shellabarger, the House sponsor of H. R. 320, is the most complete.</p>
<p><span class="star-pagination">*670</span> Shellabarger began his discussion of H. R. 320 by stating that "there is a domain of constitutional law involved in the right consideration of this measure which is wholly unexplored." Globe App. 67. There were analogies, however. With respect to the meaning of § 1 of the Fourteenth Amendment, and particularly its Privileges or Immunities Clause, Shellabarger relied on the statement of Mr. Justice Washington in <i>Corfield</i> v. <i>Coryell,</i> <span class="citation" data-id="9301445"><a href="/opinion/9306338/corfield-v-coryell/" aria-description="Citation for case: Corfield v. Coryell">4 Wash. C. C. 371</a></span> (CC ED Pa. 1825), which defined the privileges protected by Art. IV:</p>
<blockquote>"`What these fundamental privileges are[,] it would perhaps be more tedious than difficult to enumerate. They may, however, be all comprehended under the following general heads: protection by the Government;'</blockquote>
<blockquote>
<i>"Mark that</i></blockquote>
<blockquote>"`<i>protection by the Government;</i> the enjoyment of life and liberty, with the right to acquire and possess property of every kind, and to pursue and obtain happiness and safety . . . .'" Globe App. 69 (emphasis added), quoting <span class="citation" data-id="9301445"><a href="/opinion/9306338/corfield-v-coryell/#380" aria-description="Citation for case: Corfield v. Coryell">4 Wash. C. C., at 380-381</a></span>.</blockquote>
<p>Building on his conclusion that citizens were owed protectiona conclusion not disputed by opponents of the Sherman amendment<sup>[21]</sup>Shellabarger then considered Congress' role in providing that protection. Here again there were precedents:</p>
<blockquote>"[Congress has always] assumed to enforce, as against <span class="star-pagination">*671</span> the States, and also persons, every one of the provisions of the Constitution. Most of the provisions of the Constitution which restrain and directly relate to the States, such as those in [Art. I, § 10,] relate to the divisions of the political powers of the State and General Governments.. . . These prohibitions upon political powers of the States are all of such nature that they can be, and even have been, . . . enforced by the courts of the United States declaring void all State acts of encroachment on Federal powers. Thus, and thus sufficiently, has the United States `enforced' these provisions of the Constitution. But there are some that are not of this class. These are where the court secures the rights or the liabilities of persons within the States, as between such persons and the States.</blockquote>
<blockquote>"These three are: first, that as to fugitives from justice;<sup>[22]</sup> second, that as to fugitives from service, (or slaves;)<sup>[23]</sup> third, that declaring that the `citizens of each State shall be entitled to all the privileges and immunities of citizens in the several States.'<sup>[24]</sup></blockquote>
<blockquote>
<span class="star-pagination">*672</span> "And, sir, every one of thesethe only provisions where it was deemed that legislation was required to enforce the constitutional provisionsthe only three where the rights or liabilities of persons in the States, as between these persons and the States, are directly provided for, Congress has by legislation affirmatively interfered to protect . . . such persons." Globe App. 69-70.</blockquote>
<p>Of legislation mentioned by Shellabarger, the closest analog of the Sherman amendment, ironically, was the statute implementing the fugitives from justice and fugitive slave provisions of Art. IVthe Act of Feb. 12, 1793, 1 Stat. 302the constitutionality of which had been sustained in 1842, in <i>Prigg</i> v. <i>Pennsylvania,</i> <span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/" aria-description="Citation for case: Prigg v. Pennsylvania">16 Pet. 539</a></span>. There, Mr. Justice Story, writing for the Court, held that Art. IV gave slaveowners a federal right to the unhindered possession of their slaves in whatever State such slaves might be found. <span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/#612" aria-description="Citation for case: Prigg v. Pennsylvania">16 Pet., at 612</a></span>. Because state process for recovering runaway slaves might be inadequate or even hostile to the rights of the slaveowner, the right intended to be conferred could be negated if left to state implementation. <span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/#614" aria-description="Citation for case: Prigg v. Pennsylvania"><i>Id.,</i> at 614</a></span>. Thus, since the Constitution guaranteed the right and this in turn required a remedy, Story held it to be a "natural inference" that Congress had the power itself to ensure an appropriate (in the Necessary and Proper Clause sense) remedy for the right. <span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/#615" aria-description="Citation for case: Prigg v. Pennsylvania"><i>Id.,</i> at 615</a></span>.</p>
<p>Building on <i><span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/" aria-description="Citation for case: Prigg v. Pennsylvania">Prigg</a></span>,</i> Shellabarger argued that a remedy against municipalities and counties was an appropriateand hence constitutionalmethod for ensuring the protection which the Fourteenth Amendment made every citizen's federal right.<sup>[25]</sup> This much was clear from the adoption of such statutes by the several States as devices for suppressing riot.<sup>[26]</sup> Thus, said Shellabarger, the only serious question remaining <span class="star-pagination">*673</span> was "whether, since a county is an integer or part of a State, the United States can impose upon it, as such, <i>any obligations to keep the peace</i> in obedience to United States laws."<sup>[27]</sup> This he answered affirmatively, citing <i>Board of Comm'rs</i> v. <i>Aspinwall,</i> <span class="citation" data-id="87413"><a href="/opinion/87413/the-board-of-commrs-of-knox-county-v-aspinwall/" aria-description="Citation for case: The Board of Commr&#x27;s of Knox County v. Aspinwall">24 How. 376</a></span> (1861), the first of many cases<sup>[28]</sup> upholding the power of federal courts to enforce the Contract Clause against municipalities.<sup>[29]</sup></p>
<p>House opponents of the Sherman amendmentwhose views are particularly important since only the House voted down the amendmentdid not dispute Shellabarger's claim that the Fourteenth Amendment created a federal right to protection, see n. 21, <i>supra,</i> but they argued that the local units of government upon which the amendment fastened liability were not obligated to keep the peace at state law and further that the Federal Government could not constitutionally require local governments to create police forces, whether this requirement was levied directly, or indirectly by imposing damages for breach of the peace on municipalities. The most complete statement of this position is that of Representative Blair:<sup>[30]</sup></p>
<blockquote>"The proposition known as the Sherman amendment <span class="star-pagination">*674</span>. . . is entirely new. It is altogether without a precedent in this country. . . . That amendment claims the power in the General Government to go into the States of this Union and lay such obligations as it may please upon the municipalities, which are the creations of the States alone. . . .</blockquote>
<blockquote>". . . [H]ere it is proposed, not to carry into effect an obligation which rests upon the municipality, but to <span class="star-pagination">*675</span> create that obligation, and that is the provision I am unable to assent to. The parallel of the hundred does not in the least meet the case. The power that laid the obligation upon the hundred first put the duty upon the hundred that it should perform in that regard, and failing to meet the obligation which had been laid upon it, it was very proper that it should suffer damage for its neglect. . . .</blockquote>
<blockquote>"... [T]here are certain rights and duties that belong to the States, . . . there are certain powers that inhere in the State governments. They create these municipalities, they say what their powers shall be and what their obligations shall be. If the Government of the United States can step in and add to those obligations, may it not utterly destroy the municipality? If it can say that it shall be liable for damages occurring from a riot, . . . where [will] its power . . . stop and what obligations . . . might [it] not lay upon a municipality. . . .</blockquote>
<blockquote>"Now, only the other day, the Supreme Court . . . decided [in <i>Collector</i> v. <i>Day,</i> <span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">11 Wall. 113</a></span> (1871)] that there is no power in the Government of the United States, under its authority to tax, to tax the salary of a State officer. Why? Simply because the power to tax involves the power to destroy, and it was not the intent to give the Government of the United States power to destroy the government of the States in any respect. It was held also in the case of Prigg <i>vs.</i> Pennsylvania [<span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/" aria-description="Citation for case: Prigg v. Pennsylvania">16 Pet. 539</a></span> (1842)] that it is not within the power of the Congress of the United States to lay duties upon a State officer; that we cannot command a State officer to do any duty whatever, as such; and I ask . . . the difference between that and commanding a municipality, which is equally the creature of the State, to perform a duty." Globe 795.</blockquote>
<p>Any attempt to impute a unitary constitutional theory to opponents of the Sherman amendment is, of course, fraught <span class="star-pagination">*676</span> with difficulties, not the least of which is that most Members of Congress did not speak to the issue of the constitutionality of the amendment. Nonetheless, two considerations lead us to conclude that opponents of the Sherman amendment found it unconstitutional substantially because of the reasons stated by Representative Blair: First, Blair's analysis is precisely that of Poland, whose views were quoted as authoritative in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> see <i>supra,</i> at 664, and that analysis was shared in large part by all House opponents who addressed the constitutionality of the Sherman amendment.<sup>[31]</sup> Second, Blair's exegesis of the reigning constitutional theory of his day, as we shall explain, was clearly supported by precedentalbeit precedent that has not survived, see <i>Ex parte Virginia,</i> <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/#347" aria-description="Citation for case: Ex Parte Virginia">100 U. S. 339, 347-348</a></span> (1880); <i>Graves</i> v. <i>New York ex rel. O'Keefe,</i> <span class="citation" data-id="9419020"><a href="/opinion/103172/graves-v-new-york-ex-rel-okeefe/#486" aria-description="Citation for case: Graves v. New York Ex Rel. O&#x27;Keefe">306 U. S. 466, 486</a></span> (1939)and no other constitutional formula was advanced by participants in the House debates.</p>
<p><i>Collector</i> v. <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span></i><i>,</i> cited by Blair, was the clearest and, at the time of the debates, the most recent pronouncement of a doctrine of coordinate sovereignty that, as Blair stated, placed limits on even the enumerated powers of the National Government in favor of protecting state prerogatives. There, the Court held that the United States could not tax the income of Day, a Massachusetts state judge, because the independence of the States within their legitimate spheres would be imperiled if the instrumentalities through which States executed their powers were "subject to the control of another and distinct government." <span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/#127" aria-description="Citation for case: Collector v. Day">11 Wall., at 127</a></span>. Although the Court in <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span></i> apparently rested this holding in part on the proposition that the taxing "power acknowledges no limits but the will of the legislative body imposing the tax," <span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/#125" aria-description="Citation for case: Collector v. Day"><i>id.,</i> at 125-126</a></span>; cf. <i>McCulloch</i> v. <i>Maryland,</i> <span class="citation" data-id="85272"><a href="/opinion/85272/mculloch-v-state-of-maryland/" aria-description="Citation for case: M&#x27;culloch v. State of Maryland">4 Wheat. 316</a></span> (1819), the Court had in other cases limited other national powers in order to avoid interference with the States.<sup>[32]</sup></p>
<p><span class="star-pagination">*677</span> In <i>Prigg</i> v. <i><span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/" aria-description="Citation for case: Prigg v. Pennsylvania">Pennsylvania</a></span></i><i>,</i> for example, Mr. Justice Story, in addition to confirming a broad national power to legislate under the Fugitive Slave Clause, see <i>supra,</i> at 672, held that Congress could not "insist that states . . . provide means to carry into effect the duties of the national government." <span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/#615" aria-description="Citation for case: Prigg v. Pennsylvania">16 Pet., at 615-616</a></span>.<sup>[33]</sup> And Mr. Justice McLean agreed that, "[a]s a general principle," it was true "that Congress had no power to impose duties on state officers, as provided in the [Act of Feb. 12, 1793]." Nonetheless he wondered whether Congress might not impose "positive" duties on state officers where a clause of the Constitution, like the Fugitive Slave Clause, seemed to require affirmative government assistance, rather than restraint of government, to secure federal rights. See <span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/#664" aria-description="Citation for case: Prigg v. Pennsylvania"><i>id.,</i> at 664-665</a></span>.</p>
<p>Had Mr. Justice McLean been correct in his suggestion that, where the Constitution envisioned affirmative government assistance, the States or their officers or instrumentalities could be required to provide it, there would have been little doubt that Congress could have insisted that municipalities afford by "positive" action the protection<sup>[34]</sup> owed individuals under § 1 of the Fourteenth Amendment whether or not municipalities were obligated by state law to keep the peace. However, any such argument, largely foreclosed by <i><span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/" aria-description="Citation for case: Prigg v. Pennsylvania">Prigg</a></span>,</i> was made <span class="star-pagination">*678</span> impossible by the Court's holding in <i>Kentucky</i> v. <i>Dennison,</i> <span class="citation" data-id="87371"><a href="/opinion/87371/commonwealth-of-ky-v-dennison-governor-c/" aria-description="Citation for case: Commonwealth of Ky. v. DENNISON, GOVERNOR, &amp;C.">24 How. 66</a></span> (1861). There, the Court was asked to require Dennison, the Governor of Ohio, to hand over Lago, a fugitive from justice wanted in Kentucky, as required by § 1 of the Act of Feb. 12, 1793,<sup>[35]</sup> which implemented Art. IV, § 2, cl. 2, of the Constitution. Mr. Chief Justice Taney, writing for a unanimous Court, refused to enforce that section of the Act:</p>
<blockquote>"[W]e think it clear, that the Federal Government, under the Constitution, has no power to impose on a State officer, as such, any duty whatever, and compel him to perform it; for if it possessed this power, it might overload the officer with duties which would fill up all his time, and disable him from performing his obligations to the State, and might impose on him duties of a character incompatible with the rank and dignity to which he was elevated by the State." 24 How., at 107-108.</blockquote>
<p>The rationale of <i><span class="citation" data-id="87371"><a href="/opinion/87371/commonwealth-of-ky-v-dennison-governor-c/" aria-description="Citation for case: Commonwealth of Ky. v. DENNISON, GOVERNOR, &amp;C.">Dennison</a></span></i>that the Nation could not impose duties on state officers since that might impede States in their legitimate activitiesis obviously identical to that which animated the decision in <i>Collector</i> v. <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span></i><i>.</i> See <i>supra,</i> at 676. And, as Blair indicated, municipalities as instrumentalities through which States executed their policies could be equally disabled from carrying out state policies if they were also obligated to carry out federally imposed duties. Although no one cited <i><span class="citation" data-id="87371"><a href="/opinion/87371/commonwealth-of-ky-v-dennison-governor-c/" aria-description="Citation for case: Commonwealth of Ky. v. DENNISON, GOVERNOR, &amp;C.">Dennison</a></span></i> by name, the principle for which it <span class="star-pagination">*679</span> stands was well known to Members of Congress,<sup>[36]</sup> many of whom discussed <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span></i><sup>[37]</sup> as well as a series of State Supreme Court cases<sup>[38]</sup> in the mid-1860's which had invalidated a federal tax on the process of state courts on the ground that the tax threatened the independence of a vital state function.<sup>[39]</sup> Thus, there was ample support for Blair's view that the Sherman amendment, by putting municipalities to the Hobson's choice of keeping the peace or paying civil damages, attempted to impose obligations on municipalities by indirection that could not be imposed directly, thereby threatening to "destroy the government of the States." Globe 795.</p>
<p>If municipal liability under § 1 of the Civil Rights Act of 1871 created a similar Hobson's choice, we might conclude, as <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> did, that Congress could not have intended municipalities to be among the "persons" to which that section applied. But this is not the case.</p>
<p>First, opponents expressly distinguished between imposing an obligation to keep the peace and merely imposing civil liability for damages on a municipality that was obligated by state law to keep the peace, but which had not in violation of the Fourteenth Amendment. Representative Poland, for example, reasoning from Contract Clause precedents, indicated that Congress could constitutionally confer jurisdiction on the federal courts to entertain suits seeking to hold municipalities <span class="star-pagination">*680</span> liable for using their authorized powers in violation of the Constitutionwhich is as far as § 1 of the Civil Rights Act went:</p>
<blockquote>"I presume . . . that where a State had imposed a duty [to keep the peace] upon [a] municipality . . . an action would be allowed to be maintained against them in the courts of the United States under the ordinary restrictions as to jurisdiction. But the enforcing a liability, existing by their own contract, or by a State law, in the courts, is a very widely different thing from devolving a new duty or liability upon them by the national Government, which has no power either to create or destroy them, and no power or control over them whatever." Globe 794.</blockquote>
<p>Representative Burchard agreed:</p>
<blockquote>"[T]here is no duty imposed by the Constitution of the United States, or usually by State laws, upon a county to protect the people of that county against the commission of the offenses herein enumerated, such as the burning of buildings or any other injury to property or injury to person. Police powers are not conferred upon counties as corporations; they are conferred upon cities that have qualified legislative power. And so far as cities are concerned, where the equal protection required to be afforded by a State is imposed upon a city by State laws, perhaps the United States courts could enforce its performance. But counties . . . do not have any control of the police . . . ." <i>Id.,</i> at 795.</blockquote>
<p>See also the views of Rep. Willard, discussed at n. 30, <i>supra.</i></p>
<p>Second, the doctrine of dual sovereignty apparently put no limit on the power of federal courts to enforce the Constitution against municipalities that violated it. Under the theory of dual sovereignty set out in <i><span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/" aria-description="Citation for case: Prigg v. Pennsylvania">Prigg</a></span>,</i> this is quite understandable. So long as federal courts were vindicating the Federal Constitution, they were providing the "positive" government action <span class="star-pagination">*681</span> required to protect federal constitutional rights and no question was raised of enlisting the States in "positive" action. The limits of the principles announced in <i><span class="citation" data-id="87371"><a href="/opinion/87371/commonwealth-of-ky-v-dennison-governor-c/" aria-description="Citation for case: Commonwealth of Ky. v. DENNISON, GOVERNOR, &amp;C.">Dennison</a></span></i> and <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span></i> are not so well defined in logic, but are clear as a matter of history. It must be remembered that the same Court which rendered <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span></i> also vigorously enforced the Contract Clause against municipalitiesan enforcement effort which included various forms of "positive" relief, such as ordering that taxes be levied and collected to discharge federal-court judgments, once a constitutional infraction was found.<sup>[40]</sup> Thus, federal judicial enforcement of the Constitution's express limits on state power, since it was done so frequently, must, notwithstanding anything said in <i><span class="citation" data-id="87371"><a href="/opinion/87371/commonwealth-of-ky-v-dennison-governor-c/" aria-description="Citation for case: Commonwealth of Ky. v. DENNISON, GOVERNOR, &amp;C.">Dennison</a></span></i> or <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span>,</i> have been permissible, at least so long as the interpretation of the Constitution was left in the hands of the judiciary. Since § 1 of the Civil Rights Act simply conferred jurisdiction on the federal courts to enforce § 1 of the Fourteenth Amendmenta situation precisely analogous to the grant of diversity jurisdiction under which the Contract Clause was enforced against municipalitiesthere <span class="star-pagination">*682</span> is no reason to suppose that opponents of the Sherman amendment would have found any constitutional barrier to § 1 suits against municipalities.</p>
<p>Finally, the very votes of those Members of Congress, who opposed the Sherman amendment but who had voted for § 1, confirm that the liability imposed by § 1 was something very different from that imposed by the amendment. Section 1 without question could be used to obtain a damages judgment against state or municipal <i>officials</i> who violated federal constitutional rights while acting under color of law.<sup>[41]</sup> However, for <i>Prigg-Dennison-Day</i> purposes, as Blair and others recognized,<sup>[42]</sup> there was no distinction of constitutional magnitude between officers and agentsincluding corporate agentsof the State: Both were state instrumentalities and the State could be impeded no matter over which sort of instrumentality the Federal Government sought to assert its power. <i><span class="citation" data-id="87371"><a href="/opinion/87371/commonwealth-of-ky-v-dennison-governor-c/" aria-description="Citation for case: Commonwealth of Ky. v. DENNISON, GOVERNOR, &amp;C.">Dennison</a></span></i> and <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span>,</i> after all, were not suits against municipalities but against <i>officers,</i> and Blair was quite conscious that he was extending these cases by applying them to municipal corporations.<sup>[43]</sup> Nonetheless, Senator Thurman, who gave the most exhaustive critique of § 1<i>inter alia,</i> complaining that it would be applied to state officers, see Globe App. 217and who opposed both § 1 and the Sherman amendment, the latter on <i><span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/" aria-description="Citation for case: Prigg v. Pennsylvania">Prigg</a></span></i> grounds, agreed unequivocally that § 1 was constitutional.<sup>[44]</sup><span class="star-pagination">*683</span> Those who voted for § 1 must similarly have believed in its constitutionality despite <i>Prigg, Dennison,</i> and <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span>.</i></p>
<p></p>
<h2>C. Debate on § 1 of the Civil Rights Bill</h2>
<p>From the foregoing discussion, it is readily apparent that nothing said in debate on the Sherman amendment would have prevented holding a municipality liable under § 1 of the Civil Rights Act for its own violations of the Fourteenth Amendment. The question remains, however, whether the general language describing those to be liable under § 1"any person"covers more than natural persons. An examination of the debate on § 1 and application of appropriate rules of construction show unequivocally that § 1 was intended to cover legal as well as natural persons.</p>
<p>Representative Shellabarger was the first to explain the function of § 1:</p>
<blockquote>"[Section 1] not only provides a civil remedy for persons whose former condition may have been that of slaves, but also to all people where, under color of State law, they or any of them may be deprived of rights to which they are entitled under the Constitution by reason and virtue of their national citizenship." Globe App. 68.</blockquote>
<p>By extending a remedy to all people, including whites, § 1 went beyond the mischief to which the remaining sections of the 1871 Act were addressed. Representative Shellabarger also stated without reservation that the constitutionality of § 2 of the Civil Rights Act of 1866 controlled the constitutionality of § 1 of the 1871 Act, and that the former had been <span class="star-pagination">*684</span> approved by "the supreme courts of at least three States of this Union" and by Mr. Justice Swayne, sitting on circuit, who had concluded: "`We have no doubt of the constitutionality of every provision of this act.'" Globe App. 68. Representative Shellabarger then went on to describe how the courts would and should interpret § 1:</p>
<blockquote>"This act is remedial, and in aid of the preservation of human liberty and human rights. All statutes and constitutional provisions authorizing such statutes are liberally and beneficently construed. It would be most strange and, in civilized law, monstrous were this not the rule of interpretation. As has been again and again decided by your own Supreme Court of the United States, and everywhere else where there is wise judicial interpretation, the largest latitude consistent with the words employed is uniformly given in construing such statutes and constitutional provisions as are meant to protect and defend and give remedies for their wrongs to all the people. . . . Chief Justice Jay and also Story say:</blockquote>
<blockquote>"`Where a power is remedial in its nature there is much reason to contend that it ought to be construed liberally, and it is generally adopted in the interpretation of laws.'1 <i>Story on Constitution,</i> sec. 429." Globe App., at 68.</blockquote>
<p>The sentiments expressed in Representative Shellabarger's opening speech were echoed by Senator Edmunds, the manager of H. R. 320 in the Senate:</p>
<blockquote>"The first section is one that I believe nobody objects to, as defining the rights secured by the Constitution of the United States when they are assailed by any State law or under color of any State law, and it is merely carrying out the principles of the civil rights bill [of 1866], which have since become a part of the Constitution." Globe 568.</blockquote>
<blockquote>
<span class="star-pagination">*685</span> "[Section 1 is] so very simple and really reënact[s] the Constitution." <i>Id.,</i> at 569.</blockquote>
<p>And he agreed that the bill "secure[d] the rights of white men as much as of colored men." <i>Id.,</i> at 696.</p>
<p>In both Houses, statements of the supporters of § 1 corroborated that Congress, in enacting § 1, intended to give a broad remedy for violations of federally protected civil rights.<sup>[45]</sup> Moreover, since municipalities through their official <span class="star-pagination">*686</span> acts could, equally with natural persons, create the harms intended to be remedied by § 1, and, further, since Congress intended § 1 to be broadly construed, there is no reason to suppose that municipal corporations would have been excluded from the sweep of § 1. Cf., <i>e. g., </i><i>Ex parte Virginia,</i> <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/#346" aria-description="Citation for case: Ex Parte Virginia">100 U. S. 339, 346-347</a></span> (1880); <i>Home Tel. &amp; Tel. Co.</i> v. <i>Los Angeles,</i> <span class="citation" data-id="97779"><a href="/opinion/97779/home-telephone-telegraph-co-v-city-of-los-angeles/#286" aria-description="Citation for case: Home Telephone &amp; Telegraph Co. v. City of Los Angeles">227 U. S. 278, 286-287, 294-296</a></span> (1913). One need not rely on this inference alone, however, for the debates show that Members of Congress understood "persons" to include municipal corporations.</p>
<p>Representative Bingham, for example, in discussing § 1 of the bill, explained that he had drafted § 1 of the Fourteenth Amendment with the case of <i>Barron</i> v. <i>Mayor of Baltimore,</i> <span class="citation" data-id="85827"><a href="/opinion/85827/barron-ex-rel-tiernan-v-mayor-of-baltimore/" aria-description="Citation for case: Barron Ex Rel. Tiernan v. Mayor of Baltimore">7 Pet. 243</a></span> (1833), especially in mind. "In [that] case the <span class="star-pagination">*687</span> <i>city</i> had taken private property for public use, without compensation. . ., and there was no redress for the wrong . . . ." Globe App. 84 (emphasis added). Bingham's further remarks clearly indicate his view that such takings by cities, as had occurred in <i><span class="citation" data-id="85827"><a href="/opinion/85827/barron-ex-rel-tiernan-v-mayor-of-baltimore/" aria-description="Citation for case: Barron Ex Rel. Tiernan v. Mayor of Baltimore">Barron</a></span>,</i> would be redressable under § 1 of the bill. See Globe App. 85. More generally, and as Bingham's remarks confirm, § 1 of the bill would logically be the vehicle by which Congress provided redress for takings, since that section provided the only civil remedy for Fourteenth Amendment violations and that Amendment unequivocally prohibited uncompensated takings.<sup>[46]</sup> Given this purpose, it beggars reason to suppose that Congress would have exempted municipalities from suit, insisting instead that compensation for a taking come from an officer in his individual capacity rather than from the government unit that had the benefit of the property taken.<sup>[47]</sup></p>
<p>In addition, by 1871, it was well understood that corporations should be treated as natural persons for virtually all purposes of constitutional and statutory analysis. This had not always been so. When this Court first considered the question of the status of corporations, Mr. Chief Justice Marshall, writing for the Court, denied that corporations "as such" were persons as that term was used in Art. III and the Judiciary Act of 1789. See <i>Bank of the </i><i>United States</i> v. <i>Deveaux,</i> <span class="citation" data-id="84894"><a href="/opinion/84894/bank-of-the-united-states-v-deveaux/#86" aria-description="Citation for case: Bank of the United States v. Deveaux">5 Cranch 61, 86</a></span> (1809).<sup>[48]</sup> By 1844, however, the <i><span class="citation" data-id="84894"><a href="/opinion/84894/bank-of-the-united-states-v-deveaux/" aria-description="Citation for case: Bank of the United States v. Deveaux">Deveaux</a></span></i> doctrine was unhesitatingly abandoned:</p>
<blockquote>"[A] corporation created by and doing business in a particular <span class="star-pagination">*688</span> state, is to be deemed <i>to all intents and purposes as a person,</i> although an artificial person, . . . capable of being treated as a citizen of that state, as much as a natural person." <i>Louisville R. Co.</i> v. <i>Letson,</i> <span class="citation" data-id="86293"><a href="/opinion/86293/louisville-cincinnati-charleston-rail-road-v-letson/#558" aria-description="Citation for case: Louisville, Cincinnati, &amp; Charleston Rail-Road v. Letson">2 How. 497, 558</a></span> (1844) (emphasis added), discussed in Globe 752.</blockquote>
<p>And only two years before the debates on the Civil Rights Act, in <i>Cowles</i> v. <i>Mercer County,</i> <span class="citation" data-id="87989"><a href="/opinion/87989/cowles-v-mercer-county/#121" aria-description="Citation for case: Cowles v. Mercer County">7 Wall. 118, 121</a></span> (1869), the <i><span class="citation" data-id="86293"><a href="/opinion/86293/louisville-cincinnati-charleston-rail-road-v-letson/" aria-description="Citation for case: Louisville, Cincinnati, &amp; Charleston Rail-Road v. Letson">Letson</a></span></i> principle was automatically and without discussion extended to municipal corporations. Under this doctrine, municipal corporations were routinely sued in the federal courts<sup>[49]</sup> and this fact was well known to Members of Congress.<sup>[50]</sup></p>
<p>That the "usual" meaning of the word "person" would extend to municipal corporations is also evidenced by an Act of Congress which had been passed only months before the Civil Rights Act was passed. This Act provided that</p>
<blockquote>"in all acts hereafter passed . . . the word `person' may extend and be applied to bodies politic and corporate. . . unless the context shows that such words were intended to be used in a more limited sense." Act of Feb. 25, 1871, § 2, <span class="citation no-link">16 Stat. 431</span>.</blockquote>
<p>Municipal corporations in 1871 were included within the phrase "bodies politic and corporate"<sup>[51]</sup> and, accordingly, the <span class="star-pagination">*689</span> "plain meaning" of § 1 is that local government bodies were to be included within the ambit of the persons who could be sued under § 1 of the Civil Rights Act. Indeed, a Circuit Judge, writing in 1873 in what is apparently the first reported case under § 1, read the Dictionary Act in precisely this way in a case involving a corporate plaintiff and a municipal defendant.<sup>[52]</sup> See <i>Northwestern Fertilizing Co.</i> v. <i>Hyde Park,</i> <span class="citation" data-id="9299595"><a href="/opinion/9304502/northwestern-fertilizing-co-v-park/#394" aria-description="Citation for case: Northwestern Fertilizing Co. v. Park">18 F. Cas. 393, 394</a></span> (No. 10,336) (CC ND Ill. 1873).<sup>[53]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*690</span> II</h2>
<p>Our analysis of the legislative history of the Civil Rights Act of 1871 compels the conclusion that Congress <i>did</i> intend municipalities and other local government units to be included among those persons to whom § 1983 applies.<sup>[54]</sup> Local governing bodies,<sup>[55]</sup> therefore, can be sued directly under § 1983 for monetary, declaratory, or injunctive relief where, as here, the action that is alleged to be unconstitutional implements or executes a policy statement, ordinance, regulation, or decision officially adopted and promulgated by that body's officers. Moreover, although the touchstone of the § 1983 action against a government body is an allegation that official policy is responsible for a deprivation of rights protected by the Constitution, local governments, like every other § 1983 "person," by the very terms of the statute, may be sued for constitutional <span class="star-pagination">*691</span> deprivations visited pursuant to governmental "custom" even though such a custom has not received formal approval through the body's official decisionmaking channels. As Mr. Justice Harlan, writing for the Court, said in <i>Adickes</i> v. <i>S. H. Kress &amp; Co.,</i> <span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#167" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U. S. 144, 167-168</a></span> (1970): "Congress included customs and usages [in § 1983] because of the persistent and widespread discriminatory practices of state officials . . . . Although not authorized by written law, such practices of state officials could well be so permanent and well settled as to constitute a `custom or usage' with the force of law."<sup>[56]</sup></p>
<p>On the other hand, the language of § 1983, read against the background of the same legislative history, compels the conclusion that Congress did not intend municipalities to be held liable unless action pursuant to official municipal policy of some nature caused a constitutional tort. In particular, we conclude that a municipality cannot be held liable <i>solely</i> because it employs a tortfeasoror, in other words, a municipality cannot be held liable under § 1983 on a <i>respondeat superior</i> theory.</p>
<p>We begin with the language of § 1983 as originally passed:</p>
<blockquote>"[<i>A</i>]<i>ny person who,</i> under color of any law, statute, ordinance, regulation, custom, or usage of any State, <i>shall subject, or cause to be subjected,</i> any person . . . to the deprivation of any rights, privileges, or immunities secured by the Constitution of the United States, shall, any such <span class="star-pagination">*692</span> law, statute, ordinance, regulation, custom, or usage of the State to the contrary notwithstanding, be liable to the party injured in any action at law, suit in equity, or other proper proceeding for redress . . . ." <span class="citation no-link">17 Stat. 13</span> (emphasis added).</blockquote>
<p>The italicized language plainly imposes liability on a government that, under color of some official policy, "causes" an employee to violate another's constitutional rights. At the same time, that language cannot be easily read to impose liability vicariously on governing bodies solely on the basis of the existence of an employer-employee relationship with a tortfeasor. Indeed, the fact that Congress did specifically provide that A's tort became B's liability if B "caused" A to subject another to a tort suggests that Congress did not intend § 1983 liability to attach where such causation was absent.<sup>[57]</sup> See <i>Rizzo</i> v. <i>Goode,</i> <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/#370" aria-description="Citation for case: Rizzo v. Goode">423 U. S. 362, 370-371</a></span> (1976).</p>
<p><span class="star-pagination">*693</span> Equally important, creation of a federal law of <i>respondeat superior</i> would have raised all the constitutional problems associated with the obligation to keep the peace, an obligation Congress chose not to impose because it thought imposition of such an obligation unconstitutional. To this day, there is disagreement about the basis for imposing liability on an employer for the torts of an employee when the sole nexus between the employer and the tort is the fact of the employer-employee relationship. See W. Prosser, Law of Torts § 69, p. 459 (4th ed. 1971). Nonetheless, two justifications tend to stand out. First is the common-sense notion that no matter how blameless an employer appears to be in an individual case, accidents might nonetheless be reduced if employers had to bear the cost of accidents. See, <i>e. g., ibid.;</i> 2 F. Harper &amp; F. James, Law of Torts, § 26.3, pp. 1368-1369 (1956). Second is the argument that the cost of accidents should be <span class="star-pagination">*694</span> spread to the community as a whole on an insurance theory. See, <i>e. g., id.,</i> § 26.5; Prosser, <i>supra,</i> at 459.<sup>[58]</sup></p>
<p>The first justification is of the same sort that was offered for statutes like the Sherman amendment: "The obligation to make compensation for injury resulting from riot is, by arbitrary enactment of statutes, affirmatory law, and the reason of passing the statute is to secure a more perfect police regulation." Globe 777 (Sen. Frelinghuysen). This justification was obviously insufficient to sustain the amendment against perceived constitutional difficulties and there is no reason to suppose that a more general liability imposed for a similar reason would have been thought less constitutionally objectionable. The second justification was similarly put forward as a justification for the Sherman amendment: "we do not look upon [the Sherman amendment] as a punishment. . . . It is a mutual insurance." <i>Id.,</i> at 792 (Rep. Butler). Again, this justification was insufficient to sustain the amendment.</p>
<p>We conclude, therefore, that a local government may not be sued under § 1983 for an injury inflicted solely by its employees or agents. Instead, it is when execution of a government's policy or custom, whether made by its lawmakers or by those whose edicts or acts may fairly be said to represent official policy, inflicts the injury that the government as an entity is responsible under § 1983. Since this case unquestionably involves official policy as the moving force of the constitutional violation found by the District Court, see <i>supra,</i> at <span class="star-pagination">*695</span> 660-662, and n. 2, we must reverse the judgment below. In so doing, we have no occasion to address, and do not address, what the full contours of municipal liability under § 1983 may be. We have attempted only to sketch so much of the § 1983 cause of action against a local government as is apparent from the history of the 1871 Act and our prior cases, and we expressly leave further development of this action to another day.</p>
<p></p>
<h2>III</h2>
<p>Although we have stated that <i>stare decisis</i> has more force in statutory analysis than in constitutional adjudication because, in the former situation, Congress can correct our mistakes through legislation, see, <i>e. g., </i><i>Edelman</i> v. <i>Jordan,</i> <span class="citation" data-id="9425645"><a href="/opinion/108990/edelman-v-jordan/#671" aria-description="Citation for case: Edelman v. Jordan">415 U. S. 651, 671</a></span>, and n. 14 (1974), we have never applied <i>stare decisis</i> mechanically to prohibit overruling our earlier decisions determining the meaning of statutes. See, <i>e. g., </i><i>Continental T. V., Inc.</i> v. <i>GTE Sylvania Inc.,</i> <span class="citation" data-id="9426918"><a href="/opinion/109716/continental-t-v-inc-v-gte-sylvania-inc/#47" aria-description="Citation for case: Continental T. v.  Inc. v. GTE Sylvania Inc.">433 U. S. 36, 47-49</a></span> (1977); <i>Burnet v. Coronado Oil &amp; Gas Co.,</i> <span class="citation" data-id="8148759"><a href="/opinion/8186832/burnet-v-coronado-oil-gas-co/" aria-description="Citation for case: Burnet v. Coronado Oil &amp; Gas Co.">285 U. S. 393</a></span>, 406 n. 1 (1932) (Brandeis, J., dissenting) (collecting cases). Nor is this a case where we should "place on the shoulders of Congress the burden of the Court's own error." <i>Girouard</i> v. <i>United States,</i> <span class="citation" data-id="9419823"><a href="/opinion/104285/girouard-v-united-states/#70" aria-description="Citation for case: Girouard v. United States">328 U. S. 61, 70</a></span> (1946).</p>
<p>First, <i>Monroe</i> v. <i>Pape</i><i>,</i> insofar as it completely immunizes municipalities from suit under § 1983, was a departure from prior practice. See, <i>e. g., </i><i>Northwestern Fertilizing Co.</i> v. <i>Hyde Park,</i> <span class="citation" data-id="9299595"><a href="/opinion/9304502/northwestern-fertilizing-co-v-park/" aria-description="Citation for case: Northwestern Fertilizing Co. v. Park">18 F. Cas. 393</a></span> (No. 10,336) (CC ND Ill. 1873); <i>City of Manchester</i> v. <i>Leiby,</i> <span class="citation" data-id="1480162"><a href="/opinion/1480162/city-of-manchester-v-leiby/" aria-description="Citation for case: City of Manchester v. Leiby">117 F. 2d 661</a></span> (CA1 1941); <i>Hannan</i> v. <i>City of Haverhill,</i> <span class="citation" data-id="1490664"><a href="/opinion/1490664/hannan-v-city-of-haverhill/" aria-description="Citation for case: Hannan v. City of Haverhill">120 F. 2d 87</a></span> (CA1 1941); <i>Douglas</i> v. <i>City of Jeannette,</i> <span class="citation" data-id="9419344"><a href="/opinion/103833/douglas-v-city-of-jeannette/" aria-description="Citation for case: Douglas v. City of Jeannette">319 U. S. 157</a></span> (1943); <i>Holmes</i> v. <i>Atlanta,</i> <span class="citation" data-id="8928384"><a href="/opinion/8938007/holmes-v-city-of-atlanta/" aria-description="Citation for case: Holmes v. City of Atlanta">350 U. S. 879</a></span> (1955), in each of which municipalities were defendants in § 1983 suits.<sup>[59]</sup> Moreover, the constitutional defect <span class="star-pagination">*696</span> that led to the rejection of the Sherman amendment would not have distinguished between municipalities and school boards, each of which is an instrumentality of state administration. See <i>supra,</i> at 673-682. For this reason, our casesdecided both before and after <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> see n. <span class="citation" data-id="334135"><a href="/opinion/334135/12-fair-emplpraccas-836-11-empl-prac-dec-p-10755-jane-monell-v/" aria-description="Citation for case: 12 Fair empl.prac.cas. 836, 11 Empl. Prac. Dec. P 10,755...">5, <i>supra</i></a></span> holding school boards liable in § 1983 actions are inconsistent with <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> especially as <i>Monroe's</i> immunizing principle was extended to suits for injunctive relief in <i>City of Kenosha</i> v. <i>Bruno,</i> <span class="citation" data-id="9425343"><a href="/opinion/108813/city-of-kenosha-v-bruno/" aria-description="Citation for case: City of Kenosha v. Bruno">412 U. S. 507</a></span> (1973).<sup>[60]</sup> And although in many of these cases jurisdiction was not questioned, we ought not "disregard the implications of an exercise of judicial authority assumed to be proper for [100] years." <i>Brown Shoe Co.</i> v. <i>United States,</i> <span class="citation" data-id="9422445"><a href="/opinion/106440/brown-shoe-co-v-united-states/#307" aria-description="Citation for case: Brown Shoe Co. v. United States">370 U. S. 294, 307</a></span> (1962); see <i>Bank of the </i><i>United States</i> v. <i>Deveaux,</i> <span class="citation" data-id="84894"><a href="/opinion/84894/bank-of-the-united-states-v-deveaux/#88" aria-description="Citation for case: Bank of the United States v. Deveaux">5 Cranch, at 88</a></span> (Marshall, C. J.) ("Those decisions are not cited as authority . . . but they have much weight, as they show that this point neither occurred to the bar or the bench"). Thus, while we have reaffirmed <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> without further examination on three occasions,<sup>[61]</sup> it can scarcely be said that <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> is so consistent with the warp and woof of civil rights law as to be beyond question.</p>
<p>Second, the principle of blanket immunity established in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> cannot be cabined short of school boards. Yet such an extension would itself be inconsistent with recent expressions of congressional intent. In the wake of our decisions, Congress not only has shown no hostility to federal-court decisions against school boards, but it has indeed rejected efforts to strip the federal courts of jurisdiction over school boards.<sup>[62]</sup> Moreover, recognizing that school boards are often <span class="star-pagination">*697</span> defendants in school desegregation suits, which have almost without exception been § 1983 suits, Congress has twice passed legislation authorizing grants to school boards to assist them in complying with federal-court decrees.<sup>[63]</sup> Finally, in <span class="star-pagination">*698</span> regard to the Civil Rights Attorney's Fees Awards Act of 1976, <span class="citation no-link">90 Stat. 2641</span>, <span class="citation no-link">42 U. S. C. § 1988</span> (1976 ed.), which allows prevailing parties (in the discretion of the court) in § 1983 suits <span class="star-pagination">*699</span> to obtain attorney's fees from the losing parties, the Senate stated:</p>
<blockquote>"[D]efendants in these cases are often State or local <i>bodies</i> or State or local officials. In such cases it is intended that the attorneys' fees, like other items of costs, will be collected either directly from the official, <i>in his official capacity,</i> from funds of his agency or under his control, or <i>from the State or local government (whether or not the agency or government is a named party)."</i> S. Rep. No. 94-1011, p. 5 (1976) (emphasis added; footnotes omitted).</blockquote>
<p>Far from showing that Congress has relied on <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> therefore, events since 1961 show that Congress has refused to extend the benefits of <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> to school boards and has attempted to allow awards of attorney's fees against local governments even though <i>Monroe, City of Kenosha</i> v. <i><span class="citation" data-id="9425343"><a href="/opinion/108813/city-of-kenosha-v-bruno/" aria-description="Citation for case: City of Kenosha v. Bruno">Bruno</a></span>,</i> and <i>Aldinger</i> v. <i>Howard,</i> <span class="citation" data-id="9426488"><a href="/opinion/109503/aldinger-v-howard/" aria-description="Citation for case: Aldinger v. Howard">427 U. S. 1</a></span> (1976), have made the joinder of such governments impossible.<sup>[64]</sup></p>
<p>Third, municipalities can assert no reliance claim which can <span class="star-pagination">*700</span> support an absolute immunity. As Mr. Justice Frankfurter said in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> "[t]his is not an area of commercial law in which, presumably, individuals may have arranged their affairs in reliance on the expected stability of decision." <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#221" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 221-222</a></span> (dissenting in part). Indeed, municipalities simply cannot "arrange their affairs" on an assumption that they can violate constitutional rights indefinitely since injunctive suits against local officials under § 1983 would prohibit any such arrangement. And it scarcely need be mentioned that nothing in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> encourages municipalities to violate constitutional rights or even suggests that such violations are anything other than completely wrong.</p>
<p>Finally, even under the most stringent test for the propriety of overruling a statutory decision proposed by Mr. Justice Harlan in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i><sup>[65]</sup>"that it appear beyond doubt from the legislative history of the 1871 statute that <i>[Monroe]</i> misapprehended the meaning of the [section]," <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#192" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 192</a></span> (concurring opinion)the overruling of <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> insofar as it holds that local governments are not "persons" who may be defendants in § 1983 suits is clearly proper. It is simply beyond doubt that, under the 1871 Congress' view of the law, were § 1983 liability unconstitutional as to local governments, it would have been equally unconstitutional as to state officers. Yet everyoneproponents and opponents alikeknew § 1983 would be applied to state officers and nonetheless stated that § 1983 was constitutional. See <i>supra,</i> at 680-682. And, moreover, there can be no doubt that § 1 of the Civil Rights Act was intended to provide a remedy, to be broadly construed, against all forms of official violation of federally protected <span class="star-pagination">*701</span> rights. Therefore, absent a clear statement in the legislative history supporting the conclusion that § 1 was not to apply to the official acts of a municipal corporationwhich simply is not presentthere is no justification for excluding municipalities from the "persons" covered by § 1.</p>
<p>For the reasons stated above, therefore, we hold that <i>stare decisis</i> does not bar our overruling of <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> insofar as it is inconsistent with Parts I and II of this opinion.<sup>[66]</sup></p>
<p></p>
<h2>IV</h2>
<p>Since the question whether local government bodies should be afforded some form of official immunity was not presented as a question to be decided on this petition and was not briefed by the parties or addressed by the courts below, we express no views on the scope of any municipal immunity beyond holding that municipal bodies sued under § 1983 cannot be entitled to an absolute immunity, lest our decision that such bodies are subject to suit under § 1983 "be drained of meaning," <i>Scheuer</i> v. <i>Rhodes,</i> <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#248" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232, 248</a></span> (1974). Cf. <i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#397" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388, 397-398</a></span> (1971).</p>
<p></p>
<h2>
<span class="star-pagination">*702</span> V</h2>
<p>For the reasons stated above, the judgment of the Court of Appeals is</p>
<p><i>Reversed.</i></p>
<p></p>
<h2>APPENDIX TO OPINION OF THE COURT</h2>
<p>As proposed, the Sherman amendment was as follows:</p>
<blockquote>"That if any house, tenement, cabin, shop, building, barn, or granary shall be unlawfully or feloniously demolished, pulled down, burned, or destroyed, wholly or in part, by any persons riotously and tumultuously assembled together; or if any person shall unlawfully and with force and violence be whipped, scourged, wounded, or killed by any persons riotously and tumultuously assembled together; and if such offense was committed to deprive any person of any right conferred upon him by the Constitution and laws of the United States, or to deter him or punish him for exercising such right, or by reason of his race, color, or previous condition of servitude, in every such case the inhabitants of the county, city, or parish in which any of the said offenses shall be committed shall be liable to pay full compensation to the person or persons damnified by such offense if living, or to his widow or legal representative if dead; and such compensation may be recovered by such person or his representative by a suit in any court of the United States of competent jurisdiction in the district in which the offense was committed, to be in the name of the person injured, or his legal representative, and against said county, city, or parish. And execution may be issued on a judgment rendered in such suit and may be levied upon any property, real or personal, of any person in said county, city, or parish, and the said county, city, or parish may recover the full amount of such judgment, costs and interest, <span class="star-pagination">*703</span> from any person or persons engaged as principal or accessory in such riot in an action in any court of competent jurisdiction." Globe 663.</blockquote>
<p>The complete text of the first conference substitute for the Sherman amendment is:</p>
<blockquote>"That if any house, tenement, cabin, shop, building, barn, or granary shall be unlawfully or feloniously demolished, pulled down, burned, or destroyed, wholly or in part, by any persons riotously and tumultuously assembled together; or if any person shall unlawfully and with force and violence be whipped, scourged, wounded, or killed by any persons riotously and tumultuously assembled together, with intent to deprive any person of any right conferred upon him by the Constitution and laws of the United States, or to deter him or punish him for exercising such right, or by reason of his race, color, or previous condition of servitude, in every such case the county, city, or parish in which any of the said offenses shall be committed shall be liable to pay full compensation to the person or persons damnified by such offense, if living, or to his widow or legal representative if dead; and such compensation may be recovered in an action on the case by such person or his representative in any court of the United States of competent jurisdiction in the district in which the offense was committed, such action to be in the name of the person injured, or his legal representative, and against said county, city, or parish, and in which action any of the parties committing such acts may be joined as defendants. And any payment of any judgment, or part thereof unsatisfied, recovered by the plaintiff in such action, may, if not satisfied by the individual defendant therein within two months next after the recovery of such judgment upon execution duly issued against such individual defendant in such judgment, and returned unsatisfied, in whole or in part, be enforced <span class="star-pagination">*704</span> against such county, city, or parish, by execution, attachment, mandamus, garnishment, or any other proceeding in aid of execution or applicable to the enforcement of judgments against municipal corporations; and such judgment shall be a lien as well upon all moneys in the treasury of such county, city, or parish, as upon the other property thereof. And the court in any such action may on motion cause additional parties to be made therein prior to issue joined, to the end that justice may be done. And the said county, city, or parish may recover the full amount of such judgment, by it paid, with costs and interest, from any person or persons engaged as principal or accessory in such riot, in an action in any court of competent jurisdiction. And such county, city, or parish, so paying, shall also be subrogated to all the plaintiff's rights under such judgment." <i>Id.,</i> at 749, 755.</blockquote>
<p>The relevant text of the second conference substitute for the Sherman amendment is as follows:</p>
<blockquote>"[A]ny person or persons having knowledge that any of the wrongs conspired to be done and mentioned in the second section of this act are about to be committed, and having power to prevent or aid in preventing the same, <i>shall neglect or refuse so to do,</i> and such wrongful act shall be committed, such person or persons shall be liable to the person injured, or his legal representatives." <i>Id.,</i> at 804 (emphasis added).</blockquote>
<p>MR. JUSTICE POWELL, concurring.</p>
<p>I join the opinion of the Court, and express these additional views.</p>
<p>Few cases in the history of the Court have been cited more frequently than <i>Monroe</i> v. <i>Pape,</i> <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167</a></span> (1961), decided less than two decades ago. Focusing new light on <span class="citation no-link">42 U. S. C. § 1983</span>, that decision widened access to the federal courts and permitted expansive interpretations of the reach of <span class="star-pagination">*705</span> the 1871 measure. But <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> exempted local governments from liability at the same time it opened wide the courthouse door to suits against officers and employees of those entitieseven when they act pursuant to express authorization. The oddness of this result, and the weakness of the historical evidence relied on by the <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> Court in support of it, are well demonstrated by the Court's opinion today. Yet the gravity of overruling a part of so important a decision prompts me to write.</p>
<p></p>
<h2>I</h2>
<p>In addressing a complaint alleging unconstitutional police conduct that probably was unauthorized and actionable under state law,<sup>[1]</sup> the <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> Court treated the 42d Congress' rejection of the Sherman amendment as conclusive evidence of an intention to immunize local governments from all liability under the statute for constitutional injury. That reading, in light of today's thorough canvass of the legislative history, clearly "misapprehended the meaning of the controlling provision," <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#192" aria-description="Citation for case: Monroe v. Pape"><i>Monroe, supra,</i> at 192</a></span> (Harlan, J., concurring). In this case, involving formal, written policies of the Department of Social Services and the Board of Education of the city of New York that are alleged to conflict <span class="star-pagination">*706</span> with the command of the Due Process Clause, cf. <i>Cleveland Board of Education</i> v. <i>LaFleur,</i> <span class="citation" data-id="9425515"><a href="/opinion/108913/cleveland-board-of-education-v-lafleur/" aria-description="Citation for case: Cleveland Board of Education v. LaFleur">414 U. S. 632</a></span> (1974), the Court decides "not to reject [wisdom] merely because it comes late," <i>Henslee</i> v. <i>Union Planters Bank,</i> <span class="citation" data-id="9420257"><a href="/opinion/104614/henslee-v-union-planters-national-bank-trust-co/#600" aria-description="Citation for case: Henslee v. Union Planters National Bank &amp; Trust Co.">335 U. S. 595, 600</a></span> (1949) (Frankfurter, J., dissenting).</p>
<p>As the Court demonstrates, the Sherman amendment presented an extreme example of "riot act" legislation that sought to impose vicarious liability on government subdivisions for the consequences of private lawlessness. As such, it implicated concerns that are of marginal pertinence to the operative principle of § 1 of the 1871 legislationnow § 1983that "any person" acting "under color of" state law may be held liable for affirmative conduct that "subjects, or causes to be subjected, any person . . . to the deprivation of any" federal constitutional or statutory right. Of the many reasons for the defeat of the Sherman proposal, none supports <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i>'s observation that the 42d Congress was fundamentally "antagonistic," <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#191" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 191</a></span>, to the proposition that government entities and natural persons alike should be held accountable for the consequences of conduct directly working a constitutional violation. Opponents in the Senate appear to have been troubled primarily by the proposal's unprecedented lien provision, which would have exposed even property held for public purposes to the demands of § 1983 judgment lienors. <i>Ante,</i> at 673-674, n. 30. The opposition in the House of Representatives focused largely on the Sherman amendment's attempt to impose a peacekeeping obligation on municipalities when the Constitution itself imposed no such affirmative duty and when many municipalities were not even empowered under state law to maintain police forces. <i>Ante,</i> at 673-675, 679-682.<sup>[2]</sup></p>
<p><span class="star-pagination">*707</span> The Court correctly rejects a view of the legislative history that would produce the anomalous result of immunizing local government units from monetary liability for action directly causing a constitutional deprivation, even though such actions may be fully consistent with, and thus not remediable under, state law. No conduct of government comes more clearly within the "under color of" state law language of § 1983. It is most unlikely that Congress intended public officials acting under the command or the specific authorization of the government employer to be <i>exclusively</i> liable for resulting constitutional injury.<sup>[3]</sup></p>
<p>As elaborated in Part II of today's opinion, the rejection of the Sherman amendment can best be understood not as evidence of Congress' acceptance of a rule of absolute municipal immunity but as a limitation of the statutory ambit to actual wrongdoers, <i>i. e.,</i> a rejection of <i>respondeat superior</i> or any other principle of vicarious liability. Cf. Levin, The Section 1983 Municipal Immunity Doctrine, 65 Geo. L. J. 1483, 1531-1535 (1977). Thus, it has been clear that a public official may be held liable in damages when his actions are found to violate a constitutional right and there is no qualified immunity, see <i>Wood</i> v. <i>Strickland,</i> <span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308</a></span> (1975); <i>Procunier</i> v. <i>Navarette,</i> <span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/" aria-description="Citation for case: Procunier v. Navarette">434 U. S. 555</a></span> (1978). Today the Court recognizes <span class="star-pagination">*708</span> that this principle also applies to a local government when implementation of its official policies or established customs inflicts the constitutional injury.</p>
<p></p>
<h2>II</h2>
<p>This Court traditionally has been hesitant to overrule prior constructions of statutes or interpretations of common-law rules. "<i>Stare decisis</i> is usually the wise policy," <i>Burnet</i> v. <i>Coronado Oil &amp; Gas Co.,</i> <span class="citation" data-id="8148759"><a href="/opinion/8186832/burnet-v-coronado-oil-gas-co/#406" aria-description="Citation for case: Burnet v. Coronado Oil &amp; Gas Co.">285 U. S. 393, 406</a></span> (1932) (Brandeis, J., dissenting), but this cautionary principle must give way to countervailing considerations in appropriate circumstances.<sup>[4]</sup> I concur in the Court's view that this is not a case where we should "place on the shoulders of Congress the burden of the Court's own error." <i>Girouard</i> v. <i>United States,</i> <span class="citation" data-id="9419823"><a href="/opinion/104285/girouard-v-united-states/#70" aria-description="Citation for case: Girouard v. United States">328 U. S. 61, 70</a></span> (1946).</p>
<p>Nor is this the usual case in which the Court is asked to overrule a precedent. Here considerations of <i>stare decisis</i> cut in both directions. On the one hand, we have a series of rulings that municipalities and counties are not "persons" for purposes of § 1983. On the other hand, many decisions of this Court have been premised on the amenability of school boards and similar entities to § 1983 suits.</p>
<p>In <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> and its progeny, we have answered a question that was never actually briefed or argued in this Court whether a municipality is liable in damages for injuries that are the direct result of its official policies. "The theory of the complaint [in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> was] that under the circumstances [t]here alleged the City [was] liable for the acts of its police officers, by virtue of <i>respondeat superior.</i>" Brief for Petitioners, <span class="star-pagination">*709</span> O. T. 1960, No. 39, p. 21.<sup>[5]</sup> Respondents answered that adoption of petitioners' position would expose "Chicago and every other municipality in the United States . . . to Civil Rights Act liability through no action of its own and based on action contrary to its own ordinances and the laws of the state it is a part of." Brief for Respondents, O. T. 1960, No. 39, p. 26. Thus the ground of decision in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> was not advanced by either party and was broader than necessary to resolve the contentions made in that case.<sup>[6]</sup></p>
<p><span class="star-pagination">*710</span> Similarly, in <i>Moor</i> v. <i>County of Alameda,</i> <span class="citation" data-id="9425281"><a href="/opinion/108782/moor-v-county-of-alameda/" aria-description="Citation for case: Moor v. County of Alameda">411 U. S. 693</a></span> (1973), petitioners asserted that "the County was vicariously liable for the acts of its deputies and sheriff," <span class="citation" data-id="9425281"><a href="/opinion/108782/moor-v-county-of-alameda/#696" aria-description="Citation for case: Moor v. County of Alameda"><i>id.,</i> at 696</a></span>, under <span class="citation no-link">42 U. S. C. § 1988</span>. In rejecting this vicarious-liability claim, <span class="citation" data-id="9425281"><a href="/opinion/108782/moor-v-county-of-alameda/#710" aria-description="Citation for case: Moor v. County of Alameda">411 U. S., at 710</a></span>, and n. 27, we reaffirmed <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i>'s reading of the statute, but there was no challenge in that case to "the holding in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> concerning the status under § 1983 of public entities such as the County," <span class="citation" data-id="9425281"><a href="/opinion/108782/moor-v-county-of-alameda/#700" aria-description="Citation for case: Moor v. County of Alameda">411 U. S., at 700</a></span>; Brief for Petitioners, O. T. 1972, No. 72-10, p. 9.</p>
<p>Only in <i>City of Kenosha</i> v. <i>Bruno,</i> <span class="citation" data-id="9425343"><a href="/opinion/108813/city-of-kenosha-v-bruno/" aria-description="Citation for case: City of Kenosha v. Bruno">412 U. S. 507</a></span> (1973), did the Court confront a § 1983 claim based on conduct that was both authorized under state law and the direct cause of the claimed constitutional injury. In <i>Kenosha,</i> however, we raised the issue of the city's amenability to suit under § 1983 on our own initiative.<sup>[7]</sup></p>
<p>This line of casesfrom <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> to <i>Kenosha</i>is difficult to reconcile on a principled basis with a parallel series of cases <span class="star-pagination">*711</span> in which the Court has assumed <i>sub silentio</i> that some local government entities could be sued under § 1983. If now, after full consideration of the question, we continued to adhere to <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> grave doubt would be cast upon the Court's exercise of § 1983 jurisdiction over school boards. See <i>ante,</i> at 663 n. 5. Since "the principle of blanket immunity established in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> cannot be cabined short of school boards," <i>ante,</i> at 696, the conflict is squarely presented. Although there was an independent basis of jurisdiction in many of the school board cases because of the inclusion of individual public officials as nominal parties, the opinions of this Court make explicit reference to the school board party, particularly in discussions of the relief to be awarded, see, <i>e. g., </i><i>Green</i> v. <i>County School Board,</i> <span class="citation" data-id="107705"><a href="/opinion/107705/green-v-county-school-board-of-new-kent-county/#437" aria-description="Citation for case: Green v. County School Board of New Kent County">391 U. S. 430, 437-439, 441-442</a></span> (1968); <i>Milliken</i> v. <i>Bradley,</i> <span class="citation" data-id="9426944"><a href="/opinion/109723/milliken-v-bradley/#292" aria-description="Citation for case: Milliken v. Bradley">433 U. S. 267, 292-293</a></span> (1977) (POWELL, J., concurring in judgment). And, as the Court points out, <i>ante,</i> at 696-697, and nn. 62, 63, Congress has focused specifically on this Court's school board decisions in several statutes. Thus the exercise of § 1983 jurisdiction over school boards, while perhaps not premised on considered holdings, has been longstanding. Indeed, it predated <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>.</i></p>
<p>Even if one attempts to explain away the school board decisions as involving suits which "may be maintained against board members in their official capacities for injunctive relief under either § 1983 or <i>Ex parte Young,</i> <span class="citation" data-id="9418117"><a href="/opinion/96819/ex-parte-young/" aria-description="Citation for case: Ex Parte Young">209 U. S. 123</a></span> (1908)," <i>post,</i> at 716-717, n. 2, some difficulty remains in rationalizing the relevant body of precedents. At least two of the school board cases involved claims for monetary relief. <i>Cohen</i> v. <i>Chesterfield County School Board,</i> <span class="citation" data-id="1460310"><a href="/opinion/1460310/cohen-v-chesterfield-county-school-board/#1161" aria-description="Citation for case: Cohen v. Chesterfield County School Board">326 F. Supp. 1159, 1161</a></span> (ED Va. 1971), rev'd, <span class="citation multiple-matches"><a href="/c/F.%202d/474/395/">474 F. 2d 395</a></span> (CA4 1973), rev'd and remanded, <span class="citation" data-id="9425515"><a href="/opinion/108913/cleveland-board-of-education-v-lafleur/" aria-description="Citation for case: Cleveland Board of Education v. LaFleur">414 U. S. 632</a></span> (1974); <i>Tinker</i> v. <i>Des Moines Independent School Dist.,</i> <span class="citation" data-id="9423907"><a href="/opinion/107841/tinker-v-des-moines-independent-community-school-district/#504" aria-description="Citation for case: Tinker v. Des Moines Independent Community School District">393 U. S. 503, 504</a></span> (1969). See also <i>Vlandis</i> v. <i>Kline,</i> <span class="citation" data-id="9425336"><a href="/opinion/108810/vlandis-v-kline/#445" aria-description="Citation for case: Vlandis v. Kline">412 U. S. 441, 445</a></span> (1973). Although the point was not squarely presented in this Court, these claims <span class="star-pagination">*712</span> for damages could not have been maintained in official-capacity suits if the government entity were not itself suable. Cf. <i>Edelman</i> v. <i>Jordan,</i> <span class="citation" data-id="9425645"><a href="/opinion/108990/edelman-v-jordan/" aria-description="Citation for case: Edelman v. Jordan">415 U. S. 651</a></span> (1974).<sup>[8]</sup> Moreover, the rationale of <i>Kenosha</i> would have to be disturbed to avoid closing all avenues under § 1983 to injunctive relief against constitutional violations by local government. The Court of Appeals in this case suggested that we import, by analogy, the Eleventh Amendment fiction of <i>Ex parte Young</i> into § 1983, <span class="citation" data-id="334135"><a href="/opinion/334135/12-fair-emplpraccas-836-11-empl-prac-dec-p-10755-jane-monell-v/#264" aria-description="Citation for case: 12 Fair empl.prac.cas. 836, 11 Empl. Prac. Dec. P 10,755...">532 F. 2d 259, 264-266</a></span> (CA2 1976). That approach, however, would create tension with <i>Kenosha</i> because it would require "a bifurcated application" of "the generic word `person' in § 1983" to public officials "depending on the nature of the relief sought against them." 412 U. S., at 513. A public official sued in his official capacity for carrying out official policy would be a "person" for purposes of injunctive relief, but a non-"person" in an action for damages. The Court's holding avoids this difficulty. See <i>ante,</i> at 690 n. 55.</p>
<p>Finally, if we continued to adhere to a rule of absolute municipal immunity under § 1983, we could not long avoid the question whether "we should, by analogy to our decision in <i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971), imply a cause of action directly from the Fourteenth Amendment which would not be subject to the limitations contained in § 1983 . . . ." <i>Mt. Healthy City Board of Ed.</i> v. <i>Doyle,</i> <span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/#278" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">429 U. S. 274, 278</a></span> (1977). One aspect of that inquiry would be whether there are any "special factors counselling hesitation in the absence of affirmative action by Congress," <i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#396" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388, 396</a></span> (1971), such as an "explicit congressional declaration <span class="star-pagination">*713</span> that persons injured by a [municipality] may not recover money damages . . ., but must instead be remitted to another remedy, equally effective in the view of Congress," <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#397" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of..."><i>id.,</i> at 397</a></span>. In light of the Court's persuasive re-examination in today's decision of the 1871 debates, I would have difficulty inferring from § 1983 "an explicit congressional declaration" against municipal liability for the implementation of official policies in violation of the Constitution. Rather than constitutionalize a cause of action against local government that Congress intended to create in 1871, the better course is to confess error and set the record straight, as the Court does today.<sup>[9]</sup></p>
<p></p>
<h2>III</h2>
<p>Difficult questions nevertheless remain for another day. There are substantial line-drawing problems in determining "when execution of a government's policy or custom" can be said to inflict constitutional injury such that "government as an entity is responsible under § 1983." <i>Ante,</i> at 694. This case, however, involves formal, written policies of a municipal department and school board; it is the clear case. The Court also reserves decision on the availability of a qualified municipal immunity. <i>Ante,</i> at 701. Initial resolution of the question whether the protection available at common law for municipal corporations, see <i>post,</i> at 720-721, or other principles support a <span class="star-pagination">*714</span> qualified municipal immunity in the context of the § 1983 damages action, is left to the lower federal courts.</p>
<p>MR. JUSTICE STEVENS, concurring in part.</p>
<p>Since Parts II and IV of the opinion of the Court are merely advisory and are not necessary to explain the Court's decision, I join only Parts I, III, and V.</p>
<p>MR. JUSTICE REHNQUIST, with whom THE CHIEF JUSTICE joins, dissenting.</p>
<p>Seventeen years ago, in <i>Monroe</i> v. <i>Pape,</i> <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167</a></span> (1961), this Court held that the 42d Congress did not intend to subject a municipal corporation to liability as a "person" within the meaning of <span class="citation no-link">42 U. S. C. § 1983</span>. Since then, the Congress has remained silent, but this Court has reaffirmed that holding on at least three separate occasions. <i>Aldinger</i> v. <i>Howard,</i> <span class="citation" data-id="9426488"><a href="/opinion/109503/aldinger-v-howard/" aria-description="Citation for case: Aldinger v. Howard">427 U. S. 1</a></span> (1976); <i>City of Kenosha</i> v. <i>Bruno,</i> <span class="citation" data-id="9425343"><a href="/opinion/108813/city-of-kenosha-v-bruno/" aria-description="Citation for case: City of Kenosha v. Bruno">412 U. S. 507</a></span> (1973); <i>Moor</i> v. <i>County of Alameda,</i> <span class="citation" data-id="9425281"><a href="/opinion/108782/moor-v-county-of-alameda/" aria-description="Citation for case: Moor v. County of Alameda">411 U. S. 693</a></span> (1973). See also <i>Mt. Healthy City Board of Ed.</i> v. <i>Doyle,</i> <span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/#277" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">429 U. S. 274, 277-279</a></span> (1977). Today, the Court abandons this long and consistent line of precedents, offering in justification only an elaborate canvass of the same legislative history which was before the Court in 1961. Because I cannot agree that this Court is "free to disregard these precedents," which have been "considered maturely and recently" by this Court, <i>Runyon</i> v. <i>McCrary,</i> <span class="citation" data-id="9426505"><a href="/opinion/109509/runyon-v-mccrary/#186" aria-description="Citation for case: Runyon v. McCrary">427 U. S. 160, 186</a></span> (1976) (POWELL, J., concurring), I am compelled to dissent.</p>
<p></p>
<h2>I</h2>
<p>As this Court has repeatedly recognized, <i><span class="citation" data-id="9426505"><a href="/opinion/109509/runyon-v-mccrary/" aria-description="Citation for case: Runyon v. McCrary">id.,</a></span></i> at 175 n. 12; <i>Edelman</i> v. <i>Jordan,</i> <span class="citation" data-id="9425645"><a href="/opinion/108990/edelman-v-jordan/" aria-description="Citation for case: Edelman v. Jordan">415 U. S. 651</a></span>, 671 n. 14 (1974), considerations of <i>stare decisis</i> are at their strongest when this Court confronts its previous constructions of legislation. In all cases, private parties shape their conduct according to this Court's settled construction of the law, but the Congress is at <span class="star-pagination">*715</span> liberty to correct our mistakes of statutory construction, unlike our constitutional interpretations, whenever it sees fit. The controlling principles were best stated by Mr. Justice Brandeis:</p>
<blockquote>"<i>Stare decisis</i> is usually the wise policy, because in most matters it is more important that the applicable rule of law be settled than that it be settled right. . . . This is commonly true even where the error is a matter of serious concern, provided correction can be had by legislation. But in cases involving the Federal Constitution, where correction through legislative action is practically impossible, this Court has often overruled its earlier decisions." <i>Burnet</i> v. <i>Coronado Oil &amp; Gas Co.,</i> <span class="citation" data-id="8148759"><a href="/opinion/8186832/burnet-v-coronado-oil-gas-co/#406" aria-description="Citation for case: Burnet v. Coronado Oil &amp; Gas Co.">285 U. S. 393, 406-407</a></span> (1932) (dissenting opinion) (footnotes omitted).</blockquote>
<p>Only the most compelling circumstances can justify this Court's abandonment of such firmly established statutory precedents. The best exposition of the proper burden of persuasion was delivered by Mr. Justice Harlan in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> itself:</p>
<blockquote>"From my point of view, the policy of <i>stare decisis,</i> as it should be applied in matters of statutory construction, and, to a lesser extent, the indications of congressional acceptance of this Court's earlier interpretation, require that it appear <i>beyond doubt</i> from the legislative history of the 1871 statute that [<i>United States</i> v.] <i>Classic,</i> [<span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">313 U. S. 299</a></span> (1941)] and <i>Screws</i> [v. <i>United States,</i> <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">325 U. S. 91</a></span> (1945)] misapprehended the meaning of the controlling provision, before a departure from what was decided in those cases would be justified." <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#192" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 192</a></span> (concurring opinion) (footnote omitted; emphasis added).</blockquote>
<p>The Court does not demonstrate that any exception to this general rule is properly applicable here. The Court's first assertion, that <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> "was a departure from prior practice," <i>ante,</i> at 695, is patently erroneous. Neither in <i>Douglas</i> v. <i>City of Jeannette,</i> <span class="citation" data-id="9419344"><a href="/opinion/103833/douglas-v-city-of-jeannette/" aria-description="Citation for case: Douglas v. City of Jeannette">319 U. S. 157</a></span> (1943), nor in <i>Holmes</i> v. <i>Atlanta,</i> <span class="star-pagination">*716</span> <span class="citation" data-id="8928384"><a href="/opinion/8938007/holmes-v-city-of-atlanta/" aria-description="Citation for case: Holmes v. City of Atlanta">350 U. S. 879</a></span> (1955), nor in any of the school board cases cited by the Court, <i>ante,</i> at 663 n. 5, was the question now before us raised by any of the litigants or addressed by this Court. As recently as four Terms ago, we said in <i>Hagans</i> v. <i>Lavine,</i> <span class="citation" data-id="9425636"><a href="/opinion/108987/hagans-v-lavine/" aria-description="Citation for case: Hagans v. Lavine">415 U. S. 528</a></span>, 535 n. 5 (1974):</p>
<blockquote>"Moreover, when questions of jurisdiction have been passed on in prior decisions <i>sub silentio,</i> this Court has never considered itself bound when a subsequent case finally brings the jurisdictional issue before us."</blockquote>
<p>The source of this doctrine that jurisdictional issues decided <i>sub silentio</i> are not binding in other cases seems to be Mr. Chief Justice Marshall's remark in <i>United States</i> v. <i>More,</i> <span class="citation" data-id="6607492"><a href="/opinion/6726239/united-states-v-more/#172" aria-description="Citation for case: United States v. More">3 Cranch 159, 172</a></span> (1805).<sup>[1]</sup> While the Chief Justice also said that such decisions may "have much weight, as they show that this point neither occurred to the bar or the bench," <i>Bank of the </i><i>United States</i> v. <i>Deveaux,</i> <span class="citation" data-id="84894"><a href="/opinion/84894/bank-of-the-united-states-v-deveaux/#88" aria-description="Citation for case: Bank of the United States v. Deveaux">5 Cranch 61, 88</a></span> (1809), unconsidered assumptions of jurisdiction simply cannot outweigh four consistent decisions of this Court, explicitly considering and rejecting that jurisdiction.</p>
<p>Nor is there any indication that any later Congress has ever approved suit against any municipal corporation under § 1983. Of all its recent enactments, only the Civil Rights Attorney's Fees Awards Act of 1976, § 2, <span class="citation no-link">90 Stat. 2641</span>, <span class="citation no-link">42 U. S. C. § 1988</span> (1976 ed.), explicitly deals with the Civil Rights Act of 1871.<sup>[2]</sup> The 1976 Act provides that attorney's fees may be awarded <span class="star-pagination">*717</span> to the prevailing party "[i]n any action or proceeding to enforce a provision of sections 1981, 1982, 1983, 1985, and 1986 of this title." There is plainly no language in the 1976 Act which would enlarge the parties suable under those substantive sections; it simply provides that parties who are already suable may be made liable for attorney's fees. As the Court admits, <i>ante,</i> at 699, the language in the Senate Report stating that liability may be imposed "whether or not the agency or government is a named party," S. Rep. No. 94-1011, p. 5 (1976), suggests that Congress did not view its purpose as being in any way inconsistent with the well-known holding of <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>.</i></p>
<p>The Court's assertion that municipalities have no right to act "on an assumption that they can violate constitutional rights indefinitely," <i>ante,</i> at 700, is simply beside the point. Since <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> municipalities <i>have</i> had the right to expect that they would not be held liable retroactively for their officers' failure to predict this Court's recognition of new constitutional rights. No doubt innumerable municipal insurance policies and indemnity ordinances have been founded on this assumption, which is wholly justifiable under established principles of <i>stare decisis.</i> To obliterate those legitimate expectations without more compelling justifications than those advanced by the Court is a significant departure from our prior practice.</p>
<p>I cannot agree with MR. JUSTICE POWELL's view that "[w]e owe somewhat less deference to a decision that was rendered without benefit of a full airing of all the relevant considerations." <i>Ante,</i> at 709 n. 6. Private parties must be able to rely upon explicitly stated holdings of this Court without being <span class="star-pagination">*718</span> obliged to peruse the briefs of the litigants to predict the likelihood that this Court might change its mind. To cast such doubt upon each of our cases, from <i>Marbury</i> v. <i>Madison,</i> <span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/" aria-description="Citation for case: Marbury v. Madison">1 Cranch 137</a></span> (1803), forward, in which the explicit ground of decision "was never actually briefed or argued," <i>ante,</i> at 708 (POWELL, J., concurring), would introduce intolerable uncertainty into the law. Indeed, in <i><span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/" aria-description="Citation for case: Marbury v. Madison">Marbury</a></span></i> itself, the argument of Charles Lee on behalf of the applicantswhich, unlike the arguments in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> is reproduced in the Reports of this Court where anyone can see itdevotes not a word to the question of whether this Court has the power to invalidate a statute duly enacted by the Congress. Neither this ground of decision nor any other was advanced by Secretary of State Madison, who evidently made no appearance. <span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/#153" aria-description="Citation for case: Marbury v. Madison">1 Cranch, at 153-154</a></span>. More recent landmark decisions of this Court would appear to be likewise vulnerable under my Brother POWELL'S analysis. In <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), none of the parties requested the Court to overrule <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span> (1949); it did so only at the request of an <i>amicus curiae.</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 646</a></span> n. 3. That <i>Marbury, Mapp,</i> and countless other decisions retain their vitality despite their obvious flaws is a necessary byproduct of the adversary system, in which both judges and the general public rely upon litigants to present "all the relevant considerations." <i>Ante,</i> at 709 n. 6 (POWELL, J., concurring). While it undoubtedly has more latitude in the field of constitutional interpretation, this Court is surely not free to abandon settled statutory interpretation at any time a new thought seems appealing.<sup>[3]</sup></p>
<p>Thus, our only task is to discern the intent of the 42d Congress. That intent was first expounded in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> and it <span class="star-pagination">*719</span> has been followed consistently ever since. This is not some esoteric branch of the law in which congressional silence might reasonably be equated with congressional indifference. Indeed, this very year, the Senate has been holding hearings on a bill, S. 35, 95th Cong., 1st Sess. (1977), which would remove the municipal immunity recognized by <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>.</i> 124 Cong. Rec. D117 (daily ed. Feb. 8, 1978). In these circumstances, it cannot be disputed that established principles of <i>stare decisis</i> require this Court to pay the highest degree of deference to its prior holdings. <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> may not be overruled unless it has been demonstrated "beyond doubt from the legislative history of the 1871 statute that [<span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape"><i>Monroe</i></a></span>] misapprehended the meaning of the controlling provision." <i>Monroe,</i> <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#192" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 192</a></span> (Harlan, J., concurring). The Court must show not only that Congress, in rejecting the Sherman amendment, concluded that municipal liability was not unconstitutional, but also that, in enacting § 1, it intended to impose that liability. I am satisfied that no such showing has been made.</p>
<p></p>
<h2>II</h2>
<p>Any analysis of the meaning of the word "person" in § 1983, which was originally enacted as § 1 of the Ku Klux Klan Act of April 20, 1871, <span class="citation no-link">17 Stat. 13</span>, must begin, not with the Sherman amendment, but with the Dictionary Act. The latter Act, which supplied rules of construction for all legislation, provided:</p>
<blockquote>"That in all acts hereafter passed . . . the word `person' may extend and be applied to bodies politic and corporate. . . unless the context shows that such words were intended to be used in a more limited sense . . . ." Act of Feb. 25, 1871, § 2, <span class="citation no-link">16 Stat. 431</span>.</blockquote>
<p>The Act expressly provided that corporations need not be included within the scope of the word "person" where the context suggests a more limited reach. Not a word in the legislative history of the Act gives any indication of the contexts <span class="star-pagination">*720</span> in which Congress felt it appropriate to include a corporation as a person. Indeed, the chief cause of concern was that the Act's provision that "words importing the masculine gender may be applied to females," might lead to an inadvertent extension of the suffrage to women. Cong. Globe, 41st Cong., 3d Sess., 777 (1871) (remarks of Sen. Sawyer).</p>
<p>There are other factors, however, which suggest that the Congress which enacted § 1983 may well have intended the word "person" "to be used in a more limited sense," as <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for ca

[...TRUNCATED 83639 of 203639 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Monroe v. Pape.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Monroe v. Pape"
type: case
citation: "365 U.S. 167 (1961)"
parallel_cite: "81 S. Ct. 473; 5 L. Ed. 2d 492"
neutral_cite: 1961 U.S. LEXIS 1687
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1961
date_decided: 1961-02-20
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 1961-02-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Monroe v. Pape
  varies_by_point: true
  scope_note: "Overruled in part by Monell v. Department of Social Services (1978) as to municipal liability; the 'under color of' state-law holding remains good law."
  point_overrides:
    - point: legacy-limited-monroe-v-pape
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: Monell v. Department of Social Services
          cluster_id: 109881
          cite: 436 U.S. 658
          field_ii: limited
      scope_note: "Overruled in part by Monell v. Department of Social Services (1978) as to municipal liability; the 'under color of' state-law holding remains good law."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106170/monroe-v-pape/"
  cluster_id: 106170
  opinion_id: 106170
  identity_checked: true
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Key — Anchor"
related: ["[[Monell v. Department of Social Services]]", "[[Harlow v. Fitzgerald]]", "[[Graham v. Connor]]"]
aliases: []
tags: ["case", "section-1983", "under-color-of-law", "civil-rights", "federal-remedy"]
holding: "Revived § 1983 as a real federal remedy: 'under color of' state law reaches the MISUSE of authority an officer possesses by virtue of…"
lake:
  record_id: Monroe v. Pape
  status: verified
  projected_at: 2026-07-06
---

# Monroe v. Pape

*365 U.S. 167 (1961)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Thirteen Chicago police officers, without a warrant, broke into the Monroe family's home at dawn, ransacked it, made the family stand naked, and detained Mr. Monroe for questioning. The Monroes sued the officers and the City of Chicago under § 1983. The lower courts dismissed, reading § 1983 not to reach the officers' conduct.

## Issue
Whether officers who abuse their authority act "under color of" state law for purposes of § 1983, and whether the federal remedy requires first exhausting state remedies.

## Rule
"Under color of" state law reaches the misuse of authority. The Court reaffirmed that "Misuse of power, possessed by virtue of state law and made possible only because the wrongdoer is clothed with the authority of state law, is action taken 'under color of' state law." — 365 U.S. at 184 (quoting *United States v. Classic*). ^pin-184

The Court further held that the § 1983 federal remedy is supplementary to any state remedy and need not be sought and refused before the federal action is brought.

## Application
The Chicago officers acted under [[Section 1983 Liability and Qualified Immunity|color of state law]] when they used their police authority to break into and ransack the Monroes' home and detain Mr. Monroe, even though their conduct also violated state law. The Monroes could therefore sue the officers under § 1983 without first pursuing a state remedy. (The Court also held that the City of Chicago was not a suable "person" under § 1983 — a holding later overruled by *[[Monell v. Department of Social Services|Monell]]*.)

## Conclusion
Reversed as to the individual officers; § 1983 reached their misuse of authority under [[Section 1983 Liability and Qualified Immunity|color of state law]].

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS**.
- **Overruled in part by** [[Monell v. Department of Social Services]] (1978), which held that municipalities ARE suable "persons" under § 1983, rejecting *Monroe*'s contrary municipal-immunity holding. *Monroe*'s core "under color of" state-law holding — reviving § 1983 as a federal remedy for the misuse of official authority — remains good law.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Anchor*

## Sources
- *Monroe v. Pape*, 365 U.S. 167 (1961) — https://www.courtlistener.com/opinion/106170/monroe-v-pape/ — pinpoint: 184.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b23009ef0fb635b0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Monroe v. Pape"}, "payload": {"all": [{"cite": "365 U.S. 167", "page": "167", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "365"}, {"cite": "81 S. Ct. 473", "page": "473", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "81"}, {"cite": "5 L. Ed. 2d 492", "page": "492", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "5"}, {"cite": "1961 U.S. LEXIS 1687", "page": "1687", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1961"}], "display": "365 U.S. 167", "official": {"cite": "365 U.S. 167", "page": "167", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "365"}, "official_selection_present": true, "record_id": "Monroe v. Pape"}}
{"assertion_id": "2d53b1e63104df71", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-184", "record_id": "Monroe v. Pape"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-184", "pinpoint_status": "slip-only", "quote": "state law for purposes of § 1983, and whether the federal remedy requires first exhausting state remedies. ## Rule", "quote_fidelity": "mismatch", "record_id": "Monroe v. Pape", "star_marker": null}}
{"assertion_id": "ed07484a8ddae794", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Monroe v. Pape"}, "payload": {"as_of_content": "1961-02-20", "as_of_treatment": "2026-06-30", "field_i_validity": "caution", "record_id": "Monroe v. Pape", "scope_note": "Overruled in part by Monell v. Department of Social Services (1978) as to municipal liability; the 'under color of' state-law holding remains good law.", "varies_by_point": true}}
```

### lake record — Monroe v. Pape

```json
{
  "schema_version": "s2.v1",
  "record_id": "Monroe v. Pape",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Monroe v. Pape",
    "case_name_short": "Monroe",
    "case_name_full": "MONROE Et Al. v. PAPE Et Al.",
    "input_case_name": "Monroe v. Pape",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1961-02-20",
    "year": 1961,
    "docket": null,
    "cluster_id": 106170,
    "lead_opinion_id": 106170,
    "sibling_ids": [
      106170,
      9422118,
      9422119,
      9422120
    ],
    "absolute_url": "/opinion/106170/monroe-v-pape/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8949295,
        "score": 20,
        "case_name": "Monroe v. Pape"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "365 U.S. 167",
      "volume": "365",
      "reporter": "U.S.",
      "page": "167",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "81 S. Ct. 473",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "473",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "5 L. Ed. 2d 492",
        "volume": "5",
        "reporter": "L. Ed. 2d",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1961 U.S. LEXIS 1687",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "1687",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "365 U.S. 167",
        "volume": "365",
        "reporter": "U.S.",
        "page": "167",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 S. Ct. 473",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "473",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "5 L. Ed. 2d 492",
        "volume": "5",
        "reporter": "L. Ed. 2d",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1961 U.S. LEXIS 1687",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "1687",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "365 U.S. 167",
    "official_selection": {
      "court_class": "scotus",
      "selected": "365 U.S. 167",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-184",
      "page": null,
      "quote": "state law for purposes of \u00a7 1983, and whether the federal remedy requires first exhausting state remedies. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "1961-02-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Monroe v. Pape",
    "varies_by_point": true,
    "scope_note": "Overruled in part by Monell v. Department of Social Services (1978) as to municipal liability; the 'under color of' state-law holding remains good law.",
    "point_overrides": [
      {
        "point": "legacy-limited-monroe-v-pape",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "Monell v. Department of Social Services",
            "cluster_id": 109881,
            "cite": "436 U.S. 658",
            "field_ii": "limited"
          }
        ],
        "scope_note": "Overruled in part by Monell v. Department of Social Services (1978) as to municipal liability; the 'under color of' state-law holding remains good law."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "Monell v. Department of Social Services",
          "cluster_id": 109881,
          "cite": "436 U.S. 658",
          "field_ii": "limited"
        },
        "field_ii": "limited",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:limited"
      },
      {
        "citing_case": {
          "name": "Gregory Baldwin v. City of Estherville, Iowa",
          "cluster_id": 4629600,
          "cite": [
            "929 N.W.2d 691"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Keyon Harrison v. Curt Vanderkooi",
          "cluster_id": 4522518,
          "cite": [
            "918 N.W.2d 785",
            "502 Mich. 751"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cion Peralta v. T. Dillard",
          "cluster_id": 814919,
          "cite": [
            "704 F.3d 1124",
            "2013 U.S. App. LEXIS 379",
            "2013 WL 57893"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Haywood v. Drown",
          "cluster_id": 1983488,
          "cite": [
            "881 N.E.2d 180",
            "9 N.Y.3d 481",
            "851 N.Y.S.2d 84"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Monell v. New York City Dept. of Social Servs.",
          "cluster_id": 109881,
          "cite": [
            "56 L. Ed. 2d 611",
            "98 S. Ct. 2018",
            "436 U.S. 658",
            "1978 U.S. LEXIS 100",
            "16 Empl. Prac. Dec. (CCH) 8345",
            "17 Fair Empl. Prac. Cas. (BNA) 873"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "West v. Atkins",
          "cluster_id": 112116,
          "cite": [
            "101 L. Ed. 2d 40",
            "108 S. Ct. 2250",
            "487 U.S. 42",
            "1988 U.S. LEXIS 2744",
            "56 U.S.L.W. 4664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adickes v. S. H. Kress & Co.",
          "cluster_id": 108153,
          "cite": [
            "26 L. Ed. 2d 142",
            "90 S. Ct. 1598",
            "398 U.S. 144",
            "1970 U.S. LEXIS 31"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Younger v. Harris",
          "cluster_id": 108263,
          "cite": [
            "27 L. Ed. 2d 669",
            "91 S. Ct. 746",
            "401 U.S. 37",
            "1971 U.S. LEXIS 136"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Will v. Michigan Department of State Police",
          "cluster_id": 112293,
          "cite": [
            "105 L. Ed. 2d 45",
            "109 S. Ct. 2304",
            "491 U.S. 58",
            "1989 U.S. LEXIS 2975",
            "57 U.S.L.W. 4677",
            "50 Empl. Prac. Dec. (CCH) 39,067",
            "49 Fair Empl. Prac. Cas. (BNA) 1664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of Regents of State Colleges v. Roth",
          "cluster_id": 108608,
          "cite": [
            "33 L. Ed. 2d 548",
            "92 S. Ct. 2701",
            "408 U.S. 564",
            "1972 U.S. LEXIS 131",
            "1 I.E.R. Cas. (BNA) 23"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scheuer v. Rhodes",
          "cluster_id": 109009,
          "cite": [
            "40 L. Ed. 2d 90",
            "94 S. Ct. 1683",
            "416 U.S. 232",
            "1974 U.S. LEXIS 126",
            "71 Ohio Op. 2d 474"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Preiser v. Rodriguez",
          "cluster_id": 108772,
          "cite": [
            "36 L. Ed. 2d 439",
            "93 S. Ct. 1827",
            "411 U.S. 475",
            "1973 U.S. LEXIS 72"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mapp v. Ohio",
          "cluster_id": 106285,
          "cite": [
            "6 L. Ed. 2d 1081",
            "81 S. Ct. 1684",
            "367 U.S. 643",
            "1961 U.S. LEXIS 812"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Daniels v. Williams",
          "cluster_id": 111555,
          "cite": [
            "88 L. Ed. 2d 662",
            "106 S. Ct. 662",
            "474 U.S. 327",
            "1986 U.S. LEXIS 43",
            "54 U.S.L.W. 4090"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mt. Healthy City School District Board of Education v. Doyle",
          "cluster_id": 109574,
          "cite": [
            "50 L. Ed. 2d 471",
            "97 S. Ct. 568",
            "429 U.S. 274",
            "1977 U.S. LEXIS 29",
            "1 I.E.R. Cas. (BNA) 76"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of the County Commissioners of Bryan County v. Brown",
          "cluster_id": 118104,
          "cite": [
            "137 L. Ed. 2d 626",
            "117 S. Ct. 1382",
            "520 U.S. 397",
            "1997 U.S. LEXIS 2793",
            "65 U.S.L.W. 4286",
            "10 Fla. L. Weekly Fed. S 405",
            "12 I.E.R. Cas. (BNA) 1217",
            "97 Cal. Daily Op. Serv. 3033",
            "97 Daily Journal DAR 5311"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parratt v. Taylor",
          "cluster_id": 110478,
          "cite": [
            "68 L. Ed. 2d 420",
            "101 S. Ct. 1908",
            "451 U.S. 527",
            "1981 U.S. LEXIS 99",
            "49 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baker v. Carr",
          "cluster_id": 106366,
          "cite": [
            "7 L. Ed. 2d 663",
            "82 S. Ct. 691",
            "369 U.S. 186",
            "1962 U.S. LEXIS 1567"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rizzo v. Goode",
          "cluster_id": 109349,
          "cite": [
            "46 L. Ed. 2d 561",
            "96 S. Ct. 598",
            "423 U.S. 362",
            "1976 U.S. LEXIS 42"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Polk County v. Dodson",
          "cluster_id": 110589,
          "cite": [
            "70 L. Ed. 2d 509",
            "102 S. Ct. 445",
            "454 U.S. 312",
            "1981 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Allen v. McCurry",
          "cluster_id": 110360,
          "cite": [
            "66 L. Ed. 2d 308",
            "101 S. Ct. 411",
            "449 U.S. 90",
            "1980 U.S. LEXIS 156",
            "49 U.S.L.W. 4015"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106170 OR 9422118 OR 9422119 OR 9422120) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTg2NDQ0ODAwMDAwJnM9MjQxMjI2MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106170+OR+9422118+OR+9422119+OR+9422120%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 4,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      },
      "lane2_top_cited": {
        "query": "cites:(106170 OR 9422118 OR 9422119 OR 9422120)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yOTczJnM9MTEyODI1JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106170+OR+9422118+OR+9422119+OR+9422120%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106170 OR 9422118 OR 9422119 OR 9422120)",
        "reviewed": 29,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 29,
        "triage_read": 0,
        "triage_snippet_classified": 29
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106170 OR 9422118 OR 9422119 OR 9422120)",
    "indexed_citing_opinions": 3267,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106170,
        "count": 3043,
        "count_source": "search"
      },
      {
        "opinion_id": 9422118,
        "count": 291,
        "count_source": "search"
      },
      {
        "opinion_id": 9422119,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9422120,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4788,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/monroe-v-pape.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1MTA3MTYmcz05NDM2MDY5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106170+OR+9422118+OR+9422119+OR+9422120%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106170,
        "cited_id": 88661,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 89309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 90041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 90305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 90728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 90897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 91064,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 91179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 91372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 91484,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 91885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 92917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 93322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 95317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 95877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 96036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 96225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 96478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 96704,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 96723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 96885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 97288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 97326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 97779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 98516,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 98517,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 98595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 99058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 100034,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 100544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 101032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 101446,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 101552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 101765,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 101766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 101816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 101894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 101911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 102086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 102189,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103012,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103028,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103292,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103921,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104588,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104616,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104703,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 105227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 105232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 105236,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 105511,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 106008,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1149975,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1237532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1334132,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1378476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1477715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1480162,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1485471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1490664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1491816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1497082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1498873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1506239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1555915,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1678770,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1682433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1811185,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1883596,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1943607,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1975150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 2146861,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 2195375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 2245571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 2394729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 2396750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 2620779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 3413717,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 3415036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 3417801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 3424043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 5021031,
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
    "date_created": "2026-07-05T14:27:30Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:27:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:27:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:27:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Monroe v. Pape (truncated)

```
<div>
<center><b><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U.S. 167</a></span> (1961)</b></center>
<center><h1>MONROE ET AL.<br>
v.<br>
PAPE ET AL.</h1></center>
<center>No. 39.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 8, 1960.</center>
<center>Decided February 20, 1961.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SEVENTH CIRCUIT.
<p><span class="star-pagination">*168</span> <i>Donald Page Moore</i> argued the cause for petitioners. With him on the brief were <i>Morris L. Ernst, Ernst Liebman, Charles Liebman</i> and <i>John W. Rogers.</i></p>
<p><i>Sydney R. Drebin</i> argued the cause for respondents. With him on the brief was <i>John C. Melaniphy.</i></p>
<p>MR. JUSTICE DOUGLAS delivered the opinion of the Court.</p>
<p>This case presents important questions concerning the construction of R. S. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>, which reads as follows:</p>
<blockquote>"Every person who, under color of any statute, ordinance, regulation, custom, or usage, of any State or Territory, subjects, or causes to be subjected, any <span class="star-pagination">*169</span> citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress."</blockquote>
<p>The complaint alleges that 13 Chicago police officers broke into petitioners' home in the early morning, routed them from bed, made them stand naked in the living room, and ransacked every room, emptying drawers and ripping mattress covers. It further alleges that Mr. Monroe was then taken to the police station and detained on "open" charges for 10 hours, while he was interrogated about a two-day-old murder, that he was not taken before a magistrate, though one was accessible, that he was not permitted to call his family or attorney, that he was subsequently released without criminal charges being preferred against him. It is alleged that the officers had no search warrant and no arrest warrant and that they acted "under color of the statutes, ordinances, regulations, customs and usages" of Illinois and of the City of Chicago. Federal jurisdiction was asserted under R. S. § 1979, which we have set out above, and <span class="citation no-link">28 U. S. C. § 1343</span><sup>[1]</sup> and <span class="citation no-link">28 U. S. C. § 1331</span>.<sup>[2]</sup></p>
<p><span class="star-pagination">*170</span> The City of Chicago moved to dismiss the complaint on the ground that it is not liable under the Civil Rights Acts nor for acts committed in performance of its governmental functions. All defendants moved to dismiss, alleging that the complaint alleged no cause of action under those Acts or under the Federal Constitution. The District Court dismissed the complaint. The Court of Appeals affirmed, <span class="citation" data-id="249412"><a href="/opinion/249412/james-monroe-v-frank-pape/" aria-description="Citation for case: James Monroe v. Frank Pape">272 F. 2d 365</a></span>, relying on its earlier decision, <i>Stift</i> v. <i>Lynch,</i> <span class="citation" data-id="248177"><a href="/opinion/248177/stift-v-lynch/" aria-description="Citation for case: Stift v. Lynch">267 F. 2d 237</a></span>. The case is here on a writ of certiorari which we granted because of a seeming conflict of that ruling with our prior cases. <span class="citation multiple-matches"><a href="/c/U.%20S./362/926/">362 U. S. 926</a></span>.</p>
<p></p>
<h2>I.</h2>
<p>Petitioners claim that the invasion of their home and the subsequent search without a warrant and the arrest and detention of Mr. Monroe without a warrant and without arraignment constituted a deprivation of their "rights, privileges, or immunities secured by the Constitution" within the meaning of R. S. § 1979. It has been said that when <span class="citation no-link">18 U. S. C. § 241</span> made criminal a conspiracy "to injure, oppress, threaten or intimidate any citizen in the free exercise or enjoyment of any right or privilege secured to him by the Constitution," it embraced only rights that an individual has by reason of his relation to the central government, not to state governments. <i>United States</i> v. <i>Williams,</i> <span class="citation" data-id="9420563"><a href="/opinion/104889/united-states-v-williams/" aria-description="Citation for case: United States v. Williams">341 U. S. 70</a></span>. Cf. <i>United States</i> v. <i>Cruikshank,</i> <span class="citation" data-id="9417049"><a href="/opinion/89309/united-states-v-cruikshank/" aria-description="Citation for case: United States v. Cruikshank">92 U. S. 542</a></span>; <i>Ex parte Yarbrough,</i> <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">110 U. S. 651</a></span>; <i>Guinn</i> v. <i>United States,</i> <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">238 U. S. 347</a></span>. But the history of the section of the Civil Rights Act presently involved does not permit such a narrow interpretation.</p>
<p><span class="star-pagination">*171</span> Section 1979 came onto the books as § 1 of the Ku Klux Act of April 20, 1871. <span class="citation no-link">17 Stat. 13</span>. It was one of the means whereby Congress exercised the power vested in it by § 5 of the Fourteenth Amendment to enforce the provisions of that Amendment.<sup>[3]</sup> Senator Edmunds, Chairman of the Senate Committee on the Judiciary, said concerning this section:</p>
<blockquote>"The first section is one that I believe nobody objects to, as defining the rights secured by the Constitution of the United States when they are assailed by any State law or under color of any State law, and it is merely carrying out the principles of the civil rights bill,<sup>[4]</sup> which has since become a part of the Constitution,"<sup>[5]</sup><i>viz.,</i> the Fourteenth Amendment.</blockquote>
<p>Its purpose is plain from the title of the legislation, "An Act to enforce the Provisions of the Fourteenth Amendment to the Constitution of the United States, and for other Purposes." <span class="citation no-link">17 Stat. 13</span>. Allegation of facts constituting a deprivation under color of state authority of a right guaranteed by the Fourteenth Amendment satisfies to that extent the requirement of R. S. § 1979. See <i>Douglas</i> v. <i>Jeannette,</i> <span class="citation" data-id="9419344"><a href="/opinion/103833/douglas-v-city-of-jeannette/#161" aria-description="Citation for case: Douglas v. City of Jeannette">319 U. S. 157, 161-162</a></span>. So far petitioners are on solid ground. For the guarantee against unreasonable searches and seizures contained in the Fourth Amendment has been made applicable to the States by reason of the Due Process Clause of the Fourteenth Amendment. <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>; <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#213" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 213</a></span>.</p>
<p></p>
<h2>II.</h2>
<p>There can be no doubt at least since <i>Ex parte Virginia,</i> <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/#346" aria-description="Citation for case: Ex Parte Virginia">100 U. S. 339, 346-347</a></span>, that Congress has the power to <span class="star-pagination">*172</span> enforce provisions of the Fourteenth Amendment against those who carry a badge of authority of a State and represent it in some capacity, whether they act in accordance with their authority or misuse it. See <i>Home Tel. &amp; Tel. Co.</i> v. <i>Los Angeles,</i> <span class="citation" data-id="97779"><a href="/opinion/97779/home-telephone-telegraph-co-v-city-of-los-angeles/#287" aria-description="Citation for case: Home Telephone &amp; Telegraph Co. v. City of Los Angeles">227 U. S. 278, 287-296</a></span>. The question with which we now deal is the narrower one of whether Congress, in enacting § 1979, meant to give a remedy to parties deprived of constitutional rights, privileges and immunities by an official's abuse of his position. Cf. <i>Williams</i> v. <i>United States,</i> <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/" aria-description="Citation for case: Williams v. United States">341 U. S. 97</a></span>; <i>Screws</i> v. <i>United States,</i> <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">325 U. S. 91</a></span>; <i>United States</i> v. <i>Classic,</i> <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">313 U. S. 299</a></span>. We conclude that it did so intend.</p>
<p>It is argued that "under color of" enumerated state authority excludes acts of an official or policeman who can show no authority under state law, state custom, or state usage to do what he did. In this case it is said that these policemen, in breaking into petitioners' apartment, violated the Constitution<sup>[6]</sup> and laws of Illinois. It is pointed out that under Illinois law a simple remedy is offered for that violation and that, so far as it appears, the courts of Illinois are available to give petitioners that full redress which the common law affords for violence done to a person; and it is earnestly argued that no "statute, ordinance, regulation, custom or usage" of Illinois bars that redress.</p>
<p>The Ku Klux Act grew out of a message sent to Congress by President Grant on March 23, 1871, reading:</p>
<blockquote>"A condition of affairs now exists in some States of the Union rendering life and property insecure and <span class="star-pagination">*173</span> the carrying of the mails and the collection of the revenue dangerous. The proof that such a condition of affairs exists in some localities is now before the Senate. That the power to correct these evils is beyond the control of State authorities I do not doubt; that the power of the Executive of the United States, acting within the limits of existing laws, is sufficient for present emergencies is not clear. Therefore, I urgently recommend such legislation as in the judgment of Congress shall effectually secure life, liberty, and property, and the enforcement of law in all parts of the United States. . . ."<sup>[7]</sup></blockquote>
<p>The legislationin particular the section with which we are now concernedhad several purposes. There are threads of many thoughts running through the debates. One who reads them in their entirety sees that the present section had three main aims.</p>
<p><i>First,</i> it might, of course, override certain kinds of state laws. Mr. Sloss of Alabama, in opposition, spoke of that object and emphasized that it was irrelevant because there were no such laws:<sup>[8]</sup></p>
<blockquote>"The first section of this bill prohibits any invidious legislation by States against the rights or privileges of citizens of the United States. The object of this section is not very clear, as it is not pretended by its advocates on this floor that any State has passed any laws endangering the rights or privileges of the colored people."</blockquote>
<p><i>Second,</i> it provided a remedy where state law was inadequate. That aspect of the legislation was summed up as follows by Senator Sherman of Ohio:</p>
<blockquote>". . . it is said the reason is that any offense may be committed upon a negro by a white man, and a <span class="star-pagination">*174</span> negro cannot testify in any case against a white man, so that the only way by which any conviction can be had in Kentucky in those cases is in the United States courts, because the United States courts enforce the United States laws by which negroes may testify."<sup>[9]</sup></blockquote>
<p>But the purposes were much broader. The <i>third</i> aim was to provide a federal remedy where the state remedy, though adequate in theory, was not available in practice. The opposition to the measure complained that "It overrides the reserved powers of the States,"<sup>[10]</sup> just as they argued that the second section of the bill "absorb[ed] the entire jurisdiction of the States over their local and domestic affairs."<sup>[11]</sup></p>
<p>This Act of April 20, 1871, sometimes called "the third `force bill,'" was passed by a Congress that had the Klan "particularly in mind."<sup>[12]</sup> The debates are replete with references to the lawless conditions existing in the South in 1871. There was available to the Congress during these debates a report, nearly 600 pages in length, dealing with the activities of the Klan and the inability of the state governments to cope with it.<sup>[13]</sup> This report was drawn on by many of the speakers.<sup>[14]</sup> It was not the unavailability of state remedies but the failure of certain States to enforce the laws with an equal hand that furnished <span class="star-pagination">*175</span> the powerful momentum behind this "force bill." Mr. Lowe of Kansas said:</p>
<blockquote>"While murder is stalking abroad in disguise, while whippings and lynchings and banishment have been visited upon unoffending American citizens, the local administrations have been found inadequate or unwilling to apply the proper corrective. Combinations, darker than the night that hides them, conspiracies, wicked as the worst of felons could devise, have gone unwhipped of justice. Immunity is given to crime, and the records of the public tribunals are searched in vain for any evidence of effective redress."<sup>[15]</sup></blockquote>
<p>Mr. Beatty of Ohio summarized in the House the case for the bill when he said:</p>
<blockquote>". . . certain States have denied to persons within their jurisdiction the equal protection of the laws. The proof on this point is voluminous and unquestionable. . . . [M]en were murdered, houses were burned, women were outraged, men were scourged, and officers of the law shot down; and the State made no successful effort to bring the guilty to punishment or afford protection or redress to the outraged and innocent. The State, from lack of power or inclination, practically denied the equal protection of the law to these persons."<sup>[16]</sup></blockquote>
<p>While one main scourge of the evilperhaps the leading onewas the Ku Klux Klan,<sup>[17]</sup> the remedy created was <span class="star-pagination">*176</span> not a remedy against it or its members but against those who representing a State in some capacity were <i>unable</i> or <i>unwilling</i> to enforce a state law. Senator Osborn of Florida put the problem in these terms:<sup>[18]</sup></p>
<blockquote>"That the State courts in the several States have been unable to enforce the criminal laws of their respective States or to suppress the disorders existing, and in fact that the preservation of life and property in many sections of the country is beyond the power of the State government, is a sufficient reason why Congress should, so far as they have authority under the Constitution, enact the laws necessary for the protection of citizens of the United States. The question of the constitutional authority for the requisite legislation has been sufficiently discussed."</blockquote>
<p>There was, it was said, no quarrel with the state laws on the books. It was their lack of enforcement that was the nub of the difficulty. Speaking of conditions in Virginia, Mr. Porter of that State said:<sup>[19]</sup></p>
<blockquote>"The outrages committed upon loyal men there are under the forms of law."</blockquote>
<p>Mr. Burchard of Illinois pointed out that the statutes of a State may show no discrimination:<sup>[20]</sup></p>
<blockquote>"If the State Legislature pass a law discriminating against any portion of its citizens, of if it fails to enact provisions equally applicable to every class for the protection of their person and property, it will be admitted that the State does not afford the equal protection. But if the statutes show no discrimination, <span class="star-pagination">*177</span> yet in its judicial tribunals one class is unable to secure that enforcement of their rights and punishment for their infraction which is accorded to another, or if secret combinations of men are allowed by the Executive to band together to deprive one class of citizens of their legal rights without a proper effort to discover, detect, and punish the violations of law and order, the State has not afforded to all its citizens the equal protection of the laws."</blockquote>
<p>Mr. Hoar of Massachusetts stated:<sup>[21]</sup></p>
<blockquote>"Now, it is an effectual denial by a State of the equal protection of the laws when any class of officers charged under the laws with their administration permanently and as a rule refuse to extend that protection. If every sheriff in South Carolina refuses to serve a writ for a colored man and those sheriffs are kept in office year after year by the people of South Carolina, and no verdict against them for their failure of duty can be obtained before a South Carolina jury, the State of South Carolina, through the class of officers who are its representatives to afford the equal protection of the laws to that class of citizens, has denied that protection. If the jurors of South Carolina constantly and as a rule refuse to do justice between man and man where the rights of a particular class of its citizens are concerned, and that State affords by its legislation no remedy, that is as much a denial to that class of citizens of the equal protection of the laws as if the State itself put on its statute-book a statute enacting that no verdict should be rendered in the courts of that State in favor of this class of citizens."</blockquote>
<p><span class="star-pagination">*178</span> Senator Pratt of Indiana spoke of the discrimination against Union sympathizers and Negroes in the actual enforcement of the laws:<sup>[22]</sup></p>
<blockquote>"Plausibly and sophistically it is said the laws of North Carolina do not discriminate against them; that the provisions in favor of rights and liberties are general; that the courts are open to all; that juries, grand and petit, are commanded to hear and redress without distinction as to color, race, or political sentiment.</blockquote>
<blockquote>"But it is a fact, asserted in the report, that of the hundreds of outrages committed upon loyal people through the agency of this Ku Klux organization not one has been punished. This defect in the administration of the laws does not extend to other cases. Vigorously enough are the laws enforced against Union people. They only fail in efficiency when a man of known Union sentiments, white or black, invokes their aid. Then Justice closes the door of her temples."</blockquote>
<p>It was precisely that breadth of the remedy which the opposition emphasized. Mr. Kerr of Indiana referring to the section involved in the present litigation said:</p>
<blockquote>"This section gives to any person who may have been injured in any of his rights, privileges, or immunities of person or property, a civil action for damages against the wrongdoer in the Federal courts. The offenses committed against him may be the common violations of the municipal law of his State. It may give rise to numerous vexations and outrageous prosecutions, inspired by mere mercenary considerations, prosecuted in a spirit of plunder, aided by the crimes of perjury and subornation of perjury, more reckless and dangerous to society than the alleged <span class="star-pagination">*179</span> offenses out of which the cause of action may have arisen. It is a covert attempt to transfer another large portion of jurisdiction from the State tribunals, to which it of right belongs, to those of the United States. It is neither authorized nor expedient, and is not calculated to bring peace, or order, or domestic content and prosperity to the disturbed society of the South. The contrary will certainly be its effect."<sup>[23]</sup></blockquote>
<p>Mr. Voorhees of Indiana, also speaking in opposition, gave it the same construction:<sup>[24]</sup></p>
<blockquote>"And now for a few moments let us inspect the provisions of this bill, inspired as it is by the waning and decaying fortunes of the party in power, and called for, as I have shown, by no public necessity whatever. The first and second sections are designed to transfer all criminal jurisdiction from the courts of the States to the courts of the United States. This is to be done upon the assumption that the courts of the southern States fail and refuse to do their duty in the punishment of offenders against the law."</blockquote>
<p>Senator Thurman of Ohio spoke in the same vein about the section we are now considering:<sup>[25]</sup></p>
<blockquote>"It authorizes any person who is deprived of any right, privilege, or immunity secured to him by the <span class="star-pagination">*180</span> Constitution of the United States, to bring an action against the wrong-doer in the Federal courts, and that without any limit whatsoever as to the amount in controversy. The deprivation may be of the slightest conceivable character, the damages in the estimation of any sensible man may not be five dollars or even five cents; they may be what lawyers call merely nominal damages; and yet by this section jurisdiction of that civil action is given to the Federal courts instead of its being prosecuted as now in the courts of the States."</blockquote>
<p>The debates were long and extensive. It is abundantly clear that one reason the legislation was passed was to afford a federal right in federal courts because, by reason of prejudice, passion, neglect, intolerance or otherwise, state laws might not be enforced and the claims of citizens to the enjoyment of rights, privileges, and immunities guaranteed by the Fourteenth Amendment might be denied by the state agencies.</p>
<p>Much is made of the history of § 2 of the proposed legislation. As introduced § 2 was very broad:</p>
<blockquote>". . . if two or more persons shall, within the limits of any State, band, conspire, or combine together to do any act in violation of the rights, privileges, or immunities of any person, to which he is entitled under the Constitution and laws of the United States, which, committed within a place under the sole and exclusive jurisdiction of the United States, would, under any law of the United States then in force, constitute the crime of either murder, manslaughter, mayhem, robbery, assault and battery, perjury, subornation of perjury, criminal obstruction of legal process or resistance of officers in discharge of official duty, arson, or larceny; and if one or more of the parties to said conspiracy or combination shall do <span class="star-pagination">*181</span> any act to effect the object thereof, all the parties to or engaged in said conspiracy or combination, whether principals or accessories, shall be deemed guilty of a felony . . . ."</blockquote>
<p>It was this provision that raised the greatest storm. It was § 2 that was rewritten so as to be in the main confined to conspiracies to interfere with a federal or state officer in the performance of his duties. <span class="citation no-link">17 Stat. 13</span>. Senator Trumbull said:<sup>[26]</sup></p>
<blockquote>"Those provisions were changed, and as the bill passed the House of Representatives, it was understood by the members of that body to go no further than to protect persons in the rights which were guarantied to them by the Constitution and laws of the United States, and it did not undertake to furnish redress for wrongs done by one person upon another in any of the States of the Union in violation of their laws, unless he also violated some law of the United States, nor to punish one person for an ordinary assault and battery committed on another in a State."</blockquote>
<p>But § 1the section with which we are here concerned was not changed as respects any feature with which we are presently concerned.<sup>[27]</sup> The words "under <span class="star-pagination">*182</span> color of" law were in the legislation from the beginning to the end. The changes hailed by the oppositionindeed the history of the evolution of § 2 much relied upon now are utterly irrelevant to the problem before us, <i>viz.,</i> the meaning of "under color of" law. The vindication of States' rights which was hailed in the amendments to § 2 raises no implication as to the construction to be given to "color of any law" in § 1. The scope of § 1under any constructionis admittedly narrower than was the scope of the original version of § 2. Opponents of the Act, however, did not fail to note that by virtue of § 1 federal courts would sit in judgment on the misdeeds of state officers.<sup>[28]</sup> Proponents of the Act, on the other hand, were aware of the extension of federal power contemplated by every section of the Act. They found justification, however, for this extension in considerations such as those advanced by Mr. Hoar:<sup>[29]</sup></p>
<blockquote>"The question is not whether a majority of the people in a majority of the States are likely to be attached to and able to secure their own liberties. The question is not whether the majority of the people in every State are not likely to desire to secure their own rights. It is, whether a majority of the people in every State are sure to be so attached to the principles of civil freedom and civil justice as to be as much desirous of preserving the liberties of others as their own, as to insure that under no temptation of party spirit, under no political excitement, under <span class="star-pagination">*183</span> no jealousy of race or caste, will the majority either in numbers or strength in any State seek to deprive the remainder of the population of their civil rights."</blockquote>
<p>Although the legislation was enacted because of the conditions that existed in the South at that time, it is cast in general language and is as applicable to Illinois as it is to the States whose names were mentioned over and again in the debates. It is no answer that the State has a law which if enforced would give relief. The federal remedy is supplementary to the state remedy, and the latter need not be first sought and refused before the federal one is invoked. Hence the fact that Illinois by its constitution and laws outlaws unreasonable searches and seizures is no barrier to the present suit in the federal court.</p>
<p>We had before us in <i>United States</i> v. <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic, supra</a></span></i><i>,</i> § 20 of the Criminal Code, <span class="citation no-link">18 U. S. C. § 242</span>,<sup>[30]</sup> which provides a criminal punishment for anyone who "under color of any law, statute, ordinance, regulation, or custom" subjects any inhabitant of a State to the deprivation of "any rights, privileges, or immunities secured or protected by the Constitution or laws of the United States." Section 242 first came into the law as § 2 of the Civil Rights Act, Act of April 9, 1866, <span class="citation no-link">14 Stat. 27</span>. After passage of the Fourteenth Amendment, this provision was re-enacted and amended by §§ 17, 18, Act of May 31, 1870, <span class="citation no-link">16 Stat. 140</span>, 144.<sup>[31]</sup> The right involved in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case was the right of voters in a primary to have their votes counted. The laws of Louisiana required the defendants "to count the ballots, to record the result of the count, and <span class="star-pagination">*184</span> to certify the result of the election." <i>United States</i> v. <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/#325" aria-description="Citation for case: United States v. Classic"><i>Classic, supra,</i> 325-326</a></span>. But according to the indictment they did not perform their duty. In an opinion written by Mr. Justice (later Chief Justice) Stone, in which Mr. Justice Roberts, Mr. Justice Reed, and MR. JUSTICE FRANKFURTER joined, the Court ruled, "Misuse of power, possessed by virtue of state law and made possible only because the wrongdoer is clothed with the authority of state law, is action taken `under color of' state law." <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/#326" aria-description="Citation for case: United States v. Classic"><i>Id.,</i> 326</a></span>. There was a dissenting opinion; but the ruling as to the meaning of "under color of" state law was not questioned.</p>
<p>That view of the meaning of the words "under color of" state law, <span class="citation no-link">18 U. S. C. § 242</span>, was reaffirmed in <i>Screws</i> v. <i>United States, supra,</i> 108-113. The acts there complained of were committed by state officers in performance of their duties, <i>viz.,</i> making an arrest effective. It was urged there, as it is here, that "under color of" state law should not be construed to duplicate in federal law what was an offense under state law. <i>Id.</i> (dissenting opinion) 138-149, 157-161. It was said there, as it is here, that the ruling in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case as to the meaning of "under color of" state law was not in focus and was ill-advised. <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Id.</a></span></i> (dissenting opinion) 146-147. It was argued there, as it is here, that "under color of" state law included only action taken by officials pursuant to state law. <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Id.</a></span></i> (dissenting opinion) 141-146. We rejected that view. <i>Id.,</i> 110-113 (concurring opinion) 114-117. We stated:</p>
<blockquote>"The construction given § 20 [<span class="citation no-link">18 U. S. C. § 242</span>] in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case formulated a rule of law which has become the basis of federal enforcement in this important field. The rule adopted in that case was formulated after mature consideration. It should be good for more than one day only. We do not have here a situation comparable to <i>Mahnich</i> v. <i>Southern S. S. Co.,</i> <span class="citation" data-id="103927"><a href="/opinion/103927/mahnich-v-southern-steamship-co/" aria-description="Citation for case: Mahnich v. Southern Steamship Co.">321 U. S. 96</a></span>, where we <span class="star-pagination">*185</span> overruled a decision demonstrated to be a sport in the law and inconsistent with what preceded and what followed. The <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case was not the product of hasty action or inadvertence. It was not out of line with the cases which preceded. It was designed to fashion the governing rule of law in this important field. We are not dealing with constitutional interpretations which throughout the history of the Court have wisely remained flexible and subject to frequent re-examination. The meaning which the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case gave to the phrase `under color of any law' involved only a construction of the statute. Hence if it states a rule undesirable in its consequences, Congress can change it. We add only to the instability and uncertainty of the law if we revise the meaning of § 20 [<span class="citation no-link">18 U. S. C. § 242</span>] to meet the exigencies of each case coming before us." <span class="citation no-link"><i>Id.,</i> 112-113</span>.</blockquote>
<p>We adhered to that view in <i>Williams</i> v. <i>United States, supra,</i> 99.</p>
<p>Mr. Shellabarger, reporting out the bill which became the Ku Klux Act, said of the provision with which we now deal:</p>
<blockquote>"The model for it will be found in the second section of the act of April 9, 1866, known as the `civil rights act.'. . . This section of this bill, on the same state of facts, not only provides a civil remedy for persons whose former condition may have been that of slaves, but also to all people where, under color of State law, they or any of them may be deprived of rights . . . ."<sup>[32]</sup></blockquote>
<p>Thus, it is beyond doubt that this phrase should be accorded the same construction in both statutesin § 1979 and in <span class="citation no-link">18 U. S. C. § 242</span>.</p>
<p><span class="star-pagination">*186</span> Since the <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> and <i>Williams</i> decisions, Congress has had several pieces of civil rights legislation before it. In 1956 one bill reached the floor of the House. This measure had at least one provision in it penalizing actions taken "under color of law or otherwise."<sup>[33]</sup> A vigorous minority report was filed attacking, <i>inter alia,</i> the words "or otherwise."<sup>[34]</sup> But not a word of criticism of the phrase "under color of" state law as previously construed by the Court is to be found in that report.</p>
<p>Section 131 (c) of the Act of September 9, 1957, <span class="citation no-link">71 Stat. 634</span>, 637, amended <span class="citation no-link">42 U. S. C. § 1971</span> by adding a new subsection which provides that no person "whether acting under color of law or otherwise" shall intimidate any other person in voting as he chooses for federal officials. A vigorous minority report was filed<sup>[35]</sup> attacking the wide scope of the new subsection by reason of the words "or otherwise." It was said in that minority report that those words went far beyond what this Court had construed "under color of law" to mean.<sup>[36]</sup> But there was not a word of criticism directed to the prior construction given by this Court to the words "under color of" law.</p>
<p>The Act of May 6, 1960, <span class="citation no-link">74 Stat. 86</span>, uses "under color of" law in two contexts, once when § 306 defines "officer of election" and next when § 601 (a) gives a judicial remedy on behalf of a qualified voter denied the opportunity to register. Once again there was a Committee report containing minority views.<sup>[37]</sup> Once again no one challenged the scope given by our prior decisions to the phrase "under color of" law.</p>
<p><span class="star-pagination">*187</span> If the results of our construction of "under color of" law were as horrendous as now claimed, if they were as disruptive of our federal scheme as now urged, if they were such an unwarranted invasion of States' rights as pretended, surely the voice of the opposition would have been heard in those Committee reports. Their silence and the new uses to which "under color of" law have recently been given reinforce our conclusion that our prior decisions were correct on this matter of construction.</p>
<p>We conclude that the meaning given "under color of" law in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case and in the <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> and <i>Williams</i> cases was the correct one; and we adhere to it.</p>
<p>In the <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> case we dealt with a statute that imposed criminal penalties for acts "wilfully" done. We construed that word in its setting to mean the doing of an act with "a specific intent to deprive a person of a federal right." <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/#103" aria-description="Citation for case: Screws v. United States">325 U. S., at 103</a></span>. We do not think that gloss should be placed on § 1979 which we have here. The word "wilfully" does not appear in § 1979. Moreover, § 1979 provides a civil remedy, while in the <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> case we dealt with a criminal law challenged on the ground of vagueness. Section 1979 should be read against the background of tort liability that makes a man responsible for the natural consequences of his actions.</p>
<p>So far, then, the complaint states a cause of action. There remains to consider only a defense peculiar to the City of Chicago.</p>
<p></p>
<h2>III.</h2>
<p>The City of Chicago asserts that it is not liable under § 1979. We do not stop to explore the whole range of questions tendered us on this issue at oral argument and in the briefs. For we are of the opinion that Congress did not undertake to bring municipal corporations within the ambit of § 1979.</p>
<p><span class="star-pagination">*188</span> When the bill that became the Act of April 20, 1871, was being debated in the Senate, Senator Sherman of Ohio proposed an amendment which would have made "the inhabitants of the county, city, or parish" in which certain acts of violence occurred liable "to pay full compensation" to the person damaged or his widow or legal representative.<sup>[38]</sup> The amendment was adopted by the Senate.<sup>[39]</sup> The House, however, rejected it.<sup>[40]</sup> The Conference Committee reported another version.<sup>[41]</sup> The <span class="star-pagination">*189</span> House rejected the Conference report.<sup>[42]</sup> In a second conference the Sherman amendment was dropped and in its place § 6 of the Act of April 20, 1871, was substituted.<sup>[43]</sup><span class="star-pagination">*190</span> This new section, which is now R. S. § 1981, <span class="citation no-link">42 U. S. C. § 1986</span>, dropped out all provision for municipal liability and extended liability in damages to "any person or persons, having knowledge that any" of the specified wrongs are being committed. Mr. Poland, speaking for the House Conferees about the Sherman proposal to make municipalities liable, said:</p>
<blockquote>"We informed the conferees on the part of the Senate that the House had taken a stand on that subject and would not recede from it; that that section imposing liability upon towns and counties must go out or we should fail to agree."<sup>[44]</sup></blockquote>
<p>The objection to the Sherman amendment stated by Mr. Poland was that "the House had solemnly decided that in their judgment Congress had no constitutional power to impose any obligation upon county and town organizations, the mere instrumentality for the administration of state law."<sup>[45]</sup> The question of constitutional power of Congress to impose civil liability on municipalities was vigorously debated with powerful arguments advanced in the affirmative.<sup>[46]</sup></p>
<p>Much reliance is placed on the Act of February 25, 1871, <span class="citation no-link">16 Stat. 431</span>, entitled "An Act prescribing the Form of the enacting and resolving Clauses of Acts and Resolutions of Congress, and Rules for the Construction thereof." Section 2 of this Act provides that "the word `person' may extend and be applied to bodies politic and corporate."<sup>[47]</sup><span class="star-pagination">*191</span> It should be noted, however, that this definition is merely an allowable, not a mandatory, one. It is said that doubts should be resolved in favor of municipal liability because private remedies against officers for illegal searches and seizures are conspicuously ineffective,<sup>[48]</sup> and because municipal liability will not only afford plaintiffs responsible defendants but cause those defendants to eradicate abuses that exist at the police level.<sup>[49]</sup> We do not reach those policy considerations. Nor do we reach the constitutional question whether Congress has the power to make municipalities liable for acts of its officers that violate the civil rights of individuals.</p>
<p>The response of the Congress to the proposal to make municipalities liable for certain actions being brought within federal purview by the Act of April 20, 1871, was so antagonistic that we cannot believe that the word "person" was used in this particular Act to include them.<sup>[50]</sup><span class="star-pagination">*192</span> Accordingly we hold that the motion to dismiss the complaint against the City of Chicago was properly granted. But since the complaint should not have been dismissed against the officials the judgment must be and is</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE HARLAN, whom MR. JUSTICE STEWART joins, concurring.</p>
<p>Were this case here as one of first impression, I would find the "under color of any statute" issue very close indeed. However, in <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i><sup>[1]</sup> and <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i><sup>[2]</sup> this Court considered a substantially identical statutory phrase to have a meaning which, unless we now retreat from it, requires that issue to go for the petitioners here.</p>
<p>From my point of view, the policy of <i>stare decisis,</i> as it should be applied in matters of statutory construction, and, to a lesser extent, the indications of congressional acceptance of this Court's earlier interpretation, require that it appear beyond doubt from the legislative history of the 1871 statute that <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> and <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> misapprehended the meaning of the controlling provision,<sup>[3]</sup> before a departure from what was decided in those cases would be justified. Since I can find no such justifying indication in that legislative history, I join the opinion of the Court. However, what has been written on both sides of the matter makes some additional observations appropriate.</p>
<p><span class="star-pagination">*193</span> Those aspects of Congress' purpose which are quite clear in the earlier congressional debates, as quoted by my Brothers DOUGLAS and FRANKFURTER in turn, seem to me to be inherently ambiguous when applied to the case of an isolated abuse of state authority by an official. One can agree with the Court's opinion that:</p>
<blockquote>"It is abundantly clear that one reason the legislation was passed was to afford a federal right in federal courts because, by reason of prejudice, passion, neglect, intolerance or otherwise, state laws might not be enforced and the claims of citizens to the enjoyment of rights, privileges, and immunities guaranteed by the Fourteenth Amendment might be denied by the state agencies. . . ."</blockquote>
<p>without being certain that Congress meant to deal with anything other than abuses so recurrent as to amount to "custom, or usage." One can agree with my Brother FRANKFURTER, in dissent, that Congress had no intention of taking over the whole field of ordinary state torts and crimes, without being certain that the enacting Congress would not have regarded actions by an official, made possible by his position, as far more serious than an ordinary state tort, and therefore as a matter of federal concern. If attention is directed at the rare specific references to isolated abuses of state authority, one finds them neither so clear nor so disproportionately divided between favoring the positions of the majority or the dissent as to make either position seem plainly correct.<sup>[4]</sup></p>
<p>Besides the inconclusiveness I find in the legislative history, it seems to me by no means evident that a position <span class="star-pagination">*194</span> favoring departure from <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> and <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> fits better that with which the enacting Congress was concerned than does the position the Court adopted 20 years ago. There are apparent incongruities in the view of the dissent which may be more easily reconciled in terms of the earlier holding in <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span>.</i></p>
<p>The dissent considers that the "under color of" provision of § 1983 distinguishes between unconstitutional actions taken without state authority, which only the State should remedy, and unconstitutional actions authorized by the State, which the Federal Act was to reach. If so, then the controlling difference for the enacting legislature must have been either that the state remedy was more adequate for unauthorized actions than for authorized ones or that there was, in some sense, greater harm from unconstitutional actions authorized by the full panoply of state power and approval than from unconstitutional actions not so authorized or acquiesced in by the State. I find less than compelling the evidence that either distinction was important to that Congress.</p>
<p></p>
<h2>I.</h2>
<p>If the state remedy was considered adequate when the official's unconstitutional act was unauthorized, why should it not be thought equally adequate when the unconstitutional act was authorized? For if one thing is very clear in the legislative history, it is that the Congress of 1871 was well aware that no action requiring state judicial enforcement could be taken in violation of the Fourteenth Amendment without that enforcement being declared void by this Court on direct review from the state courts. And presumably it must also have been understood that there would be Supreme Court review of the denial of a state damage remedy against an official on grounds of state authorization of the unconstitutional <span class="star-pagination">*195</span> action. It therefore seems to me that the same state remedies would, with ultimate aid of Supreme Court review, furnish identical relief in the two situations. This is the point Senator Blair made when, having stated that the object of the Fourteenth Amendment was to prevent any discrimination by the law of any State, he argued that:</p>
<blockquote>"This being forbidden by the Constitution of the United States, and all the judges, State and national, being sworn to support the Constitution of the United States, and the Supreme Court of the United States having power to supervise and correct the action of the State courts when they violated the Constitution of the United States, there could be no danger of the violation of the right of citizens under color of the <i>laws</i> of the States." Cong. Globe, 42d Cong., 1st Sess., at App. 231.</blockquote>
<p>Since the suggested narrow construction of § 1983 presupposes that state measures were adequate to remedy unauthorized deprivations of constitutional rights and since the identical state relief could be obtained for state-authorized acts with the aid of Supreme Court review, this narrow construction would reduce the statute to having merely a jurisdictional function, shifting the load of federal supervision from the Supreme Court to the lower courts and providing a federal tribunal for fact findings in cases involving authorized action. Such a function could be justified on various grounds. It could, for example, be argued that the state courts would be less willing to find a constitutional violation in cases involving "authorized action" and that therefore the victim of such action would bear a greater burden in that he would more likely have to carry his case to this Court, and once here, might be bound by unfavorable state court findings. But the legislative debates do not disclose congressional <span class="star-pagination">*196</span> concern about the burdens of litigation placed upon the victims of "authorized" constitutional violations contrasted to the victims of unauthorized violations. Neither did Congress indicate an interest in relieving the burden placed on this Court in reviewing such cases.</p>
<p>The statute becomes more than a jurisdictional provision only if one attributes to the enacting legislature the view that a deprivation of a constitutional right is significantly different from and more serious than a violation of a state right and therefore deserves a different remedy even though the same act may constitute both a state tort and the deprivation of a constitutional right. This view, by no means unrealistic as a common-sense matter,<sup>[5]</sup> is, I believe, more consistent with the flavor of the legislative history than is a view that the primary purpose of the statute was to grant a lower court forum for fact findings. For example, the tone is surely one of overflowing protection of constitutional rights, and there is not a hint of concern about the administrative burden on the Supreme Court, when Senator Frelinghuysen says:</p>
<blockquote>"As to the civil remedies, for a violation of these privileges, we know that when the courts of a State <span class="star-pagination">*197</span> violate the provisions of the Constitution or the law of the United States there is now relief afforded by a review in the Federal courts. And since the 14th Amendment forbids any State from making or enforcing any law abridging these privileges and immunities, as you cannot reach the Legislatures, the injured party should have an original action in our Federal courts, so that by injunction or by the recovery of damages he could have relief against the party who under color of such law is guilty of infringing his rights. As to the civil remedy no one, I think, can object." <i>Id.,</i> at 501.</blockquote>
<p>And Senator Carpenter reflected a similar belief that the protection granted by the statute was to be very different from the relief available on review of state proceedings:</p>
<blockquote>"The prohibition in the old Constitution that no State should pass a law impairing the obligation of contracts was a negative prohibition laid upon the State. Congress was not authorized to interfere in case the State violated that provision. It is true that when private rights were affected by such a State law, and that was brought before the judiciary, either of the State or nation, it was the duty of the court to pronounce the act void; but there the matter ended. Under the present Constitution, however, in regard to those rights which are secured by the fourteenth amendment, they are not left as the right of the citizen in regard to laws impairing the obligation of contracts was left, to be disposed of by the courts as the cases should arise between man and man, but Congress is clothed with the affirmative power and jurisdiction to correct the evil.</blockquote>
<blockquote>"I think there is one of the fundamental, one of the great, the tremendous revolutions effected in our Government by that article of the Constitution. It <span class="star-pagination">*198</span> gives Congress affirmative power to protect the rights of the citizen, whereas before no such right was given to save the citizen from the violation of any of his rights by State Legislatures, and the only remedy was a judicial one when the case arose." <i>Id.,</i> at 577.</blockquote>
<p>In my view, these considerations put in serious doubt the conclusion that § 1983 was limited to state-authorized unconstitutional acts, on the premise that state remedies respecting them were considered less adequate than those available for unauthorized acts.</p>
<p></p>
<h2>II.</h2>
<p>I think this limited interpretation of § 1983 fares no better when viewed from the other possible premise for it, namely that state-approved constitutional deprivations were considered more offensive than those not so approved. For one thing, the enacting Congress was not unaware of the fact that there was a substantial overlap between the protections granted by state constitutional provisions and those granted by the Fourteenth Amendment. Indeed one opponent of the bill, Senator Trumbull, went so far as to state in a debate with Senators Carpenter and Edmunds that his research indicated a complete overlap in every State, at least as to the protections of the Due Process Clause.<sup>[6]</sup> Thus, in one very significant sense, there was no ultimate state approval of a large portion of otherwise authorized actions depriving a person of due-process rights. I hesitate to assume that the proponents of the present statute, who regarded it as necessary even though they knew that the provisions of the Fourteenth Amendment were self-executing, would have thought the remedies unnecessary whenever there were self-executing provisions of state constitutions also forbidding what the Fourteenth Amendment forbids. The only alternative is <span class="star-pagination">*199</span> to disregard the possibility that a state court would find the action unauthorized on grounds of the state constitution. But if the defendant official is denied the right to defend in the federal court upon the ground that a state court would find his action unauthorized in the light of the state constitution, it is difficult to contend that it is the added harmfulness of state approval that justifies a different remedy for authorized than for unauthorized actions of state officers. Moreover, if indeed the legislature meant to distinguish between authorized and unauthorized acts and yet did not mean the statute to be inapplicable whenever there was a state constitutional provision which, reasonably interpreted, gave protection similar to that of a provision of the Fourteenth Amendment, would there not have been some explanation of this exception to the general rule? The fact that there is none in the legislative history at least makes more difficult a contention that these legislators were in fact making a distinction between use and misuse of state power.</p>
<p>There is a further basis for doubt that it was the additional force of state approval which justified a distinction between authorized and unauthorized actions. No one suggests that there is a difference in the showing the plaintiff must make to assert a claim under § 1983 depending upon whether he is asserting a denial of rights secured by the Equal Protection Clause or a denial of rights secured by the Due Process Clause of the Fourteenth Amendment. If the same Congress which passed what is now § 1983 also provided remedies against two or more nonofficials who conspire to prevent an official from granting equal protection of the laws, see <span class="citation no-link">42 U. S. C. § 1985</span>, then it would seem almost untenable to insist that this Congress would have hesitated, on the grounds of lack of full state approval of the official's act, to provide similar remedies against an official who, unauthorized, denied that equal protection of the laws on his own initiative. For <span class="star-pagination">*200</span> there would be no likely state approval of or even acquiescence in a conspiracy to coerce a state official to deny equal protection. Indeed it is difficult to attribute to a Congress which forbade two private citizens from hindering an official's giving of equal protection an intent to leave that official free to deny equal protection of his own accord.<sup>[7]</sup></p>
<p>We have not passed upon the question whether <span class="citation no-link">42 U. S. C. § 1985</span>,<sup>[8]</sup> which was passed as the second section of the Act that included § 1983, was intended to reach only the Ku Klux Klan or other substantially organized group activity, as distinguished from what its words seem to include, any conspiracy of two persons with "the purpose of preventing or hindering the constituted authorities of any State . . . from giving or securing to all persons within such State . . . the equal protection of the laws . . . ."<sup>[9]</sup> Without now deciding the question, I think <span class="star-pagination">*201</span> it is sufficient to note that the legislative history is not without indications that what the words of the statute seem to state was in fact the meaning assumed by Congress.<sup>[10]</sup></p>
<p><span class="star-pagination">*202</span> These difficulties in explaining the basis of a distinction between authorized and unauthorized deprivations of constitutional rights fortify my view that the legislative history does not bear the burden which <i>stare decisis</i> casts upon it. For this reason and for those stated in the opinion of the Court, I agree that we should not now depart from the holdings of the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> and <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> cases.</p>
<p>MR. JUSTICE FRANKFURTER, dissenting except insofar as the Court holds that this action cannot be maintained against the City of Chicago.</p>
<p>Abstractly stated, this case concerns a matter of statutory construction. So stated, the problem before the Court is denuded of illuminating concreteness and thereby of its far-reaching significance for our federal system. Again abstractly stated, this matter of statutory construction is one upon which the Court has already passed. But it has done so under circumstances and in settings that negative those considerations of social policy upon which the doctrine of <i>stare decisions,</i> calling for the controlling application of prior statutory construction, rests.</p>
<p>This case presents the question of the sufficiency of petitioners' complaint in a civil action for damages brought under the Civil Rights Act, R. S. § 1979, <span class="star-pagination">*203</span> <span class="citation no-link">42 U. S. C. § 1983</span>.<sup>[1]</sup> The complaint alleges that on October 29, 1958, at 5:45 a.m., thirteen Chicago police officers, led by Deputy Chief of Detectives Pape, broke through two doors of the Monroe apartment, woke the Monroe couple with flashlights, and forced them at gunpoint to leave their bed and stand naked in the center of the living room; that the officers roused the six Monroe children and herded them into the living room; that Detective Pape struck Mr. Monroe several times with his flashlight, calling him "nigger" and "black boy"; that another officer pushed Mrs. Monroe; that other officers hit and kicked several of the children and pushed them to the floor; that the police ransacked every room, throwing clothing from closets to the floor, dumping drawers, ripping mattress covers; that Mr. Monroe was then taken to the police station and detained on "open" charges for ten hours, during which time he was interrogated about a murder<sup>[2]</sup> and exhibited in lineups; that he was not brought before a magistrate, although numerous magistrate's courts were accessible; that he was not advised of his procedural rights; that he was not permitted to call his family or an attorney; that he was subsequently released without criminal charges having been filed against him. It is also alleged that the actions of the officers throughout were without authority of a search warrant or an arrest warrant; that those actions constituted arbitrary and unreasonable conduct; that the <span class="star-pagination">*204</span> officers were employees of the City of Chicago, which furnished each of them with a badge and an identification card designating him as a member of the Police Department; that the officers were agents of the city, acting in the course of their employment and engaged in the performance of their duties; and that it is the custom of the Department to arrest and confine individuals for prolonged periods on "open" charges for interrogation, with the purpose of inducing incriminating statements, exhibiting its prisoners for identification, holding them <i>incommunicado</i> while police officers investigate their activities, and punishing them by imprisonment without judicial trial. On the basis of these allegations various members of the Monroe family seek damages against the individual police officers and against the City of Chicago. The District Court dismissed the complaint for failure to state a claim and the Court of Appeals for the Seventh Circuit affirmed. <span class="citation" data-id="249412"><a href="/opinion/249412/james-monroe-v-frank-pape/" aria-description="Citation for case: James Monroe v. Frank Pape">272 F. 2d 365</a></span>.</p>
<p>Petitioners base their claim to relief in the federal courts on what was enacted as § 1 of the "Ku Klux Act" of April 20, 1871, "An Act to enforce the Provisions of the Fourteenth Amendment to the Constitution of the United States, and for other Purposes." <span class="citation no-link">17 Stat. 13</span>. It became, with insignificant rephrasing, § 1979 of the Revised Statutes. As now set forth in <span class="citation no-link">42 U. S. C. § 1983</span>, it is, in relevant part, as follows:</p>
<blockquote>"Every person who, under color of any statute, ordinance, regulation, custom, or usage, of any State . . . subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress."</blockquote>
<p></p>
<h2>
<span class="star-pagination">*205</span> I.</h2>
<p>In invoking § 1979 (the old designation will be used hereafter), petitioners contend that its protection of "rights, privileges, or immunities secured by the Constitution" encompasses what "due process of law" and "the equal protection of the laws" of the Fourteenth Amendment guarantee against action by the States. In this contention they are supported both by the title of the Act of 1871 and by its legislative history. See the authoritative statement of Mr. Edmunds, reporting the bill from the Senate Committee on the Judiciary, Cong. Globe, 42d Cong., 1st Sess. 568. See also <i>id.,</i> at 332-334, App. 83-85, 310. It is true that a related phrase, "any right or privilege secured . . . by the Constitution or laws," in § 241 of Title 18, U. S. C., was said by a plurality of the Court in <i>United States</i> v. <i>Williams,</i> <span class="citation" data-id="9420563"><a href="/opinion/104889/united-states-v-williams/" aria-description="Citation for case: United States v. Williams">341 U. S. 70</a></span>, to comprehend only the rights arising immediately from the relationship of the individual to the central government. And see <i>United States</i> v. <i>Cruikshank,</i> <span class="citation" data-id="9417049"><a href="/opinion/89309/united-states-v-cruikshank/" aria-description="Citation for case: United States v. Cruikshank">92 U. S. 542</a></span>.<sup>[3]</sup> But this construction was demanded by § 241, which penalizes conspiracies of private individuals acting as such, while § 1979 applies only to action taken "under color of any statute," etc. Different problems of statutory meaning are presented by two enactments deriving from different <span class="star-pagination">*206</span> constitutional sources. See the <i>Civil Rights Cases,</i> <span class="citation" data-id="90897"><a href="/opinion/90897/civil-rights-cases/" aria-description="Citation for case: Civil Rights Cases">109 U. S. 3</a></span>. Compare <i>United States</i> v. <i>Williams, supra</i><i>,</i> with <i>Screws</i> v. <i>United States,</i> <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">325 U. S. 91</a></span>. If petitioners have alleged facts constituting a deprivation under color of state authority of a right assured them by the Fourteenth Amendment, they have brought themselves within § 1979. <i>Douglas</i> v. <i>Jeannette,</i> <span class="citation" data-id="9419344"><a href="/opinion/103833/douglas-v-city-of-jeannette/" aria-description="Citation for case: Douglas v. City of Jeannette">319 U. S. 157</a></span>; <i>Hague</i> v. <i>C. I. O.,</i> <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/#525" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">307 U. S. 496, 525-526</a></span> (opinion of Stone, J.).<sup>[4]</sup></p>
<p>To be sure, <i>Screws</i> v. <i>United States, supra</i><i>,</i> requires a finding of specific intent in order to sustain a conviction under the cognate penal provisions of <span class="citation no-link">18 U. S. C. § 242</span><sup>[5]</sup> "an intent to deprive a person of a right which has been made specific either by the express terms of the Constitution or laws of the United States or by decisions interpreting them." <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/#104" aria-description="Citation for case: Screws v. United States">325 U. S., at 104</a></span>. Petitioners' complaint here alleges no such specific intent. But, for a number of reasons, this requirement of <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> should not be carried over and applied to civil actions under § 1979. First, the word "willfully" in <span class="citation no-link">18 U. S. C. § 242</span> from which the requirement of intent was derived in <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> does not appear in § 1979. Second, § 1979, by the very fact that it is a civil provision, invites treatment different from that to be given its criminal analogue. The constitutional scruples concerning vagueness which were deemed to compel the <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> construction have less force in the context of a civil proceeding,<sup>[6]</sup><span class="star-pagination">*207</span> and § 1979, insofar as it creates an action for damages, must be read in light of the familiar basis of tort liability that a man is responsible for the natural consequences of his acts. Third, even in the criminal area, the specific intent demanded by <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> has proved to be an abstraction serving the purposes of a constitutional need without impressing any actual restrictions upon the nature of the crime which the jury tries. The <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> opinion itself said that "The fact that the defendants may not have been thinking in constitutional terms is not material where their aim was not to enforce local law but to deprive a citizen of a right and that right was protected by the Constitution." <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/#106" aria-description="Citation for case: Screws v. United States">325 U. S., at 106</a></span>. And lower courts in applying the statute have allowed inference of the requisite specific intent from evidence, it would appear, of malevolence alone.<sup>[7]</sup> But if intent to infringe "specific" constitutional rights comes in practice to mean no more than intent without justification to bring about the circumstances which infringe those rights, then the consequences of introducing the specific intent issue into a litigation is, in effect, to require fictional pleading, needlessly burden jurors with abstruse instructions, and lessen the degree of control which federal courts have over jury vagaries.</p>
<p>If the courts are to enforce § 1979, it is an unhappy form of judicial disapproval to surround it with doctrines which partially and unequally obstruct its operation. Specific intent in the context of the section would cause <span class="star-pagination">*208</span> such embarrassment without countervailing justification. Petitioners' allegations that respondents in fact did the acts which constituted violations of constitutional rights are sufficient.</p>
<p></p>
<h2>II.</h2>
<p>To show such violations, petitioners invoke primarily the Amendment's Due Process Clause.<sup>[8]</sup> The essence of their claim is that the police conduct here alleged offends those requirements of decency and fairness which, because they are "implicit in the concept of ordered liberty," are imposed by the Due Process Clause upon the States. <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319, 325</a></span>. When we apply to their complaint that standard of a "principle of justice so rooted in the traditions and conscience of our people as to be ranked as fundamental,"<sup>[9]</sup> which has been the touchstone for this Court's enforcement of due process,<sup>[10]</sup> the merit of this constitutional claim is evident. The conception expressed in <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span>, that "The security of one's privacy against arbitrary intrusion by the police. . . is basic to a free society," was not an innovation of <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>.</i> The tenet that there exists a realm of sanctuary surrounding every individual and in frangible, save in a very limited class of circumstances, by the agents of government, had informed the decision of the King's Bench two centuries earlier in <i>Entick</i> v. <i>Carrington,</i> 2 Wils. 275, had been the basis of Otis' contemporary speech against the Writ of <span class="star-pagination">*209</span> Assistance, see Gray's notes in Quincy's Massachusetts Reports, App. I, at 471; Tudor, Life of James Otis (1823) 63, and has in the intervening years found expression not only in the Fourth Amendment to the Constitution of the United States, but also in the fundamental law of every State.<sup>[11]</sup> Modern totalitarianisms have been a stark reminder, but did not newly teach, that the kicked-in door is the symbol of a rule of fear and violence fatal to institutions founded on respect for the integrity of man.</p>
<p>The essence of the liberty protected by the common law and by the American constitutions was "the right to shut the door on officials of the state unless their entry is under proper authority of law"; particularly, "the right to resist unauthorized entry which has as its design the securing of information to fortify the coercive power of the state against the individual." <i>Frank</i> v. <i>Maryland,</i> 359 U. S. <span class="star-pagination">*210</span> 360, 365.<sup>[12]</sup> Searches of the dwelling house were the special object of this universal condemnation of official intrusion.<sup>[13]</sup> Night-time search was the evil in its most obnoxious form.<sup>[14]</sup> Few reported cases have presented all of the manifold aggravating circumstances which petitioners here allegeintrusion <i>en masse,</i> by dark, by force, unauthorized by warrant, into an occupied private home, without even the asserted justification of belief by the intruders that the inhabitants were presently committing some criminal act within; physical abuse and the calculated degradation of insult and forced nakedness; sacking and disordering of personal effects throughout the home; arrest and detention against the background terror of threatened criminal proceedings. Wherever similar conduct has appeared, the courts have unanimously condemned police entries as lawless.<sup>[15]</sup></p>
<p><span class="star-pagination">*211</span> If the question whether due process forbids this kind of police invasion were before us in isolation, the answer would be quick. If, for example, petitioners had sought damages in the state courts of Illinois and if those courts had refused redress on the ground that the official character of the respondents clothed them with civil immunity, we would be faced with the sort of situation to which the language in the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> opinion was addressed: "we have no hesitation in saying that were a State affirmatively to sanction such police incursion into privacy it would run counter to the guaranty of the Fourteenth Amendment." <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#28" aria-description="Citation for case: Wolf v. Colorado">338 U. S., at 28</a></span>. If that issue is not reached in this case it is not because the conduct which the record here presents can be condoned. But by bringing their action in a Federal District Court petitioners cannot rest on the Fourteenth Amendment <i>simpliciter.</i> They invoke the protection of a specific statute by which Congress restricted federal judicial enforcement of its guarantees to particular enumerated circumstances. They must show not only that their constitutional rights have been infringed, but that they have been infringed "under color of [state] statute, ordinance, regulation, custom, or usage," as that phrase is used in the relevant congressional enactment.</p>
<p></p>
<h2>III.</h2>
<p>Of course, if Congress by appropriate statutory language attempted to reach every act which could be attributed to the States under the Fourteenth Amendment's prohibition: "No State shall . . . ," the reach of the statute would be the reach of the Amendment itself. Relevant to the enforcement of such a statute would be not only the concept of state action as this Court has developed it, see <i>Nixon</i> v. <i>Condon,</i> <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/#89" aria-description="Citation for case: Nixon v. Condon">286 U. S. 73, 89</a></span>, but also considerations of the power of Congress, under the Amendment's Enforcement Clause, to determine what <span class="star-pagination">*212</span> is "appropriate legislation" to protect the rights which the Fourteenth Amendment secures. Cf. <i>United States</i> v. <i>Raines,</i> <span class="citation" data-id="8937760"><a href="/opinion/8947114/united-states-v-raines/" aria-description="Citation for case: United States v. Raines">362 U. S. 17</a></span>. Still, in this supposed case we would arrive at the question of what Congress could do only after we had determined what it was that Congress had done. So, in the case before us now, we must ask what Congress did in 1871. We must determine what Congress meant by "under color" of enumerated state authority.<sup>[16]</sup></p>
<p>Congress used that phrase not only in R. S. § 1979, but also in the criminal provisions of § 2 of the First Civil Rights Act of April 9, 1866, <span class="citation no-link">14 Stat. 27</span>, from which is derived the present <span class="citation no-link">18 U. S. C. § 242</span>,<sup>[17]</sup> and in both cases used it with the same purpose.<sup>[18]</sup> During the seventy years <span class="star-pagination">*213</span> which followed these enactments, cases in this Court in which the "under color" provisions were invoked uniformly involved action taken either in strict pursuance of some specific command of state law<sup>[19]</sup> or within the scope of executive discretion in the administration of state laws.<sup>[20]</sup><span class="star-pagination">*214</span> The same is true, with two exceptions, in the lower federal courts.<sup>[21]</sup> In the first of these two cases it was held that § 1979 was not directed to instances of lawless police brutality, although the ruling was not put on "under color" <span class="star-pagination">*215</span> grounds.<sup>[22]</sup> In the second, an indictment charging a county tax collector with depriving one Ah Koo of a federally secured right under color of a designated California law, set forth in the indictment, was held insufficient against a demurrer. <i>United States</i> v. <i>Jackson,</i> <span class="citation" data-id="9300552"><a href="/opinion/9305449/united-states-v-jackson/" aria-description="Citation for case: United States v. Jackson">26 Fed. Cas. 563</a></span>, No. 15,459 (C. C. D. Cal. 1874). The court wrote:</p>
<blockquote>"The indictment contains no averment that Ah Koo was a foreign miner, and within the provisions of the state law. If this averment be unnecessary . . . the act of congress would then be held to apply to a case of illegal extortion by a tax collector from any person, <span class="star-pagination">*216</span> though such exaction might be wholly unauthorized by the law under which the officer pretended to act.</blockquote>
<blockquote>"We are satisfied that it was not the design of congress to prevent or to punish such abuse of authority by state officers. The object of the act was, not to prevent illegal exactions, but to forbid the execution of state laws, which, by the act itself, are made void. . . .</blockquote>
<blockquote>"It would seem, necessarily, to follow, that the person from whom the tax was exacted must have been a person from whom, under the provisions of the state law, the officer was authorized to exact it. The statute requires that a party shall be subjected to a deprivation of right secured by the statute under color of some law, statute, order or custom; but if this exaction, although made by a tax collector, has been levied upon a person not within the provisions of the state law, the exaction cannot be said to have been made `under color of law,' any more than a similar exaction from a Chinese miner, made by a person wholly unauthorized, and under the pretense of being a tax collector." <span class="citation" data-id="9300552"><a href="/opinion/9305449/united-states-v-jackson/#563" aria-description="Citation for case: United States v. Jackson"><i>Id.,</i> at 563-564</a></span>.</blockquote>
<p>Throughout this period, the only indication of this Court's views on the proper interpretation of the "under color" language is a dictum in the <i>Civil Rights Cases,</i> <span class="citation" data-id="90897"><a href="/opinion/90897/civil-rights-cases/" aria-description="Citation for case: Civil Rights Cases">109 U. S. 3</a></span>. There, in striking down other Civil Rights Act provisions which, as the Court regarded them, attempted to reach private conduct not attributable to state authority, Mr. Justice Bradley contrasted those provisions with § 2 of the Act of 1866: "This [latter] law is clearly corrective in its character, intended to counteract and furnish redress against State laws and proceedings, and customs having the force of law, which sanction the wrongful acts specified." <i>Id.,</i> at 16.</p>
<p>A sharp change from this uniform application of seventy years was made in 1941, but without acknowledgment or <span class="star-pagination">*217</span> indication of awareness of the revolutionary turnabout from what had been established practice. The opinion in <i>United States</i> v. <i>Classic,</i> <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">313 U. S. 299</a></span>, accomplished this. The case presented an indictment under § 242 charging certain local Commissioners of Elections with altering ballots cast in a primary held to nominate candidates for Congress. Sustaining the sufficiency of the indictment in an extensive opinion concerned principally with the question whether the right to vote in such a primary was a right secured by the Constitution,<sup>[23]</sup> Mr. Justice Stone wrote that the alteration of the ballots was "under color" of state law. This holding was summarily announced without exposition; it had been only passingly argued.<sup>[24]</sup> Of the three authorities cited to support it, two did not involve the "under color" statutes,<sup>[25]</sup> and the third, <i>Hague</i> v. <i>C. I. O.,</i> <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">307 U. S. 496</a></span>, was a case in which highranking municipal officials claimed authorization for their actions under municipal ordinances (here held unconstitutional) <span class="star-pagination">*218</span> and under the general police powers of the State.<sup>[26]</sup> All three of these cases had dealt with "State action" problems, and it is "State action," not the very different question of the "under color" clause, that Mr. Justice Stone appears to have considered.<sup>[27]</sup> (I joined in this opinion without having made an independent examination of the legislative history of the relevant legislation or of the authorities drawn upon for the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> construction. Acquiescence so founded does not preclude the responsible recognition of error disclosed by subsequent study.) When, however, four years later the Court was called on to review the conviction under § 242 of a Georgia County Sheriff who had beaten a Negro prisoner to death, the opinion of four of the six Justices who believed that the statute applied merely invoked <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> and <i>stare decisions</i> and did not reconsider the meaning which that case had uncritically assumed was to be attached to the language, "under color" of state authority. <i>Screws</i> v. <i>United States,</i> <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">325 U. S. 91</a></span>. The briefs in the <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> case did <span class="star-pagination">*219</span> not examine critically the legislative history of the Civil Rights Acts.<sup>[28]</sup> The only reference to this history in the plurality opinion, insofar as it bears on the interpretation of the clause "under color of . . . law," is contained in a pair of sentences discounting two statements by Senators Trumbull and Sherman regarding the Civil Rights Acts of 1866 and 1870, cited by the minority.<sup>[29]</sup> The bulk of the plurality opinion's treatment of the issue consists of the argument that "under color" had been construed in <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> and that the construction there put on the words should not be abandoned or revised. <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/#109" aria-description="Citation for case: Screws v. United States">325 U. S., at 109-113</a></span>. The case of <i>Williams</i> v. <i>United States,</i> <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/" aria-description="Citation for case: Williams v. United States">341 U. S. 97</a></span>, reaffirmed <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> and applied it to circumstances of third-degree brutality practiced by a private detective who held a special police officer's card and was accompanied by a regular policeman.<sup>[30]</sup></p>
<p><span class="star-pagination">*220</span> Thus, although this Court has three times found that conduct of state officials which is forbidden by state law may be "under color" of state law for purposes of the Civil Rights Acts, it is accurate to say that that question has never received here the consideration which its importance merits. That regard for controlling legislative history which is conventionally observed by this Court in determining the true meaning of important legislation that does not construe itself<sup>[31]</sup> has never been applied to the "under color" provisions; particularly, there has never been canvassed the full record of the debates preceding passage of the 1871 Act with which we are concerned in this case. Neither <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> nor <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> nor <i>Williams</i> warrants refusal now to take account of those debates and the illumination they afford. While we may well decline to re-examine recent cases which derive from the judicial process exercised under its adequate safeguards documenting briefs and adequate arguments on both sides as foundation for due deliberationthe relevant demands of <i>stare decisions</i> do not preclude considering, for the first time thoroughly and in the light of the best available evidence of congressional purpose, a statutory <span class="star-pagination">*221</span> interpretation which started as an unexamined assumption on the basis of inapplicable citations and has the claim of a dogma solely through reiteration. Particularly is this so when that interpretation, only recently made, was at its inception a silent reversal of the judicial history of the Civil Rights Acts for three quarters of a century.</p>
<p>"The rule of <i>stare decisions,</i> though one tending to consistency and uniformity of decision, is not inflexible." <i>Hertz</i> v. <i>Woodman,</i> <span class="citation" data-id="9418187"><a href="/opinion/97288/hertz-v-woodman/#212" aria-description="Citation for case: Hertz v. Woodman">218 U. S. 205, 212</a></span>. It is true, of course, that the reason for the rule is more compelling in cases involving inferior law, law capable of change by Congress, than in constitutional cases, where this Court although even in such cases a wise consciousness of the limitations of individual vision has impelled it always to give great weight to prior decisionsnevertheless bears the ultimate obligation for the development of the law as institutions develop. See, <i>e. g., </i><i>Smith</i> v. <i>Allwright,</i> <span class="citation" data-id="103962"><a href="/opinion/103962/smith-v-allwright/" aria-description="Citation for case: Smith v. Allwright">321 U. S. 649</a></span>. But the Court has not always declined to re-examine cases whose outcome Congress might have changed. See Mr. Justice Brandeis, dissenting, in <i>Burnet</i> v. <i>Coronado Oil &amp; Gas Co.,</i> <span class="citation" data-id="8148759"><a href="/opinion/8186832/burnet-v-coronado-oil-gas-co/#406" aria-description="Citation for case: Burnet v. Coronado Oil &amp; Gas Co.">285 U. S. 393, 406-407, n. 1</a></span>. Decisions involving statutory construction, even decisions which Congress has persuasively declined to overrule, have been overruled here. See <i>Girouard</i> v. <i>United States,</i> <span class="citation" data-id="9419823"><a href="/opinion/104285/girouard-v-united-states/" aria-description="Citation for case: Girouard v. United States">328 U. S. 61</a></span>, overruling <i>United States</i> v. <i>Schwimmer,</i> <span class="citation" data-id="9418678"><a href="/opinion/101446/united-states-v-schwimmer/" aria-description="Citation for case: United States v. Schwimmer">279 U. S. 644</a></span>, <i>United States</i> v. <i>Macintosh,</i> <span class="citation" data-id="9418720"><a href="/opinion/101765/united-states-v-macintosh/" aria-description="Citation for case: United States v. MacIntosh">283 U. S. 605</a></span>, and <i>United States</i> v. <i>Bland,</i> <span class="citation" data-id="9418722"><a href="/opinion/101766/united-states-v-bland/" aria-description="Citation for case: United States v. Bland">283 U. S. 636</a></span>; see also <i>Commissioner</i> v. <i>Estate of Church,</i> <span class="citation" data-id="9420263"><a href="/opinion/104616/commissioner-v-estate-of-church/" aria-description="Citation for case: Commissioner v. Estate of Church">335 U. S. 632</a></span>, overruling <i>May</i> v. <i>Heiner,</i> <span class="citation" data-id="101552"><a href="/opinion/101552/may-v-heiner/" aria-description="Citation for case: May v. Heiner">281 U. S. 238</a></span>.</p>
<p>And with regard to the Civil Rights Acts there are reasons of particular urgency which authorize the Court indeed, which make it the Court's responsibilityto reappraise in the hitherto skimpily considered context of R. S. § 1979 what was decided in <i>Classic, Screws</i> and <i>Williams.</i> This is not an area of commercial law in which, presumably, individuals may have arranged their affairs in <span class="star-pagination">*222</span> reliance on the expected stability of decision. Compare <i>National Bank</i> v. <i>Whitney,</i> <span class="citation" data-id="9417263"><a href="/opinion/90305/national-bank-v-whitney/" aria-description="Citation for case: National Bank v. Whitney">103 U. S. 99</a></span>; <i>Vail</i> v. <i>Arizona,</i> <span class="citation" data-id="96723"><a href="/opinion/96723/vail-v-arizona/" aria-description="Citation for case: Vail v. Arizona">207 U. S. 201</a></span>; <i>Walling</i> v. <i>Halliburton Oil Well Cementing Co.,</i> <span class="citation" data-id="9419984"><a href="/opinion/104413/walling-v-halliburton-oil-well-cementing-co/" aria-description="Citation for case: Walling v. Halliburton Oil Well Cementing Co.">331 U. S. 17</a></span>; <i>United States</i> v. <i>South Buffalo R. Co.,</i> <span class="citation" data-id="9420149"><a href="/opinion/104542/united-states-v-south-buffalo-railway-co/" aria-description="Citation for case: United States v. South Buffalo Railway Co.">333 U. S. 771</a></span>. Nor is it merely a mine-run statutory question involving a narrow compass of individual rights and duties. The issue in the present case concerns directly a basic problem of American federalism: the relation of the Nation to the States in the critically important sphere of municipal law administration. In this aspect, it has significance approximating constitutional dimension. Necessarily, the construction of the Civil Rights Acts raises issues fundamental to our institutions. This imposes on this Court a corresponding obligation to exercise its power within the fair limits of its judicial discretion. "We recognize that <i>stare decisions</i> embodies an important social policy. It represents an element of continuity in law, and is rooted in the psychologic need to satisfy reasonable expectations. But <i>stare decisions</i> is a principle of policy and not a mechanical formula of adherence to the latest decision, however recent and questionable. . . ." <i>Helvering</i> v. <i>Hallock,</i> <span class="citation" data-id="9419079"><a href="/opinion/103292/helvering-v-hallock/#119" aria-description="Citation for case: Helvering v. Hallock">309 U. S. 106, 119</a></span>.</p>
<p>Now, while invoking the prior decisions which have given "under color of [law]" a content that ignores the meaning fairly comported by the words of the text and confirmed by the legislative history, the Court undertakes a fresh examination of that legislative history. The decision in this case, therefore, does not rest on <i>stare decisions,</i> and the true construction of the statute may be thought to be as free from the restraints of that doctrine as though the matter were before us for the first time. Certainly, none of the implications which the Court seeks to draw from silences in the minority reports of congressional committees in 1956, 1957, and 1960, or from the use of "under color" language in the very different context of the Act of <span class="citation" data-id="101552"><a href="/opinion/101552/may-v-heiner/#6" aria-description="Citation for case: May v. Heiner">May 6, 1960</a></span>, <span class="star-pagination">*223</span> 74 Stat. 86concerned, in relevant part, with the preservation of election records and with the implementation of the franchiseserves as an impressive bar to re-examination of the true scope of R. S. § 1979 itself in its pertinent legislative setting.<sup>[32]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*224</span> IV.</h2>
<p>This case squarely presents the question whether the intrusion of a city policeman for which that policeman can show no such authority at state law as could be successfully interposed in defense to a state-law action against him, is nonetheless to be regarded as "under color" of state authority within the meaning of R. S. § 1979. Respondents, in breaking into the Monroe apartment, violated the laws of the State of Illinois.<sup>[33]</sup> Illinois law <span class="star-pagination">*225</span> appears to offer a civil remedy for unlawful searches;<sup>[34]</sup> petitioners do not claim that none is available. Rather they assert that they have been deprived of due process of law and of equal protection of the laws under color of state law, although from all that appears the courts of Illinois are available to give them the fullest redress which the common law affords for the violence done them, nor does any "statute, ordinance, regulation, custom, or usage" of the State of Illinois bar that redress. Did the enactment by Congress of § 1 of the Ku Klux Act of 1871 encompass such a situation?</p>
<p>That section, it has been noted, was patterned on the similar criminal provision of § 2, Act of April 9, 1866. The earlier Act had as its primary object the effective nullification of the Black Codes, those statutes of the Southern legislatures which had so burdened and disqualified the Negro as to make his emancipation appear illusory.<sup>[35]</sup> The Act had been vetoed by President Johnson, whose veto message describes contemporary understanding of its second section; the section, he wrote,</p>
<blockquote>"seems to be designed to apply to some existing or future law of State or Territory which may conflict with the provisions of the bill . . . . It provides for counteracting such forbidden legislation by imposing fine and imprisonment upon the legislators who may pass such conflicting laws, or upon the officers or agents who shall put, or attempt to put, them into execution. It means an official offense, not a common <span class="star-pagination">*226</span> crime committed against law upon the persons or property of the black race. Such an act may deprive the black man of his property, but not of the right to hold property. It means a deprivation of the right itself, either by the State judiciary or the State Legislature."<sup>[36]</sup></blockquote>
<p>And Senator Trumbull, then Chairman of the Senate Judiciary Committee,<sup>[37]</sup> in his remarks urging its passage over the veto, expressed the intendment of the second section as those who voted for it read it:</p>
<blockquote>"If an offense is committed against a colored person simply because he is colored, in a State where the law affords him the same protection as if he were white, this act neither has nor was intended to have anything to do with his case, because he has adequate remedies in the State courts; but if he is discriminated against under color of State laws because he is colored, then it becomes necessary to interfere for his protection."<sup>[38]</sup></blockquote>
<p>Section 2 of the 1866 Act was re-enacted in substance in 1870 as part of "An Act to enforce the Right of Citizens. . . to vote in the several States . . . ," <span class="citation no-link">16 Stat. 140</span>, <span class="star-pagination">*227</span> 144. The following colloquy on that occasion is particularly revealing:</p>
<blockquote>"Mr. SHERMAN. . . . My colleague cannot deny that we can by appropriate legislation prevent any private person from shielding himself under a State regulation, and thus denying to a person the right to vote . . . .</blockquote>
<blockquote>"Mr. CASSERLY. I should like to ask the Senator from Ohio how a State can be said to abridge the right of a colored man to vote when some irresponsible person in the streets is the actor in that wrong?</blockquote>
<blockquote>"Mr. SHERMAN. If the offender, who may be a loafer, the meanest man in the streets, covers himself under the protection or color of a law or regulation or constitution of a State, he may be punished for doing it.</blockquote>
<blockquote>"Mr. CASSERLY. Suppose the State law authorizes the colored man to vote; what then?</blockquote>
<blockquote>"Mr. SHERMAN. That is not the case with which we are dealing. . . . This bill only proposes to deal with offenses committed by officers or persons under color of existing State law, under color of existing State constitutions. No man could be convicted under this bill reported by the Judiciary Committee unless the denial of the right to vote was done under color or pretense of State regulation. The whole bill shows that. . . . [T]he first and second sections of the bill . . . simply punish officers as well as persons for discrimination under color of State laws or constitutions; and it so provides all the way through."<sup>[39]</sup></blockquote>
<p><span class="star-pagination">*228</span> The original text of the present § 1979 contained words, left out in the Revised Statutes, which clarified the objective to which the provision was addressed:</p>
<blockquote>"That any person who, under color of any law, statute, ordinance, regulation, custom, or usage of any State, shall subject, or cause to be subjected, any person within the jurisdiction of the United States to the deprivation of any rights, privileges, or immunities secured by the Constitution of the United States, shall, <i>any such law, statute, ordinance, regulation, custom, or usage of the State to the contrary notwithstanding,</i> be liable to the party injured . . . ."<sup>[40]</sup></blockquote>
<p>Representative Shellabarger, reporting the section, explained it to the House as "in its terms carefully confined to giving a civil action for such wrongs against citizenship as are done under color of State laws which abridge these rights."<sup>[41]</sup> Senator Edmunds, steering the measure through the Senate, found constitutional sanction for it in the Fourteenth Amendment, explaining that state action may consist in executive nonfeasance as well as malfeasance, so that any offenses against a citizen in a <span class="star-pagination">*229</span> State are susceptible of federal protection "unless the criminal who shall commit those offenses is punished and the person who suffers receives that redress which the principles and spirit of the laws entitle him to have."<sup>[42]</sup> And James A. Garfield supported the bill in the House as "so guarded as to preserve intact the autonomy of the States, the machinery of the State governments, and the municipal organizations established under State laws."<sup>[43]</sup></p>
<p>Indeed, the Ku Klux Act as a whole encountered in the course of its passage strenuous constitutional objections which focused precisely upon an assertedly unauthorized extension of federal judicial power into areas of exclusive state competence.<sup>[44]</sup> A special target was § 2 of the bill as reported to the House, providing criminal penalties:</p>
<blockquote>"if two or more persons shall, within the limits of any State, band, conspire, or combine together to do <span class="star-pagination">*230</span> any act in violation of the rights, privileges, or immunities of any person, to which he is entitled under the Constitution and laws of the United States, which, committed within a place under the sole and exclusive jurisdiction of the United States, would, under any law of the United States then in force, constitute the crime of either murder, manslaughter, mayhem, robbery, assault and battery, perjury, subornation of perjury, criminal obstruction of legal, process [<i>sic</i>] or resistance of officers in discharge of official duty, arson, or larceny . . . ."<sup>[45]</sup></blockquote>
<p>In vain the proponents of this section argued its propriety, seeking to support it by argument <i>ex necessitate</i> from the complete failure of state judicial and executive organs to control the depredations of the Klan.<sup>[46]</sup> Even <span class="star-pagination">*231</span> in the Reconstruction Congress, the majority party split. Many balked at legislation which they regarded as establishing a general federal jurisdiction for the protection of person and property in the States.<sup>[47]</sup> Only after a complete <span class="star-pagination">*232</span> rewriting of the section to meet these constitutional objections could the bill be passed.<sup>[48]</sup> Yet almost none of those who had decried § 2 as undertaking impermissibly to make the national courts tribunals of concurrent jurisdiction for the punishment of state-law offenses expressed similar objections to § 1, later § 1979.<sup>[49]</sup> One of the most <span class="star-pagination">*233</span> vehement of those who could find no constitutional sanction for federal judicial control of conduct already proscribed by state law, and who therefore opposed original § 2 as reaching beyond the limits of congressional competence, expressly supported § 1 as affording "further redress for violations under State authority of constitutional rights."<sup>[50]</sup></p>
<p>The general understanding of the legislators unquestionably was that, as amended, the Ku Klux Act did "not undertake to furnish redress for wrongs done by one person upon another in any of the States . . . in violation of their laws, unless he also violated some law of the United States, nor to punish one person for an ordinary assault and battery . . . ."<sup>[51]</sup> Even those whoopposing the constitutional objectorsfound sufficient congressional power in the Enforcement Clause of the Fourteenth Amendment to give this kind of redress, deemed inexpedient the exercise of any such power: "Convenience and courtesy to the States suggest a sparing use, and never so far as to supplant the State authorities except in cases of extreme necessity, and when the State governments criminally refuse or neglect those duties which are imposed <span class="star-pagination">*234</span> upon them."<sup>[52]</sup> Extreme Radicals, those who believed that the remedy for the oppressed Unionists in the South was a general expansion of federal judicial jurisdiction so that "loyal men could have the privilege of having their causes, civil and criminal, tried in the Federal courts." were disappointed with the Act as passed.<sup>[53]</sup></p>
<p>Finally, it is significant that the opponents of the Act, exhausting ingenuity to discover constitutional objections to every provision of it, also construed § 1 as addressed only to conduct authorized by state law, and therefore within the admitted permissible reach of Fourteenth Amendment federal power. "The first section of this bill prohibits any invidious legislation by States against the rights or privileges of citizens of the United States," one such opponent paraphrased the provision.<sup>[54]</sup> And Senator Thurman, who insisted vociferously on the absence of federal power to penalize a conspiracy of individuals to violate state law ("that is a case of mere individual violence, having no color whatsoever of authority of law, either Federal or State; and to say that you can punish men for that mere conspiracy, which is their individual act, and which is a crime against the State laws themselves, punishable by the State laws, is simply to wipe out all the State jurisdiction over crimes and transfer it bodily to the Congress"),<sup>[55]</sup> admitted without question the constitutionality of § 1<sup>[56]</sup> ("It refers to a deprivation under color of law, either statute law or `custom or usage' which has become common law").<sup>[57]</sup></p>
<p><span class="star-pagination">*235</span> The Court now says, however, that "It was not the unavailability of state remedies but the failure of certain States to enforce the laws with an equal hand that furnished the powerful momentum behind this `force bill.' " Of course, if the notion of "unavailability" of remedy is limited to mean an absence of statutory, paper right, this is in large part true.<sup>[58]</sup> Insofar as the Court undertakes to demonstrateas the bulk of its opinion seems to do that § 1979 was meant to reach some instances of action not specifically authorized by the avowed, apparent, written law inscribed in the statute books of the States, the argument knocks at an open door. No one would or could deny this, for by its express terms the statute comprehends deprivations of federal rights under color of any "statute, ordinance, regulation, <i>custom, or usage</i>" of a State. (Emphasis added.) The question is, <i>what</i> class of cases other than those involving state statute law were meant to be reached. And, with respect to this question, the Court's conclusion is undermined by the very portions of the legislative debates which it cites. For surely the misconduct of individual municipal police officers, subject to the effective oversight of appropriate state administrative and judicial authorities, presents a situation which differs <i>toto coelo</i> from one in which "Immunity is given to crime, and the records of the public tribunals are searched in vain for any evidence of effective redress,"<sup>[59]</sup> or in which murder rages while a State makes <span class="star-pagination">*236</span> "no successful effort to bring the guilty to punishment or afford protection or redress,"<sup>[60]</sup> or in which the "State courts . . . [are] unable to enforce the criminal laws . . . or to suppress the disorders existing,"<sup>[61]</sup> or in which, in a State's "judicial tribunals one class is unable to secure that enforcement of their rights and punishment for their infraction which is accorded to another,"<sup>[62]</sup> or "of . . . hundreds of outrages . . . not one [is] punished,"<sup>[63]</sup> or "the courts of the . . . States fail and refuse to do their duty in the punishment of offenders against the law,"<sup>[64]</sup> or in which a "class of officers charged under the laws with their administration permanently and as a rule refuse to extend [their] protection."<sup>[65]</sup> These statements indicate that Congressmade keenly aware by the post-bellum conditions in the South that States through their authorities could sanction offenses against the individual by settled practice which established state law as truly as written codesdesigned § 1979 to reach, as well, official conduct which, because engaged in "permanently and as a rule," or "systematically,"<sup>[66]</sup> came through acceptance by law-administering officers to constitute "custom, or usage" having the cast of law. See <i>Nashville, C. &amp; St. L. R. Co.</i> v. <i>Browning,</i> <span class="citation" data-id="103360"><a href="/opinion/103360/nashville-chattanooga-st-louis-railway-v-browning/#369" aria-description="Citation for case: Nashville, Chattanooga &amp; St. Louis Railway v. Browning">310 U. S. 362, 369</a></span>. They do not indicate an attempt to reach, nor does the statute by its terms include, instances of acts in defiance of state law and which no settled state practice, no systematic pattern of official action or inaction, no "custom, or usage, of any State," insulates from effective and adequate reparation by the State's authorities.</p>
<p><span class="star-pagination">*237</span> Rather, all the evidence converges to the conclusion that Congress by § 1979 created a civil liability enforceable in the federal courts only in instances of injury for which redress was barred in the state courts because some "statute, ordinance, regulation, custom, or usage" sanctioned the grievance complained of. This purpose, manifested even by the so-called "Radical" Reconstruction Congress in 1871, accords with the presuppositions of our federal system. The jurisdiction which Article III of the Constitution conferred on the national judiciary reflected the assumption that the state courts, not the federal courts, would remain the primary guardians of that fundamental security of person and property which the long evolution of the common law had secured to one individual as against other individuals. The Fourteenth Amendment did not alter this basic aspect of our federalism.<sup>[67]</sup></p>
<p>Its commands were addressed to the States. Only when the States, through their responsible organs for the formulation and administration of local policy, sought to deny or impede access by the individual to the central government in connection with those enumerated functions assigned to it, or to deprive the individual of a certain minimal fairness in the exercise of the coercive forces of the State, or without reasonable justification to treat him differently than other persons subject to their jurisdiction, was an overriding federal sanction imposed. As between individuals, no corpus of substantive rights was guaranteed by the Fourteenth Amendment, but only "due process of law" in the ascertainment and enforcement of rights and equality in the enjoyment of rights and safeguards that the States afford. This was the base of the distinction between federal citizenship and state <span class="star-pagination">*238</span> citizenship drawn by the <i>Slaughter-House Cases,</i> <span class="citation" data-id="9416892"><a href="/opinion/88661/butchers-benevolent-assn-v-crescent-city-live-stock-landing/" aria-description="Citation for case: Butchers&#x27; Benevolent Ass&#x27;n v. Crescent City Live-Stock...">16 Wall. 36</a></span>. This conception begot the "State action" principle on which, from the time of the <i>Civil Rights Cases,</i> <span class="citation" data-id="90897"><a href="/opinion/90897/civil-rights-cases/" aria-description="Citation for case: Civil Rights Cases">109 U. S. 3</a></span>, this Court has relied in its application of Fourteenth Amendment guarantees. As between individuals, that body of mutual rights and duties which constitute the civil personality of a man remains essentially the creature of the legal institutions of the States.</p>
<p>But, of course, in the present case petitioners argue that the wrongs done them were committed not by individuals but by the police as state officials. There are two senses in which this might be true. It might be true if petitioners alleged that the redress which state courts offer them against the respondents is different than that which those courts would offer against other individuals, guilty of the same conduct, who were not the police. This is not alleged. It might also be true merely because the respondents <i>are</i> the policebecause they are clothed with an appearance of official authority which is in itself a factor of significance in dealings between individuals. Certainly the night-time intrusion of the man with a star and a police revolver is a different phenomenon than the night-time intrusion of a burglar. The aura of power which a show of authority carries with it has been created by state government. For this reason the national legislature, exercising its power to implement the Fourteenth Amendment, might well attribute responsibility for the intrusion to the State and legislate to protect against such intrusion. The pretense of authority alone might seem to Congress sufficient basis for creating an exception to the ordinary rule that it is to the state tribunals that individuals within a State must look for redress against other individuals within that State. The same pretense of authority might suffice to sustain congressional legislation creating the exception. See <i>Ex parte Virginia,</i> <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/" aria-description="Citation for case: Ex Parte Virginia">100 U. S. 339</a></span>. But until Congress has <span class="star-pagination">*239</span> declared its purpose to shift the ordinary distribution of judicial power for the determination of causes between co-citizens of a State, this Court should not make the shift. Congress has not in § 1979 manifested that intention.</p>
<p>The unwisdom of extending federal criminal jurisdiction into areas of conduct conventionally punished by state penal law is perhaps more obvious than that of extending federal civil jurisdiction into the traditional realm of state tort law. But the latter, too, presents its problems of policy appropriately left to Congress. Suppose that a state legislature or the highest court of a State should determine that within its territorial limits no damages should be recovered in tort for pain and suffering, or for mental anguish, or that no punitive damages should be recoverable. Since the federal courts went out of the business of making "general law," <i>Erie R. Co.</i> v. <i>Tompkins,</i> <span class="citation" data-id="9418969"><a href="/opinion/103012/erie-railroad-v-tompkins/" aria-description="Citation for case: Erie Railroad v. Tompkins">304 U. S. 64</a></span>, such decisions of local policy have admittedly been the exclusive province of state lawmakers. Should the civil liability for police conduct which can claim no authority under local law, which is actionable as common-law assault or trespass in the local courts, comport different rules? Should an unlawful intrusion by a policeman in Chicago entail different consequences than an unlawful intrusion by a hoodlum? These are matters of policy in its strictly legislative sense, not for determination by this Court. And if it be, as it is, a matter for congressional choice, the legislative evidence is overwhelming that § 1979 is not expressive of that choice. Indeed, its precise limitation to acts "under color" of state statute, ordinance or other authority appears on its face designed to leave all questions of the nature and extent of liability of individuals to the laws of the several States except when a State seeks to shield those individuals under the special barrier of state authority. To extend Civil Rights Act liability beyond that point is <span class="star-pagination">*240</span> to interfere in areas of state policymaking where Congress has not determined to interfere.</p>
<p>Nor will such interference be negligible. One argument urged in <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> in favor of the result which that case reached was the announced policy of self-restraint of the Department of Justice in the prosecution of cases under <span class="citation no-link">18 U. S. C. § 242</span>. See <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/#159" aria-description="Citation for case: Screws v. United States">325 U. S., at 159-160</a></span>. Experience indicates that private litigants cannot be expected to show the same consideration for the autonomy of local administration which the Department purportedly shows.<sup>[68]</sup></p>
<p>Relevant also are the effects upon the institution of federal constitutional adjudication of sustaining under § 1979 damage actions for relief against conduct allegedly violative of federal constitutional rights, but plainly <span class="star-pagination">*241</span> violative of state law. Permitting such actions necessitates the immediate decision of federal constitutional issues despite the admitted availability of state-law remedies which would avoid those issues.<sup>[69]</sup> This would make inroads, throughout a large area, upon the principle of federal judicial self-limitation which has become a significant instrument in the efficient functioning of the national judiciary. See

[...TRUNCATED 140224 of 260224 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
