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

## GROUP: content/cases/Winston v. Lee.md  (`case`, 5 assertions)

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
{"assertion_id": "c6a3b59b0409454b", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "470 U.S. 753 (1985)", "court": "U.S. Supreme Court", "neutral_cite": "1985 U.S. LEXIS 76", "official_citation_present": true, "parallel_cite": "105 S. Ct. 1611; 84 L. Ed. 2d 662; 53 U.S.L.W. 4367", "title": "Winston v. Lee", "year": "1985"}}
{"assertion_id": "64bb05bf13118865", "dimension": "support", "kind": "home_role", "locator": {"home": "Scope Manner and Related Issues"}, "payload": {"home": "Scope Manner and Related Issues", "role": "Limiting", "title": "Winston v. Lee"}}
{"assertion_id": "a71eac5e882c1b50", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Court-ordered surgery under general anesthesia to recover a bullet for use as evidence is an unreasonable search where, under the Schmerber balance, the severe intrusion on bodily integrity and safety outweighs the State's need for the evidence — even with probable cause and a judicial order.", "title": "Winston v. Lee"}}
{"assertion_id": "207a6a0eb3d47ce1", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Winston v. Lee"}}
{"assertion_id": "51db8ea1094c6d28", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1985-03-20", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Winston v. Lee", "field_i_validity": "good_law", "scope_note": "Controlling: a compelled surgical intrusion into the body for evidence may be unreasonable even with probable cause and a court order; reasonableness turns on the Schmerber balance of intrusion against need.", "title": "Winston v. Lee", "varies_by_point": "false"}}
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

## GROUP: content/cases/Wyman v. James.md  (`case`, 5 assertions)

### content_page

```
---
title: Wyman v. James
type: case
citation: "400 U.S. 309 (1971)"
parallel_cite: "91 S. Ct. 381; 27 L. Ed. 2d 408"
neutral_cite: 1971 U.S. LEXIS 106
court: U.S.
court_level: scotus
circuit: ""
year: 1971
date_decided: 1971-01-12
docket: 69
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
  opinion_url: "https://www.courtlistener.com/opinion/108223/wyman-v-james/"
  cluster_id: 108223
  opinion_id: 9424375
  identity_checked: true
lake:
  record_id: Wyman v. James
  status: under_review
  projected_at: 2026-07-09
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: Key
related:
  - "[[Special Needs and Administrative Searches]]"
  - "[[Camara v. Municipal Court]]"
tags:
  - case
  - special-needs
  - administrative-search
  - welfare-home-visit
  - fourth-amendment
holding: "A mandatory home visit by a welfare caseworker, imposed as a condition of continued AFDC benefits, is not a Fourth Amendment search in the criminal-investigative sense and is in any event reasonable; a beneficiary who refuses the visit forfeits benefits but incurs no criminal penalty."
---

# Wyman v. James

*400 U.S. 309 (1971)* (No. 69) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 108223 → lead opinion 108223; quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Barbara James, a beneficiary of Aid to Families with Dependent Children (AFDC) in New York, refused to permit a scheduled home visit by her caseworker, and her benefits were terminated for that refusal. She sued, contending that requiring her to admit a caseworker into her home on pain of losing benefits was an unreasonable search barred by the Fourth Amendment.

## Issue
Whether conditioning continued welfare benefits on a beneficiary's consent to a caseworker's home visit is an unreasonable search under the Fourth Amendment.

## Rule
The Court held that the caseworker's home visit is not a search in the traditional criminal-law sense, and that even if it has search-like aspects it is reasonable, given the State's paramount interest in the welfare of dependent children and in ensuring that public aid reaches its intended beneficiaries. The visit is not a criminal investigation and carries no criminal consequence: "the visitation in itself is not forced or compelled, and that the beneficiary's denial of permission is not a criminal act. If consent to the visitation is withheld, no visitation takes place. The aid then never begins or merely ceases, as the case may be. ... There is no entry of the home and there is no search." — 400 U.S. at 317–318. ^pin-317

## Application
The home visit was both rehabilitative and, in a limited sense, investigative, but it was not the kind of criminal search the warrant requirement governs. It was preceded by written notice, conducted during business hours without forcible entry or snooping, and the only consequence of refusal was the loss of benefits — not prosecution. Weighed against the State's strong interests in the child's welfare and in the proper administration of public funds, the visitation was a reasonable administrative tool rather than an unreasonable Fourth Amendment intrusion.

## Conclusion
The judgment of the District Court, which had held the home-visit requirement unconstitutional, was **reversed**; the requirement was upheld. Blackmun, J., delivered the opinion of the Court; Douglas, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]]; Marshall, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], joined by Brennan, J.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Wyman* is an early precursor of the special-needs and administrative-search line: it treats a benefits-conditioned home visit as outside the criminal warrant model, upholding it on a reasonableness rationale rather than requiring probable cause or a warrant.

## Appears on
- [[Special Needs and Administrative Searches]] — *Key*

## Sources
- [*Wyman v. James*, 400 U.S. 309 (1971)](https://www.courtlistener.com/opinion/108223/wyman-v-james/) — pinpoint: 317–318 (Opinion of the Court; Blackmun, J.); quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "825f8600f69d3dc2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "400 U.S. 309 (1971)", "court": "U.S.", "neutral_cite": "1971 U.S. LEXIS 106", "official_citation_present": true, "parallel_cite": "91 S. Ct. 381; 27 L. Ed. 2d 408", "title": "Wyman v. James", "year": "1971"}}
{"assertion_id": "150aedb68059fe43", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A mandatory home visit by a welfare caseworker, imposed as a condition of continued AFDC benefits, is not a Fourth Amendment search in the criminal-investigative sense and is in any event reasonable; a beneficiary who refuses the visit forfeits benefits but incurs no criminal penalty.", "title": "Wyman v. James"}}
{"assertion_id": "b731b517e2230c68", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key", "title": "Wyman v. James"}}
{"assertion_id": "5635215c1d5a727a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Wyman v. James"}}
{"assertion_id": "c24c3117d47b3112", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Wyman v. James", "varies_by_point": "false"}}
```

### lake record — Wyman v. James

```json
{
  "schema_version": "s2.v1",
  "record_id": "Wyman v. James",
  "status": "under_review",
  "identity": {
    "case_name": "Wyman v. James",
    "case_name_short": "Wyman",
    "case_name_full": "WYMAN, COMMISSIONER OF NEW YORK DEPARTMENT OF SOCIAL SERVICES, Et Al. v. JAMES",
    "input_case_name": "Wyman v. James",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1971-01-12",
    "year": 1971,
    "docket": "69",
    "cluster_id": 108223,
    "lead_opinion_id": 9424375,
    "sibling_ids": [],
    "absolute_url": "/opinion/108223/wyman-v-james/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "400 U.S. 309",
      "volume": "400",
      "reporter": "U.S.",
      "page": "309",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "91 S. Ct. 381",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "381",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "27 L. Ed. 2d 408",
        "volume": "27",
        "reporter": "L. Ed. 2d",
        "page": "408",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1971 U.S. LEXIS 106",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "106",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "400 U.S. 309",
        "volume": "400",
        "reporter": "U.S.",
        "page": "309",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 S. Ct. 381",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "381",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "27 L. Ed. 2d 408",
        "volume": "27",
        "reporter": "L. Ed. 2d",
        "page": "408",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1971 U.S. LEXIS 106",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "106",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "400 U.S. 309",
    "official_selection": {
      "court_class": "scotus",
      "selected": "400 U.S. 309",
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
    "date_created": "2026-07-07T01:41:07Z",
    "date_modified": "2026-07-09T23:29:56Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:41:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:41:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:41:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:41:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "wyman-v-james--108223",
      "to_record_id": "Wyman v. James",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Wyman v. James

```
<opinion type="majority">
<author id="b412-10">Mr. Justice Blackmun</author>
<p id="ANB">delivered the opinion of the Court.</p>
<p id="b412-11">This appeal presents the. issue whether a beneficiary of the program for Aid to Families with Dependent Children (AFDC)<footnotemark>1</footnotemark> may refuse a home visit by the caseworker without risking the termination, of benefits.</p>
<p id="b413-4"><page-number citation-index="1" label="311">*311</page-number>The New York State and City social services commissioners appeal from a judgment and decree of a divided three-judge District Court holding invalid and unconstitutional in application § 134 of the New York Social Services Law,<footnotemark>2</footnotemark> § 175 of the New York Policies Governing <page-number citation-index="1" label="312">*312</page-number>the Administration of Public Assistance,<footnotemark>3</footnotemark> and §§ 351.10 and 351.21 of Title 18 of the New York Code of Rules and Regulations,<footnotemark>4</footnotemark> and granting injunctive relief. <em>James </em>v. <em>Goldberg, </em><span class="citation" data-id="9660354"><a href="/opinion/1623344/james-v-goldberg/" aria-description="Citation for case: James v. Goldberg">303 F. Supp. 935</a></span> (SDNY 1969). This Court noted probable jurisdiction but, by a divided vote, denied a requested stay. <span class="citation multiple-matches"><a href="/c/U.%20S./397/904/">397 U. S. 904</a></span>.</p>
<p id="b414-5">The District Court majority held that a mother receiving AFDC relief may refuse, without forfeiting her. right to that relief, the periodic home visit which the cited New York statutes and regulations 'prescribe as a condition for the continuance of assistance under the program. The beneficiary’s thesis, and that of the Dis<page-number citation-index="1" label="313">*313</page-number>trict Court majority, is that home visitation is a search and, when not consented to or when not supported by a warrant based on probable cause, violates the beneficiary’s Fourth and Fourteenth Amendment rights.</p>
<p id="b415-5">Judge McLean, in dissent, thought it unrealistic to regard the home visit as a search; felt that the requirement of a search warrant to issue only upon a showing of probable cause would make the AFDC program “in effect another criminal statute” and would “introduce a hostile arm’s length element into the relationship’-’ between worker and mother, “a relationship which can be effective only when it is based upon mutual confidence and trust”; and concluded that the majority’s holding struck “a damaging blow” to an important social welfare program. <span class="citation" data-id="9660354"><a href="/opinion/1623344/james-v-goldberg/#946" aria-description="Citation for case: James v. Goldberg">303 F. Supp., at 946</a></span>.</p>
<p id="b415-6">I</p>
<p id="b415-7">The case comes to us on the pleadings and supporting affidavits and without the benefit of testimony which an extended hearing would have provided. The pertinent facts, however, are not in dispute.</p>
<p id="b415-8">Plaintiff Barbara James is the mother of a son, Maurice, who was born in May 1967. They reside in New York City. Mrs. James first applied for AFDC assistance shortly before Maurice’s birth. A caseworker made a visit to her apartment at that time without objection. The assistance was authorized.</p>
<p id="b415-9">Two years later, on May 8, 1969, a caseworker wrote Mrs. James that she would visit her home on May 14. Upon receipt of this advice, Mrs. James telephoned the worker that, although she was willing to supply information “reasonable and relevant” to her need for public assistance, any discussion was not to take place at her home. The -worker told Mrs. James that she was required by law to visit in her home and that refusal to <page-number citation-index="1" label="314">*314</page-number>permit the visit would result in the termination of assistance. Permission was still denied.</p>
<p id="b416-5">On May 13 the City Department of Social Services sent Mrs. James a notice of intent to discontinue assistance because of the visitation refusal. The notice advised the beneficiary of her right to a hearing before a review officer. The hearing was requested and was held on-May 27. Mrs. James appeared with an attorney at that hearing.<footnotemark>5</footnotemark> They continued, to refuse permission for a worker to visit the James home, but again expressed willingness to cooperate and to permit visits elsewhere. The review officer ruled that the refusal was a proper ground for the termination of assistance. His written decision stated:</p>
<blockquote id="b416-6">“The home visit which Mrs. James refuses to permit is for the purpose of determining if there are any changes in her situation that might affect her . eligibility to continue to receive Public Assistance, or that might affect the amount of such assistance, and to see if there are any social services which the Department of Social Services can provide to the family.”</blockquote>
<p id="b416-7">A notice of termination issued on Juné 2.</p>
<p id="b416-8">Thereupon, without seeking a hearing at the state level, Mrs. James, individually and on behalf of Maurice, and purporting to act on behalf of all other persons similarly situated, instituted the present civil rights suit under <span class="citation no-link">42 U. S. C. § 1983</span>. She alleged the denial of rights guaranteed to her under the First, Third, Fourth, Fifth, Sixth, Ninth, Tenth, and Fourteenth Amendments, and under Subchapters IV and XVI of the Social Security Act and regulations issued thereunder. She further alleged that <page-number citation-index="1" label="315">*315</page-number>she and her son have no income, resources, or support other than the benefits received under the AFDC program. She asked for declaratory and injunctive relief. A temporary restraining order was issued on June 13, <em>James </em>v. <em>Goldberg, </em><span class="citation" data-id="2007222"><a href="/opinion/2007222/james-v-goldberg/" aria-description="Citation for case: James v. Goldberg">302 F. Supp. 478</a></span> (SDNY 1969), and the three-judge District Court was convened.</p>
<p id="b417-5">II</p>
<p id="b417-6">The federal aspects of the AFDC program deserve mention. They are provided for in Subchapter IV, Part A, of the Social Security Act of 1935, <span class="citation no-link">49 Stat. 627</span>, as amended, <span class="citation no-link">42 U. S. C. §§ 601-610</span> (1964 ed. and Supp. V). Section 401 of. the Act, <span class="citation no-link">42 U. S. C. § 601</span> (1964 ed., Supp. V), specifies its purpose, namely, “encouraging the care of dependent children in their own homes or in the homes of relatives by enabling each State to furnish financial assistance and rehabilitation and other services ... to needy dependent children and the parents or relatives with whom they are living to help maintain and strengthen family life <em>. . . </em>The same section authorizes the federal appropriation for payments to States that qualify. Section 402, <span class="citation no-link">42 U. S. C. § 602</span> (1964 ed., Supp. V), provides that a state plan, among other things, must “provide for granting an opportunity for a fair hearing before the State agency to any individual whose claim for aid to families with dependent children is denied or is not acted upon with reasonable promptness”; must “provide that the State agency will make such reports ... as the Secretary [of Health, Education, and Welfare] may from time to time require”; must “provide that the State agency shall, in determining need, take into consideration any other income and resources of any child or relative claiming aid”; and must “provide that where the State agency has reason to believe’ that the home in which a relative and child receiving aid reside is unsuitable for' the child because of the neglect, abuse, or exploitation of <page-number citation-index="1" label="316">*316</page-number>such child it shall bring such condition to the attention of the appropriate court or law enforcement agencies in the State . . . Section 405, <span class="citation no-link">42 U. S. C. § 605</span>, provides that..</p>
<blockquote id="b418-4">“Whenever the State agency has reason to believe that any páyments of aid . . . made with respect to a child are not being or may not be used in the best interests of the child, the State agency may provide for such counseling and guidance services with respect to the use of such payments and the management of other funds by the relative ... in order to assure use of such payments in the best interests, of such child, and may provide for advising such relative that continued failure to so use such payments will result in substitution therefor of protective payments ... or in seeking the appointment of a guardian ... or in. the imposition of criminal or civil penalties . . .. .”</blockquote>
<p id="b418-5">III</p>
<p id="b418-6">When a case involves a home and some type of official intrusion into that home, as this case appears to do, an immediate and natural reaction is one of concern about Fourth Amendment rights and the protection which that Amendment is intended to afford. Its emphasis indeed is upon one of the most precious aspects of personal security in the home: “The right of the people to be secure in their persons, houses, papers, and effects ; . . .” This Court has characterized that right as “basic to a free society.” <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span> (1949); <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span> (1967). And over the years the Court consistently has been most protective of the privacy of the dwelling. See, for example, <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#626" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 626-630</a></span> <em>(1886); Mapp v. Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961); <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969); <em>Vale </em>v. <em>Louisiana, </em><span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/" aria-description="Citation for case: Vale v. Louisiana">399 <page-number citation-index="1" label="317">*317</page-number>U. S. 30</a></span> (1970). In <em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span> </em>Mr. Justice White, after noting that the “translation of the abstract prohibition against 'unreasonable searches and seizures’ into workable guidelines, for the decision of particular cases is a difficult task,” went on to observe,</p>
<blockquote id="b419-5">“Nevertheless, one governing principle, justified by history and by current experience, has consistently been followed: except in certain carefully defined classes of cases, a search of private property without proper consent is 'unreasonable’ unless it has been authorized by a valid search warrant.” <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 528-529</a></span>.</blockquote>
<p id="b419-6">He pointed out, too, that one’s Fourth Amendment protection sübsists apart from his being suspected of criminal behavior. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#530" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 530</a></span>.</p>
<p id="b419-7">IV</p>
<p id="b419-8">This natural and quite proper protective attitude, however, is not a factor in this case, for the seemingly obvious and simple reason that we. are not concerned here with any search by the New York social service agency in the Fourth Amendment meaning of that term. It is true that the governing statute and regulations appear to make mandatory the initial home visit and the subsequent periodic “contacts” (which may include home visits) for the inception and continuance of aid. It is also true that the caseworker’s posture in the home visit is perhaps, in a sense, both rehabilitative and investigative. But this latter aspect, we think, is given too broad a character and far more emphasis than it deserves if it is equated with a search in the traditional criminal law context. We note, too, that the visitation in itself is not forced or compelled, and .that the bene-Sciary’s denial of permission is not a criminal act. If iorisent to the visitation is withheld, no visitation takes <page-number citation-index="1" label="318">*318</page-number>place. The aid then never begins or merely ceases, as the case may be. There is no entry of the home and there is no search.</p>
<p id="b420-5">V</p>
<p id="b420-6">If however, we were to assume that a caseworker’s home visit, before or subsequent to the beneficiary’s initial qualification for. benefits, somehow (perhaps because the average beneficiary might feel she is in no position to refuse consent to the visit), and despite its interview nature, does possess some of the characteristics of a search in the traditional sense, we nevertheless conclude that the visit does not fall within the Fourth Amendment’s proscription. This is because it does not descend to the level of unreasonableness. It is unreasonableness which is the Fourth Amendment’s standard. <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#9" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 9</a></span> (1968); <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#222" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 222</a></span> (1960). And Mr. Chief Justice Warren observed in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>that “the specific content and incidents of this, right must be shaped by the context in which it is asserted.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#9" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 9</a></span>.</p>
<p id="b420-7">There are a number of factors that compel us to conclude that the home visit proposed for Mrs. James is not unreasonable:</p>
<p id="b420-8">1. The public’s interest in .this particular segment of the area of assistance to the unfortunate is protection and aid for the dependent child whose family requires such aid for that child.. The focus is on the <em>child </em>and, further, it is on the child who is <em>dependent. </em>There is no more worthy object of the public’s concern. The dependent . child’s. needs are paramount, and only with hesitancy would we relegate those needs, in the scale of comparative values, to a position secondary to what the . mother claims as her rights.</p>
<p id="b420-9">2. The agency, with tax funds provided from federal as well as from state sources, is fulfilling a public trust. The State, working through its qualified welfare agency, <page-number citation-index="1" label="319">*319</page-number>has appropriate and paramount interest and concern in seeing and assuring that the intended and proper objects of that tax-produced assistance are the ones who benefit; from the aid it dispenses. . Surely it is not unreasonable, in the Fourth Amendment sense or in any other sense of that term, that the State have at its command a gentle means, of limited extent and of practical and. considerate application, of achieving that, assurance.</p>
<p id="b421-5">3. One who dispenses purely private charity naturally has an interest in and expects to know how his charitable funds are utilized and put to work. The public, when it is the provider, rightly expects the same. It might well expect more, because of the trust aspect of public funds, and the recipient, as well as the caseworker,, has not only an interest but an obligation.</p>
<p id="b421-6">4. The emphasis of the New York statutes and regulations is upon the home, upon “close contact” with the beneficiary, upon restoring the aid recipient “to a condition of self-support,” and upon the relief of his distress. The. federal emphasis is no different. It is upon “assistance and rehabilitation,” upon maintaining and strengthening family life, and upon “maximum self-support and personál independence consistent with the maintenance of continuing parental care and protection . . . .” <span class="citation no-link">42 U. S. C. §601</span> (1964 ed., Supp. V); <em>Dandridge </em>v. <em>Williams, </em><span class="citation" data-id="9424234"><a href="/opinion/108115/dandridge-v-williams/#479" aria-description="Citation for case: Dandridge v. Williams">397 U. S. 471, 479</a></span> (1970), and <span class="citation" data-id="9424234"><a href="/opinion/108115/dandridge-v-williams/#510" aria-description="Citation for case: Dandridge v. Williams"><em>id., </em>at 510</a></span> (Marshall, J., dissenting). It requires cooperation from the state agency upon specified standards and in specified ways. And it is concerned about any possible exploitation of the child.</p>
<p id="b421-7">5. The home visit, it is true, is not required by federal statute or regulation.<footnotemark>6</footnotemark> But it has been noted that the <page-number citation-index="1" label="320">*320</page-number>visit is “the heart of welfare administration”; that it affords “a personal, rehabilitative orientation, unlike that. of most federal programs”; and that the “more pronounced service orientation” effected by Congress with the 1956 amendments to the Social Security Act “gave redoubled importance to the practice of home visiting.” Note, Rehabilitation, Investigation and the Welfare Home Visit, 79 Yale L. J. 746, 748 (1970). The home visit is an established routine in States besides New York.<footnotemark>7</footnotemark></p>
<p id="b422-5">6. The means employed by the New York agency are significant. Mrs. James received written notice several days in advance of the intended home visit.<footnotemark>8</footnotemark> The date <page-number citation-index="1" label="321">*321</page-number>was specified. Section 134-a of the New York Social Services Law, effective April 1, 1967, and set forth, in n. 2, <em>supra, </em>sets the tone. Privacy is emphasized. The applicant-recipient is made the primary source of information as to eligibility. Outside informational sources, other than public records, aré to be consulted only with the beneficiary’s consent. Forcible entry or entry under false pretenses or visitation outside working hours or snooping in the home are forbidden. HEW Handbook of Public Assistance Administration, pt. IV, §§ 2200 (a) and 2300; 18 NYCRR §§351.1, 351.6, and 351.7. All this minimizes any “burden” upon the homeownér’s right against unreasonable intrusion.</p>
<p id="b423-5">7. Mrs. James, in fact, on this record presents no specific complaint of any unreasonable intrusion of her home and nothing that supports an inference that the desired home visit had as its purpose the obtaining of information as to criminal activity. She complains of no proposed visitation at an awkward or retirement hour. She suggests no forcible entry. She refers to no snooping. She describes no impolite or reprehensible conduct of any kind. She alleges only, in general and nonspecific terms, that on previous visits and, on information and belief, on visitation at the home of other aid recipients, “questions concerning personal relationships, beliefs and behavior are raised and pressed which are unnecessary for a determination of continuing eligibility.” Paradoxically, this same complaint could be. made of a conference held elsewhere than in the home, and yet this is what is sought by Mrs. James. The same complaint could be made of the census taker’s questions. See Me. Justice Makshall’s opinion, as United States Circuit Judge, in <em>United States </em>v. <em>Rickenbacker, </em><span class="citation" data-id="258604"><a href="/opinion/258604/united-states-v-william-f-rickenbacker/" aria-description="Citation for case: United States v. William F. Rickenbacker">309 F. 2d 462</a></span> (CA2 1962), cert. denied, 371 U. S, 962. What Mrs. James appears to want from the agency that provides her and her infant son with the necessities for life is the right to receive those necessities upon her own <page-number citation-index="1" label="322">*322</page-number>informational terms, to utilize the Fourth Amendment as a wedge for imposing those terms, and to avoid questions of any kind.<footnotemark>9</footnotemark></p>
<p id="b424-5">8. We are not persuaded, as Mrs.- James would have us be, that all information pertinent to the issue of eligibility can be obtained by the agency through an interview at a place other than the home, or, as the District Court majority suggested, by examining a lease or a birth certificate, or . by periodic medical examinations, or by interviews with school personnel. <span class="citation" data-id="9660354"><a href="/opinion/1623344/james-v-goldberg/#943" aria-description="Citation for case: James v. Goldberg">303 F. Supp., at 943</a></span>. Although these secondary sources might be helpful, they would not always assure verification of actual residence or-of actual physical presence in the home, which are requisites for AFDC benefits,<footnotemark>10</footnotemark> or of impending medical needs. And, of course, little children, such as Maurice James, are not yet registered in school.</p>
<p id="b424-6">9. The visit is not one by police or uniformed authorrity. It is made by "a caseworker of some training<footnotemark>11</footnotemark> whose <page-number citation-index="1" label="323">*323</page-number>primary objective is, or should be, the welfare, not the prosecution, of the aid recipient for whom the worker has profound responsibility. As has already been stressed, the program concerns dependent children and the. needy families of those children. It does not deal with crime or with the actual or suspected perpetrators of crime. The caseworker is not a sleuth but rather, we trust, is a friend to one in need.</p>
<p id="b425-5">10. The home visit is not a criminal investigation, does not equate with a criminal investigation, and despite the announced fears of Mrs. James and those who would join her, is not in aid of any criminal proceeding. If the visitation serves to discourage misrepresentation or fraud, such a byproduct of that visit does not impress upon the visit itself a dominant criminal investigative aspect. And if the visit should, by chance, lead to the discovery of fraud and a criminal prosecution should follow,<footnotemark>12</footnotemark> then, even assuming that the evidence discovered upon the home visitation is admissible, an issue upon which we express no opinion, that is a routine and expected fact of life and a consequence no greater than that which necessarily ensues upon any other discovery by a citizen of criminal conduct.</p>
<p id="b425-6">11. The warrant procedure, which the plaintiff appears to claim to be so precious to her, even if civil in nature, is not without its seriously objectionablé features in the welfare context. If a warrant could be obtained (the plaintiff affords us little help as to how it would be obtained), it presumably could be applied for <em>ex parte, </em>its execution would require no notice, it would justify entry <page-number citation-index="1" label="324">*324</page-number>by force, and its hours for execution<footnotemark>13</footnotemark> would not be so limited as those prescribed for home visitation. The warrant necessarily would imply conduct either criminal or out of compliance with an asserted governing standard. Of course, the force behind the warrant argument, welcome to the one asserting it, is the fact that it would have to rest upon probable cause, and probable cause in the welfare context, as Mrs. James concedes, requires more than the mere need of the caseworker to see the child in the home and to have assurance that the child is there and is receiving the benefit of the aid that has been authorized for it. In this setting, the warrant argument is out of place.</p>
<p id="b426-4">It seems to us that the situation is akin to that where an Internal Revenue Service agent, in making a routine civil audit of a tapayer’s income tax return, asks that the taxpayer produce for the agent’s review some, proof of a deduction the taxpayer has asserted to his benefit in the computation of his tax. If thé taxpayer refuses, . there is, absent fraud, only a disallowance of the claimed deduction and a consequent additional tax. The taxpayer is fully within his “rights” in refusing to produce the proof, but in maintaining and asserting those rights a tax detriment results and it is a detriment of the taxpayer’s own making. So here Mrs. James has the “right” to refuse the home visit, but a consequence in the form of cessation of aid,' similar to the taxpayer’s resultant additional tax, flows' from that refusal. The choice is entirely hers, and nothing of constitutional magnitude is involved.</p>
<p id="b426-5">VI</p>
<p id="b426-6"><em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967), and its companion case, <em>See </em>v. <em>City of Seattle, </em><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967), both by a divided. Court, are not incon<page-number citation-index="1" label="325">*325</page-number>sistent with our result here. Those cases concerned, respectively, a refusal of entry to city housing inspectors checking for a violation of a building’s occupancy permit, and a refusal of entry to a fire department representative interested in compliance with a city’s fire code. In each case a majority of this Court held that the Fourth Amendment barred prosecution for refusal to permit the desired warrantless inspection. <em>Frank </em>v. <em>Maryland, </em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360</a></span> (1959), a case that reáched an opposing result and that concerned a request by a health officer for entry in order to check the source of a rat infestation, was <em>pro tanto </em>overruled. Both <em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span> </em>and <em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span> </em>involved dwelling quarters. <em>See </em>had to do with a commercial warehouse.</p>
<p id="b427-5">But the facts of the three cases are significantly different from those before us. Each concerned a true search, for violations. <em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span> </em>was a criminal prosecution for the owner’s refusal to permit entry. So, too, was <em>See. Cam-ara </em>had to do with a writ of prohibition sought to prevent an already pending criminal prosecution. The community welfare aspects, of course, were highly important, but each case arose in a criminal context where a genuine search was denied and prosecution followed.</p>
<p id="b427-6">In contrast, Mrs. James is not being prosecuted for her refusal to permit the home visit and is not about to be so prosecuted. Her wishes in that respect are fully honored. We. have not been told, and have not found, that her refusal is made a criminal act by any applicable New York or federal statute. The only consequence of her refusal is that the payment of benefits ceases. Important and serious as this is, the situation is no different than if she had exercised a similar negative choice initially and refrained frorp applying for AFDC benefits. If a statute made her refusal a criminal offense, and if this case were one concerning her prosecution under that statute, <em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span> </em>and <em>See </em>would have conceivable pertinency.</p>
<p id="b428-3"><page-number citation-index="1" label="326">*326</page-number>VII</p>
<p id="b428-4">Our holding today does not mean, of course, that a termination of benefits upon refusal of a home visit is to be upheld against constitutional challenge, under all conceivable circumstances. The early morning maás raid upon homes of welfare recipients is not unknown. See <em>Parrish </em>v. <em>Civil Service Comm’n, </em><span class="citation" data-id="9577689"><a href="/opinion/1240070/parrish-v-civil-service-commission/" aria-description="Citation for case: Parrish v. Civil Service Commission">66 Cal. 2d 260</a></span>, <span class="citation" data-id="9577689"><a href="/opinion/1240070/parrish-v-civil-service-commission/" aria-description="Citation for case: Parrish v. Civil Service Commission">425 P. 2d 223</a></span> (1967); Reich, Midnight Welfare Searches and the Social Security Act, 72 Yale L. J. 1347 (1963). But that is not this case. Facts of that kind present another cáse for another day.</p>
<p id="b428-5">We therefore conclude that the home visitation as structured by the New York statutes and regulations is a reasonable administrative tool; that it serves a valid and proper administrative purpose for the dispensation of the AFDC program; that, it'is not an unwarranted invasion of personal privacy; and that it violates no right guaranteed by the Fourth Amendment.</p>
<p id="b428-6">Reversed and remanded with directions to enter a judgment of dismissal.</p>
<p id="b428-7">
<em>It is so , ordered.</em>
</p>
<judges id="b428-8">Mr. Justice White concurs in the judgment and joins the opinion of the Court with the exception of Part IV thereof.</judges>
<footnote label="1">
<p id="b412-12"> In <em>Goldberg </em>v. <em>Kelly, </em><span class="citation" data-id="9424206"><a href="/opinion/108100/goldberg-v-kelly/" aria-description="Citation for case: Goldberg v. Kelly">397 U. S. 254</a></span>, 256 n. 1 (1970), the Court observed that AFDC is a categorical assistance program supported <page-number citation-index="1" label="311">*311</page-number>by federal grants-in-aid but administered by the States according to regulations of the Secretary of Health, Education, and Welfare. See New York Social Services Law §§ 343-362 (1966 and Supp. 1969-1970). Aspects of AFDC have been considered in <em>King </em>v. <em>Smith, </em><span class="citation" data-id="9423792"><a href="/opinion/107743/king-v-smith/" aria-description="Citation for case: King v. Smith">392 U. S. 309</a></span> (1968); <em>Shapiro </em>v. <em>Thompson, </em><span class="citation" data-id="9424000"><a href="/opinion/107901/shapiro-v-thompson/" aria-description="Citation for case: Shapiro v. Thompson">394 U. S. 618</a></span> (1969); <em>Goldberg </em>v. <em><span class="citation" data-id="9424206"><a href="/opinion/108100/goldberg-v-kelly/" aria-description="Citation for case: Goldberg v. Kelly">Kelly, supra;</a></span> Rosado </em>v. <em>Wyman, </em><span class="citation" data-id="9424226"><a href="/opinion/108113/rosado-v-wyman/" aria-description="Citation for case: Rosado v. Wyman">397 U. S. 397</a></span> (1970); and <em>Dandridge </em>v. <em>Williams, </em><span class="citation" data-id="9424234"><a href="/opinion/108115/dandridge-v-williams/" aria-description="Citation for case: Dandridge v. Williams">397 U. S. 471</a></span> (1970).</p>
</footnote>
<footnote label="2">
<p id="b413-6"> “§ 134. Supervision.</p>
<blockquote id="b413-7">“The public welfare officials responsible . . ..'for investigating any. application for public assistance and care, shall maintain close contact with persons granted public assistance and care. Such persons shall be visited as frequently as is provided by the rules of the board' and/or regulations of the department or required by the circumstances of the case, in order that any treatment-or service tending to restore such persons to a condition of self-support and to relieve their distress may be rendered and in order that assistance or care may be given only in such amount and as long as necessary. The circumstances of a person receiving continued care shall be re-investigated as frequently as the rules of the board or regulations of the department may require.”</blockquote>
<p id="b413-10">Section 134-a, as added by Laws 1967, c. 183, effective April 1, 1967, provides:</p>
<blockquote id="b413-11">“In accordance with regulations- of the department, any investigation or- reinvestigation of eligibility . . . shall be limited to those factors reasonably necessary to insure that expenditures shall be in accord with applicable provisions of this chapter and the rules of the board and regulations of the department and shall be conducted in siich manner so as not to violate any civil right of the applicant or recipient. In making such investigation or reinvfestigation, sources of information, other than public records, shall be consulted only with the permission of the applicant or recipient. However, if such permission is not granted by the applicant or recipient, the appropriate public welfare official may deny, suspend or discontinue public assistance or care until such time as he may- be satisfied that such applicant or recipient is eligible therefor.”</blockquote>
</footnote>
<footnote label="3">
<p id="b414-6"> “Mandatory visits must be made in accordance with law that requires that persons be visited at least once .every three months if they are receiving . . . Aid to Dependent Children <em>. . .</em></p>
<p id="b414-9">4 “Section 351.10. <em>Required, home . visits and contacts. </em>Social investigation as defined and described . . . shall be made of each application or- reapplication for public assistance or-care as the basis for determination of initial eligibility.</p>
<blockquote id="b414-10">“a. Determination of initial eligibility, shall include contact with the applicant and at least one home visit which shall be made promptly in accordance with agency policy. . . .”</blockquote>
<blockquote id="b414-11">“Section 351.21. <em>Required contacts. </em>Contacts with recipients and collateral sources shall be adequate as to content and frequency and shall include home visits, office interviews, correspondence, reports oh resources and other necessary documentation.”</blockquote>
<blockquote id="b414-12">Section 3.69.2 of Title 18 provides in part: “(c) <em>Welfare of child or minor. </em>A child or minor shall be considered to be eligible for ADC if his home situation is one in which his physical, mental and moral well-being will be safeguarded and his religious faith preserved and protected. (1) In determining the ability of a parent or relative to care for the child so that this purpose is achieved, the home shall be judged by the same standards as are applied to self-maintaining families in the community. When, at the time of application, a home does not meet the usual standards of health and decency but the welfare of the child is not endangered, ADC shall be granted and defined services provided in an effort to improve the situation. Where appropriate, consultation or direct service shall be requested from child welfare.”</blockquote>
</footnote>
<footnote label="5">
<p id="b416-9"> No issue of procedural due process is raised in. this case. Cf. <em>Goldberg </em>v. <em>Kelly, </em><span class="citation" data-id="9424206"><a href="/opinion/108100/goldberg-v-kelly/" aria-description="Citation for case: Goldberg v. Kelly">397 U. S. 254</a></span> (1970), and <em>Wheeler </em>v. <em>Montgomery, </em><span class="citation" data-id="9805412"><a href="/opinion/2764187/wheeler-v-montgomery/" aria-description="Citation for case: Wheeler v. Montgomery">397 U. S. 280</a></span> (1970).</p>
</footnote>
<footnote label="6">
<p id="b421-8"> The federal regulations require only periodic redeterminations of eligibility. HEW Handbook of Public Assistance Administration, pt. IV, § 2200 (d). But they also require verification of eligibility by making field- investigations “including home visits” in a selected sample of cases. Pt. II, §6200 (a)(3).</p>
</footnote>
<footnote label="7">
<p id="b422-6"> See, <em>e. g., </em>Ala., Manual for Administration of Public Assistance, pt. 1-8 (B) (1968 rev.); Ariz., Regulations promulgated pursuant to Rev. Stat. Ann. §46-203 (1956), Reg. 3-203.6 (1968); Ark. Stat. Ann. §83-131 (1960); Cal. State Dept, of Social Welfare. Handbook, C-012.50 (1964); <span class="citation no-link">Colo. Rev. Stat. Ann. § 119-9-1</span> <em>et seq. </em>(Supp. 1967), as amended, Laws 1969, c. 279; Fla. Public Assistance c. 100; Ga. Division of Social Administration — Public Assistance Manual, pt. III, §V (D)(2), pt. VIII (A) (1) (b) (1969); Ill. Rev. Stat., c. 23, §4-7 (1967); Ind. Ann. Stat. §52-1247 (1964), Dept. Pub. Welfare, Rules &amp; Regs., Reg. 2-403 (1965); Mich. Public Assistance Manual, Item 243 (3) (F) (Rqv.) (1967); <span class="citation no-link">Miss. Code Ann. § 7177</span> (1942) (Laws of 1940, c. 294); Mo. Public Assistance Manual, Dept, of Welfare, § III (1969); Nebraska, State Plan and Manual Regulations, pt. IX, §§ 5760, 5771; N. J., Manual of Administration, Division of Public Welfare, pt. II, §§2120, 2122 (1969); N. M. Stat. Ann. § 13-1-13 (1953), Health and Social Services Dept. Manual, §§211.5, 272.11; S, C. Dept, of Public Welfare Manual, Vol. IV (D)(2); S. D. Comp. Laws Ann. §28-7-7 (1967) (formerly S. D. Code §55.3805); <span class="citation no-link">Tenn. Code Ann. §14-309</span> (1955), Public Assistance Manual, Vol. II, p. 212 (1968 rev.); <span class="citation no-link">Wis. Stat. § 49.19</span> (2) (1967).</p>
</footnote>
<footnote label="8">
<p id="AUq"> It is true that the record contains 12 affidavits, all essentially identical, of aid recipients (other than Mrs. James) which recite that a caseworker “most often” comes without notice; that when he does, the plans the recipient had for that time cannot be carried out; that the visit is “very embarrassing to me if the caseworker, comes when I have company”; and that the caseworker “sometimes asks very personal questions” in front of children.</p>
</footnote>
<footnote label="9">
<p id="b424-7"> We have examined Mrs. James’ case record with the New York City Department of Social Services, which, as an exhibit, accompanied defendant Wyman’s answer. It discloses numerous interviews from the time of the initial one on April 27, 1967, until the attempted termination in June 1969. The record is revealing as to Mrs. James’ failure ever really to satisfy the requirements for eligibility; as to constant and repeated demands; as to attitude toward the caseworker; as to reluctance to cooperate; as to evasiveness; and as to occasional belligerency. There are indications that all was not always well with the infant Maurice (skull fracture, a dent in the head, a possible rat bite). The picture is a sad and unhappy one.</p>
</footnote>
<footnote label="10">
<p id="b424-9"><em> </em>§ 406 (a) of the Social Security Act, as amended, <span class="citation no-link">42 U. S. C. § 606</span> (a) (1964 ed., Supp. V); § 349B1 of the New York Social Services Law.</p>
</footnote>
<footnote label="11">
<p id="b424-10"> The <em>amicus </em>brief submitted on behalf of the Social Services Employees Union Local 371, AFSCME, AFL-CIO, the bargaining representative for the social service staff" employed in the New York City Department of Social Services,- recites that “caseworkers are either badly trained or untrained” and that “[generally, a case-. worker is not only poorly trained, but also young and inexperi<page-number citation-index="1" label="323">*323</page-number>enced <em>. . . </em>Despite this astonishing description by the union of the. lack of qualification of its own members for the work they are employed to do, we must assume that the caseworker possesses at least some qualifications and some dedication to duty.</p>
</footnote>
<footnote label="12">
<p id="b425-8"> See, for example, New York Social Services Law § 145.</p>
</footnote>
<footnote label="13">
<p id="b426-7"> New York Code Crim. Proc. § 801.</p>
</footnote>
<footnote label="4">
<p id="b429-10"> See Appendix II to this opinion.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Wyoming v. Houghton.md  (`case`, 5 assertions)

