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

## GROUP: _overhaul2/lake/cases/J.D.B. v. North Carolina.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "J.D.B. v. North Carolina"
type: case
citation: "564 U.S. 261 (2011)"
parallel_cite: "180 L. Ed. 2d 310; 131 S. Ct. 2394"
neutral_cite: 2011 U.S. LEXIS 4557
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2011
date_decided: 2011-06-16
docket: 09-11121
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2011-06-16
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: J.D.B. v. North Carolina
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/7345714/j-d-b-v-north-carolina/"
  cluster_id: 7345714
  opinion_id: 7263680
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Yarborough v. Alvarado]]", "[[Berkemer v. McCarty]]", "[[Miranda v. Arizona]]", "[[Stansbury v. California]]"]
aliases: ["In re J.D.B."]
tags: ["case", "fifth-amendment", "miranda", "custody", "juveniles", "age"]
holding: "A child's age is a relevant factor in the Miranda custody analysis when it was known to or objectively apparent to the officer — because…"
lake:
  record_id: J.D.B. v. North Carolina
  status: verified
  projected_at: 2026-07-06
---

# J.D.B. v. North Carolina

*564 U.S. 261 (2011)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
J.D.B., a 13-year-old seventh-grader, was removed from his classroom by a uniformed officer, taken to a closed conference room, and questioned by police and school officials for thirty to forty-five minutes about neighborhood break-ins. He was not given *[[Miranda v. Arizona|Miranda]]* warnings, was not told he could leave or call a guardian, and ultimately confessed. The North Carolina courts held his age was irrelevant to whether he was in custody.

## Issue
Whether a child's age is relevant to the *[[Miranda v. Arizona|Miranda]]* custody analysis when that age is known to, or objectively apparent to, the officer who questions the child.

## Rule
Yes. "It is beyond dispute that children will often feel bound to submit to police questioning when an adult in the same circumstances would feel free to leave. Seeing no reason for police officers or courts to blind themselves to that commonsense reality, we hold that a child's age properly informs the Miranda custody analysis." — *J.D.B. v. North Carolina*, 564 U.S. 261 (2011) (slip op., at 1). ^pin-op1

Including age keeps the analysis objective: "So long as the child's age was known to the officer at the time of the interview, or would have been objectively apparent to any reasonable officer, including age as part of the custody analysis requires officers neither to consider circumstances 'unknowable' to them . . . nor to 'anticipat[e] the frailties or idiosyncrasies' of the particular suspect whom they question." — *Id.* (slip op., at 11). ^pin-op11

## Application
J.D.B.'s age — 13 — was known to the officers, who questioned him at his school; because age is an objective fact bearing on how a reasonable child in his position would have understood the situation, the state courts erred in excluding it from the custody inquiry. The Court did not itself decide whether J.D.B. was in custody; it [[Reading and Citing Cases#on-remand|remanded]] for the state courts to address custody taking account of all the circumstances, including his age.

