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

## GROUP: content/cases/Harris v. New York.md  (`case`, 6 assertions)

### content_page

```
---
title: "Harris v. New York"
type: case
citation: "401 U.S. 222 (1971)"
parallel_cite: "91 S. Ct. 643; 28 L. Ed. 2d 1"
neutral_cite: 1971 U.S. LEXIS 75
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1971
date_decided: 1971-02-24
docket: 206
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1971-02-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Harris v. New York
  varies_by_point: false
  scope_note: "Good law; the Miranda impeachment exception was extended in Oregon v. Hass and (for the Fourth Amendment) tracks Walder/Havens, but does not reach silence (Doyle) or defense witnesses (James v. Illinois)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108272/harris-v-new-york/"
  cluster_id: 108272
  opinion_id: 108272
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Limiting"
  - page: "[[Fruits & Attenuation]]"
    role: "Related (cross-doctrine)"
related: ["[[James v. Illinois]]", "[[United States v. Havens]]", "[[Doyle v. Ohio]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "impeachment", "exclusionary-rule"]
holding: "A statement taken in violation of Miranda, but otherwise voluntary, may be used to impeach the defendant's contrary trial testimony; Miranda's shield may not be turned into a license to commit perjury free from confrontation with prior inconsistent statements."
lake:
  record_id: Harris v. New York
  status: verified
  projected_at: 2026-07-06
---

# Harris v. New York

*401 U.S. 222 (1971)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Harris was charged with selling heroin. He had made statements to police that were inadmissible in the prosecution's case-in-chief because adequate [[Miranda and Custodial Interrogation|Miranda warnings]] had not been given. At trial Harris took the stand and gave testimony contradicting those statements. Over objection, the prosecution used the earlier statements on cross-examination to impeach his credibility. There was no claim the statements had been coerced or were involuntary.

## Issue
Whether a statement that is inadmissible in the prosecution's case-in-chief for want of [[Miranda and Custodial Interrogation|Miranda warnings]], but that is otherwise voluntary, may nonetheless be used to impeach the defendant's credibility when he testifies inconsistently at trial.

## Rule
Yes. "Having voluntarily taken the stand, petitioner was under an obligation to speak truthfully and accurately, and the prosecution here did no more than utilize the traditional truth-testing devices of the adversary process." — 401 U.S. at 225. ^pin-225

"The shield provided by *Miranda* cannot be perverted into a license to use perjury by way of a defense, free from the risk of confrontation with prior inconsistent utterances. We hold, therefore, that petitioner's credibility was appropriately impeached by use of his earlier conflicting statements." — *Id.* at 226. ^pin-226

The exception applies only where the statement is otherwise voluntary and trustworthy; a coerced statement could not be used even to impeach.

## Application
Harris's statements were voluntary; their only defect was the [[Miranda and Custodial Interrogation|Miranda warning]] lapse. When he testified to a contrary account, the State could confront him with the prior inconsistent statements to test his credibility before the jury. *[[Miranda v. Arizona|Miranda]]*'s exclusionary protection guards against using such statements as affirmative proof of guilt, but it does not license a defendant to take the stand and testify falsely immune from impeachment.

## Conclusion
The impeachment use of the un-Mirandized but voluntary statements was proper; the conviction was affirmed. This established the **impeachment exception** to *[[Miranda v. Arizona|Miranda]]*'s exclusionary rule.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The exception is bounded: it does not permit impeachment by **post-arrest silence** ([[Doyle v. Ohio]]) and does not extend to **defense witnesses** other than the defendant ([[James v. Illinois]]); the Fourth Amendment analog runs through [[United States v. Havens]].

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Limiting*
- [[The Exclusionary Rule]] — *Related (cross-doctrine)*

## Sources
- *Harris v. New York*, 401 U.S. 222 (1971) — https://www.courtlistener.com/opinion/108272/harris-v-new-york/ — pinpoints: 225, 226.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7f3a892e72cf402a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "401 U.S. 222 (1971)", "court": "U.S. Supreme Court", "neutral_cite": "1971 U.S. LEXIS 75", "official_citation_present": true, "parallel_cite": "91 S. Ct. 643; 28 L. Ed. 2d 1", "title": "Harris v. New York", "year": "1971"}}
{"assertion_id": "17899ac715a1299c", "dimension": "support", "kind": "home_role", "locator": {"home": "Fruits & Attenuation"}, "payload": {"home": "Fruits & Attenuation", "role": "Related (cross-doctrine)", "title": "Harris v. New York"}}
{"assertion_id": "5ef6685c6b9eeafb", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A statement taken in violation of Miranda, but otherwise voluntary, may be used to impeach the defendant's contrary trial testimony; Miranda's shield may not be turned into a license to commit perjury free from confrontation with prior inconsistent statements.", "title": "Harris v. New York"}}
{"assertion_id": "9f28f10150f2c8f7", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Limiting", "title": "Harris v. New York"}}
{"assertion_id": "9a459a1584e8b553", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Harris v. New York"}}
{"assertion_id": "a338a45f66fab22c", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1971-02-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Harris v. New York", "field_i_validity": "good_law", "scope_note": "Good law; the Miranda impeachment exception was extended in Oregon v. Hass and (for the Fourth Amendment) tracks Walder/Havens, but does not reach silence (Doyle) or defense witnesses (James v. Illinois).", "title": "Harris v. New York", "varies_by_point": "false"}}
```

### lake record — Harris v. New York

