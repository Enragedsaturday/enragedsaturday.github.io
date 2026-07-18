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

## GROUP: content/cases/Manson v. Brathwaite.md  (`case`, 5 assertions)

### content_page

```
---
title: "Manson v. Brathwaite"
type: case
citation: "432 U.S. 98 (1977)"
parallel_cite: "97 S. Ct. 2243; 53 L. Ed. 2d 140"
neutral_cite: 1977 U.S. LEXIS 116
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-06-16
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1977-06-16
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Manson v. Brathwaite
  varies_by_point: false
  scope_note: "Reliability/totality standard intact; Perry v. New Hampshire (2012) confirmed the due-process screen applies only where police arranged the suggestive circumstances, without disturbing the Manson reliability factors."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109693/manson-v-brathwaite/"
  cluster_id: 109693
  opinion_id: 109693
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Anchor"
related: ["[[Neil v. Biggers]]", "[[Stovall v. Denno]]", "[[United States v. Wade]]", "[[Perry v. New Hampshire]]"]
aliases: []
tags: ["case", "due-process", "eyewitness-identification", "suggestive-procedure", "reliability"]
holding: "There is no per se rule excluding identifications from unnecessarily suggestive procedures; reliability is the linchpin, assessed under…"
lake:
  record_id: Manson v. Brathwaite
  status: verified
  projected_at: 2026-07-09
---

# Manson v. Brathwaite

*432 U.S. 98 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An undercover officer, Glover, bought heroin from a seller he viewed for a few minutes at an apartment door. He described the seller to another officer, who left a single police photograph of Brathwaite on Glover's desk; Glover identified it days later, and again identified Brathwaite at trial. Brathwaite argued the single-photo procedure was impermissibly suggestive and required exclusion of the identification.

## Issue
Whether due process requires a [[Common Legal Terms#per-se|per se]] rule excluding identification evidence derived from an unnecessarily suggestive procedure, or whether admissibility turns on the reliability of the identification under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]].

## Rule
No [[Common Legal Terms#per-se|per se]] exclusion; reliability governs. "reliability is the linchpin in determining the admissibility of identification testimony for both pre- and post-*Stovall* confrontations." — 432 U.S. at 114. ^pin-114

The reliability factors, drawn from *[[Neil v. Biggers]]*, are "the opportunity of the witness to view the criminal at the time of the crime, the witness' degree of attention, the accuracy of his prior description of the criminal, the level of certainty demonstrated at the confrontation, and the time between the crime and the confrontation. Against these factors is to be weighed the corrupting effect of the suggestive identification itself." — [*Id.*](https://www.courtlistener.com/opinion/109693/manson-v-brathwaite/#:~:text=the%20opportunity%20of%20the%20witness) ^pin-114a

## Application
Even assuming the single-photograph display was suggestive, Glover's identification was reliable under the *Biggers* factors: as a trained officer he had a good, close opportunity to view the seller in daylight, paid careful attention, gave an accurate description, was certain in identifying the photograph, and made the identification only days after the crime. Weighed against the limited corrupting effect of the procedure, those indicia of reliability made the identification admissible.

## Conclusion
Reversed in favor of admissibility: identification evidence from a suggestive procedure is admitted when, under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], it is nonetheless reliable.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Manson* (with [[Neil v. Biggers]]) sets the governing due-process test for suggestive identifications. [[Perry v. New Hampshire]] (2012) later clarified that this due-process screen is triggered only when the suggestive circumstances were **arranged by law enforcement**, without disturbing *Manson*'s reliability framework.

## Appears on
- [[Eyewitness Identification]] — *Key — Anchor*

## Sources
- *Manson v. Brathwaite*, 432 U.S. 98 (1977) — https://www.courtlistener.com/opinion/109693/manson-v-brathwaite/ — pinpoint: 114.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2267c15c8247252c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "432 U.S. 98 (1977)", "court": "U.S. Supreme Court", "neutral_cite": "1977 U.S. LEXIS 116", "official_citation_present": true, "parallel_cite": "97 S. Ct. 2243; 53 L. Ed. 2d 140", "title": "Manson v. Brathwaite", "year": "1977"}}
{"assertion_id": "1c8ab290df55ef0f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "There is no per se rule excluding identifications from unnecessarily suggestive procedures; reliability is the linchpin, assessed under…", "title": "Manson v. Brathwaite"}}
{"assertion_id": "a8fd8c6a19cd2bd2", "dimension": "support", "kind": "home_role", "locator": {"home": "Eyewitness Identification"}, "payload": {"home": "Eyewitness Identification", "role": "Key — Anchor", "title": "Manson v. Brathwaite"}}
{"assertion_id": "0a8cd5eb345b3fa9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1977-06-16", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Manson v. Brathwaite", "field_i_validity": "good_law", "scope_note": "Reliability/totality standard intact; Perry v. New Hampshire (2012) confirmed the due-process screen applies only where police arranged the suggestive circumstances, without disturbing the Manson reliability factors.", "title": "Manson v. Brathwaite", "varies_by_point": "false"}}
{"assertion_id": "92c6d8334f384e7f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Manson v. Brathwaite"}}
```

### lake record — Manson v. Brathwaite

