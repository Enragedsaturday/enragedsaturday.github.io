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

## GROUP: content/cases/Pembaur v. City of Cincinnati.md  (`case`, 5 assertions)

### content_page

```
---
title: "Pembaur v. City of Cincinnati"
type: case
citation: "475 U.S. 469 (1986)"
parallel_cite: "106 S. Ct. 1292; 89 L. Ed. 2d 452; 54 U.S.L.W. 4289"
neutral_cite: 1986 U.S. LEXIS 33
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1986
date_decided: 1986-03-25
docket: 84-1160
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1986-03-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Pembaur v. City of Cincinnati
  varies_by_point: false
  scope_note: "Plurality on the single-decision point; the rule that a final policymaker's single decision can be municipal policy is settled law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111615/pembaur-v-city-of-cincinnati/"
  cluster_id: 111615
  opinion_id: 9430387
  identity_checked: true
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Monell v. Department of Social Services]]", "[[City of Canton v. Harris]]"]
aliases: []
tags: ["case", "section-1983", "municipal-liability", "policy-or-custom", "final-policymaker", "monell"]
holding: "A single decision by a municipal official with final policymaking authority for the relevant subject matter can be the 'official policy' that triggers Monell liability."
lake:
  record_id: Pembaur v. City of Cincinnati
  status: verified
  projected_at: 2026-07-06
---

# Pembaur v. City of Cincinnati

*475 U.S. 469 (1986)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Sheriff's deputies tried to serve capiases on two employees of Dr. Bernard Pembaur's medical clinic who had failed to appear before a grand jury. When Pembaur barred the deputies from entering, they telephoned the County Prosecutor, who instructed them to "go in and get" the witnesses. The deputies chopped down the door with an axe and entered. Pembaur sued the county and city under § 1983, claiming the warrantless entry was an official policy.

## Issue
Whether a municipality may be held liable under § 1983 for a single decision — here, the County Prosecutor's instruction to enter — made by an official with final authority to establish policy on that subject, even though the municipality had no pre-existing rule directing the conduct.

## Rule
Yes. *[[Monell v. Department of Social Services|Monell]]* liability does not require a rule applied in many cases; a single decision by an authorized policymaker is enough. "municipal liability under § 1983 attaches where — and only where — a deliberate choice to follow a course of action is made from among various alternatives by the official or officials responsible for establishing final policy with respect to the subject matter in question." — 475 U.S. at 483-484. ^pin-483

Liability attaches only when the decision is made by an official who possesses **final policymaking authority** for the area in question; whether an official has such authority is a question of state law.

## Application
The County Prosecutor was the official to whom the deputies were directed to turn for instruction, and on these facts he was treated as the final policymaker on how to execute the capiases. His specific direction to force entry was therefore a "deliberate choice" by a policymaking official, and the resulting entry was an act of official county policy — sufficient to support municipal liability for that single decision, without proof of any broader pattern or custom.

## Conclusion
Reversed and [[Reading and Citing Cases#on-remand|remanded]]. A municipality can be liable under § 1983 for a single act of an official with final policymaking authority for the relevant subject matter; the lower court erred in requiring a repeated practice or general policy.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Pembaur* elaborates the policy-or-custom requirement of [[Monell v. Department of Social Services]] by recognizing single-decision liability, and sits alongside the failure-to-train branch developed in [[City of Canton v. Harris]]. The "final policymaking authority" inquiry it framed remains the governing test (later refined in *City of St. Louis v. Praprotnik* and *McMillian v. Monroe County*).

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *Pembaur v. City of Cincinnati*, 475 U.S. 469 (1986) — https://www.courtlistener.com/opinion/111615/pembaur-v-city-of-cincinnati/ — pinpoint: 483-484.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "da77b0a5e5d0bdfd", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "475 U.S. 469 (1986)", "court": "U.S. Supreme Court", "neutral_cite": "1986 U.S. LEXIS 33", "official_citation_present": true, "parallel_cite": "106 S. Ct. 1292; 89 L. Ed. 2d 452; 54 U.S.L.W. 4289", "title": "Pembaur v. City of Cincinnati", "year": "1986"}}
{"assertion_id": "51160d649fa1a837", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Key — Progeny / Refinement", "title": "Pembaur v. City of Cincinnati"}}
{"assertion_id": "fcca80367849162e", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A single decision by a municipal official with final policymaking authority for the relevant subject matter can be the 'official policy' that triggers Monell liability.", "title": "Pembaur v. City of Cincinnati"}}
{"assertion_id": "398e4e95eb30400f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Pembaur v. City of Cincinnati"}}
{"assertion_id": "a8f8b76b29ab62a4", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1986-03-25", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Pembaur v. City of Cincinnati", "field_i_validity": "good_law", "scope_note": "Plurality on the single-decision point; the rule that a final policymaker's single decision can be municipal policy is settled law.", "title": "Pembaur v. City of Cincinnati", "varies_by_point": "false"}}
```

### lake record — Pembaur v. City of Cincinnati

