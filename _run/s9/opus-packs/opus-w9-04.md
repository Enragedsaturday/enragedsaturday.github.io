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

## GROUP: _overhaul2/lake/cases/Perry v. New Hampshire.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Perry v. New Hampshire"
type: case
citation: ""
parallel_cite: "181 L. Ed. 2d 694; 132 S. Ct. 716; 565 U.S. 228; 23 Fla. L. Weekly Fed. S 60; 80 U.S.L.W. 4073"
neutral_cite: "2012 U.S. LEXIS 579; 2012 WL 75048"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2012
date_decided: 2012-01-11
docket: 10-8974
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2012-01-11
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Perry v. New Hampshire
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/7350294/perry-v-new-hampshire/"
  cluster_id: 7350294
  opinion_id: 7268276
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Progeny / Refinement"
related: ["[[Manson v. Brathwaite]]", "[[Neil v. Biggers]]", "[[United States v. Wade]]", "[[Gilbert v. California]]"]
aliases: []
tags: ["case", "due-process", "eyewitness-identification", "suggestive-identification", "reliability"]
holding: "The Due Process Clause requires a preliminary judicial screening of eyewitness-identification reliability ONLY when the suggestive…"
lake:
  record_id: Perry v. New Hampshire
  status: verified
  projected_at: 2026-07-06
---

# Perry v. New Hampshire

*565 U.S. 228 (2012)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Around 3 a.m., police responding to a report of a man breaking into cars took a description from a witness, Nubia Blandon, who — pointing out her apartment window — identified Perry, who was then standing in the parking lot beside an officer. The witness later could not pick Perry out of a photo array. Perry moved to suppress the identification as the product of unnecessarily suggestive circumstances, even though the police had not orchestrated the showup-like confrontation.

## Issue
Whether the Due Process Clause requires a preliminary judicial assessment of an eyewitness identification's reliability when the suggestive circumstances were not arranged by law enforcement.

## Rule
No. Pretrial reliability screening applies only to police-arranged suggestion. "We have not extended pretrial screening for reliability to cases in which the suggestive circumstances were not arranged by law enforcement officers. . . . When no improper law enforcement activity is involved, we hold, it suffices to test reliability through the rights and opportunities generally designed for that purpose, notably, the presence of counsel at postindictment lineups, vigorous cross-examination, protective rules of evidence, and jury instructions on both the fallibility of eyewitness identification and the requirement that guilt be proved beyond a reasonable doubt." — 565 U.S. 228 (slip op., at 2). ^pin-op2

"[T]he Due Process Clause does not require a preliminary judicial inquiry into the reliability of an eyewitness identification when the identification was not procured under unnecessarily suggestive circumstances arranged by law enforcement." — *Id.* (slip op., at 18–19). ^pin-op18

## Application
The suggestive circumstance here — the witness spontaneously pointing out her window to Perry as he stood beside an officer — was not arranged by the police; an officer had merely asked her for a description. Because there was no improper police arrangement, no preliminary judicial reliability screening was required, and admitting the identification did not render Perry's trial fundamentally unfair; its reliability was for the jury to weigh after cross-examination and instructions.

## Conclusion
Absent police-arranged suggestion, due process requires no pretrial reliability screening of an eyewitness identification; the New Hampshire Supreme Court's judgment was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Perry* fixes the threshold for the [[Neil v. Biggers]]/[[Manson v. Brathwaite]] reliability inquiry at improper police arrangement.

## Appears on
- [[Eyewitness Identification]] — *Key — Progeny / Refinement*