```json
{
  "schema_version": "s2.v1",
  "record_id": "Manson v. Brathwaite",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Manson v. Brathwaite",
    "case_name_short": "Manson",
    "case_name_full": "Manson, Correction Commissioner v. Brathwaite",
    "input_case_name": "Manson v. Brathwaite",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-06-16",
    "year": 1977,
    "docket": null,
    "cluster_id": 109693,
    "lead_opinion_id": 109693,
    "sibling_ids": [
      109693,
      9426868,
      9426869,
      9426870
    ],
    "absolute_url": "/opinion/109693/manson-v-brathwaite/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9011220,
        "score": 20,
        "case_name": "Manson v. Brathwaite"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "432 U.S. 98",
      "volume": "432",
      "reporter": "U.S.",
      "page": "98",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "97 S. Ct. 2243",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "2243",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 L. Ed. 2d 140",
        "volume": "53",
        "reporter": "L. Ed. 2d",
        "page": "140",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 116",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "116",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "432 U.S. 98",
        "volume": "432",
        "reporter": "U.S.",
        "page": "98",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 2243",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "2243",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 L. Ed. 2d 140",
        "volume": "53",
        "reporter": "L. Ed. 2d",
        "page": "140",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 116",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "116",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "432 U.S. 98",
    "official_selection": {
      "court_class": "scotus",
      "selected": "432 U.S. 98",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-114",
      "page": null,
      "quote": "--- # Manson v. Brathwaite *432 U.S. 98 (1977)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An undercover officer, Glover, bought heroin from a seller he viewed for a few minutes at an apartment door. He described the seller to another officer, who left a single police photograph of Brathwaite on Glover's desk; Glover identified it days later, and again identified Brathwaite at trial. Brathwaite argued the single-photo procedure was impermissibly suggestive and required exclusion of the identification. ## Issue Whether due process requires a per se rule excluding identification evidence derived from an unnecessarily suggestive procedure, or whether admissibility turns on the reliability of the identification under the totality of the circumstances. ## Rule No per se exclusion; reliability governs.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-114a",
      "page": null,
      "quote": "the opportunity of the witness to view the criminal at the time of the crime, the witness' degree of attention, the accuracy of his prior description of the criminal, the level of certainty demonstrated at the confrontation, and the time between the crime and the confrontation. Against these factors is to be weighed the corrupting effect of the suggestive identification itself.",
      "star_marker": "114",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 39257,
      "fragment": "#:~:text=the%20opportunity%20of%20the%20witness",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1977-06-16",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Manson v. Brathwaite",
    "varies_by_point": false,
    "scope_note": "Reliability/totality standard intact; Perry v. New Hampshire (2012) confirmed the due-process screen applies only where police arranged the suggestive circumstances, without disturbing the Manson reliability factors.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Manson v. Brathwaite:lane1_negative"
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
        "journal_ref": "Manson v. Brathwaite:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. McComb",
          "cluster_id": 4394880,
          "cite": [
            "2017 Ohio 4010",
            "91 N.E.3d 255"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane1_negative"
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
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Youngblood",
          "cluster_id": 112156,
          "cite": [
            "102 L. Ed. 2d 281",
            "109 S. Ct. 333",
            "488 U.S. 51",
            "1988 U.S. LEXIS 5404"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
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
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
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
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
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
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
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
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Chipp",
          "cluster_id": 5689934,
          "cite": [
            "75 N.Y.2d 327",
            "552 N.E.2d 608",
            "553 N.Y.S.2d 72",
            "1990 N.Y. LEXIS 230"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
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
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bryant, Smith and Wheeler",
          "cluster_id": 2720490,
          "cite": [
            "60 Cal. 4th 335",
            "178 Cal. Rptr. 3d 185",
            "334 P.3d 573",
            "2014 Cal. LEXIS 6110"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
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
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
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
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
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
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
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
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
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
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gregory v. City of Louisville",
          "cluster_id": 2973641,
          "cite": [
            "444 F.3d 725",
            "2006 WL 909935"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Prudholm",
          "cluster_id": 1956631,
          "cite": [
            "446 So. 2d 729"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Arias",
          "cluster_id": 1179776,
          "cite": [
            "13 Cal. 4th 92",
            "913 P.2d 980",
            "51 Cal. Rptr. 2d 770",
            "96 Daily Journal DAR 4243",
            "96 Cal. Daily Op. Serv. 2575",
            "1996 Cal. LEXIS 1572"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ibarra v. State",
          "cluster_id": 1960811,
          "cite": [
            "11 S.W.3d 189",
            "1999 Tex. Crim. App. LEXIS 117",
            "1999 WL 956173"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. State",
          "cluster_id": 2428074,
          "cite": [
            "827 S.W.2d 949",
            "1992 Tex. Crim. App. LEXIS 106",
            "1992 WL 79216"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Madden v. State",
          "cluster_id": 2381074,
          "cite": [
            "799 S.W.2d 683",
            "1990 WL 130495"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Murad Nersesian",
          "cluster_id": 492031,
          "cite": [
            "824 F.2d 1294",
            "23 Fed. R. Serv. 487",
            "1987 U.S. App. LEXIS 8418"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
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
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Loserth v. State",
          "cluster_id": 1494741,
          "cite": [
            "963 S.W.2d 770",
            "1998 Tex. Crim. App. LEXIS 22",
            "1998 WL 75681"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Yeoman",
          "cluster_id": 2588519,
          "cite": [
            "72 P.3d 1166",
            "2 Cal. Rptr. 3d 186",
            "31 Cal. 4th 93",
            "2003 Cal. Daily Op. Serv. 6313",
            "2003 Daily Journal DAR 7888",
            "2003 Cal. LEXIS 4823"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hansen v. State",
          "cluster_id": 1829968,
          "cite": [
            "592 So. 2d 114",
            "1991 WL 280025"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109693 OR 9426868 OR 9426869 OR 9426870) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDkyNTYwMDAwMDAwJnM9NDM4NDIxMyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109693+OR+9426868+OR+9426869+OR+9426870%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      },
      "lane2_top_cited": {
        "query": "cites:(109693 OR 9426868 OR 9426869 OR 9426870)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zODAmcz0yNDM0MDI3JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109693+OR+9426868+OR+9426869+OR+9426870%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109693 OR 9426868 OR 9426869 OR 9426870)",
        "reviewed": 52,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 52,
        "triage_read": 0,
        "triage_snippet_classified": 52
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109693 OR 9426868 OR 9426869 OR 9426870)",
    "indexed_citing_opinions": 3221,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109693,
        "count": 2827,
        "count_source": "search"
      },
      {
        "opinion_id": 9426868,
        "count": 433,
        "count_source": "search"
      },
      {
        "opinion_id": 9426869,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426870,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 5121,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/manson-v-brathwaite.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNjU2ODcmcz0xMDM2MDcxNCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109693+OR+9426868+OR+9426869+OR+9426870%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109693,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 107890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 108639,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 109587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 109682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 270486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 284140,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 288139,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 308320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 314070,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 324941,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 1436230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 1801408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 2221090,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 2222943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 2611155,
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
    "date_created": "2026-07-05T11:35:13Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:35:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:35:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:39:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:35:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Manson v. Brathwaite (truncated)

```
<div>
<center><b><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">432 U.S. 98</a></span> (1977)</b></center>
<center><h1>MANSON, CORRECTION COMMISSIONER<br>
v.<br>
BRATHWAITE.</h1></center>
<center>No. 75-871.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 29, 1976.</center>
<center>Decided June 16, 1977.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT.
<p><span class="star-pagination">*99</span> <i>Bernard D. Gaffney</i> argued the cause for petitioner. With him on the brief was <i>George D. Stoughton.</i></p>
<p><i>David S. Golub</i> argued the cause for respondent. With him on the brief were <i>Frederick H. Weisberg, Richard A. Silver,</i> and <i>Jay H. Sandak.</i></p>
<p>MR. JUSTICE BLACKMUN delivered the opinion of the Court.</p>
<p>This case presents the issue as to whether the Due Process Clause of the Fourteenth Amendment compels the exclusion, in a state criminal trial, apart from any consideration of reliability, of pretrial identification evidence obtained by a police procedure that was both suggestive and unnecessary. This Court's decisions in <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span> (1967), and <i>Neil</i> v. <i>Biggers,</i> <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">409 U. S. 188</a></span> (1972), are particularly implicated.</p>
<p></p>
<h2>I</h2>
<p>Jimmy D. Glover, a full-time trooper of the Connecticut State Police, in 1970 was assigned to the Narcotics Division in an undercover capacity. On May 5 of that year, about <span class="star-pagination">*100</span> 7:45 p. m., e. d. t., and while there was still daylight, Glover and Henry Alton Brown, an informant, went to an apartment building at 201 Westland, in Hartford, for the purpose of purchasing narcotics from "Dickie Boy" Cicero, a known narcotics dealer. Cicero, it was thought, lived on the third floor of that apartment building. Tr. 45-46, 68.<sup>[1]</sup> Glover and Brown entered the building, observed by backup Officers D'Onofrio and Gaffey, and proceeded by stairs to the third floor. Glover knocked at the door of one of the two apartments served by the stairway.<sup>[2]</sup> The area was illuminated by natural light from a window in the third floor hallway. <i>Id.,</i> at 27-28. The door was opened 12 to 18 inches in response to the knock. Glover observed a man standing at the door and, behind him, a woman. Brown identified himself. Glover then asked for "two things" of narcotics. <i>Id.,</i> at 29. The man at the door held out his hand, and Glover gave him two $10 bills. The door closed. Soon the man returned and handed Glover two glassine bags.<sup>[3]</sup> While the door was open, Glover stood within two feet of the person from whom he made the purchase and observed his face. Five to seven minutes elapsed from the <span class="star-pagination">*101</span> time the door first opened until it closed the second time. <i>Id.,</i> at 30-33.</p>
<p>Glover and Brown then left the building. This was about eight minutes after their arrival. Glover drove to headquarters where he described the seller to D'Onofrio and Gaffey. Glover at that time did not know the identity of the seller. <i>Id.,</i> at 36. He described him as being "a colored man, approximately five feet eleven inches tall, dark complexion, black hair, short Afro style, and having high cheekbones, and of heavy build. He was wearing at the time blue pants and a plaid shirt." <i>Id.,</i> at 36-37. D'Onofrio, suspecting from this description that respondent might be the seller, obtained a photograph of respondent from the Records Division of the Hartford Police Department. He left it at Glover's office. D'Onofrio was not acquainted with respondent personally, but did know him by sight and had seen him "[s]everal times" prior to May 5. <i>Id.,</i> at 63-65. Glover, when alone, viewed the photograph for the first time upon his return to headquarters on May 7; he identified the person shown as the one from whom he had purchased the narcotics. <i>Id.,</i> at 36-38.</p>
<p>The toxicological report on the contents of the glassine bags revealed the presence of heroin. The report was dated July 16, 1970. <i>Id.,</i> at 75-76.</p>
<p>Respondent was arrested on July 27 while visiting at the apartment of a Mrs. Ramsey on the third floor of 201 Westland. This was the apartment at which the narcotics sale had taken place on May 5.<sup>[4]</sup></p>
<p>Respondent was charged, in a two-count information, with possession and sale of heroin, in violation of Conn. Gen. Stat. (Rev. of 1958, as amended in 1969), §§ 19-481a and 19-480a <span class="star-pagination">*102</span> (1977).<sup>[5]</sup> At his trial in January 1971, the photograph from which Glover had identified respondent was received in evidence without objection on the part of the defense. Tr. 38. Glover also testified that, although he had not seen respondent in the eight months that had elapsed since the sale, "there [was] no doubt whatsoever" in his mind that the person shown on the photograph was respondent. <i>Id.,</i> at 41-42. Glover also made a positive in-court identification without objection. <i>Id.,</i> at 37-38.</p>
<p>No explanation was offered by the prosecution for the failure to utilize a photographic array or to conduct a lineup.</p>
<p>Respondent, who took the stand in his own defense, testified that on May 5, the day in question, he had been ill at his Albany Avenue apartment ("a lot of back pains, muscle spasms . . . a bad heart . . . high blood pressure . . . neuralgia in my face, and sinus," <i>id.,</i> at 106), and that at no time on that particular day had he been at 201 Westland. <i>Id.,</i> at 106, 113-114. His wife testified that she recalled, after her husband had refreshed her memory, that he was home all day on May 5. <i>Id.,</i> at 164-165. Doctor Wesley M. Vietzke, an internist and assistant professor of medicine at the University of Connecticut, testified that respondent had consulted him on April 15, 1970, and that he took a medical history from him, heard his complaints about his back and facial pain, and discovered that he had high blood pressure. <i>Id.,</i> at 129-131. The physician found respondent, subjectively, "in great discomfort." <i>Id.,</i> at 135. Respondent in fact underwent surgery for a herniated disc at L5 and S1 on August 17. <i>Id.,</i> at 157.</p>
<p>The jury found respondent guilty on both counts of the information. He received a sentence of not less than six nor <span class="star-pagination">*103</span> more than nine years. His conviction was affirmed <i>per curiam</i> by the Supreme Court of Connecticut. <i>State</i> v. <i>Brathwaite,</i> <span class="citation" data-id="1436230"><a href="/opinion/1436230/state-v-brathwaite/" aria-description="Citation for case: State v. Brathwaite">164 Conn. 617</a></span>, <span class="citation" data-id="1436230"><a href="/opinion/1436230/state-v-brathwaite/" aria-description="Citation for case: State v. Brathwaite">325 A. 2d 284</a></span> (1973). That court noted the absence of an objection to Glover's in-court identification and concluded that respondent "has not shown that substantial injustice resulted from the admission of this evidence." <span class="citation" data-id="1436230"><a href="/opinion/1436230/state-v-brathwaite/#619" aria-description="Citation for case: State v. Brathwaite"><i>Id.,</i> at 619</a></span>, <span class="citation" data-id="1436230"><a href="/opinion/1436230/state-v-brathwaite/#285" aria-description="Citation for case: State v. Brathwaite">325 A. 2d, at 285</a></span>. Under Connecticut law, substantial injustice must be shown before a claim of error not made or passed on by the trial court will be considered on appeal. <i><span class="citation" data-id="1436230"><a href="/opinion/1436230/state-v-brathwaite/" aria-description="Citation for case: State v. Brathwaite">Ibid.</a></span></i></p>
<p>Fourteen months later, respondent filed a petition for habeas corpus in the United States District Court for the District of Connecticut. He alleged that the admission of the identification testimony at his state trial deprived him of due process of law to which he was entitled under the Fourteenth Amendment. The District Court, by an unreported written opinion based on the court's review of the state trial transcript,<sup>[6]</sup> dismissed respondent's petition. On appeal, the United States Court of Appeals for the Second Circuit reversed, with instructions to issue the writ unless the State gave notice of a desire to retry respondent and the new trial occurred within a reasonable time to be fixed by the District Judge.<sup>[7]</sup> <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d 363</a></span> (1975).</p>
<p>In brief summary, the court felt that evidence as to the photograph should have been excluded, regardless of reliability, <span class="star-pagination">*104</span> because the examination of the single photograph was unnecessary and suggestive. And, in the court's view, the evidence was unreliable in any event. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./425/957/">425 U. S. 957</a></span> (1976).</p>
<p></p>
<h2>II</h2>
<p><i>Stovall</i> v. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Denno, supra</a></span></i><i>,</i> decided in 1967, concerned a petitioner who had been convicted in a New York court of murder. He was arrested the day following the crime and was taken by the police to a hospital where the victim's wife, also wounded in the assault, was a patient. After observing Stovall and hearing him speak, she identified him as the murderer. She later made an in-court identification. On federal habeas, Stovall claimed the identification testimony violated his Fifth, Sixth, and Fourteenth Amendment rights. The District Court dismissed the petition, and the Court of Appeals, en banc, affirmed. This Court also affirmed. On the identification issue, the Court reviewed the practice of showing a suspect singly for purposes of identification, and the claim that this was so unnecessarily suggestive and conducive to irreparable mistaken identification that it constituted a denial of due process of law. The Court noted that the practice "has been widely condemned," <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#302" aria-description="Citation for case: Stovall v. Denno">388 U. S., at 302</a></span>, but it concluded that "a claimed violation of due process of law in the conduct of a confrontation depends on the totality of the circumstances surrounding it." <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Ibid.</a></span></i> In that case, showing Stovall to the victim's spouse "was imperative." The Court then quoted the observations of the Court of Appeals, <span class="citation" data-id="9451306"><a href="/opinion/270486/united-states-ex-rel-theodore-r-stovall-v-honorable-wilfred-denno-as/#735" aria-description="Citation for case: United States Ex Rel. Theodore R. Stovall v. Honorable...">355 F. 2d 731, 735</a></span> (CA2 1966), to the effect that the spouse was the only person who could possibly exonerate the accused; that the hospital was not far from the courthouse and jail; that no one knew how long she might live; that she was not able to visit the jail; and that taking Stovall to the hospital room was the only feasible procedure, and, under the circumstances, "`the usual police station line-up . . . was out of the question.'" <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#302" aria-description="Citation for case: Stovall v. Denno">388 U. S., at 302</a></span>.</p>
<p><span class="star-pagination">*105</span> <i>Neil</i> v. <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers, supra</a></span></i><i>,</i> decided in 1972, concerned a respondent who had been convicted in a Tennessee court of rape, on evidence consisting in part of the victim's visual and voice identification of Biggers at a station-house showup seven months after the crime. The victim had been in her assailant's presence for some time and had directly observed him indoors and under a full moon outdoors. She testified that she had "no doubt" that Biggers was her assailant. She previously had given the police a description of the assailant. She had made no identification of others presented at previous showups, lineups, or through photographs. On federal habeas, the District Court held that the confrontation was so suggestive as to violate due process. The Court of Appeals affirmed. This Court reversed on that issue, and held that the evidence properly had been allowed to go to the jury. The Court reviewed <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> and certain later cases where it had considered the scope of due process protection against the admission of evidence derived from suggestive identification procedures, namely, <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span> (1968); <i>Foster</i> v. <i>California,</i> <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">394 U. S. 440</a></span> (1969); and <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970).<sup>[8]</sup> The Court concluded that <span class="star-pagination">*106</span> general guidelines emerged from these cases "as to the relationship between suggestiveness and misidentification." The "admission of evidence of a showup without more does not violate due process." <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#198" aria-description="Citation for case: Neil v. Biggers">409 U. S., at 198</a></span>. The Court expressed concern about the lapse of seven months between the crime and the confrontation and observed that this "would be a seriously negative factor in most cases." <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#201" aria-description="Citation for case: Neil v. Biggers"><i>Id.,</i> at 201</a></span>. The "central question," however, was "whether under the `totality of the circumstances' the identification was reliable even though the confrontation procedure was suggestive." <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#199" aria-description="Citation for case: Neil v. Biggers"><i>Id.,</i> at 199</a></span>. Applying that test, the Court found "no substantial likelihood of misidentification. The evidence was properly allowed to go to the jury." <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#201" aria-description="Citation for case: Neil v. Biggers"><i>Id.,</i> at 201</a></span>.</p>
<p><i>Biggers</i> well might be seen to provide an unambiguous answer to the question before us: The admission of testimony concerning a suggestive and unnecessary identification procedure does not violate due process so long as the identification possesses sufficient aspects of reliability.<sup>[9]</sup> In one passage, <span class="star-pagination">*107</span> however, the Court observed that the challenged procedure occurred pre-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> and that a strict rule would make little sense with regard to a confrontation that preceded the Court's first indication that a suggestive procedure might lead to the exclusion of evidence. <i>Id.,</i> at 199. One perhaps might argue that, by implication, the Court suggested that a different rule could apply post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall.</i></a></span> The question before us, then, is simply whether the <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> analysis applies to post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> confrontations as well to those pre-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall.</i></a></span></p>
<p></p>
<h2>III</h2>
<p>In the present case the District Court observed that the "sole evidence tying Brathwaite to the possession and sale of the heroin consisted in his identifications by the police undercover agent, Jimmy Glover." App. to Pet. for Cert. 6a. On the constitutional issue, the court stated that the first inquiry was whether the police used an impermissibly suggestive procedure in obtaining the out-of-court identification. If so, the second inquiry is whether, under all the circumstances, that suggestive procedure gave rise to a substantial likelihood of irreparable misidentification. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Id.,</a></span></i> at 9a. <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> and <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> were cited. The court noted that in the Second Circuit, its controlling court, it was clear that "this type of identification procedure [display of a single photograph] is impermissibly <span class="star-pagination">*108</span> suggestive," and turned to the second inquiry. App. to Pet. for Cert. 9a. The factors <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> specified for consideration were recited and applied. The court concluded that there was no substantial likelihood of irreparable misidentification. It referred to the facts: Glover was within two feet of the seller. The duration of the confrontation was at least a "couple of minutes." There was natural light from a window or skylight and there was adequate light to see clearly in the hall. Glover "certainly was paying attention to identify the seller." <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Id.,</a></span></i> at 10a. He was a trained police officer who realized that later he would have to find and arrest the person with whom he was dealing. He gave a detailed description to D'Onofrio. The reliability of this description was supported by the fact that it enabled D'Onofrio to pick out a single photograph that was thereafter positively identified by Glover. Only two days elapsed between the crime and the photographic identification. Despite the fact that another eight months passed before the in-court identification, Glover had "no doubt" that Brathwaite was the person who had sold him heroin.</p>
<p>The Court of Appeals confirmed that the exhibition of the single photograph to Glover was "impermissibly suggestive," <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#366" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d, at 366</a></span>, and felt that, in addition, "it was unnecessarily so." <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#367" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of..."><i>Id.,</i> at 367</a></span>. There was no emergency and little urgency. The court said that prior to the decision in <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span>,</i> except in cases of harmless error, "a conviction secured as the result of admitting an identification obtained by impermissibly suggestive and unnecessary measures could not stand." <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Ibid.</a></span></i> It noted what it felt might be opposing inferences to be drawn from passages in <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span>,</i> but concluded that the case preserved the principle "requiring the exclusion of identifications resulting from `unnecessarily suggestive confrontation'" in post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> situations. <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#368" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d, at 368</a></span>. The court also concluded that for post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> identifications, <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> had not changed the existing rule. Thus: "Evidence of an identification unnecessarily obtained by impermissibly <span class="star-pagination">*109</span> suggestive means must be excluded under <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> . . . . No rules less stringent than these can force police administrators and prosecutors to adopt procedures that will give fair assurance against the awful risks of misidentification." <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#371" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d, at 371</a></span>. Finally, the court said, even if this conclusion were wrong, the writ, nevertheless, should issue. It took judicial notice that on May 5, 1970, sunset at Hartford was at 7:53 p. m. It characterized Glover's duty as an undercover agent as one "to cause arrests to be made," and his description of the suspect as one that "could have applied to hundreds of Hartford black males." <i><span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">Ibid.</a></span></i> The in-court identification had "little meaning," for Brathwaite was at the counsel table. The fact that respondent was arrested in the very apartment where the sale was made was subject to a "not implausible" explanation from the respondent, "although evidently not credited by the jury." And the court was troubled by "the long and unexplained delay" in the arrest. It was too great a danger that the respondent was convicted because he was a man D'Onofrio had previously observed near the scene, was thought to be a likely offender, and was arrested when he was known to be in Mrs. Ramsey's apartment, rather than because Glover "really remembered him as the seller." <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#371" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of..."><i>Id.,</i> at 371-372</a></span>.</p>
<p></p>
<h2>IV</h2>
<p>Petitioner at the outset acknowledges that "the procedure in the instant case was suggestive [because only one photograph was used] and unnecessary" [because there was no emergency or exigent circumstance]. Brief for Petitioner 10; Tr. of Oral Arg. 7. The respondent, in agreement with the Court of Appeals, proposes a <i>per se</i> rule of exclusion that he claims is dictated by the demands of the Fourteenth Amendment's guarantee of due process. He rightly observes that this is the first case in which this Court has had occasion to rule upon strictly post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> out-of-court identification evidence of the challenged kind.</p>
<p><span class="star-pagination">*110</span> Since the decision in <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span>,</i> the Courts of Appeals appear to have developed at least two approaches to such evidence. See Pulaski, <i>Neil</i> v. <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span>:</i> The Supreme Court Dismantles the <i>Wade</i> Trilogy's Due Process Protection, <span class="citation no-link">26 Stan. L. Rev. 1097</span>, 1111-1114 (1974). The first, or <i>per se</i> approach, employed by the Second Circuit in the present case, focuses on the procedures employed and requires exclusion of the out-of-court identification evidence, without regard to reliability, whenever it has been obtained through unnecessarily suggested confrontation procedures.<sup>[10]</sup> The justifications advanced are the elimination of evidence of uncertain reliability, deterrence of the police and prosecutors, and the stated "fair assurance against the awful risks of misidentification." <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#371" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d, at 371</a></span>. See <i>Smith</i> v. <i>Coiner,</i> <span class="citation" data-id="308320"><a href="/opinion/308320/edward-lee-smith-v-ira-m-coiner-warden-of-the-west-virginia-state/#882" aria-description="Citation for case: Edward Lee Smith v. Ira M. Coiner, Warden of the West...">473 F. 2d 877, 882</a></span> (CA4), cert. denied <i>sub nom. </i><i>Wallace</i> v. <i>Smith,</i> <span class="citation" data-id="8988513"><a href="/opinion/8996170/wallace-v-smith/" aria-description="Citation for case: Wallace v. Smith">414 U. S. 1115</a></span> (1973).</p>
<p>The second, or more lenient, approach is one that continues to rely on the totality of the circumstances. It permits the admission of the confrontation evidence if, despite the suggestive aspect, the out-of-court identification possesses certain features of reliability. Its adherents feel that the <i>per se</i> approach is not mandated by the Due Process Clause of the Fourteenth Amendment. This second approach, in contrast to the other, is ad hoc and serves to limit the societal costs imposed by a sanction that excludes relevant evidence from consideration and evaluation by the trier of fact. See <i>United States ex rel. Kirby</i> v. <i>Sturges,</i> <span class="citation" data-id="324941"><a href="/opinion/324941/united-states-of-america-ex-rel-thomas-kirby-v-david-r-sturges-chairman/#407" aria-description="Citation for case: United States of America Ex Rel. Thomas Kirby v. David R....">510 F. 2d 397, 407-408</a></span> (CA7) (opinion by Judge, now MR. JUSTICE, STEVENS), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./421/1016/">421 U. S. 1016</a></span> (1975); <i>Stanley</i> v. <i>Cox,</i> 486 F. 2d 48 <span class="star-pagination">*111</span> (CA4 1973), cert. denied <i>sub nom. Stanley</i> v. <i>Slayton,</i> <span class="citation" data-id="8990231"><a href="/opinion/8997836/stanley-v-slayton/" aria-description="Citation for case: Stanley v. Slayton">416 U. S. 958</a></span> (1974).<sup>[11]</sup></p>
<p>MR. JUSTICE STEVENS, in writing for the Seventh Circuit in <i><span class="citation" data-id="324941"><a href="/opinion/324941/united-states-of-america-ex-rel-thomas-kirby-v-david-r-sturges-chairman/" aria-description="Citation for case: United States of America Ex Rel. Thomas Kirby v. David R....">Kirby, supra,</a></span></i> observed: "There is surprising unanimity among scholars in regarding such a rule [the <i>per se</i> approach] as essential to avoid serious risk of miscarriage of justice." <span class="citation" data-id="324941"><a href="/opinion/324941/united-states-of-america-ex-rel-thomas-kirby-v-david-r-sturges-chairman/#405" aria-description="Citation for case: United States of America Ex Rel. Thomas Kirby v. David R....">510 F. 2d, at 405</a></span>. He pointed out that well-known federal judges have taken the position that "evidence of, or derived from, a showup identification should be inadmissible unless the prosecutor can justify his failure to use a more reliable identification procedure." <span class="citation" data-id="324941"><a href="/opinion/324941/united-states-of-america-ex-rel-thomas-kirby-v-david-r-sturges-chairman/#406" aria-description="Citation for case: United States of America Ex Rel. Thomas Kirby v. David R...."><i>Id.,</i> at 406</a></span>. Indeed, the ALI Model Code of Pre-Arraignment Procedure §§ 160.1 and 160.2 (1975) (hereafter Model Code) frowns upon the use of a showup or the display of only a single photograph.</p>
<p>The respondent here stresses the same theme and the need for deterrence of improper identification practice, a factor he regards as pre-eminent. Photographic identification, it is said, continues to be needlessly employed. He notes that the legislative regulation "the Court had hoped [<i>United States</i> v.] <i>Wade</i>[, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#239" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 239</a></span> (1967),] would engender," Brief for Respondent 15, has not been forthcoming. He argues that a totality rule cannot be expected to have a significant deterrent impact; only a strict rule of exclusion will have direct and immediate impact on law enforcement agents. Identification evidence is so convincing to the jury that sweeping exclusionary rules are required. Fairness of the trial is threatened by suggestive confrontation evidence, and thus, it is said, an exclusionary rule has an established constitutional predicate.</p>
<p>There are, of course, several interests to be considered and taken into account. The driving force behind <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), <i>Gilbert</i> v. <i>California,</i> 388 <span class="star-pagination">*112</span> U. S. 263 (1967) (right to counsel at a post-indictment lineup), and <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>,</i> all decided on the same day, was the Court's concern with the problems of eyewitness identification. Usually the witness must testify about an encounter with a total stranger under circumstances of emergency or emotional stress. The witness' recollection of the stranger can be distorted easily by the circumstances or by later actions of the police. Thus, <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and its companion cases reflect the concern that the jury not hear eyewitness testimony unless that evidence has aspects of reliability. It must be observed that both approaches before us are responsive to this concern. The <i>per se</i> rule, however, goes too far since its application automatically and peremptorily, and without consideration of alleviating factors, keeps evidence from the jury that is reliable and relevant.</p>
<p>The second factor is deterrence. Although the <i>per se</i> approach has the more significant deterrent effect, the totality approach also has an influence on police behavior. The police will guard against unnecessarily suggestive procedures under the totality rule, as well as the <i>per se</i> one, for fear that their actions will lead to the exclusion of identifications as unreliable.<sup>[12]</sup></p>
<p>The third factor is the effect on the administration of justice. Here the <i>per se</i> approach suffers serious drawbacks. Since it denies the trier reliable evidence, it may result, on occasion, in the guilty going free. Also, because of its rigidity, the <i>per se</i> approach may make error by the trial judge more likely than the totality approach. And in those cases in which the admission of identification evidence is error under the <i>per se</i> approach but not under the totality approach <span class="star-pagination">*113</span> cases in which the identification is reliable despite an unnecessarily suggestive identification procedurereversal is a Draconian sanction.<sup>[13]</sup> Certainly, inflexible rules of exclusion that may frustrate rather than promote justice have not been viewed recently by this Court with unlimited enthusiasm. See, for example, the several opinions in <i>Brewer</i> v. <i>Williams,</i> <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387</a></span> (1977). See also <i>United States</i> v. <i>Janis,</i> <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">428 U. S. 433</a></span> (1976).</p>
<p>It is true, as has been noted, that the Court in <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> referred to the pre-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> character of the confrontation in that case. <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#199" aria-description="Citation for case: Neil v. Biggers">409 U. S., at 199</a></span>. But that observation was only one factor in the judgmental process. It does not translate into a holding that post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> confrontation evidence automatically is to be excluded.</p>
<p>The standard, after all, is that of fairness as required by the Due Process Clause of the Fourteenth Amendment. See <i>United States</i> v. <i>Lovasco,</i> <span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#790" aria-description="Citation for case: United States v. Lovasco">431 U. S. 783, 790</a></span> (1977); <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#170" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 170-172</a></span> (1952). <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>,</i> with its reference to "the totality of the circumstances," 388 U. S., at 302, and <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span>,</i> with its continuing stress on the same totality, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#199" aria-description="Citation for case: Neil v. Biggers">409 U. S., at 199</a></span>, did not, singly or together, establish a strict exclusionary rule or new standard of due process. Judge Leventhal, although speaking pre-<span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers"><i>Biggers</i></a></span> and of a pre-<span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade"><i>Wade</i></a></span> situation, correctly has described <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> as protecting an <i>evidentiary</i> interest and, at the same time, as recognizing the limited extent of that interest in our adversary system.<sup>[14]</sup></p>
<p><span class="star-pagination">*114</span> We therefore conclude that reliability is the linchpin in determining the admissibility of identification testimony for both pre- and post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> confrontations. The factors to be considered are set out in <i>Biggers.</i> <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#199" aria-description="Citation for case: Neil v. Biggers">409 U. S., at 199-200</a></span>. These include the opportunity of the witness to view the criminal at the time of the crime, the witness' degree of attention, the accuracy of his prior description of the criminal, the level of certainty demonstrated at the confrontation, and the time between the crime and the confrontation. Against these factors is to be weighed the corrupting effect of the suggestive identification itself.</p>
<p></p>
<h2>V</h2>
<p>We turn, then, to the facts of this case and apply the analysis:</p>
<p>1. The opportunity to view. Glover testified that for two to three minutes he stood at the apartment door, within two feet of the respondent. The door opened twice, and each time the man stood at the door. The moments passed, the conversation took place, and payment was made. Glover looked directly at his vendor. It was near sunset, to be sure, but the sun had not yet set, so it was not dark or even dusk or twilight. Natural light from outside entered the hallway through a window. There was natural light, as well, from inside the apartment.</p>
<p><span class="star-pagination">*115</span> 2. The degree of attention. Glover was not a casual or passing observer, as is so often the case with eyewitness identification. Trooper Glover was a trained police officer on dutyand specialized and dangerous dutywhen he called at the third floor of 201 Westland in Hartford on May 5, 1970. Glover himself was a Negro and unlikely to perceive only general features of "hundreds of Hartford black males," as the Court of Appeals stated. <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#371" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d, at 371</a></span>. It is true that Glover's duty was that of ferreting out narcotics offenders and that he would be expected in his work to produce results. But it is also true that, as a specially trained, assigned, and experienced officer, he could be expected to pay scrupulous attention to detail, for he knew that subsequently he would have to find and arrest his vendor. In addition, he knew that his claimed observations would be subject later to close scrutiny and examination at any trial.</p>
<p>3. The accuracy of the description. Glover's description was given to D'Onofrio within minutes after the transaction. It included the vendor's race, his height, his build, the color and style of his hair, and the high cheekbone facial feature. It also included clothing the vendor wore. No claim has been made that respondent did not possess the physical characteristics so described. D'Onofrio reacted positively at once. Two days later, when Glover was alone, he viewed the photograph D'Onofrio produced and identified its subject as the narcotics seller.</p>
<p>4. The witness' level of certainty. There is no dispute that the photograph in question was that of respondent. Glover, in response to a question whether the photograph was that of the person from whom he made the purchase, testified: "There is no question whatsoever." Tr. 38. This positive assurance was repeated. <i>Id.,</i> at 41-42.</p>
<p>5. The time between the crime and the confrontation. Glover's description of his vendor was given to D'Onofrio <span class="star-pagination">*116</span> within minutes of the crime. The photographic identification took place only two days later. We do not have here the passage of weeks or months between the crime and the viewing of the photograph.</p>
<p>These indicators of Glover's ability to make an accurate identification are hardly outweighed by the corrupting effect of the challenged identification itself. Although identifications arising from single-photograph displays may be viewed in general with suspicion, see <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#383" aria-description="Citation for case: Simmons v. United States">390 U. S., at 383</a></span>, we find in the instant case little pressure on the witness to acquiesce in the suggestion that such a display entails. D'Onofrio had left the photograph at Glover's office and was not present when Glover first viewed it two days after the event. There thus was little urgency and Glover could view the photograph at his leisure. And since Glover examined the photograph alone, there was no coercive pressure to make an identification arising from the presence of another. The identification was made in circumstances allowing care and reflection.</p>
<p>Although it plays no part in our analysis, all this assurance as to the reliability of the identification is hardly undermined by the facts that respondent was arrested in the very apartment where the sale had taken place, and that he acknowledged his frequent visits to that apartment.<sup>[15]</sup></p>
<p>Surely, we cannot say that under all the circumstances of this case there is "a very substantial likelihood of irreparable misidentification." <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States"><i>Id.,</i> at 384</a></span>. Short of that point, such evidence is for the jury to weigh. We are content to rely upon the good sense and judgment of American juries, for evidence with some element of untrustworthiness is customary grist for the jury mill. Juries are not so susceptible that they cannot measure intelligently the weight of identification testimony that has some questionable feature.</p>
<p><span class="star-pagination">*117</span> Of course, it would have been better had D'Onofrio presented Glover with a photographic array including "so far as practicable . . . a reasonable number of persons similar to any person then suspected whose likeness is included in the array." Model Code § 160.2 (2). The use of that procedure would have enhanced the force of the identification at trial and would have avoided the risk that the evidence would be excluded as unreliable. But we are not disposed to view D'Onofrio's failure as one of constitutional dimension to be enforced by a rigorous and unbending exclusionary rule. The defect, if there be one, goes to weight and not to substance.<sup>[16]</sup></p>
<p>We conclude that the criteria laid down in <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> are to be applied in determining the admissibility of evidence offered by the prosecution concerning a post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> identification, and that those criteria are satisfactorily met and complied with here.</p>
<p>The judgment of the Court of Appeals is reversed.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE STEVENS, concurring.</p>
<p>While I join the Court's opinion, I would emphasize two points.</p>
<p>First, as I indicated in my opinion in <i>United States ex rel. Kirby</i> v. <i>Sturges,</i> <span class="citation" data-id="324941"><a href="/opinion/324941/united-states-of-america-ex-rel-thomas-kirby-v-david-r-sturges-chairman/#405" aria-description="Citation for case: United States of America Ex Rel. Thomas Kirby v. David R....">510 F. 2d 397, 405-406</a></span> (CA7 1975), the arguments in favor of fashioning new rules to minimize the danger of convicting the innocent on the basis of unreliable eyewitness testimony carry substantial force. Nevertheless, <span class="star-pagination">*118</span> for the reasons stated in that opinion, as well as those stated by the Court today, I am persuaded that this rulemaking function can be performed "more effectively by the legislative process than by a somewhat clumsy judicial fiat," <span class="citation" data-id="324941"><a href="/opinion/324941/united-states-of-america-ex-rel-thomas-kirby-v-david-r-sturges-chairman/#408" aria-description="Citation for case: United States of America Ex Rel. Thomas Kirby v. David R...."><i>id.,</i> at 408</a></span>, and that the Federal Constitution does not foreclose experimentation by the States in the development of such rules.</p>
<p>Second, in evaluating the admissibility of particular identification testimony it is sometimes difficult to put other evidence of guilt entirely to one side.<sup>[*]</sup> MR. JUSTICE BLACKMUN'S opinion for the Court carefully avoids this pitfall and correctly relies only on appropriate indicia of the reliability of the identification itself. Although I consider the factual question in this case extremely close, I am persuaded that the Court has resolved it properly.</p>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE BRENNAN joins, dissenting.</p>
<p>Today's decision can come as no surprise to those who have been watching the Court dismantle the protections against mistaken eyewitness testimony erected a decade ago in <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967); <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967); and <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span> (1967). But it is still distressing to see the Court virtually ignore the teaching of experience embodied in those decisions and blindly uphold the conviction of a defendant who may well be innocent.</p>
<p></p>
<h2>
<span class="star-pagination">*119</span> I</h2>
<p>The magnitude of the Court's error can be seen by analyzing the cases in the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> trilogy and the decisions following it. The foundation of the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> trilogy was the Court's recognition of the "high incidence of miscarriage of justice" resulting from the admission of mistaken eyewitness identification evidence at criminal trials. <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#228" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 228</a></span>. Relying on numerous studies made over many years by such scholars as Professor Wigmore and Mr. Justice Frankfurter, the Court concluded that "[t]he vagaries of eyewitness identification are well-known; the annals of criminal law are rife with instances of mistaken identification." <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Ibid.</a></span></i> It is, of course, impossible to control one source of such errorsthe faulty perceptions and unreliable memories of witnessesexcept through vigorously contested trials conducted by diligent counsel and judges. The Court in the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> cases acted, however, to minimize the more preventable threat posed to accurate identification by "the degree of suggestion inherent in the manner in which the prosecution presents the suspect to witnesses for pretrial identification." <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Ibid.</a></span></i></p>
<p>The Court did so in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i>Gilbert</i> v. <i>California</i> by prohibiting the admission at trial of evidence of pretrial confrontations at which an accused was not represented by counsel. Further protection was afforded by holding that an in-court identification following an uncounseled lineup was allowable only if the prosecution could clearly and convincingly demonstrate that it was not tainted by the constitutional violation. Only in this way, the Court held, could confrontations fraught with the danger of misidentification be made fairer, and could Sixth Amendment rights to assistance of counsel and confrontation of witnesses at trial be effectively preserved. The crux of the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> decisions, however, was the unusual threat to the truth-seeking process posed by the frequent untrustworthiness of eyewitness identification <span class="star-pagination">*120</span> testimony. This, combined with the fact that juries unfortunately are often unduly receptive to such evidence,<sup>[1]</sup> is the fundamental fact of judicial experience ignored by the Court today.</p>
<p><i>Stovall</i> v. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Denno</a></span></i><i>,</i> while holding that the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> prophylactic rules were not retroactive, was decided at the same time and reflects the same concerns about the reliability of identification testimony. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> recognized that, regardless of Sixth Amendment principles, "the conduct of a confrontation" may be "so unnecessarily suggestive and conducive to irreparable mistaken identification" as to deny due process of law. 388 U. S., at 301-302. The pretrial confrontation in <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> was plainly suggestive,<sup>[2]</sup> and evidence of it was introduced at trial along with the witness' in-court identification. The Court ruled that there had been no violation of due process, however, because the unusual necessity for the procedure<sup>[3]</sup> outweighed the danger of suggestion.</p>
<p><i>Stovall</i> thus established a due proceess right of criminal suspects to be free from confrontations that, under all the circumstances, are unnecessarily suggestive. The right was enforceable by exclusion at trial of evidence of the constitutionally invalid identification. Comparison with <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i>Gilbert</i> confirms this interpretation. Where their Sixth <span class="star-pagination">*121</span> Amendment holding did not apply, <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> found an analogous Fourteenth Amendment right to a lineup conducted in a fundamentally fair manner. This interpretation is reinforced by the Court's statement that "a claimed violation of due process of law <i>in the conduct of a confrontation</i> depends on the totality of the circumstances surrounding it." 388 U. S., at 302 (emphasis added). Significantly, several years later, <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> was viewed in precisely the same way, even as the Court limited <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i>Gilbert</i> to post-indictment confrontations: "The Due Process Clause . . . <i>forbids a lineup</i> that is unnecessarily suggestive and conducive to irreparable mistaken identification. <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span>; <i>Foster</i> v. <i>California,</i> <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">394 U. S. 440</a></span>." <i>Kirby</i> v. <i>Illinois,</i> <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#691" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682, 691</a></span> (1972) (emphasis added).<sup>[4]</sup></p>
<p>The development of due process protections against mistaken identification evidence, begun in <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>,</i> was continued in <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span> (1968). There, the Court developed a different rule to deal with the admission of in-court identification testimony that the accused claimed had been fatally tainted by a previous suggestive confrontation. In <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span>,</i> the exclusionary effect of <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> had already been accomplished, since the prosecution made no use of the suggestive confrontation. <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span>,</i> therefore, did not deal with the constitutionality of the pretrial identification procedure. The only question was the impact of the <span class="star-pagination">*122</span> Due Process Clause on an in-court identification that was not itself unnecessarily suggestive. <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> held that due process was violated by the later identification if the pretrial procedure had been "so impermissibly suggestive as to give rise to a very substantial likelihood of irreparable misidentification." <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U. S., at 384</a></span>. This test focused, not on the necessity for the challenged pretrial procedure, but on the degree of suggestiveness that it entailed. In applying this test, the Court understandably considered the circumstances surrounding the witnesses' initial opportunity to view the crime. Finding that any suggestion in the pretrial confrontation had not affected the fairness of the in-court identification, <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> rejected petitioner's due process attack on his conviction.</p>
<p>Again, comparison with the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> cases is instructive. The inquiry mandated by <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> is similar to the independent-source test used in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> where an in-court identification is sought following an uncounseled lineup. In both cases, the issue is whether the witness is identifying the defendant solely on the basis of his memory of events at the time of the crime, or whether he is merely remembering the person he picked out in a pretrial procedure. Accordingly, in both situations, the relevant inquiry includes factors bearing on the accuracy of the witness' identification, including his opportunity to view the crime.</p>
<p>Thus, <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> and <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> established two different due process tests for two very different situations. Where the prosecution sought to use evidence of a questionable pretrial identification, <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> required its exclusion, because due process had been violated by the confrontation, unless the necessity for the unduly suggestive procedure outweighed its potential for generating an irreparably mistaken identification. The <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> test, on the other hand, was directed to ascertaining due process violations in the introduction of in-court identification testimony that the defendant claimed was tainted by pretrial procedures. In the latter situation, a <span class="star-pagination">*123</span> court could consider the reliability of the identification under all the circumstances.<sup>[5]</sup></p>
<p>This distinction between <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> and <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> was preserved in two succeeding cases. <i>Foster</i> v. <i>California,</i> <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">394 U. S. 440</a></span> (1969), like <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>,</i> involved both unduly suggestive pretrial procedures, evidence of which was introduced at trial, and a tainted in-court identification. Accordingly, <i><span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">Foster</a></span></i> applied the <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> test, <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/#442" aria-description="Citation for case: Foster v. California">394 U. S., at 442</a></span>, and held that the police "<i>procedure</i> so undermined the reliability of the eyewitness identification as to violate due process." <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/#443" aria-description="Citation for case: Foster v. California"><i>Id.,</i> at 443</a></span> (emphasis added). In contrast, in <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970), where the witness' pretrial identification was not used to bolster his in-court identification, the plurality opinion applied the test enunciated in <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span>.</i> It concluded that an in-court identification did not violate due process because it did not stem from an allegedly suggestive lineup.</p>
<p>The Court inexplicably seemed to erase the distinction between <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> and <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> situations in <i>Neil</i> v. <i>Biggers,</i> <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">409 U. S. 188</a></span> (1972). In <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> there was a pretrial confrontation that was clearly both suggestive and unnecessary.<sup>[6]</sup> Evidence of this, together with an in-court identification, was admitted at trial. <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> was, in short, a case plainly cast in the <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> mold. Yet the Court, without explanation or apparent recognition of the distinction, applied the <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> <span class="star-pagination">*124</span> test. The Court stated: "[T]he primary evil to be avoided is `a very substantial likelihood of irreparable misidentification.' <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U. S., at 384</a></span>. . . . It is the likelihood of misidentification which violates a defendant's right to due process . . . ." <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#198" aria-description="Citation for case: Neil v. Biggers">409 U. S., at 198</a></span>. While this statement accurately describes the lesson of <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span>,</i> it plainly ignores the teaching of <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> and <i><span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">Foster</a></span></i> that an unnecessarily suggestive pretrial confrontation itself violates due process.</p>
<p>But the Court did not simply disregard the due process analysis of <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>.</i> It went on to take the <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> standard for assessing the constitutionality of an in-court identification "`a very substantial likelihood of irreparable misidentification'" and transform it into the "standard for the admissibility of testimony concerning [an] out-of-court identification." <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#198" aria-description="Citation for case: Neil v. Biggers">409 U. S., at 198</a></span>. It did so by deleting the word "irreparable" from the <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> formulation. This metamorphosis could be accomplished, however, only by ignoring the fact that <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>,</i> fortified only months earlier by <i>Kirby</i> v. <i><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Illinois</a></span>,</i> see <i>supra,</i> at 121, had established a test for precisely the same situation that focused on the need for the suggestive procedure. It is not surprising that commentators almost unanimously mourned the demise of <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> in the <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> decision.<sup>[7]</sup></p>
<p></p>
<h2>II</h2>
<p>Apparently, the Court does not consider <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> controlling in this case. I entirely agree, since I believe that <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> <span class="star-pagination">*125</span> was wrongly decided. The Court, however, concludes that <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> is distinguishable because it, like the identification decisions that preceded it, involved a pre-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> confrontation, and because a paragraph in <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> itself, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#198" aria-description="Citation for case: Neil v. Biggers">409 U. S., at 198-199</a></span>, seems to distinguish between pre- and post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> confrontations. Accordingly, in determining the admissibility of the post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> identification in this case, the Court considers two alternatives, a <i>per se</i> exclusionary rule and a totality-of-the-circumstances approach. <i>Ante,</i> at 110-111. The Court weighs three factors in deciding that the totality approach, which is essentially the test used in <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span>,</i> should be applied. <i>Ante,</i> at 111-113. In my view, the Court wrongly evaluates the impact of these factors.</p>
<p>First, the Court acknowledges that one of the factors, deterrence of police use of unnecessarily suggestive identification procedures, favors the <i>per se</i> rule. Indeed, it does so heavily, for such a rule would make it unquestionably clear to the police they must never use a suggestive procedure when a fairer alternative is available. I have no doubt that conduct would quickly conform to the rule.</p>
<p>Second, the Court gives passing consideration to the dangers of eyewitness identification recognized in the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> trilogy. It concludes, however, that the grave risk of error does not justify adoption of the <i>per se</i> approach because that would too often result in exclusion of relevant evidence. In my view, this conclusion totally ignores the lessons of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>.</i> The dangers of mistaken identification are, as <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> held, simply too great to permit unnecessarily suggestive identifications. Neither <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> nor the Court's opinion today points to any contrary empirical evidence. Studies since <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> have only reinforced the validity of its assessment of the dangers of identification testimony.<sup>[8]</sup> While the Court is "content to <span class="star-pagination">*126</span> rely on the good sense and judgment of American juries," <i>ante,</i> at 116, the impetus for <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> and <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> was repeated miscarriages of justice resulting from juries' willingness to credit inaccurate eyewitness testimony.</p>
<p>Finally, the Court errs in its assessment of the relative impact of the two approaches on the administration of justice. The Court relies most heavily on this factor, finding that "reversal is a Draconian sanction" in cases where the identification is reliable despite an unnecessarily suggestive procedure used to obtain it. Relying on little more than a strong distaste for "inflexible rules of exclusion," the Court rejects the <i>per se</i> test. <i>Ante,</i> at 113. In so doing, the Court disregards two significant distinctions between the <i>per se</i> rule advocated in this case and the exclusionary remedies for certain other constitutional violations.</p>
<p>First, the <i>per se</i> rule here is not "inflexible." Where evidence is suppressed, for example, as the fruit of an unlawful search, it may well be forever lost to the prosecution. Identification evidence, however, can by its very nature be readily and effectively reproduced. The in-court identification, permitted under <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> if it has a source independent of an uncounseled or suggestive procedure, is one example. Similarly, when a prosecuting attorney learns that there has been a suggestive confrontation, he can easily arrange another <span class="star-pagination">*127</span> lineup conducted under scrupulously fair conditions. Since the same factors are evaluated in applying both the Court's totality test and the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i>-<span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States"><i>Simmons</i></a></span> independent-source inquiry, any identification which is "reliable" under the Court's test will support admission of evidence concerning such a fairly conducted lineup. The evidence of an additional, properly conducted confrontation will be more persuasive to a jury, thereby increasing the chance of a justified conviction where a reliable identification was tainted by a suggestive confrontation. At the same time, however, the effect of an unnecessarily suggestive identificationwhich has no value whatsoever in the law enforcement processwill be completely eliminated.</p>
<p>Second, other exclusionary rules have been criticized for preventing jury consideration of relevant and usually reliable evidence in order to serve interests unrelated to guilt or innocence, such as discouraging illegal searches or denial of counsel. Suggestively obtained eyewitness testimony is excluded, in contrast, precisely because of its unreliability and concomitant irrelevance. Its exclusion both protects the integrity of the truth-seeking function of the trial and discourages police use of needlessly inaccurate and ineffective investigatory methods.</p>
<p>Indeed, impermissibly suggestive identifications are not merely worthless law enforcement tools. They pose a grave threat to society at large in a more direct way than most governmental disobedience of the law, see <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#471" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 471, 485</a></span> (1928) (Brandeis, J., dissenting). For if the police and the public erroneously conclude, on the basis of an unnecessarily suggestive confrontation, that the right man has been caught and convicted, the real outlaw must still remain at large. Law enforcement has failed in its primary function and has left society unprotected from the depredations of an active criminal.</p>
<p><span class="star-pagination">*128</span> For these reasons, I conclude that adoption of the <i>per se</i> rule would enhance, rather than detract from, the effective administration of justice. In my view, the Court's totality test will allow seriously unreliable and misleading evidence to be put before juries. Equally important, it will allow dangerous criminals to remain on the streets while citizens assume that police action has given them protection. According to my calculus, all three of the factors upon which the Court relies point to acceptance of the <i>per se</i> approach.</p>
<p>Even more disturbing than the Court's reliance on the totality test, however, is the analysis it uses, which suggests a reinterpretation of the concept of due process of law in criminal cases. The decision suggests that due process violations in identification procedures may not be measured by whether the government employed procedures violating standards of fundamental fairness. By relying on the probable accuracy of a challenged identification, instead of the necessity for its use, the Court seems to be ascertaining whether the defendant was probably guilty. Until today, I had thought that "Equal justice under law" meant that the existence of constitutional violations did not depend on the race, sex, religion, nationality, or likely guilt of the accused. The Due Process Clause requires adherence to the same high standard of fundamental fairness in dealing with every criminal defendant, whatever his personal characteristics and irrespective of the strength of the State's case against him. Strong evidence that the defendant is guilty should be relevant only to the determination whether an error of constitutional magnitude was nevertheless harmless beyond a reasonable doubt. See <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967). By importing the question of guilt into the initial determination of whether there was a constitutional violation, the apparent effect of the Court's decision is to undermine the protection afforded by the Due Process Clause. "It is therefore important to note that the state courts remain free, in interpreting state constitutions, to <span class="star-pagination">*129</span> guard against the evil clearly identified by this case." <i>Oregon</i> v. <i>Mathiason,</i> <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#499" aria-description="Citation for case: Oregon v. Mathiason">429 U. S. 492, 499</a></span> (1977) (MARSHALL, J., dissenting).<sup>[9]</sup></p>
<p></p>
<h2>III</h2>
<p>Despite my strong disagreement with the Court over the proper standards to be applied in this case, I am pleased that its application of the totality test does recognize the continuing vitality of <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>.</i> In assessing the reliability of the identification, the Court mandates weighing "the corrupting effect of the suggestive identification itself" against the "indicators of [a witness'] ability to make an accurate identification." <i>Ante,</i> at 114, 116. The Court holds, as <i>Neil</i> v. <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> failed to, that a due process identification inquiry must take account of the suggestiveness of a confrontation and the likelihood that it led to misidentification, as recognized in <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> and <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>.</i> Thus, even if a witness did have an otherwise adequate opportunity to view a criminal, the later use of a highly suggestive identification procedure can render his testimony inadmissible. Indeed, it is my view that, assuming applicability of the totality test enunciated by the Court, the facts of the present case require that result.</p>
<p>I consider first the opportunity that Officer Glover had to view the suspect. Careful review of the record shows that he could see the heroin seller only for the time it took to speak three sentences of four or five short words, to hand over some money, Tr. 29-30, and later after the door reopened, to receive the drugs in return, <i>id.,</i> at 30, 31-32. The entire face-to-face transaction could have taken as little as 15 or 20 seconds. But during this time, Glover's attention was not focused exclusively on the seller's face. He observed that the door <span class="star-pagination">*130</span> was opened 12 to 18 inches, <i>id.,</i> at 29, that there was a window in the room behind the door, <i>id.,</i> at 33, and, most importantly, that there was a woman standing behind the man, <i>id.,</i> at 29, 30. Glover was, of course, also concentrating on the details of the transactionhe must have looked away from the seller's face to hand him the money and receive the drugs. The observation during the conversation thus may have been as brief as 5 or 10 seconds.</p>
<p>As the Court notes, Glover was a police officer trained in and attentive to the need for making accurate identifications. Nevertheless, both common sense and scholarly study indicate that while a trained observer such as a police officer "is somewhat less likely to make an erroneous identification than the average untrained observer, the mere fact that he has been so trained is no guarantee that he is correct in a specific case. His identification testimony should be scrutinized just as carefully as that of the normal witness." <span class="citation" data-id="8988513"><a href="/opinion/8996170/wallace-v-smith/#1" aria-description="Citation for case: Wallace v. Smith">Wall, <i>supra,</i> n. 1</a></span>, at 14; see also Levine &amp; Tapp, <i>supra,</i> n. 8, at 1088. Moreover, "identifications made by policemen in highly competitive activities, such as undercover narcotic agents . . . , should be scrutinized with special care." <span class="citation" data-id="8988513"><a href="/opinion/8996170/wallace-v-smith/#1" aria-description="Citation for case: Wallace v. Smith">Wall, <i>supra,</i> n. 1</a></span>, at 14. Yet it is just such a searching inquiry that the Court fails to make here.</p>
<p>Another factor on which the Court reliesthe witness' degree of certainty in making the identificationis worthless as an indicator that he is correct.<sup>[10]</sup> Even if Glover had been unsure initially about his identification of respondent's picture, by the time he was called at trial to present a key piece of evidence for the State that paid his salary, it is impossible to imagine his responding negatively to such questions as "is there any doubt in your mind whatsoever" that the identification was correct. Tr. 34, 41-42. As the Court noted in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>:</i> "`It is a matter of common experience that, once a <span class="star-pagination">*131</span> witness has picked out the accused at the [pretrial confrontation], he is not likely to go back on his word later on.'" 388 U. S., at 229, quoting Williams &amp; Hammelmann, Identification ParadesI, Crim. L. Rev. 479, 482 (1963).</p>
<p>Next, the Court finds that because the identification procedure took place two days after the crime, its reliability is enhanced. While such temporal proximity makes the identification more reliable than one occurring months later, the fact is that the greatest memory loss occurs within hours after an event. After that, the dropoff continues much more slowly.<sup>[11]</sup> Thus, the reliability of an identification is increased only if it was made within several hours of the crime. If the time gap is any greater, reliability necessarily decreases.</p>
<p>Finally, the Court makes much of the fact that Glover gave a description of the seller to D'Onofrio shortly after the incident. Despite the Court's assertion that because "Glover himself was a Negro and unlikely to perceive only general features of `hundreds of Hartford black males,' as the Court of Appeals stated," <i>ante,</i> at 115, the description given by Glover was actually no more than a general summary of the seller's appearance. See <i>ante,</i> at 101. We may discount entirely the seller's clothing, for that was of no significance later in the proceeding. Indeed, to the extent that Glover noticed clothes, his attention was diverted from the seller's face. Otherwise, Glover merely described vaguely the seller's height, skin color, hairstyle, and build. He did say that the <span class="star-pagination">*132</span> seller had "high cheekbones," but there is no other mention of facial features, nor even an estimate of age. Conspicuously absent is any indication that the seller was a native of the West Indies, certainly something which a member of the black community could immediately recognize from both appearance and accent.<sup>[12]</sup></p>
<p>From all of this, I must conclude that the evidence of Glover's ability to make an accurate identification is far weaker than the Court finds it. In contrast, the procedure used to identify respondent was both extraordinarily suggestive and strongly conducive to error. In dismissing "the corrupting effect of the suggestive identification" procedure here, <i>ante,</i> at 116, the Court virtually grants the police license to convict the innocent. By displaying a single photograph of respondent to the witness Glover under the circumstances in this record almost everything that could have been done wrong was done wrong.</p>
<p>In the first place, there was no need to use a photograph at all. Because photos are static, two-dimensional, and often outdated, they are "clearly inferior in reliability" to corporeal procedures. <span class="citation" data-id="8988513"><a href="/opinion/8996170/wallace-v-smith/#1" aria-description="Citation for case: Wallace v. Smith">Wall, <i>supra,</i> n. 1</a></span>, at 70; <i>People</i> v. <i>Gould,</i> <span class="citation" data-id="1801408"><a href="/opinion/1801408/people-v-gould/#631" aria-description="Citation for case: People v. Gould">54 Cal. 2d 621, 631</a></span>, <span class="citation" data-id="1801408"><a href="/opinion/1801408/people-v-gould/#870" aria-description="Citation for case: People v. Gould">354 P. 2d 865, 870</a></span> (1960). While the use of photographs is justifiable and often essential where the police have no knowledge of an offender's identity, the poor reliability of photos makes their use inexcusable where any other means of identification is available. Here, since Detective D'Onofrio believed that he knew the seller's identity, see <i>ante,</i> at 101, 115, further investigation without resort to a photographic showup was easily possible. With little inconvenience, a corporeal <span class="star-pagination">*133</span> lineup including Brathwaite might have been arranged.<sup>[13]</sup> Properly conducted, such a procedure would have gone far to remove any doubt about the fairness and accuracy of the identification.<sup>[14]</sup></p>
<p>Worse still than the failure to use an easily available corporeal identification was the display to Glover of only a single picture, rather than a photo array. With good reason, such single-suspect procedures have "been widely condemned." <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#302" aria-description="Citation for case: Stovall v. Denno">388 U. S., at 302</a></span>. They give no assurance that the witness can identify the criminal from among a number of persons of similar appearance, surely the strongest evidence that there was no misidentification. In <i>Simmons</i> v. <i>United States</i><i>,</i> our first decision involving photographic identification, we recognized the danger that a witness seeing a suggestively displayed picture will "retain in his memory the image of the photograph rather than of the person actually seen." <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#383" aria-description="Citation for case: Simmons v. United States">390 U. S., at 383-384</a></span>. "Subsequent identification of the accused then shows nothing except that the picture was a good likeness." Williams &amp; Hammelmann, <i>supra,</i> n. 1, at 484. As <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> warned, the danger of error is at its greatest when "the police display to the witness only the picture of a single individual . . . [and] is also heightened if the police indicate to the witness that they have other evidence that . . . the perso[n] pictured committed the crime." <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#383" aria-description="Citation for case: Simmons v. United States">390 U. S., at 383</a></span>. <span class="star-pagination">*134</span> See also ALI, Model Code of Pre-Arraignment Procedure §§ 160.2 (2), (5) (1975).</p>
<p>The use of a single picture (or the display of a single live suspect, for that matter) is a grave error, of course, because it dramatically suggests to the witness that the person shown must be the culprit. Why else would the police choose the person? And it is deeply ingrained in human nature to agree with the expressed opinions of othersparticularly others who should be more knowledgeablewhen making a difficult decision.<sup>[15]</sup> In this case, moreover, the pressure was not limited to that inherent in the display of a single photograph. Glover, the identifying witness, was a state police officer on special assignment. He knew that D'Onofrio, an experienced Hartford narcotics detective, presumably familiar with local drug operations, believed respondent to be the seller. There was at work, then, both loyalty to another police officer and deference to a better-informed colleague.<sup>[16]</sup> Finally, of course, there was Glover's knowledge that without an identification <span class="star-pagination">*135</span> and arrest, government funds used to buy heroin had been wasted.</p>
<p>The Court discounts this overwhelming evidence of suggestiveness, however. It reasons that because D'Onofrio was not present when Glover viewed the photograph, there was "little pressure on the witness to acquiesce in the suggestion." <i>Ante,</i> at 116. That conclusion blinks psychological reality.<sup>[17]</sup> There is no doubt in my mind that even in D'Onofrio's absence, a clear and powerful message was telegraphed to Glover as he looked at respondent's photograph. He was emphatically told that "<i>this</i> is the man," and he responded by identifying respondent then and at trial "whether or not he was in fact `the man.'" <i>Foster</i> v. <i>California,</i> <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/#443" aria-description="Citation for case: Foster v. California">394 U. S., at 443</a></span>.<sup>[18]</sup></p>
<p>I must conclude that this record presents compelling evidence that there was "a very substantial likelihood of misidentification" of respondent Brathwaite. The suggestive <span class="star-pagination">*136</span> display of respondent's photograph to the witness Glover likely erased any independent memory that Glover had retained of the seller from his barely adequate opportunity to observe the criminal.</p>
<p></p>
<h2>IV</h2>
<p>Since I agree with the distinguished panel of the Court of Appeals that the legal standard of <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> should govern this case, but that even if it does not, the facts here reveal a substantial likelihood of misidentification in violation of respondent's right to due process of law, I would affirm the grant of habeas corpus relief. Accordingly, I dissent from the Court's reinstatement of respondent's conviction.</p>
<h2>NOTES</h2>
<p>[1]  The references are to the transcript of the trial in the Superior Court of Hartford County, Conn. The United States District Court, on federal habeas, pursuant to agreement of the parties, Tr. of Oral Arg. 23, conducted no evidentiary hearing.</p>
<p>[2]  It appears that the door on which Glover knocked may not have been that of the Cicero apartment. Petitioner concedes, in any event, that the transaction effected "was with some other person than had been intended." <i>Id.,</i> at 4.</p>
<p>[3]  This was Glover's testimony. Brown later was called as a witness for the prosecution. He testified on direct examination that, due to his then use of heroin, he had no clear recollection of the details of the incident. Tr. 81-82. On cross-examination, as in an interview with defense counsel the preceding day, he said that it was a woman who opened the door, received the money, and thereafter produced the narcotics. <i>Id.,</i> at 84, 86-87. On redirect, he acknowledged that he was using heroin daily at the time, that he had had some that day, and that there was "an inability to recall and remember events." <i>Id.,</i> at 88-89.</p>
<p>[4]  Respondent testified: "Lots of times I have been there before in that building." He also testified that Mrs. Ramsey was a friend of his wife, that her apartment was the only one in the building he ever visited, and that he and his family, consisting of his wife and five children, did not live there but at 453 Albany Avenue, Hartford. <i>Id.,</i> at 111-113.</p>
<p>[5]  These statutes have since been amended in ways that do not affect the present litigation. See <span class="citation no-link">1971 Conn. Pub. Acts 812</span>, § 1; <span class="citation no-link">1972 Conn. Pub. Acts 278</span>, §§ 25 and 26; Conn. Pub. Acts 73-137, § 10; Conn. Pub. Acts 74-332, §§ 1 and 3; Conn. Pub. Acts 75-567, § 65.</p>
<p>[6]  Neither party submitted a request to the District Court for an independent factual hearing on respondent's claims. See n. 1, <i>supra.</i></p>
<p>[7]  Although no objection was made in the state trial to the admission of the identification testimony and the photograph, the issue of their propriety as evidence was raised on the appeal to the Supreme Court of Connecticut. Petitioner has asserted no claims related to the failure of the respondent either to exhaust state remedies or to make contemporaneous objections. The District Court and the Court and the Court of Appeals, each for a somewhat different reason, App. to Pet. for Cert. 7a-8a; <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#366" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d, at 366</a></span>, concluded that the merits were properly before them. We are not inclined now to rule otherwise.</p>
<p>[8]  <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> involved photographs, mostly group ones, shown to bank-teller victims who made in-court identifications. The Court discussed the "chance of misidentification," <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#383" aria-description="Citation for case: Simmons v. United States">390 U. S., at 383</a></span>; declined to prohibit the procedure "either in the exercise of our supervisory power or, still less, as a matter of constitutional requirement," <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States"><i>id.,</i> at 384</a></span>; and held that each case must be considered on its facts and that a conviction would be set aside only if the identification procedure "was so impermissibly suggestive as to give rise to a very substantial likelihood of irreparable misidentification." <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Ibid.</a></span></i> The out-of-court identification was not offered. Mr. Justice Black would have denied Simmons' due process claim as frivolous. <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#395" aria-description="Citation for case: Simmons v. United States"><i>Id.,</i> at 395-396</a></span>.
</p>
<p><i>Foster</i> concerned repeated confrontations between a suspect and the manager of an office that had been robbed. At a second lineup, but not at the first and not at a personal one-to-one confrontation, the manager identified the suspect. At trial he testified as to this and made an in-court identification. The Court reaffirmed the <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> standard and then concluded that the repeated confrontations were so suggestive as to violate due process. The case was remanded for the state courts to consider the question of harmless error.</p>
<p>In <i><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">Coleman</a></span></i> a plurality of the Court was of the view that the trial court did not err when it found that the victim's in-court identifications did not stem from a lineup procedure so impermissibly suggestive as to give rise to a substantial likelihood of misidentification. <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#5" aria-description="Citation for case: Coleman v. Alabama">399 U. S., at 5-6</a></span>.</p>
<p>[9]  MR. JUSTICE MARSHALL argues in dissent that our cases have "established two different due process tests for two very different situations." <i>Post,</i> at 122. Pretrial identifications are to be covered by <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>,</i> which is said to require exclusion of evidence concerning unnecessarily suggestive pretrial identifications without regard to reliability. In-court identifications, on the other hand, are to be governed by <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> and admissibility turns on reliability. The Court's cases are sorted into one category or the other. <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span>,</i> which clearly adopts the reliability of the identification as the guiding factor in the admissibility of both pretrial and in-court identifications, is condemned for mixing the two lines and for adopting a uniform rule.
</p>
<p>Although it must be acknowledged that our cases are not uniform in their emphasis, they hardly suggest the formal structure the dissent would impose on them. If our cases truly established two different rules, one might expect at some point at least passing reference to the fact. There is none. And if <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> departed so grievously from the past cases, it is surprising that there was not at least some mention of the point in MR. JUSTICE BRENNAN'S dissent. In fact, the cases are not so readily sorted as the dissent suggests. Although <i><span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">Foster</a></span></i> involved both in-court and out-of-court identifications, the Court seemed to apply only a single standard for both. And although <i><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">Coleman</a></span></i> involved only an in-court identification, the plurality cited <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> for the guiding rule that the claim was to be assessed on the "totality of the surrounding circumstances." <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#4" aria-description="Citation for case: Coleman v. Alabama">399 U. S., at 4</a></span>. Thus, <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> is not properly seen as a departure from the past cases, but as a synthesis of them.</p>
<p>[10]  Although the <i>per se</i> approach demands the exclusion of testimony concerning unnecessarily suggestive identifications, it does permit the admission of testimony concerning a subsequent identification, including an in-court identification, if the subsequent identification is determined to be reliable. <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#367" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d, at 367</a></span>. The totality approach, in contrast, is simpler: if the challenged identification is reliable, then testimony as to it and any identification in its wake is admissible.</p>
<p>[11]  The Fourth Circuit's then very recent decision in <i>Smith</i> v. <i>Coiner,</i> <span class="citation" data-id="308320"><a href="/opinion/308320/edward-lee-smith-v-ira-m-coiner-warden-of-the-west-virginia-state/" aria-description="Citation for case: Edward Lee Smith v. Ira M. Coiner, Warden of the West...">473 F. 2d 877</a></span> (1973), was described as one applying the second, or totality, test. <span class="citation" data-id="8891137"><a href="/opinion/8904042/stanley-v-cox/#55" aria-description="Citation for case: Stanley v. Cox">486 F. 2d, at 55</a></span>.</p>
<p>[12]  The interest in obtaining convictions of the guilty also urges the police to adopt procedures that show the resulting identification to be accurate. Suggestive procedures often will vitiate the weight of the evidence at trial and the jury may tend to discount such evidence. Cf. McGowan, Constitutional Interpretation and Criminal Identification, <span class="citation no-link">12 Wm. &amp; Mary L. Rev. 235</span>, 241 (1970).</p>
<p>[13]  Unlike a warrantless search, a suggestive preindictment identification procedure does not in itself intrude upon a constitutionally protected interest. Thus, considerations urging the exclusion of evidence deriving from a constitutional violation do not bear on the instant problem. See <i>United States ex rel. Kirby</i> v. <i>Sturges,</i> <span class="citation" data-id="324941"><a href="/opinion/324941/united-states-of-america-ex-rel-thomas-kirby-v-david-r-sturges-chairman/#406" aria-description="Citation for case: United States of America Ex Rel. Thomas Kirby v. David R....">510 F. 2d 397, 406</a></span> (CA7 1975).</p>
<p>[14]  "In essence what the <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> due process right protects is an evidentiary interest. . . .
</p>
<p>"It is part of our adversary system that we accept at trial much evidence that has strong elements of untrustworthinessan obvious example being the testimony of witnesses with a bias. While identification testimony is significant evidence, such testimony is still only evidence, and, unlike the presence of counsel, is not a factor that goes to the very heart the `integrity'of the adversary process.</p>
<p>"Counsel can both cross-examine the identification witnesses and argue in summation as to factors causing doubts as to the accuracy of the identificationincluding reference to both any suggestibility in the identification procedure and any countervailing testimony such as alibi." <i>Clemons</i> v. <i>United States,</i> 133 U. S. App. D. C. 27, 48, <span class="citation" data-id="9454404"><a href="/opinion/284140/malcus-t-clemons-v-united-states-of-america-david-e-clark-v-united/#1251" aria-description="Citation for case: Malcus T. Clemons v. United States of America, David E....">408 F. 2d 1230, 1251</a></span> (1968) (concurring opinion) (footnote omitted), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./394/964/">394 U. S. 964</a></span> (1969).</p>
<p>[15]  Mrs. Ramsey was not a witness at the trial.</p>
<p>[16]  We are not troubled, as was the Court of Appeals, by the "long and unexplained delay" in respondent's arrest. <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#372" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d, at 372</a></span>. That arrest took place on July 27. The toxicological report verifying the substance sold as heroin had issued only 11 days earlier, on July 16. Those 11 days after verification of the contents of the glassine bags do not constitute, for us, a "long" period. And with the positive toxicological report having been received within a fortnight, the arrest's delay perhaps is not "unexplained."</p>
<p>[*]  In this case, for example, the fact that the defendant was a regular visitor to the apartment where the drug transaction occurred tends to confirm his guilt. In the <i><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span></i> case, where the conviction was for robbery, the fact that papers from the victim's wallet were found in the possession of the defendant made it difficult to question the reliability of the identification. These facts should not, however, be considered to support the admissibility of eyewitness testimony when applying the criteria identified in <i>Neil</i> v. <i>Biggers,</i> <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">409 U. S. 188</a></span>. Properly analyzed, however, such facts would be relevant to a question whether error, if any, in admitting identification testimony was harmless.</p>
<p>[1]  See, <i>e. g.,</i> P. Wall, Eye-Witness Identification in Criminal Cases 19-23 (1965); N. Sobel, Eye-Witness Identification: Legal and Practical Problems, §§ 3.01, 3.02, 30 (1972); Hammelmann &amp; Williams, Identification ParadesII, Crim. L. Rev. 545, 550 (1963).</p>
<p>[2]  The accused, a Negro, was brought handcuffed by seven white police officers and employees of the District Attorney to the hospital room of the only witness to a murder. As the Court said of this encounter: "It is hard to imagine a situation more clearly conveying the suggestion to the witness that the one presented is believed to be guilty by the police. See Frankfurter, The Case of Sacco and Vanzetti 31-32." <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#234" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 234</a></span> (1967).</p>
<p>[3]  The police reasonably feared that the witness might die before any less suggestive confrontation could be arranged.</p>
<p>[4]  See also, McGowan, Constitutional Interpretation and Criminal Identification, <span class="citation no-link">12 Wm. &amp; Mary L. Rev. 235</span>, 240 (1970).
</p>
<p>If the test enunciated in <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> permitted any consideration of the witness' opportunity to observe the offender at the time of the crime, it was only in the narrowly circumscribed context of ascertaining the extent to which the challenged procedure was "conducive to irreparable mistaken identification." It is noteworthy, however, that in applying its test in <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>,</i> the Court did not advert to the significant circumstantial evidence of guilt, see <i>United States ex rel. Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9451306"><a href="/opinion/270486/united-states-ex-rel-theodore-r-stovall-v-honorable-wilfred-denno-as/#733" aria-description="Citation for case: United States Ex Rel. Theodore R. Stovall v. Honorable...">355 F. 2d 731, 733-734</a></span> (CA2 1966), nor discuss any factors bearing on the witness' opportunity to view the assailant.</p>
<p>[5]  Mr. Justice Harlan, writing for the Court in <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span>,</i> acknowledged that there was a distinction between that case and <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>.</i> After describing the factual setting and the applicable due process test, he noted that "[t]his standard accords with our resolution of a similar issue in <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>.</i>" <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U. S., at 384</a></span>. He pointedly did not say that the cases were the same, nor did he rely on <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> to set the standard.</p>
<p>[6]  "The showup itself consisted of two detectives walking respondent past the victim." <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#195" aria-description="Citation for case: Neil v. Biggers">409 U. S., at 195</a></span>. The police also ordered respondent to repeat the words used by the criminal. Inadequate efforts were made to secure participants for a lineup, and there was no pressing need to use a showup.</p>
<p>[7]  See, <i>e. g.,</i> N. Sobel, <i>supra,</i> n. 1, §§ 37, 38 (Supp. 1977); Grano, <i>Kirby, Biggers,</i> and <i>Ash:</i> Do Any Constitutional Safeguards Remain Against the Danger of Convicting the Innocent? <span class="citation no-link">72 Mich. L. Rev. 717</span> (1974); M. Hartman &amp; N. Goldberg, The Death of the Warren Court, The Doctrine of Suggestive Identification, 32 NLADA Briefcase 78 (1974); Pulaski, <i>Neil</i> v. <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span>:</i> The Supreme Court Dismantles the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> Trilogy's Due Process Protection, <span class="citation no-link">26 Stan. L. Rev. 1097</span> (1974); Recent Developments, Identification: Unnecessary Suggestiveness May Not Violate Due Process, <span class="citation no-link">73 Colum. L. Rev. 1168</span> (1973).</p>
<p>[8]  See, <i>e. g., </i><i>People</i> v. <i>Anderson,</i> <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/#172" aria-description="Citation for case: People v. Anderson">389 Mich. 155, 172-180, 192-220</a></span>, <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/#468" aria-description="Citation for case: People v. Anderson">205 N. W. 2d 461, 468-472, 479-494, 485</a></span> (1973); Levine &amp; Tapp, The Psychology of Criminal Identification: The Gap From <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> to <i><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span>,</i> <span class="citation no-link">121 U. Pa. L. Rev. 1079</span> (1973); O'Connor, "That's the Man": A Sobering Study of Eyewitness Identification and the Polygraph, <span class="citation no-link">49 St. John's L. Rev. 1</span> (1974); McGowan, <i>supra,</i> n. 4, at 238-239; Grano, <i>supra,</i> n. 7, at 723-724, 768-770; Recent Developments, <i>supra,</i> n. 7, at 1169 n. 11.
</p>
<p>Moreover, as the exhaustive opinion of the Michigan Supreme Court in <i>People</i> v. <i><span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/" aria-description="Citation for case: People v. Anderson">Anderson, supra</a></span></i><i>,</i> noted:</p>
<p>"For a number of obvious reasons, however, including the fact that there is no on-going systematic study of the problem, the reported cases of misidentification are in every likelihood only the top of the iceberg. The writer of this opinion, for example, was able to turn up three very recent unreported cases right here in Michigan in the course of a few hours' inquiry." <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/#179" aria-description="Citation for case: People v. Anderson">389 Mich., at 179-180</a></span>, <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/#472" aria-description="Citation for case: People v. Anderson">205 N. W. 2d, at 472</a></span>.</p>
<p>[9]  See also <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">429 U. S., at 499</a></span> n. 6; <i>United States</i> v. <i>Washington,</i> <span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#193" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 193-194</a></span> (1977) (BRENNAN, J., dissenting); Brennan, State Constitutions and the Protection of Individual Rights, <span class="citation no-link">90 Harv. L. Rev. 489</span> (1977). Cf. <i>People</i> v. <i><span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/" aria-description="Citation for case: People v. Anderson">Anderson, supra</a></span></i><i>; </i><i>Commonwealth</i> v. <i>Botelho,</i>  Mass. , <span class="citation" data-id="2221090"><a href="/opinion/2221090/commonwealth-v-botelho/" aria-description="Citation for case: Commonwealth v. Botelho">343 N. E. 2d 876</a></span> (1976).</p>
<p>[10]  See, <i>e. g.,</i> <span class="citation" data-id="8988513"><a href="/opinion/8996170/wallace-v-smith/#1" aria-description="Citation for case: Wallace v. Smith">Wall, <i>supra,</i> n. 1</a></span>, at 15-16; <i>People</i> v. <i>Anderson,</i> <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/#217" aria-description="Citation for case: People v. Anderson">389 Mich., at 217-220</a></span>, <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/#493" aria-description="Citation for case: People v. Anderson">205 N. W. 2d, at 493-494</a></span>; O'Connor, <i>supra,</i> n. 8, at 4-6.</p>
<p>[11]  See, <i>e. g.,</i> Levine &amp; Tapp, <i>supra,</i> n. 8, at 1100-1101; Note, Pretrial Identification ProceduresWade to Gilbert to Stovall: Lower Courts Bobble the Ball, <span class="citation no-link">55 Minn. L. Rev. 779</span>, 789 (1971); <i>People</i> v. <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/#214" aria-description="Citation for case: People v. Anderson"><i>Anderson, supra,</i> at 214-215</a></span>, <span class=