```json
{
  "schema_version": "s2.v1",
  "record_id": "Harris v. New York",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Harris v. New York",
    "case_name_short": "Harris",
    "case_name_full": "Harris v. New York",
    "input_case_name": "Harris v. New York",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1971-02-24",
    "year": 1971,
    "docket": "206",
    "cluster_id": 108272,
    "lead_opinion_id": 108272,
    "sibling_ids": [
      108272,
      9424454,
      9424455
    ],
    "absolute_url": "/opinion/108272/harris-v-new-york/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "401 U.S. 222",
      "volume": "401",
      "reporter": "U.S.",
      "page": "222",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "91 S. Ct. 643",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "643",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "28 L. Ed. 2d 1",
        "volume": "28",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1971 U.S. LEXIS 75",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "75",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "401 U.S. 222",
        "volume": "401",
        "reporter": "U.S.",
        "page": "222",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 S. Ct. 643",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "643",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "28 L. Ed. 2d 1",
        "volume": "28",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1971 U.S. LEXIS 75",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "75",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "401 U.S. 222",
    "official_selection": {
      "court_class": "scotus",
      "selected": "401 U.S. 222",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-225",
      "page": null,
      "quote": "--- # Harris v. New York *401 U.S. 222 (1971)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Harris was charged with selling heroin. He had made statements to police that were inadmissible in the prosecution's case-in-chief because adequate Miranda warnings had not been given. At trial Harris took the stand and gave testimony contradicting those statements. Over objection, the prosecution used the earlier statements on cross-examination to impeach his credibility. There was no claim the statements had been coerced or were involuntary. ## Issue Whether a statement that is inadmissible in the prosecution's case-in-chief for want of Miranda warnings, but that is otherwise voluntary, may nonetheless be used to impeach the defendant's credibility when he testifies inconsistently at trial. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-226",
      "page": null,
      "quote": "The shield provided by *Miranda* cannot be perverted into a license to use perjury by way of a defense, free from the risk of confrontation with prior inconsistent utterances. We hold, therefore, that petitioner's credibility was appropriately impeached by use of his earlier conflicting statements.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1971-02-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Harris v. New York",
    "varies_by_point": false,
    "scope_note": "Good law; the Miranda impeachment exception was extended in Oregon v. Hass and (for the Fourth Amendment) tracks Walder/Havens, but does not reach silence (Doyle) or defense witnesses (James v. Illinois).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "People v. Hopson",
          "cluster_id": 4405826,
          "cite": [
            "219 Cal. Rptr. 3d 717",
            "396 P.3d 1054",
            "3 Cal. 5th 424",
            "2017 WL 2837126",
            "2017 Cal. LEXIS 4894"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Richared E. Ladue",
          "cluster_id": 4489460,
          "cite": [
            "168 A.3d 430",
            "2017 VT 20",
            "2017 Vt. LEXIS 23"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thomas Rigterink v. State of Florida",
          "cluster_id": 3196514,
          "cite": [
            "193 So. 3d 846",
            "41 Fla. L. Weekly Supp. 177",
            "2016 WL 1592714",
            "2016 Fla. LEXIS 835"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Patrick Broom a/k/a Patrick Brown v. United States",
          "cluster_id": 2809687,
          "cite": [
            "118 A.3d 207",
            "2015 D.C. App. LEXIS 265",
            "2015 WL 3768885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth, Aplt. v. Molina, M.",
          "cluster_id": 2753817,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Curtis Tyrell Cutler v. State of Indiana",
          "cluster_id": 2727954,
          "cite": [
            "983 N.E.2d 217",
            "2013 WL 633050",
            "2013 Ind. App. LEXIS 82"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Reid",
          "cluster_id": 5641509,
          "cite": [
            "19 N.Y.3d 382",
            "971 N.E.2d 353"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Allen Murdock",
          "cluster_id": 622650,
          "cite": [
            "399 U.S. App. D.C. 153",
            "667 F.3d 1302",
            "2012 WL 414459",
            "2012 U.S. App. LEXIS 2599"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. McCollum",
          "cluster_id": 6589541,
          "cite": [
            "79 Mass. App. Ct. 239",
            "945 N.E.2d 937",
            "2011 Mass. App. LEXIS 546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Garvin",
          "cluster_id": 6580150,
          "cite": [
            "456 Mass. 778",
            "926 N.E.2d 169",
            "2010 Mass. LEXIS 216"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Simon",
          "cluster_id": 2483876,
          "cite": [
            "456 Mass. 280",
            "923 N.E.2d 58",
            "2010 Mass. LEXIS 89"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lawrence Samuel Jr. v. State",
          "cluster_id": 3130658,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Faretta v. California",
          "cluster_id": 109309,
          "cite": [
            "45 L. Ed. 2d 562",
            "95 S. Ct. 2525",
            "422 U.S. 806",
            "1975 U.S. LEXIS 83"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mateo",
          "cluster_id": 2006639,
          "cite": [
            "811 N.E.2d 1053",
            "2 N.Y.3d 383",
            "779 N.Y.S.2d 399",
            "2 N.Y. 383",
            "2004 N.Y. LEXIS 263"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doyle v. Ohio",
          "cluster_id": 109491,
          "cite": [
            "49 L. Ed. 2d 91",
            "96 S. Ct. 2240",
            "426 U.S. 610",
            "1976 U.S. LEXIS 66"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mincey v. Arizona",
          "cluster_id": 109905,
          "cite": [
            "57 L. Ed. 2d 290",
            "98 S. Ct. 2408",
            "437 U.S. 385",
            "1978 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richardson v. Marsh",
          "cluster_id": 111865,
          "cite": [
            "95 L. Ed. 2d 176",
            "107 S. Ct. 1702",
            "481 U.S. 200",
            "1987 U.S. LEXIS 1812",
            "55 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Mosley",
          "cluster_id": 109336,
          "cite": [
            "46 L. Ed. 2d 313",
            "96 S. Ct. 321",
            "423 U.S. 96",
            "1975 U.S. LEXIS 100"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rock v. Arkansas",
          "cluster_id": 111933,
          "cite": [
            "97 L. Ed. 2d 37",
            "107 S. Ct. 2704",
            "483 U.S. 44",
            "1987 U.S. LEXIS 2732",
            "55 U.S.L.W. 4925",
            "22 Fed. R. Serv. 1128"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McKaskle v. Wiggins",
          "cluster_id": 111095,
          "cite": [
            "79 L. Ed. 2d 122",
            "104 S. Ct. 944",
            "465 U.S. 168",
            "1984 U.S. LEXIS 24",
            "52 U.S.L.W. 4176"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baxter v. Palmigiano",
          "cluster_id": 109429,
          "cite": [
            "47 L. Ed. 2d 810",
            "96 S. Ct. 1551",
            "425 U.S. 308",
            "1976 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Salvucci",
          "cluster_id": 110325,
          "cite": [
            "65 L. Ed. 2d 619",
            "100 S. Ct. 2547",
            "448 U.S. 83",
            "1980 U.S. LEXIS 141"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fare v. Michael C.",
          "cluster_id": 110117,
          "cite": [
            "61 L. Ed. 2d 197",
            "99 S. Ct. 2560",
            "442 U.S. 707",
            "1979 U.S. LEXIS 133"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salinas v. State",
          "cluster_id": 1685186,
          "cite": [
            "163 S.W.3d 734",
            "2005 Tex. Crim. App. LEXIS 741",
            "2005 WL 1162528"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Hass",
          "cluster_id": 109221,
          "cite": [
            "43 L. Ed. 2d 570",
            "95 S. Ct. 1215",
            "420 U.S. 714",
            "1975 U.S. LEXIS 5"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108272 OR 9424454 OR 9424455) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjU3OTg0MDAwMDAwJnM9MjQyMTg2NCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108272+OR+9424454+OR+9424455%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108272 OR 9424454 OR 9424455)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02ODYmcz0yMzU1MzQ0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108272+OR+9424454+OR+9424455%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108272 OR 9424454 OR 9424455)",
        "reviewed": 33,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 33,
        "triage_read": 0,
        "triage_snippet_classified": 33
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108272 OR 9424454 OR 9424455)",
    "indexed_citing_opinions": 1928,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108272,
        "count": 1795,
        "count_source": "search"
      },
      {
        "opinion_id": 9424454,
        "count": 185,
        "count_source": "search"
      },
      {
        "opinion_id": 9424455,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2903,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/harris-v-new-york.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3MDg0NTgmcz05NDgzMTAzJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108272+OR+9424454+OR+9424455%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108272,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 106699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 107265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 107651,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 108002,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 260072,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 277194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 279491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 280065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 282229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 282758,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1173777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1246844,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1290054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1433274,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1492401,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1628518,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1750859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1774823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1779353,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1885369,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1960473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 2017386,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 2029356,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 2611284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 2612058,
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
    "date_created": "2026-07-05T06:21:45Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:22:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:22:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T06:27:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:22:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Harris v. New York

```
<div>
<center><b><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U.S. 222</a></span> (1971)</b></center>
<center><h1>HARRIS<br>
v.<br>
NEW YORK.</h1></center>
<center>No. 206.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 17, 1970</center>
<center>Decided February 24, 1971</center>
CERTIORARI TO THE COURT OF APPEALS OF NEW YORK.
<p><i>Joel Martin Aurnou</i> argued the cause and filed a brief for petitioner.</p>
<p><i>James J. Duggan</i> argued the cause for respondent. With him on the brief was <i>Carl A. Vergari.</i></p>
<p><i>Sybil H. Landau</i> argued the cause for the District Attorney of New York County as <i>amicus curiae</i> urging affirmance. With her on the brief were <i>Frank S. Hogan, pro se,</i> and <i>Michael R. Juviler.</i></p>
<p>MR. CHIEF JUSTICE BURGER delivered the opinion of the Court.</p>
<p>We granted the writ in this case to consider petitioner's claim that a statement made by him to police under circumstances rendering it inadmissible to establish the prosecution's case in chief under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), may not be used to impeach his credibility.</p>
<p>The State of New York charged petitioner in a two-count indictment with twice selling heroin to an undercover <span class="star-pagination">*223</span> police officer. At a subsequent jury trial the officer was the State's chief witness, and he testified as to details of the two sales. A second officer verified collateral details of the sales, and a third offered testimony about the chemical analysis of the heroin.</p>
<p>Petitioner took the stand in his own defense. He admitted knowing the undercover police officer but denied a sale on January 4, 1966. He admitted making a sale of contents of a glassine bag to the officer on January 6 but claimed it was baking powder and part of a scheme to defraud the purchaser.</p>
<p>On cross-examination petitioner was asked seriatim whether he had made specified statements to the police immediately following his arrest on January 7statements that partially contradicted petitioner's direct testimony at trial. In response to the cross-examination, petitioner testified that he could not remember virtually any of the questions or answers recited by the prosecutor. At the request of petitioner's counsel the written statement from which the prosecutor had read questions and answers in his impeaching process was placed in the record for possible use on appeal; the statement was not shown to the jury.</p>
<p>The trial judge instructed the jury that the statements attributed to petitioner by the prosecution could be considered only in passing on petitioner's credibility and not as evidence of guilt. In closing summations both counsel argued the substance of the impeaching statements. The jury then found petitioner guilty on the second count of the indictment.<sup>[1]</sup> The New York Court of Appeals affirmed in a <i>per curiam</i> opinion, 25 N. Y. 2d 175, <span class="citation" data-id="5525131"><a href="/opinion/5677292/people-v-harris/" aria-description="Citation for case: People v. Harris">250 N. E. 2d 349</a></span> (1969).</p>
<p>At trial the prosecution made no effort in its case in chief to use the statements allegedly made by petitioner, <span class="star-pagination">*224</span> conceding that they were inadmissible under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). The transcript of the interrogation used in the impeachment, but not given to the jury, shows that no warning of a right to appointed counsel was given before questions were put to petitioner when he was taken into custody. Petitioner makes no claim that the statements made to the police were coerced or involuntary.</p>
<p>Some comments in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion can indeed be read as indicating a bar to use of an uncounseled statement for any purpose, but discussion of that issue was not at all necessary to the Court's holding and cannot be regarded as controlling. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> barred the prosecution from making its case with statements of an accused made while in custody prior to having or effectively waiving counsel. It does not follow from <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> that evidence inadmissible against an accused in the prosecution's case in chief is barred for all purposes, provided of course that the trustworthiness of the evidence satisfies legal standards.</p>
<p>In <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span> (1954), the Court permitted physical evidence, inadmissible in the case in chief, to be used for impeachment purposes.</p>
<blockquote>"It is one thing to say that the Government cannot make an affirmative use of evidence unlawfully obtained. It is quite another to say that the defendant can turn the illegal method by which evidence in the Government's possession was obtained to his own advantage, and provide himself with a shield against contradiction of his untruths. Such an extension of the <i>Weeks</i> doctrine would be a perversion of the Fourth Amendment.</blockquote>
<blockquote>"[T]here is hardly justification for letting the defendant affirmatively resort to perjurious testimony in reliance on the Government's disability to challenge his credibility." <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/#65" aria-description="Citation for case: Walder v. United States">347 U. S., at 65</a></span>.</blockquote>
<p><span class="star-pagination">*225</span> It is true that Walder was impeached as to collateral matters included in his direct examination, whereas petitioner here was impeached as to testimony bearing more directly on the crimes charged. We are not persuaded that there is a difference in principle that warrants a result different from that reached by the Court in <i><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span>.</i> Petitioner's testimony in his own behalf concerning the events of January 7 contrasted sharply with what he told the police shortly after his arrest. The impeachment process here undoubtedly provided valuable aid to the jury in assessing petitioner's credibility, and the benefits of this process should not be lost, in our view, because of the speculative possibility that impermissible police conduct will be encouraged thereby. Assuming that the exclusionary rule has a deterrent effect on proscribed police conduct, sufficient deterrence flows when the evidence in question is made unavailable to the prosecution in its case in chief.</p>
<p>Every criminal defendant is privileged to testify in his own defense, or to refuse to do so. But that privilege cannot be construed to include the right to commit perjury. See <i>United States</i> v. <i>Knox,</i> <span class="citation" data-id="9841978"><a href="/opinion/108002/united-states-v-knox/" aria-description="Citation for case: United States v. Knox">396 U. S. 77</a></span> (1969); cf. <i>Dennis</i> v. <i>United States,</i> <span class="citation" data-id="9423265"><a href="/opinion/107265/dennis-v-united-states/" aria-description="Citation for case: Dennis v. United States">384 U. S. 855</a></span> (1966). Having voluntarily taken the stand, petitioner was under an obligation to speak truthfully and accurately, and the prosecution here did no more than utilize the traditional truth-testing devices of the adversary process.<sup>[2]</sup> Had <span class="star-pagination">*226</span> inconsistent statements been made by the accused to some third person, it could hardly be contended that the conflict could not be laid before the jury by way of cross-examination and impeachment.</p>
<p>The shield provided by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> cannot be perverted into a license to use perjury by way of a defense, free from the risk of confrontation with prior inconsistent utterances. We hold, therefore, that petitioner's credibility was appropriately impeached by use of his earlier conflicting statements.</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE BLACK dissents.</p>
<p>MR. JUSTICE BRENNAN, with whom MR. JUSTICE DOUGLAS and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>It is conceded that the question-and-answer statement used to impeach petitioner's direct testimony was, under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), constitutionally inadmissible as part of the State's direct case against petitioner. I think that the Constitution also denied the State the use of the statement on cross-examination to impeach the credibility of petitioner's testimony given in his own defense. The decision in <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span> (1954), is not, as the Court today holds, dispositive to the contrary. Rather, that case supports my conclusion.</p>
<p>The State's case against Harris depended upon the jury's belief of the testimony of the undercover agent that petitioner "sold" the officer heroin on January 4 and again on January 6. Petitioner took the stand and flatly denied having sold anything to the officer on January 4. He countered the officer's testimony as to the January 6 sale with testimony that he had sold the officer two glassine bags containing what appeared to be heroin, but that actually the bags contained only baking powder intended to deceive the officer in order to obtain $12. <span class="star-pagination">*227</span> The statement contradicted petitioner's direct testimony as to the events of both days. The statement's version of the events on January 4 was that the officer had used petitioner as a middleman to buy some heroin from a third person with money furnished by the officer. The version of the events on January 6 was that petitioner had again acted for the officer in buying two bags of heroin from a third person for which petitioner received $12 and a part of the heroin. Thus, it is clear that the statement was used to impeach petitioner's direct testimony not on collateral matters but on matters directly related to the crimes for which he was on trial.<sup>[1]</sup></p>
<p><i>Walder</i> v. <i>United States</i> was not a case where tainted evidence was used to impeach an accused's direct testimony on matters directly related to the case against him. In <i><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span></i> the evidence was used to impeach the accused's testimony on matters <i>collateral</i> to the crime charged. Walder had been indicted in 1950 for purchasing and possessing heroin. When his motion to suppress use of the narcotics as illegally seized was granted, the Government dismissed the prosecution. Two years later Walder was indicted for another narcotics violation completely unrelated to the 1950 one. Testifying in his own defense, he said on direct examination that he had never in his life possessed narcotics. On cross-examination he denied that law enforcement officers had seized narcotics from his home two years earlier. The Government was then permitted to introduce the testimony of one of the officers involved in the 1950 seizure, that when he had raided Walder's home at that time he had seized narcotics there. <span class="star-pagination">*228</span> The Court held that on facts where "the defendant went beyond a mere denial of complicity in the crimes of which he was charged and made the sweeping claim that he had never dealt in or possessed any narcotics," <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/#65" aria-description="Citation for case: Walder v. United States">347 U. S., at 65</a></span>, the exclusionary rule of <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), would not extend to bar the Government from rebutting this testimony with evidence, although tainted, that petitioner had in fact possessed narcotics two years before. The Court was careful, however, to distinguish the situation of an accused whose testimony, as in the instant case, was a "denial of complicity in the crimes of which he was charged," that is, where illegally obtained evidence was used to impeach the accused's direct testimony on matters directly related to the case against him. As to that situation, the Court said:</p>
<blockquote>"Of course, the Constitution guarantees a defendant the fullest opportunity to meet the accusation against him. He must be free to deny all the elements of the case against him without thereby giving leave to the Government to introduce by way of rebuttal evidence illegally secured by it, and therefore not available for its case in chief." <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/#65" aria-description="Citation for case: Walder v. United States">347 U. S., at 65</a></span>.</blockquote>
<p>From this recital of facts it is clear that the evidence used for impeachment in <i><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span></i> was related to the earlier 1950 prosecution and had no direct bearing on "the elements of the case" being tried in 1952. The evidence tended solely to impeach the credibility of the defendant's direct testimony that he had never in his life possessed heroin. But that evidence was completely unrelated to the indictment on trial and did not in any way interfere with his freedom to deny all elements of that case against him. In contrast, here, the evidence used for impeachment, a statement concerning the details of the very sales alleged in the indictment, was directly related to the case against petitioner.</p>
<p><span class="star-pagination">*229</span> While <i><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span></i> did not identify the constitutional specifics that guarantee "a defendant the fullest opportunity to meet the accusation against him . . . [and permit him to] be free to deny all the elements of the case against him," in my view <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), identified the Fifth Amendment's privilege against self-incrimination as one of those specifics.<sup>[2]</sup><span class="star-pagination">*230</span> That privilege has been extended against the States. <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964). It is fulfilled only when an accused is guaranteed the right "to remain silent unless he chooses to speak in the <i>unfettered</i> exercise of his own will," <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#8" aria-description="Citation for case: Malloy v. Hogan"><i>id.,</i> at 8</a></span> (emphasis added). The choice of whether to testify in one's own defense must therefore be "unfettered," since that choice is an exercise of the constitutional privilege, <i>Griffin</i> v. <i>California,</i> <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">380 U. S. 609</a></span> (1965). <i><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">Griffin</a></span></i> held that comment by the prosecution upon the accused's failure to take the stand or a court instruction that such silence is evidence of guilt is impermissible because it "fetters" that choice"[i]t cuts down on the privilege by making its assertion costly." <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/#614" aria-description="Citation for case: Griffin v. California"><i>Id.,</i> at 614</a></span>. For precisely the same reason the constitutional guarantee forbids the prosecution to use a tainted statement to impeach the accused who takes the stand: The prosecution's use of the tainted statement "cuts down on the privilege by making its assertion costly." <i><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">Ibid.</a></span></i> Thus, the accused is denied an "unfettered" choice when the decision whether to take the stand is burdened by the risk that an illegally obtained prior statement may be introduced to impeach his direct testimony denying complicity in the crime charged against him.<sup>[3]</sup> We settled this proposition in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> where we said:</p>
<blockquote>"The privilege against self-incrimination protects the individual from being compelled to incriminate himself in <i>any</i> manner . . . . [S]tatements merely intended to be exculpatory by the defendant are often <i>used to impeach his testimony at trial</i> . . . . <i>These statements are incriminating in any meaningful sense of the word and may not be used without the full warnings and effective waiver required for</i> <span class="star-pagination">*231</span> <i>any other statement.</i>" 384 U. S., at 476-477 (emphasis added).</blockquote>
<p>This language completely disposes of any distinction between statements used on direct as opposed to cross-examination.<sup>[4]</sup> "An incriminating statement is as incriminating when used to impeach credibility as it is when used as direct proof of guilt and no constitutional distinction can legitimately be drawn." <i>People</i> v. <i>Kulis,</i> 18 N. Y. 2d 318, 324, <span class="citation" data-id="5522978"><a href="/opinion/5675346/people-v-kulis/#543" aria-description="Citation for case: People v. Kulis">221 N. E. 2d 541, 543</a></span> (1966) (dissenting opinion).</p>
<p>The objective of deterring improper police conduct is only part of the larger objective of safeguarding the integrity of our adversary system. The "essential mainstay" of that system, <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#460" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 460</a></span>, is the privilege against self-incrimination, which for <span class="star-pagination">*232</span> that reason has occupied a central place in our jurisprudence since before the Nation's birth. Moreover, "we may view the historical development of the privilege as one which groped for the proper scope of governmental power over the citizen. . . . All these policies point to one overriding thought: the constitutional foundation underlying the privilege is the respect a government . . . must accord to the dignity and integrity of its citizens." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> These values are plainly jeopardized if an exception against admission of tainted statements is made for those used for impeachment purposes. Moreover, it is monstrous that courts should aid or abet the law-breaking police officer. It is abiding truth that "[n]othing can destroy a government more quickly than its failure to observe its own laws, or worse, its disregard of the charter of its own existence." <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#659" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 659</a></span> (1961). Thus, even to the extent that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was aimed at deterring police practices in disregard of the Constitution, I fear that today's holding will seriously undermine the achievement of that objective. The Court today tells the police that they may freely interrogate an accused incommunicado and without counsel and know that although any statement they obtain in violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> cannot be used on the State's direct case, it may be introduced if the defendant has the temerity to testify in his own defense. This goes far toward undoing much of the progress made in conforming police methods to the Constitution. I dissent.</p>
<h2>NOTES</h2>
<p>[1]  No agreement was reached as to the first count. That count was later dropped by the State.</p>
<p>[2]  If, for example, an accused confessed fully to a homicide and led the police to the body of the victim under circumstances making his confession inadmissible, the petitioner would have us allow that accused to take the stand and blandly deny every fact disclosed to the police or discovered as a "fruit" of his confession, free from confrontation with his prior statements and acts. The voluntariness of the confession would, on this thesis, be totally irrelevant. We reject such an extravagant extension of the Constitution. Compare <i>Killough</i> v. <i>United States,</i> 114 U. S. App. D. C. 305, <span class="citation" data-id="9449118"><a href="/opinion/260072/james-w-killough-v-united-states/" aria-description="Citation for case: James W. Killough v. United States">315 F. 2d 241</a></span> (1962).</p>
<p>[1]  The trial transcript shows that petitioner testified that he remembered making a statement on January 7; that he remembered a few of the questions and answers; but that he did not "remember giving too many answers." When asked about his bad memory, petitioner, who had testified that he was a heroin addict, stated that "my joints was down and I needed drugs."</p>
<p>[2]  Three of the five judges of the Appellate Division in this case agreed that the State's use of petitioner's illegally obtained statement was an error of constitutional dimension. <i>People</i> v. <i>Harris,</i> 31 App. Div. 2d 828, 298 N. Y. S. 2d 245 (1969). However, one of the three held that the error did not play a meaningful role in the case and was therefore harmless under our decision in <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967). He therefore joined in affirming the conviction with the two judges who were of the view that there was no constitutional question involved. 31 App. Div. 2d, at 830, 298 N. Y. S. 2d, at 249. I disagree that the error was harmless and subscribe to the reasoning of the dissenting judges, <i>id.,</i> at 831-832, 298 N. Y. S. 2d at 250:
</p>
<p>"Under the circumstances outlined above, I cannot agree that this error of constitutional dimension was `harmless beyond a reasonable doubt' (<i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#24" aria-description="Citation for case: Chapman v. California">386 U. S. 18, 24</a></span>). An error is not harmless if `there is a reasonable possibility that the evidence complained of might have contributed to the conviction' (<i>Fahy</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422676"><a href="/opinion/106699/fahy-v-connecticut/#86" aria-description="Citation for case: Fahy v. Connecticut">375 U. S. 85, 86-87</a></span>). The burden of showing that a constitutional error is harmless rests with the People who, in this case, have not even attempted to assume that demonstration (<i>Chapman</i> v. <i>California, supra</i>). Surely it cannot be said with any certainty that the improper use of defendant's statement did not tip the scales against him, especially when his conviction rests on the testimony of the same undercover agent whose testimony was apparently less than convincing on the January 4 charge (cf. <i>Anderson</i> v. <i>Nelson,</i> <span class="citation" data-id="107651"><a href="/opinion/107651/anderson-v-nelson/#525" aria-description="Citation for case: Anderson v. Nelson">390 U. S. 523, 525</a></span>). On the contrary, it is difficult to see how defendant could not have been damaged severely by use of the inconsistent statement in a case which, in the final analysis, pitted his word against the officer's. The judgment should be reversed and a new trial granted."</p>
<p>The Court of Appeals affirmed <i>per curiam</i> on the authority of its earlier opinion in <i>People</i> v. <i>Kulis,</i> 18 N. Y. 2d 318, <span class="citation" data-id="5522978"><a href="/opinion/5675346/people-v-kulis/" aria-description="Citation for case: People v. Kulis">221 N. E. 2d 541</a></span> (1966). Chief Judge Fuld and Judge Keating dissented in <i><span class="citation" data-id="5522978"><a href="/opinion/5675346/people-v-kulis/" aria-description="Citation for case: People v. Kulis">Kulis</a></span></i> on the ground that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> precluded use of the statement for impeachment purposes, 18 N. Y. 2d, at 323, <span class="citation" data-id="5522978"><a href="/opinion/5675346/people-v-kulis/#542" aria-description="Citation for case: People v. Kulis">221 N. E. 2d, at 542</a></span>.</p>
<p>[3]  It is therefore unnecessary for me to consider petitioner's argument that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> has overruled the narrow exception of <i><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span></i> admitting impeaching evidence on collateral matters.</p>
<p>[4]  Six federal courts of appeals and appellate courts of 14 States have reached the same result. <i>United States</i> v. <i>Fox,</i> <span class="citation" data-id="9454030"><a href="/opinion/282229/united-states-v-jack-solomon-fox-and-samuel-norber/" aria-description="Citation for case: United States v. Jack Solomon Fox and Samuel Norber">403 F. 2d 97</a></span> (CA2 1968); <i>United States</i> v. <i>Pinto,</i> <span class="citation" data-id="280065"><a href="/opinion/280065/united-states-of-america-ex-rel-james-edward-hill-v-warren-pinto/" aria-description="Citation for case: United States of America Ex Rel. James Edward Hill v....">394 F. 2d 470</a></span> (CA3 1968); <i>Breedlove</i> v. <i>Beto,</i> <span class="citation" data-id="282758"><a href="/opinion/282758/freddie-breedlove-v-dr-george-j-beto-director-texas-department-of/" aria-description="Citation for case: Freddie Breedlove v. Dr. George J. Beto, Director, Texas...">404 F. 2d 1019</a></span> (CA5 1968); <i>Groshart</i> v. <i>United States,</i> <span class="citation" data-id="9453474"><a href="/opinion/279491/jerry-warren-groshart-v-united-states/" aria-description="Citation for case: Jerry Warren Groshart v. United States">392 F. 2d 172</a></span> (CA9 1968); <i>Blair</i> v. <i>United States,</i> 130 U. S. App. D. C. 322, <span class="citation multiple-matches"><a href="/c/F.%202d/401/387/">401 F. 2d 387</a></span> (1968); <i>Wheeler</i> v. <i>United States,</i> <span class="citation" data-id="277194"><a href="/opinion/277194/billy-wayne-wheeler-and-johnnie-green-jr-v-united-states/" aria-description="Citation for case: Billy Wayne Wheeler and Johnnie Green, Jr. v. United States">382 F. 2d 998</a></span> (CA10 1967); <i>People</i> v. <i>Barry,</i> <span class="citation" data-id="2191430"><a href="/opinion/2191430/people-v-barry/" aria-description="Citation for case: People v. Barry">237 Cal. App. 2d 154</a></span>, <span class="citation" data-id="2191430"><a href="/opinion/2191430/people-v-barry/" aria-description="Citation for case: People v. Barry">46 Cal. Rptr. 727</a></span> (1965), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./386/1024/">386 U. S. 1024</a></span> (1967); <i>Velarde</i> v. <i>People,</i> <span class="citation" data-id="1173777"><a href="/opinion/1173777/velarde-v-people/" aria-description="Citation for case: Velarde v. People">171 Colo. 261</a></span>, <span class="citation" data-id="1173777"><a href="/opinion/1173777/velarde-v-people/" aria-description="Citation for case: Velarde v. People">466 P. 2d 919</a></span> (1970); <i>State</i> v. <i>Galasso,</i> <span class="citation" data-id="1628518"><a href="/opinion/1628518/state-v-galasso/" aria-description="Citation for case: State v. Galasso">217 So. 2d 326</a></span> (Fla. 1968); <i>People</i> v. <i>Luna,</i> <span class="citation" data-id="2029356"><a href="/opinion/2029356/the-people-v-luna/" aria-description="Citation for case: The PEOPLE v. Luna">37 Ill. 2d 299</a></span>, <span class="citation" data-id="2029356"><a href="/opinion/2029356/the-people-v-luna/" aria-description="Citation for case: The PEOPLE v. Luna">226 N. E. 2d 586</a></span> (1967); <i>Franklin</i> v. <i>State,</i> <span class="citation" data-id="1492401"><a href="/opinion/1492401/franklin-v-state/" aria-description="Citation for case: Franklin v. State">6 Md. App. 572</a></span>, <span class="citation" data-id="1492401"><a href="/opinion/1492401/franklin-v-state/" aria-description="Citation for case: Franklin v. State">252 A. 2d 487</a></span> (1969); <i>People</i> v. <i>Wilson,</i> <span class="citation" data-id="2017386"><a href="/opinion/2017386/people-v-wilson/" aria-description="Citation for case: People v. Wilson">20 Mich. App. 410</a></span>, <span class="citation" data-id="2017386"><a href="/opinion/2017386/people-v-wilson/" aria-description="Citation for case: People v. Wilson">174 N. W. 2d 79</a></span> (1969); <i>State</i> v. <i>Turnbow,</i> 67 N. M. 241, <span class="citation" data-id="2611284"><a href="/opinion/2611284/state-v-turnbow/" aria-description="Citation for case: State v. Turnbow">354 P. 2d 533</a></span> (1960); <i>State</i> v. <i>Catrett,</i> <span class="citation" data-id="6701707"><a href="/opinion/6814852/state-v-riera/" aria-description="Citation for case: State v. Riera">276 N. C. 86</a></span>, <span class="citation" data-id="1290054"><a href="/opinion/1290054/state-v-catrett/" aria-description="Citation for case: State v. Catrett">171 S. E. 2d 398</a></span> (1970); <i>State</i> v. <i>Brewton,</i> <span class="citation" data-id="9628725"><a href="/opinion/1433274/state-v-brewton/" aria-description="Citation for case: State v. Brewton">247 Ore. 241</a></span>, <span class="citation" data-id="9628725"><a href="/opinion/1433274/state-v-brewton/" aria-description="Citation for case: State v. Brewton">422 P. 2d 581</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./387/943/">387 U. S. 943</a></span> (1967); <i>Commonwealth</i> v. <i>Padgett,</i> <span class="citation" data-id="1885369"><a href="/opinion/1885369/commonwealth-v-padgett/" aria-description="Citation for case: Commonwealth v. Padgett">428 Pa. 229</a></span>, <span class="citation" data-id="1885369"><a href="/opinion/1885369/commonwealth-v-padgett/" aria-description="Citation for case: Commonwealth v. Padgett">237 A. 2d 209</a></span> (1968); <i>Spann</i> v. <i>State,</i> <span class="citation" data-id="1779353"><a href="/opinion/1779353/spann-v-state/" aria-description="Citation for case: Spann v. State">448 S. W. 2d 128</a></span> (Tex. Cr. App. 1969); <i>Cardwell</i> v. <i>Commonwealth,</i> <span class="citation" data-id="9845193"><a href="/opinion/1246844/cardwell-v-commonwealth/" aria-description="Citation for case: Cardwell v. Commonwealth">209 Va. 412</a></span>, <span class="citation" data-id="9845193"><a href="/opinion/1246844/cardwell-v-commonwealth/" aria-description="Citation for case: Cardwell v. Commonwealth">164 S. E. 2d 699</a></span> (1968); <i>Gaertner</i> v. <i>State,</i> <span class="citation" data-id="1750859"><a href="/opinion/1750859/gaertner-v-state/" aria-description="Citation for case: Gaertner v. State">35 Wis. 2d 159</a></span>, <span class="citation" data-id="1750859"><a href="/opinion/1750859/gaertner-v-state/" aria-description="Citation for case: Gaertner v. State">150 N. W. 2d 370</a></span> (1967); see also <i>Kelly</i> v. <i>King,</i> <span class="citation" data-id="1774823"><a href="/opinion/1774823/kelly-v-king/" aria-description="Citation for case: Kelly v. King">196 So. 2d 525</a></span> (Miss. 1967). Only three state appellate courts have agreed with New York. <i>State</i> v. <i>Kimbrough,</i> 109 N. J. Super. 57, <span class="citation" data-id="1960473"><a href="/opinion/1960473/state-v-kimbrough/" aria-description="Citation for case: State v. Kimbrough">262 A. 2d 232</a></span> (1970); <i>State</i> v. <i>Butler,</i> <span class="citation" data-id="6754227"><a href="/opinion/6864451/state-v-butler/" aria-description="Citation for case: State v. Butler">19 Ohio St. 2d 55</a></span>, <span class="citation" data-id="6754227"><a href="/opinion/6864451/state-v-butler/" aria-description="Citation for case: State v. Butler">249 N. E. 2d 818</a></span> (1969); <i>State</i> v. <i>Grant,</i> <span class="citation" data-id="2612058"><a href="/opinion/2612058/state-v-grant/" aria-description="Citation for case: State v. Grant">77 Wash. 2d 47</a></span>, <span class="citation" data-id="2612058"><a href="/opinion/2612058/state-v-grant/" aria-description="Citation for case: State v. Grant">459 P. 2d 639</a></span> (1969).</p>

</div>
```