## Conclusion
A child's age, when known or objectively apparent, must be considered in the *[[Miranda v. Arizona|Miranda]]* custody analysis; the judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *J.D.B.* distinguishes [[Yarborough v. Alvarado]] and brings a child's age into the objective custody test of [[Miranda v. Arizona]] and [[Berkemer v. McCarty]].

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *J.D.B. v. North Carolina*, 564 U.S. 261 (2011) — https://www.courtlistener.com/opinion/218925/j-d-b-v-north-carolina/ — pinpoints given as slip-opinion pages (slip op., at 1, 11); CourtListener carries the slip opinion, paginated by slip page (opinion 218925).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "26a674d14ed20c0a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "J.D.B. v. North Carolina"}, "payload": {"all": [{"cite": "180 L. Ed. 2d 310", "page": "310", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "180"}, {"cite": "2011 U.S. LEXIS 4557", "page": "4557", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2011"}, {"cite": "131 S. Ct. 2394", "page": "2394", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "131"}, {"cite": "564 U.S. 261", "page": "261", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "564"}], "display": "564 U.S. 261", "official": {"cite": "564 U.S. 261", "page": "261", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "564"}, "official_selection_present": true, "record_id": "J.D.B. v. North Carolina"}}
{"assertion_id": "86444b8eb6b122f2", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op11", "record_id": "J.D.B. v. North Carolina"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op11", "pinpoint_status": "slip-only", "quote": "So long as the child's age was known to the officer at the time of the interview, or would have been objectively apparent to any reasonable officer, including age as part of the custody analysis requires officers neither to consider circumstances 'unknowable' to them . . . nor to 'anticipat[e] the frailties or idiosyncrasies' of the particular suspect whom they question.", "quote_fidelity": "mismatch", "record_id": "J.D.B. v. North Carolina", "star_marker": null}}
{"assertion_id": "a22ce7cb6f053746", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op1", "record_id": "J.D.B. v. North Carolina"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op1", "pinpoint_status": "slip-only", "quote": "--- # J.D.B. v. North Carolina *564 U.S. 261 (2011)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background J.D.B., a 13-year-old seventh-grader, was removed from his classroom by a uniformed officer, taken to a closed conference room, and questioned by police and school officials for thirty to forty-five minutes about neighborhood break-ins. He was not given *Miranda* warnings, was not told he could leave or call a guardian, and ultimately confessed. The North Carolina courts held his age was irrelevant to whether he was in custody. ## Issue Whether a child's age is relevant to the *Miranda* custody analysis when that age is known to, or objectively apparent to, the officer who questions the child. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "J.D.B. v. North Carolina", "star_marker": null}}
{"assertion_id": "ceecb06b253cc050", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "J.D.B. v. North Carolina"}, "payload": {"as_of_content": "2011-06-16", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "J.D.B. v. North Carolina", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — J.D.B. v. North Carolina

```json
{
  "schema_version": "s2.v1",
  "record_id": "J.D.B. v. North Carolina",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "J. D. B. v. North Carolina",
    "case_name_short": "",
    "case_name_full": "J. D. B. v. NORTH CAROLINA",
    "input_case_name": "J.D.B. v. North Carolina",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2011-06-16",
    "year": 2011,
    "docket": "09-11121",
    "cluster_id": 7345714,
    "lead_opinion_id": 7263680,
    "sibling_ids": [
      7263680,
      7263681
    ],
    "absolute_url": "/opinion/7345714/j-d-b-v-north-carolina/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 218925,
        "score": 120,
        "case_name": "J. D. B. v. North Carolina"
      },
      {
        "cluster_id": 7342486,
        "score": 20,
        "case_name": "J. D. B. v. North Carolina"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "564 U.S. 261",
      "volume": "564",
      "reporter": "U.S.",
      "page": "261",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "180 L. Ed. 2d 310",
        "volume": "180",
        "reporter": "L. Ed. 2d",
        "page": "310",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 S. Ct. 2394",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "2394",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2011 U.S. LEXIS 4557",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "4557",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "180 L. Ed. 2d 310",
        "volume": "180",
        "reporter": "L. Ed. 2d",
        "page": "310",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 U.S. LEXIS 4557",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "4557",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 S. Ct. 2394",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "2394",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "564 U.S. 261",
        "volume": "564",
        "reporter": "U.S.",
        "page": "261",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "564 U.S. 261",
    "official_selection": {
      "court_class": "scotus",
      "selected": "564 U.S. 261",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op1",
      "page": null,
      "quote": "--- # J.D.B. v. North Carolina *564 U.S. 261 (2011)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background J.D.B., a 13-year-old seventh-grader, was removed from his classroom by a uniformed officer, taken to a closed conference room, and questioned by police and school officials for thirty to forty-five minutes about neighborhood break-ins. He was not given *Miranda* warnings, was not told he could leave or call a guardian, and ultimately confessed. The North Carolina courts held his age was irrelevant to whether he was in custody. ## Issue Whether a child's age is relevant to the *Miranda* custody analysis when that age is known to, or objectively apparent to, the officer who questions the child. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op11",
      "page": null,
      "quote": "So long as the child's age was known to the officer at the time of the interview, or would have been objectively apparent to any reasonable officer, including age as part of the custody analysis requires officers neither to consider circumstances 'unknowable' to them . . . nor to 'anticipat[e] the frailties or idiosyncrasies' of the particular suspect whom they question.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2011-06-16",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "J.D.B. v. North Carolina",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Mattis",
          "cluster_id": 9459197,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re E.W.",
          "cluster_id": 2770572,
          "cite": [
            "198 Vt. 311",
            "2015 VT 7",
            "114 A.3d 112",
            "2015 Vt. LEXIS 7"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Morgan v. Swanson",
          "cluster_id": 8441074,
          "cite": [
            "659 F.3d 359",
            "2011 U.S. App. LEXIS 19656",
            "2011 WL 4470233"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vega v. Tekoh",
          "cluster_id": 6480695,
          "cite": [
            "597 U.S. 134",
            "213 L. Ed. 2d 479",
            "142 S. Ct. 2095"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Aalim (Slip Opinion)",
          "cluster_id": 4394360,
          "cite": [
            "2017 Ohio 2956",
            "150 Ohio St. 3d 489"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Long",
          "cluster_id": 2690164,
          "cite": [
            "2014 Ohio 849",
            "138 Ohio St. 3d 478",
            "8 N.E.3d 890"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sara Dees v. County of San Diego",
          "cluster_id": 4756523,
          "cite": [
            "960 F.3d 1145"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rachel Scanlon v. County of Los Angeles",
          "cluster_id": 9471587,
          "cite": [
            "92 F.4th 781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jones",
          "cluster_id": 5145789,
          "cite": [
            "55 A.3d 432",
            "2012 ME 126",
            "2012 Me. LEXIS 126"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chad Soderman",
          "cluster_id": 4841363,
          "cite": [
            "983 F.3d 369"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathan Boyer v. Darrel Vannoy, Warden",
          "cluster_id": 4409622,
          "cite": [
            "863 F.3d 428",
            "2017 U.S. App. LEXIS 12764",
            "2017 WL 3016043"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The PEOPLE of the State of Colorado, Petitioner/Cross-Respondent, IN the INTEREST OF T.B., Respondent/Cross-Petitioner",
          "cluster_id": 10018886,
          "cite": [
            "489 P.3d 752"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Coulter",
          "cluster_id": 6624576,
          "cite": [
            "41 F.4th 451"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. G.O.",
          "cluster_id": 9480222,
          "cite": [
            "543 P.3d 1096"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Bush",
          "cluster_id": 9450931,
          "cite": [
            "231 N.E.3d 569",
            "2023 Ohio 4473"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Bermudez",
          "cluster_id": 6589872,
          "cite": [
            "83 Mass. App. Ct. 46",
            "980 N.E.2d 462",
            "2012 Mass. App. LEXIS 294"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. J.H.-M.",
          "cluster_id": 10376010,
          "cite": [
            "566 P.3d 847"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In re T.D.S.",
          "cluster_id": 9476954,
          "cite": [
            "2024 Ohio 595"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jimmie Bowen v. Secretary, Florida Department of Corrections",
          "cluster_id": 9475524,
          "cite": [
            "92 F.4th 1328"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ervin Leggette",
          "cluster_id": 9357989,
          "cite": [
            "57 F.4th 406"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matter of Luis P.",
          "cluster_id": 10688544,
          "cite": [
            "32 N.Y.3d 1165",
            "2018 NY Slip Op 08427"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Campos-Ayala",
          "cluster_id": 9514436,
          "cite": [
            "105 F.4th 235"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Raymond Lewis v. Chance Andes",
          "cluster_id": 9483149,
          "cite": [
            "95 F.4th 1166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Heatherington",
          "cluster_id": 6462570,
          "cite": [
            "2022 Ohio 1375"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jorge Leal",
          "cluster_id": 4893446,
          "cite": [
            "1 F.4th 545"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In re R.C.",
          "cluster_id": 4745406,
          "cite": [
            "2020 Ohio 1486"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Logan T. Kruckenberg Anderson",
          "cluster_id": 10111918,
          "cite": [
            "2024 WI App 45"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(7263680 OR 7263681) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 69,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 69,
        "triage_read": 3,
        "triage_snippet_classified": 66
      },
      "lane2_top_cited": {
        "query": "cites:(7263680 OR 7263681)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xJnM9NzMzNTgzNCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%287263680+OR+7263681%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(7263680 OR 7263681)",
        "reviewed": 33,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 33,
        "triage_read": 1,
        "triage_snippet_classified": 32
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(7263680 OR 7263681)",
    "indexed_citing_opinions": 80,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 7263680,
        "count": 80,
        "count_source": "search"
      },
      {
        "opinion_id": 7263681,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 563,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/j-d-b-v-north-carolina.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2NDk2MjImcz05NDcxNTg3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%287263680+OR+7263681%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T08:42:32Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:43:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:43:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:46:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:43:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — J.D.B. v. North Carolina

```
<opinion type="majority">
<p id="b360-4">OPINION OF THE COURT</p>
<p id="b360-5">[<span class="citation no-link">564 U.S. 264</span>]</p>
<author id="b360-6">Justice Sotomayor</author>
<p id="ARdO">delivered the opinion of the Court.</p>
<p id="b360-7">This case presents the question whether the age of a child subjected to police questioning is relevant to the custody analysis of <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U.S. 436</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span> (1966). It is beyond dispute that children will often feel bound to submit to police questioning when an adult in the same circumstances</p>
<p id="b360-15">[<span class="citation no-link">564 U.S. 265</span>]</p>
<p id="b360-16">would feel free to leave. Seeing no reason for police officers or courts to blind themselves to that <page-number citation-index="1" label="319">*319</page-number>commonsense reality, we hold that  a child’s age properly informs the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>custody analysis.</p>
<p id="b361-4">I</p>
<p id="b361-5">A</p>
<p id="b361-6">Petitioner J. D. B. was a 13-year-old, seventh-grade student attending class at Smith Middle School in Chapel Hill, North Carolina, when he was removed from his classroom by a uniformed police officer, escorted to a closed-door conference room, and questioned by police for at least half an hour.</p>
<p id="b361-7">This was the second time that police questioned J. D. B. in the span of a week. Five days earlier, two home break-ins occurred, and various items were stolen. Police stopped and questioned J. D. B. after he was seen behind a residence in the neighborhood where the crimes occurred. That same day, police also spoke to J. D. B.’s grandmother—his legal guardian—as well as his aunt.</p>
<p id="b361-8">Police later learned that a digital camera matching the description of one of the stolen items had been found at J. D. B.’s middle school and seen in J. D. B.’s possession. Investigator DiCostanzo, the juvenile investigator with the local police force who had been assigned to the case, went to the school to question J. D. B. Upon arrival, DiCostanzo informed the uniformed police officer on detail to the school (a so-called school resource officer), the assistant principal, and an administrative intern that he was there to question J. D. B. about the break-ins. Although DiCostanzo asked the school administrators to verify J. D. B.’s date of birth, address, and parent contact information from school records, neither the police officers nor the school administrators contacted J. D. B.’s grandmother.</p>
<p id="b361-10">The uniformed officer interrupted J. D. B.’s afternoon social studies class, removed J. D. B. from the classroom, and</p>
<p id="b361-11">[<span class="citation no-link">564 U.S. 266</span>]</p>
<p id="b361-12">escorted him to a school conference room.<footnotemark>1</footnotemark> There, J. D. B. was met by DiCostanzo, the assistant principal, and the administrative intern. The door to the conference room was closed. With the two police officers and the two administrators present, J. D. B. was questioned for the next 30 to 45 minutes. Prior to the commencement of questioning, J. D. B. was given neither <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings nor the opportunity to speak to his grandmother. Nor was he informed that he was free to leave the room.</p>
<p id="b361-13">Questioning began with small talk— discussion of sports and J. D. B.’s family life. DiCostanzo asked, and J. D. B. agreed, to discuss the events of the prior weekend. Denying any wrongdoing, J. D. B. explained that he had been in the neighborhood where the crimes occurred because he was seeking work mowing lawns. DiCostanzo pressed J. D. B. for additional detail about his efforts to obtain work; asked J. D. B. to explain a prior incident, when one of the victims returned home to find J. D. B. behind her house; and confronted J. D. B. with the stolen camera. The assistant principal urged J. D. B. to “do the right thing,” warning J. D. B. that “the truth always comes out in the end.”App. 99a, 112a.</p>
<p id="b362-3"><page-number citation-index="1" label="320">*320</page-number>Eventually, J. D. B. asked whether he would “still be in trouble” if he returned the “stuff.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span> </em>In response, DiCostanzo explained that return of the stolen items would be helpful, but “this thing is going to court” regardless. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span> </em>at 112a; <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">ibid.</a></span> </em>(“[W]hat’s done is done[;] now you need to help yourself by making it right”); see also <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">id.,</a></span> </em>at 99a. DiCostanzo then warned that he may need to seek a secure custody order if he believed that J. D. B. would continue to break into other homes. When J. D. B. asked what a secure custody</p>
<p id="b362-4">[<span class="citation no-link">564 U.S. 267</span>]</p>
<p id="b362-5">order was, DiCostanzo explained that “it’s where you get sent to juvenile detention before court.” <em><span class="citation no-link">Id.,</span> </em>at 112a.</p>
<p id="b362-6">After learning of the prospect of juvenile detention, J. D. B. confessed that he and a friend were responsible for the break-ins. DiCostanzo only then informed J. D. B. that he could refuse to answer the investigator’s questions and that he was free to leave.<footnotemark>2</footnotemark> Asked whether he understood, J. D. B. nodded and provided further detail, including information about the location of the stolen items. Eventually J. D. B. wrote a statement, at DiCostanzo’s request. When the bell rang indicating the end of the school-day, J. D. B. was allowed to leave to catch the bus home.</p>
<p id="b362-7">B</p>
<p id="b362-8">Two juvenile petitions were filed against J. D. B., each alleging one count of breaking and entering and one count of larceny. J. D. B.’s public defender moved to suppress his statements and the evidence derived therefrom, arguing that suppression was necessary because J. D. B. had been “interrogated by police in a custodial setting without being afforded <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning[s],” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span> </em>at 89a, and because his</p>
<p id="b362-10">[<span class="citation no-link">564 U.S. 268</span>]</p>
<p id="b362-11">statements were involuntary under the totality of the circumstances test, <em><span class="citation no-link">id.,</span> </em>at 142a; see <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218, 226</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S. Ct. 2041</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L. Ed. 2d 854</a></span> (1973) (due process precludes admission of a confession where “a defendant’s will was overborne” by the circumstances of the interrogation). After a suppression hearing at which DiCostanzo and J. D. B. testified, the trial court denied the motion, deciding that J. D. B. was not in custody at the time of the schoolhouse interrogation and that his statements were voluntary. As a result, J. D. B. entered a transcript of admission to all four counts, renewing his objection enial of his motion to suppress, and the court adjudicated J. D. B. delinquent.</p>
<p id="b362-12">A divided panel of the North Carolina Court of Appeals affirmed. <em>In re J. D. B., </em><span class="citation" data-id="8899249"><a href="/opinion/8911477/in-re-jdb/" aria-description="Citation for case: In re J.D.B.">196 N.C. App. 234</a></span>, <span class="citation" data-id="8899249"><a href="/opinion/8911477/in-re-jdb/" aria-description="Citation for case: In re J.D.B.">674 S.E.2d 795</a></span> (2009). The North Carolina Supreme Court held, over two dissents, that J. D. B. was not in custody when he confessed, “declin<page-number citation-index="1" label="321">*321</page-number>[ing] to extend the test for custody to include consideration of the age ... of an individual subjected to questioning by police.” <em>In re J. D. B., </em><span class="citation" data-id="6722655"><a href="/opinion/6835533/in-re-jdb/#672" aria-description="Citation for case: In re J.D.B.">363 N.C. 664, 672</a></span>, <span class="citation" data-id="6722655"><a href="/opinion/6835533/in-re-jdb/#140" aria-description="Citation for case: In re J.D.B.">686 S.E.2d 135, 140</a></span> (2009) <footnotemark>3</footnotemark></p>
<p id="b363-4">We granted certiorari to determine whether the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>custody analysis includes consideration of a juvenile suspect’s age. <span class="citation multiple-matches"><a href="/c/U.S./562/1001/">562 U.S. 1001</a></span>, <span class="citation multiple-matches"><a href="/c/S.%20Ct./131/502/">131 S. Ct. 502</a></span>, <span class="citation multiple-matches"><a href="/c/L.%20Ed.%202d/178/368/">178 L. Ed. 2d 368</a></span> (2010).</p>
<p id="b363-5">II</p>
<p id="b363-6">A</p>
<p id="b363-7">Any police interview of an individual suspected of a crime has “coercive aspects to it.” <em>Oregon </em>v. <em>Mathiason, </em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U.S. 492, 495</a></span>, <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">97 S. Ct. 711</a></span>, <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">50 L. Ed. 2d 714</a></span> (1977) <em>(per curiam). </em>Only those interrogations that occur while a suspect is in police custody, however, “heighte[n] the risk” that statements obtained are not the</p>
<p id="b363-8">[<span class="citation no-link">564 U.S. 269</span>]</p>
<p id="b363-9">product of the suspect’s free choice. <em>Dickerson </em>v. <em>United States, </em><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#435" aria-description="Citation for case: Dickerson v. United States">530 U.S. 428, 435</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">120 S. Ct. 2326</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">147 L. Ed. 2d 405</a></span> (2000).</p>
<p id="b363-10">By its very nature, custodial police interrogation entails “inherently compelling pressures.” <em>Miranda, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 467</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>. Even for an adult, the physical and psychological isolation of custodial interrogation can “undermine the individual’s will to resist and . . . compel him to speak where he would not otherwise do so freely.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span> </em>Indeed, the pressure of custodial interrogation is so immense that it “can induce a frighteningly high percentage of people to confess to crimes they never committed.” <em>Corley </em>v. <em>United States, </em><span class="citation" data-id="145888"><a href="/opinion/145888/corley-v-united-states/#321" aria-description="Citation for case: Corley v. United States">556 U.S. 303, 321</a></span>, <span class="citation" data-id="145888"><a href="/opinion/145888/corley-v-united-states/" aria-description="Citation for case: Corley v. United States">129 S. Ct. 1558</a></span>, <span class="citation" data-id="145888"><a href="/opinion/145888/corley-v-united-states/" aria-description="Citation for case: Corley v. United States">173 L. Ed. 2d 443</a></span> (2009) (citing Drizin <em>&amp; </em>Leo, The Problem of False Confessions in the Post-DNA World, <span class="citation no-link">82 N.C. L. Rev. 891</span>, 906-907 (2004)); see also <em>Miranda, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#455" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 455, n. 23</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>. That risk is all the more troubling—and recent studies suggest, all the more acute—when the subject of custodial interrogation is a juvenile. See Brief for Center on Wrongful Convictions of Youth et al. as <em>Amici Curiae </em>21-22 (collecting empirical studies that “illustrate the heightened risk of false confessions from youth”).</p>
<p id="b363-12">Recognizing that the inherently coercive nature of custodial interrogation “blurs the line between voluntary and involuntary statements,” <em>Dickerson, </em><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#435" aria-description="Citation for case: Dickerson v. United States">530 U.S., at 435</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">120 S. Ct. 2326</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">147 L. Ed. 2d 405</a></span>, this Court in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>adopted a set of prophylactic measures designed to safeguard the constitutional guarantee against self-incrimination. Prior to questioning, a suspect “must be warned that he has a right to remain silent, that any statement he does make may be used as evidence against him, and that he has a right to the presence of an attorney, either retained or appointed.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 444</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>; see also <em>Florida </em>v. <em>Powell, </em><span class="citation" data-id="9413180"><a href="/opinion/1736/florida-v-powell/#60" aria-description="Citation for case: Florida v. Powell">559 U.S. 50, 60</a></span>, <span class="citation" data-id="9413180"><a href="/opinion/1736/florida-v-powell/" aria-description="Citation for case: Florida v. Powell">130 S. Ct. 1195</a></span>, <span class="citation" data-id="9413180"><a href="/opinion/1736/florida-v-powell/" aria-description="Citation for case: Florida v. Powell">175 L. Ed. 2d 1009</a></span> (2010) (“The four warnings <em>Miranda </em>requires are invariable, but this Court has not dictated the words in which the essential information must be conveyed”). And, if a suspect makes a statement during custodial interrogation, the burden is on the Government to show, as a “prerequisitje]” to the statement’s admissibility as evi<page-number citation-index="1" label="322">*322</page-number>dence</p>
<p id="b364-4">[<span class="citation no-link">564 U.S. 270</span>]</p>
<p id="b364-5">in the Government’s case in chief, that the defendant “voluntarily, knowingly and intelligently” waived his <em>rights.</em><footnotemark><em>4</em></footnotemark><em> Miranda, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 444, 475-476</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>; <em>Dickerson, </em><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#443" aria-description="Citation for case: Dickerson v. United States">530 U.S., at 443-444</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">120 S. Ct. 2326</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">147 L. Ed. 2d 405</a></span>.</p>
<p id="b364-6">Because these measures protect the individual against the coercive nature of custodial interrogation, they are required “ ‘only where there has been such a restriction on a person’s freedom as to render him “in custody.” ’ ” <em>Stansbury </em>v. <em>California, </em><span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#322" aria-description="Citation for case: Stansbury v. California">511 U.S. 318, 322</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">114 S. Ct. 1526</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">128 L. Ed. 2d 293</a></span> (1994) <em>(per curiam) </em>(quoting <em>Mathiason, </em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U.S., at 495</a></span>, <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">97 S. Ct. 711</a></span>, <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">50 L. Ed. 2d 714</a></span>). As we have repeatedly emphasized,  whether a suspect is “in custody” is an objective inquiry.</p>
<blockquote id="b364-7">“Two discrete inquiries are essential to the determination: first, what were the circumstances surrounding the interrogation; and second, given those circumstances, would a reasonable person have felt he or she was at liberty to terminate the interrogation and leave. Once the scene is set and the players’ lines and actions are reconstructed, the court must apply an objective test to resolve the ultimate inquiry: was there a formal arrest or restraint on freedom of movement of the degree associated with formal arrest.” <em>Thompson </em>v. <em>Keohane, </em><span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/#112" aria-description="Citation for case: Thompson v. Keohane">516 U.S. 99, 112</a></span>, <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/" aria-description="Citation for case: Thompson v. Keohane">116 S. Ct. 457</a></span>, <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/" aria-description="Citation for case: Thompson v. Keohane">133 L. Ed. 2d 383</a></span> (1995) (internal quotation marks, alteration, and footnote omitted).</blockquote>
<p id="b364-8">See also <em>Yarborough </em>v. <em>Alvarado, </em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#662" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S. 652, 662-663</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span> (2004); <em>Stansbury, </em><span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#323" aria-description="Citation for case: Stansbury v. California">511 U.S., at 323</a></span>; <em>Berkemer </em>v. <em>McCarty, </em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#442" aria-description="Citation for case: Berkemer v. McCarty">468 U.S. 420, 442</a></span>, and n. 35, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">104 S. Ct. 3138</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">82 L. Ed. 2d 317</a></span> (1984).  Rather than demarcate a limited set of relevant circumstances, we have required police officers and courts to “examine all of the circumstances</p>
<p id="b364-10">[<span class="citation no-link">564 U.S. 271</span>]</p>
<p id="anf-dedup-1">surrounding the interrogation,” <em>Stansbury, </em><span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#322" aria-description="Citation for case: Stansbury v. California">511 U.S., at 322</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">114 S. Ct. 1526</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">128 L. Ed. 2d 293</a></span>, including any circumstance that “would have affected how a reasonable person” in the suspect’s position “would perceive his or her freedom to leave,” <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#325" aria-description="Citation for case: Stansbury v. California"><em>id., </em>at 325</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">114 S. Ct. 1526</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">128 L. Ed. 2d 293</a></span>. On the other hand, the “subjective views harbored by either the interrogating officers or the person being questioned” are irrelevant. <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#323" aria-description="Citation for case: Stansbury v. California"><em>Id., </em>at 323</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">114 S. Ct. 1526</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">128 L. Ed. 2d 293</a></span>. The test, in other words, involves no consideration of the “actual mindset” of the particular suspect subjected to police questioning. <em>Alvarado, </em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#667" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 667</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span>; see also <em>California </em>v. <em>Beheler, </em><span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1125" aria-description="Citation for case: California v. Beheler">463 U.S. 1121, 1125, n. 3</a></span>, <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/" aria-description="Citation for case: California v. Beheler">103 S. Ct. 3517</a></span>, <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/" aria-description="Citation for case: California v. Beheler">77 L. Ed. 2d 1275</a></span> (1983) <em>(per curiam).</em></p>
<p id="b364-11">The benefit of the objective custody analysis is that it is “designed to give clear guidance to the police.” <em>Alvarado, </em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#668" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 668</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span>. But see <em>Berkemer, </em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#441" aria-description="Citation for case: Berkemer v. McCarty">468 U.S., at 441</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">104 S. Ct. 3138</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">82 L. Ed. 2d 317</a></span> (recognizing the “occasional!] . . . difficulty” that police and courts nonetheless have in “deciding exactly when a suspect has been taken into custody”). Police must make in-the-moment judgments as to <page-number citation-index="1" label="323">*323</page-number>when to administer <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. By limiting analysis to the objective circumstances of the interrogation, and asking how a reasonable person in the suspect’s position would understand his freedom to terminate questioning and leave, the objective test avoids burdening police with the task of anticipating the idiosyncrasies of every individual suspect and divining how those particular traits affect each person’s subjective state of mind. See <em>id., </em>at 430-431, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">104 S. Ct. 3138</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">82 L. Ed. 2d 317</a></span> (officers are not required to “make guesses” as to circumstances “unknowable” to them at the time); <em>Alvarado, </em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#668" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 668</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span> (officers are under no duty “to consider . . . contingent psychological factors when deciding when suspects should be advised of their <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights”).</p>
<p id="b365-5">B</p>
<p id="b365-6">The State and its <em>amici </em>contend that a child’s age has no place in the custody analysis, no matter how young the child subjected to police questioning. We cannot agree.  In some circumstances, a child’s age “would have affected how a reasonable</p>
<p id="b365-7">[<span class="citation no-link">564 U.S. 272</span>]</p>
<p id="b365-8">person” in the suspect’s position “would perceive his or her freedom to leave.” <em>Stansbury, </em><span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#325" aria-description="Citation for case: Stansbury v. California">511 U.S., at 325</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">114 S. Ct. 1526</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">128 L. Ed. 2d 293</a></span>. That is, a reasonable child subjected to police questioning will sometimes feel pressured to submit when a reasonable adult would feel free to go. We think it clear that courts can account for that reality without doing any damage to the objective nature of the custody analysis.</p>
<p id="b365-9">A child’s age is far “more than a chronological fact.” <em>Eddings </em>v. <em>Oklahoma, </em><span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/#115" aria-description="Citation for case: Eddings v. Oklahoma">455 U.S. 104, 115</a></span>, <span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/" aria-description="Citation for case: Eddings v. Oklahoma">102 S. Ct. 869</a></span>, <span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/" aria-description="Citation for case: Eddings v. Oklahoma">71 L. Ed. 2d 1</a></span> (1982); accord, <em>Gall </em>v. <em>United States, </em><span class="citation" data-id="9435287"><a href="/opinion/145843/gall-v-united-states/#58" aria-description="Citation for case: Gall v. United States">552 U.S. 38, 58</a></span>, <span class="citation" data-id="9435287"><a href="/opinion/145843/gall-v-united-states/" aria-description="Citation for case: Gall v. United States">128 S. Ct. 586</a></span>, <span class="citation" data-id="9435287"><a href="/opinion/145843/gall-v-united-states/" aria-description="Citation for case: Gall v. United States">169 L. Ed. 2d 445</a></span> (2007); <em>Roper </em>v. <em>Simmons, </em><span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/#569" aria-description="Citation for case: Roper v. Simmons">543 U.S. 551, 569</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">125 S. Ct. 1183</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">161 L. Ed. 2d 1</a></span> (2005); <em>Johnson </em>v. <em>Texas, </em><span class="citation" data-id="9432871"><a href="/opinion/112897/johnson-v-texas/#367" aria-description="Citation for case: Johnson v. Texas">509 U.S. 350, 367</a></span>, <span class="citation" data-id="9432871"><a href="/opinion/112897/johnson-v-texas/" aria-description="Citation for case: Johnson v. Texas">113 S. Ct. 2658</a></span>, <span class="citation" data-id="9432871"><a href="/opinion/112897/johnson-v-texas/" aria-description="Citation for case: Johnson v. Texas">125 L. Ed. 2d 290</a></span> (1993). It is a fact that “generates commonsense conclusions about behavior and perception.” <em>Alvarado, </em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#674" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 674</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span> (Breyer, J., dissenting). Such conclusions apply broadly to children as a class. And, they are self-evident to anyone who was a child once himself, including any police officer or judge.</p>
<p id="b365-11">Time and again, this Court has drawn these commonsense conclusions for itself. We have observed that children “generally are less mature and responsible than adults,” <em>Eddings, </em><span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/#115" aria-description="Citation for case: Eddings v. Oklahoma">455 U.S., at 115-116</a></span>, <span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/" aria-description="Citation for case: Eddings v. Oklahoma">102 S. Ct. 869</a></span>, <span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/" aria-description="Citation for case: Eddings v. Oklahoma">71 L. Ed. 2d 1</a></span>; that they “often lack the experience, perspective, and judgment to recognize and avoid choices that could be detrimental to them,” <em>Bellotti </em>v. <em>Baird, </em><span class="citation" data-id="9427704"><a href="/opinion/110145/bellotti-v-baird/#635" aria-description="Citation for case: Bellotti v. Baird">443 U.S. 622, 635</a></span>, <span class="citation" data-id="9427704"><a href="/opinion/110145/bellotti-v-baird/" aria-description="Citation for case: Bellotti v. Baird">99 S. Ct. 3035</a></span>, <span class="citation" data-id="9427704"><a href="/opinion/110145/bellotti-v-baird/" aria-description="Citation for case: Bellotti v. Baird">61 L. Ed. 2d 797</a></span> (1979) (plurality opinion); that they “are more vulnerable or susceptible to . . . outside pressures” than adults, <em>Roper, </em><span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/#569" aria-description="Citation for case: Roper v. Simmons">543 U.S., at 569</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">125 S. Ct. 1183</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">161 L. Ed. 2d 1</a></span>; and so on. See <em>Graham </em>v. <em>Florida, </em><span class="citation" data-id="6680682"><a href="/opinion/6795859/graham-v-florida/#68" aria-description="Citation for case: Graham v. Florida">560 U.S. 48, 68</a></span>, <span class="citation" data-id="6680682"><a href="/opinion/6795859/graham-v-florida/" aria-description="Citation for case: Graham v. Florida">130 S. Ct. 2011</a></span>, <span class="citation" data-id="6680682"><a href="/opinion/6795859/graham-v-florida/" aria-description="Citation for case: Graham v. Florida">176 L. Ed. 2d 825</a></span> (2010) (finding no reason to “reconsider” these observations about the common “nature of juveniles”). Addressing the specific context of police interrogation, we have observed that events that “would leave a man cold and unimpressed can overawe and overwhelm a lad in his early teens.” <em>Haley </em>v. <em>Ohio, </em><span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/#599" aria-description="Citation for case: Haley v. Ohio">332 U.S. 596, 599</a></span>, <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/" aria-description="Citation for case: Haley v. Ohio">68 S. Ct. 302</a></span>, <span class="citation no-link">92 L. Ed. 224</span> (1948) (plurality opinion); see also <em>Gallegos </em>v. <em>Colorado, </em><span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/#54" aria-description="Citation for case: Gallegos v. Colorado">370 U.S. 49, 54</a></span>, <span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/" aria-description="Citation for case: Gallegos v. Colorado">82 S. Ct. 1209</a></span>, <span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/" aria-description="Citation for case: Gallegos v. Colorado">8 L. Ed. 2d 325</a></span> (1962) <page-number citation-index="1" label="324">*324</page-number>(  “[N]o matter how sophisticated,” a juvenile subject of police interrogation “cannot be compared” to an</p>
<p id="AU2E">[<span class="citation no-link">564 U.S. 273</span>]</p>
<p id="b366-4">adult subject). Describing no one child in particular, these observations restate what “any parent knows”—indeed, what any person knows—about children generally. <em>Roper, </em><span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/#569" aria-description="Citation for case: Roper v. Simmons">543 U.S., at 569</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">125 S. Ct. 1183</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">161 L. Ed. 2d 1</a></span>.<footnotemark>5</footnotemark></p>
<p id="b366-6">Our various statements to this effect are far from unique. The law has historically reflected the same assumption that children characteristically lack the capacity to exercise mature judgment and possess only an incomplete ability to understand the world around them. See, <em>e.g., </em>1 W. Blackstone, Commentaries on the Laws of England *464-*465 (hereinafter Blackstone) (explaining that limits on children’s legal capacity under the common law “secure them from hurting themselves by their own improvident acts”). Like this Court’s own generalizations, the legal disqualifications placed on children as a <em>class—e.g., </em>limitations on their ability to alienate property, enter a binding contract enforceable against them, and marry without parental consent—exhibit the settled understanding that the differentiating characteristics of youth are universal.<footnotemark>6</footnotemark></p>
<p id="b366-8">[<span class="citation no-link">564 U.S. 274</span>]</p>
<p id="b366-9">Indeed,  even where a “reasonable person” standard otherwise applies, the common law has reflected the reality that children are not adults. In negligence suits, for instance, where liability turns on what an objectively reasonable person would do in the circumstances, “[a]ll American jurisdictions accept the idea that a person’s childhood is a relevant circumstance” to be considered. Restatement (Third) of Torts § 10, Comment <em>b, </em>p. 117 (2005); see also <em>id., </em>Reporters’ Note, pp. 121-122 (collecting cases); Restatement (Second) of Torts § 283A, Comment <em>b, </em>p. 15 (1963-1964) (“[T]here is a wide basis of community experience upon which it is possible, as a practical matter, to determine what is to be expected of [children]”).</p>
<p id="b366-10">As this discussion establishes,  “[o]ur history is replete with laws and judicial recognition” that children cannot be viewed simply as miniature adults. <em>Eddings, </em><span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/#115" aria-description="Citation for case: Eddings v. Oklahoma">455 U.S., at 115-116</a></span>, <span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/" aria-description="Citation for case: Eddings v. Oklahoma">102 S. Ct. 869</a></span>, <span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/" aria-description="Citation for case: Eddings v. Oklahoma">71 L. Ed. 2d 1</a></span>. We see no justification for taking a different course here. So long as the child’s age <page-number citation-index="1" label="325">*325</page-number>was known to the officer at the time of the interview, or would have been objectively apparent to any reasonable officer, including age as part of the custody analysis requires officers neither to consider circumstances “unknowable” to them, <em>Berkemer, </em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#430" aria-description="Citation for case: Berkemer v. McCarty">468 U.S., at 430</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">104 S. Ct. 3138</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">82 L. Ed. 2d 317</a></span>, nor to “anticipat[e] the frailties or idiosyncrasies” of the particular suspect whom they question, <em>Alvarado, </em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#662" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 662</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span> (internal quotation marks omitted). The same “wide basis of community experience” that makes it possible, as an objective matter, “to determine what is to be expected” of children in other contexts, Restatement (Second) of Torts § 283A, at 15; see <em>supra, </em>at 273, 180 L. Ed. 2d, at 324, and n. 6, likewise makes it possible to know what to expect of children subjected to police questioning.</p>
<p id="b367-4">[<span class="citation no-link">564 U.S. 275</span>]</p>
<p id="b367-5">In other words, a child’s age differs from other personal characteristics that, even when known to police, have no objectively discernible relationship to a reasonable person’s understanding of his freedom of action. <em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">Alvarado</a></span> </em>holds, for instance, that a suspect’s prior interrogation history with law enforcement has no role to play in the custody analysis because such experience could just as easily lead a reasonable person to feel free to walk away as to feel compelled to stay in place. <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#668" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 668</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span>. Because the effect in any given case would be “contingent [on the] psycholog [y]” of the individual suspect, the Court explained, such experience cannot be considered without compromising the objective nature of the custody analysis. <em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">Ibid.</a></span> </em>A child’s age, however, is different. Precisely because childhood yields objective conclusions like those we have drawn ourselves— among others, that children are “most susceptible to influence,” <em>Eddings, </em><span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/#115" aria-description="Citation for case: Eddings v. Oklahoma">455 U.S., at 115</a></span>, <span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/" aria-description="Citation for case: Eddings v. Oklahoma">102 S. Ct. 869</a></span>, <span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/" aria-description="Citation for case: Eddings v. Oklahoma">71 L. Ed. 2d 1</a></span>, and “outside pressures,” <em>Roper, </em><span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/#569" aria-description="Citation for case: Roper v. Simmons">543 U.S., at 569</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">125 S. Ct. 1183</a></span>, 161 L. Ed. 2d 1—considering age in the custody analysis in no way involves a determination of how youth “subjectively affect[s] the mindset” of any particular child, Brief for Respondent 14.<footnotemark>7</footnotemark></p>
<p id="b367-7">In fact, in many cases involving juvenile suspects, the custody analysis would be nonsensical absent some consideration of the suspect’s age. This case is a prime example. Were the court precluded from taking J. D. B.’s youth into account, it would be forced to evaluate the circumstances present here through the eyes of a reasonable person of average years. In other words, how would a reasonable adult understand his situation, after being removed from a seventh-grade social studies class by a uniformed school resource</p>
<p id="a3j-dedup-0">[<span class="citation no-link">564 U.S. 276</span>]</p>
<p id="b367-8">officer; being encouraged by his assistant principal to “do the right thing”; and being warned by a police investigator of the prospect of juvenile detention and separation from his guardian and primary caretaker? To describe such an inquiry is to demonstrate its absurdity. Neither officers nor courts can reasonably evaluate the effect of objective circumstances that, by their nature, are specific to children with<page-number citation-index="1" label="326">*326</page-number>out accounting for the age of the child subjected to those circumstances.</p>
<p id="b368-4">Indeed, although the dissent suggests that concerns “regarding the application of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>custody rule to minors can be accommodated by considering the unique circumstances present when minors are questioned in school,” <em>post, </em>at 297, 180 L. Ed. 2d, at 339 (opinion of Alito, J.),  the effect of the schoolhouse setting cannot be disentangled from the identity of the person questioned. A student— whose presence at school is compulsory and whose disobedience at school is cause for disciplinary action—is in a far different position than, say, a parent volunteer on school grounds to chaperone an event, or an adult from the community on school grounds to attend a basketball game. Without asking whether the person “questioned in school” is a “minor,” <em>ibid., </em>the coercive effect of the schoolhouse setting is unknowable.</p>
<p id="b368-5">Our prior decision in <em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">Alvarado</a></span> </em>in no way undermines these conclusions. In that case, we held that a state-court decision that failed to mention a 17-year-old’s age as part of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>custody analysis was not objectively unreasonable under the deferential standard of review set forth by the Antiterrorism and Effective Death Penalty Act of 1996 (AEDPA), <span class="citation no-link">110 Stat. 1214</span>. Like the North Carolina Supreme Court here, see <span class="citation" data-id="6722655"><a href="/opinion/6835533/in-re-jdb/#672" aria-description="Citation for case: In re J.D.B.">363 N.C., at 672</a></span>, <span class="citation" data-id="6722655"><a href="/opinion/6835533/in-re-jdb/#140" aria-description="Citation for case: In re J.D.B.">686 S.E.2d, at 140</a></span>,  we observed that accounting for a juvenile’s age in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>custody analysis “could be viewed as creating a subjective inquiry,” <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#668" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 668</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span>. We said nothing, however, of whether such a view would be correct under the law. Cf. <em>Renico </em>v. <em>Lett, </em><span class="citation" data-id="6680078"><a href="/opinion/6795263/renico-v-lett/#778" aria-description="Citation for case: Renico v. Lett">559 U.S. 766, 778, n. 3</a></span>, <span class="citation" data-id="6680078"><a href="/opinion/6795263/renico-v-lett/" aria-description="Citation for case: Renico v. Lett">130 S. Ct. 1855</a></span>, <span class="citation" data-id="6680078"><a href="/opinion/6795263/renico-v-lett/" aria-description="Citation for case: Renico v. Lett">176 L. Ed. 2d 678</a></span> (2010) (“[W]hether</p>
<p id="b368-7">[<span class="citation no-link">564 U.S. 277</span>]</p>
<p id="b368-8">the [state court] was right or wrong is not the pertinent question under AEDPA”). To the contrary, Justice O’Connor’s concurring opinion explained that a suspect’s age may indeed “be relevant to the ‘custody’ inquiry.” <em>Alvarado, </em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#669" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 669</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span>.</p>
<p id="b368-9">Reviewing the question <em>de novo </em>today, we hold that  so long as the child’s age was known to the officer at the time of police questioning, or would have been objectively apparent to a reasonable officer, its inclusion in the custody analysis is consistent with the objective nature of that test.<footnotemark>8</footnotemark> This is not to say that a child’s age will be a determinative, or even a significant, factor in every case. Cf. <em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">ibid.</a></span> </em>(O’Connor, J., concurring) (explaining that a state-court decision omitting any mention of the defendant’s age was not unreasonable under AEDPA’s deferential standard of review where the defendant “was almost 18 years old at the time of his <page-number citation-index="1" label="327">*327</page-number>interview”); <em>post, </em>at 296, 180 L. Ed. 2d, at 339 (suggesting that “teenagers nearing the age of majority” are likely to react to an interrogation as would a “typical 18-year-old in similar circumstances”). It is, however, a reality that courts cannot simply ignore.</p>
<p id="b369-4">III</p>
<p id="b369-5">The State and its <em>amici </em>offer numerous reasons that courts must blind themselves to a juvenile defendant’s age. None is persuasive.</p>
<p id="b369-6">[<span class="citation no-link">564 U.S. 278</span>]</p>
<p id="b369-7">To start, the State contends that a child’s age must be excluded from the custody inquiry because age is a personal characteristic specific to the suspect himself rather than an “external” circumstance of the interrogation. Brief for Respondent 21; see also <em>id., </em>at 18-19 (distinguishing “personal characteristics” from “objective facts related to the interrogation itself’ such as the location and duration of the interrogation). Despite the supposed significance of this distinction, however, at oral argument counsel for the State suggested without hesitation that  at least some undeniably personal characteristics—for instance, whether the individual being questioned is blind—are circumstances relevant to the custody analysis. See Tr. of Oral Arg. 41. Thus, the State’s quarrel cannot be that age is a personal characteristic, without more.<footnotemark>9</footnotemark></p>
<p id="b369-8">The State further argues that age is irrelevant to the custody analysis because it “go[es] to how a suspect may internalize and perceive the circumstances of an interrogation.” Brief for Respondent 12; see also Brief for United States as <em>Amicus Curiae </em>21 (hereinafter U. S. Brief) (arguing that a child’s age has no place in the custody analysis because it goes to whether a suspect is “particularly susceptible” to the external circumstances of the interrogation (some internal quotation marks omitted)). But the same can be said of every objective circumstance that the State agrees is relevant to the custody analysis: Each circumstance goes to how a reasonable person would “internalize and perceive” every other. See, <em>e.g., Stansbury, </em><span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#325" aria-description="Citation for case: Stansbury v. California">511 U.S., at 325</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">114 S. Ct. 1526</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">128 L. Ed. 2d 293</a></span>. Indeed, this is the very reason that we ask whether the objective circumstances “add up to custody,” <em>Keohane, </em><span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/#113" aria-description="Citation for case: Thompson v. Keohane">516 U.S., at 113</a></span>, <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/" aria-description="Citation for case: Thompson v. Keohane">116 S. Ct. 457</a></span>, <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/" aria-description="Citation for case: Thompson v. Keohane">133 L. Ed. 2d 383</a></span>, instead of evaluating the circumstances one by one.</p>
<p id="b369-10">[<span class="citation no-link">564 U.S. 279</span>]</p>
<p id="b369-11">In the same vein, the State and its <em>amici </em>protest that the “effect of... age on [the] perception of custody is internal,” Brief for Respondent 20, or “psychological,” U. S. Brief 21.  But the whole point of the custody analysis is to determine whether, given the circumstances, “a reasonable person [would] have felt he or she was ... at liberty to terminate the interrogation and leave.” <em>Keohane, </em><span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/#112" aria-description="Citation for case: Thompson v. Keohane">516 U.S., at 112</a></span>, <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/" aria-description="Citation for case: Thompson v. Keohane">116 S. Ct. 457</a></span>, <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/" aria-description="Citation for case: Thompson v. Keohane">133 L. Ed. 2d 383</a></span>. Because the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>custody inquiry turns on the mindset of a reasonable person in the suspect’s position, it cannot be the case that a circumstance is subjective simply because it has an “internal” or “psychological” impact on perception. Were that so, <page-number citation-index="1" label="328">*328</page-number>there would be no objective circumstances to consider at all.</p>
<p id="b370-4">Relying on our statements that the objective custody test is “designed to give clear guidance to the police,” <em>Alvarado, </em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#668" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 668</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span>, the State next argues that a child’s age must be excluded from the analysis in order to preserve clarity. Similarly, the dissent insists that the clarity of the custody analysis will be destroyed unless a “one-size-fits-all reasonable-person test” applies. <em>Post, </em>at 293, 180 L. Ed. 2d, at 337. In reality, however, ignoring a juvenile defendant’s age will often make the inquiry more artificial, see <em>supra, </em>at 275-276, 180 L. Ed. 2d, at 325-326, and thus only add confusion. And in any event, a child’s age, when known or apparent, is hardly an obscure factor to assess. Though the State and the dissent worry about gradations among children of different ages, that concern cannot justify ignoring a child’s age altogether. Just as police officers are competent to account for other objective circumstances that are a matter of degree such as the length of questioning or the number of officers present, so too are they competent to evaluate the effect of relative age. Indeed, they are competent to do so even though an interrogation room lacks the “reflective atmosphere of a [jury] deliberation room,” <em>post, </em>at 295, 180 L. Ed. 2d, at 338. The same is true of judges, including those whose childhoods have long since passed, see <em>post, </em>at 293, 180 L. Ed. 2d, at 337. In short, officers and judges need no imaginative powers, knowledge of developmental psychology, training in cognitive science, or expertise</p>
<p id="atz-dedup-0">[<span class="citation no-link">564 U.S. 280</span>]</p>
<p id="b370-6">in social and cultural anthropology to account for a child’s age. They simply need the common sense to know that a 7-year-old is not a 13-year-old and neither is an adult.</p>
<p id="b370-8">There is, however, an even more fundamental flaw with the State’s plea for clarity and the dissent’s singular focus on simplifying the analysis:  Not once have we excluded from the custody analysis a circumstance that we determined was relevant and objective, simply to make the fault line between custodial and noncustodial “brighter.” Indeed, were the guiding concern clarity and nothing else, the custody test would presumably ask only whether the suspect had been placed under formal arrest. <em>Berkemer, </em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#441" aria-description="Citation for case: Berkemer v. McCarty">468 U.S., at 441</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">104 S. Ct. 3138</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">82 L. Ed. 2d 317</a></span>; see <em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">ibid.</a></span> </em>(acknowledging the “occasional!] . . . difficulty” police officers confront in determining when a suspect has been taken into custody). But we have rejected that “more easily administered line,” recognizing that it would simply “enable the police to circumvent the constraints on custodial interrogations established by Miranda.” <em>Ibid.; </em>see also <em>ibid., </em>n. 33.<footnotemark>10</footnotemark></p>
<p id="b370-9">Finally, the State and the dissent suggest that excluding age from the custody analysis comes at no cost to <page-number citation-index="1" label="329">*329</page-number>juveniles’ constitutional rights because the due process voluntariness test independently accounts for a child’s youth. To be sure,  that test permits consideration of a child’s age, and it erects its own barrier to admission of a defendant’s inculpatory statements at trial. See <em>Gallegos, </em><span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/#53" aria-description="Citation for case: Gallegos v. Colorado">370 U.S., at 53-55</a></span>, <span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/" aria-description="Citation for case: Gallegos v. Colorado">82 S. Ct. 1209</a></span>, <span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/" aria-description="Citation for case: Gallegos v. Colorado">8 L. Ed. 2d 325</a></span>; <em>Haley, </em><span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/#599" aria-description="Citation for case: Haley v. Ohio">332 U.S., at 599-601</a></span>, <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/" aria-description="Citation for case: Haley v. Ohio">68 S. Ct. 302</a></span>, <span class="citation no-link">92 L. Ed. 224</span> (plurality opinion); see also <em>post,</em></p>
<p id="b371-4">[<span class="citation no-link">564 U.S. 281</span>]</p>
<p id="b371-5">at 297, 180 L. Ed. 2d, at 340 (“[C]ourts should be instructed to take particular care to ensure that [young children’s] incriminating statements were not obtained involuntarily”). But <em>Miranda’s </em>procedural safeguards exist precisely because the voluntariness test is an inadequate barrier when custodial interrogation is at stake. See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#458" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 458</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span> (“Unless adequate protective devices are employed to dispel the compulsion inherent in custodial surroundings, no statement obtained from the defendant can truly be the product of his free choice”); <em>Dickerson, </em><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#442" aria-description="Citation for case: Dickerson v. United States">530 U.S., at 442</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">120 S. Ct. 2326</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">147 L. Ed. 2d 405</a></span> (“[R]eliance on the traditional totality-of-the-circumstances test raise [s] a risk of overlooking an involuntary custodial confession”); see also <em>supra, </em>at 268-270, 180 L. Ed. 2d, at 321-322. To hold, as the State requests, that a child’s age is never relevant to whether a suspect has been taken into custody—and thus to ignore the very real differences between children and adults—would be to deny children the full scope of the procedural safeguards that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>guarantees to adults.</p>
<p id="pA12W">
<img class="p" height="64" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAVIAAABAAQAAAABgx8JmAAAAqklEQVR4nO2TPQrCQBCFd0Ow1TKl5gTiDTyVbY6QG2muIxbpXCT6LDLrTOGDNIsIM0349n2zP5CJCEtrqBarIZR2k10kkN2bjQkUvu+j7nWNgbj3jemnAABAOq3xKQIX2Xd13ms7BWkaYOo75H1Dax9MILsHGxMQ97nbaspA3Ok4asygnj+pazRmEOe5eF2Tnksgz0U1mSsyKPWfxT+dY3fdddddd939hfsGZXGCQnMUtgoAAAAASUVORK5CYII=" width="337"/>
</p>
<p id="b371-12">The question remains whether J. D. B. was in custody when police interrogated him. We remand for the state courts to address that question, this time taking account of all of the relevant circumstances of the interrogation, including J. D. B.’s age at the time. The judgment of the North Carolina Supreme Court is reversed, and the case is remanded for proceedings not inconsistent with this opinion.</p>
<p id="b371-13">It is so ordered.</p>
<p id="b371-6">SEPARATE OPINION</p>
<footnote label="1">
<p id="b361-14">. Although the State suggests that the “record is unclear as to who brought J. D. B. to the conference room, and the trial court made no factual findings on this specific point,’’ Brief for Respondent 3, n. 1, the State agreed at the certiorari stage that “the SRO [school resource officer] escorted petitioner’’ to the room, Brief in Opposition 3.</p>
</footnote>
<footnote label="2">
<p id="b362-13">. The North Carolina Supreme Court noted that the trial court’s factual findings were “uncontested and therefore . . . binding’’ on it. <em>In re J. D. B., </em><span class="citation" data-id="6722655"><a href="/opinion/6835533/in-re-jdb/#668" aria-description="Citation for case: In re J.D.B.">363 N.C. 664, 668</a></span>, <span class="citation" data-id="6722655"><a href="/opinion/6835533/in-re-jdb/#137" aria-description="Citation for case: In re J.D.B.">686 S.E.2d 135, 137</a></span> (2009). The court described the sequence of events set forth in the text. See <span class="citation" data-id="6722655"><a href="/opinion/6835533/in-re-jdb/#670" aria-description="Citation for case: In re J.D.B."><em>id., </em>at 670-671</a></span>, <span class="citation" data-id="6722655"><a href="/opinion/6835533/in-re-jdb/#139" aria-description="Citation for case: In re J.D.B.">686 S.E.2d, at 139</a></span> (“Immediately following J. D. B.’s initial confession, Investigator DiCostanzo informed J. D. B. that he did not have to speak with him and that he was free to leave’’ (internal quotation marks and alterations omitted)). Though less than perfectly explicit, the trial court’s order indicates a finding that J. D. B. initially confessed prior to DiCostanzo’s warnings. See App. 99a.</p>
<p id="Aq_o">Nonetheless, both parties’ submissions to this Court suggest that the warnings came after DiCostanzo raised the possibility of a secure custody order but before J. D. B. confessed for the first time. See Brief for Petitioner 5; Brief for Respondent 5. Because we remand for a determination whether J. D. B. was in custody under the proper analysis, the state courts remain free to revisit whether the trial court made a conclusive finding of fact in this respect.</p>
</footnote>
<footnote label="3">
<p id="b363-13">. J. D. B.’s challenge in the North Carolina Supreme Court focused on the lower courts’ conclusion that he was not in custody for purposes of <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U.S. 436</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span> (1966). The North Carolina Supreme Court did not address the trial court’s holding that the statements were voluntary, and that question is not before us.</p>
</footnote>
<footnote label="4">
<p id="b364-12">. <em>Amici </em>on behalf of J. D. B. question whether children of all ages can comprehend <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and suggest that additional procedural safeguards may be necessary to protect their <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. Brief for Juvenile Law Center et al. 13-14, n. 7. Whatever the merit of that contention, it has no relevance here, where no <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings were administered at all.</p>
</footnote>
<footnote label="5">
<p id="b366-11">. Although citation to social science and cognitive science authorities is unnecessary to establish these commonsense propositions, the literature confirms what experience bears out. See, <em>e.g., Graham </em>v. <em>Florida, </em><span class="citation" data-id="6680682"><a href="/opinion/6795859/graham-v-florida/#68" aria-description="Citation for case: Graham v. Florida">560 U.S. 48, 68</a></span>, <span class="citation" data-id="6680682"><a href="/opinion/6795859/graham-v-florida/" aria-description="Citation for case: Graham v. Florida">130 S. Ct. 2011</a></span>, <span class="citation" data-id="6680682"><a href="/opinion/6795859/graham-v-florida/" aria-description="Citation for case: Graham v. Florida">176 L. Ed. 2d 825</a></span> (2010) (“[D]evelopments in psychology and brain science continue to show fundamental differences between juvenile and adult minds”).</p>
</footnote>
<footnote label="6">
<p id="b366-12">. See, <em>e.g., </em>1 E. Farnsworth, Contracts § 4.4, p. 379, and n. 1 (1990) (“Common law courts early announced the prevailing view that a minor’s contract is ‘voidable’ at the instance of the minor” (citing 8 W. Holdsworth, History of English Law 51 (1926))); 1 D. Kramer, Legal Rights of Children § 8.1, p. 663 (rev. 2d ed. 2005) (“[W]hile minor children have the right to acquire and own property, they are considered incapable of property management” (footnote omitted)); 2 J. Kent, Commentaries on American Law *78-*79, *90 (G. Comstock ed., 11th ed. 1867); see generally <em>id., </em>at *233 (explaining that, under the common law, “[t]he necessity of guardians results from the inability of infants to take care of themselves . . . and this inability continues, in contemplation of law, until the infant has attained the age of [21] ”); 1 Blackstone *465 (“It is generally true, that an infant can neither aliene his lands, nor do any legal act, nor make a deed, nor indeed any manner of contract, that will bind him”); <em>Roper </em>v. <em>Simmons, </em><span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/#569" aria-description="Citation for case: Roper v. Simmons">543 U.S. 551, 569</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">125 S. Ct. 1183</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">161 L. Ed. 2d 1</a></span> (2005) (“In recognition of the comparative immaturity and irresponsibility of juveniles, almost every State prohibits those under 18 years of age from voting, serving on juries, or marrying without parental consent”).</p>
</footnote>
<footnote label="7">
<p id="b367-10">. Thus, contrary issent’s protestations, today’s holding neither invites consideration of whether a particular suspect is “unusually meek or <em>compliant," post, </em>at 289, 180 L. Ed. 2d, at 335 (opinion of Alito, J.), nor “ ‘expand[s]’ ’’ the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>custody analysis, <em>post, </em>at 289, 180 L. Ed. 2d, at 334, into a test that requires officers to anticipate and account for a suspect’s every personal characteristic, see <em>post, </em>at 291-292, 180 L. Ed. 2d, at 335-336.</p>
</footnote>
<footnote label="8">
<p id="b368-10">.  This approach does not undermine the basic principle that an interrogating officer’s unarticulated, internal thoughts are never—in and of themselves—objective circumstances of an interrogation. See <em>supra, </em>at 270-271, 180 L. Ed. 2d, at 322-323; <em>Stansbury </em>v. <em>California, </em><span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#323" aria-description="Citation for case: Stansbury v. California">511 U.S. 318, 323</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">114 S. Ct. 1526</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">128 L. Ed. 2d 293</a></span> (1994) <em>(per curiam). </em>Unlike a child’s youth, an officer’s purely internal thoughts have no conceivable effect on how a reasonable person in the suspect’s position would understand his freedom of action. See <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#323" aria-description="Citation for case: Stansbury v. California"><em>id., </em>at 323-325</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">114 S. Ct. 1526</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">128 L. Ed. 2d 293</a></span>; <em>Berkemer </em>v. <em>McCarty, </em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#442" aria-description="Citation for case: Berkemer v. McCarty">468 U.S. 420, 442</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">104 S. Ct. 3138</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">82 L. Ed. 2d 317</a></span> (1984). Rather than “overtur[n]” that settled principle, <em>post, </em>at 293, 180 L. Ed. 2d, at 337, the limitation that a child’s age may inform the custody analysis only when known or knowable simply reflects our unwillingness to require officers to “make guesses’’ as to circumstances “unknowable’’ to them in deciding when to give <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, <em>Berkemer, </em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#430" aria-description="Citation for case: Berkemer v. McCarty">468 U.S., at 430-431</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">104 S. Ct. 3138</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">82 L. Ed. 2d 317</a></span>.</p>
</footnote>
<footnote label="9">
<p id="b369-12">. The State’s purported distinction between blindness and age—that taking account of a suspect’s youth requires a court “to get into the mind’’ of the child, whereas taking account of a suspect’s blindness does not, Tr. of Oral Arg. 41-42—is mistaken. In either case, the question becomes how a reasonable person would understand the circumstances, either from the perspective of a blind person or, as here, a 13-year-old child.</p>
</footnote>
<footnote label="10">
<p id="b370-10">. Contrary issent’s intimation, see <em>post, </em>at 288, 180 L. Ed. 2d, at 334,  <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>does not answer the question whether a child’s age is an objective circumstance relevant to the custody analysis. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>simply holds that warnings must be given once a suspect is in custody, without “paus[ing] to inquire in individual cases whether the defendant was aware of his rights without a warning being given.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#468" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 468</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>; see also <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#468" aria-description="Citation for case: Miranda v. Arizona"><em>id., </em>at 468-469</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span> (“Assessments of the knowledge the defendant possessed, based on information as to age, education, intelligence, or prior contact with authorities, can never be more than speculation; a warning is a clearcut fact” (footnote omitted)). That conclusion says nothing about whether age properly informs whether a child is in custody in the first place.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Jacobson v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Jacobson v. United States"
type: case
citation: "503 U.S. 540 (1992)"
parallel_cite: "112 S. Ct. 1535; 118 L. Ed. 2d 174"
neutral_cite: 1992 U.S. LEXIS 2117
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1992
date_decided: 1992-04-06
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1992-04-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Jacobson v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112720/jacobson-v-united-states/"
  cluster_id: 112720
  opinion_id: 9432514
  identity_checked: true