### content_page

```
---
title: "Wyoming v. Houghton"
type: case
citation: "526 U.S. 295 (1999)"
parallel_cite: "119 S. Ct. 1297; 143 L. Ed. 2d 408"
neutral_cite: 1999 U.S. LEXIS 2347
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1999
date_decided: 1999-04-05
docket: 98-184
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1999-04-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Wyoming v. Houghton
  varies_by_point: false
  scope_note: "Extends the Ross container rule to a passenger's belongings; good law. Does not authorize searching a passenger's person."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118277/wyoming-v-houghton/"
  cluster_id: 118277
  opinion_id: 118277
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Ross]]", "[[California v. Acevedo]]", "[[Maryland v. Pringle]]"]
aliases: ["Houghton"]
tags: ["case", "fourth-amendment", "automobile-exception", "containers", "passengers", "probable-cause"]
holding: "With PC to search a car, officers may search a passenger's belongings capable of concealing the object; a non-suspect passenger's ownership is no shield."
lake:
  record_id: Wyoming v. Houghton
  status: verified
  projected_at: 2026-07-09
---

# Wyoming v. Houghton

*526 U.S. 295 (1999)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Wyoming highway patrolman stopped a car and saw a hypodermic syringe in the driver's pocket; the driver admitted he used it for drugs, giving probable cause to search the car for narcotics. Two passengers were in the car, including Sandra Houghton. Searching the passenger compartment, the officer found a purse on the back seat that Houghton acknowledged was hers, searched it, and found drug paraphernalia and methamphetamine. The Wyoming Supreme Court suppressed the evidence, reasoning the officer lacked probable cause specific to Houghton or her purse.

## Issue
Whether, when officers have probable cause to search a car for contraband, the automobile exception lets them search a passenger's belongings found in the car that could conceal the object of the search.

## Rule
Where founding-era history is inconclusive, reasonableness is assessed by balancing: the Court must "evaluate the search or seizure under traditional standards of reasonableness by assessing, on the one hand, the degree to which it intrudes upon an individual's privacy and, on the other, the degree to which it is needed for the promotion of legitimate governmental interests." — 526 U.S. at 300. ^pin-300

Applying that balance, the Court announced a [[Common Legal Terms#bright-line-rule|bright-line rule]]: "We hold that police officers with probable cause to search a car may inspect passengers' belongings found in the car that are capable of concealing the object of the search." — [*Id.* at 307](https://www.courtlistener.com/opinion/118277/wyoming-v-houghton/#:~:text=We%20hold%20that%20police%20officers). ^pin-307

The rule reaches containers and belongings in the car, not a search of the passenger's person.

## Application
On these facts the syringe in the driver's pocket and his admission gave the officer probable cause to search the car for drugs, and under the container rule that probable cause extended to any container in the car capable of holding the drugs. Houghton's purse on the back seat was such a container, and the fact that it belonged to a passenger rather than the driver did not place it off limits: contraband can be concealed in a passenger's belongings as readily as the driver's, a passenger's privacy interest in property left in a car is reduced, and the governmental interest in effective vehicle searches is substantial. The search of the purse was therefore lawful.

## Conclusion
Officers with probable cause to search a vehicle may search a passenger's belongings capable of concealing the object of the search; a non-suspect passenger's ownership is no shield. The judgment of the Wyoming Supreme Court was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Houghton* extends the container rule of [[United States v. Ross]] (reaffirmed in [[California v. Acevedo]]) to a passenger's belongings. It governs property in the car, not the passenger's person; the related question of probable cause as to passengers themselves is addressed in [[Maryland v. Pringle]].

## Appears on
- [[Automobile Exception]] — *Key — Progeny / Refinement*

## Sources
- *Wyoming v. Houghton*, 526 U.S. 295 (1999) — https://www.courtlistener.com/opinion/118277/wyoming-v-houghton/ — pinpoints: 300, 307.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b83fbf759ae74314", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "526 U.S. 295 (1999)", "court": "U.S. Supreme Court", "neutral_cite": "1999 U.S. LEXIS 2347", "official_citation_present": true, "parallel_cite": "119 S. Ct. 1297; 143 L. Ed. 2d 408", "title": "Wyoming v. Houghton", "year": "1999"}}
{"assertion_id": "2ee985cfcc42dd35", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Key — Progeny / Refinement", "title": "Wyoming v. Houghton"}}
{"assertion_id": "51a601fcf65ac037", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "With PC to search a car, officers may search a passenger's belongings capable of concealing the object; a non-suspect passenger's ownership is no shield.", "title": "Wyoming v. Houghton"}}
{"assertion_id": "a31df74d12d68968", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1999-04-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Wyoming v. Houghton", "field_i_validity": "good_law", "scope_note": "Extends the Ross container rule to a passenger's belongings; good law. Does not authorize searching a passenger's person.", "title": "Wyoming v. Houghton", "varies_by_point": "false"}}
{"assertion_id": "af3847643d98e4ef", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Wyoming v. Houghton"}}
```