```json
{
  "schema_version": "s2.v1",
  "record_id": "Pembaur v. City of Cincinnati",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Pembaur v. City of Cincinnati",
    "case_name_short": "Pembaur",
    "case_name_full": "PEMBAUR v. CITY OF CINCINNATI Et Al.",
    "input_case_name": "Pembaur v. City of Cincinnati",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-03-25",
    "year": 1986,
    "docket": "84-1160",
    "cluster_id": 111615,
    "lead_opinion_id": 9430387,
    "sibling_ids": [
      111615,
      9430387,
      9430388,
      9430389,
      9430390,
      9430391
    ],
    "absolute_url": "/opinion/111615/pembaur-v-city-of-cincinnati/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "475 U.S. 469",
      "volume": "475",
      "reporter": "U.S.",
      "page": "469",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "106 S. Ct. 1292",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 452",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "452",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4289",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4289",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 33",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "33",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "475 U.S. 469",
        "volume": "475",
        "reporter": "U.S.",
        "page": "469",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 1292",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 452",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "452",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 33",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "33",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4289",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4289",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "475 U.S. 469",
    "official_selection": {
      "court_class": "scotus",
      "selected": "475 U.S. 469",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-483",
      "page": null,
      "quote": "the witnesses. The deputies chopped down the door with an axe and entered. Pembaur sued the county and city under \u00a7 1983, claiming the warrantless entry was an official policy. ## Issue Whether a municipality may be held liable under \u00a7 1983 for a single decision \u2014 here, the County Prosecutor's instruction to enter \u2014 made by an official with final authority to establish policy on that subject, even though the municipality had no pre-existing rule directing the conduct. ## Rule Yes. *Monell* liability does not require a rule applied in many cases; a single decision by an authorized policymaker is enough.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1986-03-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Pembaur v. City of Cincinnati",
    "varies_by_point": false,
    "scope_note": "Plurality on the single-decision point; the rule that a final policymaker's single decision can be municipal policy is settled law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Baptiste v. Executive Office of Health & Human Services",
          "cluster_id": 4731494,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Harris County, Texas and Kevin Vailes v. Barbara Coats, Individually, as Personal Representative of the Estate of Jamail Amron, and as Heir to the Estate of Jamail Amron, And Ali Amron, Individually and as Heir to the Estate of Jamail Amron, Barbara Coats",
          "cluster_id": 4725124,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gregory Baldwin v. City of Estherville, Iowa",
          "cluster_id": 4629600,
          "cite": [
            "929 N.W.2d 691"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cherry Knoll, L.L.C. v. HDR Engineering, Incorpora",
          "cluster_id": 4612302,
          "cite": [
            "922 F.3d 309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Keyon Harrison v. Curt Vanderkooi",
          "cluster_id": 4522518,
          "cite": [
            "918 N.W.2d 785",
            "502 Mich. 751"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Herbert Liverman v. City of Petersburg",
          "cluster_id": 4330488,
          "cite": [
            "844 F.3d 400",
            "41 I.E.R. Cas. (BNA) 1449",
            "2016 U.S. App. LEXIS 22282",
            "100 Empl. Prac. Dec. (CCH) 45,713",
            "2016 WL 7240179"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Causey v. the State",
          "cluster_id": 3148713,
          "cite": [
            "334 Ga. App. 170",
            "778 S.E.2d 800"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lloyd v. Birkman",
          "cluster_id": 7315423,
          "cite": [
            "127 F. Supp. 3d 725",
            "2015 U.S. Dist. LEXIS 117410",
            "2015 WL 5202687"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jonathon Castro v. County of Los Angeles",
          "cluster_id": 2826317,
          "cite": [
            "797 F.3d 654",
            "2015 U.S. App. LEXIS 14132",
            "2015 WL 4731366"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Salvato Ex Rel. Estate of Salvato v. Miley",
          "cluster_id": 2812003,
          "cite": [
            "790 F.3d 1286"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jonathon Castro v. County of Los Angeles",
          "cluster_id": 2798029,
          "cite": [
            "785 F.3d 336",
            "2015 U.S. App. LEXIS 7240",
            "2015 WL 1948146"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City of Canton v. Harris",
          "cluster_id": 112209,
          "cite": [
            "103 L. Ed. 2d 412",
            "109 S. Ct. 1197",
            "489 U.S. 378",
            "1989 U.S. LEXIS 1200",
            "57 U.S.L.W. 4270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of the County Commissioners of Bryan County v. Brown",
          "cluster_id": 118104,
          "cite": [
            "137 L. Ed. 2d 626",
            "117 S. Ct. 1382",
            "520 U.S. 397",
            "1997 U.S. LEXIS 2793",
            "65 U.S.L.W. 4286",
            "10 Fla. L. Weekly Fed. S 405",
            "12 I.E.R. Cas. (BNA) 1217",
            "97 Cal. Daily Op. Serv. 3033",
            "97 Daily Journal DAR 5311"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of St. Louis v. Praprotnik",
          "cluster_id": 112017,
          "cite": [
            "99 L. Ed. 2d 107",
            "108 S. Ct. 915",
            "485 U.S. 112",
            "1988 U.S. LEXIS 1069"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Starr v. Baca",
          "cluster_id": 8441026,
          "cite": [
            "652 F.3d 1202",
            "2011 U.S. App. LEXIS 15283",
            "2011 WL 2988827"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. City of Harker Heights",
          "cluster_id": 112699,
          "cite": [
            "117 L. Ed. 2d 261",
            "112 S. Ct. 1061",
            "503 U.S. 115",
            "1992 U.S. LEXIS 1376"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lee v. City of Los Angeles",
          "cluster_id": 7092482,
          "cite": [
            "250 F.3d 668",
            "2001 WL 468408"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lee v. City Of Los Angeles",
          "cluster_id": 773312,
          "cite": [
            "250 F.3d 668",
            "2001 Cal. Daily Op. Serv. 3507",
            "2001 Daily Journal DAR 4351",
            "56 Fed. R. Serv. 698",
            "2001 U.S. App. LEXIS 8150"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
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
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jett v. Dallas Independent School District",
          "cluster_id": 112313,
          "cite": [
            "105 L. Ed. 2d 598",
            "109 S. Ct. 2702",
            "491 U.S. 701",
            "1989 U.S. LEXIS 3130",
            "57 U.S.L.W. 4858",
            "50 Fair Empl. Prac. Cas. (BNA) 27",
            "50 Empl. Prac. Dec. (CCH) 39,070"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Murray",
          "cluster_id": 111728,
          "cite": [
            "91 L. Ed. 2d 434",
            "106 S. Ct. 2661",
            "477 U.S. 527",
            "1986 U.S. LEXIS 67",
            "54 U.S.L.W. 4833"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Piotrowski v. City of Houston",
          "cluster_id": 22972,
          "cite": [
            "237 F.3d 567",
            "2001 U.S. App. LEXIS 603",
            "2001 WL 6712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Philomene Long, Surviving Spouse and Heir-At-Law of John Thomas Idlet, Deceased v. County of Los Angeles",
          "cluster_id": 793848,
          "cite": [
            "442 F.3d 1178",
            "2006 U.S. App. LEXIS 7552",
            "2006 WL 770615"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kneipp v. Tedder",
          "cluster_id": 726573,
          "cite": [
            "95 F.3d 1199",
            "159 A.L.R. Fed. 619",
            "1996 U.S. App. LEXIS 24401"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Keith A. Hill v. Borough of Kutztown and Gennaro Marino, Mayor of Kutztown, in His Individual and Official Capacity",
          "cluster_id": 795079,
          "cite": [
            "455 F.3d 225",
            "2006 U.S. App. LEXIS 18708",
            "98 Fair Empl. Prac. Cas. (BNA) 942",
            "2006 WL 2061145"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Grieveson v. Anderson",
          "cluster_id": 1443143,
          "cite": [
            "538 F.3d 763",
            "2008 WL 3823872"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lucas Burgess v. Gene Fischer",
          "cluster_id": 2641010,
          "cite": [
            "735 F.3d 462",
            "2013 WL 5873323",
            "2013 U.S. App. LEXIS 22279"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edwards v. City of Goldsboro",
          "cluster_id": 764384,
          "cite": [
            "178 F.3d 231",
            "15 I.E.R. Cas. (BNA) 333",
            "43 Fed. R. Serv. 3d 890",
            "1999 U.S. App. LEXIS 9088"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kathleen Hansen v. Ronald L. Black",
          "cluster_id": 529383,
          "cite": [
            "885 F.2d 642",
            "1989 U.S. App. LEXIS 13906",
            "1989 WL 106525"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cion Peralta v. T. Dillard",
          "cluster_id": 2655912,
          "cite": [
            "744 F.3d 1076",
            "2014 WL 878830",
            "2014 U.S. App. LEXIS 4226"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shirley Presley v. City of Charlottesville Rivanna Trails Foundation",
          "cluster_id": 795822,
          "cite": [
            "464 F.3d 480",
            "2006 U.S. App. LEXIS 24048",
            "2006 WL 2709208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Trevino v. Gates",
          "cluster_id": 7040066,
          "cite": [
            "99 F.3d 911",
            "96 Daily Journal DAR 13300",
            "45 Fed. R. Serv. 1143",
            "96 Cal. Daily Op. Serv. 8007",
            "1996 U.S. App. LEXIS 28299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gibson v. County of Washoe, Nevada",
          "cluster_id": 777732,
          "cite": [
            "290 F.3d 1175",
            "2002 Cal. Daily Op. Serv. 4392",
            "2002 Daily Journal DAR 5649",
            "2002 U.S. App. LEXIS 9604"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Laurie Tsao v. Desert Palace, Inc.",
          "cluster_id": 810771,
          "cite": [
            "698 F.3d 1128",
            "2012 WL 5200336"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Edward Hoefling, Jr. v. City of Miami",
          "cluster_id": 3171918,
          "cite": [
            "811 F.3d 1271",
            "93 Fed. R. Serv. 3d 1022",
            "2016 U.S. App. LEXIS 1177",
            "2016 WL 285358"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McTernan v. City of York, Pa.",
          "cluster_id": 1192469,
          "cite": [
            "564 F.3d 636",
            "2009 U.S. App. LEXIS 8884",
            "2009 WL 1111097"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111615 OR 9430387 OR 9430388 OR 9430389 OR 9430390 OR 9430391) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDMwNDM4NDAwMDAwJnM9Mjc5ODAyOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111615+OR+9430387+OR+9430388+OR+9430389+OR+9430390+OR+9430391%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 12,
        "triage_snippet_classified": 188
      },
      "lane2_top_cited": {
        "query": "cites:(111615 OR 9430387 OR 9430388 OR 9430389 OR 9430390 OR 9430391)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03Mzcmcz00OTgwNTEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111615+OR+9430387+OR+9430388+OR+9430389+OR+9430390+OR+9430391%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111615 OR 9430387 OR 9430388 OR 9430389 OR 9430390 OR 9430391)",
        "reviewed": 43,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 43,
        "triage_read": 0,
        "triage_snippet_classified": 43
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111615 OR 9430387 OR 9430388 OR 9430389 OR 9430390 OR 9430391)",
    "indexed_citing_opinions": 2453,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111615,
        "count": 2209,
        "count_source": "search"
      },
      {
        "opinion_id": 9430387,
        "count": 260,
        "count_source": "search"
      },
      {
        "opinion_id": 9430388,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430389,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430390,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430391,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6111,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/pembaur-v-city-of-cincinnati.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5NDczODImcz0xMDA0OTcyMSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111615+OR+9430387+OR+9430388+OR+9430389+OR+9430390+OR+9430391%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111615,
        "cited_id": 105382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 108330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 108406,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 109387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 109476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 109776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 110061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 110236,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 110553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 110754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 111219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 111355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 111441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 111480,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 276331,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 343372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 370304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 373791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 381330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 382937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 415320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 429458,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 437247,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 443017,
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
    "date_created": "2026-07-05T16:42:52Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:43:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:43:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:46:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:43:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Pembaur v. City of Cincinnati

```
<opinion type="majority">
<author id="b553-7">Justice Brennan</author>
<p id="AfU">delivered the opinion of the Court, except as to Part II-B.</p>
<p id="b553-8">In <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span> (1978), the Court concluded that municipal liability-under <span class="citation no-link">42 U. S. C. § 1983</span> is limited to deprivations of federally protected rights caused by action taken “pursuant to official municipal policy of some nature . . . .” <span class="citation no-link"><em>Id., </em>at 691</span>. The question presented is whether, and in what circumstances, a decision by municipal policymakers on a single occasion may satisfy this requirement.</p>
<p id="b553-9">I</p>
<p id="b553-10">Bertold Pembaur is a licensed Ohio physician and the sole proprietor of the Rockdale Medical Center, located in the city of Cincinnati in Hamilton County. Most of Pembaur’s patients are welfare recipients who rely on government assistance to pay for medical care. During the spring of 1977, Simon Leis, the Hamilton County Prosecutor, began investigating charges that Pembaur fraudulently had accepted payments from state welfare agencies for services not actually provided to patients. A grand jury was convened, and the case was assigned to Assistant Prosecutor William Whalen. <page-number citation-index="1" label="472">*472</page-number>In April, the grand jury charged Pembaur in a six-count indictment.</p>
<p id="b554-5">During the investigation, the grand jury issued subpoenas for the appearance of two of Pembaur’s employees. When these employees failed to appear as directed, the Prosecutor obtained capiases for their arrest and detention from the Court of Common Pleas of Hamilton County.<footnotemark>1</footnotemark></p>
<p id="b554-6">On May 19,1977, two Hamilton County Deputy Sheriffs attempted to serve the capiases at Pembaur’s clinic. Although the reception area is open to the public, the rest of the clinic may be entered only through a door next to the receptionist’s window. Upon arriving, the Deputy Sheriffs identified themselves to the receptionist and sought to pass through this door, which was apparently open. The receptionist blocked their way and asked them to wait for the doctor. When Pembaur appeared a moment later, he and the receptionist closed the door, which automatically locked from the inside, and wedged a piece of wood between it and the wall. Returning to the receptionist’s window, the Deputy Sheriffs identified themselves to Pembaur, showed him the capiases and explained why they were there. Pembaur refused to let them enter, claiming that the police had no legal authority to be there and requesting that they leave. He told them that he had called the Cincinnati police, the local media, and his lawyer. The Deputy Sheriffs decided not to take further action until the Cincinnati police arrived.</p>
<p id="b554-7">Shortly thereafter, several Cincinnati police officers appeared. The Deputy Sheriffs explained the situation to them and asked that they speak to Pembaur. The Cincinnati police told Pembaur that the papers were lawful and that he should allow the Deputy Sheriffs to enter. When Pembaur refused, the Cincinnati police called for a superior officer. When he too failed to persuade Pembaur to open the door, <page-number citation-index="1" label="473">*473</page-number>the Deputy Sheriffs decided to call their supervisor for further instructions. Their supervisor told them to call Assistant Prosecutor Whalen and to follow his instructions. The Deputy Sheriffs then telephoned Whalen and informed him of the situation. Whalen conferred with County Prosecutor Leis, who told Whalen to instruct the Deputy Sheriffs to "go in and get [the witnesses].” Whalen in turn passed these instructions along to the Deputy Sheriffs.</p>
<p id="b555-5">After a final attempt to persuade Pembaur voluntarily to allow them to enter, the Deputy Sheriffs tried unsuccessfully to force the door. City police officers, who had been advised of the County Prosecutor’s instructions to “go in and get” the witnesses, obtained an axe and chopped down the door. The Deputy Sheriffs then entered and searched the clinic. Two individuals who fit descriptions of the witnesses sought were detained, but turned out not to be the right persons.</p>
<p id="b555-6">After this incident, the Prosecutor obtained an additional indictment against Pembaur for obstructing police in the performance of an authorized act. Although acquitted of all other charges, Pembaur was convicted for this offense. The Ohio Court of Appeals reversed, reasoning that Pembaur was privileged under state law to exclude the deputies because the search of his office violated the Fourth Amendment. <em>State </em>v. <em>Pembaur, </em>No. C-790380 (Hamilton County Court of Appeals, Nov. 3, 1982). The Ohio Supreme Court reversed and reinstated the conviction. <em>State </em>v. <em>Pembaur, </em><span class="citation" data-id="6758271"><a href="/opinion/6867449/state-v-pembaur/" aria-description="Citation for case: State v. Pembaur">9 Ohio St. 3d 136</a></span>, <span class="citation" data-id="6758271"><a href="/opinion/6867449/state-v-pembaur/" aria-description="Citation for case: State v. Pembaur">459 N. E. 2d 217</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./467/1219/">467 U. S. 1219</a></span> (1984). The Supreme Court held that the state-law privilege applied only to bad-faith conduct by law enforcement officials, and that, under the circumstances of this case, Pembaur was obliged to acquiesce to the search and seek redress later in a civil action for damages. <span class="citation" data-id="6758271"><a href="/opinion/6867449/state-v-pembaur/#138" aria-description="Citation for case: State v. Pembaur">9 Ohio St. 3d, at 138</a></span>, <span class="citation" data-id="6758271"><a href="/opinion/6867449/state-v-pembaur/#219" aria-description="Citation for case: State v. Pembaur">459 N. E. 2d, at 219</a></span>.</p>
<p id="b555-7">On April 20, 1981, Pembaur filed the present action in the United States District Court for the Southern District of Ohio against the city of Cincinnati, the County of Hamilton, <page-number citation-index="1" label="474">*474</page-number>the Cincinnati Police Chief, the Hamilton County Sheriff, the members of the Hamilton Board of County Commissioners (in their official capacities only), Assistant Prosecutor Whalen, and nine city and county police officers.<footnotemark>2</footnotemark> Pembaur sought damages under <span class="citation no-link">42 U. S. C. § 1983</span>, alleging that the county and city police had violated his rights under the Fourth and Fourteenth Amendments. His theory was that, absent exigent circumstances, the Fourth Amendment prohibits police from searching an individual’s home or business without a search warrant even to execute an arrest warrant for a third person. We agreed with that proposition in <em>Steagald </em>v. <em>United States, </em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">451 U. S. 204</a></span> (1981), decided the day after Pembaur filed this lawsuit. Pembaur sought $10 million in actual and $10 million in punitive damages, plus costs and attorney’s fees.</p>
<p id="b556-4">Much of the testimony at the 4-day trial concerned the practices of the Hamilton County Police in serving capiases. Frank Webb, one of the Deputy Sheriffs present at the clinic on May 19, testified that he had previously served capiases on the property of third persons without a search warrant, but had never been required to use force to gain access. Assistant Prosecutor Whalen was also unaware of a prior instance in which police had been denied access to a third person’s property in serving a capias and had used force to gain entry. Lincoln Stokes, the County Sheriff, testified that the Department had no written policy respecting the serving of capiases on the property of third persons and that the proper response in any given situation would depend upon the circumstances. He too could not recall a specific instance in <page-number citation-index="1" label="475">*475</page-number>which entrance had been denied and forcibly gained. Sheriff Stokes did testify, however, that it was the practice in his Department to refer questions to the County Prosecutor for instructions under appropriate circumstances and that “it was the proper thing to do” in this case.</p>
<p id="b557-5">The District Court awarded judgment to the defendants and dismissed the complaint in its entirety. The court agreed that the entry and search of Pembaur’s clinic violated the Fourth Amendment under <em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">Steagald, supra,</a></span> </em>but held <em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">Steagald</a></span> </em>inapplicable since it was decided nearly four years after the incident occurred. Because it construed the law in the Sixth Circuit in 1977 to permit law enforcement officials to enter the premises of a third person to serve a capias, the District Court held that the individual municipal officials were all immune under <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800</a></span> (1982).</p>
<p id="b557-6">The claims against the county and the city were dismissed on the ground that the individual officers were not acting pursuant to the kind of “official policy” that is the predicate for municipal liability under <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>. </em>With respect to Hamilton County, the court explained that, even assuming that the entry and search were pursuant to a governmental policy, “it was not a policy of Hamilton County <em>per se” </em>because “[t]he Hamilton County Board of County Commissioners, acting on behalf of the county, simply does not establish or control the policies of the Hamilton County Sheriff.” With respect to the city of Cincinnati, the court found that “the only policy or custom followed . . . was that of aiding County Sheriff’s Deputies in the performance of their duties.” The court found that any participation by city police in the entry and search of The clinic resulted from decisions by individual officers as to the permissible scope of assistance they could provide, and not from a city policy to provide this particular kind of assistance.</p>
<p id="b557-7">On appeal, Pembaur challenged only the dismissal of his claims against Whalen, Hamilton County, and the city of Cin<page-number citation-index="1" label="476">*476</page-number>cinnati. The Court of Appeals for the Sixth Circuit upheld the dismissal of Pembaur’s claims against Whalen and Hamilton County, but reversed the dismissal of his claim against the city of Cincinnati on the ground that the District Court’s findings concerning the policies followed by the Cincinnati police were clearly erroneous. <span class="citation multiple-matches"><a href="/c/F.%202d/746/337/">746 F. 2d 337</a></span> (1984).<footnotemark>3</footnotemark></p>
<p id="b558-5">The Court of Appeals affirmed the District Court’s dismissal of Pembaur’s claim against Hamilton County, but on different grounds. The court held that the County Board’s lack of control over the Sheriff would not preclude county liability if “the nature and duties of the Sheriff are such that his acts may fairly be said to represent the county’s official policy with respect to the specific subject matter.” <em>Id., </em>at 340-341. Based upon its examination of Ohio law, the Court of Appeals found it “clea[r]” that the Sheriff and the Prosecutor were both county officials authorized to establish “the official policy of Hamilton County” with respect to matters of law enforcement. <em>Id., </em>at 341. Notwithstanding these conclusions, however, the court found that Pembaur’s claim against the county had been properly dismissed:</p>
<blockquote id="b558-6">“We believe that Pembaur failed to prove the existence of a county policy in this case. Pembaur claims that the deputy sheriffs acted pursuant to the policies of the Sheriff and Prosecutor by forcing entry into the medical center. Pembaur has failed to establish, however, anything more than that, on this <em>one occasion, </em>the Prosecutor and the Sheriff decided to force entry into his office. . . . That single, discrete decision is insufficient, <page-number citation-index="1" label="477">*477</page-number>by itself, to establish that the Prosecutor, the Sheriff, or both were implementing a governmental policy.” <em>Ibid. </em>(footnote omitted) (emphasis in original).</blockquote>
<p id="Anh">Pembaur petitioned for certiorari to review only the dismissal of his claim against Hamilton County. The decision of the Court of Appeals conflicts with holdings in several other Courts of Appeals,<footnotemark>4</footnotemark> and we granted the petition to resolve the conflict. <span class="citation multiple-matches"><a href="/c/U.%20S./472/1016/">472 U. S. 1016</a></span> (1985). We reverse.</p>
<p id="Afh">h-i t — I</p>
<p id="ASX7">A</p>
<p id="AB7">Our analysis must begin with the proposition that “Congress did not intend municipalities to be held liable unless action pursuant to official municipal policy of some nature caused a constitutional tort.” <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#691" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 691</a></span>.<footnotemark>5</footnotemark> As we read its opinion, the Court of Appeals held that a single decision to <page-number citation-index="1" label="478">*478</page-number>take particular action, although made by municipal policymakers, cannot establish the kind of “official policy” required by <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>as a predicate to municipal liability under § 1983.<footnotemark>6</footnotemark> The Court of Appeals reached this conclusion without referring to <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>— indeed, without any explanation at all. However, examination of the opinion in <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>clearly demonstrates that the Court of Appeals misinterpreted its holding.</p>
<p id="b560-5"><em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>is a case about responsibility. In the first part of the opinion, we held that local government units could be made liable under § 1983 for deprivations of federal rights, overruling a contrary holding in <em>Monroe </em>v. <em>Pape, </em><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167</a></span> (1961). In the second part of the opinion, we recognized a limitation on this liability and concluded that a municipality cannot be made liable by application of the doctrine of <em>respondeat superior. </em>See <em>Monell, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#691" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 691</a></span>. In part, this conclusion rested upon the language of §1983, which imposes liability only on a person who “subjects, or causes to be subjected,” any individual to a deprivation of federal rights; we noted that this language “cannot easily be read to impose liability vicariously on government bodies solely on the basis of the existence of an employer-employee relationship -with a tortfeasor.” <em>Id., </em>at 692. Primarily, <page-number citation-index="1" label="479">*479</page-number>however, our conclusion rested upon the legislative history, which disclosed that, while Congress never questioned its power to impose civil liability on municipalities for their <em>own </em>illegal acts, Congress did doubt its constitutional power to impose such liability in order to oblige municipalities to control the conduct of <em>others. Id., </em>at 665-683.<footnotemark>7</footnotemark> We found that, because of these doubts, Congress chose not to create such obligations in § 1983. Recognizing that this would be the effect of a federal law of <em>respondeat superior, </em>we concluded that § 1983 could not be interpreted to incorporate doctrines of vicarious liability. <em>Id., </em>at 692-694, and n. 57.</p>
<p id="b561-5">The conclusion that tortious conduct, to be the basis for municipal liability under §1983, must be pursuant to a municipality’s “official policy” is contained in this discussion. The “official policy” requirement was intended to distinguish acts of the <em>municipality </em>from acts of <em>employees </em>of the municipality, and thereby make clear that municipal liability is limited to action for which the municipality is actually responsi<page-number citation-index="1" label="480">*480</page-number>ble.<footnotemark>8</footnotemark> <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>reasoned that recovery from a municipality is limited to acts that are, properly speaking, acts “of the municipality” — that is, acts which the municipality has officially sanctioned or ordered.</p>
<p id="b562-5">With this understanding, it is plain that municipal liability may be imposed for a single decision by municipal policymakers under appropriate circumstances. No one has ever doubted, for instance, that a municipality may be liable under § 1983 for a single decision by its properly constituted legislative body — whether or not that body had taken similar action in the past or intended to do so in the future — because even a single decision by such a body unquestionably constitutes an act of official government policy. See, <em>e. g., Owen </em>v. <em>City of Independence, </em><span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/" aria-description="Citation for case: Owen v. City of Independence">445 U. S. 622</a></span> (1980) (City Council passed resolution firing plaintiff without a pretermination hearing); <em>Newport </em>v. <em>Fact Concerts, Inc., </em><span class="citation" data-id="9428471"><a href="/opinion/110553/city-of-newport-v-fact-concerts-inc/" aria-description="Citation for case: City of Newport v. Fact Concerts, Inc.">453 U. S. 247</a></span> (1981) (City Council canceled license permitting concert because of dispute over content of performance). But the power to establish policy is no more the exclusive province of the legislature at the local level than at the state or national level. Monell’s language makes clear that it expressly envisioned other officials “whose acts or edicts may fairly be said to represent official policy,” <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs."><em>Monell, supra, </em>at 694</a></span>, and whose decisions therefore may give rise to municipal liability under § 1983.</p>
<p id="b562-6">Indeed, any other conclusion would be inconsistent with the principles underlying § 1983. To be sure, “official policy” often refers to formal rules or understandings — often but not always committed to writing — that are intended to, and do, establish fixed plans of action to be followed under similar cir<page-number citation-index="1" label="481">*481</page-number>cumstances consistently and over time. That was the case in <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>itself, which involved a written rule requiring pregnant employees to take unpaid leaves of absence before such leaves were medically necessary. However, as in <em>Owen </em>and <em><span class="citation" data-id="9428471"><a href="/opinion/110553/city-of-newport-v-fact-concerts-inc/" aria-description="Citation for case: City of Newport v. Fact Concerts, Inc.">Newport</a></span>, </em>a government frequently chooses a course of action tailored to a particular situation and not intended to control decisions in later situations. If the decision to adopt that particular course of action is properly made by that government’s authorized decisionmakers, it surely represents an act of official government “policy” as that term is commonly understood.<footnotemark>9</footnotemark> More importantly, where action is directed by those who establish governmental policy, the municipality is equally responsible whether that action is to be taken only once or to be taken repeatedly. To deny compensation to the victim would therefore be contrary to the fundamental purpose of § 1983.</p>
<p id="b563-5">B</p>
<p id="b563-6">Having said this much, we hasten to emphasize that not every decision by municipal officers automatically subjects the municipality to §1983 liability. Municipal liability attaches only where the decisionmaker possesses final authority to establish municipal policy with respect to the action ordered.<footnotemark>10</footnotemark> The fact that a particular official — even a policy-<page-number citation-index="1" label="482">*482</page-number>making official — has discretion in the exercise of particular functions does not, without more, give rise to municipal liability based on an exercise of that discretion. See, <em>e. g., Oklahoma City </em>v. <em>Tuttle, </em>471 U. S., at 822-824.<footnotemark>11</footnotemark> The offi<page-number citation-index="1" label="483">*483</page-number>cial must also be responsible for establishing final government policy respecting such activity before the municipality can be held liable.<footnotemark>12</footnotemark> Authority to make municipal policy may be granted directly by a legislative enactment or may be delegated by an official who possesses such authority, and of course, whether an official had final policymaking authority is a question of state law. However, like other governmental entities, municipalities often spread policymaking authority among various officers and official bodies. As a result, particular officers may have authority to establish binding county policy respecting particular matters and to adjust that policy for the county in changing circumstances. To hold a municipality liable for actions ordered by such officers exercising their policymaking authority is no more an application of the theory of <em>respondeat superior </em>than was holding the municipalities liable for the decisions of the City Councils in <em>Owen </em>and <em><span class="citation" data-id="9428471"><a href="/opinion/110553/city-of-newport-v-fact-concerts-inc/" aria-description="Citation for case: City of Newport v. Fact Concerts, Inc.">Newport</a></span>. </em>In each case municipal liability attached to a single decision to take unlawful action made by municipal policymakers. We hold that municipal liability under §1983 attaches where — and only where — a deliberate choice to follow a course of action is made from among various alternatives by the official or officials responsible for establishing final policy with respect to the subject matter in ques<page-number citation-index="1" label="484">*484</page-number>tion. See <em>Tuttle, supra, </em>at 823 (“‘policy’ generally implies a course of action consciously chosen from among various alternatives”).</p>
<p id="b566-5">C</p>
<p id="b566-6">Applying this standard to the case before us, we have little difficulty concluding that the Court of Appeals erred in dismissing petitioner’s claim against the county. The Deputy Sheriffs who attempted to serve the capiases at petitioner’s clinic found themselves in a difficult situation. Unsure of the proper course of action to follow, they sought instructions from their supervisors. The instructions they received were to follow the orders of the County Prosecutor. The Prosecutor made a considered decision based on his understanding of the law and commanded the officers forcibly to enter petitioner’s clinic. That decision directly caused the violation of petitioner’s Fourth Amendment rights.</p>
<p id="b566-7">Respondent argues that the County Prosecutor lacked authority to establish municipal policy respecting law enforcement practices because only the County Sheriff may establish policy respecting such practices. Respondent suggests that the County Prosecutor was merely rendering “legal advice” when he ordered the Deputy Sheriffs to “go in and get” the witnesses. Consequently, the argument concludes, the action of the individual Deputy Sheriffs in following this advice and forcibly entering petitioner’s clinic was not pursuant to a properly established municipal policy.</p>
<p id="b566-8">We might be inclined to agree with respondent if we thought that the Prosecutor had only rendered “legal advice.” However, the Court of Appeals concluded, based upon its examination of Ohio law, that both the County Sheriff and the County Prosecutor could establish county policy under appropriate circumstances, a conclusion that we do not question here.<footnotemark>13</footnotemark> <span class="citation no-link">Ohio Rev. Code Ann. § 309.09</span>(A) (1979) <page-number citation-index="1" label="485">*485</page-number>provides that county officers may “require . . . instructions from [the County Prosecutor] in matters connected with their official duties.” Pursuant to standard office procedure, the Sheriff’s Office referred this matter to the Prosecutor and then followed his instructions. The Sheriff testified that his Department followed this practice under appropriate circumstances and that it was “the proper thing to do” in this case. We decline to accept respondent’s invitation to overlook this delegation of authority by disingenuously labeling the Prosecutor’s clear command mere “legal advice.” In ordering the Deputy Sheriffs to enter petitioner’s clinic the County Prosecutor was acting as the final decisionmaker for the county, and the county may therefore be held liable under § 1983.</p>
<p id="b567-5">The decision of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b567-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b554-8"> A capias is a writ of attachment commanding a county official to bring a subpoenaed witness who has failed to appear before the court to testify and to answer for civil contempt. See <span class="citation no-link">Ohio Rev. Code Ann. § 2317.21</span> (1981).</p>
</footnote>
<footnote label="2">
<p id="b556-5"> Hamilton County Prosecutor Leis was not made a defendant because counsel for petitioner believed that Leis was absolutely immune. Tr., Mar. 14-Mar. 17, p. 267. We express no view as to the correctness of this evaluation. Cf. <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#430" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409, 430-431</a></span> (1976) (leaving open the question of a prosecutor’s immunity when he acts “in the role of an administrator or investigative officer rather than that of an advocate”).</p>
</footnote>
<footnote label="3">
<p id="b558-7"> The court found that there was a city policy respecting the use of force in serving capiases as well as a policy of aiding county police. It based this conclusion on the testimony of Cincinnati Chief of Police Myron Leistler, who stated that it was the policy of his Department to take whatever steps were necessary, including the forcing of doors, to serve an arrest document. 746 F. 2d, at 341-342; see also, Tr., Mar. 14-Mar. 17, pp. 43-45, 46-47. The court remanded the case for a determination whether Pembaur’s injury was incurred as a result of the execution of this policy. 746 F. 2d, at 342.</p>
</footnote>
<footnote label="4">
<p id="A7f"> See, <em>e. g., McKinley </em>v. <em>City of Eloy, </em><span class="citation" data-id="8916800"><a href="/opinion/8927003/mckinley-v-city-of-eloy/#1116" aria-description="Citation for case: McKinley v. City of Eloy">705 F. 2d 1110, 1116-1117</a></span> (CA9 1983); <em>Berdin </em>v. <em>Duggan, </em><span class="citation" data-id="415320"><a href="/opinion/415320/thomas-berdin-cross-appellants-v-john-duggan-cross-appellees/#913" aria-description="Citation for case: Thomas Berdin, Cross-Appellants v. John Duggan,...">701 F. 2d 909, 913-914</a></span> (CA11), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./464/893/">464 U. S. 893</a></span> (1983); <em>Van Ooteghem </em>v. <em>Gray, </em><span class="citation" data-id="8911969"><a href="/opinion/8922923/van-ooteghem-v-gray/#494" aria-description="Citation for case: Van Ooteghem v. Gray">628 F. 2d 488, 494-495</a></span> (CA5 1980), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./455/909/">455 U. S. 909</a></span> (1982); <em>Quinn </em>v. <em>Syracuse Model Neighborhood Corp., </em><span class="citation" data-id="8910812"><a href="/opinion/8921905/quinn-v-syracuse-model-neighborhood-corp/#448" aria-description="Citation for case: Quinn v. Syracuse Model Neighborhood Corp.">613 F. 2d 438, 448</a></span> (CA2 1980). See also <em>Sanders </em>v. <em>St. Louis County, 724 </em>F. 2d 665, 668 (CA8 1983) <em>(per curiam) </em>(“It may be that one act of a senior county official is enough to establish the liability of the county, if that official was in a position to establish policy and if that official himself directly violated another’s constitutional rights”). But see <em>Losch </em>v. <em>Borough of Parkesburg, Pa., </em><span class="citation" data-id="437247"><a href="/opinion/437247/frank-a-losch-v-borough-of-parkesburg-pennsylvania-lester-j-thomas/#910" aria-description="Citation for case: Frank A. Losch v. Borough of Parkesburg, Pennsylvania...">736 F. 2d 903, 910-911</a></span> (CA3 1984) (“[E]ven if [the Police Chief] were the final authority with regard to police activities, . . . there is no regulation or evidence of any repeated action by [the chief]. . . that can transmute his actions in the Losch incident into a general Borough policy”).</p>
</footnote>
<footnote label="5">
<p id="AFGz"> There is no question in this case that petitioner suffered a constitutional deprivation. The Court of Appeals found, and respondent concedes, that the entry and search of petitioner’s clinic violated the Fourth Amendment under <em>Steagald </em>v. <em>United States, </em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">451 U. S. 204</a></span> (1981). See 746 F. 2d, at 340, n. 1; Brief for Respondents 11. Respondent never challenged and has in fact also conceded that <em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">Steagald</a></span> </em>applies retroactively to this case. See Tr. of Oral Arg. 26-27. We decide this case in light of respondent’s concessions.</p>
</footnote>
<footnote label="6">
<p id="b560-6"> The opinion below also can be read as holding that municipal liability cannot be imposed for a single incident of unconstitutional <em>conduct </em>by municipal employees whether or not that conduct is pursuant to municipal <em>policy. </em>Such a conclusion is unsupported by either the language or reasoning of <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>, </em>or by any of our subsequent decisions. As we explained last Term in <em>Oklahoma City </em>v. <em>Tuttle, </em><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S. 808</a></span> (1985), once a municipal policy is established, “it requires only one application ... to satisfy fully Monell’s requirement that a municipal corporation be held liable only for constitutional violations resulting from the municipality’s official policy.” <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#822" aria-description="Citation for case: City of Oklahoma v. Tuttle"><em>Id., </em>at 822</a></span> (plurality opinion); see also, <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#831" aria-description="Citation for case: City of Oklahoma v. Tuttle"><em>id., </em>at 831-832</a></span> (Brennan, J., concurring in part and concurring in judgment.). The only issue before us, then, is whether petitioner satisfied Monell’s requirement that the tor-tious conduct be pursuant to “official municipal policy.”</p>
</footnote>
<footnote label="7">
<p id="b561-6"> This legislative history is discussed at length in <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>and need only be summarized here. The distinction between imposing liability on municipalities for their own violations and imposing liability to force municipalities to prevent violations by others was made by Members of the House of Representatives who successfully opposed the “Sherman amendment” to the Civil Rights Act of 1871, <span class="citation no-link">17 Stat. 13</span>, the precursor of § 1983. The Sherman amendment sought to impose civil liability on municipalities for damage done to the person or property of its inhabitants by private persons “riotously and tumultuously assembled.” Cong. Globe, 42d Cong., 1st Sess., 749 (1871) (quoted in <em>Monell, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#664" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 664</a></span>). Opponents of the amendment argued that, in effect, it imposed an obligation on local governments to keep the peace, and that the Federal Government could not constitutionally require local governments to keep the peace if state law did not. This argument succeeded in blocking passage of the amendment. However, even the opponents of the Sherman amendment recognized Congress’ power to impose civil liability on a local government already obligated to keep the peace by state law if that government failed to do so and thereby violated the Fourteenth Amendment. See <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#665" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs."><em>id., </em>at 665-683</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b562-7"> Thus, our statement of the conclusion juxtaposes the policy requirement with imposing liability on the basis of <em>respondeat superior:</em></p>
<blockquote id="b562-8">“We conclude, therefore, that a local government may not be sued under § 1983 for an injury inflicted solely by its employees or agents. Instead, it is when execution of a government’s policy. . . , whether made by its lawmakers or by those whose edicts or acts may fairly be said to represent official policy, inflicts the injury that the government as an entity is responsible under § 1983.” <em>Id., </em>at 694.</blockquote>
</footnote>
<footnote label="9">
<p id="b563-7"> While the dictionary is not the source definitively to resolve legal questions, we note that this description of “policy” is consistent with the word’s ordinary definition. For example, Webster’s defines the word as “a specific decision or set of decisions designed to carry out such a chosen course of action.” Webster’s Third New International Dictionary 1754 (1981). Similarly, the Oxford English Dictionary defines “policy” as “[a] course of action adopted and pursued by a government, party, ruler, statesman, etc.; any course of action adopted as advantageous or expedient.” VII Oxford English Dictionary 1071 (1933). See also, Webster’s New Twentieth Century Dictionary 1392 (2d ed. 1979) (“any governing principle, plan, or course of action”); Random House Dictionary 1113 (1966) (“a course of action adopted and pursued by a government, ruler, political party, etc.”).</p>
</footnote>
<footnote label="10">
<p id="b563-8"> Section 1983 also refers to deprivations under color of a state “custom or usage,” and the Court in <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>noted accordingly that “local govern<page-number citation-index="1" label="482">*482</page-number>ments, like every other § 1983 ‘person,’. . . may be sued for constitutional deprivations visited pursuant to governmental ‘custom’ even though such a custom has not received formal approval through the body’s official deci-sionmaking channels.” <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#690" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 690-691</a></span>. A § 1983 plaintiff thus may be able to recover from a municipality without adducing evidence of an affirmative decision by policymakers if able to prove that the challenged action was pursuant to a state “custom or usage.” Because there is no allegation that the action challenged here was pursuant to a local “custom,” this aspect of <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>is not at issue in this case.</p>
</footnote>
<footnote label="11">
<p id="b564-6"> Respondent argues that the holding in <em><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">Tuttle</a></span> </em>is far broader than this. It relies on the statement near the end of Justice Rehnquist’s plurality opinion that “[p]roof of a single incident of unconstitutional activity is not sufficient to impose liability under <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>unless proof of the incident includes proof that it was caused by an <em>existing, </em>unconstitutional municipal policy, which policy can be attributed to a municipal policymaker.” <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#823" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S., at 823-824</a></span> (emphasis added). Respondent contends that a policy cannot be said to be “existing” unless similar action has been taken in the past.</p>
<p id="b564-7">This reading of the <em><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">Tuttle</a></span> </em>plurality is strained, and places far too much weight on a single word. The plaintiff in <em><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">Tuttle</a></span> </em>alleged that a police officer’s use of excessive force deprived her decedent of life without due process of law. The plaintiff proved only a single instance of unconstitutional action by a nonpolieymaking employee of the city. She argued that the city had “caused” the constitutional deprivation by adopting a “policy” of inadequate training. The trial judge instructed the jury that a single, unusually excessive use of force may warrant an inference that it was attributable to grossly inadequate training, and that the municipality could be held liable on this basis. We reversed the judgment against the city. Although there was no opinion for the Court on this question, both the plurality and the opinion concurring in the judgment found plaintiff’s submission inadequate because she failed to establish that the unconstitutional act was taken <em>pursuant to </em>a municipal policy rather than simply resulting from such a policy in a “but for” sense. <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#822" aria-description="Citation for case: City of Oklahoma v. Tuttle"><em>Id., </em>at 822-824</a></span> (plurality opinion), 829-830 (Brennan, J., concurring in part and concurring in judgment). That conclusion is entirely consistent with our holding today that the policy which ordered or authorized an unconstitutional act can be established by a single decision by proper municipal policymakers.'</p>
</footnote>
<footnote label="12">
<p id="b565-5"> Thus, for example, the County Sheriff may have discretion to hire and fire employees without also being the county official responsible for establishing county employment policy. If this were the case, the Sheriff’s decisions respecting employment would not give rise to municipal liability, although similar decisions with respect to law enforcement practices, over which the Sheriff <em>is </em>the official policymaker, <em>would </em>give rise to municipal liability. Instead, if county employment policy was set by the Board of County Commissioners, only that body’s decisions would provide a basis for county liability. This would be true even if the Board left the Sheriff discretion to hire and fire employees and the Sheriff exercised that discretion in an unconstitutional manner; the decision to act unlawfully would not be a decision of the Board. However, if the Board delegated its power to establish final employment policy to the Sheriff, the Sheriff’s decisions <em>would </em>represent county policy and could give rise to municipal liability.</p>
</footnote>
<footnote label="13">
<p id="b566-9"> We generally accord great deference to the interpretation and application of state law by the courts of appeals. <em>United States </em>v. <em>S.A. Empresa de Viacao Aerea Rio Grandense, </em><span class="citation" data-id="111219"><a href="/opinion/111219/united-states-v-sa-empresa-de-viacao-aerea-rio-grandense/#815" aria-description="Citation for case: United States v. S.A. Empresa De Viacao Aerea Rio Grandense">467 U. S. 797, 815, n. 12</a></span> (1984); <em>Brockett </em><page-number citation-index="1" label="485">*485</page-number>v. <em>Spokane Arcades, Inc., </em><span class="citation" data-id="9430103"><a href="/opinion/111480/brockett-v-spokane-arcades-inc/#499" aria-description="Citation for case: Brockett v. Spokane Arcades, Inc.">472 U. S. 491, 499-500</a></span> (1985) (citing cases); see also <em>Bishop </em>v. <em>Wood, </em><span class="citation" data-id="9426440"><a href="/opinion/109476/bishop-v-wood/#345" aria-description="Citation for case: Bishop v. Wood">426 U. S. 341, 345-347</a></span> (1976).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Pennsylvania Board of Probation and Parole v. Scott.md  (`case`, 6 assertions)

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
{"assertion_id": "448c92a127ca3f88", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "524 U.S. 357 (1998)", "court": "U.S. Supreme Court", "neutral_cite": "1998 U.S. LEXIS 4037", "official_citation_present": true, "parallel_cite": "118 S. Ct. 2014; 141 L. Ed. 2d 344", "title": "Pennsylvania Board of Probation and Parole v. Scott", "year": "1998"}}
{"assertion_id": "02802c53809334c0", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The federal Fourth Amendment exclusionary rule does not bar the introduction at a parole-revocation hearing of evidence seized in violation of a parolee's Fourth Amendment rights.", "title": "Pennsylvania Board of Probation and Parole v. Scott"}}
{"assertion_id": "19790f6cc958faee", "dimension": "support", "kind": "home_role", "locator": {"home": "The Good-Faith Exception"}, "payload": {"home": "The Good-Faith Exception", "role": "Key — Limiting", "title": "Pennsylvania Board of Probation and Parole v. Scott"}}
{"assertion_id": "ce3f86386f359d49", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Related (cross-doctrine)", "title": "Pennsylvania Board of Probation and Parole v. Scott"}}
{"assertion_id": "6162fed4fe4d0716", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1998-06-22", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Pennsylvania Board of Probation and Parole v. Scott", "field_i_validity": "good_law", "scope_note": "The federal exclusionary rule does not apply at parole-revocation hearings; good law.", "title": "Pennsylvania Board of Probation and Parole v. Scott", "varies_by_point": "false"}}
{"assertion_id": "afa27cb3f0311738", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Pennsylvania Board of Probation and Parole v. Scott"}}
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

## GROUP: content/cases/Pennsylvania v. Bruder.md  (`case`, 5 assertions)

### content_page

```
---
title: "Pennsylvania v. Bruder"
type: case
citation: "488 U.S. 9 (1988)"
parallel_cite: "109 S. Ct. 205; 102 L. Ed. 2d 172"
neutral_cite: 1988 U.S. LEXIS 4816
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1988
date_decided: 1988-10-31
docket: 88-161
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1988-10-31
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Pennsylvania v. Bruder
  varies_by_point: false
  scope_note: "Good law; per curiam application of Berkemer v. McCarty — ordinary traffic stops are non-custodial, so roadside DUI questioning needs no Miranda warnings before arrest."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112152/pennsylvania-v-bruder/"
  cluster_id: 112152
  opinion_id: 112152
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Related (custody)"
related: ["[[Berkemer v. McCarty]]", "[[Miranda v. Arizona]]", "[[California v. Beheler]]", "[[Oregon v. Mathiason]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "custody", "traffic-stop", "dui", "per-curiam"]
holding: "Ordinary roadside questioning of a motorist detained during a routine traffic stop — including DUI field-sobriety questioning before arrest — is not custodial interrogation, so Miranda warnings are not required and the roadside responses are admissible (applying Berkemer v. McCarty)."
lake:
  record_id: Pennsylvania v. Bruder
  status: verified
  projected_at: 2026-07-06
---

# Pennsylvania v. Bruder

*488 U.S. 9 (1988)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officer Shallis observed Bruder driving erratically and running a red light, and stopped him. Smelling alcohol and seeing Bruder's stumbling movements, the officer administered field sobriety tests and asked whether he had been drinking; Bruder admitted he had and recited the alphabet. He was then arrested for driving under the influence. The Pennsylvania Superior Court held that his roadside statements were the product of un-warned custodial interrogation and suppressed them for lack of [[Miranda and Custodial Interrogation|Miranda warnings]].

## Issue
Whether roadside questioning of a motorist during an ordinary traffic stop — here, DUI sobriety questioning before arrest — is custodial interrogation requiring [[Miranda and Custodial Interrogation|Miranda warnings]].

## Rule
No. The decision was "contrary to [[Berkemer v. McCarty]]," which held that the "'noncoercive aspect of ordinary traffic stops prompts us to hold that persons temporarily detained pursuant to such stops are not "in custody" for the purposes of *Miranda*.'" — 488 U.S. at 10 (quoting *Berkemer*, 468 U.S. 420, 440 (1984)). Because such a motorist's freedom is not curtailed "to a degree associated with formal arrest," "he was not entitled to a recitation of his constitutional rights prior to arrest, and his roadside responses to questioning were admissible." — *Id.* ^pin-10

"*Berkemer*'s rule, that ordinary traffic stops do not involve custody for purposes of *Miranda*, governs this case." — *Id.* at 11. ^pin-11

## Application
The uncontested facts showed "the same noncoercive aspects as the *Berkemer* detention: 'a single police officer ask[ing] respondent a modest number of questions and request[ing] him to perform a simple balancing test at a location visible to passing motorists.'" Because the stop was the ordinary, brief, public sort that *[[Berkemer v. McCarty|Berkemer]]* deemed non-custodial, Bruder was not "in custody" during the roadside questioning and no [[Miranda and Custodial Interrogation|Miranda warnings]] were required; his roadside statements were therefore admissible.

## Conclusion
Ordinary traffic stops are non-custodial for Miranda purposes; Bruder's pre-arrest roadside statements were admissible. The judgment of the Pennsylvania Superior Court was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- No negative treatment. *Bruder* is a straightforward application of [[Berkemer v. McCarty]] in the [[Miranda v. Arizona]] custody line; it relies on the "degree associated with formal arrest" custody standard from [[California v. Beheler]] and the station-house analog of [[Oregon v. Mathiason]]. (Custody can still arise if a stop escalates beyond the ordinary; *Bruder* addresses only the routine roadside encounter.)

## Appears on
- [[Miranda and Custodial Interrogation]] — *Related (custody)*

## Sources
- *Pennsylvania v. Bruder*, 488 U.S. 9 (1988) (per curiam) — https://www.courtlistener.com/opinion/112152/pennsylvania-v-bruder/ — pinpoints: 10, 11.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "fe97ae94d0100937", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "488 U.S. 9 (1988)", "court": "U.S. Supreme Court", "neutral_cite": "1988 U.S. LEXIS 4816", "official_citation_present": true, "parallel_cite": "109 S. Ct. 205; 102 L. Ed. 2d 172", "title": "Pennsylvania v. Bruder", "year": "1988"}}
{"assertion_id": "6bf479f33bd77cdc", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Ordinary roadside questioning of a motorist detained during a routine traffic stop — including DUI field-sobriety questioning before arrest — is not custodial interrogation, so Miranda warnings are not required and the roadside responses are admissible (applying Berkemer v. McCarty).", "title": "Pennsylvania v. Bruder"}}
{"assertion_id": "a1e1d618ec405694", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Related (custody)", "title": "Pennsylvania v. Bruder"}}
{"assertion_id": "a71f4ee99031cde3", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1988-10-31", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Pennsylvania v. Bruder", "field_i_validity": "good_law", "scope_note": "Good law; per curiam application of Berkemer v. McCarty — ordinary traffic stops are non-custodial, so roadside DUI questioning needs no Miranda warnings before arrest.", "title": "Pennsylvania v. Bruder", "varies_by_point": "false"}}
{"assertion_id": "f3fe3823f57c6887", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Pennsylvania v. Bruder"}}
```

### lake record — Pennsylvania v. Bruder

```json
{
  "schema_version": "s2.v1",
  "record_id": "Pennsylvania v. Bruder",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Pennsylvania v. Bruder",
    "case_name_short": "Bruder",
    "case_name_full": "Pennsylvania v. Bruder",
    "input_case_name": "Pennsylvania v. Bruder",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1988-10-31",
    "year": 1988,
    "docket": "88-161",
    "cluster_id": 112152,
    "lead_opinion_id": 112152,
    "sibling_ids": [
      112152,
      9431478,
      9431479,
      9431480
    ],
    "absolute_url": "/opinion/112152/pennsylvania-v-bruder/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "488 U.S. 9",
      "volume": "488",
      "reporter": "U.S.",
      "page": "9",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 205",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "205",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 L. Ed. 2d 172",
        "volume": "102",
        "reporter": "L. Ed. 2d",
        "page": "172",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1988 U.S. LEXIS 4816",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "4816",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "488 U.S. 9",
        "volume": "488",
        "reporter": "U.S.",
        "page": "9",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 205",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "205",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 L. Ed. 2d 172",
        "volume": "102",
        "reporter": "L. Ed. 2d",
        "page": "172",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 U.S. LEXIS 4816",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "4816",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "488 U.S. 9",
    "official_selection": {
      "court_class": "scotus",
      "selected": "488 U.S. 9",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-10",
      "page": null,
      "quote": "--- # Pennsylvania v. Bruder *488 U.S. 9 (1988)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officer Shallis observed Bruder driving erratically and running a red light, and stopped him. Smelling alcohol and seeing Bruder's stumbling movements, the officer administered field sobriety tests and asked whether he had been drinking; Bruder admitted he had and recited the alphabet. He was then arrested for driving under the influence. The Pennsylvania Superior Court held that his roadside statements were the product of un-warned custodial interrogation and suppressed them for lack of Miranda warnings. ## Issue Whether roadside questioning of a motorist during an ordinary traffic stop \u2014 here, DUI sobriety questioning before arrest \u2014 is custodial interrogation requiring Miranda warnings. ## Rule No. The decision was",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-11",
      "page": null,
      "quote": "*Berkemer*'s rule, that ordinary traffic stops do not involve custody for purposes of *Miranda*, governs this case.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1988-10-31",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Pennsylvania v. Bruder",
    "varies_by_point": false,
    "scope_note": "Good law; per curiam application of Berkemer v. McCarty \u2014 ordinary traffic stops are non-custodial, so roadside DUI questioning needs no Miranda warnings before arrest.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Tantillo",
          "cluster_id": 9413972,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Earl",
          "cluster_id": 9404588,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri v. Harvey D. Harris",
          "cluster_id": 4650068,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Cawthron",
          "cluster_id": 4500714,
          "cite": [
            "97 N.E.3d 671",
            "479 Mass. 612"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane1_negative"
      },
      {
        "citing_case": {
          "name": "National Ass'n of Telecommunications Officers & Advisors v. Federal Communications Commission",
          "cluster_id": 4407120,
          "cite": [
            "862 F.3d 18",
            "2017 WL 2883738",
            "2017 U.S. App. LEXIS 12139"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Becla",
          "cluster_id": 6589084,
          "cite": [
            "74 Mass. App. Ct. 142",
            "904 N.E.2d 783",
            "2009 Mass. App. LEXIS 436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Smith v. Ohio",
          "cluster_id": 112392,
          "cite": [
            "108 L. Ed. 2d 464",
            "110 S. Ct. 1288",
            "494 U.S. 541",
            "1990 U.S. LEXIS 1198"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hildwin v. Florida",
          "cluster_id": 112269,
          "cite": [
            "104 L. Ed. 2d 728",
            "109 S. Ct. 2055",
            "490 U.S. 638",
            "1989 U.S. LEXIS 2698"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane1_negative"
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
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson v. Keohane",
          "cluster_id": 117982,
          "cite": [
            "133 L. Ed. 2d 383",
            "116 S. Ct. 457",
            "516 U.S. 99",
            "1995 U.S. LEXIS 8315",
            "95 Cal. Daily Op. Serv. 8968"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Muniz",
          "cluster_id": 112464,
          "cite": [
            "110 L. Ed. 2d 528",
            "110 S. Ct. 2638",
            "496 U.S. 582",
            "1990 U.S. LEXIS 3211"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Ortiz, Octavio",
          "cluster_id": 2945879,
          "cite": [
            "382 S.W.3d 367",
            "2012 Tex. Crim. App. LEXIS 1386",
            "2012 WL 5348503"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Carlson",
          "cluster_id": 1219515,
          "cite": [
            "808 P.2d 1002",
            "311 Or. 201",
            "1991 Ore. LEXIS 22"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Mannion",
          "cluster_id": 1486747,
          "cite": [
            "725 A.2d 196",
            "1999 Pa. Super. 25",
            "1999 Pa. Super. LEXIS 58"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Easler",
          "cluster_id": 1421141,
          "cite": [
            "489 S.E.2d 617",
            "327 S.C. 121",
            "1997 S.C. LEXIS 146"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCambridge v. State",
          "cluster_id": 2465567,
          "cite": [
            "778 S.W.2d 70",
            "1989 WL 104638"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Fish",
          "cluster_id": 1392390,
          "cite": [
            "893 P.2d 1023",
            "321 Or. 48",
            "1995 Ore. LEXIS 30"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ah Loo",
          "cluster_id": 2632163,
          "cite": [
            "10 P.3d 728",
            "94 Haw. 207",
            "2000 Haw. LEXIS 322"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Timothy E. Dobbs",
          "cluster_id": 4765836,
          "cite": [
            "945 N.W.2d 609",
            "392 Wis. 2d 505",
            "2020 WI 64"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Turner",
          "cluster_id": 2286044,
          "cite": [
            "772 A.2d 970",
            "2001 Pa. Super. 79",
            "2001 Pa. Super. LEXIS 275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mary E. Martinez, A/K/A Esperanza Lozada and Clara J. Araujo",
          "cluster_id": 597896,
          "cite": [
            "983 F.2d 968",
            "37 Fed. R. Serv. 968",
            "1992 U.S. App. LEXIS 33785",
            "1992 WL 387386"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Fritschen",
          "cluster_id": 1351455,
          "cite": [
            "802 P.2d 558",
            "247 Kan. 592",
            "1990 Kan. LEXIS 190"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Leib",
          "cluster_id": 2177823,
          "cite": [
            "588 A.2d 922",
            "403 Pa. Super. 223",
            "1991 Pa. Super. LEXIS 383"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Wimbush",
          "cluster_id": 1926596,
          "cite": [
            "750 A.2d 807",
            "561 Pa. 368",
            "2000 Pa. LEXIS 918"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Wynne",
          "cluster_id": 606744,
          "cite": [
            "993 F.2d 760",
            "1993 U.S. App. LEXIS 11403",
            "1993 WL 158552"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Burton",
          "cluster_id": 1249245,
          "cite": [
            "651 N.W.2d 143",
            "252 Mich. App. 130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terrell v. Morris, Superintendent, Southern Ohio Correctional Facility",
          "cluster_id": 112335,
          "cite": [
            "107 L. Ed. 2d 1",
            "110 S. Ct. 4",
            "493 U.S. 1",
            "1989 U.S. LEXIS 4756",
            "58 U.S.L.W. 3236"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hasenflue",
          "cluster_id": 6162310,
          "cite": [
            "252 A.D.2d 829",
            "675 N.Y.S.2d 464",
            "1998 N.Y. App. Div. LEXIS 8593"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112152 OR 9431478 OR 9431479 OR 9431480) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 97,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 8,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 97,
        "triage_read": 8,
        "triage_snippet_classified": 89
      },
      "lane2_top_cited": {
        "query": "cites:(112152 OR 9431478 OR 9431479 OR 9431480)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOCZzPTEzNjYzMDMmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112152+OR+9431478+OR+9431479+OR+9431480%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 22,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112152 OR 9431478 OR 9431479 OR 9431480)",
        "reviewed": 2,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 2,
        "triage_read": 1,
        "triage_snippet_classified": 1
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112152 OR 9431478 OR 9431479 OR 9431480)",
    "indexed_citing_opinions": 125,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112152,
        "count": 105,
        "count_source": "search"
      },
      {
        "opinion_id": 9431478,
        "count": 22,
        "count_source": "search"
      },
      {
        "opinion_id": 9431479,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431480,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 190,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/pennsylvania-v-bruder.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQwMDE1MDgmcz0zMDc4NDczJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112152+OR+9431478+OR+9431479+OR+9431480%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112152,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 110593,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 111022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 111023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 111157,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 111962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 112024,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 1981202,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 2169088,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 2258133,
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
    "date_created": "2026-07-05T16:50:48Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:50:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:50:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:54:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:50:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Pennsylvania v. Bruder

```
<div>
<center><b><span class="citation" data-id="9431478"><a href="/opinion/112152/pennsylvania-v-bruder/" aria-description="Citation for case: Pennsylvania v. Bruder">488 U.S. 9</a></span> (1988)</b></center>
<center><h1>PENNSYLVANIA<br>
v.<br>
BRUDER</h1></center>
<center>No. 88-161.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Decided October 31, 1988</center>
ON PETITION FOR WRIT OF CERTIORARI TO THE SUPERIOR COURT OF PENNSYLVANIA
<p>PER CURIAM.</p>
<p>Because the decision of the Pennsylvania Superior Court in this case is contrary to <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420</a></span> (1984), we grant the petition for a writ of certiorari and reverse.</p>
<p>In the early morning of January 19, 1985, Officer Steve Shallis of the Newton Township, Pennsylvania, Police Department observed respondent Thomas Bruder driving very erratically along State Highway 252. Among other traffic violations, he ignored a red light. Shallis stopped Bruder's vehicle. Bruder left his vehicle, approached Shallis, and when asked for his registration card, returned to his car to obtain it. Smelling alcohol and observing Bruder's stumbling movements, Shallis administered field sobriety tests, <span class="star-pagination">*10</span> including asking Bruder to recite the alphabet. Shallis also inquired about alcohol. Bruder answered that he had been drinking and was returning home. Bruder failed the sobriety tests, whereupon Shallis arrested him, placed him in the police car, and gave him <i>Miranda</i> warnings. Bruder was later convicted of driving under the influence of alcohol. At his trial, his statements and conduct prior to his arrest were admitted into evidence. On appeal, the Pennsylvania Superior Court reversed, <span class="citation" data-id="9746375"><a href="/opinion/2258133/commonwealth-v-bruder/" aria-description="Citation for case: Commonwealth v. Bruder">365 Pa. Super. 106</a></span>, <span class="citation" data-id="9746375"><a href="/opinion/2258133/commonwealth-v-bruder/" aria-description="Citation for case: Commonwealth v. Bruder">528 A. 2d 1385</a></span> (1987), on the ground that the above statements Bruder had uttered during the roadside questioning were elicited through custodial interrogation and should have been suppressed for lack of <i>Miranda</i> warnings. The Pennsylvania Supreme Court denied the State's appeal application.</p>
<p>In <i>Berkemer</i> v. <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">McCarty, supra</a></span></i><i>,</i> which involved facts strikingly similar to those in this case, the Court concluded that the "noncoercive aspect of ordinary traffic stops prompts us to hold that persons temporarily detained pursuant to such stops are not `in custody' for the purposes of <i>Miranda.</i>" <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#440" aria-description="Citation for case: Berkemer v. McCarty"><i>Id.,</i> at 440</a></span>. The Court reasoned that although the stop was unquestionably a seizure within the meaning of the Fourth Amendment, such traffic stops typically are brief, unlike a prolonged station house interrogation. Second, the Court emphasized that traffic stops commonly occur in the "public view," in an atmosphere far "less `police dominated' than that surrounding the kinds of interrogation at issue in <i>Miranda</i> itself." <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#438" aria-description="Citation for case: Berkemer v. McCarty"><i>Id.,</i> at 438-439</a></span>. The detained motorist's "freedom of action [was not] curtailed to `a degree associated with formal arrest.' " <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Id.,</a></span></i> at 440 (citing <i>California</i> v. <i>Beheler,</i> <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1125" aria-description="Citation for case: California v. Beheler">463 U. S. 1121, 1125</a></span> (1983)). Accordingly, he was not entitled to a recitation of his constitutional rights prior to arrest, and his roadside responses to questioning were admissible.<sup>[1]</sup></p>
<p><span class="star-pagination">*11</span> The facts in this record, which Bruder does not contest, reveal the same noncoercive aspects as the <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i> detention: "a single police officer ask[ing] respondent a modest number of questions and request[ing] him to perform a simple balancing test at a location visible to passing motorists." <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#442" aria-description="Citation for case: Berkemer v. McCarty">468 U. S., at 442</a></span> (footnote omitted).<sup>[2]</sup> Accordingly, <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i>'s rule, that ordinary traffic stops do not involve custody for purposes of <i>Miranda,</i> governs this case.<sup>[3]</sup> The judgment of the Pennsylvania Superior Court that evidence was inadmissible for lack of <i>Miranda</i> warnings is reversed.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE MARSHALL, dissenting.</p>
<p>I agree with JUSTICE STEVENS that the Court should not disturb the decision of the court below, and accordingly I join his dissent. I write separately to note my continuing belief that it is unfair to litigants and damaging to the integrity and accuracy of this Court's decisions to reverse a decision summarily without the benefit of full briefing on the merits of <span class="star-pagination">*12</span> the question decided. <i>Rhodes</i> v. <i>Stewart, ante,</i> p. 1 (MARSHALL, J., dissenting); <i>Buchanan</i> v. <i>Stanships, Inc.,</i> <span class="citation" data-id="9431231"><a href="/opinion/112024/buchanan-v-stanships-inc/#269" aria-description="Citation for case: Buchanan v. Stanships, Inc.">485 U. S. 265, 269</a></span> (1988) (MARSHALL, J., dissenting); <i>Commissioner</i> v. <i>McCoy,</i> <span class="citation" data-id="9431140"><a href="/opinion/111962/commissioner-v-mccoy/#7" aria-description="Citation for case: Commissioner v. McCoy">484 U. S. 3, 7</a></span> (1987) (MARSHALL, J., dissenting). I therefore dissent from the Court's decision today to reverse summarily the decision below.</p>
<p>JUSTICE STEVENS, with whom JUSTICE MARSHALL joins, dissenting.</p>
<p>The Court explains why it reverses the decision of the Superior Court of Pennsylvania in this drunken driving case, but it does not explain why it granted certiorari.</p>
<p>In <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#440" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 440-442</a></span> (1984), the Court concluded that <i>Miranda</i> warnings are not required during a traffic stop unless the citizen is taken into custody; that there is no bright-line rule for determining when detentions short of formal arrest constitute custody; and that "the only relevant inquiry is how a reasonable man in the suspect's position would have understood his situation," <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#442" aria-description="Citation for case: Berkemer v. McCarty">468 U. S., at 442</a></span>. The rule applied in Pennsylvania is strikingly similar to this Court's statement in <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span>.</i> As the Pennsylvania Superior Court explained in this case:</p>
<blockquote>"In Pennsylvania, `custodial interrogation does not require that police make a formal arrest, nor that the police intend to make an arrest. . . . Rather, the test of custodial interrogation is whether the individual being interrogated reasonably believes his freedom of action is being restricted.' <i>Commonwealth</i> v. <i>Meyer,</i> <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/#307" aria-description="Citation for case: Commonwealth v. Meyer">488 Pa. 297, 307</a></span>, <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/#521" aria-description="Citation for case: Commonwealth v. Meyer">412 A. 2d 517, 521</a></span> (1980) (quoting <i>Commonwealth</i> v. <i>Brown,</i> <span class="citation" data-id="2169088"><a href="/opinion/2169088/commonwealth-v-brown/#570" aria-description="Citation for case: Commonwealth v. Brown">473 Pa. 562, 570</a></span>, <span class="citation" data-id="2169088"><a href="/opinion/2169088/commonwealth-v-brown/#1264" aria-description="Citation for case: Commonwealth v. Brown">375 A. 2d 1260, 1264</a></span> (1977). . . .</blockquote>
<blockquote>"In <i>Commonwealth</i> v. <i><span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">Meyer</a></span></i><i>,</i> the Pennsylvania Supreme Court ruled that the driver of a car involved in an accident who was suspected of driving under the influence of alcohol and who was told by police to wait at the scene until additional police arrived was in custody for <span class="star-pagination">*13</span> purposes of <i>Miranda.</i> The <i><span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">Meyer</a></span></i> court reasoned that because the defendant had a reasonable belief that his freedom of action had been restricted, statements elicited before he received his <i>Miranda</i> warnings should have been suppressed. <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/#307" aria-description="Citation for case: Commonwealth v. Meyer">488 Pa. at 307</a></span>, <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/#522" aria-description="Citation for case: Commonwealth v. Meyer">412 A. 2d at 522</a></span>." <span class="citation" data-id="9746375"><a href="/opinion/2258133/commonwealth-v-bruder/#111" aria-description="Citation for case: Commonwealth v. Bruder">365 Pa. Super. 106, 111-112</a></span>, <span class="citation" data-id="9746375"><a href="/opinion/2258133/commonwealth-v-bruder/#1387" aria-description="Citation for case: Commonwealth v. Bruder">528 A. 2d 1385, 1387</a></span> (1987).</blockquote>
<p>In its <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i> opinion, this Court cited the Pennsylvania Supreme Court's opinion in <i>Commonwealth</i> v. <i>Meyer,</i> <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">488 Pa. 297</a></span>, <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">412 A. 2d 517</a></span> (1980), with approval. <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#441" aria-description="Citation for case: Berkemer v. McCarty">468 U. S., at 441, n. 34</a></span>. Thus, there appears to be no significant difference between the rule of law that is generally applied to traffic stops in Pennsylvania and the rule that this Court would approve in other States.</p>
<p>There is, however, a difference of opinion on the question whether the rule was correctly applied in this case. The Superior Court of Pennsylvania was divided on the issue. See 365 Pa. Super., at 117, <span class="citation" data-id="9746375"><a href="/opinion/2258133/commonwealth-v-bruder/#1390" aria-description="Citation for case: Commonwealth v. Bruder">528 A. 2d, at 1390</a></span> (Rowley, J., concurring and dissenting). It was therefore quite appropriate for the prosecutor to seek review in the Supreme Court of Pennsylvania. That court summarily denied review without opinion. See <span class="citation no-link">518 Pa. 635</span>, <span class="citation no-link">542 A. 2d 1365</span> (1988). That action was quite appropriate for the highest court of a large State like Pennsylvania because such a court is obviously much too busy to review every arguable misapplication of settled law in cases of this kind.</p>
<p>For reasons that are unclear to me, however, this Court seems to welcome the opportunity to perform an error-correcting function in cases that do not merit the attention of the highest court of a sovereign State. See, <i>e. g., </i><i>Florida</i> v. <i>Meyers,</i> <span class="citation" data-id="9429577"><a href="/opinion/111157/florida-v-meyers/" aria-description="Citation for case: Florida v. Meyers">466 U. S. 380</a></span> (1984) <i>(per curiam)</i><i>; </i><i>Illinois</i> v. <i>Batchelder,</i> <span class="citation" data-id="9429372"><a href="/opinion/111022/illinois-v-batchelder/" aria-description="Citation for case: Illinois v. Batchelder">463 U. S. 1112</a></span> (1983) <i>(per curiam)</i><i>.</i> Although there are cases in which "there are special and important reasons" for correcting an error that is committed by another court, see this Court's Rule 17.1, this surely is not such a case. The Court does not suggest that this case involves an <span class="star-pagination">*14</span> important and unsettled question of federal law or that there is confusion among the state and federal courts concerning what legal rules govern the application of <i>Miranda</i> to ordinary traffic stops. Rather, the Court simply holds that the Superior Court of Pennsylvania misapplied our decision in <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i> to "[t]he facts in this record." <i>Ante,</i> at 11. In my judgment this Court's scarce resources would be far better spent addressing cases that are of some general importance "beyond the facts and parties involved," <i>Boag</i> v. <i>MacDougall,</i> <span class="citation" data-id="9428558"><a href="/opinion/110593/boag-v-macdougall/#368" aria-description="Citation for case: Boag v. MacDougall">454 U. S. 364, 368</a></span> (1982) (REHNQUIST, J., dissenting), than in our acting as "self-appointed . . . supervisors of the administration of justice in the state judicial systems," <i>Florida</i> v. <i>Meyers,</i> <span class="citation" data-id="9429577"><a href="/opinion/111157/florida-v-meyers/#385" aria-description="Citation for case: Florida v. Meyers">466 U. S., at 385</a></span> (STEVENS, J., dissenting).</p>
<p>Accordingly, because I would not disturb the decision of the Supreme Court of Pennsylvania  which, incidentally, is the court to which the petitioner asks us to direct the writ of certiorari  I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[1]  We did not announce an absolute rule for all motorist detentions, observing that lower courts must be vigilant that police do not "delay formally arresting detained motorists, and . . . subject them to sustained and intimidating interrogation at the scene of their initial detention." <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#440" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 440</a></span> (1984).</p>
<p>[2]  Reliance on the Pennsylvania Supreme Court's decision in <i>Commonwealth</i> v. <i>Meyer,</i> <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">488 Pa. 297</a></span>, <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">412 A. 2d 517</a></span> (1980), to which we referred in <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span>,</i> see <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#441" aria-description="Citation for case: Berkemer v. McCarty">468 U. S., at 441</a></span>, and n. 34, is inapposite. <i><span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">Meyer</a></span></i> involved facts which we implied might properly remove its result from <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i>'s application to ordinary traffic stops; specifically, the motorist in <i><span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">Meyer</a></span></i> could be found to have been placed in custody for purposes of <i>Miranda</i> safeguards because he was detained for over half an hour, and subjected to questioning while in the patrol car. Thus, we acknowledged <i><span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">Meyer</a></span></i>'s relevance to the unusual traffic stop that involves prolonged detention. We expressly disapproved, however, the attempt to extrapolate from this sensitivity to uncommon detention circumstances any general proposition that custody exists whenever motorists think that their freedom of action has been restricted, for such a rationale would eviscerate <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i> altogether. See <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#436" aria-description="Citation for case: Berkemer v. McCarty"><i>Berkemer, supra,</i> at 436-437</a></span>.</p>
<p>[3]  We thus do not reach the issue whether recitation of the alphabet in response to custodial questioning is testimonial and hence inadmissible under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966).</p>

</div>
```

---

## GROUP: content/cases/Pennsylvania v. Labron.md  (`case`, 5 assertions)

### content_page

```
---
title: "Pennsylvania v. Labron"
type: case
citation: "518 U.S. 938 (1996)"
parallel_cite: "116 S. Ct. 2485; 135 L. Ed. 2d 1031"
neutral_cite: 1996 U.S. LEXIS 4268
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1996
date_decided: 1996-07-01
docket: 95-1691
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1996-07-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Pennsylvania v. Labron
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118063/pennsylvania-v-labron/"
  cluster_id: 118063
  opinion_id: 118063
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[Carroll v. United States]]", "[[California v. Carney]]", "[[Chambers v. Maroney]]"]
aliases: ["Pennsylvania v. Kilgore"]
tags: ["case", "fourth-amendment", "automobile-exception", "ready-mobility", "per-curiam"]
holding: "No separate exigency requirement beyond ready mobility: if a car is readily mobile and PC exists to believe it contains contraband, the…"
lake:
  record_id: Pennsylvania v. Labron
  status: verified
  projected_at: 2026-07-09
---

# Pennsylvania v. Labron

*518 U.S. 938 (1996)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In two consolidated cases, the Supreme Court of Pennsylvania suppressed evidence on the theory that the automobile exception requires both probable cause *and* separate [[Exigent Circumstances and Hot Pursuit|exigent circumstances]]. In *Labron*, police watched Labron conduct street drug transactions in Philadelphia, arrested the suspects, searched the trunk of the car from which the drugs had been produced, and found cocaine. (In the companion *Kilgore* case, police searched a pickup truck after a controlled buy.)

## Issue
Whether the automobile exception requires a separate showing of [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] beyond the vehicle's ready mobility and probable cause to believe it contains contraband.

## Rule
No separate [[Exigent Circumstances and Hot Pursuit|exigency]] is required. "If a car is readily mobile and probable cause exists to believe it contains contraband, the Fourth Amendment thus permits police to search the vehicle without more." — 518 U.S. at 940. ^pin-940

A vehicle's "ready mobility" is itself "an exigency sufficient to excuse failure to obtain a search warrant once probable cause to conduct the search is clear." — [*Id.*](https://www.courtlistener.com/opinion/118063/pennsylvania-v-labron/#:~:text=ready%20mobility) ^pin-940a

## Application
Police had seen Labron place drugs in the trunk of the car they searched — supplying probable cause — and the car was readily mobile. Because ready mobility plus probable cause is all the automobile exception requires, the warrantless search of the trunk did not violate the Fourth Amendment, and the Pennsylvania Supreme Court's contrary rule (demanding separate [[Exigent Circumstances and Hot Pursuit|exigent circumstances]]) rested on an incorrect reading of the exception.

## Conclusion
The automobile exception requires only ready mobility and probable cause, not a separate [[Exigent Circumstances and Hot Pursuit|exigency]]; the Pennsylvania judgments were reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Labron* confirms the "ready-mobility" rationale traced from [[Carroll v. United States]] through [[California v. Carney]].

## Appears on
- [[Automobile Exception]] — *Key — Progeny / Refinement*

## Sources
- *Pennsylvania v. Labron*, 518 U.S. 938 (1996) (per curiam) — https://www.courtlistener.com/opinion/118063/pennsylvania-v-labron/ — pinpoint: 940.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "61cc1119362e93df", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "518 U.S. 938 (1996)", "court": "U.S. Supreme Court", "neutral_cite": "1996 U.S. LEXIS 4268", "official_citation_present": true, "parallel_cite": "116 S. Ct. 2485; 135 L. Ed. 2d 1031", "title": "Pennsylvania v. Labron", "year": "1996"}}
{"assertion_id": "3b7d492667a39e42", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "No separate exigency requirement beyond ready mobility: if a car is readily mobile and PC exists to believe it contains contraband, the…", "title": "Pennsylvania v. Labron"}}
{"assertion_id": "53a626854c1551c9", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Key — Progeny / Refinement", "title": "Pennsylvania v. Labron"}}
{"assertion_id": "4e829b3fc76a9f87", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1996-07-01", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Pennsylvania v. Labron", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Pennsylvania v. Labron", "varies_by_point": "false"}}
{"assertion_id": "e3a803efdfd4e08c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Pennsylvania v. Labron"}}
```

### lake record — Pennsylvania v. Labron

```json
{
  "schema_version": "s2.v1",
  "record_id": "Pennsylvania v. Labron",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Pennsylvania v. Labron",
    "case_name_short": "Labron",
    "case_name_full": "Pennsylvania v. Labron",
    "input_case_name": "Pennsylvania v. Labron",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1996-07-01",
    "year": 1996,
    "docket": "95-1691",
    "cluster_id": 118063,
    "lead_opinion_id": 118063,
    "sibling_ids": [
      118063,
      9433386,
      9433387
    ],
    "absolute_url": "/opinion/118063/pennsylvania-v-labron/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "518 U.S. 938",
      "volume": "518",
      "reporter": "U.S.",
      "page": "938",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "116 S. Ct. 2485",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "2485",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 L. Ed. 2d 1031",
        "volume": "135",
        "reporter": "L. Ed. 2d",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1996 U.S. LEXIS 4268",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "4268",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "518 U.S. 938",
        "volume": "518",
        "reporter": "U.S.",
        "page": "938",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "116 S. Ct. 2485",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "2485",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 L. Ed. 2d 1031",
        "volume": "135",
        "reporter": "L. Ed. 2d",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1996 U.S. LEXIS 4268",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "4268",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "518 U.S. 938",
    "official_selection": {
      "court_class": "scotus",
      "selected": "518 U.S. 938",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-940",
      "page": null,
      "quote": "--- # Pennsylvania v. Labron *518 U.S. 938 (1996)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In two consolidated cases, the Supreme Court of Pennsylvania suppressed evidence on the theory that the automobile exception requires both probable cause *and* separate exigent circumstances. In *Labron*, police watched Labron conduct street drug transactions in Philadelphia, arrested the suspects, searched the trunk of the car from which the drugs had been produced, and found cocaine. (In the companion *Kilgore* case, police searched a pickup truck after a controlled buy.) ## Issue Whether the automobile exception requires a separate showing of exigent circumstances beyond the vehicle's ready mobility and probable cause to believe it contains contraband. ## Rule No separate exigency is required.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-940a",
      "page": null,
      "quote": "ready mobility",
      "star_marker": "940",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 6615,
      "fragment": "#:~:text=ready%20mobility",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1996-07-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Pennsylvania v. Labron",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Knight",
          "cluster_id": 4499332,
          "cite": [
            "419 P.3d 637",
            "55 Kan. App. 2d 642"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rickey Beene",
          "cluster_id": 3183556,
          "cite": [
            "818 F.3d 157",
            "2016 U.S. App. LEXIS 4331",
            "2016 WL 890127"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bernard West v. United States",
          "cluster_id": 2735560,
          "cite": [
            "100 A.3d 1076",
            "2014 D.C. App. LEXIS 382",
            "2014 WL 4636023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Meekins v. State",
          "cluster_id": 2544137,
          "cite": [
            "340 S.W.3d 454",
            "2011 Tex. Crim. App. LEXIS 592",
            "2011 WL 1663151"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Black",
          "cluster_id": 1814285,
          "cite": [
            "987 So. 2d 1177",
            "2006 WL 2457818"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Tyrone Werts v. Donald T. Vaughn the District Attorney of the County of Philadelphia the Attorney General of the State of Pennsylvania",
          "cluster_id": 770608,
          "cite": [
            "228 F.3d 178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Dyson",
          "cluster_id": 2621047,
          "cite": [
            "144 L. Ed. 2d 442",
            "119 S. Ct. 2013",
            "527 U.S. 465",
            "1999 U.S. LEXIS 4200"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wayne Gaskin, AKA \"Atiba,\" and Al Castle",
          "cluster_id": 785776,
          "cite": [
            "364 F.3d 438",
            "2004 U.S. App. LEXIS 7440",
            "2004 WL 818734"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rocha",
          "cluster_id": 4345763,
          "cite": [
            "295 Neb. 716",
            "890 N.W.2d 178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Allen",
          "cluster_id": 4673511,
          "cite": [
            "2019 CO 88"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Thompson",
          "cluster_id": 1836924,
          "cite": [
            "842 So. 2d 330",
            "2003 WL 1826561"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Powell",
          "cluster_id": 1736,
          "cite": [
            "175 L. Ed. 2d 1009",
            "130 S. Ct. 1195",
            "559 U.S. 50",
            "2010 U.S. LEXIS 1898"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin Davis (03-1451) and Keith Presley (03-1621)",
          "cluster_id": 792556,
          "cite": [
            "430 F.3d 345",
            "2005 U.S. App. LEXIS 25124",
            "2005 WL 3108503"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Keehn v. State",
          "cluster_id": 2341745,
          "cite": [
            "279 S.W.3d 330",
            "2009 Tex. Crim. App. LEXIS 425",
            "2009 WL 774854"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Maynard",
          "cluster_id": 152441,
          "cite": [
            "615 F.3d 544",
            "392 U.S. App. D.C. 291",
            "2010 U.S. App. LEXIS 16417",
            "2010 WL 3063788"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Guzman",
          "cluster_id": 1785574,
          "cite": [
            "959 S.W.2d 631",
            "1998 Tex. Crim. App. LEXIS 12",
            "1998 WL 28103"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. White",
          "cluster_id": 118287,
          "cite": [
            "143 L. Ed. 2d 748",
            "119 S. Ct. 1555",
            "526 U.S. 559",
            "1999 U.S. LEXIS 3172"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Brownlee",
          "cluster_id": 2106553,
          "cite": [
            "713 N.E.2d 556",
            "186 Ill. 2d 501",
            "239 Ill. Dec. 25",
            "1999 Ill. LEXIS 686"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marco Burton",
          "cluster_id": 777431,
          "cite": [
            "288 F.3d 91",
            "2002 U.S. App. LEXIS 7851",
            "2002 WL 753492"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Turner",
          "cluster_id": 4326929,
          "cite": [
            "2016 Ohio 7983"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cooke",
          "cluster_id": 2196499,
          "cite": [
            "751 A.2d 92",
            "163 N.J. 657",
            "2000 N.J. LEXIS 529"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dixon v. State",
          "cluster_id": 1400372,
          "cite": [
            "206 S.W.3d 613",
            "2006 Tex. Crim. App. LEXIS 1006",
            "2006 WL 1408451"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Myers v. State",
          "cluster_id": 852726,
          "cite": [
            "839 N.E.2d 1146",
            "2005 Ind. LEXIS 1135",
            "2005 WL 3484607"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118063 OR 9433386 OR 9433387) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTMzOTEzNjAwMDAwJnM9MjU2NzQzMCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118063+OR+9433386+OR+9433387%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(118063 OR 9433386 OR 9433387)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04MSZzPTc3ODkxMiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118063+OR+9433386+OR+9433387%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118063 OR 9433386 OR 9433387)",
        "reviewed": 23,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 23,
        "triage_read": 0,
        "triage_snippet_classified": 23
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118063 OR 9433386 OR 9433387)",
    "indexed_citing_opinions": 389,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118063,
        "count": 330,
        "count_source": "search"
      },
      {
        "opinion_id": 9433386,
        "count": 64,
        "count_source": "search"
      },
      {
        "opinion_id": 9433387,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 669,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/pennsylvania-v-labron.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg0Njk5OTYmcz05NDMwNzA2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118063+OR+9433386+OR+9433387%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118063,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 111430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 111625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 111872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 111928,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 112175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 112205,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 112464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 112475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 117905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 1473518,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 1752565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 1983319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 1984308,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 2073495,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 2089408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 2089468,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 2100000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 2165222,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 2316698,
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
    "date_created": "2026-07-05T16:54:56Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:55:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:55:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:58:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:55:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Pennsylvania v. Labron

```
<div>
<center><b><span class="citation" data-id="9433386"><a href="/opinion/118063/pennsylvania-v-labron/" aria-description="Citation for case: Pennsylvania v. Labron">518 U.S. 938</a></span> (1996)</b></center>
<center><h1>PENNSYLVANIA<br>
v.<br>
LABRON</h1></center>
<center>No. 95-1691.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Decided July 1, 1996.<sup>[*]</sup></center>
ON PETITION FOR WRIT OF CERTIORARI TO THE SUPREME COURT OF PENNSYLVANIA
<p>Per Curiam.</p>
<p>In these two cases, the Supreme Court of Pennsylvania held that the Fourth Amendment, as applied to the States through the Fourteenth, requires police to obtain a warrant <span class="star-pagination">*939</span> before searching an automobile unless exigent circumstances are present. Because the holdings rest on an incorrect reading of the automobile exception to the Fourth Amendment's warrant requirement, we grant the petitions for certiorari and reverse.</p>
<p>In <i>Labron,</i> No. 95-1691, police observed respondent Labron and others engaging in a series of drug transactions on a street in Philadelphia. The police arrested the suspects, searched the trunk of a car from which the drugs had been produced, and found bags containing cocaine. The Pennsylvania Supreme Court agreed with the trial court (but not with the intermediate court of appeals, <span class="citation no-link">428 Pa. Super. 616</span>, <span class="citation no-link">626 A. 2d 646</span> (1993), whose judgment it reversed) that this evidence should be suppressed. <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/" aria-description="Citation for case: Commonwealth v. Labron">543 Pa. 86</a></span>, <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/" aria-description="Citation for case: Commonwealth v. Labron">669 A. 2d 917</a></span> (1995). After surveying our precedents on the automobile exception as well as some of its own decisions, the court "conclude[d] that this Commonwealth's jurisprudence of the automobile exception has long required both the existence of probable cause and the presence of exigent circumstances to justify a warrantless search." <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#100" aria-description="Citation for case: Commonwealth v. Labron"><i>Id.,</i> at 100</a></span>, <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#924" aria-description="Citation for case: Commonwealth v. Labron">669 A. 2d, at 924</a></span>. Satisfied the police had time to secure a warrant, <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#100" aria-description="Citation for case: Commonwealth v. Labron"><i>id.,</i> at 100-103</a></span>, 699 A. 2d, at 924-925, the court held that "the warrantless search of this stationary vehicle violated constitutional guarantees," <i>id.,</i> at 101, <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#924" aria-description="Citation for case: Commonwealth v. Labron">669 A. 2d, at 924</a></span>.</p>
<p>In <i>Kilgore,</i> No. 95-1738, an undercover informant agreed to buy drugs from respondent Randy Lee Kilgore's accomplice, Kelly Jo Kilgore. To obtain the drugs, Kelly Jo drove from the parking lot where the deal was made to a farmhouse where she met with Randy Kilgore and obtained the drugs. After the drugs were delivered and the Kilgores were arrested, police searched the farmhouse with the consent of its owner and also searched Randy Kilgore's pickup truck; they had seen the Kilgores walking to and from the truck, which was parked in the driveway of the farmhouse. The search turned up cocaine on the truck's floor. The trial court denied Randy Kilgore's motion to suppress the cocaine, holding the officers had probable cause to make the search. <span class="star-pagination">*940</span> The appellate court affirmed. <span class="citation" data-id="2165222"><a href="/opinion/2165222/commonwealth-v-kilgore/" aria-description="Citation for case: Commonwealth v. Kilgore">437 Pa. Super. 491</a></span>, <span class="citation" data-id="2165222"><a href="/opinion/2165222/commonwealth-v-kilgore/" aria-description="Citation for case: Commonwealth v. Kilgore">650 A. 2d 462</a></span> (1994). The Supreme Court of Pennsylvania reversed, citing <i>Labron</i> and holding that although there was probable cause to search the truck, <span class="citation" data-id="9714930"><a href="/opinion/2089408/commonwealth-v-kilgore/#444" aria-description="Citation for case: Commonwealth v. Kilgore">544 Pa. 439, 444</a></span>, <span class="citation" data-id="9714930"><a href="/opinion/2089408/commonwealth-v-kilgore/#313" aria-description="Citation for case: Commonwealth v. Kilgore">677 A. 2d 311, 313</a></span> (1995), the search violated the Fourth Amendment because no exigent circumstances justified the failure to obtain a warrant, <span class="citation" data-id="9714930"><a href="/opinion/2089408/commonwealth-v-kilgore/#445" aria-description="Citation for case: Commonwealth v. Kilgore"><i>id.,</i> at 445</a></span>, <span class="citation" data-id="9714930"><a href="/opinion/2089408/commonwealth-v-kilgore/#313" aria-description="Citation for case: Commonwealth v. Kilgore">677 A. 2d, at 313-314</a></span>.</p>
<p>The Supreme Court of Pennsylvania held the rule permitting warrantless searches of automobiles is limited to cases where "`unforeseen circumstances involving the search of an automobile [are] coupled with the presence of probable cause.' " <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#100" aria-description="Citation for case: Commonwealth v. Labron">543 Pa., at 100</a></span>, <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#924" aria-description="Citation for case: Commonwealth v. Labron">669 A. 2d, at 924</a></span>, quoting <i>Commonwealth</i> v. <i>White,</i> <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/#53" aria-description="Citation for case: Commonwealth v. White">543 Pa. 45, 53</a></span>, <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/#901" aria-description="Citation for case: Commonwealth v. White">669 A. 2d 896, 901</a></span> (1995) (emphasis deleted). This was incorrect. Our first cases establishing the automobile exception to the Fourth Amendment's warrant requirement were based on the automobile's "ready mobility," an exigency sufficient to excuse failure to obtain a search warrant once probable cause to conduct the search is clear. <i>California</i> v. <i>Carney,</i> <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#390" aria-description="Citation for case: California v. Carney">471 U. S. 386, 390-391</a></span> (1985) (tracing the history of the exception); <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925). More recent cases provide a further justification: the individual's reduced expectation of privacy in an automobile, owing to its pervasive regulation. <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#391" aria-description="Citation for case: California v. Carney"><i>Carney, supra,</i> at 391-392</a></span>. If a car isreadily mobile and probable cause exists to believe it contains contraband, the Fourth Amendment thus permits police to search the vehicle without more. <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#393" aria-description="Citation for case: California v. Carney"><i>Carney, supra,</i> at 393</a></span>. As the state courts found, there was probable cause in both of these cases: Police had seen respondent Labron put drugs in the trunk of the car they searched and had seen respondent Kilgore act in ways that suggested he had drugs in his truck. We conclude the searches of the automobiles in these cases did not violate the Fourth Amendment.</p>
<p>Respondent Labron claims we have no jurisdiction to review the judgment in his case because the Pennsylvania Supreme Court's opinion rests on an adequate and independent <span class="star-pagination">*941</span> state ground, viz., "this Commonwealth's jurisprudence of the automobile exception." 543 Pa., at 100, 669 A. 2d, at 924. We disagree. The language we have quoted is not a "plain statement" sufficient to tell us "the federal cases [were] being used only for the purpose of guidance, and d[id] not themselves compel the result that the court ha[d] reached." <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1041" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1041</a></span> (1983). The Pennsylvania Supreme Court did discuss several of its own decisions; as it noted, however, some of those cases relied on an analysis of our cases on the automobile exception, see, <i>e. g.,</i> 543 Pa., at 95, 669 A. 2d, at 921 (observing <i>Commonwealth</i> v. <i>Holzer,</i> <span class="citation" data-id="9711114"><a href="/opinion/2073495/commonwealth-v-holzer/#103" aria-description="Citation for case: Commonwealth v. Holzer">480 Pa. 93, 103</a></span>, <span class="citation" data-id="9711114"><a href="/opinion/2073495/commonwealth-v-holzer/#106" aria-description="Citation for case: Commonwealth v. Holzer">389 A. 2d 101, 106</a></span> (1978), cited <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971)); 543 Pa., at 100, 669 A. 2d, at 924 (stating <i>Commonwealth</i> v. <i><span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">White, supra</a></span></i><i>,</i> rested in part upon the Pennsylvania Supreme Court's analysis of <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970)). The law of the Commonwealth thus appears to us "interwoven with the federal law, and . . . the adequacy and independence of any possible state law ground is not clear from the face of the opinion." <i>Michigan</i> v. <i>Long,</i>  <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long">463 U. S., at 1040-1041</a></span>. Our jurisdiction in Labron's case is secure. <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Ibid.</a></span></i> The opinion in respondent Kilgore's case, meanwhile, rests on an explicit conclusion that the officers' conduct violated the Fourth Amendment; we have jurisdiction to review this judgment as well.</p>
<p>Respondent Labron's motion to proceed <i>in forma pauperis</i>  is granted. The petitions for writs of certiorari are granted, the judgments of the Supreme Court of Pennsylvania are reversed, and the cases are remanded for further proceedings not inconsistent with this opinion.</p>
<blockquote>
<i>It is so ordered.</i>  Justice Stevens, with whom Justice Ginsburg joins, dissenting.</blockquote>
<p>The decisions that the Court summarily reverses today are two of a trilogy of cases decided by the Pennsylvania Supreme <span class="star-pagination">*942</span> Court within three days of each other. See <span class="citation" data-id="9714930"><a href="/opinion/2089408/commonwealth-v-kilgore/" aria-description="Citation for case: Commonwealth v. Kilgore">544 Pa. 439</a></span>, <span class="citation" data-id="9714930"><a href="/opinion/2089408/commonwealth-v-kilgore/" aria-description="Citation for case: Commonwealth v. Kilgore">677 A. 2d 311</a></span> (1995); <i>Commonwealth</i> v. <i>White,</i> <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">543 Pa. 45</a></span>, <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">669 A. 2d 896</a></span> (1995); <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/" aria-description="Citation for case: Commonwealth v. Labron">543 Pa. 86</a></span>, <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/" aria-description="Citation for case: Commonwealth v. Labron">669 A. 2d 917</a></span> (1995).<sup>[1]</sup> In each case, that court concluded that citizens of Pennsylvania are protected from warrantless searches and seizures of their automobiles absent exigent circumstances. But a fair reading of both <i>White</i> (the holding of which the Commonwealth has not challenged in this Court) and <i>Labron</i> (which the Court reverses today) demonstrates that their judgments almost certainly rested upon the Pennsylvania court's independent consideration of its own Constitution. For that reason, I do not believe that we have jurisdiction over the decision in <i>Labron,</i> just as we would not have jurisdiction in <i>White.</i> See <span class="citation no-link">28 U. S. C. § 1257</span>(a).<sup>[2]</sup> Furthermore, when considered in light of those two more carefully reasoned decisions, there is no reason for this Court to disturb the state court's finding in <i>Kilgore,</i> since the result will almost certainly be affirmed on remand.</p>
<p>In its <i>per curiam</i> decision, this Court concludes that because the decision in <i>Labron</i> cited state decisions which in turn referred to two 25-year-old cases of this Court, any reference to state law is "`interwoven with the federal law.' " <i>Ante,</i> at 941 (quoting <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1040</a></span> (1983)). These references, however, seem to me a rather short thread with which to weavelet alone upon which to hangour jurisdiction.</p>
<p><span class="star-pagination">*943</span> In my opinion, the best reading of <i>Labron</i> `s plain language is that it relied on adequate and independent state grounds. The majority decision below includes references to four sources of federal law: the Federal Constitution and three federal cases. None of the references demonstrates that the decision rested upon anything other than state law.</p>
<p>The decision begins with the proposition, not at issue here, that "the Fourth Amendment to the United States Constitution and Article I, § 8 of the Pennsylvania Constitution generally require that searches be predicated upon a warrant issued by a neutral and detached magistrate." 543 Pa., at 93, 669 A. 2d, at 920 (citations omitted). It then reviews the history of the so-called "automobile exception" to the warrant requirement by quoting several passages from our decision in <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), which first established the exception, and then quotes a passage from <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 52</a></span> (1970),<sup>[3]</sup> which appears to support the proposition under federal law that the Court emphasizes here today (that the existence of probable cause is sufficient in and of itself to justify a search of a vehicle). 543 Pa., at 94-95, 669 A. 2d, at 920-921.</p>
<p>Rather than follow the developments of federal law, however, the decision then specifically and immediately notes that "[w]hen reviewing warrantless automobile searches <i>in this Commonwealth,</i> we have constantly held that `there is no "automobile exception" as such and [that] the constitutional protections are applicable to searches and seizures of a person's car.' <i>Commonwealth</i> v. <i>Holzer,</i> <span class="citation" data-id="9711114"><a href="/opinion/2073495/commonwealth-v-holzer/#103" aria-description="Citation for case: Commonwealth v. Holzer">480 Pa. 93, 103</a></span>, <span class="citation" data-id="9711114"><a href="/opinion/2073495/commonwealth-v-holzer/#106" aria-description="Citation for case: Commonwealth v. Holzer">389 A. 2d 101, 106</a></span> (1978) (citing <i>Coolidge</i> v. <i>New Hampshire,</i>  <span class="star-pagination">*944</span> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> .. . (1971))." <i>Id.,</i> at 95, 669 A. 2d, at 921 (emphasis added). From that point onward, the only reference to federal law in the decision's remaining 30 citations is a recognition that <i>White,</i> the sole decision of this trio of "exigent circumstance" cases that is not before our Court, was "based upon" that Court's analysis of <i>Chambers.</i> 543 Pa., at 99-100, 669 A. 2d, at 923-924. Every other citation in <i>Labron</i> is to Pennsylvania law.</p>
<p>Because <i>White</i> was issued on the same day as <i>Labron</i> and reached an identical conclusion regarding the "exigent circumstances" rule, that decision is worth reviewing. In <i>White,</i> the court hesitated before considering the merits of the case "to address the Commonwealth's claim that White has waived his claim that the search of his automobile was illegal under Article I, Section 8 of the Pennsylvania Constitution because he did not set forth his state constitutional claims in the manner required." The Commonwealth's claim, the court found, was "meritless." "White clearly raises a claim under the Pennsylvania Constitution, cites cases in support of his claim, and relates the cases to the claim. That is sufficient." 543 Pa., at 50, 669 A. 2d, at 899.</p>
<p>Having established the importance of the state constitutional claim to the defendant's argument, <i>White</i> went on to discuss the "exigent circumstance" exception at issue here in light of both federal and state law. And although the court's analysis relied upon our decision in <i>Chambers</i> v. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Maroney</a></span></i><i>,</i> it cited none of the subsequent cases in which this Court has effectively converted the "automobile exception" into an absolute rule allowing searches in the presence of probable cause. See 543 Pa., at 49-53, 669 A. 2d, at 899-901; n. 6, <i>infra</i> (noting that the Pennsylvania courts' failure to refer to this Court's subsequent decisions in this area may be intentional rather than ignorant). Stressing the independent evaluation it makes of its State Constitution, the Pennsylvania court also rejected our decision in <i>New York</i> v. <i>Belton,</i>  <span class="star-pagination">*945</span> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981), on state constitutional grounds. See 543 Pa., at 54-58, 669 A. 2d, at 901-903.<sup>[4]</sup></p>
<p>Notably, the Commonwealth has not asked this Court to review the Pennsylvania court's decision in <i>White,</i> even though the search in that case would be affirmed under the Commonwealth's and this Court's understanding of Pennsylvania's holding regarding exigent circumstances. I also note that lower state courts have explicitly read <i>White</i> as establishing a state constitutional right, not a federal right. <i>Commonwealth</i> v. <i>Haskins,</i> <span class="citation" data-id="2089468"><a href="/opinion/2089468/commonwealth-v-haskins/#545" aria-description="Citation for case: Commonwealth v. Haskins">450 Pa. Super. 540, 545</a></span>, <span class="citation" data-id="2089468"><a href="/opinion/2089468/commonwealth-v-haskins/#330" aria-description="Citation for case: Commonwealth v. Haskins">677 A. 2d 328, 330</a></span> (1996) ("In order to search an automobile without a warrant, the police must still show the existence of both probable cause and exigent circumstances. <i>Commonwealth</i>  v. <i>White,</i> <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">543 Pa. 45</a></span>, <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">669 A. 2d 896</a></span> (1995). . . . In <i>White,</i> our Supreme Court reiterated that the Pennsylvania Constitution requires such a showing"); see also <i>Commonwealth</i> v. <i>Yedinak,</i> <span class="citation" data-id="9716881"><a href="/opinion/2100000/commonwealth-v-yedinak/#359" aria-description="Citation for case: Commonwealth v. Yedinak">450 Pa. Super. 352, 359, n. 5</a></span>, <span class="citation" data-id="9716881"><a href="/opinion/2100000/commonwealth-v-yedinak/#1220" aria-description="Citation for case: Commonwealth v. Yedinak">676 A. 2d 1217, 1220, n. 5</a></span> (1996) ("The Pennsylvania Supreme Court recently held that the Pennsylvania Constitution provides greater protection than the United States Constitution with regard to automobile searches in <i>Commonwealth</i> v. <i>White</i> ").</p>
<p>The lower courts' understanding regarding the state-law nature of <i>White</i> and my understanding of the state-law nature of <i>Labron</i> as wellis almost perfectly reflected in the dissents to each case that were penned by Justice Castille. In both instances, Justice Castille recognizes, even more explicitly than the majority, that the decisions were based on state law.</p>
<p>In <i>Labron,</i> for instance, his main point was that the defendant had no standing to challenge the constitutionality of <span class="star-pagination">*946</span> the search of a car that he did not own. In making his argument, however, he noted that "the majority correctly characterizes <i>Pennsylvania law</i> regarding the `automobile exception' to the warrant requirement." 543 Pa., at 104, 669 A. 2d, at 926 (emphasis added). And although he reviewed decisions of this Court on standing to claim violations of the Fourth Amendment, he went on to note: "<i>Under Article I, Section 8 of the Pennsylvania Constitution,</i> however, this Court looks to several additional factors to determine whether a criminal defendant has standing to challenge the admission of evidence against him." <i>Id.,</i> at 106, 669 A. 2d, at 927 (emphasis added).</p>
<p>In <i>White,</i> Justice Castille stated that he believed that "the automobile exception to the warrant requirements of <i>this Commonwealth</i> should be a <i>per se</i> rule regardless of how much time police may have to obtain a warrant," 543 Pa., at 70, 669 A. 2d, at 909 (emphasis added), and he further concluded that he would "urge the adoption of a bright line rule that would allow warrantless searches of all automobiles for which police have independent probable cause," <i>id.,</i> at 71, 669 A. 2d, at 909-910. Of course, if Justice Castille were interpreting federal, rather than state, law, he would not have the luxury of "urging the adoption" of a particular rule.<sup>[5]</sup></p>
<p>Having reviewed the range of the Pennsylvania courts' statements regarding the source of the "exigent circumstances" rule, it is worthwhile to review this Court's understanding of when a state decision is based on adequate and independent state grounds. In <i>Michigan</i> v. <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span>,</i> the Court adopted a "plain statement" rule for determining whether a state decision rested on "independent and adequate" statelaw grounds. "[B]ecause of [our] respect for state courts, <span class="star-pagination">*947</span> and [a] desire to avoid advisory opinions, . . . we [did] not wish to continue to decide issues of state law that go beyond the opinion that we review, or to require state courts to reconsider cases to clarify the grounds of their decisions." <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long">463 U. S., at 1040</a></span>. When "a state court decision fairly appears to rest <i>primarily</i> on federal law, or to be interwoven with the federal law, and when the adequacy and independence of any possible state law ground is not clear from the face of the opinion," we held, we would conclude that the State decided as it did because federal law required it to do so. <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long"><i>Id.,</i>  at 1040-1041</a></span>.</p>
<p>Given the explicit and nearly exclusive references to state law that I review above, it seems to me that the Court's decision to take jurisdiction in <i>Labron</i> not only extends <i>Michigan</i> v. <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i> beyond its original scope, but stands its rationale on its head. <i>Labron</i> does not rest "primarily" on federal law; as Justice Castille understood it, as the briefing in <i>White</i> understood it, and as the Commonwealth's decision to stay out of <i>White</i> demonstrates, every indication is that the rule adopted in <i>Labron</i> and <i>White</i> rests primarily on state law. Nor are these holdings "interwoven" with federal law: Both <i>Labron</i> and <i>White</i> cite only two federal cases, both over a quarter-century old; rather than implicitly conclude that the absence of any reference to more recent decisions is due to poor legal research, I would trust the Pennsylvania courts' ability to understand and choose to deviate from our federal law. Certainly it would be a more respectful approach, in a case where the question is as close as it is in this case, to conclude that the State had made a conscious decision to depart from the jurisprudence of this Court rather than an error of law.<sup>[6]</sup></p>
<p><span class="star-pagination">*948</span> The nature of the Pennsylvania court's reliance on federal law in these cases, therefore, is quite different from that which spurred the Court to conclude in <i>Michigan</i> v. <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i>  that the judgment of the Michigan Supreme Court had not relied on adequate and independent state grounds. There, as the Court noted, the decision below "referred twice to the State Constitution in its opinion, but otherwise relied <i>exclusively</i> on federal law." <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1037" aria-description="Citation for case: Michigan v. Long">463 U. S., at 1037</a></span> (emphasis <span class="star-pagination">*949</span> added). The dissents below also relied explicitly and <i>exclusively</i> on decisions of this Court. <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1037" aria-description="Citation for case: Michigan v. Long"><i>Id.,</i> at 1037, n. 2</a></span>; <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#473" aria-description="Citation for case: People v. Long">413 Mich. 461, 473-486</a></span>, <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#870" aria-description="Citation for case: People v. Long">320 N. W. 2d 866, 870-875</a></span> (1982) (Coleman, C. J., dissenting, Moody, J., concurring in part and dissenting in part). Indeed, the critical holding of the Court was that the Michigan "Court of Appeals erroneously applied the principles of <i>Terry</i> v. <i>Ohio.</i> " <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#471" aria-description="Citation for case: People v. Long"><i>Id.,</i> at 471</a></span>, <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#869" aria-description="Citation for case: People v. Long">320 N. W. 2d, at 869</a></span> (citation omitted).<sup>[7]</sup> The opinion in these cases presents almost precisely the opposite situation: The decision refers to the Federal Constitution once, but otherwise relies <i>exclusively</i> on state law.</p>
<p>For these reasons, just as the decision in <i>White</i> would not merit summary reversal were it before this Court, the decision in <i>Labron</i> should not be summarily reversed. Although <i>Labron</i> and <i>White</i> both touch upon, and even place some historical reliance upon, federal search and seizure law, each also recognizes the broad interpretation that the Pennsylvania court has given its own constitutional prohibition against warrantless searches. I therefore seriously question <span class="star-pagination">*950</span> whether respect for the reasoning, independence, and resources of the Pennsylvania court will be advanced by today's decision.</p>
<p>While <i>Kilgore</i> relies more explicitly on the Federal Constitution than the other two decisions, it decided the identical issue that was decided in <i>Labron</i> and <i>White</i> only three days before those decisions issued. The reference to the Federal Constitution upon which the Court rests its jurisdiction only one of two references to federal lawmust be read in the context of the other two decisions, each of which relied heavily upon the Commonwealth's own Constitution. In light of <i>Labron</i> and <i>White,</i> the judgment in <i>Kilgore</i> will almost certainly remain the same on remand. In such a circumstance, the rationales supporting the rule of <i>Michigan</i>  v. <i>Long</i> simply do not support the decision to reverse. The petition in <i>Kilgore</i> should simply be denied.</p>
<p>On many prior occasions, I have noted the unfortunate effects of the rule of <i>Michigan</i> v. <i>Long.</i> See, <i>e. g., </i><i>Harris</i> v. <i>Reed,</i> <span class="citation" data-id="9431577"><a href="/opinion/112205/harris-v-reed/#266" aria-description="Citation for case: Harris v. Reed">489 U. S. 255, 266-267</a></span> (1989) (concurring opinion); <i>Delaware</i> v. <i>Van Arsdall,</i> <span class="citation" data-id="9430412"><a href="/opinion/111625/delaware-v-van-arsdall/#689" aria-description="Citation for case: Delaware v. Van Arsdall">475 U. S. 673, 689-708</a></span> (1986) (dissenting opinion); <i>Montana</i> v. <i>Hall,</i> <span class="citation" data-id="9430940"><a href="/opinion/111872/montana-v-hall/#411" aria-description="Citation for case: Montana v. Hall">481 U. S. 400, 411</a></span> (1987) <i>(per curiam)</i> (dissenting opinion); <i>Ponte</i> v. <i>Real,</i> <span class="citation" data-id="9430022"><a href="/opinion/111430/ponte-v-real/#501" aria-description="Citation for case: Ponte v. Real">471 U. S. 491, 501-503</a></span> (1985) (opinion concurring in part); see also <i>Arizona</i>  v. <i>Evans,</i> <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#24" aria-description="Citation for case: Arizona v. Evans">514 U. S. 1, 24, 31-34</a></span> (1995) (Ginsburg, J., dissenting). Because the state-law ground supporting these judgments is so much clearer than has been true on most prior occasions, see n. 5, <i>supra,</i> these decisions exacerbate those effects to a nearly intolerable degree. Particularly in light of my understanding of this Court's primary role"to protect the rights of the individual that are embodied in the Federal Constitution," <i><span class="citation" data-id="9431577"><a href="/opinion/112205/harris-v-reed/" aria-description="Citation for case: Harris v. Reed">Harris</a></span>,</i> 489 U. S., at 267the decision to summarily reverse state decisions resting tenuously at best on federal grounds is imprudent and entirely inconsistent "with the sound administration of this Court's discretionary docket." <i>Ponte,</i> <span class="citation" data-id="9430022"><a href="/opinion/111430/ponte-v-real/#502" aria-description="Citation for case: Ponte v. Real">471 U. S., at 502-503</a></span>.</p>
<p><span class="star-pagination">*951</span> The Pennsylvania court has in these and other cases expressly indicated its intent to extend the protections of its Constitution beyond those available under the Federal Constitution, see, <i>e. g., </i><i>Commonwealth</i> v. <i>Edmunds,</i> <span class="citation" data-id="9752984"><a href="/opinion/2316698/commonwealth-v-edmunds/" aria-description="Citation for case: Commonwealth v. Edmunds">526 Pa. 374</a></span>, <span class="citation" data-id="9752984"><a href="/opinion/2316698/commonwealth-v-edmunds/" aria-description="Citation for case: Commonwealth v. Edmunds">586 A. 2d 887</a></span> (1991) (setting forth test for establishing rights under Pennsylvania Constitution); <i>Commonwealth</i> v. <i>Rosenfelt,</i> <span class="citation" data-id="9636411"><a href="/opinion/1473518/commonwealth-v-rosenfelt/#634" aria-description="Citation for case: Commonwealth v. Rosenfelt">443 Pa. Super. 616, 634-637</a></span>, <span class="citation" data-id="9636411"><a href="/opinion/1473518/commonwealth-v-rosenfelt/#1140" aria-description="Citation for case: Commonwealth v. Rosenfelt">662 A. 2d 1131, 1140-1141</a></span> (1995) (reviewing state cases extending greater protections under the Pennsylvania Constitution). The <i>per curiam</i> decision that the Court issues today merely makes that task harder by requiring the Commonwealth to purge its decisions of any reliance on the latter, despite the value of the insights that our decisions can provide on related issues of law. By "unceremoniously reversing its judgment," <i>Van Arsdall,</i> <span class="citation" data-id="9430412"><a href="/opinion/111625/delaware-v-van-arsdall/#701" aria-description="Citation for case: Delaware v. Van Arsdall">475 U. S., at 701</a></span> (Stevens, J., dissenting), we also demonstrate a lack of respect for the Pennsylvania court and the sophistication of its state search and seizure law. See <span class="citation" data-id="9430412"><a href="/opinion/111625/delaware-v-van-arsdall/#699" aria-description="Citation for case: Delaware v. Van Arsdall"><i>id.,</i> at 699</a></span>.</p>
<p>These harms are particularly unnecessary given the likely result on remand. To reinvigorate the privacy protections extended to Pennsylvania citizens under <i>Labron, Kilgore,</i>  and <i>White,</i> the Pennsylvania Supreme Court need only set forth the appropriate talismanic language and state, even more clearly than it already has, that the "<i>Commonwealth's</i>  jurisprudence of the automobile exception [requires] both the existence of probable cause and the presence of exigent circumstances to justify a warrantless search." <i>Labron,</i> <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#100" aria-description="Citation for case: Commonwealth v. Labron">543 Pa., at 100</a></span>, <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#924" aria-description="Citation for case: Commonwealth v. Labron">669 A. 2d, at 924</a></span> (emphasis added).<sup>[8]</sup> While the <span class="star-pagination">*952</span> result will be identical, resources and respect will have been unnecessarily lost.</p>
<p>I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]   Together with No. 95-1738, <i>Pennsylvania</i> v. <i>Kilgore,</i> also on petition for writ of certiorari to the same court.</p>
<p>[1]  Each decision was issued by a different division of the Pennsylvania Supreme Court.</p>
<p>[2]  Even if, as the Court concludes, <i>ante,</i> at 941, some element of residual doubt suggests that Pennsylvania's Supreme Court drew inspiration from our interpretations of the Federal Constitution, I do not think that reliance sufficient to justify expending this Court's timeor that of the Pennsylvania Supreme Courtsimply to scour the state decisions of all references to the Federal Constitution. See <i>infra,</i> at 943-950.</p>
<p>[3]  As the Pennsylvania Supreme Court noted, in <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span></i> we held that "`[f]or constitutional purposes, [there is] no difference between on the one hand seizing and holding a car before presenting the probable cause issue to a magistrate and on the other hand carrying out an immediate search without a warrant.' " <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#95" aria-description="Citation for case: Commonwealth v. Labron">543 Pa. 86, 95</a></span>, <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#921" aria-description="Citation for case: Commonwealth v. Labron">669 A. 2d 917, 921</a></span> (1995) (quoting <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney">399 U. S., at 52</a></span>).</p>
<p>[4]  Although the court's main opinion in <i>Commonwealth</i> v.<i>White</i> also asked whether the search would have been permissible as a search incident to an arrest, the dissent later noted that the only question presented in the appeal was whether "exigent circumstances" were necessary to permit a warrantless search of a car based on probable cause. See 543 Pa., at 72-73, 669 A. 2d, at 910.</p>
<p>[5]  Justice Castille also specifically noted that the <i><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span></i> decision was not raised by the parties,and that the majority's discussion of it was dicta, further emphasizing that his emphasis on Pennsylvania law was related to the sole issue that he believed presented: whether a warrantless search of an automobile requires both probable cause and an exigent circumstance.</p>
<p>[6]  Indeed, the author of <i>Labron</i> noted in <i>White</i> that "the history of Article I, Section 8 and case-law interpreting it reveal a history of according a limited expectation of privacy in an automobile independently under the Pennsylvania Constitution. Therefore, the question before us today is not whether we wish to extend additional privacy protections to the Appellant but whether we wish to follow the United States Supreme Court and sharply curtail a privacy interest long recognized by this Court." <i>Commonwealth</i> v. <i>White,</i> <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/#62" aria-description="Citation for case: Commonwealth v. White">543 Pa., at 62</a></span>, <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/#905" aria-description="Citation for case: Commonwealth v. White">669 A. 2d, at 905</a></span>.
</p>
<p>To this end, I find it particularly interesting that only two Pennsylvania courts have cited the decision in <i>California</i> v. <i>Carney,</i> <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/" aria-description="Citation for case: California v. Carney">471 U. S. 386</a></span> (1985), upon which the <i>per curiam</i> decision relies as modern support for its interpretation of federal constitutional law. See <i>Commonwealth</i> v. <i>Rosenfelt,</i>  <span class="citation" data-id="9636411"><a href="/opinion/1473518/commonwealth-v-rosenfelt/#632" aria-description="Citation for case: Commonwealth v. Rosenfelt">443 Pa. Super. 616, 632-634</a></span>, <span class="citation" data-id="9636411"><a href="/opinion/1473518/commonwealth-v-rosenfelt/#1139" aria-description="Citation for case: Commonwealth v. Rosenfelt">662 A. 2d 1131, 1139</a></span> (1995); <i>Commonwealth</i>  v. <i>Camacho,</i> <span class="citation" data-id="1928985"><a href="/opinion/1928985/commonwealth-v-camacho/" aria-description="Citation for case: Commonwealth v. Camacho">425 Pa. Super. 567</a></span>, <span class="citation" data-id="1928985"><a href="/opinion/1928985/commonwealth-v-camacho/" aria-description="Citation for case: Commonwealth v. Camacho">625 A. 2d 1242</a></span> (1995). Each of those decisions expressly noted the presence of conflict between federal and state law on this issue.</p>
<p>In <i><span class="citation" data-id="1928985"><a href="/opinion/1928985/commonwealth-v-camacho/" aria-description="Citation for case: Commonwealth v. Camacho">Camacho</a></span>,</i> the Superior Court noted "the discrepancy between some of the Commonwealth's past cases and federal cases which speak to automobile searches" in cases like those at issue here. <span class="citation" data-id="1928985"><a href="/opinion/1928985/commonwealth-v-camacho/#576" aria-description="Citation for case: Commonwealth v. Camacho"><i>Id.,</i> at 576, n. 2</a></span>, <span class="citation" data-id="1928985"><a href="/opinion/1928985/commonwealth-v-camacho/#1247" aria-description="Citation for case: Commonwealth v. Camacho">625 A. 2d, at 1247, n. 2</a></span>. After reviewing the holding in <i><span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/" aria-description="Citation for case: California v. Carney">Carney</a></span>,</i> the court noted that the state cases concluding that there was no <i>per se</i> "`automobile exception' " were "simply dated and not in keeping with the tenor of current law." 425 Pa. Super., at 577, n. 2, <span class="citation" data-id="1928985"><a href="/opinion/1928985/commonwealth-v-camacho/#1247" aria-description="Citation for case: Commonwealth v. Camacho">625 A. 2d, at 1247, n. 2</a></span>.</p>
<p>The court in <i><span class="citation" data-id="9636411"><a href="/opinion/1473518/commonwealth-v-rosenfelt/" aria-description="Citation for case: Commonwealth v. Rosenfelt">Rosenfelt</a></span></i> reached an alternative explanation for the conflictand a result identical to that reached in the cases reversed by the Court today. There, the defendant agreed that the search of the vehicle was not illegal under federal law. Citing <i><span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/" aria-description="Citation for case: California v. Carney">Carney</a></span>,</i> the court noted that the federal "automobile exception" had "jettison[ed]" the requirement of exigency, essentially converting the exception into a <i>per se</i> rule allowing a search once probable cause exists. See 443 Pa. Super., at 633, 644-645, <span class="citation" data-id="9636411"><a href="/opinion/1473518/commonwealth-v-rosenfelt/#1139" aria-description="Citation for case: Commonwealth v. Rosenfelt">662 A. 2d, at 1139, 1145</a></span>. Noting that the State Constitution could extend greater protections to Pennsylvania citizens than did the Federal Constitution, but that its Supreme Court had not yet decided whether that was the case, the Superior Court went on to review the issue on its own and found a state constitutional violation. <i><span class="citation" data-id="9636411"><a href="/opinion/1473518/commonwealth-v-rosenfelt/" aria-description="Citation for case: Commonwealth v. Rosenfelt">Ibid.</a></span></i> After it decided the cases at issue here, the Pennsylvania Supreme Court denied the Commonwealth's appeal. See <span class="citation no-link">544 Pa. 605</span>, <span class="citation no-link">674 A. 2d 1070</span> (1996) (table).</p>
<p>[7]  On the many subsequent occasions in which this Court has taken jurisdiction over state decisions over which there was some dispute about the nature of the relationship between federal and state law, the state opinions were far more "interwoven" with federal law than is true in these cases. See, <i>e. g., </i><i>Illinois</i> v. <i>Rodriguez,</i> <span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/#182" aria-description="Citation for case: Illinois v. Rodriguez">497 U. S. 177, 182</a></span> (1990) (decision below did not "rely on (or even mention) any specific provision" of State Constitution); <i>Pennsylvania</i> v. <i>Muniz,</i> <span class="citation" data-id="9432075"><a href="/opinion/112464/pennsylvania-v-muniz/#588" aria-description="Citation for case: Pennsylvania v. Muniz">496 U. S. 582, 588, n. 4</a></span> (1990) (state constitutional provision construed to provide protections identical to Federal Constitution); <i>Florida</i> v. <i>Riley,</i> <span class="citation" data-id="9431518"><a href="/opinion/112175/florida-v-riley/#448" aria-description="Citation for case: Florida v. Riley">488 U. S. 445, 448, n. 1</a></span> (1989) (decision below mentioned State Constitution only twice, but "focused exclusively on federal cases dealing with the Fourth Amendment"); <i>Michigan</i> v. <i>Chesternut,</i>  <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#571" aria-description="Citation for case: Michigan v. Chesternut">486 U. S. 567, 571, n. 3</a></span> (1988) (decision below "said nothing to suggest that the Michigan Constitution's seizure provision provided an independent source of relief, and the court's entire analysis rested expressly on the Fourth Amendment and federal cases"); <i>Kentucky</i> v. <i>Stincer,</i> <span class="citation" data-id="9431052"><a href="/opinion/111928/kentucky-v-stincer/#735" aria-description="Citation for case: Kentucky v. Stincer">482 U. S. 730, 735, n. 7</a></span> (1987) (decision below "consistently referred to respondent's rights under the . . . Federal Constitution as supporting its ruling"); <i>Maryland</i> v. <i>Garrison,</i> <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#83" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79, 83-84</a></span> (1987) (State Constitution construed <i>in pari materia</i> with Federal Constitution).</p>
<p>[8]  State courts have, of course, done this on many occasions in the past. See, <i>e. g., </i><i>Ponte</i> v. <i>Real,</i> <span class="citation" data-id="9430022"><a href="/opinion/111430/ponte-v-real/#503" aria-description="Citation for case: Ponte v. Real">471 U. S. 491, 503, n. 4</a></span> (1985) (Stevens, J., concurring in part) (listing various cases in which reversals by this Court were followed by state-court decisions affirming the original holding on statelaw grounds); <i>Montana</i> v. <i>Hall,</i> <span class="citation" data-id="9430940"><a href="/opinion/111872/montana-v-hall/#411" aria-description="Citation for case: Montana v. Hall">481 U. S. 400, 411</a></span> (1987) <i>(per curiam)</i>  (Stevens, J., dissenting) (same).</p>

</div>
```

---