homes:
  - page: "[[Entrapment]]"
    role: "Key — Progeny / Refinement"
related: ["[[Sorrells v. United States]]", "[[Sherman v. United States]]", "[[Hampton v. United States]]", "[[Mathews v. United States]]"]
aliases: []
tags: ["case", "entrapment", "predisposition", "inducement", "due-process"]
holding: "Where the government induces the crime, it must prove the defendant was predisposed to commit it INDEPENDENT of, and PRIOR TO, the…"
lake:
  record_id: Jacobson v. United States
  status: verified
  projected_at: 2026-07-06
---

# Jacobson v. United States

*503 U.S. 540 (1992)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Jacobson lawfully ordered magazines containing images of nude boys before such material became illegal. After the law changed, two government agencies, through a series of fictitious organizations and a pen pal, spent about two and a half years sending him mailings probing and stoking his attitudes about child erotica and decrying censorship. Eventually he ordered a magazine depicting child pornography and was arrested. He raised the entrapment defense.

## Issue
Whether the government proved that Jacobson was predisposed to commit the crime independent of, and prior to, the government's lengthy inducement, as required to defeat an entrapment defense.

## Rule
Where the government induces the crime, it must prove predisposition that predates its own conduct. "Government agents may not originate a criminal design, implant in an innocent person's mind the disposition to commit a criminal act, and then induce commission of the crime so that the Government may prosecute." — 503 U.S. at 548. ^pin-548

"Where the Government has induced an individual to break the law and the defense of entrapment is at issue, as it was in this case, the prosecution must prove beyond reasonable doubt that the defendant was disposed to commit the criminal act prior to first being approached by Government agents." — *Id.* at 548–549. ^pin-548a

## Application
The only evidence of Jacobson's predisposition arose after the government's two-and-a-half-year campaign of mailings; his earlier, then-legal purchases did not show he was disposed to order illegal child pornography before the government approached him. Because the prosecution failed to prove predisposition independent of, and prior to, that sustained inducement, the government had implanted the disposition it then prosecuted, and the entrapment defense was established as a matter of law.

## Conclusion
The government failed to prove predisposition predating its inducement; the conviction was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Jacobson* refines the subjective entrapment test of [[Sorrells v. United States]] and [[Sherman v. United States]] by requiring that predisposition exist before the government's first approach.

## Appears on
- [[Entrapment]] — *Key — Progeny / Refinement*