[...TRUNCATED 5469 of 125469 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/Manuel v. City of Joliet.md  (`case`, 5 assertions)

### content_page

```
---
title: Manuel v. City of Joliet
type: case
citation: "580 U.S. 357 (2017)"
parallel_cite: "137 S. Ct. 911; 197 L. Ed. 2d 312; 26 Fla. L. Weekly Fed. S 476; 85 U.S.L.W. 4130"
neutral_cite: 2017 U.S. LEXIS 2021
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2017
date_decided: 2017-03-21
docket: No. 14-9496
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
  opinion_url: "https://www.courtlistener.com/opinion/4376986/manuel-v-city-of-joliet/"
  cluster_id: 4376986
  opinion_id: null
  identity_checked: true
lake:
  record_id: Manuel v. City of Joliet
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Malicious Prosecution under the Fourth Amendment]]"
    role: Anchor
related:
  - "[[Malicious Prosecution under the Fourth Amendment]]"
  - "[[Thompson v. Clark]]"
  - "[[Heck v. Humphrey]]"
tags:
  - case
  - fourth-amendment
  - pretrial-detention
  - malicious-prosecution
  - fabricated-evidence
  - section-1983
holding: "The Fourth Amendment governs a § 1983 claim for unlawful pretrial detention, including detention that continues after the start of legal process, where the legal process — here a judge's probable-cause determination resting on fabricated evidence — did not rest on genuine probable cause."
aliases:
  - Manuel v. City of Joliet
  - "Manuel v. City of Joliet (2017)"
---

# Manuel v. City of Joliet

*580 U.S. 357 (2017)* (No. 14-9496) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4376986 → majority opinion 9873459 (Kagan, J.; 580 U.S. 357, decided Mar. 21, 2017). Rule quote string-matched to the CL opinion text 2026-07-07; the CL text carries S. Ct. star-pagination (parallel 137 S. Ct. 911), so the pin is to 137 S. Ct. at 920 (page-label `*920` precedes the "Our holding" sentence) — the official U.S. Reports pagination is not present in the CL text. S9 promotes. -->

## Background
Elijah Manuel was arrested during a traffic stop in Joliet, Illinois. Officers claimed a pill in his possession tested positive for ecstasy; in fact both the field test and a later laboratory test were negative. Relying on the officers' fabricated report, a county-court judge found probable cause and ordered Manuel detained. He remained jailed for roughly 48 days before the charge was dismissed. Manuel sued under § 1983, alleging his pretrial detention violated the Fourth Amendment. The Seventh Circuit held that once legal process began, a claim challenging detention sounded only in the Due Process Clause, not the Fourth Amendment, and dismissed.

## Issue
Whether the Fourth Amendment governs a claim for unlawful pretrial detention that continues after the start of legal process.

## Rule
The Court held that the Fourth Amendment's protection against detention absent probable cause is not switched off when legal process begins: "Our holding — that the Fourth Amendment governs a claim for unlawful pretrial detention even beyond the start of legal process — does not exhaust the disputed legal issues in this case." — 137 S. Ct. at 920. ^pin-920

## Application
Pretrial detention is a "seizure," and the Fourth Amendment requires that a seizure rest on probable cause both before and after the onset of legal process. Where the legal process itself is corrupted — a judge's probable-cause finding is procured by fabricated evidence — it cannot cleanse the ensuing detention of its Fourth Amendment defect. Manuel could therefore pursue a Fourth Amendment claim for the detention that followed the judge's tainted probable-cause ruling. The Court [[Reading and Citing Cases#on-remand|remanded]], leaving to the Seventh Circuit the questions of the claim's precise contours and, in particular, when it accrues for limitations purposes.

## Conclusion
The judgment was **[[Reading and Citing Cases#vacated|vacated]]** and the case [[Reading and Citing Cases#on-remand|remanded]]. Kagan, J., delivered the opinion of the Court; Alito, J. (joined by Thomas, J.), and Thomas, J., dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Manuel* supplies the constitutional footing for what many courts call a "Fourth Amendment malicious-prosecution" claim: unlawful pretrial detention is a seizure governed by the Fourth Amendment, even after legal process begins. It expressly left open the claim's elements and accrual; the accrual point for the related fabricated-evidence claim was addressed in *[[McDonough v. Smith]]* (2019), and the favorable-termination element of a Fourth Amendment malicious-prosecution claim was settled in *[[Thompson v. Clark]]* (2022). Teach *Manuel* as the anchor and those cases as the build-out.

## Appears on
- [[Malicious Prosecution under the Fourth Amendment]] — *Anchor*

## Sources
- [*Manuel v. City of Joliet*, 580 U.S. 357 (2017)](https://www.courtlistener.com/opinion/4376986/manuel-v-city-of-joliet/) — pinpoint: 137 S. Ct. 911, 920 (Kagan, J., for the Court; the CL opinion text is paginated to the parallel S. Ct. reporter, with the page-label `*920` immediately preceding the "Our holding" sentence — the U.S. Reports star-pagination is not present in the CL text). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "dc4c0083d588b9ec", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "580 U.S. 357 (2017)", "court": "U.S. Supreme Court", "neutral_cite": "2017 U.S. LEXIS 2021", "official_citation_present": true, "parallel_cite": "137 S. Ct. 911; 197 L. Ed. 2d 312; 26 Fla. L. Weekly Fed. S 476; 85 U.S.L.W. 4130", "title": "Manuel v. City of Joliet", "year": "2017"}}
{"assertion_id": "57e20caa27d732ed", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Fourth Amendment governs a § 1983 claim for unlawful pretrial detention, including detention that continues after the start of legal process, where the legal process — here a judge's probable-cause determination resting on fabricated evidence — did not rest on genuine probable cause.", "title": "Manuel v. City of Joliet"}}
{"assertion_id": "bb3d7d4b30e6b612", "dimension": "support", "kind": "home_role", "locator": {"home": "Malicious Prosecution under the Fourth Amendment"}, "payload": {"home": "Malicious Prosecution under the Fourth Amendment", "role": "Anchor", "title": "Manuel v. City of Joliet"}}
{"assertion_id": "03ec6df9e687edd2", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Manuel v. City of Joliet"}}
{"assertion_id": "cd0654372e4963d9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Manuel v. City of Joliet", "varies_by_point": "false"}}
```

### lake record — Manuel v. City of Joliet

```json
{
  "schema_version": "s2.v1",
  "record_id": "Manuel v. City of Joliet",
  "status": "under_review",
  "identity": {
    "case_name": "Manuel v. City of Joliet",
    "case_name_short": "Manuel",
    "case_name_full": "Elijah MANUEL, Petitioner v. CITY OF JOLIET, ILLINOIS, Et Al.",
    "input_case_name": "Manuel v. City of Joliet",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2017-03-21",
    "year": 2017,
    "docket": "No. 14-9496",
    "cluster_id": 4376986,
    "lead_opinion_id": 9873459,
    "sibling_ids": [],
    "absolute_url": "/opinion/4376986/manuel-v-city-of-joliet/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "580 U.S. 357",
      "volume": "580",
      "reporter": "U.S.",
      "page": "357",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "137 S. Ct. 911",
        "volume": "137",
        "reporter": "S. Ct.",
        "page": "911",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "197 L. Ed. 2d 312",
        "volume": "197",
        "reporter": "L. Ed. 2d",
        "page": "312",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 476",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "476",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 U.S.L.W. 4130",
        "volume": "85",
        "reporter": "U.S.L.W.",
        "page": "4130",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2017 U.S. LEXIS 2021",
        "volume": "2017",
        "reporter": "U.S. LEXIS",
        "page": "2021",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "580 U.S. 357",
        "volume": "580",
        "reporter": "U.S.",
        "page": "357",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 S. Ct. 911",
        "volume": "137",
        "reporter": "S. Ct.",
        "page": "911",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "197 L. Ed. 2d 312",
        "volume": "197",
        "reporter": "L. Ed. 2d",
        "page": "312",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 U.S. LEXIS 2021",
        "volume": "2017",
        "reporter": "U.S. LEXIS",
        "page": "2021",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 476",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "476",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 U.S.L.W. 4130",
        "volume": "85",
        "reporter": "U.S.L.W.",
        "page": "4130",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "580 U.S. 357",
    "official_selection": {
      "court_class": "scotus",
      "selected": "580 U.S. 357",
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
    "date_created": "2026-07-06T13:14:47Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:14:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:14:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:14:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:14:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "manuel-v-city-of-joliet--4376986",
      "to_record_id": "Manuel v. City of Joliet",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Manuel v. City of Joliet

```
<opinion type="majority">
<author id="p-10">Justice KAGAN delivered the opinion of the Court.</author>
<p id="p-11">Petitioner Elijah Manuel was held in jail for some seven weeks after a judge relied on allegedly fabricated evidence to find probable cause that he had committed a crime. The primary question in this case is whether Manuel may bring a claim based on the Fourth Amendment to contest the legality of his pretrial confinement. Our answer follows from settled precedent. The Fourth Amendment, this Court has recognized, establishes "the standards and procedures" governing pretrial detention. See, <em>e.g.,</em> <em>Gerstein v. Pugh,</em> <extracted-citation case-ids="11642843" index="0" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U.S. 103</a></span></extracted-citation>, 111, <extracted-citation case-ids="11642843" index="1" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation>, <extracted-citation case-ids="11642843" index="2" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">43 L.Ed.2d 54</a></span></extracted-citation> (1975). And those constitutional protections apply even after the start of "legal process" in a criminal case-here, that is, after the judge's determination of probable cause. See <em>Albright v. Oliver,</em> <extracted-citation case-ids="231967" index="3" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">510 U.S. 266</a></span></extracted-citation>, 274, <extracted-citation case-ids="231967" index="4" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation>, <extracted-citation case-ids="231967" index="5" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">127 L.Ed.2d 114</a></span></extracted-citation> (1994) (plurality opinion); <em><extracted-citation case-ids="231967" index="6" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">id.,</a></span></extracted-citation></em><extracted-citation case-ids="231967" index="6" url="https://cite.case.law/us/510/266/#p274"> at 290</extracted-citation>, <extracted-citation case-ids="231967" index="7" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation> (Souter, J., concurring in judgment). Accordingly, we hold today that Manuel may challenge his pretrial detention on the ground that it violated the Fourth Amendment (while we <a class="page-label" data-citation-index="1" data-label="915" href="#p915" id="p915">*915</a>leave all other issues, including one about that claim's timeliness, to the court below).</p>
<p id="p-12">I</p>
<p id="p-13">Shortly after midnight on March 18, 2011, Manuel was riding through Joliet, Illinois, in the passenger seat of a Dodge Charger, with his brother at the wheel. A pair of Joliet police officers pulled the car over when the driver failed to signal a turn. See App. 90. According to the complaint in this case, one of the officers dragged Manuel from the car, called him a racial slur, and kicked and punched him as he lay on the ground. See <em>id.,</em> at 31-32, 63.<footnotemark>1</footnotemark> The policeman then searched Manuel and found a vitamin bottle containing pills. See <em>id.,</em> at 64. Suspecting that the pills were actually illegal drugs, the officers conducted a field test of the bottle's contents. The test came back negative for any controlled substance, leaving the officers with no evidence that Manuel had committed a crime. See <em>id.,</em> at 69. Still, the officers arrested Manuel and took him to the Joliet police station. See <em>id.,</em> at 70.</p>
<p id="p-14">There, an evidence technician tested the pills once again, and got the same (negative) result. See <em>ibid.</em> But the technician lied in his report, claiming that one of the pills was "found to be ... positive for the probable presence of ecstasy." <em>Id.,</em> at 92. Similarly, one of the arresting officers wrote in his report that "[f]rom [his] training and experience, [he] knew the pills to be ecstasy." <em>Id.,</em> at 91. On the basis of those statements, another officer swore out a criminal complaint against Manuel, charging him with unlawful possession of a controlled substance. See <em>id.,</em> at 52-53.</p>
<p id="p-15">Manuel was brought before a county court judge later that day for a determination of whether there was probable cause for the charge, as necessary for further detention. See <em>Gerstein,</em> <extracted-citation case-ids="11642843" index="8" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U.S., at 114</a></span></extracted-citation>, <extracted-citation case-ids="11642843" index="9" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation> (requiring a judicial finding of probable cause following a warrantless arrest to impose any significant pretrial restraint on liberty); Ill. Comp. Stat., ch. 725, § 5/109-1 (West 2010) (implementing that constitutional rule). The judge relied exclusively on the criminal complaint-which in turn relied exclusively on the police department's fabrications-to support a finding of probable cause. Based on that determination, he sent Manuel to the county jail to await trial. In the somewhat obscure legal lingo of this case, Manuel's subsequent detention was thus pursuant to "legal process"-because it followed from, and was authorized by, the judge's probable-cause determination.<footnotemark>2</footnotemark></p>
<p id="p-16">While Manuel sat in jail, the Illinois police laboratory reexamined the seized pills, and on April 1, it issued a report concluding (just as the prior two tests had) that they contained no controlled substances. See App. 51. But for unknown reasons, the prosecution-and, critically for this case, Manuel's detention-continued for more than another month. Only on May 4 did an Assistant State's Attorney seek dismissal of the drug charge. See <em>id.,</em> at 48, 101. The County Court immediately granted the request, and Manuel was <a class="page-label" data-citation-index="1" data-label="916" href="#p916" id="p916">*916</a>released the next day. In all, he had spent 48 days in pretrial detention.</p>
<p id="p-17">On April 22, 2013, Manuel brought this lawsuit under <extracted-citation index="10" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation> against the City of Joliet and several of its police officers (collectively, the City). Section 1983 creates a "species of tort liability," <em>Imbler v. Pachtman,</em> <extracted-citation case-ids="12026708" index="11" url="https://cite.case.law/us/424/409/#p417"><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">424 U.S. 409</a></span></extracted-citation>, 417, <extracted-citation case-ids="12026708" index="12" url="https://cite.case.law/us/424/409/#p417"><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">96 S.Ct. 984</a></span></extracted-citation>, <extracted-citation case-ids="12026708" index="13" url="https://cite.case.law/us/424/409/#p417"><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">47 L.Ed.2d 128</a></span></extracted-citation> (1976), for "the deprivation of any rights, privileges, or immunities secured by the Constitution," § 1983. Manuel's complaint alleged that the City violated his Fourth Amendment rights in two ways-first by arresting him at the roadside without any reason, and next by "detaining him in police custody" for almost seven weeks based entirely on made-up evidence. See App. 79-80.<footnotemark>3</footnotemark></p>
<p id="p-18">The District Court dismissed Manuel's suit. See <extracted-citation index="14" url="https://cite.case.law/citations/?q=2014%20WL%20551626"><span class="citation no-link">2014 WL 551626</span></extracted-citation> (N.D.Ill., Feb. 12, 2014). The court first held that the applicable two-year statute of limitations barred Manuel's claim for unlawful arrest, because more than two years had elapsed between the date of his arrest (March 18, 2011) and the filing of his complaint (April 22, 2013). But the court relied on another basis in rejecting Manuel's challenge to his subsequent detention (which stretched from March 18 to May 5, 2011). Binding Circuit precedent, the District Court explained, made clear that pretrial detention following the start of legal process could not give rise to a Fourth Amendment claim. See <em><extracted-citation index="15" url="https://cite.case.law/citations/?q=2014%20WL%20551626"><span class="citation no-link">id.,</span></extracted-citation></em> at *1 (citing, <em>e.g.,</em> <em>Newsome v. McCabe,</em> <extracted-citation case-ids="11088221" index="16" url="https://cite.case.law/f3d/256/747/#p750"><span class="citation" data-id="773982"><a href="/opinion/773982/james-newsome-v-john-mccabe-and-raymond-mcnally/" aria-description="Citation for case: James Newsome v. John McCabe and Raymond McNally">256 F.3d 747</a></span></extracted-citation>, 750 (C.A.7 2001) ). According to that line of decisions, a § 1983 plaintiff challenging such detention must allege a breach of the Due Process Clause-and must show, to recover on that theory, that state law fails to provide an adequate remedy. See <extracted-citation index="17" url="https://cite.case.law/citations/?q=2014%20WL%20551626"><span class="citation no-link">2014 WL 551626</span></extracted-citation>, at *1-*2. Because Manuel's complaint rested solely on the Fourth Amendment-and because, in any event, Illinois's remedies were robust enough to preclude the due process avenue-the District Court found that Manuel had no way to proceed. See <em>ibid</em> .</p>
<p id="p-19">The Court of Appeals for the Seventh Circuit affirmed the dismissal of Manuel's claim for unlawful detention (the only part of the District Court's decision Manuel appealed). See <extracted-citation index="18" url="https://cite.case.law/citations/?q=590%20Fed.%20Appx.%20641"><span class="citation" data-id="2774281"><a href="/opinion/2774281/elijah-manuel-v-city-of-joliet/" aria-description="Citation for case: Elijah Manuel v. City of Joliet">590 Fed.Appx. 641</a></span></extracted-citation> (2015). Invoking its prior caselaw, the Court of Appeals reiterated that such claims could not be brought under the Fourth Amendment. Once a person is detained pursuant to legal process, the court stated, "the Fourth Amendment falls out of the picture and the detainee's claim that the detention is improper becomes [one of] due process." <em><extracted-citation index="19" url="https://cite.case.law/citations/?q=590%20Fed.%20Appx.%20641"><span class="citation" data-id="2774281"><a href="/opinion/2774281/elijah-manuel-v-city-of-joliet/" aria-description="Citation for case: Elijah Manuel v. City of Joliet">Id.,</a></span></extracted-citation></em><extracted-citation index="19" url="https://cite.case.law/citations/?q=590%20Fed.%20Appx.%20641"> at 643-644</extracted-citation> (quoting <em>Llovet v. Chicago,</em> <extracted-citation case-ids="4151176" index="20" url="https://cite.case.law/f3d/761/759/#p763"><span class="citation" data-id="8413043"><a href="/opinion/8441868/llovet-v-city-of-chicago/" aria-description="Citation for case: Llovet v. City of Chicago">761 F.3d 759</a></span></extracted-citation>, 763 (C.A.7 2014) ). And again: "When, after the arrest[,] a person is not let go when he should be, the Fourth Amendment gives way to the due process clause as a basis for challenging his detention." <extracted-citation index="21" url="https://cite.case.law/citations/?q=590%20Fed.%20Appx.%20641"><span class="citation" data-id="2774281"><a href="/opinion/2774281/elijah-manuel-v-city-of-joliet/" aria-description="Citation for case: Elijah Manuel v. City of Joliet">590 Fed.Appx., at 643</a></span></extracted-citation> (quoting <em>Llovet,</em> <extracted-citation case-ids="4151176" index="22" url="https://cite.case.law/f3d/761/759/#p763">761 F.3d, at </extracted-citation>764 ). So the Seventh Circuit held that Manuel's complaint, in alleging only a Fourth Amendment violation, rested on the wrong part of the Constitution: A person detained following the onset of legal process could at most (although, the court agreed, <em>not</em> in Illinois) challenge his pretrial confinement via the Due Process Clause. See <extracted-citation index="23" url="https://cite.case.law/citations/?q=590%20Fed.%20Appx.%20641"><span class="citation" data-id="2774281"><a href="/opinion/2774281/elijah-manuel-v-city-of-joliet/" aria-description="Citation for case: Elijah Manuel v. City of Joliet">590 Fed.Appx., at 643</a></span>-644</extracted-citation>.</p>
<p id="p-20"><a class="page-label" data-citation-index="1" data-label="917" href="#p917" id="p917">*917</a>The Seventh Circuit recognized that its position makes it an outlier among the Courts of Appeals, with ten others taking the opposite view. See <em><extracted-citation index="24" url="https://cite.case.law/citations/?q=590%20Fed.%20Appx.%20641"><span class="citation" data-id="2774281"><a href="/opinion/2774281/elijah-manuel-v-city-of-joliet/" aria-description="Citation for case: Elijah Manuel v. City of Joliet">id.,</a></span></extracted-citation></em> at 643 ; <em>Hernandez-Cuevas v. Taylor,</em> <extracted-citation case-ids="4065880" index="25" url="https://cite.case.law/f3d/723/91/#p99"><span class="citation" data-id="1034188"><a href="/opinion/1034188/hernandez-cuevas-v-taylor/" aria-description="Citation for case: Hernandez-Cuevas v. Taylor">723 F.3d 91</a></span></extracted-citation>, 99 (C.A.1 2013) ("[T]here is now broad consensus among the circuits that the Fourth Amendment right to be free from seizure but upon probable cause extends through the pretrial period").<footnotemark>4</footnotemark> Still, the court decided, Manuel had failed to offer a sufficient reason for overturning settled Circuit precedent; his argument, albeit "strong," was "better left for the Supreme Court." <extracted-citation index="26" url="https://cite.case.law/citations/?q=590%20Fed.%20Appx.%20641"><span class="citation" data-id="2774281"><a href="/opinion/2774281/elijah-manuel-v-city-of-joliet/" aria-description="Citation for case: Elijah Manuel v. City of Joliet">590 Fed.Appx., at 643</a></span></extracted-citation>.</p>
<p id="p-21">On cue, we granted certiorari. 577 U.S. ----, <extracted-citation case-ids="12602162,12602163,12602164,12602165,12602166,12602167" index="27" url="https://cite.case.law/s-ct/136/890/"><span class="citation multiple-matches"><a href="/c/S.Ct./136/890/">136 S.Ct. 890</a></span></extracted-citation>, <extracted-citation case-ids="12602162,12602163,12602164,12602165,12602166,12602167" index="28" url="https://cite.case.law/s-ct/136/890/"><span class="citation multiple-matches"><a href="/c/L.Ed.2d/193/783/">193 L.Ed.2d 783</a></span></extracted-citation> (2016).</p>
<p id="p-22">II</p>
<p id="p-23">The Fourth Amendment protects "[t]he right of the people to be secure in their persons ... against unreasonable ... seizures." Manuel's complaint seeks just that protection. Government officials, it recounts, detained-which is to say, "seiz[ed]"-Manuel for 48 days following his arrest. See App. 79-80; <em>Brendlin v. California,</em> <extracted-citation case-ids="3573063" index="29" url="https://cite.case.law/us/551/249/#p254"><span class="citation" data-id="145712"><a href="/opinion/145712/brendlin-v-california/" aria-description="Citation for case: Brendlin v. California">551 U.S. 249</a></span></extracted-citation>, 254, <extracted-citation case-ids="3573063" index="30" url="https://cite.case.law/us/551/249/#p254"><span class="citation" data-id="145712"><a href="/opinion/145712/brendlin-v-california/" aria-description="Citation for case: Brendlin v. California">127 S.Ct. 2400</a></span></extracted-citation>, <extracted-citation case-ids="3573063" index="31" url="https://cite.case.law/us/551/249/#p254"><span class="citation" data-id="145712"><a href="/opinion/145712/brendlin-v-california/" aria-description="Citation for case: Brendlin v. California">168 L.Ed.2d 132</a></span></extracted-citation> (2007) ("A person is seized" whenever officials "restrain[ ] his freedom of movement" such that he is "not free to leave"). And that detention was "unreasonable," the complaint continues, because it was based solely on false evidence, rather than supported by probable cause. See App. 79-80; <em>Bailey v. United States,</em> <extracted-citation case-ids="12407374" index="32" url="https://cite.case.law/us/568/186/#p192"><span class="citation" data-id="9502775"><a href="/opinion/820749/bailey-v-united-states/" aria-description="Citation for case: Bailey v. United States">568 U.S. 186</a></span></extracted-citation>, 192, <extracted-citation case-ids="12407374" index="33" url="https://cite.case.law/us/568/186/#p192"><span class="citation" data-id="9502775"><a href="/opinion/820749/bailey-v-united-states/" aria-description="Citation for case: Bailey v. United States">133 S.Ct. 1031</a></span></extracted-citation>, <extracted-citation case-ids="12407374" index="34" url="https://cite.case.law/us/568/186/#p192"><span class="citation" data-id="9502775"><a href="/opinion/820749/bailey-v-united-states/" aria-description="Citation for case: Bailey v. United States">185 L.Ed.2d 19</a></span></extracted-citation> (2013) ( "[T]he general rule [is] that Fourth Amendment seizures are 'reasonable' only if based on probable cause to believe that the individual has committed a crime"). By their respective terms, then, Manuel's claim fits the Fourth Amendment, and the Fourth Amendment fits Manuel's claim, as hand in glove.</p>
<p id="p-24">This Court decided some four decades ago that a claim challenging pretrial detention fell within the scope of the Fourth Amendment. In <em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>,</em> two persons arrested without a warrant brought a § 1983 suit complaining that they had been held in custody for "a substantial period solely on the decision of a prosecutor." <extracted-citation case-ids="11642843" index="35" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U.S., at 106</a></span></extracted-citation>, <extracted-citation case-ids="11642843" index="36" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation>. The Court looked to the Fourth Amendment to analyze-and uphold-their claim that such a pretrial restraint on liberty is unlawful unless a judge (or grand jury) first makes a reliable finding of probable cause. See <em><extracted-citation case-ids="11642843" index="37" url="https://cite.case.law/us/420/103/#p111">id.,</extracted-citation></em><extracted-citation case-ids="11642843" index="37" url="https://cite.case.law/us/420/103/#p111"> at 114, 117, n. 19</extracted-citation>, <extracted-citation case-ids="11642843" index="38" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation>. The Fourth Amendment, we began, establishes the minimum constitutional "standards and procedures" not just for arrest but also for ensuing "detention." <em><extracted-citation case-ids="11642843" index="39" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11642843" index="39" url="https://cite.case.law/us/420/103/#p111"> at 111</extracted-citation>, <extracted-citation case-ids="11642843" index="40" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation>. In choosing that Amendment "as the rationale for decision," the Court responded to a concurring Justice's view that the Due Process Clause offered the better framework: The Fourth Amendment, the majority countered, was "tailored explicitly for the criminal justice system, and it[ ] always has been thought to define" the appropriate process "for seizures of person[s] ... in criminal cases, including the detention of suspects pending trial." <em><extracted-citation case-ids="11642843" index="41" url="https://cite.case.law/us/420/103/#p111">Id.,</extracted-citation></em><extracted-citation case-ids="11642843" index="41" url="https://cite.case.law/us/420/103/#p111"> at 125, n. 27</extracted-citation>, <extracted-citation case-ids="11642843" index="42" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation>. That Amendment, standing alone, guaranteed "a fair and reliable determination of probable cause as a condition for any significant <a class="page-label" data-citation-index="1" data-label="918" href="#p918" id="p918">*918</a>pretrial restraint." <em><extracted-citation case-ids="11642843" index="43" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11642843" index="43" url="https://cite.case.law/us/420/103/#p111"> at 125</extracted-citation>, <extracted-citation case-ids="11642843" index="44" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation>. Accordingly, those detained prior to trial without such a finding could appeal to "the Fourth Amendment's protection against unfounded invasions of liberty." <em><extracted-citation case-ids="11642843" index="45" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11642843" index="45" url="https://cite.case.law/us/420/103/#p111"> at 112</extracted-citation>, <extracted-citation case-ids="11642843" index="46" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation> ; see <em><extracted-citation case-ids="11642843" index="47" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">id.,</a></span></extracted-citation></em><extracted-citation case-ids="11642843" index="47" url="https://cite.case.law/us/420/103/#p111"> at 114</extracted-citation>, <extracted-citation case-ids="11642843" index="48" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation>.<footnotemark>5</footnotemark></p>
<p id="p-25">And so too, a later decision indicates, those objecting to a pretrial deprivation of liberty may invoke the Fourth Amendment when (as here) that deprivation occurs after legal process commences. The § 1983 plaintiff in <em><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">Albright</a></span></em> complained of various pretrial restraints imposed after a court found probable cause to issue an arrest warrant, and then bind him over for trial, based on a policeman's unfounded charges. See <extracted-citation case-ids="231967" index="49" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">510 U.S., at 268</a></span>-269</extracted-citation>, <extracted-citation case-ids="231967" index="50" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation> (plurality opinion). For uncertain reasons, Albright ignored the Fourth Amendment in drafting his complaint; instead, he alleged that the defendant officer had infringed his substantive due process rights. This Court rejected that claim, with five Justices in two opinions remitting Albright to the Fourth Amendment. See <em><extracted-citation case-ids="231967" index="51" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">id.,</a></span></extracted-citation></em><extracted-citation case-ids="231967" index="51" url="https://cite.case.law/us/510/266/#p274"> at 271</extracted-citation>, <extracted-citation case-ids="231967" index="52" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation> (plurality opinion) ("We hold that it is the Fourth Amendment ... under which [his] claim must be judged"); <em><extracted-citation case-ids="231967" index="53" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">id.,</a></span></extracted-citation></em><extracted-citation case-ids="231967" index="53" url="https://cite.case.law/us/510/266/#p274"> at 290</extracted-citation>, <extracted-citation case-ids="231967" index="54" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation> (Souter, J., concurring in judgment) ("[I]njuries like those [he] alleges are cognizable in § 1983 claims founded upon ... the Fourth Amendment"). "The Framers," the plurality wrote, "considered the matter of pretrial deprivations of liberty and drafted the Fourth Amendment to address it." <em><extracted-citation case-ids="231967" index="55" url="https://cite.case.law/us/510/266/#p274">Id.,</extracted-citation></em><extracted-citation case-ids="231967" index="55" url="https://cite.case.law/us/510/266/#p274"> at 274</extracted-citation>, <extracted-citation case-ids="231967" index="56" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation>. That the deprivations at issue were pursuant to legal process made no difference, given that they were (allegedly) unsupported by probable cause; indeed, neither of the two opinions so much as mentioned that procedural circumstance. Relying on <em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>,</em> the plurality stated that the Fourth Amendment remained the "relevan[t]" constitutional provision to assess the "deprivations of liberty"-most notably, pretrial detention-"that go hand in hand with criminal prosecutions." <extracted-citation case-ids="231967" index="57" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">510 U.S., at 274</a></span></extracted-citation>, <extracted-citation case-ids="231967" index="58" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation> ; see <em><extracted-citation case-ids="231967" index="59" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">id.,</a></span></extracted-citation></em><extracted-citation case-ids="231967" index="59" url="https://cite.case.law/us/510/266/#p274"> at 290</extracted-citation>, <extracted-citation case-ids="231967" index="60" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation> (Souter, J., concurring in judgment) ("[R]ules of recovery for such harms have naturally coalesced under the Fourth Amendment").</p>
<p id="p-26">As reflected in <em><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">Albright</a></span></em> 's tracking of <em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></em> 's analysis, pretrial detention can violate the Fourth Amendment not only when it precedes, but also when it follows, the start of legal process in a criminal case. The Fourth Amendment prohibits government officials from detaining a person in the absence of probable cause. See <em>supra,</em> at 917. That can happen when the police hold someone without any reason before the formal onset of a criminal proceeding. But it also can occur when legal process itself goes wrong-when, for example, a judge's probable-cause determination is predicated solely on a police officer's false statements. Then, too, a person is confined without constitutionally adequate justification. Legal process <a class="page-label" data-citation-index="1" data-label="919" href="#p919" id="p919">*919</a>has gone forward, but it has done nothing to satisfy the Fourth Amendment's probable-cause requirement. And for that reason, it cannot extinguish the detainee's Fourth Amendment claim-or somehow, as the Seventh Circuit has held, convert that claim into one founded on the Due Process Clause. See <extracted-citation index="61" url="https://cite.case.law/citations/?q=590%20Fed.%20Appx.%20641"><span class="citation" data-id="2774281"><a href="/opinion/2774281/elijah-manuel-v-city-of-joliet/" aria-description="Citation for case: Elijah Manuel v. City of Joliet">590 Fed.Appx., at 643</a></span>-644</extracted-citation>. If the complaint is that a form of legal process resulted in pretrial detention unsupported by probable cause, then the right allegedly infringed lies in the Fourth Amendment.<footnotemark>6</footnotemark></p>
<p id="p-27">For that reason, and contrary to the Seventh Circuit's view, Manuel stated a Fourth Amendment claim when he sought relief not merely for his (pre-legal-process) arrest, but also for his (post-legal-process) pretrial detention.<footnotemark>7</footnotemark> Consider again the facts alleged in this case. Police officers initially arrested Manuel without probable cause, based solely on his possession of pills that had field tested negative for an illegal substance. So (putting timeliness issues aside) Manuel could bring a claim for wrongful arrest under the Fourth Amendment. And the same is true (again, disregarding timeliness) as to a claim for wrongful detention-because Manuel's subsequent weeks in custody were <em>also</em> unsupported by probable cause, and so <em>also</em> constitutionally unreasonable. No evidence of Manuel's criminality had come to light in between the roadside arrest and the County Court proceeding initiating legal process; to the contrary, yet another test of Manuel's pills had come back negative in that period. All that the judge had before him were police fabrications about the pills' content. The judge's order holding Manuel for trial therefore lacked any proper basis. And that means Manuel's ensuing pretrial detention, no less than his original arrest, violated his Fourth Amendment rights. Or put just a bit differently: Legal process did not expunge Manuel's Fourth Amendment claim because the process he received failed to establish what that Amendment makes essential for pretrial <a class="page-label" data-citation-index="1" data-label="920" href="#p920" id="p920">*920</a>detention-probable cause to believe he committed a crime.<footnotemark>8</footnotemark></p>
<p id="p-28">III</p>
<p id="p-29">Our holding-that the Fourth Amendment governs a claim for unlawful pretrial detention even beyond the start of legal process-does not exhaust the disputed legal issues in this case. It addresses only the threshold inquiry in a § 1983 suit, which requires courts to "identify the specific constitutional right" at issue. <em>Albright,</em> <extracted-citation case-ids="231967" index="62" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">510 U.S., at 271</a></span></extracted-citation>, <extracted-citation case-ids="231967" index="63" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation>. After pinpointing that right, courts still must determine the elements of, and rules associated with, an action seeking damages for its violation. See, <em>e.g.,</em> <em>Carey v. Piphus,</em> <extracted-citation case-ids="2517" index="64" url="https://cite.case.law/us/435/247/#p257"><span class="citation" data-id="109815"><a href="/opinion/109815/carey-v-piphus/" aria-description="Citation for case: Carey v. Piphus">435 U.S. 247</a></span></extracted-citation>, 257-258, <extracted-citation case-ids="2517" index="65" url="https://cite.case.law/us/435/247/#p257"><span class="citation" data-id="109815"><a href="/opinion/109815/carey-v-piphus/" aria-description="Citation for case: Carey v. Piphus">98 S.Ct. 1042</a></span></extracted-citation>, <extracted-citation case-ids="2517" index="66" url="https://cite.case.law/us/435/247/#p257"><span class="citation" data-id="109815"><a href="/opinion/109815/carey-v-piphus/" aria-description="Citation for case: Carey v. Piphus">55 L.Ed.2d 252</a></span></extracted-citation> (1978). Here, the parties particularly disagree over the accrual date of Manuel's Fourth Amendment claim-that is, the date on which the applicable two-year statute of limitations began to run. The timeliness of Manuel's suit hinges on the choice between their proposed dates. But with the following brief comments, we remand that issue to the court below.</p>
<p id="p-30">In defining the contours and prerequisites of a § 1983 claim, including its rule of accrual, courts are to look first to the common law of torts. See <em><extracted-citation case-ids="2517" index="67" url="https://cite.case.law/us/435/247/#p257">ibid.</extracted-citation></em> (explaining that tort principles "provide the appropriate starting point" in specifying the conditions for recovery under § 1983 ); <em>Wallace v. Kato,</em> <extracted-citation case-ids="3553763" index="68" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S. 384</a></span></extracted-citation>, 388-390, <extracted-citation case-ids="3553763" index="69" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>, <extracted-citation case-ids="3553763" index="70" url="https://cite.case.law/us/549/384/#p388"><span class="citation no-link">166 L.Ed.2d 973</span></extracted-citation> (2007) (same for accrual dates in particular). Sometimes, that review of common law will lead a court to adopt wholesale the rules that would apply in a suit involving the most analogous tort. See <em><extracted-citation case-ids="3553763" index="71" url="https://cite.case.law/us/549/384/#p388"><span class="citation no-link">id.,</span></extracted-citation></em><extracted-citation case-ids="3553763" index="71" url="https://cite.case.law/us/549/384/#p388"> at 388-390</extracted-citation>, <extracted-citation case-ids="3553763" index="72" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation> ;</p>
<p id="p-31"><a class="page-label" data-citation-index="1" data-label="921" href="#p921" id="p921">*921</a><em>Heck v. Humphrey,</em> <extracted-citation case-ids="39868" index="73" url="https://cite.case.law/us/512/477/#p483"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U.S. 477</a></span></extracted-citation>, 483-487, <extracted-citation case-ids="39868" index="74" url="https://cite.case.law/us/512/477/#p483"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>, <extracted-citation case-ids="39868" index="75" url="https://cite.case.law/us/512/477/#p483"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">129 L.Ed.2d 383</a></span></extracted-citation> (1994). But not always. Common-law principles are meant to guide rather than to control the definition of § 1983 claims, serving "more as a source of inspired examples than of prefabricated components." <em>Hartman v. Moore,</em> <extracted-citation case-ids="3275855" index="76" url="https://cite.case.law/us/547/250/#p258"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. 250</a></span></extracted-citation>, 258, <extracted-citation case-ids="3275855" index="77" url="https://cite.case.law/us/547/250/#p258"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="78" url="https://cite.case.law/us/547/250/#p258"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">164 L.Ed.2d 441</a></span></extracted-citation> (2006) ; see <em>Rehberg v. Paulk,</em> <extracted-citation case-ids="12189183" index="79" url="https://cite.case.law/us/566/356/#p366"><span class="citation" data-id="626447"><a href="/opinion/626447/rehberg-v-paulk/" aria-description="Citation for case: Rehberg v. Paulk">566 U.S. 356</a></span></extracted-citation>, 366, <extracted-citation case-ids="12189183" index="80" url="https://cite.case.law/us/566/356/#p366"><span class="citation" data-id="626447"><a href="/opinion/626447/rehberg-v-paulk/" aria-description="Citation for case: Rehberg v. Paulk">132 S.Ct. 1497</a></span></extracted-citation>, <extracted-citation case-ids="12189183" index="81" url="https://cite.case.law/us/566/356/#p366"><span class="citation" data-id="626447"><a href="/opinion/626447/rehberg-v-paulk/" aria-description="Citation for case: Rehberg v. Paulk">182 L.Ed.2d 593</a></span></extracted-citation> (2012) (noting that " § 1983 is [not] simply a federalized amalgamation of pre-existing common-law claims"). In applying, selecting among, or adjusting common-law approaches, courts must closely attend to the values and purposes of the constitutional right at issue.</p>
<p id="p-32">With these precepts as backdrop, Manuel and the City offer competing views about what accrual rule should govern a § 1983 suit challenging post-legal-process pretrial detention. According to Manuel, that Fourth Amendment claim accrues only upon the dismissal of criminal charges-here, on May 4, 2011, less than two years before he brought his suit. See Reply Brief 2; Brief for United States as <em>Amicus Curiae</em> 24-25, n. 16 (taking the same position). Relying on this Court's caselaw, Manuel analogizes his claim to the common-law tort of malicious prosecution. See Reply Brief 9; <em>Wallace,</em> <extracted-citation case-ids="3553763" index="82" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S., at 389</a></span>-390</extracted-citation>, <extracted-citation case-ids="3553763" index="83" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>. An element of that tort is the "termination of the ... proceeding in favor of the accused"; and accordingly, the statute of limitations does not start to run until that termination takes place. <em>Heck,</em> <extracted-citation case-ids="39868" index="84" url="https://cite.case.law/us/512/477/#p483"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/#484" aria-description="Citation for case: Heck v. Humphrey">512 U.S., at 484</a></span>, 489</extracted-citation>, <extracted-citation case-ids="39868" index="85" url="https://cite.case.law/us/512/477/#p483"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>. Manuel argues that following the same rule in suits like his will avoid "conflicting resolutions" in § 1983 litigation and criminal proceedings by "preclud[ing] the possibility of the claimant succeeding in the tort action after having been convicted in the underlying criminal prosecution." <em><extracted-citation case-ids="39868" index="86" url="https://cite.case.law/us/512/477/#p483">Id.,</extracted-citation></em><extracted-citation case-ids="39868" index="86" url="https://cite.case.law/us/512/477/#p483"> at 484, 486</extracted-citation>, <extracted-citation case-ids="39868" index="87" url="https://cite.case.law/us/512/477/#p483"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation> ; see Reply Brief 10-11; Brief for United States as <em>Amicus Curiae</em> 24-25, n. 16. In support of Manuel's position, all but two of the ten Courts of Appeals that have recognized a Fourth Amendment claim like his have incorporated a "favorable termination" element and so pegged the statute of limitations to the dismissal of the criminal case. See n. 4, <em>supra</em> .<footnotemark>9</footnotemark> That means in the great majority of Circuits, Manuel's claim would be timely.</p>
<p id="p-33">The City, however, contends that any such Fourth Amendment claim accrues (and the limitations period starts to run) on the date of the initiation of legal process-here, on March 18, 2011, <em>more</em> than two years before Manuel filed suit. See Brief for Respondents 33. According to the City, the most analogous tort to Manuel's constitutional claim is not malicious prosecution but false arrest, which accrues when legal process commences. See Tr. of Oral Arg. 47; <em>Wallace,</em> <extracted-citation case-ids="3553763" index="88" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S., at 389</a></span></extracted-citation>, <extracted-citation case-ids="3553763" index="89" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation> (noting accrual rule for false arrest suits). And even if malicious prosecution were the better comparison, the City continues, a court should decline to adopt that tort's favorable-termination element and associated accrual rule in adjudicating a § 1983 claim involving pretrial detention. That element, the City argues, "make[s] little sense" in this context because "the Fourth Amendment is concerned not with the outcome of a prosecution, but with the legality of searches and seizures." Brief for Respondents 16. And finally, the City contends that Manuel forfeited an alternative theory for treating his date of release as the date of accrual: to wit, that his pretrial detention "constitute[d] a continuing Fourth Amendment violation," each day of which triggered the statute of limitations anew.</p>
<p id="p-34"><a class="page-label" data-citation-index="1" data-label="922" href="#p922" id="p922">*922</a><em>Id.,</em> at 29, and n. 6; see Tr. of Oral Arg. 36; see also <em>Albright,</em> <extracted-citation case-ids="231967" index="90" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">510 U.S., at 280</a></span></extracted-citation>, <extracted-citation case-ids="231967" index="91" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation> (GINSBURG, J., concurring) (propounding a similar view). So Manuel, the City concludes, lost the opportunity to recover for his pretrial detention by waiting too long to file suit.</p>
<p id="p-35">We leave consideration of this dispute to the Court of Appeals. "[W]e are a court of review, not of first view." <em>Cutter v. Wilkinson,</em> <extracted-citation case-ids="5868782" index="92" url="https://cite.case.law/us/544/709/#p718"><span class="citation" data-id="9434809"><a href="/opinion/142900/cutter-v-wilkinson/" aria-description="Citation for case: Cutter v. Wilkinson">544 U.S. 709</a></span></extracted-citation>, 718, n. 7, <extracted-citation case-ids="5868782" index="93" url="https://cite.case.law/us/544/709/#p718"><span class="citation" data-id="9434809"><a href="/opinion/142900/cutter-v-wilkinson/" aria-description="Citation for case: Cutter v. Wilkinson">125 S.Ct. 2113</a></span></extracted-citation>, <extracted-citation case-ids="5868782" index="94" url="https://cite.case.law/us/544/709/#p718"><span class="citation" data-id="9434809"><a href="/opinion/142900/cutter-v-wilkinson/" aria-description="Citation for case: Cutter v. Wilkinson">161 L.Ed.2d 1020</a></span></extracted-citation> (2005). Because the Seventh Circuit wrongly held that Manuel lacked any Fourth Amendment claim once legal process began, the court never addressed the elements of, or rules applicable to, such a claim. And in particular, the court never confronted the accrual issue that the parties contest here.<footnotemark>10</footnotemark> On remand, the Court of Appeals should decide that question, unless it finds that the City has previously waived its timeliness argument. See Reply to Brief in Opposition 1-2 (addressing the possibility of waiver); Tr. of Oral Arg. 40-44 (same). And so too, the court may consider any other still-live issues relating to the contours of Manuel's Fourth Amendment claim for unlawful pretrial detention.</p>
<p id="p-36">For the reasons stated, we reverse the judgment of the Seventh Circuit and remand the case for further proceedings consistent with this opinion.</p>
<p id="p-37"><em>It is so ordered.</em></p>
<footnote label="1">
<p id="p-85">Because we here review an order dismissing Manuel's suit, we accept as true all the factual allegations in his complaint. See, <em>e.g.,</em> <em>Leatherman v. Tarrant County Narcotics Intelligence and Coordination Unit,</em> <extracted-citation case-ids="6224800" index="95" url="https://cite.case.law/us/507/163/#p164"><span class="citation" data-id="112825"><a href="/opinion/112825/leatherman-v-tarrant-county-narcotics-intelligence-and-coordination-unit/" aria-description="Citation for case: Leatherman v. Tarrant County Narcotics Intelligence and...">507 U.S. 163</a></span></extracted-citation>, 164, <extracted-citation case-ids="6224800" index="96" url="https://cite.case.law/us/507/163/#p164"><span class="citation" data-id="112825"><a href="/opinion/112825/leatherman-v-tarrant-county-narcotics-intelligence-and-coordination-unit/" aria-description="Citation for case: Leatherman v. Tarrant County Narcotics Intelligence and...">113 S.Ct. 1160</a></span></extracted-citation>, <extracted-citation case-ids="6224800" index="97" url="https://cite.case.law/us/507/163/#p164"><span class="citation" data-id="112825"><a href="/opinion/112825/leatherman-v-tarrant-county-narcotics-intelligence-and-coordination-unit/" aria-description="Citation for case: Leatherman v. Tarrant County Narcotics Intelligence and...">122 L.Ed.2d 517</a></span></extracted-citation> (1993).</p>
</footnote>
<footnote label="2">
<p id="p-86">Although not addressed in Manuel's complaint, the police department's alleged fabrications did not stop at this initial hearing on probable cause. About two weeks later, on March 30, a grand jury indicted Manuel based on similar false evidence: testimony from one of the arresting officers that "[t]he pills field tested positive" for ecstasy. App. 96 (grand jury minutes).</p>
</footnote>
<footnote label="3">
<p id="p-87">Manuel's allegation of unlawful detention concerns only the period after the onset of legal process-here meaning, again, after the County Court found probable cause that he had committed a crime. See <em>supra,</em> at 915 - 916. The police also held Manuel in custody for several hours between his warrantless arrest and his first appearance in court. But throughout this litigation, Manuel has treated that short period as part and parcel of the initial unlawful arrest. See, <em>e.g.,</em> Reply Brief 1.</p>
</footnote>
<footnote label="4">
<p id="p-88">See also <em>Singer v. Fulton County Sheriff,</em> <extracted-citation case-ids="7414152" index="98" url="https://cite.case.law/f3d/63/110/#p114"><span class="citation" data-id="6935799"><a href="/opinion/7033453/singer-v-fulton-county-sheriff/" aria-description="Citation for case: Singer v. Fulton County Sheriff">63 F.3d 110</a></span></extracted-citation>, 114-118 (C.A.2 1995) ; <em>McKenna v. Philadelphia,</em> <extracted-citation case-ids="4061656" index="99" url="https://cite.case.law/f3d/582/447/#p461"><span class="citation" data-id="1349366"><a href="/opinion/1349366/mckenna-v-city-of-philadelphia/" aria-description="Citation for case: McKenna v. City of Philadelphia">582 F.3d 447</a></span></extracted-citation>, 461 (C.A.3 2009) ; <em>Lambert v. Williams,</em> <extracted-citation case-ids="11239127" index="100" url="https://cite.case.law/f3d/223/257/#p260"><span class="citation" data-id="2967278"><a href="/opinion/2967278/lambert-v-williams/" aria-description="Citation for case: Lambert v. Williams">223 F.3d 257</a></span></extracted-citation>, 260-262 (C.A.4 2000) ; <em>Castellano v. Fragozo,</em> <extracted-citation case-ids="9298683" index="101" url="https://cite.case.law/f3d/352/939/#p953"><span class="citation" data-id="8408477"><a href="/opinion/8437970/castellano-v-fragozo/" aria-description="Citation for case: Castellano v. Fragozo">352 F.3d 939</a></span></extracted-citation>, 953-954, 959-960 (C.A.5 2003) (en banc); <em>Sykes v. Anderson,</em> <extracted-citation case-ids="3801091" index="102" url="https://cite.case.law/f3d/625/294/#p308"><span class="citation" data-id="178987"><a href="/opinion/178987/sykes-v-anderson/" aria-description="Citation for case: Sykes v. Anderson">625 F.3d 294</a></span></extracted-citation>, 308-309 (C.A.6 2010) ; <em>Galbraith v. County of Santa Clara,</em> <extracted-citation case-ids="11357676" index="103" url="https://cite.case.law/f3d/307/1119/#p1126"><span class="citation" data-id="7014886"><a href="/opinion/7108812/galbraith-v-county-of-santa-clara/" aria-description="Citation for case: Galbraith v. County of Santa Clara">307 F.3d 1119</a></span></extracted-citation>, 1126-1127 (C.A.9 2002) ; <em>Wilkins v. De</em> -<em>Reyes,</em> <extracted-citation case-ids="3582012" index="104" url="https://cite.case.law/f3d/528/790/#p797"><span class="citation" data-id="170833"><a href="/opinion/170833/wilkins-v-dereyes/" aria-description="Citation for case: Wilkins v. DeReyes">528 F.3d 790</a></span></extracted-citation>, 797-799 (C.A.10 2008) ; <em>Whiting v. Traylor,</em> <extracted-citation case-ids="571886" index="105" url="https://cite.case.law/f3d/85/581/#p584"><span class="citation" data-id="70957"><a href="/opinion/70957/whiting-v-traylor/" aria-description="Citation for case: Whiting v. Traylor">85 F.3d 581</a></span></extracted-citation>, 584-586 (C.A.11 1996) ; <em>Pitt v. District of Columbia,</em> <extracted-citation case-ids="3564507,3471212" index="106" url="https://cite.case.law/f3d/491/494/"><span class="citation" data-id="798179"><a href="/opinion/798179/christopher-g-pitt-sr-and-tela-hansom-pitt-v-district-of-columbia/" aria-description="Citation for case: Christopher G. Pitt, Sr. And Tela Hansom-Pitt v. District...">491 F.3d 494</a></span></extracted-citation>, 510-511 (C.A.D.C.2007).</p>
</footnote>
<footnote label="5">
<p id="p-89">The Court repeated the same idea in a follow-on decision to <em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></em>. In <em>County of Riverside v. McLaughlin,</em> <extracted-citation case-ids="6216695" index="107" url="https://cite.case.law/us/500/44/#p47"><span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/" aria-description="Citation for case: County of Riverside v. McLaughlin">500 U.S. 44</a></span></extracted-citation>, 47, <extracted-citation case-ids="6216695" index="108" url="https://cite.case.law/us/500/44/#p47"><span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/" aria-description="Citation for case: County of Riverside v. McLaughlin">111 S.Ct. 1661</a></span></extracted-citation>, <extracted-citation case-ids="6216695" index="109" url="https://cite.case.law/us/500/44/#p47"><span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/" aria-description="Citation for case: County of Riverside v. McLaughlin">114 L.Ed.2d 49</a></span></extracted-citation> (1991), we considered how quickly a jurisdiction must provide the probable-cause determination that <em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></em> demanded "as a prerequisite to an extended pretrial detention." In holding that the decision should occur within 48 hours of an arrest, the majority understood its "task [as] articulat[ing] more clearly the boundaries of what is permissible under the Fourth Amendment." <extracted-citation case-ids="6216695" index="110" url="https://cite.case.law/us/500/44/#p47"><span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/" aria-description="Citation for case: County of Riverside v. McLaughlin">500 U.S., at 56</a></span></extracted-citation>, <extracted-citation case-ids="6216695" index="111" url="https://cite.case.law/us/500/44/#p47"><span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/" aria-description="Citation for case: County of Riverside v. McLaughlin">111 S.Ct. 1661</a></span></extracted-citation>. In arguing for still greater speed, the principal dissent invoked the original meaning of "the Fourth Amendment's prohibition of 'unreasonable seizures,' insofar as it applies to seizure of the person." <em><extracted-citation case-ids="6216695" index="112" url="https://cite.case.law/us/500/44/#p47"><span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/" aria-description="Citation for case: County of Riverside v. McLaughlin">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="6216695" index="112" url="https://cite.case.law/us/500/44/#p47"> at 60</extracted-citation>, <extracted-citation case-ids="6216695" index="113" url="https://cite.case.law/us/500/44/#p47"><span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/" aria-description="Citation for case: County of Riverside v. McLaughlin">111 S.Ct. 1661</a></span></extracted-citation> (Scalia, J., dissenting). The difference between the two opinions was significant, but the commonality still more so: All Justices agreed that the Fourth Amendment provides the appropriate lens through which to view a claim involving pretrial detention.</p>
</footnote>
<footnote label="6">
<p id="p-90">The opposite view would suggest an untenable result: that a person arrested pursuant to a warrant could not bring a Fourth Amendment claim challenging the reasonableness of even his arrest, let alone any subsequent detention. An arrest warrant, after all, is a way of initiating legal process, in which a magistrate finds probable cause that a person committed a crime. See <em>Wallace v. Kato,</em> <extracted-citation case-ids="3553763" index="114" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S. 384</a></span></extracted-citation>, 389, <extracted-citation case-ids="3553763" index="115" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>, <extracted-citation case-ids="3553763" index="116" url="https://cite.case.law/us/549/384/#p388"><span class="citation no-link">166 L.Ed.2d 973</span></extracted-citation> (2007) (explaining that the seizure of a person was "without legal process" because police officers "did not have a warrant for his arrest"); W. Keeton, D. Dobbs, R. Keeton, &amp; D. Owen, Prosser and Keeton on Law of Torts § 119, pp. 871, 886 (5th ed. 1984) (similar). If legal process is the cut-off point for the Fourth Amendment, then someone arrested (as well as later held) under a warrant procured through false testimony would have to look to the Due Process Clause for relief. But that runs counter to our caselaw. See, <em>e.g.,</em> <em>Whiteley v. Warden, Wyo. State Penitentiary,</em> <extracted-citation case-ids="11714156" index="117" url="https://cite.case.law/us/401/560/#p568"><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U.S. 560</a></span></extracted-citation>, 568-569, <extracted-citation case-ids="11714156" index="118" url="https://cite.case.law/us/401/560/#p568"><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">91 S.Ct. 1031</a></span></extracted-citation>, <extracted-citation case-ids="11714156" index="119" url="https://cite.case.law/us/401/560/#p568"><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">28 L.Ed.2d 306</a></span></extracted-citation> (1971) (holding that an arrest violated the Fourth Amendment because a magistrate's warrant was not backed by probable cause). And if the Seventh Circuit would reply that arrest warrants are somehow different-that there is legal process and then again there is <em>legal process</em> -the next (and in our view unanswerable) question would be why.</p>
</footnote>
<footnote label="7">
<p id="p-91">Even the City no longer appears to contest that conclusion. On multiple occasions during oral argument in this Court, the City agreed that "a Fourth Amendment right ... survive[d] the initiation of process" at the hearing in which the county judge found probable cause and ordered detention. Tr. of Oral Arg. 31; see <em>id.,</em> at 33 (concurring with the statement that "once [an] individual is brought ... before a magistrate, and the magistrate using the same bad evidence says, stay here in jail ... until we get to trial, that that period is a violation of the Fourth Amendment"); <em>id.,</em> at 51 (stating that a detainee has "a Fourth Amendment claim" if "misstatements at [such a probable-cause hearing] led to ongoing pretrial seizure").</p>
</footnote>
<footnote label="8">
<p id="p-92">The dissent goes some way toward claiming that a different kind of pretrial legal process-a grand jury indictment or preliminary examination-does expunge such a Fourth Amendment claim. See <em>post,</em> at 927, n. 4 (opinion of ALITO, J.) (raising but "not decid[ing] that question"); <em>post,</em> at 927 - 928 (suggesting an answer nonetheless). The effect of that view would be to cut off Manuel's claim on the date of his grand jury indictment (March 30)-even though that indictment (like the County Court's probable-cause proceeding) was entirely based on false testimony and even though Manuel remained in detention for 36 days longer. See n. 2, <em>supra</em>. Or said otherwise-even though the legal process he received failed to establish the probable cause necessary for his continued confinement. We can see no principled reason to draw that line. Nothing in the nature of the legal proceeding establishing probable cause makes a difference for purposes of the Fourth Amendment: Whatever its precise form, if the proceeding is tainted-as here, by fabricated evidence-and the result is that probable cause is lacking, then the ensuing pretrial detention violates the confined person's Fourth Amendment rights, for all the reasons we have stated. By contrast (and contrary to the dissent's suggestion, see <em>post,</em> at 927, n. 3), once a trial has occurred, the Fourth Amendment drops out: A person challenging the sufficiency of the evidence to support both a conviction and any ensuing incarceration does so under the Due Process Clause of the Fourteenth Amendment. See <em>Jackson v. Virginia,</em> <extracted-citation case-ids="6182418" index="120" url="https://cite.case.law/us/443/307/#p318"><span class="citation" data-id="9427680"><a href="/opinion/110138/jackson-v-virginia/" aria-description="Citation for case: Jackson v. Virginia">443 U.S. 307</a></span></extracted-citation>, 318, <extracted-citation case-ids="6182418" index="121" url="https://cite.case.law/us/443/307/#p318"><span class="citation" data-id="9427680"><a href="/opinion/110138/jackson-v-virginia/" aria-description="Citation for case: Jackson v. Virginia">99 S.Ct. 2781</a></span></extracted-citation>, <extracted-citation case-ids="6182418" index="122" url="https://cite.case.law/us/443/307/#p318"><span class="citation" data-id="9427680"><a href="/opinion/110138/jackson-v-virginia/" aria-description="Citation for case: Jackson v. Virginia">61 L.Ed.2d 560</a></span></extracted-citation> (1979) (invalidating a conviction under the Due Process Clause when "the record evidence could [not] reasonably support a finding of guilt beyond a reasonable doubt"); <em>Thompson v. Louisville,</em> <extracted-citation case-ids="6162984" index="123" url="https://cite.case.law/us/362/199/#p204"><span class="citation" data-id="106017"><a href="/opinion/106017/thompson-v-city-of-louisville/" aria-description="Citation for case: Thompson v. City of Louisville">362 U.S. 199</a></span></extracted-citation>, 204, <extracted-citation case-ids="6162984" index="124" url="https://cite.case.law/us/362/199/#p204"><span class="citation" data-id="106017"><a href="/opinion/106017/thompson-v-city-of-louisville/" aria-description="Citation for case: Thompson v. City of Louisville">80 S.Ct. 624</a></span></extracted-citation>, <extracted-citation case-ids="6162984" index="125" url="https://cite.case.law/us/362/199/#p204"><span class="citation" data-id="106017"><a href="/opinion/106017/thompson-v-city-of-louisville/" aria-description="Citation for case: Thompson v. City of Louisville">4 L.Ed.2d 654</a></span></extracted-citation> (1960) (striking a conviction under the same provision when "the record [wa]s entirely lacking in evidence" of guilt-such that it could not even establish probable cause). <em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></em> and <em><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">Albright</a></span>,</em> as already suggested, both reflected and recognized that constitutional division of labor. See <em>supra,</em> at 917 - 918. In their words, the Framers "drafted the Fourth Amendment" to address "the matter of <em>pretrial</em> deprivations of liberty," <em>Albright,</em> <extracted-citation case-ids="231967" index="126" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">510 U.S., at 274</a></span></extracted-citation>, <extracted-citation case-ids="231967" index="127" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation> (emphasis added), and the Amendment thus provides "standards and procedures" for "the detention of suspects <em>pending trial,</em> " <em>Gerstein,</em> <extracted-citation case-ids="11642843" index="128" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#125" aria-description="Citation for case: Gerstein v. Pugh">420 U.S., at 125</a></span>, n. 27</extracted-citation>, <extracted-citation case-ids="11642843" index="129" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation> (emphasis added).</p>
</footnote>
<footnote label="9">
<p id="p-93">The two exceptions-the Ninth and D.C. Circuits-have not yet weighed in on whether a Fourth Amendment claim like Manuel's includes a "favorable termination" element.</p>
</footnote>
<footnote label="10">
<p id="p-94">The dissent would have us address these questions anyway, on the ground that "the conflict on the malicious prosecution question was the centerpiece of Manuel's argument in favor of certiorari." <em>Post,</em> at 923. But the decision below did not implicate a "conflict on the malicious prosecution question"-because the Seventh Circuit, in holding that detainees like Manuel could not bring a Fourth Amendment claim at all, never considered whether (and, if so, how) that claim should resemble the malicious prosecution tort. Nor did Manuel's petition for certiorari suggest otherwise. The principal part of his question presented-mirroring the one and only Circuit split involving the decision below-reads as follows: "[W]hether an individual's Fourth Amendment right to be free from unreasonable seizure continues beyond legal process." Pet. for Cert. i. That is exactly the issue we have resolved. The rest of Manuel's question did indeed express a view as to what would follow from an affirmative answer ("so as to allow a malicious prosecution claim"). <em><extracted-citation case-ids="11642843" index="130" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Ibid.</a></span></extracted-citation></em> (And as the dissent notes, the Seventh Circuit recounted that he made the same argument in that court. See <em>post,</em> at 923 -924, n. 1.) But as to that secondary issue, we think (for all the reasons just stated) that Manuel jumped the gun. See <em>supra,</em> at 920 - 922. And contra the dissent, his doing so provides no warrant for our doing so too.</p>
<p id="p-95">* * *</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Mapp v. Ohio.md  (`case`, 5 assertions)