---

## GROUP: content/cases/Harris v. United States (1968).md  (`case`, 6 assertions)

### content_page

```
---
title: "Harris v. United States (1968)"
type: case
citation: "390 U.S. 234 (1968)"
parallel_cite: "88 S. Ct. 992; 19 L. Ed. 2d 1067"
neutral_cite: 1968 U.S. LEXIS 2283
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1968
date_decided: 1968-03-05
docket: 92
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1968-03-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "Harris v. United States (1968)"
  varies_by_point: false
  scope_note: "Per curiam. The plain-view-seizure formulation remains settled law; it was later structured (no-inadvertence requirement) by Horton v. California. Distinct case from the 1947 Harris v. United States (search incident to arrest), which Chimel v. California overruled."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107625/harris-v-united-states/"
  cluster_id: 107625
  opinion_id: 107625
  identity_checked: true
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Automobile Exception]]"
    role: "Related (cross-doctrine)"
related: ["[[Coolidge v. New Hampshire]]", "[[Horton v. California]]", "[[Texas v. Brown]]", "[[South Dakota v. Opperman]]", "[[Cooper v. California]]"]
aliases: ["Harris v. United States"]
tags: ["case", "fourth-amendment", "plain-view", "impound", "protective-measure", "automobile"]
holding: "Objects falling in the plain view of an officer who has a right to be in the position to have that view are subject to seizure and admissible; a protective measure taken to secure a lawfully impounded car is not a search."
lake:
  record_id: "Harris v. United States (1968)"
  status: verified
  projected_at: 2026-07-09
---

# Harris v. United States (1968)

*390 U.S. 234 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

> **Identity / disambiguation:** this is the 1968 [[Common Legal Terms#per-curiam|per curiam]] (plain-view seizure from a lawfully impounded car). It is a **different case** from *Harris v. United States*, 331 U.S. 145 (1947) (a sweeping search-incident-to-arrest holding **overruled** by [[Chimel v. California]]), and from *[[United States v. Harris (1971)|United States v. Harris]]*, 401 U.S. 1027 (1971) (reversed party). The year-suffix filename and bare-name `alias` keep the links from colliding.

## Background
Harris's car was seen leaving a robbery; it was traced and he was arrested entering it near his home. Police impounded the car as evidence and towed it to the precinct lot. Because it had begun to rain and the windows were open and a door unlocked, the arresting officer — following a department regulation to secure impounded vehicles — went to the lot to tag the car, roll up the windows, and lock the doors. Opening the passenger door to secure that window, he saw the robbery victim's automobile registration card lying face up on the door sill in plain view, and later seized it. The card was admitted at trial.

## Issue
Whether the officer discovered the registration card by means of an illegal search when he saw it in plain view while securing a lawfully impounded car.

## Rule
No. A measure taken to protect an impounded car is not a search: "the discovery of the card was not the result of a search of the car, but of a measure taken to protect the car while it was in police custody. Nothing in the Fourth Amendment requires the police to obtain a warrant in these narrow circumstances." — 390 U.S. at 236. ^pin-236

And plain-view objects are seizable: "It has long been settled that objects falling in the plain view of an officer who has a right to be in the position to have that view are subject to seizure and may be introduced in evidence." — [*Id.*](https://www.courtlistener.com/opinion/107625/harris-v-united-states/#:~:text=It%20has%20long%20been%20settled) ^pin-236a

## Application
The officer was lawfully securing a car properly impounded as evidence; the precise findings below were that the card was discovered while protecting the car, not while searching it. Once the door was lawfully opened to secure the window, the victim's registration card was "plainly visible," so it was subject to seizure. The Court expressly noted it was **not** deciding the admissibility of evidence found pursuant to the inventory regulation itself — only that this protective discovery was lawful.

## Conclusion
Affirmed (per curiam). The card was lawfully seen and seized in plain view during a lawful protective measure; there was no illegal search.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- The plain-view-seizure articulation is settled and was later given its structure by [[Coolidge v. New Hampshire]] and [[Horton v. California]] (which dropped the inadvertence requirement). The inventory-search question *Harris* reserved was answered separately in [[South Dakota v. Opperman]].

## Appears on
- [[Plain View Doctrine]] — *Key — Progeny / Refinement*
- [[Automobile Exception]] — *Related (cross-doctrine)*

## Sources
- *Harris v. United States*, 390 U.S. 234 (1968) — https://www.courtlistener.com/opinion/107625/harris-v-united-states/ — pinpoint: 236.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "706ca22a3173714c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "390 U.S. 234 (1968)", "court": "U.S. Supreme Court", "neutral_cite": "1968 U.S. LEXIS 2283", "official_citation_present": true, "parallel_cite": "88 S. Ct. 992; 19 L. Ed. 2d 1067", "title": "Harris v. United States (1968)", "year": "1968"}}
{"assertion_id": "7eecba8fe177e6d0", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Objects falling in the plain view of an officer who has a right to be in the position to have that view are subject to seizure and admissible; a protective measure taken to secure a lawfully impounded car is not a search.", "title": "Harris v. United States (1968)"}}
{"assertion_id": "da23d483562bf633", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Related (cross-doctrine)", "title": "Harris v. United States (1968)"}}
{"assertion_id": "ea97f4f25a27c89e", "dimension": "support", "kind": "home_role", "locator": {"home": "Plain View Doctrine"}, "payload": {"home": "Plain View Doctrine", "role": "Key — Progeny / Refinement", "title": "Harris v. United States (1968)"}}
{"assertion_id": "68ed8213547fd5bb", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1968-03-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Harris v. United States (1968)", "field_i_validity": "good_law", "scope_note": "Per curiam. The plain-view-seizure formulation remains settled law; it was later structured (no-inadvertence requirement) by Horton v. California. Distinct case from the 1947 Harris v. United States (search incident to arrest), which Chimel v. California overruled.", "title": "Harris v. United States (1968)", "varies_by_point": "false"}}
{"assertion_id": "dade49d112209944", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Harris v. United States (1968)"}}
```

### lake record — Harris v. United States (1968)