### lake record — Wyoming v. Houghton

```json
{
  "schema_version": "s2.v1",
  "record_id": "Wyoming v. Houghton",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Wyoming v. Houghton",
    "case_name_short": "Houghton",
    "case_name_full": "Wyoming v. Houghton",
    "input_case_name": "Wyoming v. Houghton",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1999-04-05",
    "year": 1999,
    "docket": "98-184",
    "cluster_id": 118277,
    "lead_opinion_id": 118277,
    "sibling_ids": [
      118277,
      9433782,
      9433783,
      9433784
    ],
    "absolute_url": "/opinion/118277/wyoming-v-houghton/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "526 U.S. 295",
      "volume": "526",
      "reporter": "U.S.",
      "page": "295",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "119 S. Ct. 1297",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1297",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "143 L. Ed. 2d 408",
        "volume": "143",
        "reporter": "L. Ed. 2d",
        "page": "408",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1999 U.S. LEXIS 2347",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "2347",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "526 U.S. 295",
        "volume": "526",
        "reporter": "U.S.",
        "page": "295",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "119 S. Ct. 1297",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1297",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "143 L. Ed. 2d 408",
        "volume": "143",
        "reporter": "L. Ed. 2d",
        "page": "408",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1999 U.S. LEXIS 2347",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "2347",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "526 U.S. 295",
    "official_selection": {
      "court_class": "scotus",
      "selected": "526 U.S. 295",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-300",
      "page": null,
      "quote": "--- # Wyoming v. Houghton *526 U.S. 295 (1999)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Wyoming highway patrolman stopped a car and saw a hypodermic syringe in the driver's pocket; the driver admitted he used it for drugs, giving probable cause to search the car for narcotics. Two passengers were in the car, including Sandra Houghton. Searching the passenger compartment, the officer found a purse on the back seat that Houghton acknowledged was hers, searched it, and found drug paraphernalia and methamphetamine. The Wyoming Supreme Court suppressed the evidence, reasoning the officer lacked probable cause specific to Houghton or her purse. ## Issue Whether, when officers have probable cause to search a car for contraband, the automobile exception lets them search a passenger's belongings found in the car that could conceal the object of the search. ## Rule Where founding-era history is inconclusive, reasonableness is assessed by balancing: the Court must",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-307",
      "page": null,
      "quote": "We hold that police officers with probable cause to search a car may inspect passengers' belongings found in the car that are capable of concealing the object of the search.",
      "star_marker": "307",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 25902,
      "fragment": "#:~:text=We%20hold%20that%20police%20officers",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1999-04-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Wyoming v. Houghton",
    "varies_by_point": false,
    "scope_note": "Extends the Ross container rule to a passenger's belongings; good law. Does not authorize searching a passenger's person.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Wyoming v. Houghton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Will Thomas v. State of Indiana",
          "cluster_id": 4332194,
          "cite": [
            "65 N.E.3d 1096",
            "2016 Ind. App. LEXIS 457",
            "2016 WL 7397545"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wyoming v. Houghton:lane1_negative"
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
        "journal_ref": "Wyoming v. Houghton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ted Phillips",
          "cluster_id": 4250252,
          "cite": [
            "834 F.3d 1176",
            "2016 WL 4435613"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wyoming v. Houghton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Weathers v. State of Indiana",
          "cluster_id": 4248521,
          "cite": [
            "61 N.E.3d 279",
            "2016 Ind. App. LEXIS 297",
            "2016 WL 4379346"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wyoming v. Houghton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Florida v. Jardines",
          "cluster_id": 856347,
          "cite": [
            "185 L. Ed. 2d 495",
            "133 S. Ct. 1409",
            "569 U.S. 1",
            "2013 U.S. LEXIS 2542",
            "24 Fla. L. Weekly Fed. S 117",
            "81 U.S.L.W. 4209",
            "2013 WL 1196577"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Pringle",
          "cluster_id": 131150,
          "cite": [
            "157 L. Ed. 2d 769",
            "124 S. Ct. 795",
            "540 U.S. 366",
            "2003 U.S. LEXIS 9198"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Knights",
          "cluster_id": 118468,
          "cite": [
            "151 L. Ed. 2d 497",
            "122 S. Ct. 587",
            "534 U.S. 112",
            "2001 U.S. LEXIS 10950"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
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
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Riley v. Cal. United States",
          "cluster_id": 2680439,
          "cite": [
            "189 L. Ed. 2d 430",
            "134 S. Ct. 2473",
            "2014 U.S. LEXIS 4497",
            "82 U.S.L.W. 4558"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jenkins",
          "cluster_id": 1195356,
          "cite": [
            "997 P.2d 1044",
            "95 Cal. Rptr. 2d 377",
            "22 Cal. 4th 900"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
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
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thornton v. United States",
          "cluster_id": 134746,
          "cite": [
            "158 L. Ed. 2d 905",
            "124 S. Ct. 2127",
            "541 U.S. 615",
            "2004 U.S. LEXIS 3681"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Safford Unified School District 1 v. Redding",
          "cluster_id": 145852,
          "cite": [
            "174 L. Ed. 2d 354",
            "129 S. Ct. 2633",
            "557 U.S. 364",
            "2009 U.S. LEXIS 4735",
            "21 Fla. L. Weekly Fed. S 1011",
            "77 U.S.L.W. 4591"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
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
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albert Woods v. City of Chicago, Officer Makowski, Chicago Police Officer 16971, Officer Alanis, Chicago Police Officer 5001",
          "cluster_id": 771403,
          "cite": [
            "234 F.3d 979",
            "55 Fed. R. Serv. 912",
            "2000 U.S. App. LEXIS 31315",
            "2000 WL 1801038"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Francis S. v. Stone",
          "cluster_id": 7080910,
          "cite": [
            "221 F.3d 100",
            "2000 WL 1120432"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
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
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
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
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
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
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Center for Bio-Ethical Reform, Inc. v. Los Angeles County Sheriff Department",
          "cluster_id": 1235108,
          "cite": [
            "533 F.3d 780",
            "2008 U.S. App. LEXIS 13975",
            "2008 WL 2599683"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
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
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
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
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Francis v. James Stone",
          "cluster_id": 769740,
          "cite": [
            "221 F.3d 100",
            "2000 U.S. App. LEXIS 19016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
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
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
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
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Wear",
          "cluster_id": 2231471,
          "cite": [
            "893 N.E.2d 631",
            "229 Ill. 2d 545",
            "323 Ill. Dec. 359",
            "2008 Ill. LEXIS 636"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe v. Woodard",
          "cluster_id": 4578612,
          "cite": [
            "912 F.3d 1278"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Parker",
          "cluster_id": 1401702,
          "cite": [
            "987 P.2d 73"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wyoming v. Houghton:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118277 OR 9433782 OR 9433783 OR 9433784) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDEwNDgwMDAwMDAwJnM9MjczMjUwMyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118277+OR+9433782+OR+9433783+OR+9433784%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118277 OR 9433782 OR 9433783 OR 9433784)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDcmcz04MjE1MjEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118277+OR+9433782+OR+9433783+OR+9433784%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118277 OR 9433782 OR 9433783 OR 9433784)",
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
    "complete_query": "cites:(118277 OR 9433782 OR 9433783 OR 9433784)",
    "indexed_citing_opinions": 613,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118277,
        "count": 523,
        "count_source": "search"
      },
      {
        "opinion_id": 9433782,
        "count": 97,
        "count_source": "search"
      },
      {
        "opinion_id": 9433783,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433784,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 988,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/wyoming-v-houghton.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1NDQyMzkmcz05NDQzOTIwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118277+OR+9433782+OR+9433783+OR+9433784%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118277,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 109876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 111305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 112579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 112608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 112856,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 118086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 118100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118277,
        "cited_id": 1433794,
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
    "date_created": "2026-07-06T04:48:29Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:48:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:48:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:50:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:48:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Wyoming v. Houghton

```
<div>
<center><b><span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/" aria-description="Citation for case: Wyoming v. Houghton">526 U.S. 295</a></span> (1999)</b></center>
<center><h1>WYOMING<br>
v.<br>
HOUGHTON</h1></center>
<center>No. 98-184.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued January 12, 1999.</center>
<center>Decided April 5, 1999.</center>
CERTIORARI TO THE SUPREME COURT OF WYOMING
<p><span class="star-pagination">*297</span> Scalia, J., delivered the opinion of the Court, in which Rehnquist, C. J., and O'Connor, Kennedy, Thomas, and Breyer, JJ., joined. Breyer, J., filed a concurring opinion, <i>post,</i> p. 307. Stevens, J., filed a dissenting opinion, in which Souter and Ginsburg, JJ., joined, <i>post,</i>  p. 309.</p>
<p><i>Paul S. Rehurek,</i> Deputy Attorney General of Wyoming, argued the cause for petitioner. With him on the briefs were <i>Gay Woodhouse,</i> Acting Attorney General, and <i>D. Michael Pauling,</i> Senior Assistant Attorney General.</p>
<p><i>Barbara McDowell</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With her on the brief were <i>Solicitor General Waxman, Assistant Attorney General Robinson,</i> and <i>Deputy Solicitor General Dreeben.</i> </p>
<p><span class="star-pagination">*297</span> <i>Donna D. Domonkos,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./525/980/">525 U. S. 980</a></span>, argued the cause for respondent. With her on the brief were <i>Sylvia Lee Hackl</i> and <i>Michael Dinnerstein.</i><sup>[*]</sup></p>
<p>Justice Scalia, delivered the opinion of the Court.</p>
<p>This case presents the question whether police officers violate the Fourth Amendment when they search a passenger's personal belongings inside an automobile that they have probable cause to believe contains contraband.</p>
<p></p>
<h2>I</h2>
<p>In the early morning hours of July 23, 1995, a Wyoming Highway Patrol officer stopped an automobile for speeding and driving with a faulty brake light. There were three <span class="star-pagination">*298</span> passengers in the front seat of the car: David Young (the driver), his girlfriend, and respondent. While questioning Young, the officer noticed a hypodermic syringe in Young's shirt pocket. He left the occupants under the supervision of two backup officers as he went to get gloves from his patrol car. Upon his return, he instructed Young to step out of the car and place the syringe on the hood. The officer then asked Young why he had a syringe; with refreshing candor, Young replied that he used it to take drugs.</p>
<p>At this point, the backup officers ordered the two female passengers out of the car and asked them for identification. Respondent falsely identified herself as "Sandra James" and stated that she did not have any identification. Meanwhile, in light of Young's admission, the officer searched the passenger compartment of the car for contraband. On the back seat, he found a purse, which respondent claimed as hers. He removed from the purse a wallet containing respondent's driver's license, identifying her properly as Sandra K. Houghton. When the officer asked her why she had lied about her name, she replied: "In case things went bad."</p>
<p>Continuing his search of the purse, the officer found a brown pouch and a black wallet-type container. Respondent denied that the former was hers, and claimed ignorance of how it came to be there; it was found to contain drug paraphernalia and a syringe with 60 ccs of methamphetamine. Respondent admitted ownership of the black container, which was also found to contain drug paraphernalia, and a syringe (which respondent acknowledged was hers) with 10 ccs of methamphetaminean amount insufficient to support the felony conviction at issue in this case. The officer also found fresh needle-track marks on respondent's arms. He placed her under arrest.</p>
<p>The State of Wyoming charged respondent with felony possession of methamphetamine in a liquid amount greater than three-tenths of a gram. See <span class="citation no-link">Wyo. Stat. Ann. § 35-71031</span>(c)(iii) (Supp. 1996). After a hearing, the trial court denied <span class="star-pagination">*299</span> her motion to suppress all evidence obtained from the purse as the fruit of a violation of the Fourth and Fourteenth Amendments. The court held that the officer had probable cause to search the car for contraband, and, by extension, any containers therein that could hold such contraband. A jury convicted respondent as charged.</p>
<p>The Wyoming Supreme Court, by divided vote, reversed the conviction and announced the following rule:</p>
<blockquote>"Generally, once probable cause is established to search a vehicle, an officer is entitled to search all containers therein which may contain the object of the search. However, if the officer knows or should know that a container is the personal effect of a passenger who is not suspected of criminal activity, then the container is outside the scope of the search unless someone had the opportunity to conceal the contraband within the personal effect to avoid detection." <span class="citation" data-id="9628871"><a href="/opinion/1433794/houghton-v-state/#372" aria-description="Citation for case: Houghton v. State">956 P. 2d 363, 372</a></span> (1998).</blockquote>
<p>The court held that the search of respondent's purse violated the Fourth and Fourteenth Amendments because the officer "knew or should have known that the purse did not belong to the driver, but to one of the passengers," and because "there was no probable cause to search the passengers' personal effects and no reason to believe that contraband had been placed within the purse." <i><span class="citation" data-id="9628871"><a href="/opinion/1433794/houghton-v-state/" aria-description="Citation for case: Houghton v. State">Ibid.</a></span></i> We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./524/983/">524 U. S. 983</a></span> (1998).</p>
<p></p>
<h2>II</h2>
<p>The Fourth Amendment protects "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures." In determining whether a particular governmental action violates this provision, we inquire first whether the action was regarded as an unlawful search or seizure under the common law when the Amendment was framed. See <i>Wilson</i> v. <i>Arkansas,</i> <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#931" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927, 931</a></span> (1995); <i>California</i> v. <i>Hodari D.,</i> <span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/#624" aria-description="Citation for case: California v. Hodari D.">499 U. S. 621, 624</a></span> (1991). Where that inquiry yields no answer, we must <span class="star-pagination">*300</span> evaluate the search or seizure under traditional standards of reasonableness by assessing, on the one hand, the degree to which it intrudes upon an individual's privacy and, on the other, the degree to which it is needed for the promotion of legitimate governmental interests. See, <i>e. g., </i><i>Vernonia School Dist. 47J</i> v. <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#652" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646, 652-653</a></span> (1995).</p>
<p>It is uncontested in the present case that the police officers had probable cause to believe there were illegal drugs in the car. <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), similarly involved the warrantless search of a car that law enforcement officials had probable cause to believe contained contrabandin that case, bootleg liquor. The Court concluded that the Framers would have regarded such a search as reasonable in light of legislation enacted by Congress from 1789 through 1799as well as subsequent legislation from the founding era and beyondthat empowered customs officials to search any ship or vessel without a warrant if they had probable cause to believe that it contained goods subject to a duty. <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#150" aria-description="Citation for case: Carroll v. United States"><i>Id.,</i> at 150-153</a></span>. See also <i>United States</i> v. <i>Ross,</i>  <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#806" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 806</a></span> (1982); <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#623" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 623-624</a></span> (1886). Thus, the Court held that "contraband goods concealed and illegally transported in an automobile or other vehicle may be searched for without a warrant" where probable cause exists. <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States"><i>Carroll, supra,</i> at 153</a></span>.</p>
<p>We have furthermore read the historical evidence to show that the Framers would have regarded as reasonable (if there was probable cause) the warrantless search of containers <i>within</i> an automobile. In <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross, supra,</a></span></i> we upheld as reasonable the warrantless search of a paper bag and leather pouch found in the trunk of the defendant's car by officers who had probable cause to believe that the trunk contained drugs. Justice Stevens, writing for the Court, observed:</p>
<blockquote>"It is noteworthy that the early legislation on which the Court relied in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> concerned the enforcement of laws imposing duties on imported merchandise. . . . Presumably such merchandise was shipped then in containers <span class="star-pagination">*301</span> of various kinds, just as it is today. Since Congress had authorized warrantless searches of vessels and beasts for imported merchandise, it is inconceivable that it intended a customs officer to obtain a warrant for every package discovered during the search; certainly Congress intended customs officers to open shipping containers when necessary and not merely to examine the exterior of cartons or boxes in which smuggled goods might be concealed. During virtually the entire history of our countrywhether contraband was transported in a horse-drawn carriage, a 1921 roadster, or a modern automobileit has been assumed that a lawful search of a vehicle would include a search of any container that might conceal the object of the search." <i>Id.,</i>  at 820, n. 26.</blockquote>
<p><i>Ross</i> summarized its holding as follows: "If probable cause justifies the search of a lawfully stopped vehicle, it justifies the search of <i>every part of the vehicle and its contents</i> that may conceal the object of the search." <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#825" aria-description="Citation for case: United States v. Ross"><i>Id.,</i> at 825</a></span> (emphasis added). And our later cases describing <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> have characterized it as applying broadly to <i>all</i> containers within a car, without qualification as to ownership. See, <i>e. g., </i><i>California</i>  v. <i>Acevedo,</i> <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/#572" aria-description="Citation for case: California v. Acevedo">500 U. S. 565, 572</a></span> (1991) ("[T]his Court in <i>Ross</i>  took the critical step of saying that closed containers in cars could be searched without a warrant because of their presence within the automobile"); <i>United States</i> v. <i>Johns,</i> <span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/#479" aria-description="Citation for case: United States v. Johns">469 U. S. 478, 479-480</a></span> (1985) (<i>Ross</i> "held that if police officers have probable cause to search a lawfully stopped vehicle, they may conduct a warrantless search of any containers found inside that may conceal the object of the search").</p>
<p>To be sure, there was no passenger in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>,</i> and it was not claimed that the package in the trunk belonged to anyone other than the driver. Even so, if the rule of law that <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i>  announced were limited to contents belonging to the driver, or contents other than those belonging to passengers, one would have expected that substantial limitation to be expressed. <span class="star-pagination">*302</span> And, more importantly, one would have expected that limitation to be apparent in the historical evidence that formed the basis for <i>Ross'</i> s holding. In fact, however, nothing in the statutes <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> relied upon, or in the practice under those statutes, would except from authorized warrantless search packages belonging to passengers on the suspect ship, horse-drawn carriage, or automobile.</p>
<p>Finally, we must observe that the analytical principle underlying the rule announced in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> is fully consistentas respondent's proposal is notwith the balance of our Fourth Amendment jurisprudence. <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> concluded from the historical evidence that the permissible scope of a warrantless car search "is defined by the object of the search and the places in which there is probable cause to believe that it may be found." <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross">456 U. S., at 824</a></span>. The same principle is reflected in an earlier case involving the constitutionality of a search warrant directed at premises belonging to one who is not suspected of any crime: "The critical element in a reasonable search is not that the owner of the property is suspected of crime but that there is reasonable cause to believe that the specific `things' to be searched for and seized are located on the property to which entry is sought." <i>Zurcher</i> v. <i>Stanford Daily,</i> <span class="citation" data-id="9427224"><a href="/opinion/109876/zurcher-v-stanford-daily/#556" aria-description="Citation for case: Zurcher v. Stanford Daily">436 U. S. 547, 556</a></span> (1978). This statement was illustrated by citation and description of <i>Carroll,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S., at 158-159, 167</a></span>. <span class="citation" data-id="9427224"><a href="/opinion/109876/zurcher-v-stanford-daily/#556" aria-description="Citation for case: Zurcher v. Stanford Daily">436 U. S., at 556-557</a></span>.</p>
<p>In sum, neither <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> itself nor the historical evidence it relied upon admits of a distinction among packages or containers based on ownership. When there is probable cause to search for contraband in a car, it is reasonable for police officerslike customs officials in the founding erato examine packages and containers without a showing of individualized probable cause for each one. A passenger's personal belongings, just like the driver's belongings or containers attached to the car like a glove compartment, are "in" the car, and the officer has probable cause to search for contraband <i>in</i> the car.</p>
<p><span class="star-pagination">*303</span> Even if the historical evidence, as described by <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>,</i> were thought to be equivocal, we would find that the balancing of the relative interests weighs decidedly in favor of allowing searches of a passenger's belongings. Passengers, no less than drivers, possess a reduced expectation of privacy with regard to the property that they transport in cars, which "trave[l] public thoroughfares," <i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590</a></span> (1974), "seldom serv[e] as . . . the repository of personal effects," <i>ibid.,</i> are subjected to police stop and examination to enforce "pervasive" governmental controls "[a]s an everyday occurrence," <i>South Dakota</i> v. <i>Opperman,</i> <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#368" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 368</a></span> (1976), and, finally, are exposed to traffic accidents that may render all their contents open to public scrutiny.</p>
<p>In this regardthe degree of intrusiveness upon personal privacy and indeed even personal dignitythe two cases the Wyoming Supreme Court found dispositive differ substantially from the package search at issue here. <i>United States</i>  v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/" aria-description="Citation for case: United States v. Di Re">332 U. S. 581</a></span> (1948), held that probable cause to search a car did not justify a body search of a passenger. And <i>Ybarra</i> v. <i>Illinois,</i> <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85</a></span> (1979), held that a search warrant for a tavern and its bartender did not permit body searches of all the bar's patrons. These cases turned on the unique, significantly heightened protection afforded against searches of one's person. "Even a limited search of the outer clothing . . . constitutes a severe, though brief, intrusion upon cherished personal security, and it must surely be an annoying, frightening, and perhaps humiliating experience." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 24-25</a></span> (1968). Such traumatic consequences are not to be expected when the police examine an item of personal property found in a car.<sup>[1]</sup></p>
<p><span class="star-pagination">*304</span> Whereas the passenger's privacy expectations are, as we have described, considerably diminished, the governmental interests at stake are substantial. Effective law enforcement would be appreciably impaired without the ability to search a passenger's personal belongings when there is reason to believe contraband or evidence of criminal wrongdoing is hidden in the car. As in all car-search cases, the "ready mobility" of an automobile creates a risk that the evidence or contraband will be permanently lost while a warrant is obtained. <i>California</i> v. <i>Carney,</i> <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#390" aria-description="Citation for case: California v. Carney">471 U. S. 386, 390</a></span> (1985). In addition, a car passengerunlike the unwitting tavern patron in <i><span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">Ybarra</a></span></i> will often be engaged in a common enterprise with the driver, and have the same interest in <span class="star-pagination">*305</span> concealing the fruits or the evidence of their wrongdoing. Cf. <i>Maryland</i> v. <i>Wilson,</i> <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#413" aria-description="Citation for case: Maryland v. Wilson">519 U. S. 408, 413-414</a></span> (1997). A criminal might be able to hide contraband in a passenger's belongings as readily as in other containers in the car, see, <i>e. g., </i><i>Rawlings</i> v. <i>Kentucky,</i> <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/#102" aria-description="Citation for case: Rawlings v. Kentucky">448 U. S. 98, 102</a></span> (1980)perhaps even surreptitiously, without the passenger's knowledge or permission. (This last possibility provided the basis for respondent's defense at trial;she testified that most of the seized contraband must have been placed in her purse by her traveling companions at one or another of various times, including the time she was "half asleep" in the car.)</p>
<p>To be sure, these factors favoring a search will not always be present, but the balancing of interests must be conducted with an eye to the generality of cases. To require that the investigating officer have positive reason to believe that the passenger and driver were engaged in a common enterprise, or positive reason to believe that the driver had time and occasion to conceal the item in the passenger's belongings, surreptitiously or with friendly permission, is to impose requirements so seldom met that a "passenger's property" rule would dramatically reduce the ability to find and seize contraband and evidence of crime. Of course these requirements would not attach (under the Wyoming Supreme Court's rule) until the police officer knows or has reason to know that the container belongs to a passenger. But once a "passenger's property" exception to car searches became widely known, one would expect passenger-confederates to claim everything as their own. And one would anticipate a bog of litigationin the form of both civil lawsuits and motions to suppress in criminal trialsinvolving such questions as whether the officer should have believed a passenger's claim of ownership, whether he should have inferred ownership from various objective factors, whether he had probable cause to believe that the passenger was a confederate, or to believe that the driver might have introduced the contraband <span class="star-pagination">*306</span> into the package with or without the passenger's knowledge.<sup>[2]</sup> When balancing the competing interests, our determinations of "reasonableness" under the Fourth Amendment must take account of these practical realities. We think they militate in favor of the needs of law enforcement, and against a personal-privacy interest that is ordinarily weak.</p>
<p>Finally, if we were to invent an exception from the historical practice that <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> accurately described and summarized, it is perplexing why that exception should protect only property belonging to a passenger, rather than (what seems much more logical) property belonging to <i>anyone</i> other than the driver. Surely Houghton's privacy would have been invaded to the same degree whether she was present or absent when her purse was searched. And surely her presence in the car with the driver provided more, rather than less, reason to believe that the two were in league. It may ordinarily be easier to identify the property as belonging to someone other than the driver when the purported owner is present to identify itbut in the many cases (like <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> itself) where the car is seized, that identification may occur later, at the station <span class="star-pagination">*307</span> house; and even at the site of the stop one can readily imagine a package clearly marked with the owner's name and phone number, by which the officer can confirm the driver's denial of ownership. The sensible rule (and the one supported by history and case law) is that such a package may be searched, whether or not its owner is present as a passenger or otherwise, because it may contain the contraband that the officer has reason to believe is in the car.</p>
<p></p>
<h2>* * *</h2>
<p>We hold that police officers with probable cause to search a car may inspect passengers' belongings found in the car that are capable of concealing the object of the search. The judgment of the Wyoming Supreme Court is reversed.</p>
<p><i>It is so ordered.</i> </p>
<p>Justice Breyer, concurring.</p>
<p>I join the Court's opinion with the understanding that history is meant to inform, but not automatically to determine, the answer to a Fourth Amendment question. <i>Ante,</i> at 299300. I also agree with the Court that when a police officer has probable cause to search a car, say, for drugs, it is reasonable for that officer also to search containers within the car. If the police must establish a container's ownership prior to the search of that container (whenever, for example, a passenger says "that's mine"), the resulting uncertainty will destroy the workability of the bright-line rule set forth in <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982). At the same time, police officers with probable cause to search a car for drugs would often have probable cause to search containers regardless. Hence a bright-line rule will authorize only a limited number of searches that the law would not otherwise justify.</p>
<p>At the same time, I would point out certain limitations upon the scope of the bright-line rule that the Court describes. <span class="star-pagination">*308</span> Obviously, the rule applies only to automobile searches. Equally obviously, the rule applies only to containers found within automobiles. And it does not extend to the search of a person found in that automobile. As the Court notes, and as <i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#586" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 586-587</a></span> (1948), relied on heavily by Justice Stevens' dissent, makes clear, the search of a person, including even "`a limited search of the outer clothing,' " <i>ante,</i> at 303 (quoting <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 24-25</a></span> (1968)), is a very different matter in respect to which the law provides "significantly heightened protection." <i>Ante,</i> at 303; cf. <i>Ybarra</i> v. <i>Illinois,</i>  <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/#91" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85, 91</a></span> (1979); <i>Sibron</i> v. <i>New York,</i> <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#62" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 62-64</a></span> (1968).</p>
<p>Less obviously, but in my view also important, is the fact that the container here at issue, a woman's purse, was found at a considerable distance from its owner, who did not claim ownership until the officer discovered her identification while looking through it. Purses are special containers. They are repositories of especially personal items that people generally like to keep with them at all times. So I am tempted to say that a search of a purse involves an intrusion so similar to a search of one's person that the same rule should govern both. However, given this Court's prior cases, I cannot argue that the fact that the container was a purse <i>automatically</i> makes a legal difference, for the Court has warned against trying to make that kind of distinction. <i>United States</i> v. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#822" aria-description="Citation for case: United States v. Ross"><i>Ross, supra,</i> at 822</a></span>. But I can say that it would matter if a woman's purse, like a man's billfold, were attached to her person. It might then amount to a kind of "outer clothing," <i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i> at 24</a></span>, which under the Court's cases would properly receive increased protection. See <i>post,</i> at 312-313 (Stevens, J., dissenting) (quoting <i>United States</i> v. <i>Di Re, supra,</i> at 587). In this case, the purse was separate from the person, and no one has claimed that, under those circumstances, the type of container makes a difference. For that reason, I join the Court's opinion.</p>
<p><span class="star-pagination">*309</span> Justice Stevens, with whom Justice Souter and Justice Ginsburg join, dissenting.</p>
<p>After Wyoming's highest court decided that a state highway patrolman unlawfully searched Sandra Houghton's purse, the State of Wyoming petitioned for a writ of certiorari. The State asked that we consider the propriety of searching an automobile <i>passenger's</i> belongings when the government has developed probable cause to search the vehicle for contraband based on the <i>driver's</i> conduct. The State conceded that the trooper who searched Houghton's purse lacked a warrant, consent, or "probable cause specific to the purse or passenger." Pet. for Cert. i. In light of our established preference for warrants and individualized suspicion, I would respect the result reached by the Wyoming Supreme Court and affirm its judgment.</p>
<p>In all of our prior cases applying the automobile exception to the Fourth Amendment's warrant requirement, either the defendant was the operator of the vehicle and in custody of the object of the search, or no question was raised as to the defendant's ownership or custody.<sup>[1]</sup> In the only automobile case confronting the search of a passenger defendant <i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/" aria-description="Citation for case: United States v. Di Re">332 U. S. 581</a></span> (1948)-the Court held that the exception to the warrant requirement did not apply. <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#583" aria-description="Citation for case: United States v. Di Re"><i>Id.,</i> at 583-587</a></span> (addressing searches of the passenger's pockets and the space between his shirt and underwear, both of which uncovered counterfeit fuel rations). In <i>Di Re,</i> as here, the information prompting the search directly implicated the driver, not the passenger. Today, instead of adhering to the settled distinction between drivers and passengers, the Court fashions a new rule that is based on a distinction between property contained in clothing worn by <span class="star-pagination">*310</span> a passenger and property contained in a passenger's briefcase or purse. In cases on both sides of the Court's newly minted test, the property is in a "container" (whether a pocket or a pouch) located in the vehicle. Moreover, unlike the Court, I think it quite plain that the search of a passenger's purse or briefcase involves an intrusion on privacy that may be just as serious as was the intrusion in <i>Di Re.</i> See, <i>e. g., </i><i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#339" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 339</a></span> (1985); <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727, 733</a></span> (1878).</p>
<p>Even apart from <i>Di Re,</i> the Court's rights-restrictive approach is not dictated by precedent. For example, in <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982), we were concerned with the interest of the driver in the integrity of "his automobile," <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#823" aria-description="Citation for case: United States v. Ross"><i>id.,</i> at 823</a></span>, and we categorically rejected the notion that the scope of a warrantless search of a vehicle might be "defined by the nature of the container in which the contraband is secreted," <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross"><i>id.,</i> at 824</a></span>. "Rather, it is defined by the object of the search and the places in which there is probable cause to believe that it may be found." <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ibid.</a></span></i> We thus disapproved of a possible container-based distinction between a man's pocket and a woman's pocketbook. Ironically, while we concluded in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> that "[p]robable cause to believe that a container placed in the trunk of a taxi contains contraband or evidence does not justify a search of the entire cab," <i>ibid.,</i>  the rule the Court fashions would apparently permit a warrantless search of a passenger's briefcase if there is probable cause to believe the taxidriver had a syringe somewhere in his vehicle.</p>
<p>Nor am I persuaded that the mere spatial association between a passenger and a driver provides an acceptable basis for presuming that they are partners in crime or for ignoring privacy interests in a purse.<sup>[2]</sup> Whether or not the Fourth <span class="star-pagination">*311</span> Amendment required a warrant to search Houghton's purse, cf. <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 153</a></span> (1925), at the very least the trooper in this case had to have probable cause to believe that her purse contained contraband. The Wyoming Supreme Court concluded that he did not. <span class="citation" data-id="9628871"><a href="/opinion/1433794/houghton-v-state/#372" aria-description="Citation for case: Houghton v. State">956 P. 2d 363, 372</a></span> (1998); see App. 20-21.</p>
<p>Finally, in my view, the State's legitimate interest in effective law enforcement does not outweigh the privacy concerns at issue.<sup>[3]</sup> I am as confident in a police officer's ability to apply a rule requiring a warrant or individualized probable cause to search belongings that areas in this caseobviously owned by and in the custody of a passenger as is the Court in a "passenger-confederate[`]s" ability to circumvent the rule. <i>Ante,</i> at 305. Certainly the ostensible clarity of the Court's rule is attractive. But that virtue is insufficient justification for its adoption. <i>Arizona</i> v. <i>Hicks,</i> 480 U. S. <span class="star-pagination">*312</span> 321, 329 (1987); <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#393" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 393</a></span> (1978). Moreover, a rule requiring a warrant or individualized probable cause to search passenger belongings is every bit as simple as the Court's rule; it simply protects more privacy.</p>
<p>I would decide this case in accord with what we <i>have</i> said about passengers and privacy, rather than what we <i>might have</i> said in cases where the issue was not squarely presented. See <i>ante,</i> at 301-302. What Justice Jackson wrote for the Court 50 years ago is just as sound today:</p>
<blockquote>"The Government says it would not contend that, armed with a search warrant for a residence only, it could search all persons found in it. But an occupant of a house could be used to conceal this contraband on his person quite as readily as can an occupant of a car. Necessity, an argument advanced in support of this search, would seem as strong a reason for searching guests of a house for which a search warrant had issued as for search of guests in a car for which none had been issued. By a parity of reasoning with that on which the Government disclaims the right to search occupants of a house, we suppose the Government would not contend that if it had a valid search warrant for the car only it could search the occupants as an incident to its execution. How then could we say that the right to search a car without a warrant confers greater latitude to search occupants than a search by warrant would permit?</blockquote>
<blockquote>"We see no ground for expanding the ruling in the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case to justify this arrest and search as incident to the search of a car. We are not convinced that a person, by mere presence in a suspected car, loses immunities from search of his person to which he would otherwise be entitled." <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#587" aria-description="Citation for case: United States v. Di Re">332 U. S., at 587</a></span>.</blockquote>
<p>Accord, <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#823" aria-description="Citation for case: United States v. Ross">456 U. S., at 823, 825</a></span> (the proper scope of a warrantless automobile search based on probable cause is "no broader" than the proper scope of a search authorized <span class="star-pagination">*313</span> by a warrant supported by probable cause).<sup>[4]</sup> Instead of applying ordinary Fourth Amendment principles to this case, the majority extends the automobile warrant exception to allow searches of passenger belongings based on the driver's misconduct. Thankfully, the Court's automobile-centered analysis limits the scope of its holding. But it does not justify the outcome in this case.</p>
<p>I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the State of Kentucky et al. by <i>Albert B. Chandler III,</i> Attorney General of Kentucky, <i>Matthew Nelson,</i> Assistant Attorney General, <i>Dan Schweitzer,</i> and <i>John M. Bailey,</i> Chief State's Attorney of Connecticut, and by the Attorneys General for their respective jurisdictions as follows: <i>Bill Pryor</i> of Alabama, <i>Grant Woods</i> of Arizona, <i>Winston Bryant</i> of Arkansas, <i>Daniel E. Lungren</i> of California, <i>M. Jane Brady</i> of Delaware, <i>Thurbert E. Baker</i> of Georgia, <i>Gus F. Diaz</i> of Guam, <i>Margery S. Bronster</i> of Hawaii, <i>Alan G. Lance</i> of Idaho, <i>Thomas J. Miller</i> of Iowa, <i>Richard P. Ieyoub</i> of Louisiana, <i>Andrew Ketterer</i> of Maine, <i>J. Joseph Curran, Jr.,</i> of Maryland, <i>Frank J. Kelley</i> of Michigan, <i>Hubert H. Humphrey III</i> of Minnesota, <i>Mike Moore</i>  of Mississippi, <i>Jeremiah W. (Jay) Nixon</i> of Missouri, <i>Joseph P. Mazurek</i>  of Montana, <i>Don Stenberg</i> of Nebraska, <i>Frankie Sue Del Papa</i> of Nevada, <i>Peter Verniero</i> of New Jersey, <i>Dennis C. Vacco</i> of New York, <i>Michael F. Easley</i> of North Carolina, <i>Heidi Heitkamp</i> of North Dakota, <i>Betty D. Montgomery</i> of Ohio, <i>W. A. Drew Edmondson</i> of Oklahoma, <i>Charles M. Condon</i> of South Carolina, <i>Mark Barnett</i> of South Dakota, and <i>Jan Graham</i> of Utah; for the Criminal Justice Legal Foundation by <i>Kent S. Scheidegger</i> and <i>Charles L. Hobson;</i> and for the National Association of Police Organizations by <i>Stephen R. McSpadden.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the Legal Aid Society of New York City et al. by <i>M. Sue Wycoff;</i> for the National Association of Criminal Defense Lawyers by <i>Paul Mogin</i> and <i>Lisa B. Kemler;</i> and for the Rutherford Institute by <i>Steven H. Aden</i> and <i>John W. Whitehead.</i> </p>
<p>[1]  The dissent begins its analysis, <i>post,</i> at 309-310 (opinion of Stevens, J.), with an assertion that this case is governed by our decision in <i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/" aria-description="Citation for case: United States v. Di Re">332 U. S. 581</a></span> (1948), which held, as the dissent describes it, that the automobile exception to the warrant requirement did not justify "searches of the passenger's pockets and the space between his shirt and underwear," <i>post,</i> at 309. It attributes that holding to "the settled distinction between drivers and passengers," rather than to a distinction between search of the person and search of property, which the dissent claims is "newly minted" by today's opiniona "new rule that is based on a distinction between property contained in clothing worn by a passenger and property contained in a passenger's briefcase or purse." <i>Post,</i> at 309, 309-310.
</p>
<p>In its peroration, however, the dissent quotes extensively from Justice Jackson's opinion in <i>Di Re,</i> which makes it very clear that it is <i>precisely</i>  this distinction between search of the person and search of property that the case relied upon:</p>
<p>"The Government says it would not contend that, armed with a search warrant for a residence only, it could search all persons found in it. But an occupant of a house could be used to conceal this contraband on his person quite as readily as can an occupant of a car." <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#587" aria-description="Citation for case: United States v. Di Re">332 U. S., at 587</a></span> (quoted <i>post,</i> at 312). Does the dissent really believe that Justice Jackson was saying that a house search could not inspect <i>property</i> belonging to persons found in the housesay a large standing safe or violin case belonging to the owner's visiting godfather? Of course that is not what Justice Jackson meant at all. He was referring <i>precisely</i> to that "distinction between property contained in clothing worn by a passenger and property contained in a passenger's briefcase or purse" that the dissent disparages, <i>post,</i> at 309. This distinction between searches of the person and searches of property is assuredly <i>not</i> "newly minted," see <i>post,</i> at 310. And if the dissent thinks "pockets" and "clothing" do not count as part of the person, it must believe that the only searches of the person are strip searches.</p>
<p>[2]  The dissent is "confident in a police officer's ability to apply a rule requiring a warrant or individualized probable cause to search belongings that are . . . obviously owned by and in the custody of a passenger," <i>post,</i>  at 311. If this is the dissent's strange criterion for warrant protection ("<i>obviously</i> owned by and in the custody of") its preceding paean to the importance of preserving passengers' privacy rings a little hollow on rehearing. Should it not be enough if the passenger <i>says</i> he owns the briefcase, and the officer has no concrete reason to believe otherwise? Or would the dissent consider <i>that</i> an example of "obvious" ownership? On reflection, it seems not at all obvious precisely what constitutes obviousnessand so even the dissent's on-the-cheap protection of passengers' privacy interest in their property turns out to be unclear, and hence unadministrable. But maybe the dissent does not mean to propose an obviously-owned-by-and-in-the-custody-of test after all, since a few sentences later it endorses, <i>simpliciter,</i> "a rule requiring a warrant or individualized probable cause to search passenger belongings," <i>post,</i> at 312. For the reasons described in text, that will not work.</p>
<p>[1]  See, <i>e. g., </i><i>California</i> v. <i>Acevedo,</i> <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/" aria-description="Citation for case: California v. Acevedo">500 U. S. 565</a></span> (1991); <i>California</i> v. <i>Carney,</i> <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/" aria-description="Citation for case: California v. Carney">471 U. S. 386</a></span> (1985); <i>United States</i> v. <i>Johns,</i> <span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/" aria-description="Citation for case: United States v. Johns">469 U. S. 478</a></span> (1985); <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982); <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925); 3 W. LaFave, Search and Seizure § 7.2(c), pp. 487-488, and n. 113 (3d ed. 1996); <i>id.,</i> § 7.2(d),at 506, n. 167.</p>
<p>[2]  See <i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#587" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 587</a></span> (1948) ("We are not convinced that a person, by mere presence in a suspected car, loses immunities from search of his person to which he would otherwise be entitled"); <i>Chandler</i> v. <i>Miller,</i> <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#308" aria-description="Citation for case: Chandler v. Miller">520 U. S. 305, 308</a></span> (1997) (emphasizing individualized suspicion); <i>Ybarra</i> v. <i>Illinois,</i> <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/#91" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85, 91, 94-96</a></span> (1979) (explaining that "a person's mere propinquity to others independently suspected of criminal activity does not, without more, give rise to probable cause to search that person," and discussing <i>Di Re</i> ); <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#52" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 52</a></span> (1979); <i>Sibron</i> v. <i>New York,</i> <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#62" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 62-63</a></span> (1968); see also <i>United States</i> v. <i>Padilla,</i> <span class="citation" data-id="112856"><a href="/opinion/112856/united-states-v-padilla/#82" aria-description="Citation for case: United States v. Padilla">508 U. S. 77, 82</a></span> (1993) <i>(per curiam)</i> ("Expectations of privacy and property interests govern the analysis of Fourth Amendment search and seizure claims. Participants in a criminal conspiracy may have such expectations or interests, but the conspiracy itself neither adds to nor detracts from them").</p>
<p>[3]  To my knowledge, we have never restricted ourselves to a two-step Fourth Amendment approach wherein the privacy and governmental interests at stake must be considered only if 18th-century common law "yields no answer." <i>Ante,</i> at 299. Neither the precedent cited by the Court, nor the majority's opinion in this case, mandate that approach. In a later discussion, the Court does attempt to address the contemporary privacy and governmental interests at issue in cases of this nature. <i>Ante,</i>  at 303-306. Either the majority is unconvinced by its own recitation of the historical materials, or it has determined that considering additional factors is appropriate in any event. The Court does not admit the former; and of course the latter, standing alone, would not establish uncertainty in the common law as the prerequisite to looking beyond history in Fourth Amendment cases.</p>
<p>[4]  In response to this dissent the Court has crafted an imaginative footnote suggesting that the <i>Di Re</i> decision rested, not on Di Re's status as a mere occupant of the vehicle and the importance of individualized suspicion, but rather on the intrusive character of the search. See <i>ante,</i> at 303-304, n. 1. That the search of a safe or violin case would be less intrusive than a strip search does not, however, persuade me that the <i>Di Re</i>  case would have been decided differently if Di Re had been a woman and the gas coupons had been found in her purse. Significantly, in commenting on the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case immediately preceding the paragraphs that I have quoted in the text, the <i>Di Re</i> Court stated: "But even the National Prohibition Act did not direct the arrest of all occupants but only of the person in charge of the offending vehicle, though there is better reason to assume that no passenger in a car loaded with liquor would remain innocent of knowledge of the car's cargo than to assume that a passenger must know what pieces of paper are carried in the pockets of the driver." <i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#586" aria-description="Citation for case: United States v. Di Re">332 U. S., at 586-587</a></span>.</p>

</div>
```

---

## GROUP: content/cases/Yarborough v. Alvarado.md  (`case`, 5 assertions)

### content_page

```
---
title: "Yarborough v. Alvarado"
type: case
citation: "541 U.S. 652 (2004)"
parallel_cite: "124 S. Ct. 2140; 158 L. Ed. 2d 938"
neutral_cite: 2004 U.S. LEXIS 3843
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-06-01
docket: 02-1684
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2004-06-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Yarborough v. Alvarado
  varies_by_point: false
  scope_note: "Good law; the Miranda custody test is objective and the Court's cases had not made a suspect's age/experience part of it, so a state court did not unreasonably apply clearly established law (AEDPA). Qualified for juveniles by J.D.B. v. North Carolina (2011): a child's age is part of the custody analysis when known to the officer or objectively apparent — J.D.B. distinguished Alvarado as an AEDPA-deference holding."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/134748/yarborough-v-alvarado/"
  cluster_id: 134748
  opinion_id: 134748
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[California v. Beheler]]", "[[J.D.B. v. North Carolina]]", "[[Thompson v. Keohane]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "custody", "objective-test", "juvenile", "aedpa", "habeas"]
holding: "Because the Miranda custody test is objective and the Court's cases had not made a suspect's age or experience part of it, a state court's conclusion that a 17-year-old was not in custody was not an unreasonable application of clearly established federal law, and AEDPA barred habeas relief."
lake:
  record_id: Yarborough v. Alvarado
  status: verified
  projected_at: 2026-07-06
