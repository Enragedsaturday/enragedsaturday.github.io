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

## GROUP: _overhaul2/lake/cases/LaChance v. Erickson.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "LaChance v. Erickson"
type: case
citation: "522 U.S. 262 (1998)"
parallel_cite: "118 S. Ct. 753; 139 L. Ed. 2d 695"
neutral_cite: 1998 U.S. LEXIS 636
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1998
date_decided: 1998-01-21
docket: 96-1395
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1998-01-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: LaChance v. Erickson
  varies_by_point: false
  scope_note: "Good law; marks the boundary of the Garrity line — the privilege lets a public employee stay silent, but not lie."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118163/lachance-v-erickson/"
  cluster_id: 118163
  opinion_id: 118163
  identity_checked: true
homes:
  - page: "[[Public-Employee Compelled Statements (Garrity)]]"
    role: "Related (cross-doctrine)"
related: ["[[Garrity v. New Jersey]]", "[[Gardner v. Broderick]]", "[[Lefkowitz v. Turley]]"]
aliases: []
tags: ["case", "fifth-amendment", "due-process", "public-employee", "garrity", "false-statements", "federal-employee"]
holding: "Neither due process nor the civil-service statutes bar a federal agency from disciplining an employee for making false statements to investigators in response to an underlying misconduct charge; the right to be heard does not include a right to lie (an employee facing criminal exposure may stay silent, but may not lie)."
lake:
  record_id: LaChance v. Erickson
  status: under_review
  projected_at: 2026-07-06
---

# LaChance v. Erickson

*522 U.S. 262 (1998)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Several federal employees were the subject of agency adverse actions for misconduct, and each made false statements to agency investigators denying the charged conduct. The agencies added a false-statement charge and relied on it in part. The Merit Systems Protection Board upheld the penalties based on the underlying misconduct but overturned the false-statement charges, and the Court of Appeals for the Federal Circuit agreed, reasoning that due process barred charging an employee for denying the underlying charge. The Director of the Office of Personnel Management sought review.

## Issue
Whether the Due Process Clause or the Civil Service Reform Act precludes a federal agency from sanctioning an employee for making false statements to the agency in response to an underlying charge of employment-related misconduct.

## Rule
No. There is no right to lie, even within a right to be heard. Quoting *Bryson*: "A citizen may decline to answer the question, or answer it honestly, but he cannot with impunity knowingly and willfully answer with a falsehood." — 522 U.S. at 265. ^pin-265

The privilege protects silence, not falsehood: "If answering an agency's investigatory question could expose an employee to a criminal prosecution, he may exercise his Fifth Amendment right to remain silent." — *Id.* at 267. ^pin-267

The Court therefore held: "[W]e hold that a Government agency may take adverse action against an employee because the employee made false statements in response to an underlying charge of misconduct." — *Id.* at 268. ^pin-268

## Application
The respondent employees did not stay silent or answer truthfully; they lied to investigators about the conduct with which they were charged. A "meaningful opportunity to be heard" does not include a right to make false statements, and the absence of an oath was immaterial because the charge was making false statements, not perjury. Because each employee could have declined to answer — invoking the Fifth Amendment if answering risked criminal exposure — rather than lying, the agencies were free to sanction the false statements made in response to the underlying charges.

## Conclusion
A government agency may take adverse action against an employee for making false statements in response to an underlying misconduct charge; the Federal Circuit's judgments were reversed. Within the public-employee privilege line, *LaChance* marks the limit: the privilege secures the right to remain silent, not a right to lie.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *LaChance* is good law and complements [[Garrity v. New Jersey]], [[Gardner v. Broderick]], and [[Lefkowitz v. Turley]]: those cases protect an employee from being penalized for asserting the privilege, while *LaChance* makes clear the privilege does not shelter affirmative falsehoods.

## Appears on
- [[Public-Employee Compelled Statements (Garrity)]] — *Related (cross-doctrine)*