```json
{
  "schema_version": "s2.v1",
  "record_id": "Harris v. United States (1968)",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Harris v. United States",
    "case_name_short": "Harris",
    "case_name_full": "Harris v. United States",
    "input_case_name": "Harris v. United States (1968)",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-03-05",
    "year": 1968,
    "docket": "92",
    "cluster_id": 107625,
    "lead_opinion_id": 107625,
    "sibling_ids": [
      107625,
      9423622,
      9423623
    ],
    "absolute_url": "/opinion/107625/harris-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 107608,
        "score": 20,
        "case_name": "Haynes v. United States"
      },
      {
        "cluster_id": 107623,
        "score": 20,
        "case_name": "United States v. Habig"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "390 U.S. 234",
      "volume": "390",
      "reporter": "U.S.",
      "page": "234",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 992",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "992",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "19 L. Ed. 2d 1067",
        "volume": "19",
        "reporter": "L. Ed. 2d",
        "page": "1067",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 2283",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "2283",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "390 U.S. 234",
        "volume": "390",
        "reporter": "U.S.",
        "page": "234",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 992",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "992",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "19 L. Ed. 2d 1067",
        "volume": "19",
        "reporter": "L. Ed. 2d",
        "page": "1067",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 2283",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "2283",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "390 U.S. 234",
    "official_selection": {
      "court_class": "scotus",
      "selected": "390 U.S. 234",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-236",
      "page": null,
      "quote": "--- # Harris v. United States (1968) *390 U.S. 234 (1968)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> > **Identity / disambiguation:** this is the 1968 per curiam (plain-view seizure from a lawfully impounded car). It is a **different case** from *Harris v. United States*, 331 U.S. 145 (1947) (a sweeping search-incident-to-arrest holding **overruled** by [[Chimel v. California]]), and from *United States v. Harris*, 401 U.S. 1027 (1971) (reversed party). The year-suffix filename and bare-name `alias` keep the links from colliding. ## Background Harris's car was seen leaving a robbery; it was traced and he was arrested entering it near his home. Police impounded the car as evidence and towed it to the precinct lot. Because it had begun to rain and the windows were open and a door unlocked, the arresting officer \u2014 following a department regulation to secure impounded vehicles \u2014 went to the lot to tag the car, roll up the windows, and lock the doors. Opening the passenger door to secure that window, he saw the robbery victim's automobile registration card lying face up on the door sill in plain view, and later seized it. The card was admitted at trial. ## Issue Whether the officer discovered the registration card by means of an illegal search when he saw it in plain view while securing a lawfully impounded car. ## Rule No. A measure taken to protect an impounded car is not a search:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-236a",
      "page": null,
      "quote": "It has long been settled that objects falling in the plain view of an officer who has a right to be in the position to have that view are subject to seizure and may be introduced in evidence.",
      "star_marker": "236",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 4774,
      "fragment": "#:~:text=It%20has%20long%20been%20settled",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1968-03-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Harris v. United States (1968)",
    "varies_by_point": false,
    "scope_note": "Per curiam. The plain-view-seizure formulation remains settled law; it was later structured (no-inadvertence requirement) by Horton v. California. Distinct case from the 1947 Harris v. United States (search incident to arrest), which Chimel v. California overruled.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Martin v. State",
          "cluster_id": 10740496,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
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
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Florida v. Clarence E. Johnson",
          "cluster_id": 4343883,
          "cite": [
            "208 So. 3d 843",
            "2017 Fla. App. LEXIS 995"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jesus Rodriguez v. State",
          "cluster_id": 2920356,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Lang",
          "cluster_id": 6109,
          "cite": [
            "8 F.3d 268",
            "38 Fed. R. Serv. 579",
            "1993 U.S. App. LEXIS 30076",
            "1993 WL 478488"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. $10,000 in United States Currency",
          "cluster_id": 8946555,
          "cite": [
            "780 F.2d 213",
            "1986 U.S. App. LEXIS 21660"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jerome F. Blakeney",
          "cluster_id": 446901,
          "cite": [
            "753 F.2d 152",
            "243 U.S. App. D.C. 334",
            "1985 U.S. App. LEXIS 27774"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Stewart v. State",
          "cluster_id": 1531281,
          "cite": [
            "681 S.W.2d 774",
            "1984 Tex. App. LEXIS 6422"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Clement Kolodziej",
          "cluster_id": 418003,
          "cite": [
            "706 F.2d 590",
            "1983 U.S. App. LEXIS 27009"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Milan Bagaric, Mile Markich, Ante Ljubas, Vinko Logarusic, Ranko Primorac, and Drago Sudar",
          "cluster_id": 417774,
          "cite": [
            "706 F.2d 42",
            "1983 U.S. App. LEXIS 28806"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dees",
          "cluster_id": 1518524,
          "cite": [
            "639 S.W.2d 149",
            "1982 Mo. App. LEXIS 3679"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sims",
          "cluster_id": 1518614,
          "cite": [
            "639 S.W.2d 105",
            "1982 Mo. App. LEXIS 3686"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
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
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Opperman",
          "cluster_id": 109537,
          "cite": [
            "49 L. Ed. 2d 1000",
            "96 S. Ct. 3092",
            "428 U.S. 364",
            "1976 U.S. LEXIS 15"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Brown",
          "cluster_id": 110901,
          "cite": [
            "75 L. Ed. 2d 502",
            "103 S. Ct. 1535",
            "460 U.S. 730",
            "1983 U.S. LEXIS 143",
            "51 U.S.L.W. 4361"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Horton v. California",
          "cluster_id": 112448,
          "cite": [
            "110 L. Ed. 2d 112",
            "110 S. Ct. 2301",
            "496 U.S. 128",
            "1990 U.S. LEXIS 2937"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cady v. Dombrowski",
          "cluster_id": 108850,
          "cite": [
            "37 L. Ed. 2d 706",
            "93 S. Ct. 2523",
            "413 U.S. 433",
            "1973 U.S. LEXIS 48"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Bertine",
          "cluster_id": 111788,
          "cite": [
            "93 L. Ed. 2d 739",
            "107 S. Ct. 738",
            "479 U.S. 367",
            "1987 U.S. LEXIS 286",
            "55 U.S.L.W. 4105"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arkansas v. Sanders",
          "cluster_id": 110119,
          "cite": [
            "61 L. Ed. 2d 235",
            "99 S. Ct. 2586",
            "442 U.S. 753",
            "1979 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Frazier v. Cupp",
          "cluster_id": 107913,
          "cite": [
            "22 L. Ed. 2d 684",
            "89 S. Ct. 1420",
            "394 U.S. 731",
            "1969 U.S. LEXIS 1870"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cardwell v. Lewis",
          "cluster_id": 109069,
          "cite": [
            "41 L. Ed. 2d 325",
            "94 S. Ct. 2464",
            "417 U.S. 583",
            "1974 U.S. LEXIS 75",
            "69 Ohio Op. 2d 69"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stoker v. State",
          "cluster_id": 2464243,
          "cite": [
            "788 S.W.2d 1",
            "1989 Tex. Crim. App. LEXIS 167",
            "1989 WL 107536"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robbins v. California",
          "cluster_id": 110558,
          "cite": [
            "69 L. Ed. 2d 744",
            "101 S. Ct. 2841",
            "453 U.S. 420",
            "1981 U.S. LEXIS 132"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harold B. Dorman v. United States",
          "cluster_id": 293653,
          "cite": [
            "435 F.2d 385",
            "140 U.S. App. D.C. 313",
            "1970 U.S. App. LEXIS 9785"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sharon Olabisiomotosho v. City of Houston City of Houston P. J. Bartlett K. L. Richards Rene Bertrand",
          "cluster_id": 765388,
          "cite": [
            "185 F.3d 521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carmine Tramunti",
          "cluster_id": 326798,
          "cite": [
            "513 F.2d 1087"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Reisman",
          "cluster_id": 5678745,
          "cite": [
            "29 N.Y.2d 278",
            "277 N.E.2d 396",
            "327 N.Y.S.2d 342",
            "1971 N.Y. LEXIS 943"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Superior Court",
          "cluster_id": 1435013,
          "cite": [
            "478 P.2d 449",
            "3 Cal. 3d 807",
            "91 Cal. Rptr. 729",
            "45 A.L.R. 3d 559",
            "1970 Cal. LEXIS 249"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. State",
          "cluster_id": 1914341,
          "cite": [
            "419 So. 2d 563"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Bowden",
          "cluster_id": 2123427,
          "cite": [
            "399 N.E.2d 482",
            "379 Mass. 472",
            "1980 Mass. LEXIS 944"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Silva",
          "cluster_id": 2120427,
          "cite": [
            "318 N.E.2d 895",
            "366 Mass. 402",
            "1974 Mass. LEXIS 732"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Servis v. Commonwealth",
          "cluster_id": 1349258,
          "cite": [
            "371 S.E.2d 156",
            "6 Va. App. 507",
            "5 Va. Law Rep. 37",
            "1988 Va. App. LEXIS 66"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Seagull",
          "cluster_id": 1157235,
          "cite": [
            "632 P.2d 44",
            "95 Wash. 2d 898",
            "1981 Wash. LEXIS 1130"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Frank Diecidue, Larry Neil Miller, Frank Boni, Jr., A/K/A \"Mustache Frankie,\" Manuel Gispert, Anthony Antone, and Homer Rex Davis",
          "cluster_id": 368882,
          "cite": [
            "603 F.2d 535",
            "4 Fed. R. Serv. 1294",
            "1979 U.S. App. LEXIS 11494"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107625 OR 9423622 OR 9423623) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zODU2ODk2MDAwMDAmcz0xMTg3MTY3JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107625+OR+9423622+OR+9423623%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107625 OR 9423622 OR 9423623)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjYmcz0xMzA3NjAyJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107625+OR+9423622+OR+9423623%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107625 OR 9423622 OR 9423623)",
        "reviewed": 10,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 10,
        "triage_read": 2,
        "triage_snippet_classified": 8
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107625 OR 9423622 OR 9423623)",
    "indexed_citing_opinions": 1248,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107625,
        "count": 1158,
        "count_source": "search"
      },
      {
        "opinion_id": 9423622,
        "count": 111,
        "count_source": "search"
      },
      {
        "opinion_id": 9423623,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1768,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/harris-v-united-states-1968.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU2NDQ2MzQmcz00NDQ2MzkxJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107625+OR+9423622+OR+9423623%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107625,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107625,
        "cited_id": 101118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107625,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107625,
        "cited_id": 106771,
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
    "date_created": "2026-07-05T06:27:40Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:28:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:28:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T06:34:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:28:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Harris v. United States (1968)

```
<div>
<center><b><span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U.S. 234</a></span> (1968)</b></center>
<center><h1>HARRIS<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 92.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 18, 1968.</center>
<center>Decided March 5, 1968.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE DISTRICT OF COLUMBIA CIRCUIT.
<p><i>Paul H. Weinstein</i> argued the cause for petitioner. With him on the brief was <i>Laurence Levitan.</i></p>
<p><i>Francis X. Beytagh, Jr.,</i> argued the cause for the United States. On the brief were <i>Acting Solicitor General Spritzer, Assistant Attorney General Vinson, Beatrice Rosenberg</i> and <i>Julia P. Cooper.</i></p>
<p>PER CURIAM.</p>
<p>Petitioner was charged with robbery under the District of Columbia Code. D. C. Code Ann. § 22-2901. At his trial in the United States District Court for the District of Columbia, petitioner moved to suppress an automobile registration card belonging to the robbery victim, which the Government sought to introduce in evidence. The trial court, after a hearing, ruled that the card was admissible. Petitioner was convicted of the crime charged and sentenced to imprisonment for a period of <span class="star-pagination">*235</span> two to seven years. On appeal, a panel of the United States Court of Appeals for the District of Columbia Circuit reversed, holding that the card had been obtained by means of an unlawful search. The Government's petition for rehearing <i>en banc</i> was, however, granted, and the full Court of Appeals affirmed petitioner's conviction, with two judges dissenting. We granted certiorari to consider the problem presented under the Fourth Amendment. <span class="citation" data-id="8958920"><a href="/opinion/8967537/jackson-v-district-court-of-appeal-of-california-fourth-appellate/" aria-description="Citation for case: Jackson v. District Court of Appeal of California, Fourth...">386 U. S. 1003</a></span> (1967). We affirm.</p>
<p>Petitioner's automobile had been seen leaving the site of the robbery. The car was traced and petitioner was arrested as he was entering it, near his home. After a cursory search of the car, the arresting officer took petitioner to a police station. The police decided to impound the car as evidence, and a crane was called to tow it to the precinct. It reached the precinct about an hour and a quarter after petitioner. At this moment, the windows of the car were open and the door unlocked. It had begun to rain.</p>
<p>A regulation of the Metropolitan Police Department requires the officer who takes an impounded vehicle in charge to search the vehicle thoroughly, to remove all valuables from it, and to attach to the vehicle a property tag listing certain information about the circumstances of the impounding. Pursuant to this regulation, and without a warrant, the arresting officer proceeded to the lot to which petitioner's car had been towed, in order to search the vehicle, to place a property tag on it, to roll up the windows, and to lock the doors. The officer entered on the driver's side, searched the car, and tied a property tag on the steering wheel. Stepping out of the car, he rolled up an open window on one of the back doors. Proceeding to the front door on the passenger side, the officer opened the door in order to secure the window and door. He then saw the registration card, which lay face up on the metal stripping over which <span class="star-pagination">*236</span> the door closes. The officer returned to the precinct, brought petitioner to the car, and confronted petitioner with the registration card. Petitioner disclaimed all knowledge of the card. The officer then seized the card and brought it into the precinct. Returning to the car, he searched the trunk, rolled up the windows, and locked the doors.</p>
<p>The sole question for our consideration is whether the officer discovered the registration card by means of an illegal search. We hold that he did not. The admissibility of evidence found as a result of a search under the police regulation is not presented by this case. The precise and detailed findings of the District Court, accepted by the Court of Appeals, were to the effect that the discovery of the card was not the result of a search of the car, but of a measure taken to protect the car while it was in police custody. Nothing in the Fourth Amendment requires the police to obtain a warrant in these narrow circumstances.</p>
<p>Once the door had lawfully been opened, the registration card, with the name of the robbery victim on it, was plainly visible. It has long been settled that objects falling in the plain view of an officer who has a right to be in the position to have that view are subject to seizure and may be introduced in evidence. <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#42" aria-description="Citation for case: Ker v. California">374 U. S. 23, 42-43</a></span> (1963); <i>United States</i> v. <i>Lee,</i> <span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/" aria-description="Citation for case: United States v. Lee">274 U. S. 559</a></span> (1927); <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924).</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE MARSHALL took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE DOUGLAS, concurring.</p>
<p>Though <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span>, is not mentioned in the Court's opinion, I assume it has survived <span class="star-pagination">*237</span> because in the present case (1) the car was lawfully in police custody, and the police were responsible for protecting the car; (2) while engaged in the performance of their duty to protect the car, and not engaged in an inventory or other search of the car, they came across incriminating evidence.</p>
</div>
```

---

## GROUP: content/cases/Hayes v. Florida.md  (`case`, 5 assertions)

### content_page

```
---
title: "Hayes v. Florida"
type: case
citation: "470 U.S. 811 (1985)"
parallel_cite: "105 S. Ct. 1643; 84 L. Ed. 2d 705; 53 U.S.L.W. 4382"
neutral_cite: 1985 U.S. LEXIS 1523
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-03-20
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-03-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hayes v. Florida
  varies_by_point: false
  scope_note: "Good law; transporting a suspect to the station for fingerprinting without consent, a warrant, or probable cause is a seizure tantamount to arrest. The Court left open (dicta) that brief field fingerprinting on reasonable suspicion, carried out with dispatch, might be permissible."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111382/hayes-v-florida/"
  cluster_id: 111382
  opinion_id: 9429967
  identity_checked: true
homes:
  - page: "[[Seizure of the Person]]"
    role: "Limiting"
related: ["[[Davis v. Mississippi]]", "[[Florida v. Royer]]", "[[United States v. Hensley]]", "[[Terry v. Ohio]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure", "fingerprinting", "investigative-detention", "arrest"]
holding: "Transporting a suspect to the station for fingerprinting without consent, a warrant, or probable cause is a seizure tantamount to arrest requiring probable cause (brief field fingerprinting on reasonable suspicion left open)."
lake:
  record_id: Hayes v. Florida
  status: verified
  projected_at: 2026-07-06
---

# Hayes v. Florida

*470 U.S. 811 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating a series of burglary-rapes, officers without probable cause or a warrant went to Hayes's home, and — when he balked — effectively told him he would be arrested if he did not accompany them. They transported him to the station and fingerprinted him; the prints matched those at a crime scene and were used to convict him. Hayes moved to suppress, relying on *[[Davis v. Mississippi]]*.

## Issue
Whether the Fourth Amendment permits police, without probable cause or judicial authorization, to transport a suspect from his home to the station and detain him there for fingerprinting.

## Rule
No — such a station-house detention is an arrest requiring probable cause: "the line is crossed when the police, without probable cause or a warrant, forcibly remove a person from his home or other place in which he is entitled to be and transport him to the police station, where he is detained, although briefly, for investigative purposes. We adhere to the view that such seizures, at least where not under judicial supervision, are sufficiently like arrests to invoke the traditional rule that arrests may constitutionally be made only on probable cause." — 470 U.S. at 816. ^pin-816

The Court reserved a narrower field practice: "There is thus support in our cases for the view that the Fourth Amendment would permit seizures for the purpose of fingerprinting, if there is reasonable suspicion that the suspect has committed a criminal act, if there is a reasonable basis for believing that fingerprinting will establish or negate the suspect's connection with that crime, and if the procedure is carried out with dispatch." — *Id.* at 817. ^pin-817