### content_page

```
---
title: "Mapp v. Ohio"
type: case
citation: "367 U.S. 643 (1961)"
parallel_cite: "81 S. Ct. 1684; 6 L. Ed. 2d 1081"
neutral_cite: 1961 U.S. LEXIS 812
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1961
date_decided: 1961-10-09
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1961-06-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Mapp v. Ohio
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106285/mapp-v-ohio/"
  cluster_id: 106285
  opinion_id: 106285
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Anchor"
related: ["[[Weeks v. United States]]", "[[Wolf v. Colorado]]", "[[United States v. Leon]]", "[[Herring v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "incorporation", "fourteenth-amendment"]
holding: "The exclusionary rule applies to the States through the Fourteenth Amendment."
lake:
  record_id: Mapp v. Ohio
  status: verified
  projected_at: 2026-07-06
---

# Mapp v. Ohio

*367 U.S. 643 (1961)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Cleveland officers forced their way into Dollree Mapp's home without a valid warrant, searched it while looking for a bombing suspect and gambling materials, and found allegedly obscene materials, for which she was convicted. The Ohio courts admitted the unlawfully seized evidence, relying on *[[Wolf v. Colorado]]*, which had held the Fourth Amendment's exclusionary remedy was not binding on the States.

## Issue
Whether evidence obtained by a search and seizure that violates the Fourth Amendment is inadmissible in a state criminal prosecution.

## Rule
Yes. "We hold that all evidence obtained by searches and seizures in violation of the Constitution is, by that same authority, inadmissible in a state court." — 367 U.S. at 655. ^pin-655

Because the Fourth Amendment's right of privacy is enforceable against the States through the Due Process Clause of the Fourteenth Amendment, it is enforceable against them by the same sanction of exclusion used against the Federal Government.

## Application
The evidence used to convict Mapp was obtained in a warrantless, forcible entry and search of her home in violation of the Fourth Amendment. Under the rule announced here, that unlawfully seized evidence was inadmissible in the Ohio courts, so its admission could not stand. The Court overruled the contrary holding of *[[Wolf v. Colorado]]* to the extent it had left the States free to admit such evidence.

## Conclusion
The conviction, resting on unconstitutionally seized evidence, was reversed. The federal exclusionary rule of *[[Weeks v. United States|Weeks]]* applies to the States through the Fourteenth Amendment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Mapp* extended the [[Weeks v. United States]] exclusionary rule to the States and overruled the contrary portion of [[Wolf v. Colorado]]. The exclusionary rule remains good law, though later cases have narrowed its **scope** through the [[The Good-Faith Exception|good-faith exception]] ([[United States v. Leon]]) and a culpability requirement for deterrence ([[Herring v. United States]]) — refinements of the remedy, not abrogations of *Mapp*.

## Appears on
- [[The Exclusionary Rule]] — *Key — Anchor*

## Sources
- *Mapp v. Ohio*, 367 U.S. 643 (1961) — https://www.courtlistener.com/opinion/106285/mapp-v-ohio/ — pinpoint: 655.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "44fee0072543f66f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "367 U.S. 643 (1961)", "court": "U.S. Supreme Court", "neutral_cite": "1961 U.S. LEXIS 812", "official_citation_present": true, "parallel_cite": "81 S. Ct. 1684; 6 L. Ed. 2d 1081", "title": "Mapp v. Ohio", "year": "1961"}}
{"assertion_id": "6f0a6ca2b7f4294f", "dimension": "support", "kind": "home_role", "locator": {"home": "Fruits & Attenuation"}, "payload": {"home": "Fruits & Attenuation", "role": "Key — Anchor", "title": "Mapp v. Ohio"}}
{"assertion_id": "96883f9e532c81ac", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The exclusionary rule applies to the States through the Fourteenth Amendment.", "title": "Mapp v. Ohio"}}
{"assertion_id": "b84b779e899715b8", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1961-06-19", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Mapp v. Ohio", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Mapp v. Ohio", "varies_by_point": "false"}}
{"assertion_id": "ec0eb9565b24ef88", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Mapp v. Ohio"}}
```