---

# Yarborough v. Alvarado

*541 U.S. 652 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Seventeen-year-old Michael Alvarado was questioned by a sheriff's detective about a murder committed during an attempted carjacking by his older companion. Alvarado's parents brought him to the station and waited outside while the detective interviewed him for about two hours without [[Miranda and Custodial Interrogation|Miranda warnings]]; she appealed to his interest in being truthful, twice offered breaks, and let him go home afterward. He made incriminating statements and was later charged. The California courts held he had not been in custody. On federal [[Common Legal Terms#habeas-corpus|habeas]], the Ninth Circuit granted relief, reasoning that Alvarado's youth and inexperience should have been weighed in the custody analysis.

## Issue
Whether the state court's determination that Alvarado was not "in custody" — made without considering his age and inexperience — was an unreasonable application of clearly established federal law warranting [[Common Legal Terms#habeas-corpus|habeas]] relief under AEDPA.

## Rule
No. Under AEDPA, "[w]e cannot grant relief . . . by conducting our own independent inquiry into whether the state court was correct as a *de novo* matter. . . . Relief is available under §2254(d)(1) only if the state court's decision is objectively unreasonable. . . . Under that standard, relief cannot be granted." — 541 U.S. at 665–666. ^pin-665

The custody test is objective and had not incorporated age: "Our opinions applying the *Miranda* custody test have not mentioned the suspect's age, much less mandated its consideration. The only indications in the Court's opinions relevant to a suspect's experience with law enforcement have rejected reliance on such factors." — *Id.* at 666 (citing [[California v. Beheler]] and *Berkemer*). ^pin-666

"[T]he custody inquiry states an objective rule designed to give clear guidance to the police, while consideration of a suspect's individual characteristics — including his age — could be viewed as creating a subjective inquiry." — *Id.* at 668. ^pin-668

## Application
The objective facts cut both ways — Alvarado came to a voluntary, eventually-released interview (like *[[Oregon v. Mathiason|Mathiason]]*), but it was two hours long, at the station, and he was brought by his guardians and not told he was free to leave. Given those "differing indications," the state court's no-custody conclusion fit within the Court's prior decisions and was not objectively unreasonable. The Ninth Circuit erred by treating the omission of Alvarado's age and inexperience as an unreasonable failure to extend clearly established law, when the Court's cases had never made those individual traits part of the objective custody test.

## Conclusion
The state court reasonably applied clearly established law; AEDPA barred relief. The judgment of the Court of Appeals was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- **Juvenile qualifier (field-relevant):** [[J.D.B. v. North Carolina]], 564 U.S. 261 (2011), held that a child's age **is** part of the Miranda custody analysis when it was known to the officer or objectively apparent. *[[J.D.B. v. North Carolina|J.D.B.]]* **distinguished** *Alvarado* as a deferential AEDPA holding that did not decide, on [[Common Legal Terms#de-novo|de novo]] review, whether age is categorically irrelevant. *Alvarado*'s objective-custody rule still governs adults; for juveniles, *[[J.D.B. v. North Carolina|J.D.B.]]* now requires accounting for age.
- The objective custody framework appears in [[California v. Beheler]] and [[Thompson v. Keohane]], in the [[Miranda v. Arizona]] line.

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Yarborough v. Alvarado*, 541 U.S. 652 (2004) — https://www.courtlistener.com/opinion/134748/yarborough-v-alvarado/ — pinpoints: 665, 666, 668.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "86116fd1dbce7d02", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "541 U.S. 652 (2004)", "court": "U.S. Supreme Court", "neutral_cite": "2004 U.S. LEXIS 3843", "official_citation_present": true, "parallel_cite": "124 S. Ct. 2140; 158 L. Ed. 2d 938", "title": "Yarborough v. Alvarado", "year": "2004"}}
{"assertion_id": "4adf1e7661e4591b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Because the Miranda custody test is objective and the Court's cases had not made a suspect's age or experience part of it, a state court's conclusion that a 17-year-old was not in custody was not an unreasonable application of clearly established federal law, and AEDPA barred habeas relief.", "title": "Yarborough v. Alvarado"}}
{"assertion_id": "cfb1577f4f08b820", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Progeny / Refinement", "title": "Yarborough v. Alvarado"}}
{"assertion_id": "8c6a6251bc802551", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2004-06-01", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Yarborough v. Alvarado", "field_i_validity": "good_law", "scope_note": "Good law; the Miranda custody test is objective and the Court's cases had not made a suspect's age/experience part of it, so a state court did not unreasonably apply clearly established law (AEDPA). Qualified for juveniles by J.D.B. v. North Carolina (2011): a child's age is part of the custody analysis when known to the officer or objectively apparent — J.D.B. distinguished Alvarado as an AEDPA-deference holding.", "title": "Yarborough v. Alvarado", "varies_by_point": "false"}}
{"assertion_id": "dc001a34cb830f58", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Yarborough v. Alvarado"}}
```

### lake record — Yarborough v. Alvarado

```json
{
  "schema_version": "s2.v1",
  "record_id": "Yarborough v. Alvarado",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Yarborough v. Alvarado",
    "case_name_short": "Yarborough",
    "case_name_full": "Yarborough, Warden v. Alvarado",
    "input_case_name": "Yarborough v. Alvarado",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-06-01",
    "year": 2004,
    "docket": "02-1684",
    "cluster_id": 134748,
    "lead_opinion_id": 134748,
    "sibling_ids": [
      134748,
      9434617,
      9434618,
      9434619
    ],
    "absolute_url": "/opinion/134748/yarborough-v-alvarado/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "541 U.S. 652",
      "volume": "541",
      "reporter": "U.S.",
      "page": "652",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "124 S. Ct. 2140",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2140",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "158 L. Ed. 2d 938",
        "volume": "158",
        "reporter": "L. Ed. 2d",
        "page": "938",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 3843",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "3843",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "541 U.S. 652",
        "volume": "541",
        "reporter": "U.S.",
        "page": "652",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 2140",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2140",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "158 L. Ed. 2d 938",
        "volume": "158",
        "reporter": "L. Ed. 2d",
        "page": "938",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 3843",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "3843",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "541 U.S. 652",
    "official_selection": {
      "court_class": "scotus",
      "selected": "541 U.S. 652",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-665",
      "page": null,
      "quote": "\u2014 made without considering his age and inexperience \u2014 was an unreasonable application of clearly established federal law warranting habeas relief under AEDPA. ## Rule No. Under AEDPA,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-666",
      "page": null,
      "quote": "Our opinions applying the *Miranda* custody test have not mentioned the suspect's age, much less mandated its consideration. The only indications in the Court's opinions relevant to a suspect's experience with law enforcement have rejected reliance on such factors.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-668",
      "page": null,
      "quote": "[T]he custody inquiry states an objective rule designed to give clear guidance to the police, while consideration of a suspect's individual characteristics \u2014 including his age \u2014 could be viewed as creating a subjective inquiry.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2004-06-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Yarborough v. Alvarado",
    "varies_by_point": false,
    "scope_note": "Good law; the Miranda custody test is objective and the Court's cases had not made a suspect's age/experience part of it, so a state court did not unreasonably apply clearly established law (AEDPA). Qualified for juveniles by J.D.B. v. North Carolina (2011): a child's age is part of the custody analysis when known to the officer or objectively apparent \u2014 J.D.B. distinguished Alvarado as an AEDPA-deference holding.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Evelyn",
          "cluster_id": 4786331,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hallford",
          "cluster_id": 4444995,
          "cite": [
            "280 F. Supp. 3d 170"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Harrington v. Richter",
          "cluster_id": 182992,
          "cite": [
            "178 L. Ed. 2d 624",
            "131 S. Ct. 770",
            "562 U.S. 86",
            "2011 U.S. LEXIS 912"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Knowles v. Mirzayance",
          "cluster_id": 145897,
          "cite": [
            "173 L. Ed. 2d 251",
            "129 S. Ct. 1411",
            "556 U.S. 111",
            "2009 U.S. LEXIS 2329"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "White v. Woodall",
          "cluster_id": 2670965,
          "cite": [
            "188 L. Ed. 2d 698",
            "134 S. Ct. 1697",
            "2014 U.S. LEXIS 2935",
            "82 U.S.L.W. 4288",
            "572 U.S. 415",
            "24 Fla. L. Weekly Fed. S 695",
            "2014 WL 1612424"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carey v. Musladin",
          "cluster_id": 145770,
          "cite": [
            "166 L. Ed. 2d 482",
            "127 S. Ct. 649",
            "549 U.S. 70",
            "2006 U.S. LEXIS 9587",
            "2006 WL 3542769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parker v. Matthews",
          "cluster_id": 801975,
          "cite": [
            "183 L. Ed. 2d 32",
            "132 S. Ct. 2148",
            "567 U.S. 37",
            "2012 U.S. LEXIS 4306"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. Ayala",
          "cluster_id": 2811849,
          "cite": [
            "576 U.S. 257",
            "135 S. Ct. 2187",
            "192 L. Ed. 2d 323",
            "2015 U.S. LEXIS 4059",
            "25 Fla. L. Weekly Fed. S 371",
            "83 U.S.L.W. 4470"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Howes v. Fields",
          "cluster_id": 623144,
          "cite": [
            "182 L. Ed. 2d 17",
            "132 S. Ct. 1181",
            "565 U.S. 499",
            "2012 U.S. LEXIS 1077",
            "2012 WL 538280"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marshall v. Rodgers",
          "cluster_id": 856791,
          "cite": [
            "185 L. Ed. 2d 540",
            "133 S. Ct. 1446",
            "569 U.S. 58",
            "2013 U.S. LEXIS 2546",
            "81 U.S.L.W. 4226",
            "24 Fla. L. Weekly Fed. S 131",
            "2013 WL 1285304"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donald Eugene Lambert v. James Blodgett, Donald Eugene Lambert v. James Blodgett",
          "cluster_id": 788795,
          "cite": [
            "393 F.3d 943",
            "2004 U.S. App. LEXIS 26895"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
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
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Davenport",
          "cluster_id": 6461473,
          "cite": [
            "596 U.S. 118",
            "142 S. Ct. 1510"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. Lafler",
          "cluster_id": 614567,
          "cite": [
            "658 F.3d 525",
            "2011 U.S. App. LEXIS 20036",
            "2011 WL 4537788"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Linton",
          "cluster_id": 944931,
          "cite": [
            "56 Cal. 4th 1146",
            "302 P.3d 927",
            "158 Cal. Rptr. 3d 521",
            "2013 WL 3214690",
            "2013 Cal. LEXIS 5338"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Juan H. v. Walter Allen III",
          "cluster_id": 790372,
          "cite": [
            "408 F.3d 1262"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Blystone v. Horn",
          "cluster_id": 619606,
          "cite": [
            "664 F.3d 397",
            "81 Fed. R. Serv. 3d 370",
            "2011 U.S. App. LEXIS 25553",
            "2011 WL 6598166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Murray v. Dora Schriro",
          "cluster_id": 2657481,
          "cite": [
            "745 F.3d 984",
            "2014 WL 997716",
            "2014 U.S. App. LEXIS 5002"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Abdul-Kabir v. Quarterman",
          "cluster_id": 145742,
          "cite": [
            "167 L. Ed. 2d 585",
            "127 S. Ct. 1654",
            "550 U.S. 233",
            "2007 U.S. LEXIS 4536"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Leonard",
          "cluster_id": 2632907,
          "cite": [
            "157 P.3d 973",
            "58 Cal. Rptr. 3d 368",
            "40 Cal. 4th 1370",
            "2007 Cal. Daily Op. Serv. 5424",
            "2007 Cal. LEXIS 5071"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shinn v. Kayer",
          "cluster_id": 4838846,
          "cite": [
            "592 U.S. 111",
            "208 L. Ed. 2d 353",
            "141 S. Ct. 517"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edwards v. Fischer",
          "cluster_id": 2451137,
          "cite": [
            "414 F. Supp. 2d 342",
            "2006 U.S. Dist. LEXIS 7195",
            "2006 WL 354317"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 1654613,
          "cite": [
            "760 N.W.2d 35",
            "277 Neb. 37"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Byrd v. Workman",
          "cluster_id": 217643,
          "cite": [
            "645 F.3d 1159",
            "2011 U.S. App. LEXIS 10678",
            "2011 WL 2084204"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lewis v. Zon",
          "cluster_id": 2309715,
          "cite": [
            "573 F. Supp. 2d 804",
            "2008 U.S. Dist. LEXIS 66064",
            "2008 WL 4006780"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stanley v. Cullen",
          "cluster_id": 183944,
          "cite": [
            "633 F.3d 852",
            "2011 WL 285218"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Yarborough v. Alvarado:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(134748 OR 9434617 OR 9434618 OR 9434619) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTA1MjYwODAwMDAwJnM9NDQyNTg3MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28134748+OR+9434617+OR+9434618+OR+9434619%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 2,
        "triage_snippet_classified": 198
      },
      "lane2_top_cited": {
        "query": "cites:(134748 OR 9434617 OR 9434618 OR 9434619)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjkmcz0yMjMxOTA1JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28134748+OR+9434617+OR+9434618+OR+9434619%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(134748 OR 9434617 OR 9434618 OR 9434619)",
        "reviewed": 54,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 54,
        "triage_read": 0,
        "triage_snippet_classified": 54
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(134748 OR 9434617 OR 9434618 OR 9434619)",
    "indexed_citing_opinions": 911,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 134748,
        "count": 729,
        "count_source": "search"
      },
      {
        "opinion_id": 9434617,
        "count": 195,
        "count_source": "search"
      },
      {
        "opinion_id": 9434618,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434619,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3547,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/yarborough-v-alvarado.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxODIxNDQmcz0xMDMyMDczMiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28134748+OR+9434617+OR+9434618+OR+9434619%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 134748,
        "cited_id": 76066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 107439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 109587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 111023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 111198,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 112206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 112771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 117843,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 117982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 122243,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 127898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 127919,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 145122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 771619,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 780555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134748,
        "cited_id": 2248648,
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
    "date_created": "2026-07-06T04:50:52Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:51:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:51:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:55:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:51:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Yarborough v. Alvarado

```
<div>
<center><b><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S. 652</a></span> (2004)</b></center>
<center><h1>YARBOROUGH, WARDEN<br>
v.<br>
ALVARADO</h1></center>
<center>No. 02-1684.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 1, 2004.</center>
<center>Decided June 1, 2004.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><span class="star-pagination">*653</span> <span class="star-pagination">*654</span> KENNEDY, J., delivered the opinion of the Court, in which REHNQUIST, C. J., and O'CONNOR, SCALIA, and THOMAS, JJ., joined. O'CONNOR, J., filed a concurring opinion, <i>post,</i> p. 669. BREYER, J., filed a dissenting opinion, in which STEVENS, SOUTER, and GINSBURG, JJ., joined, <i>post,</i> p. 669.</p>
<p><i>Deborah Jane Chuang,</i> Deputy Attorney General of California, argued the cause for petitioner. With her on the <span class="star-pagination">*655</span> briefs were <i>Bill Lockyer,</i> Attorney General, <i>Manuel M. Medeiros,</i> State Solicitor General, <i>Robert R. Anderson,</i> Chief Assistant Attorney General, <i>Pamela C. Hamanaka,</i> Senior Assistant Attorney General, <i>Donald E. De Nicola,</i> Deputy Attorney General, and <i>Kenneth C. Byrne,</i> Supervising Deputy Attorney General.</p>
<p><i>John P. Elwood</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Olson, Assistant Attorney General Wray, Deputy Solicitor General Dreeben,</i> and <i>Deborah Watson.</i></p>
<p><i>Tara K. Allen,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./540/1043/">540 U. S. 1043</a></span>, argued the cause for respondent. With her on the briefs were <i>Thomas J. Phalen</i> and <i>John H. Blume.</i><sup>[*]</sup></p>
<p>JUSTICE KENNEDY delivered the opinion of the Court.</p>
<p>Under the Antiterrorism and Effective Death Penalty Act of 1996 (AEDPA), <span class="citation no-link">110 Stat. 1214</span>, a federal court can grant an application for a writ of habeas corpus on behalf of a person held pursuant to a state-court judgment if the state-court adjudication "resulted in a decision that was contrary to, or involved an unreasonable application of, clearly established Federal law, as determined by the Supreme Court of the United States." <span class="citation no-link">28 U. S. C. § 2254</span>(d)(1). The United States Court of Appeals for the Ninth Circuit ruled that a state court unreasonably applied clearly established law when it held that the respondent was not in custody for <i>Miranda</i> purposes. <i>Alvarado</i> v. <i>Hickman,</i> <span class="citation" data-id="780555"><a href="/opinion/780555/michael-alvarado-v-rq-hickman-warden-acting-warden-of-mule-creek-state/" aria-description="Citation for case: Michael Alvarado v. R.Q. Hickman, Warden, Acting Warden...">316 F. 3d 841</a></span> (2002). We disagree and reverse.</p>
<p></p>
<h2>I</h2>
<p>Paul Soto and respondent Michael Alvarado attempted to steal a truck in the parking lot of a shopping mall in Santa <span class="star-pagination">*656</span> Fe Springs, California. Soto and Alvarado were part of a larger group of teenagers at the mall that night. Soto decided to steal the truck, and Alvarado agreed to help. Soto pulled out a .357 Magnum and approached the driver, Francisco Castaneda, who was standing near the truck emptying trash into a dumpster. Soto demanded money and the ignition keys from Castaneda. Alvarado, then five months short of his 18th birthday, approached the passenger side door of the truck and crouched down. When Castaneda refused to comply with Soto's demands, Soto shot Castaneda, killing him. Alvarado then helped hide Soto's gun.</p>
<p>Los Angeles County Sheriff's detective Cheryl Comstock led the investigation into the circumstances of Castaneda's death. About a month after the shooting, Comstock left word at Alvarado's house and also contacted Alvarado's mother at work with the message that she wished to speak with Alvarado. Alvarado's parents brought him to the Pico Rivera Sheriff's Station to be interviewed around lunchtime. They waited in the lobby while Alvarado went with Comstock to be interviewed. Alvarado contends that his parents asked to be present during the interview but were rebuffed.</p>
<p>Comstock brought Alvarado to a small interview room and began interviewing him at about 12:30 p.m. The interview lasted about two hours, and was recorded by Comstock with Alvarado's knowledge. Only Comstock and Alvarado were present. Alvarado was not given a warning under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Comstock began the interview by asking Alvarado to recount the events on the night of the shooting. On that night, Alvarado explained, he had been drinking alcohol at a friend's house with some other friends and acquaintances. After a few hours, part of the group went home and the rest walked to a nearby mall to use its public telephones. In Alvarado's initial telling, that was the end of it. The group went back to the friend's home and "just went to bed." App. 101.</p>
<p>Unpersuaded, Comstock pressed on:</p>
<blockquote>
<span class="star-pagination">*657</span> "Q. Okay. We did real good up until this point and everything you've said it's pretty accurate till this point, except for you left out the shooting.</blockquote>
<blockquote>"A. The shooting?</blockquote>
<blockquote>"Q. Uh huh, the shooting.</blockquote>
<blockquote>"A. Well I had never seen no shooting.</blockquote>
<blockquote>"Q. Well I'm afraid you did.</blockquote>
<blockquote>"A. I had never seen no shooting.</blockquote>
<blockquote>"Q. Well I beg to differ with you. I've been told quite the opposite and we have witnesses that are saying quite the opposite.</blockquote>
<blockquote>"A. That I had seen the shooting?</blockquote>
<blockquote>"Q. So why don't you take a deep breath, like I told you before, the very best thing is to be honest. . . . You can't have that many people get involved in a murder and expect that some of them aren't going to tell the truth, okay? Now granted if it was maybe one person, you might be able to keep your fingers crossed and say, god I hope he doesn't tell the truth, but the problem is is that they have to tell the truth, okay? Now all I'm simply doing is giving you the opportunity to tell the truth and when we got that many people telling a story and all of a sudden you tell something way far fetched different." <i>Id.,</i> at 101-102 (punctuation added).</blockquote>
<p>At this point, Alvarado slowly began to change his story. First he acknowledged being present when the carjacking occurred but claimed that he did not know what happened or who had a gun. When he hesitated to say more, Comstock tried to encourage Alvarado to discuss what happened by appealing to his sense of honesty and the need to bring the man who shot Castaneda to justice. See, <i>e. g., id.,</i> at 106 ("[W]hat I'm looking for is to see if you'll tell the truth"); <i>id.,</i> at 105-106 ("I know it's very difficult when it comes time to `drop the dime' on somebody[,] . . . [but] if that had been <span class="star-pagination">*658</span> your parent, your mother, or your brother, or your sister, you would darn well want [the killer] to go to jail `cause no one has the right to take someone's life like that . . ."). Alvarado then admitted he had helped the other man try to steal the truck by standing near the passenger side door. Next he admitted that the other man was Paul Soto, that he knew Soto was armed, and that he had helped hide the gun after the murder. Alvarado explained that he had expected Soto to scare the driver with the gun, but that he did not expect Soto to kill anyone. <i>Id.,</i> at 127. Toward the end of the interview, Comstock twice asked Alvarado if he needed to take a break. Alvarado declined. When the interview was over, Comstock returned with Alvarado to the lobby of the sheriff's station where his parents were waiting. Alvarado's father drove him home.</p>
<p>A few months later, the State of California charged Soto and Alvarado with first-degree murder and attempted robbery. Citing <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda, supra,</a></span></i> Alvarado moved to suppress his statements from the Comstock interview. The trial court denied the motion on the ground that the interview was noncustodial. App. 196. Alvarado and Soto were tried together, and Alvarado testified in his own defense. He offered an innocent explanation for his conduct, testifying that he happened to be standing in the parking lot of the mall when a gun went off nearby. The government's cross-examination relied on Alvarado's statement to Comstock. Alvarado admitted having made some of the statements but denied others. When Alvarado denied particular statements, the prosecution countered by playing excerpts from the audio recording of the interview.</p>
<p>During cross-examination, Alvarado agreed that the interview with Comstock "was a pretty friendly conversation," <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#438" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 438</a></span>, that there was "sort of a free flow between [Alvarado] and Detective Comstock," <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#439" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 439</a></span>, and that Alvarado did not "feel coerced or threatened in any way" during the interview, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">ibid.</a></span></i> The jury convicted Soto and Alvarado of first-degree murder and attempted robbery. The <span class="star-pagination">*659</span> trial judge later reduced Alvarado's conviction to second-degree murder for his comparatively minor role in the offense. The judge sentenced Soto to life in prison and Alvarado to 15-years-to-life.</p>
<p>On direct appeal, the Second Appellate District Court of Appeal (hereinafter state court) affirmed. <i>People</i> v. <i>Soto,</i> <span class="citation" data-id="2248648"><a href="/opinion/2248648/people-v-soto/" aria-description="Citation for case: People v. Soto">74 Cal. App. 4th 1099</a></span>, <span class="citation" data-id="2248648"><a href="/opinion/2248648/people-v-soto/" aria-description="Citation for case: People v. Soto">88 Cal. Rptr. 2d 688</a></span> (1999) (unpublished in relevant part). The state court rejected Alvarado's contention that his statements to Comstock should have been excluded at trial because no <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings were given. The court ruled Alvarado had not been in custody during the interview, so no warning was required. The state court relied upon the custody test articulated in <i>Thompson</i> v. <i>Keohane,</i> <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/#112" aria-description="Citation for case: Thompson v. Keohane">516 U. S. 99, 112</a></span> (1995), which requires a court to consider the circumstances surrounding the interrogation and then determine whether a reasonable person would have felt at liberty to leave. The state court reviewed the facts of the Comstock interview and concluded Alvarado was not in custody. App. to Pet. for Cert. C-17. The court emphasized the absence of any intense or aggressive tactics and noted that Comstock had not told Alvarado that he could not leave. The California Supreme Court denied discretionary review.</p>
<p>Alvarado filed a petition for a writ of habeas corpus in the United States District Court for the Central District of California. The District Court agreed with the state court that Alvarado was not in custody for <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> purposes during the interview. <i>Alvarado</i> v. <i><span class="citation" data-id="780555"><a href="/opinion/780555/michael-alvarado-v-rq-hickman-warden-acting-warden-of-mule-creek-state/" aria-description="Citation for case: Michael Alvarado v. R.Q. Hickman, Warden, Acting Warden...">Hickman</a></span>,</i> No. ED CV-00-326-VAP(E) (2000), App. to Pet. for Cert. B-1 to B-10. "At a minimum," the District Court added, the deferential standard of review provided by <span class="citation no-link">28 U. S. C. § 2254</span>(d) foreclosed relief. App. to Pet. for Cert. B-7.</p>
<p>The Court of Appeals for the Ninth Circuit reversed. <i>Alvarado</i> v. <i>Hickman,</i> <span class="citation" data-id="780555"><a href="/opinion/780555/michael-alvarado-v-rq-hickman-warden-acting-warden-of-mule-creek-state/" aria-description="Citation for case: Michael Alvarado v. R.Q. Hickman, Warden, Acting Warden...">316 F. 3d 841</a></span> (2002). First, the Court of Appeals held that the state court erred in failing to account for Alvarado's youth and inexperience when evaluating whether a reasonable person in his position would have felt <span class="star-pagination">*660</span> free to leave. It noted that this Court has considered a suspect's juvenile status when evaluating the voluntariness of confessions and the waiver of the privilege against self-incrimination. See <i><span class="citation" data-id="780555"><a href="/opinion/780555/michael-alvarado-v-rq-hickman-warden-acting-warden-of-mule-creek-state/" aria-description="Citation for case: Michael Alvarado v. R.Q. Hickman, Warden, Acting Warden...">id.,</a></span></i> at 843 (citing, <i>inter alia, </i><i>Haley</i> v. <i>Ohio,</i> <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/#599" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596, 599-601</a></span> (1948), and <i>In re Gault,</i> <span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/#45" aria-description="Citation for case: In Re GAULT">387 U. S. 1, 45</a></span> (1967)). The Court of Appeals held that in light of these authorities, Alvarado's age and experience must be a factor in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> custody inquiry. <span class="citation" data-id="780555"><a href="/opinion/780555/michael-alvarado-v-rq-hickman-warden-acting-warden-of-mule-creek-state/#843" aria-description="Citation for case: Michael Alvarado v. R.Q. Hickman, Warden, Acting Warden...">316 F. 3d, at 843</a></span>. A minor with no criminal record would be more likely to feel coerced by police tactics and conclude he is under arrest than would an experienced adult, the Court of Appeals reasoned. This required extra "safeguards . . . commensurate with the age and circumstances of a juvenile defendant." See <span class="citation" data-id="780555"><a href="/opinion/780555/michael-alvarado-v-rq-hickman-warden-acting-warden-of-mule-creek-state/#850" aria-description="Citation for case: Michael Alvarado v. R.Q. Hickman, Warden, Acting Warden..."><i>id.,</i> at 850</a></span>. According to the Court of Appeals, the effect of Alvarado's age and inexperience was so substantial that it turned the interview into a custodial interrogation.</p>
<p>The Court of Appeals next considered whether Alvarado could obtain relief in light of the deference a federal court must give to a state-court determination on habeas review. The deference required by AEDPA did not bar relief, the Court of Appeals held, because the relevance of juvenile status in Supreme Court case law as a whole compelled the "extension of the principle that juvenile status is relevant" to the context of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> custody determinations. <span class="citation" data-id="780555"><a href="/opinion/780555/michael-alvarado-v-rq-hickman-warden-acting-warden-of-mule-creek-state/#853" aria-description="Citation for case: Michael Alvarado v. R.Q. Hickman, Warden, Acting Warden...">316 F. 3d, at 853</a></span>. In light of the clearly established law considering juvenile status, it was "simply unreasonable to conclude that a reasonable 17-year-old, with no prior history of arrest or police interviews, would have felt that he was at liberty to terminate the interrogation and leave." <span class="citation" data-id="780555"><a href="/opinion/780555/michael-alvarado-v-rq-hickman-warden-acting-warden-of-mule-creek-state/#854" aria-description="Citation for case: Michael Alvarado v. R.Q. Hickman, Warden, Acting Warden..."><i>Id.,</i> at 854-855</a></span> (internal quotation marks omitted).</p>
<p>We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./539/986/">539 U. S. 986</a></span> (2003).</p>
<p></p>
<h2>II</h2>
<p>We begin by determining the relevant clearly established law. For purposes of <span class="citation no-link">28 U. S. C. § 2254</span>(d)(1), clearly established law as determined by this Court "refers to the holdings, as opposed to the dicta, of this Court's decisions as of <span class="star-pagination">*661</span> the time of the relevant state-court decision." <i>Williams</i> v. <i>Taylor,</i> <span class="citation" data-id="9434817"><a href="/opinion/145122/williams-v-taylor/#412" aria-description="Citation for case: Williams v. Taylor">529 U. S. 362, 412</a></span> (2000). We look for "the governing legal principle or principles set forth by the Supreme Court at the time the state court renders its decision." <i>Lockyer</i> v. <i>Andrade,</i> <span class="citation" data-id="9434390"><a href="/opinion/127898/lockyer-v-andrade/#71" aria-description="Citation for case: Lockyer v. Andrade">538 U. S. 63, 71-72</a></span> (2003).</p>
<p><i>Miranda</i> itself held that preinterrogation warnings are required in the context of custodial interrogations given "the compulsion inherent in custodial surroundings." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#458" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 458</a></span>. The Court explained that "custodial interrogation" meant "questioning initiated by law enforcement officers after a person has been taken into custody or otherwise deprived of his freedom of action in any significant way." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 444</a></span>. The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> decision did not provide the Court with an opportunity to apply that test to a set of facts.</p>
<p>After <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the Court first applied the custody test in <i>Oregon</i> v. <i>Mathiason,</i> <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">429 U. S. 492</a></span> (1977) <i>(per curiam)</i><i>.</i> In <i><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">Mathiason</a></span>,</i> a police officer contacted the suspect after a burglary victim identified him. The officer arranged to meet the suspect at a nearby police station. At the outset of the questioning, the officer stated his belief that the suspect was involved in the burglary but that he was not under arrest. During the 30-minute interview, the suspect admitted his guilt. He was then allowed to leave. The Court held that the questioning was not custodial because there was "no indication that the questioning took place in a context where [the suspect's] freedom to depart was restricted in any way." <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason"><i>Id.,</i> at 495</a></span>. The Court noted that the suspect had come voluntarily to the police station, that he was informed that he was not under arrest, and that he was allowed to leave at the end of the interview. <i><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">Ibid.</a></span></i></p>
<p>In <i>California</i> v. <i>Beheler,</i> <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/" aria-description="Citation for case: California v. Beheler">463 U. S. 1121</a></span> (1983) <i>(per curiam)</i><i>,</i> the Court reached the same result in a case with facts similar to those in <i><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">Mathiason</a></span>.</i> In <i><span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/" aria-description="Citation for case: California v. Beheler">Beheler</a></span>,</i> the state court had distinguished <i><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">Mathiason</a></span></i> based on what it described as differences in the totality of the circumstances. The police interviewed Beheler shortly after the crime occurred; Beheler had been drinking earlier in the day; he was emotionally <span class="star-pagination">*662</span> distraught; he was well known to the police; and he was a parolee who knew it was necessary for him to cooperate with the police. <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1124" aria-description="Citation for case: California v. Beheler">463 U. S., at 1124-1125</a></span>. The Court agreed that "the circumstances of each case must certainly influence" the custody determination, but reemphasized that "the ultimate inquiry is simply whether there is a formal arrest or restraint on freedom of movement of the degree associated with a formal arrest." <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1125" aria-description="Citation for case: California v. Beheler"><i>Id.,</i> at 1125</a></span> (internal quotation marks omitted). The Court found the case indistinguishable from <i><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">Mathiason</a></span>.</i> It noted that how much the police knew about the suspect and how much time had elapsed after the crime occurred were irrelevant to the custody inquiry. <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1125" aria-description="Citation for case: California v. Beheler">463 U. S., at 1125</a></span>.</p>
<p>Our more recent cases instruct that custody must be determined based on how a reasonable person in the suspect's situation would perceive his circumstances. In <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420</a></span> (1984), a police officer stopped a suspected drunk driver and asked him some questions. Although the officer reached the decision to arrest the driver at the beginning of the traffic stop, he did not do so until the driver failed a sobriety test and acknowledged that he had been drinking beer and smoking marijuana. The Court held the traffic stop noncustodial despite the officer's intent to arrest because he had not communicated that intent to the driver. "A policeman's unarticulated plan has no bearing on the question whether a suspect was `in custody' at a particular time," the Court explained. <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#442" aria-description="Citation for case: Berkemer v. McCarty"><i>Id.,</i> at 442</a></span>. "[T]he only relevant inquiry is how a reasonable man in the suspect's position would have understood his situation." <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Ibid.</a></span></i> In a footnote, the Court cited a New York state case for the view that an objective test was preferable to a subjective test in part because it does not "`place upon the police the burden of anticipating the frailties or idiosyncrasies of every person whom they question.'" <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#442" aria-description="Citation for case: Berkemer v. McCarty"><i>Id.,</i> at 442</a></span>, n. 35 (quoting <i>People</i> v. <i>P.,</i> 21 N. Y. 2d 1, 9-10, <span class="citation" data-id="9787785"><a href="/opinion/2590535/people-v-rodney-panonymous/#260" aria-description="Citation for case: People v. Rodney P.(Anonymous)">233 N. E. 2d 255, 260</a></span> (1967)).</p>
<p><span class="star-pagination">*663</span> <i>Stansbury</i> v. <i>California,</i> <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">511 U. S. 318</a></span> (1994) <i>(per curiam)</i><i>,</i> confirmed this analytical framework. <i><span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">Stansbury</a></span></i> explained that "the initial determination of custody depends on the objective circumstances of the interrogation, not on the subjective views harbored by either the interrogating officers or the person being questioned." <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#323" aria-description="Citation for case: Stansbury v. California"><i>Id.,</i> at 323</a></span>. Courts must examine "all of the circumstances surrounding the interrogation" and determine "how a reasonable person in the position of the individual being questioned would gauge the breadth of his or her freedom of action." <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#322" aria-description="Citation for case: Stansbury v. California"><i>Id.,</i> at 322, 325</a></span> (internal quotation marks and alteration omitted).</p>
<p>Finally, in <i>Thompson</i> v. <i>Keohane,</i> <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/" aria-description="Citation for case: Thompson v. Keohane">516 U. S. 99</a></span> (1995), the Court offered the following description of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> custody test:</p>
<blockquote>"Two discrete inquiries are essential to the determination: first, what were the circumstances surrounding the interrogation; and second, given those circumstances, would a reasonable person have felt he or she was not at liberty to terminate the interrogation and leave. Once the scene is set and the players' lines and actions are reconstructed, the court must apply an objective test to resolve the ultimate inquiry: was there a formal arrest or restraint on freedom of movement of the degree associated with a formal arrest." <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/#112" aria-description="Citation for case: Thompson v. Keohane">516 U. S., at 112</a></span> (internal quotation marks and footnote omitted).</blockquote>
<p>We turn now to the case before us and ask if the state-court adjudication of the claim "involved an unreasonable application" of clearly established law when it concluded that Alvarado was not in custody. <span class="citation no-link">28 U. S. C. § 2254</span>(d)(1). See <i>Williams,</i> <span class="citation" data-id="9434817"><a href="/opinion/145122/williams-v-taylor/#413" aria-description="Citation for case: Williams v. Taylor">529 U. S., at 413</a></span> ("Under the `unreasonable application' clause, a federal habeas court may grant the writ if the state court identifies the correct governing principle from this Court's decisions but unreasonably applies that principle to the facts of the prisoner's case"). The term "`unreasonable'" is "a common term in the legal world and, <span class="star-pagination">*664</span> accordingly, federal judges are familiar with its meaning." <span class="citation" data-id="9434817"><a href="/opinion/145122/williams-v-taylor/#410" aria-description="Citation for case: Williams v. Taylor"><i>Id.,</i> at 410</a></span>. At the same time, the range of reasonable judgment can depend in part on the nature of the relevant rule. If a legal rule is specific, the range may be narrow. Applications of the rule may be plainly correct or incorrect. Other rules are more general, and their meaning must emerge in application over the course of time. Applying a general standard to a specific case can demand a substantial element of judgment. As a result, evaluating whether a rule application was unreasonable requires considering the rule's specificity. The more general the rule, the more leeway courts have in reaching outcomes in case-by-case determinations. Cf. <i>Wright</i> v. <i>West,</i> <span class="citation" data-id="9432630"><a href="/opinion/112771/wright-v-west/#308" aria-description="Citation for case: Wright v. West">505 U. S. 277, 308-309</a></span> (1992) (KENNEDY, J., concurring in judgment).</p>
<p>Based on these principles, we conclude that the state court's application of our clearly established law was reasonable. Ignoring the deferential standard of § 2254(d)(1) for the moment, it can be said that fairminded jurists could disagree over whether Alvarado was in custody. On one hand, certain facts weigh against a finding that Alvarado was in custody. The police did not transport Alvarado to the station or require him to appear at a particular time. Cf. <i>Mathiason,</i> <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S., at 495</a></span>. They did not threaten him or suggest he would be placed under arrest. <i><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">Ibid.</a></span></i> Alvarado's parents remained in the lobby during the interview, suggesting that the interview would be brief. See <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#441" aria-description="Citation for case: Berkemer v. McCarty"><i>Berkemer, supra,</i> at 441-442</a></span>. In fact, according to trial counsel for Alvarado, he and his parents were told that the interview was "`not going to be long.'" App. 186. During the interview, Comstock focused on Soto's crimes rather than Alvarado's. Instead of pressuring Alvarado with the threat of arrest and prosecution, she appealed to his interest in telling the truth and being helpful to a police officer. Cf. <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason"><i>Mathiason, supra,</i> at 495</a></span>. In addition, Comstock twice asked Alvarado if he wanted to take a break. At the end of the interview, Alvarado went home. App. 186. All of these objective <span class="star-pagination">*665</span> facts are consistent with an interrogation environment in which a reasonable person would have felt free to terminate the interview and leave. Indeed, a number of the facts echo those of <i><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">Mathiason</a></span>,</i> a <i>per curiam</i> summary reversal in which we found it "clear from these facts" that the suspect was not in custody. 494 U. S., at 495.</p>
<p>Other facts point in the opposite direction. Comstock interviewed Alvarado at the police station. The interview lasted two hours, four times longer than the 30-minute interview in <i><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">Mathiason</a></span>.</i> Unlike the officer in <i><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">Mathiason</a></span>,</i> Comstock did not tell Alvarado that he was free to leave. Alvarado was brought to the police station by his legal guardians rather than arriving on his own accord, making the extent of his control over his presence unclear. Counsel for Alvarado alleges that Alvarado's parents asked to be present at the interview but were rebuffed, a fact that  if known to Alvarado  might reasonably have led someone in Alvarado's position to feel more restricted than otherwise. These facts weigh in favor of the view that Alvarado was in custody.</p>
<p>These differing indications lead us to hold that the state court's application of our custody standard was reasonable. The Court of Appeals was nowhere close to the mark when it concluded otherwise. Although the question of what an "unreasonable application" of law might be is difficult in some cases, it is not difficult here. The custody test is general, and the state court's application of our law fits within the matrix of our prior decisions. We cannot grant relief under AEDPA by conducting our own independent inquiry into whether the state court was correct as a <i>de novo</i> matter. "[A] federal habeas court may not issue the writ simply because that court concludes in its independent judgment that the state-court decision applied [the law] incorrectly." <i>Woodford</i> v. <i>Visciotti,</i> <span class="citation" data-id="122243"><a href="/opinion/122243/woodford-v-visciotti/#24" aria-description="Citation for case: Woodford v. Visciotti">537 U. S. 19, 24-25</a></span> (2002) <i>(per curiam)</i><i>.</i> Relief is available under § 2254(d)(1) only if the state court's decision is objectively unreasonable. See <i>Williams,</i> <span class="star-pagination">*666</span> <span class="citation" data-id="9434817"><a href="/opinion/145122/williams-v-taylor/#410" aria-description="Citation for case: Williams v. Taylor">529 U. S., at 410</a></span>; <i>Andrade,</i> <span class="citation" data-id="9434390"><a href="/opinion/127898/lockyer-v-andrade/#75" aria-description="Citation for case: Lockyer v. Andrade">538 U. S., at 75</a></span>. Under that standard, relief cannot be granted.</p>
<p></p>
<h2>III</h2>
<p>The Court of Appeals reached the opposite result by placing considerable reliance on Alvarado's age and inexperience with law enforcement. Our Court has not stated that a suspect's age or experience is relevant to the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> custody analysis, and counsel for Alvarado did not press the importance of either factor on direct appeal or in habeas proceedings. According to the Court of Appeals, however, our Court's emphasis on juvenile status in other contexts demanded consideration of Alvarado's age and inexperience here. The Court of Appeals viewed the state court's failure to "`extend a clearly established legal principle [of the relevance of juvenile status] to a new context'" as objectively unreasonable in this case, requiring issuance of the writ. <span class="citation" data-id="780555"><a href="/opinion/780555/michael-alvarado-v-rq-hickman-warden-acting-warden-of-mule-creek-state/" aria-description="Citation for case: Michael Alvarado v. R.Q. Hickman, Warden, Acting Warden...">316 F. 3d, at 853</a></span> (quoting <i>Anthony</i> v. <i>Cambra,</i> <span class="citation" data-id="9493702"><a href="/opinion/771619/michael-anthony-v-steven-cambra-jr-warden/#578" aria-description="Citation for case: Michael Anthony v. Steven Cambra, Jr., Warden">236 F. 3d 568, 578</a></span> (CA9 2000)).</p>
<p>The petitioner contends that if a habeas court must extend a rationale before it can apply to the facts at hand then the rationale cannot be clearly established at the time of the state-court decision. Brief for Petitioner 10-24. See also <i>Hawkins</i> v. <i>Alabama,</i> <span class="citation" data-id="76066"><a href="/opinion/76066/weaver-lee-hawkins-iv-v-state-of-alabama/#1306" aria-description="Citation for case: Weaver Lee Hawkins, IV v. State of Alabama">318 F. 3d 1302, 1306, n. 3</a></span> (CA11 2003) (asserting a similar argument). There is force to this argument. Section 2254(d)(1) would be undermined if habeas courts introduced rules not clearly established under the guise of extensions to existing law. Cf. <i>Teague</i> v. <i>Lane,</i> <span class="citation" data-id="9431581"><a href="/opinion/112206/teague-v-lane/" aria-description="Citation for case: Teague v. Lane">489 U. S. 288</a></span> (1989). At the same time, the difference between applying a rule and extending it is not always clear. Certain principles are fundamental enough that when new factual permutations arise, the necessity to apply the earlier rule will be beyond doubt.</p>
<p>This is not such a case, however. Our opinions applying the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> custody test have not mentioned the suspect's age, much less mandated its consideration. The only indications <span class="star-pagination">*667</span> in the Court's opinions relevant to a suspect's experience with law enforcement have rejected reliance on such factors. See <i>Beheler,</i> <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1125" aria-description="Citation for case: California v. Beheler">463 U. S., at 1125</a></span> (rejecting a lower court's view that the defendant's prior interview with the police was relevant to the custody inquiry); <i>Berkemer,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#442" aria-description="Citation for case: Berkemer v. McCarty">468 U. S., at 442</a></span>, n. 35 (citing <i>People</i> v. <i>P.,</i> 21 N. Y. 2d, at 9-10, <span class="citation" data-id="9787785"><a href="/opinion/2590535/people-v-rodney-panonymous/#260" aria-description="Citation for case: People v. Rodney P.(Anonymous)">233 N. E. 2d, at 260</a></span>, which noted the difficulties of a subjective test that would require police to "`anticipat[e] the frailties or idiosyncrasies of every person whom they question'"); <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#430" aria-description="Citation for case: Berkemer v. McCarty">468 U. S., at 430-432</a></span> (describing a suspect's criminal past and police record as a circumstance "unknowable to the police").</p>
<p>There is an important conceptual difference between the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> custody test and the line of cases from other contexts considering age and experience. The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> custody inquiry is an objective test. As we stated in <i><span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/" aria-description="Citation for case: Thompson v. Keohane">Keohane</a></span>,</i> "[o]nce the scene is set and the players' lines and actions are reconstructed, the court must apply an objective test to resolve the ultimate inquiry." <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/#112" aria-description="Citation for case: Thompson v. Keohane">516 U. S., at 112</a></span> (internal quotation marks omitted). The objective test furthers "the clarity of [<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span>'s] rule," <i>Berkemer,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#430" aria-description="Citation for case: Berkemer v. McCarty">468 U. S., at 430</a></span>, ensuring that the police do not need "to make guesses as to [the circumstances] at issue before deciding how they may interrogate the suspect," <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#431" aria-description="Citation for case: Berkemer v. McCarty"><i>id.,</i> at 431</a></span>. To be sure, the line between permissible objective facts and impermissible subjective experiences can be indistinct in some cases. It is possible to subsume a subjective factor into an objective test by making the latter more specific in its formulation. Thus the Court of Appeals styled its inquiry as an objective test by considering what a "reasonable 17-year-old, with no prior history of arrest or police interviews," would perceive. <span class="citation" data-id="780555"><a href="/opinion/780555/michael-alvarado-v-rq-hickman-warden-acting-warden-of-mule-creek-state/#854" aria-description="Citation for case: Michael Alvarado v. R.Q. Hickman, Warden, Acting Warden...">316 F. 3d, at 854-855</a></span> (case below).</p>
<p>At the same time, the objective <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> custody inquiry could reasonably be viewed as different from doctrinal tests that depend on the actual mindset of a particular suspect, where we do consider a suspect's age and experience. For example, the voluntariness of a statement is often said to <span class="star-pagination">*668</span> depend on whether "the defendant's will was overborne," <i>Lynumn</i> v. <i>Illinois,</i> <span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/#534" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528, 534</a></span> (1963), a question that logically can depend on "the characteristics of the accused," <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 226</a></span> (1973). The characteristics of the accused can include the suspect's age, education, and intelligence, see <i>ibid.,</i> as well as a suspect's prior experience with law enforcement, see <span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/#534" aria-description="Citation for case: Lynumn v. Illinois"><i>Lynumn, supra,</i> at 534</a></span>. In concluding that there was "no principled reason" why such factors should not also apply to the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> custody inquiry, <span class="citation" data-id="780555"><a href="/opinion/780555/michael-alvarado-v-rq-hickman-warden-acting-warden-of-mule-creek-state/#850" aria-description="Citation for case: Michael Alvarado v. R.Q. Hickman, Warden, Acting Warden...">316 F. 3d, at 850</a></span>, the Court of Appeals ignored the argument that the custody inquiry states an objective rule designed to give clear guidance to the police, while consideration of a suspect's individual characteristics  including his age  could be viewed as creating a subjective inquiry. Cf. <i>Mathiason,</i> <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S., at 495-496</a></span> (noting that facts arguably relevant to whether an environment is coercive may have "nothing to do with whether respondent was in custody for purposes of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule"). For these reasons, the state court's failure to consider Alvarado's age does not provide a proper basis for finding that the state court's decision was an unreasonable application of clearly established law.</p>
<p>Indeed, reliance on Alvarado's prior history with law enforcement was improper not only under the deferential standard of <span class="citation no-link">28 U. S. C. § 2254</span>(d)(1), but also as a <i>de novo</i> matter. In most cases, police officers will not know a suspect's interrogation history. See <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#430" aria-description="Citation for case: Berkemer v. McCarty"><i>Berkemer, supra,</i> at 430-431</a></span>. Even if they do, the relationship between a suspect's past experiences and the likelihood a reasonable person with that experience would feel free to leave often will be speculative. True, suspects with prior law enforcement experience may understand police procedures and reasonably feel free to leave unless told otherwise. On the other hand, they may view past as prologue and expect another in a string of arrests. We do not ask police officers to consider these contingent psychological factors when deciding when suspects should be advised of their <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. See <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span>,</i> <span class="star-pagination">*669</span> <i>supra,</i> at 431-432. The inquiry turns too much on the suspect's subjective state of mind and not enough on the "objective circumstances of the interrogation." <i>Stansbury,</i> <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#323" aria-description="Citation for case: Stansbury v. California">511 U. S., at 323</a></span>.</p>
<p>The state court considered the proper factors and reached a reasonable conclusion. The judgment of the Court of Appeals is</p>
<p><i>Reversed.</i></p>
<p>JUSTICE O'CONNOR, concurring.</p>
<p>I join the opinion of the Court, but write separately to express an additional reason for reversal. There may be cases in which a suspect's age will be relevant to the "custody" inquiry under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). In this case, however, Alvarado was almost 18 years old at the time of his interview. It is difficult to expect police to recognize that a suspect is a juvenile when he is so close to the age of majority. Even when police do know a suspect's age, it may be difficult for them to ascertain what bearing it has on the likelihood that the suspect would feel free to leave. That is especially true here; 17½-year-olds vary widely in their reactions to police questioning, and many can be expected to behave as adults. Given these difficulties, I agree that the state court's decision in this case cannot be called an unreasonable application of federal law simply because it failed explicitly to mention Alvarado's age.</p>
<p>JUSTICE BREYER, with whom JUSTICE STEVENS, JUSTICE SOUTER, and JUSTICE GINSBURG join, dissenting.</p>
<p>In my view, Michael Alvarado clearly was "in custody" when the police questioned him (without <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings) about the murder of Francisco Castaneda. To put the question in terms of federal law's well-established legal standards: Would a "reasonable person" in Alvarado's "position" have felt he was "at liberty to terminate the interrogation <span class="star-pagination">*670</span> and leave"? <i>Thompson</i> v. <i>Keohane,</i> <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/#112" aria-description="Citation for case: Thompson v. Keohane">516 U. S. 99, 112</a></span> (1995); <i>Stansbury</i> v. <i>California,</i> <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#325" aria-description="Citation for case: Stansbury v. California">511 U. S. 318, 325</a></span> (1994) <i>(per curiam)</i><i>.</i> A court must answer this question in light of "all of the circumstances surrounding the interrogation." <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#322" aria-description="Citation for case: Stansbury v. California"><i>Id.,</i> at 322</a></span>. And the obvious answer here is "no."</p>
<p></p>
<h2>I</h2>
<p></p>
<h2>A</h2>
<p>The law in this case asks judges to apply, not arcane or complex legal directives, but ordinary common sense. Would a reasonable person in Alvarado's position have felt free simply to get up and walk out of the small room in the station house at will during his 2-hour police interrogation? I ask the reader to put himself, or herself, in Alvarado's circumstances and then answer that question: Alvarado hears from his parents that he is needed for police questioning. His parents take him to the station. On arrival, a police officer separates him from his parents. His parents ask to come along, but the officer says they may not. App. 185-186. Another officer says, "`What do we have here; we are going to question a suspect.'" <i>Id.,</i> at 189.</p>
<p>The police take Alvarado to a small interrogation room, away from the station's public area. A single officer begins to question him, making clear in the process that the police have evidence that he participated in an attempted carjacking connected with a murder. When he says that he never saw any shooting, the officer suggests that he is lying, while adding that she is "giving [him] the opportunity to tell the truth" and "tak[e] care of [him]self." <i>Id.,</i> at 102, 105. Toward the end of the questioning, the officer gives him permission to take a bathroom or water break. After two hours, by which time he has admitted he was involved in the attempted theft, knew about the gun, and helped to hide it, the questioning ends.</p>
<p>What reasonable person in the circumstances  brought to a police station by his parents at police request, put in a <span class="star-pagination">*671</span> small interrogation room, questioned for a solid two hours, and confronted with claims that there is strong evidence that he participated in a serious crime, could have thought to himself, "Well, anytime I want to leave I can just get up and walk out"? If the person harbored any doubts, would he still think he might be free to leave once he recalls that the police officer has just refused to let his parents remain with him during questioning? Would he still think that he, rather than the officer, controls the situation?</p>
<p>There is only one possible answer to these questions. A reasonable person would <i>not</i> have thought he was free simply to pick up and leave in the middle of the interrogation. I believe the California courts were clearly wrong to hold the contrary, and the Ninth Circuit was right in concluding that those state courts unreasonably applied clearly established federal law. See <span class="citation no-link">28 U. S. C. § 2254</span>(d)(1).</p>
<p></p>
<h2>B</h2>
<p>What about the Court's view that "fairminded jurists could disagree over whether Alvarado was in custody"? <i>Ante,</i> at 664. Consider each of the facts it says "weigh against a finding" of custody:</p>
<p>(1) <i>"The police did not transport Alvarado to the station or require him to appear at a particular time." <span class="citation no-link">Ibid.</span></i> (emphasis added). True. His parents brought him to the station at police request. But why does that matter? The relevant question is whether Alvarado came to the station of his own free will or submitted to questioning voluntarily. Cf. <i>Oregon</i> v. <i>Mathiason,</i> <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#493" aria-description="Citation for case: Oregon v. Mathiason">429 U. S. 492, 493-495</a></span> (1977) <i>(per curiam)</i><i>; </i><i>California</i> v. <i>Beheler,</i> <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1122" aria-description="Citation for case: California v. Beheler">463 U. S. 1121, 1122-1123</a></span> (1983) <i>(per curiam)</i><i>; </i><span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/#118" aria-description="Citation for case: Thompson v. Keohane"><i>Thompson, supra,</i> at 118</a></span> (THOMAS, J., dissenting). And the involvement of Alvarado's parents suggests <i>in</i>voluntary, not voluntary, behavior on Alvarado's part.</p>
<p>(2) <i>"Alvarado's parents remained in the lobby during the interview, suggesting that the interview would be brief. In</i> <span class="star-pagination">*672</span> <i>fact, [Alvarado] and his parents were told that the interview was `"not going to be long."'" Ante,</i> at 664 (citation omitted and emphasis added). Whatever was communicated to Alvarado <i>before</i> the questioning began, the fact is that the interview was not brief, nor, after the first half hour or so, would Alvarado have expected it to be brief. And those are the relevant considerations. See <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#441" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 441</a></span> (1984).</p>
<p>(3) <i>"At the end of the interview, Alvarado went home." Ante,</i> at 664 (emphasis added). As the majority acknowledges, our recent case law makes clear that the relevant question is how a reasonable person would have gauged his freedom to leave <i>during,</i> not <i>after,</i> the interview. See <i>ante,</i> at 663 (citing <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#325" aria-description="Citation for case: Stansbury v. California"><i>Stansbury, supra,</i> at 325</a></span>).</p>
<p>(4) <i>"During the interview, [Officer] Comstock focused on Soto's crimes rather than Alvarado's." Ante,</i> at 664 (emphasis added). In fact, the police officer characterized Soto as the ringleader, while making clear that she knew Alvarado had participated in the attempted carjacking during which Castaneda was killed. See App. 102-103, 109. Her questioning would have reinforced, not diminished, Alvarado's fear that he was not simply a witness, but also suspected of having been involved in a serious crime. See <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#325" aria-description="Citation for case: Stansbury v. California"><i>Stansbury, supra,</i> at 325</a></span>.</p>
<p>(5) <i>"[The officer did not] pressur[e] Alvarado with the threat of arrest and prosecution ... [but instead] appealed to his interest in telling the truth and being helpful to a police officer." Ante,</i> at 664 (emphasis added). This factor might be highly significant were the question one of "coercion." But it is not. The question is whether Alvarado would have felt free to terminate the interrogation and leave. In respect to that question, police politeness, while commendable, does not significantly help the majority.</p>
<p>(6) <i>"Comstock twice asked Alvarado if he wanted to take a break." <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">Ibid.</a></span></i> (emphasis added). This circumstance, emphasizing the officer's control of Alvarado's movements, <span class="star-pagination">*673</span> makes it <i>less</i> likely, not <i>more</i> likely, that Alvarado would have thought he was free to leave at will.</p>
<p>The facts to which the majority points make clear what the police did <i>not</i> do, for example, come to Alvarado's house, tell him he was under arrest, handcuff him, place him in a locked cell, threaten him, or tell him explicitly that he was not free to leave. But what is important here is what the police <i>did</i> do  namely, have Alvarado's parents bring him to the station, put him with a single officer in a small room, keep his parents out, let him know that he was a suspect, and question him for two hours. These latter facts compel a single conclusion: A reasonable person in Alvarado's circumstances would <i>not</i> have felt free to terminate the interrogation and leave.</p>
<p></p>
<h2>C</h2>
<p>What about Alvarado's youth? The fact that Alvarado was 17 helps to show that he was unlikely to have felt free to ignore his parents' request to come to the station. See <i>Schall</i> v. <i>Martin,</i> <span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/#265" aria-description="Citation for case: Schall v. Martin">467 U. S. 253, 265</a></span> (1984) (juveniles assumed "to be subject to the control of their parents"). And a 17-year-old is more likely than, say, a 35-year-old, to take a police officer's assertion of authority to keep parents outside the room as an assertion of authority to keep their child inside as well.</p>
<p>The majority suggests that the law might <i>prevent</i> a judge from taking account of the fact that Alvarado was 17. See <i>ante,</i> at 666-668. I can find nothing in the law that supports that conclusion. Our cases do instruct lower courts to apply a "reasonable person" standard. But the "reasonable person" standard does not require a court to pretend that Alvarado was a 35-year-old with aging parents whose middle-aged children do what their parents ask only out of respect. Nor does it say that a court should pretend that Alvarado was the statistically determined "average person"  a working, married, 35-year-old white female with a high school degree. <span class="star-pagination">*674</span> See U. S. Dept. of Commerce, Bureau of Census, Statistical Abstract of the United States: 2003 (123d ed.).</p>
<p>Rather, the precise legal definition of "reasonable person" may, depending on legal context, appropriately account for certain personal characteristics. In negligence suits, for example, the question is what would a "reasonable person" do "`under the same or similar circumstances.'" In answering that question, courts enjoy "latitude" and may make "allowance not only for external facts, but sometimes for certain characteristics of the actor himself," including physical disability, youth, or advanced age. W. Keeton, D. Dobbs, R. Keeton, &amp; D. Owen, Prosser and Keeton on Law of Torts § 32, pp. 174-179 (5th ed. 1984); see <i>id.,</i> at 179-181; see also Restatement (Third) of Torts § 10, Comment <i>b,</i> pp. 128-130 (Tent. Draft No. 1, Mar. 28, 2001) (all American jurisdictions count a person's childhood as a "relevant circumstance" in negligence determinations). This allowance makes sense in light of the tort standard's recognized purpose: deterrence. Given that purpose, why pretend that a child is an adult or that a blind man can see? See O. Holmes, The Common Law 85-89 (M. Howe ed. 1963).</p>
<p>In the present context, that of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s "in custody" inquiry, the law has introduced the concept of a "reasonable person" to avoid judicial inquiry into subjective states of mind, and to focus the inquiry instead upon objective circumstances that are known to both the officer and the suspect and that are likely relevant to the way a person would understand his situation. See <i>Stansbury,</i> <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#323" aria-description="Citation for case: Stansbury v. California">511 U. S., at 323-325</a></span>; <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#442" aria-description="Citation for case: Berkemer v. McCarty"><i>Berkemer, supra,</i> at 442</a></span>, and n. 35. This focus helps to keep <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> a workable rule. See <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#430" aria-description="Citation for case: Berkemer v. McCarty"><i>Berkemer, supra,</i> at 430-431</a></span>.</p>
<p>In this case, Alvarado's youth is an objective circumstance that was known to the police. It is not a special quality, but rather a widely shared characteristic that generates commonsense conclusions about behavior and perception. To focus on the circumstance of age in a case like this does not <span class="star-pagination">*675</span> complicate the "in custody" inquiry. And to say that courts should ignore widely shared, objective characteristics, like age, on the ground that only a (large) <i>minority</i> of the population possesses them would produce absurd results, the present instance being a case in point. I am not surprised that the majority points to no case suggesting any such limitation. Cf. <i>Alvarado</i> v. <i>Hickman,</i> <span class="citation" data-id="780555"><a href="/opinion/780555/michael-alvarado-v-rq-hickman-warden-acting-warden-of-mule-creek-state/#848" aria-description="Citation for case: Michael Alvarado v. R.Q. Hickman, Warden, Acting Warden...">316 F. 3d 841, 848, 850-851, n. 5</a></span> (CA9 2002) (case below) (listing 12 cases from 12 different jurisdictions suggesting the contrary).</p>
<p>Nor am I surprised that the majority makes no real argument at all explaining <i>why</i> any court would believe that the objective fact of a suspect's age could <i>never</i> be relevant. But see <i>ante,</i> at 669 (O'CONNOR, J., concurring) ("There may be cases in which a suspect's age will be relevant to the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> `custody' inquiry"). The majority does discuss a suspect's "history with law enforcement," <i>ante,</i> at 668  a bright red herring in the present context where Alvarado's youth (an objective fact) simply helps to show (with the help of a legal presumption) that his appearance at the police station was not voluntary. See <i>supra,</i> at 673.</p>
<p></p>
<h2>II</h2>
<p>As I have said, the law in this case is clear. This Court's cases establish that, even if the police do not tell a suspect he is under arrest, do not handcuff him, do not lock him in a cell, and do not threaten him, he may nonetheless reasonably believe he is not free to leave the place of questioning  and thus be in custody for <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> purposes. See <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#325" aria-description="Citation for case: Stansbury v. California"><i>Stansbury, supra,</i> at 325-326</a></span>; <i>Berkemer,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#440" aria-description="Citation for case: Berkemer v. McCarty">468 U. S., at 440</a></span>.</p>
<p>Our cases also make clear that to determine how a suspect would have "gaug[ed]" his "freedom of movement," a court must carefully examine "all of the circumstances surrounding the interrogation," <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#322" aria-description="Citation for case: Stansbury v. California"><i>Stansbury, supra,</i> at 322, 325</a></span> (internal quotation marks omitted), including, for example, how long the interrogation lasted (brief and routine or protracted?), see, <i>e. g., </i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#441" aria-description="Citation for case: Berkemer v. McCarty"><i>Berkemer, supra,</i> at 441</a></span>; how the suspect came to <span class="star-pagination">*676</span> be questioned (voluntarily or against his will?), see, <i>e. g., </i><i>Mathiason,</i> <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S., at 495</a></span>; where the questioning took place (at a police station or in public?), see, <i>e. g., </i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#438" aria-description="Citation for case: Berkemer v. McCarty"><i>Berkemer, supra,</i> at 438-439</a></span>; and what the officer communicated to the individual during the interrogation (that he was a suspect? that he was under arrest? that he was free to leave at will?), see, <i>e. g., </i><span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#325" aria-description="Citation for case: Stansbury v. California"><i>Stansbury, supra,</i> at 325</a></span>. In the present case, every one of these factors argues  and argues strongly  that Alvarado was in custody for <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> purposes when the police questioned him.</p>
<p>Common sense, and an understanding of the law's basic purpose in this area, are enough to make clear that Alvarado's age  an objective, widely shared characteristic about which the police plainly knew  is also relevant to the inquiry. Cf. <i>Kaupp</i> v. <i>Texas,</i> <span class="citation" data-id="127919"><a href="/opinion/127919/kaupp-v-texas/#629" aria-description="Citation for case: Kaupp v. Texas">538 U. S. 626, 629-631</a></span> (2003) <i>(per curiam)</i><i>.</i> Unless one is prepared to pretend that Alvarado is someone he is not, a middle-aged gentleman, well versed in police practices, it seems to me clear that the California courts made a serious mistake. I agree with the Ninth Circuit's similar conclusions. Consequently, I dissent.</p>
<h2>NOTES</h2>
<p>[*]   <i>Kent S. Scheidegger</i> and <i>Charles L. Hobson</i> filed a brief for the Criminal Justice Legal Foundation as <i>amicus curiae</i> urging reversal.
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the Juvenile Law Center et al. by <i>Marsha L. Levick</i> and <i>Lourdes M. Rosado;</i> and for the National Association of Criminal Defense Lawyers by <i>Jeffrey T. Green</i> and <i>David M. Porter.</i></p>

</div>
```

---