## Application
Officers had neither probable cause nor a warrant nor judicial authorization, yet — under threat of arrest — removed Hayes from his home, transported him to the station, and detained him to take his prints. That conduct crossed the line into a [[Common Legal Terms#de-facto|de facto]] arrest requiring probable cause, so the fingerprints were the fruit of an unlawful seizure and had to be suppressed. The Court emphasized that its holding did not foreclose a brief *field* detention to take fingerprints where officers have reasonable suspicion and proceed with dispatch — but no such limited, on-site procedure occurred here.

## Conclusion
The warrantless station-house fingerprinting detention was an arrest without probable cause; the fingerprints were suppressed and the conviction reversed. *Hayes* reaffirms [[Davis v. Mississippi]] and marks the transport-to-the-station line while flagging the open question of brief field fingerprinting on reasonable suspicion.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Reaffirms and applies [[Davis v. Mississippi]]; consistent with the de-facto-arrest analysis of [[Florida v. Royer]] and the *[[Terry v. Ohio|Terry]]*-stop reach discussed in [[United States v. Hensley]] and [[Terry v. Ohio]].

## Appears on
- [[Seizure of the Person]] — *Limiting*

## Sources
- *Hayes v. Florida*, 470 U.S. 811 (1985) — https://www.courtlistener.com/opinion/111382/hayes-v-florida/ — pinpoints: 816, 817.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "43665a1911568bdd", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "470 U.S. 811 (1985)", "court": "U.S. Supreme Court", "neutral_cite": "1985 U.S. LEXIS 1523", "official_citation_present": true, "parallel_cite": "105 S. Ct. 1643; 84 L. Ed. 2d 705; 53 U.S.L.W. 4382", "title": "Hayes v. Florida", "year": "1985"}}
{"assertion_id": "0c37e14631f7a56d", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Transporting a suspect to the station for fingerprinting without consent, a warrant, or probable cause is a seizure tantamount to arrest requiring probable cause (brief field fingerprinting on reasonable suspicion left open).", "title": "Hayes v. Florida"}}
{"assertion_id": "777183c6fd18855b", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Limiting", "title": "Hayes v. Florida"}}
{"assertion_id": "042e9c572910b7b3", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1985-03-20", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Hayes v. Florida", "field_i_validity": "good_law", "scope_note": "Good law; transporting a suspect to the station for fingerprinting without consent, a warrant, or probable cause is a seizure tantamount to arrest. The Court left open (dicta) that brief field fingerprinting on reasonable suspicion, carried out with dispatch, might be permissible.", "title": "Hayes v. Florida", "varies_by_point": "false"}}
{"assertion_id": "d92dee305adc6fa4", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Hayes v. Florida"}}
```

### lake record — Hayes v. Florida

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hayes v. Florida",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hayes v. Florida",
    "case_name_short": "Hayes",
    "case_name_full": "Hayes v. Florida",
    "input_case_name": "Hayes v. Florida",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-03-20",
    "year": 1985,
    "docket": null,
    "cluster_id": 111382,
    "lead_opinion_id": 9429967,
    "sibling_ids": [
      111382,
      9429967,
      9429968
    ],
    "absolute_url": "/opinion/111382/hayes-v-florida/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "470 U.S. 811",
      "volume": "470",
      "reporter": "U.S.",
      "page": "811",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 1643",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1643",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 2d 705",
        "volume": "84",
        "reporter": "L. Ed. 2d",
        "page": "705",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4382",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4382",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 1523",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "1523",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "470 U.S. 811",
        "volume": "470",
        "reporter": "U.S.",
        "page": "811",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 1643",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1643",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 2d 705",
        "volume": "84",
        "reporter": "L. Ed. 2d",
        "page": "705",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 1523",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "1523",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4382",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4382",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "470 U.S. 811",
    "official_selection": {
      "court_class": "scotus",
      "selected": "470 U.S. 811",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-816",
      "page": null,
      "quote": "--- # Hayes v. Florida *470 U.S. 811 (1985)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigating a series of burglary-rapes, officers without probable cause or a warrant went to Hayes's home, and \u2014 when he balked \u2014 effectively told him he would be arrested if he did not accompany them. They transported him to the station and fingerprinted him; the prints matched those at a crime scene and were used to convict him. Hayes moved to suppress, relying on *Davis v. Mississippi*. ## Issue Whether the Fourth Amendment permits police, without probable cause or judicial authorization, to transport a suspect from his home to the station and detain him there for fingerprinting. ## Rule No \u2014 such a station-house detention is an arrest requiring probable cause:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-817",
      "page": null,
      "quote": "There is thus support in our cases for the view that the Fourth Amendment would permit seizures for the purpose of fingerprinting, if there is reasonable suspicion that the suspect has committed a criminal act, if there is a reasonable basis for believing that fingerprinting will establish or negate the suspect's connection with that crime, and if the procedure is carried out with dispatch.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-03-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hayes v. Florida",
    "varies_by_point": false,
    "scope_note": "Good law; transporting a suspect to the station for fingerprinting without consent, a warrant, or probable cause is a seizure tantamount to arrest. The Court left open (dicta) that brief field fingerprinting on reasonable suspicion, carried out with dispatch, might be permissible.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "People v. Financial Casualty & Surety, Inc.",
          "cluster_id": 4380249,
          "cite": [
            "10 Cal. App. 5th 369",
            "216 Cal. Rptr. 3d 173",
            "2017 Cal. App. LEXIS 294"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Paul Allen Decker v. State of Indiana",
          "cluster_id": 2745993,
          "cite": [
            "19 N.E.3d 368",
            "2014 Ind. App. LEXIS 515",
            "2014 WL 5461790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cabral",
          "cluster_id": 8727521,
          "cite": [
            "965 F. Supp. 2d 161",
            "2013 WL 1684162",
            "2013 U.S. Dist. LEXIS 53890"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Branham v. Commonwealth",
          "cluster_id": 1057965,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Porter v. State",
          "cluster_id": 1759540,
          "cite": [
            "255 S.W.3d 234",
            "2008 WL 553648"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Corbin v. State",
          "cluster_id": 1636551,
          "cite": [
            "91 S.W.3d 383",
            "2002 Tex. App. LEXIS 7528",
            "2002 WL 31374687"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Elmer Pace and Linda Pace v. City of Des Moines, Iowa, and Brian Danner",
          "cluster_id": 767420,
          "cite": [
            "201 F.3d 1050",
            "2000 U.S. App. LEXIS 388",
            "2000 WL 31713"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Shareef",
          "cluster_id": 154170,
          "cite": [
            "100 F.3d 1491",
            "1996 U.S. App. LEXIS 29483",
            "1996 WL 657885"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane1_negative"
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
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. United States",
          "cluster_id": 803270,
          "cite": [
            "183 L. Ed. 2d 351",
            "132 S. Ct. 2492",
            "567 U.S. 387",
            "2012 U.S. LEXIS 4872",
            "80 U.S.L.W. 4539",
            "23 Fla. L. Weekly Fed. S 437",
            "2012 WL 2368661",
            "95 Empl. Prac. Dec. (CCH) 44,539",
            "115 Fair Empl. Prac. Cas. (BNA) 353"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
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
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.",
          "cluster_id": 136990,
          "cite": [
            "159 L. Ed. 2d 292",
            "124 S. Ct. 2451",
            "542 U.S. 177",
            "2004 U.S. LEXIS 4385",
            "17 Fla. L. Weekly Fed. S 406",
            "72 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cheryl James v. Wilkes Barre City",
          "cluster_id": 812864,
          "cite": [
            "700 F.3d 675",
            "2012 U.S. App. LEXIS 24592",
            "2012 WL 5954632"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
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
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cortez v. McCauley",
          "cluster_id": 167088,
          "cite": [
            "478 F.3d 1108",
            "2007 WL 503819"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
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
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "David Evans v. Patrick Baker",
          "cluster_id": 813710,
          "cite": [
            "703 F.3d 636"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
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
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
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
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jaime Soto, Also Known as Leonel Guerra",
          "cluster_id": 602824,
          "cite": [
            "988 F.2d 1548",
            "1993 U.S. App. LEXIS 5415",
            "1993 WL 77475"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Thomas Cherry",
          "cluster_id": 450747,
          "cite": [
            "759 F.2d 1196",
            "81 A.L.R. Fed. 303",
            "1985 U.S. App. LEXIS 29511"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
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
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Luis Lopez-Medina",
          "cluster_id": 795541,
          "cite": [
            "461 F.3d 724",
            "71 Fed. R. Serv. 50",
            "2006 U.S. App. LEXIS 21682",
            "2006 WL 2454962"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Turner v. City of Taylor",
          "cluster_id": 2972481,
          "cite": [
            "412 F.3d 629",
            "2005 WL 1398522"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnny L. Marshall v. Secretary, Florida Department of Corrections",
          "cluster_id": 4237860,
          "cite": [
            "828 F.3d 1277",
            "2016 U.S. App. LEXIS 12812",
            "2016 WL 3742164"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williams v. Commonwealth",
          "cluster_id": 1206381,
          "cite": [
            "354 S.E.2d 79",
            "4 Va. App. 53",
            "3 Va. Law Rep. 2081",
            "1987 Va. App. LEXIS 165"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
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
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cynthia Kernats v. Thomas O'Sullivan",
          "cluster_id": 678542,
          "cite": [
            "35 F.3d 1171",
            "1994 U.S. App. LEXIS 25789",
            "1994 WL 503404"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Henry Espinosa",
          "cluster_id": 463815,
          "cite": [
            "782 F.2d 888",
            "1986 U.S. App. LEXIS 21494"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sornberger v. City Of Knoxville",
          "cluster_id": 792982,
          "cite": [
            "434 F.3d 1006",
            "2006 U.S. App. LEXIS 1394"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Arthur Maez",
          "cluster_id": 521939,
          "cite": [
            "872 F.2d 1444",
            "1989 U.S. App. LEXIS 5092",
            "1989 WL 36532"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111382 OR 9429967 OR 9429968) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MTcwMzM2MDAwMDAmcz01OTEyMDAmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111382+OR+9429967+OR+9429968%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111382 OR 9429967 OR 9429968)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTkmcz0xODkxNTA0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111382+OR+9429967+OR+9429968%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111382 OR 9429967 OR 9429968)",
        "reviewed": 9,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 9,
        "triage_read": 0,
        "triage_snippet_classified": 9
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111382 OR 9429967 OR 9429968)",
    "indexed_citing_opinions": 357,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111382,
        "count": 319,
        "count_source": "search"
      },
      {
        "opinion_id": 9429967,
        "count": 44,
        "count_source": "search"
      },
      {
        "opinion_id": 9429968,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 604,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hayes-v-florida.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY3MTMyMzQmcz05NTA0MjM2JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111382+OR+9429967+OR+9429968%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111382,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 1226554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 1677682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 2223532,
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
    "date_created": "2026-07-05T06:34:43Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:34:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:34:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T06:38:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:34:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hayes v. Florida

```
<opinion type="majority">
<author id="b868-6">Justice White</author>
<p id="AG2">delivered the opinion of the Court.</p>
<p id="b868-7">The issue before us in this case is whether the Fourth Amendment to the Constitution of the United States, applicable to the States by virtue of the Fourteenth Amendment, was properly applied by the District Court of Appeal of Florida, Second District, to allow police to transport a suspect to the station house for fingerprinting, without his consent and without probable cause or prior judicial authorization.</p>
<p id="b868-8">A series of burglary-rapes occurred in Punta Gorda, Florida, in 1980. Police found latent fingerprints on the doorknob of the bedroom of one of the victims, fingerprints they believed belonged to the assailant. The police also found a herringbone pattern tennis shoe print near the victim’s front porch. Although they had little specific information to tie petitioner Hayes to the crime, after police interviewed him along with 30 to 40 other men who generally fit the description of the assailant, the investigators came to consider petitioner a principal suspect. They decided to visit petitioner’s home to obtain his fingerprints or, if he was uncooperative, to arrest him. They did not seek a warrant authorizing this procedure.</p>
<p id="b868-9">Arriving at petitioner’s house, the officers spoke to petitioner on his front porch. When he expressed reluctance voluntarily to accompany them to the station for fingerprinting, one of the investigators explained that they would therefore arrest him. Petitioner, in the words of the investigator, then “blurted out” that he would rather go with the officers to the station than be arrested. App. 20. While the officers were on the front porch, they also seized a pair of herringbone pattern tennis shoes in plain view.</p>
<p id="b869-4"><page-number citation-index="1" label="813">*813</page-number>Petitioner was then taken to the station house, where he was fingerprinted. When police determined that his prints matched those left at the scene of the crime, petitioner was placed under formal arrest. Before trial, petitioner moved to suppress the fingerprint evidence, claiming it was the fruit of an illegal detention. The trial court denied the motion and admitted the evidence without expressing a reason. Petitioner was convicted of the burglary and sexual battery committed at the scene where the latent fingerprints were found.</p>
<p id="b869-5">The District Court of Appeal of Florida, Second District, affirmed the conviction. <span class="citation" data-id="1677682"><a href="/opinion/1677682/hayes-v-state/" aria-description="Citation for case: Hayes v. State">439 So. 2d 896</a></span> (1983). The court declined to find consent, reasoning that in view of the threatened arrest it was, “at best, highly questionable” that Hayes voluntarily accompanied the officers to the station. <span class="citation" data-id="1677682"><a href="/opinion/1677682/hayes-v-state/#898" aria-description="Citation for case: Hayes v. State"><em>Id., </em>at 898</a></span>. The court also expressly found that the officers did not have probable cause to arrest petitioner until after they obtained his fingerprints. <span class="citation" data-id="1677682"><a href="/opinion/1677682/hayes-v-state/#899" aria-description="Citation for case: Hayes v. State"><em>Id., </em>at 899</a></span>. Nevertheless, although finding neither consent nor probable cause, the court held, analogizing to the stop-and-frisk rule of <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), that the officers could transport petitioner to the station house and take his fingerprints on the basis of their reasonable suspicion that he was involved in the crime. <span class="citation" data-id="1677682"><a href="/opinion/1677682/hayes-v-state/#899" aria-description="Citation for case: Hayes v. State">439 So. 2d, at 899, 904</a></span>.</p>
<p id="b869-6">The Florida Supreme Court denied review by a four-to-three decision, <span class="citation no-link">447 So. 2d 886</span> (1983). We granted certiorari to review this application of <em>Terry, </em><span class="citation multiple-matches"><a href="/c/U.%20S./469/816/">469 U. S. 816</a></span> (1984), and we now reverse.</p>
<p id="b869-7">We agree with petitioner that <em>Davis </em>v. <em>Mississippi, </em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969), requires reversal of the judgment below. In <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span>, </em>in the course of investigating a rape, police officers brought petitioner Davis to police headquarters on December 3, 1965. He was fingerprinted and briefly questioned before being released. He was later charged and convicted of the rape. An issue there was whether the fingerprints taken on December 3 were the inadmissible fruits of an illegal detention. Concededly, the police at that time were without prob<page-number citation-index="1" label="814">*814</page-number>able cause for an arrest, there was no warrant, and Davis had not consented to being taken to the station house. The State nevertheless contended that the Fourth Amendment did not forbid an investigative detention for the purpose of fingerprinting, even in the absence of probable cause or a warrant. We rejected that submission, holding that Davis’ detention for the purpose of fingerprinting was subject to the constraints of the Fourth Amendment and exceeded the permissible limits of those temporary seizures authorized by <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra.</a></span> </em>This was so even though fingerprinting, because it involves neither repeated harassment nor any of the probing into private life and thoughts that often marks interrogation and search, represents a much less serious intrusion upon personal security than other types of searches and detentions. <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#727" aria-description="Citation for case: Davis v. Mississippi">394 U. S., at 727</a></span>. Nor was it a sufficient answer to the Fourth Amendment issue to recognize that fingerprinting is an inherently more reliable and effective crime-solving mechanism than other types of evidence such as lineups and confessions. <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Ibid.</a></span> </em>The Court indicated that perhaps under narrowly confined circumstances, a detention for fingerprinting on less than probable cause might comply with the Fourth Amendment, but found it unnecessary to decide that question since no effort was made to employ the procedures necessary to satisfy the Fourth Amendment. <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#728" aria-description="Citation for case: Davis v. Mississippi">Id., at 728</a></span>. Rather, Davis had been detained at police headquarters without probable cause to arrest and without authorization by a judicial officer.</p>
<p id="b870-5">Here, as in <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span>, </em>there was no probable cause to arrest, no consent to the journey to the police station, and no judicial authorization for such a detention for fingerprinting purposes.<footnotemark>1</footnotemark> Unless later cases have undermined <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span> </em>or <page-number citation-index="1" label="815">*815</page-number>we now disavow that decision, the judgment below must be reversed.</p>
<p id="b871-5">None of our later cases have undercut the holding in <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span> </em>that transportation to and investigative detention at the station house without probable cause or judicial authorization together violate the Fourth Amendment. Indeed, some 10 years later, in <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979), we refused to extend <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra,</a></span> </em>to authorize investigative interrogations at police stations on less than probable cause, even though proper warnings under <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), had been given. We relied on and reaffirmed the holding in <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span> </em>that in the absence of probable cause or a warrant investigative detentions at the police station for fingerprinting purposes could not be squared with the Fourth Amendment, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#213" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 213-216</a></span>, while at the same time repeating the possibility that the Amendment might permit a narrowly circumscribed procedure for fingerprinting detentions on less than probable cause. Since that time, we have several times revisited and explored the reach of <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio</a></span>, </em>most recently in <em>United States </em>v. <em>Sharpe, ante, </em>p. 675, and <em>United States </em>v. <em>Hensley, </em><span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/" aria-description="Citation for case: United States v. Hensley">469 U. S. 221</a></span> (1985). But none of these cases have sustained against Fourth Amendment challenge the involuntary removal of a suspect from his home to a police station and his detention there for investigative purposes, whether for interrogation or fingerprinting, absent probable cause or judicial authorization.</p>
<p id="b871-6">Nor are we inclined to forswear <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span>. </em>There is no doubt that at some point in the investigative process, police pro<page-number citation-index="1" label="816">*816</page-number>cedures can qualitatively and quantitatively be so intrusive with respect to a suspect’s freedom of movement and privacy interests as to trigger the full protection of the Fourth and Fourteenth Amendments. <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#212" aria-description="Citation for case: Dunaway v. New York"><em>Dunaway, supra, </em>at 212</a></span>; <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#499" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 499</a></span> (1983) (plurality opinion). And our view continues to be that the line is crossed when the police, without probable cause or a warrant, forcibly remove a person from his home or other place in which he is entitled to be and transport him to the police station, where he is detained, although briefly, for investigative purposes. We adhere to the view that such seizures, at least where not under judicial supervision, are sufficiently like arrests to invoke the traditional rule that arrests may constitutionally be made only on probable cause.<footnotemark>2</footnotemark></p>
<p id="b872-5">None of the foregoing implies that a brief detention in the field for the purpose of fingerprinting, where there is only reasonable suspicion not amounting to probable cause, is necessarily impermissible under the Fourth Amendment. In addressing the reach of a <em>Terry </em>stop in <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 146</a></span> (1972), we observed that “[a] brief stop of a suspicious individual, in order to determine his identity or to maintain the status quo momentarily while obtaining more information, may be most reasonable in light of the facts known to the officer at the time.” Also, just this Term, we concluded that if there are articulable facts supporting a reasonable suspicion that a person has committed a criminal offense, that person may be stopped in order to identify him, to question him briefly, or to detain him briefly while attempting to obtain additional information. <em>United States </em>v. <span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/#229" aria-description="Citation for case: United States v. Hensley"><em>Hensley, supra, </em>at 229, 232, 234</a></span>. Cf. <em>United States </em><page-number citation-index="1" label="817">*817</page-number>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983); <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976); <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975). There is thus support in our cases for the view that the Fourth Amendment would permit seizures for the purpose of fingerprinting, if there is reasonable suspicion that the suspect has committed a criminal act, if there is a reasonable basis for believing that fingerprinting will establish or negate the suspect’s connection with that crime, and if the procedure is carried out with dispatch. Cf. <em>United States </em>v. <em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place, supra.</a></span> </em>Of course, neither reasonable suspicion nor probable cause would suffice to permit the officers to make a warrantless entry into a person’s house for the purpose of obtaining fingerprint identification. <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980).</p>
<p id="b873-5">We also do not abandon the suggestion in <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span> </em>and <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span> </em>that under circumscribed procedures, the Fourth Amendment might permit the judiciary to authorize the seizure of a person on less than probable cause and his removal to the police station for the purpose of fingerprinting. We do not, of course, have such a case before us.<footnotemark>3</footnotemark> We do note, however, that some States, in reliance on the suggestion in <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span>, </em>have enacted procedures for judicially authorized seizures for the purpose of fingerprinting. The state courts are not in accord on the validity of these efforts to insulate investigative seizures from Fourth Amendment invalidation. Compare <em>People </em>v. <em>Madson, </em><span class="citation" data-id="1226554"><a href="/opinion/1226554/people-v-madson/#31" aria-description="Citation for case: People v. Madson">638 P. 2d 18, 31-32</a></span> (Colo. 1981), with <em>State </em>v. <em>Evans, </em><span class="citation" data-id="9740420"><a href="/opinion/2223532/state-v-evans/#438" aria-description="Citation for case: State v. Evans">215 Neb. 433, 438-439</a></span>, <span class="citation" data-id="9740420"><a href="/opinion/2223532/state-v-evans/#792" aria-description="Citation for case: State v. Evans">338 N. W. 2d 788, 792-793</a></span> (1983), and <em>In re an Investigation into Death of Abe A., </em>56 N. Y. 2d 288, 295-296, <span class="citation" data-id="5534665"><a href="/opinion/5685680/in-re-of-an-investigation-into-the-death-of-jon-l/#269" aria-description="Citation for case: In re of an Investigation into the Death of Jon L.">437 N. E. 2d 265, 269</a></span> (1982).</p>
<p id="b873-6">As we have said, absent probable cause and a warrant, <em>Davis </em>v. <em>Mississippi, </em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969), requires the <page-number citation-index="1" label="818">*818</page-number>reversal of the judgment of the Florida District Court of Appeal.</p>
<p id="b874-5">
<em>It is so ordered.</em>
</p>
<judges id="b874-6">Justice Blackmun concurs in the judgment.</judges>
<judges id="b874-7">Justice Powell took no part in the consideration or decision in this case.</judges>
<footnote label="1">
<p id="b870-6"> The Florida District Court of Appeal judged this case on the basis of its determination that the police were without probable cause to arrest and that Hayes did not voluntarily agree to accompany the officers to the police station. Although the State invites us to review the record and hold either that there was probable cause to arrest or that Hayes voluntarily <page-number citation-index="1" label="815">*815</page-number>went with the officers to the station, we decline to become involved in these fact-bound issues. We also put aside the State’s suggestion that the inevitable discovery exception to the exclusionary rule, see <em>Nix </em>v. <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams"><em>Williams, 467 </em>U. S. 431</a></span> (1984), applies in this case. This argument was not presented to or passed upon by any of the state courts and is presented here for the first time. We thus address only the issue decided by the Florida court and presented in the petition for certiorari.</p>
</footnote>
<footnote label="2">
<p id="b872-6"> Thus, in <em>United States </em>v. <em>Sharpe, ante, </em>p. 675, where we recently sustained a 20-minute investigatory stop on a highway, we pointed out that the pertinent facts in <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>, </em>where we invalidated the detention, were “that (1) the defendant was taken from a private dwelling; (2) he was transported unwillingly to the police station; and (3) he there was subjected to custodial interrogation resulting in a confession.” <em>Ante, </em>at 684, n. 4.</p>
</footnote>
<footnote label="3">
<p id="b873-7"> Nor is there any suggestion in this case that there were any exigent circumstances making necessary the removal of Hayes to the station house for the purpose of fingerprinting.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Haynes v. Washington.md  (`case`, 5 assertions)