### lake record — Mapp v. Ohio

```json
{
  "schema_version": "s2.v1",
  "record_id": "Mapp v. Ohio",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Mapp v. Ohio",
    "case_name_short": "Mapp",
    "case_name_full": "Mapp v. Ohio",
    "input_case_name": "Mapp v. Ohio",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1961-10-09",
    "year": 1961,
    "docket": null,
    "cluster_id": 106285,
    "lead_opinion_id": 106285,
    "sibling_ids": [
      106285,
      9422279,
      9422280,
      9422281,
      9422282
    ],
    "absolute_url": "/opinion/106285/mapp-v-ohio/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8951163,
        "score": 20,
        "case_name": "Mapp v. Ohio"
      },
      {
        "cluster_id": 6861770,
        "score": 20,
        "case_name": "Mapp v. Ohio"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "367 U.S. 643",
      "volume": "367",
      "reporter": "U.S.",
      "page": "643",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "81 S. Ct. 1684",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "1684",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "6 L. Ed. 2d 1081",
        "volume": "6",
        "reporter": "L. Ed. 2d",
        "page": "1081",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1961 U.S. LEXIS 812",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "812",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "367 U.S. 643",
        "volume": "367",
        "reporter": "U.S.",
        "page": "643",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 S. Ct. 1684",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "1684",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "6 L. Ed. 2d 1081",
        "volume": "6",
        "reporter": "L. Ed. 2d",
        "page": "1081",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1961 U.S. LEXIS 812",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "812",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "367 U.S. 643",
    "official_selection": {
      "court_class": "scotus",
      "selected": "367 U.S. 643",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-655",
      "page": null,
      "quote": "--- # Mapp v. Ohio *367 U.S. 643 (1961)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Cleveland officers forced their way into Dollree Mapp's home without a valid warrant, searched it while looking for a bombing suspect and gambling materials, and found allegedly obscene materials, for which she was convicted. The Ohio courts admitted the unlawfully seized evidence, relying on *Wolf v. Colorado*, which had held the Fourth Amendment's exclusionary remedy was not binding on the States. ## Issue Whether evidence obtained by a search and seizure that violates the Fourth Amendment is inadmissible in a state criminal prosecution. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1961-06-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Mapp v. Ohio",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
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
        "journal_ref": "Mapp v. Ohio:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Raenard Romalle Douglas",
          "cluster_id": 10129058,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mapp v. Ohio:lane1_negative"
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
        "journal_ref": "Mapp v. Ohio:lane1_negative"
      },
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re WINSHIP",
          "cluster_id": 108111,
          "cite": [
            "25 L. Ed. 2d 368",
            "90 S. Ct. 1068",
            "397 U.S. 358",
            "1970 U.S. LEXIS 56"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neil v. Biggers",
          "cluster_id": 108639,
          "cite": [
            "34 L. Ed. 2d 401",
            "93 S. Ct. 375",
            "409 U.S. 188",
            "1972 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brecht v. Abrahamson",
          "cluster_id": 112845,
          "cite": [
            "123 L. Ed. 2d 353",
            "113 S. Ct. 1710",
            "507 U.S. 619",
            "1993 U.S. LEXIS 2981"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Simmons v. United States",
          "cluster_id": 107636,
          "cite": [
            "19 L. Ed. 2d 1247",
            "88 S. Ct. 967",
            "390 U.S. 377",
            "1968 U.S. LEXIS 2167"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106285 OR 9422279 OR 9422280 OR 9422281 OR 9422282) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjE3NTgwODAwMDAwJnM9NDg3MDgyOCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106285+OR+9422279+OR+9422280+OR+9422281+OR+9422282%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(106285 OR 9422279 OR 9422280 OR 9422281 OR 9422282)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MDY1JnM9MTA3OTgwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106285+OR+9422279+OR+9422280+OR+9422281+OR+9422282%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106285 OR 9422279 OR 9422280 OR 9422281 OR 9422282)",
        "reviewed": 134,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 134,
        "triage_read": 2,
        "triage_snippet_classified": 132
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106285 OR 9422279 OR 9422280 OR 9422281 OR 9422282)",
    "indexed_citing_opinions": 5734,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106285,
        "count": 5215,
        "count_source": "search"
      },
      {
        "opinion_id": 9422279,
        "count": 658,
        "count_source": "search"
      },
      {
        "opinion_id": 9422280,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9422281,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9422282,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 9090,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mapp-v-ohio.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNzI2MDImcz0xMDU5NDg2NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28106285+OR+9422279+OR+9422280+OR+9422281+OR+9422282%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 9422282,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 104937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 105055,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 105343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 106183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 106223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 1237532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 3580565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 9417418,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 98058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 101320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 103660,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 104006,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 104455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 104713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 104937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 105055,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 105336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 105343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 105382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 105911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 106180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 106183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 106223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 1237532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 3580565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 3780866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 9417418,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 9420649,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 9422279,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 98058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 101320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 103660,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 104006,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 104713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 105336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 105343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 105382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 105911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 106180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 1237532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 3580565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 104006,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 104455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 9420649,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 104937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 105343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 106180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 3780866,
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
    "date_created": "2026-07-05T11:39:19Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:39:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:39:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:42:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:39:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Mapp v. Ohio (truncated)

```
<div>
<center><b><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U.S. 643</a></span> (1961)</b></center>
<center><h1>MAPP<br>
v.<br>
OHIO.</h1></center>
<center>No. 236.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 29, 1961.</center>
<center>Decided June 19, 1961.</center>
APPEAL FROM THE SUPREME COURT OF OHIO.
<p><i>A. L. Kearns</i> argued the cause for appellant. With him on the brief was <i>Walter L. Greene.</i></p>
<p><i>Gertrude Bauer Mahon</i> argued the cause for appellee. With her on the brief was <i>John T. Corrigan.</i></p>
<p><i>Bernard A. Berkman</i> argued the cause for the American Civil Liberties Union et al., as <i>amici curiae,</i> urging reversal. With him on the brief was <i>Rowland Watts.</i></p>
<p>MR. JUSTICE CLARK delivered the opinion of the Court.</p>
<p>Appellant stands convicted of knowingly having had in her possession and under her control certain lewd and lascivious books, pictures, and photographs in violation of § 2905.34 of Ohio's Revised Code.<sup>[1]</sup> As officially stated in the syllabus to its opinion, the Supreme Court of Ohio found that her conviction was valid though "based primarily upon the introduction in evidence of lewd and lascivious books and pictures unlawfully seized during an unlawful search of defendant's home . . . ." <span class="citation no-link">170 Ohio St. 427</span>-428, <span class="citation no-link">166 N. E. 2d 387</span>, 388.</p>
<p><span class="star-pagination">*644</span> On May 23, 1957, three Cleveland police officers arrived at appellant's residence in that city pursuant to information that "a person [was] hiding out in the home, who was wanted for questioning in connection with a recent bombing, and that there was a large amount of policy paraphernalia being hidden in the home." Miss Mapp and her daughter by a former marriage lived on the top floor of the two-family dwelling. Upon their arrival at that house, the officers knocked on the door and demanded entrance but appellant, after telephoning her attorney, refused to admit them without a search warrant. They advised their headquarters of the situation and undertook a surveillance of the house.</p>
<p>The officers again sought entrance some three hours later when four or more additional officers arrived on the scene. When Miss Mapp did not come to the door immediately, at least one of the several doors to the house was forcibly opened<sup>[2]</sup> and the policemen gained admittance. Meanwhile Miss Mapp's attorney arrived, but the officers, having secured their own entry, and continuing in their defiance of the law, would permit him neither to see Miss Mapp nor to enter the house. It appears that Miss Mapp was halfway down the stairs from the upper floor to the front door when the officers, in this highhanded manner, broke into the hall. She demanded to see the search warrant. A paper, claimed to be a warrant, was held up by one of the officers. She grabbed the "warrant" and placed it in her bosom. A struggle ensued in which the officers recovered the piece of paper and as a result of which they handcuffed appellant because she had been "belligerent" <span class="star-pagination">*645</span> in resisting their official rescue of the "warrant" from her person. Running roughshod over appellant, a policeman "grabbed" her, "twisted [her] hand," and she "yelled [and] pleaded with him" because "it was hurting." Appellant, in handcuffs, was then forcibly taken upstairs to her bedroom where the officers searched a dresser, a chest of drawers, a closet and some suitcases. They also looked into a photo album and through personal papers belonging to the appellant. The search spread to the rest of the second floor including the child's bedroom, the living room, the kitchen and a dinette. The basement of the building and a trunk found therein were also searched. The obscene materials for possession of which she was ultimately convicted were discovered in the course of that widespread search.</p>
<p>At the trial no search warrant was produced by the prosecution, nor was the failure to produce one explained or accounted for. At best, "There is, in the record, considerable doubt as to whether there ever was any warrant for the search of defendant's home." 170 Ohio St., at 430, 166 N. E. 2d, at 389. The Ohio Supreme Court believed a "reasonable argument" could be made that the conviction should be reversed "because the `methods' employed to obtain the [evidence] . . . were such as to `offend "a sense of justice," ' " but the court found determinative the fact that the evidence had not been taken "from defendant's person by the use of brutal or offensive physical force against defendant." 170 Ohio St., at 431, 166 N. E. 2d, at 389-390.</p>
<p>The State says that even if the search were made without authority, or otherwise unreasonably, it is not prevented from using the unconstitutionally seized evidence at trial, citing <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span> (1949), in which this Court did indeed hold "that in a prosecution in a State court for a State crime the Fourteenth Amendment <span class="star-pagination">*646</span> does not forbid the admission of evidence obtained by an unreasonable search and seizure." At p. 33. On this appeal, of which we have noted probable jurisdiction, <span class="citation multiple-matches"><a href="/c/U.%20S./364/868/">364 U. S. 868</a></span>, it is urged once again that we review that holding.<sup>[3]</sup></p>
<p></p>
<h2>I.</h2>
<p>Seventy-five years ago, in <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span> (1886), considering the Fourth<sup>[4]</sup> and Fifth Amendments as running "almost into each other"<sup>[5]</sup> on the facts before it, this Court held that the doctrines of those Amendments</p>
<blockquote>"apply to all invasions on the part of the government and its employes of the sanctity of a man's home and the privacies of life. It is not the breaking of his doors, and the rummaging of his drawers, <span class="star-pagination">*647</span> that constitutes the essence of the offence; but it is the invasion of his indefeasible right of personal security, personal liberty and private property . . . . Breaking into a house and opening boxes and drawers are circumstances of aggravation; but any forcible and compulsory extortion of a man's own testimony or of his private papers to be used as evidence to convict him of crime or to forfeit his goods, is within the condemnation . . . [of those Amendments]."</blockquote>
<p>The Court noted that</p>
<blockquote>"constitutional provisions for the security of person and property should be liberally construed. . . . It is the duty of courts to be watchful for the constitutional rights of the citizen, and against any stealthy encroachments thereon." At p. 635.</blockquote>
<p>In this jealous regard for maintaining the integrity of individual rights, the Court gave life to Madison's prediction that "independent tribunals of justice . . . will be naturally led to resist every encroachment upon rights expressly stipulated for in the Constitution by the declaration of rights." I Annals of Cong. 439 (1789). Concluding, the Court specifically referred to the use of the evidence there seized as "unconstitutional." At p. 638.</p>
<p>Less than 30 years after <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>,</i> this Court, in <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), stated that</p>
<blockquote>"the Fourth Amendment . . . put the courts of the United States and Federal officials, in the exercise of their power and authority, under limitations and restraints [and] . . . forever secure[d] the people, their persons, houses, papers and effects against all unreasonable searches and seizures under the guise of law . . . and the duty of giving to it force and effect is obligatory upon all entrusted under our Federal system with the enforcement of the laws." At pp. 391-392.</blockquote>
<p><span class="star-pagination">*648</span> Specifically dealing with the use of the evidence unconstitutionally seized, the Court concluded:</p>
<blockquote>"If letters and private documents can thus be seized and held and used in evidence against a citizen accused of an offense, the protection of the Fourth Amendment declaring his right to be secure against such searches and seizures is of no value, and, so far as those thus placed are concerned, might as well be stricken from the Constitution. The efforts of the courts and their officials to bring the guilty to punishment, praiseworthy as they are, are not to be aided by the sacrifice of those great principles established by years of endeavor and suffering which have resulted in their embodiment in the fundamental law of the land." At p. 393.</blockquote>
<p>Finally, the Court in that case clearly stated that use of the seized evidence involved "a denial of the constitutional rights of the accused." At p. 398. Thus, in the year 1914, in the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case, this Court "for the first time" held that "in a federal prosecution the Fourth Amendment barred the use of evidence secured through an illegal search and seizure." <i>Wolf</i> v. <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#28" aria-description="Citation for case: Wolf v. Colorado"><i>Colorado, supra,</i> at 28</a></span>. This Court has ever since required of federal law officers a strict adherence to that command which this Court has held to be a clear, specific, and constitutionally requiredeven if judicially implieddeterrent safeguard without insistence upon which the Fourth Amendment would have been reduced to "a form of words." Holmes, J., <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span> (1920). It meant, quite simply, that "conviction by means of unlawful seizures and enforced confessions . . . should find no sanction in the judgments of the courts . . .," <i>Weeks</i> v. <i>United States, supra,</i> at 392, and that such evidence "shall not be used at all." <i>Silverthorne Lumber Co.</i> v. <i>United States, supra,</i> at 392.</p>
<p><span class="star-pagination">*649</span> There are in the cases of this Court some passing references to the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule as being one of evidence. But the plain and unequivocal language of <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i>and its later paraphrase in <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i>to the effect that the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule is of constitutional origin, remains entirely undisturbed. In <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U. S. 28</a></span> (1927), a unanimous Court declared that "the doctrine [cannot] . . . be tolerated <i>under our constitutional system,</i> that evidences of crime discovered by a federal officer in making a search without lawful warrant may be used against the victim of the unlawful search where a timely challenge has been interposed." At pp. 29-30 (emphasis added). The Court, in <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span> (1928), in unmistakable language restated the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule:</p>
<blockquote>"The striking outcome of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case and those which followed it was the sweeping declaration that the Fourth Amendment, although not referring to or limiting the use of evidence in courts, really forbade its introduction if obtained by government officers through a violation of the Amendment." At p. 462.</blockquote>
<p>In <i>McNabb</i> v. <i>United States,</i> <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U. S. 332</a></span> (1943), we note this statement:</p>
<blockquote>"[A] conviction in the federal courts, the foundation of which is evidence obtained in disregard of liberties deemed fundamental by the Constitution, cannot stand. <i>Boyd</i> v. <i>United States</i> . . . <i>Weeks</i> v. <i>United States</i> . . . And this Court has, on Constitutional grounds, set aside convictions, both in the federal and state courts, which were based upon confessions `secured by protracted and repeated questioning of ignorant and untutored persons, in whose minds the power of officers was greatly magnified' <span class="star-pagination">*650</span>. . . or `who have been unlawfully held incommunicado without advice of friends or counsel'. . . ." At pp. 339-340.</blockquote>
<p>Significantly in <i><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">McNabb</a></span>,</i> the Court did then pass on to formulate a rule of evidence, saying, "[i]n the view we take of the case, however, it becomes unnecessary to reach the Constitutional issue [for] . . . [t]he principles governing the admissibility of evidence in federal criminal trials have not been restricted . . . to those derived solely from the Constitution." At pp. 340-341.</p>
<p></p>
<h2>II.</h2>
<p>In 1949, 35 years after <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> was announced, this Court, in <i>Wolf</i> v. <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Colorado, supra</a></span></i><i>,</i> again for the first time,<sup>[6]</sup> discussed the effect of the Fourth Amendment upon the States through the operation of the Due Process Clause of the Fourteenth Amendment. It said:</p>
<blockquote>"[W]e have no hesitation in saying that were a State affirmatively to sanction such police incursion into privacy it would run counter to the guaranty of the Fourteenth Amendment." At p. 28.</blockquote>
<p>Nevertheless, after declaring that the "security of one's privacy against arbitrary intrusion by the police" is "implicit in the concept of ordered liberty' and as such enforceable against the States through the Due Process Clause," cf. <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319</a></span> (1937), and announcing that it "stoutly adhere[d]" to the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> decision, the Court decided that the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule would not then be imposed upon the States as "an essential ingredient of the right." <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S., at 27-29</a></span>. The Court's reasons for not considering essential to the <span class="star-pagination">*651</span> right to privacy, as a curb imposed upon the States by the Due Process Clause, that which decades before had been posited as part and parcel of the Fourth Amendment's limitation upon federal encroachment of individual privacy, were bottomed on factual considerations.</p>
<p>While they are not basically relevant to a decision that the exclusionary rule is an essential ingredient of the Fourth Amendment as the right it embodies is vouchsafed against the States by the Due Process Clause, we will consider the current validity of the factual grounds upon which <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> was based.</p>
<p>The Court in <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> first stated that "[t]he contrariety of views of the States" on the adoption of the exclusionary rule of <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> was "particularly impressive" (at p. 29); and, in this connection, that it could not "brush aside the experience of States which deem the incidence of such conduct by the police too slight to call for a deterrent remedy . . . by overriding the [States'] relevant rules of evidence." At pp. 31-32. While in 1949, prior to the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> case, almost two-thirds of the States were opposed to the use of the exclusionary rule, now, despite the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> case, more than half of those since passing upon it, by their own legislative or judicial decision, have wholly or partly adopted or adhered to the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule. See <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S. 206</a></span>, Appendix, pp. 224-232 (1960). Significantly, among those now following the rule is California, which, according to its highest court, was "compelled to reach that conclusion because other remedies have completely failed to secure compliance with the constitutional provisions . . . ." <i>People</i> v. <i>Cahan,</i> <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/#445" aria-description="Citation for case: People v. Cahan">44 Cal. 2d 434, 445</a></span>, <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/#911" aria-description="Citation for case: People v. Cahan">282 P. 2d 905, 911</a></span> (1955). In connection with this California case, we note that the second basis elaborated in <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> in support of its failure to enforce the exclusionary doctrine against the States was that "other means of protection" have been afforded "the <span class="star-pagination">*652</span> right to privacy."<sup>[7]</sup> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#30" aria-description="Citation for case: Wolf v. Colorado">338 U. S., at 30</a></span>. The experience of California that such other remedies have been worthless and futile is buttressed by the experience of other States. The obvious futility of relegating the Fourth Amendment to the protection of other remedies has, moreover, been <span class="star-pagination">*653</span> recognized by this Court since <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>.</i> See <i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#137" aria-description="Citation for case: Irvine v. California">347 U. S. 128, 137</a></span> (1954).</p>
<p>Likewise, time has set its face against what <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> called the "weighty testimony" of <i>People</i> v. <i>Defore,</i> <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">242 N. Y. 13</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">150 N. E. 585</a></span> (1926). There Justice (then Judge) Cardozo, rejecting adoption of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule in New York, had said that "[t]he Federal rule as it stands is either too strict or too lax." <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#22" aria-description="Citation for case: People v. Defore">242 N. Y., at 22</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#588" aria-description="Citation for case: People v. Defore">150 N. E., at 588</a></span>. However, the force of that reasoning has been largely vitiated by later decisions of this Court. These include the recent discarding of the "silver platter" doctrine which allowed federal judicial use of evidence seized in violation of the Constitution by state agents, <i>Elkins</i> v. <i>United States, supra</i><i>;</i> the relaxation of the formerly strict requirements as to standing to challenge the use of evidence thus seized, so that now the procedure of exclusion, "ultimately referable to constitutional safeguards," is available to anyone even "legitimately on [the] premises" unlawfully searched, <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#266" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 266-267</a></span> (1960); and, finally, the formulation of a method to prevent state use of evidence unconstitutionally seized by federal agents, <i>Rea</i> v. <i>United States,</i> <span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/" aria-description="Citation for case: Rea v. United States">350 U. S. 214</a></span> (1956). Because there can be no fixed formula, we are admittedly met with "recurring questions of the reasonableness of searches," but less is not to be expected when dealing with a Constitution, and, at any rate, "[r]easonableness is in the first instance for the [trial court] . . . to determine." <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#63" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 63</a></span> (1950).</p>
<p>It, therefore, plainly appears that the factual considerations supporting the failure of the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> Court to include the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule when it recognized the enforceability of the right to privacy against the States in 1949, while not basically relevant to the constitutional consideration, could not, in any analysis, now be deemed controlling.</p>
<p></p>
<h2>
<span class="star-pagination">*654</span> III.</h2>
<p>Some five years after <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>,</i> in answer to a plea made here Term after Term that we overturn its doctrine on applicability of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule, this Court indicated that such should not be done until the States had "adequate opportunity to adopt or reject the [<span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States"><i>Weeks</i></a></span>] rule." <i>Irvine</i> v. <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#134" aria-description="Citation for case: Irvine v. California"><i>California, supra,</i> at 134</a></span>. There again it was said:</p>
<blockquote>"Never until June of 1949 did this Court hold the basic search-and-seizure prohibition in any way applicable to the states under the Fourteenth Amendment." <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Ibid.</a></span></i>
</blockquote>
<p>And only last Term, after again carefully re-examining the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> doctrine in <i>Elkins</i> v. <i>United States, supra</i><i>,</i> the Court pointed out that "the controlling principles" as to search and seizure and the problem of admissibility "seemed clear" (at p. 212) until the announcement in <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> "that the Due Process Clause of the Fourteenth Amendment does not itself require state courts to adopt the exclusionary rule" of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case. At p. 213. At the same time, the Court pointed out, "the underlying constitutional doctrine which <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> established . . . that the Federal Constitution . . . prohibits unreasonable searches and seizures by state officers" had undermined the "foundation upon which the admissibility of stateseized evidence in a federal trial originally rested . . . ." <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Ibid.</a></span></i> The Court concluded that it was therefore obliged to hold, although it chose the narrower ground on which to do so, that all evidence obtained by an unconstitutional search and seizure was inadmissible in a federal court regardless of its source. Today we once again examine <i>Wolf's</i> constitutional documentation of the right to privacy free from unreasonable state intrusion, and, after its dozen years on our books, are led by it to close the only <span class="star-pagination">*655</span> courtroom door remaining open to evidence secured by official lawlessness in flagrant abuse of that basic right, reserved to all persons as a specific guarantee against that very same unlawful conduct. We hold that all evidence obtained by searches and seizures in violation of the Constitution is, by that same authority, inadmissible in a state court.</p>
<p></p>
<h2>IV.</h2>
<p>Since the Fourth Amendment's right of privacy has been declared enforceable against the States through the Due Process Clause of the Fourteenth, it is enforceable against them by the same sanction of exclusion as is used against the Federal Government. Were it otherwise, then just as without the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule the assurance against unreasonable federal searches and seizures would be "a form of words," valueless and undeserving of mention in a perpetual charter of inestimable human liberties, so too, without that rule the freedom from state invasions of privacy would be so ephemeral and so neatly severed from its conceptual nexus with the freedom from all brutish means of coercing evidence as not to merit this Court's high regard as a freedom "implicit in the concept of ordered liberty." At the time that the Court held in <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> that the Amendment was applicable to the States through the Due Process Clause, the cases of this Court, as we have seen, had steadfastly held that as to federal officers the Fourth Amendment included the exclusion of the evidence seized in violation of its provisions. Even <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> "stoutly adhered" to that proposition. The right to privacy, when conceded operatively enforceable against the States, was not susceptible of destruction by avulsion of the sanction upon which its protection and enjoyment had always been deemed dependent under the <i>Boyd, Weeks</i> and <i>Silverthorne</i> cases. Therefore, in extending the substantive protections of due process to all constitutionally unreasonable searchesstate or federalit was <span class="star-pagination">*656</span> logically and constitutionally necessary that the exclusion doctrinean essential part of the right to privacybe also insisted upon as an essential ingredient of the right newly recognized by the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> case. In short, the admission of the new constitutional right by <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> could not consistently tolerate denial of its most important constitutional privilege, namely, the exclusion of the evidence which an accused had been forced to give by reason of the unlawful seizure. To hold otherwise is to grant the right but in reality to withhold its privilege and enjoyment. Only last year the Court itself recognized that the purpose of the exclusionary rule "is to deterto compel respect for the constitutional guaranty in the only effectively available wayby removing the incentive to disregard it." <i>Elkins</i> v. <i>United States, supra,</i> at 217.</p>
<p>Indeed, we are aware of no restraint, similar to that rejected today, conditioning the enforcement of any other basic constitutional right. The right to privacy, no less important than any other right carefully and particularly reserved to the people, would stand in marked contrast to all other rights declared as "basic to a free society." <i>Wolf</i> v. <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado"><i>Colorado, supra,</i> at 27</a></span>. This Court has not hesitated to enforce as strictly against the States as it does against the Federal Government the rights of free speech and of a free press, the rights to notice and to a fair, public trial, including, as it does, the right not to be convicted by use of a coerced confession, however logically relevant it be, and without regard to its reliability. <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534</a></span> (1961). And nothing could be more certain than that when a coerced confession is involved, "the relevant rules of evidence" are overridden without regard to "the incidence of such conduct by the police," slight or frequent. Why should not the same rule apply to what is tantamount to coerced testimony by way of unconstitutional seizure of goods, papers, effects, documents, etc.? We find that, <span class="star-pagination">*657</span> as to the Federal Government, the Fourth and Fifth Amendments and, as to the States, the freedom from unconscionable invasions of privacy and the freedom from convictions based upon coerced confessions do enjoy an "intimate relation"<sup>[8]</sup> in their perpetuation of "principles of humanity and civil liberty [secured] . . . only after years of struggle," <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#543" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 543-544</a></span> (1897). They express "supplementing phases of the same constitutional purposeto maintain inviolate large areas of personal privacy." <i>Feldman</i> v. <i>United States,</i> <span class="citation" data-id="9419517"><a href="/opinion/104006/feldman-v-united-states/#489" aria-description="Citation for case: Feldman v. United States">322 U. S. 487, 489-490</a></span> (1944). The philosophy of each Amendment and of each freedom is complementary to, although not dependent upon, that of the other in its sphere of influencethe very least that together they assure in either sphere is that no man is to be convicted on unconstitutional evidence. Cf. <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#173" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 173</a></span> (1952).</p>
<p></p>
<h2>V.</h2>
<p>Moreover, our holding that the exclusionary rule is an essential part of both the Fourth and Fourteenth Amendments is not only the logical dictate of prior cases, but it also makes very good sense. There is no war between the Constitution and common sense. Presently, a federal prosecutor may make no use of evidence illegally seized, but a State's attorney across the street may, although he supposedly is operating under the enforceable prohibitions of the same Amendment. Thus the State, by admitting evidence unlawfully seized, serves to encourage disobedience to the Federal Constitution which it is bound to uphold. Moreover, as was said in <i><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">Elkins</a></span>,</i> "[t]he very essence of a healthy federalism depends upon the avoidance of needless conflict between <span class="star-pagination">*658</span> state and federal courts." <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#221" aria-description="Citation for case: Elkins v. United States">364 U. S., at 221</a></span>. Such a conflict, hereafter needless, arose this very Term, in <i>Wilson</i> v. <i>Schnettler,</i> <span class="citation" data-id="9422132"><a href="/opinion/106180/wilson-v-schnettler/" aria-description="Citation for case: Wilson v. Schnettler">365 U. S. 381</a></span> (1961), in which, and in spite of the promise made by <i><span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/" aria-description="Citation for case: Rea v. United States">Rea</a></span>,</i> we gave full recognition to our practice in this regard by refusing to restrain a federal officer from testifying in a state court as to evidence unconstitutionally seized by him in the performance of his duties. Yet the double standard recognized until today hardly put such a thesis into practice. In non-exclusionary States, federal officers, being human, were by it invited to and did, as our cases indicate, step across the street to the State's attorney with their unconstitutionally seized evidence. Prosecution on the basis of that evidence was then had in a state court in utter disregard of the enforceable Fourth Amendment. If the fruits of an unconstitutional search had been inadmissible in both state and federal courts, this inducement to evasion would have been sooner eliminated. There would be no need to reconcile such cases as <i><span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/" aria-description="Citation for case: Rea v. United States">Rea</a></span></i> and <i><span class="citation" data-id="9422132"><a href="/opinion/106180/wilson-v-schnettler/" aria-description="Citation for case: Wilson v. Schnettler">Schnettler</a></span>,</i> each pointing up the hazardous uncertainties of our heretofore ambivalent approach.</p>
<p>Federal-state cooperation in the solution of crime under constitutional standards will be promoted, if only by recognition of their now mutual obligation to respect the same fundamental criteria in their approaches. "However much in a particular case insistence upon such rules may appear as a technicality that inures to the benefit of a guilty person, the history of the criminal law proves that tolerance of shortcut methods in law enforcement impairs its enduring effectiveness." <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#313" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 313</a></span> (1958). Denying shortcuts to only one of two cooperating law enforcement agencies tends naturally to breed legitimate suspicion of "working arrangements" whose results are equally tainted. <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U. S. 28</a></span> (1927); <i>Lustig</i> v. <i>United States,</i> <span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/" aria-description="Citation for case: Lustig v. United States">338 U. S. 74</a></span> (1949).</p>
<p><span class="star-pagination">*659</span> There are those who say, as did Justice (then Judge) Cardozo, that under our constitutional exclusionary doctrine "[t]he criminal is to go free because the constable has blundered." <i>People</i> v. <i>Defore,</i> <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#21" aria-description="Citation for case: People v. Defore">242 N. Y., at 21</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#587" aria-description="Citation for case: People v. Defore">150 N. E., at 587</a></span>. In some cases this will undoubtedly be the result.<sup>[9]</sup> But, as was said in <i><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">Elkins</a></span>,</i> "there is another considerationthe imperative of judicial integrity." <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#222" aria-description="Citation for case: Elkins v. United States">364 U. S., at 222</a></span>. The criminal goes free, if he must, but it is the law that sets him free. Nothing can destroy a government more quickly than its failure to observe its own laws, or worse, its disregard of the charter of its own existence. As Mr. Justice Brandeis, dissenting, said in <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#485" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 485</a></span> (1928): "Our Government is the potent, the omnipresent teacher. For good or for ill, it teaches the whole people by its example. . . . If the Government becomes a lawbreaker, it breeds contempt for law; it invites every man to become a law unto himself; it invites anarchy." Nor can it lightly be assumed that, as a practical matter, adoption of the exclusionary rule fetters law enforcement. Only last year this Court expressly considered that contention and found that "pragmatic evidence of a sort" to the contrary was not wanting. <i>Elkins</i> v. <i>United States, supra,</i> at 218. The Court noted that</p>
<blockquote>"The federal courts themselves have operated under the exclusionary rule of <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> for almost half a century; <span class="star-pagination">*660</span> yet it has not been suggested either that the Federal Bureau of Investigation<sup>[10]</sup> has thereby been rendered ineffective, or that the administration of criminal justice in the federal courts has thereby been disrupted. Moreover, the experience of the states is impressive. . . . The movement towards the rule of exclusion has been halting but seemingly inexorable." <i>Id.,</i> at 218-219.</blockquote>
<p>The ignoble shortcut to conviction left open to the State tends to destroy the entire system of constitutional restraints on which the liberties of the people rest.<sup>[11]</sup> Having once recognized that the right to privacy embodied in the Fourth Amendment is enforceable against the States, and that the right to be secure against rude invasions of privacy by state officers is, therefore, constitutional in origin, we can no longer permit that right to remain an empty promise. Because it is enforceable in the same manner and to like effect as other basic rights secured by the Due Process Clause, we can no longer permit it to be revocable at the whim of any police officer who, in the name of law enforcement itself, chooses to suspend its enjoyment. Our decision, founded on reason and truth, gives to the individual no more than that which the Constitution guarantees him, to the police officer no less than that to which honest law enforcement is entitled, and, to the courts, that judicial integrity so necessary in the true administration of justice.</p>
<p>The judgment of the Supreme Court of Ohio is reversed and the cause remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>Reversed and remanded.</i></p>
<p><span class="star-pagination">*661</span> MR. JUSTICE BLACK, concurring.</p>
<p>For nearly fifty years, since the decision of this Court in <i>Weeks</i> v. <i>United States</i><i>,</i><sup>[1]</sup> federal courts have refused to permit the introduction into evidence against an accused of his papers and effects obtained by "unreasonable searches and seizures" in violation of the Fourth Amendment. In <i>Wolf</i> v. <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Colorado</a></span></i><i>,</i> decided in 1948, however, this Court held that "in a prosecution in a State court for a State crime the Fourteenth Amendment does not forbid the admission of evidence obtained by an unreasonable search and seizure."<sup>[2]</sup> I concurred in that holding on these grounds:</p>
<blockquote>"For reasons stated in my dissenting opinion in <i>Adamson</i> v. <i>California,</i> <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/#68" aria-description="Citation for case: Adamson v. California">332 U. S. 46, 68</a></span>, I agree with the conclusion of the Court that the Fourth Amendment's prohibition of `unreasonable searches and seizures' is enforceable against the states. Consequently, I should be for reversal of this case if I thought the Fourth Amendment not only prohibited `unreasonable searches and seizures,' but also, of itself, barred the use of evidence so unlawfully obtained. But I agree with what appears to be a plain implication of the Court's opinion that the federal exclusionary rule is not a command of the Fourth Amendment but is a judicially created rule of evidence which Congress might negate."<sup>[3]</sup></blockquote>
<p>I am still not persuaded that the Fourth Amendment, standing alone, would be enough to bar the introduction into evidence against an accused of papers and effects seized from him in violation of its commands. For the Fourth Amendment does not itself contain any provision expressly precluding the use of such evidence, and I am <span class="star-pagination">*662</span> extremely doubtful that such a provision could properly be inferred from nothing more than the basic command against unreasonable searches and seizures. Reflection on the problem, however, in the light of cases coming before the Court since <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>,</i> has led me to conclude that when the Fourth Amendment's ban against unreasonable searches and seizures is considered together with the Fifth Amendment's ban against compelled self-incrimination, a constitutional basis emerges which not only justifies but actually requires the exclusionary rule.</p>
<p>The close interrelationship between the Fourth and Fifth Amendments, as they apply to this problem,<sup>[4]</sup> has long been recognized and, indeed, was expressly made the ground for this Court's holding in <i>Boyd</i> v. <i>United States</i><i>.</i><sup>[5]</sup> There the Court fully discussed this relationship and declared itself "unable to perceive that the seizure of a man's private books and papers to be used in evidence against him is substantially different from compelling him to be a witness against himself."<sup>[6]</sup> It was upon this ground that Mr. Justice Rutledge largely relied in his dissenting opinion in the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> case.<sup>[7]</sup> And, although I rejected the argument at that time, its force has, for me at least, become compelling with the more thorough understanding of the problem brought on by recent cases. In the final analysis, it seems to me that the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> doctrine, though perhaps not required by the express language of the Constitution strictly construed, is amply justified from an historical standpoint, soundly based in reason, <span class="star-pagination">*663</span> and entirely consistent with what I regard to be the proper approach to interpretation of our Bill of Rightsan approach well set out by Mr. Justice Bradley in the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case:</p>
<blockquote>"[C]onstitutional provisions for the security of person and property should be liberally construed. A close and literal construction deprives them of half their efficacy, and leads to gradual depreciation of the right, as if it consisted more in sound than in substance. It is the duty of the courts to be watchful for the constitutional rights of the citizen, and against any stealthy encroachments thereon."<sup>[8]</sup></blockquote>
<p>The case of <i>Rochin</i> v. <i>California</i><i>,</i><sup>[9]</sup> which we decided three years after the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> case, authenticated, I think, the soundness of Mr. Justice Bradley's and Mr. Justice Rutledge's reliance upon the interrelationship between the Fourth and Fifth Amendments as requiring the exclusion of unconstitutionally seized evidence. In the <i><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span></i> case, three police officers, acting with neither a judicial warrant nor probable cause, entered Rochin's home for the purpose of conducting a search and broke down the door to a bedroom occupied by Rochin and his wife. Upon their entry into the room, the officers saw Rochin pick up and swallow two small capsules. They immediately seized him and took him in handcuffs to a hospital where the capsules <span class="star-pagination">*664</span> were recovered by use of a stomach pump. Investigation showed that the capsules contained morphine and evidence of that fact was made the basis of his conviction of a crime in a state court.</p>
<p>When the question of the validity of that conviction was brought here, we were presented with an almost perfect example of the interrelationship between the Fourth and Fifth Amendments. Indeed, every member of this Court who participated in the decision of that case recognized this interrelationship and relied on it, to some extent at least, as justifying reversal of Rochin's conviction. The majority, though careful not to mention the Fifth Amendment's provision that "[n]o person . . . shall be compelled in any criminal case to be a witness against himself," showed at least that it was not unaware that such a provision exists, stating: "Coerced confessions offend the community's sense of fair play and decency . . . . It would be a stultification of the responsibility which the course of constitutional history has cast upon this Court to hold that in order to convict a man the police cannot extract by force what is in his mind but can extract what is in his stomach."<sup>[10]</sup> The methods used by the police thus were, according to the majority, "too close to the rack and the screw to permit of constitutional differentiation,"<sup>[11]</sup> and the case was reversed on the ground that these methods had violated the Due Process Clause of the Fourteenth Amendment in that the treatment accorded Rochin was of a kind that "shocks the conscience," "offend[s] `a sense of justice' " and fails to "respect certain decencies of civilized conduct."<sup>[12]</sup></p>
<p>I concurred in the reversal of the <i><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span></i> case, but on the ground that the Fourteenth Amendment made the Fifth Amendment's provision against self-incrimination <span class="star-pagination">*665</span> applicable to the States and that, given a broad rather than a narrow construction, that provision barred the introduction of this "capsule" evidence just as much as it would have forbidden the use of words Rochin might have been coerced to speak.<sup>[13]</sup> In reaching this conclusion I cited and relied on the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case, the constitutional doctrine of which was, of course, necessary to my disposition of the case. At that time, however, these views were very definitely in the minority for only MR. JUSTICE DOUGLAS and I rejected the flexible and uncertain standards of the "shock-the-conscience test" used in the majority opinion.<sup>[14]</sup></p>
<p>Two years after <i><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span>,</i> in <i>Irvine</i> v. <i>California</i><i>,</i><sup>[15]</sup> we were again called upon to consider the validity of a conviction based on evidence which had been obtained in a manner clearly unconstitutional and arguably shocking to the conscience. The five opinions written by this Court in that case demonstrate the utter confusion and uncertainty that had been brought about by the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> and <i><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span></i> decisions. In concurring, MR. JUSTICE CLARK emphasized the unsatisfactory nature of the Court's "shock-the-conscience test," saying that this "test" "makes for such uncertainty and unpredictability that it would be impossible to foretellother than by guessworkjust how brazen the invasion of the intimate privacies of one's home must be in order to shock itself into the protective arms of the Constitution. In truth, the practical result of this <i>ad hoc</i> approach is simply that when five Justices are sufficiently revolted by local police action, a conviction is overturned and a guilty man may go free."<sup>[16]</sup></p>
<p><span class="star-pagination">*666</span> Only one thing emerged with complete clarity from the <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Irvine</a></span></i> casethat is that seven Justices rejected the "shock-the-conscience" constitutional standard enunciated in the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> and <i><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span></i> cases. But even this did not lessen the confusion in this area of the law because the continued existence of mutually inconsistent precedents together with the Court's inability to settle upon a majority opinion in the <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Irvine</a></span></i> case left the situation at least as uncertain as it had been before.<sup>[17]</sup> Finally, today, we clear up that uncertainty. As I understand the Court's opinion in this case, we again reject the confusing "shock-the-conscience" standard of the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> and <i><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span></i> cases and, instead, set aside this state conviction in reliance upon the precise, intelligible and more predictable constitutional doctrine enunciated in the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case. I fully agree with Mr. Justice Bradley's opinion that the two Amendments upon which the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> doctrine rests are of vital importance in our constitutional scheme of liberty and that both are entitled to a liberal rather than a niggardly interpretation. The courts of the country are entitled to know with as much certainty as possible what scope they cover. The Court's opinion, in my judgment, dissipates the doubt and uncertainty in this field of constitutional law and I am persuaded, for this and other reasons stated, to depart from my prior views, to accept the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> doctrine as controlling in this state case and to join the Court's judgment and opinion which are in accordance with that constitutional doctrine.</p>
<p>MR. JUSTICE DOUGLAS, concurring.</p>
<p>Though I have joined the opinion of the Court, I add a few words. This criminal proceeding started with a lawless search and seizure. The police entered a home <span class="star-pagination">*667</span> forcefully, and seized documents that were later used to convict the occupant of a crime.</p>
<p>She lived alone with her fifteen-year-old daughter in the second-floor flat of a duplex in Cleveland. At about 1:30 in the afternoon of May 23, 1957, three policemen arrived at this house. They rang the bell, and the appellant, appearing at her window, asked them what they wanted. According to their later testimony, the policemen had come to the house on information from "a confidential source that there was a person hiding out in the home, who was wanted for questioning in connection with a recent bombing."<sup>[1]</sup> To the appellant's question, however, they replied only that they wanted to question her and would not state the subject about which they wanted to talk.</p>
<p>The appellant, who had retained an attorney in connection with a pending civil matter, told the police she would call him to ask if she should let them in. On her attorney's advice, she told them she would let them in only when they produced a valid search warrant. For the next two and a half hours, the police laid siege to the house. At four o'clock, their number was increased to at least seven. Appellant's lawyer appeared on the scene; and one of the policemen told him that they now had a search warrant, but the officer refused to show it. Instead, going to the back door, the officer first tried to kick it in and, when that proved unsuccessful, he broke the glass in the door and opened it from the inside.</p>
<p>The appellant, who was on the steps going up to her flat, demanded to see the search warrant; but the officer refused to let her see it although he waved a paper in front of her face. She grabbed it and thrust it down the front of her dress. The policemen seized her, took the paper <span class="star-pagination">*668</span> from her, and had her handcuffed to another officer. She was taken upstairs, thus bound, and into the larger of the two bedrooms in the apartment; there she was forced to sit on the bed. Meanwhile, the officers entered the house and made a complete search of the four rooms of her flat and of the basement of the house.</p>
<p>The testimony concerning the search is largely nonconflicting. The approach of the officers; their long wait outside the home, watching all its doors; the arrival of reinforcements armed with a paper;<sup>[2]</sup> breaking into the house; putting their hands on appellant and handcuffing her; numerous officers ransacking through every room and piece of furniture, while the appellant sat, a prisoner in her own bedroom. There is direct conflict in the testimony, however, as to where the evidence which is the basis of this case was found. To understand the meaning of that conflict, one must understand that this case is based on the knowing possession<sup>[3]</sup> of four little pamphlets, a couple of photographs and a little pencil doodleall of which are alleged to be pornographic.</p>
<p>According to the police officers who participated in the search, these articles were found, some in appellant's <span class="star-pagination">*669</span> dressers and some in a suitcase found by her bed. According to appellant, most of the articles were found in a cardboard box in the basement; one in the suitcase beside her bed. All of this material, appellantand a friend of herssaid were odds and ends belonging to a recent boarder, a man who had left suddenly for New York and had been detained there. As the Supreme Court of Ohio read the statute under which appellant is charged, she is guilty of the crime whichever story is true.</p>
<p>The Ohio Supreme Court sustained the conviction even though it was based on the documents obtained in the lawless search. For in Ohio evidence obtained by an unlawful search and seizure is admissible in a criminal prosecution at least where it was not taken from the "defendant's person by the use of brutal or offensive force against defendant." <i>State</i> v. <i>Mapp,</i> <span class="citation no-link">170 Ohio St. 427</span>, 166 N. E. 2d, at 388, syllabus 2; <i>State</i> v. <i>Lindway,</i> <span class="citation" data-id="3780866"><a href="/opinion/4024496/state-v-lindway/" aria-description="Citation for case: State v. Lindway">131 Ohio St. 166</a></span>, <span class="citation" data-id="3780866"><a href="/opinion/4024496/state-v-lindway/" aria-description="Citation for case: State v. Lindway">2 N. E. 2d 490</a></span>. This evidence would have been inadmissible in a federal prosecution. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>; <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S. 206</a></span>. For, as stated in the former decision, "The effect of the Fourth Amendment is to put the courts of the United States and Federal officials, in the exercise of their power and authority, under limitations and restraints . . . ." <i>Id.,</i> 391-392. It was therefore held that evidence obtained (which in that case was documents and correspondence) from a home without any warrant was not admissible in a federal prosecution.</p>
<p>We held in <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>, that the Fourth Amendment was applicable to the States by reason of the Due Process Clause of the Fourteenth Amendment. But a majority held that the exclusionary rule of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case was not required of the States, that they could apply such sanctions as they chose. That position had the necessary votes to carry the day. But with all respect it was not the voice of reason or principle.</p>
<p><span class="star-pagination">*670</span> As stated in the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case, if evidence seized in violation of the Fourth Amendment can be used against an accused, "his right to be secure against such searches and seizures is of no value, and . . . might as well be stricken from the Constitution." <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#393" aria-description="Citation for case: Weeks v. United States">232 U. S., at 393</a></span>.</p>
<p>When we allowed States to give constitutional sanction to the "shabby business" of unlawful entry into a home (to use an expression of Mr. Justice Murphy, <i>Wolf</i> v. <i>Colorado</i><i>,</i> at 46), we did indeed rob the Fourth Amendment of much meaningful force. There are, of course, other theoretical remedies. One is disciplinary action within the hierarchy of the police system, including prosecution of the police officer for a crime. Yet as Mr. Justice Murphy said in <i>Wolf</i> v. <i>Colorado</i><i>,</i> at 42, "Self-scrutiny is a lofty ideal, but its exaltation reaches new heights if we expect a District Attorney to prosecute himself or his associates for well-meaning violations of the search and seizure clause during a raid the District Attorney or his associates have ordered."</p>
<p>The only remaining remedy, if exclusion of the evidence is not required, is an action of trespass by the homeowner against the offending officer. Mr. Justice Murphy showed how onerous and difficult it would be for the citizen to maintain that action and how meagre the relief even if the citizen prevails. <span class="citation multiple-matches"><a href="/c/U.%20S./338/42/">338 U. S. 42</a></span>-44. The truth is that trespass actions against officers who make unlawful searches and seizures are mainly illusory remedies.</p>
<p>Without judicial action making the exclusionary rule applicable to the States, <i>Wolf</i> v. <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Colorado</a></span></i> in practical effect reduced the guarantee against unreasonable searches and seizures to "a dead letter," as Mr. Justice Rutledge said in his dissent. See 338 U. S., at 47.</p>
<p><i>Wolf</i> v. <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Colorado, supra</a></span></i><i>,</i> was decided in 1949. The immediate result was a storm of constitutional controversy which only today finds its end. I believe that this is an appropriate case in which to put an end to the asymmetry which <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> imported into the law. See <span class="star-pagination">*671</span> <i>Stefanelli</i> v. <i>Minard,</i> <span class="citation" data-id="9420643"><a href="/opinion/104937/stefanelli-v-minard/" aria-description="Citation for case: Stefanelli v. Minard">342 U. S. 117</a></span>; <i>Rea</i> v. <i>United States,</i> <span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/" aria-description="Citation for case: Rea v. United States">350 U. S. 214</a></span>; <i>Elkins</i> v. <i>United States, supra</i><i>; </i><i>Monroe</i> v. <i>Pape,</i> <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167</a></span>. It is an appropriate case because the facts it presents showas would few other cases the casual arrogance of those who have the untrammelled power to invade one's home and to seize one's person.</p>
<p>It is also an appropriate case in the narrower and more technical sense. The issues of the illegality of the search and the admissibility of the evidence have been presented to the state court and were duly raised here in accordance with the applicable Rule of Practice.<sup>[4]</sup> The question was raised in the notice of appeal, the jurisdictional statement and in appellant's brief on the merits.<sup>[5]</sup> It is true that argument was mostly directed to another issue in the case, but that is often the fact. See <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#535" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 535-540</a></span>. Of course, an earnest advocate of a position always believes that, had he only an additional opportunity for argument, his side would win. But, subject to the sound discretion of a court, all argument must at last come to a halt. This is especially so as to an issue about which this Court said last year that "The arguments of its antagonists and of its proponents have been so many times marshalled as to require no lengthy elaboration here." <i>Elkins</i> v. <i>United States, supra,</i> 216.</p>
<p>Moreover, continuance of <i>Wolf</i> v. <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Colorado</a></span></i> in its full vigor breeds the unseemly shopping around of the kind revealed in <i>Wilson</i> v. <i>Schnettler,</i> <span class="citation" data-id="9422132"><a href="/opinion/106180/wilson-v-schnettler/" aria-description="Citation for case: Wilson v. Schnettler">365 U. S. 381</a></span>. Once evidence, inadmissible in a federal court, is admissible in <span class="star-pagination">*672</span> a state court a "double standard" exists which, as the Court points out, leads to "working arrangements" that undercut federal policy and reduce some aspects of law enforcement to shabby business. The rule that supports that practice does not have the force of reason behind it.</p>
<p>Memorandum of MR. JUSTICE STEWART.</p>
<p>Agreeing fully with Part I of MR. JUSTICE HARLAN'S dissenting opinion, I express no view as to the merits of the constitutional issue which the Court today decides. I would, however, reverse the judgment in this case, because I am persuaded that the provision of § 2905.34 of the Ohio Revised Code, upon which the petitioner's conviction was based, is, in the words of MR. JUSTICE HARLAN, not "consistent with the rights of free thought and expression assured against state action by the Fourteenth Amendment."</p>
<p>MR. JUSTICE HARLAN, whom MR. JUSTICE FRANKFURTER and MR. JUSTICE WHITTAKER join, dissenting.</p>
<p>In overruling the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> case the Court, in my opinion, has forgotten the sense of judicial restraint which, with due regard for <i>stare decisis,</i> is one element that should enter into deciding whether a past decision of this Court should be overruled. Apart from that I also believe that the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> rule represents sounder Constitutional doctrine than the new rule which now replaces it.</p>
<p></p>
<h2>I.</h2>
<p>From the Court's statement of the case one would gather that the central, if not controlling, issue on this appeal is whether illegally state-seized evidence is Constitutionally admissible in a state prosecution, an issue which would of course face us with the need for re-examining <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>.</i> However, such is not the situation. For, although that question was indeed raised here and below among appellant's subordinate points, the new and <span class="star-pagination">*673</span> pivotal issue brought to the Court by this appeal is whether § 2905.34 of the Ohio Revised Code making criminal the <i>mere</i> knowing possession or control of obscene material,<sup>[1]</sup> and under which appellant has been convicted, is consistent with the rights of free thought and expression assured against state action by the Fourteenth Amendment.<sup>[2]</sup> That was the principal issue which was decided by the Ohio Supreme Court,<sup>[3]</sup> which was tendered by appellant's Jurisdictional Statement,<sup>[4]</sup> and which was briefed<sup>[5]</sup> and argued<sup>[6]</sup> in this Court.</p>
<p><span class="star-pagination">*674</span> In this posture of things, I think it fair to say that five members of this Court have simply "reached out" to overrule <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>.</i> With all respect for the views of the majority, and recognizing that <i>stare decisis</i> carries different <span class="star-pagination">*675</span> weight in Constitutional adjudication than it does in nonconstitutional decision, I can perceive no justification for regarding this case as an appropriate occasion for re-examining <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>.</i></p>
<p>The action of the Court finds no support in the rule that decision of Constitutional issues should be avoided wherever possible. For in overruling <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> the Court, instead of passing upon the validity of Ohio's § 2905.34, has simply chosen between two Constitutional questions. Moreover, I submit that it has chosen the more difficult and less appropriate of the two questions. The Ohio statute which, as construed by the State Supreme Court, punishes knowing possession or control of obscene material, irrespective of the purposes of such possession or control (with exceptions not here applicable)<sup>[7]</sup> and irrespective of whether the accused had any reasonable opportunity to rid himself of the material after discovering that it was obscene,<sup>[8]</sup> surely presents a Constitutional <span class="star-pagination">*676</span> question which is both simpler and less far-reaching than the question which the Court decides today. It seems to me that justice might well have been done in this case without overturning a decision on which the administration of criminal law in many of the States has long justifiably relied.</p>
<p>Since the demands of the case before us do not require us to reach the question of the validity of <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>,</i> I think this case furnishes a singularly inappropriate occasion for reconsideration of that decision, if reconsideration is indeed warranted. Even the most cursory examination will reveal that the doctrine of the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> case has been of continuing importance in the administration of state criminal law. Indeed, certainly as regards its "non-exclusionary" aspect, <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> did no more than articulate the then existing assumption among the States that the federal cases enforcing the exclusionary rule "do not bind [the States], for they construe provisions of the Federal Constitution, the Fourth and Fifth Amendments, not applicable to the States." <i>People</i> v. <i>Defore,</i> <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#20" aria-description="Citation for case: People v. Defore">242 N. Y. 13, 20</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#587" aria-description="Citation for case: People v. Defore">150 N. E. 585, 587</a></span>. Though, of course, not reflecting the full measure of this continuing reliance, I find that during the last three Terms, for instance, the issue of the inadmissibility of illegally state-obtained evidence appears on an average of about fifteen times per Term just in the <i>in forma pauperis</i> cases summarily disposed of by us. This would indicate both that the issue which is now being decided may well have untoward practical ramifications respecting state cases long since disposed of in reliance on <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>,</i> and that were we determined to re-examine that doctrine we would not lack future opportunity.</p>
<p>The occasion which the Court has taken here is in the context of a case where the question was briefed not at all and argued only extremely tangentially. The unwisdom of overruling <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> without full-dress argument <span class="star-pagination">*677</span> is aggravated by the circumstance that that decision is a comparatively recent one (1949) to which three members of the present majority have at one time or other expressly subscribed, one to be sure with explicit misgivings.<sup>[9]</sup> I would think that our obligation to the States, on whom we impose this new rule, as well as the obligation of orderly adherence to our own processes would demand that we seek that aid which adequate briefing and argument lends to the determination of an important issue. It certainly has never been a postulate of judicial power that mere altered disposition, or subsequent membership on the Court, is sufficient warrant for overturning a deliberately decided rule of Constitutional law.</p>
<p>Thus, if the Court were bent on reconsidering <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>,</i> I think that there would soon have presented itself an appropriate opportunity in which we could have had the benefit of full briefing and argument. In any event, at the very least, the present case should have been set down for reargument, in view of the inadequate briefing and argument we have received on the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> point. To all intents and purposes the Court's present action amounts to a summary reversal of <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>,</i> without argument.</p>
<p>I am bound to say that what has been done is not likely to promote respect either for the Court's adjudicatory process or for the stability of its decisions. Having been unable, however, to persuade any of the majority to a different procedural course, I now turn to the merits of the present decision.</p>
<p></p>
<h2>
<span class="star-pagination">*678</span> II.</h2>
<p>Essential to the majority's argument against <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> is the proposition that the rule of <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, excluding in federal criminal trials the use of evidence obtained in violation of the Fourth Amendment, derives not from the "supervisory power" of this Court over the federal judicial system, but from Constitutional requirement. This is so because no one, I suppose, would suggest that this Court possesses any general supervisory power over the state courts. Although I entertain considerable doubt as to the soundness of this foundational proposition of the majority, cf. <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#39" aria-description="Citation for case: Wolf v. Colorado">338 U. S., at 39-40</a></span> (concurring opinion), I shall assume, for present purposes, that the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule "is of constitutional origin."</p>
<p>At the heart of the majority's opinion in this case is the following syllogism: (1) the rule excluding in federal criminal trials evidence which is the product of an illegal search and seizure is "part and parcel" of the Fourth Amendment; (2) <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> held that the "privacy" assured against federal action by the Fourth Amendment is also protected against state action by the Fourteenth Amendment; and (3) it is therefore "logically and constitutionally necessary" that the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule should also be enforced against the States.<sup>[10]</sup></p>
<p>This reasoning ultimately rests on the unsound premise that because <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> carried into the States, as part of "the concept of ordered liberty" embodied in the Fourteenth Amendment, the principle of "privacy" underlying the Fourth Amendment (338 U. S., at 27), it must follow that whatever configurations of the Fourth Amendment have been developed in the particularizing federal precedents are likewise to be deemed a part of "ordered liberty," <span class="star-pagination">*679</span> and as such are enforceable against the States. For me, this does not follow at all.</p>
<p>It cannot be too much emphasized that what was recognized in <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> was not that the Fourth Amendment <i>as such</i> is enforceable against the States as a facet of due process, a view of the Fourteenth Amendment which, as <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> itself pointed out (338 U. S., at 26), has long since been discredited, but the principle of privacy "which is at the core of the Fourth Amendment." (<i>Id.,</i> at 27.) It would not be proper to expect or impose any precise equivalence, either as regards the scope of the right or the means of its implementation, between the requirements of the Fourth and Fourteenth Amendments. For the Fourth, unlike what was said in <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> of the Fourteenth, does not state a general principle only; it is a particular command, having its setting in a pre-existing legal context on which both interpreting decisions and enabling statutes must at least build.</p>
<p>Thus, even in a case which presented simply the question of whether a particular search and seizure was constitutionally "unreasonable"say in a tort action against state officerswe would not be true to the Fourteenth Amendment were we merely to stretch the general principle of individual privacy on a Procrustean bed of federal precedents under the Fourth Amendment. But in this instance more than that is involved, for here we are reviewing not a determination that what the state police did was Constitutionally permissible (since the state court quite evidently assumed that it was not), but a determination that appellant was properly found guilty of conduct which, for present purposes, it is to be assumed the State could Constitutionally punish. Since there is not the slightest suggestion that Ohio's policy is "affirmatively to sanction . . . police incursion into privacy" (338 U. S., at 28), compare <i>Marcus</i> v. <i>Search Warrants, post,</i> p. 717, what the Court is now doing is to impose <span class="star-pagination">*680</span> upon the States not only federal substantive standards of "search and seizure" but also the basic federal remedy for violation of those standards. For I think it entirely clear that the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule is but a remedy which, by penalizing past official misconduct, is aimed at deterring such conduct in the future.</p>
<p>I would not impose upon the States this federal exclusionary remedy. The reasons given by the majority for now suddenly turning its back on <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> seem to me notably unconvincing.</p>
<p>First, it is said that "the factual grounds upon which <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> was based" have since changed, in that more States now follow the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule than was so at the time <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> was decided. While that is true, a recent survey indicates that at present one-half of the States still adhere to the common-law non-exclusionary rule, and one, Maryland, retains the rule as to felonies. Berman and Oberst, Admissibility of Evidence Obtained by an Unconstitutional Search and Seizure, 55 N. W. L. Rev. 525, 532-533. But in any case surely all this is beside the point, as the majority itself indeed seems to recognize. Our concern here, as it was in <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>,</i> is not with the desirability of that rule but only with the question whether the States are Constitutionally free to follow it or not as they may themselves determine, and the relevance of the disparity of views among the States on this point lies simply in the fact that the judgment involved is a debatable one. Moreover, the very fact on which the majority relies, instead of lending support to what is now being done, points away from the need of replacing voluntary state action with federal compulsion.</p>
<p>The preservation of a proper balance between state and federal responsibility in the administration of criminal justice demands patience on the part of those who might like to see things move faster among the States in this respect. Problems of criminal law enforcement vary <span class="star-pagination">*681</span> widely from State to State. One State, in considering the totality of its legal picture, may conclude that the need for embracing the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule is pressing because other remedies are unavailable or inadequate to secure compliance with the substantive Constitutional principle involved. Another, though equally solicitous of Constitutional rights, may choose to pursue one purpose at a time, allowing all evidence relevant to guilt to be brought into a criminal trial, and dealing with Constitutional infractions by other means. Still another may consider the exclusionary rule too rough-and-ready a remedy, in that it reaches only unconstitutional intrusions which eventuate in criminal prosecution of the victims. Further, a State after experimenting with the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule for a time may, because of unsatisfactory experience with it, decide to revert to a non-exclusionary rule. And so on. From the standpoint of Constitutional permissibility in pointing a State in one direction or another, I do not see at all why "time has set its face against" the considerations which led Mr. Justice Cardozo, then chief judge of the New York Court of Appeals, to reject for New York in <i>People</i> v. <i>Defore,</i> <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">242 N. Y. 13</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">150 N. E. 585</a></span>, the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule. For us the question remains, as it has always been, one of state power, not one of passing judgment on the wisdom of one state course or another. In my view this Court should continue to forbear from fettering the States with an adamant rule which may embarrass them in coping with their own peculiar problems in criminal law enforcement.</p>
<p>Further, we are told that imposition of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule on the States makes "very good sense," in that it will promote recognition by state and federal officials of their "mutual obligation to respect the same fundamental criteria" in their approach to law enforcement, and will avoid " `needless conflict between state and federal courts.' " Indeed the majority now finds an incongruity <span class="star-pagination">*682</span> in <i>Wolf's</i> discriminating perception between the demands of "ordered liberty" as respects the basic right of "privacy" and the means of securing it among the States. That perception, resting both on a sensitive regard for our federal system and a sound recognition of this Court's remoteness from particular state problems, is for me the strength of that decision.</p>
<p>An approach which regards the issue as one of achieving procedural symmetry or of serving administrative convenience surely disfigures the boundaries of this Court's functions in relation to the state and federal courts. Our role in promulgating the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule and its extensions in such cases as <i>Rea, Elkins,</i> and <i>Rios</i><sup>[11]</sup> was quite a different one than it is here. There, in implementing the Fourth Amendment, we occupied the position of a tribunal having the ultimate responsibility for developing the standards and procedures of judicial administration within the judicial system over which it presides. Here we review state procedures whose measure is to be taken not against the specific substantive commands of the Fourth Amendment but under the flexible contours of the Due Process Clause. I do not believe that the Fourteenth Amendment empowers this Court to mould state remedies effectuating the right to freedom from "arbitrary intrusion by the police" to suit its own notions of how things should be done, as, for instance, the California Supreme Court did in <i>People</i> v. <i>Cahan,</i> <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/" aria-description="Citation for case: People v. Cahan">44 Cal. 2d 434</a></span>, <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/" aria-description="Citation for case: People v. Cahan">282 P. 2d 905</a></span>, with reference to procedures in the California courts or as this Court did in <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> for the lower federal courts.</p>
<p>A state conviction comes to us as the complete product of a sovereign judicial system. Typically a case will have been tried in a trial court, tested in some final appellate <span class="star-pagination">*683</span> court, and will go no further. In the comparatively rare instance when a conviction is reviewed by us on due process grounds we deal then with a finished product in the creation of which we are allowed no hand, and our task, far from being one of over-all supervision, is, speaking generally, restricted to a determination of whether the prosecution was Constitutionally fair. The specifics of trial procedure, which in every mature legal system will vary greatly in detail, are within the sole competence of the States. I do not see how it can be said that a trial becomes unfair simply because a State determines that evidence may be considered by the trier of fact, regardless of how it was obtained, if it is relevant to the one issue with which the trial is concerned, the guilt or innocence of the accused. Of course, a court may use its procedures as an incidental means of pursuing other ends than the correct resolution of the controversies before it. Such indeed is the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule, but if a State does not choose to use its courts in this way, I do not believe that this Court is empowered to impose this much-debated procedure on local courts, however efficacious we may consider the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule to be as a means of securing Constitutional rights.</p>
<p>Finally, it is said that the overruling of <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> is supported by the established doctrine that the admission in evidence of an involuntary confession renders a state conviction Constitutionally invalid. Since such a confession may often be entirely reliable, and therefore of the greatest relevance to the issue of the trial, the argument continues, this doctrine is ample warrant in precedent that the way evidence was obtained, and not just its relevance, is Constitutionally significant to the fairness of a trial. I believe this analogy is not a true one. The "coerced confession" rule is certainly not a rule that any illegally obtained statements may not be used in evidence. I would suppose that a statement which is procured during <span class="star-pagination">*684</span> a period of illegal detention, <i>McNabb</i> v. <i>United States,</i> <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U. S. 332</a></span>, is, as much as unlawfully seized evidence, illegally obtained, but this Court has consistently refused to reverse state convictions resting on the use of such statements. Indeed it would seem the Court laid at rest the very argument now made by the majority when in <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">314 U. S. 219</a></span>, a state-coerced confession case, it said (at 235):</p>
<blockquote>"It may be assumed [that the] treatment of the petitioner [by the police] . . . deprived him of his liberty without due process and that the petitioner would have been afforded preventive relief if he could have gained access to a court to seek it.</blockquote>
<blockquote>"But illegal acts, as such, committed in the course of obtaining a confession . . . do not furnish an answer to the constitutional question we must decide.. . . The gravamen of his complaint is the unfairness of the <i>use</i> of his confessions, and what occurred in their procurement is relevant only as it bears on that issue." (Emphasis supplied.)</blockquote>
<p>The point, then, must be that in requiring exclusion of an involuntary statement of an accused, we are concerned not with an appropriate remedy for what the police have done, but with something which is regarded as going to the heart of our concepts of fairness in judicial procedure. The operative assumption of our procedural system is that "Ours is the accusatorial as opposed to the inquisitorial system. Such has been the characteristic of Anglo-American criminal justice since it freed itself from practices borrowed by the Star Chamber from the Continent whereby the accused was interrogated in secret for hours on end." <i>Watts</i> v. <i>Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#54" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 54</a></span>. See <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#541" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 541</a></span>. The pressures brought to bear against an accused leading to a confession, unlike an unconstitutional violation of privacy, do not, apart <span class="star-pagination">*685</span> from the use of the confession at trial, necessarily involve independent Constitutional violations. What is crucial is that the trial defense to which an accused is entitled should not be rendered an empty formality by reason of statements wrung from him, for then "a prisoner. . . [has been] made the deluded instrument of his own conviction." 2 Hawkins, Pleas of the Crown (8th ed., 1824), c. 46, § 34. That this is a <i>procedural right,</i> and that its violation occurs at the time his improperly obtained statement is admitted at trial, is manifest. For without this right all the careful safeguards erected around the giving of testimony, whether by an accused or any other witness, would become empty formalities in a procedure where the most compelling possible evidence of guilt, a confession, would have already been obtained at the unsupervised pleasure of the police.</p>
<p>This, and not the disciplining of the police, as with illegally seized evidence, is surely the true basis for excluding a statement of the accused which was unconstitutionally obtained. In sum, I think the coerced confession analogy works strongly <i>against</i> what the Court does today.</p>
<p>In conclusion, it should be noted that the majority opinion in this case is in fact an opinion only for the <i>judgment</i> overruling <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>,</i> and not for the basic rationale by which four members of the majority have reached that result. For my Brother BLACK is unwilling to subscribe to their view that the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule derives from the Fourth Amendment itself (see <i>ante,</i> p. 661), but joins the majority opinion on the premise that its end result can be achieved by bringing the Fifth Amendment to the aid of the Fourth (see <i>ante,</i> pp. 662-665).<sup>[12]</sup> On that score I need only say that whatever the validity of <span class="star-pagination">*686</span> the "Fourth-Fifth Amendment" correlation which the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case (<span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>) found, see 8 Wigmore, Evidence (3d ed. 1940), § 2184, we have only very recently again reiterated the long-established doctrine of this Court that the Fifth Amendment privilege against self-incrimination is not applicable to the States. See <i>Cohen</i> v. <i>Hurley,</i> <span class="citation" data-id="9422196"><a href="/opinion/106223/cohen-v-hurley/" aria-description="Citation for case: Cohen v. Hurley">366 U. S. 117</a></span>.</p>
<p>I regret that I find so unwise in principle and so inexpedient in policy a decision motivated by the high purpose of increasing respect for Constitutional rights. But in the last analysis I think this Court can increase respect for the Constitution only if it rigidly respects the limitations which the Constitution places upon it, and respects as well the principles inherent in its own processes. In the present case I think we exceed both, and that our voice becomes only a voice of power, not of reason.</p>
<h2>NOTES</h2>
<p>[1]  The statute provides in pertinent part that
</p>
<p>"No person shall knowingly . . . have in his possession or under his control an obscene, lewd, or lascivious book [or] . . . picture . . . .</p>
<p>"Whoever violates this section shall be fined not less than two hundred nor more than two thousand dollars or imprisoned not less than one nor more than seven years, or both."</p>
<p>[2]  A police officer testified that "we did pry the screen door to gain entrance"; the attorney on the scene testified that a policeman "tried . . . to kick in the door" and then "broke the glass in the door and somebody reached in and opened the door and let them in"; the appellant testified that "The back door was broken."</p>
<p>[3]  Other issues have been raised on this appeal but, in the view we have taken of the case, they need not be decided. Although appellant chose to urge what may have appeared to be the surer ground for favorable disposition and did not insist that <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> be overruled, the <i>amicus curiae,</i> who was also permitted to participate in the oral argument, did urge the Court to overrule <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>.</i></p>
<p>[4]  "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</p>
<p>[5]  The close connection between the concepts later embodied in these two Amendments had been noted at least as early as 1765 by Lord Camden, on whose opinion in <i>Entick</i> v. <i>Carrington,</i> 19 Howell's State Trials 1029, the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> court drew heavily. Lord Camden had noted, at 1073:
</p>
<p>"It is very certain, that the law obligeth no man to accuse himself; because the necessary means of compelling self-accusation, falling upon the innocent as well as the guilty, would be both cruel and unjust; and it should seem, that search for evidence is disallowed upon the same principle. There too the innocent would be confounded with the guilty."</p>
<p>[6]  See, however,<i>National Safe Deposit Co.</i> v. <i>Stead,</i> <span class="citation" data-id="98058"><a href="/opinion/98058/national-safe-deposit-co-v-stead/" aria-description="Citation for case: National Safe Deposit Co. v. Stead">232 U. S. 58</a></span> (1914), and <i>Adams</i> v. <i>New York,</i> <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U. S. 585</a></span> (1904).</p>
<p>[7]  Less than half of the States have any criminal provisions relating directly to unreasonable searches and seizures. The punitive sanctions of the 23 States attempting to control such invasions of the right of privacy may be classified as follows:
</p>
<p><i>Criminal Liability of Affiant for Malicious Procurement of Search Warrant.</i>Ala. Code, 1958, Tit. 15, § 99; Alaska Comp. Laws Ann., 1949, § 66-7-15; Ariz. Rev. Stat. Ann., 1956, § 13-1454; <span class="citation no-link">Cal. Pen. Code § 170</span>; Fla. Stat., 1959, § 933.16; Ga. Code Ann., 1953, § 27-301; Idaho Code Ann., 1948, § 18-709; Iowa Code Ann., 1950, § 751.38; Minn. Stat. Ann., 1947, § 613.54; Mont. Rev. Codes Ann., 1947, § 94-35-122; <span class="citation no-link">Nev. Rev. Stat. §§ 199.130</span>, 199.140; N. J. Stat. Ann., 1940, § 33:1-64; N. Y. Pen. Law § 1786, N. Y. Code Crim. Proc. § 811; N. C. Gen. Stat., 1953, § 15-27 (applies to "officers" only); N. D. Century Code Ann., 1960, §§ 12-17-08, 29-29-18; Okla. Stat., 1951, Tit. 21, § 585, Tit. 22, § 1239; Ore. Rev. Stat. § 141.990; S. D. Code, 1939 (Supp. 1960), § 34.9904; Utah Code Ann., 1953, § 77-54-21.</p>
<p><i>Criminal Liability of Magistrate Issuing Warrant Without Supporting Affidavit.</i>N. C. Gen. Stat., 1953, § 15-27; Va. Code Ann., 1960 Replacement Volume, § 19.1-89.</p>
<p><i>Criminal Liability of Officer Willfully Exceeding Authority of Search Warrant.</i>Fla. Stat. Ann., 1944, § 933.17; Iowa Code Ann., 1950, § 751.39; Minn. Stat. Ann., 1947, § 613.54; <span class="citation no-link">Nev. Rev. Stat. § 199.450</span>; N. Y. Pen. Law § 1847, N. Y. Code Crim. Proc. § 812; N. D. Century Code Ann., 1960, §§ 12-17-07, 29-29-19; Okla. Stat., 1951, Tit. 21, § 536, Tit. 22, § 1240; S. D. Code, 1939 (Supp. 1960), § 34.9905; Tenn. Code Ann., 1955, § 40-510; Utah Code Ann., 1953, § 77-54-22.</p>
<p><i>Criminal Liability of Officer for Search with Invalid Warrant or no Warrant.</i>Idaho Code Ann., 1948, § 18-703; Minn. Stat. Ann., 1947, §§ 613.53, 621.17; Mo. Ann. Stat., 1953, § 558.190; Mont. Rev. Codes Ann., 1947, § 94-3506; N. J. Stat. Ann., 1940, § 33:1-65; N. Y. Pen. Law § 1846; N. D. Century Code Ann., 1960, § 12-17-06; Okla. Stat. Ann., 1958, Tit. 21, § 535; Utah Code Ann., 1953, § 76-28-52; Va. Code Ann., 1960 Replacement Volume, § 19.1-88; <span class="citation no-link">Wash. Rev. Code §§ 10.79.040</span>, 10.79.045.</p>
<p>[8]  But compare <i>Waley</i> v. <i>Johnston,</i> <span class="citation" data-id="103660"><a href="/opinion/103660/waley-v-johnston/#104" aria-description="Citation for case: Waley v. Johnston">316 U. S. 101, 104</a></span>, and <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#236" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227, 236</a></span>, with <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, and <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>.</p>
<p>[9]  As is always the case, however, state procedural requirements governing assertion and pursuance of direct and collateral constitutional challenges to criminal prosecutions must be respected. We note, moreover, that the class of state convictions possibly affected by this decision is of relatively narrow compass when compared with <i>Burns</i> v. <i>Ohio,</i> <span class="citation" data-id="9421835"><a href="/opinion/105911/burns-v-ohio/" aria-description="Citation for case: Burns v. Ohio">360 U. S. 252</a></span>, <i>Griffin</i> v. <i>Illinois,</i> <span class="citation" data-id="9421263"><a href="/opinion/105382/griffin-v-illinois/" aria-description="Citation for case: Griffin v. Illinois">351 U. S. 12</a></span>, and <i>Herman</i> v. <i>Claudy,</i> <span class="citation" data-id="105336"><a href="/opinion/105336/pennsylvania-ex-rel-herman-v-claudy/" aria-description="Citation for case: Pennsylvania Ex Rel. Herman v. Claudy">350 U. S. 116</a></span>. In those cases the same contention was urged and later proved unfounded. In any case, further delay in reaching the present result could have no effect other than to compound the difficulties.</p>
<p>[10]  See the remarks of Mr. Hoover, Director of the Federal Bureau of Investigation, FBI Law Enforcement Bulletin, September, 1952, pp. 1-2, quoted in <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#218" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 218-219, note 8</a></span>.</p>
<p>[11]  Cf. <i>Marcus</i> v. <i>Search Warrant, post,</i> p. 717.</p>
<p>[1]  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, decided in 1914.</p>
<p>[2]  <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#33" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 33</a></span>.</p>
<p>[3]  <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#39" aria-description="Citation for case: Wolf v. Colorado"><i>Id.,</i> at 39-40</a></span>.</p>
<p>[4]  The interrelationship between the Fourth and the Fifth Amendments in this area does not, of course, justify a narrowing in the interpretation of either of these Amendments with respect to areas in which they operate separately. See <i>Feldman</i> v. <i>United States,</i> <span class="citation" data-id="9419517"><a href="/opinion/104006/feldman-v-united-states/#502" aria-description="Citation for case: Feldman v. United States">322 U. S. 487, 502-503</a></span> (dissenting opinion); <i>Frank</i> v. <i>Maryland,</i> <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#374" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360, 374-384</a></span> (dissenting opinion).</p>
<p>[5]  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>.</p>
<p>[6]  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#633" aria-description="Citation for case: Boyd v. United States"><i>Id.,</i> at 633</a></span>.</p>
<p>[7]  338 U. S., at 47-48.</p>
<p>[8]  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U. S., at 635</a></span>. As the Court points out, Mr. Justice Bradley's approach to interpretation of the Bill of Rights stemmed directly from the spirit in which that great charter of liberty was offered for adoption on the floor of the House of Representatives by its framer, James Madison: "If they [the first ten Amendments] are incorporated into the Constitution, independent tribunals of justice will consider themselves in a peculiar manner the guardians of those rights; they will be an impenetrable bulwark against every assumption of power in the Legislative or Executive; they will be naturally led to resist every encroachment upon rights expressly stipulated for in the Constitution by the declaration of rights." I Annals of Congress 439 (1789).</p>
<p>[9]  <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span>.</p>
<p>[10]  <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#173" aria-description="Citation for case: Rochin v. California"><i>Id.,</i> at 173</a></span>.</p>
<p>[11]  <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#172" aria-description="Citation for case: Rochin v. California"><i>Id.,</i> at 172</a></span>.</p>
<p>[12]  <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#172" aria-description="Citation for case: Rochin v. California"><i>Id.,</i> at 172, 173</a></span>.</p>
<p>[13]  <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#174" aria-description="Citation for case: Rochin v. California"><i>Id.,</i> at 174-177</a></span>.</p>
<p>[14]  For the concurring opinion of MR. JUSTICE DOUGLAS see <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#177" aria-description="Citation for case: Rochin v. California"><i>id.,</i> at 177-179</a></span>.</p>
<p>[15]  <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">347 U. S. 128</a></span>.</p>
<p>[16]  <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#138" aria-description="Citation for case: Irvine v. California"><i>Id.,</i> at 138</a></span>.</p>
<p>[17]  See also <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 66-68</a></span> (dissenting opinion).</p>
<p>[1]  This "confidential source" told the police, in the same breath, that "there was a large amount of policy paraphernalia being hidden in the home."</p>
<p>[2]  The purported warrant has disappeared from the case. The State made no attempt to prove its existence, issuance or contents, either at the trial or on the hearing of a preliminary motion to suppress. The Supreme Court of Ohio said: "There is, in the record, considerable doubt as to whether there ever was <i>any</i> warrant for the search of defendant's home. . . . Admittedly . . . there was no warrant authorizing a search . . . for any `lewd, or lascivious book . . . print, [or] picture.' " <span class="citation no-link">170 Ohio St. 427</span>, 430, <span class="citation no-link">166 N. E. 2d 387</span>, 389. (Emphasis added.)</p>
<p>[3]  Ohio Rev. Code, § 2905.34: "No person shall knowingly . . . have in his possession or under his control an obscene, lewd, or lascivious book, magazine, pamphlet, paper, writing, advertisement, circular, print, picture . . . or drawing . . . of an indecent or immoral nature. . . . Whoever violates this section shall be fined not less than two hundred nor more than two thousand dollars or imprisoned not less than one nor more than seven years, or both."</p>
<p>[4]  "The notice of appeal . . . shall set forth the questions presented by the appeal . . . . Only the questions set forth in the notice of appeal or fairly comprised therein will be considered by the court." Rule 10 (2) (c), Rules of the Supreme Court of the United States.</p>
<p>[5]  "Did the conduct of the police in procuring the books, papers and pictures placed in evidence by the Prosecution violate Amendment IV, Amendment V, and Amendment XIV Section 1 of the United States Constitution . . . ?"</p>
<p>[1]  The material parts of that law are quoted in note 1 of the Court's opinion. <i>Ante,</i> p. 643.</p>
<p>[2]  In its note 3, <i>ante,</i> p. 646, the Court, it seems to me, has turned upside down the relative importance of appellant's reliance on the various points made by him on this appeal.</p>
<p>[3]  See <span class="citation no-link">170 Ohio St. 427</span>, <span class="citation no-link">166 N. E. 2d 387</span>. Because of the unusual provision of the Ohio Constitution requiring "the concurrence of at least all but one of the judges" of the Ohio Supreme Court before a state law is held unconstitutional (except in the case of affirmance of a holding of unconstitutionality by the Ohio Court of Appeals), Ohio Const., Art. IV, § 2, the State Supreme Court was compelled to uphold the constitutionality of § 2905.34, despite the fact that four of its seven judges thought the statute offensive to the Fourteenth Amendment.</p>
<p>[4]  Respecting the "substantiality" of the federal questions tendered by this appeal, appellant's Jurisdictional Statement contained the following:
</p>
<p>"The Federal questions raised by this appeal are substantial for the following reasons:</p>
<p>"The Ohio Statute under which the defendant was convicted violates one's sacred right to own and hold property, which has been held inviolate by the Federal Constitution. The right of the individual `to read, to believe or disbelieve, and to think without governmental supervision is one of our basic liberties, but to dictate to the mature adult what books he may have in his own private library seems to be a clear infringement of the constitutional rights of the individual' (Justice Herbert's dissenting Opinion, Appendix `A'). Many convictions have followed that of the defendant in the State Courts of Ohio based upon this very same statute. Unless this Honorable Court hears this matter and determines once and for all that the Statute is unconstitutional as defendant contends, there will be many such appeals. When Sections 2905.34, 2905.37 and 3767.01 of the Ohio Revised Code [the latter two Sections providing exceptions to the coverage of § 2905.34 and related provisions of Ohio's obscenity statutes] are read together, . . . they obviously contravene the Federal and State constitutional provisions; by being convicted under the Statute involved herein, and in the manner in which she was convicted, Defendant-Appellant has been denied due process of law; a sentence of from one (1) to seven (7) years in a penal institution for alleged violation of this unconstitutional section of the Ohio Revised Code deprives the defendant of her right to liberty and the pursuit of happiness, contrary to the Federal and State constitutional provisions, for circumstances which she herself did not put in motion, and is a cruel and unusual punishment 

