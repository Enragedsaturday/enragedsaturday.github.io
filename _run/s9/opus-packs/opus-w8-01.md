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

## GROUP: _overhaul2/lake/cases/Minnesota v. Olson.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Minnesota v. Olson"
type: case
citation: "495 U.S. 91 (1990)"
parallel_cite: "110 S. Ct. 1684; 109 L. Ed. 2d 85; 58 U.S.L.W. 4464"
neutral_cite: 1990 U.S. LEXIS 2038
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1990
date_decided: 1990-04-18
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1990-04-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Minnesota v. Olson
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112416/minnesota-v-olson/"
  cluster_id: 112416
  opinion_id: 112416
  identity_checked: true
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: "Key — Progeny / Refinement"
related: ["[[Minnesota v. Carter]]", "[[Rakas v. Illinois]]", "[[Jones v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "standing", "expectation-of-privacy", "overnight-guest", "home"]
holding: "An overnight guest has a reasonable expectation of privacy in his host's home and therefore standing to challenge a warrantless entry to…"
lake:
  record_id: Minnesota v. Olson
  status: verified
  projected_at: 2026-07-06
---

# Minnesota v. Olson

*495 U.S. 91 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police suspected Olson of being the getaway driver in a robbery-murder and believed he was staying as an overnight guest in the home of two women. Without a warrant, they entered the home and arrested him. He sought to suppress a statement as the fruit of an unlawful warrantless entry.

## Issue
Whether an overnight guest has a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in his host's home sufficient to challenge a warrantless entry.

## Rule
Yes. "we think that society recognizes that a houseguest has a legitimate expectation of privacy in his host's home." — 495 U.S. at 98. ^pin-98

An overnight guest's status is alone enough to establish an expectation of privacy in the host's home that society is prepared to recognize as reasonable.

## Application
Olson was staying as an overnight guest in the women's home when police entered without a warrant to arrest him. Because his status as an overnight guest gave him a legitimate expectation of privacy in that home, he could challenge the warrantless entry, which — absent consent or [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] — was unlawful.

## Conclusion
Affirmed; Olson had [[Standing to Challenge a Search|standing to challenge]] the entry, and the warrantless arrest in the home was unconstitutional.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Olson* refines the standing framework of [[Rakas v. Illinois]]; its overnight-guest rule is bounded by [[Minnesota v. Carter]], which denied protection to a short-term commercial visitor.

## Appears on
- [[Standing to Challenge a Search]] — *Key — Progeny / Refinement*

## Sources
- *Minnesota v. Olson*, 495 U.S. 91 (1990) — https://www.courtlistener.com/opinion/112416/minnesota-v-olson/ — pinpoint: 98.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4ee5871c486af17d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Minnesota v. Olson"}, "payload": {"all": [{"cite": "495 U.S. 91", "page": "91", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "495"}, {"cite": "110 S. Ct. 1684", "page": "1684", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "110"}, {"cite": "109 L. Ed. 2d 85", "page": "85", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "109"}, {"cite": "1990 U.S. LEXIS 2038", "page": "2038", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1990"}, {"cite": "58 U.S.L.W. 4464", "page": "4464", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "58"}], "display": "495 U.S. 91", "official": {"cite": "495 U.S. 91", "page": "91", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "495"}, "official_selection_present": true, "record_id": "Minnesota v. Olson"}}
{"assertion_id": "c8b7d9585128856b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-98", "record_id": "Minnesota v. Olson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-98", "pinpoint_status": "slip-only", "quote": "--- # Minnesota v. Olson *495 U.S. 91 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police suspected Olson of being the getaway driver in a robbery-murder and believed he was staying as an overnight guest in the home of two women. Without a warrant, they entered the home and arrested him. He sought to suppress a statement as the fruit of an unlawful warrantless entry. ## Issue Whether an overnight guest has a reasonable expectation of privacy in his host's home sufficient to challenge a warrantless entry. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Minnesota v. Olson", "star_marker": null}}
{"assertion_id": "86783880786b0830", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Minnesota v. Olson"}, "payload": {"as_of_content": "1990-04-18", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Minnesota v. Olson", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Minnesota v. Olson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Minnesota v. Olson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Minnesota v. Olson",
    "case_name_short": "Olson",
    "case_name_full": "Minnesota v. Olson",
    "input_case_name": "Minnesota v. Olson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-04-18",
    "year": 1990,
    "docket": null,
    "cluster_id": 112416,
    "lead_opinion_id": 112416,
    "sibling_ids": [
      112416,
      9431979,
      9431980,
      9431981
    ],
    "absolute_url": "/opinion/112416/minnesota-v-olson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9097985,
        "score": 20,
        "case_name": "Minnesota v. Olson"
      },
      {
        "cluster_id": 9097984,
        "score": 20,
        "case_name": "Minnesota v. Olson"
      },
      {
        "cluster_id": 9093477,
        "score": 20,
        "case_name": "Minnesota v. Olson"
      },
      {
        "cluster_id": 9093476,
        "score": 20,
        "case_name": "Minnesota v. Olson"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "495 U.S. 91",
      "volume": "495",
      "reporter": "U.S.",
      "page": "91",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "110 S. Ct. 1684",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "1684",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 L. Ed. 2d 85",
        "volume": "109",
        "reporter": "L. Ed. 2d",
        "page": "85",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 U.S.L.W. 4464",
        "volume": "58",
        "reporter": "U.S.L.W.",
        "page": "4464",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 2038",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "2038",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "495 U.S. 91",
        "volume": "495",
        "reporter": "U.S.",
        "page": "91",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 S. Ct. 1684",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "1684",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 L. Ed. 2d 85",
        "volume": "109",
        "reporter": "L. Ed. 2d",
        "page": "85",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 2038",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "2038",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 U.S.L.W. 4464",
        "volume": "58",
        "reporter": "U.S.L.W.",
        "page": "4464",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "495 U.S. 91",
    "official_selection": {
      "court_class": "scotus",
      "selected": "495 U.S. 91",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-98",
      "page": null,
      "quote": "--- # Minnesota v. Olson *495 U.S. 91 (1990)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police suspected Olson of being the getaway driver in a robbery-murder and believed he was staying as an overnight guest in the home of two women. Without a warrant, they entered the home and arrested him. He sought to suppress a statement as the fruit of an unlawful warrantless entry. ## Issue Whether an overnight guest has a reasonable expectation of privacy in his host's home sufficient to challenge a warrantless entry. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1990-04-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Minnesota v. Olson",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Jordan",
          "cluster_id": 9487045,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane1_negative"
      },
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
        "journal_ref": "Minnesota v. Olson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Stanley",
          "cluster_id": 4497878,
          "cite": [
            "817 S.E.2d 107",
            "259 N.C. App. 708"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Aiken",
          "cluster_id": 8619549,
          "cite": [
            "877 F.3d 451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane1_negative"
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
        "journal_ref": "Minnesota v. Olson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Bodie Witzlib",
          "cluster_id": 2825238,
          "cite": [
            "796 F.3d 799",
            "2015 U.S. App. LEXIS 13811",
            "2015 WL 4664340"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Hillary Lee Tyler",
          "cluster_id": 2820149,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Hillary Lee Tyler",
          "cluster_id": 2812907,
          "cite": [
            "867 N.W.2d 136",
            "2015 Iowa Sup. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Haynes",
          "cluster_id": 2795871,
          "cite": [
            "116 A.3d 640",
            "2015 Pa. Super. 94",
            "2015 Pa. Super. LEXIS 207",
            "2015 WL 1814017"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane1_negative"
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
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kentucky v. King",
          "cluster_id": 216733,
          "cite": [
            "179 L. Ed. 2d 865",
            "131 S. Ct. 1849",
            "563 U.S. 452",
            "2011 U.S. LEXIS 3541"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Villarreal v. State",
          "cluster_id": 2365320,
          "cite": [
            "935 S.W.2d 134",
            "1996 Tex. Crim. App. LEXIS 237",
            "1996 WL 668593"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
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
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Carter",
          "cluster_id": 118249,
          "cite": [
            "142 L. Ed. 2d 373",
            "119 S. Ct. 469",
            "525 U.S. 83",
            "1998 U.S. LEXIS 7844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
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
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
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
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
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
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marvin Berkowitz",
          "cluster_id": 557342,
          "cite": [
            "927 F.2d 1376",
            "1991 U.S. App. LEXIS 4135",
            "1991 WL 33079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Welch",
          "cluster_id": 1277687,
          "cite": [
            "976 P.2d 754",
            "85 Cal. Rptr. 2d 203",
            "20 Cal. 4th 701",
            "99 Daily Journal DAR 5242",
            "99 Cal. Daily Op. Serv. 4127",
            "1999 Cal. LEXIS 2976",
            "1999 WL 344511"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Linette Perez, United States of America v. Juancho Alcantera, United States of America v. Edmundo Batoon",
          "cluster_id": 776532,
          "cite": [
            "280 F.3d 318",
            "2002 WL 171241"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Givens",
          "cluster_id": 2482051,
          "cite": [
            "934 N.E.2d 470",
            "237 Ill. 2d 311"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Granados v. State",
          "cluster_id": 1588783,
          "cite": [
            "85 S.W.3d 217",
            "2002 Tex. Crim. App. LEXIS 99",
            "2002 WL 922901"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Figueroa v. Mazza",
          "cluster_id": 3209159,
          "cite": [
            "825 F.3d 89",
            "2016 U.S. App. LEXIS 10152",
            "2016 WL 3126772"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Louis Lalonde v. County of Riverside, Robert Moquin, and Jason Horton, Opinion",
          "cluster_id": 767803,
          "cite": [
            "204 F.3d 947",
            "2000 Daily Journal DAR 2031",
            "2000 Cal. Daily Op. Serv. 1433",
            "2000 U.S. App. LEXIS 2778",
            "2000 WL 217552"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sharrar v. Felsing",
          "cluster_id": 747743,
          "cite": [
            "128 F.3d 810",
            "1997 U.S. App. LEXIS 29129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
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
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Byrd v. United States",
          "cluster_id": 4497658,
          "cite": [
            "584 U.S. 395",
            "138 S. Ct. 1518",
            "200 L. Ed. 2d 805",
            "2018 U.S. LEXIS 2803"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McPeters",
          "cluster_id": 1182062,
          "cite": [
            "832 P.2d 146",
            "2 Cal. 4th 1148",
            "9 Cal. Rptr. 2d 834",
            "92 Cal. Daily Op. Serv. 6202",
            "92 Daily Journal DAR 9757",
            "1992 Cal. LEXIS 3177"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Luna v. State",
          "cluster_id": 1488102,
          "cite": [
            "268 S.W.3d 594",
            "2008 Tex. Crim. App. LEXIS 1672",
            "2008 WL 4724087"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald Tobin, Clifford Roger Ackerson, United States of America v. Ronald Tobin",
          "cluster_id": 554960,
          "cite": [
            "923 F.2d 1506",
            "1991 U.S. App. LEXIS 2683"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Attaway",
          "cluster_id": 1349754,
          "cite": [
            "870 P.2d 103",
            "117 N.M. 141"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maureen Tierney, for Herself and as Mother of Philip T. Newton, Patrick J. Newton v. Joel R. Davidson Thomas E. Williams, State of Vermont",
          "cluster_id": 750084,
          "cite": [
            "133 F.3d 189",
            "1998 U.S. App. LEXIS 111"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vernon Snype, Marisa Hicks",
          "cluster_id": 793658,
          "cite": [
            "441 F.3d 119",
            "69 Fed. R. Serv. 817",
            "2006 U.S. App. LEXIS 6909"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Coffin v. Stacy Brandau",
          "cluster_id": 3048939,
          "cite": [
            "642 F.3d 999",
            "2011 U.S. App. LEXIS 11353",
            "2011 WL 2162997"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Olson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112416 OR 9431979 OR 9431980 OR 9431981) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzY2MTU2ODAwMDAwJnM9Mjk0ODMxNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112416+OR+9431979+OR+9431980+OR+9431981%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112416 OR 9431979 OR 9431980 OR 9431981)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzYmcz0xMDU3NzI3JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112416+OR+9431979+OR+9431980+OR+9431981%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112416 OR 9431979 OR 9431980 OR 9431981)",
        "reviewed": 37,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 37,
        "triage_read": 1,
        "triage_snippet_classified": 36
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112416 OR 9431979 OR 9431980 OR 9431981)",
    "indexed_citing_opinions": 1069,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112416,
        "count": 919,
        "count_source": "search"
      },
      {
        "opinion_id": 9431979,
        "count": 166,
        "count_source": "search"
      },
      {
        "opinion_id": 9431980,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431981,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1716,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/minnesota-v-olson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4MTQ4ODcmcz05NTA3MDQ0JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112416+OR+9431979+OR+9431980+OR+9431981%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112416,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112416,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112416,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112416,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112416,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112416,
        "cited_id": 111226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112416,
        "cited_id": 111625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112416,
        "cited_id": 1678447,
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
    "date_created": "2026-07-05T14:02:15Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:02:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:02:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:06:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:02:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Minnesota v. Olson

```
<div>
<center><b><span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">495 U.S. 91</a></span> (1990)</b></center>
<center><h1>MINNESOTA<br>
v.<br>
OLSON</h1></center>
<center>No. 88-1916.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 26, 1990</center>
<center>Decided April 18, 1990</center>
CERTIORARI TO THE SUPREME COURT OF MINNESOTA
<p><span class="star-pagination">*92</span> <i>Anne E. Peek</i> argued the cause for petitioner. With her on the briefs were <i>Hubert H. Humphrey III,</i> Attorney General of Minnesota, and <i>Thomas L. Johnson.</i></p>
<p><i>Stephen J. Marzen</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Starr, Assistant Attorney General Dennis,</i> and <i>Deputy Solicitor General Bryson.</i></p>
<p><i>Glenn P. Bruder,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./493/989/">493 U. S. 989</a></span>, argued the cause for respondent.<sup>[*]</sup></p>
<p><span class="star-pagination">*93</span> JUSTICE WHITE delivered the opinion of the Court.</p>
<p>The police in this case made a warrantless, nonconsensual entry into a house where respondent Robert Olson was an overnight guest and arrested him. The issue is whether the arrest violated Olson's Fourth Amendment rights. We hold that it did.</p>
<p></p>
<h2>I</h2>
<p>Shortly before 6 a.m. on Saturday, July 18, 1987, a lone gunman robbed an Amoco gasoline station in Minneapolis, Minnesota, and fatally shot the station manager. A police officer heard the police dispatcher report and suspected Joseph Ecker. The officer and his partner drove immediately to Ecker's home, arriving at about the same time that an Oldsmobile arrived. The driver of the Oldsmobile took evasive action, and the car spun out of control and came to a stop. Two men fled the car on foot. Ecker, who was later identified as the gunman, was captured shortly thereafter inside his home. The second man escaped.</p>
<p>Inside the abandoned Oldsmobile, police found a sack of money and the murder weapon. They also found a title certificate with the name of Rob Olson crossed out as a secured party, a letter addressed to a Roger R. Olson of 3151 Johnson Street, and a videotape rental receipt made out to Rob Olson and dated two days earlier. The police verified that a Robert Olson lived at 3151 Johnson Street.</p>
<p>The next morning, Sunday, July 19, a woman identifying herself as Dianna Murphy called the police and said that a man by the name of Rob drove the car in which the gas station killer left the scene and that Rob was planning to leave town by bus. About noon, the same woman called again, gave her address and phone number, and said that a man named Rob had told a Maria and two other women, Louanne and Julie, that he was the driver in the Amoco robbery. The caller stated that Louanne was Julie's mother and that the two women lived at 2406 Fillmore Northeast. The detective-in-charge who took the second phone call sent police <span class="star-pagination">*94</span> officers to 2406 Fillmore to check out Louanne and Julie. When police arrived they determined that the dwelling was a duplex and that Louanne Bergstrom and her daughter Julie lived in the upper unit but were not home. Police spoke to Louanne's mother, Helen Niederhoffer, who lived in the lower unit. She confirmed that a Rob Olson had been staying upstairs but was not then in the unit. She promised to call the police when Olson returned. At 2 p.m., a pickup order, or "probable cause arrest bulletin," was issued for Olson's arrest. The police were instructed to stay away from the duplex.</p>
<p>At approximately 2:45 p.m., Niederhoffer called police and said Olson had returned. The detective-in-charge instructed police officers to go to the house and surround it. He then telephoned Julie from headquarters and told her Rob should come out of the house. The detective heard a male voice say, "tell them I left." Julie stated that Rob had left, whereupon at 3 p.m. the detective ordered the police to enter the house. Without seeking permission and with weapons drawn, the police entered the upper unit and found respondent hiding in a closet. Less than an hour after his arrest, respondent made an inculpatory statement at police headquarters.</p>
<p>The Hennepin County trial court held a hearing and denied respondent's motion to suppress his statement. App. 3-13. The statement was admitted into evidence at Olson's trial, and he was convicted on one count of first-degree murder, three counts of armed robbery, and three counts of second-degree assault. On appeal, the Minnesota Supreme Court reversed. <span class="citation" data-id="1678447"><a href="/opinion/1678447/state-v-olson/" aria-description="Citation for case: State v. Olson">436 N. W. 2d 92</a></span> (1989). The court ruled that respondent had a sufficient interest in the Bergstrom home to challenge the legality of his warrantless arrest there, that the arrest was illegal because there were no exigent circumstances to justify a warrantless entry,<sup>[1]</sup> and that respondent's <span class="star-pagination">*95</span> statement was tainted by that illegality and should have been suppressed.<sup>[2]</sup> Because the admission of the statement was not harmless beyond reasonable doubt, the court reversed Olson's conviction and remanded for a new trial.<sup>[3]</sup></p>
<p>We granted the State's petition for certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./493/806/">493 U. S. 806</a></span> (1989), and now affirm.</p>
<p></p>
<h2>II</h2>
<p>It was held in <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980), that a suspect should not be arrested in his house without an arrest warrant, even though there is probable cause to arrest him. The purpose of the decision was not to protect the person of the suspect but to protect his home from entry in the absence of a magistrate's finding of probable cause. In this case, the court below held that Olson's warrantless arrest was illegal because he had a sufficient connection with the premises to be treated like a householder. The State challenges that conclusion.</p>
<p>Since the decision in <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), it has been the law that "capacity to claim the protection of the Fourth Amendment depends . . . upon whether the person who claims the protection of the Amendment has a legitimate expectation of privacy in the invaded place." <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 143</a></span> (1978). A subjective expectation of privacy is legitimate if it is " `one that society <span class="star-pagination">*96</span> is prepared to recognize as "reasonable," ' " <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois"><i>id.,</i> at 143-144, n. 12</a></span>, quoting <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States"><i>Katz, supra,</i> at 361</a></span> (Harlan, J., concurring).</p>
<p>The State argues that Olson's relationship to the premises does not satisfy the 12 factors which in its view determine whether a dwelling is a "home."<sup>[4]</sup> Aside from the fact that it is based on the mistaken premise that a place must be one's "home" in order for one to have a legitimate expectation of privacy there,<sup>[5]</sup> the State's proposed test is needlessly complex. We need go no further than to conclude, as we do, that Olson's status as an overnight guest is alone enough to show <span class="star-pagination">*97</span> that he had an expectation of privacy in the home that society is prepared to recognize as reasonable.</p>
<p>As recognized by the Minnesota Supreme Court, the facts of this case are similar to those in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960). In <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> the defendant was arrested in a friend's apartment during the execution of a search warrant and sought to challenge the warrant as not supported by probable cause.</p>
<blockquote>"[Jones] testified that the apartment belonged to a friend, Evans, who had given him the use of it, and a key, with which [Jones] had admitted himself on the day of the arrest. On cross-examination [Jones] testified that he had a suit and shirt at the apartment, that his home was elsewhere, that he paid nothing for the use of the apartment, that Evans had let him use it `as a friend,' that he had slept there `maybe a night,' and that at the time of the search Evans had been away in Philadelphia for about five days." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#259" aria-description="Citation for case: Jones v. United States"><i>Id.,</i> at 259</a></span>.<sup>[6]</sup></blockquote>
<p>The Court ruled that Jones could challenge the search of the apartment because he was "legitimately on [the] premises," <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States"><i>id.,</i> at 267</a></span>. Although the "legitimately on [the] premises" standard was rejected in <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span></i> as too broad, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#142" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 142-148</a></span>, the <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span></i> Court explicitly reaffirmed the factual holding in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>:</i></p>
<blockquote>"We do not question the conclusion in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> that the defendant in that case suffered a violation of his personal Fourth Amendment rights if the search in question was unlawful. . . .</blockquote>
<blockquote>"We think that <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> on its facts merely stands for the unremarkable proposition that a person can have a legally sufficient interest in a place other than his own <span class="star-pagination">*98</span> home so that the Fourth Amendment protects him from unreasonable governmental intrusion into that place." <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#141" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 141-142</a></span>.</blockquote>
<p><i>Rakas</i> thus recognized that, as an overnight guest, Jones was much more than just legitimately on the premises.</p>
<p>The distinctions relied on by the State between this case and <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> are not legally determinative. The State emphasizes that in this case Olson was never left alone in the duplex or given a key, whereas in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> the owner of the apartment was away and Jones had a key with which he could come and go and admit and exclude others. These differences are crucial, it is argued, because in not disturbing the holding in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> the Court pointed out that while his host was away, Jones had complete dominion and control over the apartment and could exclude others from it. <i>Rakas,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#149" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 149</a></span>. We do not understand <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span>,</i> however, to hold that an overnight guest can never have a legitimate expectation of privacy except when his host is away and he has a key, or that only when those facts are present may an overnight guest assert the "unremarkable proposition," <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#142" aria-description="Citation for case: Rakas v. Illinois"><i>id.,</i> at 142</a></span>, that a person may have a sufficient interest in a place other than his home to enable him to be free in that place from unreasonable searches and seizures.</p>
<p>To hold that an overnight guest has a legitimate expectation of privacy in his host's home merely recognizes the everyday expectations of privacy that we all share. Staying overnight in another's home is a longstanding social custom that serves functions recognized as valuable by society. We stay in others' homes when we travel to a strange city for business or pleasure, when we visit our parents, children, or more distant relatives out of town, when we are in between jobs or homes, or when we house-sit for a friend. We will all be hosts and we will all be guests many times in our lives. From either perspective, we think that society recognizes that a houseguest has a legitimate expectation of privacy in his host's home.</p>
<p><span class="star-pagination">*99</span> From the overnight guest's perspective, he seeks shelter in another's home precisely because it provides him with privacy, a place where he and his possessions will not be disturbed by anyone but his host and those his host allows inside. We are at our most vulnerable when we are asleep because we cannot monitor our own safety or the security of our belongings. It is for this reason that, although we may spend all day in public places, when we cannot sleep in our own home we seek out another private place to sleep, whether it be a hotel room, or the home of a friend. Society expects at least as much privacy in these places as in a telephone booth  "a temporarily private place whose momentary occupants' expectations of freedom from intrusion are recognized as reasonable," <i>Katz,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S., at 361</a></span> (Harlan, J., concurring).</p>
<p>That the guest has a host who has ultimate control of the house is not inconsistent with the guest having a legitimate expectation of privacy. The houseguest is there with the permission of his host, who is willing to share his house and his privacy with his guest. It is unlikely that the guest will be confined to a restricted area of the house; and when the host is away or asleep, the guest will have a measure of control over the premises. The host may admit or exclude from the house as he prefers, but it is unlikely that he will admit someone who wants to see or meet with the guest over the objection of the guest. On the other hand, few houseguests will invite others to visit them while they are guests without consulting their hosts; but the latter, who have the authority to exclude despite the wishes of the guest, will often be accommodating. The point is that hosts will more likely than not respect the privacy interests of their guests, who are entitled to a legitimate expectation of privacy despite the fact that they have no legal interest in the premises and do not have the legal authority to determine who may or may not enter the household. If the untrammeled power to admit and exclude were essential to Fourth Amendment protection, <span class="star-pagination">*100</span> an adult daughter temporarily living in the home of her parents would have no legitimate expectation of privacy because her right to admit or exclude would be subject to her parents' veto.</p>
<p>Because respondent's expectation of privacy in the Bergstrom home was rooted in "understandings that are recognized and permitted by society," <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#144" aria-description="Citation for case: Rakas v. Illinois"><i>Rakas, supra,</i> at 144, n. 12</a></span>, it was legitimate, and respondent can claim the protection of the Fourth Amendment.</p>
<p></p>
<h2>III</h2>
<p>In <i>Payton</i> v. <i><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">New York</a></span></i><i>,</i> the Court had no occasion to "consider the sort of emergency or dangerous situation, described in our cases as `exigent circumstances,' that would justify a warrantless entry into a home for the purpose of either arrest or search," <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York">445 U. S., at 583</a></span>. This case requires us to determine whether the Minnesota Supreme Court was correct in holding that there were no exigent circumstances that justified the warrantless entry into the house to make the arrest.</p>
<p>The Minnesota Supreme Court applied essentially the correct standard in determining whether exigent circumstances existed. The court observed that "a warrantless intrusion may be justified by hot pursuit of a fleeing felon, or imminent destruction of evidence, <i>Welsh</i> [v. <i>Wisconsin</i>], <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740</a></span> [(1984)], or the need to prevent a suspect's escape, or the risk of danger to the police or to other persons inside or outside the dwelling." <span class="citation" data-id="1678447"><a href="/opinion/1678447/state-v-olson/#97" aria-description="Citation for case: State v. Olson">436 N. W. 2d, at 97</a></span>. The court also apparently thought that in the absence of hot pursuit there must be at least probable cause to believe that one or more of the other factors justifying the entry were present and that in assessing the risk of danger, the gravity of the crime and likelihood that the suspect is armed should be considered. Applying this standard, the state court determined that exigent circumstances did not exist.</p>
<p>We are not inclined to disagree with this fact-specific application of the proper legal standard. The court pointed out <span class="star-pagination">*101</span> that although a grave crime was involved, respondent "was known not to be the murderer but thought to be the driver of the getaway car," <i>ibid.,</i> and that the police had already recovered the murder weapon, <i><span class="citation" data-id="1678447"><a href="/opinion/1678447/state-v-olson/" aria-description="Citation for case: State v. Olson">ibid.</a></span></i> "The police knew that Louanne and Julie were with the suspect in the upstairs duplex with no suggestion of danger to them. Three or four Minneapolis police squads surrounded the house. The time was 3 p.m., Sunday. . . . It was evident the suspect was going nowhere. If he came out of the house he would have been promptly apprehended." <i><span class="citation" data-id="1678447"><a href="/opinion/1678447/state-v-olson/" aria-description="Citation for case: State v. Olson">Ibid.</a></span></i> We do not disturb the state court's judgment that these facts do not add up to exigent circumstances.</p>
<p></p>
<h2>IV</h2>
<p>We therefore affirm the judgment of the Minnesota Supreme Court.</p>
<p><i>It is so ordered.</i></p>
<p>CHIEF JUSTICE REHNQUIST and JUSTICE BLACKMUN dissent.</p>
<p>JUSTICE STEVENS, concurring.</p>
<p>While I join the Court's entire opinion, I add this caveat concerning the discussion in Part II of respondent's standing to challenge his arrest on federal constitutional grounds. If we had concluded that he did not have standing as a matter of federal law, the question that would then have been presented would be whether this Court simply should have dismissed the appeal. For we have no power to prevent state courts from allowing litigants to raise federal questions even though they would not have standing to do so in a federal court. See <i>Secretary of State of Maryland</i> v. <i>Joseph H. Munson Co.,</i> <span class="citation" data-id="9429676"><a href="/opinion/111226/secretary-of-state-of-md-v-joseph-h-munson-co/#970" aria-description="Citation for case: Secretary of State of Md. v. Joseph H. Munson Co.">467 U. S. 947, 970-971</a></span> (1984) (concurring opinion).</p>
<p>Questions of that kind buttress my opinion that the Court grants review in far too many cases in which state courts have protected the constitutional rights of their own citizens. Notwithstanding the Court's decision to enlarge its <span class="star-pagination">*102</span> own power to review state-court judgments, see <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983), I remain convinced that this power should be used sparingly. See generally <i>Delaware</i> v. <i>Van Arsdall,</i> <span class="citation" data-id="9430412"><a href="/opinion/111625/delaware-v-van-arsdall/#689" aria-description="Citation for case: Delaware v. Van Arsdall">475 U. S. 673, 689-708</a></span> (1986) (dissenting opinion). Only in the most unusual case should the Court volunteer its opinion that a state court has imposed standards upon its own law enforcement officials that are too high.</p>
<p>JUSTICE KENNEDY, concurring.</p>
<p>I interpret the last two paragraphs of Part III as deference to a state court's application of the exigent circumstances test to the facts of this case, and not as an endorsement of that particular application of the standard. With that understanding, I join the opinion of the Court.</p>
<h2>NOTES</h2>
<p>[*]  A brief of <i>amici curiae</i> urging reversal was filed for the State of Connecticut et al. by <i>John J. Kelly,</i> Chief State's Attorney of Connecticut, <i>Charles M. Oberly III,</i> Attorney General of Delaware, <i>Linley E. Pearson,</i> Attorney General of Indiana, <i>Robert T. Stephan,</i> Attorney General of Kansas, <i>Frederic J. Cowan,</i> Attorney General of Kentucky, <i>Frank J. Kelley,</i> Attorney General of Michigan, <i>Mike Moore,</i> Attorney General of Mississippi, <i>William L. Webster,</i> Attorney General of Missouri, <i>John P. Arnold,</i> Attorney General of New Hampshire, <i>Peter N. Perretti, Jr.,</i> Attorney General of New Jersey, <i>Hal Stratton,</i> Attorney General of New Mexico, <i>Lacy H. Thornburg,</i> Attorney General of North Carolina, <i>T. Travis Medlock,</i> Attorney General of South Carolina, <i>Roger A. Tellinghuisen,</i> Attorney General of South Dakota, <i>R. Paul Van Dam,</i> Attorney General of Utah, <i>Jeffrey L. Amestoy,</i> Attorney General of Vermont, <i>Mary Sue Terry,</i> Attorney General of Virginia, <i>Joseph B. Meyer,</i> Attorney General of Wyoming, <i>James B. Early,</i> Special Assistant Attorney General of Minnesota, <i>George D. Webster, Jack E. Yelverton,</i> and <i>Gregory U. Evans.</i></p>
<p>[1]  Because the absence of a warrant made respondent's arrest illegal, the court did not review the trial court's determination that the police had probable cause for the arrest. <span class="citation" data-id="1678447"><a href="/opinion/1678447/state-v-olson/#95" aria-description="Citation for case: State v. Olson">436 N. W. 2d, at 95</a></span>. Hence, we judge the case on the assumption that there was probable cause.</p>
<p>[2]  The State had not argued that, if the arrest was illegal, respondent's statement was nevertheless not tainted by the illegality. <span class="citation" data-id="1678447"><a href="/opinion/1678447/state-v-olson/#98" aria-description="Citation for case: State v. Olson"><i>Id.,</i> at 98</a></span>. Likewise, at oral argument before this Court, counsel for the State expressly disavowed any claim that the statement was not a fruit of the arrest. Tr. of Oral Arg. 4-5. We will therefore not raise <i>sua sponte</i> the applicability of <i>New York</i> v. <i>Harris, ante,</i> p. 14, to the facts of this case.</p>
<p>[3]  The court left for the trial court on remand respondent's claims that other evidence  statements by persons present at 2406 Fillmore at the time of the arrest and a statement by Ecker obtained after the police showed him respondent's statement  should also have been suppressed as fruit of the illegal arrest.</p>
<p>[4]  The 12 factors are:
</p>
<p>(1) the visitor has some property rights in the dwelling;</p>
<p>(2) the visitor is related by blood or marriage to the owner or lessor of the dwelling;</p>
<p>(3) the visitor receives mail at the dwelling or has his name on the door;</p>
<p>(4) the visitor has a key to the dwelling;</p>
<p>(5) the visitor maintains a regular or continuous presence in the dwelling, especially sleeping there regularly;</p>
<p>(6) the visitor contributes to the upkeep of the dwelling, either monetarily or otherwise;</p>
<p>(7) the visitor has been present at the dwelling for a substantial length of time prior to the arrest;</p>
<p>(8) the visitor stores his clothes or other possessions in the dwelling;</p>
<p>(9) the visitor has been granted by the owner exclusive use of a particular area of the dwelling;</p>
<p>(10) the visitor has the right to exclude other persons from the dwelling;</p>
<p>(11) the visitor is allowed to remain in the dwelling when the owner is absent; and</p>
<p>(12) the visitor has taken precautions to develop and maintain his privacy in the dwelling. Brief for Petitioner 21.</p>
<p>[5]  Of course, 2406 Fillmore need not be respondent's "home," temporary or otherwise, in order for him to enjoy a reasonable expectation of privacy there. "[T]he Fourth Amendment protects people, not places," <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967), and provides sanctuary for citizens wherever they have a legitimate expectation of privacy. <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#359" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 359</a></span>. Mr. Katz could complain because he had such an expectation in a telephone booth, not because it was his "home" for Fourth Amendment purposes. Similarly, if Olson had a reasonable expectation of privacy as a one-night guest, his warrantless seizure was unreasonable whether or not the upper unit at 2406 Fillmore was his home.</p>
<p>[6]  Olson, who had been staying at Ecker's home for several days before the robbery, spent the night of the robbery on the floor of the Bergstroms' home, with their permission. He had a change of clothes with him at the duplex.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Minnick v. Mississippi.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Minnick v. Mississippi"
type: case
citation: "498 U.S. 146 (1990)"
parallel_cite: "111 S. Ct. 486; 112 L. Ed. 2d 489"
neutral_cite: 1990 U.S. LEXIS 6118
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1990
date_decided: 1990-12-03
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1990-12-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Minnick v. Mississippi
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112513/minnick-v-mississippi/"
  cluster_id: 112513
  opinion_id: 112513
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Edwards v. Arizona]]", "[[Arizona v. Roberson]]", "[[Maryland v. Shatzer]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "edwards", "right-to-counsel", "invocation"]
holding: "Once counsel is invoked, Edwards bars police-initiated re-interrogation without counsel PRESENT — and that protection is not satisfied…"
lake:
  record_id: Minnick v. Mississippi
  status: verified
  projected_at: 2026-07-06
---

# Minnick v. Mississippi

*498 U.S. 146 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After his arrest, Minnick invoked his right to counsel during FBI questioning, and the interview stopped. He then consulted with appointed counsel. Days later, a state officer returned and, without counsel present, questioned him again; Minnick made incriminating statements.

## Issue
Whether the *[[Edwards v. Arizona|Edwards]]* bar on police-initiated interrogation after a request for counsel ends once the suspect has consulted with an attorney.

## Rule
No. "we now hold that when counsel is requested, interrogation must cease, and officials may not reinitiate interrogation without counsel present, whether or not the accused has consulted with his attorney." — 498 U.S. at 153. ^pin-153

## Application
Minnick invoked counsel during the FBI interview, so police could not reinitiate interrogation without counsel present. His intervening consultation with appointed counsel did not lift that protection; the later police-initiated questioning, conducted without counsel present, therefore violated the *[[Edwards v. Arizona|Edwards]]* rule, and his statements were inadmissible.

## Conclusion
Reversed; the statements were obtained in violation of *[[Edwards v. Arizona|Edwards]]* and could not be used.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Minnick* strengthens [[Edwards v. Arizona]] by holding that mere consultation with counsel does not end the bar; [[Maryland v. Shatzer]] later supplied a break-in-custody endpoint to the *[[Edwards v. Arizona|Edwards]]* protection.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *Minnick v. Mississippi*, 498 U.S. 146 (1990) — https://www.courtlistener.com/opinion/112513/minnick-v-mississippi/ — pinpoint: 153.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7c7606f5a219a4cc", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Minnick v. Mississippi"}, "payload": {"all": [{"cite": "498 U.S. 146", "page": "146", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "498"}, {"cite": "111 S. Ct. 486", "page": "486", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "111"}, {"cite": "112 L. Ed. 2d 489", "page": "489", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "112"}, {"cite": "1990 U.S. LEXIS 6118", "page": "6118", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1990"}], "display": "498 U.S. 146", "official": {"cite": "498 U.S. 146", "page": "146", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "498"}, "official_selection_present": true, "record_id": "Minnick v. Mississippi"}}
{"assertion_id": "b9eff4501b9b7fb3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-153", "record_id": "Minnick v. Mississippi"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-153", "pinpoint_status": "slip-only", "quote": "--- # Minnick v. Mississippi *498 U.S. 146 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After his arrest, Minnick invoked his right to counsel during FBI questioning, and the interview stopped. He then consulted with appointed counsel. Days later, a state officer returned and, without counsel present, questioned him again; Minnick made incriminating statements. ## Issue Whether the *Edwards* bar on police-initiated interrogation after a request for counsel ends once the suspect has consulted with an attorney. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "Minnick v. Mississippi", "star_marker": null}}
{"assertion_id": "ae68f64957059513", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Minnick v. Mississippi"}, "payload": {"as_of_content": "1990-12-03", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Minnick v. Mississippi", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Minnick v. Mississippi

```json
{
  "schema_version": "s2.v1",
  "record_id": "Minnick v. Mississippi",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Minnick v. Mississippi",
    "case_name_short": "Minnick",
    "case_name_full": "Minnick v. Mississippi",
    "input_case_name": "Minnick v. Mississippi",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-12-03",
    "year": 1990,
    "docket": null,
    "cluster_id": 112513,
    "lead_opinion_id": 112513,
    "sibling_ids": [
      112513,
      9432173,
      9432174
    ],
    "absolute_url": "/opinion/112513/minnick-v-mississippi/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9099703,
        "score": 20,
        "case_name": "Minnick v. Mississippi"
      },
      {
        "cluster_id": 9099702,
        "score": 20,
        "case_name": "Minnick v. Mississippi"
      },
      {
        "cluster_id": 9099554,
        "score": 20,
        "case_name": "Minnick v. Mississippi"
      },
      {
        "cluster_id": 9099553,
        "score": 20,
        "case_name": "Minnick v. Mississippi"
      },
      {
        "cluster_id": 9096960,
        "score": 20,
        "case_name": "Minnick v. Mississippi"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "498 U.S. 146",
      "volume": "498",
      "reporter": "U.S.",
      "page": "146",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "111 S. Ct. 486",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "486",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "112 L. Ed. 2d 489",
        "volume": "112",
        "reporter": "L. Ed. 2d",
        "page": "489",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 6118",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "6118",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "498 U.S. 146",
        "volume": "498",
        "reporter": "U.S.",
        "page": "146",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "111 S. Ct. 486",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "486",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "112 L. Ed. 2d 489",
        "volume": "112",
        "reporter": "L. Ed. 2d",
        "page": "489",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 6118",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "6118",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "498 U.S. 146",
    "official_selection": {
      "court_class": "scotus",
      "selected": "498 U.S. 146",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-153",
      "page": null,
      "quote": "--- # Minnick v. Mississippi *498 U.S. 146 (1990)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After his arrest, Minnick invoked his right to counsel during FBI questioning, and the interview stopped. He then consulted with appointed counsel. Days later, a state officer returned and, without counsel present, questioned him again; Minnick made incriminating statements. ## Issue Whether the *Edwards* bar on police-initiated interrogation after a request for counsel ends once the suspect has consulted with an attorney. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1990-12-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Minnick v. Mississippi",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. DeJong",
          "cluster_id": 2669581,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hodson v. State",
          "cluster_id": 2542781,
          "cite": [
            "350 S.W.3d 169",
            "2011 WL 1796088"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Colby Alan Palmer",
          "cluster_id": 4472471,
          "cite": [
            "791 N.W.2d 840",
            "2010 Iowa Sup. LEXIS 144"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pecina v. State",
          "cluster_id": 2292956,
          "cite": [
            "326 S.W.3d 249",
            "2010 Tex. App. LEXIS 5631",
            "2010 WL 2825663"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Flores v. State",
          "cluster_id": 1871985,
          "cite": [
            "299 S.W.3d 843",
            "2009 WL 3466009"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Plugh",
          "cluster_id": 2496,
          "cite": [
            "576 F.3d 135",
            "2009 U.S. App. LEXIS 16979",
            "2009 WL 2341966"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Martinez v. State",
          "cluster_id": 1450662,
          "cite": [
            "275 S.W.3d 29",
            "2008 WL 2840151"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gobert",
          "cluster_id": 1947904,
          "cite": [
            "244 S.W.3d 861",
            "2008 Tex. App. LEXIS 742",
            "2008 WL 269448"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Van Hook v. Carl S. Anderson, Warden",
          "cluster_id": 793987,
          "cite": [
            "444 F.3d 830",
            "2006 U.S. App. LEXIS 9628",
            "2006 WL 997203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "in the Matter of H v.",
          "cluster_id": 2847659,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gregory Johnson, A/K/A Little Greg, United States of America v. Gregory Johnson, A/K/A Little Greg",
          "cluster_id": 789459,
          "cite": [
            "400 F.3d 187",
            "2005 WL 526889"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 117863,
          "cite": [
            "129 L. Ed. 2d 362",
            "114 S. Ct. 2350",
            "512 U.S. 452",
            "1994 U.S. LEXIS 4827"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNeil v. Wisconsin",
          "cluster_id": 112622,
          "cite": [
            "115 L. Ed. 2d 158",
            "111 S. Ct. 2204",
            "501 U.S. 171",
            "1991 U.S. LEXIS 3483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dinkins v. State",
          "cluster_id": 1688238,
          "cite": [
            "894 S.W.2d 330",
            "1995 Tex. Crim. App. LEXIS 9",
            "1995 WL 40331"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Acevedo",
          "cluster_id": 112608,
          "cite": [
            "114 L. Ed. 2d 619",
            "111 S. Ct. 1982",
            "500 U.S. 565",
            "1991 U.S. LEXIS 3016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Muniz v. State",
          "cluster_id": 1471480,
          "cite": [
            "851 S.W.2d 238",
            "1993 Tex. Crim. App. LEXIS 5",
            "1993 WL 871"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Waidla",
          "cluster_id": 1316339,
          "cite": [
            "996 P.2d 46",
            "94 Cal. Rptr. 2d 396",
            "22 Cal. 4th 690",
            "22 Cal. 690",
            "2000 Daily Journal DAR 3605",
            "2000 Cal. Daily Op. Serv. 2687",
            "2000 Cal. LEXIS 2229"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Montejo v. Louisiana",
          "cluster_id": 145873,
          "cite": [
            "173 L. Ed. 2d 955",
            "129 S. Ct. 2079",
            "556 U.S. 778",
            "2009 U.S. LEXIS 3973"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Shatzer",
          "cluster_id": 1734,
          "cite": [
            "175 L. Ed. 2d 1045",
            "130 S. Ct. 1213",
            "559 U.S. 98",
            "2010 U.S. LEXIS 1899"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Taylor v. State",
          "cluster_id": 1936088,
          "cite": [
            "672 So. 2d 1246",
            "1996 WL 197700"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradford",
          "cluster_id": 1407706,
          "cite": [
            "14 Cal. 4th 1005",
            "929 P.2d 544",
            "97 Daily Journal DAR 899",
            "97 Cal. Daily Op. Serv. 520",
            "60 Cal. Rptr. 2d 225",
            "1997 Cal. LEXIS 9"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holland v. State",
          "cluster_id": 1913318,
          "cite": [
            "705 So. 2d 307",
            "1997 WL 562038"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Willie v. State",
          "cluster_id": 1706565,
          "cite": [
            "585 So. 2d 660",
            "1991 WL 142136"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Traylor v. State",
          "cluster_id": 1765408,
          "cite": [
            "596 So. 2d 957",
            "1992 WL 4873"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Balfour v. State",
          "cluster_id": 1858937,
          "cite": [
            "598 So. 2d 731",
            "1992 WL 64497"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ladner v. State",
          "cluster_id": 1106169,
          "cite": [
            "584 So. 2d 743",
            "1991 WL 134881"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Martin",
          "cluster_id": 2445914,
          "cite": [
            "5 A.3d 177",
            "607 Pa. 165",
            "2010 Pa. LEXIS 2866"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Simmons v. State",
          "cluster_id": 1652484,
          "cite": [
            "805 So. 2d 452",
            "2001 WL 1587933"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Duplantis v. State",
          "cluster_id": 1659824,
          "cite": [
            "644 So. 2d 1235",
            "1994 WL 590825"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Green",
          "cluster_id": 1730571,
          "cite": [
            "655 So. 2d 272",
            "1995 WL 312446"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Leonard David Griffin",
          "cluster_id": 553880,
          "cite": [
            "922 F.2d 1343",
            "1990 U.S. App. LEXIS 22396",
            "1990 WL 212298"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. State",
          "cluster_id": 1868949,
          "cite": [
            "684 So. 2d 1213",
            "1996 WL 694199"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Abram v. State",
          "cluster_id": 1096122,
          "cite": [
            "606 So. 2d 1015",
            "1992 WL 223914"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lester v. State",
          "cluster_id": 1136432,
          "cite": [
            "692 So. 2d 755",
            "1997 WL 167015"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112513 OR 9432173 OR 9432174) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDM4OTYwMDAwMDAwJnM9MTY3MDIxMyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112513+OR+9432173+OR+9432174%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112513 OR 9432173 OR 9432174)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xODUmcz0xNzQ3MDk5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112513+OR+9432173+OR+9432174%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112513 OR 9432173 OR 9432174)",
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
    "complete_query": "cites:(112513 OR 9432173 OR 9432174)",
    "indexed_citing_opinions": 541,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112513,
        "count": 492,
        "count_source": "search"
      },
      {
        "opinion_id": 9432173,
        "count": 63,
        "count_source": "search"
      },
      {
        "opinion_id": 9432174,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 848,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/minnick-v-mississippi.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc0NDk5MTkmcz0xMDI4MDE1MSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28112513+OR+9432173+OR+9432174%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112513,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 107209,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 109309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 110065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 110987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 111288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 111355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 112100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 112127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 112385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 1140464,
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
    "date_created": "2026-07-05T14:06:13Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:06:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:06:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:09:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:06:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Minnick v. Mississippi

```
<div>
<center><b><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">498 U.S. 146</a></span> (1990)</b></center>
<center><h1>MINNICK<br>
v.<br>
MISSISSIPPI.</h1></center>
<center>No. 89-6332.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued October 3, 1990.</center>
<center>Decided December 3, 1990.</center>
CERTIORARI TO THE SUPREME COURT OF MISSISSIPPI.
<p><span class="star-pagination">*147</span> <i>Floyd Abrams</i> argued the cause for petitioner. With him on the briefs were <i>Anthony Paduano</i> and <i>Clive A. Stafford Smith.</i></p>
<p><i>Marvin L. White, Jr.,</i> Assistant Attorney General of Mississippi, argued the cause for respondent. With him on the brief was <i>Mike Moore,</i> Attorney General.<sup>[*]</sup></p>
<p>JUSTICE KENNEDY delivered the opinion of the Court.</p>
<p>To protect the privilege against self-incrimination guaranteed by the Fifth Amendment, we have held that the police must terminate interrogation of an accused in custody if the accused requests the assistance of counsel. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 474</a></span> (1966). We reinforced the protections of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477, 484-485</a></span> (1981), which held that once the accused requests counsel, officials may not reinitiate questioning "until counsel has been made available" to him. The issue in the case before us is whether <i>Edwards'</i> protection ceases once the suspect has consulted with an attorney.</p>
<p><span class="star-pagination">*148</span> Petitioner Robert Minnick and fellow prisoner James Dyess escaped from a county jail in Mississippi and, a day later, broke into a mobile home in search of weapons. In the course of the burglary they were interrupted by the arrival of the trailer's owner, Ellis Thomas, accompanied by Lamar Lafferty and Lafferty's infant son. Dyess and Minnick used the stolen weapons to kill Thomas and the senior Lafferty. Minnick's story is that Dyess murdered one victim and forced Minnick to shoot the other. Before the escapees could get away, two young women arrived at the mobile home. They were held at gunpoint, then bound hand and foot. Dyess and Minnick fled in Thomas' truck, abandoning the vehicle in New Orleans. The fugitives continued to Mexico, where they fought, and Minnick then proceeded alone to California. Minnick was arrested in Lemon Grove, California, on a Mississippi warrant, some four months after the murders.</p>
<p>The confession at issue here resulted from the last interrogation of Minnick while he was held in the San Diego jail, but we first recount the events which preceded it. Minnick was arrested on Friday, August 22, 1986. Petitioner testified that he was mistreated by local police during and after the arrest. The day following the arrest, Saturday, two Federal Bureau of Investigation (FBI) agents came to the jail to interview him. Petitioner testified that he refused to go to the interview, but was told he would "have to go down or else." App. 45. The FBI report indicates that the agents read petitioner his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, and that he acknowledged he understood his rights. He refused to sign a rights waiver form, however, and said he would not answer "very many" questions. Minnick told the agents about the jailbreak and the flight, and described how Dyess threatened and beat him. Early in the interview, he sobbed "[i]t was my life or theirs," but otherwise he hesitated to tell what happened at the trailer. The agents reminded him he did not have to answer questions without a lawyer present. According to the report, "Minnick stated `Come back Monday when I have a lawyer,' <span class="star-pagination">*149</span> and stated that he would make a more complete statement then with his lawyer present." App. 16. The FBI interview ended.</p>
<p>After the FBI interview, an appointed attorney met with petitioner. Petitioner spoke with the lawyer on two or three occasions, though it is not clear from the record whether all of these conferences were in person.</p>
<p>On Monday, August 25, Deputy Sheriff J. C. Denham of Clarke County, Mississippi, came to the San Diego jail to question Minnick. Minnick testified that his jailers again told him he would "have to talk" to Denham and that he "could not refuse." <i>Id.,</i> at 45. Denham advised petitioner of his rights, and petitioner again declined to sign a rights waiver form. Petitioner told Denham about the escape and then proceeded to describe the events at the mobile home. According to petitioner, Dyess jumped out of the mobile home and shot the first of the two victims, once in the back with a shotgun and once in the head with a pistol. Dyess then handed the pistol to petitioner and ordered him to shoot the other victim, holding the shotgun on petitioner until he did so. Petitioner also said that when the two girls arrived, he talked Dyess out of raping or otherwise hurting them.</p>
<p>Minnick was tried for murder in Mississippi. He moved to suppress all statements given to the FBI or other police officers, including Denham. The trial court denied the motion with respect to petitioner's statements to Denham, but suppressed his other statements. Petitioner was convicted on two counts of capital murder and sentenced to death.</p>
<p>On appeal, petitioner argued that the confession to Denham was taken in violation of his rights to counsel under the Fifth and Sixth Amendments. The Mississippi Supreme Court rejected the claims. With respect to the Fifth Amendment aspect of the case, the court found "the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> bright-line rule as to initiation" inapplicable. <span class="citation" data-id="1140464"><a href="/opinion/1140464/minnick-v-state/#83" aria-description="Citation for case: Minnick v. State">551 So. 2d 77, 83</a></span> (1988). Relying on language in <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> indicating that the bar on interrogating the accused after a request for counsel <span class="star-pagination">*150</span> applies "`until counsel has been made available to him,'" <i>ibid.,</i> quoting <i>Edwards</i> v. <i>Arizona, supra,</i> at 484-485, the court concluded that "[s]ince counsel was made available to Minnick, his Fifth Amendment right to counsel was satisfied." <span class="citation" data-id="1140464"><a href="/opinion/1140464/minnick-v-state/#83" aria-description="Citation for case: Minnick v. State">551 So. 2d, at 83</a></span>. The court also rejected the Sixth Amendment claim, finding that petitioner waived his Sixth Amendment right to counsel when he spoke with Denham. <span class="citation" data-id="1140464"><a href="/opinion/1140464/minnick-v-state/#83" aria-description="Citation for case: Minnick v. State"><i>Id.,</i> at 83-85</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./495/903/">495 U. S. 903</a></span> (1990), and, without reaching any Sixth Amendment implications in the case, we decide that the Fifth Amendment protection of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> is not terminated or suspended by consultation with counsel.</p>
<p>In <i>Miranda</i> v. <i>Arizona, supra,</i> at 474, we indicated that once an individual in custody invokes his right to counsel, interrogation "must cease until an attorney is present"; at that point, "the individual must have an opportunity to confer with the attorney and to have him present during any subsequent questioning." <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> gave force to these admonitions, finding it "inconsistent with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and its progeny for the authorities, at their instance, to reinterrogate an accused in custody if he has clearly asserted his right to counsel." <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#485" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 485</a></span>. We held that "when an accused has invoked his right to have counsel present during custodial interrogation, a valid waiver of that right cannot be established by showing only that he responded to further police-initiated custodial interrogation even if he has been advised of his rights." <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona"><i>Id.,</i> at 484</a></span>. Further, an accused who requests an attorney, "having expressed his desire to deal with the police only through counsel, is not subject to further interrogation by the authorities until counsel has been made available to him, unless the accused himself initiates further communication, exchanges, or conversations with the police." <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona"><i>Id.,</i> at 484-485</a></span>.</p>
<p><i>Edwards</i> is "designed to prevent police from badgering a defendant into waiving his previously asserted <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights." <i>Michigan</i> v. <i>Harvey,</i> <span class="citation" data-id="9431937"><a href="/opinion/112385/michigan-v-harvey/#350" aria-description="Citation for case: Michigan v. Harvey">494 U. S. 344, 350</a></span> (1990). <span class="star-pagination">*151</span> See also <i>Smith v. Illinois,</i> <span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#98" aria-description="Citation for case: Smith v. Illinois">469 U. S. 91, 98</a></span> (1984). The rule ensures that any statement made in subsequent interrogation is not the result of coercive pressures. <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> conserves judicial resources which would otherwise be expended in making difficult determinations of voluntariness, and implements the protections of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in practical and straightforward terms.</p>
<p>The merit of the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> decision lies in the clarity of its command and the certainty of its application. We have confirmed that the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> rule provides "`clear and unequivocal' guidelines to the law enforcement profession." <i>Arizona v. Roberson,</i> <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/#682" aria-description="Citation for case: Arizona v. Roberson">486 U. S. 675, 682</a></span> (1988). Cf. <i>Moran v. Burbine,</i> <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#425" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 425-426</a></span> (1986). Even before <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>,</i> we noted that <i>Miranda's</i> "relatively rigid requirement that interrogation must cease upon the accused's request for an attorney . . . has the virtue of informing police and prosecutors with specificity as to what they may do in conducting custodial interrogation, and of informing courts under what circumstances statements obtained during such interrogation are not admissible. This gain in specificity, which benefits the accused and the State alike, has been thought to outweigh the burdens that the decision in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> imposes on law enforcement agencies and the courts by requiring the suppression of trustworthy and highly probative evidence even though the confession might be voluntary under traditional Fifth Amendment analysis." <i>Fare</i> v. <i>Michael C.,</i> <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#718" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 718</a></span> (1979). This pre-<span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona"><i>Edwards</i></a></span> explanation applies as well to <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> and its progeny. <i>Arizona</i> v. <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/#681" aria-description="Citation for case: Arizona v. Roberson"><i>Roberson, supra,</i> at 681-682</a></span>.</p>
<p>The Mississippi Supreme Court relied on our statement in <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> that an accused who invokes his right to counsel "is not subject to further interrogation by the authorities until counsel has been made available to him . . . ." <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484-485</a></span>. We do not interpret this language to mean, as the Mississippi court thought, that the protection of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> terminates once counsel has consulted with the suspect. In <span class="star-pagination">*152</span> context, the requirement that counsel be "made available" to the accused refers to more than an opportunity to consult with an attorney outside the interrogation room.</p>
<p>In <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>,</i> we focused on <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s instruction that when the accused invokes his right to counsel, "the interrogation must cease until an attorney is <i>present,"</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 474</a></span> (emphasis added), agreeing with Edwards' contention that he had not waived his right "to have counsel <i>present</i> during custodial interrogation." <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#482" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 482</a></span> (emphasis added). In the sentence preceding the language quoted by the Mississippi Supreme Court, we referred to the "right to have counsel <i>present</i> during custodial interrogation," and in the sentence following, we again quoted the phrase "`interrogation must cease until an attorney is <i>present'"</i> from <i>Miranda.</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484-485</a></span> (emphasis added). The full sentence relied on by the Mississippi Supreme Court, moreover, says: "We further hold that an accused, such as Edwards, <i>having expressed his desire to deal with the police only through counsel,</i> is not subject to further interrogation by the authorities until counsel has been made available to him, unless the accused himself initiates further communication, exchanges, or conversations with the police." <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Ibid.</a></span></i> (emphasis added).</p>
<p>Our emphasis on counsel's <i>presence</i> at interrogation is not unique to <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>.</i> It derives from <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> where we said that in the cases before us "[t]he presence of counsel . . . would be the adequate protective device necessary to make the process of police interrogation conform to the dictates of the [Fifth Amendment] privilege. His presence would insure that statements made in the government-established atmosphere are not the product of compulsion." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#466" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 466</a></span>. See <i>Fare</i> v. <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#719" aria-description="Citation for case: Fare v. Michael C."><i>Michael C., supra,</i> at 719</a></span>. Our cases following <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> have interpreted the decision to mean that the authorities may not initiate questioning of the accused in counsel's absence. Writing for a plurality of the Court, for instance, then-JUSTICE REHNQUIST described the holding of <span class="star-pagination">*153</span> <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> to be "that subsequent incriminating statements made <i>without [Edwards'] attorney present</i> violated the rights secured to the defendant by the Fifth and Fourteenth Amendments to the United States Constitution." <i>Oregon v. Bradshaw,</i> <span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1043" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S. 1039, 1043</a></span> (1983) (emphasis added). See also <i>Arizona</i> v. <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/#680" aria-description="Citation for case: Arizona v. Roberson"><i>Roberson, supra,</i> at 680</a></span> ("The rule of the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> case came as a corollary to <i>Miranda's</i> admonition that `[i]f the individual states that he wants an attorney, the interrogation must cease until an attorney is present"); <i>Shea v. Louisiana,</i> <span class="citation" data-id="9429912"><a href="/opinion/111355/shea-v-louisiana/#52" aria-description="Citation for case: Shea v. Louisiana">470 U. S. 51, 52</a></span> (1985) ("In <i>Edwards</i> v. <i>Arizona</i><i>,</i>. . . this Court ruled that a criminal defendant's rights under the Fifth and Fourteenth Amendments were violated by the use of his confession obtained by police-instigated interrogationwithout counsel presentafter he requested an attorney"). These descriptions of <i>Edwards'</i> holding are consistent with our statement that "[p]reserving the integrity of an accused's choice to communicate with police only through counsel is the essence of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> and its progeny." <i>Patterson v. Illinois,</i> <span class="citation" data-id="9431404"><a href="/opinion/112127/patterson-v-illinois/#291" aria-description="Citation for case: Patterson v. Illinois">487 U. S. 285, 291</a></span> (1988). In our view, a fair reading of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> and subsequent cases demonstrates that we have interpreted the rule to bar police-initiated interrogation unless the accused has counsel with him at the time of questioning. Whatever the ambiguities of our earlier cases on this point, we now hold that when counsel is requested, interrogation must cease, and officials may not reinitiate interrogation without counsel present, whether or not the accused has consulted with his attorney.</p>
<p>We consider our ruling to be an appropriate and necessary application of the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> rule. A single consultation with an attorney does not remove the suspect from persistent attempts by officials to persuade him to waive his rights, or from the coercive pressures that accompany custody and that may increase as custody is prolonged. The case before us well illustrates the pressures, and abuses, that may be concomitants of custody. Petitioner testified that though he resisted, he was required to submit to both the FBI and the <span class="star-pagination">*154</span> Denham interviews. In the latter instance, the compulsion to submit to interrogation followed petitioner's unequivocal request during the FBI interview that questioning cease until counsel was present. The case illustrates also that consultation is not always effective in instructing the suspect of his rights. One plausible interpretation of the record is that petitioner thought he could keep his admissions out of evidence by refusing to sign a formal waiver of rights. If the authorities had complied with Minnick's request to have counsel present during interrogation, the attorney could have corrected Minnick's misunderstanding, or indeed counseled him that he need not make a statement at all. We decline to remove protection from police-initiated questioning based on isolated consultations with counsel who is absent when the interrogation resumes.</p>
<p>The exception to <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> here proposed is inconsistent with <i>Edwards'</i> purpose to protect the suspect's right to have counsel present at custodial interrogation. It is inconsistent as well with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> where we specifically rejected respondent's theory that the opportunity to consult with one's attorney would substantially counteract the compulsion created by custodial interrogation. We noted in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> that "[e]ven preliminary advice given to the accused by his own attorney can be swiftly overcome by the secret interrogation process. Thus the need for counsel to protect the Fifth Amendment privilege comprehends not merely a right to consult with counsel prior to questioning, but also to have counsel present during any questioning if the defendant so desires." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#470" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 470</a></span> (citation omitted).</p>
<p>The exception proposed, furthermore, would undermine the advantages flowing from <i>Edwards'</i> "clear and unequivocal" character. Respondent concedes that even after consultation with counsel, a second request for counsel should reinstate the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> protection. We are invited by this formulation to adopt a regime in which <i>Edwards'</i> protection could pass in and out of existence multiple times prior to arraignment, <span class="star-pagination">*155</span> at which point the same protection might reattach by virtue of our Sixth Amendment jurisprudence, see <i>Michigan v. Jackson,</i> <span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625</a></span> (1986). Vagaries of this sort spread confusion through the justice system and lead to a consequent loss of respect for the underlying constitutional principle.</p>
<p>In addition, adopting the rule proposed would leave far from certain the sort of consultation required to displace <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>.</i> Consultation is not a precise concept, for it may encompass variations from a telephone call to say that the attorney is en route, to a hurried interchange between the attorney and client in a detention facility corridor, to a lengthy in-person conference in which the attorney gives full and adequate advice respecting all matters that might be covered in further interrogations. And even with the necessary scope of consultation settled, the officials in charge of the case would have to confirm the occurrence and, possibly, the extent of consultation to determine whether further interrogation is permissible. The necessary inquiries could interfere with the attorney-client privilege.</p>
<p>Added to these difficulties in definition and application of the proposed rule is our concern over its consequence that the suspect whose counsel is prompt would lose the protection of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>,</i> while the one whose counsel is dilatory would not. There is more than irony to this result. There is a strong possibility that it would distort the proper conception of the attorney's duty to the client and set us on a course at odds with what ought to be effective representation.</p>
<p>Both waiver of rights and admission of guilt are consistent with the affirmation of individual responsibility that is a principle of the criminal justice system. It does not detract from this principle, however, to insist that neither admissions nor waivers are effective unless there are both particular and systemic assurances that the coercive pressures of custody were not the inducing cause. The <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> rule sets forth a specific standard to fulfill these purposes, and we have declined <span class="star-pagination">*156</span> to confine it in other instances. See <i>Arizona v. Roberson,</i> <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">486 U. S. 675</a></span> (1988). It would detract from the efficacy of the rule to remove its protections based on consultation with counsel.</p>
<p><i>Edwards</i> does not foreclose finding a waiver of Fifth Amendment protections after counsel has been requested, provided the accused has initiated the conversation or discussions with the authorities; but that is not the case before us. There can be no doubt that the interrogation in question was initiated by the police; it was a formal interview which petitioner was compelled to attend. Since petitioner made a specific request for counsel before the interview, the police-initiated interrogation was impermissible. Petitioner's statement to Denham was not admissible at trial.</p>
<p>The judgment is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE SOUTER took no part in the consideration or decision of this case.</p>
<p>JUSTICE SCALIA, with whom THE CHIEF JUSTICE joins, dissenting.</p>
<p>The Court today establishes an irrebuttable presumption that a criminal suspect, after invoking his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> right to counsel, can <i>never</i> validly waive that right during any police-initiated encounter, even after the suspect has been provided multiple <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and has actually consulted his attorney. This holding builds on foundations already established in <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981), but "the rule of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> is our rule, not a constitutional command; and it is our obligation to justify its expansion." <i>Arizona v. Roberson,</i> <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/#688" aria-description="Citation for case: Arizona v. Roberson">486 U. S. 675, 688</a></span> (1988) (KENNEDY, J., dissenting). Because I see no justification for applying the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> irrebuttable presumption when a criminal suspect has actually consulted with his attorney, I respectfully dissent.</p>
<p></p>
<h2>
<span class="star-pagination">*157</span> I</h2>
<p>Some recapitulation of pertinent facts is in order, given the Court's contention that "[t]he case before us well illustrates the pressures, and abuses, that may be concomitants of custody." <i>Ante,</i> at 153. It is undisputed that the FBI agents who first interviewed Minnick on Saturday, August 23, 1986, advised him of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights before any questioning began. Although he refused to sign a waiver form, he agreed to talk to the agents, and described his escape from prison in Mississippi and the ensuing events. When he came to what happened at the trailer, however, Minnick hesitated. The FBI agents then reminded him that he did not have to answer questions without a lawyer present. Minnick indicated that he would finish his account on Monday, when he had a lawyer, and the FBI agents terminated the interview forthwith.</p>
<p>Minnick was then provided with an attorney, with whom he consulted several times over the weekend. As Minnick testified at a subsequent suppression hearing:</p>
<blockquote>"I talked to [my attorney] two different times andit might have been three different times . . . . He told me that first day that he was my lawyer and that he was appointed to me and to not to talk to nobody and not tell nobody nothing and to not sign no waivers and not sign no extradition papers or sign anything and that he was going to get a court order to have any of the policeI advised him of the FBI talking to me and he advised me not to tell anybody anything that he was going to get a court order drawn up to restrict anybody talking to me outside of the San Diego Police Department." App. 46-47.</blockquote>
<p>On Monday morning, Minnick was interviewed by Deputy Sheriff J. C. Denham, who had come to San Diego from Mississippi. Before the interview, Denham reminded Minnick of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. Minnick again refused to sign a <span class="star-pagination">*158</span> waiver form, but he did talk with Denham and did not ask for his attorney. As Minnick recalled at the hearing, he and Denham</p>
<blockquote>"went through several different conversations about first, about how everybody was back in the county jail and what everybody was doing, had he heard from Mama and had he went and talked to Mama and had he seen my brother, Tracy, and several different other questions pertaining to such things as that. And, we went off into how the escape went down at the county jail . . . ." App. 50.</blockquote>
<p>Minnick then proceeded to describe his participation in the double murder at the trailer.</p>
<p>Minnick was later extradited and tried for murder in Mississippi. Before trial, he moved to suppress the statements he had given the FBI agents and Denham in the San Diego jail. The trial court granted the motion with respect to the statements made to the FBI agents, but ordered a hearing on the admissibility of the statements made to Denham. After receiving testimony from both Minnick and Denham, the court concluded that Minnick's confession had been "freely and voluntarily given from the evidence beyond a reasonable doubt," <i>id.,</i> at 25, and allowed Denham to describe Minnick's confession to the jury.</p>
<p>The Court today reverses the trial court's conclusion. It holds that, because Minnick had asked for counsel during the interview with the FBI agents, he could notas a matter of lawvalidly waive the right to have counsel present during the conversation initiated by Denham. That Minnick's original request to see an attorney had been honored, that Minnick had consulted with his attorney on several occasions, and that the attorney had specifically warned Minnick not to speak to the authorities, are irrelevant. That Minnick was familiar with the criminal justice system in general or <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings in particular (he had previously been convicted of robbery in Mississippi and assault with a deadly <span class="star-pagination">*159</span> weapon in California) is also beside the point. The confession must be suppressed, not because it was "compelled," nor even because it was obtained from an individual who could realistically be assumed to be unaware of his rights, but simply because this Court sees fit to prescribe as a "systemic assuranc[e]," <i>ante,</i> at 155, that a person in custody who has once asked for counsel cannot thereafter be approached by the police unless counsel is present. Of course the Constitution's proscription of compelled testimony does not remotely authorize this incursion upon state practices; and even our recent precedents are not a valid excuse.</p>
<p></p>
<h2>II</h2>
<p>In <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), this Court declared that a criminal suspect has a right to have counsel present during custodial interrogation, as a prophylactic assurance that the "inherently compelling pressures," <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 467</a></span>, of such interrogation will not violate the Fifth Amendment. But <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> did not hold that these "inherently compelling pressures" precluded a suspect from waiving his right to have counsel present. On the contrary, the opinion recognized that a State could establish that the suspect "knowingly and intelligently waived . . . his right to retained or appointed counsel." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 475</a></span>. For this purpose, the Court expressly adopted the "high standar[d] of proof for the waiver of constitutional rights," <i>ibid.,</i> set forth in <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458</a></span> (1938).</p>
<p>The <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">Zerbst</a></span></i> waiver standard, and the means of applying it, are familiar: Waiver is "an intentional relinquishment or abandonment of a known right or privilege," <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst"><i>id.,</i> at 464</a></span>; and whether such a relinquishment or abandonment has occurred depends "in each case, upon the particular facts and circumstances surrounding that case, including the background, experience, and conduct of the accused," <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">ibid.</a></span></i> We have applied the <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">Zerbst</a></span></i> approach in many contexts where a State bears the burden of showing a waiver of constitutional criminal <span class="star-pagination">*160</span> procedural rights. See, <i>e. g., </i><i>Faretta</i> v. <i>California,</i> <span class="citation" data-id="9426191"><a href="/opinion/109309/faretta-v-california/#835" aria-description="Citation for case: Faretta v. California">422 U. S. 806, 835</a></span> (1975) (right to the assistance of counsel at trial); <i>Brookhart</i> v. <i>Janis,</i> <span class="citation" data-id="107209"><a href="/opinion/107209/brookhart-v-janis/#4" aria-description="Citation for case: Brookhart v. Janis">384 U. S. 1, 4</a></span> (1966) (right to confront adverse witnesses); <i>Adams</i> v. <i>United States ex rel. McCann,</i> <span class="citation" data-id="9419274"><a href="/opinion/103735/adams-v-united-states-ex-rel-mccann/#275" aria-description="Citation for case: Adams v. United States Ex Rel. McCann">317 U. S. 269, 275-280</a></span> (1942) (right to trial by jury).</p>
<p>Notwithstanding our acknowledgment that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights are "not themselves rights protected by the Constitution but. . . instead measures to insure that the right against compulsory self-incrimination [is] protected," <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 444</a></span> (1974), we have adhered to the principle that nothing less than the <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">Zerbst</a></span></i> standard for the waiver of constitutional rights applies to the waiver of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. Until <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>,</i> however, we refrained from imposing on the States a <i>higher</i> standard for the waiver of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. For example, in <i>Michigan</i> v. <i>Mosley,</i> <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96</a></span> (1975), we rejected a proposed irrebuttable presumption that a criminal suspect, after invoking the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> right to remain silent, could not validly waive the right during any subsequent questioning by the police. In <i>North Carolina</i> v. <i>Butler,</i> <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369</a></span> (1979), we rejected a proposed rule that waivers of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights must be deemed involuntary absent an explicit assertion of waiver by the suspect. And in <i>Fare</i> v. <i>Michael C.,</i> <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#723" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 723-727</a></span> (1979), we declined to hold that waivers of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights by juveniles are <i>per se</i> involuntary.</p>
<p><i>Edwards,</i> however, broke with this approach, holding that a defendant's waiver of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> right to counsel, made in the course of a police-initiated encounter after he had requested counsel but before counsel had been provided, was <i>per se</i> involuntary. The case stands as a solitary exception to our waiver jurisprudence. It does, to be sure, have the desirable consequences described in today's opinion. In the narrow context in which it applies, it provides 100% assurance against confessions that are "the result of coercive pressures," <i>ante,</i> at 151; it "`prevent[s] police from badgering a <span class="star-pagination">*161</span> defendant,'" <i>ante,</i> at 150 (quoting <i>Michigan</i> v. <i>Harvey,</i> <span class="citation" data-id="9431937"><a href="/opinion/112385/michigan-v-harvey/#350" aria-description="Citation for case: Michigan v. Harvey">494 U. S. 344, 350</a></span> (1990)); it "conserves judicial resources which would otherwise be expended in making difficult determinations of voluntariness," <i>ante,</i> at 151; and it provides "`"clear and unequivocal" guidelines to the law enforcement profession,'" <i><span class="citation" data-id="9431937"><a href="/opinion/112385/michigan-v-harvey/" aria-description="Citation for case: Michigan v. Harvey">ibid.</a></span></i> (quoting <i>Arizona</i> v. <i>Roberson,</i> <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/#682" aria-description="Citation for case: Arizona v. Roberson">486 U. S., at 682</a></span>). But so would a rule that simply excludes all confessions by all persons in police custody. The value of any prophylactic rule (assuming the authority to adopt a prophylactic rule) must be assessed not only on the basis of what is gained, but also on the basis of what is lost. In all other contexts we have thought the above-described consequences of abandoning <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">Zerbst</a></span></i> outweighed by "`the need for police questioning as a tool for effective enforcement of criminal laws,'" <i>Moran v. Burbine,</i> <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#426" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 426</a></span> (1986). "Admissions of guilt," we have said, "are more than merely `desirable'; they are essential to society's compelling interest in finding, convicting, and punishing those who violate the law." <i><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">Ibid.</a></span></i> (citation omitted).</p>
<p></p>
<h2>III</h2>
<p>In this case, of course, we have not been called upon to reconsider <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>,</i> but simply to determine whether its irrebuttable presumption should continue after a suspect has actually consulted with his attorney. Whatever justifications might support <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> are even less convincing in this context.</p>
<p>Most of the Court's discussion of <i>Edwardswhich</i> stresses repeatedly, in various formulations, the case's emphasis upon the "right `to have counsel <i>present</i> during custodial interrogation,'" <i>ante,</i> at 152, quoting <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#482" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 482</a></span> (emphasis added by the Court)is beside the point. The existence and the importance of the <i>Miranda-created</i> right "to have counsel <i>present"</i> are unquestioned here. What <i>is</i> questioned is why a State should not be given the opportunity to prove (under <i>Zerbst)</i> that the right was <i>voluntarily waived</i> by a suspect who, after having been read his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights twice and <span class="star-pagination">*162</span> having consulted with counsel at least twice, chose to speak to a police officer (and to admit his involvement in two murders) without counsel present.</p>
<p><i>Edwards</i> did not assert the principle that no waiver of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> right "to have counsel <i>present"</i> is possible. It simply adopted the presumption that no waiver is <i>voluntary</i> in certain circumstances, and the issue before us today is how broadly those circumstances are to be defined. They should not, in my view, extend beyond the circumstances present in <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> itselfwhere the suspect in custody asked to consult an attorney and was interrogated before that attorney had ever been provided. In those circumstances, the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> rule rests upon an assumption similar to that of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> itself: that when a suspect in police custody is first questioned he is likely to be ignorant of his rights and to feel isolated in a hostile environment. This likelihood is thought to justify special protection against unknowing or coerced waiver of rights. After a suspect has seen his request for an attorney honored, however, and has actually spoken with that attorney, the probabilities change. The suspect then knows that he has an advocate on his side, and that the police will permit him to consult that advocate. He almost certainly also has a heightened awareness (above what the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning itself will provide) of his right to remain silentsince at the earliest opportunity "any lawyer worth his salt will tell the suspect in no uncertain terms to make no statement to the police under any circumstances." <i>Watts v. Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#59" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 59</a></span> (1949) (opinion of Jackson, J.).</p>
<p>Under these circumstances, an irrebuttable presumption that any police-prompted confession is the result of ignorance of rights, or of coercion, has no genuine basis in fact. After the first consultation, therefore, the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> exclusionary rule should cease to apply. Does this mean, as the Court implies, that the police will thereafter have license to "badger" the suspect? Only if all one means by "badger" is asking, without such insistence or frequency as would constitute coercion, <span class="star-pagination">*163</span> whether he would like to reconsider his decision not to confess. Nothing in the Constitution (the only basis for our intervention here) prohibits such inquiry, which may often produce the desirable result of a voluntary confession. If and when postconsultation police inquiry becomes so protracted or threatening as to constitute coercion, the <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">Zerbst</a></span></i> standard will afford the needed protection.</p>
<p>One should not underestimate the extent to which the Court's expansion of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> constricts law enforcement. Today's ruling, that the invocation of a right to counsel permanently prevents a police-initiated waiver, makes it largely impossible for the police to urge a prisoner who has initially declined to confess to change his mindor indeed, even to ask whether he has changed his mind. Many persons in custody will invoke the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> right to counsel during the first interrogation, so that the permanent prohibition will attach at once. Those who do not do so will almost certainly request or obtain counsel at arraignment. We have held that a general request for counsel, after the Sixth Amendment right has attached, also triggers the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> prohibition of police-solicited confessions, see <i>Michigan</i> v. <i>Jackson,</i> <span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625</a></span> (1986), and I presume that the perpetuality of prohibition announced in today's opinion applies in that context as well. "Perpetuality" is not too strong a term, since, although the Court rejects one logical moment at which the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> presumption might end, it suggests no alternative. In this case Minnick was reapproached by the police three days after he requested counsel, but the result would presumably be the same if it had been three months, or three years, or even three decades. This perpetual irrebuttable presumption will apply, I might add, not merely to interrogations involving the original crime, but to those involving other subjects as well. See <i>Arizona</i> v. <i>Roberson,</i> <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">486 U. S. 675</a></span> (1988).</p>
<p>Besides repeating the uncontroverted proposition that the suspect has a "right to have counsel <i>present,"</i> the Court stresses the clarity and simplicity that are achieved by today's <span class="star-pagination">*164</span> holding. Clear and simple rules are desirable, but only in pursuance of authority that we possess. We are authorized by the Fifth Amendment to exclude confessions that are "compelled," which we have interpreted to include confessions that the police obtain from a suspect in custody without a knowing and voluntary waiver of his right to remain silent. Undoubtedly some bright-line rules can be adopted to implement that principle, marking out the situations in which knowledge or voluntariness cannot possibly be established for example, a rule excluding confessions obtained after five hours of continuous interrogation. But a rule excluding all confessions that follow upon even the slightest police inquiry cannot conceivably be justified on this basis. It does not rest upon a reasonable prediction that all such confessions, or even most such confessions, will be unaccompanied by a knowing and voluntary waiver.</p>
<p>It can be argued that the same is true of the category of confessions excluded by the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> rule itself. I think that is so, but, as I have discussed above, the presumption of involuntariness is at least more plausible for that category. There is, in any event, a clear and rational line between that category and the present one, and I see nothing to be said for expanding upon a past mistake. Drawing a distinction between police-initiated inquiry before consultation with counsel and police-initiated inquiry after consultation with counsel is assuredly more reasonable than other distinctions <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> has already led us intosuch as the distinction between police-initiated inquiry after assertion of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> right to remain silent, and police-initiated inquiry after assertion of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> right to counsel, see Kamisar, The <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> and <i><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/" aria-description="Citation for case: Oregon v. Bradshaw">Bradshaw</a></span></i> Cases: The Court Giveth and the Court Taketh Away, in 5 The Supreme Court: Trends and Developments 153, 157 (J. Choper, Y. Kamisar, &amp; L. Tribe eds. 1984) ("[E]ither <i><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">Mosley</a></span></i> was wrongly decided or <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> was"); or the distinction between what is needed to prove waiver of the <span class="star-pagination">*165</span> <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> right to have counsel present and what is needed to prove waiver of rights found in the Constitution.</p>
<p>The rest of the Court's arguments can be answered briefly. The suggestion that it will either be impossible or ethically impermissible to determine whether a "consultation" between the suspect and his attorney has occurred is alarmist. Since, as I have described above, the main purpose of the consultation requirement is to eliminate the suspect's feeling of isolation and to assure him the presence of legal assistance, any discussion between him and an attorney whom he asks to contact, or who is provided to him, in connection with his arrest, will suffice. The precise content of the discussion is irrelevant.</p>
<p>As for the "irony" that "the suspect whose counsel is prompt would lose the protection of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>,</i> while the one whose counsel is dilatory would not," <i>ante,</i> at 155: There seems to me no irony in applying a special protection only when it is needed. The <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> rule is premised on an (already tenuous) assumption about the suspect's psychological state, and when the event of consultation renders that assumption invalid the rule should no longer apply. One searching for ironies in the state of our law should consider, first, the irony created by <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> itself: The suspect in custody who says categorically "I do not wish to discuss this matter" can be asked to change his mind; but if he should say, more tentatively, "I do not think I should discuss this matter without my attorney present" he can no longer be approached. To that there is added, by today's decision, the irony that it will be far harder for the State to establish a knowing and voluntary waiver of Fifth Amendment rights by a prisoner who has already consulted with counsel than by a newly arrested suspect.</p>
<p>Finally, the Court's concern that <i>"Edwards'</i> protection could pass in and out of existence multiple times," <i>ante,</i> at 154, does not apply to the resolution of the matter I have proposed. <span class="star-pagination">*166</span> <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> would cease to apply, permanently, once consultation with counsel has occurred.</p>
<p></p>
<h2>* * *</h2>
<p>Today's extension of the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> prohibition is the latest stage of prophylaxis built upon prophylaxis, producing a veritable fairyland castle of imagined constitutional restriction upon law enforcement. This newest tower, according to the Court, is needed to avoid "inconsisten[cy] with [the] purpose" of <i>Edwards'</i> prophylactic rule, <i>ante,</i> at 154, which was needed to protect <i>Miranda's</i> prophylactic right to have counsel present, which was needed to protect the right against <i>compelled self-incrimination</i> found (at last!) in the Constitution.</p>
<p>It seems obvious to me that, even in <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> itself but surely in today's decision, we have gone far beyond any genuine concern about suspects who do not <i>know</i> their right to remain silent, or who have been <i>coerced</i> to abandon it. Both holdings are explicable, in my view, only as an effort to protect suspects against what is regarded as their own folly. The sharp-witted criminal would know better than to confess; why should the dull-witted suffer for his lack of mental endowment? Providing him an attorney at every stage where he might be induced or persuaded (though not coerced) to incriminate himself will even the odds. Apart from the fact that this protective enterprise is beyond our authority under the Fifth Amendment or any other provision of the Constitution, it is unwise. The procedural protections of the Constitution protect the guilty as well as the innocent, but it is not their objective to set the guilty free. That some clever criminals may employ those protections to their advantage is poor reason to allow criminals who have not done so to escape justice.</p>
<p>Thus, even if I were to concede that an honest confession is a foolish mistake, I would welcome rather than reject it; a rule that foolish mistakes do not count would leave most offenders <span class="star-pagination">*167</span> not only unconvicted but undetected. More fundamentally, however, it is wrong, and subtly corrosive of our criminal justice system, to regard an honest confession as a "mistake." While every person is entitled to stand silent, it is more virtuous for the wrongdoer to admit his offense and accept the punishment he deserves. Not only for society, but for the wrongdoer himself, "admissio[n] of guilt . . . , if not coerced, [is] inherently desirable," <i>United States v. Washington,</i> <span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#187" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 187</a></span> (1977), because it advances the goals of both "justice <i>and</i> rehabilitation," <i>Michigan v. Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#448" aria-description="Citation for case: Michigan v. Tucker">417 U. S., at 448, n. 23</a></span> (emphasis added). A confession is rightly regarded by the Sentencing Guidelines as warranting a reduction of sentence, because it "demonstrates a recognition and affirmative acceptance of personal responsibility for . . . criminal conduct," U. S. Sentencing Commission, Guidelines Manual § 3E1.1 (1988), which is the beginning of reform. We should, then, rejoice at an honest confession, rather than pity the "poor fool" who has made it; and we should regret the attempted retraction of that good act, rather than seek to facilitate and encourage it. To design our laws on premises contrary to these is to abandon belief in either personal responsibility or the moral claim of just government to obedience. Cf. Caplan, Questioning <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> <span class="citation no-link">38 Vand. L. Rev. 1417</span>, 1471-1473 (1985). Today's decision is misguided, it seems to me, in so readily exchanging, for marginal, super-<span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst"><i>Zerbst</i></a></span> protection against genuinely compelled testimony, investigators' ability to urge, or even ask, a person in custody to do what is right.</p>
<h2>NOTES</h2>
<p>[*]  <i>David W. DeBruin</i> and <i>Donald B. Verrilli, Jr.,</i> filed a brief for the Mississippi State Bar as <i>amicus curiae</i> urging reversal.
</p>
<p><i>Solicitor General Starr, Assistant Attorney General Dennis, Deputy Solicitor General Bryson,</i> and <i>Nina Goodman</i> filed a brief for the United States as <i>amicus curiae</i> urging affirmance.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Miranda v. Arizona.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Miranda v. Arizona"
type: case
citation: "384 U.S. 436 (1966)"
parallel_cite: "86 S. Ct. 1602; 16 L. Ed. 2d 694; 10 Ohio Misc. 9; 36 Ohio Op. 2d 237; 10 A.L.R. 3d 974"
neutral_cite: 1966 U.S. LEXIS 2817
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1966
date_decided: 1966-06-13
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1966-06-13
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Miranda v. Arizona
  varies_by_point: false
  scope_note: Reaffirmed as a constitutional rule in Dickerson v. United States.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107252/miranda-v-arizona/"
  cluster_id: 107252
  opinion_id: 9423233
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Anchor"
related: ["[[Dickerson v. United States]]", "[[Berkemer v. McCarty]]", "[[Berghuis v. Thompkins]]", "[[Edwards v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "custodial-interrogation", "warnings", "self-incrimination"]
holding: "Statements from custodial interrogation are inadmissible unless police first gave the warnings and the suspect knowingly, voluntarily…"
lake:
  record_id: Miranda v. Arizona
  status: verified
  projected_at: 2026-07-09
---

# Miranda v. Arizona

*384 U.S. 436 (1966)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In four consolidated cases, suspects were questioned in police custody without being advised of their rights and made incriminating statements used to convict them. Miranda himself was interrogated and signed a written confession without being told he had a right to remain silent or to the assistance of counsel.

## Issue
What safeguards the prosecution must show were used before statements obtained from custodial interrogation may be admitted against a defendant.

## Rule
"the prosecution may not use statements, whether exculpatory or inculpatory, stemming from custodial interrogation of the defendant unless it demonstrates the use of procedural safeguards effective to secure the privilege against self-incrimination." — 384 U.S. at 444. ^pin-444

"By custodial interrogation, we mean questioning initiated by law enforcement officers after a person has been taken into custody or otherwise deprived of his freedom of action in any significant way." — [*Id.*](https://www.courtlistener.com/opinion/107252/miranda-v-arizona/#:~:text=By%20custodial%20interrogation%2C%20we%20mean) ^pin-444a

Absent other effective safeguards, before any custodial questioning the person must be warned that he has the right to remain silent, that anything he says may be used against him, and that he has the right to retained or appointed counsel.

## Application
Miranda was interrogated in police custody and signed a confession without being advised of his right to remain silent or to counsel. Because the prosecution could not show that the required procedural safeguards were used to protect his privilege against self-incrimination, his confession was inadmissible against him.

## Conclusion
Reversed; the confession obtained without the now-required warnings could not be used.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Miranda* was **reaffirmed** as a constitutional rule that Congress may not supersede by statute in [[Dickerson v. United States]]. It applies to all custodial interrogation regardless of offense severity ([[Berkemer v. McCarty]]), and its invocation/waiver doctrine was developed in cases such as [[Edwards v. Arizona]] and [[Berghuis v. Thompkins]].

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Anchor*

## Sources
- *Miranda v. Arizona*, 384 U.S. 436 (1966) — https://www.courtlistener.com/opinion/107252/miranda-v-arizona/ — pinpoint: 444.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "074284d5f7275234", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Miranda v. Arizona"}, "payload": {"all": [{"cite": "384 U.S. 436", "page": "436", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "384"}, {"cite": "86 S. Ct. 1602", "page": "1602", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "86"}, {"cite": "16 L. Ed. 2d 694", "page": "694", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "16"}, {"cite": "1966 U.S. LEXIS 2817", "page": "2817", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1966"}, {"cite": "10 Ohio Misc. 9", "page": "9", "reporter": "Ohio Misc.", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "10"}, {"cite": "36 Ohio Op. 2d 237", "page": "237", "reporter": "Ohio Op. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "36"}, {"cite": "10 A.L.R. 3d 974", "page": "974", "reporter": "A.L.R. 3d", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "10"}], "display": "384 U.S. 436", "official": {"cite": "384 U.S. 436", "page": "436", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "384"}, "official_selection_present": true, "record_id": "Miranda v. Arizona"}}
{"assertion_id": "71b2f692f9c92026", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-444a", "record_id": "Miranda v. Arizona"}, "payload": {"fragment": "#:~:text=By%20custodial%20interrogation%2C%20we%20mean", "page": null, "pin_id": "pin-444a", "pinpoint_status": "star-verified", "quote": "By custodial interrogation, we mean questioning initiated by law enforcement officers after a person has been taken into custody or otherwise deprived of his freedom of action in any significant way.", "quote_fidelity": "matched", "record_id": "Miranda v. Arizona", "star_marker": "444"}}
{"assertion_id": "d0e00ca210c5a3a8", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-444", "record_id": "Miranda v. Arizona"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-444", "pinpoint_status": "slip-only", "quote": "--- # Miranda v. Arizona *384 U.S. 436 (1966)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In four consolidated cases, suspects were questioned in police custody without being advised of their rights and made incriminating statements used to convict them. Miranda himself was interrogated and signed a written confession without being told he had a right to remain silent or to the assistance of counsel. ## Issue What safeguards the prosecution must show were used before statements obtained from custodial interrogation may be admitted against a defendant. ## Rule", "quote_fidelity": "mismatch", "record_id": "Miranda v. Arizona", "star_marker": null}}
{"assertion_id": "638723eaca16523f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Miranda v. Arizona"}, "payload": {"as_of_content": "1966-06-13", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Miranda v. Arizona", "scope_note": "Reaffirmed as a constitutional rule in Dickerson v. United States.", "varies_by_point": false}}
```

### lake record — Miranda v. Arizona

```json
{
  "schema_version": "s2.v1",
  "record_id": "Miranda v. Arizona",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Miranda v. Arizona",
    "case_name_short": "Miranda",
    "case_name_full": "Miranda v. Arizona",
    "input_case_name": "Miranda v. Arizona",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1966-06-13",
    "year": 1966,
    "docket": null,
    "cluster_id": 107252,
    "lead_opinion_id": 9423233,
    "sibling_ids": [
      107252,
      9423233,
      9423234,
      9423235
    ],
    "absolute_url": "/opinion/107252/miranda-v-arizona/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "384 U.S. 436",
      "volume": "384",
      "reporter": "U.S.",
      "page": "436",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "86 S. Ct. 1602",
        "volume": "86",
        "reporter": "S. Ct.",
        "page": "1602",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 L. Ed. 2d 694",
        "volume": "16",
        "reporter": "L. Ed. 2d",
        "page": "694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 Ohio Misc. 9",
        "volume": "10",
        "reporter": "Ohio Misc.",
        "page": "9",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "36 Ohio Op. 2d 237",
        "volume": "36",
        "reporter": "Ohio Op. 2d",
        "page": "237",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 A.L.R. 3d 974",
        "volume": "10",
        "reporter": "A.L.R. 3d",
        "page": "974",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1966 U.S. LEXIS 2817",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "2817",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "384 U.S. 436",
        "volume": "384",
        "reporter": "U.S.",
        "page": "436",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "86 S. Ct. 1602",
        "volume": "86",
        "reporter": "S. Ct.",
        "page": "1602",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 L. Ed. 2d 694",
        "volume": "16",
        "reporter": "L. Ed. 2d",
        "page": "694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1966 U.S. LEXIS 2817",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "2817",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 Ohio Misc. 9",
        "volume": "10",
        "reporter": "Ohio Misc.",
        "page": "9",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "36 Ohio Op. 2d 237",
        "volume": "36",
        "reporter": "Ohio Op. 2d",
        "page": "237",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 A.L.R. 3d 974",
        "volume": "10",
        "reporter": "A.L.R. 3d",
        "page": "974",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "384 U.S. 436",
    "official_selection": {
      "court_class": "scotus",
      "selected": "384 U.S. 436",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-444",
      "page": null,
      "quote": "--- # Miranda v. Arizona *384 U.S. 436 (1966)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In four consolidated cases, suspects were questioned in police custody without being advised of their rights and made incriminating statements used to convict them. Miranda himself was interrogated and signed a written confession without being told he had a right to remain silent or to the assistance of counsel. ## Issue What safeguards the prosecution must show were used before statements obtained from custodial interrogation may be admitted against a defendant. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-444a",
      "page": null,
      "quote": "By custodial interrogation, we mean questioning initiated by law enforcement officers after a person has been taken into custody or otherwise deprived of his freedom of action in any significant way.",
      "star_marker": "444",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 9263,
      "fragment": "#:~:text=By%20custodial%20interrogation%2C%20we%20mean",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1966-06-13",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Miranda v. Arizona",
    "varies_by_point": false,
    "scope_note": "Reaffirmed as a constitutional rule in Dickerson v. United States.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "AJAY (AJAY) v. STATE (CRIMINAL)",
          "cluster_id": 10774936,
          "cite": [
            "142 Nev. Adv. Op. No. 4"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane1_negative"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barker v. Wingo",
          "cluster_id": 108590,
          "cite": [
            "33 L. Ed. 2d 101",
            "92 S. Ct. 2182",
            "407 U.S. 514",
            "1972 U.S. LEXIS 34"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bruton v. United States",
          "cluster_id": 107684,
          "cite": [
            "20 L. Ed. 2d 476",
            "88 S. Ct. 1620",
            "391 U.S. 123",
            "1968 U.S. LEXIS 1630"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gregg v. Georgia",
          "cluster_id": 109532,
          "cite": [
            "49 L. Ed. 2d 859",
            "96 S. Ct. 2909",
            "428 U.S. 153",
            "1976 U.S. LEXIS 82"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rose v. Lee",
          "cluster_id": 773551,
          "cite": [
            "252 F.3d 676",
            "2001 U.S. App. LEXIS 10698",
            "2001 WL 558079"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edwards v. Arizona",
          "cluster_id": 110475,
          "cite": [
            "68 L. Ed. 2d 378",
            "101 S. Ct. 1880",
            "451 U.S. 477",
            "1981 U.S. LEXIS 96"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'Sullivan v. Boerckel",
          "cluster_id": 118296,
          "cite": [
            "144 L. Ed. 2d 1",
            "119 S. Ct. 1728",
            "526 U.S. 838",
            "1999 U.S. LEXIS 4003"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pembaur v. City of Cincinnati",
          "cluster_id": 111615,
          "cite": [
            "89 L. Ed. 2d 452",
            "106 S. Ct. 1292",
            "475 U.S. 469",
            "1986 U.S. LEXIS 33",
            "54 U.S.L.W. 4289"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rose v. Lundy",
          "cluster_id": 110662,
          "cite": [
            "71 L. Ed. 2d 379",
            "102 S. Ct. 1198",
            "455 U.S. 509",
            "1982 U.S. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rhode Island v. Innis",
          "cluster_id": 110254,
          "cite": [
            "64 L. Ed. 2d 297",
            "100 S. Ct. 1682",
            "446 U.S. 291",
            "1980 U.S. LEXIS 94"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Furman v. Georgia",
          "cluster_id": 108605,
          "cite": [
            "33 L. Ed. 2d 346",
            "92 S. Ct. 2726",
            "408 U.S. 238",
            "1972 U.S. LEXIS 169"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
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
        "journal_ref": "Miranda v. Arizona:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107252 OR 9423233 OR 9423234 OR 9423235) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzYwNTcyODAwMDAwJnM9MTA3MDYyNzUmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107252+OR+9423233+OR+9423234+OR+9423235%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107252 OR 9423233 OR 9423234 OR 9423235)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMzQwJnM9MTExNjE0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107252+OR+9423233+OR+9423234+OR+9423235%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107252 OR 9423233 OR 9423234 OR 9423235)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzY1NDExMjAwMDAwJnM9MTA3NTMzNzMmdD1vJmQ9MjAyNi0wNy0wNiZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107252+OR+9423233+OR+9423234+OR+9423235%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107252 OR 9423233 OR 9423234 OR 9423235)",
    "indexed_citing_opinions": 34147,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107252,
        "count": 30407,
        "count_source": "search"
      },
      {
        "opinion_id": 9423233,
        "count": 4367,
        "count_source": "search"
      },
      {
        "opinion_id": 9423234,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423235,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 58315,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/miranda-v-arizona.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yLjc3Nzc1ODQmcz04NzI3NjQyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107252+OR+9423233+OR+9423234+OR+9423235%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 9423235,
        "cited_id": 91057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 94082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 94327,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 94454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 97552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 103855,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 103974,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 104931,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 105149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 106512,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 107116,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 270056,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 270206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 270413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 1177527,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 2189589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423235,
        "cited_id": 2402399,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 85330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 91057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 94454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 97242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 101320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103792,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 104849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 104890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 104931,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105449,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105508,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 107014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 107085,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 236744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 244463,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 264658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 265586,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 267168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 268400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 268701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 269239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 269286,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 270022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 1167454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 1177555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 1297557,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 1393125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 1429077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 1544343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 2045374,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 2221754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 2608355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 3314077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 5516029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 5520716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 5521593,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 5521618,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 6751647,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 6913112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 8144042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 8155149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 8156474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 8571803,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 8571939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 9419181,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 9422869,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 9423096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423233,
        "cited_id": 9549155,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 91057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 94327,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 94454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 97552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 100776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 102189,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 103792,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 103833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 104010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 104931,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 104997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 105095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 105149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106512,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 106962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 265095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 265525,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 265586,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 266372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 267167,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 267168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 268701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 270054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 1177555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 1177616,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 1484800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 1512810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 1513064,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 1738732,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 1789370,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 2106318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 2138506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 2221754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 2398929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 2402413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 2619836,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 5521591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 9421842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9423234,
        "cited_id": 9444722,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 85330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 91057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 94082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 94327,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 94454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 97242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 97552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 100776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 101320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 102189,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103792,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103855,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103974,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104931,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 104997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105449,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105508,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106512,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 106962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 107014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 107085,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 107116,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 236744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 244463,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 264658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 265095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 265525,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 265586,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 266372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 267167,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 267168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 268400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 268701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 269239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 269286,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 270022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 270054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 270056,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 270206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 270413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1167454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1177527,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1177555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1177616,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1297557,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1393125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1429077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1484800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1512810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1513064,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1544343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1738732,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 1789370,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2045374,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2106318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2138506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2189589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2221754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2398929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2402399,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2402413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2608355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 2619836,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 3314077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 5516029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 5520716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 5521591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 5521593,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 5521618,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 6751647,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 6913112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 8144042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 8155149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 8156474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 8571803,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 8571939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 9419181,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 9421842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 9422869,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 9423096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 9423233,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 9444722,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107252,
        "cited_id": 9549155,
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
    "date_created": "2026-07-05T14:09:29Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:09:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:09:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:13:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:09:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Miranda v. Arizona (truncated)

```
<opinion type="majority">
<author id="b537-7">Mr. Chief Justice Warren</author>
<p id="AMNy">delivered the opinion of the Court.</p>
<p id="b537-8">The cases before us raise questions which go to the roots of our concepts of American criminal jurisprudence: the restraints society must observe consistent with the Federal Constitution in prosecuting individuals for crime. More specifically, we deal with the admissibility of statements obtained from an individual who is subjected to custodial police interrogation and the necessity for procedures which assure that the individual is accorded his privilege under the Fifth Amendment to the Constitution not to be compelled to incriminate himself.</p>
<p id="b538-5"><page-number citation-index="1" label="440">*440</page-number>We dealt with certain phases of this problem recently in <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964). There, as in the four cases before us, law enforcement officials took the defendant into custody and interrogated him in a police station for the purpose of obtaining a confession. The police did not effectively advise him of his right to remain silent or of his right to consult with his attorney. Rather, they confronted him with an alleged accomplice who accused him of having perpetrated a murder. When the defendant denied the accusation and said “I didn’t shoot Manuel, you did it,” they handcuffed him and took him to an interrogation room. There, while handcuffed and standing, he was questioned for four hours until he confessed. During this interrogation, the police denied his request to speak to his attorney, and they prevented his retained attorney, who had come to the police station, from consulting with him. At his trial, the State, over his objection, introduced the confession against him. We held that the statements thus made were constitutionally inadmissible.</p>
<p id="b538-6">This case has been the subject of judicial interpretation and spirited legal debate since it was decided two years ago. Both state and federal courts, in assessing its implications, have arrived at varying conclusions.<footnotemark>1</footnotemark> A wealth of scholarly material has been written tracing its ramifications and underpinnings.<footnotemark>2</footnotemark> Police and prose<page-number citation-index="1" label="441">*441</page-number>cutor have speculated on its range and desirability.<footnotemark>3</footnotemark> We granted certiorari in these cases, <span class="citation multiple-matches"><a href="/c/U.%20S./382/924/">382 U. S. 924</a></span>, 925, 937, in order further to explore some facets of the problems, thus exposed, of applying the privilege against self-incrimination to in-custody interrogation, and to give <page-number citation-index="1" label="442">*442</page-number>concrete constitutional guidelines for law enforcement agencies and courts to follow.</p>
<p id="b540-6">We start here, as we did in <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>, </em>with the premise that our holding is not an innovation in our jurisprudence, but is an application of principles long recognized and applied in other settings. We have undertaken a thorough re-examination of the <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>decision and the principles it announced, and we reaffirm it. That case was but an explication of basic rights that are enshrined in our Constitution — that “No person . . . shall be compelled in any criminal case to be a witness against himself,” and that “the accused shall . . . have the Assistance of Counsel” — rights which were put in jeopardy in that case through official overbearing. These precious rights were fixed in our Constitution only after centuries of persecution and struggle. And in the words of Chief Justice Marshall, they were secured “for ages to come, and . . . designed to approach immortality as nearly as human institutions can approach it,” <em>Cohens </em>v. <em>Virginia, </em><span class="citation" data-id="85330"><a href="/opinion/85330/cohens-v-virginia/#387" aria-description="Citation for case: Cohens v. Virginia">6 Wheat. 264, 387</a></span> (1821).</p>
<p id="b540-7">Over 70 years ago, our predecessors on this Court eloquently stated:</p>
<blockquote id="b540-8">“The maxim <em>nemo tenetur seipsum acensare </em>had its origin in a protest against the inquisitorial and manifestly unjust methods of- interrogating accused persons, which [have] long obtained in the continental system, and, until the expulsion of the Stuarts from the British throne in 1688, and the erection of additional barriers for the protection of the people against the exercise of arbitrary power, [were] not uncommon even in England. While the admissions or confessions of the prisoner, when voluntarily and freely made, have always ranked high in the scale of incriminating evidence, if an accused person be asked to explain his apparent connection with a crime under investigation, the ease with which the <page-number citation-index="1" label="443">*443</page-number>questions put to him may assume an inquisitorial character, the temptation to press the witness unduly, to browbeat him if he be timid or reluctant, to push him into a corner, and to entrap him into fatal contradictions, which is so painfully evident in many of the earlier state trials, notably in those of Sir Nicholas Throckmorton, and Udal, the Puritan minister, made the system so odious as to give rise to a demand for its total abolition. The change in the English criminal procedure in that particular seems to be founded upon no statute and no judicial opinion, but upon a general and silent acquiescence of the courts in a popular demand. But, however adopted, it has become firmly embedded in English, as well as in American jurisprudence. So deeply did the iniquities of the ancient system impress themselves upon the minds of the American colonists that the States, with one accord, made a denial of the right to question an accused person a part of their fundamental law, so that a maxim, which in England was a mere rule of evidence, became clothed in this country with the impregnability of a constitutional enactment.” <em>Brown </em>v. <em>Walker, </em><span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#596" aria-description="Citation for case: Brown v. Walker">161 U. S. 591, 596-597</a></span> (1896).</blockquote>
<p id="b541-5">In stating the obligation of the judiciary to apply these constitutional rights, this Court declared in <em>Weems </em>v. <em>United States, </em><span class="citation" data-id="9418181"><a href="/opinion/97242/weems-v-united-states/#373" aria-description="Citation for case: Weems v. United States">217 U. S. 349, 373</a></span> (1910):</p>
<blockquote id="b541-8"><em>. </em>. our contemplation cannot be only of what has been but of what may be. Under any other rule a constitution would indeed be as easy of application as it would be deficient in efficacy and power. Its general principles would have little value and be converted by precedent into impotent and lifeless formulas. Rights declared in words might be lost in reality. And this has been recognized. The <page-number citation-index="1" label="444">*444</page-number>meaning and vitality of the Constitution have developed against narrow and restrictive construction.”</blockquote>
<p id="b542-6">This was the spirit in which we delineated, in meaningful language, the manner in which the constitutional rights of the individual could be enforced against overzealous police practices. It was necessary in <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>, </em>as here, to insure that what was proclaimed in the Constitution had not become but a “form of words,” <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span> (1920), in the hands of government officials. And it is in this spirit, consistent with our role as judges, that we adhere to the principles of <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>today.</p>
<p id="b542-7">Our holding will be spelled out with some specificity in the pages which follow but briefly stated it is this: the prosecution may not use statements, whether exculpatory or inculpatory, stemming from custodial interrogation of the defendant unless it demonstrates the use of procedural safeguards effective to secure the privilege against self-incrimination. By custodial interrogation, we mean questioning initiated by law enforcement officers after a person has been taken into custody or otherwise deprived of his freedom of action in any significant way.<footnotemark>4</footnotemark> As for the procedural safeguards to be employed, unless other fully effective means are devised to inform accused persons of their right of silence and to assure a continuous opportunity to exercise it, the following measures are required. Prior to any questioning, the person must be warned that he has a right to remain silent, that any statement he does make may be used as evidence against him, and that he has a right to the presence of an attorney, either retained or appointed. The defendant may waive effectuation of these rights, provided the waiver is made voluntarily, knowingly and intelligently. If, however, he indicates in any manner and at any stage of the <page-number citation-index="1" label="445">*445</page-number>process that he wishes to consult with an attorney before speaking there can be no questioning. Likewise, if the individual is alone and indicates in any manner that he does not wish to be interrogated, the police may not question him. The mere fact that he may have answered some questions or volunteered some statements on his own does not deprive him of the right to refrain from answering any further inquiries until he has consulted with an attorney and thereafter consents to be questioned.</p>
<p id="b543-5">I.</p>
<p id="b543-6">The constitutional issue we decide in each of these cases is the admissibility of statements obtained from a defendant questioned while in custody or otherwise deprived of his freedom of action in any significant way. In each, the defendant was questioned by police officers, detectives, or a prosecuting attorney in a room in which he was cut off from the outside world. In none of these cases was the defendant given a full and effective warning of his rights at the outset of the interrogation process. In all the cases, the questioning elicited oral admissions, and in three of them, signed statements as well which were admitted at their trials. They all thus share salient features— incommunicado interrogation of individuals in a police-dominated atmosphere, resulting in self-incriminating statements without full warnings of constitutional rights.</p>
<p id="b543-7">An understanding of the nature and setting of this in-custody interrogation is essential to our decisions today. The difficulty in depicting what transpires at such interrogations stems from the fact that in this country they have largely taken place incommunicado. From extensive factual studies undertaken in the early 1930’s, including the famous Wickersham Report to Congress by a Presidential Commission, it is clear that police violence and the “third degree” flourished at that time.<footnotemark>5</footnotemark> <page-number citation-index="1" label="446">*446</page-number>In a series of cases decided by this Court long after these studies, the police resorted to physical brutality — beating, hanging, whipping — and to sustained and protracted questioning incommunicado in order to extort confessions.<footnotemark>6</footnotemark> The Commission on Civil Rights in 1961 found much evidence to indicate that “some policemen still resort to physical force to obtain confessions,” 1961 Comm’n on Civil Rights Rep., Justice, pt. 5, 17. The use of physical brutality and violence is not, unfortunately, relegated to the past or to any part of the country. Only recently in Kings County, New York, the police brutally beat, kicked and placed lighted cigarette butts on the back of a potential witness under interrogation for the purpose of securing a statement incriminating a third party. <em>People </em>v. <em>Portelli, </em>15 N. Y. 2d 235, <span class="citation" data-id="5521593"><a href="/opinion/5674064/people-v-portelli/" aria-description="Citation for case: People v. Portelli">205 N. E. 2d 857</a></span>, 257 N. Y. S. 2d 931 (1965).<footnotemark>7</footnotemark></p>
<p id="b545-4"><page-number citation-index="1" label="447">*447</page-number>The examples given above are undoubtedly the exception now, but they are sufficiently widespread to be the object of concern. Unless a proper limitation upon custodial interrogation is achieved — such as these decisions will advance — -there can be no assurance that practices of this nature will be eradicated in the foreseeable future. The conclusion of the Wickersham Commission Report, made over 30 years ago, is still pertinent:</p>
<blockquote id="b545-5">“To the contention that the third degree is necessary to get the facts, the reporters aptly reply in the language of the present Lord Chancellor of England (Lord Sankey): ‘It is not admissible to do a great right by doing a little wrong. ... It is not sufficient to do justice by obtaining a proper result by irregular or improper means.’ Not only does the use of the third degree involve a flagrant violation of law by the officers of the law, but it involves also the dangers of false confessions, and it tends to make police and prosecutors less zealous in the search for objective evidence. As the New York prosecutor quoted in the report said, <em>‘It </em>is a short cut and makes the police lazy and unenterprising.’ Or, as another official quoted remarked: Tf you use your fists, you <page-number citation-index="1" label="448">*448</page-number>are not so likely to use your wits.’ We agree with the conclusion expressed in the report, that ‘The third degree brutalizes the police, hardens the prisoner against society, and lowers the esteem in which the administration of justice is held by the public.’ ” IV National Commission on Law Observance and Enforcement, Report on Lawlessness in Law Enforcement 5 (1931).</blockquote>
<p id="b546-6">Again we stress that the modern practice of in-custody interrogation is psychologically rather than physically oriented. As we have stated before, “Since <em>Chambers </em>v. <em>Florida, </em><span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span>, this Court has recognized that coercion can be mental as well as physical, and that the blood of the accused is not the only hallmark of an unconstitutional inquisition.” <em>Blackburn </em>v. <em>Alabama, </em><span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 206</a></span> (1960). Interrogation still takes place in privacy. Privacy results in secrecy and this in turn results in a gap in our knowledge as to what in fact goes on in the interrogation rooms. A valuable source of information about present police practices, however, may be found in various police manuals and texts which document procedures employed with success in the past, and which recommend various other effective tactics.<footnotemark>8</footnotemark> These <page-number citation-index="1" label="449">*449</page-number>texts are used by law enforcement agencies themselves as guides.<footnotemark>9</footnotemark> It should be noted that these texts professedly present the most enlightened and effective means presently used to obtain statements through custodial interrogation. By considering these texts and other data, it is possible to describe procedures observed and noted around the country.</p>
<p id="b547-5">The officers are told by the manuals that the “principal psychological factor contributing to a successful interrogation is <em>privacy </em>— being alone with the person under interrogation.” <footnotemark>10</footnotemark> The efficacy of this tactic has been explained as follows:</p>
<blockquote id="b547-6">“If at all practicable, the interrogation should take place in the investigator’s office or at least in a room of his own choice. The subject should be deprived of every psychological advantage. In his own home he may be confident, indignant, or recalcitrant. He is more keenly aware of his rights and <page-number citation-index="1" label="450">*450</page-number>more reluctant to tell of his indiscretions or criminal behavior within the walls of his home. Moreover his family and other friends are nearby, their presence lending moral support. In his own office, the investigator possesses all the advantages. The atmosphere suggests the invincibility of the forces of the law.” <footnotemark>11</footnotemark></blockquote>
<p id="b548-6">To highlight the isolation and unfamiliar surroundings, the manuals instruct the police to display an air of confidence in the suspect’s guilt and from outward appearance to maintain only an interest in confirming certain details. The guilt of the subject is to be posited as a fact. The interrogator should direct his comments toward the reasons why the subject committed the act, rather than court failure by asking the subject whether he did it. Like other men, perhaps the subject has had a bad family life, had an unhappy childhood, had too much to drink, had an unrequited desire for women. The officers are instructed to minimize the moral seriousness of the offense,<footnotemark>12</footnotemark> to cast blame on the victim or on society.<footnotemark>13</footnotemark> These tactics are designed to put the subject in a psychological state where his story is but an elaboration of what the police purport to know already— that he is guilty. Explanations to the contrary are dismissed and discouraged.</p>
<p id="b548-7">The texts thus stress that the major qualities an interrogator should possess are patience and perseverance. <page-number citation-index="1" label="451">*451</page-number>One writer describes the efficacy of these characteristics in this manner:</p>
<blockquote id="b549-5">“In the preceding paragraphs emphasis has been placed on kindness and stratagems. The investigator will, however, encounter many situations where the sheer weight of his personality will be the deciding factor. Where emotional appeals and tricks are employed to no avail, he must rely on an oppressive atmosphere of dogged persistence. He must interrogate steadily and without relent, leaving the subject no prospect of surcease. He must dominate his subject and overwhelm him with his inexorable will to obtain the truth. He should interrogate for a spell of several hours pausing only for the subject’s necessities in acknowledgment of the need to avoid a charge of duress that can be technically substantiated. In a serious case, the interrogation may continue for days, with the required intervals for food and sleep, but with no respite from the atmosphere of domination. It is possible in this way to induce the subject to talk without resorting to duress or coercion. The method should be used only when the guilt of the subject appears highly probable.” <footnotemark>14</footnotemark></blockquote>
<p id="b549-6">The manuals suggest that the suspect be offered legal excuses for his actions in order to obtain an initial admission of guilt. Where there is a suspected revenge-killing, for example, the interrogator may say:</p>
<blockquote id="b549-7">“Joe, you probably didn’t go out looking for this fellow with the purpose of shooting him. My guess is, however, that you expected something from him and that’s why you carried a gun — for your own protection. You knew him for what he was, no good. Then when you met him he probably started using foul, abusive language and he gave some indi<page-number citation-index="1" label="452">*452</page-number>cation that he was about to pull a gun on you, and that’s when you had to act to save your own life. That’s about it, isn’t it, Joe?” <footnotemark>15</footnotemark></blockquote>
<p id="ABc">Having then obtained the admission of shooting, the interrogator is advised to refer to circumstantial evidence which negates the self-defense explanation. This should enable him to secure the entire story. One text notes that “Even if he fails to do so, the inconsistency between the subject’s original denial of the shooting and his present admission of at least doing the shooting will serve to deprive him of a self-defense ‘out’ at the time of trial.” <footnotemark>16</footnotemark></p>
<p id="b550-6">When the techniques described above prove unavailing, the texts recommend they be alternated with a show of some hostility. One ploy often used has been termed the “friendly-unfriendly” or the “Mutt and Jeff” act:</p>
<blockquote id="b550-7">“. . . In this technique, two agents are employed. Mutt, the relentless investigator, who knows the subject is guilty and is not going , to waste any time. He’s sent a dozen men away for this crime and he’s going to send the subject away for the full term. Jeff, on the other hand, is obviously a kindhearted man. He has a family himself. He has a brother who was involved in a little scrape like this. He disapproves of Mutt and his tactics and will arrange to get him off the case if the subject will cooperate. He can’t hold Mutt off for very long. The subject would be wise to make a quick decision. The technique is applied by having both investigators present while Mutt acts out his role. Jeff may stand by quietly and demur at some of Mutt’s tactics. When Jeff makes his plea for cooperation, Mutt is not present in the room.” <footnotemark>17</footnotemark></blockquote>
<p id="b551-4"><page-number citation-index="1" label="453">*453</page-number>The interrogators sometimes are instructed to induce a confession out of trickery. The technique here is quite effective in crimes which require identification or which run in series. In the identification situation, the interrogator may take a break in his questioning to place the subject among a group of men in a line-up. “The witness or complainant (previously coached, if necessary) studies the line-up and confidently points out the subject as the guilty party.” <footnotemark>18</footnotemark> Then the questioning resumes “as though there were now no doubt about the guilt of the subject.” A variation on this technique is called the “reverse line-up”:</p>
<blockquote id="b551-5">“The accused is placed in a line-up, but this time he is identified by several fictitious witnesses or victims who associated him with different offenses. It is expected that the subject will become desperate and confess to the offense under investigation in order to escape from the false accusations.” <footnotemark>19</footnotemark></blockquote>
<p id="b551-6">The manuals also contain instructions for police on how to handle the individual who refuses to discuss the matter entirely, or who asks for an attorney or relatives. The examiner is to concede him the right to remain silent. “This usually has a very undermining effect. First of all, he is disappointed in his expectation of an unfavorable reaction on the part of the interrogator. Secondly, a concession of this right to remain silent im<page-number citation-index="1" label="454">*454</page-number>presses the subject with the apparent fairness of his interrogator.”<footnotemark>20</footnotemark> After this psychological conditioning, however, the officer is told to point out the incriminating significance of the suspect’s refusal to talk:</p>
<blockquote id="b552-6">“Joe, you have a right to remain silent. That’s your privilege and I’m the last person in the world who’ll try to take it away from you. If that’s the way you want to leave this, O. K. But let me ask you this. Suppose you were in my shoes and I were in yours and you called me in to ask me about this and I told you, T don’t want to answer any of your questions.’ You’d think I had something to hide, and you’d probably be right in thinking that. That’s exactly what I’ll have to think about you, and so will everybody else. So let’s sit here and talk this whole thing over.” <footnotemark>21</footnotemark></blockquote>
<p id="b552-7">New will persist in their initial refusal to talk, it is said, if this monologue is employed correctly.</p>
<p id="b552-8">In the event that the subject wishes to speak to a relative or an attorney, the following advice is tendered:</p>
<blockquote id="b552-9">“[T]he interrogator should respond by suggesting that the subject first tell the truth to the interrogator himself rather than get anyone else involved in the matter. If the request is for an attorney, the interrogator may suggest that the subject save himself or his family the expense of any such professional service, particularly if he is innocent of the offense under investigation. The interrogator may also add, ‘Joe, I’m only looking for the truth, and if you’re telling the truth, that’s it. You can handle this by yourself.’ ” <footnotemark>22</footnotemark></blockquote>
<p id="b553-4"><page-number citation-index="1" label="455">*455</page-number>From these representative samples of interrogation techniques, the setting prescribed by the manuals and observed in practice becomes clear. In essence, it is this: To be alone with the subject is essential to prevent distraction and to deprive him of any outside support. The aura of confidence in his guilt undermines his will to resist. He merely confirms the preconceived story the police seek to have him describe. Patience and persistence, at times relentless questioning, are employed. To obtain a confession, the interrogator must “patiently maneuver himself or his quarry into a position from which the desired objective may be attained.” <footnotemark>23</footnotemark> When normal procedures fail to produce the needed result, the police may resort to deceptive stratagems such as giving false legal advice. It is important to keep the subject off balance, for example, by trading on his insecurity about himself or his surroundings. The police then persuade, trick, or cajole him out of exercising his constitutional rights.</p>
<p id="b553-5">Even without employing brutality, the “third degree” or the specific stratagems described above, the very fact of custodial interrogation exacts a heavy toll on individual liberty and trades on the weakness of individuals.<footnotemark>24</footnotemark> <page-number citation-index="1" label="456">*456</page-number>This fact may be illustrated simply by referring to three confession cases decided by this Court in the Term immediately preceding our <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>decision. In <em>Townsend </em>v. <em>Sain, </em><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">372 U. S. 293</a></span> (1963), the defendant was a 19-year-old heroin addict, described as a “near mental defective,” <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/#307" aria-description="Citation for case: Townsend v. Sain"><em>id., </em>at 307-310</a></span>. The defendant in <em>Lynumn </em>v. <em>Illinois, </em><span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528</a></span> (1963), was a woman who confessed to the arresting officer after being importuned to “cooperate” in order to prevent her children from being taken by relief authorities. This Court as in those cases reversed the conviction of a defendant in <em>Haynes </em>v. <em>Washington, </em><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span> (1963), whose persistent request during his interrogation was to phone his wife or attorney.<footnotemark>25</footnotemark> In other settings, these individuals might have exercised their constitutional rights. In the incommunicado police-dominated atmosphere, they succumbed.</p>
<p id="b554-6">In the cases before us today, given this background, we concern ourselves primarily with this interrogation atmosphere and the evils it can bring. In No. 759, <em>Miranda </em>v. <em>Arizona, </em>the police arrested the defendant and took him to a special interrogation room where they secured a confession. In No. 760, <em>Vignera </em>v. <em>New York, </em>the defendant made oral admissions to the police after interrogation in the afternoop, and then signed an inculpatory statement upon being questioned by an assistant district attorney later the same evening. In No. 761, <em>Westover </em>v. <em>United States, </em>the defendant was handed over to the Federal Bureau of Investigation by <page-number citation-index="1" label="457">*457</page-number>local authorities after they had detained and interrogated him for a lengthy period, both at night and the following morning. After some two hours of questioning, the federal officers had obtained signed statements from the defendant. Lastly, in No. 584, <em>California </em>v. <em>Stewart, </em>the local police held the defendant five days in the station and interrogated him on nine separate occasions before they secured his inculpatory statement.</p>
<p id="b555-5">In these cases, we might not find the defendants’ statements to have been involuntary in traditional terms. Our concern for adequate safeguards to protect precious Fifth Amendment rights is, of course, not lessened in the slightest. In each of the cases, the defendant was thrust into an unfamiliar atmosphere and run through menacing police interrogation procedures. The potentiality for compulsion is forcefully apparent, for example, in <em>Miranda, </em>where the indigent Mexican defendant was a seriously disturbed individual with pronounced sexual fantasies, and in <em>Stewart, </em>in which the defendant was an indigent Los Angeles Negro who had dropped out of school in the sixth grade. To be sure, the records do not evince overt physical coercion or patent psychological ploys. The fact remains that in none of these cases did the officers undertake to afford appropriate safeguards at the outset of the interrogation to insure that the statements were truly the product of free choice.</p>
<p id="b555-6">It is obvious that such an interrogation environment is created for no purpose other than to subjugate the individual to the will of his examiner. This atmosphere carries its own badge of intimidation. To be sure, this is not physical intimidation, but it is equally destructive of human dignity.<footnotemark>26</footnotemark> The current practice of incommunicado interrogation is at odds with one of our <page-number citation-index="1" label="458">*458</page-number>Nation’s most cherished principles — that the individual may not be compelled to incriminate himself. Unless adequate protective devices are employed to dispel the compulsion inherent in custodial surroundings, no statement obtained from the defendant can truly be the product of his free choice.</p>
<p id="b556-6">From the foregoing, we can readily perceive an intimate connection between the privilege against self-incrimination and police custodial questioning. It is fitting to turn to history and precedent underlying the Self-Incrimination Clause to determine its applicability in this situation.</p>
<p id="b556-7">II.</p>
<p id="b556-8">We sometimes forget how long it has taken to establish the privilege against self-incrimination, the sources from which it came and the fervor with which it was defended. Its roots go back into ancient times.<footnotemark>27</footnotemark> Per<page-number citation-index="1" label="459">*459</page-number>haps the critical historical event shedding light on its origins and evolution was the trial of one John Lilburn, a vocal anti-Stuart Leveller, who was made to take the Star Chamber Oath in 1637. The oath would have bound him to answer to all questions posed to him on any subject. The Trial of John Lilburn and John Wharton, 3 How. St. Tr. 1315 (1637). He resisted the oath and declaimed the proceedings, stating:</p>
<blockquote id="b557-5">“Another fundamental right I then contended for, was, that no man’s conscience ought to be racked by oaths imposed, to answer to questions concerning himself in matters criminal, or pretended to be so.” Haller &amp; Davies, The Leveller Tracts 1647-1653, p. 454 (1944).</blockquote>
<p id="b557-6">On account of the Lilburn Trial, Parliament abolished the inquisitorial Court of Star Chamber and went further in giving him generous reparation. The lofty principles to which Lilburn had appealed during his trial gained popular acceptance in England.<footnotemark>28</footnotemark> These sentiments worked their way over to the Colonies and were implanted after great struggle into the Bill of Rights.<footnotemark>29</footnotemark> Those who framed our Constitution and the Bill of Rights were ever aware of subtle encroachments on individual liberty. They knew that “illegitimate and unconstitutional practices get their first footing ... by silent approaches and slight deviations from legal modes of procedure.” <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 635</a></span> (1886). The privilege was elevated to constitutional status and has always been “as broad as the mischief <page-number citation-index="1" label="460">*460</page-number>against which it seeks to guard.” <em>Counselman </em>v. <em>Hitchcock, </em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#562" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 562</a></span> (1892). We cannot depart from this noble heritage.</p>
<p id="b558-6">Thus we may view the historical development of the privilege as one which groped for the proper scope of governmental power over the citizen. As a “noble principle often transcends its origins,” the privilege has come rightfully to be recognized in part as an individual’s substantive right, a “right to a private enclave where he may lead a private life. That right is the hallmark of our democracy.” <em>United States </em>v. <em>Grunewald, </em><span class="citation" data-id="6913112"><a href="/opinion/7012574/united-states-v-grunewald/#579" aria-description="Citation for case: United States v. Grunewald">233 F. 2d 556, 579, 581-582</a></span> (Frank, J., dissenting), rev’d, <span class="citation" data-id="9421440"><a href="/opinion/105508/grunewald-v-united-states/" aria-description="Citation for case: Grunewald v. United States">353 U. S. 391</a></span> (1957). We have recently noted that the privilege against self-incrimination — the essential mainstay of our adversary system — is founded on a complex of values, <em>Murphy </em>v. <em>Waterfront Comm’n, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#55" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 55-57, n. 5</a></span> (1964); <em>Tehan </em>v. <em>Shott, </em><span class="citation" data-id="6751647"><a href="/opinion/6862154/tehan-v-united-states-ex-rel-shott/#414" aria-description="Citation for case: Tehan v. United States ex rel. Shott">382 U. S. 406, 414-415, n. 12</a></span> (1966). All these policies point to one overriding thought: the constitutional foundation underlying the privilege is the respect a government — state or federal— must accord to the dignity and integrity of its citizens. To maintain a “fair state-individual balance,” to require the government “to shoulder the entire load,” 8 Wigmore, Evidence 317 (McNaughton rev. 1961), to respect the inviolability of the human personality, our accusatory system of criminal justice demands that the government seeking to punish an individual produce the evidence against him by its own independent labors, rather than by the cruel, simple expedient of compelling it from his own mouth. <em>Chambers </em>v. <em>Florida, </em><span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#235" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227, 235-238</a></span> (1940). In sum, the privilege is fulfilled only when the person is guaranteed the right “to remain silent unless he chooses to speak in the unfettered exercise of his own will.” <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#8" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 8</a></span> (1964).</p>
<p id="b558-7">The question in these cases is whether the privilege is fully applicable during a period of custodial interroga<page-number citation-index="1" label="461">*461</page-number>tion. In this Court, the privilege has consistently been accorded a liberal construction. <em>Albertson </em>v. <em>SACB, </em><span class="citation" data-id="9423096"><a href="/opinion/107110/albertson-v-subversive-activities-control-board/#81" aria-description="Citation for case: Albertson v. Subversive Activities Control Board">382 U. S. 70, 81</a></span> (1965); <em>Hoffman </em>v. <em>United States, </em>341 U. S.. 479, 486 (1951); <em>Arndstein </em>v. <em>McCarthy, </em><span class="citation" data-id="8144042"><a href="/opinion/8182123/arndstein-v-mccarthy/#72" aria-description="Citation for case: Arndstein v. McCarthy">254 U. S. 71, 72-73</a></span> (1920); <em>Counselman </em>v. <em>Hitchock, </em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#562" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 562</a></span> (1892). We are satisfied that all the principles embodied in the privilege apply to informal compulsion exerted by law-enforcement officers during in-custody questioning. An individual swept from familiar surroundings into police custody, surrounded by antagonistic forces, and subjected to the techniques of persuasion described above cannot be otherwise than under compulsion to speak. As a practical matter, the compulsion to speak in the isolated setting of the police station may well be greater than in courts or other official investigations, where there are often impartial observers to guard against intimidation or trickery.<footnotemark>30</footnotemark></p>
<p id="b559-5">This question, in fact, could have been taken as settled in federal courts almost 70 years ago, when, in <em>Bram </em>v. <em>United States, </em><span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#542" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 542</a></span> (1897), this Court held:</p>
<blockquote id="b559-6">“In criminal trials, in the courts of the United States, wherever a question arises whether a confession is incompetent because not voluntary, the issue is controlled by that portion of the Fifth Amendment . . . commanding that no person ‘shall be compelled in any criminal case to be a witness against himself.’ ”</blockquote>
<p id="b559-7">In <em><span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">Bram</a></span>, </em>the Court reviewed the British and American history and case law and set down the Fifth Amendment standard for compulsion which we implement today:</p>
<blockquote id="AVB-">“Much of the confusion which has resulted from the effort to deduce from the adjudged cases what <page-number citation-index="1" label="462">*462</page-number>would be a sufficient quantum of proof to show that a confession was or was not voluntary, has arisen from a misconception of the subject to which the proof must address itself. The rule is not that in order to render a statement admissible the proof must be adequate to establish that the particular communications contained in a statement were voluntarily made, but it must be sufficient to establish that the making of the statement was voluntary; that is to say, that from the causes, which the law treats as legally sufficient to engender in the mind of the accused hope or fear in respect to the crime charged, the accused was not involuntarily impelled to make a statement, when but for the improper influences he would have remained silent. . . .” <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#549" aria-description="Citation for case: Bram v. United States">168 U. S., at 549</a></span>. And see, <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#542" aria-description="Citation for case: Bram v. United States"><em>id., </em>at 542</a></span>.</blockquote>
<p id="b560-6">The Court has adhered to this reasoning. In 1924, Mr. Justice Brandéis wrote for a unanimous Court in reversing a conviction resting on a compelled confession, <em>Wan </em>v. <em>United States, </em><span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/" aria-description="Citation for case: Ziang Sung Wan v. United States">266 U. S. 1</a></span>. He stated:</p>
<blockquote id="b560-7">“In the federal courts, the requisite of voluntariness is not satisfied by establishing merely that the confession was not induced by a promise or a threat. A confession is voluntary in law if, and only if, it was, in fact, voluntarily made. A confession may have been given voluntarily, although it was made to police officers, while in custody, and in answer to an examination conducted by them. But a confession obtained by compulsion must be excluded whatever may have been the character of the compulsion, and whether the compulsion was applied in a judicial proceeding or otherwise. <em>Bram </em>v. <em>United States, </em><span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">168 U. S. 532</a></span>.” <span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/#14" aria-description="Citation for case: Ziang Sung Wan v. United States">266 U. S., at 14-15</a></span>.</blockquote>
<p id="b560-8">In addition to the expansive historical development of the privilege and the sound policies which have nurtured <page-number citation-index="1" label="463">*463</page-number>its evolution, judicial precedent thus clearly establishes its application to incommunicado interrogation. In fact, the Government concedes this point as well established in No. 761, <em>Westover </em>v. <em>United States, </em>stating: “We have no doubt . . . that it is possible for a suspect’s Fifth Amendment right to be violated during in-custody questioning by a law-enforcement officer.” <footnotemark>31</footnotemark></p>
<p id="b561-5">Because of the adoption by Congress of Rule 5 (a) of the Federal Rules of Criminal Procedure, and this Court’s effectuation of that Rule in <em>McNabb </em>v. <em>United States, </em><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U. S. 332</a></span> (1943), and <em>Mallory </em>v. <em>United States, </em><span class="citation" data-id="105545"><a href="/opinion/105545/mallory-v-united-states/" aria-description="Citation for case: Mallory v. United States">354 U. S. 449</a></span> (1957), we have had little occasion in the past quarter century to reach the constitutional issues in dealing with federal interrogations. These supervisory rules, requiring production of an arrested person before a commissioner “without unnecessary delay” and excluding evidence obtained in default of that statutory obligation, were nonetheless responsive to the same considerations of Fifth Amendment policy that unavoidably face us now as to the States. In <em>McNabb, </em><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#343" aria-description="Citation for case: McNabb v. United States">318 U. S., at 343-344</a></span>, and in <em>Mallory, </em><span class="citation" data-id="105545"><a href="/opinion/105545/mallory-v-united-states/#455" aria-description="Citation for case: Mallory v. United States">354 U. S., at 455-456</a></span>, we recognized both the dangers of interrogation and the appropriateness of prophylaxis stemming from the very fact of interrogation itself.<footnotemark>32</footnotemark></p>
<p id="b561-6">Our decision in <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964), necessitates an examination of the scope of the privilege in state cases as well. In <em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Malloy</a></span>, </em>we squarely held the <page-number citation-index="1" label="464">*464</page-number>privilege applicable to the States, and held that the substantive standards underlying the privilege applied with full force to state court proceedings. There, as in <em>Murphy </em>v. <em>Waterfront Comm’n, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52</a></span> (1964), and <em>Griffin </em>v. <em>California, </em><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">380 U. S. 609</a></span> (1965), we applied the existing Fifth Amendment standards to the case before us. Aside from the holding itself, the reasoning in <em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Malloy</a></span> </em>made clear what had already become apparent — that the substantive and procedural safeguards surrounding admissibility of confessions in state cases had become exceedingly exacting, reflecting all the policies embedded in the privilege, 378 U. S., at 7-8.<footnotemark>33</footnotemark> The voluntariness doctrine in the state cases, as <em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Malloy</a></span> </em>indicates, encompasses all interrogation practices which are likely to exert such pressure upon an individual as to disable him from <page-number citation-index="1" label="465">*465</page-number>making a free and rational choice.<footnotemark>34</footnotemark> The implications of this proposition were elaborated in our decision in <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span>, decided one week after <em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Malloy</a></span> </em>applied the privilege to the States.</p>
<p id="b563-5">Our holding there stressed the fact that the police had not advised the defendant of his constitutional privilege to remain silent at the outset of the interrogation, and we drew attention to that fact at several points in the decision, 378 U. S., at 483, 485, 491. This was no isolated factor, but an essential ingredient in our decision. The entire thrust of police interrogation there, as in all the cases today, was to put the defendant in such an emotional state as to impair his capacity for rational judgment. The abdication of the constitutional privilege— the choice on his part to speak to the police — was not made knowingly or competently because of the failure to apprise him of his rights; the compelling atmosphere of the in-custody interrogation, and not an independent decision on his part, caused the defendant to speak.</p>
<p id="b563-6">A different phase of the <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>decision was significant in its attention to the absence of counsel during the questioning. There, as in the cases today, we sought a protective device to dispel the compelling atmosphere of the interrogation. In <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>, </em>however, the police did not relieve the defendant of the anxieties which they had created in the interrogation rooms. Rather, they denied his request for the assistance of counsel, 378 U. S., at 481, 488, 491.<footnotemark>35</footnotemark> This heightened his dilemma, and <page-number citation-index="1" label="466">*466</page-number>made his later statements the product of this compulsion. Cf. <em>Haynes </em>v. <em>Washington, </em><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#514" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503, 514</a></span> (1963). The denial of the defendant’s request for his attorney thus undermined his ability to exercise the privilege— to remain silent if he chose or to speak without any intimidation, blatant or subtle. The presence of counsel, in all the cases before us today, would be the adequate protective device necessary to make the process of police interrogation conform to the dictates of the privilege. His presence would insure that statements made in the government-established atmosphere are not the product of compulsion.</p>
<p id="b564-6">It was in this manner that <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>explicated another facet of the pre-trial privilege, noted in many of the Court’s prior decisions: the protection of rights at trial.<footnotemark>36</footnotemark> That counsel is present when statements are taken from an individual during interrogation obviously enhances the integrity of the fact-finding processes in court. The presence of an attorney, and the warnings delivered to the individual, enable the defendant under otherwise compelling circumstances to tell his story without fear, effectively, and in a way that eliminates the evils in the interrogation process. Without the protections flowing from adequate warnings and the rights of counsel, “all the careful safeguards erected around the giving of testimony, whether by an accused or any other witness, would become empty formalities in a procedure where the most compelling possible evidence of guilt, a confession, would have already been obtained at the unsupervised pleasure of the police.” <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#685" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 685</a></span> (1961) (Harlan, J., dissenting). Cf. <em>Pointer </em>v. <em>Texas, </em><span class="citation" data-id="9422988"><a href="/opinion/107014/pointer-v-texas/" aria-description="Citation for case: Pointer v. Texas">380 U. S. 400</a></span> (1965).</p>
<p id="b565-4"><page-number citation-index="1" label="467">*467</page-number>III.</p>
<p id="b565-5">Today, then, there can be no doubt that the Fifth Amendment privilege is available outside of criminal court proceedings and serves to protect persons in all settings in which their freedom of action is curtailed in any significant way from being compelled to incriminate themselves. We have concluded that without proper safeguards the process of in-custody interrogation of persons suspected or accused of crime contains inherently compelling pressures which work to undermine the individual’s will to resist and to compel him to speak where he would not otherwise do so freely. In order, to combat these pressures and to permit a full opportunity to exercise the privilege against self-incrimination, the accused must be adequately and effectively apprised of his rights and the exercise of those rights must be fully honored.</p>
<p id="b565-6">It is impossible for us to foresee the potential alternatives for protecting the privilege which might be devised by Congress or the States in the exercise of their creative rule-making capacities. Therefore we cannot say that the Constitution necessarily requires adherence to any particular solution for the inherent compulsions of the interrogation process as it is presently conducted. Our decision in no way creates a constitutional straitjacket which will handicap sound efforts at reform, nor is it intended to have this effect. We encourage Congress and the States to continue their laudable search for increasingly effective ways of protecting the rights of the individual while promoting efficient enforcement of our criminal laws. However, unless we are shown other procedures which are at least as effective in apprising accused persons of their right of silence and in assuring a continuous opportunity to exercise it, the following safeguards must be observed.</p>
<p id="b565-7">At the outset, if a person in custody is to be subjected to interrogation, he must first be informed in clear and <page-number citation-index="1" label="468">*468</page-number>unequivocal terms that he has the right to remain silent. For those unaware of the privilege, the warning is needed simply to make them aware of it — the threshold requirement for an intelligent decision as to its exercise. More important, such a warning is an absolute prerequisite in overcoming the inherent pressures of the interrogation atmosphere. It is not just the subnormal or woefully ignorant who succumb to an interrogator’s imprecations, whether implied or expressly stated, that the interrogation will continue until a confession is obtained or that silence in the face of accusation is itself damning and will bode ill when presented to a jury.<footnotemark>37</footnotemark> Further, the warning will show the individual that his interrogators are prepared to recognize his privilege should he choose to exercise it.</p>
<p id="b566-6">The Fifth Amendment privilege is so fundamental to our system of constitutional rule and the expedient of giving an adequate warning as to the availability of the privilege so simple, we will not pause to inquire in individual cases whether the defendant was aware of his rights without a warning being given. Assessments of the knowledge the defendant possessed, based on infor<page-number citation-index="1" label="469">*469</page-number>mation as to his age, education, intelligence, or prior contact with authorities, can never be more than speculation; <footnotemark>38</footnotemark> a warning is a clearcut fact. More important, whatever the background of the person interrogated, a warning at the time of the interrogation is indispensable to overcome its pressures and to insure that the individual knows he is free to exercise the privilege at that point in time.</p>
<p id="b567-4">The warning of the right to remain silent must be accompanied by the explanation that anything said can and will be used against the individual in court. This warning is needed in order to make him aware not only of the privilege, but also of the consequences of forgoing it. It is only through an awareness of these consequences that there can be any assurance of real understanding and intelligent exercise of the privilege. Moreover, this warning may serve to make the individual more acutely aware that he is faced with a phase of the adversary system — -that he is not in the presence of persons acting solely in his interest.</p>
<p id="b567-5">The circumstances surrounding in-custody interrogation can operate very quickly to overbear the will of one merely made aware of his privilege by his interrogators. Therefore, the right to have counsel present at the interrogation is indispensable to the protection of the Fifth Amendment privilege under the system we delineate today. Our aim is to assure that the individual’s right to choose between silence and speech remains unfettered throughout the interrogation process. A once-stated warning, delivered by those who will conduct the interrogation, cannot itself suffice to that end among those who most require knowledge of their rights. A mere <page-number citation-index="1" label="470">*470</page-number>warning given by the interrogators is not alone sufficient to accomplish that end. Prosecutors themselves claim that the admonishment of the right to remain silent without more “will benefit only the recidivist and the professional.” Brief for the National District Attorneys Association as <em>amicus curiae, </em>p. 14. Even preliminary advice given to the accused by his own attorney can be swiftly overcome by the secret interrogation process. Cf. <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#485" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478, 485, n. 5</a></span>. Thus, the need for counsel to protect the Fifth Amendment privilege comprehends not merely a right to consult with counsel prior to questioning, but also to have counsel present during any questioning if the defendant so desires.</p>
<p id="b568-6">The presence of counsel at the interrogation may serve several significant subsidiary functions as well. If the accused decides to talk to his interrogators, the assistance of counsel can mitigate the dangers of untrustworthiness. With a lawyer present the likelihood that the police will practice coercion is reduced, and if coercion is nevertheless exercised the lawyer can testify to it in court. The presence of a lawyer can also help to guarantee that the accused gives a fully accurate statement to the police and that the statement is rightly reported by the prosecution at trial. See <em>Crooker </em>v. <em>California, </em><span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/#443" aria-description="Citation for case: Crooker v. California">357 U. S. 433, 443-448</a></span> (1958) (Douglas, J., dissenting).</p>
<p id="b568-7">An individual need not make a pre-interrogation request for a lawyer. While such request affirmatively secures his right to have one, his failure to ask for a lawyer does not constitute a waiver. No effective waiver of the right to counsel during interrogation can be recognized unless specifically made after the warnings we here delineate have been given. The accused who does not know his rights and therefore does not make a request <page-number citation-index="1" label="471">*471</page-number>may be the person who most needs counsel. As the California Supreme Court has aptly put it:</p>
<blockquote id="b569-5">“Finally, we must recognize that the imposition of the requirement for the request would discriminate against the defendant who does not know his rights. The defendant who does not ask for counsel is the very defendant who most needs counsel. We cannot penalize a defendant who, not understanding his constitutional rights, does not make the formal request and by such failure demonstrates his helplessness. To require the request would be to favor the defendant whose sophistication or status had fortuitously prompted him to make it.” <em>People </em>v. <em>Dorado, </em><span class="citation" data-id="9549155"><a href="/opinion/1177555/people-v-dorado/#351" aria-description="Citation for case: People v. Dorado">62 Cal. 2d 338, 351</a></span>, <span class="citation" data-id="9549155"><a href="/opinion/1177555/people-v-dorado/#369" aria-description="Citation for case: People v. Dorado">398 P. 2d 361, 369-370</a></span>, <span class="citation" data-id="9549155"><a href="/opinion/1177555/people-v-dorado/#177" aria-description="Citation for case: People v. Dorado">42 Cal. Rptr. 169, 177-178</a></span> (1965) (Tobriner, J.).</blockquote>
<p id="b569-6">In <em>Carnley </em>v. <em>Cochran, </em><span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/#513" aria-description="Citation for case: Carnley v. Cochran">369 U. S. 506, 513</a></span> (1962), we stated: “[I]t is settled that where the assistance of counsel is a constitutional requisite, the right to be furnished counsel does not depend on a request.” This proposition applies with equal force in the context of providing counsel to protect an accused’s Fifth Amendment privilege in the face of interrogation.<footnotemark>39</footnotemark> Although the role of counsel at trial differs from the role during interrogation, the differences are not relevant to the question whether a request is a prerequisite.</p>
<p id="b569-7">Accordingly we hold that an individual held for interrogation must be clearly informed that he has the right to consult with a lawyer and to have the lawyer with him during interrogation under the system for protecting the privilege we delineate today. As with the warnings of the right to remain silent and that anything stated can be used in evidence against him, this warning is an absolute prerequisite to interrogation. No amount of <page-number citation-index="1" label="472">*472</page-number>circumstantial evidence that the person may have been aware of this right will suffice to stand in its stead. Only through such a warning is there ascertainable assurance that the accused was aware of this right.</p>
<p id="b570-6">If an individual indicates that he wishes the assistance of counsel before any interrogation occurs, the authorities cannot rationally ignore or deny his request on the basis that the individual does not have or cannot afford a retained attorney. The financial ability of the individual has no relationship to the scope of the rights involved here. The privilege against self-incrimination secured by the Constitution applies to all individuals. The need for counsel in order to protect the privilege exists for the indigent as well as the affluent. In fact, were we to limit these constitutional rights to those who can retain an attorney, our decisions today would be of little significance. The cases before us as well as the vast majority of confession cases with which we have dealt in the past involve those unable to retain counsel.<footnotemark>40</footnotemark> While authorities are not required to relieve the accused of his poverty, they have the obligation not to take advantage of indigence in the administration of justice.<footnotemark>41</footnotemark> Denial <page-number citation-index="1" label="473">*473</page-number>of counsel to the indigent at the time of interrogation while allowing an attorney to those who can afford one would be no more supportable by reason or logic than the similar situation at trial and on appeal struck down in <em>Gideon </em>v. <em>Wainwright, </em><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span> (1963), and <em>Douglas </em>v. <em>California, </em><span class="citation" data-id="9422548"><a href="/opinion/106546/douglas-v-california/" aria-description="Citation for case: Douglas v. California">372 U. S. 353</a></span> (1963).</p>
<p id="b571-5">In order fully to apprise a person interrogated of the extent of his rights under this system then, it is necessary to warn him not only that he has the right to consult with an attorney, but also that if he is indigent a lawyer will be appointed to represent him. Without this additional warning, the admonition of the right to consult with counsel would often be understood as meaning only that he can consult with a lawyer if he has one or has the funds to obtain one. The warning of a right to counsel would be hollow if not couched in terms that would convey to the indigent — the person most often subjected to interrogation — the knowledge that he too has a right to have counsel present.<footnotemark>42</footnotemark> As with the warnings of the right to remain silent and of the general right to counsel, only by effective and express explanation to the indigent of this right can there be assurance that he was truly in a position to exercise it.<footnotemark>43</footnotemark></p>
<p id="b571-6">Once warnings have been given, the subsequent procedure is clear. If the individual indicates in any man-<page-number citation-index="1" label="474">*474</page-number>hén, at any time prior to or during questioning, that he wishes to remain silent, the interrogation must cease.<footnotemark>44</footnotemark> At this point he has shown that he intends to exercise his Fifth Amendment privilege; any statement taken after the person invokes his privilege cannot be other than the product of compulsion, subtle or otherwise. Without the right to cut off questioning, the setting of in-custody interrogation operates on the individual to overcome free choice in producing a statement after the privilege has been once invoked. If the individual states that he wants an attorney, the interrogation must cease until an attorney is present. At that time, the individual must have an opportunity to confer with the attorney and to have him present during any subsequent questioning. If the individual cannot obtain an attorney and he indicates that he wants one before speaking to police, they must respect his decision to remain silent.</p>
<p id="b572-4">This does not mean, as some have suggested, that each police station must have a “station house lawyer” present at all times to advise prisoners. It does mean, however, that if police propose to interrogate a person they must make known to him that he is entitled to a lawyer and that if he cannot afford one, a lawyer will be provided for him prior to any interrogation. If authorities conclude that they will not provide counsel during a reasonable period of time in which investigation in the field is carried out, they may refrain from doing so without violating the person’s Fifth Amendment privilege so long as they do not question him during that time.</p>
<p id="b573-4"><page-number citation-index="1" label="475">*475</page-number>If the interrogation continues without the presence of an attorney and a statement is taken, a heavy burden rests on the government to demonstrate that the defendant knowingly and intelligently waived his privilege against self-incrimination and his right to retained or appointed counsel. <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#490" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478, 490, n. 14</a></span>. This Court has always set high standards of proof for the waiver of constitutional rights, <em>Johnson </em>v. <em>Zerbst, </em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458</a></span> (1938), and we re-assert these standards as applied to in-custody interrogation. Since the State is responsible for establishing the isolated circumstances under which the interrogation takes place and has the only means of making available corroborated evidence of warnings given during incommunicado interrogation, the burden is rightly on its shoulders.</p>
<p id="b573-5">An express statement that the individual is willing to make a statement and does not want an attorney followed closely by a statement could constitute a waiver. But a valid waiver will not be presumed simply from the silence of the accused after warnings are given or simply from the fact that a confession was in fact eventually obtained. A statement we made in <em>Carnley </em>v. <em>Cochran, </em><span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/#516" aria-description="Citation for case: Carnley v. Cochran">369 U. S. 506, 516</a></span> (1962), is applicable here:</p>
<blockquote id="b573-6">“Presuming waiver from a silent record is impermissible. The record must show, or there must be an allegation and evidence which show, that an accused was offered counsel but intelligently and understanding^ rejected the offer. Anything less is not waiver.”</blockquote>
<p id="b573-7">See also <em>Glasser </em>v. <em>United States, </em><span class="citation" data-id="103597"><a href="/opinion/103597/glasser-v-united-states/" aria-description="Citation for case: Glasser v. United States">315 U. S. 60</a></span> (1942). Moreover, where in-custody interrogation is involved, there is no room for the contention that the privilege is waived if the individual answers some questions or gives <page-number citation-index="1" label="476">*476</page-number>some information on his own prior to invoking his right to remain silent when interrogated.<footnotemark>45</footnotemark></p>
<p id="b574-5">Whatever the testimony of the authorities as to waiver of rights by an accused, the fact of lengthy interrogation or incommunicado incarceration before a statement is made is strong evidence that the accused did not validly waive his rights. In these circumstances the fact that the individual eventually made a statement is consistent with the conclusion that the compelling influence of the interrogation finally forced him to do so. It is inconsistent with any notion of a voluntary relinquishment of the privilege. Moreover, any evidence that the accused was threatened, tricked, or cajoled into a waiver will, of course, show that the defendant did not voluntarily waive his privilege. The requirement of warnings and waiver of rights is a fundamental with respect to the Fifth Amendment privilege and not simply a preliminary ritual to existing methods of interrogation.</p>
<p id="b574-6">The warnings required and the waiver necessary in accordance with our opinion today are, in the absence of a fully effective equivalent, prerequisites to the admissibility of any statement made by a defendant. No distinction can be drawn between statements which are direct confessions and statements which amount to “admissions” of part or all of an offense. The privilege against self-incrimination protects the individual from being compelled to incriminate himself in any manner; it does not distinguish degrees of incrimination. Sim<page-number citation-index="1" label="477">*477</page-number>ilarly, for precisely the same reason, no distinction may be drawn between inculpatory statements and statements alleged to be merely “exculpatory.” If a statement made were in fact truly exculpatory it would, of course, never be used by the prosecution. In fact, statements merely intended to be exculpatory by the defendant are often used to impeach his testimony at trial or to demonstrate untruths in the statement given under interrogation and thus to prove guilt by implication. These statements are incriminating in any meaningful sense of the word and may not be used without the full warnings and effective waiver required for any other statement. In <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>itself, the defendant fully intended his accusation of another as the slayer to be exculpatory as to himself.</p>
<p id="b575-5">The principles announced today deal with the protection which must be given to the privilege against self-incrimination when the individual is first subjected to police interrogation while in custody at the station or otherwise deprived of his freedom of action in any significant way. It is at this point that our adversary system of criminal proceedings commences, distinguishing itself at the outset from the inquisitorial system recognized in some countries. Under the system of warnings we delineate today or under any other system which may be devised and found effective, the safeguards to be erected about the privilege must come into play at this point.</p>
<p id="b575-6">Our decision is not intended to hamper the traditional function of police officers in investigating crime. See <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#492" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478, 492</a></span>. When an individual is in custody on probable cause, the police may, of course, seek out evidence in the field to be used at trial against him. Such investigation may include inquiry of persons not under restraint. General on-the-scene questioning as to facts surrounding a crime or other general questioning of citizens in the fact-finding process is not affected by our holding. It is an act of <page-number citation-index="1" label="478">*478</page-number>responsible citizenship for individuals to give whatever information they may have to aid in law enforcement. In such situations the compelling atmosphere inherent in the process of in-custody interrogation is not necessarily present.<footnotemark>46</footnotemark></p>
<p id="b576-6">In dealing with statements obtained through interrogation, we do not purport to find all confessions inadmissible. Confessions remain a proper element in. law enforcement. Any statement given freely and voluntarily without any compelling influences is, of course, admissible in evidence. The fundamental import of the privilege while an individual is in custody is not whether he is allowed to talk to the police without the benefit of warnings and counsel, but whether he can be interrogated. There is no requirement that police, stop a person who enters a police station and states that he wishes to confess to a crime,<footnotemark>47</footnotemark> or a person who calls the police to offer a confession or any other statement he desires to make. Volunteered statements of any kind are not barred by the Fifth Amendment and their admissibility is not affected by our holding today. '</p>
<p id="b576-7">To summarize, we hold that when an individual is taken into custody or otherwise deprived of his freedom by the authorities in any significant way and is subjected to questioning, the privilege against self-incrimination is jeopardized. Procedural safeguards must be employed to <page-number citation-index="1" label="479">*479</page-number>protect the privilege, and unless other fully effective means are adopted to notify the person of his right of silence and to assure that the exercise of the right will be scrupulously honored, the following measures are required. He must be warned prior to any questioning that he has the right to remain silent, that anything he says can be used against him in a court of law, that he has the right to the presence of an attorney, and that if he cannot afford an attorney one will be appointed for him prior to any questioning if he so desires. Opportunity to exercise these rights must be afforded to him throughout the interrogation. After such warnings have been given, and such opportunity afforded him, the individual may knowingly and intelligently waive these rights and agree to answer questions or make a statement. But unless and until such warnings and waiver are demonstrated by the prosecution at trial, no evidence obtained as a result of interrogation can be used against him.<footnotemark>48</footnotemark></p>
<p id="b577-5">IV.</p>
<p id="b577-6">A recurrent argument made in these cases is that' society’s need for interrogation outweighs the privilege. This argument is not unfamiliar to this Court. See, <em>e. g., Chambers </em>v. <em>Florida, </em><span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#240" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227, 240-241</a></span> (1940). The whole thrust of our foregoing discussion demonstrates that the Constitution has prescribed the rights of the individual when confronted with the power of government when it provided in the Fifth Amendment that an individual cannot be compelled to be a witness against himself. That right cannot be abridged. As Mr. Justice Brandéis once observed:</p>
<blockquote id="b577-7">“Decency, security and liberty alike demand that government officials shall be subjected to the same <page-number citation-index="1" label="480">*480</page-number>rules of conduct that are commands to the citizen. In a government of laws, existence of the government will be imperilled if it fails to observe the law scrupulously. Our Government is the potent, the omnipresent teacher. For good or' for ill, it teaches the whole people by its example. Crime is contagious. If the Government becomes a lawbreaker, it breeds contempt for law; it invites every man to become a law unto himself; it invites anarchy. To declare that in the administration of the criminal law the end justifies the means . . . would bring terrible retribution. Against that pernicious doctrine this Court should resolutely set its face.” <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#485" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 485</a></span> (1928) (dissenting opinion) ,<footnotemark>49</footnotemark></blockquote>
<p id="b578-5">In this connection, one of our country’s distinguished jurists has pointed out: “The quality of a nation’s civilization can be largely measured by the methods it uses in the enforcement of its criminal law.” <footnotemark>50</footnotemark></p>
<p id="b578-6">If the individual desires to exercise his privilege, he has the right to do so. This is not for the authorities to decide. An attorney may advise his client not to talk to police until he has had an opportunity to investigate the case, or he may wish to be present with his client during any police questioning. In doing so an attorney is merely exercising the good professional judgment he has been, taught. This is not cause for considering the attorney a menace to law enforcement. He is merely carrying out what he is sworn to do under his oáth— to protect to the extent of his ability the rights of his <page-number citation-index="1" label="481">*481</page-number>client. In fulfilling this responsibility the attorney plays a vital role in the administration of criminal justice under our Constitution.</p>
<p id="b579-5">In announcing these principles, we are not unmindful of the burdens which law enforcement officials must bear, often under trying circumstances. We also fully recognize the obligation of all citizens to aid in enforcing the criminal laws. This- Court, while protecting individual rights, has always given ample latitude to law enforcement agencies in the legitimate exercise of their duties. The limits we have placed on the interrogation process should not constitute an undue interference with a proper system of law enforcement. As we have noted, our decision does not in any way preclude police from carrying out their traditional investigatory functions. Although confessions may play an important role in some convictions, the cases before us present graphic examples of the overstatement of the “need” for confessions. In each case authorities conducted interrogations ranging up to five days in duration despite the presence, through standard investigating practices, of considerable evidence against each defendant.<footnotemark>51</footnotemark> Further examples are chronicled in our prior cases. See, <em>e. g., Haynes </em>v. <em>Washington, </em><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#518" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503, 518-519</a></span> (1963); <em>Rogers </em>v. <em>Richmond, </em><span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#541" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 541</a></span> (1961); <em>Malinski </em>v. <em>New York, </em><span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#402" aria-description="Citation for case: Malinski v. New York">324 U. S. 401, 402</a></span> (1945).<footnotemark>52</footnotemark></p>
<p id="b580-4"><page-number citation-index="1" label="482">*482</page-number>It is also urged that an unfettered right to detention for interrogation should be allowed because it will often redound to the benefit of the person questioned. When police inquiry determines that there is no reason to believe that the person has committed any crime, it is said, he will be released without need for further formal procedures. The person who has committed no offense, however, will be better able to clear himself after warnings with counsel present than without. It can be assumed that in such circumstances a lawyer would advise his client to talk freely to police in order to clear himself.</p>
<p id="b580-5">Custodial interrogation, by contrast, does not necessarily afford the innocent an opportunity to clear themselves. A serious consequence of the present practice of the interrogation alleged to be beneficial for the innocent is that many arrests “for investigation” subject large numbers of innocent persons to detention and interrogation. In one of the cases before us, No. 584, <em>California </em>v. <em>Stewart, </em>police held four persons, who were in the defendant’s house at the time of the arrest, in jail for five days until defendant confessed. At that time they were finally released. Police stated that there was “no evidence to connect them with any crime.” Available statistics on the extent of this practice where it is condoned indicate that these four are far from alone in being subjected to arrest, prolonged detention, and interrogation without the requisite probable cause.<footnotemark>53</footnotemark></p>
<p id="b581-5"><page-number citation-index="1" label="483">*483</page-number>Over the years the Federal Bureau of Investigation has compiled an exemplary record of effective law enforcement while advising any suspect or arrested person, at the outset of an interview, that he is not required to make a statement, that any statement may be used against him in court, that the individual may obtain the services of an attorney of his own choice and, more recently, that he has a right to free counsel if he is unable to pay.<footnotemark>54</footnotemark> A letter received from the Solicitor General in response to a question from the Bench makes it clear that the present pattern of warnings and respect for the <page-number citation-index="1" label="484">*484</page-number>rights of the individual followed as a practice by the FBI is consistent with the procedure which we delineate today. It states:</p>
<blockquote id="b582-4">“At the oral argument of the above cause, Mr. Justice Fortas asked whether I could provide certain information as to the practices followed by the Federal Bureau of Investigation. I have directed these questions to the attention of the Director of the Federal Bureau of Investigation and am submitting herewith a statement of the questions and of the answers which we have received.</blockquote>
<blockquote id="b582-5">“ ‘(1) When an individual is interviewed by agents of the Bureau, what warning is given to him?</blockquote>
<blockquote id="b582-6">“ 'The standard warning long given by Special Agents of the FBI to both suspects and persons under arrest is that the person has a right to say nothing and a right to counsel, and that any statement he does make may be used against him in court. Examples of this warning are to be found in the <em>Westover </em>case at <span class="citation" data-id="267168"><a href="/opinion/267168/carl-calvin-westover-v-united-states/" aria-description="Citation for case: Carl Calvin Westover v. United States">342 F. 2d 684</a></span> (1965), and <em>Jackson </em>v. <em>U. S., </em><span class="citation" data-id="9450314"><a href="/opinion/265586/john-w-jackson-jr-v-united-states/" aria-description="Citation for case: John W. Jackson, Jr. v. United States">337 F. 2d 136</a></span> (1964), cert. den. <span class="citation multiple-matches"><a href="/c/U.%20S./380/935/">380 U. S. 935</a></span>.</blockquote>
<blockquote id="b582-7">“ 'After passage of the Criminal Justice Act of 1964, which provides free counsel for Federal defendants unable to pay, we added to our instructions to Special Agents the requirement that any person who is under arrest for an offense under FBI jurisdiction, or whose arrest is contemplated following the interview, must also be advised of his right to free counsel if he is unable to pay, and the fact that such counsel will be assigned by the Judge. At the same time, we broadened the right to counsel warn<page-number citation-index="1" label="485">*485</page-number>ing to read counsel of his own choice, or anyone else with whom he might wish to speak.</blockquote>
<blockquote id="b583-5">“ ‘(2) When is the warning given?</blockquote>
<blockquote id="b583-6">“ ‘The FBI warning is given to a suspect at the very outset of the interview, as shown in the <em>West-over </em>case, cited above. The warning may be given to a person arrested as soon as practicable after the arrest, as shown in the <em>Jackson </em>case, also cited above, and in <em>U. S. </em>v. <em>Konigsberg, </em><span class="citation multiple-matches"><a href="/c/F.%202d/336/844/">336 F. 2d 844</a></span> (1964), cert. den. <span class="citation" data-id="8951108"><a href="/opinion/8959978/konigsberg-v-united-states/" aria-description="Citation for case: Konigsberg v. United States">379 U. S. 933</a></span>, but in any event it must precede the interview with the person for a confession or admission of his own guilt.</blockquote>
<blockquote id="b583-7">“ ‘(3) What is the Bureau’s practice in the event that (a) the individual requests counsel and (b) counsel appears?</blockquote>
<blockquote id="b583-8">“ ‘When the person who has been warned of his right to counsel decides that he wishes to consult with counsel before making a statement, the interview is terminated at that point, <em>Shultz </em>v. <em>U. S., </em><span class="citation" data-id="269239"><a href="/opinion/269239/clayman-clifford-shultz-v-united-states/" aria-description="Citation for case: Clayman Clifford Shultz v. United States">351 F. 2d 287</a></span> (1965). It may be continued, however, as to all matters <em>other </em>than the person’s own guilt or innocence. If he is indecisive in his request for counsel, there may be some question on whether he did or did not waive counsel. Situations of this kind must necessarily be left to the judgment of the interviewing Agent. For example, in <em>Hiram </em>v. <em>U. S., </em><span class="citation" data-id="270022"><a href="/opinion/270022/randolph-k-hiram-v-united-states/" aria-description="Citation for case: Randolph K. Hiram v. United States">354 F. 2d 4</a></span> (1965), the Agent’s conclusion that the person arrested had waived his right to counsel was upheld by the courts.</blockquote>
<blockquote id="b583-9">“ ‘A person being interviewed and desiring to consult counsel by telephone must be permitted to do so, as shown in <em>Caldwell </em>v. <em>U. S., </em><span class="citation" data-id="269286"><a href="/opinion/269286/william-ambrose-caldwell-v-united-states/" aria-description="Citation for case: William Ambrose Caldwell v. United States">351 F. 2d 459</a></span> (1965). When counsel appears in person, he is permitted to confer with his client in private.</blockquote>
<blockquote id="b584-5"><page-number citation-index="1" label="486">*486</page-number>“ ‘(4) What is the Bureau’s practice if the individual requests counsel, but cannot afford to retain an attorney?</blockquote>
<blockquote id="b584-6">. “ Tf any person being interviewed after warning of counsel decides that he wishes to consult with counsel before proceeding further the interview is terminated, as shown above. FBI Agents do not pass judgment on the ability of the person to pay for counsel. They do, however, advise those who have been arrested for an offense under FBI jurisdiction, or whose arrest is contemplated following the interview, of a right to free counsel <em>if </em>they are unable to pay, and the availability of such counsel from the Judge.’ ”<footnotemark>55</footnotemark></blockquote>
<p id="b584-7">The practice of the FBI can readily be emulated by state and local enforcement agencies. The argument that the FBI deals with different crimes than are dealt with by state authorities does not mitigate the significance of the FBI experience.<footnotemark>56</footnotemark></p>
<p id="b584-8">The experience in some other countries also suggests that the danger to law enforcement in curbs on interrogation is overplayed. The English procedure since 1912 under the Judges’ Rules is significant. As recently <page-number citation-index="1" label="487">*487</page-number>strengthened, the Rules require that a cautionary warning be given an accused by a police officer as soon as he has evidence that affords reasonable grounds for suspicion; they also require that any statement made be given by the accused without questioning by police.<footnotemark>57</footnotemark> <page-number citation-index="1" label="488">*488</page-number>The right of the individual to consult with an attorney during this period is expressly recognized.<footnotemark>58</footnotemark></p>
<p id="b586-6">The safeguards present under Scottish law may be even greater than in England. Scottish judicial decisions bar use in evidence of most confessions obtained through police interrogation.<footnotemark>59</footnotemark> In India, confessions made to police not in the presence of a magistrate have been ex-<page-number citation-index="1" label="489">*489</page-number>eluded by rule of evidence since 1872, at a time when it operated under British law.<footnotemark>60</footnotemark> Identical provisions appear in the Evidence Ordinance of Ceylon, enacted in 1895.<footnotemark>61</footnotemark> Similarly, in our country the Uniform Code of Military Justice has long provided that no suspect may be interrogated without first being warned of his right not to make a statement and that any statement he makes may be used against him.<footnotemark>62</footnotemark> Denial of the right to consult counsel during interrogation has also been proscribed by military tribunals.<footnotemark>63</footnotemark> There appears to have been no marked detrimental effect on criminal law enforcement in these jurisdictions as a result of these rules. Conditions of law enforcement in our country are sufficiently similar to permit reference to this experience as assurance that lawlessness will not result from warning an individual of his rights or allowing him to exercise them. Moreover, it is consistent with our legal system that we give at least as much protection to these rights as is given in the jurisdictions described. We deal in our country with rights grounded in a specific requirement of the Fifth Amendment of the Constitution, <page-number citation-index="1" label="490">*490</page-number>whereas other jurisdictions arrived at their conclusions on the basis of principles of justice not so specifically defined.<footnotemark>64</footnotemark></p>
<p id="b588-6">It is also urged upon us that we withhold decision on this issue until state legislative bodies and advisory groups have had an opportunity to deal with these problems by rule making.<footnotemark>65</footnotemark> We have already pointed out that the Constitution does not require any specific code of procedures for protecting the privilege against self-incrimination during custodial interrogation. Congress and the States are free to develop their own safeguards for the privilege, so long as they are fully as effective as those described above in informing accused persons of their right of silence and in affording a continuous opportunity to exercise it. In any event, however, the issues presented are of constitutional dimensions and must be determined by the courts. The admissibility of a statement in the face of a claim that it was obtained in violation of the defendant’s constitutional rights is an issue the resolution of which has long since been undertaken by this Court. See <em>Hopt </em>v. <em>Utah, </em><span class="citation" data-id="91057"><a href="/opinion/91057/hopt-v-people-of-territory-of-utah/" aria-description="Citation for case: Hopt v. People of Territory of Utah">110 U. S. 574</a></span> (1884). Judicial solutions to problems of constitutional dimension have evolved decade by decade. As courts have been presented with the need to enforce constitutional rights, they have found means of doing so. That was our responsibility when <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>was before us and it is our <page-number citation-index="1" label="491">*491</page-number>responsibility today. Where rights secured by the Constitution are involved, there can be no rule making or legislation which would abrogate them.</p>
<p id="b589-5">V.</p>
<p id="b589-6">Because of the nature of the problem and because of its recurrent significance in numerous cases, we have to this point discussed the relationship of the Fifth Amendment privilege to police interrogation without specific concentration on the facts of the cases before us. We turn now to these facts to consider the application to these cases of the constitutional principles discussed above. In each instance, we have concluded that statements were obtained from the defendant under circumstances that did not meet constitutional standards for protection of the privilege.</p>
<p id="b589-7">No. 759. <em>Miranda </em>v. <em>Arizona.</em></p>
<p id="b589-8">On March 13, 1963, petitioner, Ernesto Miranda, was arrested at his home and taken in custody to a Phoenix police station. He was there identified by the complaining witness. The police then took him to “Interrogation Room No. <em>2” </em>of the detective bureau. There he was questioned by two police officers. The officers admitted at trial that Miranda was not advised that he had a right to have an attorney present.<footnotemark>66</footnotemark> Two hours later, the <page-number citation-index="1" label="492">*492</page-number>officers emerged from the interrogation room with a written confession signed by Miranda. At the top of the statement was a typed paragraph stating that the confession was made voluntarily, without threats or promises of immunity and “with full knowledge of my legal rights, understanding any statement I make may be used against me.” <footnotemark>67</footnotemark></p>
<p id="b590-6">At his trial before a jury, the written confession was admitted into evidence over the objection of defense counsel, and the officers testified to the prior oral confession made by Miranda during the interrogation. Miranda was found guilty of kidnapping and rape. He was sentenced to 20 to 30 years’ imprisonment on each count, the sentences to run concurrently. On appeal, the Supreme Court of Arizona held that Miranda’s constitutional rights were not violated in obtaining the confession and affirmed the conviction. <span class="citation" data-id="1297557"><a href="/opinion/1297557/state-v-miranda/" aria-description="Citation for case: State v. Miranda">98 Ariz. 18</a></span>, <span class="citation" data-id="1297557"><a href="/opinion/1297557/state-v-miranda/" aria-description="Citation for case: State v. Miranda">401 P. 2d 721</a></span>. In reaching its decision, the court emphasized heavily the fact that Miranda did not specifically request counsel.</p>
<p id="b590-7">We reverse. From the testimony of the officers and by the admission of respondent, it is clear that Miranda was not in any way apprised of his right to consult with an attorney and to have one present during the interrogation, nor was his right not to be compelled to incriminate himself effectively protected in any other manner. Without these warnings the statements were inadmissible. The mere fact that he signed a statement which contained a typed-in clause stating that he had “full knowledge” of his “legal rights” does not approach the knowing and intelligent waiver required to relinquish constitutional rights. Cf. <em>Haynes </em>v. <em>Washington, </em><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#512" aria-description="Citation for case: Haynes v. Washington">373 U. S. <page-number citation-index="1" label="493">*493</page-number>503, 512-513</a></span> (1963); <em>Haley </em>v. <em>Ohio, </em><span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/#601" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596, 601</a></span> (1948) (opinion of Mr. Justice Douglas).</p>
<p id="b591-5">No. 760. <em>Vignera </em>v. <em><span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">New York</a></span>.</em></p>
<p id="b591-6">Petitioner, Michael Vignera, was picked up by New York police on October 14, 1960, in connection with the robbery three days earlier of a Brooklyn dress shop. They took him to the 17th Detective Squad headquarters in Manhattan. Sometime thereafter he was taken to the 66th Detective Squad. There a detective questioned Vignera with respect to the robbery. Vignera orally admitted the robbery to the detective. The detective was asked on cross-examination at trial by defense counsel whether Vignera was warned of his right to counsel before being interrogated. The prosecution objected to the question and the trial judge sustained the objection. Thus, the defense was precluded from making any showing that warnings had not been given. While at the 66th Detective Squad, Vignera was identified by the s'tore owner and a saleslady as the man who robbed the dress shop. At about 3 p. m. he was formally arrested. The police then transported him to still another station, the 70th Precinct in Brooklyn, “for detention.” At 11 p. m. Vignera was questioned by an assistant district attorney in the presence of a hearing reporter who transcribed the questions and Vignera’s answers. This verbatim account of these proceedings contains no statement of any warnings given by the assistant district attorney. At Vignera’s trial on a charge of first degree robbery, the detective testified as to the oral confession. The transcription of the statement taken was also introduced in evidence. At the conclusion of the testimony, the trial judge charged the jury in part as follows:</p>
<blockquote id="b591-7">“The law doesn’t say that the confession is void or invalidated because the police officer didn’t advise the defendant as to his rights. Did you hear what <page-number citation-index="1" label="494">*494</page-number>I said? I am telling you what the law of the State of New York is.”</blockquote>
<p id="b592-6">Yignera was found guilty of first degree robbery. He was subsequently adjudged a third-felony offender and sentenced to 30 to 60 years’ imprisonment.<footnotemark>68</footnotemark> The conviction was affirmed without opinion by the Appellate Division, Second Department, 21 App. Div. 2d 752, 252 N. Y. S. 2d 19, and by the Court of Appeals, also without opinion, 15 N. Y. 2d 970, <span class="citation multiple-matches"><a href="/c/N.%20E.%202d/207/527/">207 N. E. 2d 527</a></span>, 259 N. Y. S. 2d 857, remittitur amended, 16 N. Y. 2d 614, <span class="citation multiple-matches"><a href="/c/N.%20E.%202d/209/110/">209 N. E. 2d 110</a></span>, 261 N. Y. S. 2d 65. In argument to the Court of Appeals, the State contended that Vignera had no constitutional right to be advised of his right to counsel or his privilege against self-incrimination.</p>
<p id="b592-7">We reverse. The foregoing indicates that Vignera was not warned of any of his rights before the questioning by the detective and by the assistant district attorney. No other steps were taken to protect these rights. Thus he was not effectively apprised of his Fifth Amendment privilege or of his right to have counsel present and his statements are inadmissible.</p>
<p id="b592-8">No. 761. <em>Westover </em>v. <em>United States.</em></p>
<p id="b592-9">At approximately 9:45 p. m. on March 20, 1963, petitioner, Carl Calvin Westover, was arrested by local police in Kansas City as a suspect in two Kansas City robberies. A report was also received from the FBI that he was wanted on a felony charge in California. The local authorities took him to a police station and placed him in a line-up on the local charges, and at about 11:45 p. m. he was booked. Kansas City police interrogated West-<page-number citation-index="1" label="495">*495</page-number>over on the night of his arrest. He denied any knowledge of criminal activities. The next day local officers interrogated him again throughout the morning. Shortly before noon they informed the FBI that they were through interrogating Westover and that the FBI could proceed to interrogate him. There is nothing in the record to indicate that Westover was ever given any warning as to his rights by local police. At noon, three special agents of the FBI continued the interrogation in a private interview room of the Kansas City Police Department, this time with respect to the robbery of a savings and loan association and a bank in Sacramento, California. After two or two and one-half hours, West-over signed separate confessions to each of these two robberies which had been prepared by one of the agents during the interrogation. At trial one of the agents testified, and a paragraph on each of the statements states, that the agents advised Westover that he did not have to make a statement, that any statement he made could be used against him, and that he had the right to see an attorney.</p>
<p id="b593-5">Westover was tried by a jury in federal court and convicted of the California robberies. His statements were introduced at trial. He was sentenced to 15 years’ imprisonment on each count, the sentences to run consecutively. On appeal, the conviction was affirmed by the Court of Appeals for the Ninth Circuit. <span class="citation" data-id="267168"><a href="/opinion/267168/carl-calvin-westover-v-united-states/" aria-description="Citation for case: Carl Calvin Westover v. United States">342 F. 2d 684</a></span>.</p>
<p id="b593-6">We reverse. On the facts of this case we cannot find that Westover knowingly and intelligently waived his right to remain silent and his right to consult with counsel prior to the time he made the statement.<footnotemark>69</footnotemark> At the <page-number citation-index="1" label="496">*496</page-number>time the FBI agents began questioning Westover, he had been in custody for over 14 hours and had been interrogated at length during that period. The FBI interrogation began immediately upon the conclusion of the interrogation by Kansas City police and was conducted in local police headquarters. Although the two law enforcement authorities are legally distinct and the crimes for which they interrogated Westover were different, the impact on him was that of a continuous period of questioning. There is no evidence of any warning given prior to the FBI interrogation nor is there any evidence of an articulated waiver of rights after the FBI commenced its interrogation. The record simply shows that the defendant did in fact confess a short time after being turned over to the FBI following interrogation by local police. Despite the fact that the FBI agents gave warnings at the outset of their interview, from West-over’s point of view the warnings came at the end of the interrogation process. In these circumstances an intelligent waiver of constitutional rights cannot be assumed.</p>
<p id="b594-6">We do not suggest that law enforcement authorities are precluded from questioning any individual who has been held for a period of time by other authorities and interrogated by them without appropriate warnings. A different case would be presented if an accused were taken into custody by the second authority, removed both in time and place from his original surroundings, and then adequately advised of his rights and given an opportunity to exercise them. But here the FBI interrogation was conducted immediately following the state interrogation in the same police station — in the same compelling surroundings. Thus, in obtaining a confession from West-<page-number citation-index="1" label="497">*497</page-number>over the federal authorities were the beneficiaries of the pressure applied by the local in-custody interrogation. In these circumstances the giving of warnings alone was not sufficient to protect the privilege.</p>
<p id="b595-5">No. 584. <em>California </em>v. <em>Stewart.</em></p>
<p id="b595-6">In the course of investigating a series of purse-snatch robberies in which one of the victims had died of injuries inflicted by her assailant, respondent, Roy Allen Stewart, was pointed out to Los Angeles police as the endorser of dividend checks taken in one of the robberies. At about 7:15 p. m., January 31, 1963, police officers went to Stewart’s house and arrested him. One of the officers asked Stewart if they could search the house, to which he replied, “Go ahead.” The search turned up various items taken from the five robbery victims. At the time of Stewart’s arrest, police also arrested Stewart’s wife and three other persons who were visiting him. These four were jailed along with Stewart and were interrogated. Stewart was taken to the University Station of the Los Angeles Police Department where he was placed in a cell. During the next five days, police interrogated Stewart on nine different occasions. Except during the first interrogation session, when he was confronted with an accusing witness, Stewart was isolated with his interrogators.</p>
<p id="b595-7">During the ninth interrogation session, Stewart admitted that he had robbed the deceased and stated that he had not meant to hurt her. Police then brought Stewart before a magistrate for the first time. Since there was no evidence to connect them with any crime, the police then released the other four persons arrested with him.</p>
<p id="b595-8">Nothing in the record specifically indicates whether Stewart was or was not advised of his right to remain silent or his right to counsel. In a number of instances, <page-number citation-index="1" label="498">*498</page-number>however, the interrogating officers were asked to recount everything that was said during the interrogations. None indicated that Stewart was ever advised of his rights.</p>
<p id="b596-6">Stewart was charged with kidnapping to commit robbery, rape, and murder. At his trial, transcripts of the first interrogation and the confession at the last interrogation were introduced in evidence. The jury found Stewart guilty of robbery and first degree murder and fixed the penalty as death. On appeal, the Supreme Court of California reversed. <span class="citation" data-id="9791096"><a href="/opinion/2608355/people-v-stewart/" aria-description="Citation for case: People v. Stewart">62 Cal. 2d 571</a></span>, <span class="citation" data-id="9791096"><a href="/opinion/2608355/people-v-stewart/" aria-description="Citation for case: People v. Stewart">400 P. 2d 97</a></span>, <span class="citation" data-id="9791096"><a href="/opinion/2608355/people-v-stewart/" aria-description="Citation for case: People v. Stewart">43 Cal. Rptr. 201</a></span>. It held that under this Court’s decision in <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>, </em>Stewart should have been advised of his right to remain silent and of his right to counsel and that it would not presume in the face of a silent record that the police advised Stewart of his rights.<footnotemark>70</footnotemark></p>
<p id="b596-7">We affirm.<footnotemark>71</footnotemark> In dealing with custodial interrogation, we will not presume that a defendant has been effectively apprised of his rights and that his privilege against self-incrimination has been adequately safeguarded on a record that does not show that any warnings have been given or that any effective alternative has been employed. Nor can a knowing and intelligent waiver of <page-number citation-index="1" label="499">*499</page-number>these rights be assumed on a silent record. Furthermore, Stewart’s steadfast denial of the alleged offenses through eight of the nine interrogations over a period of five days is subject to no other construction than that he was compelled by persistent interrogation to forgo his Fifth Amendment privilege.</p>
<p id="b597-4">Therefore, in accordance with the foregoing, the judgments of the Supreme Court of Arizona in No. 759, of the New York Court of Appeals in No. 760, and of the Court of Appeals for the Ninth Circuit in No. 761 are reversed. The judgment of the Supreme Court of California in No. 584 is affirmed.</p>
<p id="b597-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b538-7"> Compare <em>United States </em>v. <em>Childress, </em><span class="citation" data-id="268400"><a href="/opinion/268400/united-states-v-freddie-lee-childress/" aria-description="Citation for case: United States v. Freddie Lee Childress">347 F. 2d 448</a></span> (C. A. 7th Cir. 1965), with <em>Collins </em>v. <em>Beto, </em><span class="citation" data-id="9450950"><a href="/opinion/268701/clarence-collins-v-george-j-beto-director-texas-department-of/" aria-description="Citation for case: Clarence Collins v. George J. Beto, Director, Texas...">348 F. 2d 823</a></span> (C. A. 5th Cir. 1965). Compare <em>People </em>v. <em>Dorado, </em><span class="citation" data-id="9549155"><a href="/opinion/1177555/people-v-dorado/" aria-description="Citation for case: People v. Dorado">62 Cal. 2d 338</a></span>, <span class="citation" data-id="9549155"><a href="/opinion/1177555/people-v-dorado/" aria-description="Citation for case: People v. Dorado">398 P. 2d 361</a></span>, <span class="citation" data-id="9549155"><a href="/opinion/1177555/people-v-dorado/" aria-description="Citation for case: People v. Dorado">42 Cal. Rptr. 169</a></span> (1964) with <em>People </em>v. <em>Hartgraves, </em><span class="citation" data-id="2221754"><a href="/opinion/2221754/the-people-v-hartgraves/" aria-description="Citation for case: The People v. Hartgraves">31 Ill. 2d 375</a></span>, <span class="citation" data-id="2221754"><a href="/opinion/2221754/the-people-v-hartgraves/" aria-description="Citation for case: The People v. Hartgraves">202 N. E. 2d 33</a></span> (1964).</p>
</footnote>
<footnote label="2">
<p id="b538-8"> See, <em>e. g., </em>Enker <em>&amp; </em>Elsen, Counsel for the Suspect: <em>Massiah </em>v. <em>United States </em>and <em>Escobedo </em>v. <em>Illinois, </em><span class="citation no-link">49 Minn. L. Rev. 47</span> (1964); Herman, The Supreme Court and Restrictions on Police Interrogation, 25 Ohio St. L. J. 449 (1964); Kamisar, Equal Justice in the Gatehouses and Mansions of American Criminal Procedure, in Criminal Justice in Our Time 1 (1965); Dowling, Escobedo and <page-number citation-index="1" label="441">*441</page-number>Beyond: The Need for a Fourteenth Amendment Code of Criminal Procedure, 56 J. Crim. L., C. &amp; P. S. 143, 156 (1965).</p>
<p id="b539-6">The complex problems also prompted discussions by jurists. Compare Bazelon, Law, Morality, and Civil Liberties, 12 U. C. L. A. L. Rev. 13 (1964), with Friendly, The Bill of Rights as a Code of Criminal Procedure, <span class="citation no-link">53 Calif. L. Rev. 929</span> (1965).</p>
</footnote>
<footnote label="3">
<p id="b539-7"> For example, the Los Angeles Police Chief stated that “If the police are required . . . to . . . establish that the defendant was apprised of his constitutional guarantees of silence and legal counsel prior to the uttering of any admission or confession, and that he intelligently waived these guarantees ... a whole Pandora’s box is opened as to under what circumstances . . . can a defendant intelligently waive these rights. . . . Allegations that modern criminal investigation can compensate for the lack of a confession or admission in every criminal case is totally absurd!” Parker, 40 L. A. Bar Bull. 603, 607, 642 (1965). His prosecutorial counterpart, District Attorney Younger, stated that “[I]t begins to appear that many of these seemingly restrictive decisions are going to contribute directly to a more effective, efficient and professional level of law enforcement.” L. A. Times, Oct. 2, 1965, p. 1. The former Police Commissioner of New York, Michael J. Murphy, stated of <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>: </em>“What the Court is doing is akin to requiring one boxer to fight by Marquis of Queensbury rules while permitting the other to butt, gouge and bite.” N. Y. Times, May 14, 1965, p. 39. The former United States Attorney for the District of Columbia, David C. Acheson, who is presently Special Assistant to the Secretary of the Treasury (for Enforcement), and directly in charge of the Secret Service and the Bureau of Narcotics, observed that “Prosecution procedure has, at most, only the most remote causal connection with crime. Changes in court decisions and prosecution procedure would have about the same effect on the crime rate as an aspirin would have on a tumor of the brain.” Quoted in Herman, <em>supra, </em>n. 2, at 500, n. 270. Other views on the subject in general are collected in Weisberg, Police Interrogation of Arrested Persons: A Skeptical View, 52 J. Crim. L., C. &amp; P. S. 21 (1961).</p>
</footnote>
<footnote label="4">
<p id="b542-8"> This is what we meant in <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>when we spoke of an investigation which had focused on an accused.</p>
</footnote>
<footnote label="5">
<p id="b543-8"> See, for example, IV' National Commission on Law Observance and Enforcement, Report on Lawlessness in Law Enforcement (1931) <page-number citation-index="1" label="446">*446</page-number>[Wickersham Report]; Booth, Confessions, and Methods Employed in Procuring Them, 4 So. Calif. L. Rev. 83 (1930); Kauper, Judicial Examination of the Accused — A Remedy for the Third Degree, <span class="citation no-link">30 Mich. L. Rev. 1224</span> (1932). It is significant that instances of third-degree treatment of prisoners almost invariably took place during the period between arrest and preliminary examination. Wicker-sham Report, at 169; Hall, The Law of Arrest in Relation to Contemporary Social Problems, <span class="citation no-link">3 U. Chi. L. Rev. 345</span>, 357 (1936). See also Foote, Law and Police Practice: Safeguards in the Law of Arrest, <span class="citation no-link">52 Nw. U. L. Rev. 16</span> (1957).</p>
</footnote>
<footnote label="6">
<p id="b544-11"> <em>Brown </em>v. <em>Mississippi, </em><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936); <em>Chambers </em>v. <em>Florida, </em><span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span> (1940); <em>Canty </em>v. <em>Alabama, </em><span class="citation" data-id="8155149"><a href="/opinion/8193214/canty-v-alabama/" aria-description="Citation for case: Canty v. Alabama">309 U. S. 629</a></span> (1940); <em>White </em>v. <em>Texas, </em><span class="citation" data-id="103368"><a href="/opinion/103368/white-v-texas/" aria-description="Citation for case: White v. Texas">310 U. S. 530</a></span> (1940); <em>Vernon </em>v. <em>Alabama, </em><span class="citation" data-id="8156474"><a href="/opinion/8194539/vernon-v-alabama/" aria-description="Citation for case: Vernon v. Alabama">313 U. S. 547</a></span> (1941); <em>Ward </em>v. <em>Texas, </em><span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/" aria-description="Citation for case: Ward v. Texas">316 U. S. 547</a></span> (1942); <em>Ashcraft </em>v. <em>Tennessee, </em><span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span> (1944); <em>Malinski </em>v. <em>New York, </em><span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span> (1945); <em>Leyra </em>v. <em>Denno, </em><span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556</a></span> (1954). See also <em>Williams </em>v. <em>United States, </em><span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/" aria-description="Citation for case: Williams v. United States">341 U. S. 97</a></span> (1951).</p>
</footnote>
<footnote label="7">
<p id="b544-12"> In addition, see <em>People </em>v. <em>Wakat, </em><span class="citation" data-id="2045374"><a href="/opinion/2045374/people-v-wakat/" aria-description="Citation for case: People v. Wakat">415 Ill. 610</a></span>, <span class="citation" data-id="2045374"><a href="/opinion/2045374/people-v-wakat/" aria-description="Citation for case: People v. Wakat">114 N. E. 2d 706</a></span> (1953); <em>Wa

[...TRUNCATED 44991 of 164991 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Missouri v. McNeely.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Missouri v. McNeely"
type: case
citation: ""
parallel_cite: "133 S. Ct. 1552; 185 L. Ed. 2d 696; 569 U.S. 141; 81 U.S.L.W. 4250; 24 Fla. L. Weekly Fed. S 150"
neutral_cite: "2013 U.S. LEXIS 3160; 2013 WL 1628934"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2013
date_decided: 2013-04-17
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2013-04-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Missouri v. McNeely
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/858288/missouri-v-mcneely/"
  cluster_id: 858288
  opinion_id: 858288
  identity_checked: true
homes:
  - page: "[[Destruction of Evidence]]"
    role: "Key — Progeny / Refinement"
  - page: "[[SIA Alcohol Tests]]"
    role: "Related (cross-doctrine)"
related: ["[[Schmerber v. California]]", "[[Mitchell v. Wisconsin]]", "[[Birchfield v. North Dakota]]"]
aliases: []
tags: ["case", "fourth-amendment", "exigent-circumstances", "blood-draw", "dui", "warrant"]
holding: "The natural metabolization of alcohol is NOT a per se exigency justifying a warrantless DUI blood draw in every case; exigency must be…"
lake:
  record_id: Missouri v. McNeely
  status: verified
  projected_at: 2026-07-06
---

# Missouri v. McNeely

*569 U.S. 141 (2013)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
McNeely was stopped for speeding, showed signs of intoxication, and refused a breath test. Without seeking a warrant, the officer took him to a hospital and directed a blood draw over his objection. Missouri defended the warrantless draw on the theory that the body's natural elimination of alcohol always creates an [[Exigent Circumstances and Hot Pursuit|exigency]].

## Issue
Whether the natural metabolization of alcohol in the bloodstream categorically creates an [[Exigent Circumstances and Hot Pursuit|exigency]] that justifies a warrantless blood draw in every drunk-driving case.

## Rule
No. "We hold that in drunk-driving investigations, the natural dissipation of alcohol in the bloodstream does not constitute an exigency in every case sufficient to justify conducting a blood test without a warrant." — 569 U.S. at 156. ^pin-156

Whether a warrantless blood draw is justified by [[Exigent Circumstances and Hot Pursuit|exigency]] must instead be determined case by case on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]].

## Application
Missouri relied solely on the [[Common Legal Terms#per-se|per se]] theory that dissipating alcohol always creates an [[Exigent Circumstances and Hot Pursuit|exigency]]; it did not show that obtaining a warrant in McNeely's case was impractical or that any other emergency was present. Because metabolization alone did not categorically justify the warrantless draw, and no case-specific [[Exigent Circumstances and Hot Pursuit|exigency]] was established, the blood draw was unreasonable.

## Conclusion
Affirmed; on these facts the warrantless blood draw was not justified by a [[Common Legal Terms#per-se|per se]] [[Exigent Circumstances and Hot Pursuit|exigency]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *McNeely* rejects a [[Common Legal Terms#per-se|per se]] [[Exigent Circumstances and Hot Pursuit|exigency]] rule and was later **refined by** [[Mitchell v. Wisconsin]], which addressed the distinct unconscious-driver scenario.

## Appears on
- [[Exigent Circumstances and Hot Pursuit]] — *Key — Progeny / Refinement*
- [[SIA Alcohol Tests]] — *Related (cross-doctrine)*

## Sources
- *Missouri v. McNeely*, 569 U.S. 141 (2013) — https://www.courtlistener.com/opinion/858288/missouri-v-mcneely/ — pinpoint: 156 (per the official U.S. Reports citation; CL carries the reporter text without inline star pagination).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "59388489bc2f6897", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Missouri v. McNeely"}, "payload": {"all": [{"cite": "133 S. Ct. 1552", "page": "1552", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "133"}, {"cite": "185 L. Ed. 2d 696", "page": "696", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "185"}, {"cite": "2013 U.S. LEXIS 3160", "page": "3160", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2013"}, {"cite": "569 U.S. 141", "page": "141", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "569"}, {"cite": "81 U.S.L.W. 4250", "page": "4250", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "81"}, {"cite": "24 Fla. L. Weekly Fed. S 150", "page": "150", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "24"}, {"cite": "2013 WL 1628934", "page": "1628934", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2013"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Missouri v. McNeely"}}
{"assertion_id": "92460c55b0b57168", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-156", "record_id": "Missouri v. McNeely"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-156", "pinpoint_status": "slip-only", "quote": "--- # Missouri v. McNeely *569 U.S. 141 (2013)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background McNeely was stopped for speeding, showed signs of intoxication, and refused a breath test. Without seeking a warrant, the officer took him to a hospital and directed a blood draw over his objection. Missouri defended the warrantless draw on the theory that the body's natural elimination of alcohol always creates an exigency. ## Issue Whether the natural metabolization of alcohol in the bloodstream categorically creates an exigency that justifies a warrantless blood draw in every drunk-driving case. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "Missouri v. McNeely", "star_marker": null}}
{"assertion_id": "f3f95c39e570438c", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Missouri v. McNeely"}, "payload": {"as_of_content": "2013-04-17", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Missouri v. McNeely", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Missouri v. McNeely

```json
{
  "schema_version": "s2.v1",
  "record_id": "Missouri v. McNeely",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Missouri v. McNeely",
    "case_name_short": "McNeely",
    "case_name_full": "MISSOURI, Petitioner v. Tyler G. McNEELY.",
    "input_case_name": "Missouri v. McNeely",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2013-04-17",
    "year": 2013,
    "docket": null,
    "cluster_id": 858288,
    "lead_opinion_id": 858288,
    "sibling_ids": [
      858288
    ],
    "absolute_url": "/opinion/858288/missouri-v-mcneely/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9239980,
        "score": 20,
        "case_name": "Missouri v. McNeely"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "133 S. Ct. 1552",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "1552",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "185 L. Ed. 2d 696",
        "volume": "185",
        "reporter": "L. Ed. 2d",
        "page": "696",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "569 U.S. 141",
        "volume": "569",
        "reporter": "U.S.",
        "page": "141",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 U.S.L.W. 4250",
        "volume": "81",
        "reporter": "U.S.L.W.",
        "page": "4250",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 150",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "150",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2013 U.S. LEXIS 3160",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "3160",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 WL 1628934",
        "volume": "2013",
        "reporter": "WL",
        "page": "1628934",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "133 S. Ct. 1552",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "1552",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "185 L. Ed. 2d 696",
        "volume": "185",
        "reporter": "L. Ed. 2d",
        "page": "696",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 U.S. LEXIS 3160",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "3160",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "569 U.S. 141",
        "volume": "569",
        "reporter": "U.S.",
        "page": "141",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 U.S.L.W. 4250",
        "volume": "81",
        "reporter": "U.S.L.W.",
        "page": "4250",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 150",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "150",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 WL 1628934",
        "volume": "2013",
        "reporter": "WL",
        "page": "1628934",
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
      "id": "pin-156",
      "page": null,
      "quote": "--- # Missouri v. McNeely *569 U.S. 141 (2013)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background McNeely was stopped for speeding, showed signs of intoxication, and refused a breath test. Without seeking a warrant, the officer took him to a hospital and directed a blood draw over his objection. Missouri defended the warrantless draw on the theory that the body's natural elimination of alcohol always creates an exigency. ## Issue Whether the natural metabolization of alcohol in the bloodstream categorically creates an exigency that justifies a warrantless blood draw in every drunk-driving case. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2013-04-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Missouri v. McNeely",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Missouri v. McNeely:lane1_negative"
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
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Colby Davis Laub",
          "cluster_id": 9493043,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Colby Davis Laub",
          "cluster_id": 9473742,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Portulano",
          "cluster_id": 10135231,
          "cite": [
            "320 Or. App. 335",
            "514 P.3d 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. McCarthy",
          "cluster_id": 10160868,
          "cite": [
            "369 Or. 129",
            "501 P.3d 478"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Bohigian",
          "cluster_id": 4806187,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jerel Chinedu Igboji v. State",
          "cluster_id": 4789820,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hedgpeth",
          "cluster_id": 10160693,
          "cite": [
            "365 Or. 724",
            "452 P.3d 948"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re B.B.",
          "cluster_id": 6243638,
          "cite": [
            "567 S.W.3d 786"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gonzalez v. City of Schenectady",
          "cluster_id": 1038554,
          "cite": [
            "728 F.3d 149",
            "2013 U.S. App. LEXIS 17943",
            "2013 WL 4528864"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. William L. Witt(074468)",
          "cluster_id": 2993869,
          "cite": [
            "223 N.J. 409",
            "126 A.3d 850",
            "2015 N.J. LEXIS 890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
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
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brokers' Choice of America, Inc. v. NBC Universal, Inc.",
          "cluster_id": 2682361,
          "cite": [
            "757 F.3d 1125",
            "2014 WL 3307834"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fitzgerald v. People",
          "cluster_id": 4385083,
          "cite": [
            "2017 CO 26",
            "394 P.3d 671",
            "2017 WL 1377349"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson, Ex Parte Ronald",
          "cluster_id": 2949202,
          "cite": [
            "442 S.W.3d 325",
            "2014 Tex. Crim. App. LEXIS 969",
            "2014 WL 4627231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Evans",
          "cluster_id": 4331789,
          "cite": [
            "153 A.3d 323",
            "2016 Pa. Super. 293",
            "2016 Pa. Super. LEXIS 778"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. McCumber",
          "cluster_id": 4370918,
          "cite": [
            "295 Neb. 941",
            "893 N.W.2d 411"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Caniglia v. Strom",
          "cluster_id": 4883694,
          "cite": [
            "593 U.S. 194",
            "209 L. Ed. 2d 604",
            "141 S. Ct. 1596"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Lemaricus Devall Davidson",
          "cluster_id": 4331383,
          "cite": [
            "509 S.W.3d 156",
            "2016 Tenn. LEXIS 913"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Williams v. Brian Maurer",
          "cluster_id": 4958226,
          "cite": [
            "9 F.4th 416"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. William Robert Bernard, Jr.",
          "cluster_id": 2778772,
          "cite": [
            "859 N.W.2d 762",
            "2015 Minn. LEXIS 46",
            "2015 WL 543160"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Michael R. Tullberg",
          "cluster_id": 2764887,
          "cite": [
            "359 Wis. 2d 421",
            "2014 WI 134",
            "857 N.W.2d 120",
            "2014 Wisc. LEXIS 951"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth, Aplt. v. Myers, D.",
          "cluster_id": 4410366,
          "cite": [
            "164 A.3d 1162",
            "2017 WL 3045867",
            "2017 Pa. LEXIS 1689"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wurie",
          "cluster_id": 870435,
          "cite": [
            "728 F.3d 1",
            "2013 U.S. App. LEXIS 9937",
            "2013 WL 2129119"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Corrin Kathleen Reynolds",
          "cluster_id": 4318256,
          "cite": [
            "504 S.W.3d 283",
            "2016 Tenn. LEXIS 821"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Martinez",
          "cluster_id": 6243814,
          "cite": [
            "570 S.W.3d 278"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Dean M. Blatterman",
          "cluster_id": 2798569,
          "cite": [
            "362 Wis. 2d 138",
            "2015 WI 46",
            "864 N.W.2d 26",
            "2015 Wisc. LEXIS 175"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Micah Abraham Wulff",
          "cluster_id": 3133317,
          "cite": [
            "157 Idaho 416",
            "337 P.3d 575",
            "2014 Ida. LEXIS 286"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mitchell v. Wisconsin",
          "cluster_id": 4633470,
          "cite": [
            "588 U.S. 840",
            "139 S. Ct. 2525",
            "2019 U.S. LEXIS 4400"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Christopher George Storm",
          "cluster_id": 4405282,
          "cite": [
            "898 N.W.2d 140",
            "2017 WL 2822483",
            "2017 Iowa Sup. LEXIS 81"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anne Marie Gennusa v. Brian Canova",
          "cluster_id": 2669144,
          "cite": [
            "748 F.3d 1103",
            "2014 WL 1363541"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Kenneth Ray Washington III",
          "cluster_id": 4472220,
          "cite": [
            "832 N.W.2d 650",
            "2013 WL 2450146",
            "2013 Iowa Sup. LEXIS 69"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(858288) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTI2NDI4ODAwMDAwJnM9NjIzOTYzMyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28858288%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 10,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 10,
        "triage_snippet_classified": 190
      },
      "lane2_top_cited": {
        "query": "cites:(858288)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NCZzPTkwMzQ4OSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28858288%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(858288)",
        "reviewed": 77,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 77,
        "triage_read": 4,
        "triage_snippet_classified": 73
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(858288)",
    "indexed_citing_opinions": 808,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 858288,
        "count": 808,
        "count_source": "search"
      }
    ],
    "citation_count": 1552,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/missouri-v-mcneely.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwODM5MzUmcz0xMDI3ODMzNCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28858288%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 858288,
        "cited_id": 1755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 108854,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 109504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 110832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 111380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 112475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 112608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 118103,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 118326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 118405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 145669,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 145814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 216733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 622303,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 1257859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 1869975,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 2009694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 2035860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 2219022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 2586146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 2620702,
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
    "date_created": "2026-07-05T14:13:34Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:13:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:13:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:17:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:13:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Missouri v. McNeely

```
(Slip Opinion)              OCTOBER TERM, 2012                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                        MISSOURI v. MCNEELY

       CERTIORARI TO THE SUPREME COURT OF MISSOURI

    No. 11–1425. Argued January 9, 2013—Decided April 17, 2013
Respondent McNeely was stopped by a Missouri police officer for speed-
  ing and crossing the centerline. After declining to take a breath test
  to measure his blood alcohol concentration (BAC), he was arrested
  and taken to a nearby hospital for blood testing. The officer never at-
  tempted to secure a search warrant. McNeely refused to consent to
  the blood test, but the officer directed a lab technician to take a sam-
  ple. McNeely’s BAC tested well above the legal limit, and he was
  charged with driving while intoxicated (DWI). He moved to suppress
  the blood test result, arguing that taking his blood without a warrant
  violated his Fourth Amendment rights. The trial court agreed, con-
  cluding that the exigency exception to the warrant requirement did
  not apply because, apart from the fact that McNeely’s blood alcohol
  was dissipating, no circumstances suggested that the officer faced an
  emergency.      The State Supreme Court affirmed, relying on
  Schmerber v. California, 384 U. S. 757, in which this Court upheld a
  DWI suspect’s warrantless blood test where the officer “might rea-
  sonably have believed that he was confronted with an emergency, in
  which the delay necessary to obtain a warrant, under the circum-
  stances, threatened ‘the destruction of evidence,’ ” id., at 770. This
  case, the state court found, involved a routine DWI investigation
  where no factors other than the natural dissipation of blood alcohol
  suggested that there was an emergency, and, thus, the nonconsensu-
  al warrantless test violated McNeely’s right to be free from unrea-
  sonable searches of his person.
Held: The judgment is affirmed.
358 S. W. 3d 65, affirmed.
     JUSTICE SOTOMAYOR delivered the opinion of the Court with respect
  to Parts I, II–A, II–B, and IV, concluding that in drunk-driving inves-
  tigations, the natural dissipation of alcohol in the bloodstream does
2                        MISSOURI v. MCNEELY

                                  Syllabus

    not constitute an exigency in every case sufficient to justify conduct-
    ing a blood test without a warrant. Pp. 4–13, 20–23.
       (a) The principle that a warrantless search of the person is reason-
    able only if it falls within a recognized exception, see, e.g., United
    States v. Robinson, 414 U. S. 218, 224, applies here, where the search
    involved a compelled physical intrusion beneath McNeely’s skin and
    into his veins to obtain a blood sample to use as evidence in a crimi-
    nal investigation. One recognized exception “applies when ‘ “the exi-
    gencies of the situation” make the needs of law enforcement so com-
    pelling that [a] warrantless search is objectively reasonable.’ ”
    Kentucky v. King, 563 U. S. ___, ___. This Court looks to the totality
    of circumstances in determining whether an exigency exits. See
    Brigham City v. Stuart, 547 U. S. 398, 406. Applying this approach
    in Schmerber, the Court found a warrantless blood test reasonable af-
    ter considering all of the facts and circumstances of that case and
    carefully basing its holding on those specific facts, including that al-
    cohol levels decline after drinking stops and that testing was delayed
    while officers transported the injured suspect to the hospital and in-
    vestigated the accident scene. Pp. 4–8.
       (b) The State nonetheless seeks a per se rule, contending that exi-
    gent circumstances necessarily exist when an officer has probable
    cause to believe a person has been driving under the influence of al-
    cohol because BAC evidence is inherently evanescent. Though a per-
    son’s blood alcohol level declines until the alcohol is eliminated, it
    does not follow that the Court should depart from careful case-by-
    case assessment of exigency. When officers in drunk-driving investi-
    gations can reasonably obtain a warrant before having a blood sam-
    ple drawn without significantly undermining the efficacy of the
    search, the Fourth Amendment mandates that they do so. See
    McDonald v. United States, 335 U. S. 451, 456. Circumstances may
    make obtaining a warrant impractical such that the alcohol’s dissipa-
    tion will support an exigency, but that is a reason to decide each case
    on its facts, as in Schmerber, not to accept the “considerable overgen-
    eralization” that a per se rule would reflect, Richards v. Wisconsin,
    520 U. S. 385, 393. Blood testing is different in critical respects from
    other destruction-of-evidence cases. Unlike a situation where, e.g., a
    suspect has control over easily disposable evidence, see Cupp v. Mur-
    phy, 412 U. S. 291, 296, BAC evidence naturally dissipates in a grad-
    ual and relatively predictable manner. Moreover, because an officer
    must typically take a DWI suspect to a medical facility and obtain a
    trained medical professional’s assistance before having a blood test
    conducted, some delay between the time of the arrest or accident and
    time of the test is inevitable regardless of whether a warrant is ob-
    tained. The State’s rule also fails to account for advances in the 47
                     Cite as: 569 U. S. ____ (2013)                      3

                                Syllabus

  years since Schmerber was decided that allow for the more expedi-
  tious processing of warrant applications, particularly in contexts like
  drunk-driving investigations where the evidence supporting probable
  cause is simple. The natural dissipation of alcohol in the blood may
  support an exigency finding in a specific case, as it did in Schmerber,
  but it does not do so categorically. Pp. 8–13.
     (c) Because the State sought a per se rule here, it did not argue that
  there were exigent circumstances in this particular case. The argu-
  ments and the record thus do not provide the Court with an adequate
  framework for a detailed discussion of all the relevant factors that
  can be taken into account in determining the reasonableness of act-
  ing without a warrant. It suffices to say that the metabolization of
  alcohol in the bloodstream and the ensuing loss of evidence are
  among the factors that must be considered in deciding whether a
  warrant is required. Pp. 20–23.
     JUSTICE SOTOMAYOR, joined by JUSTICE SCALIA, JUSTICE GINSBURG,
  and JUSTICE KAGAN, concluded in Part III that other arguments ad-
  vanced by the State and amici in support of a per se rule are unper-
  suasive. Their concern that a case-by-case approach to exigency will
  not provide adequate guidance to law enforcement officers may make
  the desire for a bright-line rule understandable, but the Fourth
  Amendment will not tolerate adoption of an overly broad categorical
  approach in this context. A fact-intensive, totality of the circum-
  stances, approach is hardly unique within this Court’s Fourth
  Amendment jurisprudence. See, e.g., Illinois v. Wardlow, 528 U. S.
  119, 123–125. They also contend that the privacy interest implicated
  here is minimal. But motorists’ diminished expectation of privacy
  does not diminish their privacy interest in preventing a government
  agent from piercing their skin. And though a blood test conducted in
  a medical setting by trained personnel is less intrusive than other
  bodily invasions, this Court has never retreated from its recognition
  that any compelled intrusion into the human body implicates signifi-
  cant, constitutionally protected privacy interests. Finally, the gov-
  ernment’s general interest in combating drunk driving does not justi-
  fy departing from the warrant requirement without showing exigent
  circumstances that make securing a warrant impractical in a particu-
  lar case. Pp. 15–20.

  SOTOMAYOR, J., announced the judgment of the Court and delivered
the opinion of the Court with respect to Parts I, II–A, II–B, and IV, in
which SCALIA, KENNEDY, GINSBURG, and KAGAN, JJ., joined, and an
opinion with respect to Parts II–C and III, in which SCALIA, GINSBURG,
and KAGAN, JJ., joined. KENNEDY, J., filed an opinion concurring in
part. ROBERTS, C. J., filed an opinion concurring in part and dissenting
4                    MISSOURI v. MCNEELY

                             Syllabus

in part, in which BREYER and ALITO, JJ., joined. THOMAS, J., filed a
dissenting opinion.
                       Cite as: 569 U. S. ____ (2013)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash­
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 11–1425
                                  _________________


   MISSOURI, PETITIONER v. TYLER G. MCNEELY
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                                                 

                      MISSOURI


                                [April 17, 2013] 


  JUSTICE SOTOMAYOR announced the judgment of the
Court and delivered the opinion of the Court with respect
to Parts I, II–A, II–B, and IV, and an opinion with respect
to Parts II–C and III, in which JUSTICE SCALIA, JUSTICE
GINSBURG, and JUSTICE KAGAN join.
  In Schmerber v. California, 384 U. S. 757 (1966), this
Court upheld a warrantless blood test of an individual
arrested for driving under the influence of alcohol because
the officer “might reasonably have believed that he was
confronted with an emergency, in which the delay neces­
sary to obtain a warrant, under the circumstances, threat­
ened the destruction of evidence.” Id., at 770 (internal
quotation marks omitted). The question presented here
is whether the natural metabolization of alcohol in the
bloodstream presents a per se exigency that justifies an
exception to the Fourth Amendment’s warrant require­
ment for nonconsensual blood testing in all drunk-driving
cases. We conclude that it does not, and we hold, con­
sistent with general Fourth Amendment principles, that
exigency in this context must be determined case by case
based on the totality of the circumstances.
2                          MISSOURI v. MCNEELY

                             Opinion of the Court

                               I
   While on highway patrol at approximately 2:08 a.m., a
Missouri police officer stopped Tyler McNeely’s truck after
observing it exceed the posted speed limit and repeatedly
cross the centerline. The officer noticed several signs
that McNeely was intoxicated, including McNeely’s blood­
shot eyes, his slurred speech, and the smell of alcohol on his
breath. McNeely acknowledged to the officer that he had
consumed “a couple of beers” at a bar, App. 20, and he
appeared unsteady on his feet when he exited the truck.
After McNeely performed poorly on a battery of field­
sobriety tests and declined to use a portable breath-test
device to measure his blood alcohol concentration (BAC),
the officer placed him under arrest.
   The officer began to transport McNeely to the station
house. But when McNeely indicated that he would again
refuse to provide a breath sample, the officer changed
course and took McNeely to a nearby hospital for blood
testing. The officer did not attempt to secure a warrant.
Upon arrival at the hospital, the officer asked McNeely
whether he would consent to a blood test. Reading from
a standard implied consent form, the officer explained to
McNeely that under state law refusal to submit voluntar-
ily to the test would lead to the immediate revocation of his
driver’s license for one year and could be used against him
in a future prosecution. See Mo. Ann. Stat. §§577.020.1,
577.041 (West 2011). McNeely nonetheless refused. The
officer then directed a hospital lab technician to take a
blood sample, and the sample was secured at approxi­
mately 2:35 a.m. Subsequent laboratory testing measured
McNeely’s BAC at 0.154 percent, which was well above the
legal limit of 0.08 percent. See §577.012.1.
   McNeely was charged with driving while intoxicated
(DWI), in violation of §577.010.1 He moved to suppress
——————
    1 As   a result of his two prior drunk-driving convictions, McNeely was
                   Cite as: 569 U. S. ____ (2013)               3

                       Opinion of the Court

the results of the blood test, arguing in relevant part that,
under the circumstances, taking his blood for chemi­
cal testing without first obtaining a search warrant vio-
lated his rights under the Fourth Amendment. The trial
court agreed. It concluded that the exigency exception to
the warrant requirement did not apply because, apart from
the fact that “[a]s in all cases involving intoxication,
[McNeely’s] blood alcohol was being metabolized by his
liver,” there were no circumstances suggesting the officer
faced an emergency in which he could not practicably
obtain a warrant. No. 10CG–CR01849–01 (Cir. Ct. Cape
Giradeau Cty., Mo., Div. II, Mar. 3, 2011), App. to Pet.
for Cert. 43a. On appeal, the Missouri Court of Appeals
stated an intention to reverse but transferred the case
directly to the Missouri Supreme Court. No. ED 96402
(June 21, 2011), id., at 24a.
   The Missouri Supreme Court affirmed. 358 S. W. 3d 65
(2012) (per curiam). Recognizing that this Court’s decision
in Schmerber v. California, 384 U. S. 757, “provide[d] the
backdrop” to its analysis, the Missouri Supreme Court
held that “Schmerber directs lower courts to engage in
a totality of the circumstances analysis when determin­
ing whether exigency permits a nonconsensual, warrantless
blood draw.” 358 S. W. 3d, at 69, 74. The court further
concluded that Schmerber “requires more than the mere
dissipation of blood-alcohol evidence to support a warrant­
less blood draw in an alcohol-related case.” 358 S. W. 3d,
at 70. According to the court, exigency depends heavily on
the existence of additional “ ‘special facts,’ ” such as whether
an officer was delayed by the need to investigate an ac-
cident and transport an injured suspect to the hospital,
as had been the case in Schmerber. 358 S. W. 3d, at 70,
—————— 

charged with a class D felony under Missouri law, which carries a 

maximum imprisonment term of four years. See Mo. Ann. Stat.
     

§§558.011, 577.023.1(5), 577.023.3 (West 2011).

                                               

4                      MISSOURI v. MCNEELY

                          Opinion of the Court

74. Finding that this was “unquestionably a routine DWI
case” in which no factors other than the natural dissi­
pation of blood-alcohol suggested that there was an emer­
gency, the court held that the nonconsensual warrantless
blood draw violated McNeely’s Fourth Amendment right
to be free from unreasonable searches of his person. Id.,
at 74–75.
  We granted certiorari to resolve a split of authority on
the question whether the natural dissipation of alcohol in
the bloodstream establishes a per se exigency that suffices
on its own to justify an exception to the warrant require­
ment for nonconsensual blood testing in drunk-driving
investigations.2 See 567 U. S. ___ (2012). We now affirm.
                             II

                               

                             A

   The Fourth Amendment provides in relevant part that
“[t]he right of the people to be secure in their persons,
houses, papers, and effects, against unreasonable searches
and seizures, shall not be violated, and no Warrants shall
issue, but upon probable cause.” Our cases have held that
a warrantless search of the person is reasonable only if
it falls within a recognized exception. See, e.g., United
States v. Robinson, 414 U. S. 218, 224 (1973). That prin­
ciple applies to the type of search at issue in this case,
which involved a compelled physical intrusion beneath
McNeely’s skin and into his veins to obtain a sample of his
blood for use as evidence in a criminal investigation. Such
an invasion of bodily integrity implicates an individual’s
——————
  2 Compare 358 S. W. 3d 65 (2012) (case below), State v. Johnson, 744

N. W. 2d 340 (Iowa 2008) (same conclusion), and State v. Rodriguez,
2007 UT 15, 156 P. 3d 771 (same), with State v. Shriner, 751 N. W. 2d
538 (Minn. 2008) (holding that the natural dissipation of blood-alcohol
evidence alone constitutes a per se exigency), State v. Bohling, 173 Wis.
2d 529, 494 N. W. 2d 399 (1993) (same); State v. Woolery, 116 Idaho
368, 775 P. 2d 1210 (1989) (same).
                 Cite as: 569 U. S. ____ (2013)            5

                     Opinion of the Court

“most personal and deep-rooted expectations of privacy.”
Winston v. Lee, 470 U. S. 753, 760 (1985); see also Skinner
v. Railway Labor Executives’ Assn., 489 U. S. 602, 616
(1989).
   We first considered the Fourth Amendment restrictions
on such searches in Schmerber, where, as in this case, a
blood sample was drawn from a defendant suspected of
driving while under the influence of alcohol. 384 U. S., at
758. Noting that “[s]earch warrants are ordinarily re­
quired for searches of dwellings,” we reasoned that “absent
an emergency, no less could be required where intrusions
into the human body are concerned,” even when the search
was conducted following a lawful arrest. Id., at 770. We
explained that the importance of requiring authorization
by a “ ‘neutral and detached magistrate’ ” before allowing a
law enforcement officer to “invade another’s body in search
of evidence of guilt is indisputable and great.” Ibid. (quot­
ing Johnson v. United States, 333 U. S. 10, 13–14 (1948)).
   As noted, the warrant requirement is subject to ex­
ceptions. “One well-recognized exception,” and the one
at issue in this case, “applies when the exigencies of the
situation make the needs of law enforcement so compelling
that a warrantless search is objectively reasonable under
the Fourth Amendment.” Kentucky v. King, 563 U. S. ___,
___ (2011) (slip op., at 6) (internal quotation marks and
brackets omitted). A variety of circumstances may give
rise to an exigency sufficient to justify a warrantless
search, including law enforcement’s need to provide emer­
gency assistance to an occupant of a home, Michigan v.
Fisher, 558 U. S. 45, 47–48 (2009) (per curiam), engage in
“hot pursuit” of a fleeing suspect, United States v. San­
tana, 427 U. S. 38, 42–43 (1976), or enter a burning building
to put out a fire and investigate its cause, Michigan v.
Tyler, 436 U. S. 499, 509–510 (1978). As is relevant here,
we have also recognized that in some circumstances law
enforcement officers may conduct a search without a
6                  MISSOURI v. MCNEELY

                      Opinion of the Court

warrant to prevent the imminent destruction of evidence.
See Cupp v. Murphy, 412 U. S. 291, 296 (1973); Ker v.
California, 374 U. S. 23, 40–41 (1963) (plurality opinion).
While these contexts do not necessarily involve equiva-
lent dangers, in each a warrantless search is potentially
reasonable because “there is compelling need for official
action and no time to secure a warrant.” Tyler, 436 U. S.,
at 509.
   To determine whether a law enforcement officer faced
an emergency that justified acting without a warrant, this
Court looks to the totality of circumstances. See Brigham
City v. Stuart, 547 U. S. 398, 406 (2006) (finding officers’
entry into a home to provide emergency assistance “plain­
ly reasonable under the circumstances”); Illinois v. Mc-
Arthur, 531 U. S. 326, 331 (2001) (concluding that a war­
rantless seizure of a person to prevent him from returning
to his trailer to destroy hidden contraband was reasonable
“[i]n the circumstances of the case before us” due to exi­
gency); Cupp, 412 U. S., at 296 (holding that a limited
warrantless search of a suspect’s fingernails to preserve
evidence that the suspect was trying to rub off was justi­
fied “[o]n the facts of this case”); see also Richards v.
Wisconsin, 520 U. S. 385, 391–396 (1997) (rejecting a
per se exception to the knock-and-announce requirement
for felony drug investigations based on presumed exigen­
cy, and requiring instead evaluation of police conduct “in
a particular case”). We apply this “finely tuned approach”
to Fourth Amendment reasonableness in this context be-
cause the police action at issue lacks “the traditional
justification that . . . a warrant . . . provides.” Atwater v.
Lago Vista, 532 U. S. 318, 347, n. 16 (2001). Absent that
established justification, “the fact-specific nature of the
reasonableness inquiry,” Ohio v. Robinette, 519 U. S. 33,
39 (1996), demands that we evaluate each case of alleged
exigency based “on its own facts and circumstances.” Go-
Bart Importing Co. v. United States, 282 U. S. 344, 357
                    Cite as: 569 U. S. ____ (2013)                   7

                         Opinion of the Court

(1931).3
   Our decision in Schmerber applied this totality of the
circumstances approach. In that case, the petitioner had
suffered injuries in an automobile accident and was taken
to the hospital. 384 U. S., at 758. While he was there
receiving treatment, a police officer arrested the petitioner
for driving while under the influence of alcohol and or­
dered a blood test over his objection. Id., at 758–759.
After explaining that the warrant requirement applied
generally to searches that intrude into the human body,
we concluded that the warrantless blood test “in the pre­
sent case” was nonetheless permissible because the officer
“might reasonably have believed that he was confronted
with an emergency, in which the delay necessary to obtain
a warrant, under the circumstances, threatened ‘the de­
struction of evidence.’ ” Id., at 770 (quoting Preston v.
United States, 376 U. S. 364, 367 (1964)).
   In support of that conclusion, we observed that evidence
could have been lost because “the percentage of alcohol in
the blood begins to diminish shortly after drinking stops,
as the body functions to eliminate it from the system.”
384 U. S., at 770. We added that “[p]articularly in a case
such as this, where time had to be taken to bring the
accused to a hospital and to investigate the scene of the
accident, there was no time to seek out a magistrate and
secure a warrant.” Id., at 770–771. “Given these special
facts,” we found that it was appropriate for the police to
——————
  3 We have recognized a limited class of traditional exceptions to the

warrant requirement that apply categorically and thus do not require
an assessment of whether the policy justifications underlying the ex-
ception, which may include exigency-based considerations, are im­
plicated in a particular case. See, e.g., California v. Acevedo, 500
U. S. 565, 569–570 (1991) (automobile exception); United States v.
Robinson, 414 U. S. 218, 224–235 (1973) (searches of a person incident
to a lawful arrest). By contrast, the general exigency exception, which
asks whether an emergency existed that justified a warrantless search,
naturally calls for a case-specific inquiry.
8                  MISSOURI v. MCNEELY

                     Opinion of the Court

act without a warrant. Id., at 771. We further held that
the blood test at issue was a reasonable way to recover the
evidence because it was highly effective, “involve[d] vir­
tually no risk, trauma, or pain,” and was conducted in a
reasonable fashion “by a physician in a hospital environ­
ment according to accepted medical practices.” Ibid. And
in conclusion, we noted that our judgment that there had
been no Fourth Amendment violation was strictly based
“on the facts of the present record.” Id., at 772.
   Thus, our analysis in Schmerber fits comfortably within
our case law applying the exigent circumstances excep­
tion. In finding the warrantless blood test reasonable in
Schmerber, we considered all of the facts and circumstances
of the particular case and carefully based our holding on
those specific facts.
                             B
  The State properly recognizes that the reasonableness
of a warrantless search under the exigency exception to
the warrant requirement must be evaluated based on the
totality of the circumstances. Brief for Petitioner 28–29.
But the State nevertheless seeks a per se rule for blood
testing in drunk-driving cases. The State contends that
whenever an officer has probable cause to believe an
individual has been driving under the influence of alcohol,
exigent circumstances will necessarily exist because BAC
evidence is inherently evanescent. As a result, the State
claims that so long as the officer has probable cause and
the blood test is conducted in a reasonable manner, it is
categorically reasonable for law enforcement to obtain the
blood sample without a warrant.
  It is true that as a result of the human body’s natural
metabolic processes, the alcohol level in a person’s blood
begins to dissipate once the alcohol is fully absorbed and
continues to decline until the alcohol is eliminated. See
Skinner, 489 U. S., at 623; Schmerber, 384 U. S., at 770–
                 Cite as: 569 U. S. ____ (2013)            9

                     Opinion of the Court

771. Testimony before the trial court in this case indicated
that the percentage of alcohol in an individual’s blood
typically decreases by approximately 0.015 percent to 0.02
percent per hour once the alcohol has been fully absorbed.
App. 47. More precise calculations of the rate at which
alcohol dissipates depend on various individual character­
istics (such as weight, gender, and alcohol tolerance) and
the circumstances in which the alcohol was consumed.
See Stripp, Forensic and Clinical Issues in Alcohol Analy­
sis, in Forensic Chemistry Handbook 437–441 (L. Kobilin­
sky ed. 2012). Regardless of the exact elimination rate, it
is sufficient for our purposes to note that because an indi­
vidual’s alcohol level gradually declines soon after he stops
drinking, a significant delay in testing will negatively
affect the probative value of the results. This fact was
essential to our holding in Schmerber, as we recognized
that, under the circumstances, further delay in order to
secure a warrant after the time spent investigating the
scene of the accident and transporting the injured suspect
to the hospital to receive treatment would have threatened
the destruction of evidence. 384 U. S., at 770–771.
   But it does not follow that we should depart from careful
case-by-case assessment of exigency and adopt the cate­
gorical rule proposed by the State and its amici. In those
drunk-driving investigations where police officers can
reasonably obtain a warrant before a blood sample can be
drawn without significantly undermining the efficacy of
the search, the Fourth Amendment mandates that they
do so. See McDonald v. United States, 335 U. S. 451, 456
(1948) (“We cannot . . . excuse the absence of a search
warrant without a showing by those who seek exemption
from the constitutional mandate that the exigencies of the
situation made [the search] imperative”). We do not doubt
that some circumstances will make obtaining a warrant
impractical such that the dissipation of alcohol from the
bloodstream will support an exigency justifying a properly
10                 MISSOURI v. MCNEELY

                     Opinion of the Court

conducted warrantless blood test. That, however, is a
reason to decide each case on its facts, as we did in
Schmerber, not to accept the “considerable overgeneraliza­
tion” that a per se rule would reflect. Richards, 520 U. S.,
at 393.
   The context of blood testing is different in critical re­
spects from other destruction-of-evidence cases in which
the police are truly confronted with a “ ‘now or never’ ”
situation. Roaden v. Kentucky, 413 U. S. 496, 505 (1973).
In contrast to, for example, circumstances in which the
suspect has control over easily disposable evidence, see
Georgia v. Randolph, 547 U. S. 103, 116, n. 6 (2006);
Cupp, 412 U. S., at 296, BAC evidence from a drunk­
driving suspect naturally dissipates over time in a gradual
and relatively predictable manner. Moreover, because a
police officer must typically transport a drunk-driving
suspect to a medical facility and obtain the assistance of
someone with appropriate medical training before con­
ducting a blood test, some delay between the time of the
arrest or accident and the time of the test is inevitable
regardless of whether police officers are required to obtain
a warrant. See State v. Shriner, 751 N. W. 2d 538, 554
(Minn. 2008) (Meyer, J., dissenting). This reality under­
mines the force of the State’s contention, endorsed by the
dissent, see post, at 3 (opinion of THOMAS, J.), that we
should recognize a categorical exception to the warrant
requirement because BAC evidence “is actively being
destroyed with every minute that passes.” Brief for Peti­
tioner 27. Consider, for example, a situation in which the
warrant process will not significantly increase the delay
before the blood test is conducted because an officer can
take steps to secure a warrant while the suspect is being
transported to a medical facility by another officer. In
such a circumstance, there would be no plausible justifica­
tion for an exception to the warrant requirement.
   The State’s proposed per se rule also fails to account for
                     Cite as: 569 U. S. ____ (2013)                   11

                          Opinion of the Court

advances in the 47 years since Schmerber was decided
that allow for the more expeditious processing of warrant
applications, particularly in contexts like drunk-driving
investigations where the evidence offered to establish
probable cause is simple. The Federal Rules of Criminal
Procedure were amended in 1977 to permit federal magis­
trate judges to issue a warrant based on sworn testimony
communicated by telephone. See 91 Stat. 319. As amended,
the law now allows a federal magistrate judge to con-
sider “information communicated by telephone or other
reliable electronic means.” Fed. Rule Crim. Proc. 4.1.
States have also innovated. Well over a majority of States
allow police officers or prosecutors to apply for search
warrants remotely through various means, including
telephonic or radio communication, electronic communica­
tion such as e-mail, and video conferencing.4 And in addi­
——————
  4 See Ala. Rule Crim. Proc. 3.8(b) (2012–2013); Alaska Stat.

§12.35.015 (2012); Ariz. Rev. Stat. Ann. §§13–3914(C), 13–3915(D), (E)
(West 2010); Ark. Code Ann. §16–82–201 (2005); Cal. Penal Code Ann.
§1526(b) (West 2011); Colo. Rule Crim. Proc. 41(c)(3) (2012); Ga. Code
Ann. §17–5–21.1 (2008); Haw. Rules Penal Proc. 41(h)–(i) (2013); Idaho
Code §§19–4404, 19–4406 (Lexis 2004); Ind. Code §35–33–5–8 (2012);
Iowa Code §§321J.10(3), 462A.14D(3) (2009) (limited to specific circum­
stances involving accidents); Kan. Stat. Ann. §§22–2502(a), 22–2504
(2011 Cum. Supp.); La. Code Crim. Proc. Ann., Arts. 162.1(B), (D) (West
2003); Mich. Comp. Laws Ann. §§780.651(2)–(6) (West 2006); Minn.
Rules Crim. Proc. 33.05, 36.01–36.08 (2010 and Supp. 2013); Mont.
Code Ann. §§46–5–221, 46–5–222 (2012); Neb. Rev. Stat. §§29–814.01,
29–814.03, 29–814.05 (2008); Nev. Rev. Stat. §§179.045(2), (4) (2011);
N. H. Rev. Stat. Ann. §595–A:4–a (Lexis Supp. 2012); N. J. Rule Crim.
Proc. 3:5–3(b) (2013); N. M. Rules Crim. Proc. 5–211(F)(3), (G)(3) (Supp.
2012); N. Y. Crim. Proc. Law Ann. §§690.35(1), 690.36(1), 690.40(3),
690.45(1), (2) (West 2009); N. C. Gen. Stat. Ann. §15A–245(a)(3) (Lexis
2011); N. D. Rules Crim. Proc. 41(c)(2)–(3) (2012–2013); Ohio Rules
Crim. Proc. 41(C)(1)–(2) (2011); Okla. Stat. Ann., Tit. 22, §§1223.1,
1225(B) (West 2011); Ore. Rev. Stat. §§133.545(5)–(6) (2011); Pa. Rules
Crim. Proc. 203(A), (C) (2012); S. D. Codified Laws §§23A–35–4.2, 23A–
35–5, 23A–35–6 (2004); Utah Rule Crim. Proc. 40(l) (2012); Vt. Rules
Crim. Proc. 41(c)(4), (g)(2) (Supp. 2012); Va. Code Ann. §19.2–54 (Lexis
12                     MISSOURI v. MCNEELY

                         Opinion of the Court

tion to technology-based developments, jurisdictions have
found other ways to streamline the warrant process, such
as by using standard-form warrant applications for drunk­
driving investigations.5
   We by no means claim that telecommunications inno­
vations have, will, or should eliminate all delay from the
warrant-application process. Warrants inevitably take
some time for police officers or prosecutors to complete and
for magistrate judges to review. Telephonic and electronic
warrants may still require officers to follow time­
consuming formalities designed to create an adequate
record, such as preparing a duplicate warrant before
calling the magistrate judge. See Fed. Rule Crim. Proc.
4.1(b)(3). And improvements in communications technolo­
gy do not guarantee that a magistrate judge will be avail­
able when an officer needs a warrant after making a late­
night arrest. But technological developments that enable
police officers to secure warrants more quickly, and do so
without undermining the neutral magistrate judge’s es­
sential role as a check on police discretion, are relevant to
an assessment of exigency. That is particularly so in this
context, where BAC evidence is lost gradually and

—————— 

Supp. 2012); Wash. Super. Ct. Crim. Rule 2.3(c) (2002); Wis. Stat. 

§968.12(3) (2007–2008); Wyo. Stat. Ann. §31–6–102(d) (2011); see 

generally 2 W. LaFave, Search and Seizure §4.3(b), pp. 511–516, and
     

n. 29 (4th ed. 2004) (describing oral search warrants and collecting
state laws). Missouri requires that search warrants be in writing and
does not permit oral testimony, thus excluding telephonic warrants. Mo.
Ann. Stat. §§542.276.2(1), 542.276.3 (West Supp. 2012). State law does
permit the submission of warrant applications “by facsimile or other
electronic means.” §542.276.3.
  5 During the suppression hearing in this case, McNeely entered into

evidence a search-warrant form used in drunk-driving cases by the
prosecutor’s office in Cape Girardeau County, where the arrest took
place. App. 61–69. The arresting officer acknowledged that he had
used such forms in the past and that they were “readily available.” Id.,
at 41–42.
                     Cite as: 569 U. S. ____ (2013)                   13

                         Opinion of the Court
                       Opinion of SOTOMAYOR, J.

relatively predictably.6
  Of course, there are important countervailing concerns.
While experts can work backwards from the BAC at the
time the sample was taken to determine the BAC at the
time of the alleged offense, longer intervals may raise
questions about the accuracy of the calculation. For that
reason, exigent circumstances justifying a warrantless
blood sample may arise in the regular course of law en­
forcement due to delays from the warrant application
process. But adopting the State’s per se approach would
improperly ignore the current and future technological
developments in warrant procedures, and might well
diminish the incentive for jurisdictions “to pursue progres­
sive approaches to warrant acquisition that preserve the
protections afforded by the warrant while meeting the
legitimate interests of law enforcement.” State v. Rodri-
guez, 2007 UT 15, ¶46, 156 P. 3d 771, 779.
   In short, while the natural dissipation of alcohol in the
blood may support a finding of exigency in a specific case,
as it did in Schmerber, it does not do so categorically.
Whether a warrantless blood test of a drunk-driving sus­
pect is reasonable must be determined case by case based
on the totality of the circumstances.
                            C
  In an opinion concurring in part and dissenting in part,
THE CHIEF JUSTICE agrees that the State’s proposed per se
rule is overbroad because “[f]or exigent circumstances to
——————
  6 The dissent claims that a “50-state survey [is] irrelevant to the ac­

tual disposition of this case” because Missouri requires written warrant
applications. Post, at 8. But the per se exigency rule that the State
seeks and the dissent embraces would apply nationally because it
treats “the body’s natural metabolization of alcohol” as a sufficient
basis for a warrantless search everywhere and always. Post, at 1. The
technological innovations in warrant procedures that many States
have adopted are accordingly relevant to show that the per se rule is
overbroad.
14                  MISSOURI v. MCNEELY

                      Opinion of the Court
                    Opinion of SOTOMAYOR, J.

justify a warrantless search . . . there must . . . be ‘no time
to secure a warrant.’ ” Post, at 6 (quoting Tyler, 436 U. S.,
at 509). But THE CHIEF JUSTICE then goes on to suggest
his own categorical rule under which a warrantless blood
draw is permissible if the officer could not secure a war­
rant (or reasonably believed he could not secure a war­
rant) in the time it takes to transport the suspect to a
hospital or similar facility and obtain medical assistance.
Post, at 8–9. Although we agree that delay inherent to the
blood-testing process is relevant to evaluating exigency,
see supra, at 10, we decline to substitute THE CHIEF
JUSTICE’s modified per se rule for our traditional totality of
the circumstances analysis.
   For one thing, making exigency completely dependent
on the window of time between an arrest and a blood test
produces odd consequences. Under THE CHIEF JUSTICE’s
rule, if a police officer serendipitously stops a suspect near
an emergency room, the officer may conduct a noncon-
sensual warrantless blood draw even if all agree that a
warrant could be obtained with very little delay under the
circumstances (perhaps with far less delay than an aver­
age ride to the hospital in the jurisdiction). The rule
would also distort law enforcement incentives. As with
the State’s per se rule, THE CHIEF JUSTICE’s rule might
discourage efforts to expedite the warrant process because
it categorically authorizes warrantless blood draws so long
as it takes more time to secure a warrant than to obtain
medical assistance. On the flip side, making the require­
ment of independent judicial oversight turn exclusively on
the amount of time that elapses between an arrest and
BAC testing could induce police departments and individ­
ual officers to minimize testing delay to the detriment of
other values. THE CHIEF JUSTICE correctly observes that
“[t]his case involves medical personnel drawing blood at a
medical facility, not police officers doing so by the side of
the road.” Post, at 6–7, n. 2. But THE CHIEF JUSTICE does
                  Cite as: 569 U. S. ____ (2013)           15

                      Opinion of the Court
                    Opinion of SOTOMAYOR, J.

not say that roadside blood draws are necessarily un-
reasonable, and if we accepted THE CHIEF JUSTICE’s ap­
proach, they would become a more attractive option for the
police.
                              III
   The remaining arguments advanced in support of a
per se exigency rule are unpersuasive.
   The State and several of its amici, including the United
States, express concern that a case-by-case approach to
exigency will not provide adequate guidance to law en­
forcement officers deciding whether to conduct a blood test
of a drunk-driving suspect without a warrant. THE CHIEF
JUSTICE and the dissent also raise this concern. See post,
at 1, 9–10 (opinion of ROBERTS, C. J.); post, at 5–7 (opinion
of THOMAS, J.). While the desire for a bright-line rule is
understandable, the Fourth Amendment will not tolerate
adoption of an overly broad categorical approach that
would dilute the warrant requirement in a context where
significant privacy interests are at stake. Moreover, a
case-by-case approach is hardly unique within our Fourth
Amendment jurisprudence. Numerous police actions
are judged based on fact-intensive, totality of the circum­
stances analyses rather than according to categorical
rules, including in situations that are more likely to require
police officers to make difficult split-second judgments.
See, e.g., Illinois v. Wardlow, 528 U. S. 119, 123–125
(2000) (whether an officer has reasonable suspicion to
make an investigative stop and to pat down a suspect for
weapons under Terry v. Ohio, 392 U. S. 1 (1968)); Robi-
nette, 519 U. S., at 39–40 (whether valid consent has been
given to search); Tennessee v. Garner, 471 U. S. 1, 8–9, 20
(1985) (whether force used to effectuate a seizure, includ­
ing deadly force, is reasonable). As in those contexts, we
see no valid substitute for careful case-by-case evaluation
16                      MISSOURI v. MCNEELY

                          Opinion of the Court
                        Opinion of SOTOMAYOR, J.

of reasonableness here.7
   Next, the State and the United States contend that the
privacy interest implicated by blood draws of drunk­
driving suspects is relatively minimal. That is so, they
claim, both because motorists have a diminished expecta­
tion of privacy and because our cases have repeatedly
indicated that blood testing is commonplace in society and
typically involves “virtually no risk, trauma, or pain.”
Schmerber, 384 U. S., at 771. See also post, at 3, and n. 1
(opinion of THOMAS, J.).
   But the fact that people are “accorded less privacy in . . .
automobiles because of th[e] compelling governmental
need for regulation,” California v. Carney, 471 U. S. 386,
392 (1985), does not diminish a motorist’s privacy interest
in preventing an agent of the government from piercing
his skin. As to the nature of a blood test conducted in a
medical setting by trained personnel, it is concededly less
intrusive than other bodily invasions we have found un­
reasonable. See Winston, 470 U. S., at 759–766 (surgery
to remove a bullet); Rochin v. California, 342 U. S. 165,
172–174 (1952) (induced vomiting to extract narcotics
capsules ingested by a suspect violated the Due Process
Clause). For that reason, we have held that medically
drawn blood tests are reasonable in appropriate circum­
stances. See Skinner, 489 U. S., at 618–633 (upholding
——————
  7 The dissent contends that officers in the field will be unable to apply

the traditional totality of the circumstances test in this context because
they will not know all of the relevant facts at the time of an arrest.
See post, at 6. But because “[t]he police are presumably familiar with
the mechanics and time involved in the warrant process in their partic­
ular jurisdiction,” post, at 8 (opinion of ROBERTS, C. J.), we expect that
officers can make reasonable judgments about whether the warrant
process would produce unacceptable delay under the circumstances.
Reviewing courts in turn should assess those judgments “ ‘from the
perspective of a reasonable officer on the scene, rather than with the
20/20 vision of hindsight.’ ” Ryburn v. Huff, 565 U. S. ___, ___ (2012)
(per curiam) (slip op., at 8).
                     Cite as: 569 U. S. ____ (2013)                    17

                         Opinion of the Court
                       Opinion of SOTOMAYOR, J.

warrantless blood testing of railroad employees involved
in certain train accidents under the “special needs” doc­
trine); Schmerber, 384 U. S., at 770–772. We have never
retreated, however, from our recognition that any com­
pelled intrusion into the human body implicates signifi­
cant, constitutionally protected privacy interests.
   Finally, the State and its amici point to the compelling
governmental interest in combating drunk driving and
contend that prompt BAC testing, including through blood
testing, is vital to pursuit of that interest. They argue
that is particularly so because, in addition to laws that
make it illegal to operate a motor vehicle under the influ­
ence of alcohol, all 50 States and the District of Columbia
have enacted laws that make it per se unlawful to operate
a motor vehicle with a BAC of over 0.08 percent. See
National Highway Traffic Safety Admin. (NHTSA), Al­
cohol and Highway Safety: A Review of the State of
Knowledge 167 (No. 811374, Mar. 2011) (NHTSA Re­
view).8 To enforce these provisions, they reasonably as­
sert, accurate BAC evidence is critical. See also post, at
4–5 (opinion of ROBERTS, C. J.); post, at 4–5 (opinion of
THOMAS, J.).
   “No one can seriously dispute the magnitude of the
drunken driving problem or the States’ interest in eradi­
cating it.” Michigan Dept. of State Police v. Sitz, 496 U. S.
444, 451 (1990). Certainly we do not. While some pro­
gress has been made, drunk driving continues to exact a

——————
  8 Pursuant to congressional directive, the NHTSA conditions federal

highway grants on States’ adoption of laws making it a per se offense to
operate a motor vehicle with a BAC of 0.08 percent or greater. See 23
U. S. C. §163(a); 23 CFR §1225.1 (2012). Several federal prohibitions
on drunk driving also rely on the 0.08 percent standard. E.g., 32 CFR
§§234.17(c)(1)(ii), 1903.4(b)(1)(i)–(ii); 36 CFR §4.23(a)(2). In addition,
32 States and the District of Columbia have adopted laws that impose
heightened penalties for operating a motor vehicle at or above a BAC of
0.15 percent. See NHTSA Review 175.
18                 MISSOURI v. MCNEELY

                     Opinion of the Court
                   Opinion of SOTOMAYOR, J.

terrible toll on our society. See NHTSA, Traffic Safety
Facts, 2011 Data 1 (No. 811700, Dec. 2012) (reporting that
9,878 people were killed in alcohol-impaired driving
crashes in 2011, an average of one fatality every 53
minutes).
  But the general importance of the government’s interest
in this area does not justify departing from the warrant
requirement without showing exigent circumstances that
make securing a warrant impractical in a particular case.
To the extent that the State and its amici contend that
applying the traditional Fourth Amendment totality-of­
the-circumstances analysis to determine whether an exi­
gency justified a warrantless search will undermine the
governmental interest in preventing and prosecuting
drunk-driving offenses, we are not convinced.
  As an initial matter, States have a broad range of legal
tools to enforce their drunk-driving laws and to secure
BAC evidence without undertaking warrantless noncon­
sensual blood draws. For example, all 50 States have
adopted implied consent laws that require motorists, as a
condition of operating a motor vehicle within the State, to
consent to BAC testing if they are arrested or otherwise
detained on suspicion of a drunk-driving offense. See
NHTSA Review 173; supra, at 2 (describing Missouri’s
implied consent law). Such laws impose significant conse­
quences when a motorist withdraws consent; typically the
motorist’s driver’s license is immediately suspended or
revoked, and most States allow the motorist’s refusal to
take a BAC test to be used as evidence against him in a
subsequent criminal prosecution. See NHTSA Review
173–175; see also South Dakota v. Neville, 459 U. S. 553,
554, 563–564 (1983) (holding that the use of such an ad­
verse inference does not violate the Fifth Amendment
right against self-incrimination).
  It is also notable that a majority of States either place
significant restrictions on when police officers may obtain
                     Cite as: 569 U. S. ____ (2013)                  19

                         Opinion of the Court
                       Opinion of SOTOMAYOR, J.

a blood sample despite a suspect’s refusal (often limiting
testing to cases involving an accident resulting in death or
serious bodily injury) or prohibit nonconsensual blood
tests altogether.9 Among these States, several lift re­
strictions on nonconsensual blood testing if law enforce­
ment officers first obtain a search warrant or similar court
order.10 Cf. Bullcoming v. New Mexico, 564 U. S. ___, ___
——————
  9 See Ala. Code §32–5–192(c) (2010); Alaska Stat. §§28.35.032(a),

28.35.035(a) (2012); Ariz. Rev. Stat. Ann. §28–1321(D)(1) (West 2012);
Ark. Code Ann. §§5–65–205(a)(1), 5–65–208(a)(1) (Supp. 2011);
Conn. Gen. Stat. §§14–227b(b), 14–227c(b) (2011); Fla. Stat. Ann.
§316.1933(1)(a) (West 2006); Ga. Code Ann. §§40–5–67.1(d), (d.1)
(2011); Haw. Rev. Stat. §291E–15 (2009 Cum. Supp.), §§291E–21(a),
291E–33 (2007), §291E–65 (2009 Cum. Supp.); Iowa Code §§321J.9(1),
321J.10(1), 321J.10A(1) (2009); Kan. Stat. Ann. §§8–1001(b), (d) (2001);
Ky. Rev. Stat. Ann. §189A.105(2) (Lexis Supp. 2012); La. Rev. Stat.
Ann. §§32:666.A(1)(a)(i), (2) (Supp. 2013); Md. Transp. Code Ann. §§16–
205.1(b)(i)(1), (c)(1) (Lexis 2012); Mass. Gen. Laws Ann., ch. 90,
§§24(1)(e), (f)(1) (West 2012); Mich. Comp. Laws Ann. §257.625d(1)
(West 2006); Miss. Code Ann. §63–11–21 (1973–2004); Mont. Code Ann.
§§61–8–402(4), (5) (2011); Neb. Rev. Stat. §60–498.01(2) (2012
Cum. Supp.), §60–6,210 (2010); N. H. Rev. Stat. Ann. §§265–A:14(I),
265–A:16 (West 2012 Cum. Supp.); N. M. Stat. Ann. §66–8–111(A)
(LexisNexis 2009); N. Y. Veh. & Traf. Law Ann. §§1194(2)(b)(1), 1194(3)
(West 2011); N. D. Cent. Code Ann. §39–20–01.1(1) (Lexis Supp. 2011),
§39–20–04(1) (Lexis 2008); Okla. Stat., Tit. 47, §753 (West Supp. 2013);
Ore. Rev. Stat. §813.100(2) (2011); 75 Pa. Cons. Stat. §1547(b)(1)
(2004); R. I. Gen. Laws §§31–27–2.1(b), 31–27–2.9(a) (Lexis 2010); S. C.
Code Ann. §56–5–2950(B) (Supp. 2011); Tenn. Code Ann. §§55–10–
406(a)(4), (f) (2012); Tex. Transp. Code Ann. §§724.012(b), 724.013
(West 2011); Vt. Stat. Ann., Tit. 23, §§1202(b), (f) (2007); Wash. Rev.
Code §§46.20.308 (2)–(3), (5) (2012); W. Va. Code Ann. §17C–5–7 (Lexis
Supp. 2012); Wyo. Stat. Ann. §31–6–102(d) (Lexis 2011).
  10 See Ariz. Rev. Stat. Ann. §28–1321(D)(1) (West 2012); Ga. Code

Ann. §§40–5–67.1(d), (d.1) (2011); Ky. Rev. Stat. Ann. §189A.105(2)(b)
(Lexis Supp. 2012); Mich. Comp. Laws Ann. §257.625d(1) (West 2006);
Mont. Code Ann. §61–8–402(5) (2011); N. M. Stat. Ann. §66–8–111(A)
(LexisNexis 2009); N. Y. Veh. & Traf. Law Ann. §§1194(2)(b)(1), 1194(3)
(West 2011); Ore. Rev. Stat. 813.320(2)(b) (2011); R. I. Gen. Laws §31–
27–2.9(a) (Lexis 2010); Tenn. Code Ann. §55–10–406(a)(4) (2012); Vt.
Stat. Ann., Tit. 23, §1202(f) (2007); Wash. Rev. Code §46.20.308(1)
20                    MISSOURI v. MCNEELY

                         Opinion of the Court

(2011) (slip op., at 3) (noting that the blood test was ob­
tained pursuant to a warrant after the petitioner refused a
breath test). We are aware of no evidence indicating that
restrictions on nonconsensual blood testing have compro­
mised drunk-driving enforcement efforts in the States that
have them. And in fact, field studies in States that permit
nonconsensual blood testing pursuant to a warrant have
suggested that, although warrants do impose administra­
tive burdens, their use can reduce breath-test-refusal
rates and improve law enforcement’s ability to recover
BAC evidence. See NHTSA, Use of Warrants for Breath
Test Refusal: Case Studies 36–38 (No. 810852, Oct. 2007).
   To be sure, “States [may] choos[e] to protect privacy
beyond the level that the Fourth Amendment requires.”
Virginia v. Moore, 553 U. S. 164, 171 (2008). But wide­
spread state restrictions on nonconsensual blood testing
provide further support for our recognition that compelled
blood draws implicate a significant privacy interest. They
also strongly suggest that our ruling today will not “se­
verely hamper effective law enforcement.” Garner, 471
U. S., at 19.
                            IV
  The State argued before this Court that the fact that
alcohol is naturally metabolized by the human body cre­
ates an exigent circumstance in every case. The State did
not argue that there were exigent circumstances in this
particular case because a warrant could not have been
obtained within a reasonable amount of time. In his
testimony before the trial court, the arresting officer did
—————— 

(2012); W. Va. Code Ann. §17C–5–7 (Supp. 2012) (as interpreted in
     

State v. Stone, 229 W. Va. 271, ___, 728 S. E. 2d 155, 167–168 (2012)); 

Wyo. Stat. Ann. §31–6–102(d) (2011); see also State v. Harris, 763 

N. W. 2d 269, 273–274 (Iowa 2009) (per curiam) (recognizing that Iowa
law imposes a warrant requirement subject to a limited case-specific
exigency exception).
                     Cite as: 569 U. S. ____ (2013)                  21

                         Opinion of the Court

not identify any other factors that would suggest he faced
an emergency or unusual delay in securing a warrant.
App. 40. He testified that he made no effort to obtain
a search warrant before conducting the blood draw even
though he was “sure” a prosecuting attorney was on call
and even though he had no reason to believe that a magis­
trate judge would have been unavailable. Id., at 39, 41–
42. The officer also acknowledged that he had obtained
search warrants before taking blood samples in the past
without difficulty. Id., at 42. He explained that he elected
to forgo a warrant application in this case only because he
believed it was not legally necessary to obtain a warrant.
Id., at 39–40. Based on this testimony, the trial court
concluded that there was no exigency and specifically
found that, although the arrest took place in the middle of
the night, “a prosecutor was readily available to apply for
a search warrant and a judge was readily available to
issue a warrant.” App. to Pet. for Cert. 43a.11
   The Missouri Supreme Court in turn affirmed that
judgment, holding first that the dissipation of alcohol did
not establish a per se exigency, and second that the State
could not otherwise satisfy its burden of establishing
exigent circumstances. 358 S. W. 3d, at 70, 74–75. In
petitioning for certiorari to this Court, the State chal­
lenged only the first holding; it did not separately contend
that the warrantless blood test was reasonable regardless
of whether the natural dissipation of alcohol in a suspect’s
blood categorically justifies dispensing with the warrant
——————
  11 No findings were made by the trial court concerning how long a
warrant would likely have taken to issue under the circumstances. The
minimal evidence presented on this point was not uniform. A second
patrol officer testified that in a typical DWI case, it takes between 90
minutes and 2 hours to obtain a search warrant following an arrest.
App. 53–54. McNeely, however, also introduced an exhibit document­
ing six recent search warrant applications for blood testing in Cape
Girardeau County that had shorter processing times. Id., at 70.
22                  MISSOURI v. MCNEELY

                      Opinion of the Court

requirement. See Pet. for Cert. i.
   Here and in its own courts the State based its case on
an insistence that a driver who declines to submit to test­
ing after being arrested for driving under the influence of
alcohol is always subject to a nonconsensual blood test
without any precondition for a warrant. That is incorrect.
   Although the Missouri Supreme Court referred to this
case as “unquestionably a routine DWI case,” 358 S. W.
3d, at 74, the fact that a particular drunk-driving stop is
“routine” in the sense that it does not involve “ ‘special
facts,’ ” ibid., such as the need for the police to attend to a
car accident, does not mean a warrant is required. Other
factors present in an ordinary traffic stop, such as the
procedures in place for obtaining a warrant or the avail­
ability of a magistrate judge, may affect whether the police
can obtain a warrant in an expeditious way and therefore
may establish an exigency that permits a warrantless
search. The relevant factors in determining whether a
warrantless search is reasonable, including the practical
problems of obtaining a warrant within a timeframe that
still preserves the opportunity to obtain reliable evidence,
will no doubt vary depending upon the circumstances in
the case.
   Because this case was argued on the broad proposition
that drunk-driving cases present a per se exigency, the
arguments and the record do not provide the Court with
an adequate analytic framework for a detailed discussion
of all the relevant factors that can be taken into account in
determining the reasonableness of acting without a war­
rant. It suffices to say that the metabolization of alcohol
in the bloodstream and the ensuing loss of evidence are
among the factors that must be considered in deciding
whether a warrant is required. No doubt, given the large
number of arrests for this offense in different jurisdictions
nationwide, cases will arise when anticipated delays in
obtaining a warrant will justify a blood test without judi­
                 Cite as: 569 U. S. ____ (2013)           23

                     Opinion of the Court

cial authorization, for in every case the law must be con­
cerned that evidence is being destroyed. But that inquiry
ought not to be pursued here where the question is not
properly before this Court. Having rejected the sole ar­
gument presented to us challenging the Missouri Supreme
Court’s decision, we affirm its judgment.
                        *     *     *
  We hold that in drunk-driving investigations, the natu­
ral dissipation of alcohol in the bloodstream does not con-
stitute an exigency in every case sufficient to justify
conducting a blood test without a warrant.
  The judgment of the Missouri Supreme Court is
affirmed.
                                            It is so ordered.
                  Cite as: 569 U. S. ____ (2013)            1

                 KENNEDY, J., concurring in part

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 11–1425
                          _________________


   MISSOURI, PETITIONER v. TYLER G. MCNEELY
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF 

                      MISSOURI

                         [April 17, 2013] 


   JUSTICE KENNEDY, concurring in part.
   I join Parts I, II–A, II–B, and IV of the opinion for the
Court.
   For the reasons stated below this case does not call for
the Court to consider in detail the issue discussed in Part
II–C and the separate opinion by THE CHIEF JUSTICE.
   As to Part III, much that is noted with respect to the
statistical and survey data will be of relevance when this
issue is explored in later cases. The repeated insistence in
Part III that every case be determined by its own circum-
stances is correct, of course, as a general proposition; yet
it ought not to be interpreted to indicate this question is
not susceptible of rules and guidelines that can give im-
portant, practical instruction to arresting officers, in-
struction that in any number of instances would allow a
warrantless blood test in order to preserve the critical
evidence.
   States and other governmental entities which enforce
the driving laws can adopt rules, procedures, and protocols
that meet the reasonableness requirements of the Fourth
Amendment and give helpful guidance to law enforcement
officials. And this Court, in due course, may find it appro-
priate and necessary to consider a case permitting it to
provide more guidance than it undertakes to give today.
   As the opinion of the Court is correct to note, the instant
case, by reason of the way in which it was presented and
2                  MISSOURI v. MCNEELY

                KENNEDY, J., concurring in part

decided in the state courts, does not provide a framework
where it is prudent to hold any more than that always
dispensing with a warrant for a blood test when a driver is
arrested for being under the influence of alcohol is incon-
sistent with the Fourth Amendment.
                 Cite as: 569 U. S. ____ (2013)           1

                   Opinion of ROBERTS, C. J.

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 11–1425
                         _________________


   MISSOURI, PETITIONER v. TYLER G. MCNEELY
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF 

                      MISSOURI


                        [April 17, 2013] 


   CHIEF JUSTICE ROBERTS, with whom JUSTICE BREYER
and JUSTICE ALITO join, concurring in part and dissenting
in part.
   A police officer reading this Court’s opinion would have
no idea—no idea—what the Fourth Amendment requires
of him, once he decides to obtain a blood sample from a
drunk driving suspect who has refused a breathalyzer
test. I have no quarrel with the Court’s “totality of the
circumstances” approach as a general matter; that is what
our cases require. But the circumstances in drunk driving
cases are often typical, and the Court should be able to
offer guidance on how police should handle cases like the
one before us.
   In my view, the proper rule is straightforward. Our
cases establish that there is an exigent circumstances
exception to the warrant requirement. That exception
applies when there is a compelling need to prevent the
imminent destruction of important evidence, and there is
no time to obtain a warrant. The natural dissipation of
alcohol in the bloodstream constitutes not only the immi-
nent but ongoing destruction of critical evidence. That
would qualify as an exigent circumstance, except that
there may be time to secure a warrant before blood can be
drawn. If there is, an officer must seek a warrant. If an
officer could reasonably conclude that there is not, the
exigent circumstances exception applies by its terms, and
2                  MISSOURI v. MCNEELY

                    Opinion of ROBERTS, C. J.

the blood may be drawn without a warrant.
                           I
    The Fourth Amendment provides:
     “The right of the people to be secure in their persons,
     houses, papers, and effects, against unreasonable
     searches and seizures, shall not be violated, and no
     Warrants shall issue, but upon probable cause, sup-
     ported by Oath or affirmation, and particularly de-
     scribing the place to be searched, and the persons or
     things to be seized.”
That language does not state that warrants are required
prior to searches, but this Court has long held that war-
rants must generally be obtained. See Kentucky v. King,
563 U. S. ___, ___ (2011) (slip op., at 5). We have also held
that bodily intrusions like blood draws constitute searches
and are subject to the warrant requirement.               See
Schmerber v. California, 384 U. S. 757, 767, 770 (1966).
   However, “the ultimate touchstone of the Fourth
Amendment is ‘reasonableness,’ ” Brigham City v. Stuart,
547 U. S. 398, 403 (2006), and thus “the warrant require-
ment is subject to certain reasonable exceptions,” King,
563 U. S., at ___ (slip op., at 6). One of those exceptions is
known as the “exigent circumstances exception,” which
“applies when the exigencies of the situation make the
needs of law enforcement so compelling that a warrantless
search is objectively reasonable under the Fourth
Amendment.” Ibid. (internal quotation marks and altera-
tions omitted).
   Within the exigent circumstances exception, we have
identified several sets of exigent circumstances excusing
the need for a warrant. For example, there is an emergency
aid exception to the warrant requirement. In Brigham
City, supra, at 403, we held that “law enforcement officers
may enter a home without a warrant to render emergency
                 Cite as: 569 U. S. ____ (2013)           3

                   Opinion of ROBERTS, C. J.

assistance to an injured occupant or to protect an occupant
from imminent injury.” There is also a fire exception to
the warrant requirement. In Michigan v. Tyler, 436 U. S.
499, 509 (1978), we held that “[a] burning building clearly
presents an exigency of sufficient proportions to render
a warrantless entry ‘reasonable.’ ” And there is a hot pur-
suit exception to the warrant requirement as well. In
United States v. Santana, 427 U. S. 38 (1976), and War-
den, Md. Penitentiary v. Hayden, 387 U. S. 294 (1967), we
recognized “the right of police, who had probable cause to
believe that an armed robber had entered a house a few
minutes before, to make a warrantless entry to arrest the
robber and to search for weapons.” Santana, supra, at 42.
In each of these cases, the requirement that we base our
decision on the “totality of the circumstances” has not
prevented us from spelling out a general rule for the police
to follow.
  The exigency exception most on point here is the one for
imminent destruction of evidence. We have affirmed on
several occasions that “law enforcement officers may make
a warrantless entry onto private property . . . to prevent
the imminent destruction of evidence.” Brigham City,
supra, at 403 (citing Ker v. California, 374 U. S. 23, 40
(1963) (plurality opinion)); see also, e.g., King, supra, at
___ (slip op., at 6). For example, in Ker, the police had
reason to believe that the defendant was in possession of
marijuana and was expecting police pursuit. We upheld
the officers’ warrantless entry into the defendant’s home,
with the plurality explaining that the drugs “could be
quickly and easily destroyed” or “distributed or hidden
before a warrant could be obtained at that time of night.”
374 U. S., at 40, 42.
  As an overarching principle, we have held that if there
is a “compelling need for official action and no time to
secure a warrant,” the warrant requirement may be ex-
4                  MISSOURI v. MCNEELY

                    Opinion of ROBERTS, C. J.

cused. Tyler, supra, at 509. The question here is whether
and how this principle applies in the typical case of a
police officer stopping a driver on suspicion of drunk
driving.
                                II

                                  

                                A

   The reasonable belief that critical evidence is being
destroyed gives rise to a compelling need for blood draws
in cases like this one. Here, in fact, there is not simply
a belief that any alcohol in the bloodstream will be de-
stroyed; it is a biological certainty. Alcohol dissipates from
the bloodstream at a rate of 0.01 percent to 0.025 percent
per hour. Stripp, Forensic and Clinical Issues in Alcohol
Analysis, in Forensic Chemistry Handbook 440 (L. Kobil-
insky ed. 2012). Evidence is literally disappearing by the
minute. That certainty makes this case an even stronger
one than usual for application of the exigent circumstances
exception.
   And that evidence is important. A serious and deadly
crime is at issue. According to the Department of Trans-
portation, in 2011, one person died every 53 minutes due
to drinking and driving. National Highway Traffic Safety
Admin. (NHTSA), Traffic Safety Facts, 2011 Data 1 (No.
811700, Dec. 2012). No surprise then that drinking and
driving is punished severely, including with jail time. See
generally Dept. of Justice, Bureau of Justice Statistics, L.
Maruschak, Special Report, DWI Offenders under Correc-
tional Supervision (1999). McNeely, for instance, faces up
to four years in prison. See App. 22–23 (citing Mo. Ann.
Stat. §§558.011, 577.010, 577.023 (West 2011)).
   Evidence of a driver’s blood alcohol concentration (BAC)
is crucial to obtain convictions for such crimes. All 50
States and the District of Columbia have laws providing
that it is per se illegal to drive with a BAC of 0.08 percent
or higher. Most States also have laws establishing addi-
                 Cite as: 569 U. S. ____ (2013)           5

                   Opinion of ROBERTS, C. J.

tional penalties for drivers who drive with a “high BAC,”
often defined as 0.15 percent or above. NHTSA, Digest
of Impaired Driving and Selected Beverage Control Laws,
pp. vii, x–xviii (No. 811673, Oct. 2012). BAC evidence
clearly matters. And when drivers refuse breathalyzers,
as McNeely did here, a blood draw becomes necessary to
obtain that evidence.
   The need to prevent the imminent destruction of BAC
evidence is no less compelling because the incriminating
alcohol dissipates over a limited period of time, rather
than all at once. As noted, the concentration of alcohol
 can make a difference not only between guilt and inno-
cence, but between different crimes and different degrees
of punishment. The officer is unlikely to know precisely
when the suspect consumed alcohol or how much; all he
knows is that critical evidence is being steadily lost. Fire
can spread gradually, but that does not lessen the need
and right of the officers to respond immediately. See
Tyler, supra.
   McNeely contends that there is no compelling need for a
warrantless blood draw, because if there is some alcohol
left in the blood by the time a warrant is obtained, the
State can use math and science to work backwards and
identify a defendant’s BAC at the time he was driving.
See Brief for Respondent 44–46. But that’s not good
enough. We have indicated that exigent circumstances
justify warrantless entry when drugs are about to be
flushed down the toilet. See, e.g., King, 563 U. S., at ___–
___ (slip op., at 7–8). We have not said that, because there
could well be drug paraphernalia elsewhere in the home,
or because a defendant’s co-conspirator might testify to
the amount of drugs involved, the drugs themselves are
not crucial and there is no compelling need for warrantless
entry.
   The same approach should govern here. There is a
6                       MISSOURI v. MCNEELY

                        Opinion of ROBERTS, C. J.

compelling need to search because alcohol—the nearly
conclusive evidence of a serious crime—is dissipating from
the bloodstream. The need is no less compelling because
the police might be able to acquire second-best evidence
some other way.1
                             B
  For exigent circumstances to justify a warrantless
search, however, there must also be “no time to secure a
warrant.” Tyler, 436 U. S., at 509; see Schmerber, 384
U. S., at 771 (warrantless search legal when “there was no
time to seek out a magistrate and secure a warrant”). In
this respect, obtaining a blood sample from a suspected
drunk driver differs from other exigent circumstances
cases.
  Importantly, there is typically delay between the mo-
ment a drunk driver is stopped and the time his blood can
be drawn. Drunk drivers often end up in an emergency
room, but they are not usually pulled over in front of one.
In most exigent circumstances situations, police are just
outside the door to a home. Inside, evidence is about to be
destroyed, a person is about to be injured, or a fire has
broken out. Police can enter promptly and must do so to
respond effectively to the emergency. But when police pull
a person over on suspicion of drinking and driving, they
cannot test his blood right away.2 There is a time-
——————
    1 Andthat second-best evidence may prove useless. When experts
have worked backwards to identify a defendant’s BAC at the time he
was driving, defense attorneys have objected to that evidence, courts
have at times rejected it, and juries may be suspicious of it. See, e.g., 1
D. Nichols & F. Whited, Drinking/Driving Litigation §2:9, pp. 2–130 to
2–137 (2d ed. 2006) (noting counsel objections to such evidence); State
v. Eighth Judicial District Court, 127 Nev. ___, 267 P. 3d 777 (2011)
(affirming rejection of such evidence); L. Taylor & S. Oberman, Drunk
Driving Defense §6.03 (7th ed. 2010) (describing ways to undermine
such evidence before a jury).
  2 This case involves medical personnel drawing blood at a medical
                     Cite as: 569 U. S. ____ (2013)                   7

                       Opinion of ROBERTS, C. J.

consuming obstacle to their search, in the form of a trip
to the hospital and perhaps a wait to see a medical pro-
fessional. In this case, for example, approximately 25
minutes elapsed between the time the police stopped
McNeely and the time his blood was drawn. App. 36, 38.
  As noted, the fact that alcohol dissipates gradually from
the bloodstream does not diminish the compelling need for
a search—critical evidence is still disappearing. But the
fact that the dissipation persists for some time means that
the police—although they may not be able to do anything
about it right away—may still be able to respond to the
ongoing destruction of evidence later on.
  There might, therefore, be time to obtain a warrant in
many cases. As the Court explains, police can often re-
quest warrants rather quickly these days. At least 30
States provide for electronic warrant applications. See
ante, at 10–12, and n. 4. In many States, a police officer
can call a judge, convey the necessary information, and be
authorized to affix the judge’s signature to a warrant.
See, e.g., Ala. Rule Crim. Proc. 3.8(b) (2012–2013); Alaska
Stat. §12.35.015 (2012); Idaho Code §§19–4404, 19–4406
(Lexis 2004); Minn. Rules Crim. Proc. 36.01–36.08 (2010
and Supp. 2013); Mont. Code Ann. §46–5–222 (2012); see
——————
facility, not police officers doing so by the side of the road. See
Schmerber v. California, 384 U. S. 757, 771–772 (1966) (“Petitioner’s
blood was taken by a physician in a hospital environment according to
accepted medical practices. We are thus not presented with the serious
questions which would arise if a search involving use of a medical
technique, even of the most rudimentary sort, were made by other than
medical personnel or in other than a medical environment—for exam-
ple, if it were administered by police in the privacy of the station-
house”); Brief for Respondent 53, and n. 21 (describing roadside blood
draws in Arizona). A plurality of the Court suggests that my approach
could make roadside blood draws a more attractive option for police,
but such a procedure would pose practical difficulties and, as the Court
noted in Schmerber, would raise additional and serious Fourth
Amendment concerns. See ante, at 14–15.
8                  MISSOURI v. MCNEELY

                   Opinion of ROBERTS, C. J.

generally NHTSA, Use of Warrants for Breath Test Re-
fusal: Case Studies 6–32 (No. 810852, Oct. 2007) (overview
of procedures in Arizona, Michigan, Oregon, and Utah).
Utah has an e-warrant procedure where a police officer
enters information into a system, the system notifies
a prosecutor, and upon approval the officer forwards
the information to a magistrate, who can electronically re-
turn a warrant to the officer. Utah, e-Warrants: Cross
Boundary Collaboration 1 (2008). Judges have been known
to issue warrants in as little as five minutes. Bergreen,
Faster Warrant System Hailed, Salt Lake Tribune, Dec.
26, 2008, p. B1, col. 1. And in one county in Kansas, police
officers can e-mail warrant requests to judges’ iPads;
judges have signed such warrants and e-mailed them back
to officers in less than 15 minutes. Benefiel, DUI Search
Warrants: Prosecuting DUI Refusals, 9 Kansas Prosecutor
17, 18 (Spring 2012). The police are presumably familiar
with the mechanics and time involved in the warrant
process in their particular jurisdiction.
                              III

                                 

                               A

  In a case such as this, applying the exigent circum-
stances exception to the general warrant requirement of
the Fourth Amendment seems straightforward: If there is
time to secure a warrant before blood can be drawn, the
police must seek one. If an officer could reasonably con-
clude that there is not sufficient time to seek and receive a
warrant, or he applies for one but does not receive a re-
sponse before blood can be drawn, a warrantless blood
draw may ensue. See Tyler, supra, at 509; see also Illinois
v. Rodriguez, 497 U. S. 177, 185–186 (1990) (“in order to
satisfy the ‘reasonableness’ requirement of the Fourth
Amendment, what is generally demanded of the many
factual determinations that must regularly be made by . . .
police officer[s] conducting a search or seizure under one of
                 Cite as: 569 U. S. ____ (2013)            9

                   Opinion of ROBERTS, C. J.

the exceptions to the warrant requirement . . . is not that
they always be correct, but that they always be reasona-
ble”); Terry v. Ohio, 392 U. S. 1, 20 (1968) (“police must,
whenever practicable, obtain advance judicial approval of
searches and seizures through the warrant procedure”).
   Requiring police to apply for a warrant if practicable
increases the likelihood that a neutral, detached judicial
officer will review the case, helping to ensure that there is
probable cause for any search and that any search is
reasonable. We have already held that forced blood draws
can be constitutional—that such searches can be reasonable—
but that does not change the fact that they are significant
bodily intrusions. See Schmerber, 384 U. S., at 770 (up-
holding a warrantless forced blood draw but noting the
“importance of informed, detached and deliberate deter-
minations of the issue whether or not to invade another’s
body in search of evidence of guilt” as “indisputable and
great”). Requiring a warrant whenever practicable helps
ensure that when blood draws occur, they are indeed
justified.
   At the same time, permitting the police to act without a
warrant to prevent the imminent destruction of evidence
is well established in Fourth Amendment law. There is no
reason to preclude application of that exception in drunk
driving cases simply because it may take the police some
time to be able to respond to the undoubted destruction of
evidence, or because the destruction occurs continuously
over an uncertain period.
   And that is so even in situations where police have
requested a warrant but do not receive a timely response.
An officer who reasonably concluded there was no time to
secure a warrant may have blood drawn from a suspect
upon arrival at a medical facility. There is no reason an
officer should be in a worse position, simply because he
sought a warrant prior to his arrival at the hospital.
10                 MISSOURI v. MCNEELY

                   Opinion of ROBERTS, C. J.

                             B
   The Court resists the foregoing, contending that the
question presented somehow inhibits such a focused anal-
ysis in this case. See ante, at 20–23. It does not. The
question presented is whether a warrantless blood draw is
permissible under the Fourth Amendment “based upon
the natural dissipation of alcohol in the bloodstream.”
Pet. for Cert. i. The majority answers “It depends,” and
so do I. The difference is that the majority offers no ad-
ditional guidance, merely instructing courts and police
officers to consider the totality of the circumstances. I
believe more meaningful guidance can be provided about
how to handle the typical cases, and nothing about the
question presented prohibits affording that guidance.
   A plurality of the Court also expresses concern that my
approach will discourage state and local efforts to expedite
the warrant application process. See ante, at 14. That is
not plausible: Police and prosecutors need warrants in a
wide variety of situations, and often need them quickly.
They certainly would not prefer a slower process, just
because that might obviate the need to ask for a warrant
in the occasional drunk driving case in which a blood draw
is necessary. The plurality’s suggestion also overlooks the
interest of law enforcement in the protection a warrant
provides.
   The Court is correct when it says that every case must
be considered on its particular facts. But the pertinent
facts in drunk driving cases are often the same, and the
police should know how to act in recurring factual situa-
tions. Simply put, when a drunk driving suspect fails field
sobriety tests and refuses a breathalyzer, whether a war-
rant is required for a blood draw should come down to
whether there is time to secure one.
   Schmerber itself provides support for such an analysis.
The Court there made much of the fact that “there was no
                 Cite as: 569 U. S. ____ (2013)         11

                   Opinion of ROBERTS, C. J.

time to seek out a magistrate and secure a warrant.” 384
U. S., at 771. It did so in an era when cell phones and
e-mail were unknown. It follows quite naturally that if
cell phones and e-mail mean that there is time to contact
a magistrate and secure a warrant, that must be done. At
the same time, there is no need to jettison the well-
established exception for the imminent destruction of
evidence, when the officers are in a position to do some-
thing about it.
                        *    *    *
  Because the Missouri courts did not apply the rule I
describe above, and because this Court should not do so in
the first instance, I would vacate and remand for further
proceedings in the Missouri courts.
                 Cite as: 569 U. S. ____ (2013)            1

                    THOMAS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 11–1425
                         _________________


   MISSOURI, PETITIONER v. TYLER G. MCNEELY
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF 

                      MISSOURI


                        [April 17, 2013] 


  JUSTICE THOMAS, dissenting.
  This case requires the Court to decide whether the
Fourth Amendment prohibits an officer from obtaining a
blood sample without a warrant when there is probable
cause to believe that a suspect has been driving under the
influence of alcohol. Because the body’s natural meta­
bolization of alcohol inevitably destroys evidence of the
crime, it constitutes an exigent circumstance. As a result, I
would hold that a warrantless blood draw does not violate
the Fourth Amendment.
                             I

                             A

  The Fourth Amendment states that “[t]he right of the
people to be secure in their persons . . . against unreason­
able searches and seizures, shall not be violated, and no
Warrants shall issue, but upon probable cause.” Before a
search occurs, “a warrant must generally be secured,”
Kentucky v. King, 563 U. S. ___, ___ (2011) (slip op., at 5),
but “this presumption may be overcome in some circum­
stances because ‘[t]he ultimate touchstone of the Fourth
Amendment is “reasonableness.” ’ ” Ibid. (quoting Brig­
ham City v. Stuart, 547 U. S. 398, 403 (2006); alteration
in original).
  The presence of “exigent circumstances” is one such
exception to the warrant requirement. Exigency applies
2                  MISSOURI v. MCNEELY

                     THOMAS, J., dissenting

when “ ‘the needs of law enforcement [are] so compelling
that [a] warrantless search is objectively reasonable under
the Fourth Amendment.’ ” 563 U. S., at ___ (slip op., at 6)
(quoting Mincey v. Arizona, 437 U. S. 385, 394 (1978);
second alteration in original). Thus, when exigent circum­
stances are present, officers may take actions that would
typically require a warrant, such as entering a home in
hot pursuit of a fleeing suspect. 563 U. S., at ___ (slip op.,
at 6). As relevant in this case, officers may also conduct
a warrantless search when they have probable cause to
believe that failure to act would result in “ ‘imminent
destruction of evidence.’ ” Ibid. (quoting Brigham City,
supra, at 403).
                              B
   Once police arrest a suspect for drunk driving, each
passing minute eliminates probative evidence of the crime.
The human liver eliminates alcohol from the bloodstream
at a rate of approximately 0.015 percent to 0.020 percent
per hour, ante, at 8, with some heavy drinkers as high as
0.022 percent per hour, Brief for Petitioner 21 (citing
medical studies), depending on, among other things, a per-
son’s sex, weight, body type, and drinking history. Ante,
at 8–9; Brief for United States as Amicus Curiae 23.
The Court has acknowledged this fact since Schmerber v.
California, 384 U. S. 757, 770 (1966) (“We are told that the
percentage of alcohol in the blood begins to diminish shortly
after drinking stops, as the body functions to eliminate
it from the system”). In that case, the Court recognized
that destruction of evidence is inherent in drunk-driving
cases and held that an officer investigating a drunk­
driving crime “might reasonably [believe] that he [is]
confronted with an emergency, in which the delay neces­
sary to obtain a warrant, under the circumstances, threat­
en[s] ‘the destruction of evidence.’ ” Ibid. (quoting Preston
v. United States, 376 U. S. 364, 367 (1964)). The Court
                    Cite as: 569 U. S. ____ (2013)                   3

                        THOMAS, J., dissenting

explained that drawing a person’s blood is “a highly ef-
fective means of determining the degree to which [he] is
under the influence of alcohol” and is a reasonable proce­
dure because blood tests are “commonplace” and “involv[e]
virtually no risk, trauma, or pain.”1 384 U. S., at 771. The
Court, therefore, held that dissipation of alcohol in the
blood constitutes an exigency that allows a blood draw
without a warrant.
   The rapid destruction of evidence acknowledged by the
parties, the majority, and Schmerber’s exigency determi­
nation occurs in every situation where police have probable
cause to arrest a drunk driver. In turn, that destruction
of evidence implicates the exigent-circumstances doctrine.
See Cupp v. Murphy, 412 U. S. 291 (1973). In Cupp,
officers questioning a murder suspect observed a spot on
the suspect’s finger that they believed might be dried
blood. Id., at 292. After the suspect began making obvi­
ous efforts to remove the spots from his hands, the officers
took samples without obtaining either his consent or a
warrant. Id., at 296. Following a Fourth Amendment
challenge to this search, the Court held that the “ready
destructibility of the evidence” and the suspect’s observed
efforts to destroy it “justified the police in subjecting him
to the very limited search necessary to preserve the highly
evanescent evidence they found under his fingernails.”
Ibid.
   In this case, a similar exigency is present. Just as the
suspect’s efforts to destroy “highly evanescent evidence”
gave rise to the exigency in Cupp, the natural metaboliza­
tion of blood alcohol concentration (BAC) creates an exi­
gency once police have probable cause to believe the driver

——————
  1 Neither party has challenged this determination, which this Court
has reaffirmed several times. See, e.g., Skinner v. Railway Labor
Executives’ Assn., 489 U. S. 602, 625 (1989); Winston v. Lee, 470 U. S.
753, 761–763 (1985).
4                  MISSOURI v. MCNEELY

                    THOMAS, J., dissenting

is drunk. It naturally follows that police may conduct a
search in these circumstances.
   A hypothetical involving classic exigent circumstances
further illustrates the point. Officers are watching a
warehouse and observe a worker carrying bundles from
the warehouse to a large bonfire and throwing them into
the blaze. The officers have probable cause to believe
the bundles contain marijuana. Because there is only one
person carrying the bundles, the officers believe it will
take hours to completely destroy the drugs. During that
time the officers likely could obtain a warrant. But it is
clear that the officers need not sit idly by and watch the
destruction of evidence while they wait for a warrant. The
fact that it will take time for the evidence to be destroyed
and that some evidence may remain by the time the offi­
cers secure a warrant are not relevant to the exigency.
However, the ever-diminishing quantity of drugs may
have an impact on the severity of the crime and the
length of the sentence. See, e.g., 21 U. S. C. §841(b)(1)(D)
(lower penalties for less than 50 kilograms of marijuana);
United States Sentencing Commission, Guidelines Manual
§2D1.1(c) (Nov. 2012) (drug quantity table tying base
offense level to drug amounts). Conducting a warrantless
search of the warehouse in this situation would be entirely
reasonable.
   The same obtains in the drunk-driving context. Just
because it will take time for the evidence to be completely
destroyed does not mean there is no exigency. Congress
has conditioned federal highway grants on states’ adoption
of laws penalizing the operation of a motor vehicle “with a
blood alcohol concentration of 0.08 percent or greater.” 23
U. S. C. §163(a). See also 23 CFR §1225.1 (2012). All 50
States have acceded to this condition. National Highway
Traffic Safety Admin. (NHTSA), Alcohol and Highway
Safety: A Review of the State of Knowledge 167 (No.
811374, Mar. 2011) (NHTSA State Review); Mo. Ann.
                 Cite as: 569 U. S. ____ (2013)           5

                    THOMAS, J., dissenting

Stat. §§577.012(1)–(2) (West 2011) (establishing Missouri’s
0.08 percent BAC standard). Moreover, as of 2005, 32
States and the District of Columbia imposed additional
penalties for BAC levels of 0.15 percent or higher. NHTSA
State Review 175. Missouri is one such State. See, e.g.,
Mo. Stat. Ann. §§577.010(3)–(4), 577.012(4)–(5) (suspended
sentence unavailable even for first offenders with BAC
above 0.15 percent unless they complete drug treatment;
mandatory jail time if treatment is not completed). As a
result, the level of intoxication directly bears on enforce­
ment of these laws. Nothing in the Fourth Amendment
requires officers to allow evidence essential to enforcement
of drunk-driving laws to be destroyed while they wait for a
warrant to issue.
                              II
  In today’s decision, the Court elides the certainty of
evidence destruction in drunk-driving cases and focuses
primarily on the time necessary for destruction. In doing
so, it turns the exigency inquiry into a question about the
amount of evidentiary destruction police must permit
before they may act without a warrant. That inquiry is
inconsistent with the actual exigency at issue: the un­
contested destruction of evidence due to metabolization of
alcohol. See Part I, supra. Moreover, the Court’s facts­
and-circumstances analysis will be difficult to administer,
a particularly important concern in the Fourth Amend­
ment context.
  The Court’s judgment reflects nothing more than a
vague notion that everything will come out right most of
the time so long as the delay is not too lengthy. Ante, at
12 (justifying delays in part because “BAC evidence is lost
gradually and relatively predictably”); ante, at 10 (same,
quoting Brief for Petitioner 27). But hard percentage lines
have meaningful legal consequences in the drunk-driving
context. The fact that police will be able to retrieve some
6                   MISSOURI v. MCNEELY

                     THOMAS, J., dissenting

evidence before it is all destroyed is simply not relevant to
the exigency inquiry.
   The majority believes that, absent special facts and
circumstances, some destruction of evidence is acceptable.
See ante, at 9 (“sufficient for our purposes to note that . . .
significant delay in testing will negatively affect the pro­
bative value” (emphasis added)). This belief must rest
on the assumption that whatever evidence remains once a
warrant is obtained will be sufficient to prosecute the
suspect. But that assumption is clearly wrong. Suspects’
initial levels of intoxication and the time necessary to
obtain warranted blood draws will vary widely from case
to case. Even a slight delay may significantly affect pro­
bative value in borderline cases of suspects who are mod­
erately intoxicated or suspects whose BAC is near a statu­
tory threshold that triggers a more serious offense. See
supra, at 4–5 (discussing laws penalizing heightened BAC
levels). Similarly, the time to obtain a warrant can be ex­
pected to vary, and there is no reason to believe it will
do so in a predictable fashion.
   Further, the Court nowhere explains how an officer in
the field is to apply the facts-and-circumstances test it
adopts. First, officers do not have the facts needed to
assess how much time can pass before too little evidence
remains. They will never know how intoxicated a suspect
is at the time of arrest. Otherwise, there would be no need
for testing. Second, they will not know how long it will
take to roust a magistrate from his bed, reach the hospital,
or obtain a blood sample once there. As the Minnesota
Supreme Court recognized in rejecting arguments like
those adopted by the Court today:
    “[T]he officer has no control over how long it would
    take to travel to a judge or the judge’s availability.
    The officer also may not know the time of the sus­
    pect’s last drink, the amount of alcohol consumed, or
                     Cite as: 569 U. S. ____ (2013)                     7

                         THOMAS, J., dissenting

     the rate at which the suspect will metabolize alcohol.
     Finally, an officer cannot know how long it will take to
     obtain the blood sample once the suspect is brought
     to the hospital. Under a totality of the circumstances
     test, an officer would be called upon to speculate on
     each of these considerations and predict how long the
     most probative evidence of the defendant’s blood­
     alcohol level would continue to exist before a blood
     sample was no longer reliable.” State v. Shriner, 751
     N. W. 2d 538, 549 (2008) (footnote omitted).
The Court should not adopt a rule that requires police to
guess whether they will be able to obtain a warrant before
“too much” evidence is destroyed, for the police lack reli-
able information concerning the relevant variables.2
   This case demonstrates the uncertainty officers face
with regard to the delay caused by obtaining a warrant.
The arresting officer clearly had probable cause to believe
respondent was drunk, but there was no way for the of­
ficer to quantify the level of intoxication to determine how
quickly he needed to act in order to obtain probative evi­
dence. Another officer testified at respondent’s trial that
it typically took 1 ½ to 2 hours to obtain a drunk-driving
warrant at night in Cape Girardeau County, Missouri.
See App. 53–54. Respondent submitted an exhibit sum­
marizing six late afternoon and nighttime drunk-driving
search warrants that suggests the time may be shorter.
——————
  2 Because the Court’s position is likely to result in delay in obtaining

BAC evidence, it also increases the likelihood that prosecutors will be
forced to estimate the amount of alcohol in a defendant’s bloodstream
using BAC numbers obtained hours later. In practice, this backwards
extrapolation is likely to devolve into a battle of the experts, as each
side seeks to show that stale evidence supports its position. There is no
need for this outcome. Police facing inevitable destruction situations
need not forgo collecting the most accurate available evidence simply
because they might be able to use an expert witness and less persuasive
evidence to approximate what they lost.
8                    MISSOURI v. MCNEELY

                       THOMAS, J., dissenting

Brief for Respondent 56; App. 70. Ultimately this factual
tiff is beside the point; the spotty evidence regarding
timing itself illustrates the fact that delays in obtaining
warrants are unpredictable and potentially lengthy. A
rule that requires officers (and ultimately courts) to bal­
ance transportation delays, hospital availability, and ac-
cess to magistrates is not a workable rule for cases where
natural processes inevitably destroy the evidence with
every passing minute.
   The availability of telephonic warrant applications is
not an answer to this conundrum. See ante, at 10–12,
and n. 4. For one thing, Missouri still requires written
warrant applications and affidavits, Mo. Ann. Stat.
§§542.276.2(1), 542.276.2.3 (West Supp. 2012), rendering
the Court’s 50-State survey irrelevant to the actual dispo­
sition of this case. Ante, at 11, n. 4. But even if telephonic
applications were available in Missouri, the same difficul­
ties would arise. As the majority correctly recognizes,
“[w]arrants inevitably take some time for police officers
or prosecutors to complete and for magistrate judges to
review.” Ante, at 12. During that time, evidence is de­
stroyed, and police who have probable cause to believe a
crime has been committed should not have to guess how
long it will take to secure a warrant.

                          *    *    * 

    For the foregoing reasons, I respectfully dissent. 


```

---