## Sources
- *Perry v. New Hampshire*, 565 U.S. 228 (2012) — https://www.courtlistener.com/opinion/620671/perry-v-new-hampshire/ — pinpoints: slip op., at 2, 18–19 (CL carries the slip opinion).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "364db54a45d8ea1e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Perry v. New Hampshire"}, "payload": {"all": [{"cite": "181 L. Ed. 2d 694", "page": "694", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "181"}, {"cite": "2012 U.S. LEXIS 579", "page": "579", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2012"}, {"cite": "132 S. Ct. 716", "page": "716", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "132"}, {"cite": "565 U.S. 228", "page": "228", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "565"}, {"cite": "23 Fla. L. Weekly Fed. S 60", "page": "60", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "23"}, {"cite": "80 U.S.L.W. 4073", "page": "4073", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "80"}, {"cite": "2012 WL 75048", "page": "75048", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2012"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Perry v. New Hampshire"}}
{"assertion_id": "0fb66487aa9a5f79", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op18", "record_id": "Perry v. New Hampshire"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op18", "pinpoint_status": "slip-only", "quote": "[T]he Due Process Clause does not require a preliminary judicial inquiry into the reliability of an eyewitness identification when the identification was not procured under unnecessarily suggestive circumstances arranged by law enforcement.", "quote_fidelity": "mismatch", "record_id": "Perry v. New Hampshire", "star_marker": null}}
{"assertion_id": "ac7f0eded418e8c7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op2", "record_id": "Perry v. New Hampshire"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op2", "pinpoint_status": "slip-only", "quote": "--- # Perry v. New Hampshire *565 U.S. 228 (2012)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Around 3 a.m., police responding to a report of a man breaking into cars took a description from a witness, Nubia Blandon, who — pointing out her apartment window — identified Perry, who was then standing in the parking lot beside an officer. The witness later could not pick Perry out of a photo array. Perry moved to suppress the identification as the product of unnecessarily suggestive circumstances, even though the police had not orchestrated the showup-like confrontation. ## Issue Whether the Due Process Clause requires a preliminary judicial assessment of an eyewitness identification's reliability when the suggestive circumstances were not arranged by law enforcement. ## Rule No. Pretrial reliability screening applies only to police-arranged suggestion.", "quote_fidelity": "mismatch", "record_id": "Perry v. New Hampshire", "star_marker": null}}
{"assertion_id": "031d0255e5a60a98", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Perry v. New Hampshire"}, "payload": {"as_of_content": "2012-01-11", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Perry v. New Hampshire", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Perry v. New Hampshire

```json
{
  "schema_version": "s2.v1",
  "record_id": "Perry v. New Hampshire",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Perry v. New Hampshire",
    "case_name_short": "Perry",
    "case_name_full": "BARION PERRY v. NEW HAMPSHIRE",
    "input_case_name": "Perry v. New Hampshire",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2012-01-11",
    "year": 2012,
    "docket": "10-8974",
    "cluster_id": 7350294,
    "lead_opinion_id": 7268276,
    "sibling_ids": [
      7268276,
      7268277,
      7268278
    ],
    "absolute_url": "/opinion/7350294/perry-v-new-hampshire/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 620671,
        "score": 120,
        "case_name": "Perry v. New Hampshire"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "181 L. Ed. 2d 694",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "132 S. Ct. 716",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "716",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "565 U.S. 228",
        "volume": "565",
        "reporter": "U.S.",
        "page": "228",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "23 Fla. L. Weekly Fed. S 60",
        "volume": "23",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "60",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 U.S.L.W. 4073",
        "volume": "80",
        "reporter": "U.S.L.W.",
        "page": "4073",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2012 U.S. LEXIS 579",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "579",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 WL 75048",
        "volume": "2012",
        "reporter": "WL",
        "page": "75048",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "181 L. Ed. 2d 694",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 U.S. LEXIS 579",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "579",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "132 S. Ct. 716",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "716",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "565 U.S. 228",
        "volume": "565",
        "reporter": "U.S.",
        "page": "228",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "23 Fla. L. Weekly Fed. S 60",
        "volume": "23",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "60",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 U.S.L.W. 4073",
        "volume": "80",
        "reporter": "U.S.L.W.",
        "page": "4073",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 WL 75048",
        "volume": "2012",
        "reporter": "WL",
        "page": "75048",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "scotus",
      "selected": null,
      "reason": "unlisted_reporter:Fla. L. Weekly Fed. S"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op2",
      "page": null,
      "quote": "--- # Perry v. New Hampshire *565 U.S. 228 (2012)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Around 3 a.m., police responding to a report of a man breaking into cars took a description from a witness, Nubia Blandon, who \u2014 pointing out her apartment window \u2014 identified Perry, who was then standing in the parking lot beside an officer. The witness later could not pick Perry out of a photo array. Perry moved to suppress the identification as the product of unnecessarily suggestive circumstances, even though the police had not orchestrated the showup-like confrontation. ## Issue Whether the Due Process Clause requires a preliminary judicial assessment of an eyewitness identification's reliability when the suggestive circumstances were not arranged by law enforcement. ## Rule No. Pretrial reliability screening applies only to police-arranged suggestion.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op18",
      "page": null,
      "quote": "[T]he Due Process Clause does not require a preliminary judicial inquiry into the reliability of an eyewitness identification when the identification was not procured under unnecessarily suggestive circumstances arranged by law enforcement.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2012-01-11",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Perry v. New Hampshire",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Dickson",
          "cluster_id": 4244499,
          "cite": [
            "141 A.3d 810",
            "322 Conn. 410",
            "2016 Conn. LEXIS 236"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Shepard-Fraser",
          "cluster_id": 2795991,
          "cite": [
            "784 F.3d 11",
            "97 Fed. R. Serv. 306",
            "2015 U.S. App. LEXIS 6692"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Newman",
          "cluster_id": 2791286,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Balderas v. State",
          "cluster_id": 5448260,
          "cite": [
            "517 S.W.3d 756",
            "2016 WL 6496715",
            "2016 Tex. Crim. App. LEXIS 1329"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Martinez",
          "cluster_id": 9998900,
          "cite": [
            "478 P.3d 880",
            "2021 NMSC 002"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Douglas Stewart v. O'Bell \"Tom\" Winn",
          "cluster_id": 4770981,
          "cite": [
            "967 F.3d 534"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Arizona v. Ronald Bruce Bigger",
          "cluster_id": 4957843,
          "cite": [
            "492 P.3d 1020",
            "251 Ariz. 402"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Espinal-Almeida",
          "cluster_id": 811894,
          "cite": [
            "699 F.3d 588",
            "2012 WL 5511702"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robinson v. Cook",
          "cluster_id": 815781,
          "cite": [
            "706 F.3d 25",
            "2013 U.S. App. LEXIS 1532",
            "2013 WL 238772"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Walden v. David Shinn",
          "cluster_id": 4863579,
          "cite": [
            "990 F.3d 1183"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Samuel Fields v. Scott Jordan",
          "cluster_id": 9437053,
          "cite": [
            "86 F.4th 218"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Arthur",
          "cluster_id": 2720361,
          "cite": [
            "764 F.3d 92",
            "2014 U.S. App. LEXIS 16240",
            "2014 WL 4177373"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Shields",
          "cluster_id": 6478700,
          "cite": [
            "511 P.3d 931"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 805413,
          "cite": [
            "689 F.3d 12",
            "2012 WL 3064841",
            "2012 U.S. App. LEXIS 15631"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. City of Cheyenne",
          "cluster_id": 9497271,
          "cite": [
            "99 F.4th 1206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Aekins",
          "cluster_id": 9373586,
          "cite": [
            "207 N.E.3d 934",
            "2023 Ohio 322"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jeremiah Edwards",
          "cluster_id": 6469003,
          "cite": [
            "34 F.4th 570"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 2700836,
          "cite": [
            "2013 Ohio 756"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jeremiah Farmer",
          "cluster_id": 6619700,
          "cite": [
            "38 F.4th 591"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 4878853,
          "cite": [
            "953 N.W.2d 772",
            "308 Neb. 331"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Matthew R. Davis",
          "cluster_id": 4526287,
          "cite": [
            "2018 ME 116",
            "191 A.3d 1147"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Elijah Vines",
          "cluster_id": 4957586,
          "cite": [
            "9 F.4th 500"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Pope",
          "cluster_id": 4777304,
          "cite": [
            "943 N.W.2d 294",
            "305 Neb. 912"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jonathan Wayne Daniels",
          "cluster_id": 9468693,
          "cite": [
            "91 F.4th 1083"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(7268276 OR 7268277 OR 7268278) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 72,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 72,
        "triage_read": 3,
        "triage_snippet_classified": 69
      },
      "lane2_top_cited": {
        "query": "cites:(7268276 OR 7268277 OR 7268278)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00JnM9MTAxMTg1NTMmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%287268276+OR+7268277+OR+7268278%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(7268276 OR 7268277 OR 7268278)",
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
    "complete_query": "cites:(7268276 OR 7268277 OR 7268278)",
    "indexed_citing_opinions": 88,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 7268276,
        "count": 88,
        "count_source": "search"
      },
      {
        "opinion_id": 7268277,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 7268278,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 847,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/perry-v-new-hampshire.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1NzYzNjgmcz05NDUxOTg5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%287268276+OR+7268277+OR+7268278%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T17:07:49Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:08:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:08:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:11:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:08:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Perry v. New Hampshire

```
<opinion type="majority">
<p id="b802-5">OPINION OF THE COURT</p>
<p id="b802-6">[<span class="citation no-link">565 U.S. 231</span>]</p>
<author id="b802-7">Justice Ginsburg</author>
<p id="Augc">delivered the opinion of the Court.</p>
<p id="b802-8">In our system of justice, fair trial for persons charged with criminal offenses is secured by the Sixth Amendment, which</p>
<p id="b802-9">[<span class="citation no-link">565 U.S. 232</span>]</p>
<p id="b802-10">guarantees to defendants the right to counsel, compulsory process to obtain defense witnesses, and the opportunity to cross-examine witnesses for the prosecution. Those safeguards apart, admission of evidence in state trials is ordinarily governed by state law, and the reliability of relevant testimony typically falls within the province of the jury to determine. This Court has recognized, in addition, a due process check on the admission of eyewitness identification, applicable when the police have arranged suggestive circumstances leading the witness to identify a particular person as the perpetrator of a crime.</p>
<p id="b802-16">An identification infected by improper police influence, our case law holds, is not automatically excluded. Instead, the trial judge must screen the evidence for reliability pretrial. If there is “a very substantial likelihood of irreparable misidentification,” <em>Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U.S. 377, 384</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">88 S. Ct. 967</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">19 L. Ed. 2d 1247</a></span> (1968), the judge must disallow presentation of the evidence at trial. But if the indicia of reliability are strong enough to outweigh the corrupting <page-number citation-index="1" label="703">*703</page-number>effect of the police-arranged suggestive circumstances, the identification evidence ordinarily will be admitted, and the jury will ultimately determine its worth.</p>
<p id="b803-4">We have not extended pretrial screening for reliability to cases in which the suggestive circumstances were not arranged by law enforcement officers. Petitioner requests that we do so because of the grave risk that mistaken identification will yield a miscarriage of justice.<footnotemark>1</footnotemark> Our decisions,</p>
<p id="ANlU">[<span class="citation no-link">565 U.S. 233</span>]</p>
<p id="b803-5">however, turn on the presence of state action and aim to deter police from rigging identification procedures, for example, at a lineup, showup, or photograph array. When no improper law enforcement activity is involved, we hold, it suffices to test reliability through the rights and opportunities generally designed for that purpose, notably, the presence of counsel at postindictment lineups, vigorous cross-examination, protective rules of evidence, and jury instructions on both the fallibility of eyewitness identification and the requirement that guilt be proved beyond a reasonable doubt.</p>
<p id="b803-6">I</p>
<p id="b803-7">A</p>
<p id="b803-8">Around 3 a.m. on August 15, 2008, Joffre Ullon called the Nashua, New Hampshire, Police Department and reported that an African-American male was trying to break into cars parked in the lot of Ullon’s apartment building. Officer Nicole Clay responded to the call. Upon arriving at the parking lot, Clay heard what “sounded like a metal bat hitting the ground.” App. 37a-38a. She then saw petitioner Barion Perry standing between two cars. Perry walked toward Clay, holding two car-stereo amplifiers in his hands. A metal bat lay on the ground behind him. Clay asked Perry where the amplifiers came from. “[I] found them on the ground,” Perry responded. <span class="citation no-link">Id.,</span> at 39a.</p>
<p id="b803-10">Meanwhile, Ullon’s wife, Nubia Blandón, woke her neighbor, Alex Clavijo, and told him she had just seen someone break into his car. Clavijo immediately went downstairs to the parking lot to inspect the car. He first observed that one of the rear windows had been shattered. On further inspection, he discovered that the speakers and amplifiers from his car stereo were missing, as were his bat and</p>
<p id="b803-11">[<span class="citation no-link">565 U.S. 234</span>]</p>
<p id="b803-12">wrench. Clavijo then approached Clay and told her about Blandon’s alert and his own subsequent observations.</p>
<p id="b803-13">By this time, another officer had arrived at the scene. Clay asked Perry to stay in the parking lot with that officer, while she and Clavijo went to talk to Blandón. Clay and Clavijo then entered the apartment building and took the stairs to the fourth floor, where Blandon’s and Clavijo’s apart<page-number citation-index="1" label="704">*704</page-number>ments were located. They met Blan-dón in the hallway just outside the open door to her apartment.</p>
<p id="b804-4">Asked to describe what she had seen, Blandón stated that, around 2:30 a.m., she saw from her kitchen window a tall, African-American man roaming the parking lot and looking into cars. Eventually, the man circled Clavijo’s car, opened the trunk, and removed a large box.<footnotemark>2</footnotemark></p>
<p id="b804-5">Clay asked Blandón for a more specific description of the man. Blandón pointed to her kitchen window and said the person she saw breaking into Clavijo’s car was standing in the parking lot, next to the police officer. Perry’s arrest followed this identification.</p>
<p id="b804-6">About a month later, the police showed Blandón a photographic array that included a picture of Perry and asked her to point out the man who had broken into Clavijo’s car. Blandón was unable to identify Perry.</p>
<p id="b804-7">B</p>
<p id="b804-8">Perry was charged in New Hampshire state court with one count of theft by unauthorized taking and one count of criminal mischief.<footnotemark>3</footnotemark> Before trial, he moved to suppress Blandon’s identification on the ground that admitting it at trial would violate due process. Blandón witnessed what</p>
<p id="Ap5qT">[<span class="citation no-link">565 U.S. 235</span>]</p>
<p id="b804-9">amounted to a one-person showup in the parking lot, Perry asserted, which all but guaranteed that she would identify him as the culprit. <em><span class="citation no-link">Id.,</span> </em>at 15a-16a.</p>
<p id="b804-10">The New Hampshire Superior Court denied the motion. <em><span class="citation no-link">Id.,</span> </em>at 82a-88a. To determine whether due process prohibits the introduction of an out-of-court identification at trial, the Superior Court said, this Court’s decisions instruct a two-step inquiry. First, the trial court must decide whether the police used an unnecessarily suggestive identification procedure. <em><span class="citation no-link">Id.,</span> </em>at 85a. If they did, the court must next consider whether the improper identification procedure so tainted the resulting identification as to render it unreliable and therefore inadmissible. <em><span class="citation no-link">Ibid.</span> </em>(citing <em>Neil </em>v. <em>Biggers, </em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">409 U.S. 188</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">93 S. Ct. 375</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">34 L. Ed. 2d 401</a></span> (1972), and <em>Manson </em>v. <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">432 U.S. 98</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span> (1977)).</p>
<p id="b804-12">Perry’s challenge, the Superior Court concluded, failed at step one: Blandon’s identification of Perry on the night of the crime did not result from an unnecessarily suggestive procedure “manufacture [d] ... by the police.” App. 86a-87a. Blandón pointed to Perry “spontaneously,” the court noted, “without any inducement from the police.” <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Id.,</a></span> </em>at 85a-86a. Clay did not ask Blandón whether the man standing in the parking lot was the man Blandón had seen breaking into Clavijo’s car. <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Ibid.</a></span> </em>Nor did Clay ask Blandón to move to the window from which she had observed the break-in. <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Id.,</a></span> </em>at 86a.</p>
<p id="b804-13">The Superior Court recognized that there were reasons to question the accuracy of Blandon’s identification: The parking lot was dark in some locations; Perry was standing next to a police officer; Perry was the only African American man in the vicinity; and Blandón was unable, later, to pick <page-number citation-index="1" label="705">*705</page-number>Perry out of a photographic array. <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Id.,</a></span> </em>at 86a-87a. But “[b]ecause the police procedures were not unnecessarily suggestive,” the court ruled that the reliability of Blandon’s testimony was for the jury to consider. <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Id.,</a></span> </em>at 87a.</p>
<p id="b805-4">[<span class="citation no-link">565 U.S. 236</span>]</p>
<p id="b805-5">At the ensuing trial, Blandón and Clay testified to Blandon’s out-of-court identification. The jury found Perry guilty of theft and not guilty of criminal mischief.</p>
<p id="b805-6">On appeal, Perry repeated his challenge to the admissibility of Blandon’s out-of-court identification. The trial court erred, Perry contended, in requiring an initial showing that the police arranged the suggestive identification procedure. Suggestive circumstances alone, Perry argued, suffice to trigger the court’s duty to evaluate the reliability of the resulting identification before allowing presentation of the evidence to the jury.</p>
<p id="b805-7">The New Hampshire Supreme Court rejected Perry’s argument and affirmed his conviction. <em><span class="citation no-link">Id.,</span> </em>at 9a-11a. Only where the police employ suggestive identification techniques, that court held, does the Due Process Clause require a trial court to assess the reliability of identification evidence before permitting a jury to consider it. <em><span class="citation no-link">Id.,</span> </em>at 10a-11a.</p>
<p id="b805-8">We granted certiorari to resolve a division of opinion on the question whether the Due Process Clause requires a trial judge to conduct a preliminary assessment of the reliability of an eyewitness identification made under suggestive circumstances not arranged by the police. <span class="citation multiple-matches"><a href="/c/U.S./563/1020/">563 U.S. 1020</a></span>, <span class="citation multiple-matches"><a href="/c/S.%20Ct./131/2932/">131 S. Ct. 2932</a></span>, <span class="citation multiple-matches"><a href="/c/L.%20Ed.%202d/180/224/">180 L. Ed. 2d 224</a></span> (2011).<footnotemark>4</footnotemark></p>
<p id="b805-10">[<span class="citation no-link">565 U.S. 237</span>]</p>
<p id="b805-11">II</p>
<p id="b805-12">A</p>
<p id="b805-13">The Constitution, our decisions indicate, protects a defendant against a conviction based on evidence of questionable reliability, not by prohibiting introduction of the evidence, but by affording the defendant means to persuade the jury that the evidence should be discounted as unworthy of credit. Constitutional safeguards available to defendants to counter the State’s evidence include the Sixth Amendment rights to counsel, <em>Gideon </em>v. <em>Wainwright, </em><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/#343" aria-description="Citation for case: Gideon v. Wainwright">372 U.S. 335, 343-345</a></span>, <span class="citation" data-id="106545"><a href="/opinion/106545/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">83 S. Ct. 792</a></span>, <span class="citation" data-id="106545"><a href="/opinion/106545/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">9 L. Ed. 2d 799</a></span> (1963); compulsory process, <em>Taylor </em>v. <em>Illinois, </em><span class="citation" data-id="9431168"><a href="/opinion/111986/taylor-v-illinois/#408" aria-description="Citation for case: Taylor v. Illinois">484 U.S. 400, 408-409</a></span>, <span class="citation" data-id="9431168"><a href="/opinion/111986/taylor-v-illinois/" aria-description="Citation for case: Taylor v. Illinois">108 S. Ct. 646</a></span>, <span class="citation" data-id="9431168"><a href="/opinion/111986/taylor-v-illinois/" aria-description="Citation for case: Taylor v. Illinois">98 L. Ed. 2d 798</a></span> (1988); and confrontation plus cross-examination of witnesses, <em>Delaware </em>v. <em>Fensterer, </em><span class="citation" data-id="9430219"><a href="/opinion/111535/delaware-v-fensterer/#18" aria-description="Citation for case: Delaware v. Fensterer">474 U.S. 15, 18-20</a></span>, <span class="citation" data-id="9430219"><a href="/opinion/111535/delaware-v-fensterer/" aria-description="Citation for case: Delaware v. Fensterer">106 S. Ct. 292</a></span>, <span class="citation" data-id="9430219"><a href="/opinion/111535/delaware-v-fensterer/" aria-description="Citation for case: Delaware v. Fensterer">88 L. Ed. 2d 15</a></span> (1985) <em>(per curiam). </em>Apart from these guarantees, we have recognized, state and federal statutes and rules ordinarily govern the admissibility of evidence, and juries are assigned the task of determining the reliability of the evidence presented <page-number citation-index="1" label="706">*706</page-number>at trial. See <em>Kansas </em>v. <em>Ventris, </em><span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/#594" aria-description="Citation for case: Kansas v. Ventris">556 U.S. 586, 594</a></span>, n., <span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/" aria-description="Citation for case: Kansas v. Ventris">129 S. Ct. 1841</a></span>, <span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/" aria-description="Citation for case: Kansas v. Ventris">173 L. Ed. 2d 801</a></span> (2009) (“Our legal system ... is built on the premise that it is the province of the jury to weigh the credibility of competing witnesses.”). Only when evidence “is so extremely unfair that its admission violates fundamental conceptions of justice,” <em>Dowling </em>v. <em>United States, </em><span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/#352" aria-description="Citation for case: Dowling v. United States">493 U.S. 342, 352</a></span>, <span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/" aria-description="Citation for case: Dowling v. United States">110 S. Ct. 668</a></span>, <span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/" aria-description="Citation for case: Dowling v. United States">107 L. Ed. 2d 708</a></span> (1990) (internal quotation marks omitted), have we imposed a constraint tied to the Due Process Clause. See, <em>e.g., Napue </em>v. <em>Illinois, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois">360 U.S. 264, 269</a></span>, <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">79 S. Ct. 1173</a></span>, <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">3 L. Ed. 2d 1217</a></span> (1959) (Due process prohibits the State’s “knowin[g] use [of] false evidence,” because such use violates “any concept of ordered liberty.”).</p>
<p id="b806-4">Contending that the Due Process Clause is implicated here, Perry relies on a series of decisions involving police-arranged identification procedures. In <em>Stovall </em>v. <em>Denno, </em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U.S. 293</a></span>, <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">87 S. Ct. 1967</a></span>, <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">18 L. Ed. 2d 1199</a></span> (1967), first of those decisions, a witness identified the defendant as her assailant after police officers brought</p>
<p id="A7GA8">[<span class="citation no-link">565 U.S. 238</span>]</p>
<p id="b806-5">the defendant to the witness’ hospital room. <span class="citation no-link"><em>Id., </em>at 295</span>, <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">87 S. Ct. 1967</a></span>, <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">18 L. Ed. 2d 1199</a></span>. At the time the witness made the identification, the defendant—the only African-American in the room—was handcuffed and surrounded by police officers. <em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Ibid.</a></span> </em>Although the police-arranged showup was undeniably suggestive, the Court held that no due process violation occurred. <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#302" aria-description="Citation for case: Stovall v. Denno"><em>Id., </em>at 302</a></span>, <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">87 S. Ct. 1967</a></span>, <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">18 L. Ed. 2d 1199</a></span>. Crucial to the Court’s decision was the procedure’s necessity: The witness was the only person who could identify or exonerate the defendant; the witness could not leave her hospital room; and it was uncertain whether she would live to identify the defendant in more neutral circumstances. <em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Ibid.</a></span></em></p>
<p id="b806-7">A year later, in <em>Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U.S. 377</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">88 S. Ct. 967</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">19 L. Ed. 2d 1247</a></span> (1968), the Court addressed a due process challenge to police use of a photographic array. When a witness identifies the defendant in a police-organized photo lineup, the Court ruled, the identification should be suppressed only where “the photographic identification procedure was so [unnecessarily] suggestive as to give rise to a very substantial likelihood of irreparable misidentification.” <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States"><em>Id., </em>at 384-385</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">88 S. Ct. 967</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">19 L. Ed. 2d 1247</a></span>. Satisfied that the photo array used by Federal Bureau of Investigation agents in <em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span> </em>was both necessary and unlikely to have led to a mistaken identification, the Court rejected the defendant’s due process challenge to admission of the identification. <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#385" aria-description="Citation for case: Simmons v. United States"><em>Id., </em>at 385-386</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">88 S. Ct. 967</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">19 L. Ed. 2d 1247</a></span>. In contrast,  the Court held in <em>Foster </em>v. <em>California, </em><span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">394 U.S. 440</a></span>, <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">89 S. Ct. 1127</a></span>, <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">22 L. Ed. 2d 402</a></span> (1969), that due process required the exclusion of an eyewitness identification obtained through police-arranged procedures that “made it all but inevitable that [the witness] would identify [the defendant].” <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/#443" aria-description="Citation for case: Foster v. California"><em>Id., </em>at 443</a></span>, <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">89 S. Ct. 1127</a></span>, <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">22 L. Ed. 2d 402</a></span>.</p>
<p id="b806-8">Synthesizing previous decisions,  we set forth in <em>Neil </em>v. <em>Biggers, </em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">409 U.S. 188</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">93 S. Ct. 375</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">34 L. Ed. 2d 401</a></span> (1972), and reiterated in <em>Manson </em>v. <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">432 U.S. 98</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span> (1977), the approach appropriately used to determine whether the Due Process Clause requires suppression of an eyewitness identification tainted by police arrangement. The Court emphasized, first, that due process concerns arise only when law enforcement officers <page-number citation-index="1" label="707">*707</page-number>use an</p>
<p id="b807-4">[<span class="citation no-link">565 U.S. 239</span>]</p>
<p id="b807-5">identification procedure that is both suggestive and unnecessary. <em>Id., </em>at 107, 109, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>; <em>Biggers, </em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#198" aria-description="Citation for case: Neil v. Biggers">409 U.S., at 198</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">93 S. Ct. 375</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">34 L. Ed. 2d 401</a></span>. Even when the police use such a procedure, the Court next said, suppression of the resulting identification is not the inevitable consequence. <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#112" aria-description="Citation for case: Manson v. Brathwaite">432 U.S., at 112-113</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>; <em>Biggers, </em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#198" aria-description="Citation for case: Neil v. Biggers">409 U.S., at 198-199</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">93 S. Ct. 375</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">34 L. Ed. 2d 401</a></span>.</p>
<p id="b807-6">A rule requiring automatic exclusion, the Court reasoned, would “g[o] too far,” for it would “kee[p] evidence from the jury that is reliable and relevant,” and “may result, on occasion, in the guilty going free.” <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#112" aria-description="Citation for case: Manson v. Brathwaite">432 U.S., at 112</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>; see <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#113" aria-description="Citation for case: Manson v. Brathwaite"><em>id., </em>at 113</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span> (when an “identification is reliable despite an unnecessarily suggestive [police] identification procedure,” automatic exclusion “is a Draconian sanction,” one “that may frustrate rather than promote justice”).</p>
<p id="b807-7">Instead of mandating a <em>per se </em>exclusionary rule, the Court held that the Due Process Clause requires courts to assess, on a case-by-case basis, whether improper police conduct created a “substantial likelihood of misidentification.” <em>Biggers, </em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#201" aria-description="Citation for case: Neil v. Biggers">409 U.S., at 201</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">93 S. Ct. 375</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">34 L. Ed. 2d 401</a></span>; see <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#116" aria-description="Citation for case: Manson v. Brathwaite">432 U.S., at 116</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>. “[R]eliability [of the eyewitness identification] is the linchpin” of that evaluation, the Court stated in <em>Brathwaite. Id., </em>at 114, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>. Where the “indicators of [a witness’] ability to make an accurate identification” are “outweighed by the corrupting effect” of law enforcement suggestion, the identification should be suppressed. <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#114" aria-description="Citation for case: Manson v. Brathwaite"><em>Id., </em>at 114, 116</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>. Otherwise, the evidence (if admissible in all other respects) should be submitted to the jury.<footnotemark>5</footnotemark></p>
<p id="b807-9">Applying this “totality of the circumstances” approach, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#110" aria-description="Citation for case: Manson v. Brathwaite"><em>id., </em>at 110</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>, the Court held in <em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span> </em>that law enforcement’s use</p>
<p id="b807-10">[<span class="citation no-link">565 U.S. 240</span>]</p>
<p id="b807-11">of an unnecessarily suggestive showup did not require suppression of the victim’s identification of her assailant. <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#199" aria-description="Citation for case: Neil v. Biggers">409 U.S., at 199-200</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">93 S. Ct. 375</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">34 L. Ed. 2d 401</a></span>. Notwithstanding the improper procedure, the victim’s identification was reliable: She saw her assailant for a considerable period of time under adequate light, provided police with a detailed description of her attacker long before the showup, and had “no doubt” that the defendant was the person she had seen. <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#200" aria-description="Citation for case: Neil v. Biggers"><em>Id., </em>at 200</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">93 S. Ct. 375</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">34 L. Ed. 2d 401</a></span> (internal quotation marks omitted). Similarly, the Court concluded in <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Brathwaite</a></span> </em>that police use of an unnecessarily suggestive photo array did not require exclusion of the resulting identification. <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#114" aria-description="Citation for case: Manson v. Brathwaite">432 U.S., at 114-117</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>. The witness, an undercover police officer, viewed the defendant in good light for several minutes, provided a thorough description of the suspect, and was certain of his identification. <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#115" aria-description="Citation for case: Manson v. Brathwaite"><em>Id., </em>at 115</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d <page-number citation-index="1" label="708">*708</page-number>140</a></span>. Hence, the “indicators of [the witness’] ability to make an accurate identification [were] hardly outweighed by the corrupting effect of the challenged identification.” <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#116" aria-description="Citation for case: Manson v. Brathwaite"><em>Id., </em>at 116</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>.</p>
<p id="b808-4">B</p>
<p id="b808-5">Perry concedes that, in contrast to every case in the <em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span> </em>line, law enforcement officials did not arrange the suggestive circumstances surrounding Blandon’s identification. See Brief for Petitioner 34; Tr. of Oral Arg. 5 (counsel for Perry) (“[W]e do not allege any manipulation or intentional orchestration by the police.”). He contends, however, that it was mere happenstance that each of the <em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span> </em>cases involved improper police action. The rationale underlying our decisions, Perry asserts, supports a rule requiring trial judges to pre-screen eyewitness evidence for reliability any time an identification is made under suggestive circumstances. We disagree.</p>
<p id="b808-6">Perry’s argument depends, in large part, on the Court’s statement in <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Brathwaite</a></span> </em>that “reliability is the linchpin in determining the admissibility of identification testimony.” <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#114" aria-description="Citation for case: Manson v. Brathwaite">432 U.S., at 114</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>. If reliability is the linchpin of admissibility</p>
<p id="b808-7">[<span class="citation no-link">565 U.S. 241</span>]</p>
<p id="ATboI">under the Due Process Clause, Perry maintains, it should make no difference whether law enforcement was responsible for creating the suggestive circumstances that marred the identification.</p>
<p id="b808-8">Perry has removed our statement in <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Brathwaite</a></span> </em>from its mooring, and thereby attributes to the statement a meaning a fair reading of our opinion does not bear. As just explained, <em>supra, </em>at 238-239, 181 L. Ed. 2d, at 706-707,  the <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Brathwaite</a></span> </em>Court’s reference to reliability appears in a portion of the opinion concerning the appropriate remedy <em>when the police use an unnecessarily suggestive identification procedure. </em>The Court adopted a judicial screen for reliability as a course preferable to a <em>per se </em>rule requiring exclusion of identification evidence whenever law enforcement officers employ an improper procedure. The due process check for reliability, <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Brathwaite</a></span> </em>made plain, comes into play only after the defendant establishes improper police conduct. The very purpose of the check, the Court noted, was to avoid depriving the jury of identification evidence that is reliable, <em>notwithstanding </em>improper police conduct. <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#112" aria-description="Citation for case: Manson v. Brathwaite">432 U.S., at 112-113</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>.<footnotemark>6</footnotemark></p>
<p id="b808-10">Perry’s contention that improper police action was not essential to the reliability check <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Brathwaite</a></span> </em>required is echoed by the dissent. <em>Post, </em>at 252, 181 L. Ed. 2d, at 715. Both ignore  a key premise of the <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Brathwaite</a></span> </em>decision: A primary aim of excluding identification evidence obtained under unnecessarily suggestive circumstances, the Court said, is to deter law enforcement use of improper lineups, showups, and photo arrays in the first place. See <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#112" aria-description="Citation for case: Manson v. Brathwaite">432 U.S., at 112</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>. Alerted to the prospect that identification evidence improperly obtained may be excluded, the Court reasoned, police officers will “guard <page-number citation-index="1" label="709">*709</page-number>against unnecessarily suggestive procedures.” <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Ibid.</a></span> </em>This deterrence rationale is inapposite in cases, like Perry’s, in which the police engaged in no improper conduct.</p>
<p id="b809-5"><em>Coleman </em>v. <em>Alabama, </em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U.S. 1</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">90 S. Ct. 1999</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">26 L. Ed. 2d 387</a></span> (1970), another decision in the <em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span> </em>line, similarly shows that the Court has linked the due process check, not to suspicion of eyewitness testimony generally, but only to improper police arrangement of the circumstances surrounding an identification. The defendants in <em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">Coleman</a></span> </em>contended that a witness’ in-court identifications violated due process, because a pretrial stationhouse lineup was “so unduly prejudicial and conducive to irreparable misidentification as fatally to taint [the later identifications].” <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#3" aria-description="Citation for case: Coleman v. Alabama">399 U.S., at 3</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">90 S. Ct. 1999</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">26 L. Ed. 2d 387</a></span> (plurality opinion). The Court rejected this argument. <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#5" aria-description="Citation for case: Coleman v. Alabama"><em>Id., </em>at 5-6</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">90 S. Ct. 1999</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">26 L. Ed. 2d 387</a></span> (plurality opinion), 13-14, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">90 S. Ct. 1999</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">26 L. Ed. 2d 387</a></span> (Black, J., concurring), 22, n. 2, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">90 S. Ct. 1999</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">26 L. Ed. 2d 387</a></span> (Burger, C. J., dissenting), 28, n. 2, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">90 S. Ct. 1999</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">26 L. Ed. 2d 387</a></span> (Stewart, J., dissenting). No due process violation occurred, the plurality explained, because nothing “the police said or did prompted [the witness’] virtually spontaneous identification of [the defendants].” <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#6" aria-description="Citation for case: Coleman v. Alabama"><em>Id., </em>at 6</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">90 S. Ct. 1999</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">26 L. Ed. 2d 387</a></span>. True, Coleman was the only person in the lineup wearing a hat, the plurality noted, but “nothing in the record show[ed] that he was required to do so.” <em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">Ibid.</a></span> See </em>also <em>Colorado </em>v. <em>Connelly, </em><span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/#163" aria-description="Citation for case: Colorado v. Connelly">479 U.S. 157, 163, 167</a></span>, <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/" aria-description="Citation for case: Colorado v. Connelly">107 S. Ct. 515</a></span>, <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/" aria-description="Citation for case: Colorado v. Connelly">93 L. Ed. 2d 473</a></span> (1986) (Where the “crucial element of police overreaching” is missing, the admissibility of an allegedly unreliable confession is “a matter to be governed by the evidentiary laws of the forum, . . . and not by the Due Process Clause.”).</p>
<p id="b809-9">Perry and the dissent place significant weight on <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U.S. 218</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">87 S. Ct. 1926</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">18 L. Ed. 2d 1149</a></span> (1967), describing it as a decision not anchored to improper police conduct. See Brief for Petitioner 12, 15, 21-22, 28; <em>post, </em>at 250-253, 256-258, 181 L. Ed. 2d, at 714-716, 718-719. In fact,  the risk of police rigging was the very danger to which the Court responded in <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>when it recognized a defendant’s right to counsel at postindictment, police-organized identification procedures. 388 U.S., at 233, 235-236, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">87 S. Ct. 1926</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">18 L. Ed. 2d 1149</a></span>. “[T]he confrontation <em>compelled by the State </em>between the accused and the</p>
<p id="A0bn">[<span class="citation no-link">565 U.S. 243</span>]</p>
<p id="b809-10">victim or witnesses,” the Court began, “is peculiarly riddled with innumerable dangers and variable factors which might seriously, even crucially, derogate from a fair trial.” <em>Id., </em>at 228, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">87 S. Ct. 1926</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">18 L. Ed. 2d 1149</a></span> (emphasis added). “A major factor contributing to the high incidence of miscarriage of justice from mistaken identification,” the Court continued, “has been the degree of suggestion inherent in the manner in which <em>the prosecution </em>presents the suspect to witnesses for pretrial identification.” <em>Ibid, </em>(emphasis added). To illustrate the improper suggestion it was concerned about, the Court pointed to police-designed lineups where “all in the lineup but the suspect were known to the identifying witness, . . . the other participants in [the] lineup were grossly dissimilar in appearance to the suspect, . . . only the suspect was required to wear distinctive clothing which the culprit allegedly wore, . . . the witness is told by the police that they have caught the culprit after <page-number citation-index="1" label="710">*710</page-number>which the defendant is brought before the witness alone or is viewed in jail, .. . the suspect is pointed out before or during a lineup, . . . the participants in the lineup are asked to try on an article of clothing which fits only the <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#233" aria-description="Citation for case: United States v. Wade"><em>suspect.” Id., </em>at 233</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">87 S. Ct. 1926</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">18 L. Ed. 2d 1149</a></span>. Beyond genuine debate, then, prevention of unfair police practices prompted the Court to extend a defendant’s right to counsel to cover postindictment lineups and showups. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><em>Id., </em>at 235</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">87 S. Ct. 1926</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">18 L. Ed. 2d 1149</a></span>.</p>
<p id="b810-4">Perry’s argument, reiterated by the dissent, thus lacks support in the case law he cites. Moreover, his position would open the door to judicial preview, under the banner of due process, of most, if not all, eyewitness identifications. External suggestion is hardly the only factor that casts doubt on the trustworthiness of an eyewitness’ testimony. As one of Perry’s <em>amici </em>points out, many other factors bear on “the likelihood of misidentification,” <em>post, </em>at 258, 181 L. Ed. 2d, at 719—for example, the passage of time between exposure to and identification of the defendant, whether the witness was under stress when he first encountered the suspect, how much time the witness had to observe the suspect, how far the witness was</p>
<p id="ADT2">[<span class="citation no-link">565 U.S. 244</span>]</p>
<p id="b810-5">from the suspect, whether the suspect carried a weapon, and the race of the suspect and the witness. Brief for American Psychological Association as <em>Amicus Curiae </em>9-12. There is no reason why an identification made by an eyewitness with poor vision, for example, or one who harbors a grudge against the defendant, should be regarded as inherently more reliable, less of a “threat to the fairness of trial,” <em>post, </em>at 262, 181 L. Ed. 2d, at 722, than the identification Blandón made in this case. To embrace Perry’s view would thus entail a vast enlargement of the reach of due process as a constraint on the admission of evidence.</p>
<p id="b810-8">Perry maintains that the Court can limit the due process check he proposes to identifications made under “suggestive circumstances.” Tr. of Oral Arg. 11-14. Even if we could rationally distinguish suggestiveness from other factors bearing on the reliability of eyewitness evidence, Perry’s limitation would still involve trial courts, routinely, in preliminary examinations.  Most eyewitness identifications involve some element of suggestion. Indeed, all in-court identifications do. Out-of-court identifications volunteered by witnesses are also likely to involve suggestive circumstances. For example, suppose a witness identifies the defendant to police officers after seeing a photograph of the defendant in the press captioned “theft suspect,” or hearing a radio report implicating the defendant in the crime. Or suppose the witness knew that the defendant ran with the wrong crowd and saw him on the day and in the vicinity of the crime. Any of these circumstances might have “suggested” to the witness that the defendant was the person the witness observed committing the crime.</p>
<p id="b810-9">C</p>
<p id="b810-10">In urging a broadly applicable due process check on eyewitness identifications, Perry maintains that eyewitness identifications are a uniquely unreliable form of evidence. See Brief for Petitioner 17-22 (citing studies showing that</p>
<p id="b810-11">[<span class="citation no-link">565 U.S. 245</span>]</p>
<p id="b810-12">eyewitness mis-identifications are the leading cause of wrongful convictions); Brief for American Psychological Association as <em>Amicus Curiae </em>14-17 (describing research indicating that as many as <page-number citation-index="1" label="711">*711</page-number>one in three eyewitness identifications is inaccurate). See also <em>post, </em>at 262-265, 181 L. Ed. 2d, at 722-724. We do not doubt either the importance or the fallibility of eyewitness identifications. Indeed, in recognizing that defendants have a constitutional right to counsel at postindictment police lineups, we observed that “the annals of criminal law are rife with instances of mistaken identification.” <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#228" aria-description="Citation for case: United States v. Wade">388 U.S., at 228</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">87 S. Ct. 1926</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">18 L. Ed. 2d 1149</a></span>.</p>
<p id="b811-4">We have concluded in other contexts, however, that the potential unreliability of a type of evidence does not alone render its introduction at the defendant’s trial fundamentally unfair. See, <em>e.g., Ventris, </em><span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/#594" aria-description="Citation for case: Kansas v. Ventris">556 U.S., at 594</a></span>, n., <span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/" aria-description="Citation for case: Kansas v. Ventris">129 S. Ct. 1841</a></span>, <span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/" aria-description="Citation for case: Kansas v. Ventris">173 L. Ed. 2d 801</a></span> (declining to “craft a broa[d] exclusionary rule for uncorroborated statements obtained [from jailhouse snitches],” even though “rewarded informant testimony” may be inherently untrustworthy); <em>Dowling, </em><span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/#353" aria-description="Citation for case: Dowling v. United States">493 U.S., at 353</a></span>, <span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/" aria-description="Citation for case: Dowling v. United States">110 S. Ct. 668</a></span>, <span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/" aria-description="Citation for case: Dowling v. United States">107 L. Ed. 2d 708</a></span> (rejecting argument that the introduction of evidence concerning acquitted conduct is fundamentally unfair because such evidence is “inherently unreliable”). We reach a similar conclusion here: The fallibility of eyewitness evidence does not, without the taint of improper state conduct, warrant a due process rule requiring a trial court to screen such evidence for reliability before allowing the jury to assess its creditworthiness.</p>
<p id="b811-6">Our unwillingness to enlarge the domain of due process as Perry and the dissent urge rests, in large part, on our recognition that the jury, not the judge, traditionally determines the reliability of evidence. See <em>supra, </em>at 237, 181 L. Ed. 2d, at 705. We also take account of other safeguards built into our adversary system that caution juries against placing undue weight on eyewitness testimony of questionable reliability. These protections include the defendant’s Sixth Amendment right to confront the eyewitness. See <em>Maryland </em>v. <em>Craig, </em><span class="citation" data-id="9842114"><a href="/opinion/112489/maryland-v-craig/#845" aria-description="Citation for case: Maryland v. Craig">497 U.S. 836, 845</a></span>, <span class="citation" data-id="9842114"><a href="/opinion/112489/maryland-v-craig/" aria-description="Citation for case: Maryland v. Craig">110 S. Ct. 3157</a></span>, <span class="citation" data-id="9842114"><a href="/opinion/112489/maryland-v-craig/" aria-description="Citation for case: Maryland v. Craig">111 L. Ed. 2d 666</a></span> (1990) (“The central concern of the Confrontation Clause</p>
<p id="A-rq">[<span class="citation no-link">565 U.S. 246</span>]</p>
<p id="b811-7">is to ensure the reliability of the evidence against a criminal defendant.”). Another is the defendant’s right to the effective assistance of an attorney, who can expose the flaws in the eyewitness’ testimony during cross-examination and focus the jury’s attention on the fallibility of such testimony during opening and closing arguments. Eyewitness-specific jury instructions, which many federal and state courts have adopted,<footnotemark>7</footnotemark> likewise warn the jury to take care in appraising identification evidence. See, <em>e.g., </em><page-number citation-index="1" label="712">*712</page-number><em>United States </em>v. <em>Telfaire, </em><span class="citation" data-id="9458886"><a href="/opinion/306634/united-states-v-melvin-telfaire/#558" aria-description="Citation for case: United States v. Melvin Telfaire">469 F.2d 552, 558-559</a></span> (CADC 1972) <em>(per curiam) </em>(D. C. Circuit Model Jury Instructions) (“If the identification by the witness may have been influenced by the circumstances under which the defendant was presented to him for identification, you should scrutinize the identification with great care.”). See also <em>Ventris, </em><span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/#594" aria-description="Citation for case: Kansas v. Ventris">556 U.S., at 594</a></span>, n., <span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/" aria-description="Citation for case: Kansas v. Ventris">129 S. Ct. 1841</a></span>, <span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/" aria-description="Citation for case: Kansas v. Ventris">173 L. Ed. 2d 801</a></span> (citing jury instructions that informed jurors about the unreliability of uncorroborated jailhouse-informant testimony as a reason to</p>
<p id="b812-4">[<span class="citation no-link">565 U.S. 247</span>]</p>
<p id="b812-5">resist a ban on such testimony); <em>Dowling, </em><span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/#352" aria-description="Citation for case: Dowling v. United States">493 U.S., at 352-353</a></span>, <span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/" aria-description="Citation for case: Dowling v. United States">110 S. Ct. 668</a></span>, <span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/" aria-description="Citation for case: Dowling v. United States">107 L. Ed. 2d 708</a></span>. The constitutional requirement that the government prove the defendant’s guilt beyond a reasonable doubt also impedes convictions based on dubious identification evidence.</p>
<p id="b812-6">State and Federal Rules of Evidence, moreover, permit trial judges to exclude relevant evidence if its probative value is substantially outweighed by its prejudicial impact or potential for misleading the jury. See, <em>e.g., </em>Fed. Rule Evid. 403; N.H. Rule Evid. 403 (2011). See also Tr. of Oral Arg. 19-22 (inquiring whether the standard Perry seeks differs materially from the one set out in Rule 403). In appropriate cases, some States also permit defendants to present expert testimony on the hazards of eyewitness identification evidence. See, <em>e.g., State </em>v. <em>Clopten, </em><span class="citation" data-id="9788258"><a href="/opinion/2592762/state-v-clopten/#33" aria-description="Citation for case: State v. Clopten">2009 UT 84, ¶ 33</a></span>, <span class="citation" data-id="9788258"><a href="/opinion/2592762/state-v-clopten/#1113" aria-description="Citation for case: State v. Clopten">223 P.3d 1103, 1113</a></span> (“We expect . . . that in cases involving eyewitness identification of strangers or near-strangers, trial courts will routinely admit expert testimony [on the dangers of such evidence].”).</p>
<p id="b812-7">Many of the safeguards just noted were at work at Perry’s trial. During her opening statement, Perry’s cour-tappointed attorney cautioned the jury about the vulnerability of Bland-on’s identification. App. 115a (Blan-dón, “the eyewitness that the State needs you to believe [,] can’t pick [Perry] out of a photo array. How carefully did she really see what was going on? . . . How well could she really see him?”). While cross-examining Blandón and Officer Clay, Perry’s attorney constantly brought up the weaknesses of Blandon’s identification. She highlighted: (1) the significant distance between Blandon’s window and the parking lot, <em><span class="citation" data-id="9788258"><a href="/opinion/2592762/state-v-clopten/" aria-description="Citation for case: State v. Clopten">id.,</a></span> </em>at 226a; (2) the lateness of the hour, <em><span class="citation" data-id="9788258"><a href="/opinion/2592762/state-v-clopten/" aria-description="Citation for case: State v. Clopten">id.,</a></span> </em>at 225a; (3) the van that partly obstructed Blandon’s view, <em><span class="citation" data-id="9788258"><a href="/opinion/2592762/state-v-clopten/" aria-description="Citation for case: State v. Clopten">id.,</a></span> </em>at 226a; (4) Blandon’s concession that she was “so scared [she] really didn’t pay attention” to what Perry was wearing, <em><span class="citation" data-id="9788258"><a href="/opinion/2592762/state-v-clopten/" aria-description="Citation for case: State v. Clopten">id.,</a></span> </em>at 233a; (5) Blandon’s inability to describe Perry’s facial features or other identifying marks, <em><span class="citation" data-id="9788258"><a href="/opinion/2592762/state-v-clopten/" aria-description="Citation for case: State v. Clopten">id.,</a></span> </em>at 205a, 233a-235a; (6) Blandon’s failure to pick Perry out of a photo array, <em><span class="citation" data-id="9788258"><a href="/opinion/2592762/state-v-clopten/" aria-description="Citation for case: State v. Clopten">id.,</a></span> </em>at 235a; and (7)</p>
<p id="b812-9">[<span class="citation no-link">565 U.S. 248</span>]</p>
<p id="b812-10">Perry’s position next to a uniformed, gun-bearing police officer at the moment Blandón made her identification, <em><span class="citation no-link">id.,</span> </em>at 202a-205a. Perry’s counsel reminded the jury of these frailties during her summation. <em><span class="citation no-link">Id.,</span> </em>at 374a-375a (Blandón “wasn’t able to tell you much about who she saw .... She couldn’t pick [Perry] out of a lineup, out of a photo array .... [Blandón said] [t]hat guy that was with the police officer, that’s who was circling. Again, think about the context with the guns, the uniforms. Powerful, powerful context clues.”).</p>
<p id="b812-11">After closing arguments, the trial court read the jury a lengthy instruction on identification testimony and the factors the jury should consider <page-number citation-index="1" label="713">*713</page-number>when evaluating it. <em><span class="citation no-link">Id.,</span> </em>at 399a-40la. The court also instructed the jury that the defendant’s guilt must be proved beyond a reasonable doubt, <em><span class="citation no-link">id.,</span> </em>at 390a, 392a, 395a-396a, and specifically cautioned that “one of the things the State must prove [beyond a reasonable doubt] is the identification of the defendant as the person who committed the offense,” <em><span class="citation no-link">id.,</span> </em>at 398a-399a.</p>
<p id="b813-6">Given the safeguards generally applicable in criminal trials, protections availed of by the defense in Perry’s case, we hold that the introduction of Blandon’s eyewitness testimony, without a preliminary judicial assessment of its reliability, did not render Perry’s trial fundamentally unfair.</p>
<p id="Am26">* * *</p>
<p id="b813-11">For the foregoing reasons, we agree with the New Hampshire courts’ appraisal of our decisions. See <em>supra, </em>at 235-236, 181 L. Ed. 2d, at 704-705. Finding no convincing reason to alter our precedent, we hold that [16] the Due Process Clause does not require a preliminary judicial inquiry into the reliability of an eyewitness identification when the identification was not procured under unnecessarily suggestive circumstances arranged by law enforcement. Accordingly, the judgment of the New Hampshire Supreme Court is affirmed.</p>
<footnote label="1">
<p id="b803-14">. The dissent, too, appears to urge that all suggestive circumstances raise due process concerns warranting a pretrial ruling. See <em>post, </em>at 254, 257, 262-265, 181 L. Ed. 2d, at 717, 718, 722-724. Neither Perry nor the dissent, however, points to a single case in which we have required pretrial screening absent a police arranged identification procedure. Understandably so, for there are no such cases. Instead, the dissent surveys our decisions, heedless of the police arrangement that underlies every one of them, and inventing a “longstanding rule,’’ <em>post, </em>at 254, 181 L. Ed. 2d, at 717, that never existed. Nor are we, as the dissent suggests, imposing a <em>mens rea </em>requirement, <em>post, </em>at 250, 255, 181 L. Ed. 2d, at 714, 717, or otherwise altering our precedent in any way.  As our case law makes clear, what triggers due process concerns is police use of an unnecessarily suggestive identification procedure, whether or not they intended the arranged procedure to be suggestive.</p>
</footnote>
<footnote label="2">
<p id="b804-14">. The box, which Clay found on the ground near where she first encountered Perry, contained car-stereo speakers. App. 177a-178a.</p>
</footnote>
<footnote label="3">
<p id="b804-15">. The theft charge was based on the taking of items from Clavijo’s car, while the criminal mischief count was founded on the shattering of Clavijo’s car window.</p>
</footnote>
<footnote label="4">
<p id="b805-14">. Compare <em>United States </em>v. <em>Bouthot, </em><span class="citation" data-id="526035"><a href="/opinion/526035/united-states-v-joseph-t-bouthot/#1516" aria-description="Citation for case: United States v. Joseph T. Bouthot">878 F.2d 1506, 1516</a></span> (CA1 1989) (Due process requires federal courts to “scrutinize all suggestive identification procedures, not just those orchestrated by the police.’’); <em>Dunnigan </em>v. <em>Keane, </em><span class="citation" data-id="751771"><a href="/opinion/751771/richard-w-dunnigan-v-john-p-keane-superintendent-sing-sing/#128" aria-description="Citation for case: Richard W. Dunnigan v. John P. Keane, Superintendent,...">137 F.3d 117, 128</a></span> (CA2 1998) (same); <em>Thigpen </em>v. <em>Cory, </em><span class="citation" data-id="9475532"><a href="/opinion/478967/willie-arthur-thigpen-v-duane-cory/#895" aria-description="Citation for case: Willie Arthur Thigpen v. Duane Cory">804 F.2d 893, 895</a></span> (CA6 1986) (same), with <em>United States </em>v. <em>Kimberlin, </em><span class="citation" data-id="9475552"><a href="/opinion/479235/united-states-v-brett-c-kimberlin/#233" aria-description="Citation for case: United States v. Brett C. Kimberlin">805 F.2d 210, 233</a></span> (CA7 1986) (Due process check is required only in cases involving improper state action.); <em>United States </em>v. <em>Zeiler, </em><span class="citation" data-id="307083"><a href="/opinion/307083/united-states-v-william-edward-zeiler/#720" aria-description="Citation for case: United States v. William Edward Zeiler">470 F.2d 717, 720</a></span> (CA3 1972) (same); <em>State </em>v. <em>Addison, </em><span class="citation" data-id="2446404"><a href="/opinion/2446404/state-v-addison/#801" aria-description="Citation for case: State v. Addison">160 N.H. 792, 801</a></span>, <span class="citation" data-id="2446404"><a href="/opinion/2446404/state-v-addison/#125" aria-description="Citation for case: State v. Addison">8 A.3d 118, 125</a></span> (2010) (same); <em>State </em>v. <em>Reid, </em><span class="citation" data-id="9662547"><a href="/opinion/1636806/state-v-reid/#272" aria-description="Citation for case: State v. Reid">91 S.W.3d 247, 272</a></span> (Tenn. 2002) (same); <em>State </em>v. <em>Nordstrom, </em><span class="citation" data-id="2587271"><a href="/opinion/2587271/state-v-nordstrom/#241" aria-description="Citation for case: State v. Nordstrom">200 Ariz. 229, 241</a></span>, <span class="citation" data-id="2587271"><a href="/opinion/2587271/state-v-nordstrom/#729" aria-description="Citation for case: State v. Nordstrom">25 P.3d 717, 729</a></span> (2001) (same); <em>Semple </em>v. <em>State, </em><span class="citation" data-id="1226333"><a href="/opinion/1226333/semple-v-state/#417" aria-description="Citation for case: Semple v. State">271 Ga. 416, 417-418</a></span>, <span class="citation" data-id="1226333"><a href="/opinion/1226333/semple-v-state/#913" aria-description="Citation for case: Semple v. State">519 S.E.2d 912, 913-914</a></span> (1999) (same); <em>Harris </em>v. <em>State, </em><span class="citation" data-id="2232289"><a href="/opinion/2232289/harris-v-state/#581" aria-description="Citation for case: Harris v. State">619 N.E.2d 577, 581</a></span> (Ind. 1993) (same); <em>State </em>v. <em>Pailon, </em><span class="citation" data-id="2390875"><a href="/opinion/2390875/state-v-pailon/#862" aria-description="Citation for case: State v. Pailon">590 A.2d 858, 862-863</a></span> (R. I. 1991) (same); <em>Commonwealth </em>v. <em>Colon-Cruz, </em><span class="citation" data-id="2153683"><a href="/opinion/2153683/commonwealth-v-colon-cruz/#541" aria-description="Citation for case: Commonwealth v. Colon-Cruz">408 Mass. 533, 541-542</a></span>, <span class="citation" data-id="2153683"><a href="/opinion/2153683/commonwealth-v-colon-cruz/#805" aria-description="Citation for case: Commonwealth v. Colon-Cruz">562 N.E.2d 797, 805</a></span> (1990) (same); <em>State </em>v. <em>Brown, </em><span class="citation" data-id="6760622"><a href="/opinion/6869000/state-v-brown/#310" aria-description="Citation for case: State v. Brown">38 Ohio St. 3d 305, 310-311</a></span>, <span class="citation multiple-matches"><a href="/c/N.E.2d/528/523/">528 N.E.2d 523</a></span>, 533 (1988) (same); <em>Wilson </em>v. <em>Commonwealth, </em><span class="citation" data-id="1777225"><a href="/opinion/1777225/wilson-v-commonwealth/#857" aria-description="Citation for case: Wilson v. Commonwealth">695 S.W.2d 854, 857</a></span> (Ky. 1985) (same).</p>
</footnote>
<footnote label="5">
<p id="b807-12">. Among “factors to be considered’’ in evaluating a witness’ “ability to make an accurate identification,’’ the Court listed: “the opportunity of the witness to view the criminal at the time of the crime, the witness’ degree of attention, the accuracy of his prior description of the criminal, the level of certainty demonstrated at the confrontation, and the time between the crime and the confrontation.’’ <em>Manson </em>v. <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#114" aria-description="Citation for case: Manson v. Brathwaite">432 U.S. 98, 114</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span> (1977) (citing <em>Neil </em>v. <em>Biggers, </em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#199" aria-description="Citation for case: Neil v. Biggers">409 U.S. 188, 199-200</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">93 S. Ct. 375</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">34 L. Ed. 2d 401</a></span> (1972)).</p>
</footnote>
<footnote label="6">
<p id="b808-11">. The Court’s description of the question presented in <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Brathwaite</a></span> </em>assumes that improper state action occurred: “[Does] the Due Process Clause of the Fourteenth Amendment compe[l] the exclusion, in a state criminal trial, apart from any consideration of reliability, of pretrial identification evidence obtained by a police procedure that was both suggestive and unnecessary.’’ <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#99" aria-description="Citation for case: Manson v. Brathwaite">432 U.S., at 99</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b811-9">. See Model Crim. Jury Instr. No. 4.15 (CA3 2009); <em>United States </em>v. <em>Holley, </em><span class="citation" data-id="321228"><a href="/opinion/321228/united-states-v-albert-junior-holley/#277" aria-description="Citation for case: United States v. Albert Junior Holley">502 F.2d 273, 277-278</a></span> (CA4 1974); Pattern Crim. Jury Instr. No. 1.29 (CA5 2001); Pattern Crim. Jury Instr. No. 7.11 (CA6 2011); Fed. Crim. Jury Instr. No. 3.08 (CA7 1999); Model Crim. Jury Instr. for the District Courts No. 4.08 (CA8 2011); Model Crim. Jury Instr. No. 4.11 (CA9 2010); Pattern Crim. Jury Instr. No. 1.29 (CA10 2011); Pattern Jury Instr., Crim. Cases, Spec. Instr. No. 3 (CA11 2010); Rev. Ariz. Jury Instr., Crim., No. 39 (3d ed. 2008); 1 Judicial Council of Cal., Crim. Jury Instr., No. 315 (Summer 2011); Conn. Crim. Jury Instr. No. 2.6-4 (4th ed. 2007); 2 Ga. Suggested Pattern Jury Instr., Crim. Cases, No. 1.35.10 (4th ed. 2011); Ill. Pattern Jury Instr., Crim., No. 3.15 (Supp. 2011); Pattern Instr., Kan. 3d, Crim., No. 52.20 (2011); 1 Md. Crim. Jury Instr. &amp; Commentary §§ 2.56, 2.57(A), 2.57(B) (3d ed. 2009 and Supp. 2010); Mass. Crim. Model Jury Instr. No. 9.160 (2009); 10 Minn. Jury Instr. Guides, Crim., No. 3.19 (Supp. 2006); N.H. Crim. Jury Instr. No. 3.06 (1985); N.Y. Crim. Jury Instr. “Identification—One Witness’’ and “Identification—Witness Plus’’ (2d ed. 2011); Okla. Uniform Jury Instr., Crim., No. 9-19 (Supp. 2000); 1 Pa. Suggested Standard Crim. Jury Instr. No. 4.07B (2d ed. 2010); Term. Pattern Jury Instr., Crim., No. 42.05 (15th ed. 2011); Model <page-number citation-index="1" label="712">*712</page-number>Utah Jury Instr. CR404 (2d ed. 2011); Model Instructions from the Vt. Crim. Jury Instr. Comm. Nos. CR5-601, CR5-605 (2003); W. Va. Crim. Jury Instr. No. 5.05 (6th ed. 2003).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Perttu v. Richards.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Perttu v. Richards
type: case
citation: "605 U.S. 460 (2025)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2025
date_decided: ""
docket: 23-1324
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
  opinion_url: "https://www.courtlistener.com/opinion/10776832/perttu-v-richards/"
  cluster_id: 10776832
  opinion_id: null
  identity_checked: true
lake:
  record_id: Perttu v. Richards
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
  - plra
  - seventh-amendment
  - first-amendment-retaliation
holding: "When a dispute over PLRA exhaustion is intertwined with the merits of a claim carrying a Seventh Amendment jury-trial right, the parties are entitled to a jury trial on the exhaustion question rather than a bench determination by the judge."
---

# Perttu v. Richards

*605 U.S. 460 (2025)* (No. 23-1324) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10776832 → opinion 11243419; quote string-matched to the CL opinion text 2026-07-07 (CL preliminary print carries U.S. Reports pagination). S9 promotes. -->

## Background
Kyle Richards, a Michigan prisoner, sued prison employee Thomas Perttu under 42 U.S.C. § 1983, alleging that Perttu sexually abused him and other inmates and then destroyed the grievance forms Richards tried to file about the abuse and retaliated against him for filing — violating Richards's First Amendment right to file grievances. Perttu moved for summary judgment, arguing the plaintiffs had failed to exhaust available grievance procedures as the Prison Litigation Reform Act (PLRA) requires. A magistrate judge held an evidentiary hearing, found Richards's witnesses on the destruction-of-grievances issue "lacked credibility," and recommended dismissal for failure to exhaust; the district court adopted that recommendation. The same disputed fact — whether Perttu destroyed the grievances — governed both exhaustion and the First Amendment merits. The Sixth Circuit reversed.

## Issue
Whether a party has a right to a jury trial on PLRA exhaustion when that dispute is intertwined with the merits of a claim that requires a jury trial under the Seventh Amendment.

## Rule
PLRA exhaustion is an ordinary [[Common Legal Terms#affirmative-defense|affirmative defense]], and the PLRA is silent on whether a judge or a jury resolves exhaustion disputes. Congress legislates against a background of common-law adjudicatory principles under which factual disputes intertwined with jury-triable legal claims go to the jury (*Beacon Theatres*; *Smithers*), and that silence is "strong evidence that the usual practice should be followed." The Court therefore held: "For those reasons, we hold as a matter of statutory interpretation that parties have a right to a jury trial on PLRA exhaustion when that issue is intertwined with the merits of a claim that falls under the Seventh Amendment." — 605 U.S. at 468. ^pin-468

## Application
Whether Perttu destroyed Richards's grievances decided both the exhaustion defense and the First Amendment retaliation claim — a legal claim triable to a jury. Because those questions were intertwined, the district court could not resolve the shared fact at a bench hearing and then dismiss for non-exhaustion; the intertwined factual dispute had to be tried to a jury. The Court construed the PLRA to require that result and so did not reach whether the Seventh Amendment would independently compel it.

## Conclusion
The judgment of the Sixth Circuit was **affirmed**. Roberts, C.J., delivered the opinion of the Court, joined by Sotomayor, Kagan, Gorsuch, and Jackson, JJ.; Barrett, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], joined by Thomas, Alito, and Kavanaugh, JJ.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Perttu* is a procedural decision at the § 1983 prisoner-litigation gate: it keeps a jury, not the judge, as the factfinder when a PLRA exhaustion dispute and a jury-triable constitutional claim rise or fall on the same disputed fact.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Perttu v. Richards*, 605 U.S. 460 (2025)](https://www.courtlistener.com/opinion/10776832/perttu-v-richards/) — pinpoint: 468 (Opinion of the Court, holding; Roberts, C.J.); quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "44228f30ee925427", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Perttu v. Richards"}, "payload": {"all": [{"cite": "605 U.S. 460", "page": "460", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "605"}], "display": "605 U.S. 460", "official": {"cite": "605 U.S. 460", "page": "460", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "605"}, "official_selection_present": true, "record_id": "Perttu v. Richards"}}
{"assertion_id": "31060197ca8075a5", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Perttu v. Richards"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Perttu v. Richards", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Perttu v. Richards

```json
{
  "schema_version": "s2.v1",
  "record_id": "Perttu v. Richards",
  "status": "under_review",
  "identity": {
    "case_name": "Perttu v. Richards",
    "case_name_short": "Perttu",
    "case_name_full": "",
    "input_case_name": "Perttu v. Richards",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2025,
    "docket": "23-1324",
    "cluster_id": 10776832,
    "lead_opinion_id": 11243419,
    "sibling_ids": [],
    "absolute_url": "/opinion/10776832/perttu-v-richards/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "605 U.S. 460",
      "volume": "605",
      "reporter": "U.S.",
      "page": "460",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "605 U.S. 460",
        "volume": "605",
        "reporter": "U.S.",
        "page": "460",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "605 U.S. 460",
    "official_selection": {
      "court_class": "scotus",
      "selected": "605 U.S. 460",
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
    "date_created": "2026-07-06T12:12:42Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:12:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:12:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "perttu-v-richards--10776832",
      "to_record_id": "Perttu v. Richards",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Perttu v. Richards

```
                   PRELIMINARY PRINT

              Volume 605 U. S. Part 2
                             Pages 460–494




       OFFICIAL REPORTS
                                     OF


   THE SUPREME COURT
                                June 18, 2025


Page Proof Pending Publication


                    REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D. C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
460                     OCTOBER TERM, 2024

                                Syllabus


                     PERTTU v. RICHARDS

certiorari to the united states court of appeals for
                  the sixth circuit
      No. 23–1324 Argued February 25, 2025—Decided June 18, 2025
The Prison Litigation Reform Act (PLRA) requires prisoners with com-
  plaints about prison conditions to exhaust available grievance proce-
  dures before fling suit in federal court. 42 U. S. C. § 1997e(a). But
  “exhaustion is not required” when a prison administrator “threaten[s]
  individual inmates so as to prevent their use of otherwise proper proce-
  dures.” Ross v. Blake, 578 U. S. 632, 644. “Such interference with an
  inmate's pursuit of relief renders the administrative process unavail-
  able,” so “§ 1997e(a) poses no bar” to suit. Ibid. The question pre-
  sented is whether a party has a right to a jury trial on PLRA exhaustion
  when that dispute is intertwined with the merits of the underlying suit.
    In this case, inmate Kyle Richards alleges that Thomas Perttu, a
  prison employee, sexually harassed Richards and other inmates. Rich-
  ards also alleges that, when he attempted to fle grievance documents
Page Proof Pending Publication
  about the abuse, Perttu destroyed them and “retaliated against” him for
  attempting to fle them. Richards sued Perttu under 42 U. S. C. § 1983
  for violating his constitutional rights, including his First Amendment
  right to fle grievances. Perttu moved for summary judgment, arguing
  that the plaintiffs had failed to exhaust available grievance procedures
  as required by the PLRA. The Magistrate Judge concluded that there
  was “a genuine issue of fact as to whether Plaintiffs were excused from
  properly exhausting their claims due to interference by Perttu” and that
  the issue was “appropriate for resolution during an evidentiary hear-
  ing.” App. to Pet. for Cert. 86a. At that hearing, the Magistrate
  Judge concluded that Richards's witnesses regarding Perttu's alleged
  destruction of grievance forms “lacked credibility.” The Magistrate
  Judge recommended dismissal without prejudice for failure to exhaust,
  and the District Court adopted that recommendation. The Sixth Cir-
  cuit reversed. It stated that there was “no doubt that a judge may
  otherwise resolve factual disputes regarding exhaustion under the
  PLRA,” but it held that “the Seventh Amendment requires a jury trial
  when the resolution of the exhaustion issue under the PLRA would also
  resolve a genuine dispute of material fact regarding the merits of the
  plaintiff 's substantive case.” 96 F. 4th 911, 917, 923. That decision
  conficted with Seventh Circuit precedent.
                       Cite as: 605 U. S. 460 (2025)                   461

                                 Syllabus

Held: Parties are entitled to a jury trial on PLRA exhaustion when that
 issue is intertwined with the merits of a claim that requires a jury trial
 under the Seventh Amendment. Pp. 467–479.
    (a) Before reaching Richards's arguments for why his Seventh
 Amendment right to a jury trial has been violated, the Court must frst
 determine whether a construction of the PLRA is “fairly possible” by
 which the constitutional question may be avoided. Monterey v. Del
 Monte Dunes at Monterey, Ltd., 526 U. S. 687, 707. Such a construc-
 tion is possible here. Because the Court construes the PLRA to re-
 quire a jury trial in Richards's case, the Court need not address whether
 Congress could have required otherwise in the PLRA without violating
 the Seventh Amendment.
    PLRA exhaustion is a standard affrmative defense subject to “the
 usual practice” under the Federal Rules of Civil Procedure. Jones v.
 Bock, 549 U. S. 199, 212. The usual practice is that factual disputes
 regarding legal claims go to the jury, even if that means a judge must let
 a jury decide questions he could ordinarily resolve on his own. Beacon
 Theatres, Inc. v. Westover, 359 U. S. 500, 510–511. That usual practice
 matters for interpreting the PLRA because “Congress is understood to
 legislate against a background of common-law adjudicatory principles
 . . . with an expectation that the principle[s] will apply except `when a
Page Proof Pending Publication
 statutory purpose to the contrary is evident.' ” Astoria Fed. Sav. &
 Loan Assn. v. Solimino, 501 U. S. 104, 108 (quoting Isbrandtsen Co. v.
 Johnson, 343 U. S. 779, 783). No such contrary purpose is evident in the
 PLRA. The PLRA is “silent” on whether judges or juries should resolve
 exhaustion disputes, and that silence is “strong evidence that the usual
 practice should be followed.” Jones, 549 U. S., at 212. Pp. 467–470.
    (b) At the time the PLRA was enacted, it was well established that
 factual disputes intertwined with claims that fall under the Seventh
 Amendment should go to a jury. The Court has held in various con-
 texts that, in cases of intertwinement, district courts should structure
 their order of operations to preserve the jury trial right. Pp. 470–474.
       (1) One prominent line of cases involves suits that contain both
 legal and equitable claims. Ordinarily, judges resolve equitable claims
 and juries resolve legal claims. In Beacon Theatres, this Court held
 that judges may not resolve equitable claims frst if doing so could pre-
 vent legal claims from getting to the jury. In that case, both the legal
 and equitable claims hinged on the “common issue” whether there was
 an antitrust violation. 359 U. S. 500, 503. The Court emphasized that
 in that situation, judicial “discretion is very narrowly limited and must,
 wherever possible, be exercised to preserve jury trial.” Id., at 510.
 Because resolving the equitable claims could “prevent a full jury trial”
462                     PERTTU v. RICHARDS

                                 Syllabus

 on the legal claims, the legal claims frst needed to be resolved by a jury.
 Id., at 505, 508. In this case, the parties agree that the exhaustion
 and First Amendment questions depend on common factual issues, and
 Beacon Theatres teaches that a trial court must preserve the jury trial
 in such a situation whenever possible. Nothing in the PLRA prevents
 holding a jury trial here. Pp. 471–472.
       (2) Cases involving subject matter jurisdiction are also instructive.
 Ordinarily, judges may resolve factual disputes when determining sub-
 ject matter jurisdiction. But courts may not do so when the factual
 disputes are intertwined with the merits. In Smithers v. Smith, 204
 U. S. 632, the Court held that judicial authority to dismiss for lack of
 subject matter jurisdiction “obviously is not unlimited,” for that would
 risk summarily determining the merits “without the ordinary incidents
 of a trial, including the right to a jury.” Id., at 645. In Land v. Dollar,
 330 U. S. 731, the Court found that Land was “the type of case where
 the question of jurisdiction is dependent on decision of the merits” and
 thus held the District Court should have “proceed[ed] to a decision on
 the merits.” Id., at 735, 738–739.
    In its decision below, the Sixth Circuit relied on its precedent applying
 Land, reasoning that if “certain cases [must] be heard and determined
 on the merits even when constitutionally implicated jurisdictional dis-
Page Proof Pending Publication
 putes” are at play, then “the result should be the same when the lesser
 concern of an affrmative defense, such as the PLRA's requirement to
 exhaust administrative remedies, implicates the merits of a claim.” 96
 F. 4th, at 923. The Court fnds this reasoning persuasive. After all,
 when the PLRA was enacted, many lower court decisions and treatises
 had extended the intertwinement principle to other threshold questions,
 like personal jurisdiction and venue. The Court expresses no view
 today on whether lower courts have been correct to extend the inter-
 twinement principle to these other issues, but simply notes that these
 cases—along with Beacon Theatres and Smithers—show that when the
 PLRA was enacted, the usual practice in the federal courts across a
 variety of contexts was to resolve factual disputes that are intertwined
 with the merits at the merits stage. Pp. 472–474.
    (c) Perttu's counterarguments are unpersuasive. Perttu argues that
 Beacon Theatres is inapplicable, but his argument relies on the question-
 able assumption that judicial factual fndings concerning exhaustion
 have no estoppel effect in later jury trials. Regardless, even if Perttu
 is correct about estoppel, Beacon Theatres still applies when judicial
 resolution might prevent a full jury trial for other reasons. Here, Rich-
 ards's claim is being dismissed entirely rather than just estopped, and
 it is usually impossible for prisoners to go back and exhaust then fle
 suit again, because grievance deadlines will have long since passed.
                       Cite as: 605 U. S. 460 (2025)                   463

                                 Syllabus

  Perttu's argument that jury trials confict with the PLRA's purpose of
  conserving judicial resources also fails, because the PLRA contemplates
  that merits claims will be resolved by a jury and is silent about exhaus-
  tion. The usual federal court practice in cases of intertwinement is to
  send common issues to the jury, and nothing in the PLRA suggests
  Congress intended to depart from that practice. Pp. 474–478.
96 F. 4th 911, affrmed.
   Roberts, C. J., delivered the opinion of the Court, in which Sotomayor,
Kagan, Gorsuch, and Jackson, JJ., joined. Barrett, J., fled a dissent-
ing opinion, in which Thomas, Alito, and Kavanaugh, JJ., joined, post,
p. 479.

  Ann M. Sherman, Solicitor General of Michigan, argued
the cause for petitioner. With her on the briefs were Kyla
L. Barranco, Assistant Solicitor General, and Joshua S.
Smith, Assistant Attorney General.
  Lori Alvino McGill argued the cause for respondent.
With her on the brief was J. Scott Ballenger.*
  *Briefs of amici curiae urging reversal were fled for the State of Ohio
Page
et al. by DaveProof        Pending
               Yost, Attorney                   Publication
                              General of Ohio, T. Elliot Gaiser, Solicitor
General, Zachery P. Keller, Deputy Solicitor General, and Daniel McKit-
rick and Brandon Kennedy, Assistant Attorneys General, and by the At-
torneys General for their respective jurisdictions as follows: Steve Mar-
shall of Alabama, Tim Griffn of Arkansas, William Tong of Connecticut,
Brian L. Schwalb of the District of Columbia, Ashley Moody of Florida,
Christopher M. Carr of Georgia, Raúl R. Labrador of Idaho, Theodore E.
Rokita of Indiana, Brenna Bird of Iowa, Kris Kobach of Kansas, Russell
Coleman of Kentucky, Elizabeth B. Murrill of Louisiana, Anthony G.
Brown of Maryland, Lynn Fitch of Mississippi, Austin Knudsen of Mon-
tana, Michael T. Hilgers of Nebraska, Gentner Drummond of Oklahoma,
Ellen F. Rosenblum of Oregon, Peter F. Neronha of Rhode Island, Alan
Wilson of South Carolina, Marty Jackley of South Dakota, Jonathan
Skrmetti of Tennessee, Ken Paxton of Texas, and Sean D. Reyes of Utah;
for the International Municipal Lawyers Association et al. by F. Andrew
Hessick, Richard A. Simpson, Amanda Karras, and Erich Eiselt; and for
the National Sheriffs' Association et al. by Gregory C. Champagne and
Maurice E. Bostick.
  Briefs of amici curiae urging affrmance were fled for the American
Civil Liberties Union et al. by Jennifer A. Wedekind, Cecillia D. Wang,
and Daniel S. Korobkin; for the Cato Institute by Clark M. Neily III and
Matthew Cavedon; and for Law Professors by Kevin K. Russell.
464                 PERTTU v. RICHARDS

                      Opinion of the Court

  Chief Justice Roberts delivered the opinion of the
Court.
   The Prison Litigation Reform Act of 1995 (PLRA) re-
quires prisoners with complaints about prison conditions to
exhaust available grievance procedures before bringing suit
in federal court. 42 U. S. C. § 1997e(a). In some cases the
question whether a prisoner has exhausted those procedures
is intertwined with the merits of the prisoner's lawsuit. Re-
spondent Kyle Richards is a prisoner in Michigan. He al-
leges that he was sexually abused by petitioner Thomas
Perttu, a prison employee. He also alleges that when he
tried to fle grievance forms about the abuse, Perttu de-
stroyed them and threatened to kill him if he fled more.
   Richards sued Perttu for violating his constitutional
rights, including his First Amendment right to fle griev-
ances. Perttu responded that Richards had failed to ex-
haust available grievance procedures as required by the
Page Proof Pending Publication
PLRA. The parties agree that the exhaustion and First
Amendment issues are intertwined, because both depend on
whether Perttu did in fact destroy Richards's grievances and
retaliate against him. The question presented is whether a
party has a right to a jury trial on PLRA exhaustion when
that dispute is intertwined with the merits of the underly-
ing suit.
                              I
                              A
   “Our legal system [is] committed to guaranteeing that pris-
oner claims of illegal conduct by their custodians are fairly
handled according to law.” Jones v. Bock, 549 U. S. 199, 203
(2007). “The challenge,” however, “lies in ensuring that the
food of nonmeritorious claims does not submerge and effec-
tively preclude consideration of the allegations with merit.”
Ibid. To address that challenge, Congress enacted the Prison
Litigation Reform Act of 1995, 110 Stat. 1321–71, as amended,
42 U. S. C. § 1997e, which aims to “reduce the quantity and im-
                   Cite as: 605 U. S. 460 (2025)            465

                      Opinion of the Court

prove the quality of prisoner suits.” Porter v. Nussle, 534
U. S. 516, 524 (2002).
  A “centerpiece” of the PLRA is its exhaustion provision.
Woodford v. Ngo, 548 U. S. 81, 84 (2006). It provides:
    “No action shall be brought with respect to prison condi-
    tions under [42 U. S. C. § 1983], or any other Federal law,
    by a prisoner confned in any jail, prison, or other correc-
    tional facility until such administrative remedies as are
    available are exhausted.” § 1997e(a).
We have held that this provision “requires proper exhaus-
tion” of available prison grievance procedures, meaning a
prisoner “must complete the administrative review process
in accordance with the applicable procedural rules . . . as a
precondition to bringing suit in federal court.” Woodford,
548 U. S., at 88, 93. But “exhaustion is not required” when
a prison administrator “threaten[s] individual inmates so as
to prevent their use of otherwise proper procedures.” Ross
Page Proof Pending Publication
v. Blake, 578 U. S. 632, 644 (2016). As we have explained,
“such interference with an inmate's pursuit of relief renders
the administrative process unavailable,” so “§ 1997e(a) poses
no bar” to suit. Ibid.
                              B
   In 2020, Richards and two other prisoners fled this suit
against Perttu under 42 U. S. C. § 1983. The complaint al-
leged that, over the prior year, Perttu had “engaged in a
pattern of prolifc and repetitive sexual abuse, against at
least a dozen inmates,” in violation of their constitutional
rights. App. 2–3. The complaint also alleged that the
plaintiffs had “attempted to exhaust remedies to the best of
[their] ability” but had been “threatened and retaliated
against” for doing so. Id., at 2, 13. The complaint listed
specifc incidents in which Perttu allegedly ripped up the
plaintiffs' grievance forms, threw them away, and threatened
to kill the plaintiffs if they fled more. Id., at 13–18. The
plaintiffs also alleged they were being “wrongfully held in
466                 PERTTU v. RICHARDS

                      Opinion of the Court

administrative segregation in retaliation for fling griev-
ances” and that Perttu was retaliating against them in other
ways, all in violation of their First Amendment rights. Id.,
at 18–27.
   Perttu moved for summary judgment, arguing that the
plaintiffs had failed to exhaust available grievance proce-
dures as required by the PLRA. To support his motion,
Perttu submitted an affdavit from a prison grievance coordi-
nator attesting that there was no record evidence of the
plaintiffs fling grievances about sexual abuse by Perttu in
2019 or 2020. The plaintiffs responded by reiterating that
Perttu had intercepted and destroyed those grievances and
had warned them not to fle more. The Magistrate Judge
concluded that there was “a genuine issue of fact as to
whether Plaintiffs were excused from properly exhausting
their claims due to interference by Perttu” and that the issue
was “appropriate for resolution during an evidentiary hear-
ing.” App. to Pet. for Cert. 86a.
Page Proof Pending Publication
   The Magistrate Judge held the evidentiary hearing by
video conference in November 2021. App. 88. Richards,
representing himself, conducted direct examinations of mul-
tiple witnesses who testifed that they had seen Perttu de-
stroy Richards's grievance forms and retaliate against him
for fling them. See, e.g., id., at 210–214, 230, 234–238, 250–
255. Perttu denied doing so. Id., at 339–341. The Magis-
trate Judge concluded that Richards's witnesses “lacked
credibility” because their testimony “was either substan-
tially guided by Richards's manner of questioning or wholly
conclusory.” App. to Pet. for Cert. 69a. The Magistrate
Judge therefore recommended the case be dismissed without
prejudice for failure to exhaust. Id., at 76a. The District
Court adopted the recommendation. Id., at 28a–29a.

                               C
  Richards appealed to the Sixth Circuit. Still representing
himself, he argued that resolving exhaustion through “a
                   Cite as: 605 U. S. 460 (2025)             467

                      Opinion of the Court

bench trial”—one before a judge without a jury—is “not per-
missible where it would essentially be resolving a claim it-
self.” Brief for Appellant in No. 22–1298, p. 1. After ap-
pointing counsel for Richards and requesting supplemental
briefng, the Sixth Circuit reversed. It acknowledged that,
under Circuit precedent, there was “no doubt that a judge
may otherwise resolve factual disputes regarding exhaustion
under the PLRA.” 96 F. 4th 911, 917 (2024) (citing Lee v.
Willey, 789 F. 3d 673, 677 (CA6 2015)). But the court held
that “the Seventh Amendment requires a jury trial when the
resolution of the exhaustion issue under the PLRA would
also resolve a genuine dispute of material fact regarding the
merits of the plaintiff's substantive case.” 96 F. 4th, at 923.
That decision conficted with a contrary holding on the same
question from the Seventh Circuit, see Pavey v. Conley, 544
F. 3d 739, 742 (2008), and we granted certiorari to resolve
the split. 603 U. S. 949 (2024).

Page Proof Pending
             II    Publication
   “The right to trial by jury is `of such importance and occu-
pies so frm a place in our history and jurisprudence that any
seeming curtailment of the right' has always been and
`should be scrutinized with the utmost care.' ” SEC v. Jark-
esy, 603 U. S. 109, 121 (2024) (quoting Dimick v. Schiedt, 293
U. S. 474, 486 (1935)). Richards makes two arguments for
why his Seventh Amendment right to a jury trial has been
violated here. First, he argues that the dispute over ex-
haustion in this case is intertwined with a claim that falls
squarely under the Seventh Amendment—his First Amend-
ment retaliation claim for damages under § 1983—and that
factual questions related to that claim must be resolved by
a jury. See Monterey v. Del Monte Dunes at Monterey,
Ltd., 526 U. S. 687, 709, 720–721 (1999) (holding that “a § 1983
suit seeking legal relief is an action at law within the mean-
ing of the Seventh Amendment” and that a “predominantly
factual question” in such an action is “for the jury”). Sec-
468                 PERTTU v. RICHARDS

                      Opinion of the Court

ond, Richards makes a broader argument that, based on the
historical test in Markman v. Westview Instruments, Inc.,
517 U. S. 370 (1996), the Seventh Amendment requires a jury
trial for all factual disputes related to PLRA exhaustion,
even those not intertwined with the merits.
   Our precedents make clear that “[b]efore inquiring into
the applicability of the Seventh Amendment, we must `frst
ascertain whether a construction of the statute is fairly
possible by which the [constitutional] question may be
avoided.' ” Del Monte Dunes, 526 U. S., at 707 (quoting Felt-
ner v. Columbia Pictures Television, Inc., 523 U. S. 340, 345
(1998)). Such a construction is possible here. PLRA ex-
haustion is an affrmative defense subject to “the usual prac-
tice under the Federal Rules [of Civil Procedure].” Jones,
549 U. S., at 212. The usual practice is that factual disputes
regarding the merits of a legal claim go to the jury, even if
that means a judge must let a jury decide questions he could
Page Proof Pending Publication
ordinarily decide on his own. See Beacon Theatres, Inc. v.
Westover, 359 U. S. 500, 510–511 (1959). That usual practice
matters for interpreting the statute because “Congress is un-
derstood to legislate against a background of common-law
adjudicatory principles . . . with an expectation that the prin-
ciple[s] will apply except `when a statutory purpose to the
contrary is evident.' ” Astoria Fed. Sav. & Loan Assn. v.
Solimino, 501 U. S. 104, 108 (1991) (quoting Isbrandtsen Co.
v. Johnson, 343 U. S. 779, 783 (1952)). No such contrary pur-
pose is evident in the PLRA.
   For those reasons, we hold as a matter of statutory inter-
pretation that parties have a right to a jury trial on PLRA
exhaustion when that issue is intertwined with the merits of
a claim that falls under the Seventh Amendment. In light
of this holding, we express no view today on whether Con-
gress could have required otherwise in the PLRA without
violating a party's Seventh Amendment right to a jury trial.
See Byrd v. Blue Ridge Rural Elec. Cooperative, Inc., 356
U. S. 525, 537, and n. 10 (1958) (holding that affrmative de-
                       Cite as: 605 U. S. 460 (2025)                    469

                           Opinion of the Court

fense should go to jury due to “the manner in which [the
federal system] distributes trial functions between judge and
jury,” making it “unnecessary” to consider “the constitu-
tional question”).1
                               A
   We begin with a settled premise: PLRA exhaustion is a
standard affrmative defense. Jones, 549 U. S., at 216. As
we said in Woodford, 548 U. S., at 101, PLRA exhaustion is
“not jurisdictional,” which is why “a district court [is al-
lowed] to dismiss plainly meritless claims without frst ad-
dressing” the often “more complex question” of exhaustion.
And as we said in Jones, 549 U. S., at 216, PLRA exhaustion
is not a “pleading requirement,” which is why “inmates are
not required to specially plead or demonstrate exhaustion in
their complaints.” Rather, PLRA exhaustion is an “affrm-
ative defense” subject to “the usual practice under the Fed-
eral Rules.” Id., at 212. And that usual practice applies,
Page Proof Pending Publication
Jones explained, even though the PLRA is “silent on the
issue,” because that silence is itself “strong evidence that the
usual practice should be followed.” Ibid.
   The PLRA is similarly “silent on the issue” whether
judges or juries should resolve factual disputes related to
exhaustion. The exhaustion provision states simply that
“[n]o action shall be brought with respect to prison condi-
   1
     The dissent criticizes us for asking whether we can avoid the constitu-
tional question by answering the statutory one. Post, at 484–486, and
n. 3 (Barrett, J., dissenting). But we have described doing exactly that
as a “cardinal principle.” Tull v. United States, 481 U. S. 412, 417, n. 3
(1987). The dissent suggests the principle does not apply here because
the parties did not raise it and the courts below did not address it. But
the same was true in Tull, yet we still began by asking whether it was
possible to read the statute to avoid the constitutional question, and moved
on only after concluding the answer was no. Surely we should not deviate
from that principle simply because our answer this time is yes. And in
this case, the statutory question has been fully briefed by amici and in-
volves the same precedents relied on by the parties. See Brief for Law
Professors as Amici Curiae 8–15.
470                     PERTTU v. RICHARDS

                          Opinion of the Court

tions . . . until such administrative remedies as are available
are exhausted.” 42 U. S. C. § 1997e(a). Perttu does not
argue that this provision requires that exhaustion disputes
be resolved by judges. And rightly so. As we noted in
Jones, the phrase “[n]o action shall be brought” is “boiler-
plate language” often used for other affrmative defenses,
like statutes of limitations, 549 U. S., at 220, that routinely
go to the jury. And “failure to exhaust was notably not
added” to the PLRA's screening provisions, which require
judges to dismiss cases on specifed grounds. Id., at 214.
   Just like in Jones, then, the statutory silence on the ques-
tion before us “is strong evidence that the usual practice
should be followed.” Id., at 212; see also Dixon v. United
States, 548 U. S. 1, 17 (2006) (“In light of Congress' silence
on the issue . . . it is up to the federal courts to effectuate
the affrmative defense . . . as Congress may have contem-
plated it . . . given the long-established common-law rule.”
(internal quotation marks omitted)). We therefore look to
Page Proof Pending Publication
the usual practice for resolving factual disputes intertwined
with the merits.2
                                B
  The PLRA was enacted in 1996. By that time, it was well
established that when a factual dispute is intertwined with
the merits of a claim that falls under the Seventh Amend-
ment, that dispute should go to a jury, even if that requires
judges to defer determinations they would ordinarily make
on their own. We have accordingly held in various contexts

   2
     The dissent thinks this should be an even “easier case” than Tull and
others where we concluded that a statute did not confer a jury trial right.
Post, at 488. But our analysis in this case is that “the usual practice
should be followed,” Jones v. Bock, 549 U. S. 199, 212 (2007), and that the
usual practice in cases of intertwinement is to send the question to the
jury, see Beacon Theatres, Inc. v. Westover, 359 U. S. 500, 510–511 (1959);
see also post, at 490 (recognizing that Beacon Theatres establishes a “gen-
eral prudential rule”). Tull and the other cases did not implicate a prac-
tice or rule like Beacon Theatres that itself calls for a jury trial.
                   Cite as: 605 U. S. 460 (2025)             471

                      Opinion of the Court

that, in cases of intertwinement, district courts should struc-
ture their order of operations to preserve the jury trial right.

                                1
   One prominent line of cases involves suits that contain
both legal and equitable claims. Ordinarily, judges resolve
equitable claims and juries resolve legal claims. But in Bea-
con Theatres, 359 U. S., at 510–511, we held that judges may
not resolve equitable claims frst if doing so could prevent
legal claims from getting to the jury.
   Beacon Theatres involved an antitrust dispute between
two movie theater companies. One company brought an eq-
uitable claim for a declaratory judgment that it had not vio-
lated antitrust laws. The other company brought a legal
claim for money damages alleging that the frst company had
violated antitrust laws. Both the equitable and legal claims
therefore hinged on the “common issue” whether there was
Page Proof Pending Publication
an antitrust violation. Id., at 503. Faced with this di-
lemma, we emphasized that, while judges ordinarily have
“discretion in deciding whether the legal or equitable cause
should be tried frst,” “that discretion is very narrowly lim-
ited and must, wherever possible, be exercised to preserve
jury trial.” Id., at 510; see also id., at 510–511 (“[O]nly
under the most imperative circumstances, circumstances
which in view of the fexible procedures of the Federal Rules
we cannot now anticipate, can the right to a jury trial of
legal issues be lost through prior determination of equitable
claims.” (footnote omitted)). The consequence in that case
was clear: Because resolving the equitable claims could “pre-
vent a full jury trial” on the legal claims, the legal claims
needed to be resolved by a jury frst. Id., at 505, 508. The
district court's decision to instead resolve the equitable
claims frst was therefore “not permissible.” Id., at 508.
   Later cases confrm that Beacon Theatres should be read
“expansively,” applying to any claim triable by a jury even
“in a suit in which the basic relief sought is equitable.” 9 C.
472                 PERTTU v. RICHARDS

                      Opinion of the Court

Wright & A. Miller, Federal Practice and Procedure § 2302.1,
pp. 33–34 (4th ed. 2020). For example, in Dairy Queen, Inc.
v. Wood, 369 U. S. 469, 473, 475 (1962), the plaintiff alleged
that the defendant had breached a contract for use of the
trademark “Dairy Queen,” and the plaintiff sought both legal
and equitable relief. We observed that the legal and equita-
ble claims therefore depended on “common” “factual issues
related to the question of whether there [had] been a breach
of contract.” Id., at 479. For that reason, the consequence
was again clear: “[T]he district judge erred in refusing to
grant petitioner's demand for a trial by jury.” Ibid.
   In this case, the parties agree that the exhaustion and
First Amendment questions depend on common factual is-
sues. And Beacon Theatres teaches that a trial court's dis-
cretion in such a situation is “very narrowly limited and
must, wherever possible, be exercised to preserve jury trial.”
359 U. S., at 510. Nothing in the PLRA prevents holding a
jury trial here.
Page Proof Pending Publication2
  Our cases involving subject matter jurisdiction are also
instructive. Ordinarily, judges may resolve factual disputes
in the course of determining whether subject matter juris-
diction is proper. See Wetmore v. Rymer, 169 U. S. 115,
120–121 (1898). But we have long held that a court may
not do so when the factual disputes are intertwined with
the merits.
  For example, in Smithers v. Smith, 204 U. S. 632, 641–642
(1907), the district court concluded that it lacked subject
matter jurisdiction because the case did not meet the $2,000
amount-in-controversy requirement. The district court did
so, however, by fnding that even if the defendants had each
taken a part of the plaintiff 's land—as the plaintiff alleged—
the defendants had not acted jointly, and so the aggregate
amount in controversy did not exceed $2,000. Id., at 645–
646. We reversed because we found that, in arriving at this
conclusion, the district court had decided a factual question
that was “an essential element of the merits of the dispute”—
                    Cite as: 605 U. S. 460 (2025)             473

                       Opinion of the Court

whether the defendants had acted jointly—and so had “in
effect, decided the controversy between the parties upon the
merits.” Id., at 646. We acknowledged that judges ordi-
narily have “the authority to dismiss [an] action [for lack of
subject matter jurisdiction] without trial by jury.” Id., at
644–645. But we held that this authority “obviously is not
unlimited,” “lest under the guise of determining jurisdiction
the merits of the controversy between the parties be sum-
marily decided without the ordinary incidents of a trial, in-
cluding the right to a jury.” Id., at 645.
   We applied similar analysis in Land v. Dollar, 330 U. S.
731 (1947). There the district court concluded that it lacked
subject matter jurisdiction due to sovereign immunity, be-
cause the suit for unlawful possession of stock shares by fed-
eral offcials was in fact a suit “against the United States.”
Id., at 734. We recognized that “as a general rule the Dis-
trict Court would have authority to consider questions of
jurisdiction.” Id., at 735. But we found that Land was
Page Proof Pending Publication
“the type of case where the question of jurisdiction is de-
pendent on decision of the merits,” because both questions
hinged on the plaintiffs' claims that “the shares of stock
never were property of the United States.” Id., at 735, 738.
We therefore held that the district court should have “pro-
ceed[ed] to a decision on the merits” rather than resolve the
jurisdictional issue at a preliminary stage. Id., at 739. See
Gulf Oil Corp. v. Copp Paving Co., 419 U. S. 186, 203, n. 19
(1974) (acknowledging practice of “reserving the jurisdic-
tional issues” when there is “an identity between the `juris-
dictional' issues and certain issues on the merits”); see also
8 J. Moore, D. Coquillette, G. Joseph, G. Vairo, & C. Varner,
Moore's Federal Practice § 38.34[1][c][i], p. 38–154 (3d ed.
2024) (Moore); 5B C. Wright, A. Miller, & A. Spencer, Fed-
eral Practice and Procedure § 1350, pp. 224–226 (4th ed.
2024).
   In its decision below, the Sixth Circuit relied on its Circuit
precedent applying Land, reasoning that if “certain cases
[must] be heard and determined on the merits even when
474                  PERTTU v. RICHARDS

                       Opinion of the Court

constitutionally implicated jurisdictional disputes” are at
play, then “the result should be the same when the lesser
concern of an affrmative defense, such as the PLRA's re-
quirement to exhaust administrative remedies, implicates
the merits of a claim.” 96 F. 4th, at 923 (citing Fireman's
Fund Ins. Co. v. Railway Express Agency, Inc., 253 F. 2d
780, 784 (CA6 1958)). We fnd that reasoning persuasive.
After all, when the PLRA was enacted, many lower court
decisions and treatises had extended the intertwinement
principle to other threshold questions, including personal ju-
risdiction, venue, choice of law, and forum non conveniens.
See, e. g., 5 J. Moore et al., Moore's Federal Practice ¶38.36[3],
p. 38–341 (2d ed. 1996) (“[T]o determine that the alleged acts
did not take place . . . on motion to dismiss for want of proper
venue would be to deny the plaintiff a jury trial on the mer-
its.”); see also 8 Moore §§ 38.34[1][e], [2], [3] (3d ed. 2024).
We express no view today on whether lower courts have
been correct to extend the intertwinement principle to these
Page Proof Pending Publication
other issues. We simply note that these cases—along with
Beacon Theatres and Smithers—show that when the PLRA
was enacted, the usual practice in the federal courts across
a variety of contexts was to resolve factual disputes that are
intertwined with the merits at the merits stage. The
PLRA's complete silence on that question is therefore
“strong evidence” that this “usual practice should be fol-
lowed.” Jones, 549 U. S., at 212.

                                C
   Perttu offers important counterarguments, but we are ul-
timately not persuaded. First, Perttu argues that Beacon
Theatres is inapplicable here. According to Perttu, the con-
cern in Beacon Theatres was that judicial resolution of the
equitable claims would have had collateral estoppel effect on
the legal claims. But here, Perttu says, the judge's factual
fndings related to exhaustion would have no such effect in a
later jury trial.
                        Cite as: 605 U. S. 460 (2025)                      475

                            Opinion of the Court

   Two Circuits have suggested they agree with Perttu that
factual fndings related to exhaustion have no estoppel effect,
but with little analysis and in cases that did not squarely
present an estoppel issue. See Pavey, 544 F. 3d, at 742; Al-
bino v. Baca, 747 F. 3d 1162, 1171 (CA9 2014). Legal trea-
tises, on the other hand, provide support for the proposition
that factual determinations in a frst action can have direct
estoppel effect in a second action on the same claim. See
Restatement (Second) of Judgments § 27, Comment b, Illus-
tration 3, Comment d, pp. 251–255 (1980); 18 C. Wright, A.
Miller, & E. Cooper, Federal Practice and Procedure § 4418,
pp. 505–506 (3d ed. 2016). The Restatement gives an exam-
ple analogous to the situation before us: If a court dismisses
a case for lack of personal jurisdiction based on a particular
factual fnding, that factual fnding has preclusive effect in a
subsequent action on issues beyond just personal jurisdic-
tion. Restatement (Second) of Judgments § 27, Illustration
Page Proof Pending Publication
3, p. 252.3 Perttu also overlooks the fact that, if the judge
below had ruled that Perttu did destroy Richards's griev-
ances, then Perttu himself may have been precluded from
relitigating that issue before the jury under law of the case.
See 18B C. Wright, A. Miller, & E. Cooper, Federal Practice
and Procedure § 4478.5, p. 773 (3d ed. 2019).
   We therefore cannot reject the possibility that a judicial
ruling on PLRA exhaustion might have estoppel effect in a
later jury trial. And Beacon Theatres shows that the
proper path in that situation is to hold the jury trial, not to
change the estoppel rules. See Parklane Hosiery Co. v.
Shore, 439 U. S. 322, 333 (1979) (“Recognition that an equita-
ble determination could have collateral-estoppel effect in a

   3
     See also, e. g., Carr v. Tillery, 591 F. 3d 909, 917 (CA7 2010) (“[A] dis-
missal can be without prejudice yet have preclusive effect.”); Deutsch v.
Flannery, 823 F. 2d 1361, 1364 (CA9 1987) (“It matters not that the prior
action resulted in a dismissal without prejudice, so long as the determina-
tion being accorded preclusive effect was essential to the dismissal.”).
476                     PERTTU v. RICHARDS

                          Opinion of the Court

subsequent legal action was the major premise of this
Court's decision in Beacon Theatres.”).4
   Regardless, even if Perttu is right that factual fndings
concerning exhaustion have no estoppel effect in a later jury
trial, we decline to limit Beacon Theatres artifcially to cases
involving estoppel. The problem in Beacon Theatres was
that judicial resolution of a “common issue” might have “pre-
vent[ed] a full jury trial” on the legal claims. 359 U. S., at
503, 505, 508. Estoppel was simply the reason why a “full
jury trial” might have been “prevent[ed]” in that case. Id.,
at 505 (“[T]o try the equitable cause frst . . . might, through
collateral estoppel, prevent a full jury trial.” (emphasis
added)). The principle of Beacon Theatres still applies
when judicial resolution of a common issue might “prevent a
full jury trial” for some reason other than estoppel. And
here, that other reason is clear. Instead of just being es-
topped, Richards's claim is being dismissed entirely. We
therefore agree with the Sixth Circuit's reasoning: Even as-
Page Proof Pending Publication
suming Perttu is right that a jury may “reexamine the
judge's factual fndings,” that “rationale” “rings hollow if the
prisoner's case is dismissed for failure to exhaust,” because
“[i]n such an instance, a jury would never be assembled to
resolve the factual disputes.” 96 F. 4th, at 921.
   It is no answer, in our view, to say that a prisoner might
someday get a jury by starting over, exhausting the griev-
ance procedures, then refling his lawsuit. After all, that
path is impossible in most cases. As Perttu acknowledged
at oral argument, “the time frames for . . . grievances are
very short”— on the order of days. Tr. of Oral Arg. 35; see,

  4
   The dissent reads this “major premise” language from Parklane as
suggesting that Beacon Theatres is all about estoppel. Post, at 491. But
the question in Parklane was whether a prior equitable ruling could have
estoppel effect in a subsequent legal action, and Parklane simply pointed
out that Beacon Theatres believed it could—i.e., that Beacon Theatres
took that fact as a “major premise” then reasoned from there. That logic
does not imply that Beacon Theatres is limited to cases involving estoppel.
                         Cite as: 605 U. S. 460 (2025)                     477

                            Opinion of the Court

e. g., Jones, 549 U. S., at 207 (grievance deadlines of 2 to 5
days); Woodford, 548 U. S., at 95–96 (grievance deadlines of
14 to 30 days). By the time a case is dismissed for failure
to exhaust, grievance deadlines will have long since passed.
But Perttu makes no argument that such deadlines are tolled
in these situations. Instead, he points to the fact that prison
administrators in some (but not all) jurisdictions have discre-
tion to excuse missed grievance deadlines, with no evidence
of how often administrators actually exercise that discretion,
let alone in cases where—as here—doing so would foresee-
ably set up a second lawsuit. And though Perttu makes a
different argument for why Richards could exhaust and refle
in this case,5 he does not argue that courts should treat indi-
vidual cases of intertwinement differently based on whether
a particular party in a given case might one day get to a
jury. See Beacon Theatres, 359 U. S., at 504 (concern at
  5
      Perttu argues that Richards remains able to exhaust because his alle-
Page          Proof
gations fall under  the PrisonPending
                                Rape Elimination ActPublication
                                                        of 2003 (PREA), 117
Stat. 972, 34 U. S. C. § 30301 et seq., and federal regulations prevent pris-
ons from imposing deadlines on PREA grievances regarding sexual abuse.
Reply Brief 14 (citing 28 CFR § 115.52(b)(1) (2024)). Accordingly, Perttu
says, the PREA policy applicable in the State of Michigan when Richards
fled suit did not bar him from fling new grievances. See App. 75 (“A
prisoner may fle a PREA grievance at any time.”). Richards, however,
says “[t]his is the frst time in this fve years of litigation that [Perttu] has
represented that . . . all of [Richards's] claims might be able to be ex-
hausted.” Tr. of Oral Arg. 51. Richards also says that his “First Amend-
ment claim . . . is not protected by the PREA policy.” Id., at 51–52;
see also App. 76 (“Any PREA grievance containing multiple issues, which
include sexual abuse and non-sexual abuse issues, shall be processed . . .
to address the allegations of sexual abuse only.”). We take no position on
this dispute.
  Perttu also notes that the Michigan Department of Corrections has since
amended its PREA policy to “eliminat[e] the administrative grievance pro-
cedure for addressing prisoner grievances regarding sexual abuse.”
Reply Brief 14, n. 3. We take no position on whether this new policy
covers Richards's First Amendment claim or whether there are other ad-
ministrative remedies that Richards would need to exhaust before fling a
subsequent action.
478                 PERTTU v. RICHARDS

                      Opinion of the Court

issue arises when prior determination by judge “might” de-
prive party of jury trial); id., at 505 (same).
   Finally, Perttu argues that requiring a jury trial here
would confict with the purpose of PLRA exhaustion, which
is to conserve judicial resources by preventing unexhausted
claims from going to trial. For support, Perttu cites our
decision in Katchen v. Landy, 382 U. S. 323 (1966). There
we held that a bankruptcy court could proceed to decide an
equitable claim—even if similar issues might one day arise
before a jury on a legal claim—because to prevent the equita-
ble claim from being “tried in the bankruptcy court in the
normal manner” would be “to dismember a scheme which
Congress has prescribed.” Id., at 339.
   But Katchen is clearly far afeld. That case involved
a “specifc statutory scheme”—bankruptcy—“contemplating
the prompt trial of a disputed claim without the intervention
of a jury” in a special set of courts created for that purpose.
Page Proof Pending Publication
Ibid. The equivalent “statutory scheme” here—the
PLRA—contemplates that Richards's First Amendment
claim will be resolved by a jury and is silent about whether
a jury should resolve exhaustion.
   Perttu responds that holding a jury trial on exhaustion
nonetheless conficts with congressional intent because the
point of PLRA exhaustion is to ensure that only exhausted
claims go to trial. But that objection would apply with even
greater force in Smithers and Land, because—by the same
logic—holding a trial on subject matter jurisdiction would
confict with the purpose of ensuring that trials happen only
where jurisdiction is proper. See Ex parte McCardle, 7
Wall. 506, 514 (1869) (“Without jurisdiction the court cannot
proceed at all in any cause.”). Yet Smithers and Land show
that, in cases of intertwinement, the proper practice is in-
deed to go to trial. We therefore cannot agree with Perttu
that the PLRA's general interest in conserving judicial re-
sources shows that Congress clearly intended for judges to
resolve exhaustion disputes in this unique circumstance.
                   Cite as: 605 U. S. 460 (2025)            479

                     Barrett, J., dissenting

                         *      *      *
   If Congress had expressly provided in the PLRA that ex-
haustion disputes must be resolved by judges, then we would
have been required to consider today whether such a provi-
sion violates the Seventh Amendment. But it is a “cardinal
principle” that we not address such a constitutional question
unless necessary. Tull v. United States, 481 U. S. 412, 417,
n. 3 (1987). Meanwhile, as we have shown, the usual prac-
tice of the federal courts in cases of intertwinement is to
send common issues to the jury. Because nothing in the
PLRA suggests Congress intended to depart from that prac-
tice here, we hold that parties are entitled to a jury trial on
PLRA exhaustion when that issue is intertwined with the
merits of a claim protected by the Seventh Amendment.
   The judgment of the United States Court of Appeals for
the Sixth Circuit is affrmed.
                                              It is so ordered.
Page
 Justice Proof    Pending
         Barrett, with            Publication
                       whom Justice Thomas, Justice
Alito, and Justice Kavanaugh join, dissenting.
  The Prison Litigation Reform Act of 1995 (PLRA) re-
quires prisoners suing under 42 U. S. C. § 1983 to frst ex-
haust the administrative remedies that are “available” to
them. § 1997e(a). In the decision below, the Sixth Circuit
held that even if prisoners are not ordinarily entitled to a
jury trial to resolve this threshold question, the Seventh
Amendment requires a jury when exhaustion is intertwined
with the merits. I would reverse. The jury right con-
ferred by the Seventh Amendment does not depend on the
degree of factual overlap between a threshold issue and the
merits of the plaintiff's claim.
  The Court takes a different path. Instead of resolving
the constitutional question that the parties brought to us,
the Court holds that the PLRA itself requires a jury trial
whenever an issue is common to exhaustion and the merits.
No matter, the Court says, that the PLRA is silent on the
480                 PERTTU v. RICHARDS

                     Barrett, J., dissenting

subject. No matter that this statutory argument was not
briefed before us. And no matter that it was not passed on
by the courts below.
  Having taken this detour, the Court ends up in the wrong
place. Reading the PLRA's silence to implicitly confer a
right to a jury trial contravenes not only basic principles
of statutory interpretation, but also several of this Court's
precedents. I respectfully dissent.

                               I
   Kyle Richards, a state prisoner, sued Thomas Perttu, a
prison employee, for damages under § 1983. Richards al-
leged two bases for relief: First, he alleged that Perttu had
sexually harassed several inmates, including Richards. And
second, Richards alleged that when he had attempted to fle
grievances reporting the harassment, Perttu had retaliated
in several ways, including by destroying Richards's griev-
Page Proof Pending Publication
ance forms. See ante, at 465–466. Richards claimed that
Perttu's initial harassment and subsequent retaliation vio-
lated the Eighth and First Amendments, respectively. See
App. 18.
   Because a damages suit under § 1983 is a “Sui[t] at common
law,” all agree that the Seventh Amendment entitles Rich-
ards to a jury trial on the merits of his claims. U. S. Const.,
Amdt. 7 (“In Suits at common law, where the value in contro-
versy shall exceed twenty dollars, the right of trial by jury
shall be preserved”); see Monterey v. Del Monte Dunes at
Monterey, Ltd., 526 U. S. 687, 720–721 (1999). To litigate
the merits, however, the PLRA requires Richards to estab-
lish that he exhausted “such administrative remedies as are
available” to him. § 1997e(a). Whether Richards did so
turns on a factual dispute about the availability of his admin-
istrative remedies. According to Richards, Perttu's de-
struction of Richards's grievances rendered the prison griev-
ance system “unavailable” for purposes of the PLRA. Ross
v. Blake, 578 U. S. 632, 644 (2016). Perttu, for his part, in-
                      Cite as: 605 U. S. 460 (2025)                  481

                        Barrett, J., dissenting

sists that he did not destroy Richards's grievances; thus, he
says, the system was available to Richards and Richards's
failure to fle grievances dooms his § 1983 claims. See
§ 1997e(a).
   This dispute about the facts engendered another about the
law—and more specifcally, about the role of the jury. The
PLRA itself says nothing about the right to a jury trial on
the question of exhaustion. And all the circuits to have con-
sidered the question hold that the Seventh Amendment does
not require one. So the consensus rule in the courts of ap-
peals has been that PLRA exhaustion can be resolved
through a bench trial.1
   Although the Sixth Circuit has long embraced this rule,
see Lee v. Willey, 789 F. 3d 673, 678 (2015), Richards argued
that his case was special—and the Sixth Circuit agreed. An
exception applies, it held, “when the resolution of the exhaus-
tion issue . . . would also resolve a genuine dispute of mate-
rial fact regarding the merits of the plaintiff's substantive
Page Proof Pending Publication
case.” 96 F. 4th 911, 923 (2024). In such cases, the Sixth
Circuit held, the Seventh Amendment entitles the parties to
a jury. That holding broke with the decisions of the Seventh
and Ninth Circuits, both of which have rejected a factual-
overlap exception. See Pavey v. Conley, 544 F. 3d 739, 742
(CA7 2008); Albino v. Baca, 747 F. 3d 1162, 1171 (CA9 2014)
(en banc) (agreeing with Pavey in dicta).

                                   II
  Having granted certiorari to resolve this split, I would re-
verse. The jury-trial right conferred by the Seventh
Amendment does not turn on the degree of factual overlap
  1
    See Messa v. Goord, 652 F. 3d 305, 308–310 (CA2 2011) (per curiam);
Small v. Camden Cty., 728 F. 3d 265, 269–271 (CA3 2013); Dillon v. Rog-
ers, 596 F. 3d 260, 271 (CA5 2010); Lee v. Willey, 789 F. 3d 673, 677–678
(CA6 2015); Pavey v. Conley, 544 F. 3d 739, 741–742 (CA7 2008); Albino v.
Baca, 747 F. 3d 1162, 1170–1171 (CA9 2014) (en banc); Bryant v. Rich, 530
F. 3d 1368, 1373–1377 (CA11 2008).
482                      PERTTU v. RICHARDS

                          Barrett, J., dissenting

between a threshold question and the merits of the plain-
tiff 's claim.
   Because the Seventh Amendment provides that the “ `right
of trial by jury shall be preserved,' ” it protects “ `the right
which existed under the English common law when the
Amendment was adopted.' ” Markman v. Westview Instru-
ments, Inc., 517 U. S. 370, 376 (1996). In actions that would
have been tried at law at the founding, such as this one, the
question is whether the “particular trial decision” at issue
“must fall to the jury in order to preserve the substance of
the common-law right as it existed in 1791.” Ibid.
   The parties devote much of their time to debating the best
founding-era analogue to the exhaustion defense. Accord-
ing to Richards, exhaustion is analogous to common-law de-
fenses that would have been raised through a plea in bar.2
Under the common-law pleading system, Richards argues,
the parties' dueling pleas would isolate disputed points of
law and fact, with the former allocated to a judge and the
Page Proof Pending Publication
latter allocated to a jury. See H. Stephen, Principles of
Pleading in Civil Actions 59–61 (1882); B. Shipman, Hand-
book of Common-Law Pleading § 15, p. 32 (3d ed. 1923).
Perttu, on the other hand, grounds exhaustion in traditional
equitable practice. In his view, an exhaustion defense most
closely resembles a defensive equitable action to enjoin a
lawsuit—an action that would have been heard by the chan-
cellor, not a jury. Liberty Oil Co. v. Condon Nat. Bank, 260
U. S. 235, 242–243 (1922).
   The Court does not get into this back-and-forth—and here,
I agree with the Court. We did not take this case to deter-
mine whether the Seventh Amendment requires jury trials
for all disputes about exhaustion. There is no circuit split
on that question, and the court below did not address it.
   2
     Richards relies primarily on the plea in discharge, a type of plea in bar
that applies when the plaintiff 's cause of action has been “discharged by
some matter subsequent, either of fact or of law.” B. Shipman, Handbook
of Common-Law Pleading § 198b, p. 348 (3d ed. 1923).
                   Cite as: 605 U. S. 460 (2025)            483

                     Barrett, J., dissenting

(Recall that under binding Sixth Circuit precedent, there is
generally no Seventh Amendment right to a jury trial for
exhaustion disputes. See Lee, 789 F. 3d, at 678.) The ques-
tion, moreover, might be very diffcult. Neither party iden-
tifes an obvious analogue to exhaustion, a defense that de-
veloped long after the founding. See R. Berger, Exhaustion
of Administrative Remedies, 48 Yale L. J. 981, and n. 1 (1939).
Resolving the dispute would therefore require us to confront
challenging historical and methodological questions: Did the
Seventh Amendment constitutionalize common-law pleading
rules? Does Congress have the authority, after the merger
of law and equity, to fashion novel defenses as “equitable”?
What presumption applies when the historical evidence is
ambiguous? It would be unwise to address these questions
before the lower courts have seriously considered them.
   Answering the question presented, however, would not
have required us to resolve these knotty issues. We granted
Page Proof Pending Publication
certiorari to decide the same limited issue that the Sixth
Circuit decided: whether a special Seventh Amendment rule
applies when a factual dispute about exhaustion is inter-
twined with the merits. And on this question, the historical
record is much clearer. Richards has presented no evidence
that intertwinement with the merits was relevant to the
jury-trial right. Instead, he simply repeats his broader his-
torical argument: that factual disputes raised through pleas
were heard by juries. But this was true regardless of
whether the dispute overlapped with the merits. See, e. g.,
Wetmore v. Rymer, 169 U. S. 115, 120–123 (1898) (describing
“trial[s] had with a jury” over subject-matter jurisdiction).
Likewise, Perttu's account does not implicate intertwine-
ment. All equitable defenses were heard by “the judge as
a chancellor” because they were freestanding equitable ac-
tions. Liberty Oil, 260 U. S., at 242–243; see W. Cook, Equi-
table Defenses, 32 Yale L. J. 645, 650–652 (1922–1923).
   The upshot is that there is no historical support for a spe-
cial intertwinement rule. Mere factual overlap with the
484                      PERTTU v. RICHARDS

                          Barrett, J., dissenting

merits does not transform a collateral issue ordinarily re-
solved by a court into one necessarily resolved by a jury.
We could have corrected that constitutional error and saved
the broader, more complicated debate for another day.
                              III
   Remarkably, in this Seventh Amendment case, the Court
has nothing to say about the Seventh Amendment. In fact,
the Court sets the Constitution entirely aside, “express[ing]
no view” on how or when it demands that a jury resolve
intertwined factual disputes. Ante, at 468–469. Left with
nothing else to interpret, the Court pivots to the PLRA.
True, the Court acknowledges, the PLRA says nothing about
the role of the jury—and certainly nothing about the role of
the jury in resolving disputes about exhaustion. But as a
matter of statutory interpretation and “ `common-law adjudi-
catory principles,' ” the Court holds that the PLRA nonethe-
less requires a jury trial when a dispute about exhaustion is
Page Proof Pending Publication
“intertwined with the merits” of the plaintiff 's claim. Ante,
at 468.
   This is wrong several times over. Richards did not pres-
ent this statutory theory to us or any other court; the PLRA
does not confer a jury right through its silence; and the
Court plucks its purported “common-law adjudicatory princi-
ple” out of thin air. I take each point in turn.
                             A
  To begin, the Court spins a statutory theory that Richards
has never even mentioned, much less developed.3 Before us,
   3
     The avoidance canon permits a court to choose a less plausible interpre-
tation of a statute when the most natural one would provoke a “ `serious' ”
constitutional question. Zadvydas v. Davis, 533 U. S. 678, 689 (2001).
Though the Court invokes the canon in this case, it is unwilling to say that
interpreting the PLRA to permit a court to resolve Richards's exhaustion
defense would pose a “serious” constitutional question. This reticence
is presumably attributable to the scant historical support for Richards's
proposed intertwinement rule. Even if the canon applied, moreover, the
                     Cite as: 605 U. S. 460 (2025)               485

                       Barrett, J., dissenting

Richards argues only that he has a constitutional right to a
jury trial. Both his Brief in Opposition and his merits brief
focus exclusively on the Seventh Amendment. See Brief for
Respondent 3 (“[T]he Seventh Amendment clearly protects
Respondent's right to jury resolution of disputed historical
facts central to the merits of his legal claim”); Brief in Oppo-
sition 1 (“The Sixth Circuit correctly held that [the District
Court's] process violated the Seventh Amendment”). The
same was true below. In the District Court, Richards's ar-
gument turned on the proper application of circuit prece-
dent—precedent that has everything to do with the Seventh
Amendment and nothing to do with the PLRA. See Objec-
tions and Request for Review in No. 2:20–cv–00076 (WD
Mich., Aug. 6, 2021), ECF Doc. 102, p. 2; Lee, 789 F. 3d, at
678. Following Richards's lead, the District Court likewise
focused on the Seventh Amendment. 2021 WL 3508384, *2
(WD Mich., Aug. 10, 2021) (“[T]he Seventh Amendment right
to a jury trial [does] not extend to the exhaustion question”).
Page Proof Pending Publication
On appeal in the Sixth Circuit, Richards continued to press
the same Seventh Amendment argument. Brief for Appel-
lant in No. 22–1298, p. 2; see generally Supplemental Brief
for Appellant in No. 22–1289. So, no surprise, the Sixth Cir-
cuit addressed only the Seventh Amendment. See 96 F. 4th,
at 923 (“[T]he Seventh Amendment requires a jury trial
when the resolution of the exhaustion issue under the PLRA
would also resolve a genuine dispute of material fact regard-
ing the merits of the plaintiff 's substantive case”).
   In light of this procedural history, the Court's path is per-
plexing. We typically refuse to consider arguments that the
parties failed to make before us. See Reno v. American
Civil Liberties Union, 521 U. S. 844, 863, n. 30 (1997). Like-
wise, “we normally decline to entertain . . . arguments” that
a party “failed to raise . . . in the courts below.” Kingdom-
ware Technologies, Inc. v. United States, 579 U. S. 162, 173
chosen interpretation must be plausible—and, as I explain in the next
Part, the Court's interpretation most certainly is not.
486                   PERTTU v. RICHARDS

                      Barrett, J., dissenting

(2016). And we regularly emphasize that “we are a court of
review, not of frst view,” so we generally do not address
issues that the court of appeals did not analyze frst. Cutter
v. Wilkinson, 544 U. S. 709, 718, n. 7 (2005). (Making mat-
ters worse, it is not clear that any court has considered the
statutory question the Court resolves today.) Apparently,
these party-presentation principles have no purchase here.
Without any prompting from the parties, the Court devises
and embraces a theory that Richards himself never raised—
all, ironically enough, to save his case from dismissal for an
alleged failure to exhaust.
                               B
   Nor does the Court depart from party presentation in
service of a sound result. Its analysis goes wrong at every
turn, beginning with its choice to venture beyond statutory
text into the realm of statutory silence.
   As the Court recognizes, the PLRA is “ `silent on the issue'
Page Proof Pending Publication
whether judges or juries should resolve factual disputes re-
lated to exhaustion.” Ante, at 469. Indeed, a search of the
exhaustion provision yields nothing remotely related to a
jury trial:
      “No action shall be brought with respect to prison condi-
      tions under [42 U. S. C. § 1983], or any other Federal law,
      by a prisoner confned in any jail, prison, or other correc-
      tional facility until such administrative remedies as are
      available are exhausted.” § 1997e(a).
Notwithstanding this silence, the Court says that the PLRA
guarantees the plaintiff “a right to a jury trial on PLRA
exhaustion when that issue is intertwined with the merits of
a claim that falls under the Seventh Amendment.” Ante, at
468. According to the Court, this “intertwinement” rule is
so well established that Congress expected courts to apply
it even when the statute says nothing about it. Ibid. Sup-
posedly, the rule is a “ `common-law adjudicatory principl[e]' ”
against which Congress legislates. Ibid.
                   Cite as: 605 U. S. 460 (2025)            487

                     Barrett, J., dissenting

   It is true that Congress sometimes legislates against the
backdrop of a well-established principle. For example, rely-
ing on the “strength of the traditional rule” that criminal
offenses require mens rea, we interpret statutes to incorpo-
rate that requirement “ `even where the statutory defnition
did not in terms include it.' ” Staples v. United States, 511
U. S. 600, 605–606 (1994) (quoting United States v. Balint,
258 U. S. 250, 251–252 (1922)). Section 1997e(a), however,
implicates no such “traditional rule.” (Note that while the
Court treats the “intertwinement” rule as bedrock, it is ap-
parently not confdent enough in the rule's historical roots to
call it constitutionally required.) Even beyond that, how-
ever, the Court does not cite precedent applying this sup-
posed rule—or anything like it—as a background principle
of statutory interpretation. And so far as I can tell, there
is no such precedent. On the contrary, when we have con-
sidered whether a statute confers the right to a jury trial,
Page Proof Pending Publication
we have understood silence to mean what you would ex-
pect—that Congress did not affrmatively confer such a
right.
   Consider Tull v. Uni ted States, 481 U. S. 412 (1987).
There, we considered whether a civil action under the Clean
Water Act required the jury's involvement. We asked the
same question that the Court asks today: Was a “ `construc-
tion of the statute . . . fairly possible by which the [Seventh
Amendment] question may be avoided' ”? Id., at 417, n. 3.
No, we said: “Nothing in the language of the Clean Water
Act or its legislative history implies any congressional intent
to grant defendants the right to a jury trial.” Ibid. “Given
this statutory silence,” there was no statutory basis for a
jury-trial right. Ibid. (emphasis added). That was so even
though the traditional role of the jury in this context meant
that the Seventh Amendment required one. Id., at 418–419.
   Our decision in Feltner v. Columbia Pictures Television,
Inc., is similar. 523 U. S. 340 (1998). Faced with the ques-
tion whether a copyright owner was entitled to a jury trial
488                  PERTTU v. RICHARDS

                      Barrett, J., dissenting

in a suit for damages, we observed that the statute was “si-
lent on the point.” Id., at 342. The “entire statutory provi-
sion” made “no mention of a right to a jury trial or, for that
matter, to juries at all.” Id., at 346. As in Tull, that si-
lence was dispositive: We “discern[ed] no statutory right to
a jury trial.” 523 U. S., at 347. And again, that was so even
though the Seventh Amendment demanded a jury. Id., at
348–355.
   Finally, in Monterey, we held that § 1983 “does not itself
confer the jury right.” 526 U. S., at 707. This was true, we
explained, even though § 1983 authorizes a party to proceed
through an “ `action at law.' ” Ibid. We declined to inter-
pret the phrase as a “term of art implying a right to a jury
trial,” and, as a result, we declined “to fnd a statutory jury
right under § 1983.” Id., at 707–708.
   This should have been an easier case than Tull, Feltner,
or Monterey. In each of those cases, the statute invoked
terms traditionally associated with the jury-trial right. See
Page Proof Pending Publication
Monterey, 526 U. S., at 707 (“ `action[s] at law' ”); Feltner, 523
U. S., at 352–353 (“statutory damages”); Tull, 481 U. S., at
422 (“civil penalty”). Indeed, in all three cases, we ulti-
mately held that the Seventh Amendment required a jury
trial. Monterey, 526 U. S., at 720–721; Feltner, 523 U. S., at
355; Tull, 481 U. S., at 427. It would have been easy to read
into a phrase such as “action at law” an implicit instruction
to require jury trials, but we did not do so; instead, we read
the statute to mean what it actually said. Monterey, 526
U. S., at 708. Here, the statute contains no term tradition-
ally associated with the jury-trial right, and the claim to a
statutory backdrop is even weaker. That is perhaps why
Richards never attempted to make the statutory argument
that the Court advances now.

                                C
  The Court's approach to statutory interpretation is not only
adventuresome—it also rests on an illusion. Neither history,
nor logic, nor precedent supports its “intertwinement” rule.
                   Cite as: 605 U. S. 460 (2025)             489

                     Barrett, J., dissenting

   I covered the lack of historical support for the rule in my
discussion of the Seventh Amendment. On, then, to logic:
The Court's proposed rule is both manifestly unfair and in-
herently arbitrary. Under the Court's approach, similarly
situated plaintiffs are entitled to a jury (or not) based on
immaterial distinctions in the claims they choose to bring.
To see why, imagine that another inmate (say, Smith) sues
Perttu based on the very same facts that Richards alleges
here. Like Richards, Smith claims that Perttu sexually har-
assed him. And, like Richards, Smith contends that Perttu
destroyed his grievances, thus excusing his failure to exhaust
his available administrative remedies. But suppose that,
unlike Richards, Smith brings only an Eighth Amendment
claim. Because the destruction of grievance forms does not
implicate the Eighth Amendment, Richards's proposed rule
would not entitle Smith to a jury trial on exhaustion.
   As this example illustrates, the Court's rule makes little
sense. There is no question that both Richards and Smith
Page Proof Pending Publication
would be entitled to a jury trial on the merits of their § 1983
claims. For both Richards and Smith, an adverse ruling on
administrative exhaustion would require dismissal. For
both Richards and Smith, the exhaustion question would de-
pend on the same set of facts and credibility determinations.
And for both Richards and Smith, an exhaustion-related dis-
missal would not preclude a subsequent suit once they have
adequately exhausted their claims. So why should Richards
get a jury trial, but not Smith? The Court does not say.
   Instead, the Court relies on three cases holding (it says)
that an issue triggers the jury-trial right if it is intertwined
with the merits, even if it could ordinarily be resolved by the
court. None of the cited cases stands for this proposition.

                                1
   The Court leads with Beacon Theatres, Inc. v. Westover,
359 U. S. 500 (1959). See ante, at 471–472. In that case, the
District Court had two actions before it: (1) an equitable ac-
tion by the plaintiff (Fox Theatres); and (2) a countersuit by
490                 PERTTU v. RICHARDS

                     Barrett, J., dissenting

the defendant (Beacon Theatres) for damages. See 359
U. S., at 502–503. Both actions involved a common issue re-
lated to the reasonableness of the plaintiff's underlying con-
tracts. But only the latter action—a suit at law—implicated
the right to a jury trial. That teed up the question: Which
should the trial court resolve frst?
   The answer, we held, is that courts ultimately have “dis-
cretion in deciding whether the legal or equitable cause
should be tried frst.” Id., at 510. But this discretion
should, “wherever possible, be exercised” such that the legal
claims would be heard before the equitable ones. Ibid.
Resolving the equitable claim frst, we explained, might inad-
vertently “ `operate either by way of res judicata or collateral
estoppel' ” so as to limit the “ `opportunity fully to try to a
jury every issue which has a bearing upon' ” the legal claim.
Id., at 504 (quoting Beacon Theatres, Inc. v. Westover, 252
F. 2d 864, 874 (CA9 1958)).
Page Proof Pending Publication
   Beacon Theatres does not hold, however, that the Seventh
Amendment compels legal-then-equitable sequencing. Nor
does it “construc[t]” statutory silence to require such a rule.
Ante, at 468. Instead, as our later cases confrm, Beacon
Theatres “enunciate[s] no more than a general prudential
rule” governing the trial court's “discretion in determining
the sequence of trial” when legal and equitable claims are
joined in the same action. Parklane Hosiery Co. v. Shore,
439 U. S. 322, 334 (1979). As a rule of discretion, it is not
hard and fast: We have observed that “there might be situa-
tions” in which a court may “resolve the equitable claim frst
even though the results might be dispositive of the issues
involved in the legal claim.” Katchen v. Landy, 382 U. S.
323, 339–340 (1966). Congress, too, has fexibility: It may
devise “a specifc statutory scheme” that contemplates “the
prompt trial of a disputed claim without the intervention of
a jury.” Id., at 339.
   With that understanding of Beacon Theatres in mind, the
differences with this case are hard to miss. Beacon The-
                       Cite as: 605 U. S. 460 (2025)                    491

                         Barrett, J., dissenting

atres involved a court's discretion in judicial administra-
tion—discretion that Congress is always free to override.
See Katchen, 382 U. S., at 339–340 (emphasizing that the
Beacon Theatres rule can be displaced “[t]o implement con-
gressional intent”). The Court's analysis here, by contrast,
turns on whether Congress affrmatively conferred a jury-
trial right on prisoners when it enacted the PLRA.
   Besides, the problem that drove the Court's decision in
Beacon Theatres is absent here. Recall the concern: that
Fox's equitable claim would proceed to fnal judgment before
Beacon Theatres's legal claim and thus preclusively resolve
“the issues involved” in that claim. Katchen, 382 U. S., at
339–340. Indeed, as we later explained in Parklane Ho-
siery, “[r]ecognition that an equitable determination could
have collateral-estoppel effect in a subsequent legal action
was the major premise” of Beacon Theatres. 439 U. S., at
333 (emphasis added). The holding of Beacon Theatres, we
Page Proof Pending Publication
underscored, was specifcally intended to avoid foreclosing,
“by res judicata or collateral estoppel,” the “relitigation” of
an “issue common to both legal and equitable claims.” 439
U. S., at 334.
   No such concern is present in this case. Both courts to
have considered the issue have concluded, consistent with
principles of collateral estoppel, that the resolution of facts
relating to administrative exhaustion does not bind the jury
in a subsequent trial. See Pavey, 544 F. 3d, at 742; Albino,
747 F. 3d, at 1171. This makes sense: Because collateral es-
toppel requires a “fnal judgment,” it should have no force
when the resolution of a threshold issue (like exhaustion)
results in a without-prejudice dismissal. Restatement (Sec-
ond) of Judgments § 27 (1980).4

  4
    While Richards does not dispute that collateral estoppel is inapplicable
here, the Court suggests that it may apply. To support this contention,
however, the Court simply relies on the hornbook principle that “factual
determinations in a frst action can have direct estoppel effect in a second
492                     PERTTU v. RICHARDS

                         Barrett, J., dissenting

  For reasons I do not understand, the Court recasts Beacon
Theatres as having little to do with collateral estoppel.
Without any hesitation, it turns Beacon Theatres's “major
premise” into a minor corollary, announcing that the case will
not be “artifcially” limited “to cases involving estoppel.”
Ante, at 476. But the reasoning of Beacon Theatres ex-
pressly turned on estoppel, and we have subsequently identi-
fed this principle as the animating force behind its holding.
Parklane Hosiery, 439 U. S., at 333; Katchen, 382 U. S., at
339–340. And estoppel is the one circumstance where inter-
twinement with the merits has practical relevance to the
jury-trial right. Without fanfare, citation, or explanation,
the Court thus transforms our 40-year understanding of a
seminal case on equity.
                              2
  The Court's reliance on Smithers v. Smith and Land v.
Dollar is even more of a stretch: Neither has anything to do
Page Proof Pending Publication
with the question presented here.

action on the same claim.” Ante, at 475. To be sure, the resolution of a
threshold issue precludes relitigation of that same threshold issue in a
subsequent suit. See 18A C. Wright, A. Miller, & E. Cooper, Federal
Practice and Procedure § 4436, p. 143 (3d ed. 2017). For that reason, if a
court rules against a plaintiff on exhaustion and dismisses her case, she
cannot relitigate whether she exhausted her administrative remedies.
But if she prevails on exhaustion and proceeds to the merits, collateral
estoppel should not preclude revisiting the facts that informed the court's
ruling on exhaustion. Indeed, the cases cited by the majority, see ante,
at 475, n. 3, are consistent with this principle. See Carr v. Tillery, 591
F. 3d 909, 916–917 (CA7 2010) (a determination that a federal court lacks
subject-matter jurisdiction over a suit would bar a federal court from as-
serting jurisdiction in a subsequent suit); Deutsch v. Flannery, 823 F. 2d
1361, 1364 (CA9 1987) (a determination that a complaint fails to allege
fraud with particularity could preclude the refling of an identical com-
plaint). The law-of-the-case doctrine would be similarly inapplicable.
See 18B C. Wright, A. Miller, & E. Cooper, Federal Practice & Procedure
§ 4478.5, p. 774 (3d ed. 2019) (“Reconsideration of a fact issue may be ap-
propriate . . . if a change of procedural posture changes the nature of
the issue”).
                   Cite as: 605 U. S. 460 (2025)             493

                     Barrett, J., dissenting

   Start with Smithers, in which the plaintiff asserted that
the defendants had stolen his land. 204 U. S. 632, 640 (1907).
The land, the plaintiff claimed, was worth more than $2,000,
the amount-in-controversy requirement then in effect. See
id., at 639–641. After holding a bench trial, the District
Court dismissed the case for lack of jurisdiction; according
to the court, each defendant had taken a parcel worth less
than $2,000, and the defendants had not acted jointly. Id.,
at 641–642. In so holding, the court violated the black-letter
rule that a plaintiff's declaration generally establishes the
amount in controversy. Id., at 642. Because it was “legally
possible for the plaintiff to recover the full amount of all the
land and the full amount of the damages claimed,” we held
that the District Court had erred in dismissing the case.
Id., at 644.
   In other words, the District Court simply misapplied long-
standing jurisdictional principles. The plaintiff 's pleadings
were suffcient to establish jurisdiction, notwithstanding any
Page Proof Pending Publication
factual disputes that might limit the plaintiff 's potential re-
covery down the line. But these disputes implicated the
merits—damages, in particular—not jurisdiction. Smith-
ers's rule is therefore unremarkable. A trial court may not
prematurely resolve a merits question by framing it as a ju-
risdictional question, thereby depriving the plaintiff of a
jury. Smithers says nothing about whether a threshold
question requires a jury simply because of factual overlap
with the merits.
   Land v. Dollar, 330 U. S. 731 (1947), is even further afeld.
There, stockholders sued members of the U. S. Maritime
Commission to recover stock previously delivered to the
Commission. Id., at 733–734. The District Court dis-
missed the case, reasoning that because the stock was federal
property, sovereign immunity barred the plaintiff's suit.
Id., at 734–735. That was an error, we held: Ownership of
the stock implicated the merits of the stockholders' claim, so
the court should not have decided that issue at the outset of
the case. Id., at 739.
494                 PERTTU v. RICHARDS

                     Barrett, J., dissenting

   Nothing in Land turned on the Seventh Amendment; in-
deed, the word “jury” does not appear in our opinion or the
opinion of the court below. See Dollar v. Land, 154 F. 2d
307 (CADC 1946). This may be because Land was a suit for
injunctive relief and mandamus, not damages. See 330
U. S., at 740 (Reed, J., concurring); Dollar, 154 F. 2d, at 308
(“The complaint prayed for relief by way of injunction and
mandamus against the defendant”). In fact, in the end “a
lengthy trial was had before the court without a jury.” Dol-
lar v. Land, 184 F. 2d 245, 247 (CADC 1950). Sensibly, then,
we have never understood Land to inform the scope of the
right to a jury trial. It stands for the more limited proposi-
tion that when there is “an identity between the `jurisdic-
tional' issues and certain issues on the merits,” there is “no
objection to reserving the jurisdictional issues until a hear-
ing on the merits.” Gulf Oil Corp. v. Copp Paving Co., 419
U. S. 186, 203, n. 19 (1974). This rule is just a principle of
judicial administration—addressing circumstances in which
Page Proof Pending Publication
it makes sense to defer ruling on a potentially jurisdictional
issue until the merits—and not a holding on the jury-trial
right.
                          *    *     *
  The Court reads the PLRA to say what it does not. It
does so for reasons that the parties did not brief; that have
no basis in our doctrine; and that are contrary to well-
established principles of statutory interpretation. In so
doing, the Court creates a regime under which an exhaustion
requirement designed to “reduce the quantity and improve
the quality of prisoner suits” just generates more litigation
of its own. Porter v. Nussle, 534 U. S. 516, 524 (2002).
Now, any prisoner can potentially obtain full jury review of
the very threshold question that was designed to streamline
prisoner litigation. All he has to do is fnd a way to trans-
form his inability to use the prison system into a claim for
relief. Congress did not devise such a rule, and we have
never adopted one. I respectfully dissent.
                            Reporter’s Note

  The attached opinion has been revised to refect the usual publication
and citation style of the United States Reports. The revised pagination
makes available the offcial United States Reports citation in advance of
publication. The syllabus has been prepared by the Reporter of Decisions
for the convenience of the reader and constitutes no part of the opinion of
Page Proof Pending Publication
the Court. A list of counsel who argued or fled briefs in this case, and
who were members of the bar of this Court at the time this case was
argued, has been inserted following the syllabus. Other revisions may
include adjustments to formatting, captions, citation form, and any errant
punctuation. The following additional edits were made:

p. 464, line 2 from bottom: “94 Stat. 352” is changed to “110 Stat. 1321–71,
   as amended,”

```

---

## GROUP: _overhaul2/lake/cases/Peters v. New York.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Peters v. New York"
type: case
citation: "392 U.S. 40 (1968)"
parallel_cite: "88 S. Ct. 1889; 20 L. Ed. 2d 917; 44 Ohio Op. 2d 402"
neutral_cite: 1968 U.S. LEXIS 1346
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
  composite_basis_ref: Peters v. New York
  varies_by_point: false
  scope_note: "Good law. Decided in the same opinion as Sibron v. New York (and companion to Terry v. Ohio): where probable cause to arrest existed, the search was valid as a search incident to a lawful arrest. opinion_id shared with Sibron (consolidated)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107730/sibron-v-new-york/"
  cluster_id: 107730
  opinion_id: 9423756
  identity_checked: true
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Related (cross-doctrine)"
  - page: "[[SIA Persons]]"
    role: "Related (cross-doctrine)"
related: ["[[Sibron v. New York]]", "[[Terry v. Ohio]]", "[[Henry v. United States (1959)]]", "[[Brinegar v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "probable-cause", "terry-stop", "burglary"]
holding: "Where probable cause to arrest existed (furtive conduct and flight indicating attempted burglary), the search of the suspect was valid as incident to a lawful arrest, even though the formal arrest followed the seizure."
lake:
  record_id: Peters v. New York
  status: verified
  projected_at: 2026-07-06
---

# Peters v. New York

*392 U.S. 40 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Off-duty New York City officer Lasky, at home, heard noises at his apartment door that led him to believe someone was trying to force entry. Looking through the peephole, he saw two men — strangers he had never seen in his twelve years in the building — tiptoeing furtively in the hallway. He telephoned the police, dressed, and entered the hall with his service revolver; the men immediately fled down the stairs. Lasky caught Peters between the fourth and fifth floors, patted down his clothing, and felt a hard object in an opaque envelope, which proved to be burglar's tools. Peters was convicted of possessing burglar's tools and moved to suppress them. The case was decided in the same opinion as *[[Sibron v. New York]]*.

## Issue
Whether the burglar's tools were lawfully seized — specifically, whether Officer Lasky had probable cause to arrest Peters, so that the search was valid as incident to a lawful arrest rather than as a *[[Terry v. Ohio|Terry]]* frisk.

## Rule
Yes. The search was justified as incident to a lawful arrest supported by probable cause. "We think, however, that for purposes of the Fourth Amendment the search was properly incident to a lawful arrest. By the time Officer Lasky caught up with Peters on the stairway between the fourth and fifth floors of the apartment building, he had probable cause to arrest him for attempted burglary." — 392 U.S. at 66. ^pin-66

Furtive conduct and flight can supply that probable cause: "deliberately furtive actions and flight at the approach of strangers or law officers are strong indicia of *mens rea*, and when coupled with specific knowledge on the part of the officer relating the suspect to the evidence of crime, they are proper factors to be considered in the decision to make an arrest." — *Id.* at 66–67. ^pin-66b

When the arrest is complete on probable cause, the officer may search: "When the policeman grabbed Peters by the collar, he abruptly 'seized' him . . . on the basis of probable cause . . . . At that point he had the authority to search Peters, and the incident search was obviously justified 'by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the destruction of evidence of the crime.'" — *Id.* at 67 (quoting *Preston v. United States*). ^pin-67

## Application
Lasky's observations — strange noises at his door, two strangers tiptoeing furtively about the hallway, their continued maneuvers, and their flight the moment he entered — supplied probable cause to arrest for attempted burglary; the Court observed it was "difficult to conceive of stronger grounds for an arrest, short of actual eyewitness observation of criminal activity." When Lasky grabbed Peters by the collar, the arrest was, for constitutional purposes, already complete on probable cause, so the ensuing search — reasonably limited and conducted primarily for weapons — was a lawful search incident to that arrest, and the burglar's tools were admissible.

## Conclusion
The search was valid as incident to a lawful arrest founded on probable cause, and the conviction was affirmed. *Peters* marks the other side of the line drawn in [[Sibron v. New York]]: where probable cause to arrest has developed, a full [[Search Incident to Arrest|search incident to arrest]] is permissible — unlike the unjustified pocket search condemned in *[[Sibron v. New York|Sibron]]*.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. Companion to [[Sibron v. New York]] and [[Terry v. Ohio]]; applies the probable-cause standard of [[Brinegar v. United States]] and [[Henry v. United States (1959)]] (the arrest is dated to the seizure on probable cause) and the search-incident rationale later associated with [[Chimel v. California]].

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Related (cross-doctrine)*
- [[SIA Persons]] — *Related (cross-doctrine)*

## Sources
- *Peters v. New York* (decided with *Sibron v. New York*), 392 U.S. 40 (1968) — https://www.courtlistener.com/opinion/107730/sibron-v-new-york/ — pinpoints: 66–67.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4d19e3c05400ebea", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Peters v. New York"}, "payload": {"all": [{"cite": "392 U.S. 40", "page": "40", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "392"}, {"cite": "88 S. Ct. 1889", "page": "1889", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "88"}, {"cite": "20 L. Ed. 2d 917", "page": "917", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "20"}, {"cite": "1968 U.S. LEXIS 1346", "page": "1346", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1968"}, {"cite": "44 Ohio Op. 2d 402", "page": "402", "reporter": "Ohio Op. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "44"}], "display": "392 U.S. 40", "official": {"cite": "392 U.S. 40", "page": "40", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "392"}, "official_selection_present": true, "record_id": "Peters v. New York"}}
{"assertion_id": "78d34ead566c3070", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-67", "record_id": "Peters v. New York"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-67", "pinpoint_status": "slip-only", "quote": "When the policeman grabbed Peters by the collar, he abruptly 'seized' him . . . on the basis of probable cause . . . . At that point he had the authority to search Peters, and the incident search was obviously justified 'by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the destruction of evidence of the crime.'", "quote_fidelity": "mismatch", "record_id": "Peters v. New York", "star_marker": null}}
{"assertion_id": "9d3244710c4397a4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-66", "record_id": "Peters v. New York"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-66", "pinpoint_status": "slip-only", "quote": "--- # Peters v. New York *392 U.S. 40 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Off-duty New York City officer Lasky, at home, heard noises at his apartment door that led him to believe someone was trying to force entry. Looking through the peephole, he saw two men — strangers he had never seen in his twelve years in the building — tiptoeing furtively in the hallway. He telephoned the police, dressed, and entered the hall with his service revolver; the men immediately fled down the stairs. Lasky caught Peters between the fourth and fifth floors, patted down his clothing, and felt a hard object in an opaque envelope, which proved to be burglar's tools. Peters was convicted of possessing burglar's tools and moved to suppress them. The case was decided in the same opinion as *Sibron v. New York*. ## Issue Whether the burglar's tools were lawfully seized — specifically, whether Officer Lasky had probable cause to arrest Peters, so that the search was valid as incident to a lawful arrest rather than as a *Terry* frisk. ## Rule Yes. The search was justified as incident to a lawful arrest supported by probable cause.", "quote_fidelity": "mismatch", "record_id": "Peters v. New York", "star_marker": null}}
{"assertion_id": "a65e54188036ba91", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-66b", "record_id": "Peters v. New York"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-66b", "pinpoint_status": "slip-only", "quote": "deliberately furtive actions and flight at the approach of strangers or law officers are strong indicia of *mens rea*, and when coupled with specific knowledge on the part of the officer relating the suspect to the evidence of crime, they are proper factors to be considered in the decision to make an arrest.", "quote_fidelity": "mismatch", "record_id": "Peters v. New York", "star_marker": null}}
{"assertion_id": "569c10ba4843ec39", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Peters v. New York"}, "payload": {"as_of_content": "1968-06-10", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Peters v. New York", "scope_note": "Good law. Decided in the same opinion as Sibron v. New York (and companion to Terry v. Ohio): where probable cause to arrest existed, the search was valid as a search incident to a lawful arrest. opinion_id shared with Sibron (consolidated).", "varies_by_point": false}}
```

### lake record — Peters v. New York

```json
{
  "schema_version": "s2.v1",
  "record_id": "Peters v. New York",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Sibron v. New York",
    "case_name_short": "Sibron",
    "case_name_full": "Sibron v. New York",
    "input_case_name": "Peters v. New York",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-06-10",
    "year": 1968,
    "docket": null,
    "cluster_id": 107730,
    "lead_opinion_id": 9423756,
    "sibling_ids": [
      107730,
      9423756,
      9423757,
      9423758,
      9423759,
      9423760,
      9423761,
      9423762
    ],
    "absolute_url": "/opinion/107730/sibron-v-new-york/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": false,
    "alternates": [],
    "reason_code": "caption_mismatch_canonical"
  },
  "citations": {
    "official": {
      "cite": "392 U.S. 40",
      "volume": "392",
      "reporter": "U.S.",
      "page": "40",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 1889",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1889",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 917",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "917",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "44 Ohio Op. 2d 402",
        "volume": "44",
        "reporter": "Ohio Op. 2d",
        "page": "402",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 1346",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1346",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "392 U.S. 40",
        "volume": "392",
        "reporter": "U.S.",
        "page": "40",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 1889",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1889",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 917",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "917",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 1346",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1346",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "44 Ohio Op. 2d 402",
        "volume": "44",
        "reporter": "Ohio Op. 2d",
        "page": "402",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "392 U.S. 40",
    "official_selection": {
      "court_class": "scotus",
      "selected": "392 U.S. 40",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-66",
      "page": null,
      "quote": "--- # Peters v. New York *392 U.S. 40 (1968)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Off-duty New York City officer Lasky, at home, heard noises at his apartment door that led him to believe someone was trying to force entry. Looking through the peephole, he saw two men \u2014 strangers he had never seen in his twelve years in the building \u2014 tiptoeing furtively in the hallway. He telephoned the police, dressed, and entered the hall with his service revolver; the men immediately fled down the stairs. Lasky caught Peters between the fourth and fifth floors, patted down his clothing, and felt a hard object in an opaque envelope, which proved to be burglar's tools. Peters was convicted of possessing burglar's tools and moved to suppress them. The case was decided in the same opinion as *Sibron v. New York*. ## Issue Whether the burglar's tools were lawfully seized \u2014 specifically, whether Officer Lasky had probable cause to arrest Peters, so that the search was valid as incident to a lawful arrest rather than as a *Terry* frisk. ## Rule Yes. The search was justified as incident to a lawful arrest supported by probable cause.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-66b",
      "page": null,
      "quote": "deliberately furtive actions and flight at the approach of strangers or law officers are strong indicia of *mens rea*, and when coupled with specific knowledge on the part of the officer relating the suspect to the evidence of crime, they are proper factors to be considered in the decision to make an arrest.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-67",
      "page": null,
      "quote": "When the policeman grabbed Peters by the collar, he abruptly 'seized' him . . . on the basis of probable cause . . . . At that point he had the authority to search Peters, and the incident search was obviously justified 'by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the destruction of evidence of the crime.'",
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
    "composite_basis_ref": "Peters v. New York",
    "varies_by_point": false,
    "scope_note": "Good law. Decided in the same opinion as Sibron v. New York (and companion to Terry v. Ohio): where probable cause to arrest existed, the search was valid as a search incident to a lawful arrest. opinion_id shared with Sibron (consolidated).",
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
        "journal_ref": "Peters v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Powell",
          "cluster_id": 9409078,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. McGann",
          "cluster_id": 4736928,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "D.L. v. Sheppard Pratt Health Sys.",
          "cluster_id": 4649052,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "D.L. v. Sheppard Pratt Health Sys.",
          "cluster_id": 4647891,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wanda Horn v. Timothy Arnold Horn",
          "cluster_id": 4522724,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Perez",
          "cluster_id": 7172931,
          "cite": [
            "96 N.E.3d 772",
            "31 N.Y.3d 964",
            "73 N.Y.S.3d 508"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The People v. Sean Garvin",
          "cluster_id": 4436829,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Steiner",
          "cluster_id": 4345072,
          "cite": [
            "847 F.3d 103",
            "102 Fed. R. Serv. 711",
            "2017 WL 437657",
            "2017 U.S. App. LEXIS 1823"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Gordon v. Loretta E. Lynch",
          "cluster_id": 3191464,
          "cite": [
            "422 U.S. App. D.C. 30",
            "817 F.3d 804",
            "2016 U.S. App. LEXIS 6175",
            "2016 WL 1319282"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Callahan v. Unified Govt of Wyandotte",
          "cluster_id": 3154974,
          "cite": [
            "806 F.3d 1022",
            "2015 U.S. App. LEXIS 19872",
            "2015 WL 7172922"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri v. Nicholas Carr",
          "cluster_id": 2731166,
          "cite": [
            "441 S.W.3d 166",
            "2014 Mo. App. LEXIS 997",
            "2014 WL 4411614"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane1_negative"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "North Carolina v. Pearce",
          "cluster_id": 107978,
          "cite": [
            "23 L. Ed. 2d 656",
            "89 S. Ct. 2072",
            "395 U.S. 711",
            "1969 U.S. LEXIS 1165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Benton v. Maryland",
          "cluster_id": 107980,
          "cite": [
            "23 L. Ed. 2d 707",
            "89 S. Ct. 2056",
            "395 U.S. 784",
            "1969 U.S. LEXIS 1167"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dunaway v. New York",
          "cluster_id": 110096,
          "cite": [
            "60 L. Ed. 2d 824",
            "99 S. Ct. 2248",
            "442 U.S. 200",
            "1979 U.S. LEXIS 126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spencer v. Kemna",
          "cluster_id": 118176,
          "cite": [
            "140 L. Ed. 2d 43",
            "118 S. Ct. 978",
            "523 U.S. 1",
            "1998 U.S. LEXIS 1597"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Robinson",
          "cluster_id": 108893,
          "cite": [
            "38 L. Ed. 2d 427",
            "94 S. Ct. 467",
            "414 U.S. 218",
            "1973 U.S. LEXIS 21",
            "66 Ohio Op. 2d 202"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Belton",
          "cluster_id": 110559,
          "cite": [
            "69 L. Ed. 2d 768",
            "101 S. Ct. 2860",
            "453 U.S. 454",
            "1981 U.S. LEXIS 13"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Mimms",
          "cluster_id": 109751,
          "cite": [
            "54 L. Ed. 2d 331",
            "98 S. Ct. 330",
            "434 U.S. 106",
            "1977 U.S. LEXIS 157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carmouche v. State",
          "cluster_id": 1463452,
          "cite": [
            "10 S.W.3d 323",
            "2000 Tex. Crim. App. LEXIS 8",
            "2000 WL 60020"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Evitts v. Lucey",
          "cluster_id": 111302,
          "cite": [
            "83 L. Ed. 2d 821",
            "105 S. Ct. 830",
            "469 U.S. 387",
            "1985 U.S. LEXIS 42"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Powell v. McCormack",
          "cluster_id": 107969,
          "cite": [
            "23 L. Ed. 2d 491",
            "89 S. Ct. 1944",
            "395 U.S. 486",
            "1969 U.S. LEXIS 3103"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. De Bour",
          "cluster_id": 5682261,
          "cite": [
            "40 N.Y.2d 210",
            "386 N.Y.S.2d 375",
            "1976 N.Y. LEXIS 2873",
            "352 N.E.2d 562"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Dickerson",
          "cluster_id": 112873,
          "cite": [
            "124 L. Ed. 2d 334",
            "113 S. Ct. 2130",
            "508 U.S. 366",
            "1993 U.S. LEXIS 4018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107730 OR 9423756 OR 9423757 OR 9423758 OR 9423759 OR 9423760 OR 9423761 OR 9423762) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDA3MTk2ODAwMDAwJnM9MjcwODMzNiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107730+OR+9423756+OR+9423757+OR+9423758+OR+9423759+OR+9423760+OR+9423761+OR+9423762%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 12,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(107730 OR 9423756 OR 9423757 OR 9423758 OR 9423759 OR 9423760 OR 9423761 OR 9423762)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTcwJnM9MTExODM1JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107730+OR+9423756+OR+9423757+OR+9423758+OR+9423759+OR+9423760+OR+9423761+OR+9423762%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107730 OR 9423756 OR 9423757 OR 9423758 OR 9423759 OR 9423760 OR 9423761 OR 9423762)",
        "reviewed": 44,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 44,
        "triage_read": 1,
        "triage_snippet_classified": 43
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107730 OR 9423756 OR 9423757 OR 9423758 OR 9423759 OR 9423760 OR 9423761 OR 9423762)",
    "indexed_citing_opinions": 2550,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107730,
        "count": 2329,
        "count_source": "search"
      },
      {
        "opinion_id": 9423756,
        "count": 293,
        "count_source": "search"
      },
      {
        "opinion_id": 9423757,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423758,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423759,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423760,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423761,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423762,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4328,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/peters-v-new-york.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNjU2ODcmcz0xMDM2MDczMiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28107730+OR+9423756+OR+9423757+OR+9423758+OR+9423759+OR+9423760+OR+9423761+OR+9423762%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107730,
        "cited_id": 91800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 103481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 103610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 103823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 104336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 105176,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 105450,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 107431,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 107540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 107663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 107679,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 107689,
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
    "date_created": "2026-07-05T18:14:17Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "input caption does not match CL canonical caption",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T18:15:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T18:15:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T18:19:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T18:15:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Peters v. New York

```
<opinion type="majority">
<author id="b85-7">MR. Chief Justice Warren</author>
<p id="AlL">delivered the opinion of the Court.</p>
<p id="b85-8">These are companion cases to No. 67, <em>Terry </em>v. <em>Ohio, ante, </em>p. 1, decided today. They present related questions under the Fourth and Fourteenth Amendments, but the cases arise in the context of New York’s “stop-and-frisk” law, N. Y. Code Crim. Proc. § 180-a. This statute provides:</p>
<blockquote id="b85-9">“1. A police officer may stop any person abroad in a public place whom he reasonably suspects is committing, has committed or is about to commit a felony or any of the offenses specified in section five hundred fifty-two of this chapter, and may demand of him his name, address and an explanation of his actions.</blockquote>
<blockquote id="b85-10">“2. When a police officer has stopped a person for questioning pursuant to this section and reasonably <page-number citation-index="1" label="44">*44</page-number>suspects that he is in danger of life or limb, he may-search such person for a dangerous weapon. If the police officer finds such a weapon or any other thing the possession of which may constitute a crime, he may take and keep it until the completion of the questioning, at which time he shall either return it, if lawfully possessed, or arrest such person.”</blockquote>
<p id="b86-5">The appellants, Sibron and Peters, were both convicted of crimes in New York state courts on the basis of evidence seized from their persons by police officers. The Court of Appeals of New York held that the evidence was properly admitted, on the ground that the searches which uncovered it were authorized by the statute. <em>People </em>v. <em>Sibron, </em>18 N. Y. 2d 603, <span class="citation" data-id="5523032"><a href="/opinion/5675381/people-v-sibron/" aria-description="Citation for case: People v. Sibron">219 N. E. 2d 196</a></span>, 272 N. Y. S. 2d 374 (1966) (memorandum); <em>People </em>v. <em>Peters, </em>18 N. Y. 2d 238, <span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">219 N. E. 2d 595</a></span>, 273 N. Y. S. 2d 217 (1966). Sibron and Peters have appealed their convictions to this Court, claiming that §. 180-a is unconstitutional on its face and as construed and applied, because the searches and seizures which it was held to have authorized violated their rights under the Fourth Amendment, made applicable to the States by the Fourteenth. <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961). We noted probable jurisdiction, <span class="citation multiple-matches"><a href="/c/U.%20S./386/954/">386 U. S. 954</a></span> (1967); <span class="citation multiple-matches"><a href="/c/U.%20S./386/980/">386 U. S. 980</a></span> (1967), and consolidated the two cases for argument with No. 67.</p>
<p id="b86-6">The facts in these cases may be stated briefly. Sibron, the appellant in No. 63, was convicted of the unlawful possession of heroin.<footnotemark>1</footnotemark> He moved before trial to suppress <page-number citation-index="1" label="45">*45</page-number>the heroin seized from his person by the arresting officer, Brooklyn Patrolman Anthony Martin. After the trial court denied his motion, Sibron pleaded guilty to the charge, preserving his right to appeal the evidentiary ruling.<footnotemark>2</footnotemark> At the hearing on the motion to suppress, Officer Martin testified that while he was patrolling his beat in uniform on March 9, 1965, he observed Sibron “continually from the hours of 4:00 P. M. to 12:00, midnight ... in the vicinity of 742 Broadway.” He stated that during this period of time he saw Sibron in conversation with six or eight persons whom he (Patrolman Martin) knew from past experience to be narcotics addicts. The officer testified that he did not overhear any of these conversations, and that he did not see anything pass between Sibron and any of the others. Late in the evening Sibron entered a restaurant. Patrolman Martin saw Sibron speak with three more known addicts inside the restaurant. Once again, nothing was overheard and nothing was seen to pass between Sibron and the addicts. Sibron sat down and ordered pie and coffee, and, as he was eating, Patrolman Martin approached him and told him to come outside. Once outside, the officer said to Sibron, “You know what I am after.” According to the officer, Sibron “mumbled something and reached into his pocket.” Simultaneously, Patrolman Martin thrust his hand into the same pocket, discovering several glassine envelopes, which, it turned out, contained heroin.</p>
<p id="b87-5">The State has had some difficulty in settling upon a <page-number citation-index="1" label="46">*46</page-number>theory for the admissibility of these envelopes of heroin. In his sworn complaint Patrolman Martin stated:</p>
<blockquote id="b88-5">“As the officer approached the defendant, the latter being in the direction of the officer and seeing him, he did put his hand in his left jacket pocket and pulled out a tinfoil envelope and did attempt to throw same to the ground. The officer never losing sight of the said envelope seized it from the def[endan]t’s left hand, examined it and found it to contain ten glascine [sic] envelopes with a white substance alleged to be Heroin.”</blockquote>
<p id="b88-6">This version of the encounter, however, bears very little resemblance to Patrolman Martin’s testimony at the hearing on the motion to suppress. In fact, he discarded the abandonment theory at the hearing.<footnotemark>3</footnotemark> Nor did the officer ever seriously suggest that he was in fear of bodily harm and that he searched Sibron in self-protection to find weapons.<footnotemark>4</footnotemark></p>
<p id="b89-3"><page-number citation-index="1" label="47">*47</page-number>The prosecutor’s theory at the hearing was that Patrolman Martin had probable cause to believe that Sibron was in possession of narcotics because he had seen him conversing with a number of known addicts over an eight-hour period. In the absence of any knowledge on Patrolman Martin’s part concerning the nature of the intercourse between Sibron and the addicts, however, the trial court was inclined to grant the motion to suppress. As the judge stated, “All he knows about the unknown men: They are narcotics addicts. They might have been talking about the World Series. They might have been talking about prize fights.” The prosecutor, however, reminded the judge that Sibron had admitted on the stand, in Patrolman Martin’s absence, that he had been talking to the addicts about narcotics. Thereupon, the trial judge changed his mind and ruled that the officer had probable cause for an arrest.</p>
<p id="b89-4">Section 180-a, the “stop-and-frisk” statute, was not mentioned at any point in the trial court. The Appellate Term of the Supreme Court affirmed the conviction without opinion. In the Court of Appeals of New York, Sibron’s case was consolidated with the <em><span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">Peters</a></span> </em>case, No. 74. The Court of Appeals held that the search in <em><span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">Peters</a></span> </em>was justified under the statute, but it wrote no opinion in Sibron’s case. The dissents of Judges Fuld and Van Voorhis, however, indicate that the court rested its holding on § 180-a. At any rate, in its Brief in Oppo<page-number citation-index="1" label="48">*48</page-number>sition to the Jurisdictional Statement in this Court, the State sought to justify the search on the basis of the statute. After we noted probable jurisdiction, the District Attorney for Kings County confessed error.</p>
<p id="b90-6">Peters, the appellant in No. 74, was convicted of possessing burglary tools under circumstances evincing an intent to employ them in the commission of a crime.<footnotemark>5</footnotemark> The tools were seized from his person at the time of his arrest, and like Sibron he made a pretrial motion to suppress them. When the trial court denied the motion, he too pleaded guilty, preserving his right to appeal. Officer Samuel Lasky of the New York City Police Department testified at the hearing on the motion that he was at home in his apartment in Mount Vernon, New York, at about 1 p. m. on July 10, 1964. He had just finished taking a shower and was drying himself when he heard a noise at his door. His attempt to investigate was interrupted by a telephone call, but when he returned and looked through the peephole into the hall, Officer Lasky saw “two men tiptoeing out of the alcove toward the stairway.” He immediately called the police, put on some civilian clothes and armed himself with his service revolver. Returning to the peephole, he saw “a tall man tiptoeing away from the alcove and followed by this shorter man, Mr. Peters, toward the stairway.” Officer Lasky testified that he had lived in the 120-unit building for 12 years and that he did not recognize either of the men as tenants. Believing that he had happened upon the two men in the course of an attempted burglary,<footnotemark>6</footnotemark> <page-number citation-index="1" label="49">*49</page-number>Officer Lasky opened his door, entered the hallway and slammed the door loudly behind him. This precipitated a flight down the stairs on the part of the two men,<footnotemark>7</footnotemark> and Officer Lasky gave chase. His apartment was located on the sixth floor, and he apprehended Peters between the fourth and fifth floors. Grabbing Peters by the collar, he continued down another flight in unsuccessful pursuit of the other man. Peters explained his presence in the building to Officer Lasky by saying that he was visiting a girl friend. However, he declined to reveal the girl friend’s name, on the ground that she was a married woman. Officer Lasky patted Peters down for weapons, and discovered a hard object in his pocket. He stated at the hearing that the object did not feel like a gun, but that it might have been a knife. He removed the object from Peters’ pocket. It was an opaque plastic envelope, containing burglar’s tools.</p>
<p id="b91-5">The trial court explicitly refused to credit Peters’ testimony that he was merely in the building to visit his girl friend. It found that Officer Lasky had the requisite “reasonable suspicion” of Peters under § 180-a to stop him and question him. It also found that Peters’ response was “clearly unsatisfactory,” and that “under <page-number citation-index="1" label="50">*50</page-number>the circumstances Lasky’s action in frisking Peters for a dangerous weapon was reasonable, even though Lasky was himself armed.” It held that the hallway of the apartment building was a “public place” within the meaning of the statute. The Appellate Division of the Supreme Court affirmed without opinion. The Court of Appeals also affirmed, essentially adopting the reasoning of the trial judge, with Judges Fuld and Van Voorhis dissenting separately.</p>
<p id="b92-6">I.</p>
<p id="b92-7">At the outset we must deal with the question whether we have jurisdiction in No. 63. It is asserted that because Sibron has completed service of the six-month sentence imposed upon him as a result of his conviction, the case has become moot under <em>St. Pierre </em>v. <em>United States, </em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">319 U. S. 41</a></span> (1943).<footnotemark>8</footnotemark> We have concluded that the case is not moot.</p>
<p id="b93-4"><page-number citation-index="1" label="51">*51</page-number>In the first place, it is clear that the broad dictum with which the Court commenced its discussion in <em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span> </em>— that “the case is moot because, after petitioner’s service of his sentence and its expiration, there was no longer a subject matter on which the judgment of this Court could operate” (<span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#42" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 42</a></span>) — fails to take account of significant qualifications recognized in <em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span> </em>and developed in later cases. Only a few days ago we held unanimously that the writ of habeas corpus was available to test the constitutionality of a state conviction where the petitioner had been in custody when he applied for the writ, but had been released before this Court could adjudicate his claims. <em>Carafas </em>v. <em>LaVallee, </em><span class="citation" data-id="9423702"><a href="/opinion/107689/carafas-v-lavallee/" aria-description="Citation for case: Carafas v. LaVallee">391 U. S. 234</a></span> (1968). On numerous occasions in the past this Court has proceeded to adjudicate the merits of criminal cases in which the sentence had been fully served or the probationary period during which a suspended sentence could be reimposed had terminated. <em>Ginsberg </em>v. <em>New York, </em><span class="citation" data-id="9423666"><a href="/opinion/107663/ginsberg-v-new-york/" aria-description="Citation for case: Ginsberg v. New York">390 U. S. 629</a></span> (1968); <em>Pollard </em>v. <em>United States, </em><span class="citation" data-id="9421375"><a href="/opinion/105450/pollard-v-united-states/" aria-description="Citation for case: Pollard v. United States">352 U. S. 354</a></span> (1957); <em>United States </em>v. <em>Morgan, </em><span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/" aria-description="Citation for case: United States v. Morgan">346 U. S. 502</a></span> (1954); <em>Fiswick </em>v. <em>United States, </em><span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/" aria-description="Citation for case: Fiswick v. United States">329 U. S. 211</a></span> (1946). Thus mere release of the prisoner does not mechanically foreclose consideration of the merits by this Court.</p>
<p id="b93-5"><em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span> </em>itself recognized two possible exceptions to its “doctrine” of mootness, and both of them appear to us to be applicable here. The Court stated that “[i]t does not appear that petitioner could not have brought his case to this Court for review before the expiration of his sentence,” noting also that because the petitioner’s conviction was for contempt and because his controversy with the Government was a continuing one, there was a good chance that there would be “ample opportunity to review” the important question presented on the merits in a future proceeding. <span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#43" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 43</a></span>. This <page-number citation-index="1" label="52">*52</page-number>was a plain recognition of the vital importance of keeping open avenues of judicial review of deprivations of constitutional right.<footnotemark>9</footnotemark> There was no way for Sibron to bring his case here before his six-month sentence expired. By statute he was precluded from obtaining bail pending appeal,<footnotemark>10</footnotemark> and by virtue of the inevitable delays of the New York court system, he was released less than a month after his newly appointed appellate counsel had been supplied with a copy of the transcript and roughly two months before it was physically possible to present his case to the first tier in the state appellate court system.<footnotemark>11</footnotemark> This was true despite the fact that he took all steps to perfect his appeal in a prompt, diligent, and timely manner.</p>
<p id="b94-6">Many deep and abiding constitutional problems are encountered primarily at a level of “low visibility” in the criminal process — in the context of prosecutions for “minor” offenses which carry only short sentences.<footnotemark>12</footnotemark> We do not believe that the Constitution contemplates that <page-number citation-index="1" label="53">*53</page-number>people deprived of constitutional rights at this level should be left utterly remediless and defenseless against repetitions of unconstitutional conduct. A State may not cut off federal review of whole classes of such cases by the simple expedient of a blanket denial of bail pending appeal. As <em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span> </em>clearly recognized, a State may not effectively deny a convict access to its appellate courts until he has been released and then argue that his case has been mooted by his failure to do what it alone prevented him from doing.<footnotemark>13</footnotemark></p>
<p id="b95-5">The second exception recognized in <em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span> </em>permits adjudication of the merits of a criminal case where “under either state or federal law further penalties or disabilities can be imposed ... as a result of the judgment which <page-number citation-index="1" label="54">*54</page-number>has . . . been satisfied.” <span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#43" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 43</a></span>. Subsequent cases have expanded this exception to the point where it may realistically be said that inroads have been made upon the principle itself. <em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span> </em>implied that the burden was upon the convict to show the existence of collateral legal consequences. Three years later in <em>Fiswick </em>v. <em>United States, </em><span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/" aria-description="Citation for case: Fiswick v. United States">329 U. S. 211</a></span> (1946), however, the Court held that a criminal case had not become moot upon release of the prisoner, noting that the convict, an alien, might be subject to deportation for having committed a crime of “moral turpitude” — even though it had never been held (and the Court refused to hold) that the crime of which he was convicted fell into this category. The Court also pointed to the fact that if the petitioner should in the future decide he wanted to become an American citizen, he might have difficulty proving that he was of “good moral character.” <span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/#222" aria-description="Citation for case: Fiswick v. United States"><em>Id., </em>at 222</a></span>.<footnotemark>14</footnotemark></p>
<p id="b96-4">The next case which dealt with the problem of collateral consequences was <em>United States </em>v. <em>Morgan, </em><span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/" aria-description="Citation for case: United States v. Morgan">346 U. S. 502</a></span> (1954). There the convict had probably been subjected to a higher sentence as a recidivist by a state court on account of the old federal conviction which he sought to attack. But as the dissent pointed out, there was no indication that the recidivist increment would be removed from his state sentence upon invalidation of the federal conviction, <span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/#516" aria-description="Citation for case: United States v. Morgan"><em>id., </em>at 516, n. 4</a></span>, and the Court chose to rest its holding that the case was not moot upon <page-number citation-index="1" label="55">*55</page-number>a broader view of the matter. Without canvassing the possible disabilities which might be imposed upon Morgan or alluding specifically to the recidivist sentence, the Court stated:</p>
<blockquote id="b97-5">“Although the term has been served, the results of the conviction may persist. Subsequent convictions may carry heavier penalties, civil rights may be affected. As the power to remedy an invalid sentence exists, we think, respondent is entitled to an opportunity to attempt to show that this conviction was invalid.” <span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/#512" aria-description="Citation for case: United States v. Morgan"><em>Id., </em>at 512-513</a></span>.</blockquote>
<p id="b97-6">Three years later, in <em>Pollard </em>v. <em>United States, </em><span class="citation" data-id="9421375"><a href="/opinion/105450/pollard-v-united-states/" aria-description="Citation for case: Pollard v. United States">352 U. S. 354</a></span> (1957), the Court abandoned all inquiry into the actual existence of specific collateral consequences and in effect presumed that they existed. With nothing more than citations to <em><span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/" aria-description="Citation for case: United States v. Morgan">Morgan</a></span> </em>and <em><span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/" aria-description="Citation for case: Fiswick v. United States">Fiswick</a></span>, </em>and a statement that “convictions may entail collateral legal disadvantages in the future,” <span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/#358" aria-description="Citation for case: Fiswick v. United States"><em>id., </em>at 358</a></span>, the Court concluded that “[t]he possibility of consequences collateral to the imposition of sentence is sufficiently substantial to justify our dealing with the merits.” <em><span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/" aria-description="Citation for case: Fiswick v. United States">Ibid.</a></span> </em>The Court thus acknowledged the obvious fact of life that most criminal convictions do in fact entail adverse collateral legal consequences.<footnotemark>15</footnotemark> The mere “possibility” that this will be the case is enough to preserve a criminal case from ending “ignominiously in the limbo of mootness.” <em>Parker </em>v. <em>Ellis, </em><span class="citation" data-id="9421986"><a href="/opinion/106050/parker-v-ellis/#577" aria-description="Citation for case: Parker v. Ellis">362 U. S. 574, 577</a></span> (1960) (dissenting opinion).</p>
<p id="b97-7">This case certainly meets that test for survival. Without pausing to canvass the possibilities in detail, we note that New York expressly provides by statute that Sibron’s conviction may be used to impeach his character should he choose to put it in issue at any future <page-number citation-index="1" label="56">*56</page-number>criminal trial, N. Y. Code Crim. Proc. § 393-e, and that it must be submitted to a trial judge for his consideration in sentencing should Sibron again be convicted of a crime, N. Y. Code Crim. Proc. § 482. There are doubtless other collateral consequences. Moreover, we see no relevance in the fact that Sibron is a multiple offender. Morgan was a multiple offender, see <span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/#503" aria-description="Citation for case: United States v. Morgan">346 U. S. at 503-504</a></span>, and so was Pollard, see <span class="citation" data-id="9421375"><a href="/opinion/105450/pollard-v-united-states/#355" aria-description="Citation for case: Pollard v. United States">352 U. S., at 355-357</a></span>. A judge or jury faced with a question of character, like a sentencing judge, may be inclined to forgive or at least discount a limited number of minor transgressions, particularly if they occurred at some time in the relatively distant past.<footnotemark>16</footnotemark> It is impossible for this Court to say at what point the number of convictions on a man’s record renders his reputation irredeemable.<footnotemark>17</footnotemark> And even if we believed that an individual had reached that point, it would be impossible for us to say that he had no interest in beginning the process of redemption with the particular case sought to be adjudicated. We cannot foretell what opportunities might present themselves in the future for the removal of other convictions from an individual’s record. The question of the validity of a criminal conviction can arise in many contexts, compare <em>Burgett </em>v. <em>Texas, </em><span class="citation" data-id="9423521"><a href="/opinion/107540/burgett-v-texas/" aria-description="Citation for case: Burgett v. Texas">389 U. S. 109</a></span> (1967), and the sooner the issue is fully litigated the better for all concerned. It is always preferable to litigate a matter <page-number citation-index="1" label="57">*57</page-number>when it is directly and principally in dispute, rather than in a proceeding where it is collateral to the central controversy. Moreover, litigation is better conducted when the dispute is fresh and additional facts may, if necessary, be taken without a substantial risk that witnesses will die or memories fade. And it is far better to eliminate the source of a potential legal disability than to require the citizen to suffer the possibly unjustified consequences of the disability itself for an indefinite period of time before he can secure adjudication of the State’s right to impose it on the basis of some past action. Cf. <em>Peyton </em>v. <em>Rowe, </em><span class="citation" data-id="107679"><a href="/opinion/107679/peyton-v-rowe/#64" aria-description="Citation for case: Peyton v. Rowe">391 U. S. 54, 64</a></span> (1968).<footnotemark>18</footnotemark></p>
<p id="b99-5">None of the concededly imperative policies behind the constitutional rule against entertaining moot controversies would be served by a dismissal in this case. There is nothing abstract, feigned, or hypothetical about Sibron’s appeal. Nor is there any suggestion that either Sibron or the State has been wanting in diligence or fervor in the litigation. We have before us a fully developed record of testimony about contested historical facts, which reflects the “impact of actuality” <footnotemark>19</footnotemark> to a far greater degree than many controversies accepted for adjudication as a matter of course under the Federal Declaratory Judgment Act, <span class="citation no-link">28 U. S. C. § 2201</span>.</p>
<p id="b99-6"><em>St. Pierre </em>v. <em>United States, supra, </em>must be read in light of later cases to mean that a criminal case is moot only if it is shown that there is no possibility that any collateral legal consequences will be imposed on the basis of the challenged conviction. That certainly is not <page-number citation-index="1" label="58">*58</page-number>the ease here. Sibron “has a substantial stake in the judgment of conviction which survives the satisfaction of the sentence imposed on him.” <em>Fiswick </em>v. <em>United States, supra, </em>at 222. The case is not moot.</p>
<p id="b100-6">II.</p>
<p id="b100-7">We deal next with the confession of error by the District Attorney for Kings County in No. 63. Confessions of error are, of course, entitled to and given great weight, but they do not “relieve this Court of the performance of the judicial function.” <em>Young </em>v. <em>United States, </em><span class="citation" data-id="103610"><a href="/opinion/103610/young-v-united-states/#258" aria-description="Citation for case: Young v. United States">315 U. S. 257, 258</a></span> (1942). It is the uniform practice of this Court to conduct its own examination of the record in all cases where the Federal Government or a State confesses that a conviction has been erroneously obtained. For one thing, as we noted in <em><span class="citation" data-id="103610"><a href="/opinion/103610/young-v-united-states/" aria-description="Citation for case: Young v. United States">Young</a></span>, </em>“our judgments are precedents, and the proper administration of the criminal law cannot be left merely to the stipulation of parties.” <span class="citation" data-id="103610"><a href="/opinion/103610/young-v-united-states/#259" aria-description="Citation for case: Young v. United States">315 U. S., at 259</a></span>. See also <em>Marino </em>v. <em>Ragen, </em><span class="citation" data-id="9420073"><a href="/opinion/104487/marino-v-ragen/" aria-description="Citation for case: Marino v. Ragen">332 U. S. 561</a></span> (1947). This consideration is entitled to special weight where, as in this case, we deal with a judgment of a State’s highest court interpreting a state statute which is challenged on constitutional grounds. The need for such authoritative declarations of state law in sensitive constitutional contexts has been the very reason for the development of the abstention doctrine by this Court. See, <em>e. g., Railroad Comm’n </em>v. <em>Pullman Co., </em><span class="citation" data-id="103481"><a href="/opinion/103481/railroad-commn-of-tex-v-pullman-co/" aria-description="Citation for case: Railroad Comm&#x27;n of Tex. v. Pullman Co.">312 U. S. 496</a></span> (1941). Such a judgment is the final product of a sovereign judicial system, and is deserving of respectful treatment by this Court. Moreover, in this case the confession of error on behalf of the entire state executive and judicial branches is made, not by a state official, but by the elected legal officer of one political subdivision within the State. The District Attorney for Kings County seems to have come late to the opinion that this conviction violated Sibron’s constitutional <page-number citation-index="1" label="59">*59</page-number>rights. For us to accept his view blindly in the circumstances, when a majority of the Court of Appeals of New York has expressed the contrary view, would be a disservice to the State of New York and an abdication of our obligation to lower courts to decide cases upon proper constitutional grounds in a manner which permits them to conform their future behavior to the demands of the Constitution. We turn to the merits.</p>
<p id="b101-5">III.</p>
<p id="b101-6">The parties on both sides of these two cases have urged that the principal issue before us is the constitutionality of § 180-a “on its face.” We decline, however, to be drawn into what we view as the abstract and unproductive exercise of laying the extraordinarily elastic categories of § 180-a next to the categories of the Fourth Amendment in an effort to determine whether the two are in some sense compatible. The constitutional validity of a warrantless search is pre-eminently the sort of question which can only be decided in the concrete factual context of the individual case. In this respect it is quite different from the question of the adequacy of the procedural safeguards written into a statute which purports to authorize the issuance of search warrants in certain circumstances. See <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967). No search required to be made under a warrant is valid if the procedure for the issuance of the warrant is inadequate to ensure the sort of neutral contemplation by a magistrate of the grounds for the search and its proposed scope, which lies at the heart of the Fourth Amendment. <em>E. g., Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964); <em>Giordenello </em>v. <em>United States, </em><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span> (1958). This Court held last Term in <em>Berger </em>v. <em>New York, supra, </em>that N. Y. Code Crim Proc. § 813-a, which established a procedure for the issuance of search warrants to permit electronic eavesdropping, failed to <page-number citation-index="1" label="60">*60</page-number>embody the safeguards demanded by the Fourth and Fourteenth Amendments.</p>
<p id="b102-6">Section 180-a, unlike § 813-a, deals with the substantive validity of certain types of seizures and searches without warrants. It purports to authorize police officers to “stop” people, “demand” explanations of them and “search [them] for dangerous weapon [s]” in certain circumstances upon “reasonable suspicion” that they are engaged in criminal activity and that they represent a danger to the policeman. The operative categories of § 180-a are not the categories of the Fourth Amendment, and they are susceptible of a wide variety of interpretations.<footnotemark>20</footnotemark> New York is, of course, free to develop its own <page-number citation-index="1" label="61">*61</page-number>law of search and seizure to meet the needs of local law enforcement, see <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#34" aria-description="Citation for case: Ker v. California">374 U. S. 23, 34</a></span> (1963), and in the process it may call the standards it employs by any names it may choose. It may not, however, authorize police conduct which trenches upon Fourth Amendment rights, regardless of the labels which it attaches to such conduct. The question in this Court upon review of a state-approved search or seizure “is not whether the search [or seizure] was authorized by state law. The question is rather whether the search was reasonable under the Fourth Amendment. Just as a search authorized by state law may be an unreasonable one under that amendment, so may a search not expressly authorized by state law be justified as a constitutionally reasonable one.” <em>Cooper </em>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 61</a></span> (1967).</p>
<p id="b103-5">Accordingly, we make no pronouncement on the facial constitutionality of § 180-a. The constitutional point <page-number citation-index="1" label="62">*62</page-number>with respect to a statute of this peculiar sort, as the Court of Appeals of New York recognized, is “not so much . . . the language employed as . . . the conduct it authorizes.” <em>People </em>v. <em>Peters, </em>18 N. Y. 2d 238, 245, <span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/#599" aria-description="Citation for case: People v. Peters">219 N. E. 2d 595, 599</a></span>, 273 N. Y. S. 2d 217, 222 (1966). We have held today in <em>Terry </em>v. <em>Ohio, ante, </em>p. 1, that police conduct of the sort with which § 180-a deals must be judged under the Reasonable Search and Seizure Clause of the Fourth Amendment. The inquiry under that clause may differ sharply from the inquiry set up by the categories of § 180-a. Our constitutional inquiry would not be furthered here by an attempt to pronounce judgment on the words of the statute. We must confine our review instead to the reasonableness of the searches and seizures which underlie these two convictions.</p>
<p id="b104-4">IV.</p>
<p id="b104-5">Turning to the facts of Sibron’s case, it is clear that the heroin was inadmissible in evidence against him. The prosecution has quite properly abandoned the notion that there was probable cause to arrest Sibron for any crime at the time Patrolman Martin accosted him in the restaurant, took him outside and searched him. The officer was not acquainted with Sibron and had no information concerning him. He merely saw Sibron talking to a number of known narcotics addicts over a period of eight hours. It must be emphasized that Patrolman Martin was completely ignorant regarding the content .of these conversations, and that he saw nothing pass between Sibron and the addicts. So far as he knew, they might indeed “have been talking about the World Series.” The inference that persons who talk to narcotics addicts are engaged in the criminal traffic in narcotics is simply not the sort of reasonable inference required to support an intrusion by the police upon an individual’s personal security. Nothing resembling probable cause existed <page-number citation-index="1" label="63">*63</page-number>until after the search had turned up the envelopes of heroin. It is axiomatic that an incident search may not precede an arrest and serve as part of its justification. <em>E. g., Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span> (1959); <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#16" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 16-17</a></span> (1948). Thus the search cannot be justified as incident to a lawful arrest.</p>
<p id="b105-5">If Patrolman Martin lacked probable cause for an arrest, however, his seizure and search of Sibron might still have been justified at the outset if he had reasonable grounds to believe that Sibron was armed and dangerous. <em>Terry </em>v. <em>Ohio, ante, </em>p. 1. We are not called- upon to decide in this case whether there was a “seizure” of Sibron inside the restaurant antecedent to the physical seizure which accompanied the search. The record is unclear with respect to what transpired between Sibron and the officer inside the restaurant. It is totally barren of any indication whether Sibron accompanied Patrolman Martin outside in submission to a show of force or authority which left him no choice, or whether he went voluntarily in a spirit of apparent cooperation with the officer’s investigation. In any event, this deficiency in the record is immaterial, since Patrolman Martin obtained no new information in the interval between his initiation of the encounter in the restaurant and his physical seizure and search of Sibron outside.</p>
<p id="b105-6">Although the Court of Appeals of New York wrote no opinion in this case, it seems to have viewed the search here as a self-protective search for weapons and to have affirmed on the basis of § 180-a, which authorizes such a search when the officer “reasonably suspects that he is in danger of life or limb.” The Court of Appeals has, at any rate, justified searches during field interrogation on the ground that “[t]he answer to the question propounded by the policeman may be a <page-number citation-index="1" label="64">*64</page-number>bullet; in any case the exposure to danger could be very great.” <em>People </em>v. <em>Rivera, </em>14 N. Y. 2d 441, 446, <span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/#35" aria-description="Citation for case: People v. Rivera">201 N. E. 2d 32, 35</a></span>, 252 N. Y. S. 2d 458, 463 (1964), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./379/978/">379 U. S. 978</a></span> (1965). But the application of this reasoning to the facts of this case proves too much. The police officer is not entitled to seize and search every person whom he sees on the street or of whom he makes inquiries. Before he places a hand on the person of a citizen in search of anything, he must have constitutionally adequate, reasonable grounds for doing so. In the case of the self-protective search for weapons, he must be able to point to particular facts from which he reasonably inferred that the individual was armed and dangerous. <em>Terry </em>v. <em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Ohio, supra.</a></span> </em>Patrolman Martin's testimony reveals no such facts. The suspect’s mere act of talking with a number of known narcotics addicts over an eight-hour period no more gives rise to reasonable fear of life or limb on the part of the police officer than it justifies an arrest for committing a crime. Nor did Patrolman Martin urge that when Sibron put his hand in his pocket, he feared that he was going for a weapon and acted in self-defense. His opening statement to Sibron — “You know what I am after” — made it abundantly clear that he sought narcotics, and his testimony at the hearing left no doubt that he thought there were narcotics in Sibron’s pocket.<footnotemark>21</footnotemark></p>
<p id="b107-4"><page-number citation-index="1" label="65">*65</page-number>Even assuming <em>arguendo </em>that there were adequate grounds to search Sibron for weapons, the nature and scope of the search conducted by Patrolman Martin were so clearly unrelated to that justification as to render the heroin inadmissible. The search for weapons approved in <em>Terry </em>consisted solely of a limited patting of the outer clothing of the suspect for concealed objects which might be used as instruments of assault. Only when he discovered such objects did the officer in <em>Terry </em>place his hands in the pockets of the men he searched. In this case, with no attempt at an initial limited exploration for arms, Patrolman Martin thrust his hand into Sibron’s pocket and took from him envelopes of heroin. His testimony shows that he was looking for narcotics, and he found them. The search was not reasonably limited in scope to the accomplishment of the only goal which might conceivably have justified its inception — the protection of the officer by disarming a potentially dangerous man. Such a search violates the guarantee of the Fourth <page-number citation-index="1" label="66">*66</page-number>Amendment, which protects the sanctity of the person against unreasonable intrusions on the part of all government agents.</p>
<p id="b108-6">V.</p>
<p id="b108-7">We think it is equally clear that the search in Peters’ case was wholly reasonable under the Constitution. The Court of Appeals of New York held that the search was made legal by § 180-a, since Peters was “abroad in a public place,” and since Officer Lasky was reasonably suspicious of his activities and, once he had stopped Peters, reasonably suspected that he was in danger of life or limb, even though he held Peters at gun point. This may be the justification for the search under state law. We think, however, that for purposes of the Fourth Amendment the search was properly incident to a lawful arrest. By the time Officer Lasky caught up with Peters on the stairway between the fourth and fifth floors of the apartment building, he had probable cause to arrest him for attempted burglary. The officer heard strange noises at his door which apparently led him to believe that someone sought to force entry. When he investigated these noises he saw two men, whom he had never seen before in his 12 years in the building, tiptoeing furtively about the hallway. They were still engaged in these maneuvers after he called the police and dressed hurriedly. And when Officer Lasky entered the hallway, the men fled down the stairs. It is difficult to conceive of stronger grounds for an arrest, short of actual eyewitness observation of criminal activity. As the trial court explicitly recognized,<footnotemark>22</footnotemark> deliberately furtive actions and flight at the approach of strangers or law officers are strong indicia of <em>mens rea, </em>and when coupled with specific knowledge on the part of the officer relating the suspect to the evidence of crime, they are proper factors <page-number citation-index="1" label="67">*67</page-number>to be considered in the decision to make an arrest. <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949); <em>Husty </em>v. <em>United States, </em><span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/" aria-description="Citation for case: Husty v. United States">282 U. S. 694</a></span> (1931); see <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#103" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 103</a></span> (1959).</p>
<p id="b109-5">As we noted in Sibron’s case, a search incident to a lawful arrest may not precede the arrest and serve as part of its justification. It is a question of fact precisely when, in each case, the arrest took place. <em>Rios </em>v. <em>United States, </em><span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/#261" aria-description="Citation for case: Rios v. United States">364 U. S. 253, 261-262</a></span> (1960). And while there was some inconclusive discussion in the trial court concerning when Officer Lasky “arrested” Peters, it is clear that the arrest had, for purposes of constitutional justification, already taken place before the search commenced. When the policeman grabbed Peters by the collar, he abruptly “seized” him and curtailed his freedom of movement on the basis of probable cause to believe that he was engaged in criminal activity. See <em>Henry </em>v. <em>United States, supra, </em>at 103. At that point he had the authority to search Peters, and the incident search was obviously justified “by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the destruction of evidence of the crime.” <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964). Moreover, it was reasonably limited in scope by these purposes. Officer Lasky did not engage in an unrestrained and thoroughgoing examination of Peters and his personal effects. He seized him to cut short his flight, and he searched him primarily for weapons. While patting down his outer clothing, Officer Lasky discovered an object in his pocket which might have been used as a weapon. He seized it and discovered it to be a potential instrument of the crime of burglary.</p>
<p id="b109-6">We have concluded that Peters’ conviction fully comports with the commands of the Fourth and Fourteenth Amendments, and must be affirmed. The conviction in <page-number citation-index="1" label="68">*68</page-number>No. 63, however, must be reversed, on the ground that the heroin was unconstitutionally admitted in evidence against the appellant.</p>
<p id="b110-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b86-7"> N. Y. Pub. Health Law § 3305 makes the unauthorized possession of any narcotic drug unlawful, and §§ <em>1751 </em>and 1751-a of the <em>N. </em>Y. Penal Law of 1909, then in effect, made the grade of the offense depend upon the amount of the drugs found in the possession of the defendant. The complaint in this case originally charged a felony, but the trial court granted the prosecutor’s motion to reduce the <page-number citation-index="1" label="45">*45</page-number>charge on the ground that “the Laboratory report will indicate a misdemeanor charge.” Sibron was convicted of a misdemeanor and sentenced to six months in jail.</p>
</footnote>
<footnote label="2">
<p id="b87-7"> N. Y. Code Crim. Proc. § 813-e provides that an order denying a motion to suppress evidence in a criminal case “may be reviewed on appeal from a judgment of conviction notwithstanding the fact that such judgment of conviction is predicated upon a plea of guilty.”</p>
</footnote>
<footnote label="3">
<p id="b88-7"> Patrolman Martin stated several times that he put his hand into Sibron’s pocket and seized the heroin before Sibron had any opportunity to remove his own hand from the pocket. The trial court questioned him on this point:</p>
<blockquote id="b88-8">“Q. Would you say at that time that he reached into his pocket and handed the packets to you? Is that what he did or did he drop the packets?</blockquote>
<blockquote id="b88-9">“A. He did not drop them. <em>I do not know what his intentions were. </em>He pushed his hand into his pocket.</blockquote>
<blockquote id="b88-10">“MR. Joseph [Prosecutor]: You intercepted it; didn’t you, Officer?</blockquote>
<blockquote id="b88-11">“The Witness: Yes.” (Emphasis added.)</blockquote>
<p id="b88-12">It is of course highly unlikely that Sibron, facing the officer at such close quarters, would have tried to remove the heroin from his pocket and throw it to the ground in the hope that he could escape responsibility for it.</p>
</footnote>
<footnote label="4">
<p id="b88-13"> The possibility that Sibron, who never, so far as appears from the record, offered any resistance, might have posed a danger to <page-number citation-index="1" label="47">*47</page-number>Patrolman Martin’s safety was never even discussed as a potential justification for the search. The only mention of weapons by the officer in his entire testimony came in response to a leading question by Sibron’s counsel, when Martin stated that he “thought he [Sibron] might have been” reaching for a gun. Even so, Patrolman Martin did not accept this suggestion by the opposition regarding the reason for his action; the discussion continued upon the plain premise that he had been looking for narcotics all the time.</p>
</footnote>
<footnote label="5">
<p id="b90-7"><em> </em>N. Y. Pen. Law of 1909, § 408, made the possession of such tools under such circumstances a misdemeanor for first offenders and a felony for all those who have “been previously convicted of any crime.” Peters was convicted of a felony under this section.</p>
</footnote>
<footnote label="6">
<p id="b90-8"> Officer Lasky testified that when he called the police immediately before leaving his apartment, he “told the Sergeant at the desk that two burglars were on my floor.”</p>
</footnote>
<footnote label="7">
<p id="b91-6"> Officer Lasky testified that when he emerged from his apartment, “I slammed the door, I had my gun and I ran down the stairs after them.” A sworn affidavit of the Assistant District Attorney, which was before the trial court when it ruled on the motion to suppress, stated that when apprehended Peters was “fleeing down the steps of the building.” The trial court explicitly took note of the flight of Peters and his companion as a factor contributing to Officer Lasky’s “reasonable suspicion” of them:</p>
<blockquote id="b91-7">“We think the testimony at the hearing does not require further laboring of this aspect of the matter, unless one is to believe that it is legitimately normal for a man to tip-toe about in the public hall of an apartment house while on a visit to his unidentified girl-friend, and, when observed by another tenant, to rapidly descend by stairway in the presence of elevators.”</blockquote>
</footnote>
<footnote label="8">
<p id="b92-8"> The first suggestion of mootness in this case came upon oral argument, when it was revealed for the first time that appellant had been released. This fact did not appear in the record, despite the fact that the release occurred well over two years before the case was argued here. Nor was mootness hinted at by the State in its Brief in Opposition to the Jurisdictional Statement in this Court— where it took the position that the decision below was so clearly right that it did not merit further review — or in its brief on the merits — in which it conceded that the decision below clearly violated Sibron’s constitutional rights and urged that it was an aberrant interpretation which should not impair the constitutionality of the New York statute. Following the suggestion of mootness on oral argument, moreover, the State filed a brief in which it amplified its views as to why the case should be held moot, but added the extraordinary suggestion that this Court should ignore the problem and pronounce upon the constitutionality of a statute in a case which has become moot. Normally in these circumstances we would consider ourselves fully justified in foreclosing a party upon an issue; however, since the question goes to the very existence of a controversy for us to adjudicate, we have undertaken to review it.</p>
</footnote>
<footnote label="9">
<p id="b94-7"> Cf. <em>Fay </em>v. <em>Noia, </em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#424" aria-description="Citation for case: Fay v. Noia">372 U. S. 391, 424</a></span> (1963):</p>
<blockquote id="b94-8">“[C]onventional notions of finality in criminal litigation cannot be permitted to defeat the manifest federal policy that federal constitutional rights of personal liberty shall not be denied without the fullest opportunity for plenary federal judicial review/'</blockquote>
</footnote>
<footnote label="10">
<p id="b94-9"> See N. Y. Code Crim. Proc. § 555 subd. 2.</p>
</footnote>
<footnote label="11">
<p id="b94-10"> Sibron was arrested on March 9, 1965, and was unable to make bail before trial because of his indigency. He thus remained in jail from that time until the expiration of his sentence (with good time credit) on July 10, 1965. He was convicted on April 23. His application for leave to proceed <em>in forma pauperis </em>was not granted until May 14, and his assigned appellate counsel was not provided with a transcript until June 11. The Appellate Term of the Supreme Court recessed on June 7 until September. Thus Sibron was released well before there had been any opportunity even to argue his case in the intermediate state appellate court. A decision by the Court of Appeals of New York was not had until July 10, 1966, the anniversary of Sibron's release.</p>
</footnote>
<footnote label="12">
<p id="b94-11"> Cf., <em>e. g., Thompson </em>v. <em>City of Louisville, </em><span class="citation" data-id="106017"><a href="/opinion/106017/thompson-v-city-of-louisville/" aria-description="Citation for case: Thompson v. City of Louisville">362 U. S. 199</a></span> (1960).</p>
</footnote>
<footnote label="13">
<p id="b95-6"> In <em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span> </em>the Court noted that the petitioner could have taken steps to preserve his ease, but that “he did not apply to this Court for a stay or a supersedeas.” <span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#43" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 43</a></span>. Here however, it is abundantly clear that there is no procedure of which Sibron could have availed himself to prevent the expiration of his sentence long before this Court could hear his case. A supersedeas from this Court is a purely ancillary writ, and may issue only in connection with an appeal actually taken. <em>Ex parte Ralston, </em><span class="citation" data-id="91800"><a href="/opinion/91800/ex-parte-ralston/" aria-description="Citation for case: Ex Parte Ralston">119 U. S. 613</a></span> (1887); Sup. Ct. Rule 18; see R. Robertson <em>&amp; F. </em>Kirkham, Jurisdiction of the Supreme Court of the United States § 435, at 883 (R. Wolfson &amp; P. Kurland ed., 1951). At the time Sibron completed service of his sentence, the only judgment outstanding was the conviction itself, rendered by the Criminal Court of the City of New York, County of Kings. This Court had no jurisdiction to hear an appeal from that judgment, since it was not rendered by the “highest court of a State in which a decision could be had,” <span class="citation no-link">28 U. S. C. § 1257</span>, and there could be no warrant for interference with the orderly appellate processes of the state courts. Thus no supersedeas could have issued. Nor could this Court have ordered Sibron admitted to bail before the expiration of his sentence, since the offense was not bailable, <span class="citation no-link">18 U. S. C. § 3144</span>; see n. 10, <em>supra. </em>Thus this case is distinguishable from <em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span> </em>in that Sibron “could not have brought his ease to this Court for review before the expiration of his sentence.” <span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#43" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 43</a></span>.</p>
</footnote>
<footnote label="14">
<p id="b96-5"> Compare <em>Ginsberg </em>v. <em>New York, </em><span class="citation" data-id="9423666"><a href="/opinion/107663/ginsberg-v-new-york/#633" aria-description="Citation for case: Ginsberg v. New York">390 U. S. 629, 633, n. 2</a></span> (1968), where this Court held that the mere possibility that the Commissioner of Buildings of the Town of Hempstead, New York, might “in his discretion” attempt in the future to revoke a license to run a luncheonette because of a single conviction for selling relatively inoffensive “girlie” magazines to a 16-year-old boy was sufficient to preserve a criminal case from mootness.</p>
</footnote>
<footnote label="15">
<p id="b97-8"> See generally Note, <span class="citation no-link">53 Va. L. Rev. 403</span> (1967).</p>
</footnote>
<footnote label="16">
<p id="b98-6"> We do not know from the record how many convictions Sibron had, for what crimes, or when they were rendered. At the hearing he admitted to a 1955 conviction for burglary and a 1957 misdemeanor conviction for possession of narcotics. He also admitted that he had other convictions, but none were specifically alluded to.</p>
</footnote>
<footnote label="17">
<p id="b98-7"> We note that there is a clear distinction between a general impairment of credibility, to which the Court referred in <em>St. Pierre, see </em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#43" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 43</a></span>, and New York’s specific statutory authorization for use of the conviction to impeach the “character” of a defendant in a criminal proceeding. The latter is a clear legal disability deliberately and specifically imposed by the legislature.</p>
</footnote>
<footnote label="18">
<p id="b99-7"> This factor has clearly been considered relevant by the Court in the past in determining the issue of mootness. See <em>Fiswick </em>v. <em>United States, </em><span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/#221" aria-description="Citation for case: Fiswick v. United States">329 U. S. 211, 221-222</a></span> (1946).</p>
</footnote>
<footnote label="19">
<p id="b99-8"> Frankfurter, A Note on Advisory Opinions, <span class="citation no-link">37 Harv. L. Rev. 1002</span>, 1006 (1924). See also <em>Parker </em>v. <em>Ellis, </em><span class="citation" data-id="9421986"><a href="/opinion/106050/parker-v-ellis/#592" aria-description="Citation for case: Parker v. Ellis">362 U. S. 574, 592-593</a></span> (1960) (dissenting opinion).</p>
</footnote>
<footnote label="20">
<p id="b102-7"> It is not apparent, for example, whether the power to “stop” granted by the statute entails a power to “detain” for investigation or interrogation upon less than probable cause, or if so what sort of durational limitations upon such detention are contemplated. And while the statute’s apparent grant of a power of compulsion indicates that many “stops” will constitute “seizures,” it is not clear that all conduct analyzed under the rubric of the statute will either rise to the level of a “seizure” or be based upon less than probable cause. In No. 74, the <em><span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">Peters</a></span> </em>case, for example, the New York courts justified the seizure of appellant under § 180-a, but we have concluded that there was in fact probable cause for an arrest when Officer Lasky seized Peters on the stairway. See <em>infra, </em>at 66. In any event, a pronouncement by this Court upon the abstract validity of § 180-a’s “stop” category would be most inappropriate in these cases, since we have concluded that neither of them presents the question of the validity of a seizure of the person for purposes of interrogation upon less than probable cause.</p>
<p id="b102-8">The statute’s other categories are equally elastic, and it was passed too recent^ for the State’s highest court to have ruled upon many of the questions involving potential intersections with federal constitutional guarantees. We cannot tell, for example, whether the officer's power to “demand” of a person an “explanation of his actions” contemplates either an obligation on the part of the citizen to answer or some additional power on the part of the officer in the event of a refusal to answer, or even whether the interrogation following the “stop” is “custodial.” Compare <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. <page-number citation-index="1" label="61">*61</page-number>436</a></span> (1966). There are, moreover, substantial indications that the statutory category of a “search for a dangerous weapon” may encompass conduct considerably broader in scope than that which we approved in <em>Terry </em>v. <em>Ohio, ante, </em>p. 1. See <em>infra, </em>at 65-66. See also <em>People </em>v. <em>Taggart, </em>20 N. Y. 2d 335, <span class="citation" data-id="5523803"><a href="/opinion/5676096/people-v-taggart/" aria-description="Citation for case: People v. Taggart">229 N. E. 2d 581</a></span>, 283 N. Y. S. 2d 1 (1967). At least some of the activity apparently permitted under the rubric of searching for dangerous weapons may thus be permissible under the Constitution only if the “reasonable suspicion” of criminal activity rises to the level of probable cause. Finally, it is impossible to tell whether the standard of “reasonable suspicion” connotes the same sort of specificity, reliability, and objectivity which is the touchstone of permissible governmental action under the Fourth Amendment. Compare <em>Terry </em>v. <em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Ohio, supra,</a></span> </em>with <em>People </em>v. <em><span class="citation" data-id="5523803"><a href="/opinion/5676096/people-v-taggart/" aria-description="Citation for case: People v. Taggart">Taggart, supra.</a></span> </em>In this connection we note that the searches and seizures in both <em><span class="citation" data-id="5523032"><a href="/opinion/5675381/people-v-sibron/" aria-description="Citation for case: People v. Sibron">Sibron</a></span> </em>and <em><span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">Peters</a></span> </em>were upheld by the Court of Appeals of New York as predicated upon “reasonable suspicion,” whereas we have concluded that the officer in <em><span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">Peters</a></span> </em>had probable cause for an arrest, while the policeman in <em><span class="citation" data-id="5523032"><a href="/opinion/5675381/people-v-sibron/" aria-description="Citation for case: People v. Sibron">Sibron</a></span> </em>was not possessed of any information which would justify an intrusion upon rights protected by the Fourth Amendment.</p>
</footnote>
<footnote label="21">
<p id="b106-6"><em> </em>It is argued in dissent that this Court has in effect overturned factual findings by the two courts below that the search in this case was a self-protective measure on the part of Patrolman Martin, who thought that Sibron might have been reaching for a gun. It is true, as we have noted, that the Court of Appeals of New York apparently rested its approval of the search on this view. The trial court, however, made no such finding of fact. The trial judge adopted the theory of the prosecution at the hearing on the motion to suppress. This theory was that there was probable cause to arrest Sibron for some crime having to do with narcotics. The fact <page-number citation-index="1" label="65">*65</page-number>which tipped the scales for the trial court had nothing to do with danger to the policeman. The judge expressly changed his original view and held the heroin admissible upon being reminded that Sibron had admitted on the stand that he spoke to the addicts about narcotics. This admission was not relevant on the issue of probable cause, and we do not understand the dissent to take the position that prior to the discovery of heroin, there was probable cause for an arrest.</p>
<p id="AqB">Moreover, Patrolman Martin himself never at any time put forth the notion that he acted to protect himself. As we have noted, this subject never came up, until on re-direct examination defense counsel raised the question whether Patrolman Martin thought Sibron was going for a gun. See n. 4, <em>supra. </em>This was the only reference to weapons at any point in the hearing, and the subject was swiftly dropped. In the circumstances an unarticulated “finding” by an appellate court which wrote no opinion, apparently to the effect that the officer’s invasion of Sibron’s person comported with the Constitution because of the need to protect himself, is not deserving of controlling deference.</p>
</footnote>
<footnote label="22">
<p id="b108-8"> See n. 7, <em>supra.</em></p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Plumhoff v. Rickard.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Plumhoff v. Rickard"
type: case
citation: ""
parallel_cite: "134 S. Ct. 2012; 188 L. Ed. 2d 1056; 82 U.S.L.W. 4394; 572 U.S. 765; 24 Fla. L. Weekly Fed. S 790"
neutral_cite: "2014 U.S. LEXIS 3816; 2014 WL 2178335"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2014
date_decided: 2014-05-27
docket: 12-1117
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2014-05-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Plumhoff v. Rickard
  varies_by_point: false
  scope_note: "Good law: deadly force to end a dangerous high-speed chase is reasonable; officers also had QI. Reasonableness is judged on the totality (consistent with Barnes v. Felix (2025))."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2675750/plumhoff-v-rickard/"
  cluster_id: 2675750
  opinion_id: 2675750
  identity_checked: true
homes:
  - page: "[[Use of Force]]"
    role: "Key — Progeny / Refinement"
related: ["[[Scott v. Harris]]", "[[Graham v. Connor]]", "[[Mullenix v. Luna]]"]
aliases: []
tags: ["case", "use-of-force", "deadly-force", "high-speed-chase", "qualified-immunity", "section-1983"]
holding: "Using deadly force to end a dangerous high-speed chase is reasonable under the Fourth Amendment, and officers need not stop shooting until the threat ends; even if it were unreasonable, the officers would be entitled to qualified immunity."
lake:
  record_id: Plumhoff v. Rickard
  status: verified
  projected_at: 2026-07-09
---

# Plumhoff v. Rickard

*572 U.S. 765 (2014)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A West Memphis officer stopped Donald Rickard's car for a broken headlight. When asked to step out, Rickard sped off and led police on a chase exceeding 100 mph for over five minutes, passing more than two dozen cars. After colliding with cruisers and spinning into a parking lot, Rickard kept maneuvering to escape — bumper flush against a police car, accelerator down, wheels spinning. Officers fired 15 shots, killing Rickard and his passenger, Kelly Allen. Rickard's daughter sued the officers under § 1983 for excessive force.

## Issue
Whether the officers' use of deadly force to end the chase (and the firing of 15 shots) violated the Fourth Amendment, and if so whether the officers were entitled to [[Qualified Immunity|qualified immunity]].

## Rule
The deadly force was reasonable. "it is beyond serious dispute that Rickard's flight posed a grave public safety risk, and here, as in *Scott*, the police acted reasonably in using deadly force to end that risk." — 572 U.S. at 777. ^pin-777

And the number of shots was not excessive: "if police officers are justified in firing at a suspect in order to end a severe threat to public safety, the officers need not stop shooting until the threat has ended." — [*Id.*](https://www.courtlistener.com/opinion/2675750/plumhoff-v-rickard/#:~:text=if%20police%20officers%20are%20justified) ^pin-777b

Alternatively, the officers had [[Qualified Immunity|qualified immunity]]: "We have held that petitioners' conduct did not violate the Fourth Amendment, but even if that were not the case, petitioners would still be entitled to summary judgment based on qualified immunity." — *Id.* at 778. ^pin-778

## Application
Judged from the perspective of a reasonable officer at the moment force was used, Rickard's continued effort to flee — engine revving, wheels spinning against a cruiser — showed he was intent on resuming a chase that had already endangered many motorists, so deadly force to stop him was reasonable as in [[Scott v. Harris]]. Because Rickard never gave up during the roughly ten-second span of fire and in fact drove off afterward, the 15 shots did not make the force excessive. The passenger Kelly Allen's presence did not enhance Rickard's own Fourth Amendment rights. And even assuming a violation, no clearly established law (per *[[Brosseau v. Haugen]]*) precluded the officers' conduct, so [[Qualified Immunity|qualified immunity]] applied.

## Conclusion
Reversed. The use of deadly force to end the chase was reasonable and the 15 shots were not excessive; in any event the officers were entitled to [[Qualified Immunity|qualified immunity]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Plumhoff* applies the dangerous-flight deadly-force rule of [[Scott v. Harris]] and the [[Graham v. Connor]] reasonableness standard, and pairs with the high-specificity qualified-immunity cases like [[Mullenix v. Luna]]. Its totality-based reasonableness analysis is consistent with the later clarification in [[Barnes v. Felix]] (2025) that there is no "moment of the threat" rule cutting off the surrounding circumstances. No negative treatment.

## Appears on
- [[Use of Force]] — *Key — Progeny / Refinement*
- [[Section 1983 Liability and Qualified Immunity]] — *Related (cross-doctrine)*

## Sources
- *Plumhoff v. Rickard*, 572 U.S. 765 (2014) — https://www.courtlistener.com/opinion/2675750/plumhoff-v-rickard/ — pinpoints: 777, 778.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e5dfb2cae327de7d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Plumhoff v. Rickard"}, "payload": {"all": [{"cite": "134 S. Ct. 2012", "page": "2012", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "134"}, {"cite": "188 L. Ed. 2d 1056", "page": "1056", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "188"}, {"cite": "2014 U.S. LEXIS 3816", "page": "3816", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2014"}, {"cite": "82 U.S.L.W. 4394", "page": "4394", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "82"}, {"cite": "572 U.S. 765", "page": "765", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "572"}, {"cite": "24 Fla. L. Weekly Fed. S 790", "page": "790", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "24"}, {"cite": "2014 WL 2178335", "page": "2178335", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2014"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Plumhoff v. Rickard"}}
{"assertion_id": "83a7992d83211bdb", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-777", "record_id": "Plumhoff v. Rickard"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-777", "pinpoint_status": "slip-only", "quote": "--- # Plumhoff v. Rickard *572 U.S. 765 (2014)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A West Memphis officer stopped Donald Rickard's car for a broken headlight. When asked to step out, Rickard sped off and led police on a chase exceeding 100 mph for over five minutes, passing more than two dozen cars. After colliding with cruisers and spinning into a parking lot, Rickard kept maneuvering to escape — bumper flush against a police car, accelerator down, wheels spinning. Officers fired 15 shots, killing Rickard and his passenger, Kelly Allen. Rickard's daughter sued the officers under § 1983 for excessive force. ## Issue Whether the officers' use of deadly force to end the chase (and the firing of 15 shots) violated the Fourth Amendment, and if so whether the officers were entitled to qualified immunity. ## Rule The deadly force was reasonable.", "quote_fidelity": "mismatch", "record_id": "Plumhoff v. Rickard", "star_marker": null}}
{"assertion_id": "a39df41abb770308", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-777b", "record_id": "Plumhoff v. Rickard"}, "payload": {"fragment": "#:~:text=if%20police%20officers%20are%20justified", "page": null, "pin_id": "pin-777b", "pinpoint_status": "star-verified", "quote": "if police officers are justified in firing at a suspect in order to end a severe threat to public safety, the officers need not stop shooting until the threat has ended.", "quote_fidelity": "matched", "record_id": "Plumhoff v. Rickard", "star_marker": "8"}}
{"assertion_id": "cc1bbaa6fa9b30d4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-778", "record_id": "Plumhoff v. Rickard"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-778", "pinpoint_status": "slip-only", "quote": "We have held that petitioners' conduct did not violate the Fourth Amendment, but even if that were not the case, petitioners would still be entitled to summary judgment based on qualified immunity.", "quote_fidelity": "mismatch", "record_id": "Plumhoff v. Rickard", "star_marker": null}}
{"assertion_id": "3d6abfd5c6be5e0e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Plumhoff v. Rickard"}, "payload": {"as_of_content": "2014-05-27", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Plumhoff v. Rickard", "scope_note": "Good law: deadly force to end a dangerous high-speed chase is reasonable; officers also had QI. Reasonableness is judged on the totality (consistent with Barnes v. Felix (2025)).", "varies_by_point": false}}
```

### lake record — Plumhoff v. Rickard

```json
{
  "schema_version": "s2.v1",
  "record_id": "Plumhoff v. Rickard",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Plumhoff v. Rickard",
    "case_name_short": "Plumhoff",
    "case_name_full": "Officer Vance PLUMHOFF, Et Al., Petitioners v. Whitne RICKARD, a Minor Child, Individually, and as Surviving Daughter of Donald Rickard, Deceased, by and Through Her Mother Samantha Rickard, as Parent and Next Friend.",
    "input_case_name": "Plumhoff v. Rickard",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2014-05-27",
    "year": 2014,
    "docket": "12-1117",
    "cluster_id": 2675750,
    "lead_opinion_id": 2675750,
    "sibling_ids": [
      2675750
    ],
    "absolute_url": "/opinion/2675750/plumhoff-v-rickard/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8415040,
        "score": 20,
        "case_name": "Plumhoff v. Rickard"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "134 S. Ct. 2012",
        "volume": "134",
        "reporter": "S. Ct.",
        "page": "2012",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "188 L. Ed. 2d 1056",
        "volume": "188",
        "reporter": "L. Ed. 2d",
        "page": "1056",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 U.S.L.W. 4394",
        "volume": "82",
        "reporter": "U.S.L.W.",
        "page": "4394",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "572 U.S. 765",
        "volume": "572",
        "reporter": "U.S.",
        "page": "765",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 790",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "790",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2014 U.S. LEXIS 3816",
        "volume": "2014",
        "reporter": "U.S. LEXIS",
        "page": "3816",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 2178335",
        "volume": "2014",
        "reporter": "WL",
        "page": "2178335",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "134 S. Ct. 2012",
        "volume": "134",
        "reporter": "S. Ct.",
        "page": "2012",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "188 L. Ed. 2d 1056",
        "volume": "188",
        "reporter": "L. Ed. 2d",
        "page": "1056",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 U.S. LEXIS 3816",
        "volume": "2014",
        "reporter": "U.S. LEXIS",
        "page": "3816",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 U.S.L.W. 4394",
        "volume": "82",
        "reporter": "U.S.L.W.",
        "page": "4394",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "572 U.S. 765",
        "volume": "572",
        "reporter": "U.S.",
        "page": "765",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 790",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "790",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 2178335",
        "volume": "2014",
        "reporter": "WL",
        "page": "2178335",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "scotus",
      "selected": null,
      "reason": "unlisted_reporter:Fla. L. Weekly Fed. S"
    }
  },
  "pinpoints": [
    {
      "id": "pin-777",
      "page": null,
      "quote": "--- # Plumhoff v. Rickard *572 U.S. 765 (2014)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A West Memphis officer stopped Donald Rickard's car for a broken headlight. When asked to step out, Rickard sped off and led police on a chase exceeding 100 mph for over five minutes, passing more than two dozen cars. After colliding with cruisers and spinning into a parking lot, Rickard kept maneuvering to escape \u2014 bumper flush against a police car, accelerator down, wheels spinning. Officers fired 15 shots, killing Rickard and his passenger, Kelly Allen. Rickard's daughter sued the officers under \u00a7 1983 for excessive force. ## Issue Whether the officers' use of deadly force to end the chase (and the firing of 15 shots) violated the Fourth Amendment, and if so whether the officers were entitled to qualified immunity. ## Rule The deadly force was reasonable.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-777b",
      "page": null,
      "quote": "if police officers are justified in firing at a suspect in order to end a severe threat to public safety, the officers need not stop shooting until the threat has ended.",
      "star_marker": "8",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 26739,
      "fragment": "#:~:text=if%20police%20officers%20are%20justified",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-778",
      "page": null,
      "quote": "We have held that petitioners' conduct did not violate the Fourth Amendment, but even if that were not the case, petitioners would still be entitled to summary judgment based on qualified immunity.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2014-05-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Plumhoff v. Rickard",
    "varies_by_point": false,
    "scope_note": "Good law: deadly force to end a dangerous high-speed chase is reasonable; officers also had QI. Reasonableness is judged on the totality (consistent with Barnes v. Felix (2025)).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Christopher J. Weiland v. Palm Beach County Sheriff's Office",
          "cluster_id": 2815299,
          "cite": [
            "792 F.3d 1313",
            "92 Fed. R. Serv. 3d 378",
            "2015 U.S. App. LEXIS 11750",
            "2015 WL 4098270"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Maben v. Troy Thelen",
          "cluster_id": 4483206,
          "cite": [
            "887 F.3d 252"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schuchardt v. President of the United States",
          "cluster_id": 4302531,
          "cite": [
            "839 F.3d 336",
            "2016 U.S. App. LEXIS 18025",
            "2016 WL 5799656"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barna v. Board of School Directors of the Panther Valley School District",
          "cluster_id": 4449477,
          "cite": [
            "877 F.3d 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Raspardo v. Carlone",
          "cluster_id": 8442004,
          "cite": [
            "770 F.3d 97",
            "2014 U.S. App. LEXIS 19010",
            "98 Empl. Prac. Dec. (CCH) 45,175",
            "124 Fair Empl. Prac. Cas. (BNA) 1049",
            "2014 WL 4958157"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "David Gavitt v. Bruce Born",
          "cluster_id": 4253418,
          "cite": [
            "835 F.3d 623",
            "2016 FED App. 0216P",
            "2016 U.S. App. LEXIS 16181"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ana Sandoval v. County of San Diego",
          "cluster_id": 4847368,
          "cite": [
            "985 F.3d 657"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Reese, Jr. v. County of Sacramento",
          "cluster_id": 4489118,
          "cite": [
            "888 F.3d 1030"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Katie Joseph v. John Doe",
          "cluster_id": 4821017,
          "cite": [
            "981 F.3d 319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillip Cordell v. Glen McKinney",
          "cluster_id": 2683914,
          "cite": [
            "759 F.3d 573",
            "2014 WL 3455556",
            "2014 U.S. App. LEXIS 13500"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "A.M. Ex Rel. F.M. v. Holmes",
          "cluster_id": 4241340,
          "cite": [
            "830 F.3d 1123"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "E.W. v. Rosemary Dolgos",
          "cluster_id": 4467174,
          "cite": [
            "884 F.3d 172"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paige Ray-Cluney v. Charles Palmer",
          "cluster_id": 4542007,
          "cite": [
            "906 F.3d 540"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Austin Gates v. Hassan Khokar",
          "cluster_id": 4476683,
          "cite": [
            "884 F.3d 1290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morrow v. Meachum",
          "cluster_id": 8443910,
          "cite": [
            "917 F.3d 870"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael-Ryan Kruger v. State of Nebraska",
          "cluster_id": 3192229,
          "cite": [
            "820 F.3d 295",
            "2016 U.S. App. LEXIS 6326",
            "2016 WL 1376343"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Angelo DiLuzio v. Village of Yorkville Ohio",
          "cluster_id": 2982966,
          "cite": [
            "796 F.3d 604",
            "2015 FED App. 0179P",
            "2015 U.S. App. LEXIS 13720",
            "2015 WL 4646121"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brittany Harris v. Kimberly Klare",
          "cluster_id": 4532638,
          "cite": [
            "902 F.3d 630"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leona Mullins v. Oscar Cyranek",
          "cluster_id": 3153107,
          "cite": [
            "805 F.3d 760",
            "2015 FED App. 0273P",
            "2015 U.S. App. LEXIS 19485",
            "2015 WL 6859303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Randy Cole v. Michael Hunter",
          "cluster_id": 4654098,
          "cite": [
            "935 F.3d 444"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roger Trent v. Steven Wade",
          "cluster_id": 2774855,
          "cite": [
            "776 F.3d 368",
            "2015 WL 394096"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Debbie Latits v. Lowell Phillips",
          "cluster_id": 4455479,
          "cite": [
            "878 F.3d 541"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James P. Crocker v. Deputy Sheriff Steven Eric Beatty",
          "cluster_id": 4875336,
          "cite": [
            "995 F.3d 1232"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edrei v. Maguire",
          "cluster_id": 8439942,
          "cite": [
            "892 F.3d 525"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kishna Brown v. Bradley Lewis",
          "cluster_id": 2782387,
          "cite": [
            "779 F.3d 401",
            "2004 FED App. 0354P",
            "2015 U.S. App. LEXIS 2917",
            "2015 WL 794705"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2675750) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTkyNzg0MDAwMDAwJnM9NDc2MjY5MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%282675750%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(2675750)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTkmcz00NzgzNjIwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%282675750%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2675750)",
        "reviewed": 144,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 144,
        "triage_read": 0,
        "triage_snippet_classified": 144
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2675750)",
    "indexed_citing_opinions": 498,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2675750,
        "count": 498,
        "count_source": "search"
      }
    ],
    "citation_count": 1736,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/plumhoff-v-rickard.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzMzEyODUmcz0xMDQ2MzYxMSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%282675750%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2675750,
        "cited_id": 76270,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 111481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 117950,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 137736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 145705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 145738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 145875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 145918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 543722,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 772438,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 783116,
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
    "date_created": "2026-07-05T17:12:36Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:12:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:12:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:15:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:12:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Plumhoff v. Rickard

```
(Slip Opinion)              OCTOBER TERM, 2013                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

       PLUMHOFF ET AL. v. RICKARD, A MINOR CHILD,

         INDIVIDUALLY, AND AS SURVIVING DAUGHTER

             OF RICKARD, DECEASED, BY AND

              THROUGH HER MOTHER RICKARD,

                      AS PARENT AND NEXT FRIEND


CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE SIXTH CIRCUIT

      No. 12–1117. Argued March 4, 2014—Decided May 27, 2014
Donald Rickard led police officers on a high-speed car chase that came
 to a temporary halt when Rickard spun out into a parking lot. Rick-
 ard resumed maneuvering his car, and as he continued to use the ac-
 celerator even though his bumper was flush against a patrol car, an
 officer fired three shots into Rickard’s car. Rickard managed to drive
 away, almost hitting an officer in the process. Officers fired 12 more
 shots as Rickard sped away, striking him and his passenger, both of
 whom died from some combination of gunshot wounds and injuries
 suffered when the car eventually crashed.
    Respondent, Rickard’s minor daughter, filed a 42 U. S. C. §1983
 action, alleging that the officers used excessive force in violation of
 the Fourth and Fourteenth Amendments. The District Court denied
 the officers’ motion for summary judgment based on qualified im-
 munity, holding that their conduct violated the Fourth Amendment
 and was contrary to clearly established law at the time in question.
 After finding that it had appellate jurisdiction, the Sixth Circuit held
 that the officers’ conduct violated the Fourth Amendment. It af-
 firmed the District Court’s order, suggesting that it agreed that the
 officers violated clearly established law.
Held:
    1. The Sixth Circuit properly exercised jurisdiction under 28
 U. S. C. §1291, which gives courts of appeals jurisdiction to hear ap-
 peals from “final decisions” of the district courts. The general rule
2                        PLUMHOFF v. RICKARD

                                  Syllabus

    that an order denying a summary judgment motion is not a “final de-
    cision[n],” and thus not immediately appealable, does not apply when
    it is based on a qualified immunity claim. Johnson v. Jones, 515
    U. S. 304, 311. Respondent argues that Johnson forecloses appellate
    jurisdiction here, but the order in Johnson was not immediately ap-
    pealable because it merely decided “a question of ‘evidence sufficien-
    cy,’ ” id., at 313, while here, petitioners’ qualified immunity claims
    raise legal issues quite different from any purely factual issues that
    might be confronted at trial. Deciding such legal issues is a core re-
    sponsibility of appellate courts and does not create an undue burden
    for them. See, e.g., Scott v. Harris, 550 U. S. 372. Pp. 5–7.
       2. The officers’ conduct did not violate the Fourth Amendment.
    Pp. 7–15.
          (a) Addressing this question first will be “beneficial” in “devel-
    op[ing] constitutional precedent” in an area that courts typically con-
    sider in cases in which the defendant asserts a qualified immunity
    defense, Pearson v. Callahan, 555 U. S. 223, 236. Pp. 7–8.
          (b) Respondent’s excessive-force argument requires analyzing the
    totality of the circumstances from the perspective “of a reasonable of-
    ficer on the scene.” Graham v. Connor, 490 U. S. 386, 396. Respond-
    ent contends that the Fourth Amendment did not allow the officers to
    use deadly force to terminate the chase, and that, even if they were
    permitted to fire their weapons, they went too far when they fired as
    many rounds as they did. Pp. 8–12.
            (1) The officers acted reasonably in using deadly force. A “po-
    lice officer’s attempt to terminate a dangerous high-speed car chase
    that threatens the lives of innocent bystanders does not violate the
    Fourth Amendment, even when it places the fleeing motorist at risk
    of serious injury or death.” Scott, supra, at 385. Rickard’s outra-
    geously reckless driving—which lasted more than five minutes, ex-
    ceeded 100 miles per hour, and included the passing of more than two
    dozen other motorists—posed a grave public safety risk, and the rec-
    ord conclusively disproves that the chase was over when Rickard’s
    car came to a temporary standstill and officers began shooting. Un-
    der the circumstances when the shots were fired, all that a reasona-
    ble officer could have concluded from Rickard’s conduct was that he
    was intent on resuming his flight, which would again pose a threat to
    others on the road. Pp. 9–11.
            (2) Petitioners did not fire more shots than necessary to end
    the public safety risk. It makes sense that, if officers are justified in
    firing at a suspect in order to end a severe threat to public safety,
    they need not stop shooting until the threat has ended. Here, during
    the 10-second span when all the shots were fired, Rickard never
    abandoned his attempt to flee and eventually managed to drive away.
                     Cite as: 572 U. S. ____ (2014)                    3

                                Syllabus

  A passenger’s presence does not bear on whether officers violated
  Rickard’s Fourth Amendment rights, which “are personal rights
  [that] may not be vicariously asserted.” Alderman v. United States,
  394 U. S. 165, 174. Pp. 11–12.
     3. Even if the officers’ conduct had violated the Fourth Amend-
  ment, petitioners would still be entitled to summary judgment based
  on qualified immunity. An official sued under §1983 is entitled to
  qualified immunity unless it is shown that the official violated a
  statutory or constitutional right that was “ ‘clearly established’ ” at
  the time of the challenged conduct. Ashcroft v. al-Kidd, 563 U. S. ___,
  ___. Brosseau v. Haugen, 543 U. S. 194, 201, where an officer shot at
  a fleeing vehicle to prevent possible harm, makes plain that no clear-
  ly established law precluded the officer’s conduct there. Thus, to pre-
  vail, respondent must meaningfully distinguish Brosseau or point to
  any “controlling authority” or “robust ‘consensus of cases of persua-
  sive authority,’ ” al-Kidd, supra, at ___, that emerged between the
  events there and those here that would alter the qualified-immunity
  analysis. Respondent has made neither showing. If anything, the
  facts here are more favorable to the officers than the facts in
  Brosseau; and respondent points to no cases that could be said to
  have clearly established the unconstitutionality of using lethal force
  to end a high-speed car chase. Pp. 12–15.
509 Fed. Appx. 388, reversed and remanded.

  ALITO, J., delivered the opinion of the Court, in which ROBERTS, C. J.,
and SCALIA, KENNEDY, THOMAS, SOTOMAYOR, and KAGAN, JJ., joined, in
which GINSBURG, J., joined as to the judgment and Parts I, II, and III–
C, and in which BREYER, J., joined except as to Part III–B–2.
                        Cite as: 572 U. S. ____ (2014)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash­
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 12–1117
                                   _________________


OFFICER VANCE PLUMHOFF, ET AL., PETITIONERS v.

WHITNE RICKARD, A MINOR CHILD, INDIVIDUALLY, AND

   AS SURVIVING DAUGHTER OF DONALD RICKARD,

      DECEASED, BY AND THROUGH HER MOTHER

        SAMANTHA RICKARD, AS PARENT AND 

                   NEXT FRIEND

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE SIXTH CIRCUIT

                                 [May 27, 2014] 


   JUSTICE ALITO delivered the opinion of the Court.*
   The courts below denied qualified immunity for police
officers who shot the driver of a fleeing vehicle to put an
end to a dangerous car chase. We reverse and hold that
the officers did not violate the Fourth Amendment. In the
alternative, we conclude that the officers were entitled to
qualified immunity because they violated no clearly estab­
lished law.
                             I

                             A

   Because this case arises from the denial of the officers’
motion for summary judgment, we view the facts in the
light most favorable to the nonmoving party, the daughter
——————
  * JUSTICE GINSBURG joins the judgment and Parts I, II, and III–C of
this opinion. JUSTICE BREYER joins this opinion except as to Part III–
B–2.
2                     PLUMHOFF v. RICKARD

                         Opinion of the Court

of the driver who attempted to flee. Wilkie v. Robbins, 551
U. S. 537, 543, n. 2 (2007). Near midnight on July 18,
2004, Lieutenant Joseph Forthman of the West Memphis,
Arkansas, Police Department pulled over a white Honda
Accord because the car had only one operating headlight.
Donald Rickard was the driver of the Accord, and Kelly
Allen was in the passenger seat. Forthman noticed an
indentation, “ ‘roughly the size of a head or a basketball’ ”
in the windshield of the car. Estate of Allen v. West Mem-
phis, 2011 WL 197426, *1 (WD Tenn., Jan. 20, 2011). He
asked Rickard if he had been drinking, and Rickard re­
sponded that he had not. Because Rickard failed to pro­
duce his driver’s license upon request and appeared nerv­
ous, Forthman asked him to step out of the car. Rather
than comply with Forthman’s request, Rickard sped away.
   Forthman gave chase and was soon joined by five other
police cruisers driven by Sergeant Vance Plumhoff and
Officers Jimmy Evans, Lance Ellis, Troy Galtelli, and
John Gardner. The officers pursued Rickard east on In­
terstate 40 toward Memphis, Tennessee. While on I–40,
they attempted to stop Rickard using a “rolling roadblock,”
id., at *2, but they were unsuccessful. The District Court
described the vehicles as “swerving through traffic at high
speeds,” id., at *8, and respondent does not dispute that
the cars attained speeds over 100 miles per hour.1 See
Memorandum of Law in Response to Defendants’ Motion
for Summary Judgment in No. 2:05–cv–2585 (WD Tenn.),
p. 16; see also Tr. of Oral Arg. 54:23–55:6. During the
——————
    1 It
      is also undisputed that Forthman saw glass shavings on the
dashboard of Rickard’s car, a sign that the windshield had been broken
recently; that another officer testified that the windshield indentation
and glass shavings would have justified a suspicion “ ‘that someone had
possibly been struck by that vehicle, like a pedestrian’ ”; and that
Forthman saw beer in Rickard’s car. See App. 424–426 (Response to
Defendant’s Statement of Undisputed Material Facts in No. 2:05–cv–
2585 (WD Tenn.), ¶¶15–19).
                 Cite as: 572 U. S. ____ (2014)            3

                     Opinion of the Court

chase, Rickard and the officers passed more than two
dozen vehicles.
   Rickard eventually exited I–40 in Memphis, and shortly
afterward he made “a quick right turn,” causing “contact
[to] occu[r]” between his car and Evans’ cruiser. 2011 WL
197426, *3. As a result of that contact, Rickard’s car spun
out into a parking lot and collided with Plumhoff ’s cruiser.
Now in danger of being cornered, Rickard put his car into
reverse “in an attempt to escape.” Ibid. As he did so,
Evans and Plumhoff got out of their cruisers and ap­
proached Rickard’s car, and Evans, gun in hand, pounded
on the passenger-side window. At that point, Rickard’s
car “made contact with” yet another police cruiser. Ibid.
Rickard’s tires started spinning, and his car “was rocking
back and forth,” ibid., indicating that Rickard was using
the accelerator even though his bumper was flush against
a police cruiser. At that point, Plumhoff fired three shots
into Rickard’s car. Rickard then “reversed in a 180 degree
arc” and “maneuvered onto” another street, forcing Ellis to
“step to his right to avoid the vehicle.” Ibid. As Rickard
continued “fleeing down” that street, ibid., Gardner and
Galtelli fired 12 shots toward Rickard’s car, bringing the
total number of shots fired during this incident to 15.
Rickard then lost control of the car and crashed into a
building. Ibid. Rickard and Allen both died from some
combination of gunshot wounds and injuries suffered in
the crash that ended the chase. See App. 60, 76.
                              B
  Respondent, Rickard’s surviving daughter, filed this
action under Rev. Stat. §1979, 42 U. S. C. §1983, against
the six individual police officers and the mayor and chief
of police of West Memphis. She alleged that the officers
used excessive force in violation of the Fourth and Four­
teenth Amendments.
  The officers moved for summary judgment based on
4                     PLUMHOFF v. RICKARD

                        Opinion of the Court

qualified immunity, but the District Court denied that
motion, holding that the officers’ conduct violated the
Fourth Amendment and was contrary to law that was
clearly established at the time in question. The officers
appealed, but a Sixth Circuit motions panel initially dis­
missed the appeal for lack of jurisdiction based on this
Court’s decision in Johnson v. Jones, 515 U. S. 304, 309
(1995). Later, however, that panel granted rehearing,
vacated its dismissal order, and left the jurisdictional
issue to be decided by a merits panel.
   The merits panel then affirmed the District Court’s
decision on the merits. Estate of Allen v. West Memphis,
509 Fed. Appx. 388 (CA6 2012). On the issue of appellate
jurisdiction, the merits panel began by stating that a
“motion for qualified immunity denied on the basis of a
district court’s determination that there exists a triable
issue of fact generally cannot be appealed on an interlocu­
tory basis.” Id., at 391. But the panel then noted that the
Sixth Circuit had previously interpreted our decision in
Scott v. Harris, 550 U. S. 372 (2007), as creating an “ex­
ception to this rule” under which an immediate appeal
may be taken to challenge “ ‘blatantly and demonstrably
false’ ” factual determinations. 509 Fed. Appx., at 391
(quoting Moldowan v. Warren, 578 F. 3d 351, 370 (CA6
2009)). Concluding that none of the District Court’s fac-
tual determinations ran afoul of that high standard, and
distinguishing the facts of this case from those in Scott,
the panel held that the officers’ conduct violated the
Fourth Amendment. 509 Fed. Appx., at 392, and n. 3.
The panel said nothing about whether the officers violated
clearly established law, but since the panel affirmed the
order denying the officers’ summary judgment motion,2
——————
  2 After expressing some confusion about whether it should dismiss or

affirm, the panel wrote that “it would seem that what we are doing is
affirming [the District Court’s] judgment.” 509 Fed. Appx., at 393.
                 Cite as: 572 U. S. ____ (2014)           5

                     Opinion of the Court

the panel must have decided that issue in respondent’s
favor.
  We granted certiorari. 571 U. S. ____ (2013).
                              II
   We start with the question whether the Court of Ap­
peals properly exercised jurisdiction under 28 U. S. C.
§1291, which gives the courts of appeals jurisdiction to
hear appeals from “final decisions” of the district courts.
   An order denying a motion for summary judgment is
generally not a final decision within the meaning of §1291
and is thus generally not immediately appealable. John-
son, 515 U. S., at 309. But that general rule does not
apply when the summary judgment motion is based on a
claim of qualified immunity. Id., at 311; Mitchell v. For-
syth, 472 U. S. 511, 528 (1985). “[Q]ualified immunity is
‘an immunity from suit rather than a mere defense to
liability.’ ” Pearson v. Callahan, 555 U. S. 223, 231 (2009)
(quoting Mitchell, supra, at 526). As a result, pretrial
orders denying qualified immunity generally fall within
the collateral order doctrine. See Ashcroft v. Iqbal, 556
U. S. 662, 671–672 (2009). This is so because such orders
conclusively determine whether the defendant is entitled
to immunity from suit; this immunity issue is both im­
portant and completely separate from the merits of the
action, and this question could not be effectively reviewed
on appeal from a final judgment because by that time the
immunity from standing trial will have been irretrievably
lost. See ibid; Johnson, supra, at 311–312 (citing Mitchell,
supra, at 525–527).
   Respondent argues that our decision in Johnson, fore­
closes appellate jurisdiction under the circumstances here,
but the order from which the appeal was taken in Johnson
was quite different from the order in the present case. In
Johnson, the plaintiff brought suit against certain police
officers who, he alleged, had beaten him. 515 U. S., at
6                  PLUMHOFF v. RICKARD

                      Opinion of the Court

307. These officers moved for summary judgment, assert­
ing that they were not present at the time of the alleged
beating and had nothing to do with it. Id., at 307–308.
The District Court determined, however, that the evidence
in the summary judgment record was sufficient to support
a contrary finding, and the court therefore denied the
officers’ motion for summary judgment. Id., at 308. The
officers then appealed, arguing that the District Court had
not correctly analyzed the relevant evidence. Ibid.
   This Court held that the Johnson order was not imme­
diately appealable because it merely decided “a question of
‘evidence sufficiency,’ i.e., which facts a party may, or may
not, be able to prove at trial.” Id., at 313. The Court noted
that an order denying summary judgment based on a
determination of “evidence sufficiency” does not present a
legal question in the sense in which the term was used in
Mitchell, the decision that first held that a pretrial order
rejecting a claim of qualified immunity is immediately
appealable. Johnson, 515 U. S., at 314. In addition, the
Court observed that a determination of evidence sufficiency
is closely related to other determinations that the trial
court may be required to make at later stages of the case.
Id., at 317. The Court also noted that appellate courts
have “no comparative expertise” over trial courts in mak­
ing such determinations and that forcing appellate courts
to entertain appeals from such orders would impose an
undue burden. Id., at 309–310, 316.
   The District Court order in this case is nothing like the
order in Johnson. Petitioners do not claim that other
officers were responsible for shooting Rickard; rather, they
contend that their conduct did not violate the Fourth
Amendment and, in any event, did not violate clearly
established law. Thus, they raise legal issues; these issues
are quite different from any purely factual issues that the
trial court might confront if the case were tried; deciding
legal issues of this sort is a core responsibility of appellate
                 Cite as: 572 U. S. ____ (2014)            7

                     Opinion of the Court

courts, and requiring appellate courts to decide such is­
sues is not an undue burden.
  The District Court order here is not materially distin­
guishable from the District Court order in Scott v. Harris,
and in that case we expressed no doubts about the juris­
diction of the Court of Appeals under §1291. Accordingly,
here, as in Scott, we hold that the Court of Appeals prop-
erly exercised jurisdiction, and we therefore turn to the
merits.
                             III

                              A

   Petitioners contend that the decision of the Court of
Appeals is wrong for two separate reasons. They maintain
that they did not violate Rickard’s Fourth Amendment
rights and that, in any event, their conduct did not violate
any Fourth Amendment rule that was clearly established
at the time of the events in question. When confronted
with such arguments, we held in Saucier v. Katz, 533 U. S.
194, 200 (2001), that “the first inquiry must be whether a
constitutional right would have been violated on the facts
alleged.” Only after deciding that question, we concluded,
may an appellate court turn to the question whether the
right at issue was clearly established at the relevant time.
Ibid.
   We subsequently altered this rigid framework in Pear-
son, declaring that “Saucier’s procedure should not be
regarded as an inflexible requirement.” 555 U. S., at 227.
At the same time, however, we noted that the Saucier
procedure “is often beneficial” because it “promotes the
development of constitutional precedent and is especially
valuable with respect to questions that do not frequently
arise in cases in which a qualified immunity defense is
unavailable.” 555 U. S., at 236. Pearson concluded that
courts “have the discretion to decide whether that [Sau-
cier] procedure is worthwhile in particular cases.” Id., at
8                  PLUMHOFF v. RICKARD

                      Opinion of the Court

242.
  Heeding our guidance in Pearson, we begin in this case
with the question whether the officers’ conduct violated
the Fourth Amendment. This approach, we believe, will
be “beneficial” in “develop[ing] constitutional precedent” in
an area that courts typically consider in cases in which the
defendant asserts a qualified immunity defense. See
Pearson, supra, at 236.
                               B
   A claim that law-enforcement officers used excessive
force to effect a seizure is governed by the Fourth
Amendment’s “reasonableness” standard. See Graham v.
Connor, 490 U. S. 386 (1989); Tennessee v. Garner, 471
U. S. 1 (1985). In Graham, we held that determining the
objective reasonableness of a particular seizure under the
Fourth Amendment “requires a careful balancing of the
nature and quality of the intrusion on the individual’s
Fourth Amendment interests against the countervailing
governmental interests at stake.” 490 U. S., at 396 (inter­
nal quotation marks omitted). The inquiry requires ana­
lyzing the totality of the circumstances. See ibid.
   We analyze this question from the perspective “of a
reasonable officer on the scene, rather than with the 20/20
vision of hindsight.” Ibid. We thus “allo[w] for the fact
that police officers are often forced to make split-second
judgments—in circumstances that are tense, uncertain,
and rapidly evolving—about the amount of force that is
necessary in a particular situation.” Id., at 396–397.
   In this case, respondent advances two main Fourth
Amendment arguments. First, she contends that the
Fourth Amendment did not allow petitioners to use deadly
force to terminate the chase. See Brief for Respondent 24–
35. Second, she argues that the “degree of force was ex­
cessive,” that is, that even if the officers were permitted to
fire their weapons, they went too far when they fired as
                 Cite as: 572 U. S. ____ (2014)            9

                     Opinion of the Court

many rounds as they did. See id., at 36–38. We address
each issue in turn.
                              1
   In Scott, we considered a claim that a police officer
violated the Fourth Amendment when he terminated a
high-speed car chase by using a technique that placed a
“fleeing motorist at risk of serious injury or death.” 550
U. S., at 386. The record in that case contained a vide­
otape of the chase, and we found that the events recorded
on the tape justified the officer’s conduct. We wrote as
follows: “Although there is no obvious way to quantify the
risks on either side, it is clear from the videotape that
respondent posed an actual and imminent threat to the
lives of any pedestrians who might have been present, to
other civilian motorists, and to the officers involved in the
chase.” Id., at 383–384. We also wrote:
    “[R]espondent’s vehicle rac[ed] down narrow, two-lane
    roads in the dead of night at speeds that are shock-
    ingly fast. We see it swerve around more than a dozen
    other cars, cross the double-yellow line, and force cars
    traveling in both directions to their respective shoul­
    ders to avoid being hit. We see it run multiple red
    lights and travel for considerable periods of time in
    the occasional center left-turn-only lane, chased by
    numerous police cars forced to engage in the same
    hazardous maneuvers just to keep up.” Id., at 379–
    380 (footnote omitted).
  In light of those facts, “we [thought] it [was] quite clear
that [the police officer] did not violate the Fourth Amend­
ment.” Id., at 381. We held that a “police officer’s attempt
to terminate a dangerous high-speed car chase that
threatens the lives of innocent bystanders does not violate
the Fourth Amendment, even when it places the fleeing
10                     PLUMHOFF v. RICKARD

                          Opinion of the Court

motorist at risk of serious injury or death.”3 Id., at 386.
  We see no basis for reaching a different conclusion here.
As we have explained supra, at ___, the chase in this case
exceeded 100 miles per hour and lasted over five minutes.
During that chase, Rickard passed more than two dozen
other vehicles, several of which were forced to alter course.
Rickard’s outrageously reckless driving posed a grave
public safety risk. And while it is true that Rickard’s car
eventually collided with a police car and came temporarily
to a near standstill, that did not end the chase. Less than
three seconds later, Rickard resumed maneuvering his
car. Just before the shots were fired, when the front
bumper of his car was flush with that of one of the police
cruisers, Rickard was obviously pushing down on the
accelerator because the car’s wheels were spinning, and
then Rickard threw the car into reverse “in an attempt to
escape.” Thus, the record conclusively disproves respond­
ent’s claim that the chase in the present case was already
over when petitioners began shooting. Under the circum­
stances at the moment when the shots were fired, all that
a reasonable police officer could have concluded was that
Rickard was intent on resuming his flight and that, if he
was allowed to do so, he would once again pose a deadly
threat for others on the road. Rickard’s conduct even after
the shots were fired—as noted, he managed to drive away
despite the efforts of the police to block his path—
——————
  3 In holding that petitioners’ conduct violated the Fourth Amend­
ment, the District Court relied on reasoning that is irreconcilable with
our decision in Scott. The District Court held that the danger presented
by a high-speed chase cannot justify the use of deadly force because
that danger was caused by the officers’ decision to continue the chase.
Estate of Allen v. West Memphis, 2011 WL 197426, *8 (WD Tenn., Jan.
20, 2011). In Scott, however, we declined to “lay down a rule requiring
the police to allow fleeing suspects to get away whenever they drive so
recklessly that they put other people’s lives in danger,” concluding that
the Constitution “assuredly does not impose this invitation to impunity­
earned-by-recklessness.” 550 U. S., at 385–386.
                  Cite as: 572 U. S. ____ (2014)            11

                      Opinion of the Court

underscores the point.
  In light of the circumstances we have discussed, it is
beyond serious dispute that Rickard’s flight posed a grave
public safety risk, and here, as in Scott, the police acted
reasonably in using deadly force to end that risk.
                                 2
   We now consider respondent’s contention that, even if
the use of deadly force was permissible, petitioners acted
unreasonably in firing a total of 15 shots. We reject that
argument. It stands to reason that, if police officers are
justified in firing at a suspect in order to end a severe
threat to public safety, the officers need not stop shooting
until the threat has ended. As petitioners noted below, “if
lethal force is justified, officers are taught to keep shooting
until the threat is over.” 509 Fed. Appx., at 392.
   Here, during the 10-second span when all the shots were
fired, Rickard never abandoned his attempt to flee. In­
deed, even after all the shots had been fired, he managed
to drive away and to continue driving until he crashed.
This would be a different case if petitioners had initiated a
second round of shots after an initial round had clearly
incapacitated Rickard and had ended any threat of con­
tinued flight, or if Rickard had clearly given himself up.
But that is not what happened.
   In arguing that too many shots were fired, respondent
relies in part on the presence of Kelly Allen in the front
seat of the car, but we do not think that this factor
changes the calculus. Our cases make it clear that “Fourth
Amendment rights are personal rights which . . . may not
be vicariously asserted.” Alderman v. United States, 394
U. S. 165, 174 (1969); see also Rakas v. Illinois, 439 U. S.
128, 138–143 (1978). Thus, the question before us is
whether petitioners violated Rickard’s Fourth Amendment
rights, not Allen’s. If a suit were brought on behalf of
Allen under either §1983 or state tort law, the risk to
12                    PLUMHOFF v. RICKARD

                         Opinion of the Court

Allen would be of central concern.4 But Allen’s presence in
the car cannot enhance Rickard’s Fourth Amendment
rights. After all, it was Rickard who put Allen in danger
by fleeing and refusing to end the chase, and it would be
perverse if his disregard for Allen’s safety worked to his
benefit.
                               C
   We have held that petitioners’ conduct did not violate
the Fourth Amendment, but even if that were not the case,
petitioners would still be entitled to summary judgment
based on qualified immunity.
   An official sued under §1983 is entitled to qualified
immunity unless it is shown that the official violated a
statutory or constitutional right that was “ ‘clearly estab­
lished’ ” at the time of the challenged conduct. Ashcroft v.
al-Kidd, 563 U. S. ___, ___ (2011) (slip op., at 3). And a
defendant cannot be said to have violated a clearly estab­
lished right unless the right’s contours were sufficiently
definite that any reasonable official in the defendant’s
shoes would have understood that he was violating it. Id.,
at ___ (slip op., at 9). In other words, “existing precedent
must have placed the statutory or constitutional question”
confronted by the official “beyond debate.” Ibid. In addi­
tion, “[w]e have repeatedly told courts . . . not to define
clearly established law at a high level of generality,” id., at
——————
  4 There seems to be some disagreement among lower courts as to
whether a passenger in Allen’s situation can recover under a Fourth
Amendment theory. Compare Vaughan v. Cox, 343 F. 3d 1323 (CA11
2003) (suggesting yes), and Fisher v. Memphis, 234 F. 3d 312 (CA6
2000) (same), with Milstead v. Kibler, 243 F. 3d 157 (CA4 2001) (sug­
gesting no), and Landol-Rivera v. Cruz Cosme, 906 F. 2d 791 (CA1
1990) (same). We express no view on this question. We also note that
in County of Sacramento v. Lewis, 523 U. S. 833, 836 (1998), the Court
held that a passenger killed as a result of a police chase could recover
under a substantive due process theory only if the officer had “a pur­
pose to cause harm unrelated to the legitimate object of arrest.”
                  Cite as: 572 U. S. ____ (2014)            13

                      Opinion of the Court

___ (slip op., at 10), since doing so avoids the crucial ques­
tion whether the official acted reasonably in the particular
circumstances that he or she faced. We think our deci­
sion in Brosseau v. Haugen, 543 U. S. 194 (2004) (per
curiam) squarely demonstrates that no clearly established
law precluded petitioners’ conduct at the time in question.
In Brosseau, we held that a police officer did not violate
clearly established law when she fired at a fleeing vehicle
to prevent possible harm to “other officers on foot who
[she] believed were in the immediate area, . . . occupied
vehicles in [the driver’s] path[,] and . . . any other citizens
who might be in the area.” Id., at 197 (quoting 339 F. 3d
857, 865 (CA9 2003); internal quotation marks omitted).
After surveying lower court decisions regarding the rea­
sonableness of lethal force as a response to vehicular
flight, we observed that this is an area “in which the result
depends very much on the facts of each case” and that the
cases “by no means ‘clearly establish[ed]’ that [the of­
ficer’s] conduct violated the Fourth Amendment.” 543
U. S., at 201. In reaching that conclusion, we held that
Garner and Graham, which are “cast at a high level of
generality,” did not clearly establish that the officer’s
decision was unreasonable. 543 U. S., at 199.
   Brosseau makes plain that as of February 21, 1999—the
date of the events at issue in that case—it was not clearly
established that it was unconstitutional to shoot a fleeing
driver to protect those whom his flight might endanger.
We did not consider later decided cases because they
“could not have given fair notice to [the officer].” Id., at
200, n. 4. To defeat immunity here, then, respondent
must show at a minimum either (1) that the officers’ con­
duct in this case was materially different from the conduct
in Brosseau or (2) that between February 21, 1999, and
July 18, 2004, there emerged either “ ‘controlling authority’ ”
or a “robust ‘consensus of cases of persuasive authority,’ ”
al-Kidd, supra, at ___ (slip op., at 10) (quoting Wilson
14                 PLUMHOFF v. RICKARD

                     Opinion of the Court

v. Layne, 526 U. S. 603, 617 (1999); some internal quota­
tion marks omitted), that would alter our analysis of the
qualified immunity question. Respondent has made nei­
ther showing.
   To begin, certain facts here are more favorable to the
officers. In Brosseau, an officer on foot fired at a driver
who had just begun to flee and who had not yet driven his
car in a dangerous manner. In contrast, the officers here
shot at Rickard to put an end to what had already been a
lengthy, high-speed pursuit that indisputably posed a
danger both to the officers involved and to any civilians
who happened to be nearby. Indeed, the lone dissenting
Justice in Brosseau emphasized that in that case, “there
was no ongoing or prior high-speed car chase to inform the
[constitutional] analysis.” 543 U. S., at 206, n. 4 (opinion
of Stevens, J.). Attempting to distinguish Brosseau, re­
spondent focuses on the fact that the officer there fired
only 1 shot, whereas here three officers collectively fired
15 shots. But it was certainly not clearly established at
the time of the shooting in this case that the number of
shots fired, under the circumstances present here, ren­
dered the use of force excessive.
   Since respondent cannot meaningfully distinguish
Brosseau, her only option is to show that its analysis was
out of date by 2004. Yet respondent has not pointed us to
any case—let alone a controlling case or a robust consen­
sus of cases—decided between 1999 and 2004 that could
be said to have clearly established the unconstitutionality
of using lethal force to end a high-speed car chase. And
respondent receives no help on this front from the opinions
below. The District Court cited only a single case decided
between 1999 and 2004 that identified a possible constitu­
tional violation by an officer who shot a fleeing driver, and
the facts of that case—where a reasonable jury could have
concluded that the suspect merely “accelerated to eighty to
eighty-five miles per hour in a seventy-miles-per-hour
                 Cite as: 572 U. S. ____ (2014)           15

                     Opinion of the Court

zone” and did not “engag[e] in any evasive maneuvers,”
Vaughan v. Cox, 343 F. 3d 1323, 1330–1331 (CA11
2003)—bear little resemblance to those here.
                        *     *    *
  Under the circumstances present in this case, we hold
that the Fourth Amendment did not prohibit petitioners
from using the deadly force that they employed to termi­
nate the dangerous car chase that Rickard precipitated.
In the alternative, we note that petitioners are entitled to
qualified immunity for the conduct at issue because they
violated no clearly established law.
  The judgment of the Court of Appeals is reversed, and
the case is remanded for further proceedings consistent
with this opinion.
                                            It is so ordered.

```

---