[...TRUNCATED 6758 of 126758 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/Marbury v. Madison.md  (`case`, 5 assertions)

### content_page

```
---
title: "Marbury v. Madison"
type: case
citation: "5 U.S. 137 (1803)"
parallel_cite: "2 L. Ed. 60; 1 Cranch 137"
neutral_cite: 1803 U.S. LEXIS 352
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1803
date_decided: 1803-02-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1803-02-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Marbury v. Madison
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/84759/marbury-v-madison/"
  cluster_id: 84759
  opinion_id: 84759
  identity_checked: false
homes:
  - page: "[[The Federal Court System]]"
    role: "Key — Anchor"
related: []
aliases: []
tags: ["case", "constitutional-law", "judicial-review", "federal-courts", "separation-of-powers"]
holding: "Establishes judicial review: it is the province and duty of the judiciary to say what the law is, and a law repugnant to the…"
lake:
  record_id: Marbury v. Madison
  status: under_review
  projected_at: 2026-07-09
---

# Marbury v. Madison

*5 U.S. (1 Cranch) 137 (1803)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In the final days of the Adams administration, William Marbury was appointed a justice of the peace, but his commission was not delivered before Jefferson took office, and the new Secretary of State, Madison, withheld it. Marbury sued directly in the Supreme Court for a writ of mandamus to compel delivery, invoking a power the Judiciary Act of 1789 purported to grant the Court.

## Issue
Whether the Supreme Court could issue the writ — and, underlying that, whether a court may decline to give effect to an Act of Congress that conflicts with the Constitution.

## Rule
The judiciary determines what the law is and must disregard a statute that conflicts with the Constitution. "It is emphatically the province and duty of the judicial department to say what the law is." — 5 U.S. (1 Cranch) at 177. ^pin-177

And because the Constitution is supreme, "an act of the legislature, repugnant to the constitution, is void." — [*Id.*](https://www.courtlistener.com/opinion/84759/marbury-v-madison/#:~:text=an%20act%20of%20the%20legislature%2C%20repugnant%20to%20the%20constitution%2C%20is%20void.) ^pin-177a

## Application
Marbury was entitled to his commission and mandamus was a proper remedy, but the provision of the Judiciary Act of 1789 that purported to authorize the Supreme Court to issue mandamus in an original action enlarged the Court's original jurisdiction beyond what Article III allows. Confronting that conflict between the statute and the Constitution, the Court applied the principle that it must follow the Constitution and treat the repugnant statutory grant as void; it therefore lacked jurisdiction to issue the writ.

## Conclusion
The Court denied the writ for want of jurisdiction, holding the jurisdiction-expanding statute unconstitutional and establishing the power of judicial review.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Marbury* is the foundational source of judicial review and remains undisturbed; it anchors the structure of the federal court system and the courts' authority to measure statutes against the Constitution.

## Appears on
- [[The Federal Court System]] — *Key — Anchor*

## Sources
- *Marbury v. Madison*, 5 U.S. (1 Cranch) 137 (1803) — https://www.courtlistener.com/opinion/84759/marbury-v-madison/ — pinpoint: 177.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "db997f27d4d4fb60", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "5 U.S. 137 (1803)", "court": "U.S. Supreme Court", "neutral_cite": "1803 U.S. LEXIS 352", "official_citation_present": true, "parallel_cite": "2 L. Ed. 60; 1 Cranch 137", "title": "Marbury v. Madison", "year": "1803"}}
{"assertion_id": "6717dcc2b255fe26", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Establishes judicial review: it is the province and duty of the judiciary to say what the law is, and a law repugnant to the…", "title": "Marbury v. Madison"}}
{"assertion_id": "83b65bc4c0815a04", "dimension": "support", "kind": "home_role", "locator": {"home": "The Federal Court System"}, "payload": {"home": "The Federal Court System", "role": "Key — Anchor", "title": "Marbury v. Madison"}}
{"assertion_id": "a3235b0044e3ad37", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Marbury v. Madison"}}
{"assertion_id": "e82c57c1676ad94f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1803-02-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Marbury v. Madison", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Marbury v. Madison", "varies_by_point": "false"}}
```

### lake record — Marbury v. Madison

```json
{
  "schema_version": "s2.v1",
  "record_id": "Marbury v. Madison",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Marbury v. Madison",
    "case_name_short": "Marbury",
    "case_name_full": "WILLIAM MARBURY v. JAMES MADISON, Secretary of State of the United States",
    "input_case_name": "Marbury v. Madison",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1803-02-24",
    "year": 1803,
    "docket": null,
    "cluster_id": 84759,
    "lead_opinion_id": 84759,
    "sibling_ids": [
      84759
    ],
    "absolute_url": "/opinion/84759/marbury-v-madison/",
    "identity_method": "pending",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "5 U.S. 137",
      "volume": "5",
      "reporter": "U.S.",
      "page": "137",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "2 L. Ed. 60",
        "volume": "2",
        "reporter": "L. Ed.",
        "page": "60",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1 Cranch 137",
        "volume": "1",
        "reporter": "Cranch",
        "page": "137",
        "type": 5,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1803 U.S. LEXIS 352",
        "volume": "1803",
        "reporter": "U.S. LEXIS",
        "page": "352",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "5 U.S. 137",
        "volume": "5",
        "reporter": "U.S.",
        "page": "137",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2 L. Ed. 60",
        "volume": "2",
        "reporter": "L. Ed.",
        "page": "60",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1 Cranch 137",
        "volume": "1",
        "reporter": "Cranch",
        "page": "137",
        "type": 5,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1803 U.S. LEXIS 352",
        "volume": "1803",
        "reporter": "U.S. LEXIS",
        "page": "352",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "5 U.S. 137",
    "official_selection": {
      "court_class": "scotus",
      "selected": "5 U.S. 137",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-177",
      "page": null,
      "quote": "--- # Marbury v. Madison *5 U.S. (1 Cranch) 137 (1803)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In the final days of the Adams administration, William Marbury was appointed a justice of the peace, but his commission was not delivered before Jefferson took office, and the new Secretary of State, Madison, withheld it. Marbury sued directly in the Supreme Court for a writ of mandamus to compel delivery, invoking a power the Judiciary Act of 1789 purported to grant the Court. ## Issue Whether the Supreme Court could issue the writ \u2014 and, underlying that, whether a court may decline to give effect to an Act of Congress that conflicts with the Constitution. ## Rule The judiciary determines what the law is and must disregard a statute that conflicts with the Constitution.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-177a",
      "page": null,
      "quote": "an act of the legislature, repugnant to the constitution, is void.",
      "star_marker": "177",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 52598,
      "fragment": "#:~:text=an%20act%20of%20the%20legislature%2C%20repugnant%20to%20the%20constitution%2C%20is%20void.",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1803-02-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Marbury v. Madison",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Savage v. N.C. Dep't of Transp.",
          "cluster_id": 10658754,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Douglas Bienvenu v. 1 and 2 87184 C/W John Doe v. 1 and 2 87515",
          "cluster_id": 9541526,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In the Matter of the Welfare of the Children of: L. K. and A. S., Parents",
          "cluster_id": 10707173,
          "cite": [
            "9 N.W.3d 174"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane1_negative"
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
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Booker",
          "cluster_id": 137739,
          "cite": [
            "160 L. Ed. 2d 621",
            "125 S. Ct. 738",
            "543 U.S. 220",
            "2005 U.S. LEXIS 628"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
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
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williams v. Taylor",
          "cluster_id": 145122,
          "cite": [
            "146 L. Ed. 2d 389",
            "120 S. Ct. 1495",
            "529 U.S. 362",
            "2000 U.S. LEXIS 2837"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
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
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas Ass'n of Business v. Texas Air Control Board",
          "cluster_id": 1515115,
          "cite": [
            "852 S.W.2d 440",
            "1993 WL 54269"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bell v. Hood",
          "cluster_id": 104272,
          "cite": [
            "327 U.S. 678",
            "66 S. Ct. 773",
            "90 L. Ed. 939",
            "1946 U.S. LEXIS 2569",
            "13 A.L.R. 2d 383"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Martinez v. Ryan",
          "cluster_id": 625711,
          "cite": [
            "182 L. Ed. 2d 272",
            "132 S. Ct. 1309",
            "566 U.S. 1",
            "2012 U.S. LEXIS 2317"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
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
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Seminole Tribe of Florida v. Florida",
          "cluster_id": 118011,
          "cite": [
            "134 L. Ed. 2d 252",
            "116 S. Ct. 1114",
            "517 U.S. 44",
            "1996 U.S. LEXIS 2165",
            "96 Cal. Daily Op. Serv. 2125",
            "96 Daily Journal DAR 3499",
            "64 U.S.L.W. 4167",
            "9 Fla. L. Weekly Fed. S 484",
            "34 Collier Bankr. Cas. 2d 1199",
            "42 ERC (BNA) 1289",
            "67 Empl. Prac. Dec. (CCH) 43,952"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "TransUnion LLC v. Ramirez",
          "cluster_id": 4894912,
          "cite": [
            "594 U.S. 413",
            "210 L. Ed. 2d 568",
            "141 S. Ct. 2190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Swain v. Alabama",
          "cluster_id": 106997,
          "cite": [
            "13 L. Ed. 2d 759",
            "85 S. Ct. 824",
            "380 U.S. 202",
            "1965 U.S. LEXIS 1668"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Heller",
          "cluster_id": 145777,
          "cite": [
            "171 L. Ed. 2d 637",
            "128 S. Ct. 2783",
            "554 U.S. 570",
            "2008 U.S. LEXIS 5268"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
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
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lopez",
          "cluster_id": 117927,
          "cite": [
            "131 L. Ed. 2d 626",
            "115 S. Ct. 1624",
            "514 U.S. 549",
            "1995 U.S. LEXIS 3039"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "DaimlerChrysler Corp. v. Cuno",
          "cluster_id": 145658,
          "cite": [
            "164 L. Ed. 2d 589",
            "126 S. Ct. 1854",
            "547 U.S. 332",
            "2006 U.S. LEXIS 3956"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
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
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
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
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clinton v. Jones",
          "cluster_id": 118115,
          "cite": [
            "137 L. Ed. 2d 945",
            "117 S. Ct. 1636",
            "520 U.S. 681",
            "1997 U.S. LEXIS 3254"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Olmstead v. United States",
          "cluster_id": 101320,
          "cite": [
            "277 U.S. 438",
            "48 S. Ct. 564",
            "72 L. Ed. 944",
            "1928 U.S. LEXIS 694",
            "66 A.L.R. 376"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Watson",
          "cluster_id": 109352,
          "cite": [
            "46 L. Ed. 2d 598",
            "96 S. Ct. 820",
            "423 U.S. 411",
            "1976 U.S. LEXIS 121"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McDonald v. City of Chicago",
          "cluster_id": 149702,
          "cite": [
            "177 L. Ed. 2d 894",
            "130 S. Ct. 3020",
            "561 U.S. 742",
            "2010 U.S. LEXIS 5523",
            "22 Fla. L. Weekly Fed. S 619",
            "78 U.S.L.W. 4844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Boerne v. Flores",
          "cluster_id": 118140,
          "cite": [
            "138 L. Ed. 2d 624",
            "117 S. Ct. 2157",
            "521 U.S. 507",
            "1997 U.S. LEXIS 4035",
            "65 U.S.L.W. 4612",
            "97 Daily Journal DAR 7973",
            "1997 Colo. J. C.A.R. 1329",
            "97 Cal. Daily Op. Serv. 4904",
            "11 Fla. L. Weekly Fed. S 140",
            "70 Empl. Prac. Dec. (CCH) 44,785",
            "74 Fair Empl. Prac. Cas. (BNA) 62"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Citizens United v. Federal Election Commission",
          "cluster_id": 1741,
          "cite": [
            "175 L. Ed. 2d 753",
            "130 S. Ct. 876",
            "558 U.S. 310",
            "2010 U.S. LEXIS 766",
            "22 Fla. L. Weekly Fed. S 73",
            "78 U.S.L.W. 4078",
            "187 L.R.R.M. (BNA) 2961",
            "159 Lab. Cas. (CCH) 10,166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Raines v. Byrd",
          "cluster_id": 118146,
          "cite": [
            "138 L. Ed. 2d 849",
            "117 S. Ct. 2312",
            "521 U.S. 811",
            "1997 U.S. LEXIS 4040"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "IN RE INITIATIVE PETITION NO. 448, STATE QUESTION NO. 836; THE OKLAHOMA REPUBLICAN PARTY v. SETTER",
          "cluster_id": 10676729,
          "cite": [
            "2025 OK 56"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane3_recency"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(84759) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzEyMDE2MDAwMDAwJnM9OTQ4OTk5OCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%2884759%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(84759)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDE4JnM9MTE3OTE2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%2884759%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(84759)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzE5NzkyMDAwMDAwJnM9OTk5OTk5MyZ0PW8mZD0yMDI2LTA3LTA2JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%2884759%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 2,
        "triage_snippet_classified": 198
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(84759)",
    "indexed_citing_opinions": 3102,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 84759,
        "count": 3102,
        "count_source": "search"
      }
    ],
    "citation_count": 6020,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/marbury-v-madison.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0NjkzOSZzPTEwNjQ1Mjk5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%2884759%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LRU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T11:42:31Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:42:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:42:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:46:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:42:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Marbury v. Madison

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<p id="b173-13">
<em>
   Opinion of
  </em>
</p>
<author id="Abzf">
<em>
   the court.
  </em>
</author>
<p id="b173-14">
  At the last term on the affidavits then read and filed with the clerk, a rule was granted in this case, requiring the secretary of state to shew cause why a mandamus
  <span citation-index="1" class="star-pagination" label="154"> 
   *154
   </span>
  should not issue, directing him to deliver to William Marbury his commission as a justice of the peace for the county of Washington in the district of Columbia.
 </p>
<p id="b174-5">
  No cause has been shewn, and the present motion is for a mandamus. The peculiar delicacy of this case, the novelty of some of its circumstances, and the real difficulty attending the points which occur in it, require a complete exposition of the principles, on which the opinion to be given by the court, is founded.
 </p>
<p id="b174-6">
  These principles have been, on the side of the applicant, very ably argued at the bar. In rendering the opinion of the court, there will be some departure in form, though not in substance, from the points stated in that argument.
 </p>
<p id="b174-7">
  In the order in which the court has viewed this subject, the following questions have been considered and decided.
 </p>
<p id="b174-8">
  1st. Has the applicant a right to the commission he demands ?
 </p>
<p id="b174-9">
  2dly. If he has a right, and that right has been violated, do the laws of his country afford him a remedy?
 </p>
<p id="b174-10">
  3dly. If they do afford him a remedy, is it a
  <em>
   mandamus
  </em>
  issuing from this court?
 </p>
<p id="b174-11">
  The first object of enquiry is,
 </p>
<p id="b174-12">
  1st. Has the applicant a right to the commission he demands?
 </p>
<p id="b174-13">
  His right originates in an act of congress passed in February 1801, concerning the district of Columbia.
 </p>
<p id="b174-14">
  After dividing the district into two counties, the 11th section of this law, enacts, “ that there shall be appointed in and for each of the said counties, such number of discreet persons to be justices of the peace as the president of the United States shall, from time to time, think expedient, to continue in office for five years.
 </p>
<p id="b175-2">
<span citation-index="1" class="star-pagination" label="155"> 
   *155
   </span>
  It appears, from the affidavits, that in compliance with this law, a commission for William Marbury as justice of peace for the country of Washington, was signed by John Adams, then president of the United States; after which the seal of the United States was affixed to it; but the commission has never reached the person for whom it was made out.
 </p>
<p id="b175-10">
  In order to determine whether he is entitled to this commission, it becomes necessary to enquire whether he has been appointed to the office. For if he has been appointed, the law continues him in office for five years, and he is entitled to the possession of those evidences of office, which, being completed, became his property.
 </p>
<p id="b175-11">
  The 2d section of the 2d article of the constitution, declares, that, “ the president shall nominate, and, by “ and with the advice and consent of the senate, shall “ appoint ambassadors, other public ministers and consuls, “ and all other officers of the United States, whose ap- “ pointments are not otherwise provided for.”
 </p>
<p id="b175-13">
  The third section declares, that “ he shall commission “ all the officers of the United States.”
 </p>
<p id="b175-14">
  An act of congress directs the secretary of state to keep the seal of the United States, “ to make out and record, and affix the said seal to all civil commissions to officers of the United States, to be appointed by the President, by and with the
  <em>
   consent
  </em>
  of the senate, or by the President alone; provided that the said seal shall not be affixed to any commission before the same shall have been signed by the President of the United States.”
 </p>
<p id="b175-15">
  These are the clauses of the constitution and laws of the United States, which affect this part of the case. They seem to contemplate three distinct operations:
 </p>
<p id="b175-17">
  1st, The nomination. This is the sole act of the President, and is completely voluntary.
 </p>
<p id="b175-18">
  2d. The appointment. This is also the act of the President, and is also a voluntary act, though it can only be performed by and with the advice and consent of the senate.
 </p>
<p id="b176-2">
<span citation-index="1" class="star-pagination" label="156"> 
   *156
   </span>
  3d. The commission. To grant a commission to a person appointed, might perhaps be deemed a duty enjoined by the constitution. " He shall," says that instrument, " commission all the officers of the United States."
 </p>
<p id="b176-3">
  The acts of appointing to office, and commissioning the person appointed, can scarcely be considered as one and the same; since the power to perform them is given in two separate and distinct sections of the constitution. The distinction between the appointment and the commission will be rendered more apparent, by adverting to that provision in the second section of the second article of the constitution, which authorizes congress " to vest, by law, the appointment of such inferior officers, as they think proper, in the President alone, in the courts of law, or in the heads of departments ;" thus contemplating cases where the law may direct the President to commission an officer appointed by the courts, or by the heads of departments. In such a case, to issue a commission would be apparently a duty distinct from the appointment, the performance of which, perhaps, could not legally be refused.
 </p>
<p id="b176-4">
  Although that clause of the constitution which requires the President to commission all the officers of the United States, may never have been applied to officers appointed otherwise than by himself, yet it would be difficult to deny the legislative power to apply it to such cases. Of consequence the constitutional distinction between the appointment to an office and the commission of an officer, who has been appointed, remains the same as if in practice the President had commissioned officers appointed by an authority other than his own.
 </p>
<p id="b176-5">
  It follows too, from the existence of this distinction, that, if an appointment was to be evidenced by any public act, other than the commission, the performance of such public act would create the officer; and if he was not removeable at the will of the President, would either give him a right to his commission, or enable him to perform the duties without it.
 </p>
<p id="b176-6">
  These observations are premised solely for the purpose of rendering more intelligible those which apply more directly to the particular case under consideration.
 </p>
<p id="b177-3">
<span citation-index="1" class="star-pagination" label="157"> 
   *157
   </span>
  This is an appointment made by the President, by and with the advice and consent of the senate, and is evidenced by no act but the commission itself. In such a case therefore the commission and the appointment seem inseparable; it being almost impossible to shew an appointment otherwise than by proving the existence of a commission; still the commission is not necessarily the appointment ; though conclusive evidence of it.
 </p>
<p id="b177-11">
  But at what stage does it amount to this conclusive evidence ?
 </p>
<p id="b177-12">
  The answer to this question seems an obvious one. The appointment being the sole act of the President, must be completely evidenced, when it is shewn that he has done every thing to be performed by him.
 </p>
<p id="b177-14">
  Should the commission, instead of being evidence of an appointment, even be considered as constituting the appointment itself; still it would be made when the last act to be done by the President was performed, or, at furthest, when the commission was complete.
 </p>
<p id="b177-15">
  The last act to be done by the President, is the signature of the commission. He has then acted on the advice and consent of the senate to his own nomination. The time for deliberation has then passed. He has decided. His judgment, on the advice and consent of the senate concurring with his nomination, has been made, and the officer is appointed. This appointment is evidenced by an open, unequivocal act; and being the last act required from the person making it, necessarily excludes the idea of its being, so far as respects the appointment, an inchoate and incomplete transaction.
 </p>
<p id="b177-17">
  Some point of time must be taken when the power of the executive over an officer, not removeable at his will, must cease. That point of time must be when the constitutional power of appointment has been exercised. And this power has been exercised when the last act, required from the person possessing the power, has been performed. This last act is the signature of the commission. This idea seems to have prevailed with the legislature, when the act passed, converting the department
  <span citation-index="1" class="star-pagination" label="158"> 
   *158
   </span>
  of foreign affairs into the department of state. By that act it is enacted, that the secretary of state shall keep that seal of the United States, and shall make out and re- " cord, and shall affix the said seal to all civil commissions “ to officers of the United States, to be appointed by the “ President:" "Provided that the said seal shall not be af- “ fixed to any commission, before the same shall have been “ signed by the President of the United States; nor to “ any other instrument or act, without the special war- “ rant of the President therefor.”
 </p>
<p id="b178-13">
  The signature is a warrant for affixing the great seal to the commission; and the great seal is only to be affixed to an instrument which is complete. It attests, by an act supposed to be of public notoriety, the verity of the Presidential signature.
 </p>
<p id="b178-14">
  It is never to be affixed till the commission is signed, because the signature, which gives force and effect to the commission, is conclusive evidence that the appointment is made.
 </p>
<p id="b178-15">
  The commission being signed, the subsequent duty of the secretary of state is prescribed by law, and not to be guided by the will of the President. He is to affix the seal of the United States to the commission, and is to record it.
 </p>
<p id="b178-16">
  This is not a proceeding which may be varied, if the judgment of the executive shall suggest one more eligible; but is a precise course accurately marked out by law, and is to be strictly pursued. It is the duty of the secretary of state to conform to the law, and in this he is an officer of the United States, bound to obey the laws. He acts, in this respect, as has been very properly stated at the bar, under the authority of law, and not by the instructions of the President. It is a ministerial act which the law enjoins on 3 particular officer for a particular purpose.
 </p>
<p id="b178-17">
  If it should be supposed, that the solemnity of affixing the seal, is necessary not only to the validity of the commission, but even to the completion of an appointment, still when the seal is affixed the appointment is made, and
  <span citation-index="1" class="star-pagination" label="159"> 
   *159
   </span>
  the commission is valid. No other solemnity is required by law ; no other act is to be performed on the part of government. All that the executive can do to invest the person with his office, is done; and unless the appointment be then made, the executive cannot make one without the co-operation of others.
 </p>
<p id="b179-4">
  After searching anxiously for the principles on which a contrary opinion may be supported, none have been found which appear of sufficient force to maintain the opposite doctrine.
 </p>
<p id="b179-5">
  Such as the imagination of the court could suggest, have been very deliberately examined, and after allowing them all the weight which it appears possible to give them, they do not shake the opinion which has been formed.
 </p>
<p id="b179-6">
  In considering this question, it has been conjectured that the commission may have been assimilated to a deed, to the validity of which, delivery is essential.
 </p>
<p id="b179-7">
  This idea is founded on the supposition that the commission is not merely
  <em>
   evidence
  </em>
  of an appointment, but is itself the actual appointment; a supposition by no means unquestionable. But for the purpose of examining this objection fairly, let it be conceded, that the principle, claimed for its support, is established.
 </p>
<p id="b179-8">
  The appointment being, under the constitution, to be made by the President
  <em>
   personally,
  </em>
  the delivery of the deed of appointment, if necessary to its completion, must be made by the President also. It is not necessary that the livery should be made personally to the grantee of the office : It never is so made. The law would seem to contemplate that it should be made to the secretary of state, since it directs the secretary to affix the seal to the commission
  <em>
   after
  </em>
  it shall have been signed by the President. If then the act of livery be necessary to give validity to the commission, it has been delivered when executed and given to the secretary for the purpose of being sealed, recorded, and transmitted to the party.
 </p>
<p id="b179-9">
  But in all cases of letters patent, certain solemnities are required by law, which solemnities are the evidences
  <span citation-index="1" class="star-pagination" label="160"> 
   *160
   </span>
  of the validity of the instrument. A formal delivery to the person is not among them. In cases of commissions, the sign manual of the President, and the seal of the United States, are those solemnities. This objection therefore does not touch the case.
 </p>
<p id="b180-7">
  It has also occurred as possible, and barely possible, that the transmission of the commission, and the acceptance thereof, might be deemed necessary to complete the right of the plaintiff.
 </p>
<p id="b180-8">
  The transmission of the commission, is a practice directed by convenience, but not by law. It cannot therefore be necessary to constitute the appointment which must precede it, and which is the mere act of the President. If the executive required that every person appointed to an office, should himself take means to procure his commission, the appointment would not be the less valid on that account. The appointment is the sole act of the President; the transmission of the commission is the sole act of the officer to whom that duty is assigned, and may be accelerated or retarded by circumstances which can have no influence on the appointment. A commission is transmitted to a person already appointed ; not to a person to be appointed or not, as the letter enclosing the commission should happen to get into the post-office and reach him in safety, or to miscarry.
 </p>
<p id="b180-9">
  It may have some tendency to elucidate this point, to enquire, whether the possession of the original commission be indispensably necessary to authorize a person, appointed to any office, to perform the duties of that office. If it was necessary, then a loss of the commission would lose the office. Not only negligence, but accident or fraud, fire or theft, might deprive an individual of his office. In such a case, I presume it could not be doubted, but that a copy from the record of the office of the secretary of state, would be, to every intent and purpose, equal to the original. The act of congress has expressly made it so. To give that copy validity, it would not be necessary to prove that the original had been transmitted and afterwards lost. The copy would be complete evidence that the original had existed, and that the appointment had been made, but, not that the original had been transmitted. If indeed it should appear that
  <span citation-index="1" class="star-pagination" label="161"> 
   *161
   </span>
  the original had been mislaid in the office of state, that circumstance would not affect the operation of the copy. When all the requisites have been performed which authorize a recording officer to record any instrument whatever, and the order for that purpose has been given, the instrument is, in law, considered as recorded, although the manual labour of inserting it in a book kept for that purpose may not have been performed.
 </p>
<p id="b181-9">
  In the case of commissions, the law orders the secretary of state to record them. When therefore they are signed and sealed, the order for their being recorded is given; and whether inserted in the book or not, they are in law recorded.
 </p>
<p id="b181-10">
  A copy of this record is declared equal to the original, and the fees, to be paid by a person requiring a copy, are ascertained by law. Can a keeper of a public record, erase therefrom a commission which has been recorded ? Or can he refuse a copy thereof to a person demanding it on the terms prescribed by law ?
 </p>
<p id="b181-12">
  Such a copy would, equally with the original, authorize the justice of peace to proceed in the performance of his duty, because it would, equally with the original, attest his appointment.
 </p>
<p id="b181-13">
  If the transmission of a commission be not considered as necessary to give validity to an appointment; still less is its acceptance. The appointment is the sole act of the President; the acceptance is the sole act of the officer, and is, in plain common sense, posterior to the appointment. As he may resign, so may he refuse to accept : but neither the one, nor the other, is capable of rendering the appointment a non-entity.
 </p>
<p id="b181-14">
  That this is the understanding of the government, is apparent from the whole tenor of its conduct.
 </p>
<p id="b181-15">
  A commission bears date, and the salary of the officer commences from his appointment; not from the transmission or acceptance of his commission. When a person, appointed to any office, refuses to accept that office, the successor is nominated in the place of the person who
  <span citation-index="1" class="star-pagination" label="162"> 
   *162
   </span>
  has declined to accept, and not in the place of the person who had been previously in office, and had created the original vacancy.
 </p>
<p id="b182-6">
  It is therefore decidedly the opinion of the court, that when a commission has been signed by the President, the appointment is made ; and that the commission is complete, when the seal of the United States has been affixed to it by the secretary of state.
 </p>
<p id="b182-7">
  Where an officer is removeable at the will of the executive, the circumstance which completes his appointment is of no concern; because the act is at any time revocable; and the commission may be arrested, if still in the office. But when the officer is not removeable at the will of the executive, the appointment is not revocable, and cannot be annulled. It has conferred legal rights which cannot be resumed.
 </p>
<p id="b182-8">
  The discretion of the executive is to be exercised until the appointment has been made. But having once made the appointment, his power over the office is terminated in all cases, where, by law, the officer is not removeable by him. The right to the office is
  <em>
   then
  </em>
  in the person appointed, and he has the absolute, unconditional, power of accepting or rejecting it.
 </p>
<p id="b182-9">
  Mr. Marbury, then, since his commission was signed by the President, and sealed by the secretary of state, was appointed; and as the law creating the office, gave the officer a right to hold for five years, independent of the executive, the appointment was not revocable; but vested in the officer legal rights, which are protected by the laws of his country.
 </p>
<p id="b182-10">
  To withhold his commission, therefore, is an act deemed by the court not warranted by law, but violative of a vested legal right.
 </p>
<p id="b182-11">
  This brings
  <em>
   us
  </em>
  to the second enquiry
  <em>
   ;
  </em>
  which is,
 </p>
<p id="b182-12">
  2dly. If he has a right, and that right has been violated, do the laws of his country afford him a remedy?
 </p>
<p id="b183-2">
<span citation-index="1" class="star-pagination" label="163"> 
   *163
   </span>
  The very essence of civil liberty certainly consists in the right of every individual to claim the protection of the laws, whenever he receives an injury. One of the first duties of government is to afford that protection. In Great Britain the king himself is sued in the respectful form of a petition, and he never fails to comply with the judgment of his court.
 </p>
<p id="b183-3">
  In the 3d vol. of his commentaries, p. 23, Blackstone states two cases in which a remedy is afforded by mere operation of law.
 </p>
<p id="b183-4">
  “In all other cases,” he says, “it is a general and indis-“putable rule, that where there is a legal right, there is “ also a legal remedy by suit or action at law, whenever “that right is invaded.”
 </p>
<p id="b183-5">
  And afterwards, p. 109, of the same vol. he says, “I "am next to consider such injuries as are cognizable by “the courts of the common law. And herein I shall for "the present only remark, that all possible injuries what-"soever, that did not fall within the exclusive cognizance “of either the ecclesiastical, military, or maritime tribu-"nals, are for that very reason, within the cognizance "of the common law courts of justice; for it is a settled "and invariable principle in the laws of England, that "every right, when withheld, must have a remedy, and “every injury its proper redress.”
 </p>
<p id="b183-6">
  The government of the United States has been emphatically termed a government of laws, and not of men. It will certainly cease to deserve this high appellation, if the laws furnish no remedy for the violation of a vested legal right.
 </p>
<p id="b183-8">
  If this obloquy is to be cast on the jurisprudence of our country, it must arise from the peculiar character of the case.
 </p>
<p id="b183-9">
  It behoves us then to enquire whether there be in its composition any ingredient which shall exempt it from legal investigation, or exclude the injured party from legal redress. In pursuing this enquiry the first question which presents itself, is, whether this can be arranged
  <span citation-index="1" class="star-pagination" label="164"> 
   *164
   </span>
  with that class of cases which come under the description of
  <em>
   damnum absque
  </em>
  injuria—a loss without an injury.
 </p>
<p id="Ada">
  This description of cases never has been considered, and it is believed never can be considered, as comprehending offices of trust, of honor or of profit. The office of justice of peace in the district of Columbia is such an office; it is therefore worthy of the attention and guardianship of the laws. It has received that attention and guardianship. It has been created by special act of congress, and has been secured, so far as the laws can give security to the person appointed to fill it, for five years. It is not then on account of the worthlessness of the thing pursued, that the injured party can be alleged to be without remedy.
 </p>
<p id="b184-7">
  Is it in the nature of the transaction ? Is the act of delivering or withholding a commission to be considered as a mere political act, belonging to the executive department alone, for the performance of which, entire confidence is placed by our constitution in the supreme executive; and for any misconduct respecting which, the injured individual has no remedy.
 </p>
<p id="b184-8">
  That there may be such cases is not to be questioned; but that every act of duty, to be performed in any of the great departments of government, constitutes such a case, is not to be admitted.
 </p>
<p id="b184-9">
  By the act concerning invalids, passed in June, 1794, vol. 3. p. 112, the secretary at war is ordered to place on the pension list, all persons whose names are contained in a report previously made by him to congress. If he should refuse to do so, would the wounded veteran be without remedy ? Is it to be contended that where the law in precise terms, directs the performance of an act, in which an individual is interested, the law is incapable of securing obedience to its mandate ? Is it on account of the character of the person against whom the complaint is made ? Is it to be contended that the heads of departments are not amenable to the laws of their country ?
 </p>
<p id="b184-10">
  Whatever the practice on particular occasions may be, the theory of this principle will certainly never be main
  <span citation-index="1" class="star-pagination" label="165"> 
   *165
   </span>
  tained. No act of the legislature confers so extraordinary a privilege, nor can it derive countenance from the doctrines of the common law. After stating that personal injury from the king to a subject is presumed to be impossible, Blackstone, vol. 3. p. 255, says, “but injuries “to the rights of property can scarcely be committed by “the crown without the intervention of its officers; for "whom, the law, in matters of right, entertains no re-“spect or delicacy; but furnishes various methods of de-"tecting the errors and misconduct of those agents, by "whom the king has been deceived and induced to do a “temporary injustice.”
 </p>
<p id="b185-4">
  By the act passed in 1796, authorising the sale of the lands above the mouth of Kentucky river (vol. 3d. p. 2991 the purchaser, on paying his purchase money, becomes completely entitled to the property purchased; and on producing to the secretary of state, the receipt of the treasurer upon a certificate required by the law, the president of the United States is authorised to grant him a patent. It is further enacted that all patents shall be countersigned by the secretary of state, and recorded in his office. If the secretary of state should choose to withhold this patent; or the patent being lost, should refuse a copy of it; can it be imagined that the law furnishes to the injured person no remedy?
 </p>
<p id="b185-6">
  It is not believed that any person whatever would attempt to maintain such a proposition.
 </p>
<p id="b185-7">
  It follows then that the question, whether the legality of an act of the head of a department be examinable in a court of justice or not, must always depend on the nature of that act.
 </p>
<p id="b185-8">
  If some acts be examinable, and others not, there must be some rule of law to guide the court in the exercise of its jurisdiction.
 </p>
<p id="b185-9">
  In some instances there may be difficulty in applying the rule to particular cases; but there cannot, it is believed, be much difficulty in laying down the rule.
 </p>
<p id="b185-10">
  By the constitution of the United States, the President is invested with certain important political powers, in the
  <span citation-index="1" class="star-pagination" label="166"> 
   *166
   </span>
  exercise of which he is to use his own discretion, and is accountable only to his country in his political character, and to his own conscience. To aid him in the performance of these duties, he is authorized to appoint certain officers, who act by his authority and in conformity with his orders.
 </p>
<p id="b186-7">
  In such cases, their acts are his acts; and whatever opinion may be entertained of the manner in which executive discretion may be used, still there exists, and can exist, no power to control that discretion. The subjects are political. They respect the nation, not individual rights, and being entrusted to the executive, the decision of the executive is conclusive. The application of this remark will be perceived by adverting to the act of congress for establishing the department of foreign affairs. This officer, as his duties were prescribed by that act, is to conform precisely to the will of the President. He is the mere organ by whom that will is communicated. The acts of such an officer, as an officer, can never be examinable by the courts.
 </p>
<p id="b186-8">
  But when the legislature proceeds to impose on that officer other duties; when he is directed peremptorily to perform certain acts; when the rights of individuals are dependent on the performance of those acts; he is so far the officer of the law; is amenable to the laws for his conduct; and cannot at his discretion sport away the vested rights of others.
 </p>
<p id="b186-9">
  The conclusion from this reasoning is, that where the heads of departments are the political or confidential agents of the executive, merely to execute the will of the President, or rather to act in cases in which the executive possesses a constitutional or legal discretion, nothing can be more perfectly clear than that their acts are only politically examinable. But where a specific duty is assigned by law, and individual rights depend upon the performance of that duty, it seems equally clear that the individual who considers himself injured, has a right to resort to the laws of his country for a remedy.
 </p>
<p id="b186-10">
  If this be the rule, let us enquire how it applies to the case under the consideration of the court.
 </p>
<p id="b187-2">
<span citation-index="1" class="star-pagination" label="167"> 
   *167
   </span>
  The power of nominating to the senate, and the power of appointing the person nominated, are political powers, to be exercised by the President according to his own discretion. When he has made an appointment, he has exercised his whole power, and his discretion has been completely applied to the case. If, by law, the officer be removable at the will of the President, then a new appointment may be immediately made, and the rights of the officer are terminated. But as a fact which has existed cannot be made never to have existed, the appointment cannot be annihilated; and consequently if the officer is by law not removable at the will of the President; the rights he has acquired are protected by the law, and are not resumable by the President. They cannot be extinguished by executive authority, and he has the privilege of asserting them in like manner as if they had been derived from any other source.
 </p>
<p id="b187-5">
  The question whether a right has vested or not, is, in its nature, judicial, and must be tried by the judicial authority. It, for example, Mr. Marbury had taken the oaths of a magistrate, and proceeded to act as one; in consequence of which a suit had been instituted against him, in which his defence had depended on his being a magistrate; the validity of his appointment must have been determined by judicial authority.
 </p>
<p id="b187-6">
  So, if he conceives that, by virtue of his appointment, he has a legal right, either to the commission which has been made out for him, or to a copy of that commission, it is equally a question examinable in a court, and the decision of the court upon it must depend on the opinion entertained of his appointment.
 </p>
<p id="b187-7">
  That question has been discussed, and the opinion is, that the latest point of time which can be taken as that at which the appointment was complete, and evidenced, was when, after the signature of the president, the seal of the United States was affixed to the commission.
 </p>
<p id="b187-8">
  It is then the opinion of the court,
 </p>
<p id="b187-9">
  1st. That by signing the commission of Mr. Marbury, the president of the United States appointed him a justice
  <span citation-index="1" class="star-pagination" label="168"> 
   *168
   </span>
  of peace, for the county of Washington in the district of Columbia; and that the seal of the United States, affixed thereto by the secretary of state, is conclusive testimony of the verity of the signature, and of the completion of the appointment; and that the appointment conferred on him a legal right to the office for the space of five years.
 </p>
<p id="b188-5">
  2dly. That, having this legal title to the office, he has a consequent right to the commission; a refusal to deliver which, is a plain violation of that right, for which the laws of his country afford him a remedy.
 </p>
<p id="b188-6">
  It remains to be enquired whether,
 </p>
<p id="b188-7">
  3dly. He is entitled to the remedy for which he applies. This depends on,
 </p>
<p id="b188-8">
  1st. The nature of the writ applied for, and,
 </p>
<p id="b188-9">
  2dly. The power of this court.
 </p>
<p id="b188-10">
  1st. The nature of the writ.
 </p>
<p id="b188-11">
  Blackstone, in the 3d volume of his commentaries, page 110, defines a mandamus to be, “a command is-“suing in the king’s name from the court of king’s bench, "and directed to any person, corporation, or inferior "court of judicature within the king’s dominions, re-"quiring them to do some particular thing therein speci-"fied, which appertains to their office and duty, and “which the court of king’s bench has previously deter-“mined, or at least supposes, to be consonant to right “and justice.”
 </p>
<p id="b188-12">
  Lord Mansfield, in 3d Burrows 1266, in the case of the
  <em>
   King v.
  </em>
  Baker,
  <em>
   et al.
  </em>
  states with much precision and explicitness the cases in which this writ may be used.
 </p>
<p id="b188-13">
  “ Whenever,” says that very able judge, “there is a “right to execute an office, perform a service, or exercise “ a franchise (more especially if it be in a matter of pub-“lic concern, or attended with profit) and a person is “kept out of possession, or dispossessed of such right, and
  <span citation-index="1" class="star-pagination" label="169"> 
   *169
   </span>
  "has no other specific legal remedy, this court ought "to assist by mandamus, upon reasons of justice, as the “writ expresses, and upon reasons of public policy, to "preserve peace, order and good government.” In the same case he says, “this writ ought to be used upon all “occasions where the law has established no specific “remedy, and where in justice and good government “there ought to be one.”
 </p>
<p id="b189-6">
  In addition to the authorities now particularly cited, many others were relied on at the bar, which show how far the practice has conformed to the general doctrines that have been just quoted.
 </p>
<p id="b189-7">
  This writ, if awarded, would be directed to an officer of government, and its mandate to him would be, to use the words of Blackstone, “to do a particular thing “therein specified, which appertains to his office and “duty and which the court has previously determined, “or at least supposes, to be consonant to right and jus-“tice.” Or, in the words of Lord Mansfield, the applicant, in this case, has a right to execute an office of public concern, and is kept out of possession of that right.
 </p>
<p id="b189-9">
  These circumstances certainly concur in this case.
 </p>
<p id="b189-10">
  Still, to render the mandamus a proper remedy, the officer to whom it is to be directed, must be one to whom, on legal principles, such writ may be directed; and the person applying for it must be without any other specific and legal remedy.
 </p>
<p id="b189-11">
  1st. With respect to the officer to whom it would be directed. The intimate political relation, subsisting between the president of the United States and the heads of departments, necessarily renders any legal investigation of the acts of one of those high officers peculiarly irksome, as well as delicate; and excites some hesitation with respect to the propriety of entering into such investigation. Impressions are often received without much reflection or examination, and it is not wonderful that in such a case, as this, the assertion, by an individual, of his legal claims, in a court of justice; to which claims it is the duty of that court to attend; should at first view be considered
  <span citation-index="1" class="star-pagination" label="170"> 
   *170
   </span>
  by some, as an attempt to intrude into the cabinet, and to intermeddle with the prerogatives of the executive.
 </p>
<p id="A0I">
  It is scarcely necessary for the court to disclaim all pretensions to such a jurisdiction. An extravagance, so absurd and excessive, could not have been entertained for a moment. The province of the court is, solely, to decide on the rights of individuals, not to enquire how the executive, or executive officers, perform duties in which they have a discretion. Questions, in their nature political, or which are, by the constitution and laws, submitted to the executive, can never be made in this court.
 </p>
<p id="AC">
  But, if this be not such a question; if so far from being an intrusion into the secrets of the cabinet, it respects a paper, which, according to law, is upon record, and to a copy of which the law gives a right, on the payment of ten cents; if it be no intermeddling with a subject, over which the executive can be considered as having exercised any control; what is there in the exalted station of the officer, which shall bar a citizen from asserting, in a court of justice, his legal rights, or shall forbid a court to listen to the claim
  <em>
   ;
  </em>
  or to issue a mandamus, directing the performance of a duty, not depending on executive discretion, but on particular acts of congress and the general principles of law?
 </p>
<p id="b190-9">
  If one of the heads of departments commits any illegal act, under color of his office, by which an individual sustains an injury, it cannot be pretended that his office alone exempts him from being sued in the ordinary mode of proceeding, and being compelled to obey the judgment of the law. How then can his office exempt him from this particular mode of deciding on the legality of his conduct, if the case be such a case as would, were any other individual the party complained of, authorize the process?
 </p>
<p id="b190-10">
  It is not by the office of the person to whom the writ is directed, but the nature of the thing to be done that the propriety or impropriety of issuing a mandamus, is to be determined. Where the head of a department acts in a case, in which executive discretion is to be exercised; in which he is the mere organ of executive will; it is
  <span citation-index="1" class="star-pagination" label="171"> 
   *171
   </span>
  again repeated, that any application to a court to control, in any respect, his conduct, would be rejected without hesitation.
 </p>
<p id="b191-4">
  But where he is directed by law to do a certain act affecting the absolute rights of individuals, in the performance of which he is not placed under the particular direction of the President, and the performance of which, the President cannot lawfully forbid, and therefore is never presumed to have forbidden; as for example, to record a commission, or a patent for land, which has received all the legal solemnities; or to give a copy of such record; in such cases, it is not perceived on what ground the courts of the country are further excused from the duty of giving judgment, that right be done to an injured individual, than if the same services were to be performed by a person not the head of a department.
 </p>
<p id="b191-5">
  This opinion seems not now, for the first time, to be taken up in this country.
 </p>
<p id="b191-6">
  It must be well recollected that in 1792, an act passed, directing the secretary at war to place on the pension list such disabled officers and soldiers as should be reported to him, by the circuit courts, which act, so far as the duty was imposed on the courts, was deemed unconstitutional; but some of the judges, thinking that the law might be executed by them in the character of commissioners, proceeded to act and to report in that character.
 </p>
<p id="b191-7">
  This law being deemed unconstitutional at the circuits, was repealed, and a different system was established; but the question whether those persons, who had been reported by the judges, as commissioners, were entitled, in consequence of that report, to be placed on the pension list, was a legal question, properly determinable in the courts, although the act of placing such persons on the list was to be performed by the head of a department.
 </p>
<p id="b191-8">
  That this question might be properly settled, congress passed an act in February, 1793, making it the duty of the secretary of war, in conjunction with the attorney general, to take such measures, as might be necessary to obtain an adjudication of the supreme court of the United
  <span citation-index="1" class="star-pagination" label="172"> 
   *172
   </span>
  States on the validity of any such rights, claimed under the act aforesaid.
 </p>
<p id="AYPn">
  After the passage of this act, a mandamus was moved for, to be directed to the secretary at war, commanding him to place on the pension list, a person stating himself to be on the report of the judges.
 </p>
<p id="b192-7">
  There is, therefore, much reason to believe, that this mode of trying the legal right of the complainant, was deemed by the head of a department, and by the highest law officer of the United States, the most proper which could be selected for the purpose.
 </p>
<p id="b192-8">
  When the subject was brought before the court the decision was, not that a mandamus would not lie to the head of a department, directing him to perform an act, enjoined by law, in the performance of which an individual had a vested interest; but that a mandamus ought not to issue in that case—the decision necessarily to be made if the report of the commissioners did not confer on the applicant a legal right.
 </p>
<p id="b192-16">
  The judgment in that case, is understood to have decided the merits of all claims of that description; and the persons on the report of the commissioners found it necessary to pursue the mode prescribed by the law subsequent to that which had been deemed unconditional, in order to place themselves on the pension list.
 </p>
<p id="b192-17">
  The doctrine, therefore, now advanced, is by no means a novel one.
 </p>
<p id="b192-18">
  It is true that the mandamus, now moved for, is not for the performance of an act expressly enjoined by statute.
 </p>
<p id="b192-19">
  It is to deliver a commission; on which subject the acts of Congress are silent. This difference is not considered as affecting the case. It has already been stated that the applicant has, to that commission, a vested legal right, of which the executive cannot deprive him. He has been appointed to an office, from which he is not removable at the will of the executive; and being so
  <span citation-index="1" class="star-pagination" label="173"> 
   *173
   </span>
  appointed, he has a right to the commission which the secretary has received from the president for his use. The act of congress does not indeed order the secretary of state to send it to him, but it is placed in his hands for the person entitled to it; and cannot be more lawfully withheld by him, than by any other person.
 </p>
<p id="b193-5">
  It was at first doubted whether the action of
  <em>
   detinue
  </em>
  was not a specific legal remedy for the commission which has been withheld from Mr. Marbury; in which case a mandamus would be improper. But this doubt has yielded to the consideration that the judgment in
  <em>
   detinue
  </em>
  is for the thing itself,
  <em>
   or
  </em>
  its value. The value of a public office not to be sold, is incapable of being ascertained; and the applicant has a right to the office itself, or to nothing. He will obtain the office by obtaining the commission, or a copy of it from the record.
 </p>
<p id="b193-6">
  This, then, is a plain case for a mandamus, either to deliver the commission, or a copy of it from the record ; and it only remains to be enquired,
 </p>
<p id="b193-7">
  Whether it can issue from this court.
 </p>
<p id="b193-8">
  The act to establish the judicial courts of the United States authorizes the supreme court “to issue writs of “mandamus, in cases warranted by the principles and “usages of law, to any courts appointed, or persons hold-"ing office, under the authority of the United States.”
 </p>
<p id="b193-10">
  The secretary of state, being a person holding an office under the authority of the United States, is precisely within the letter of the description; and if this court is not authorized to issue a writ of mandamus to such an officer, it must be because the law is unconstitutional, and therefore absolutely incapable of conferring the authority, and assigning the duties which its words purport to confer and assign.
 </p>
<p id="b193-11">
  The constitution vests the whole judicial power of the United States in one supreme court, and such inferior courts as congress shall, from time to time, ordain and establish. This power is expressly extended to all cases arising under the laws of the United States; and consequently, in some form, may be exercised over the present
  <span citation-index="1" class="star-pagination" label="174"> 
   *174
   </span>
  case; because the right claimed is given by a law of the United States.
 </p>
<p id="AA-t">
  In the distribution of this power it is declared that “the “supreme court shall have original jurisdiction in all “cases affecting ambassadors, other public ministers and “consuls, and those in which a state shall be a party. “In all other cases, the supreme court shall have appellate “jurisdiction.”
 </p>
<p id="b194-5">
  It has been insisted, at the bar, that as the original grant of jurisdiction, to the supreme and inferior courts, is general, and the clause, assigning original jurisdiction, to the supreme court, contains no negative or restrictive words; the power remains to the legislature, to assign original jurisdiction to that court in other cases than those specified in the article which has been recited; provided those cases belong to the judicial power of the United States.
 </p>
<p id="b194-6">
  If it had been intended to leave it in the discretion of the legislature to apportion the judicial power between the supreme and inferior courts according to the will of that body, it would certainly have been useless to have proceeded further than to have defined the judicial power, and the tribunals in which it should be vested. The subsequent part of the section is mere surplussage, is entirely without meaning, if such is to be the construction. If congress remains at liberty to give this court appellate jurisdiction, where the constitution has declared their jurisdiction shall be original; and original jurisdiction where the constitution has declared it shall be appellate; the distribution of jurisdiction, made in the constitution, is form without substance.
 </p>
<p id="b194-7">
  Affirmative words are often, in their operation, negative of other objects than those affirmed; and in this case, a negative or exclusive sense must be given to them or they have no operation at all.
 </p>
<p id="b194-8">
  It cannot be presumed that any clause in the constitution is intended to be without effect; and therefore such a construction is inadmissible, unless the words require it.
 </p>
<p id="b195-2">
<span citation-index="1" class="star-pagination" label="175"> 
   *175
   </span>
  If the solicitude of the convention, respecting our peace with foreign powers, induced a provision that the supreme court should take original jurisdiction in cases which might be supposed to affect them; yet the clause would have proceeded no further than to provide for such cases, if no further restriction on the powers of congress had been intended. That they should have appellate jurisdiction in all other cases, with such exceptions as congress might make, is no restriction; unless the words be deemed exclusive of original jurisdiction.
 </p>
<p id="b195-3">
  When an instrument organizing fundamentally a judicial system, divides it into one supreme, and so many inferior courts as the legislature may ordain and establish; then enumerates its powers, and proceeds so far to distribute them, as to define the jurisdiction of the supreme court by declaring the cases in which it shall take original jurisdiction, and that in others it shall take appellate jurisdiction; the plain import of the words seems to be, that in one class of cases its jurisdiction is original, and not appellate; in the other it is appellate, and not original. If any other construction would render the clause inoperative, that is an additional reason for rejecting such other construction, and for adhering to their obvious meaning.
 </p>
<p id="b195-4">
  To enable this court then to issue a mandamus, it must be shewn to be an exercise of appellate jurisdiction, or to be necessary to enable them to exercise appellate jurisdiction.
 </p>
<p id="b195-5">
  It has been stated at the bar that the appellate jurisdiction may be exercised in a variety of forms, and that if it be the will of the legislature that a mandamus should be used for that purpose, that will must be obeyed. This is true, yet the jurisdiction must be appellate, not original.
 </p>
<p id="b195-7">
  It is the essential criterion of appellate jurisdiction, that it revises and corrects the proceedings in a cause already instituted, and does not create that cause. Although, therefore, a mandamus may be directed to courts, yet to issue such a writ to an officer for the delivery of a paper, is in effect the same as to sustain an original action
  <em>
   for
  </em>
  that paper, and therefore seems not
  <em>
   to
  </em>
  belong to
  <span citation-index="1" class="star-pagination" label="176"> 
   *176
   </span>
  appellate, but to original jurisdiction. Neither is it necessary in such a case as this, to enable the court to exercise its appellate jurisdiction.
 </p>
<p id="b196-5">
  The authority, therefore, given to the supreme court, by the act establishing the judicial courts of the United States, to issue writs of mandamus to public officers, appears not to be warranted by the constitution; and it becomes necessary to enquire whether a jurisdiction, so conferred, can be exercised.
 </p>
<p id="b196-6">
  The question, whether an act, repugnant to the constitution, can become the law of the land, is a question deeply interesting to the United States; but, happily, not of an intricacy proportioned to its interest. It seems only necessary to recognise certain principles, supposed to have been long and well established, to decide it.
 </p>
<p id="b196-7">
  That the people have an original right to establish, for their future government, such principles as, in their opinion, shall most conduce to their own happiness, is the basis, on which the whole American fabric has been erected. The exercise of this original right is a very great exertion; nor can it, nor ought it to be, frequently repeated. The principles, therefore, so established, are deemed fundamental. And as the authority, from which they proceed, is supreme, and can seldom act, they are designed to be permanent.
 </p>
<p id="b196-8">
  This original and supreme will organizes the government, and assigns,to different departments, their respective powers. It may either stop here; or establish certain limits not to be transcended by those departments.
 </p>
<p id="b196-9">
  The government of the United States is of the latter description. The powers of the legislature are defined, and limited; and that those limits may not be mistaken, or forgotten, the constitution is written. To what purpose are powers limited, and to what purpose is that limitation committed to writing, if these limits may, at any time, be passed by those intended to be restrained? The distinction, between a government with limited and unlimited powers, is abolished, if those limits do not confine the persons on whom they are imposed, and if acts pro
  <span citation-index="1" class="star-pagination" label="177"> 
   *177
   </span>
  hibited and acts allowed, are of equal obligation. It is a proposition too plain to be contested, that the constitution controls any legislative act repugnant to it; or, that the legislature may alter the constitution by an ordinary act.
 </p>
<p id="b197-3">
  Between these alternatives there is no middle ground. The constitution is either a superior, paramount law, unchangeable by ordinary means, or it is on a level with ordinary legislative acts, and like other acts, is alterable when the legislature shall please to alter it.
 </p>
<p id="b197-5">
  If the former part of the alternative be true, then a legislative act contrary to the constitution is not law: if the latter part be true, then written constitutions are absurd attempts, on the part of the people, to limit a power, in its own nature illimitable.
 </p>
<p id="b197-6">
  Certainly all those who have framed written constitutions contemplate them as forming the fundamental and paramount law of the nation, and consequently the theory of every such government must be, that an act of the legislature, repugnant to the constitution, is void.
 </p>
<p id="b197-7">
  This theory is essentially attached to a written constitution, and is consequently to be considered, by this court, as one of the fundamental principles of our society. It is not therefore to be lost fight of in the further consideration of this subject.
 </p>
<p id="b197-8">
  If an act of the legislature, repugnant to the constitution, is void, does it, notwithstanding its invalidity, bind the courts, and oblige them to give it effect? Or, in other words, though it be not law, does it constitute a rule as operative as if it was a law ? This would be to overthrow in fact what was established in theory; and would seem, at first view, an absurdity too gross to be insisted on. It shall, however, receive a more attentive consideration.
 </p>
<p id="b197-9">
  It is emphatically the province and duty of the judicial department to say what the law is. Those who apply the use to particular cases, must of necessity expound and interpret that rule. If two laws conflict with each other, the courts must decide on the operation of each.
 </p>
<p id="AIn">
<span citation-index="1" class="star-pagination" label="178"> 
   *178
   </span>
  So if a law be in opposition to the constitution; if both the law and the constitution apply to a particular case, so that the court must either decide that case conformably to the law, disregarding the constitution; or conformably to the constitution, disregarding the law; the court must determime which of these conflicting rules governs the case. This is of the very essence of judicial duty.
 </p>
<p id="b198-6">
  If then the courts are to regard the constitution; and the constitution is superior to any ordinary act of the legislature; the constitution, and not such ordinary act, must govern the case to which they both apply.
 </p>
<p id="b198-7">
  Those then who controvert the principle that the constitution is to be considered, in court, as a paramount law, are reduced to the necessity of maintaining that courts must close their eyes on the constitution, and see only the law.
 </p>
<p id="b198-8">
  This doctrine would subvert the very foundation of all written constitutions. It would declare that an act, which, according to the principles and theory of our government, is entirely void; is yet, in practice, completely obligatory, It would declare, that if the legislature shall do what is expressly forbiden, such act, notwithstanding the express prohibition, is in reality effectual. It would be giving to the legislature a practical and real omnipotence, with the same breath which professes to restrict their powers within narrow limits. It is prescribing limits, and declaring that those limits may be passed at pleasure.
 </p>
<p id="b198-9">
  That it thus reduces to nothing what we have deemed the greatest improvement on political institutions—a written constitution—would of itself be sufficient, in America, where written constitutions have been viewed with so much reverence, for rejecting the construction. But the peculiar expressions of the constitution of the United States furnish additional arguments in favour of its rejection.
 </p>
<p id="b198-10">
  The judicial power of the United States is extended to all cases arising under the constitution.
 </p>
<p id="b199-3">
<span citation-index="1" class="star-pagination" label="179"> 
   *179
   </span>
  Could it be the intention of those who gave this power, to say that, in using it, the constitution should not be looked into? That a case arising under the constitution should be decided without examining the instrument under which it arises?
 </p>
<p id="b199-4">
  This is too extravagant to be maintained.
 </p>
<p id="b199-5">
  In some cases then, the constitution must be looked into by the judges. And if they can open it at all, what part of it are they forbidden to read, or to obey?
 </p>
<p id="b199-6">
  There are many other parts of the constitution which serve to illustrate this subject.
 </p>
<p id="b199-7">
  It is declared that “ no tax or duty shall be laid on arti-“cles exported from any state.” Suppose a duty on the export of cotton, of tobacco, or of flour; and a suit instituted to recover it. Ought judgment to be rendered in such a case? ought the judges to close their eyes on the constitution, and only see the law.
 </p>
<p id="b199-8">
  The constitution declares that “no bill of attainder or "ex
  <em>
   post facto
  </em>
  law shall be passed.”
 </p>
<p id="b199-9">
  If, however, such a bill should be passed and a person should be prosecuted under it; must the court condemn to death those victims whom the constitution endeavours to preserve?
 </p>
<p id="b199-10">
  “No person,” says the constitution, “shall be convicted “of treason unless on the testimony of two witnesses to the same overt act, or on confession in open court.”
 </p>
<p id="b199-12">
  Here the language of the constitution is addressed especially to the courts. It prescribes, directly for them, a rule of evidence not to be departed from. If the legislature should change that rule, and declare
  <em>
   one
  </em>
  witness, or a confession
  <em>
   out
  </em>
  of court, sufficient for conviction, must the constitutional principles yield to the legislative act?
 </p>
<p id="b199-13">
  From these, and many other selections which might be made, it is apparent, that the framers of the consti
  <span citation-index="1" class="star-pagination" label="180"> 
   *180
   </span>
  tution contemplated that instrument, as a rule for the government of courts, as well as of the legislature.
 </p>
<p id="AY9">
  Why otherwise does it direct the judges to take an oath to support it ? This oath certainly applies, in an especial manner, to their conduct in their official character. How immoral to impose it on them, if they were to be used as the instruments, and the knowing instruments, for violating what they swear to support!
 </p>
<p id="b200-6">
  The oath of office, too, imposed by the legislature, is completely demonstrative of the legislative opinion on this subject. It is in these words, “I do solemnly “swear that I will administer justice without respect “to persons, and do equal right to the poor and to the “rich; and that I will faithfully and impartially discharge “all the duties incumbent on me as accord-“ing to the best of my abilities and understanding, agree-“ably to
  <em>
   the constitution,
  </em>
  and laws of the United States.”
 </p>
<p id="b200-8">
  Why does a judge swear to discharge his duties agreably to the constitution of the United States, if that constitution forms no rule for his government? if it is closed upon him, and cannot be inspected by him?
 </p>
<p id="b200-9">
  If such be the real state of things, this is worse than solemn mockery. To prescribe, or to take this oath, becomes equally a crime.
 </p>
<p id="b200-10">
  It is also not entirely unworthy of observation, that in declaring what shall be the
  <em>
   supreme
  </em>
  law of the land, the
  <em>
   constitution
  </em>
  itself is first mentioned; and not the laws of the United States generally, but those only which shall be made in
  <em>
   pursuance
  </em>
  of the constitution, have that rank.
 </p>
<p id="b200-11">
  Thus, the particular phraseology of the constitution of the United States confirms and strengthens the principle, supposed to be essential to all written constitutions, that a law repugnant to the constitution is void; and that
  <em>
   courts,
  </em>
  as well as other departments, are bound by that instrument.
 </p>
<p id="b200-12">
  The rule must be discharged.
 </p>
</opinion>
```

---