### content_page

```
---
title: "Haynes v. Washington"
type: case
citation: "373 U.S. 503 (1963)"
parallel_cite: "83 S. Ct. 1336; 10 L. Ed. 2d 513"
neutral_cite: 1963 U.S. LEXIS 1439
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1963
date_decided: 1963-05-27
docket: 147
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1963-05-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Haynes v. Washington
  varies_by_point: false
  scope_note: "Good law; incommunicado detention plus an express threat/promise (you may call your wife only if you sign a confession) renders a written confession involuntary under the totality of circumstances."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106625/haynes-v-washington/"
  cluster_id: 106625
  opinion_id: 106625
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Lynumn v. Illinois]]", "[[Spano v. New York]]", "[[Ashcraft v. Tennessee]]", "[[Brown v. Mississippi]]"]
aliases: []
tags: ["case", "fifth-amendment", "fourteenth-amendment", "confessions", "voluntariness", "due-process", "incommunicado", "coercion"]
holding: "A written confession obtained in an atmosphere of substantial coercion and inducement — incommunicado detention plus the express threat of continued isolation and the promise of contact with family conditioned on signing a confession — is involuntary under the totality of circumstances and inadmissible under the Fourteenth Amendment."
lake:
  record_id: Haynes v. Washington
  status: verified
  projected_at: 2026-07-09
---

# Haynes v. Washington

*373 U.S. 503 (1963)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Haynes was arrested for robbery and held in police custody. He repeatedly asked to call his wife and to contact a lawyer, and the police repeatedly refused — telling him he could make a call only after he cooperated and gave a written, signed confession. Held incommunicado and confronted with that condition, Haynes — who at first resisted a written statement — gave in and signed a written confession, which was admitted against him at trial.

## Issue
Whether a written confession obtained during incommunicado detention, after police conditioned the suspect's contact with his family on his signing the confession, was voluntary under the Due Process Clause.

## Rule
No — it was the product of substantial coercion and inducement. "The uncontroverted portions of the record thus disclose that the petitioner's written confession was obtained in an atmosphere of substantial coercion and inducement created by statements and actions of state authorities." — 373 U.S. at 513. ^pin-513

The express threat and conditioned promise made the choice involuntary: "Confronted with the express threat of continued incommunicado detention and induced by the promise of communication with and access to family, Haynes understandably chose to make and sign the damning written statement; given the unfair and inherently coercive context in which made, that choice cannot be said to be the voluntary product of a free and unconstrained will, as required by the Fourteenth Amendment." — [*Id.* at 514](https://www.courtlistener.com/opinion/106625/haynes-v-washington/#:~:text=Confronted%20with%20the%20express%20threat). ^pin-514

The Court added that "even apart from the express threat, the basic techniques present here—the secret and incommunicado detention and interrogation—are devices adapted and used to extort confessions from suspects." — *Id.* at 514–515. ^pin-514a

## Application
Like the petitioner in [[Lynumn v. Illinois]], Haynes "was alone in the hands of the police, with no one to advise or aid him," and had no reason to doubt the police could continue his incommunicado detention indefinitely. He resisted a written statement and yielded only after consistent denials of his requests to call his wife and the conditioning of that contact on his confessing. Under the totality of those circumstances his signed confession was involuntary, and its admission violated due process — a conclusion the Court reached on its own independent review of the record, not bound by the state courts.

## Conclusion
The written confession was involuntary; admitting it violated the Fourteenth Amendment, and the judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Haynes* applies the overborne-will test of [[Lynumn v. Illinois]] to incommunicado detention plus a conditioned promise, in the due-process line anchored by [[Brown v. Mississippi]] and developed in [[Spano v. New York]] and [[Ashcraft v. Tennessee]].

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Haynes v. Washington*, 373 U.S. 503 (1963) — https://www.courtlistener.com/opinion/106625/haynes-v-washington/ — pinpoints: 513–515.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "687b8bcdcab9166e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "373 U.S. 503 (1963)", "court": "U.S. Supreme Court", "neutral_cite": "1963 U.S. LEXIS 1439", "official_citation_present": true, "parallel_cite": "83 S. Ct. 1336; 10 L. Ed. 2d 513", "title": "Haynes v. Washington", "year": "1963"}}
{"assertion_id": "97ba043c94737114", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A written confession obtained in an atmosphere of substantial coercion and inducement — incommunicado detention plus the express threat of continued isolation and the promise of contact with family conditioned on signing a confession — is involuntary under the totality of circumstances and inadmissible under the Fourteenth Amendment.", "title": "Haynes v. Washington"}}
{"assertion_id": "ae52638f7df0105f", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key — Progeny / Refinement", "title": "Haynes v. Washington"}}
{"assertion_id": "3fe3096f0d277bf6", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1963-05-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Haynes v. Washington", "field_i_validity": "good_law", "scope_note": "Good law; incommunicado detention plus an express threat/promise (you may call your wife only if you sign a confession) renders a written confession involuntary under the totality of circumstances.", "title": "Haynes v. Washington", "varies_by_point": "false"}}
{"assertion_id": "63d0d8c40759ec2b", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Haynes v. Washington"}}
```

### lake record — Haynes v. Washington

