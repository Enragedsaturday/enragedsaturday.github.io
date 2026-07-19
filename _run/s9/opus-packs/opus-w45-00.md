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

## GROUP: content/cases/James v. Illinois.md  (`case`, 5 assertions)

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
{"assertion_id": "e00f7aa3ac0a1526", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "493 U.S. 307 (1990)", "court": "U.S. Supreme Court", "neutral_cite": "1990 U.S. LEXIS 335", "official_citation_present": true, "parallel_cite": "110 S. Ct. 648; 107 L. Ed. 2d 676; 58 U.S.L.W. 4115", "title": "James v. Illinois", "year": "1990"}}
{"assertion_id": "333d2453e5e12f87", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The impeachment exception to the exclusionary rule is confined to the defendant's own testimony; the prosecution may not use illegally obtained evidence to impeach the testimony of other defense witnesses.", "title": "James v. Illinois"}}
{"assertion_id": "9e0f99ed17d119af", "dimension": "support", "kind": "home_role", "locator": {"home": "Fruits & Attenuation"}, "payload": {"home": "Fruits & Attenuation", "role": "Key — Limiting (impeachment exception)", "title": "James v. Illinois"}}
{"assertion_id": "9dedf0859aea49a3", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "James v. Illinois"}}
{"assertion_id": "cb47e40fa3b9bda7", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1990-01-10", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "James v. Illinois", "field_i_validity": "good_law", "scope_note": "Caps the impeachment exception at the defendant's own testimony; good law.", "title": "James v. Illinois", "varies_by_point": "false"}}
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

## GROUP: content/cases/Johnson v. Glick.md  (`case`, 5 assertions)

### content_page

```
---
title: Johnson v. Glick
type: case
citation: "481 F.2d 1028 (1973)"
parallel_cite: ""
neutral_cite: ""
court: 2d Cir. 1973
court_level: coa
circuit: ca2
year: 1973
date_decided: 1973-06-29
docket: "No. 845, Docket 72-2428"
authority_weight: "Binding in-circuit — 2d Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/8903545/johnson-v-glick/"
  cluster_id: 8903545
  opinion_id: null
  identity_checked: true
lake:
  record_id: Johnson v. Glick
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Use of Force]]"
    role: Key
related:
  - "[[Use of Force]]"
  - "[[Graham v. Connor]]"
tags:
  - case
  - fourth-amendment
  - use-of-force
  - excessive-force
  - substantive-due-process
  - pretrial-detainee
  - section-1983
holding: "Not every use of force by a custodial officer is a constitutional violation; whether the line is crossed depends on the need for force, the relationship between the need and the amount used, the extent of injury, and whether force was applied in good faith to maintain discipline or maliciously to cause harm — the pre-Graham due-process test for excessive force."
---

# Johnson v. Glick

*481 F.2d 1028 (2d Cir. 1973)* (No. 72-2428) · U.S. Court of Appeals for the Second Circuit · **Binding in-circuit — 2d Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 8903545 → majority opinion 8890588 (481 F.2d 1028, Friendly, J., decided 1973-06-29); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Australia Johnson, a pretrial detainee at a Manhattan house of detention, alleged that a corrections officer, angered during a disturbance, struck him in the head and threatened him, causing injury. He sued the warden and the officer under § 1983, and the district court dismissed the complaint. On appeal, Judge Friendly confronted the question of what constitutional standard governs a custodial officer's use of force against a detainee.

## Issue
By what standard does a court decide whether a custodial officer's use of force against a detainee is so excessive as to violate the Constitution and support a § 1983 claim.

## Rule
Grounding the claim in substantive due process rather than the Fourth or Eighth Amendments, Judge Friendly announced a multi-factor test that became the template for excessive-force analysis: "In determining whether the constitutional line has been crossed, a court must look to such factors as the need for the application of force, the relationship between the need and the amount of force that was used, the extent of injury inflicted, and whether force was applied in a good faith effort to maintain or restore discipline or maliciously and sadistically for the very purpose of causing harm." — 481 F.2d at 1033.

## Application
Not every push or shove, even one that later seems unnecessary in the calm of a courtroom, offends the Constitution; managing detainees may justify some intentional force. But a blow inflicted maliciously, without penological need, does. Reading the [[Common Legal Terms#pro-se|pro se]] complaint generously, the court held it stated a claim against the officer who allegedly struck Johnson, while affirming dismissal against the warden, who could not be liable under § 1983 on a [[Common Legal Terms#respondeat-superior|respondeat superior]] theory absent personal involvement.

## Conclusion
Dismissal was **reversed** as to the officer and **affirmed** as to the warden; the case was [[Reading and Citing Cases#on-remand|remanded]]. Friendly, J., wrote for the panel.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Johnson v. Glick*'s four-factor test was the dominant excessive-force standard for a generation, but *[[Graham v. Connor]]* (1989) held that force claims arising during an arrest, investigatory stop, or other seizure are governed by the Fourth Amendment's objective-reasonableness standard — not *Glick*'s substantive-due-process test — and criticized importing *Glick*'s "malicious and sadistic" element into that context. *Glick*'s approach continued to inform the analysis for pretrial detainees until the standard there was itself recalibrated by *[[Kingsley v. Hendrickson]]* (2015).

## Appears on
- [[Use of Force]] — *Key*

## Sources
- [*Johnson v. Glick*, 481 F.2d 1028 (2d Cir. 1973)](https://www.courtlistener.com/opinion/8903545/johnson-v-glick/) — pinpoint: 1033 (majority; Friendly, J.); Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "44779f121fe653bd", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "481 F.2d 1028 (1973)", "court": "2d Cir. 1973", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Johnson v. Glick", "year": "1973"}}
{"assertion_id": "0bee2037c10601f0", "dimension": "support", "kind": "home_role", "locator": {"home": "Use of Force"}, "payload": {"home": "Use of Force", "role": "Key", "title": "Johnson v. Glick"}}
{"assertion_id": "4dba6add8992e24f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Not every use of force by a custodial officer is a constitutional violation; whether the line is crossed depends on the need for force, the relationship between the need and the amount used, the extent of injury, and whether force was applied in good faith to maintain discipline or maliciously to cause harm — the pre-Graham due-process test for excessive force.", "title": "Johnson v. Glick"}}
{"assertion_id": "3f29e3a95fd07efc", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Johnson v. Glick", "varies_by_point": "false"}}
{"assertion_id": "f917d84fef3d2f36", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 2d Cir.", "title": "Johnson v. Glick"}}
```

### lake record — Johnson v. Glick

```json
{
  "schema_version": "s2.v1",
  "record_id": "Johnson v. Glick",
  "status": "under_review",
  "identity": {
    "case_name": "Johnson v. Glick",
    "case_name_short": "Glick",
    "case_name_full": "Australia JOHNSON v. A. GLICK, Warden of Manhattan House of Detention for Men, 125 White Street, New York, N. Y. Employee-Officer John, 1765 Badge Number, Manhattan House of Detention for Men, 125 White Street, New York, N. Y.",
    "input_case_name": "Johnson v. Glick",
    "court": "2d Cir. 1973",
    "court_id": "ca2",
    "court_level": "coa",
    "circuit": "ca2",
    "state": null,
    "date_decided": "1973-06-29",
    "year": 1973,
    "docket": "No. 845, Docket 72-2428",
    "cluster_id": 8903545,
    "lead_opinion_id": 8890588,
    "sibling_ids": [],
    "absolute_url": "/opinion/8903545/johnson-v-glick/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "481 F.2d 1028",
      "volume": "481",
      "reporter": "F.2d",
      "page": "1028",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "481 F.2d 1028",
        "volume": "481",
        "reporter": "F.2d",
        "page": "1028",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "481 F.2d 1028",
    "official_selection": {
      "court_class": "state",
      "selected": "481 F.2d 1028",
      "reason": "selected_rank_3"
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
    "date_created": "2026-07-06T05:46:05Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:46:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:46:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:46:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:46:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "johnson-v-glick--8903545",
      "to_record_id": "Johnson v. Glick",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Johnson v. Glick

```
<opinion type="majority">
<author id="b1091-21">FRIENDLY, Circuit Judge:</author>
<p id="b1091-22">This appeal concerns an order of the District Court for the Southern District of New York dismissing a complaint under the Civil Rights Act, <span class="citation no-link">42 U.S.C. § 1983</span>, <span class="citation no-link">28 U.S.C. § 1343</span>(3), for failure to state a claim on which relief can be granted. The complaint was brought against the Warden of the Manhattan House of Detention for Men and a correction officer, described in the complaint only as Officer John, Badge No. 1765, but now identified as John Fuller; by plaintiff Australia Johnson, who had been held in the House of Detention prior to and during his trial in the state courts on felony charges. It alleged that, while plaintiff was being checked back into the House of Detention, Officer Fuller reprimanded Johnson and other men for a claimed failure to follow instructions; that when Johnson endeavored to explain that they were doing only what another officer had told them to do, Officer Fuller rushed into the holding cell, grabbed him by the collar and struck him twice on the head with something enclosed in the officer’s fist; that during this incident the officer <page-number citation-index="1" label="1030">*1030</page-number>threatened him, saying “I’ll kill you, old man, I’ll break you in half”; that Fuller than harassed Johnson by detaining him in the holding cell for two hours before returning him to his cell; that when Johnson requested medical attention, Fuller, who was called upon by another officer to escort Johnson to the jail doctor, instead held him for another two hours in another cell before permitting him to see the doctor; and that despite the “pain pills” given him by the doctor, Johnson has since “been having terrible pains in his head.”</p>
<p id="b1092-4">Recognizing that there were numerous decisions in other circuits that would seem to uphold the validity of the'complaint as against the officer, as well as one to the contrary, Judge Knapp nevertheless dismissed the complaint, saying “So far as I am aware no decision in this circuit requires such a conclusion, and it is one at which I would arrive only under constraint.” Although we realize that upholding this complaint may well lead to considerable further expansion of actions by state prisoners under <span class="citation no-link">42 U.S.C. § 1983</span>, so long as they may bring their civil rights complaints directly to federal courts without first presenting them to state courts,<footnotemark>1</footnotemark> we think the ruling was in error so far as the officer was concerned.</p>
<p id="b1092-5">The longest line of authority for the proposition that a complaint alleging an unprovoked attack on a prisoner by a state prison guard is within <span class="citation no-link">42 U.S.C. § 1983</span> comes from the Ninth Circuit. The first case in the line is Brown v. Brown, <span class="citation" data-id="273780"><a href="/opinion/273780/homer-ray-brown-v-edmund-g-brown-governor-state-of-california/" aria-description="Citation for case: Homer Ray Brown v. Edmund G. Brown, Governor, State of...">368 F.2d 992</a></span> (9 Cir. 1966), where, however, the complaint alleged other deprivations of civil rights.<footnotemark>2</footnotemark> This was followed by Dodd v. Spokane County, <span class="citation" data-id="279782"><a href="/opinion/279782/dodd-v-spokane-county/#333" aria-description="Citation for case: Dodd v. Spokane County">393 F.2d 330, 333-334</a></span> (9 Cir. 1968),</p>
<p id="b1092-8">although the complaint there alleged not brutality <em>simpliciter </em>but the administration of violence in an effort to cause Dodd to testify falsely in another’s criminal trial. Next came Wiltsie v. California Department of Corrections, <span class="citation" data-id="8880072"><a href="/opinion/8893681/wiltsie-v-california-department-of-corrections/" aria-description="Citation for case: Wiltsie v. California Department of Corrections">406 F.2d 515</a></span> (9 Cir. 1968). Although this was a case of beating pure and simple, the court, over Judge Chambers' dissent held it to be “indistinguishable from Brown v. Brown,” <em>supra. </em>To the same effect is Allison v. California Adult Authority, <span class="citation" data-id="287696"><a href="/opinion/287696/charles-allison-v-california-adult-authority/" aria-description="Citation for case: Charles Allison v. California Adult Authority">419 F.2d 822</a></span> (9 Cir. 1969), where the court followed <em><span class="citation" data-id="273780"><a href="/opinion/273780/homer-ray-brown-v-edmund-g-brown-governor-state-of-california/" aria-description="Citation for case: Homer Ray Brown v. Edmund G. Brown, Governor, State of...">Brown</a></span> </em>despite its recognition “that frivolous Civil Rights suits by prison inmates have become a matter of concern to district courts” and its belief that “Allison’s allegations of physical abuse stretch one’s credulity.”</p>
<p id="b1092-9">Several other circuits have reached the same result. Bethea v. Crouse, <span class="citation" data-id="9454967"><a href="/opinion/286950/oscar-bethea-v-sherman-h-crouse-warden-kansas-state-penitentiary-james/" aria-description="Citation for case: Oscar Bethea v. Sherman H. Crouse, Warden, Kansas State...">417 F.2d 504</a></span> (10 Cir. 1969); Collum v. Butler, <span class="citation" data-id="288499"><a href="/opinion/288499/curtis-collum-cross-appellee-v-frank-a-butler-james-hand-and-james/" aria-description="Citation for case: Curtis Collum, Cross-Appellee v. Frank A. Butler, James...">421 F.2d 1257</a></span> (7 Cir. 1970); Tolbert v. Bragan, <span class="citation" data-id="300228"><a href="/opinion/300228/george-tolbert-jr-v-warden-bragan/" aria-description="Citation for case: George Tolbert, Jr. v. Warden Bragan">451 F.2d 1020</a></span> (5th Cir. 1971) ; Howell v. Cataldi, <span class="citation" data-id="9458497"><a href="/opinion/304768/henry-howell-v-cataldi/" aria-description="Citation for case: Henry Howell v. Cataldi">464 F.2d 272</a></span> (3 Cir. 1972). Still others, though they apparently^have not yet been faced with precisely the issue posed by this complaint, have sustained civil rights actions involving closely related situations. Jenkins v. Averett, <span class="citation" data-id="9455514"><a href="/opinion/289671/robert-leon-jenkins-a-minor-by-his-mother-and-next-friend-roberta-b/" aria-description="Citation for case: Robert Leon Jenkins, a Minor, by His Mother and Next...">424 F.2d 1228</a></span> (4 Cir. 1970) (police brutality following arrest) ; Carter v. Carlson, <span class="citation" data-id="9457236"><a href="/opinion/298619/melvin-carter-v-john-r-carlson/" aria-description="Citation for case: Melvin Carter v. John R. Carlson">144 U.S.App.D.C. 388</a></span>, <span class="citation" data-id="9457236"><a href="/opinion/298619/melvin-carter-v-john-r-carlson/" aria-description="Citation for case: Melvin Carter v. John R. Carlson">447 F.2d 358</a></span> (1971) (same), rev’d on other grounds sub nom. District of Columbia <em>v. </em>Carter, <span class="citation" data-id="108654"><a href="/opinion/108654/district-of-columbia-v-carter/" aria-description="Citation for case: District of Columbia v. Carter">409 U.S. 418</a></span>, <span class="citation" data-id="108654"><a href="/opinion/108654/district-of-columbia-v-carter/" aria-description="Citation for case: District of Columbia v. Carter">93 S.Ct. 602</a></span>, <span class="citation" data-id="108654"><a href="/opinion/108654/district-of-columbia-v-carter/" aria-description="Citation for case: District of Columbia v. Carter"><em>34 </em>L.Ed.2d 613</a></span> (1973); Fitzke v. Shappell, <span class="citation" data-id="306421"><a href="/opinion/306421/robert-fitzke-and-joy-fitzke-v-barry-shappell-deputy-sheriff-and-elwin/" aria-description="Citation for case: Robert Fitzke and Joy Fitzke v. Barry Shappell, Deputy...">468 F.2d 1072</a></span> (6 Cir. 1972) (failure to provide medical care for prisoner). Only one circuit is clearly to the contrary, Cole v. Smith, <span class="citation" data-id="267690"><a href="/opinion/267690/robert-l-cole-v-lavern-smith-bernard-danner-and-allen-vogel/" aria-description="Citation for case: Robert L. Cole v. Lavern Smith, Bernard Danner and Allen...">344 F.2d 721</a></span> (8 Cir. 1965).</p>
<p id="b1092-12">Aside from the weight of all this authority, we are not so certain as was the <page-number citation-index="1" label="1031">*1031</page-number>district judge that the slate in this circuit is completely clean. In Martinez v. Mancusi, <span class="citation" data-id="297139"><a href="/opinion/297139/louis-martinez-v-vincent-r-mancusi-warden-attica-prison-dr-williams/" aria-description="Citation for case: Louis Martinez v. Vincent R. Mancusi, Warden, Attica...">443 F.2d 921</a></span> (2 Cir. 1970), we upheld a civil rights complaint against prison officials which was read to allege “a deliberate indifference to, and defiance of, the express instructions of the operating surgeons and the hospital attendants,” <span class="citation" data-id="297139"><a href="/opinion/297139/louis-martinez-v-vincent-r-mancusi-warden-attica-prison-dr-williams/#924" aria-description="Citation for case: Louis Martinez v. Vincent R. Mancusi, Warden, Attica...">443 F.2d at 924</a></span>; it seems hard to draw a satisfactory legal distinction between such conduct and the deliberate infliction of physical suffering in a non-medical setting. In Inmates of the Attica Correctional Facility v. Rockefeller, <span class="citation" data-id="9457668"><a href="/opinion/300646/inmates-of-the-attica-correctional-facility-v-nelson-rockefeller/#22" aria-description="Citation for case: Inmates of the Attica Correctional Facility v. Nelson...">453 F.2d 12, 22-24</a></span> (2 Cir. 1971), we granted preliminary injunctive relief where there had been a record of “beatings, physical abuse, torture, running of gauntlets, and similar cruelty.” While some emphasis was placed on the continuing and systematic acts of the correctional officers, this was said more in justification of issuance of an injunction than as a predicate for actionability. And, subsequent to Judge Knapp’s decision, we have stated in dictum:</p>
<blockquote id="b1093-5">We assume that brutal police conduct violates a right guaranteed by the due process clause of the Fourteenth Amendment.</blockquote>
<p id="b1093-6">Rosenberg v. Martin, <span class="citation" data-id="310933"><a href="/opinion/310933/jerome-rosenberg-v-raymond-v-martin/#526" aria-description="Citation for case: Jerome Rosenberg v. Raymond v. Martin">478 F.2d 520, 526</a></span> (2 Cir. 1973).</p>
<p id="b1093-7">The great weight of authority in favor of the assumption thus stated in <em><span class="citation" data-id="310933"><a href="/opinion/310933/jerome-rosenberg-v-raymond-v-martin/" aria-description="Citation for case: Jerome Rosenberg v. Raymond v. Martin">Rosenberg</a></span> </em>has not been accompanied by an equivalent amount of analysis. Many of 'the opinions, including our own in <em><span class="citation" data-id="297139"><a href="/opinion/297139/louis-martinez-v-vincent-r-mancusi-warden-attica-prison-dr-williams/" aria-description="Citation for case: Louis Martinez v. Vincent R. Mancusi, Warden, Attica...">Martinez</a></span> </em>and <em>Inmates, </em>rely on a passing reference to the “cruel and unusual punishment” clause of the Eighth Amendment. The most extensive judicial treatment of the subject,' Judge Aldisert’s opinion in Howell v. <span class="citation" data-id="9458497"><a href="/opinion/304768/henry-howell-v-cataldi/" aria-description="Citation for case: Henry Howell v. Cataldi">Cataldi, <em>supra, </em></a></span><span class="citation" data-id="9458497"><a href="/opinion/304768/henry-howell-v-cataldi/#280" aria-description="Citation for case: Henry Howell v. Cataldi">464 F.2d at 280-282</a></span>, likewise relies on that clause.</p>
<p id="b1093-8">A case like this, however, does not lie comfortably within the Eighth Amendment. The text:</p>
<p id="b1093-11">Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted suggests action taken, usually by a court, in carrying out a legislative authorization or command. The language, as is well known, is practically a verbatim copy of the tenth clause of the English Bill of Rights, 1 Wm. &amp; Mary, 2d sess., eh. 2 (1688), which, in turn, embodied a corresponding section of the Declaration of Rights that was a cornerstone of the settlement of the Glorious Revolution. Although George Mason, who drafted the similar clause in the Virginia Declaration of Rights, which was the more immediate progenitor of the Eighth Amendment, may have been mistaken in thinking that the provision was aimed merely at torturous rather than at excessive punishments,<footnotemark>3</footnotemark> there can be no disagreement that what sparked the English provision was the conduct of judges under James II. ^The background of our own Bill of Rights/ however,^ makes clear that the Eighth Amendment was intended to apply not only to the acts of judges but as a restraint on legislative action as wellH See In re Kemmler, <span class="citation" data-id="92834"><a href="/opinion/92834/in-re-kemmler/#446" aria-description="Citation for case: In Re Kemmler">136 U.S. 436, 446-447</a></span>, <span class="citation" data-id="92834"><a href="/opinion/92834/in-re-kemmler/" aria-description="Citation for case: In Re Kemmler">10 S.Ct. 930</a></span>, <span class="citation" data-id="92834"><a href="/opinion/92834/in-re-kemmler/" aria-description="Citation for case: In Re Kemmler">34 L.Ed. 519</a></span> (1890); Weems v. United States, <span class="citation" data-id="9418181"><a href="/opinion/97242/weems-v-united-states/#371" aria-description="Citation for case: Weems v. United States">217 U.S. 349, 371-373, 378-379</a></span>, <span class="citation" data-id="9418181"><a href="/opinion/97242/weems-v-united-states/" aria-description="Citation for case: Weems v. United States">30 S.Ct. 544</a></span>, <span class="citation" data-id="9418181"><a href="/opinion/97242/weems-v-united-states/" aria-description="Citation for case: Weems v. United States">54 L.Ed. 793</a></span> (1910); Furman v. Georgia, <span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/#266" aria-description="Citation for case: Furman v. Georgia">408 U.S. 238, 266-269</a></span>, <span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/" aria-description="Citation for case: Furman v. Georgia">92 S.Ct. 2726</a></span>, <span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/" aria-description="Citation for case: Furman v. Georgia">33 L.Ed.2d 346</a></span> (1972) (concurring opinion of Mr. Justice Brennan).<footnotemark>4</footnotemark> Undeed, every decision of the Supreme Court striking down a punishment under the Eighth Amendment has concerned a legislative act. Weems v. United <span class="citation" data-id="9418181"><a href="/opinion/97242/weems-v-united-states/" aria-description="Citation for case: Weems v. United States">States, <em>supra; </em></a></span>Trop v. Dulles, <span class="citation" data-id="9421564"><a href="/opinion/105659/trop-v-dulles/" aria-description="Citation for case: Trop v. Dulles">356 U.S. 86</a></span>, <span class="citation" data-id="9421564"><a href="/opinion/105659/trop-v-dulles/" aria-description="Citation for case: Trop v. Dulles">78 S.Ct. 590</a></span>, <span class="citation" data-id="9421564"><a href="/opinion/105659/trop-v-dulles/" aria-description="Citation for case: Trop v. Dulles">2 L.Ed.2d 630</a></span> (1958) (plurality opinion of Chief Justice Warren); Robinson v. California, <span class="citation" data-id="9422471"><a href="/opinion/106451/robinson-v-california/" aria-description="Citation for case: Robinson v. California">370 U.S. 660</a></span>, <span class="citation" data-id="9422471"><a href="/opinion/106451/robinson-v-california/" aria-description="Citation for case: Robinson v. California">82 S.Ct. 1417</a></span>, <span class="citation" data-id="9422471"><a href="/opinion/106451/robinson-v-california/" aria-description="Citation for case: Robinson v. California">8 L.Ed.2d 758</a></span> (1962); Furman v. <span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/" aria-description="Citation for case: Furman v. Georgia">Georgia, <em>supra.</em></a></span></p>
<p id="AAB"><page-number citation-index="1" label="1032">*1032</page-number>We do not suggest, however, that the cruel and unusual punishment clause must necessarily be read as limited to acts of legislatures in authorizing sentences or of judges imposing them. It can fairly be deemed to be applicable to the manner in which an otherwise constitutional sentence, as the death penalty was then thought to be, is carried out by an executioner, see Louisiana ex rel. Francis v. Resweber, <span class="citation" data-id="9419910"><a href="/opinion/104355/louisiana-ex-rel-francis-v-resweber/" aria-description="Citation for case: Louisiana Ex Rel. Francis v. Resweber">329 U.S. 459</a></span>, <span class="citation" data-id="9419910"><a href="/opinion/104355/louisiana-ex-rel-francis-v-resweber/" aria-description="Citation for case: Louisiana Ex Rel. Francis v. Resweber">67 S.Ct. 374</a></span>, <span class="citation" data-id="9419910"><a href="/opinion/104355/louisiana-ex-rel-francis-v-resweber/" aria-description="Citation for case: Louisiana Ex Rel. Francis v. Resweber">91 L.Ed. 422</a></span> (1947), or to cover conditions of confinement which may make intolerable an otherwise constitutional term of imprisonment, see Holt v. Sarver, <span class="citation" data-id="9456861"><a href="/opinion/296489/lawrence-j-holt-v-robert-sarver-commissioner-of-corrections/" aria-description="Citation for case: Lawrence J. Holt v. Robert Sarver, Commissioner of...">442 F.2d 304</a></span> (8 Cir. 1971). On a parity of reasoning, we find no difficulty in considering the cruel and unusual punishment clause to be applicable to such systems of prison discipline as solitary confinement, see Wright v. McMann, <span class="citation" data-id="9453201"><a href="/opinion/278308/lawrence-william-wright-v-daniel-mcmann-as-warden-of-clinton-state-prison/" aria-description="Citation for case: Lawrence William Wright v. Daniel McMann as Warden of...">387 F.2d 519</a></span> (2 Cir. 1967) (reversing dismissal of complaint), <span class="citation multiple-matches"><a href="/c/F.2d/460/126/">460 F.2d 126</a></span> (2 Cir.) (upholding award of damages), cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./409/885/">409 U.S. 885</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./93/115/">93 S.Ct. 115</a></span>, <span class="citation no-link">34 L.Ed.2d 141</span> (1972); Sostre v. McGinnis, <span class="citation" data-id="8885370"><a href="/opinion/8898661/sostre-v-mcginnis/#190" aria-description="Citation for case: Sostre v. McGinnis">442 F.2d 178, 190-194</a></span> (2 Cir. 1971), cert. denied, <span class="citation" data-id="108452"><a href="/opinion/108452/robins-v-united-states/" aria-description="Citation for case: Robins v. United States">404 U.S. 1049</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./92/719/">92 S.Ct. 719</a></span>, <span class="citation no-link">30 L.Ed.2d 740</span> (1972); Novak v. Beto, <span class="citation" data-id="8886941"><a href="/opinion/8900130/novak-v-beto/" aria-description="Citation for case: Novak v. Beto">453 F.2d 661</a></span> (5 Cir. 1971), cert. denied, <span class="citation" data-id="9425123"><a href="/opinion/108686/sellars-et-al-v-beto-corrections-director/" aria-description="Citation for case: Sellars Et Al. v. Beto, Corrections Director">409 U.S. 968</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./93/279/">93 S.Ct. 279</a></span>, <span class="citation" data-id="9425123"><a href="/opinion/108686/sellars-et-al-v-beto-corrections-director/" aria-description="Citation for case: Sellars Et Al. v. Beto, Corrections Director">34 L.Ed.2d 233</a></span> (1972), or corporal punishment, see Jackson v. Bishop, <span class="citation" data-id="8879837"><a href="/opinion/8893462/jackson-v-bishop/" aria-description="Citation for case: Jackson v. Bishop">404 F.2d 571</a></span> (8 Cir. 1968). The thread common to all these cases is that “punishment” has been deliberately administered for a penal or disciplinary purpose, with the apparent authorization of high prison officials charged by the state with responsibility for care, control, and discipline of prisoners. In contrast, although a spontaneous attack by a guard is “cruel” and, we hope, “unusual,” it does not fit any ordinary concept of “punishment.”</p>
<p id="b1094-6">This is particularly clear in a case like the present where the plaintiff had not yet been found liable to “punishment” of any sort. We have considerable doubt that the cruel and unusual punishment clause is properly applicable at all until after conviction and sentence. See Anderson v. Nosser, 456 F.2d 2d 835 (5 Cir.) (en banc), cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./409/848/">409 U.S. 848</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./93/53/">93 S.Ct. 53</a></span>, <span class="citation" data-id="8981837"><a href="/opinion/8989681/berger-v-columbia-broadcasting-system-inc/" aria-description="Citation for case: Berger v. Columbia Broadcasting System, Inc.">34 L.Ed.2d 89</a></span> (1972) modifying <span class="citation" data-id="9456521"><a href="/opinion/294828/katie-ruth-anderson-v-j-j-nosser-james-bradley-v-j-j-nosser/" aria-description="Citation for case: Katie Ruth Anderson v. J. J. Nosser, James Bradley v. J....">438 F.2d 183</a></span> (5 Cir. 1971); Hamilton v. Love, <span class="citation" data-id="1428202"><a href="/opinion/1428202/hamilton-v-love/#1191" aria-description="Citation for case: Hamilton v. Love">328 F.Supp. 1182, 1191</a></span> (E.D.Ark.1971); but see Rhem v. McGrath, <span class="citation" data-id="1460390"><a href="/opinion/1460390/rhem-v-mcgrath/#690" aria-description="Citation for case: Rhem v. McGrath">326 F.Supp. 681, 690</a></span> (S.D.N.Y. 1971). Yet it would be absurd to hold that a pre-trial detainee has less constitutional protection against acts of prison guards than one who has been convicted.</p>
<p id="b1094-7">The solution lies in the proposition that, both before and after sentence, constitutional protection against police brutality is not limited to conduct violating the specific command of the Eighth Amendment or, as in Monroe v. Pape, <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U.S. 167</a></span>, <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">81 S.Ct. 473</a></span>, <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">5 L.Ed.2d 492</a></span> (1961), of the Fourth. Rochin v. California, <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U.S. 165</a></span>, <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">72 S.Ct. 205</a></span>, <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">96 L.Ed. 183</a></span> (1952), must stand for the proposition that, quite apart from any “specific” of the Bill of Rights, application of undue force by law enforcement officers deprives a suspect of liberty without due process of law. If Rochin suffered such a violation of his constitutional rights by the police as to be entitled to invalidation of a conviction obtained as a consequence, he also was the victim of a violation sufficient to sustain an action under the Civil Rights Act.<footnotemark>5</footnotemark> The same principle <page-number citation-index="1" label="1033">*1033</page-number>should extend to acts of brutality by correctional officers, although the notion of what constitutes brutality may not necessarily be the same. This, apparently, was the view taken by the Seventh Circuit in Collum v. <span class="citation" data-id="288499"><a href="/opinion/288499/curtis-collum-cross-appellee-v-frank-a-butler-james-hand-and-james/" aria-description="Citation for case: Curtis Collum, Cross-Appellee v. Frank A. Butler, James...">Butler, <em>supra, </em></a></span><span class="citation" data-id="288499"><a href="/opinion/288499/curtis-collum-cross-appellee-v-frank-a-butler-james-hand-and-james/#1259" aria-description="Citation for case: Curtis Collum, Cross-Appellee v. Frank A. Butler, James...">421 F.2d at 1259-1260</a></span>, by the Fifth in Tolbert v. <span class="citation" data-id="300228"><a href="/opinion/300228/george-tolbert-jr-v-warden-bragan/" aria-description="Citation for case: George Tolbert, Jr. v. Warden Bragan">Bragan, <em>supra, </em></a></span><span class="citation" data-id="300228"><a href="/opinion/300228/george-tolbert-jr-v-warden-bragan/" aria-description="Citation for case: George Tolbert, Jr. v. Warden Bragan">451 F.2d 1020</a></span>, and by the Ninth in Wiltsie v. California Department of Corrections, <em>supra, </em><span class="citation" data-id="8880072"><a href="/opinion/8893681/wiltsie-v-california-department-of-corrections/#517" aria-description="Citation for case: Wiltsie v. California Department of Corrections">406 F.2d at 517</a></span>. See also Jenkins v. <span class="citation" data-id="9455514"><a href="/opinion/289671/robert-leon-jenkins-a-minor-by-his-mother-and-next-friend-roberta-b/" aria-description="Citation for case: Robert Leon Jenkins, a Minor, by His Mother and Next...">Averett, <em>supra, </em></a></span><span class="citation" data-id="9455514"><a href="/opinion/289671/robert-leon-jenkins-a-minor-by-his-mother-and-next-friend-roberta-b/#1232" aria-description="Citation for case: Robert Leon Jenkins, a Minor, by His Mother and Next...">424 F.2d at 1232</a></span>, Fitzke v. <span class="citation" data-id="306421"><a href="/opinion/306421/robert-fitzke-and-joy-fitzke-v-barry-shappell-deputy-sheriff-and-elwin/" aria-description="Citation for case: Robert Fitzke and Joy Fitzke v. Barry Shappell, Deputy...">Shappell, <em>supra, </em></a></span><span class="citation" data-id="306421"><a href="/opinion/306421/robert-fitzke-and-joy-fitzke-v-barry-shappell-deputy-sheriff-and-elwin/#1076" aria-description="Citation for case: Robert Fitzke and Joy Fitzke v. Barry Shappell, Deputy...">468 F.2d at 1076</a></span>. And most of the courts faced with challenges to the conditions of <em>pre-trial </em>detention have primarily based their analysis directly on the due process clause. See Anderson v. Nosser, <em>supra, </em><span class="citation" data-id="302032"><a href="/opinion/302032/katie-ruth-anderson-v-j-j-nosser-james-bradley-v-j-j-nosser/" aria-description="Citation for case: Katie Ruth Anderson v. J. J. Nosser, James Bradley v. J....">456 F.2d 835</a></span>; Hamilton v. <span class="citation" data-id="1428202"><a href="/opinion/1428202/hamilton-v-love/" aria-description="Citation for case: Hamilton v. Love">Love, <em>supra, </em></a></span><span class="citation" data-id="1428202"><a href="/opinion/1428202/hamilton-v-love/" aria-description="Citation for case: Hamilton v. Love">328 F.Supp. 1182</a></span>; Jones v. Wittenberg, <span class="citation" data-id="1572711"><a href="/opinion/1572711/jones-v-wittenberg/" aria-description="Citation for case: Jones v. Wittenberg">323 F.Supp. 93</a></span> (N.D.Ohio 1971), aff’d, <span class="citation" data-id="302035"><a href="/opinion/302035/charles-jones-v-william-metzger-homer-roberts/" aria-description="Citation for case: Charles Jones v. William Metzger, Homer Roberts">456 F.2d 854</a></span> (6 Cir. 1972); Brenneman v. Madigan, <span class="citation" data-id="1691314"><a href="/opinion/1691314/brenneman-v-madigan/" aria-description="Citation for case: Brenneman v. Madigan">343 F.Supp. 128</a></span> (N.D.Cal. 1972).</p>
<p id="b1095-5">While the <em><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span> </em>test, “conduct that shocks the conscience,” <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#172" aria-description="Citation for case: Rochin v. California">342 U. S. at 172</a></span>, <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">72 S.Ct. 205</a></span>, is not one that can be applied by a computer,<footnotemark>6</footnotemark> it at least points the way. Certainly the constitutional protection is nowhere nearly so extensive as that afforded by the common law tort action for battery, which makes actionable any intentional and unpermitted contact with the plaintiff’s person or anything attached to it and practically identified with it, see Prosser, Torts § 9 (4th ed. 1971); still less is it as extensive as that afforded by the common law tort action for assault, redressing “Any act of such a nature as to excite an apprehension of battery,” <em>id. </em>§ 10, at <em>38.</em><footnotemark><em>7</em></footnotemark><em> </em>Although “the least touching of another in anger is a battery,” Cole v. Turner, 6 Mod. 149, 87 Eng.Rep. 907, 90 Eng.Rep. 958 (K.B. 1704) (Holt, C. J.), it is not a violation of a constitutional right actionable under <span class="citation no-link">42 U.S.C. § 1983</span>. The management by a few guards of large numbers of prisoners, not usually the most gentle or tractable of men and women, may require and justify the occasional use of a degree of intentional force. Not every push or shove, even if it may later seem unnecessary in the peace of a judge’s chambers, violates a prisoner’s constitutional rights. In determining whether the constitutional line has been crossed, a court must look to such factors as the need for the application of force, the relationship between the need and the amount of force that was used, the extent of injury inflicted, and whether force was applied in a good faith effort to maintain or restore discipline or maliciously and sadistically for the very purpose of causing harm. Taking this view, and reading the complaint with the generosity required in <em>pro se </em>civil rights actions, Haines v. Kerner, <span class="citation" data-id="108432"><a href="/opinion/108432/haines-v-kerner/#520" aria-description="Citation for case: Haines v. Kerner">404 U.S. 519, 520-521</a></span>, <span class="citation" data-id="108432"><a href="/opinion/108432/haines-v-kerner/" aria-description="Citation for case: Haines v. Kerner">92 S.Ct. 594</a></span>, <span class="citation" data-id="108432"><a href="/opinion/108432/haines-v-kerner/" aria-description="Citation for case: Haines v. Kerner">30 L.Ed.2d 652</a></span> (1972), we think it stated a claim against Officer Fuller.</p>
<p id="b1095-11">On the other hand, even on a charitable reading, we see no basis for <page-number citation-index="1" label="1034">*1034</page-number>sustaining the complaint against the warden. The rule in this circuit is that when monetary damages are sought under § 1983, the general doctrine of <em>respondeat superior </em>does not suffice and a showing of some personal responsibility of the defendant is required. Thus in Martinez v. <span class="citation" data-id="297139"><a href="/opinion/297139/louis-martinez-v-vincent-r-mancusi-warden-attica-prison-dr-williams/" aria-description="Citation for case: Louis Martinez v. Vincent R. Mancusi, Warden, Attica...">Mancusi, <em>supra, </em></a></span><span class="citation" data-id="297139"><a href="/opinion/297139/louis-martinez-v-vincent-r-mancusi-warden-attica-prison-dr-williams/#924" aria-description="Citation for case: Louis Martinez v. Vincent R. Mancusi, Warden, Attica...">443 F.2d at 924</a></span>, we conditioned a conclusion of liability of the warden on a finding that he was personally “responsible for what the guards did.” Again, in Wright v. Mc-Mann, <em>supra, </em>460 F.2d at 134-135, in upholding a damage award as against Warden McMann, we stressed that “there is every reason to believe that he was aware of segregation cell conditions,” and that “responsibility for permitting such conditions to exist was ultimately, in any event, squarely his.” See also Harty v. Rockefeller, <span class="citation" data-id="2182189"><a href="/opinion/2182189/harty-v-rockefeller/" aria-description="Citation for case: Harty v. Rockefeller">338 F. Supp. 367</a></span> (S.D.N.Y.1972); (Gurfein, J.). Adams v. Pate, <span class="citation" data-id="297684"><a href="/opinion/297684/vernon-c-adams-v-frank-j-pate-warden-luther-w-miller-v-illinois/" aria-description="Citation for case: Vernon C. Adams v. Frank J. Pate, Warden, Luther W....">445 F.2d 105</a></span>, 107 &amp; n. 2 (7 Cir. 1971), and a dictum in Dunham v. Crosby, <span class="citation" data-id="293866"><a href="/opinion/293866/kenneth-t-dunham-v-philip-b-crosby-jr/#1180" aria-description="Citation for case: Kenneth T. Dunham v. Philip B. Crosby, Jr.">435 F.2d 1177, 1180</a></span> (1 Cir. 1970), are in accord. We reaffirm our position here, though we are aware that Anderson v. Nosser, <span class="citation" data-id="9456521"><a href="/opinion/294828/katie-ruth-anderson-v-j-j-nosser-james-bradley-v-j-j-nosser/" aria-description="Citation for case: Katie Ruth Anderson v. J. J. Nosser, James Bradley v. J....">438 F.2d 183</a></span>, 199-200 &amp; n. 13 (5 Cir. 1971), modified, <span class="citation" data-id="302032"><a href="/opinion/302032/katie-ruth-anderson-v-j-j-nosser-james-bradley-v-j-j-nosser/" aria-description="Citation for case: Katie Ruth Anderson v. J. J. Nosser, James Bradley v. J....">456 F.2d 835</a></span> (5 Cir. 1972) (en banc), left the question open; that Hesselgesser v. Reilly, <span class="citation" data-id="295850"><a href="/opinion/295850/donald-d-hesselgesser-v-william-j-reilly-sheriff-of-spokane-county/" aria-description="Citation for case: Donald D. Hesselgesser v. William J. Reilly, Sheriff of...">440 F.2d 901</a></span> (9 Cir. 1971), held that § 1983 liability might be predicated on a specific state statute making a sheriff liable for the acts of his deputies; and that Carter v. Carlson, <span class="citation" data-id="9457236"><a href="/opinion/298619/melvin-carter-v-john-r-carlson/" aria-description="Citation for case: Melvin Carter v. John R. Carlson">144 U.S.App.D.C. 388</a></span>, <span class="citation" data-id="9457236"><a href="/opinion/298619/melvin-carter-v-john-r-carlson/" aria-description="Citation for case: Melvin Carter v. John R. Carlson">447 F.2d 358</a></span>, 370 &amp; n. 39, rev’d on other grounds, <span class="citation" data-id="108654"><a href="/opinion/108654/district-of-columbia-v-carter/" aria-description="Citation for case: District of Columbia v. Carter">409 U.S. 418</a></span>, <span class="citation" data-id="108654"><a href="/opinion/108654/district-of-columbia-v-carter/" aria-description="Citation for case: District of Columbia v. Carter">93 S.Ct. 602</a></span>, <span class="citation" data-id="108654"><a href="/opinion/108654/district-of-columbia-v-carter/" aria-description="Citation for case: District of Columbia v. Carter">34 L.Ed.2d 613</a></span> (1973), went all the way, holding <em>respondeat superior </em>to be fully applicable to actions under § 1983.</p>
<p id="b1096-6">Here the complaint alleged only that Warden Glick was in charge of all the correctional officers employed at the House of Detention. It did not allege that the warden had authorized the officer’s conduct, see Martinez v. <span class="citation" data-id="297139"><a href="/opinion/297139/louis-martinez-v-vincent-r-mancusi-warden-attica-prison-dr-williams/" aria-description="Citation for case: Louis Martinez v. Vincent R. Mancusi, Warden, Attica...">Mancusi, <em>supra, </em></a></span><span class="citation" data-id="297139"><a href="/opinion/297139/louis-martinez-v-vincent-r-mancusi-warden-attica-prison-dr-williams/#924" aria-description="Citation for case: Louis Martinez v. Vincent R. Mancusi, Warden, Attica...">443 F.2d at 924</a></span>, or even that there had been a history of previous episodes requiring the warden to take therapeutic action, <em>cf. </em>Wright v. <span class="citation" data-id="9453201"><a href="/opinion/278308/lawrence-william-wright-v-daniel-mcmann-as-warden-of-clinton-state-prison/" aria-description="Citation for case: Lawrence William Wright v. Daniel McMann as Warden of...">McMann, <em>supra, </em></a></span>460 F.2d at 134-135; it alleged a single spontaneous incident, unforeseen and unforeseeable by higher authority. While appellant’s counsel urged that we permit him to develop further facts that might implicate the warden, the better course is to affirm the dismissal of the complaint against the warden without prejudice to an application for leave to amend if a factual basis for this should appear. We request that counsel assigned by the judge to take this appeal shall continue to act for Johnson in the district court.</p>
<p id="b1096-8">Reversed with respect to Officer Fuller; affirmed with respect to Warden Glick. No costs.</p>
<footnote label="1">
<p id="b1092-6">. Apart from controlling Supreme Court authority, see Preiser v. Rodriguez, <span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/#477" aria-description="Citation for case: Preiser v. Rodriguez">411 U.S. 475, 477, 498-499</a></span>, <span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">93 S.Ct. 1827</a></span>, <span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">36 L.Ed.2d 439</a></span> (1973), this would be a most inappropriate ease in which to require exhaustion of state judicial remedies. As a result of Johnson’s conviction of manslaughter, and the consequent suspension of his civil rights, N.Y_. Civil Rights Law, McKinney’s Consol.Laws, c. 6, § 79, he is presently unable to bring an action in the state courts.</p>
</footnote>
<footnote label="2">
<p id="b1092-14">. Also, it may be that all the beatings alleged there were for the purpose of extracting a confession from Brown, see <span class="citation" data-id="273780"><a href="/opinion/273780/homer-ray-brown-v-edmund-g-brown-governor-state-of-california/" aria-description="Citation for case: Homer Ray Brown v. Edmund G. Brown, Governor, State of...">368 F.2d at 993</a></span>-994 n. 2, in which case Fifth Amendment protections would be implicated.</p>
</footnote>
<footnote label="3">
<p id="b1093-9">. See Granucci, “Nor Cruel and Unusual Punishments Inflicted”: The Originnl Meaning, 57 Calif.L.Rev. 839 (1969).</p>
</footnote>
<footnote label="4">
<p id="b1093-12">. The history of the cruel and unusual punishment clause is lucidly recounted in Mr. Justice Marshall’s concurring opinion in Furman v. <span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/" aria-description="Citation for case: Furman v. Georgia">Georgia, <em>supra, </em></a></span><span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/#316" aria-description="Citation for case: Furman v. Georgia">408 U.S. at 316-322</a></span>, <span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/" aria-description="Citation for case: Furman v. Georgia">92 S.Ct. 2726</a></span>.</p>
</footnote>
<footnote label="5">
<p id="b1094-4">. We note also that in Williams v. United States, <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/" aria-description="Citation for case: Williams v. United States">341 U.S. 97</a></span>, <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/" aria-description="Citation for case: Williams v. United States">71 S.Ct. 576</a></span>, <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/" aria-description="Citation for case: Williams v. United States">95 L.Ed. 774</a></span> (1951), the Supreme Court had little difficulty in upholding a conviction of a law enforcement officer under <span class="citation no-link">18 U.S.C. § 242</span>, the criminal counterpart of <span class="citation no-link">42 U.S.C. § 1983</span>, finding due process to be violated “where police take matters in their own hands, seize victims, [and] beat and pound them until they confess.” <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/#101" aria-description="Citation for case: Williams v. United States">341 U.S. at 101</a></span>, <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/#579" aria-description="Citation for case: Williams v. United States">71 S.Ct. at 579</a></span>. The indictment charged that the victim had been deprived of</p>
<blockquote id="b1094-9">the right and privilege not to be deprived of liberty without due process of law, the right and privilege to be secure in his person while in the custody of the State of Florida, the right and privilege not to be subjected to punishment without due process of <page-number citation-index="1" label="1033">*1033</page-number>law, the right to be immune, while in the custody of persons acting under color of the laws of the State of Florida, from illegal assault and battery by any person exercising the authority of said State</blockquote>
<p id="b1095-7">as well as the right to be tried in accordance with due process of law, <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/#103" aria-description="Citation for case: Williams v. United States">341 U.S. at 103</a></span>, <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/#580" aria-description="Citation for case: Williams v. United States">71 S.Ct. at 580</a></span>, and the trial judge charged the jury that it could find Williams guilty if he beat the victim “for the purpose of imposing illegal summary punishment upon him” as well as if the beating was “for the purpose of forcing him to make a confession”. <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/#104" aria-description="Citation for case: Williams v. United States">341 U.S. at 104</a></span>, <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/#580" aria-description="Citation for case: Williams v. United States">71 S.Ct. at 580</a></span>. See also United States v. Price, <span class="citation" data-id="107202"><a href="/opinion/107202/united-states-v-price/#793" aria-description="Citation for case: United States v. Price">383 U.S. 787, 793</a></span>, <span class="citation" data-id="107202"><a href="/opinion/107202/united-states-v-price/" aria-description="Citation for case: United States v. Price">86 S.Ct. 1152</a></span>, <span class="citation" data-id="107202"><a href="/opinion/107202/united-states-v-price/" aria-description="Citation for case: United States v. Price">16 L.Ed.2d 267</a></span> (1966).</p>
</footnote>
<footnote label="6">
<p id="b1095-12">. The standard gains added content from other language in the opinion. The acts must do more than “offend some fastidious squeamishness or private sentimentalism about combatting crime too energetically”; they must be such as “to offend even hardened sensibilities,” <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#172" aria-description="Citation for case: Rochin v. California">342 U.S. at 172</a></span>, <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#209" aria-description="Citation for case: Rochin v. California">72 S.Ct. at 209</a></span>, or constitute force that is “brutal” and “offensive to human dignity.” <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#174" aria-description="Citation for case: Rochin v. California">342 U.S. at 174</a></span>, <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">72 S.Ct. 205</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b1095-13">. Even at common law “mere words, however violent, are held not to amount to an assault,” <em><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Id.</a></span> </em>§ 10, at 39.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Kalkines v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Kalkines v. United States"
type: case
citation: ""
parallel_cite: "200 Ct. Cl. 570; 473 F.2d 1391; 1973 U.S. Ct. Cl. LEXIS 11"
neutral_cite: ""
court: U.S. Court of Claims
court_level: other
circuit: ""
year: 1973
date_decided: 1973-02-16
docket: ""
authority_weight: Historical
treatment:
  field_i_validity: good_law
  as_of_content: 1973-02-16
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Kalkines v. United States
  varies_by_point: false
  scope_note: "Good law; the 'Kalkines warning' remains the governing standard for compelling federal employees to answer job-related questions. A U.S. Court of Claims decision; its precedent was adopted as binding by the Federal Circuit (South Corp. v. United States)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/8615714/kalkines-v-united-states/"
  cluster_id: 8615714
  opinion_id: 8594616
  identity_checked: true
homes:
  - page: "[[Public-Employee Compelled Statements (Garrity)]]"
    role: "Key — Progeny / Refinement"
related: ["[[Garrity v. New Jersey]]", "[[Gardner v. Broderick]]", "[[Lefkowitz v. Turley]]"]
aliases: []
tags: ["case", "fifth-amendment", "self-incrimination", "public-employee", "garrity", "kalkines-warning", "federal-employee"]
holding: "A federal employee may be discharged for refusing to answer narrowly job-related questions only if first adequately advised both that refusal subjects him to discharge and that his answers (and their fruits) cannot be used against him in a criminal case — the 'Kalkines warning.'"
lake:
  record_id: Kalkines v. United States
  status: verified
  projected_at: 2026-07-06
---

# Kalkines v. United States

*473 F.2d 1391 (Ct. Cl. 1973)* · U.S. Court of Claims · **Binding in-circuit — Fed. Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
George Kalkines, an import specialist with the Bureau of Customs, was investigated for allegedly accepting a bribe, with a criminal grand-jury investigation proceeding concurrently with the agency's administrative inquiry. At four interviews he declined to answer certain questions about his finances and the performance of his duties. The agency discharged him for failing to answer work-related questions in violation of Customs and Treasury manuals, and the Civil Service Commission affirmed. Kalkines sued, contending he had never been adequately assured that his answers could not be used against him in the pending criminal matter.

## Issue
Whether a federal employee may be discharged for refusing to answer questions about the performance of his duties when he was not adequately advised that he must answer or face discharge, and that his answers and their fruits could not be used against him in a criminal prosecution.

## Rule
A public employee cannot be fired merely for invoking the privilege: "It is now settled that the individual cannot be discharged simply because he invokes his Fifth Amendment privilege against self-incrimination in refusing to respond." — 473 F.2d at 1393 (200 Ct. Cl. at 574). ^pin-1393a

But he can be compelled to answer under a sufficient warning: "[A] governmental employer is not wholly barred from insisting that relevant information be given it; the public servant can be removed for not replying if he is adequately informed both that he is subject to discharge for not answering and that his replies (and their fruits) cannot be employed against him in a criminal case." — *Id.* ^pin-1393

## Application
Throughout the interviews Kalkines faced a concurrent criminal bribery investigation, so the protection against criminal use of his answers was critical. On none of the four occasions was he adequately advised both that refusal would subject him to discharge and that his answers (and their fruits) could not be used against him criminally — the agent's most explicit statement omitted the "fruits" protection and never properly brought home that he would have immunity. Because the required warning was not given, Kalkines's refusals did not violate the duty-to-answer regulations, and his discharge on that ground was invalid.

## Conclusion
Kalkines's removal could not stand, because he was discharged for refusing to answer without first receiving the constitutionally adequate assurance of immunity. The decision establishes the federal "Kalkines warning" implementing *[[Garrity v. New Jersey|Garrity]]* and *[[Gardner v. Broderick|Gardner]]* for federal employees.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — Fed. Cir.**
- *Kalkines* is good law; the "Kalkines warning" it articulates is the standard federal-employer advisement when compelling job-related answers. It implements [[Garrity v. New Jersey]] and [[Gardner v. Broderick]] (and parallels [[Lefkowitz v. Turley]]). As a U.S. Court of Claims decision, its precedent binds in the Federal Circuit.

## Appears on
- [[Public-Employee Compelled Statements (Garrity)]] — *Key — Progeny / Refinement*

## Sources
- *Kalkines v. United States*, 473 F.2d 1391 (Ct. Cl. 1973) (200 Ct. Cl. 570) — https://www.courtlistener.com/opinion/8615714/kalkines-v-united-states/ — pinpoints: 473 F.2d 1393 (200 Ct. Cl. 574). (CourtListener copy carries Ct. Cl. star-pagination.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "654b6e40df6114a0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Court of Claims", "neutral_cite": "", "official_citation_present": false, "parallel_cite": "200 Ct. Cl. 570; 473 F.2d 1391; 1973 U.S. Ct. Cl. LEXIS 11", "title": "Kalkines v. United States", "year": "1973"}}
{"assertion_id": "562f179bf9b312c6", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A federal employee may be discharged for refusing to answer narrowly job-related questions only if first adequately advised both that refusal subjects him to discharge and that his answers (and their fruits) cannot be used against him in a criminal case — the 'Kalkines warning.'", "title": "Kalkines v. United States"}}
{"assertion_id": "82ea054f1327420c", "dimension": "support", "kind": "home_role", "locator": {"home": "Public-Employee Compelled Statements (Garrity)"}, "payload": {"home": "Public-Employee Compelled Statements (Garrity)", "role": "Key — Progeny / Refinement", "title": "Kalkines v. United States"}}
{"assertion_id": "32a0dabddc3c9a16", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1973-02-16", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Kalkines v. United States", "field_i_validity": "good_law", "scope_note": "Good law; the 'Kalkines warning' remains the governing standard for compelling federal employees to answer job-related questions. A U.S. Court of Claims decision; its precedent was adopted as binding by the Federal Circuit (South Corp. v. United States).", "title": "Kalkines v. United States", "varies_by_point": "false"}}
{"assertion_id": "b008a5d70d6f6677", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Historical", "title": "Kalkines v. United States"}}
```

### lake record — Kalkines v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kalkines v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Kalkines v. United States",
    "case_name_short": "Kalkines",
    "case_name_full": "GEORGE KALKINES v. United States",
    "input_case_name": "Kalkines v. United States",
    "court": "U.S. Court of Claims",
    "court_id": "cc",
    "court_level": "other",
    "circuit": null,
    "state": null,
    "date_decided": "1973-02-16",
    "year": 1973,
    "docket": null,
    "cluster_id": 8615714,
    "lead_opinion_id": 8594616,
    "sibling_ids": [
      8594616
    ],
    "absolute_url": "/opinion/8615714/kalkines-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "200 Ct. Cl. 570",
        "volume": "200",
        "reporter": "Ct. Cl.",
        "page": "570",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "473 F.2d 1391",
        "volume": "473",
        "reporter": "F.2d",
        "page": "1391",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. Ct. Cl. LEXIS 11",
        "volume": "1973",
        "reporter": "U.S. Ct. Cl. LEXIS",
        "page": "11",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "200 Ct. Cl. 570",
        "volume": "200",
        "reporter": "Ct. Cl.",
        "page": "570",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "473 F.2d 1391",
        "volume": "473",
        "reporter": "F.2d",
        "page": "1391",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. Ct. Cl. LEXIS 11",
        "volume": "1973",
        "reporter": "U.S. Ct. Cl. LEXIS",
        "page": "11",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "other",
      "selected": null,
      "reason": "unlisted_reporter:Ct. Cl."
    }
  },
  "pinpoints": [
    {
      "id": "pin-1393a",
      "page": null,
      "quote": "--- # Kalkines v. United States *473 F.2d 1391 (Ct. Cl. 1973)* \u00b7 U.S. Court of Claims \u00b7 **Binding in-circuit \u2014 Fed. Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background George Kalkines, an import specialist with the Bureau of Customs, was investigated for allegedly accepting a bribe, with a criminal grand-jury investigation proceeding concurrently with the agency's administrative inquiry. At four interviews he declined to answer certain questions about his finances and the performance of his duties. The agency discharged him for failing to answer work-related questions in violation of Customs and Treasury manuals, and the Civil Service Commission affirmed. Kalkines sued, contending he had never been adequately assured that his answers could not be used against him in the pending criminal matter. ## Issue Whether a federal employee may be discharged for refusing to answer questions about the performance of his duties when he was not adequately advised that he must answer or face discharge, and that his answers and their fruits could not be used against him in a criminal prosecution. ## Rule A public employee cannot be fired merely for invoking the privilege:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1393",
      "page": null,
      "quote": "[A] governmental employer is not wholly barred from insisting that relevant information be given it; the public servant can be removed for not replying if he is adequately informed both that he is subject to discharge for not answering and that his replies (and their fruits) cannot be employed against him in a criminal case.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1973-02-16",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Kalkines v. United States",
    "varies_by_point": false,
    "scope_note": "Good law; the 'Kalkines warning' remains the governing standard for compelling federal employees to answer job-related questions. A U.S. Court of Claims decision; its precedent was adopted as binding by the Federal Circuit (South Corp. v. United States).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "John P. Mack v. United States of America, Federal Bureau of Investigation, Defendants",
          "cluster_id": 484948,
          "cite": [
            "814 F.2d 120",
            "1987 U.S. App. LEXIS 4041",
            "43 Empl. Prac. Dec. (CCH) 37,032"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kalkines v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aguilera v. Baca",
          "cluster_id": 1390016,
          "cite": [
            "510 F.3d 1161",
            "27 I.E.R. Cas. (BNA) 31",
            "2007 U.S. App. LEXIS 29804",
            "2007 WL 4531990"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kalkines v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Meyer Kama v. Alejandro Mayorkas",
          "cluster_id": 10006780,
          "cite": [
            "107 F.4th 1054"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kalkines v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sergio Luna v. Department of Homeland Security",
          "cluster_id": 9459217,
          "cite": [
            "2024 MSPB 2"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kalkines v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michelle Shows v. Department of the Treasury",
          "cluster_id": 10743161,
          "cite": [
            "2025 MSPB 5"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kalkines v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Use of Polygraph Examinations in Investigating Disclosure of Information About Pending Criminal Investigations",
          "cluster_id": 4342987,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kalkines v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(8594616) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus)",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 0,
        "triage_read": 0,
        "triage_snippet_classified": 0
      },
      "lane2_top_cited": {
        "query": "cites:(8594616)",
        "reviewed": 6,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 6,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(8594616)",
        "reviewed": 3,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 3,
        "triage_read": 0,
        "triage_snippet_classified": 3
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(8594616)",
    "indexed_citing_opinions": 6,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 8594616,
        "count": 6,
        "count_source": "search"
      }
    ],
    "citation_count": 59,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/kalkines-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 6,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T09:03:38Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Ct. Cl.",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T09:03:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T09:03:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T09:04:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T09:03:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Kalkines v. United States

```
<opinion type="majority">
<author id="b604-7">Davis, <em>Judge,</em></author>
<p id="Aq--">delivered the opinion of the court:</p>
<p id="b604-8">Plaintiff George Kalkines worked for the Bureau of Customs of the Treasury Department from November 1960 until his suspension in June 1968, rising from an initial rating of GS-7 to the position of import specialist, GS-1'3. His suspension and subsequent discharge came about because of his alleged failure, in violation of the Customs Manual, the Customs Personnel Manual, and the Treasury Personnel Manual,<footnotemark>1</footnotemark> to answer questions put to him by the Bureau of Customs relating to the performance of his duties. According to management, this failure occurred at four separate interviews, three in New York and one in Washington, each listed as an individual specification of the charge. The agency sustained his removal on this charge, upholding each of the four specifications.<footnotemark>2</footnotemark> The Civil Service Commission affirmed. The validity of this determination is brought before us by the parties’ cross-motions for summary judgment, both of <page-number citation-index="1" label="573">*573</page-number>which invoke the administrative record on which we rest for onr decision.<footnotemark>3</footnotemark></p>
<p id="b605-6">In November 1967 the Burean of Customs began an investigation sparked by information saying that plaintiff had accepted a $200 payment from an importer’s representative in return for favorable treatment on valuation of a customs entry. The inquiry initially disclosed that plaintiff had had lunch with the representative on November 16th and had made a $400 deposit in his personal bank account on November 17th. He was then visited or summoned by customs agents (acting as investigatory arms of the Bureau) on several occasions, at four of which (November 28,1967, May 2, 1968, May 8, 1968, all in New York, and June 5, 1968, in Washington) he did not answer, or indicated that he would not answer, certain questions relating to the $400 deposit, his finances, and some aspects of the performance of his customs duties. At other interviews he did answer the queries then put to him. Plaintiff’s defense is that his failure to reply at the four specified times was excusable and justifiable in each instance, and therefore not contrary to the directives cited in footnote 1, <em>supra.</em></p>
<p id="b605-7">The most important fact bearing on the propriety of Mr. Kalkines’ conduct at the interviews is that, for all or most of the time, a criminal investigation was being carried on concurrently with the civil inquiry connected with possible disciplinary proceedings against him. The United States Attorney’s Office had been informed about the possible bribery before the customs agents’ first interview with plaintiff, and it became active in investigating the matter in December 1967; witnesses were subpoenaed to, and did, testify before the grand jury. This criminal inquest continued until well into the spring of 1968, and perhaps even longer. Plaintiff was never indicted, the United States Attorney ultimately declining prosecution, but Mr. Kalkines saw the Damoclean sword poised overhead during the entire period with which we are concerned.</p>
<p id="b606-4"><page-number citation-index="1" label="574">*574</page-number>In recent years the courts have given more precise content to the obligations of a public employee to answer his employer’s work-related questions where, as here, there is a substantial risk that the employee may be subject to prosecution for actions connected with the subject of management’s inquiry. It is now settled that the individual cannot be discharged simply because he invokes his Fifth Amendment privilege against self-incrimination in refusing to respond. <em>Gardner </em>v. Broderick, <span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">392 U.S. 273</a></span> (1968); <em>Uniformed Sanitation Men Ass'n </em>v. <em>Commissioner of </em>Sanitation, <span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">392 U.S. 280</a></span> (1968). Conversely, a later prosecution cannot constitutionally use statements (or their fruits) coerced from the employee — in an earlier disciplinary investigation or proceeding — by a threat of removal from office if he fails to answer the question. <em>Garrity </em>v. <em>New </em>Jersey, <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">385 U.S. 493</a></span> (1967). But a governmental employer is not wholly barred from insisting that relevant information be given it; the public servant can be removed for not replying if he is adequately informed both that he is subject to discharge for not answering and that his replies (and their fruits) cannot be employed against him in a criminal case. <em>See Gardner </em>v. <span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">Broderick, <em>supra, </em></a></span>392 U.S. at 278; <em>Uniformed Sanitation Men Ass’n </em>v. <em>Commissioner of Sanitation, supra, </em>392 U.S. at 283, 284, 285 [hereafter cited as <em>Uniformed Sanitation Men </em>I] ; <em>Uniformed Sanitation Men Ass'n </em>v. <em>Commissioner of Sanitation, </em><span class="citation" data-id="290212"><a href="/opinion/290212/uniformed-sanitation-men-association-inc-v-commissioner-of-sanitation-of/" aria-description="Citation for case: Uniformed Sanitation Men Association, Inc. v....">426 F. 2d 619</a></span> (C.A. 2, 1970), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./406/961/">406 U.S. 961</a></span> (1972) [hereafter cited as <em>Uniformed Sanitation Men </em>II].</p>
<p id="b606-5">This requirement for a sufficient warning to the employee, before questioning, was foreshadowed by the Supreme Court in <em>Uniformed Sanitation Men I, </em>and has been set forth more exactly by the Second Circuit in <em>Uniformed Sanitation Men II. </em>The highest court said that public employees “subject themselves to dismissal if they refuse to account for their performance of their public trust, after proper proceedings, which do not involve an attempt to coerce them to relinquish their constitutional rights.” 392 U.S. at 285. “Proper proceedings” of that type means, according to Chief Judge Friendly in <em>Uniformed Sanitation Men II, </em>inquiries, such <page-number citation-index="1" label="575">*575</page-number>as were held in that case,<footnotemark>4</footnotemark> “in which the employee is asked only pertinent questions about the performance of his duties <em>and is duly advised of his options and the consequences of his </em>choice.” <span class="citation" data-id="290212"><a href="/opinion/290212/uniformed-sanitation-men-association-inc-v-commissioner-of-sanitation-of/#627" aria-description="Citation for case: Uniformed Sanitation Men Association, Inc. v....">426 F. 2d at 627</a></span> (emphasis added). The same opinion said: “To require a public body to continue to keep an officer or employee who refuses to answer pertinent questions concerning his official conduct, <em>although assured of protection against use of his answers or their fruits in any criminal </em>prosecution, would push the constitutional protection beyond its language, its history or any conceivable purpose of the framers of the Bill of Rights.” <span class="citation" data-id="290212"><a href="/opinion/290212/uniformed-sanitation-men-association-inc-v-commissioner-of-sanitation-of/#626" aria-description="Citation for case: Uniformed Sanitation Men Association, Inc. v....">426 F. 2d at 626</a></span> (emphasis added). We think that the general directives of the various Treasury and Customs manuals (footnote 1, <em>supra) </em>should be read with this specific gloss supplied by the <em>Uniformed Sanitation Men </em>opinions.</p>
<p id="b607-6">The only issue we need address is whether plaintiff was “duly advised of his options and the consequences of his choice” and was adequately “assured of protection against use of his answers or their fruits in any criminal prosecution.” For the reasons which follow, we hold that this requirement was not fulfilled on any of the four occasions at which he is charged with failing to respond, that as a consequence he did not transgress the duty-to-reply regulations, and therefore that he was invalidly discharged for not answering the questions put to him.</p>
<p id="b607-7">At the interview of November 28, 1967, it is clear that no advice or warnings as to his constitutional rights was given to Mr. Kalkines, though he was told of the requirement of <page-number citation-index="1" label="576">*576</page-number>the Customs Manual that he answer. -Despite the fact that the matter had already been presented to the United States Attorney (as the customs agents knew), plaintiff was not told that his answers (or information stemming from them) could not be used against him in a criminal proceeding. So as far as the investigators were concerned, he was left sharply impaled on the dilemma of either answering and thereby subjecting himself to the possibility of self-incrimination, or of avoiding giving such help to the prosecution at the cost of his livelihood. The record shows conclusively that at this interview Mr. Kalkines was keenly aware of, and troubled by, the possible criminal implications, and that his failure to respond stemmed, at least in very substantial part, from this anxiety. <em>See also </em>note 6 <em>infra.</em></p>
<p id="b608-5">The next specification is that plaintiff refused to answer pertinent questions on May 2, 1968.<footnotemark>5</footnotemark> By this time, he had retained an attorney, but counsel was not present. Mr. Kalkines declined to answer unless he had the opportunity of consulting with his lawyer. After an exchange on this subject, the customs agent did not attempt to question him further, but called the attorney on the telephone and arranged for a joint meeting on May 8th. The Regional Office of the Civil Service Commission “concluded that there was at the least an implied acquiescence to the [plaintiff’s] request for the presence of his attorney as of May 2, 1968, and, in the circumstances, the [plaintiff’s] failure to answer questions on that date may not be recognized to have established a substantive basis to support” the specification as to May 2d which, accordingly, the Regional Office held not to be sustained. Without overturning the Regional Office’s factual finding on this point, the Board of Appeals and Review ruled that plaintiff was nevertheless guilty of failing to respond on May 2d. The basis for this holding appears <page-number citation-index="1" label="577">*577</page-number>to be that an employee’s obligation to answer is so absolute that it cannot even be waived by the interrogating agent’s agreement to wait until the lawyer is present. This, we hold, was plain error. If, as in this instance, the interrogator acquiesces in a request that questioning be deferred, the employee cannot be held to have violated his duty to account. The directives of the manuals cannot reasonably be interpreted in so absolute, rigid, and insensitive a fashion.<footnotemark>6</footnotemark></p>
<p id="b609-6">In addition, there is no indication whatever that plaintiff was told on May 2d that any answers could <em>not </em>be used against him criminally. Ait the last meeting on December 15th <em>(see </em>note 5 supra), the agent had specifically informed Mr. Kalkines that his answers <em>could </em>be used against him in a criminal proceeding, and in the absence of an explicit disavowal that advice could be expected to retain its force. Plaintiff justifiably remained under the impression that his replies could lead to his conviction of a criminal offense.</p>
<p id="b609-7">The third day on which plaintiff is accused of not answering was May 8,1968. At that time he appeared with counsel. There is a dispute in the testimony as to whether the attorney improperly interfered with the questioning by preventing, in effect, the putting of particular questions. In any event, no specific questions were asked or answered, and the agent <page-number citation-index="1" label="578">*578</page-number>ultimately directed counsel to withdraw from the room while a statement was taken from Mr. Kalkines. Thereupon both the attorney and plaintiff left the room. Plaintiff was told that he had to answer and that he had no right to have his counsel present but declined to stay or respond. Again, the significant element is that it is indisputable that neither the employee nor the lawyer was ever advised on May 8th that the responses to the questions, and their products, could not be used against plaintiff in a criminal trial or proceeding. In whatever way one interprets the controverted evidence as to the course of that meeting, this much is clear — no such caution was given, expressly or impliedly, by the agents.</p>
<p id="b610-5">On these facts, the only outcome, for the first three of the four specifications (November 28,1967; May 2,1968; May 8, 1968), must be that plaintiff cannot be held to have violated his obligation to answer. At those times a criminal investigation was either in the immediate offing or was actively being carried on. At the least, there is no question but that plaintiff thought so, and had no good reason to think otherwise. He obviously obtained a lawyer primarily because he was disturbed at the possibility of a criminal accusation; that danger was uppermost in his mind. It was reasonable for him to fear that any answer he gave to the customs agents might help to bring prosecution nearer; indeed, it was sensible to think that the civil and the criminal investigations were coordinated, so that the former would help the latter. He was never told that under the law his responses to the customs agents could not be used or would not be used as bricks to build him a prison cell. On the contrary, the one time the subject was mentioned by the agents (on December 15th, <em>see </em>note 5 supra), they said that his replies <em>could </em>be used against him. Under the standard of the <em>Uniformed Sanitation Mm </em>decisions, these three proceedings cannot be called “proper.” Plaintiff was not “duly advised of his options and the consequences of his choice.” Quite the opposite, he was left to squirm with a choice he should not have been put to — the possibility of going to jail or of losing his job. <em>Cf. Stevens </em>v. <em>Marks, </em><span class="citation" data-id="9423156"><a href="/opinion/107173/stevens-v-marks/" aria-description="Citation for case: Stevens v. Marks">383 U.S. 234</a></span> (1966).</p>
<p id="b610-6">The Government suggests that Mr. Kalkines, or at least <page-number citation-index="1" label="579">*579</page-number>his lawyer, should have known that his answers (and their fruits) could not be used to his disadvantage, and therefore that the explicit caution mandated by <em>Uniformed Sanitation Men II </em>might be omitted. With respect to the plaintiff, a frightened layman, this is certainly an unacceptable position; he could not be expected to know what lawyers and judges were even then arguing about. The case is hardly better for insisting that the attorney should have known, and should have been responsible for alerting his client. <em>Garriiy </em>v. <em>New </em><span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Jersey, <em>supra, </em></a></span><span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">385 U.S. 493</a></span>, was not decided until January 16, 1967, and its reach was uncertain for some years. <em><span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">Gardner</a></span> </em>and <em>Uniformed Sanitation Men I </em>did not come down until June 10, 1968 — after the last failure-to-respond charged against this plaintiff. <em>Uniformed Sanitation Men II </em>was not decided until April 3, 1970 (the Supreme Court did not decline review until May 30,1972). Many knowledgeable people believed that a specific immunity statute was necessary before anybody in the Federal Government could assure criminal immunity to individuals, including employees, being questioned in noncriminal proceedings. Perhaps, we may add, the law on the point is not yet wholly firm. At any rate, even the legendary Mr. Tutt, fictional legal genius of a generation or two ago, would have been hard put to know with any certainty, in the fall of 1967 and the spring of 1968, that this employee would be protected against prosecutorial use of his statements made to the customs agents.</p>
<p id="b611-6">This brings us to the last interview on June 5, 1968. Plaintiff was peremptorily ordered to come to Washington for this meeting with less than a day’s notice; he came without his lawyer who was engaged at the time on other urgent legal business and could not leave the New York area. The record contains a transcript of a portion of the interview. An agent opened by informing Mr. Kalkines that he was required to answer questions, and inquired whether he would “answer such questions as they pertain to your employee-employer relationship to the Bureau of Customs and the duties you perform on behalf of the Customs Service.” Plaintiff then said that he had “been advised by the customs agents that they are investigating me on an alleged criminal <page-number citation-index="1" label="580">*580</page-number>action. I was further advised by them to engage counsel.” He denied that he 'had refused to answer proper questions and went on to say that his attorney had advised him that “since this is a criminal action” the counsel should be present; “all I [plaintiff] ask is that if there is a criminal action pending against me that I have a right to have my counsel present.”</p>
<p id="b612-5">The agent replied “that the following interview is administrative in nature, that it is not criminal, that there is no criminal action pending against you and that the purpose of this interview is entirely on an employer-employee basis and that furthermore any answers given to questions put to you in the interview cannot and will not be used against you in any criminal action”; that if the interview were in connection with a criminal action the attorney would most certainly be permitted to be present and to advise; and “this is an administrative interview and do you understand that this interview is administrative and accordingly your attorney will not be permitted to be present during the interview.” The agent concluded these observations by asking plaintiff whether he would answer questions in counsel’s absence.</p>
<p id="b612-6">The defendant urges that this was proper and sufficient advice to Mr. Kalkines that he had immunity against use of his responses. But even the agent’s most explicit statement was incomplete since it did not refer to the fruits of the answers (in addition to the answers themselves). Moreover, and very significantly, the remainder of the colloquy shows that plaintiff was still very concerned about a criminal prosecution and that the agent never properly brought home that he would have immunity with respect to his answers. This portion of the interview is set forth in the footnote.<footnotemark>7</footnotemark></p>
<p id="b613-5"><page-number citation-index="1" label="581">*581</page-number>The essential aspects are four: First, in describing a “conduct” investigation the agent clearly indicated that a criminal investigation or trial was still possible; he contented himself with reiterating that his own concern was “administrative” and he was not pursuing a violation of criminal law, without denying that a criminal proceeding could possibly eventuate. Second, the agent never really responded to plaintiff’s query as to whether the criminal investigation had been dropped, and did not tell him that the U.S. Attorney had refused to go forward with prosecution.<footnotemark>8</footnotemark> Third, the agent failed to repeat or even refer to the earlier statement about non-use for criminal purposes of plaintiff’s answers in this “administrative” inquiry. Fourth, the plaintiff was obviously, and quite reasonably, left uncertain as to the connection between the questioning he was then being asked to undergo and a potential criminal action. This last element seems to us reinforced by some confused remarks of plaintiff’s later on in the exchange — after the agent had commenced to ask specific questions — which seem to express great doubt about the separation between the civil and criminal sides of the investigation.<footnotemark>9</footnotemark> Moreover, at the agency hearing, both the interrogating agent and the plaintiff made it clear in their testimony that <page-number citation-index="1" label="582">*582</page-number>plaintiff was fearful on June <em>5th that the </em>criminal aspect was still inextricably linked to the so-called “conduct investigation.”</p>
<p id="b614-5">The sum of this June 5th. episode is that, by failing to make and maintain a clear and unequivocal declaration of plaintiff’s “use” immunity, the customs agents gave the employee very good reason to be apprehensive that he could be walking into the criminal trap if he responded to potentially incriminating questions, and that in that dangerous situation he very much needed his lawyer’s help. The record compels this conclusion. Perhaps the agents were not more positive in their statements because there still remained at that time the possibility of prosecution.<footnotemark>10</footnotemark> Whatever the basis for their failure to clear up plaintiff’s reasonable doubts, we are convinced the record shows that he was not “duly advised of his options and •the consequences of his choice.”<footnotemark>11</footnotemark> His failure to respond was excused on this occasion, as on the earlier dates cited in the other specifications. The agency and the Civil Service Commission erred in disregarding this justification, and in holding that the duty to respond was absolute and was violated.</p>
<p id="b614-6">The result is that, for this reason,<footnotemark>12</footnotemark> plaintiff’s discharge in 1968 was invalid, and he is now entitled to recover his lost pay, less offsets. His motion for summary judgment is granted and the defendant’s is denied. The amount of recovery will be determined under Rule 131 (c) ,<footnotemark>13</footnotemark></p>
<footnote label="1">
<p id="b604-9"> The Customs Manual provided (§ 27.39(j)) : “Customs employees shall disclose any information in their possession pertaining to customs matters when requested to do so by a customs agent, and shall answer any proper questions put to them by customs agents.”</p>
<p id="b604-10">The Customs Personnel Manual stated (ch. 73,5, § 3, ¶ 3f) : “Every customs employee is required to disclose any information he has concerning customs matters when requested to do so by a customs agent. Every customs employee is required to answer any proper questions posed by a customs agent. Every customs employee, when requested to do so by a customs agent, shall furnish to such agent, or authorize him in writing to obtain, information of the employee’s financial affairs which bears a reasonable relationship to customs matters.”</p>
<p id="b604-11">The Treasury Personnel Manual declared (ch. 735, § 0.735-48) : “When directed to do so by competent Treasury authority, employees must testify or respond to questions (under oath when required) concerning matters of official interest. See further 31 CFR <em>1.10."</em></p>
</footnote>
<footnote label="2">
<p id="b604-12"> The original notice contained three other charges which were not sustained by the agency and are not before us.</p>
</footnote>
<footnote label="3">
<p id="b605-8"> There was a full-scale hearing within the Treasury Department (the “agency hearing”), which the record sets forth in question-and-answer form, as well as some additional testimony taken by the Civil Service Commission’s Regional Office, of which we have a narrative summary.</p>
</footnote>
<footnote label="4">
<p id="b607-8"> Those employees were advised as follows at the time management put the questions to them (<span class="citation" data-id="290212"><a href="/opinion/290212/uniformed-sanitation-men-association-inc-v-commissioner-of-sanitation-of/#621" aria-description="Citation for case: Uniformed Sanitation Men Association, Inc. v....">426 F. 2d at 621</a></span>) :</p>
<blockquote id="b607-9">“I want to advise you, Mr. -, that you have all the rights and privileges guaranteed by the Laws of the State of New Xork and the Constitution of this State and of the united States, including the right to be represented by counsel at this inquiry, the right to remain silent, although you may be subject to disciplinary action by the Department of Sanitation for the failure to answer material and relevant questions relating to the performance of your duties as an employee of the City of New Xork.</blockquote>
<blockquote id="b607-11">“I further advise you that the answers you may give to the questions propounded to you at this proceeding, or any information or evidence which is gained by reason of your answers, may not be used against you in a criminal proceeding except that you may be subject to criminal prosecution for any false answer that you may give under any applicable law, including Section 1121 of the New Xork City Charter.”</blockquote>
</footnote>
<footnote label="5">
<p id="b608-6"> Between November 28, 1967, and May 2, 1968, he had been called for an interview on December 15th. On this occasion he was informed, according to the Civil Service Commission’s Regional Office, "of his constitutional rights to remain silent and to have the presence of an attorney for consultation during the questioning, <em>and that anything he said could, he used against him in court proceedings" </em>(emphasis added). He answered the questions posed, and his conduct at that interview is not charged against him in the present proceedings.</p>
</footnote>
<footnote label="6">
<p id="b609-8"> We are also very dubious about a related bolding of tbe Board of Appeals and Review with respect to tbe first interview on November 28tb, <em>supra. </em>Tbe Regional Office accepted plaintiff’s testimony that on that day be was first confronted with a serious allegation of misconduct on bis part (with criminal implications) and as a consequence became nervous and flustered, being unable to continue the interview and just “closed down.” He did return the next day and answered detailed and extensive questions, including inquiries as to tbe $400 deposit on November 17th. On tbe basis of these facts, tbe Region found that plaintiff’s “first refusal to reply on November 2S, 1967 was effectively set aside as basis for the adverse action” and that tbe specification involving November 28th “is not sustained as substantive cause in support of that action.”</p>
<p id="b609-9">Again, without reversing the Regional Office’s finding of fact — paraphrased by the Board as: “the Region was persuaded that Mr. Kalkines’ refusal to cooperate at the first interview could be attributed to shock and mental stress” — .the Board of Appeals and Review reinstated that specification on the ground, apparently, that the duty to respond is so absolute that failure cannot be excused even by “shock and mental stress”, and even though the questions were answered the next day. This harsh position is very questionable. We have the greatest doubt that a federal employee can be validly discharged if it is determined, first, that his failure to answer queries on one day is due to such a disabling mental or emotional condition and, second, that he did respond to the questions shortly ther»after.</p>
</footnote>
<footnote label="7">
<p id="b612-7"> “A. To go over what you just said, are you stating that there Is no criminal Investigation relative to this matter, has this been dropped?</p>
<p id="b612-8">“Q. This Interview and the purpose of this interview Is purely administrative and is not a criminal action or related to a criminal action as it pertains to you.</p>
<p id="b612-9">“A. I don’t understand, you are not answering my question, is there an Investigation relative to me, a criminal investigation <em>1</em></p>
<p id="b612-10">“Q. No, there is a conduct investigation pending against you.</p>
<p id="b612-11">“A. For the record, may I state this is the first time that I have ever been told this. X have been advised for the last 6 months that I am under investigation for a criminal action and further I don’t know the difference between a conduct and a criminal action.</p>
<p id="b612-12">“Q. It is possible that if you have acted improper in the conduct of your business that your conduct may have involved conduct which is in violation <page-number citation-index="1" label="581">*581</page-number>of some criminal law. I restate that this interview is administrative and is not pursuing the violation of criminal law if one existed and in view of its administrative nature, your attorney will not be present. Please answer will you or will you not answer the questions I am about to put to you?</p>
<p id="Ayhs">“A. I can’t see the separation in which you call an administrative interview and the allegations that have unjustly been made against me. In my position, as I have stated, I will answer any and all questions regarding my customs duties gladly, cheerfully, openly, but I would lite to be afforded the opportunity of having my counsel .present.”</p>
</footnote>
<footnote label="8">
<p id="b613-11"> This is clear enough from the transcript of the interview. It is confirmed, moreover, by Mr. Kalkines’ explicit testimony at the agency hearing that at no time during that meeting did the agents tell him that criminal proceedings were not pending against him or that all criminal charges had been dropped. The agents did not testify to the contrary.</p>
</footnote>
<footnote label="9">
<p id="b613-13"> When the agent began to ash about the questioned customs transaction, the plaintiff repeated that he had never refused, and did not then refuse, to answer about his customs duties, that he wished counsel, and that he had previously answered that question. He went on: “The records cannot substantiate that to sit here and to state that there is disassoeiation between the allegation made against me and that this is merely the ordinary practice of Customs, I don’t think is correct. This is directly associated with an allegation against me and there is no disassoeiation, cannot be considered an administrative action, and again let me reiterate I have and will continue to answer every question relative to my customs duty, all I ask is that I have a right to have my counsel * *</p>
</footnote>
<footnote label="10">
<p id="b614-7"> There is a question whether the idea of a criminal proceeding had been entirely dropped by June 5th. The defendant says it had been but admits that formal notification to that effect was not given by the united States Attorney’s Office until some months later. In any event, the customs agent who interrogated plaintiff on June 5th conceded at the agency hearing that, if Mr. Kalkines had then made what appeared to the agents to be incriminating responses or had revealed circumstances which were obviously of a criminal nature, a report would probably have been made to the U.S. Attorney. The agent’s superior, who was present at the interrogation, testified at the agency hearing to similar effect.</p>
</footnote>
<footnote label="11">
<p id="b614-8"> An example of proper advice is that given in <em>Uniformed Sanitation Ken II, see </em>note 4 <em>supra.</em></p>
</footnote>
<footnote label="12">
<p id="b614-9"> We do not reach or consider any of plaintiff’s other contentions, including the argument that in any event he was entitled to the assistance of a lawyer at the May 8th and June 5th interviews even if properly advised as to his options.</p>
</footnote>
<footnote label="13">
<p id="b614-10"> Plaintiff is granted 30 days to file, if he desires, an amendment to his petition requesting restoration under <span class="citation no-link">Public Law 92-415, 86</span> Stat. 652 (August 29, 1972) to his position in the Bureau of Customs. <em>See </em>General Order No. 3 of 1972 (Dee. 12,1972), paras. 3(a), 4(b).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Kingsley v. Hendrickson.md  (`case`, 5 assertions)

### content_page

```
---
title: "Kingsley v. Hendrickson"
type: case
citation: ""
parallel_cite: "576 U.S. 389; 135 S. Ct. 2466; 192 L. Ed. 2d 416; 25 Fla. L. Weekly Fed. S 401; 83 U.S.L.W. 4515"
neutral_cite: 2015 U.S. LEXIS 4073
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2015
date_decided: 2015-06-22
docket: 14-6368
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2015-06-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Kingsley v. Hendrickson
  varies_by_point: false
  scope_note: "Good law: pretrial-detainee excessive-force claims use a purely objective-reasonableness standard under the Fourteenth Amendment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2811847/kingsley-v-hendrickson/"
  cluster_id: 2811847
  opinion_id: 9808641
  identity_checked: true
homes:
  - page: "[[Use of Force]]"
    role: "Key — Progeny / Refinement"
related: ["[[Graham v. Connor]]", "[[County of Sacramento v. Lewis]]"]
aliases: []
tags: ["case", "use-of-force", "pretrial-detainee", "objective-reasonableness", "fourteenth-amendment", "section-1983"]
holding: "A pretrial detainee's Fourteenth Amendment excessive-force claim requires only that the force purposely or knowingly used against him was objectively unreasonable; no subjective awareness of unreasonableness need be shown."
lake:
  record_id: Kingsley v. Hendrickson
  status: verified
  projected_at: 2026-07-06
---

# Kingsley v. Hendrickson

*576 U.S. 389 (2015)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Michael Kingsley, a pretrial detainee in a Wisconsin jail, refused to remove paper covering the light fixture in his cell. Officers forcibly removed him to a receiving cell, where — Kingsley alleged — they slammed his head against a concrete bunk and used a Taser on him. He sued under § 1983 for excessive force. The jury was instructed that he had to prove the officers "recklessly" disregarded his safety (a subjective element) and returned a verdict for the officers; the Seventh Circuit affirmed.

## Issue
Whether a pretrial detainee's excessive-force claim under the Fourteenth Amendment requires proof that the officers were subjectively aware that their use of force was unreasonable, or only that the force was objectively unreasonable.

## Rule
Only objective unreasonableness need be shown. "we agree with the dissenting appeals court judge, the Seventh Circuit's jury instruction committee, and Kingsley, that a pretrial detainee must show only that the force purposely or knowingly used against him was objectively unreasonable." — 576 U.S. at 396-397 (135 S. Ct. at 2473). ^pin-397

The use of force must be deliberate (purposeful or knowing, not accidental), but its reasonableness is judged from the perspective of a reasonable officer on the scene, on a non-exhaustive set of factors — not on the officer's subjective intent. This differs from the Eighth Amendment standard for convicted prisoners, which asks whether force was applied maliciously and sadistically.

## Application
Because the jury had been told to apply a subjective standard, asking whether the officers were aware their force was unreasonable, the instructions were erroneous: Kingsley needed to prove only that the deliberate force used against him was objectively unreasonable in light of the facts the officers confronted (the need for force, the threat reasonably perceived, his resistance, the injury, and efforts to temper the response). The Court [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]] for consideration under the correct objective standard.

## Conclusion
[[Reading and Citing Cases#vacated|Vacated]] and [[Reading and Citing Cases#on-remand|remanded]]. A pretrial detainee's Fourteenth Amendment excessive-force claim is governed by an objective-reasonableness standard, with no requirement to prove the officers' subjective intent to punish or awareness of unreasonableness.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Kingsley* extends an objective-reasonableness approach akin to [[Graham v. Connor]] to the pretrial-detention setting and distinguishes the [[County of Sacramento v. Lewis]] line on substantive-due-process culpability. Several circuits have since extended its objective framework to pretrial-detainee conditions and medical-care claims. No negative treatment.

## Appears on
- [[Use of Force]] — *Key — Progeny / Refinement*
- [[Section 1983 Liability and Qualified Immunity]] — *Related (cross-doctrine)*

## Sources
- *Kingsley v. Hendrickson*, 576 U.S. 389 (2015) — https://www.courtlistener.com/opinion/2811847/kingsley-v-hendrickson/ — pinpoint: 396-397 (135 S. Ct. at 2473, CL page-label confirmed; lead opinion id 9808641).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7cf9a497f3d4d14e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2015 U.S. LEXIS 4073", "official_citation_present": false, "parallel_cite": "576 U.S. 389; 135 S. Ct. 2466; 192 L. Ed. 2d 416; 25 Fla. L. Weekly Fed. S 401; 83 U.S.L.W. 4515", "title": "Kingsley v. Hendrickson", "year": "2015"}}
{"assertion_id": "a81c936ba684375c", "dimension": "support", "kind": "home_role", "locator": {"home": "Use of Force"}, "payload": {"home": "Use of Force", "role": "Key — Progeny / Refinement", "title": "Kingsley v. Hendrickson"}}
{"assertion_id": "ef9e48cdeb40b3d5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A pretrial detainee's Fourteenth Amendment excessive-force claim requires only that the force purposely or knowingly used against him was objectively unreasonable; no subjective awareness of unreasonableness need be shown.", "title": "Kingsley v. Hendrickson"}}
{"assertion_id": "46ff909a437c025e", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Kingsley v. Hendrickson"}}
{"assertion_id": "83f91e60e50652b6", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2015-06-22", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Kingsley v. Hendrickson", "field_i_validity": "good_law", "scope_note": "Good law: pretrial-detainee excessive-force claims use a purely objective-reasonableness standard under the Fourteenth Amendment.", "title": "Kingsley v. Hendrickson", "varies_by_point": "false"}}
```

### lake record — Kingsley v. Hendrickson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kingsley v. Hendrickson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Kingsley v. Hendrickson",
    "case_name_short": "Kingsley",
    "case_name_full": "Michael B. KINGSLEY, Petitioner v. Stan HENDRICKSON, Et Al.",
    "input_case_name": "Kingsley v. Hendrickson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2015-06-22",
    "year": 2015,
    "docket": "14-6368",
    "cluster_id": 2811847,
    "lead_opinion_id": 9808641,
    "sibling_ids": [
      2811847,
      9808641,
      9808642
    ],
    "absolute_url": "/opinion/2811847/kingsley-v-hendrickson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8174063,
        "score": 20,
        "case_name": "Kingsley v. Hendrickson"
      },
      {
        "cluster_id": 8172260,
        "score": 20,
        "case_name": "Kingsley v. Hendrickson"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "576 U.S. 389",
        "volume": "576",
        "reporter": "U.S.",
        "page": "389",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 S. Ct. 2466",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "2466",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "192 L. Ed. 2d 416",
        "volume": "192",
        "reporter": "L. Ed. 2d",
        "page": "416",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 401",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "401",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4515",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4515",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2015 U.S. LEXIS 4073",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "4073",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "576 U.S. 389",
        "volume": "576",
        "reporter": "U.S.",
        "page": "389",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 S. Ct. 2466",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "2466",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "192 L. Ed. 2d 416",
        "volume": "192",
        "reporter": "L. Ed. 2d",
        "page": "416",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 U.S. LEXIS 4073",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "4073",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 401",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "401",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4515",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4515",
        "type": 4,
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
      "id": "pin-397",
      "page": null,
      "quote": "disregarded his safety (a subjective element) and returned a verdict for the officers; the Seventh Circuit affirmed. ## Issue Whether a pretrial detainee's excessive-force claim under the Fourteenth Amendment requires proof that the officers were subjectively aware that their use of force was unreasonable, or only that the force was objectively unreasonable. ## Rule Only objective unreasonableness need be shown.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2015-06-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Kingsley v. Hendrickson",
    "varies_by_point": false,
    "scope_note": "Good law: pretrial-detainee excessive-force claims use a purely objective-reasonableness standard under the Fourteenth Amendment.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Foster v. Commissioner of Correction (No. 1)",
          "cluster_id": 4758096,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jonathon Castro v. County of Los Angeles",
          "cluster_id": 4247081,
          "cite": [
            "833 F.3d 1060",
            "2016 U.S. App. LEXIS 14950",
            "2016 WL 4268955"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Darnell v. City of New York",
          "cluster_id": 4369355,
          "cite": [
            "849 F.3d 17",
            "2017 WL 676521",
            "2017 U.S. App. LEXIS 2911"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alfredo Miranda v. County of Lake",
          "cluster_id": 4525558,
          "cite": [
            "900 F.3d 335"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mary Gordon v. County of Orange",
          "cluster_id": 4493836,
          "cite": [
            "888 F.3d 1118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barton Ex Rel. Estate of Barton v. Taber",
          "cluster_id": 3198370,
          "cite": [
            "820 F.3d 958",
            "2016 WL 1658098"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tapanga Hardeman v. David Wathen",
          "cluster_id": 4647629,
          "cite": [
            "933 F.3d 816"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony Mays v. Thomas Dart",
          "cluster_id": 4783259,
          "cite": [
            "974 F.3d 810"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heriberto Rodriguez v. County of Los Angeles",
          "cluster_id": 4502306,
          "cite": [
            "891 F.3d 776"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tammy Brawner v. Scott Cnty., Tenn.",
          "cluster_id": 5106013,
          "cite": [
            "14 F.4th 585"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Melisa Richmond v. Rubab Huq",
          "cluster_id": 4480081,
          "cite": [
            "885 F.3d 928"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
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
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shane Horton v. City of Santa Maria",
          "cluster_id": 4586718,
          "cite": [
            "915 F.3d 592"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Frost v. New York City Police Department",
          "cluster_id": 4805103,
          "cite": [
            "980 F.3d 231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gail Stockton v. Milwaukee County, Wisconsin",
          "cluster_id": 7855452,
          "cite": [
            "44 F.4th 605"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Denise Coley v. Lucas County, Ohio",
          "cluster_id": 2829693,
          "cite": [
            "799 F.3d 530",
            "2015 FED App. 0200P",
            "2015 U.S. App. LEXIS 14702",
            "2015 WL 4978463"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeffery Mays v. Ronald Sprinkle",
          "cluster_id": 4869132,
          "cite": [
            "992 F.3d 295"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Short v. J. Hartman",
          "cluster_id": 9450747,
          "cite": [
            "87 F.4th 593"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Eric Darden v. City of Fort Worth, Texas",
          "cluster_id": 4461803,
          "cite": [
            "880 F.3d 722"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Julie Helphenstine v. Lewis County",
          "cluster_id": 9374379,
          "cite": [
            "60 F.4th 305"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
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
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Larry Alderson v. Concordia Parish Corrtl Facil, e",
          "cluster_id": 4347641,
          "cite": [
            "848 F.3d 415",
            "2017 WL 541006",
            "2017 U.S. App. LEXIS 2382"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Altony Brooks v. Captain Jacumin",
          "cluster_id": 4618747,
          "cite": [
            "924 F.3d 104"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joan Kedra v. Richard Schroeter",
          "cluster_id": 4446761,
          "cite": [
            "876 F.3d 424"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Danzel Stearns v. Inmate Services Corporation",
          "cluster_id": 4749382,
          "cite": [
            "957 F.3d 902"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2811847 OR 9808641 OR 9808642) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDk0Mjg4MDAwMDAwJnM9NDM5MDAxOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%282811847+OR+9808641+OR+9808642%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(2811847 OR 9808641 OR 9808642)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzcmcz00NDg2MTU3JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%282811847+OR+9808641+OR+9808642%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2811847 OR 9808641 OR 9808642)",
        "reviewed": 73,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 73,
        "triage_read": 0,
        "triage_snippet_classified": 73
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2811847 OR 9808641 OR 9808642)",
    "indexed_citing_opinions": 284,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2811847,
        "count": 113,
        "count_source": "search"
      },
      {
        "opinion_id": 9808641,
        "count": 174,
        "count_source": "search"
      },
      {
        "opinion_id": 9808642,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4145,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/kingsley-v-hendrickson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxMTQwOTMmcz0xMDI5MTA2NyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%282811847+OR+9808641+OR+9808642%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2811847,
        "cited_id": 77039,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 109402,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 109635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 111198,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 111254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 111555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 111610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 111891,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 111904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 112626,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 112693,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 112833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 112924,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 118144,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 149651,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 312370,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 718230,
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
    "date_created": "2026-07-05T09:19:13Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T09:19:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T09:59:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:05:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T09:59:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Kingsley v. Hendrickson

```
<opinion type="majority">
<author id="p-11">Justice BREYERdelivered the opinion of the Court.</author>
<p id="p-12">In this case, an individual detained in a jail prior to trial brought a claim under Rev. Stat. § 1979, <extracted-citation index="0" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation>, against several jail officers, alleging that they used excessive force against him, in violation of the Fourteenth Amendment's Due Process Clause. The officers concede that they intended to use the force that they used. But the parties disagree about whether the force used was excessive.</p>
<p id="p-13">The question before us is whether, to prove an excessive force claim, a pretrial detainee must show that the officers were <em>subjectively</em>aware that their use of force was unreasonable, or only that the officers' use of that force was <em>objectively</em>unreasonable. We conclude that the latter standard is the correct one.</p>
<p id="p-14">I</p>
<p id="p-15">A</p>
<p id="p-16">Some but not all of the facts are undisputed: Michael Kingsley, the petitioner, was arrested on a drug charge and detained in a Wisconsin county jail prior to trial. On the evening of May 20, 2010, an officer performing a cell check noticed a piece of paper covering the light fixture above Kingsley's bed. The officer told Kingsley to remove it; Kingsley refused; subsequently other officers told Kingsley to remove the paper; and each time Kingsley refused. The next morning, the jail administrator, Lieutenant Robert Conroy, ordered Kingsley to remove the paper. Kingsley once again refused. Conroy then told Kingsley that officers would remove the paper and that he would be moved to a receiving cell in the interim.</p>
<p id="p-17">Shortly thereafter, four officers, including respondents Sergeant Stan Hendrickson and Deputy Sheriff Fritz Degner, approached the cell and ordered Kingsley to stand, back up to the door, and keep his hands behind him. When Kingsley refused to comply, the officers handcuffed him, forcibly removed him from the cell, carried him to a receiving cell, and placed him face down on a bunk with his hands handcuffed behind his back.</p>
<p id="p-18">The parties' views about what happened next differ. The officers testified that Kingsley resisted their efforts to remove his handcuffs. Kingsley testified that he did not resist. All agree that Sergeant Hendrickson placed his knee in Kingsley's back and Kingsley told him in impolite language to get off. Kingsley testified that Hendrickson and Degner then slammed his head into the concrete bunk-an allegation the officers deny.</p>
<p id="p-19">The parties agree, however, about what happened next: Hendrickson directed Degner to stun Kingsley with a Taser; Degner applied a Taser to Kingsley's back for approximately five seconds; the officers then left the handcuffed Kingsley alone in the receiving cell; and officers returned to the cell 15 minutes later and removed Kingsley's handcuffs.</p>
<p id="p-20">B</p>
<p id="p-21">Based on these and related events, Kingsley filed a § 1983complaint in Federal District Court claiming (among other <a class="page-label" data-citation-index="1" data-label="2471" href="#p2471" id="p2471">*2471</a>things) that Hendrickson and Degner used excessive force against him, in violation of the Fourteenth Amendment's Due Process Clause. The officers moved for summary judgment, which the District Court denied, stating that "a reasonable jury could conclude that [the officers] acted with malice and intended to harm [Kingsley] when they used force against him." <em>Kingsley v. Josvai,</em>No. 10-cv-832-bbc (WD Wis., Nov. 16, 2011), App to Pet. for Cert. 66a-67a. Kingsley's excessive force claim accordingly proceeded to trial. At the conclusion of the trial, the District Court instructed the jury as follows:</p>
<blockquote id="p-22">"Excessive force means force <em>applied recklessly</em>that is unreasonable in light of the facts and circumstances of the time. Thus, to succeed on his claim of excessive use of force, plaintiff must prove each of the following factors by a preponderance of the evidence:</blockquote>
<blockquote id="p-23">"(1) Defendants used force on plaintiff;</blockquote>
<blockquote id="p-24">"(2) Defendants' use of force was unreasonable in light of the facts and circumstances at the time;</blockquote>
<blockquote id="p-25">"(3) Defendants knew that using force presented a risk of harm to plaintiff, but they recklessly disregarded plaintiff's safety by failing to take reasonable measures to minimize the risk of harm to plaintiff; and</blockquote>
<blockquote id="p-26">"(4) Defendants' conduct caused some harm to plaintiff.</blockquote>
<blockquote id="p-27">"In deciding whether one or more defendants used 'unreasonable' force against plaintiff, you must consider whether it was unreasonable from the perspective of a reasonable officer facing the same circumstances that defendants faced. You must make this decision based on what defendants knew at the time of the incident, not based on what you know now.</blockquote>
<blockquote id="p-28">"Also, in deciding whether one or more defendants used unreasonable force and acted with <em>reckless disregard of plaintiff's rights</em>, you may consider factors such as:</blockquote>
<blockquote id="p-29">"• The need to use force;</blockquote>
<blockquote id="p-30">"• The relationship between the need to use force and the amount of force used;</blockquote>
<blockquote id="p-31">"• The extent of plaintiff's injury;</blockquote>
<blockquote id="p-32">"• Whether defendants reasonably believed there was a threat to the safety of staff or prisoners; and</blockquote>
<blockquote id="p-33">"• Any efforts made by defendants to limit the amount of force used." App. 277-278 (emphasis added).</blockquote>
<p id="p-34">The jury found in the officers' favor.</p>
<p id="p-35">On appeal, Kingsley argued that the correct standard for judging a pretrial detainee's excessive force claim is objective unreasonableness. And, the jury instruction, he said, did not hew to that standard. A panel of the Court of Appeals disagreed, with one judge dissenting. The majority held that the law required a "subjective inquiry" into the officer's state of mind. There must be " 'an actual intent to violate [the plaintiff's] rights or reckless disregard for his rights.' " <extracted-citation case-ids="4120237" index="1" url="https://cite.case.law/f3d/744/443/#p451"><span class="citation" data-id="9802445"><a href="/opinion/2708847/michael-kingsley-v-stan-hendrickson/" aria-description="Citation for case: Michael Kingsley v. Stan Hendrickson">744 F.3d 443</a></span></extracted-citation>, 451 (C.A.7 2014)(quoting <em>Wilson v. Williams,</em><extracted-citation case-ids="11645248" index="2" url="https://cite.case.law/f3d/83/870/#p875"><span class="citation" data-id="718230"><a href="/opinion/718230/jackie-wilson-v-james-k-williams/" aria-description="Citation for case: Jackie Wilson v. James K. Williams">83 F.3d 870</a></span></extracted-citation>, 875 (C.A.7 1996)). The dissent would have used instructions promulgated by the Committee on Pattern Civil Jury Instructions of the Seventh Circuit, which require a pretrial detainee claiming excessive force to show only that the use of force was objectively unreasonable. <extracted-citation case-ids="4120237" index="3" url="https://cite.case.law/f3d/744/443/#p451"><span class="citation" data-id="9802445"><a href="/opinion/2708847/michael-kingsley-v-stan-hendrickson/#455" aria-description="Citation for case: Michael Kingsley v. Stan Hendrickson">744 F.3d, at 455</a></span></extracted-citation>(opinion of Hamilton, J.); see Pattern Civ. Jury Instr. § 7.08 (2009). The dissent further stated that the District Court's use of the word "reckless" in the jury instruction added "an unnecessary and confusing element." <extracted-citation case-ids="4120237" index="4" url="https://cite.case.law/f3d/744/443/#p451"><span class="citation" data-id="9802445"><a href="/opinion/2708847/michael-kingsley-v-stan-hendrickson/" aria-description="Citation for case: Michael Kingsley v. Stan Hendrickson">744 F.3d, at 455</a></span></extracted-citation>.</p>
<p id="p-36">Kingsley filed a petition for certiorari asking us to determine whether the requirements <a class="page-label" data-citation-index="1" data-label="2472" href="#p2472" id="p2472">*2472</a>of a § 1983excessive force claim brought by a pretrial detainee must satisfy the subjective standard or only the objective standard. In light of disagreement among the Circuits, we agreed to do so. Compare, <em>e.g.,</em> <em>Murray v. Johnson No. 260,</em><extracted-citation index="5" url="https://cite.case.law/citations/?q=367%20Fed.%20Appx.%20196"><span class="citation" data-id="3804"><a href="/opinion/3804/murray-v-johnson-260/" aria-description="Citation for case: Murray v. Johnson 260">367 Fed.Appx. 196</a></span></extracted-citation>, 198 (C.A.2 2010); <em>Bozeman v. Orum,</em><extracted-citation case-ids="8938554" index="6" url="https://cite.case.law/f3d/422/1265/#p1271"><span class="citation" data-id="9415944"><a href="/opinion/77039/willie-h-bozeman-v-silas-orum-iii/" aria-description="Citation for case: Willie H. Bozeman v. Silas Orum, III">422 F.3d 1265</a></span></extracted-citation>, 1271 (C.A.11 2005)(<em>per curiam</em>), with <em>Aldini v. Johnson,</em><extracted-citation case-ids="3691423" index="7" url="https://cite.case.law/f3d/609/858/#p865"><span class="citation" data-id="149651"><a href="/opinion/149651/aldini-v-johnson/" aria-description="Citation for case: Aldini v. Johnson">609 F.3d 858</a></span></extracted-citation>, 865-866 (C.A.6 2010); <em>Young v. Wolfe,</em><extracted-citation index="8" url="https://cite.case.law/citations/?q=478%20Fed.%20Appx.%20354"><span class="citation" data-id="798412"><a href="/opinion/798412/john-young-v-aron-wolfe/" aria-description="Citation for case: John Young v. Aron Wolfe">478 Fed.Appx. 354</a></span></extracted-citation>, 356 (C.A.9 2012).</p>
<p id="p-37">II</p>
<p id="p-38">A</p>
<p id="p-39">We consider a legally requisite state of mind. In a case like this one, there are, in a sense, two separate state-of-mind questions. The first concerns the defendant's state of mind with respect to his physical acts-<em>i.e.,</em>his state of mind with respect to the bringing about of certain physical consequences in the world. The second question concerns the defendant's state of mind with respect to whether his use of force was "excessive." Here, as to the first question, there is no dispute. As to the second, whether to interpret the defendant's physical acts in the world as involving force that was "excessive," there is a dispute. We conclude with respect to that question that the relevant standard is objective not subjective. Thus, the defendant's state of mind is not a matter that a plaintiff is required to prove.</p>
<p id="p-40">Consider the series of physical events that take place in the world-a series of events that might consist, for example, of the swing of a fist that hits a face, a push that leads to a fall, or the shot of a Taser that leads to the stunning of its recipient. No one here denies, and we must assume, that, as to the series of events that have taken place in the world, the defendant must possess a purposeful, a knowing, or possibly a reckless state of mind. That is because, as we have stated, "liability for <em>negligently</em>inflicted harm is categorically beneath the threshold of constitutional due process." <em>County of Sacramento v. Lewis,</em><extracted-citation case-ids="11504410" index="9" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">523 U.S. 833</a></span></extracted-citation>, 849, <extracted-citation case-ids="11504410" index="10" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">118 S.Ct. 1708</a></span></extracted-citation>, <extracted-citation case-ids="11504410" index="11" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">140 L.Ed.2d 1043</a></span></extracted-citation> (1998)(emphasis added). See also <em>Daniels v. Williams,</em><extracted-citation case-ids="6204748" index="12" url="https://cite.case.law/us/474/327/#p331"><span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/" aria-description="Citation for case: Daniels v. Williams">474 U.S. 327</a></span></extracted-citation>, 331, <extracted-citation case-ids="6204748" index="13" url="https://cite.case.law/us/474/327/#p331"><span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/" aria-description="Citation for case: Daniels v. Williams">106 S.Ct. 662</a></span></extracted-citation>, <extracted-citation case-ids="6204748" index="14" url="https://cite.case.law/us/474/327/#p331"><span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/" aria-description="Citation for case: Daniels v. Williams">88 L.Ed.2d 662</a></span></extracted-citation> (1986)("Historically, this guarantee of due process has been applied to <em>deliberate</em> decisions of government officials to deprive a person of life, liberty, or property"). Thus, if an officer's Taser goes off by accident or if an officer unintentionally trips and falls on a detainee, causing him harm, the pretrial detainee cannot prevail on an excessive force claim. But if the use of force is deliberate-<em>i.e.,</em> purposeful or knowing-the pretrial detainee's claim may proceed. In the context of a police pursuit of a suspect the Court noted, though without so holding, that recklessness in some cases might suffice as a standard for imposing liability. See <span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#849" aria-description="Citation for case: County of Sacramento v. Lewis"><em>Lewis, supra,</em>at 849</a></span>, <extracted-citation case-ids="11504410" index="15" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">118 S.Ct. 1708</a></span></extracted-citation>. Whether that standard might suffice for liability in the case of an alleged mistreatment of a pretrial detainee need not be decided here; for the officers do not dispute that they acted purposefully or knowingly with respect to the force they used against Kingsley.</p>
<p id="p-41">We now consider the question before us here-the defendant's state of mind with respect to the proper <em>interpretation</em> of the force (a series of events in the world) that the defendant deliberately (not accidentally or negligently) used. In deciding whether the force deliberately used is, constitutionally speaking, "excessive," should courts use an objective standard only, or instead a subjective standard that takes into account a defendant's state of mind? It is with respect to <em>this</em> question that we hold that courts must use an <a class="page-label" data-citation-index="1" data-label="2473" href="#p2473" id="p2473">*2473</a>objective standard. In short, we agree with the dissenting appeals court judge, the Seventh Circuit's jury instruction committee, and Kingsley, that a pretrial detainee must show only that the force purposely or knowingly used against him was objectively unreasonable.</p>
<p id="p-42">A court (judge or jury) cannot apply this standard mechanically. See <span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#850" aria-description="Citation for case: County of Sacramento v. Lewis"><em>Lewis, supra,</em>at 850</a></span>, <extracted-citation case-ids="11504410" index="16" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">118 S.Ct. 1708</a></span></extracted-citation>. Rather, objective reasonableness turns on the "facts and circumstances of each particular case." <em>Graham v. Connor,</em><extracted-citation case-ids="605535" index="17" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U.S. 386</a></span></extracted-citation>, 396, <extracted-citation case-ids="605535" index="18" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">109 S.Ct. 1865</a></span></extracted-citation>, <extracted-citation case-ids="605535" index="19" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">104 L.Ed.2d 443</a></span></extracted-citation> (1989). A court must make this determination from the perspective of a reasonable officer on the scene, including what the officer knew at the time, not with the 20/20 vision of hindsight. See <em><extracted-citation case-ids="605535" index="20" url="https://cite.case.law/us/490/386/#p396">ibid</extracted-citation></em><extracted-citation case-ids="605535" index="20" url="https://cite.case.law/us/490/386/#p396">.</extracted-citation> A court must also account for the "legitimate interests that stem from [the government's] need to manage the facility in which the individual is detained," appropriately deferring to "policies and practices that in th[e] judgment" of jail officials "are needed to preserve internal order and discipline and to maintain institutional security." <em>Bell v. Wolfish,</em><extracted-citation case-ids="1780223" index="21" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">441 U.S. 520</a></span></extracted-citation>, 540, 547, <extracted-citation case-ids="1780223" index="22" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>, <extracted-citation case-ids="1780223" index="23" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">60 L.Ed.2d 447</a></span></extracted-citation> (1979).</p>
<p id="p-43">Considerations such as the following may bear on the reasonableness or unreasonableness of the force used: the relationship between the need for the use of force and the amount of force used; the extent of the plaintiff's injury; any effort made by the officer to temper or to limit the amount of force; the severity of the security problem at issue; the threat reasonably perceived by the officer; and whether the plaintiff was actively resisting. See, <em>e.g.,</em><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor"><em>Graham, supra,</em>at 396</a></span>, <extracted-citation case-ids="605535" index="24" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">109 S.Ct. 1865</a></span></extracted-citation>. We do not consider this list to be exclusive. We mention these factors only to illustrate the types of objective circumstances potentially relevant to a determination of excessive force.</p>
<p id="p-44">B</p>
<p id="p-45">Several considerations have led us to conclude that the appropriate standard for a pretrial detainee's excessive force claim is solely an objective one. For one thing, it is consistent with our precedent. We have said that "the Due Process Clause protects a pretrial detainee from the use of excessive force that amounts to punishment." <em>Graham,</em> <em>supra,</em>at 395, n. 10, <extracted-citation case-ids="605535" index="25" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">109 S.Ct. 1865</a></span></extracted-citation>. And in <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span>,</em>we explained that such "punishment" can consist of actions taken with an "expressed intent to punish." <extracted-citation case-ids="1780223" index="26" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">441 U.S., at 538</a></span></extracted-citation>, <extracted-citation case-ids="1780223" index="27" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. But the <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>Court went on to explain that, in the absence of an expressed intent to punish, a pretrial detainee can nevertheless prevail by showing that the actions are not "rationally related to a legitimate nonpunitive governmental purpose" or that the actions "appear excessive in relation to that purpose."<span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#561" aria-description="Citation for case: Bell v. Wolfish"><em>Id.,</em>at 561</a></span>, <extracted-citation case-ids="1780223" index="28" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. The <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>Court applied this latter objective standard to evaluate a variety of prison conditions, including a prison's practice of double-bunking. In doing so, it did not consider the prison officials' subjective beliefs about the policy. <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#541" aria-description="Citation for case: Bell v. Wolfish"><em>Id.,</em>at 541-543</a></span>, <extracted-citation case-ids="1780223" index="29" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. Rather, the Court examined objective evidence, such as the size of the rooms and available amenities, before concluding that the conditions were reasonably related to the legitimate purpose of holding detainees for trial and did not appear excessive in relation to that purpose. <em><extracted-citation case-ids="1780223" index="30" url="https://cite.case.law/us/441/520/#p540">Ibid</extracted-citation></em><extracted-citation case-ids="1780223" index="30" url="https://cite.case.law/us/441/520/#p540">.</extracted-citation></p>
<p id="p-46"><em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>'s focus on "punishment" does not mean that proof of intent (or motive) to punish is required for a pretrial detainee to prevail on a claim that his due process rights were violated. Rather, as <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>itself shows (and as our later precedent affirms), a pretrial detainee can prevail by providing only objective evidence that the challenged governmental action is not rationally related <a class="page-label" data-citation-index="1" data-label="2474" href="#p2474" id="p2474">*2474</a>to a legitimate governmental objective or that it is excessive in relation to that purpose. Cf. <em>Block v. Rutherford,</em><extracted-citation case-ids="11339397" index="31" url="https://cite.case.law/us/468/576/#p585"><span class="citation" data-id="9429742"><a href="/opinion/111254/block-v-rutherford/" aria-description="Citation for case: Block v. Rutherford">468 U.S. 576</a></span></extracted-citation>, 585-586, <extracted-citation case-ids="11339397" index="32" url="https://cite.case.law/us/468/576/#p585"><span class="citation" data-id="9429742"><a href="/opinion/111254/block-v-rutherford/" aria-description="Citation for case: Block v. Rutherford">104 S.Ct. 3227</a></span></extracted-citation>, <extracted-citation case-ids="11339397" index="33" url="https://cite.case.law/us/468/576/#p585"><span class="citation" data-id="9429742"><a href="/opinion/111254/block-v-rutherford/" aria-description="Citation for case: Block v. Rutherford">82 L.Ed.2d 438</a></span></extracted-citation> (1984)(where there was no suggestion that the purpose of jail policy of denying contact visitation was to punish inmates, the Court need only evaluate whether the policy was "reasonably related to legitimate governmental objectives" and whether it appears excessive in relation to that objective); <em>Schall v. Martin,</em><extracted-citation case-ids="6198853" index="34" url="https://cite.case.law/us/467/253/#p269"><span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/" aria-description="Citation for case: Schall v. Martin">467 U.S. 253</a></span></extracted-citation>, 269-271, <extracted-citation case-ids="6198853" index="35" url="https://cite.case.law/us/467/253/#p269"><span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/" aria-description="Citation for case: Schall v. Martin">104 S.Ct. 2403</a></span></extracted-citation>, <extracted-citation case-ids="6198853" index="36" url="https://cite.case.law/us/467/253/#p269"><span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/" aria-description="Citation for case: Schall v. Martin">81 L.Ed.2d 207</a></span></extracted-citation> (1984)(similar); see also <em>United States v. Salerno,</em><extracted-citation case-ids="6222105" index="37" url="https://cite.case.law/us/481/739/#p747"><span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/" aria-description="Citation for case: United States v. Salerno">481 U.S. 739</a></span></extracted-citation>, 747, <extracted-citation case-ids="6222105" index="38" url="https://cite.case.law/us/481/739/#p747"><span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/" aria-description="Citation for case: United States v. Salerno">107 S.Ct. 2095</a></span></extracted-citation>, <extracted-citation case-ids="6222105,1148012" index="39" url="https://cite.case.law/l-ed-2d/95/697/"><span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/" aria-description="Citation for case: United States v. Salerno">95 L.Ed.2d 697</a></span></extracted-citation> (1987)("[T]he punitive/regulatory distinction <em>turns on</em>'whether an alternative purpose to which [the restriction] may rationally be connected is assignable for it, and whether it appears excessive in relation to the alternative purpose assigned [to it]' " (quoting <span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/#269" aria-description="Citation for case: Schall v. Martin"><em>Schall, supra,</em>at 269</a></span>, <extracted-citation case-ids="6198853" index="40" url="https://cite.case.law/us/467/253/#p269"><span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/" aria-description="Citation for case: Schall v. Martin">104 S.Ct. 2403</a></span></extracted-citation>; emphasis added and some internal quotation marks omitted)). The Court did not suggest in any of these cases, either by its words or its analysis, that its application of <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>'s objective standard should involve subjective considerations. Our standard is also consistent with our use of an objective "excessive force" standard where officers apply force to a person who, like Kingsley, has been accused but not convicted of a crime, but who, unlike Kingsley, is free on bail. See <em>Graham, <extracted-citation case-ids="605535" index="41" url="https://cite.case.law/us/490/386/#p396">supra</extracted-citation></em><extracted-citation case-ids="605535" index="41" url="https://cite.case.law/us/490/386/#p396">.</extracted-citation></p>
<p id="p-47">For another thing, experience suggests that an objective standard is workable. It is consistent with the pattern jury instructions used in several Circuits. We are also told that many facilities, including the facility at issue here, train officers to interact with all detainees as if the officers' conduct is subject to an objective reasonableness standard. See Brief for Petitioner 26; App. 247-248; Brief for Former Corrections Administrators and Experts as <em>Amici Curiae</em>8-18.</p>
<p id="p-48">Finally, the use of an objective standard adequately protects an officer who acts in good faith. We recognize that "[r]unning a prison is an inordinately difficult undertaking," <em>Turner v. Safley,</em><extracted-citation case-ids="6210045" index="42" url="https://cite.case.law/us/482/78/#p84"><span class="citation" data-id="9431005"><a href="/opinion/111904/turner-v-safley/" aria-description="Citation for case: Turner v. Safley">482 U.S. 78</a></span></extracted-citation>, 84-85, <extracted-citation case-ids="6210045" index="43" url="https://cite.case.law/us/482/78/#p84"><span class="citation" data-id="9431005"><a href="/opinion/111904/turner-v-safley/" aria-description="Citation for case: Turner v. Safley">107 S.Ct. 2254</a></span></extracted-citation>, <extracted-citation case-ids="6210045" index="44" url="https://cite.case.law/us/482/78/#p84"><span class="citation" data-id="9431005"><a href="/opinion/111904/turner-v-safley/" aria-description="Citation for case: Turner v. Safley">96 L.Ed.2d 64</a></span></extracted-citation> (1987), and that "safety and order at these institutions requires the expertise of correctional officials, who must have substantial discretion to devise reasonable solutions to the problems they face," <em>Florence v. Board of Chosen Freeholders of County of Burlington,</em>566 U.S. ----, ----, <extracted-citation case-ids="12189139" index="45" url="https://cite.case.law/us/566/318/#p1515"><span class="citation" data-id="9485643"><a href="/opinion/626454/florence-v-board-of-chosen-freeholders-of-county-of-burlington/" aria-description="Citation for case: Florence v. Board of Chosen Freeholders of County of...">132 S.Ct. 1510</a></span></extracted-citation>, 1515, <extracted-citation case-ids="12189139" index="46" url="https://cite.case.law/us/566/318/#p1515"><span class="citation" data-id="9485643"><a href="/opinion/626454/florence-v-board-of-chosen-freeholders-of-county-of-burlington/" aria-description="Citation for case: Florence v. Board of Chosen Freeholders of County of...">182 L.Ed.2d 566</a></span></extracted-citation> (2012). Officers facing disturbances "are often forced to make split-second judgments-in circumstances that are tense, uncertain, and rapidly evolving." <em>Graham,</em><extracted-citation case-ids="605535" index="47" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U.S., at 397</a></span></extracted-citation>, <extracted-citation case-ids="605535" index="48" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">109 S.Ct. 1865</a></span></extracted-citation>. For these reasons, we have stressed that a court must judge the reasonableness of the force used from the perspective and with the knowledge of the defendant officer. We have also explained that a court must take account of the legitimate interests in managing a jail, acknowledging as part of the objective reasonableness analysis that deference to policies and practices needed to maintain order and institutional security is appropriate. See Part II-A, <em>supra.</em>And we have limited liability for excessive force to situations in which the use of force was the result of an intentional and knowing act (though we leave open the possibility of including a "reckless" act as well). <em><extracted-citation case-ids="605535" index="49" url="https://cite.case.law/us/490/386/#p396">Ibid.</extracted-citation></em> Additionally, an officer enjoys qualified immunity and is not liable for excessive force unless he has violated a "clearly established" right, such that "it would [have been] clear to a reasonable officer that his conduct was unlawful in the situation he confronted." <em>Saucier v. Katz,</em><extracted-citation case-ids="9313023" index="50" url="https://cite.case.law/us/533/194/#p202"><span class="citation multiple-matches"><a href="/c/U.S./533/194/">533 U.S. 194</a></span></extracted-citation>, 202, <extracted-citation case-ids="9313023" index="51" url="https://cite.case.law/us/533/194/#p202"><span class="citation multiple-matches"><a href="/c/S.Ct./121/2151/">121 S.Ct. 2151</a></span></extracted-citation>, <extracted-citation case-ids="9313023" index="52" url="https://cite.case.law/us/533/194/#p202"><span class="citation multiple-matches"><a href="/c/L.Ed.2d/150/272/">150 L.Ed.2d 272</a></span></extracted-citation> (2001); see also Brief for United States as <em>Amicus Curiae</em>27-28. It is unlikely (though theoretically possible)</p>
<p id="p-49"><a class="page-label" data-citation-index="1" data-label="2475" href="#p2475" id="p2475">*2475</a>that a plaintiff could overcome these hurdles where an officer acted in good faith.</p>
<p id="p-50">C</p>
<p id="p-51">Respondents believe that the relevant legal standard should be subjective, <em>i.e.,</em>that the plaintiff must prove that the use of force was not "applied in a good-faith effort to maintain or restore discipline" but, rather, was applied "maliciously and sadistically to cause harm." Brief for Respondents 27. And they refer to several cases that they believe support their position. See <em>id.,</em>at 26-31 (citing <em>Whitley v. Albers,</em><extracted-citation case-ids="6202378" index="53" url="https://cite.case.law/us/475/312/"><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">475 U.S. 312</a></span></extracted-citation>, <extracted-citation case-ids="6202378" index="54" url="https://cite.case.law/us/475/312/"><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">106 S.Ct. 1078</a></span></extracted-citation>, <extracted-citation case-ids="6202378" index="55" url="https://cite.case.law/us/475/312/"><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">89 L.Ed.2d 251</a></span></extracted-citation> (1986); <em>Hudson v. McMillian,</em><extracted-citation case-ids="6219215" index="56" url="https://cite.case.law/us/503/1/"><span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/" aria-description="Citation for case: Hudson v. McMillian">503 U.S. 1</a></span></extracted-citation>, <extracted-citation case-ids="6219215" index="57" url="https://cite.case.law/us/503/1/"><span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/" aria-description="Citation for case: Hudson v. McMillian">112 S.Ct. 995</a></span></extracted-citation>, <extracted-citation case-ids="6219215" index="58" url="https://cite.case.law/us/503/1/"><span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/" aria-description="Citation for case: Hudson v. McMillian">117 L.Ed.2d 156</a></span></extracted-citation> (1992); <em>Lewis,</em><extracted-citation case-ids="11504410" index="59" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">523 U.S. 833</a></span></extracted-citation>, <extracted-citation case-ids="11504410" index="60" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">118 S.Ct. 1708</a></span></extracted-citation>, <extracted-citation case-ids="11504410" index="61" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">140 L.Ed.2d 1043</a></span></extracted-citation>; <em>Johnson v. Glick,</em><extracted-citation case-ids="1318048" index="62" url="https://cite.case.law/f2d/481/1028/"><span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">481 F.2d 1028</a></span></extracted-citation> (C.A.2 1973)).</p>
<p id="p-52">The first two of these cases, however, concern excessive force claims brought by convicted prisoners under the Eighth Amendment's Cruel and Unusual Punishment Clause, not claims brought by pretrial detainees under the Fourteenth Amendment's Due Process Clause. <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#320" aria-description="Citation for case: Whitley v. Albers"><em>Whitley, supra,</em>at 320</a></span>, <extracted-citation case-ids="6202378" index="63" url="https://cite.case.law/us/475/312/"><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">106 S.Ct. 1078</a></span></extracted-citation>; <span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/#6" aria-description="Citation for case: Hudson v. McMillian"><em>Hudson, supra,</em>at 6-7</a></span>, <extracted-citation case-ids="6219215" index="64" url="https://cite.case.law/us/503/1/"><span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/" aria-description="Citation for case: Hudson v. McMillian">112 S.Ct. 995</a></span></extracted-citation>. The language of the two Clauses differs, and the nature of the claims often differs. And, most importantly, pretrial detainees (unlike convicted prisoners) cannot be punished at all, much less "maliciously and sadistically<em>.</em>" <em>Ingraham v. Wright,</em><extracted-citation case-ids="12126861" index="65" url="https://cite.case.law/us/430/651/#p671"><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">430 U.S. 651</a></span></extracted-citation>, 671-672, n. 40, <extracted-citation case-ids="12126861" index="66" url="https://cite.case.law/us/430/651/#p671"><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">97 S.Ct. 1401</a></span></extracted-citation>, <extracted-citation case-ids="12126861" index="67" url="https://cite.case.law/us/430/651/#p671"><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">51 L.Ed.2d 711</a></span></extracted-citation> (1977); <em>Graham,</em> <em>supra,</em>at 395, n. 10, <extracted-citation case-ids="605535" index="68" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">109 S.Ct. 1865</a></span></extracted-citation> (1989); see also 4 W. Blackstone, Commentaries *300 ("[I]f the offence be not bailable, or the party cannot find bail, he is to be committed to the county [jail] ... [b]ut ... only for safe custody, and not for punishment"). Thus, there is no need here, as there might be in an Eighth Amendment case, to determine when punishment is unconstitutional. <em><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">Whitley</a></span></em>and <em>Hudson</em>are relevant here only insofar as they address the practical importance of taking into account the legitimate safety-related concerns of those who run jails. And, as explained above, we believe we have done so.</p>
<p id="p-53"><em><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">Lewis</a></span></em>does not prove respondents' point, either. There, the Court considered a claim that a police officer had violated due process by causing a death during a high-speed automobile chase aimed at apprehending a suspect. We wrote that "[j]ust as a purpose to cause harm is needed for Eighth Amendment liability in a [prison] riot case, so it ought to be needed for due process liability in a pursuit case." <extracted-citation case-ids="11504410" index="69" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">523 U.S., at 854</a></span></extracted-citation>, <extracted-citation case-ids="11504410" index="70" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">118 S.Ct. 1708</a></span></extracted-citation>. Respondents contend that this statement shows that the Court embraced a standard for due process claims that requires a showing of subjective intent. Brief for Respondents 30-31. Other portions of the <em><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">Lewis</a></span></em>opinion make clear, however, that this statement referred to the defendant's intent to commit the <em>acts</em> in question, not to whether the force intentionally used was "excessive." <extracted-citation case-ids="11504410" index="71" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">523 U.S., at 854</a></span></extracted-citation>, and n. 13, <extracted-citation case-ids="11504410" index="72" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">118 S.Ct. 1708</a></span></extracted-citation>. As explained above, the parties here do not dispute that respondents' use of force was intentional. See Part II-A, <em>supra</em>.</p>
<p id="p-54">Nor does <em><span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">Glick</a></span></em>provide respondents with significant support. In that case Judge Friendly, writing for the Second Circuit, considered an excessive force claim brought by a pretrial detainee under the Fourteenth Amendment's Due Process Clause. Judge Friendly pointed out that the "management by a few guards of large numbers of prisoners" in an institution "may require and justify the occasional use of a degree of intentional force." <extracted-citation case-ids="1318048" index="73" url="https://cite.case.law/f2d/481/1028/"><span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">481 F.2d, at 1033</a></span></extracted-citation>. He added that, in determining whether that intentional use of force "crosse[s]" the "constitutional line," a court should look:</p>
<blockquote id="p-55"><a class="page-label" data-citation-index="1" data-label="2476" href="#p2476" id="p2476">*2476</a>"to such factors as [ (1) ] the need for the application of force, [ (2) ] the relationship between the need and the amount of force that was used, [ (3) ] the extent of injury inflicted, and [ (4) ] whether force was applied in a good faith effort to maintain or restore discipline or maliciously and sadistically for the very purpose of causing harm." <em><extracted-citation case-ids="1318048" index="74" url="https://cite.case.law/f2d/481/1028/"><span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">Ibid.</a></span></extracted-citation></em></blockquote>
<p id="p-56">This statement does not suggest that the fourth factor (malicious and sadistic purpose to cause harm) is a <em>necessary</em>condition for liability. To the contrary, the words "such ... as" make clear that the four factors provide examples of some considerations, among others, that might help show that the use of force was excessive.</p>
<p id="p-57">Respondents believe these cases nonetheless help them make a broader point-namely, that a subjective standard "protects against a relative flood of claims," many of them perhaps unfounded, brought by pretrial detainees. Brief for Respondents 38. But we note that the Prison Litigation Reform Act of 1995, 42 U.S.C. § 1997e, which is designed to deter the filing of frivolous litigation against prison officials, applies to both pretrial detainees and convicted prisoners. Nor is there evidence of a rash of unfounded filings in Circuits that use an objective standard.</p>
<p id="p-58">We acknowledge that our view that an objective standard is appropriate in the context of excessive force claims brought by pretrial detainees pursuant to the Fourteenth Amendment may raise questions about the use of a subjective standard in the context of excessive force claims brought by convicted prisoners. We are not confronted with such a claim, however, so we need not address that issue today.</p>
<p id="p-59">III</p>
<p id="p-60">We now consider the lawfulness of the jury instruction given in this case in light of our adoption of an objective standard for pretrial detainees' excessive force claims. See Part II-A, <em>supra</em>. That jury instruction defined "excessive force" as "force applied recklessly that is unreasonable in light of the facts and circumstances of the time." App. 277. It required Kingsley to show that the officers "recklessly disregarded [Kingsley's] safety." <em>Id.,</em>at 278. And it suggested that Kingsley must show the defendants "acted with reckless disregard of [Kingsley's] rights," while telling the jury that it could consider several objective factors in making this determination. <em>Ibid</em>.</p>
<p id="p-61">Kingsley argues that the jury instruction is faulty because the word "reckless" suggests a need to prove that respondents acted with a certain subjective state of mind with respect to the excessive or nonexcessive nature of the force used, contrary to what we have just held. Reply Brief 20-22. Respondents argue that irrespective of our holding, any error in the instruction was harmless. Brief for Respondents 57-58. And the Solicitor General suggests that, because the instructions defined "recklessness" with reference to objective factors, those instructions effectively embody our objective standard and did not confuse the jury. Brief for United States as <em>Amicus Curiae</em>28-32.</p>
<p id="p-62">We agree with Kingsley that the instructions were erroneous. "[R]eckles[s] disregar[d] [of Kingsley's] safety" was listed as an additional requirement, beyond the need to find that "[respondents'] use of force was unreasonable in light of the facts and circumstances at the time." App. 278. See also <em>ibid.</em>(Kingsley had to show respondents "used unreasonable force <em>and</em>acted with reckless disregard of [Kingsley's] rights" (emphasis added)). And in determining whether respondents "acted with reckless disregard of [Kingsley's] rights," the jury was instructed to "consider <a class="page-label" data-citation-index="1" data-label="2477" href="#p2477" id="p2477">*2477</a>... [w]hether [respondents] reasonably <em>believed</em>there was a threat to the safety of staff or prisoners." <em>Ibid.</em>(emphasis added). Together, these features suggested the jury should weigh respondents' subjective reasons for using force and subjective views about the excessiveness of the force. As we have just held, that was error. But because the question whether that error was harmless may depend in part on the detailed specifics of this case, we leave that question for the Court of Appeals to resolve in the first instance.</p>
<p id="p-63">The decision of the Court of Appeals is vacated, and the case is remanded for proceedings consistent with this opinion.</p>
<p id="p-64"><em>It is so ordered.</em></p>
<p id="p-65">Justice SCALIA, with whom THE CHIEF JUSTICE and Justice THOMAS join, dissenting.</p>
<p id="p-66">The Constitution contains no freestanding prohibition of excessive force. There are, however, four constitutional provisions that we have said forbid the use of excessive force in certain circumstances. The Fourth Amendment prohibits it when it makes a search or seizure "unreasonable." The Eighth Amendment prohibits it when it constitutes "cruel and unusual" punishment. The Fifth and Fourteenth Amendments prohibit it (or, for that matter, any use of force) when it is used to "deprive" someone of "life, liberty, or property, without due process of law."</p>
<p id="p-67">This is a Fourteenth Amendment case. The Fifth Amendment applies only to federal actors; Kingsley forfeited any argument under the Fourth Amendment by failing to raise it below; and he acknowledges that the Eighth Amendment standard is inapplicable, Brief for Petitioner 27, n. 8. The only question before us is whether a pretrial detainee's due process rights are violated when "the force purposely or knowingly used against him [is] objectively unreasonable." <em>Ante,</em> at 2473. In my view, the answer is no. Our cases hold that the intentional infliction of punishment upon a pretrial detainee may violate the Fourteenth Amendment; but the infliction of "objectively unreasonable" force, without more, is not the intentional infliction of punishment.</p>
<p id="p-68">In <em>Bell v. Wolfish,</em><extracted-citation case-ids="1780223" index="75" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">441 U.S. 520</a></span></extracted-citation>, <extracted-citation case-ids="1780223" index="76" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>, <extracted-citation case-ids="1780223" index="77" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">60 L.Ed.2d 447</a></span></extracted-citation> (1979), we held that the Due Process Clause forbids holding pretrial detainees in conditions that "amount to punishment." <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#535" aria-description="Citation for case: Bell v. Wolfish"><em>Id.,</em>at 535</a></span>, <extracted-citation case-ids="1780223" index="78" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. Conditions amount to punishment, we explained, when they are "imposed for the purpose of punishment." <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#538" aria-description="Citation for case: Bell v. Wolfish"><em>Id.,</em>at 538</a></span>, <extracted-citation case-ids="1780223" index="79" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. Acting with the intent to punish means taking a " 'deliberate act intended to chastise or deter.' " <em>Wilson v. Seiter,</em><extracted-citation case-ids="1107993" index="80" url="https://cite.case.law/us/501/294/#p300"><span class="citation" data-id="9432339"><a href="/opinion/112626/wilson-v-seiter/" aria-description="Citation for case: Wilson v. Seiter">501 U.S. 294</a></span></extracted-citation>, 300, <extracted-citation case-ids="1107993" index="81" url="https://cite.case.law/us/501/294/#p300"><span class="citation" data-id="9432339"><a href="/opinion/112626/wilson-v-seiter/" aria-description="Citation for case: Wilson v. Seiter">111 S.Ct. 2321</a></span></extracted-citation>, <extracted-citation case-ids="1107993" index="82" url="https://cite.case.law/us/501/294/#p300"><span class="citation" data-id="9432339"><a href="/opinion/112626/wilson-v-seiter/" aria-description="Citation for case: Wilson v. Seiter">115 L.Ed.2d 271</a></span></extracted-citation> (1991)(quoting <em>Duckworth v. Franzen,</em><extracted-citation case-ids="1531408" index="83" url="https://cite.case.law/f2d/780/645/#p652"><span class="citation" data-id="462687"><a href="/opinion/462687/junior-ray-duckworth-cross-appellants-v-gayle-franzen-cross-appellees/" aria-description="Citation for case: Junior Ray Duckworth, Cross-Appellants v. Gayle Franzen,...">780 F.2d 645</a></span></extracted-citation>, 652 (C.A.7 1985)); see also <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#537" aria-description="Citation for case: Bell v. Wolfish"><em>Bell, supra,</em>at 537-538</a></span>, <extracted-citation case-ids="1780223" index="84" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. The Court in <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>recognized that intent to punish need not be "expressed," <extracted-citation case-ids="1780223" index="85" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">441 U.S. at 538</a></span></extracted-citation>, <extracted-citation case-ids="1780223" index="86" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>, but may be established with circumstantial evidence. More specifically, if the condition of confinement being challenged "is not reasonably related to a legitimate goal-if it is arbitrary or purposeless-a court permissibly may infer that the purpose of the governmental action is punishment." <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#539" aria-description="Citation for case: Bell v. Wolfish"><em>Id.,</em>at 539</a></span>, <extracted-citation case-ids="1780223" index="87" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. We endorsed the same inference when we applied <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>'s intent-to-punish test in challenges brought by pretrial detainees against jailhouse security policies, <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#560" aria-description="Citation for case: Bell v. Wolfish"><em>id.,</em>at 560-562</a></span>, <extracted-citation case-ids="1780223" index="88" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>; <em>Block v. Rutherford,</em><extracted-citation case-ids="11339397" index="89" url="https://cite.case.law/us/468/576/#p585"><span class="citation" data-id="9429742"><a href="/opinion/111254/block-v-rutherford/" aria-description="Citation for case: Block v. Rutherford">468 U.S. 576</a></span></extracted-citation>, 583-584, <extracted-citation case-ids="11339397" index="90" url="https://cite.case.law/us/468/576/#p585"><span class="citation" data-id="9429742"><a href="/opinion/111254/block-v-rutherford/" aria-description="Citation for case: Block v. Rutherford">104 S.Ct. 3227</a></span></extracted-citation>, <extracted-citation case-ids="11339397" index="91" url="https://cite.case.law/us/468/576/#p585"><span class="citation" data-id="9429742"><a href="/opinion/111254/block-v-rutherford/" aria-description="Citation for case: Block v. Rutherford">82 L.Ed.2d 438</a></span></extracted-citation> (1984), and statutes permitting pretrial detention, <em>Schall v. Martin,</em><extracted-citation case-ids="6198853" index="92" url="https://cite.case.law/us/467/253/#p269"><span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/" aria-description="Citation for case: Schall v. Martin">467 U.S. 253</a></span></extracted-citation>, 255, 269, <extracted-citation case-ids="6198853" index="93" url="https://cite.case.law/us/467/253/#p269"><span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/" aria-description="Citation for case: Schall v. Martin">104 S.Ct. 2403</a></span></extracted-citation>, <extracted-citation case-ids="6198853" index="94" url="https://cite.case.law/us/467/253/#p269"><span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/" aria-description="Citation for case: Schall v. Martin">81 L.Ed.2d 207</a></span></extracted-citation> (1984); <em>United States v. Salerno,</em><extracted-citation case-ids="6222105" index="95" url="https://cite.case.law/us/481/739/#p747"><span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/" aria-description="Citation for case: United States v. Salerno">481 U.S. 739</a></span></extracted-citation>, 741, 746-747, <extracted-citation case-ids="6222105" index="96" url="https://cite.case.law/us/481/739/#p747"><span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/" aria-description="Citation for case: United States v. Salerno">107 S.Ct. 2095</a></span></extracted-citation>, <extracted-citation case-ids="6222105,1148012" index="97" url="https://cite.case.law/l-ed-2d/95/697/"><span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/" aria-description="Citation for case: United States v. Salerno">95 L.Ed.2d 697</a></span></extracted-citation> (1987).</p>
<p id="p-69"><a class="page-label" data-citation-index="1" data-label="2478" href="#p2478" id="p2478">*2478</a>In light of these cases, I agree with the Court that "the Due Process Clause protects a pretrial detainee from the use of excessive force that amounts to punishment." <em>Graham v. Connor,</em><extracted-citation case-ids="605535" index="98" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U.S. 386</a></span></extracted-citation>, 395, n. 10, <extracted-citation case-ids="605535" index="99" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">109 S.Ct. 1865</a></span></extracted-citation>, <extracted-citation case-ids="605535" index="100" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">104 L.Ed.2d 443</a></span></extracted-citation> (1989)(citing <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#535" aria-description="Citation for case: Bell v. Wolfish"><em>Bell, supra,</em>at 535-539</a></span>, <extracted-citation case-ids="1780223" index="101" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>). I disagree, however, that any intentional application of force that is objectively unreasonable in degree is a use of excessive force that "amount[s] to punishment." <em>Bell,</em><extracted-citation case-ids="1780223" index="102" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">441 U.S., at 535</a></span></extracted-citation>, <extracted-citation case-ids="1780223" index="103" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. The Court reaches that conclusion by misreading <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>as forbidding States to take <em>any</em> harmful action against pretrial detainees that is not "reasonably related to a legitimate goal." <em><extracted-citation case-ids="1780223" index="104" url="https://cite.case.law/us/441/520/#p540">Id</extracted-citation></em><extracted-citation case-ids="1780223" index="104" url="https://cite.case.law/us/441/520/#p540">., at 539</extracted-citation>, <extracted-citation case-ids="1780223" index="105" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>.</p>
<p id="p-70"><em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>endorsed this "reasonable relation" inference in the context of a challenge <em>to conditions of a confinement</em>-specifically, challenges to the State's policy of housing two people in each cell, <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#528" aria-description="Citation for case: Bell v. Wolfish"><em>id.,</em>at 528</a></span>, 99 S.Ct. 1861and various security policies, <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#548" aria-description="Citation for case: Bell v. Wolfish"><em>id.,</em>at 548-549, 553, 555, 558, 560-562</a></span>, <extracted-citation case-ids="1780223" index="106" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. The conditions in which pretrial detainees are held, and the security policies to which they are subject, are the result of considered deliberation by the authority imposing the detention. If those conditions and policies lack any reasonable relationship to a legitimate, nonpunitive goal, it is logical to infer a punitive intent. And the same logic supports finding a punitive intent in statutes authorizing detention that lacks any reasonable relationship to a valid government interest. <span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/#269" aria-description="Citation for case: Schall v. Martin"><em>Schall, supra,</em>at 269</a></span>, <extracted-citation case-ids="6198853" index="107" url="https://cite.case.law/us/467/253/#p269"><span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/" aria-description="Citation for case: Schall v. Martin">104 S.Ct. 2403</a></span></extracted-citation>; <span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/#746" aria-description="Citation for case: United States v. Salerno"><em>Salerno, supra,</em>at 746-747</a></span>, <extracted-citation case-ids="6222105" index="108" url="https://cite.case.law/us/481/739/#p747"><span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/" aria-description="Citation for case: United States v. Salerno">107 S.Ct. 2095</a></span></extracted-citation>.</p>
<p id="p-71">It is <em>illogical,</em>however, automatically to infer punitive intent from the fact that a prison guard used more force against a pretrial detainee than was necessary. That could easily have been the result of a misjudgment about the degree of force required to maintain order or protect other inmates, rather than the product of an intent to punish the detainee for his charged crime (or for any other behavior). An officer's decision regarding how much force to use is made "in haste, under pressure, and frequently without the luxury of a second chance," <em>Hudson v. McMillian,</em><extracted-citation case-ids="6219215" index="109" url="https://cite.case.law/us/503/1/"><span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/" aria-description="Citation for case: Hudson v. McMillian">503 U.S. 1</a></span></extracted-citation>, 6, <extracted-citation case-ids="6219215" index="110" url="https://cite.case.law/us/503/1/"><span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/" aria-description="Citation for case: Hudson v. McMillian">112 S.Ct. 995</a></span></extracted-citation>, <extracted-citation case-ids="6219215" index="111" url="https://cite.case.law/us/503/1/"><span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/" aria-description="Citation for case: Hudson v. McMillian">117 L.Ed.2d 156</a></span></extracted-citation> (1992)(internal quotation marks omitted), not after the considered thought that precedes detention-policy determinations like those at issue in <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span>,</em><em>Block,</em><em>Schall,</em>and <em><span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/" aria-description="Citation for case: United States v. Salerno">Salerno</a></span></em>. That an officer used more force than necessary might be <em>evidence</em>that he acted with intent to punish, but it is no more than that.</p>
<p id="p-72">In sum: <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>makes intent to punish the focus of its due-process analysis. Objective reasonableness of the force used is nothing more than a heuristic for identifying this intent. That heuristic makes good sense for considered decisions by the detaining authority, but is much weaker in the context of excessive-force claims. Kingsley does not argue that respondents actually intended to punish him, and his reliance on <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>to infer such an intent is misplaced.</p>
<p id="p-73">Kingsley claims that "the protections of due process ... extend beyond the narrow context of 'punishment.' " Brief for Petitioner 15. Unquestionably. A State would plainly violate the Due Process Clause if it extended a detainee's confinement because it believed him mentally ill (not as "punishment"), without giving him the constitutionally guaranteed processes that must precede the deprivation of liberty. But Kingsley does not claim deprivation of liberty in that normal sense of that word-the right to walk about free. He claims that the Due Process Clause confers, on pretrial detainees, a substantive "liberty" interest that consists of freedom from objectively unreasonable force. Kingsley seeks relief, in other words, under <a class="page-label" data-citation-index="1" data-label="2479" href="#p2479" id="p2479">*2479</a>the doctrine of "substantive due process," through which we have occasionally recognized "liberty" interests other than freedom from incarceration or detention, that "cannot be limited at all, except by provisions that are 'narrowly tailored to serve a compelling state interest.' " <em>Kerry v. Din,</em> --- U.S. ----, ----, <extracted-citation case-ids="12590180" index="112" url="https://cite.case.law/s-ct/135/2128/#p2133"><span class="citation" data-id="2808292"><a href="/opinion/2808292/kerry-v-din/" aria-description="Citation for case: Kerry v. Din">135 S.Ct. 2128</a></span></extracted-citation>, 2133, --- L.Ed.2d ---- (2015)(plurality opinion) (quoting <em>Reno v. Flores,</em><extracted-citation case-ids="6228898" index="113" url="https://cite.case.law/us/507/292/#p301"><span class="citation" data-id="9432751"><a href="/opinion/112833/reno-v-flores/" aria-description="Citation for case: Reno v. Flores">507 U.S. 292</a></span></extracted-citation>, 301-302, <extracted-citation case-ids="6228898" index="114" url="https://cite.case.law/us/507/292/#p301"><span class="citation" data-id="9432751"><a href="/opinion/112833/reno-v-flores/" aria-description="Citation for case: Reno v. Flores">113 S.Ct. 1439</a></span></extracted-citation>, <extracted-citation case-ids="6228898" index="115" url="https://cite.case.law/us/507/292/#p301"><span class="citation" data-id="9432751"><a href="/opinion/112833/reno-v-flores/" aria-description="Citation for case: Reno v. Flores">123 L.Ed.2d 1</a></span></extracted-citation> (1993)).</p>
<p id="p-74">Even if one believed that the right to process can confer the right to substance in particular cases, Kingsley's interest is not one of the "fundamental liberty interests" that substantive due process protects. We have said that that doctrine protects only those liberty interests that, carefully described, are "objectively, deeply rooted in this Nation's history and tradition, and implicit in the concept of ordered liberty, such that neither liberty nor justice would exist if they were sacrificed." <em>Washington v. Glucksberg,</em><extracted-citation case-ids="916123" index="116" url="https://cite.case.law/us/521/702/#p720"><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">521 U.S. 702</a></span></extracted-citation>, 720-721, <extracted-citation case-ids="916123" index="117" url="https://cite.case.law/us/521/702/#p720"><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">117 S.Ct. 2258</a></span></extracted-citation>, <extracted-citation case-ids="916123" index="118" url="https://cite.case.law/us/521/702/#p720"><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">138 L.Ed.2d 772</a></span></extracted-citation> (1997)(citations and internal quotation marks omitted). Carefully described, the liberty interest Kingsley asserts is the right of pretrial detainees to be free from the application of force that is more than is objectively required to further some legitimate, nonpunitive, governmental interest. He does not argue (nor could he) that this asserted interest could pass the test announced in <em><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">Glucksberg</a></span></em>.</p>
<p id="p-75">I conclude by emphasizing that our Constitution is not the only source of American law. There is an immense body of state statutory and common law under which individuals abused by state officials can seek relief. Kingsley himself, in addition to suing respondents for excessive force under <extracted-citation index="119" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation>, brought a state-law claim for assault and battery. <extracted-citation case-ids="4120237" index="120" url="https://cite.case.law/f3d/744/443/#p451"><span class="citation" data-id="9802445"><a href="/opinion/2708847/michael-kingsley-v-stan-hendrickson/" aria-description="Citation for case: Michael Kingsley v. Stan Hendrickson">744 F.3d 443</a></span></extracted-citation>, 446, n. 6 (C.A.7 2014). The Due Process Clause is not "a font of tort law to be superimposed upon" that state system. <em>Daniels v. Williams,</em><extracted-citation case-ids="6204748" index="121" url="https://cite.case.law/us/474/327/#p331"><span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/" aria-description="Citation for case: Daniels v. Williams">474 U.S. 327</a></span></extracted-citation>, 332, <extracted-citation case-ids="6204748" index="122" url="https://cite.case.law/us/474/327/#p331"><span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/" aria-description="Citation for case: Daniels v. Williams">106 S.Ct. 662</a></span></extracted-citation>, <extracted-citation case-ids="6204748" index="123" url="https://cite.case.law/us/474/327/#p331"><span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/" aria-description="Citation for case: Daniels v. Williams">88 L.Ed.2d 662</a></span></extracted-citation> (1986)(quoting <em>Paul v. Davis,</em><extracted-citation case-ids="12027375" index="124" url="https://cite.case.law/us/424/693/#p701"><span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/" aria-description="Citation for case: Paul v. Davis">424 U.S. 693</a></span></extracted-citation>, 701, <extracted-citation case-ids="12027375" index="125" url="https://cite.case.law/us/424/693/#p701"><span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/" aria-description="Citation for case: Paul v. Davis">96 S.Ct. 1155</a></span></extracted-citation>, <extracted-citation case-ids="12027375" index="126" url="https://cite.case.law/us/424/693/#p701"><span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/" aria-description="Citation for case: Paul v. Davis">47 L.Ed.2d 405</a></span></extracted-citation> (1976)). Today's majority overlooks this in its tender-hearted desire to tortify the Fourteenth Amendment.</p>
</opinion>
```

---
