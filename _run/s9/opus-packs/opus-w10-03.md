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

## GROUP: _overhaul2/lake/cases/Neil v. Biggers.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Neil v. Biggers"
type: case
citation: "409 U.S. 188 (1972)"
parallel_cite: "93 S. Ct. 375; 34 L. Ed. 2d 401"
neutral_cite: 1972 U.S. LEXIS 6
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1972
date_decided: 1972-12-06
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1972-12-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Neil v. Biggers
  varies_by_point: false
  scope_note: "Source of the five reliability factors; carried forward in Manson v. Brathwaite; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108639/neil-v-biggers/"
  cluster_id: 108639
  opinion_id: 108639
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Progeny / Refinement"
related: ["[[Manson v. Brathwaite]]", "[[Stovall v. Denno]]", "[[Perry v. New Hampshire]]", "[[United States v. Wade]]"]
aliases: []
tags: ["case", "due-process", "eyewitness-identification", "reliability", "showup"]
holding: "Even an unnecessarily suggestive identification is admissible if, under the totality of the circumstances, it is nonetheless reliable;…"
lake:
  record_id: Neil v. Biggers
  status: verified
  projected_at: 2026-07-06
---

# Neil v. Biggers

*409 U.S. 188 (1972)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A rape victim identified Biggers at a station-house showup seven months after the crime, after viewing him and hearing him repeat words spoken by her attacker. During the crime she had had a prolonged opportunity to observe the assailant under light from the moon and a kitchen light. Biggers challenged the identification as the product of an unnecessarily suggestive showup.

## Issue
Whether an identification produced by an unnecessarily suggestive procedure must be excluded, or whether it may be admitted if it is reliable under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]].

## Rule
Reliability, not suggestiveness alone, controls admissibility. "[T]he central question [is] whether under the 'totality of the circumstances' the identification was reliable even though the confrontation procedure was suggestive." — 409 U.S. at 199. ^pin-199

"[T]he factors to be considered in evaluating the likelihood of misidentification include the opportunity of the witness to view the criminal at the time of the crime, the witness' degree of attention, the accuracy of the witness' prior description of the criminal, the level of certainty demonstrated by the witness at the confrontation, and the length of time between the crime and the confrontation." — *Id.* at 199–200. ^pin-199b

## Application
Applying those factors, the victim had had an extended opportunity to view her assailant, had paid close attention, had given an accurate prior description, and was certain in her identification; although seven months had passed, she had made no prior misidentification. Under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], her identification was sufficiently reliable to be admitted despite the suggestive showup.

## Conclusion
The identification was reliable and admissible; the judgment granting relief on the identification claim was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The five *Biggers* reliability factors were carried forward and made the governing test for suggestive identifications in [[Manson v. Brathwaite]].

## Appears on
- [[Eyewitness Identification]] — *Key — Progeny / Refinement*

