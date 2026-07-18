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

## GROUP: content/cases/United States v. Miller.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Miller"
type: case
citation: "425 U.S. 435 (1976)"
parallel_cite: "96 S. Ct. 1619; 48 L. Ed. 2d 71; 37 A.F.T.R.2d (RIA) 1261"
neutral_cite: 1976 U.S. LEXIS 148
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-04-21
docket: 74-1179
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-04-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Miller
  varies_by_point: false
  scope_note: "Foundational third-party-doctrine case (bank records); remains good law. Carpenter v. United States (2018) declined to extend the third-party doctrine to cell-site location information but expressly did not overrule Miller."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109433/united-states-v-miller/"
  cluster_id: 109433
  opinion_id: 9426375
  identity_checked: true
homes:
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Key — Anchor"
related: ["[[Smith v. Maryland]]", "[[Carpenter v. United States]]", "[[Katz v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "third-party-doctrine", "bank-records", "standing"]
holding: "No legitimate expectation of privacy in bank records (checks, deposit slips) voluntarily conveyed to a bank; a depositor assumes the risk the bank will disclose them to the government (third-party doctrine)."
lake:
  record_id: United States v. Miller
  status: verified
  projected_at: 2026-07-09
---

# United States v. Miller

*425 U.S. 435 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
During an investigation into untaxed-whiskey offenses, federal agents obtained Miller's bank records — microfilmed checks, deposit slips, and financial statements — from two banks through grand-jury subpoenas. Miller moved to suppress the records, arguing the government's acquisition of his financial records from the banks was an unreasonable search and seizure of materials in which he had a Fourth Amendment interest.

## Issue
Whether a bank depositor has a Fourth Amendment-protected expectation of privacy in financial records (cancelled checks, deposit slips, and statements) maintained by his bank, so that the government's acquisition of them constitutes a search or seizure as to the depositor.

## Rule
No. The records are the bank's business records, and the depositor has no legitimate expectation of privacy in information he conveys to the bank. "All of the documents obtained, including financial statements and deposit slips, contain only information voluntarily conveyed to the banks and exposed to their employees in the ordinary course of business." — 425 U.S. at 442. ^pin-442

That voluntary exposure forfeits any Fourth Amendment claim: "The depositor takes the risk, in revealing his affairs to another, that the information will be conveyed by that person to the Government." — [*Id.* at 443](https://www.courtlistener.com/opinion/109433/united-states-v-miller/#:~:text=The%20depositor%20takes%20the%20risk%2C). ^pin-443

## Application
The checks were not confidential communications but negotiable instruments used in commercial transactions, and the statements and deposit slips contained only information Miller had voluntarily handed to his banks and exposed to their employees in the ordinary course of business. Because the records were not Miller's private papers and he had assumed the risk the banks would disclose them, he had no legitimate expectation of privacy and no Fourth Amendment interest the government's acquisition could invade.

## Conclusion
Miller had no protectable Fourth Amendment interest in the bank records; obtaining them worked no search or seizure as to him. With [[Smith v. Maryland]] (dialed numbers), *Miller* is a pillar of the third-party doctrine the Court later confronted for digital data in [[Carpenter v. United States]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Miller* remains good law. [[Carpenter v. United States]] (2018) declined to extend the third-party doctrine to historical cell-site location information, but **expressly declined to overrule** *Miller* or [[Smith v. Maryland]]; the bank-records holding stands. (The result also prompted the statutory Right to Financial Privacy Act, a non-constitutional check.)

## Appears on
- [[Third-Party Doctrine & CSLI]] — *Key — Anchor*

## Sources
- *United States v. Miller*, 425 U.S. 435 (1976) — https://www.courtlistener.com/opinion/109433/united-states-v-miller/ — pinpoints: 442, 443.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "edd39ddc24d2e628", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "425 U.S. 435 (1976)", "court": "U.S. Supreme Court", "neutral_cite": "1976 U.S. LEXIS 148", "official_citation_present": true, "parallel_cite": "96 S. Ct. 1619; 48 L. Ed. 2d 71; 37 A.F.T.R.2d (RIA) 1261", "title": "United States v. Miller", "year": "1976"}}
{"assertion_id": "5359bb92b17ad131", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "No legitimate expectation of privacy in bank records (checks, deposit slips) voluntarily conveyed to a bank; a depositor assumes the risk the bank will disclose them to the government (third-party doctrine).", "title": "United States v. Miller"}}
{"assertion_id": "6359b7dd8bdf7e18", "dimension": "support", "kind": "home_role", "locator": {"home": "Third-Party Doctrine & CSLI"}, "payload": {"home": "Third-Party Doctrine & CSLI", "role": "Key — Anchor", "title": "United States v. Miller"}}
{"assertion_id": "436c02e2ebb75d30", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1976-04-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Miller", "field_i_validity": "good_law", "scope_note": "Foundational third-party-doctrine case (bank records); remains good law. Carpenter v. United States (2018) declined to extend the third-party doctrine to cell-site location information but expressly did not overrule Miller.", "title": "United States v. Miller", "varies_by_point": "false"}}
{"assertion_id": "ff2e4a6b0fd85fb3", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Miller"}}
```

### lake record — United States v. Miller

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Miller",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Miller",
    "case_name_short": "",
    "case_name_full": "United States v. Miller",
    "input_case_name": "United States v. Miller",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-04-21",
    "year": 1976,
    "docket": "74-1179",
    "cluster_id": 109433,
    "lead_opinion_id": 9426375,
    "sibling_ids": [
      109433,
      9426375,
      9426376,
      9426377
    ],
    "absolute_url": "/opinion/109433/united-states-v-miller/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "425 U.S. 435",
      "volume": "425",
      "reporter": "U.S.",
      "page": "435",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 1619",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "1619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "48 L. Ed. 2d 71",
        "volume": "48",
        "reporter": "L. Ed. 2d",
        "page": "71",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 A.F.T.R.2d (RIA) 1261",
        "volume": "37",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1261",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 148",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "148",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "425 U.S. 435",
        "volume": "425",
        "reporter": "U.S.",
        "page": "435",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 1619",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "1619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "48 L. Ed. 2d 71",
        "volume": "48",
        "reporter": "L. Ed. 2d",
        "page": "71",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 148",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "148",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 A.F.T.R.2d (RIA) 1261",
        "volume": "37",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1261",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "425 U.S. 435",
    "official_selection": {
      "court_class": "scotus",
      "selected": "425 U.S. 435",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-442",
      "page": null,
      "quote": "--- # United States v. Miller *425 U.S. 435 (1976)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background During an investigation into untaxed-whiskey offenses, federal agents obtained Miller's bank records \u2014 microfilmed checks, deposit slips, and financial statements \u2014 from two banks through grand-jury subpoenas. Miller moved to suppress the records, arguing the government's acquisition of his financial records from the banks was an unreasonable search and seizure of materials in which he had a Fourth Amendment interest. ## Issue Whether a bank depositor has a Fourth Amendment-protected expectation of privacy in financial records (cancelled checks, deposit slips, and statements) maintained by his bank, so that the government's acquisition of them constitutes a search or seizure as to the depositor. ## Rule No. The records are the bank's business records, and the depositor has no legitimate expectation of privacy in information he conveys to the bank.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-443",
      "page": null,
      "quote": "The depositor takes the risk, in revealing his affairs to another, that the information will be conveyed by that person to the Government.",
      "star_marker": "443",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15418,
      "fragment": "#:~:text=The%20depositor%20takes%20the%20risk%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-04-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Miller",
    "varies_by_point": false,
    "scope_note": "Foundational third-party-doctrine case (bank records); remains good law. Carpenter v. United States (2018) declined to extend the third-party doctrine to cell-site location information but expressly did not overrule Miller.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Lepage",
          "cluster_id": 9503197,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hoffman",
          "cluster_id": 10135310,
          "cite": [
            "321 Or. App. 330",
            "515 P.3d 912"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ajemian v. Yahoo!, Inc.",
          "cluster_id": 4434746,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Fulgiam",
          "cluster_id": 4389223,
          "cite": [
            "477 Mass. 20",
            "73 N.E.3d 798"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Zodhiates",
          "cluster_id": 7318729,
          "cite": [
            "166 F. Supp. 3d 328",
            "2016 U.S. Dist. LEXIS 55748",
            "2016 WL 1594558"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri v. Sandra G. Plunkett",
          "cluster_id": 2827918,
          "cite": [
            "473 S.W.3d 166",
            "2015 Mo. App. LEXIS 827"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jon Thomas Ford v. State",
          "cluster_id": 2719207,
          "cite": [
            "444 S.W.3d 171",
            "2014 Tex. App. LEXIS 9159",
            "2014 WL 4099731"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Augustine",
          "cluster_id": 6580805,
          "cite": [
            "467 Mass. 230",
            "4 N.E.3d 846",
            "2014 WL 901649",
            "2014 Mass. LEXIS 30"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Leotis B. Branigh, III",
          "cluster_id": 1034108,
          "cite": [
            "155 Idaho 404",
            "313 P.3d 732",
            "2013 WL 3718751",
            "2013 Ida. App. LEXIS 63"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
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
        "journal_ref": "United States v. Miller:lane2_top_cited"
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
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Maryland",
          "cluster_id": 110118,
          "cite": [
            "61 L. Ed. 2d 220",
            "99 S. Ct. 2577",
            "442 U.S. 735",
            "1979 U.S. LEXIS 134"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Martinez-Fuerte",
          "cluster_id": 109541,
          "cite": [
            "49 L. Ed. 2d 1116",
            "96 S. Ct. 3074",
            "428 U.S. 543",
            "1976 U.S. LEXIS 87"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nixon v. Administrator of General Services",
          "cluster_id": 109729,
          "cite": [
            "53 L. Ed. 2d 867",
            "97 S. Ct. 2777",
            "433 U.S. 425",
            "1977 U.S. LEXIS 24",
            "2 Media L. Rep. (BNA) 2025"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Andresen v. Maryland",
          "cluster_id": 109522,
          "cite": [
            "49 L. Ed. 2d 627",
            "96 S. Ct. 2737",
            "427 U.S. 463",
            "1976 U.S. LEXIS 78"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Ciraolo",
          "cluster_id": 111666,
          "cite": [
            "90 L. Ed. 2d 210",
            "106 S. Ct. 1809",
            "476 U.S. 207",
            "1986 U.S. LEXIS 154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carpenter v. United States",
          "cluster_id": 4510032,
          "cite": [
            "585 U.S. 296",
            "138 S. Ct. 2206",
            "201 L. Ed. 2d 507",
            "2018 U.S. LEXIS 3844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
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
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 622304,
          "cite": [
            "181 L. Ed. 2d 911",
            "132 S. Ct. 945",
            "565 U.S. 400",
            "2012 U.S. LEXIS 1063"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karo",
          "cluster_id": 111257,
          "cite": [
            "82 L. Ed. 2d 530",
            "104 S. Ct. 3296",
            "468 U.S. 705",
            "1984 U.S. LEXIS 148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Payner",
          "cluster_id": 110317,
          "cite": [
            "65 L. Ed. 2d 468",
            "100 S. Ct. 2439",
            "447 U.S. 727",
            "1980 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Edmunds",
          "cluster_id": 2316698,
          "cite": [
            "586 A.2d 887",
            "526 Pa. 374",
            "1991 Pa. LEXIS 28"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Campbell",
          "cluster_id": 4463634,
          "cite": [
            "2018 COA 5",
            "425 P.3d 1163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
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
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Kennedy",
          "cluster_id": 1142841,
          "cite": [
            "666 P.2d 1316",
            "295 Or. 260",
            "1983 Ore. LEXIS 1311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Warshak",
          "cluster_id": 181032,
          "cite": [
            "631 F.3d 266",
            "2010 U.S. App. LEXIS 25415",
            "2010 WL 5071766"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Moore",
          "cluster_id": 1147295,
          "cite": [
            "782 P.2d 91",
            "109 N.M. 119"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hunt",
          "cluster_id": 2285004,
          "cite": [
            "450 A.2d 952",
            "91 N.J. 338",
            "1982 N.J. LEXIS 2189"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hardy",
          "cluster_id": 1494781,
          "cite": [
            "963 S.W.2d 516",
            "1997 WL 716775"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Sell",
          "cluster_id": 1462347,
          "cite": [
            "470 A.2d 457",
            "504 Pa. 46",
            "1983 Pa. LEXIS 792"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cecil Dwayne Evans, Arnold Gene Tate, and Charles Edward Gent, Jr.",
          "cluster_id": 354019,
          "cite": [
            "572 F.2d 455"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hempele",
          "cluster_id": 1435469,
          "cite": [
            "576 A.2d 793",
            "120 N.J. 182",
            "1990 N.J. LEXIS 92"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. DeJohn",
          "cluster_id": 2055341,
          "cite": [
            "403 A.2d 1283",
            "486 Pa. 32",
            "1979 Pa. LEXIS 572"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109433 OR 9426375 OR 9426376 OR 9426377) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjc5MjM4NDAwMDAwJnM9MTUwODEyJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109433+OR+9426375+OR+9426376+OR+9426377%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 12,
        "triage_snippet_classified": 188
      },
      "lane2_top_cited": {
        "query": "cites:(109433 OR 9426375 OR 9426376 OR 9426377)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTQmcz0yNDQ2ODgyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109433+OR+9426375+OR+9426376+OR+9426377%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109433 OR 9426375 OR 9426376 OR 9426377)",
        "reviewed": 29,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 29,
        "triage_read": 1,
        "triage_snippet_classified": 28
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109433 OR 9426375 OR 9426376 OR 9426377)",
    "indexed_citing_opinions": 766,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109433,
        "count": 639,
        "count_source": "search"
      },
      {
        "opinion_id": 9426375,
        "count": 148,
        "count_source": "search"
      },
      {
        "opinion_id": 9426376,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426377,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1198,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-miller.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5OTgyNzQmcz0xMDEyNDY0MCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109433+OR+9426375+OR+9426376+OR+9426377%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109433,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 104239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 108236,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 108650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 109005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 109257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 109380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 109402,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 320663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 1172381,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 2301022,
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
    "date_created": "2026-07-06T01:42:56Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:43:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:43:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:47:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:43:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Miller

```
<opinion type="majority">
<author id="b506-9">Mr. Justice Powell</author>
<p id="AvQ">delivered the opinion of the Court.</p>
<p id="b506-10">Respondent was convicted of possessing an unregistered still, carrying on the business of a distiller without giving bond and with intent to defraud the Government of whiskey tax, possessing 175 gallons of whiskey upon which no taxes had been paid, and conspiring to defraud the United States of tax revenues. <span class="citation no-link">26 U. S. C. §§ 5179</span>, 5205, 5601 <em>et seq.; </em><span class="citation no-link">18 U. S. C. § 371</span>. Prior to trial respondent moved to suppress copies of checks and other bank records obtained by means of allegedly defective subpoenas <em>duces tecum </em>served upon two banks at which he had accounts. The records had been maintained by the banks in compliance with the requirements of the Bank Secrecy Act of 1970, <span class="citation no-link">84 Stat. 1114</span>, 12 U. S. C. § 1829b (d).</p>
<p id="b507-4"><page-number citation-index="1" label="437">*437</page-number>The District Court overruled respondent’s motion to suppress, and the evidence was admitted. The Court of Appeals for the Fifth Circuit reversed on the ground that a depositor’s Fourth Amendment rights are violated when bank records maintained pursuant to the Bank Secrecy Act are obtained by means of a defective subpoena. It held that any evidence so obtained must be suppressed. Since we find that respondent had no pro-tectable Fourth Amendment interest in the subpoenaed documents, we reverse the decision below.</p>
<p id="b507-5">I</p>
<p id="b507-6">On December 18, 1972, in response to an informant’s tip, a deputy sheriff from Houston County, Ga., stopped a van-type truck occupied by two of respondent’s alleged co-conspirators. The truck contained distillery apparatus and raw material. On January 9, 1973, a fire broke out in a Kathleen, Ga., warehouse rented to respondent. During the blaze firemen and sheriff department officials discovered a 7,500-gallon-eapacity distillery, 175 gallons of non-tax-paid whiskey, and related paraphernalia.</p>
<p id="b507-7">Two weeks later agents from the Treasury Department’s Alcohol, Tobacco and Firearms Bureau presented grand jury subpoenas issued in blank by the clerk of the District Court, and completed by the United States Attorney’s office, to the presidents of the Citizens &amp; Southern National Bank of Warner Robins and the Bank of Byron, where respondent maintained accounts. The subpoenas required the two presidents to appear on January 24, 1973, and to produce</p>
<blockquote id="b507-8">“all records of accounts, <em>i. e., </em>savings, checking, loan or otherwise, in the name of Mr. Mitch Miller [respondent], 3859 Mathis Street, Macon, Ga. and/or Mitch Miller Associates, 100 Executive <page-number citation-index="1" label="438">*438</page-number>Terrace, Warner Robins, Ga., from October 1, 1972, through the present date [January 22, 1973, in the case of the Bank of Byron, and January 23, 1973, in the case of the Citizens &amp; Southern National Bank of Warner Robins]</blockquote>
<p id="b508-5">The banks did not advise respondent that the subpoenas had been served but ordered their employees to make the records available and to provide copies .of any documents the agents desired. At the Bank of Byron, an agent was shown microfilm records of the relevant account and provided with copies of one deposit slip and one or two checks. At the Citizens &amp; Southern National Bank microfilm records also were shown to the agent, and he was given copies-of the records of respondent's account during the applicable period. These included all checks, deposit slips, two financial statements, and three monthly statements. The bank presidents were then told that it would not be necessary to appear in person before the grand jury.</p>
<p id="b508-6">The grand jury met on February 12, 1973, 19 days after the return date on the subpoenas. Respondent and four others were indicted. The overt acts alleged to have been committed in furtherance of the conspiracy included three financial transactions — the rental by respondent of the van-type truck, the purchase by respondent of radio equipment, and the purchase by respondent of a quantity of sheet metal and metal pipe. The record does not indicate whether any of the bank records were in fact presented to the grand jury. They were used in the investigation and provided “one or two" investigatory leads. Copies of the checks also were introduced at trial to establish the overt acts described above.</p>
<p id="b508-7">In his motion to suppress, denied by the District Court, respondent contended that the bank documents were illegally seized. It was urged that the subpoenas were <page-number citation-index="1" label="439">*439</page-number>defective because they were issued by the United States Attorney rather than a court, no return was made to a court, and the subpoenas were returnable on a date when the grand jury was not in session. The Court of Appeals reversed. <span class="citation" data-id="320663"><a href="/opinion/320663/united-states-v-mitchell-miller-susan-mcduffie-weeks-and-john-henry/" aria-description="Citation for case: United States v. Mitchell Miller, Susan McDuffie Weeks,...">500 F. 2d 751</a></span> (1974). Citing the prohibition in <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#622" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 622</a></span> (1886), against “compulsory production of a man’s private papers to establish a criminal charge against him,” the court held that the Government had improperly circumvented <em>Boyd’s </em>protections of respondent’s Fourth Amendment right against “unreasonable searches and seizures” by “first requiring a third party bank to copy all of its depositors’ personal checks and then, with an improper invocation of legal process, calling upon the bank to allow inspection and reproduction of those copies.” <span class="citation" data-id="320663"><a href="/opinion/320663/united-states-v-mitchell-miller-susan-mcduffie-weeks-and-john-henry/#757" aria-description="Citation for case: United States v. Mitchell Miller, Susan McDuffie Weeks,...">500 F. 2d, at 757</a></span>. The court acknowledged that the recordkeeping requirements of the Bank Secrecy Act had been held to be constitutional on their face in <em>California Bankers Assn. </em>v. <em>Shultz, </em><span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S. 21</a></span> (1974), but noted that access to the records was to be controlled by “existing legal process.” See <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#52" aria-description="Citation for case: California Bankers Assn. v. Shultz"><em>id., </em>at 52</a></span>. The subpoenas issued here were found not to constitute adequate “legal process.” The fact that the bank officers cooperated voluntarily was found to be irrelevant, for “he whose rights are threatened by the improper disclosure here was a bank depositor, not a bank official.” <span class="citation" data-id="320663"><a href="/opinion/320663/united-states-v-mitchell-miller-susan-mcduffie-weeks-and-john-henry/#758" aria-description="Citation for case: United States v. Mitchell Miller, Susan McDuffie Weeks,...">500 F. 2d, at 758</a></span>.</p>
<p id="b509-5">The Government contends that the Court of Appeals erred in three respects: (i) in finding that respondent had the Fourth Amendment interest necessary to entitle him to challenge the validity of the subpoenas <em>duces tecum </em>through his motion to suppress; (ii) in holding that the subpoenas were defective; and (iii) in determining that suppression of the evidence obtained was the appropriate remedy if a constitutional violation did take place.</p>
<p id="b510-4"><page-number citation-index="1" label="440">*440</page-number>We find that there was no intrusion into any area in which respondent had a protected Fourth Amendment interest and that the District Court therefore correctly denied respondent’s motion to suppress. Because we reverse the decision of the Court of Appeals on that ground alone, we do not reach the Government’s latter two contentions.</p>
<p id="b510-5">II</p>
<p id="b510-6">In <em>Hoffa </em>v. <em>United States, </em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#301" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 301-302</a></span> (1966), the Court said that “no interest legitimately protected by the Fourth Amendment” is implicated by governmental investigative activities unless there is an intrusion into a zone of privacy, into “the security a man relies upon when he places himself or his property within a constitutionally protected area.” The Court of Appeals, as noted above, assumed that respondent had the necessary Fourth Amendment interest, pointing to the language in <em>Boyd </em>v. <em>United States, supra, at </em>622, which describes that Amendment’s protection against the “compulsory production of a man’s private papers.”<footnotemark>1</footnotemark> We think that the Court of Appeals erred in finding the subpoenaed documents to fall within a protected zone of privacy.</p>
<p id="b510-7">On their face, the documents subpoenaed here are not respondent’s “private papers.” Unlike the claimant in <em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>, </em>respondent can assert neither ownership nor possession. Instead, these are the business records of the banks. As we said in <em>California Bankers Assn. </em>v. <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#48" aria-description="Citation for case: California Bankers Assn. v. Shultz"><em>Shultz, supra, </em>at 48-49</a></span>, “[blanks are . . . not . . . neutrals in transactions involving negotiable instruments, but parties to the instruments with a substantial stake in their continued availability and acceptance.” The records of re<page-number citation-index="1" label="441">*441</page-number>spondent’s accounts, like “all of the records [which are required to be kept pursuant to the Bank Secrecy Act,] pertain to transactions to which the bank was itself a party.” <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#52" aria-description="Citation for case: California Bankers Assn. v. Shultz"><em>Id., </em>at 52</a></span>.</p>
<p id="b511-4">Respondent argues, however, that the Bank Secrecy Act introduces a factor that makes the subpoena in this case the functional equivalent of a search and seizure of the depositor’s “private papers.” We have held, in <em>California Bankers Assn. </em>v. <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#54" aria-description="Citation for case: California Bankers Assn. v. Shultz"><em>Shultz, supra, </em>at 54</a></span>, that the mere maintenance of records pursuant to the requirements of the Act “invade [s] no Fourth Amendment right of any depositor.” But respondent contends that the combination of the recordkeeping requirements of the Act and the issuance of a subpoena<footnotemark>2</footnotemark> to obtain those records permits the Government to circumvent the requirements of the Fourth Amendment by allowing it to obtain a depositor’s private records without complying with the legal requirements that would be applicable had it proceeded against him directly.<footnotemark>3</footnotemark> Therefore, we must address the question whether the compulsion embodied in the Bank Secrecy Act as exercised in this case creates a Fourth Amendment interest in the depositor where none existed before. This question was expressly re<page-number citation-index="1" label="442">*442</page-number>served in <em>California Bankers Assn., supra, </em>at 53-54, and n. 24.</p>
<p id="b512-5">Respondent urges that he has a Fourth Amendment interest in the records kept by the banks because they are merely copies of personal records that were made available to the banks for a limited purpose and in which he has a reasonable expectation of privacy. He relies on this Court’s statement in <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 353</a></span> (1967), quoting <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#304" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 304</a></span> (1967), that “we have . . . departed from the narrow view” that “ 'property interests control the right of the Government to search and seize,’ ” and that a “search and seizure” become unreasonable when the Government’s activities violate “the privacy upon which [a person] justifiably reliefs].” But in <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>the Court also stressed that “[w]hat a person knowingly exposes to the public ... is not a subject of Fourth Amendment protection.” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S., at 351</a></span>. We must examine the nature of the particular documents sought to be protected in order to determine whether there is a legitimate “expectation of privacy” concerning their contents. Cf. <em>Couch </em>v. <em>United States, </em><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#335" aria-description="Citation for case: Couch v. United States">409 U. S. 322, 335</a></span> (1973).</p>
<p id="b512-6">Even if we direct our attention to the original checks and deposit slips, rather than to the microfilm copies actually viewed and obtained by means of the subpoena, we perceive no legitimate “expectation of privacy” in their contents. The checks are not confidential communications but negotiable instruments to be used in commercial transactions. All of the documents obtained, including financial statements and deposit slips, contain only information voluntarily conveyed to the banks and exposed to their employees in the ordinary course of business. The lack of any legitimate expectation of privacy concerning the information kept in bank records was assumed by Congress in enacting the Bank Secrecy Act, the expressed purpose of which is to require records <page-number citation-index="1" label="443">*443</page-number>to be maintained because they “have a high degree of usefulness in criminal, tax, and regulatory investigations and proceedings.” 12 U. S. C. § 1829b (a) (1). Cf. <em>Couch </em>v. <em>United States, supra, </em>at 335.</p>
<p id="b513-5">The depositor takes the risk, in revealing his affairs to another, that the information will be conveyed by that person to the Government. <em>United States </em>v. <em>White, </em><span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#751" aria-description="Citation for case: United States v. White">401 U. S. 745, 751-752</a></span> (1971). This Court has held repeatedly that the Fourth Amendment does not prohibit the obtaining of information revealed to a third party and conveyed by him to Government authorities, even if the information is revealed on the assumption that it will be used only for a limited purpose and the confidence placed in the third party will not be betrayed. <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#752" aria-description="Citation for case: United States v. White"><em>Id., </em>at 752</a></span>; <em>Hoffa </em>v. <em>United States, </em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#302" aria-description="Citation for case: Hoffa v. United States">385 U. S., at 302</a></span>; <em>Lopez </em>v. <em>United States, </em><span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">373 U. S. 427</a></span> (1963).<footnotemark>4</footnotemark></p>
<p id="b513-6">This analysis is not changed by the mandate of the Bank Secrecy Act that records of depositors' transactions be maintained by banks. In <em>California Bankers Assn. </em>v. <em>Shultz, </em><span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#52" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S., at 52-53</a></span>, we rejected the contention that banks, when keeping records of their depositors' transactions pursuant to the Act, are acting solely as agents of the Government. But, even if the banks could be said to have been acting solely as Government agents in transcribing the necessary information and complying without protest<footnotemark>5</footnotemark> with the requirements of the subpoenas, there would be no intrusion upon the depositors' Fourth Amendment rights. See <em>Osborn </em>v. <em>United States, </em><span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/" aria-description="Citation for case: Osborn v. United States">385 U. S. 323</a></span> (1966); <em>Lewis </em>v. <em>United States, </em><span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/" aria-description="Citation for case: Lewis v. United States">385 U. S. 206</a></span> (1966).</p>
<p id="b514-4"><page-number citation-index="1" label="444">*444</page-number>Ill</p>
<p id="b514-5">Since no Fourth Amendment interests of the depositor are implicated here, this case is governed by the general rule that the issuance of a subpoena to a third party to obtain the records of that party does not violate the rights of a defendant, even if a criminal prosecution is contemplated at the time the subpoena is issued. <em>California Bankers Assn. </em>v. <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#53" aria-description="Citation for case: California Bankers Assn. v. Shultz"><em>Shultz, supra, </em>at 53</a></span>; <em>Donaldson </em>v. <em>United States, </em><span class="citation" data-id="9424399"><a href="/opinion/108236/donaldson-v-united-states/#537" aria-description="Citation for case: Donaldson v. United States">400 U. S. 517, 537</a></span> (1971) (Douglas, J., concurring). Under these principles, it was firmly settled, before the passage of the Bank Secrecy Act, that an Internal Revenue Service summons directed to a third-party bank does not violate the Fourth Amendment rights of a depositor under investigation. See <em>First National Bank of Mobile </em>v. <em>United States, </em><span class="citation multiple-matches"><a href="/c/U.%20S./267/576/">267 U. S. 576</a></span> (1925), aff’g <span class="citation" data-id="8833975"><a href="/opinion/8848641/united-states-v-first-nat-bank/" aria-description="Citation for case: United States v. First Nat. Bank">295 F. 142</a></span> (SD Ala. 1924). See also <em>California Bankers Assn. </em>v. <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#53" aria-description="Citation for case: California Bankers Assn. v. Shultz"><em>Shultz, supra, </em>at 53</a></span>; <em>Donaldson </em>v. <em>United States, supra, </em>at 522.</p>
<p id="b514-6">Many banks traditionally kept permanent records of their depositors’ accounts, although not all banks did so and the practice was declining in recent years. By requiring that such records be kept by all banks, the Bank Secrecy Act is not a novel means designed to circumvent established Fourth Amendment rights. It is merely an attempt to facilitate the use of a proper and longstanding law enforcement technique by insuring that records are available when they are needed.<footnotemark>6</footnotemark></p>
<p id="b515-4"><page-number citation-index="1" label="445">*445</page-number>We hold that the District Court correctly denied respondent’s motion to suppress, since he possessed no Fourth Amendment interest that could be vindicated by a challenge to the subpoenas.</p>
<p id="b515-5">IV</p>
<p id="b515-6">Respondent contends not only that the subpoenas <em>duces tecum </em>directed against the banks infringed his Fourth Amendment rights, but that a subpoena issued to a bank to obtain records maintained pursuant to the Act is subject to more stringent Fourth Amendment requirements than is the ordinary subpoena. In making this assertion he relies on our statement in <em>California Bankers Assn., supra, </em>at 52, that access to the records maintained by banks under the Act is to be controlled by "existing legal process.” <footnotemark>7</footnotemark></p>
<p id="b515-7">In <em>Oklahoma Press Pub. Co. </em>v. <em>Walling, </em><span class="citation" data-id="9419755"><a href="/opinion/104239/oklahoma-press-publishing-co-v-walling/#208" aria-description="Citation for case: Oklahoma Press Publishing Co. v. Walling">327 U. S. 186, 208</a></span> (1946), the Court said that “the Fourth [Amendment], if applicable [to subpoenas for the production of business records and papers], at the most guards against abuse only by way of too much indefiniteness or breadth in the things required to be 'particularly described,’ if also the inquiry is one the demanding <page-number citation-index="1" label="446">*446</page-number>agency is authorized by law to make and the materials specified are relevant.” See also <em>United States </em>v. <em>Dionisio, </em><span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#11" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1, 11-12</a></span> (1973). Respondent, citing <em>United States </em>v. <em>United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297</a></span> (1972), in which we discussed the application of the warrant requirements of the Fourth Amendment to domestic security surveillance through electronic eavesdropping, suggests that greater judicial scrutiny, equivalent to that required for a search warrant, is necessary when a subpoena is to be used to obtain bank records of a depositor’s account. But in <em>California Bankers Assn., </em><span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#52" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S., at 52</a></span>, we emphasized only that access to the records was to be in accordance with “existing legal process.” There was no indication that a new rule was to be devised, or that the traditional distinction between a search warrant and a subpoena would not be recognized.<footnotemark>8</footnotemark></p>
<p id="b516-5">In any event, for the reasons stated above, we hold that respondent lacks the requisite Fourth Amendment interest to challenge the validity of the subpoenas.<footnotemark>9</footnotemark></p>
<p id="b516-6">V</p>
<p id="b516-7">The judgment of the Court of Appeals is reversed. The court deferred decision on whether the trial court had improperly overruled respondent’s motion to suppress <page-number citation-index="1" label="447">*447</page-number>distillery apparatus and raw material seized from a rented truck. We remand for disposition of that issue.</p>
<p id="b517-5">
<em>So ordered.</em>
</p>
<footnote label="1">
<p id="b510-8"> The Fourth Amendment implications of <em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span> </em>as it applies to subpoenas <em>duces tecum </em>have been undercut by more recent cases. <em>Fisher </em>v. <em>United States, ante, at </em>407-409. <em>See infra, </em>at 445-446.</p>
</footnote>
<footnote label="2">
<p id="b511-5"> Respondent appears to contend that a depositor’s Fourth Amendment interest comes into play only when a <em>defective </em>subpoena is used to obtain records kept pursuant to the Act. We see no reason why the existence of a Fourth Amendment interest turns on whether the subpoena is defective. Therefore, we do not limit our consideration to the situation in which there is an alleged defect in the subpoena served on the bank.</p>
</footnote>
<footnote label="3">
<p id="b511-6"> It is not clear whether respondent refers to attempts to obtain private documents through a subpoena issued directly to the depositor or through a search pursuant to a warrant. The question whether personal business records may be seized pursuant to a valid warrant is before this Court in No. 74-1646, <em>Andresen </em>v. <em>Maryland, </em>cert. granted, <span class="citation multiple-matches"><a href="/c/U.%20S./423/822/">423 U. S. 822</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b513-7"> We do not address here the question of evidentiary privileges, such as that protecting communications between an attorney and his client. Cf. <em>Fisher </em>v. <em>United States, ante, </em>at 403-405.</p>
</footnote>
<footnote label="5">
<p id="b513-8"> Nor did the banks notify respondent, a neglect without legal consequences here, however unattractive it may be.</p>
</footnote>
<footnote label="6">
<p id="b514-7"> Respondent does not contend that the subpoenas infringed upon his First Amendment rights. There was no blanket reporting requirement of the sort we addressed in <em>Buckley </em>v. <em>Valeo, </em><span class="citation" data-id="109380"><a href="/opinion/109380/buckley-v-valeo/#60" aria-description="Citation for case: Buckley v. Valeo">424 U. S. 1, 60-84</a></span> (1976), nor any allegation of an improper inquiry into protected associational activities of the sort presented in <em>Eastland </em>v. <em>United States Servicemen’s Fund, </em><span class="citation" data-id="9426086"><a href="/opinion/109257/eastland-v-united-states-servicemens-fund/" aria-description="Citation for case: Eastland v. United States Servicemen&#x27;s Fund">421 U. S. 491</a></span> (1975).</p>
<p id="APj">We are not confronted with a situation in which the Government, through “unreviewed executive discretion,” has made a wide-ranging <page-number citation-index="1" label="445">*445</page-number>inquiry that unnecessarily "touch[es] upon intimate areas of an individual’s personal affairs.” <em>California Bankers </em>Assn. v. <em>Shultz, </em><span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#78" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S., at 78-79</a></span> (Powell, J., concurring). Here the Government has exercised its powers through narrowly directed subpoenas <em>duces tecum </em>subject to the legal restraints attendant to such process. See Part IV, <em>infra.</em></p>
</footnote>
<footnote label="7">
<p id="b515-14"> This case differs from <em>Burrows </em>v. <em>Superior Court, 13 </em>Cal. 3d 238, <span class="citation" data-id="1172381"><a href="/opinion/1172381/burrows-v-superior-court/" aria-description="Citation for case: Burrows v. Superior Court">529 P. 2d 590</a></span> (1974), relied on by Mr. Justice Brennan in dissent, in that the bank records of respondent’s accounts were furnished in response to “compulsion by legal process” in the form of subpoenas <em>duces tecum. </em>The court in <em><span class="citation" data-id="1172381"><a href="/opinion/1172381/burrows-v-superior-court/" aria-description="Citation for case: Burrows v. Superior Court">Burrows</a></span> </em>found it “significant . . . that the bank [in that case) provided the statements to the police in response to an informal oral request for information.” <span class="citation" data-id="1172381"><a href="/opinion/1172381/burrows-v-superior-court/#243" aria-description="Citation for case: Burrows v. Superior Court"><em>Id., </em>at 243</a></span>, <span class="citation" data-id="1172381"><a href="/opinion/1172381/burrows-v-superior-court/#593" aria-description="Citation for case: Burrows v. Superior Court">529 P. 2d, at 593</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b516-8"> A subpoena <em>duces tecum </em>issued to obtain records is subject to nó more stringent Fourth Amendment requirements than is the ordinary subpoena. A search warrant, in contrast, is issuable only pursuant to prior judicial approval and authorizes Government officers to seize evidence without requiring enforcement through the courts. See <em>United States </em>v. <em>Dionisio, </em><span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#9" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1, 9-10</a></span> (1973).</p>
</footnote>
<footnote label="9">
<p id="b516-9"> There is no occasion for us to address whether the subpoenas complied with the requirements outlined in <em>Oklahoma Press Pub. Co. </em>v. <em>Walling, </em><span class="citation" data-id="9419755"><a href="/opinion/104239/oklahoma-press-publishing-co-v-walling/" aria-description="Citation for case: Oklahoma Press Publishing Co. v. Walling">327 U. S. 186</a></span> (1946). The banks upon which they were served did not contest their validity.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Nora.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Nora
type: case
citation: "765 F.3d 1049 (2014)"
parallel_cite: ""
neutral_cite: "2014 U.S. App. LEXIS 16677; 2014 WL 4235955"
court: 9th Cir.
court_level: coa
circuit: ca9
year: 2014
date_decided: 2014-08-28
docket: 12-50485
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
  opinion_url: "https://www.courtlistener.com/opinion/2722177/united-states-v-johnny-casel-nora/"
  cluster_id: 2722177
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Nora
  status: under_review
  projected_at: 2026-07-08
homes:
  - page: "[[Entry to Arrest]]"
    role: "Key — Anchor (SACO spine: perimeter-defeats-flight-exigency, 765 F.3d at 1055; containment-vs-exit-command line)"
  - page: "[[Arrest in the Home]]"
    role: "Related — cross-doctrine (constructive-entry consequence of Payton)"
---

# United States v. Nora

*765 F.3d 1049 (9th Cir. 2014)* (No. 12-50485) · U.S. Court of Appeals, 9th Cir. · **Binding in-circuit — 9th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the treatment framing below is authored orientation, not machine-certified. Identity cluster 2722177 → 765 F.3d 1049, No. 12-50485, decided 2014-08-28 (Watford, J.). Rule/Application quotes string-matched to the CL opinion text 2026-07-08. -->

## Background
On a night in January 2008, two uniformed officers patrolling South Central Los Angeles saw Johnny Nora and two other men on the street; when Nora saw the officers he fled into his house. Officers detained a companion in the front yard while another ran to cover the back door, and then called for backup: "some 20 to 30 officers arrived and surrounded the house with weapons drawn," aided by a police helicopter. After a 20-to-30-minute standoff, "the officers used a public address system to order the occupants of the house to come out," and Nora complied and was arrested in front of the house. Officers then obtained a warrant and searched the home, seizing narcotics and firearms that formed the basis of the federal charges. Nora moved to suppress; the district court denied the motion, and he entered a conditional guilty plea.

## Issue
Whether officers who surround a suspect's home with an overwhelming show of force and summon him out over a public-address system effect a warrantless arrest "in violation of *Payton v. New York*," and whether any [[Exigent Circumstances and Hot Pursuit|exigency]] excused the failure to obtain an arrest warrant.

## Rule
*[[Payton v. New York|Payton]]* supplies the baseline: "The Court held in *Payton* that the Fourth Amendment forbids arresting a suspect inside his home unless the police first obtain an arrest warrant or an exception to the warrant requirement applies." 765 F.3d at 1054 (citing *Payton v. New York*, 445 U.S. 573, 590 (1980)). ^pin-1054

A suspect summoned out of a surrounded home is treated as arrested inside it unless he voluntarily exposed himself; the government must then justify the warrantless in-home arrest by an exception such as [[Exigent Circumstances and Hot Pursuit|exigent circumstances]]. <!-- pin-1054 star-page CONFIRMED at orchestrator finalization 2026-07-08: quote at doc position 15602, between star markers *1054 (pos 14213) and *1055 (pos 22131) — MCP search_document, opinion 2722177. -->

The perimeter itself defeats the flight-and-danger [[Exigent Circumstances and Hot Pursuit|exigency]] the government invoked. The court found no basis to believe anyone else was endangered, and "[n]or had Nora given any other indication that he was in 'an agitated and violent state,'" *[[United States v. Al-Azzawy]]*, 784 F.2d 890, 894 (9th Cir. 1986); "[f]inally, the officers had no reason to believe Nora might pose a danger to the public by attempting to flee, since they had the house completely surrounded and could monitor all exit points." — 765 F.3d at 1055. ^pin-1055

## Application
Because the officers had probable cause but no warrant, and because a complete perimeter with monitored exits eliminated any risk of flight or escape, no [[Exigent Circumstances and Hot Pursuit|exigency]] excused the warrant requirement. The surround-and-summon tactic was therefore a warrantless arrest that *[[Payton v. New York|Payton]]* forbids: the officers "could monitor all exit points," so the very containment the government offered as justification is what negated the claimed [[Exigent Circumstances and Hot Pursuit|exigency]]. 765 F.3d at 1055. ^pin-1055b

The evidence derived from the ensuing search was fruit of the unlawful arrest and should have been suppressed.

## Conclusion
The Ninth Circuit reversed the denial of suppression and [[Reading and Citing Cases#on-remand|remanded]]. Officers who surround a home and order a suspect out cannot rely on flight-based [[Exigent Circumstances and Hot Pursuit|exigency]] to avoid the warrant requirement when the perimeter already forecloses escape.

## Treatment & subsequent history
- **Status:** ⚪ unverified (frontier stub) — **Binding in-circuit — 9th Cir.** Treatment/progeny not machine-certified until S9 promotion.
- *Nora* is the modern Ninth-Circuit spine of the surround-and-call-out (SACO) line: it applies the containment-vs-exit-command rule of *[[United States v. Al-Azzawy]]* (coerced emergence from a surrounded home is an in-home arrest) and marks the outer boundary of the flight-[[Exigent Circumstances and Hot Pursuit|exigency]] exception (perimeter defeats flight). It contrasts with the voluntary-exposure holding of *[[United States v. Vaneaton]]*, 49 F.3d 1423 (9th Cir. 1995), and with the armed-standoff [[Exigent Circumstances and Hot Pursuit|exigency]] of *Fisher v. City of San Jose*, 558 F.3d 1069 (9th Cir. 2009) (en banc).

*Status note (⚪):* authored from a CourtListener-verified identity stub (two-key: cluster 2722177 + 765 F.3d 1049); renders under the ⚪ banner until S9 promotion.

## Appears on
- [[Entry to Arrest]] — *Key*
- [[Arrest in the Home]] — *Key*

## Sources
- [*United States v. Nora*, 765 F.3d 1049 (9th Cir. 2014)](https://www.courtlistener.com/opinion/2722177/united-states-v-nora/) — pinpoints: 1054 (*Payton* rule), 1055 (perimeter defeats flight/danger exigency; distinguishing *Al-Azzawy* at 894); quotes string-matched to the CL opinion text 2026-07-08.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "653da5170e94347a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "765 F.3d 1049 (2014)", "court": "9th Cir.", "neutral_cite": "2014 U.S. App. LEXIS 16677; 2014 WL 4235955", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Nora", "year": "2014"}}
{"assertion_id": "68ac86e203b304bf", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Related — cross-doctrine (constructive-entry consequence of Payton)", "title": "United States v. Nora"}}
{"assertion_id": "ffc898b7c606cfaa", "dimension": "support", "kind": "home_role", "locator": {"home": "Entry to Arrest"}, "payload": {"home": "Entry to Arrest", "role": "Key — Anchor (SACO spine: perimeter-defeats-flight-exigency, 765 F.3d at 1055; containment-vs-exit-command line)", "title": "United States v. Nora"}}
{"assertion_id": "b2f6cbdb48ce02c7", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 9th Cir.", "title": "United States v. Nora"}}
{"assertion_id": "d4431c05e4a1eb61", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Nora", "varies_by_point": "false"}}
```

### lake record — United States v. Nora

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Nora",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Johnny Casel Nora",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Johnny Casel NORA, AKA John Carter, AKA John Nora, AKA Johnny Nora, AKA Johnny Carl Nora, Defendant-Appellant",
    "input_case_name": "United States v. Nora",
    "court": "9th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": "2014-08-28",
    "year": 2014,
    "docket": "12-50485",
    "cluster_id": 2722177,
    "lead_opinion_id": 2722177,
    "sibling_ids": [],
    "absolute_url": "/opinion/2722177/united-states-v-johnny-casel-nora/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "765 F.3d 1049",
      "volume": "765",
      "reporter": "F.3d",
      "page": "1049",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2014 U.S. App. LEXIS 16677",
        "volume": "2014",
        "reporter": "U.S. App. LEXIS",
        "page": "16677",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 4235955",
        "volume": "2014",
        "reporter": "WL",
        "page": "4235955",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "765 F.3d 1049",
        "volume": "765",
        "reporter": "F.3d",
        "page": "1049",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 U.S. App. LEXIS 16677",
        "volume": "2014",
        "reporter": "U.S. App. LEXIS",
        "page": "16677",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 4235955",
        "volume": "2014",
        "reporter": "WL",
        "page": "4235955",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "765 F.3d 1049",
    "official_selection": {
      "court_class": "coa",
      "selected": "765 F.3d 1049",
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
    "date_created": "2026-07-08T16:52:09Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-08T16:52:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T16:52:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T16:52:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-08T16:52:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-nora--2722177",
      "to_record_id": "United States v. Nora",
      "as_of": "2026-07-08T22:30:00Z",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Nora

```
                FOR PUBLICATION

  UNITED STATES COURT OF APPEALS
       FOR THE NINTH CIRCUIT


UNITED STATES OF AMERICA,                No. 12-50485
                Plaintiff-Appellee,
                                            D.C. No.
                 v.                      2:09-cr-00092-
                                            SVW-1
JOHNNY CASEL NORA, AKA John
Carter, AKA John Nora, AKA
Johnny Nora, AKA Johnny Carl               OPINION
Nora,
              Defendant-Appellant.


      Appeal from the United States District Court
          for the Central District of California
      Stephen V. Wilson, District Judge, Presiding

                Argued and Submitted
        January 8, 2014—Pasadena, California

                 Filed August 28, 2014

   Before: William A. Fletcher, Milan D. Smith, Jr.,
         and Paul J. Watford, Circuit Judges.

              Opinion by Judge Watford
2                   UNITED STATES V. NORA

                           SUMMARY*


                          Criminal Law

    The panel reversed the district court’s denial of a motion
to suppress evidence seized from the defendant’s home, and
remanded for further proceedings, in a case in which the
defendant entered a conditional guilty plea to possession of
cocaine base with intent to distribute.

    The panel held that although the defendant’s arrest was
supported by probable cause, the arrest violated Payton v.
New York, 445 U.S. 573 (1980), and violated the Fourth
Amendment, where the officers physically took the defendant
into custody outside his home in the front yard only by
surrounding his house and ordering him to come out at
gunpoint, and no exigency existed.

    The panel held that evidence seized during a pat-down
search incident to an arrest made in violation of Payton must
be suppressed, whether the search occurs inside the home or,
as in the case of the cash and marijuana here, outside the
home. The panel held that the defendant’s post-arrest
statements are subject to suppression as well, as fruit of the
unlawful search of his person. The panel held that
suppression of this evidence renders the portions of the
warrant authorizing a search for narcotics-related evidence
and evidence of gang membership invalid. The panel held
that the remaining untainted evidence did not establish
probable cause to search the defendant’s home for the broad

  *
    This summary constitutes no part of the opinion of the court. It has
been prepared by court staff for the convenience of the reader.
                 UNITED STATES V. NORA                     3

range of firearms described in the warrant, and that as a
consequence, the entire warrant was invalid and all evidence
seized pursuant to it must be suppressed.


                        COUNSEL

Michael J. Treman (argued), Santa Barbara, California, for
Defendant-Appellant.

André Birotte Jr., United States Attorney, Robert E. Dugdale,
Chief, Criminal Division, Cheryl L. O’Connor (argued) and
Max B. Shiner, Assistant United States Attorneys, Los
Angeles, California, for Plaintiff-Appellee.


                        OPINION

WATFORD, Circuit Judge:

    The issue raised by this appeal is whether the police
violated Johnny Nora’s Fourth Amendment rights when they
searched his home. The search yielded narcotics and
firearms, which formed the basis for the federal charges
brought against him. After the district court denied Nora’s
motion to suppress the evidence seized from his home, Nora
entered a conditional guilty plea pending the outcome of this
appeal.

    Nora contends that, although the officers obtained a
search warrant, all of the evidence discovered during the
search must be suppressed because the warrant was invalid.
The warrant was invalid, Nora argues, because it was based
on information acquired as a result of his unlawful arrest.
4                 UNITED STATES V. NORA

And his arrest was unlawful, Nora urges, because the officers
either lacked probable cause to arrest him or, alternatively,
arrested him in violation of Payton v. New York, 445 U.S. 573
(1980).

                               I

    The events relevant here occurred on a single night in
January 2008. Two uniformed police officers were patrolling
Nora’s neighborhood in South Central Los Angeles in an
unmarked car. As they drove down Nora’s street, the officers
saw three men they didn’t know standing on the sidewalk in
front of Nora’s two-bedroom house, about 75 yards away.
The officers lost sight of the men for a few seconds. By the
time the officers pulled up in front of the house and got out of
the car, two of the three men (Nora and Andre Davis) were
standing on the porch, while the third (Patrick Hodges) stood
in the front yard, which was enclosed by a metal fence. See
Appendix (photograph of front yard and porch). The officers
stood on the sidewalk and attempted to engage in casual
conversation with the men.

    According to the officers, whose testimony the district
court credited over Nora’s conflicting testimony, Nora
appeared nervous and stood stiffly with his right side
obscured from the officers’ view. Seconds into the
conversation, Nora abruptly spun toward the front door and
pushed past Davis to get into the house. As he did so, the
officers could see that Nora was holding a blue-steel semi-
automatic handgun in his right hand. One of the officers
shouted “Stop! Police!” but Nora and Davis ignored the
command, rushed into the house, and shut the door behind
them.
                  UNITED STATES V. NORA                     5

    After Nora and Davis fled into the house, one of the
officers detained Hodges, who was still standing in the front
yard, while the other officer ran around the side of the house
to watch the back door. Someone inside the house turned off
the only light that had been on, leaving the house completely
dark. The officers then called for backup. Within minutes,
some 20 to 30 officers arrived and surrounded the house with
weapons drawn. They were aided by a police helicopter
hovering above whose lights, Nora’s wife testified, lit up the
house “like the daytime.”

    A standoff ensued for the next 20 to 30 minutes, which
ended when the officers used a public address system to order
the occupants of the house to come out. Nora and Davis
complied, followed a few minutes later by Nora’s wife and
children.

    Officers immediately handcuffed Nora and searched him.
They found a small amount of marijuana and more than
$1,000 in cash on his person. One of the officers read Nora
the warnings required by Miranda v. Arizona, 384 U.S. 436
(1966), and then briefly questioned him. Nora made several
incriminating statements in response to those questions.
Specifically, Nora admitted that he had personal use
quantities of methamphetamine and heroin in a dresser
drawer, that he lived at the house, and that he belonged to a
particular street gang. After determining Nora’s identity, the
officers ran a criminal background check, which revealed that
Nora had a prior conviction for carrying a loaded firearm and
two prior convictions for being a felon in possession of a
firearm.

   The officers sought and obtained a warrant to search
Nora’s home for the following items: marijuana,
6                 UNITED STATES V. NORA

methamphetamine, heroin, and related paraphernalia;
evidence relating to the sale of narcotics; firearms,
magazines, and ammunition; and evidence of gang
membership. The affidavit supporting the warrant relied on
the officers’ observations of Nora outside his home, as well
as the evidence obtained as a result of Nora’s arrest—namely,
the marijuana and cash found on his person, his post-arrest
statements, and the record of his prior convictions. Among
other things, the search of Nora’s home resulted in seizure of
the following:

    •   From an ironing-board closet hidden behind the
        refrigerator: quantities of cocaine, cocaine base,
        marijuana, over $9,000 in cash, and four semi-
        automatic handguns.

    •   From a bedroom dresser drawer: quantities of heroin
        and methamphetamine.

    •   From the detached garage: quantities of cocaine base,
        one handgun, one rifle, two shotguns, two electronic
        scales, handgun magazines, and ammunition.

    A federal grand jury charged Nora with possession with
intent to distribute controlled substances, possession of
firearms in furtherance of a drug trafficking offense,
possession of an unregistered firearm, and one count of being
a felon in possession of a firearm. Nora entered a conditional
guilty plea to possession of cocaine base with intent to
distribute, reserving his right to appeal the district court’s
denial of his suppression motion. The court ultimately
sentenced Nora to 122 months in prison.
                      UNITED STATES V. NORA                               7

                                     II

    Nora first contends that the officers lacked probable cause
to arrest him. The government counters that the officers had
probable cause to arrest Nora for violating California Penal
Code § 25850(a) (formerly § 12031(a)). That statute, as
relevant here, makes it a misdemeanor to carry a loaded
firearm “while in any public place or on any public street.”
§ 25850(a).1

    The officers’ firsthand observations of Nora on the porch
undoubtedly gave them probable cause to believe he was
carrying a firearm. But for purposes of § 25850(a), Nora’s
front porch is not a “public place.” See People v. Strider,
100 Cal. Rptr. 3d 66, 74 (Ct. App. 2009). The question, then,
is whether the officers had probable cause to believe both that
Nora had been carrying the firearm while standing on the
sidewalk (which is a public place), and that the firearm was
loaded.

    The officers’ observations gave rise to a “fair probability”
that Nora had been carrying the handgun while standing on
the sidewalk. Illinois v. Gates, 462 U.S. 213, 238 (1983).
That’s where the officers first saw him, and they lost sight of
him for only a few seconds before they next saw him standing
on the porch with the gun in his hand. They did not see him
pick up anything or accept anything from Davis or Hodges
while on the porch. Given the short interval during which the


  1
     “A person is guilty of carrying a loaded firearm when the person
carries a loaded firearm on the person or in a vehicle while in any public
place or on any public street in an incorporated city or in any public place
or on any public street in a prohibited area of unincorporated territory.”
Cal. Penal Code § 25850(a).
8                 UNITED STATES V. NORA

officers lost sight of Nora, they had reasonable grounds to
believe that the firearm they saw him holding on the porch
had been in his hand just moments earlier on the sidewalk as
well. See Maryland v. Pringle, 540 U.S. 366, 371 (2003).

    The facts known to the officers also established a fair
probability that the firearm was loaded. The particular
firearm involved here—a semi-automatic handgun—is
principally used for self-defense and protection of the home,
see District of Columbia v. Heller, 554 U.S. 570, 628 (2008),
purposes served most effectively if the weapon is loaded.
The officers saw Nora carrying the handgun at night outside
a home in which he later sought refuge, suggesting he was in
fact carrying the handgun for those purposes. As the district
court noted, the fact that Nora carried the handgun in his hand
“at the ready” strengthened the inference it was loaded; it
wasn’t stored in a gun case or left unattended in a vehicle,
circumstances in which a firearm might more plausibly be
unloaded. And Nora’s unprovoked flight into the house upon
seeing the officers added further weight to the inference that
criminal wrongdoing might be afoot. See Illinois v. Wardlow,
528 U.S. 119, 124–25 (2000); Sibron v. New York, 392 U.S.
40, 66–67 (1968). These facts, taken together, provided a
reasonable basis for believing Nora had violated § 25850(a).

   Nora argues that it’s possible he picked up the handgun
between the time he was standing on the sidewalk and the
time he reached the porch, and that the gun could have been
unloaded. But the concept of probable cause requires us to
deal in probabilities, not certainties, and for that reason it
doesn’t demand “the same type of specific evidence of each
element of the offense as would be needed to support a
conviction.” Adams v. Williams, 407 U.S. 143, 149 (1972).
Taking into account the totality of the circumstances, the
                  UNITED STATES V. NORA                        9

officers needed to have only a “reasonable ground” for
believing Nora had violated § 25850(a). Pringle, 540 U.S. at
371. Here, they did.

                               III

    Nora next contends that, even if the officers had probable
cause to arrest him, they arrested him in violation of Payton
v. New York, 445 U.S. 573 (1980). The Court held in Payton
that the Fourth Amendment forbids arresting a suspect inside
his home unless the police first obtain an arrest warrant or an
exception to the warrant requirement applies. Id. at 590.
That rule is designed to protect “the privacy and the sanctity
of the home,” id. at 588, and stems from “the overriding
respect for the sanctity of the home that has been embedded
in our traditions since the origins of the Republic.” Id. at 601.

    The government properly concedes that the police
arrested Nora “inside” his home for purposes of the Payton
rule. Although officers physically took Nora into custody
outside his home in the front yard, they accomplished that
feat only by surrounding his house and ordering him to come
out at gunpoint. We’ve held that forcing a suspect to exit his
home in those circumstances constitutes an in-home arrest
under Payton. See, e.g., Fisher v. City of San Jose, 558 F.3d
1069, 1074–75 (9th Cir. 2009) (en banc); United States v. Al-
Azzawy, 784 F.2d 890, 893 (9th Cir. 1985). Since the officers
didn’t obtain an arrest warrant, Nora’s arrest violated the
Fourth Amendment unless an exception to the warrant
requirement applies.

   The government argues, and the district court found, that
the “exigent circumstances” exception to the warrant
requirement applies. That exception permits a warrantless in-
10                UNITED STATES V. NORA

home arrest in certain narrowly defined circumstances. See
United States v. Struckman, 603 F.3d 731, 743 (9th Cir.
2010). One such circumstance is where the government can
show that the delay necessary to secure a warrant would
create “a substantial risk of harm to the persons involved or
to the law enforcement process.” Al-Azzawy, 784 F.2d at 894
(internal quotation marks omitted).

    Nora didn’t present the kind of immediate threat to the
safety of officers or others necessary to justify a disregard of
the warrant requirement. Our decision in Al-Azzawy provides
a useful contrast. In that case the defendant refused
commands to exit his home a short time after he threatened to
shoot his neighbor, to light his neighbor’s trailer on fire, and
to “blow up” the entire trailer park in which the two lived if
the neighbor bothered the defendant’s family again. Id.
at 891, 894. Officers were told that the defendant had also
threatened the neighbor with a pistol the day before and had
been seen in possession of hand grenades and automatic
weapons a few days earlier. Id. at 891. We held that exigent
circumstances justified the defendant’s warrantless in-home
arrest because the officers reasonably believed that he
“possessed illegal explosives and was in an agitated and
violent state.” Id. at 894. Even on those facts, we said the
exigency question was close. Id.

    The facts of this case are decidedly less compelling from
an exigency standpoint than those in Al-Azzawy. True, the
officers saw Nora in possession of a handgun. But Nora
never aimed the weapon at the officers or anyone else, and
the officers had no evidence that he had used or threatened to
use it. Cf. Fisher, 558 F.3d at 1072–73 (suspect aimed rifle
at officers and threatened to shoot). The officers had no
reason to believe that illegal weapons such as explosives were
                    UNITED STATES V. NORA                         11

present inside Nora’s home, or that anyone else to whom
Nora may have posed a danger was inside. Nor had Nora
given any other indication that he was in “an agitated and
violent state.” Al-Azzawy, 784 F.2d at 894. Finally, the
officers had no reason to believe Nora might pose a danger to
the public by attempting to flee, since they had the house
completely surrounded and could monitor all exit points. See
United States v. Gooch, 6 F.3d 673, 679 (9th Cir. 1993)
(defendant resting in closed tent posed no present danger to
officers or other campers, despite having discharged firearm
in crowded campground hours earlier).

    Our conclusion that no exigency existed is buttressed by
the fact that the offense involved here was a misdemeanor.
At the time the officers ordered Nora to exit his home, they
had probable cause to believe he had committed only a
misdemeanor violation of California Penal Code § 25850(a).2
The Supreme Court has said we should be hesitant to find
exigent circumstances “when the underlying offense for
which there is probable cause to arrest is relatively minor.”
Welsh v. Wisconsin, 466 U.S. 740, 750 (1984). Reflecting
that hesitancy, we’ve held that “an exigency related to a
misdemeanor will seldom, if ever, justify a warrantless entry
into the home.” Hopkins v. Bonvicino, 573 F.3d 752, 769
(9th Cir. 2009) (internal quotation marks omitted). In our
view, this isn’t one of the rare cases in which exigent
circumstances can be found notwithstanding the relatively
minor nature of the offense involved.




  2
    The officers were not yet aware of Nora’s criminal history, which
would have elevated the offense to a felony. See Cal. Penal Code
§ 25850(c)(1).
12                UNITED STATES V. NORA

                              IV

    Having concluded that the officers had probable cause to
arrest Nora but made the arrest in violation of Payton, we
must next decide whether the evidence obtained as a result of
Nora’s unlawful arrest should be suppressed. See Wong Sun
v. United States, 371 U.S. 471, 484–88 (1963). That evidence
falls into three categories: (1) the cash and marijuana found
on Nora during the pat-down search incident to his arrest;
(2) Nora’s post-arrest statements admitting gang membership
and the presence of personal use quantities of narcotics in the
house; and (3) information relating to Nora’s identity—in
particular, the record of his past convictions.

                              A

    As to the cash and marijuana found on Nora’s person, our
analysis is guided first and foremost by New York v. Harris,
495 U.S. 14 (1990), which established the scope of the
exclusionary rule’s application following a Payton violation.
In Harris, police had probable cause to arrest the defendant
but arrested him in his home without a warrant or exigent
circumstances. The defendant made incriminating statements
while still inside his home, and later signed a written
confession incriminating himself at the police station. The
Court noted that the statements made inside the home were
properly suppressed. Id. at 20. But the Court held that the
written statement made at the police station was not subject
to suppression, reasoning that “where the police have
probable cause to arrest a suspect, the exclusionary rule does
not bar the State’s use of a statement made by the defendant
outside of his home, even though the statement is taken after
an arrest made in the home in violation of Payton.” Id. at 21.
                  UNITED STATES V. NORA                      13

    The Court refused to suppress the statement made outside
the home because doing so would not have advanced the
deterrent purpose the exclusionary rule is designed to serve.
That purpose is served, the Court held, only by suppressing
evidence that “is in some sense the product of illegal
governmental activity.” Id. at 19 (internal quotation marks
omitted). In the context of a Payton violation, the illegality
doesn’t consist of gaining custody of the defendant; the
existence of probable cause to arrest provides a lawful basis
for that intrusion upon the defendant’s liberty. Id. at 18.
Instead, the illegality consists of the officers’ intrusion into
the privacy and sanctity of the home without prior judicial
authorization. Id. at 17. Only evidence that the police
discover as a result of having made the arrest “in the home
rather than someplace else” can be deemed the product of a
Payton violation. Id. at 19.

    Both the Supreme Court and our court have held that we
must suppress evidence seized during a pat-down search of
the defendant’s person following a Payton violation. See
Kirk v. Louisiana, 536 U.S. 635, 637–38 (2002) (per curiam);
United States v. Blake, 632 F.2d 731, 733, 736 (9th Cir.
1980). Those cases involved Payton violations in which the
police physically intruded into the home and conducted the
pat-down search while still inside. The question before us is
whether the rule of Kirk and Blake should be applied to
Payton violations involving a suspect who, like Nora, is
forced to exit his home in response to police coercion, such
that the pat-down search takes place outside the physical
confines of the home. The Sixth Circuit appears to have
applied the rule in these circumstances, albeit without
analysis. See United States v. Saari, 272 F.3d 804, 807, 812
(6th Cir. 2001) (upholding suppression of handgun found in
14                UNITED STATES V. NORA

defendant’s waistband after police ordered him to exit his
home).

    Deciding whether to apply a rule to a new factual scenario
requires knowing something of the rule’s rationale. Although
the exact rationale underlying the rule established in Kirk and
Blake wasn’t articulated, each of the potential rationales
supports extending the exclusionary rule to the scenario at
issue here. On the one hand, the rule could be based simply
on the notion that a Payton violation renders an arrest
unlawful, and a search incident to an unlawful arrest is itself
always unlawful, wherever it happens to occur. If Kirk and
Blake rest on that rationale, then deciding the suppression
issue before us is easy: The cash and marijuana found during
the search incident to Nora’s unlawful arrest must be
suppressed, even though the search occurred outside his home
in the front yard.

     On the other hand, Kirk and Blake could rest on the notion
that, when the police arrest a suspect by physically intruding
into his home without a warrant, any personal effects found
on his person must be suppressed in order to protect the
privacy and sanctity of the home. An individual might wear
or carry things on his person within the confines of his home
that he wouldn’t take with him when venturing out in public,
so items discovered during a pat-down search conducted
inside the home could well be “the fruit of having been
arrested in the home rather than someplace else.” Harris,
495 U.S. at 19. Viewed in that light, Payton’s protection of
the privacy and sanctity of the home would be incomplete if
it didn’t extend to the person of a suspect arrested inside his
home.
                  UNITED STATES V. NORA                      15

    That same rationale applies when the police violate
Payton by ordering a suspect to exit his home at gunpoint.
The home receives special constitutional protection in part
because “at the very core of the Fourth Amendment stands
the right of a man to retreat into his own home and there be
free from unreasonable governmental intrusion.” Payton,
445 U.S. at 589–90 (internal quotation marks and alterations
omitted). When the police unreasonably intrude upon that
interest by ordering a suspect to exit his home at gunpoint, the
suspect’s opportunity to collect himself before venturing out
in public is certainly diminished, if not eliminated altogether.
In this context, too, Payton’s protection of the privacy and
sanctity of the home would be incomplete if it didn’t extend
to the person of a suspect forced to abandon the refuge of his
home involuntarily.

    For these reasons, evidence seized during a pat-down
search incident to an arrest made in violation of Payton must
be suppressed, whether the search occurs inside the home, as
in Kirk and Blake, or outside the home, as in this case. In
either scenario, evidence found on the suspect’s person
should be regarded as “the fruit of having been arrested in the
home rather than someplace else.” Harris, 495 U.S. at 19.
Accordingly, the cash and marijuana seized during the search
incident to Nora’s arrest must be suppressed.

                               B

    We conclude that Nora’s post-arrest statements are
subject to suppression as well. Under our decision in United
States v. Shetler, 665 F.3d 1150 (9th Cir. 2011), Nora’s
statements must be deemed the fruit of the unlawful search of
his person.
16                UNITED STATES V. NORA

     In Shetler, the police conducted an extensive illegal
search of the defendant’s home while the defendant was
detained outside, watching as the search progressed. Id. at
1154. Officers found evidence of methamphetamine
production in the house and garage. When questioned by the
police 36 hours later, the defendant confessed to having
engaged in methamphetamine production. We held that the
defendant’s confession was the product of the illegal search
and had to be suppressed. We noted that in these
circumstances officers will likely use evidence gleaned from
the illegal search in questioning the suspect, and the suspect’s
answers “may be influenced by his knowledge that the
officials had already seized certain evidence.” Id. at 1158.
Because the government bore the burden of proving that the
defendant’s confession was not “fruit of the poisonous tree,”
id. at 1157, the government was required to produce evidence
demonstrating that the defendant’s answers “were not
induced or influenced by the illegal search.” Id. at 1158. The
government failed to do so.

    The same is true here. Nora’s incriminating statements
followed immediately on the heels of the unlawful search of
his person, which yielded marijuana and a large amount of
cash. Whether the police questioned Nora about that
evidence or not, his answers were likely influenced by his
knowledge that the police had already discovered it. As in
Shetler, the government produced no evidence to the
contrary. Nor has the government shown that intervening
circumstances rendered the connection between Nora’s
statements and the illegal search “so attenuated as to dissipate
the taint.” Id. at 1159 (internal quotation marks omitted).
Nora’s post-arrest statements must therefore be suppressed.
                    UNITED STATES V. NORA                          17

                                  C

    As to Nora’s identity—in particular, the record of his
prior convictions—we need not decide whether that evidence
is admissible. We will assume that it is, resolving any doubts
on that score in the government’s favor. As will become
clear, even on that assumption, we conclude that the
government cannot prevail.

                                 V

    In light of what we’ve said above, some of the evidence
included in the search warrant affidavit was admissible and
some of it wasn’t. The remaining question is whether that
fact renders the search warrant invalid in whole or in part.

     A search warrant isn’t rendered invalid merely because
some of the evidence included in the affidavit is tainted.
United States v. Reed, 15 F.3d 928, 933 (9th Cir. 1994). The
warrant remains valid if, after excising the tainted evidence,
the affidavit’s “remaining untainted evidence would provide
a neutral magistrate with probable cause to issue a warrant.”
Id. (internal quotation marks omitted); see also United States
v. Grandstaff, 813 F.2d 1353, 1355 (9th Cir. 1987). Thus,
after excising the cash and marijuana found on Nora’s person
and his post-arrest statements, we must determine whether the
remaining untainted evidence was sufficient to support
issuance of the warrant.3 We make that determination
without the usual deference owed to the magistrate’s initial


  3
     The government doesn’t challenge the district court’s decision to
suppress evidence discovered during a protective sweep of Nora’s home,
which officers conducted before obtaining the warrant, so we will
disregard that evidence as well.
18                UNITED STATES V. NORA

finding of probable cause. United States v. Kelley, 482 F.3d
1047, 1051 (9th Cir. 2007).

    Two principal pieces of evidence remain after excising
the tainted evidence from the affidavit: (1) the officers’
observation of Nora with a handgun under circumstances
establishing probable cause to believe he had violated
California Penal Code § 25850(a); and (2) the officers’
knowledge of Nora’s criminal history, in particular his prior
conviction for carrying a loaded firearm and his two prior
convictions for being a felon in possession of a firearm.

    This remaining, untainted evidence did not provide
probable cause to search Nora’s home for marijuana, heroin,
and methamphetamine, or for evidence of gang membership,
all of which were listed in the warrant as items subject to
seizure. Those portions of the warrant are therefore invalid.
That leaves the portion of the warrant authorizing the seizure
of “[f]irearms, assault rifles, handguns of any caliber and
shotguns of any caliber,” as well as ammunition for such
firearms. We must decide whether that portion of the warrant
is valid; if it is, the severance doctrine might apply. See
United States v. Gomez-Soto, 723 F.2d 649, 654 (9th Cir.
1984) (noting that, if applicable, the severance doctrine
“allows us to strike from a warrant those portions that are
invalid and preserve those portions that satisfy the fourth
amendment”).

    To satisfy the Fourth Amendment, the warrant’s firearms
clause must be supported by probable cause and describe with
particularity the items to be seized. United States v. Sells,
463 F.3d 1148, 1156 (10th Cir. 2006); In re Grand Jury
Subpoenas Dated Dec. 10, 1987, 926 F.2d 847, 857 (9th Cir.
1991). Because we conclude that the firearms clause was not
                  UNITED STATES V. NORA                    19

supported by probable cause, we need not decide whether the
clause satisfies the particularity requirement.

    The untainted evidence unquestionably provided probable
cause to search Nora’s home for the blue-steel semi-
automatic handgun the officers saw him carrying. Nora ran
into the house with the gun in his hand but exited without it,
giving the officers reason to believe it was still inside. The
gun was of course evidence of the crime for which the
officers had probable cause to arrest him and would therefore
have been subject to seizure on that basis alone. But without
more, the officers’ firsthand observations of Nora with a gun
in his hand did not give them reasonable grounds to believe
that any additional firearms would be found in the house. See
Millender v. Cnty. of Los Angeles, 620 F.3d 1016, 1025 (9th
Cir. 2010) (en banc), rev’d on other grounds sub nom.
Messerschmidt v. Millender, 132 S. Ct. 1235 (2012).

    The only other arguably untainted evidence the officers
had was knowledge of Nora’s criminal history. We have
stated that criminal history “can be helpful in establishing
probable cause, especially where the previous arrest or
conviction involves a crime of the same general nature as the
one the warrant is seeking to uncover.” Greenstreet v. Cnty.
of San Bernardino, 41 F.3d 1306, 1309 (9th Cir. 1994); see
also 2 Wayne R. LaFave, Search & Seizure: A Treatise on the
Fourth Amendment § 3.2(d), at 72 & n.147 (5th ed. 2012).
For example, in Hart v. Parks, 450 F.3d 1059 (9th Cir. 2006),
we noted that the suspect’s prior theft convictions were
“particularly relevant” (when combined with other evidence)
to determining whether the police had probable cause to
arrest him for another theft. Id. at 1066.
20                 UNITED STATES V. NORA

    By the same logic, Nora’s prior firearms convictions
might have been relevant if the officers had observed Nora
holding an object that appeared to be a firearm, and the issue
was whether the officers had probable cause to believe the
object was in fact a firearm. But here, the officers didn’t need
the prior convictions to support the inference that Nora in fact
possessed a firearm; they already had probable cause to
believe that. Rather, at issue is whether a fair probability
existed that Nora owned other firearms, in addition to the
single firearm the officers had observed. Nora’s prior
firearms convictions don’t speak to that issue and thus are of
marginal relevance to the probable cause issue before us.

    Our decision in United States v. Weber, 923 F.2d 1338
(9th Cir. 1991), illustrates the shortcoming here. In Weber,
the defendant ordered four photographs of children engaged
in sexually explicit acts from a fictitious distributor created as
part of a government-orchestrated sting operation. Id. at
1340. The agents planned to deliver the photographs to the
defendant’s home through a mail courier. They then sought
an anticipatory warrant to search the defendant’s home, not
just for the four photographs he had ordered, but for any other
photographs, books, magazines, and videotapes depicting
child pornography. Id. at 1340–41. To justify this much
broader search for child pornography, the warrant affidavit
contained an officer’s expert opinion regarding three classes
of suspects likely to keep such materials at home (“child
molesters,” “pedophiles,” and “child pornography
collectors”). Id. at 1341. We found the evidence insufficient
to establish probable cause to search for materials beyond the
four photographs involved in the sting. Although the expert’s
opinion described three classes of suspects likely to possess
the broad range of child pornography materials described in
                  UNITED STATES V. NORA                     21

the warrant, the government failed to demonstrate that the
defendant belonged to one of those classes. Id. at 1341, 1345.

    Here, the government’s evidence is insufficient for the
opposite reason: The affidavit established that Nora belonged
to a class of suspects with prior firearms convictions, but
didn’t show why that class of suspects would tend to own
multiple firearms. Nor did the affidavit contain other facts
tying Nora himself to firearms beyond the one he had been
observed carrying. Were we to hold that this evidence
suffices for probable cause, officers would have free rein to
search a suspect’s home anytime the suspect had prior
firearms convictions and was spotted with a single gun,
whether near his home or not. While the police in those
circumstances might have probable cause to search for the
specific firearm they observed, they would need evidence
tending to show that the suspect in question—or the class of
people to which the suspect belonged—possessed additional
firearms to justify a more expansive search. As we stated in
Weber, “probable cause to believe that some incriminating
evidence will be present at a particular place does not
necessarily mean there is probable cause to believe that there
will be more of the same.” Id. at 1344.

    We are thus left with no portion of the warrant that
satisfies the Fourth Amendment’s requirements. The officers
had probable cause to search for the blue-steel semi-
automatic handgun they saw Nora carrying, but the only
clause of the warrant addressing firearms did not specifically
describe that weapon. It instead purported to authorize the
seizure of firearms of any stripe, expanding the scope of the
search to include firearms for which the officers did not have
probable cause. Since a warrant must “be no broader than the
probable cause on which it is based,” id. at 1342, the firearms
22                UNITED STATES V. NORA

clause must be stricken as well. With no valid portion of the
warrant that could even potentially be saved, the severance
doctrine cannot apply.

    Because the entire warrant was invalid, the government’s
plain view argument also fails. In order for the plain view
doctrine to apply, “the officer must lawfully have been in the
place from which the object could be seen in plain view.”
United States v. Galpin, 720 F.3d 436, 451 (2d Cir. 2013); see
Minnesota v. Dickerson, 508 U.S. 366, 375 (1993). The
officers’ entry into Nora’s home was not authorized by a
valid warrant or an exception to the warrant requirement,
which means they were not lawfully present in the home in
the first place. The plain view doctrine is therefore
inapplicable. See United States v. Spilotro, 800 F.2d 959, 968
(9th Cir. 1986).

                      *       *       *

    Although Nora’s arrest was supported by probable cause,
the manner in which officers made the arrest violated Payton.
Evidence obtained as a result of Nora’s unlawful arrest must
be suppressed, which renders the portions of the warrant
authorizing a search for narcotics-related evidence and
evidence of gang membership invalid. The remaining
untainted evidence did not establish probable cause to search
Nora’s home for the broad range of firearms described in the
warrant. As a consequence, the entire warrant was invalid
and all evidence seized pursuant to it must be suppressed.
We reverse the district court’s order denying Nora’s
suppression motion and remand for further proceedings.

     REVERSED and REMANDED.
UNITED STATES V. NORA   23




     APPENDIX
                        24   UNITED STATES V. NORA




                                        Case 2:09-cr-00092-SVW Document ID: 862538211/02/09 Page 2 of Page: 31 ID #:189
                                         Case: 12-50485 05/10/2013      36-7 Filed    DktEntry: 10-2 3 Page of 257




                                  PAGE 23




United States v. Nora                                                         28                                          Excerpts of Record
CA # 12-50485                                                                                                             Volume II

```

---

## GROUP: content/cases/United States v. Ramsey.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Ramsey"
type: case
citation: "431 U.S. 606 (1977)"
parallel_cite: "97 S. Ct. 1972; 52 L. Ed. 2d 617"
neutral_cite: 1977 U.S. LEXIS 101
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-06-06
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1977-06-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Ramsey
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109675/united-states-v-ramsey/"
  cluster_id: 109675
  opinion_id: 109675
  identity_checked: true
homes:
  - page: "[[Border Searches]]"
    role: "Key — Anchor"
related: ["[[Carroll v. United States]]", "[[United States v. Flores-Montano]]", "[[United States v. Montoya de Hernandez]]"]
aliases: []
tags: ["case", "fourth-amendment", "border-searches", "international-mail", "customs", "reasonable-suspicion"]
holding: "Routine searches at the international border (including incoming international mail) require neither a warrant nor probable cause; the…"
lake:
  record_id: United States v. Ramsey
  status: verified
  projected_at: 2026-07-09
---

# United States v. Ramsey

*431 U.S. 606 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A customs inspector working incoming international mail opened envelopes mailed from Thailand to addresses in the United States. The envelopes were bulky, many times the weight of a normal airmail letter, and felt as though they contained something; inside, the inspector found heroin. Charged with importing heroin through the mails, the defendants moved to suppress, contending that opening the letters without a warrant violated the Fourth Amendment.

## Issue
Whether customs officials may open incoming international mail at the border without a warrant, consistent with the Fourth Amendment, when they have reasonable cause to suspect it contains contraband.

## Rule
Border searches are reasonable simply because they occur at the border. "That searches made at the border, pursuant to the longstanding right of the sovereign to protect itself by stopping and examining persons and property crossing into this country, are reasonable simply by virtue of the fact that they occur at the border, should, by now, require no extended demonstration." — 431 U.S. at 616. ^pin-616

The governing statute permits opening such mail on "reasonable cause to suspect" contraband — a standard less demanding than probable cause: "The 'reasonable cause to suspect' test adopted by the statute is, we think, a practical test which imposes a less stringent requirement than that of 'probable cause' imposed by the Fourth Amendment as a requirement for the issuance of warrants." — [431 U.S. at 612–613](https://www.courtlistener.com/opinion/109675/united-states-v-ramsey/#:~:text=with%20%22-,reasonable%20cause%20to%20suspect). ^pin-612

## Application
The inspector knew the letters were from Thailand, were bulky, were many times the weight of a normal airmail letter, and felt as though they held something — facts giving reasonable cause to suspect they contained merchandise or contraband. The search was authorized by statute, and because it was a border search it required neither a warrant nor probable cause; opening the envelopes therefore did not violate the Fourth Amendment.

## Conclusion
The warrantless opening of the international mail was a constitutional border search; the Supreme Court reversed the Court of Appeals and upheld the searches.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Ramsey* anchors the border-search exception and extends it to incoming international mail: routine border searches need neither a warrant nor probable cause, and the statutory "reasonable cause to suspect" standard for opening mail is less demanding than probable cause.

## Appears on
- [[Border Searches]] — *Key — Anchor*

## Sources
- *United States v. Ramsey*, 431 U.S. 606 (1977) — https://www.courtlistener.com/opinion/109675/united-states-v-ramsey/ — pinpoints: 612–613, 616 (parallel 97 S. Ct. 1972).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9a586b7b187031ae", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "431 U.S. 606 (1977)", "court": "U.S. Supreme Court", "neutral_cite": "1977 U.S. LEXIS 101", "official_citation_present": true, "parallel_cite": "97 S. Ct. 1972; 52 L. Ed. 2d 617", "title": "United States v. Ramsey", "year": "1977"}}
{"assertion_id": "1d731b0aaf9d0d21", "dimension": "support", "kind": "home_role", "locator": {"home": "Border Searches"}, "payload": {"home": "Border Searches", "role": "Key — Anchor", "title": "United States v. Ramsey"}}
{"assertion_id": "b9deb83992536f63", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Routine searches at the international border (including incoming international mail) require neither a warrant nor probable cause; the…", "title": "United States v. Ramsey"}}
{"assertion_id": "36ea7953d7f515fe", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1977-06-06", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Ramsey", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Ramsey", "varies_by_point": "false"}}
{"assertion_id": "8cd7ed6605fa3d56", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Ramsey"}}
```

### lake record — United States v. Ramsey

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Ramsey",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Ramsey",
    "case_name_short": "Ramsey",
    "case_name_full": "UNITED STATES v. RAMSEY Et Al.",
    "input_case_name": "United States v. Ramsey",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-06-06",
    "year": 1977,
    "docket": null,
    "cluster_id": 109675,
    "lead_opinion_id": 109675,
    "sibling_ids": [
      109675,
      9426823,
      9426824,
      9426825
    ],
    "absolute_url": "/opinion/109675/united-states-v-ramsey/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "431 U.S. 606",
      "volume": "431",
      "reporter": "U.S.",
      "page": "606",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "97 S. Ct. 1972",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "1972",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 L. Ed. 2d 617",
        "volume": "52",
        "reporter": "L. Ed. 2d",
        "page": "617",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 101",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "101",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "431 U.S. 606",
        "volume": "431",
        "reporter": "U.S.",
        "page": "606",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 1972",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "1972",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 L. Ed. 2d 617",
        "volume": "52",
        "reporter": "L. Ed. 2d",
        "page": "617",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 101",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "101",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "431 U.S. 606",
    "official_selection": {
      "court_class": "scotus",
      "selected": "431 U.S. 606",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-616",
      "page": null,
      "quote": "--- # United States v. Ramsey *431 U.S. 606 (1977)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A customs inspector working incoming international mail opened envelopes mailed from Thailand to addresses in the United States. The envelopes were bulky, many times the weight of a normal airmail letter, and felt as though they contained something; inside, the inspector found heroin. Charged with importing heroin through the mails, the defendants moved to suppress, contending that opening the letters without a warrant violated the Fourth Amendment. ## Issue Whether customs officials may open incoming international mail at the border without a warrant, consistent with the Fourth Amendment, when they have reasonable cause to suspect it contains contraband. ## Rule Border searches are reasonable simply because they occur at the border.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-612",
      "page": null,
      "quote": "reasonable cause to suspect",
      "star_marker": "607",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 1178,
      "fragment": "#:~:text=with%20%22-,reasonable%20cause%20to%20suspect",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1977-06-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Ramsey",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Caballero",
          "cluster_id": 7319742,
          "cite": [
            "178 F. Supp. 3d 1008",
            "2016 U.S. Dist. LEXIS 51132",
            "2016 WL 1546731"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cotterman",
          "cluster_id": 213651,
          "cite": [
            "637 F.3d 1068",
            "2011 U.S. App. LEXIS 6483",
            "2011 WL 1137302"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Stefan Irving",
          "cluster_id": 794720,
          "cite": [
            "452 F.3d 110",
            "2006 U.S. App. LEXIS 16077",
            "2006 WL 1735582"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Oladiji v. United States",
          "cluster_id": 8744707,
          "cite": [
            "953 F. Supp. 43",
            "1996 U.S. Dist. LEXIS 20367",
            "1996 WL 785758"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. LePera",
          "cluster_id": 6100913,
          "cite": [
            "197 A.D.2d 43",
            "611 N.Y.S.2d 394"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Antonio Sylvester Hill and Joseph Herbert Francois",
          "cluster_id": 565137,
          "cite": [
            "939 F.2d 934",
            "1991 U.S. App. LEXIS 19428",
            "1991 WL 148908"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Vincent Ezeiruaku",
          "cluster_id": 563242,
          "cite": [
            "936 F.2d 136",
            "1991 WL 105684"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Christopher Patrick, Linda Taylor and Christopher Patrick",
          "cluster_id": 538805,
          "cite": [
            "899 F.2d 169",
            "1990 U.S. App. LEXIS 4674"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Enrique Carreon",
          "cluster_id": 521938,
          "cite": [
            "872 F.2d 1436",
            "1989 U.S. App. LEXIS 5032",
            "1989 WL 36046"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Juan Manuel Caminos",
          "cluster_id": 457063,
          "cite": [
            "770 F.2d 361",
            "1985 U.S. App. LEXIS 22328"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
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
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
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
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
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
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
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
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
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
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dalia v. United States",
          "cluster_id": 110061,
          "cite": [
            "60 L. Ed. 2d 177",
            "99 S. Ct. 1682",
            "441 U.S. 238",
            "1979 U.S. LEXIS 89"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Andreas",
          "cluster_id": 111013,
          "cite": [
            "77 L. Ed. 2d 1003",
            "103 S. Ct. 3319",
            "463 U.S. 765",
            "1983 U.S. LEXIS 106",
            "51 U.S.L.W. 5157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. Rodriguez",
          "cluster_id": 11663,
          "cite": [
            "110 F.3d 299",
            "1997 WL 163525"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Villamonte-Marquez",
          "cluster_id": 110973,
          "cite": [
            "77 L. Ed. 2d 22",
            "103 S. Ct. 2573",
            "462 U.S. 579",
            "1983 U.S. LEXIS 68",
            "51 U.S.L.W. 4812"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
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
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
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
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rita Ann Cardenas and Shamsideen Abiodun Lawal",
          "cluster_id": 657339,
          "cite": [
            "9 F.3d 1139"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. Puerto Rico",
          "cluster_id": 2620876,
          "cite": [
            "61 L. Ed. 2d 1",
            "99 S. Ct. 2425",
            "442 U.S. 465",
            "1979 U.S. LEXIS 111"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Flores-Montano",
          "cluster_id": 134729,
          "cite": [
            "158 L. Ed. 2d 311",
            "124 S. Ct. 1582",
            "541 U.S. 149",
            "2004 U.S. LEXIS 2548",
            "72 U.S.L.W. 4263",
            "17 Fla. L. Weekly Fed. S 207"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stuart Romm",
          "cluster_id": 795139,
          "cite": [
            "455 F.3d 990",
            "2006 U.S. App. LEXIS 18474",
            "2006 WL 2042827"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
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
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pierce v. Smith",
          "cluster_id": 12443,
          "cite": [
            "117 F.3d 866",
            "13 I.E.R. Cas. (BNA) 8",
            "1997 U.S. App. LEXIS 17907",
            "1997 WL 395259"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Frank Gunnar Williams",
          "cluster_id": 375926,
          "cite": [
            "617 F.2d 1063",
            "1980 U.S. App. LEXIS 17636",
            "1980 A.M.C. 2550"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Serafin Alfonso, Humberto Rayo, Fabian Mora, Primo Antonio Serrano-Tellez",
          "cluster_id": 450644,
          "cite": [
            "759 F.2d 728",
            "18 Fed. R. Serv. 1398",
            "1985 U.S. App. LEXIS 30539"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alfaro-Moncada",
          "cluster_id": 147332,
          "cite": [
            "607 F.3d 720",
            "2010 A.M.C. 1680",
            "2010 U.S. App. LEXIS 10841",
            "2010 WL 2103442"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elias Attallah, Violeta Lajam De Attallah, and the Conjugal Partnership They Comprise v. United States",
          "cluster_id": 577110,
          "cite": [
            "955 F.2d 776",
            "1992 U.S. App. LEXIS 1454",
            "1992 WL 17486"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hensel",
          "cluster_id": 8926652,
          "cite": [
            "699 F.2d 18"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Silveus",
          "cluster_id": 1439120,
          "cite": [
            "542 F.3d 993",
            "50 V.I. 1101",
            "2008 U.S. App. LEXIS 19224",
            "2008 WL 4138460"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reporters Committee for Freedom of the Press v. American Telephone & Telegraph Company",
          "cluster_id": 363949,
          "cite": [
            "593 F.2d 1030",
            "192 U.S. App. D.C. 376"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109675 OR 9426823 OR 9426824 OR 9426825) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NjYxMjgwMDAwMDAmcz00NDE3NDYmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109675+OR+9426823+OR+9426824+OR+9426825%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 10,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 12,
        "triage_snippet_classified": 188
      },
      "lane2_top_cited": {
        "query": "cites:(109675 OR 9426823 OR 9426824 OR 9426825)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05OCZzPTU3MzA2NyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109675+OR+9426823+OR+9426824+OR+9426825%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109675 OR 9426823 OR 9426824 OR 9426825)",
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
    "complete_query": "cites:(109675 OR 9426823 OR 9426824 OR 9426825)",
    "indexed_citing_opinions": 459,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109675,
        "count": 393,
        "count_source": "search"
      },
      {
        "opinion_id": 9426823,
        "count": 86,
        "count_source": "search"
      },
      {
        "opinion_id": 9426824,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426825,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 663,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-ramsey.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY5ODE2NDgmcz00Nzk5ODI0JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109675+OR+9426823+OR+9426824+OR+9426825%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109675,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 90759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 103143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 105930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 106078,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 108083,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 108332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 108841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 108854,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 109011,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 109097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 109504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 265141,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 307979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 321210,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 326933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 327074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 328030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 337566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 337725,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 339048,
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
    "date_created": "2026-07-06T02:24:42Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:24:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:24:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:28:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:24:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Ramsey

```
<div>
<center><b><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">431 U.S. 606</a></span> (1977)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
RAMSEY ET AL.</h1></center>
<center>No. 76-167.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 30, 1977.</center>
<center>Decided June 6, 1977.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE DISTRICT OF COLUMBIA CIRCUIT.
<p><span class="star-pagination">*607</span> <i>Kenneth S. Geller</i> argued the cause for the United States. on the brief were <i>Solicitor General Bork, Assistant Attorney General Thornburgh,</i> and <i>Jerome M. Feit.</i></p>
<p><i>Allan M. Palmer</i> argued the cause and filed a brief for respondent Ramsey. <i>Irving R. M. Panzer,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./429/916/">429 U. S. 916</a></span>, argued the cause and filed a brief for respondent Kelly.<sup>[*]</sup></p>
<p>MR. JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>Customs officials, acting with "reasonable cause to suspect" a violation of customs laws, opened for inspection incoming international letter-class mail without first obtaining a search warrant. A divided Court of Appeals for the District of Columbia <span class="star-pagination">*608</span> Circuit held, contrary to every other Court of Appeals which has considered the matter,<sup>[1]</sup> that the Fourth Amendment forbade the opening of such mail without probable cause and a search warrant. 176 U. S. App. D. C. 67, <span class="citation" data-id="9462874"><a href="/opinion/337566/united-states-v-charles-w-ramsey-united-states-of-america-v-james-w/" aria-description="Citation for case: United States v. Charles W. Ramsey, United States of...">538 F. 2d 415</a></span>. We granted the Government's petition for certiorari to resolve this Circuit conflict. <span class="citation multiple-matches"><a href="/c/U.%20S./429/815/">429 U. S. 815</a></span>. We now reverse.</p>
<p></p>
<h2>I</h2>
<p>Charles W. Ramsey and James W. Kelly jointly commenced a heroin-by-mail enterprise in the Washington, D. C., area. The process involved their procuring of heroin, which was mailed in letters from Bangkok, Thailand, and sent to various locations in the District of Columbia area for collection. Two of their suppliers, Sylvia Bailey and William Ward, who were located in West Germany, were engaged in international narcotics trafficking during the latter part of 1973 and the early part of 1974. West German agents, pursuant to court-authorized electronic surveillance, intercepted several trans-Atlantic conversations between Bailey and Ramsey during which their narcotics operation was discussed. By late January 1974, Bailey and Ward had gone to Thailand. Thai <span class="star-pagination">*609</span> officials, alerted to their presence by West German authorities, placed them under surveillance. Ward was observed mailing letter-sized envelopes in six different mail boxes; five of these envelopes were recovered; and one of the addresses in Washington, D. C., was later linked to respondents. Bailey and Ward were arrested by Thai officials on February 2, 1974; among the items seized were eleven heroin-filled envelopes addressed to the Washington, D. C., area, and later connected with respondents.</p>
<p>Two days after this arrest of Bailey and Ward, Inspector George Kallnischkies, a United States customs officer in New York City, without any knowledge of the foregoing events, inspecting a sack of incoming international mail from Thailand, spotted eight envelopes that were bulky and which he believed might contain merchandise.<sup>[2]</sup> The envelopes, all of which appeared to him to have been typed on the same typewriter, were addressed to four different locations in the Washington, D. C., area. Inspector Kallnischkies, based on the fact that the letters were from Thailand, a known source of narcotics, and were "rather bulky," suspected that the envelopes might contain merchandise or contraband rather than correspondence. He took the letters to an examining area in the post office, and felt one of the letters: It "felt like there was something in there, in the envelope. It was not just plain paper that the envelope is supposed to contain." He weighed one of the envelopes, and found it weighed 42 grams, some three to six times the normal weight of an airmail letter. Inspector Kallnischkies then opened that envelope:<sup>[3]</sup></p>
<blockquote>"In there I saw some cardboard and between the cardboard, if I recall, there was a plastic bag containing a <span class="star-pagination">*610</span> white powdered substance, which, based on experience, I knew from Thailand would be heroin.</blockquote>
<blockquote>"I went ahead and removed a sample. Gave it a field test, a Marquis Reagent field test, and I had a positive reaction for heroin." App. 32.</blockquote>
<p>He proceeded to open the other seven envelopes which "in a lot of ways were identical"; examination revealed that at least the contents were in fact identical: each contained heroin.</p>
<p>The envelopes were then sent to Washington in a locked pouch where agents of the Drug Enforcement Administration, after obtaining a search warrant, opened the envelopes again and removed most of the heroin.<sup>[4]</sup> The envelopes were then resealed, and six of them were delivered under surveillance. After Kelly collected the envelopes from the three different addressees, rendezvoused with Ramsey, and gave Ramsey a brown paper bag, federal agents arrested both of them. The bag contained the six envelopes with heroin, $1,100 in cash, and "cutting" material for the heroin. The next day, in executing a search upon warrant of Ramsey's residence, agents recovered, <i>inter alia,</i> two pistols.</p>
<p>Ramsey and Kelly were indicted, along with Bailey and Ward, in a 17-count indictment.<sup>[5]</sup> Respondents moved to <span class="star-pagination">*611</span> suppress the heroin and the two pistols.<sup>[6]</sup> The District Court denied the motions, and after a bench trial on the stipulated record, respondents were found guilty and sentenced to imprisonment for what is in effect a term of 10 to 30 years. The Court of Appeals for the District of Columbia Circuit, one judge dissenting, reversed the convictions, holding that the "border search exception to the warrant requirement" applicable to persons, baggage, and mailed packages did not apply to the routine opening of international letter mail, and held that the Constitution requires that "before international letter mail is opened, a showing of probable cause be made to and a warrant secured from a neutral magistrate." 176 U. S. App. D. C., at 73, <span class="citation" data-id="9462874"><a href="/opinion/337566/united-states-v-charles-w-ramsey-united-states-of-america-v-james-w/#421" aria-description="Citation for case: United States v. Charles W. Ramsey, United States of...">538 F. 2d, at 421</a></span>.<sup>[7]</sup></p>
<p></p>
<h2>II</h2>
<p>Congress and the applicable postal regulations authorized the actions undertaken in this case. Title <span class="citation no-link">19 U. S. C. § 482</span>, a recodification of Rev. Stat. § 3061, and derived from § 3 of the Act of July 18, 1866, <span class="citation no-link">14 Stat. 178</span>, explicitly deals with the search of an "envelope":</p>
<blockquote>"Any of the officers or persons authorized to board or search vessels may . . . search any trunk or envelope, wherever found, in which he may have a reasonable cause to suspect there is merchandise which was imported contrary to law . . . ."</blockquote>
<p>This provision authorizes customs officials to inspect, under <span class="star-pagination">*612</span> the circumstances therein stated, incoming international mail.<sup>[8]</sup> The "reasonable cause to suspect" test adopted by the statute is, we think, a practical test which imposes a less stringent <span class="star-pagination">*613</span> requirement than that of "probable cause" imposed by the Fourth Amendment as a requirement for the issuance of warrants. See <i>United States</i> v. <i>King,</i> <span class="citation" data-id="328030"><a href="/opinion/328030/united-states-v-edward-king-and-mose-franklin-pearson/" aria-description="Citation for case: United States v. Edward King and Mose Franklin Pearson">517 F. 2d 350</a></span>, 352 <span class="star-pagination">*614</span> (CA5 1975); cf. <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#8" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 8, 21-22, 27</a></span> (1968). Inspector Kallnischkies, at the time he opened the letters, knew that they were from Thailand, were bulky, were many times the weight of a normal airmail letter, and "felt like there was something in there." Under these circumstances, we have no doubt that he had reasonable "cause to suspect" that there was merchandise or contraband in the envelopes.<sup>[9]</sup><span class="star-pagination">*615</span> The search, therefore, was plainly authorized by the statute.<sup>[10]</sup></p>
<p>Since the search in this case was authorized by statute, we are left simply with the question of whether the search, nevertheless violated the Constitution. Cf. <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#877" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 877</a></span> (1975). Specifically, we need not decide whether Congress conceived the statute as a necessary precondition to the validity of the search or whether it was viewed, instead, as a limitation on otherwise existing authority of the Executive.<sup>[11]</sup> Having acted pursuant to, and <span class="star-pagination">*616</span> within the scope of, a congressional Act, Inspector Kallnischkies' searches were permissible unless they violated the Constitution.</p>
<p></p>
<h2>III</h2>
<p></p>
<h2>A</h2>
<p>That searches made at the border, pursuant to the longstanding right of the sovereign to protect itself by stopping and examining persons and property crossing into this country, are reasonable simply by virtue of the fact that they occur at the border, should, by now, require no extended demonstration. The Congress which proposed the Bill of Rights, including the Fourth Amendment, to the state legislatures on September 25, 1789, <span class="citation no-link">1 Stat. 97</span>, had, some two months prior to that proposal, enacted the first customs statute, Act of July 31, 1789, c. 5, <span class="citation no-link">1 Stat. 29</span>. Section 24 of this statute granted customs officials "full power and authority" to enter and search "any ship or vessel, in which they shall have reason to suspect any goods, wares or merchandise subject to duty shall be concealed . . . ." This acknowledgment of plenary customs power was differentiated from the more limited power to enter and search "any particular dwelling-house, store, building, or other place . . ." where a warrant upon "cause to suspect" was required.<sup>[12]</sup> The historical importance of the <span class="star-pagination">*617</span> enactment of this customs statute by the same Congress which proposed the Fourth Amendment is, we think, manifest. This Court so concluded almost a century ago. In <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#623" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 623</a></span> (1886), this Court observed:</p>
<blockquote>"The seizure of stolen goods is authorized by the common law; and the seizure of goods forfeited for a breach of the revenue laws, or concealed to avoid the duties payable on them, has been authorized by English statutes for at least two centuries past; and the like seizures have been authorized by our own revenue acts from the commencement of the government. The first statute passed by Congress to regulate the collection of duties, the act of July 31, 1789, <span class="citation no-link">1 Stat. 29</span>, 43, contains provisions to this effect. <i>As this act was passed by the same Congress which proposed for adoption the original amendments to the Constitution, it is clear that the members of that body did not regard searches and seizures of this kind as `unreasonable,' and they are not embraced within the prohibition of the amendment.</i>" (Emphasis supplied.)</blockquote>
<p>This interpretation, that border searches were not subject to the warrant provisions of the Fourth Amendment and were "reasonable" within the meaning of that Amendment, has been faithfully adhered to by this Court. <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), after noting that "[t]he Fourth Amendment <span class="star-pagination">*618</span> does not denounce all searches or seizures, but only such as are unreasonable," <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#147" aria-description="Citation for case: Carroll v. United States"><i>id.,</i> at 147</a></span>, recognized the distinction between searches within this country, requiring probable cause, and border searches, <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">id.,</a></span></i> at 153-154:</p>
<blockquote>"It would be intolerable and unreasonable if a prohibition agent were authorized to stop every automobile on the chance of finding liquor and thus subject all persons lawfully using the highways to the inconvenience and indignity of such a search. <i>Travellers may be so stopped in crossing an international boundary because of national self protection reasonably requiring one entering the country to identify himself as entitled to come in, and his belongings as effects which may be lawfully brought in.</i> But those lawfully within the country . . . have a right to free passage without interruption or search unless there is known to a competent official authorized to search, probable cause for believing that their vehicles are carrying contraband or illegal merchandise."<sup>[13]</sup> (Emphasis supplied.)</blockquote>
<p>More recently, we noted this longstanding history in <i>United States</i> v. <i>Thirty-seven Photographs,</i> <span class="citation" data-id="9424558"><a href="/opinion/108332/united-states-v-thirty-seven-37-photographs/#376" aria-description="Citation for case: United States v. Thirty-Seven (37) Photographs">402 U. S. 363, 376</a></span> (1971):</p>
<blockquote>"But a port of entry is not a traveler's home. His right to be let alone neither prevents the search of his luggage nor the seizure of unprotected, but illegal, materials when his possession of them is discovered during such a search. Customs officials characteristically inspect luggage and their power to do so is not questioned in this case; it is an old practice and is intimately associated with excluding illegal articles from the country."</blockquote>
<p><span class="star-pagination">*619</span> In <i>United States</i> v. <i>12 200-Ft. Reels of Film,</i> <span class="citation" data-id="9425385"><a href="/opinion/108841/united-states-v-12-200-ft-reels-of-super-8mm-film/#125" aria-description="Citation for case: United States v. 12 200-Ft. Reels of Super 8MM. Film">413 U. S. 123, 125</a></span> (1973), we observed: "Import restrictions and searches of persons or packages at the national borders rest on different considerations and different rules of constitutional law from domestic regulations. The Constitution gives Congress broad, comprehensive powers `[t]o regulate Commerce with foreign Nations.' Art. I, § 8, cl. 3. Historically such broad powers have been necessary to prevent smuggling and to prevent prohibited articles from entry." Finally, citing <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> and <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>,</i> this Court stated in <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#272" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 272</a></span> (1973), that it was "without doubt" that the power to exclude aliens "can be effectuated by routine inspections and searches of individuals or conveyances seeking to cross our borders." See also <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#288" aria-description="Citation for case: Almeida-Sanchez v. United States"><i>id.,</i> at 288</a></span> (WHITE, J., dissenting).</p>
<p>Border searches, then, from before the adoption of the Fourth Amendment, have been considered to be "reasonable" by the single fact that the person or item in question had entered into our country from outside. There has never been any additional requirement that the reasonableness of a border search depended on the existence of probable cause. This longstanding recognition that searches at our borders without probable cause and without a warrant are nonetheless "reasonable" has a history as old as the Fourth Amendment itself.<sup>[14]</sup> We reaffirm it now.</p>
<p></p>
<h2>B</h2>
<p>Respondents urge upon us, however, the position that mailed letters are somehow different, and, whatever may be the normal rule with respect to border searches, different considerations, requiring the full panoply of Fourth Amendment <span class="star-pagination">*620</span> protections, apply to international mail. The Court of Appeals agreed, and felt that whatever the rule may be with respect to travelers, their baggage, and even mailed packages, it would not "extend" the border-search exception to include mailed letter-size envelopes. 176 U. S. App. D. C., at 73, <span class="citation" data-id="9462874"><a href="/opinion/337566/united-states-v-charles-w-ramsey-united-states-of-america-v-james-w/#421" aria-description="Citation for case: United States v. Charles W. Ramsey, United States of...">538 F. 2d, at 421</a></span>. We do not agree that this inclusion of letters within the border-search exception represents any "extension" of that exception.</p>
<p>The border-search exception is grounded in the recognized right of the sovereign to control, subject to substantive limitations imposed by the Constitution, who and what may enter the country. It is clear that there is nothing in the rationale behind the border-search exception which suggests that the mode of entry will be critical. It was conceded at oral argument that customs officials could search, without probable cause and without a warrant, envelopes carried by an entering traveler, whether in his luggage or on his person. Tr. of Oral Arg. 43-44. Surely no different constitutional standard should apply simply because the envelopes were mailed, not carried. The critical fact is that the envelopes cross the border and enter this country, not that they are brought in by one mode of transportation rather than another. It is their entry into this country from without it that makes a resulting search "reasonable."</p>
<p>Almost a century ago this Court rejected such a distinction in construing a protocol to the Treaty of Berne, <span class="citation no-link">19 Stat. 604</span>, which prohibited the importation of letters which might contain dutiable items. <i>Cotzhausen</i> v. <i>Nazro,</i> <span class="citation" data-id="90759"><a href="/opinion/90759/cotzhausen-v-nazro/" aria-description="Citation for case: Cotzhausen v. Nazro">107 U. S. 215</a></span> (1883). Condemning the unsoundness of any distinction between entry by mail and entry by other means, Mr. Justice Miller, on behalf of a unanimous Court, wrote, <i><span class="citation" data-id="90759"><a href="/opinion/90759/cotzhausen-v-nazro/" aria-description="Citation for case: Cotzhausen v. Nazro">id.,</a></span></i> at 218:</p>
<blockquote>"Of what avail would it be that every passenger, citizen and foreigner, without distinction of country or sex, is compelled to sign a declaration before landing, either <span class="star-pagination">*621</span> that his trunks and satchels in hand contain nothing liable to duty, or if they do, to state what it is, and even the person may be subjected to a rigid examination, if the mail is to be left unwatched, and all its sealed contents, even after delivery to the person to whom addressed, are to be exempt from seizure, though laces, jewels, and other dutiable matter of great value may thus be introduced from foreign countries."</blockquote>
<p>The historically recognized scope of the border-search doctrine, suggests no distinction in constitutional doctrine stemming from the mode of transportation across our borders. The contrary view of the Court of Appeals and respondents stems, we think, from an erroneous reading of <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S., at 153</a></span>, under which the Court of Appeals reasoned that "the rationale of the border search exception . . . is based upon . . . the difficulty of obtaining a warrant when the subject of the search is mobile, as a car or person . . . ." 176 U. S. App. D. C., at 70, <span class="citation" data-id="9462874"><a href="/opinion/337566/united-states-v-charles-w-ramsey-united-states-of-america-v-james-w/#418" aria-description="Citation for case: United States v. Charles W. Ramsey, United States of...">538 F. 2d, at 418</a></span>.<sup>[15]</sup></p>
<p>The fundamental difficulty with this position is that the "border search" exception is not based on the doctrine of "exigent circumstances" at all. It is a longstanding, historically recognized exception to the Fourth Amendent's general principle that a warrant be obtained, and in this respect is like the similar "search incident to lawful arrest" exception treated in <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#224" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 224</a></span> (1973). We think that the language in <i>Carroll</i> v. <i>United States, supra</i><i>,</i> makes this point abundantly clear. The <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> Court <span class="star-pagination">*622</span> quoted verbatim the above-quoted language from <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886), including the reference to customs searches and seizures of the kind authorized by <span class="citation no-link">1 Stat. 29</span>, 43, as being neither "unreasonable" nor "embraced within the prohibition of the [Fourth] [A]mendment." Later in the opinion, the Court commented that having "established that contraband goods concealed and illegally transported in an automobile or other vehicle may be searched for <i>without a warrant,</i> we come now to consider under what circumstances such search may be made." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S., at 153</a></span> (emphasis supplied). It then, in the passage quoted <i>supra,</i> at 618, distinguished, among these types of searches which required no warrant, those which required <i>probable cause</i> from those which did not: border searches did not; vehicular searches inside the country did. <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> thus recognized that there was no "probable cause" requirement at the border. This determination simply has nothing to do with "exigent circumstances."</p>
<p>The Court of Appeals also relied upon what it described as this Court's refusal in recent years twice "to take an expansive view of the border search exception or the authority of the Border Patrol. See <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> . . . (1975); <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> . . . (1973)." 176 U. S. App. D. C., at 72, <span class="citation" data-id="9462874"><a href="/opinion/337566/united-states-v-charles-w-ramsey-united-states-of-america-v-james-w/#420" aria-description="Citation for case: United States v. Charles W. Ramsey, United States of...">538 F. 2d, at 420</a></span>. But, as the language from each of these opinions suggests, <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#876" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 876, 884</a></span>; 413 U. S., at 272-273, plenary border-search authority was not implicated by our refusal to uphold searches and stops made at places in the interior of the country; the express premise for each holding was that the checkpoint or stop in question was not the border or its "functional equivalent."</p>
<p>In view of the wealth of authority establishing the border search as "reasonable" within the Fourth Amendment even though there be neither probable cause nor a warrant, we reject the distinctions made by the Court of Appeals in its opinion.</p>
<p><span class="star-pagination">*623</span> Nor do we agree that, under the circumstances presented by this case, First Amendment considerations dictate a full panoply of Fourth Amendment rights prior to the border search of mailed letters. There is, again, no reason to distinguish between letters mailed into the country, and letters carried on the traveler's person.<sup>[16]</sup> More fundamentally, however, the existing system of border searches has not been shown to invade protected First Amendment rights,<sup>[17]</sup> and hence there is no reason to think that the potential presence of correspondence makes the otherwise constitutionally reasonable search "unreasonable."</p>
<p>The statute in question requires that there be "reasonable cause to believe" the customs laws are being violated prior to the opening of envelopes. Applicable postal regulations flatly prohibit, under all circumstances, the reading of correspondence absent a search warrant, <span class="citation no-link">19 CFR § 145.3</span> (1976):</p>
<blockquote>"No customs officer or employee shall read or authorize or allow any other person to read any correspondence contained in sealed letter mail of foreign origin unless a search warrant has been obtained in advance from an appropriate judge or U. S. magistrate which authorizes such action."</blockquote>
<p>Cf. <span class="citation no-link">18 U. S. C. § 1702</span>.</p>
<p>We are unable to agree with the Court of Appeals that the opening of international mail in search of customs violations, <span class="star-pagination">*624</span> under the above guidelines, impermissibly chills the exercise of free speech. Accordingly, we find it unnecessary to consider the constitutional reach of the First Amendment in this area in the absence of the existing statutory and regulatory protection.<sup>[18]</sup> Here envelopes are opened at the border only when the customs officers have reason to believe they contain other than correspondence, while the reading of any correspondence inside the envelopes is forbidden. Any "chill" that might exist under these circumstances may fairly be considered not only "minimal," <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#560" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 560, 562</a></span> (1976); cf. <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S. 311, 316-317</a></span> (1972), but also wholly subjective.<sup>[19]</sup></p>
<p>We therefore conclude that the Fourth Amendment does not interdict the actions taken by Inspector Kallnischkies in <span class="star-pagination">*625</span> opening and searching the eight envelopes. The judgment of the Court of Appeals is, therefore,</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE POWELL, concurring.</p>
<p>The statute at issue expressly authorizes customs officials to "search any . . . envelope" at the border where there is "reasonable cause to suspect" the importation of contraband. <span class="citation no-link">19 U. S. C. § 482</span>. In view of the necessarily enhanced power of the Federal Government to enforce customs laws at the border, I have no doubt that this statuterequiring as a precondition to the opening of mail "reasonable cause to suspect" a violation of lawadequately protects both First and Fourth Amendment rights.<sup>[*]</sup></p>
<p>I therefore join in the judgment of the Court. On the understanding that the precedential effect of today's decision does not go beyond the validity of mail searches at the border pursuant to the statute, I also join the opinion of the Court.</p>
<p>MR. JUSTICE STEVENS, with whom MR. JUSTICE BRENNAN and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>The decisive question in this case is whether Congress has granted customs officials the authority to open and inspect personal letters entering the United States from abroad without the knowledge or consent of the sender or the addressee, and without probable cause to believe the mail contains contraband or dutiable merchandise.</p>
<p>In 1971 the Department of the Treasury and the Post Office Department first asserted that Congress had granted such authority in an awkwardly drafted statute enacted in 1866. <span class="star-pagination">*626</span> Under the earlier practice, which had been consistently followed for 105 years, customs officials were not allowed to open foreign mail except in the presence, and with the consent, of the addressees,<sup>[1]</sup> unless of course a warrant supported by probable cause had been first obtained. There are five reasons why I am convinced that Congress did not authorize the kind of secret searches of private mail that the Executive here conducted.</p>
<p>First, throughout our history Congress has respected the individual's interest in private communication. The notion that private letters could be opened and inspected without notice to the sender or the addressee is abhorrent to the tradition of privacy and freedom to communicate protected by the Bill of Rights. I cannot believe that any member of the Congress would grant such authority without considering its constitutional implications.<sup>[2]</sup></p>
<p><span class="star-pagination">*627</span> Second, the legislative history of the 1866 statute unambiguously discloses that this very concern was voiced during debate by Senator Howe, and that he was assured by the sponsor of the legislation that the bill would not authorize the examination of the United States mails. This colloquy is too plain to be misunderstood:</p>
<blockquote>"Mr. HOWE. The second and third sections of this bill speak of the seizure, search, and examination of all trunks, packages, and envelopes. It seems to me that language is broad enough to cover the United States mails. I suppose it is not the purpose of the bill to authorize the examination of the United States mails.</blockquote>
<blockquote>"Mr. MORRILL [sponsor of the bill]. Of course not.</blockquote>
<blockquote>"Mr. HOWE. I propose to offer an amendment to prevent such a construction.</blockquote>
<blockquote>"Mr. EDMUNDS. There is no danger of such a construction being placed upon this language. It is the language usually employed in these bills.</blockquote>
<blockquote>"Mr. HOWE. If gentlemen are perfectly confident that it will bear no such construction, and will receive no such construction, I do not care to press it.</blockquote>
<blockquote>"The PRESIDING OFFICER. The Senator from Wisconsin withdraws his amendment."<sup>[3]</sup></blockquote>
<p><span class="star-pagination">*628</span> Third, the language of the statute itself, when read in its entirety, quite plainly has reference to packages of the kind normally used to import dutiable merchandise.<sup>[4]</sup> It is true <span class="star-pagination">*629</span> that buried deep in the first long sentence in § 3 of the Act to prevent smuggling there is an authorization to "search any trunk or envelope, wherever found." I do not believe, however, that the word "envelope" as there used was intended to refer to ordinary letters. Contemporary American dictionaries <span class="star-pagination">*630</span> emphasize the usage of the word as descriptive of a package or wrapper as well as an ordinary letter.<sup>[5]</sup> This emphasis is consistent with the text of the bill as originally introduced, which used the phrase "any trunk, or other envelope."<sup>[6]</sup> Moreover, in 1866 when the Act was passed, there was no concern expressed in Congress about the smuggling of merchandise that would fit in a letter-size envelope.<sup>[7]</sup> A legislative decision to authorize the secret search of private mail would surely be expressed in plainer language than is found in the long statutory provision quoted in the margin; at the very least it would be supported by some affirmative evidence in the legislative history rather than the total disclaimer in the colloquy quoted above.</p>
<p><span class="star-pagination">*631</span> Fourth, the consistent construction of the statutory authorization by a series of changing administrations over a span of 105 years must be accorded great respect.<sup>[8]</sup><i>NLRB</i> v. <i>Bell Aerospace Co.,</i> <span class="citation" data-id="9425683"><a href="/opinion/109011/national-labor-relations-board-v-bell-aerospace-co/#274" aria-description="Citation for case: National Labor Relations Board v. Bell Aerospace Co.">416 U. S. 267, 274-275</a></span>; <i>Helvering</i> v. <i>Reynolds Co.,</i> <span class="citation" data-id="103143"><a href="/opinion/103143/helvering-v-r-j-reynolds-tobacco-co/#114" aria-description="Citation for case: Helvering v. R. J. Reynolds Tobacco Co.">306 U. S. 110, 114-115</a></span>. If the Executive perceives that new conditions and problems justify enlargement of the authority that had been found adequate for over a century, then these matters should be brought to the attention of Congress. Cf. <i>H. K. Porter Co.</i> v. <i>NLRB,</i> <span class="citation" data-id="9424188"><a href="/opinion/108083/h-k-porter-co-v-national-labor-relations-board/#109" aria-description="Citation for case: H. K. Porter Co. v. National Labor Relations Board">397 U. S. 99, 109</a></span>.<sup>[9]</sup></p>
<p>Finally, the asserted justification for the broad power claimed is so weak that it is difficult to believe that Congress would accept it without the most searching analysis. The fear the new practice is intended to overcome is that the addressee of a suspicious item of mail would withhold consent to open foreign mail, thereby necessitating the return of the item to the sender. But the refusal to accept delivery without disclosing the contents of a suspicious letter would itself be a fact which could be consideredalong with whatever indicia caused the inspector to regard the item with suspicion in the first place in a probable-cause determination. There is no reason to believe that the alternatives of probable cause or consent would lead to the extensive return of contraband that <span class="star-pagination">*632</span> would otherwise be confiscated on the basis of "reasonable cause to suspect."</p>
<p>If the Government is allowed to exercise the power it claims, the door will be open to the wholesale, secret examination of all incoming international letter mail. No notice would be necessary either before or after the search. Until Congress has made an unambiguous policy decision that such an unprecedented intrusion upon a vital method of personal communication is in the Nation's interest, this Court should not address the serious constitutional question it decides today. For it is settled that</p>
<blockquote>"when action taken by an inferior governmental agency was accomplished by procedures which raise serious constitutional questions, an initial inquiry will be made to determine whether or not `the President or Congress, within their respective constitutional powers, specifically has decided that the imposed procedures are necessary and warranted and has authorized their use.' [<i>Greene</i> v. <i>McElroy,</i> <span class="citation" data-id="9421855"><a href="/opinion/105930/greene-v-mcelroy/" aria-description="Citation for case: Greene v. McElroy">360 U. S. 474</a></span>,] 507." <i>Hannah</i> v. <i>Larche,</i> <span class="citation" data-id="9422021"><a href="/opinion/106078/hannah-v-larche/#430" aria-description="Citation for case: Hannah v. Larche">363 U. S. 420, 430</a></span>.</blockquote>
<p>Cf. <i>Ashwander</i> v. <i>Tennessee Valley Authority,</i> <span class="citation" data-id="9418878"><a href="/opinion/102605/ashwander-v-tennessee-valley-authority/#347" aria-description="Citation for case: Ashwander v. Tennessee Valley Authority">297 U. S. 288, 347-348</a></span> (Brandeis, J., concurring). Accordingly, I would affirm the judgment of the Court of Appeals.</p>
<h2>NOTES</h2>
<p>[*]  <i>Melvin L. Wulf, Joel M. Gora,</i> and <i>Jack D. Novik</i> filed a brief for the American Civil Liberties Union as <i>amicus curiae</i> urging affirmance.</p>
<p>[1]  Several Courts of Appeals have held that international letter-class mail may be opened, pursuant to a border search, without probable cause and without a warrant. <i>United States</i> v. <i>Milroy,</i> <span class="citation" data-id="337725"><a href="/opinion/337725/united-states-v-robert-michael-milroy/" aria-description="Citation for case: United States v. Robert Michael Milroy">538 F. 2d 1033</a></span> (CA4), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./426/924/">426 U. S. 924</a></span> (1976); <i>United States</i> v. <i>King,</i> <span class="citation" data-id="328030"><a href="/opinion/328030/united-states-v-edward-king-and-mose-franklin-pearson/" aria-description="Citation for case: United States v. Edward King and Mose Franklin Pearson">517 F. 2d 350</a></span> (CA5 1975); <i>United States</i> v. <i>Barclift,</i> <span class="citation" data-id="8896380"><a href="/opinion/8908839/united-states-v-barclift/" aria-description="Citation for case: United States v. Barclift">514 F. 2d 1073</a></span> (CA9), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./423/842/">423 U. S. 842</a></span> (1975); <i>United States</i> v. <i>Bolin,</i> <span class="citation" data-id="326933"><a href="/opinion/326933/united-states-v-robert-c-bolin-aka-bob-bolin/" aria-description="Citation for case: United States v. Robert C. Bolin, A/K/A Bob Bolin">514 F. 2d 554</a></span> (CA7 1975); <i>United States</i> v. <i>Odland,</i> <span class="citation" data-id="321210"><a href="/opinion/321210/united-states-v-david-john-odland/" aria-description="Citation for case: United States v. David John Odland">502 F. 2d 148</a></span> (CA7), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/1088/">419 U. S. 1088</a></span> (1974). Several other Courts of Appeals, in approving the warrantless opening of mailed packages crossing the borders, have indicated that the opening of international letter-class mail should be governed by the same standards. <i>United States</i> v. <i>Doe,</i> <span class="citation" data-id="307979"><a href="/opinion/307979/united-states-v-john-doe-aka-francisco-rodriquez-aka-juan-velez-s/" aria-description="Citation for case: United States v. John Doe, A/K/A Francisco Rodriquez,...">472 F. 2d 982</a></span> (CA2), cert. denied, <i>sub nom. Rodriguez</i> v. <i>United States,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./411/969/">411 U. S. 969</a></span> (1973); <i>United States</i> v. <i>Beckley,</i> <span class="citation" data-id="265141"><a href="/opinion/265141/united-states-v-john-e-beckley-united-states-of-america-v-anderson/" aria-description="Citation for case: United States v. John E. Beckley, United States of...">335 F. 2d 86</a></span> (CA6 1964), cert. denied, <i>sub nom. </i><i>Stone</i> v. <i>United States,</i> <span class="citation" data-id="8951845"><a href="/opinion/8960691/stone-v-united-states/" aria-description="Citation for case: Stone v. United States">380 U. S. 922</a></span> (1965). The First Circuit has reserved the question of letters. <i>United States</i> v. <i>Emery,</i> <span class="citation" data-id="339048"><a href="/opinion/339048/united-states-v-john-edward-emery/#888" aria-description="Citation for case: United States v. John Edward Emery">541 F. 2d 887, 888-889</a></span> (1976).</p>
<p>[2]  The mail was inspected at the General Post Office in New York City, where incoming international air mail landing at Kennedy Airport is taken for routing and customs inspections. There is no dispute that this is the "border" for purposes of border searches, see n. 11, <i>infra.</i></p>
<p>[3]  Inspector Kallnischkies also testified that his "normal procedure," when examining envelopes from certain countries which were of a certain weight and bulkiness, was to "shake it a little," and "if it moves, I know there is something in there that is not correspondence. It is merchandise and I have to open it to check it out." App. 48-49. He was unable to specifically recall, however, whether or not he had followed the "normal procedure" in this case.</p>
<p>[4]  The Government does not seek to justify the original discovery of the heroin on the basis of this warrant: "[A] post-opening warrant obviously does not justify the original opening." Brief for United States 4 n. 2. We accordingly accord no significance to the obtaining of this subsequent warrant.</p>
<p>[5]  Bailey and Ward, although indicted, were not tried, as they have remained outside the United States.</p>
<p>[6]  The Government acknowledges that "[t]he weapons were found as a result of respondents' arrests and so are `fruit' of the discovery of the heroin. The convictions consequently must stand or fall with the heroin offenses." <i><span class="citation" data-id="339048"><a href="/opinion/339048/united-states-v-john-edward-emery/" aria-description="Citation for case: United States v. John Edward Emery">Id.,</a></span></i> at 5 n. 4.</p>
<p>[7]  Neither court below considered whether Ramsey or Kelly had standing to object to the opening of the envelopes in light of the fact that none of the envelopes were addressed to them. The Government, however, did not raise the issue below, and consequently we do not reach it. <i>United States</i> v. <i>Santana,</i> <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">427 U. S. 38</a></span>, 41 n. 2 (1976).</p>
<p>[8]  Postal regulations have implemented this authority. See <span class="citation no-link">19 CFR § 145.2</span> (1976); <span class="citation no-link">39 CFR § 61.1</span> (1975). The regulations were promulgated in 1971; prior to that time existing regulations did not implement the statutory authority. The fact that postal authorities did not open incoming international letter-class mail upon "reasonable cause to suspect" prior to 1971 does not change our analysis.
</p>
<p>Title <span class="citation no-link">39 U. S. C. § 3623</span> (d), which prohibits the opening of first-class mail of "domestic origin," "except under authority of a search warrant authorized by law . . . ," has, by its own terms, no application to international mail of any class. A proposed amendment, which would have imposed similar statutory requirements on the opening of international mail, was defeated on the floor of the House, 116 Cong. Rec. 20482-20483 (1970).</p>
<p>Our dissenting Brethren find no fewer than five separate reasons for refusing to follow the unambiguous language of the statutory section. The first is the longstanding respect Congress has shown for "the individual's interest in private communication." <i>Post,</i> at 626. But as we examine it, <i>infra,</i> at 616-619, no such support may be garnered from the history of the Fourth Amendment insofar as border searches are concerned. Insofar as they rely on the First Amendment, they ignore the limitations imposed on the search by the statute, <i>infra,</i> at 623-624, as well as by the regulations. Postulating a sensitive concern for First Amendment values as of 1866 is a difficult historical exercise on the basis of available materials from that time. Cf. <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727</a></span> (1878) (Fourth Amendment analysis only). Most puzzling of all, however, is the dissent's reliance on the defeated amendment, offered in 1970, when there is no dearth of available materials, which would have imposed a specific warrant requirement on the opening of international letter-class mail. Contrary to the tenor of the dissent, the amendment was defeated, not passed. The one bit of legislative history the dissent quotes, a statement of Congressman Derwinski, reflects only the concern that with the amendment " `the problem of stopping the flow of narcotics and pornography would be greatly compounded.' " <i>Post,</i> at 626 n. 2. We do not see how any solace whatever for the dissenting position may be derived from this sort of legislative history.</p>
<p>The dissent also relies on a brief colloquy on the floor of the Senate during the debate on the 1866 Act. The colloquy is notable both for its brevity and for its ambiguity. It does not distinguish between mailed packages and mailed letters; it refers generally to the " `examination of . . . the United States mails.' " <i>Post,</i> at 627. Yet, by that time, the "mail" encompassed both. See <span class="citation no-link">12 Stat. 704</span>. (To the extent the colloquy was meant to encompass <i>any</i> intrusion on the "mails," the statute has long since been interpreted otherwise. <i>Cotzhausen</i> v. <i>Nazro,</i> <span class="citation" data-id="90759"><a href="/opinion/90759/cotzhausen-v-nazro/#219" aria-description="Citation for case: Cotzhausen v. Nazro">107 U. S. 215, 219</a></span> (1883).) Perhaps because of its brevity, the colloquy does not distinguish between domestic and international mail, nor does it distinguish between the searching of envelopes for contraband and the possible reading of enclosed communications. It explicitly manifests a concern with § 2 as well as with § 3 of the bill. But § 2 allowed customs inspectors "to go on board of any vessel . . . and to inspect, search, and examine the same, and any person, trunk, or envelope on board . . . ." Section 3, however, contains a "reasonable cause to suspect" requirement that is not found in § 2, and the colloquy may have simply referred to a concern about the wholesale opening, and reading, of letters. Cf. Cong. Globe 39th Cong., 1st Sess., 3440-3441 (1866). The colloquy by no means indicates to us that Congress was concerned only with detecting smuggling that would be carried in "trunk"-sized packages. It is at best insufficient to overcome the precise and clear statutory language Congress actually enacted.</p>
<p>The dissent additionally relies on the language of the statute in its entirety as demonstrating a concern only with "packages of the kind normally used to import dutiable merchandise." <i>Post,</i> at 628. But this assertionassuming we as judges know what size packages dutiable merchandise <i>usually</i> comes inis wholly contrary to the thrust of the purpose, and the language, of the Act. The purpose of the Act is "to Prevent Smuggling." Nowhere does this purpose, however and wherever articulated, reflect a concern with the physical size of the container employed in smuggling, nor do we possess any reliable indication that only large items were smuggled into this country in 1866. As for the word "envelope," it is difficult to see how our dissenting Brethren derive comfort from its use in the statute. The contemporary dictionary source they cite states that the most common use of the word "envelope" is in the sense of " `the cover or wrapper of a document, as of a letter.' " <i>Post,</i> at 630 n. 5. We are quite unable to see how this, the most common usage of the word, reinforces the view that Congress intended only a narrow definition when it used the word without restriction.</p>
<p>The dissent also relies on a "consistent construction" over 105 years by the Executive. <i>Post,</i> at 631. To the extent it relies on a construction that things entering by mail are not covered by the statute, this reliance founders on the opinion of a former Acting Attorney General. See 18 Op. Atty. Gen. 457 (1886). To the extent it is referring only to lettersized mail, the dissent nowhere demonstrates <i>any</i> actual interpretation by anyone that the congressional authority was perceived as an affirmative limitation on the power of the Executive to open letters at the border when there existed "reasonable cause" to suspect a violation of customs laws. The evidence marshaled by our dissenting Brethren on this point could be called "consistent" only by the most generous appraiser of such material.</p>
<p>The dissent's final reliance is on the assertion that asking the addressee for consent to open a letter had not been proved unworkable. Presumably the conclusion to be drawn from this is that the Executive's reason for a change in its policy is weak. But this is beside the point; it reflects not at all on Congress' words or intent in 1866 or at any other time. That the Executive Branch may have relied on a less-than-cogent reason in its 1971 regulatory change has nothing to do with the interpretation of an Act of Congress.</p>
<p>Underlying all of these reasons, apparently, is the fear that "[i]f the Government is allowed to exercise the power it claims, the door will be open to the wholesale, secret examination of all incoming international letter mail." <i>Post,</i> at 632. That specter is simply not presented by this case. As we observe, <i>infra,</i> at 623-624, the opening of mail is limited by a "reasonable cause" requirement, while the reading of letters is totally interdicted by regulation. It is this unwarranted speculation, and not the policy followed by the Executive, that poses the "serious constitutional question" to be avoided.</p>
<p>[9]  The Court of Appeals, it should be noted, evidently believed that Inspector Kallnischkies possessed sufficient information at the time the envelopes were opened to meet the stricter "probable cause" requirement; it believed "that the facts in this case are such that, had they been presented to a magistrate, issuance of a search warrant permitting opening of the envelopes would have been appropriate." 176 U. S. App. D. C. 67, 73 n. 8, <span class="citation" data-id="9462874"><a href="/opinion/337566/united-states-v-charles-w-ramsey-united-states-of-america-v-james-w/" aria-description="Citation for case: United States v. Charles W. Ramsey, United States of...">538 F. 2d 415</a></span>, 421 n. 8. Because of our disposition of this case, we do not reach that question.</p>
<p>[10]  In light of our conclusion that there existed "reasonable cause to suspect" a violation of the customs laws, we need not, and do not, decide whether the search would have nonetheless been authorized by other statutory grants of authority urged alternatively upon us by the Government. Title <span class="citation no-link">19 U. S. C. § 482</span> also authorizes customs officials to "stop, search, and examine . . . any vehicle, beast, or person, on which or whom . . . they shall suspect there is merchandise which is subject to duty, or shall have been introduced into the United States in any manner contrary to law, whether by the person in possession or charge, or by, in, or upon such vehicle or beast, or otherwise . . . ." Title <span class="citation no-link">19 U. S. C. § 1582</span> provides, in pertinent part, that "[t]he Secretary of the Treasury may prescribe regulations for the search of persons and baggage . . . ; and all persons coming into the United States from foreign countries shall be liable to detention and search by authorized officers or agents of the Government under such regulations."</p>
<p>[11]  Although the statutory authority authorizes searches of envelopes "wherever found," <span class="citation no-link">19 U. S. C. § 482</span>, the envelopes were searched at the New York City Post Office as the mail was entering the United States. We, therefore, do not have before us the question, recently addressed in other contexts, of the geographical limits to border searches. See <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975); <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973). Nor do we need to decide whether the broad statutory authority subjects such mail to customs inspection at a place other than the point of entry into this country. See <i>United States</i> v. <i>King,</i> <span class="citation" data-id="328030"><a href="/opinion/328030/united-states-v-edward-king-and-mose-franklin-pearson/#354" aria-description="Citation for case: United States v. Edward King and Mose Franklin Pearson">517 F. 2d, at 354</a></span> ("[T]he envelopes had passed an initial stage in the customs process when they were routed to Alabama, but they were still in the process of being delivered, and still subject to customs inspection").</p>
<p>[12]  Section 23 of this customs statute provided, in pertinent part:
</p>
<p>"[I]t shall be lawful for the collector, or other officer of the customs, after entry made of any goods, wares or merchandise, on suspicion of fraud, to open and examine, in the presence of two or more reputable merchants, any package or packages thereof . . . ."</p>
<p>Section 24 of this customs statute provided, in pertinent part:</p>
<p>"[E]very collector, naval officer and surveyor, or other person specially appointed by either of them for that purpose, shall have full power and authority, to enter any ship or vessel, in which they shall have reason to suspect any goods, wares or merchandise subject to duty shall be concealed; and therein to search for, seize, and secure any such goods, wares or merchandise; and if they shall have cause to suspect a concealment thereof, in any particular dwelling-house, store, building, or other place, they or either of them shall, upon application on oath or affirmation to any justice of the peace, be entitled to a warrant to enter such house, store, or other place (in the day time only) and there to search for such goods, and if any shall be found, to seize and secure the same for trial . . . ."</p>
<p>[13]  We do not decide whether, and under what circumstances, a border search might be deemed "unreasonable" because of the particularly offensive manner in which it is carried out. Cf. <i>Kremen</i> v. <i>United States,</i> <span class="citation" data-id="8931353"><a href="/opinion/8940894/kremen-v-united-states/" aria-description="Citation for case: Kremen v. United States">353 U. S. 346</a></span> (1957); <i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#356" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 356-358</a></span> (1931)</p>
<p>[14]  The opinion in <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 149</a></span> (1925), itself reminds us that "[t]he Fourth Amendment is to be construed in the light of what was deemed an unreasonable search and seizure when it was adopted, and in a manner which will conserve public interests as well as the interests and rights of individual citizens."</p>
<p>[15]  This explanation does not, and cannot, fully explain the border-search "exception" even if it were grounded in the "exigent circumstances" doctrine. For a letter may as easily be held by customs officials when it crosses with a traveler as it can when it crosses in the mail. Too, this explanation cannot explain the different treatment which the Court of Appeals apparently would have accorded mailed packages, which presumably may be detained as easily as letter-size envelopes.</p>
<p>[16]  There is no reason to infer that mailed letters somehow carry with them a greater expectation of privacy than do letters carried on one's person. Cf. <span class="citation no-link">39 U. S. C. § 3623</span> (d).</p>
<p>[17]  There are limited justifiable expectations of privacy for incoming material crossing United States borders. Not only is there the longstanding, constitutionally authorized right of customs officials to search incoming persons and goods, but there is no statutorily created expectation of privacy. See <span class="citation no-link">39 U. S. C. § 3623</span> (d). See also <i>United States</i> v. <i>King,</i> <span class="citation" data-id="328030"><a href="/opinion/328030/united-states-v-edward-king-and-mose-franklin-pearson/#354" aria-description="Citation for case: United States v. Edward King and Mose Franklin Pearson">517 F. 2d, at 354</a></span>; <i>United States</i> v. <i>Odland,</i> <span class="citation" data-id="321210"><a href="/opinion/321210/united-states-v-david-john-odland/" aria-description="Citation for case: United States v. David John Odland">502 F. 2d 148</a></span> (CA7), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/1088/">419 U. S. 1088</a></span> (1974); <i>United States</i> v. <i>Doe,</i> <span class="citation" data-id="307979"><a href="/opinion/307979/united-states-v-john-doe-aka-francisco-rodriquez-aka-juan-velez-s/#985" aria-description="Citation for case: United States v. John Doe, A/K/A Francisco Rodriquez,...">472 F. 2d, at 985</a></span>.</p>
<p>[18]  We, accordingly, have no occasion to decide whether, in the absence of the regulatory restrictions, speech would be "chilled," or, if it were, whether the appropriate response would be to apply the full panoply of Fourth Amendment requirements. Cf. <i>Roaden</i> v. <i>Kentucky,</i> <span class="citation" data-id="9425416"><a href="/opinion/108854/roaden-v-kentucky/#502" aria-description="Citation for case: Roaden v. Kentucky">413 U. S. 496, 502-506</a></span> (1973); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19</a></span> (1968); <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 485</a></span> (1965).</p>
<p>[19]  In <i>Wolff</i> v. <i>McDonnell,</i> <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/" aria-description="Citation for case: Wolff v. McDonnell">418 U. S. 539</a></span> (1974), this Court, in the context of the opening of mail from an attorney to a prisoner-client, noted that "freedom from censorship is not equivalent to freedom from inspection or perusal," <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#576" aria-description="Citation for case: Wolff v. McDonnell"><i>id.,</i> at 576</a></span>. This Court held:
</p>
<p>"As to the ability to open the mail in the presence of inmates, this could in no way constitute censorship, since the mail would not be read. Neither could it chill such communications, since the inmate's presence insures that prison officials will not read the mail. The possibility that contraband will be enclosed in letters, even those from apparent attorneys, surely warrants prison officials' opening the letters." <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#577" aria-description="Citation for case: Wolff v. McDonnell"><i>Id.,</i> at 577</a></span>.</p>
<p>We deal here, of course, with borders, not prisons. Yet the power of customs officials to take plenary action to stop the entry of contraband is no less in the border-search area than in prisons. The safeguards in the border-search area, we think, are comparable to those found constitutionally valid in <i><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/" aria-description="Citation for case: Wolff v. McDonnell">Wolff</a></span>.</i></p>
<p>[*]  As the Court notes, <i>ante,</i> at 623, postal regulations flatly prohibit the reading of "any correspondence contained in sealed letter mail of foreign origin unless a search warrant has been obtained . . . ." <span class="citation no-link">19 CFR § 145.3</span> (1976).</p>
<p>[1]  This was the procedure followed by the customs officials in <i>Cotzhausen</i> v. <i>Nazro,</i> <span class="citation" data-id="90759"><a href="/opinion/90759/cotzhausen-v-nazro/" aria-description="Citation for case: Cotzhausen v. Nazro">107 U. S. 215</a></span>, relied upon by the Government here. For 100 years, from 1871 to 1971, Post Office Regulations allowed incoming international letter mail to be opened only in the presence, and with the consent, of the addressee. Brief for United States 20-21, nn. 12a, 14 (citing regulations).</p>
<p>[2]  This conviction is bolstered by the history of the defeat of the amendment which would have imposed a specific warrant requirement on the opening of international mails, <i>ante,</i> at 612 n. 8. The amendment was offered during the course of House debate on the Postal Reorganization and Salary Adjustment Act of 1970, Title 39 U. S. C., which created the United States Postal Service. This amendment was but one of more than 35 amendments to the Act offered on the floor of the House that day. 116 Cong. Rec. 20481 (1970). Speaking immediately before the amendment was defeated, Congressman Derwinski said:
</p>
<p>"Going beyond the constitutional debate which we do not have the time for this afternoon, if this amendment were to be adopted, the problem of stopping the flow of narcotics and pornography would be greatly compounded.</p>
<p>"I do not believe we want to legislate on such a major issue with just 10 minutes of debate." <i>Id.,</i> at 20483.</p>
<p>Under such circumstances the defeat of this amendment cannot be considered an expression of the will of the House of Representatives on the issue, but it does emphasize the reluctance of Congress to legislate in the area without careful consideration of the constitutional questions. See, <i>e. g.,</i> <span class="citation no-link">18 U. S. C. § 2510</span> (Omnibus Crime Control and Safe Streets Act of 1968) (warrant required to electronically intercept wire or oral communications); S. Rep. No. 1097, 90th Cong., 2d Sess., 66-76, 88-108, 161-177, 182-183, 187, 214-218, 224-226, 234-239 (1968). I do not, of course, imply that this incident is, in itself, sufficient to demonstrate congressional sensitivity to the individual interest in private communication. See <i>ante,</i> at 612 n. 8. I cannot believe, however, that the Court seriously questions the validity of my assumption that Congress (in 1866 as well as today) was indeed concerned about such matters.</p>
<p>[3]  Cong. Globe, 39th Cong., 1st Sess., 2596 (1866). After consideration of one more amendment the bill passed the Senate the same day.</p>
<p>[4]  The first three sections of the Act, Further to Prevent Smuggling and for Other Purposes, enacted on July 18, 1866, read as follows:
</p>
<p>"<i>Be it enacted by the Senate and House of Representatives of the United States of America in Congress assembled,</i> That, for the purposes of this act, the term `vessel,' whenever hereinafter used, shall be held to include every description of water-craft, raft, vehicle, and contrivance used or capable of being used as a means or auxiliary of transportation on or by water; and the term `vehicle,' whenever hereinafter used, shall be held to include every description of carriage, wagon, engine, car, sleigh, sled, sledge, hurdle, cart, and other artificial contrivance, used or capable of being used as a means or auxiliary of transportation on land.</p>
<p>"SEC. 2. <i>And be it further enacted,</i> That it shall be lawful for any officer of the customs, including inspectors and occasional inspectors, or of a revenue cutter, or authorized agent of the Treasury Department, or other person specially appointed for the purpose in writing by a collector, naval officer, or surveyor of the customs, to go on board of any vessel, as well without as within his district, and to inspect, search, and examine the same, and any person, trunk, or envelope on board, and to this end, to hail and stop such vessel if under way, and to use all necessary force to compel compliance; and if it shall appear that any breach or violation of the laws of the United States has been committed, whereby or in consequence of which, such vessel, or the goods, wares, and merchandise, or any part thereof, on board of or imported by such vessel, is or are liable to forfeiture, to make seizure of the same, or either or any part thereof, and to arrest, or in case of escape, or any attempt to escape, to pursue and arrest any person engaged in such breach or violation: <i>Provided,</i> That the original appointment in writing of any person specially appointed as aforesaid shall be filed in the custom-house where such appointment is made.</p>
<p>"SEC. 3. <i>And be it further enacted,</i> That any of the officers or persons authorized by the second section of this act to board or search vessels may stop, search, and examine, as well without as within their respective districts, any vehicle, beast, or person on which or whom he or they shall suspect there are goods, wares, or merchandise which are subject to duty or shall have been introduced into the United States in any manner contrary to law, whether by the person in possession or charge, or by, in, or upon such vehicle or beast, or otherwise, and to search any trunk or envelope, wherever found, in which he may have a reasonable cause to suspect there are goods which were imported contrary to law; and if any such officer or other person so authorized as aforesaid shall find any goods, wares, or merchandise, on or about any such vehicle, beast, or person, or in any such trunk or envelope, which he shall have reasonable cause to believe are subject to duty, or to have been unlawfully introduced into the United States, whether by the person in possession or charge, or by, in, or upon such vehicle, beast, or otherwise, he shall seize and secure the same for trial; and every such vehicle and beast, or either, together with teams or other motive-power used in conveying, drawing, or propelling such vehicle, goods, wares, or merchandise, and all other appurtenances, including trunks, envelopes, covers, and all means of concealment, and all the equipage, trappings, and other appurtenances of such beast, team, or vehicle shall be subject to seizure and forfeiture; and if any person who may be driving or conducting, or in charge of any such carriage or vehicle or beast, or any person travelling, shall wilfully refuse to stop and allow search and examination to be made as herein provided, when required so to do by any authorized person, he or she shall, on conviction, be fined in any sum, in the discretion of the court convicting him or her, not exceeding one thousand dollars, nor less than fifty dollars; and the Secretary of the Treasury may from time to time prescribe regulations for the search of persons and baggage, and for the employment of female inspectors for the examination and search of persons of their own sex; and all persons coming into the United States from foreign countries shall be liable to detention and search by authorized officers or agents of the government, under such regulations as the Secretary of the Treasury shall from time to time prescribe: <i>Provided,</i> That no railway car or engine or other vehicle, or team used by any person or corporation, as common carriers in the transaction of their business as such common carriers shall be subject to forfeiture by force of the provisions of this act unless it shall appear that the owners, superintendent, or agent of the owner in charge thereof at the time of such unlawful importation or transportation thereon or thereby, was a consenting party, or privy to such illegal importation or transportation." <span class="citation no-link">14 Stat. 178</span>-179.</p>
<p>[5]  "A wrapper; an outward covering or case." J. Worcester, A Dictionary of the English Language (1860).
</p>
<p>"That which envelops, wraps up, encases, or surrounds; a wrapper; a cover; especially, the cover or wrapper of a document, as of a letter." N. Webster, An American Dictionary of the English Language (Goodrich &amp; Porter eds. 1869).</p>
<p>These are the primary definitions given for "envelope."</p>
<p>[6]  The word "other was deleted by amendment, Cong. Globe, 39th Cong., 1st Sess., 2564 (1866). I recognize that one may argue that the deletion of the word "other" is evidence of an intent to include every kind of envelope rather than just those comparable to a "trunk." It seems more reasonable to infer, however, that the draftsmen considered the direct comparison to a trunk too restrictive and merely had in mind all containers which performed the same kind of packaging function even though not as large as a trunk. It seems unrealistic to interpret this change as intended to broaden the statute to encompass personal mail.</p>
<p>[7]  The stated object of the 1866 Act was to prevent smuggling, especially from Canada along the North and Northwestern frontier:
</p>
<p>"It has been found very difficult on our frontier during the last two years to prevent the system of smuggling which has been going on and increasing day by day. The custom-houses are defrauded and the Government is cheated." Remarks of Congressman Eliot, Cong. Globe, 39th Cong., 1st Sess., 3419 (1866).</p>
<p>See also remarks of Senator Morrill, <span class="citation no-link"><i>id.,</i> at 2563</span>; of Senator Williams, <span class="citation no-link"><i>id.,</i> at 2567</span>.</p>
<p>[8]  An 1886 opinion of Acting Attorney General Jenks made reference to the practice followed in <i>Cotzhausen</i> v. <i>Nazro,</i> <span class="citation" data-id="90759"><a href="/opinion/90759/cotzhausen-v-nazro/" aria-description="Citation for case: Cotzhausen v. Nazro">107 U. S. 215</a></span>, a case which involved the opening of package mail with the consent, and in the presence, of the addressee. See 18 Op. Atty. Gen. 457, 458. No opinion of any subsequent Attorney General has construed the statute any more broadly.</p>
<p>[9]  In support of its argument in this Court that the 1971 regulations are reasonable within the meaning of the Fourth Amendment, the Government has assembled a plethora of statistical data obtained after the regulations were adopted. Such a <i>post hoc</i> justification cannot, of course, inform us about the actual motivation for the adoption of the regulations. I mention the point only because the Government's reliance on these data tends to confirm my judgment that if a new rule is to be fashioned, it should be drafted by the Congress.</p>

</div>
```

---

## GROUP: content/cases/United States v. Robinson.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Robinson"
type: case
citation: "414 U.S. 218 (1973)"
parallel_cite: "94 S. Ct. 467; 38 L. Ed. 2d 427; 66 Ohio Op. 2d 202"
neutral_cite: 1973 U.S. LEXIS 21
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1973
date_decided: 1973-12-11
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1973-12-11
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Robinson
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108893/united-states-v-robinson/"
  cluster_id: 108893
  opinion_id: 9425474
  identity_checked: true
homes:
  - page: "[[SIA Persons]]"
    role: "Key — Anchor"
related: ["[[Chimel v. California]]", "[[Arizona v. Gant]]", "[[Riley v. California]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "full-custody-arrest", "bright-line-rule"]
holding: "A lawful custodial arrest categorically authorizes a full search of the arrestee's person; the search needs no additional justification…"
lake:
  record_id: United States v. Robinson
  status: verified
  projected_at: 2026-07-06
---

# United States v. Robinson

*414 U.S. 218 (1973)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An officer lawfully arrested Robinson on a full-custody basis for operating a motor vehicle after revocation of his driver's license. Searching Robinson incident to the arrest, the officer felt an object in Robinson's coat pocket, removed a crumpled cigarette package, opened it, and found heroin capsules. Robinson moved to suppress, arguing the search went beyond what was needed to protect the officer or to preserve evidence of the license offense.

## Issue
Whether, incident to a lawful custodial arrest, an officer may conduct a full search of the arrestee's person without additional justification — even with no particular reason to believe the search will produce weapons or evidence of the crime of arrest.

## Rule
Yes. "A custodial arrest of a suspect based on probable cause is a reasonable intrusion under the Fourth Amendment; that intrusion being lawful, a search incident to the arrest requires no additional justification. It is the fact of the lawful arrest which establishes the authority to search, and we hold that in the case of a lawful custodial arrest a full search of the person is not only an exception to the warrant requirement of the Fourth Amendment, but is also a 'reasonable' search under that Amendment." — 414 U.S. at 235. ^pin-235

The authority to search the person is automatic upon a lawful custodial arrest; it does not depend on a case-by-case judgment that weapons or evidence would in fact be found in the particular situation.

## Application
The officer made a lawful full-custody arrest of Robinson for driving after revocation of his license. Searching him incident to that arrest, the officer found a crumpled cigarette package, opened it, and discovered heroin. Because the arrest was lawful and custodial, the full search of Robinson's person — including opening the cigarette package — required no further justification and was reasonable; that the search was unlikely to yield weapons or evidence of the license offense was immaterial.

## Conclusion
The search of Robinson's person and the seizure of the heroin were valid as incident to a lawful custodial arrest; the Supreme Court reversed the Court of Appeals.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Robinson* states the [[Common Legal Terms#bright-line-rule|bright-line rule]] for searches of the person incident to a custodial arrest. [[Riley v. California]] later declined to extend that automatic-search authority to the **digital contents of a cell phone** (those require a warrant), and [[Arizona v. Gant]] cabined vehicle [[Search Incident to Arrest|searches incident to arrest]] — but neither disturbs *Robinson*'s rule for a full search of the arrestee's person and physical effects.

## Appears on
- [[SIA Persons]] — *Key — Anchor*

## Sources
- *United States v. Robinson*, 414 U.S. 218 (1973) — https://www.courtlistener.com/opinion/108893/united-states-v-robinson/ — pinpoint: 235 (parallel 94 S. Ct. 467).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3276cb9afb8573d9", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "414 U.S. 218 (1973)", "court": "U.S. Supreme Court", "neutral_cite": "1973 U.S. LEXIS 21", "official_citation_present": true, "parallel_cite": "94 S. Ct. 467; 38 L. Ed. 2d 427; 66 Ohio Op. 2d 202", "title": "United States v. Robinson", "year": "1973"}}
{"assertion_id": "b2aaab7db7b782c0", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Persons"}, "payload": {"home": "SIA Persons", "role": "Key — Anchor", "title": "United States v. Robinson"}}
{"assertion_id": "f252d27dc2ce8408", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A lawful custodial arrest categorically authorizes a full search of the arrestee's person; the search needs no additional justification…", "title": "United States v. Robinson"}}
{"assertion_id": "6317a11559790392", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Robinson"}}
{"assertion_id": "682c8f62708eb3e5", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1973-12-11", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Robinson", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Robinson", "varies_by_point": "false"}}
```

### lake record — United States v. Robinson

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Robinson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Robinson",
    "case_name_short": "Robinson",
    "case_name_full": "United States v. Robinson",
    "input_case_name": "United States v. Robinson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1973-12-11",
    "year": 1973,
    "docket": null,
    "cluster_id": 108893,
    "lead_opinion_id": 9425474,
    "sibling_ids": [
      108893,
      9425474,
      9425475,
      9425476
    ],
    "absolute_url": "/opinion/108893/united-states-v-robinson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "414 U.S. 218",
      "volume": "414",
      "reporter": "U.S.",
      "page": "218",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "94 S. Ct. 467",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "467",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "38 L. Ed. 2d 427",
        "volume": "38",
        "reporter": "L. Ed. 2d",
        "page": "427",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "66 Ohio Op. 2d 202",
        "volume": "66",
        "reporter": "Ohio Op. 2d",
        "page": "202",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1973 U.S. LEXIS 21",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "21",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "414 U.S. 218",
        "volume": "414",
        "reporter": "U.S.",
        "page": "218",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 S. Ct. 467",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "467",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "38 L. Ed. 2d 427",
        "volume": "38",
        "reporter": "L. Ed. 2d",
        "page": "427",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. LEXIS 21",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "21",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "66 Ohio Op. 2d 202",
        "volume": "66",
        "reporter": "Ohio Op. 2d",
        "page": "202",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "414 U.S. 218",
    "official_selection": {
      "court_class": "scotus",
      "selected": "414 U.S. 218",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-235",
      "page": null,
      "quote": "--- # United States v. Robinson *414 U.S. 218 (1973)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An officer lawfully arrested Robinson on a full-custody basis for operating a motor vehicle after revocation of his driver's license. Searching Robinson incident to the arrest, the officer felt an object in Robinson's coat pocket, removed a crumpled cigarette package, opened it, and found heroin capsules. Robinson moved to suppress, arguing the search went beyond what was needed to protect the officer or to preserve evidence of the license offense. ## Issue Whether, incident to a lawful custodial arrest, an officer may conduct a full search of the arrestee's person without additional justification \u2014 even with no particular reason to believe the search will produce weapons or evidence of the crime of arrest. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1973-12-11",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Robinson",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Garrett",
          "cluster_id": 4552162,
          "cite": [
            "2018 Ohio 4530",
            "123 N.E.3d 327"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Indiana v. Justin Crager",
          "cluster_id": 4547157,
          "cite": [
            "113 N.E.3d 657"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brandon Pegg v. Grant Herrnberger",
          "cluster_id": 4335908,
          "cite": [
            "845 F.3d 112",
            "2017 WL 35722",
            "2017 U.S. App. LEXIS 109"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Ryan Mark Thompson",
          "cluster_id": 4311783,
          "cite": [
            "886 N.W.2d 224",
            "2016 Minn. LEXIS 656"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tony Williams",
          "cluster_id": 4257975,
          "cite": [
            "837 F.3d 1016",
            "2016 U.S. App. LEXIS 17150",
            "2016 WL 5030343"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane1_negative"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Gant",
          "cluster_id": 145887,
          "cite": [
            "173 L. Ed. 2d 485",
            "129 S. Ct. 1710",
            "556 U.S. 332",
            "2009 U.S. LEXIS 3120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chadwick",
          "cluster_id": 109714,
          "cite": [
            "53 L. Ed. 2d 538",
            "97 S. Ct. 2476",
            "433 U.S. 1",
            "1977 U.S. LEXIS 133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. DeFillippo",
          "cluster_id": 110127,
          "cite": [
            "61 L. Ed. 2d 343",
            "99 S. Ct. 2627",
            "443 U.S. 31",
            "1979 U.S. LEXIS 135"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. United States",
          "cluster_id": 109860,
          "cite": [
            "56 L. Ed. 2d 168",
            "98 S. Ct. 1717",
            "436 U.S. 128",
            "1978 U.S. LEXIS 89"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Santana",
          "cluster_id": 109504,
          "cite": [
            "49 L. Ed. 2d 300",
            "96 S. Ct. 2406",
            "427 U.S. 38",
            "1976 U.S. LEXIS 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108893 OR 9425474 OR 9425475 OR 9425476) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDUyNTU2ODAwMDAwJnM9MzE2ODkyOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108893+OR+9425474+OR+9425475+OR+9425476%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 5,
        "triage_snippet_classified": 195
      },
      "lane2_top_cited": {
        "query": "cites:(108893 OR 9425474 OR 9425475 OR 9425476)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00ODAmcz02MDY2ODkmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28108893+OR+9425474+OR+9425475+OR+9425476%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108893 OR 9425474 OR 9425475 OR 9425476)",
        "reviewed": 56,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 56,
        "triage_read": 0,
        "triage_snippet_classified": 56
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108893 OR 9425474 OR 9425475 OR 9425476)",
    "indexed_citing_opinions": 2137,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108893,
        "count": 1919,
        "count_source": "search"
      },
      {
        "opinion_id": 9425474,
        "count": 268,
        "count_source": "search"
      },
      {
        "opinion_id": 9425475,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425476,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3541,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-robinson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxMDIwMjQmcz0xMDI4NjMwNiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28108893+OR+9425474+OR+9425475+OR+9425476%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108893,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 250962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 279289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 284470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 298864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 307722,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 308053,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 1141467,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 1170737,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 1211726,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 1604308,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 1821304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 1922425,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 1992458,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 3579530,
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
    "date_created": "2026-07-06T02:32:43Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:33:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:33:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:35:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:33:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Robinson

```
<opinion type="majority">
<author id="b371-10">Mr. Justice Rehnquist</author>
<p id="Aif">delivered the opinion of the Court.</p>
<p id="b371-12">Respondent Robinson was convicted in United States District Court for the District of Columbia of the possession and facilitation of concealment of heroin in violation of <span class="citation no-link">26 U. S. C. § 4704</span> (a) (1964 ed.), and <span class="citation no-link">21 U. S. C. § 174</span> (1964 ed.). He was sentenced to concurrent terms of imprisonment for these offenses. On his appeal to the Court of Appeals for the District of Columbia Cir<page-number citation-index="1" label="220">*220</page-number>cuit, that court first remanded the case to the District Court for an evidentiary hearing concerning the scope of the search of respondent’s person which had occurred at the time of his arrest. 145 U. S. App. D. C. 46, <span class="citation" data-id="9457297"><a href="/opinion/298864/united-states-v-willie-robinson-jr/" aria-description="Citation for case: United States v. Willie Robinson, Jr.">447 F. 2d 1215</a></span> (1971). The District Court made findings of fact and conclusions of law adverse to respondent, and he again appealed. This time the Court of Appeals en banc reversed the judgment of conviction, holding that the heroin introduced in evidence against respondent had been obtained as a result of a search which violated the Fourth Amendment to the United States Constitution. 153 U. S. App. D. C. 114, <span class="citation" data-id="9459062"><a href="/opinion/307722/united-states-v-willie-robinson-jr/" aria-description="Citation for case: United States v. Willie Robinson, Jr.">471 F. 2d 1082</a></span> (1972). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./410/982/">410 U. S. 982</a></span> (1973), and set the case for argument together with <em>Gustafson </em>v. <em>Florida, </em>No. 71-1669, <em>post, </em>p. 260, also decided today.</p>
<p id="b372-5">On April 23, 1968, at approximately 11 p. m., Officer Richard Jenks, a 15-year veteran of the District of Columbia Metropolitan Police Department, observed the respondent driving a 1965 Cadillac near the intersection of 8th and C Streets, N. E., in the District of Columbia. Jenks, as a result of previous investigation following a check of respondent’s operator’s permit four days earlier, determined there was reason to believe that respondent was operating a motor vehicle after the revocation of his operator’s permit. This is an offense defined by statute in the District of Columbia which carries a mandatory minimum jail term, a mandatory minimum fine, or both. D. C. Code Ann. § 40-302 (d) (1967).</p>
<p id="b372-6">Jenks signaled respondent to stop the automobile, which respondent did, and all three of the occupants emerged from the car. At that point Jenks informed respondent that he was under arrest for “operating after revocation and obtaining a permit by misrepresentation.” It was assumed by the Court of Appeals, and is conceded by the respondent here, that Jenks had <page-number citation-index="1" label="221">*221</page-number>probable cause to arrest respondent, and that he effected a full-custody arrest.<footnotemark>1</footnotemark></p>
<p id="b373-5">In accordance with procedures prescribed in police department instructions,<footnotemark>2</footnotemark> Jenks then began to search <page-number citation-index="1" label="222">*222</page-number>respondent. He explained at a subsequent hearing that he was “face-to-face” with the respondent, and “placed [his] hands on [the respondent], my right-hand to his <page-number citation-index="1" label="223">*223</page-number>left breast like this (demonstrating) and proceeded to pat him down thus [with the right hand].” During this patdown, Jenks felt an object in the left breast pocket of the heavy coat respondent was wearing, but testified that he “couldn't tell what it was” and also that he “couldn’t actually tell the size of it.” Jenks then reached into the pocket and pulled out the object, which turned out to be a “crumpled up cigarette package.” Jenks testified that at this point he still did not know what was in the package:</p>
<blockquote id="b375-5">“As I felt the package I could feel objects in the package but I couldn’t tell what they were. ... I knew they weren’t cigarettes.”</blockquote>
<p id="b375-6">The officer then opened the cigarette pack and found 14 gelatin capsules of white powder which .he thought to be, and which later analysis proved to be, heroin. Jenks then continued his search of respondent to completion, feeling around his waist and trouser legs, and examining the remaining pockets. The heroin seized from the respondent was admitted into evidence at the trial which resulted in his conviction in the District Court.</p>
<p id="b375-7">The opinion for the plurality judges of the Court of Appeals, written by Judge Wright, the concurring opinion of Chief Judge Bazelon, and the dissenting opinion of Judge Wilkey, concurred in by three judges, gave careful and comprehensive treatment to the authority of a police officer to search the person of one <page-number citation-index="1" label="224">*224</page-number>who has been validly arrested and taken into custody. We conclude that the search conducted by Jenks in this case did not offend the limits imposed by the Fourth Amendment, and we therefore reverse the judgment of the Court of Appeals.</p>
<p id="b376-5">I</p>
<p id="b376-6">It is well settled that a search incident to a lawful arrest is a traditional exception to the warrant requirement of the Fourth Amendment. This general exception has historically been formulated into two distinct propositions. The first is that a search may be made of the <em>person </em>of the arrestee by virtue of the lawful arrest. The second is that a search may be made of the area within the control of the arrestee.</p>
<p id="b376-7">Examination of this Court’s decisions shows that these two propositions have been treated quite differently. The validity of the search of a person incident to a lawful arrest has been regarded as settled from its first enunciation, and has remained virtually unchallenged until the present case. The validity of the second proposition, while likewise conceded in principle, has been subject to differing interpretations as to the extent of the area which may be searched.</p>
<p id="b376-8">Because the rule requiring exclusion of evidence obtained in violation of the Fourth Amendment was first enunciated in <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), it is understandable that virtually all of this Court’s search-and-seizure law has been developed since that time. In <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>, </em>the Court made clear its recognition of the validity of a search incident to a lawful arrest:</p>
<blockquote id="b376-9">“What then is the present case? Before answering that inquiry specifically, it may be well by a process of exclusion to state what it is not. It is not an assertion of the right on the part of the <page-number citation-index="1" label="225">*225</page-number>Government, always recognized under English and American law, to search the person of the accused when legally arrested to discover and seize the fruits or evidences of crime. This right has been uniformly maintained in many cases. 1 Bishop on Criminal Procedure, §211; Wharton, Crim. Plead, and Practice, 8th ed., § 60; <em>Dillon </em>v. <em>O’Brien and Davis, </em>16 Cox C. C. 245.” <em>Id., </em>at 392.</blockquote>
<p id="b377-5"><em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span> (1925), decided 11 years after <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>, </em>repeats the categorical recognition of the validity of a search incident to lawful arrest:</p>
<blockquote id="b377-6">“The right without a search warrant contemporaneously to search persons lawfully arrested while committing crime and to search the place where the arrest is made in order to find and seize things connected with the crime as its fruits or as the means by which it was committed, as well as weapons and other things to effect an escape from custody, is not to be doubted.” <em>Id., </em>at 30.</blockquote>
<p id="b377-7">Throughout the series of cases in which the Court has addressed the second proposition relating to a search incident to a lawful arrest — the permissible area beyond the person of the arrestee which such a search may cover — no doubt has been expressed as to the unqualified authority of the arresting authority to search the person of the arrestee. <em>E. g., Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925); <em>Marron </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span> (1927); <em>Go-Bart Co. </em>v. <em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span> (1931); <em>United States </em>v. <em>Lefkowitz, </em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452</a></span> (1932); <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span> (1947); <em>Trupiano </em>v. <em>United States, </em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span> (1948); <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span> (1950); <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span> (1964); <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969). In <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>, </em>where the Court overruled <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>and <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>as to the area <page-number citation-index="1" label="226">*226</page-number>of permissible search incident to a lawful arrest, full recognition was again given to the authority to search the person of the arrestee:</p>
<blockquote id="b378-5">“When an arrest is made, it is reasonable for the arresting officer to search the person arrested in order to remove any weapons that the latter might seek to use in order to resist arrest or effect his escape. Otherwise, the officer's safety might well be endangered, and the arrest itself frustrated. In addition, it is entirely reasonable for the arresting officer to search for and seize any evidence on the arrestee’s person in order to prevent its concealment or destruction.” <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California">395 U. S., at 762-763</a></span>.</blockquote>
<p id="b378-6">Three years after the decision in <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel, supra,</a></span> </em>we upheld the validity of a search in which heroin had been taken from the person of the defendant after his arrest on a weapons charge, in <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span> (1972), saying:</p>
<blockquote id="b378-7">“Under the circumstances surrounding Williams’ possession of the gun seized by Sgt. Connolly, the arrest on the weapons charge was supported by probable cause, and the search of his person and of the car incident to that arrest was lawful.” <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#149" aria-description="Citation for case: Adams v. Williams"><em>Id., </em>at 149</a></span>.</blockquote>
<p id="b378-8">Last Term in <em>Cupp </em>v. <em>Murphy, </em><span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#295" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291, 295</a></span> (1973), we again reaffirmed the traditional statement of the authority to search incident to a valid arrest.</p>
<p id="b378-9">Thus the broadly stated rule, and the reasons for it, have been repeatedly affirmed in the decisions of this Court since <em>Weeks </em>v. <em>United States, supra, </em>nearly 60 years ago. Since the statements in the cases speak not simply in terms of an exception to the warrant requirement, but in terms of an affirmative authority to search, they clearly imply that such searches also meet the Fourth Amendment’s requirement of reasonableness.</p>
<p id="b379-4"><page-number citation-index="1" label="227">*227</page-number>II</p>
<p id="b379-5">In its decision of this case, the Court of Appeals decided that even after a police officer lawfully places a suspect under arrest for the purpose of taking him into custody, he may not ordinarily proceed to fully search the prisoner. He must, instead, conduct a limited frisk of the outer clothing and remove such weapons that he may, as a result of that limited frisk, reasonably believe and ascertain that the suspect has in his possession. While recognizing that <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), dealt with a permissible “frisk” incident to an investigative stop based on less than probable cause to arrest, the Court of Appeals felt that the principles of that case should be carried over to this probable-cause arrest for driving while one’s license is revoked. Since there would be no further evidence of such a crime to be obtained in a search of the arrestee, the court held that only a search for weapons could be justified.</p>
<p id="b379-6"><em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra,</a></span> </em>did not involve an arrest for probable cause, and it made quite clear that the “protective frisk” for weapons which it approved might be conducted without probable cause. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 21-22, 24-25</a></span>. This Court’s opinion explicitly recognized that there is a “distinction in purpose, character, and extent between a search incident to an arrest and a limited search for weapons.”</p>
<blockquote id="b379-7">“The former, although justified in part by the acknowledged necessity to protect the arresting officer from assault with a concealed weapon, <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964), is also justified on other grounds, <em>ibid., </em>and can therefore involve a relatively extensive exploration of the person. A search for weapons in the absence of probable cause to arrest, however, must, like any other search, be strictly circumscribed by the exigen<page-number citation-index="1" label="228">*228</page-number>cies which justify its initiation. <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#310" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 310</a></span> (1967) (Mr. Justice Fortas, concurring). Thus it must be limited to that which is necessary for the discovery of weapons which might be used to harm the officer or others nearby, and may realistically be characterized as something less than a ‘full’ search, even though it remains a serious intrusion.</blockquote>
<blockquote id="b380-5">"... An arrest is a wholly different kind of intrusion upon individual freedom from a limited search for weapons, and the interests each is designed to serve are likewise quite different. An arrest is the initial stage of a criminal prosecution. It is intended to vindicate society’s interest in having its laws obeyed, and it is inevitably accompanied by future interference with the individual’s freedom of movement, whether or not trial or conviction ultimately follows. The protective search for weapons, on the other hand, constitutes a brief, though far from inconsiderable, intrusion upon the sanctity of the person.” <em>Id., </em>at 25-26 (footnote omitted).</blockquote>
<p id="b380-6"><em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>therefore, affords no basis to carry over to a probable-cause arrest the limitations this Court placed on a stop-and-frisk search permissible without probable cause.</p>
<p id="b380-7">The Court of Appeals also relied on language in <em>Peters </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#66" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 66</a></span> (1968), a companion case to <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>. </em>There the Court held that the police officer had authority to search Peters because he had probable cause to arrest him, and went on to say:</p>
<blockquote id="b380-8">“[T]he incident search was obviously justified 'by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the <page-number citation-index="1" label="229">*229</page-number>destruction of evidence of the crime.’ <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964). Moreover, it was reasonably limited in scope by these purposes. Officer Lasky did not engage in an unrestrained and thorough-going examination of Peters and his personal effects.” <em>Id., </em>at 67.</blockquote>
<p id="b381-5">It is, of course, possible to read the second sentence from this quotation as imposing a novel limitation on the established doctrine set forth in the first sentence. It is also possible to read it as did Mr. Justice Harlan in his opinion concurring in the result:</p>
<blockquote id="b381-6">“The second possible source of confusion is the Court’s statement that 'Officer Lasky did not engage in an unrestrained and thorough-going examination of Peters and his personal effects.’ [392 U. S.], at 67. Since the Court found probable cause to arrest Peters, and since an officer arresting on probable cause is entitled to make a very full incident search, I assume that this is merely a factual observation. As a factual matter, I agree with it.” <em>Id., </em>at 77 (footnote omitted).</blockquote>
<p id="b381-7">We do not believe that the Court in <em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">Peters</a></span> </em>intended in one unexplained and unelaborated sentence to impose a novel and far-reaching limitation on the authority to search the person of an arrestee incident to his lawful arrest. While the language from <em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">Peters</a></span> </em>was quoted with approval in <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#764" aria-description="Citation for case: Chimel v. California">395 U. S., at 764</a></span>, it is preceded by a full exposition of the traditional and unqualified authority of the arresting officer to search the arrestee’s person. <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California"><em>Id., </em>at 763</a></span>. We do not believe that either <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>or <em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">Peters</a></span>, </em>when considered in the light of the previously discussed statements of this Court, justified the sort of limitation upon that authority which the Court of Appeals fashioned in this case.</p>
<p id="b382-4"><page-number citation-index="1" label="230">*230</page-number>Ill</p>
<p id="b382-5">Virtually all of the statements of this Court affirming the existence of an unqualified authority to search incident to a lawful arrest are dicta. We would not, therefore, be foreclosed by principles of <em>stare decisis </em>from further examination into history and practice in order to see- whether the sort of qualifications imposed by the Court of Appeals in this case were in fact intended by the Framers of the Fourth Amendment or recognized in cases decided prior to <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>. </em>Unfortunately such authorities as exist are sparse. Such common-law treatises as Blackstone’s Commentaries and Holmes’ Common Law are simply silent on the subject. Pollock and Maitland, in their History of English Law, describe the law of arrest as “rough and rude” before the time of Edward I, but do not address the authority to search incident to arrest. 2 F. Pollock &amp; F. Maitland, The History of English Law <em>582 </em>(2d ed. 1909).</p>
<p id="b382-6">The issue was apparently litigated in the English courts in <em>Dillon </em>v. <em>O’Brien, </em>16 Cox C. C. 245 (Exch. Ireland, 1887), cited in <em>Weeks </em>v. <em>United States, supra, </em>There Baron Palles said:</p>
<blockquote id="b382-7">“But the interest of the State in the person charged being brought to trial in due course necessarily extends, as well -to the preservation of material evidence of his guilt or innocence, as to his custody for the purpose of trial. His custody is of no value if the law is powerless to prevent the abstraction or destruction of this evidence, without which a trial would be no more than an empty form. But if there be a right to production or preservation of this evidence, I cannot see how it can be enforced otherwise than by capture.” 16 Cox C. C., at 250.</blockquote>
<p id="b383-3"><page-number citation-index="1" label="231">*231</page-number><em>Spalding </em>v. <em>Preston, </em><span class="citation" data-id="6573992"><a href="/opinion/6694075/spalding-v-preston/" aria-description="Citation for case: Spalding v. Preston">21 Vt. 9</a></span> (1848), represents an early holding in this country that evidence may be seized from one who is lawfully arrested. In <em>Closson </em>v. <em>Morrison, </em>47 N. H. 482 (1867), the Court made the following statement:</p>
<blockquote id="b383-4">“[W]e think that an officer would also be justified in taking from a person whom he had arrested for crime, any deadly weapon he might find upon him, such as a revolver, a dirk, a knife, a sword cane, a slung shot, or a club, though it had not been used or intended to be used in the commission of the offence for which the prisoner had been arrested, and even though no threats of violence towards the officer had been made. A due regard for his own safety on the part of the officer, and also for the public safety, would justify a sufficient search to ascertain if such weapons were carried about the person of the prisoner, or were in his possession, and if found, to seize and hold them until the prisoner should be discharged, or until they could be otherwise properly disposed of. <em>Spalding </em>v. <em>Preston, </em><span class="citation" data-id="6573992"><a href="/opinion/6694075/spalding-v-preston/#16" aria-description="Citation for case: Spalding v. Preston">21 Vt. 9, 16</a></span>.</blockquote>
<blockquote id="b383-5">“So we think it might be with money or other articles of value, found upon the prisoner, by means of which, if left in his possession, he might procure his escape, or obtain tools, or implements, or weapons with which to effect his escape. We think the officer arresting a man for crime, not only may, but frequently should, make such searches and seizures; that in many cases they might be reasonable and proper, and courts would hold him harmless for so doing, when he acts in good faith, and from a regard to his own or the public safety, or the security of his prisoner.” <em>Id., </em>at 484-485.</blockquote>
<p id="b384-4"><page-number citation-index="1" label="232">*232</page-number>Similarly, in <em>Holker </em>v. <em>Hennessey, </em><span class="citation" data-id="8012666"><a href="/opinion/8055583/holker-v-hennessey/" aria-description="Citation for case: Holker v. Hennessey">141 Mo. 527</a></span>, <span class="citation" data-id="8012666"><a href="/opinion/8055583/holker-v-hennessey/" aria-description="Citation for case: Holker v. Hennessey">42 S. W. 1090</a></span> (1897), the Supreme Court of Missouri said:</p>
<blockquote id="b384-5">"Generally speaking, in the absence of a statute, an officer has no right to take any property from the person of the prisoner except such as may afford evidence of the crime charged, or means'of identifying the criminal, or may be helpful in making an escape.” <span class="citation" data-id="8012666"><a href="/opinion/8055583/holker-v-hennessey/#539" aria-description="Citation for case: Holker v. Hennessey"><em>Id., </em>at 539</a></span>, <span class="citation" data-id="8012666"><a href="/opinion/8055583/holker-v-hennessey/#1093" aria-description="Citation for case: Holker v. Hennessey">42 S. W., at 1093</a></span>.</blockquote>
<p id="b384-6">Then Associate Judge Cardozo of the New York Court of Appeals summarized his understanding of the historical basis for the authority to search incident to arrest in these words:</p>
<blockquote id="b384-7">“The basic principle is this: Search of the person is unlawful when the seizure of the body is a trespass, and the purpose of the search is to discover grounds as yet unknown for arrest or accusation [citation omitted]. Search of the person becomes lawful when grounds for arrest and accusation have been discovered, and the law is in the act of subjecting the body of the accused to its physical dominion.</blockquote>
<blockquote id="b384-8">“The distinction may seem subtle, but in truth it is founded in shrewd appreciation of the necessities of government. We are not to strain an immunity to the point at which human nature rebels against honoring it in conduct. The peace officer empowered to arrest must be empowered to disarm. If he may disarm, he may search, lest a. weapon be concealed. The search being lawful, he retains what he finds if connected with the crime.” <em>People </em>v. <em>Chiagles, </em><span class="citation" data-id="3579530"><a href="/opinion/3598271/people-v-chiagles/#197" aria-description="Citation for case: People v. . Chiagles">237 N. Y. 193, 197</a></span>, <span class="citation" data-id="3579530"><a href="/opinion/3598271/people-v-chiagles/#584" aria-description="Citation for case: People v. . Chiagles">142 N. E. 583, 584</a></span> (1923).</blockquote>
<p id="b384-10">While these earlier authorities are sketchy, they tend to support the broad statement of the authority to <page-number citation-index="1" label="233">*233</page-number>search incident to arrest found in the successive decisions of this Court, rather than the restrictive one which was applied by the Court of Appeals in this case. The scarcity of case law before <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>is doubtless due in part to the fact that the exclusionary rule there enunciated had been first adopted only 11 years earlier in Iowa; but it would seem to be also due in part to the fact that the issue was regarded as well settled.<footnotemark>3</footnotemark></p>
<p id="b385-4">The Court of Appeals in effect determined that the <em>only </em>reason supporting the authority for a <em>full </em>search incident to lawful arrest was the possibility of discovery of evidence or fruits.<footnotemark>4</footnotemark> Concluding that there could be no evidence or fruits in the case of an offense such as that with which respondent was charged, it held that any protective search would have to be limited by the conditions laid down in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>for a search upon less than probable cause to arrest. Quite apart from the fact that <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>clearly recognized the distinction between the two types of searches, and that a different rule governed one than governed the other, we find additional reason to disagree with the Court of Appeals.</p>
<p id="b386-4"><page-number citation-index="1" label="234">*234</page-number>The justification or reason for the authority to search incident to a lawful arrest rests quite as much on the need to disarm the suspect in order to take him into custody as it does on the need to preserve evidence on his person for later use at trial. <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span> (1925); <em>Abel </em>v. <em>United States, </em><span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span> (1960). The standards traditionally governing a search incident to lawful arrest are not, therefore, commuted to the stricter <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>standards by the absence of probable fruits or further evidence of the particular crime for which the arrest is made.</p>
<p id="b386-5">Nor are we inclined, on the basis of what seems to us to be a rather speculative judgment, to qualify the breadth of the general authority to search incident to a lawful custodial arrest on an assumption that persons arrested for the offense of driving while their licenses have been revoked are less likely to possess dangerous weapons than are those arrested for other crimes.<footnotemark>5</footnotemark> It is scarcely open to doubt that the danger to an officer is far greater in the case of the extended exposure which <page-number citation-index="1" label="235">*235</page-number>follows the taking of a suspect into custody and transporting him to the police station than in the case of the relatively fleeting contact resulting from the typical <em>Terry-type </em>stop. This is an adequate basis for treating all custodial arrests alike for purposes of search justification.</p>
<p id="b387-5">But quite apart from these distinctions, our more fundamental disagreement with the Court of Appeals arises from its suggestion that there must be litigated in each case the issue of whether or not there was present one of the reasons supporting the authority for a search of the person incident to a lawful arrest. We do not think the long line of authorities of this Court dating back to <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>, </em>or what we can glean from the history of practice in this country and in England, requires such a case-by-case adjudication. A police officer's determination as to how and where to search the person of a suspect whom he has arrested is necessarily a quick <em>ad hoc </em>judgment which the Fourth Amendment does not require to be broken down in each instance into an analysis of each step in the search. The authority to search the person incident to a lawful custodial arrest, while based upon the need to disarm and to discover evidence, does not depend on what a court may later decide was the probability in a particular arrest situation that weapons or evidence would in fact be found upon the person of the suspect. A custodial arrest of a suspect based on probable cause is a reasonable intrusion under the Fourth Amendment; that intrusion being lawful, a search incident to the arrest requires no additional justification. It is the fact of the lawful arrest which establishes the authority to search, and we hold that in the case of a lawful custodial arrest a full search of the person is not only an exception to the warrant requirement of the Fourth Amendment, but is also a “reasonable” search under that Amendment.</p>
<p id="b388-4"><page-number citation-index="1" label="236">*236</page-number>IV</p>
<p id="b388-5">The search of respondent’s person conducted by Officer Jenks in this case and the seizure from him of the heroin, were permissible under established Fourth Amendment law. While thorough, the search partook of none of the extreme or patently abusive characteristics which were held to violate the Due Process Clause of the Fourteenth Amendment in <em>Rochin </em>v. <em>California, </em><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952). Since it is the fact of custodial arrest which gives rise to the authority to search,<footnotemark>6</footnotemark> it is of no moment that Jenks did not indicate any subjective fear of the respondent or that he did not himself suspect that respondent was armed.<footnotemark>7</footnotemark> Having in the course of a lawful search come upon the crumpled package of cigarettes, he was entitled to inspect it; and when his inspection revealed the heroin capsules, he was entitled to seize them as “fruits, instrumentalities, or contraband” probative of criminal conduct. <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#154" aria-description="Citation for case: Harris v. United States">331 U. S., at 154-155</a></span>; <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#299" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 299, 307</a></span> (1967); <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#149" aria-description="Citation for case: Adams v. Williams">407 U. S., at 149</a></span>. <page-number citation-index="1" label="237">*237</page-number>The judgment of the Court of Appeals holding otherwise is</p>
<p id="b389-5">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b373-6"> The Court of Appeals noted that there was a difference in the presentation of the facts in the various proceedings that were conducted in the District Court. Counsel for respondent on appeal stressed that respondent had a record of two prior narcotics convictions, and suggested that Officer Jenks may have been aware of that record through his investigation of criminal records, while Jenks was cheeking out the discrepancies in the birthdates on the operator’s permit and on the Selective Service card that had been given to him for examination when he had confronted the respondent on the previous occasion. Respondent argued below that Jenks may have used the subsequent traffic violation arrest as a mere pretext for a narcotics search which would not have been allowed by a neutral magistrate had Jenks sought a warrant. The Court of Appeals found that Jenks had denied he had any such motive, and for the purposes of its opinion accepted the Government’s version of that factual question, since even accepting that version it still found the search involved to be unconstitutional. 153 U. S. App. D. C. 114, 120 n. 3, <span class="citation" data-id="9459062"><a href="/opinion/307722/united-states-v-willie-robinson-jr/" aria-description="Citation for case: United States v. Willie Robinson, Jr.">471 F. 2d 1082</a></span>, 1088 n. 3. We think it is sufficient for purposes of our decision that respondent was lawfully arrested for an offense, and that Jenks’ placing him in custody following that arrest was not a departure from established police department practice. See n. 2, <em>infra. </em>We leave for another day questions which would arise on facts different from these.</p>
</footnote>
<footnote label="2">
<p id="b373-7"> The Government introduced testimony at the evidentiary hearing upon the original remand by the Court of Appeals as to certain standard operating procedures of the Metropolitan Police Department. Sergeant Dennis C. Donaldson, a Metropolitan Police Department Training Division instructor, testified that when a police officer makes "a full custody arrest,” which he defined as one where an officer “would arrest a subject and subsequently transport him to a police facility for booking,” the officer is trained to make a full “field type search”:</p>
<blockquote id="b373-8">“Q. Would you describe the physical acts the officer is instructed to perform with respect to this field search in a full custody arrest situation?</blockquote>
<blockquote id="b373-9">“A. (Sgt. Donaldson). Basically, it is a thorough search of the <page-number citation-index="1" label="222">*222</page-number>individual. We would expect in a field search that the officer completely search the individual and inspect areas such as behind the collar, underneath the collar, the waistband of the trousers, the cuffs, the socks and shoes. Those are the areas we would ask a complete thorough search of.</blockquote>
<blockquote id="b374-6">“Q. What are the instructions in a field type search situation when an officer feels something on the outside of the garment?</blockquote>
<blockquote id="b374-7">“A. If it is a full custody arrest and he is conducting a field search, we expect him to remove anything and examine it to determine exactly what it is.</blockquote>
<blockquote id="b374-8">“THE COURT: That is a full custody arrest. What is the last part of it?</blockquote>
<blockquote id="b374-9">“THE WITNESS: In conducting a field search, which is done any time there is a full custody arrest, we expect the officer to examine anything he might find on the subject.</blockquote>
<blockquote id="b374-10">“THE COURT: Would he do the same thing in a pat-down search?</blockquote>
<blockquote id="b374-11">“THE WITNESS: If he could determine in his pat-down or frisk by squeezing that it was not, in fact, a weapon that could be used against him, then we don’t instruct him to go further.</blockquote>
<blockquote id="b374-12">“THE COURT: But in a field search, even though he may feel something that he believes is not a weapon, is he instructed, to take it out?</blockquote>
<blockquote id="b374-13">“THE WITNESS: Yes, sir.”</blockquote>
<p id="b374-14">Sergeant Donaldson testified that officers are instructed to examine the “contents of all of the pockets” of the arrestee in the course of the field search. It was stated that these standard operating procedures were initiated bjr the police department “ [primarily, for [the officer’s] own safety and, secondly, for the safety of the individual he has placed under arrest and, thirdly, to search for evidence of the crime.” While the officer is instructed to make a full field search of the person of the individual he arrests, he is instructed, and police department regulations provide, that in the case of a full-custody arrest for driving after revocation, "areas beyond [the arrestee’s] immediate control should not be searched because there is no probable cause to believe that the vehicle contains fruits, instrumentalities, contraband or evidence of the offense of driving after revocation.” Those regulations also provide that in the case <page-number citation-index="1" label="223">*223</page-number>of some traffic offenses, including the crime of operating a motor vehicle after revocation of an operator’s permit, the officer shall make a summary arrest of the violator and take the violator, in custody, to the station house for booking. D. C. Metropolitan Police Department General Order No. 3, series 1959 (Apr. 24, 1959).</p>
<p id="b375-9">Such operating procedures are not, of course, determinative of the constitutional issues presented by this case.</p>
</footnote>
<footnote label="3">
<p id="b385-5"> See T. Taylor, Two Studies in Constitutional Interpretation 44-45 (1969).</p>
<p id="b385-6">Taylor suggests that there “is little reason to doubt that search of an arrestee’s person and premises is as old as the institution of arrest itself.” <em>Id., </em>at 28. “Neither in the reported cases nor the legal literature is there any indication that search of the person of an arrestee, or the premises in which he was taken, was ever challenged in England until the end of the nineteenth century . . . [and] the English courts gave the point short shrift.” <em>Id., </em>at 29.</p>
</footnote>
<footnote label="4">
<p id="b385-7"> Where the arrest is made for a crime for which it is reasonable to believe that evidence exists, the Court of Appeals recognizes that “warrantless intrusion into the pockets of the arrestee to discover such evidence is reasonable under the 'search incident’ exception.” 153 U. S. App. D. C., at 127, <span class="citation" data-id="9459062"><a href="/opinion/307722/united-states-v-willie-robinson-jr/#1095" aria-description="Citation for case: United States v. Willie Robinson, Jr.">471 F. 2d, at 1095</a></span>. The court then states that the officer may use this “reasonable [evidentiary] intrusion” to simultaneously look for weapons. <em><span class="citation" data-id="9459062"><a href="/opinion/307722/united-states-v-willie-robinson-jr/" aria-description="Citation for case: United States v. Willie Robinson, Jr.">Ibid.</a></span></em></p>
</footnote>
<footnote label="5">
<p id="b386-6"> Such an assumption appears at least questionable in light of the available statistical data concerning assaults on police officers who are in the course of making arrests. The danger to the police officer flows from the fact of the arrest, and its attendant proximity, stress, and uncertainty, and not from the grounds for arrest. One study concludes that approximately 30% of the shootings of police officers occur when an officer stops a person in an automobile. Bristow, Police Officer <em>Shootings </em>— A Tactical Evaluation, 54 J. Crim. L. C. &amp; P. S. 93 (1963), cited in <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#148" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 148</a></span> (1972). The Government in its brief notes that the Uniform Crime Reports, prepared by the Federal Bureau of Investigation, indicate that a significant percentage of murders of police officers occurs when the officers are making traffic stops. Brief for the United States 23. Those reports indicate that during January-March 1973, 35 police officers were murdered; 11 of those officers were killed while engaged in making traffic stops. <em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">Ibid.</a></span></em></p>
</footnote>
<footnote label="6">
<p id="b388-6"> The opinion of the Court of Appeals also discussed its understanding of the law where the police officer makes what the court characterized as “a routine traffic stop,” <em>i. e., </em>where the officer would simply issue a notice of violation and allow the offender to proceed. Since in this case the officer did make a full-custody arrest of the violator, we do not reach the question discussed by the Court of Appeals.</p>
</footnote>
<footnote label="7">
<p id="b388-7"> The United States concedes that “in searching respondent, [Officer Jenks] was not motivated by a feeling of imminent danger and was not specifically looking for weapons.” Brief for the United States 34. Officer Jenks testified, “I just searched him [Robinson], I didn't think about what I was looking for. I just searched him.” As previously noted, Officer Jenks also testified that upon removing the cigarette package from the respondent’s custody, he was still unsure what was in the package, but that he knew it was not cigarettes.</p>
</footnote>
</opinion>
```

---
