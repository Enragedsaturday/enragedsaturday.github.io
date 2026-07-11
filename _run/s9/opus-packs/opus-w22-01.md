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

## GROUP: _overhaul2/lake/cases/Winston v. Lee.json  (`lake-record`, 6 assertions)

### content_page

```
---
title: "Winston v. Lee"
type: case
citation: "470 U.S. 753 (1985)"
parallel_cite: "105 S. Ct. 1611; 84 L. Ed. 2d 662; 53 U.S.L.W. 4367"
neutral_cite: 1985 U.S. LEXIS 76
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-03-20
docket: 83-1334
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-03-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Winston v. Lee
  varies_by_point: false
  scope_note: "Controlling: a compelled surgical intrusion into the body for evidence may be unreasonable even with probable cause and a court order; reasonableness turns on the Schmerber balance of intrusion against need."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111380/winston-v-lee/"
  cluster_id: 111380
  opinion_id: 9429963
  identity_checked: true
homes:
  - page: "[[Scope Manner and Related Issues]]"
    role: "Limiting"
related: ["[[Schmerber v. California]]", "[[Cupp v. Murphy]]", "[[Missouri v. McNeely]]"]
aliases: ["Lee v. Winston"]
tags: ["case", "fourth-amendment", "bodily-intrusion", "warrant-requirement", "reasonableness", "surgery"]
holding: "Court-ordered surgery under general anesthesia to recover a bullet for use as evidence is an unreasonable search where, under the Schmerber balance, the severe intrusion on bodily integrity and safety outweighs the State's need for the evidence — even with probable cause and a judicial order."
lake:
  record_id: Winston v. Lee
  status: verified
  projected_at: 2026-07-06
---

# Winston v. Lee

*470 U.S. 753 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Lee was suspected of an armed robbery in which the store owner shot the robber. Hours later, Lee appeared at a hospital with a gunshot wound and was identified by the owner. To prove the bullet lodged under Lee's collarbone came from the owner's gun, the Commonwealth sought a court order compelling Lee to undergo surgery — requiring general anesthesia — to remove it. Lee resisted, and the lower courts enjoined the surgery as an unreasonable search.

## Issue
Does the Fourth Amendment permit a State to compel a suspect to undergo surgery under general anesthesia to recover a bullet for use as evidence?

## Rule
Not on these facts. "A compelled surgical intrusion into an individual's body for evidence . . . implicates expectations of privacy and security of such magnitude that the intrusion may be 'unreasonable' even if likely to produce evidence of a crime." — 470 U.S. at 759. ^pin-759

"The reasonableness of surgical intrusions beneath the skin depends on a case-by-case approach, in which the individual's interests in privacy and security are weighed against society's interests in conducting the procedure." — *Id.* at 760. ^pin-760

The *[[Schmerber v. California|Schmerber]]* framework controls: beyond the threshold requirements of probable cause and (absent emergency) a warrant, the court weighs the extent of the intrusion on bodily integrity, dignity, and safety against the community's need for the evidence. Where the State "seeks to intrude upon an area in which our society recognizes a significantly heightened privacy interest, a more substantial justification is required to make the search 'reasonable.'" — *Id.* at 767. ^pin-767

## Application
The proposed surgery — general anesthesia and a virtually total divestment of Lee's control over probing beneath his skin — was a severe intrusion, and the medical risks were a subject of genuine dispute, which itself counseled against reasonableness. The Commonwealth's need was not compelling: it already had substantial other proof that Lee was the robber, including the owner's spontaneous identification, Lee's presence near the store shortly after the crime, and the bullet's location correlating with the owner's account. With the intrusion severe and the need weak, the balance tipped decisively against the surgery: "the Commonwealth has failed to demonstrate that it would be 'reasonable' . . . to search for evidence of this crime by means of the contemplated surgery." — *Id.* at 766. ^pin-766

## Conclusion
Compelling the surgery would be an unreasonable search under the Fourth Amendment. The judgment enjoining the operation was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Winston* remains the controlling authority that a deep, compelled surgical bodily intrusion can be unreasonable even with a warrant and probable cause, decided under the [[Schmerber v. California]] balancing framework. It contrasts with minor, justified intrusions like the fingernail scraping in [[Cupp v. Murphy]] and informs the bodily-intrusion analysis applied in [[Missouri v. McNeely]]. No negative treatment.

## Appears on
- [[Scope Manner and Related Issues]] — *Limiting*

## Sources
- *Winston v. Lee*, 470 U.S. 753 (1985) — https://www.courtlistener.com/opinion/111380/winston-v-lee/ — pinpoints: 759, 760, 766, 767.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "17ee1e6c28569471", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Winston v. Lee"}, "payload": {"all": [{"cite": "470 U.S. 753", "page": "753", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "470"}, {"cite": "105 S. Ct. 1611", "page": "1611", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "105"}, {"cite": "84 L. Ed. 2d 662", "page": "662", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "84"}, {"cite": "1985 U.S. LEXIS 76", "page": "76", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1985"}, {"cite": "53 U.S.L.W. 4367", "page": "4367", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "53"}], "display": "470 U.S. 753", "official": {"cite": "470 U.S. 753", "page": "753", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "470"}, "official_selection_present": true, "record_id": "Winston v. Lee"}}
{"assertion_id": "447f2823d7c6bec9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-767", "record_id": "Winston v. Lee"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-767", "pinpoint_status": "slip-only", "quote": "seeks to intrude upon an area in which our society recognizes a significantly heightened privacy interest, a more substantial justification is required to make the search 'reasonable.'", "quote_fidelity": "mismatch", "record_id": "Winston v. Lee", "star_marker": null}}
{"assertion_id": "53a8aeb995174196", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-766", "record_id": "Winston v. Lee"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-766", "pinpoint_status": "slip-only", "quote": "the Commonwealth has failed to demonstrate that it would be 'reasonable' . . . to search for evidence of this crime by means of the contemplated surgery.", "quote_fidelity": "mismatch", "record_id": "Winston v. Lee", "star_marker": null}}
{"assertion_id": "8f40005581672c53", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-759", "record_id": "Winston v. Lee"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-759", "pinpoint_status": "slip-only", "quote": "--- # Winston v. Lee *470 U.S. 753 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Lee was suspected of an armed robbery in which the store owner shot the robber. Hours later, Lee appeared at a hospital with a gunshot wound and was identified by the owner. To prove the bullet lodged under Lee's collarbone came from the owner's gun, the Commonwealth sought a court order compelling Lee to undergo surgery — requiring general anesthesia — to remove it. Lee resisted, and the lower courts enjoined the surgery as an unreasonable search. ## Issue Does the Fourth Amendment permit a State to compel a suspect to undergo surgery under general anesthesia to recover a bullet for use as evidence? ## Rule Not on these facts.", "quote_fidelity": "mismatch", "record_id": "Winston v. Lee", "star_marker": null}}
{"assertion_id": "b0cd20bc142752a1", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-760", "record_id": "Winston v. Lee"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-760", "pinpoint_status": "slip-only", "quote": "The reasonableness of surgical intrusions beneath the skin depends on a case-by-case approach, in which the individual's interests in privacy and security are weighed against society's interests in conducting the procedure.", "quote_fidelity": "mismatch", "record_id": "Winston v. Lee", "star_marker": null}}
{"assertion_id": "09fe8ca780b89319", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Winston v. Lee"}, "payload": {"as_of_content": "1985-03-20", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Winston v. Lee", "scope_note": "Controlling: a compelled surgical intrusion into the body for evidence may be unreasonable even with probable cause and a court order; reasonableness turns on the Schmerber balance of intrusion against need.", "varies_by_point": false}}
```

### lake record — Winston v. Lee