## Sources
- *Neil v. Biggers*, 409 U.S. 188 (1972) — https://www.courtlistener.com/opinion/108639/neil-v-biggers/ — pinpoints: 199, 199–200.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3d196a8974244098", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Neil v. Biggers"}, "payload": {"all": [{"cite": "409 U.S. 188", "page": "188", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "409"}, {"cite": "93 S. Ct. 375", "page": "375", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "93"}, {"cite": "34 L. Ed. 2d 401", "page": "401", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "34"}, {"cite": "1972 U.S. LEXIS 6", "page": "6", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1972"}], "display": "409 U.S. 188", "official": {"cite": "409 U.S. 188", "page": "188", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "409"}, "official_selection_present": true, "record_id": "Neil v. Biggers"}}
{"assertion_id": "420938a1eb57e618", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-199", "record_id": "Neil v. Biggers"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-199", "pinpoint_status": "slip-only", "quote": "--- # Neil v. Biggers *409 U.S. 188 (1972)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A rape victim identified Biggers at a station-house showup seven months after the crime, after viewing him and hearing him repeat words spoken by her attacker. During the crime she had had a prolonged opportunity to observe the assailant under light from the moon and a kitchen light. Biggers challenged the identification as the product of an unnecessarily suggestive showup. ## Issue Whether an identification produced by an unnecessarily suggestive procedure must be excluded, or whether it may be admitted if it is reliable under the totality of the circumstances. ## Rule Reliability, not suggestiveness alone, controls admissibility.", "quote_fidelity": "mismatch", "record_id": "Neil v. Biggers", "star_marker": null}}
{"assertion_id": "94d03bb06c78b82e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-199b", "record_id": "Neil v. Biggers"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-199b", "pinpoint_status": "slip-only", "quote": "[T]he factors to be considered in evaluating the likelihood of misidentification include the opportunity of the witness to view the criminal at the time of the crime, the witness' degree of attention, the accuracy of the witness' prior description of the criminal, the level of certainty demonstrated by the witness at the confrontation, and the length of time between the crime and the confrontation.", "quote_fidelity": "mismatch", "record_id": "Neil v. Biggers", "star_marker": null}}
{"assertion_id": "07b42e8f333e5474", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Neil v. Biggers"}, "payload": {"as_of_content": "1972-12-06", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Neil v. Biggers", "scope_note": "Source of the five reliability factors; carried forward in Manson v. Brathwaite; good law.", "varies_by_point": false}}
```

### lake record — Neil v. Biggers

```json
{
  "schema_version": "s2.v1",
  "record_id": "Neil v. Biggers",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Neil v. Biggers",
    "case_name_short": "Neil",
    "case_name_full": "Neil, Warden v. Biggers",
    "input_case_name": "Neil v. Biggers",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1972-12-06",
    "year": 1972,
    "docket": null,
    "cluster_id": 108639,
    "lead_opinion_id": 108639,
    "sibling_ids": [
      108639,
      9425063,
      9425064
    ],
    "absolute_url": "/opinion/108639/neil-v-biggers/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8987110,
        "score": 20,
        "case_name": "Neil v. Biggers"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "409 U.S. 188",
      "volume": "409",
      "reporter": "U.S.",
      "page": "188",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "93 S. Ct. 375",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "375",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "34 L. Ed. 2d 401",
        "volume": "34",
        "reporter": "L. Ed. 2d",
        "page": "401",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1972 U.S. LEXIS 6",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "6",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "409 U.S. 188",
        "volume": "409",
        "reporter": "U.S.",
        "page": "188",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 S. Ct. 375",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "375",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "34 L. Ed. 2d 401",
        "volume": "34",
        "reporter": "L. Ed. 2d",
        "page": "401",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1972 U.S. LEXIS 6",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "6",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "409 U.S. 188",
    "official_selection": {
      "court_class": "scotus",
      "selected": "409 U.S. 188",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-199",
      "page": null,
      "quote": "--- # Neil v. Biggers *409 U.S. 188 (1972)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A rape victim identified Biggers at a station-house showup seven months after the crime, after viewing him and hearing him repeat words spoken by her attacker. During the crime she had had a prolonged opportunity to observe the assailant under light from the moon and a kitchen light. Biggers challenged the identification as the product of an unnecessarily suggestive showup. ## Issue Whether an identification produced by an unnecessarily suggestive procedure must be excluded, or whether it may be admitted if it is reliable under the totality of the circumstances. ## Rule Reliability, not suggestiveness alone, controls admissibility.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-199b",
      "page": null,
      "quote": "[T]he factors to be considered in evaluating the likelihood of misidentification include the opportunity of the witness to view the criminal at the time of the crime, the witness' degree of attention, the accuracy of the witness' prior description of the criminal, the level of certainty demonstrated by the witness at the confrontation, and the length of time between the crime and the confrontation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1972-12-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Neil v. Biggers",
    "varies_by_point": false,
    "scope_note": "Source of the five reliability factors; carried forward in Manson v. Brathwaite; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Tappia Green",
          "cluster_id": 9409950,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Traynham v. State",
          "cluster_id": 10021058,
          "cite": [
            "243 Md. App. 717"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Myers v. State",
          "cluster_id": 10021078,
          "cite": [
            "243 Md. App. 154"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane1_negative"
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
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
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
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cuyler v. Sullivan",
          "cluster_id": 110256,
          "cite": [
            "64 L. Ed. 2d 333",
            "100 S. Ct. 1708",
            "446 U.S. 335",
            "1980 U.S. LEXIS 96"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
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
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tibbs v. Florida",
          "cluster_id": 110731,
          "cite": [
            "72 L. Ed. 2d 652",
            "102 S. Ct. 2211",
            "457 U.S. 31",
            "1982 U.S. LEXIS 116",
            "50 U.S.L.W. 4607"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
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
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estelle v. Williams",
          "cluster_id": 109438,
          "cite": [
            "48 L. Ed. 2d 126",
            "96 S. Ct. 1691",
            "425 U.S. 501",
            "1976 U.S. LEXIS 50"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sumner v. Mata",
          "cluster_id": 110382,
          "cite": [
            "66 L. Ed. 2d 722",
            "101 S. Ct. 764",
            "449 U.S. 539",
            "1981 U.S. LEXIS 62",
            "49 U.S.L.W. 4133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wright v. West",
          "cluster_id": 112771,
          "cite": [
            "120 L. Ed. 2d 225",
            "112 S. Ct. 2482",
            "505 U.S. 277",
            "1992 U.S. LEXIS 3689"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Piatkowski",
          "cluster_id": 2206245,
          "cite": [
            "870 N.E.2d 403",
            "225 Ill. 2d 551",
            "312 Ill. Dec. 338",
            "2007 Ill. LEXIS 857"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Exxon Shipping Co. v. Baker",
          "cluster_id": 145779,
          "cite": [
            "128 S. Ct. 2605",
            "554 U.S. 471"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Crews",
          "cluster_id": 110230,
          "cite": [
            "63 L. Ed. 2d 537",
            "100 S. Ct. 1244",
            "445 U.S. 463",
            "1980 U.S. LEXIS 1293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Reid",
          "cluster_id": 1636806,
          "cite": [
            "91 S.W.3d 247"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cunningham",
          "cluster_id": 2587254,
          "cite": [
            "25 P.3d 519",
            "108 Cal. Rptr. 2d 291",
            "25 Cal. 4th 926"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Owens",
          "cluster_id": 111992,
          "cite": [
            "98 L. Ed. 2d 951",
            "108 S. Ct. 838",
            "484 U.S. 554",
            "1988 U.S. LEXIS 940",
            "56 U.S.L.W. 4160"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williams v. State",
          "cluster_id": 1743700,
          "cite": [
            "937 S.W.2d 479",
            "1996 WL 724669"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Trans World Airlines, Inc. v. Hardison",
          "cluster_id": 109692,
          "cite": [
            "53 L. Ed. 2d 113",
            "97 S. Ct. 2264",
            "432 U.S. 63",
            "1977 U.S. LEXIS 115",
            "14 Empl. Prac. Dec. (CCH) 7620",
            "14 Fair Empl. Prac. Cas. (BNA) 1697"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rutledge v. United States",
          "cluster_id": 118013,
          "cite": [
            "134 L. Ed. 2d 419",
            "116 S. Ct. 1241",
            "517 U.S. 292",
            "1996 U.S. LEXIS 2163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McDaniel v. Brown",
          "cluster_id": 1750,
          "cite": [
            "175 L. Ed. 2d 582",
            "130 S. Ct. 665",
            "558 U.S. 120",
            "2010 U.S. LEXIS 3"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gimmy v. People",
          "cluster_id": 1231296,
          "cite": [
            "645 P.2d 262",
            "1982 Colo. LEXIS 568"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sumner v. Mata",
          "cluster_id": 110667,
          "cite": [
            "71 L. Ed. 2d 480",
            "102 S. Ct. 1303",
            "455 U.S. 591",
            "1982 U.S. LEXIS 83",
            "50 U.S.L.W. 3760"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Malloy",
          "cluster_id": 5685415,
          "cite": [
            "55 N.Y.2d 296",
            "434 N.E.2d 237",
            "449 N.Y.S.2d 168",
            "1982 N.Y. LEXIS 3140"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Schevers",
          "cluster_id": 1191968,
          "cite": [
            "979 P.2d 659",
            "132 Idaho 786",
            "1999 Ida. App. LEXIS 10"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moore v. Illinois",
          "cluster_id": 109757,
          "cite": [
            "54 L. Ed. 2d 424",
            "98 S. Ct. 458",
            "434 U.S. 220",
            "1977 U.S. LEXIS 163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108639 OR 9425063 OR 9425064) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTY5NDU2MDAwMDAwJnM9NDY2NDc1MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108639+OR+9425063+OR+9425064%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108639 OR 9425063 OR 9425064)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MDImcz0yMDc3MTc4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108639+OR+9425063+OR+9425064%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108639 OR 9425063 OR 9425064)",
        "reviewed": 69,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 69,
        "triage_read": 0,
        "triage_snippet_classified": 69
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108639 OR 9425063 OR 9425064)",
    "indexed_citing_opinions": 4347,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108639,
        "count": 3947,
        "count_source": "search"
      },
      {
        "opinion_id": 9425063,
        "count": 458,
        "count_source": "search"
      },
      {
        "opinion_id": 9425064,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 7060,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/neil-v-biggers.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxNTAzNTQmcz0xMDMwNzE1MCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28108639+OR+9425063+OR+9425064%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108639,
        "cited_id": 85455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 85481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 87987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 94988,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 98883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 100433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 100923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 101908,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 104451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 104591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 104726,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 106109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 106328,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 107638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 107890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 107893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 284140,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 291028,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 298978,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 303254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 1493381,
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
    "date_created": "2026-07-05T15:14:05Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:14:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:24:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:28:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:24:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Neil v. Biggers

```
<div>
<center><b><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">409 U.S. 188</a></span> (1972)</b></center>
<center><h1>NEIL, WARDEN<br>
v.<br>
BIGGERS.</h1></center>
<center>No. 71-586.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 18-19, 1972.</center>
<center>Decided December 6, 1972.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SIXTH CIRCUIT.
<p><span class="star-pagination">*189</span> <i>Bart C. Durham III,</i> Assistant Attorney General of Tennessee, argued the cause for petitioner. With him on the brief was <i>David M. Pack,</i> Attorney General.</p>
<p><i>Michael Meltsner</i> argued the cause for respondent. With him on the brief were <i>Jack Greenberg, Anthony G. Amsterdam, Avon N. Williams, Jr.,</i> and <i>Z. Alexander Looby.</i></p>
<p><i>Louis J. Lefkowitz,</i> Attorney General of New York, <i>pro se, Samuel A. Hirshowitz,</i> First Assistant Attorney General, and <i>Maria L. Marcus,</i> Assistant Attorney General, filed a brief for the Attorney General of New York as <i>amicus curiae</i> urging reversal.</p>
<p><i>Shirley Fingerhood, Richard G. Green, Burt Neuborne,</i> and <i>Melvin L. Wulf</i> filed a brief for the American Civil Liberties Union as <i>amicus curiae</i> urging affirmance.</p>
<p>MR. JUSTICE POWELL delivered the opinion of the Court.</p>
<p>In 1965, after a jury trial in a Tennessee court, respondent was convicted of rape and was sentenced to 20 years' imprisonment. The State's evidence consisted in part of testimony concerning a station-house identification of respondent by the victim. The Tennessee Supreme Court affirmed. <i>Biggers</i> v. <i>State,</i> <span class="citation" data-id="1493381"><a href="/opinion/1493381/biggers-v-state/" aria-description="Citation for case: Biggers v. State">219 Tenn. 553</a></span>, <span class="citation" data-id="1493381"><a href="/opinion/1493381/biggers-v-state/" aria-description="Citation for case: Biggers v. State">411 S. W. 2d 696</a></span> (1967). On certiorari, the judgment of the Tennessee Supreme Court was affirmed by an equally divided Court. <i>Biggers</i> v. <i>Tennessee,</i> <span class="citation" data-id="9423641"><a href="/opinion/107638/biggers-v-tennessee/" aria-description="Citation for case: Biggers v. Tennessee">390 U. S. 404</a></span> (1968) (MARSHALL, J., not participating). Respondent then brought a federal habeas corpus action raising several claims. In reply, <span class="star-pagination">*190</span> petitioner contended that the claims were barred by <span class="citation no-link">28 U. S. C. § 2244</span> (c), which provides in pertinent part:</p>
<blockquote>"In a habeas corpus proceeding brought in behalf of a person in custody pursuant to the judgment of a State court, a prior judgment of the Supreme Court of the United States on an appeal or review by a writ of certiorari at the instance of the prisoner of the decision of such State court, shall be conclusive as to all issues of fact or law with respect to an asserted denial of a Federal right which constitutes ground for discharge in a habeas corpus proceeding, actually adjudicated by the Supreme Court therein. . . ."</blockquote>
<p>The District Court held that the claims were not barred and, after a hearing, held in an unreported opinion that the station-house identification procedure was so suggestive as to violate due process. The Court of Appeals affirmed. <span class="citation" data-id="9457324"><a href="/opinion/298978/archie-nathaniel-biggers-v-william-s-neil-warden-tennessee-state/" aria-description="Citation for case: Archie Nathaniel Biggers v. William S. Neil, Warden,...">448 F. 2d 91</a></span> (1971). We granted certiorari to decide whether an affirmance by an equally divided Court is an actual adjudication barring subsequent consideration on habeas corpus, and, if not, whether the identification procedure violated due process. <span class="citation multiple-matches"><a href="/c/U.%20S./405/954/">405 U. S. 954</a></span> (1972).</p>
<p></p>
<h2>I</h2>
<p>The intended scope of the phrase "actually adjudicated by the Supreme Court" must be determined by reference to the peculiarities of federal court jurisdiction and the context in which § 2244 (c) was enacted. Jurisdiction to hear state prisoner claims on habeas corpus was first expressly conferred on the federal courts by the Judiciary Act of 1867, c. 28, <span class="citation no-link">14 Stat. 385</span>. Thereafter, decisions of this Court established not only that <i>res judicata</i> was inapplicable, <i>e. g., </i><i>Salinger</i> v. <i>Loisel,</i> <span class="citation" data-id="100433"><a href="/opinion/100433/salinger-v-loisel/#230" aria-description="Citation for case: Salinger v. Loisel">265 U. S. 224, 230</a></span> (1924); <i>Fay</i> v. <i>Noia,</i> <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">372 U. S. 391</a></span>, 423 <span class="star-pagination">*191</span> (1963), but also that federal courts were obliged in appropriate cases to redetermine issues of fact and federal law. By the same token, the Court developed a number of limiting principles to restrain open-ended relitigation, among them that a successive habeas corpus application raising grounds rejected in a previous application might be denied without reaching the merits. <i>Salinger</i> v. <span class="citation" data-id="100433"><a href="/opinion/100433/salinger-v-loisel/#231" aria-description="Citation for case: Salinger v. Loisel"><i>Loisel, supra,</i> at 231</a></span>.</p>
<p>In 1948, Congress codified a version of the <i><span class="citation" data-id="100433"><a href="/opinion/100433/salinger-v-loisel/" aria-description="Citation for case: Salinger v. Loisel">Salinger</a></span></i> rule in <span class="citation no-link">28 U. S. C. § 2244</span>. As redesignated and amended in 1966, § 2244 (b) shields against senseless repetition of claims by state prisoners without endangering the principle that each is entitled, other limitations aside, to a redetermination of his federal claims by a federal court on habeas corpus. With this in mind, the purpose of § 2244 (c), also enacted in 1966, becomes clear. This subsection embodies a recognition that if this Court has "actually adjudicated" a claim on direct appeal or certiorari, a state prisoner has had the federal redetermination to which he is entitled. A subsequent application for habeas corpus raising the same claims would serve no valid purpose and would add unnecessarily to an already overburdened system of criminal justice.<sup>[1]</sup></p>
<p>In this light, we review our cases explicating the disposition "affirmed by an equally divided Court." On what was apparently the first occasion of an equal division, <span class="star-pagination">*192</span> <i>The Antelope,</i> <span class="citation" data-id="85455"><a href="/opinion/85455/the-antelope/" aria-description="Citation for case: The Antelope">10 Wheat. 66</a></span> (1825), the Court simply affirmed on the point of division without much discussion. <span class="citation" data-id="85455"><a href="/opinion/85455/the-antelope/#126" aria-description="Citation for case: The Antelope"><i>Id.,</i> at 126-127</a></span>. Faced with a similar division during the next Term, the Court again affirmed, Chief Justice Marshall explaining that "the principles of law which have been argued, cannot be settled; but the judgment is affirmed, the court being divided in opinion upon it." <i>Etting</i> v. <i>Bank of the United States,</i> <span class="citation" data-id="85481"><a href="/opinion/85481/etting-v-bank-of-united-states/#78" aria-description="Citation for case: Etting v. Bank of United States">11 Wheat. 59, 78</a></span> (1826). As was later elaborated, in such cases it is the appellant or petitioner who asks the Court to overturn a lower court's decree.</p>
<blockquote>"If the judges are divided, the reversal cannot be had, for no order can be made. The judgment of the court below, therefore, stands in full force. It is, indeed, the settled practice in such case to enter a judgment of affirmance; but this is only the most convenient mode of expressing the fact that the cause is finally disposed of in conformity with the action of the court below, and that that court can proceed to enforce its judgment. The legal effect would be the same if the appeal, or writ of error, were dismissed." <i>Durant</i> v. <i>Essex Co.,</i> <span class="citation" data-id="87987"><a href="/opinion/87987/durant-v-essex-co/#112" aria-description="Citation for case: Durant v. Essex Co.">7 Wall. 107, 112</a></span> (1869).</blockquote>
<p>Nor is an affirmance by an equally divided Court entitled to precedential weight. <i>Ohio ex rel. Eaton</i> v. <i>Price,</i> <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/#264" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">364 U. S. 263, 264</a></span> (1960). We decline to construe § 2244 (c)'s bar as extending to claims on which the judgment of a state court stands because of the absence of a majority position in this Court, and accordingly conclude that the courts below properly reached the merits.<sup>[2]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*193</span> II</h2>
<p>We proceed, then, to consider respondent's due process claim.<sup>[3]</sup> As the claim turns upon the facts, we must first review the relevant testimony at the jury trial and at the habeas corpus hearing regarding the rape and the identification. The victim testified at trial that on the evening of January 22, 1965, a youth with a butcher knife grabbed her in the doorway to her kitchen:</p>
<blockquote>"A. [H]e grabbed me from behind, and grappled twisted me on the floor. Threw me down on the floor.</blockquote>
<blockquote>"Q. And there was no light in that kitchen?</blockquote>
<blockquote>
<span class="star-pagination">*194</span> "A. Not in the kitchen.</blockquote>
<blockquote>"Q. So you couldn't have seen him then?</blockquote>
<blockquote>"A. Yes, I could see him, when I looked up in his face.</blockquote>
<blockquote>"Q. In the dark?</blockquote>
<blockquote>"A. He was right in the doorwayit was enough light from the bedroom shining through. Yes, I could see who he was.</blockquote>
<blockquote>"Q. You could see? No light? And you could see him and know him then?</blockquote>
<blockquote>"A. Yes." Tr. of Rec. in No. 237, O. T. 1967, pp. 33-34.</blockquote>
<p>When the victim screamed, her 12-year-old daughter came out of her bedroom and also began to scream. The assailant directed the victim to "tell her [the daughter] to shut up, or I'll kill you both." She did so, and was then walked at knifepoint about two blocks along a railroad track, taken into a woods, and raped there. She testified that "the moon was shining brightly, full moon." After the rape, the assailant ran off, and she returned home, the whole incident having taken between 15 minutes and half an hour.</p>
<p>She then gave the police what the Federal District Court characterized as "only a very general description," describing him as "being fat and flabby with smooth skin, bushy hair and a youthful voice." Additionally, though not mentioned by the District Court, she testified at the habeas corpus hearing that she had described her assailant as being between 16 and 18 years old and between five feet ten inches and six feet tall, as weighing between 180 and 200 pounds, and as having a dark brown complexion. This testimony was substantially corroborated by that of a police officer who was testifying from his notes.</p>
<p>On several occasions over the course of the next seven months, she viewed suspects in her home or at the police <span class="star-pagination">*195</span> station, some in lineups and others in showups, and was shown between 30 and 40 photographs. She told the police that a man pictured in one of the photographs had features similar to those of her assailant, but identified none of the suspects. On August 17, the police called her to the station to view respondent, who was being detained on another charge. In an effort to construct a suitable lineup, the police checked the city jail and the city juvenile home. Finding no one at either place fitting respondent's unusual physical description, they conducted a showup instead.</p>
<p>The showup itself consisted of two detectives walking respondent past the victim. At the victim's request, the police directed respondent to say "shut up or I'll kill you." The testimony at trial was not altogether clear as to whether the victim first identified him and then asked that he repeat the words or made her identification after he had spoken.<sup>[4]</sup> In any event, the victim testified that she had "no doubt" about her identification. At the habeas corpus hearing, she elaborated in response to questioning.</p>
<blockquote>"A. That I have no doubt, I mean that I am sure that when Isee, when I first laid eyes on him, I <span class="star-pagination">*196</span> knew that it was the individual, because his face well, there was just something that I don't think I could ever forget. I believe_____</blockquote>
<blockquote>"Q. You say when you first laid eyes on him, which time are you referring to?</blockquote>
<blockquote>"A. When I identified himwhen I seen him in the courthouse when I was took up to view the suspect." App. 127.</blockquote>
<p>We must decide whether, as the courts below held, this identification and the circumstances surrounding it failed to comport with due process requirements.</p>
<p></p>
<h2>III</h2>
<p>We have considered on four occasions the scope of due process protection against the admission of evidence deriving from suggestive identification procedures. In <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span> (1967), the Court held that the defendant could claim that "the confrontation conducted . . . was so unnecessarily suggestive and conducive to irreparable mistaken identification that he was denied due process of law." <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#301" aria-description="Citation for case: Stovall v. Denno"><i>Id.,</i> at 301-302</a></span>. This, we held, must be determined "on the totality of the circumstances." We went on to find that on the facts of the case then before us, due process was not violated, emphasizing that the critical condition of the injured witness justified a showup in her hospital room. At trial, the witness, whose view of the suspect at the time of the crime was brief, testified to the out-of-court identification, as did several police officers present in her hospital room, and also made an in-court identification.</p>
<p>Subsequently, in a case where the witnesses made in-court identifications arguably stemming from previous exposure to a suggestive photographic array, the Court restated the governing test:</p>
<blockquote>"[W]e hold that each case must be considered on its own facts, and that convictions based on eyewitness <span class="star-pagination">*197</span> identification at trial following a pretrial identification by photograph will be set aside on that ground only if the photographic identification procedure was so impermissibly suggestive as to give rise to a very substantial likelihood of irreparable misidentification." <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 384</a></span> (1968).</blockquote>
<p>Again we found the identification procedure to be supportable, relying both on the need for prompt utilization of other investigative leads and on the likelihood that the photographic identifications were reliable, the witnesses having viewed the bank robbers for periods of up to five minutes under good lighting conditions at the time of the robbery.</p>
<p>The only case to date in which this Court has found identification procedures to be violative of due process is <i>Foster</i> v. <i>California,</i> <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/#442" aria-description="Citation for case: Foster v. California">394 U. S. 440, 442</a></span> (1969). There, the witness failed to identify Foster the first time he confronted him, despite a suggestive lineup. The police then arranged a showup, at which the witness could make only a tentative identification. Ultimately, at yet another confrontation, this time a lineup, the witness was able to muster a definite identification. We held all of the identifications inadmissible, observing that the identifications were "all but inevitable" under the circumstances. <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/#443" aria-description="Citation for case: Foster v. California"><i>Id.,</i> at 443</a></span>.</p>
<p>In the most recent case of <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970), we held admissible an in-court identification by a witness who had a fleeting but "real good look" at his assailant in the headlights of a passing car. The witness testified at a pretrial suppression hearing that he identified one of the petitioners among the participants in the lineup before the police placed the participants in a formal line. MR. JUSTICE BRENNAN for four members of the Court stated that this evidence could support a finding that the in-court identification was <span class="star-pagination">*198</span> "entirely based upon observations at the time of the assault and not at all induced by the conduct of the lineup." <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#5" aria-description="Citation for case: Coleman v. Alabama"><i>Id.,</i> at 5-6</a></span>.</p>
<p>Some general guidelines emerge from these cases as to the relationship between suggestiveness and misidentification. It is, first of all, apparent that the primary evil to be avoided is "a very substantial likelihood of irreparable misidentification." <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U. S., at 384</a></span>. While the phrase was coined as a standard for determining whether an in-court identification would be admissible in the wake of a suggestive out-of-court identification, with the deletion of "irreparable" it serves equally well as a standard for the admissibility of testimony concerning the out-of-court identification itself.<sup>[5]</sup> It is the likelihood of misidentification which violates a defendant's right to due process, and it is this which was the basis of the exclusion of evidence in <i><span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">Foster</a></span>.</i> Suggestive confrontations are disapproved because they increase the likelihood of misidentification, and unnecessarily suggestive ones are condemned for the further reason that the increased chance of misidentification is gratuitous. But as <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> makes clear, the admission of evidence of a showup without more does not violate due process.</p>
<p>What is less clear from our cases is whether, as intimated by the District Court, unnecessary suggestiveness <span class="star-pagination">*199</span> alone requires the exclusion of evidence.<sup>[6]</sup> While we are inclined to agree with the courts below that the police did not exhaust all possibilities in seeking persons physically comparable to respondent, we do not think that the evidence must therefore be excluded. The purpose of a strict rule barring evidence of unnecessarily suggestive confrontations would be to deter the police from using a less reliable procedure where a more reliable one may be available, and would not be based on the assumption that in every instance the admission of evidence of such a confrontation offends due process. <i>Clemons</i> v. <i>United States,</i> 133 U. S. App. D. C. 27, 48, <span class="citation" data-id="9454404"><a href="/opinion/284140/malcus-t-clemons-v-united-states-of-america-david-e-clark-v-united/#1251" aria-description="Citation for case: Malcus T. Clemons v. United States of America, David E....">408 F. 2d 1230, 1251</a></span> (1968) (Leventhal, J., concurring); cf. <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#273" aria-description="Citation for case: Gilbert v. California">388 U. S. 263, 273</a></span> (1967); <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961). Such a rule would have no place in the present case, since both the confrontation and the trial preceded <i>Stovall</i> v. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Denno, supra</a></span></i><i>,</i> when we first gave notice that the suggestiveness of confrontation procedures was anything other than a matter to be argued to the jury.</p>
<p>We turn, then, to the central question, whether under the "totality of the circumstances" the identification was reliable even though the confrontation procedure was suggestive. As indicated by our cases, the factors to be considered in evaluating the likelihood of misidentification include the opportunity of the witness to view the criminal at the time of the crime, the witness' degree of attention, the accuracy of the witness' prior description of the criminal, the level of certainty demonstrated by the witness at the confrontation, and the length of time <span class="star-pagination">*200</span> between the crime and the confrontation. Applying these factors, we disagree with the District Court's conclusion.</p>
<p>In part, as discussed above, we think the District Court focused unduly on the relative reliability of a lineup as opposed to a showup, the issue on which expert testimony was taken at the evidentiary hearing. It must be kept in mind also that the trial was conducted before <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> and that therefore the incentive was lacking for the parties to make a record at trial of facts corroborating or undermining the identification. The testimony was addressed to the jury, and the jury apparently found the identification reliable. Some of the State's testimony at the federal evidentiary hearing may well have been self-serving in that it too neatly fit the case law, but it surely does nothing to undermine the state record, which itself fully corroborated the identification.</p>
<p>We find that the District Court's conclusions on the critical facts are unsupported by the record and clearly erroneous. The victim spent a considerable period of time with her assailant, up to half an hour. She was with him under adequate artificial light in her house and under a full moon outdoors, and at least twice, once in the house and later in the woods, faced him directly and intimately. She was no casual observer, but rather the victim of one of the most personally humiliating of all crimes.<sup>[7]</sup> Her description to the police, which included the assailant's approximate age, height, weight, complexion, skin texture, build, and voice, might not have satisfied Proust but was more than ordinarily thorough. She had "no doubt" that respondent was the person who raped her. In the nature of the crime, there are rarely witnesses to a rape other than the victim, who often has a limited <span class="star-pagination">*201</span> opportunity of observation.<sup>[8]</sup> The victim here, a practical nurse by profession, had an unusual opportunity to observe and identify her assailant. She testified at the habeas corpus hearing that there was something about his face "I don't think I could ever forget." App. 127.</p>
<p>There was, to be sure, a lapse of seven months between the rape and the confrontation. This would be a seriously negative factor in most cases. Here, however, the testimony is undisputed that the victim made no previous identification at any of the showups, lineups, or photographic showings. Her record for reliability was thus a good one, as she had previously resisted whatever suggestiveness inheres in a showup. Weighing all the factors, we find no substantial likelihood of misidentification. The evidence was properly allowed to go to the jury.<sup>[9]</sup></p>
<p><i>Affirmed in part, reversed in part, and remanded.</i></p>
<p>MR. JUSTICE MARSHALL took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE BRENNAN, with whom MR. JUSTICE DOUGLAS and MR. JUSTICE STEWART concur, concurring in part and dissenting in part.</p>
<p>We granted certiorari in this case to determine whether our affirmance by an equally divided Court of respondent's state conviction constitutes an actual adjudication <span class="star-pagination">*202</span> within the meaning of <span class="citation no-link">28 U. S. C. § 2244</span> (c), and thus bars subsequent consideration of the same issues on federal habeas corpus. The Court holds today that such an affirmance does not bar further federal relief, and I fully concur in that aspect of the Court's opinion. Regrettably, however, the Court also addresses the merits and delves into the factual background of the case to reverse the District Court's finding, upheld by the Court of Appeals, that under the "totality of the circumstances," the pre-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> showup was so impermissibly suggestive as to give rise to a substantial likelihood of misidentification. This is an unjustified departure from our long-established practice not to reverse findings of fact concurred in by two lower courts unless shown to be clearly erroneous. See, <i>e. g., </i><i>Blau</i> v. <i>Lehman,</i> <span class="citation" data-id="9422327"><a href="/opinion/106328/blau-v-lehman/#408" aria-description="Citation for case: Blau v. Lehman">368 U. S. 403, 408-409</a></span> (1962); <i>Faulkner</i> v. <i>Gibbs,</i> <span class="citation" data-id="104726"><a href="/opinion/104726/faulkner-v-gibbs/#268" aria-description="Citation for case: Faulkner v. Gibbs">338 U. S. 267, 268</a></span> (1949); <i>United States</i> v. <i>Dickinson,</i> <span class="citation" data-id="104451"><a href="/opinion/104451/united-states-v-dickinson/#751" aria-description="Citation for case: United States v. Dickinson">331 U. S. 745, 751</a></span> (1947); <i>United States</i> v. <i>Commercial Credit Co.,</i> <span class="citation" data-id="101908"><a href="/opinion/101908/united-states-v-commercial-credit-co/#67" aria-description="Citation for case: United States v. Commercial Credit Co.">286 U. S. 63, 67</a></span> (1932); <i>United States</i> v. <i>Chemical Foundation,</i> <span class="citation" data-id="100923"><a href="/opinion/100923/united-states-v-chemical-foundation-inc/#14" aria-description="Citation for case: United States v. Chemical Foundation, Inc.">272 U. S. 1, 14</a></span> (1926); <i>Baker</i> v. <i>Schofield,</i> <span class="citation" data-id="98883"><a href="/opinion/98883/baker-v-schofield/#118" aria-description="Citation for case: Baker v. Schofield">243 U. S. 114, 118</a></span> (1917); <i>Towson</i> v. <i>Moore,</i> <span class="citation" data-id="94988"><a href="/opinion/94988/towson-v-moore/#24" aria-description="Citation for case: Towson v. Moore">173 U. S. 17, 24</a></span> (1899); cf. <i>Boulden</i> v. <i>Holman,</i> <span class="citation" data-id="9423981"><a href="/opinion/107893/boulden-v-holman/#480" aria-description="Citation for case: Boulden v. Holman">394 U. S. 478, 480-481</a></span> (1969).</p>
<p>As the Court recognizes, a pre-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> identification obtained as a result of an unnecessarily suggestive showup may still be introduced in evidence if, under the "totality of the circumstances," the identification retains strong indicia of reliability. After an extensive hearing and careful review of the state court record, however, the District Court found that, under the circumstances of this case, there existed an intolerable risk of misidentification. Moreover, in making this determination, the court specifically found that "the complaining witness did not get an opportunity to obtain a good view of the suspect during the commission of the crime," "the show-up confrontation was not conducted near the time of the alleged crime, but, rather, some seven months after its commission," <span class="star-pagination">*203</span> and the complaining witness was unable to give "a good physical description of her assailant" to the police. App. 41-42. The Court of Appeals, which conducted its own review of the record, upheld the District Court's findings in their entirety. <span class="citation" data-id="9457324"><a href="/opinion/298978/archie-nathaniel-biggers-v-william-s-neil-warden-tennessee-state/#95" aria-description="Citation for case: Archie Nathaniel Biggers v. William S. Neil, Warden,...">448 F. 2d 91, 95</a></span> (CA6 1971).</p>
<p>Although this case would seem to fall squarely within the bounds of the "two-court" rule, the Court seems to suggest that the rule is "inapplicable here" because "this is a habeas corpus case in which the facts are contained primarily in the state court record (equally available to us as to the federal courts below) . . . ." <i>Ante,</i> at 193 n. 3. The "two-court" rule, however, rests upon more than mere deference to the trier of fact who has a firsthand opportunity to observe the testimony and to gauge the credibility of witnesses. For the rule also serves as an indispensable judicial "time-saver," making it unnecessary for this Court to waste scarce time and resources on minor factual questions which have already been accorded consideration by two federal courts and whose resolution is without significance except to the parties immediately involved. Thus, the "two-court" rule must logically apply even where, as here, the lower courts' findings of fact are based primarily upon the state court record.</p>
<p>The Court argues further, however, that the rule is irrelevant here because, in its view, "the dispute between the parties is not so much over the elemental facts as over the constitutional significance to be attached to them." <i>Ante,</i> at 193 n. 3. I cannot agree. Even a cursory examination of the Court's opinion reveals that its concern is not limited solely to the proper application of legal principles but, rather, extends to an essentially <i>de novo</i> inquiry into such "elemental facts" as the nature of the victim's opportunity to observe the assailant and the type of description the victim gave <span class="star-pagination">*204</span> the police at the time of the crime. And although we might reasonably disagree with the lower courts' findings as to such matters, the "two-court" rule wisely inhibits us from cavalierly substituting our own view of the facts simply because we might adopt a different construction of the evidence or resolve the ambiguities differently. On the contrary, these findings are "final here in the absence of very exceptional showing of error." <i>Comstock</i> v. <i>Group of Institutional Investors,</i> <span class="citation" data-id="9420225"><a href="/opinion/104591/comstock-v-group-of-institutional-investors/#214" aria-description="Citation for case: Comstock v. Group of Institutional Investors">335 U. S. 211, 214</a></span> (1948). The record before us is simply not susceptible of such a showing and, indeed, the petitioner does not argue otherwise. I would therefore dismiss the writ of certiorari as improvidently granted insofar as it relates to Question 2 of the Questions Presented.</p>
<h2>NOTES</h2>
<p>[1]  The legislative history adds little. The Senate Report states, cryptically, that "[t]his subsection is intended to give a conclusive presumption only to actual adjudications of Federal rights, by the Supreme Court, and not to give such a presumption to mere denials of writs of certiorari." S. Rep. No. 1797, 89th Cong., 2d Sess., 2 (1966). We conclude from this only that Congress did not expressly address itself to the effect of an affirmance by an equally divided Court. Nor is this surprising in view of the rarity of such divided affirmances in criminal cases.</p>
<p>[2]  We have been aided, and are confirmed in this view, by the thoughtful opinion of Judge Mansfield in <i>United States ex rel. Radich</i> v. <i>Criminal Ct. of City of New York,</i> <span class="citation" data-id="9458134"><a href="/opinion/303254/united-states-ex-rel-stephen-radich-v-the-criminal-court-of-the-city-of/" aria-description="Citation for case: United States Ex Rel. Stephen Radich v. The Criminal...">459 F. 2d 745</a></span> (CA2 1972), pet. for cert. pending <i>sub nom. Ross</i> v. <i>Radich,</i> No. 71-1510.</p>
<p>[3]  The dissent would have us decline to address the merits because the District Court, after an evidentiary hearing, found due process to have been violated, and the Court of Appealsafter reviewing the entire recordfound that "the conclusions of fact of the District Judge are [not] clearly erroneous." <span class="citation" data-id="9457324"><a href="/opinion/298978/archie-nathaniel-biggers-v-william-s-neil-warden-tennessee-state/#95" aria-description="Citation for case: Archie Nathaniel Biggers v. William S. Neil, Warden,...">448 F. 2d 91, 95</a></span>. It is said that we should not depart from "our long-established practice not to reverse findings of fact concurred in by two lower courts unless shown to be clearly erroneous." <i>Post,</i> at 202. This rule of practice, under which the Court does not lightly overturn the concurrent findings of fact of two lower federal courts, is a salutary one to be followed where applicable. We think it inapplicable here where the dispute between the parties is not so much over the elemental facts as over the constitutional significance to be attached to them. Moreover, this is a habeas corpus case in which the facts are contained primarily in the state court record (equally available to us as to the federal courts below) and where the evidentiary hearing in the District Court purported to be "confined" to two specific issues which we deem not controlling. Of the nine cases cited in the dissenting opinion in support of the rule of practice urged upon us, eight of them involved civil litigation in the federal system. Only one of the cases cited, <i>Boulden</i> v. <i>Holman,</i> <span class="citation" data-id="9423981"><a href="/opinion/107893/boulden-v-holman/" aria-description="Citation for case: Boulden v. Holman">394 U. S. 478</a></span> (1969), involved a habeas corpus review and the Court simply heldon the basis of "an independent study of the entire record"that the conclusion reached by the District Court and the Court of Appeals "was justified." <span class="citation" data-id="9423981"><a href="/opinion/107893/boulden-v-holman/#480" aria-description="Citation for case: Boulden v. Holman"><i>Id.,</i> at 480, 481</a></span>.</p>
<p>[4]  At trial, one of the police officers present at the identification testified explicitly that the words were spoken after the identification. The victim testified:
</p>
<p>"Q. What physical characteristics, if any, caused you to be able to identify him?</p>
<p>"A. First of all,uhhis size,next I could remember his voice.</p>
<p>"Q. What about his voice? Describe his voice to the Jury.</p>
<p>"A. Well, he has the voice of an immature youthI call it an immature youth. I have teen-age boys. And that was the first thing that made me think it was the boy." Tr. of Rec. in No. 237, O. T. 1967, p. 17.</p>
<p>The colloquy continued, with the victim describing the voice and other physical characteristics. At the habeas corpus hearing, the victim and all of the police witnesses testified that a visual identification preceded the voice identification. App. 80, 123, 134.</p>
<p>[5]  See <i>Clemons</i> v. <i>United States,</i> 133 U. S. App. D. C. 27, 47, <span class="citation" data-id="9454404"><a href="/opinion/284140/malcus-t-clemons-v-united-states-of-america-david-e-clark-v-united/#1250" aria-description="Citation for case: Malcus T. Clemons v. United States of America, David E....">408 F. 2d 1230, 1250</a></span> (1968) (McGowan, J., for the court <i>en banc</i>), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./394/964/">394 U. S. 964</a></span> (1969). In the present case, there has been controversy, in our view irrelevant, over whether, as she testified at the habeas corpus hearing, the victim actually made an in-court identification. While we think it evident from the many testimonial links between her out-of-court identification and "the defendant" before her in court that the answer is "yes," we recognize that if the testimony concerning the out-of-court identification was inadmissible, the conviction must be overturned.</p>
<p>[6]  The District Court stated:
</p>
<p>"In this case it appears to the Court that a line-up, which both sides admit is generally more reliable than a show-up, could have been arranged. The fact that this was not done tended needlessly to decrease the fairness of the identification process to which petitioner was subjected." App. 42.</p>
<p>[7]  See <i>United States ex rel. Phipps</i> v. <i>Follette,</i> <span class="citation" data-id="291028"><a href="/opinion/291028/united-states-of-america-ex-rel-robert-phipps-relator-appellant-v-harold/#915" aria-description="Citation for case: United States of America Ex Rel. Robert Phipps,...">428 F. 2d 912, 915-916</a></span> (CA2) (Friendly, J.), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./400/908/">400 U. S. 908</a></span> (1970).</p>
<p>[8]  Respondent attaches some weight to the failure of the victim's daughter to identify him. Apart from the fact that this does not bear directly on the reliability of her mother's identification, the girl was only 12 years old and had, as best we can tell, only a very brief view of the assailant from across the room.</p>
<p>[9]  Respondent's habeas corpus petition raised a number of other claims, including one challenging the legality of his detention at the time he was viewed by the victim. The courts below did not address these claims, nor do we.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Nix v. Williams.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Nix v. Williams"
type: case
citation: "467 U.S. 431 (1984)"
parallel_cite: "104 S. Ct. 2501; 81 L. Ed. 2d 377; 52 U.S.L.W. 4732"
neutral_cite: 1984 U.S. LEXIS 101
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-06-11
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-06-11
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Nix v. Williams
  varies_by_point: false
  scope_note: "Establishes the inevitable-discovery exception to the exclusionary rule; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111204/nix-v-williams/"
  cluster_id: 111204
  opinion_id: 9429647
  identity_checked: true
homes:
  - page: "[[Inevitable Discovery & Independent Source]]"
    role: "Key — Progeny / Refinement"
related: ["[[Murray v. United States]]", "[[Brewer v. Williams]]", "[[Segura v. United States]]", "[[Wong Sun v. United States]]"]
aliases: []
tags: ["case", "exclusionary-rule", "inevitable-discovery", "fruit-of-the-poisonous-tree"]
holding: "Inevitable discovery: unlawfully obtained evidence is admissible if the prosecution proves by a preponderance it would inevitably have…"
lake:
  record_id: Nix v. Williams
  status: verified
  projected_at: 2026-07-06
---

# Nix v. Williams

*467 U.S. 431 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After his arrest for the murder of a 10-year-old girl, Williams was subjected to the "Christian burial speech" that led him to direct police to the body — interrogation later held to have violated his right to counsel (*[[Brewer v. Williams]]*). At the same time, a large organized volunteer search party was systematically searching the area and was within a few miles of the body. At Williams's retrial, the body-related evidence was admitted on an inevitable-discovery theory.

## Issue
Whether evidence obtained as the fruit of a constitutional violation is nevertheless admissible if it would inevitably have been discovered by lawful means.

## Rule
Yes. "If the prosecution can establish by a preponderance of the evidence that the information ultimately or inevitably would have been discovered by lawful means . . . then the deterrence rationale has so little basis that the evidence should be received." — 467 U.S. at 444. ^pin-444

The prosecution need not also prove the absence of police bad faith.

## Application
The volunteer search party was conducting an organized, systematic search and, in the normal course, would have discovered the body in essentially the same condition; the State proved by a preponderance that the body and related evidence would inevitably have been found by lawful means. The evidence was therefore admissible despite the antecedent right-to-counsel violation.

## Conclusion
The body-related evidence was admissible under the inevitable-discovery doctrine; the grant of [[Common Legal Terms#habeas-corpus|habeas]] relief was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Nix* establishes [[Inevitable Discovery and Independent Source|inevitable discovery]] as a sibling of the independent-source doctrine ([[Murray v. United States]]), both grounded in restoring the police to the position they would have occupied absent the illegality.

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *Nix v. Williams*, 467 U.S. 431 (1984) — https://www.courtlistener.com/opinion/111204/nix-v-williams/ — pinpoint: 444.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e9bbe273752141d6", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Nix v. Williams"}, "payload": {"all": [{"cite": "467 U.S. 431", "page": "431", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "467"}, {"cite": "104 S. Ct. 2501", "page": "2501", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "104"}, {"cite": "81 L. Ed. 2d 377", "page": "377", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "81"}, {"cite": "1984 U.S. LEXIS 101", "page": "101", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1984"}, {"cite": "52 U.S.L.W. 4732", "page": "4732", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "52"}], "display": "467 U.S. 431", "official": {"cite": "467 U.S. 431", "page": "431", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "467"}, "official_selection_present": true, "record_id": "Nix v. Williams"}}
{"assertion_id": "54c196006984037e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-444", "record_id": "Nix v. Williams"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-444", "pinpoint_status": "slip-only", "quote": "that led him to direct police to the body — interrogation later held to have violated his right to counsel (*Brewer v. Williams*). At the same time, a large organized volunteer search party was systematically searching the area and was within a few miles of the body. At Williams's retrial, the body-related evidence was admitted on an inevitable-discovery theory. ## Issue Whether evidence obtained as the fruit of a constitutional violation is nevertheless admissible if it would inevitably have been discovered by lawful means. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Nix v. Williams", "star_marker": null}}
{"assertion_id": "95896b78e1501a68", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Nix v. Williams"}, "payload": {"as_of_content": "1984-06-11", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Nix v. Williams", "scope_note": "Establishes the inevitable-discovery exception to the exclusionary rule; good law.", "varies_by_point": false}}
```

### lake record — Nix v. Williams

```json
{
  "schema_version": "s2.v1",
  "record_id": "Nix v. Williams",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Nix v. Williams",
    "case_name_short": "Nix",
    "case_name_full": "Nix, Warden of the Iowa State Penitentiary v. Williams",
    "input_case_name": "Nix v. Williams",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-06-11",
    "year": 1984,
    "docket": null,
    "cluster_id": 111204,
    "lead_opinion_id": 9429647,
    "sibling_ids": [
      111204,
      9429647,
      9429648,
      9429649,
      9429650
    ],
    "absolute_url": "/opinion/111204/nix-v-williams/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "467 U.S. 431",
      "volume": "467",
      "reporter": "U.S.",
      "page": "431",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 2501",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2501",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 L. Ed. 2d 377",
        "volume": "81",
        "reporter": "L. Ed. 2d",
        "page": "377",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4732",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4732",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 101",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "101",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "467 U.S. 431",
        "volume": "467",
        "reporter": "U.S.",
        "page": "431",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 2501",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2501",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 L. Ed. 2d 377",
        "volume": "81",
        "reporter": "L. Ed. 2d",
        "page": "377",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 101",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "101",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4732",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4732",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "467 U.S. 431",
    "official_selection": {
      "court_class": "scotus",
      "selected": "467 U.S. 431",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-444",
      "page": null,
      "quote": "that led him to direct police to the body \u2014 interrogation later held to have violated his right to counsel (*Brewer v. Williams*). At the same time, a large organized volunteer search party was systematically searching the area and was within a few miles of the body. At Williams's retrial, the body-related evidence was admitted on an inevitable-discovery theory. ## Issue Whether evidence obtained as the fruit of a constitutional violation is nevertheless admissible if it would inevitably have been discovered by lawful means. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-06-11",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Nix v. Williams",
    "varies_by_point": false,
    "scope_note": "Establishes the inevitable-discovery exception to the exclusionary rule; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 10705828,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Seneca Warrior Steeprock",
          "cluster_id": 10102625,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane1_negative"
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
        "journal_ref": "Nix v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Michael Hillery",
          "cluster_id": 4868029,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Michael Hillery",
          "cluster_id": 4865672,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kennebrew v. State",
          "cluster_id": 10366687,
          "cite": [
            "304 Ga. 406"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Wallace",
          "cluster_id": 6239020,
          "cite": [
            "222 Cal. Rptr. 3d 795",
            "15 Cal. App. 5th 82",
            "2017 Cal. App. LEXIS 775"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Turpin",
          "cluster_id": 4423584,
          "cite": [
            "2017 Ohio 7435",
            "96 N.E.3d 1171"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Matthew Elliot Cohagan",
          "cluster_id": 4421478,
          "cite": [
            "162 Idaho 717",
            "404 P.3d 659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane1_negative"
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
        "journal_ref": "Nix v. Williams:lane2_top_cited"
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
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bourjaily v. United States",
          "cluster_id": 111938,
          "cite": [
            "97 L. Ed. 2d 144",
            "107 S. Ct. 2775",
            "483 U.S. 171",
            "1987 U.S. LEXIS 2874",
            "22 Fed. R. Serv. 1105",
            "55 U.S.L.W. 4962"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
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
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. Seibert",
          "cluster_id": 137002,
          "cite": [
            "159 L. Ed. 2d 643",
            "124 S. Ct. 2601",
            "542 U.S. 600",
            "2004 U.S. LEXIS 4578"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray v. United States",
          "cluster_id": 112136,
          "cite": [
            "101 L. Ed. 2d 472",
            "108 S. Ct. 2529",
            "487 U.S. 533",
            "1988 U.S. LEXIS 2881",
            "56 U.S.L.W. 4801"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Dominguez-Castor",
          "cluster_id": 4691722,
          "cite": [
            "2020 COA 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
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
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Medina v. California",
          "cluster_id": 112775,
          "cite": [
            "120 L. Ed. 2d 353",
            "112 S. Ct. 2572",
            "505 U.S. 437",
            "1992 U.S. LEXIS 3696"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Arkansas",
          "cluster_id": 117936,
          "cite": [
            "131 L. Ed. 2d 976",
            "115 S. Ct. 1914",
            "514 U.S. 927",
            "1995 U.S. LEXIS 3464"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Kraft",
          "cluster_id": 2590211,
          "cite": [
            "5 P.3d 68",
            "99 Cal. Rptr. 2d 1",
            "23 Cal. 4th 978",
            "2000 Daily Journal DAR 8825",
            "2000 Cal. Daily Op. Serv. 6660",
            "2000 Cal. LEXIS 5822"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Coffman",
          "cluster_id": 2623595,
          "cite": [
            "96 P.3d 30",
            "17 Cal. Rptr. 3d 710",
            "34 Cal. 4th 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
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
        "journal_ref": "Nix v. Williams:lane2_top_cited"
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
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Zapien",
          "cluster_id": 1367717,
          "cite": [
            "846 P.2d 704",
            "4 Cal. 4th 929",
            "17 Cal. Rptr. 2d 122",
            "93 Daily Journal DAR 2940",
            "93 Cal. Daily Op. Serv. 1612",
            "1993 Cal. LEXIS 756"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Patane",
          "cluster_id": 137003,
          "cite": [
            "159 L. Ed. 2d 667",
            "124 S. Ct. 2620",
            "542 U.S. 630",
            "2004 U.S. LEXIS 4577"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hayes v. Florida",
          "cluster_id": 111382,
          "cite": [
            "84 L. Ed. 2d 705",
            "105 S. Ct. 1643",
            "470 U.S. 811",
            "1985 U.S. LEXIS 1523",
            "53 U.S.L.W. 4382"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Montoya",
          "cluster_id": 1202376,
          "cite": [
            "753 P.2d 729",
            "12 Brief Times Rptr. 482",
            "1988 Colo. LEXIS 39",
            "1988 WL 25119"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aaron Lindh v. James P. Murphy, Warden",
          "cluster_id": 726705,
          "cite": [
            "96 F.3d 856",
            "1996 U.S. App. LEXIS 24136",
            "1996 WL 517290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
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
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Sutherland",
          "cluster_id": 2036519,
          "cite": [
            "860 N.E.2d 178",
            "223 Ill. 2d 187",
            "307 Ill. Dec. 524"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Moody",
          "cluster_id": 867478,
          "cite": [
            "94 P.3d 1119",
            "208 Ariz. 424"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ramirez",
          "cluster_id": 118180,
          "cite": [
            "140 L. Ed. 2d 191",
            "118 S. Ct. 992",
            "523 U.S. 65",
            "1998 U.S. LEXIS 1600"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brimage v. State",
          "cluster_id": 2417512,
          "cite": [
            "918 S.W.2d 466",
            "1996 Tex. Crim. App. LEXIS 5",
            "1994 WL 511395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nix v. Williams:lane2_top_cited"
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
        "journal_ref": "Nix v. Williams:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111204 OR 9429647 OR 9429648 OR 9429649 OR 9429650) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDkyNzMyODAwMDAwJnM9NDM4NjA3OSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111204+OR+9429647+OR+9429648+OR+9429649+OR+9429650%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(111204 OR 9429647 OR 9429648 OR 9429649 OR 9429650)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNDAmcz0xNDMyMjk0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111204+OR+9429647+OR+9429648+OR+9429649+OR+9429650%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111204 OR 9429647 OR 9429648 OR 9429649 OR 9429650)",
        "reviewed": 69,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 69,
        "triage_read": 2,
        "triage_snippet_classified": 67
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111204 OR 9429647 OR 9429648 OR 9429649 OR 9429650)",
    "indexed_citing_opinions": 1839,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111204,
        "count": 1618,
        "count_source": "search"
      },
      {
        "opinion_id": 9429647,
        "count": 249,
        "count_source": "search"
      },
      {
        "opinion_id": 9429648,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429649,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429650,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3080,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/nix-v-williams.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwMTE3NyZzPTEwMTMyOTkxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111204+OR+9429647+OR+9429648+OR+9429649+OR+9429650%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111204,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 107423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 108429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 108846,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 108967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 109310,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 109590,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 109757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 109816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 110067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 110230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 110300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 110372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 110589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 110676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 111169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 260072,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 260805,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 289216,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 354373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 374338,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 382927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 393006,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 405982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 410451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 414450,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 414492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 416957,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 1669210,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 1764351,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 1861096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 2115457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 2118871,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 2216952,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111204,
        "cited_id": 3580565,
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
    "date_created": "2026-07-05T15:53:21Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:53:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:53:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:56:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:53:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Nix v. Williams

```
<opinion type="majority">
<author id="A9P"><page-number citation-index="1" label="434">*434</page-number>Chief Justice Burger</author>
<p id="ABT">delivered the opinion of the Court.</p>
<p id="Aji">We granted certiorari to consider whether, at respondent Williams’ second murder trial in state court, evidence pertaining to the discovery and condition of the victim’s body was properly admitted on the ground that it would ultimately or inevitably have been discovered even if no violation of any constitutional or statutory provision had taken place.</p>
<p id="Alq">On December 24, 1968, 10-year-old Pamela Powers disappeared from a YMCA building in Des Moines, Iowa, where she had accompanied her parents to watch an athletic contest. Shortly after she disappeared, Williams was seen leaving the YMCA carrying a large bundle wrapped in a blanket; a 14-year-old boy who had helped Williams open his car door reported that he had seen “two legs in it and they were skinny and white.”</p>
<p id="Ad8q">Williams’ car was found the next day 160 miles east of Des Moines in Davenport, Iowa. Later several items of clothing belonging to the child, some of Williams’ clothing, and an army blanket like the one used to wrap the bundle that Williams carried out of the YMCA were found at a rest stop on <page-number citation-index="1" label="435">*435</page-number>Interstate 80 near Grinnell, between Des Moines and Davenport. A warrant was issued for Williams’ arrest.</p>
<p id="b493-5">Police surmised that Williams had left Pamela Powers or her body somewhere between Des Moines and the Grinnell rest stop where some of the young girl’s clothing had been found. On December 26, the Iowa Bureau of Criminal Investigation initiated a large-scale search. Two hundred volunteers divided into teams began the search 21 miles east of Grinnell, covering an area several miles to the north and south of Interstate 80. They moved westward from Poweshiek County, in which Grinnell was located, into Jasper County. Searchers were instructed to check all roads, abandoned farm buildings, ditches, culverts, and any other place in which the body of a small child could be hidden.</p>
<p id="b493-6">Meanwhile, Williams surrendered to local police in Davenport, where he was promptly arraigned. Williams contacted a Des Moines attorney who arranged for an attorney in Davenport to meet Williams at the Davenport police station. Des Moines police informed counsel they would pick Williams up in Davenport and return him to Des Moines without questioning him. Two Des Moines detectives then drove to Davenport, took Williams into custody, and proceeded to drive him back to Des Moines.</p>
<p id="b493-7">During the return trip, one of the policemen, Detective Learning, began a conversation with Williams, saying:</p>
<blockquote id="b493-8">“I want to give you something to think about while we’re traveling down the road. .. . They are predicting several inches of snow for tonight, and I feel that you yourself are the only person that knows where this little girl’s body is . . . and if you get a snow on top of it you yourself may be unable to find it. And since we will be going right past the area [where the body is] on the way into Des Moines, I feel that we could stop and locate the body, that the parents of this little girl should be entitled to a Christian burial for the little girl who was snatched away from them on Christmas [E]ve and murdered. . . . <page-number citation-index="1" label="436">*436</page-number>[A]fter a snow storm [we may not be] able to find it at all.”</blockquote>
<p id="b494-5">Learning told Williams he knew the body was in the area of Mitchellville — a town they would be passing on the way to Des Moines. He concluded the conversation by saying: “I do not want you to answer me. . . . Just think about it . . . .”</p>
<p id="b494-6">Later, as the police car approached Grinnell, Williams asked Learning whether the police had found the young girl’s shoes. After Learning replied that he was unsure, Williams directed the police to a point near a service station where he said he had left the shoes; they were not found. As they continued the drive to Des Moines, Williams asked whether the blanket had been found and then directed the officers to a rest area in Grinnell where he said he had disposed of the blanket; they did not find the blanket. At this point Learning and his party were joined by the officers in charge of the search. As they approached Mitchellville, Williams, without any further conversation, agreed to direct the officers to the child’s body.</p>
<p id="b494-7">The officers directing the search had called off the search at 3 p. m., when they left the Grinnell Police Department to join Learning at the rest area. At that time, one search team near the Jasper County-Polk County line was only two and one-half miles from where Williams soon guided Learning and his party to the body. The child’s body was found next to a culvert in a ditch beside a gravel road in Polk County, about two miles south of Interstate 80, and essentially within the area to be searched.</p>
<p id="b494-8">B</p>
<p id="b494-9">
<em>First Trial</em>
</p>
<p id="b494-10">In February 1969 Williams was indicted for first-degree murder. Before trial in the Iowa court, his counsel moved to suppress evidence of the body and all related evidence including the condition of the body as shown by the autopsy. The ground for the motion was that such evidence was the “fruit” <page-number citation-index="1" label="437">*437</page-number>or product of Williams’ statements made during the automobile ride from Davenport to Des Moines and prompted by Learning’s statements. The motion to suppress was denied.</p>
<p id="b495-5">The jury found Williams guilty of first-degree murder; the judgment of conviction was affirmed by the Iowa Supreme Court. <em>State </em>v. <em>Williams, </em><span class="citation" data-id="9720125"><a href="/opinion/2115457/state-v-williams/" aria-description="Citation for case: State v. Williams">182 N. W. 2d 396</a></span> (1970). Williams then sought release on habeas corpus in the United States District Court for the Southern District of Iowa. That court concluded that the evidence in question had been wrongly admitted at Williams’ trial, <em>Williams </em>v. <em>Brewer, </em><span class="citation" data-id="1669210"><a href="/opinion/1669210/williams-v-brewer/" aria-description="Citation for case: Williams v. Brewer">375 F. Supp. 170</a></span> (1974); a divided panel of the Court of Appeals for the Eighth Circuit agreed. <span class="citation" data-id="9461373"><a href="/opinion/324530/robert-anthony-williams-aka-anthony-erthel-williams-v-lou-v-brewer/" aria-description="Citation for case: Robert Anthony Williams, A/K/A Anthony Erthel Williams v....">509 F. 2d 227</a></span> (1974).</p>
<p id="b495-6">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./423/1031/">423 U. S. 1031</a></span> (1975), and a divided Court affirmed, holding that Detective Learning had obtained incriminating statements from Williams by what was viewed as interrogation in violation of his right to counsel. <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387</a></span> (1977). This Court’s opinion noted, however, that although Williams’ incriminating statements could not be introduced into evidence at a second trial, evidence of the body’s location and condition “might well be admissible on the theory that the body would have been discovered in any event, even had incriminating statements not been elicited from Williams.” <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#407" aria-description="Citation for case: Brewer v. Williams"><em>Id., </em>at 407, n. 12</a></span>.</p>
<p id="b495-7">C</p>
<p id="b495-8">
<em>Second Trial</em>
</p>
<p id="b495-9">At Williams’ second trial in 1977 in the Iowa court, the prosecution did not offer Williams’ statements into evidence, nor did it seek to show that Williams had directed the police to the child’s body. However, evidence of the condition of her body as it was found, articles and photographs of her clothing, and the results of post mortem medical and chemical tests on the body were admitted. The trial court concluded that the State had proved by a preponderance of the evidence that, if the search had not been suspended and Williams had not led the police to the victim, her body would have been <page-number citation-index="1" label="438">*438</page-number>discovered <em>“within a short time” </em>in essentially the same condition as it was actually found. The trial court also ruled that if the police had not located the body, “the search would clearly have been taken up again where it left off, given the extreme circumstances of this case and the body would [have] been found <em>in short order” </em>App. 86 (emphasis added).</p>
<p id="b496-5">In finding that the body would have been discovered in essentially the same condition as it was actually found, the court noted that freezing temperatures had prevailed and tissue deterioration would have been suspended. <em>Id., </em>at 87. The challenged evidence was admitted and the jury again found Williams guilty of first-degree murder; he was sentenced to life in prison.</p>
<p id="b496-6">On appeal, the Supreme Court of Iowa again affirmed. <span class="citation" data-id="2118871"><a href="/opinion/2118871/state-v-williams/" aria-description="Citation for case: State v. Williams">285 N. W. 2d 248</a></span> (1979). That court held that there was in fact a “hypothetical independent source” exception to the exclusionary rule:</p>
<blockquote id="b496-7">“After the defendant has shown unlawful conduct on the part of the police, the State has the burden to show by a preponderance of the evidence that (1) the police did not act in bad faith for the purpose of hastening discovery of the evidence in question, and (2) that the evidence in question would have been discovered by lawful means.” <span class="citation" data-id="2118871"><a href="/opinion/2118871/state-v-williams/#260" aria-description="Citation for case: State v. Williams"><em>Id., </em>at 260</a></span>.</blockquote>
<p id="b496-8">As to the first element, the Iowa Supreme Court, having reviewed the relevant cases, stated:</p>
<blockquote id="b496-9">“The issue of the propriety of the police conduct in this case, as noted earlier in this opinion, has caused the closest possible division of views in every appellate court which has considered the question. In light of the legitimate disagreement among individuals well versed in the law of criminal procedure who were given the opportunity for calm deliberation, it cannot be said that the actions of the police were taken in bad faith.” <span class="citation" data-id="2118871"><a href="/opinion/2118871/state-v-williams/#260" aria-description="Citation for case: State v. Williams"><em>Id., </em>at 260-261</a></span>.</blockquote>
<p id="b497-4"><page-number citation-index="1" label="439">*439</page-number>The Iowa court then reviewed the evidence <em>de </em>novo<footnotemark>1</footnotemark> and concluded that the State had shown by a preponderance of the evidence that, even if Williams had not guided police to the child’s body, it would inevitably have been found by lawful activity of the search party before its condition had materially changed.</p>
<p id="b497-5">In 1980 Williams renewed his attack on the state-court conviction by seeking a writ of habeas corpus in the United States District Court for the Southern District of Iowa. The District Court conducted its own independent review of the evidence and concluded, as had the state courts, that the body would inevitably have been found by the searchers in essentially the same condition it was in when Williams led police to its discovery. The District Court denied Williams’ petition. <span class="citation" data-id="1764351"><a href="/opinion/1764351/williams-v-nix/" aria-description="Citation for case: Williams v. Nix">528 F. Supp. 664</a></span> (1981).</p>
<p id="b497-6">The Court of Appeals for the Eighth Circuit reversed, <span class="citation" data-id="9470326"><a href="/opinion/414492/robert-anthony-williams-v-crispus-nix-warden-of-the-iowa-state/" aria-description="Citation for case: Robert Anthony Williams v. Crispus Nix, Warden of the...">700 F. 2d 1164</a></span> (1983); an equally divided court denied rehearing en banc. <span class="citation" data-id="9470326"><a href="/opinion/414492/robert-anthony-williams-v-crispus-nix-warden-of-the-iowa-state/#1175" aria-description="Citation for case: Robert Anthony Williams v. Crispus Nix, Warden of the..."><em>Id., </em>at 1175</a></span>. That court assumed, without deciding, that there is an inevitable discovery exception to the exclusionary rule and that the Iowa Supreme Court correctly stated that exception to require proof that the police did not act in bad faith and that the evidence would have been discovered absent any constitutional violation. In reversing the District Court’s denial of habeas relief, the Court of Appeals stated:</p>
<blockquote id="b497-7">“We hold that the State has not met the first requirement. It is therefore unnecessary to decide whether the state courts’ finding that the body would have been discovered anyway is fairly supported by the record. It is also unnecessary to decide whether the State must prove the two elements of the exception by clear and <page-number citation-index="1" label="440">*440</page-number>convincing evidence, as defendant argues, or by a preponderance of the evidence, as the state courts held.</blockquote>
<blockquote id="A-J">“The state trial court, in denying the motion to suppress, made no finding one way or the other on the question of bad faith. Its opinion does not even mention the issue and seems to proceed on the assumption — contrary to the rule of law later laid down by the Supreme Court of Iowa — that the State needed to show only that the body would have been discovered in any event. The Iowa Supreme Court did expressly address the issue . . . and a finding by an appellate court of a state is entitled to the same presumption of correctness that attaches to trial-court findings under <span class="citation no-link">28 U. S. C. § 2254</span>(d). . . . We conclude, however, that the state Supreme Court’s finding that the police did not act in bad faith is not entitled to the shield of §2254(d) . . . .” <em>Id., </em>at 1169-1170 (footnotes omitted).</blockquote>
<p id="AMx">We granted the State’s petition for certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./461/956/">461 U. S. 956</a></span> (1983), and we reverse.</p>
<p id="AQIK">a</p>
<p id="Ai2">
<em>&gt;</em>
</p>
<p id="A68">The Iowa Supreme Court correctly stated that the “vast majority” of all courts, both state and federal, recognize an inevitable discovery exception to the exclusionary rule.<footnotemark>2</footnotemark> We <page-number citation-index="1" label="441">*441</page-number>are now urged to adopt and apply the so-called ultimate or inevitable discovery exception to the exclusionary rule.</p>
<p id="b499-5">Williams contends that evidence of the body’s location and condition is “fruit of the poisonous tree,” <em>i. e., </em>the “fruit” or product of Detective Learning’s plea to help the child’s parents give her “a Christian burial,” which this Court had already held equated to interrogation. He contends that admitting the challenged evidence violated the Sixth Amendment whether it would have been inevitably discovered or not. Williams also contends that, if the inevitable discovery doctrine is constitutionally permissible, it must include a threshold showing of police good faith.</p>
<p id="b499-6">B</p>
<p id="b499-7">The doctrine requiring courts to suppress evidence as the tainted “fruit” of unlawful governmental conduct had its genesis in <em>Silverthome Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920); there, the Court held that the exclusionary rule applies not only to the illegally obtained evidence itself, but also to other incriminating evidence derived from the primary evidence. The holding of <em>Silverthome </em>was carefully limited, however, for the Court emphasized that such information does not automatically become “sacred and inaccessible.” <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States"><em>Id., </em>at 392</a></span>.</p>
<blockquote id="b499-8">“If knowledge of [such facts] is gained from an <em>independent source, </em>they may be proved like any others . . . .” <em>Ibid, </em>(emphasis added).</blockquote>
<p id="b499-9"><em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), extended the exclusionary rule to evidence that was the indirect product or “fruit” of unlawful police conduct, but there again the Court emphasized that evidence that has been illegally obtained need not always be suppressed, stating:</p>
<blockquote id="b500-4"><page-number citation-index="1" label="442">*442</page-number>“We need not hold that all evidence is ‘fruit of the poisonous tree’ simply because it would not have come to light <em>but for the illegal actions </em>of the police. Rather, the more apt question in such a case is ‘whether, granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint. <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#487" aria-description="Citation for case: Wong Sun v. United States"><em>Id., </em>at 487-488</a></span> (emphasis added) (quoting J. Maguire, Evidence of Guilt 221 (1959)).</blockquote>
<p id="b500-5">The Court thus pointedly negated the kind of good-faith requirement advanced by the Court of Appeals in reversing the District Court.</p>
<p id="b500-6">Although <em>Silverthorne </em>and <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span> </em>involved violations of the Fourth Amendment, the “fruit of the poisonous tree” doctrine has not been limited to cases in which there has been a Fourth Amendment violation. The Court has applied the doctrine where the violations were of the Sixth Amendment, see <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), as well as of the Fifth Amendment.<footnotemark>3</footnotemark></p>
<p id="b500-7">The core rationale consistently advanced by this Court for extending the exclusionary rule to evidence that is the fruit of unlawful police conduct has been that this admittedly drastic and socially costly course is needed to deter police from <page-number citation-index="1" label="443">*443</page-number>violations of constitutional and statutory protections. This Court has accepted the argument that the way to ensure such protections is to exclude evidence seized as a result of such violations notwithstanding the high social cost of letting persons obviously guilty go unpunished for their crimes. On this rationale, the prosecution is not to be put in a better position than it would have been in if no illegality had transpired.</p>
<p id="b501-5">By contrast, the derivative evidence analysis ensures that the prosecution is not put in a <em>worse </em>position simply because of some earlier police error or misconduct. The independent source doctrine allows admission of evidence that has been discovered by means wholly independent of any constitutional violation. That doctrine, although closely related to the inevitable discovery doctrine, does not apply here; Williams’ statements to Learning indeed led police to the child’s body, but that is not the whole story. The independent source doctrine teaches us that the interest of society in deterring unlawful police conduct and the public interest in having juries receive all probative evidence of a crime are properly balanced by putting the police in the same, not a <em>worse, </em>position that they would have been in if no police error or misconduct had occurred.<footnotemark>4</footnotemark> See <em>Murphy </em>v. <em>Waterfront Comm’n of New York Harbor, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#79" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 79</a></span> (1964); <em>Kastigar </em>v. <em>United States, </em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#457" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 457, 458-459</a></span> (1972). When the challenged evidence has an independent source, exclusion of such evidence would put the police in a worse position than they would have been in absent any error or violation. There <page-number citation-index="1" label="444">*444</page-number>is a functional similarity between these two doctrines in that exclusion of evidence that would inevitably have been discovered would also put the government in a worse position, because the police would have obtained that evidence if no misconduct had taken place. Thus, while the independent source exception would not justify admission of evidence in this case, its rationale is wholly consistent with and justifies our adoption of the ultimate or inevitable discovery exception to the exclusionary rule.</p>
<p id="b502-5">It is clear that the cases implementing the exclusionary rule “begin with the premise that the challenged evidence is <em>in some sense </em>the product of illegal governmental activity.” <em>United States </em>v. <em>Crews, </em><span class="citation" data-id="9427838"><a href="/opinion/110230/united-states-v-crews/#471" aria-description="Citation for case: United States v. Crews">445 U. S. 463, 471</a></span> (1980) (emphasis added). Of course, this does not end the inquiry. If the prosecution can establish by a preponderance of the evidence that the information ultimately or inevitably would have been discovered by lawful means — here the volunteers’ search— then the deterrence rationale has so little basis that the evidence should be received.<footnotemark>5</footnotemark> Anything less would reject logic, experience, and common sense.</p>
<p id="b503-4"><page-number citation-index="1" label="445">*445</page-number>The requirement that the prosecution must prove the absence of bad faith, imposed here by the Court of Appeals, would place courts in the position of withholding from juries relevant and undoubted truth that would have been available to police absent any unlawful police activity. Of course, that view would put the police in a <em>worse </em>position than they would have been in if no unlawful conduct had transpired. And, of equal importance, it wholly fails to take into account the enormous societal cost of excluding truth in the search for truth in the administration of justice. Nothing in this Court’s prior holdings supports any such formalistic, pointless, and punitive approach.</p>
<p id="b503-5">The Court of Appeals concluded, without analysis, that if an absence-of-bad-faith requirement were not imposed, “the temptation to risk deliberate violations of the Sixth Amendment would be too great, and the deterrent effect of the Exclusionary Rule reduced too far.” <span class="citation" data-id="9470326"><a href="/opinion/414492/robert-anthony-williams-v-crispus-nix-warden-of-the-iowa-state/#1169" aria-description="Citation for case: Robert Anthony Williams v. Crispus Nix, Warden of the...">700 F. 2d, at 1169, n. 5</a></span>. We reject that view. A police officer who is faced with the opportunity to obtain evidence illegally will rarely, if ever, be in a position to calculate whether the evidence sought would inevitably be discovered. Cf. <em>United States </em>v. <em>Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#283" aria-description="Citation for case: United States v. Ceccolini">435 U. S. 268, 283</a></span> (1978):</p>
<blockquote id="b503-6">“[T]he concept of effective deterrence assumes that the police officer consciously realizes the probable consequences of a presumably impermissible course of conduct” (opinion concurring in judgment).</blockquote>
<p id="b503-7">On the other hand, when an officer is aware that the evidence will inevitably be discovered, he will try to avoid engaging in <page-number citation-index="1" label="446">*446</page-number>any questionable practice. In that situation, there will be little to gain from taking any dubious “shortcuts” to obtain the evidence. Significant disincentives to obtaining evidence illegally — including the possibility of departmental discipline and civil liability — also lessen the likelihood that the ultimate or inevitable discovery exception will promote police misconduct. See <em>Bivens </em>v. <em>Six Unknown Federal Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#397" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388, 397</a></span> (1971). In these circumstances, the societal costs of the exclusionary rule far outweigh any possible benefits to deterrence that a good-faith requirement might produce.</p>
<p id="b504-5">Williams contends that because he did not waive his right to the assistance of counsel, the Court may not balance competing values in deciding whether the challenged evidence was properly admitted. He argues that, unlike the exclusionary rule in the Fourth Amendment context, the essential purpose of which is to deter police misconduct, the Sixth Amendment exclusionary rule is designed to protect the right to a fair trial and the integrity of the factfinding process. Williams contends that, when those interests are at stake, the societal costs of excluding evidence obtained from responses presumed involuntary are irrelevant in determining whether such evidence should be excluded. We disagree.</p>
<p id="b504-6">Exclusion of physical evidence that would inevitably have been discovered adds nothing to either the integrity or fairness of a criminal trial. The Sixth Amendment right to counsel protects against unfairness by preserving the adversary process in which the reliability of proffered evidence may be tested in cross-examination. See <em>United States </em>v. <em>Ash, </em><span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/#314" aria-description="Citation for case: United States v. Ash">413 U. S. 300, 314</a></span> (1973); <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#241" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 241</a></span> (1973). Here, however, Detective Learning’s conduct did nothing to impugn the reliability of the evidence in question — the body of the child and its condition as it was found, articles of clothing found on the body, and the autopsy. No one would seriously contend that the presence of counsel in the police car when Learning appealed to Wil<page-number citation-index="1" label="447">*447</page-number>liams’ decent human instincts would have had any bearing on the reliability of the body as evidence. Suppression, in these circumstances, would do nothing whatever to promote the integrity of the trial process, but would inflict a wholly unacceptable burden on the administration of criminal justice.</p>
<p id="b505-5">Nor would suppression ensure fairness on the theory that it tends to safeguard the adversary system of justice. To assure the fairness of trial proceedings, this Court has held that assistance of counsel must be available at pretrial confrontations where “the subsequent trial [cannot] cure a[n otherwise] one-sided confrontation between prosecuting authorities and the uncounseled defendant.” <em>United States </em>v. <span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/#315" aria-description="Citation for case: United States v. Ash"><em>Ash, supra, </em>at 315</a></span>. Fairness can be assured by placing the State and the accused in the same positions they would have been in had the impermissible conduct not taken place. However, if the government can prove that the evidence would have been obtained inevitably and, therefore, would have been admitted regardless of any overreaching by the police, there is no rational basis to keep that evidence from the jury in order to ensure the fairness of the trial proceedings. In that situation, the State has gained no advantage at trial and the defendant has suffered no prejudice. Indeed, suppression of the evidence would operate to undermine the adversary system by putting the State in a <em>worse </em>position than it would have occupied without any police misconduct. Williams’ argument that inevitable discovery constitutes impermissible balancing of values is without merit.</p>
<p id="b505-6">More than a half century ago, Judge, later Justice, Cardozo made his seminal observation that under the exclusionary rule “[t]he criminal is to go free because the constable has blundered.” <em>People </em>v. <em>Defore, </em><span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#21" aria-description="Citation for case: People v. Defore">242 N. Y. 13, 21</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#587" aria-description="Citation for case: People v. Defore">150 N. E. 585, 587</a></span> (1926). Prophetically, he went on to consider “how far-reaching in its effect upon society” the exclusionary rule would be when</p>
<blockquote id="b505-7">“[t]he pettiest peace officer would have it in his power through overzeal or indiscretion to confer immunity upon <page-number citation-index="1" label="448">*448</page-number>an offender for crimes the most flagitious.” <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#23" aria-description="Citation for case: People v. Defore"><em>Id., </em>at 23</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#588" aria-description="Citation for case: People v. Defore">150 N. E., at 588</a></span>.</blockquote>
<p id="b506-5">Some day, Cardozo speculated, some court might press the exclusionary rule to the outer limits of its logic — or beyond— and suppress evidence relating to the “body of a murdered” victim because of the means by which it was found. <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#23" aria-description="Citation for case: People v. Defore"><em>Id., </em>at 23-24</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#588" aria-description="Citation for case: People v. Defore">150 N. E., at 588</a></span>. Cardozo’s prophecy was fulfilled in <em>Killough </em>v. <em>United States, </em>114 U. S. App. D. C. 305, 309, <span class="citation" data-id="9449118"><a href="/opinion/260072/james-w-killough-v-united-states/#245" aria-description="Citation for case: James W. Killough v. United States">315 F. 2d 241, 245</a></span> (1962) (en banc). But when, as here, the evidence in question would inevitably have been discovered without reference to the police error or misconduct, there is no nexus sufficient to provide a taint and the evidence is admissible.</p>
<p id="b506-6">C</p>
<p id="b506-7">The Court of Appeals did not find it necessary to consider whether the record fairly supported the finding that the volunteer search party would ultimately or inevitably have discovered the victim’s body. However, three courts independently reviewing the evidence have found that the body of the child inevitably would have been found by the searchers. Williams challenges these findings, asserting that the record contains only the <em>“post hoc </em>rationalization” that the search efforts would have proceeded two and one-half miles into Polk County where Williams had led police to the body.</p>
<p id="b506-8">When that challenge was made at the suppression hearing preceding Williams’ second trial, the prosecution offered the testimony of Agent Ruxlow of the Iowa Bureau of Criminal Investigation. Ruxlow had organized and directed some 200 volunteers who were searching for the child’s body. Tr. of Hearings on Motion to Suppress in <em>State </em>v. <em>Williams, </em>No. CR 55805, p. 34 (May 31, 1977). The searchers were instructed “to check all the roads, the ditches, any culverts .... If they came upon any abandoned farm buildings, they were instructed to go onto the property and search those abandoned farm buildings or any other places where a <page-number citation-index="1" label="449">*449</page-number>small child could be secreted.” <em>Id., </em>at 35. Ruxlow testified that he marked off highway maps of Poweshiek and Jasper Counties in grid fashion, divided the volunteers into teams of four to six persons, and assigned each team to search specific grid areas. <em>Id., </em>at 34. Ruxlow also testified that, if the search had not been suspended because of Williams’ promised cooperation, it would have continued into Polk County, using the same grid system. <em>Id., </em>at 36, 39-40. Although he had previously marked off into grids only the highway maps of Poweshiek and Jasper Counties, Ruxlow had obtained a map of Polk County, which he said he would have marked off in the same manner had it been necessary for the search to continue. <em>Id., </em>at 39.</p>
<p id="b507-5">The search had commenced at approximately 10 a. m. and moved westward through Poweshiek County into Jasper County. At approximately 3 p. m., after Williams had volunteered to cooperate with the police, Detective Learning, who was in the police car with Williams, sent word to Ruxlow and the other Special Agent directing the search to meet him at the Grinnell truck stop and the search was suspended at that time. <em>Id., </em>at 51-52. Ruxlow also stated that he was “under the impression that there was a possibility” that Williams would lead them to the child’s body at that time. Id., at 61. The search was not resumed once it was learned that Williams had led the police to the body, <em>id., </em>at 57, which was found two and one-half miles from where the search had stopped in what would have been the easternmost grid to be searched in Polk County, <em>id., </em>at 39. There was testimony that it would have taken an additional three to five hours to discover the body if the search had continued, <em>id., </em>at 41; the body was found near a culvert, one of the kinds of places the teams had been specifically directed to search.</p>
<p id="b507-6">On this record it is clear that the search parties were approaching the actual location of the body, and we are satisfied, along with three courts earlier, that the volunteer search teams would have resumed the search had Williams <page-number citation-index="1" label="450">*450</page-number>not earlier led the police to the body and the body inevitably would have been found. The evidence asserted by Williams as newly discovered, <em>i. e., </em>certain photographs of the body and deposition testimony of Agent Ruxlow made in connection with the federal habeas proceeding, does not demonstrate that the material facts were inadequately developed in the suppression hearing in state court or that Williams was denied a full, fair, and adequate opportunity to present all relevant facts at the suppression hearing.<footnotemark>6</footnotemark></p>
<p id="b508-5">The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.<footnotemark>7</footnotemark></p>
<p id="b508-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b497-8"> Iowa law provides for <em>de novo </em>appellate review of factual as well as legal determinations in cases raising constitutional challenges. See, <em>e. g., Armento </em>v. <em>Baughman, </em><span class="citation" data-id="2216952"><a href="/opinion/2216952/armento-v-baughman/#15" aria-description="Citation for case: Armento v. Baughman">290 N. W. 2d 11, 15</a></span> (Iowa 1980); <em>State </em>v. <em>Ege, </em><span class="citation" data-id="9689598"><a href="/opinion/1861096/state-v-ege/#352" aria-description="Citation for case: State v. Ege">274 N. W. 2d 350, 352</a></span> (Iowa 1979).</p>
</footnote>
<footnote label="2">
<p id="AGm"> Every Federal Court of Appeals having jurisdiction over criminal matters, including the Eighth Circuit in a case decided after the instant case, has endorsed the inevitable discovery doctrine. See <em>Wayne </em>v. <em>United States, </em>115 U. S. App. D. C. 234, 238, <span class="citation" data-id="9449370"><a href="/opinion/260805/lewis-l-wayne-v-united-states/#209" aria-description="Citation for case: Lewis L. Wayne v. United States">318 F. 2d 205, 209</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./375/860/">375 U. S. 860</a></span> (1963); <em>United States </em>v. <em>Bienvenue, </em><span class="citation" data-id="382927"><a href="/opinion/382927/united-states-v-donald-bienvenue/#914" aria-description="Citation for case: United States v. Donald Bienvenue">632 F. 2d 910, 914</a></span> (CA1 1980); <em>United States </em>v. <em>Fisher, </em><span class="citation" data-id="414450"><a href="/opinion/414450/united-states-v-howard-fisher/#784" aria-description="Citation for case: United States v. Howard Fisher">700 F. 2d 780, 784</a></span> (CA2 1983); <em>Government of Virgin Islands </em>v. <em>Gereau, </em><span class="citation" data-id="8173389"><a href="/opinion/8210936/government-of-virgin-islands-v-gereau/#927" aria-description="Citation for case: Government of Virgin Islands v. Gereau">502 F. 2d 914, 927-928</a></span> (CA3 1974), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./420/909/">420 U. S. 909</a></span> (1975); <em>United States </em>v. <em>Seohnlein, </em><span class="citation" data-id="289216"><a href="/opinion/289216/united-states-v-charles-w-seohnlein/#1053" aria-description="Citation for case: United States v. Charles W. Seohnlein">423 F. 2d 1051, 1053</a></span> (CA4), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./399/913/">399 U. S. 913</a></span> (1970); <em>United States </em>v. <em>Brookins, </em><span class="citation" data-id="9466472"><a href="/opinion/374338/united-states-v-wayne-garfield-brookins-iii/#1042" aria-description="Citation for case: United States v. Wayne Garfield Brookins, III">614 F. 2d 1037, 1042, 1044</a></span> (CA5 1980); <em>Papp </em>v. <em>Jago, </em><span class="citation" data-id="393006"><a href="/opinion/393006/timothy-papp-v-arnold-r-jago-supt/#222" aria-description="Citation for case: Timothy Papp v. Arnold R. Jago, Supt.">656 F. 2d 221, 222</a></span> (CA6 1981); <em>United States ex rel. Owens </em>v. <em>Twomey, </em><span class="citation" data-id="324383"><a href="/opinion/324383/united-states-of-america-ex-rel-jesse-owens-v-john-j-twomey-warden/#865" aria-description="Citation for case: United States of America Ex Rel. Jesse Owens v. John J....">508 F. 2d 858, 865-866</a></span> (CA7 1974); <em>United States </em>v. <em>Apker, </em><span class="citation" data-id="8916749"><a href="/opinion/8926961/united-states-v-apker/#306" aria-description="Citation for case: United States v. Apker">705 F. 2d 293, 306-307</a></span> (CA8 1983); <page-number citation-index="1" label="441">*441</page-number><em>United States </em>v. <em>Schmidt, </em><span class="citation" data-id="9464701"><a href="/opinion/354373/united-states-v-richard-a-schmidt/#1065" aria-description="Citation for case: United States v. Richard A. Schmidt">573 F. 2d 1057, 1065-1066, n. 9</a></span> (CA9), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./439/881/">439 U. S. 881</a></span> (1978); <em>United States </em>v. <em>Romero, </em><span class="citation" data-id="410451"><a href="/opinion/410451/united-states-v-carlos-richard-romero-united-states-of-america-v-joseph/#704" aria-description="Citation for case: United States v. Carlos Richard Romero, United States of...">692 F. 2d 699, 704</a></span> (CA10 1982); <em>United States </em>v. <em>Roper, </em><span class="citation" data-id="405982"><a href="/opinion/405982/united-states-v-james-morrow-roper-christian-matthew-newton-john-jackson/#1358" aria-description="Citation for case: United States v. James Morrow Roper, Christian Matthew...">681 F. 2d 1354, 1358</a></span> (CA11 1982).</p>
</footnote>
<footnote label="3">
<p id="b500-8"> In <em>Murphy </em>v. <em>Waterfront Comm’n of New York Harbor, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#79" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 79</a></span> (1964), the Court held that “a state witness may not be compelled to give testimony which may be incriminating under federal law unless the compelled testimony and its fruits cannot be used in any manner by federal officials in connection with a criminal prosecution against him.” The Court added, however, that “[o]nce a defendant demonstrates that he has testified, under a state grant of immunity, to matters related to the federal prosecution, the federal authorities have the burden of showing that their evidence is not tainted by establishing that they had an independent, legitimate source for the disputed evidence.” <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#79" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor"><em>Id., </em>at 79, n. 18</a></span>; see <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#103" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor"><em>id., </em>at 103</a></span> (White, J., concurring). Application of the independent source doctrine in the Fifth Amendment context was reaffirmed in <em>Kastigar </em>v. <em>United States, </em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#460" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 460-461</a></span> (1972).</p>
</footnote>
<footnote label="4">
<p id="b501-6"> The ultimate or inevitable discovery exception to the exclusionary rule is closely related in purpose to the harmless-error rule of <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#22" aria-description="Citation for case: Chapman v. California">386 U. S. 18, 22</a></span> (1967). The harmless-constitutional-error rule “serve[s] a very useful purpose insofar as [it] block[s] setting aside convictions for small errors or defects that have little, if any, likelihood of having changed the result of the trial.” The purpose of the inevitable discovery rule is to block setting aside convictions that would have been obtained without police misconduct.</p>
</footnote>
<footnote label="5">
<p id="b502-6"> As to the quantum of proof, we have already established some relevant guidelines. In <em>United States </em>v. <em>Matlock, </em><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/#178" aria-description="Citation for case: United States v. Matlock">415 U. S. 164, 178, n. 14</a></span> (1974) (emphasis added), we stated that “the controlling burden of proof at suppression hearings should impose <em>no greater burden </em>than proof by a preponderance of the evidence.” In <em>Lego </em>v. <em>Twomey, </em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#488" aria-description="Citation for case: Lego v. Twomey">404 U. S. 477, 488</a></span> (1972), we observed “from our experience [that] no substantial evidence has accumulated that federal rights have suffered from determining admissibility by a preponderance of the evidence” and held that the prosecution must prove by a preponderance of the evidence that a confession sought to be used at trial was voluntary. We are unwilling to impose added burdens on the already difficult task of proving guilt in criminal cases by enlarging the barrier to placing evidence of unquestioned truth before juries.</p>
<p id="b502-7">Williams argues that the preponderance-of-the-evidence standard used by the Iowa courts is inconsistent with <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967). In requiring clear and convincing evidence of an independent source for an in-court identification, the Court gave weight to the effect an uncounseled pretrial identification has in “crystallizing] the witnesses’ identification of the defendant for future reference.” <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#240" aria-description="Citation for case: United States v. Wade"><em>Id., </em>at 240</a></span>. The <page-number citation-index="1" label="445">*445</page-number>Court noted as well that possible unfairness at the lineup “may be the sole means of attack upon the unequivocal courtroom identification,” <em>ibid., </em>and recognized the difficulty of determining whether an in-court identification was based on independent recollection unaided by the lineup identification, <em>■id., </em>at 240-241. By contrast, inevitable discovery involves no speculative elements but focuses on demonstrated historical facts capable of ready verification or impeachment and does not require a departure from the usual burden of proof at suppression hearings.</p>
</footnote>
<footnote label="6">
<p id="b508-9"> Williams had presented to the District Court newly discovered evidence consisting of “previously overlooked photographs of the body at the site of its discovery and recent deposition testimony of the investigative officer in charge of the search [Ruxlow].” <span class="citation" data-id="1764351"><a href="/opinion/1764351/williams-v-nix/#671" aria-description="Citation for case: Williams v. Nix">528 F. Supp., at 671, n. 6</a></span>. He contends that Ruxlow’s testimony was no more than <em>“post hoc </em>rationalization” and challenges Ruxlow’s credibility. However, the state trial court and Federal District Court that heard Ruxlow’s testimony credited it. The District Court found that the newly discovered evidence “neither adds much to nor subtracts much from the suppression hearing evidence.” <em><span class="citation" data-id="1764351"><a href="/opinion/1764351/williams-v-nix/" aria-description="Citation for case: Williams v. Nix">Ibid.</a></span></em></p>
</footnote>
<footnote label="7">
<p id="b508-10"> In view of our holding that the challenged evidence was admissible under the inevitable discovery exception to the exclusionary rule, we find it unnecessary to decide whether <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U. S. 465</a></span> (1976), should be extended to bar federal habeas corpus review of Williams’ Sixth Amendment claim, and we express no view on that issue.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Pennsylvania Board of Probation and Parole v. Scott.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Pennsylvania Board of Probation and Parole v. Scott"
type: case
citation: "524 U.S. 357 (1998)"
parallel_cite: "118 S. Ct. 2014; 141 L. Ed. 2d 344"
neutral_cite: 1998 U.S. LEXIS 4037
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1998
date_decided: 1998-06-25
docket: 97-581
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1998-06-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Pennsylvania Board of Probation and Parole v. Scott
  varies_by_point: false
  scope_note: "The federal exclusionary rule does not apply at parole-revocation hearings; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118235/pennsylvania-bd-of-probation-and-parole-v-scott/"
  cluster_id: 118235
  opinion_id: 9433685
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Limiting"
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Calandra]]", "[[United States v. Janis]]", "[[United States v. Leon]]", "[[Griffin v. Wisconsin]]", "[[Samson v. California]]"]
aliases: ["Pennsylvania Bd. of Probation and Parole v. Scott"]
tags: ["case", "fourth-amendment", "exclusionary-rule", "parole", "revocation-hearing", "deterrence"]
holding: "The federal Fourth Amendment exclusionary rule does not bar the introduction at a parole-revocation hearing of evidence seized in violation of a parolee's Fourth Amendment rights."
lake:
  record_id: Pennsylvania Board of Probation and Parole v. Scott
  status: verified
  projected_at: 2026-07-06
---

# Pennsylvania Board of Probation and Parole v. Scott

*524 U.S. 357 (1998)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Keith Scott, a Pennsylvania parolee, was arrested for parole violations; parole officers searched his residence and found firearms, a bow, and arrows, the possession of which violated his parole. At his parole-revocation hearing, Scott objected that the search was unconstitutional and sought to exclude the evidence. The Pennsylvania Supreme Court held the exclusionary rule applied at revocation hearings and ordered the evidence suppressed.

## Issue
Whether the Fourth Amendment exclusionary rule applies to — and bars the introduction of unlawfully seized evidence at — state parole-revocation hearings.

## Rule
No; the exclusionary rule is a prudential deterrent, not a personal constitutional right. "[A] Fourth Amendment violation is 'fully accomplished' by the illegal search or seizure, and no exclusion of evidence from a judicial or administrative proceeding can 'cure the invasion of the defendant's rights which he has already suffered.'" — 524 U.S. at 363 (quoting *United States v. Leon*, 468 U.S. 897, 906). The rule therefore "applies only in contexts 'where its remedial objectives are thought most efficaciously served,'" and the Court has "repeatedly declined to extend the exclusionary rule to proceedings other than criminal trials." — *Id.* at 363.

## Application
As in the grand-jury (*[[United States v. Calandra|Calandra]]*), civil-tax (*[[United States v. Janis|Janis]]*), and civil-deportation (*[[Immigration & Naturalization Service v. Lopez-Mendoza|Lopez-Mendoza]]*) contexts, the Court declined to extend the rule. Applying it at parole-revocation hearings "would both hinder the functioning of state parole systems and alter the traditionally flexible, administrative nature of parole revocation proceedings," while adding "only minimal deterrence benefits" because the criminal-trial exclusionary rule already deters unconstitutional searches. The social costs of excluding reliable evidence — letting violators escape revocation — outweighed those marginal benefits.

## Conclusion
"We therefore hold that the federal exclusionary rule does not bar the introduction at parole revocation hearings of evidence seized in violation of parolees' Fourth Amendment rights." — 524 U.S. at 364. ^pin-364

The judgment of the Pennsylvania Supreme Court was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Scott* extends the cost-benefit limit on the exclusionary rule of [[United States v. Calandra]] and [[United States v. Janis]] (and *[[Immigration & Naturalization Service v. Lopez-Mendoza|INS v. Lopez-Mendoza]]*) to parole-revocation hearings, applying the deterrence framework of [[United States v. Leon]]. It complements the reduced-privacy supervision cases [[Griffin v. Wisconsin]] and [[Samson v. California]].

## Appears on
- [[The Exclusionary Rule]] — *Key — Limiting*
- [[Special Needs and Administrative Searches]] — *Related (cross-doctrine)*

## Sources
- *Pennsylvania Bd. of Probation and Parole v. Scott*, 524 U.S. 357 (1998) — https://www.courtlistener.com/opinion/118235/pennsylvania-bd-of-probation-and-parole-v-scott/ — pinpoints: 363, 364.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "34c035d0a0f0ad87", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Pennsylvania Board of Probation and Parole v. Scott"}, "payload": {"all": [{"cite": "524 U.S. 357", "page": "357", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "524"}, {"cite": "118 S. Ct. 2014", "page": "2014", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "118"}, {"cite": "141 L. Ed. 2d 344", "page": "344", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "141"}, {"cite": "1998 U.S. LEXIS 4037", "page": "4037", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1998"}], "display": "524 U.S. 357", "official": {"cite": "524 U.S. 357", "page": "357", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "524"}, "official_selection_present": true, "record_id": "Pennsylvania Board of Probation and Parole v. Scott"}}
{"assertion_id": "acef632e09f32ce9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-364", "record_id": "Pennsylvania Board of Probation and Parole v. Scott"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-364", "pinpoint_status": "slip-only", "quote": "because the criminal-trial exclusionary rule already deters unconstitutional searches. The social costs of excluding reliable evidence — letting violators escape revocation — outweighed those marginal benefits. ## Conclusion", "quote_fidelity": "mismatch", "record_id": "Pennsylvania Board of Probation and Parole v. Scott", "star_marker": null}}
{"assertion_id": "bb1368ac11271a0b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Pennsylvania Board of Probation and Parole v. Scott"}, "payload": {"as_of_content": "1998-06-22", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Pennsylvania Board of Probation and Parole v. Scott", "scope_note": "The federal exclusionary rule does not apply at parole-revocation hearings; good law.", "varies_by_point": false}}
```

### lake record — Pennsylvania Board of Probation and Parole v. Scott

```json
{
  "schema_version": "s2.v1",
  "record_id": "Pennsylvania Board of Probation and Parole v. Scott",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Pennsylvania Bd. of Probation and Parole v. Scott",
    "case_name_short": "Scott",
    "case_name_full": "Pennsylvania Board of Probation and Parole v. Scott",
    "input_case_name": "Pennsylvania Board of Probation and Parole v. Scott",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1998-06-25",
    "year": 1998,
    "docket": "97-581",
    "cluster_id": 118235,
    "lead_opinion_id": 9433685,
    "sibling_ids": [
      118235,
      9433685,
      9433686,
      9433687
    ],
    "absolute_url": "/opinion/118235/pennsylvania-bd-of-probation-and-parole-v-scott/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9174362,
        "score": 20,
        "case_name": "Pennsylvania Board of Probation & Parole v. Scott"
      },
      {
        "cluster_id": 118176,
        "score": 20,
        "case_name": "Spencer v. Kemna"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "524 U.S. 357",
      "volume": "524",
      "reporter": "U.S.",
      "page": "357",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "118 S. Ct. 2014",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "2014",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 L. Ed. 2d 344",
        "volume": "141",
        "reporter": "L. Ed. 2d",
        "page": "344",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1998 U.S. LEXIS 4037",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "4037",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "524 U.S. 357",
        "volume": "524",
        "reporter": "U.S.",
        "page": "357",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "118 S. Ct. 2014",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "2014",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 L. Ed. 2d 344",
        "volume": "141",
        "reporter": "L. Ed. 2d",
        "page": "344",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 U.S. LEXIS 4037",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "4037",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "524 U.S. 357",
    "official_selection": {
      "court_class": "scotus",
      "selected": "524 U.S. 357",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-364",
      "page": null,
      "quote": "because the criminal-trial exclusionary rule already deters unconstitutional searches. The social costs of excluding reliable evidence \u2014 letting violators escape revocation \u2014 outweighed those marginal benefits. ## Conclusion",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1998-06-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Pennsylvania Board of Probation and Parole v. Scott",
    "varies_by_point": false,
    "scope_note": "The federal exclusionary rule does not apply at parole-revocation hearings; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 10705828,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane1_negative"
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
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Rush",
          "cluster_id": 3164356,
          "cite": [
            "808 F.3d 1007",
            "2015 U.S. App. LEXIS 22212",
            "2015 WL 9269763"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane1_negative"
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
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Fallon v. Colorado Department of Revenue",
          "cluster_id": 2379299,
          "cite": [
            "250 P.3d 691",
            "2010 Colo. App. LEXIS 358",
            "2010 WL 961642"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Weikert",
          "cluster_id": 202888,
          "cite": [
            "504 F.3d 1",
            "2007 U.S. App. LEXIS 18845",
            "2007 WL 2265660"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dennis Russell Callaghan",
          "cluster_id": 2933574,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane1_negative"
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
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 218926,
          "cite": [
            "180 L. Ed. 2d 285",
            "131 S. Ct. 2419",
            "564 U.S. 229",
            "2011 U.S. LEXIS 4560"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Birchfield v. N. Dakota. William Robert Bernard",
          "cluster_id": 3216497,
          "cite": [
            "579 U.S. 438",
            "195 L. Ed. 2d 560",
            "2016 U.S. LEXIS 4058",
            "136 S. Ct. 2160"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
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
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Samson v. California",
          "cluster_id": 145640,
          "cite": [
            "165 L. Ed. 2d 250",
            "126 S. Ct. 2193",
            "547 U.S. 843",
            "2006 U.S. LEXIS 4885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McCullough",
          "cluster_id": 2594742,
          "cite": [
            "6 P.3d 774",
            "2000 Colo. J. C.A.R. 3950",
            "2000 Colo. LEXIS 817",
            "2000 WL 870824"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sanchez-Llamas v. Oregon",
          "cluster_id": 145628,
          "cite": [
            "165 L. Ed. 2d 557",
            "126 S. Ct. 2669",
            "548 U.S. 331",
            "2006 U.S. LEXIS 5177"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Erickson Meko Campbell",
          "cluster_id": 6357475,
          "cite": [
            "26 F.4th 860"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Caldarola v. Calabrese",
          "cluster_id": 7106428,
          "cite": [
            "298 F.3d 156",
            "2002 WL 1759778"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. Virginia",
          "cluster_id": 4501697,
          "cite": [
            "584 U.S. 586",
            "138 S. Ct. 1663",
            "201 L. Ed. 2d 9",
            "2018 U.S. LEXIS 3210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mayfield v. United States",
          "cluster_id": 594,
          "cite": [
            "599 F.3d 964",
            "2010 U.S. App. LEXIS 6015",
            "2010 WL 1052341"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Caldarola v. Calabrese",
          "cluster_id": 778515,
          "cite": [
            "298 F.3d 156",
            "2002 U.S. App. LEXIS 15339"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Reyes",
          "cluster_id": 1444172,
          "cite": [
            "968 P.2d 445",
            "80 Cal. Rptr. 2d 734",
            "19 Cal. 4th 743"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zerby v. Shanon",
          "cluster_id": 1490851,
          "cite": [
            "964 A.2d 956",
            "2009 Pa. Commw. LEXIS 22",
            "2009 WL 233053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, State of California, Intervenor v. Raphyal Crawford, AKA Aarmyl Crawford",
          "cluster_id": 786677,
          "cite": [
            "372 F.3d 1048",
            "2004 U.S. App. LEXIS 12116",
            "2004 WL 1375521"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Kazmierczak",
          "cluster_id": 1965440,
          "cite": [
            "605 N.W.2d 667",
            "461 Mich. 411",
            "2000 WL 146099"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hernandez v. State",
          "cluster_id": 1882057,
          "cite": [
            "60 S.W.3d 106",
            "2001 Tex. Crim. App. LEXIS 104",
            "2001 WL 1415274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Cameron Kincade",
          "cluster_id": 787362,
          "cite": [
            "379 F.3d 813",
            "2004 U.S. App. LEXIS 17191",
            "2004 WL 1837840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Donald Reyes, Robert Jubic",
          "cluster_id": 776901,
          "cite": [
            "283 F.3d 446",
            "2002 U.S. App. LEXIS 3646"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Motley v. Parks",
          "cluster_id": 3035469,
          "cite": [
            "432 F.3d 1072",
            "2005 WL 3556971"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Frazier",
          "cluster_id": 842682,
          "cite": [
            "733 N.W.2d 713",
            "478 Mich. 231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Anstey",
          "cluster_id": 845579,
          "cite": [
            "719 N.W.2d 579",
            "476 Mich. 436"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ernest Edgar Black Jeff Wigington",
          "cluster_id": 3171438,
          "cite": [
            "811 F.3d 1259",
            "2016 U.S. App. LEXIS 1057",
            "2016 WL 278918"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Townes v. City Of New York",
          "cluster_id": 763761,
          "cite": [
            "176 F.3d 138",
            "1999 U.S. App. LEXIS 9319"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Townes v. City of New York",
          "cluster_id": 7077429,
          "cite": [
            "176 F.3d 138",
            "1999 WL 279798"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania Board of Probation and Parole v. Scott:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118235 OR 9433685 OR 9433686 OR 9433687) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTEwMTUzNjAwMDAwJnM9Nzg5NTYwJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118235+OR+9433685+OR+9433686+OR+9433687%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(118235 OR 9433685 OR 9433686 OR 9433687)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NCZzPTE2Nzk1NyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118235+OR+9433685+OR+9433686+OR+9433687%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118235 OR 9433685 OR 9433686 OR 9433687)",
        "reviewed": 20,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 20,
        "triage_read": 1,
        "triage_snippet_classified": 19
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118235 OR 9433685 OR 9433686 OR 9433687)",
    "indexed_citing_opinions": 334,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118235,
        "count": 280,
        "count_source": "search"
      },
      {
        "opinion_id": 9433685,
        "count": 63,
        "count_source": "search"
      },
      {
        "opinion_id": 9433686,
        "count": 1,
        "count_source": "search"
      },
      {
        "opinion_id": 9433687,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 589,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/pennsylvania-board-of-probation-and-parole-v-scott.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgxODkxODgmcz05Mzg1NjA4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118235+OR+9433685+OR+9433686+OR+9433687%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118235,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 108606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 108785,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 110267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 110317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 111105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 111259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 111265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 111835,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 117905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 296403,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 412039,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 1068423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 1968474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 1969552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 1982665,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 2108285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 2110701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 2388645,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 4952023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118235,
        "cited_id": 4952935,
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
    "date_created": "2026-07-05T16:46:40Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:47:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:47:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:50:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:47:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Pennsylvania Board of Probation and Parole v. Scott

```
<opinion type="majority">
<author id="b403-6">Justice Thomas</author>
<p id="APb">delivered the opinion of the Court.</p>
<p id="b403-7">This ease presents the question whether the exclusionary-rule, which generally prohibits the introduction at criminal trial of evidence obtained in violation of a defendant’s Fourth Amendment rights, applies in parole revocation hearings. We hold that it does not.</p>
<p id="b403-8">I</p>
<p id="b403-9">Respondent Keith M. Scott pleaded <em>nolo contendere </em>to a charge of third-degree murder and was sentenced to a prison <page-number citation-index="1" label="360">*360</page-number>term of 10 to 20 years, beginning on March 31, 1983. On September 1, 1993, just months after completing the minimum sentence, respondent was released on parole. One of the conditions of respondent’s parole was that he would refrain from “owning or possessing any firearms or other weapons.” App. 5a. The parole agreement, which respondent signed, further provided:</p>
<blockquote id="b404-4">“I expressly consent to the search of my person, property and residence, without a warrant by agents of the Pennsylvania Board of Probation and Parole. Any items, in <em>[sic] </em>the possession of which constitutes a violation of parole/reparole shall be subject to seizure, and may be used as evidence in the parole revocation process.” <em>Id., </em>at 7a.</blockquote>
<p id="b404-5">About five months later, after obtaining an arrest warrant based on evidence that respondent had'violated several conditions of his parole by possessing firearms, consuming alcohol, and assaulting a co-worker, three parole officers arrested respondent at a local diner. Before being transferred to a correctional facility, respondent gave the officers the keys to his residence. The officers entered the home, which was owned by his mother, but did not perform a search for parole violations until respondent’s mother arrived. The officers neither requested nor obtained consent to perform the search, but respondent’s mother, did direct them to his bedroom. After finding no relevant evidence there, the officers searched an adjacent sitting room in which they found five firearms, a compound bow, and three arrows.</p>
<p id="b404-6">At his parole violation hearing, respondent objected to the introduction of the evidence obtained during the search of his home on the ground that the search was unreasonable under the Fourth Amendment. The hearing examiner, however, rejected the challenge and admitted the evidence. As a result, the Pennsylvania Board of Probation and Parole found sufficient evidence in the record to support the weap<page-number citation-index="1" label="361">*361</page-number>ons and alcohol charges and recommitted respondent to serve 36 months’ backtime.</p>
<p id="b405-5">The Commonwealth Court of Pennsylvania reversed and remanded, holding, <em>inter alia, </em>that the hearing examiner had erred in admitting the evidence obtained during the search of respondent’s residence.<footnotemark>1</footnotemark> The court ruled that the search violated respondent’s Fourth Amendment rights because it was conducted without the owner’s consent and was not authorized by any state statutory or regulatory framework ensuring the reasonableness of searches by parole officers. <span class="citation" data-id="4952023"><a href="/opinion/5132700/scott-v-pennsylvania-board-of-probation-parole/#596" aria-description="Citation for case: Scott v. Pennsylvania Board of Probation &amp; Parole">668 A. 2d 590, 596</a></span> (1995). The court further held that the exclusionary rule should apply because, in the circumstances of respondent’s case, the deterrence benefits of the rule outweighed its costs. <span class="citation" data-id="4952023"><a href="/opinion/5132700/scott-v-pennsylvania-board-of-probation-parole/#600" aria-description="Citation for case: Scott v. Pennsylvania Board of Probation &amp; Parole"><em>Id., </em>at 600</a></span>.<footnotemark>2</footnotemark></p>
<p id="b405-6">The Pennsylvania Supreme Court affirmed. <span class="citation multiple-matches"><a href="/c/Pa./548/418/">548 Pa. 418</a></span>, <span class="citation" data-id="1968474"><a href="/opinion/1968474/scott-v-pennsylvania-board-of-probation-parole/" aria-description="Citation for case: Scott v. Pennsylvania Board of Probation &amp; Parole">698 A. 2d 32</a></span> (1997). The court stated that respondent’s Fourth Amendment right against unreasonable searches and seizures was “unaffected” by his signing of the parole agreement giving parole officers permission to conduct warrant-less searches. <em>Id., </em>at 427, <span class="citation" data-id="1968474"><a href="/opinion/1968474/scott-v-pennsylvania-board-of-probation-parole/#36" aria-description="Citation for case: Scott v. Pennsylvania Board of Probation &amp; Parole">698 A. 2d, at 36</a></span>. It then held that the search in question was unreasonable because it was supported only by “mere speculation” rather than a “reasonable suspicion” of a parole violation. <em><span class="citation" data-id="1968474"><a href="/opinion/1968474/scott-v-pennsylvania-board-of-probation-parole/" aria-description="Citation for case: Scott v. Pennsylvania Board of Probation &amp; Parole">Ibid.</a></span> </em>Carving out an exception to its <em>per se </em>bar against application of the exclusionary rule in parole revocation hearings, see <em>Commonwealth </em>v. <em>Kates, </em><span class="citation" data-id="9764222"><a href="/opinion/2388645/commonwealth-v-kates/#120" aria-description="Citation for case: Commonwealth v. Kates">452 Pa. 102, 120</a></span>, <span class="citation" data-id="9764222"><a href="/opinion/2388645/commonwealth-v-kates/#710" aria-description="Citation for case: Commonwealth v. Kates">305 A. 2d 701, 710</a></span> (1973), the court further ruled that the federal exclusionary rule applied to this ease because the officers who conducted the <page-number citation-index="1" label="362">*362</page-number>search were aware of respondent’s parole status, <span class="citation" data-id="1968474"><a href="/opinion/1968474/scott-v-pennsylvania-board-of-probation-parole/#428" aria-description="Citation for case: Scott v. Pennsylvania Board of Probation &amp; Parole">548 Pa., at 428-432</a></span>, <span class="citation" data-id="1968474"><a href="/opinion/1968474/scott-v-pennsylvania-board-of-probation-parole/#37" aria-description="Citation for case: Scott v. Pennsylvania Board of Probation &amp; Parole">698 A. 2d, at 37-38</a></span>. The court reasoned that, in the absence of the rule, illegal searches would be undeterred when officers know that the subjects of their searches are parolees and that illegally obtained evidence can be introduced at parole hearings. <em><span class="citation" data-id="1968474"><a href="/opinion/1968474/scott-v-pennsylvania-board-of-probation-parole/" aria-description="Citation for case: Scott v. Pennsylvania Board of Probation &amp; Parole">Ibid.</a></span></em></p>
<p id="b406-6">We granted certiorari to determine whether the Fourth Amendment exclusionary rule applies to parole revocation proceedings. <span class="citation multiple-matches"><a href="/c/U.%20S./522/992/">522 U. S. 992</a></span> (1997).<footnotemark>3</footnotemark></p>
<p id="b406-7">rH <em>&gt; </em>— \</p>
<p id="b406-1">We have emphasized repeatedly that the government’s use of evidence obtained in violation of the Fourth Amendment does not itself violate the Constitution. See, <em>e. g., United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 906</a></span> (1984); <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#482" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 482, 486</a></span> (1976). Rather, a Fourth Amendment violation is “‘fully accomplished’” by the illegal search or seizure, and no exclusion of evidence from a judicial or administrative proceeding can “ ‘cure the invasion of the defendant’s rights which he has already suffered.’” <em>United States </em>v. <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon, supra,</a></span> </em>at 906 (quoting <em>Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#540" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 540</a></span> <page-number citation-index="1" label="363">*363</page-number>(White, J., dissenting)). The exclusionary rule is instead a judicially created means of deterring illegal searches and seizures. <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 348</a></span> (1974). As such, the rule does not “proscribe the introduction of illegally seized evidence in all proceedings or against all persons,” <em>Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 486</a></span>, but applies only in contexts “where its remedial objectives are thought most efficaciously served,” <em>United States </em>v. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>; see also <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#454" aria-description="Citation for case: United States v. Janis">428 U. S. 433, 454</a></span> (1976) (“If... the exclusionary rule does not result in appreciable deterrence, then, clearly, its use in the instant situation is unwarranted”). Moreover, because the rule is prudential rather than constitutionally mandated, we have held it to be applicable only where its deterrence benefits outweigh its “substantial social costs.” <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#907" aria-description="Citation for case: United States v. Leon">468 U. S., at 907</a></span>.</p>
<p id="b407-5">Recognizing these costs, we have repeatedly declined to extend the exclusionary rule to proceedings other than criminal trials. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#909" aria-description="Citation for case: United States v. Leon"><em>Id., </em>at 909</a></span>; <em>United States </em>v. <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#447" aria-description="Citation for case: United States v. Janis"><em>Janis, supra, </em>at 447</a></span>. For example, in <em>United States </em>v. <em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">Calandra</a></span>, </em>we held that the exclusionary rule does not apply to grand jury proceedings; in so doing, we emphasized that such proceedings play a special role in the law enforcement process and that the traditionally flexible, nonadversarial nature of those proceedings would be jeopardized by application of the rule. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#343" aria-description="Citation for case: United States v. Calandra">414 U. S., at 343-346, 349-350</a></span>. Likewise, in <em>United States </em>v. <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span>, </em>we held that the exclusionary rule did not bar the introduction of unconstitutionally obtained evidence in a civil tax proceeding because the costs of excluding relevant and reliable evidence would outweigh the marginal deterrence benefits, which, we noted, would be minimal because the use of the exclusionary rule in criminal trials already deterred illegal searches. 428 U. S., at 448, 454. Finally, in <em>INS </em>v. <em>Lopez-Mendoza, </em><span class="citation" data-id="9429772"><a href="/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Lopez-Mendoza">468 U. S. 1032</a></span> (1984), we refused to extend the exclusionary rule to civil deportation proceedings, citing the high social costs of allowing an immigrant to remain illegally <page-number citation-index="1" label="364">*364</page-number>in this country and noting the incompatibility of the rule with the civil, administrative nature of those proceedings. <span class="citation" data-id="9429772"><a href="/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/#1050" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Lopez-Mendoza"><em>Id., </em>at 1050</a></span>.</p>
<p id="b408-4">As in <em>Calandra, Janis, </em>and <em><span class="citation" data-id="9429772"><a href="/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Lopez-Mendoza">Lopez-Mendoza</a></span>, </em>we are asked to extend the operation of the exclusionary rule beyond the criminal trial context. We again decline to do so. Application of the exclusionary rule would both hinder the functioning of state parole systems and alter the traditionally flexible, administrative nature of parole revocation proceedings. The rule would provide only minimal deterrence benefits in this context, because application of the rule in the criminal trial context already provides significant deterrence of unconstitutional searches. We therefore hold that the federal exclusionary rule does not bar the introduction at parole revocation hearings of evidence seized in violation of parolees’ Fourth Amendment rights.</p>
<p id="b408-5">Because the exclusionary rule precludes consideration of reliable, probative evidence, it imposes significant costs: It undeniably detracts from the truthfinding process and allows many who would otherwise be incarcerated to escape the consequences of their actions. See <em>Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#490" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 490</a></span>. Although we have held these costs to be worth bearing in certain circumstances,<footnotemark>4</footnotemark> our eases have repeatedly emphasized that the rule’s “costly toll” upon truth-seeking and law enforcement objectives presents a high obstacle for those <page-number citation-index="1" label="365">*365</page-number>urging application of the rule. <em>United States </em>v. <em>Payner, </em><span class="citation" data-id="9428014"><a href="/opinion/110317/united-states-v-payner/#784" aria-description="Citation for case: United States v. Payner">447 U. S. 727, 784</a></span> (1980).</p>
<p id="b409-5">The costs of excluding reliable, probative evidence are particularly high in the context of parole revocation proceedings. Parole is a ‘Variation on imprisonment of convicted criminals,” <em>Morrissey </em>v. <em>Brewer, </em><span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#477" aria-description="Citation for case: Morrissey v. Brewer">408 U. S. 471, 477</a></span> (1972), in which the State accords a limited degree of freedom in return for the parolee’s assurance that he will comply with the often strict terms and conditions of his release. In most cases, the State is willing to extend parole only because it is able to condition it upon compliance with certain requirements. The State thus has an “overwhelming interest” in ensuring that a parolee complies with those requirements and is returned to prison if he fails to do so. <span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#483" aria-description="Citation for case: Morrissey v. Brewer"><em>Id., </em>at 483</a></span>. The exclusion of evidence establishing a parole violation, however, hampers the State’s ability to ensure compliance with these conditions by permitting the parolee to avoid the consequences of his noncompliance. The costs of allowing a parolee to avoid the consequences of his violation are compounded by the fact that parolees (particularly those who have already committed parole violations) are more likely to commit future criminal offenses than are average citizens. See <em>Griffin </em>v. <em>Wisconsin, </em><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#880" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868, 880</a></span> (1987). Indeed, this is the very premise behind the system of close parole supervision. <em><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Ibid.</a></span></em></p>
<p id="b409-6">The exclusionary rule, moreover, is incompatible with the traditionally flexible, administrative procedures of parole revocation. Because parole revocation deprives the parolee not “of the absolute liberty to which every citizen is entitled, but only of the conditional liberty properly dependent on observance of special parolé restrictions,” <em>Morrissey </em>v. <span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#480" aria-description="Citation for case: Morrissey v. Brewer"><em>Brewer, supra, </em>at 480</a></span>, States have wide latitude under the Constitution to structure parole revocation proceedings.<footnotemark>5</footnotemark> Most <page-number citation-index="1" label="366">*366</page-number>States, including Pennsylvania, see <span class="citation" data-id="1968474"><a href="/opinion/1968474/scott-v-pennsylvania-board-of-probation-parole/#427" aria-description="Citation for case: Scott v. Pennsylvania Board of Probation &amp; Parole">548 Pa., at 427-428</a></span>, <span class="citation" data-id="1968474"><a href="/opinion/1968474/scott-v-pennsylvania-board-of-probation-parole/#36" aria-description="Citation for case: Scott v. Pennsylvania Board of Probation &amp; Parole">698 A. 2d, at 36</a></span>; <em>Rivenbark </em>v. <em>Pennsylvania Bd. of Probation and Parole, </em><span class="citation" data-id="6263399"><a href="/opinion/6393108/rivenbark-v-commonwealth-pennsylvania-board-of-probation-parole/" aria-description="Citation for case: Rivenbark v. Commonwealth, Pennsylvania Board of...">509 Pa. 248</a></span>, <span class="citation" data-id="6263399"><a href="/opinion/6393108/rivenbark-v-commonwealth-pennsylvania-board-of-probation-parole/" aria-description="Citation for case: Rivenbark v. Commonwealth, Pennsylvania Board of...">501 A. 2d 1110</a></span> (1985), have adopted informal, administrative parole revocation procedures in order to accommodate the large number of parole proceedings. These proceedings generally are not conducted by judges, but instead by parole boards, “members of which need not be judicial officers or lawyers.” <em>Morrissey </em>v. <em>Brewer, </em><span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#489" aria-description="Citation for case: Morrissey v. Brewer">408 U. S., at 489</a></span>. And traditional rules of evidence generally do not apply. <em><span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/" aria-description="Citation for case: Morrissey v. Brewer">Ibid.</a></span> </em>(“[T]he process should be flexible enough to consider evidence including letters, affidavits, and other material that would not be admissible in an adversary criminal trial”). Nor are these proceedings entirely adversarial, as they are designed to be “'predictive and discretionary5 as well as factfinding.” <em>Gagnon </em>v. <em>Scarpelli, </em><span class="citation" data-id="9425285"><a href="/opinion/108785/gagnon-v-scarpelli/#787" aria-description="Citation for case: Gagnon v. Scarpelli">411 U. S. 778, 787</a></span> (1973) (quoting <em>Morrissey </em>v. <span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#480" aria-description="Citation for case: Morrissey v. Brewer"><em>Brewer, supra, </em>at 480</a></span>).</p>
<p id="b410-4">Application of the exclusionary rule would significantly alter this process. The exclusionary rule frequently requires extensive litigation to determine whether particular evidence must be excluded. Cf. <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#349" aria-description="Citation for case: United States v. Calandra">414 U. S., at 349</a></span> (noting that application of the exclusionary rule “would delay and disrupt grand jury proceedings” because “[suppression hearings would halt the orderly process of an investigation and might necessitate extended litigation of issues only tangentially related to the grand jury’s primary objective”); <em>INS </em>v. <em>Lopez-Mendoza, </em><span class="citation" data-id="9429772"><a href="/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/#1048" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Lopez-Mendoza">468 U. S., at 1048</a></span> (noting that “[t]he prospect of even occasional invocation of the exclusionary rule might significantly change and complicate the character of” the deportation system). Such litigation is inconsistent with the nonadversarial, administrative processes established by the States. Although States could adapt their parole revocation proceedings to accommodate <page-number citation-index="1" label="367">*367</page-number>such litigation, such a change would transform those proceedings from a “predictive and discretionary” effort to promote the best interests of both parolees and society into trial-like proceedings “less attuned” to the interests of the parolee. <em>Gagnon </em>v. <em><span class="citation" data-id="9425285"><a href="/opinion/108785/gagnon-v-scarpelli/" aria-description="Citation for case: Gagnon v. Scarpelli">Scarpelli, supra,</a></span> </em>at 787-788 (quoting <em>Morrissey </em>v. <span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#480" aria-description="Citation for case: Morrissey v. Brewer"><em>Brewer, supra, </em>at 480</a></span>). We are simply unwilling so to intrude into the States’ correctional schemes. See <em>Morrissey </em>v. <span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#483" aria-description="Citation for case: Morrissey v. Brewer"><em>Brewer, supra, </em>at 483</a></span> (recognizing that States have an “overwhelming interest” in maintaining informal, administrative parole revocation procedures). Such a transformation ultimately might disadvantage parolees because in an adversarial proceeding, “the hearing body may be less tolerant of marginal deviant behavior and feel more pressure to reincarcerate than to continue nonpunitive rehabilitation.” <em>Gagnon </em>v. <span class="citation" data-id="9425285"><a href="/opinion/108785/gagnon-v-scarpelli/#788" aria-description="Citation for case: Gagnon v. Scarpelli"><em>Scarpelli, supra, </em>at 788</a></span>. And the financial costs of such a system could reduce the State’s incentive to extend parole in the first place, as one of the purposes of parole is to reduce the costs of criminal punishment while maintaining a degree of supervision over the parolee.</p>
<p id="b411-5">The deterrence benefits of the exclusionary rule would not outweigh these costs. As the Supreme Court of Pennsylvania recognized, application of the exclusionary rule to parole revocation proceedings would have little deterrent effect upon an officer who is unaware that the subject of his search is a parolee. <span class="citation" data-id="1968474"><a href="/opinion/1968474/scott-v-pennsylvania-board-of-probation-parole/#431" aria-description="Citation for case: Scott v. Pennsylvania Board of Probation &amp; Parole">548 Pa., at 431</a></span>, <span class="citation" data-id="1968474"><a href="/opinion/1968474/scott-v-pennsylvania-board-of-probation-parole/#38" aria-description="Citation for case: Scott v. Pennsylvania Board of Probation &amp; Parole">698 A. 2d, at 38</a></span>. In that situation, the officer will likely be searching for evidence of criminal conduct with an eye toward the introduction of the evidence at a criminal trial. The likelihood that illegally obtained evidence will be excluded from trial provides deterrence against Fourth Amendment violations, and the remote possibility that the subject is a parolee and that the evidence may be admitted at a parole revocation proceeding surely has little, if any, effect on the officer’s incentives. Cf. <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#448" aria-description="Citation for case: United States v. Janis">428 U. S., at 448</a></span>.</p>
<p id="b411-6">The Pennsylvania Supreme Court thus fashioned a special rule for those situations in which the officer performing the <page-number citation-index="1" label="368">*368</page-number>search knows that the subject of his search is a parolee. We decline to adopt such an approach. We have never suggested that the exclusionary rule must apply in every circumstance in which it might provide marginal deterrence. <em>United States </em>v. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#350" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 350</a></span>; <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 174</a></span> (1969). Furthermore, such a piecemeal approach to the exclusionary rule would add an additional layer of collateral litigation regarding the officer’s knowledge of the parolee’s status.</p>
<p id="b412-4">In any event, any additional deterrence from the Pennsylvania Supreme Court’s rule would be minimal. Where the person conducting the search is a police officer, the officer’s focus is not upon ensuring compliance with parole conditions or obtaining evidence for introduction at administrative proceedings, but upon obtaining convictions of those who commit crimes. The noncriminal parole proceeding “falls outside the offending officer’s zone of primary interest.” <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#458" aria-description="Citation for case: United States v. Janis"><em>Janis, supra, </em>at 458</a></span>. Thus, even when the officer knows that the subject of his search is a parolee, the officer will be deterred from violating Fourth Amendment rights by the application of the exclusionary rule to criminal trials.</p>
<p id="b412-5">Even when the officer performing the search is a parole officer, the deterrence benefits of the exclusionary rule remain limited. Parole agents, in contrast to police officers, are not “engaged in the often competitive enterprise of ferreting out crime,” <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#914" aria-description="Citation for case: United States v. Leon">468 U. S., at 914</a></span>; instead, their primary concern is whether their parolees should remain free on parole. Thus, their relationship with parolees is more supervisory than adversarial. <em>Griffin </em>v. <em>Wisconsin, </em><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#879" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868, 879</a></span> (1987). It is thus “unfair to assume that the parole officer bears hostility against the parolee that destroys his neutrality; realistically the failure of the parolee is in a sense a failure for his supervising officer.” <em>Morrissey </em>v. <span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#485" aria-description="Citation for case: Morrissey v. Brewer"><em>Brewer, supra, </em>at 485-486</a></span>. Although this relationship does not prevent parole officers from <em>ever </em>violating the Fourth Amendment rights of their parolees, it does mean <page-number citation-index="1" label="369">*369</page-number>that the harsh deterrent of exclusion is unwarranted, given such other deterrents as departmental training and discipline and the threat of damages actions. Moreover, although in some instances parole officers may act like police officers and seek to uncover evidence of illegal activity, they (like police officers) are undoubtedly aware that any unconstitutionally seized evidence that could lead to an indictment could be suppressed in a criminal trial. In this case, assuming that the search violated respondent’s Fourth Amendment rights, the evidence could have been inadmissible at trial if respondent had been criminally prosecuted.</p>
<p id="b413-5">* <em>*</em></p>
<p id="b413-6">We have long been averse to imposing federal requirements upon the parole systems of the States. A federal requirement that parole boards apply the exclusionary rule, which is itself a “ ‘grudgingly taken, medicament,’ ” <em>United States </em>v. <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#455" aria-description="Citation for case: United States v. Janis"><em>Janis, supra, </em>at 455, n. 29</a></span>, would severely disrupt the traditionally informal, administrative process of parole revocation. The marginal deterrence of unreasonable searches and seizures is insufficient to justify such an intrusion. We therefore hold that parole boards are not required by federal law to exclude evidence obtained in violation of the Fourth Amendment. Accordingly, the judgment below is reversed, and the case is remanded to the Pennsylvania Supreme Court.</p>
<p id="b413-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b405-7"> The court also held that the Board of Probation and Parole erred by admitting hearsay evidence regarding alcohol consumption and a separate incident of weapons possession.</p>
</footnote>
<footnote label="2">
<p id="b405-8"> While this case was pending in the Pennsylvania Supreme Court, the Commonwealth Court filed an en banc opinion in another case that overruled its decision in respondent’s case and held that the exclusionary rule does not apply in parole revocation hearings. <em>Kyte </em>v. <em>Pennsylvania Bd. of Probation and Parole, </em><span class="citation" data-id="4952935"><a href="/opinion/5133529/kyte-v-pennsylvania-board-of-probation-parole/#18" aria-description="Citation for case: Kyte v. Pennsylvania Board of Probation &amp; Parole">680 A. 2d 14, 18, n. 8</a></span> (1996).</p>
</footnote>
<footnote label="3">
<p id="b406-2"> We also invited the parties to brief the question whether a search of a parolee’s residence must be based on reasonable suspicion where the parolee has consented to searches as a condition of parole. Respondent argues that we lack jurisdiction to decide this question in this case because the Pennsylvania Supreme Court held, as a matter of Pennsylvania law, that respondent’s consent to warrantless searches as a condition of his state parole did not constitute consent to searches that are unreasonable under the Fourth Amendment. Petitioner and its <em>amid </em>contend that the Pennsylvania Supreme Court’s opinion was at least ambiguous as to whether it relied on state or federal law to determine the extent of respondent’s consent, and that we therefore have jurisdiction under <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983). We need not parse the Pennsylvania Supreme Court’s decision in an attempt to discern its intent, however, because it is clear that we have jurisdiction to determine whether the exclusionary rule applies to state parole revocation proceedings, and our decision on that issue is sufficient to decide the case. We therefore express no opinion regarding the constitutionality of the search.</p>
</footnote>
<footnote label="4">
<p id="b408-6"> As discussed above, we have generally held the exclusionary rule to apply only in criminal trials. We have, moreover, significantly limited its application even in that context. For example, we have held that the rule does not apply when the officer reasonably relied on a search warrant that was later deemed invalid, <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#920" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 920-922</a></span> (1984); when the officer reasonably relied on a statute later deemed unconstitutional, <em>Illinois </em>v. <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#349" aria-description="Citation for case: Illinois v. Krull">480 U. S. 340, 349-350</a></span> (1987); when the defendant seeks to assert another person’s Fourth Amendment rights, <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 174-175</a></span> (1969); and when the illegally obtained evidence is used to impeach a defendant’s testimony, <em>United States </em>v. <em>Havens, </em><span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#627" aria-description="Citation for case: United States v. Havens">446 U. S. 620, 627-628</a></span> (1980); <em>Walder </em>v. <em>United States, </em><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/#65" aria-description="Citation for case: Walder v. United States">347 U. S. 62, 65</a></span> (1954).</p>
</footnote>
<footnote label="5">
<p id="b409-7"> We thus have held that a parolee is not entitled to “the full panoply” of due process rights to which a criminal defendant is entitled, <em>Morrissey </em>v. <em>Brewer, </em><span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#480" aria-description="Citation for case: Morrissey v. Brewer">408 U. S. 471, 480</a></span> (1972), and that the right to counsel generally <page-number citation-index="1" label="366">*366</page-number>does not attach to such proceedings because the introduction of counsel would “alter significantly the nature of the proceeding,” <em>Gagnon </em>v. <em>Scarpelli, </em><span class="citation" data-id="9425285"><a href="/opinion/108785/gagnon-v-scarpelli/#787" aria-description="Citation for case: Gagnon v. Scarpelli">411 U. S. 778, 787</a></span> (1973).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Samson v. California.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Samson v. California"
type: case
citation: "547 U.S. 843 (2006)"
parallel_cite: "126 S. Ct. 2193; 165 L. Ed. 2d 250"
neutral_cite: 2006 U.S. LEXIS 4885
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2006
date_decided: 2006-06-19
docket: 04-9728
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2006-06-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Samson v. California
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145640/samson-v-california/"
  cluster_id: 145640
  opinion_id: 145640
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Knights]]", "[[Griffin v. Wisconsin]]", "[[Board of Education v. Earls]]"]
aliases: []
tags: ["case", "fourth-amendment", "parolee", "suspicionless-search", "diminished-privacy", "special-needs"]
holding: "A suspicionless search of a parolee is reasonable; a parolee subject to a search condition has severely diminished privacy expectations,…"
lake:
  record_id: Samson v. California
  status: verified
  projected_at: 2026-07-09
---

# Samson v. California

*547 U.S. 843 (2006)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
California law required every parolee to agree in writing to be subject to search by a parole or other peace officer "at any time of the day or night, with or without a search warrant and with or without cause." A police officer who knew Samson was a parolee stopped and searched him on a city street without any particularized suspicion and found methamphetamine. Samson moved to suppress.

## Issue
Whether a suspicionless search of a parolee, conducted pursuant to a state parole search condition, violates the Fourth Amendment.

## Rule
No. Parolees have sharply reduced privacy expectations: "The extent and reach of these conditions clearly demonstrate that parolees like petitioner have severely diminished expectations of privacy by virtue of their status alone." — 547 U.S. at 852. ^pin-852

Weighed against the State's substantial interests in supervising parolees and reducing recidivism, "we conclude that the Fourth Amendment does not prohibit a police officer from conducting a suspicionless search of a parolee." — [547 U.S. at 857](https://www.courtlistener.com/opinion/145640/samson-v-california/#:~:text=we%20conclude%20that%20the%20Fourth). ^pin-857

## Application
Samson was a California parolee subject to the State's clearly expressed, signed suspicionless-search condition, giving him severely diminished privacy expectations; the State's strong interests in closely supervising parolees (who reoffend at high rates) and reintegrating them justified the search. Because the search was not arbitrary, capricious, or harassing — conduct California law independently forbids — the suspicionless street search of Samson was reasonable.

## Conclusion
The suspicionless search of a parolee subject to a search condition is reasonable; the California Court of Appeal's judgment was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Samson* extends the diminished-privacy reasoning of [[United States v. Knights]] from probationers (searched on reasonable suspicion) to parolees (searched suspicionlessly).

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *Samson v. California*, 547 U.S. 843 (2006) — https://www.courtlistener.com/opinion/145640/samson-v-california/ — pinpoints: 852, 857.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3b3fc4fac6346011", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Samson v. California"}, "payload": {"all": [{"cite": "547 U.S. 843", "page": "843", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "547"}, {"cite": "126 S. Ct. 2193", "page": "2193", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "126"}, {"cite": "165 L. Ed. 2d 250", "page": "250", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "165"}, {"cite": "2006 U.S. LEXIS 4885", "page": "4885", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2006"}], "display": "547 U.S. 843", "official": {"cite": "547 U.S. 843", "page": "843", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "547"}, "official_selection_present": true, "record_id": "Samson v. California"}}
{"assertion_id": "1a44672c5965a13e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-857", "record_id": "Samson v. California"}, "payload": {"fragment": "#:~:text=we%20conclude%20that%20the%20Fourth", "page": null, "pin_id": "pin-857", "pinpoint_status": "slip-only", "quote": "we conclude that the Fourth Amendment does not prohibit a police officer from conducting a suspicionless search of a parolee.", "quote_fidelity": "matched", "record_id": "Samson v. California", "star_marker": null}}
{"assertion_id": "5fcffdb51e2b4925", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-852", "record_id": "Samson v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-852", "pinpoint_status": "slip-only", "quote": "A police officer who knew Samson was a parolee stopped and searched him on a city street without any particularized suspicion and found methamphetamine. Samson moved to suppress. ## Issue Whether a suspicionless search of a parolee, conducted pursuant to a state parole search condition, violates the Fourth Amendment. ## Rule No. Parolees have sharply reduced privacy expectations:", "quote_fidelity": "mismatch", "record_id": "Samson v. California", "star_marker": null}}
{"assertion_id": "5b5becc88d4f0c29", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Samson v. California"}, "payload": {"as_of_content": "2006-06-19", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Samson v. California", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Samson v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Samson v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Samson v. California",
    "case_name_short": "Samson",
    "case_name_full": "Samson v. California",
    "input_case_name": "Samson v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2006-06-19",
    "year": 2006,
    "docket": "04-9728",
    "cluster_id": 145640,
    "lead_opinion_id": 145640,
    "sibling_ids": [
      145640,
      9434919,
      9434920
    ],
    "absolute_url": "/opinion/145640/samson-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "547 U.S. 843",
      "volume": "547",
      "reporter": "U.S.",
      "page": "843",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "126 S. Ct. 2193",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "2193",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "165 L. Ed. 2d 250",
        "volume": "165",
        "reporter": "L. Ed. 2d",
        "page": "250",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2006 U.S. LEXIS 4885",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "4885",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "547 U.S. 843",
        "volume": "547",
        "reporter": "U.S.",
        "page": "843",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "126 S. Ct. 2193",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "2193",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "165 L. Ed. 2d 250",
        "volume": "165",
        "reporter": "L. Ed. 2d",
        "page": "250",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2006 U.S. LEXIS 4885",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "4885",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "547 U.S. 843",
    "official_selection": {
      "court_class": "scotus",
      "selected": "547 U.S. 843",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-852",
      "page": null,
      "quote": "A police officer who knew Samson was a parolee stopped and searched him on a city street without any particularized suspicion and found methamphetamine. Samson moved to suppress. ## Issue Whether a suspicionless search of a parolee, conducted pursuant to a state parole search condition, violates the Fourth Amendment. ## Rule No. Parolees have sharply reduced privacy expectations:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-857",
      "page": null,
      "quote": "we conclude that the Fourth Amendment does not prohibit a police officer from conducting a suspicionless search of a parolee.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 30946,
      "fragment": "#:~:text=we%20conclude%20that%20the%20Fourth",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2006-06-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Samson v. California",
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
        "journal_ref": "Samson v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hilton",
          "cluster_id": 10018723,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hilton",
          "cluster_id": 5144554,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane1_negative"
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
        "journal_ref": "Samson v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Stenhoff",
          "cluster_id": 4609284,
          "cite": [
            "2019 ND 106",
            "925 N.W.2d 429"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4603999,
          "cite": [
            "119 N.E.3d 669",
            "481 Mass. 710"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Blue",
          "cluster_id": 3185413,
          "cite": [
            "783 S.E.2d 524",
            "246 N.C. App. 259",
            "2016 N.C. App. LEXIS 293"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Morris",
          "cluster_id": 3185407,
          "cite": [
            "783 S.E.2d 528",
            "246 N.C. App. 349",
            "2016 N.C. App. LEXIS 291"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Moore",
          "cluster_id": 3168462,
          "cite": [
            "473 Mass. 481",
            "43 N.E.3d 294"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Edward Sullivan",
          "cluster_id": 2821420,
          "cite": [
            "797 F.3d 623",
            "2015 U.S. App. LEXIS 13702",
            "2015 WL 4547498"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Indiana v. Brishen R. Vanderkolk",
          "cluster_id": 2806588,
          "cite": [
            "32 N.E.3d 775",
            "2015 Ind. LEXIS 507",
            "2015 WL 3608834"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane1_negative"
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
        "journal_ref": "Samson v. California:lane2_top_cited"
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
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Segundo v. State",
          "cluster_id": 1590541,
          "cite": [
            "270 S.W.3d 79",
            "2008 Tex. Crim. App. LEXIS 1505",
            "2008 WL 4724093"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bull v. City and County of San Francisco",
          "cluster_id": 1313115,
          "cite": [
            "595 F.3d 964",
            "2010 WL 431790"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Delores Henry v. Melody Hulett",
          "cluster_id": 4774392,
          "cite": [
            "969 F.3d 769"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Villarreal, David",
          "cluster_id": 2948963,
          "cite": [
            "475 S.W.3d 784",
            "2014 Tex. Crim. App. LEXIS 1898",
            "2014 WL 6734178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jacoby, T., Aplt.",
          "cluster_id": 4429713,
          "cite": [
            "170 A.3d 1065"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Douglas McClish v. Richard B. Nugent",
          "cluster_id": 77659,
          "cite": [
            "483 F.3d 1231",
            "2007 U.S. App. LEXIS 8294",
            "2007 WL 1063337"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Merritt Sharp, III v. County of Orange",
          "cluster_id": 4427211,
          "cite": [
            "871 F.3d 901",
            "2017 WL 4126947",
            "2017 U.S. App. LEXIS 18148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Grady v. North Carolina",
          "cluster_id": 2789928,
          "cite": [
            "575 U.S. 306",
            "135 S. Ct. 1368",
            "191 L. Ed. 2d 459",
            "2015 U.S. LEXIS 2124",
            "83 U.S.L.W. 4226",
            "25 Fla. L. Weekly Fed. S 181"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Samuels",
          "cluster_id": 2601800,
          "cite": [
            "228 P.3d 229",
            "2009 Colo. App. LEXIS 1789",
            "2009 WL 3297504"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warshak v. United States",
          "cluster_id": 1425282,
          "cite": [
            "532 F.3d 521",
            "2008 U.S. App. LEXIS 14717",
            "2008 WL 2698177"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vilar",
          "cluster_id": 1039434,
          "cite": [
            "729 F.3d 62",
            "92 A.L.R. Fed. 2d 661",
            "2013 WL 4608948",
            "2013 U.S. App. LEXIS 18143"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. James Maximiliano Ochoa",
          "cluster_id": 4472474,
          "cite": [
            "792 N.W.2d 260",
            "2010 Iowa Sup. LEXIS 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lewis",
          "cluster_id": 626016,
          "cite": [
            "674 F.3d 1298",
            "2012 WL 967969"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Justin Dean Short",
          "cluster_id": 2687558,
          "cite": [
            "851 N.W.2d 474",
            "2014 WL 3537029",
            "2014 Iowa Sup. LEXIS 86"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Nuckles",
          "cluster_id": 858615,
          "cite": [
            "56 Cal. 4th 601",
            "298 P.3d 867",
            "155 Cal. Rptr. 3d 374",
            "2013 WL 1707968",
            "2013 Cal. LEXIS 3329"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Scottize Danyelle Brown",
          "cluster_id": 4635121,
          "cite": [
            "930 N.W.2d 840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Christine Ann Kern",
          "cluster_id": 4472227,
          "cite": [
            "831 N.W.2d 149",
            "2013 WL 2278018",
            "2013 Iowa Sup. LEXIS 61"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCain v. Com.",
          "cluster_id": 1058509,
          "cite": [
            "659 S.E.2d 512",
            "275 Va. 546",
            "2008 Va. LEXIS 55"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Jesse Michael Gaskins",
          "cluster_id": 2812905,
          "cite": [
            "866 N.W.2d 1",
            "2015 Iowa Sup. LEXIS 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jaime P.",
          "cluster_id": 2588357,
          "cite": [
            "146 P.3d 965",
            "51 Cal. Rptr. 3d 430",
            "40 Cal. 4th 128",
            "2006 Daily Journal DAR 15618",
            "2006 Cal. Daily Op. Serv. 10933",
            "2006 Cal. LEXIS 14082",
            "2006 WL 3437058"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Earl Davis",
          "cluster_id": 2968788,
          "cite": [
            "690 F.3d 226",
            "2012 WL 3518479",
            "2012 U.S. App. LEXIS 17217"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ward",
          "cluster_id": 2010509,
          "cite": [
            "862 N.E.2d 1102",
            "308 Ill. Dec. 899",
            "371 Ill. App. 3d 382",
            "2007 Ill. App. LEXIS 75"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Weaver",
          "cluster_id": 5639938,
          "cite": [
            "12 N.Y.3d 433",
            "909 N.E.2d 1195"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145640 OR 9434919 OR 9434920) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDI4NjI0MDAwMDAwJnM9Mjc5Mjg3NCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145640+OR+9434919+OR+9434920%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(145640 OR 9434919 OR 9434920)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04OSZzPTE2MzE5NDYmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145640+OR+9434919+OR+9434920%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145640 OR 9434919 OR 9434920)",
        "reviewed": 40,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 40,
        "triage_read": 1,
        "triage_snippet_classified": 39
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145640 OR 9434919 OR 9434920)",
    "indexed_citing_opinions": 593,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145640,
        "count": 505,
        "count_source": "search"
      },
      {
        "opinion_id": 9434919,
        "count": 99,
        "count_source": "search"
      },
      {
        "opinion_id": 9434920,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 985,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/samson-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5ODkyODImcz0xMDEyMDUzOCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145640+OR+9434919+OR+9434920%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145640,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 102473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 108606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 108785,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 111252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 111904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 112220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 118100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 118235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 118391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 118414,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 118468,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 127897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 541733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 776901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 786677,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 791251,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 1112011,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 1212086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 1444172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 2281190,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 2545822,
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
    "date_created": "2026-07-05T18:34:52Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T18:35:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T18:35:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T18:38:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T18:35:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Samson v. California

```
(Slip Opinion)              OCTOBER TERM, 2005                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                       SAMSON v. CALIFORNIA

    CERTIORARI TO THE COURT OF APPEAL OF CALIFORNIA,

                FIRST APPELLATE DISTRICT


   No. 04–9728.       Argued February 22, 2006—Decided June 19, 2006
Pursuant to a California statute—which requires every prisoner eligi
  ble for release on state parole to “agree in writing to be subject to
  search or seizure by a parole officer or other peace officer . . . , with or
  without a search warrant and with or without cause”—and based
  solely on petitioner’s parolee status, an officer searched petitioner
  and found methamphetamine. The trial court denied his motions to
  suppress that evidence, and he was convicted of possession. Affirm
  ing, the State Court of Appeal held that suspicionless searches of pa
  rolees are lawful under California law and that the search in this
  case was reasonable under the Fourth Amendment because it was
  not arbitrary, capricious, or harassing.
Held: The Fourth Amendment does not prohibit a police officer from
 conducting a suspicionless search of a parolee. Pp. 3–12.
    (a) The “totality of the circumstances” must be examined to deter
 mine whether a search is reasonable under the Fourth Amendment.
 United States v. Knights, 534 U. S. 112, 118. Reasonableness “is de
 termined by assessing, on the one hand, the degree to which [the
 search] intrudes upon an individual’s privacy and, on the other, the
 degree to which it is needed for the promotion of legitimate govern
 mental interests.” Id., at 118–119. Applying this approach in
 Knights, the Court found reasonable the warrantless search of a pro
 bationer’s apartment based on reasonable suspicion and a probation
 condition authorized by California law. In evaluating the degree of
 intrusion into Knights’ privacy, the Court found his probationary
 status “salient,” id., at 118, observing that probation is on a contin
 uum of possible punishments and that probationers “do not enjoy ‘the
 absolute liberty’ ” of other citizens, id., at 119. It also found probation
 searches necessary to promote legitimate governmental interests of
2                       SAMSON v. CALIFORNIA

                                  Syllabus

    integrating probationers back into the community, combating recidi
    vism, and protecting potential victims. Balancing those interests, the
    intrusion was reasonable. However, because the search was predi
    cated on both the probation search condition and reasonable suspi
    cion, the Court did not address the reasonableness of a search solely
    predicated upon the probation condition. Pp. 3–5.
       (b) Parolees, who are on the “continuum” of state-imposed punish
    ments, have fewer expectations of privacy than probationers, because
    parole is more akin to imprisonment than probation is. “The essence
    of parole is release from prison, before the completion of sentence, on
    the condition that the prisoner abides by certain rules during the
    balance of the sentence.” Morrissey v. Brewer, 408 U. S. 471, 477.
    California’s system is consistent with these observations. An inmate
    electing to complete his sentence out of physical custody remains in
    the Department of Corrections’ legal custody for the remainder of his
    term and must comply with the terms and conditions of his parole.
    The extent and reach of those conditions demonstrate that parolees
    have severely diminished privacy expectations by virtue of their
    status alone. Additionally, as in Knights, the state law’s parole
    search condition was clearly expressed to petitioner, who signed an
    order submitting to the condition and thus was unambiguously aware
    of it. Examining the totality of the circumstances, petitioner did not
    have an expectation of privacy that society would recognize as legiti
    mate. The State’s interests, by contrast, are substantial. A State has
    an “overwhelming interest” in supervising parolees because they “are
    more likely to commit future criminal offenses.” Pennsylvania Bd. of
    Probation and Parole v. Scott, 524 U. S. 357, 365. Similarly, a State’s
    interests in reducing recidivism, thereby promoting reintegration and
    positive citizenship among probationers and parolees, warrant pri
    vacy intrusions that would not otherwise be tolerated under the
    Fourth Amendment. The Amendment does not render States power
    less to address these concerns effectively. California’s 60-to70
    percent recidivism rate demonstrates that most parolees are ill pre
    pared to handle the pressures of reintegration and require intense
    supervision. The State Legislature has concluded that, given the
    State’s number of parolees and its high recidivism rate, an individu
    alized suspicion requirement would undermine the State’s ability to
    effectively supervise parolees and protect the public from criminal
    acts by reoffenders. Contrary to petitioner’s argument, the fact that
    some States and the Federal Government require a level of individu
    alized suspicion before searching a parolee is of little relevance in de
    termining whether California’s system is drawn to meet the State’s
    needs and is reasonable, taking into account a parolee’s substantially
    diminished expectation of privacy. Nor is there merit to the argu
                     Cite as: 547 U. S. ___ (2006)                    3

                               Syllabus

  ment that California’s law grants discretion without procedural safe
  guards. The concern that the system gives officers unbridled discre
  tion to conduct searches, thereby inflicting dignitary harms that
  arouse strong resentment in parolees and undermine their ability to
  reintegrate into society, is belied by the State’s prohibition on arbi
  trary, capricious, or harassing searches. And petitioner’s concern
  that the law frustrates reintegration efforts by permitting intrusions
  into the privacy interests of third persons is unavailing because that
  concern would arise under a suspicion-based system as well. Pp. 5–
  12.
Affirmed.

   THOMAS, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and SCALIA, KENNEDY, GINSBURG, and ALITO, JJ., joined. STE
VENS, J., filed a dissenting opinion, in which SOUTER and BREYER, JJ.,
joined.
                        Cite as: 547 U. S. ____ (2006)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 04–9728
                                   _________________


      DONALD CURTIS SAMSON, PETITIONER v.

                 CALIFORNIA 

   ON WRIT OF CERTIORARI TO THE COURT OF APPEAL OF

        CALIFORNIA, FIRST APPELLATE DISTRICT

                                 [June 19, 2006]

  JUSTICE THOMAS delivered the opinion of the Court.
  California law provides that every prisoner eligible for
release on state parole “shall agree in writing to be subject
to search or seizure by a parole officer or other peace
officer at any time of the day or night, with or without a
search warrant and with or without cause.” Cal. Penal
Code Ann. §3067(a) (West 2000). We granted certiorari to
decide whether a suspicionless search, conducted under
the authority of this statute, violates the Constitution. We
hold that it does not.
                             I
   In September 2002, petitioner Donald Curtis Samson
was on state parole in California, following a conviction for
being a felon in possession of a firearm. On September 6,
2002, Officer Alex Rohleder of the San Bruno Police De
partment observed petitioner walking down a street with
a woman and a child. Based on a prior contact with peti
tioner, Officer Rohleder was aware that petitioner was on
parole and believed that he was facing an at large war
rant. Accordingly, Officer Rohleder stopped petitioner and
asked him whether he had an outstanding parole warrant.
2                  SAMSON v. CALIFORNIA

                      Opinion of the Court

Petitioner responded that there was no outstanding war
rant and that he “was in good standing with his parole
agent.” Brief for Petitioner 4. Officer Rohleder confirmed,
by radio dispatch, that petitioner was on parole and that
he did not have an outstanding warrant. Nevertheless,
pursuant to Cal. Penal Code Ann. §3067(a) (West 2000)
and based solely on petitioner’s status as a parolee, Officer
Rohleder searched petitioner. During the search, Officer
Rohleder found a cigarette box in petitioner’s left breast
pocket. Inside the box he found a plastic baggie contain
ing methamphetamine.
   The State charged petitioner with possession of
methamphetamine pursuant to Cal. Health & Safety Code
Ann. §11377(a) (West 1991). The trial court denied peti
tioner’s motion to suppress the methamphetamine evi
dence, finding that Cal. Penal Code Ann. §3067(a) (West
2000) authorized the search and that the search was not
“arbitrary or capricious.” App. 62–63 (Proceedings on
Motion to Supress). A jury convicted petitioner of the
possession charge and the trial court sentenced him to
seven years’ imprisonment.
   The California Court of Appeal affirmed. Relying on
People v. Reyes, 19 Cal. 4th 743, 968 P. 2d 445 (1998), the
court held that suspicionless searches of parolees are
lawful under California law; that “ ‘[s]uch a search is
reasonable within the meaning of the Fourth Amendment
as long as it is not arbitrary, capricious or harassing’ ”; and
that the search in this case was not arbitrary, capricious,
or harassing. No. A102394 (Ct. App. Cal., 1st App. Dist.,
Oct. 14, 2004), App. 12–14.
   We granted certiorari, 545 U. S. ___ (2005), to answer a
variation of the question this Court left open in United
States v. Knights, 534 U. S. 112, 120, n. 6 (2001)—whether
a condition of release can so diminish or eliminate a re
leased prisoner’s reasonable expectation of privacy that a
suspicionless search by a law enforcement officer would
                      Cite as: 547 U. S. ____ (2006)                      3

                           Opinion of the Court

not offend the Fourth Amendment.1 Answering that
question in the affirmative today, we affirm the judgment
of the California Court of Appeal.
                              II
  “[U]nder our general Fourth Amendment approach” we
“examin[e] the totality of the circumstances” to determine
whether a search is reasonable within the meaning of the
Fourth Amendment. Id., at 118 (internal quotation marks
omitted). Whether a search is reasonable “is determined by
assessing, on the one hand, the degree to which it intrudes
upon an individual’s privacy and, on the other, the degree to
which it is needed for the promotion of legitimate govern
mental interests.” Id., at 118–119 (internal quotation
marks omitted).
  We recently applied this approach in United States v.
Knights. In that case, California law required Knights, as
a probationer, to “ ‘[s]ubmit his . . . person, property, place
of residence, vehicle, personal effects, to search anytime,
with or without a search warrant, warrant of arrest or
reasonable cause by any probation officer or law enforce
ment officer.’ ” Id., at 114 (brackets in original). Several
days after Knights had been placed on probation, police
suspected that he had been involved in several incidents of
arson and vandalism. Based upon that suspicion and
pursuant to the search condition of his probation, a police
officer conducted a warrantless search of Knights’ apart
ment and found arson and drug paraphernalia. Id., at
115–116.
  We concluded that the search of Knights’ apartment was
reasonable. In evaluating the degree of intrusion into
——————
   1 Knights, 534 U. S., at 120, n. 6 (“We do not decide whether the proba

tion condition so diminished, or completely eliminated, Knights’ reason
able expectation of privacy . . . that a search by a law enforcement officer
without any individualized suspicion would have satisfied the reasonable
ness requirement of the Fourth Amendment”).
4                  SAMSON v. CALIFORNIA

                     Opinion of the Court

Knights’ privacy, we found Knights’ probationary status
“salient,” id., at 118, observing that “[p]robation is ‘one
point . . . on a continuum of possible punishments ranging
from solitary confinement in a maximum-security facility
to a few hours of mandatory community service.’ ” Id., at
119 (quoting Griffin v. Wisconsin, 483 U. S. 868, 874
(1987)). Cf. Hudson v. Palmer, 468 U. S. 517, 530 (1984)
(holding that prisoners have no reasonable expectation of
privacy). We further observed that, by virtue of their status
alone, probationers “ ‘do not enjoy “the absolute liberty to
which every citizen is entitled,” ’ ” Knights, supra, at 119
(quoting Griffin, supra, at 874, in turn quoting Morrissey
v. Brewer, 408 U. S. 471, 480 (1972)), justifying the “im
pos[ition] [of] reasonable conditions that deprive the of
fender of some freedoms enjoyed by law-abiding citizens.”
Knights, supra, at 119. We also considered the facts that
Knights’ probation order clearly set out the probation
search condition, and that Knights was clearly informed of
the condition. See Knights, 534 U. S., at 119. We con
cluded that under these circumstances, Knights’ expecta
tion of privacy was significantly diminished. See id., at
119–120.
   We also concluded that probation searches, such as the
search of Knights’ apartment, are necessary to the promo
tion of legitimate governmental interests. Noting the
State’s dual interest in integrating probationers back into
the community and combating recidivism, see id., at 120–
121, we credited the “ ‘assumption’ ” that, by virtue of his
status, a probationer “ ‘is more likely than the ordinary
citizen to violate the law.’ ” Id., at 120 (quoting Griffin,
supra, at 880). We further found that “probationers have
even more of an incentive to conceal their criminal activi
ties and quickly dispose of incriminating evidence than the
ordinary criminal because probationers are aware that
they may be subject to supervision and face revocation of
probation, and possible incarceration, in proceedings in
                  Cite as: 547 U. S. ____ (2006)              5

                      Opinion of the Court

which the trial rights of a jury and proof beyond a reason
able doubt, among other things, do not apply.” Knights,
534 U. S., at 120. We explained that the State did not
have to ignore the reality of recidivism or suppress its
interests in “protecting potential victims of criminal en
terprise” for fear of running afoul of the Fourth Amend
ment. Id., at 121.
  Balancing these interests, we held that “[w]hen an
officer has reasonable suspicion that a probationer subject
to a search condition is engaged in criminal activity, there
is enough likelihood that criminal conduct is occurring
that an intrusion on the probationer’s significantly dimin
ished privacy interests is reasonable.” Ibid. Because the
search at issue in Knights was predicated on both the
probation search condition and reasonable suspicion, we
did not reach the question whether the search would have
been reasonable under the Fourth Amendment had it been
solely predicated upon the condition of probation. Id., at
120, n. 6. Our attention is directed to that question today,
albeit in the context of a parolee search.
                               III
   As we noted in Knights, parolees are on the “continuum”
of state-imposed punishments. Id., at 119 (internal quota
tion marks omitted). On this continuum, parolees have
fewer expectations of privacy than probationers, because
parole is more akin to imprisonment than probation is to
imprisonment. As this Court has pointed out, “parole is an
established variation on imprisonment of convicted crimi
nals. . . . The essence of parole is release from prison, before
the completion of sentence, on the condition that the pris
oner abides by certain rules during the balance of the sen
tence.” Morrissey, supra, at 477. “In most cases, the State
is willing to extend parole only because it is able to condition
it upon compliance with certain requirements.” Pennsyl
vania Bd. of Probation and Parole v. Scott, 524 U. S. 357,
6                     SAMSON v. CALIFORNIA

                          Opinion of the Court

365 (1998). See also United States v. Reyes, 283 F. 3d 446,
461 (CA2 2002) (“[F]ederal supervised release, . . . in
contrast to probation, is meted out in addition to, not in
lieu of, incarceration” (citation and internal quotation
marks omitted)); United States v. Cardona, 903 F. 2d 60,
63 (CA1 1990) (“[O]n the Court’s continuum of possible
punishments, parole is the stronger medicine; ergo, parol
ees enjoy even less of the average citizen’s absolute liberty
than do probationers” (internal quotation marks and
citation omitted)).2
   California’s system of parole is consistent with these
observations: A California inmate may serve his parole
period either in physical custody, or elect to complete his
sentence out of physical custody and subject to certain
conditions. Cal. Penal Code Ann. §3060.5 (West 2000).
Under the latter option, an inmate-turned-parolee re
mains in the legal custody of the California Department of
Corrections through the remainder of his term, §3056, and
——————
    2 Contrary
             to the dissent’s contention, nothing in our recognition that
parolees are more akin to prisoners than probationers is inconsistent
with our precedents. Nor, as the dissent suggests, do we equate parol
ees with prisoners for the purpose of concluding that parolees, like
prisoners, have no Fourth Amendment rights. See post, at 5 (opinion of
STEVENS, J.). That view misperceives our holding. If that were the
basis of our holding, then this case would have been resolved solely
under Hudson v. Palmer, 468 U. S. 517 (1984), and there would have
been no cause to resort to Fourth Amendment analysis. See ibid.
(holding traditional Fourth Amendment analysis of the totality of the
circumstances inapplicable to the question whether a prisoner had a
reasonable expectation of privacy in his prison cell). Nor is our ration
ale inconsistent with Morrissey v. Brewer, 408 U. S. 471, 482 (1972). In
that case, the Court recognized that restrictions on a parolee’s liberty
are not unqualified. That statement, even if accepted as a truism,
sheds no light on the extent to which a parolee’s constitutional rights
are indeed limited—and no one argues that a parolee’s constitutional
rights are not limited. Morrissey itself does not cast doubt on today’s
holding given that the liberty at issue in that case—the Fourteenth
Amendment Due Process right to a hearing before revocation of pa
role—invokes wholly different analysis than the search at issue here.
                 Cite as: 547 U. S. ____ (2006)            7

                     Opinion of the Court

must comply with all of the terms and conditions of parole,
including mandatory drug tests, restrictions on association
with felons or gang members, and mandatory meetings
with parole officers, Cal. Code Regs., tit. 15, §2512 (2005);
Cal. Penal Code Ann. §3067 (West 2000). See also Morris
sey, supra, at 478 (discussing other permissible terms and
conditions of parole). General conditions of parole also
require a parolee to report to his assigned parole officer
immediately upon release, inform the parole officer within
72 hours of any change in employment status, request
permission to travel a distance of more than 50 miles from
the parolee’s home, and refrain from criminal conduct and
possession of firearms, specified weapons, or knives unre
lated to employment. Cal. Code Regs., tit. 15, §2512.
Parolees may also be subject to special conditions, includ
ing psychiatric treatment programs, mandatory absti
nence from alcohol, residence approval, and “[a]ny other
condition deemed necessary by the Board [of Parole Hear
ings] or the Department [of Corrections and Rehabilita
tion] due to unusual circumstances.” §2513. The extent
and reach of these conditions clearly demonstrate that
parolees like petitioner have severely diminished expecta
tions of privacy by virtue of their status alone.
   Additionally, as we found “salient” in Knights with
respect to the probation search condition, the parole
search condition under California law—requiring inmates
who opt for parole to submit to suspicionless searches by a
parole officer or other peace officer “at any time,” Cal.
Penal Code Ann. §3067(a) (West 2000)—was “clearly
expressed” to petitioner. Knights, 534 U. S., at 119. He
signed an order submitting to the condition and thus was
“unambiguously” aware of it. Ibid. In Knights, we found
that acceptance of a clear and unambiguous search condi
tion “significantly diminished Knights’ reasonable expec
tation of privacy.” Id., at 120. Examining the totality of
the circumstances pertaining to petitioner’s status as a
8                      SAMSON v. CALIFORNIA

                          Opinion of the Court

parolee, “an established variation on imprisonment,” Mor
rissey, 408 U. S., at 477, including the plain terms of the
parole search condition, we conclude that petitioner did
not have an expectation of privacy that society would
recognize as legitimate.3
   The State’s interests, by contrast, are substantial. This
Court has repeatedly acknowledged that a State has an
“overwhelming interest” in supervising parolees because
“parolees. . . are more likely to commit future criminal
offenses.” Pennsylvania Bd. of Probation and Parole, 524
U. S., at 365 (explaining that the interest in combating
recidivism “is the very premise behind the system of close
parole supervision”). Similarly, this Court has repeatedly
acknowledged that a State’s interests in reducing recidivism
and thereby promoting reintegration and positive citizen
——————
    3 Because we find that the search at issue here is reasonable under
our general Fourth Amendment approach, we need not reach the issue
whether “acceptance of the search condition constituted consent in the
Schneckloth [v. Bustamonte, 412 U. S. 218 (1973),] sense of a complete
waiver of his Fourth Amendment rights.” United States v. Knights, 534
U. S. 112, 118 (2001). The California Supreme Court has not yet
construed Cal. Penal Code Ann. §3067 (West 2000), the statute which
governs parole for crimes committed after 1996, and which imposes the
consent requirement. The California Court of Appeal has, and it has
concluded that, under §3067(b), “inmates who are otherwise eligible for
parole yet refuse to agree to the mandatory search condition will
remain imprisoned . . . until either the inmate (1) agrees to the search
condition and is otherwise eligible for parole or (2) has lost all worktime
credits and is eligible for release after having served the balance of
his/her sentence.” People v. Middleton, 131 Cal. App. 4th 732, 739–740,
31 Cal. Rptr. 3d 813, 818 (2005). Nonetheless, we decline to rest our
holding today on the consent rationale. The California Supreme Court,
we note, has not yet had a chance to address the question squarely, and
it is far from clear that the State properly raised its consent theory in
the courts below.
   Nor do we address whether California’s parole search condition is
justified as a special need under Griffin v. Wisconsin, 483 U. S. 868
(1987), because our holding under general Fourth Amendment princi
ples renders such an examination unnecessary.
                 Cite as: 547 U. S. ____ (2006)            9

                     Opinion of the Court

ship among probationers and parolees warrant privacy
intrusions that would not otherwise be tolerated under the
Fourth Amendment. See Griffin, 483 U. S., at 879; Knights,
supra, at 121.
  The empirical evidence presented in this case clearly
demonstrates the significance of these interests to the
State of California. As of November 30, 2005, California
had over 130,000 released parolees. California’s parolee
population has a 68-to-70 percent recidivism rate. See
California Attorney General, Crime in California 37 (Apr.
2001) (explaining that 68 percent of adult parolees are
returned to prison, 55 percent for a parole violation, 13
percent for the commission of a new felony offense); J.
Petersilia, Challenges of Prisoner Reentry and Parole in
California, 12 California Policy Research Center Brief, p. 2
(June 2000), available at http://www.ucop.edu/cprc/pa
role.pdf (as visited June 15, 2006, and available in Clerk of
Court’s case file) (“70% of the state’s paroled felons reof
fend within 18 months—the highest recidivism rate in the
nation”). This Court has acknowledged the grave safety
concerns that attend recidivism. See Ewing v. California,
538 U. S. 11, 26 (2003) (plurality opinion) (“Recidivism is a
serious public safety concern in California and throughout
the Nation”).
  As we made clear in Knights, the Fourth Amendment
does not render the States powerless to address these
concerns effectively. See 534 U. S., at 121. Contrary to
petitioner’s contention, California’s ability to conduct
suspicionless searches of parolees serves its interest in
reducing recidivism, in a manner that aids, rather than
hinders, the reintegration of parolees into productive
society.
  In California, an eligible inmate serving a determinate
sentence may elect parole when the actual days he has
served plus statutory time credits equal the term imposed
by the trial court, Cal. Penal Code Ann. §§2931, 2933,
10                SAMSON v. CALIFORNIA

                     Opinion of the Court

3000(b)(1) (West 2000), irrespective of whether the inmate
is capable of integrating himself back into productive
society. As the recidivism rate demonstrates, most parol
ees are ill prepared to handle the pressures of reintegra
tion. Thus, most parolees require intense supervision.
The California Legislature has concluded that, given the
number of inmates the State paroles and its high recidi
vism rate, a requirement that searches be based on indi
vidualized suspicion would undermine the State’s ability
to effectively supervise parolees and protect the public
from criminal acts by reoffenders. This conclusion makes
eminent sense. Imposing a reasonable suspicion require
ment, as urged by petitioner, would give parolees greater
opportunity to anticipate searches and conceal criminality.
See Knights, supra, at 120; Griffin, 483 U. S., at 879. This
Court concluded that the incentive-to-conceal concern
justified an “intensive” system for supervising probation
ers in Griffin, id., at 875. That concern applies with even
greater force to a system of supervising parolees. See
United States v. Reyes, 283 F. 3d, at 461 (observing that
the Griffin rationale “appl[ies] a fortiori” to “federal su
pervised release, which, in contrast to probation, is ‘meted
out in addition to, not in lieu of, incareration’ ”); United
States v. Crawford, 372 F. 3d 1048, 1077 (CA9 2004) (en
banc) (Kleinfeld, J., concurring) (explaining that parolees,
in contrast to probationers, “have been sentenced to prison
for felonies and released before the end of their prison
terms” and are “deemed to have acted more harmfully
than anyone except those felons not released on parole”);
Hudson, 468 U. S., at 526 (persons sentenced to terms of
imprisonment have been “deemed to have acted more
harmfully than anyone except those felons not released on
parole”); id., at 529 (observing that it would be “naive” to
institute a system of “ ‘planned random searches’ ” as that
would allow prisoners to “anticipate” searches, thus de
feating the purpose of random searches).
                     Cite as: 547 U. S. ____ (2006)                   11

                          Opinion of the Court

   Petitioner observes that the majority of States and the
Federal Government have been able to further similar
interests in reducing recidivism and promoting re
integration, despite having systems that permit parolee
searches based upon some level of suspicion. Thus, peti
tioner contends, California’s system is constitutionally
defective by comparison. Petitioner’s reliance on the
practices of jurisdictions other than California, however, is
misplaced. That some States and the Federal Government
require a level of individualized suspicion is of little rele
vance to our determination whether California’s supervi
sory system is drawn to meet its needs and is reasonable,
taking into account a parolee’s substantially diminished
expectation of privacy.4
   Nor is there merit to the argument that California’s
parole search law permits “a blanket grant of discretion
——————
   4 The dissent argues that, “once one acknowledges that parolees do

have legitimate expectations of privacy beyond those of prisoners, our
Fourth Amendment jurisprudence does not permit the conclusion,
reached by the Court here for the first time, that a search supported by
neither individualized suspicion nor ‘special needs’ is nonetheless
‘reasonable.’ ” Post, at 2. That simply is not the case. The touchstone
of the Fourth Amendment is reasonableness, not individualized suspi
cion. Thus, while this Court’s jurisprudence has often recognized that
“to accommodate public and private interests some quantum of indi
vidualized suspicion is usually a prerequisite to a constitutional search
or seizure,” United States v. Martinez-Fuerte, 428 U. S. 543, 560 (1976),
we have also recognized that the “Fourth Amendment imposes no
irreducible requirement of such suspicion,” id., at 561. Therefore,
although this Court has only sanctioned suspicionless searches in
limited circumstances, namely programmatic and special needs
searches, we have never held that these are the only limited circum
stances in which searches absent individualized suspicion could be
“reasonable” under the Fourth Amendment. In light of California’s
earnest concerns respecting recidivism, public safety, and reintegration
of parolees into productive society, and because the object of the Fourth
Amendment is reasonableness, our decision today is far from remark
able. Nor, given our prior precedents and caveats, is it “unprece
dented.” Post, at 1.
12                   SAMSON v. CALIFORNIA

                        Opinion of the Court

untethered by any procedural safeguards,” post, at 1
(STEVENS, J., dissenting). The concern that California’s
suspicionless search system gives officers unbridled dis
cretion to conduct searches, thereby inflicting dignitary
harms that arouse strong resentment in parolees and
undermine their ability to reintegrate into productive
society, is belied by California’s prohibition on “arbitrary,
capricious or harassing” searches. See Reyes, 19 Cal. 4th,
at 752, 753–754, 968 P. 2d, at 450, 451; People v. Bravo, 43
Cal. 3d 600, 610, 738 P. 2d 336, 342 (1987) (probation); see
also Cal. Penal Code Ann. §3067(d) (West 2000) (“It is not
the intent of the Legislature to authorize law enforcement
officers to conduct searches for the sole purpose of har
assment”).5 The dissent’s claim that parolees under Cali
fornia law are subject to capricious searches conducted at
the unchecked “whim” of law enforcement officers, post, at
3, 4, ignores this prohibition. Likewise, petitioner’s con
cern that California’s suspicionless search law frustrates
reintegration efforts by permitting intrusions into the
privacy interests of third parties is also unavailing be
cause that concern would arise under a suspicion-based
regime as well.
                             IV
   Thus, we conclude that the Fourth Amendment does not
prohibit a police officer from conducting a suspicionless
search of a parolee. Accordingly, we affirm the judgment
of the California Court of Appeal.
                                           It is so ordered.



——————
  5 Under California precedent, we note, an officer would not act rea

sonably in conducting a suspicionless search absent knowledge that the
person stopped for the search is a parolee. See People v. Sanders, 31
Cal. 4th 318, 331–332, 73 P. 3d 496, 505–506 (2003); Brief for United
States as Amicus Curiae 20.
                 Cite as: 547 U. S. ____ (2006)           1

                    STEVENS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 04–9728
                         _________________


     DONALD CURTIS SAMSON, PETITIONER v.

                CALIFORNIA 

   ON WRIT OF CERTIORARI TO THE COURT OF APPEAL OF

        CALIFORNIA, FIRST APPELLATE DISTRICT

                        [June 19, 2006]

  JUSTICE STEVENS, with whom JUSTICE SOUTER and
JUSTICE BREYER join, dissenting.
  Our prior cases have consistently assumed that the
Fourth Amendment provides some degree of protection for
probationers and parolees. The protection is not as robust
as that afforded to ordinary citizens; we have held that
probationers’ lowered expectation of privacy may justify
their warrantless search upon reasonable suspicion of
wrongdoing, see United States v. Knights, 534 U. S. 112
(2001). We have also recognized that the supervisory
responsibilities of probation officers, who are required to
provide “ ‘individualized counseling’ ” and to monitor their
charges’ progress, Griffin v. Wisconsin, 483 U. S. 868, 876–
877 (1987), and who are in a unique position to judge “how
close a supervision the probationer requires,” id., at 876,
may give rise to special needs justifying departures from
Fourth Amendment strictures. See ibid. (“Although a
probation officer is not an impartial magistrate, neither is
he the police officer who normally conducts searches against
the ordinary citizen”). But neither Knights nor Griffin
supports a regime of suspicionless searches, conducted
pursuant to a blanket grant of discretion untethered by
any procedural safeguards, by law enforcement personnel
who have no special interest in the welfare of the parolee
or probationer.
2                  SAMSON v. CALIFORNIA

                    STEVENS, J., dissenting

   What the Court sanctions today is an unprecedented
curtailment of liberty. Combining faulty syllogism with
circular reasoning, the Court concludes that parolees have
no more legitimate an expectation of privacy in their
persons than do prisoners. However superficially appeal
ing that parity in treatment may seem, it runs roughshod
over our precedent. It also rests on an intuition that fares
poorly under scrutiny. And once one acknowledges that
parolees do have legitimate expectations of privacy beyond
those of prisoners, our Fourth Amendment jurisprudence
does not permit the conclusion, reached by the Court here
for the first time, that a search supported by neither indi
vidualized suspicion nor “special needs” is nonetheless
“reasonable.”
   The suspicionless search is the very evil the Fourth
Amendment was intended to stamp out. See Boyd v.
United States, 116 U. S. 616, 625–630 (1886); see also, e.g.,
Indianapolis v. Edmond, 531 U. S. 32, 37 (2000). The pre-
Revolutionary “writs of assistance,” which permitted
roving searches for contraband, were reviled precisely
because they “placed ‘the liberty of every man in the hands
of every petty officer.’ ” Boyd, 116 U. S., at 625. While
individualized suspicion “is not an ‘irreducible’ component
of reasonableness” under the Fourth Amendment, Ed
mond, 531 U. S., at 37 (quoting United States v. Marti
nez-Fuerte, 428 U. S. 543, 561 (1976)), the requirement
has been dispensed with only when programmatic
searches were required to meet a “ ‘special need’ . . . di
vorced from the State’s general interest in law enforce
ment.” Ferguson v. Charleston, 532 U. S. 67, 79 (2001);
see Edmond, 531 U. S., at 37; see also Griffin, 483 U. S., at
873 (“Although we usually require that a search be under
taken only pursuant to a warrant (and thus supported by
probable cause, as the Constitution says warrants must
be), . . . we have permitted exceptions when ‘special needs,
beyond the normal need for law enforcement, make the
                       Cite as: 547 U. S. ____ (2006)                        3

                          STEVENS, J., dissenting

warrant and probable-cause requirement impracticable’ ”).
   Not surprisingly, the majority does not seek to justify
the search of petitioner on “special needs” grounds. Al
though the Court has in the past relied on special needs to
uphold warrantless searches of probationers, id., at 873,
880, it has never gone so far as to hold that a probationer
or parolee may be subjected to full search at the whim of
any law enforcement officer he happens to encounter,
whether or not the officer has reason to suspect him of
wrongdoing. Griffin, after all, involved a search by a
probation officer that was supported by reasonable suspi
cion. The special role of probation officers was critical to
the analysis; “we deal with a situation,” the Court ex
plained, “in which there is an ongoing supervisory rela
tionship—and one that is not, or at least not entirely,
adversarial—between the object of the search and the
decisionmaker.” Id., at 879. The State’s interest or “spe
cial need,” as articulated in Griffin, was an interest in
supervising the wayward probationer’s reintegration into
society—not, or at least not principally, the general law
enforcement goal of detecting crime, see ante, at 8–9.1
——————
   1 As we observed in Ferguson v. Charleston, 532 U. S. 67 (2001), Grif

fin’s special needs rationale was cast into doubt by our later decision in
Skinner v. Railway Labor Executives’ Assn., 489 U. S. 602 (1989), which
reserved the question whether “ ‘routine use in criminal prosecutions of
evidence obtained pursuant to the administrative scheme would give rise
to an inference of pretext, or otherwise impugn the administrative nature
of the . . . program,’ ” Ferguson, 532 U. S., at 79, n. 15 (quoting Skinner,
489 U. S., at 621, n. 5). But at least the State in Griffin could in good faith
contend that its warrantless searches were supported by a special need
conceptually distinct from law enforcement goals generally. Indeed, that a
State’s interest in supervising its parolees and probationers to ensure
their smooth reintegration may occasionally diverge from its general law
enforcement aims is illustrated by this very case. Petitioner’s possession
of a small amount of illegal drugs would not have been grounds for
revocation of his parole. See Cal. Penal Code Ann. §3063.1(a) (West Supp.
2006). Presumably, the California Legislature determined that it is
unnecessary and perhaps even counterproductive, as a means of further
4                     SAMSON v. CALIFORNIA

                        STEVENS, J., dissenting

   It is no accident, then, that when we later upheld the
search of a probationer by a law enforcement officer (again,
based on reasonable suspicion), we forwent any reliance on
the special needs doctrine. See Knights, 534 U. S. 112.
Even if the supervisory relationship between a probation
officer and her charge may properly be characterized as
one giving rise to needs “divorced from the State’s general
interest in law enforcement,” Ferguson, 532 U. S., at 79;
but see id., at 79, n. 15, the relationship between an ordi
nary law enforcement officer and a probationer unknown
to him may not. “None of our special needs precedents has
sanctioned the routine inclusion of law enforcement, both
in the design of the policy and in using arrests, either
threatened or real, to implement the system designed for
the special needs objectives.” Id., at 88 (KENNEDY, J.,
concurring in judgment).
   Ignoring just how “closely guarded” is that “category of
constitutionally permissible suspicionless searches,”
Chandler v. Miller, 520 U. S. 305, 309 (1997), the Court for
the first time upholds an entirely suspicionless search
unsupported by any special need. And it goes further: In
special needs cases we have at least insisted upon pro
grammatic safeguards designed to ensure evenhandedness
in application; if individualized suspicion is to be jetti
soned, it must be replaced with measures to protect
against the state actor’s unfettered discretion. See, e.g.,
Delaware v. Prouse, 440 U. S. 648, 654–655 (1979) (where
a special need “precludes insistence upon ‘some quantum
of individualized suspicion,’ other safeguards are generally
relied upon to assure that the individual’s reasonable
expectation of privacy is not ‘subject to the discretion of
the official in the field’ ” (quoting Camara v. Municipal
—————— 

ing the goals of the parole system, to reincarcerate former prisoners for

simple possession. The general law enforcement interests the State 

espouses, by contrast, call for reincarceration. 

                       Cite as: 547 U. S. ____ (2006)                        5

                          STEVENS, J., dissenting

Court of City and County of San Francisco, 387 U. S. 523,
532 (1967); footnote omitted); United States v. Brignoni-
Ponce, 422 U. S. 873, 882 (1975) (“[T]he reasonableness
requirement of the Fourth Amendment demands some
thing more than the broad and unlimited discretion
sought by the Government”). Here, by contrast, there are
no policies in place—no “standards, guidelines, or proce
dures,” Prouse, 440 U. S., at 650—to rein in officers and
furnish a bulwark against the arbitrary exercise of discre
tion that is the height of unreasonableness.
   The Court is able to make this unprecedented move only
by making another. Coupling the dubious holding of
Hudson v. Palmer, 468 U. S. 517 (1984), with the bald
statement that “parolees have fewer expectations of pri
vacy than probationers,” ante, at 5, the Court two-steps its
way through a faulty syllogism and, thus, avoids the
application of Fourth Amendment principles altogether.
The logic, apparently, is this: Prisoners have no legitimate
expectation of privacy; parolees are like prisoners; there
fore, parolees have no legitimate expectation of privacy.
The conclusion is remarkable not least because we have
long embraced its opposite.2 It also rests on false prem
ises. First, it is simply not true that a parolee’s status,
vis-à-vis either the State or the Constitution, is tanta
mount to that of a prisoner or even materially distinct
from that of a probationer. See Morrissey v. Brewer, 408
U. S. 471, 482 (1972) (“Though the State properly subjects
[a parolee] to many restrictions not applicable to other
——————
  2 See  Morrissey v. Brewer, 408 U. S. 471, 482 (1972) (“[T]he liberty of a
parolee, although indeterminate, includes many of the core values of
unqualified liberty”); Griffin v. Wisconsin, 483 U. S. 868, 875 (1987) (the
“degree of impingement upon [a probationer’s] privacy . . . is not unlim
ited”); see also Ferguson, 532 U. S., at 101 (SCALIA, J., dissenting) (“I doubt
whether Griffin’s reasonable expectation of privacy in his home was any
less than petitioners’ reasonable expectation of privacy in their urine
taken”).
6                  SAMSON v. CALIFORNIA

                     STEVENS, J., dissenting

citizens, his condition is very different from that of con
finement in a prison”). A parolee, like a probationer, is set
free in the world subject to restrictions intended to facili
tate supervision and guard against antisocial behavior. As
with probation, “the State is willing to extend parole only
because it is able to condition it upon compliance with
certain requirements.” Pennsylvania Bd. of Probation and
Parole v. Scott, 524 U. S. 357, 365 (1998). Certainly,
parole differs from probation insofar as parole is “ ‘meted
out in addition to, not in lieu of, incarceration.’ ” Ante, at 6
(quoting United States v. Reyes, 283 F. 3d 446, 461 (CA2
2002)). And, certainly, parolees typically will have com
mitted more serious crimes—ones warranting a prior term
of imprisonment—than probationers. The latter distinc
tion, perhaps, would support the conclusion that a State
has a stronger interest in supervising parolees than it
does in supervising probationers. But see United States v.
Williams, 417 F. 3d 373, 376, n. 1 (CA3 2005) (“ ‘[T]here is
no constitutional difference between probation and parole
for purposes of the [F]ourth [A]mendment’ ”). But why
either distinction should result in refusal to acknowledge
as legitimate, when harbored by parolees, the same expec
tation of privacy that probationers reasonably may harbor
is beyond fathom.
   In any event, the notion that a parolee legitimately
expects only so much privacy as a prisoner is utterly with
out foundation. Hudson v. Palmer does stand for the
proposition that “[a] right of privacy in traditional Fourth
Amendment terms” is denied individuals who are incar
cerated. 468 U. S., at 527. But this is because it “is neces
sary, as a practical matter, to accommodate a myriad of
‘institutional needs and objectives’ of prison facilities, . . .
chief among which is internal security.” Id., at 524; see
id., at 538 (O’Connor, J., concurring) (“I agree that the
government’s compelling interest in prison safety, together
with the necessarily ad hoc judgments required of prison
                     Cite as: 547 U. S. ____ (2006)                    7

                        STEVENS, J., dissenting

officials, make prison cell searches and seizures appropri
ate for categorical treatment”3); see also Treasury Employ
ees v. Von Raab, 489 U. S. 656, 680 (1989) (SCALIA, J.,
dissenting). These “institutional needs”—safety of in
mates and guards, “internal order,” and sanitation, Hud
son, 468 U. S., at 527–528—manifestly do not apply to
parolees. As discussed above and in Griffin, other state
interests may warrant certain intrusions into a parolee’s
privacy, but Hudson’s rationale cannot be mapped blindly
onto the situation with which we are presented in this
case.
   Nor is it enough, in deciding whether someone’s expec
tation of privacy is “legitimate,” to rely on the existence of
the offending condition or the individual’s notice thereof.
Cf. ante, at 7. The Court’s reasoning in this respect is
entirely circular. The mere fact that a particular State
refuses to acknowledge a parolee’s privacy interest cannot
mean that a parolee in that State has no expectation of
privacy that society is willing to recognize as legitimate—
especially when the measure that invades privacy is both
the subject of the Fourth Amendment challenge and a
clear outlier. With only one or two arguable exceptions,
neither the Federal Government nor any other State
subjects parolees to searches of the kind to which peti
tioner was subjected. And the fact of notice hardly cures
the circularity; the loss of a subjective expectation of pri
vacy would play “no meaningful role” in analyzing the
legitimacy of expectations, for example, “if the Govern
ment were suddenly to announce on nationwide television
that all homes henceforth would be subject to warrantless
entry.” Smith v. Maryland, 442 U. S. 735, 740–741, n. 5
——————
  3 Particularly in view of Justice O’Connor’s concurrence, which em

phasized the prison’s programmatic interests in conducting suspi
cionless searches, see Hudson, 468 U. S., at 538, Hudson is probably best
understood as a “special needs” case—not as standing for the blanket
proposition that prisoners have no Fourth Amendment rights.
8                      SAMSON v. CALIFORNIA

                         STEVENS, J., dissenting

(1979).4
    Threaded through the Court’s reasoning is the sugges
tion that deprivation of Fourth Amendment rights is part
and parcel of any convict’s punishment. See ante, at 4–6.5
If a person may be subject to random and suspicionless
searches in prison, the Court seems to assume, then he
cannot complain when he is subject to the same invasion
outside of prison, so long as the State still can imprison
him. Punishment, though, is not the basis on which Hud
son was decided. (Indeed, it is settled that a prison inmate
“ ‘retains those [constitutional] rights that are not incon
sistent with his status as a prisoner or with the legitimate
penological objectives of the corrections system.’ ” Turner
v. Safley, 482 U. S. 78, 95 (1987).) Nor, to my knowledge,
have we ever sanctioned the use of any search as a puni
tive measure. Instead, the question in every case must be
whether the balance of legitimate expectations of privacy,
on the one hand, and the State’s interests in conducting
the relevant search, on the other, justifies dispensing with
——————
   4 Likewise, the State’s argument that a California parolee “consents”

to the suspicionless search condition is sophistry. Whether or not a
prisoner can choose to remain in prison rather than be released on
parole, cf. ante, at 8, n. 3, he has no “choice” concerning the search
condition; he may either remain in prison, where he will be subjected to
suspicionless searches, or he may exit prison and still be subject to
suspicionless searches. Accordingly, “to speak of consent in this context
is to resort to a manifest fiction, for the [parolee] who purportedly
waives his rights by accepting such a condition has little genuine option
to refuse.” 5 W. LaFave, Search and Seizure: A Treatise on the Fourth
Amendment §10.10(b), pp. 440–441 (4th ed. 2004).
   5 This is a vestige of the long-discredited “act of grace” theory of pa

role. Compare Escoe v. Zerbst, 295 U. S. 490, 492–493 (1935) (“Probation
or suspension of sentence comes as an act of grace to one convicted of a
crime, and may be coupled with such conditions in respect of its duration
as Congress may impose”), with Gagnon v. Scarpelli, 411 U. S. 778, 782, n.
4 (1973) (“a probationer can no longer be denied due process, in reliance
on the dictum in Escoe v. Zerbst, that probation is an ‘act of grace’ ”
(citation omitted)). See also Morrissey, 408 U. S., at 482.
                    Cite as: 547 U. S. ____ (2006)                  9

                       STEVENS, J., dissenting

the warrant and probable-cause requirements that are
otherwise dictated by the Fourth Amendment. That bal
ance is not the same in prison as it is out. We held in
Knights—without recourse to Hudson—that the balance
favored allowing the State to conduct searches based on
reasonable suspicion. Never before have we plunged
below that floor absent a demonstration of “special needs.”
   Had the State imposed as a condition of parole a re
quirement that petitioner submit to random searches by
his parole officer, who is “supposed to have in mind the
welfare of the [parolee]” and guide the parolee’s transition
back into society, Griffin, 483 U. S., at 876–877, the condi
tion might have been justified either under the special
needs doctrine or because at least part of the requisite
“reasonable suspicion” is supplied in this context by the
individual-specific knowledge gained through the supervi
sory relationship. See id., at 879 (emphasizing probation
office’s ability to “assess probabilities in the light of its
knowledge of [the probationer’s] life, character, and cir
cumstances”). Likewise, this might have been a different
case had a court or parole board imposed the condition at
issue based on specific knowledge of the individual’s
criminal history and projected likelihood of reoffending, or
if the State had had in place programmatic safeguards to
ensure evenhandedness. See supra, at 4. Under either of
those scenarios, the State would at least have gone some
way toward averting the greatest mischief wrought by
officials’ unfettered discretion. But the search condition
here is imposed on all parolees—whatever the nature of
their crimes, whatever their likelihood of recidivism, and
whatever their supervisory needs—without any program
matic procedural protections.6
——————
  6 The Court devotes a good portion of its analysis to the recidivism

rates among parolees in California. See ante, at 8–9. One might
question whether those statistics, which postdate the California Su
10                     SAMSON v. CALIFORNIA

                         STEVENS, J., dissenting

   The Court seems to acknowledge that unreasonable
searches “inflic[t] dignitary harms that arouse strong
resentment in parolees and undermine their ability to
reintegrate into productive society.” Ante, at 11; see Terry
v. Ohio, 392 U. S. 1, 19, 29 (1968). It is satisfied, however,
that the California courts’ prohibition against “ ‘arbitrary,
capricious or harassing’ ” searches suffices to avert those
harms—which are of course counterproductive to the
State’s purported aim of rehabilitating former prisoners
and reintegrating them into society. See ante, at 11 (citing
People v. Reyes, 19 Cal. 4th 743, 968 P. 2d 445 (1998)). I
am unpersuaded.        The requirement of individualized
suspicion, in all its iterations, is the shield the Framers
selected to guard against the evils of arbitrary action,
caprice, and harassment. To say that those evils may be
averted without that shield is, I fear, to pay lipservice to
the end while withdrawing the means.7
   Respectfully, I dissent.




——————
preme Court’s decision to allow the purportedly recidivism-reducing
suspicionless searches at issue here, actually demonstrate that the
State’s interest is being served by the searches. Cf. Reply Brief for
Petitioner 10, and n. 10. Of course, one cannot deny that the interest
itself is valid. That said, though, it has never been held sufficient to
justify suspicionless searches. If high crime rates were grounds enough
for disposing of Fourth Amendment protections, the Amendment long
ago would have become a dead letter.
   7 As the Court observes, see ante, at 12, n. 5, under California law “an

officer is entitled to conduct suspicionless searches only of persons
known by him to be parolees.” Brief for United States as Amicus
Curiae 20 (citing People v. Sanders, 31 Cal. 4th 318, 331–332, 73 P. 3d
496, 505 (2003)). It would necessarily be arbitrary, capricious, and
harassing to conduct a suspicionless search of someone without knowl
edge of the status that renders that person, in the State’s judgment,
susceptible to such an invasion.

```

---