## Sources
- *Jacobson v. United States*, 503 U.S. 540 (1992) — https://www.courtlistener.com/opinion/112720/jacobson-v-united-states/ — pinpoints: 548, 549.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8cccdaf9b84351ff", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Jacobson v. United States"}, "payload": {"all": [{"cite": "503 U.S. 540", "page": "540", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "503"}, {"cite": "112 S. Ct. 1535", "page": "1535", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "112"}, {"cite": "118 L. Ed. 2d 174", "page": "174", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "118"}, {"cite": "1992 U.S. LEXIS 2117", "page": "2117", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1992"}], "display": "503 U.S. 540", "official": {"cite": "503 U.S. 540", "page": "540", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "503"}, "official_selection_present": true, "record_id": "Jacobson v. United States"}}
{"assertion_id": "00b7c34b3f358b75", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-548a", "record_id": "Jacobson v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-548a", "pinpoint_status": "slip-only", "quote": "Where the Government has induced an individual to break the law and the defense of entrapment is at issue, as it was in this case, the prosecution must prove beyond reasonable doubt that the defendant was disposed to commit the criminal act prior to first being approached by Government agents.", "quote_fidelity": "mismatch", "record_id": "Jacobson v. United States", "star_marker": null}}
{"assertion_id": "8aab813053ba6274", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-548", "record_id": "Jacobson v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-548", "pinpoint_status": "slip-only", "quote": "--- # Jacobson v. United States *503 U.S. 540 (1992)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Jacobson lawfully ordered magazines containing images of nude boys before such material became illegal. After the law changed, two government agencies, through a series of fictitious organizations and a pen pal, spent about two and a half years sending him mailings probing and stoking his attitudes about child erotica and decrying censorship. Eventually he ordered a magazine depicting child pornography and was arrested. He raised the entrapment defense. ## Issue Whether the government proved that Jacobson was predisposed to commit the crime independent of, and prior to, the government's lengthy inducement, as required to defeat an entrapment defense. ## Rule Where the government induces the crime, it must prove predisposition that predates its own conduct.", "quote_fidelity": "mismatch", "record_id": "Jacobson v. United States", "star_marker": null}}
{"assertion_id": "451ab310ab8d8656", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Jacobson v. United States"}, "payload": {"as_of_content": "1992-04-06", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Jacobson v. United States", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Jacobson v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Jacobson v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Jacobson v. United States",
    "case_name_short": "Jacobson",
    "case_name_full": "Jacobson v. United States",
    "input_case_name": "Jacobson v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1992-04-06",
    "year": 1992,
    "docket": null,
    "cluster_id": 112720,
    "lead_opinion_id": 9432514,
    "sibling_ids": [
      112720,
      9432514,
      9432515
    ],
    "absolute_url": "/opinion/112720/jacobson-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "503 U.S. 540",
      "volume": "503",
      "reporter": "U.S.",
      "page": "540",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "112 S. Ct. 1535",
        "volume": "112",
        "reporter": "S. Ct.",
        "page": "1535",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "118 L. Ed. 2d 174",
        "volume": "118",
        "reporter": "L. Ed. 2d",
        "page": "174",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1992 U.S. LEXIS 2117",
        "volume": "1992",
        "reporter": "U.S. LEXIS",
        "page": "2117",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "503 U.S. 540",
        "volume": "503",
        "reporter": "U.S.",
        "page": "540",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "112 S. Ct. 1535",
        "volume": "112",
        "reporter": "S. Ct.",
        "page": "1535",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "118 L. Ed. 2d 174",
        "volume": "118",
        "reporter": "L. Ed. 2d",
        "page": "174",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1992 U.S. LEXIS 2117",
        "volume": "1992",
        "reporter": "U.S. LEXIS",
        "page": "2117",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "503 U.S. 540",
    "official_selection": {
      "court_class": "scotus",
      "selected": "503 U.S. 540",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-548",
      "page": null,
      "quote": "--- # Jacobson v. United States *503 U.S. 540 (1992)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Jacobson lawfully ordered magazines containing images of nude boys before such material became illegal. After the law changed, two government agencies, through a series of fictitious organizations and a pen pal, spent about two and a half years sending him mailings probing and stoking his attitudes about child erotica and decrying censorship. Eventually he ordered a magazine depicting child pornography and was arrested. He raised the entrapment defense. ## Issue Whether the government proved that Jacobson was predisposed to commit the crime independent of, and prior to, the government's lengthy inducement, as required to defeat an entrapment defense. ## Rule Where the government induces the crime, it must prove predisposition that predates its own conduct.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-548a",
      "page": null,
      "quote": "Where the Government has induced an individual to break the law and the defense of entrapment is at issue, as it was in this case, the prosecution must prove beyond reasonable doubt that the defendant was disposed to commit the criminal act prior to first being approached by Government agents.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1992-04-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Jacobson v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Von Harris",
          "cluster_id": 10324088,
          "cite": [
            "2025 Ohio 279"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. James Barta",
          "cluster_id": 2774293,
          "cite": [
            "776 F.3d 931",
            "2015 WL 350672",
            "2015 U.S. App. LEXIS 1382"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Delgado-Marrero",
          "cluster_id": 2652872,
          "cite": [
            "744 F.3d 167",
            "2014 WL 522462"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Delaine and Malisa Fitzpat",
          "cluster_id": 889950,
          "cite": [
            "2012 MT 300",
            "367 Mont. 385",
            "291 P.3d 1106",
            "2012 Mont. LEXIS 368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin Eric Curtin",
          "cluster_id": 798060,
          "cite": [
            "489 F.3d 935",
            "73 Fed. R. Serv. 646",
            "2007 U.S. App. LEXIS 12110",
            "2007 WL 1500295"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Eduardo Sandoval-Mendoza",
          "cluster_id": 796368,
          "cite": [
            "472 F.3d 645",
            "2006 U.S. App. LEXIS 31815",
            "2006 WL 3783435"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cunningham",
          "cluster_id": 3952337,
          "cite": [
            "808 N.E.2d 488",
            "156 Ohio App. 3d 714",
            "2004 Ohio 1935"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gutierrez",
          "cluster_id": 32172,
          "cite": [
            "343 F.3d 415",
            "2003 U.S. App. LEXIS 16694",
            "2003 WL 21940783"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Reginald Dodd",
          "cluster_id": 770267,
          "cite": [
            "225 F.3d 340",
            "2000 U.S. App. LEXIS 21423"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Terry Lee Brooks",
          "cluster_id": 769099,
          "cite": [
            "215 F.3d 842",
            "2000 U.S. App. LEXIS 13688",
            "2000 WL 764784"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Free Speech Coalition v. Reno",
          "cluster_id": 7079655,
          "cite": [
            "198 F.3d 1083",
            "1999 WL 1206649"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hawkins v. Freeman",
          "cluster_id": 2966971,
          "cite": [
            "166 F.3d 267",
            "1999 WL 21325"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas",
          "cluster_id": 7058791,
          "cite": [
            "134 F.3d 975",
            "98 Daily Journal DAR 763",
            "98 Cal. Daily Op. Serv. 555",
            "48 Fed. R. Serv. 924",
            "1998 U.S. App. LEXIS 832",
            "1998 WL 19640"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vazquez v. State",
          "cluster_id": 1799192,
          "cite": [
            "700 So. 2d 5",
            "1997 WL 361832"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dwayne A. Washington",
          "cluster_id": 735397,
          "cite": [
            "106 F.3d 983",
            "323 U.S. App. D.C. 175",
            "46 Fed. R. Serv. 719",
            "1997 U.S. App. LEXIS 3057"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Sprouse",
          "cluster_id": 1119600,
          "cite": [
            "983 P.2d 771",
            "1999 Colo. J. C.A.R. 3329",
            "1999 Colo. LEXIS 553",
            "1999 WL 391087"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dixon v. United States",
          "cluster_id": 145638,
          "cite": [
            "165 L. Ed. 2d 299",
            "126 S. Ct. 2437",
            "548 U.S. 1",
            "2006 U.S. LEXIS 4894"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William D. Davis, United States of America v. Curry James Williams",
          "cluster_id": 679513,
          "cite": [
            "36 F.3d 1424",
            "94 Daily Journal DAR 13648",
            "1994 U.S. App. LEXIS 27168",
            "1994 WL 525969"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony N. Matteo v. Superintendent, Sci Albion the District Attorney of the County of Chester the Attorney General of the State of Pennsylvania",
          "cluster_id": 762628,
          "cite": [
            "171 F.3d 877",
            "1999 U.S. App. LEXIS 5163",
            "1999 WL 164152"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gendron",
          "cluster_id": 195225,
          "cite": [
            "18 F.3d 955",
            "1994 WL 50975"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brand",
          "cluster_id": 8439509,
          "cite": [
            "467 F.3d 179",
            "71 Fed. R. Serv. 672",
            "2006 U.S. App. LEXIS 25887",
            "2006 WL 2981524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hilario Mendoza-Salgado, United States of America v. Ramon Edwardo Garcia",
          "cluster_id": 583725,
          "cite": [
            "964 F.2d 993",
            "35 Fed. R. Serv. 1029",
            "1992 U.S. App. LEXIS 10413",
            "1992 WL 101352"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gifford",
          "cluster_id": 195222,
          "cite": [
            "17 F.3d 462",
            "1994 WL 46738"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Carter",
          "cluster_id": 1795509,
          "cite": [
            "974 So. 2d 181",
            "2008 WL 80764"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ram Singh",
          "cluster_id": 696216,
          "cite": [
            "54 F.3d 1182",
            "1995 U.S. App. LEXIS 13496",
            "1995 WL 325249"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, Plaintiff-Appellee-Cross-Appellant v. Joe Garza-Juarez and Esteban Garza-Juarez, Defendants-Appellants-Cross-Appellees",
          "cluster_id": 606075,
          "cite": [
            "992 F.2d 896",
            "93 Daily Journal DAR 5160",
            "93 Cal. Daily Op. Serv. 2972",
            "1993 U.S. App. LEXIS 8960"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Al Kassar",
          "cluster_id": 613957,
          "cite": [
            "660 F.3d 108",
            "2011 U.S. App. LEXIS 19357",
            "2011 WL 4375654"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wise",
          "cluster_id": 21510,
          "cite": [
            "221 F.3d 140",
            "2000 U.S. App. LEXIS 18282",
            "2000 WL 1041236"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Squillacote",
          "cluster_id": 2967273,
          "cite": [
            "221 F.3d 542",
            "2000 WL 1139526"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Jacquez Lamarr, United States of America v. Guy A. Dillard, United States of America v. Maurice L. Mallory, A/K/A Darrell Lee Lawson",
          "cluster_id": 712191,
          "cite": [
            "75 F.3d 964",
            "43 Fed. R. Serv. 1014",
            "1996 U.S. App. LEXIS 2316"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brace",
          "cluster_id": 15106,
          "cite": [
            "145 F.3d 247",
            "1998 WL 333453"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jimenez Recio",
          "cluster_id": 122255,
          "cite": [
            "154 L. Ed. 2d 744",
            "123 S. Ct. 819",
            "537 U.S. 270",
            "2003 U.S. LEXIS 901"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stephanie Cannon, Also Known as Stephanie Lynch, United States of America v. Keith Anthony Cannon, United States of America v. Stephanie Cannon, Also Known as Stephanie Lynch, United States of America v. Keith Anthony Cannon",
          "cluster_id": 721470,
          "cite": [
            "88 F.3d 1495"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Davis",
          "cluster_id": 662451,
          "cite": [
            "15 F.3d 1393",
            "1994 WL 32296"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Charles Jones",
          "cluster_id": 770998,
          "cite": [
            "231 F.3d 508",
            "2000 Cal. Daily Op. Serv. 8848",
            "2000 Daily Journal DAR 11717",
            "2000 U.S. App. LEXIS 27330"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Munoz v. State",
          "cluster_id": 1676101,
          "cite": [
            "629 So. 2d 90",
            "1993 WL 406367"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lively",
          "cluster_id": 1119419,
          "cite": [
            "921 P.2d 1035"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112720 OR 9432514 OR 9432515) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04MjYyNDMyMDAwMDAmcz03MTQ4MzQmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112720+OR+9432514+OR+9432515%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 15,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 16,
        "triage_snippet_classified": 184
      },
      "lane2_top_cited": {
        "query": "cites:(112720 OR 9432514 OR 9432515)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04NiZzPTE1MDk1NSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112720+OR+9432514+OR+9432515%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112720 OR 9432514 OR 9432515)",
        "reviewed": 11,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 11,
        "triage_read": 1,
        "triage_snippet_classified": 10
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112720 OR 9432514 OR 9432515)",
    "indexed_citing_opinions": 428,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112720,
        "count": 369,
        "count_source": "search"
      },
      {
        "opinion_id": 9432514,
        "count": 60,
        "count_source": "search"
      },
      {
        "opinion_id": 9432515,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 691,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/jacobson-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcwMTMzOTEmcz00ODA2NDMxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112720+OR+9432514+OR+9432515%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112720,
        "cited_id": 101997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 105681,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 107685,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 107898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 108768,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 108839,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 109939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 110794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 112012,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 112417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 230738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 342581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 416501,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 417704,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 445246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 527667,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 549820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 556376,
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
    "date_created": "2026-07-05T08:46:20Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:46:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:46:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:52:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:46:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Jacobson v. United States

```
<opinion type="majority">
<author id="ArMK"><page-number citation-index="1" label="542">*542</page-number>Justice White</author>
<p id="Anh">delivered the opinion of the Court.</p>
<p id="AzeW">On September 24, 1987, petitioner Keith Jacobson was indicted for violating a provision of the Child Protection Act of 1984 (Act), <span class="citation no-link">Pub. L. 98-292, 98</span> Stat. 204, which criminalizes the knowing receipt through the mails of a “visual depiction [that] involves the use of a minor engaging in sexually explicit conduct. . . .” <span class="citation no-link">18 U. S. C. § 2252</span>(a)(2)(A). Petitioner defended on the ground that the Government entrapped him into committing the crime through a series of communications from undercover agents that spanned the 26 months preceding his arrest. Petitioner was found guilty after a jury trial. The Court of Appeals affirmed his conviction, holding that the Government had carried its burden of proving beyond reasonable doubt that petitioner was predisposed to break the law and hence was not entrapped.</p>
<p id="Ayo">Because the Government overstepped the line between setting a trap for the “unwary innocent” and the “unwary criminal,” <em>Sherman </em>v. <em>United States, </em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#372" aria-description="Citation for case: Sherman v. United States">356 U. S. 369, 372</a></span> (1958), and as a matter of law failed to establish that petitioner was independently predisposed to commit the crime for which he was arrested, we reverse the Court of Appeals’ judgment affirming his conviction.</p>
<p id="AqC">I</p>
<p id="A7S5">In February 1984, petitioner, a 56-year-old veteran-turned-farmer who supported his elderly father in Nebraska, ordered two magazines and a brochure from a California adult bookstore. The magazines, entitled Bare Boys I and Bare Boys II, contained photographs of nude preteen and <page-number citation-index="1" label="543">*543</page-number>teenage boys. The contents of the magazines startled petitioner, who testified that he had expected to receive photographs of “young men 18 years or older.” Tr. 425. On cross-examination, he explained his response to the magazines:</p>
<blockquote id="b599-4">“[PROSECUTOR]: [Y]ou were shocked and surprised that there were pictures of very young boys without clothes on, is that correct?</blockquote>
<blockquote id="b599-5">“[JACOBSON]: Yes, I was.</blockquote>
<blockquote id="b599-6">“[PROSECUTOR]: Were you offended?</blockquote>
<blockquote id="b599-7">“[JACOBSON]: I was not offended because I thought these were a nudist type publication. Many of the pictures were out in a rural or outdoor setting. There was — I didn’t draw any sexual connotation or connection with that.” <span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#463" aria-description="Citation for case: Sherman v. United States"><em>Id., </em>at 463</a></span>.</blockquote>
<p id="b599-8">The young men depicted in the magazines were not engaged in sexual activity, and petitioner’s receipt of the magazines was legal under both federal and Nebraska law. Within three months, the law with respect to child pornography changed; Congress passed the Act illegalizing the receipt through the mails of sexually explicit depictions of children. In the very month that the new provision became law, postal inspectors found petitioner’s name on the mailing list of the California bookstore that had mailed him Bare Boys I and II. There followed over the next 2V2 years repeated efforts by two Government agencies, through five fictitious organizations and a bogus pen pal, to explore petitioner’s willingness to break the new law by ordering sexually explicit photographs of children through the mail.</p>
<p id="b599-9">The Government began its efforts in January 1985 when a postal inspector sent petitioner a letter supposedly from the American Hedonist Society, which in fact was a fictitious organization. The letter included a membership application and stated the Society’s doctrine: that members had the <page-number citation-index="1" label="544">*544</page-number>“right to read what we desire, the right to discuss similar interests with those who share our philosophy, and finally that we have the right to seek pleasure without restrictions being placed on us by outdated puritan morality.” Record, Government Exhibit 7. Petitioner enrolled in the organization and returned a sexual attitude questionnaire that asked him to rank on a scale of one to four his enjoyment of various sexual materials, with one being “really enjoy,” two being “enjoy,” three being “somewhat enjoy,” and four being “do not enjoy.” Petitioner ranked the entry “[p]re-teen sex” as a two, but indicated that he was opposed to pedophilia. <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Ibid.</a></span></em></p>
<p id="b600-5">For a time, the Government left petitioner alone. But then a new “prohibited mailing specialist” in the Postal Service found petitioner’s name in a file, Tr. 328-331, and in May 1986, petitioner received a solicitation from a second fictitious consumer research company, “Midlands ■ Data Research,” seeking a response from those who “believe in the joys of sex and the complete awareness of those lusty and youthful lads and lasses of the neophite <em>[sic] </em>age.” Record, Government Exhibit 8. The letter never explained whether “neophite” referred to minors or young adults. Petitioner responded: “Please feel free to send me more information, I am interested in teenage sexuality. Please keep my name confidential.” <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Ibid.</a></span></em></p>
<p id="b600-6">Petitioner then heard from yet another Government creation, “Heartland Institute for a New Tomorrow” (HINT), which proclaimed that it was “an organization founded to protect and promote sexual freedom and freedom of choice. We believe that arbitrarily imposed legislative sanctions restricting <em>your </em>sexual freedom should be rescinded through the legislative process.” <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Id.,</a></span> </em>Defendant’s Exhibit 102. The letter also enclosed a second survey. Petitioner indicated that his interest in “[pjreteen sex-homosexual” material was above average, but not high. In response to another question, petitioner wrote: “Not only sexual expression but freedom of the press is under attack. We must be ever vigilant <page-number citation-index="1" label="545">*545</page-number>to counter attack right wing fundamentalists who are determined to curtail our freedoms.” <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Id.,</a></span> </em>Government Exhibit 9.</p>
<p id="b601-5">HINT replied, portraying itself as a lobbying organization seeking to repeal “all statutes which regulate sexual activities, except those laws which deal with violent behavior, such as rape. HINT is also lobbying to eliminate any legal definition of ‘the age of consent.’ ” <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Id.,</a></span> </em>Defendant’s Exhibit 113. These lobbying efforts were to be funded by sales from a catalog to be published in the future “offering the sale of various items which we believe you will find to be both interesting and stimulating.” <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Ibid.</a></span> </em>HINT also provided computer matching of group members with similar survey responses; and, although petitioner was supplied with a list of potential “pen pals,” he did not initiate any correspondence.</p>
<p id="b601-6">Nevertheless, the Government’s “prohibited mailing specialist” began writing to petitioner, using the pseudonym “Carl Long.” The letters employed a tactic known as “mirroring,” which the inspector described as “reflect[ing] whatever the interests are of the person we are writing to.” Tr. 342. Petitioner responded at first, indicating that his interest was primarily in “male-male items.” Record, Government Exhibit 9A. Inspector “Long” wrote back:</p>
<blockquote id="b601-7">“My interests too are primarily male-male items. Are you satisfied with the type of VCR tapes available? Personally, I like the amateur stuff better if its <em>[sic] </em>well produced as it can get more kinky and also seems more real. I think the actors enjoy it more.” <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Id.,</a></span> </em>Government Exhibit 13.</blockquote>
<p id="b601-8">Petitioner responded:</p>
<blockquote id="b601-9">“As far as my likes are concerned, I like good looking young guys (in their late teens and early 20’s) doing their thing together.” <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Id.,</a></span> </em>Government Exhibit 14.</blockquote>
<p id="b601-10">Petitioner’s letters to “Long” made no reference to child pornography. After writing two letters, petitioner discontinued the correspondence.</p>
<p id="b602-4"><page-number citation-index="1" label="546">*546</page-number>By March 1987, 34 months had passed since the Government obtained petitioner’s name from the mailing list of the California bookstore, and 26 months had passed since the Postal Service had commenced its mailings to petitioner. Although petitioner had responded to surveys and letters, the Government had no evidence that petitioner had ever intentionally possessed or been exposed to child pornography. The Postal Service had not checked petitioner’s mail to determine whether he was receiving questionable mailings from persons — other than the Government — involved in the child pornography industry. Tr. 348.</p>
<p id="b602-5">At this point, a second Government agency, the Customs Service, included petitioner in its own child pornography sting, “Operation Borderline,” after receiving his name on lists submitted by the Postal Service. <em>Id., </em>at 71-72. Using the name of a fictitious Canadian company called “Produit Outaouais,” the Customs Service mailed petitioner a brochure advertising photographs of young boys engaging in sex. Record, Government Exhibit 22. Petitioner placed an order that was never filled. <em>Id., </em>Government Exhibit 24.</p>
<p id="b602-6">The Postal Service also continued its efforts in the Jacobson case, writing to petitioner as the “Far Eastern Trading Company Ltd.” The letter began:</p>
<blockquote id="b602-7">“As many of you know, much hysterical nonsense has appeared in the American media concerning ‘pornography’ and what must be done to stop it from coming across your borders. This brief letter does not allow us to give much comments; however, why is your government spending millions of dollars to exercise international censorship while tons of drugs, which makes yours the world’s most crime ridden country are passed through easily.” <em>Id., </em>Government Exhibit 1.</blockquote>
<p id="b602-8">The letter went on to say:</p>
<blockquote id="b602-9">“[W]e have devised a method of getting these to you without prying eyes of U. S. Customs seizing your <page-number citation-index="1" label="547">*547</page-number>mail. . . . After consultations with American solicitors, we have been advised that once we have posted our material through your system, it cannot be opened for any inspection without authorization of a judge.” <em>Ibid.</em></blockquote>
<p id="b603-5">The letter invited petitioner to send for more information. It also asked petitioner to sign an affirmation that he was “not a law enforcement officer or agent of the U. S. Government acting in an undercover capacity for the purpose of entrapping Far Eastern Trading Company, its agents or customers.” Petitioner responded. <em>Ibid. </em>A catalog was sent, <em>id., </em>Government Exhibit 2, and petitioner ordered Boys Who Love Boys, <em>id., </em>Government Exhibit 3, a pornographic magazine depicting young boys engaged in various sexual activities. Petitioner was arrested after a controlled delivery of a photocopy of the magazine.</p>
<p id="b603-6">When petitioner was asked at trial why he placed such an order, he explained that the Government had succeeded in piquing his curiosity:</p>
<blockquote id="b603-7">“Well, the statement was made of all the trouble and the hysteria over pornography and I wanted to see what the material was. It didn’t describe the — I didn’t know for sure what kind of sexual action they were referring to in the Canadian letter.” Tr. 427-428.</blockquote>
<p id="b603-8">In petitioner’s home, the Government found the Bare Boys magazines and materials that the Government had sent to him in the course of its protracted investigation, but no other materials that would indicate that petitioner collected, or was actively interested in, child pornography.</p>
<p id="b603-9">Petitioner was indicted for violating <span class="citation no-link">18 U. S. C. § 2252</span>(a) (2)(A). The trial court instructed the jury on the petitioner’s entrapment defense,<footnotemark>1</footnotemark> petitioner was convicted, and a di<page-number citation-index="1" label="548">*548</page-number>vided Court of Appeals for the Eighth Circuit, sitting en banc, affirmed, concluding that “Jacobson was not entrapped as a matter of law.” <span class="citation" data-id="9480896"><a href="/opinion/549820/united-states-v-keith-m-jacobson/#470" aria-description="Citation for case: United States v. Keith M. Jacobson">916 F. 2d 467, 470</a></span> (1990). We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./499/974/">499 U. S. 974</a></span> (1991).</p>
<p id="b604-3">II</p>
<p id="ArF">There can be no dispute about the evils of child pornography or the difficulties that laws and law enforcement have encountered in eliminating it. See generally <em>Osborne </em>v. <em>Ohio, </em><span class="citation" data-id="9431982"><a href="/opinion/112417/osborne-v-ohio/#110" aria-description="Citation for case: Osborne v. Ohio">495 U. S. 103, 110</a></span> (1990); <em>New York </em>v. <em>Ferber, </em><span class="citation" data-id="9428936"><a href="/opinion/110794/new-york-v-ferber/#759" aria-description="Citation for case: New York v. Ferber">458 U. S. 747, 759-760</a></span> (1982). Likewise, there can be no dispute that the Government may use undercover agents to enforce the law. “It is well settled that the fact that officers or employees of the Government merely afford opportunities or facilities for the commission of the offense does not defeat the prosecution. Artifice and stratagem may be employed to catch those engaged in criminal enterprises.” <em>Sorrells </em>v. <em>United States, </em><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#441" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435, 441</a></span> (1932); <em>Sherman, </em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#372" aria-description="Citation for case: Sherman v. United States">356 U. S., at 372</a></span>; <em>United States </em>v. <em>Russell, </em><span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#435" aria-description="Citation for case: United States v. Russell">411 U. S. 423, 435-436</a></span> (1973).</p>
<p id="b604-4">In their zeal to enforce the law, however, Government agents may not originate a criminal design, implant in an innocent person’s mind the disposition to commit a criminal act, and then induce commission of the crime so that the Government may prosecute. <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#442" aria-description="Citation for case: Sorrells v. United States"><em>Sorrells, supra, </em>at 442</a></span>; <span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#372" aria-description="Citation for case: Sherman v. United States"><em>Sherman, supra, </em>at 372</a></span>. Where the Government has induced an <page-number citation-index="1" label="549">*549</page-number>individual to break the law and the defense of entrapment is at issue, as it was in this case, the prosecution must prove beyond reasonable doubt that the defendant was disposed to commit the criminal act prior to first being approached by Government agents. <em>United States </em>v. <em>Whole, </em>288 U. S. App. D. C. 261, 263-264, <span class="citation" data-id="556376"><a href="/opinion/556376/united-states-v-donald-whoie/#1483" aria-description="Citation for case: United States v. Donald Whoie">925 F. 2d 1481, 1483-1484</a></span> (1991).<footnotemark>2</footnotemark></p>
<p id="b605-5">Thus, an agent deployed to stop the traffic in illegal drugs may offer the opportunity to buy or sell drugs and, if the offer is accepted, make an arrest on the spot or later. In <page-number citation-index="1" label="550">*550</page-number>such a typical case, or in a more elaborate “sting” operation involving government-sponsored fencing where the defendant is simply provided with the opportunity to commit a crime, the entrapment defense is of little use because the ready commission of the criminal act amply demonstrates the defendant’s predisposition. See <em>United States </em>v. <em>Sherman, </em><span class="citation" data-id="230738"><a href="/opinion/230738/united-states-v-sherman/#882" aria-description="Citation for case: United States v. Sherman">200 F. 2d 880, 882</a></span> (CA2 1952). Had the agents in this case simply offered petitioner the opportunity to order child pornography through the mails, and petitioner — who must be presumed to know the law — had promptly availed himself of this criminal opportunity, it is unlikely that his entrapment defense would have warranted a jury instruction. <em>Mathews </em>v. <em>United States, </em><span class="citation" data-id="9431220"><a href="/opinion/112012/mathews-v-united-states/#66" aria-description="Citation for case: Mathews v. United States">485 U. S. 58, 66</a></span> (1988).</p>
<p id="b606-5">But that is not what happened here. By the time petitioner finally placed his order, he had already been the target of 26 months of repeated mailings and communications from Government agents and fictitious organizations. Therefore, although he had become predisposed to break the law by May 1987, it is our view that the Government did not prove that this predisposition was independent and not the product of the attention that the Government had directed at petitioner since January 1985. <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#442" aria-description="Citation for case: Sorrells v. United States"><em>Sorrells, supra, </em>at 442</a></span>; <em>Sherman, </em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#372" aria-description="Citation for case: Sherman v. United States">356 U. S., at 372</a></span>.</p>
<p id="b606-6">The prosecution’s evidence of predisposition falls into two categories: evidence developed prior to the Postal Service’s mail campaign, and that developed during the course of the investigation. The sole piece of preinvestigation evidence is petitioner’s 1984 order and receipt of the Bare Boys magazines. But this is scant if any proof of petitioner’s predisposition to commit an illegal act, the criminal character of which a defendant is presumed to know. It may indicate a predisposition to view sexually oriented photographs that are responsive to his sexual tastes; but evidence that merely indicates a generic inclination to act within a broad range, not all of which is criminal, is of little probative value in establishing predisposition.</p>
<p id="b607-4"><page-number citation-index="1" label="551">*551</page-number>Furthermore, petitioner was acting within the law at the time he received these magazines. Receipt through the mails of sexually explicit depictions of children for noncommercial use did not become illegal under federal law until May 1984, and Nebraska had no law that forbade petitioner’s possession of such material until 1988. <span class="citation no-link">Neb. Rev. Stat. § 28-813.01</span> (1989). Evidence of predisposition to do what once was lawful is not, by itself, sufficient to show predisposition to do what is now illegal, for there is a common understanding that most people obey the law even when they disapprove of it. This obedience may reflect a generalized respect for legality or the fear of prosecution, but for whatever reason, the law’s prohibitions are matters of consequence. Hence, the fact that petitioner legally ordered and received the Bare Boys magazines does little to further the Government’s burden of proving that petitioner was predisposed to commit a criminal act. This is particularly true given petitioner’s unchallenged testimony that he did not know until they arrived that the magazines would depict minors.</p>
<p id="b607-5">The prosecution’s evidence gathered during the investigation also fails to carry the ■ Government’s burden. Petitioner’s responses to the many communications prior to the ultimate criminal act were at most indicative of certain personal inclinations, including a predisposition to view photographs of preteen sex and a willingness to promote a given agenda by supporting lobbying organizations. Even so, petitioner’s responses hardly support an inference that he would commit the crime of receiving child pornography through the mails.<footnotemark>3</footnotemark> Furthermore, a person’s inclinations and “fantasies . . . are <page-number citation-index="1" label="552">*552</page-number>his own and beyond the reach of government. . . <em>Paris Adult Theatre I </em>v. <em>Slaton, </em><span class="citation" data-id="9425382"><a href="/opinion/108839/paris-adult-theatre-i-v-slaton/#67" aria-description="Citation for case: Paris Adult Theatre I v. Slaton">413 U. S. 49, 67</a></span> (1973); <em>Stanley </em>v. <em>Georgia, </em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/#565" aria-description="Citation for case: Stanley v. Georgia">394 U. S. 557, 565-566</a></span> (1969).</p>
<p id="b608-5">On the other hand, the strong arguable inference is that, by waving the banner of individual rights and disparaging the legitimacy and constitutionality of efforts to restrict the availability of sexually explicit materials, the Government not only excited petitioner’s interest in sexually explicit materials banned by law but also exerted substantial pressure on petitioner to obtain and read such material as part of a fight against censorship and the infringement of individual rights. For instance, HINT described itself as “an organization founded to protect and promote sexual freedom and freedom of choice” and stated that “the most appropriate means to accomplish [its] objectives is to promote honest dialogue among concerned individuals and to continue its lobbying efforts with State Legislators.” Record, Defendant’s Exhibit 113. These lobbying efforts were to be financed through catalog sales. <em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/" aria-description="Citation for case: Stanley v. Georgia">Ibid.</a></span> </em>Mailings from the equally fictitious American Hedonist Society, <em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/" aria-description="Citation for case: Stanley v. Georgia">id.,</a></span> </em>Government Exhibit 7, and the correspondence from the nonexistent Carl Long, <em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/" aria-description="Citation for case: Stanley v. Georgia">id.,</a></span> </em>Defendant’s Exhibit 5, endorsed these themes.</p>
<p id="b608-6">Similarly, the two solicitations in the spring of 1987 raised the spectre of censorship while suggesting that petitioner ought to be allowed to do what he had been solicited to do. The mailing from the Customs Service referred to “the worldwide ban and intense enforcement on this type of material,” observed that “what was legal and commonplace is now an ‘underground’ and secretive service,” and emphasized that “[t]his environment forces us to take extreme measures” to ensure delivery. <em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/" aria-description="Citation for case: Stanley v. Georgia">Id.,</a></span> </em>Government Exhibit 22. The Postal Service solicitation described the concern about child pornography as “hysterical nonsense,” decried “international censorship,” and assured petitioner, based on consultation with “American solicitors,” that an order that had been posted could not be opened for inspection without au<page-number citation-index="1" label="553">*553</page-number>thorization of a judge. <em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/" aria-description="Citation for case: Stanley v. Georgia">Id.,</a></span> </em>Government Exhibit 1. It further asked petitioner to affirm that he was not a Government agent attempting to entrap the mail order company or its customers. <em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/" aria-description="Citation for case: Stanley v. Georgia">Ibid.</a></span> </em>In these particulars, both Government solicitations suggested that receiving this material was something that petitioner ought to be allowed to do.</p>
<p id="b609-5">Petitioner’s ready response to these solicitations cannot be enough to establish beyond reasonable doubt that he was predisposed, prior to the Government acts intended to create predisposition, to commit the crime of receiving child pornography through the mails. See <em>Sherman, </em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#374" aria-description="Citation for case: Sherman v. United States">356 U. S., at 374</a></span>. The evidence that petitioner was ready and willing to commit the offense came only after the Government had devoted 2V2 years to convincing him that he had or should have the right to engage in the very behavior proscribed by law. Rational jurors could not say beyond a reasonable doubt that petitioner possessed the requisite predisposition prior to the Government’s investigation and that it existed independent of the Government’s many and varied approaches to petitioner. As was explained in <em>Sherman, </em>where entrapment was found as a matter of law, “the Government [may not] pla[y] on the weaknesses of an innocent party and beguil[e] him into committing crimes which he otherwise would not have attempted.” <em>Id., </em>at 376.</p>
<p id="b609-6">Law enforcement officials go too far when they “implant in the mind of an innocent person the <em>disposition </em>to commit the alleged offense and induce its commission in order that they may prosecute.” <em>Sorrells, </em><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#442" aria-description="Citation for case: Sorrells v. United States">287 U. S., at 442</a></span> (emphasis added). Like the <em><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span> </em>Court, we are “unable to conclude that it was the intention of the Congress in enacting this statute that its processes of detection and enforcement should be abused by the instigation by government officials of an act on the part of persons otherwise innocent in order to lure them to its commission and to punish them.” <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#448" aria-description="Citation for case: Sorrells v. United States"><em>Id., </em>at 448</a></span>. When the Government’s quest for convictions leads to the apprehension of an otherwise law-abiding citizen who, if <page-number citation-index="1" label="554">*554</page-number>left to his own devices, likely would have never run afoul of the law, the courts should intervene.</p>
<p id="b610-5">Because we conclude that this is such a case and that the prosecution failed, as a matter of law, to adduce evidence to support the jury verdict that petitioner was predisposed, independent of the Government’s acts and beyond a reasonable doubt, to violate the law by receiving child pornography through the mails, we reverse the Court of Appeals’ judgment affirming the conviction of Keith Jacobson.</p>
<p id="b610-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b603-10"> The jury was instructed:</p>
<blockquote id="b603-11">“As mentioned, one of the issues in this case is whether the defendant was entrapped. If the defendant was entrapped he must be found not <page-number citation-index="1" label="548">*548</page-number>guilty. The government has the burden of proving beyond a reasonable doubt that the defendant was not entrapped.</blockquote>
<blockquote id="b604-6">“If the defendant before contact with law-enforcement officers or their agents did not have any intent or disposition to commit the crime charged and was induced or persuaded by law-enforcement officers o[r] their agents to commit that crime, then he was entrapped. On the other hand, if the defendant before contact with law-enforcement officers or their agents did have an intent or disposition to commit the crime; charged, then he was not entrapped even though law-enforcement officers or their agents provided a favorable opportunity to commit the crime or made committing the crime easier or even participated in acts essential to the crime.” App. 11-12.</blockquote>
</footnote>
<footnote label="2">
<p id="b605-6"> Inducement is not at issue in this case. The Government does not dispute that it induced petitioner to commit the crime. The sole issue is whether the Government carried its burden of proving that petitioner was predisposed to violate the law <em>before </em>the Government intervened. The dissent is mistaken in claiming that this is an innovation in entrapment law and in suggesting that the Government’s conduct prior to the moment of solicitation is irrelevant. See <em>post, </em>at 556-557. The Court rejected these arguments six decades ago in <em>Sorrells </em>v. <em>United States, </em><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435</a></span> (1932), when the Court wrote that the Government may not punish an individual “for an alleged offense which is the product of the creative activity of its own officials” and that in such a case the Government “is in no position to object to evidence of the activities of its representatives in relation to the accused . . . .” <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#451" aria-description="Citation for case: Sorrells v. United States"><em>Id., </em>at 451</a></span>. Indeed, the proposition that the accused must be predisposed prior to contact with law enforcement officers is so firmly established that the Government conceded the point at oral argument, submitting that the evidence it developed during the course of its investigation was probative because it indicated petitioner’s state of mind <em>prior </em>to the commencement of the Government’s investigation. See Tr. of Oral Arg. 41, 49.</p>
<p id="b605-7">This long-established standard in no way encroaches upon Government investigatory activities. Indeed, the Government’s internal guidelines for undercover operations provide that an inducement to commit a crime should not be offered unless:</p>
<blockquote id="b605-8">“(a) [Tjhere is a reasonable indication, based on information developed through informants or other means, that the subject is engaging, has engaged, or is likely to engage in illegal activity of a similar type; <em>or</em></blockquote>
<blockquote id="b605-9">“(b) The opportunity for illegal activity has been structured so that there is reason for believing that-persons drawn to the opportunity, or brought to it, are predisposed to engage in the contemplated illegal activity.” Attorney General’s Guidelines on FBI Undercover Operations (Dec. 31,1980), reprinted in S. Rep. No. 97-682, p. 551 (1982).-</blockquote>
</footnote>
<footnote label="3">
<p id="b607-6"> We do not hold, as the dissent suggests, see <em>post, </em>at 559-560, that the Government was required to prove that petitioner knowingly violated the law. We simply conclude that proof that petitioner engaged in legal conduct and possessed certain generalized personal inclinations is not sufficient evidence to prove beyond a reasonable doubt that he would have been predisposed to commit the crime charged independent of the Government’s coaxing.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/James v. Illinois.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "James v. Illinois"
type: case
citation: "493 U.S. 307 (1990)"
parallel_cite: "110 S. Ct. 648; 107 L. Ed. 2d 676; 58 U.S.L.W. 4115"
neutral_cite: 1990 U.S. LEXIS 335
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1990
date_decided: 1990-01-10
docket: 88-6075
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1990-01-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: James v. Illinois
  varies_by_point: false
  scope_note: "Caps the impeachment exception at the defendant's own testimony; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112350/james-v-illinois/"
  cluster_id: 112350
  opinion_id: 112350
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Limiting (impeachment exception)"
related: ["[[Walder v. United States]]", "[[United States v. Havens]]", "[[Elkins v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "impeachment-exception", "defense-witness", "deterrence"]
holding: "The impeachment exception to the exclusionary rule is confined to the defendant's own testimony; the prosecution may not use illegally obtained evidence to impeach the testimony of other defense witnesses."
lake:
  record_id: James v. Illinois
  status: verified
  projected_at: 2026-07-06
---

# James v. Illinois

*493 U.S. 307 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
James was tried for murder. Eyewitnesses described the shooter as having slicked-back reddish hair; a defense witness, Henderson, testified that James's hair was black and worn in a natural style on the day of the shooting. To impeach Henderson, the prosecution introduced statements James had made after an illegal arrest — that his hair had been reddish-brown and curly and that he had it dyed and straightened. The Illinois courts extended the impeachment exception to permit this use against the defense witness, and James was convicted.

## Issue
Whether the impeachment exception to the exclusionary rule permits the prosecution to use illegally obtained evidence to impeach the testimony of defense witnesses other than the defendant himself.

## Rule
No. "[E]xpanding the class of impeachable witnesses from the defendant alone to all defense witnesses would create different incentives affecting the behavior of both defendants and law enforcement officers. As a result, this expansion would not promote the truth-seeking function to the same extent as did creation of the original exception, and yet it would significantly undermine the deterrent effect of the general exclusionary rule." — 493 U.S. at 313–314. ^pin-313

Defendants "ought not be able to 'pervert' the exclusion of illegally obtained evidence into a shield for perjury, but it seems no more appropriate for the State to brandish such evidence as a sword with which to dissuade defendants from presenting a meaningful defense through other witnesses." — *Id.* at 317. ^pin-317

## Application
The illegally obtained statements were used to impeach Henderson, a defense witness, not James himself. Extending the exception that far would chill defendants from calling witnesses (who cannot be perfectly controlled) and would sharply increase the prosecution's incentive to gather evidence illegally, since defense witnesses far outnumber testifying defendants — making police misconduct "far more than a 'speculative possibility.'" The truth-seeking rationale of *[[Walder v. United States|Walder]]* "does not apply to other witnesses with equal force," so the exclusionary rule's deterrent purpose required keeping the exception narrow.

## Conclusion
"[W]e adhere to the line drawn in our previous cases. Accordingly, we hold that the Illinois Supreme Court erred in affirming James' convictions despite the prosecutor's use of illegally obtained statements to impeach a defense witness' testimony." — *Id.* at 320. ^pin-320

The judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *James* **limits** the impeachment exception of [[Walder v. United States]] and [[United States v. Havens]] to the defendant's own testimony, invoking the deterrence rationale of [[Elkins v. United States]].

## Appears on
- [[The Exclusionary Rule]] — *Key — Limiting (impeachment exception)*

## Sources
- *James v. Illinois*, 493 U.S. 307 (1990) — https://www.courtlistener.com/opinion/112350/james-v-illinois/ — pinpoints: 313–314, 317, 320.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "cf3dc345a59a9fce", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "James v. Illinois"}, "payload": {"all": [{"cite": "493 U.S. 307", "page": "307", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "493"}, {"cite": "110 S. Ct. 648", "page": "648", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "110"}, {"cite": "107 L. Ed. 2d 676", "page": "676", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "107"}, {"cite": "1990 U.S. LEXIS 335", "page": "335", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1990"}, {"cite": "58 U.S.L.W. 4115", "page": "4115", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "58"}], "display": "493 U.S. 307", "official": {"cite": "493 U.S. 307", "page": "307", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "493"}, "official_selection_present": true, "record_id": "James v. Illinois"}}
{"assertion_id": "4724b8f3494e2bf5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-320", "record_id": "James v. Illinois"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-320", "pinpoint_status": "slip-only", "quote": "so the exclusionary rule's deterrent purpose required keeping the exception narrow. ## Conclusion", "quote_fidelity": "mismatch", "record_id": "James v. Illinois", "star_marker": null}}
{"assertion_id": "ad1bba4400211a3b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-313", "record_id": "James v. Illinois"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-313", "pinpoint_status": "slip-only", "quote": "--- # James v. Illinois *493 U.S. 307 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background James was tried for murder. Eyewitnesses described the shooter as having slicked-back reddish hair; a defense witness, Henderson, testified that James's hair was black and worn in a natural style on the day of the shooting. To impeach Henderson, the prosecution introduced statements James had made after an illegal arrest — that his hair had been reddish-brown and curly and that he had it dyed and straightened. The Illinois courts extended the impeachment exception to permit this use against the defense witness, and James was convicted. ## Issue Whether the impeachment exception to the exclusionary rule permits the prosecution to use illegally obtained evidence to impeach the testimony of defense witnesses other than the defendant himself. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "James v. Illinois", "star_marker": null}}
{"assertion_id": "c2d916e4b07d5884", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-317", "record_id": "James v. Illinois"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-317", "pinpoint_status": "slip-only", "quote": "ought not be able to 'pervert' the exclusion of illegally obtained evidence into a shield for perjury, but it seems no more appropriate for the State to brandish such evidence as a sword with which to dissuade defendants from presenting a meaningful defense through other witnesses.", "quote_fidelity": "mismatch", "record_id": "James v. Illinois", "star_marker": null}}
{"assertion_id": "84690db2c6e10a89", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "James v. Illinois"}, "payload": {"as_of_content": "1990-01-10", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "James v. Illinois", "scope_note": "Caps the impeachment exception at the defendant's own testimony; good law.", "varies_by_point": false}}
```

### lake record — James v. Illinois

```json
{
  "schema_version": "s2.v1",
  "record_id": "James v. Illinois",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "James v. Illinois",
    "case_name_short": "James",
    "case_name_full": "James v. Illinois",
    "input_case_name": "James v. Illinois",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-01-10",
    "year": 1990,
    "docket": "88-6075",
    "cluster_id": 112350,
    "lead_opinion_id": 112350,
    "sibling_ids": [
      112350,
      9431873,
      9431874,
      9431875
    ],
    "absolute_url": "/opinion/112350/james-v-illinois/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "493 U.S. 307",
      "volume": "493",
      "reporter": "U.S.",
      "page": "307",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "110 S. Ct. 648",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "648",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 L. Ed. 2d 676",
        "volume": "107",
        "reporter": "L. Ed. 2d",
        "page": "676",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 U.S.L.W. 4115",
        "volume": "58",
        "reporter": "U.S.L.W.",
        "page": "4115",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 335",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "335",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "493 U.S. 307",
        "volume": "493",
        "reporter": "U.S.",
        "page": "307",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 S. Ct. 648",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "648",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 L. Ed. 2d 676",
        "volume": "107",
        "reporter": "L. Ed. 2d",
        "page": "676",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 335",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "335",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 U.S.L.W. 4115",
        "volume": "58",
        "reporter": "U.S.L.W.",
        "page": "4115",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "493 U.S. 307",
    "official_selection": {
      "court_class": "scotus",
      "selected": "493 U.S. 307",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-313",
      "page": null,
      "quote": "--- # James v. Illinois *493 U.S. 307 (1990)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background James was tried for murder. Eyewitnesses described the shooter as having slicked-back reddish hair; a defense witness, Henderson, testified that James's hair was black and worn in a natural style on the day of the shooting. To impeach Henderson, the prosecution introduced statements James had made after an illegal arrest \u2014 that his hair had been reddish-brown and curly and that he had it dyed and straightened. The Illinois courts extended the impeachment exception to permit this use against the defense witness, and James was convicted. ## Issue Whether the impeachment exception to the exclusionary rule permits the prosecution to use illegally obtained evidence to impeach the testimony of defense witnesses other than the defendant himself. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-317",
      "page": null,
      "quote": "ought not be able to 'pervert' the exclusion of illegally obtained evidence into a shield for perjury, but it seems no more appropriate for the State to brandish such evidence as a sword with which to dissuade defendants from presenting a meaningful defense through other witnesses.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-320",
      "page": null,
      "quote": "so the exclusionary rule's deterrent purpose required keeping the exception narrow. ## Conclusion",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1990-01-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "James v. Illinois",
    "varies_by_point": false,
    "scope_note": "Caps the impeachment exception at the defendant's own testimony; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Patricia Hendrickson v. Larry Norris, Director, Arkansas Department of Correction",
          "cluster_id": 770174,
          "cite": [
            "224 F.3d 748",
            "2000 U.S. App. LEXIS 22529",
            "2000 WL 1264147"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Payne v. Tennessee",
          "cluster_id": 112643,
          "cite": [
            "115 L. Ed. 2d 720",
            "111 S. Ct. 2597",
            "501 U.S. 808",
            "1991 U.S. LEXIS 3821"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
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
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Boyer",
          "cluster_id": 2515839,
          "cite": [
            "133 P.3d 581",
            "42 Cal. Rptr. 3d 677",
            "38 Cal. 4th 412",
            "2006 Daily Journal DAR 5671",
            "2006 Cal. Daily Op. Serv. 3863",
            "2006 Cal. LEXIS 5397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Johnson",
          "cluster_id": 4889243,
          "cite": [
            "2021 CO 35"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
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
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Electroplating, Inc.",
          "cluster_id": 1082668,
          "cite": [
            "990 S.W.2d 211",
            "1998 Tenn. Crim. App. LEXIS 618",
            "1998 WL 301728"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Toma",
          "cluster_id": 2221692,
          "cite": [
            "613 N.W.2d 694",
            "462 Mich. 281"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 2085422,
          "cite": [
            "692 N.E.2d 1109",
            "181 Ill. 2d 297",
            "229 Ill. Dec. 898",
            "1998 Ill. LEXIS 5"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Daugherty",
          "cluster_id": 1777786,
          "cite": [
            "931 S.W.2d 268",
            "1996 Tex. Crim. App. LEXIS 88",
            "1996 WL 350804"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williams v. Poulos",
          "cluster_id": 195087,
          "cite": [
            "11 F.3d 271",
            "1993 WL 503326"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Goldston",
          "cluster_id": 848710,
          "cite": [
            "682 N.W.2d 479",
            "470 Mich. 523"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State Ex Rel. State Farm Fire & Casualty Co. v. Madden",
          "cluster_id": 1327799,
          "cite": [
            "451 S.E.2d 721",
            "192 W. Va. 155",
            "1994 W. Va. LEXIS 157"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lopez-Vazquez v. State",
          "cluster_id": 2313621,
          "cite": [
            "956 A.2d 1280",
            "2008 Del. LEXIS 391",
            "2008 WL 3988236"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Flynn",
          "cluster_id": 1303640,
          "cite": [
            "527 N.W.2d 343",
            "190 Wis. 2d 31",
            "1994 Wisc. App. LEXIS 1514"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manns v. State",
          "cluster_id": 1881009,
          "cite": [
            "122 S.W.3d 171",
            "2003 Tex. Crim. App. LEXIS 960",
            "2003 WL 22962189"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Burris",
          "cluster_id": 1998119,
          "cite": [
            "679 A.2d 121",
            "145 N.J. 509",
            "1996 N.J. LEXIS 958"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Kuntz",
          "cluster_id": 1598839,
          "cite": [
            "467 N.W.2d 531",
            "160 Wis. 2d 722",
            "1991 Wisc. LEXIS 33"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mertz",
          "cluster_id": 2099747,
          "cite": [
            "842 N.E.2d 618",
            "218 Ill. 2d 1",
            "299 Ill. Dec. 581",
            "2005 Ill. LEXIS 1612"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Johnson",
          "cluster_id": 2282662,
          "cite": [
            "183 Cal. App. 4th 253",
            "107 Cal. Rptr. 3d 228",
            "2010 Cal. App. LEXIS 429"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Guthrie",
          "cluster_id": 1347152,
          "cite": [
            "518 S.E.2d 83",
            "205 W. Va. 326",
            "1999 W. Va. LEXIS 62"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Herrera",
          "cluster_id": 167373,
          "cite": [
            "444 F.3d 1238",
            "2006 U.S. App. LEXIS 9830",
            "2006 WL 1017642"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Johnson",
          "cluster_id": 4672578,
          "cite": [
            "2019 COA 159"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Edward Trzaska",
          "cluster_id": 739906,
          "cite": [
            "111 F.3d 1019",
            "46 Fed. R. Serv. 1526",
            "1997 U.S. App. LEXIS 9336",
            "1997 WL 211540"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jones",
          "cluster_id": 2128162,
          "cite": [
            "810 N.E.2d 415",
            "2 N.Y.3d 235",
            "778 N.Y.S.2d 133",
            "2 N.Y. 235",
            "2004 N.Y. LEXIS 638"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joshua Brent Gray, United States of America v. Terrence A. Askew",
          "cluster_id": 798157,
          "cite": [
            "491 F.3d 138",
            "2007 U.S. App. LEXIS 15760",
            "2007 WL 1881194"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "James v. Illinois:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112350 OR 9431873 OR 9431874 OR 9431875) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
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
        "query": "cites:(112350 OR 9431873 OR 9431874 OR 9431875)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMCZzPTIyNzA2ODcmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112350+OR+9431873+OR+9431874+OR+9431875%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112350 OR 9431873 OR 9431874 OR 9431875)",
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
    "complete_query": "cites:(112350 OR 9431873 OR 9431874 OR 9431875)",
    "indexed_citing_opinions": 114,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112350,
        "count": 104,
        "count_source": "search"
      },
      {
        "opinion_id": 9431873,
        "count": 11,
        "count_source": "search"
      },
      {
        "opinion_id": 9431874,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431875,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 171,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/james-v-illinois.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQwNTM0ODEmcz0yNjUxMDMyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112350+OR+9431873+OR+9431874+OR+9431875%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112350,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 108551,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 108718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 109387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 110090,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 110267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 111834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 111835,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 1975705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 2037151,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 2228726,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112350,
        "cited_id": 3420640,
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
    "date_created": "2026-07-05T08:52:02Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:52:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:52:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:55:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:52:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — James v. Illinois

```
<div>
<center><b><span class="citation" data-id="9431873"><a href="/opinion/112350/james-v-illinois/" aria-description="Citation for case: James v. Illinois">493 U.S. 307</a></span> (1990)</b></center>
<center><h1>JAMES<br>
v.<br>
ILLINOIS</h1></center>
<center>No. 88-6075.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 3, 1989</center>
<center>Decided January 10, 1990</center>
CERTIORARI TO THE SUPREME COURT OF ILLINOIS
<p><span class="star-pagination">*308</span> <i>Martin S. Carlson</i> argued the cause for petitioner. With him on the briefs were <i>Theodore A. Gottfried, Michael J. Pelletier,</i> and <i>Patricia Unsinn.</i></p>
<p><i>Terence M. Madsen,</i> Assistant Attorney General of Illinois, argued the cause for respondent. With him on the brief were <i>Neil F. Hartigan,</i> Attorney General, <i>Robert J. Ruiz,</i> Solicitor General, <i>Arleen C. Anderson, Nathan P. Maddox,</i> and <i>Michael J. Singer,</i> Assistant Attorneys General, <i>Cecil A. Partee, Inge Fryklund,</i> and <i>Sharon Johnson Coleman.</i><sup>[*]</sup></p>
<p>JUSTICE BRENNAN delivered the opinion of the Court.</p>
<p>The impeachment exception to the exclusionary rule permits the prosecution in a criminal proceeding to introduce illegally <span class="star-pagination">*309</span> obtained evidence to impeach the defendant's own testimony. The Illinois Supreme Court extended this exception to permit the prosecution to impeach the testimony of <i>all</i> defense witnesses with illegally obtained evidence. <span class="citation" data-id="9741804"><a href="/opinion/2228726/people-v-james/" aria-description="Citation for case: People v. James">123 Ill. 2d 523</a></span>, <span class="citation" data-id="9741804"><a href="/opinion/2228726/people-v-james/" aria-description="Citation for case: People v. James">528 N. E. 2d 723</a></span> (1988). Finding this extension inconsistent with the balance of values underlying our previous applications of the exclusionary rule, we reverse.</p>
<p></p>
<h2>I</h2>
<p>On the night of August 30, 1982, eight young boys returning home from a party were confronted by a trio of other boys who demanded money. When the eight boys refused to comply, one member of the trio produced a gun and fired into the larger group, killing one boy and seriously injuring another. When the police arrived, the remaining members of the larger group provided eyewitness accounts of the event and descriptions of the perpetrators.</p>
<p>The next evening, two detectives of the Chicago Police Department took 15-year-old Darryl James into custody as a suspect in the shooting. James was found at his mother's beauty parlor sitting under a hair dryer; when he emerged, his hair was black and curly. After placing James in their car, the detectives questioned him about his prior hair color. He responded that the previous day his hair had been reddish brown, long, and combed straight back. The detectives questioned James again later at the police station, and he further stated that he had gone to the beauty parlor in order to have his hair "dyed black and curled in order to change his appearance." App. 11.</p>
<p>The State subsequently indicted James for murder and attempted murder. Prior to trial, James moved to suppress the statements regarding his hair, contending that they were the fruit of a Fourth Amendment violation because the detectives lacked probable cause for his warrantless arrest. After an evidentiary hearing, the trial court sustained this <span class="star-pagination">*310</span> motion and ruled that the statements would be inadmissible at trial.</p>
<p>At trial, five members of the larger group of boys testified for the State, and each made an in-court identification of the defendant. Each testified that the person responsible for the shooting had "reddish" hair, worn shoulder length in a slicked-back "butter" style. Each also recalled having seen James several weeks earlier at a parade, at which time James had the aforementioned hair color and style. At trial, however, his hair was black and worn in a "natural" style. Despite the discrepancy between the witnesses' description and his present appearance, the witnesses stood firm in their conviction that James had been present and had fired the shots.</p>
<p>James did not testify in his own defense. He called as a witness Jewel Henderson, a fried of his family. Henderson testified that on the day of the shooting she had taken James to register for high school and that, at that time, his hair was black. The State then sought, over James' objection, to introduce his illegally obtained statements as a means of impeaching the credibility of Henderson's testimony. After determining that the suppressed statements had been made voluntarily, the trial court overruled James' objection. One of the interrogating detectives then reported James' prior admissions that he had reddish hair the night of the shooting and he dyed and curled his hair the next day in order to change his appearance. James ultimately was convicted of both murder and attempted murder and sentenced to 30 years' imprisonment.</p>
<p>On appeal, the Illinois Appellate Court reversed James' convictions and ordered a new trial. <span class="citation" data-id="1975705"><a href="/opinion/1975705/people-v-james/" aria-description="Citation for case: People v. James">153 Ill. App. 3d 131</a></span>, <span class="citation" data-id="1975705"><a href="/opinion/1975705/people-v-james/" aria-description="Citation for case: People v. James">505 N. E. 2d 1118</a></span> (1987). The appellate court held that the exclusionary rule barred admission of James' illegally obtained statements for the purpose of impeaching a defense witness' testimony and that the resulting constitutional error was not harmless. However, the Illinois Supreme Court reversed. <span class="star-pagination">*311</span> The court reasoned that, in order to deter the defendant from engaging in perjury "by proxy," the impeachment exception to the exclusionary rule ought to be expanded to allow the State to introduce illegally obtained evidence to impeach the testimony of defense witnesses other than the defendant himself. The court therefore ordered James' convictions reinstated. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./489/1010/">489 U. S. 1010</a></span> (1989).</p>
<p></p>
<h2>II</h2>
<p>"There is no gainsaying that arriving at the truth is a fundamental goal of our legal system." <i>United States</i> v. <i>Havens,</i> <span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#626" aria-description="Citation for case: United States v. Havens">446 U. S. 620, 626</a></span> (1980). But various constitutional rules limit the means by which government may conduct this search for truth in order to promote other values embraced by the Framers and cherished throughout our Nation's history. "Ever since its inception, the rule excluding evidence seized in violation of the Fourth Amendment has been recognized as a principal mode of discouraging lawless police conduct. . . . [W]ithout it the constitutional guarantee against unreasonable searches and seizures would be a mere `form of words.' " <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#12" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 12</a></span> (1968), quoting <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#655" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 655</a></span> (1961). The occasional suppression of illegally obtained yet probative evidence has long been considered a necessary cost of preserving overriding constitutional values: "[T]here is nothing new in the realization that the Constitution sometimes insulates the criminality of a few in order to protect the privacy of us all." <i>Arizona</i> v. <i>Hicks,</i> <span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#329" aria-description="Citation for case: Arizona v. Hicks">480 U. S. 321, 329</a></span> (1987).</p>
<p>This Court has carved out exceptions to the exclusionary rule, however, where the introduction of reliable and probative evidence would significantly further the truth-seeking function of a criminal trial and the likelihood that admissibility of such evidence would encourage police misconduct is but a "speculative possibility." <i>Harris</i> v. <i>New York,</i> 401 U. S. <span class="star-pagination">*312</span> 222, 225 (1971).<sup>[1]</sup> One exception to the rule permits prosecutors to introduce illegally obtained evidence for the limited purpose of impeaching the credibility of the defendant's own testimony. This Court first recognized this exception in <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span> (1954), permitting the prosecutor to introduce into evidence heroin obtained through an illegal search to undermine the credibility of the defendant's claim that he had never possessed narcotics. The Court explained that a defendant</p>
<blockquote>"must be free to deny all the elements of the case against him without thereby giving leave to the Government to introduce by way of rebuttal evidence illegally secured by it, and therefore not available for its case in chief. Beyond that, however, there is hardly justification for letting the defendant affirmatively resort to perjurious testimony in reliance on the Government's disability to challenge his credibility." <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/#65" aria-description="Citation for case: Walder v. United States"><i>Id.,</i> at 65</a></span>.</blockquote>
<p>In <i>Harris</i> v. <i>New York, supra</i><i>,</i> and <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714</a></span> (1975), the Court applied the exception to permit prosecutors to impeach defendants using incriminating yet voluntary and reliable statements elicited in violation of <i>Miranda</i> requirements.<sup>[2]</sup> Finally, in <i>United States</i> v. <i><span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/" aria-description="Citation for case: United States v. Havens">Havens, supra</a></span></i><i>,</i> the Court expanded the exception to permit <span class="star-pagination">*313</span> prosecutors to introduce illegally obtained evidence in order to impeach a defendant's "answers to questions put to him on cross-examination that are plainly within the scope of the defendant's direct examination." <span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#627" aria-description="Citation for case: United States v. Havens"><i>Id.,</i> at 627</a></span>.</p>
<p>This Court insisted throughout this line of cases that "evidence that has been illegally obtained . . . is inadmissible on the government's direct case, or otherwise, as substantive evidence of guilt." <span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#628" aria-description="Citation for case: United States v. Havens"><i>Id.,</i> at 628</a></span>.<sup>[3]</sup> However, because the Court believed that permitting the use of such evidence to impeach defendants' testimony would further the goal of truthseeking by preventing defendants from perverting the exclusionary rule " `into a license to use perjury by way of a defense,' " <span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#626" aria-description="Citation for case: United States v. Havens"><i>id.,</i> at 626</a></span> (citation omitted), and because the Court further believed that permitting such use would create only a "speculative possibility that impermissible police conduct will be encouraged thereby," <i>Harris, supra,</i> at 225, the Court concluded that the balance of values underlying the exclusionary rule justified an exception covering impeachment of defendants' testimony.</p>
<p></p>
<h2>III</h2>
<p>In this case, the Illinois Supreme Court held that our balancing approach in <i><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span></i> and its progeny justifies expanding the scope of the impeachment exception to permit prosecutors to use illegally obtained evidence to impeach the credibility of defense witnesses. We disagree. Expanding the class of impeachable witnesses from the defendant alone to all defense witnesses would create different incentives affecting the behavior of both defendants and law enforcement officers. As a result, this expansion would not promote the truth-seeking function to the same extent as did creation of the original exception, and yet it would significantly undermine <span class="star-pagination">*314</span> the deterrent effect of the general exclusionary rule. Hence, we believe that this proposed expansion would frustrate rather than further the purposes underlying the exclusionary rule.</p>
<p>The previously recognized exception penalizes defendants for committing perjury by allowing the prosecution to expose their perjury through impeachment using illegally obtained evidence. Thus defendants are discouraged in the first instance from "affirmatively resort[ing] to perjurious testimony." <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/#65" aria-description="Citation for case: Walder v. United States"><i>Walder, supra,</i> at 65</a></span>. But the exception leaves defendants free to testify truthfully on their own behalf; they can offer probative and exculpatory evidence to the jury without opening the door to impeachment by carefully avoiding any statements that directly contradict the suppressed evidence. The exception thus generally discourages perjured testimony without discouraging truthful testimony.</p>
<p>In contrast, expanding the impeachment exception to encompass the testimony of all defense witnesses would not have the same beneficial effects. First, the mere threat of a subsequent criminal prosecution for perjury is far more likely to deter a witness from intentionally lying on a defendant's behalf than to deter a defendant, already facing conviction for the underlying offense, from lying on his own behalf. Hence the Illinois Supreme Court's underlying premise that a defendant frustrated by our previous impeachment exception can easily find a witness to engage in "perjury by proxy" is suspect.<sup>[4]</sup></p>
<p>More significantly, expanding the impeachment exception to encompass the testimony of all defense witnesses likely would chill some defendants from presenting their best defense <span class="star-pagination">*315</span>  and sometimes any defense at all  through the testimony of others. Whenever police obtained evidence illegally, defendants would have to assess prior to trial the likelihood that the evidence would be admitted to impeach the otherwise favorable testimony of any witness they call. Defendants might reasonably fear that one or more of their witnesses, in a position to offer truthful and favorable testimony, would also make some statement in sufficient tension with the tainted evidence to allow the prosecutor to introduce that evidence for impeachment. First, defendants sometimes need to call "reluctant" or "hostile" witnesses to provide reliable and probative exculpatory testimony, and such witnesses likely will not share the defendants' concern for avoiding statements that invite impeachment through contradictory evidence. Moreover, defendants often cannot trust even "friendly" witnesses to testify without subjecting themselves to impeachment, simply due to insufficient care or attentiveness. This concern is magnified in those occasional situations when defendants must call witnesses to testify despite having had only a limited opportunity to consult with or prepare them in advance. For these reasons, we have recognized in a variety of contexts that a party "cannot be absolutely certain that his witnesses will testify as expected." <i>Brooks</i> v. <i>Tennessee,</i> <span class="citation" data-id="108551"><a href="/opinion/108551/brooks-v-tennessee/#609" aria-description="Citation for case: Brooks v. Tennessee">406 U. S. 605, 609</a></span> (1972).<sup>[5]</sup> As a result, <span class="star-pagination">*316</span> an expanded impeachment exception likely would chill some defendants from calling witnesses who would otherwise offer probative evidence.<sup>[6]</sup></p>
<p><span class="star-pagination">*317</span> This realization alters the balance of values underlying the current impeachment exception governing defendants' testimony. Our prior cases make clear that defendants ought not be able to "pervert" the exclusion of illegally obtained evidence into a shield for perjury, but it seems no more appropriate for the State to brandish such evidence as a sword with which to dissuade defendants from presenting a meaningful defense through other witnesses. Given the potential chill created by expanding the impeachment exception, the conceded gains to the truth-seeking process from discouraging or disclosing perjured testimony would be offset to some extent by the concomitant loss of probative witness testimony. Thus, the truth-seeking rationale supporting the impeachment of defendants in <i><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span></i> and its progeny does not apply to other witnesses with equal force.</p>
<p>Moreover, the proposed expansion of the current impeachment exception would significantly weaken the exclusionary rule's deterrent effect on police misconduct. This Court has characterized as a mere "speculative possibility," <i>Harris</i> v. <i>New York,</i> 401 U. S., at 225, the likelihood that permitting prosecutors to impeach defendants with illegally obtained <span class="star-pagination">*318</span> evidence would encourage police misconduct. Law enforcement officers will think it unlikely that the defendant will first decide to testify at trial and will also open the door inadvertently to admission of any illegally obtained evidence. Hence, the officers' incentive to acquire evidence through illegal means is quite weak.</p>
<p>In contrast, expanding the impeachment exception to <i>all</i> defense witnesses would significantly enhance the expected value to the prosecution of illegally obtained evidence. First, this expansion would vastly increase the number of occasions on which such evidence could be used. Defense witnesses easily outnumber testifying defendants, both because many defendants do not testify themselves and because many if not most defendants call multiple witnesses on their behalf. Moreover, due to the chilling effect identified above, see <i>supra,</i> at 315-316, illegally obtained evidence holds even greater value to the prosecution for each individual witness than for each defendant. The prosecutor's access to impeachment evidence would not just deter perjury; it would also deter defendants from calling witnesses in the first place, thereby keeping from the jury much probative exculpatory evidence. For both of these reasons, police officers and their superiors would recognize that obtaining evidence through illegal means stacks the deck heavily in the prosecution's favor. It is thus far more than a "speculative possibility" that police misconduct will be encouraged by permitting such use of illegally obtained evidence.</p>
<p>The United States argues that this result is constitutionally acceptable because excluding illegally obtained evidence solely from the prosecution's case in chief would still provide a quantum of deterrence sufficient to protect the privacy interests underlying the exclusionary rule.<sup>[7]</sup> We disagree. Of course, a police officer might in certain situations believe that obtaining particular evidence through illegal means, resulting <span class="star-pagination">*319</span> in its suppression from the case in chief, would prevent the prosecution from establishing a prima facie case to take to a jury. In such situations, the officer likely would be deterred from obtaining the evidence illegally for fear of jeopardizing the entire case. But much if not most of the time, police officers confront opportunities to obtain evidence illegally after they have already legally obtained (or know that they have other means of legally obtaining) sufficient evidence to sustain a prima facie case. In these situations, a rule requiring exclusion of illegally obtained evidence from only the government's case in chief would leave officers with little to lose and much to gain by overstepping constitutional limits on evidence gathering.<sup>[8]</sup> Narrowing the exclusionary rule in this manner, therefore, would significantly undermine the rule's ability "to compel respect for the constitutional guaranty in the only effectively available way  by removing the incentive to disregard it." <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 217</a></span> (1960). So long as we are committed to protecting the people from the disregard of their constitutional rights during the course of criminal investigations, inadmissibility of illegally obtained evidence must remain the rule, not the exception.</p>
<p></p>
<h2>IV</h2>
<p>The cost to the truth-seeking process of evidentiary exclusion invariably is perceived more tangibly in discrete prosecutions than is the protection of privacy values through deterrence of future police misconduct. When defining the precise scope of the exclusionary rule, however, we must focus on systemic effects of proposed exceptions to ensure <span class="star-pagination">*320</span> that individual liberty from arbitrary or oppressive police conduct does not succumb to the inexorable pressure to introduce all incriminating evidence, no matter how obtained, in each and every criminal case. Our previous recognition of an impeachment exception limited to the testimony of defendants reflects a careful weighing of the competing values. Because expanding the exception to encompass the testimony of all defense witnesses would not further the truth-seeking value with equal force but would appreciably undermine the deterrent effect of the exclusionary rule, we adhere to the line drawn in our previous cases.</p>
<p>Accordingly, we hold that the Illinois Supreme Court erred in affirming James' convictions despite the prosecutor's use of illegally obtained statements to impeach a defense witness' testimony. The court's judgment is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE STEVENS, concurring.</p>
<p>While I join the opinion of the Court, certain comments in the dissent prompt this postscript. The dissent answers the wrong question when it states that "[t]he interest in protecting the truth-seeking function of the criminal trial is every bit as strong in this case as in our earlier cases." <i>Post,</i> at 324. This is self-evident. The State always has a strong interest in the truth-seeking function. The proper question, however, is whether the admission of the illegally obtained evidence in this case would sufficiently advance the truth-seeking function to overcome the loss to the deterrent value of the exclusionary rule. With respect to this issue, the dissent overestimates the benefit of the exclusionary rule even to the defendant bent on presenting perjured testimony and exaggerates the injury that exclusion of unlawfully obtained evidence causes to the truth-seeking function.</p>
<p>In "contested criminal trials," <i>post,</i> at 326, the urge to win can unfortunately lead each side to overstate its case. As <span class="star-pagination">*321</span> the Court properly observes, the ability of the dishonest defendant to procure false testimony is tempered by the availability of the illegally obtained evidence for use in a subsequent perjury prosecution of the defense witness. <i>Ante,</i> at 314. A witness who is not on trial faces a far different calculus than one whose testimony can mean the difference between acquittal and a prison sentence. He or she will think long and hard before accepting a defendant's invitation to knowingly offer false testimony that is directly contradicted by the State's evidence. The dissent ignores this "hard reality," <i>post,</i> at 326, in presuming that a defense witness will offer false testimony when that testimony is immunized from rebuttal at trial.</p>
<p>While the dissent assumes false testimony or, at least, faulty recollection with respect to defense witnesses, it is unwilling to entertain the same assumption with respect to the prosecution's witnesses. The evidentiary issue in this case involves the testimony of a police officer about a statement that he allegedly heard the defendant make at the time of his arrest. An officer whose testimony provides the foundation for admission of an oral statement or physical evidence may be influenced by his interest in effective law enforcement or may simply have faulty recollection. It is only by giving 100percent credence to every word of the officer's testimony that the dissent can so categorically state that "the defendant himself revealed the witness' testimony to be false," <i>post,</i> at 324, that "James . . . said his hair was previously red," <i>post,</i> at 327, n. 2, or that information presented to the jury was "known to be untrue," <i>post,</i> at 327. That assumption is no more warranted in the case of prosecution witnesses than the opposite assumption is warranted in the case of defense witnesses.</p>
<p>In this case, in which the guilty verdict is supported by the testimony of five eyewitnesses, it is highly probable that these characterizations are accurate. But the testimony of those five witnesses, on which the dissenters rely for their conclusion that any error committed by the trial court was <span class="star-pagination">*322</span> harmless, <i>post,</i> at 330, would also seem to be sufficient to obviate the need to rely on the officer's rebuttal to discredit the witness Henderson's testimony. Were the officer's testimony not so corroborated, it would surely be improper to presume  as the dissenters do  that the conflict between the testimony of the officer and Henderson should necessarily be resolved in the officer's favor or that exclusion of the evidence would result in a decision by jurors who are "positively misled." <i>Post,</i> at 324.</p>
<p>JUSTICE KENNEDY, with whom THE CHIEF JUSTICE, JUSTICE O'CONNOR, and JUSTICE SCALIA join, dissenting.</p>
<p>To deprive the prosecution of probative evidence acquired in violation of the law may be a tolerable and necessary cost of the exclusionary rule. Implementation of the rule requires us to draw certain lines to effect its purpose of deterring unlawful conduct. But the line drawn by today's opinion grants the defense side in a criminal case broad immunity to introduce whatever false testimony it can produce from the mouth of a friendly witness. Unless petitioner's conviction is reversed, we are told, police would flout the Fourth Amendment, and as a result, the accused would be unable to offer any defense. This exaggerated view leads to a drastic remedy: The jury cannot learn that defense testimony is inconsistent with probative evidence of undoubted value. A more cautious course is available, one that retains Fourth Amendment protections and yet safeguards the truth-seeking function of the criminal trial.</p>
<p>Our precedents establish that the exclusionary rule does not apply where the interest in pursuing truth or other important values outweighs any deterrence of unlawful conduct that the rule might achieve. See, <i>e. g., </i><i>Illinois</i> v. <i>Krull,</i> <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#347" aria-description="Citation for case: Illinois v. Krull">480 U. S. 340, 347-348</a></span> (1987); <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 906-907</a></span> (1984); <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 486-489</a></span> (1976); <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#347" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 347-348</a></span> (1974). One instance is a defendant's attempt to take advantage by presenting testimony in outright contradiction of excluded <span class="star-pagination">*323</span> facts, secure in the knowledge that the inconsistency will not be revealed to the jury. As we said over 35 years ago:</p>
<blockquote>"It is one thing to say that the Government cannot make an affirmative use of evidence unlawfully obtained. It is quite another to say that the defendant can turn the illegal method by which evidence in the Government's possession was obtained to his own advantage, and provide himself with a shield against contradiction of his untruths. Such an extension of the <i>Weeks</i> [v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914),] doctrine would be a perversion of the Fourth Amendment." <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/#65" aria-description="Citation for case: Walder v. United States">347 U. S. 62, 65</a></span> (1954).</blockquote>
<p>Under this rationale, our consistent rule has been that a defendant's testimony is subject to rebuttal by contradicting evidence that otherwise would be excluded. The principle applies to suppressed physical evidence, as in <i><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span></i> itself and <i>United States</i> v. <i>Havens,</i> <span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/" aria-description="Citation for case: United States v. Havens">446 U. S. 620</a></span> (1980), and to statements obtained in violation of the law, so long as the statements are voluntary and reliable, see <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714</a></span> (1975); <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971).</p>
<p>Petitioner argues that the rationale of these cases is confined to "impeachment" of testimony presented by the defendant himself because these cases involve only "impeachment by self-contradiction." Brief for Petitioner 13. The theory, it seems, is that excluded evidence introduced in opposition to the defendant's testimony impeaches by means of the contradiction itself; the substantive truth or falsity of the suppressed evidence is irrelevant. Our cases do not bear this reading. In <i><span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/" aria-description="Citation for case: United States v. Havens">Havens</a></span>,</i> the defendant was charged as an accomplice in the smuggling of narcotics. A codefendant hid the drugs in a T-shirt constructed with special pockets. The pockets were made of patches cut from another T-shirt found in the defendant's luggage during an illegal search. When the defendant denied having possessed the T-shirts, the cut <span class="star-pagination">*324</span> T-shirt, which had been excluded at the outset, was admitted as rebuttal evidence. We upheld its admission. See <span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#623" aria-description="Citation for case: United States v. Havens">446 U. S., at 623, 628</a></span>. There was no "self-contradiction" involved, for the rebuttal of the defendant's testimony could only have been based on the jury's belief in the substantive truth of the fact that the altered T-shirt was used in the smuggling, and that it belonged to the defendant. The same was true in <i><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span>,</i> where we upheld the admission of illegally seized heroin from an unrelated investigation to impeach the defendant's statement that he had never possessed the drug. In sum, our cases show that introduction of testimony contrary to excluded but reliable evidence subjects the testimony to rebuttal by that evidence.</p>
<p>I agree with the majority that the resolution of this case depends on a balance of values that informs our exclusionary rule jurisprudence. We weigh the " 'likelihood of . . . deterrence against the costs of withholding reliable information from the truth-seeking process.' " <i>Ante,</i> at 312, n. 1 (quoting <i>Illinois</i> v. <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#347" aria-description="Citation for case: Illinois v. Krull"><i>Krull, supra,</i> at 347</a></span>). The majority adopts a sweeping rule that the testimony of witnesses other than the defendant may never be rebutted with excludable evidence. I cannot draw the line where the majority does.</p>
<p>The interest in protecting the truth-seeking function of the criminal trial is every bit as strong in this case as in our earlier cases that allowed rebuttal with evidence that was inadmissible as part of the prosecution's case in chief. Here a witness who knew the accused well took the stand to testify about the accused's personal appearance. The testimony could be expected to create real doubt in the minds of jurors concerning the eyewitness identifications by persons who did not know the accused. To deprive the jurors of knowledge that statements of the defendant himself revealed the witness' testimony to be false would result in a decision by triers of fact who were not just kept in the dark as to excluded evidence, but positively misled. The potential for harm to the truth-seeking process resulting from the majority's new rule <span class="star-pagination">*325</span> in fact will be greater than if the defendant himself had testified. It is natural for jurors to be skeptical of self-serving testimony by the defendant. Testimony by a witness said to be independent has the greater potential to deceive. And if a defense witness can present false testimony with impunity, the jurors may find the rest of the prosecution's case suspect, for ineffective and artificial cross-examination will be viewed as a real weakness in the state's case. Jurors will assume that if the prosecution had any proof the statement was false, it would make the proof known. The majority does more than deprive the prosecution of evidence. The state must also suffer the introduction of false testimony and appear to bolster the falsehood by its own silence.</p>
<p>The majority's fear that allowing the jury to know the whole truth will chill defendants from putting on any defense seems to me far too speculative to justify the rule here announced. No restriction on the defense results if rebuttal of testimony by witnesses other than the defendant is confined to the introduction of excludable evidence that is in direct contradiction of the testimony. If mere "tension with the tainted evidence," <i>ante,</i> at 315, opened the door to introduction of <i>all</i> the evidence subject to suppression, then the majority's fears might be justified. But in this context rebuttal can and should be confined to situations where there is direct conflict, which is to say where, within reason, the witness' testimony and the excluded testimony cannot both be true.<sup>[1]</sup></p>
<p><span class="star-pagination">*326</span> Also missing from the majority's analysis is the almost certain knowledge that the testimony immunized from rebuttal is false. The majority's apparent assumption that defense witnesses protected by today's rule have only truthtelling in mind strikes me as far too sanguine to support acceptance of a rule that controls the hard reality of contested criminal trials. The majority expresses the common sense of the matter in saying that presentation of excluded evidence must sometimes be allowed because it "penalizes defendants for committing perjury." <i>Ante,</i> at 314.</p>
<p>In some cases, of course, false testimony can result from faulty recollection. But the majority's ironclad rule is one that applies regardless of the witness' motives, and may be misused as a license to perjure. Even if the witness testifies in good faith, the defendant and his lawyer, who offer the testimony, know the facts. Indeed, it is difficult here to imagine the defense attorney's reason for asking Henderson about petitioner's hair color if he did not expect her to cast doubt on the eyewitness identification of petitioner by giving a description of petitioner's hair color contrary to that contained in his own (suppressed) statement.</p>
<p>The suggestion that the threat of a perjury prosecution will provide sufficient deterrence to prevent false testimony, <i>ante,</i> <span class="star-pagination">*327</span> at 314 (opinion of BRENNAN, J.); <i>ante,</i> at 320-321 (opinion of STEVENS, J.), is not realistic. See generally <i>Dunn</i> v. <i>United States,</i> <span class="citation" data-id="110090"><a href="/opinion/110090/dunn-v-united-states/#108" aria-description="Citation for case: Dunn v. United States">442 U. S. 100, 108</a></span> (1979) (describing proof of perjury as "exceptionally difficult"). A heightened proof requirement applies in Illinois and other States, making perjury convictions difficult to sustain. See <i>People</i> v. <i>Alkire,</i> <span class="citation" data-id="3420640"><a href="/opinion/3423790/the-people-v-alkire/" aria-description="Citation for case: The People v. Alkire">321 Ill. 28</a></span>, <span class="citation" data-id="3420640"><a href="/opinion/3423790/the-people-v-alkire/" aria-description="Citation for case: The People v. Alkire">151 N. E. 518</a></span> (1926); <i>People</i> v. <i>Harrod,</i> <span class="citation" data-id="2037151"><a href="/opinion/2037151/people-v-harrod/" aria-description="Citation for case: People v. Harrod">140 Ill. App. 3d 96</a></span>, <span class="citation" data-id="2037151"><a href="/opinion/2037151/people-v-harrod/" aria-description="Citation for case: People v. Harrod">488 N. E. 2d 316</a></span> (1986). Where testimony presented on behalf of a friend or family member is involved, the threat that a future jury will convict the witness may be an idle one.</p>
<p>The damage to the truth-seeking process caused by the majority's rule is certain to be great whether the testimony is perjured or merely false. In this case there can be little doubt of the falsity, since petitioner's description of his own hair was at issue. And as a general matter the alternative to rebuttal is endorsement of judicial proceedings conducted in reliance on information known to be untrue. Suppressed evidence is likely to consist of either voluntary statements by the defendant himself or physical evidence. Both have a high degree of reliability, and testimony in direct conflict to such evidence most often will represent an attempt to place falsehoods before the jury.<sup>[2]</sup></p>
<p><span class="star-pagination">*328</span> The suggestion that all this is so far beyond the control of the defendant that he will put on no defense is not supported. As to sympathetic witnesses, such as the family friend here, it should not be too hard to assure the witness does not volunteer testimony in contradiction of the facts. The defendant knows the content of the suppressed evidence. Even in cases where the time for consultation is limited, the defense attorney can take care not to elicit contradicting testimony. And in the case of truly neutral witnesses, or witnesses hostile to the accused, it is hard to see the danger that they will present false testimony for the benefit of the defense.</p>
<p>The majority's concerns may carry greater weight where contradicting testimony is elicited from a defense witness on cross-examination. In that situation there might be a concern that the prosecution would attempt to produce such testimony as the foundation to put excluded evidence before the jury. We have found that possibility insufficient to justify immunity for a defendant's own false testimony on cross-examination. <i>United States</i> v. <i>Havens,</i> <span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/" aria-description="Citation for case: United States v. Havens">446 U. S. 620</a></span> (1980). As to cross-examination of other witnesses, perhaps a different rule could be justified. Rather than wait for an appropriate case to consider this or similar measures, however, the majority opts for a wooden rule immunizing all defense testimony from rebuttal, without regard to knowledge that the testimony introduced at the behest of the defendant is false or perjured.</p>
<p>I also cannot agree that admission of excluded evidence on rebuttal would lead to the "disregard of . . . constitutional rights," by law enforcement officers, <i>ante,</i> at 319, that the majority fears. This argument has been raised in our previous cases in this area of the law. See <span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#633" aria-description="Citation for case: United States v. Havens"><i>Havens, supra,</i> at 633-634</a></span> (BRENNAN, J., dissenting); <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#725" aria-description="Citation for case: Oregon v. Hass">420 U. S., at 725</a></span> (BRENNAN, J., dissenting); <i>Harris,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#232" aria-description="Citation for case: Harris v. New York">401 U. S., at 232</a></span> (BRENNAN, J., dissenting). To date we have rejected it. Now the specter appears premised on an assumption that a single slip of the tongue by any defense witness will open the door to <span class="star-pagination">*329</span> any suppressed evidence at the prosecutor's disposal. If this were so, the majority's concern that officers would be left with little to lose from conducting an illegal search would be understandable. And the argument might hold more force if, as the majority speculates, <i>ante,</i> at 319, police confront the temptation to seize evidence illegally "much if not most of the time" after gathering sufficient evidence to present proof of guilt beyond a reasonable doubt in the case in chief. Again, however, I disagree with the predictions.</p>
<p>It is unrealistic to say that the decision to make an illegal search turns on a precise calculation of the possibilities of rebuttal at some future trial. There is no reason to believe a police officer, unschooled in the law, will assess whether evidence already in his possession would suffice to survive a motion for acquittal following the case in chief. The officer may or may not even know the identity of the ultimate defendant.<sup>[3]</sup> He certainly will not know anything about potential defense witnesses, much less what the content of their testimony might be. What he will know for certain is that evidence from an illegal search or arrest (which may well be crucial to securing a conviction) will be lost to the case in chief. Our earlier assessments of the marginal deterrent effect are applicable here. "Assuming that the exclusionary rule has a deterrent effect on proscribed police conduct, sufficient deterrence flows when the evidence in question is made unavailable <span class="star-pagination">*330</span> to the prosecution in its case in chief." <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#225" aria-description="Citation for case: Harris v. New York"><i>Harris, supra,</i> at 225</a></span>.</p>
<p>In this case, the defense witness, one Jewel Henderson, testified that petitioner's hair was black on the date of the offense. Her statement, perjured or not, should not have been offered to the jurors without giving them the opportunity to consider the unequivocal and contradicting description by the person whose own hair it was. I would allow the introduction of petitioner's statement that his hair was red on the day of the shootings. The result is consistent with our line of cases from <i><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span></i> to <i><span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/" aria-description="Citation for case: United States v. Havens">Havens</a></span></i> and compelled by their reasoning.</p>
<p>The prosecution, it is true, did not limit itself to petitioner's description of his hair color. It went beyond this to introduce petitioner's statement that he went to the beauty shop to "change his appearance." App. 11. The prosecutor used this statement to suggest that petitioner had a guilty mind and an intention to evade capture by disguise. This goes beyond what was necessary to rebut Henderson's testimony and raises many of the concerns expressed in the majority opinion. Nonetheless, there was overwhelming evidence of petitioner's guilt in this case, including the testimony of five eyewitnesses. In view of these circumstances, I agree with the Illinois Supreme Court that any error as to the additional statements or the prosecutor's argument had no effect on petitioner's trial and may be considered harmless.</p>
<p>Where the jury is misled by false testimony, otherwise subject to flat contradiction by evidence illegally seized, the protection of the exclusionary rule is " `perverted into a license to use perjury by way of a defense, free from the risk of confrontation with prior inconsistent utterances.' " <i><span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/" aria-description="Citation for case: United States v. Havens">Havens, supra,</a></span></i> at 626 (quoting <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#226" aria-description="Citation for case: Harris v. New York"><i>Harris, supra,</i> at 226</a></span>). The perversion is the same where the perjury is by proxy. I would affirm the judgment of the Illinois Supreme Court.</p>
<h2>NOTES</h2>
<p>[*]  <i>Solicitor General Starr, Assistant Attorney General Dennis, Deputy Solicitor General Bryson,</i> and <i>Joel Gershowitz</i> filed a brief for the United States as <i>amicus curiae</i> urging affirmance.</p>
<p>[1]  See generally <i>Illinois</i> v. <i>Krull,</i> <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#347" aria-description="Citation for case: Illinois v. Krull">480 U. S. 340, 347</a></span> (1987) (when evaluating proposed exceptions to the exclusionary rule, this Court "has examined whether the rule's deterrent effect will be achieved, and has weighed the likelihood of such deterrence against the costs of withholding reliable information from the truth-seeking process"); <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#908" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 908-913</a></span> (1984) (discussing balancing approach).
</p>
<p>Certain Members of the Court have previously expressed their view that the exclusionary rule is designed not merely to deter police misconduct but also to prevent courts from becoming parties to the constitutional violation by admitting illegally obtained evidence at trial. See <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#931" aria-description="Citation for case: United States v. Leon">468 U. S., at 931-938</a></span> (BRENNAN, J., joined by MARSHALL, J., dissenting); <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#976" aria-description="Citation for case: United States v. Leon"><i>id.,</i> at 976-978</a></span> (STEVENS, J., concurring in judgment in part and dissenting in part).</p>
<p>[2]  See <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966).</p>
<p>[3]  See also <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#721" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714, 721</a></span> (1975) ("[T]rial court instructed the jury that the statements attributed to [defendant] could be used only in passing on his credibility and not as evidence of guilt"); <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#223" aria-description="Citation for case: Harris v. New York">401 U. S. 222, 223</a></span> (1971) (same); <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/#64" aria-description="Citation for case: Walder v. United States">347 U. S. 62, 64</a></span> (1954) (same).</p>
<p>[4]  The dissent concedes, as it must, that "of course, false testimony can result from faulty recollection" as opposed to intentional lying. <i>Post,</i> at 326. Even assuming that Henderson's testimony in this case (as opposed to the detective's contrary testimony) was indeed false, nothing in the record suggests that Henderson intentionally committed perjury rather than honestly provided her best (even if erroneous) perception and recollection of events.</p>
<p>[5]  These reasons to doubt a party's ability to control the testimony of his own witnesses led long ago to abandonment of the common-law rule that a party automatically "vouches for" and hence is inexorably bound by what the witnesses say. See, <i>e. g.,</i> Fed. Rule Evid. 607 ("The credibility of a witness may be attacked by any party, including the party calling him"); see generally 3A J. Wigmore, Evidence § 899, p. 655 (J. Chadbourn rev. 1970) ("[E]very experienced lawyer knows that he is often required to call witnesses who happen to have some knowledge of the facts but whose trustworthiness he could not guarantee. There are also many occasions upon which a lawyer is surprised by the witness testifying in direct contradiction to a prior statement given to the attorney" (citation omitted)); cf. <i>Chambers</i> v. <i>Mississippi,</i> <span class="citation" data-id="9425169"><a href="/opinion/108718/chambers-v-mississippi/" aria-description="Citation for case: Chambers v. Mississippi">410 U. S. 284</a></span> (1973) (state evidentiary rule precluding defendant from impeaching own witness after witness offered incriminating testimony violated due process). See also <i>Imbler</i> v. <i>Pachtman,</i> <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#426" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409, 426</a></span> (1976) (holding prosecutors absolutely immune from damages liability for having knowingly presented perjured witness testimony against criminal defendants, observing that the "veracity of witnesses in criminal cases frequently is subject to doubt before and after they testify . . . . If prosecutors were hampered in exercising their judgment as to the use of such witnesses by concern about resulting personal liability, [they often would refrain from calling such witnesses and hence] the triers of fact in criminal cases often would be denied relevant evidence"); <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#446" aria-description="Citation for case: Imbler v. Pachtman"><i>id.,</i> at 446</a></span> (WHITE, J., concurring in judgment) ("[O]ne of the effects of permitting suits for knowing use of perjured testimony will be detrimental to the [truth-seeking] process  prosecutors may withhold questionable but valuable testimony from the court").</p>
<p>[6]  Apparently to minimize this concern, the Illinois Supreme Court suggested that prosecutors could impeach witnesses only with respect to statements that are "purposely presented by the defendant." <span class="citation" data-id="9741804"><a href="/opinion/2228726/people-v-james/#537" aria-description="Citation for case: People v. James">123 Ill. 2d 523, 537</a></span>, <span class="citation" data-id="9741804"><a href="/opinion/2228726/people-v-james/#729" aria-description="Citation for case: People v. James">528 N. E. 2d 723, 729</a></span> (1988). However, the court did not even purport to determine whether James had "purposely presented" Henderson's testimony that his hair had been black on the day of the shooting, an omission that clearly highlights "the difficulty of determining whether particular testimony elicited from a defense witness was `purposely presented' by the defendant." Brief for United States as <i>Amicus Curiae</i> 21, n. 5. Given the inherent subjectivity of this proposed test, a defendant could hardly be confident that all witness statements that are actually inadvertent or surprising to the defendant will be found to be such by the trial court so as not to open the door to impeachment. This proposed limitation thus would not meaningfully blunt the chill imposed on defendants' presentation of witnesses.
</p>
<p>The Illinois Supreme Court also suggested that prosecutors could be allowed to impeach witnesses only with respect to statements offered on direct examination, perhaps recognizing that defendants likely would feel even more insecure about their witnesses' ability to avoid statements triggering admissibility of suppressed evidence when responding to cross-examination by the prosecutor. We need not decide whether there is a salient distinction between direct and cross-examination in this context, cf. <i>United States</i> v. <i>Havens,</i> <span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/" aria-description="Citation for case: United States v. Havens">446 U. S. 620</a></span> (1980) (rejecting such distinction with respect to defendants' testimony), because even the more limited expansion of the impeachment exception would palpably inhibit defendants' presentation of a defense.</p>
<p>Finally, the dissent embraces the Illinois Supreme Court's suggestion that prosecutors could be allowed to impeach witnesses only when their testimony is in "direct conflict" with the illegally seized evidence. <i>Post,</i> at 325. The dissent suggests that judicial inquiry as to the inconsistency of various statements is "commonplace" under various rules of evidence. <i>Post,</i> at 325, n. 1. But the result of such an inquiry distinguishing between "direct" and "indirect" evidentiary conflicts is far from predictable. Indeed, the authority upon which the dissent relies to define a direct evidentiary conflict observes that "[s]uch is the possible variety of statement that it is often difficult to determine whether this inconsistency exists." 3A Wigmore § 1040, at 1048. The <i>ex ante</i> uncertainty whether a court might find a witness' testimony to pose a "direct" conflict and therefore trigger the impeachment exception likely will chill defendants' presentation of potential witnesses in many cases.</p>
<p>[7]  Brief for United States as <i>Amicus Curiae</i> 18-22.</p>
<p>[8]  Indeed, the detectives who unlawfully detained James and elicited his incriminating statements already knew that there were several eyewitnesses to the shooting. Because the detectives likely believed that the exclusion of any statement they obtained from James probably would not have precluded the prosecution from making a prima facie case, an exclusionary rule applicable only to the prosecution's case in chief likely would have provided little deterrent effect in this case.</p>
<p>[1]  Defining the proper scope of rebuttal is a task that trial judges can be expected to perform without difficulty, for this type of inquiry is a familiar one. In a different context, for example, Federal Rule of Evidence 801(d) (1) provides that a prior statement under oath is not hearsay if "the statement is . . . inconsistent with the declarant's testimony." Likewise, Rule 613(b) contemplates the admission of extrinsic evidence of a "prior inconsistent statement." Trial judges apply these and similar state rules every day, and general formulations of the principles involved are commonplace. For example, the relevant question has been described as whether two statements "cannot at the same time be true . . . . Thus, it is not a mere difference of statement that suffices; nor yet is an absolute oppositeness essential; it is an inconsistency that is required." 3A J. Wigmore, Evidence § 1040 (J. Chadbourn rev. 1970).
</p>
<p>The trial court's handling of the rebuttal in this case provides an illustration. There is no suggestion that the trial court considered witness Jewel Henderson's testimony about petitioner's hair color to be a basis for admitting petitioner's other statements about the shootings. Henderson also testified that she was with petitioner at his home on the night of the shooting, and that petitioner had arrived there between 10 and 11 p.m., but that she could not be specific about the time. The State sought to rebut this testimony with petitioner's suppressed statements about the shooting, contending that Henderson's testimony established an alibi for the shooting, which occurred around 11 p.m. The court concluded that no alibi was established and refused to allow introduction of the suppressed statements on rebuttal. The trial court thus refused to introduce excluded evidence on the basis of mere tension with the witness' statement.</p>
<p>[2]  JUSTICE STEVENS takes exception to the "assumption" that the police officer's recollection of James' statement about his hair was reliable. <i>Ante,</i> at 321. But one need hardly be credulous to so describe the officer's testimony. James, it must be remembered, said his hair was previously red and straight just after he emerged from the dryer with curlers still in his hair. Moreover, in cases involving the suppression of physical evidence, which the majority's rule must also govern, the reliability of the suppressed evidence itself will not be in question since the evidence is not testimonial. In any event, the issue here is not credibility. Perhaps a jury in this case would also find reasons to be skeptical of the rebuttal testimony. My point is that the factfinder should be given the chance to do so. This will not happen under the majority's approach, by which, as I have said, the verdict will be delivered by jurors who have been misled.</p>
<p>[3]  In this case, contrary to the impression conveyed by the majority, <i>ante,</i> at 319, n. 8, the arresting officers knew almost nothing of the state of a future prosecution case. The officers did know there were several eyewitnesses to the shooting. But these eyewitnesses had made no identification of any suspect. The officers did not know petitioner's real name or his true appearance, but had sought him out at the beauty parlor on an anonymous tip. They could not know what physical evidence, such as the murder weapon, they might find on petitioner, or might lose to the case in chief as a result of illegal conduct. The suggestion that the officers' calculated assessment of a future trial allowed them to ignore the exclusionary rule finds no support in the record and, in fact, is pure speculation.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Jimerson v. Lewis.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Jimerson v. Lewis
type: case
citation: "94 F.4th 423 (2024)"
parallel_cite: ""
neutral_cite: ""
court: 5th Cir. 2024
court_level: coa
circuit: ca5
year: 2024
date_decided: 2024-02-15
docket: 22-10441
authority_weight: "Binding in-circuit — 5th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/9475670/jimerson-v-lewis/"
  cluster_id: 9475670
  opinion_id: null
  identity_checked: false
lake:
  record_id: Jimerson v. Lewis
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Qualified Immunity]]"
    role: Key
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Maryland v. Garrison]]"
tags:
  - case
  - fourth-amendment
  - qualified-immunity
  - section-1983
  - search-warrant
  - wrong-house
  - clearly-established-law
holding: "A SWAT commander whose team executed a no-knock warrant at the wrong house was entitled to qualified immunity because, although his efforts to identify the correct residence were deficient, no clearly established law made that failure a Fourth Amendment violation."
---

# Jimerson v. Lewis

*94 F.4th 423 (5th Cir. 2024)* (No. 22-10441) · U.S. Court of Appeals for the Fifth Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 9475670 → lead opinion 9941201 (94 F.4th 423, decided 2024-02-15); Rule quote string-matched to the CL opinion text 2026-07-07. CL text is slip-paginated (no 94 F.4th star pagination), so the pin is slip-style per S2 A3. S9 promotes. -->

## Background
A DEA officer asked Waxahachie SWAT commander Lieutenant Mike Lewis to help execute a nighttime search warrant on a suspected methamphetamine "stash house" at 573 8th Street. Led to the block, the team first assembled at the wrong house; when Lewis looked to a neighboring house he mistakenly identified it as the target, then, realizing that too was wrong, directed the team to yet another house — the Jimersons' home, in the opposite direction from the target. The SWAT team executed a no-knock, forced entry on the Jimersons. They sued Lewis under § 1983; the district court denied him [[Qualified Immunity|qualified immunity]], finding a fact dispute about the reasonableness of his identification efforts.

## Issue
Whether a SWAT commander whose team executed a warrant at the wrong residence is entitled to [[Qualified Immunity|qualified immunity]] where his efforts to identify the correct house were deficient but no clearly established law condemned them.

## Rule
The Fifth Circuit reversed, holding that the material facts were undisputed and the question was one of law: measured against *[[Maryland v. Garrison|Garrison]]*'s reasonable-effort standard, Lewis's conduct did not transgress a clearly established rule. "We conclude that this officer's efforts to identify the correct residence, though deficient, did not violate clearly established law." — slip op. at 1–2. Absent precedent placing the constitutional question "beyond debate," [[Qualified Immunity|qualified immunity]] shields the officer.

## Application
The court accepted that Lewis's identification of the house was objectively deficient but explained that [[Qualified Immunity|qualified immunity]] turns on notice: the plaintiffs pointed to no controlling, factually analogous precedent that would have told a reasonable commander his errors crossed a constitutional line. A nonprecedential decision could not supply clearly established law, and the circuit's cases did not clearly govern this wrong-house raid. Judge Dennis dissented, arguing the undisputed facts showed a violation of clearly established law.

## Conclusion
The denial of [[Qualified Immunity|qualified immunity]] was **reversed** and the case **[[Reading and Citing Cases#on-remand|remanded]] for dismissal**. Southwick, J., wrote for the majority; Dennis, J., dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Jimerson* is a recent, sharply divided illustration of [[Qualified Immunity|qualified immunity]]'s "clearly established law" prong operating in the wrong-house-raid context: even a deficient effort to identify the place to be searched (*[[Maryland v. Garrison|Garrison]]*) does not defeat immunity without precedent squarely on point.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key*

## Sources
- [*Jimerson v. Lewis*, 94 F.4th 423 (5th Cir. 2024)](https://www.courtlistener.com/opinion/9475670/jimerson-v-lewis/) — pinpoint: slip op. at 1–2 (holding on qualified immunity / clearly established law); the CL opinion text carries the slip-opinion page numbers rather than 94 F.4th star pagination, so the pin is slip-style per S2 A3. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "93ccfc4a4ad900e7", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Jimerson v. Lewis"}, "payload": {"all": [{"cite": "94 F.4th 423", "page": "423", "reporter": "F.4th", "selected_official": true, "source": "web-dual-leg", "type": 1, "volume": "94"}], "display": "94 F.4th 423", "official": {"cite": "94 F.4th 423", "page": "423", "reporter": "F.4th", "selected_official": true, "source": "web-dual-leg", "type": 1, "volume": "94"}, "official_selection_present": true, "record_id": "Jimerson v. Lewis"}}
{"assertion_id": "765296912f68f1c4", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Jimerson v. Lewis"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Jimerson v. Lewis", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Jimerson v. Lewis

```json
{
  "schema_version": "s2.v1",
  "record_id": "Jimerson v. Lewis",
  "status": "under_review",
  "identity": {
    "case_name": "Jimerson v. Lewis",
    "case_name_short": "Jimerson",
    "case_name_full": "",
    "input_case_name": "Jimerson v. Lewis",
    "court": "5th Cir. 2024",
    "court_id": "ca5",
    "court_level": "coa",
    "circuit": "ca5",
    "state": null,
    "date_decided": "2024-02-15",
    "year": 2024,
    "docket": "22-10441",
    "cluster_id": 9475670,
    "lead_opinion_id": 9941201,
    "sibling_ids": [],
    "absolute_url": "/opinion/9475670/jimerson-v-lewis/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "94 F.4th 423",
      "volume": "94",
      "reporter": "F.4th",
      "page": "423",
      "type": 1,
      "selected_official": true,
      "source": "web-dual-leg"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "94 F.4th 423",
        "volume": "94",
        "reporter": "F.4th",
        "page": "423",
        "type": 1,
        "selected_official": true,
        "source": "web-dual-leg"
      }
    ],
    "display": "94 F.4th 423",
    "official_selection": {
      "court_class": "coa",
      "selected": "94 F.4th 423",
      "reason": "web-dual-leg"
    },
    "web_legs": [
      {
        "source": "Justia",
        "url": "https://law.justia.com/cases/federal/appellate-courts/ca5/22-10441/22-10441-2024-02-01.html",
        "cite": "94 F.4th 423",
        "checked_date": "2026-07-07"
      },
      {
        "source": "FindLaw",
        "url": "https://caselaw.findlaw.com/court/us-5th-circuit/115835080.html",
        "cite": "94 F.4th 423",
        "checked_date": "2026-07-07"
      }
    ]
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
    "date_created": "2026-07-06T05:45:54Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:46:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:46:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:46:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:46:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "jimerson-v-lewis--9475670",
      "to_record_id": "Jimerson v. Lewis",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Jimerson v. Lewis

```
Case: 22-10441     Document: 00517065342       Page: 1    Date Filed: 02/15/2024




                       REVISED February 15, 2024


           United States Court of Appeals
                for the Fifth Circuit
                               ____________
                                                                  United States Court of Appeals
                                                                           Fifth Circuit
                                 No. 22-10441
                               ____________                              FILED
                                                                   February 1, 2024
   Karen Jimerson; JJ; JJ; XP; JP,                                  Lyle W. Cayce
                                                                         Clerk
                                                         Plaintiffs—Appellees,

                                     versus

   Mike Lewis, Lt,

                                           Defendant—Appellant.
                  ______________________________

                  Appeal from the United States District Court
                      for the Northern District of Texas
                           USDC No. 3:20-CV-2826
                  ______________________________

   Before Stewart, Dennis, and Southwick, Circuit Judges.
   Leslie H. Southwick, Circuit Judge:
         A search warrant showed the correct address for the target house, but
   police officers executed the warrant at an incorrect address. The homeowner
   brought suit against the officers under Section 1983. When denying summary
   judgment on the issue of qualified immunity for the officer who led the
   search, the district court held that fact questions prevented deciding the
   issue. We find no genuine disputes of material fact. The disputed issue is
   one of law. We conclude that this officer’s efforts to identify the correct
Case: 22-10441      Document: 00517065342          Page: 2   Date Filed: 02/15/2024




                                    No. 22-10441


   residence, though deficient, did not violate clearly established law.
   REVERSED and REMANDED for dismissal.
           FACTUAL AND PROCEDURAL BACKGROUND
          In March 2019, at approximately 7:15 p.m., Waxahachie Police
   Department (“WPD”) SWAT Team Commander Mike Lewis received a
   call from a Drug Enforcement Administration (“DEA”) officer. The DEA
   officer needed assistance executing a search warrant that night on a suspected
   methamphetamine “stash” house located at 573 8th Street, Lancaster, Texas
   (“target house”). The officer provided Commander Lewis with information
   about a drug deal involving the target house. Lewis requested further
   information, including pictures of the target house, whether “the location
   was fortified,” whether “it appeared to have surveillance equipment,” and
   whether “there were any exterior indicators on the property that children
   may be present.”      He also “requested identifying information on the
   [methamphetamine] seller, as well as prior law enforcement history at that
   address” involving the Lancaster Police Department (“LPD”).
          In response, Lewis received pictures showing the front of the house
   and was told there was “surveillance established at the location.” DEA
   agents told Lewis that they saw no fortification or surveillance cameras at the
   property or any evidence of children. The agents had no description of the
   people occupying the target house.
          Lewis entered the information into the WPD SWAT’s risk analysis
   assessment worksheet, which scored the incident within the range for
   “optional SWAT deployment.” Consequently, Lewis contacted the WPD
   Chief and received approval to activate the SWAT team. He also gathered
   information on the target house from the Dallas Central Appraisal District
   website, including that the house was 744 square feet, was built in 1952, and
   had a “large, deeply extending backyard.”




                                         2
Case: 22-10441        Document: 00517065342              Page: 3      Date Filed: 02/15/2024




                                         No. 22-10441


           Lewis then briefed SWAT officers at the WPD. The group decided
   to have a six-member team enter the target house and a three-member team
   enter the detached garage and backyard. Thereafter, Lewis received “real-
   time intelligence that surveillance officers at the scene reported a truck
   pulling a white box trailer [had] pulled up in front of the target location.” 1
   When Lewis received a copy of the warrant, he confirmed the address of the
   target house. The officers then finalized their preparations. LPD Officer
   Zachary Beauchamp led the SWAT team to the target house. Beauchamp
   was followed by the SWAT team vehicle, then Lewis in his marked patrol
   unit, then the Waxahachie K9, and then several unmarked DEA vehicles.
   Beauchamp was directed “to stop about a house before the target location,
   so SWAT officers could make an approach on foot.”
           When they arrived at the area, the SWAT team vehicle’s driver saw
   Beauchamp’s vehicle stop abruptly, “causing him to believe [Beauchamp]
   may have driven too far and stopped them too close to the target location.”
   As the officers exited their vehicles, Beauchamp pointed to the house with
   the truck and white trailer in front of it, and officers began their approach. As
   the SWAT team began gathering on the front porch, however, Lewis realized
   that the house did not look like the house from intelligence photos. The
   SWAT team had assembled at 583 8th Street, not at the target house at 573
   8th Street.
           When Lewis looked one house to the left, he decided the layout of the
   front of that house matched the one in the intel photos. Lewis noticed that
   “[f]rom left to right, it had one large window, followed by the front entry
   door, followed by a small window and then [four] larger windows.” He also

           _____________________
           1
             The record indicates that this intelligence was not accurate. Later investigation
   revealed that the white trailer was in front of 583 8th Street — not the target house.




                                               3
Case: 22-10441       Document: 00517065342         Page: 4    Date Filed: 02/15/2024




                                    No. 22-10441


   noticed that “[t]he driveway was . . . on the left side of the property,” and he
   believed numbers on the front of the house read “573,” though the porch
   light obscured his view. This house, it turns out, was also the wrong house.
   The house Lewis identified was 593 8th Street, two doors down from the
   target house.
          Nevertheless, Lewis told the team that they were at the wrong house
   and instructed them to “go to the house just to the left of the house where
   they were.” That house was the home of plaintiffs Karen Jimerson, James
   Parks, and their two young sons and daughter. Officers ran to the front of the
   plaintiffs’ house, deployed a flashbang, broke the front windows, and
   breached the door. The officers began a protective sweep and checked for
   occupants. They “encountered two females” whom they told to get on the
   ground. The officers then encountered an adult male, but before they could
   direct him to get down, SWAT team members yelled “Wrong House!”
          The SWAT team left the plaintiffs’ home and proceeded to the target
   house. After the target house was secured, Lewis returned to the plaintiffs’
   house, where he joined other DEA agents who were already checking on the
   plaintiffs’ welfare. Plaintiff Karen Jimerson reported some pain in her side.
   Lewis called an ambulance and she was taken to the hospital. Lewis also
   coordinated with a glass company to make repairs and remained on the scene
   until 1:30 a.m.
          A WPD internal investigation determined that “reasonable and
   normal protocol was completely overlooked” and the WPD Chief of Police
   stated that these kinds of mistakes should not happen. Lewis was suspended
   for two days without pay.
          In September 2020, the plaintiffs brought this action under 42 U.S.C.
   § 1983. They alleged violations of the Fourth Amendment and several state
   laws against 20 John Doe defendants. They later amended their complaint,




                                          4
Case: 22-10441      Document: 00517065342           Page: 5     Date Filed: 02/15/2024




                                     No. 22-10441


   naming each of the individuals in the WPD SWAT team who executed the
   warrant, including Lewis. Shortly thereafter, the plaintiffs’ state-law tort
   claims were dismissed. The defendants moved for summary judgment based
   on qualified immunity, and the matter was referred to a magistrate judge for
   pretrial management.
          The magistrate judge recommended the district court grant qualified
   immunity to all the officers, whether they entered the house or not. The
   magistrate judge also concluded the plaintiffs failed to show that Lewis did
   not make reasonable efforts to identify the target house.
          The district court agreed with the magistrate judge’s analysis on
   qualified immunity except with respect to whether Lewis made reasonable
   efforts to identify the target house. The court found “a genuine dispute of
   material fact regarding whether [Lewis] made the necessary reasonable effort
   to identify the correct residence and whether his actions were ‘[in]consistent
   with a reasonable effort to ascertain and identify the place intended to be
   searched,’” quoting Maryland v. Garrison, 480 U.S. 79, 88 (1987). The court
   denied Lewis qualified immunity. Lewis timely appealed.
                                  DISCUSSION
          Federal and state officials may be entitled to qualified immunity from
   claims for money damages for their actions. Ashcroft v. al-Kidd, 563 U.S. 731,
   735 (2011). To overcome this defense, a plaintiff needs to plead plausible
   facts “(1) that the official violated a statutory or constitutional right, and (2)
   that the right was ‘clearly established’ at the time of the challenged
   conduct.” Id. (quoting Harlow v. Fitzgerald, 457 U.S. 800, 818 (1982)).
          If the district court denies qualified immunity either on a motion to
   dismiss or on summary judgment, the defendant official may immediately
   appeal under the collateral order doctrine. Behrens v. Pelletier, 516 U.S. 299,
   307 (1996). Here, summary judgment was denied, and our review is de novo.




                                           5
Case: 22-10441      Document: 00517065342           Page: 6     Date Filed: 02/15/2024




                                     No. 22-10441


   Joseph ex rel. Joseph v. Bartlett, 981 F.3d 319, 331 (5th Cir. 2020). Review is
   limited to considering issues of law, including the legal significance of factual
   disputes identified by the district court. Id. at 331. That means “we may
   evaluate whether a factual dispute is material (i.e., legally significant), but we
   may not evaluate whether it is genuine (i.e., exists).”        Id. (emphasis in
   original). “Because the plaintiff is the non-moving party, we construe all
   facts and inferences in the light most favorable to the plaintiff.” Melton, 875
   F.3d at 261.
          As a preliminary matter, Lewis argues the plaintiffs failed to plead and
   argue that his efforts to identify the correct house were unreasonable. A
   plaintiff seeking to overcome qualified immunity “must specifically identify
   each defendant’s personal involvement in the alleged wrongdoing.” Thomas
   v. Humfield, 32 F.3d 566, 1994 WL 442484, at *5 (5th Cir. 1994). The
   plaintiffs complied with the need for specificity by alleging in the complaint
   that Lewis “was the person in charge” of the mistaken raid on their home,
   and in their summary judgment arguments that Lewis was the “overall leader
   of [the] misconduct” and that he overlooked “reasonable and normal
   protocol.”
          As to the merits, Lewis does not challenge the district court’s analysis
   of whether defendants violated the plaintiffs’ rights under federal law. The
   Fourth Amendment provides that individuals have a right “to be secure in
   their persons, houses, papers, and effects, against unreasonable searches and
   seizures.” U.S. CONST. amend. IV. The Supreme Court has held that
   officers must make “reasonable effort[s] to ascertain and identify the place
   intended to be searched” in order to comply with the Fourth Amendment.
   Garrison, 480 U.S. at 88. To be clear about an occasional irrelevant addition
   to the proper analysis, we do not consider whether the officer’s actions were
   “objectively unreasonable.” That quoted standard is a “vestige of older
   caselaw that predates the Supreme Court’s current test.” Parker v. LeBlanc,



                                           6
Case: 22-10441      Document: 00517065342          Page: 7   Date Filed: 02/15/2024




                                    No. 22-10441


   73 F.4th 400, 406 n.1 (5th Cir. 2023). In another precedential rejection of an
   “objectively unreasonable” component of qualified immunity, we held there
   is no “standalone ‘objective reasonableness’ element to the Supreme
   Court’s two-pronged test for qualified immunity.” Baker v. Coburn, 68 F.4th
   240, 251 n.10 (5th Cir. 2023).
          We evaluate the reasonableness of Lewis’s actions because the
   plaintiffs’ claims arise under the Fourth Amendment. The district court
   denied qualified immunity because the court found a “genuine dispute of
   material fact regarding whether [Lewis] made the necessary reasonable
   efforts to identify the correct residence.” As we stated earlier, we cannot
   review a district court’s determination that a factual dispute is genuine.
   Bartlett, 981 F.3d at 331. We are to decide, though, legal significance, i.e.,
   whether disputed facts are material to resolution of the case. Id.
          The district court did not find evidentiary disputes about what Lewis
   and others did before entering the incorrect house. The court stated that the
   central dispute was whether those actions constituted “necessary reasonable
   efforts.” Certainly, unlike here, exactly what an officer did may sometimes
   be factually unclear. A court’s determination of reasonableness under the
   Fourth Amendment, though, “‘is predominantly an objective inquiry.’” al-
   Kidd, 563 U.S. at 736 (quoting City of Indianapolis v. Edmond, 531 U.S. 32, 47
   (2000)).    The circumstances are to be “viewed objectively” and a
   determination made of whether they “justify” the search. Id. (quoting Scott
   v. United States, 436 U.S. 128, 138 (1978)).
          Consequently, as a legal issue for our de novo review, we consider
   whether Lewis’s conduct violated clearly established law. See id. at 325–26.
   Clearly established law is determined by reference to “controlling
   authority[,] or a robust consensus of persuasive authority.” Delaughter v.
   Woodall, 909 F.3d 130, 139 (5th Cir. 2018) (citation omitted). The keystone




                                          7
Case: 22-10441        Document: 00517065342              Page: 8       Date Filed: 02/15/2024




                                          No. 22-10441


   in this analysis is fair warning. Id. at 139–40. To overcome qualified
   immunity, plaintiffs must cite “a body of relevant case law [] in which an
   officer acting under similar circumstances . . . was held to have violated” a
   defendant’s constitutional rights. Bartlett, 981 F.3d at 330 (quotation marks and
   citations omitted). “While there need not be ‘a case directly on point,’ the
   unlawfulness of the challenged conduct must be ‘beyond debate.’” Id.
   (quoting al–Kidd, 563 U.S. at 741).
           Compliance with the Fourth Amendment requires a law enforcement
   officer’s “reasonable effort[s] to ascertain and identify the place intended to
   be searched.” Garrison, 480 U.S. at 88. In applying that general principle,
   the district court relied on two opinions. One was a nonprecedential opinion
   of this court. Rogers v. Hooper, 271 F. App’x 431 (5th Cir. 2008). The other
   was nonprecedential in the Fifth Circuit because it was issued by a different
   circuit court of appeals. Hartsfield v. Lemacks, 50 F.3d 950 (11th Cir.
   1995). 2 The plaintiffs do not cite any other authority.
           In Rogers, we affirmed a grant of qualified immunity. Rogers, 271 F.
   App’x at 436. Officers secured a warrant to search a suspected drug house.
   Id. at 432. Before executing the warrant, officers drove by the target house
   to confirm its location. Id. They saw a maroon vehicle parked in front of the

           _____________________
           2
             A nonprecedential opinion “cannot be the source of clearly established law for
   qualified immunity analysis.” Marks v. Hudson, 933 F.3d 481, 486 (5th Cir. 2019).
   Nevertheless, such opinions may be used to illustrate clearly established law. Bartlett, 981
   F.3d at 341 n.105; see also Cooper v. Brown, 844 F.3d 517, 525 n.8 (5th Cir. 2016). As for
   Hartsfield, “[w]e have not previously identified the level of out-of-circuit consensus
   necessary to put the relevant question ‘beyond debate’” and to constitute clearly
   established law. Morrow v. Meachum, 917 F.3d 870, 879 (5th Cir. 2019) (quoting al-Kidd,
   563 U.S. at 741). It is unlikely that one out-of-circuit case is sufficient.




                                                8
Case: 22-10441      Document: 00517065342            Page: 9   Date Filed: 02/15/2024




                                    No. 22-10441


   target house. Id. The officers then briefed their team on the location of the
   home and developed a plan for executing the warrant. Id. The night of the
   warrant’s execution, however, the maroon vehicle was parked in front of the
   house next door to the target house. Id. Officers broke into that house before
   ultimately realizing their mistake. Id.
          We emphasized that the officers made several efforts to identify the
   correct residence, including conducting “initial surveillance of the house
   shortly before the warrant was executed, though [the officers] increased the
   chance for mistake by approaching the house in the opposite direction than
   they would use later.” Id. at 435. There were differences in appearance
   between the mistaken house and target house, but “those differences were
   less noticeable at night.” Id. Further, we acknowledged the confusion that
   arose from the fact that “a car that earlier had been thought to be in front of
   the house to be searched was instead in front of the [p]laintiffs’ home when
   the search began.” Id. “[T]he officers made reasonable efforts, though
   obviously insufficient ones, to identify the correct house.” Id.
          In Hartsfield, the Eleventh Circuit determined that an officer was not
   entitled to qualified immunity when he executed a warrant at the wrong
   residence. 50 F.3d at 956. The officer had been to the proper residence the
   day before. Id. at 951. On the day of the raid, though, he did little to ensure
   he was leading officers to the correct address:
          As it is uncontroverted that the numbers on the houses are
          clearly marked, and that the raid took place during daylight
          hours, simply checking the warrant would have avoided the
          mistaken entry. Moreover, evidence before the court showed
          that the houses were located on different parts of the street,
          separated by at least one other residence, and that their
          appearances were distinguishable.




                                             9
Case: 22-10441     Document: 00517065342            Page: 10   Date Filed: 02/15/2024




                                     No. 22-10441


   Id. at 955. “[S]earching the wrong residence when [the officer] had done
   nothing to make sure he was searching the house described in the warrant”
   violated clearly established law. Id.
          The dissent argues Hartsfield and Rogers constitute clearly established
   law that distinguishes Lewis’s actions as objectively unreasonable under the
   fair warning analysis. Even if these two nonprecedential opinions were
   indicative of clearly established law, they would not support that Lewis
   violated that law. Lewis erred, but he made significant efforts to identify the
   correct residence. As the district court summarized, Lewis
          (1) reviewed the search warrant; (2) conducted additional
          searches on the target residence through the Dallas Central
          Appraisal District website; (3) ran a computerized criminal
          history search of the occupant of the target residence; (4)
          debriefed with DEA agents twice; (5) was provided with “real-
          time intelligence that surveillance officers at the scene reported
          a truck pulling a white box trailer just pulled up in front of the
          target location and stopped;” and (6) observed the home and
          took note of the front windows, driveway, and the numbers on
          the front of the home in an attempt to confirm the residence as
          being the target location.
   To elaborate on that final point, Lewis was careful to confirm the house had
   the proper arrangement and size of windows, but only later became aware
   that those window features were shared by the plaintiffs’ home. Moreover,
   Lewis’s confusion was compounded by misleading intelligence.                When
   officers arrived, the white trailer was not parked in front of the target house.
   Lewis correctly identified that fact, but then erred in redirecting the officers.
   Lewis was far more careful than the officers in the two opinions cited to us as
   showing he violated clearly established law.
          The “central concern” when evaluating the immunity question “is
   whether the official has fair warning that his conduct violates a constitutional




                                           10
Case: 22-10441     Document: 00517065342           Page: 11   Date Filed: 02/15/2024




                                    No. 22-10441


   right.” Delaughter, 909 F.3d at 140. That means the “dispositive question
   is whether the violative nature of particular conduct is clearly established.”
   Morrow, 917 F.3d at 875 (emphasis in original) (quotation marks and citation
   omitted). Here, the plaintiffs have not cited authority demonstrating that
   Lewis’s conduct violated clearly established law.
          We REVERSE the district court’s denial of summary judgment to
   Lewis and REMAND in order for the district court to dismiss this suit.




                                         11
Case: 22-10441        Document: 00517065342               Page: 12       Date Filed: 02/15/2024




                                          No. 22-10441


   James L. Dennis, Circuit Judge, dissenting:
           I respectfully dissent from the majority opinion. The district court
   properly denied qualified immunity to Lieutenant Mike Lewis, commander
   of the Waxahachie Police Department (WPD) SWAT team. The Jimersons’
   Fourth Amendment claim against Lewis is based on his failure to take
   sufficient steps to ensure that his team executed a no-knock warrant at the
   correct address. The district court found that factual disputes as to the
   reasonableness of Lewis’ efforts to identify the target house precluded
   granting qualified immunity to Lewis. While I agree with the majority’s
   finding that there are no factual disputes as to Lewis’ actions in leading the
   SWAT team to the wrong residence, I disagree that Lewis is entitled to
   qualified immunity 1 under clearly established law.
           Based on the undisputed facts in this case, Lewis failed to use the
   intelligence he received from the Drug Enforcement Administration (DEA)
   that would have easily allowed him to direct the SWAT team to the target
   house. The DEA alerted Lewis that the house number was painted on the
   curb and affixed to a wooden pole on the deck, and that the target house was
   the thirteenth one on the block. Despite having this information, Lewis did
   not even check the number of the house before instructing the SWAT team
   to execute the warrant on the Jimersons’ home—separated from the target

           _____________________
           1
            It’s worth noting that one of our colleagues recently suggested that “the Supreme
   Court’s original justification for qualified immunity—that Congress wouldn’t have
   abrogated common-law immunities absent explicit language—is faulty because the 1871
   Civil Rights Act expressly included such language.” Rogers v. Jarrett, 63 F.4th 971, 980 (5th
   Cir. 2023) (Willett, J., concurring); see also Alexander A. Reinert, Qualified Immunity’s
   Flawed Foundation, 111 CAL. L. REV. 201, 207–08 (2023) (arguing that “the problem with
   current qualified immunity doctrine is not just that it departs from the common law
   immunity that existed when Section 1983 was enacted,” but also that “no qualified
   immunity doctrine at all should apply in Section 1983 actions, if courts stay true to the text
   adopted by the enacting Congress and other evidence of legislative intent”).




                                                12
Case: 22-10441        Document: 00517065342                Page: 13        Date Filed: 02/15/2024




                                           No. 22-10441


   house by more than one 2 residence—by deploying a flash bang, breaking all
   their front windows using the “break and rake” technique, and forcing open
   the front door. Lewis wrote in an incident report that he “believed” the
   numbers on the Jimersons’ home to be that of the target house, despite the
   fact that he admitted his view was obscured because the Jimersons “had a
   brightly glowing porch light directly above them that was causing a reflection
   on the siding of the house.” Regardless of Lewis’ ability to see the numbers
   on the home, the search warrant alerted him that the target house number
   was written on the curb in front of the house and on a wooden pole supporting
   the house—not on the front of the house like at the Jimerson residence. Even
   more glaring are the notable physical distinctions between the two houses:
   while there is a prominent wheelchair ramp that protrudes from the Jimerson
   house with railings that appear to be waist-high, the target house had no such
   ramp and featured a chain-link fence around the perimeter of the property—
   differences evident from the photographs of the target house provided to
   Lewis before the execution of the warrant.
           Though it is undisputed that Lewis violated the Jimersons’ Fourth
   Amendment rights in executing a SWAT-style entry into their home without
   a warrant, the majority finds that the Jimersons’ claim fails because the
   unlawfulness of Lewis’ actions were not clearly established law. 3 Specifically,
           _____________________
           2
            As the majority opinion acknowledges, the SWAT team initially assembled on the
   front porch of the wrong house. After Lewis recognized that the SWAT team was at the
   wrong house, he instructed the SWAT team to execute the warrant on the Jimerson
   residence, which was in the opposite direction of the target residence.
           3
               We have sometimes described the second prong of the qualified immunity
   analysis as an inquiry into whether an official’s “actions were objectively unreasonable in
   light of clearly established law.” See, e.g., Roque v. Harvel, 993 F.3d 325, 334 (5th Cir. 2021)
   (Willett, J.). The different phrasing is of no moment because, of course, violating a clearly
   established right is objectively unreasonable. See Ziglar v. Abbasi, 582 U.S. 120, 151 (2017);
   see also Anderson v. Creighton, 483 U.S. 635, 653 (1987) (“Reliance on the objective
   reasonableness of an official’s conduct, as measured by reference to clearly established




                                                 13
Case: 22-10441        Document: 00517065342              Page: 14       Date Filed: 02/15/2024




                                          No. 22-10441


   the majority concludes that there is not enough legal authority supporting the
   Jimersons’ contention that Lewis’ efforts to locate the target residence were
   constitutionally deficient. While the majority is certainly correct that “[a]
   clearly established right is one that is sufficiently clear that every reasonable
   official would have understood that what he is doing violates that right,”
   Mullenix v. Luna, 577 U.S. 7, 11 (2015), they nonetheless unfairly limit the
   legal authority the Jimersons may rely on in rebutting Lewis’ assertion of
   qualified immunity. The “focus” of the qualified immunity analysis is
   whether the officer had “fair notice” that his conduct was unlawful, and here
   the clearly established law gave Lewis ample warning of the constitutionally
   sufficient efforts required to ensure he directed the SWAT team to the
   correct residence. Brosseau v. Haugen, 543 U.S. 194, 198 (2004) (noting that
   the “focus” of qualified immunity analysis is “whether the officer had fair
   notice that her conduct was unlawful”).
           Contrary to the majority’s assertion that there is no clearly established
   law that would have put Lewis on notice of the unlawfulness of his actions,
   the Supreme Court has stated that officers must make “a reasonable effort to
   ascertain and identify the place intended to be searched within the meaning
   of the Fourth Amendment.” Maryland v. Garrison, 480 U.S. 79, 88 (1987).
   In Garrison, officers mistakenly executed a search warrant on the wrong
   apartment because they believed that the third floor of an apartment complex
   contained only one rather than two apartments. Id. There, the Supreme
   Court found that the officers made a reasonable effort to identify the correct
   apartment because “[t]he objective facts available to the officers at the time
   suggested no distinction between McWebb’s apartment and the third-floor
   premises.” Id. Specifically, those officers made a “reasonable effort” to
           _____________________
   law[.]”); Horvath v. City of Leander, 946 F.3d 787, 800 (5th Cir. 2020) (Ho, J., concurring)
   (quoting Pearson v. Callahan, 555 U.S. 222, 232 (2009)).




                                               14
Case: 22-10441     Document: 00517065342            Page: 15   Date Filed: 02/15/2024




                                     No. 22-10441


   identify the target residence where they: (1) went to the premises to see if it
   matched the description given by an informant; (2) checked with the
   Baltimore Gas and Electric Company to ascertain in whose name the third
   floor apartment was listed; and (3) checked with the Baltimore Police
   Department to make sure that the description and address of the suspect
   matched the information provided by the informant. Id. at 81–82, 85–86 n.10.
          Moreover, Hartsfield v. Lemacks, 50 F.3d 950 (11th Cir. 1995) “aptly
   illustrates the established right” at issue in the Jimersons’ claim against
   Lewis. See id. at 955 (recognizing as “clearly established law” that “absent
   probable cause and exigent circumstances, a warrantless search of a residence
   violates the Fourth Amendment, unless the officers engage in reasonable
   efforts to avoid error”); see also Cooper v. Brown, 844 F.3d 517, 525 (5th Cir.
   2016) (explaining that where a case “does not constitute clearly established
   law for purposes of QI” it may still “aptly illustrates the established right”).
   In Hartsfield, the Eleventh Circuit denied qualified immunity where an
   officer “had the warrant in his possession” yet “did not check to make sure
   he was leading the other officers to the correct address” Hartsfield, 50 F.3d
   at 955. There, the officers’ efforts to identify the target of the search warrant
   were insufficient where: (1) the numbers were clearly marked on the houses;
   (2) the houses were separated by at least one other residence; and (3) the
   houses were physically distinguishable; (4) there were no exigent
   circumstances; and (5) the raid occurred during the daytime. Id. at 952–55.
   Here, similarly, the numbers on the houses were clearly marked (despite it
   being nighttime), the houses were separated by at least one residence and
   were physically distinguishable, and there were no exigent circumstances.
   While Lewis arguably did more to identify the correct residence than the
   officer in Hartsfield, who “did nothing to make sure he was leading the
   officers to the correct residence,” Lewis nonetheless could have easily
   avoided the mistaken entry by “simply checking” the house number or using




                                          15
Case: 22-10441        Document: 00517065342              Page: 16       Date Filed: 02/15/2024




                                          No. 22-10441


   other information at his disposal to identify the correct residence. Id. at 955.
   In light of Hartsfield’s guidance interpreting the clearly established law in
   Garrison, the Jimersons rebutted Lewis’ assertion of qualified immunity.
           Our unpublished decision in Rogers v. Hooper, 271 F. App’x 431 (5th
   Cir. 2008) also supports the denial of qualified immunity to Lewis. In Rogers,
   we affirmed a grant of qualified immunity to an officer who mistakenly led his
   team to the wrong house where: (1) the two houses were next to each other;
   (2) the officer had previously been at the correct house twice; and (3) the
   minor differences between the houses were “less noticeable at night.” Here,
   in contrast, the houses were not next to each other, and Lewis could have
   easily checked the number of the target house that was painted on the curb
   and affixed to a wooden beam supporting the home’s porch. Moreover, the
   obvious physical distinctions between the houses would have been noticeable
   even at night; while the target house had a chain-link fence around it, the
   Jimerson house did not have any fence and featured a wheelchair ramp with
   waist-high railings along it. Because Lewis did not take the same steps 4 as the
   officer in Rogers to identify the correct residence, our nonprecedential case
   law supports the denial of qualified immunity.
           In light of the efforts identified as adequate by the Supreme Court in
   Garrison and elaborated on by circuit courts, Lewis had “fair notice” of the
   minimum efforts required to comply with the Fourth Amendment when
           _____________________
           4
              Notably, the officers in Rogers and Garrison each previously visited the correct
   houses as part of their efforts to identify the target of the search warrant, whereas here
   Lewis made no such attempts. See Rogers, 271 F. App’x at 433–43 (noting that the officers
   “had been at the correct house at least twice before”); Garrison, 480 U.S. at 86 n.10 (“The
   officer went to [the target residence] and found that it matched the description given by the
   informant.”). WPD Police Chief Wade Goolsby even testified that after this incident, the
   WPD implemented additional procedures requiring officers to “get[] eyes on the location
   so that [the officer] not only sees the target, but the surrounding homes” before executing
   a search warrant.




                                                16
Case: 22-10441     Document: 00517065342           Page: 17   Date Filed: 02/15/2024




                                    No. 22-10441


   identifying a house for the purposes of executing a search warrant. Brosseau,
   543 U.S. at 198; see also Hope v. Pelzer, 536 U.S. 730, 731 (2002) (“Qualified
   immunity operates to ensure that before they are subjected to suit, officers
   are on notice that their conduct is unlawful.”). As announced in Garrison and
   elucidated in Rogers and Hartsfield, it is “beyond debate” that Lewis’ efforts
   to identify the target house were constitutionally deficient. Ashcroft v. al–
   Kidd, 563 U.S. 731, 741 (2011). The panel should affirm the district court’s
   denial of Lewis’ assertion of qualified immunity.




                                         17

```

---