```json
{
  "schema_version": "s2.v1",
  "record_id": "Haynes v. Washington",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Haynes v. Washington",
    "case_name_short": "Haynes",
    "case_name_full": "Haynes v. Washington",
    "input_case_name": "Haynes v. Washington",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1963-05-27",
    "year": 1963,
    "docket": "147",
    "cluster_id": 106625,
    "lead_opinion_id": 106625,
    "sibling_ids": [
      106625,
      9422619,
      9422620
    ],
    "absolute_url": "/opinion/106625/haynes-v-washington/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "373 U.S. 503",
      "volume": "373",
      "reporter": "U.S.",
      "page": "503",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "83 S. Ct. 1336",
        "volume": "83",
        "reporter": "S. Ct.",
        "page": "1336",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 L. Ed. 2d 513",
        "volume": "10",
        "reporter": "L. Ed. 2d",
        "page": "513",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1963 U.S. LEXIS 1439",
        "volume": "1963",
        "reporter": "U.S. LEXIS",
        "page": "1439",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "373 U.S. 503",
        "volume": "373",
        "reporter": "U.S.",
        "page": "503",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 S. Ct. 1336",
        "volume": "83",
        "reporter": "S. Ct.",
        "page": "1336",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 L. Ed. 2d 513",
        "volume": "10",
        "reporter": "L. Ed. 2d",
        "page": "513",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1963 U.S. LEXIS 1439",
        "volume": "1963",
        "reporter": "U.S. LEXIS",
        "page": "1439",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "373 U.S. 503",
    "official_selection": {
      "court_class": "scotus",
      "selected": "373 U.S. 503",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-513",
      "page": null,
      "quote": "--- # Haynes v. Washington *373 U.S. 503 (1963)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Haynes was arrested for robbery and held in police custody. He repeatedly asked to call his wife and to contact a lawyer, and the police repeatedly refused \u2014 telling him he could make a call only after he cooperated and gave a written, signed confession. Held incommunicado and confronted with that condition, Haynes \u2014 who at first resisted a written statement \u2014 gave in and signed a written confession, which was admitted against him at trial. ## Issue Whether a written confession obtained during incommunicado detention, after police conditioned the suspect's contact with his family on his signing the confession, was voluntary under the Due Process Clause. ## Rule No \u2014 it was the product of substantial coercion and inducement.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-514",
      "page": null,
      "quote": "Confronted with the express threat of continued incommunicado detention and induced by the promise of communication with and access to family, Haynes understandably chose to make and sign the damning written statement; given the unfair and inherently coercive context in which made, that choice cannot be said to be the voluntary product of a free and unconstrained will, as required by the Fourteenth Amendment.",
      "star_marker": "514",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 20502,
      "fragment": "#:~:text=Confronted%20with%20the%20express%20threat",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-514a",
      "page": null,
      "quote": "even apart from the express threat, the basic techniques present here\u2014the secret and incommunicado detention and interrogation\u2014are devices adapted and used to extort confessions from suspects.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1963-05-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Haynes v. Washington",
    "varies_by_point": false,
    "scope_note": "Good law; incommunicado detention plus an express threat/promise (you may call your wife only if you sign a confession) renders a written confession involuntary under the totality of circumstances.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Vasquez-Santiago",
          "cluster_id": 10133179,
          "cite": [
            "301 Or. App. 90",
            "456 P.3d 270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jalonte Little v. United States",
          "cluster_id": 3153940,
          "cite": [
            "125 A.3d 1119",
            "2015 D.C. App. LEXIS 526"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Corley v. United States",
          "cluster_id": 145888,
          "cite": [
            "173 L. Ed. 2d 443",
            "129 S. Ct. 1558",
            "556 U.S. 303",
            "2009 U.S. LEXIS 2512"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Charley B. Haswood",
          "cluster_id": 784327,
          "cite": [
            "350 F.3d 1024",
            "2003 Cal. Daily Op. Serv. 10282",
            "62 Fed. R. Serv. 1478",
            "2003 U.S. App. LEXIS 24181",
            "2003 WL 22833048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dickerson",
          "cluster_id": 2967209,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gomes v. State",
          "cluster_id": 2342281,
          "cite": [
            "9 S.W.3d 373",
            "1999 WL 1080989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Riley v. Dorton",
          "cluster_id": 2966500,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane1_negative"
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
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chapman v. California",
          "cluster_id": 107359,
          "cite": [
            "17 L. Ed. 2d 705",
            "87 S. Ct. 824",
            "386 U.S. 18",
            "1967 U.S. LEXIS 2198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
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
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York Times Co. v. Sullivan",
          "cluster_id": 106761,
          "cite": [
            "11 L. Ed. 2d 686",
            "84 S. Ct. 710",
            "376 U.S. 254",
            "1964 U.S. LEXIS 1655",
            "1 Media L. Rep. (BNA) 1527",
            "95 A.L.R. 2d 1412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
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
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
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
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
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
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Denno",
          "cluster_id": 106881,
          "cite": [
            "12 L. Ed. 2d 908",
            "84 S. Ct. 1774",
            "378 U.S. 368",
            "1964 U.S. LEXIS 826",
            "1 A.L.R. 3d 1205",
            "28 Ohio Op. 2d 177"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
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
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
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
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Escobedo v. Illinois",
          "cluster_id": 106883,
          "cite": [
            "12 L. Ed. 2d 977",
            "84 S. Ct. 1758",
            "378 U.S. 478",
            "1964 U.S. LEXIS 827",
            "4 Ohio Misc. 197",
            "32 Ohio Op. 2d 31"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mincey v. Arizona",
          "cluster_id": 109905,
          "cite": [
            "57 L. Ed. 2d 290",
            "98 S. Ct. 2408",
            "437 U.S. 385",
            "1978 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
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
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
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
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. New Jersey",
          "cluster_id": 107260,
          "cite": [
            "16 L. Ed. 2d 882",
            "86 S. Ct. 1772",
            "384 U.S. 719",
            "1966 U.S. LEXIS 1127",
            "36 Ohio Op. 2d 439",
            "8 Ohio Misc. 324"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
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
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hoffa v. United States",
          "cluster_id": 107318,
          "cite": [
            "17 L. Ed. 2d 374",
            "87 S. Ct. 408",
            "385 U.S. 293",
            "1966 U.S. LEXIS 2778"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mayle v. Felix",
          "cluster_id": 799989,
          "cite": [
            "162 L. Ed. 2d 582",
            "125 S. Ct. 2562",
            "545 U.S. 644",
            "2005 U.S. LEXIS 5016"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
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
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lego v. Twomey",
          "cluster_id": 108429,
          "cite": [
            "30 L. Ed. 2d 618",
            "92 S. Ct. 619",
            "404 U.S. 477",
            "1972 U.S. LEXIS 100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miller v. Fenton",
          "cluster_id": 111542,
          "cite": [
            "88 L. Ed. 2d 405",
            "106 S. Ct. 445",
            "474 U.S. 104",
            "1985 U.S. LEXIS 144",
            "54 U.S.L.W. 4022"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garrity v. New Jersey",
          "cluster_id": 107336,
          "cite": [
            "17 L. Ed. 2d 562",
            "87 S. Ct. 616",
            "385 U.S. 493",
            "1967 U.S. LEXIS 2882"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murphy v. Waterfront Commission of New York Harbor",
          "cluster_id": 106864,
          "cite": [
            "12 L. Ed. 2d 678",
            "84 S. Ct. 1594",
            "378 U.S. 52",
            "1964 U.S. LEXIS 2229",
            "56 L.R.R.M. (BNA) 2544"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
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
        "journal_ref": "Haynes v. Washington:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106625 OR 9422619 OR 9422620) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04NDMxNzc2MDAwMDAmcz0xNDQzODEzJnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106625+OR+9422619+OR+9422620%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(106625 OR 9422619 OR 9422620)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MzUmcz03ODE3MjImdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28106625+OR+9422619+OR+9422620%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106625 OR 9422619 OR 9422620)",
        "reviewed": 9,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 9,
        "triage_read": 0,
        "triage_snippet_classified": 9
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106625 OR 9422619 OR 9422620)",
    "indexed_citing_opinions": 904,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106625,
        "count": 865,
        "count_source": "search"
      },
      {
        "opinion_id": 9422619,
        "count": 64,
        "count_source": "search"
      },
      {
        "opinion_id": 9422620,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1405,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/haynes-v-washington.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjYzNjE5NzEmcz00NjM1NzAwJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106625+OR+9422619+OR+9422620%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106625,
        "cited_id": 94454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 104933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 105149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 105436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 105683,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 106421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 1156234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106625,
        "cited_id": 2499246,
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
    "date_created": "2026-07-05T06:38:39Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:38:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:38:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T06:41:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:38:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Haynes v. Washington

```
<div>
<center><b><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U.S. 503</a></span> (1963)</b></center>
<center><h1>HAYNES<br>
v.<br>
WASHINGTON.</h1></center>
<center>No. 147.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 26-27, 1963.</center>
<center>Decided May 27, 1963.</center>
CERTIORARI TO THE SUPREME COURT OF WASHINGTON.
<p><i>Lawrence Speiser</i> argued the cause for petitioner. With him on the briefs were <i>Francis Hoague</i> and <i>William W. Ross.</i></p>
<p><i>George A. Kain</i> argued the cause for respondent. With him on the briefs were <i>Joseph J. Rekofke</i> and <i>John J. Lally.</i></p>
<p><span class="star-pagination">*504</span> MR. JUSTICE GOLDBERG delivered the opinion of the Court.</p>
<p>The petitioner, Raymond L. Haynes, was tried in a Superior Court of the State of Washington on a charge of robbery, found guilty by a jury, and sentenced to imprisonment "for a term of not more than 20 years." The Washington Supreme Court affirmed the conviction, with four of nine judges dissenting. <span class="citation" data-id="9539685"><a href="/opinion/1156234/state-v-haynes/" aria-description="Citation for case: State v. Haynes">58 Wash. 2d 716</a></span>, <span class="citation" data-id="9539685"><a href="/opinion/1156234/state-v-haynes/" aria-description="Citation for case: State v. Haynes">364 P. 2d 935</a></span>. Certiorari was granted, <span class="citation multiple-matches"><a href="/c/U.%20S./370/902/">370 U. S. 902</a></span>, to consider whether the admission of the petitioner's written and signed confession into evidence against him at trial constituted a denial of due process of law.</p>
<p>Haynes contends that the confession was involuntary, and thus constitutionally inadmissible, because induced by police threats and promises. He testified at trial that during the approximately 16-hour period between the time of his arrest and the making and signing of the written confession, he several times asked police to allow him to call an attorney and to call his wife. He said that such requests were uniformly refused and that he was repeatedly told that he would not be allowed to call unless and until he "cooperated" with police and gave them a written and signed confession admitting participation in the robbery. He was not permitted to phone his wife, or for that matter anyone, either on the night of his arrest or the next day. The police persisted in their refusals to allow him contact with the outside world, he said, even after he signed one written confession and after a preliminary hearing before a magistrate, late on the day following his arrest. According to the petitioner, he was, in fact, held incommunicado by the police until some five or seven days after his arrest.<sup>[1]</sup></p>
<p><span class="star-pagination">*505</span> The State asserts that the petitioner's version of events is contradicted, that the confession was freely given, and that, in any event, the question of voluntariness was conclusively resolved against the petitioner by the verdict of the jury at trial. We consider each of these contentions in turn.</p>
<p></p>
<h2>I.</h2>
<p>The petitioner was charged with robbing a gasoline service station in the City of Spokane, Washington, at about 9 p. m. on Thursday, December 19, 1957. He was arrested by Spokane police in the vicinity of the station within approximately one-half hour after the crime.<sup>[2]</sup> Though he orally admitted the robbery to officers while en route to the police station, he was, on arrival there, not charged with the crime, but instead booked for "investigation," or, as it is locally called, placed on the "small book." Concededly, prisoners held on the "small book" are permitted by police neither to make phone calls nor to have any visitors.<sup>[3]</sup></p>
<p>Shortly after arriving at the station at about 10 p. m., the petitioner was questioned for about one-half hour by Lieutenant Wakeley of the Spokane police, during which period he again orally admitted the crime. He was then placed in a line-up and identified by witnesses as one of the robbers. Apparently, nothing else was done that night.</p>
<p>On the following morning, beginning at approximately 9:30 a. m., the petitioner was again questioned for about an hour and a half, this time by Detectives Peck and <span class="star-pagination">*506</span> Cockburn. He once more orally admitted the robbery, and a written confession was transcribed. Shortly thereafter, he was taken to the office of the deputy prosecutor, where still another statement was taken and transcribed. Though Haynes refused to sign this second confession, he then did sign the earlier statement given to Detectives Peck and Cockburn.<sup>[4]</sup> Later that same afternoon he was taken before a magistrate for a preliminary hearing; this was at about 4 p. m. on December 20, the day after his arrest.</p>
<p>At the conclusion of the hearing, Haynes was transferred to the county jail and on either the following Tuesday or Thursday was returned to the deputy prosecutor's office. He was again asked to sign the second statement which he had given there some four to six days earlier, but again refused to do so.</p>
<p>The written confession taken from Haynes by Detectives Peck and Cockburn on the morning after his arrest and signed by Haynes on the same day in the deputy prosecutor's office was introduced into evidence against the petitioner over proper and timely objection by his counsel that such use would violate due process of law. Under the Washington procedure then in effect,<sup>[5]</sup> voluntariness of the confession was treated as a question of fact <span class="star-pagination">*507</span> for ultimate determination by the jury. In overruling the petitioner's objection to use of the confession, the trial judge, however, made an apparently preliminary determination that it was voluntary and "conditionally" admissible. See <span class="citation" data-id="9539685"><a href="/opinion/1156234/state-v-haynes/#719" aria-description="Citation for case: State v. Haynes">58 Wash. 2d, at 719-720</a></span>, <span class="citation" data-id="9539685"><a href="/opinion/1156234/state-v-haynes/#937" aria-description="Citation for case: State v. Haynes">364 P. 2d, at 937</a></span>. The evidence going to voluntariness was heard before the jury and the issue submitted to it. The jury returned a general verdict of guilty and was not required to, and did not, indicate its view with respect to the voluntariness of the confession.</p>
<p></p>
<h2>II.</h2>
<p>The State first contends that the petitioner's version of the circumstances surrounding the making and signing of his written confession is evidentially contradicted and thus should be rejected by this Court. We have carefully reviewed the entire record, however, and find that Haynes' account is uncontradicted in its essential elements.</p>
<p>Haynes testified that on the evening of his arrest he made several specific requests of the police that he be permitted to call an attorney and to call his wife. Each such request, he said, was refused. He stated, however, that he was told he might make a call if he confessed:</p>
<blockquote>"They kept wanting me to own up to robbing a Richfield Service Station and I asked Mr. [Detective] Pike several times if I could call a lawyer and he said if I cooperated and gave him a statement . . . that I would be allowed to call, to make a phone call . . . ."</blockquote>
<p>On cross-examination, Lieutenant Wakeley, the officer who interrogated the petitioner on the night of his arrest, first said that Haynes did not ask him for permission to call his wife, but merely inquired whether his wife would be notified of his arrest. Lieutenant Wakeley said that <span class="star-pagination">*508</span> he told the petitioner that his wife would be notified.<sup>[6]</sup> Defense counsel, however, pursued the point and, only a moment later, Wakeley testified that Haynes "may have" asked permission to call his wife himself; Wakeley said he didn't "remember exactly whether he asked or whether we wouldn't notify his wife." Wakeley then testified that he simply didn't "remember" whether Haynes asked to call his wife so that she might secure a lawyer for him; in addition, the lieutenant admitted that the petitioner might have asked to call his wife after the interrogation was completed. Detective Pike, also testifying at trial, said simply that he had not talked to Haynes on the evening of the arrest.</p>
<p>If this were the only evidence of police coercion and inducement in the record, we would face the problem of determining whether, in view of the testimony of Lieutenant Wakeley and Detective Pike, the petitioner's own testimony would be sufficient, on review by this Court, to establish the existence of impermissible police conduct barring use of the written confession ultimately obtained. We need not pursue such an inquiry, however, since the record contains other probative, convincing, and uncontradicted evidence.</p>
<p>The written confession introduced at trial was dictated and transcribed while Haynes was being questioned by Detectives Peck and Cockburn on the morning of December 20, the day after the robbery. Haynes testified:</p>
<blockquote>"Q. . . . [S]tate whether or not the officers at that time asked you to give them a statement. A. Yes.</blockquote>
<blockquote>
<span class="star-pagination">*509</span> "Q. And what was your answer to that? A. I wanted to call my wife.</blockquote>
<blockquote>"Q. And were you allowed to call your wife? A. No.</blockquote>
<blockquote>"Q. . . . This was on Friday? A. Friday.</blockquote>
<blockquote>"Q. December 20th? A. Yes.</blockquote>
<blockquote>"Q. And was anything else said with respect to making a telephone call? A. Mr. Pike [<i>sic</i>] and the other officer both told me that when I had made a statement and cooperated with them that they would see to it that as soon as I got booked I could call my wife.</blockquote>
<blockquote>"Q. Well, that was the night before you were told that, wasn't it? A. I was told that the next day too, several times.</blockquote>
<blockquote>"Q. Who were the officers that were with you? A. Oh, not Mr. Pike. Mr. Cockburn and Mr. Peck, I believe.</blockquote>
<blockquote>"Q. In any event, Mr. Haynes, did you soon after that give them a statement? A. Well, not readily.</blockquote>
<blockquote>"Q. Did you give them a statement? A. Yes."</blockquote>
<p>The transcribed statement itself discloses that early in the interrogation Haynes asked whether he might at least talk to the prosecutor before proceeding further. He was told: "We just want to get this down for our records, and then we will go to the prosecutor's office and he will ask the same questions that I am."</p>
<p>Whatever contradiction of Haynes' account of his interrogation on the night of his arrest might be found in the testimony of Lieutenant Wakeley and Detective Pike, his explicit description of the circumstances surrounding his questioning and the taking by Detectives Peck and Cockburn of the challenged confession on the following day remains testimonially undisputed. Though he took the stand at trial, Detective Cockburn did not deny that he or Detective Peck had told the petitioner that he might <span class="star-pagination">*510</span> call his wife only if he "cooperated" and gave the police a statement. Cockburn said merely that he could not "remember" whether Haynes had asked to call his wife. He conceded that the petitioner "could have" made such a request. No legal alchemy can transmute such wholly equivocal testimony into a denial or refutation of the petitioner's specific recitation of events. Detective Peck did not testify and no other evidence was presented to contradict the petitioner's testimony, either as part of the prosecution's case in chief or, even more importantly, by way of rebuttal subsequent to the petitioner's testimony. We cannot but attribute significance to the failure of the State, after listening to the petitioner's direct and explicit testimony, to attempt to contradict that crucial evidence; this testimonial void is the more meaningful in light of the availability and willing cooperation of the policemen who, if honestly able to do so, could have readily denied the defendant's claims. Similarly, no evidence was offered to contradict in any way the petitioner's testimony that when first taken to the deputy prosecutor's office to sign the statement he had given to Detectives Peck and Cockburn he again requested permission to call his wife and was again refused.<sup>[7]</sup></p>
<p>Though the police were in possession of evidence more than adequate to justify his being charged without delay, it is uncontroverted that Haynes was not taken before a magistrate and granted a preliminary hearing until he had acceded to demands that he give and sign the written statement. Nor is there any indication in the record that prior to signing the written confession, or even thereafter, <span class="star-pagination">*511</span> Haynes was advised by authorities of his right to remain silent, warned that his answers might be used against him, or told of his rights respecting consultation with an attorney.</p>
<p>In addition, there is no contradiction of Haynes' testimony that even after he submitted and supplied the written confession used at trial, the police nonetheless continued the incommunicado detention while persisting in efforts to secure still another signature on another statement.<sup>[8]</sup> Upon being returned to the deputy prosecutor's office during the week following his arrest and while still being held incommunicado, the petitioner was again asked to sign the second statement which he had given there several days earlier. He refused to do so, he said, because, as he then told the deputy prosecutor, "all the promises of all the officers I had talked to had not been fulfilled and I had not been able to call my wife and I would sign nothing under any conditions until I was allowed to call my wife to see about legal counsel." The State offered no evidence to rebut this testimony.<sup>[9]</sup> Similarly uncontradicted is Haynes' testimony that it was not until <span class="star-pagination">*512</span> during or after this second interview with the prosecutor on the Tuesday or ThursdayHaynes could not be quite certainbut, in any event, some five or seven days after his arrest, that he was first allowed to call his wife.</p>
<p>The contested written confession itself contains the following exchange:</p>
<blockquote>"Q. Have we made you any threats or promises? A. No.</blockquote>
<blockquote>"Q. Has [<i>sic</i>] any police officers made you any promises or threats? A. Noexcept that the Lieutenant promised me that as soon as I was booked that I could call my wife.</blockquote>
<blockquote>"Q. You are being held for investigationyou haven't been booked yet. When you are, you will be able to phone your wife."</blockquote>
<p>The State argues that the quoted answers to the first two of these questions conclusively negative existence of coercion or inducement on the part of the police. The statement bears no such reading, however. The questions on their face disclose that the petitioner was told that "booking" was a prerequisite to calling his wife, and "booking" must mean booking on a charge of robbery. Since the police already had enough evidence to warrant charging the petitioner with the robberythey had the petitioner's prior oral admissions, the circumstances surrounding his arrest, and his identification by witnessesthe only fair inference to be drawn under all the circumstances is that he would not be booked on the robbery charge until the police had secured the additional evidence they desired, the signed statement for which they were pressing. The quoted portions of the signed confession thus support the petitioner's version of events; under any view, they offer no viable or reliable contradiction.</p>
<p>Even were it otherwise, there would be substantial doubt as to the probative effect to be accorded recitations <span class="star-pagination">*513</span> in the challenged confession that it was not involuntarily induced. Cf. <i>Haley</i> v. <i>Ohio,</i> <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/#601" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596, 601</a></span> (opinion of MR. JUSTICE DOUGLAS). It would be anomalous, indeed, if such a statement, contained within the very document asserted to have been obtained by use of impermissible coercive pressures, was itself enough to create an evidentiary conflict precluding this Court's effective review of the constitutional issue. Common sense dictates the conclusion that if the authorities were successful in compelling the totally incriminating confession of guilt, the very issue for determination, they would have little, if any, trouble securing the self-contained concession of voluntariness. Certainly, we cannot accord any conclusive import to such an admission, particularly when, as here, it is immediately followed by recitations supporting the petitioner's version of events.</p>
<p></p>
<h2>III.</h2>
<p>The uncontroverted portions of the record thus disclose that the petitioner's written confession was obtained in an atmosphere of substantial coercion and inducement created by statements and actions of state authorities. We have only recently held again that a confession obtained by police through the use of threats is violative of due process and that "the question in each case is whether the defendant's will was overborne at the time he confessed," <i>Lynumn</i> v. <i>Illinois,</i> <span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/#534" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528, 534</a></span>. "In short, the true test of admissibility is that the confession is made freely, voluntarily and without compulsion or inducement of any sort." <i>Wilson</i> v. <i>United States,</i> <span class="citation" data-id="94454"><a href="/opinion/94454/wilson-v-united-states/#623" aria-description="Citation for case: Wilson v. United States">162 U. S. 613, 623</a></span>. See also <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">168 U. S. 532</a></span>. And, of course, whether the confession was obtained by coercion or improper inducement can be determined only by an examination of all of the attendant circumstances. See, <i>e. g., </i><i>Leyra</i> <span class="star-pagination">*514</span> v. <i>Denno,</i> <span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/#558" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556, 558</a></span>.<sup>[10]</sup> Haynes' undisputed testimony as to the making and signing of the challenged confession used against him at trial permits no doubt that it was obtained under a totality of circumstances evidencing an involuntary written admission of guilt.</p>
<p>Here, as in <i><span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/" aria-description="Citation for case: Lynumn v. Illinois">Lynumn, supra,</a></span></i> the petitioner was alone in the hands of the police, with no one to advise or aid him, and he had "no reason not to believe that the police had ample power to carry out their threats," <span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/#534" aria-description="Citation for case: Lynumn v. Illinois">372 U. S., at 534</a></span>, to continue, for a much longer period if need be, the incommunicado detentionas in fact was actually done. Neither the petitioner's prior contacts with the authorities nor the fact that he previously had made incriminating oral admissions negatives the existence and effectiveness of the coercive tactics used in securing the written confession introduced at trial. The petitioner at first resisted making a written statement and gave in only after consistent denials of his requests to call his wife, and the conditioning of such outside contact upon his accession to police demands. Confronted with the express threat of continued incommunicado detention and induced by the promise of communication with and access to family, Haynes understandably chose to make and sign the damning written statement; given the unfair and inherently coercive context in which made, that choice cannot be said to be the voluntary product of a free and unconstrained will, as required by the Fourteenth Amendment.</p>
<p>We cannot blind ourselves to what experience unmistakably teaches: that even apart from the express threat, the basic techniques present herethe secret and incommunicado detention and interrogationare devices adapted and used to extort confessions from suspects. Of course, detection and solution of crime is, at best, a difficult <span class="star-pagination">*515</span> and arduous task requiring determination and persistence on the part of all responsible officers charged with the duty of law enforcement. And, certainly, we do not mean to suggest that all interrogation of witnesses and suspects is impermissible. Such questioning is undoubtedly an essential tool in effective law enforcement. The line between proper and permissible police conduct and techniques and methods offensive to due process is, at best, a difficult one to draw, particularly in cases such as this where it is necessary to make fine judgments as to the effect of psychologically coercive pressures and inducements on the mind and will of an accused. But we cannot escape the demands of judging or of making the difficult appraisals inherent in determining whether constitutional rights have been violated. We are here impelled to the conclusion, from all of the facts presented, that the bounds of due process have been exceeded.</p>
<p></p>
<h2>IV.</h2>
<p>Our conclusion is in no way foreclosed, as the State contends, by the fact that the state trial judge or the jury may have reached a different result on this issue.</p>
<p>It is well settled that the duty of constitutional adjudication resting upon this Court requires that the question whether the Due Process Clause of the Fourteenth Amendment has been violated by admission into evidence of a coerced confession be the subject of an <i>independent</i> determination here, see, <i>e. g., </i><i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/#147" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143, 147-148</a></span>; "we cannot escape the responsibility of making our own examination of the record," <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#316" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 316</a></span>. While, for purposes of review in this Court, the determination of the trial judge or of the jury will ordinarily be taken to resolve evidentiary conflicts and may be entitled to some weight even with respect to the ultimate conclusion on the crucial issue of voluntariness, we cannot avoid our responsibilities <span class="star-pagination">*516</span> by permitting ourselves to be "completely bound by state court determination of any issue essential to decision of a claim of federal right, else federal law could be frustrated by distorted fact finding." <i>Stein</i> v. <i>New York,</i> <span class="citation" data-id="9420977"><a href="/opinion/105149/stein-v-new-york/#181" aria-description="Citation for case: Stein v. New York">346 U. S. 156, 181</a></span>. As state courts are, in instances such as this, charged with the primary responsibility of protecting basic and essential rights, we accord an appropriate and substantial effect to their resolutions of conflicts in evidence as to the occurrence or nonoccurrence of factual events and happenings. This is particularly apposite because the trial judge and jury are closest to the trial scene and thus afforded the best opportunity to evaluate contradictory testimony. But, as declared in <i>Ward</i> v. <i>Texas,</i> <span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/#550" aria-description="Citation for case: Ward v. Texas">316 U. S. 547, 550</a></span>, "when, as in this case, the question is properly raised as to whether a defendant has been denied the due process of law . . . we cannot be precluded by the verdict of a jury from determining whether the circumstances under which the confession was made were such that its admission in evidence amounts to a denial of due process." To the same effect, see, <i>e. g., </i><i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span>; <i>Thomas</i> v. <i>Arizona,</i> <span class="citation" data-id="105683"><a href="/opinion/105683/thomas-v-arizona/#393" aria-description="Citation for case: Thomas v. Arizona">356 U. S. 390, 393</a></span>; <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#562" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560, 562, 568</a></span>; <i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/#147" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143, 147-148</a></span>; <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#237" aria-description="Citation for case: Lisenba v. California">314 U. S. 219, 237-238</a></span>; <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#228" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227, 228</a></span>.</p>
<p>Beyond even the compelling nature of our precedents, however, there is here still another reason for refusing to consider the present inquiry foreclosed by the verdict of the jury to which the issue of voluntariness of the confession was submitted. The jury was instructed, in effect, not to consider as relevant on the issue of voluntariness of the confession the fact that a defendant is not reminded that he is under arrest, that he is not cautioned that he may remain silent, that he is not warned that his answers may be used against him, or that he is not advised that <span class="star-pagination">*517</span> he is entitled to counsel.<sup>[11]</sup> Whatever independent consequence these factors may otherwise have, they are unquestionably attendant circumstances which the accused is entitled to have appropriately considered in determining voluntariness and admissibility of his confession.<sup>[12]</sup></p>
<p>In addition, the trial court instructed in terms of a Washington statute which permits consideration of a corroborated confession "made under inducement" and excepts only confessions "made under the influence of fear produced by threats."<sup>[13]</sup> It seems reasonably clear from this portion of the instructions that the jury may well have been misled as to the requisite constitutional standard, notwithstanding the apparent propriety of other portions of the instructions. Given the fact that the jury did no more than return a general verdict of guilty, we obviously have no way of knowing whether it found the confession to be voluntary and admissible or not. Because <span class="star-pagination">*518</span> there was sufficient other evidence to sustain the verdict, the jury may have found the defendant guilty even though it rejected the confession as involuntary; alternatively, the jury may have based its finding of guilt on the confession, reasoning, under the questionable instructions and the Washington statute, that the confession was admissible as voluntary, even though improperly induced, because it was corroborated by the other evidence. Although, for the reasons indicated, the Washington statute and the quoted instructions raise a serious and substantial question whether a proper constitutional standard was applied by the jury, we need not rely on the imperfections in the instructions as a separate ground of reversal. We think it clear, however, that these imperfections are entirely sufficient to preclude any dependence we might otherwise place on the jury verdict as settling the issue of voluntariness here.</p>
<p></p>
<h2>V.</h2>
<p>In reaching the conclusion which we do, we are not unmindful of substantial independent evidence tending to demonstrate the guilt of the petitioner. As was said in <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534</a></span>, 541:</p>
<blockquote>"Indeed, in many of the cases in which the command of the Due Process Clause has compelled us to reverse state convictions involving the use of confessions obtained by impermissible methods, independent corroborating evidence left little doubt of the truth of what the defendant had confessed. Despite such verification, confessions were found to be the product of constitutionally impermissible methods in their inducement."</blockquote>
<p>Of course, we neither express nor suggest a view with regard to the ultimate guilt or innocence of the petitioner here; that is for a jury to decide on a new trial free of <span class="star-pagination">*519</span> constitutional infirmity, which the State is at liberty to order.</p>
<p>This case illustrates a particular facet of police utilization of improper methods. While history amply shows that confessions have often been extorted to save law enforcement officials the trouble and effort of obtaining valid and independent evidence, the coercive devices used here were designed to obtain admissions which would incontrovertibly complete a case in which there had already been obtained, by proper investigative efforts, competent evidence sufficient to sustain a conviction. The procedures here are no less constitutionally impermissible, and perhaps more unwarranted because so unnecessary. There is no reasonable or rational basis for claiming that the oppressive and unfair methods utilized were in any way essential to the detection or solution of the crime or to the protection of the public. The claim, so often made in the context of coerced confession cases, that the devices employed by the authorities were requisite to solution of the crime and successful prosecution of the guilty party cannot here be made.</p>
<p>Official overzealousness of the type which vitiates the petitioner's conviction below has only deleterious effects. Here it has put the State to the substantial additional expense of prosecuting the case through the appellate courts and, now, will require even a greater expenditure in the event of retrial, as is likely. But it is the deprivation of the protected rights themselves which is fundamental and the most regrettable, not only because of the effect on the individual defendant, but because of the effect on our system of law and justice. Whether there is involved the brutal "third degree," or the more subtle, but no less offensive, methods here obtaining, official misconduct cannot but breed disrespect for law, as well as for those charged with its enforcement.</p>
<p><span class="star-pagination">*520</span> The judgment below is vacated and the case is remanded to the Supreme Court of Washington for further proceedings not inconsistent herewith.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE CLARK, with whom MR. JUSTICE HARLAN, MR. JUSTICE STEWART and MR. JUSTICE WHITE join, dissenting.</p>
<p>On December 19, 1957, at 9:05 p. m., a report was received by the Spokane Police Station that a filling station robbery was in progress in a certain area of the city. The report was broadcast to police cars working in the area. Twenty-five minutes later uniformed officers riding in a police car near the scene of the reported robbery observed petitioner walking down the street. As they approached him he went into the yard of a home in the vicinity. The police drove up and called to petitioner, who was questioned for a moment by one of the officers. Petitioner indicated that "he lived there" and, after talking with the officers, walked onto the porch of the house and began fumbling with the screen door as if to unlock it. The officer remained at the curb observing petitioner, who in a few moments returned to the car and spontaneously exclaimed to the officers, "You got me, let's go." He was placed in the police car, admitted the robbery to the officers and, as they drove to the filling station, identified it as the place he had robbed. He was taken to the police station where he arrived within 20 minutes of his arrest and made a second oral confession to Lieutenant Wakeley, who was in charge of the detective office on the 4 o'clock to midnight shift. This confession was related by the lieutenant at the trial, without objection, in the following testimony:</p>
<blockquote>"A. [By Lt. Wakeley.] He said they decided to hold up a place so they drove around to find some <span class="star-pagination">*521</span> place that didn't seem to have any customers and they didn't know the streets, didn't know the town very well. They said they were out where they found the car. They drove by and saw a service station which didn't seem to have any business, so they parked the car in the alley and walked into the service station, and Raymond said that he told the man it was a holdup and his brother stood behind the man and he got the money from the service station operator. He didn't think his brother got any of it. After they held up the place they ran out the door and he ran down the side street, not directly toward the car, down around toward the end of the block and come [<i>sic</i>] back down the alley and as he was approaching the car he saw a police officer had his brother in custody. So he turned and ran north about two blocks and then turned and went west about three blocks before a prowl car came along and they stopped and talked to him and asked him where he was going. He said he was going home and he turned and walked up onto a porch. He stood on the porch and he said the prowl car sat out there in the street, didn't move, so he thought well, I might as well give up. So he went back and told them he was the man they were looking for."</blockquote>
<p>Thus within an hour and 20 minutes after his surrender petitioner had made two oral confessionsboth admitted into evidence without objectionidentical in relevant details to the written confession made the following day which the Court finds coerced. In light of the circumstances surrounding petitioner's arrest and confession, I believe the Court's reversal to be an abrupt departure from the rule laid down in the cases of this Court and an enlargement of the requirements heretofore visited upon state courts in confession cases. I therefore dissent.</p>
<p><span class="star-pagination">*522</span> The petitioner is neither youthful in age (though his exact age is not shown by the record) nor lacking in experience in law breaking. He is married and was a skilled sheet-metal worker temporarily unemployed. Some indication of his approximate age is given by the facts that his wife had been employed for some 14 years by the same employer, and that 11 years prior to the trial he had his first brush with the law, <i>i. e.,</i> drunken driving, resisting arrest and being without a driver's license. Further, in 1949 he was convicted of breaking and entering, and in 1950 of robbery. During the same year he pleaded guilty to breaking jail and to "taking a car." He had not only served time but had been on parole for two years, making regular visits to parole officers to whom he was assigned. He cannot, therefore, be placed in the category of those types of people with whom the Court's cases in this area have ordinarily dealt, such as the mentally subnormal accused, <i>Fikes</i> v. <i>Alabama,</i> <span class="citation" data-id="9421354"><a href="/opinion/105436/fikes-v-alabama/" aria-description="Citation for case: Fikes v. Alabama">352 U. S. 191</a></span> (1957); <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span> (1958), and <i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/" aria-description="Citation for case: Reck v. Pate">367 U. S. 433</a></span> (1961); the youthful offender, such as <i>Haley</i> v. <i>Ohio,</i> <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596</a></span> (1948), and <i>Gallegos</i> v. <i>Colorado,</i> <span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/" aria-description="Citation for case: Gallegos v. Colorado">370 U. S. 49</a></span> (1962); or the naive and impressionable defendant, such as <i>Lynumn</i> v. <i>Illinois,</i> <span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528</a></span> (1963). On the contrary, he is a mature adult who appears, from his testimony at the trial, to be of at least average intelligence and who is neither a stranger to police techniques and custodial procedures nor unaware of his rights on arrest. Thus the Court's reliance on <i>Lynumn</i> v. <i><span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/" aria-description="Citation for case: Lynumn v. Illinois">Illinois, supra,</a></span></i><sup></sup>[1] is completely misplaced.</p>
<p><span class="star-pagination">*523</span> I do not say that only the young, the weak and the mentally disturbed are susceptible to coercion, but only that these factors have ordinarily been involved in coerced confession cases and have been consistently regarded by the Court as important circumstances in the determination as to whether a confession was voluntarily made. Along with circumstances related to the petitioner, of course, the determination of coercion requires examination of the conduct of the police and the environment in which interrogation and confession occurred. We have long recognized that coercion need not be based upon the physical torture involved in <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936). But here there is no contention by the petitioner either of physical abuse or of the more sophisticated techniques associated with police coercive practices. There was no extended or repeated interrogation,<sup>[2]</sup> no deprivation of sleep or food,<sup>[3]</sup> no use of psychiatric techniques.<sup>[4]</sup> Further, there were no external circumstances such as threat of mob violence<sup>[5]</sup> furnishing an atmosphere tending to subvert petitioner's rationality and free will.</p>
<p>I cannot condone the conduct of the police in holding the petitioner incommunicado, but of course we have no supervisory power over state courts. The question under the Fourteenth Amendment is whether the will of the accused is so overborne at the time of the confession that his statement is not "the product of a rational intellect and a free will," <i>Reck</i> v. <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/#440" aria-description="Citation for case: Reck v. Pate"><i>Pate, supra,</i> at 440</a></span>, and its determination "is one on which we must make an independent <span class="star-pagination">*524</span> determination on the undisputed facts." <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#404" aria-description="Citation for case: Malinski v. New York">324 U. S. 401, 404</a></span> (1945), citing <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">314 U. S. 219</a></span> (1941), and <i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span> (1944). We have held that the fact that one has been denied consultation with an attorney, <i>Cicenia</i> v. <i>Lagay,</i> <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">357 U. S. 504</a></span> (1958), <i>Crooker</i> v. <i>California,</i> <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">357 U. S. 433</a></span> (1958), was not in itself controlling in such cases. Further, not even the fact that one is "held incommunicado, is subjected to questioning by officers for long periods, and deprived of the advice of counsel," without a showing that he had "so lost his freedom of action" that the confession was not his own, requires a reversal under the Fourteenth Amendment. <i>Lisenba</i> v. <i>California, supra,</i> at 240-241. Finally, the fact that police officers violated state statutes in their treatment of the petitioner does "not furnish an answer" to the question whether a confession was voluntarily made. <i>Id.,</i> at 235; see <i>Gallegos</i> v. <i>Nebraska,</i> <span class="citation" data-id="9420632"><a href="/opinion/104933/gallegos-v-nebraska/" aria-description="Citation for case: Gallegos v. Nebraska">342 U. S. 55</a></span> (1951).</p>
<p>The Court's reversal here must be based upon the fact that, on the day after petitioner's arrest, when he signed the written confession at issue, he was told that after he made a statement and was booked he could call his wife. As to his testimony relating to the evening of his arrest, it is certainly disputed. Petitioner testified that he asked Detective Pike if he could call his wife, but Detective Pike testified that he did not even talk to petitioner. Lieutenant Wakeley testified unequivocally that petitioner made no such requests to him during their conversation, though he could not recall whether such requests were made "at any time that night."<sup>[6]</sup></p>
<p><span class="star-pagination">*525</span> The Court concludes, then, that the police, by holding petitioner incommunicado and telling him that he could call his wife after he made a statement and was booked, wrung from him a confession he would not otherwise have made, a confession which was not the product of a free will. In <i>Crooker</i> v. <i>California, supra,</i> at 436, however, we found no coercion or inducement, despite the fact that the petitioner's repeated requests for an attorney were denied and he "was told that `after [the] investigation was concluded he could call an attorney.' "</p>
<p>In light of petitioner's age, intelligence and experience with the police, in light of the comparative absence of any coercive circumstances, and in light of the fact that petitioner never, from the time of his arrest, evidenced a will to deny his guilt, I must conclude that his written confession was not involuntary. I find no support in any of the 33 cases decided on the question by this Court for a contrary conclusion. Therefore, I would affirm the judgment before us.</p>
<h2>NOTES</h2>
<p>[1]  Haynes makes no claim that he was physically abused, deprived of food or rest, or subjected to uninterrupted questioning for prolonged periods.</p>
<p>[2]  The petitioner's brother, Keith Haynes, had been arrested a few minutes earlier. Though also charged with, and convicted of, participation in the robbery of the service station, he does not seek review of his conviction here.</p>
<p>[3]  Apparently recognizing the questionable nature of such a practice, the Spokane police, we are told, have since abandoned use of the "small book" and the attendant restrictive practices.</p>
<p>[4]  The written confession appears to indicate on its face that it was signed shortly before 2 p. m. on December 20, about 16 1/4 hours after Haynes was arrested. The State asserts in its brief, however, that the total time of detention prior to signing of the confession was "17 to 19" hours. We assume, for purposes here, that the 16-hour period is sufficiently accurate.</p>
<p>[5]  Washington has since revised its rules of practice to provide for a preliminary hearing by the trial court, out of the presence of the jury, on the issue of voluntariness of a confession. See <span class="citation" data-id="9539685"><a href="/opinion/1156234/state-v-haynes/#720" aria-description="Citation for case: State v. Haynes">58 Wash. 2d, at 720</a></span>, <span class="citation" data-id="9539685"><a href="/opinion/1156234/state-v-haynes/#937" aria-description="Citation for case: State v. Haynes">364 P. 2d, at 937</a></span>, and Rules of Pleading, Practice and Procedure, Wash. Rev. Code, Rule 101.20W, Vol. O, as amended, effective January 2, 1961.</p>
<p>[6]  There is no indication that she was actually so notified. In fact, the petitioner's wife telephoned police at about noon on the day following the robbery, but was refused any information beyond the fact that her husband was being held. Though she identified herself and asked specifically why her husband was in jail, she was told simply "to get the morning paper and read it."</p>
<p>[7]  The petitioner's incommunicado detention was in contravention of an explicit Washington statute, Wash. Rev. Code, § 9.33.020 (5), which prohibits and makes it a misdemeanor for police to "refuse permission to [an] . . . arrested person to communicate with his friends or with an attorney" when the refusal has as its purpose the obtaining of a confession.</p>
<p>[8]  While occurring after completion of the signed confession here challenged, such action not only tends to bear out petitioner's version of what happened earlier but displays and confirms an official disregard by police of state law, see note 7, <i>supra,</i> and of the basic rights of the defendant. See <i>Haley</i> v. <i>Ohio,</i> <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/#600" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596, 600</a></span> (opinion of MR. JUSTICE DOUGLAS). The police "were rather concerned primarily with securing a statement from defendant on which they could convict him. The undeviating intent of the officers to extract a confession from petitioner is therefore patent. When such an intent is shown, this Court has held that the confession obtained must be examined with the most careful scrutiny . . . ." <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#324" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 324</a></span>.</p>
<p>[9]  Though the deputy prosecutor himself appeared as a witness for the State at the trial, his testimony was in no way directed to this statement made in his office or the attendant circumstances and he was not recalled to the stand after Haynes testified so that he might controvert the petitioner's version of events.</p>
<p>[10]  See also <i>Fikes</i> v. <i>Alabama,</i> <span class="citation" data-id="9421354"><a href="/opinion/105436/fikes-v-alabama/#197" aria-description="Citation for case: Fikes v. Alabama">352 U. S. 191, 197-198</a></span>; <i>Gallegos</i> v. <i>Nebraska,</i> <span class="citation" data-id="9420632"><a href="/opinion/104933/gallegos-v-nebraska/#65" aria-description="Citation for case: Gallegos v. Nebraska">342 U. S. 55, 65</a></span> (opinion of Mr. Justice Reed).</p>
<p>[11]  The trial court told the jury:
</p>
<p>"And in this connection, I further instruct you that a confession or admission of a defendant is not rendered involuntary because he is not at the time of making the same reminded that he was under arrest, or that he was not obliged to reply, or that his answers would be used against him, or that he was entitled to be represented by counsel."</p>
<p>That the jury was to take this as precluding consideration of the cited factors is evidenced by the immediately succeeding instruction which advised that it <i>should</i> consider a denial of communication with friends or an attorney in connection with determining whether the written confession was voluntary or not.</p>
<p>[12]  See note 10, <i>supra.</i></p>
<p>[13]  The instruction commenced:
</p>
<p>"By statute of the State of Washington, it is provided:</p>
<p>" `The confession of a defendant made under inducement, with all the circumstances, may be given as evidence against him, except when made under the influence of fear produced by threats; but a confession made under inducement is not sufficient to warrant a conviction without corroborating testimony.' "</p>
<p>[1]  In <i>Lynumn</i> v. <i>Illinois,</i> <span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528</a></span> (1963), the petitioner was a woman who "had no previous experience with the criminal law, and had no reason not to believe that the police had ample power to carry out their threats." <span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/#534" aria-description="Citation for case: Lynumn v. Illinois"><i>Id.,</i> at 534</a></span>. She confessed after the police told her that if she did not cooperate she would be imprisoned for 10 years, her children would be taken away and she would be deprived of state aid for them.</p>
<p>[2]  See <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span> (1959); <i>Ward</i> v. <i>Texas.</i> <span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/" aria-description="Citation for case: Ward v. Texas">316 U. S. 547</a></span> (1942); <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span> (1940).</p>
<p>[3]  See <i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/" aria-description="Citation for case: Reck v. Pate">367 U. S. 433</a></span> (1961); <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span> (1958).</p>
<p>[4]  See <i>Leyra</i> v. <i>Denno,</i> <span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556</a></span> (1954); cf. <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span> (1945).</p>
<p>[5]  See <i>Payne</i> v. <i><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">Arkansas</a></span>,</i> note 3, <i>supra; Chambers</i> v. <i><span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">Florida</a></span>,</i> note 2, <i>supra.</i></p>
<p>[6]  Lieutenant Wakeley testified as follows:
</p>
<p>"Q. Did Raymond Haynes at any time during that conversation [when he was interrogated] ask permission to make a telephone call to his wife? A. Not during the conversation.</p>
<p>"Q. Well, at any time that night? A. He might have asked afterward, after I got through talking to him. He wanted to know if his wife would be notified. I told him we would notify her that he was being held.</p>
<p>"Q. Did he ask permission to make a phone call himself to his wife? A. He may have. I don't remember exactly whether he asked or whether we wouldn't notify his wife.</p>
<p>"Q. Did he say anything to you, Lieutenant Wakeley, if you remember in substance that he wanted to call his wife so that she could get a lawyer? A. No, I don't remember that."</p>

</div>
```

---