## Sources
- *LaChance v. Erickson*, 522 U.S. 262 (1998) — https://www.courtlistener.com/opinion/118163/lachance-v-erickson/ — pinpoints: 265, 267, 268.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "224e63005e439621", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "LaChance v. Erickson"}, "payload": {"all": [{"cite": "522 U.S. 262", "page": "262", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "522"}, {"cite": "118 S. Ct. 753", "page": "753", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "118"}, {"cite": "139 L. Ed. 2d 695", "page": "695", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "139"}, {"cite": "1998 U.S. LEXIS 636", "page": "636", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1998"}], "display": "522 U.S. 262", "official": {"cite": "522 U.S. 262", "page": "262", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "522"}, "official_selection_present": true, "record_id": "LaChance v. Erickson"}}
{"assertion_id": "077b1d9f9ba8c7c2", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-268", "record_id": "LaChance v. Erickson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-268", "pinpoint_status": "slip-only", "quote": "[W]e hold that a Government agency may take adverse action against an employee because the employee made false statements in response to an underlying charge of misconduct.", "quote_fidelity": "mismatch", "record_id": "LaChance v. Erickson", "star_marker": null}}
{"assertion_id": "0ba5c802e8e880fb", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-267", "record_id": "LaChance v. Erickson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-267", "pinpoint_status": "slip-only", "quote": "If answering an agency's investigatory question could expose an employee to a criminal prosecution, he may exercise his Fifth Amendment right to remain silent.", "quote_fidelity": "mismatch", "record_id": "LaChance v. Erickson", "star_marker": null}}
{"assertion_id": "7efe3ed076b27cae", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-265", "record_id": "LaChance v. Erickson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-265", "pinpoint_status": "slip-only", "quote": "--- # LaChance v. Erickson *522 U.S. 262 (1998)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Several federal employees were the subject of agency adverse actions for misconduct, and each made false statements to agency investigators denying the charged conduct. The agencies added a false-statement charge and relied on it in part. The Merit Systems Protection Board upheld the penalties based on the underlying misconduct but overturned the false-statement charges, and the Court of Appeals for the Federal Circuit agreed, reasoning that due process barred charging an employee for denying the underlying charge. The Director of the Office of Personnel Management sought review. ## Issue Whether the Due Process Clause or the Civil Service Reform Act precludes a federal agency from sanctioning an employee for making false statements to the agency in response to an underlying charge of employment-related misconduct. ## Rule No. There is no right to lie, even within a right to be heard. Quoting *Bryson*:", "quote_fidelity": "mismatch", "record_id": "LaChance v. Erickson", "star_marker": null}}
{"assertion_id": "f5416d381277fb49", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "LaChance v. Erickson"}, "payload": {"as_of_content": "1998-01-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "LaChance v. Erickson", "scope_note": "Good law; marks the boundary of the Garrity line — the privilege lets a public employee stay silent, but not lie.", "varies_by_point": false}}
```

### lake record — LaChance v. Erickson

```json
{
  "schema_version": "s2.v1",
  "record_id": "LaChance v. Erickson",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "LaChance v. Erickson",
    "case_name_short": "LaChance",
    "case_name_full": "LACHANCE, DIRECTOR, OFFICE OF PERSONNEL MANAGEMENT v. ERICKSON Et Al.",
    "input_case_name": "LaChance v. Erickson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1998-01-21",
    "year": 1998,
    "docket": "96-1395",
    "cluster_id": 118163,
    "lead_opinion_id": 118163,
    "sibling_ids": [
      118163
    ],
    "absolute_url": "/opinion/118163/lachance-v-erickson/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "522 U.S. 262",
      "volume": "522",
      "reporter": "U.S.",
      "page": "262",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "118 S. Ct. 753",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "753",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "139 L. Ed. 2d 695",
        "volume": "139",
        "reporter": "L. Ed. 2d",
        "page": "695",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1998 U.S. LEXIS 636",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "636",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "522 U.S. 262",
        "volume": "522",
        "reporter": "U.S.",
        "page": "262",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "118 S. Ct. 753",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "753",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "139 L. Ed. 2d 695",
        "volume": "139",
        "reporter": "L. Ed. 2d",
        "page": "695",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 U.S. LEXIS 636",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "636",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "522 U.S. 262",
    "official_selection": {
      "court_class": "scotus",
      "selected": "522 U.S. 262",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-265",
      "page": null,
      "quote": "--- # LaChance v. Erickson *522 U.S. 262 (1998)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Several federal employees were the subject of agency adverse actions for misconduct, and each made false statements to agency investigators denying the charged conduct. The agencies added a false-statement charge and relied on it in part. The Merit Systems Protection Board upheld the penalties based on the underlying misconduct but overturned the false-statement charges, and the Court of Appeals for the Federal Circuit agreed, reasoning that due process barred charging an employee for denying the underlying charge. The Director of the Office of Personnel Management sought review. ## Issue Whether the Due Process Clause or the Civil Service Reform Act precludes a federal agency from sanctioning an employee for making false statements to the agency in response to an underlying charge of employment-related misconduct. ## Rule No. There is no right to lie, even within a right to be heard. Quoting *Bryson*:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-267",
      "page": null,
      "quote": "If answering an agency's investigatory question could expose an employee to a criminal prosecution, he may exercise his Fifth Amendment right to remain silent.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-268",
      "page": null,
      "quote": "[W]e hold that a Government agency may take adverse action against an employee because the employee made false statements in response to an underlying charge of misconduct.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1998-01-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "LaChance v. Erickson",
    "varies_by_point": false,
    "scope_note": "Good law; marks the boundary of the Garrity line \u2014 the privilege lets a public employee stay silent, but not lie.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Douglas M. Wright v. United States Postal Service",
          "cluster_id": 765216,
          "cite": [
            "183 F.3d 1328",
            "1999 U.S. App. LEXIS 13194",
            "1999 WL 391364"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Stevenson v. Carroll",
          "cluster_id": 1395962,
          "cite": [
            "495 F.3d 62",
            "2007 WL 2164165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Veal",
          "cluster_id": 73222,
          "cite": [
            "153 F.3d 1233",
            "1998 U.S. App. LEXIS 38861",
            "1998 WL 564374"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Veal",
          "cluster_id": 73223,
          "cite": [
            "153 F.3d 1233"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ex Parte Geiken",
          "cluster_id": 1755481,
          "cite": [
            "28 S.W.3d 553",
            "2000 Tex. Crim. App. LEXIS 90",
            "2000 WL 1468654"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joshua v. City of Gainesville",
          "cluster_id": 1140033,
          "cite": [
            "768 So. 2d 432",
            "25 Fla. L. Weekly Supp. 641",
            "2000 Fla. LEXIS 1751",
            "2000 WL 1227755"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Azad Haji Abdullah",
          "cluster_id": 3133306,
          "cite": [
            "158 Idaho 386",
            "348 P.3d 1",
            "2015 Ida. LEXIS 78"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aubrey v. Koppes",
          "cluster_id": 4786583,
          "cite": [
            "975 F.3d 995"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hale v. Fox",
          "cluster_id": 4239796,
          "cite": [
            "829 F.3d 1162",
            "2016 U.S. App. LEXIS 13155",
            "2016 WL 3902561"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph A. Kirschenbaum, A/K/A Ari Kirschenbaum, Appeal Of: Julie Kirschenbaum",
          "cluster_id": 758074,
          "cite": [
            "156 F.3d 784"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Xy, LLC v. Trans Ova Genetics, L.C.",
          "cluster_id": 4500454,
          "cite": [
            "890 F.3d 1282"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elliott v. Martinez",
          "cluster_id": 626933,
          "cite": [
            "675 F.3d 1241",
            "2012 U.S. App. LEXIS 7096",
            "2012 WL 1153488"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Psc Vsmpo-Avismo Corp. v. United States",
          "cluster_id": 805388,
          "cite": [
            "688 F.3d 751",
            "2012 WL 3055876",
            "34 I.T.R.D. (BNA) 1737",
            "2012 U.S. App. LEXIS 15638"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sears v. State",
          "cluster_id": 1636585,
          "cite": [
            "91 S.W.3d 451",
            "2002 Tex. App. LEXIS 8309",
            "2002 WL 31627990"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Frey Corporation v. City of Peoria, Illinois",
          "cluster_id": 2709391,
          "cite": [
            "735 F.3d 505",
            "2013 WL 4257891",
            "2013 U.S. App. LEXIS 17123"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. William Little",
          "cluster_id": 3216832,
          "cite": [
            "499 Mich. 332"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Carlin",
          "cluster_id": 2254756,
          "cite": [
            "58 Cal. Rptr. 3d 495",
            "150 Cal. App. 4th 322",
            "2007 Daily Journal DAR 5883",
            "2007 Cal. Daily Op. Serv. 4622",
            "2007 Cal. App. LEXIS 658"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roberts v. Total Health Care, Inc.",
          "cluster_id": 2070848,
          "cite": [
            "709 A.2d 142",
            "349 Md. 499",
            "1998 Md. LEXIS 313"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alisal Water Corporation Toro Water Service, Inc. North Monterey County Water Service, Inc. Moss Landing Water Service, Inc. Natholyn P. Adcock Robert T. Adcock, United States of America v. Alisal Water Corporation Toro Water Service, Inc. Robert T. Adcock North Monterey County Water Service, Inc. Moss Landing Water Service, Inc. Natholyn P. Adcock, and Patricia Adcock Bruce Pierson David M. Simcho, John W. Richardson, Receiver",
          "cluster_id": 792691,
          "cite": [
            "431 F.3d 643",
            "62 ERC (BNA) 1009",
            "2005 U.S. App. LEXIS 27271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neifert v. Department of the Environment",
          "cluster_id": 2320041,
          "cite": [
            "910 A.2d 1100",
            "395 Md. 486",
            "64 ERC (BNA) 1685",
            "2006 Md. LEXIS 754"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sullivan v. Barnett",
          "cluster_id": 752420,
          "cite": [
            "139 F.3d 158"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hardy v. State",
          "cluster_id": 2174351,
          "cite": [
            "50 S.W.3d 689",
            "2001 Tex. App. LEXIS 4458",
            "2001 WL 739242"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas Department of Public Safety v. Story",
          "cluster_id": 1880958,
          "cite": [
            "115 S.W.3d 588",
            "2003 Tex. App. LEXIS 6040",
            "2003 WL 21665542"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118163) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 98,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 98,
        "triage_read": 1,
        "triage_snippet_classified": 97
      },
      "lane2_top_cited": {
        "query": "cites:(118163)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMiZzPTI0NzUxNTEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118163%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 22,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118163)",
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
    "complete_query": "cites:(118163)",
    "indexed_citing_opinions": 125,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118163,
        "count": 125,
        "count_source": "search"
      }
    ],
    "citation_count": 220,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/lachance-v-erickson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcxNjc3NjQmcz01MzEzMzU5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118163%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118163,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 106221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 107265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 108001,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 109429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 109658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 109922,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 110267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 110331,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 111372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 111603,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 112821,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 722408,
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
    "date_created": "2026-07-05T10:42:02Z",
    "date_modified": "2026-07-06T08:11:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:42:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:42:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:46:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:42:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — LaChance v. Erickson

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b440-4">
<span citation-index="1" class="star-pagination" label="264"> 
   *264
   </span>
  CHIEF Justice Rehnquist
 </author>
<p id="AEn">
  delivered the opinion of the Court.
 </p>
<p id="b440-5">
  The question presented by this action is whether either the Due Process Clause or the Civil Service Reform Act of 1978 (CSRA), <span class="citation no-link">5 U. S. C. § 1101</span>
  <em>
   et seq.,
  </em>
  precludes a federal agency from sanctioning an employee for making false statements to the agency regarding alleged employment-related misconduct on the part of the employee. We hold that they do not.
 </p>
<p id="b440-6">
  Respondents Walsh, Erickson, Kye, Barrett, Roberts, and McManus are Government employees who were the subject of adverse actions by the various agencies for which they worked. Each employee made false statements to agency investigators with respect to the misconduct with which they were charged. In each ease, the agency additionally charged the false statement as a ground for adverse action, and the action taken in each was based in part on the added charge. The employees separately appealed the actions taken against them to the Merit Systems Protection Board (Board). The Board upheld that portion of the penalty based on the underlying charge in each case, but overturned the false statement charge. The Board further held that an employee’s false statements could not be used for purposes of impeaching the employee’s credibility, nor could they be considered in setting the appropriate punishment for the employee’s underlying misconduct. Finally, the Board held that an agency may not charge an employee with failure to report an act of fraud when reporting such fraud would tend to implicate the employee in employment-related misconduct.
 </p>
<p id="b440-7">
  The Director of the Office of Personnel Management appealed each of these decisions by the Board to the Court of Appeals for the Federal Circuit. In a consolidated appeal involving the cases of Walsh, Erickson, Kye, Barrett, and Roberts, that court agreed with the Board that no penalty could be based on a false denial of the underlying claim.
  <span citation-index="1" class="star-pagination" label="265"> 
   *265
   </span>
<em>
   King
  </em>
  v.
  <em>
   Erickson,
  </em>
  <span class="citation" data-id="722408"><a href="/opinion/722408/king-v-erickson/" aria-description="Citation for case: King v. Erickson">89 F. 3d 1575</a></span> (1996). Citing the Fifth Amendment’s Due Process Clause, the court held that “an agency may not charge an employee with falsification or a similar charge on the ground of the employee’s denial of another charge or of underlying facts relating to that other charge,” nor may “[d]enials of charges and related facts ... he considered in determining a penalty.”
  <span class="citation" data-id="722408"><a href="/opinion/722408/king-v-erickson/#1585" aria-description="Citation for case: King v. Erickson"><em>
   Id.,
  </em>
  at 1585</a></span>. In a separate unpublished decision, judgt. order reported at <span class="citation multiple-matches"><a href="/c/F.%203d/92/1208/">92 F. 3d 1208</a></span> (1996), the Court of Appeals affirmed the Board’s reversal of the false statement charge against McManus as well as the Board’s conclusion that an employee’s “false statements . . : may not be considered” even for purposes of impeachment.
  <em>
   McManus
  </em>
  v.
  <em>
   Department of Justice,
  </em>
  66 MSPR 564, 568 (1995).
 </p>
<p id="b441-5">
  We granted certiorari in both cases, <span class="citation multiple-matches"><a href="/c/U.%20S./521/1117/">521 U. S. 1117</a></span> (1997), and now reverse. In
  <em>
   Bryson
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9424114"><a href="/opinion/108001/bryson-v-united-states/" aria-description="Citation for case: Bryson v. United States">396 U. S. 64</a></span> (1969), we said: “Our legal system provides methods for challenging the Government’s right to ask questions — lying is not one of them. A citizen may decline to answer the question, or answer it honestly, but he cannot with impunity knowingly and willfully answer with a falsehood.”
  <span class="citation" data-id="9424114"><a href="/opinion/108001/bryson-v-united-states/#72" aria-description="Citation for case: Bryson v. United States"><em>
   Id.,
  </em>
  at 72</a></span> (footnote omitted). We find it impossible to square the result reached by the Court of Appeals in the present case with our holding in
  <em>
   <span class="citation" data-id="9424114"><a href="/opinion/108001/bryson-v-united-states/" aria-description="Citation for case: Bryson v. United States">Bryson</a></span>
  </em>
  and in other cases of similar import.
 </p>
<p id="b441-6">
  Title <span class="citation no-link">5 U. S. C. § 7513</span>(a) provides that an agency may impose the sort of penalties involved here “for such eause as will promote the efficiency of the service.” It then sets forth four procedural rights accorded to the employee against whom adverse action is proposed. The agency must:
 </p>
<blockquote id="b441-7">
  (1) give the employee “at least 30 days’ advance written notice”; (2) allow the employee “a reasonable time, but not less than 7 days, to answer orally and in writing and to furnish . . . evidence in support of the answer”; (3) permit the employee to “be represented by an attorney or other representative”; and (4) provide the employee ,
  <span citation-index="1" class="star-pagination" label="266"> 
   *266
   </span>
  with “a written decision and the specific reasons therefor.” <span class="citation no-link">5 U. S. C. § 7513</span>(b).
 </blockquote>
<p id="b442-5">
  In these carefully delineated rights there is no hint of any right to “put the government to its proof” by falsely denying the charged conduct. Such a right, then, if it exists at all, must come from the Fifth Amendment of the United States Constitution.
 </p>
<p id="b442-6">
  The Fifth Amendment be deprived of life, liberty, or property, without due process of law . . . .” The Court of Appeals stated that “it is undisputed that the government employees here had a protected property interest in their employment,” <span class="citation" data-id="722408"><a href="/opinion/722408/king-v-erickson/#1581" aria-description="Citation for case: King v. Erickson">89 F. 3d, at 1581</a></span>, and we assume that to be the ease for purposes of our decision.
 </p>
<p id="b442-7">
  The core of due process is ingful opportunity to be heard.
  <em>
   Cleveland Bd. of Ed.
  </em>
  v.
  <em>
   Loudermill,
  </em>
  <span class="citation" data-id="9429945"><a href="/opinion/111372/cleveland-board-of-education-v-loudermill/#542" aria-description="Citation for case: Cleveland Board of Education v. Loudermill">470 U. S. 532, 542</a></span> (1985). But we reject, on the basis of both precedent and principle, the view expressed by the Court of Appeals in this action that a “meaningful opportunity to be heard” includes a right to make false statements with respect to the charged conduct.
 </p>
<p id="b442-8">
  It is well established that a testify does not include the light to commit perjury.
  <em>
   Nix
  </em>
  v.
  <em>
   Whiteside,
  </em>
  <span class="citation" data-id="9430360"><a href="/opinion/111603/nix-v-whiteside/#173" aria-description="Citation for case: Nix v. Whiteside">475 U. S. 157, 173</a></span> (1986);
  <em>
   United States
  </em>
  v.
  <em>
   Havens,
  </em>
  <span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#626" aria-description="Citation for case: United States v. Havens">446 U. S. 620, 626</a></span> (1980);
  <em>
   United States
  </em>
  v.
  <em>
   Grayson,
  </em>
  <span class="citation" data-id="9427313"><a href="/opinion/109922/united-states-v-grayson/#54" aria-description="Citation for case: United States v. Grayson">438 U. S. 41, 54</a></span> (1978). Indeed, in
  <em>
   United States
  </em>
  v.
  <em>
   Dunnigan,
  </em>
  <span class="citation" data-id="112821"><a href="/opinion/112821/united-states-v-dunnigan/#97" aria-description="Citation for case: United States v. Dunnigan">507 U. S. 87, 97</a></span> (1993), we held that a court could, consistent with the Constitution, enhance a criminal defendant’s sentence based on a finding that he perjured himself at trial.
 </p>
<p id="b442-9">
  Witnesses appearing before a grand jury under oath are likewise required to testify truthfully, on pain of being prosecuted for perjury.
  <em>
   United States
  </em>
  v.
  <em>
   Wong,
  </em>
  <span class="citation" data-id="109658"><a href="/opinion/109658/united-states-v-wong/" aria-description="Citation for case: United States v. Wong">431 U. S. 174</a></span> (1977). There we said that “the predicament of being forced to choose between incriminatory truth and falsehood... does not justify perjury.”
  <span class="citation" data-id="109658"><a href="/opinion/109658/united-states-v-wong/#178" aria-description="Citation for case: United States v. Wong"><em>
   Id.,
  </em>
  at 178</a></span>. Similarly, one who files a
  <span citation-index="1" class="star-pagination" label="267"> 
   *267
   </span>
  false affidavit required by statute may be fined and imprisoned.
  <em>
   Dennis
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9423265"><a href="/opinion/107265/dennis-v-united-states/" aria-description="Citation for case: Dennis v. United States">384 U. S. 855</a></span> (1966).
 </p>
<p id="b443-5">
  The Court of Appeals sought to distinguish these eases on the ground that the defendants in them had been under oath, while here the respondents were not. The fact that respondents were not under oath, of course, negates a charge of perjury, but that is not the charge brought against them. They were charged with making false statements during the course of an agency investigation, a charge that does not require that the statements be made under oath. While the Court of Appeals would apparently permit the imposition of punishment for the former but not the latter, we fail to see how the presence or absence of an oath is material to the due process inquiry.
 </p>
<p id="b443-6">
  The Court of Appeals also relied on its fear that if employees were not allowed to make false statements, they might “be coerced into admitting the misconduct, whether they believe that they are guilty or not, in order to avoid the more severe penalty of removal possibly resulting from a falsification charge.” App. to Pet. for Cert. 16a-17a. But we rejected a similar claim in
  <em>
   United States
  </em>
  v.
  <em>
   Grayson,
  </em>
  <span class="citation" data-id="9427313"><a href="/opinion/109922/united-states-v-grayson/" aria-description="Citation for case: United States v. Grayson">438 U. S. 41</a></span> (1978). There a sentencing judge took into consideration his belief that the defendant had testified falsely at his trial. The defendant argued before us that such a practice would inhibit the exercise of the right to testify truthfully in the proceeding. We described that contention as “entirely frivolous.”
  <span class="citation" data-id="9427313"><a href="/opinion/109922/united-states-v-grayson/#55" aria-description="Citation for case: United States v. Grayson"><em>
   Id.,
  </em>
  at 55</a></span>.
 </p>
<p id="b443-7">
  If answering an agency’s investigatory question could expose an employee to a criminal prosecution, he may exercise his Fifth Amendment right to remain silent. See
  <em>
   Hale
  </em>
  v.
  <em>
   Henkel,
  </em>
  <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#67" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 67</a></span> (1906);
  <em>
   United States
  </em>
  v.
  <em>
   Ward,
  </em>
  <span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/#248" aria-description="Citation for case: United States v. Ward">448 U. S. 242, 248</a></span> (1980). It may well be that an agency, in ascertaining the truth or falsity of the charge, would take into consideration the failure of the employee to respond. See
  <em>
   Baxter
  </em>
  v.
  <em>
   Palmigiano,
  </em>
  <span class="citation" data-id="9426363"><a href="/opinion/109429/baxter-v-palmigiano/#318" aria-description="Citation for case: Baxter v. Palmigiano">425 U. S. 308, 318</a></span> (1976) (discussing the “prevailing rule that the Fifth Amendment does not for
  <span citation-index="1" class="star-pagination" label="268"> 
   *268
   </span>
  bid adverse inferences against parties to civil actions when they refuse to testify”). But there is nothing inherently irrational about such an investigative posture. See
  <em>
   Konigsberg
  </em>
  v.
  <em>
   State Bar of Cal.,
  </em>
  <span class="citation" data-id="9422190"><a href="/opinion/106221/konigsberg-v-state-bar-of-cal/" aria-description="Citation for case: Konigsberg v. State Bar of Cal.">366 U. S. 36</a></span> (1961).
 </p>
<p id="b444-5">
  For these reasons, we hold that a Government agency may take adverse action against an employee because the employee made false statements in response to an underlying charge of misconduct. The judgments of the Court of Appeals are therefore
 </p>
<p id="b444-6">
<em>
   Reversed.
  </em>
</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/LaDuke v. Nelson.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: LaDuke v. Nelson
type: case
citation: "762 F.2d 1318 (1985)"
parallel_cite: 53 U.S.L.W. 2625
neutral_cite: 1985 U.S. App. LEXIS 19963
court: 9th Cir.
court_level: coa
circuit: ca9
year: 1985
date_decided: 1985-06-10
docket: 83-3608
authority_weight: "Binding in-circuit — 9th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/452994/charles-laduke-v-alan-c-nelson-etc/"
  cluster_id: 452994
  opinion_id: null
  identity_checked: true
lake:
  record_id: LaDuke v. Nelson
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Tents]]"
    role: Key
related:
  - "[[Tents]]"
tags:
  - case
  - fourth-amendment
  - curtilage
  - dwelling
  - migrant-housing
  - warrantless-entry
  - injunction
holding: "Migrant farmworkers' dwellings retain their occupants' reasonable expectations of privacy, so the INS may not conduct warrantless 'area control' entries of farm housing to search or arrest absent consent or probable cause; the Ninth Circuit affirmed a class injunction barring the practice as a Fourth Amendment violation."
---

# LaDuke v. Nelson

*762 F.2d 1318 (9th Cir. 1985)* (No. 83-3608) · U.S. Court of Appeals for the Ninth Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 452994 → opinion 452994 (762 F.2d 1318, decided 1985-06-10); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
A class of migrant and seasonal farmworkers in Washington's Spokane Sector challenged the Immigration and Naturalization Service's "area control operations" — sweeps in which agents entered farm labor camps and the workers' dwellings, and stopped and interrogated residents, without warrants or individualized suspicion. The district court found the practices unconstitutional and issued a class-wide injunction; the INS appealed, contesting standing, the seizure findings, and the scope of the injunction.

## Issue
Whether the INS's warrantless entries into migrant farmworker dwellings and its suspicionless detentive stops of residents violate the Fourth Amendment, and whether the district court's injunction was proper.

## Rule
The Ninth Circuit affirmed. It held that the humble, often temporary dwellings of migrant farmworkers are fully protected by the Fourth Amendment and that the injunction's first component — barring warrantless entries of farm dwellings to search or arrest absent clear consent or probable cause — was sound: "we think the plain language of the first component provides ample flexibility for INS searches while preserving class members' reasonable expectations of privacy." — 762 F.2d at 1331. The court agreed that the INS "farm checks, as described by the witnesses, run afoul of the Fourth Amendment." — *Id.* at 1332.

## Application
The injunction had three parts: no warrantless entries of farm dwellings to search or arrest absent consent or probable cause; no warrantless arrests or searches of residents without probable cause; and no detentive stops without articulable suspicion of both alienage and unlawful presence. The court sustained each, rejecting the INS's overbreadth arguments and stressing that the modest character of migrant housing does not diminish its occupants' constitutional protection; the injunction still left ample room for consensual encounters and legitimate, warrant-based enforcement.

## Conclusion
The judgment and injunction were **affirmed** (with a modification to the fee award); the INS's area-control entries and suspicionless stops violated the Fourth Amendment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *LaDuke* stands for the proposition that a dwelling's protection does not depend on its permanence or grandeur: temporary and makeshift homes — farmworker cabins, shacks, and tents — remain within the Fourth Amendment's shelter against warrantless government entry.

## Appears on
- [[Tents]] — *Key*

## Sources
- [*LaDuke v. Nelson*, 762 F.2d 1318 (9th Cir. 1985)](https://www.courtlistener.com/opinion/452994/charles-laduke-v-alan-c-nelson-etc/) — pinpoint: 1331–1332 (holding on warrantless farm-dwelling entries and the affirmed injunction); Rule quotes string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9a8f07dbaddeb1ae", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "LaDuke v. Nelson"}, "payload": {"all": [{"cite": "762 F.2d 1318", "page": "1318", "reporter": "F.2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "762"}, {"cite": "1985 U.S. App. LEXIS 19963", "page": "19963", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1985"}, {"cite": "53 U.S.L.W. 2625", "page": "2625", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "53"}], "display": "762 F.2d 1318", "official": {"cite": "762 F.2d 1318", "page": "1318", "reporter": "F.2d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "762"}, "official_selection_present": true, "record_id": "LaDuke v. Nelson"}}
{"assertion_id": "a81ac6385d6ebbb8", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "LaDuke v. Nelson"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "LaDuke v. Nelson", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — LaDuke v. Nelson

```json
{
  "schema_version": "s2.v1",
  "record_id": "LaDuke v. Nelson",
  "status": "under_review",
  "identity": {
    "case_name": "Charles Laduke v. Alan C. Nelson, Etc.",
    "case_name_short": "",
    "case_name_full": "Charles LaDUKE, Et Al., Plaintiffs/Appellees, v. Alan C. NELSON, Etc., Et Al., Defendants/Appellants",
    "input_case_name": "LaDuke v. Nelson",
    "court": "9th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": "1985-06-10",
    "year": 1985,
    "docket": "83-3608",
    "cluster_id": 452994,
    "lead_opinion_id": 452994,
    "sibling_ids": [],
    "absolute_url": "/opinion/452994/charles-laduke-v-alan-c-nelson-etc/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "762 F.2d 1318",
      "volume": "762",
      "reporter": "F.2d",
      "page": "1318",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "53 U.S.L.W. 2625",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "2625",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. App. LEXIS 19963",
        "volume": "1985",
        "reporter": "U.S. App. LEXIS",
        "page": "19963",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "762 F.2d 1318",
        "volume": "762",
        "reporter": "F.2d",
        "page": "1318",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. App. LEXIS 19963",
        "volume": "1985",
        "reporter": "U.S. App. LEXIS",
        "page": "19963",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 2625",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "2625",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "762 F.2d 1318",
    "official_selection": {
      "court_class": "coa",
      "selected": "762 F.2d 1318",
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
    "date_created": "2026-07-07T01:37:21Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:37:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:37:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:37:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:37:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "laduke-v-nelson--452994",
      "to_record_id": "LaDuke v. Nelson",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — LaDuke v. Nelson

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b1417-10">
  FERGUSON, Circuit Judge:
 </author>
<p id="b1417-11">
  The Immigration and Naturalization Service (“INS”) appeals from an injunction issued by the district court prohibiting the INS from conducting farm and ranch checks of migrant farm housing without a warrant, probable cause, or articulable suspicion.
  <em>
   See LaDuke v. Nelson,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. 158</a></span> (E.D.Wash.1982). The INS also appeals the award of fees under the Equal Access to Justice Act. We affirm.
 </p>
<p id="b1417-12">
  I.
 </p>
<p id="b1417-13">
  The plaintiffs, residents of migrant farm dwellings in the INS region known as the Spokane Sector, covering the states of Washington, Idaho and Montana, brought suit in 1977 alleging that the defendant’s practice of initiating and executing searches of migrant farm housing violated their Fourth Amendment rights. The district court certified the plaintiffs as a class in 1979 under Federal Rule of Civil Procedure 23(b)(2). In 1981 the district court refined the plaintiff class to include all persons who have resided or will reside in particularly described farm housing within the Sector.
 </p>
<p id="b1417-14">
  The district court found that the INS engaged in a “standard pattern” of searches within farm labor housing communities in the Sector. The court found that the INS initiated these warrantless searches without articulable suspicion or probable cause.
  <em>
   LaDuke,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/#161" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 161</a></span>;
  <em>
   see
  </em>
  note 12
  <em>
   infra.
  </em>
  The armed Border Patrol agents periodically cordoned off migrant housing during early morning or late evening hours, surrounded the residences in emergency vehicles with flashing lights, approached the homes with flashlights, and stationed officers at all doors and windows. The agents would then conduct house-to-house searches either without consent or with the alleged “knowing” consent of the occupants.
 </p>
<p id="b1417-15">
  The district court found that under these circumstances the occupants were not free to leave and, consequently, a seizure had taken place. The court further found that any consent obtained was involuntary given the substantial show of official force. The court also found that the seizures took place without probable cause, reasonable belief, or articulable suspicion that illegal aliens were present. The court enjoined the defendants and those acting in concert with them from engaging in similar unconstitutional farm check practices.
 </p>
<p id="b1417-16">
  II.
 </p>
<p id="b1417-17">
  The standard of review over the district court’s grant of a permanent injunction must, of course, be segmented according to the component functions performed by the district court.
  <em>
   See United States v. McConney,
  </em>
  <span class="citation" data-id="9471865"><a href="/opinion/431931/united-states-v-winston-bryant-mcconney/" aria-description="Citation for case: United States v. Winston Bryant McConney">728 F.2d 1195</a></span> (9th Cir.) (en banc),
  <em>
   cert. denied,
  </em>
  — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./105/101/">105 S.Ct. 101</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/83/46/">83 L.Ed.2d 46</a></span> (1984). Accordingly, the district court’s findings of fact are reviewed under the clearly erroneous standard. Fed.R.Civ.P. 52(a). A district court’s findings on the voluntariness of consent to search are reviewed under the clearly erroneous standard.
  <em>
   United States v. Caicedo-Guarnizo,
  </em>
  <span class="citation" data-id="429241"><a href="/opinion/429241/united-states-v-jose-orlando-caicedo-guarnizo/#1423" aria-description="Citation for case: United States v. Jose Orlando Caicedo-Guarnizo">723 F.2d 1420, 1423</a></span> (9th Cir.1984). The district court’s
  <span citation-index="1" class="star-pagination" label="1322"> 
   *1322
   </span>
  finding that the ranch checks are not based on articulable suspicion is also reviewed under the clearly erroneous standard.
  <em>
   United States v. Garcia-Nunez,
  </em>
  <span class="citation" data-id="9470736"><a href="/opinion/419810/united-states-v-agustin-garcia-nunez-united-states-of-america-v-charles/#561" aria-description="Citation for case: United States v. Agustin Garcia-Nunez, United States of...">709 F.2d 559, 561</a></span> (9th Cir.1983).
  <em>
   Cf. United States v. Cortez,
  </em>
  <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#416" aria-description="Citation for case: United States v. Cortez">449 U.S. 411, 416</a></span>, <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#694" aria-description="Citation for case: United States v. Cortez">101 S.Ct. 690, 694</a></span>, <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">66 L.Ed.2d 621</a></span> (1981).
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  Because the court’s jurisdiction is dependent on Article III standing, this issue is subject to de novo review. Finally, the district court’s determinations on questions of law and on mixed questions of facts and law implicating constitutional rights are reviewed de novo.
  <em>
   United States v. McConney,
  </em>
  <span class="citation" data-id="9471865"><a href="/opinion/431931/united-states-v-winston-bryant-mcconney/#1203" aria-description="Citation for case: United States v. Winston Bryant McConney">728 F.2d at 1203</a></span>.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b1418-4">
  III.
 </p>
<p id="b1418-5">
  This opinion will focus on the major arguments
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  raised by the INS in the following sequence:
 </p>
<blockquote id="b1418-6">
  (A) Do the plaintiffs have Article III standing to seek an injunction?
 </blockquote>
<blockquote id="b1418-10">
  (B) Did the district court err in its decision on the merits of plaintiffs’ Fourth Amendment claim?
 </blockquote>
<blockquote id="b1418-11">
  (C) Did the district court err in finding the essential prerequisites for an injunction met and, if not, is the issued injunction overbroad?
 </blockquote>
<blockquote id="b1418-12">
  (D) Was the class properly certified under Fed.R.Civ.P. 23(b)(2)?
 </blockquote>
<blockquote id="b1418-13">
  (E) Was the award of attorney fees and costs appropriate under the Equal Access to Justice Act?
 </blockquote>
<p id="b1418-14">
  A.
 </p>
<p id="b1418-15">
  The INS has challenged the plaintiffs’ standing to bring suit for injunctive relief under Article III of the Constitution. The “case or controversy” standing requirement serves to limit federal jurisdiction to those cases in which an adversarial
  <span citation-index="1" class="star-pagination" label="1323"> 
   *1323
   </span>
  setting is guaranteed by the parties’ “personal stake” in the outcome of the litigation.
  <em>
   Warth v. Seldin,
  </em>
  <span class="citation" data-id="9426170"><a href="/opinion/109301/warth-v-seldin/#498" aria-description="Citation for case: Warth v. Seldin">422 U.S. 490, 498</a></span>, <span class="citation" data-id="9426170"><a href="/opinion/109301/warth-v-seldin/#2204" aria-description="Citation for case: Warth v. Seldin">95 S.Ct. 2197, 2204</a></span>, <span class="citation" data-id="9426170"><a href="/opinion/109301/warth-v-seldin/" aria-description="Citation for case: Warth v. Seldin">45 L.Ed.2d 343</a></span> (1975). The Supreme Court has also extended the standing inquiry beyond this Article III based minimum to include judicially imposed “prudential limitations” on the appropriate exercise of federal judicial power.
  <em>
   Allen v. Wright,
  </em>
  — U.S. -, <span class="citation" data-id="9429754"><a href="/opinion/111258/allen-v-wright/#3324" aria-description="Citation for case: Allen v. Wright">104 S.Ct. 3315, 3324-25</a></span>, <span class="citation" data-id="9429754"><a href="/opinion/111258/allen-v-wright/" aria-description="Citation for case: Allen v. Wright">82 L.Ed.2d 556</a></span> (1984);
  <em>
   Warth v. Seldin,
  </em>
  <span class="citation" data-id="9426170"><a href="/opinion/109301/warth-v-seldin/#499" aria-description="Citation for case: Warth v. Seldin">422 U.S. at 499-500</a></span>, <span class="citation" data-id="9426170"><a href="/opinion/109301/warth-v-seldin/#2205" aria-description="Citation for case: Warth v. Seldin">95 S.Ct. at 2205</a></span>. The “irreducible minimum” demanded of a proper plaintiff by Article Ill’s constitutional demands, however, requires that a plaintiff show he has “personally ... suffered some actual or threatened injury as a result of the putatively illegal conduct of the defendant,” that can be “fairly” traced to the defendant’s challenged conduct, and which “is likely to be redressed by a favorable decision.”
  <em>
   Valley Forge Christian College v. Americans United for Separation of Church and State, Inc.,
  </em>
  <span class="citation" data-id="9428574"><a href="/opinion/110599/valley-forge-christian-college-v-americans-united-for-separation-of-church/#472" aria-description="Citation for case: Valley Forge Christian College v. Americans United for...">454 U.S. 464, 472</a></span>,<span class="citation" data-id="9428574"><a href="/opinion/110599/valley-forge-christian-college-v-americans-united-for-separation-of-church/#758" aria-description="Citation for case: Valley Forge Christian College v. Americans United for...">102 S.Ct. 752, 758</a></span>, <span class="citation" data-id="9428574"><a href="/opinion/110599/valley-forge-christian-college-v-americans-united-for-separation-of-church/" aria-description="Citation for case: Valley Forge Christian College v. Americans United for...">70 L.Ed.2d 700</a></span> (1982).
 </p>
<p id="b1419-7">
  Added to this core constitutional standing test are judicially created prudential limitations, including: a general prohibition on “raising another person’s legal rights”,
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  a preference for the resolution of “generalized grievances” in the representative branches,
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  and the “requirement that a plaintiff’s complaint fall within the zone of interests protected” by the pertinent law.
  <em>
   Allen v. Wright,
  </em>
  — U.S. -, <span class="citation" data-id="9429754"><a href="/opinion/111258/allen-v-wright/#3324" aria-description="Citation for case: Allen v. Wright">104 S.Ct. 3315, 3324-25</a></span>, <span class="citation" data-id="9429754"><a href="/opinion/111258/allen-v-wright/" aria-description="Citation for case: Allen v. Wright">82 L.Ed.2d 556</a></span> (1984). Finally, the Supreme Court has indicated that, at least when injunctive relief is sought, litigants must adduce a “credible threat” of recurrent injury.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
<em>
   Kolender v. Lawson,
  </em>
  <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">461 U.S. 352</a></span>, <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">103 S.Ct. 1855</a></span>, 1857 n. 3, <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">75 L.Ed.2d 903</a></span> (1983);
  <em>
   Los Angeles v. Lyons,
  </em>
  <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">461 U.S. 95</a></span>, <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">103 S.Ct. 1660</a></span>, <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">75 L.Ed.2d 675</a></span> (1983). We first address the significance of
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  to plaintiffs’ standing to seek injunctive relief.
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
</p>
<p id="b1419-13">
  In
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>,
  </em>
  the plaintiff brought suit under <span class="citation no-link">42 U.S.C. § 1983</span> for damages and declaratory and injunctive relief against the City of Los Angeles and four of its police officers. The plaintiff had previously been subjected to an allegedly unprovoked and unjustified “chokehold” by a police officer in the course of a routine stop for a traffic violation. The Supreme Court reversed the Ninth Circuit’s affirmance of a preliminary injunction in three discrete holdings. First, the Court held that Lyons lacked standing under the case or controversy clause of Article III to seek injunctive relief and consequently the lower courts lacked jurisdiction over his injunctive claim.
  <span class="citation no-link"><em>
   Id.
  </em>
  at 101</span>, 103 S.Ct. at 1664. Second, the Court held that the plaintiff had not met the standards for issuance of injunctive relief.
  <em>
   Id.
  </em>
  at 109, 103 S.Ct. at 1668. Third, the Court held that the jurisprudential concerns of “equity, comity, and federalism” sharply constrict federal judicial oversight of “state law enforcement authorities,”
  <em>
   id.
  </em>
<span citation-index="1" class="star-pagination" label="1324"> 
   *1324
   </span>
  at 112, 103 S.Ct. at 1670, thereby making injunctive relief inappropriate.
 </p>
<p id="b1420-4">
  As the Supreme Court summarized: “Lyons’ standing to seek the injunction requested depended on whether he was likely to suffer future injury from the use of the chokeholds by police officers.” 461 U.S. at 105, 103 S.Ct. at 1667. Relying heavily on
  <em>
   O’Shea v. Littleton,
  </em>
  <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">414 U.S. 488</a></span>, <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">94 S.Ct. 669</a></span>, <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">38 L.Ed.2d 674</a></span> (1974) and
  <em>
   Rizzo v. Goode,
  </em>
  <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">423 U.S. 362</a></span>, <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">96 S.Ct. 598</a></span>, <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">46 L.Ed.2d 561</a></span> (1976), the Court held that Lyons did not face “a real and immediate threat of again being illegally choked.”
  <em>
   Id.
  </em>
  461 U.S. at 110, 103 S.Ct. at 1669. Finding the plaintiff’s allegation of future injury speculative,
  <em>
   id.
  </em>
  at 108, 103 S.Ct. at 1668, Court held that the objective “reality of the threat of repeated injury,”
  <em>
   id.
  </em>
  at 107 n. 8, 103 S.Ct. at 1668 n. 8, was beyond reasonable belief given the remote probability that Lyons would once again violate the law and incite an unjustifiable response by Los Angeles police. Finally, the Court found probative the fact that the district court had made “no finding that Lyons faced a real and immediate threat of again being illegally choked.”
  <em>
   Id.
  </em>
  at 110, 103 S.Ct. at 1669.
 </p>
<p id="b1420-5">
  At a minimum,
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  requires that the “personal stake” showing necessary under Article III in cases involving injunctive relief includes an essential showing of the likelihood of similar injury in the future. At least for Lyons, past injury was insufficient, standing alone, to afford him a “personal stake” in the prospective relief provided by an injunction.
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
  Four fundamental differences between
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  and this case demonstrate why the plaintiff class has a sufficient “personal stake” under Article III to warrant the prospective relief only an injunction can provide.
 </p>
<p id="b1420-6">
  The first difference between
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  and this case lies in the respective district court findings on the likelihood of recurrent injury. The district court in
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  made no finding of likely recurrence,
  <em>
   Lyons,
  </em>
  <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">461 U.S. at 110</a></span> n. 9, 103 S.Ct. at 1669 n. 9, while the district court in this case made a specific finding of likely recurrence.
  <em>
   LaDuke,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/#164" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 164</a></span>. Second, the district court in this case explicitly found that the defendants engaged in a standard pattern of officially sanctioned officer behavior, <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/#160" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 160</a></span>, violative of the plaintiffs’ constitutional rights. Conversely, the
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  opinion expressly noted the absence of any written or oral pronouncements by the Los Angeles Police Department sanctioning the unjustifiable application of the chokehold and pointed to the absence of "any [record] evidence showing a pattern of police behavior” suggestive of an unconstitutional application of the chokehold.
  <em>
   Id.
  </em>
  461 U.S. at 110 n. 9, 103 S.Ct. at 1669 n. 9. The Supreme Court has repeatedly upheld the appropriateness of federal injunctive relief to combat a “pattern” of illicit law enforcement behavior.
  <em>
   See Allee v. Medrano,
  </em>
  <span class="citation" data-id="9425720"><a href="/opinion/109031/allee-v-medrano/#812" aria-description="Citation for case: Allee v. Medrano">416 U.S. 802, 812</a></span>, <span class="citation" data-id="9425720"><a href="/opinion/109031/allee-v-medrano/#2198" aria-description="Citation for case: Allee v. Medrano">94 S.Ct. 2191, 2198</a></span>, <span class="citation" data-id="9425720"><a href="/opinion/109031/allee-v-medrano/" aria-description="Citation for case: Allee v. Medrano">40 L.Ed.2d 566</a></span> (1974);
  <em>
   Hague v. CIO,
  </em>
  <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">307 U.S. 496</a></span>, <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">59 S.Ct. 954</a></span>, <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">83 L.Ed. 1423</a></span> (1939);
  <em>
   see also INS v. Delgado,
  </em>
  — U.S. -, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">104 S.Ct. 1758</a></span>, 1763 n. 4, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">80 L.Ed.2d 247</a></span> (1984);
  <em>
   Rizzo v. Goode,
  </em>
  <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/#375" aria-description="Citation for case: Rizzo v. Goode">423 U.S. 362, 375</a></span>, <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/#606" aria-description="Citation for case: Rizzo v. Goode">96 S.Ct. 598, 606</a></span>, <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">46 L.Ed.2d 561</a></span> (1976) (distinguishing
  <em>
   Allee
  </em>
  and
  <em>
   Hague
  </em>
  as involving patterns of misbehavior, not isolated incidents).
 </p>
<p id="b1420-13">
  A third distinguishing feature that separates the present case from
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  is the absence of the prudential limitations circumscribing federal court intervention in state law enforcement matters.
  <em>
   Lyons, Rizzo,
  </em>
  and
  <em>
   <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">O’Shea</a></span>
  </em>
  all involved attempts by plaintiffs to entangle federal courts in the operations of state law enforcement and criminal justice institutions.
  <em>
   See City of Los Angeles v. Lyons,
  </em>
  <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">461 U.S. 95</a></span>, <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">103 S.Ct. 1660</a></span>, <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">75 L.Ed.2d 675</a></span> (1983) (city law enforcement practices);
  <em>
   Rizzo v. Goode,
  </em>
  <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">423 U.S. 362</a></span>, <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">96 S.Ct. 598</a></span>, <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">46 L.Ed.2d 561</a></span> (1976) (same);
  <em>
   O’Shea v. Littleton,
  </em>
  <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">414 U.S. 488</a></span>, <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">94 S.Ct. 669</a></span>, <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">38 L.Ed.2d 674</a></span> (1974) (county criminal justice system).
  <span citation-index="1" class="star-pagination" label="1325"> 
   *1325
   </span>
  Obviously, none of the considerations inherent in the judicial concept of “Our Federalism,”
  <em>
   Younger v. Harris,
  </em>
  <span class="citation" data-id="9424435"><a href="/opinion/108263/younger-v-harris/#44" aria-description="Citation for case: Younger v. Harris">401 U.S. 37, 44</a></span>, <span class="citation" data-id="9424435"><a href="/opinion/108263/younger-v-harris/#751" aria-description="Citation for case: Younger v. Harris">91 S.Ct. 746, 751</a></span>, <span class="citation" data-id="9424435"><a href="/opinion/108263/younger-v-harris/" aria-description="Citation for case: Younger v. Harris">27 L.Ed.2d 669</a></span> (1971), are implicated in constitutional challenges to executive branch behavior in federal courts. This court cannot rely on a state judiciary to correct the unconstitutional practices of federal officials.
  <em>
   Cf Los Angeles v. Lyons,
  </em>
  461 U.S. at 113, <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/#1671" aria-description="Citation for case: City of Los Angeles v. Lyons">103 S.Ct. at 1671</a></span> (comity counsels in favor of permitting state judiciary systems to oversee state law enforcement practices). Accordingly, the comity considerations which influenced the Supreme Court’s decisions in
  <em>
   O’Shea, Rizzo
  </em>
  and
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  are inapplicable in this case.
 </p>
<p id="b1421-5">
  Enforcement of the nation’s immigration laws has been delegated by Congress to the Executive Branch.
  <em>
   See United States v. Valenzuela-Bernal,
  </em>
  <span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/#864" aria-description="Citation for case: United States v. Valenzuela-Bernal">458 U.S. 858, 864</a></span>, <span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/#3444" aria-description="Citation for case: United States v. Valenzuela-Bernal">102 S.Ct. 3440, 3444</a></span>, <span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/" aria-description="Citation for case: United States v. Valenzuela-Bernal">73 L.Ed.2d 1193</a></span> (1982). Nonetheless, the federal judiciary has been vested with the ultimate authority to determine the constitutionality of the actions of the other branches of the federal government.
  <a class="footnote" href="#fn9" id="fn9_ref">
   9
  </a>
  While the co-equal branches of the federal government are entitled to “the widest latitude in the dispatch of [their] own internal affairs,”
  <em>
   Rizzo,
  </em>
  <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/#379" aria-description="Citation for case: Rizzo v. Goode">423 U.S. at 379</a></span>, <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">96 S.Ct. at 608</a></span> (quoting
  <em>
   Cafeteria Workers v. McElroy,
  </em>
  <span class="citation" data-id="9422292"><a href="/opinion/106290/cafeteria-restaurant-workers-union-local-473-v-mcelroy/" aria-description="Citation for case: Cafeteria &amp; Restaurant Workers Union, Local 473 v. McElroy">367 U.S. 886</a></span>, <span class="citation" data-id="9422292"><a href="/opinion/106290/cafeteria-restaurant-workers-union-local-473-v-mcelroy/" aria-description="Citation for case: Cafeteria &amp; Restaurant Workers Union, Local 473 v. McElroy">81 S.Ct. 1743</a></span>, <span class="citation" data-id="9422292"><a href="/opinion/106290/cafeteria-restaurant-workers-union-local-473-v-mcelroy/" aria-description="Citation for case: Cafeteria &amp; Restaurant Workers Union, Local 473 v. McElroy">6 L.Ed.2d 1230</a></span> (1961)), the executive branch has no discretion with which to violate constitutional rights.
  <em>
   Accord Illinois Migrant Council v. Pilliod,
  </em>
  <span class="citation" data-id="9463025"><a href="/opinion/338582/illinois-migrant-council-etc-v-alva-l-pilliod-etc/#1068" aria-description="Citation for case: Illinois Migrant Council, Etc. v. Alva L. Pilliod, Etc.">540 F.2d 1062, 1068</a></span> (7th Cir.1976),
  <em>
   modified en banc,
  </em>
  <span class="citation" data-id="342479"><a href="/opinion/342479/illinois-migrant-council-etc-v-alva-l-pilliod-etc/" aria-description="Citation for case: Illinois Migrant Council, Etc. v. Alva L. Pilliod, Etc.">548 F.2d 715</a></span> (1977).
 </p>
<p id="b1421-6">
  The fourth and final feature which distinguishes this case from
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  and O’Shea
  <a class="footnote" href="#fn10" id="fn10_ref">
   10
  </a>
  is the fact that the plaintiffs constitute a certified class under Federal Rule of Civil Procedure 23(b)(2). For standing purposes, this court’s inquiry must focus on the standing of the
  <em>
   class
  </em>
  to seek equitable relief.
  <em>
   See Sosna v. Iowa,
  </em>
  <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/#399" aria-description="Citation for case: Sosna v. Iowa">419 U.S. 393, 399</a></span>, <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/#557" aria-description="Citation for case: Sosna v. Iowa">95 S.Ct. 553, 557</a></span>, <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/" aria-description="Citation for case: Sosna v. Iowa">42 L.Ed.2d 532</a></span> (1975) ("When the District Court certified the propriety of the class action, the class of unnamed persons described in the certification acquired a legal status separate from the interest asserted by appellant.”). Standing, however, is a jurisdictional element that must be satisfied prior to class certification. While the fact of certification will preserve a class’s standing even after the named individual representatives have lost the required “personal stake,”
  <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/#399" aria-description="Citation for case: Sosna v. Iowa"><em>
   see id.
  </em>
  at 399</a></span>, 95 S.Ct. at 557, certification is not sufficient in itself to bestow standing, on individuals or a class who lacked the requisite personal stake at the outset. The Supreme Court has held that, under the analogous doctrine of mootness, the “personal-stake requirement relating] to the first purpose of the ease-or-controversy doctrine” is met in class actions simply by class certification notwithstanding the subsequent loss of a “personal stake” by the class representative.
  <em>
   United States Parole Commission v. Geraghty,
  </em>
  <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#400" aria-description="Citation for case: United States Parole Commission v. Geraghty">445 U.S. 388, 400</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#1210" aria-description="Citation for case: United States Parole Commission v. Geraghty">100 S.Ct. 1202, 1210</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/" aria-description="Citation for case: United States Parole Commission v. Geraghty">63 L.Ed.2d 479</a></span> (1980). The
  <em>
   <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/" aria-description="Citation for case: United States Parole Commission v. Geraghty">Geraghty</a></span>
  </em>
  court, noting it was following precedent which had eroded the “strict, formalistic perception of Article III,”
  <em>
   <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/" aria-description="Citation for case: United States Parole Commission v. Geraghty">id.</a></span>
  </em>
  at 404 n. 11, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/" aria-description="Citation for case: United States Parole Commission v. Geraghty">100 S.Ct. at 1213</a></span> n. 11, applied a “flexible” approach in concluding the personal stake necessary to satisfy Article Ill’s case or controversy requirement is satisfied by the class representative’s cognizable interest in the certification decision.
  <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#404" aria-description="Citation for case: United States Parole Commission v. Geraghty"><em>
   Id.
  </em>
  at 404</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#1212" aria-description="Citation for case: United States Parole Commission v. Geraghty">100 S.Ct. at 1212</a></span>. This “personal stake” in the certification decision survives the mootness of the named plaintiffs’ claims.
  <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#403" aria-description="Citation for case: United States Parole Commission v. Geraghty"><em>
   Id.
  </em>
  at 403</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#1212" aria-description="Citation for case: United States Parole Commission v. Geraghty">100 S.Ct. at 1212</a></span>.
 </p>
<p id="b1422-3">
<span citation-index="1" class="star-pagination" label="1326"> 
   *1326
   </span>
  Although mootness and standing are separate justiciability requirements, they share the component of a necessary “personal interest” in the outcome of the litigation.
  <em>
   See Geraghty,
  </em>
  <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#397" aria-description="Citation for case: United States Parole Commission v. Geraghty">445 U.S. at 397</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#1209" aria-description="Citation for case: United States Parole Commission v. Geraghty">100 S.Ct. at 1209</a></span>. “The requisite personal interest that must exist at the commencement of the litigation (standing) must continue throughout its existence (mootness).”
  <em>
   Geraghty,
  </em>
  <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#397" aria-description="Citation for case: United States Parole Commission v. Geraghty">445 U.S. at 397</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/" aria-description="Citation for case: United States Parole Commission v. Geraghty">100 S.Ct. at 1209</a></span> (quoting Monaghan,
  <em>
   Constitutional Adjudication: The Who and When,
  </em>
  <span class="citation no-link">82 Yale L.J. 1363</span>, 1384 (1973)). Of course, as class representatives, by definition, the named plaintiffs can prosecute only the class claims. Accordingly, the standing inquiry on the merits of plaintiffs’ case is directed to whether the class has standing — the necessary personal interest — to raise their constitutional claim for injunctive relief. The evidence presented at trial reveals that the plaintiff class faces a credible threat of recurring injury.
 </p>
<p id="b1422-4">
  Each of the four distinguishing features described above supports the conclusion that the class has standing under Article III as interpreted by
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>.
  </em>
  The systematic pattern finding of the district court, the official INS policy for the conduct of ranch checks, and the district court’s finding of likely recurrence all reinforce the reality and immediacy of the plaintiffs’ constitutional claims. Unlike Lyons, the members of plaintiff class do not have to induce a police encounter before the possibility of injury can occur.
  <em>
   See Lewis v. Tully,
  </em>
  <span class="citation" data-id="8800747"><a href="/opinion/8816245/lewis-v-tully/" aria-description="Citation for case: Lewis v. Tully">99 F.R.D. 632</a></span> (N.D.Ill.1983). The class members are subject to constitutional injury based on the completely innocent behavior of residing in migrant farm housing. Their grievances are general only to the residents of farm housing in the Spokane Sector. Members of the class have repeatedly suffered personal injuries in the past that can fairly be traced to the INS’s standard ranch and farm practices. Class members have been and will continue to be aggrieved by the defendants’ unconstitutional pattern of conduct in contravention of the Fourth Amendment. The equitable relief sought by the plaintiff class is both efficacious and responsive to the individual interests of class members and the certified class.
 </p>
<p id="b1422-7">
  B.
 </p>
<p id="b1422-8">
  The district court found that the defendants’ pattern of conduct violated the plaintiffs’ Fourth Amendment rights under either of two separate holdings. The district court first held that the methods employed by the Border Patrol — “sealing] off roads or paths leading out of the housing area” if possible, and “stationpng] officers at all doors and windows” of the dwellings to prevent egress — constituted a “seizure” of the occupants such that “a reasonable person would have believed that he was not free to leave.”
  <em>
   LaDuke,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/#162" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 162-63</a></span>. Because the seizure thus preceded the alleged consent, the question of consent is immaterial to the finding of a Fourth Amendment violation. In the alternative, the district court concluded that under the INS’s standard farm check practice the consent given by the farm occupants was not voluntary.
 </p>
<p id="b1422-9">
  In response, the INS argues that the consent given by the occupants was voluntary and, citing
  <em>
   INS v. Delgado,
  </em>
  — U.S. --, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">104 S.Ct. 1758</a></span>, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">80 L.Ed.2d 247</a></span> (1984), contests the district court’s conclusion that a “seizure” occurs in the course of their farm and ranch checks. Other than its contention, raised unsuccessfully in the district court, that farm housing searches are identical to factory worksite sweeps, the INS has not explained why it requires its agents to obtain a warrant for urban residential searches but not for rural residential searches.
  <a class="footnote" href="#fn11" id="fn11_ref">
   11
  </a>
</p>
<p id="b1423-4">
<span citation-index="1" class="star-pagination" label="1327"> 
   *1327
   </span>
  In fashioning the injunction, the district court followed the law of this and every other circuit which has addressed the issue by requiring the INS to adduce articulable suspicion of both alienage and unlawful presence prior to the initiation of detentive stops.
  <em>
   See, e.g., Benitez-Mendez v. INS,
  </em>
  <span class="citation" data-id="418799"><a href="/opinion/418799/eleuterio-benitez-mendez-v-immigration-and-naturalization-service/#1100" aria-description="Citation for case: Eleuterio Benitez-Mendez v. Immigration and...">707 F.2d 1107, 1100</a></span> (9th Cir.1983),
  <em>
   amended
  </em>
  <span class="citation" data-id="444456"><a href="/opinion/444456/eleuterio-benitez-mendez-v-immigration-and-naturalization-service/" aria-description="Citation for case: Eleuterio Benitez-Mendez v. Immigration and...">748 F.2d 539</a></span> (9th Cir.1984) (clarifying that a seizure had taken place);
  <em>
   International Ladies Garment Workers Union v. Sureck,
  </em>
  <span class="citation" data-id="8915362"><a href="/opinion/8925775/international-ladies-garment-workers-union-v-sureck/#638" aria-description="Citation for case: International Ladies&#x27; Garment Workers&#x27; Union v. Sureck">681 F.2d 624, 638</a></span> (9th Cir.1982),
  <em>
   rev’d on other grounds sub nom. INS v. Delgado,
  </em>
  — U.S.-, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">104 S.Ct. 1758</a></span>, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">80 L.Ed.2d 247</a></span> (1984).
  <em>
   Accord Illinois Migrant Council v. Pilliod,
  </em>
  <span class="citation" data-id="9463025"><a href="/opinion/338582/illinois-migrant-council-etc-v-alva-l-pilliod-etc/#1070" aria-description="Citation for case: Illinois Migrant Council, Etc. v. Alva L. Pilliod, Etc.">540 F.2d 1062, 1070</a></span> (7th Cir.1976),
  <em>
   modified on reh’g en banc,
  </em>
  <span class="citation" data-id="342479"><a href="/opinion/342479/illinois-migrant-council-etc-v-alva-l-pilliod-etc/" aria-description="Citation for case: Illinois Migrant Council, Etc. v. Alva L. Pilliod, Etc.">548 F.2d 715</a></span> (1977);
  <em>
   Ojeda-Vinales v. INS,
  </em>
  <span class="citation" data-id="330250"><a href="/opinion/330250/jose-gil-ojeda-vinales-v-the-immigration-and-naturalization-service/#287" aria-description="Citation for case: Jose Gil Ojeda-Vinales v. The Immigration and...">523 F.2d 286, 287</a></span> (2d Cir.1975) (following
  <em>
   Au Yi
  </em>
  Lau);
  <em>
   Au Yi Lau v. INS,
  </em>
  <span class="citation multiple-matches"><a href="/c/F.2d/445/217/">445 F.2d 217</a></span>, 223 (D.C.Cir.),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./404/864/">404 U.S. 864</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./92/64/">92 S.Ct. 64</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/30/108/">30 L.Ed.2d 108</a></span> (1971);
  <em>
   Ramirez v. Webb,
  </em>
  <span class="citation" data-id="1897912"><a href="/opinion/1897912/ramirez-v-webb/#1282" aria-description="Citation for case: Ramirez v. Webb">599 F.Supp. 1278, 1282</a></span> (W.D.Mich.1984). Consistent with the statutory language of <span class="citation no-link">8 U.S.C. § 1357</span>(a)(1), however, the district court’s injunction does permit nondetentive interrogations based solely on alienage.
  <em>
   LaDuke,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/#165" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 165</a></span>.
  <em>
   Accord Illinois Migrant Council v. Pilliod,
  </em>
  <span class="citation" data-id="342479"><a href="/opinion/342479/illinois-migrant-council-etc-v-alva-l-pilliod-etc/" aria-description="Citation for case: Illinois Migrant Council, Etc. v. Alva L. Pilliod, Etc.">548 F.2d 715</a></span> (7th Cir.1977) (en banc).
  <em>
   But see Marquez v. Kiley,
  </em>
  <span class="citation" data-id="1430125"><a href="/opinion/1430125/marquez-v-kiley/" aria-description="Citation for case: Marquez v. Kiley">436 F.Supp. 100</a></span> (S.D.N.Y.1977) (Fourth Amendment bars both detentive and nondetentive INS interrogations based solely on alien-age).
 </p>
<p id="b1423-12">
  1.
 </p>
<p id="b1423-13">
  The district court’s conclusion that the INS farm and ranch check practices result in the seizure of an entire farm housing community is predicated on the facts as the district court found them. On this record we cannot say that these facts are clearly erroneous.
  <a class="footnote" href="#fn12" id="fn12_ref">
   12
  </a>
  Nonetheless, the seizure conclusion is a mixed question of law and fact subject to de novo review on these facts. The district court concluded: “when uniformed officers surround residences with emergency vehicles with flashing lights, approach the houses with flashlights, awaken the occupants, and station officers at all doors and windows, it borders on the incredulous to conclude that people such as the members of the class in this action would feel free to walk away.” This conclusion is reinforced by the further factual finding that residents who exited the housing “were apprehended, detained, and interrogated.”
 </p>
<p id="b1423-14">
  The record in this case contains incidents in which Border Patrol agents forcibly intruded, either physically or with a flash
  <span citation-index="1" class="star-pagination" label="1328"> 
   *1328
   </span>
  light, into the housing units.
  <a class="footnote" href="#fn13" id="fn13_ref">
   13
  </a>
  Looking at the entire record, especially the findings that the access roads were sealed, the means of egress from the individual units were surrounded and those who left were seized, we affirm the district court’s conclusion that a seizure of the entire unit is routinely accomplished. Moreover, the Supreme Court’s opinion in
  <em>
   INS v. Delgado
  </em>
  only strengthens the validity of the district court’s seizure conclusion.
 </p>
<p id="b1424-4">
  In
  <em>
   INS v. Delgado,
  </em>
  — U.S. -, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">104 S.Ct. 1758</a></span>, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">80 L.Ed.2d 247</a></span> (1984), the Supreme Court held that INS worksite interrogations conducted pursuant to warrants do not violate the Fourth Amendment. The
  <em>
   <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>
  </em>
  opinion rejected a contrary holding by this circuit wherein we had held that such factory surveys resulted in a seizure of the workforce. The Court also reversed our alternate holding that employee questioning must be based on particularized suspicion.
 </p>
<p id="b1424-6">
  In dismissing the seizure-of-the-workforce theory the Supreme Court discounted the plaintiff’s evidence that employees were not free to leave the factory.
  <a class="footnote" href="#fn14" id="fn14_ref">
   14
  </a>
  The Court then held that: “if mere questioning does not constitute a seizure when it occurs inside the factory, it is no more a seizure when it occurs at the exits.” If INS agents were lawfully conducting questioning, pursuant to a warrant, inside the workplace, then similar conduct is permissible at points of egress.
 </p>
<p id="b1424-7">
  On the issue of particularized suspicion of illegal alienage, the Supreme Court found that none of the individual encounters rose to the level of a detentive interrogation.
  <em>
   Id.
  </em>
  104 S.Ct. at 1764. According to the Court, the brief encounters only amounted to “questioning” that did not involve any reasonable apprehension of, or actual detention by the INS agents. Under the “seizure” test articulated in
  <em>
   Delgado: “Unless the circumstances of the encounter are so intimidating
  </em>
  as to demonstrate that a reasonable person would have believed he was not free to leave if he had not responded, one cannot say that the questioning resulted in a detention under the Fourth Amendment.”
  <em>
   Id.
  </em>
  at 1763 (emphasis added).
 </p>
<p id="b1424-10">
  Two material distinctions between
  <em>
   <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>
  </em>
  and the present case are noteworthy. First, unlike
  <em>
   <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>,
  </em>
  the INS agents do not obtain any form of warrant for ranch and farm checks. As the district court found, the INS agents base their decision to check on a random basis without any current articulable suspicion that particular units will contain illegal aliens. Also unlike
  <em>
   <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>,
  </em>
  the INS systematically fails to obtain the consent of the owner of the farm housing. A second distinction between the factory surveys in
  <em>
   <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>
  </em>
  and farm checks is the materially different forum in which these searches take place— the workplace versus the home. Although the INS persists in contending that farm housing is part and parcel of the workplace and should be treated similarly, the simple truth is that the INS itself has recognized that they are dissimilar. If the INS truly thought that the occupants of farm housing were living at the workplace then the INS would be obliged to seek the consent of the employer — not the occupant — to obtain access. The measure of protection
  <span citation-index="1" class="star-pagination" label="1329"> 
   *1329
   </span>
  accorded the home under the Fourth Amendment is .qualitatively different from that afforded the workplace under
  <em>
   <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>.
  </em>
  “[T]he employers’ expectation of privacy in the plant setting ... certainly is far less than the traditional expectation of privacy in one’s residence.”
  <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#1767" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><em>
   Id.
  </em>
  at 1767</a></span> (Powell, J., concurring). Significantly, the
  <em>
   <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>
  </em>
  opinion’s reliance on the permissibility of questioning within the open interior of the workplace to justify questioning at the workplace exits is clearly inapplicable to the home setting.
 </p>
<p id="b1425-5">
  2.
 </p>
<p id="b1425-6">
  In the alternative, the district court held that under the circumstances of these farm checks, any consent given by the occupants was not voluntary. The government has the burden of proving voluntary consent.
  <em>
   Schneckloth,
  </em>
  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#248" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218 at 248</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#2058" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041 at 2058</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L.Ed.2d 854</a></span> (1973) (state must show voluntariness “when the subject of a search is not in custody”). On appeal, we can reverse the district court’s consent finding “only if in viewing the evidence in the light most favorable to the [plaintiffs],” the finding is clearly erroneous.
  <a class="footnote" href="#fn15" id="fn15_ref">
   15
  </a>
</p>
<p id="b1425-7">
  The district court listed the following factors as supportive of its finding that, under the standard practices applicable to ranch and farm checks, any consent given by the occupants was not voluntary: the uniform failure of the agents to advise the occupants of the right to refuse; the inherent fear that the residents of the camp have of uniformed officers because of their Mexican heritage; the limited lingual and educational background of the housing occupants; the early morning or late evening hours of the checks; and the occupant’s knowledge of the “power which INS has in dealing with them” as opposed to the average citizen.
  <em>
   LaDuke,
  </em>
  460 F.Supp. at 163 (citing
  <em>
   Marquez v. Kiley,
  </em>
  <span class="citation" data-id="1430125"><a href="/opinion/1430125/marquez-v-kiley/#113" aria-description="Citation for case: Marquez v. Kiley">436 F.Supp. 100, 113-14</a></span> (S.D.N.Y.1977)). Citing the show of official force and the vulnerable nature of the migrant workforce, the district court found that the government had not met its burden in showing voluntary consent to search. When placed against the court’s other factual findings and the record as a whole, the district court’s factual finding of involuntary consent when the occupants are confronted with the standard pattern of conduct in a ranch check is not clearly erroneous.
  <a class="footnote" href="#fn16" id="fn16_ref">
   16
  </a>
</p>
<p id="b1425-11">
  Courts have referred to identical or similar factors as probative on the factual question of the voluntariness of consent to search.
  <em>
   See, e.g., Schneckloth v. Bustamonte,
  </em>
  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L.Ed.2d 854</a></span> (1973) (“traditional definition of voluntariness we accept today has always taken into account evidence of minimal schooling”; failure to inform of right to refuse consent probative on voluntariness);
  <em>
   United States v. Mayes,
  </em>
  <span class="citation" data-id="344431"><a href="/opinion/344431/united-states-v-theodore-howard-mayes/" aria-description="Citation for case: United States v. Theodore Howard Mayes">552 F.2d 729</a></span> (6th Cir.1977) (minimal schooling);
  <em>
   United States v. O’Looney,
  </em>
  <span class="citation" data-id="9463220"><a href="/opinion/340099/united-states-v-michael-olooney/#388" aria-description="Citation for case: United States v. Michael O&#x27;LOOney">544 F.2d 385, 388</a></span> (9th Cir.) (business sophistication),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./429/1023/">429 U.S. 1023</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./97/642/">97 S.Ct. 642</a></span>, <span class="citation no-link">50 L.Ed.2d 625</span> (1976);
  <em>
   United States v. Rodriguez,
  </em>
  <span class="citation" data-id="331358"><a href="/opinion/331358/united-states-v-eduardo-rodriguez/#1315" aria-description="Citation for case: United States v. Eduardo Rodriguez">525 F.2d 1313, 1315-16</a></span> (10th Cir.1975) (lack of fluency in English);
  <em>
   United States v. Marshall,
  </em>
  <span class="citation" data-id="315664"><a href="/opinion/315664/united-states-v-robert-marshall-united-states-of-america-v-dennis/#1187" aria-description="Citation for case: United States v. Robert Marshall, United States of...">488 F.2d 1169, 1187-89</a></span> (9th Cir.1973) (show of force by armed officers; display of authority);
  <em>
   Harless v. Turner,
  </em>
  <span class="citation" data-id="302265"><a href="/opinion/302265/george-franklin-harless-v-john-w-turner-warden-utah-state-prison/#1338" aria-description="Citation for case: George Franklin Harless v. John W. Turner, Warden, Utah...">456 F.2d 1337, 1338</a></span> (10th Cir.1972) (defendant awakened by numerous officers at early morning hour);
  <em>
   Marquez v. Kiley,
  </em>
  <span class="citation" data-id="1430125"><a href="/opinion/1430125/marquez-v-kiley/#113" aria-description="Citation for case: Marquez v. Kiley">436 F.Supp. 100, 113-14</a></span> (S.D.N.Y.1977). The district court’s finding of involuntary consent also finds support on this record in that the INS did not meet its evidentiary burden to prove consent; the record demonstrates “no more than acquiescence to a claim of lawful authority.”
  <em>
   Bumper v. North Carolina,
  </em>
  <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#548" aria-description="Citation for case: Bumper v. North Carolina">391 U.S. 543, 548-49</a></span>, <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#1792" aria-description="Citation for case: Bumper v. North Carolina">88 S.Ct. 1788, 1792</a></span>, <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">20 L.Ed.2d 797</a></span> (1968);
  <em>
   cf. Gomez v. Turner,
  </em>
  <span class="citation" data-id="400070"><a href="/opinion/400070/manuel-gomez-v-maurice-t-turner-jr-chief-of-police/#141" aria-description="Citation for case: Manuel Gomez v. Maurice T. Turner, Jr., Chief of Police">672 F.2d 134, 141</a></span> (D.C.Cir.1982) (“ ‘seizure’ occurs when a police officer, by force or show of authority, restrains the liberty of a citizen”). The atmo
  <span citation-index="1" class="star-pagination" label="1330"> 
   *1330
   </span>
  sphere surrounding the INS’s standard farm check practices depicts a substantial show of official force. The tenor of the injunction reveals that it is aimed at preventing involuntary consent prompted by shows of force or claims of lawful authority.
  <em>
   LaDuke,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/#165" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 165</a></span>.
 </p>
<p id="b1426-4">
  C.
 </p>
<p id="b1426-5">
  The government challenges both the appropriateness of injunctive relief and the breadth of the injunction issued. We affirm the issuance of an injunction and reject the INS’s overbreadth arguments as raised in the district court.
 </p>
<p id="b1426-6">
  1.
 </p>
<p id="b1426-7">
  The district court correctly stated the basic prerequisites for issuance of a permanent injunction as “the likelihood of substantial and immediate irreparable injury and the inadequacy of remedies at law.”
  <em>
   LaDuke,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 162</a></span> (citing
  <em>
   O’Shea,
  </em>
  <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/#502" aria-description="Citation for case: O&#x27;Shea v. Littleton">414 U.S. at 502</a></span>, 94 S.Ct. at 679). The district court then found that plaintiffs had prevailed on the merits and the balance of the equities favored injunctive relief.
  <em>
   La-Duke,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/#162" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 162</a></span>. The court then determined “what form of [equitable] relief is appropriate.”
  <em>
   <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/" aria-description="Citation for case: LaDuke v. Nelson">Id.</a></span>
  </em>
  Twenty days after issuance
  <em>
   of the
  </em>
  original injunction, the district court amended the injunction, an act clearly within its jurisdiction,
  <em>
   Safe Flight Instrument Corp. v. United Control Corp.,
  </em>
  <span class="citation" data-id="8906441"><a href="/opinion/8918072/safe-flight-instrument-corp-v-united-control-corp/#1343" aria-description="Citation for case: Safe Flight Instrument Corp. v. United Control Corp.">576 F.2d 1340, 1343</a></span> (9th Cir.1978), to clarify that the injunction “is not intended to prohibit clearly consensual entries such as those made for the purpose of gathering an arrested alien’s belongings.”
  <em>
   LaDuke,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 165</a></span> n. 1.
 </p>
<p id="b1426-8">
  From the preceding discussion of the merits of plaintiffs’ case, the district court’s conclusion on the appropriateness of injunctive relief is sound. From the previous discussion on the plaintiffs’ standing, it should be evident that plaintiffs face a “likelihood of substantial and immediate irreparable injury.”
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>,
  </em>
  461 U.S. at Ill, 103 S.Ct. at 1670 (quoting
  <em>
   <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">O’Shea</a></span>,
  </em>
  at 502, 94 S.Ct. at 679). The likelihood that class members will suffer prospective injury is buttressed not only by the defendants’ past conduct but also by the defendants’ avowed future intent.
 </p>
<p id="b1426-13">
  The district court’s conclusion that the remedies at law are inadequate is also sound. As the Supreme Court stated in rejecting the application of the exclusionary rule in deportation hearings, the deterrent value of the rule “is undermined by the availability of alternative remedies for institutional practices by the INS” in contravention of the Fourth Amendment.
  <em>
   INS v. Lopez-Mendoza,
  </em>
  — U.S.-, <span class="citation" data-id="9429772"><a href="/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/#3488" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Lopez-Mendoza">104 S.Ct. 3479, 3488</a></span>, <span class="citation" data-id="9429772"><a href="/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Lopez-Mendoza">82 L.Ed.2d 778</a></span> (1984). In particular, “[T]he possibility of declaratory relief against the agency thus offers a means for challenging the validity of INS practices, when standing requirements for bringing such an action can be met.”
  <em>
   Id.
  </em>
  104 S.Ct. at 3488.
 </p>
<p id="b1426-16">
  The only other remedy at law available to the class is an action for damages.
  <a class="footnote" href="#fn17" id="fn17_ref">
   17
  </a>
  For various reasons the district court found that damages were not available to the individual class representatives. The plaintiffs have not appealed this ruling nor has the INS asserted that damages constituted an adequate alternative remedy at law for plaintiffs individually or as a class. The high likelihood that the violations will recur absent issuance of an injunction counsels in favor of equitable rather than legal relief. In addition, the district court certified this suit as a class under Rule 23(b)(2), which literally permits only class applications for injunctive or declaratory relief.
  <a class="footnote" href="#fn18" id="fn18_ref">
   18
  </a>
<em>
   See
  </em>
  Fed. R.Civ.P. 23(b)(2).
 </p>
<p id="b1426-17">
  2.
 </p>
<p id="b1426-18">
  The INS further contends that the injunction is overbroad. We reject those challenges to the breadth of the injunction unsuccessfully raised in the district court. We decline to express any opinion on any overbreadth claim not originally addressed
  <span citation-index="1" class="star-pagination" label="1331"> 
   *1331
   </span>
  to the district court. Given the district court’s extensive experience with the facts and litigants, sound principles of judicial administration indicate that any further challenges to the scope of the injunction be directed initially to the jurisdiction of the district court.
 </p>
<p id="b1427-5">
  The amended injunction has three separate components barring: (a) warrantless entries of farm dwellings to search or arrest unless the officers have “clear[] consent” or probable cause; (b) warrantless arrests or searches of migrant farm housing residents unless based on probable cause; and (c) “stopping, detaining, and interrogating [class members] by force, threats of force or a command based upon official authority” absent a warrant, probable cause, or reasonable suspicion based on articulable fact that the person is an alien illegally within the United States. The injunction does expressly permit, however, the nondetentive interrogation of suspected aliens concerning their lawful presence in the United States.
  <em>
   <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/" aria-description="Citation for case: LaDuke v. Nelson">LaDuke</a></span>,
  </em>
  560 P.Supp. at 165.
 </p>
<p id="b1427-6">
  According to the INS, the first component of the injunction is overbroad because it allegedly bars consensual searches. This argument was previously made in the district court after the issuance of the original injunction, and any ambiguity on this matter was clarified by the amended injunction. Under the amended injunction, clearly consensual searches are expressly permitted. The first component of the injunction is directed to farm housing entries. If anything, this component’s • simple language overstates the bounds of the INS’s authority to enter housing units with or without a warrant. In sum, however, we think the plain language of the first component provides ample flexibility for INS searches while preserving class members’ reasonable expectations of privacy.
 </p>
<p id="b1427-7">
  The INS finds the second component of the injunction legally “unremarkable” but claims it would cast a chill on officer performance because they are not fully conversant in the legal standards for searches and seizures. We sympathize with the INS’s educational task in keeping its officers abreast of the developments in the fast-moving world of the Fourth Amendment. When the Chief Patrol Agent for the Spokane Sector testified in the district court, however, he stated that house-to-house searches of farm dwellings would not be permitted under INS policy without individualized suspicion as to each searched dwelling. The testimony of his agents, on the other hand, indicated that house-to-house searches without information as to specific dwellings was a standard practice. Consequently, we cannot affix the entire blame for the educational difficulties of the INS solely on the prolix language of the numerous judicial interpretations of the Fourth Amendment. We find the plain language of the injunction’s second component sufficiently clear to convey the Fourth Amendment’s core commands to all who wish to listen.
 </p>
<p id="b1427-9">
  The third injunctive proscription is challenged by the INS because it bars detentive stops without articulable suspicion of both alienage and illegal presence in the United States. For reasons previously explained, in this nonborder context the Fourth Amendment requires at least articulable suspicion of both alienage and unlawful presence for a detentive stop. The government’s overbreadth claim completely ignores the language of the injunction’s third component, which permits nondetentive interrogations as to illegal presence based solely on reasonable belief of alienage.
 </p>
<p id="b1427-10">
  Lest there remain any dotibts, the amended injunction as it-.currently stands does not infringe upon the legitimate use of law enforcement practices within the migrant worker farm housing community in the Spokane Sector. As the district court stated in the course of the trial, none of the parties disputed the legitimate enforcement needs of the INS within this community. As the district court found, however, the use of ranch checks by the INS in the Spokane Sector cannot be viewed as casual encounters between residents and law enforcement. We agree with the district court’s conclusion that
  <span citation-index="1" class="star-pagination" label="1332"> 
   *1332
   </span>
  farm checks, as described by the witnesses, run afoul of the Fourth Amendment.
 </p>
<p id="b1428-4">
  D.
 </p>
<p id="b1428-5">
  The bulk of the INS’s certification contentions are merely adjuncts to the INS’s challenges to class standing. Nonetheless, assuming that the propriety of the district court’s certification decision has been placed at issue by the government on appeal, the district court did not abuse its discretion in certifying the plaintiff class.
  <em>
   See Moore v. Hughes Helicopters, Inc.,
  </em>
  <span class="citation" data-id="419216"><a href="/opinion/419216/tommie-y-moore-plaintiff-appellant-v-hughes-helicopters-inc-a/#479" aria-description="Citation for case: Tommie Y. MOORE, Plaintiff-Appellant, v. HUGHES...">708 F.2d 475, 479</a></span> (9th Cir.1983) (standard of review for class certification is “abuse of discretion or impermissible legal criteria”).
 </p>
<p id="b1428-6">
  Rule 23(a) sets forth the four minimum requirements of (a) numerosity (b) commonality (c) typicality, and (d) adequate representation. Fed.R.Civ.P. 23(a). Only commonality and typicality have been questioned by the INS. The position of the INS is without merit. Plainly, the constitutionality of the INS ranch check technique as it affects the defined class is a “question of law or fact common to the class.”
  <em>
   <span class="citation" data-id="419216"><a href="/opinion/419216/tommie-y-moore-plaintiff-appellant-v-hughes-helicopters-inc-a/" aria-description="Citation for case: Tommie Y. MOORE, Plaintiff-Appellant, v. HUGHES...">Id.</a></span>
  </em>
</p>
<p id="b1428-7">
<em>
   Of
  </em>
  course, if material variations exist as to the law or facts involved with individual class member injuries, then the commonality requirement would not be met.
  <em>
   In re Hotel Telephone Charges, <span class="citation" data-id="320513"><a href="/opinion/320513/in-re-hotel-telephone-charges/#89" aria-description="Citation for case: In Re HOTEL TELEPHONE CHARGES">500 F.2d 86, 89</a></span>
  </em>
  (9th Cir.1974). The district court’s ultimate factual finding of a uniform pattern of INS conduct, upon which the court premised its legal conclusions, reinforces the court’s pri- or conclusion that there are no material differences among individual class grievances. Accordingly, the district court can hardly be held to have abused its discretion in finding commonality for class claims.
 </p>
<p id="b1428-8">
  Similarly, the typicality of the class representative’s claims was vigorously litigated in the district court and the district court did not abuse its discretion in finding that the named plaintiffs’ claims are typical of those raised by the class as to the propriety of injunctive relief. The minor differences in the manner in which the representative’s Fourth Amendment rights were violated
  <a class="footnote" href="#fn19" id="fn19_ref">
   19
  </a>
  does not render their claims atypical of those of the class. We agree that the representatives’ claims fairly encompass the Fourth Amendment claims of the remaining class members.
 </p>
<p id="b1428-11">
  Finally,
  <em>
   citing Betts v. Reliable Collection Agency, Ltd.,
  </em>
  <span class="citation" data-id="8913981"><a href="/opinion/8924619/betts-v-reliable-collection-agency-ltd/#1005" aria-description="Citation for case: Betts v. Reliable Collection Agency, Ltd.">659 F.2d 1000, 1005</a></span> (9th Cir.1981) (after certification court may divide class into subclasses), the INS contends that the class certified by the district court is actually composed of discrete subclasses which require separate treatment by the court. We reject the INS’s attempt to raise the subclass issue for the first time on appeal. The district court did not abuse its discretion in failing to address sua sponte the possibility of subclasses under Federal Rule of Civil Procedure 23(c)(4)(B) when the subclass proponent fails to request such a procedure,
  <em>
   see United States Parole Commission v. Geraghty, 445 U.S.
  </em>
  388, 408, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#1214" aria-description="Citation for case: United States Parole Commission v. Geraghty">100 S.Ct. 1202, 1214</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/" aria-description="Citation for case: United States Parole Commission v. Geraghty">63 L.Ed.2d 479</a></span> (1980), and no obvious basis for subclass creation, such as conflicting interests within the class, is apparent on the record.
 </p>
<p id="b1428-12">
  E.
 </p>
<p id="b1428-13">
  After two days of hearings the district court awarded plaintiffs’ counsel approximately $300,000 in attorney fees and costs under the Equal Access to Justice Act (“EAJA”), <span class="citation no-link">28 U.S.C. § 2412</span>. The fee application of the various counsel for plaintiff class was premised on the availability of fees under either § 2412(b) or § 2412(d)(1)(A). The distrit court held plaintiffs’ counsel entitled to fees under both provisions. The district court then rigorously analyzed the various fee applications, awarded reasonable hourly fees of $100 to Mr. Fox and $125 for Mr. Ginsberg, and applied a 20% multiplier based on the risk that the attorneys’ work on such a protracted case would go uncompensated.
 </p>
<p id="b1429-4">
<span citation-index="1" class="star-pagination" label="1333"> 
   *1333
   </span>
  The government now challenges both statutory bases of entitlement under the EAJA found by the court below. The standard of review applied in this circuit to a district court’s ruling on attorney fees is abuse of discretion.
  <em>
   Foster v. Tourtellotte,
  </em>
  <span class="citation" data-id="8916719"><a href="/opinion/8926932/foster-v-tourtellotte/#1110" aria-description="Citation for case: Foster v. Tourtellotte">704 F.2d 1109, 1110-11</a></span> (9th Cir.). Nonetheless, issues regarding the proper interpretation of the EAJA are subject to
  <em>
   de novo
  </em>
  review.
  <em>
   Lauritzen v. Lehman,
  </em>
  <span class="citation" data-id="8922565"><a href="/opinion/8932408/lauritzen-v-lehman/#553" aria-description="Citation for case: Lauritzen v. Lehman">736 F.2d 550, 553</a></span> (9th Cir.1984).
 </p>
<p id="b1429-5">
  The district court rejected plaintiffs’ claim to fees under § 2412(b) which had been raised under a “common law benefit” theory. The district court’s alternative finding of fee entitlement under the analogous “statute” prong of § 2412(b) is no longer consistent with Ninth Circuit precedent.
  <em>
   See Lauritzen v. Lehman,
  </em>
  <span class="citation" data-id="8922565"><a href="/opinion/8932408/lauritzen-v-lehman/#553" aria-description="Citation for case: Lauritzen v. Lehman">736 F.2d 550, 553-59</a></span> (9th Cir.1984).
 </p>
<p id="b1429-6">
  The district court’s separate ruling on entitlement under <span class="citation no-link">28 U.S.C. § 2412</span>(d)(1)(A), however, did not constitute an abuse of discretion. The court’s finding that plaintiffs were prevailing parties
  <a class="footnote" href="#fn20" id="fn20_ref">
   20
  </a>
  has not been challenged on appeal. The INS largely contests the district court’s finding that the government’s position was not “substantially justified.”
  <a class="footnote" href="#fn21" id="fn21_ref">
   21
  </a>
</p>
<p id="b1429-7">
  Following
  <em>
   Rawlings v. Heckler,
  </em>
  <span class="citation" data-id="8918963"><a href="/opinion/8928923/rawlings-v-heckler/" aria-description="Citation for case: Rawlings v. Heckler">725 F.2d 1192</a></span> (9th Cir.1984), the district court found the government’s position lacked a reasonable basis in law and fact because the law regarding the need for articulable suspicion was clear, the defendants failed to follow both the law and their own policies, and the INS needlessly protracted the litigation by denying routine INS practices. The district court, having a unique perspective earned from tireless effort in this protracted litigation, did not abuse its discretion in finding an absence of substantial justification.
 </p>
<p id="b1429-8">
  Finally, the INS charges that the hourly fee award ($100 and $125) to class counsel unreasonably exceeded the normal fee of $75 per hour under the EAJA. The EAJA authorizes exceeding the $75 “cap” on attorney fees based on either a cost of living increase or a “special factor, such as the limited availability of qualified attorneys for the proceedings.” 28 .U.S.C. § 2412(d)(2)(A)(ii). The court did not abuse its discretion in finding a special factor existed for breaching the $75 cap based on expert testimony.
  <em>
   Accord Action on Smoking and Health v. CAB,
  </em>
  <span class="citation" data-id="429382"><a href="/opinion/429382/action-on-smoking-and-health-v-civil-aeronautics-board-action-on-smoking/#219" aria-description="Citation for case: Action on Smoking and Health v. Civil Aeronautics Board,...">724 F.2d 211, 219</a></span> (D.C.Cir.1984). The court relied on a concurring opinion in
  <em>
   Blum v. Stenson,
  </em>
  — U.S. -, <span class="citation" data-id="9429529"><a href="/opinion/111123/blum-v-stenson/" aria-description="Citation for case: Blum v. Stenson">104 S.Ct. 1541</a></span>, <span class="citation" data-id="9429529"><a href="/opinion/111123/blum-v-stenson/" aria-description="Citation for case: Blum v. Stenson">79 L.Ed.2d 891</a></span> (1984), to support the position that the inordinate risk of no fee award was sufficient to justify a multiplier. The contingent nature of fee awards under the EAJA has been held a “special factor” permitting a multiplier.
  <em>
   Action on Smoking and Health v. CAB,
  </em>
  <span class="citation" data-id="429382"><a href="/opinion/429382/action-on-smoking-and-health-v-civil-aeronautics-board-action-on-smoking/" aria-description="Citation for case: Action on Smoking and Health v. Civil Aeronautics Board,...">724 F.2d 211</a></span>-218 (D.C.Cir.1984) (citing
  <em>
   Copeland v. Marshall,
  </em>
  <span class="citation" data-id="9467613"><a href="/opinion/387362/dolores-j-copeland-individually-and-on-behalf-of-the-class-of-all-others/#905" aria-description="Citation for case: Dolores J. Copeland, Individually and on Behalf of the...">641 F.2d 880, 905-08</a></span> (D.C.Cir.1980) (en banc));
  <em>
   Coleman v. Block,
  </em>
  <span class="citation" data-id="1869791"><a href="/opinion/1869791/coleman-v-block/#1421" aria-description="Citation for case: Coleman v. Block">589 F.Supp. 1411, 1421</a></span> (D.N.Dak.1984);
  <em>
   Local 3-98, Int. Woodworkers of America v. Donovan,
  </em>
  <span class="citation" data-id="1450572"><a href="/opinion/1450572/local-3-98-international-woodworkers-of-america-v-donovan/#717" aria-description="Citation for case: Local 3-98, International Woodworkers of America v. Donovan">580 F.Supp. 714, 717</a></span> (N.D.Cal.1984). Consequently, the district court properly took this special factor into account in adjusting the plaintiffs’ attorney fees.
 </p>
<p id="b1429-13">
  IV.
 </p>
<p id="b1429-14">
  We affirm the district court’s issuance of an amended injunction and the award of fees and costs.
 </p>





















<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b1418-7">
   . We note that
   <em>
    United States v. Maybusher,
   </em>
   <span class="citation" data-id="436162"><a href="/opinion/436162/united-states-v-frank-j-maybusher/" aria-description="Citation for case: United States v. Frank J. Maybusher">735 F.2d 366</a></span>, 371 n. 1 (9th Cir.1984), holds that we exercise de novo review over district court determinations on the mixed question of fact and law regarding the presence of articulable facts justifying a detentive stop. Rather than reconcile the conflicting signals we have received from our past precedent, we have carefully reviewed the evidence and found the district court’s finding of no articulable suspicion correct under both de novo and the clearly erroneous standards.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b1418-8">
   . Similarly, we recognize that some post
   <em>
    -McConney
   </em>
   case law suggests that a Fourth Amendment "seizure” conclusion is reviewable under the clearly erroneous standard.
   <em>
    See United States v. Moreno,
   </em>
   <span class="citation" data-id="9472553"><a href="/opinion/440411/united-states-v-vidal-moreno/#537" aria-description="Citation for case: United States v. Vidal Moreno">742 F.2d 532, 537</a></span> (9th Cir.1984) (Wallace, J., concurring). Reviewed under either standard, we reach the same conclusion as the district court.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b1418-9">
   . The INS offers a general contention that because some class representatives, Charles La-Duke, for example, are not currently engaged in farm labor or residing in farm dwellings, they are not proper class representatives and therefore they lack standing to bring this suit. Although immaterial, plaintiffs assert that the class representatives will continue to reside in migrant worker housing. The INS argument as to the mootness of class representative claims was correctly rejected by the district court. The class was originally certified by Judge McNichols on October 13, 1981. When the district court redefined the class, largely to narrow the definition of the affected dwellings, it found the class representatives still remaining in the case were representative as of the original certification date.
  </p>
<p id="b1418-17">
   The district court based its 1981 finding that the class representatives would still represent the class on two alternate grounds. First, the court found the representatives’ individual circumstances within the class action rule for constitutional violations "capable of repetition, yet evading review" pronounced in
   <em>
    Sosna v. Iowa,
   </em>
   <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/#399" aria-description="Citation for case: Sosna v. Iowa">419 U.S. 393, 399-400</a></span>, <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/#557" aria-description="Citation for case: Sosna v. Iowa">95 S.Ct. 553, 557</a></span>, <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/" aria-description="Citation for case: Sosna v. Iowa">42 L.Ed.2d 532</a></span> (1975). In the alternative, the district court followed Ninth Circuit precedent which permits class representatives to prosecute class claims even though their individual claims become moot after certification.
   <em>
    Kuahulu v. Employers Insurance of Wausau,
   </em>
   <span class="citation" data-id="346935"><a href="/opinion/346935/bernard-kuahulu-for-himself-and-for-all-others-similarly-situated-v/" aria-description="Citation for case: Bernard Kuahulu, for Himself and for All Others Similarly...">557 F.2d 1334</a></span> (9th Cir.1977).
  </p>
<p id="b1418-18">
   The basis for allowing class representatives to continue despite mooted individual claims lies in the notion that, upon certification, the class acquires an independent legal status,
   <em>
    Kuahulu,
   </em>
   <span class="citation" data-id="346935"><a href="/opinion/346935/bernard-kuahulu-for-himself-and-for-all-others-similarly-situated-v/#1336" aria-description="Citation for case: Bernard Kuahulu, for Himself and for All Others Similarly...">557 F.2d at 1336</a></span>, for which the representative acts in a role "analogous to the private attorney general.”
   <em>
    United States Parole Commission v. Geraghty,
   </em>
   <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#403" aria-description="Citation for case: United States Parole Commission v. Geraghty">445 U.S. 388, 403</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#1212" aria-description="Citation for case: United States Parole Commission v. Geraghty">100 S.Ct. 1202, 1212</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/" aria-description="Citation for case: United States Parole Commission v. Geraghty">63 L.Ed.2d 479</a></span> (1980). Given the transience of the migrant labor force,
   <em>
    see also Ger-stein v. Pugh,
   </em>
   <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U.S. 103</a></span>, 111 n. 11, <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span>, 861 n. 11, <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">43 L.Ed.2d 54</a></span> (1975) ("constant existence of a class of persons suffering the deprivation is certain”), and the district court’s finding that the representatives would continue to press the class claims with diligence, both of the district court’s alternative grounds for rejecting the INS’s mootness challenge to the class representatives’ status are correct.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b1419-8">
   . This prudential standing limit has not been directly raised by the INS. Plaintiff class members are not attempting to assert the rights of nonparties to this litigation. Rather, they press and seek vindication of their personal rights. Moreover, in the context of this class action we find the “underlying justifications” for this prudential limitation absent.
   <em>
    See Singleton v. Wulff,
   </em>
   <span class="citation" data-id="9426552"><a href="/opinion/109530/singleton-v-wulff/#114" aria-description="Citation for case: Singleton v. Wulff">428 U.S. 106, 114</a></span>, <span class="citation" data-id="9426552"><a href="/opinion/109530/singleton-v-wulff/#2874" aria-description="Citation for case: Singleton v. Wulff">96 S.Ct. 2868, 2874</a></span>, <span class="citation" data-id="9426552"><a href="/opinion/109530/singleton-v-wulff/" aria-description="Citation for case: Singleton v. Wulff">49 L.Ed.2d 826</a></span> (1976) (Blackmun, J.).
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b1419-9">
   .
   <em>
    See generally
   </em>
   Note,
   <em>
    The Generalized Grievance Restriction: Prudential Restraint or Constitutional Mandate,
   </em>
   70 Geo.L.J. 1157 (1982) (discussing contours of the generalized grievance standing rule as a prudential limit).
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b1419-10">
   . We reserve ruling on whether remedial standing under
   <em>
    <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
   </em>
   is a prudential or constitutional standing limitation because the characterization would have no effect on the disposition of this case.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b1419-15">
   . We would prefer, however, to follow the Supreme Court’s post
   <em>
    -Lyons
   </em>
   standing analysis in
   <em>
    Kolender v. Lawson,
   </em>
   <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">461 U.S. 352</a></span>, <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">103 S.Ct. 1855</a></span>, <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">75 L.Ed.2d 903</a></span> (1983), and simply determine whether there is a "credible threat” that the plaintiffs will again be subject to ranch checks.
   <em>
    Id.
   </em>
   103 S.Ct. at 1857 n. 3.
   <em>
    <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">Kolender</a></span>
   </em>
   involved a facial challenge to a California identification statute under which plaintiff had repeatedly been arrested.
   <em>
    <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">Kolender</a></span>
   </em>
   also sought injunctive relief. Nonetheless, we think
   <em>
    <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
   </em>
   "cannot be so easily confined to [its] facts,” 461 U.S. at 108-09, 103 S.Ct. at 1668, and therefore will give careful attention to its teachings.
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b1420-7">
   . Obviously, proof of past injury, especially of a repetitive character, is not immaterial to the issue of likely recurrence.
   <em>
    See Kolender v. Lawson,
   </em>
   <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">461 U.S. 352</a></span>, 355 n. 3, <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">103 S.Ct. 1855</a></span>, 1857 n. 3, <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">75 L.Ed.2d 903</a></span> (1983);
   <em>
    Lewis v. Tally,
   </em>
   <span class="citation" data-id="8800747"><a href="/opinion/8816245/lewis-v-tully/#641" aria-description="Citation for case: Lewis v. Tully">99 F.R.D. 632, 641</a></span> (N.D.Ill.1983).
  </p>
</div><div class="footnote" id="fn9" label="9">
<a class="footnote" href="#fn9_ref">
   9
  </a>
<p id="b1421-7">
   . As the Court made clear in
   <em>
    Almeida-Sanchez,
   </em>
   the statutory authority bestowed on the INS must comply with the Constitution and courts should narrowly construe the INS’s statutory search and seizure authority consistent with Fourth Amendment precedent.
   <em>
    Almeida-Sanchez,
   </em>
   <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#272" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U.S. 266 at 272</a></span>, <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#2539" aria-description="Citation for case: Almeida-Sanchez v. United States">93 S.Ct. 2535 at 2539</a></span>, <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">37 L.Ed.2d 596</a></span> (1973).
  </p>
</div><div class="footnote" id="fn10" label="10">
<a class="footnote" href="#fn10_ref">
   10
  </a>
<p id="b1421-9">
   .
   <em>
    See O’Shea v. Littleton,
   </em>
   <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">414 U.S. at 494</a></span> n. 3, 94 S.Ct. at 675 n. 3. Although
   <em>
    <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">Rizzo</a></span>
   </em>
   did involve a class action, the Court declined to address the relevance of this fact.
   <em>
    Rizzo,
   </em>
   432 U.S. at 373, <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/#605" aria-description="Citation for case: Rizzo v. Goode">96 S.Ct. at 605</a></span>. The
   <em>
    <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">Rizzo</a></span>
   </em>
   opinion found no “pattern” of police misconduct sufficient to justify the detailed affirmative injunction ordered by the lower courts to rectify the undifferentiated allegations of police abuse.
   <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/#374" aria-description="Citation for case: Rizzo v. Goode"><em>
    Id.
   </em>
   at 374</a></span>, 96 S.Ct. at 605.
  </p>
</div><div class="footnote" id="fn11" label="11">
<a class="footnote" href="#fn11_ref">
   11
  </a>
<p id="b1422-5">
   . These ranch checks are not border area searches and the INS has not contended that these area control operations are conducted under its border control authority. Moreover, the Fourth Amendment does not permit the INS to differentiate on a per se basis in the privacy accorded different stocks of housing. Without question, the Fourth Amendment was intended to protect the resident’s, not the INS’s, expectation of privacy.
  </p>
<p id="b1422-13">
   The poorest man may in his cottage bid defiance to all the forces of the Crown. It may be
   <span citation-index="1" class="star-pagination" label="1327"> 
    *1327
    </span>
   frail; its roof may shake; the wind may blow through it; the storm may enter; the rain may enter; but the King of England cannot enter — all his force dares not cross the threshold of the ruined tenement!
  </p>
<p id="A6y">
<em>
    Miller
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#307" aria-description="Citation for case: Miller v. United States">357 U.S. 301, 307</a></span>, <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#1195" aria-description="Citation for case: Miller v. United States">78 S.Ct. 1190, 1195</a></span>, <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">2 L.Ed.2d 1332</a></span> (1958) (expressing principle articulated by William Pitt).
  </p>
</div><div class="footnote" id="fn12" label="12">
<a class="footnote" href="#fn12_ref">
   12
  </a>
<p id="b1423-9">
   . The INS does challenge the finding that the ranch checks are conducted without any individualized suspicion as to the presence of illegal aliens in the checked units. The district court’s finding to the contrary is amply supported in the record through the testimony of the INS Border Patrol agents.
  </p>
<p id="b1423-10">
   As the district court recognized, the Border Patrol Agents themselves presented conflicting evidence on the amount of information they obtained prior to initiating farm and ranch checks. For example, Agent Turner testified he never had any specific information in advance that identified a particular suspect or dwelling for a ranch check since at least 1974. Others indicated that they relied on notoriety or the "reputation” of a particular camp. Supervising Agent Minyard echoed these comments, noting that he normally did not refer to records of prior apprehensions in determining whether to initiate a check, and conceding that any information the Sector offices might receive from complaining witnesses was systematically destroyed and unavailable even after this suit was filed. He admitted that the decision to initiate ranch checks was sometimes based on no specific information and sometimes just on proximity to a migrant worker housing unit. Even in those situations where agents claimed to be acting on prior anonymous tips, the tips often were vague references to geographic areas or farm locations. Finally, the agents testified that it was INS policy to conduct complete sweeps of all community residences, with or without information as to specific residences. For example, Agent Minyard, on whom many of the other agents relied exclusively for information to commence a check, testified that a sole factor in approaching a particular residence was whether the lights were on.
  </p>
</div><div class="footnote" id="fn13" label="13">
<a class="footnote" href="#fn13_ref">
   13
  </a>
<p id="b1424-8">
   . For example, one agent testified that his "customary procedure" for obtaining consent was to grasp the belt of the person responding to the door. In another incident, class member Sally Wilson testified that on one occasion she was awakened by the flashlight of an agent, standing in her bedroom doorway, who then attempted to pull the blanket off her bed to ascertain if she was alone. In another episode, Ms. Wilson was making a pie in her kitchen when INS agents fanned around her residence, stationed themselves at all windows and doors, and peered into her home. As she was staring at the face of an agent looking through the window, the agent yelled that everything was okay because it was an “American family.” These and other incidents demonstrate that the atmosphere surrounding these early morning or nocturnal visitations is indeed intimidating to those residing in the farm housing units.
  </p>
</div><div class="footnote" id="fn14" label="14">
<a class="footnote" href="#fn14_ref">
   14
  </a>
<p id="b1424-12">
   .
   <em>
    See
   </em>
   104 S.Ct. at 1764 n. 6. The Court was only able to find one piece of evidence, contained in a deposition, that agents attempted to restrain a worker from leaving the factory. According to the Court, this was "an ambiguous, isolated event.”
  </p>
</div><div class="footnote" id="fn15" label="15">
<a class="footnote" href="#fn15_ref">
   15
  </a>
<p id="b1425-8">
   .
   <em>
    Id.
   </em>
   at 227, 93 S.Ct. at 2047;
   <em>
    United States v. Cawley,
   </em>
   <span class="citation" data-id="9467110"><a href="/opinion/382245/united-states-v-ralph-collins-cawley/#1349" aria-description="Citation for case: United States v. Ralph Collins Cawley">630 F.2d 1345, 1349</a></span> (9th Cir.1980).
  </p>
</div><div class="footnote" id="fn16" label="16">
<a class="footnote" href="#fn16_ref">
   16
  </a>
<p id="b1425-12">
   . While the district court’s link between Mexican culture and an inherent fear of uniformed officers is a questionable stereotype, it was not the sole basis for the court’s decision.
  </p>
</div><div class="footnote" id="fn17" label="17">
<a class="footnote" href="#fn17_ref">
   17
  </a>
<p id="b1426-9">
   . We do not mean to suggest that injunctive relief is limited to those situations in which the exclusionary rule is unavailable.
  </p>
</div><div class="footnote" id="fn18" label="18">
<a class="footnote" href="#fn18_ref">
   18
  </a>
<p id="b1426-19">
   . The complaint sought certification under Rule 23(b)(1)(A) but the court did not certify such a class.
  </p>
</div><div class="footnote" id="fn19" label="19">
<a class="footnote" href="#fn19_ref">
   19
  </a>
<p id="b1428-9">
   . LaDuke's privacy was violated by a flashlight search of his tent and a physical trespass while the Garcias’ privacy was violated only through trespass. Other class members suffered similar violations of their Fourth Amendment rights.
   <em>
    Cf.
   </em>
   Deposition of Ramon Castillo (unauthorized physical entry by agents, lights shined through windows).
  </p>
</div><div class="footnote" id="fn20" label="20">
<a class="footnote" href="#fn20_ref">
   20
  </a>
<p id="b1429-9">
   . The district court rejected INS arguments that the dismissal of some defendants, denial of a preliminary injunction, failure to settle the case, and limited nature of the injunction issued operated to deprive plaintiffs of prevailing party status.
  </p>
</div><div class="footnote" id="fn21" label="21">
<a class="footnote" href="#fn21_ref">
   21
  </a>
<p id="b1429-16">
   . The court also found no "special circumstances” rendered an award unjust and the INS has not contested this finding.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Lackey v. Stinnie.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Lackey v. Stinnie
type: case
citation: "604 U.S. 192 (2025)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2025
date_decided: ""
docket: 23-621
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
  opinion_url: "https://www.courtlistener.com/opinion/10776869/lackey-v-stinnie/"
  cluster_id: 10776869
  opinion_id: null
  identity_checked: true
lake:
  record_id: Lackey v. Stinnie
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
tags:
  - case
  - section-1983
  - attorneys-fees
  - section-1988
  - prevailing-party
  - preliminary-injunction
holding: "A party who obtains only a preliminary injunction — with no final judgment on the merits before the case becomes moot — is not a 'prevailing party' eligible for attorney's fees under 42 U.S.C. § 1988(b), because a preliminary injunction does not conclusively resolve the merits or create a judicially sanctioned, enduring change in the parties' legal relationship."
---

# Lackey v. Stinnie

*604 U.S. 192 (2025)* (No. 23-621) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10776869 → opinion 11243456; quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Virginia drivers whose licenses had been suspended for unpaid court fines and costs sued state officials under 42 U.S.C. § 1983, challenging the suspension statute. They obtained a preliminary injunction barring enforcement, and Virginia then repealed the law — mooting the case before any final judgment on the merits. The drivers sought attorney's fees under 42 U.S.C. § 1988(b), which lets a court award a reasonable fee to the "prevailing party" in certain civil-rights actions. The [[Reading and Citing Cases#en-banc|en banc]] Fourth Circuit held that a plaintiff who wins a preliminary injunction can be a "prevailing party," and awarded fees.

## Issue
Whether a party who obtains a preliminary injunction, but whose case becomes moot before the court enters a final judgment, is a "prevailing party" entitled to attorney's fees under § 1988(b).

## Rule
"Prevailing party" is a legal term of art meaning the party who successfully maintains its claim "when the matter is finally set at rest" — one who obtains a judicially sanctioned, enduring change in the legal relationship of the parties. A preliminary injunction does not qualify, because it rests only on a likelihood of success and does not conclusively resolve the merits. As the Court held: "Today, we establish that the enduring nature of that change must itself be judicially sanctioned. A plaintiff who wins a transient victory on a preliminary injunction does not become a 'prevailing party' simply because external events convert the transient victory into a lasting one." — 604 U.S. at 204. ^pin-204

## Application
The drivers' preliminary injunction gave them only temporary success at an intermediary stage of the suit; it never resolved their claims on the merits, and the subsequent repeal of the statute — an external event, not a judicial decision — was what made their relief lasting. Following *Buckhannon* and *Sole v. Wyner*, the Court held that such a transient, likelihood-based victory confers no prevailing-party status, and it favored a [[Common Legal Terms#bright-line-rule|bright-line rule]] as easy to administer and protective of judicial economy. The Court rejected the drivers' textual and historical arguments that § 1988(b) contains no finality requirement.

## Conclusion
The judgment of the Fourth Circuit was **reversed** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. Roberts, C.J., delivered the opinion of the Court, joined by Thomas, Alito, Kagan, Gorsuch, Kavanaugh, and Barrett, JJ.; Jackson, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], joined by Sotomayor, J.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Lackey* narrows the availability of § 1988(b) fee awards in § 1983 civil-rights litigation: a preliminary-injunction winner whose case is mooted before final judgment cannot recover fees, which may affect the incentives to bring and settle such suits.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Lackey v. Stinnie*, 604 U.S. 192 (2025)](https://www.courtlistener.com/opinion/10776869/lackey-v-stinnie/) — pinpoint: 204 (holding, Opinion of the Court); quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f6a8cbfd079e2eba", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Lackey v. Stinnie"}, "payload": {"all": [{"cite": "604 U.S. 192", "page": "192", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "604"}], "display": "604 U.S. 192", "official": {"cite": "604 U.S. 192", "page": "192", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "604"}, "official_selection_present": true, "record_id": "Lackey v. Stinnie"}}
{"assertion_id": "fd562434b5b462b5", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Lackey v. Stinnie"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Lackey v. Stinnie", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Lackey v. Stinnie

```json
{
  "schema_version": "s2.v1",
  "record_id": "Lackey v. Stinnie",
  "status": "under_review",
  "identity": {
    "case_name": "Lackey v. Stinnie",
    "case_name_short": "Lackey",
    "case_name_full": "",
    "input_case_name": "Lackey v. Stinnie",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2025,
    "docket": "23-621",
    "cluster_id": 10776869,
    "lead_opinion_id": 11243456,
    "sibling_ids": [],
    "absolute_url": "/opinion/10776869/lackey-v-stinnie/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "604 U.S. 192",
      "volume": "604",
      "reporter": "U.S.",
      "page": "192",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "604 U.S. 192",
        "volume": "604",
        "reporter": "U.S.",
        "page": "192",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "604 U.S. 192",
    "official_selection": {
      "court_class": "scotus",
      "selected": "604 U.S. 192",
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
    "date_created": "2026-07-06T12:12:30Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:12:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:12:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "lackey-v-stinnie--10776869",
      "to_record_id": "Lackey v. Stinnie",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Lackey v. Stinnie

```
                   PRELIMINARY PRINT

              Volume 604 U. S. Part 1
                             Pages 192–225




       OFFICIAL REPORTS
                                     OF


   THE SUPREME COURT
                             February 25, 2025


Page Proof Pending Publication


                    REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D. C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
192                     OCTOBER TERM, 2024

                                 Syllabus


      LACKEY, COMMISSIONER OF THE VIRGINIA
        DEPARTMENT OF MOTOR VEHICLES v.
                 STINNIE et al.
certiorari to the united states court of appeals for
                 the fourth circuit
      No. 23–621. Argued October 8, 2024—Decided February 25, 2025
Drivers whose licenses were suspended under a Virginia statute for failure
 to pay court fnes sued the Commissioner of the Virginia Department
 of Motor Vehicles under 42 U. S. C. § 1983, challenging the statute as
 unconstitutional. The District Court granted a preliminary injunction
 prohibiting the Commissioner from enforcing the statute. Before trial,
 the Virginia General Assembly repealed the statute and required re-
 instatement of licenses suspended under the law. The parties then
 agreed to dismiss the pending case as moot.
    Section 1988(b) allows an award of attorney's fees to “prevailing par-
 t[ies]” under § 1983. The District Court declined to award attorney's
 fees to the drivers under that section on the ground that parties who
Page Proof Pending Publication
 obtain a preliminary injunction do not qualify as “prevailing part[ies].”
 A Fourth Circuit panel affrmed, but the Fourth Circuit reversed en
 banc. The en banc court held that some preliminary injunctions can
 provide lasting, merits-based relief and qualify plaintiffs as prevailing
 parties, even if the case becomes moot before fnal judgment.
Held: The plaintiff drivers here—who gained only preliminary injunctive
 relief before this action became moot—do not qualify as “prevailing par-
 t[ies]” eligible for attorney's fees under § 1988(b) because no court con-
 clusively resolved their claims by granting enduring judicial relief on
 the merits that materially altered the legal relationship between the
 parties. Pp. 199–208.
    (a) Under the “American Rule,” a prevailing litigant is ordinarily not
 entitled to collect attorney's fees from the loser absent express statu-
 tory authorization. See Alyeska Pipeline Service Co. v. Wilderness So-
 ciety, 421 U. S. 240, 249. Congress has provided that in actions brought
 under certain civil rights statutes—including 42 U. S. C. § 1983—“the
 court, in its discretion, may allow the prevailing party, other than the
 United States, a reasonable attorney's fee as part of the costs.”
 § 1988(b).
    To determine whether the drivers here qualify as “prevailing par-
 t[ies]” under § 1988(b), the Court begins with the statute's text. The
 Court has recognized “prevailing party” as a legal term of art. Buck-
                      Cite as: 604 U. S. 192 (2025)                      193

                                 Syllabus

 hannon Board & Care Home, Inc. v. West Virginia Dept. of Health and
 Human Resources, 532 U. S. 598, 603. When § 1988(b) was adopted,
 contemporary dictionaries defned a prevailing party as one who suc-
 cessfully maintains its claim when the matter is fnally resolved. See
 Black's Law Dictionary 1352 (rev. 4th ed. 1968); Ballentine's Law Dic-
 tionary 985 (3d ed. 1969).
    Preliminary injunctions do not make a party “prevailing” because
 they do not conclusively decide the case on the merits. Such injunc-
 tions only determine if a plaintiff is likely to succeed, along with factors
 such as irreparable harm, the balance of equities, and the public interest.
 See Winter v. Natural Resources Defense Council, Inc., 555 U. S. 7, 20.
 The purpose of a preliminary injunction is to preserve the status quo
 until a trial can occur, see University of Tex. v. Camenisch, 451 U. S.
 390, 395, and external events that render a dispute moot do not convert
 that temporary order into a conclusive adjudication. Pp. 199–202.
    (b) The Court's precedents interpreting § 1988(b) establish that a
 plaintiff “prevails” when a court grants enduring judicial relief that ma-
 terially alters the legal relationship between the parties. Two recent
 decisions emphasize that this change must be both judicially sanctioned
 and enduring. In Buckhannon, the Court rejected the “catalyst the-
 ory”—the theory that a plaintiff may receive attorney's fees under
Page Proof Pending Publication
 § 1988(b) when he “achieves the desired result because the lawsuit
 brought about a voluntary change in the defendant's conduct.” 532
 U. S., at 601. The Court explained that the plaintiff was not a “prevail-
 ing party” because there had been “no judicially sanctioned change in
 the legal relationship of the parties.” Id., at 605. And in Sole v.
 Wyner, 551 U. S. 74, the Court decided that a plaintiff initially granted
 a preliminary injunction after an abbreviated hearing, but denied a per-
 manent injunction after a adjudication on the merits, did not qualify as
 a “prevailing party” within the meaning of § 1988(b) because the plaintiff
 gained no enduring change in the legal relationship between herself and
 the defendants. Id., at 77, 78, 86. The Court's holding in this case—
 that the enduring nature of that change must itself be judicially sanc-
 tioned—follows naturally from Sole and Buckhannon. A plaintiff who
 wins a transient victory on a preliminary injunction does not become a
 “prevailing party” simply because external events convert the transient
 victory into a lasting one. Pp. 202–204.
    (c) The rule established serves the interests of judicial economy. A
 straightforward, bright-line rule is easy to administer, reducing the risk
 of signifcant litigation over attorney's fees. Concerns that government
 defendants who have lost at the preliminary injunction stage will strate-
 gically moot litigation are speculative, and such a risk could arise in only
 a small number of contexts. The judicial role here is limited. Con-
194                      LACKEY v. STINNIE

                                 Syllabus

  gress may amend the statutory language to empower courts to award
  attorney's fees to plaintiffs who have enjoyed some success but have not
  prevailed in a judgment on the merits. Pp. 204–205.
     (d) The drivers' remaining arguments are unpersuasive. The argu-
  ment that § 1988(b) was enacted against a historical backdrop that fa-
  vored awarding interim costs at equity, including for preliminary injunc-
  tions, was rejected by the Court in Alyeska Pipeline. 421 U. S., at 241,
  247. The drivers also contend that the availability of fees in some cases
  while litigation is ongoing suggests that § 1988(b) includes no fnality
  requirement, but the Court's decisions simply indicate that attorney's
  fees may be awarded when conclusive, enduring judicial relief is meted
  out on an incremental basis. Finally, the availability of fees after a
  court-ordered consent decree is consistent with the rule announced here.
  While the decree refects the parties' own resolution of the merits, it is
  approved and given force of law by a court, and it may grant enduring
  relief that materially alters the legal relationship between the parties.
  The dissent confates preliminary judicial relief that becomes irrevers-
  ible by way of mootness with relief that is permanent by virtue of a
  judicial order. Pp. 205–207.
77 F. 4th 200, reversed and remanded.

Page       Proof Pending Publication
 Roberts, C. J., delivered the opinion of the Court, in which Thomas,
Alito, Kagan, Gorsuch, Kavanaugh, and Barrett, JJ., joined. Jack-
son, J., fled a dissenting opinion, in which Sotomayor, J., joined, post,
p. 208.

  Erika L. Maley, Solicitor General of Virginia, argued the
cause for petitioner. With her on the briefs were Jason S.
Miyares, Attorney General of Virginia, Kevin M. Gallagher,
Principal Deputy Solicitor General, Graham K. Bryant, Dep-
uty Solicitor General, M. Jordan Minot, Assistant Solicitor
General, Maya M. Eckstein, Trevor S. Cox, and David M.
Parker.
  Anthony A. Yang argued the cause for the United States
as amicus curiae urging reversal. With him on the brief
were Solicitor General Prelogar, Principal Deputy Assist-
ant Attorney General Boynton, Deputy Solicitor General
Stewart, Charles W. Scarborough, Thomas Pulham, and
Dana Kaersvang.
  Brian D. Schmalzbach argued the cause for respondents.
With him on the brief were Matthew A. Fitzgerald, John J.
                       Cite as: 604 U. S. 192 (2025)                    195

                           Opinion of the Court

Woolard, Jonathan T. Blank, Angela A. Ciolfi, and Patrick
Levy-Lavelle.*
  Chief Justice Roberts delivered the opinion of the
Court.
  Respondents are Virginia drivers whose licenses were sus-
pended due to their failure to pay court fnes or costs. The
   *Briefs of amici curiae urging reversal were fled for the State of Geor-
gia et al. by Christopher M. Carr, Attorney General of Georgia, Stephen J.
Petrany, Solicitor General, Ross W. Bergethon, Principal Deputy Solicitor
General, and Paul R. Draper, Deputy Solicitor General, and by the Attor-
neys General for their respective States as follows: Steve Marshall of Ala-
bama, Tim Griffn of Arkansas, Ashley Moody of Florida, Raúl R. Labra-
dor of Idaho, Theodore E. Rokita of Indiana, Brenna Bird of Iowa, Kris
Kobach of Kansas, Elizabeth Murrill of Louisiana, Lynn Fitch of Missis-
sippi, Andrew Bailey of Missouri, Austin Knudsen of Montana, Michael
T. Hilgers of Nebraska, Drew Wrigley of North Dakota, Dave Yost of Ohio,
Gentner Drummond of Oklahoma, Alan Wilson of South Carolina, Marty
J. Jackley of South Dakota, Jonathan Skrmetti of Tennessee, Ken Paxton
Page Proof Pending Publication
of Texas, and Sean Reyes of Utah; for the Local Government Legal Center
et al. by Joshua A. Skinner, Benjamin J. Gibbs, and Alexander J. Lind-
vall; and for the University of Florida Board of Trustees by H. Christo-
pher Bartolomucci and Justin A. Miller.
   Briefs of amici curiae urging affrmance were fled for the Alliance De-
fending Freedom et al. by Allyson N. Ho, Elizabeth A. Kiernan, Christine
A. Budasoff, John J. Bursch, Travis C. Barham, and Cynthia Fleming
Crawford; for the American Civil Liberties Union et al. by Andrew J.
Pincus; for the Christian Legal Society et al. by Douglas Laycock, John
Greil, and Steven T. Collis; for the Constitutional Accountability Center
by Elizabeth B. Wydra, Brianne J. Gorod, and Brian R. Frazelle; for the
Firearms Policy Coalition, Inc., et al. by Cody J. Wisniewski; for the First
Liberty Institute by Kelly J. Shackelford, Jeffrey C. Mateer, David J.
Hacker, Jeremiah G. Dys, and Camille P. Varone; for the Foundation for
Individual Rights and Expression et al. by Joshua A. House and Edward
S. Rudofsky; for the Institute for Free Speech et al. by Alan Gura and
Brett R. Nolan; for the Lawyers' Committee for Civil Rights Under Law
et al. by Damon T. Hewitt, Dariely Rodriguez, Ezra D. Rosenberg,
Thomas Silverstein, Pooja Chaudhuri, Angela M. Liu, and Christopher
J. Merken; and for the New Jersey State Bar Association by Gary S. Stein,
William H. Mergner, Jr., Robert B. Hille, Peter J. Gallagher, and James
A. Lewis V.
196                  LACKEY v. STINNIE

                      Opinion of the Court

drivers sued the Commissioner of the Virginia Department
of Motor Vehicles under 42 U. S. C. § 1983, arguing that the
Virginia statute requiring suspension of their licenses was
unconstitutional. The District Court preliminarily enjoined
the Commissioner from enforcing the statute. But before
the case reached fnal judgment, the Virginia General As-
sembly repealed the challenged law, rendering the action
moot. The question presented is whether the drivers are
“prevailing part[ies]” who qualify for an award of attorney's
fees under § 1988(b).
                             I
   Until recently, a Virginia statute directed the state courts
to suspend the license of any driver who failed to pay “any
fne, costs, forfeitures, restitution, or penalty lawfully as-
sessed against him” for violation of a federal, state, or local
law. Va. Code Ann. § 46.2–395(B) (2016) (repealed 2020).
The suspension remained in force until the amount due was
Page Proof Pending Publication
paid in full or the driver entered into a court-approved pay-
ment plan. Virginia drivers—whose licenses were sus-
pended under the law and who asserted that they could not
afford to pay the fnes or costs or keep up with a payment
plan—sued the Commissioner of the Virginia Department of
Motor Vehicles on their own behalf and on behalf of a puta-
tive class. The drivers alleged that the statute facially vio-
lated the Due Process Clause by “failing to provide suffcient
notice or hearing to any driver before license suspension”
and violated both the Due Process and Equal Protection
Clauses “as applied to people who cannot afford to pay due
to their modest fnancial circumstances.” First Amended
Class Action Complaint in Stinnie v. Holcomb, No.
3:16−cv−00044 (WD Va., Sept. 11, 2018), ECF Doc. 84, pp.
2−3; see also id., at 37−43. The drivers sought declaratory
relief, preliminary and permanent injunctive relief, and at-
torney's fees under 42 U. S. C. § 1988(b).
   In December 2018, the District Court granted a prelimi-
nary injunction, prohibiting the Commissioner from enforc-
                   Cite as: 604 U. S. 192 (2025)            197

                      Opinion of the Court

ing the statute against the drivers or future class members.
See Stinnie v. Holcomb, 355 F. Supp. 3d 514, 520 (WD Va.
2018). The court explained that the drivers had made “a
clear showing that [they were] likely to succeed” on their
procedural due process claim, though it noted that they need
not “establish a certainty of success.” Id., at 527 (quoting
Di Biase v. SPX Corp., 872 F. 3d 224, 230 (CA4 2017)). The
court also determined that the remaining preliminary injunc-
tion factors—the risk of irreparable harm, the balance of eq-
uities, and the public interest—weighed in the drivers' favor.
Stinnie, 355 F. Supp. 3d, at 532; see Winter v. Natural Re-
sources Defense Council, Inc., 555 U. S. 7, 20 (2008). The
Commissioner did not appeal the grant of the preliminary
injunction.
   In April 2019, about four months before a bench trial was
scheduled to begin, the Commissioner moved to dismiss as
moot or, in the alternative, stay the case. See Stinnie v.
Page Proof Pending Publication
Holcomb, 396 F. Supp. 3d 653, 656 (WD Va.). The Virginia
General Assembly had recently adopted Budget Amendment
No. 33, which “eliminate[d] the suspension of drivers' li-
censes for failure to pay court fnes and costs through July
1, 2020, but [did] not repeal § 46.2–395.” Ibid. The Com-
missioner represented that the General Assembly was likely
to repeal the law during the next legislative session. The
District Court granted a stay, reasoning in part that doing
so served the interests of judicial economy and enabled the
court to avoid “weigh[ing] in on sensitive constitutional ques-
tions about license suspension schemes about which other
courts ha[d] disagreed.” Id., at 660.
   In April 2020, the Virginia General Assembly repealed
§ 46.2–395 and required the permanent reinstatement of li-
censes suspended under the law. See 2020 Va. Acts ch. 965.
As a result, the parties agreed that the action had become
moot and stipulated to dismissal. The drivers, however, as-
serted that they were entitled to attorney's fees under
§ 1988(b), so the parties jointly requested that the court re-
198                  LACKEY v. STINNIE

                      Opinion of the Court

tain jurisdiction to resolve that dispute. The District Court
declined to award attorney's fees, following Smyth v. Rivero,
282 F. 3d 268 (CA4 2002). See Stinnie v. Holcomb, 2021 WL
2292807 (WD Va., June 4, 2021). In Smyth the Fourth Cir-
cuit held that a plaintiff awarded a preliminary injunction is
not a “prevailing party” within the meaning of § 1988(b).
282 F. 3d, at 277. A Fourth Circuit panel affrmed, again
relying on Smyth. Stinnie v. Holcomb, 37 F. 4th 977 (2022).
Judge Harris concurred, suggesting that the Circuit may
wish to reconsider that precedent. Id., at 983.
   The Fourth Circuit did so, rehearing the case en banc and
overturning its decision in Smyth. Stinnie v. Holcomb, 77
F. 4th 200 (2023). It observed that Smyth had become the
“outlier” among the courts of appeals. 77 F. 4th, at 209. It
reasoned that some preliminary injunctions “provide endur-
ing, merits-based relief that satisfes all the requisites of the
prevailing party standard.” Id., at 203. And it explained,
Page Proof Pending Publication
in light of this Court's decision in Winter v. Natural Re-
sources Defense Council, that a plaintiff could no longer pre-
vail on a preliminary injunction for reasons that “had virtu-
ally nothing to do with the merits of her claim.” 77 F. 4th,
at 208−209; see Winter, 555 U. S., at 20 (clarifying that a
fnding of likely success on the merits is a prerequisite to
preliminary injunctive relief). Finally, it noted that Con-
gress had enacted § 1988(b) in the interest of facilitating the
redress of civil rights grievances. 77 F. 4th, at 210.
   The en banc court articulated a new standard: “When a
preliminary injunction provides the plaintiff concrete, irre-
versible relief on the merits of her claim and becomes moot
before fnal judgment because no further court-ordered as-
sistance proves necessary, the subsequent mootness of the
case does not preclude an award of attorney's fees.” Ibid.
Applying that standard, the en banc court vacated and re-
manded the case to allow the District Court to determine a
reasonable fee. Id., at 218. Judge Quattlebaum dissented,
arguing that a preliminary injunction does not constitute a
                   Cite as: 604 U. S. 192 (2025)            199

                      Opinion of the Court

judicial decision on the merits and that a fee award on the
basis of such an injunction therefore conficts with both the
text of § 1988(b) and this Court's precedents. See id., at 225,
227, 231.
  We granted certiorari to determine whether the term
“prevailing party” in § 1988(b) encompasses a party who is
awarded a preliminary injunction, if the case becomes moot
before the court reaches a fnal judgment. 601 U. S. 1161
(2024).
                               II
   Since 1796, this Court has maintained that “the Judiciary
itself would not create a general rule, independent of any
statute, allowing awards of attorneys' fees in federal courts.”
Alyeska Pipeline Service Co. v. Wilderness Society, 421 U. S.
240, 249 (1975) (citing Arcambel v. Wiseman, 3 Dall. 306
(1796)). The principle that “the prevailing litigant is ordi-
narily not entitled to collect a reasonable attorneys' fee from
Page Proof Pending Publication
the loser” became known as the “American Rule.” Alyeska
Pipeline, 421 U. S., at 247. Federal courts may depart from
this rule only when “there is express statutory authoriza-
tion” to do so. Hensley v. Eckerhart, 461 U. S. 424, 429
(1983).
   In 1976, Congress adopted the Civil Rights Attorney's
Fees Awards Act. 90 Stat. 2641. The law provides that, in
actions brought under certain civil rights statutes—includ-
ing 42 U. S. C. § 1983—“the court, in its discretion, may allow
the prevailing party, other than the United States, a reason-
able attorney's fee as part of the costs.” § 1988(b). The
question is whether the drivers in this case qualify as “pre-
vailing part[ies]” within the meaning of § 1988(b).

                                A
  When interpreting a statute, we begin with the text. As
we have previously recognized, the phrase “prevailing party”
in § 1988(b) is a “legal term of art.” Buckhannon Board &
Care Home, Inc. v. West Virginia Dept. of Health and
200                  LACKEY v. STINNIE

                      Opinion of the Court

Human Resources, 532 U. S. 598, 603 (2001). We assume
that “when Congress `borrows terms of art in which are ac-
cumulated the legal tradition and meaning of centuries of
practice, it presumably knows and adopts the cluster of ideas
that were attached to each borrowed word.' ” United States
v. Hansen, 599 U. S. 762, 774 (2023) (quoting Morissette v.
United States, 342 U. S. 246, 263 (1952)).
   At the time § 1988(b) was adopted, Black's Law Dictionary
defned “prevailing party” as the party “who successfully
prosecutes the action or successfully defends against it.”
Black's Law Dictionary 1352 (rev. 4th ed. 1968). It ex-
plained that prevailing party status “does not depend upon
the degree of success at different stages of the suit, but
whether, at the end of the suit, or other proceeding, the
party who has made a claim against the other, has success-
fully maintained it.” Ibid.; accord, Ballentine's Law Dic-
tionary 985 (3d ed. 1969). A prevailing party, in other
Page Proof Pending Publication
words, is “[t]he party ultimately prevailing when the matter
is fnally set at rest.” Black's Law Dictionary 1352.
   Preliminary injunctions, however, do not conclusively re-
solve legal disputes. In awarding preliminary injunctions,
courts determine if a plaintiff is likely to succeed on the mer-
its—along with the risk of irreparable harm, the balance of
equities, and the public interest. Winter, 555 U. S., at 20.
“The purpose of a preliminary injunction is merely to pre-
serve the relative positions of the parties until a trial on the
merits can be held,” University of Tex. v. Camenisch, 451
U. S. 390, 395 (1981), and “to balance the equities as the liti-
gation moves forward,” Trump v. International Refugee As-
sistance Project, 582 U. S. 571, 580 (2017) (per curiam).
“Crafting a preliminary injunction is an exercise of discre-
tion and judgment, often dependent as much on the equities
of a given case as the substance of the legal issues it pre-
sents.” Id., at 579. Such relief is also “customarily granted
on the basis of procedures that are less formal and evidence
that is less complete than in a trial on the merits.” Camen-
                   Cite as: 604 U. S. 192 (2025)            201

                      Opinion of the Court

isch, 451 U. S., at 395. As a result, we have previously cau-
tioned against “improperly equat[ing] `likelihood of success'
with `success' ” and treating preliminary injunctions as “tan-
tamount to decisions on the underlying merits.” Id., at 394.
   The transient nature of preliminary injunctions is most ap-
parent when a court reaches a different conclusion upon full
consideration of the merits. For example, in one of our
more recent cases interpreting § 1988, Sole v. Wyner, 551
U. S. 74, 78–79 (2007), protesters sought a preliminary in-
junction against a state regulation of beach attire in order
to assemble nude in the form of a peace sign. The day after
the complaint was fled, the District Court held a hearing
and granted the preliminary injunction. Id., at 79. The
preliminary injunction permitted the protest to occur and
thus preserved the participants' rights until a fnal determi-
nation could be made on the merits of their claim. Ulti-
mately, however, the court declined to award a permanent
Page Proof Pending Publication
injunction, ruling that the regulation was no more burden-
some than necessary to protect the public. Id., at 80−81.
   Because preliminary injunctions do not conclusively re-
solve the rights of parties on the merits, they do not confer
prevailing party status. A plaintiff who secures a prelimi-
nary injunction has achieved only temporary success at an
intermediary “stage[ ] of the suit.” Black's Law Dictionary
1352. It cannot yet be said that he will “ultimately prevail[ ]
when the matter is fnally set at rest” or that he will have
“successfully maintained” his claim “at the end.” Ibid.
And external events that render a dispute moot do not con-
vert a temporary order designed to preserve the status of
the parties into a conclusive adjudication of their rights.
   The Fourth Circuit en banc was persuaded that “Winter's
stringent merits requirement” avoided the “risk” that “a
plaintiff may prevail, and thus be entitled to fees, based on
a preliminary injunction that had virtually nothing to do
with the merits of her claim.” 77 F. 4th, at 209. But it is
not enough that Winter guarantees a preliminary injunction
202                  LACKEY v. STINNIE

                      Opinion of the Court

award has at least something to do with the merits. The
plaintiff must succeed on the merits.

                               B
   This conclusion is consistent with our precedents inter-
preting § 1988(b). We have held that, for the purposes of
§ 1988(b), a plaintiff “prevails” when a court grants enduring
judicial relief that constitutes a “material alteration of the
legal relationship of the parties.” Texas State Teachers
Assn. v. Garland Independent School Dist., 489 U. S. 782,
792−793 (1989). For example, we have ruled that a plaintiff
may qualify as a “prevailing party” based on an award of
nominal damages, Farrar v. Hobby, 506 U. S. 103, 112 (1992),
or a fnal victory on a material even if not predominant claim,
Texas State Teachers Assn., 489 U. S., at 791−793. By con-
trast, a party does not qualify as a “prevailing party” when
a court of appeals overturns directed verdicts and discovery
Page Proof Pending Publication
orders entered against him, Hanrahan v. Hampton, 446 U. S.
754, 756 (1980) (per curiam), or when a court enters a declar-
atory judgment but does not modify the defendant's behavior
toward the plaintiff, Rhodes v. Stewart, 488 U. S. 1, 3−4
(1988) (per curiam) (holding that no fees were available
under § 1988 when the judgment afforded no relief to the
plaintiff due to mootness).
   Two of our more recent decisions highlight the require-
ments that the change in legal relationship be judicially sanc-
tioned and enduring. In Buckhannon Board & Care Home,
Inc. v. West Virginia Department of Health and Human Re-
sources, we rejected the “catalyst theory”—the theory that
a plaintiff may receive attorney's fees under § 1988(b) when
he “achieves the desired result because the lawsuit brought
about a voluntary change in the defendant's conduct.” 532
U. S., at 601; see id., at 600. In that context, we explained
that the plaintiff was not a “prevailing party” because there
had been “no judicially sanctioned change in the legal rela-
tionship of the parties.” Id., at 605. The defendant's volun-
                   Cite as: 604 U. S. 192 (2025)            203

                      Opinion of the Court

tary actions “lack[ed] the necessary judicial imprimatur.”
Ibid. We were not persuaded that § 1988(b) “authorizes fed-
eral courts to award attorney's fees to a plaintiff who” fled
a “potentially meritless lawsuit” and “reached the `sought-
after destination' without obtaining any judicial relief.” Id.,
at 606 (quoting id., at 634 (Ginsburg, J., dissenting)).
   In Sole v. Wyner, we decided that “a plaintiff who gain[ed]
a preliminary injunction after an abbreviated hearing, but
[was] denied a permanent injunction after a dispositive adju-
dication on the merits,” did not qualify as a “prevailing
party” within the meaning of § 1988(b). 551 U. S., at 77; see
id., at 78. That plaintiff, we explained, “gained no enduring
change in the legal relationship” between herself and the de-
fendants. Id., at 86 (emphasis added; alterations and inter-
nal quotation marks omitted). Although we left open the
question presented in this case, see ibid., we described the
plaintiff's success at the preliminary injunction stage as
Page Proof Pending Publication
“a transient victory at the threshold of an action,” a “feeting
success” that “did not establish that [the plaintiff] prevailed
on the gravamen of her plea for injunctive relief,” one
“tentative [in] character, in view of the continuation of the
litigation to defnitively resolve the controversy,” id., at 78,
83, 84.
   We recognize that neither opinion resolves this case, but
our holding today follows naturally from these precedents.
In Sole, we established that the change in the legal rela-
tionship between the parties must be “enduring.” Id., at
86. In Buckhannon, we established that the change must
be “judicially sanctioned.” 532 U. S., at 605. Today, we
establish that the enduring nature of that change must itself
be judicially sanctioned. A plaintiff who wins a transient
victory on a preliminary injunction does not become a
“prevailing party” simply because external events convert
the transient victory into a lasting one. Rather, a plaintiff
“prevails” under the statute when a court conclusively re-
solves a claim by granting enduring judicial relief on the
204                      LACKEY v. STINNIE

                          Opinion of the Court

merits that materially alters the legal relationship between
the parties.*
                              C
   The rule we establish today also serves the interests of
judicial economy. A straightforward, bright-line rule is
easy to administer, reducing the risk of “a second major liti-
gation” over attorney's fees. Cf. Hensley, 461 U. S., at 437.
The drivers, however, suggest that our rule promotes sim-
plicity at the cost of creating perverse incentives. They fear
that government defendants who have lost at the prelimi-
nary injunction stage will strategically moot litigation rather
than risk a fee award were they to ultimately lose on the
merits. See Brief for Respondents 42−47. We found simi-
lar concerns to be “entirely speculative” when we rejected
the catalyst theory in Buckhannon, 532 U. S., at 608. We
reiterate that such risk could arise in only a small number of
contexts. After all, if a plaintiff “has a cause of action for
Page Proof Pending Publication
damages, a defendant's change in conduct will not moot the
case.” Id., at 609. And even if the plaintiff seeks only in-
junctive relief, voluntary cessation of the challenged conduct
does not moot an action “unless it is `absolutely clear that
the allegedly wrongful behavior could not reasonably be ex-
pected to recur.' ” Ibid. (quoting Friends of the Earth, Inc.
v. Laidlaw Environmental Services (TOC), Inc., 528 U. S.
167, 189 (2000)); see also FBI v. Fikre, 601 U. S. 234, 241
(2024) (characterizing this burden as “formidable” (quoting
Friends of the Earth, 528 U. S., at 190)). A survey asking
public interest organizations to self-report on the impact of

   *A different body of caselaw addresses when a defendant is a “prevail-
ing party” for the purposes of other fee-shifting statutes. Our decision
today should not be read to affect our previous holding that a defendant
need not obtain a favorable judgment on the merits to prevail, nor to
address the question we left open of whether a defendant must obtain a
preclusive judgment in order to prevail. See CRST Van Expedited, Inc.
v. EEOC, 578 U. S. 419, 431−434 (2016). As we have explained, “[p]lain-
tiffs and defendants come to court with different objectives.” Id., at 431.
                   Cite as: 604 U. S. 192 (2025)            205

                      Opinion of the Court

Buckhannon does not change our minds. See post, at 224
(Jackson, J., dissenting).
   It is Congress's job to craft policy and ours to interpret
the words that codify it. “Atextual judicial supplementation
is particularly inappropriate when . . . Congress has shown
that it knows how to adopt the omitted language or provi-
sion.” Rotkiske v. Klemm, 589 U. S. 8, 14 (2019). Congress
has shown that it knows how to empower courts to award
attorney's fees to plaintiffs who have enjoyed some success
but have not prevailed in a judgment on the merits. In the
Freedom of Information Act, for example, Congress author-
ized courts to assess attorney's fees when a complainant has
“substantially prevailed,” even if through “a voluntary or
unilateral change in position by the agency.” 5 U. S. C.
§ 552(a)(4)(E). If Congress determines that the rule we
adopt today is unwise, it may amend the statutory lan-
guage—just as it enacted § 1988(b) itself in response to our
decision in Alyeska Pipeline Service Co. v. Wilderness Soci-
Page Proof Pending Publication
ety. 421 U. S. 240; see Hensley, 461 U. S., at 429. Until
then, “it is of course our job to apply faithfully the law Con-
gress has written.” Henson v. Santander Consumer USA
Inc., 582 U. S. 79, 89 (2017).

                                D
   The drivers urge the opposite conclusion, but we fnd their
arguments unpersuasive.
   First, the drivers, joined by the dissent, argue that the
dictionary defnitions support them. But they assume that
the favorable resolution of a dispute is tantamount to success
on a claim in a legal action. A “prevailing party,” however,
is defned in the latter sense—one who “successfully prose-
cutes the action,” who has “made a claim” against another
and “has successfully maintained it.” Black's Law Diction-
ary 1352.
   Second, the drivers and dissent contend that § 1988(b) was
enacted against a historical backdrop that favored awarding
206                  LACKEY v. STINNIE

                      Opinion of the Court

interim costs at equity, including for preliminary injunctions.
See Brief for Respondents 19−21. The dissent in Alyeska
Pipeline similarly invoked “the well-established power of
federal equity courts to award attorneys' fees when the in-
terests of justice so require.” 421 U. S., at 272 (Marshall,
J., dissenting). We rejected that argument, however, and
determined that the American Rule supplied the default rule
at law and equity, subject to narrow historical exceptions not
at issue here. See id., at 241, 247 (majority opinion).
   Next, the drivers argue that the availability of fees while
litigation is ongoing suggests that § 1988(b) includes no fnal-
ity requirement. See Brief for Respondents 40−42. The
dissent likewise points to our statement in Buckhannon that
a “ `prevailing party' is not intended to be limited to the vic-
tor only after entry of a fnal judgment following a full trial
on the merits.” 532 U. S., at 607 (quoting H. R. Rep. No.
94–1558, p. 7 (1976)); see post, at 221. We have recognized
Page Proof Pending Publication
that “Congress contemplated the award of fees pendente lite
in some cases.” Hanrahan, 446 U. S., at 757. For example,
we have explained that, in school desegregation cases, “many
fnal orders may issue in the course of the litigation” because
injunctive relief “must prove its effcacy . . . over a period
of time and often with frequent modifcations.” Bradley v.
School Bd. of Richmond, 416 U. S. 696, 723 (1974). Our deci-
sions simply indicate that attorney's fees may be awarded
when conclusive, enduring judicial relief is meted out on an
incremental basis. Hanrahan, 446 U. S., at 758 (“Congress
intended to permit the interim award of counsel fees only
when a party has prevailed on the merits of at least some of
his claims.”). Key language on which the dissent relies—
our statement that a party prevails when it “succeed[s] on
any signifcant claim affording it some of the relief sought,”
including relief on the merits pendente lite—explained our
rejection of the “central issue test,” which would have re-
quired a party to prevail on its central claim in order to be
awarded attorney's fees. Texas State Teachers Assn., 489
                   Cite as: 604 U. S. 192 (2025)           207

                      Opinion of the Court

U. S., at 791; see post, at 211. It did not refer to prelimi-
nary relief.
   The availability of fees following the entry of a court-
ordered consent decree is fully consistent with the rule we
announce today. A consent decree refects the parties' own
resolution of the merits, but it is approved and given force
of law by the court. See Firefghters v. Cleveland, 478 U. S.
501, 523 (1986). Violation of a consent decree is enforceable
by a citation for contempt. Ibid. So a consent decree is
like a fnal judgment in the relevant ways: It conclusively
resolves the claim, bears a judicial imprimatur, and may
grant enduring relief that materially alters the legal re-
lationship between the parties. That is why “[w]e have only
awarded attorney's fees where the plaintiff has received
a judgment on the merits or obtained a court-ordered con-
sent decree.” Buckhannon, 532 U. S., at 605 (citation omit-
ted). For its part, the dissent confates preliminary judicial
relief that becomes irreversible by way of mootness with re-
Page Proof Pending Publication
lief that is permanent by virtue of a judicial order. See
post, at 217−218. That a preliminary order may sometimes
“function[ ] . . . like” a fnal order due to external circum-
stances, see post, at 218, is not dispositive of the nature of
the order.
                           *    *    *
   Section 1988(b) permits courts to award attorney's fees to
a “prevailing party.” A party “prevails” when a court con-
clusively resolves his claim by granting enduring relief on
the merits that alters the legal relationship between the par-
ties. Critically, both the change in relationship and its per-
manence must result from a judicial order. A preliminary
injunction, which temporarily preserves the parties' litigat-
ing positions based in part on a prediction of the likelihood
of success on the merits, does not render a plaintiff a “pre-
vailing party.” Nor do external events that moot the action
and prevent the court from conclusively adjudicating the
claim. Because the drivers in the present case gained only
208                   LACKEY v. STINNIE

                      Jackson, J., dissenting

preliminary injunctive relief before this action became moot,
they do not qualify as “prevailing part[ies]” eligible for attor-
ney's fees under § 1988(b).
  The judgment of the Court of Appeals for the Fourth Cir-
cuit is reversed, and the case is remanded for further pro-
ceedings consistent with this opinion.
                                               It is so ordered.

  Justice Jackson, with whom Justice Sotomayor joins,
dissenting.
   Congress has authorized courts to award attorney's fees
to the “prevailing party” in certain civil rights cases. 42
U. S. C. § 1988(b). Today, the Court holds that a plaintiff
who secures a preliminary injunction does not “prevail”
under this fee-shifting statute, even when the preliminary
injunction provides meaningful relief and is never reversed
on the merits. The Court maintains that this holding “fol-
Page Proof Pending Publication
lows naturally from” our precedents. Ante, at 203. But
that will come as a surprise to the 11 Courts of Appeals that
have previously considered this issue; all of them agree that
at least some preliminary injunctions trigger fee eligibility
under § 1988(b).
   Stated simply, the majority's categorical preclusion of fee
awards for any plaintiff who successfully obtains preliminary
injunctive relief is unwarranted. It lacks any basis in the
text of § 1988(b) and is plainly inconsistent with that statu-
tory provision's clear objective, which is to encourage attor-
neys to fle civil rights actions on behalf of the most vulnera-
ble people in our society. The Court has now eliminated fee
eligibility for all preliminary injunctions—even those that
effectively resolve the case. But if Congress had meant for
“prevailing party” status to hinge entirely on the “conclu-
sive” nature of a judicial order, it could easily have said so.
It is the role of Congress, not this Court, to weigh concerns
about administrative ease against the benefts of guaran-
                   Cite as: 604 U. S. 192 (2025)             209

                      Jackson, J., dissenting

teeing individuals an opportunity to vindicate their civil
rights.
  There is no persuasive reason to believe that Congress
meant to preclude fee awards for every plaintiff who secures
preliminary injunctive relief but not a fnal judgment, no
matter the context. Therefore, I respectfully dissent.

                                I
                                A
   Nothing in § 1988(b)'s text compels the conclusion that a
plaintiff who obtains preliminary injunctive relief is never
eligible for a fee award. Section 1988(b) states simply that,
in actions to enforce certain civil rights statutes, including
42 U. S. C. § 1983, “the court, in its discretion, may allow the
prevailing party, other than the United States, a reasonable
attorney's fee as part of the costs.” § 1988(b). The major-
ity recognizes that “prevailing party” is a legal term of art
Page Proof Pending Publication
and begins its analysis by asserting that this term means
what legal dictionaries said it meant at the time that
§ 1988(b) was enacted.
   According to the majority's preferred dictionary, a “pre-
vailing party” is one “ `who successfully prosecutes the action
or successfully defends against it.' ” Ante, at 200 (quoting
Black's Law Dictionary 1352 (rev. 4th ed. 1968)). Thus, pre-
vailing party status turns on “ `whether, at the end of the
suit, or other proceeding, the party who has made a claim
against the other, has successfully maintained it.' ” Ante,
at 200 (quoting Black's Law Dictionary, at 1352). Reasoning
from this defnition, the majority holds that preliminary in-
junctions, which provide interim relief by their nature, can
never confer prevailing party status because they do not
“conclusively resolve the rights of parties on the merits.”
Ante, at 201.
   But the majority's analysis inexplicably confates the re-
quirement for success when the suit ends (which is what the
dictionary defnition says) with a requirement that the suit
210                  LACKEY v. STINNIE

                      Jackson, J., dissenting

end by virtue of a “conclusive” judicial ruling on the merits
of the plaintiff's claims (which is nowhere in Black's Law
Dictionary or anywhere else). In other words, the majori-
ty's reasoning elides the fact that a suit can end in various
ways—including through acts of the defendant or others that
moot the legal action. Black's Law Dictionary and its con-
temporaries simply require a court determining eligibility
for a fee award to take stock of where things stand at the end
of the lawsuit. A prevailing party for § 1988(b) purposes is
one who has successfully maintained his claim (in the manner
I describe below, see Part II–A, infra) “when the matter is
fnally set at rest.” Black's Law Dictionary, at 1352.
   In essence, then, the majority errs by assuming that the
only kind of resolution to a suit that can precipitate a fee
award is a “conclusive” fnal judgment on the merits. See,
e. g., ante, at 200–201, 203, 206. That assumption is un-
founded. The text of the fee statute does not require a fnal
Page Proof Pending Publication
judgment in the party's favor, “conclusive” or otherwise.
Nor does any dictionary defnition of “prevailing party” to
which the majority cites. Rather, according to Black's Law
Dictionary, a “prevailing party” is simply a “part[y] to a suit
who successfully prosecutes the action or successfully de-
fends against it, prevailing on the main issue, even though
not to the extent of his original contention.” Black's Law
Dictionary, at 1352. Ballentine's Law Dictionary is substan-
tially similar; it defnes “prevailing party” as “[t]he party
who is successful or partially successful in an action, so as to
be entitled to costs.” Ballentine's Law Dictionary 985 (3d
ed. 1969).
   Signifcantly for present purposes, both dictionaries fur-
ther emphasize that “[t]o be [a prevailing party] does not de-
pend upon the degree of success at different stages of the
suit, but whether, at the end of the suit . . . the party who
has made a claim against the other, has successfully main-
tained it.” Black's Law Dictionary, at 1352; accord, Ballen-
tine's Law Dictionary, at 985. Yet, today, the majority de-
                       Cite as: 604 U. S. 192 (2025)                    211

                          Jackson, J., dissenting

mands that, in order to prevail, the party must have achieved
a certain degree of success at a certain point in the case: a
conclusive fnal judgment in his favor at the end of litigation.

                                    B
   This Court has not previously linked prevailing party
status to securing a conclusive fnal judgment. Quite to
the contrary, we have held that a prevailing party for fee-
shifting purposes is one who has “succeeded on any signif-
cant claim affording it some of the relief sought, either pen-
dente lite”—i. e., pending the suit—“or at the conclusion of
the litigation.” Texas State Teachers Assn. v. Garland In-
dependent School Dist., 489 U. S. 782, 791 (1989). That is, a
plaintiff prevails when he accomplishes his lawsuit's “objec-
tiv[e],” which is to achieve “a material alteration in the legal
relationship between the parties.” CRST Van Expedited,
Inc. v. EEOC, 578 U. S. 419, 431 (2016). This is because, for
Page Proof Pending Publication
a plaintiff, “[a]t the end of the rainbow lies not a judgment,
but some action (or cessation of action) by the defendant that
the judgment produces—the payment of damages, or some
specifc performance, or the termination of some conduct.”
Hewitt v. Helms, 482 U. S. 755, 761 (1987).
   A plaintiff who secures a preliminary injunction awarding
actual relief on the merits of his claim that is never reversed
by a fnal decision of the court has “successfully maintained”
his claim “at the end.” Black's Law Dictionary, at 1352.
Such a plaintiff has achieved what he has “come to court”
for—the desired “alteration in the legal relationship between
the parties.” CRST, 578 U. S., at 431.1
   Take this case, for example. At the point it ended—when
the District Court dismissed the litigation as moot—re-
   1
     There are, of course, other kinds of preliminary injunctive orders, in-
cluding orders that maintain the status quo. All that is necessary to re-
ject the majority's categorical rule is the recognition that at least some
preliminary injunctions afford the type of material change that confers
prevailing party status.
212                  LACKEY v. STINNIE

                      Jackson, J., dissenting

spondents had secured a preliminary injunction against the
Commissioner of the Virginia Department of Motor Vehicles.
That order enabled respondents to drive their cars on Vir-
ginia's highways for 16 months, over the Commissioner's ob-
jection. And, because the District Court's interim award
had facilitated respondents' access to the road as licensed
drivers, they had prevailed on the merits of their claim in
every meaningful sense. Put another way, “at the end of
the litigation,” respondents did not “leav[e] the courthouse
emptyhanded.” Sole v. Wyner, 551 U. S. 74, 78 (2007). In-
stead, they departed having accomplished exactly what they
had sought to achieve. The fact that respondents achieved
their goal via a preliminary court ruling, as opposed to a
fnal judgment, is irrelevant, for “[n]othing in the language
of § 1988 conditions the District Court's power to award fees
on full litigation of the issues or on a judicial determination
that the plaintiff's rights have been violated.” Maher v.
Page Proof Pending Publication
Gagne, 448 U. S. 122, 129 (1980) (emphasis added).
   Juxtapose that reality with the text of other statutes that
make “prevailing party” status expressly dependent on the
entry of a fnal order. For example, the Emergency School
Aid Act of 1972—enacted just four years before § 1988(b)—
states that, “[u]pon the entry of a fnal order,” a court hear-
ing a school desegregation case may “allow the prevailing
party, other than the United States, a reasonable attorney's
fee as part of the costs.” 20 U. S. C. § 1617 (repealed 1979)
(emphasis added). Several statutes enacted after § 1988(b)
are similarly explicit about when a fee award must be fastened
to a fnal judgment. See, e. g., 28 U. S. C. § 2412(d)(2)(H) (de-
fning “prevailing party” in eminent domain proceedings to
“mea[n] a party who obtains a fnal judgment” of a certain
amount); 15 U. S. C. § 6104(d) (authorizing courts hearing ac-
tions under the Telemarketing and Consumer Fraud and
Abuse Prevention Act to award “reasonable fees . . . to the
prevailing party” upon “issuing any fnal order”). The fact
that § 1988(b) lacks any such language confrms that a conclu-
                      Cite as: 604 U. S. 192 (2025)                  213

                         Jackson, J., dissenting

sive ruling from the court in the form of a fnal judgment is
not a prerequisite for a fee award under that statute.
                                   C
   The majority disregards these important context clues and
focuses instead on a provision of the Freedom of Information
Act (FOIA) that authorizes fee awards for a “complainant”
who “has substantially prevailed” by “obtain[ing] relief
through either—(I) a judicial order, or an enforceable written
agreement or consent decree; or (II) a voluntary or unilateral
change in position by the agency.” 5 U. S. C. § 552(a)(4)(E).
The term “prevailing party” appears nowhere in this FOIA
provision. But, no matter: The majority nevertheless sug-
gests that this is how Congress authorizes fee shifting for
“plaintiffs who have enjoyed some success but have not pre-
vailed in a judgment on the merits.” Ante, at 205.
   The problem is that Congress had a much more targeted
objective when it enacted § 552(a)(4)(E). It sought merely
Page Proof Pending Publication
to repudiate this Court's decision in Buckhannon Board &
Care Home, Inc. v. West Virginia Dept. of Health and
Human Resources, 532 U. S. 598, 606 (2001), which had held
that a plaintiff must obtain some “judicial relief ” to be eligi-
ble for a fee award in FOIA cases.2 Since the point of
§ 552(a)(4)(E) was to “abrogat[e] the rule of Buckhannon in
the FOIA context and reviv[e] the possibility of FOIA fee
awards in the absence of a court decree,” Brayton v. Offce
of U. S. Trade Rep., 641 F. 3d 521, 525 (CADC 2011), that
  2
   Congress enacted 5 U. S. C. § 552(a)(4)(E) because Buckhannon had
empowered Government agencies to “stonewall valid FOIA claims” and
then prevent an award of attorney's fees by “disclosing the documents at
the last moment before judgment,” thereby mooting the case. Brayton
v. Offce of U. S. Trade Rep., 641 F. 3d 521, 525 (CADC 2011). Under
Buckhannon, such plaintiffs were not eligible for fee awards because they
had not obtained any judicial order—preliminary, fnal, or otherwise.
This strategic behavior ensured that FOIA plaintiffs never became eligi-
ble for fee awards despite incurring signifcant costs, so Congress inter-
vened. 641 F. 3d, at 525.
214                       LACKEY v. STINNIE

                          Jackson, J., dissenting

statutory provision sheds no light whatsoever on whether
the term “prevailing party” requires a plaintiff to secure a
conclusive ruling on the merits to qualify as a prevailing
party for purposes of § 1988(b).
   In short, while the majority insists that obtaining a pre-
liminary injunction can never suffce for a fee award under
§ 1988(b) “[b]ecause preliminary injunctions do not conclu-
sively resolve the rights of parties on the merits,” ante, at
201, the text of § 1988(b), contemporary dictionary def-
nitions, and our precedents require far less. All of the
Courts of Appeals to consider the question—11 in total—
understood this and thus correctly held that, for fee-shifting
purposes, it is possible for a party to prevail based on a pre-
liminary ruling.3 The majority's reading of “prevailing
party” in § 1988(b) makes obtaining a court's conclusive fnal
judgment the hallmark of that status in a manner that is
both novel and in many ways anathema to the legal term of
art that Congress actually chose.
Page Proof Pending Publication
                                    II
                                    A
  So what does it take to qualify as a “prevailing party” for
purposes of this fee-shifting statute? In Farrar v. Hobby,
506 U. S. 103 (1992), we explained that a plaintiff “ `prevails' ”
  3
    See, e. g., Haley v. Pataki, 106 F. 3d 478, 484 (CA2 1997); Singer Mgmt.
Consultants, Inc. v. Milgram, 650 F. 3d 223, 229–230, and n. 4 (CA3 2011)
(en banc); Stinnie v. Holcomb, 77 F. 4th 200, 210 (CA4 2023) (en banc) (case
below); Dearmore v. Garland, 519 F. 3d 517, 524 (CA5 2008); Planned
Parenthood Southwest Ohio Region v. Dewine, 931 F. 3d 530, 534 (CA6
2019); Dupuy v. Samuels, 423 F. 3d 714, 723, and n. 4 (CA7 2005); Rogers
Group, Inc. v. Fayetteville, 683 F. 3d 903, 909–910 (CA8 2012); Higher
Taste, Inc. v. Tacoma, 717 F. 3d 712, 717–718 (CA9 2013); Kansas Jud.
Watch v. Stout, 653 F. 3d 1230, 1232, 1238–1239 (CA10 2011); Common
Cause Ga. v. Georgia, 17 F. 4th 102, 107 (CA11 2021); Select Milk Produc-
ers, Inc. v. Johanns, 400 F. 3d 939, 942, 948–949 (CADC 2005). The First
Circuit has not yet considered the issue. See Sinapi v. Rhode Island Bd.
of Bar Examiners, 910 F. 3d 544, 552 (2018).
                    Cite as: 604 U. S. 192 (2025)             215

                      Jackson, J., dissenting

if he receives (1) “actual relief on the merits of his claim” in
a manner that (2) “materially alters the legal relationship
between the parties by modifying the defendant's behavior
in a way that directly benefts the plaintiff.” Id., at 111–
112; see also Lefemine v. Wideman, 568 U. S. 1, 4 (2012) (per
curiam). This test is well established, and it leads inexora-
bly to the conclusion that, in some circumstances, an unre-
versed preliminary injunction can confer prevailing party
status.
   Start with the requirement of a “ `material alteration of
the legal relationship of the parties,' ” which we have repeat-
edly called the “ `touchstone' ” of the prevailing party inquiry.
Sole, 551 U. S., at 82 (quoting Texas State Teachers Assn.,
489 U. S., at 792–793). A plaintiff need not obtain all of the
relief he has requested in the lawsuit to satisfy this require-
ment. Instead, under our precedents, a plaintiff who has
achieved even “ `some of the beneft' ” he sought has secured
Page Proof Pending Publication
the change in the parties' legal relationship necessary to
“cros[s] the threshold to a fee award of some kind.” Id., at
791–792 (quoting Nadeau v. Helgemoe, 581 F. 2d 275, 278–279
(CA1 1978); emphasis added).
   A permanent injunction—just like a declaratory judgment
or a damages award—“will usually satisfy that test,” Lefe-
mine, 568 U. S., at 4, because permanent injunctive relief
generally “affects the behavior of the defendant toward the
plaintiff,” Rhodes v. Stewart, 488 U. S. 1, 4 (1988) (per cu-
riam). At least some preliminary injunctions also qualify.
The preliminary injunction in this case, for example, pro-
vided respondents with actual relief by reinstating their sus-
pended licenses, allowing them to drive without fear of sanc-
tion for failing to repay their fnes and fees. For the roughly
16 months that the preliminary injunction was in place, “that
ruling worked the requisite material alteration in the par-
ties' relationship” by permitting respondents to engage in
conduct that would have been prohibited otherwise. Lefe-
mine, 568 U. S., at 5.
216                   LACKEY v. STINNIE

                      Jackson, J., dissenting

   It is indisputable that the preliminary injunction the Dis-
trict Court issued provided a “direc[t] beneft” to respond-
ents. Farrar, 506 U. S., at 111. That relief was also
awarded “ `on the merits.' ” Lefemine, 568 U. S., at 4 (quoting
Farrar, 506 U. S., at 111–112). We have long taken a “prac-
tical” approach to the merits inquiry in this context. Han-
rahan v. Hampton, 446 U. S. 754, 758 (1980) (per curiam).
Under that approach, relief is granted “on the merits” when
it provides “a resolution of the dispute which changes the
legal relationship between [the plaintiff] and the defendant.”
Texas State Teachers Assn., 489 U. S., at 792 (internal quota-
tion marks omitted).
   Notably, for prevailing party status, we have not required
that a court actually determine whether a legal claim is meri-
torious. The majority acknowledges our holding that the
entry of a consent decree following “the parties' own resolu-
tion of the merits” counts. Ante, at 207; see Farrar, 506
Page Proof Pending Publication
U. S., at 111 (recognizing that a consent decree satisfes the
requirement that the plaintiff “obtain at least some relief on
the merits of his claim”). Indeed, in Maher, we upheld a fee
award based on a consent decree that “did not purport to
adjudicate” the plaintiff's claims at all. 448 U. S., at 126,
n. 8, 129. We have also suggested that default judgments,
which do not involve any assessment of the merits of the
plaintiff 's claims, “almost invariably give rise to fee awards.”
Kirtsaeng v. John Wiley & Sons, Inc., 579 U. S. 197, 208,
n. 3 (2016).
   A court's entry of a preliminary injunction—which does
require a judge to make a preliminary assessment of the
merits—provides a basis for prevailing party status that is
at least as strong as a consent decree or a default judgment.
Plaintiffs seeking the “extraordinary remedy” of a prelimi-
nary injunction must make a “clear showing” that they are
“likely to succeed on the merits.” Winter v. Natural Re-
sources Defense Council, Inc., 555 U. S. 7, 20, 22 (2008).
And the court's decision to order preliminary injunctive re-
                    Cite as: 604 U. S. 192 (2025)              217

                       Jackson, J., dissenting

lief often involves “searching” proceedings, Sole, 551 U. S.,
at 84, even though the “evidence . . . is less complete than in
a trial on the merits,” University of Tex. v. Camenisch, 451
U. S. 390, 395 (1981).
   In this case, the District Court thoroughly assessed the
merits of respondents' claims and granted their request for
preliminary injunctive relief after extensive briefng and an
evidentiary hearing during which multiple witnesses testi-
fed. It blinks reality to suggest that the District Court's
order requiring the Commissioner to give respondents their
licenses back now—based on the court's conclusion that re-
spondents were likely to succeed if this matter proceeded to
trial—is “not the stuff of which legal victories are made.”
Hewitt, 482 U. S., at 760.
   It is no answer to simply declare by ipse dixit that prelimi-
nary injunctions are materially different from consent de-
crees because “a consent decree is like a fnal judgment in
Page Proof Pending Publication
the relevant ways”—i. e., “[i]t conclusively resolves the
claim, bears a judicial imprimatur, and may grant enduring
relief that materially alters the legal relationship between
the parties.” Ante, at 207. The very question before us is
the relevance of this kind of fnality to the prevailing party
determination. And, luckily, that question has already been
answered: Neither the text of § 1988(b) nor any of this
Court's past cases make fee eligibility dependent on the
entry of a conclusive fnal judgment, as I explained above.
   In any event, if a plaintiff need only obtain an order that
is “like a fnal judgment” to prevail, ibid., it is not at all clear
why at least some preliminary injunctions would not count.
Consider, for example, a dispute in which the district court
reviews the evidence and the parties' arguments and enters
the type of preliminary injunction that changes the legal re-
lationship of the parties. The case proceeds but then be-
comes moot such that the litigation ends; the preliminary
injunction is not—and can never be—reversed by a subse-
quent order of the court. In this scenario, all the purport-
218                  LACKEY v. STINNIE

                      Jackson, J., dissenting

edly “relevant” characteristics of a consent decree exist, be-
cause the parties' legal relationship was materially altered
by judicial imprimatur, and that preliminary relief is conclu-
sive insofar as the case has ended and the ruling cannot be
undone by a later determination. In this circumstance, the
preliminary injunction “functions much like the grant of
an irreversible partial summary judgment on the merits,”
Northern Cheyenne Tribe v. Jackson, 433 F. 3d 1083, 1086
(CA8 2006), which all appear to agree would suffce to confer
fee eligibility under § 1988(b).

                                B
   Our decisions in Buckhannon, 532 U. S. 598, and Sole, 551
U. S. 74, are not to the contrary. The majority cites these
two decisions to support its view that obtaining a prelimi-
nary injunction is never suffcient to qualify the recipient for
a fee award under § 1988(b). Ante, at 202–204. But those
Page Proof Pending Publication
cases hold no such thing. Instead, they simply clarify that,
for a plaintiff to prevail, the requisite “change in the legal
relationship of the parties” must be both “judicially sanc-
tioned,” Buckhannon, 532 U. S., at 605, and “enduring,” Sole,
551 U. S., at 86. Neither case mandates the majority's cate-
gorical rule.
   In Buckhannon, this Court rejected the so-called “catalyst
theory,” under which a plaintiff could collect a fee award as
a “prevailing party” without securing any judicial relief so
long as the lawsuit produced “a voluntary change in the de-
fendant's conduct.” 532 U. S., at 601. We held that such a
voluntary change, “although perhaps accomplishing what the
plaintiff sought to achieve by the lawsuit, lacks the necessary
judicial imprimatur on the change” to trigger fee eligibility.
Id., at 605. In Sole, we considered whether a plaintiff who
obtains a preliminary injunction but is subsequently denied
a permanent one prevails for fee purposes under § 1988(b).
551 U. S., at 77. We explained that when a plaintiff 's “initial
victory” at the preliminary injunction stage is “superseded”
                    Cite as: 604 U. S. 192 (2025)             219

                      Jackson, J., dissenting

by a nonfavorable fnal “ruling on the merits,” he does not
qualify as a “prevailing party,” because the relief he received
was not “enduring.” Id., at 84–86.
   A preliminary injunction that mandates a judicially sanc-
tioned legal change in the parties' relationship and is never
reversed by a fnal ruling on the merits satisfes both Buck-
hannon and Sole. A court that issues interim injunctive re-
lief unquestionably gives its “judicial imprimatur” to the
change afforded, as Buckhannon requires. 532 U. S., at 605.
For its part, Sole stands merely for the proposition that a
party can be divested of “prevailing party” status if his “suc-
cess rested on a premise the District Court ultimately re-
jected.” 551 U. S., at 84–86. But Sole is inapposite when a
subsequent fnal decision does not thwart the judge-
sanctioned basis for the preliminary injunction. Indeed,
Sole expressly said so, by specifcally reserving the question
“whether, in the absence of a fnal decision on the merits of
Page Proof Pending Publication
a claim for permanent injunctive relief, success in gaining a
preliminary injunction may sometimes warrant an award of
counsel fees,” id., at 86—the precise issue that is before the
Court today.
   The majority thus overreads our precedents to support its
blanket rule that preliminary injunctions can never support
fee awards. Ante, at 202–204. With respect to Sole in par-
ticular, it is true that we characterized the preliminary injunc-
tion at issue there as “feeting” and “tentative.” 551 U. S.,
at 83–84; see also ante, at 203 (contrasting interim relief with
relief that “last[s]”). But the Sole Court did not tie the re-
quirement for “enduring” relief to the inherent permanence
of the relevant judicial order. Instead, we made crystal
clear that “[o]f controlling importance to our decision” was
the fact that “the eventual ruling on the merits for defend-
ants, after both sides considered the case ft for fnal adjudi-
cation, superseded the preliminary ruling.” 551 U. S., at 84–
85 (emphasis added); see also id., at 78 (observing that a
plaintiff does not prevail if “at the end of the litigation, her
220                  LACKEY v. STINNIE

                     Jackson, J., dissenting

initial success is undone and she leaves the courthouse
emptyhanded”).
   At the end of the day, Sole should be taken to mean only
what it expressly holds: Preliminary injunctive relief that is
subsequently superseded by a fnal judgment reversing the
ruling does not endure for fee-shifting purposes. Here, the
preliminary injunction provided actual relief to respondents
for more than 16 months, and there was no Sole-like sup-
planting of that preliminary relief by a subsequent court
order.
                             III
                               A
   In addition to misinterpreting the text of § 1988(b) and
misconstruing our precedents, the majority ignores Con-
gress's clear intent to expand access to justice. It is puz-
zling, to say the least, that the majority seems to go out of
its way to adopt a rule that categorically prohibits fee shift-
Page Proof Pending Publication
ing while interpreting a statute that expressly authorizes
fee awards.
   There is no dispute that Congress enacted § 1988(b) “for a
specifc purpose”: to respond to this Court's decision in Aly-
eska Pipeline Service Co. v. Wilderness Society, 421 U. S.
240 (1975), which had rejected the “former equitable practice
of awarding attorney's fees to the prevailing party in certain
civil rights cases.” Farrar, 506 U. S., at 118 (O'Connor, J.,
concurring). The Alyeska Court held that, absent statutory
authorization, courts should not depart from the “ `American
Rule,' ” under which litigants ordinarily bear their own at-
torney's fees. 421 U. S., at 247. Congress swiftly enacted
§ 1988(b) in Alyeska's wake to codify a civil rights exception
to the American Rule. The majority does not, and cannot,
dispute that Congress's intent was “to ensure `effective ac-
cess to the judicial process' for persons with civil rights
grievances.” Hensley v. Eckerhart, 461 U. S. 424, 429 (1983)
(quoting H. R. Rep. No. 94–1558, p. 1 (1976)).
                   Cite as: 604 U. S. 192 (2025)             221

                      Jackson, J., dissenting

    Consistent with that “clear congressional intent,” this
Court has previously recognized that fee awards should be
available to “partially prevailing civil rights plaintiffs.”
Texas State Teachers Assn., 489 U. S., at 790. This principle
is, in fact, readily apparent from the statute's enactment his-
tory. See Buckhannon, 532 U. S., at 607. The history dem-
onstrates that the question of awarding fees for success
based on interim orders was not overlooked by the legisla-
ture; to the contrary, Congress specifcally “contemplated the
award of fees pendente lite,” at least where a party “has
established his entitlement to some relief on the merits of
his claims.” Hanrahan, 446 U. S., at 757 (citing S. Rep. No.
94–1011, p. 5 (1976); H. R. Rep. No. 94–1558, at 7–8).
    The majority says that Congress merely wanted § 1988(b)
to authorize fee awards when “conclusive, enduring judicial
relief is meted out on an incremental basis.” Ante, at 206.
But that is not what the historical record establishes, and
Buckhannon fatly rejects this contention. There, we spe-
Page Proof Pending Publication
cifcally observed that, per § 1988(b)'s legislative history,
“ ` “prevailing party” is not intended to be limited to the vic-
tor only after entry of a fnal judgment following a full trial
on the merits.' ” 532 U. S., at 607 (quoting H. R. Rep. No.
94–1558, at 7); see also Hanrahan, 446 U. S., at 756–757.
The legislative history is likewise unequivocal that a prevail-
ing party for § 1988(b) purposes should “also include a liti-
gant who succeeds even if the case is concluded prior to a
full evidentiary hearing before a judge or jury.” H. R. Rep.
No. 94–1558, at 7.
                                B
  Nor could a Congress that wished to authorize fee awards
for civil rights victories have intended the absurdities that
will result from the majority's categorical preclusion of pre-
liminary injunctive relief from § 1988(b). To state the obvi-
ous, the majority's bright-line rule lacks the nuance that is
needed to account for the various circumstances in which a
preliminary injunction may be “preliminary” in name only.
222                  LACKEY v. STINNIE

                     Jackson, J., dissenting

   One example is the plaintiff who requests a preliminary
injunction to achieve an interim result, given the timeframe
at issue. “When protesters seek an injunction to exercise
their First Amendment rights at a specifc time and place—
say to demonstrate at a Saturday parade—a preliminary in-
junction will give them all the court-ordered relief they need
and the end of the parade will moot the case.” McQueary
v. Conway, 614 F. 3d 591, 599 (CA6 2010). Thus, the Courts
of Appeals regularly hold that plaintiffs who successfully ob-
tain a preliminary injunction that permits them to engage in
the otherwise prohibited conduct “prevail” for fee-shifting
purposes. See, e. g., Young v. Chicago, 202 F. 3d 1000, 1000–
1001 (CA7 2000) (per curiam) (awarding fees to plaintiffs
who obtained a preliminary injunction to protest a political
convention even though the “suit became moot before a de-
fnitive determination of its merits” could be made).
   In its rush to carve preliminary injunctions out of
Page Proof Pending Publication
§ 1988(b), the majority also overlooks situations in which
courts have, in fact, conclusively resolved the merits of a
plaintiff 's claims at the preliminary injunction stage. A
trial court might defnitively determine that a law is “ ` “fa-
cially unconstitutional” ' ” in the course of granting prelimi-
nary relief, for example. Singer Mgmt. Consultants, Inc. v.
Milgram, 650 F. 3d 223, 229–230, and n. 4 (CA3 2011) (en
banc) (quoting People Against Police Violence v. Pittsburgh,
520 F. 3d 226, 229 (CA3 2008)). But the majority nonethe-
less adopts a sweeping rule under which preliminary injunc-
tions can never be the basis for fee eligibility.
   And to what end? The majority seeks to justify its broad
holding on the grounds that it discourages fee disputes and
thereby “serves the interests of judicial economy.” Ante,
at 204. But concerns about judicial administration cannot
supplant Congress's clear intent to promote access to justice
via fee shifting in civil rights cases.
   What is more, it is actually the majority's categorical rule
that will promote wasteful litigation and incentivize litigants
                    Cite as: 604 U. S. 192 (2025)             223

                      Jackson, J., dissenting

to manipulate fee liability. Under the majority's rule, a
plaintiff who has incurred substantial attorney's fees in order
to secure a preliminary injunction that provides all the relief
he needs will face a choice: He may either concede that the
litigation has run its course and pay his own fees, or he may
seek to litigate the case to fnal judgment in order to secure
a fee award. No one would blame a plaintiff with a strong
case for choosing the latter option. But such additional liti-
gation is an ineffcient waste of judicial resources if the plain-
tiff has already achieved his objective at an earlier part of
the case.
   Worse still, the majority's rule appears to preference con-
servation of judicial resources over the maintenance of meri-
torious civil rights lawsuits, to the extent that excluding
preliminary injunctive relief from § 1988(b) facilitates the
strategic mooting of cases by defendants to avoid paying at-
torney's fees. This case illustrates precisely that problem.
Page Proof Pending Publication
After a robust evidentiary hearing, the District Court issued
a comprehensive opinion that preliminarily enjoined the
Commissioner from enforcing the challenged law against re-
spondents. Seeing the writing on the wall, the Commis-
sioner sought and obtained a stay of the case—over respond-
ents' objections—based on his representation that the
legislature was likely to repeal the challenged law. The
Commissioner then successfully lobbied the legislature to re-
peal the legislation, emphasizing that doing so would, in his
words, “result in [respondents'] pending litigation being dis-
missed, relieving the Department from continuing to incur
costly legal fees.” App. 409.
   As the Fourth Circuit observed, precluding fee shifting
in this scenario is manifestly inequitable, because it leaves
respondents “holding the bag” for considerable litigation fees
despite—and largely because of—their having succeeded in
obtaining preliminary relief. Stinnie v. Holcomb, 77 F. 4th
200, 210 (2023) (en banc). Ironically, it was the strength of
respondents' challenge as verifed by the court's preliminary
224                    LACKEY v. STINNIE

                       Jackson, J., dissenting

order that prompted both the change in law and the Commis-
sioner's robust effort to stiff the plaintiffs with respect to
attorney's fees. Moreover, it is hardly a revelation that law-
yers who would otherwise be willing to litigate meritorious
civil rights cases (i. e., matters in which interim relief is criti-
cal due to ongoing civil rights violations) will likely be dis-
couraged from taking on such representations if fee awards
can be so easily thwarted.
   The majority dismisses concerns about strategic mooting
as both “ `entirely speculative' ” and likely to “arise in only a
small number of contexts.” Ante, at 204 (quoting Buckhan-
non, 532 U. S., at 608). But, as I have shown, the facts of
this very case belie the majority's nonchalance, particularly
in light of the Buckhannon experience. Research suggests
that the Court's rejection of the catalyst theory in that case
had the predictable practical effect of discouraging public in-
terest organizations and private attorneys from taking on
Page Proof Pending Publication
civil rights actions. C. Albiston & L. Nielsen, The Proce-
dural Attack on Civil Rights: The Empirical Reality of Buck-
hannon for the Private Attorney General, 54 UCLA L. Rev.
1087, 1092 (2007); cf. n. 2, supra. Similarly, a multitude of
legal advocacy groups have fled amicus briefs in this case
to explain that losing the ability to recoup fees for securing
interim relief will jeopardize their missions. See, e. g., Brief
for Alliance Defending Freedom et al. as Amici Curiae 7–10;
Brief for American Civil Liberties Union et al. as Amici Cu-
riae 28–30; Brief for Lawyers' Committee for Civil Rights
Under Law et al. as Amici Curiae 17–18.
   There is thus every reason to believe that the net result
of today's decision will be less civil rights enforcement in the
long run. Without irony, the majority reads a statute that
was “enacted to [e]nsure that private citizens have a mean-
ingful opportunity to vindicate their [civil] rights,” Pennsyl-
vania v. Delaware Valley Citizens' Council for Clean Air,
478 U. S. 546, 559 (1986), as if Congress meant to make pri-
vate civil rights enforcement harder to achieve.
                   Cite as: 604 U. S. 192 (2025)            225

                     Jackson, J., dissenting

                         *      *      *
  The majority holds that obtaining a preliminary injunction
never entitles a plaintiff to fees under § 1988(b). In doing
so, it overrules the decisions of every Court of Appeals to
consider the issue, relies on an atextual “conclusive judg-
ment” requirement, and ignores both our precedents and
Congress's intent.
  It is quite true that Congress has demonstrated its ability
to fx our mistakes in this realm. Ante, at 205. But, in my
view, rather than relying on Congress to check our work, we
should give full effect to the plain text and remedial purpose
of § 1988(b) in the frst instance. This Court should have
held that, when a court hearing a civil rights lawsuit issues a
preliminary injunction that materially alters the relationship
between the parties and is never reversed, the requesting
party “prevails” for fee-shifting purposes and is thus eligible
for a fee award under § 1988(b).
Page Proof Pending Publication
                            Reporter’s Note

  The attached opinion has been revised to refect the usual publication
and citation style of the United States Reports. The revised pagination
makes available the offcial United States Reports citation in advance of
publication. The syllabus has been prepared by the Reporter of Decisions
Page Proof Pending Publication
for the convenience of the reader and constitutes no part of the opinion of
the Court. A list of counsel who argued or fled briefs in this case, and
who were members of the bar of this Court at the time this case was
argued, has been inserted following the syllabus. Other revisions may
include adjustments to formatting, captions, citation form, and any errant
punctuation. The following additional edits were made:

p. 217, line 13: “was” is changed to “is”

```

---

## GROUP: _overhaul2/lake/cases/Landor v. Louisiana Dept. of Corrections.json  (`lake-record`, 1 assertions)

### content_page

```
---
title: Landor v. Louisiana Dept. of Corrections
type: case
citation: "No. 23-1197, slip op. (U.S. 2026)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2026
date_decided: ""
docket: 23-1197
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
  opinion_url: "https://www.courtlistener.com/opinion/10878535/landor-v-louisiana-dept-of-corrections-and-public-safety/"
  cluster_id: 10878535
  opinion_id: 11346052
  identity_checked: false
lake:
  record_id: Landor v. Louisiana Dept. of Corrections
  status: under_review
  projected_at: 2026-07-09
homes:
  - page: "[[Suing Federal Officers]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
tags:
  - case
  - section-1983
  - rluipa
  - spending-clause
  - individual-capacity
  - damages
  - supreme-court
holding: "Because RLUIPA was enacted under Congress's Spending Clause authority, an individual state official may be held personally liable under the statute only if that individual voluntarily and knowingly consented to answer such suits; the officers who allegedly shaved a Rastafarian inmate's head never entered any funding agreement with the federal government, so RLUIPA affords no damages claim against them in their personal capacities."
aliases:
  - Landor v. Louisiana Dept. of Corrections
  - Landor v. Louisiana Department of Corrections and Public Safety
  - Landor v. Louisiana
---

# Landor v. Louisiana Dept. of Corrections

*No. 23-1197, slip op. (U.S. 2026)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10878535 → majority opinion 11346052 (Gorsuch, J.; No. 23-1197, decided June 23, 2026). Rule quote string-matched to the CL slip-opinion syllabus 2026-07-07; slip-style pin (current-Term slip opinion, no reporter cite assigned — S2 A3). S9 promotes. -->

## Background
Damon Landor, a Rastafarian whose faith forbids cutting his hair, alleged that Louisiana Department of Corrections officers — aware of his religious beliefs — forcibly shaved his head. He sued LDOC and several officers in their personal capacities under the Religious Land Use and Institutionalized Persons Act (RLUIPA), which Congress enacted under its Spending Clause power and which conditions federal prison funds on the recipient system's agreement to answer certain religious-exercise suits. The district court dismissed the RLUIPA claims; the Fifth Circuit declined to revive the claim against the individual officers, holding RLUIPA does not authorize personal-capacity suits.

## Issue
Whether RLUIPA, a Spending Clause statute, permits damages suits against individual state officials in their personal capacities.

## Rule
The Spending Clause lets Congress attach conditions to federal funds, but "[a]dditional sanctions are permissible only with the 'voluntar[y] and knowin[g]' consent of those who must bear them," tested through a "contract analogy" under which a person is bound only by conditions to which he actually, knowingly agreed. The Court held: "Individuals may not be held liable in their personal capacities under a Spending Clause statute unless those individuals have voluntarily and knowingly consented to answer lawsuits under the statute." — slip op. at 1. ^pin-slip1

## Application
LDOC, as the funding recipient, agreed to answer certain RLUIPA suits — but the individual officers did not. Landor never alleged that any officer personally entered an agreement with the federal government, let alone voluntarily and knowingly consented to face RLUIPA damages liability. Just as a breach-of-contract action cannot proceed against someone who never formed the contract, Landor's RLUIPA claim cannot proceed against officers who never accepted the statute's conditions. His agency-law and related arguments all failed because they sidestepped the dispositive consent requirement.

## Conclusion
**Affirmed** as to the individual-capacity claims. Justice Gorsuch wrote for the Court (6–3).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Landor* marks the ceiling of Spending Clause remedies against individuals: unlike § 1983, which reaches state officers sued in their personal capacities by force of statute, a funding-condition statute like RLUIPA binds only the consenting recipient — leaving injured plaintiffs to look elsewhere for personal-capacity damages.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Landor v. Louisiana Dept. of Corrections and Public Safety*, No. 23-1197, slip op. (U.S. 2026)](https://www.courtlistener.com/opinion/10878535/landor-v-louisiana-dept-of-corrections-and-public-safety/) — pinpoint: slip op. at 1 (Spending Clause individual-capacity consent rule). Rule quote string-matched to the CL slip-opinion syllabus 2026-07-07. Current-Term slip opinion; no U.S. Reports cite assigned yet (S2 A3 slip precedent).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c21ef49ebd9a5d8d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Landor v. Louisiana Dept. of Corrections"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Landor v. Louisiana Dept. of Corrections", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Landor v. Louisiana Dept. of Corrections

```json
{
  "schema_version": "s2.v1",
  "record_id": "Landor v. Louisiana Dept. of Corrections",
  "status": "under_review",
  "identity": {
    "case_name": "Landor v. Louisiana Dept of Corrections and Public Safety",
    "case_name_short": "Landor",
    "case_name_full": "",
    "input_case_name": "Landor v. Louisiana Department of Corrections and Public Safety",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2026,
    "docket": "23-1197",
    "cluster_id": 10878535,
    "lead_opinion_id": 11346052,
    "sibling_ids": [],
    "absolute_url": "/opinion/10878535/landor-v-louisiana-dept-of-corrections-and-public-safety/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": "scotus",
      "selected": null,
      "reason": "no_official_class_citation"
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "SCOTUS No. 23-1197, decided 2026-06-23 (609 U.S. ___; Gorsuch, 6-3). No S. Ct. page yet.",
      "legs": [
        {
          "source": "Cornell LII",
          "url": "https://www.law.cornell.edu/supremecourt/text/23-1197",
          "cite": "No. 23-1197, decided 2026-06-23"
        },
        {
          "source": "Justia",
          "url": "https://supreme.justia.com/cases/federal/us/609/23-1197/",
          "cite": "609 U.S. ___ (2026) placeholder"
        }
      ]
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
    "date_created": "2026-07-06T12:14:06Z",
    "date_modified": "2026-07-09T05:52:34Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:14:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:14:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:14:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:14:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "landor-v-louisiana-department-of-corrections-and-public-safety--10878535",
      "to_record_id": "Landor v. Louisiana Dept. of Corrections",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Landor v. Louisiana Dept. of Corrections

```
(Slip Opinion)              OCTOBER TERM, 2025                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

         LANDOR v. LOUISIANA DEPARTMENT OF
         CORRECTIONS AND PUBLIC SAFETY ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE FIFTH CIRCUIT

   No. 23–1197.      Argued November 10, 2025—Decided June 23, 2026
The Religious Land Use and Institutionalized Persons Act of 2000
  (RLUIPA) was enacted pursuant to Congress’s Spending Clause au-
  thority and imposes various conditions on federal funds distributed to
  state prison systems like the Louisiana Department of Corrections
  (LDOC). One condition requires state prison systems to agree to an-
  swer federal suits by private plaintiffs alleging certain substantial bur-
  dens on their religious exercises. See 42 U. S. C. §§2000cc–1(a), (b)(1).
  Relying on that provision, inmate Damon Landor brought this
  RLUIPA lawsuit against LDOC as well as some of the prison system’s
  individual officers in their personal capacities, seeking damages from
  them. Mr. Landor is a Rastafarian whose religious convictions require
  him to leave his hair uncut. He claims that LDOC officers—despite
  being aware of his religious beliefs—forcibly shaved his head. The of-
  ficers moved to dismiss, arguing that while their employer LDOC may
  have agreed to answer certain private suits under RLUIPA, they were
  not parties to any such agreement, and therefore Mr. Landor had no
  federal cause of action against them. The district court dismissed Mr.
  Landor’s RLUIPA claims against both the officers and LDOC. On ap-
  peal, Mr. Landor challenged only the dismissal of his claim against the
  individual officers. The Fifth Circuit declined to revive that portion of
  his suit, holding that RLUIPA does not permit suits against officers in
  their individual capacities.
Held: Individuals may not be held liable in their personal capacities un-
 der a Spending Clause statute unless those individuals have voluntar-
 ily and knowingly consented to answer lawsuits under the statute; be-
 cause the individual defendants in this case did not voluntarily and
2       LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                        PUBLIC SAFETY
                           Syllabus

    knowingly consent to face RLUIPA liability in an agreement with the
    federal government, Mr. Landor’s case cannot proceed against them.
    Pp. 3–18.
       (a) While the Constitution’s “Spending Clause,” Art. I, §8, cl. 1, may
    confer on Congress the power to spend money for the general welfare,
    it does not “endow Congress with [any] power to regulate conduct.”
    Medina v. Planned Parenthood South Atlantic, 606 U. S. 357, 370.
    Congress may attach conditions to the funds it distributes, and if a
    recipient “violates those conditions,” Congress typically may “termi-
    nate” its agreement to provide funds. Id., at 365–366 (internal quota-
    tion marks omitted). But Congress cannot dictate whatever other
    sanctions it might wish for violating conditions found in its Spending
    Clause legislation. Additional sanctions are permissible only with the
    “voluntar[y] and knowin[g]” consent of those who must bear them.
    Pennhurst State School and Hospital v. Halderman, 451 U. S. 1, 17.
    To sort out whether consent exists, the Court has traditionally em-
    ployed a “contract analogy” that helps to ensure conditions attached to
    federal funds—including those prescribing exposure to potential sanc-
    tions—apply only to those who have knowingly and voluntarily agreed
    to them. Pp. 3–8.
       (b) These settled principles resolve this case. Before this Court,
    LDOC does not dispute that it is a recipient of federal funds and has
    agreed to answer certain RLUIPA suits as a condition of accepting
    those funds. But this case involves only claims against individual state
    employees in their personal capacities, and Mr. Landor does not allege
    that any of those individuals has entered any agreement with the fed-
    eral government, let alone that any of them has voluntarily and know-
    ingly consented to answer private suits under RLUIPA. Because they
    never agreed to answer suits like this one, Mr. Landor’s case cannot
    proceed against them any more than a breach of contract action might
    proceed against a defendant who never formed a contract. P. 8.
       (c) Mr. Landor’s arguments are all variations on the theme that the
    lack of voluntary and knowing consent does not matter. And they all
    fail for that reason. Under the Spending Clause and the Court’s prec-
    edents, the consent requirement is key. Pp. 9–18.
          (1) Mr. Landor invokes agency law, arguing that LDOC employees
    may be held liable because they are LDOC’s agents. But as a matter
    of blackletter law, when a principal enters a contract with a third
    party, the principal’s agents do not become liable to the third party for
    their principal’s nonperformance. LDOC might be subject to certain
    private suits under RLUIPA if it breaches its promises to the federal
    government, but it does not follow that LDOC’s employees are as well.
    Pp. 9–10.
          (2) Mr. Landor next turns to South Dakota v. Dole, 483 U. S. 203,
                      Cite as: 609 U. S. ___ (2026)                     3

                                Syllabus

  arguing that his proposed cause of action satisfies Dole’s four require-
  ments and therefore satisfies the Spending Clause too. But Dole’s re-
  quirements apply in addition to—not instead of—the rule that Con-
  gress may not use the Spending Clause to bind entities and individuals
  without their knowing and voluntary consent. Dole itself added a fifth
  rule barring compulsion and reaffirmed the clear-statement rule, both
  of which serve to ensure real consent exists. Mr. Landor also argues
  that RLUIPA’s mere existence sufficed to alert the individual defend-
  ants that they could be held personally liable. This argument fares no
  better. A Spending Clause statute assumes binding effect only
  through “voluntar[y] and knowin[g]” agreement, which is lacking here.
  Pennhurst, 451 U. S., at 17. Pp. 10–12.
       (3) Mr. Landor next turns to the fungibility of money, contending
  that the individual defendants are indirect recipients of federal funds
  because they receive paychecks from LDOC. But this argument would
  mean that so long as a penny of federal spending makes its way to an
  individual, Congress could directly regulate his conduct based on the
  fiction that he has consented to regulation. This is inconsistent with
  the requirement of knowing and voluntary consent, and it would give
  Congress an effectively unbridled police power impossible to square
  with the Spending Clause’s terms or our precedents. Pp. 12–15.
       (4) Mr. Landor’s reliance on the Necessary and Proper Clause and
  Sabri v. United States, 541 U. S. 600, is misplaced. In Sabri, the Court
  held that Congress’s criminal ban on theft, fraud, or bribery against a
  federal funding recipient is a necessary and proper incident to Con-
  gress’s authority to spend money. 541 U. S., at 605–606. Mr. Landor
  contends that his proposed cause of action is likewise incidental to
  RLUIPA’s policy protecting religious exercises. But Mr. Landor is an-
  swering the wrong question. The correct question is instead whether
  such a cause of action is a necessary and proper incident to Congress’s
  enumerated power to spend money. Suits against nonconsenting par-
  ties like the individual officers here might advance RLUIPA’s policy
  but do not safeguard federal funds from being “frittered away in graft.”
  Id., at 605. Adopting Mr. Landor’s proposed cause of action would al-
  low Congress to evade the consent requirement inherent in its Spend-
  ing Clause authority and regulate directly the conduct of countless
  nonconsenting individuals in spheres traditionally reserved to the
  States. Such a result would be inconsistent with principles of state
  sovereignty and a federal government of limited and enumerated reg-
  ulatory powers. Pp. 15–18.
82 F. 4th 337, affirmed.

  GORSUCH, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and THOMAS, ALITO, KAVANAUGH, and BARRETT, JJ., joined.
4     LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                         Syllabus

JACKSON, J., filed a dissenting opinion, in which SOTOMAYOR and KAGAN,
JJ., joined.
                       Cite as: 609 U. S. ____ (2026)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    United States Reports. Readers are requested to notify the Reporter of
    Decisions, Supreme Court of the United States, Washington, D. C. 20543,
    pio@supremecourt.gov, of any typographical or other formal errors.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 23–1197
                                  _________________


    DAMON LANDOR, PETITIONER v. LOUISIANA
      DEPARTMENT OF CORRECTIONS AND
            PUBLIC SAFETY, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE FIFTH CIRCUIT
                                [June 23, 2026]

   JUSTICE GORSUCH delivered the opinion of the Court.
   This case concerns whether the Religious Land Use and
Institutionalized Persons Act of 2000 permits plaintiffs to
sue nonconsenting state employees in their private capaci-
ties for damages.
                              I
  Today, Congress offers financial support to all 50 States
and many other entities. Much of that support comes with
strings attached. So, for example, Congress has conditioned
receipt of federal highway funds on a State’s agreement to
maintain laws setting a minimum drinking age of 21. See
South Dakota v. Dole, 483 U. S. 203 (1987). Likewise, Con-
gress has conditioned federal Medicaid funds on a State’s
willingness to administer its healthcare programs con-
sistent with various rules.       See Medina v. Planned
Parenthood South Atlantic, 606 U. S. 357, 362–364 (2025).
In each of these contexts and many others, the penalty for
noncompliance is straightforward: Congress may “termi-
nate funds” if a recipient fails to abide by the conditions
2    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                    Opinion of the Court

associated with its grants. Id., at 365–366 (internal quota-
tion marks omitted).
   The statute at issue before us, the Religious Land Use
and Institutionalized Persons Act of 2000 (RLUIPA), works
similarly. As relevant here, RLUIPA imposes various con-
ditions on federal funds distributed to state prison systems
like the Louisiana Department of Corrections (LDOC). One
condition requires prison systems to refrain from imposing
“substantial burden[s] on the religious exercise[s]” of state
prisoners outside exceptional circumstances.           See 42
U. S. C. §§2000cc–1(a), (b)(1); see also Tr. of Oral Arg. 60.
If a prison system fails to comply with that condition, Con-
gress may cut off its funding.
   But when enacting RLUIPA, Congress did something
more: It included another, distinct remedy as part of the
bargain. As a condition of funding, Congress called on state
prison systems to agree to answer suits by private plaintiffs
alleging substantial burdens on their religious exercises.
Specifically, the law asked those systems to consent to suit
by any injured party “assert[ing] a violation of ” RLUIPA
and seeking “appropriate relief.” §2000cc–2(a).
   This case concerns that provision. Damon Landor is a
Rastafarian whose religious convictions require him to
leave his hair uncut. In 2020, after a conviction in Louisi-
ana state court, Mr. Landor spent a few months in custody.
Near the end of his sentence, as officers transferred him
from one facility to another, Mr. Landor grew concerned
that the new facility’s intake officers might cut his hair pur-
suant to standard LDOC grooming policies. To avoid that
possibility, he provided the officers with a copy of Ware v.
LDOC, 866 F. 3d 263 (CA5 2017), which held that RLUIPA
generally bars prisons from cutting Rastafarians’ hair. See
id., at 266, 274. But, Mr. Landor says, the LDOC officers
in the new facility responded by throwing his copy of Ware
in the trash and proceeding to shave his head, causing him
to violate his religious beliefs.
                 Cite as: 609 U. S. ____ (2026)           3

                     Opinion of the Court

   After that transpired, Mr. Landor brought this lawsuit
under RLUIPA seeking money damages. He sued not only
LDOC, but also some of the prison system’s individual of-
ficers in their personal capacities. The officers responded
by asking the district court to dismiss Mr. Landor’s com-
plaint. As they saw it, their employer, LDOC, may have
struck a bargain with the federal government to answer
certain private suits by prisoners like Mr. Landor. But,
they argued, they were not parties to that or any other
agreement to answer private suits under RLUIPA. Accord-
ingly, they continued, Mr. Landor had no federal cause of
action against them. Ultimately, the court dismissed Mr.
Landor’s RLUIPA claims against both LDOC and the offic-
ers.
   On appeal to the Fifth Circuit, Mr. Landor did not chal-
lenge the district court’s dismissal of his RLUIPA claim
against LDOC. Instead, he focused on his claim against the
individual officers, asking the Court of Appeals to revive
only that portion of his suit. The Fifth Circuit declined to
do so. It did not question that RLUIPA may permit certain
claims against funding recipients like LDOC. But, the
court held, RLUIPA “does not permit suits against officers
in their individual capacities.” 82 F. 4th 337, 341 (2023).
We granted Mr. Landor’s petition for a writ of certiorari.
606 U. S. 916 (2025).
                            II
  Before us, the parties dispute two questions. One is
whether, by authorizing private lawsuits seeking “appro-
priate relief,” RLUIPA ever permits suits for money dam-
ages—or whether the statute instead limits plaintiffs like
Mr. Landor to other remedies, like injunctions or declara-
tory judgments. Brief for Petitioner 2–3, 18–19; Brief for
Respondents 4. The other question the parties spar over is
whether, consistent with the Constitution, a plaintiff may
bring an RLUIPA suit against individuals, like the officers
4     LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                     Opinion of the Court

in this case, who have not formed any agreement with the
federal government. Brief for Petitioner 38–46; Brief for
Respondents 28–30, 45–46. To resolve this case, we need
answer only the second question.1
   Article I of the Constitution grants Congress certain lim-
ited and enumerated powers. Congress, for example, may
“regulate Commerce . . . among the several States.” Art. I,
§8, cl. 3. It may “establish a uniform Rule of Naturaliza-
tion, and uniform Laws on the subject of Bankruptcies.”
Cl. 4. It may “coin Money” and “provide for the Punishment
of counterfeiting.” Cls. 5–6. These provisions and others
allow Congress to regulate the behavior of the American
people in specific fields. And each allows Congress to back
up its regulations “with a sanction” enforced either “by the
COERTION of the magistracy, or by the COERTION of arms.”
The Federalist No. 15, p. 95 (J. Cooke ed. 1961) (A. Hamil-
ton). So, for example, federal statutes require airlines op-
erating in interstate commerce to hold certificates and com-
ply with federal requirements. See 49 U. S. C. §§41101,
41102, 41109. The Bankruptcy Code allows a court to alter
a creditor’s rights and a debtor’s responsibilities. See Title
11. And Title 18, Chapter 25, criminalizes counterfeiting.
See, e.g., 18 U. S. C. §473. Each of these regulations finds
its footing in a provision of Article I that empowers Con-
gress to do just that: regulate.
   The terms of RLUIPA before us rest on a different foun-
dation. As the parties agree, Congress enacted them
——————
   1 The dissent says we give “short shrift” to the principle that constitu-

tional questions are to be avoided “ ‘if there is some other ground upon
which to dispose of the case.’ ” Post, at 4 (opinion of JACKSON, J.) (quoting
Bond v. United States, 572 U. S. 844, 855 (2014)). But this is a “pruden-
tial rule,” Zobrest v. Catalina Foothills School Dist., 509 U. S. 1, 8 (1993),
not a “mechanica[l ]” one, Almendarez-Torres v. United States, 523 U. S.
224, 239 (1998). And for reasons we outline, the constitutional question
here is readily resolved by our precedents. It is also narrower than the
statutory question in an important respect: It does not require us to ad-
dress whether RLUIPA ever authorizes money damages.
                  Cite as: 609 U. S. ____ (2026)             5

                      Opinion of the Court

pursuant to what is sometimes called the Constitution’s
Spending Clause. See Sossamon v. Texas, 563 U. S. 277,
290 (2011); Brief for Petitioner 3; Brief for Respondents 2.
That provision of Article I gives Congress the “Power To lay
and collect Taxes, Duties, Imposts and Excises, to pay the
Debts and provide for the common Defence and general
Welfare of the United States.” Art. I, §8, cl. 1. At the found-
ing, some argued this language conferred on Congress the
power to regulate on nearly any topic it wishes, backed by
practically any sanction it chooses, so long as it does so in
service of the “general Welfare.” See Medina, 606 U. S., at
370. It appears that Gouverneur Morris, a leading advocate
of this reading and a member of the Committee on Style,
even tried to replace one of the draft Clause’s commas with
a semicolon with the hope of making his reading more plau-
sible. See W. Treanor, The Case of the Dishonest Scrivener:
Gouverneur Morris and the Creation of the Federalist Con-
stitution, 120 Mich. L. Rev. 1, 20–24 (2021). But a careful
proofreader—Roger Sherman—noticed the surreptitious
edit, and the Convention rejected it. See ibid.
   In the end, the founding generation rejected Morris’s
reading of the Clause just as it had his semicolon. See Me-
dina, 606 U. S., at 370–371. While the Clause may allow
Congress to raise and spend money in support of the “gen-
eral Welfare,” early authorities concluded, it did not “endow
Congress with [any] power to regulate conduct.” Ibid. (in-
ternal quotation marks omitted). Were it otherwise, they
recognized, “the ‘enumeration of specific powers’ elsewhere
in Article I would be rendered largely pointless, and the Na-
tion would trade a limited federal government for ‘an un-
limited’ one.” Id., at 371 (quoting 2 J. Story, Commentaries
on the Constitution of the United States §§904, 906, pp.
367, 369 (1833)). This Court’s precedents have long re-
spected that founding-era consensus. See Medina, 606
U. S., at 371; accord, Cummings v. Premier Rehab Keller,
596 U. S. 212, 219 (2022).
6     LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                     Opinion of the Court

   It is an understanding that gives rise to important limi-
tations on spending legislation. Often, Congress attaches
conditions to the funds it distributes. And typically, if a re-
cipient “violates those conditions,” Congress may “termi-
nate” its agreement to provide funds. Medina, 606 U. S., at
365–366 (internal quotation marks omitted). But because
the Spending Clause confers no authority to “regulate di-
rectly,” Dole, 483 U. S., at 209, Congress cannot just dictate
whatever other sanctions it might wish for violating condi-
tions found in its Spending Clause legislation.
   Instead, additional sanctions are permissible only with
the “voluntar[y] and knowin[g]” consent of those who must
bear them. Pennhurst State School and Hospital v. Halder-
man, 451 U. S. 1, 17 (1981). Put simply, without independ-
ent regulatory authority, Congress must rely on consent. It
must ask and others must agree to face liability should they
violate a funding condition. Time and time again, from at
least 1845 to the present, our precedents have stressed the
centrality of consent in this field. Compare Searight v.
Stokes, 3 How. 151, 169 (1845) (calling spending legislation
a “compact . . . to which the state assented”), with Medina,
606 U. S., at 372 (describing spending statutes as “federal-
state agreements”).2
——————
  2 See also, e.g., Neil, Moore & Co. v. Ohio, 3 How. 720, 742 (1845) (call-

ing spending legislation “an agreement . . . between the United States
and a state”); McGee v. Mathis, 4 Wall. 143, 155 (1866) (“It is not doubted
that the grant by the United States to the State upon conditions, and the
acceptance of the grant by the State, constituted a contract” founded on
“consent of minds”); Steward Machine Co. v. Davis, 301 U. S. 548, 597–
598 (1937) (Spending legislation is an “agreemen[t] . . . with Congress”);
Pennhurst, 451 U. S., at 17 (“[L]egislation enacted pursuant to the spend-
ing power is much in the nature of a contract: in return for federal funds,
the States agree to comply with federally imposed conditions”); Gebser v.
Lago Vista Independent School Dist., 524 U. S. 274, 287 (1998) (discuss-
ing the “contractual nature” of Title IX); Barnes v. Gorman, 536 U. S.
181, 186 (2002) (“We have repeatedly characterized . . . Spending Clause
                      Cite as: 609 U. S. ____ (2026)                      7

                           Opinion of the Court

  To sort out whether consent exists—and thus whether a
condition associated with spending legislation is enforcea-
ble—we have traditionally turned to contract principles for
guidance. See Sossamon, 563 U. S., at 290 (The contract
analogy represents “a . . . limitation on” the “liability”
Spending Clause statutes may impose (emphasis deleted)).
Consider some examples. At common law, coerced assent
to a contract is invalid. See Restatement (Second) of Con-
tracts §175(1) (1979). Likewise, we have held, coerced as-
sent to a spending condition—by way of an economic “gun
to the head”—is invalid. National Federation of Independ-
ent Business v. Sebelius, 567 U. S. 519, 581–582 (2012)
(opinion of ROBERTS, C. J.); see also id., at 676–677 (joint
dissent of Scalia, Kennedy, THOMAS, and ALITO, JJ.); Dole,
483 U. S., at 211. At common law, ambiguous contractual
language is construed against its drafter. See C & L Enter-
prises, Inc. v. Citizen Band Potawatomi Tribe of Okla., 532
U. S. 411, 423 (2001). Similarly, we have concluded, Con-
gress must clearly and unambiguously alert a grant recipi-
ent to any condition on federal funds. Pennhurst, 451 U. S.,
at 17. In these ways and others, our “contract analogy”
helps safeguard against conflating Congress’s spending
power with a regulatory power. It does so by ensuring that
conditions attached to federal funds—including those pre-
scribing exposure to potential sanctions—apply only to
those who have knowingly and voluntarily agreed to them.
See Cummings, 596 U. S., at 220; cf. Medina, 606 U. S., at

——————
legislation as much in the nature of a contract” (internal quotation marks
omitted)); National Federation of Independent Business v. Sebelius, 567
U. S. 519, 577 (2012) (opinion of ROBERTS, C. J.) (“The legitimacy of Con-
gress’s exercise of the spending power . . . rests on whether the State vol-
untarily and knowingly accepts the terms of the contract” (internal quo-
tation marks omitted)); Cummings v. Premier Rehab Keller, 596 U. S.
212, 219 (2022) (“Spending Clause legislation operates based on consent:
in return for federal funds, the recipients agree to comply with federally
imposed conditions” (internal quotation marks and alteration omitted)).
8     LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                     Opinion of the Court

371–372 (noting that an analogy to treaties, another con-
sensual instrument, may also be appropriate).3
   These settled principles resolve this case. Before us,
LDOC does not dispute that it is a recipient of federal funds.
It does not question that it has agreed to answer certain
RLUIPA suits as a condition of accepting those funds. But
as it comes to us, this case does not involve claims against
LDOC. It involves only claims against individuals in their
personal capacities. And Mr. Landor does not allege that
any of those individuals has entered any agreement with
the federal government, let alone that any of them has vol-
untarily and knowingly consented to answer private suits
under RLUIPA.
   To know that is enough to know the Court of Appeals was
correct. Mr. Landor does not have a federal RLUIPA cause
of action against the officers. Under the Spending Clause,
Congress lacks regulatory authority to impose liability on
them directly and must depend instead on consent. And
because they never agreed to answer suits like this one, Mr.
Landor’s case cannot proceed against them any more than
a breach of contract action might proceed against a defend-
ant who never formed a contract.




——————
   3 The contract analogy operates “only as a potential limitation on lia-

bility,” Cummings, 596 U. S., at 225 (internal quotation marks omitted),
meaning that consent is a necessary but not sufficient condition for con-
stitutionality. As we have explained, “the exercise of the spending power
must [also] be in pursuit of the general welfare,” spending conditions
must be “german[e] . . . to federal purposes,” and still “other constitu-
tional provisions may provide an independent bar.” Dole, 483 U. S., at
207–208 (internal quotation marks omitted). A spending agreement that
violates one of these requirements is invalid, just like “an illegal con-
tract” at common law is invalid, even if freely assented to. Kaiser Steel
Corp. v. Mullins, 455 U. S. 72, 77 (1982) (internal quotation marks omit-
ted).
                  Cite as: 609 U. S. ____ (2026)             9

                      Opinion of the Court

                            III
  Seeking to avoid this conclusion, Mr. Landor and the dis-
sent advance many arguments. But each is a variation on
the same theme. In different ways, Mr. Landor and the dis-
sent submit, the lack of voluntary and knowing consent
does not matter. And each of their arguments fails for ex-
actly that reason. Under the Spending Clause and our prec-
edents, voluntary and knowing consent is key.
                               A
   Mr. Landor begins by invoking agency and contract law.
As LDOC’s agents, he contends, the individual defendants
have a “duty to obey all reasonable directions” from their
principal. Restatement (Second) of Agency §385(1) (1957).
And, he adds, an agent’s actions can sometimes “bin[d] his
principal” to a contract when he acts “within the scope of
his authority.” United States v. Gooding, 12 Wheat. 460,
469 (1827); see also Restatement (Second) of Agency §140.
From these common law principles, Mr. Landor reasons, it
follows that the individual defendants in this case may be
held personally liable under RLUIPA. Brief for Petitioner
31–33; see also post, at 13–14, 24, n. 10 (opinion of
JACKSON, J.).
   That much does not follow even from the precepts Mr.
Landor cites. Certainly, an agent usually must obey his
principal’s directions and sometimes may bind his princi-
pal. But when a principal (here, LDOC) enters a contract
with a third party (here, the federal government), as a mat-
ter of blackletter contract law the principal’s agents do not
become “liable” to the third party for their principal’s “non-
performance.” Restatement (Second) of Agency §328 (bold-
face deleted); see also, e.g., 12 R. Lord, Williston on Con-
tracts §35:34, p. 502 (4th ed. 2012) (“The agent cannot
enforce the [principal’s] contract, nor is the agent bound by
it” (footnote omitted)); Hodgson v. Dexter, 1 Cranch 345, 363
(1803) (Marshall, C. J., for the Court) (“It is too clear to be
10    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                     Opinion of the Court

controverted, that . . . contracts made on account of the gov-
ernment . . . are obligatory on the government; not the [gov-
ernment’s] officer”). So, yes, LDOC might be subject to cer-
tain private suits under RLUIPA for breaching its promises
to the federal government. But under normal principles of
agency and contract law, that does not mean LDOC’s em-
ployees are as well.
   To be sure, Mr. Landor and the dissent identify ways in
which Congress could have lawfully imposed personal lia-
bility on the individual defendants. For example, Congress
could have said that, as a condition of federal funding to
LDOC, its officers had to agree to enter separate contracts
with the federal government consenting to answer suits un-
der RLUIPA. Or Congress might have conditioned its funds
on Louisiana’s agreement to exercise its own regulatory
powers to adopt a state law cause of action enforceable
against LDOC officers who violate RLUIPA. Brief for Peti-
tioner 47; cf. post, at 23–24. But these untapped possibili-
ties only underscore Mr. Landor’s bind. The first hypothet-
ical has what this case does not, namely, an agreement
between the federal government and the defendants. And
in the second hypothetical, again unlike this case, the State
would have exercised its own regulatory powers. See Ran-
dolph v. Donaldson, 9 Cranch 76, 84–85 (1815) (Story, J.,
for the Court) (describing a Virginia statute that did essen-
tially that in response to a federal request).4
                            B
   Next, Mr. Landor points to Dole. That case, he says, set
out just four requirements for Spending Clause legisla-
tion—and consent is not among them. As he reads Dole, a
——————
  4 Nor, of course, does anything prevent Louisiana from acting on its

own initiative to adopt a state law permitting damages in cases like this
one. Indeed, counsel for the individual officers before us indicated that
just such a claim may be available to Mr. Landor under state law in state
court. Tr. of Oral Arg. 113–114.
                  Cite as: 609 U. S. ____ (2026)           11

                      Opinion of the Court

condition on the grant of federal funds need only be “(1) in
pursuit of the general welfare; (2) unambiguously ex-
pressed; (3) related to the federal interest in particular na-
tional projects or programs; and (4) not in violation of other
constitutional provisions.” Brief for Petitioner 33 (citing
483 U. S., at 207–208; internal quotation marks omitted).
And because a condition requiring nonconsenting individu-
als to answer RLUIPA suits satisfies all these require-
ments, Mr. Landor concludes, his case may proceed. The
dissent appears to agree, suggesting that the voluntary and
knowing consent requirement finds no support in “any of
Dole’s prongs.” Post, at 13.
   That is incorrect. The four rules Mr. Landor extracts
from Dole apply in addition to—not instead of—the rule
that Congress may not use the Spending Clause to bind en-
tities and individuals without their knowing and voluntary
consent. That much is evident from Dole itself. As the dis-
sent admits, Dole proceeds to add a fifth rule for Spending
Clause legislation shortly after the passage Mr. Landor
cites: Funding conditions may not “pass the point at which
pressure turns into compulsion.” 483 U. S., at 211 (internal
quotation marks omitted); post, at 12–13. And that bar on
compulsion, as we have seen, serves to help ensure real con-
sent exists. See Part II, supra. The same holds true of the
clear-statement rule that Dole reaffirmed. Congress must
impose spending conditions “unambiguously,” not for no
reason, but so that participants in federally funded pro-
grams may “exercise their choice knowingly, cognizant of
the consequences of their participation.” 483 U. S., at 207
(internal quotation marks omitted). Had Dole meant to
bulldoze the consent requirement and condone consent-free
regulation under the Spending Clause, post, at 14–15, it
would have had no occasion to emphasize any of this. Nor
does Mr. Landor’s and the dissent’s consent-free gloss on
Dole merely overlook important qualifications in Dole itself.
Worse still, their misreading would pit that decision
12    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                     Opinion of the Court

against nearly two centuries’ worth of cases recognizing the
consent requirement, see n. 1, supra—hardly a sensible
way to construe our precedents.
   Responding to these problems, Mr. Landor and the dis-
sent submit that RLUIPA’s mere existence sufficed to alert
the individual defendants, or at least their employer, that
they could be held personally liable. See Brief for Petitioner
35; post, at 20. But, just like the attempt to rewrite Dole,
this argument misses the point. A Spending Clause statute
does not carry independent regulatory force. It assumes
binding effect only through “voluntar[y] and knowin[g]”
agreement. Pennhurst, 451 U. S., at 17. If someone has not
agreed to be bound, it does not matter that he may be aware
of the existence of a contract between other parties. And if
someone has not agreed to be bound, it does not matter
whether other contracting parties might wish to bind him.
Either way, he has not agreed to be bound, so he cannot be.5
                            C
  Seeking still another way around the consent require-
ment, Mr. Landor turns next to the fungibility of money.
The individual defendants, he observes, receive paychecks
from LDOC, and some of that entity’s funding comes from
the federal government. As a result, Mr. Landor submits,
the individual defendants are indirect recipients of federal
funds and, for that reason, should be deemed to have im-
plicitly consented to RLUIPA liability.

——————
  5 The dissent also attempts a factual analogy to Dole, suggesting that,

because Congress “use[d] its spending power to regulate . . . drinking
habits” there, it is free to regulate the individual officers’ conduct here.
Post, at 14. But this analogy fails for reasons we have seen. Under the
spending legislation at issue in Dole, Congress conditioned federal high-
way funds on an agreement by the States to exercise their regulatory
powers to raise their drinking ages to 21. See 483 U. S., at 205, 211.
Congress did not purport to regulate “drinking habits” directly, let alone
create a federal cause of action against underage drinkers.
                  Cite as: 609 U. S. ____ (2026)             13

                      Opinion of the Court

   This submission fails as well. Mr. Landor would have us
hold, for the first time, that so long as a penny of federal
spending makes its way to an individual, however indi-
rectly, Congress can regulate his conduct directly based on
the fiction that he has consented to regulation. None of that
is consistent with our precedents holding that funding con-
ditions in Spending Clause legislation lack independent
regulatory force but instead derive their effect from “volun-
tar[y] and knowin[g]” assent. Pennhurst, 451 U. S., at 17.
   Notice too where Mr. Landor’s theory would lead. Given
the “explo[sion]” of Spending Clause legislation in recent
decades, Medina, 606 U. S., at 373, Congress would enjoy
an effectively unbridled police power. Federal authorities
would have no need to show that their regulations repre-
sent proper exercises of Congress’s limited and enumerated
powers found in the Commerce Clause, the Bankruptcy
Clause, or any other. All they would have to show is that a
recipient who consented to a funding condition spent some
formerly federal money in transactions with a third party.
Just like that, the federal government could directly regu-
late the third party’s conduct. Take some examples. On
Mr. Landor’s theory, Congress could require coaches at uni-
versities that receive federal funds to permit transgender
athletes to play women’s sports—or face personal liability
in suits for damages. Likewise, Congress could bar doctors
at medical practices that accept federal funds from admin-
istering certain vaccines to children—again on pain of dam-
ages. See Tr. of Oral Arg. 37–43. None of that fits with our
system of limited and enumerated federal powers where all
others are reserved to the States and the people.
   The dissent criticizes us for “trot[ting] out” this “parade
of horribles.” Post, at 24. But if this is a parade, the dissent
marches right along, embracing these hypotheticals and
more. See ibid. In fact, as the dissent sees it, we should
not engage in “hairsplitting” over any “strict direct-consent-
to-liability . . . requirement” or “ill-formed” contract
14   LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                    Opinion of the Court

analogy. Post, at 17, 25. On its view, these things are all
just “empt[y] . . . formalism[s].” Post, at 24. If Congress can
ask individuals to consent to funding conditions—or ask
States to enact laws in order to receive federal funds—Con-
gress might as well be allowed to regulate private behavior
directly. Ibid. Likely enough, that vision would have de-
lighted Gouverneur Morris. But it is one at war with the
terms of the Spending Clause, how that Clause has been
widely understood since the founding, and a long line of this
Court’s precedents. Nor is there anything “empty” about
insisting that Congress operate within the limited and enu-
merated powers the Constitution provides. This Court has
rejected views like the dissent’s many times before. See
Part II, supra. And we do so again today.
   Faced with that problem, Mr. Landor and the dissent
search for some foothold in our precedents to support their
view that the Spending Clause grants Congress direct reg-
ulatory authority. Perhaps the best they can muster is a
line snipped from Rust v. Sullivan, 500 U. S. 173 (1991),
where we said that an individual employed in a federally
funded program must “perform [his] duties in accordance
with the . . . restrictions” specified by Congress. Id., at 198;
Brief for Petitioner 32; post, at 24. But even that is of no
help. Rust did not involve an attempt to impose personal
liability on the program’s employees. The only consequence
for violating Congress’s funding conditions fell on the fed-
eral funding recipient itself and amounted to no more than
a loss of funding. See 500 U. S., at 178–179. And that is
exactly the “typical remedy” for noncompliance our cases
have long described. Medina, 606 U. S., at 373 (internal
quotation marks omitted).
   Mr. Landor and the dissent also point to Grove City Col-
lege v. Bell, 465 U. S. 555 (1984), a Title IX case. Brief for
Petitioner 32–33; post, at 15–16, n. 7. But there, too, the
only penalty was the traditional one—the “terminati[on]” of
federal funding. See Grove City College, 465 U. S., at 561.
                       Cite as: 609 U. S. ____ (2026)                        15

                            Opinion of the Court

Subsequent events illustrate as much: After losing the
case, the college decided “to exit the federal [funding] pro-
grams rather than surrender its autonomy,” a choice it was
free to make because Title IX binds only those who have
freely elected to accept federal funds. Grove City College,
Forty Years Ago, Supreme Court Case Changed GCC For-
ever (Feb. 26, 2024) (archived at https://perma.cc/2AQU-
3PME). Pretty plainly, neither Rust nor Grove City College
purported to reimagine the Spending Clause’s terms or to
rewrite our precedents construing them.6
                              D
  Finding our precedents under the Spending Clause una-
vailing, Mr. Landor and the dissent appeal to ones constru-
ing the Necessary and Proper Clause. In Sabri v. United
States, 541 U. S. 600 (2004), we held that Congress’s crimi-
nal ban on theft, fraud, or bribery against a federal funding
recipient, 18 U. S. C. §666, is a necessary and proper inci-
dent to Congress’s authority under the Spending Clause.
See 541 U. S., at 605–606; see also Salinas v. United States,
522 U. S. 52, 60–61 (1997). Mr. Landor and the dissent

——————
   6 The dissent also resorts to a supposed concession. Respondents, the

dissent says, concede “ ‘that Louisiana prison officials must comply with
RLUIPA’s substantive protections.’ ” Post, at 17 (quoting Brief for Re-
spondents 46). But the dissent omits the rest of the sentence, which clar-
ifies that respondents concede only the possibility of “injunctive relief”
against them “in their official capacities” for RLUIPA violations. Brief
for Respondents 46 (emphasis added). And, of course, an “official capac-
ity” suit is “no different from a suit against the State itself.” Printz v.
United States, 521 U. S. 898, 931 (1997) (internal quotation marks omit-
ted). Contrary to the dissent, respondents have clearly maintained all
along that they cannot “be held personally liable for an alleged RLUIPA
violation.” Brief for Respondents 46. The dissent is also wrong to sug-
gest that any LDOC official who might be sued in his official capacity can
for that reason be sued in his personal capacity. See post, at 18. The
whole point of an official-capacity suit is that it “is not a suit against the
official but rather is a suit against the official’s office.” Printz, 521 U. S.,
at 930–931 (internal quotation marks omitted).
16   LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                    Opinion of the Court

contend this case is no different because personal liability
for nonconsenting defendants is likewise a necessary and
proper incident to RLUIPA’s policy protecting religious ex-
ercises. Brief for Petitioner 36–39; post, at 15–20.
   Much as the other arguments we have encountered mis-
conceive the Spending Clause, this one misunderstands the
Necessary and Proper Clause. The latter provision author-
izes Congress to employ “necessary and proper” means for
“carrying into Execution” its other enumerated powers.
Art. I, §8, cl. 18. Put another way, the Clause allows Con-
gress to enact laws “incidental to those powers which are
expressly given.” McCulloch v. Maryland, 4 Wheat. 316,
411 (1819). So the question is not, as Mr. Landor and the
dissent would have it, whether a personal-capacity cause of
action is incidental to RLUIPA’s policy protecting religious
exercises. The question, instead, is whether their proposed
cause of action is a necessary and proper incident to Con-
gress’s constitutionally enumerated power to spend money.
   With the question correctly framed, the distinction be-
tween this case and Sabri becomes unmistakable. Sec-
tion 666 addresses thieves, fraudsters, bribers, and others
who threaten to “fritte[r] away in graft” the funds Congress
distributes pursuant to the Spending Clause. 541 U. S., at
605. The thief steals allocated money; the fraudster ex-
tracts it under false pretenses; the briber obtains it by
greasing palms. “Congress,” Sabri held, “does not have to
sit by and accept the risk” actors of that sort pose to its con-
stitutionally enumerated spending power. Ibid. Instead,
as a necessary and proper incident to that power, Congress
may punish people who seek to sap federal funds from their
intended beneficiaries. See ibid. And Congress may do so,
Sabri concluded, even where not every misappropriated
dollar may be “ ‘traceabl[e]’ ” to “ ‘specific federal pay-
ments.’ ” United States v. Comstock, 560 U. S. 126, 147
(2010) (quoting Sabri, 541 U. S., at 605–606).
                  Cite as: 609 U. S. ____ (2026)           17

                      Opinion of the Court

   Nothing similar can be said for the cause of action Mr.
Landor and the dissent propose. Suits against nonconsent-
ing parties, like the individual officers here, might advance
RLUIPA’s laudable policy of protecting religious exercises.
But they do not safeguard from graft the federal funds Con-
gress distributes pursuant to its spending power. Recogniz-
ing as much, seemingly every Court of Appeals to address
the question has concluded that Sabri does not begin to
command the result Mr. Landor and the dissent seek. See
Tripathy v. McKoy, 103 F. 4th 106, 115 (CA2 2024) (“Sabri
is easily distinguishable”); Sharp v. Johnson, 669 F. 3d 144,
155, n. 15 (CA3 2012) (“Sabri is inapposite”); Haight v.
Thompson, 763 F. 3d 554, 570 (CA6 2014) (“RLUIPA is
nothing like the Sabri statute”); Barnett v. Short, 129 F. 4th
534, 543 (CA8 2025) (Sabri “is too dissimilar”); Wood v.
Yordy, 753 F. 3d 899, 903 (CA9 2014) (reliance on Sabri is
“not . . . sensible”).
   Nor, with Sabri out of the picture, can Mr. Landor and
the dissent explain how their proposed cause of action
would help “carr[y] into execution” Congress’s enumerated
power to spend money. McCulloch, 4 Wheat., at 434. In
truth, they don’t even try. Instead, they suggest, the Nec-
essary and Proper Clause ought to be elastic enough to al-
low the “extraction of money damages” from virtually any-
one who violates virtually any condition found in Spending
Clause legislation. Post, at 17–20, 24. But while the Nec-
essary and Proper Clause may allow Congress to enact pro-
visions actually incidental to its spending power, like those
protecting federal money against graft, it does not tolerate
outcomes that would “undermine the structure of [the fed-
eral] government established by the Constitution.” Sebe-
lius, 567 U. S., at 559 (opinion of ROBERTS, C. J.). Nor does
the Clause tolerate results that would “violat[e] the princi-
ple of state sovereignty.” Printz v. United States, 521 U. S.
898, 924 (1997). And adopting the expansive approach Mr.
18   LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                    Opinion of the Court

Landor and the dissent propose would require us to violate
both rules.
   Just consider what they would have us say. On their
view, Congress may evade the consent requirement inher-
ent in its Spending Clause authority simply by invoking the
Necessary and Proper Clause. Post, at 17–20. With even a
modest federal expenditure somewhere nearby, Congress
could then proceed to regulate directly the conduct of count-
less nonconsenting individuals—not just the individual of-
ficers here, but also others like the coaches and physicians
we discussed above. See Part III–C, supra. Congress could
regulate directly, too, in innumerable spheres, including
ones traditionally reserved to the States. Really, under Mr.
Landor’s and the dissent’s logic, we would be “hard pressed
to posit any activity . . . that Congress [would be] without
power to regulate.” United States v. Lopez, 514 U. S. 549,
564 (1995). And as inconsistent as all that is with both
principles of state sovereignty and a federal government of
limited and enumerated regulatory powers, it hardly repre-
sents a “proper means for carrying into [e]xecution” Con-
gress’s spending power. Sebelius, 567 U. S., at 559 (opinion
of ROBERTS, C. J.) (internal quotation marks and some al-
terations omitted).
                             *
  Under the Spending Clause, Congress’s power to spend
money does not include the power to regulate. Spending
Clause statutes can bind only those who voluntarily and
knowingly undertake obligations by agreement with the
federal government. Because that essential element is
missing here, we affirm the judgment of the Fifth Circuit.
                                             It is so ordered.
                 Cite as: 609 U. S. ____ (2026)            1

                    JACKSON, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 23–1197
                         _________________


    DAMON LANDOR, PETITIONER v. LOUISIANA
      DEPARTMENT OF CORRECTIONS AND
            PUBLIC SAFETY, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE FIFTH CIRCUIT
                        [June 23, 2026]

   JUSTICE JACKSON, with whom JUSTICE SOTOMAYOR and
JUSTICE KAGAN join, dissenting.
   Congress enacted the Religious Land Use and Institu-
tionalized Persons Act of 2000 (RLUIPA) to ensure that
state and local prisons respect prisoners’ right to religious
exercise. Congress might have opted to accomplish this
through contracts with the prisons it funds. Instead, it
passed a law.
   RLUIPA requires state and local prisons that accept fed-
eral funding to accommodate prisoners’ religious exercise
more generously than the Constitution mandates. Like
many, this law comes with an enforcement mechanism: To
ensure compliance, RLUIPA authorizes an impacted pris-
oner to sue any prison employee who violates the statute.
Such suits, the statute provides, may proceed against the
employee in the employee’s individual capacity and may
yield “appropriate relief.”    42 U. S. C. §§2000cc–2(a),
2000cc–5(4)(A).
   Neither respondents nor the Court contests Congress’s
power to impose RLUIPA’s substantive directive accommo-
dating religious freedom. The majority nevertheless adopts
the peculiar position that Congress is powerless to create,
and a State is powerless to accept, the natural next step: a
damages remedy against officials who violate that directive.
2    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                   JACKSON, J., dissenting

   This severance of rights and remedies is a sleight of hand;
it comes by way of the majority’s full-throated endorsement
of a contract analogy even though what secures the rights
at issue is not a contract but a law. Today’s decision magi-
cally transforms a federal statute into an invitation to be
accepted or declined, deemed binding only if each particular
defendant has explicitly agreed to be penalized. No matter
that laws, as opposed to contracts, don’t ordinarily work
this way. The trick here is the majority’s effortless confla-
tion of law making and agreement making—two different
sources of binding authority.
   The majority’s analysis is spellbindingly straightforward:
Spending Clause statutes are contracts, and contracts bind
only those who consent. Ante, at 6–8. But pulling this rab-
bit out of the hat requires misconstruing the Spending
Clause and the Necessary and Proper Clause, and ignoring
decades of precedent affirming Congress’s authority to use
the power of the purse to govern. In the end, the Court re-
duces some of Congress’s greatest legislative achieve-
ments—federal laws that secure civil rights, environmental
stability, healthcare, and more—to nothing more than the
wheelings-and-dealings of an especially wealthy private
party. Because I would not so trivialize a federal statute or
the constitutional powers pursuant to which it was passed,
I respectfully dissent.
                                 I
  It is not often that a real-life incident so clearly illustrates
Congress’s reasons for adopting legislation, or the Consti-
tution’s wisdom in enabling it.
  Damon Landor’s Rastafarian faith requires him to “let
the locks of the hair of his head grow.” The Holy Bible,
Numbers 6:5 (King James Version). For a Rastafari like
Landor, locks are “the physical embodiment of . . . spiritual
identity and connection to God.” See Brief for Rastafari
Scholars as Amici Curiae 3. Landor preserved this
                  Cite as: 609 U. S. ____ (2026)            3

                     JACKSON, J., dissenting

connection—through what is known as the Nazarite Vow—
for two decades, allowing his hair to grow to his knees. And
he continued for most of a brief stint in Louisiana jails in
2020: At the two facilities that housed Landor for the bulk
of his prison time, officials accommodated his vow without
incident.
   They did so not just because it was the right thing to do
but also because federal law required it. This Court’s deci-
sion in Holt v. Hobbs, 574 U. S. 352 (2015), held that
RLUIPA mandated an accommodation for prisoners’ reli-
giously motivated beards, id., at 369–370, and thus strongly
suggested that Landor was entitled to a similar accommo-
dation. Even more on point, the Fifth Circuit—which co-
vers Louisiana—had precedent specifically requiring ac-
commodation of the Nazarite Vow. See Ware v. Louisiana
Dept. of Corrections, 866 F. 3d 263 (2017).
   Landor knew of Ware. He also knew of the threat that
jails posed to his hair (and faith) despite it. So when he was
transferred to a third jail with three weeks remaining in his
sentence, he came prepared. He carried with him a copy—
a physical, printed copy—of Ware. Upon arrival, Landor
presented the case to the intake guard. “Unmoved,” the
guard “threw Landor’s papers in the trash.” 82 F. 4th 337,
340 (CA5 2023) (case below). The guard summoned the
warden, who demanded documentation from Landor’s sen-
tencing judge corroborating his religious beliefs. “When
Landor couldn’t instantly meet that demand, two guards
carried him into another room, handcuffed him to a chair,
held him down, and shaved his head.” Ibid.
   After serving his time, Landor sued the Louisiana De-
partment of Corrections (LDOC), the jail, the warden, the
department’s secretary, and John Doe officers 1–10 in their
individual and official capacities. In addition to state-law
claims, he brought claims under RLUIPA as well as under
42 U. S. C. §1983 for violations of his First, Eighth, and
4    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                   JACKSON, J., dissenting

Fourteenth Amendment rights, seeking both injunctive re-
lief and damages.
   Respondents successfully moved to dismiss Landor’s com-
plaint. Landor’s release from prison, the District Court ex-
plained, mooted his bid for injunctive relief. Landor’s
RLUIPA claim thus remained only by dint of his request for
damages against the defendants in their individual capaci-
ties. But Fifth Circuit precedent held that RLUIPA does
not permit individual-capacity suits. See Sossamon v.
Texas, 560 F. 3d 316, 327–329 (2009). With Landor’s re-
maining claims failing for other reasons not relevant here,
the District Court dismissed his complaint.
   Landor had federal law on his side. And he did every-
thing he could do in real time to ensure that prison officials
knew that. We took this case to address whether Landor
can seek money damages from the officials who ignored the
law, held him down, and “uncrowned him before God.”
Brief for Rastafari Scholars as Amici Curiae 12.
                               II
   Before us, respondents offer two reasons why Landor can-
not obtain damages—one statutory and the other constitu-
tional. First, they posit that RLUIPA’s provision for “ap-
propriate relief ” against a “person acting under color of
State law,” 42 U. S. C. §§2000cc–2(a), 2000cc–5(4)(A), au-
thorizes only injunctive relief. Second, they assert that, if
RLUIPA purports to authorize individual-capacity dam-
ages lawsuits against prison officials, Congress will have
exceeded the Constitution’s limits on its spending power.
   The majority addresses only the constitutional argument,
giving short shrift to the “well-established principle . . . that
normally the Court will not decide a constitutional question
if there is some other ground upon which to dispose of the
case.” Bond v. United States, 572 U. S. 844, 855 (2014) (in-
ternal quotation marks omitted); see Ashwander v. TVA,
297 U. S. 288, 347 (1936) (Brandeis, J., concurring); Spector
                      Cite as: 609 U. S. ____ (2026)                     5

                         JACKSON, J., dissenting

Motor Service, Inc. v. McLaughlin, 323 U. S. 101, 105 (1944)
(calling this principle “more deeply rooted than any other
in the process of constitutional adjudication”). The majority
is of course correct that the practice is prudential, not inex-
orable. Ante, at 4, n. 1. But there is prudence behind a
prudential rule. The reasons for this one include “the deli-
cacy” and “comparative finality” “of [the] function” of inval-
idating a congressional enactment, and “the consideration
due to the judgment of other repositories of constitutional
power concerning the scope of their authority.” Rescue
Army v. Municipal Court of Los Angeles, 331 U. S. 549, 571
(1947).1
   So I begin by rejecting respondents’ statutory argument.
RLUIPA plainly authorizes individual-capacity lawsuits for
money damages. We have already interpreted identical
language in RLUIPA’s sister statute, the Religious Free-
dom Restoration Act of 1993 (RFRA), to allow for individ-
ual-capacity damages lawsuits. See Tanzin v. Tanvir, 592
U. S. 43 (2020). And RLUIPA’s Spending Clause underpin-
ning does not rob the statute’s text of its plain meaning.
Understanding this is necessary background for Part III,
infra, my response to the majority’s constitutional analysis.
                             A
  RLUIPA is Congress’s latest contribution to a long-run-
ning religious-liberty dialogue between Congress and this
Court. That dialogue began, for our purposes, with Employ-
ment Div., Dept. of Human Resources of Ore. v. Smith, 494
U. S. 872 (1990). Smith is a seminal case in which the
——————
  1 I have no quarrel with the premise that a court may prioritize a con-

stitutional question that is “readily resolved by our precedents” and “nar-
rower” than the statutory alternative. Ante, at 4, n. 1. But the majority’s
approach has neither virtue. As I will explain, if our precedents “readily
resolv[e]” this case, they do so in Landor’s favor. And, while the conse-
quences for RLUIPA are indeed narrower, the consequences for other
Spending Clause statutes—not to mention congressional power more
generally—are substantial.
6    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                   JACKSON, J., dissenting

Court held that the First Amendment does not carve out
religious exemptions from neutral and generally applicable
laws. Id., at 878–882. Smith “recognized, however, that
the political branches could shield religious exercise
through legislative accommodation.” Cutter v. Wilkinson,
544 U. S. 709, 714 (2005). Taking up the invitation, Con-
gress sought to “restore” via statute what Smith left unpro-
tected by the Constitution. Tanzin, 592 U. S., at 45. The
result was RFRA, which forbade States and the Federal
Government alike from substantially burdening religious
exercise without compelling interest and narrow tailoring.
See 42 U. S. C. §2000bb et seq.
   Importantly, RFRA was not meant to be merely advisory;
like the constitutional rights it sought to imitate, RFRA
needed bite. Thus, “RFRA made clear that it was reinstat-
ing both the pre-Smith substantive protections of the First
Amendment and the right to vindicate those protections by
a claim.” Tanzin, 592 U. S., at 50. It did so by authorizing
“appropriate relief ” for violations of its terms. §2000bb–
1(c).
   As enacted, RFRA applied to State and Federal Govern-
ments and their officials. Tanzin, 592 U. S., at 50. But
RFRA’s application to States and state officials was short
lived: This Court would soon invalidate RFRA’s application
to the States as exceeding Congress’s power under Section
5 of the Fourteenth Amendment. See City of Boerne v. Flo-
res, 521 U. S. 507 (1997).
   Partially rebuffed, Congress tried again, enacting
RLUIPA, 42 U. S. C. §2000cc et seq. In contrast to RFRA’s
“sweeping” scope, RLUIPA focused in narrowly on two dis-
crete “areas of state and local action” in which Congress
thought religious freedom faced particular threat: land-use
regulation and institutionalized persons. Sossamon v.
Texas, 563 U. S. 277, 281 (2011).
   Other than the narrower coverage, RLUIPA practically
mirrors RFRA, its “sister statute.” Ramirez v. Collier, 595
                  Cite as: 609 U. S. ____ (2026)             7

                     JACKSON, J., dissenting

U. S. 411, 424 (2022). Like RFRA, RLUIPA aims to “secure
redress” for “undue barriers” to religious exercise. Cutter,
544 U. S., at 716–717. Like RFRA, RLUIPA features “an
express private cause of action” (indeed, one “that is taken
from RFRA”). Sossamon, 563 U. S., at 282. And like
RFRA’s, RLUIPA’s express cause of action allows “[a] per-
son” who suffers a violation of the statute to “assert” the
violation “as a claim or defense in a judicial proceeding and
obtain appropriate relief against a government.” §§2000cc–
2(a), 2000bb–1(c).
  Though neither statute elaborates on what a plaintiff can
get, both specify from whom they can get it. Neither stat-
ute, that is, defines “appropriate relief.” But both define
“government” to mean, among other things, an “official” of
the relevant sovereign and any “other person acting under
color of ” the relevant sovereign’s law. §§2000cc–5(4)(A),
2000bb–2(1). Thus, like RFRA, RLUIPA creates “a claim”
for “appropriate relief against” an “official” or “other person
acting under color of ” law. §§2000cc–2(a), 2000cc–5(4)(A),
2000bb–1(c), 2000bb–2(1).
                              B
   As a matter of text, the question whether RLUIPA au-
thorizes a claim for money damages is controlled by a unan-
imous holding this Court issued just six Terms ago. In Tan-
zin, 592 U. S. 43, we held that RFRA’s materially identical
terms authorize a damages claim. Our analysis was
straightforward. First, we ascertained the who. We iden-
tified the potential defendants in a RFRA lawsuit, asking
whether “injured parties can sue Government officials in
their personal capacities.” Id., at 47. And to that question,
we said that “RFRA’s text provides a clear answer: They
can.” Ibid. RFRA authorizes lawsuits not just against a
“government” as colloquially understood, but also against
government “official[s]” and “other person[s] acting under
color of law.” §§2000bb–1(c), 2000bb–2(1). This language,
8     LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                    JACKSON, J., dissenting

we noted, echoes “one of the most well-known civil rights
statutes: 42 U. S. C. §1983,” which authorizes individual-
capacity lawsuits against “ ‘person[s]’ ” acting “ ‘under color
of any statute.’ ” Tanzin, 592 U. S., at 48.
   With that answer in hand, we had no trouble discerning
the what: “what ‘appropriate relief ’ entails.” Ibid. We
acknowledged that the term is “ ‘open-ended’ ” and “ ‘inher-
ently context dependent.’ ” Id., at 49 (quoting Sossamon,
563 U. S., at 286). But given the who, the term had an ob-
vious meaning: “In the context of suits against Government
officials, damages have long been awarded as appropriate
relief.” Tanzin, 592 U. S., at 49.
   So too here. Indeed, Tanzin’s reasoning applies with even
more force to RLUIPA. RLUIPA’s prison context redoubles
Tanzin’s observation that damages will often be not only an
appropriate form of relief but “the only form of relief ” avail-
able. Id., at 51. The Prison Litigation Reform Act’s exhaus-
tion requirement and strict limitations on injunctive relief
in prisons, coupled with States’ ability to transfer prisoners
and thereby moot claims for injunctive relief, mean that
withholding a damages remedy will often leave prisoners
with no remedy at all.2
   Accordingly, if RFRA’s text authorizes individual-
capacity lawsuits for money damages, RLUIPA’s must do so
as well.
                              C
   It is true, though, that while the relevant statutory text
is the same, the two statutes’ fonts of power are not. It is
on this observation that respondents rest their statutory ar-
gument. Unlike RFRA, RLUIPA relies on (as relevant here)
——————
  2 See Brief for Rights Behind Bars et al. as Amici Curiae; Brief for the

National Police Accountability Project as Amicus Curiae 17–21. Con-
gress was aware of the interaction between the Prison Litigation Reform
Act (PLRA) and RLUIPA, as it expressly preserved the PLRA in
RLUIPA. See 42 U. S. C. §2000cc–2(e).
                    Cite as: 609 U. S. ____ (2026)                  9

                       JACKSON, J., dissenting

the Spending Clause. Any divergence between the statutes’
meanings, then, would have to come not from text but from
constitutional inference—something particular to the
Spending Clause compelling us not to adopt the same read-
ing of that same statutory language. When interpreting
Spending Clause legislation, we have used a contract anal-
ogy to require that Congress express its intent to impose
conditions on the receipt of federal funds “unambiguously.”
Barnes v. Gorman, 536 U. S. 181, 186 (2002) (internal quo-
tation marks omitted). Under our precedent, this is where
contract-law principles should come into play—not as a sub-
stantive limitation on Congress’s power (as the majority
uses it today) but as a demand for statutory clarity.
   But RLUIPA’s authorization of an individual-capacity
damages remedy is unambiguous for Spending Clause pur-
poses. Our cases foreclose any argument to the contrary.
Eight years before Congress passed RLUIPA, we considered
the remedies available under Title IX, another Spending
Clause statute—but one far less clear about remedies. See
Franklin v. Gwinnett County Public Schools, 503 U. S. 60,
64–65 (1992). Where RLUIPA is strident, Title IX is coy:
That statute has no express private right of action and, ac-
cordingly, no relevant remedial language. Id., at 65–66, 71.
Yet we still concluded that it authorized damages. We ex-
plained that, even absent explicit statutory language, “we
presume the availability of all appropriate remedies unless
Congress has expressly indicated otherwise.” Id., at 66.
And we flatly rejected the notion “that the normal presump-
tion in favor of all appropriate remedies”—including dam-
ages—“should not apply because Title IX was enacted pur-
suant to Congress’ Spending Clause power.” Id., at 74; see
also id., at 69 (explaining that the available “appropriate
relief ” encompassed damages).3
——————
  3 Franklin is not alone in suggesting that monetary damages are “ap-

propriate relief ” for the violation of a spending statute. Take, for
10    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                    JACKSON, J., dissenting

   Against Franklin, respondents point to Sossamon. But
Sossamon cannot bear anything close to the weight re-
spondents place on it. There, we held that the same
RLUIPA provision at issue today does not authorize dam-
ages in one very particular context, one with a different
who: “where the defendant is a sovereign.” Sossamon, 563
U. S., at 286. Sovereigns enjoy sovereign immunity, and
“[t]he essence of sovereign immunity . . . is that remedies
against the government differ from ‘general remedies prin-
ciples’ applicable to private litigants.” Id., at 291, n. 8. We
did not question the obvious meaning of “appropriate relief ”
in lawsuits against individuals. See ibid.4
   In short, RLUIPA leaves no need to “wonder . . . what sort
of penalties might be on the table” for a violation of its

——————
example, Barnes v. Gorman, 536 U. S. 181 (2002). There we observed
that, because of the contract analogy, “a remedy is ‘appropriate relief ’ ”
under a spending statute “only if the funding recipient is on notice that,
by accepting federal funding, it exposes itself to liability of that nature.”
Id., at 187. But we went on to explain that “[a] funding recipient is gen-
erally on notice that it is subject not only to those remedies explicitly
provided in the relevant legislation, but also to those remedies tradition-
ally available in suits for breach of contract”—including “compensatory
damages.” Ibid.
  4 Sossamon thus teaches that the term “appropriate relief ” is “ ‘inher-

ently context dependent.’ ” Tanzin, 592 U. S., at 49 (quoting Sossamon,
563 U. S., at 286). And the relevant lesson from Tanzin is that, in the
context of a suit against an individual, “appropriate relief ” plainly in-
cludes monetary damages. 592 U. S., at 49. Indeed, it can hardly mean
anything else; as damages often are not available in official-capacity law-
suits, the prospect of damages is the reason to sue officers individually.
See, e.g., Hafer v. Melo, 502 U. S. 21, 25, 27 (1991). Thus Tanzin (inter-
preting RFRA) disposed easily of Sossamon (interpreting RLUIPA), in-
voking not the different congressional powers involved but the different
defendants sued. See 592 U. S., at 51–52 (“Sossamon held that a State’s
acceptance of federal funding did not waive sovereign immunity to suits
for damages under a related statute—[RLUIPA]—which also permits
‘appropriate relief.’ The obvious difference is that this case features a
suit against individuals, who do not enjoy sovereign immunity” (citation
omitted)).
                     Cite as: 609 U. S. ____ (2026)                  11

                        JACKSON, J., dissenting

terms. Cummings v. Premier Rehab Keller, 596 U. S. 212,
220 (2022). Like RFRA, RLUIPA “reinstat[ed] both the pre-
Smith substantive protections of the First Amendment and
the right to vindicate those protections by a claim,” Tanzin,
592 U. S., at 50—with an individual damages remedy
where appropriate.5
                               III
   At long last, I arrive where today’s majority starts. On
the majority’s view, no matter how clearly Congress speaks,
all that matters is the response it elicits: Spending Clause
legislation may not make anybody liable without their ex-
press consent. And because prison officials (as opposed to
their state-prison employers) have not directly accepted
federal funds, they have not consented to being sanctioned
for their failure to follow federal law. Ante, at 6–8.
   The majority’s reasoning requires it to diminish two con-
gressional powers and contort many more precedents of this
Court. Stated simply, the Spending Clause contains no
direct-consent requirement. The power it grants Congress
“is of course not unlimited.” South Dakota v. Dole, 483 U. S.
203, 207 (1987). But neither is it so cramped as the major-
ity imagines. Most important, it is a power to legislate, not
merely to negotiate. And if the Spending Clause falls short,
the Necessary and Proper Clause supplies the additional
power Congress needs to bind prison officials—state agents
——————
   5 Because our Spending Clause precedent requires Congress to trans-

late its intent unambiguously into the statute, I do not rely heavily on
RLUIPA’s legislative history. But make no mistake: Congress indisput-
ably intended RLUIPA to authorize individual-capacity lawsuits for
money damages. See, e.g., H. R. Rep. No. 106–219, p. 29 (1999) (RLUIPA
“track[s] RFRA, creating a private cause of action for damages, injunc-
tion, and declaratory judgment”); 146 Cong. Rec. 19123 (2000) (state-
ment of Rep. Canady) (same); Religious Liberty: Hearing before the Sen-
ate Committee on the Judiciary, 106th Cong., 1st Sess., p. 91 (1999)
(statement of Douglas Laycock) (“Appropriate relief includes declaratory
judgments, injunctions, and damages”).
12   LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                   JACKSON, J., dissenting

whose compliance is critical to RLUIPA’s effective imple-
mentation.
                               A
   The Spending Clause is embedded within Congress’s first
enumerated power. It gives Congress the “Power To lay and
collect Taxes, Duties, Imposts and Excises, to pay the Debts
and provide for the common Defence and general Welfare
of the United States.” U. S. Const., Art. I, §8, cl. 1.
   The authority to spend money for the “general Welfare”
naturally includes the power to determine the general wel-
fare and to ensure that expenditures further it. See, e.g.,
Helvering v. Davis, 301 U. S. 619, 645 (1937). Thus, “Con-
gress has broad power under the Spending Clause of the
Constitution to set the terms on which it disburses federal
funds.” Cummings, 596 U. S., at 216. To exercise that
spending power, Congress passes laws conditioning federal
funding on compliance.
   The product is, of course, federal law like any other—en-
acted via bicameralism and presentment, and constituting
“the supreme Law of the Land.” U. S. Const., Art. VI, cl. 2;
see Armstrong v. Exceptional Child Center, Inc., 575 U. S.
320, 324 (2015); Health and Hospital Corporation of Marion
Cty. v. Talevski, 599 U. S. 166, 171–172 (2023). And such
law may further not only Congress’s other enumerated pow-
ers but also ends otherwise beyond Congress’s reach. See
United States v. Butler, 297 U. S. 1, 66 (1936).
   For decades, the Court has used a consistent yardstick to
measure the constitutionality of Spending Clause legisla-
tion. We crystallized that metric in Dole, 483 U. S. 203.
Funding conditions in laws enacted pursuant to the Spend-
ing Clause must be in pursuit of the general welfare; unam-
biguously expressed; related to the federal interest; and not
in violation of other constitutional provisions. Id., at 207–
208. The “financial inducement offered by Congress” also
                  Cite as: 609 U. S. ____ (2026)           13

                     JACKSON, J., dissenting

may not be “so coercive as to pass the point at which ‘pres-
sure turns into compulsion.’ ” Id., at 211.
  When Congress “exercise[s] its Spending Power,” we have
long understood, “Dole provides the appropriate framework
for assessing . . . constitutionality.” United States v. Amer-
ican Library Assn., Inc., 539 U. S. 194, 203, n. 2 (2003)
(opinion of Rehnquist, C. J.). But neither respondents nor
the majority attempts to invalidate RLUIPA under any of
Dole’s prongs. Instead, they devise a new one: Spending
Clause legislation can make liable only those who have di-
rectly and expressly consented to be made liable. See ante,
at 8.
  This new rule starts from a kernel of truth. Spending
Clause legislation does not take effect of its own accord. It
requires a funding recipient to accept funds, and thereby to
consent to the accompanying conditions. In this way,
spending legislation differs from other federal law, which
may command without offering.
  From that kernel, though, the majority sprouts a dra-
matic innovation. The conditions prescribed in Spending
Clause legislation, the majority insists, may not bind any-
body but the funding recipient itself, no matter the recipi-
ent’s relationship to the nonrecipient (i.e., sovereign, em-
ployer, or, as here, both), and no matter how essential the
conditions are to Congress’s spending program.
                              B
  This novel consent requirement discards decades of
Spending Clause and Necessary and Proper Clause prece-
dent. This Court has upheld spending statutes that make
RLUIPA look modest in its reach.
  Recall that the individuals RLUIPA exposes to liability
are state prison officials. These are agents of the State who
voluntarily seek the State’s employ and wield its power.
The State—the funding recipient—thus exercises authority
over them in two ways. As their employer, the State can
14    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                    JACKSON, J., dissenting

place conditions on their employment. And as a sovereign,
the State can govern their behavior. Under our precedents,
either should have sufficed. With both, this is an easy case.
   Start with Dole itself. Dole upheld a federal law condi-
tioning highway funding on States raising the legal age for
purchasing or publicly possessing alcohol—that is, on
States forbidding a category of behavior for young adults.
483 U. S., at 205. Underage drinkers are not the Federal
Government’s contracting partners. Cf. id., at 218 (O’Con-
nor, J., dissenting) (arguing that the law was unconstitu-
tional because it was not “a condition determining how fed-
eral highway money shall be expended” but rather “a
regulation determining who shall be able to drink liquor”).
But we held that Congress could nonetheless use its spend-
ing power to regulate their drinking habits in this fashion.
   Thus, one need look no further than this Court’s most ca-
nonical Spending Clause case to cast doubt on the major-
ity’s insistence on individual consent. “If South Dakota can
agree to criminalize the behavior of its 19-year-old bourbon
enthusiasts, it’s unclear why Louisiana cannot agree to
make its prison officials liable for forcibly shaving Damon
Landor’s head.” 93 F. 4th 259, 265 (CA5 2024) (Oldham, J.,
dissenting from denial of rehearing en banc).6
   The majority maintains that this is not Dole. RLUIPA is
different, the majority says, because Congress has bound
individual prison officials directly whereas the federal law
in Dole did not act directly upon nonrecipients. Instead,
that law “influence[d] a State’s legislative choices,” causing
the State to regulate young drinkers. New York v. United
States, 505 U. S. 144, 167 (1992) (discussing Dole); ante, at
12, n. 5. But that distinction makes no relevant difference.
Either way, Congress has used its spending power to

——————
   6 See also Haight v. Thompson, 763 F. 3d 554, 570 (CA6 2014) (Sutton,

J.) (pointing out that the position the majority embraces today “is not
consistent with Dole” or multiple other precedents of this Court).
                      Cite as: 609 U. S. ____ (2026)                    15

                         JACKSON, J., dissenting

regulate individuals without their express consent. In Dole,
the State exposed the individual to liability in exchange for
federal funds. So too here.
   Regardless, in subsequent cases, we have not been
squeamish about recognizing Congress’s authority to regu-
late nonrecipients directly in service of protecting “the in-
tegrity and proper operation of the federal program.” Sa-
linas v. United States, 522 U. S. 52, 61 (1997). In Salinas,
for instance, we harbored “no serious doubt about the con-
stitutionality” of an anti-bribery statute that regulated in-
dividuals situated identically to the prison officials here—
i.e., “state and local officials employed by agencies receiving
federal funds.” See id., at 58, 60. (Salinas thus checked
both the “employer” and “sovereign” boxes.) And in Sabri
v. United States, 541 U. S. 600 (2004), we went further still,
explaining that the Spending Clause, buttressed by the
Necessary and Proper Clause, empowered Congress to
criminalize private individuals’ bribery of state and local of-
ficials employed by entities receiving federal funds, see id.,
at 605. The private individuals were complete strangers to
the funding relationship between the Federal Government
and the funded entities. No matter. Congress, we ex-
plained, can “bring federal power to bear directly on indi-
viduals” where necessary “to see to it that taxpayer dollars
appropriated under [the Spending Clause] are in fact spent
for the general welfare.” Id., at 605, 608.7
——————
  7 Our statutory-interpretation cases teach the same lesson.         Take
Grove City College v. Bell, 465 U. S. 555 (1984), where we held that Title
IX—a Spending Clause statute forbidding sex discrimination by recipi-
ents of federal funds—regulates a college that “accepts no direct [federal]
assistance but enrolls students who receive federal grants,” id., at 558.
We reasoned that the language of the statute “contain[ed] no hint that
Congress perceived a substantive difference between direct institutional
assistance and aid received by a school through its students.” Id., at 564;
see also National Collegiate Athletic Assn. v. Smith, 525 U. S. 459, 468
(1999) (“Entities that receive federal assistance, whether directly or
through an intermediary, are recipients within the meaning of Title IX”).
16    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                    JACKSON, J., dissenting

   So it is not I but the majority that jettisons “a long line of
this Court’s precedents.” Ante, at 14. We have lived for
decades in a world in which Congress has been able to use
its spending power to reach beyond direct recipients of fed-
eral funds. And it has done so repeatedly. In the Federal
Nursing Home Reform Act, for instance, Congress author-
ized civil penalties against individual employees of feder-
ally funded nursing homes who falsify resident assess-
ments.       See 42 U. S. C. §1396r(b)(3)(B)(ii).         In the
Emergency Medical Treatment and Active Labor Act, Con-
gress authorized civil penalties against doctors in federally
funded hospitals who negligently violate the law’s require-
ments. See 42 U. S. C. §1395dd(d)(1)(B). And in Title X of
the Public Health Service Act, Congress authorized fines
and imprisonment for state officers and employees who co-
erce abortion or sterilization by threatening the loss of fed-
erally funded benefits. See 42 U. S. C. §300a–8.
   These are important measures, for obvious reasons. They
are also required if these laws’ intended ends are to be ac-
complished, for a “State can act only through its officials,”
and an institution only through its employees. Pennhurst
State School and Hospital v. Halderman, 465 U. S. 89, 114,
n. 25 (1984); cf. Printz v. United States, 521 U. S. 898, 931
(1997) (“To say that the Federal Government cannot control
the State, but can control all of its officers, is to say nothing
of significance”). Congress reasonably seeks to ensure
——————
We never suggested, much less held, that such a statutory scheme raised
constitutional concerns. In fact, the college, lacking the gumption of to-
day’s Court, argued only that Congress had not bound indirect recipients
through Title IX, not that it could not. The more extreme position (the
one the majority adopts now) occurred to nobody.
  The majority makes hay of the college’s subsequent decision to stop
welcoming students who received federal financial aid and therefore to
escape Title IX. Ante, at 14–15. Of course, this same option is available
to prison officials, who may likewise “exit the federal [funding]
progra[m]” by seeking alternative employment. Ante, at 15 (internal
quotation marks omitted).
                     Cite as: 609 U. S. ____ (2026)                   17

                        JACKSON, J., dissenting

compliance with its directives by giving individual actors
imbued with state authority a personal stake in the matter.
Nothing in the Constitution prevents Congress from de-
signing Spending Clause statutes in this fashion.
                               C
   That should spell the end of this dispute. The Spending
Clause has no strict direct-consent-to-liability requirement,
and respondents offer no reason to think RLUIPA fails the
traditional Dole test. But Congress has still more reser-
voirs of power from which to draw. The Necessary and
Proper Clause “empowers Congress to enact laws in effec-
tuation of its enumerated powers”—including the spending
power—“that are not within its authority to enact in isola-
tion.” Gonzales v. Raich, 545 U. S. 1, 39 (2005) (Scalia, J.,
concurring in judgment); see Sabri, 541 U. S., at 605.
Should RLUIPA’s individual-capacity remedy require more
power than the Spending Clause provides, the Necessary
and Proper Clause supplies it.
   This conclusion flows from a concession respondents
make without reservation: “[T]here is no dispute that Lou-
isiana prison officials must comply with RLUIPA’s substan-
tive protections.” Brief for Respondents 46. Respondents,
in other words, do not place prison officials beyond
RLUIPA’s substantive reach; accepting that RLUIPA im-
poses a duty on prison officials, they just seek to “exempt”
those officials “from any of its liability provisions.” Depart-
ment of Agriculture Rural Development Rural Housing Ser-
vice v. Kirtz, 601 U. S. 42, 62 (2024).
   There is “no proper place in our jurisprudence” for this
“wholly artificial” distinction. Ibid. (internal quotation
marks omitted).8 The Necessary and Proper Clause makes
——————
  8 What two years ago was “wholly artificial” today becomes the crux of

the majority’s decision, which depends entirely on divorcing law from li-
ability, right from remedy.      See, e.g., ante, at 14–15, and n. 6
18    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                    JACKSON, J., dissenting

sure of it. That Clause enables “Congress to provide, by
suitable penalties, for the enforcement of all legislation nec-
essary or proper to the execution of powers with which it is
intrusted.” United States v. Fox, 95 U. S. 670, 672 (1878).
So where an enumerated power enables Congress to pre-
scribe rules, the Necessary and Proper Clause empowers
Congress to “give those rules force by imposing conse-
quences on [those] who disobey them.” United States v. Ke-
bodeaux, 570 U. S. 387, 400 (2013) (ROBERTS, C. J., concur-
ring in judgment); McCulloch v. Maryland, 4 Wheat. 316,
416 (1819) (attributing to the Necessary and Proper Clause
the government’s ability to “punish any violation of its
laws”); Ex parte Yarbrough, 110 U. S. 651, 658–659 (1884).
That is all RLUIPA’s cause of action does. It authorizes the
extraction of money damages for behavior Congress conced-
edly may proscribe.
   Notably, the majority does not contest the premise that
Louisiana’s prison officials must abide by RLUIPA. And it
admits, as it must, that a court may order prison officials in
their official capacities to comply with RLUIPA. See ante,
at 15, n. 6. But this leaves the majority in an odd spot. In
the majority’s view, the prison official’s relationship to the
State is close enough that “the actions of ” the official are
“the actions of the [State] itself ” such that the official may
stand in for the State in litigation, Brandon v. Holt, 469
U. S. 464, 472 (1985), but distant enough that the State’s
consent to damages liability on the official’s behalf means
nothing at all. There is no rational basis for that distinc-
tion.
   Battling uphill, the majority reworks the Necessary and
Proper Clause. The majority contends that, rather than al-
low Congress to enforce statutes passed pursuant to other

——————
(distinguishing precedents of this Court and respondents’ concession on
the grounds that they “did not involve an attempt to impose personal
liability”).
                     Cite as: 609 U. S. ____ (2026)                  19

                        JACKSON, J., dissenting

enumerated powers, the Necessary and Proper Clause must
facilitate the enumerated power itself. Ante, at 16. Only if
a regulation is “a necessary and proper incident to Con-
gress’s constitutionally enumerated power,” the majority
insists, does the Necessary and Proper Clause justify it.
Ibid.
   This is a deft maneuver but not a successful one, as it
diverts our focus to the wrong relationship. “The relevant
question is simply whether the means chosen are ‘reasona-
bly adapted’ to the attainment of a legitimate end” sought
under an enumerated power, not whether the means chosen
are incidental to the power itself. Gonzales, 545 U. S., at 37
(Scalia, J., concurring in judgment) (quoting United States
v. Darby, 312 U. S. 100, 121 (1941); emphasis added); see
also Kebodeaux, 570 U. S., at 406 (Scalia, J., dissenting)
(“[W]hat is necessary and proper to enforce a statute validly
enacted pursuant to an enumerated power is . . . itself nec-
essary and proper to the execution of an enumerated
power”).
   Said otherwise, “we look to see whether the statute con-
stitutes a means that is rationally related to the implemen-
tation of a constitutionally enumerated power.” United
States v. Comstock, 560 U. S. 126, 134 (2010) (emphasis
added). This is why “the Necessary and Proper Clause . . .
authorizes Congress, in the implementation of other ex-
plicit powers, to create federal crimes, to confine offenders
to prison” and more, Kebodeaux, 570 U. S., at 394–395—not
because the power to imprison is incidental to the power to,
say, regulate commerce, but because the power to imprison
gives Congress the ability to “ ‘make [its] regulation[s] effec-
tive,’ ” Gonzales, 545 U. S., at 36 (Scalia, J., concurring in
judgment) (quoting United States v. Wrightwood Dairy Co.,
315 U. S. 110, 119 (1942)).9
——————
  9 Even viewed from a first-principles standpoint, the majority’s fram-

ing makes little sense. The majority gives the Necessary and Proper
20    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                    JACKSON, J., dissenting

   The majority resorts finally to abstraction, retorting that
the Necessary and Proper Clause does not permit Congress
to “undermine the structure of [the federal] government es-
tablished by the Constitution” or “violat[e] the principle of
state sovereignty.” Ante, at 17 (alterations in original; in-
ternal quotation marks omitted). I do not contest these as-
sertions. It is the Court’s application of them here that is
baffling, since exposing state officials to damages liability
does nothing so dramatic. That state officials might be vul-
nerable to federally imposed money judgments for unlawful
conduct is a common feature of our federal system. See,
e.g., 42 U. S. C. §1983. RLUIPA’s imposition of damages
liability for state officials comes as no surprise to States or
their agents and by no means offends state sovereignty.
The State chose to accept the funds with full knowledge of
RLUIPA’s command, and the officials in turn chose to ac-
cept state employment with full knowledge of federal law.
   That the Necessary and Proper Clause may extend the
reach of the Spending Clause (as we have long recognized)
does not, of course, mean that congressional power is un-
bounded. Contra, ante, at 18. But it does mean (as again
we have long recognized) that where Congress may require
compliance via law it may also secure compliance via impo-
sition of liability, including damages.
——————
Clause no independent work to do, rendering it superfluous rather than
treating it as the adjunct the Framers envisioned. See, e.g., McCulloch
v. Maryland, 4 Wheat. 316, 417 (1819) (commenting that, although “the
right to carry the mail, and to punish those who rob it, is not indispensa-
bly necessary to” the power “ ‘to establish post offices and post roads,’ ”
the Necessary and Proper Clause affords Congress the power to take
those steps); see also Letter from A. Hamilton to G. Washington, Opinion
on the Constitutionality of an Act To Establish a Bank (Feb. 23, 1791),
in 8 Papers of Alexander Hamilton 70 (H. Syrett & J. Cooke eds. 1965)
(“The clause . . . is evidently designed to place on an unequivocal footing
the power of the government to employ all the means fairly relative to
the execution of its specified powers and to the fulfilment of the objects
entrusted to its direction”).
                  Cite as: 609 U. S. ____ (2026)           21

                     JACKSON, J., dissenting

                               IV
   I do not doubt that difficult questions about the limits of
Congress’s spending power exist. But, as I have explained
thus far, this case offered no opportunity to resolve them.
Respondents seek to limit the Spending Clause in a manner
directly contrary to our precedents. And when it comes to
enforcement of a concededly proper exercise of congres-
sional power, the Necessary and Proper Clause supplies
any authority that the Spending Clause cannot.
   Let us, then, step back and examine the origin and con-
sequences of the majority’s unprecedented invocation of a
“categorical font-of-power condition” limiting Congress’s
reach under the Spending Clause. Talevski, 599 U. S., at
192 (rejecting a similar effort). This limitation is not lo-
cated in the Constitution’s text; “[i]t is hard to imagine a
broader statement of the scope of Congress’s power” than
the Spending Clause. E. Chemerinsky, Protecting the
Spending Power, 4 Chapman L. Rev. 89, 93 (2001). And it
is not in our precedents either—today’s Court cannot suc-
cessfully explain the decisions of yesterday’s. Rather, it ap-
pears that the seeds of the majority’s dramatic weakening
of the spending power were first planted some time ago, and
are rooted in a loose contract analogy the Court has repeat-
edly cautioned against taking as anything more. The ma-
jority supercharges that analogy here and now, ensuring
that it comes to full flower. This may prove to be a conse-
quential choice.
                              A
   The contract analogy derives from the insight that
Spending Clause legislation requires acceptance of federal
funds before it can take hold, making it “much in the nature
of a contract.” Pennhurst State School and Hospital v. Hal-
derman, 451 U. S. 1, 17 (1981). Until today, we have used
that insight in two relatively modest ways, both as inter-
pretive aids. First, the contract analogy gives rise to a
22   LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                   JACKSON, J., dissenting

clear-notice requirement. See, e.g., id., at 24–25; Part II–C,
supra. Second, the analogy offers background principles to
fill in gaps where a statute falls short of the required clar-
ity. See, e.g., Cummings, 596 U. S., at 220, 221 (explaining
that a Spending Clause statute that is “silent as to availa-
ble remedies” presumptively authorizes “the usual contract
remedies” (emphasis deleted)); Barnes, 536 U. S., at 187 (“A
funding recipient is generally on notice that it is subject not
only to those remedies explicitly provided in the relevant
legislation, but also to those remedies traditionally availa-
ble in suits for breach of contract”).
   But even when using the analogy for those purposes, the
Court has always viewed it cautiously. We have consist-
ently refused to “imply . . . that suits under Spending
Clause legislation are suits in contract, or that contract-law
principles apply to all issues that they raise.” Id., at 189,
n. 2; see also Sossamon, 563 U. S., at 290 (same); Cum-
mings, 596 U. S., at 226 (declining to “incorporat[e] the law
of contract remedies wholesale”). Some Justices have war-
ily accepted the contract analogy in certain contexts while
cautioning that it “may fail” elsewhere. Barnes, 536 U. S.,
at 191 (Souter, J., concurring). Others have protested its
use as “novel.” Id., at 192 (Stevens, J., concurring in judg-
ment); Talevski, 599 U. S., at 193 (BARRETT, J., joined by
ROBERTS, C. J., concurring). Still others have cast doubt on
it as “an imperfect way” to interpret Spending Clause legis-
lation. Cummings, 596 U. S., at 230 (KAVANAUGH, J.,
joined by GORSUCH, J., concurring). In all events, the Court
has always rejected the idea—though pressed with vigor in
dissent—that Spending Clause legislation “is nothing more
than a contractual offer.” Talevski, 599 U. S., at 196
(THOMAS, J., dissenting); see also id., at 229 (criticizing the
Court for “holding that spending conditions are not merely
contractual”).
   At most, the Court has accepted that Spending Clause
legislation has “a contractual aspect” while steadfastly
                    Cite as: 609 U. S. ____ (2026)               23

                       JACKSON, J., dissenting

insisting that such laws nonetheless “cannot be viewed in
the same manner as a bilateral contract governing a con-
crete transaction.” Bennett v. Kentucky Dept. of Ed., 470
U. S. 656, 669 (1985); accord, B. Fahey, Federalism by Con-
tract, 129 Yale L. J. 2326, 2330 (2020) (noting spending
statutes’ “dual character” as “both contract-like instru-
ments and public lawmaking instruments”). After all,
“[u]nlike normal contractual undertakings,” Spending
Clause laws are “statut[es] . . . expressing the judgment of
Congress concerning desirable public policy.” Bennett, 470
U. S., at 669. Having undergone bicameralism and present-
ment, Spending Clause legislation “is legislation, in the
end, not a buy-sell transaction.” T. Seligmann, Muddy Wa-
ters: The Supreme Court and the Clear Statement Rule for
Spending Clause Legislation, 84 Tulane L. Rev. 1067, 1120
(2010).
   Today the Court abandons its warranted caution. An in-
terpretive guide becomes a substantive limitation on Con-
gress’s authority, as the Court takes a step toward embrac-
ing what one scholar has criticized as the “strong contract
theory”: the radical notion that Spending Clause legislation
is not just “ ‘in the nature of ’ a contract,” but is in fact “noth-
ing but a contract.” S. Bagenstos, Spending Clause Litiga-
tion in the Roberts Court, 58 Duke L. J. 345, 385 (2008)
(quoting Pennhurst, 451 U. S., at 17).
   Strange as it seems, today’s majority appears to mean it.
One indication is the majority’s concession that “Congress
could have lawfully imposed personal liability on the indi-
vidual defendants” if it had tweaked RLUIPA to better con-
form to the Court’s understanding of the limits of contract
law. Ante, at 10. “For example,” the majority allows, “Con-
gress could have said that, as a condition of federal funding
to LDOC, its officers had to agree to enter separate con-
tracts with the federal government consenting to answer
suits under RLUIPA.” Ibid. “Or,” the majority posits, “Con-
gress might have conditioned its funds on Louisiana’s
24    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                    JACKSON, J., dissenting

agreement to exercise its own regulatory powers to adopt a
state law cause of action enforceable against LDOC officers
who violate RLUIPA.” Ibid. Those arrangements, the ma-
jority assures us, would have sufficed for Spending Clause
purposes. But the one Congress chose fails because it hews
insufficiently to the tenets of binding contractual relation-
ships.
   Of course, the arrangement Congress chose is not far off
from the “untapped possibilities” the Court prefers. Ibid.
RLUIPA is no secret. Prison officials know when they sign
up to work at a state prison that they must obey the law or
face the consequences the law prescribes; this is simply “a
consequence of their decision to accept employment.” Rust
v. Sullivan, 500 U. S. 173, 199 (1991); Brief for Former Cor-
rectional Officials as Amici Curiae 13–16. What meaning-
ful difference would it make to have them sign a contract
attesting to that knowledge?10 Similarly, it makes no mean-
ingful difference for Congress to require a State to flex its
own legislative power to bind state officials rather than al-
low the Federal Government to make state officials liable
directly, as federal law so often does. The majority, in other
words, deals in form, not substance.
   The emptiness of the majority’s formalism is further il-
lustrated by the parade of horribles it trots out. The
——————
   10 Such attestation would likely be unnecessary even if this were a true

contract case. Under the doctrine of implied consent, courts may recog-
nize an agreement “which, although not embodied in an express contract,
is inferred . . . from conduct of the parties showing, in the light of the
surrounding circumstances, their tacit understanding.” Baltimore &
Ohio R. Co. v. United States, 261 U. S. 592, 597 (1923). “[A] reasonably
competent public official should know the law governing his conduct.”
Harlow v. Fitzgerald, 457 U. S. 800, 819 (1982); see also Heckler v. Com-
munity Health Services of Crawford Cty., Inc., 467 U. S. 51, 63 (1984)
(noting “the general rule that those who deal with the Government,” and
especially “those who seek public funds,” “are expected to know the law”).
And prison officials manifest their assent to RLUIPA by showing up to
work each day.
                     Cite as: 609 U. S. ____ (2026)                   25

                        JACKSON, J., dissenting

majority warns that, if RLUIPA’s individual-capacity dam-
ages provision is constitutional, Congress could subject col-
lege coaches to liability if they refuse “to permit
transgender athletes to play women’s sports,” or make doc-
tors personally liable if they “administe[r] certain vaccines
to children.” Ante, at 13. What the majority intends by
these examples is not clear. Congress could of course im-
pose these conditions on the colleges and medical practices
themselves, assuming they receive federal funds and the
laws are otherwise constitutional and not coercive.11 Con-
gress’s reach thus remains the same either way; all that
changes is whether noncompliant coaches and doctors lose
their jobs (in the majority’s world) or become liable in dam-
ages (in Congress’s, and therefore mine).
   So the Court’s ruling apparently boils down to dissatis-
faction with the precise way Congress structured RLUIPA.
Such hairsplitting undervalues Congress’s lawmaking pre-
rogative; we ought not substitute our rigid contract-based
preferences for Congress’s considered statutory design.
“Some play must be allowed for the joints of the machine,
and it must be remembered that legislatures are ultimate
guardians of the liberties and welfare of the people in quite
as great a degree as the courts.” Missouri, K. & T. R. Co. v.
May, 194 U. S. 267, 270 (1904). Taking this wisdom to
heart, the Court usually exhibits a well-founded “reticence
to invalidate the acts of the Nation’s elected leaders.” Na-
tional Federation of Independent Business v. Sebelius, 567
U. S. 519, 537–538 (2012) (opinion of ROBERTS, C. J.). In
my view, an ill-formed analogy to contract law is a regret-
table basis on which to turn reticence into enthusiasm.



——————
  11 A Title IX case currently pending before us asks whether Congress

imposed the majority’s first “hypothetical” condition on federally funded
educational institutions. See West Virginia v. B. P. J., No. 24–43.
26   LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                   JACKSON, J., dissenting

                               B
  Ultimately, I fear that the majority has now conjured an
apparition to replace a once-efficacious vision of Congress’s
spending power—a constitutional grant of authority that is
central to the design and functioning of our federal system.
History demonstrates that power’s significance.
  Under the Articles of Confederation, the power to tax re-
mained with the States. See Art. VIII; see also Art. II. This
arrangement left the Federal Government largely depend-
ent upon the States, eager for their cooperation but strug-
gling to secure it. D. Spencer, Sanctuary Cities and the
Power of the Purse: An Executive Dole Test, 106 Iowa
L. Rev. 1209, 1218 (2021). Thus, one major motivation for
the new Constitution was to give the Federal Government
the tools “to better incentivize states to work collectively for
the good of the entire Union.” Ibid. Granting Congress the
power to tax allowed the Federal Government to amass the
resources it needed to dangle those incentives. And grant-
ing Congress the power to spend allowed the Federal Gov-
ernment to follow through.
  Follow through it has. We owe to the Spending Clause,
for example, Title VI of the Civil Rights Act of 1964—a law
with which “few pieces of federal legislation rank in signif-
icance.” Bostock v. Clayton County, 590 U. S. 644, 649
(2020); see Students for Fair Admissions, Inc. v. President
and Fellows of Harvard College, 600 U. S. 181, 308 (2023)
(GORSUCH, J., concurring). We owe to the Spending Clause,
too, the relative cleanliness of our Nation’s air, see 42
U. S. C. §7401 et seq. (Clean Air Act), and the relative
health of our Nation’s populace, 42 U. S. C. §1395 et seq.;
§1396 et seq. (Medicare and Medicaid Acts). “Other exam-
ples, spanning virtually every domain of national and state
policy, abound.” Talevski, 599 U. S., at 198 (THOMAS, J.,
dissenting).
  While today’s decision does not endanger those laws di-
rectly, the majority’s reasoning casts a shadow that will not
                 Cite as: 609 U. S. ____ (2026)           27

                    JACKSON, J., dissenting

easily be escaped. No one knows what changes lie at the
end of a strict contract-law construction of the spending
power. But, as Members of this Court have long recognized,
importing contract principles wholesale could have “poten-
tially far-reaching consequences.” Barnes, 536 U. S., at 192
(Stevens, J., concurring in judgment).
   Indeed, it is our rejection of the strict contract analogy
that renders Spending Clause rights enforceable under
§1983. See Talevski, 599 U. S., at 229 (THOMAS, J., dissent-
ing); accord, D. Engdahl, The Contract Thesis of the Federal
Spending Power, 52 S. D. L. Rev. 496, 510 (2007). Simi-
larly, contracts presumably may not preempt state law, yet
Spending Clause legislation can do so. See, e.g., Dalton v.
Little Rock Family Planning Services, 516 U. S. 474, 476
(1996) (per curiam); Bennett v. Arkansas, 485 U. S. 395, 396
(1988) (per curiam); Philpott v. Essex County Welfare Bd.,
409 U. S. 413, 417 (1973); Townsend v. Swank, 404 U. S.
282, 286 (1971). And Congress likely could not hitch its
Necessary and Proper power to a mere contract, either, see
Engdahl, 52 S. D. L. Rev., at 532, but we have blessed just
this cocktail of enumerated powers, see Sabri, 541 U. S., at
605.
   This means that today’s decision might well land a seri-
ous blow to Congress’s effectiveness. Or it could end up
merely a bothersome statutory drafting guide: If Congress
adapts its Spending Clause legislation to fit the Court’s
newly prescribed formulas—and if the Court lets it do so—
then the majority’s robotic importation of contract princi-
ples will have little real-world effect. Either way, though,
“[t]he suggestion that [Spending Clause] statutes are not
‘law’ on the same level as other pieces of legislation makes
little sense.” See A. Gluck, Our [National] Federalism, 123
Yale L. J. 1996, 2031 (2014). And it makes even less sense
of the jurisprudence that has developed for decades around
those laws, to the great benefit of the American people.
28   LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                   JACKSON, J., dissenting

  As for RLUIPA itself, the consequences are more predict-
able. Prisoners like Landor who suffer violations of their
religious freedom in state prisons—no matter how bla-
tant—will often be left remediless. And encroachments on
prisoners’ statutory rights are likely to happen with fair fre-
quency, as state-empowered prison officials will have little
incentive to abide by federal law, even if it is handed to
them on a piece of paper.
                         *    *    *
  When Sossamon concluded that RLUIPA did not expose
States and their institutions to damages liability, JUSTICE
SOTOMAYOR lamented that the Court’s holding left RLUIPA
plaintiffs “to seek enforcement of [their] rights with one
hand tied behind their backs.” 563 U. S., at 303 (dissenting
opinion). Today the Court ties the other hand.
  To be clear, the Court’s decision does not eliminate all
damages liability from RLUIPA. See ante, at 4, n. 1. A pris-
oner who happens to be housed in a local rather than state
jail may recover damages from the municipality, which nei-
ther enjoys sovereign immunity, see Jinks v. Richland
County, 538 U. S. 456, 466 (2003), nor suffers from the
indirect-recipient defect the Court identifies, see Barnett v.
Short, 129 F. 4th 534, 542 (CA8 2025). Furthermore,
RLUIPA channels the commerce power, rather than the
spending power, in some of its applications. See 42 U. S. C.
§2000cc–1(b)(2). So the rare RLUIPA plaintiff who finds a
Commerce Clause hook may recover damages, too. See
Tripathy v. McKoy, 103 F. 4th 106, 115, n. 6 (CA2 2024).
But Congress did not enact such a patchwork scheme, and
the Constitution does not demand it.
  Yet the Court imposes such a scheme today. The Court
does so by concluding that, even where Congress can legis-
late under the Spending Clause, it may be left powerless to
enforce that legislation in the way it chooses. This
                  Cite as: 609 U. S. ____ (2026)           29

                     JACKSON, J., dissenting

development is as new as it is peculiar, and it devalues prec-
edent and congressional authority alike.

```

---