```json
{
  "schema_version": "s2.v1",
  "record_id": "Winston v. Lee",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Winston v. Lee",
    "case_name_short": "Winston",
    "case_name_full": "WINSTON, SHERIFF, Et Al. v. LEE",
    "input_case_name": "Winston v. Lee",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-03-20",
    "year": 1985,
    "docket": "83-1334",
    "cluster_id": 111380,
    "lead_opinion_id": 9429963,
    "sibling_ids": [
      111380,
      9429963,
      9429964
    ],
    "absolute_url": "/opinion/111380/winston-v-lee/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "470 U.S. 753",
      "volume": "470",
      "reporter": "U.S.",
      "page": "753",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 1611",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1611",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 2d 662",
        "volume": "84",
        "reporter": "L. Ed. 2d",
        "page": "662",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4367",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4367",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 76",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "76",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "470 U.S. 753",
        "volume": "470",
        "reporter": "U.S.",
        "page": "753",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 1611",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1611",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 2d 662",
        "volume": "84",
        "reporter": "L. Ed. 2d",
        "page": "662",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 76",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "76",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4367",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4367",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "470 U.S. 753",
    "official_selection": {
      "court_class": "scotus",
      "selected": "470 U.S. 753",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-759",
      "page": null,
      "quote": "--- # Winston v. Lee *470 U.S. 753 (1985)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Lee was suspected of an armed robbery in which the store owner shot the robber. Hours later, Lee appeared at a hospital with a gunshot wound and was identified by the owner. To prove the bullet lodged under Lee's collarbone came from the owner's gun, the Commonwealth sought a court order compelling Lee to undergo surgery \u2014 requiring general anesthesia \u2014 to remove it. Lee resisted, and the lower courts enjoined the surgery as an unreasonable search. ## Issue Does the Fourth Amendment permit a State to compel a suspect to undergo surgery under general anesthesia to recover a bullet for use as evidence? ## Rule Not on these facts.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-760",
      "page": null,
      "quote": "The reasonableness of surgical intrusions beneath the skin depends on a case-by-case approach, in which the individual's interests in privacy and security are weighed against society's interests in conducting the procedure.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-767",
      "page": null,
      "quote": "seeks to intrude upon an area in which our society recognizes a significantly heightened privacy interest, a more substantial justification is required to make the search 'reasonable.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-766",
      "page": null,
      "quote": "the Commonwealth has failed to demonstrate that it would be 'reasonable' . . . to search for evidence of this crime by means of the contemplated surgery.",
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
    "composite_basis_ref": "Winston v. Lee",
    "varies_by_point": false,
    "scope_note": "Controlling: a compelled surgical intrusion into the body for evidence may be unreasonable even with probable cause and a court order; reasonableness turns on the Schmerber balance of intrusion against need.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Dennis",
          "cluster_id": 4679939,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Adrian King, Jr. v. Jim Rubenstein",
          "cluster_id": 3210222,
          "cite": [
            "825 F.3d 206",
            "2016 U.S. App. LEXIS 10276",
            "2016 WL 3165598"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cole v. State",
          "cluster_id": 5446855,
          "cite": [
            "490 S.W.3d 918",
            "2016 Tex. Crim. App. LEXIS 84",
            "2016 WL 3018203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane1_negative"
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
        "journal_ref": "Winston v. Lee:lane1_negative"
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
        "journal_ref": "Winston v. Lee:lane2_top_cited"
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
        "journal_ref": "Winston v. Lee:lane2_top_cited"
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
        "journal_ref": "Winston v. Lee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Washington v. Glucksberg",
          "cluster_id": 118144,
          "cite": [
            "138 L. Ed. 2d 772",
            "117 S. Ct. 2258",
            "521 U.S. 702",
            "1997 U.S. LEXIS 4039",
            "11 Fla. L. Weekly Fed. S 190",
            "97 Cal. Daily Op. Serv. 5008",
            "97 Daily Journal DAR 8150",
            "65 U.S.L.W. 4669"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Skinner v. Railway Labor Executives' Assn.",
          "cluster_id": 112219,
          "cite": [
            "103 L. Ed. 2d 639",
            "109 S. Ct. 1402",
            "489 U.S. 602",
            "1989 U.S. LEXIS 1568",
            "4 I.E.R. Cas. (BNA) 224",
            "1989 CCH OSHD 28,476",
            "57 U.S.L.W. 4324",
            "13 OSHC (BNA) 2065",
            "130 L.R.R.M. (BNA) 2857",
            "49 Empl. Prac. Dec. (CCH) 38,791"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Planned Parenthood of Southeastern Pa. v. Casey",
          "cluster_id": 112786,
          "cite": [
            "120 L. Ed. 2d 674",
            "112 S. Ct. 2791",
            "505 U.S. 833",
            "1992 U.S. LEXIS 4751"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane2_top_cited"
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
        "journal_ref": "Winston v. Lee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Washington v. Harper",
          "cluster_id": 112381,
          "cite": [
            "108 L. Ed. 2d 178",
            "110 S. Ct. 1028",
            "494 U.S. 210",
            "1990 U.S. LEXIS 1174"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane2_top_cited"
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
        "journal_ref": "Winston v. Lee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sell v. United States",
          "cluster_id": 130152,
          "cite": [
            "156 L. Ed. 2d 197",
            "123 S. Ct. 2174",
            "539 U.S. 166",
            "2003 U.S. LEXIS 4594"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane2_top_cited"
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
        "journal_ref": "Winston v. Lee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bowers v. Hardwick",
          "cluster_id": 111738,
          "cite": [
            "92 L. Ed. 2d 140",
            "106 S. Ct. 2841",
            "478 U.S. 186",
            "1986 U.S. LEXIS 123"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cruzan Ex Rel. Cruzan v. Director, Missouri Department of Health",
          "cluster_id": 112478,
          "cite": [
            "111 L. Ed. 2d 224",
            "110 S. Ct. 2841",
            "497 U.S. 261",
            "1990 U.S. LEXIS 3301",
            "58 U.S.L.W. 4916"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marshall King v. Robert McCarty",
          "cluster_id": 2789826,
          "cite": [
            "781 F.3d 889",
            "2015 U.S. App. LEXIS 5008",
            "2015 WL 1396611"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane2_top_cited"
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
        "journal_ref": "Winston v. Lee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hedges v. Musco",
          "cluster_id": 767706,
          "cite": [
            "204 F.3d 109",
            "2000 U.S. App. LEXIS 2671"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Officer Melissa Kallstrom v. City of Columbus",
          "cluster_id": 751709,
          "cite": [
            "136 F.3d 1055",
            "26 Media L. Rep. (BNA) 1353",
            "13 I.E.R. Cas. (BNA) 1202",
            "1998 U.S. App. LEXIS 1941"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Melton",
          "cluster_id": 1215941,
          "cite": [
            "750 P.2d 741",
            "44 Cal. 3d 713",
            "244 Cal. Rptr. 867",
            "1988 Cal. LEXIS 53"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sanchez v. Pereira-Castillo",
          "cluster_id": 204120,
          "cite": [
            "590 F.3d 31",
            "2009 U.S. App. LEXIS 28250",
            "2009 WL 4936397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jordan v. Gardner",
          "cluster_id": 601474,
          "cite": [
            "986 F.2d 1521",
            "93 Cal. Daily Op. Serv. 1354",
            "1993 U.S. App. LEXIS 3065",
            "1993 WL 46630"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane2_top_cited"
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
        "journal_ref": "Winston v. Lee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shari Guertin v. State of Mich.",
          "cluster_id": 4578962,
          "cite": [
            "912 F.3d 907"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terebesi v. Torreso",
          "cluster_id": 8441937,
          "cite": [
            "764 F.3d 217",
            "2014 U.S. App. LEXIS 16133",
            "2014 WL 4099309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Winston v. Lee:lane2_top_cited"
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
        "journal_ref": "Winston v. Lee:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111380 OR 9429963 OR 9429964) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDE5NjA2NDAwMDAwJnM9Nzc3NTM5JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111380+OR+9429963+OR+9429964%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 60,
        "triage_read": 1,
        "triage_snippet_classified": 59
      },
      "lane2_top_cited": {
        "query": "cites:(111380 OR 9429963 OR 9429964)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzMmcz0xNjM5MDUmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111380+OR+9429963+OR+9429964%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111380 OR 9429963 OR 9429964)",
        "reviewed": 6,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 6,
        "triage_read": 0,
        "triage_snippet_classified": 6
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111380 OR 9429963 OR 9429964)",
    "indexed_citing_opinions": 474,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111380,
        "count": 411,
        "count_source": "search"
      },
      {
        "opinion_id": 9429963,
        "count": 73,
        "count_source": "search"
      },
      {
        "opinion_id": 9429964,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 734,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/winston-v-lee.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY4NDc0OSZzPTQ3Njc3MTEmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28111380+OR+9429963+OR+9429964%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111380,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 105456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 110360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 339793,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 424900,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 1332724,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 1672565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 1784735,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 1948196,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111380,
        "cited_id": 2365879,
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
    "date_created": "2026-07-06T04:33:28Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:33:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:33:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:41:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:33:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Winston v. Lee

```
<opinion type="majority">
<author id="Akj3"><page-number citation-index="1" label="755">*755</page-number>Justice Brennan</author>
<p id="ADD">delivered the opinion of the Court.</p>
<p id="A_A"><em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966), held, <em>inter alia, </em>that a State may, over the suspect’s protest, have a physician extract blood from a person suspected of drunken driving without violation of the suspect’s right secured by the Fourth Amendment not to be subjected to unreasonable searches and seizures. However, <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>cautioned: “That we today hold that the Constitution does not forbid the States[’] minor intrusions into an individual’s body under stringently limited conditions in no way indicates that it permits more substantial intrusions, or intrusions under other conditions.” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#772" aria-description="Citation for case: Schmerber v. California"><em>Id., </em>at 772</a></span>. In this case, the Commonwealth of Virginia seeks to compel the respondent Rudolph Lee, who is suspected of attempting to commit armed robbery, to undergo a surgical procedure under a general anesthetic for removal of a bullet lodged in his chest. Petitioners allege that the bullet will provide evidence of respondent’s guilt or innocence. We conclude that the procedure sought here is an example of the “more substantial intrusion” cautioned against in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>, </em>and hold that to permit the procedure would violate respondent’s right to be secure in his person guaranteed by the Fourth Amendment.</p>
<p id="ADv">A</p>
<p id="AjQ">At approximately 1 a. m. on July 18, 1982, Ralph E. Watkinson was closing his shop for the night. As he was locking the door, he observed someone armed with a gun coming toward him from across the street. Watkinson was also armed and when he drew his gun, the other person told him to freeze. Watkinson then fired at the other person, who returned his fire. Watkinson was hit in the legs, while the other individual, who appeared to be wounded in his left side, ran from the scene. The police arrived on the scene shortly thereafter, and Watkinson was taken by ambulance <page-number citation-index="1" label="756">*756</page-number>to the emergency room of the Medical College of Virginia (MCV) Hospital.</p>
<p id="b812-5">Approximately 20 minutes later, police officers responding to another call found respondent eight blocks from where the earlier shooting occurred. Respondent was suffering from a gunshot wound to his left chest area and told the police that he had been shot when two individuals attempted to rob him. An ambulance took respondent to the MCV Hospital. Watkinson was still in the MCV emergency room and, when respondent entered that room, said “[tjhat’s the man that shot me.” App. 14. After an investigation, the police decided that respondent’s story of having been himself the victim of a robbery was untrue and charged respondent with attempted robbery, malicious wounding, and two counts of using a firearm in the commission of a felony.</p>
<p id="b812-6">B</p>
<p id="b812-7">The Commonwealth shortly thereafter moved in state court for an order directing respondent to undergo surgery to remove an object thought to be a bullet lodged under his left collarbone. The court conducted several evidentiary hearings on the motion. At the first hearing, the Commonwealth’s expert testified that the surgical procedure would take 45 minutes and would involve a three to four percent chance of temporary nerve damage, a one percent chance of permanent nerve damage, and a one-tenth of one percent chance of death. At the second hearing, the expert testified that on reexamination of respondent, he discovered that the bullet was not “back inside close to the nerves and arteries,” <em>id., </em>at 52, as he originally had thought. Instead, he now believed the bullet to be located “just beneath the skin.” <em>Id., </em>at 57. He testified that the surgery would require an incision of only one and one-half centimeters (slightly more than one-half inch), could be performed under local anesthesia, and would result in “no danger on the basis that there’s no general anesthesia employed.” <em>Id., </em>at 51.</p>
<p id="b813-3"><page-number citation-index="1" label="757">*757</page-number>The state trial judge granted the motion to compel surgery. Respondent petitioned the Virginia Supreme Court for a writ of prohibition and/or a writ of habeas corpus, both of which were denied. Respondent then brought an action in the United States District Court for the Eastern District of Virginia to enjoin the pending operation on Fourth Amendment grounds. The court refused to issue a preliminary injunction, holding that respondent’s cause had little likelihood of success on the merits. <span class="citation" data-id="2365879"><a href="/opinion/2365879/lee-v-winston/#247" aria-description="Citation for case: Lee v. Winston">551 F. Supp. 247, 247-253</a></span> (1982).<footnotemark>1</footnotemark></p>
<p id="b813-4">On October 18, 1982, just before the surgery was scheduled, the surgeon ordered that X rays be taken of respondent’s chest. The X rays revealed that the bullet was in fact lodged two and one-half to three centimeters (approximately one inch) deep in muscular tissue in respondent’s chest, substantially deeper than had been thought when the state court granted the motion to compel surgery. The surgeon now believed that a general anesthetic would be desirable for medical reasons.</p>
<p id="b813-5">Respondent moved the state trial court for a rehearing based on the new evidence. After holding an evidentiary hearing, the state trial court denied the rehearing, and the Virginia Supreme Court affirmed. Respondent then returned to federal court, where he moved to alter or amend the judgment previously entered against him. After an evi-dentiary hearing, the District Court enjoined the threatened surgery. <span class="citation" data-id="2365879"><a href="/opinion/2365879/lee-v-winston/#253" aria-description="Citation for case: Lee v. Winston">551 F. Supp., at 253-261</a></span> (supplemental opinion).<footnotemark>2</footnotemark></p>
<p id="b814-4"><page-number citation-index="1" label="758">*758</page-number>A divided panel of the Court of Appeals for the Fourth Circuit affirmed. <span class="citation" data-id="9471202"><a href="/opinion/424900/rudolph-lee-jr-v-andrew-j-winston-sheriff-aubrey-m-davis-jr-and/" aria-description="Citation for case: Rudolph Lee, Jr. v. Andrew J. Winston, Sheriff Aubrey M....">717 F. 2d 888</a></span> (1983).<footnotemark>3</footnotemark> We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./466/942/">466 U. S. 942</a></span> (1984), to consider whether a State may consistently with the Fourth Amendment compel a suspect to undergo surgery of this kind in a search for evidence of a crime.</p>
<p id="b814-5">II</p>
<p id="b814-6">The Fourth Amendment protects “expectations of privacy,” see <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967) — the individual’s legitimate expectations that in certain places and at certain times he has “the right to be let alone — the most comprehensive of rights and the right most valued by civilized men.” <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#478" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, <page-number citation-index="1" label="759">*759</page-number>478</a></span> (1928) (Brandéis, J., dissenting). Putting to one side the procedural protections of the warrant requirement, the Fourth Amendment generally protects the “security” of “persons, houses, papers, and effects” against official intrusions up to the point where the community’s need for evidence surmounts a specified standard, ordinarily “probable cause.” Beyond this point, it is ordinarily justifiable for the community to demand that the individual give up some part of his interest in privacy and security to advance the community’s vital interests in law enforcement; such a search is generally “reasonable” in the Amendment’s terms.</p>
<p id="b815-5">A compelled surgical intrusion into an individual’s body for evidence, however, implicates expectations of privacy and security of such magnitude that the intrusion may be “unreasonable” even if likely to produce evidence of a crime. In <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966), we addressed a claim that the State had breached the Fourth Amendment’s protection of the “right of the people to be secure in their <em>persons </em>. . . against unreasonable searches and seizures” (emphasis added) when it compelled an individual suspected of drunken driving to undergo a blood test. Schmerber had been arrested at a hospital while receiving treatment for injuries suffered when the automobile he was driving struck a tree. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#758" aria-description="Citation for case: Schmerber v. California"><em>Id., </em>at 758</a></span>. Despite Schmerber’s objection, a police officer at the hospital had directed a physician to take a blood sample from him. Schmerber subsequently objected to the introduction at trial of evidence obtained as a result of the blood test.</p>
<p id="b815-6">The authorities in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>clearly had probable cause to believe that he had been driving while intoxicated, <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#768" aria-description="Citation for case: Schmerber v. California"><em>id., </em>at 768</a></span>, and to believe that a blood test would provide evidence that was exceptionally probative in confirming this belief. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California"><em>Id., </em>at 770</a></span>. Because the case fell within the exigent-circumstances exception to the warrant requirement, no warrant was necessary. <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Ibid.</a></span> </em>The search was not more intrusive than reasonably necessary to accomplish its goals. Nonetheless, <page-number citation-index="1" label="760">*760</page-number>Schmerber argued that the Fourth Amendment prohibited the authorities from intruding into his body to extract the blood that was needed as evidence.</p>
<p id="b816-5"><em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>noted that “[t]he overriding function of the Fourth Amendment is to protect personal privacy and dignity against unwarranted intrusion by the State.” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#767" aria-description="Citation for case: Schmerber v. California"><em>Id., </em>at 767</a></span>. Citing <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span> (1949), and <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), we observed that these values were “basic to a free society.” We also noted that “[b]ecause we are dealing with intrusions into the human body rather than with state interferences with property relationships or private papers — ‘houses, papers, and effects’— we write on a clean slate.” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#767" aria-description="Citation for case: Schmerber v. California">384 U. S., at 767-768</a></span>. The intrusion perhaps implicated Schmerber’s most personal and deep-rooted expectations of privacy, and the Court recognized that Fourth Amendment analysis thus required a discerning inquiry into the facts and circumstances to determine whether the intrusion was justifiable. The Fourth Amendment neither forbids nor permits all such intrusions; rather, the Amendment’s “proper function is to constrain, not against all intrusions as such, but against intrusions which are not justified in the circumstances, or which are made in an improper manner.” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#768" aria-description="Citation for case: Schmerber v. California"><em>Id., </em>at 768</a></span>.</p>
<p id="b816-6">The reasonableness of surgical intrusions beneath the skin depends on a case-by-case approach, in which the individual’s interests in privacy and security are weighed against society’s interests in conducting the procedure. In a given case, the question whether the community’s need for evidence outweighs the substantial privacy interests at stake is a delicate one admitting of few categorical answers. We believe that <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>, </em>however, provides the appropriate framework of analysis for such cases.</p>
<p id="b816-7"><em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>recognized that the ordinary requirements of the Fourth Amendment would be the threshold requirements for conducting this kind of surgical search and seizure. We noted the importance of probable cause. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#768" aria-description="Citation for case: Schmerber v. California"><em>Id., </em>at 768-769</a></span>. <page-number citation-index="1" label="761">*761</page-number>And we pointed out: “Search warrants are ordinarily required for searches of dwellings, and, absent an emergency, no less could be required where intrusions into the human body are concerned. . . . The importance of informed, detached and deliberate determinations of the issue whether or not to invade another’s body in search of evidence of guilt is indisputable and great.” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California"><em>Id., </em>at 770</a></span>.</p>
<p id="b817-5">Beyond these standards, <em>Schmerber’s </em>inquiry considered a number of other factors in determining the “reasonableness” of the blood test. A crucial factor in analyzing the magnitude of the intrusion in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>is the extent to which the procedure may threaten the safety or health of the individual. “[F]or most people [a blood test] involves virtually no risk, trauma, or pain.” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#771" aria-description="Citation for case: Schmerber v. California"><em>Id., </em>at 771</a></span>. Moreover, all reasonable medical precautions were taken and no unusual or untested procedures were employed in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>; </em>the procedure was performed “by a physician in a hospital environment according to accepted medical practices.” <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Ibid.</a></span> </em>Notwithstanding the existence of probable cause, a search for evidence of a crime may be unjustifiable if it endangers the life or health of the suspect.<footnotemark>4</footnotemark></p>
<p id="b817-6">Another factor is the extent of intrusion upon the individual’s dignitary interests in personal privacy and bodily integrity. Intruding into an individual’s living room, see <em>Payton </em><page-number citation-index="1" label="762">*762</page-number>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980), eavesdropping upon an individual’s telephone conversations, see <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S., at 361</a></span>, or forcing an individual to accompany police officers to the police station, see <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979), typically do not injure the physical person of the individual. Such intrusions do, however, damage the individual’s sense of personal privacy and security and are thus subject to the Fourth Amendment’s dictates. In noting that a blood test was “a commonplace in these days of periodic physical examinations,” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#771" aria-description="Citation for case: Schmerber v. California">384 U. S., at 771</a></span>, <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>recognized society’s judgment that blood tests do not constitute an unduly extensive imposition on an individual’s personal privacy and bodily integrity.<footnotemark>6</footnotemark></p>
<p id="b818-5">Weighed against these individual interests is the community’s interest in fairly and accurately determining guilt or innocence. This interest is of course of great importance. We noted in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>that a blood test is “a highly effective means of determining the degree to which a person is under the influence of alcohol.” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#771" aria-description="Citation for case: Schmerber v. California"><em>Id., </em>at 771</a></span>. Moreover, there was “a clear indication that in fact [desired] evidence [would] be found” if the blood test were undertaken. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California"><em>Id., </em>at 770</a></span>. <page-number citation-index="1" label="763">*763</page-number>Especially given the difficulty of proving drunkenness by other means, these considerations showed that results of the blood test were of vital importance if the State were to enforce its drunken driving laws. In <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>, </em>we concluded that this state interest was sufficient to justify the intrusion, and the compelled blood test was thus “reasonable” for Fourth Amendment purposes.</p>
<p id="ASd">HH H-1</p>
<p id="Aah">Applying the <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>balancing test in this case, we believe that the Court of Appeals reached the correct result. The Commonwealth plainly had probable cause to conduct the search. In addition, all parties apparently agree that respondent has had a full measure of procedural protections and has been able fully to litigate the difficult medical and legal questions necessarily involved in analyzing the reasonableness of a surgical incision of this magnitude.<footnotemark>6</footnotemark> Our inquiry therefore must focus on the extent of the intrusion on respondent’s privacy interests and on the State’s need for the evidence.</p>
<p id="AoZB">The threats to the health or safety of respondent posed by the surgery are the subject of sharp dispute between the parties. Before the new revelations of October 18, the District Court found that the procedure could be carried out “with virtually no risk to [respondent].” <span class="citation" data-id="2365879"><a href="/opinion/2365879/lee-v-winston/#252" aria-description="Citation for case: Lee v. Winston">551 F. Supp., at 252</a></span>. On rehearing, however, with new evidence before it, the District Court held that “the risks previously involved have increased in magnitude even as new risks are being added.” <span class="citation" data-id="2365879"><a href="/opinion/2365879/lee-v-winston/#260" aria-description="Citation for case: Lee v. Winston"><em>Id., </em>at 260</a></span>.</p>
<p id="APqF">The Court of Appeals examined the medical evidence in the record and found that respondent would suffer some risks <page-number citation-index="1" label="764">*764</page-number>associated with the surgical procedure.<footnotemark>7</footnotemark> One surgeon had testified that the difficulty of discovering the exact location of the bullet “could require extensive probing and retracting of the muscle tissue,” carrying with it “the concomitant risks of injury to the muscle as well as injury to the nerves, blood vessels and other tissue in the chest and pleural cavity.” <span class="citation" data-id="9471202"><a href="/opinion/424900/rudolph-lee-jr-v-andrew-j-winston-sheriff-aubrey-m-davis-jr-and/#900" aria-description="Citation for case: Rudolph Lee, Jr. v. Andrew J. Winston, Sheriff Aubrey M....">717 F. 2d, at 900</a></span>. The court further noted that “the greater intrusion and the larger incisions increase the risks of infection.” <em><span class="citation" data-id="9471202"><a href="/opinion/424900/rudolph-lee-jr-v-andrew-j-winston-sheriff-aubrey-m-davis-jr-and/" aria-description="Citation for case: Rudolph Lee, Jr. v. Andrew J. Winston, Sheriff Aubrey M....">Ibid.</a></span> </em>Moreover, there was conflict in the testimony concerning the nature and the scope of the operation. One surgeon stated that it would take 15-20 minutes, while another predicted the procedure could take up to two and one-half hours. <em><span class="citation" data-id="9471202"><a href="/opinion/424900/rudolph-lee-jr-v-andrew-j-winston-sheriff-aubrey-m-davis-jr-and/" aria-description="Citation for case: Rudolph Lee, Jr. v. Andrew J. Winston, Sheriff Aubrey M....">Ibid.</a></span> </em>The court properly took the resulting uncertainty about the medical risks into account.<footnotemark>8</footnotemark></p>
<p id="b820-5">Both lower courts in this case believed that the proposed surgery, which for purely medical reasons required the use of a general anesthetic,<footnotemark>9</footnotemark> would be an “extensive” intrusion on respondent’s personal privacy and bodily integrity. <em><span class="citation" data-id="9471202"><a href="/opinion/424900/rudolph-lee-jr-v-andrew-j-winston-sheriff-aubrey-m-davis-jr-and/" aria-description="Citation for case: Rudolph Lee, Jr. v. Andrew J. Winston, Sheriff Aubrey M....">Ibid.</a></span> </em><page-number citation-index="1" label="765">*765</page-number>When conducted with the consent of the patient, surgery-requiring general anesthesia is not necessarily demeaning or intrusive. In such a case, the surgeon is carrying out the patient’s own will concerning the patient’s body and the patient’s right to privacy is therefore preserved. In this case, however, the Court of Appeals noted that the Commonwealth proposes to take control of respondent’s body, to “drug this citizen — not yet convicted of a criminal offense— with narcotics and barbiturates into a state of unconsciousness,” <span class="citation" data-id="9471202"><a href="/opinion/424900/rudolph-lee-jr-v-andrew-j-winston-sheriff-aubrey-m-davis-jr-and/#901" aria-description="Citation for case: Rudolph Lee, Jr. v. Andrew J. Winston, Sheriff Aubrey M...."><em>id., </em>at 901</a></span>, and then to search beneath his skin for evidence of a crime. This kind of surgery involves a virtually total divestment of respondent’s ordinary control over surgical probing beneath his skin.</p>
<p id="b821-5">The other part of the balance concerns the Commonwealth’s need to intrude into respondent’s body to retrieve the bullet. The Commonwealth claims to need the bullet to demonstrate that it was fired from Watkinson’s gun, which in turn would show that respondent was the robber who confronted Wat-kinson. However, although we recognize the difficulty of making determinations in advance as to the strength of the case against respondent, petitioners’ assertions of a compelling need for the bullet are hardly persuasive. The very circumstances relied on in this case to demonstrate probable cause to believe that evidence will be found tend to vitiate the Commonwealth’s need to compel respondent to undergo surgery. The Commonwealth has available substantial additional evidence that respondent was the individual who accosted Watkinson on the night of the robbery. No party in this case suggests that Watkinson’s entirely spontaneous identification of respondent at the hospital would be inadmissible. In addition, petitioners can no doubt prove that Wat-kinson was found a few blocks from Watkinson’s store shortly after the incident took place. And petitioners can certainly show that the location of the bullet (under respondent’s left collarbone) seems to correlate with Watkinson’s report that the robber “jerked” to the left. App. 13. The fact that the <page-number citation-index="1" label="766">*766</page-number>Commonwealth has available such substantial evidence of the origin of the bullet restricts the need for the Commonwealth to compel respondent to undergo the contemplated surgery.<footnotemark>10</footnotemark></p>
<p id="b822-5">In weighing the various factors in this case, we therefore reach the same conclusion as the courts below. The operation sought will intrude substantially on respondent’s protected interests. The medical risks of the operation, although apparently not extremely severe, are a subject of considerable dispute; the very uncertainty militates against finding the operation to be “reasonable.” In addition, the intrusion on respondent’s privacy interests entailed by the operation can only be characterized as severe. On the other hand, although the bullet may turn out to be useful to the Commonwealth in prosecuting respondent, the Commonwealth has failed to demonstrate a compelling need for it. We believe that in these circumstances the Commonwealth has failed to demonstrate that it would be “reasonable” under the terms of the Fourth Amendment to search for evidence of this crime by means of the contemplated surgery.</p>
<p id="AdA"><page-number citation-index="1" label="767">*767</page-number>P&gt; I — I</p>
<p id="AKD">The Fourth Amendment is a vital safeguard of the right of the citizen to be free from unreasonable governmental intrusions into any area in which he has a reasonable expectation of privacy. Where the Court has found a lesser expectation of privacy, see, <em>e. g., Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978); <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span> (1976), or where the search involves a minimal intrusion on privacy interests, see, <em>e. g., United States </em>v. <em>Hensley, </em><span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/" aria-description="Citation for case: United States v. Hensley">469 U. S. 221</a></span> (1985); <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#210" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 210-211</a></span>; <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#880" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 880</a></span> (1975); <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span> (1972); <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), the Court has held that the Fourth Amendment’s protections are correspondingly less stringent. Conversely, however, the Fourth Amendment’s command that searches be “reasonable” requires that when the State seeks to intrude upon an area in which our society recognizes a significantly heightened privacy interest, a more substantial justification is required to make the search “reasonable.” Applying these principles, we hold that the proposed search in this case would be “unreasonable” under the Fourth Amendment.</p>
<p id="AoFc">
<em>Affirmed.</em>
</p>
<judges id="AFD">Justice Blackmun and Justice Rehnquist concur in the judgment.</judges>
<footnote label="1">
<p id="b813-6"> Respondent’s action in the District Court was styled as a petition for habeas corpus and an action under <span class="citation no-link">42 U. S. C. § 1983</span> for a preliminary injunction. Because the District Court denied the relief sought, it found it unnecessary to consider whether res judicata, see <em>Allen </em>v. <em>McCurry, </em><span class="citation" data-id="9428105"><a href="/opinion/110360/allen-v-mccurry/" aria-description="Citation for case: Allen v. McCurry">449 U. S. 90</a></span> (1980), would bar consideration of the § 1983 claim. 551F. Supp., at 252, n. 4.</p>
</footnote>
<footnote label="2">
<p id="b813-7"> Respondent had moved to reopen the petition for habeas corpus, as well as to alter or amend the judgment. Petitioners moved to dismiss the petition for habeas on the ground that respondent was not at that time “in custody” for purposes of <span class="citation no-link">28 U. S. C. § 2241</span>. The District Court rejected this contention, holding that habeas was available because respondent was <page-number citation-index="1" label="758">*758</page-number>objecting to a <em>future </em>custody that would take place when the operation was to be performed. <span class="citation" data-id="2365879"><a href="/opinion/2365879/lee-v-winston/#257" aria-description="Citation for case: Lee v. Winston">551 F. Supp., at 257-259</a></span>. The Court of Appeals held that respondent’s claim was cognizable only under § 1983. <span class="citation" data-id="9471202"><a href="/opinion/424900/rudolph-lee-jr-v-andrew-j-winston-sheriff-aubrey-m-davis-jr-and/#893" aria-description="Citation for case: Rudolph Lee, Jr. v. Andrew J. Winston, Sheriff Aubrey M....">717 F. 2d 888, 893</a></span> (1983). Respondent has not cross-petitioned for review of this holding, and it is therefore not before us.</p>
</footnote>
<footnote label="3">
<p id="b814-9"> The Fourth Circuit held that <em>Allen </em>v. <em><span class="citation" data-id="9428105"><a href="/opinion/110360/allen-v-mccurry/" aria-description="Citation for case: Allen v. McCurry">McCurry, supra,</a></span> </em>did not bar respondent’s attempt to relitigate in federal court the same Fourth Amendment issues previously litigated in state court. The court agreed with the District Court’s conclusion, see <span class="citation" data-id="2365879"><a href="/opinion/2365879/lee-v-winston/#258" aria-description="Citation for case: Lee v. Winston">551 F. Supp., at 258-259</a></span>, that respondent had not had a full and fair opportunity to litigate in the state trial court. <span class="citation" data-id="9471202"><a href="/opinion/424900/rudolph-lee-jr-v-andrew-j-winston-sheriff-aubrey-m-davis-jr-and/#895" aria-description="Citation for case: Rudolph Lee, Jr. v. Andrew J. Winston, Sheriff Aubrey M....">717 F. 2d, at 895-899</a></span>. Respondent filed his motion for rehearing in state court on October 18, the day he was informed of the changed circumstances regarding the removal of the bullet. On October 19, the state court ordered an evidentiary hearing to be held on October 21. The Court of Appeals was “satisfied from the record that counsel was not able, despite obviously diligent effort, to obtain an independent review of the medical record by outside physicians nor was he able to consult with the independent expert in anesthesiology in order to prepare a presentation on the risks of general anesthesia.” <span class="citation" data-id="9471202"><a href="/opinion/424900/rudolph-lee-jr-v-andrew-j-winston-sheriff-aubrey-m-davis-jr-and/#897" aria-description="Citation for case: Rudolph Lee, Jr. v. Andrew J. Winston, Sheriff Aubrey M...."><em>Id., </em>at 897</a></span>. Yet, despite the crucial nature of the medical evidence, the state court refused to grant respondent’s repeated request for a continuance. Because “[t]he arbitrary truncation of preparation time deprived [respondent] of a fair opportunity to determine the crucial factors relevant to his claim and to obtain independent expert witnesses to testify about those factors,” <span class="citation" data-id="9471202"><a href="/opinion/424900/rudolph-lee-jr-v-andrew-j-winston-sheriff-aubrey-m-davis-jr-and/#898" aria-description="Citation for case: Rudolph Lee, Jr. v. Andrew J. Winston, Sheriff Aubrey M...."><em>id., </em>at 898-899</a></span>, the Court of Appeals refused to grant preclusive effect to the state court’s findings. Petitioners do not challenge this ruling.</p>
</footnote>
<footnote label="4">
<p id="b817-7"><em> </em>Numerous courts have recognized the crucial importance of this factor. See, <em>e. g., Bowden </em>v. <em>State, </em><span class="citation" data-id="1672565"><a href="/opinion/1672565/bowden-v-state/#823" aria-description="Citation for case: Bowden v. State">256 Ark. 820, 823</a></span>, <span class="citation" data-id="1672565"><a href="/opinion/1672565/bowden-v-state/#882" aria-description="Citation for case: Bowden v. State">510 S. W. 2d 879, 882</a></span> (1974) (refusing to order surgery because of medical risk); <em>People </em>v. <em>Smith, </em><span class="citation" data-id="6195999"><a href="/opinion/6327461/people-v-smith/" aria-description="Citation for case: People v. Smith">80 Misc. 2d 210</a></span>, 362 N. Y. S. 2d 909 (1974) (same); <em>State </em>v. <em>Allen, </em>277 S. C. 595, <span class="citation" data-id="1332724"><a href="/opinion/1332724/state-v-allen/" aria-description="Citation for case: State v. Allen">291 S. E. 2d 459</a></span> (1982) (same); see also <span class="citation" data-id="9471202"><a href="/opinion/424900/rudolph-lee-jr-v-andrew-j-winston-sheriff-aubrey-m-davis-jr-and/#900" aria-description="Citation for case: Rudolph Lee, Jr. v. Andrew J. Winston, Sheriff Aubrey M....">717 F. 2d 888, 900</a></span> (CA4 1983) (case below); <span class="citation" data-id="9471202"><a href="/opinion/424900/rudolph-lee-jr-v-andrew-j-winston-sheriff-aubrey-m-davis-jr-and/#905" aria-description="Citation for case: Rudolph Lee, Jr. v. Andrew J. Winston, Sheriff Aubrey M...."><em>id., </em>at 905-908</a></span> (Widener, J., dissenting); <em>United States </em>v. <em>Crowder, </em>177 U. S. App. D. C. 165, 169, <span class="citation" data-id="9463171"><a href="/opinion/339793/united-states-v-james-l-crowder/#316" aria-description="Citation for case: United States v. James L. Crowder">543 F. 2d 312, 316</a></span> (1976) (en banc), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./429/1062/">429 U. S. 1062</a></span> (1977); <em>State </em>v. <em>Overstreet, </em><span class="citation" data-id="9858704"><a href="/opinion/1784735/state-v-overstreet/#628" aria-description="Citation for case: State v. Overstreet">551 S. W. 2d 621, 628</a></span> (Mo. 1977) (en banc). See generally Note, <span class="citation no-link">68 Marq. L. Rev. 130</span>, 135 (1984) (discussing cases involving bodily intrusions); Note, <span class="citation no-link">60 Notre Dame L. Rev. 149</span>, 152-156 (1984) (same); Note, 55 Texas L. Rev. 147 (1976) (same); Mandell &amp; Richardson, Surgical Search: Removing a Scar on the Fourth Amendment, 75 J. Crim. L. <em>&amp; </em>C., No. 3, p. 525 (1984).</p>
</footnote>
<footnote label="6">
<p id="b818-6"> See also <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>, </em>384 U.S, at 771, n. 13 (‘“The blood test procedure has become routine in our everyday life. It is a ritual for those going into the military service as well as those applying for marriage licenses. Many colleges require such tests before permitting entrance and literally millions of us have voluntarily gone through the same, though a longer, routine in becoming blood donors’ ”) (quoting <em>Breithaupt </em>v. <em>Abram, </em><span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#436" aria-description="Citation for case: Breithaupt v. Abram">352 U. S. 432, 436</a></span> (1957)). The degree of intrusion in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>was minimized as well by the fact that a blood test “involves virtually no risk, trauma, or pain,” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#771" aria-description="Citation for case: Schmerber v. California">384 U. S., at 771</a></span>, and by the fact that the blood test was conducted “in a hospital environment according to accepted medical practices.” <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Ibid.</a></span> </em>As such, the procedure in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>contrasted sharply with the practice in <em>Rochin </em>v. <em>California, </em><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952), in which police officers broke into a suspect’s room, attempted to extract narcotics capsules he had put into his mouth, took him to a hospital, and directed that an emetic be administered to induce vomiting. <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#166" aria-description="Citation for case: Rochin v. California"><em>Id., </em>at 166</a></span>. <em><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span>, </em>recognizing the individual’s interest in “human dignity,” <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#174" aria-description="Citation for case: Rochin v. California"><em>id., </em>at 174</a></span>, held the search and seizure unconstitutional under the Due Process Clause.</p>
</footnote>
<footnote label="6">
<p id="A_a"> Because the State has afforded respondent the benefit of a full adversary presentation and appellate review, we do not reach the question whether the State may compel a suspect to undergo a surgical search of this magnitude for evidence absent such special procedural protections. Cf. <em>United States </em>v. <span class="citation" data-id="9463171"><a href="/opinion/339793/united-states-v-james-l-crowder/#169" aria-description="Citation for case: United States v. James L. Crowder"><em>Crowder, supra, </em>at 169</a></span>, 643 F. 2d, at 316; <em>State </em>v. <em>Lawson, </em>187 N. J. Super. 25, 28-29, <span class="citation" data-id="1948196"><a href="/opinion/1948196/state-v-lawson/#558" aria-description="Citation for case: State v. Lawson">453 A. 2d 556, 558</a></span> (App. Div. 1982).</p>
</footnote>
<footnote label="7">
<p id="b820-6"> The Court of Appeals concluded, however, that “the specific physical risks from putting [respondent] under general anesthesia may therefore be considered minimal.” <span class="citation" data-id="9471202"><a href="/opinion/424900/rudolph-lee-jr-v-andrew-j-winston-sheriff-aubrey-m-davis-jr-and/#900" aria-description="Citation for case: Rudolph Lee, Jr. v. Andrew J. Winston, Sheriff Aubrey M....">717 F. 2d, at 900</a></span>. Testimony had shown that “the general risks of harm or death from general anesthesia are quite low, and that [respondent] was in the statistical group of persons with the lowest risk of injury from general anesthesia.” <em><span class="citation" data-id="9471202"><a href="/opinion/424900/rudolph-lee-jr-v-andrew-j-winston-sheriff-aubrey-m-davis-jr-and/" aria-description="Citation for case: Rudolph Lee, Jr. v. Andrew J. Winston, Sheriff Aubrey M....">Ibid.</a></span></em></p>
</footnote>
<footnote label="8">
<p id="b820-7"> One expert testified that this would be “minor” surgery. See App. 99. The question whether the surgery is to be characterized in medical terms as “major” or “minor” is not controlling. We agree with the Court of Appeals and the District Court in this case that “there is no reason to suppose that the definition of a medical term of art should coincide with the parameters of a constitutional standard.” <span class="citation" data-id="2365879"><a href="/opinion/2365879/lee-v-winston/#260" aria-description="Citation for case: Lee v. Winston">551 F. Supp., at 260</a></span> (quoted at <span class="citation" data-id="9471202"><a href="/opinion/424900/rudolph-lee-jr-v-andrew-j-winston-sheriff-aubrey-m-davis-jr-and/#901" aria-description="Citation for case: Rudolph Lee, Jr. v. Andrew J. Winston, Sheriff Aubrey M....">717 F. 2d, at 901</a></span>); accord, <em>State </em>v. <em>Overstreet, </em><span class="citation" data-id="9858704"><a href="/opinion/1784735/state-v-overstreet/#628" aria-description="Citation for case: State v. Overstreet">551 S. W. 2d, at 628</a></span>. This does not mean that the application of medical concepts in such cases is to be ignored. However, no specific medical categorization can control the multifaceted legal inquiry that the court must undertake.</p>
</footnote>
<footnote label="9">
<p id="b820-8"> Somewhat different issues would be raised if the use of a general anesthetic became necessary because of the patient’s refusal to cooperate. Cf. <em>State </em>v. <em><span class="citation" data-id="1948196"><a href="/opinion/1948196/state-v-lawson/" aria-description="Citation for case: State v. Lawson">Lawson, supra.</a></span></em></p>
</footnote>
<footnote label="10">
<p id="b822-6"> There are also some questions concerning the probative value of the bullet, even if it could be retrieved. The evidentiary value of the bullet depends on a comparison between markings, if any, on the bullet in respondent’s shoulder and markings, if any, found on a test bullet that the police could fire from Watkinson’s gun. However, the record supports some doubt whether this kind of comparison is possible. This is because the bullet’s markings may have been corroded in the time that the bullet has been in respondent’s shoulder, thus making it useless for comparison purposes. See <span class="citation" data-id="9471202"><a href="/opinion/424900/rudolph-lee-jr-v-andrew-j-winston-sheriff-aubrey-m-davis-jr-and/#901" aria-description="Citation for case: Rudolph Lee, Jr. v. Andrew J. Winston, Sheriff Aubrey M....">717 F. 2d, at 901, n. 15</a></span>. In addition, respondent argues that any given gun may be incapable of firing bullets that have a consistent set of markings. See Joling, An Overview of Firearms Identification Evidence for Attorneys I: Salient Features of Firearms Evidence, 26 J. Forensic Sci. 153, 154 (1981). The record is devoid of any evidence that the police have attempted to test-fire Watkinson’s gun, and there thus remains the additional possibility that a comparison of bullets is impossible because Watkinson’s gun does not consistently fire bullets with the same markings. However, because the courts below made no findings on this point, we hesitate to give it significant weight in our analysis.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Wolf v. Colorado.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Wolf v. Colorado"
type: case
citation: "338 U.S. 25 (1949)"
parallel_cite: "69 S. Ct. 1359; 93 L. Ed. 2d 1782; 93 L. Ed. 1782"
neutral_cite: 1949 U.S. LEXIS 2079
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1949
date_decided: 1949-06-27
docket: "17, 18"
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: superseded
  as_of_content: 1949-06-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Wolf v. Colorado
  varies_by_point: false
  scope_note: "Wolf's holding that the Fourteenth Amendment does not require the exclusionary rule of the States was overruled on that remedy point by Mapp v. Ohio (1961). Wolf's separate holding incorporating the Fourth Amendment's core against the States survived and was reaffirmed in Mapp."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/104709/wolf-v-colorado/"
  cluster_id: 104709
  opinion_id: 104709
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Historical (overruled by Mapp on remedy)"
related: ["[[Mapp v. Ohio]]", "[[Weeks v. United States]]", "[[Elkins v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "incorporation", "fourteenth-amendment", "overruled", "historical"]
holding: "The Fourth Amendment's core security against arbitrary police intrusion is enforceable against the States through the Fourteenth Amendment's Due Process Clause, but the Weeks exclusionary rule is not itself commanded of the States — a remedy holding later overruled by Mapp v. Ohio."
lake:
  record_id: Wolf v. Colorado
  status: verified
  projected_at: 2026-07-09
---

# Wolf v. Colorado

*338 U.S. 25 (1949)* · U.S. Supreme Court · **Historical** · Treatment: **overruled** *(as of 2026-06-30)* — overruled on remedy by [[Mapp v. Ohio]]
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Wolf was convicted in a Colorado court of conspiracy to commit abortion on evidence (including an appointment book) obtained by a sheriff without a warrant. He argued that the Fourteenth Amendment required a state court to exclude evidence obtained by an unreasonable search and seizure, just as *[[Weeks v. United States]]* required exclusion in federal prosecutions.

## Issue
Whether the Due Process Clause of the Fourteenth Amendment requires a state court to exclude evidence obtained by an unreasonable search and seizure, as the *[[Weeks v. United States|Weeks]]* rule requires in federal court.

## Rule
The Fourth Amendment's core is binding on the States, but its federal exclusionary remedy is not. "The security of one's privacy against arbitrary intrusion by the police—which is at the core of the Fourth Amendment—is basic to a free society. It is therefore implicit in 'the concept of ordered liberty' and as such enforceable against the States through the Due Process Clause." — 338 U.S. at 27–28. ^pin-27

But the *[[Weeks v. United States|Weeks]]* exclusionary rule was a judicially implied remedy, not a constitutional command on the States: "in a prosecution in a State court for a State crime the Fourteenth Amendment does not forbid the admission of evidence obtained by an unreasonable search and seizure." — [*Id.* at 33](https://www.courtlistener.com/opinion/104709/wolf-v-colorado/#:~:text=in%20a%20prosecution%20in%20a). ^pin-33

**This remedy holding was overruled by [[Mapp v. Ohio]] (1961).**

## Application
Because exclusion was an implied federal remedy rather than an essential ingredient of the right enforceable against the States, the Court left the States free to choose other means of enforcing the constitutional guarantee. Colorado's admission of the unlawfully obtained evidence therefore did not deny Wolf due process of law.

## Conclusion
The conviction was affirmed: the Fourteenth Amendment incorporated the substance of the Fourth Amendment against the States but did not, in 1949, compel them to apply the exclusionary rule. **The Court reversed course twelve years later in [[Mapp v. Ohio]], which extended the exclusionary rule to the States and overruled this part of *Wolf*.**

## Treatment & subsequent history
- **Status:** overruled *(as of 2026-06-30)* — **Historical** (tier 6). **Overruled on the remedy holding by [[Mapp v. Ohio]], 367 U.S. 643 (1961)**, which held the exclusionary rule applicable to the States.
- *Wolf*'s incorporation holding — that the Fourth Amendment's core binds the States through the Fourteenth — **survived** and was reaffirmed in *[[Mapp v. Ohio|Mapp]]*. *Wolf* is taught as the foil for the modern rule: it is the case instructors name to explain how *[[Mapp v. Ohio|Mapp]]* came to require state exclusion. Compare [[Elkins v. United States]] (abolishing the silver-platter doctrine the year before *[[Mapp v. Ohio|Mapp]]*).

## Appears on
- [[The Exclusionary Rule]] — *Key — Historical (overruled by Mapp on remedy)*

## Sources
- *Wolf v. Colorado*, 338 U.S. 25 (1949) — https://www.courtlistener.com/opinion/104709/wolf-v-colorado/ — pinpoints: 27–28, 33.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6df33aea3c9e3644", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Wolf v. Colorado"}, "payload": {"all": [{"cite": "338 U.S. 25", "page": "25", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "338"}, {"cite": "69 S. Ct. 1359", "page": "1359", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "69"}, {"cite": "93 L. Ed. 2d 1782", "page": "1782", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "93"}, {"cite": "1949 U.S. LEXIS 2079", "page": "2079", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1949"}, {"cite": "93 L. Ed. 1782", "page": "1782", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "93"}], "display": "338 U.S. 25", "official": {"cite": "338 U.S. 25", "page": "25", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "338"}, "official_selection_present": true, "record_id": "Wolf v. Colorado"}}
{"assertion_id": "8f8e97341488af46", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-33", "record_id": "Wolf v. Colorado"}, "payload": {"fragment": "#:~:text=in%20a%20prosecution%20in%20a", "page": null, "pin_id": "pin-33", "pinpoint_status": "star-verified", "quote": "in a prosecution in a State court for a State crime the Fourteenth Amendment does not forbid the admission of evidence obtained by an unreasonable search and seizure.", "quote_fidelity": "matched", "record_id": "Wolf v. Colorado", "star_marker": "33"}}
{"assertion_id": "d258a00b10f0ee45", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-27", "record_id": "Wolf v. Colorado"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-27", "pinpoint_status": "slip-only", "quote": "--- # Wolf v. Colorado *338 U.S. 25 (1949)* · U.S. Supreme Court · **Historical** · Treatment: **overruled** *(as of 2026-06-30)* — overruled on remedy by [[Mapp v. Ohio]] <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Wolf was convicted in a Colorado court of conspiracy to commit abortion on evidence (including an appointment book) obtained by a sheriff without a warrant. He argued that the Fourteenth Amendment required a state court to exclude evidence obtained by an unreasonable search and seizure, just as *Weeks v. United States* required exclusion in federal prosecutions. ## Issue Whether the Due Process Clause of the Fourteenth Amendment requires a state court to exclude evidence obtained by an unreasonable search and seizure, as the *Weeks* rule requires in federal court. ## Rule The Fourth Amendment's core is binding on the States, but its federal exclusionary remedy is not.", "quote_fidelity": "mismatch", "record_id": "Wolf v. Colorado", "star_marker": null}}
{"assertion_id": "8196867a9a012434", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Wolf v. Colorado"}, "payload": {"as_of_content": "1949-06-27", "as_of_treatment": "2026-06-30", "field_i_validity": "superseded", "record_id": "Wolf v. Colorado", "scope_note": "Wolf's holding that the Fourteenth Amendment does not require the exclusionary rule of the States was overruled on that remedy point by Mapp v. Ohio (1961). Wolf's separate holding incorporating the Fourth Amendment's core against the States survived and was reaffirmed in Mapp.", "varies_by_point": false}}
```

### lake record — Wolf v. Colorado

```json
{
  "schema_version": "s2.v1",
  "record_id": "Wolf v. Colorado",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Wolf v. Colorado",
    "case_name_short": "Wolf",
    "case_name_full": "Wolf v. Colorado",
    "input_case_name": "Wolf v. Colorado",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1949-06-27",
    "year": 1949,
    "docket": "17, 18",
    "cluster_id": 104709,
    "lead_opinion_id": 104709,
    "sibling_ids": [
      104709,
      9420374,
      9420375,
      9420376,
      9420377,
      9420378
    ],
    "absolute_url": "/opinion/104709/wolf-v-colorado/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "338 U.S. 25",
      "volume": "338",
      "reporter": "U.S.",
      "page": "25",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "69 S. Ct. 1359",
        "volume": "69",
        "reporter": "S. Ct.",
        "page": "1359",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 1782",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "1782",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 1782",
        "volume": "93",
        "reporter": "L. Ed.",
        "page": "1782",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1949 U.S. LEXIS 2079",
        "volume": "1949",
        "reporter": "U.S. LEXIS",
        "page": "2079",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "338 U.S. 25",
        "volume": "338",
        "reporter": "U.S.",
        "page": "25",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 S. Ct. 1359",
        "volume": "69",
        "reporter": "S. Ct.",
        "page": "1359",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 1782",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "1782",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1949 U.S. LEXIS 2079",
        "volume": "1949",
        "reporter": "U.S. LEXIS",
        "page": "2079",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 1782",
        "volume": "93",
        "reporter": "L. Ed.",
        "page": "1782",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "338 U.S. 25",
    "official_selection": {
      "court_class": "scotus",
      "selected": "338 U.S. 25",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-27",
      "page": null,
      "quote": "--- # Wolf v. Colorado *338 U.S. 25 (1949)* \u00b7 U.S. Supreme Court \u00b7 **Historical** \u00b7 Treatment: **overruled** *(as of 2026-06-30)* \u2014 overruled on remedy by [[Mapp v. Ohio]] <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Wolf was convicted in a Colorado court of conspiracy to commit abortion on evidence (including an appointment book) obtained by a sheriff without a warrant. He argued that the Fourteenth Amendment required a state court to exclude evidence obtained by an unreasonable search and seizure, just as *Weeks v. United States* required exclusion in federal prosecutions. ## Issue Whether the Due Process Clause of the Fourteenth Amendment requires a state court to exclude evidence obtained by an unreasonable search and seizure, as the *Weeks* rule requires in federal court. ## Rule The Fourth Amendment's core is binding on the States, but its federal exclusionary remedy is not.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-33",
      "page": null,
      "quote": "in a prosecution in a State court for a State crime the Fourteenth Amendment does not forbid the admission of evidence obtained by an unreasonable search and seizure.",
      "star_marker": "33",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 16043,
      "fragment": "#:~:text=in%20a%20prosecution%20in%20a",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "superseded",
    "as_of_content": "1949-06-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Wolf v. Colorado",
    "varies_by_point": false,
    "scope_note": "Wolf's holding that the Fourteenth Amendment does not require the exclusionary rule of the States was overruled on that remedy point by Mapp v. Ohio (1961). Wolf's separate holding incorporating the Fourth Amendment's core against the States survived and was reaffirmed in Mapp.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Mapp v. Ohio",
          "cluster_id": 106285,
          "cite": "367 U.S. 643",
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:overruled"
      },
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
        "journal_ref": "Wolf v. Colorado:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rauf v. State",
          "cluster_id": 4243712,
          "cite": [
            "145 A.3d 430",
            "2016 Del. LEXIS 419",
            "2016 WL 4224252"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane1_negative"
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
        "journal_ref": "Wolf v. Colorado:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Armendariz v. State",
          "cluster_id": 1495683,
          "cite": [
            "123 S.W.3d 401",
            "2003 Tex. Crim. App. LEXIS 924",
            "2003 WL 22902856"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Munroe v. Zoning Board of Appeals",
          "cluster_id": 7899534,
          "cite": [
            "261 Conn. 263",
            "802 A.2d 55",
            "2002 Conn. LEXIS 298"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gary Lynn Weaver",
          "cluster_id": 729642,
          "cite": [
            "99 F.3d 1372",
            "1996 WL 648108"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hatcher v. State",
          "cluster_id": 2449969,
          "cite": [
            "916 S.W.2d 643",
            "1996 WL 46937"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 1676406,
          "cite": [
            "912 S.W.2d 227",
            "1995 Tex. Crim. App. LEXIS 115",
            "1995 WL 675559"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane1_negative"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Katz v. United States",
          "cluster_id": 107564,
          "cite": [
            "19 L. Ed. 2d 576",
            "88 S. Ct. 507",
            "389 U.S. 347",
            "1967 U.S. LEXIS 2"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Franks v. Delaware",
          "cluster_id": 109925,
          "cite": [
            "57 L. Ed. 2d 667",
            "98 S. Ct. 2674",
            "438 U.S. 154",
            "1978 U.S. LEXIS 127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gideon v. Wainwright",
          "cluster_id": 106545,
          "cite": [
            "9 L. Ed. 2d 799",
            "83 S. Ct. 792",
            "372 U.S. 335",
            "1963 U.S. LEXIS 1942",
            "93 A.L.R. 2d 733",
            "23 Ohio Op. 2d 258"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spinelli v. United States",
          "cluster_id": 107831,
          "cite": [
            "21 L. Ed. 2d 637",
            "89 S. Ct. 584",
            "393 U.S. 410",
            "1969 U.S. LEXIS 2701"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schmerber v. California",
          "cluster_id": 107262,
          "cite": [
            "16 L. Ed. 2d 908",
            "86 S. Ct. 1826",
            "384 U.S. 757",
            "1966 U.S. LEXIS 1129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clewis v. State",
          "cluster_id": 2462780,
          "cite": [
            "922 S.W.2d 126",
            "1996 Tex. Crim. App. LEXIS 11",
            "1996 WL 37908"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Monroe v. Pape",
          "cluster_id": 106170,
          "cite": [
            "5 L. Ed. 2d 492",
            "81 S. Ct. 473",
            "365 U.S. 167",
            "1961 U.S. LEXIS 1687"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pointer v. Texas",
          "cluster_id": 107014,
          "cite": [
            "13 L. Ed. 2d 923",
            "85 S. Ct. 1065",
            "380 U.S. 400",
            "1965 U.S. LEXIS 1481"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griswold v. Connecticut",
          "cluster_id": 107082,
          "cite": [
            "14 L. Ed. 2d 510",
            "85 S. Ct. 1678",
            "381 U.S. 479",
            "1965 U.S. LEXIS 2282"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stone v. Powell",
          "cluster_id": 109540,
          "cite": [
            "49 L. Ed. 2d 1067",
            "96 S. Ct. 3037",
            "428 U.S. 465",
            "1976 U.S. LEXIS 86"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fay v. Noia",
          "cluster_id": 106548,
          "cite": [
            "9 L. Ed. 2d 837",
            "83 S. Ct. 822",
            "372 U.S. 391",
            "1963 U.S. LEXIS 1945",
            "24 Ohio Op. 2d 12"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Duncan v. Louisiana",
          "cluster_id": 107685,
          "cite": [
            "20 L. Ed. 2d 491",
            "88 S. Ct. 1444",
            "391 U.S. 145",
            "1968 U.S. LEXIS 1631",
            "45 Ohio Op. 2d 198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
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
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. O'Brien",
          "cluster_id": 107701,
          "cite": [
            "20 L. Ed. 2d 672",
            "88 S. Ct. 1673",
            "391 U.S. 367",
            "1968 U.S. LEXIS 2910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Camara v. Municipal Court of City and County of San Francisco",
          "cluster_id": 107473,
          "cite": [
            "18 L. Ed. 2d 930",
            "87 S. Ct. 1727",
            "387 U.S. 523",
            "1967 U.S. LEXIS 1254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wolf v. Colorado:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(104709 OR 9420374 OR 9420375 OR 9420376 OR 9420377 OR 9420378) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03NDM3MzEyMDAwMDAmcz0zOTU5MTYzJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28104709+OR+9420374+OR+9420375+OR+9420376+OR+9420377+OR+9420378%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(104709 OR 9420374 OR 9420375 OR 9420376 OR 9420377 OR 9420378)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDM1JnM9MTQ5NzAyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28104709+OR+9420374+OR+9420375+OR+9420376+OR+9420377+OR+9420378%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(104709 OR 9420374 OR 9420375 OR 9420376 OR 9420377 OR 9420378)",
        "reviewed": 8,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 8,
        "triage_read": 1,
        "triage_snippet_classified": 7
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(104709 OR 9420374 OR 9420375 OR 9420376 OR 9420377 OR 9420378)",
    "indexed_citing_opinions": 960,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 104709,
        "count": 890,
        "count_source": "search"
      },
      {
        "opinion_id": 9420374,
        "count": 103,
        "count_source": "search"
      },
      {
        "opinion_id": 9420375,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9420376,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9420377,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9420378,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1555,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/wolf-v-colorado.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjYzNTY5MDYmcz00NjU4OTgyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28104709+OR+9420374+OR+9420375+OR+9420376+OR+9420377+OR+9420378%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 104709,
        "cited_id": 89675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 91054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 96885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 104455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3233534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3246119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3307559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3311672,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3312462,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3314804,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3321660,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3412636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3471999,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3484807,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3487094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3529427,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3536208,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3553875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3571966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3580565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3588018,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3594947,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3646527,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3672959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3682031,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3780866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3812264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3827556,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3839135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3842073,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3848320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3870663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3907069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3932614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3977442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3980535,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 3990360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104709,
        "cited_id": 4012941,
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
    "date_created": "2026-07-06T04:41:07Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: overruled -> superseded",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:41:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:41:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:41:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Wolf v. Colorado

```
<div>
<center><b><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U.S. 25</a></span> (1949)</b></center>
<center><h1>WOLF<br>
v.<br>
COLORADO.</h1></center>
<center>Nos. 17 and 18.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 19, 1948.</center>
<center>Decided June 27, 1949.</center>
CERTIORARI TO THE SUPREME COURT OF COLORADO.
<p><i>Philip Hornbein,</i> argued the cause for petitioner. With him on the brief were <i>Philip Hornbein, Jr.</i> and <i>Donald M. Shere.</i></p>
<p><i>James S. Henderson,</i> Assistant Attorney General of Colorado, argued the cause for respondent. With him on the brief was <i>H. Lawrence Hinkley,</i> Attorney General.</p>
<p>MR. JUSTICE FRANKFURTER delivered the opinion of the Court.</p>
<p>The precise question for consideration is this: Does a conviction by a State court for a State offense deny the "due process of law" required by the Fourteenth Amendment, solely because evidence that was admitted <span class="star-pagination">*26</span> at the trial was obtained under circumstances which would have rendered it inadmissible in a prosecution for violation of a federal law in a court of the United States because there deemed to be an infraction of the Fourth Amendment as applied in <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>? The Supreme Court of Colorado has sustained convictions in which such evidence was admitted, <span class="citation no-link">117 Col. 279</span>, <span class="citation" data-id="3312462"><a href="/opinion/3317383/wolf-v-people/" aria-description="Citation for case: Wolf v. People">187 P. 2d 926</a></span>; <span class="citation no-link">117 Col. 321</span>, <span class="citation" data-id="3314804"><a href="/opinion/3319666/wolf-v-people/" aria-description="Citation for case: Wolf v. People">187 P. 2d 928</a></span>, and we brought the cases here. <span class="citation multiple-matches"><a href="/c/U.%20S./333/879/">333 U. S. 879</a></span>.</p>
<p>Unlike the specific requirements and restrictions placed by the Bill of Rights (Amendments I to VIII) upon the administration of criminal justice by federal authority, the Fourteenth Amendment did not subject criminal justice in the States to specific limitations. The notion that the "due process of law" guaranteed by the Fourteenth Amendment is shorthand for the first eight amendments of the Constitution and thereby incorporates them has been rejected by this Court again and again, after impressive consideration. See, e. g., <i>Hurtado</i> v. <i>California,</i> <span class="citation" data-id="9417375"><a href="/opinion/91054/hurtado-v-california/" aria-description="Citation for case: Hurtado v. California">110 U. S. 516</a></span>; <i>Twining</i> v. <i>New Jersey,</i> <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">211 U. S. 78</a></span>; <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span>; <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319</a></span>. Only the other day the Court reaffirmed this rejection after thorough reexamination of the scope and function of the Due Process Clause of the Fourteenth Amendment. <i>Adamson</i> v. <i>California,</i> <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/" aria-description="Citation for case: Adamson v. California">332 U. S. 46</a></span>. The issue is closed.</p>
<p>For purposes of ascertaining the restrictions which the Due Process Clause imposed upon the States in the enforcement of their criminal law, we adhere to the views expressed in <i>Palko</i> v. <i><span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/" aria-description="Citation for case: Palko v. Connecticut">Connecticut, supra,</a></span></i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319</a></span>. That decision speaks to us with the great weight of the authority, particularly in matters of civil liberty, of a court that included Mr. Chief Justice Hughes, Mr. Justice Brandeis, Mr. Justice Stone and Mr. Justice Cardozo, to name only the dead. In rejecting the suggestion that the Due Process Clause incorporated the original Bill of Rights, Mr. Justice Cardozo reaffirmed on behalf of that <span class="star-pagination">*27</span> Court a different but deeper and more pervasive conception of the Due Process Clause. This Clause exacts from the States for the lowliest and the most outcast all that is "implicit in the concept of ordered liberty." <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U. S. at 325</a></span>.</p>
<p>Due process of law thus conveys neither formal nor fixed nor narrow requirements. It is the compendious expression for all those rights which the courts must enforce because they are basic to our free society. But basic rights do not become petrified as of any one time, even though, as a matter of human experience, some may not too rhetorically be called eternal verities. It is of the very nature of a free society to advance in its standards of what is deemed reasonable and right. Representing as it does a living principle, due process is not confined within a permanent catalogue of what may at a given time be deemed the limits or the essentials of fundamental rights.</p>
<p>To rely on a tidy formula for the easy determination of what is a fundamental right for purposes of legal enforcement may satisfy a longing for certainty but ignores the movements of a free society. It belittles the scale of the conception of due process. The real clue to the problem confronting the judiciary in the application of the Due Process Clause is not to ask where the line is once and for all to be drawn but to recognize that it is for the Court to draw it by the gradual and empiric process of "inclusion and exclusion." <i>Davidson</i> v. <i>New Orleans,</i> <span class="citation" data-id="9841711"><a href="/opinion/89675/davidson-v-new-orleans/#104" aria-description="Citation for case: Davidson v. New Orleans">96 U. S. 97, 104</a></span>. This was the Court's insight when first called upon to consider the problem; to this insight the Court has on the whole been faithful as case after case has come before it since <i>Davidson</i> v. <i><span class="citation" data-id="9841711"><a href="/opinion/89675/davidson-v-new-orleans/" aria-description="Citation for case: Davidson v. New Orleans">New Orleans</a></span></i> was decided.</p>
<p>The security of one's privacy against arbitrary intrusion by the policewhich is at the core of the Fourth Amendmentis basic to a free society. It is therefore implicit in "the concept of ordered liberty" and as such enforceable against the States through the Due Process <span class="star-pagination">*28</span> Clause. The knock at the door, whether by day or by night, as a prelude to a search, without authority of law but solely on the authority of the police, did not need the commentary of recent history to be condemned as inconsistent with the conception of human rights enshrined in the history and the basic constitutional documents of English-speaking peoples.</p>
<p>Accordingly, we have no hesitation in saying that were a State affirmatively to sanction such police incursion into privacy it would run counter to the guaranty of the Fourteenth Amendment. But the ways of enforcing such a basic right raise questions of a different order. How such arbitrary conduct should be checked, what remedies against it should be afforded, the means by which the right should be made effective, are all questions that are not to be so dogmatically answered as to preclude the varying solutions which spring from an allowable range of judgment on issues not susceptible of quantitative solution.</p>
<p>In <i>Weeks</i> v. <i>United <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">States, supra</a></span></i><i>,</i> this Court held that in a federal prosecution the Fourth Amendment barred the use of evidence secured through an illegal search and seizure. This ruling was made for the first time in 1914. It was not derived from the explicit requirements of the Fourth Amendment; it was not based on legislation expressing Congressional policy in the enforcement of the Constitution. The decision was a matter of judicial implication. Since then it has been frequently applied and we stoutly adhere to it. But the immediate question is whether the basic right to protection against arbitrary intrusion by the police demands the exclusion of logically relevant evidence obtained by an unreasonable search and seizure because, in a federal prosecution for a federal crime, it would be excluded. As a matter of inherent reason, one would suppose this to be an issue as to which men with complete devotion to the protection of the right <span class="star-pagination">*29</span> of privacy might give different answers. When we find that in fact most of the English-speaking world does not regard as vital to such protection the exclusion of evidence thus obtained, we must hesitate to treat this remedy as an essential ingredient of the right. The contrariety of views of the States is particularly impressive in view of the careful reconsideration which they have given the problem in the light of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> decision.</p>
   I. Before the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> decision 27 States had passed on
       the admissibility of evidence obtained by unlawful
       search and seizure.
         (a) Of these, 26 States opposed the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine.
               (See Appendix, Table A.)
         (b) Of these, 1 State anticipated the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine.
               (Table B.)
   II. Since the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> decision 47 States all told have
         passed on the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine. (Table C.)
           (a) Of these, 20 passed on it for the first time.
                   (1) Of the foregoing States, 6 followed
                         the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine. (Table D.)
                   (2) Of the foregoing States, 14 rejected
                         the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine. (Table E.)
           (b) Of these, 26 States reviewed prior decisions
                 contrary to the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine.
                   (1) Of these, 10 States have followed
                         <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>,</i> overruling or distinguishing
                         their prior decisions. (Table
                         F.)
                   (2) Of these, 16 States adhered to their
                         prior decisions against <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>.</i>
                         (Table G.)
            (c) Of these, 1 State repudiated its prior formulation
                 of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine. (Table H.)
   III. As of today 31 States reject the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine, 16
         States are in agreement with it. (Table I.)
<span class="star-pagination">*30</span>
   IV. Of 10 jurisdictions within the United Kingdom and
        the British Commonwealth of Nations which have
        passed on the question, none has held evidence
        obtained by illegal search and seizure inadmissible.
        (Table J.)
<p>The jurisdictions which have rejected the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine have not left the right to privacy without other means of protection.<sup>[1]</sup> Indeed, the exclusion of evidence <span class="star-pagination">*31</span> is a remedy which directly serves only to protect those upon whose person or premises something incriminating has been found. We cannot, therefore, regard it as a departure from basic standards to remand such persons, together with those who emerge scatheless from a search, to the remedies of private action and such protection as the internal discipline of the police, under the eyes of an alert public opinion, may afford. Granting that in practice the exclusion of evidence may be an effective way of deterring unreasonable searches, it is not for this Court to condemn as falling below the minimal standards assured by the Due Process Clause a State's reliance upon other methods which, if consistently enforced, would be equally effective. Weighty testimony against such an insistence on our own view is furnished by the opinion of Mr. Justice (then Judge) Cardozo in <i>People</i> v. <i>Defore,</i> <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">242 N. Y. 13</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">150 N. E. 585</a></span>.<sup>[2]</sup> We cannot brush aside the experience of States which deem the incidence of such <span class="star-pagination">*32</span> conduct by the police too slight to call for a deterrent remedy not by way of disciplinary measures but by overriding the relevant rules of evidence. There are, moreover, reasons for excluding evidence unreasonably obtained by the federal police which are less compelling in the case of police under State or local authority. The public opinion of a community can far more effectively be exerted against oppressive conduct on the part of police directly responsible to the community itself than can local opinion, sporadically aroused, be brought to bear upon <span class="star-pagination">*33</span> remote authority pervasively exerted throughout the country.</p>
<p>We hold, therefore, that in a prosecution in a State court for a State crime the Fourteenth Amendment does not forbid the admission of evidence obtained by an unreasonable search and seizure. And though we have interpreted the Fourth Amendment to forbid the admission of such evidence, a different question would be presented if Congress under its legislative powers were to pass a statute purporting to negate the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine. We would then be faced with the problem of the respect to be accorded the legislative judgment on an issue as to which, in default of that judgment, we have been forced to depend upon our own. Problems of a converse character, also not before us, would be presented should Congress under § 5 of the Fourteenth Amendment undertake to enforce the rights there guaranteed by attempting to make the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine binding upon the States.</p>
<p><i>Affirmed.</i></p>
                        APPENDIX.<sup>[*]</sup>
                           TABLE A.
    STATES WHICH OPPOSED THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE BEFORE
           THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> CASE HAD BEEN DECIDED.
ALA.    <i>Shields</i> v. <i>State,</i> <span class="citation" data-id="6515773"><a href="/opinion/6639159/shields-v-state/" aria-description="Citation for case: Shields v. State">104 Ala. 35</a></span>, <span class="citation no-link">16 So. 85</span>.
ARK.    <i>Starchman</i> v. <i>State,</i> <span class="citation" data-id="6543624"><a href="/opinion/6665982/starchman-v-state/" aria-description="Citation for case: Starchman v. State">62 Ark. 538</a></span>, <span class="citation" data-id="6543624"><a href="/opinion/6665982/starchman-v-state/" aria-description="Citation for case: Starchman v. State">36 S. W. 940</a></span>.
CONN.   <i>State</i> v. <i>Griswold,</i> <span class="citation" data-id="6583651"><a href="/opinion/6703553/state-v-griswold/" aria-description="Citation for case: State v. Griswold">67 Conn. 290</a></span>, <span class="citation" data-id="6583651"><a href="/opinion/6703553/state-v-griswold/" aria-description="Citation for case: State v. Griswold">34 A. 1046</a></span>.
GA.     <i>Williams</i> v. <i>State,</i> <span class="citation" data-id="5567449"><a href="/opinion/5717379/williams-v-state/" aria-description="Citation for case: Williams v. State">100 Ga. 511</a></span>, <span class="citation" data-id="5567449"><a href="/opinion/5717379/williams-v-state/" aria-description="Citation for case: Williams v. State">28 S. E. 624</a></span>.
IDAHO   <i>State</i> v. <i>Bond,</i> <span class="citation" data-id="5169254"><a href="/opinion/5337571/state-v-bond/#439" aria-description="Citation for case: State v. Bond">12 Idaho 424, 439</a></span>, <span class="citation" data-id="5169254"><a href="/opinion/5337571/state-v-bond/#47" aria-description="Citation for case: State v. Bond">86 P. 43, 47</a></span>.
ILL.    <i>Siebert</i> v. <i>People,</i> <span class="citation" data-id="6965240"><a href="/opinion/7061242/siebert-v-people/#583" aria-description="Citation for case: Siebert v. People">143 Ill. 571, 583</a></span>, <span class="citation" data-id="6965240"><a href="/opinion/7061242/siebert-v-people/#434" aria-description="Citation for case: Siebert v. People">32 N. E. 431, 434</a></span>.
KAN.    <i>State</i> v. <i>Miller,</i> <span class="citation" data-id="7891978"><a href="/opinion/7941374/state-v-miller/" aria-description="Citation for case: State v. Miller">63 Kan. 62</a></span>, <span class="citation" data-id="7891978"><a href="/opinion/7941374/state-v-miller/" aria-description="Citation for case: State v. Miller">64 P. 1033</a></span>.
ME.     See <i>State</i> v. <i>Gorham,</i> <span class="citation" data-id="4932917"><a href="/opinion/5114261/state-v-gorham/#272" aria-description="Citation for case: State v. Gorham">65 Me. 270, 272</a></span>.
MD.     <i>Lawrence</i> v. <i>State,</i> <span class="citation" data-id="3487094"><a href="/opinion/3489145/lawrence-v-state/#35" aria-description="Citation for case: Lawrence v. State">103 Md. 17, 35</a></span>, <span class="citation" data-id="3487094"><a href="/opinion/3489145/lawrence-v-state/#103" aria-description="Citation for case: Lawrence v. State">63 A. 96, 103</a></span>.
<span class="star-pagination">*34</span>
    STATES WHICH OPPOSED THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE BEFORE
           THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> CASE HAD BEEN DECIDED.
MASS.   <i>Commonwealth</i> v. <i>Dana,</i> <span class="citation no-link">2 Metc. 329</span>.
MICH.   <i>People</i> v. <i>Aldorfer,</i> <span class="citation" data-id="7946344"><a href="/opinion/7992842/people-v-aldorfer/" aria-description="Citation for case: People v. Aldorfer">164 Mich. 676</a></span>, <span class="citation" data-id="7946344"><a href="/opinion/7992842/people-v-aldorfer/" aria-description="Citation for case: People v. Aldorfer">130 N. W. 351</a></span>.
MINN.   <i>State</i> v. <i>Strait,</i> <span class="citation" data-id="7973247"><a href="/opinion/8017916/state-v-strait/" aria-description="Citation for case: State v. Strait">94 Minn. 384</a></span>, <span class="citation" data-id="7973247"><a href="/opinion/8017916/state-v-strait/" aria-description="Citation for case: State v. Strait">102 N. W. 913</a></span>.
MO.     <i>State</i> v. <i>Pomeroy,</i> <span class="citation" data-id="8011909"><a href="/opinion/8054876/state-v-pomeroy/" aria-description="Citation for case: State v. Pomeroy">130 Mo. 489</a></span>, <span class="citation" data-id="8011909"><a href="/opinion/8054876/state-v-pomeroy/" aria-description="Citation for case: State v. Pomeroy">32 S. W. 1002</a></span>.
MONT.   See <i>State</i> v. <i>Fuller,</i> <span class="citation" data-id="8020864"><a href="/opinion/8063090/state-v-fuller/#19" aria-description="Citation for case: State v. Fuller">34 Mont. 12, 19</a></span>, <span class="citation" data-id="8020864"><a href="/opinion/8063090/state-v-fuller/#373" aria-description="Citation for case: State v. Fuller">85 P. 369, 373</a></span>.
NEB.    <i>Geiger</i> v. <i>State,</i> <span class="citation" data-id="6642402"><a href="/opinion/6759719/geiger-v-state/" aria-description="Citation for case: Geiger v. State">6 Neb. 545</a></span>.
N. H.   <i>State</i> v. <i>Flynn,</i> 36 N. H. 64.
N. Y.   <i>People</i> v. <i>Adams,</i> <span class="citation" data-id="5650086"><a href="/opinion/5795142/people-v-adams/" aria-description="Citation for case: People v. Adams">176 N. Y. 351</a></span>, <span class="citation" data-id="3588018"><a href="/opinion/3606309/people-v-adams/" aria-description="Citation for case: People v. . Adams">68 N. E. 636</a></span>.
N. C.   <i>State</i> v. <i>Wallace,</i> <span class="citation" data-id="6695783"><a href="/opinion/6809677/state-v-wallace/" aria-description="Citation for case: State v. Wallace">162 N. C. 622</a></span>, <span class="citation" data-id="3672959"><a href="/opinion/3926369/s-v-wallace/" aria-description="Citation for case: S. v. . Wallace">78 S. E. 1</a></span>.
OKLA.   <i>Silva</i> v. <i>State,</i> <span class="citation" data-id="3827556"><a href="/opinion/4069690/silva-v-state/" aria-description="Citation for case: Silva v. State">6 Okla. Cr. 97</a></span>, <span class="citation" data-id="3827556"><a href="/opinion/4069690/silva-v-state/" aria-description="Citation for case: Silva v. State">116 P. 199</a></span>.
ORE.    <i>State</i> v. <i>McDaniel,</i> <span class="citation" data-id="6898602"><a href="/opinion/6999518/state-v-mcdaniel/#169" aria-description="Citation for case: State v. McDaniel">39 Ore. 161, 169-70</a></span>, <span class="citation" data-id="6898602"><a href="/opinion/6999518/state-v-mcdaniel/#523" aria-description="Citation for case: State v. McDaniel">65 P. 520, 523</a></span>.
S. C.   <i>State</i> v. <i>Atkinson,</i> 40 S. C. 363, 371, <span class="citation" data-id="6678093"><a href="/opinion/6793472/state-v-atkinson/#1024" aria-description="Citation for case: State v. Atkinson">18 S. E. 1021, 1024</a></span>.
S. D.   <i>State</i> v. <i>Madison,</i> 23 S. D. 584, 591, <span class="citation" data-id="6687221"><a href="/opinion/6802175/state-v-madison/#650" aria-description="Citation for case: State v. Madison">122 N. W. 647, 650</a></span>.
TENN.   <i>Cohn</i> v. <i>State,</i> <span class="citation" data-id="8300564"><a href="/opinion/8332572/cohn-v-state/" aria-description="Citation for case: Cohn v. State">120 Tenn. 61</a></span>, <span class="citation" data-id="3980535"><a href="/opinion/4208407/parriss-v-hughes/" aria-description="Citation for case: Parriss v. Hughes">109 S. W. 1149</a></span>.
VT.     <i>State</i> v. <i>Mathers,</i> <span class="citation" data-id="6583727"><a href="/opinion/6703627/state-v-mathers/" aria-description="Citation for case: State v. Mathers">64 Vt. 101</a></span>, <span class="citation no-link">23 A. 590</span>.
WASH.   <i>State</i> v. <i>Royce,</i> <span class="citation" data-id="4726508"><a href="/opinion/4919818/state-v-royce/" aria-description="Citation for case: State v. Royce">38 Wash. 111</a></span>, <span class="citation" data-id="4726508"><a href="/opinion/4919818/state-v-royce/" aria-description="Citation for case: State v. Royce">80 P. 268</a></span>.
W. VA.  See <i>State</i> v. <i>Edwards,</i> <span class="citation" data-id="8175125"><a href="/opinion/8212628/state-v-edwards/#229" aria-description="Citation for case: State v. Edwards">51 W. Va. 220, 229</a></span>, <span class="citation" data-id="8175125"><a href="/opinion/8212628/state-v-edwards/#432" aria-description="Citation for case: State v. Edwards">41 S. E. 429,
          432-33</a></span>.
                           TABLE B.
    STATE WHICH HAD FORMULATED THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE
              BEFORE THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DECISION.
IOWA    <i>State</i> v. <i>Sheridan,</i> <span class="citation" data-id="7110547"><a href="/opinion/7199309/state-v-sheridan/" aria-description="Citation for case: State v. Sheridan">121 Iowa 164</a></span>, <span class="citation" data-id="7110547"><a href="/opinion/7199309/state-v-sheridan/" aria-description="Citation for case: State v. Sheridan">96 N. W. 730</a></span>.
                           TABLE C.
    STATES WHICH HAVE PASSED ON THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE
          SINCE THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> CASE WAS DECIDED.
   Every State except Rhode Island. But see <i>State</i> v. <i>Lorenzo,</i> 72
R. I. 175, <span class="citation" data-id="3870663"><a href="/opinion/4110701/state-v-lorenzo/" aria-description="Citation for case: State v. Lorenzo">48 A. 2d 407</a></span> (holding that defendant had consented to
the search, but that, even if he had not and even if the federal rule
applied, the evidence was admissible because no timely motion to
suppress had been made).
<span class="star-pagination">*35</span>
                           TABLE D.
STATES WHICH PASSED ON THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE FOR THE FIRST TIME
AFTER THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DECISION AND IN SO DOING FOLLOWED IT.
FLA.    <i>Atz</i> v. <i>Andrews,</i> <span class="citation" data-id="4921024"><a href="/opinion/5103176/atz-v-andrews/" aria-description="Citation for case: Atz v. Andrews">84 Fla. 43</a></span>, <span class="citation" data-id="4921024"><a href="/opinion/5103176/atz-v-andrews/" aria-description="Citation for case: Atz v. Andrews">94 So. 329</a></span>.
IND.    <i>Flum</i> v. <i>State,</i> <span class="citation" data-id="7057995"><a href="/opinion/7149435/flum-v-state/" aria-description="Citation for case: Flum v. State">193 Ind. 585</a></span>, <span class="citation" data-id="7057995"><a href="/opinion/7149435/flum-v-state/" aria-description="Citation for case: Flum v. State">141 N. E. 353</a></span>.
KY.     <i>Youman</i> v. <i>Commonwealth,</i> <span class="citation" data-id="7146240"><a href="/opinion/7233831/youman-v-commonwealth/" aria-description="Citation for case: Youman v. Commonwealth">189 Ky. 152</a></span>, <span class="citation" data-id="7146240"><a href="/opinion/7233831/youman-v-commonwealth/" aria-description="Citation for case: Youman v. Commonwealth">224 S. W. 860</a></span>.
MISS.   <i>Tucker</i> v. <i>State,</i> <span class="citation" data-id="7994199"><a href="/opinion/8037845/tucker-v-state/" aria-description="Citation for case: Tucker v. State">128 Miss. 211</a></span>, <span class="citation" data-id="7994199"><a href="/opinion/8037845/tucker-v-state/" aria-description="Citation for case: Tucker v. State">90 So. 845</a></span>.
WIS.    <i>Hoyer</i> v. <i>State,</i> <span class="citation" data-id="8194030"><a href="/opinion/8229755/hoyer-v-state/" aria-description="Citation for case: Hoyer v. State">180 Wis. 407</a></span>, <span class="citation" data-id="8194030"><a href="/opinion/8229755/hoyer-v-state/" aria-description="Citation for case: Hoyer v. State">193 N. W. 89</a></span>.
WYO.    <i>State</i> v. <i>George,</i> <span class="citation" data-id="4012941"><a href="/opinion/4235695/state-v-george/" aria-description="Citation for case: State v. George">32 Wyo. 223</a></span>, <span class="citation" data-id="4012941"><a href="/opinion/4235695/state-v-george/" aria-description="Citation for case: State v. George">231 P. 683</a></span>.
                           TABLE E.
STATES WHICH PASSED ON THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE FOR THE FIRST TIME
AFTER THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DECISION AND IN SO DOING REJECTED IT.
ARIZ.   <i>Argetakis</i> v. <i>State,</i> <span class="citation" data-id="6474949"><a href="/opinion/6599573/argetakis-v-state/" aria-description="Citation for case: Argetakis v. State">24 Ariz. 599</a></span>, <span class="citation" data-id="6474949"><a href="/opinion/6599573/argetakis-v-state/" aria-description="Citation for case: Argetakis v. State">212 P. 372</a></span>.
CALIF.  <i>People</i> v. <i>Mayen,</i> 188 Calif. 237, <span class="citation" data-id="3307559"><a href="/opinion/3307673/people-v-mayen/" aria-description="Citation for case: People v. Mayen">205 P. 435</a></span> (adopting the
          general rule but distinguishing the cases then decided by
          this Court on the ground that they apply only when a
          timely motion for return of the property seized has been
          made).
COLO.   <i>Massantonio</i> v. <i>People,</i> <span class="citation" data-id="3311672"><a href="/opinion/3316610/massantonio-v-people/" aria-description="Citation for case: Massantonio v. People">77 Colo. 392</a></span>, <span class="citation" data-id="3311672"><a href="/opinion/3316610/massantonio-v-people/" aria-description="Citation for case: Massantonio v. People">236 P. 1019</a></span>.
DEL.    <i>State</i> v. <i>Chuchola,</i> <span class="citation" data-id="6556679"><a href="/opinion/6677615/state-v-chuchola/" aria-description="Citation for case: State v. Chuchola">32 Del. 133</a></span>, <span class="citation" data-id="6556679"><a href="/opinion/6677615/state-v-chuchola/" aria-description="Citation for case: State v. Chuchola">120 A. 212</a></span> (distinguishing
          this Court's decisions).
LA.     <i>State</i> v. <i>Fleckinger,</i> <span class="citation" data-id="7172743"><a href="/opinion/7258568/nolan-v-brown/" aria-description="Citation for case: Nolan v. Brown">152 La. 337</a></span>, <span class="citation" data-id="7172750"><a href="/opinion/7258573/state-v-fleckinger/" aria-description="Citation for case: State v. Fleckinger">93 So. 115</a></span>. The constitutional
          convention of 1921 refused to adopt an amendment
          incorporating the federal rule. See <i>State</i> v. <i>Eddins,</i>
          <span class="citation" data-id="3471999"><a href="/opinion/3472961/state-v-eddins/" aria-description="Citation for case: State v. Eddins">161 La. 240</a></span>, <span class="citation" data-id="3471999"><a href="/opinion/3472961/state-v-eddins/" aria-description="Citation for case: State v. Eddins">108 So. 468</a></span>.
NEV.    <i>State</i> v. <i>Chin Gim,</i> <span class="citation" data-id="8042834"><a href="/opinion/8083180/state-v-chin-gim/" aria-description="Citation for case: State v. Chin Gim">47 Nev. 431</a></span>, <span class="citation" data-id="8042834"><a href="/opinion/8083180/state-v-chin-gim/" aria-description="Citation for case: State v. Chin Gim">224 P. 798</a></span>.
N. J.   <i>State</i> v. <i>Black,</i> 5 N. J. Misc. 48, <span class="citation" data-id="8506298"><a href="/opinion/8533787/state-v-black/" aria-description="Citation for case: State v. Black">135 A. 685</a></span>.
N. M.   <i>State</i> v. <i>Dillon,</i> 34 N. M. 366, <span class="citation" data-id="3571966"><a href="/opinion/3591159/state-v-dillon/" aria-description="Citation for case: State v. Dillon">281 P. 474</a></span>.
N. D.   <i>State</i> v. <i>Fahn,</i> <span class="citation" data-id="3682031"><a href="/opinion/3934924/state-v-fahn/" aria-description="Citation for case: State v. Fahn">53 N. D. 203</a></span>, <span class="citation" data-id="3682031"><a href="/opinion/3934924/state-v-fahn/" aria-description="Citation for case: State v. Fahn">205 N. W. 67</a></span>.
OHIO    <i>State</i> v. <i>Lindway,</i> <span class="citation" data-id="3780866"><a href="/opinion/4024496/state-v-lindway/" aria-description="Citation for case: State v. Lindway">131 Ohio St. 166</a></span>, <span class="citation" data-id="3780866"><a href="/opinion/4024496/state-v-lindway/" aria-description="Citation for case: State v. Lindway">2 N. E. 2d 490</a></span>.
PA.     <i>Commonwealth</i> v. <i>Dabbierio,</i> <span class="citation" data-id="3848320"><a href="/opinion/4089084/commonwealth-v-dabbierio/" aria-description="Citation for case: Commonwealth v. Dabbierio">290 Pa. 174</a></span>, <span class="citation" data-id="3848320"><a href="/opinion/4089084/commonwealth-v-dabbierio/" aria-description="Citation for case: Commonwealth v. Dabbierio">138 A. 679</a></span>.
TEX.    <i>Welchek</i> v. <i>State,</i> 93 Tex. Cr. Rep. 271, <span class="citation" data-id="3977441"><a href="/opinion/4205697/welchek-v-state/" aria-description="Citation for case: Welchek v. State">247 S. W. 524</a></span>. In
          1925 a statute changed the rule by providing that "No
          evidence obtained by an officer or other person in violation
          of any provisions of the Constitution or laws of the State
<span class="star-pagination">*36</span>
STATES WHICH PASSED ON THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE FOR THE FIRST TIME
AFTER THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DECISION AND IN SO DOING REJECTED IT.
          of Texas, or of the Constitution of the United States of
          America, shall be admitted in evidence against the accused
          on the trial of any criminal case." Texas Laws 1925,
          c. 49, as amended, 2 Vernon's Tex. Stat., 1948 (Code
          of Crim. Proc.), Art. 727a.
UTAH    <i>State</i> v. <i>Aime,</i> <span class="citation" data-id="8657438"><a href="/opinion/8674530/state-v-aime/" aria-description="Citation for case: State v. Aime">62 Utah 476</a></span>, <span class="citation" data-id="8657438"><a href="/opinion/8674530/state-v-aime/" aria-description="Citation for case: State v. Aime">220 P. 704</a></span>.
VA.     <i>Hall</i> v. <i>Commonwealth,</i> <span class="citation" data-id="6815460"><a href="/opinion/6919821/hall-v-commonwealth/" aria-description="Citation for case: Hall v. Commonwealth">138 Va. 727</a></span>, <span class="citation" data-id="6815460"><a href="/opinion/6919821/hall-v-commonwealth/" aria-description="Citation for case: Hall v. Commonwealth">121 S. E. 154</a></span>.
                           TABLE F.
 STATES WHICH, AFTER THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DECISION, OVERRULED OR
            DISTINGUISHED PRIOR CONTRARY DECISIONS.
IDAHO   Idaho expressly refused to follow the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> decision in <i>State</i>
          v. <i>Myers,</i> <span class="citation" data-id="5171906"><a href="/opinion/5339733/state-v-myers/" aria-description="Citation for case: State v. Myers">36 Idaho 396</a></span>, <span class="citation" data-id="5171906"><a href="/opinion/5339733/state-v-myers/" aria-description="Citation for case: State v. Myers">211 P. 440</a></span>, but repudiated the
          <i><span class="citation" data-id="5171906"><a href="/opinion/5339733/state-v-myers/" aria-description="Citation for case: State v. Myers">Myers</a></span></i> case and adopted the federal rule in <i>State</i> v.
          <i>Arregui,</i> <span class="citation" data-id="3412636"><a href="/opinion/3416496/state-v-arregui/" aria-description="Citation for case: State v. Arregui">44 Idaho 43</a></span>, <span class="citation" data-id="3412636"><a href="/opinion/3416496/state-v-arregui/" aria-description="Citation for case: State v. Arregui">254 P. 788</a></span>.
ILL.    After two cases following the former state rule, Illinois
          adopted the federal rule in <i>People</i> v. <i>Castree,</i> <span class="citation" data-id="6981353"><a href="/opinion/7076578/people-v-castree/" aria-description="Citation for case: People v. Castree">311 Ill. 392</a></span>,
          <span class="citation" data-id="6981353"><a href="/opinion/7076578/people-v-castree/" aria-description="Citation for case: People v. Castree">143 N. E. 112</a></span>.
MICH.   <i>People</i> v. <i>Marxhausen,</i> <span class="citation" data-id="7950359"><a href="/opinion/7996598/people-v-marxhausen/" aria-description="Citation for case: People v. Marxhausen">204 Mich. 559</a></span>, <span class="citation" data-id="7950359"><a href="/opinion/7996598/people-v-marxhausen/" aria-description="Citation for case: People v. Marxhausen">171 N. W. 557</a></span> (distinguishing
          earlier cases on the ground that in them no
          preliminary motion to suppress had been made).
MO.     <i>State</i> v. <i>Graham,</i> <span class="citation" data-id="3536208"><a href="/opinion/3558301/state-v-graham/" aria-description="Citation for case: State v. Graham">295 Mo. 695</a></span>, <span class="citation" data-id="3536208"><a href="/opinion/3558301/state-v-graham/" aria-description="Citation for case: State v. Graham">247 S. W. 194</a></span>, supported
          the old rule in a dictum, but the federal rule was adopted
          in <i>State</i> v. <i>Owens,</i> <span class="citation" data-id="3529427"><a href="/opinion/3553710/state-v-owens/" aria-description="Citation for case: State v. Owens">302 Mo. 348</a></span>, <span class="citation" data-id="3529427"><a href="/opinion/3553710/state-v-owens/" aria-description="Citation for case: State v. Owens">259 S. W. 100</a></span> (distinguishing
          earlier cases on the ground that in them no
          preliminary motion to dismiss had been made).
MONT.   <i>State ex rel. King</i> v. <i>District Court,</i> <span class="citation" data-id="8024014"><a href="/opinion/8066072/state-ex-rel-king-v-district-court/" aria-description="Citation for case: State ex rel. King v. District Court">70 Mont. 191</a></span>, <span class="citation" data-id="8024014"><a href="/opinion/8066072/state-ex-rel-king-v-district-court/" aria-description="Citation for case: State ex rel. King v. District Court">224 P.
          862</a></span>.
OKLA.   <i>Gore</i> v. <i>State,</i> <span class="citation" data-id="3812264"><a href="/opinion/4054922/gore-v-state/" aria-description="Citation for case: Gore v. State">24 Okla. Cr. 394</a></span>, <span class="citation" data-id="3812264"><a href="/opinion/4054922/gore-v-state/" aria-description="Citation for case: Gore v. State">218 P. 545</a></span>.
S. D.   <i>State</i> v. <i>Gooder,</i> 57 S. D. 619, <span class="citation" data-id="6692555"><a href="/opinion/6806990/state-v-gooder/" aria-description="Citation for case: State v. Gooder">234 N. W. 610</a></span>. But cf.
          S. D. Laws 1935, c. 96, now S. D. Code § 34.1102 (1939),
          amending Rev. Code 1919, § 4606 (all evidence admissible
<span class="star-pagination">*37</span>
 STATES WHICH, AFTER THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DECISION, OVERRULED OR
            DISTINGUISHED PRIOR CONTRARY DECISIONS.
            under a valid search warrant is admissible notwithstanding
            defects in the issuance of the warrant).
TENN.   <i>Hughes</i> v. <i>State,</i> <span class="citation" data-id="8302107"><a href="/opinion/8334068/hughes-v-state/" aria-description="Citation for case: Hughes v. State">145 Tenn. 544</a></span>, <span class="citation no-link">238 S. W. 588</span> (distinguishing
          <i>Cohn</i> v. <i>State, supra,</i> Table A).
WASH.   <i>State</i> v. <i>Gibbons,</i> <span class="citation" data-id="4720844"><a href="/opinion/4914645/state-v-gibbons/" aria-description="Citation for case: State v. Gibbons">118 Wash. 171</a></span>, <span class="citation" data-id="4720844"><a href="/opinion/4914645/state-v-gibbons/" aria-description="Citation for case: State v. Gibbons">203 P. 390</a></span>.
W. VA.  <i>State</i> v. <i>Andrews,</i> <span class="citation" data-id="8179544"><a href="/opinion/8216695/state-v-andrews/" aria-description="Citation for case: State v. Andrews">91 W. Va. 720</a></span>, <span class="citation" data-id="8179544"><a href="/opinion/8216695/state-v-andrews/" aria-description="Citation for case: State v. Andrews">114 S. E. 257</a></span> (distinguishing
          earlier cases).
                           TABLE G.
STATES WHICH, AFTER THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DECISION, REVIEWED PRIOR CONTRARY
     DECISIONS AND IN SO DOING ADHERED TO THOSE DECISIONS.
ALA.    <i>Banks</i> v. <i>State,</i> <span class="citation" data-id="3233534"><a href="/opinion/3232762/banks-v-state/" aria-description="Citation for case: Banks v. State">207 Ala. 179</a></span>, <span class="citation" data-id="3233534"><a href="/opinion/3232762/banks-v-state/" aria-description="Citation for case: Banks v. State">93 So. 293</a></span>.
ARK.    <i>Benson</i> v. <i>State,</i> <span class="citation" data-id="7811152"><a href="/opinion/7866973/benson-v-state/" aria-description="Citation for case: Benson v. State">149 Ark. 633</a></span>, <span class="citation" data-id="7811152"><a href="/opinion/7866973/benson-v-state/" aria-description="Citation for case: Benson v. State">233 S. W. 758</a></span>.
CONN.   <i>State</i> v. <i>Reynolds,</i> <span class="citation" data-id="3321660"><a href="/opinion/3326264/state-v-reynolds/" aria-description="Citation for case: State v. Reynolds">101 Conn. 224</a></span>, <span class="citation" data-id="3321660"><a href="/opinion/3326264/state-v-reynolds/" aria-description="Citation for case: State v. Reynolds">125 A. 636</a></span>.
GA.     <i>Jackson</i> v. <i>State,</i> <span class="citation" data-id="5584660"><a href="/opinion/5734032/jackson-v-state/" aria-description="Citation for case: Jackson v. State">156 Ga. 647</a></span>, <span class="citation" data-id="5584660"><a href="/opinion/5734032/jackson-v-state/" aria-description="Citation for case: Jackson v. State">119 S. E. 525</a></span>.
KAN.    <i>State</i> v. <i>Johnson,</i> <span class="citation" data-id="7907024"><a href="/opinion/7955587/state-v-johnson/" aria-description="Citation for case: State v. Johnson">116 Kan. 58</a></span>, <span class="citation" data-id="7907024"><a href="/opinion/7955587/state-v-johnson/" aria-description="Citation for case: State v. Johnson">226 P. 245</a></span>.
ME.     <i>State</i> v. <i>Schoppe,</i> <span class="citation" data-id="4938095"><a href="/opinion/5119383/state-v-schoppe/#16" aria-description="Citation for case: State v. Schoppe">113 Me. 10, 16</a></span>, <span class="citation" data-id="4938095"><a href="/opinion/5119383/state-v-schoppe/#869" aria-description="Citation for case: State v. Schoppe">92 A. 867, 869</a></span> (alternative
          holding, not noticing <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i>).
MD.     <i>Meisinger</i> v. <i>State,</i> <span class="citation" data-id="3484807"><a href="/opinion/3486914/meisinger-v-state/" aria-description="Citation for case: Meisinger v. State">155 Md. 195</a></span>, <span class="citation" data-id="3484807"><a href="/opinion/3486914/meisinger-v-state/" aria-description="Citation for case: Meisinger v. State">141 A. 536</a></span>, <span class="citation no-link">142 A. 190</span>.
          But cf. Md. Laws 1929, c. 194, as amended, Md. Code
          Ann., Art. 35, § 5 (1947 Supp.) (in trial of misdemeanors,
          evidence obtained by illegal search and seizure is inadmissible).
MASS.   <i>Commonwealth</i> v. <i>Wilkins,</i> <span class="citation" data-id="6436025"><a href="/opinion/6562275/commonwealth-v-wilkins/" aria-description="Citation for case: Commonwealth v. Wilkins">243 Mass. 356</a></span>, <span class="citation no-link">138 N. E. 11</span>.
MINN.   <i>State</i> v. <i>Pluth,</i> <span class="citation" data-id="7981382"><a href="/opinion/8025591/state-v-pluth/" aria-description="Citation for case: State v. Pluth">157 Minn. 145</a></span>, <span class="citation" data-id="7981382"><a href="/opinion/8025591/state-v-pluth/" aria-description="Citation for case: State v. Pluth">195 N. W. 789</a></span>.
NEB.    <i>Billings</i> v. <i>State,</i> <span class="citation" data-id="8032854"><a href="/opinion/8074092/billings-v-state/" aria-description="Citation for case: Billings v. State">109 Neb. 596</a></span>, <span class="citation" data-id="8032854"><a href="/opinion/8074092/billings-v-state/" aria-description="Citation for case: Billings v. State">191 N. W. 721</a></span>.
N. H.   <i>State</i> v. <i>Agalos,</i> 79 N. H. 241, 242, <span class="citation" data-id="3553875"><a href="/opinion/3573624/state-v-agalos/#315" aria-description="Citation for case: State v. Agalos">107 A. 314, 315</a></span> (not
          noticing <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i>).
N. Y.   <i>People</i> v. <i>Defore,</i> <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">242 N. Y. 13</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">150 N. E. 585</a></span>; <i>People</i> v.
          <i>Richter's Jewelers,</i> <span class="citation" data-id="3594947"><a href="/opinion/3612831/people-v-richters-jewelers-inc/#169" aria-description="Citation for case: People v. Richter&#x27;s Jewelers, Inc.">291 N. Y. 161, 169</a></span>, <span class="citation" data-id="3594947"><a href="/opinion/3612831/people-v-richters-jewelers-inc/#693" aria-description="Citation for case: People v. Richter&#x27;s Jewelers, Inc.">51 N. E. 2d 690,
          693</a></span> (holding that adoption of Amendment to State Constitution
<span class="star-pagination">*38</span>
STATES WHICH, AFTER THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DECISION, REVIEWED PRIOR CONTRARY
     DECISIONS AND IN SO DOING ADHERED TO THOSE DECISIONS.
         in same language as Civil Rights Law construed
         in the <i><span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">Defore</a></span></i> case is not occasion for changing interpretation,
         especially since proceedings of the convention
         which framed the amendment show that no change was
         intended).
N. C.   <i>State</i> v. <i>Simmons,</i> <span class="citation" data-id="3646527"><a href="/opinion/3900534/state-v-simmons/" aria-description="Citation for case: State v. . Simmons">183 N. C. 684</a></span>, <span class="citation" data-id="3646527"><a href="/opinion/3900534/state-v-simmons/" aria-description="Citation for case: State v. . Simmons">110 S. E. 591</a></span> (distinguishing
          between evidentiary articles and corpus delicti).
ORE.    See <i>State</i> v. <i>Folkes,</i> <span class="citation" data-id="3842073"><a href="/opinion/4083033/state-v-folkes/#588" aria-description="Citation for case: State v. Folkes">174 Ore. 568, 588-89</a></span>, <span class="citation" data-id="3842073"><a href="/opinion/4083033/state-v-folkes/#25" aria-description="Citation for case: State v. Folkes">150 P. 2d 17, 25</a></span>.
          But see <i>State</i> v. <i>Laundy,</i> <span class="citation" data-id="6907613"><a href="/opinion/7007488/state-v-laundy/#493" aria-description="Citation for case: State v. Laundy">103 Ore. 443, 493-95</a></span>, <span class="citation" data-id="6907613"><a href="/opinion/7007488/state-v-laundy/#974" aria-description="Citation for case: State v. Laundy">204 P.
          958, 974-75</a></span>.
S. C.   After granting a motion to return illegally seized property
         in <i>Blacksburg</i> v. <i>Beam,</i> 104 S. C. 146, <span class="citation" data-id="3880639"><a href="/opinion/4119711/town-of-blacksburg-v-beam/" aria-description="Citation for case: Town of Blacksburg v. Beam">88 S. E. 441</a></span>, South
         Carolina reaffirmed its agreement with the general rule in
         <i>State</i> v. <i>Green,</i> 121 S. C. 230, <span class="citation no-link">114 S. E. 317</span>.
VT.     <i>State</i> v. <i>Stacy,</i> <span class="citation" data-id="3990360"><a href="/opinion/4216163/state-v-stacy/#401" aria-description="Citation for case: State v. Stacy">104 Vt. 379, 401</a></span>, <span class="citation no-link">160 A. 257</span>, 266.
                           TABLE H.
       STATE WHICH HAS REPUDIATED ITS PRIOR FORMULATION
                OF THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE.
IOWA    <i>State</i> v. <i>Rowley,</i> <span class="citation" data-id="7120701"><a href="/opinion/7208995/state-v-rowley/" aria-description="Citation for case: State v. Rowley">197 Iowa 977</a></span>, <span class="citation no-link">195 N. W. 881</span> (withdrawing
          earlier opinion in <span class="citation no-link">187 N. W. 7</span>).
                           TABLE I.
       SUMMARY OF PRESENT POSITION OF STATES WHICH HAVE
            PASSED ON THE <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> DOCTRINE.
   (a) States that reject <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>:</i>
   Ala., Ariz., Ark., Calif., Colo., Conn., Del., Ga., Iowa, Kan., La.,
Me., Md., Mass., Minn., Neb., Nev., N. H., N. J., N. M., N. Y.,
N. C., N. D., Ohio, Ore., Pa., S. C., Texas, Utah, Vt., Va.
   (b) States that are in agreement with <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>:</i>
   Fla., Idaho, Ill., Ind., Ky., Mich., Miss., Mo., Mont., Okla., S. D.,
Tenn., Wash., W. Va., Wis., Wyo.
<span class="star-pagination">*39</span>
                           TABLE J.
JURISDICTIONS OF THE UNITED KINGDOM AND THE BRITISH COMMONWEALTH
             OF NATIONS WHICH HAVE HELD ADMISSIBLE
       EVIDENCE OBTAINED BY ILLEGAL SEARCH AND SEIZURE.
AUSTRALIA  <i>Miller</i> v. <i>Noblet,</i> [1927] S. A. S. R. 385.
CANADA
  ALTA.   <i>Rex</i> v. <i>Nelson,</i> [1922] 2 W. W. R. 381, 69 D. L. R. 180.
   MAN.   <i>Rex</i> v. <i>Duroussel,</i> 41 Man. 15, [1933] 2 D. L. R. 446.
   ONT.   <i>Regina</i> v. <i>Doyle,</i> 12 Ont. 347.
  SASK.   <i>Rex</i> v. <i>Kostachuk,</i> 24 Sask. 485, 54 Can. C. C. 189.
ENGLAND   See <i>Elias</i> v. <i>Pasmore,</i> [1934] 2 K. B. 164.
INDIA
  ALL.    <i>Ali Ahmad Khan</i> v. <i>Emperor,</i> 81 I. C. 615 (1).
  CAL.    <i>Baldeo Bin</i> v. <i>Emperor,</i> 142 I. C. 639.
  RANG.   <i>Chwa Hum Htive</i> v. <i>Emperor,</i> 143 I. C. 824.
SCOTLAND  See <i>Hodgson</i> v. <i>Macpherson,</i> [1913] S. C. (J.) 68, 73.
<p>MR. JUSTICE BLACK, concurring.</p>
<p>In this case petitioner was convicted of a crime in a state court on evidence obtained by a search and seizure conducted in a manner that this Court has held "unreasonable" and therefore in violation of the Fourth Amendment. And under a rule of evidence adopted by this Court evidence so obtained by federal officers cannot be used against defendants in federal courts. For reasons stated in my dissenting opinion in <i>Adamson</i> v. <i>California,</i> <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/#68" aria-description="Citation for case: Adamson v. California">332 U. S. 46, 68</a></span>, I agree with the conclusion of the Court that the Fourth Amendment's prohibition of "unreasonable searches and seizures" is enforceable against the states. Consequently, I should be for reversal of this case if I thought the Fourth Amendment not only prohibited "unreasonable searches and seizures," but also, of itself, barred the use of evidence so unlawfully obtained. But I agree with what appears to be a plain implication of the Court's opinion that the federal exclusionary rule is <span class="star-pagination">*40</span> not a command of the Fourth Amendment but is a judicially created rule of evidence which Congress might negate. See <i>McNabb</i> v. <i>United States,</i> <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U. S. 332</a></span>. This leads me to concur in the Court's judgment of affirmance.</p>
<p>It is not amiss to repeat my belief that the Fourteenth Amendment was intended to make the Fourth Amendment in its entirety applicable to the states. The Fourth Amendment was designed to protect people against unrestrained searches and seizures by sheriffs, policemen and other law enforcement officers. Such protection is an essential in a free society. And I am unable to agree that the protection of people from over-zealous or ruthless state officers is any less essential in a country of "ordered liberty" than is the protection of people from over-zealous or ruthless federal officers. Certainly there are far more state than federal enforcement officers and their activities, up to now, have more frequently and closely touched the intimate daily lives of people than have the activities of federal officers. A state officer's "knock at the door . . . as a prelude to a search, without authority of law," may be, as our experience shows, just as ominous to "ordered liberty" as though the knock were made by a federal officer.</p>
<p>MR. JUSTICE DOUGLAS, dissenting.</p>
<p>I believe for the reasons stated by MR. JUSTICE BLACK in his dissent in <i>Adamson</i> v. <i>California,</i> <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/#68" aria-description="Citation for case: Adamson v. California">332 U. S. 46, 68</a></span>, that the Fourth Amendment is applicable to the States. I agree with MR. JUSTICE MURPHY that the evidence obtained in violation of it <i>must</i> be excluded in state prosecutions as well as in federal prosecutions, since in absence of that rule of evidence the Amendment would have no effective sanction. I also agree with him that under that <span class="star-pagination">*41</span> test this evidence was improperly admitted and that the judgments of conviction must be reversed.</p>
<p>MR. JUSTICE MURPHY, with whom MR. JUSTICE RUTLEDGE joins, dissenting.</p>
<p>It is disheartening to find so much that is right in an opinion which seems to me so fundamentally wrong. Of course I agree with the Court that the Fourteenth Amendment prohibits activities which are proscribed by the search and seizure clause of the Fourth Amendment. See my dissenting views, and those of MR. JUSTICE BLACK, in <i>Adamson</i> v. <i>California,</i> <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/#68" aria-description="Citation for case: Adamson v. California">332 U. S. 46, 68, 123</a></span>. Quite apart from the blanket application of the Bill of Rights to the States, a devotee of democracy would ill suit his name were he to suggest that his home's protection against unlicensed governmental invasion was not "of the very essence of a scheme of ordered liberty." <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319, 325</a></span>. It is difficult for me to understand how the Court can go this far and yet be unwilling to make the step which can give some meaning to the pronouncements it utters.</p>
<p>Imagination and zeal may invent a dozen methods to give content to the commands of the Fourth Amendment. But this Court is limited to the remedies currently available. It cannot legislate the ideal system. If we would attempt the enforcement of the search and seizure clause in the ordinary case today, we are limited to three devices: judicial exclusion of the illegally obtained evidence; criminal prosecution of violators; and civil action against violators in the action of trespass.</p>
<p>Alternatives are deceptive. Their very statement conveys the impression that one possibility is as effective as the next. In this case their statement is blinding. For there is but one alternative to the rule of exclusion. That is no sanction at all.</p>
<p><span class="star-pagination">*42</span> This has been perfectly clear since 1914, when a unanimous Court decided <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#393" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 393</a></span>. "If letters and private documents can thus be seized and held and used in evidence against a citizen accused of an offense," we said, "the protection of the Fourth Amendment declaring his right to be secure against such searches and seizures is of no value, and, so far as those thus placed are concerned, might as well be stricken from the Constitution." "It reduces the Fourth Amendment to a form of words." Holmes, J., for the Court, in <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span>.</p>
<p>Today the Court wipes those statements from the books with its bland citation of "other remedies." Little need be said concerning the possibilities of criminal prosecution. Self-scrutiny is a lofty ideal, but its exaltation reaches new heights if we expect a District Attorney to prosecute himself or his associates for well-meaning violations of the search and seizure clause during a raid the District Attorney or his associates have ordered.<sup>[1]</sup> But there is an appealing ring in another alternative. A trespass action for damages is a venerable means of securing reparation for unauthorized invasion of the home. Why not put the old writ to a new use? When the Court cites cases permitting the action, the remedy seems complete.</p>
<p>But what an illusory remedy this is, if by "remedy" we mean a positive deterrent to police and prosecutors <span class="star-pagination">*43</span> tempted to violate the Fourth Amendment. The appealing ring softens when we recall that in a trespass action the measure of damages is simply the extent of the injury to physical property. If the officer searches with care, he can avoid all but nominal damagesa penny, or a dollar. Are punitive damages possible? Perhaps. But a few states permit none, whatever the circumstances.<sup>[2]</sup> In those that do, the plaintiff must show the real ill will or malice of the defendant,<sup>[3]</sup> and surely it is not unreasonable to assume that one in honest pursuit of crime bears no malice toward the search victim. If that burden is carried, recovery may yet be defeated by the rule that there must be physical damages before punitive damages may be awarded.<sup>[4]</sup> In addition, some states limit punitive damages to the actual expenses of litigation. See <span class="citation no-link">61 Harv. L. Rev. 113</span>, 119-120. Others demand some arbitrary ratio between actual and punitive damages before a verdict may stand. See Morris, <i>Punitive Damages in Tort Cases,</i> <span class="citation no-link">44 Harv. L. Rev. 1173</span>, 1180-1181. Even assuming the ill will of the officer, his reasonable grounds for belief that the home he searched harbored evidence of crime is admissible in mitigation of punitive damages. <i>Gamble</i> v. <i>Keyes,</i> 35 S. D. 644, <span class="citation" data-id="6688877"><a href="/opinion/6803692/gamble-v-keyes/" aria-description="Citation for case: Gamble v. Keyes">153 N. W. 888</a></span>; <i>Simpson</i> v. <i>McCaffrey,</i> <span class="citation no-link">13 Ohio 508</span>. The bad reputation of the plaintiff is likewise admissible. <i>Banfill</i> v. <i>Byrd,</i> <span class="citation" data-id="7993628"><a href="/opinion/8037305/banfill-v-byrd/" aria-description="Citation for case: Banfill v. Byrd">122 Miss. 288</a></span>, <span class="citation" data-id="7993628"><a href="/opinion/8037305/banfill-v-byrd/" aria-description="Citation for case: Banfill v. Byrd">84 So. 227</a></span>. If the evidence seized was actually used at a trial, that fact has been <span class="star-pagination">*44</span> held a complete justification of the search, and a defense against the trespass action. <i>Elias</i> v. <i>Pasmore</i> [1934] 2 K. B. 164. And even if the plaintiff hurdles all these obstacles, and gains a substantial verdict, the individual officer's finances may well make the judgment useless for the municipality, of course, is not liable without its consent. Is it surprising that there is so little in the books concerning trespass actions for violation of the search and seizure clause?</p>
<p>The conclusion is inescapable that but one remedy exists to deter violations of the search and seizure clause. That is the rule which excludes illegally obtained evidence. Only by exclusion can we impress upon the zealous prosecutor that violation of the Constitution will do him no good. And only when that point is driven home can the prosecutor be expected to emphasize the importance of observing constitutional demands in his instructions to the police.</p>
<p>If proof of the efficacy of the federal rule were needed, there is testimony in abundance in the recruit training programs and in-service courses provided the police in states which follow the federal rule.<sup>[5]</sup> St. Louis, for example, demands extensive training in the rules of search and seizure, with emphasis upon the ease with which a case may collapse if it depends upon evidence obtained <span class="star-pagination">*45</span> unlawfully. Current court decisions are digested and read at roll calls. The same general pattern prevails in Washington, D. C.<sup>[6]</sup> In Dallas, officers are thoroughly briefed and instructed that "the courts will follow the rules very closely and will detect any frauds."<sup>[7]</sup> In Milwaukee, a stout volume on the law of arrest and search and seizure is made the basis of extended instruction.<sup>[8]</sup> Officer preparation in the applicable rules in Jackson, Mississippi, has included the lectures of an Associate Justice of the Mississippi Supreme Court. The instructions on evidence and search and seizure given to trainees in San Antonio carefully note the rule of exclusion in Texas, and close with this statement: "Every police officer should know the laws and the rules of evidence. Upon knowledge of these facts determines whether the . . . defendant will be convicted or acquitted. . . . When you investigate a case . . . remember throughout your investigation that only admissible evidence can be used."</p>
<p>But in New York City, we are informed simply that "copies of the State Penal Law and Code of Criminal Procedure" are given to officers, and that they are "kept advised" that illegally obtained evidence may be admitted in New York courts. In Baltimore, a "Digest of Laws" is distributed, and it is made clear that the <span class="star-pagination">*46</span> statutory section excluding evidence "is limited in its application to the trial of misdemeanors. . . . It would appear . . . that . . . evidence illegally obtained may still be admissible in the trial of felonies." In Cleveland, recruits and other officers are told of the rules of search and seizure, but "instructed that it is admissible in the courts of Ohio. The Ohio Supreme Court has indicated very definitely and clearly that Ohio belongs to the `admissionist' group of states when evidence obtained by an illegal search is presented to the court." A similar pattern emerges in Birmingham, Alabama.</p>
<p>The contrast between states with the federal rule and those without it is thus a positive demonstration of its efficacy. There are apparent exceptions to the contrast Denver, for example, appears to provide as comprehensive a series of instructions as that in Chicago, although Colorado permits introduction of the evidence and Illinois does not. And, so far as we can determine from letters, a fairly uniform standard of officer instruction appears in other cities, irrespective of the local rule of evidence. But the examples cited above serve to ground an assumption that has motivated this Court since the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case: that this is an area in which judicial action has positive effect upon the breach of law; and that, without judicial action, there are simply no effective sanctions presently available.</p>
<p>I cannot believe that we should decide due process questions by simply taking a poll of the rules in various jurisdictions, even if we follow the <i><span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/" aria-description="Citation for case: Palko v. Connecticut">Palko</a></span></i> "test." Today's decision will do inestimable harm to the cause of fair police methods in our cities and states. Even more important, perhaps, it must have tragic effect upon public respect for our judiciary. For the Court now allows what is indeed shabby business: lawlessness by officers of the law.</p>
<p><span class="star-pagination">*47</span> Since the evidence admitted was secured in violation of the Fourth Amendment, the judgment should be reversed.</p>
<p>MR. JUSTICE RUTLEDGE, dissenting.</p>
<p>"Wisdom too often never comes, and so one ought not to reject it merely because it comes late." Similarly, one should not reject a piecemeal wisdom, merely because it hobbles toward the truth with backward glances. Accordingly, although I think that all "the specific guarantees of the Bill of Rights should be carried over intact into the first section of the Fourteenth Amendment," <i>Adamson</i> v. <i>California,</i> <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/" aria-description="Citation for case: Adamson v. California">332 U. S. 46</a></span>, dissenting opinion at 124, I welcome the fact that the Court, in its slower progress toward this goal, today finds the substance of the Fourth Amendment "to be implicit in the concept of ordered liberty, and thus, through the Fourteenth Amendment,. . . valid as against the states." <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319, 325</a></span>.</p>
<p>But I reject the Court's simultaneous conclusion that the mandate embodied in the Fourth Amendment, although binding on the states, does not carry with it the one sanctionexclusion of evidence taken in violation of the Amendment's termsfailure to observe which means that "the protection of the Fourth Amendment . . . might as well be stricken from the Constitution." <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#393" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 393</a></span>. For I agree with my brother MURPHY'S demonstration that the Amendment without the sanction is a dead letter. Twenty-nine years ago this Court, speaking through Justice Holmes, refused to permit the Government to subpoena documentary evidence which it had stolen, copied and then returned, for the reason that such a procedure "reduces the Fourth Amendment to a form of words." <i>Silverthrone Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span>. But the version of the Fourth Amendment today held <span class="star-pagination">*48</span> applicable to the states hardly rises to the dignity of a form of words; at best it is a pale and frayed carbon copy of the original, bearing little resemblance to the Amendment the fulfillment of whose command I had heretofore thought to be "an indispensable need for a democratic society." <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span>, dissenting opinion at 161.</p>
<p>I also reject any intimation that Congress could validly enact legislation permitting the introduction in federal courts of evidence seized in violation of the Fourth Amendment. I had thought that issue settled by this Court's invalidation on dual grounds, in <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, of a federal statute which in effect required the production of evidence thought probative by Government counselthe Court there holding the statute to be "obnoxious to the prohibition of the Fourth Amendment of the Constitution, as well as of the Fifth." <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#632" aria-description="Citation for case: Boyd v. United States"><i>Id.</i> at 632</a></span>. See <i>Adams</i> v. <i>New York,</i> <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/#597" aria-description="Citation for case: Adams v. New York">192 U. S. 585, 597, 598</a></span>. The view that the Fourth Amendment itself forbids the introduction of evidence illegally obtained in federal prosecutions is one of long standing and firmly established. See <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#462" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 462</a></span>. It is too late in my judgment to question it now. We apply it today in <i>Lustig</i> v. <i>United States, post,</i> p. 74.</p>
<p>As Congress and this Court are, in my judgment, powerless to permit the admission in federal courts of evidence seized in defiance of the Fourth Amendment, so I think state legislators and judgesif subject to the Amendment, as I believe them to bemay not lend their offices to the admission in state courts of evidence thus seized. Compliance with the Bill of Rights betokens more than lip service.</p>
<p>The Court makes the illegality of this search and seizure its inarticulate premise of decision. I acquiesce in that premise and think the convictions should be reversed.</p>
<p>MR. JUSTICE MURPHY joins in this opinion.</p>
<h2>NOTES</h2>
<p>[1]  The common law provides actions for damages against the searching officer, e. g., <i>Entick</i> v. <i>Carrington,</i> 2 Wils. 275, 19 How. St. Tr. 1029; <i>Grumon</i> v. <i>Raymond,</i> <span class="citation" data-id="6572959"><a href="/opinion/6693083/grumon-v-raymond/" aria-description="Citation for case: Grumon v. Raymond">1 Conn. 40</a></span>; <i>Sandford</i> v. <i>Nichols,</i> <span class="citation" data-id="6404479"><a href="/opinion/6530776/sandford-v-nichols/" aria-description="Citation for case: Sandford v. Nichols">13 Mass. 286</a></span>; <i>Halsted</i> v. <i>Brice,</i> <span class="citation" data-id="6613020"><a href="/opinion/6731385/halsted-v-brice/" aria-description="Citation for case: Halsted v. Brice">13 Mo. 171</a></span>; <i>Hussey</i> v. <i>Davis,</i> 58 N. H. 317; <i>Reed</i> v. <i>Lucas,</i> <span class="citation" data-id="4892398"><a href="/opinion/5076811/reed-v-lucas/" aria-description="Citation for case: Reed v. Lucas">42 Texas 529</a></span>; against one who procures the issuance of a warrant maliciously and without probable cause, e. g., <i>Gulsby</i> v. <i>Louisville &amp; N. R. Co.,</i> <span class="citation" data-id="7365014"><a href="/opinion/7444823/gulsby-v-louisville-nashville-r-r/" aria-description="Citation for case: Gulsby v. Louisville &amp; Nashville R. R.">167 Ala. 122</a></span>, <span class="citation" data-id="7365014"><a href="/opinion/7444823/gulsby-v-louisville-nashville-r-r/" aria-description="Citation for case: Gulsby v. Louisville &amp; Nashville R. R.">52 So. 392</a></span>; <i>Whitson</i> v. <i>May,</i> <span class="citation" data-id="7043683"><a href="/opinion/7136045/whitson-v-may/" aria-description="Citation for case: Whitson v. May">71 Ind. 269</a></span>; <i>Krehbiel</i> v. <i>Henkle,</i> <span class="citation" data-id="7114657"><a href="/opinion/7203240/krehbiel-v-henkle/" aria-description="Citation for case: Krehbiel v. Henkle">152 Iowa 604</a></span>, <span class="citation" data-id="7114378"><a href="/opinion/7202985/roberts-v-playle/" aria-description="Citation for case: Roberts v. Playle">129 N. W. 945</a></span>; <i>Olson</i> v. <i>Tvete,</i> <span class="citation" data-id="7966966"><a href="/opinion/8012053/olson-v-tvete/" aria-description="Citation for case: Olson v. Tvete">46 Minn. 225</a></span>, <span class="citation" data-id="7966966"><a href="/opinion/8012053/olson-v-tvete/" aria-description="Citation for case: Olson v. Tvete">48 N. W. 914</a></span>; <i>Boeger</i> v. <i>Langenberg,</i> <span class="citation" data-id="8009494"><a href="/opinion/8052623/boeger-v-langenberg/" aria-description="Citation for case: Boeger v. Langenberg">97 Mo. 390</a></span>, <span class="citation no-link">11 S. W. 223</span>; <i>Doane</i> v. <i>Anderson,</i> <span class="citation" data-id="5501189"><a href="/opinion/5654770/doane-v-anderson/" aria-description="Citation for case: Doane v. Anderson">60 Hun 586</a></span>, 15 N. Y. S. 459; <i>Shall</i> v. <i>Minneapolis, St. P. &amp; S. S. M. R. Co.,</i> <span class="citation" data-id="8191222"><a href="/opinion/8227270/shall-v-minneapolis-st-paul-sault-ste-marie-railway-co/" aria-description="Citation for case: Shall v. Minneapolis, St. Paul &amp; Sault Ste. Marie Railway...">156 Wis. 195</a></span>, <span class="citation" data-id="8191222"><a href="/opinion/8227270/shall-v-minneapolis-st-paul-sault-ste-marie-railway-co/" aria-description="Citation for case: Shall v. Minneapolis, St. Paul &amp; Sault Ste. Marie Railway...">145 N. W. 649</a></span>; against a magistrate who has acted without jurisdiction in issuing a warrant, e. g., <i>Williams</i> v. <i>Kozak,</i> <span class="citation" data-id="8825314"><a href="/opinion/8840170/williams-v-kozak/" aria-description="Citation for case: Williams v. Kozak">280 F. 373</a></span> (C. A. 4th Cir.); <i>Grumon</i> v. <i>Raymond,</i> <span class="citation" data-id="6572959"><a href="/opinion/6693083/grumon-v-raymond/" aria-description="Citation for case: Grumon v. Raymond">1 Conn. 40</a></span>; <i>Kennedy</i> v. <i>Terrill,</i> Hardin (Ky.) 490; <i>Shaw</i> v. <i>Moon,</i> <span class="citation" data-id="3839135"><a href="/opinion/4080582/shaw-v-moon/" aria-description="Citation for case: Shaw v. Moon">117 Ore. 558</a></span>, <span class="citation" data-id="3839135"><a href="/opinion/4080582/shaw-v-moon/" aria-description="Citation for case: Shaw v. Moon">245 P. 318</a></span>; and against persons assisting in the execution of an illegal search, e. g., <i>Hebrew</i> v. <i>Pulis,</i> 73 N. J. L. 621, 625, <span class="citation" data-id="8271776"><a href="/opinion/8304929/hebrew-v-pulis/#122" aria-description="Citation for case: Hebrew v. Pulis">64 A. 121, 122</a></span>; <i>Cartwright</i> v. <i>Canode,</i> <span class="citation" data-id="3932614"><a href="/opinion/4166002/cartwright-v-canode/" aria-description="Citation for case: Cartwright v. Canode">138 S. W. 792</a></span> (Tex. Civ. App.), aff'd, <span class="citation" data-id="3907069"><a href="/opinion/4143577/cartwright-v-canode/" aria-description="Citation for case: Cartwright v. Canode">106 Texas 502</a></span>, <span class="citation" data-id="3907069"><a href="/opinion/4143577/cartwright-v-canode/" aria-description="Citation for case: Cartwright v. Canode">171 S. W. 696</a></span>. One may also without liability use force to resist an unlawful search. E. g., <i>Commonwealth</i> v. <i>Martin,</i> <span class="citation" data-id="6416154"><a href="/opinion/6542429/commonwealth-v-certain-intoxicating-liquors/" aria-description="Citation for case: Commonwealth v. Certain Intoxicating Liquors">105 Mass. 178</a></span>; <i>State</i> v. <i>Mann,</i> <span class="citation" data-id="3659541"><a href="/opinion/3913233/state-v-mann/" aria-description="Citation for case: State v. Mann">27 N. C. 45</a></span>.
</p>
<p>Statutory sanctions in the main provide for the punishment of one maliciously procuring a search warrant or willfully exceeding his authority in exercising it. <i>E. g.,</i> 18 U. S. C. (1946 ed.) §§ 630, 631; Ala. Code, Tit. 15, § 99 (1940); Ariz. Code Ann. § 44-3513 (1939); <span class="citation no-link">Fla. Stat. Ann. §§ 933.16</span>, 933.17 (1944); <span class="citation no-link">Iowa Code §§ 751.38</span>, 751.39 (1946); Mont. Rev. Code Ann. §§ 10948, 10952 (1935); Nev. Comp. Laws §§ 10425, 10426 (1929); N. Y. Crim. Code §§ 811, 812, N. Y. Penal Law §§ 1786, 1847; N. D. Rev. Code §§ 12-1707, 12-1708 (1943); Okla. Stat. Ann., Tit. 21, §§ 536, 585, Tit. 22, §§ 1239, 1240 (1937); Ore. Comp. Laws Ann. § 26-1717 (1940); S. D. Code §§ 13.1213, 13.1234, 34.9904, 34.9905 (1939); <span class="citation no-link">Tenn. Code Ann. § 11905</span> (1934). Some statutes more broadly penalize unlawful searches. <i>E. g.,</i> 18 U. S. C. (1946 ed.) § 53a; <span class="citation no-link">Idaho Code Ann. §§ 17-1004</span>, 17-1024 (1932); <span class="citation no-link">Minn. Stat. §§ 613.54</span>, 621.17 (1945); Va. Code Ann. § 4822d (Michie, 1942); Wash. Rev. Stat. Ann. §§ 2240-1, 2240-2. Virginia also makes punishable one who issues a general search warrant or a warrant unsupported by affidavit. Va. Code Ann. § 4822e (Michie, 1942). A few States have provided statutory civil remedies. See, <i>e. g.,</i> <span class="citation no-link">Ga. Code Ann. § 27-301</span> (1935); Ill. Rev. Stat., c. 38, § 698 (Smith-Hurd, 1935); <span class="citation no-link">Miss. Code Ann. § 1592</span> (1942). And in one State, misuse of a search warrant may be an abuse of process punishable as contempt of court. See Mich. Stat. Ann. § 27.511 (1938).</p>
<p>[2]  "We hold, then, with the defendant that the evidence against him was the outcome of a trespass. The officer might have been resisted, or sued for damages, or even prosecuted for oppression (Penal Law, §§ 1846, 1847). He was subject to removal or other discipline at the hands of his superiors. These consequences are undisputed. The defendant would add another. We must determine whether evidence of criminality, procured by an act of trespass, is to be rejected as incompetent for the misconduct of the trespasser. . . .
</p>
<p>"Those judgments [<i>Weeks</i> v. <i>United States</i> and cases which followed it] do not bind us, for they construe provisions of the Federal Constitution, the Fourth and Fifth Amendments, not applicable to the States. Even though not binding, they merit our attentive scrutiny. . . .</p>
<p>"In so holding [<i>i. e.,</i> that evidence procured by unlawful search is not incompetent], we are not unmindful of the argument that unless the evidence is excluded, the statute becomes a form and its protection an illusion. This has a strange sound when the immunity is viewed in the light of its origin and history. The rule now embodied in the statute was received into English law as the outcome of the prosecution of Wilkes and Entick . . . . Wilkes sued the messengers who had ransacked his papers, and recovered a verdict of £4,000 against one and £1,000 against the other. Entick, too, had a substantial verdict . . . . We do not know whether the public, represented by its juries, is to-day more indifferent to its liberties than it was when the immunity was born. If so, the change of sentiment without more does not work a change of remedy. Other sanctions, penal and disciplinary, supplementing the right to damages, have already been enumerated. No doubt the protection of the statute would be greater from the point of view of the individual whose privacy had been invaded if the government were required to ignore what it had learned through the invasion. The question is whether protection for the individual would not be gained at a disproportionate loss of protection for society. On the one side is the social need that crime shall be repressed. On the other, the social need that law shall not be flouted by the insolence of office. There are dangers in any choice. The rule of the <i>Adams</i> case [<span class="citation multiple-matches"><a href="/c/N.%20Y./176/351/">176 N. Y. 351</a></span>, <span class="citation" data-id="3588018"><a href="/opinion/3606309/people-v-adams/" aria-description="Citation for case: People v. . Adams">68 N. E. 636</a></span>] strikes a balance between opposing interests." <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#19" aria-description="Citation for case: People v. Defore">242 N. Y. at 19, 20, 24-25</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#586" aria-description="Citation for case: People v. Defore">150 N. E. at 586-87, 587, 588-89</a></span>.</p>
<p>[*]  In the case of jurisdictions which have decided more than one case in point, the following Tables cite only the leading case.</p>
<p>[1]  See Pound, Criminal Justice in America (New York, 1930): "Under our legal system the way of the prosecutor is hard, and the need of `getting results' puts pressure upon prosecutors to . . . indulge in that lawless enforcement of law which produces a vicious circle of disrespect for law." P. 186.
</p>
<p>And note the statement of the Wickersham Commission, with reference to arrests: ". . . in case of persons of no influence or little or no means the legal restrictions are not likely to give an officer serious trouble." II National Commission on Law Observance and Enforcement, Report on Criminal Procedure (1931), p. 19.</p>
<p>[2]  See McCormick, Damages, § 78. See Willis, <i>Measure of Damages When Property is Wrongfully Taken by a Private Individual,</i> <span class="citation no-link">22 Harv. L. Rev. 419</span>.</p>
<p>[3]  <i><span class="citation no-link">Id.,</span></i> § 79. See <i>Fennemore</i> v. <i>Armstrong,</i> <span class="citation" data-id="6556335"><a href="/opinion/6677276/fennemore-v-armstrong/" aria-description="Citation for case: Fennemore v. Armstrong">29 Del. 35</a></span>, <span class="citation" data-id="6556335"><a href="/opinion/6677276/fennemore-v-armstrong/" aria-description="Citation for case: Fennemore v. Armstrong">96 A. 204</a></span>.</p>
<p>[4]  "It is a well settled and almost universally accepted rule in the law of damages that a finding of exemplary damages must be predicated upon a finding of actual damages." <span class="citation no-link">17 Iowa L. Rev. 413</span>, 414. This appears to be an overstatement. See McCormick, <i>supra,</i> § 83; Restatement IV, Torts, § 908, comment <i>c.</i></p>
<p>[5]  The material which follows is gleaned from letters and other material from Commissioners of Police and Chiefs of Police in twenty-six cities. Thirty-eight large cities in the United States were selected at random, and inquiries directed concerning the instructions provided police on the rules of search and seizure. Twenty-six replies have been received to date. Those of any significance are mentioned in the text of this opinion. The sample is believed to be representative, but it cannot, of course, substitute for a thoroughgoing comparison of present-day police procedures by a completely objective observer. A study of this kind would be of inestimable value.</p>
<p>[6]  <i>E. g.,</i> Assistant Superintendent Truscott's letter to the Washington Police Force of January 3, 1949, concerning <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>.</p>
<p>[7]  Recently lectures have included two pages of discussion of the opinions in <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span>.</p>
<p>[8]  Chief of Police John W. Polcyn notes, in a Foreword to the book, that officers were often not properly informed with respect to searches and seizures before thoroughgoing instruction was undertaken. One of their fears was that of "losing their cases in court, only because they neglected to do what they might have done with full legal sanction at the time of the arrest, or did what they had no legal right to do at such time."</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Wong Sun v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Wong Sun v. United States"
type: case
citation: "371 U.S. 471 (1963)"
parallel_cite: "83 S. Ct. 407; 9 L. Ed. 2d 441"
neutral_cite: 1963 U.S. LEXIS 2431
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1963
date_decided: 1963-01-14
docket: 36
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1963-01-14
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Wong Sun v. United States
  varies_by_point: false
  scope_note: "Foundational fruit-of-the-poisonous-tree / attenuation case; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106515/wong-sun-v-united-states/"
  cluster_id: 106515
  opinion_id: 106515
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Anchor"
related: ["[[Brown v. Illinois]]", "[[Utah v. Strieff]]", "[[Nix v. Williams]]"]
aliases: ["Wong Sun"]
tags: ["case", "fourth-amendment", "exclusionary-rule", "fruit-of-the-poisonous-tree", "attenuation"]
holding: "'Fruit of the poisonous tree': derivative evidence is suppressed if come at by exploitation of the primary illegality, not merely 'but…"
lake:
  record_id: Wong Sun v. United States
  status: verified
  projected_at: 2026-07-06
---

# Wong Sun v. United States

*371 U.S. 471 (1963)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal narcotics agents, acting without probable cause, broke into James Wah Toy's living quarters and arrested him; in his bedroom Toy made statements implicating "Johnny" Yee. Agents went to Yee, who surrendered heroin and implicated Toy and Wong Sun. Both were arrested without probable cause, arraigned, and released on their own recognizance. Several days later, each voluntarily returned and gave an unsigned statement. Toy and Wong Sun moved to suppress the statements and the heroin as fruits of the unlawful police conduct.

## Issue
Whether verbal statements and physical evidence obtained as a consequence of an unlawful arrest must be excluded as "fruit of the poisonous tree," and how to determine when the connection to the illegality is too attenuated to require suppression.

## Rule
Not every consequence of police illegality is suppressed; "but for" causation is not the test. The Court rejected the idea that all evidence is "'fruit of the poisonous tree' simply because it would not have come to light but for the illegal actions of the police." Instead, "the more apt question … is 'whether, granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint.'" — 371 U.S. at 487–488. ^pin-488

Where the link between the illegality and the evidence is sufficiently weakened, the taint dissipates: evidence is admissible when "the connection between the arrest and the statement had 'become so attenuated as to dissipate the taint.'" — *Id.* at 491. ^pin-491

## Application
Applying that test to each defendant's evidence, the Court reached different results. Toy's bedroom statements were come at by exploitation of the agents' unlawful entry — they followed immediately on the illegal break-in and were not purged of the primary taint — so they were suppressed; and the heroin Yee surrendered, traced through Toy's tainted statements, was inadmissible against Toy for the same reason. Wong Sun's statement was different: he had been released on his own recognizance after arraignment and returned voluntarily several days later, so the connection between his unlawful arrest and his statement had become so attenuated as to dissipate the taint, and the statement was admissible. (Wong Sun's conviction was nonetheless reversed because of corroboration concerns.)

## Conclusion
Evidence obtained by exploiting an unlawful arrest is suppressed as [[Common Legal Terms#fruit-of-the-poisonous-tree|fruit of the poisonous tree]], but evidence sufficiently attenuated from the illegality is admissible. The judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Wong Sun* is the foundational fruit-of-the-poisonous-tree case; its [[Fruits and Attenuation|attenuation]] inquiry was given concrete factors in [[Brown v. Illinois]] and applied to an intervening arrest warrant in [[Utah v. Strieff]]. The related independent-source and inevitable-discovery limits appear in [[Nix v. Williams]].

## Appears on
- [[The Exclusionary Rule]] — *Key — Anchor*

## Sources
- *Wong Sun v. United States*, 371 U.S. 471 (1963) — https://www.courtlistener.com/opinion/106515/wong-sun-v-united-states/ — pinpoints: 487–488, 491.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "809f5c187032b9c0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Wong Sun v. United States"}, "payload": {"all": [{"cite": "371 U.S. 471", "page": "471", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "371"}, {"cite": "83 S. Ct. 407", "page": "407", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "83"}, {"cite": "9 L. Ed. 2d 441", "page": "441", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "9"}, {"cite": "1963 U.S. LEXIS 2431", "page": "2431", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1963"}], "display": "371 U.S. 471", "official": {"cite": "371 U.S. 471", "page": "471", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "371"}, "official_selection_present": true, "record_id": "Wong Sun v. United States"}}
{"assertion_id": "17257bbb3de904d8", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-491", "record_id": "Wong Sun v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-491", "pinpoint_status": "slip-only", "quote": "the connection between the arrest and the statement had 'become so attenuated as to dissipate the taint.'", "quote_fidelity": "mismatch", "record_id": "Wong Sun v. United States", "star_marker": null}}
{"assertion_id": "e9abdc45a82e759a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-488", "record_id": "Wong Sun v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-488", "pinpoint_status": "slip-only", "quote": "and how to determine when the connection to the illegality is too attenuated to require suppression. ## Rule Not every consequence of police illegality is suppressed;", "quote_fidelity": "mismatch", "record_id": "Wong Sun v. United States", "star_marker": null}}
{"assertion_id": "d98bbfea2668bdc8", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Wong Sun v. United States"}, "payload": {"as_of_content": "1963-01-14", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Wong Sun v. United States", "scope_note": "Foundational fruit-of-the-poisonous-tree / attenuation case; good law.", "varies_by_point": false}}
```

### lake record — Wong Sun v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Wong Sun v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Wong Sun v. United States",
    "case_name_short": "Wong Sun",
    "case_name_full": "WONG SUN Et Al. v. UNITED STATES",
    "input_case_name": "Wong Sun v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1963-01-14",
    "year": 1963,
    "docket": "36",
    "cluster_id": 106515,
    "lead_opinion_id": 106515,
    "sibling_ids": [
      106515,
      9422515,
      9422516
    ],
    "absolute_url": "/opinion/106515/wong-sun-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "371 U.S. 471",
      "volume": "371",
      "reporter": "U.S.",
      "page": "471",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "83 S. Ct. 407",
        "volume": "83",
        "reporter": "S. Ct.",
        "page": "407",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "9 L. Ed. 2d 441",
        "volume": "9",
        "reporter": "L. Ed. 2d",
        "page": "441",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1963 U.S. LEXIS 2431",
        "volume": "1963",
        "reporter": "U.S. LEXIS",
        "page": "2431",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "371 U.S. 471",
        "volume": "371",
        "reporter": "U.S.",
        "page": "471",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 S. Ct. 407",
        "volume": "83",
        "reporter": "S. Ct.",
        "page": "407",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "9 L. Ed. 2d 441",
        "volume": "9",
        "reporter": "L. Ed. 2d",
        "page": "441",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1963 U.S. LEXIS 2431",
        "volume": "1963",
        "reporter": "U.S. LEXIS",
        "page": "2431",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "371 U.S. 471",
    "official_selection": {
      "court_class": "scotus",
      "selected": "371 U.S. 471",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-488",
      "page": null,
      "quote": "and how to determine when the connection to the illegality is too attenuated to require suppression. ## Rule Not every consequence of police illegality is suppressed;",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-491",
      "page": null,
      "quote": "the connection between the arrest and the statement had 'become so attenuated as to dissipate the taint.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1963-01-14",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Wong Sun v. United States",
    "varies_by_point": false,
    "scope_note": "Foundational fruit-of-the-poisonous-tree / attenuation case; good law.",
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
        "journal_ref": "Wong Sun v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jenkins v. State",
          "cluster_id": 10680001,
          "cite": [
            "894 S.E.2d 566",
            "317 Ga. 585"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Serrano (A173250)",
          "cluster_id": 10135658,
          "cite": [
            "324 Or. App. 453",
            "527 P.3d 54"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Gumkowski",
          "cluster_id": 4880252,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Terry v. Ohio",
          "cluster_id": 107729,
          "cite": [
            "20 L. Ed. 2d 889",
            "88 S. Ct. 1868",
            "392 U.S. 1",
            "1968 U.S. LEXIS 1345",
            "44 Ohio Op. 2d 383"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Katz v. United States",
          "cluster_id": 107564,
          "cite": [
            "19 L. Ed. 2d 576",
            "88 S. Ct. 507",
            "389 U.S. 347",
            "1967 U.S. LEXIS 2"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wade",
          "cluster_id": 107486,
          "cite": [
            "18 L. Ed. 2d 1149",
            "87 S. Ct. 1926",
            "388 U.S. 218",
            "1967 U.S. LEXIS 1085"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beck v. Ohio",
          "cluster_id": 106936,
          "cite": [
            "13 L. Ed. 2d 142",
            "85 S. Ct. 223",
            "379 U.S. 89",
            "1964 U.S. LEXIS 151",
            "3 Ohio Misc. 71",
            "31 Ohio Op. 2d 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McMann v. Richardson",
          "cluster_id": 108138,
          "cite": [
            "25 L. Ed. 2d 763",
            "90 S. Ct. 1441",
            "397 U.S. 759",
            "1970 U.S. LEXIS 46"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stone v. Powell",
          "cluster_id": 109540,
          "cite": [
            "49 L. Ed. 2d 1067",
            "96 S. Ct. 3037",
            "428 U.S. 465",
            "1976 U.S. LEXIS 86"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gilbert v. California",
          "cluster_id": 107487,
          "cite": [
            "18 L. Ed. 2d 1178",
            "87 S. Ct. 1951",
            "388 U.S. 263",
            "1967 U.S. LEXIS 1086"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Calandra",
          "cluster_id": 108898,
          "cite": [
            "38 L. Ed. 2d 561",
            "94 S. Ct. 613",
            "414 U.S. 338",
            "1974 U.S. LEXIS 145",
            "66 Ohio Op. 2d 320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warden, Maryland Penitentiary v. Hayden",
          "cluster_id": 107465,
          "cite": [
            "18 L. Ed. 2d 782",
            "87 S. Ct. 1642",
            "387 U.S. 294",
            "1967 U.S. LEXIS 2753"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ker v. California",
          "cluster_id": 106641,
          "cite": [
            "10 L. Ed. 2d 726",
            "83 S. Ct. 1623",
            "374 U.S. 23",
            "1963 U.S. LEXIS 2473",
            "24 Ohio Op. 2d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "110OAG40",
          "cluster_id": 10638768,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane3_recency"
      },
      {
        "citing_case": {
          "name": "Maryland Attorney General Opinion 110OAG40",
          "cluster_id": 10848272,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane3_recency"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106515 OR 9422515 OR 9422516) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjIwMDg2NDAwMDAwJnM9NDg4MDI1MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106515+OR+9422515+OR+9422516%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(106515 OR 9422515 OR 9422516)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDY4JnM9MTExMjE0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106515+OR+9422515+OR+9422516%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106515 OR 9422515 OR 9422516)",
        "reviewed": 147,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 147,
        "triage_read": 4,
        "triage_snippet_classified": 143
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106515 OR 9422515 OR 9422516)",
    "indexed_citing_opinions": 8572,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106515,
        "count": 7826,
        "count_source": "search"
      },
      {
        "opinion_id": 9422515,
        "count": 934,
        "count_source": "search"
      },
      {
        "opinion_id": 9422516,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 12874,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/wong-sun-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0ODYzNDQmcz0xMDY1MTU1NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28106515+OR+9422515+OR+9422516%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106515,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 94334,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 94447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 94565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 94573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 103663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 104336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 104440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 104646,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105256,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 233231,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 234904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 235392,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 236713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 237954,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 242778,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 246074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 246966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 248139,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 251634,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 253508,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 1424394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 1428666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 1478266,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 1507600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 1512100,
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
    "date_created": "2026-07-06T04:43:58Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:44:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:44:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:46:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:44:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Wong Sun v. United States

```
<div>
<center><b><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U.S. 471</a></span> (1963)</b></center>
<center><h1>WONG SUN ET AL.<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 36.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 29 and April 2, 1962.</center>
<center>Restored to calendar for reargument June 4, 1962.</center>
<center>Reargued October 8, 1962.</center>
<center>Decided January 14, 1963.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><span class="star-pagination">*472</span> <i>Edward Bennett Williams,</i> acting under appointment by the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./368/973/">368 U. S. 973</a></span>, reargued the cause and filed a supplemental brief for petitioners. <i>Sol A. Abrams</i> also filed a brief for petitioners.</p>
<p><i>J. William Doolittle</i> reargued the cause for the United States. On the brief were <i>Solicitor General Cox, Assistant Attorney General Miller, Beatrice Rosenberg</i> and <i>J. F. Bishop.</i></p>
<p>MR. JUSTICE BRENNAN delivered the opinion of the Court.</p>
<p>The petitioners were tried without a jury in the District Court for the Northern District of California under a two-count indictment for violation of the Federal Narcotics <span class="star-pagination">*473</span> Laws, <span class="citation no-link">21 U. S. C. § 174</span>.<sup>[1]</sup> They were acquitted under the first count which charged a conspiracy, but convicted under the second count which charged the substantive offense of fraudulent and knowing transportation and concealment of illegally imported heroin. The Court of Appeals for the Ninth Circuit, one judge dissenting, affirmed the convictions. <span class="citation" data-id="9447810"><a href="/opinion/253508/wong-sun-and-james-wah-toy-v-united-states/" aria-description="Citation for case: Wong Sun and James Wah Toy v. United States">288 F. 2d 366</a></span>. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./368/817/">368 U. S. 817</a></span>. We heard argument in the 1961 Term and reargument this Term. <span class="citation multiple-matches"><a href="/c/U.%20S./370/908/">370 U. S. 908</a></span>.</p>
<p>About 2 a. m. on the morning of June 4, 1959, federal narcotics agents in San Francisco, after having had one Hom Way under surveillance for six weeks, arrested him and found heroin in his possession. Hom Way, who had not before been an informant, stated after his arrest that he had bought an ounce of heroin the night before from one known to him only as "Blackie Toy," proprietor of a laundry on Leavenworth Street.</p>
<p>About 6 a. m. that morning six or seven federal agents went to a laundry at 1733 Leavenworth Street. The sign <span class="star-pagination">*474</span> above the door of this establishment said "Oye's Laundry." It was operated by the petitioner James Wah Toy. There is, however, nothing in the record which identifies James Wah Toy and "Blackie Toy" as the same person. The other federal officers remained nearby out of sight while Agent Alton Wong, who was of Chinese ancestry, rang the bell. When petitioner Toy appeared and opened the door, Agent Wong told him that he was calling for laundry and dry cleaning. Toy replied that he didn't open until 8 o'clock and told the agent to come back at that time. Toy started to close the door. Agent Wong thereupon took his badge from his pocket and said, "I am a federal narcotics agent." Toy immediately "slammed the door and started running" down the hallway through the laundry to his living quarters at the back where his wife and child were sleeping in a bedroom. Agent Wong and the other federal officers broke open the door and followed Toy down the hallway to the living quarters and into the bedroom. Toy reached into a nightstand drawer. Agent Wong thereupon drew his pistol, pulled Toy's hand out of the drawer, placed him under arrest and handcuffed him. There was nothing in the drawer and a search of the premises uncovered no narcotics.</p>
<p>One of the agents said to Toy ". . . [Hom Way] says he got narcotics from you." Toy responded, "No. I haven't been selling any narcotics at all. However, I do know somebody who has." When asked who that was, Toy said, "I only know him as Johnny. I don't know his last name." However, Toy described a house on Eleventh Avenue where he said Johnny lived; he also described a bedroom in the house where he said "Johnny kept about a piece"<sup>[2]</sup> of heroin and where he and Johnny had smoked some of the drug the night before. The agents <span class="star-pagination">*475</span> left immediately for Eleventh Avenue and located the house. They entered and found one Johnny Yee in the bedroom. After a discussion with the agents, Yee took from a bureau drawer several tubes containing in all just less than one ounce of heroin, and surrendered them. Within the hour Yee and Toy were taken to the Office of the Bureau of Narcotics. Yee there stated that the heroin had been brought to him some four days earlier by petitioner Toy and another Chinese known to him only as "Sea Dog."</p>
<p>Toy was questioned as to the identity of "Sea Dog" and said that "Sea Dog" was Wong Sun. Some agents, including Agent Alton Wong, took Toy to Wong Sun's neighborhood where Toy pointed out a multifamily dwelling where he said Wong Sun lived. Agent Wong rang a downstairs door bell and a buzzer sounded, opening the door. The officer identified himself as a narcotics agent to a woman on the landing and asked "for Mr. Wong." The woman was the wife of petitioner Wong Sun. She said that Wong Sun was "in the back room sleeping." Alton Wong and some six other officers climbed the stairs and entered the apartment. One of the officers went into the back room and brought petitioner Wong Sun from the bedroom in handcuffs. A thorough search of the apartment followed, but no narcotics were discovered.</p>
<p>Petitioner Toy and Johnny Yee were arraigned before a United States Commissioner on June 4 on a complaint charging a violation of <span class="citation no-link">21 U. S. C. § 174</span>. Later that day, each was released on his own recognizance. Petitioner Wong Sun was arraigned on a similar complaint filed the next day and was also released on his own recognizance.<sup>[3]</sup><span class="star-pagination">*476</span> Within a few days, both petitioners and Yee were interrogated at the office of the Narcotics Bureau by Agent William Wong, also of Chinese ancestry.<sup>[4]</sup> The agent advised each of the three of his right to withhold information which might be used against him, and stated to each that he was entitled to the advice of counsel, though it does not appear that any attorney was present during the questioning of any of the three. The officer also explained to each that no promises or offers of immunity or leniency were being or could be made.</p>
<p>The agent interrogated each of the three separately. After each had been interrogated the agent prepared a statement in English from rough notes. The agent read petitioner Toy's statement to him in English and interpreted certain portions of it for him in Chinese. Toy also read the statement in English aloud to the agent, said there were corrections to be made, and made the corrections in his own hand. Toy would not sign the statement, however; in the agent's words "he wanted to know first if the other persons involved in the case had signed theirs." Wong Sun had considerable difficulty understanding the <span class="star-pagination">*477</span> statement in English and the agent restated its substance in Chinese. Wong Sun refused to sign the statement although he admitted the accuracy of its contents.<sup>[5]</sup></p>
<p>Hom Way did not testify at petitioners' trial. The Government offered Johnny Yee as its principal witness but excused him after he invoked the privilege against self-incrimination and flatly repudiated the statement he had given to Agent William Wong. That statement was not offered in evidence nor was any testimony elicited from him identifying either petitioner as the source of the heroin in his possession, or otherwise tending to support the charges against the petitioners.</p>
<p>The statute expressly provides that proof of the accused's possession of the drug will support a conviction under the statute unless the accused satisfactorily explains the possession. The Government's evidence tending to prove the petitioners' possession (the petitioners offered no exculpatory testimony) consisted of four items which the trial court admitted over timely objections that they were inadmissible as "fruits" of unlawful arrests or of attendant searches: (1) the statements made orally by petitioner Toy in his bedroom at the time of his arrest; (2) the heroin surrendered to the agents by Johnny Yee; (3) petitioner Toy's pretrial unsigned statement; and (4) petitioner Wong Sun's similar statement. The dispute below and here has centered around the correctness of the rulings of the trial judge allowing these items in evidence.</p>
<p>The Court of Appeals held that the arrests of both petitioners were illegal because not based on " `probable cause' within the meaning of the Fourth Amendment" nor "reasonable grounds" within the meaning of the Narcotic <span class="star-pagination">*478</span> Control Act of 1956.<sup>[6]</sup> The Court said as to Toy's arrest, "There is no showing in this case that the agent knew Hom Way to be reliable," and, furthermore, found "nothing in the circumstances occurring at Toy's premises that would provide sufficient justification for his arrest without a warrant." <span class="citation" data-id="9447810"><a href="/opinion/253508/wong-sun-and-james-wah-toy-v-united-states/#369" aria-description="Citation for case: Wong Sun and James Wah Toy v. United States">288 F. 2d, at 369, 370</a></span>. As to Wong Sun's arrest, the Court said "there is no showing that Johnnie Yee was a reliable informer." The Court of Appeals nevertheless held that the four items of proof were not the "fruits" of the illegal arrests and that they were therefore properly admitted in evidence.</p>
<p>The Court of Appeals rejected two additional contentions of the petitioners. The first was that there was insufficient evidence to corroborate the petitioners' unsigned admissions of possession of narcotics. The court held that the narcotics in evidence surrendered by Johnny Yee, together with Toy's statements in his bedroom at the time of arrest corroborated petitioners' admissions. The second contention was that the confessions were <span class="star-pagination">*479</span> inadmissible because they were not signed. The Court of Appeals held on this point that the petitioners were not prejudiced, since the agent might properly have testified to the substance of the conversations which produced the statements.</p>
<p>We believe that significant differences between the cases of the two petitioners require separate discussion of each. We shall first consider the case of petitioner Toy.</p>
<p></p>
<h2>I.</h2>
<p>The Court of Appeals found there was neither reasonable grounds nor probable cause for Toy's arrest. Giving due weight to that finding, we think it is amply justified by the facts clearly shown on this record. It is basic that an arrest with or without a warrant must stand upon firmer ground than mere suspicion, see <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#101" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 101</a></span>, though the arresting officer need not have in hand evidence which would suffice to convict. The quantum of information which constitutes probable causeevidence which would "warrant a man of reasonable caution in the belief" that a felony has been committed, <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>, 162must be measured by the facts of the particular case. The history of the use, and not infrequent abuse, of the power to arrest cautions that a relaxation of the fundamental requirements of probable cause would "leave law-abiding citizens at the mercy of the officers' whim or caprice."<sup>[7]</sup><i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span>.</p>
<p>Whether or not the requirements of reliability and particularity of the information on which an officer may act are more stringent where an arrest warrant is absent, they surely cannot be less stringent than where an arrest warrant is obtained. Otherwise, a principal incentive now <span class="star-pagination">*480</span> existing for the procurement of arrest warrants would be destroyed.<sup>[8]</sup> The threshold question in this case, therefore, is whether the officers could, on the information which impelled them to act, have procured a warrant for the arrest of Toy. We think that no warrant would have issued on evidence then available.</p>
<p>The narcotics agents had no basis in experience for confidence in the reliability of Hom Way's information; he had never before given information. And yet they acted upon his imprecise suggestion that a person described only as "Blackie Toy," the proprietor of a laundry somewhere on Leavenworth Street, had sold one ounce of heroin. We have held that identification of the suspect by a reliable informant may constitute probable cause for arrest where the information given is sufficiently accurate to lead the officers directly to the suspect. <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span>. That rule does not, however, fit this case. For aught that the record discloses, Hom Way's accusation merely invited the officers to roam the length of Leavenworth Street (some 30 blocks) in search of one "Blackie Toy's" laundryand whether by chance or other <span class="star-pagination">*481</span> means (the record does not say) they came upon petitioner Toy's laundry, which bore not his name over the door, but the unrevealing label "Oye's." Not the slightest intimation appears on the record, or was made on oral argument, to suggest that the agents had information giving them reason to equate "Blackie" Toy and James Wah Toy<i>e. g.,</i> that they had the criminal record of a Toy, or that they had consulted some other kind of official record or list, or had some information of some kind which had narrowed the scope of their search to this particular Toy.</p>
<p>It is conceded that the officers made no attempt to obtain a warrant for Toy's arrest. The simple fact is that on the sparse information at the officers' command, no arrest warrant could have issued consistently with Rules 3 and 4 of the Federal Rules of Criminal Procedure. <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#486" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 486</a></span>.<sup>[9]</sup> The arrest warrant procedure serves to insure that the deliberate, impartial judgment of a judicial officer will be interposed <span class="star-pagination">*482</span> between the citizen and the police, to assess the weight and credibility of the information which the complaining officer adduces as probable cause. Cf. <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#270" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 270</a></span>. To hold that an officer may act in his own, unchecked discretion upon information too vague and from too untested a source to permit a judicial officer to accept it as probable cause for an arrest warrant, would subvert this fundamental policy.</p>
<p>The Government contends, however, that any defects in the information which somehow took the officers to petitioner Toy's laundry were remedied by events which occurred after they arrived. Specifically, it is urged that Toy's flight down the hall when the supposed customer at the door revealed that he was a narcotics agent adequately corroborates the suspicion generated by Hom Way's accusation. Our holding in <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">357 U. S. 301</a></span>, is relevant here, and exposes the fallacy of this contention. We noted in that case that the lawfulness of an officer's entry to arrest without a warrant "must be tested by criteria identical with those embodied in <span class="citation no-link">18 U. S. C. § 3109</span>, which deals with entry to execute a search warrant." 357 U. S., at 306. That statute requires that an officer must state his authority and his purpose at the threshold, and be refused admittance, before he may break open the door. We held that when an officer insufficiently or unclearly identifies his office or his mission, the occupant's flight from the door must be regarded as ambiguous conduct. We expressly reserved the question "whether the unqualified requirements of the rule admit of an exception justifying noncompliance in exigent circumstances." 357 U. S., at 309. In the instant case, Toy's flight from the door afforded no surer an inference of guilty knowledge than did the suspect's conduct in the <i><span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">Miller</a></span></i> case. Agent Wong did eventually disclose that he was a narcotics officer. However, he affirmatively misrepresented his mission at the <span class="star-pagination">*483</span> outset, by stating that he had come for laundry and dry cleaning. And before Toy fled, the officer never adequately dispelled the misimpression engendered by his own ruse. Cf. <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>; <i>Gatewood</i> v. <i>United States,</i> <span class="citation" data-id="9444040"><a href="/opinion/233231/gatewood-v-united-states/" aria-description="Citation for case: Gatewood v. United States">209 F. 2d 789</a></span>.</p>
<p>Moreover, he made no effort at that time, nor indeed at any time thereafter, to ascertain whether the man at the door was the "Blackie Toy" named by Hom Way. Therefore, this is not the case we hypothesized in <i><span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">Miller</a></span></i> where "without an express announcement of purpose, the facts known to officers would justify them in being virtually certain" that the person at the door knows their purpose. 357 U. S., at 310. Toy's refusal to admit the officers and his flight down the hallway thus signified a guilty knowledge no more clearly than it did a natural desire to repel an apparently unauthorized intrusion.<sup>[10]</sup> Here, as in <i><span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">Miller</a></span>,</i> <span class="star-pagination">*484</span> the Government claims no extraordinary circumstances such as the imminent destruction of vital evidence, or the need to rescue a victim in perilsee 357 U. S., at 309 which excused the officer's failure truthfully to state his mission before he broke in.</p>
<p>A contrary holding here would mean that a vague suspicion could be transformed into probable cause for arrest by reason of ambiguous conduct which the arresting officers themselves have provoked. Cf. <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#104" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 104</a></span>. That result would have the same essential vice as a proposition we have consistently rejectedthat a search unlawful at its inception may be validated by what it turns up. <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U. S. 28</a></span>; <i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#595" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 595</a></span>. Thus we conclude that the Court of Appeals' finding that the officers' uninvited entry into Toy's living quarters was unlawful and that the bedroom arrest which followed was likewise unlawful, was fully justified on the evidence. It remains to be seen what consequences flow from this conclusion.</p>
<p></p>
<h2>II.</h2>
<p>It is conceded that Toy's declarations in his bedroom are to be excluded if they are held to be "fruits" of the agents' unlawful action.</p>
<p>In order to make effective the fundamental constitutional guarantees of sanctity of the home and inviolability of the person, <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, this Court held nearly half a century ago that evidence seized during an unlawful search could not constitute proof against the victim of the search. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>. The exclusionary prohibition extends as well to the indirect as the direct products of such invasions. <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> 251 <span class="star-pagination">*485</span> U. S. 385. Mr. Justice Holmes, speaking for the Court in that case, in holding that the Government might not make use of information obtained during an unlawful search to subpoena from the victims the very documents illegally viewed, expressed succinctly the policy of the broad exclusionary rule:</p>
<blockquote>"The essence of a provision forbidding the acquisition of evidence in a certain way is that not merely evidence so acquired shall not be used before the Court but that it shall not be used at all. Of course this does not mean that the facts thus obtained become sacred and inaccessible. If knowledge of them is gained from an independent source they may be proved like any others, but the knowledge gained by the Government's own wrong cannot be used by it in the way proposed." 251 U. S., at 392.</blockquote>
<p>The exclusionary rule has traditionally barred from trial physical, tangible materials obtained either during or as a direct result of an unlawful invasion. It follows from our holding in <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span>, that the Fourth Amendment may protect against the overhearing of verbal statements as well as against the more traditional seizure of "papers and effects." Similarly, testimony as to matters observed during an unlawful invasion has been excluded in order to enforce the basic constitutional policies. <i>McGinnis</i> v. <i>United States,</i> <span class="citation" data-id="6912304"><a href="/opinion/7011844/mcginnis-v-united-states/" aria-description="Citation for case: McGinnis v. United States">227 F. 2d 598</a></span>. Thus, verbal evidence which derives so immediately from an unlawful entry and an unauthorized arrest as the officers' action in the present case is no less the "fruit" of official illegality than the more common tangible fruits of the unwarranted intrusion.<sup>[11]</sup> See <span class="star-pagination">*486</span> <i>Nueslein</i> v. <i>District of Columbia,</i> <span class="citation" data-id="1512100"><a href="/opinion/1512100/nueslein-v-district-of-columbia/" aria-description="Citation for case: Nueslein v. District of Columbia">115 F. 2d 690</a></span>. Nor do the policies underlying the exclusionary rule invite any logical distinction between physical and verbal evidence. Either in terms of deterring lawless conduct by federal officers, <i>Rea</i> v. <i>United States,</i> <span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/" aria-description="Citation for case: Rea v. United States">350 U. S. 214</a></span>, or of closing the doors of the federal courts to any use of evidence unconstitutionally obtained, <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S. 206</a></span>, the danger in relaxing the exclusionary rules in the case of verbal evidence would seem too great to warrant introducing such a distinction.</p>
<p>The Government argues that Toy's statements to the officers in his bedroom, although closely consequent upon the invasion which we hold unlawful, were nevertheless admissible because they resulted from "an intervening independent act of a free will." This contention, however, takes insufficient account of the circumstances. Six or seven officers had broken the door and followed on Toy's heels into the bedroom where his wife and child were sleeping. He had been almost immediately handcuffed and arrested. Under such circumstances it is unreasonable to infer that Toy's response was sufficiently an act of free will to purge the primary taint of the unlawful invasion.<sup>[12]</sup></p>
<p><span class="star-pagination">*487</span> The Government also contends that Toy's declarations should be admissible because they were ostensibly exculpatory rather than incriminating. There are two answers to this argument. First, the statements soon turned out to be incriminating, for they led directly to the evidence which implicated Toy. Second, when circumstances are shown such as those which induced these declarations, it is immaterial whether the declarations be termed "exculpatory."<sup>[13]</sup> Thus we find no substantial reason to omit Toy's declarations from the protection of the exclusionary rule.</p>
<p></p>
<h2>III.</h2>
<p>We now consider whether the exclusion of Toy's declarations requires also the exclusion of the narcotics taken from Yee, to which those declarations led the police. The prosecutor candidly told the trial court that "we wouldn't have found those drugs except that Mr. Toy helped us to." Hence this is not the case envisioned by this Court where the exclusionary rule has no application because the Government learned of the evidence "from an independent source," <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span>; nor is this a case in which the connection between the lawless conduct of the police and the discovery of the challenged evidence has "become so attenuated as to dissipate the taint." <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span>. We need not hold that all evidence <span class="star-pagination">*488</span> is "fruit of the poisonous tree" simply because it would not have come to light but for the illegal actions of the police. Rather, the more apt question in such a case is "whether, granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint." Maguire, Evidence of Guilt, 221 (1959). We think it clear that the narcotics were "come at by the exploitation of that illegality" and hence that they may not be used against Toy.</p>
<p></p>
<h2>IV.</h2>
<p>It remains only to consider Toy's unsigned statement. We need not decide whether, in light of the fact that Toy was free on his own recognizance when he made the statement, that statement was a fruit of the illegal arrest. Cf. <i>United States</i> v. <i>Bayer,</i> <span class="citation" data-id="9420019"><a href="/opinion/104440/united-states-v-bayer/" aria-description="Citation for case: United States v. Bayer">331 U. S. 532</a></span>. Since we have concluded that his declarations in the bedroom and the narcotics surrendered by Yee should not have been admitted in evidence against him, the only proofs remaining to sustain his conviction are his and Wong Sun's unsigned statements. Without scrutinizing the contents of Toy's ambiguous recitals, we conclude that no reference to Toy in Wong Sun's statement constitutes admissible evidence corroborating any admission by Toy. We arrive at this conclusion upon two clear lines of decisions which converge to require it. One line of our decisions establishes that criminal confessions and admissions of guilt require extrinsic corroboration; the other line of precedents holds that an out-of-court declaration made after arrest may not be used at trial against one of the declarant's partners in crime.</p>
<p>It is a settled principle of the administration of criminal justice in the federal courts that a conviction must rest upon firmer ground than the uncorroborated admission or <span class="star-pagination">*489</span> confession of the accused.<sup>[14]</sup> We observed in <i>Smith</i> v. <i>United States,</i> <span class="citation" data-id="105256"><a href="/opinion/105256/smith-v-united-states/#153" aria-description="Citation for case: Smith v. United States">348 U. S. 147, 153</a></span>, that the requirement of corroboration is rooted in "a long history of judicial experience with confessions and in the realization that sound law enforcement requires police investigations which extend beyond the words of the accused." In <i>Opper</i> v. <i>United States,</i> <span class="citation" data-id="105249"><a href="/opinion/105249/opper-v-united-states/#89" aria-description="Citation for case: Opper v. United States">348 U. S. 84, 89-90</a></span>, we elaborated the reasons for the requirement:</p>
<blockquote>"In our country the doubt persists that the zeal of the agencies of prosecution to protect the peace, the self-interest of the accomplice, the maliciousness of an enemy or the aberration or weakness of the accused under the strain of suspicion may tinge or warp the facts of the confession. Admissions, retold at a trial, are much like hearsay, that is, statements not made at the pending trial. They had neither the compulsion of the oath nor the test of cross-examination."</blockquote>
<p>It is true that in <i>Smith</i> v. <i>United States, supra</i><i>,</i> we held that although "corroboration is necessary for all elements of the offense established by admissions alone," extrinsic proof was sufficient which "merely fortifies the truth of the confession, without independently establishing the crime charged . . . ." 348 U. S., at 156.<sup>[15]</sup><span class="star-pagination">*490</span> However, Wong Sun's unsigned confession does not furnish competent corroborative evidence. The second governing principle, likewise well settled in our decisions, is that an out-of-court declaration made after arrest may not be used at trial against one of the declarant's partners in crime. While such a statement is "admissible against the others where it is in furtherance of the criminal undertaking. . . all such responsibility is at an end when the conspiracy ends." <i>Fiswick</i> v. <i>United States,</i> <span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/#217" aria-description="Citation for case: Fiswick v. United States">329 U. S. 211, 217</a></span>. We have consistently refused to broaden that very narrow exception to the traditional hearsay rule which admits statements of a codefendant made in furtherance of a conspiracy or joint undertaking.<sup>[16]</sup> See <i>Krulewitch</i> v. <i>United States,</i> <span class="citation" data-id="9420292"><a href="/opinion/104646/krulewitch-v-united-states/#443" aria-description="Citation for case: Krulewitch v. United States">336 U. S. 440, 443-445</a></span>. And where postconspiracy declarations have been admitted, we have carefully ascertained that limiting instructions kept the jury from considering the contents with respect to the guilt of anyone but the declarant. <i>Lutwak</i> v. <i>United States,</i> <span class="citation" data-id="9420873"><a href="/opinion/105079/lutwak-v-united-states/#618" aria-description="Citation for case: Lutwak v. United States">344 U. S. 604, 618-619</a></span>; <i>Delli Paoli</i> v. <i>United States,</i> <span class="citation" data-id="9421359"><a href="/opinion/105440/delli-paoli-v-united-states/#236" aria-description="Citation for case: Delli Paoli v. United States">352 U. S. 232, 236-237</a></span>. We have never ruled squarely on the question presented here, whether a codefendant's statement might serve to corroborate even where it will not suffice to convict.<sup>[17]</sup> We see <span class="star-pagination">*491</span> no warrant for a different result so long as the rule which regulates the use of out-of-court statements is one of admissibility, rather than simply of weight, of the evidence. The import of our previous holdings is that a co-conspirator's hearsay statements may be admitted against the accused for no purpose whatever, unless made during and in furtherance of the conspiracy. Thus as to Toy the only possible source of corroboration is removed and his conviction must be set aside for lack of competent evidence to support it.</p>
<p></p>
<h2>V.</h2>
<p>We turn now to the case of the other petitioner, Wong Sun. We have no occasion to disagree with the finding of the Court of Appeals that his arrest, also, was without probable cause or reasonable grounds. At all events no evidentiary consequences turn upon that question. For Wong Sun's unsigned confession was not the fruit of that arrest, and was therefore properly admitted at trial. On the evidence that Wong Sun had been released on his own recognizance after a lawful arraignment, and had returned voluntarily several days later to make the statement, we hold that the connection between the arrest and the statement had "become so attenuated as to dissipate the taint." <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span>. The fact that the statement was unsigned, whatever bearing this may have upon its weight and credibility. does not render it inadmissible; Wong Sun understood and adopted its substance, though he could not comprehend the English words. The petitioner has never suggested any impropriety in the interrogation itself which would require the exclusion of this statement.</p>
<p>We must then consider the admissibility of the narcotics surrendered by Yee. Our holding, <i>supra,</i> that this <span class="star-pagination">*492</span> ounce of heroin was inadmissible against Toy does not compel a like result with respect to Wong Sun. The exclusion of the narcotics as to Toy was required solely by their tainted relationship to information unlawfully obtained from Toy, and not by any official impropriety connected with their surrender by Yee. The seizure of this heroin invaded no right of privacy of person or premises which would entitle Wong Sun to object to its use at his trial. Cf. <i>Goldstein</i> v. <i>United States,</i> <span class="citation" data-id="9419243"><a href="/opinion/103663/goldstein-v-united-states/" aria-description="Citation for case: Goldstein v. United States">316 U. S. 114</a></span>.<sup>[18]</sup></p>
<p>However, for the reasons that Wong Sun's statement was incompetent to corroborate Toy's admissions contained in Toy's own statement, any references to Wong Sun in Toy's statement were incompetent to corroborate Wong Sun's admissions. Thus, the only competent source of corroboration for Wong Sun's statement was the heroin itself. We cannot be certain, however, on this state of the record, that the trial judge may not also have considered the contents of Toy's statement as a source of corroboration. Petitioners raised as one ground of objection to the introduction of the statements the claim that each statement, "even if it were a purported admission or confession or declaration against interest of a defendant . . . would not be binding upon the other defendant." The trial judge, in allowing the statements in, apparently overruled all of petitioners' objections, including this one. Thus we presume that he considered all portions of both statements as bearing upon the guilt of both petitioners.</p>
<p>We intimate no view one way or the other as to whether the trial judge might have found in the narcotics alone sufficient evidence to corroborate Wong Sun's admissions <span class="star-pagination">*493</span> that he delivered heroin to Yee and smoked heroin at Yee's house around the date in question. But because he might, as the factfinder, have found insufficient corroboration from the narcotics alone, we cannot be sure that the scales were not tipped in favor of conviction by reliance upon the inadmissible Toy statement. This is particularly important because of the nature of the offense involved here.</p>
<p>Surely, under the narcotics statute, the discovery of heroin raises a presumption that someonegenerally the possessorviolated the law. As to him, once possession alone is proved, the other elements of the offensetransportation and concealment with knowledge of the illegal importation of the drugneed not be separately demonstrated, much less corroborated. <span class="citation no-link">21 U. S. C. § 174</span>. Thus particular care ought to be taken in this area, when the crucial element of the accused's possession is proved solely by his own admissions, that the requisite corroboration be found among the evidence which is properly before the trier of facts. We therefore hold that petitioner Wong Sun is also entitled to a new trial.</p>
<p>The judgment of the Court of Appeals is reversed and the case is remanded to the District Court for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>[For concurring opinion of MR. JUSTICE DOUGLAS, see <i>post,</i> p. 497.]</p>
<p>[For dissenting opinion of MR. JUSTICE CLARK, see <i>post,</i> p. 498.]</p>
<p></p>
<h2>APPENDIX TO OPINION OF THE COURT.</h2>
<p></p>
<h2>Statement of JAMES WAH TOY taken on June 5, 1959, concerning his knowledge of WONG SUN's narcotic trafficking</h2>
<p>I have know WONG SUN for about 3 months. I know him as SEA DOG which is what everyone calls him. <span class="star-pagination">*494</span> I first met him in Marysville, California, during a Chinese holiday. I drove him back to San Francisco on that occasion. Sometimes he asks me to drive him home and to different places in San Francisco.</p>
<p>Sometime during April or May of this year, he asked me to drive him out to JOHNNY YEE's house, at 11th and Balboa Streets. He asked me to call JOHNNY and tell him we were coming. When we got there we went into the house and WONG SUN took a paper package out of his pocket and put it on the table. Then both WONG SUN and JOHNNY YEE opened the package. I don't know how much heroin was in it, but I know it was more than 10 spoons. I asked them if I could have some for myself and they said yes. I took a little bit and went across the room and smoked it in a cigarette.</p>
<p>WONG SUN and JOHNNY YEE talked for about 10 or 15 minutes, but they were talking in low tones so that I could not hear what they were saying. I didn't see any money change hands, because I wasn't paying too much attention. WONG SUN and I then left the house and drove. I drove WONG SUN to his home and he gave me $15.00. He said the money was for driving him out there.</p>
<p>I have driven WONG SUN out to JOHNNY YEE's house about 5 times altogether. Each time WONG SUN gave me $10 or $15 for doing it and also, Johnny gave me a little heroinenough to put in 3 or 4 cigarettes. The last time I drove WONG SUN out to YEE's house was last Tuesday, May 26, 1959. On Wednesday night June 3, 1959, at about 10:00 p. m., I called JOHNNY YEE and told him that "I'm coming out pretty soonI don't have anything." He said okay, so I drove out there. When I got there I went in the house and Johnny gave me a paper of heroin. The bindle had about enough for 5 or 6 cigarettes. I didn't give him any money and he didn't ask for any. He gives it to me just out of friendship. He has given me heroin like this quite a few times. I don't remember how many times. I have known HOM WEI <span class="star-pagination">*495</span> about 2 or 3 years but I have never dealt in narcotics with him. I have known ED FONG about 1 year and I have never dealt in narcotics with him, either. I have heard people that I know in the Hop Sing Tong Club talk about HOM WEI dealing in narcotics but nothing about ED FONG. I do not know JOHN MOW LIM or BILL FONG. The only connection I have now is JOHNNY YEE.</p>
<p>I have carefully read the foregoing statement, which was made of my own free will, without promise of reward or immunity and not under duress. I have been given ample opportunity to make corrections have initialed or signed each page as evidence thereof and hereby state that this statement is true to the best of my knowledge and belief.</p>
                         ______________________________
                                  JAMES WAH TOY
<p></p>
<h2>.....</h2>
<p>JAMES WAH TOY did not wish to sign this statement at this time. He stated he may change his mind at a later date. However, I read this statement to him and in addition he read it also and stated that the contents thereof were true to the best of his knowledge. Corrections made were by JAMES WAH TOY without his initials.</p>
                    /s/ WILLIAM WONG
                        William Wong. Narcotic Agent
<p></p>
<h2>STATEMENT OF WONG SUN</h2>
<p>I met JAMES TOY approximately the middle of March, this year, at Marysville, California, during a Chinese celebration. We returned to San Francisco together and we discussed the possible sale of heroin. I told JAMES that I could get a piece of heroin for $450 from a person known as BILL.</p>
<p>Shortly after returning to San Francisco, JAMES told me he wanted me to get a piece. I asked him who it was <span class="star-pagination">*496</span> for and he told me it was for JOHNNY. He gave me $450 and I obtained a piece of heroin from BILL. I did this on approximately 8 occasions, however, at least one of these times the heroin was not for JOHNNYfor another friend of JAMES TOY. JOHNNY would pay JAMES $600 for each piece.</p>
<p>On several occasions after I had obtained the piece for JAMES I would drive with him to JOHNNY's house, 606 11th Avenue, and we would go upstairs to the bedroom. There, all three of us would smoke some of the heroin and JAMES would give the piece to JOHNNY. I also went with JAMES on approximately 3 other occasions when he did not take any heroin and then we smoked at JOHNNY's and we would also get some for our own use.</p>
<p>About 4 days before I was arrested (arrested on June 4, 1959) JAMES called me at home about 7 o'clock in the evening and told me to come by. I went to the laundry and JAMES told me to get a piece. I called BILL and arranged to meet him. JAMES gave me $450 which I gave to BILL when I met him. BILL called me about one hour later at the laundry and I met him. He gave me one piece, which I gave to JAMES, and JAMES immediately thereafter called JOHNNY. We drove to 606 11th Ave. at approximately midnight and JAMES gave the piece to JOHNNY. It was contained in a rubber contraceptive in a small brown paper bag.</p>
<p>Again on June 3rd, the night before I was arrested, I met JAMES at the laundry, prior to 11 o'clock in the evening, and JAMES telephoned JOHNNY at EV6-9336. Then we went out to JOHNNY's and smoked heroin and also had one paper for our own use later. We were there approximately 1/2 hour and then left.</p>
<p>The laundry mentioned is OYE's LAUNDRY, 1733 Leavenworth Street, which is run by JAMES TOY. I do not know JOHNNY's last name and know him only <span class="star-pagination">*497</span> through JAMES TOY. As well as the few times at JOHNNY's home, I have seen JOHNNY on a number of occasions at the laundry.</p>
<p>I have carefully read the foregoing statement, consisting of 2 pages which was made of my own free will, without promise of reward or immunity and not under duress. I have been given ample opportunity to make corrections, have initialed or signed each page as evidence thereof and hereby state that this statement is true to the best of my knowledge and belief.</p>
                             ______________________________
                                          WONG SUN
<p></p>
<h2>.....</h2>
<p>WONG SUN, being unable to read English, did not sign this statement. However, I read this statement to him and he stated that the contents thereof were true to the best of his knowledge.</p>
                     /s/ WILLIAM WONG
                         William Wong, Narcotic Agent
<p>MR. JUSTICE DOUGLAS, concurring.</p>
<p>While I join the Court's opinion I do so because nothing the Court holds is inconsistent with my belief that there having been time to get a warrant, probable cause alone could not have justified the arrest of petitioner Toy without a warrant.</p>
<p>I adhere to the views I expressed in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#273" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 273</a></span>. What I said in the <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> case had been earlier stated by Mr. Justice Jackson, writing for the Court in <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (another narcotics case):</p>
<blockquote>"The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection <span class="star-pagination">*498</span> consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime. Any assumption that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers." Pp. 13-14. And see <i>Chapman</i> v. <i>United States,</i> <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/#615" aria-description="Citation for case: Chapman v. United States">365 U. S. 610, 615-616</a></span>.</blockquote>
<p>The Court finds it unnecessary to reach that constitutional question. I mention it only to reiterate that the <i><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Johnson</a></span></i> case represents the law and is in no way eroded by what we fail to decide today.</p>
<p>MR. JUSTICE CLARK, with whom MR. JUSTICE HARLAN, MR. JUSTICE STEWART and MR. JUSTICE WHITE join. dissenting.</p>
<p>The Court has made a Chinese puzzle out of this simple case involving four participants: Hom Way, Blackie Toy, Johnny Yee and "Sea Dog" Sun. In setting aside the convictions of Toy and Sun it has dashed to pieces the heretofore recognized standards of probable cause necessary to secure an arrest warrant or to make an arrest without one. Instead of dealing with probable cause as involving "probabilities," "the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act," <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175</a></span> (1949), the Court sets up rigid, mechanical standards, applying the 20-20 vision of hindsight in an area where the ambiguity and immediacy inherent in unexpected arrest are present. While probable cause must be based on more than mere suspicion, <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#104" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 104</a></span> (1959), it does <span class="star-pagination">*499</span> not require proof sufficient to establish guilt. <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#312" aria-description="Citation for case: Draper v. United States">358 U. S. 307, 312</a></span> (1959). The sole requirement heretofore has been that the knowledge in the hands of the officers at the time of arrest must support a "man of reasonable caution in the belief" that the subject had committed narcotic offenses. <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#162" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 162</a></span> (1925). That decision is faced initially not in the courtroom but at the scene of arrest where the totality of the circumstances facing the officer is weighed against his split-second decision to make the arrest. This is an everyday occurrence facing law enforcement officers, and the unrealistic, enlarged standards announced here place an unnecessarily heavy hand upon them. I therefore dissent.</p>
<p></p>
<h2>I.</h2>
<p>The first character in this affair is Hom Way, who was arrested in possession of narcotics and told the officers early that morning that he had purchased an ounce of heroin on the previous night from Blackie Toy, who operated a laundry on Leavenworth Street. Narcotics agents, armed with this information from a person they had known for six weeks and who was under arrest for possession of narcotics, immediately sought out Blackie Toy, the second character. The laundry was located without difficulty (as far as the record shows) from the information furnished by Hom Way. The Court gratuitously reads into the record its supposition that Hom Way "merely invited the officers to roam the length of Leavenworth Street (some 30 blocks) in search of one `Blackie Toy's' laundry . . . ." On the contrary, the identification of "Blackie" and the directions to his laundry were sufficiently accurate for the officerstwo of whom were of Chinese ancestryto find Blackie at his laundry within an hour. I cannot say in the face of this record that this was a "roaming" performance <span class="star-pagination">*500</span> up and down Leavenworth Street. To me it was efficient police work by officers familiar with San Francisco and the habits and practices of its Chinese-American inhabitants. Indeed, the information was much more explicit than that approved by this Court in <i>Draper</i> v. <i>United States, supra</i><i>.</i></p>
<p>There are other indicia of reliability, however. Here the informer, believed by the officers to be reliable,<sup>[*]</sup> was under arrest when he implicated himself in the purchase of an ounce of heroin the previous night. Since he was in possession of narcotics and his information related to a narcotics sale in which he was the buyer, the officers had good reason to rely on Hom Way's knowledge. See <i>Rodgers</i> v. <i>United States,</i> <span class="citation" data-id="248139"><a href="/opinion/248139/e-nadine-rodgers-v-united-states/" aria-description="Citation for case: E. Nadine Rodgers v. United States">267 F. 2d 79</a></span> (C. A. 9th Cir. 1959), and <i>Thomas</i> v. <i>United States,</i> <span class="citation" data-id="251634"><a href="/opinion/251634/patrick-fagan-thomas-v-united-states/" aria-description="Citation for case: Patrick Fagan Thomas v. United States">281 F. 2d 132</a></span> (C. A. 8th Cir.), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./364/904/">364 U. S. 904</a></span> (1960). As to his credibility, he was confronted with prosecution for possession of narcotics and well knew that any discrepancies in his story might go hard with him. Furthermore, the statement was a declaration against interest which stripped Hom Way of any explanation for his possession of narcotics and made certain the presumption of <span class="citation no-link">21 U. S. C. § 174</span>. I do not see what stronger and more reliable information one could have to establish probable cause for the arrest without warrant of Blackie Toy.</p>
<p>But even assuming there was no probable cause at this point, the Government produced additional evidence to support the lawfulness of Blackie's arrest. In broad daylight, about 6:30 on the same morning that Hom Way was arrested, one of the officers of Chinese ancestry, Agent Alton Wong, knocked on Blackie Toy's laundry door. When Wong told him that he wanted laundry, Blackie <span class="star-pagination">*501</span> opened the door and advised him to return at 8 a. m. Wong testified that he then "pulled out [his] badge" and announced that he was a narcotics agent. Blackie slammed the door in Wong's face and ran down the hall of the laundry. Wong broke through the door after himcalling again that he was "a narcotics Treasury agent." Only when Blackie reached the family bedroom was Wong able to arrest him, as he reached into a nightstand drawer, apparently looking for narcotics. Agent Wong immediately confronted him with Hom Way's accusation that Blackie Toy had sold him narcotics. Blackie denied selling narcotics, but he did not deny knowing Hom Way and later admitted knowing him. There is no basis in <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">357 U. S. 301</a></span> (1958), for the Court's conclusion that Blackie's flight "signified . . . a natural desire [by Toy] to repel an apparently unauthorized intrusion. . . ." As I see it this is incredible in the light of the record. Nor is there any support in the record that "before Toy fled, the officer never adequately dispelled the misimpression engendered by his own ruse." On the contrary the officer's showing of his badge and announcement that he was a narcotics agent immediately put Blackie in flight behind the slamming door. To conclude otherwise takes all prizes as a <i>non sequitur.</i> As he pursued, Wong continued to identify himself as a narcotics agent. I ask, how could he more clearly announce himself and his purpose?</p>
<p>This Court has often held unexplained flightas here from an officer to be strong evidence of guilt. <i>E. g., </i><i>Husty</i> v. <i>United States,</i> <span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/" aria-description="Citation for case: Husty v. United States">282 U. S. 694</a></span> (1931); <i>Brinegar</i> v. <i>United States, supra,</i> at p. 166, n. 7; see <i>Henry</i> v. <i>United States, supra</i><i>,</i> where the Court was careful to distinguish its facts from those of "fleeing men or men acting furtively." <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#103" aria-description="Citation for case: Henry v. United States">361 U. S., at 103</a></span>. Moreover, as the Government has always emphasized, this is particularly true in narcotics cases where delay may have serious consequences, <i>i. e.,</i> the hiding <span class="star-pagination">*502</span> or destruction of the drugs. This Court noted without disapproval in <i>Miller</i> v. <i>United States, supra</i><i>,</i> the state decisions holding that "justification for noncompliance [with the rule] exists in exigent circumstances, as, for example, when the officers may in good faith believe . . . that the person to be arrested is fleeing or attempting to destroy evidence. <i>People</i> v. <i>Maddox,</i> <span class="citation" data-id="9627819"><a href="/opinion/1428666/people-v-maddox/" aria-description="Citation for case: People v. Maddox">46 Cal. 2d 301</a></span>, <span class="citation" data-id="9627819"><a href="/opinion/1428666/people-v-maddox/" aria-description="Citation for case: People v. Maddox">294 P. 2d 6</a></span>." 357 U. S., at 309. And the Court continued, "It may be that, without an express announcement of purpose, the facts known to officers would justify them in being virtually certain that the petitioner already knows their purpose so that an announcement would be a useless gesture. Cf. <i>People</i> v. <i>Martin,</i> <span class="citation" data-id="1139982"><a href="/opinion/1139982/people-v-martin/" aria-description="Citation for case: People v. Martin">45 Cal. 2d 755</a></span>, <span class="citation" data-id="1139982"><a href="/opinion/1139982/people-v-martin/" aria-description="Citation for case: People v. Martin">290 P. 2d 855</a></span>; Wilgus, Arrest Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 541</span>, 798, 802 (1924)." <span class="citation no-link"><i>Id.,</i> at 310</span>.</p>
<p>The Court places entire reliance on the decision in <i><span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">Miller</a></span>.</i> I submit that it is inapposite. That case involved interpretation of the law of the District of Columbia. <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#306" aria-description="Citation for case: Miller v. United States"><i>Id.,</i> at 306</a></span>. The arrest was at night, and the door was broken in just as the defendant began to close it. Thus there was no flight but only what the officer believed to be an attempt to bar their entrance. The only identification given by the officers occurred before the defendant opened the door, when "in a low voice" through the closed door they answered the defendant's query as to who was there by saying, "Police." <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#303" aria-description="Citation for case: Miller v. United States"><i>Id.,</i> at 303</a></span>. The facts in <i><span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">Miller</a></span></i> differ significantly from this case both in the clarity of identification by the officers and in the character and extent of the defendant's conduct. For that reason, the conclusions that Blackie's flight is evidence to support probable cause and that the officers gave sufficient notice to permit lawful entry are supported rather than weakened by the Court's decision in <i><span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">Miller</a></span>.</i></p>
<p>The information from Hom Way and Blackie Toy's unexplained flight cannot be viewed "in two separate. logic-tight compartments. . . . [T]ogether they composed <span class="star-pagination">*503</span> a picture meaningful to a trained, experienced observer." <i>Christensen</i> v. <i>United States,</i> 104 U. S. App. D.C. 35, 36, <span class="citation" data-id="9446395"><a href="/opinion/246074/george-a-christensen-v-united-states/#193" aria-description="Citation for case: George A. Christensen v. United States">259 F. 2d 192, 193</a></span> (1958). I submit that the officers as reasonable men properly concluded that the petitioner was the "Blackie Toy" who Hom Way informed them had committed a felony and that his immediate arrestas he ran through his hallwas lawful and was imperative in order to prevent his escape. In view of this there is no "poisonous tree" whose fruits we must evaluate, and Blackie's declaration at the time of the arrest and the narcotics found in Yee's possession are admissible in evidence. The trial court found that evidence sufficiently corroborative of Toy's confession, and the Court of Appeals affirmed. For the same reasons discussed, <i>infra,</i> as to Wong Sun, I see no occasion to overturn these consistent findings of two courts.</p>
<p></p>
<h2>II.</h2>
<p>As to "Sea Dog," Wong Sun, there is no disagreement that his confession and the narcotics found in Yee's possession were admissible in evidence against him. The question remains as to whether there was sufficient independent evidence to corroborate the confession. Such evidence "does not have to prove the offense beyond a reasonable doubt, or even by a preponderance . . . ." <i>Smith</i> v. <i>United States,</i> <span class="citation" data-id="105256"><a href="/opinion/105256/smith-v-united-states/#156" aria-description="Citation for case: Smith v. United States">348 U. S. 147, 156</a></span> (1954). The requirement is satisfied "if the corroboration merely fortifies the truth of the confession, without independently establishing the crime charged . . . ." <i>Ibid.;</i> see also <i>Opper</i> v. <i>United States,</i> <span class="citation" data-id="105249"><a href="/opinion/105249/opper-v-united-states/" aria-description="Citation for case: Opper v. United States">348 U. S. 84</a></span> (1954). Wong Sun's confession stated in part that about four days before his arrest he and Toy delivered an ounce of heroin to Yee and that on the night before his arrestthe night of June 3, 1959 he and Toy smoked some heroin at Yee's house. On June 4, 1959, the officers found at Yee's residence quantities of heroin totaling "just less than one ounce." In light <span class="star-pagination">*504</span> of this evidence, I am unable to say that the trial court and the Court of Appeals erred in holding that Wong Sun's confession was sufficiently corroborated.</p>
<p>The Court does not reach a contrary conclusion as to corroboration, but it grants Wong Sun a new trial on the ground that the trial court "may" also "have considered the contents of Toy's statement as a source of corroboration" of it. This point was not raised as a question here nor was it discussed in the briefs. Despite this the Court goes to some lengths to develop a chain of inferences in finding prejudicial error. This might be plausible where the case was tried to a jury, as were all the cases cited by the Court. Indeed, I find no case where such presumption of error was applied, as here, to a trial before a judge. The Court admits that the heroin found in Johnny Yee's possession might itself be sufficient corroboration, but it reverses on the excuse that the judge "may" have considered Toy's confession as well. I see no reason for this assumption where a federal judge is the trier of the fact, and I would therefore affirm the judgment as to both petitioners.</p>
<h2>NOTES</h2>
<p>[1]  <span class="citation no-link">21 U. S. C. § 174</span>:
</p>
<p>"Whoever fraudulently or knowingly imports or brings any narcotic drug into the United States or any territory under its control or jurisdiction, contrary to law, or receives, conceals, buys, sells, or in any manner facilitates the transportation, concealment, or sale of any such narcotic drug after being imported or brought in, knowing the same to have been imported or brought into the United States contrary to law, or conspires to commit any of such acts in violation of the laws of the United States, shall be imprisoned not less than five or more than twenty years and, in addition, may be fined not more than $20,000. For a second or subsequent offense (as determined under section 7237 (c) of the Internal Revenue Code of 1954), the offender shall be imprisoned not less than ten or more than forty years and, in addition, may be fined not more than $20,000.</p>
<p>"Whenever on trial for a violation of this section the defendant is shown to have or to have had possession of the narcotic drug, such possession shall be deemed sufficient evidence to authorize conviction unless the defendant explains the possession to the satisfaction of the jury."</p>
<p>[2]  A "piece" is approximately one ounce.</p>
<p>[3]  The Record of the arraignment proceedings recites that arrest warrants were issued, on the arraignment dates, for the arrest of both petitioners and Yee. It was conceded in the trial court, however, that no arrest warrants were outstanding at the time of the actual arrests on June 4.
</p>
<p>The Record also states that bond was initially fixed for each of the petitioners and for Yee in the amount of $5,000, on the recommendation of the United States Attorney. Later on the respective arraignment days, again on motion of the United States Attorney, it was ordered that each of the three be released on his own recognizance.</p>
<p>[4]  Because neither statement was ever signed, the blanks in which the dates were to have been inserted were never filled in. The heading of Toy's statement suggests that it was made on June 5, although Agent William Wong at the trial suggested he had only talked informally with Toy on that date, the formal statement not being made until June 9. The agent also testified that Wong Sun's statement was made June 9, although a rubber-stamp date beneath the agent's own signature at the foot of the statement reads, "June 15, 1959."</p>
<p>[5]  The full texts of both statements are set forth in an Appendix to this opinion.</p>
<p>[6]  <span class="citation no-link">26 U. S. C. § 7607</span>:
</p>
<p>"The Commissioner, Deputy Commissioner, Assistant to the Commissioner, and agents, of the Bureau of Narcotics of the Department of the Treasury, and officers of the customs (as defined in section 401 (1) of the Tariff Act of 1930, as amended; <span class="citation no-link">19 U. S. C., sec. 1401</span> (1)), may</p>
<p>"(1) carry firearms, execute and serve search warrants and arrest warrants, and serve subpenas and summonses issued under the authority of the United States, and</p>
<p>"(2) make arrests without warrant for violations of any law of the United States relating to narcotic drugs (as defined in section 4731) or marihuana (as defined in section 4761) where the violation is committed in the presence of the person making the arrest or where such person has reasonable grounds to believe that the person to be arrested has committed or is committing such violation."</p>
<p>The terms "probable cause" for purposes of the Fourth Amendment and "reasonable grounds" as used in the statute, mean substantially the same. <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#310" aria-description="Citation for case: Draper v. United States">358 U. S. 307, 310, n. 3</a></span>; <i>United States</i> v. <i>Walker,</i> <span class="citation" data-id="242778"><a href="/opinion/242778/the-united-states-of-america-v-farris-walker/#526" aria-description="Citation for case: The United States of America v. Farris Walker">246 F. 2d 519, 526</a></span>.</p>
<p>[7]  See <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#485" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 485-487</a></span>; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#16" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 16-17</a></span>. See generally Wilgus, Arrest Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 541</span>, 673, 695-701 (1924).</p>
<p>[8]  Our discussion implies no view whether a search warrant should be obtained where a search is conducted incident to a valid arrest, cf. <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>, for nothing in this case turns on the presence or absence of a search warrant. Since the officers had obtained an arrest warrant in <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span>,</i> the question before us here was not there presented. As to the question before us, see <i>Wrightson</i> v. <i>United States,</i> <span class="citation" data-id="9444624"><a href="/opinion/236713/samuel-wrightson-v-united-states/" aria-description="Citation for case: Samuel Wrightson v. United States">222 F. 2d 556</a></span>, 559-560:
</p>
<p>"But, if officers can arrest without a warrant and never be required to disclose the facts upon which they based their belief of probable causeif, in other words, they have an untouchable power to arrest without a warrant,why would they ever bother to get a warrant? And the same obvious conclusion follows if the courts, when an arrest is attacked as illegal, will assume, without facts, that an arrest without a warrant was for probable cause. To strike down all factual requirements in respect to probable cause for arrests without a warrant, while maintaining them for the issuance of a warrant, would be to blast one of the support columns of justice by law."</p>
<p>[9]  We noted in <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> that Rules 3 and 4 of the Federal Rules of Criminal Procedure provide that an arrest warrant shall issue only upon a sworn complaint setting forth "the essential facts constituting the offense charged," and showing "that there is probable cause to believe that an offense has been committed and that the defendant has committed it . . . ." The Fourth Amendment, from which the requirements of the Rules derive, provides that ". . . no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and <i>particularly describing</i> . . . the persons or things to be seized." (Emphasis added.) The requirement applies both to arrest and search warrants. A description of a suspect merely as "Blackie Toy," operator of a laundry somewhere on Leavenworth Street, hardly is information "particularly describing . . . the person . . . to be seized." Such information is no better than the wholesale or "dragnet" search warrant, which we have condemned. See, <i>e. g., </i><i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 196</a></span>; see generally Kaplan, Search and Seizure: A No-Man's Land in the Criminal Law, <span class="citation no-link">49 Calif. L. Rev. 474</span>, 480-482 (1961).</p>
<p>[10]  Although the question presented here is only whether the petitioner's flight justified an inference of guilt sufficient to generate probable cause for his arrest, and not whether his flight would serve to corroborate proof of his guilt at trial, the two questions are inescapably related. Thus it is relevant to the present case that we have consistently doubted the probative value in criminal trials of evidence that the accused fled the scene of an actual or supposed crime. In <i>Alberty</i> v. <i>United States,</i> <span class="citation" data-id="94447"><a href="/opinion/94447/alberty-v-united-states/#511" aria-description="Citation for case: Alberty v. United States">162 U. S. 499, 511</a></span>, this Court said:
</p>
<p>". . . it is not universally true that a man, who is conscious that he has done a wrong, `will pursue a certain course not in harmony with the conduct of a man who is conscious of having done an act which is innocent, right and proper;' since it is a matter of common knowledge that men who are entirely innocent do sometimes fly from the scene of a crime through fear of being apprehended as the guilty parties, or from an unwillingness to appear as witnesses. Nor is it true as an accepted axiom of criminal law that `the wicked flee when no man pursueth, but the righteous are as bold as a lion.' "</p>
<p>See also <i>Hickory</i> v. <i>United States,</i> <span class="citation" data-id="94334"><a href="/opinion/94334/hickory-v-united-states/" aria-description="Citation for case: Hickory v. United States">160 U. S. 408</a></span>; <i>Allen</i> v. <i>United States,</i> <span class="citation" data-id="94565"><a href="/opinion/94565/allen-v-united-states/" aria-description="Citation for case: Allen v. United States">164 U. S. 492</a></span>; <i>Starr</i> v. <i>United States,</i> <span class="citation" data-id="94573"><a href="/opinion/94573/starr-v-united-states/" aria-description="Citation for case: Starr v. United States">164 U. S. 627</a></span>; and for the views of two Courts of Appeals see <i>Vick</i> v. <i>United States,</i> <span class="citation" data-id="234904"><a href="/opinion/234904/earl-e-vick-v-united-states/#233" aria-description="Citation for case: Earl E. Vick v. United States">216 F. 2d 228, 233</a></span> (C. A. 5th Cir.) ("One motive is about as likely as another. Appellant may be guilty, but his conviction cannot rest upon mere conjecture and suspicion"); cf. <i>Cooper</i> v. <i>United States,</i> <span class="citation" data-id="235392"><a href="/opinion/235392/cooper-v-united-states/#41" aria-description="Citation for case: Cooper v. United States">218 F. 2d 39, 41</a></span> (C. A. D. C. Cir.) ("After all, innocent people caught in a web of circumstances frequently become terror-stricken"). But cf. <i>United States</i> v. <i>Heitner,</i> <span class="citation" data-id="1507600"><a href="/opinion/1507600/united-states-v-heitner/" aria-description="Citation for case: United States v. Heitner">149 F. 2d 105</a></span> (C. A. 2d Cir.).</p>
<p>[11]  See Kamisar, Illegal Searches or Seizures and Contemporaneous Incriminating Statements: A Dialogue on a Neglected Area of Criminal Procedure, 1961 U. of Ill. Law Forum 78, 84-96. But compare Maguire, Evidence of Guilt (1959), 187-190.</p>
<p>[12]  See Lord Devlin's comment: "It is probable that even today, when there is much less ignorance about these matters than formerly, there is still a general belief that you must answer all questions put to you by a policeman, or at least that it will be the worse for you if you do not." Devlin, The Criminal Prosecution in England (1958), 32. Even in the absence of such oppressive circumstances, and where an exclusionary rule rests principally on nonconstitutional grounds, we have sometimes refused to differentiate between voluntary and involuntary declarations. See Hogan and Snee, The McNabb-Mallory Rule: Its Rise, Rationale and Rescue, 47 Geo. L. J. 1, 26-27 (1958). For illustrative situations where a voluntary act of the accused has been held insufficient to cure the otherwise unlawful acquisition of evidence, see <i>Bynum</i> v. <i>United States,</i> <span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/" aria-description="Citation for case: Clayborne Bynum v. United States">262 F. 2d 465</a></span> (holding inadmissible fingerprints made by defendant after unlawful arrest); <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="1424394"><a href="/opinion/1424394/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">189 F. Supp. 776</a></span> (excluding narcotics voluntarily surrendered by accused in the course of an unauthorized search). The Ninth Circuit Court of Appeals from which the instant case comes has recognized in an analogous context, that "all declarations and statements under the compulsion of the things so seized, are affected by the vice of primary illegality. . . ." <i>Takahashi</i> v. <i>United States,</i> <span class="citation" data-id="1478266"><a href="/opinion/1478266/takahashi-v-united-states/#122" aria-description="Citation for case: Takahashi v. United States">143 F. 2d 118, 122</a></span>.</p>
<p>[13]  Moreover, we held in <i>Opper</i> v. <i>United States,</i> <span class="citation" data-id="105249"><a href="/opinion/105249/opper-v-united-states/#92" aria-description="Citation for case: Opper v. United States">348 U. S. 84, 92</a></span>, that even where exculpatory statements are voluntary and thus clearly admissible, they require at least the degree of corroboration required of incriminating statements.</p>
<p>[14]  For the history and development of the corroboration requirement, see 7 Wigmore, Evidence (3d ed. 1940), §§ 2070-2071; Note, Proof of the Corpus Delicti Aliunde the Defendant's Confession, 103 U. of Pa. L. Rev. 638-649 (1955). For the present scope and application of the rule, see 2 Underhill, Criminal Evidence (5th ed. 1956), §§ 402-403. For a comprehensive collection of cases, see Annot., 45 A. L. R. 2d 1316 (1956).</p>
<p>[15]  Where the crime involves physical damage to person or property, the prosecution must generally show that the injury for which the accused confesses responsibility did in fact occur, and that some person was criminally culpable. A notable example is the principle that an admission of homicide must be corroborated by tangible evidence of the death of the supposed victim. See 7 Wigmore, Evidence (3d ed. 1940), § 2072, n. 5. There need in such a case be no link, outside the confession, between the injury and the accused who admits having inflicted it. But where the crime involves no tangible <i>corpus delicti,</i> we have said that "the corroborative evidence must implicate the accused in order to show that a crime has been committed." 348 U. S., at 154. Finally, we have said that one uncorroborated admission by the accused does not, standing alone, corroborate an unverified confession. <i>United States</i> v. <i>Calderon,</i> <span class="citation" data-id="105257"><a href="/opinion/105257/united-states-v-calderon/#165" aria-description="Citation for case: United States v. Calderon">348 U. S. 160, 165</a></span>.</p>
<p>[16]  See Developments in the LawCriminal Conspiracy, <span class="citation no-link">72 Harv. L. Rev. 922</span>, 989-990 (1959).</p>
<p>[17]  Cf. Williams, The Proof of Guilt (1958), 135: "Even where . . . the evidence of an accomplice becomes admissible against his fellows, it remains suspect evidence, because of the tainted source from which it comes. The accomplice may no longer have anything to fear or hope from the way in which he gives his evidence; yet he may mistakenly entertain such a fear or hope, or he may wish by his evidence against others to gratify some spite against them."</p>
<p>[18]  This case is not like <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span>, where the person challenging the seizure of evidence was lawfully on the premises at the time of the search. Nor is it like <i>Chapman</i> v. <i>United States,</i> <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span>, where we held that a landlord could not lawfully consent to a search of his tenant's premises. See generally Edwards, Standing to Suppress Unreasonably Seized Evidence, 47 N. W. U. L. Rev. 471 (1952).</p>
<p>[*]  One of the officers testified at the trial that he had known Hom Way for six weeks. In response to the question whether Hom Way was a reliable informer, the officer replied, "I believe so, yes, sir."</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Wright v. City of Euclid.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Wright v. City of Euclid"
type: case
citation: "962 F.3d 852 (2020)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, Sixth Circuit"
court_level: coa
circuit: 6th
year: 2020
date_decided: 2020-06-18
docket: 19-3452
authority_weight: "Binding in-circuit — 6th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2020-06-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Wright v. City of Euclid
  varies_by_point: false
  scope_note: "Published Sixth Circuit decision; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4762133/lamar-wright-v-city-of-euclid/"
  cluster_id: 4762133
  opinion_id: 4542480
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Recent development (role-based)"
related: ["[[Graham v. Connor]]", "[[Monell v. Department of Social Services]]", "[[Pearson v. Callahan]]"]
aliases: ["Lamar Wright v. City of Euclid", "Wright v. Euclid"]
tags: ["case", "section-1983", "qualified-immunity", "excessive-force", "false-arrest", "municipal-liability", "sixth-circuit"]
holding: "The Sixth Circuit REVERSED summary judgment / denial of qualified immunity on multiple Fourth Amendment § 1983 claims: excessive force…"
lake:
  record_id: Wright v. City of Euclid
  status: verified
  projected_at: 2026-07-06
---

# Wright v. City of Euclid

*962 F.3d 852 (6th Cir. 2020)* · U.S. Court of Appeals, Sixth Circuit · **Binding in-circuit — 6th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Plainclothes Euclid, Ohio officers in an unmarked car, suspecting a drug deal, stopped Lamar Wright. According to Wright, within moments — without his fleeing or actively resisting — Officer Flagg drew a weapon and tased him and Officer Williams brandished a firearm and pepper-sprayed him; Wright, who wore a colostomy bag, was pulled from his SUV. He was arrested, his arrest designated drug-related (subjecting him to more invasive searches), and held roughly four hours past posting bond for a body scan that found no drugs; the charges were later dropped. Wright sued the officers and the City under § 1983. The district court granted summary judgment to the defendants on qualified-immunity and Monell grounds.

## Issue
Whether genuine disputes of material fact precluded summary judgment — and whether [[Qualified Immunity|qualified immunity]] shielded the officers — on Wright's Fourth Amendment claims for excessive force, false arrest, and extended detention, and whether the City could face Monell municipal liability.

## Rule
[[Qualified Immunity|Qualified immunity]] is overcome where, taking the plaintiff's version of the facts as true, a jury could find a violation of a clearly established right. On excessive force: "It was clearly established as of November 4, 2016 that drawing a weapon on a suspect who was not fleeing or posing a safety risk and tasering a suspect who was not actively resisting arrest constituted excessive force." — *Wright v. City of Euclid*, 962 F.3d 852 (6th Cir. 2020) (slip op., at 17). ^pin-op17

On false arrest: "the right to be free from arrest without probable cause is a 'quintessential example[] of [a] "clearly established" constitutional right.'" — *Id.* (slip op., at 23). ^pin-op23

On municipal liability: "Wright has produced enough evidence such that a reasonable jury could find that the City's custom surrounding use of force is so settled so as to have the force of law and that it was the moving force behind violations of Wright's constitutional rights." — *Id.* (slip op., at 33). ^pin-op33

## Application
On these facts, taking Wright's account as true (as required at summary judgment), a reasonable jury could find that Flagg and Williams used excessive force by drawing weapons and deploying a taser and pepper spray against a suspect who was neither fleeing nor actively resisting, and that the officers lacked probable cause to arrest him. Because both rights were clearly established by November 2016, the officers were not entitled to [[Qualified Immunity|qualified immunity]] on those claims, and the extended detention (derivative of the arrest) failed for the same reason. Wright's evidence about the Euclid department's use-of-force training and culture, including offensive training materials, also permitted a jury to find a municipal custom that was the moving force behind the violations. The court reversed the grants of summary judgment on these claims.

## Conclusion
Genuine fact disputes precluded summary judgment, and the rights at issue were clearly established, so the officers were not entitled to [[Qualified Immunity|qualified immunity]]; the City could face [[Section 1983 Liability and Qualified Immunity|Monell liability]]. The Sixth Circuit reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 6th Cir.**
- No negative treatment. *Wright* applies the excessive-force standard of [[Graham v. Connor]], the clearly-established/qualified-immunity framework reflected in [[Pearson v. Callahan]], and the municipal-liability "policy or custom" rule of [[Monell v. Department of Social Services]].

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development (role-based)*

## Sources
- *Wright v. City of Euclid*, 962 F.3d 852 (6th Cir. 2020) — https://www.courtlistener.com/opinion/4762133/lamar-wright-v-city-of-euclid/ — pinpoints given as slip-opinion pages (slip op., at 17, 23, 33); CourtListener carries the slip opinion, paginated by slip page (cluster 4762133 → opinion 4542480).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "97bcd6eebaf39aa4", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Wright v. City of Euclid"}, "payload": {"all": [{"cite": "962 F.3d 852", "page": "852", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "962"}], "display": "962 F.3d 852", "official": {"cite": "962 F.3d 852", "page": "852", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "962"}, "official_selection_present": true, "record_id": "Wright v. City of Euclid"}}
{"assertion_id": "9bd5480368c4a375", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op23", "record_id": "Wright v. City of Euclid"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op23", "pinpoint_status": "slip-only", "quote": "the right to be free from arrest without probable cause is a 'quintessential example[] of [a]", "quote_fidelity": "mismatch", "record_id": "Wright v. City of Euclid", "star_marker": null}}
{"assertion_id": "d7fe79013ddabddf", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op17", "record_id": "Wright v. City of Euclid"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op17", "pinpoint_status": "slip-only", "quote": "--- # Wright v. City of Euclid *962 F.3d 852 (6th Cir. 2020)* · U.S. Court of Appeals, Sixth Circuit · **Binding in-circuit — 6th Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Plainclothes Euclid, Ohio officers in an unmarked car, suspecting a drug deal, stopped Lamar Wright. According to Wright, within moments — without his fleeing or actively resisting — Officer Flagg drew a weapon and tased him and Officer Williams brandished a firearm and pepper-sprayed him; Wright, who wore a colostomy bag, was pulled from his SUV. He was arrested, his arrest designated drug-related (subjecting him to more invasive searches), and held roughly four hours past posting bond for a body scan that found no drugs; the charges were later dropped. Wright sued the officers and the City under § 1983. The district court granted summary judgment to the defendants on qualified-immunity and Monell grounds. ## Issue Whether genuine disputes of material fact precluded summary judgment — and whether qualified immunity shielded the officers — on Wright's Fourth Amendment claims for excessive force, false arrest, and extended detention, and whether the City could face Monell municipal liability. ## Rule Qualified immunity is overcome where, taking the plaintiff's version of the facts as true, a jury could find a violation of a clearly established right. On excessive force:", "quote_fidelity": "mismatch", "record_id": "Wright v. City of Euclid", "star_marker": null}}
{"assertion_id": "d9139b004411eed7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op33", "record_id": "Wright v. City of Euclid"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op33", "pinpoint_status": "slip-only", "quote": "Wright has produced enough evidence such that a reasonable jury could find that the City's custom surrounding use of force is so settled so as to have the force of law and that it was the moving force behind violations of Wright's constitutional rights.", "quote_fidelity": "mismatch", "record_id": "Wright v. City of Euclid", "star_marker": null}}
{"assertion_id": "f85584c9ed6e53e8", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Wright v. City of Euclid"}, "payload": {"as_of_content": "2020-06-18", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Wright v. City of Euclid", "scope_note": "Published Sixth Circuit decision; good law.", "varies_by_point": false}}
```

### lake record — Wright v. City of Euclid

```json
{
  "schema_version": "s2.v1",
  "record_id": "Wright v. City of Euclid",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Lamar Wright v. City of Euclid",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "Wright v. City of Euclid",
    "court": "U.S. Court of Appeals, Sixth Circuit",
    "court_id": "ca6",
    "court_level": "coa",
    "circuit": "6th",
    "state": null,
    "date_decided": "2020-06-18",
    "year": 2020,
    "docket": "19-3452",
    "cluster_id": 4762133,
    "lead_opinion_id": 4542480,
    "sibling_ids": [
      4542480
    ],
    "absolute_url": "/opinion/4762133/lamar-wright-v-city-of-euclid/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "962 F.3d 852",
      "volume": "962",
      "reporter": "F.3d",
      "page": "852",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "962 F.3d 852",
        "volume": "962",
        "reporter": "F.3d",
        "page": "852",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "962 F.3d 852",
    "official_selection": {
      "court_class": "coa",
      "selected": "962 F.3d 852",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op17",
      "page": null,
      "quote": "--- # Wright v. City of Euclid *962 F.3d 852 (6th Cir. 2020)* \u00b7 U.S. Court of Appeals, Sixth Circuit \u00b7 **Binding in-circuit \u2014 6th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Plainclothes Euclid, Ohio officers in an unmarked car, suspecting a drug deal, stopped Lamar Wright. According to Wright, within moments \u2014 without his fleeing or actively resisting \u2014 Officer Flagg drew a weapon and tased him and Officer Williams brandished a firearm and pepper-sprayed him; Wright, who wore a colostomy bag, was pulled from his SUV. He was arrested, his arrest designated drug-related (subjecting him to more invasive searches), and held roughly four hours past posting bond for a body scan that found no drugs; the charges were later dropped. Wright sued the officers and the City under \u00a7 1983. The district court granted summary judgment to the defendants on qualified-immunity and Monell grounds. ## Issue Whether genuine disputes of material fact precluded summary judgment \u2014 and whether qualified immunity shielded the officers \u2014 on Wright's Fourth Amendment claims for excessive force, false arrest, and extended detention, and whether the City could face Monell municipal liability. ## Rule Qualified immunity is overcome where, taking the plaintiff's version of the facts as true, a jury could find a violation of a clearly established right. On excessive force:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op23",
      "page": null,
      "quote": "the right to be free from arrest without probable cause is a 'quintessential example[] of [a]",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op33",
      "page": null,
      "quote": "Wright has produced enough evidence such that a reasonable jury could find that the City's custom surrounding use of force is so settled so as to have the force of law and that it was the moving force behind violations of Wright's constitutional rights.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2020-06-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Wright v. City of Euclid",
    "varies_by_point": false,
    "scope_note": "Published Sixth Circuit decision; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Pearlie Gambrel v. Knox Cnty., Ky.",
          "cluster_id": 6347889,
          "cite": [
            "25 F.4th 391"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salvatore Palma, Jr. v. Matthew Johns",
          "cluster_id": 6445970,
          "cite": [
            "27 F.4th 419"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tucker v. City of Shreveport",
          "cluster_id": 4884106,
          "cite": [
            "998 F.3d 165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Shumate v. City of Adrian, Mich.",
          "cluster_id": 7855599,
          "cite": [
            "44 F.4th 427"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lutfi Saalim v. Walmart, Inc.",
          "cluster_id": 9490587,
          "cite": [
            "97 F.4th 995"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wendy Browning v. Edmonson Cnty., Ky.",
          "cluster_id": 5298175,
          "cite": [
            "18 F.4th 516"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kamel Chaney-Snell v. Andrew Young",
          "cluster_id": 9493618,
          "cite": [
            "98 F.4th 699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Timothy Raimey v. City of Niles, Ohio",
          "cluster_id": 9419576,
          "cite": [
            "77 F.4th 441"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "LaChance v. Town of Charlton",
          "cluster_id": 4860892,
          "cite": [
            "990 F.3d 14"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chana Wiley v. City of Columbus",
          "cluster_id": 6474125,
          "cite": [
            "36 F.4th 661"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Howard Linden v. City of Southfield, Mich.",
          "cluster_id": 9416052,
          "cite": [
            "75 F.4th 597"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joseph Meadows v. City of Walker, Mich.",
          "cluster_id": 7857927,
          "cite": [
            "46 F.4th 416"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whitney Hodges v. City of Grand Rapids, Mich.",
          "cluster_id": 10595782,
          "cite": [
            "139 F.4th 495"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sean Hart v. City of Grand Rapids, Mich.",
          "cluster_id": 10584953,
          "cite": [
            "138 F.4th 409"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Linda Moser v. Etowah Police Dep't",
          "cluster_id": 6447900,
          "cite": [
            "27 F.4th 1148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Clemons v. John Couch",
          "cluster_id": 4898166,
          "cite": [
            "3 F.4th 897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jones",
          "cluster_id": 6479950,
          "cite": [
            "2022 Ohio 2122"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cory Driscoll v. Montgomery Cnty. Bd. of Comm'rs",
          "cluster_id": 10847360,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Louis Alford v. Brandon Deffendoll",
          "cluster_id": 10778906,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ashly Romero v. City of Lansing, Mich.",
          "cluster_id": 10738319,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reuben Jelani Adams v. Lexington-Fayette Urban Cnty. Gov't",
          "cluster_id": 10700490,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael Chrestman v. Metro Gov't of Nashville & Davidson Cnty., Tenn.",
          "cluster_id": 10672549,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4542480) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca6)",
        "reviewed": 16,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 16,
        "triage_read": 0,
        "triage_snippet_classified": 16
      },
      "lane2_top_cited": {
        "query": "cites:(4542480)",
        "reviewed": 22,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 22,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(4542480)",
        "reviewed": 11,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 11,
        "triage_read": 0,
        "triage_snippet_classified": 11
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4542480)",
    "indexed_citing_opinions": 22,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4542480,
        "count": 22,
        "count_source": "search"
      }
    ],
    "citation_count": 217,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/wright-v-city-of-euclid.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU3OTQxMiZzPTEwNzc4OTA2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%284542480%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4542480,
        "cited_id": 2092,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 178987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 196191,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 220504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 478767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 533819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 675736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 746760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 774301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 781854,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 792929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 794492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 796462,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 797071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 797998,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 804467,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 807291,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 807347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 856354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 857543,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 1192312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 1207949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 1238362,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 1462051,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 2641010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 2658128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 2760321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 2783172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 2787500,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 2805007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 2809264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 2981244,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 3178832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 3192192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 3194675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 3711678,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 3739859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 3747697,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 3763766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4027018,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4155276,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4193066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4216889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4237060,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4263410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4398647,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4405225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4422863,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4431725,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4486948,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 6762733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 6771749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 6951820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 7081890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9422887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9424277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9425988,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9427232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9430379,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9430387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9430599,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9431589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9431666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9434318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9475403,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9498217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9498341,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9501733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9501893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9520246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9842136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9848411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9873459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9877396,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "C",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T04:46:06Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:46:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:46:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:48:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:46:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Wright v. City of Euclid

```
                               RECOMMENDED FOR PUBLICATION
                               Pursuant to Sixth Circuit I.O.P. 32.1(b)
                                      File Name: 20a0185p.06

                   UNITED STATES COURT OF APPEALS
                                 FOR THE SIXTH CIRCUIT



 LAMAR WRIGHT,                                              ┐
                                  Plaintiff-Appellant,      │
                                                            │
                                                             >        No. 19-3452
        v.                                                  │
                                                            │
                                                            │
 CITY OF EUCLID, OHIO; KYLE FLAGG; VASHON                   │
 WILLIAMS,                                                  │
                         Defendants-Appellees.              │
                                                            ┘

                         Appeal from the United States District Court
                        for the Northern District of Ohio at Cleveland.
                    No. 1:17-cv-02503—Donald C. Nugent, District Judge.

                                  Argued: January 28, 2020

                              Decided and Filed: June 18, 2020

                                      _________________

                                           COUNSEL

ARGUED: Jacqueline C. Greene, FRIEDMAN & GILBERT, Cleveland, Ohio, for Appellant.
Frank H. Scialdone, MAZANEC, RASKIN AND RYDER CO., L.P.A., Cleveland, Ohio, for
Appellees. ON BRIEF: Jacqueline C. Greene, Sarah Gelsomino, Terry H. Gilbert,
FRIEDMAN & GILBERT, Cleveland, Ohio, for Appellant. Frank H. Scialdone, James A.
Climer, John D. Pinzone, MAZANEC, RASKIN AND RYDER CO., L.P.A., Cleveland, Ohio,
for Appellees.
                                     _________________

                                            OPINION
                                     _________________

       JOHN K. BUSH, Circuit Judge. This appeal involves a Chris Rock video and a cartoon,
but it is no laughing matter. In fact, this case raises a gravely important issue—police use of
 No. 19-3452                       Wright v. City of Euclid, et al.                        Page 2


force—that has dominated the nation’s attention in recent weeks. Lamar Wright, an African
American man, brought claims under 42 U.S.C. § 1983 of unconstitutional excessive force, false
arrest, malicious prosecution, and municipal liability, along with state-law claims, relating to the
actions of certain police officers and other officials employed by the City of Euclid, Ohio.

       The police officers, in plain clothes, approached Wright’s parked SUV with weapons
drawn. Thinking he was about to be robbed, Wright tried to back up the vehicle to get away.
A flash of a badge made him realize that the men he thought were about rob him were the police.
Wright stopped the SUV, and the officers pulled open the driver’s side door. Wright had no
weapon, and the officers holstered theirs. Nonetheless, they simultaneously deployed a taser
against him and pepper-sprayed him at point-blank range, all while he remained seated in the
vehicle. Wright had trouble getting out of the SUV because of a colostomy bag stapled to the
right side of his abdomen. He was recovering from a medical operation for diverticulitis. The
police aggravated the staples from his surgery, causing bleeding from around the bag.

       The officers then arrested Wright even though there was arguably no probable cause for
the arrest. The officers designated Wright’s arrest as arising from a drug investigation, even
though they found no drugs on him. This designation resulted in Wright’s being detained for
more than nine hours and subjected to an intrusive body scan for drugs well after the officers
knew of Wright’s medical condition. The scan revealed no drugs, and no drug-related charges
were ever brought against him.

       The district court granted summary judgment to the officers on the basis of qualified
immunity, and to the City based on Monell v. Department of Social Services, 436 U.S. 658, 690
(1978). As explained below, we disagree with the district court’s qualified immunity analysis.
With respect to the Monell claim, the evidence against the City includes the Chris Rock video,
played as part of its use-of-force training for officers, in which the comedian makes remarks
about Rodney King and police misconduct that are highly inappropriate for law-enforcement
instruction. The proof also includes an offensive cartoon in the City’s police-training manual
that portrays an officer in riot gear beating a prone and unarmed civilian with a club, with the
caption “protecting and serving the poop out of you.” R. 23 at PageID 808. Based on this
 No. 19-3452                       Wright v. City of Euclid, et al.                         Page 3


evidence and more, we find that Wright has introduced sufficient evidence of municipal policy to
satisfy Monell.

       For the reasons set forth below, we AFFIRM in part and REVERSE in part the district
court’s judgment, and REMAND for further proceedings consistent with this opinion.

                                                 I.

A.     Wright’s Stop, Arrest and Experience in Custody

       On November 4, 2016, at around 6:00 p.m., Lamar Wright pulled an SUV onto a
residential driveway off of 207th Street in Euclid, Ohio. After Wright rolled down his window,
conversation ensued with a friend who stood outside the residence. The friend never came over
to the SUV, and Wright never exited the vehicle. Their visit lasted for about a minute.

       Unbeknownst to Wright and his friend, plain-clothed Officers Kyle Flagg and Vashon
Williams, in an unmarked vehicle, were surveilling the friend’s home based on reports of illegal
drug activity in the area and at that residence in particular. The officers identified Wright’s
vehicle as a rented Ford Edge SUV. Based on the short amount of time Wright spent at the
house, the officers suspected that he may have been involved in a drug transaction.

       After Wright pulled out of the driveway, Flagg and Williams followed him. He turned
right onto Recher Avenue and then left onto East 212th Street. The officers maintain that at both
turns, Wright failed to use his turn signal, but there is no dash-cam footage or other evidence to
confirm the officers’ word. Wright insists that he did use his turn signal in both instances.

       The situation escalated after Wright pulled into a second driveway to answer a text
message from his girlfriend. While Wright texted in the SUV, the officers exited their vehicle,
drawing their guns as they approached the SUV. One of the men caught Wright’s eye when he
glanced up from his texting. In his side mirror, Wright could see this man dressed in dark
clothing with a gun pointed at the SUV. Believing that he was about to be robbed, Wright
dropped his cellphone in the center console and threw the car into reverse. Glancing to his left,
he saw another armed man, but this time he noticed a badge. Wright heard the men yell: “Shut
the car off!” and “Open the door!” Now realizing that the men were police officers, he put the
 No. 19-3452                        Wright v. City of Euclid, et al.                         Page 4


car in park and put his hands up. These events are corroborated by the body-cam footage.
At this point, Flagg stood beside the driver’s side door while Williams was next to the front
passenger door. Both officers holstered their guns.

       Next, Flagg yanked the driver’s side door open and demanded that Wright shut off the
vehicle. Wright complied and then raised his hands once more. Flagg grabbed Wright’s left
wrist, twisting his arm behind his back. The officer then attempted to gain control of Wright’s
right arm in order to handcuff him behind his back while he remained seated in the vehicle.
Flagg was unsuccessful in his efforts.       As Flagg continued to twist the left arm, Wright
repeatedly exclaimed that the officer was hurting him, to which Flagg responded, “let me see
your hand,” apparently referring to Wright’s right hand.

       Flagg then tried to pull Wright from the vehicle, but the latter had difficulty getting out.
As noted, Wright had recently undergone surgery for diverticulitis, which required staples in his
stomach and a colostomy bag attached to his abdomen. Though the officers apparently could not
see the bag and staples, these items prevented Wright from easily moving from his seat. Wright
placed his right hand on the center console of the car to better situate his torso to exit the car. By
this point Williams had moved over to stand behind Flagg on the driver’s side. Williams
responded to Wright’s hand movement by reaching around Flagg to pepper-spray Wright at
point-blank range.    Flagg simultaneously deployed his taser into Wright’s abdomen.             The
besieged detainee finally managed to exit the car with his hands up. He then was forced face
down on the ground, where he explained to officers that he had a “shit bag” on. Officer Williams
next handcuffed Wright while he was on the ground.

       Wright was bleeding from the staples that attached the colostomy bag to his abdomen.
The bag was now visible to Williams, who would testify that he “was kind of leery of getting
some sort of biohazard on [him].” R. 24 at PageID 938. The officers had Wright sit on the trunk
of his car while they called an ambulance. As the body cam continued to record, Flagg made
various arguably self-serving statements, including that “[Wright] was reaching like he had a
f***ing gun,” and that Flagg had been afraid that Wright was going to shoot him. Wright did not
have a gun, nor did he have any drugs or other contraband. The officers conceded that they did
not have probable cause to arrest Wright until after they believed he was resisting, and that they
 No. 19-3452                         Wright v. City of Euclid, et al.                     Page 5


had not seen Wright engage in any illegal activity prior to the arrest apart from his alleged
failures to use his turn signal. They arrested Wright for the misdemeanors of obstructing official
business and resisting arrest.

       After Wright’s arrest, a hospital doctor treated him for bleeding in his abdomen because
of the stress placed on the staples around his colostomy bag. Wright refused to submit to an x-
ray because of his recent surgery. The officers responded by demanding a CT scan of Wright’s
abdomen, but the doctors refused to perform the scan after consulting with the hospital’s legal
department. Wright was then discharged from the hospital and taken to the Euclid jail.

       At his 10:45 p.m. booking, Wright was charged with the two misdemeanors for which he
was arrested (obstructing official business and resisting arrest), along with two other offenses
(criminal trespass and failure to use a turn signal). Despite the fact that Wright had no drugs
when he was arrested and was not charged with any drug-related offenses, the officers
designated Wright’s arrest as stemming from a drug investigation. Flagg acknowledged that he
knew that this designation would result in Wright’s being subjected to additional, more thorough
searches.

       Wright posted bond between 11:00 p.m. and midnight, but he still was not released from
police custody. As Wright was attempting to leave the Euclid jail, a corrections officer told him
that he would be taken to the Cuyahoga County jail for a full body scan to see if he was hiding
drugs in his abdomen. Shortly after 1:00 a.m., he arrived at this next facility, where jail staff
searched him using a body scanner. The search turned up nothing. Wright finally was released
from custody at 3:55 a.m.

       Over seven months later, all the charges against Wright were dropped. Neither Flagg nor
Williams was investigated or disciplined for his encounter with Wright, and their use of force
was approved by their supervisors.

B.     The City of Euclid’s Practices and Customs

       Wright argues that his injury is directly attributable to the City’s policy or custom of
indifference to use of force. Euclid police officers undergo “defensive tactics training” that
 No. 19-3452                       Wright v. City of Euclid, et al.                       Page 6


purportedly trains officers in methods to defend themselves or defuse a situation.           Flagg
maintains he used “defensive tactics” in subduing Wright.

       This training contains a link to a YouTube video of a Chris Rock comedy skit entitled
“How not to get your ass kicked by the police!” The video shows numerous clips of multiple
police officers beating African-American suspects. During the video, Rock says things such as:

       “People in the black community . . . often wonder that we might be a victim of
       police brutality, so as a public service the Chris Rock Show proudly presents: this
       educational video.”
       “Have you ever been face-to-face with a police officer and wondered: is he about
       to kick my ass? Well wonder no more. If you follow these easy tips, you’ll be
       fine.”
       “We all know what happened to Rodney King, but Rodney wouldn’t have got his
       ass kicked if he had just followed this simple tip. When you see flashing police
       lights in your mirror, stop immediately. Everybody knows, if the police have to
       come and get you, they’re bringing an ass kicking with ‘em.”
       “If you have to give a friend a ride, get a white friend. A white friend can be the
       difference between a ticket and a bullet in the ass.”

InsaneNutter, Chris Rock-How not to get your ass kicked by the police! (Feb. 2, 2007),
https://www.youtube.com/watch?v=uj0mtxXEGE8 [https://perma.cc/NU2W-MGLN].

       Sergeant Murowsky conducts the use-of-force trainings and reviews all incidents of
officer-involved force. He stated that he thought the video was humorous and that it related to
things that Euclid police officers have experienced.        The City’s use-of-force training also
includes a PowerPoint presentation, the first page of which displays a stick figure cartoon
portraying a police officer in riot gear beating a prone and unarmed civilian with a club with the
caption “protecting and serving the poop out of you.” R. 23 at PageID 808.
 No. 19-3452                        Wright v. City of Euclid, et al.                        Page 7




        Sergeant Murowsky testified that he did not believe that the graphic conveys that the
Euclid Police Department “beat[s] the hell out of people,” R. 25 at PageID 1200, but he didn’t
know what other message could possibly be taken away from the image.

        Finally, the use-of-force training contains a meme that depicts two officers with their
guns drawn and aimed at something. It is captioned “Bed bug! Bed bug on my shoe!” Sergeant
Murowsky testified that he believed the image conveyed that the officers were overreacting to
and escalating a situation.

        When the Euclid Police Department receives allegations of excessive force, Sergeant
Murowsky reviews the relevant incident report to determine whether the use of force was
appropriate. Murowsky approved the use of force against Wright, as he had done numerous
times with respect to other incident reports. In fact, he testified that he had never heard of a use-
of-force incident by another Euclid officer that he deemed inappropriate. Likewise, Chief Meyer
testified that he had never found merit to any civilian complaint concerning use of force, false
arrest, or illegal searches.
 No. 19-3452                        Wright v. City of Euclid, et al.                         Page 8


C.     Proceedings Below

       Wright brought suit in the U.S. District Court for the Northern District of Ohio against
the City of Euclid and Officers Flagg and Williams, alleging counts under 42 U.S.C. § 1983 of
excessive force, false arrest, malicious prosecution, failure to intervene, extended detention, and
the City’s municipal liability, along with claims under Ohio law for malicious prosecution and
intentional infliction of emotional distress. After the close of discovery, the district court granted
summary judgment to the officers and the City. Wright v. City of Euclid, No. 1:17 CV 2503,
2019 WL 2009453, at *12 (N.D. Ohio May 7, 2019). Wright filed a timely appeal.

                                                 II.

       We review a district court’s grant of summary judgment de novo. Jackson v. City of
Cleveland, 925 F.3d 793, 806 (6th Cir. 2019) (internal quotations omitted). Summary judgment
is appropriate when “no genuine dispute as to any material fact” exists and the moving party “is
entitled to judgment as a matter of law.” Fed. R. Civ. P. 56(a). “A genuine dispute of material
fact exists ‘if the evidence is such that a reasonable jury could return a verdict for the nonmoving
party.’” Peffer v. Stephens, 880 F.3d 256, 262 (6th Cir. 2018) (quoting Anderson v. Liberty
Lobby, Inc., 477 U.S. 242, 248 (1986)). At the summary judgment stage, “the evidence is
construed and all reasonable inferences are drawn in favor of the nonmoving party.” Burgess v.
Fischer, 735 F.3d 462, 471 (6th Cir. 2013) (citing Hawkis v. Anheuser-Busch, Inc., 517 F.3d
321, 332 (6th Cir. 2008)).

       Wright raises several arguments on appeal. First, he argues that the district court erred in
granting summary judgment on qualified immunity grounds to Flagg and Williams for his
excessive-force and failure-to-intervene claims based on brandishing their firearms and using a
taser and pepper spray when he was not actively resisting arrest. Second, he argues that the
district court erred in granting the officers qualified immunity on his false-arrest and extended-
detention claims. Third, he claims that the district court erred in granting qualified immunity to
the officers on his federal malicious-prosecution claim. Fourth, he argues that the district court
erred in holding that the officers were entitled to statutory immunity for his state-law claims.
Fifth, he argues that the district court erred in granting the officers summary judgment on his
 No. 19-3452                       Wright v. City of Euclid, et al.                        Page 9


state-law claims of malicious prosecution and intentional infliction of emotional distress. Sixth,
and finally, he argues that the district court erred in granting summary judgment to the City of
Euclid under Monell.

       Most of Wright’s arguments hinge on whether Flagg and Williams are immune from suit
through qualified immunity or statutory immunity under Ohio law. We analyze whether an
officer is entitled to qualified immunity using two steps: (1) whether the defendant violated a
constitutional right; and (2) whether that constitutional right was clearly established at the time
of the alleged violation. Fazica v. Jordan, 926 F.3d 283, 289 (6th Cir. 2019). A similar inquiry
applies to statutory immunity under Ohio law. See Hopper v. Phil Plummer, 887 F.3d 744, 759
(6th Cir. 2018).

A.     Excessive Force

       Wright first argues that the district court erred in granting qualified immunity to Flagg
and Williams on his excessive-force claims. He maintains that the officers used excessive force
in brandishing their firearms as they approached his vehicle, that Flagg used excessive force in
deploying his taser, and that Williams used excessive force in using pepper spray, all while
(Wright claims) he was not resisting arrest.

       “When more than one officer is involved, the court must consider each officer’s
entitlement to qualified immunity separately.” Smith v. City of Troy, 874 F.3d 938, 944 (6th Cir.
2017) (per curiam). And when, as here, a plaintiff claims that excessive force was used multiple
times, “the court must segment the incident into its constituent parts and consider the officer’s
entitlement to qualified immunity at each step along the way.” Id.

       1.      Officer Flagg

               a.      Constitutional Violation

       Wright argues that Flagg “used far more force than necessary to effect an arrest,”
Appellant’s Br. at 42, when he approached Wright’s SUV with his gun drawn and later deployed
his taser on Wright while the latter sat in the driver’s seat of the vehicle. When making an arrest
or investigatory stop, the police have “the right to use some degree of physical coercion or threat
 No. 19-3452                       Wright v. City of Euclid, et al.                       Page 10


thereof to effect it.” Graham v. Connor, 490 U.S. 386, 396 (1989). In determining whether the
use of force in effecting an arrest is excessive in violation of the Fourth Amendment, we must
determine “whether the officers’ actions [were] ‘objectively reasonable’ in light of the facts and
circumstances confronting them, without regard to their underlying intent or motivation.” Id. at
397. This inquiry assesses “reasonableness at the moment” of the use of force, as “judged from
the perspective of a reasonable officer on the scene, rather than with the 20/20 vision of
hindsight.” Goodwin v. City of Painesville, 781 F.3d 314, 321 (6th Cir. 2015) (quoting Graham,
490 U.S. at 396).

       The bottom-line inquiry is “whether the totality of the circumstances justifies a particular
level of force.”    Coffey v. Carroll, 933 F.3d 577, 588 (6th Cir. 2019) (citing Mitchell v.
Schlabach, 864 F.3d 416, 421 (6th Cir. 2017)). Three factors from Graham guide this analysis:
“[1] the severity of the crime at issue, [2] whether the suspect poses an immediate threat to the
safety of the officers or others, and [3] whether he is actively resisting arrest or attempting to
evade arrest by flight.” Shreve v. Jessamine Cty. Fiscal Court, 453 F.3d 681, 687 (6th Cir. 2006)
(quoting Graham, 490 U.S. at 396). Balancing these factors, and viewing the record in the light
most favorable to Wright, a reasonable juror could conclude that Flagg used excessive force both
when he brandished his firearm and when he deployed his taser.

       As to the firearm, we have held that a police officer may approach a suspect with a
weapon drawn during a Terry stop when the officer reasonably fears for his safety. United States
v. Hardnett, 804 F.2d 353, 357 (6th Cir. 1986); see also United States v. Heath, 259 F.3d 522,
530 (6th Cir. 2001) (“[When the] surrounding circumstances give rise to a justifiable fear for
personal safety, a seizure effectuated with weapons drawn may properly be considered an
investigative stop.” (alteration in original) (quoting Hardnett, 804 F.2d at 357)). Moreover, we
have held that when a suspect is reasonably suspected of carrying drugs, an officer is “entitled to
rely on [his] experience and training in concluding that weapons are frequently used in drug
transactions.” Heath, 259 F.3d at 530. In Heath, the officers surveilled the defendant four times
over the course of a month and observed conduct that they believed was consistent with drug
activity, including stopping at locations under investigation for drug activity, checking for tails,
and associating with “a large-scale drug trafficker.” Id. at 525. The police had identified the
 No. 19-3452                        Wright v. City of Euclid, et al.                      Page 11


defendant and knew that he had three misdemeanor convictions and one felony drug conviction.
Id. at 524. They also obtained information from a confidential informant that the defendant was
trafficking in large quantities of cocaine. Id. In those circumstances, we held that it was
reasonable for the officers to approach the defendant’s vehicle with their guns drawn when
conducting a Terry stop after seeing him leave a building with a known large-scale drug
trafficker while carrying a bag. Id. at 530.

       Relying on Heath’s “drug activity = guns” premise, the district court in this case held as a
matter of law that Flagg and Williams were justified in drawing their weapons for protection
upon approaching Wright’s vehicle. See Appellant’s Br. at 44; see also Wright, 2019 WL
2009453, at *6 (“Thus, the officers in this case, having an objective reason to believe that
Mr. Wright may have been involved in drug activity, also had a reasonable belief that he may be
in possession of a weapon.”). The facts in this case, however, can be distinguished from Heath.
Unlike the defendant officers in Heath, the officers here had very little, if any, reason to think
that the detainee was involved in drug activity. Flagg and Williams had observed Wright pull
into a driveway at his friend’s house and speak to his friend for about one minute to exchange
greetings. According to Wright, he did not pull all the way up the driveway. While conversing,
Wright stayed in his car and the friend stayed on the porch. According to the officers, they were
surveilling the residence “based upon multiple arrests and complaints regarding drug activity.”
However, according to Wright, the prior complaints for the residence were all stale, only three of
the six complaints pertained to drugs, and none of the complaints pertained to him. Flagg and
Williams also admit that they did not see Wright engage in any criminal activity, drug-related or
otherwise, while stopped at the residence.

       Nevertheless, based only on Wright’s brief stop at the residence, the officers decided to
conduct a traffic stop with weapons drawn. These circumstances are very different from those in
Heath where the officers had a justifiable fear for their safety given that the defendant, whom
they had identified and surveilled for a month, was a large-scale drug dealer and likely to be
carrying a weapon. Flagg and Williams at most had a suspicion that Wright had briefly visited
with a suspected drug dealer, but given that the officers had not identified Wright himself as a
drug dealer or sought any corroboration of their suspicions of criminal activity, there is a genuine
 No. 19-3452                        Wright v. City of Euclid, et al.                     Page 12


dispute as to whether the officers were justified in brandishing their firearms upon approach.
Thus, a jury must determine whether their decision to do so was unconstitutionally excessive.
See, e.g., Croom v. Balkwill, 645 F.3d 1240, 1252 n.17 (11th Cir. 2011) (“An officer’s decision
to point a gun at an unarmed civilian who objectively poses no threat to the officer or the public
can certainly sustain a claim of excessive force.” (collecting cases)).

       Second, as to Flagg’s use of his taser, we hold that this too must be submitted to a jury to
determine whether the use of force was excessive. The tasering occurred when Flagg had, at
most, reasonable suspicion—not probable cause—to detain him for the officers’ drug
investigation. See Ciminillo v. Streicher, 434 F.3d 461, 467 (6th Cir. 2006) (noting that “the fact
that a plaintiff in a § 1983 suit had committed no crime clearly weighed against a finding of
reasonableness”). Therefore, at no point before Flagg began to seize Wright did Flagg have
probable cause to arrest him. The first Graham factor, relating to the severity of the suspected
crime, thus cuts against a finding of justified use of force because there was no probable cause
that he had committed any crime at all before the tasering occurred.

       “Of course, the use of force can be reasonable, even when the crime at issue is innocuous.
To determine whether this is so, we turn to the [second and third] Graham factors.” Thomas v.
Plummer, 489 F. App’x 116, 126 (6th Cir. 2012). Construing the record in the light most
favorable to Wright, the second Graham factor—the immediate safety threat posed by the
suspect to police and others—weighs in his favor as well. When Flagg deployed his taser,
Wright was doing his best to comply with the officers’ commands despite his recent surgery and
difficulty in exiting the SUV. After Flagg and Williams had holstered their weapons, Flagg
opened the driver’s side door and Wright put his hands up. Flagg then demanded Wright turn off
the engine, an order with which Wright complied, followed immediately by putting his hands up
again. When Wright was unable to comply with Flagg’s commands because of his stomach
staples and colostomy bag, the encounter turned violent. Wright was not armed. According to
Flagg, he thought Wright was reaching for a weapon in the center console and considered that
movement to be an act of resisting arrest. Wright, however, disputes that his hand movement
was threatening to the extent that he moved his hand at all. Although these two versions of
events are not inconsistent with each other—that is, Flagg could have reasonably believed
 No. 19-3452                       Wright v. City of Euclid, et al.                       Page 13


Wright was reaching for a gun when in reality he was trying to comply with orders—a
reasonable jury could find, based on the totality of the circumstances, that a reasonable officer
would not believe that Wright posed an immediate threat to their safety.

       Finally, the third Graham factor, which hinges on whether Wright was “actively” or
“passively” resisting arrest, weighs in his favor as well when the facts are construed in his favor.
See Goodwin v. City of Painesville, 781 F.3d 314, 323 (6th Cir. 2015) (noting that while active
resistance to an officer’s command can justify use of a taser, passive resistance—or no resistance
at all—does not justify such use of force) (citing Hagans v. Franklin Cty. Sheriff’s Office,
695 F.3d 505, 509 (6th Cir. 2012)). Flagg maintains that when he opened the driver’s side door,
he grabbed Wright’s left wrist and began to bring his left arm under control. Flagg claims that
when Wright pushed down on the center console, Flagg lost control of Wright’s arm, which
Flagg described as an act of resistance. A reasonable juror, however, could accept Wright’s
account that he was not resisting, but rather was simply having difficulty maneuvering while
seated in the vehicle and in Officer Flagg’s forced hold.

       Even if Flagg is correct that Wright’s act of pushing down on the center console
constituted some resistance, if the resistance was merely “passive,” then the use of a taser was
unreasonable. See Goodwin, 781 F.3d at 323. The tasering of Wright was justified only if he
engaged in resistance that was “active,” which “can take the form of ‘verbal hostility’ or a
‘deliberate act of defiance.’” Id. at 323 (quoting Eldridge v. City of Warren, 533 F. App’x 529,
534–35 (6th Cir. 2013)).

       We recognized this principle in Smith v. City of Troy, where the plaintiff was tased while
experiencing an epileptic seizure. 874 F.3d at 942. In that case, when officers arrived at the
scene, the plaintiff was standing outside his car clinging to a fence, which led the officers
mistakenly to believe that he had been driving under the influence. Id. In an attempt to return
the plaintiff to his car, an officer tried to pry the plaintiff’s fingers from the fence. Id. The
plaintiff responded by pulling his arm away from the officer, at which point the officer forced the
plaintiff to the ground and wrestled with him until a second officer arrived and deployed his
taser. Id. The district court granted the officers qualified immunity, holding that “the officers
used measured force in response to [the plaintiff’s] defiance of their orders and reaching where
 No. 19-3452                       Wright v. City of Euclid, et al.                      Page 14


the officers could not see his hands.” Id. at 943. We reversed, holding that “[a] reasonable juror
could conclude that, in pulling his arm away, [the plaintiff’s] resistance was minimal and that
[the force used] was excessive.” Id. at 945.

        Similarly, the facts regarding Wright’s arm movement would allow a reasonable juror to
find that his resistance was minimal to the extent that it constituted resistance at all. Wright
maintains that he reached down towards the center console in order to assist the officers in
removing him from the SUV because his mobility was limited as a result of his surgery,
colostomy bag, and staples in his stomach. However, Flagg claims that he was not aware of
Wright’s medical problems until after he had deployed his taser. The reasonableness of force is
predicated solely on the knowledge of officers in the moments before the force is used. Graham,
490 U.S. at 396–97. Therefore, if the officers did not know of Wright’s recent surgery, the
colostomy bag or the stomach staples, those facts would bear no weight in the reasonableness
calculus. But, even if the officers had no knowledge of any of these facts, there are other facts
that, when construed in Wright’s favor, could support a reasonable juror’s finding that Wright
did not actively resist. In a split-second reaction, Wright pushed down on the center console in
an attempt to maneuver his torso into a better position to get out of the car. Construing the
record in the light most favorable to Wright, his act of purported resistance is close enough to
that of the plaintiff in Smith to present a question of fact for a jury to decide whether Wright in
fact actively resisted arrest.

        That this issue presents a jury question is confirmed by our consideration of the officer’s
actions “in light of testimony regarding the training that [the officer] received.” Griffith v.
Coburn, 473 F.3d 650, 657 (6th Cir. 2007). Wright presented expert testimony from Roy Taylor,
a police officer and expert on police-involved use of force, who testified that the level of force
used was unreasonable. In his affidavit, Taylor noted that the Model Policy on Electronic
Control Weapons of the International Association of Chiefs of Police (of which the Euclid police
chief is a member), the TASER training manual, and the Euclid Police Department’s use-of-
force continuum, each outline circumstances in which use of a taser is appropriate. According to
Taylor, “[n]one of the circumstances . . . were present when Officer Flagg deployed his taser
 No. 19-3452                        Wright v. City of Euclid, et al.                      Page 15


against Lamar Wright. Officer Flagg used a greater level of force than other officers would have
used if facing the same, or similar circumstances.” R. 31-6 at PageID 1415.

         Finally, and significantly, at no point before Flagg deployed his taser was Wright under
arrest for any offense. As we noted in Smith, “the mere failure of a citizen—not arrested for any
crime—to follow the officer’s commands does not give a law enforcement official authority to
put the citizen in handcuffs.” 874 F.3d at 945. By the same logic, an officer may not tase a
citizen not under arrest merely for failure to follow the officer’s orders when the officer has no
reasonable fear for his or her safety. Whether the tasering in this instance was constitutionally
permissible must be decided by the jury, given the genuine factual disputes described above
concerning the circumstances of Wright’s encounter with the officers.

                b.      Clearly Established Right

         We now must decide whether, accepting Wright’s version of the facts, Flagg’s drawing
of his weapon and use of the taser violated a constitutional right that was “clearly established at
the time of the alleged violation.” Campbell v. City of Springboro, 700 F.3d 779, 786 (6th Cir.
2012).    For this prong of the qualified immunity analysis, we are “not to define clearly
established law at a high level of generality.” Ashcroft v. al-Kidd, 563 U.S. 731, 742 (2011).

         The district court held that it was “unaware of any controlling cases that have established
a constitutional violation occurred when non-lethal force was used to obtain control over the
suspect who reasonably appeared to pose a safety risk to officers.” Wright, 2019 WL 2009453,
at *7. In so holding, the district court examined the issue of whether the law was clearly
established using too specific of a level of generality. See al-Kidd, 563 U.S. at 742. The district
court also incorrectly framed the issue based upon Flagg’s version of the facts by assuming that
Wright did in fact “reasonably appear[] to pose a safety risk” to the officer. Given that this was a
summary judgment ruling, the district court instead should have considered whether the law was
clearly established using Wright’s version of the facts. Wright contends that he had done
nothing prior to his encounter with police to justify the officers’ brandishing of their firearms.
He also maintains that he had a right not to be tased when, during the course of an investigatory
detention, he inadvertently broke away from the officer’s grip, but presented no threat to others,
 No. 19-3452                       Wright v. City of Euclid, et al.                       Page 16


and did not actively resist arrest. For the reasons discussed below, we hold that, viewing the
facts in Wright’s favor, Flagg’s drawing of his firearm and use of his taser violated Wright’s
constitutional rights that were clearly established as of the date of the encounter, November 4,
2016.

        We reach this conclusion by examining “whether the contours of” the plaintiff’s
constitutional rights “were sufficiently defined to give a reasonable officer fair warning that the
conduct at issue was unconstitutional.” Brown v. Chapman, 814 F.3d 447, 461 (6th Cir. 2016).
“This is not to say that an official action is protected by qualified immunity unless the very
action in question has previously been held unlawful, . . . but it is to say that in light of pre-
existing law the unlawfulness must be apparent.” Hope v. Pelzer, 536 U.S. 730, 739 (2002)
(quoting Anderson v. Creighton, 482 U.S. 635, 640 (1987)). “In determining whether a right was
clearly established, we look first to decisions of the Supreme Court, then to our own
precedents, and then to decisions of other courts of appeal, and we ask whether these precedents
‘placed the . . . constitutional question beyond debate.’” Hearring v. Sliwowski, 712 F.3d 275,
280 (6th Cir. 2013) (quoting al-Kidd, 563 U.S. at 741).

        With respect to an officer’s use of a firearm, we have recognized that “pointing a firearm
at an individual and making a demand of that individual . . . communicates the implicit threat
that if the individual does not comply with the . . . demands, the [one pointing the firearm] will
shoot the individual.” Vanderhoef v. Dixon, 938 F.3d 271, 277 (6th Cir. 2019) (quoting United
States v. Bolden, 479 F.3d 455, 461 (6th Cir. 2007)). We have also recognized that pointing a
gun at an individual can constitute excessive force under the Fourth Amendment. See Binay v.
Bettendorf, 601 F.3d 640, 650 (6th Cir. 2010). We have addressed a similar scenario before. In
Davis v. Bergeon, 187 F.3d 635, 1999 WL 591448 (6th Cir. 1999) (table), we concluded that
pointing or displaying a firearm could constitute excessive force in the following circumstances:

        [The detective] was not in the process of an arrest, but inspecting the ladies’
        restroom. [The plaintiff] was attempting to enter the men’s restroom to use the
        facilities and was not suspected of any wrongdoing at that point in time. [The
        detective], dressed in plainclothes, allegedly did not identify herself, pointed her
        weapon at [the plaintiff] and ordered him to get on the floor.
 No. 19-3452                        Wright v. City of Euclid, et al.                       Page 17


Id. at *5. We concluded that those facts sufficed to allow a jury to find that the officer had
violated the plaintiff’s clearly established Fourth Amendment rights. Id. at *5–6; see also Saad
v. City of Dearborn, No. 10-12635, 2011 WL 3112517, at *5 (E.D. Mich. July 26, 2011), aff’d
sub nom. Saad v. Krause, 472 F. App’x 403 (6th Cir. 2012) (per curiam) (noting that that the
Sixth Circuit has “held that pointing a gun at an unarmed suspect who is not fleeing or posing a
risk to police officers may be an objectively unreasonable use of force” (citing Binay, 601 F.3d at
650)). Based on this authority, it was clearly established as of the time of Wright’s encounter
with the officers that brandishing a firearm without a justifiable fear that Wright was fleeing or
dangerous was unreasonable and constituted excessive force.

       In conducting the analysis as it pertains to use of the taser, two lines of cases emerge.
The first holds that there is no clearly established right not to be tased when a suspect is actively
resisting arrest. See, e.g., Hagans v. Franklin Cty. Sheriff’s Office, 695 F.3d 505, 509–10 (6th
Cir. 2012) (noting that, as of 2007, a suspect who refused to be handcuffed and actively resisted
arrest did not have a clearly established right not to be tased). The second line of authority holds
that there is a clearly established right not to be tased when the suspect is not actively resisting
arrest. See Brown, 814 F.3d at 462 (holding that “as of December 31, 2010, it was clearly
established that tasering a non-threatening suspect who was not actively resisting arrest
constituted excessive force”); Coffey, 933 F.3d at 589 (“Drawing the line at a suspect’s active
resistance defines the right at a level of particularity appropriate for a claim pursued under
§ 1983.”); Smith, 874 F.3d at 945 (“It was well-established [in 2014] that a non-violent, non-
resisting, or only passively resisting suspect who is not under arrest has a right to be free from an
officer’s use of force.”). Assuming Wright’s version of the facts to be true, this case falls neatly
within the second category of cases.

       To summarize, a reasonable jury could find that Flagg’s actions constituted unreasonable
and constituted excessive force. It was clearly established as of November 4, 2016 that drawing
a weapon on a suspect who was not fleeing or posing a safety risk and tasering a suspect who
was not actively resisting arrest constituted excessive force. Therefore, we REVERSE the
district court’s grant of summary judgment on qualified immunity grounds to Flagg as to the
excessive-force claims.
 No. 19-3452                         Wright v. City of Euclid, et al.                      Page 18


         2.     Officer Williams

                a.      Violation of a Constitutional Right

         Wright’s excessive-force claim against Williams, based on his brandishing of a firearm
and use of the pepper spray, largely mirrors the claim against Flagg based on his similar use of a
firearm and tasing, and therefore the analysis is largely the same. The discussion of the Graham
factors as they relate to Williams is identical to the analysis of those factors as they concern
Flagg. The severity of the crime, whether Wright was a threat to the police, and whether Wright
actively resisted arrest all present questions of fact that should be decided by a jury.

         In Adams v. Metiva, 31 F.3d 375 (6th Cir. 1994), we held that summary judgment was
inappropriate for an excessive-force claim brought against police officers for the use of pepper
spray, when it remained genuinely disputed whether the plaintiff had committed a crime,
whether he posed a threat, and whether he was resisting arrest. Id. at 385–86; see also Vaughn v.
City of Lebanon, 18 F. App’x 252, 266–68 (6th Cir. 2001). Here, as discussed, it remains
genuinely disputed whether Wright had committed a crime, whether he posed a threat to officers,
and whether he was actively resisting arrest. See, e.g., Grawey v. Drury, 567 F.3d 302, 311 (6th
Cir. 2009) (“An officer has used excessive force when he pepper sprays a suspect who has not
been told she is under arrest and is not resisting arrest.”).

         The body-cam footage shows that while Flagg was attempting to gain control of Wright’s
right arm, Williams reached into the car with the can of pepper spray and sprayed Wright within
inches of his face. Wright’s expert opined that the use of pepper spray at this close distance was
unreasonably dangerous and violated nationally-accepted standards and protocols, which dictate
that pepper spray “should not be used on someone closer than three feet from the canister’s
nozzle.” R. 31-6 at PageID 1416. Further, this expert noted that the Euclid Police Department’s
use-of-force continuum indicates that pepper spray should be used only when an individual is
wrestling with or pushing an officer, not when the suspect is pulling away from an officer. This
testimony supports Wright’s argument that Williams acted unreasonably in his use of the pepper
spray.
 No. 19-3452                        Wright v. City of Euclid, et al.                        Page 19


        Furthermore, the evaluation of the reasonableness of officers’ use of force “considers the
effects of their actions, as any inquiry into a violation of the Fourth Amendment requires a
careful balancing of ‘the nature and quality of the intrusion on the individual’s Fourth
Amendment interests’ against the countervailing governmental interests at stake.”             Brown,
814 F.3d at 459 (quoting Graham, 490 U.S. at 396). As Wright’s expert opined, use of pepper
spray at such a close proximity risks significant injury, which is not present if the officer uses the
spray at a safe distance. This testimony and the other proof present a jury question as to whether
Williams’s use of the pepper spray constituted excessive force in violation of Wright’s
constitutional rights.

                b.       Clearly Established Right

        For reasons similar to those discussed above as they relate to Flagg’s use of his taser, we
hold that the right to be free from being pepper sprayed when a suspect is not actively resisting
arrest was also clearly established at the time of the encounter in question. See, e.g., Coffey, 933
F.3d at 589 (6th Cir. 2019) (“Drawing the line at a suspect’s active resistance defines the right at
a level of particularity appropriate for a claim pursued under § 1983.”); Smith, 874 F.3d at 945
(“It was well-established [in 2014] that a non-violent, non-resisting, or only passively resisting
suspect who is not under arrest has a right to be free from an officer’s use of force.”).

        Wright has produced evidence that would allow a reasonable juror to conclude that he
had not committed a serious crime, or any crime at all; that he was not a danger to the officers or
the public; and that he was not resisting arrest. Although the officers tell a different story, it
should be up to the jury to determine whose story is more credible. Therefore, we REVERSE as
to the excessive-force claim against Williams for deploying his pepper spray, as well as for
brandishing his firearm.

B.      Failure to Intervene

        Wright further claims that both Flagg and Williams failed to intervene to protect him
from alleged excessive force committed by the other. In order to establish such a claim, Wright
must prove that “the officer observed or had reason to know that the excessive force would be or
was being used and that the officer had both the opportunity and the means to prevent the harm
 No. 19-3452                        Wright v. City of Euclid, et al.                      Page 20


from occurring.” Smith, 874 F.3d at 945–46 (citing Turner v. Scott, 119 F.3d 425, 429 (6th Cir.
1997)). Wright maintains that because the officers were “practically on top of each other” when
they used the allegedly excessive force of the taser and pepper spray, Appellant’s Br. at 49, each
officer had the opportunity to prevent the other from using force.          However, we are not
persuaded that the evidence would allow a reasonable juror to find a constitutional violation as to
either of these failure-to-intervene claims.

       In Smith, we held that when one officer was “occupied trying to gain control of [the
plaintiff’s] arms while [the other officer] was deploying his taser,” no reasonable juror could find
that the officer had the opportunity and the means to prevent the excessive force. 874 F.3d at
946. So too here. Although Wright is correct that the officers were in close proximity to each
other, the body-cam footage from both Flagg and Williams shows that when Williams used
pepper spray on Wright, Flagg was struggling with Wright in an attempt to remove him from the
car. Like the officer in Smith, at the time Williams used his pepper spray, Flagg was preoccupied
with attempting to detain Wright. The body-cam footage shows Flagg grappling with Wright’s
arms when Williams reached into the car to deploy the pepper spray. This all happened within a
span of approximately ten seconds. Therefore, similar to the court’s holding in Smith, we hold
that no reasonable juror could find that Flagg had the opportunity and means to prevent Williams
from using pepper spray. See id.

       Likewise, no reasonable juror could find a constitutional violation in Williams’s failure to
prevent Flagg’s use of his taser. The body cam footage shows that Flagg tased Wright for
approximately five seconds during which time Williams reached around Flagg to pepper spray
Wright. The use of force happened almost simultaneously. Wright has failed to demonstrate
“that the incident lasted long enough for [Williams] to both perceive what was going on” with
Flagg’s tasering “and intercede to stop it.” Burgess, 735 F.3d at 475.

       Therefore, we AFFIRM the district court’s grant of summary judgment to Flagg and
Williams with respect to the failure-to-intervene claims.
 No. 19-3452                        Wright v. City of Euclid, et al.                      Page 21


C.     Fourth Amendment False Arrest

       Wright also maintains that the district court erred in granting summary judgment to the
officers on his Fourth Amendment false-arrest claim. For Wright to succeed on this claim, he
must prove that the police lacked probable cause to arrest him. Burley v. Gagacki, 834 F.3d 606,
613–14 (6th Cir. 2016). “An officer possesses probable cause when, at the moment the officer
seeks the arrest, ‘the facts and circumstances within the officer’s knowledge and of which [he]
had reasonably trustworthy information are sufficient to warrant a prudent man in believing that
the plaintiff had committed or was committing an offense.’” Wesley v. Campbell, 779 F.3d 421,
429 (6th Cir. 2015) (alterations omitted) (quoting Beck v. Ohio, 379 U.S. 89, 91 (1964)). “If
probable cause exists to arrest the suspect for any of the charged offenses, then the false arrest
claim must fail.” Fineout v. Kostanko, 780 F. App’x 317, 328 (6th Cir. 2019) (citing Lyons v.
City of Xenia, 417 F.3d 565, 573 (6th Cir. 2005)).

       Wright was charged for failure to use his turn signal, resisting arrest, obstructing official
business, and criminal trespass. However, for purposes of summary judgment, the officers
maintain that their bases for probable cause to arrest were Wright’s resisting arrest and his
obstruction of official business. We therefore address below whether probable cause existed for
the arrest based on these latter charges only.

       1.      Obstructing Official Business

       The officers contend that they arrested Wright, in part, “because he was … obstruct[ing]
official business.” Appellees’ Br. at 40. Under Ohio law, one is guilty of obstructing official
business if he, “without privilege to do so and with purpose to prevent, obstruct, or delay the
performance by a public official of any authorized act within the public official’s official
capacity, shall do any act that hampers or impedes a public official in the performance of the
public official’s lawful duties.” Ohio Rev. Code § 2921.31. With respect to the element of
“purpose to obstruct,” “[a] person acts purposely when it is his specific intention to cause a
certain result.” City of N. Ridgeville v. Reichbaum, 677 N.E.2d 1245, 1249 (Ohio 1996) (quoting
Ohio Rev. Code § 2901.22(A)). The statute also requires an affirmative act that interrupts police
business; “[a] person may not be convicted of the offense simply by doing nothing.” Lyons,
 No. 19-3452                        Wright v. City of Euclid, et al.                        Page 22


415 F.3d at 573 (citing State v. McCrone, 580 N.E.2d 468, 470–71 (Ohio 1989)). The act must
actually hamper or impede the officer in the performance of his duties, and “there must be some
substantial stoppage of the officer’s progress.” State v. Wellman, 879 N.E.2d 215, 219 (Ohio
2007) (quoting State v. Stephens, 387 N.E.2d 252, 253 (Ohio 1978)).

       On several occasions we have examined the Ohio statute that prohibits obstruction of
official business. The affirmative-act requirement requires more than a failure to comply with an
officer’s request. See Jones v. City of Elyria, 947 F.3d 905, 915 (6th Cir. 2020) (citing Patrizi v.
Huff, 690 F.3d 459, 464 (6th Cir. 2012)). Also, when a suspect pulls her hand away from the
police but otherwise complies with orders, she has not engaged in an affirmative act giving
officers probable cause to arrest for obstruction of official business. Smith v. City of Wyoming,
821 F.3d 697, 716 (6th Cir. 2016). Based on this standard, a reasonable juror could find that
Wright’s actions did not involve any affirmative act that obstructed police business. Wright
maintains that he was doing his best to comply, and the act of moving his arm was really an
attempt to maneuver his torso in the car so as to allow Flagg to remove him from the car—
despite the fact that the seizure was unlawful.

       Certainly, Wright’s and the officers’ respective versions of events are not necessarily
inconsistent. Wright could have earnestly believed that he was trying to help Flagg remove him
from the car, and Flagg could have simultaneously believed that Wright was trying to interfere
with his arrest. But viewing the facts in the light most favorable to Wright, a reasonable jury
could find that he did not engage in an affirmative act such as to give rise to probable cause that
he was obstructing official business.

       2.      Resisting Arrest

       In his deposition, Flagg conceded that he did not have probable cause to arrest Wright
until he started “resisting.” This puts the cart before the horse. When an underlying arrest is for
resisting arrest and nothing more, “the officers could not, as a matter of law, have probable cause
to arrest [Wright] where the underlying arrest was not lawful.” Osberry v. Slusher, 750 F. App’x
385, 395 (6th Cir. 2018); see Ohio Rev. Code § 2921.33(A) (“No person, recklessly or by force,
shall resist or interfere with a lawful arrest . . . .”) (emphasis added); see also Hoover v. Garfield
 No. 19-3452                          Wright v. City of Euclid, et al.                   Page 23


Heights Mun. Court, 802 F.2d 168, 174 (6th Cir. 1986) (“[W]e conclude that [Ohio Rev. Code]
§ 2921.33 indeed forbids only resisting a lawful arrest and does not prohibit resisting an unlawful
arrest.”). Because a reasonable jury could find that Flagg and Williams did not have probable
cause to arrest Wright prior to his alleged resistance, they are not entitled to summary judgment
that the arrest was justified. See Osberry, 750 F. App’x at 395.

                                              * * * * *

       If the jury finds that the officers lacked probable cause that Wright had engaged in any
illegal activity, then it would be clearly established that the officers falsely arrested him, in
violation of his Fourth Amendment rights. Indeed, the right to be free from arrest without
probable cause is a “quintessential example[] of [a] ‘clearly established’ constitutional right.”
Jones, 947 F.3d at 915. Wright has presented sufficient evidence for a reasonable jury to find no
probable cause—and no qualified immunity—for the arrest.

       Therefore we REVERSE the district court’s grant of summary judgment to Flagg and
Williams on the false-arrest claim.

D.     Extended Detention

       Wright also brought a claim for a violation of the Fourth Amendment based on his
extended detention after he posted bond. This claim is, in essence, derivative of his false-arrest
claim—that is, his detention was unreasonably extended without probable cause. The Fourth
Amendment “establishes the minimum constitutional ‘standards and procedures’ not just for
arrest but also the ensuing ‘detention.’” Manuel v. City of Joliet, 137 S. Ct. 911, 917 (2017)
(quoting Gerstein v. Pugh, 420 U.S. 103, 111 (1975)).

       1.      Constitutional Violation

       Before being taken into custody, Wright was hospitalized for his injuries from his
encounter with Flagg and Williams.          Both officers stayed in the hospital with Wright for
approximately four hours. Wright alleges that, during that time, the officers sought a CT scan of
Wright because they thought he was hiding drugs in his abdomen. At one point, hospital staff
took Wright to get an X-ray, but he refused to consent because of radiation concerns. According
 No. 19-3452                       Wright v. City of Euclid, et al.                    Page 24


to Wright, his refusal to be X-rayed infuriated Flagg and Williams, along with other unnamed
officers who were present at the hospital. The officers were so angry, according to Wright, that
they told him they were going to charge him because he would not be X-rayed.

       Upon discharge from the hospital, Wright was indeed arrested and taken to the Euclid
City Jail. Wright was booked at this facility at 10:49 p.m. His cousin arrived and posted bond
for Wright sometime between 11:00 p.m. and midnight. However, Wright was not then released.
Instead, after Wright posted bond, an officer told him that he had to be taken downtown to
undergo a body scan to see if he was hiding drugs in his body.

       At approximately 1:00 a.m., Wright was transferred from the Euclid City Jail to the
downtown Cuyahoga County Jail. When he arrived at this next facility, the staff asked him if he
had ingested any drugs or was hiding any drugs in his body. The jail staff informed him that his
bond had been paid, and he would be released once they had performed a body scan. County jail
staff then subjected Wright to a full-body scan.        The scan revealed that Wright was not
sequestering any drugs. Wright was finally released from custody at 3:55 a.m., approximately
four hours after he posted bond, and almost ten hours after Flagg and Williams detained him.

       Under Ohio law, when a defendant posts bail bond, he should be released from custody.
See Ohio Rev. Code § 2713.13 (“The bond, when accepted, shall be returned to the clerk’s
office, and the defendant shall be discharged.”). The approximate four-hour delay in his release
was caused by the designation of his arrest as drug-related. At the time the drug designation
occurred, both Wright and his SUV had been searched, and no drugs or other contraband had
been found. Nor were drugs or other contraband found on him when he was searched (again) by
officials at the jail. He was never charged with any drug-related offense.

       The Fourth Amendment protects “[t]he right of the people to be secure in their
persons . . . against unreasonable searches and seizures.” U.S. Const. amend. IV. As the text
indicates, and the Supreme Court has repeatedly affirmed, “the ultimate touchstone of the Fourth
Amendment is ‘reasonableness.’” Heien v. North Carolina, 574 U.S. 54, 60 (2014) (quoting
Riley v. California, 573 U.S. 373, 381)). Nothing happened from the time that Wright was
detained in his SUV to the time he posted bond to give officers probable cause to believe that
 No. 19-3452                        Wright v. City of Euclid, et al.                       Page 25


Wright was hiding drugs in his body. Despite the officers’ having no information that would
give them probable cause, Wright was seized for four hours after he should have been free to go.
A jury could find that this detention violated Wright’s right to be free from unreasonable
seizures.

         2.      Clearly Established Right

         Because the extended-detention claim, in essence, is derivative of Wright’s false-arrest
claim, the law was likewise clearly established that officers could not seize him without probable
cause.      As we stated above, the right to be free from arrest without probable cause is a
“quintessential example[] of [a] ‘clearly established’ constitutional right.” Jones, 947 F.3d at
915. Wright has presented sufficient evidence for a reasonable jury to find no probable cause—
and no qualified immunity—for the extended detention. Therefore, we REVERSE the district
court’s grant of summary judgment on Wright’s extended-detention claim.

E.       Fourth-Amendment Malicious Prosecution

         Wright next argues that the district court erred in granting summary judgment on his
claim of malicious prosecution in violation of the Fourth Amendment.             The Sixth Circuit
“recognizes a separate constitutionally cognizable claim of malicious prosecution under the
Fourth Amendment, which encompasses wrongful investigation, prosecution, conviction, and
incarceration.” Sykes v. Anderson, 625 F.3d 294, 308 (6th Cir. 2010) (cleaned up) (quoting
Barnes v. Wright, 449 F.3d 709, 715–16 (6th Cir. 2006)).

         To succeed on this claim, Wright must prove four things: (1) that a criminal prosecution
was initiated against him and that the defendant “made, influenced, or participated in the
decision to prosecute,” id. (alterations omitted) (quoting Fox v. Desoto, 489 F.3d 227, 237 (6th
Cir. 2007)); (2) that there was a lack of probable cause for the criminal prosecution; (3) that, as a
consequence of a legal proceeding, he suffered a deprivation of liberty apart from the initial
seizure; and (4) that the criminal proceeding was resolved in his favor, id. at 308–09; see also
Fox, 489 F.3d at 237.
 No. 19-3452                        Wright v. City of Euclid, et al.                      Page 26


          1.     The Officer Influenced or Participated in the Decision to Prosecute

          At minimum, “whether an officer influenced or participated in the decision to prosecute
hinges on the degree of the officer’s involvement and the nature of the officer’s actions.” Sykes,
625 F.3d at 311 n. 9; see Malley v. Briggs, 475 U.S. 335, 344–45 n. 7 (1986) (internal quotation
omitted) (construing § 1983 “against the background of tort liability,” in which people are
responsible for the “natural consequences” of their acts).

          Although Wright need not show that the officers influenced or participated with malice,
“there must be some element of blameworthiness or culpability in the participation,” that is,
“truthful participation in the prosecution is not actionable.” Johnson v. Moseley, 790 F.3d 649,
655 (6th Cir. 2015) (citing Sykes, 625 F.3d at 314). The most clear-cut way for a plaintiff to
satisfy this prong is to show that the officer gave false testimony before a grand jury. See Webb
v. United States, 789 F.3d 647, 663 (6th Cir. 2015). But an officer can also influence or
participate in the decision to prosecute by falsely prompting or urging a prosecutor’s decision to
bring charges in the first place. See id. at 666.

          Wright maintains that because Flagg conceded in his deposition that “by signing the
tickets he initiated prosecution against Lamar Wright,” the first prong of his malicious
prosecution claim is met. The “tickets,” or “traffic citations” as Flagg called them, were the
official citations that appear to have been filed in Euclid Municipal Court that charged Wright
with traffic violations, resisting arrest, obstructing official business, and criminal trespass. The
district court noted that Wright “makes general allegations that the officers fabricated evidence,
but points to no evidence of fabrication or falsification.” Wright, 2019 WL 2009453, at *9.
However, because the officers designated Wright’s arrest to be the result of a drug investigation,
despite knowing that Wright had no drugs when he was arrested and he was not arrested for any
drug-related offenses, a reasonable juror could find that Flagg and Williams engaged in
misrepresentation such that they were culpable in their involvement with Wright’s prosecution.
Cf. Jones, 947 F.3d at 918–19 (holding that filing a narrative report that falsely accuses a
defendant of resisting arrest establishes sufficient culpability for a federal malicious prosecution
claim).
 No. 19-3452                        Wright v. City of Euclid, et al.                       Page 27


       At the time of the designation, the officers knew two things of which they were unaware
when they pulled Wright over. First, they knew that Wright had a serious medical condition that
prevented him from exiting the vehicle. Second, they knew that Wright was not possessing any
drugs when they arrested him. These facts are sufficient for a reasonable juror to find the
officers made a false statement that Wright’s arrest was drug related, thereby establishing their
requisite involvement in his prosecution for a claim that it was malicious.

       2.      Lack of Probable Cause for the Prosecution

       For the same reasons set forth above regarding Wright’s false-arrest claim, a reasonable
jury could likewise find that there was a lack of probable cause to prosecute Wright.

       3.      Deprivation of Liberty

       We have recognized that an “initial arrest alone is an insufficient deprivation of liberty”
to support a claim for malicious prosecution. Noonan v. Cty. of Oakland, 683 F. App’x 455, 463
(6th Cir. 2017). Something more is required, and this circuit has held that “service with a
summons to appear at trial or some other court proceeding does not rise to the level of a
constitutional deprivation.” Id. at 463 (internal quotation marks and citation omitted).

       Wright argues that he suffered a deprivation of liberty beyond the initial seizure because
he was confined in the jail and in the hospital for many hours after the initial seizure but before
being released. That is enough to present a jury question under our caselaw. In Miller v.
Maddox, the plaintiff had suffered a deprivation of liberty apart from the initial seizure when she
remained detained for an extra forty-five minutes, paid a fee to be released, and was required to
participate in a pretrial release program. 866 F.3d 386, 393 (6th Cir. 2017).

       Here, Wright was booked into the Euclid jail at around 10:49 p.m., and he posted a
$905.00 bond between 11:00 p.m. and midnight. After he posted bond, Wright was not allowed
to leave. Rather, he was transported to the Cuyahoga County jail at around 1:00 a.m. He was
then required to undergo a full body scan as a result of the “drug investigation” that was noted on
his record. Wright was finally released at approximately 3:55 a.m. These facts would allow a
reasonable jury to find that Wright suffered a deprivation of liberty beyond the initial seizure.
 No. 19-3452                        Wright v. City of Euclid, et al.                      Page 28


       4.      Criminal Proceeding Resolved in his Favor

       The district court did not explicitly address this element of the action, but it is obviously
satisfied. The prosecution was terminated in Wright’s favor when the prosecutor dropped all
charges against him. See Ash v. Ash, 651 N.E.2d 945, 947–48 (Ohio 1995) (“[A]n unconditional,
unilateral dismissal of criminal charges or an abandonment of a prosecution by the prosecutor or
the complaining witness that results in the discharge of the accused generally constitutes a
termination in favor of the accused.”).

                                               * * * * *

       The right to be free from malicious prosecution is clearly established, but “the right is a
narrow one.” Coffey, 933 F.3d at 590 (citing Johnson, 790 F.3d at 649). “A police officer
violates a suspect’s clearly established right to freedom from malicious prosecution under the
Fourth Amendment ‘only when his deliberate or reckless falsehood results in arrest and
prosecution without probable cause.’” Johnson, 790 F.3d at 655 (quoting Newman v. Twp. of
Hamburg, 773 F.3d 769, 772 (6th Cir. 2014)). The officers’ designation of Wright’s arrest as
drug-related, given their knowledge of the circumstances of his arrest, including his medical
condition, is sufficient proof for a reasonable jury to find that the officers engaged in at least
reckless falsehood that resulted in his wrongful detention and intrusive search. Because Wright
has produced enough evidence such that a jury could find in his favor on the federal malicious-
prosecution claim, we REVERSE the district court’s grant of qualified immunity on this count.

F.     State-Law Claims

       In addition to his claims brought under § 1983, Wright brought state-law claims,
including malicious prosecution and intentional infliction of emotional distress. The district
court held that the officers were entitled to immunity under the Ohio statute that grants immunity
to municipal employees acting within the scope of their employment. For the reasons that
follow, we disagree with the district court.
 No. 19-3452                       Wright v. City of Euclid, et al.                     Page 29


       1.      State-Law Immunity

       The district court granted summary judgment to the officers and the City on Wright’s
state-law claims based on Ohio statutory immunity. Ohio Revised Code Chapter 2744 grants
immunity to political subdivisions and to employees of political subdivisions for actions arising
within the course or scope of their employment. The City is immune from suit for damages
unless one of several exceptions applies. Wright has not presented an argument as to why the
City should be liable for his state-law claims, so this argument is forfeited. See McPherson v.
Kelsey, 125 F.3d 989, 995 (6th Cir. 1997) (“[I]ssues adverted to in a perfunctory manner,
unaccompanied by some effort at developed argumentation, are deemed waived. It is not
sufficient for a party to mention a possible argument in the most skeletal way, leaving the court
to . . . put flesh on its bones.” (quoting Citizens Awareness Network, Inc. v. United States
Nuclear Regulatory Comm’n, 59 F.3d 284, 293–94 (1st Cir. 1995))).

       As to Flagg and Williams, Ohio law grants immunity from civil suits to employees of
political subdivisions unless:

       (a) the employee’s acts or omissions were manifestly outside the scope of their
           employment or official responsibilities;
       (b) the employee’s acts or omissions were with malicious purpose, in bad faith, or in a
           wanton or reckless manner; [or]
       (c) civil liability is expressly imposed by a section of the Revised Code.

Ohio Rev. Code § 2744.03(A)(6)(a)–(c). Because the officers’ conduct was within the scope of
their employment and because civil liability is not expressly imposed by another section of the
Ohio Revised Code, Wright must show that their acts were “with malicious purpose, in bad faith,
or in a wanton or reckless manner.” Id. § 2744.03(A)(6)(b).

       “When federal qualified immunity and Ohio state-law immunity under [Ohio Rev. Code]
§ 2744.03(A)(6) rest on the same questions of material fact, we may review the state-law
immunity defense ‘through the lens of federal qualified immunity analysis.’” Hopper v.
Plummer, 887 F.3d 744, 759 (6th Cir. 2018) (quoting Chappell v. City of Cleveland, 585 F.3d
901, 907 n.1 (6th Cir. 2009)). The officers’ state-law statutory-immunity defense therefore
“stands or falls with their federal qualified immunity defense.” Id. at 760; cf. Martin v. City of
 No. 19-3452                       Wright v. City of Euclid, et al.                     Page 30


Broadview Heights, 712 F.3d 951, 963 (6th Cir. 2013) (holding that “[a]s resolution of the state-
law immunity issue is heavily dependent on the same disputed material facts as the excessive
force determination under § 1983, the district court properly denied summary judgment to the
officers on the estate’s state-law claims”). For the reasons discussed above regarding qualified
immunity, we hold that the district court erred in granting statutory immunity to Flagg and
Williams.

       2.      State-Law Malicious Prosecution

       To sustain an action for malicious prosecution under Ohio law, Wright must establish:
(1) malice in instituting or continuing the prosecution; (2) lack of probable cause; and
(3) termination of the prosecution in his favor. Ash v. Ash, 651 N.E.2d 945, 947 (Ohio 1995).
Unlike Wright’s federal malicious-prosecution claim, his Ohio state law claim requires a
showing of malice. “Ohio law defines ‘malice’ as ‘an improper purpose, or any purpose other
than the legitimate interest of bringing an offender to justice.’” Harris v. Bornhorst, 513 F.3d
503, 521 (6th Cir. 2008) (quoting Criss v. Springfield Twp., 564 N.E.2d 440, 443 (Ohio 1990));
accord, e.g., Harris v. United States, 422 F.3d 322, 327 (6th Cir. 2005). Moreover, under Ohio
law, the absence of probable cause to seize a person raises an inference of malice. See, e.g.,
Melanowski v. Judy, 131 N.E. 360, 361 (Ohio 1921) (“If want of probable cause be proven, the
legal inference may be drawn that the proceedings were actuated by malice.”); Criss, 564 N.E.2d
at 443 (“If the basis for prosecution cannot be shown, those who made the decision will appear to
have acted with no basis—that is maliciously.”); accord, e.g., Bornhorst, 513 F.3d at 521;
Thacker v. City of Columbus, 328 F.3d 244, 261 (6th Cir. 2003).

       As explained above, Wright has demonstrated a genuine factual dispute as to whether
Officers Flagg and Williams lacked probable cause to arrest him. He has also demonstrated a
triable issue regarding whether Officers Flagg and Williams wrongfully, and perhaps even
willfully, designated his arrest as stemming from a drug investigation in order to detain him,
cause him to undergo a full body scan, and potentially justify their past actions. Under our case
law, this constitutes an “improper purpose” sufficient to overcome Defendants’ motion for
summary judgment. See, e.g., Jones, 947 F.3d at 921 (holding that “a reasonable jury could infer
malice on behalf of all three officers” where “the jury could find that all three officers lied in
 No. 19-3452                       Wright v. City of Euclid, et al.                       Page 31


ways that were material to the eventual decision to prosecute Jones, for the purpose of justifying
their own prior actions”).

       Therefore, we REVERSE the district court’s grant of summary judgment on the state law
malicious prosecution claim.

       3.      Intentional Infliction of Emotional Distress

       Though Wright dedicates some portion of his briefing to arguing that the district court
erred in granting summary judgment to the officers on his intentional-infliction-of-emotional-
distress claim, his argument is little more than a bare recitation of the elements of the cause of
action, and for that reason is forfeited. See United States v. Fowler, 819 F.3d 298, 309 (6th Cir.
2016) (“It is not sufficient for a party to mention a possible argument in [a] skeletal way, leaving
the court to put flesh on its bones.” (quoting El-Moussa v. Holder, 569 F.3d 250, 257 (6th Cir.
2009)). We therefore we AFFIRM the district court’s grant of summary judgment on this claim.

G.     Municipal Liability under 42 U.S.C. § 1983

       We now reach Wright’s Monell claim. Wright argues that the City is liable under § 1983
for its inadequate policy on use of force by police; ratification of use of excessive force by the
chief of police; failure to adequately train or supervise its officers on use of force; and a custom
of tolerance or inaction towards excessive force. The district court granted the City summary
judgment on this claim for want of a constitutional violation.

       The § 1983 cause of action may be exercised only against a “person who . . . causes to be
subjected, any citizen of the United States or other person within the jurisdiction thereof to the
deprivation of any rights, privileges, or immunities secured by the Constitution and laws.” 42
U.S.C. § 1983. Although “person” has been given a wide meaning under § 1983, Monell v.
Dep’t of Soc. Servs., 436 U.S. 658, 690 (1978), when the person is a municipality, liability
attaches only under a narrow set of circumstances. “A municipality may not be held liable under
§ 1983 on a respondeat superior theory—in other words, ‘solely because it employs a
tortfeasor.’” D’Ambrosio v. Marino, 747 F.3d 378, 388–89 (6th Cir. 2014) (quoting Monell,
436 U.S. at 691).    Instead, a plaintiff must show that “through its deliberate conduct, the
 No. 19-3452                        Wright v. City of Euclid, et al.                        Page 32


municipality was the ‘moving force’ behind the injury alleged.” Alman v. Reed, 703 F.3d 887,
903 (6th Cir. 2013) (quoting Bd. of Cty. Comm’rs v. Brown, 520 U.S. 397, 404 (1997)).
A plaintiff does this by showing that the municipality had a “policy or custom” that caused the
violation of his rights. Monell, 436 U.S. at 694.

       There are four methods of proving a municipality’s illegal policy or custom: the plaintiff
may prove “(1) the existence of an illegal official policy or legislative enactment; (2) that an
official with final decision making authority ratified illegal actions; (3) the existence of a policy
of inadequate training or supervision; or (4) the existence of a custom of tolerance or
acquiescence of federal rights violations.” Jackson v. City of Cleveland, 925 F.3d 793, 828 (6th
Cir. 2019) (citing Burgess, 735 F.3d at 478). Wright argues that he can establish municipal
liability under three of the four methods: (1) a custom of tolerance or acquiescence of federal
rights violations; (2) inadequate training and supervision; and (3) ratification of illegal actions by
an official with final decision-making authority.

       1.      Illegal Official Policy

       “[T]o satisfy the Monell requirements a plaintiff must identify the policy, connect the
policy to the city itself, and show that the particular injury was incurred because of the execution
of that policy.” Jackson, 925 F.3d at 829 (internal quotation omitted). Wright argues that the
Euclid Police Department has a custom of permitting or acquiescing to the use of excessive
force, which directly caused his injury. “[A] city may be liable under Monell for a policy of
permitting constitutional violations regardless of whether the policy is written.” Id. at 830; see
Monell, 436 U.S. at 691 (“Congress included customs and usages [in § 1983] . . . . Although not
authorized by written law, such practices . . . could well be so permanent and well settled as to
constitute a ‘custom or usage’ with the force of law.” (quoting Adickes v. S.H. Kress & Co., 398
U.S. 144, 167–68 (1970))). When proceeding under the first theory of Monell liability, Wright
must show that there were “formal rules or understandings—often but not always committed to
writing—that [were] intended to, and [did], establish fixed plans of action to be followed under
similar circumstances consistently and over time.” Pembaur v. City of Cincinnati, 475 U.S. 469,
480–81 (1986).
 No. 19-3452                       Wright v. City of Euclid, et al.                      Page 33


       Wright points to the Euclid Police department training on use of force to support his
argument that the City has a custom of allowing excessive force. First, there is the link in the
training materials to the YouTube video of the Chris Rock comedy sketch discussed earlier. As
noted, it is entitled “How not to get your ass kicked by the police!”. It includes numerous
vignettes depicting police officers beating African-American suspects, with commentary from
Rock about Rodney King and other matters as also described earlier.

       The evidence further includes, as also noted, a slide from the same training titled
“Defensive Tactics Training.” The slide includes a cartoon in which a stick figure police officer
in riot gear is shown beating a prone and unarmed civilian with a club with the caption
“protecting and serving the poop out of you.” R. 23 at PageID 808. Again, as noted, Murowsky
testified that he did not believe that the image conveys that the Euclid Police Department
“beat[s] the hell out of people,” R. 25 at PageID 1200, but that he didn’t know what other
message could possibly be taken away from the image.

       Finally, the use-of-force training contains a meme that depicts two officers with their
guns drawn and aimed at something.         It is captioned “Bed bug! Bed bug on my shoe!”.
Murowsky testified that he believed the image conveyed that the officers were overreacting to
and escalating a situation.

       Wright has produced enough evidence such that a reasonable jury could find that the
City’s custom surrounding use of force is so settled so as to have the force of law and that it was
the moving force behind violations of Wright’s constitutional rights. We therefore REVERSE
the district court’s grant of summary judgment on the issue of municipal liability under § 1983.

       2.      Failure to Train or Supervise

       “When determining whether a municipality has adequately trained its employees, ‘the
focus must be on adequacy of the training program in relation to the tasks the particular officers
must perform.” Jackson, 925 F.3d at 834 (quoting City of Canton v. Harris, 489 U.S. 378, 390
(1989)). A failure-to-supervise claim requires a showing of “prior instances of unconstitutional
conduct demonstrating that the municipality had ignored a history of abuse and was clearly on
 No. 19-3452                              Wright v. City of Euclid, et al.                                  Page 34


notice that the training in this particular area was deficient and likely to cause injury.” Burgess,
735 F.3d at 478.

         It is undisputed that Euclid police officers received some form of training on the proper
use of force, but a reasonable juror could find that this training is deficient. The Euclid Police
Department’s training policy and procedures mandate that “[t]he department will establish and
maintain a training committee.” However, no such training committee apparently has ever
existed.

         The City’s training seems to consist initially of simply reading the use-of-force policy to
the officers at rollcall until “it is believed that all the officers have heard it,” R. 31-7 at PageID
1508, which is then followed up with a one-or-two-page quiz that may or may not be given to
officers. The City also engages in some sort of practical training exercise in which officers are
given scenarios in which they may use force. But according to Murowsky, who implemented
these scenario-based trainings, the scenarios never changed, and the officers’ performances were
never evaluated.        And recall that this training also included the graphic and comedy skit
discussed above.1

         A reasonable jury could find that the City’s excessive-force training regimen and
practices gave rise to a culture that encouraged, permitted, or acquiesced to the use of
unconstitutional excessive force, and that, as a result, such force was used on Wright. Therefore,
we REVERSE the district court’s grant of summary judgment on Wright’s Monell claim based
on failure to train or supervise. See Jackson, 925 F.3d at 836–37 (holding that a single instance
of unconstitutional conduct can give rise to a failure-to-train claim when the natural consequence
of the municipality’s training regimen is that officials will violate constitutional rights); accord
Canton, 489 U.S. at 390 (“[I]t may happen that in the light of the duties assigned to specific
officers or employees the need for more or different training is so obvious . . . that the



         1
          Wright directs our attention to three other instances of police force by Euclid police officers to support the
notion that the police department “has a track record of excessive force and ongoing failure to take seriously the
need to properly . . . train officers on use of force.” Appellant’s Br. at 66. Those three instances of use of force,
while certainly troubling in their own right, cannot establish that the Euclid Police Department had a track record of
excessive force at the time of Wright’s constitutional injury because they all occurred after the incident with Wright.
 No. 19-3452                        Wright v. City of Euclid, et al.                      Page 35


policymakers of the city can reasonably be said to have been deliberately indifferent to the
need.”).

       3.       Ratification by Decision-Maker

       Wright argues that Chief Meyer’s failure to investigate numerous claims of excessive
force amounts to ratification of unconstitutional acts by a final decision-maker. A plaintiff can
establish municipal liability by showing that the municipality ratifies the unconstitutional acts of
its employees by failing to meaningfully investigate and punish allegations of unconstitutional
conduct. Leach v. Shelby Cty. Sheriff, 891 F.2d 1241, 1247–48 (6th Cir. 1990). Wright points us
to Chief Meyer’s lack of investigation and discipline in the other high-profile use-of-force cases
involving Euclid police officers, but those instances occurred after Wright’s encounter with
Flagg and Williams and cannot show that Meyer’s failure to investigate and punish the officers
involved in those uses of force led in any way to Wright’s injuries. However, Murowsky
testified that he had never heard of a use of force incident by a Euclid officer that seemed
inappropriate to him. That too moves the needle so that a reasonable jury could decide that use
of excessive force is ratified by the department. A reasonable jury could likewise find that
Meyer and Murowsky’s seeming failure to ever meaningfully investigate excessive force
complaints rises to the level of a ratification of use of force by a policymaker.

                                                  IV.

       It is very troubling that the City of Euclid’s law-enforcement training included jokes
about Rodney King—who was tased and beaten in one of the most infamous police encounters in
history—and a cartoon with a message that twists the mission of police. The offensive statements
and depictions in the training contradict the ethical duty of law enforcement officer “to serve the
community; to safeguard lives and property; to protect the innocent against deception, the weak
against oppression or intimidation and the peaceful against violence or disorder; and to respect
the constitutional rights of all to liberty, equality, and justice.” Law Enforcement Code of Ethics,
International   Association    of   Chiefs   of    Police,   https://www.theiacp.org/resources/law-
enforcement-code-of-ethics.
 No. 19-3452                      Wright v. City of Euclid, et al.                     Page 36


       There is enough evidence to present jury questions that preclude summary judgment on
the Monell claims under 42 U.S.C. § 1983. Likewise, the evidence regarding Wright’s encounter
with the police present jury questions that preclude summary judgment on the excessive-force,
false-arrest, extended-detention, and federal malicious-prosecution claims under § 1983 as well.
Accordingly, for the reasons stated above, we AFFIRM in part, REVERSE in part, and
REMAND to the district court for further proceedings.

```

---
