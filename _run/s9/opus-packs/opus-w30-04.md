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

## GROUP: content/cases/County of Sacramento v. Lewis.md  (`case`, 5 assertions)

### content_page

```
---
title: "County of Sacramento v. Lewis"
type: case
citation: "523 U.S. 833 (1998)"
parallel_cite: "118 S. Ct. 1708; 140 L. Ed. 2d 1043"
neutral_cite: 1998 U.S. LEXIS 3404
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1998
date_decided: 1998-05-26
docket: 96-1337
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1998-05-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: County of Sacramento v. Lewis
  varies_by_point: false
  scope_note: "Good law: pursuit deaths without a seizure are judged under Fourteenth Amendment substantive due process ('shocks the conscience'), requiring a purpose to cause harm."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118214/county-of-sacramento-v-lewis/"
  cluster_id: 118214
  opinion_id: 118214
  identity_checked: true
homes:
  - page: "[[Use of Force]]"
    role: "Key — Progeny / Refinement"
related: ["[[Graham v. Connor]]", "[[Scott v. Harris]]", "[[Kingsley v. Hendrickson]]"]
aliases: ["Sacramento v. Lewis"]
tags: ["case", "use-of-force", "high-speed-pursuit", "substantive-due-process", "shocks-the-conscience", "section-1983"]
holding: "A death caused by a high-speed police pursuit, absent a Fourth Amendment seizure, is analyzed under Fourteenth Amendment substantive due process; only a purpose to cause harm unrelated to the legitimate object of arrest shocks the conscience — deliberate indifference is not enough in a pursuit."
lake:
  record_id: County of Sacramento v. Lewis
  status: verified
  projected_at: 2026-07-09
---

# County of Sacramento v. Lewis

*523 U.S. 833 (1998)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Sacramento County sheriff's deputies responded to a fight call when a motorcycle sped past, driven by Brian Willard with 16-year-old Philip Lewis as a passenger. Deputy James Everett Smith pursued at high speed through a residential area. When the motorcycle tipped over, Smith's patrol car could not stop in time and struck and killed Lewis. Lewis's parents sued Smith and the county under § 1983, alleging the pursuit deprived their son of life without due process.

## Issue
Whether a police officer violates the Fourteenth Amendment's substantive-due-process guarantee by causing death through deliberate or reckless indifference to life in a high-speed pursuit aimed at apprehending a suspect.

## Rule
Such a claim is judged under substantive due process, and only a purpose to harm shocks the conscience. "We answer no, and hold that in such circumstances only a purpose to cause harm unrelated to the legitimate object of arrest will satisfy the element of arbitrary conduct shocking to the conscience, necessary for a due process violation." — 523 U.S. at 836. ^pin-836

"Accordingly, we hold that high-speed chases with no intent to harm suspects physically or to worsen their legal plight do not give rise to liability under the Fourteenth Amendment, redressible by an action under § 1983." — [*Id.* at 854](https://www.courtlistener.com/opinion/118214/county-of-sacramento-v-lewis/#:~:text=Accordingly%2C%20we%20hold%20that%20high%2Dspeed). ^pin-854

## Application
Because no Fourth Amendment "seizure" occurred — Lewis's death resulted from the pursuit itself, not from a means intentionally applied to stop him — the claim fell under Fourteenth Amendment substantive due process rather than the Fourth Amendment. In the high-speed-pursuit setting, where officers must make instant judgments without time to deliberate, the deliberate-indifference standard used for unhurried custodial decisions does not apply; only an intent to harm unrelated to legitimate law enforcement shocks the conscience. Deputy Smith's conduct, even if reckless, did not meet that standard, so there was no due-process violation.

## Conclusion
Reversed. A high-speed-pursuit death without a seizure is governed by the Fourteenth Amendment's "shocks the conscience" standard, which in the pursuit context requires a purpose to cause harm; deliberate or reckless indifference is insufficient.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Lewis* marks the boundary between the [[Graham v. Connor]] Fourth Amendment standard (which applies only when a seizure occurs) and substantive due process; where a pursuit ends in an intentional seizure, the Fourth Amendment governs instead (see [[Scott v. Harris]]). Its culpability analysis is contrasted in the pretrial-detainee context by [[Kingsley v. Hendrickson]]. No negative treatment.

## Appears on
- [[Use of Force]] — *Key — Progeny / Refinement*
- [[Section 1983 Liability and Qualified Immunity]] — *Related (cross-doctrine)*

## Sources
- *County of Sacramento v. Lewis*, 523 U.S. 833 (1998) — https://www.courtlistener.com/opinion/118214/county-of-sacramento-v-lewis/ — pinpoints: 836, 854.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "493cdfc1b2e9b4f3", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "523 U.S. 833 (1998)", "court": "U.S. Supreme Court", "neutral_cite": "1998 U.S. LEXIS 3404", "official_citation_present": true, "parallel_cite": "118 S. Ct. 1708; 140 L. Ed. 2d 1043", "title": "County of Sacramento v. Lewis", "year": "1998"}}
{"assertion_id": "247d46f3105c7d16", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A death caused by a high-speed police pursuit, absent a Fourth Amendment seizure, is analyzed under Fourteenth Amendment substantive due process; only a purpose to cause harm unrelated to the legitimate object of arrest shocks the conscience — deliberate indifference is not enough in a pursuit.", "title": "County of Sacramento v. Lewis"}}
{"assertion_id": "886650430a1cd73f", "dimension": "support", "kind": "home_role", "locator": {"home": "Use of Force"}, "payload": {"home": "Use of Force", "role": "Key — Progeny / Refinement", "title": "County of Sacramento v. Lewis"}}
{"assertion_id": "2fab45941377de1f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "County of Sacramento v. Lewis"}}
{"assertion_id": "405d387a78912c38", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1998-05-26", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "County of Sacramento v. Lewis", "field_i_validity": "good_law", "scope_note": "Good law: pursuit deaths without a seizure are judged under Fourteenth Amendment substantive due process ('shocks the conscience'), requiring a purpose to cause harm.", "title": "County of Sacramento v. Lewis", "varies_by_point": "false"}}
```

### lake record — County of Sacramento v. Lewis

```json
{
  "schema_version": "s2.v1",
  "record_id": "County of Sacramento v. Lewis",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "County of Sacramento v. Lewis",
    "case_name_short": "Lewis",
    "case_name_full": "COUNTY OF SACRAMENTO Et Al. v. LEWIS, Et Al., Personal Representatives of the ESTATE OF LEWIS, DECEASED",
    "input_case_name": "County of Sacramento v. Lewis",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1998-05-26",
    "year": 1998,
    "docket": "96-1337",
    "cluster_id": 118214,
    "lead_opinion_id": 118214,
    "sibling_ids": [
      118214,
      9433650,
      9433651,
      9433652,
      9433653,
      9433654,
      9433655
    ],
    "absolute_url": "/opinion/118214/county-of-sacramento-v-lewis/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "523 U.S. 833",
      "volume": "523",
      "reporter": "U.S.",
      "page": "833",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "118 S. Ct. 1708",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "1708",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "140 L. Ed. 2d 1043",
        "volume": "140",
        "reporter": "L. Ed. 2d",
        "page": "1043",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1998 U.S. LEXIS 3404",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "3404",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "523 U.S. 833",
        "volume": "523",
        "reporter": "U.S.",
        "page": "833",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "118 S. Ct. 1708",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "1708",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "140 L. Ed. 2d 1043",
        "volume": "140",
        "reporter": "L. Ed. 2d",
        "page": "1043",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 U.S. LEXIS 3404",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "3404",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "523 U.S. 833",
    "official_selection": {
      "court_class": "scotus",
      "selected": "523 U.S. 833",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-836",
      "page": null,
      "quote": "--- # County of Sacramento v. Lewis *523 U.S. 833 (1998)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Sacramento County sheriff's deputies responded to a fight call when a motorcycle sped past, driven by Brian Willard with 16-year-old Philip Lewis as a passenger. Deputy James Everett Smith pursued at high speed through a residential area. When the motorcycle tipped over, Smith's patrol car could not stop in time and struck and killed Lewis. Lewis's parents sued Smith and the county under \u00a7 1983, alleging the pursuit deprived their son of life without due process. ## Issue Whether a police officer violates the Fourteenth Amendment's substantive-due-process guarantee by causing death through deliberate or reckless indifference to life in a high-speed pursuit aimed at apprehending a suspect. ## Rule Such a claim is judged under substantive due process, and only a purpose to harm shocks the conscience.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-854",
      "page": null,
      "quote": "Accordingly, we hold that high-speed chases with no intent to harm suspects physically or to worsen their legal plight do not give rise to liability under the Fourteenth Amendment, redressible by an action under \u00a7 1983.",
      "star_marker": "854",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 43691,
      "fragment": "#:~:text=Accordingly%2C%20we%20hold%20that%20high%2Dspeed",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1998-05-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "County of Sacramento v. Lewis",
    "varies_by_point": false,
    "scope_note": "Good law: pursuit deaths without a seizure are judged under Fourteenth Amendment substantive due process ('shocks the conscience'), requiring a purpose to cause harm.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "John McNeill, Jr, R.Ph. And Nichols Southside Pharmacy v. Courtney N. Phillips, Executive Commissioner Sylvia Hernandez Kauffman, Inspector General And Texas Health and Human Services Commission",
          "cluster_id": 4654085,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Michael Campos v. Cook County",
          "cluster_id": 4645586,
          "cite": [
            "932 F.3d 972"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pearson v. Callahan",
          "cluster_id": 145918,
          "cite": [
            "172 L. Ed. 2d 565",
            "129 S. Ct. 808",
            "555 U.S. 223",
            "2009 U.S. LEXIS 591"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. Harris",
          "cluster_id": 145738,
          "cite": [
            "167 L. Ed. 2d 686",
            "127 S. Ct. 1769",
            "550 U.S. 372",
            "2007 U.S. LEXIS 4748"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillips v. County of Allegheny",
          "cluster_id": 1387268,
          "cite": [
            "515 F.3d 224",
            "2008 U.S. App. LEXIS 2513",
            "2008 WL 305025"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In the Interest of J.F.C.",
          "cluster_id": 5275637,
          "cite": [
            "96 S.W.3d 256",
            "46 Tex. Sup. Ct. J. 328",
            "2002 Tex. LEXIS 215"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kingsley v. Hendrickson",
          "cluster_id": 2811847,
          "cite": [
            "576 U.S. 389",
            "135 S. Ct. 2466",
            "192 L. Ed. 2d 416",
            "2015 U.S. LEXIS 4073",
            "25 Fla. L. Weekly Fed. S 401",
            "83 U.S.L.W. 4515"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re JFC",
          "cluster_id": 1377577,
          "cite": [
            "96 S.W.3d 256",
            "2002 WL 31890913"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Toguchi v. Soon Hwang Chung",
          "cluster_id": 788614,
          "cite": [
            "391 F.3d 1051",
            "2004 U.S. App. LEXIS 25465",
            "2004 WL 2827667"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brosseau v. Haugen",
          "cluster_id": 137736,
          "cite": [
            "160 L. Ed. 2d 583",
            "125 S. Ct. 596",
            "543 U.S. 194",
            "2004 U.S. LEXIS 8275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Layne",
          "cluster_id": 118289,
          "cite": [
            "143 L. Ed. 2d 818",
            "119 S. Ct. 1692",
            "526 U.S. 603",
            "1999 U.S. LEXIS 3633"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
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
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Plumhoff v. Rickard",
          "cluster_id": 2675750,
          "cite": [
            "188 L. Ed. 2d 1056",
            "134 S. Ct. 2012",
            "2014 U.S. LEXIS 3816",
            "82 U.S.L.W. 4394",
            "572 U.S. 765",
            "24 Fla. L. Weekly Fed. S 790",
            "2014 WL 2178335"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "D. S. v. East Porter County School Corp",
          "cluster_id": 2830138,
          "cite": [
            "799 F.3d 793",
            "2015 U.S. App. LEXIS 14901",
            "2015 WL 5005080"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brendlin v. California",
          "cluster_id": 145712,
          "cite": [
            "168 L. Ed. 2d 132",
            "127 S. Ct. 2400",
            "551 U.S. 249",
            "2007 U.S. LEXIS 7897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lawrence v. Texas",
          "cluster_id": 130160,
          "cite": [
            "156 L. Ed. 2d 508",
            "123 S. Ct. 2472",
            "539 U.S. 558",
            "2003 U.S. LEXIS 5013"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lingle v. Chevron U. S. A. Inc.",
          "cluster_id": 142894,
          "cite": [
            "161 L. Ed. 2d 876",
            "125 S. Ct. 2074",
            "544 U.S. 528",
            "2005 U.S. LEXIS 4342",
            "18 Fla. L. Weekly Fed. S 303",
            "35 Envtl. L. Rep. (Envtl. Law Inst.) 20106",
            "73 U.S.L.W. 4343"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
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
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
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
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Caperton v. A. T. Massey Coal Co., Inc.",
          "cluster_id": 145867,
          "cite": [
            "173 L. Ed. 2d 1208",
            "129 S. Ct. 2252",
            "556 U.S. 868",
            "2009 U.S. LEXIS 4157",
            "39 Envtl. L. Rep. (Envtl. Law Inst.) 20125",
            "77 U.S.L.W. 4456",
            "21 Fla. L. Weekly Fed. S 908"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Geinosky v. City of Chicago",
          "cluster_id": 626218,
          "cite": [
            "675 F.3d 743",
            "86 A.L.R. 6th 713",
            "2012 U.S. App. LEXIS 6261",
            "2012 WL 1021141"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sutton v. Utah State School for the Deaf & Blind",
          "cluster_id": 157630,
          "cite": [
            "173 F.3d 1226",
            "1999 Colo. J. C.A.R. 1387",
            "1999 U.S. App. LEXIS 3159",
            "1999 WL 100895"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chavez v. Martinez",
          "cluster_id": 127927,
          "cite": [
            "155 L. Ed. 2d 984",
            "123 S. Ct. 1994",
            "538 U.S. 760",
            "2003 U.S. LEXIS 4274"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alexandra Chavarriaga v. State of NJ Department of Corr",
          "cluster_id": 3154962,
          "cite": [
            "806 F.3d 210",
            "2015 U.S. App. LEXIS 19854",
            "2015 WL 7171306"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Monterey v. Del Monte Dunes at Monterey, Ltd.",
          "cluster_id": 118291,
          "cite": [
            "143 L. Ed. 2d 882",
            "119 S. Ct. 1624",
            "526 U.S. 687",
            "1999 U.S. LEXIS 3631"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matson v. BD. OF EDUC., CITY SCHOOL DIST. OF NY",
          "cluster_id": 182561,
          "cite": [
            "631 F.3d 57",
            "31 I.E.R. Cas. (BNA) 1185",
            "23 Am. Disabilities Cas. (BNA) 1825",
            "39 Media L. Rep. (BNA) 1321",
            "2011 U.S. App. LEXIS 514",
            "2011 WL 70572"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Moreno",
          "cluster_id": 800522,
          "cite": [
            "63 M.J. 129",
            "2006 CAAF LEXIS 632",
            "2006 WL 1311865"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Sacramento v. Lewis:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118214 OR 9433650 OR 9433651 OR 9433652 OR 9433653 OR 9433654 OR 9433655) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTYwMTI0ODAwMDAwJnM9NDYyNzk3NiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118214+OR+9433650+OR+9433651+OR+9433652+OR+9433653+OR+9433654+OR+9433655%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118214 OR 9433650 OR 9433651 OR 9433652 OR 9433653 OR 9433654 OR 9433655)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NzYmcz0xMDM2OTQ0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28118214+OR+9433650+OR+9433651+OR+9433652+OR+9433653+OR+9433654+OR+9433655%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118214 OR 9433650 OR 9433651 OR 9433652 OR 9433653 OR 9433654 OR 9433655)",
        "reviewed": 111,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 111,
        "triage_read": 0,
        "triage_snippet_classified": 111
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118214 OR 9433650 OR 9433651 OR 9433652 OR 9433653 OR 9433654 OR 9433655)",
    "indexed_citing_opinions": 2439,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118214,
        "count": 2084,
        "count_source": "search"
      },
      {
        "opinion_id": 9433650,
        "count": 386,
        "count_source": "search"
      },
      {
        "opinion_id": 9433651,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433652,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433653,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433654,
        "count": 1,
        "count_source": "search"
      },
      {
        "opinion_id": 9433655,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6251,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/county-of-sacramento-v-lewis.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MDc4NzQmcz0xMDYxNDU2NiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118214+OR+9433650+OR+9433651+OR+9433652+OR+9433653+OR+9433654+OR+9433655%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118214,
        "cited_id": 85272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 91054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 103694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 105456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 108568,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 109097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 109402,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 109561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 110478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 110746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 110998,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 111555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 111556,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 111610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 111891,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 112202,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 112209,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 112218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 112295,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 112579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 112594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 112699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 112786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 112808,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 112924,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 118021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 118098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 118144,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 197095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 466102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 493644,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 549807,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 669076,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 698391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 728048,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 730829,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 744143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 745416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 1163447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 1472846,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 2620710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118214,
        "cited_id": 3224606,
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
    "date_created": "2026-07-05T01:46:12Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T01:46:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T01:46:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T01:51:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T01:46:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — County of Sacramento v. Lewis

```
<div>
<center><b><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">523 U.S. 833</a></span> (1998)</b></center>
<center><h1>COUNTY OF SACRAMENTO et al.<br>
v.<br>
LEWIS, et al.,<br>
PERSONAL REPRESENTATIVES OF THE ESTATE OF LEWIS, DECEASED</h1></center>
<center>No. 96-1337.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued December 9, 1997.</center>
<center>Decided May 26, 1998.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
<p><span class="star-pagination">*834</span> <span class="star-pagination">*835</span> Souter, J., delivered the opinion of the Court, in which Rehnquist, C. J., and O'Connor, Kennedy, Ginsburg, and Breyer, JJ., joined. Rehnquist, C. J., filed a concurring opinion, <i>post,</i> p. 855. Kennedy, J., filed a concurring opinion, in which O'Connor, J., joined, <i>post,</i> p. 856. Breyer, J., filed a concurring opinion, <i>post,</i> p. 858. Stevens, J., filed an opinion concurring in the judgment, <i>post,</i> p. 859. Scalia, J., filed an opinion concurring in the judgment, in which Thomas, J., joined, <i>post,</i>  p. 860.</p>
<p><i>Terence J. Cassidy</i> argued the cause and filed briefs for petitioners.</p>
<p><i>Paul J. Hedlund</i> argued the cause for respondents. With him on the brief was <i>Michael L. Baum.</i><sup>[*]</sup></p>
<p><span class="star-pagination">*836</span> Justice Souter, delivered the opinion of the Court.</p>
<p>The issuein this case is whether a police officer violates the Fourteenth Amendment's guarantee of substantive due process by causing death through deliberate or reckless indifference to life in a high-speed automobile chase aimed at apprehending a suspected offender. We answer no, and hold that in such circumstances only a purpose to cause harm unrelated to the legitimate object of arrest will satisfy the element of arbitrary conduct shocking to the conscience, necessary for a due process violation.</p>
<p></p>
<h2>I</h2>
<p>On May 22, 1990, at approximately 8:30 p.m., petitioner James Everett Smith, a Sacramento County sheriff's deputy, along with another officer, Murray Stapp, responded to a call to break up a fight. Upon returning to his patrol car, Stapp saw a motorcycle approaching at high speed. It was operated by 18-year-old Brian Willard and carried Philip Lewis, respondents' 16-year-old decedent, as a passenger. Neither boy had anything to do with the fight that prompted the call to the police.</p>
<p>Stapp turned on his overhead rotating lights, yelled to the boys to stop, and pulled his patrol car closer to Smith's, attempting to pen the motorcycle in. Instead of pulling over in response to Stapp's warning lights and commands, Willard <span class="star-pagination">*837</span> slowly maneuvered the motorcycle between the two police cars and sped off. Smith immediately switched on his own emergency lights and siren, made a quick turn, and began pursuit at high speed. For 75 seconds over a course of 1.3 miles in a residential neighborhood, the motorcycle wove in and out of oncoming traffic, forcing two cars and a bicycle to swerve off the road. The motorcycle and patrol car reached speeds up to 100 miles an hour, with Smith following at a distance as short as 100 feet; at that speed, his car would have required 650 feet to stop.</p>
<p>The chase ended after the motorcycle tipped over as Willard tried a sharp left turn. By the time Smith slammed on his brakes, Willard was out of the way, but Lewis was not. The patrol car skidded into him at 40 miles an hour, propelling him some 70 feet down the road and inflicting massive injuries. Lewis was pronounced dead at the scene.</p>
<p>Respondents, Philip Lewis's parents and the representatives of his estate, brought this action under Rev. Stat. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>, against petitioners Sacramento County, the Sacramento County Sheriff's Department, and Deputy Smith, alleging a deprivation of Philip Lewis's Fourteenth Amendment substantive due process right to life.<sup>[1]</sup> The District Court granted summary judgment for Smith, reasoning that even if he violated the Constitution, he was entitled to qualified immunity, because respondents could point to no "state or federal opinion published before May, 1990, when the alleged misconduct took place, that supports <span class="star-pagination">*838</span> [their] view that [the decedent had] a Fourteenth Amendment substantive due process right in the context of high speed police pursuits." App. to Pet. for Cert. 52.<sup>[2]</sup></p>
<p>The Court of Appeals for the Ninth Circuit reversed, holding that "the appropriate degree of fault to be applied to high-speed police pursuits is deliberate indifference to, or reckless disregard for, a person's right to life and personal security," <span class="citation multiple-matches"><a href="/c/F.%203d/98/434/">98 F. 3d 434</a></span>, 441 (1996), and concluding that "the law regarding police liability for death or injury caused by an officer during the course of a high-speed chase was clearly established" at the time of Philip Lewis's death, <i>id.,</i> at 445. Since Smith apparently disregarded the Sacramento County Sheriff's Department's General Order on police pursuits, the Ninth Circuit found a genuine issue of material fact that might be resolved by a finding that Smith's conduct amounted to deliberate indifference:</p>
<blockquote>"The General Order requires an officer to communicate his intention to pursue a vehicle to the sheriff's department dispatch center. But defendants concede that Smith did not contact the dispatch center. The General Order requires an officer to consider whether the seriousness of the offense warrants a chase at speeds in excess of the posted limit. But here, the only apparent `offense' was the boys' refusal to stop when another officer told them to do so. The General Order requires an officer to consider whether the need for apprehension <span class="star-pagination">*839</span> justifies the pursuit under existing conditions. Yet Smith apparently only `needed' to apprehend the boys because they refused to stop. The General Order requires an officer to consider whether the pursuit presents unreasonable hazards to life and property. But taking the facts here in the light most favorable to plaintiffs, there existed an unreasonable hazard to Lewis's and Willard's lives. The General Order also directs an officer to discontinue a pursuit when the hazards of continuing outweigh the benefits of immediate apprehension. But here, there was no apparent danger involved in permitting the boys to escape. There certainly was risk of harm to others in continuing the pursuit." <i>Id.,</i>  at 442.</blockquote>
<p>Accordingly, the Court of Appeals reversed the summary judgment in favor of Smith and remanded for trial.</p>
<p>We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./520/1250/">520 U. S. 1250</a></span> (1997), to resolve a conflict among the Circuits over the standard of culpability on the part of a law enforcement officer for violating substantive due process in a pursuit case. Compare 98 F. 3d, at 441 ("deliberate indifference" or "reckless disregard"),<sup>[3]</sup> with <i>Evans</i> v. <i>Avery,</i> <span class="citation" data-id="197095"><a href="/opinion/197095/evans-v-avery/#1038" aria-description="Citation for case: Evans v. Avery">100 F. 3d 1033, 1038</a></span> (CA1 1996) ("shocks the conscience"), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./520/1210/">520 U. S. 1210</a></span> (1997); <i>Williams</i> v. <i>Denver,</i> <span class="citation" data-id="6943026"><a href="/opinion/7040076/williams-v-city-county-of-denver/#1014" aria-description="Citation for case: Williams v. City &amp; County of Denver">99 F. 3d 1009, 1014-1015</a></span> (CA10 1996) (same); <i>Fagan</i>  v. <i>Vineland,</i> <span class="citation multiple-matches"><a href="/c/F.%203d/22/1296/">22 F. 3d 1296</a></span>, 1306-1307 (CA3 1994) (en banc) (same); <i>Temkin</i> v. <i>Frederick County Commissioners,</i> 945 <span class="star-pagination">*840</span> F. 2d 716, 720 (CA4 1991) (same), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./502/1095/">502 U. S. 1095</a></span> (1992); and <i>Checki</i> v. <i>Webb,</i> <span class="citation" data-id="466102"><a href="/opinion/466102/ron-checki-v-richard-webb/#538" aria-description="Citation for case: Ron Checki v. Richard Webb">785 F. 2d 534, 538</a></span> (CA5 1986) (same). We now reverse.</p>
<p></p>
<h2>II</h2>
<p>Our prior cases have held the provision that "[n]o State shall . . . deprive any person of life, liberty, or property, without due process of law," U. S. Const., Amdt. 14, § 1, to "guarante[e] more than fair process," <i>Washington</i> v. <i>Glucksberg,</i>  <span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/#719" aria-description="Citation for case: Washington v. Glucksberg">521 U. S. 702, 719</a></span> (1997), and to cover a substantive sphere as well, "barring certain government actions regardless of the fairness of the procedures used to implement them," <i>Daniels</i> v. <i>Williams,</i> <span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/#331" aria-description="Citation for case: Daniels v. Williams">474 U. S. 327, 331</a></span> (1986); see also <i>Zinermon</i> v. <i>Burch,</i> <span class="citation" data-id="9795096"><a href="/opinion/2620710/zinermon-v-burch/#125" aria-description="Citation for case: Zinermon v. Burch">494 U. S. 113, 125</a></span> (1990) (noting that substantive due process violations are actionable under § 1983). The allegation here that Lewis was deprived of his right to life in violation of substantive due process amounts to such a claim, that under the circumstances described earlier, Smith's actions in causing Lewis's death were an abuse of executive power so clearly unjustified by any legitimate objective of law enforcement as to be barred by the Fourteenth Amendment. Cf. <i>Collins</i> v. <i>Harker Heights,</i> <span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/#126" aria-description="Citation for case: Collins v. City of Harker Heights">503 U. S. 115, 126</a></span> (1992) (noting that the Due Process Clause was intended to prevent government officials "` "from abusing [their] power, or employing it as an instrument of oppression"` ") (quoting <i>DeShaney</i> v. <i>Winnebago County Dept. of Social Servs.,</i> <span class="citation" data-id="9431570"><a href="/opinion/112202/deshaney-v-winnebago-county-department-of-social-services/#196" aria-description="Citation for case: DeShaney v. Winnebago County Department of Social Services">489 U. S. 189, 196</a></span> (1989), in turn quoting <i>Davidson</i> v. <i>Cannon,</i> <span class="citation" data-id="9430261"><a href="/opinion/111556/davidson-v-cannon/#348" aria-description="Citation for case: Davidson v. Cannon">474 U. S. 344, 348</a></span> (1986)).<sup>[4]</sup></p>
<p><span class="star-pagination">*841</span> Leaving aside the question of qualified immunity, which formed the basis for the District Court's dismissal of their case,<sup>[5]</sup> respondents face two principal objections to their <span class="star-pagination">*842</span> claim. The first is that its subject is necessarily governed by a more definite provision of the Constitution (to the exclusion of any possible application of substantive due process); the second, that in any event the allegations are insufficient to state a substantive due process violation through executive abuse of power. Respondents can meet the first objection, but not the second.</p>
<p></p>
<h2>A</h2>
<p>Because we have "always been reluctant to expand the concept of substantive due process," <i>Collins</i> v. <span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/#125" aria-description="Citation for case: Collins v. City of Harker Heights"><i>Harker Heights, supra,</i> at 125</a></span>, we held in <i>Graham</i> v. <i>Connor,</i> <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U. S. 386</a></span> (1989), that "[w]here a particular Amendment provides an explicit textual source of constitutional protection against a particular sort of government behavior, that Amendment, not the more generalized notion of substantive due process, must be the guide for analyzing these claims." <i>Albright</i> v. <i>Oliver,</i> <span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/#273" aria-description="Citation for case: Albright v. Oliver">510 U. S. 266, 273</a></span> (1994) (plurality opinion of Rehnquist, C. J.) (quoting <i>Graham</i> v. <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#395" aria-description="Citation for case: Graham v. Connor"><i>Connor, supra,</i>  at 395</a></span>) (internal quotation marks omitted). Given the rule in <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span>,</i> we were presented at oral argument with the threshold issue raised in several <i>amicus</i> briefs,<sup>[6]</sup> whether facts involving a police chase aimed at apprehending suspects can ever support a due process claim. The argument runs that in chasing the motorcycle, Smith was attempting to make a seizure within the meaning of the Fourth Amendment, and, perhaps, even that he succeeded when Lewis was stopped by the fatal collision. Hence, any liability must turn on an application of the reasonableness standard <span class="star-pagination">*843</span> governing searches and seizures, not the due process standard of liability for constitutionally arbitrary executive action. See <i>Graham</i> v. <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#395" aria-description="Citation for case: Graham v. Connor"><i>Connor, supra,</i> at 395</a></span> ("<i>[A]ll</i> claims that law enforcement officers have used excessive force deadly or notin the course of an arrest, investigatory stop, or other `seizure' of a free citizen should be analyzed under the Fourth Amendment and its `reasonableness' standard, rather than under a `substantive due process' approach" (emphasis in original)); <i>Albright</i> v. <i>Oliver,</i> <span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/#276" aria-description="Citation for case: Albright v. Oliver">510 U. S., at 276</a></span> (Ginsburg, J., concurring); <span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/#288" aria-description="Citation for case: Albright v. Oliver"><i>id.,</i> at 288, n. 2</a></span> (Souter, J., concurring in judgment). One Court of Appeals has indeed applied the rule of <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> to preclude the application of principles of generalized substantive due process to a motor vehicle passenger's claims for injury resulting from reckless police pursuit. See <i>Mays</i> v. <i>East St. Louis,</i> <span class="citation" data-id="9490608"><a href="/opinion/745416/eddie-mays-v-city-of-east-st-louis-illinois-leland-cherry-and-victor/#1002" aria-description="Citation for case: Eddie Mays v. City of East St. Louis, Illinois, Leland...">123 F. 3d 999, 1002-1003</a></span> (CA7 1997).</p>
<p>The argument is unsound. Just last Term, we explained that <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i></p>
<blockquote>"does not hold that all constitutional claims relating to physically abusive government conduct must arise under either the Fourth or Eighth Amendments; rather, <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> simply requires that if a constitutional claim is covered by a specific constitutional provision, such as the Fourth or Eighth Amendment, the claim must be analyzed under the standard appropriate to that specific provision, not under the rubric of substantive due process." <i>United States</i> v. <i>Lanier,</i> <span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/#272" aria-description="Citation for case: United States v. Lanier">520 U. S. 259, 272, n. 7</a></span> (1997).</blockquote>
<p>Substantive due process analysis is therefore inappropriate in this case only if respondents' claim is "covered by" the Fourth Amendment. It is not.</p>
<p>The Fourth Amendment covers only "searches and seizures," neither of which took place here. No one suggests that there was a search, and our cases foreclose finding a seizure. We held in <i>California</i> v. <i>Hodari D.,</i> <span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/" aria-description="Citation for case: California v. Hodari D.">499 U. S. 621</a></span>, <span class="star-pagination">*844</span> 626 (1991), that a police pursuit in attempting to seize a person does not amount to a "seizure" within the meaning of the Fourth Amendment. And in <i>Brower</i> v. <i>County of Inyo,</i>  <span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/#596" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo">489 U. S. 593, 596-597</a></span> (1989), we explained that "a Fourth Amendment seizure does not occur whenever there is a governmentally caused termination of an individual's freedom of movement (the innocent passerby), nor even whenever there is a governmentally caused and governmentally <i>desired</i> termination of an individual's freedom of movement (the fleeing felon), but only when there is a governmental termination of freedom of movement <i>through means intentionally applied.</i> " We illustrated the point by saying that no Fourth Amendment seizure would take place where a "pursuing police car sought to stop the suspect only by the show of authority represented by flashing lights and continuing pursuit," but accidentally stopped the suspect by crashing into him. <span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/#597" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo"><i>Id.,</i> at 597</a></span>. That is exactly this case. See, <i>e. g., </i><i>Campbell</i> v. <i>White,</i> <span class="citation" data-id="549807"><a href="/opinion/549807/james-campbell-and-lois-campbell-as-co-administrators-for-the-estate-of/#423" aria-description="Citation for case: James Campbell and Lois Campbell, as Co-Administrators...">916 F. 2d 421, 423</a></span> (CA7 1990) (following <i>Brower</i> and finding no seizure where a police officer accidentally struck and killed a fleeing motorcyclist during a high-speed pursuit), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./499/922/">499 U. S. 922</a></span> (1991). <i>Graham</i> `s more-specific-provision rule is therefore no bar to respondents' suit. See, <i>e. g., </i><i>Frye</i> v. <i>Akron,</i> <span class="citation" data-id="1472846"><a href="/opinion/1472846/frye-v-town-of-akron/#1324" aria-description="Citation for case: Frye v. Town of Akron">759 F. Supp. 1320, 1324</a></span> (ND Ind. 1991) (parents of a motorcyclist who was struck and killed by a police car during a high-speed pursuit could sue under substantive due process because no Fourth Amendment seizure took place); <i>Evans</i> v. <i>Avery,</i> <span class="citation" data-id="197095"><a href="/opinion/197095/evans-v-avery/#1036" aria-description="Citation for case: Evans v. Avery">100 F. 3d, at 1036</a></span> (noting that "outside the context of a seizure, . . . a person injured as a result of police misconduct may prosecute a substantive due process claim under section 1983"); <i>Pleasant</i> v. <i>Zamieski,</i> <span class="citation" data-id="9479969"><a href="/opinion/536074/anna-pleasant-personal-representative-of-the-estate-of-jeffrey-pleasant/#276" aria-description="Citation for case: Anna Pleasant, Personal Representative of the Estate of...">895 F. 2d 272, 276, n. 2</a></span> (CA6) (noting that <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> "preserve[s] fourteenth amendment substantive due process analysis for those instances in which a free citizen is denied his or her constitutional right to life through means other than a law enforcement official's arrest, investigatory <span class="star-pagination">*845</span> stop or other seizure"), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./498/851/">498 U. S. 851</a></span> (1990).<sup>[7]</sup></p>
<p></p>
<h2>B</h2>
<p>Since the time of our early explanations of due process, we have understood the core of the concept to be protection against arbitrary action:</p>
<blockquote>"The principal and true meaning of the phrase has never been more tersely or accurately stated than by Mr. Justice Johnson, in <i>Bank of Columbia</i> v. <i>Okely,</i> <span class="citation" data-id="85266"><a href="/opinion/85266/somervilles-executors-v-hamilton/" aria-description="Citation for case: Somerville&#x27;s Executors v. Hamilton">4 Wheat. 235</a></span>-244 [(1819)]: `As to the words from Magna Charta, incorporated into the Constitution of Maryland, after volumes spoken and written with a view to their exposition, the good sense of mankind has at last settled down to this: that they were intended to secure the individual from the arbitrary exercise of the powers of government, unrestrained by the established principles of private right and distributive justice.' " <i>Hurtado</i> v. <i>California,</i> <span class="citation" data-id="9417375"><a href="/opinion/91054/hurtado-v-california/#527" aria-description="Citation for case: Hurtado v. California">110 U. S. 516, 527</a></span> (1884).</blockquote>
<p>We have emphasized time and again that "[t]he touchstone of due process is protection of the individual against arbitrary action of government," <i>Wolff</i> v. <i>McDonnell,</i> <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#558" aria-description="Citation for case: Wolff v. McDonnell">418 U. S. 539, 558</a></span> (1974), whether the fault lies in a denial of fundamental <span class="star-pagination">*846</span> procedural fairness, see, <i>e. g., </i><i>Fuentes</i> v. <i>Shevin,</i> <span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#82" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67, 82</a></span> (1972) (the procedural due process guarantee protects against "arbitrary takings"), or in the exercise of power without any reasonable justification in the service of a legitimate governmental objective, see, <i>e. g., </i><i>Daniels</i> v. <i>Williams,</i>  <span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/#331" aria-description="Citation for case: Daniels v. Williams">474 U. S., at 331</a></span> (the substantive due process guarantee protects against government power arbitrarily and oppressively exercised). While due process protection in the substantive sense limits what the government may do in both its legislative, see, <i>e. g., </i><i>Griswold</i> v. <i>Connecticut,</i> <span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/" aria-description="Citation for case: Griswold v. Connecticut">381 U. S. 479</a></span> (1965), and its executive capacities, see, <i>e. g., </i><i>Rochin</i> v. <i>California,</i>  <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952), criteria to identify what is fatally arbitrary differ depending on whether it is legislation or a specific act of a governmental officer that is at issue.</p>
<p>Our cases dealing with abusive executive action have repeatedly emphasized that only the most egregious official conduct can be said to be "arbitrary in the constitutional sense," <i>Collins</i> v. <i>Harker Heights,</i> <span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/#129" aria-description="Citation for case: Collins v. City of Harker Heights">503 U. S., at 129</a></span>, thereby recognizing the point made in different circumstances by Chief Justice Marshall, "`that it is <i>a constitution</i> we are expounding,' " <i>Daniels</i> v. <i>Williams, supra,</i> at 332 (quoting <i>McCulloch</i> v. <i>Maryland,</i> <span class="citation" data-id="85272"><a href="/opinion/85272/mculloch-v-state-of-maryland/#407" aria-description="Citation for case: M&#x27;culloch v. State of Maryland">4 Wheat. 316, 407</a></span> (1819) (emphasis in original)). Thus, in <i>Collins</i> v. <i><span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/" aria-description="Citation for case: Collins v. City of Harker Heights">Harker Heights</a></span></i><i>,</i> for example, we said that the Due Process Clause was intended to prevent government officials "` "from abusing [their] power, or employing it as an instrument of oppression."` " <span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/" aria-description="Citation for case: Collins v. City of Harker Heights">503 U. S., at 126</a></span> (quoting <i>DeShaney</i> v. <i>Winnebago County Dept. of Social Servs.,</i> 489 U. S., at 196, in turn quoting <i>Davidson</i> v. <i>Cannon,</i>  <span class="citation" data-id="9430261"><a href="/opinion/111556/davidson-v-cannon/#348" aria-description="Citation for case: Davidson v. Cannon">474 U. S., at 348</a></span>).</p>
<p>To this end, for half a century now we have spoken of the cognizable level of executive abuse of power as that which shocks the conscience. We first put the test this way in <i>Rochin</i> v. <i>California, supra,</i> at 172-173, where we found the forced pumping of a suspect's stomach enough to offend due process as conduct "that shocks the conscience" and violates the "decencies of civilized conduct." In the intervening <span class="star-pagination">*847</span> years we have repeatedly adhered to <i><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span></i> `s benchmark. See, <i>e. g., </i><i>Breithaupt</i> v. <i>Abram,</i> <span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#435" aria-description="Citation for case: Breithaupt v. Abram">352 U. S. 432, 435</a></span> (1957) (reiterating that conduct that "`shocked the conscience' and was so `brutal' and `offensive' that it did not comport with traditional ideas of fair play and decency" would violate substantive due process); <i>Whitley</i> v. <i>Albers,</i> <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#327" aria-description="Citation for case: Whitley v. Albers">475 U. S. 312, 327</a></span> (1986) (same); <i>United States</i> v. <i>Salerno,</i> <span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/#746" aria-description="Citation for case: United States v. Salerno">481 U. S. 739, 746</a></span> (1987) ("So-called `substantive due process' prevents the government from engaging in conduct that `shocks the conscience,'. . . or interferes with rights `implicit in the concept of ordered liberty' ") (quoting <i>Rochin</i> v. <i>California, supra,</i> at 172, and <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319, 325-326</a></span> (1937)). Most recently, in <i>Collins</i> v. <span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/#128" aria-description="Citation for case: Collins v. City of Harker Heights"><i>Harker Heights, supra,</i> at 128</a></span>, we said again that the substantive component of the Due Process Clause is violated by executive action only when it "can properly be characterized as arbitrary, or conscience shocking, in a constitutional sense." While the measure of what is conscience shocking is no calibrated yard stick, it does, as Judge Friendly put it, "poin[t] the way." <i>Johnson</i>  v. <i>Glick,</i> <span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/#1033" aria-description="Citation for case: Johnson v. Glick">481 F. 2d 1028, 1033</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1033/">414 U. S. 1033</a></span> (1973).<sup>[8]</sup></p>
<p><span class="star-pagination">*848</span> It should not be surprising that the constitutional concept of conscience shocking duplicates no traditional category of common-law fault, but rather points clearly away from liability, or clearly toward it, only at the ends of the tort law's spectrum of culpability. Thus, we have made it clear that the due process guarantee does not entail a body of constitutional law imposing liability whenever someone cloaked with state authority causes harm. In <i>Paul</i> v. <i>Davis,</i> <span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/#701" aria-description="Citation for case: Paul v. Davis">424 U. S. 693, 701</a></span> (1976), for example, we explained that the Fourteenth Amendment is not a "font of tort law to be superimposed upon whatever systems may already be administered by the States," and in <i>Daniels</i> v. <i>Williams,</i> <span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/#332" aria-description="Citation for case: Daniels v. Williams">474 U. S., at 332</a></span>, we reaffirmed the point that "[o]ur Constitution deals with the large concerns of the governors and the governed, but it does not purport to supplant traditional tort law in laying down rules of conduct to regulate liability for injuries that attend living together in society." We have accordingly rejected the lowest common denominator of customary tort liability <span class="star-pagination">*849</span> as any mark of sufficiently shocking conduct, and have held that the Constitution does not guarantee due care on the part of state officials; liability for negligently inflicted harm is categorically beneath the threshold of constitutional due process. See <span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/#328" aria-description="Citation for case: Daniels v. Williams"><i>id.,</i> at 328</a></span>; see also <i>Davidson</i> v. <i>Cannon,</i>  <span class="citation" data-id="9430261"><a href="/opinion/111556/davidson-v-cannon/#348" aria-description="Citation for case: Davidson v. Cannon">474 U. S., at 348</a></span> (clarifying that <i><span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/" aria-description="Citation for case: Daniels v. Williams">Daniels</a></span></i> applies to substantive, as well as procedural, due process). It is, on the contrary, behavior at the other end of the culpability spectrum that would most probably support a substantive due process claim; conduct intended to injure in some way unjustifiable by any government interest is the sort of official action most likely to rise to the conscience-shocking level. See <i>Daniels</i>  v. <i>Williams,</i> <span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/#331" aria-description="Citation for case: Daniels v. Williams">474 U. S., at 331</a></span> ("Historically, this guarantee of due process has been applied to <i>deliberate</i> decisions of government officials to deprive a person of life, liberty, or property" (emphasis in original)).</p>
<p>Whether the point of the conscience shocking is reached when injuries are produced with culpability falling within the middle range, following from something more than negligence but "less than intentional conduct, such as recklessness or `gross negligence,' " <span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/#334" aria-description="Citation for case: Daniels v. Williams"><i>id.,</i> at 334, n. 3</a></span>, is a matter for closer calls.<sup>[9]</sup> To be sure, we have expressly recognized the possibility that some official acts in this range may be actionable under the Fourteenth Amendment, <i>ibid.,</i> and our cases have compelled recognition that such conduct is egregious enough to state a substantive due process claim in at least one instance. We held in <i>City of Revere</i> v. <i>Massachusetts Gen. Hospital,</i> <span class="citation" data-id="9429305"><a href="/opinion/110998/city-of-revere-v-massachusetts-general-hospital/" aria-description="Citation for case: City of Revere v. Massachusetts General Hospital">463 U. S. 239</a></span> (1983), that "the due process rights of a [pretrial detainee] are at least as great as the <span class="star-pagination">*850</span> Eighth Amendment protections available to a convicted prisoner." <i><span class="citation" data-id="9429305"><a href="/opinion/110998/city-of-revere-v-massachusetts-general-hospital/" aria-description="Citation for case: City of Revere v. Massachusetts General Hospital">Id.,</a></span></i> at 244 (citing <i>Bell</i> v. <i>Wolfish,</i> <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#535" aria-description="Citation for case: Bell v. Wolfish">441 U. S. 520, 535, n. 16, 545</a></span> (1979)). Since it may suffice for Eighth Amendment liability that prison officials were deliberately indifferent to the medical needs of their prisoners, see <i>Estelle</i> v. <i>Gamble,</i> <span class="citation" data-id="9426610"><a href="/opinion/109561/estelle-v-gamble/#104" aria-description="Citation for case: Estelle v. Gamble">429 U. S. 97, 104</a></span> (1976), it follows that such deliberately indifferent conduct must also be enough to satisfy the fault requirement for due process claims based on the medical needs of someone jailed while awaiting trial, see, <i>e. g., </i><i>Barrie</i> v. <i>Grand County, Utah,</i> <span class="citation" data-id="9436928"><a href="/opinion/155087/barrie-v-grand-county-utah/#867" aria-description="Citation for case: Barrie v. Grand County, Utah">119 F. 3d 862, 867</a></span> (CA10 1997); <i>Weyant</i> v. <i>Okst,</i> <span class="citation" data-id="730829"><a href="/opinion/730829/weyant-v-okst/#856" aria-description="Citation for case: Weyant v. Okst">101 F. 3d 845, 856</a></span> (CA2 1996).<sup>[10]</sup></p>
<p>Rules of due process are not, however, subject to mechanical application in unfamiliar territory. Deliberate indifference that shocks in one environment may not be so patently egregious in another, and our concern with preserving the constitutional proportions of substantive due process demands an exact analysis of circumstances before any abuse of power is condemned as conscience shocking. What we have said of due process in the procedural sense is just as true here:</p>
<blockquote>"The phrase [due process of law] formulates a concept less rigid and more fluid than those envisaged in other specific and particular provisions of the Bill of Rights. Its application is less a matter of rule. Asserted denial is to be tested by an appraisal of the totality of facts in a given case. That which may, in one setting, constitute a denial of fundamental fairness, shocking to the universal sense of justice, may, in other circumstances, and in the light of other considerations, fall short of such denial." <i>Betts</i> v. <i>Brady,</i> <span class="citation" data-id="103694"><a href="/opinion/103694/betts-v-brady/#462" aria-description="Citation for case: Betts v. Brady">316 U. S. 455, 462</a></span> (1942).</blockquote>
<p><span class="star-pagination">*851</span> Thus, attention to the markedly different circumstances of normal pretrial custody and high-speed law enforcement chases shows why the deliberate indifference that shocks in the one case is less egregious in the other (even assuming that it makes sense to speak of indifference as deliberate in the case of sudden pursuit). As the very term "deliberate indifference" implies, the standard is sensibly employed only when actual deliberation is practical, see <i>Whitley</i> v. <i>Albers,</i>  <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#320" aria-description="Citation for case: Whitley v. Albers">475 U. S., at 320</a></span>,<sup>[11]</sup> and in the custodial situation of a prison, forethought about an inmate's welfare is not only feasible but obligatory under a regime that incapacitates a prisoner to exercise ordinary responsibility for his own welfare.</p>
<blockquote>"[W]hen the State takes a person into its custody and holds him there against his will, the Constitution imposes upon it a corresponding duty to assume some responsibility for his safety and general well-being. The rationale for this principle is simple enough: when the State by the affirmative exercise of its power so restrains an individual's liberty that it renders him unable to care for himself, and at the same time fails to provide for his basic human needs<i>e. g.,</i> food, clothing, shelter, medical care, and reasonable safetyit transgresses the substantive limits on state action set by the . . . Due Process Clause." <i>DeShaney</i> v. <i>Winnebago County Dept.</i>  <i>of Social Servs.,</i> 489 U. S., at 199-200 (citation and footnote omitted).</blockquote>
<p>Nor does any substantial countervailing interest excuse the State from making provision for the decent care and protection of those it locks up; "the State's responsibility to attend <span class="star-pagination">*852</span> to the medical needs of prisoners [or detainees] does not ordinarily clash with other equally important governmental responsibilities." <i>Whitley</i> v. <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#320" aria-description="Citation for case: Whitley v. Albers"><i>Albers, supra,</i> at 320</a></span>.<sup>[12]</sup></p>
<p>But just as the description of the custodial prison situation shows how deliberate indifference can rise to a constitutionally shocking level, so too does it suggest why indifference may well not be enough for liability in the different circumstances of a case like this one. We have, indeed, found that deliberate indifference does not suffice for constitutional liability (albeit under the Eighth Amendment) even in prison circumstances when a prisoner's claim arises not from normal custody but from response to a violent disturbance. Our analysis is instructive here:</p>
<blockquote>"[I]n making and carrying out decisions involving the use of force to restore order in the face of a prison disturbance, prison officials undoubtedly must take into account the very real threats the unrest presents to inmates and prison officials alike, in addition to the possible harms to inmates against whom force might be used. . . . In this setting, a deliberate indifference standard does not adequately capture the importance of such competing obligations, or convey the appropriate hesitancy to critique in hindsight decisions necessarily made in haste, under pressure, and frequently without the luxury of a second chance." <i>Whitley</i> v. <i>Albers,</i> <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#320" aria-description="Citation for case: Whitley v. Albers">475 U. S., at 320</a></span>.</blockquote>
<p>We accordingly held that a much higher standard of fault than deliberate indifference has to be shown for officer liability <span class="star-pagination">*853</span> in a prison riot. In those circumstances, liability should turn on "whether force was applied in a good faith effort to maintain or restore discipline or maliciously and sadistically for the very purpose of causing harm." <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#320" aria-description="Citation for case: Whitley v. Albers"><i>Id.,</i> at 320-321</a></span> (internal quotation marks omitted). The analogy to sudden police chases (under the Due Process Clause) would be hard to avoid.</p>
<p>Like prison officials facing a riot, the police on an occasion calling for fast action have obligations that tend to tug against each other. Their duty is to restore and maintain lawful order, while not exacerbating disorder more than necessary to do their jobs. They are supposed to act decisively and to show restraint at the same moment, and their decisions have to be made "in haste, under pressure, and frequently without the luxury of a second chance." <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#320" aria-description="Citation for case: Whitley v. Albers"><i>Id.,</i> at 320</a></span>; cf. <i>Graham</i> v. <i>Connor,</i> <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#397" aria-description="Citation for case: Graham v. Connor">490 U. S., at 397</a></span> ("[P]olice officers are often forced to make split-second judgmentsin circumstances that are tense, uncertain, and rapidly evolving"). A police officer deciding whether to give chase must balance on one hand the need to stop a suspect and show that flight from the law is no way to freedom, and, on the other, the highspeed threat to all those within stopping range, be they suspects, their passengers, other drivers, or bystanders.</p>
<p>To recognize a substantive due process violation in these circumstances when only mid level fault has been shown would be to forget that liability for deliberate indifference to inmate welfare rests upon the luxury enjoyed by prison officials of having time to make unhurried judgments, upon the chance for repeated reflection, largely uncomplicated by the pulls of competing obligations. When such extended opportunities to do better are teamed with protracted failure even to care, indifference is truly shocking. But when unforeseen circumstances demand an officer's instant judgment, even precipitate recklessness fails to inch close enough to harmful purpose to spark the shock that implicates "the large concerns of the governors and the governed." <i>Daniels</i> v. <i>Wil-</i>  <span class="star-pagination">*854</span> <i>liams,</i> <span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/#332" aria-description="Citation for case: Daniels v. Williams">474 U. S., at 332</a></span>. Just as a purpose to cause harm is needed for Eighth Amendment liability in a riot case, so it ought to be needed for due process liability in a pursuit case. Accordingly, we hold that high-speed chases with no intent to harm suspects physically or to worsen their legal plight do not give rise to liability under the Fourteenth Amendment, redressible by an action under § 1983.<sup>[13]</sup></p>
<p>The fault claimed on Smith's part in this case accordingly fails to meet the shocks-the-conscience test. In the count charging him with liability under § 1983, respondents' complaint alleges a variety of culpable states of mind: "negligently responsible in some manner," App. 11, Count one, ¶ 8, "reckless and careless," <i>id.,</i> at 12, ¶15, "recklessness, gross negligence and conscious disregard for [Lewis's] safety," <i>id.,</i>  at 13, ¶18, and "oppression, fraud and malice," <i>ibid.</i> The subsequent summary judgment proceedings revealed that the height of the fault actually claimed was "conscious disregard," the malice allegation having been made in aid of a request for punitive damages, but unsupported either in allegations of specific conduct or in any affidavit of fact offered on the motions for summary judgment. The Court of Appeals understood the claim to be one of deliberate indifference to Lewis's survival, which it treated as equivalent to one of reckless disregard for life. We agree with this reading of respondents' allegations, but consequently part company from the Court of Appeals, which found them sufficient to state a substantive due process claim, and from the District Court, which made the same assumption <i>arguendo.</i><sup>[14]</sup></p>
<p><span class="star-pagination">*855</span> Smith was faced with a course of lawless behavior for which the police were not to blame. They had done nothing to cause Willard's high-speed driving in the first place, nothing to excuse his flouting of the commonly understood law enforcement authority to control traffic, and nothing (beyond a refusal to call off the chase) to encourage him to race through traffic at breakneck speed forcing other drivers out of their travel lanes. Willard's outrageous behavior was practically instantaneous, and so was Smith's instinctive response. While prudence would have repressed the reaction, the officer's instinct was to do his job as a law enforcement officer, not to induce Willard's lawlessness, or to terrorize, cause harm, or kill. Prudence, that is, was subject to countervailing enforcement considerations, and while Smith exaggerated their demands, there is no reason to believe that they were tainted by an improper or malicious motive on his part.</p>
<p>Regardless whether Smith's behavior offended the reasonableness held up by tort law or the balance struck in law enforcement's own codes of sound practice, it does not shock the conscience, and petitioners are not called upon to answer for it under § 1983. The judgment below is accordingly reversed.</p>
<p><i>It is so ordered.</i></p>
<p>Chief Justice Rehnquist, concurring.</p>
<p>I join the opinion of the Court in this case. The first question presented in the county's petition for certiorari is:</p>
<blockquote>"Whether, in a police pursuit case, the legal standard of conduct necessary to establish a violation of substantive <span class="star-pagination">*856</span> due process under the Fourteenth Amendment is `shocks the conscience'. . . or is `deliberate indifference' or `reckless disregard.' " Pet. for Cert. i.</blockquote>
<p>The county's petition assumed that the constitutional question was one of substantive due process, and the parties briefed the question on that assumption. The assumption was surely not without foundation in our case law, as the Court makes clear. <i>Ante,</i> at 846-847. The Court is correct in concluding that "shocks the conscience" is the right choice among the alternatives posed in the question presented, and correct in concluding that this demanding standard has not been met here.</p>
<p>Justice Kennedy, with whom Justice O'Connor joins, concurring.</p>
<p>I join the opinion of the Court, and write this explanation of the objective character of our substantive due process analysis.</p>
<p>The Court is correct, of course, in repeating that the prohibition against deprivations of life, liberty, or property contained in the Due Process Clause of the Fourteenth Amendment extends beyond the command of fair procedures. It can no longer be controverted that due process has a substantive component as well. See, <i>e. g., </i><i>Washington</i> v. <i>Glucksberg,</i> <span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">521 U. S. 702</a></span> (1997); <i>Planned Parenthood of Southeastern Pa.</i> v<i>. Casey,</i> <span class="citation" data-id="9432680"><a href="/opinion/112786/planned-parenthood-of-southeastern-pa-v-casey/" aria-description="Citation for case: Planned Parenthood of Southeastern Pa. v. Casey">505 U. S. 833</a></span> (1992); <i>Collins</i> v<i>. Harker Heights,</i> <span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/#125" aria-description="Citation for case: Collins v. City of Harker Heights">503 U. S. 115, 125-128</a></span> (1992); <i>Michael H.</i> v. <i>Gerald D.,</i> <span class="citation" data-id="9431740"><a href="/opinion/112295/michael-h-v-gerald-d/" aria-description="Citation for case: Michael H. v. Gerald D.">491 U. S. 110</a></span> (1989). As a consequence, certain actions are prohibited no matter what procedures attend them. In the case before us, there can be no question that an interest protected by the text of the Constitution is implicated: The actions of the State were part of a causal chain resulting in the undoubted loss of life. We have no definitional problem, then, in determining whether there is an interest sufficient to invoke due process. Cf. <i>Ohio Adult Parole Authority</i> v. <i>Woodard, ante,</i> p. 272.</p>
<p><span class="star-pagination">*857</span> What we do confront is the question of the standard of conduct the Constitution requires the State, in this case the local police, to follow to protect against the unintentional taking of life in the circumstances of a police pursuit. Unlike the separate question whether or not, given the fact of a constitutional violation, the state entity is liable for damages, see <i>Monell</i> v. <i>New York City Dept. of Social Servs.,</i>  <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658, 694-695</a></span> (1978); <i>Canton</i> v. <i>Harris,</i> <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">489 U. S. 378</a></span> (1989), which is a matter of statutory interpretation or elaboration, the question here is the distinct, anterior issue whether or not a constitutional violation occurred at all. See <i>Collins</i> v. <span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/#120" aria-description="Citation for case: Collins v. City of Harker Heights"><i>Harker Heights, supra,</i> at 120, 124</a></span>.</p>
<p>The Court decides this case by applying the "shocks the conscience" test first recognized in <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#172" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 172-173</a></span> (1952), and reiterated in subsequent decisions. The phrase has the unfortunate connotation of a standard laden with subjective assessments. In that respect, it must be viewed with considerable skepticism. As our opinion in <i>Collins</i> v. <i><span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/" aria-description="Citation for case: Collins v. City of Harker Heights">Harker Heights</a></span></i> illustrates, however, the test can be used to mark the beginning point in asking whether or not the objective character of certain conduct is consistent with our traditions, precedents, and historical understanding of the Constitution and its meaning. <span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/#126" aria-description="Citation for case: Collins v. City of Harker Heights">503 U. S., at 126-128</a></span>. As Justice Scalia is correct to point out, we so interpreted the test in <i>Glucksberg. Post,</i> at 860 861 (opinion concurring in judgment). In the instant case, the authorities cited by Justice Scalia are persuasive, indicating that we would contradict our traditions were we to sustain the claims of the respondents.</p>
<p>That said, it must be added that history and tradition are the starting point but not in all cases the ending point of the substantive due process inquiry. There is room as well for an objective assessment of the necessities of law enforcement, in which the police must be given substantial latitude and discretion, acknowledging, of course, the primacy of the interest in life which the State, by the Fourteenth Amendment, <span class="star-pagination">*858</span> is bound to respect. I agree with the Court's assessment of the State's interests in this regard. Absent intent to injure, the police, in circumstances such as these, may conduct a dangerous chase of a suspect who disobeys a lawful command to stop when they determine it is appropriate to do so. There is a real danger in announcing a rule, or suggesting a principle, that in some cases a suspect is free to ignore a lawful police command to stop. No matter how narrow its formulation, any suggestion that suspects may ignore a lawful command to stop and then sue for damages sustained in an ensuing chase might cause suspects to flee more often, increasing accidents of the kind which occurred here.</p>
<p>Though I share Justice Scalia's concerns about using the phrase "shocks the conscience" in a manner suggesting that it is a self-defining test, the reasons the Court gives in support of its judgment go far toward establishing that objective considerations, including history and precedent, are the controlling principle, regardless of whether the State's action is legislative or executive in character. To decide this case, we need not attempt a comprehensive definition of the level of causal participation which renders a State or its officers liable for violating the substantive commands of the Fourteenth Amendment. It suffices to conclude that neither our legal traditions nor the present needs of law enforcement justify finding a due process violation when unintended injuries occur after the police pursue a suspect who disobeys their lawful order to stop.</p>
<p>Justice Breyer, concurring.</p>
<p>I join the Court's judgment and opinion. I write separately only to point out my agreement with Justice Stevens, <i>post,</i> at 859, that <i>Siegert</i> v. <i>Gilley,</i> <span class="citation" data-id="9432276"><a href="/opinion/112594/siegert-v-gilley/" aria-description="Citation for case: Siegert v. Gilley">500 U. S. 226</a></span> (1991), should not be read to deny lower courts the flexibility, in appropriate cases, to decide <span class="citation no-link">42 U. S. C. § 1983</span> claims on the basis of qualified immunity, and thereby avoid wrestling with <span class="star-pagination">*859</span> constitutional issues that are either difficult or poorly presented. See <span class="citation" data-id="9432276"><a href="/opinion/112594/siegert-v-gilley/#235" aria-description="Citation for case: Siegert v. Gilley"><i>Siegert, supra,</i> at 235</a></span> (Kennedy, J., concurring) (lower court "adopted the altogether normal procedure of deciding the case before it on the ground that appeared to offer the most direct and appropriate resolution, and one argued by the parties").</p>
<p>Justice Stevens, concurring in the judgment.</p>
<p>When defendants in a <span class="citation no-link">42 U. S. C. § 1983</span> action argue in the alternative (a) that they did not violate the Constitution, and (b) that in any event they are entitled to qualified immunity because the constitutional right was not clearly established, the opinion in <i>Siegert</i> v. <i>Gilley,</i> <span class="citation" data-id="9432276"><a href="/opinion/112594/siegert-v-gilley/" aria-description="Citation for case: Siegert v. Gilley">500 U. S. 226</a></span> (1991), tells us that we should address the constitutional question at the outset. That is sound advice when the answer to the constitutional question is clear. When, however, the question is both difficult and unresolved, I believe it wiser to adhere to the policy of avoiding the unnecessary adjudication of constitutional questions. Because I consider this such a case, I would reinstate the judgment of the District Court on the ground that the relevant law was not clearly defined in 1990.</p>
<p>The Court expresses concern that deciding the immunity issue without resolving the underlying constitutional question would perpetuate a state of uncertainty in the law. <i>Ante,</i> at 841-842, n. 5. Yet the Court acknowledges, as it must, that a qualified immunity defense is unavailable in an action against the municipality itself. <i><span class="citation" data-id="9432276"><a href="/opinion/112594/siegert-v-gilley/" aria-description="Citation for case: Siegert v. Gilley">Ibid.</a></span></i> Sound reasons exist for encouraging the development of new constitutional doctrines in adversarial suits against municipalities, which have a substantial stake in the outcome and a risk of exposure to damages liability even when individual officers are plainly protected by qualified immunity.</p>
<p>In sum, I would hold that Officer Smith is entitled to qualified immunity. Accordingly, I concur in the Court's judgment, but I do not join its opinion.</p>
<p><span class="star-pagination">*860</span> Justice Scalia, with whom Justice Thomas joins, concurring in the judgment.</p>
<p>Today's opinion gives the lie to those cynics who claim that changes in this Court's jurisprudence are attributable to changes in the Court's membership. It proves that the changes are attributable to nothing but the passage of time (not much time, at that), plus application of the ancient maxim, "That was then, this is now."</p>
<p>Just last Term, in <i>Washington</i> v. <i>Glucksberg,</i> <span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/#720" aria-description="Citation for case: Washington v. Glucksberg">521 U. S. 702, 720-722</a></span> (1997), the Court specifically rejected the method of substantive-due-process analysis employed by Justice Souter in his concurrence in that case, which is the very same method employed by Justice Souter in his opinion for the Court today. To quote the opinion in <i><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">Glucksberg</a></span>:</i></p>
<blockquote>"Our established method of substantive-due-process analysis has two primary features: First, we have regularly observed that the Due Process Clause specially protects those fundamental rights and liberties which are, objectively, `deeply rooted in this Nation's history and tradition,' . . . and `implicit in the concept of ordered liberty' . . . . Second, we have required in substantivedue-process cases a `careful description' of the asserted fundamental liberty interest. . . . Our Nation's history, legal traditions, and practices thus provide the crucial `guideposts for responsible decision making,' . . . that direct and restrain our exposition of the Due Process Clause. . . .</blockquote>
<blockquote>"Justice Souter . . . would largely abandon this restrained methodology, and instead ask `whether [Washington's] statute sets up one of those "arbitrary impositions" or "purposeless restraints" at odds with the Due Process Clause . . . ` [citations and footnote omitted]. In our view, however, the development of this Court's substantive-due-process jurisprudence . . . has been a process whereby the outlines of the `liberty' specially protected by the Fourteenth Amendment . . . have at <span class="star-pagination">*861</span> least been carefully refined by concrete examples involving fundamental rights found to be deeply rooted in our legal tradition. This approach tends to rein in the subjective elements that are necessarily present in due process judicial review." <span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/#720" aria-description="Citation for case: Washington v. Glucksberg"><i>Id.,</i> at 720-722</a></span>.</blockquote>
<p>Today, so to speak, the stone that the builders had rejected has become the foundation stone of our substantive-dueprocess jurisprudence. The atavistic methodology that Justice Souter announces for the Court is the very same methodology that the Court called atavistic when it was proffered by Justice Souter in <i><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">Glucksberg</a></span>.</i> In fact, if anything, today's opinion is even more of a throwback to highly subjective substantive-due-process methodologies than the concurrence in <i><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">Glucksberg</a></span></i> was. Whereas the latter said merely that substantive due process prevents "arbitrary impositions" and "purposeless restraints" (without any objective criterion as to what is arbitrary or purposeless), today's opinion resuscitates the <i>one plus ultra,</i> the Napoleon Brandy, the Mahatma Gandhi, the Cellophane<sup>[1]</sup> of subjectivity, th' ol' "shocks-the-conscience" test. According to today's opinion, this is the <i>measure</i> of arbitrariness when what is at issue is executive, rather than legislative, action. <i>Ante,</i> at 846-847.<sup>[2]</sup><span class="star-pagination">*862</span> <i><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">Glucksberg</a></span>,</i> of course, rejected "shocks-the-conscience," just as it rejected the less subjective "arbitrary action" test. A 1992 executive-action case, <i>Collins</i> v. <i>Harker Heights,</i>  <span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/" aria-description="Citation for case: Collins v. City of Harker Heights">503 U. S. 115</a></span>, which had paid lipservice to "shocks-theconscience," see <span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/#128" aria-description="Citation for case: Collins v. City of Harker Heights"><i>id.,</i> at 128</a></span>, was cited in <i><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">Glucksberg</a></span></i> for the proposition that "[o]ur Nation's history, legal traditions, and practices . . . provide the crucial `guide posts for responsible decision making.' " <span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/#721" aria-description="Citation for case: Washington v. Glucksberg">521 U. S., at 721</a></span>, quoting <span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/#125" aria-description="Citation for case: Collins v. City of Harker Heights"><i>Collins, supra,</i>  at 125</a></span>. In fact, even before <i><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">Glucksberg</a></span></i> we had characterized the last "shocks-the-conscience" claim to come before us as "nothing more than [a] bald assertio[n]," and had rejected it on the objective ground that the petitioner "failed to proffer any historical, textual, or controlling precedential support for [his alleged due process right], and we decline to fashion a new due process right out of thin air." <i>Carlisle</i> v. <i>United States,</i> <span class="citation" data-id="9433281"><a href="/opinion/118021/carlisle-v-united-states/#429" aria-description="Citation for case: Carlisle v. United States">517 U. S. 416, 429</a></span> (1996).</p>
<p>Adhering to our decision in <i><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">Glucksberg</a></span>,</i> rather than ask whether the police conduct here at issue shocks my unelected conscience, I would ask whether our Nation has traditionally protected the right respondents assert. The first step of our analysis, of course, must be a "careful description" of the right asserted, <span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/#721" aria-description="Citation for case: Washington v. Glucksberg"><i>Glucksberg, supra,</i> at 721</a></span>. Here the complaint alleges that the police officer deprived Lewis "of his Fourteenth Amendment right to life, liberty and property without due process of law when he operated his vehicle with recklessness, gross negligence and conscious disregard for his safety." App. 13. I agree with the Court's conclusion that this asserts a substantive right to be free from "deliberate or reckless indifference to life in a high-speed automobile chase aimed at apprehending a suspected offender." <i>Ante,</i> at 836; see also <i>ante,</i> at 853.</p>
<p>Respondents provide no textual or historical support for this alleged due process right, and, as in <i><span class="citation" data-id="9433281"><a href="/opinion/118021/carlisle-v-united-states/" aria-description="Citation for case: Carlisle v. United States">Carlisle</a></span>,</i> I would "decline to fashion a new due process right out of thin air." <span class="citation" data-id="9433281"><a href="/opinion/118021/carlisle-v-united-states/#429" aria-description="Citation for case: Carlisle v. United States">517 U. S., at 429</a></span>. Nor have respondents identified any precedential support. Indeed, precedent is to the contrary: <span class="star-pagination">*863</span> "Historically, th[e] guarantee of due process has been applied to <i>deliberate</i> decisions of government officials to deprive a person of life, liberty, or property." <i>Daniels</i> v. <i>Williams,</i>  <span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/#331" aria-description="Citation for case: Daniels v. Williams">474 U. S. 327, 331</a></span> (1986) (citations omitted); <span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/#127" aria-description="Citation for case: Collins v. City of Harker Heights"><i>Collins, supra,</i>  at 127, n. 10</a></span> (same). Though it is true, as the Court explains, that "deliberate indifference" to the medical needs of pretrial detainees, <i>City of Revere</i> v. <i>Massachusetts Gen. Hospital,</i> <span class="citation" data-id="9429305"><a href="/opinion/110998/city-of-revere-v-massachusetts-general-hospital/#244" aria-description="Citation for case: City of Revere v. Massachusetts General Hospital">463 U. S. 239, 244-245</a></span> (1983), or of involuntarily committed mental patients, <i>Youngberg</i> v. <i>Romeo,</i> <span class="citation" data-id="9428825"><a href="/opinion/110746/youngberg-v-romeo-ex-rel-romeo/#314" aria-description="Citation for case: Youngberg v. Romeo Ex Rel. Romeo">457 U. S. 307, 314-325</a></span> (1982), may violate substantive due process, it is not the deliberate indifference alone that is the "deprivation." Rather, it is that combined with "the State's affirmative act of restraining the individual's freedom to act on his own behalfthrough incarceration, institutionalization, or other similar restraint of personal liberty," <i>DeShaney</i> v. <i>Winnebago County Dept. of Social Servs.,</i> <span class="citation" data-id="9431570"><a href="/opinion/112202/deshaney-v-winnebago-county-department-of-social-services/#200" aria-description="Citation for case: DeShaney v. Winnebago County Department of Social Services">489 U. S. 189, 200</a></span> (1989). "[W]hen the State by the affirmative exercise of its power so restrains an individual's liberty that it renders him unable to care for himself, and <i>at the same time</i> fails to provide for his basic human needs[,] . . . it transgresses the substantive limits on state action set by the . . . Due Process Clause." <i><span class="citation" data-id="9431570"><a href="/opinion/112202/deshaney-v-winnebago-county-department-of-social-services/" aria-description="Citation for case: DeShaney v. Winnebago County Department of Social Services">Ibid.</a></span></i> (emphasis added). We have expressly left open whether, in a context in which the individual has <i>not</i>  been deprived of the ability to care for himself in the relevant respect, "something less than intentional conduct, such as recklessness or `gross negligence,' " can ever constitute a "deprivation" under the Due Process Clause. <i>Daniels,</i> <span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/#334" aria-description="Citation for case: Daniels v. Williams">474 U. S., at 334, n. 3</a></span>. Needless to say, if it is an open question whether recklessness can <i>ever</i> trigger due process protections, there is no precedential support for a substantive-dueprocess right to be free from reckless police conduct during a car chase.</p>
<p>To hold, as respondents urge, that all government conduct deliberately indifferent to life, liberty, or property violates the Due Process Clause would make "`the Fourteenth Amendment a font of tort law to be superimposed upon whatever <span class="star-pagination">*864</span> systems may already be administered by the States.' " <span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/#332" aria-description="Citation for case: Daniels v. Williams"><i>Id.,</i>  at 332</a></span>, quoting <i>Paul</i> v. <i>Davis,</i> <span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/#701" aria-description="Citation for case: Paul v. Davis">424 U. S. 693, 701</a></span> (1976) (other citation omitted). Here, for instance, it is not fair to say that it was the police officer alone who "deprived" Lewis of his life. Though the police car did run Lewis over, it was the driver of the motorcycle, Willard, who dumped Lewis in the car's path by recklessly making a sharp left turn at high speed. (Willard had the option of rolling to a gentle stop and showing the officer his license and registration.) Surely Willard "deprived" Lewis of his life in every sense that the police officer did. And if Lewis encouraged Willard to make the reckless turn, Lewis himself would be responsible, at least in part, for his own death. Was there contributory fault on the part of Willard or Lewis? Did the police officer have the "last clear chance" to avoid the accident? Did Willard and Lewis, by fleeing from the police, "assume the risk" of the accident? These are interesting questions of tort law, not of constitutional governance. "Our Constitution deals with the large concerns of the governors and the governed, but it does not purport to supplant traditional tort law in laying down rules of conduct to regulate liability for injuries that attend living together in society." <span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/#332" aria-description="Citation for case: Daniels v. Williams"><i>Daniels, supra,</i> at 332</a></span>. As we have said many times, "the Due Process Clause of the Fourteenth Amendment . . . does not transform every tort committed by a state actor into a constitutional violation." <span class="citation" data-id="9431570"><a href="/opinion/112202/deshaney-v-winnebago-county-department-of-social-services/#202" aria-description="Citation for case: DeShaney v. Winnebago County Department of Social Services"><i>DeShaney, supra,</i> at 202</a></span> (citations omitted).</p>
<p>If the people of the State of California would prefer a system that renders police officers liable for reckless driving during high-speed pursuits, "[t]hey may create such a system. . . by changing the tort law of the State in accordance with the regular lawmaking process." 489 U. S., at 203. For now, they prefer not to hold public employees "liable for civil damages on account of personal injury to or death of any person or damage to property resulting from the operation, in the line of duty, of an authorized emergency vehicle . . . when in the immediate pursuit of an actual or suspected violator <span class="star-pagination">*865</span> of the law." Cal. Veh. Code Ann. § 17004 (West 1971). It is the prerogative of a self-governing people to make that legislative choice. "Political society," as the Seventh Circuit has observed, "must consider not only the risks to passengers, pedestrians, and other drivers that high-speed chases engender, but also the fact that if police are forbidden to pursue, then many more suspects will fleeand successful flights not only reduce the number of crimes solved but also create their own risks for passengers and bystanders." <i>Mays</i> v. <i>City of East St. Louis,</i> <span class="citation" data-id="9490608"><a href="/opinion/745416/eddie-mays-v-city-of-east-st-louis-illinois-leland-cherry-and-victor/#1003" aria-description="Citation for case: Eddie Mays v. City of East St. Louis, Illinois, Leland...">123 F. 3d 999, 1003</a></span> (1997). In allocating such risks, the people of California and their elected representatives may vote their consciences. But for judges to overrule that democratically adopted policy judgment on the ground that it shocks <i>their</i> consciences is not judicial review but judicial governance.</p>
<p>I would reverse the judgment of the Ninth Circuit, not on the ground that petitioners have failed to shock my still, soft voice within, but on the ground that respondents offer no textual or historical support for their alleged due process right. Accordingly, I concur in the judgment of the Court.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the State of Alaska et al. by <i>Daniel E. Lungren,</i> Attorney General of California, <i>Margaret A. Rodda,</i> Senior Assistant Attorney General, <i>Darryl L. Doke,</i>  Supervising Deputy Attorney General, and <i>Stephen J. Egan,</i> Deputy Attorney General, joined by the Attorneys General for their respective States as follows: <i>Bruce M. Botelho</i> of Alaska, <i>Grant Woods</i> of Arizona, <i>Margery S. Bronster</i> of Hawaii, <i>Alan G. Lance</i> of Idaho, <i>Thomas J. Miller</i>  of Iowa, <i>Michael E. Carpenter</i> of Maine, <i>Scott Harshbarger</i> of Massachusetts, <i>Frank J. Kelley</i> of Michigan, <i>Hubert H. Humphrey III</i> of Minnesota, <i>Jeremiah W. (Jay) Nixon</i> of Missouri, <i>Joseph P. Mazurek</i> of Montana, <i>Don Stenberg</i> of Nebraska, <i>Frankie Sue Del Papa</i> of Nevada, <i>Dennis C. Vacco</i>  of New York, <i>Heidi Heitkamp</i> of North Dakota, <i>D. Michael Fisher</i> of Pennsylvania, <i>Mark W. Barnett</i> of South Dakota, <i>Jan Graham</i> of Utah, <i>Richard Cullen</i> of Virginia, <i>Darrell V. McGraw, Jr.,</i> of West Virginia, <i>James E. Doyle</i> of Wisconsin, and <i>William U. Hill</i> of Wyoming; for the City and County of Denver by <i>Theodore S. Halaby;</i> for the County of Riverside et al. by <i>William C. Katzenstein, James K. Hahn, Gregory</i>  <i>P. Orland, Timothy T. Coates, H. Peter Klein, Alan K. Marks, James B. Lindholm, Jr., Steven M. Woodside, James Rumble,</i> and <i>James P. Botz;</i>  for the Grand Lodge of the Fraternal Order of Police by <i>Gary Lightman, Thomas T. Rutherford,</i> and <i>William J. Friedman;</i> for the National Association of Counties et al. by <i>Richard Ruda</i> and <i>Charles Rothfeld;</i> and for the Criminal Justice Legal Foundation by <i>Kent S. Scheidegger.</i>
</p>
<p>Briefsof <i>amici curiae</i> urging affirmance were filedfor the Association of Trial Lawyers of America by <i>Howard A. Friedman</i> and <i>Richard D. Haley;</i> for GabrielTorres et al. by <i>Stephen Yagman</i> and <i>Marion R. Yagman;</i> and for Solutions to the Tragedies of Police Pursuits (STOPP) by <i>Andrew C. Clarke.</i></p>
<p>[1]  Respondents also brought claims under state law. The District Court found that Smith was immune from state tort liability by operation of California Vehicle Code § 17004, which provides that "[a] public employee is not liable for civil damages on account of personal injury to or death of any person or damage to property resulting from the operation, in the line of duty, of an authorized emergency vehicle . . . when in the immediate pursuit of an actual or suspected violator of the law." Cal. Veh. Code Ann. § 17004 (West 1971). The court declined to rule on the potential liability of the county under state law, instead dismissing the tort claims against the county without prejudice to refiling in state court.</p>
<p>[2]  The District Court also granted summary judgment in favor of the county and the Sheriff's Department on the § 1983 claim, concluding that municipal liability would not lie under <i>Monell</i> v. <i>New York City Dept. of Social Servs.,</i> <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span> (1978), after finding no genuine factual dispute as to whether the county adequately trains its officers in the conduct of vehicular pursuits or whether the pursuit policy of the Sheriff's Department evinces deliberate indifference to the constitutional rights of the public. The Ninth Circuit affirmed the District Court on these points, <span class="citation multiple-matches"><a href="/c/F.%203d/98/434/">98 F. 3d 434</a></span>, 446-447 (1996), and the issue of municipal liability is not before us.</p>
<p>[3]  In <i>Jones</i> v. <i>Sherrill,</i> <span class="citation" data-id="493644"><a href="/opinion/493644/janice-jones-v-charles-e-sherrill/#1106" aria-description="Citation for case: Janice Jones v. Charles E. Sherrill">827 F. 2d 1102, 1106</a></span> (1987), the Sixth Circuit adopted a "gross negligence" standard for imposing liability for harm caused by police pursuit. Subsequently, in <i>Foy</i> v. <i>Berea,</i> <span class="citation" data-id="698391"><a href="/opinion/698391/cynthia-d-foy-administratrix-of-the-estate-of-terry-a-foy-deceased-v/#230" aria-description="Citation for case: Cynthia D. Foy, Administratrix of the Estate of Terry A....">58 F. 3d 227, 230</a></span> (1995), the Sixth Circuit, without specifically mentioning <i><span class="citation" data-id="493644"><a href="/opinion/493644/janice-jones-v-charles-e-sherrill/" aria-description="Citation for case: Janice Jones v. Charles E. Sherrill">Jones</a></span>,</i> disavowed the notion that "gross negligence is sufficient to support a substantive due process claim." Although <i><span class="citation" data-id="698391"><a href="/opinion/698391/cynthia-d-foy-administratrix-of-the-estate-of-terry-a-foy-deceased-v/" aria-description="Citation for case: Cynthia D. Foy, Administratrix of the Estate of Terry A....">Foy</a></span></i> involved police inaction, rather than police pursuit, it seems likely that the Sixth Circuit would now apply the "deliberate indifference" standard utilized in that case, see <span class="citation" data-id="698391"><a href="/opinion/698391/cynthia-d-foy-administratrix-of-the-estate-of-terry-a-foy-deceased-v/#232" aria-description="Citation for case: Cynthia D. Foy, Administratrix of the Estate of Terry A....">58 F. 3d, at 232-233</a></span>, rather than the "gross negligence" standard adopted in <i><span class="citation" data-id="493644"><a href="/opinion/493644/janice-jones-v-charles-e-sherrill/" aria-description="Citation for case: Janice Jones v. Charles E. Sherrill">Jones</a></span>,</i> in a police pursuit situation.</p>
<p>[4]  Respondents do not argue that they were denied due process of law by virtue of the fact that California's post deprivation procedures and rules of immunity have effectively denied them an adequate opportunity to seek compensation for the state-occasioned deprivation of their son's life. We express no opinion here on the merits of such a claim, cf. <i>Albright</i> v. <i>Oliver,</i> <span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/#281" aria-description="Citation for case: Albright v. Oliver">510 U. S. 266, 281-286</a></span> (1994) (Kennedy, J., concurring in judgment); <i>Parratt</i> v. <i>Taylor,</i> <span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">451 U. S. 527</a></span> (1981), or on the adequacy of California's post deprivation compensation scheme.</p>
<p>[5]  As in any action under § 1983, the first step is to identify the exact contours of the underlying right said to have been violated. See <i>Graham</i>  v. <i>Connor,</i> <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#394" aria-description="Citation for case: Graham v. Connor">490 U. S. 386, 394</a></span> (1989). The District Court granted summary judgment to Smith on the basis of qualified immunity, assuming without deciding that a substantive due process violation took place but holding that the law was not clearly established in 1990 so as to justify imposition of § 1983 liability. We do not analyze this case in a similar fashion because, as we have held, the better approach to resolving cases in which the defense of qualified immunity is raised is to determine first whether the plaintiff has alleged a deprivation of a constitutional right at all. Normally, it is only then that a court should ask whether the right allegedly implicated was clearly established at the time of the events in question. See <i>Siegert</i> v. <i>Gilley,</i> <span class="citation" data-id="9432276"><a href="/opinion/112594/siegert-v-gilley/#232" aria-description="Citation for case: Siegert v. Gilley">500 U. S. 226, 232</a></span> (1991) ("A necessary concomitant to the determination of whether the constitutional right asserted by a plaintiff is `clearly established' at the time the defendant acted is the determination of whether the plaintiff has asserted a violation of a constitutional right at all," and courts should not "assum[e], without deciding, this preliminary issue").
</p>
<p>Justice Stevens suggests that the rule of <i><span class="citation" data-id="9432276"><a href="/opinion/112594/siegert-v-gilley/" aria-description="Citation for case: Siegert v. Gilley">Siegert</a></span></i> should not apply where, as here, the constitutional question presented "is both difficult and unresolved." <i>Post,</i> at 859. But the generally sound rule of avoiding determination of constitutional issues does not readily fit the situation presented here; when liability is claimed on the basis of a constitutional violation, even a finding of qualified immunity requires some determination about the state of constitutional law at the time the officer acted. What is more significant is that if the policy of avoidance were always followed in favor of ruling on qualified immunity whenever there was no clearly settled constitutional rule of primary conduct, standards of official conduct would tend to remain uncertain, to the detriment both of officials and individuals. An immunity determination, with nothing more, provides no clear standard, constitutional or non constitutional. In practical terms, escape from uncertainty would require the issue to arise in a suit to enjoin future conduct, in an action against a municipality, or in litigating a suppression motion in a criminal proceeding; in none of these instances would qualified immunity be available to block a determination of law. See Shapiro, Public Officials' Qualified Immunity in Section 1983 Actions Under <i>Harlow</i> v. <i>Fitzgerald</i> and its Progeny, 22 U. Mich. J. L. Ref. 249, 265, n. 109 (1989). But these avenues would not necessarily be open, and therefore the better approach is to determine the right before determining whether it was previously established with clarity.</p>
<p>[6]  See Brief for National Association of Counties et al. as <i>Amici Curiae</i>  8-13; Brief for Grand Lodge of the Fraternal Order of Police as <i>Amicus Curiae</i> 4-9; Brief for City and County of Denver, Colorado, as <i>Amici Curiae</i> 2-7; Brief for County of Riverside et al. as <i>Amici Curiae</i> 6-18; Brief for Gabriel Torres et al. as <i>Amici Curiae</i> 3-11.</p>
<p>[7]  Several <i>amici</i> suggest that, for the purposes of <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span>,</i> the Fourth Amendment should cover not only seizures,but also failed attempts to make a seizure. See, <i>e. g.,</i> Brief for National Association of Counties et al. as <i>Amici Curiae</i> 10-11. This argument is foreclosed by <i>California</i>  v. <i>Hodari D.,</i> <span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/" aria-description="Citation for case: California v. Hodari D.">499 U. S. 621</a></span> (1991), in which we explained that "neither usage nor common-law tradition makes an <i>attempted</i> seizure a seizure. The common law may have made an attempted seizure unlawful in certain circumstances; but it made many things unlawful, very few of which were elevated to constitutional proscriptions." <span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/#626" aria-description="Citation for case: California v. Hodari D."><i>Id.,</i> at 626, n. 2</a></span>. Attempted seizures of a person are beyond the scope of the Fourth Amendment. See <span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/#646" aria-description="Citation for case: California v. Hodari D."><i>id.,</i> at 646</a></span> (Stevens, J., dissenting) (disagreeing with the Court's position that "an attempt to make [a] . . . seizure is beyond the coverage of the Fourth Amendment").</p>
<p>[8]  As Justice Scalia has explained before, he fails to see "the usefulness of `conscience shocking' as a legal test," <i>Herrera</i> v. <i>Collins,</i> <span class="citation" data-id="9432727"><a href="/opinion/112808/herrera-v-collins/#428" aria-description="Citation for case: Herrera v. Collins">506 U. S. 390, 428</a></span> (1993), and his independent analysis of this case is therefore understandable. He is, however, simply mistaken in seeing our insistence on the shocks-the-conscience standard as an atavistic return to a scheme of due process analysis rejected by the Court in <i>Washington</i> v. <i>Glucksberg,</i>  <span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">521 U. S. 702</a></span> (1997).
</p>
<p><i>Glucksberg</i> presented a disagreement about the significance of historical examples of protected liberty in determining whether a given statute could be judged to contravene the Fourteenth Amendment. The differences of opinion turned on the issues of how much history indicating recognition of the asserted right, viewed at what level of specificity, is necessary to support the finding of a substantive due process right entitled to prevail over state legislation.</p>
<p>As we explain in the text, a case challenging executive action on substantive due process grounds, like this one, presents an issue antecedent to any question about the need for historical examples of enforcing a liberty interest of the sort claimed. For executive action challenges raise a particular need to preserve the constitutional proportions of constitutional claims, lest the Constitution be demoted to what we have called a font of tort law. Thus, in a due process challenge to executive action, the threshold question is whether the behavior of the governmental officer is so egregious, so outrageous, that it may fairly be said to shock the contemporary conscience. That judgment may be informed by a history of liberty protection, but it necessarily reflects an understanding of traditional executive behavior, of contemporary practice, and of the standards of blame generally applied to them. Only if the necessary condition of egregious behavior were satisfied would there be a possibility of recognizing a substantive due process right to be free of such executive action, and only then might there be a debate about the sufficiency of historical examples of enforcement of the right claimed, or its recognition in other ways. In none of our prior cases have we considered the necessity for such examples, and no such question is raised in this case.</p>
<p>In sum, the difference of opinion in <i><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">Glucksberg</a></span></i> was about the need for historical examples of recognition of the claimed liberty protection at some appropriate level of specificity. In an executive action case, no such issue can arise if the conduct does not reach the degree of the egregious.</p>
<p>[9]  In <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952), the case in which we formulated and first applied the shocks-the-conscience test, it was not the ultimate purpose of the government actors to harm the plaintiff, but they apparently acted with full appreciation of what the Court described as the brutality of their acts. <i><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span>,</i> of course, was decided long before <i>Graham</i> v. <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Connor</a></span></i> (and <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961)), and today would be treated under the Fourth Amendment, albeit with the same result.</p>
<p>[10]  We have also employed deliberate indifference as a standard of culpability sufficient to identify a dereliction as reflective of municipal policy and to sustain a claim of municipal liability for failure to train an employee who causes harm by unconstitutional conduct for which he would be individually liable. See <i>Canton</i> v. <i>Harris,</i> <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#388" aria-description="Citation for case: City of Canton v. Harris">489 U. S. 378, 388-389</a></span> (1989).</p>
<p>[11]  By "actual deliberation," we do not mean "deliberation" in the narrow, technical sense in which it has sometimes been used in traditional homicide law. See, <i>e. g., </i><i>Caldwell</i> v. <i>State,</i> <span class="citation" data-id="3224606"><a href="/opinion/3224387/caldwell-v-state/#276" aria-description="Citation for case: Caldwell v. State">84 So. 272, 276</a></span> (Ala. 1919) (noting that "`deliberation here does not mean that the man slayer must ponder over the killing for a long time' "; rather, "it may exist and may be entertained while the man slayer is pressing the trigger of the pistol that fired the fatal shot[,] even if it be only for a moment or instant of time").</p>
<p>[12]  <i>Youngberg</i> v. <i>Romeo,</i> <span class="citation" data-id="9428825"><a href="/opinion/110746/youngberg-v-romeo-ex-rel-romeo/" aria-description="Citation for case: Youngberg v. Romeo Ex Rel. Romeo">457 U. S. 307</a></span> (1982), can be categorized on much the same terms. There, we held that a severely retarded person could state a claim under § 1983 for a violation of substantive due process if the personnel at the mental institution where he was confined failed to exercise professional judgment when denying him training and habilitation. <i>Id.,</i> at 319-325. The combination of a patient's involuntary commitment and his total dependence on his custodians obliges the government to take thought and make reasonable provision for the patient's welfare.</p>
<p>[13]  Cf.<i>Checki</i> v. <i>Webb,</i> <span class="citation" data-id="466102"><a href="/opinion/466102/ron-checki-v-richard-webb/#538" aria-description="Citation for case: Ron Checki v. Richard Webb">785 F.2d 534, 538</a></span> (CA5 1986) ("Where a citizen suffers physical injury due to a police officer's <i>negligent use</i> of his vehicle, no section 1983 claim is stated. It is a different story when a citizen suffers or is seriously threatened with physical injury due to a police officer's <i>intentional misuse</i> of his vehicle" (citation omitted)).</p>
<p>[14]  To say that due process is not offended by the police conduct described here is not, of course, to imply anything about its appropriate treatment under state law. See <i>Collins</i> v. <i>Harker Heights,</i> <span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/#128" aria-description="Citation for case: Collins v. City of Harker Heights">503 U. S. 115, 128-129</a></span> (1992) (decisions about civil liability standards that "involve a host of policy choices . . .must be made by locally elected representatives [or by courts enforcing the common law of torts], rather than by federal judges interpreting the basic charter of Government for the entire country"). Cf. <i>Thomas</i> v. <i>City of Richmond,</i> <span class="citation" data-id="9544012"><a href="/opinion/1163447/thomas-v-city-of-richmond/" aria-description="Citation for case: Thomas v. City of Richmond">9 Cal. 4th 1154</a></span>, <span class="citation" data-id="9544012"><a href="/opinion/1163447/thomas-v-city-of-richmond/" aria-description="Citation for case: Thomas v. City of Richmond">892 P. 2d 1185</a></span> (1995) (en banc) (discussing municipal liability under California law for injuries caused by police pursuits).</p>
<p>[1]  For those unfamiliar with classical music, I note that the exemplars of excellence in the text are borrowed from Cole Porter's "You're the Top," copyright 1934.</p>
<p>[2]  The proposition that "shocks-the-conscience" is a test applicable only to executive action is original with today's opinion. That has never been suggested in any of our cases, and in fact "shocks-the-conscience" was recited in at least one opinion involving legislative action. See <i>United States</i> v. <i>Salerno,</i> <span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/#746" aria-description="Citation for case: United States v. Salerno">481 U. S. 739, 746</a></span> (1987) (in considering whether the Bail Reform Act of 1984 violated the Due Process Clause, we said that "[s]o-called `substantive due process' prevents the government from engaging in conduct that `shocks the conscience' "). I am of course happy to accept whatever limitations the Court today is willing to impose upon the "shocks-the-conscience" test, though it is a puzzlement why substantive due process protects some liberties against executive officers but not against legislatures.</p>

</div>
```

---

## GROUP: content/cases/Culley v. Marshall.md  (`case`, 5 assertions)

### content_page

```
---
title: Culley v. Marshall
type: case
citation: "601 U.S. 377 (2024)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2024
date_decided: ""
docket: 22-585
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
  opinion_url: "https://www.courtlistener.com/opinion/10600097/culley-v-marshall/"
  cluster_id: 10600097
  opinion_id: 11066685
  identity_checked: true
lake:
  record_id: Culley v. Marshall
  status: under_review
  projected_at: 2026-07-09
homes:
  - page: "[[Civil Asset Forfeiture]]"
    role: Recent development
related:
  - "[[Civil Asset Forfeiture]]"
tags:
  - case
  - civil-asset-forfeiture
  - due-process
  - section-1983
holding: "In civil forfeiture cases involving personal property, the Due Process Clause requires a timely forfeiture hearing but does not require a separate preliminary hearing to decide whether police may retain the property pending that hearing."
---

# Culley v. Marshall

*601 U.S. 377 (2024)* (No. 22-585) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10600097 → opinion 11066685; quotes string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Halima Culley and Lena Sutton each lent a car to someone who was then stopped by Alabama police and found with drugs; the State seized both cars and initiated civil forfeiture proceedings. The owners sued under 42 U.S.C. § 1983, contending that the Due Process Clause required a prompt post-seizure hearing to decide whether the police could retain their cars while the forfeiture cases proceeded. The federal district courts and, on consolidated appeal, the Eleventh Circuit rejected the claims, holding that a timely forfeiture hearing affords due process and that no separate preliminary retention hearing is constitutionally required.

## Issue
Whether the Due Process Clause requires a separate preliminary hearing — beyond a timely forfeiture hearing — to determine whether police may retain seized personal property (here, a car) pending the civil forfeiture proceeding.

## Rule
When police seize personal property for civil forfeiture, due process is governed by the Court's forfeiture-timing precedents rather than by a new preliminary-hearing requirement. Drawing on *[[United States v. $8,850 in Currency|United States v. $8,850]]* and *[[United States v. Von Neumann]]*, the Court held that "[t]his Court's precedents establish that the answer is no: The Constitution requires a timely forfeiture hearing; the Constitution does not also require a separate preliminary hearing." — 601 U.S. at 381. ^pin-381

The timeliness of the forfeiture hearing itself is measured under the four-factor *[[United States v. $8,850 in Currency|$8,850]]* test, through which a property owner may press for a prompt hearing.

## Application
The petitioners' demand for a separate preliminary hearing was, in substance, a request for a *more timely* forfeiture hearing — a protection the Court's precedents already supply, and one a claimant can invoke through the *[[United States v. $8,850 in Currency|$8,850]]* timeliness factors. The Court declined to import the *Mathews v. Eldridge* balancing test, noting that *[[United States v. $8,850 in Currency|$8,850]]* and *[[United States v. Von Neumann|Von Neumann]]* had themselves been decided without applying *Mathews*, and reasoned that an added preliminary hearing would interfere with legitimate law-enforcement activity in the interval between seizure and the forfeiture hearing. The decision fixes only the constitutional baseline; States remain free to provide additional procedural protections by statute.

## Conclusion
The judgment of the Eleventh Circuit was **affirmed**. Kavanaugh, J., delivered the opinion of the Court; Gorsuch, J., joined by Thomas, J., concurred; Sotomayor, J., joined by Kagan and Jackson, JJ., dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Culley* is a due-process/timing decision that sets the federal floor for civil forfeiture of personal property; it leaves state-law innovations and the *[[United States v. $8,850 in Currency|$8,850]]* timeliness inquiry undisturbed.

## Appears on
- [[Civil Asset Forfeiture]] — *Recent development*

## Sources
- [*Culley v. Marshall*, 601 U.S. 377 (2024)](https://www.courtlistener.com/opinion/10600097/culley-v-marshall/) — pinpoint: 381 (Opinion of the Court, holding); quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "34a21add8bc7b7a5", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "601 U.S. 377 (2024)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Culley v. Marshall", "year": "2024"}}
{"assertion_id": "994b0f76e37e8ace", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "In civil forfeiture cases involving personal property, the Due Process Clause requires a timely forfeiture hearing but does not require a separate preliminary hearing to decide whether police may retain the property pending that hearing.", "title": "Culley v. Marshall"}}
{"assertion_id": "f6f23c9c2d485bc6", "dimension": "support", "kind": "home_role", "locator": {"home": "Civil Asset Forfeiture"}, "payload": {"home": "Civil Asset Forfeiture", "role": "Recent development", "title": "Culley v. Marshall"}}
{"assertion_id": "2d44185e144843bc", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Culley v. Marshall", "varies_by_point": "false"}}
{"assertion_id": "e99889ea66ddcb6f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Culley v. Marshall"}}
```

### lake record — Culley v. Marshall

```json
{
  "schema_version": "s2.v1",
  "record_id": "Culley v. Marshall",
  "status": "under_review",
  "identity": {
    "case_name": "Culley v. Marshall",
    "case_name_short": "Culley",
    "case_name_full": "",
    "input_case_name": "Culley v. Marshall",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2024,
    "docket": "22-585",
    "cluster_id": 10600097,
    "lead_opinion_id": 11066685,
    "sibling_ids": [],
    "absolute_url": "/opinion/10600097/culley-v-marshall/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "601 U.S. 377",
      "volume": "601",
      "reporter": "U.S.",
      "page": "377",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "601 U.S. 377",
        "volume": "601",
        "reporter": "U.S.",
        "page": "377",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "601 U.S. 377",
    "official_selection": {
      "court_class": "scotus",
      "selected": "601 U.S. 377",
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
    "date_created": "2026-07-06T12:11:55Z",
    "date_modified": "2026-07-09T23:29:56Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:12:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:12:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "culley-v-marshall--10600097",
      "to_record_id": "Culley v. Marshall",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Culley v. Marshall

```
                   PRELIMINARY PRINT

             Volume 601 U. S. Part 2
                             Pages 377–415




       OFFICIAL REPORTS
                                    OF


   THE SUPREME COURT
                                May 9, 2024


Page Proof Pending Publication


                   REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D.C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
                         OCTOBER TERM, 2023                               377

                                  Syllabus


       CULLEY et al. v. MARSHALL, ATTORNEY
           GENERAL OF ALABAMA, et al.
certiorari to the united states court of appeals for
                the eleventh circuit
      No. 22–585. Argued October 30, 2023—Decided May 9, 2024
Petitioner Halima Culley loaned her car to her son, who was later pulled
  over by Alabama police offcers and arrested for possession of mari-
  juana. Petitioner Lena Sutton loaned her car to a friend, who was
  stopped by Alabama police and arrested for traffcking methamphet-
  amine. In both cases, petitioners' cars were seized under an Alabama
  civil forfeiture law that permitted seizure of a car “incident to an arrest”
  so long as the State then “promptly” initiated a forfeiture case. Ala.
  Code § 20–2–93(b)(1), (c). The State of Alabama fled forfeiture com-
  plaints against Culley's and Sutton's cars just 10 and 13 days, respec-
  tively, after their seizure. While their forfeiture proceedings were
  pending, Culley and Sutton each fled purported class-action complaints
  in federal court seeking money damages under 42 U. S. C. § 1983, claim-
Page Proof Pending Publication
  ing that state offcials violated their due process rights by retaining
  their cars during the forfeiture process without holding preliminary
  hearings. In a consolidated appeal, the Eleventh Circuit affrmed the
  dismissal of petitioners' claims, holding that a timely forfeiture hearing
  affords claimants due process and that no separate preliminary hearing
  is constitutionally required.
Held: In civil forfeiture cases involving personal property, the Due Proc-
 ess Clause requires a timely forfeiture hearing but does not require a
 separate preliminary hearing. Pp. 384–393.
    (a) Due process ordinarily requires States to provide notice and a
 hearing before seizing real property. But States may immediately
 seize personal property subject to civil forfeiture when the property (for
 example, a car) otherwise could be removed, destroyed, or concealed
 before a forfeiture hearing. When a State seizes personal property, due
 process requires a timely post-seizure forfeiture hearing. See United
 States v. Von Neumann, 474 U. S. 242, 249–250; United States v. $8,850,
 461 U. S. 555, 562–565.
    The Court's decisions in $8,850 and Von Neumann make crystal clear
 that due process does not require a separate preliminary hearing to
 determine whether seized personal property may be retained pending
 the ultimate forfeiture hearing. In $8,850, the Court addressed the
 process due when the Customs Service seized currency from an individ-
378                     CULLEY v. MARSHALL

                                 Syllabus

  ual entering the United States but did not immediately fle for civil
  forfeiture of the currency. The Court concluded that a post-seizure
  delay “may become so prolonged that the dispossessed property owner
  has been deprived of a meaningful hearing at a meaningful time,” 461
  U. S., at 562–563, and prescribed factors for courts to consider in assess-
  ing whether a forfeiture hearing is timely. Id., at 564–565. In Von
  Neumann, a property owner failed to declare the purchase of his new
  car upon driving it into the United States, and a customs offcial seized
  the car after determining that it was subject to civil forfeiture. The
  plaintiff fled a petition for remission of the forfeiture—in essence, a
  request under federal law that the Government exercise its discretion
  to forgive the forfeiture—which the Government did not answer for
  36 days. The plaintiff sued, arguing that the Government's delay in
  answering the remission petition violated due process. The Court re-
  jected that claim, broadly holding that due process did not require a
  pre-forfeiture-hearing remission procedure in the frst place. See 474
  U. S., at 249–250. Instead, Von Neumann held that a timely forfeiture
  hearing satisfes due process in civil forfeiture cases, and that $8,850
  specifes the standard for when a forfeiture hearing is timely.
     Petitioners' argument for a separate preliminary hearing appears to

Page Proof Pending Publication
  be a backdoor argument for a more timely forfeiture hearing to allow a
  property owner with a good defense to recover her property quickly.
  But the Court's precedents already require a timely hearing, and a prop-
  erty owner can raise $8,850-based arguments to ensure a timely hearing.
  Petitioners' efforts to distinguish Von Neumann on the ground that the
  statutory remission procedure in that case was discretionary fail be-
  cause that fact played no role in the Court's constitutional analysis.
  Petitioners also cannot distinguish the relevant language in Von Neu-
  mann as dicta, as the Court ruled for the Government on the ground
  that a timely “forfeiture proceeding, without more, provides the postsei-
  zure hearing required by due process” in civil forfeiture cases. 474
  U. S., at 249. Similarly, petitioners' contention that Mathews v. El-
  dridge, 424 U. S. 319, should govern petitioners' request for a prelimi-
  nary hearing fails given that this Court decided $8,850 and Von
  Neumann after Mathews.
     In addition, petitioners point to the Court's Fourth Amendment deci-
  sions in the criminal context to support their contention that a prelimi-
  nary hearing is required in the civil forfeiture context. That analogy
  fails. Fourth Amendment hearings are not adversarial, and address
  only whether probable cause supports the arrestee's detention. See
  Gerstein v. Pugh, 420 U. S. 103, 119–122. Here, petitioners argue that
                       Cite as: 601 U. S. 377 (2024)                    379

                                 Syllabus

  the immediate seizure of personal property requires adversarial prelimi-
  nary hearings, and they assert that those hearings must address their
  affrmative defense of innocent ownership. But the Due Process Clause
  does not require more extensive preliminary procedures for the tempo-
  rary retention of property than for the temporary restraint of persons.
  Pp. 384–390.
    (b) Historical practice reinforces the Court's conclusions in $8,850 and
  Von Neumann that due process does not require preliminary hearings
  in civil forfeiture cases. Since the Founding era, many federal and
  state statutes have authorized the Government to seize personal prop-
  erty and hold it pending a forfeiture hearing, without a separate prelimi-
  nary hearing. Petitioners and their amici do not identify any federal
  or state statutes that, before the late 20th century, required preliminary
  hearings in civil forfeiture cases. Some States have recently enacted
  laws requiring preliminary hearings in civil forfeiture cases, but those
  recent laws do not support a constitutional mandate for preliminary
  hearings in every State. History demonstrates that both Congress and
  the States have long authorized law enforcement to seize personal prop-
  erty and hold it until a forfeiture hearing. The absence of separate
  preliminary hearings in civil forfeiture proceedings—from the Founding
  until the late 20th century—is weighty evidence that due process does
Page Proof Pending Publication
  not require such hearings. Pp. 390–392.
Affrmed.

   Kavanaugh, J., delivered the opinion of the Court, in which Roberts,
C. J., and Thomas, Alito, Gorsuch, and Barrett, JJ., joined. Gorsuch,
J., fled a concurring opinion, in which Thomas, J., joined, post, p. 393.
Sotomayor, J., fled a dissenting opinion, in which Kagan and Jackson,
JJ., joined, post, p. 403.

   Shay Dvoretzky argued the cause for petitioners. With
him on the briefs were Parker Rider-Longmaid, Kyser
Blakely, Jeremy Patashnik, and Brian M. Clark.
   Edmund G. LaCour, Jr., Solicitor General of Alabama, ar-
gued the cause for respondents. With him on the brief were
Steve Marshall, Attorney General, pro se, Robert M. Over-
ing, Deputy Solicitor General, Brad A. Chynoweth, Assistant
Chief Deputy Attorney General, and Brenton M. Smith, As-
sistant Attorney General. Ed R. Haden, Michael P. Taun-
ton, Thomas O. Gaillard, III, William W. Watts, III, and
380                    CULLEY v. MARSHALL

                          Opinion of the Court

H. Edgar Howard fled a brief for respondents City of Sat-
suma, Alabama, et al.
  Nicole Frazer Reaves argued the cause for the United
States as amicus curiae urging affrmance. With her on the
brief were Solicitor General Prelogar, Acting Assistant At-
torney General Argentieri, Principal Deputy Assistant At-
torney General Boynton, Deputy Solicitor General Feigin,
Ann O'Connell Adams, and Sarah Carroll.*


   Justice Kavanaugh delivered the opinion of the Court.
  When police seize and then seek civil forfeiture of a car
that was used to commit a drug offense, the Constitution
requires a timely forfeiture hearing. The question here is
whether the Constitution also requires a separate prelimi-
nary hearing to determine whether the police may retain the

  *Briefs of amici curiae urging reversal were fled for the American
Page         Proof
Civil Liberties Union et al.Pending            Publication
                             by Abram J. Pafford, John W. Whitehead,
David D. Cole, and Jay R. Schweikert; for the Buckeye Institute by Jay
R. Carson and David C. Tryon; for the Constitutional Accountability Cen-
ter by Elizabeth B. Wydra, Brianne J. Gorod, and Brian R. Frazelle; for
the Goldwater Institute et al. by Timothy Sandefur, Deborah J. La Fetra,
and Ilya Shapiro; for the Institute for Justice et al. by Robert Johnson;
and for the Legal Aid Society by Thomas M. O'Brien, Corey Stoughton,
and Philip Desgranges.
   Briefs of amici curiae urging affrmance were fled for the State of
Georgia et al. by Christopher M. Carr, Attorney General of Georgia, and
Stephen J. Petrany, Solicitor General, and by the Attorneys General for
their respective States as follows: Treg Taylor of Alaska, Tim Griffn of
Arkansas, Raúl Labrador of Idaho, Lynn Fitch of Mississippi, Austin
Knudsen of Montana, Michael T. Hilgers of Nebraska, John M. Formella
of New Hampshire, Gentner Drummond of Oklahoma, Michelle A. Henry
of Pennsylvania, Alan Wilson of South Carolina, Marty Jackley of South
Dakota, and Jonathan Skrmetti of Tennessee; for Wayne County, Michi-
gan, by Davidde A. Stella; and for the International Municipal Lawyers
Association et al. by Gilbert C. Dickey.
   Briefs of amici curiae were fled for the National Federation of Inde-
pendent Business Small Business Legal Center, Inc., by Elizabeth Gaudio
Milito; and for Restore the Fourth, Inc., by Mahesha P. Subbaraman.
                    Cite as: 601 U. S. 377 (2024)             381

                       Opinion of the Court

car pending the forfeiture hearing. This Court's precedents
establish that the answer is no: The Constitution requires a
timely forfeiture hearing; the Constitution does not also re-
quire a separate preliminary hearing.

                                 I
   Halima Culley loaned her car to her college-aged son. On
February 17, 2019, police offcers in Satsuma, Alabama,
stopped the car while the son was driving, and the offcers
discovered marijuana and a loaded handgun in the car. The
offcers arrested Culley's son and charged him with possess-
ing marijuana. The offcers also seized the car incident to
the arrest.
   At about the same time in 2019, Lena Sutton loaned her
car to a friend. On February 21, 2019, police offcers in
Leesburg, Alabama, stopped the car while Sutton's friend
was driving, and the offcers discovered a large amount of
Page Proof Pending Publication
methamphetamine in the car. The offcers arrested Sutton's
friend and charged him with traffcking methamphetamine
and possessing drug paraphernalia. The offcers also seized
the car incident to the arrest.
   At the time of the seizures of the two cars, Alabama law
authorized the civil forfeiture of a car used to commit or facil-
itate a drug crime. See Ala. Code § 20–2–93(a)(5) (2015).
Offcers could seize the car “incident to an arrest” so long as
the State then “promptly” initiated a forfeiture case. § 20–
2–93(b)(1), (c). In the interim before the forfeiture hearing,
the car's owner could recover it by posting bond at double
the car's value. See § 20–2–93(h); § 28–4–287 (2013). At
the forfeiture hearing, the owner could prevail and recover
the car under Alabama's “affrmative defense” for “innocent
owners of property subject to forfeiture.” Wallace v. State,
229 So. 3d 1108, 1110 (Ala. Civ. App. 2017). That defense
required the owner to show that the owner lacked knowledge
of the car's connection to the drug crime. See Ala. Code
§ 20–2–93(h) (2015).
382                 CULLEY v. MARSHALL

                      Opinion of the Court

   The State of Alabama fled a forfeiture complaint against
Culley's car on February 27, 2019, just 10 days after the sei-
zure of the car. But Culley waited six months before an-
swering that complaint. And she waited another year—
until September 21, 2020—before raising an innocent owner
defense in a motion for summary judgment. Soon thereaf-
ter, on October 30, 2020, an Alabama state court granted
Culley's motion and ordered the return of her car.
   Sutton similarly moved slowly in her forfeiture proceed-
ing. Alabama brought a forfeiture case against Sutton's car
on March 6, 2019, just 13 days after the seizure of the car.
Sutton initially failed to appear in the case, causing the state
court to enter a default judgment for Alabama. Sutton later
requested that the state court set aside that judgment, and
the state court did so. Sutton then submitted a brief answer
and served discovery requests on Alabama, but Sutton other-
wise took no action until the state court set a date for the
Page Proof Pending Publication
forfeiture trial. On April 10, 2020, three weeks before the
scheduled trial date, Sutton fnally moved for summary judg-
ment on the ground that she was an innocent owner. Soon
thereafter, on May 28, 2020, the state court granted her mo-
tion, and she recovered her car.
   While those forfeiture cases were ongoing, Culley and Sut-
ton fled purported class-action complaints in federal court.
Culley sued in the U. S. District Court for the Southern Dis-
trict of Alabama. Sutton sued in the U. S. District Court
for the Northern District of Alabama. Both sought money
damages under 42 U. S. C. § 1983, claiming that the state of-
fcials violated their due process rights by retaining their
cars during the forfeiture process without holding prelimi-
nary hearings. Culley and Sutton argued that a preliminary
hearing (also referred to as a retention hearing) is required
under the Mathews v. Eldridge due process test, which bal-
ances the private interests at stake, the value of added pro-
cedures, and the burdens on the government from the added
procedures. See 424 U. S. 319, 334–335 (1976).
                   Cite as: 601 U. S. 377 (2024)             383

                      Opinion of the Court

   The District Court for the Southern District of Alabama
dismissed Culley's complaint. Culley v. Marshall, Civ. Ac-
tion No. 19–701 (Sept. 29, 2021), App. to Pet. for Cert. 58a.
Relying on this Court's decisions in United States v. $8,850,
461 U. S. 555 (1983), and United States v. Von Neumann, 474
U. S. 242 (1986), the District Court held that due process
requires a timely forfeiture hearing but not a separate pre-
liminary hearing. See App. to Pet. for Cert. 44a–46a. The
District Court then assessed the timeliness of Culley's for-
feiture hearing under the four-factor test set forth in $8,850,
which looks to (i) the length of the delay of the forfeiture
hearing, (ii) the reason for the delay, (iii) whether the claim-
ant requested a timely hearing, and (iv) whether the delay
was prejudicial. See id., at 46a–47a (citing $8,850, 461 U. S.,
at 563–565). The District Court concluded that Culley's for-
feiture hearing was timely under those factors because she
played a “signifcant role” in delaying her own case. App.
Page Proof Pending Publication
to Pet. for Cert. 47a.
   The District Court for the Northern District of Alabama
similarly entered summary judgment against Sutton on her
due process claim. Sutton v. Leesburg, Civ. Action No. 20–
91 (Sept. 13, 2021), App. to Pet. for Cert. 71a. The District
Court determined that Sutton's claim depended on whether
she received a timely forfeiture hearing within the meaning
of $8,850. See id., at 66a–70a. The District Court ruled
that Sutton's forfeiture hearing was timely and satisfed due
process, in part because Sutton never asked for an earlier
hearing. See id., at 70a–71a.
   The U. S. Court of Appeals for the Eleventh Circuit consol-
idated the two cases and affrmed. Culley v. Attorney Gen-
eral, No. 21–13805 etc. (July 11, 2022), App. to Pet. for Cert.
1a–2a. The Court of Appeals agreed with the two district
courts that a timely forfeiture hearing affords claimants due
process and that no separate preliminary hearing is constitu-
tionally required. See id., at 6a–8a. The Court of Appeals
rested its conclusion on circuit precedent, which in turn re-
384                     CULLEY v. MARSHALL

                           Opinion of the Court

lied on this Court's decisions in $8,850 and Von Neumann.
See ibid.
   Because of a conflict in the Courts of Appeals over
whether the Constitution requires a preliminary hearing in
civil forfeiture cases, this Court granted certiorari. See 598
U. S. 1243 (2023). Compare App. to Pet. for Cert. 6a–8a
with Ingram v. Wayne County, 81 F. 4th 603, 620 (CA6 2023);
Krimstock v. Kelly, 306 F. 3d 40, 44 (CA2 2002).1

                                     II
  Under the Due Process Clause of the Fourteenth Amend-
ment as interpreted by this Court, States ordinarily may not
seize real property before providing notice and a hearing.
See United States v. James Daniel Good Real Property, 510
U. S. 43, 62 (1993). But States may immediately seize per-
sonal property (for example, a car) that is subject to civil
forfeiture when the property otherwise could be removed,
Page Proof Pending Publication
destroyed, or concealed before a forfeiture hearing. See
Calero-Toledo v. Pearson Yacht Leasing Co., 416 U. S. 663,
679–680 (1974).
  When States seize and seek civil forfeiture of personal
property, due process requires a timely post-seizure forfeit-
ure hearing. See United States v. Von Neumann, 474 U. S.
242, 247–250 (1986); United States v. $8,850, 461 U. S. 555,
562–565 (1983). In this case, petitioners Culley and Sutton
do not challenge the timeliness of their forfeiture hearings.
Rather, they argue that the Due Process Clause requires

  1
    Before the entry of judgment by the Court of Appeals, Alabama
amended its forfeiture laws to allow an innocent owner to request an “ex-
pedited hearing” “at any time after seizure of property and before entry
of a conviction” in a “related criminal case.” Ala. Code § 15–5–63(3)
(2018); § 20–2–93(l) (Cum. Supp. 2023); see also Ala. Act 2021–497 (effective
Jan. 1, 2022). That amendment did not moot this case because Culley's
and Sutton's requested relief includes money damages against the munici-
palities of Satsuma and Leesburg. See Culley v. Attorney General, No.
21–13805 etc., App. to Pet. for Cert. 6a.
                   Cite as: 601 U. S. 377 (2024)            385

                      Opinion of the Court

States to also hold a separate preliminary hearing before the
forfeiture hearing.
                              A
   Culley and Sutton argue that a preliminary hearing is con-
stitutionally necessary to determine whether States may re-
tain seized personal property pending the ultimate forfeiture
hearing. As petitioners envision it, the preliminary hearing
would focus on the “ `probable validity' ” of the forfeiture.
Krimstock v. Kelly, 306 F. 3d 40, 48 (CA2 2002) (quoting
Commissioner v. Shapiro, 424 U. S. 614, 629 (1976)). The
preliminary hearing would be adversarial, the parties could
introduce evidence and cross-examine witnesses, and prop-
erty owners could raise affrmative defenses, including inno-
cent ownership. In essence, the preliminary hearing would
be an earlier version of the forfeiture hearing itself.
   Alabama and its amici, including the United States, dis-
agree. They argue that a preliminary hearing is not consti-
Page Proof Pending Publication
tutionally required. To begin, they emphasize that most
States and the Federal Government do not currently provide
preliminary hearings in civil forfeiture cases. So requiring
a preliminary hearing as a matter of constitutional dictate
would necessitate a major change in the States' and the Fed-
eral Government's longstanding practices. Alabama and its
amici also contend that a property owner's post-seizure
rights are already protected by the constitutional require-
ment that the forfeiture hearing be timely. They further
assert that requiring a “hearing before a hearing” in every
case, as petitioners want, would interfere with important
law-enforcement activities that must occur after the seizure
and before the forfeiture hearing—including identifying and
contacting potential claimants of the property; coordinating
forfeiture proceedings with related criminal investigations
and prosecutions; and ensuring that property is not removed,
destroyed, or put to illegal use before the forfeiture hearing.
   Ultimately, we need not reweigh the competing due proc-
ess arguments advanced by the parties because this Court's
386                  CULLEY v. MARSHALL

                       Opinion of the Court

decisions in United States v. $8,850, 461 U. S. 555 (1983), and
United States v. Von Neumann, 474 U. S. 242 (1986), already
resolved the issue. After a State seizes and seeks civil for-
feiture of personal property, due process requires a timely
forfeiture hearing but does not require a separate prelimi-
nary hearing.
   The dispute in $8,850 arose when the Customs Service
seized currency from an individual entering the United
States, but then waited before fling for civil forfeiture of the
currency. See 461 U. S., at 558–561. The property owner
argued that the delay violated due process. See id., at 562.
   This Court concluded that a post-seizure delay “may be-
come so prolonged that the dispossessed property owner has
been deprived of a meaningful hearing at a meaningful
time.” Id., at 562–563. The Court elaborated that timeli-
ness in civil forfeiture cases must be assessed by “analog[iz-
ing] . . . to a defendant's right to a speedy trial” and consider-
Page Proof Pending Publication
ing four factors: the length of the delay, the reason for the
delay, whether the property owner asserted his rights, and
whether the delay was prejudicial. Id., at 564 (citing Barker
v. Wingo, 407 U. S. 514, 530 (1972)). Those factors are ap-
propriate guides in the civil forfeiture context, the Court ex-
plained, because the factors ensure that “the fexible require-
ments of due process have been met.” 461 U. S., at 564–565.
   In Von Neumann, the Court addressed whether a timely
forfeiture hearing, without more, provides the process that
is due in civil forfeiture cases. See 474 U. S., at 249–251.
The property owner there failed to declare the purchase of
his new car upon driving it into the United States. See id.,
at 245. A customs offcial determined that the car was sub-
ject to civil forfeiture and seized it. See ibid. The plaintiff
fled a petition for remission of the forfeiture—in essence, a
request under federal law that the Federal Government ex-
ercise its discretion to forgive the forfeiture. See id., at
245–246. The Government did not respond to that petition
for 36 days. See id., at 246. The plaintiff sued, arguing
                       Cite as: 601 U. S. 377 (2024)                   387

                          Opinion of the Court

that the Government's 36-day delay in answering the remis-
sion petition violated due process. See id., at 246–247.
   Justice Brennan's opinion for the Court broadly held that
due process did not require a pre-forfeiture-hearing remis-
sion procedure in the frst place. See id., at 249–251. Cit-
ing $8,850, the Court ruled that a timely “forfeiture proceed-
ing, without more, provides the postseizure hearing required
by due process” to protect the plaintiff 's “property interest
in the car.” 474 U. S., at 249. The Court explained that the
plaintiff 's “right to a forfeiture proceeding” that meets the
$8,850 timeliness test “satisfes any due process right with
respect to the car.” 474 U. S., at 251. A separate remission
hearing is not “constitutionally required.” Id., at 250.2
   This Court's decisions in $8,850 and Von Neumann resolve
this case. As the Court stated in Von Neumann, a timely
forfeiture hearing “satisfes any due process right” with re-
spect to a “car” that has been seized for civil forfeiture. 474
U. S., at 251; see also id., at 249. The Due Process Clause
Page Proof Pending Publication
does not require a separate preliminary hearing.3
   Culley and Sutton's argument for a separate preliminary
hearing appears in many respects to be a backdoor argument
for a more timely hearing so that a property owner with a
good defense against forfeiture can recover her property
more quickly. But the Court's precedents already require a
timely hearing, and a property owner can of course raise
$8,850-based arguments in an individual case to ensure a
timely hearing.
  2
    At oral argument in Von Neumann, Justice O'Connor asked the United
States whether the “forfeiture proceeding itself provides all the process
that's due” to protect the “property interest in the car.” Tr. of Oral Arg.
in United States v. Von Neumann, O. T. 1985, No. 84–1144, p. 18. The
United States answered, “that is our position.” Ibid.; see also id., at 26–
27. The Court subsequently agreed with that position. See Von Neu-
mann, 474 U. S., at 249–251.
  3
    In this opinion, we do not address any due process issues related to
civil forfeiture other than the question about a separate preliminary
hearing.
388                  CULLEY v. MARSHALL

                        Opinion of the Court

   Culley and Sutton (echoed by the dissent here) try to
brush aside Von Neumann on the ground that the statutory
remission procedure in that case was discretionary. See 474
U. S., at 244, and n. 2 (citing 19 U. S. C. § 1618 (1982 ed., Supp.
III)); see also post, at 410–411 (Sotomayor, J., dissenting).
But the discretionary nature of the remission procedure
played no role in the Court's constitutional analysis. See
474 U. S., at 249–251. Culley and Sutton also try to charac-
terize the language in Von Neumann as dicta. We disagree.
The Court ruled for the Government in Von Neumann on
the ground that a timely “forfeiture proceeding, without
more, provides the postseizure hearing required by due proc-
ess” in civil forfeiture cases. Id., at 249. No separate pre-
liminary hearing is constitutionally required.
   Culley and Sutton also contend that Mathews v. Eldridge
should be the test for deciding when additional process is
due and that, under Mathews, a preliminary hearing would
Page Proof Pending Publication
be required in civil forfeiture cases. 424 U. S. 319 (1976).
But this Court decided $8,850 and Von Neumann after Ma-
thews, yet in those two cases, the Court did not apply the
Mathews test. In any event, there is no good reason to
think that the Mathews balancing test would yield a differ-
ent result here. A timely forfeiture hearing protects the
interests of both the claimant and the government. And an
additional preliminary hearing of the kind sought by peti-
tioners would interfere with the government's important
law-enforcement activities in the period after the seizure and
before the forfeiture hearing.
   In arguing that the Constitution requires a preliminary
hearing, Culley and Sutton also point to this Court's Fourth
Amendment decisions in the criminal context. That analogy
is fawed. The Fourth Amendment requires that any person
who is arrested without a warrant be brought before a neu-
tral magistrate within 48 hours, absent extraordinary cir-
cumstances. See County of Riverside v. McLaughlin, 500
U. S. 44, 53, 56–57 (1991). But the Fourth Amendment hear-
                   Cite as: 601 U. S. 377 (2024)            389

                      Opinion of the Court

ings are not adversarial, and they address only whether
probable cause supports the arrestee's detention. See
Gerstein v. Pugh, 420 U. S. 103, 119–122 (1975). Here, Cul-
ley and Sutton do not request a mere probable cause hearing
of the kind described in Gerstein. Rather, they argue that
the immediate seizure of property requires adversarial pre-
liminary hearings, and they assert that those hearings must
address their “affrmative defense” of innocent ownership.
Wallace v. State, 229 So. 3d 1108, 1110 (Ala. Civ. App. 2017).
Culley and Sutton therefore contend that the Due Process
Clause requires more extensive preliminary procedures for
the temporary retention of property than for the temporary
restraint of persons. The Due Process Clause does not de-
mand that incongruity. See United States v. Monsanto, 491
U. S. 600, 615–616 (1989).
   Finally, the dissent here relies heavily on United States v.
James Daniel Good Real Property, 510 U. S. 43. See post,
Page Proof Pending Publication
at 412. There, this Court held that the government must
ordinarily provide notice and a hearing before seizing real
property that is subject to civil forfeiture. See 510 U. S., at
62. The Court emphasized that real property, unlike per-
sonal property, “can be neither moved nor concealed” during
the forfeiture process. Id., at 52–53; see also id., at 56–57.
That case did not purport to disturb the rule that the govern-
ment may seize and retain personal property, such as a car,
that is subject to civil forfeiture when the property other-
wise could be removed, destroyed, or concealed before a for-
feiture hearing. See id., at 57 (citing Calero-Toledo, 416
U. S., at 679). And more to the point, that case did not alter
Von Neumann's holding that a timely forfeiture hearing pro-
vides the process that is due following the immediate seizure
of personal property.
   In sum, Von Neumann held that a timely forfeiture hear-
ing satisfes due process in civil forfeiture cases, and $8,850
specifed the standard for when forfeiture hearings are
timely. Culley and Sutton have not asked the Court to dis-
390                 CULLEY v. MARSHALL

                       Opinion of the Court

card those precedents in this case. And those precedents
make crystal clear that due process does not require a sepa-
rate preliminary hearing before the forfeiture hearing.

                                B
   Historical practice reinforces the holdings of $8,850 and
Von Neumann that due process does not require preliminary
hearings in civil forfeiture cases.
   Since the Founding era, statutes have authorized the Gov-
ernment to seize personal property and hold it pending a
forfeiture hearing, without a separate preliminary hearing.
For example, the frst federal forfeiture law, the Collection
Act of 1789, authorized the civil forfeiture of ships, goods,
and merchandise involved in suspected violations of the cus-
toms laws. See, e. g., Act of July 31, 1789, ch. 5, §§ 12, 22–
24, 34, 1 Stat. 29, 39, 42–43, 46; see generally C. Nelson, The
Constitutionality of Civil Forfeiture, 125 Yale L. J. 2446,
Page Proof Pending Publication
2464–2466 (2016). The Act's forfeiture process began with
the seizure of property by a customs collector. See, e. g.,
§ 25, 1 Stat. 43. The collector then fled a forfeiture action,
which a court would “hear and determine . . . according to
law.” § 36, id., at 47. While that action was pending, the
seized property could “remain in the custody of the collec-
tor.” § 25, id., at 43. A claimant could also recover the
property on bond. See § 36, id., at 47.
   The Collection Act did not require a separate preliminary
hearing before the forfeiture hearing. Rather, the forfeit-
ure “trial” supplied the opportunity for the property owner
to challenge the collector's case. Ibid.
   In 1790 and 1799, Congress revised and reenacted the Col-
lection Act. See Act of Mar. 2, 1799, ch. 22, 1 Stat. 627; Act
of Aug. 4, 1790, ch. 35, 1 Stat. 145. The revised versions of
the Act contained similar forfeiture provisions and likewise
lacked anything resembling a separate preliminary hearing.
See, e. g., Act of Mar. 2, 1799, §§ 69, 89, 1 Stat. 678, 695–696;
Act of Aug. 4, 1790, §§ 49, 67, 1 Stat. 170, 176–177.
                    Cite as: 601 U. S. 377 (2024)             391

                       Opinion of the Court

   Many state forfeiture statutes from the Founding period
similarly did not require a preliminary hearing before the
forfeiture hearing. See, e. g., Act of Apr. 11, 1787, ch. 81, in
2 Laws of the State of New York Passed at the Sessions of
the Legislature Held in the Years 1785, 1786, 1787 and 1788,
Inclusive, pp. 514–515, 517–520 (1886); Act of Oct. 1785,
ch. 14, in 12 The Statutes at Large; Being a Collection of All
the Laws of Virginia, from the First Session of the Legisla-
ture, in the Year 1619, pp. 46–47 (1823). For example, a
New York customs statute from that era provided that a
property owner could recover his seized goods by either pre-
vailing at a forfeiture “trial” or executing a “bond” for an
appraised amount. Act of Apr. 11, 1787, at 517–518. The
statute did not allow property owners to challenge the valid-
ity of the seizure through a separate preliminary hearing or
any similar procedure. See id., at 517–520.
   In addition, when the Fourteenth Amendment was ratifed
Page Proof Pending Publication
in 1868, Congress did not require preliminary hearings. In
1864, for example, Congress provided that goods seized
under a new revenue law should “remain” in the “care and
custody” of the government “until fnal judgment” in a for-
feiture trial. Act of Mar. 7, 1864, ch. 20, § 2, 13 Stat. 14, 15.
Although that revenue law provided for bond, it did not
grant property owners a right to preliminary hearings. See
ibid. Similarly, in 1866, Congress required that goods and
vessels seized under a new customs law “remain in the cus-
tody” of a customs offcial pending “adjudication by the
proper tribunal.” Act of July 18, 1866, ch. 201, § 31, 14 Stat.
178, 186.
   Many state forfeiture laws from around the time of the
Fourteenth Amendment likewise did not provide for a pre-
liminary hearing. For example, a New Hampshire statute
required that a state offcial “detain” personal property that
was seized for civil forfeiture until the property was “legally
disposed of ” through either bond or a forfeiture trial. The
General Statutes of the State of New-Hampshire, ch. 249,
392                 CULLEY v. MARSHALL

                      Opinion of the Court

§§ 3, 6–7, pp. 503–504 (1867). Likewise, a Vermont statute
authorized the seizure of liquor that was intended for sale,
required the seizing offcer to “keep” the liquor “until fnal
action is had thereon,” and limited the conditions in which
a claimant could recover the liquor. The Revised Laws of
Vermont, 1880, § 3818, p. 738 (1881); see § 3827, id., at 740.
   Petitioners and their amici do not identify any federal or
state statutes that, before the late 20th century, required
preliminary hearings in civil forfeiture cases. To be sure,
some States have recently enacted laws requiring prelimi-
nary hearings in civil forfeiture cases. See, e. g., Ala. Act
2021–497, p. 9; 2021 Minn. Laws pp. 2064–2065; 2017 Ill. Laws
pp. 6854–6855; 2017 Wis. Laws p. 815; 2012 Colo. Sess. Laws
pp. 856–857; 2001 N. C. Sess. Laws p. 1159. But those re-
cent laws do not support a constitutional mandate for prelim-
inary hearings in every State.
   In short, both Congress and the States have long author-
ized law enforcement to seize personal property and hold it
Page Proof Pending Publication
until a forfeiture hearing. The absence of separate prelimi-
nary hearings in civil forfeiture proceedings—from the
Founding until the late 20th century—is weighty evidence
that due process does not require such hearings. Cf. United
States v. Ursery, 518 U. S. 267, 274, 287–288 (1996); Bennis v.
Michigan, 516 U. S. 442, 446–448 (1996); Calero-Toledo, 416
U. S., at 680–690. The historical practice in civil forfeiture
proceedings thus reinforces $8,850 and Von Neumann: In
civil forfeiture cases involving personal property such as
cars, the Due Process Clause requires a timely forfeiture
hearing but does not require a preliminary hearing.

                         *     *     *
   To balance the interests of the government and individuals
in civil forfeiture cases involving personal property, the
States and Congress have adopted a wide variety of ap-
proaches. For example, some States require that the for-
feiture hearing occur within a fxed period of time. Others
                   Cite as: 601 U. S. 377 (2024)             393

                     Gorsuch, J., concurring

require a jury trial. Still others condition civil forfeiture on
a successful criminal prosecution. And a few now require
preliminary hearings. See Brief for State of Georgia et al.
as Amici Curiae 5–21.
  Our decision today does not preclude those legislatively
prescribed innovations. Rather, our decision simply ad-
dresses the baseline protection of the Due Process Clause.
  In civil forfeiture cases, the Due Process Clause requires
a timely forfeiture hearing, but does not require a separate
preliminary hearing. We affrm the judgment of the U. S.
Court of Appeals for the Eleventh Circuit.
                                               It is so ordered.

  Justice Gorsuch, with whom Justice Thomas joins,
concurring.
   I agree with the Court that, at a minimum, the Due Proc-
ess Clause requires a prompt hearing in civil forfeiture cases.
Page Proof Pending Publication
Ante, at 384. I agree that no legal authority presented to
us indicates a prompt hearing must necessarily take the form
Ms. Culley and Ms. Sutton suppose. Ante, at 385–386. I
agree, too, that Mathews v. Eldridge, 424 U. S. 319 (1976),
does not teach otherwise. Ante, at 388. Under its terms,
judges balance “the private and governmental interests at
stake,” Mathews, 424 U. S., at 340, to determine “what proce-
dures the government must observe” when it seeks to with-
hold “benefts” “such as welfare or Social Security,” Nelson
v. Colorado, 581 U. S. 128, 141 (2017) (Alito, J., concurring
in judgment). That test does not control—and we do not
afford any particular solicitude to “governmental inter-
ests”—in cases like this one where the government seeks to
deprive an individual of her private property. But if all that
leads me to join today's decision, I also agree with the dissent
that this case leaves many larger questions unresolved about
whether, and to what extent, contemporary civil forfeiture
practices can be squared with the Constitution's promise of
due process. I write separately to highlight some of them.
394                 CULLEY v. MARSHALL

                     Gorsuch, J., concurring

                               I
   The facts of this case are worth pausing over because they
are typical of many. Halima Culley, a Georgia resident,
bought a 2015 Nissan Altima for her son to use while he was
away studying at the University of South Alabama. App.
58, ¶¶22–24. The car belongs to her and she pays for its
registration and insurance. Ibid., ¶¶25–26. The plan was
for her son to bring the car home during the summer for
the family to share. Id., at 60, ¶37. But before that could
happen, a police offcer in Alabama pulled her son over and
arrested him for possessing marijuana and drug parapherna-
lia. Id., at 59, ¶27. The offcer also took the car. Ibid.,
¶28. Eventually, law enforcement offcials learned that the
Nissan belonged to Ms. Culley, not her son. But instead of
returning it, they initiated civil forfeiture proceedings in the
hope of keeping the vehicle permanently. Ibid., ¶¶30–33.
It took a lawsuit and a 20-month wait for the car to make its
Page Proof Pending Publication
way back to her. App. to Pet. for Cert. 3a.
   For Alabama, this was business as usual. Often, the
State's law enforcement agencies may take and keep private
property without a warrant or any other form of prior proc-
ess. Ala. Code § 20–2–93(d) (Cum. Supp. 2023). Instead,
only after taking the property must the agency fle a civil
forfeiture action in court. Once there, the agency need
present only a “prima facie” case that the property in
question represents proceeds “traceable” to a drug crime or
property used to “facilitate” one. §§ 20–2–93(b)(3), (b)(5);
Ex parte McConathy, 911 So. 2d 677, 681 (Ala. 2005). If the
agency proves just that much, the burden sometimes shifts
to the property's owner to prove she was an “innocent
owner” who did not know about or consent to the conduct
that caused the property to be taken. §§ 20–2–93(w), (a)(4).
Should the agency prevail in the end, it may keep the
property for its own use or sell it and keep the money.
§ 20–2–93(s).
                   Cite as: 601 U. S. 377 (2024)             395

                     Gorsuch, J., concurring

   Laws like Alabama's exist in many States and at the fed-
eral level. But as commonplace as these civil forfeiture laws
may be, most are pretty new. As part of the War on Drugs,
in the 1970s and 1980s Congress began enacting sweeping
new civil forfeiture statutes allowing the government to
seize and keep the proceeds of drug crimes and the personal
property used to facilitate them. See S. Cassella, Asset
Forfeiture Law in the United States § 2–4, p. 48 (3d ed. 2022).
Since then, the federal government has extended similar civil
forfeiture rules to most federal offenses. Id., at 49. Today,
it appears, “[w]hite-collar and frearms crimes” now “ac-
coun[t] for larger shares of all [federal] forfeitures than drug
crimes.” L. Knepper, J. McDonald, K. Sanchez, & E. Pohl,
Policing for Proft: The Abuse of Civil Asset Forfeiture 26
(3d ed. 2020) (Knepper). Following the federal govern-
ment's lead, many States have adopted similar laws of their
own. See id., at 170–185.
Page Proof Pending Publication
   These new laws have altered law enforcement practices
across the Nation in profound ways. My dissenting col-
leagues catalogue a number of examples, see post, at 405–
408 (opinion of Sotomayor, J.), but consider just a few here.
To secure a criminal penalty like a fne, disgorgement of ille-
gal profts, or restitution, the government must comply with
strict procedural rules and prove the defendant's guilt be-
yond a reasonable doubt. In re Winship, 397 U. S. 358, 363
(1970). In civil forfeiture, however, the government can
simply take the property and later proceed to court to earn
the right to keep it under a far more forgiving burden of
proof. See Knepper 39. In part thanks to this asymmetry,
civil forfeiture has become a booming business. In 2018,
federal forfeitures alone brought in $2.5 billion. Id., at 15.
Meanwhile, according to some reports, these days “up to 80%
of civil forfeitures are not accompanied by a criminal convic-
tion.” Brief for Buckeye Institute as Amicus Curiae 14
(Buckeye Brief).
396                 CULLEY v. MARSHALL

                     Gorsuch, J., concurring

   Law enforcement agencies have become increasingly de-
pendent on the money they raise from civil forfeitures. The
federal government shares a large portion of what it receives
with state and local law enforcement agencies that aid its
forfeiture efforts. Dept. of Justice & Dept. of Treasury,
Guide to Equitable Sharing for State, Local, and Tribal Law
Enforcement Agencies 3, 12 (Mar. 2024). At one time or an-
other, “[o]ver 90% of the agencies serving jurisdictions with
populations” above 250,000 have participated in this “equita-
ble sharing” scheme. E. Jensen & J. Gerber, The Civil For-
feiture of Assets and the War on Drugs: Expanding Criminal
Sanctions While Reducing Due Process Protections, 42
Crime & Delinquency 421, 425 (1996). And it seems that,
when local law enforcement budgets tighten, forfeiture activ-
ity often increases. B. Kelly, Fighting Crime or Raising
Revenue? Testing Opposing Views of Forfeiture 15 (2019).
   Not only do law enforcement agencies have strong fnancial
Page Proof Pending Publication
incentives to pursue forfeitures, those incentives also appear
to infuence how they conduct them. Some agencies, for ex-
ample, reportedly place special emphasis on seizing low-
value items and relatively small amounts of cash, hopeful
their actions won't be contested because the cost of litigating
to retrieve the property may cost more than the value of
the property itself. See Knepper 9. Other agencies seem
to prioritize seizures they can monetize rather than those
they cannot, posing for example as drug dealers rather than
buyers so they can seize the buyer's cash rather than illicit
drugs that hold no value for law enforcement. See Buckeye
Brief 7–8.
   Delay can work to these agencies' advantage as well. See
Brief for Institute for Justice et al. as Amici Curiae 16.
Faced with the prospect of waiting months or years to secure
the return of a car or some other valuable piece of property
they need to work and live, even innocent owners sometimes
“settle” by “paying a fee to get it back.” Knepper 36. Con-
tributing to the inducement to settle is how little proof the
                   Cite as: 601 U. S. 377 (2024)             397

                     Gorsuch, J., concurring

agencies must produce to win forfeiture, the cost of liti-
gation, and the need to appear in court—sometimes, as
Ms. Culley learned, in a different State. And if these tactics
and burdens work against all affected individuals, can it be
any surprise “the poor and other groups least able to defend
their interests” often suffer most? Leonard v. Texas, 580
U. S. 1178, 1180 (2017) (statement of Thomas, J., respecting
denial of certiorari); see post, at 406–407.

                                II
   To my mind, the due process questions surrounding these
relatively new civil forfeiture practices are many. Start
with the most fundamental one. The Fifth and Fourteenth
Amendments guarantee that no government in this country
may take “life, liberty, or property, without due process of
law.” As originally understood, this promise usually meant
that a government seeking to deprive an individual of her
Page Proof Pending Publication
property could do so only after a trial before a jury in which
it (not the individual) bore the burden of proof. See, e. g., 1
W. Blackstone, Commentaries on the Laws of England 134–
135 (1765) (Blackstone); Vanhorne's Lessee v. Dorrance, 2
Dall. 304, 315 (CC Pa. 1795) (Paterson, J.); Wilkinson v.
Leland, 2 Pet. 627, 657 (1829) (Story, J.). So how is it that,
in civil forfeiture, the government may confscate property
frst and provide process later?
   The answer, if there is one, turns on history. If, as a rule,
the Due Process Clauses require governments to conduct a
trial before taking property, some exceptions are just as
deeply rooted. And for just that reason, these exceptions,
too, may be consistent with the original meaning of the Fifth
and Fourteenth Amendments. As this Court has put it, “a
process of law . . . must be taken to be due process of law”
if it enjoys “the sanction of settled usage both in England
and in this country.” Hurtado v. California, 110 U. S. 516,
528 (1884); see, e. g., Murray's Lessee v. Hoboken Land &
Improvement Co., 18 How. 272, 278–280 (1856).
398                 CULLEY v. MARSHALL

                     Gorsuch, J., concurring

   But can contemporary civil forfeiture practices boast that
kind of pedigree? In Calero-Toledo v. Pearson Yacht Leas-
ing Co., 416 U. S. 663 (1974), this Court noted that English
and early American admiralty laws allowed the government
to seize a vessel involved in “piratical” or other maritime
offenses and later initiate postdeprivation civil forfeiture
proceedings. Id., at 684. The Court observed that similar
legal rules existed for cases involving “objects used in viola-
tion of the customs and revenue laws.” Id., at 682; see also
K. Arlyck, The Founders' Forfeiture, 119 Colum. L. Rev.
1449, 1466 (2019). After emphasizing the existence of those
traditions, the Court proceeded to uphold the civil forfeiture
of a boat. Calero-Toledo, 416 U. S., at 682, 690. Later and
proceeding on much the same basis, the Court approved vari-
ous aspects of civil forfeiture practice in the context of cus-
toms enforcement actions. See United States v. $8,850, 461
U. S. 555, 562, n. 12 (1983); United States v. Von Neumann,
Page Proof Pending Publication
474 U. S. 242, 249, n. 7 (1986).
   These historical traditions suggest that postdeprivation
civil forfeiture processes in the discrete arenas of admiralty,
customs, and revenue law may satisfy the Constitution. But
as the Court stressed in Von Neumann, “the general rule”
remains that the government cannot “ `seize a person's prop-
erty without a prior judicial determination that the seizure
is justifed.' ” Id., at 249, n. 7. And it is far from clear to
me whether the postdeprivation practices historically toler-
ated inside the admiralty, customs, and revenue contexts
enjoy “the sanction of settled usage” outside them. Hur-
tado, 110 U. S., at 528.
   The reasons for the law's traditionally permissive attitude
toward civil forfeiture in those three contexts may merit ex-
ploration, too. From a brief look, it seems they were some-
times justifed for reasons particular to their felds. In the
early Republic, for example, once a ship involved in viola-
tions of the Nation's piracy or customs laws slipped port for a
foreign destination, American courts often could not exercise
                   Cite as: 601 U. S. 377 (2024)            399

                     Gorsuch, J., concurring

jurisdiction over it or its crew, let alone its owners. See R.
Waples, Proceedings in Rem § 19, p. 22 (1882) (Waples). In
many instances, the law recognized that seizing the ship,
subject to postdeprivation procedures, represented “the only
adequate means of suppressing the offence or wrong, or in-
suring an indemnity to the injured party.” Harmony v.
United States, 2 How. 210, 233 (1844) (Story, J.); see also 3
Blackstone 262 (1768) ( justifying civil forfeiture in customs
cases as necessary “to secure such forfeited goods for the
public use, though the offender himself had escaped the reach
of justice”). But if history sanctions that line of thinking,
it's hard not to wonder: How does any of that support the
use of civil forfeiture in so many cases today, where the gov-
ernment can secure personal jurisdiction over the wrong-
doer? And where seizing his property is not the only ade-
quate means of addressing his offense?
   Even supposing some modern civil forfeiture regimes are
Page Proof Pending Publication
able to claim the sanction of history, I wonder whether all
their particulars might. In the past, it seems the govern-
ment could confscate only certain classes of property. So,
for example, admiralty statutes regularly authorized the
government to seize and pursue the civil forfeiture of “the
instrument[s] of the offence,” say, a ship used to engage in
piracy. Smith v. Maryland, 18 How. 71, 75 (1855); see Har-
mony, 2 How., at 233. But statutes like that did not neces-
sarily mean forfeiture extended to the vessel's cargo, and
courts were loath to assume they did. Id., at 235. Today,
by contrast, civil forfeiture statutes routinely permit govern-
ments to confscate not just instruments used in an offense,
but other “facilitating” property as well. See supra, at 395.
(In this respect, Alabama's statute is again illustrative.)
And if that difference seems a small one, it is anything but:
It is the difference between being able to confscate the ma-
terials and equipment used to produce an illicit drug and
being able to confscate someone's car after he used it as the
site to conduct a single drug transaction as either buyer or
400                 CULLEY v. MARSHALL

                     Gorsuch, J., concurring

seller. See Austin v. United States, 509 U. S. 602, 627–
628 (1993) (Scalia, J., concurring in part and concurring in
judgment).
   Even in the areas where the law tolerated civil forfeiture,
earlier generations tempered some of its harshest features.
Courts, for example, ordinarily entertained “overwhelming
necessity” as a defense to “the violation of revenue laws”
that might otherwise justify forfeiture. 1 J. Bishop, Com-
mentaries on the Criminal Law § 697, p. 575 (1856) (Bishop);
see Peisch v. Ware, 4 Cranch 347, 363 (1808) (Marshall, C. J.)
(“[A] forfeiture can only be applied to those cases in which
the means that are prescribed for the prevention of a forfeit-
ure may be employed”). Some statutes permitted the
owner to avoid forfeiture by proving that the violation “pro-
ceeded from accident or mistake.” 1 Stat. 677; see United
States v. Nine Packages of Linen, 27 F. Cas. 154, 157
(No. 15,884) (CC NY 1818); Bishop § 697, at 575; cf. 3 Stat. 183
Page Proof Pending Publication
(no forfeiture of goods from “bona fde purchaser”). Others
empowered the Treasury Secretary himself to afford the
same remedy—and evidence suggests offcials “were exceed-
ingly liberal in their use of the . . . power, granting relief
in the overwhelming majority of cases presented to them.”
Arlyck, 119 Colum. L. Rev., at 1487; see also The Laura, 114
U. S. 411, 414–415 (1885). These days, meanwhile, many
civil forfeiture statutes lack some or all of these mitigating
features. I acknowledge that this Court has suggested an
innocent owner defense is not always constitutionally re-
quired. Bennis v. Michigan, 516 U. S. 442, 443 (1996); see
id., at 455–457 (Thomas, J., concurring) (discussing limits to
the Court's holding); id., at 457–458 (Ginsburg, J., concurring)
(same). But even putting that debate aside, what of early
forfeiture's other ameliorative attributes?
   It appears, too, that time was often of the essence in tradi-
tional civil forfeiture practice. So, for example, an early fed-
eral statute permitting forfeiture for nonpayment of internal
duties “enjoined” the “collector” “to cause suits for [forfeit-
                   Cite as: 601 U. S. 377 (2024)            401

                     Gorsuch, J., concurring

ure] to be commenced without delay, and prosecuted to ef-
fect.” 3 Stat. 242. In an admiralty case, Chief Justice Mar-
shall remarked, “If the seizing offcer should refuse to
institute proceedings to ascertain the forfeiture, the district
court may, upon the application of the aggrieved party, com-
pel the offcer to proceed to adjudication, or to abandon the
seizure.” Slocum v. Mayberry, 2 Wheat. 1, 10 (1817). And
in many instances owners could recover their property while
the forfeiture proceedings were ongoing by posting a bond.
See, e. g., 3 Stat. 242; United States v. Ames, 99 U. S. 35, 36
(1879); Waples § 81, at 112; ante, at 391. It's another feature
of historic practice that raises questions about current ones
in which even innocent owners can wait for months or years
for forfeiture proceedings to play out.

                               III
   Why does a Nation so jealous of its liberties tolerate ex-
Page Proof Pending Publication
pansive new civil forfeiture practices that have “led to egre-
gious and well-chronicled abuses” ? Leonard, 580 U. S., at
1180 (statement of Thomas, J.). Perhaps it has something
to do with the relative lack of power of those on whom the
system preys. Perhaps government agencies' increasing de-
pendence on forfeiture as a source of revenue is an important
piece of the puzzle. Cf. Calero-Toledo, 416 U. S., at 679 (in-
dicating, over 50 years ago and before the rise of many mod-
ern innovations, that “self-interes[t]” did not motivate the
forfeiture of the vessel at issue). But maybe, too, part of
the reason lies closer to home. In this Nation, the right to
a jury trial before the government may take life, liberty,
or property has always been the rule. Yes, some excep-
tions exist. But perhaps it is past time for this Court to
examine more fully whether and to what degree contempo-
rary civil forfeiture practices align with that rule and those
exceptions.
   Really, it's hard not to wonder whether some current civil
forfeiture practices represent much less than a revival of the
402                 CULLEY v. MARSHALL

                     Gorsuch, J., concurring

archaic common-law deodand. The deodand required the
forfeiture of any object responsible for a death—say, a knife,
cart, or horse—to the Crown. See 1 Blackstone 290.
Today, the idea seems much the same even if the practice
now sweeps more broadly, requiring almost any object in-
volved in almost any serious offense to be surrendered to the
government in amends.
   The hardships deodands often imposed seem more than
faintly familiar, too. Deodands required forfeiture regard-
less of the fault of the owner, himself sometimes the de-
ceased. Not infrequently, the practice left impoverished
families without the means to support themselves, faced not
only with the loss of a loved one but also with the loss of a
horse or perhaps a cart essential to their livelihoods. See 2
F. Pollock & F. Maitland, The History of English Law 472
(1895); E. Burke, Deodand—A Legal Antiquity That May
Still Exist, 8 Chi.-Kent L. Rev. 15, 17, 19–20 (1930). Some-
Page Proof Pending Publication
times grieving families could persuade authorities or juries
to forgo a deodand, but often not, and generally the burden
to avoid a deodand was on them. See M. Foster, Crown Law
266 (1762).
   As time went on, too, curiously familiar fnancial incentives
wormed their way into the system. Originally, the Crown
was supposed to pass the deodand (literally, a thing given to
God) onto the church “as an expiation for the sou[l]” of the
deceased. 1 Blackstone 290. Over time, though, the Crown
increasingly chose instead to sell off its rights to deodands
to local lords and others. These recipients inevitably wound
up with a strong interest in the perpetuation of the enter-
prise. See id., at 292. Ultimately, the deodand's appeal
faded in England, and this Court has held that it “did not
become part of the common-law tradition of this country.”
Calero-Toledo, 416 U. S., at 682; see id., at 681, n. 19. But
has something not wholly unlike it gradually reemerged in
our own lifetimes?
                   Cite as: 601 U. S. 377 (2024)           403

                    Sotomayor, J., dissenting

                                *
   In asking the questions I do today, I do not profess a com-
prehensive list, let alone any frm answers. Nor does the
way the parties have chosen to litigate this case give cause
to supply them. But in future cases, with the beneft of full
briefng, I hope we might begin the task of assessing how
well the profound changes in civil forfeiture practices we
have witnessed in recent decades comport with the Constitu-
tion's enduring guarantee that “[n]o person shall . . . be de-
prived of life, liberty, or property, without due process of
law.”
  Justice Sotomayor, with whom Justice Kagan and
Justice Jackson join, dissenting.
   A police offcer can seize your car if he claims it is con-
nected to a crime committed by someone else. The police
department can then keep the car for months or even years
Page Proof Pending Publication
until the State ultimately seeks ownership of it through civil
forfeiture. In most States, the resulting proceeds from the
car's sale go to the police department's budget. Petitioners
claim that the Due Process Clause requires a prompt, post-
seizure opportunity for innocent car owners to argue to a
judge why they should retain their cars pending that fnal
forfeiture determination. When an offcer has a fnancial in-
centive to hold onto a car and an owner pleads innocence,
they argue, a retention hearing at least ensures that the of-
fcer has probable cause to connect the owner and the car to
a crime.
   Today, the Court holds that the Due Process Clause never
requires that minimal safeguard. In doing so, it sweeps
far more broadly than the narrow question presented and
hamstrings lower courts from addressing myriad abuses of
the civil forfeiture system. Because I would have decided
only which due process test governs whether a retention
hearing is required and left it to the lower courts to apply
404                  CULLEY v. MARSHALL

                     Sotomayor, J., dissenting

that test to different civil forfeiture schemes, I respectfully
dissent.
                                I
                                A
   Civil forfeiture occupies a murky space between criminal
forfeiture and ordinary government deprivations of property.
Criminal forfeiture is part of a defendant's criminal punish-
ment. The government must therefore proceed against the
person (in personam) to obtain someone's property via crim-
inal forfeiture, which generally requires notice of intent to
forfeit the property in a criminal indictment and full criminal
procedural protections for the defendant. At the outset, the
government must typically prove that it has probable cause
to seize the person for a specifc crime and therefore to hold
any property related to that crime. See Gerstein v. Pugh,
420 U. S. 103 (1975).
   Outside the criminal context, the government usually must
Page Proof Pending Publication
provide a hearing before depriving someone of essential
property. See, e. g., Goldberg v. Kelly, 397 U. S. 254, 264–
266 (1970) (public assistance); Bell v. Burson, 402 U. S. 535,
542–543 (1971) (driver's license); Fuentes v. Shevin, 407 U. S.
67, 96–97 (1972) (household goods to which a creditor lays a
claim). In some circumstances “the necessity of quick action
by the State” may prevent a predeprivation hearing. Par-
ratt v. Taylor, 451 U. S. 527, 539 (1981), overruled on other
grounds, Daniels v. Williams, 474 U. S. 327 (1986). Then,
however, the government must make “availab[le] . . . some
meaningful means by which to assess the propriety of the
State's action at some time after the initial [seizure], [to] sat-
isfy the requirements of procedural due process.” 451 U. S.,
at 539.
   Civil forfeiture is a hybrid, where prosecutors proceed
against any property (in rem) they believe is connected to a
crime, even when the owner is innocent. Unlike criminal
forfeiture, civil forfeiture proceedings are untethered from
                    Cite as: 601 U. S. 377 (2024)             405

                     Sotomayor, J., dissenting

any criminal prosecution. In fact, as many as 80% of civil
forfeitures are not accompanied by any ultimate criminal
conviction. Brief for Buckeye Institute as Amicus Curiae
14. Civil forfeiture is unnecessary where the government
pursues criminal forfeiture in an indictment and sustains a
conviction. Only if an offcer seizes property that he be-
lieves is connected to a crime, but does not belong to a de-
fendant charged with that crime, must prosecutors bring
civil forfeiture proceedings outside a criminal case. Even
when the State abandons the prosecution that formed the
basis for the seizure, an innocent property owner can be left
in civil forfeiture proceedings trying to get her property
back.
                               B
   The Federal Government, States, and localities set their
own rules for civil forfeiture, subject only to the limits of the
Due Process Clause. This lack of standardized procedural
Page Proof Pending Publication
safeguards makes civil forfeiture vulnerable to abuse. In 32
States and the federal system, when law enforcement agen-
cies forfeit property, the proceeds go to their own budgets.
Brief for Institute for Justice et al. as Amici Curiae 4. As
a result, police agencies often have a fnancial incentive to
seize as many cars as possible and try to retain them. The
forfeiture revenue is not a supplement; many police agencies
in fact depend on cash fow from forfeitures for their budgets.
See, e. g., J. Worrall & T. Kovandzic, Is Policing for Proft?
Answers From Asset Forfeiture, 7 Criminology & Pub. Pol'y
219, 222 (2008) (“[M]ore than 60% of police agencies surveyed
reported dependence on asset forfeiture”). These cash in-
centives not only encourage counties to create labyrinthine
processes for retrieving property in the hopes that innocent
owners will abandon attempts at recovery, they also infu-
ence which laws police enforce, how they enforce them, and
who they enforce them against. See Brief for Buckeye In-
stitute as Amicus Curiae 6–20 (detailing empirical studies
406                 CULLEY v. MARSHALL

                    Sotomayor, J., dissenting

on the effect of fscal incentives in civil forfeiture on law en-
forcement decisionmaking).
   Police offcers have an incentive to enforce the law in a
way that leads to the recovery of fungible property, like cash
or cars. For example, offcers might pose as drug dealers
instead of buyers in a sting operation, because “it allows po-
lice to seize a buyer's cash rather than a seller's drugs (which
have no legal value to the seizing agency).” E. Blumen-
son & E. Nilsen, Policing for Proft: The Drug War's Hidden
Economic Agenda, 65 U. Chi. L. Rev. 35, 67 (1998). Simi-
larly, police offcers might target low-level drug possession
in cars instead of drug transactions on the street, so that
they can seize the vehicle. In this case, police offcers pulled
over petitioner Halima Tariffa Culley's college-age son while
he was driving a car registered to her, charged him with
possession of marijuana, and seized the car. A police offcer
cannot sell recovered marijuana and a prosecutor's offce
Page Proof Pending Publication
does not ordinarily pursue low-level marijuana offenses.
When a police department can recover the proceeds from a
car civilly forfeited in connection to a low-level marijuana
offense, however, targeting that offense becomes more
appealing.
   Moreover, offcers have a fnancial incentive to target mar-
ginalized groups, such as low-income communities of color,
who are less likely to have the resources to challenge the
forfeiture in court. See A. Crawford, Civil Asset Forfeiture
in Massachusetts: A Flawed Incentive Structure and Its Im-
pact on Indigent Property Owners, 35 Boston College J. L. &
Soc. Justice 257, 274–277 (2015) (“[O]ne way for law enforce-
ment agencies to generate profts is to target low-income
parties who are fnancially incapable of challenging sei-
zures”). A 2019 study found that “the seizure of nonnarcotic
property from black and Hispanic arrestees increases with
the size of the [budget] defcit in states where police depart-
ments can retain revenue from seized property.” M. Ma-
kowsky, T. Stratmann, & A. Tabarrok, To Serve and Collect:
                   Cite as: 601 U. S. 377 (2024)             407

                    Sotomayor, J., dissenting

The Fiscal and Racial Determinants of Law Enforcement, 48
J. Legal Studies 189, 208–209.
   “[T]hese same groups are often the most burdened by for-
feiture,” because “they are more likely to suffer in their daily
lives while they litigate for the return of a critical item of
property, such as a car.” Leonard v. Texas, 580 U. S. 1178,
1180 (2017) (statement of Thomas, J., respecting denial of
certiorari). For many people, loss of access to a car, even
temporarily, is signifcant. Over 85% of Americans drive to
work. J. Hirsch & P. Jones, Driver's License Suspension for
Unpaid Fines and Fees: The Movement for Reform, 54
U. Mich. J. L. Reform 875, 881 (2021). Unsurprisingly, stud-
ies have found a link between the inability to drive and the
loss of a job. For example, “[i]n New Jersey, 42% of people
lost their jobs after their driver's license was suspended.”
Ibid. Loss of a car not only “takes away one's ability to
commute” but also imposes a barrier to “buy[ing] necessi-
Page Proof Pending Publication
ties, access[ing] healthcare, and visit[ing] family members,
pharmacies, grocery stores, hospitals, and other essential
services.” Ibid.
   Given these burdens, low-income communities are also the
most vulnerable to pressure from unchecked prosecutors,
who can use coercive civil forfeiture processes to extract set-
tlement money from innocent owners desperate to get their
property back. See Brief for Institute for Justice et al. as
Amici Curiae 19–20 (detailing examples). In Detroit, to
take one example, car owners recently alleged that Wayne
County seizes vehicles in areas generally associated with
crime and holds on to the vehicles and their contents unless
the owners pay steep redemption fees: $900 for the frst sei-
zure; $1,800 for the second; and $2,700 for the third. See
Ingram v. Wayne Cty., 81 F. 4th 603, 606 (CA6 2023). If the
owner is unwilling or unable to pay this fee, she must either
abandon the vehicle or wait for county prosecutors to decide
whether to initiate forfeiture proceedings. Before such pro-
ceedings are brought, however, the owner allegedly must at-
408                     CULLEY v. MARSHALL

                        Sotomayor, J., dissenting

tend four or more pretrial conferences during regular work
hours, during which the owner typically will not get to plead
her case to a judge. Instead, prosecutors will attempt to
persuade her to pay the redemption fee, towing costs, and
storage fees. Missing just one conference allegedly will re-
sult in automatic forfeiture and transfer of title to the
county.
   Similarly, in Massachusetts, one investigation found over
500 instances in a single county where law enforcement held
property for a decade or more before offcials fnally com-
menced forfeiture proceedings. S. Datar & S. Dooling, Mas-
sachusetts Police Can Easily Seize Your Money. The DA of
One County Makes It Nearly Impossible To Get It Back,
ProPublica (Aug. 18, 2021), www.propublica.org/article/
massachusetts-police-can-easily-seize-your-money.-the-da-of-
one-county-makes-it-near-impossible-to-get-it-back. In
other words, those owners had to wait more than a decade
for the chance to explain to a judge why they should get
Page Proof Pending Publication
their property back. In one instance, prosecutors ran a
newspaper notice four years after a seizure, at which point
the property owner had only 20 days to file a claim to avoid
forfeiture. Similar delays have been reported in South Car-
olina, Oklahoma, and Pennsylvania. See Brief for Institute
for Justice et al. as Amici Curiae 16 (collecting studies).
   In short, law enforcement can seize cars, hold them in-
defnitely, and then rely on an owner's lack of resources to
forfeit those cars to fund agency budgets, all without any
initial check by a judge as to whether there is a basis to hold
the car in the frst place.
                               II
   This Court granted certiorari to address which of its tests
should govern due process challenges that seek a retention
hearing after an offcer seizes a car.1 Now, the Court
  1
   See Pet. for Cert. i (“In determining whether the Due Process Clause
requires a state or local government to provide a post seizure probable
cause hearing prior to a statutory judicial forfeiture proceeding and, if so,
                       Cite as: 601 U. S. 377 (2024)                     409

                        Sotomayor, J., dissenting

reaches far beyond that question to hold that people whose
cars are seized by the police never have a due process right
to a retention hearing. The Court arrives at this conclusion
by relying on two customs cases from the 1980s and histori-
cal practice that purportedly reinforces their application.
Its reasoning is deeply fawed.

                                     A
   The majority says that “[t]his Court's decisions in $8,850
and Von Neumann resolve this case.” Ante, at 387. These
cases, however, have little to say about what due process
requires when an innocent owner seeks to retain her car
pending an ultimate forfeiture determination in schemes like
those described above. Instead, the claimants in these cases
argued that the United States Customs Service took too long
to resolve forfeiture proceedings against property seized at
the border as part of the claimants' own alleged violations of
Page Proof Pending Publication
customs law.
   In United States v. $8,850, 461 U. S. 555, 558 (1983), a cus-
toms inspector seized $8,850 in cash from Mary Josephine
Vasquez, who had declared she was carrying less than $5,000.
Vasquez was charged with a felony and a misdemeanor, with
the indictment seeking forfeiture of the $8,850 as part of the
misdemeanor charge. When a jury ultimately convicted
Vasquez of only the felony count, which did not contain the
forfeiture allegations, the Government fnally fled civil for-
feiture proceedings against the cash. Vasquez argued only
that the Government's 18-month delay in fling civil forfeit-
ure proceedings was unconstitutionally long. To evaluate
her claim, the Court borrowed the Barker v. Wingo multifac-

when such a hearing must take place, should district courts apply the
`speedy trial' test employed in United States v. $8,850, 461 U. S. 555 (1983)
and Barker v. Wingo, 407 U. S. 514 (1972), as held by the Eleventh Circuit
or the three-part due process analysis set forth in Mathews v. Eldridge,
424 U. S. 319 (1976) as held by at least the Second, Fifth, Seventh, and
Ninth Circuits”).
410                 CULLEY v. MARSHALL

                    Sotomayor, J., dissenting

tor test from the speedy-trial context and held that “the bal-
ance of factors indicate[d] that the Government's delay . . .
was reasonable” in the circumstances. 461 U. S., at 569; see
id., at 564 (citing Barker v. Wingo, 407 U. S. 514 (1972)). In
so holding, the Court emphasized that the Government had
“diligent[ ly]” pursued the pending criminal proceedings
against Vasquez. 461 U. S., at 568. Because a conviction on
the misdemeanor count could have rendered civil forfeiture
unnecessary, the Government's delay in fling a civil forfeit-
ure proceeding was understandable. Ibid.
   In United States v. Von Neumann, 474 U. S. 242, 245
(1986), Von Neumann failed to declare a newly purchased
Jaguar Panther car to customs offcials when he drove it back
to the United States. United States Customs seized the car,
and Von Neumann fled a petition for administrative remis-
sion proceedings the same day. Two weeks later, he posted
a bond and regained possession of the car. Thirty-six days
Page Proof Pending Publication
after he fled his remission petition, Customs resolved it by
reducing Von Neumann's penalty for failure to declare to
$3,600.
   Von Neumann argued that the 36-day delay in responding
to his administrative remission petition violated due process.
The Government responded that “due process considerations
do not govern the Secretary's disposition of [administrative]
remission petitions.” Id., at 249. The Court agreed with
the Government. “Implicit in this Court's discussion of
timeliness in $8,850 was the view that the [regular civil] for-
feiture proceeding, without more, provides the postseizure
hearing required by due process to protect Von Neumann's
property interest in [his] car.” Ibid. The administrative
proceedings did not trigger a separate due process right, the
Court continued, because they were discretionary and “not
necessary to a forfeiture determination.” Id., at 250.
   The Court then declined to address the argument that the
remission statute “itself creates a property right which can-
not be taken away without due process.” Ibid. “[E]ven if
                      Cite as: 601 U. S. 377 (2024)                   411

                        Sotomayor, J., dissenting

respondent had such a property right,” the Court explained,
“any due process requirement of timely disposition was more
than adequately provided here.” Ibid. The Court had “al-
ready noted that his right to a forfeiture proceeding meeting
the Barker test satisfes any due process right with respect
to the car and the money.” Id., at 251. Von Neumann had
also failed to show “what prejudice [he] suffered from the
36-day delay in the response” to his remission petition. Id.,
at 250.
   The majority takes Von Neumann's imprecise categorical
language out of this vital context to hold that “a timely for-
feiture hearing `satisfes any due process right' with respect
to a `car' that has been seized for civil forfeiture.” Ante, at
387 (quoting Von Neumann, 474 U. S., at 251).2 In doing so,
it extends the holdings of both Von Neumann and $8,850 to
situations neither Court contemplated. In both, the Gov-
ernment sought to forfeit property tied to the claimants' un-
lawful conduct. The claimants were not, and did not claim
Page Proof Pending Publication
to be, innocent owners of property used for criminal ends
without their knowledge. Unlike petitioners here, neither
the claimant in $8,850 nor the claimant in Von Neumann had
argued that a retention hearing was necessary to test Cus-
toms' justifcation for seizing their property at the outset.
Instead, both argued only that the Government took too long
to resolve their proceedings: in $8,850 through a statutory
process, and in Von Neumann through a discretionary ad-
ministrative one. The majority's reading here improperly
resolves a constitutional challenge that the Court in those
cases had no cause or reason to address.
                                    B
  With the sole exception of the Eleventh Circuit, every
court of appeals has rejected Von Neumann's application to
  2
   Perhaps recognizing that it stretches the reasoning of the opinion, the
majority relies in a footnote on statements made at oral argument. See
ante, at 387, n. 2.
412                     CULLEY v. MARSHALL

                        Sotomayor, J., dissenting

state and county civil forfeiture schemes concerning claim-
ants' cars.3 Indeed, this Court has distinguished Von Neu-
mann in contexts where offcers have a fnancial incentive
to seize property and owners may assert innocence of the
underlying crime as a defense. In United States v. James
Daniel Good Real Property, 510 U. S. 43, 46 (1993), for exam-
ple, this Court held that the Government must conduct a
predeprivation hearing before it seizes real property con-
nected to criminal conduct through civil forfeiture. Four
years after James Daniel Good pleaded guilty to state
charges based on drugs found in his home, the Federal Gov-
ernment fled civil forfeiture proceedings against his home.
Even though Good did not assert innocence, the Court em-
phasized that proceedings without a predeprivation hearing
created an unacceptable risk of error for property owners
asserting an “innocent owner” defense, because waiting until
the fnal forfeiture hearing “ `would not cure the temporary
deprivation that an earlier hearing might have prevented.' ”
Page Proof Pending Publication
Id., at 56. Crucial to the Court's reasoning was the fact that
“the Government has a direct pecuniary interest in the out-
come of the proceeding” when it is entitled to forfeit the
property. Id., at 55–56.
   This reasoning applies directly to due process challenges
where police seize the cars of innocent owners and use for-
feiture proceeds to fund department budgets. The narrow
holdings of $8,850 and Von Neumann should not determine
the due process claims of every claimant deprived of access
to her car by state prosecutors on untested grounds for
months or years.

  3
    See Ingram v. Wayne Cty., 81 F. 4th 603, 616–617 (CA6 2023); Serrano
v. CBP, 975 F. 3d 488, 500 (CA5 2020) (per curiam); Smith v. Chicago, 524
F. 3d 834, 837–838 (CA7 2008), vacated as moot, Alvarez v. Smith, 558 U. S.
87 (2009); Krimstock v. Kelly, 306 F. 3d 40, 52, n. 12 (CA2 2002) (Soto-
mayor, J.); cf. Booker v. St. Paul, 762 F. 3d 730 (CA8 2014) (declining to
reference Von Neumann).
                   Cite as: 601 U. S. 377 (2024)            413

                    Sotomayor, J., dissenting

                               III
   The majority's categorical rule that due process never re-
quires a retention hearing also cannot be squared with the
context-specifc analysis that this Court's due process doc-
trine requires. “ `[D]ue process,' unlike some legal rules, is
not a technical conception with a fxed content unrelated to
time, place and circumstances.” Cafeteria & Restaurant
Workers v. McElroy, 367 U. S. 886, 895 (1961) (alteration in
original). “[D]ue process is fexible and calls for such pro-
cedural protections as the particular situation demands.”
Morrissey v. Brewer, 408 U. S. 471, 481 (1972).
   The Court granted this case to resolve which of two fexi-
ble due process tests should govern, not to resolve whether
due process ever requires a retention hearing in civil forfeit-
ure schemes. That difference is important. An appropri-
ately context-specifc due process test should not always
yield the same result when applied to different schemes. Of
Page Proof Pending Publication
the six Circuits that have applied the test from Mathews
v. Eldridge, 424 U. S. 319 (1976), to various civil forfeiture
schemes, three have held that due process requires a reten-
tion hearing, Ingram, 81 F. 4th, at 620; Smith v. Chicago, 524
F. 3d 834, 838 (CA7 2008), vacated as moot, Alvarez v. Smith,
558 U. S. 87 (2009); Krimstock v. Kelly, 306 F. 3d 40, 67–68
(CA2 2002) (Sotomayor, J.), and three have held that it does
not, Serrano v. CBP, 975 F. 3d 488, 500–502 (CA5 2020)
(per curiam); Booker v. St. Paul, 762 F. 3d 730, 736–737 (CA8
2014); United States v. One 1971 BMW, 652 F. 2d 817, 820–
821 (CA9 1981). That result is consistent with the fexible
dictates of any due process test, which should take into ac-
count all the component parts of an individual scheme.
   For instance, petitioners had the right to post a bond to
get back their vehicles, the right to move for summary judg-
ment in the forfeiture proceeding itself, and the opportunity
to seek separate relief under the Alabama Rules of Criminal
Procedure for an illegal seizure. The adequacy of those al-
414                    CULLEY v. MARSHALL

                       Sotomayor, J., dissenting

ternative procedures was never briefed below because the
only question was which test should apply. By contrast, the
New York City scheme that the Second Circuit concluded
violated due process lacked all of those procedures. See
Krimstock, 306 F. 3d, at 55, 59–60. Differences in the ade-
quacy of available procedures can and should result in differ-
ent due process outcomes.
  Instead of answering the question presented and then re-
manding to the lower court to apply the appropriate test,
the majority instead holds that due process never requires
a retention hearing. The majority acknowledges that “the
States and Congress have adopted a wide variety of ap-
proaches.” Ante, at 392. Yet it prescribes a categorical
constitutional rule for all of them. The Court today ham-
strings federal courts from conducting a context-specifc
analysis in civil forfeiture schemes that are less generous
than the one here.
                              IV
Page    Proof Pending Publication
 The majority's holding relates only to retention hearings.
It does not foreclose other potential due process challenges to
civil forfeiture proceedings. See ante, at 387, n. 3. People
who have their property seized by police remain free to chal-
lenge other abuses in the civil forfeiture system. For in-
stance, such claimants could challenge notice of a forfeiture
posted only in a newspaper, the lack of a neutral adjudicator
at an initial hearing, or the standard of proof necessary to
seize a car. Lower courts remain free to apply Mathews to
those claims. See ante, at 388. Due process also still “re-
quires a timely post-seizure forfeiture hearing,” ante, at 384,
so claimants may continue to challenge unreasonable delays.4
  4
    Courts applying the Barker factors to due process challenges of unrea-
sonable delay should not apply a narrower version of that test than the
one this Court articulated in $8,850. The $8,850 Court emphasized that
Barker is a “fexible” test, and “none of [its] factors is a necessary or
suffcient condition for fnding unreasonable delay.” United States v.
$8,850, 461 U. S. 555, 564–565 (1983); see also Barker v. Wingo, 407
                       Cite as: 601 U. S. 377 (2024)                    415

                        Sotomayor, J., dissenting

   The abuses of many civil forfeiture systems are well docu-
mented. See, e. g., supra, at 405–408. I commend States
or localities that have adopted retention hearings as a way
of guarding against those abuses. See, e. g., Brief for Legal
Aid Society as Amicus Curiae (detailing the benefts of New
York City's prompt postseizure hearings). Other States and
localities should not view today's decision as precluding them
from following suit and adopting similar measures.

                              *      *      *
   The majority today holds that due process never requires
the minimal check of a retention hearing before a police off-
cer deprives an innocent owner of her car for months or
years. Given the diverse schemes adopted by States, some
with adequate safeguards and some without, the Court
should have just answered the question presented. Instead,
it announces a universal rule for all schemes without heeding
the dictates of this Court's due process precedents that re-
Page Proof Pending Publication
quire a scheme-specifc analysis. Because I instead would
have answered the question presented and left lower courts
the fexibility to apply the appropriate test in these myriad
circumstances, I respectfully dissent.




U. S. 514, 533 (1972) (“[T]hese factors have no talismanic qualities; courts
must still engage in a diffcult and sensitive balancing process”). The fac-
tors are merely “guides in balancing the interests of the claimant and the
Government to assess whether the basic due process requirement of fair-
ness has been satisfed in a particular case.” $8,850, 461 U. S., at 565. In
the civil forfeiture context, “the balance of the interests, which depends
so heavily on the context of the particular situation, may differ from a
situation involving the right to a speedy trial.” Ibid., n. 14. Recognizing
that the Barker and Mathews balancing tests have similar aims and fac-
tors, the Government notes that the tests are not necessarily mutually
exclusive. See Brief for United States as Amicus Curiae 20–22.
                           Reporter’s Note

  The attached opinion has been revised to refect the usual publication
and citation style of the United States Reports. The revised pagination
makes available the offcial United States Reports citation in advance of
publication. The syllabus has been prepared by the Reporter of Decisions
Page Proof Pending Publication
for the convenience of the reader and constitutes no part of the opinion of
the Court. A list of counsel who argued or fled briefs in this case, and
who were members of the bar of this Court at the time this case was
argued, has been inserted following the syllabus. Other revisions may
include adjustments to formatting, captions, citation form, and any errant
punctuation. The following additional edits were made:

None

```

---

## GROUP: content/cases/Cupp v. Murphy.md  (`case`, 5 assertions)

### content_page

```
---
title: "Cupp v. Murphy"
type: case
citation: "412 U.S. 291 (1973)"
parallel_cite: "93 S. Ct. 2000; 36 L. Ed. 2d 900"
neutral_cite: 1973 U.S. LEXIS 63
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1973
date_decided: 1973-05-29
docket: 72-212
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1973-05-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Cupp v. Murphy
  varies_by_point: false
  scope_note: "Good law; a narrow holding confined to a very limited intrusion on probable cause where the evidence is readily destructible and no formal arrest was made."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108801/cupp-v-murphy/"
  cluster_id: 108801
  opinion_id: 108801
  identity_checked: true
homes:
  - page: "[[Destruction of Evidence]]"
    role: "Key — evanescent evidence"
related: ["[[Chimel v. California]]", "[[Schmerber v. California]]", "[[Davis v. Mississippi]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "exigency", "destruction-of-evidence", "probable-cause"]
holding: "Where probable cause exists and evidence is readily destructible, the very limited search needed to preserve highly evanescent evidence (fingernail scrapings) is reasonable on the Chimel rationale, even without a formal arrest — though a full Chimel search would not be."
lake:
  record_id: Cupp v. Murphy
  status: verified
  projected_at: 2026-07-09
---

# Cupp v. Murphy

*412 U.S. 291 (1973)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Murphy voluntarily came to the police station after his estranged wife was found strangled. Police, who had probable cause to believe he committed the murder, noticed a dark spot on his finger and asked to take fingernail scrapings. He refused, then put his hands behind his back, appeared to rub them together, and slipped them into his pockets (a metallic rattling was heard). Without arresting him or obtaining a warrant, officers took the scrapings, which contained the victim's skin and blood.

## Issue
Whether police with probable cause, but who have not made a formal arrest, may take a very limited, warrantless sample of readily destructible evidence (fingernail scrapings) from a suspect.

## Rule
Yes, on a narrowed *[[Chimel v. California|Chimel]]* rationale. The taking of the scrapings "went beyond mere 'physical characteristics . . . constantly exposed to the public'" and was a search subject to the Fourth Amendment, but: "The rationale of *Chimel*, in these circumstances, justified the police in subjecting him to the very limited search necessary to preserve the highly evanescent evidence they found under his fingernails." — 412 U.S. at 296. ^pin-296

The Court expressly did **not** authorize a full search: "we do not hold that a full *Chimel* search would have been justified in this case without a formal arrest and without a warrant." — *Id.* ^pin-296b

Holding: "On the facts of this case, considering the existence of probable cause, the very limited intrusion undertaken incident to the station house detention, and the ready destructibility of the evidence, we cannot say that this search violated the Fourth and Fourteenth Amendments." — [*Id.*](https://www.courtlistener.com/opinion/108801/cupp-v-murphy/#:~:text=On%20the%20facts%20of%20this) ^pin-296a

## Application
There was probable cause that Murphy committed the murder. Although there was no formal arrest, his awareness of the detectives' suspicions and his conduct in rubbing his hands and concealing them showed an attempt to destroy the readily destructible evidence under his fingernails. The intrusion was confined to that evidence — not a full search of his person — so, given probable cause and the evidence's evanescence, the limited search was reasonable.

## Conclusion
Reversed. A limited warrantless search to preserve highly destructible evidence, supported by probable cause, was reasonable even without a formal arrest; the suppression order was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Cupp* sits at the intersection of the [[Search Incident to Arrest]] rationale ([[Chimel v. California]]) and the destruction-of-evidence [[Exigent Circumstances and Hot Pursuit|exigency]], alongside [[Schmerber v. California]]; it builds on the seizure-of-the-person limits of [[Davis v. Mississippi]] (distinguished, because here probable cause existed).

## Appears on
- [[Exigent Circumstances and Hot Pursuit]] — *Related (cross-doctrine)*

## Sources
- *Cupp v. Murphy*, 412 U.S. 291 (1973) — https://www.courtlistener.com/opinion/108801/cupp-v-murphy/ — pinpoint: 296.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9724561673cadabc", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "412 U.S. 291 (1973)", "court": "U.S. Supreme Court", "neutral_cite": "1973 U.S. LEXIS 63", "official_citation_present": true, "parallel_cite": "93 S. Ct. 2000; 36 L. Ed. 2d 900", "title": "Cupp v. Murphy", "year": "1973"}}
{"assertion_id": "4d4ce0fa6c0b1d86", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Where probable cause exists and evidence is readily destructible, the very limited search needed to preserve highly evanescent evidence (fingernail scrapings) is reasonable on the Chimel rationale, even without a formal arrest — though a full Chimel search would not be.", "title": "Cupp v. Murphy"}}
{"assertion_id": "df63bb2a003eb13d", "dimension": "support", "kind": "home_role", "locator": {"home": "Destruction of Evidence"}, "payload": {"home": "Destruction of Evidence", "role": "Key — evanescent evidence", "title": "Cupp v. Murphy"}}
{"assertion_id": "2afb92c8e088d54d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1973-05-29", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Cupp v. Murphy", "field_i_validity": "good_law", "scope_note": "Good law; a narrow holding confined to a very limited intrusion on probable cause where the evidence is readily destructible and no formal arrest was made.", "title": "Cupp v. Murphy", "varies_by_point": "false"}}
{"assertion_id": "3e961ed64a4d405b", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Cupp v. Murphy"}}
```

### lake record — Cupp v. Murphy

```json
{
  "schema_version": "s2.v1",
  "record_id": "Cupp v. Murphy",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Cupp v. Murphy",
    "case_name_short": "Cupp",
    "case_name_full": "Cupp, Penitentiary Superintendent v. Murphy",
    "input_case_name": "Cupp v. Murphy",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1973-05-29",
    "year": 1973,
    "docket": "72-212",
    "cluster_id": 108801,
    "lead_opinion_id": 108801,
    "sibling_ids": [
      108801,
      9425320,
      9425321,
      9425322,
      9425323,
      9425324,
      9425325
    ],
    "absolute_url": "/opinion/108801/cupp-v-murphy/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8991915,
        "score": 20,
        "case_name": "Cupp v. Murphy"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "412 U.S. 291",
      "volume": "412",
      "reporter": "U.S.",
      "page": "291",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "93 S. Ct. 2000",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2000",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "36 L. Ed. 2d 900",
        "volume": "36",
        "reporter": "L. Ed. 2d",
        "page": "900",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1973 U.S. LEXIS 63",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "63",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "412 U.S. 291",
        "volume": "412",
        "reporter": "U.S.",
        "page": "291",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 S. Ct. 2000",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2000",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "36 L. Ed. 2d 900",
        "volume": "36",
        "reporter": "L. Ed. 2d",
        "page": "900",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. LEXIS 63",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "63",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "412 U.S. 291",
    "official_selection": {
      "court_class": "scotus",
      "selected": "412 U.S. 291",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-296",
      "page": null,
      "quote": "--- # Cupp v. Murphy *412 U.S. 291 (1973)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Murphy voluntarily came to the police station after his estranged wife was found strangled. Police, who had probable cause to believe he committed the murder, noticed a dark spot on his finger and asked to take fingernail scrapings. He refused, then put his hands behind his back, appeared to rub them together, and slipped them into his pockets (a metallic rattling was heard). Without arresting him or obtaining a warrant, officers took the scrapings, which contained the victim's skin and blood. ## Issue Whether police with probable cause, but who have not made a formal arrest, may take a very limited, warrantless sample of readily destructible evidence (fingernail scrapings) from a suspect. ## Rule Yes, on a narrowed *Chimel* rationale. The taking of the scrapings",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-296b",
      "page": null,
      "quote": "we do not hold that a full *Chimel* search would have been justified in this case without a formal arrest and without a warrant.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-296a",
      "page": null,
      "quote": "On the facts of this case, considering the existence of probable cause, the very limited intrusion undertaken incident to the station house detention, and the ready destructibility of the evidence, we cannot say that this search violated the Fourth and Fourteenth Amendments.",
      "star_marker": "296",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 14318,
      "fragment": "#:~:text=On%20the%20facts%20of%20this",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1973-05-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Cupp v. Murphy",
    "varies_by_point": false,
    "scope_note": "Good law; a narrow holding confined to a very limited intrusion on probable cause where the evidence is readily destructible and no formal arrest was made.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Cupp v. Murphy:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Friedman v. Boucher",
          "cluster_id": 3064806,
          "cite": [
            "580 F.3d 847",
            "2009 WL 2857199"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kareem Jamal Currence",
          "cluster_id": 794165,
          "cite": [
            "446 F.3d 554",
            "2006 U.S. App. LEXIS 11090",
            "2006 WL 1172337"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Blais",
          "cluster_id": 6577730,
          "cite": [
            "428 Mass. 294",
            "701 N.E.2d 314",
            "1998 Mass. LEXIS 547"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vester v. State",
          "cluster_id": 2449964,
          "cite": [
            "916 S.W.2d 708",
            "1996 WL 70218"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Joyce",
          "cluster_id": 7906322,
          "cite": [
            "30 Conn. App. 164",
            "619 A.2d 872",
            "1993 Conn. App. LEXIS 43"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane1_negative"
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
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
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
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Hodari D.",
          "cluster_id": 112579,
          "cite": [
            "113 L. Ed. 2d 690",
            "111 S. Ct. 1547",
            "499 U.S. 621",
            "1991 U.S. LEXIS 2397",
            "91 Cal. Daily Op. Serv. 2893",
            "59 U.S.L.W. 4335",
            "91 Daily Journal DAR 4665"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
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
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
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
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
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
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
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
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
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
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rawlings v. Kentucky",
          "cluster_id": 110326,
          "cite": [
            "65 L. Ed. 2d 633",
            "100 S. Ct. 2556",
            "448 U.S. 98",
            "1980 U.S. LEXIS 142"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
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
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vernonia School District 47J v. Acton",
          "cluster_id": 117964,
          "cite": [
            "132 L. Ed. 2d 564",
            "115 S. Ct. 2386",
            "515 U.S. 646",
            "1995 U.S. LEXIS 4275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
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
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cantor",
          "cluster_id": 5681132,
          "cite": [
            "36 N.Y.2d 106",
            "324 N.E.2d 872",
            "365 N.Y.S.2d 509",
            "1975 N.Y. LEXIS 3100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Knowles v. Iowa",
          "cluster_id": 118250,
          "cite": [
            "142 L. Ed. 2d 492",
            "119 S. Ct. 484",
            "525 U.S. 113",
            "1998 U.S. LEXIS 8068"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe v. Poritz",
          "cluster_id": 1473573,
          "cite": [
            "662 A.2d 367",
            "142 N.J. 1",
            "36 A.L.R. 5th 711",
            "1995 N.J. LEXIS 519"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
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
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Crutcher",
          "cluster_id": 2454155,
          "cite": [
            "989 S.W.2d 295",
            "1999 Tenn. LEXIS 228"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
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
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aliff v. State",
          "cluster_id": 1669433,
          "cite": [
            "627 S.W.2d 166",
            "1982 Tex. Crim. App. LEXIS 824"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Amaya-Ruiz",
          "cluster_id": 2612518,
          "cite": [
            "800 P.2d 1260",
            "166 Ariz. 152"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. State",
          "cluster_id": 1136943,
          "cite": [
            "690 So. 2d 276",
            "1996 WL 711294"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Asherman",
          "cluster_id": 7891879,
          "cite": [
            "193 Conn. 695",
            "478 A.2d 227",
            "1984 Conn. LEXIS 629"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
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
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In re of an Investigation into the Death of Jon L.",
          "cluster_id": 5685680,
          "cite": [
            "56 N.Y.2d 288",
            "437 N.E.2d 265",
            "452 N.Y.S.2d 6",
            "1982 N.Y. LEXIS 3395"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 2369299,
          "cite": [
            "795 S.W.2d 171",
            "1990 Tex. Crim. App. LEXIS 67",
            "1990 WL 55049"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cupp v. Murphy:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108801 OR 9425320 OR 9425321 OR 9425322 OR 9425323 OR 9425324 OR 9425325) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02MzAxMTUyMDAwMDAmcz01MzQ1NTEmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108801+OR+9425320+OR+9425321+OR+9425322+OR+9425323+OR+9425324+OR+9425325%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 6,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 6,
        "triage_snippet_classified": 194
      },
      "lane2_top_cited": {
        "query": "cites:(108801 OR 9425320 OR 9425321 OR 9425322 OR 9425323 OR 9425324 OR 9425325)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTMmcz01Njg0MDMxJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108801+OR+9425320+OR+9425321+OR+9425322+OR+9425323+OR+9425324+OR+9425325%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108801 OR 9425320 OR 9425321 OR 9425322 OR 9425323 OR 9425324 OR 9425325)",
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
    "complete_query": "cites:(108801 OR 9425320 OR 9425321 OR 9425322 OR 9425323 OR 9425324 OR 9425325)",
    "indexed_citing_opinions": 484,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108801,
        "count": 440,
        "count_source": "search"
      },
      {
        "opinion_id": 9425320,
        "count": 57,
        "count_source": "search"
      },
      {
        "opinion_id": 9425321,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425322,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425323,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425324,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425325,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 739,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/cupp-v-murphy.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjYzOTM2NyZzPTEwNjEwMTE3JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108801+OR+9425320+OR+9425321+OR+9425322+OR+9425323+OR+9425324+OR+9425325%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108801,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108801,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108801,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108801,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108801,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108801,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108801,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108801,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108801,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108801,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108801,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108801,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108801,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108801,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108801,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108801,
        "cited_id": 108710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108801,
        "cited_id": 303975,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108801,
        "cited_id": 1176185,
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
    "date_created": "2026-07-05T01:51:50Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T01:52:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T01:52:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T01:55:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T01:52:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Cupp v. Murphy

```
<div>
<center><b><span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/" aria-description="Citation for case: Cupp v. Murphy">412 U.S. 291</a></span> (1973)</b></center>
<center><h1>CUPP, PENITENTIARY SUPERINTENDENT<br>
v.<br>
MURPHY.</h1></center>
<center>No. 72-212.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 20, 1973.</center>
<center>Decided May 29, 1973.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><i>Thomas H. Denney,</i> Assistant Attorney General of Oregon, argued the cause for petitioner. With him on the brief were <i>Lee Johnson,</i> Attorney General, and <i>John W. Osborn,</i> Solicitor General.</p>
<p><i>Howard R. Lonergan</i> argued the cause and filed a brief for respondent.<sup>[*]</sup></p>
<p><i>Melvin L. Wulf, Burt Neuborne,</i> and <i>Joel M. Gora</i> filed a brief for the American Civil Liberties Union as <i>amicus curiae</i> urging affirmance.</p>
<p><span class="star-pagination">*292</span> MR. JUSTICE STEWART delivered the opinion of the Court.</p>
<p>The respondent, Daniel Murphy, was convicted by a jury in an Oregon court of the second-degree murder of his wife. The victim died by strangulation in her home in the city of Portland, and abrasions and lacerations were found on her throat. There was no sign of a break-in or robbery. Word of the murder was sent to the respondent, who was not then living with his wife. Upon receiving the message, Murphy promptly telephoned the Portland police and voluntarily came into Portland for questioning. Shortly after the respondent's arrival at the station house, where he was met by retained counsel, the police noticed a dark spot on the respondent's finger. Suspecting that the spot might be dried blood and knowing that evidence of strangulation is often found under the assailant's fingernails, the police asked Murphy if they could take a sample of scrapings from his fingernails. He refused. Under protest and without a warrant, the police proceeded to take the samples, which turned out to contain traces of skin and blood cells, and fabric from the victim's nightgown. This incriminating evidence was admitted at the trial.</p>
<p>The respondent appealed his conviction, claiming that the fingernail scrapings were the product of an unconstitutional search under the Fourth and Fourteenth Amendments. The Oregon Court of Appeals affirmed the conviction, <span class="citation" data-id="1176185"><a href="/opinion/1176185/state-v-murphy/" aria-description="Citation for case: State v. Murphy">2 Ore. App. 251</a></span>, <span class="citation" data-id="1176185"><a href="/opinion/1176185/state-v-murphy/" aria-description="Citation for case: State v. Murphy">465 P. 2d 900</a></span>, and we denied certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./400/944/">400 U. S. 944</a></span>. Murphy then commenced the present action for federal habeas corpus relief. <span class="star-pagination">*293</span> The District Court, in an unreported decision, denied the habeas petition, and the Court of Appeals for the Ninth Circuit reversed, <span class="citation" data-id="303975"><a href="/opinion/303975/daniel-p-murphy-v-hoyt-c-cupp/" aria-description="Citation for case: Daniel P. Murphy v. Hoyt C. Cupp">461 F. 2d 1006</a></span>. The Court of Appeals assumed the presence of probable cause to search or arrest, but held that in the absence of an arrest or other exigent circumstances, the search was unconstitutional. <span class="citation" data-id="303975"><a href="/opinion/303975/daniel-p-murphy-v-hoyt-c-cupp/#1007" aria-description="Citation for case: Daniel P. Murphy v. Hoyt C. Cupp"><i>Id.,</i> at 1007</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./409/1036/">409 U. S. 1036</a></span>, to consider the constitutional question presented.</p>
<p>The trial court, the Oregon Court of Appeals, and the Federal District Court all agreed that the police had probable cause to arrest the respondent at the time they detained him and scraped his fingernails. As the Oregon Court of Appeals said,</p>
<blockquote>"At the time the detectives took these scrapings they knew:</blockquote>
<blockquote>"The bedroom in which the wife was found dead showed no signs of disturbance, which fact tended to indicate a killer known to the victim rather than to a burglar or other stranger.</blockquote>
<blockquote>"The decedent's son, the only other person in the house that night, did not have fingernails which could have made the lacerations observed on the victim's throat.</blockquote>
<blockquote>"The defendant and his deceased wife had had a stormy marriage and did not get along well.</blockquote>
<blockquote>"The defendant had, in fact, been at his home on the night of the murder. He left and drove back to central Oregon claiming that he did not enter the house or see his wife. He volunteered a great deal of information without being asked, yet expressed no concern or curiosity about his wife's fate." <span class="citation" data-id="1176185"><a href="/opinion/1176185/state-v-murphy/#259" aria-description="Citation for case: State v. Murphy">2 Ore. App., at 259-260</a></span>, 465 P. 2d. at 904.</blockquote>
<p>The Court of Appeals for the Ninth Circuit did not disagree with the conclusion that the police had probable cause to make an arrest, 461 F. 2d. at 1007, nor do we.</p>
<p><span class="star-pagination">*294</span> It is also undisputed that the police did not obtain an arrest warrant or formally "arrest" the respondent, as that term is understood under Oregon law.<sup>[1]</sup> The respondent was detained only long enough to take the fingernail scrapings, and was not formally "arrested" until approximately one month later. Nevertheless, the detention of the respondent against his will constituted a seizure of his person, and the Fourth Amendment guarantee of freedom from "unreasonable searches and seizures" is clearly implicated, cf. <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1</a></span>, <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19</a></span>. As the Court said in <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#726" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 726-727</a></span>, "Nothing is more clear than that the Fourth Amendment was meant to prevent wholesale intrusions upon the personal security of our citizenry, whether these intrusions be termed `arrests' or `investigatory detentions.' "</p>
<p>In <i><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span>,</i> the Court held that fingerprints obtained during the brief detention of persons seized in a police dragnet procedure, without probable cause, were inadmissible in evidence. Though the Court recognized that fingerprinting "involves none of the probing into an individual's private life and thoughts that marks an interrogation or search," <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#727" aria-description="Citation for case: Davis v. Mississippi"><i>id.,</i> at 727</a></span>, the Court held the station-house detention in that case to be violative of the Fourth and Fourteenth Amendments. "Investigatory seizures would subject unlimited numbers of innocent persons to the harassment and ignominy incident to involuntary detention," <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#726" aria-description="Citation for case: Davis v. Mississippi"><i>id.,</i> at 726</a></span>.</p>
<p>The respondent in this case, like Davis, was briefly detained at the station house. Yet here, there was, as three courts have found, probable cause to believe that <span class="star-pagination">*295</span> the respondent had committed the murder. The vice of the detention in <i><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span></i> is therefore absent in the case before us. Cf. <i>United States</i> v. <i><span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/" aria-description="Citation for case: United States v. Dionisio">Dionisio, supra</a></span></i><i>.</i></p>
<p>The inquiry does not end here, however, because Murphy was subjected to a search as well as a seizure of his person. Unlike the fingerprinting in <i><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span>,</i> the voice exemplar obtained in <i>United States</i> v. <i><span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/" aria-description="Citation for case: United States v. Dionisio">Dionisio, supra</a></span></i><i>,</i> or the handwriting exemplar obtained in <i>United States</i> v. <i>Mara,</i> <span class="citation" data-id="9425147"><a href="/opinion/108710/united-states-v-mara/" aria-description="Citation for case: United States v. Mara">410 U. S. 19</a></span>, the search of the respondent's fingernails went beyond mere "physical characteristics. . . constantly exposed to the public," <i>United States</i> v. <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#14" aria-description="Citation for case: United States v. Dionisio"><i>Dionisio, supra,</i> at 14</a></span>, and constituted the type of "severe, though brief, intrusion upon cherished personal security" that is subject to constitutional scrutiny. <i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i> at 24-25</a></span>.</p>
<p>We believe this search was constitutionally permissible under the principles of <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>. <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> stands in a long line of cases recognizing an exception to the warrant requirement when a search is incident to a valid arrest. <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#755" aria-description="Citation for case: Chimel v. California"><i>Id.,</i> at 755-762</a></span>. The basis for this exception is that when an arrest is made, it is reasonable for a police officer to expect the arrestee to use any weapons he may have and to attempt to destroy any incriminating evidence then in his possession. <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California"><i>Id.,</i> at 762-763</a></span>. The Court recognized in <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> that the scope of a warrantless search must be commensurate with the rationale that excepts the search from the warrant requirement.<sup>[2]</sup> Thus, a warrantless search incident to arrest, the Court held in <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>,</i> must be limited to the area "into which an arrestee might reach." <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California"><i>Id.,</i> at 763</a></span>.</p>
<p><span class="star-pagination">*296</span> Where there is no formal arrest, as in the case before us, a person might well be less hostile to the police and less likely to take conspicuous, immediate steps to destroy incriminating evidence on his person. Since he knows he is going to be released, he might be likely instead to be concerned with diverting attention away from himself. Accordingly, we do not hold that a full <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> search would have been justified in this case without a formal arrest and without a warrant. But the respondent was not subjected to such a search.</p>
<p>At the time Murphy was being detained at the station house, he was obviously aware of the detectives' suspicions. Though he did not have the full warning of official suspicion that a formal arrest provides, Murphy was sufficiently apprised of his suspected role in the crime to motivate him to attempt to destroy what evidence he could without attracting further attention. Testimony at trial indicated that after he refused to consent to the taking of fingernail samples, he put his hands behind his back and appeared to rub them together. He then put his hands in his pockets, and a "metallic sound, such as keys or change rattling" was heard. The rationale of <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>,</i> in these circumstances, justified the police in subjecting him to the very limited search necessary to preserve the highly evanescent evidence they found under his fingernails, cf. <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span>.</p>
<p>On the facts of this case, considering the existence of probable cause, the very limited intrusion undertaken incident to the station house detention, and the ready destructibility of the evidence, we cannot say that this search violated the Fourth and Fourteenth Amendments. Accordingly, the judgment of the Court of Appeals is</p>
<p><i>Reversed.</i></p>
<p><span class="star-pagination">*297</span> MR. JUSTICE WHITE joins the opinion of the Court but does not consider the issue of probable cause to have been decided here or to be foreclosed on remand to the Court of Appeals where it has never been considered.</p>
<p>MR. JUSTICE MARSHALL, concurring.</p>
<p>I join the opinion of my BROTHER STEWART.</p>
<p>Murphy's freedom of movement was unquestionably limited when the police did not acquiesce in his refusal to permit them to take scrapings from his fingernails. But that detention, although a seizure of the person protected by the Fourth Amendment, did not amount to an arrest under Oregon law. See Ore. Rev. Stat. § 133.210. The police, understanding this, did not, for example, take Murphy promptly before a magistrate after this detention, as state law requires after an arrest. <i>Id.,</i> § 133.550.<sup>[1]</sup> As we have said before, however, "It is quite plain that the Fourth Amendment governs `seizures' of the person which do not eventuate in a trip to the station house and prosecution for crime `arrests' in traditional terminology. It must be recognized that whenever a police officer accosts an individual and restrains his freedom to walk away, he has `seized' that person." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 16</a></span> (1968). See also <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">id.,</a></span></i> at 19 n. 16, 26; <i>Sibron</i> v. <i>New York,</i> <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#67" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 67</a></span> (1968).</p>
<p>Murphy argues, however, that the detention was unlawful because the police did not satisfy "the general requirement that the authorization of a judicial officer be obtained in advance of detention," <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#728" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 728</a></span> (1969). See also <i>Terry</i> v. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio</a></span>,</i> <span class="star-pagination">*298</span> <i>supra,</i> at 20. But until the officer saw a dark spot under Murphy's thumbnail, and remembered that he had seen lacerations on the throat of the deceased, he had no reason to detain Murphy for the limited purpose of taking fingernail scrapings. Then, when he brought to Murphy's attention his interest in taking such scrapings, he was dealing with a suspect alerted to the desire of the police to inspect his fingernails. At that point, there was no way to preserve the status quo while a warrant was sought, and there was good reason to believe that Murphy might attempt to alter the status quo unless he were prevented from doing so. The police could not assure the preservation of the evidence simply by placing Murphy under close surveillance, because of the nature of the evidence. And, for purposes of Fourth Amendment analysis, detaining him while a warrant was sought would have been as much a seizure as detaining him while his fingernails were scraped. If the Fourth Amendment permits a stop-and-frisk when the police have specific articulable facts from which they may infer that a person, who they suspect is about to commit a crime, is armed and dangerous, <i>Terry</i> v. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra</a></span></i><i>,</i> it also permits detention, where the police have probable cause to arrest,<sup>[2]</sup> to take fingernail scrapings in the circumstances of this case.<sup>[3]</sup></p>
<p>Murphy's argument is, of course, a troublesome one, and, if the police had done more than take fingernail <span class="star-pagination">*299</span> scrapings, I would be inclined to hold the search illegal. For, as a general principle of the law of the Fourth Amendment, the scope of a search must be strictly limited in terms of the circumstances that justify the search. See, <i>e. g., </i><i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i> at 19-20</a></span>; <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969). When a person is detained, but not arrested, the detention must be justified by particularized police interests other than a desire to initiate a criminal proceeding against the person they detain. The police therefore cannot do more than investigate the circumstances that occasion the detention. In this case, the police limited their intrusion to precisely the area that led them to restrict Murphy's freedom; he was not searched as extensively as he might have been had an arrest occurred. Indeed, in my view, the Fourth Amendment would have barred a more extensive search, for the police had no reason at all to believe that Murphy had on his person more evidence relating to the crime, or, in light of the fact that this case involved a strangulation, a weapon that he might use at the station house.</p>
<p>I realize that exceptions to the warrant requirement may be established because of "powerful hydraulic pressures. . . that bear heavily on the Court to water down constitutional guarantees," <i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#39" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i> at 39</a></span> (DOUGLAS, J., dissenting), and that those same pressures may lead to later expansion of the exceptions beyond the narrow confines of the cases in which they are established, <i>Adams</i> v. <i>Williams,</i> <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#161" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 161-162</a></span> (1972) (MARSHALL, J., dissenting). But I cannot say that, in the precise circumstances of this case, the police violated the Fourth Amendment in detaining Murphy for the limited purpose of scraping his fingernails. I emphasize, as does the opinion of the Court, that the search conducted incident to this detention was extremely narrow in scope, and that its scope was tied closely to the reasons justifying <span class="star-pagination">*300</span> the detention. On this understanding, I join the opinion of the Court.</p>
<p>MR. JUSTICE BLACKMUN, with whom THE CHIEF JUSTICE joins, concurring.</p>
<p>The Court today permits a search for evidence without an arrest but under circumstances where probable cause for an arrest existed, where the officers had reasonable cause to believe that the evidence was on respondent's person, and where that evidence was highly destructible. The Court, however, restricts the permissible quest to "the very limited search necessary to preserve the highly evanescent evidence they found under [respondent's] fingernails."</p>
<p>While I join the Court's opinion, I do so with the understanding that what the Court says here applies only where no arrest has been made. Far different factors, in my view, govern the permissible scope of a search incident to a lawful arrest.</p>
<p>MR. JUSTICE POWELL, with whom THE CHIEF JUSTICE and MR. JUSTICE REHNQUIST join, concurring.</p>
<p>In this case the District Court and the Court of Appeals entertained a habeas corpus attack upon a state court conviction on the ground that the evidence seized in violation of the Fourth Amendment had been wrongly admitted at the state trial. For the reasons set forth in my concurring opinion in <i>Schneckloth</i> v. <i>Bustamonte, ante,</i> p. 250, I think a claim such as this is properly available in federal habeas corpus only to the extent of ascertaining whether the prisoner was afforded a fair opportunity to raise and have adjudicated the question in state courts. The Court today, however, reaches the merits of the respondent's Fourth Amendment claim, and on the merits I join the Court's opinion.</p>
<p><span class="star-pagination">*301</span> MR. JUSTICE DOUGLAS, dissenting in part.</p>
<p>I agree with the Court that exigent circumstances existed making it likely that the fingernail scrapings of suspect Murphy might vanish if he were free to move about. The police would therefore have been justified in detaining him while a search warrant was sought from a magistrate. None was sought and the Court now holds there was probable cause to search or arrest, making a warrant unnecessary.</p>
<p>Whether there was or was not probable cause is difficult to determine on this record. It is a question that the Court of Appeals never reached. We should therefore remand to it for a determination of that question.</p>
<p>The question is clouded in my mind because the police did not arrest Murphy until a month later. It is a case not covered by <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>, on which the Court relies, for in <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> an arrest had been made.</p>
<p>As the Court states, Oregon defines arrest as "the taking of a person into custody so that he may be held to answer for a crime." Ore. Rev. Stat. § 133.210. No such arrest was made until a month after Murphy's fingernails were scraped. As we stated in <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, 15 n. 5, "State law determines the validity of arrests without warrant." The case is therefore on all fours with <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span>, where a suspect was detained for the sole purpose of obtaining fingerprints but at the time the police were not detaining him to charge him with the crime. Like the seizure in this case, <i><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span></i> involved an investigative seizure. In <i><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span>,</i> at 727, as in <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19</a></span>, the Court rejected the view that the Fourth Amendment does not limit police conduct "if the officers stop short of something called a `technical arrest' or a `full-blown search.' "</p>
<p><span class="star-pagination">*302</span> The reason why no arrest of Murphy was made on the day his fingernails were scraped creates a nagging doubt that they did not then have probable cause to make an arrest and did not reach that conclusion until a month later. Why was Murphy allowed to roam at will, a free man, for the next month? The evolving pattern of a conspiracy offense might induce the police to turn a suspect loose in order to tail him and see what other suspects could be brought into their net. But no such circumstances were present here.</p>
<p>What the decision made today comes down to, I fear, is that "suspicion" is the basis for a search of the person without a warrant. Yet "probable cause" is the requirement of the Fourth Amendment which is applicable to the States by reason of the Fourteenth Amendment. <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>. Suspicion has never been sufficient for a warrantless search, save for the narrow situation of searches incident to an arrest as was involved in <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>.</i> That exception is designed (see <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#769" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 769-770</a></span>) to protect the officer against assaults through weapons within easy reach of the accused or to save evidence within that narrow zone from destruction. However, this is a case where a warrant might have been sought but was not. It is therefore governed by the rule that the rights of a person "against unlawful search and seizure are to be protected even if the same result might have been achieved in a lawful way." <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span>. No warrant could have been issued by the police, for as we held in <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#453" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 453</a></span>, a warrant must be issued by "the neutral and detached magistrate required by the Constitution." And see <i>Mancusi</i> v. <i>DeForte,</i> <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#371" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364, 371</a></span>. As stated in <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S., at 14</a></span>, "When the right of privacy must reasonably yield to the right of search is, <span class="star-pagination">*303</span> as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent." In that case the officers, smelling opium, asked for entrance, which was given. On entry, discovering that the accused was the sole occupant, the police arrested her. "Thus the Government is obliged to justify the arrest by the search and at the same time to justify the search by the arrest. This will not do." <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#16" aria-description="Citation for case: Johnson v. United States"><i>Id.,</i> at 16-17</a></span>.</p>
<p>It will not do here either. As <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, stated, the Fourth Amendment is closely related to the Self-Incrimination Clause of the Fifth.<sup>[*]</sup> A warrantless search on suspicion, today sustained, gives the police evidence otherwise protected by the Self-Incrimination Clause of the Fifth Amendment. It was in that regard that the Court in <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> said: "[T]he Fourth and Fifth Amendments run almost into each other." <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States"><i>Id.,</i> at 630</a></span>. And that Court went on to say: "For the `unreasonable searches and seizures' condemned in the Fourth Amendment are almost always made for the purpose of compelling a man to give evidence against himself, which in criminal cases is condemned in the Fifth Amendment; and compelling a man `in a criminal case to be a witness against himself,' which is condemned in the Fifth Amendment, throws light on the question as to what is an `unreasonable search and seizure' within the meaning of the Fourth Amendment. And we have been unable to perceive that the seizure of a man's private books and papers to be used in evidence against him is substantially different from compelling him to be a <span class="star-pagination">*304</span> witness against himself. We think it is within the clear intent and meaning of those terms." <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#633" aria-description="Citation for case: Boyd v. United States"><i>Id.,</i> at 633</a></span>.</p>
<p>The same can be said of incriminating evidence found under a suspect's fingernails. See <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span>. Moreover, the Fourth Amendment guarantees the right of the people to be secure "in their persons." Scraping a man's fingernails is an invasion of that privacy and it is tolerable, constitutionally speaking, only if there is a warrant for a search or seizure issued by a magistrate on a showing of "probable cause" that the suspect had committed the crime. There was time to get a warrant; Murphy could have been detained while one was sought; and that detention would have preserved the perishable evidence the police sought. A suspect on the loose could get rid of it; but a suspect closely detained until a warrant is obtained plainly could not.</p>
<p>Our approval of the shortcut taken to avoid the Fourth and Fifth Amendments may be typical of this age. Erosions of constitutional guarantees usually start slowly, not in dramatic onsets. As stated in <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> "illegitimate and unconstitutional practices get their first footing . . . by silent approaches and slight deviations from legal modes of procedure." <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U. S., at 635</a></span>.</p>
<p>The issue of probable cause should be considered by the Court of Appeals. On the record before us and the arguments based on it I cannot say there was "probable cause" for an arrest and for a search, since the arrest came after a month's delay. The only weight we can put in the scales to turn suspicion into probable cause is Murphy's conviction by a jury based on the illegally obtained evidence. That is but a simple way of making the end justify the meansa principle wholly at war with our constitutionally enshrined adversary system.</p>
<p><span class="star-pagination">*305</span> MR. JUSTICE BRENNAN, dissenting in part.</p>
<p>Without effecting an arrest, and without first seeking to obtain a search warrant from a magistrate, the police decided to scrape respondent's fingernails for destructible evidence. In upholding this search, the Court engrafts another, albeit limited, exception on the warrant requirement. Before we take the serious step of legitimating even limited searches merely upon probable causewithout a warrant or as incident to an arrestwe ought first be certain that such probable cause in fact existed. Here, as my Brother DOUGLAS convincingly demonstrates "[w]hether there was or was not probable cause is difficult to determine on this record." <i>Ante,</i> at 301. And, since the Court of Appeals did not consider that question, the proper course would be to remand to that court so that it might decide in the first instance whether there was probable cause to arrest or search. There is simply no need for this Court to decide, upon a disputed record and at this stage of the litigation, whether the instant search would be permissible if probable cause existed.</p>
<h2>NOTES</h2>
<p>[*]  <i>Alan S. Ganz, Frank Carrington, Ronald E. Sherk,</i> and <i>Fred E. Inbau</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging reversal.</p>
<p>[1]  Oregon defines arrest as "the taking of a person into custody so that he may be held to answer for a crime." Ore. Rev. Stat. § 133.210.</p>
<p>[2]  As the Court stated in <i>Terry</i> v. <i>Ohio</i><i>,</i> "our inquiry is a dual one whether the officer's action was justified at its inception, and whether it was reasonably related in scope to the circumstances which justified the interference in the first place." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19-20</a></span>.</p>
<p>[1]  Thus this case does not require us to determine whether the police were required to obtain a warrant for Murphy's arrest at the relevant time. Cf. <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499-500</a></span> (1958); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#477" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 477-481</a></span> (1971).</p>
<p>[2]  The Court of Appeals assumed that there was probable cause to arrest, and I proceed on that assumption. I agree with MR. JUSTICE WHITE that the question of probable cause to arrest is open on remand.</p>
<p>[3]  MR. JUSTICE DOUGLAS suggests that the taking of fingernail scrapings might violate the Fifth Amendment privilege against self-incrimination. In my view, however, that privilege is confined to situations in which the evidence could be secured by the State only with the defendant's "affirmative cooperation," <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#31" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1, 31</a></span> (1973) (MARSHALL, J., dissenting).</p>
<p>[*]  My Brother MARSHALL says that this privilege is confined to cases where the evidence can be obtained only with the defendant's cooperation. But that extends even the boundaries set by <i>Schmerber</i> v. <i>California</i><i>,</i> involving forced giving of blood, <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#761" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 761</a></span>, with which my Brother MARSHALL disagrees. <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1</a></span>.</p>

</div>
```

---

## GROUP: content/cases/Dalia v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Dalia v. United States"
type: case
citation: "441 U.S. 238 (1979)"
parallel_cite: "99 S. Ct. 1682; 60 L. Ed. 2d 177"
neutral_cite: 1979 U.S. LEXIS 89
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-04-18
docket: 77-1722
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1979-04-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Dalia v. United States
  varies_by_point: false
  scope_note: Constitutional holdings on covert entry and manner-of-execution remain good law and are regularly applied to surveillance-installation warrants.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110061/dalia-v-united-states/"
  cluster_id: 110061
  opinion_id: 110061
  identity_checked: true
homes:
  - page: "[[Scope Manner and Related Issues]]"
    role: "Progeny (manner of execution / covert entry)"
related: ["[[Berger v. New York]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant", "search-warrant", "electronic-surveillance", "covert-entry", "warrant-execution", "title-iii"]
holding: "A court order authorizing Title III electronic surveillance implicitly authorizes the covert entry needed to install the device; the Fourth Amendment does not require a warrant to specify the manner of its execution, including covert entry."
lake:
  record_id: Dalia v. United States
  status: verified
  projected_at: 2026-07-09
---

# Dalia v. United States

*441 U.S. 238 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Acting under a Title III order (18 U.S.C. § 2518) authorizing interception of oral communications in Dalia's business office, FBI agents covertly entered the office at night, installed a bug in the ceiling, and later re-entered to remove it. The authorizing order did not expressly state that the surveillance would be carried out by a covert entry. Dalia moved to suppress the resulting evidence, arguing the unannounced break-in to install the device was unconstitutional and unauthorized.

## Issue
(1) Whether the Fourth Amendment categorically forbids covert entry of private premises to install electronic surveillance equipment; and (2) whether a Title III surveillance order must include an explicit, advance statement authorizing such a covert entry.

## Rule
Covert entry to install lawful bugging equipment is not [[Common Legal Terms#per-se|per se]] unconstitutional. "We make explicit, therefore, what has long been implicit in our decisions dealing with this subject: The Fourth Amendment does not prohibit *per se* a covert entry performed for the purpose of installing otherwise legal electronic bugging equipment." — 441 U.S. at 248. ^pin-248

A warrant authorizing surveillance need not separately spell out that it will be executed by covert entry. "Nothing in the language of the Constitution or in this Court's decisions interpreting that language suggests that, in addition to the three requirements discussed above, search warrants also must include a specification of the precise manner in which they are to be executed. On the contrary, it is generally left to the discretion of the executing officers to determine the details of how best to proceed with the performance of a search authorized by warrant" — subject to the general protection "against unreasonable searches and seizures." — [*Id.* at 257](https://www.courtlistener.com/opinion/110061/dalia-v-united-states/#:~:text=Nothing%20in%20the%20language%20of). ^pin-257

## Application
Title III's language, structure, and history showed Congress meant to authorize courts to approve electronic surveillance "without limitation on the means necessary to its accomplishment, so long as they are reasonable," and Congress understood that "[a]bsent covert entry … almost all electronic bugging would be impossible." The April 5 order therefore implicitly authorized the covert entry needed to install the device; and because the Fourth Amendment does not require a warrant to specify its manner of execution, the order's silence about the break-in did not invalidate the surveillance. The covert entry was a reasonable means of executing a valid order.

## Conclusion
The covert entry to install the bug was constitutional and authorized by the Title III order; Dalia's conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Dalia*'s constitutional holdings — that covert entry to install lawful surveillance equipment is not [[Common Legal Terms#per-se|per se]] unreasonable, and that a warrant need not specify the manner of its execution — remain good law and govern surveillance-installation and analogous warrant-execution questions.

## Appears on
- [[Scope Manner and Related Issues]] — *Progeny (manner of execution / covert entry)*

## Sources
- *Dalia v. United States*, 441 U.S. 238 (1979) — https://www.courtlistener.com/opinion/110061/dalia-v-united-states/ — pinpoints: 248, 257.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f658ba71939f78cf", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "441 U.S. 238 (1979)", "court": "U.S. Supreme Court", "neutral_cite": "1979 U.S. LEXIS 89", "official_citation_present": true, "parallel_cite": "99 S. Ct. 1682; 60 L. Ed. 2d 177", "title": "Dalia v. United States", "year": "1979"}}
{"assertion_id": "a0c0fcb3d0eed016", "dimension": "support", "kind": "home_role", "locator": {"home": "Scope Manner and Related Issues"}, "payload": {"home": "Scope Manner and Related Issues", "role": "Progeny (manner of execution / covert entry)", "title": "Dalia v. United States"}}
{"assertion_id": "eeffb5b846cb6155", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A court order authorizing Title III electronic surveillance implicitly authorizes the covert entry needed to install the device; the Fourth Amendment does not require a warrant to specify the manner of its execution, including covert entry.", "title": "Dalia v. United States"}}
{"assertion_id": "4340f9006bd6809c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Dalia v. United States"}}
{"assertion_id": "9e28646ad18b2318", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1979-04-18", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Dalia v. United States", "field_i_validity": "good_law", "scope_note": "Constitutional holdings on covert entry and manner-of-execution remain good law and are regularly applied to surveillance-installation warrants.", "title": "Dalia v. United States", "varies_by_point": "false"}}
```

### lake record — Dalia v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Dalia v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Dalia v. United States",
    "case_name_short": "Dalia",
    "case_name_full": "Dalia v. United States",
    "input_case_name": "Dalia v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-04-18",
    "year": 1979,
    "docket": "77-1722",
    "cluster_id": 110061,
    "lead_opinion_id": 110061,
    "sibling_ids": [
      110061,
      9427537,
      9427538,
      9427539
    ],
    "absolute_url": "/opinion/110061/dalia-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "441 U.S. 238",
      "volume": "441",
      "reporter": "U.S.",
      "page": "238",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 1682",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1682",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 L. Ed. 2d 177",
        "volume": "60",
        "reporter": "L. Ed. 2d",
        "page": "177",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 89",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "89",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "441 U.S. 238",
        "volume": "441",
        "reporter": "U.S.",
        "page": "238",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 1682",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1682",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 L. Ed. 2d 177",
        "volume": "60",
        "reporter": "L. Ed. 2d",
        "page": "177",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 89",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "89",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "441 U.S. 238",
    "official_selection": {
      "court_class": "scotus",
      "selected": "441 U.S. 238",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-248",
      "page": null,
      "quote": "--- # Dalia v. United States *441 U.S. 238 (1979)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting under a Title III order (18 U.S.C. \u00a7 2518) authorizing interception of oral communications in Dalia's business office, FBI agents covertly entered the office at night, installed a bug in the ceiling, and later re-entered to remove it. The authorizing order did not expressly state that the surveillance would be carried out by a covert entry. Dalia moved to suppress the resulting evidence, arguing the unannounced break-in to install the device was unconstitutional and unauthorized. ## Issue (1) Whether the Fourth Amendment categorically forbids covert entry of private premises to install electronic surveillance equipment; and (2) whether a Title III surveillance order must include an explicit, advance statement authorizing such a covert entry. ## Rule Covert entry to install lawful bugging equipment is not per se unconstitutional.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-257",
      "page": null,
      "quote": "Nothing in the language of the Constitution or in this Court's decisions interpreting that language suggests that, in addition to the three requirements discussed above, search warrants also must include a specification of the precise manner in which they are to be executed. On the contrary, it is generally left to the discretion of the executing officers to determine the details of how best to proceed with the performance of a search authorized by warrant",
      "star_marker": "257",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 30611,
      "fragment": "#:~:text=Nothing%20in%20the%20language%20of",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1979-04-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Dalia v. United States",
    "varies_by_point": false,
    "scope_note": "Constitutional holdings on covert entry and manner-of-execution remain good law and are regularly applied to surveillance-installation warrants.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Lonnell Glover",
          "cluster_id": 2641656,
          "cite": [
            "407 U.S. App. D.C. 189",
            "736 F.3d 509",
            "2013 WL 5951521",
            "2013 U.S. App. LEXIS 22667"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane1_negative"
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
        "journal_ref": "Dalia v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Christi Lynn Johnston",
          "cluster_id": 2855234,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cunningham",
          "cluster_id": 197364,
          "cite": [
            "113 F.3d 289",
            "1997 U.S. App. LEXIS 11632",
            "1997 WL 251388"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Garner",
          "cluster_id": 6577195,
          "cite": [
            "423 Mass. 735",
            "672 N.E.2d 510",
            "1996 Mass. LEXIS 305"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Joan Cody v. Keith Mello and Thomas Murray",
          "cluster_id": 698733,
          "cite": [
            "59 F.3d 13",
            "32 Fed. R. Serv. 3d 1002",
            "1995 U.S. App. LEXIS 15863",
            "1995 WL 377409"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chen",
          "cluster_id": 9012794,
          "cite": [
            "979 F.2d 714"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Koyomejian",
          "cluster_id": 9002607,
          "cite": [
            "946 F.2d 1450",
            "1991 WL 204462"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane1_negative"
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
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Steagald v. United States",
          "cluster_id": 110464,
          "cite": [
            "68 L. Ed. 2d 38",
            "101 S. Ct. 1642",
            "451 U.S. 204",
            "1981 U.S. LEXIS 89",
            "49 U.S.L.W. 4418"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
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
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Garrison",
          "cluster_id": 111823,
          "cite": [
            "94 L. Ed. 2d 72",
            "107 S. Ct. 1013",
            "480 U.S. 79",
            "1987 U.S. LEXIS 559",
            "55 U.S.L.W. 4190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lewis v. United States",
          "cluster_id": 110213,
          "cite": [
            "63 L. Ed. 2d 198",
            "100 S. Ct. 915",
            "445 U.S. 55",
            "1980 U.S. LEXIS 85"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Grubbs",
          "cluster_id": 145670,
          "cite": [
            "164 L. Ed. 2d 195",
            "126 S. Ct. 1494",
            "547 U.S. 90",
            "2006 U.S. LEXIS 2496"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lawmaster v. Ward",
          "cluster_id": 155277,
          "cite": [
            "125 F.3d 1341",
            "1997 WL 577708"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mink v. Knox",
          "cluster_id": 158328,
          "cite": [
            "613 F.3d 995",
            "38 Media L. Rep. (BNA) 1961",
            "2010 U.S. App. LEXIS 14684",
            "2010 WL 2802729"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cynthia Archer v. John Chisholm",
          "cluster_id": 4422481,
          "cite": [
            "870 F.3d 603",
            "2017 WL 3709149",
            "2017 U.S. App. LEXIS 16493"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. George Wuagneux",
          "cluster_id": 406519,
          "cite": [
            "683 F.2d 1343",
            "1982 U.S. App. LEXIS 16435",
            "11 Fed. R. Serv. 334"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jimmy Dewitt Webster, Sr., Candido Daniel Santiago, Barry Weinreich, Joe Buhajla, Arthur Byron Murphy, and Clarence Royalston",
          "cluster_id": 445460,
          "cite": [
            "750 F.2d 307"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Liston v. County of Riverside",
          "cluster_id": 7049587,
          "cite": [
            "120 F.3d 965",
            "97 Daily Journal DAR 9229",
            "97 Cal. Daily Op. Serv. 5742",
            "1997 U.S. App. LEXIS 18962",
            "1997 WL 403988"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Henning Heldt and Duke Snider, United States of America v. Mary Sue Hubbard, United States of America v. Sharon Thomas, United States of America v. Gregory Willardson, United States of America v. Richard Weigand, United States of America v. Cindy Raymond, United States of America v. Gerald Bennett Wolfe, United States of America v. Mitchell Hermann",
          "cluster_id": 398883,
          "cite": [
            "668 F.2d 1238"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Southard",
          "cluster_id": 8926695,
          "cite": [
            "700 F.2d 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gilmere v. City Of Atlanta",
          "cluster_id": 459876,
          "cite": [
            "774 F.2d 1495"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Euge",
          "cluster_id": 110191,
          "cite": [
            "63 L. Ed. 2d 141",
            "100 S. Ct. 874",
            "444 U.S. 707",
            "1980 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lawmaster v. Ward",
          "cluster_id": 746807,
          "cite": [
            "125 F.3d 1341",
            "1997 Colo. J. C.A.R. 2061",
            "1997 U.S. App. LEXIS 25248"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Abu-Jihaad",
          "cluster_id": 181375,
          "cite": [
            "630 F.3d 102",
            "2010 U.S. App. LEXIS 25832",
            "2010 WL 5140864"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fred Tarpley, Sr. v. Raymond J. Greene",
          "cluster_id": 406593,
          "cite": [
            "684 F.2d 1",
            "221 U.S. App. D.C. 227",
            "1982 U.S. App. LEXIS 17751"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Purdy Lambert (84-5660) Philip M. Block (84-5661), Defendants",
          "cluster_id": 457615,
          "cite": [
            "771 F.2d 83",
            "1985 U.S. App. LEXIS 22335"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jack Southard, United States of America v. Monsour Ferris, A/K/A Monte, United States of America v. Lester Banker, A/K/A Lem, United States of America v. John Brian, A/K/A John Baborian, United States of America v. Anna Quinterno, United States of America v. Vincent Quinterno, United States of America v. Harry Kachougian, A/K/A Tom and Tommy, United States of America v. Robert Martin, United States of America v. Bernard Falk, United States of America v. Anthony Lauro, A/K/A Poochie",
          "cluster_id": 414332,
          "cite": [
            "700 F.2d 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Aaron Graham",
          "cluster_id": 3208153,
          "cite": [
            "824 F.3d 421",
            "2016 WL 3068018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mark L. Simons",
          "cluster_id": 767973,
          "cite": [
            "206 F.3d 392",
            "2000 U.S. App. LEXIS 2877",
            "2000 WL 223332"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110061 OR 9427537 OR 9427538 OR 9427539) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NDQ0NTc2MDAwMDAmcz04OTg4ODEzJnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110061+OR+9427537+OR+9427538+OR+9427539%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110061 OR 9427537 OR 9427538 OR 9427539)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05MiZzPTgxMDEzMyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110061+OR+9427537+OR+9427538+OR+9427539%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110061 OR 9427537 OR 9427538 OR 9427539)",
        "reviewed": 28,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 28,
        "triage_read": 0,
        "triage_snippet_classified": 28
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110061 OR 9427537 OR 9427538 OR 9427539)",
    "indexed_citing_opinions": 348,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110061,
        "count": 285,
        "count_source": "search"
      },
      {
        "opinion_id": 9427537,
        "count": 67,
        "count_source": "search"
      },
      {
        "opinion_id": 9427538,
        "count": 1,
        "count_source": "search"
      },
      {
        "opinion_id": 9427539,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 641,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/dalia-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2NzE2NjImcz05NDc2MzI0JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110061+OR+9427537+OR+9427538+OR+9427539%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110061,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 105021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 105172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 106078,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 106288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 106525,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 107319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 107735,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 108582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 108596,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 108767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 109572,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 109584,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 109755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 109876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 308678,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 324480,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 339006,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 344771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 345743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 349546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 350102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 355846,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 359575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 359662,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 1442699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 1595144,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 2443377,
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
    "date_created": "2026-07-05T01:55:39Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T01:55:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T01:55:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:04:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T01:55:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Dalia v. United States (truncated)

```
<div>
<center><b><span class="citation" data-id="9427537"><a href="/opinion/110061/dalia-v-united-states/" aria-description="Citation for case: Dalia v. United States">441 U.S. 238</a></span> (1979)</b></center>
<center><h1>DALIA<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 77-1722.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 9, 10, 1979.</center>
<center>Decided April 18, 1979.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE THIRD CIRCUIT.
<p><span class="star-pagination">*240</span> <i>Louis Ruprecht</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Deputy Solicitor General Frey</i> argued the cause for the United States. With him on the brief were <i>Solicitor General McCree, Assistant Attorney General Heymann, William C. Bryson, Kenneth S. Geller,</i> and <i>Jerome M. Feit.</i></p>
<p>MR. JUSTICE POWELL delivered the opinion of the Court.</p>
<p>Title III of the Omnibus Crime Control and Safe Streets Act of 1968 (Title III), <span class="citation no-link">18 U. S. C. §§ 2510-2520</span>, permits courts to authorize electronic surveillance<sup>[1]</sup> by Government officers in specified situations. We took this case by writ of <span class="star-pagination">*241</span> certiorari to resolve two questions concerning the implementation of Title III surveillance orders. <span class="citation multiple-matches"><a href="/c/U.%20S./439/817/">439 U. S. 817</a></span>. First, may courts authorize electronic surveillance that requires covert entry<sup>[2]</sup> into private premises for installation of the necessary equipment? Second, must authorization for such surveillance include a specific statement by the court that it approves of the covert entry?<sup>[3]</sup></p>
<p></p>
<h2>I</h2>
<p>On March 14, 1973, Justice Department officials applied to the United States District Court for the District of New Jersey, seeking authorization under <span class="citation no-link">18 U. S. C. § 2518</span> to intercept telephone conversations on two telephones in petitioner's business office. After examining the affidavits submitted in support of the Government's request, the District Court authorized the wiretap for a period of 20 days or until the purpose of the interception was achieved, whichever came first. The court found probable cause to believe that petitioner was a member of a conspiracy the purpose of which was to steal goods being shipped in interstate commerce in violation of <span class="citation no-link">18 U. S. C. § 659</span>. Moreover, the court found reason to believe that petitioner's business telephones were being used to further this conspiracy and that means of investigating the conspiracy <span class="star-pagination">*242</span> other than electronic surveillance would be unlikely to succeed and would be dangerous. The wiretap order carefully enumerated the telephones to be affected and the types of conversations to be intercepted. Finally, the court ordered the officials in charge of the interceptions to take all reasonable precautions "to minimize the interception of communications not otherwise subject to interception," and required the officials to make periodic progress reports.</p>
<p>At the end of the 20-day period covered by the March 14 court order, the Government requested an extension of the wiretap authorization. In addition, the Government for the first time asked the court to allow it to intercept all oral communications taking place in petitioner's office, including those not involving the telephone. On April 5, 1973, the court granted the Government's second request. Its order concerning the wiretap of petitioner's telephones closely tracked the March 14 order. Finding reasonable cause to believe that petitioner's office was being used by petitioner and others in connection with the alleged conspiracy, the court also authorized, for a maximum period of 20 days, the interception of all oral communications concerning the conspiracy at "the business office of Larry Dalia, consisting of an enclosed room, approximately fifteen (15) by eighteen (18) feet in dimension, and situated in the northwesterly corner of a one-story building housing Wrap-O-Matic Machinery Company, Ltd., and Precise Packaging, and located at 1105 West St. George Avenue, Linden, New Jersey." The order included protective provisions similar to those in the March 14 wiretapping order.<sup>[4]</sup> The electronic surveillance order of April 5 was extended by court order on April 27, 1973.</p>
<p><span class="star-pagination">*243</span> On November 6, 1975, petitioner was indicted in a five-count indictment charging that he had been involved in a <span class="star-pagination">*244</span> conspiracy to steal an interstate shipment of fabric.<sup>[5]</sup> At trial, the Government introduced evidence showing that petitioner had been approached in March 1973 and asked to store in his New Jersey warehouse "a load of merchandise." Although petitioner declined the request, he directed the requesting party to Higgins, an associate, with whom he agreed to share the $1,500 storage fee that was offered. The merchandise stored under this contract proved to be a tractor-trailer full of fabric worth $250,000 that three men stole on April 3, 1973, and transported to Higgins' warehouse. Two days after the theft, FBI agents arrested Higgins and the individuals involved in the robbery.</p>
<p>The Government introduced into evidence at petitioner's trial various conversations intercepted pursuant to the court <span class="star-pagination">*245</span> orders of March 14, April 5, and April 27, 1973. Intercepted telephone conversations showed that petitioner had arranged for the storage at Higgins' warehouse and had helped negotiate the terms for that storage. One telephone conversation that took place after Higgins' arrest made clear that petitioner had given advice to others involved in the robbery to "sit tight" and not to use the telephone. Finally, the Government introduced transcripts of conversations intercepted from petitioner's office under the April 5 bugging order. In these conversations, petitioner had discussed with various participants in the robbery how best to proceed after their confederates had been arrested. The unmistakable inference to be drawn from petitioner's statements in these conversations is that he was an active participant in the scheme to steal the truckload of fabric.</p>
<p>Before trial, petitioner moved to suppress evidence obtained through the interception of conversations by means of the device installed in his office. The District Court denied the suppression motion without prejudice to its being renewed following trial. After petitioner was convicted on two counts,<sup>[6]</sup> he renewed his motion and the court held an evidentiary hearing concerning the method by which the electronic device had been installed. At this hearing it was shown that, although the April 5 court order did not explicitly authorize entry of petitioner's business, the FBI agents assigned the task of implementing the order had entered petitioner's office secretly at midnight on April 5 and had spent three hours in the building installing an electronic bug in the ceiling. All electronic surveillance of petitioner ended on May 16, 1973, at which time the agents re-entered petitioner's office and removed the bug.</p>
<p>In denying a second time petitioner's motion to suppress the evidence obtained from the bug, the trial court ruled <span class="star-pagination">*246</span> that under Title III a covert entry to install electronic eavesdropping equipment is not unlawful merely because the court approving the surveillance did not explicitly authorize such an entry. <span class="citation" data-id="1595144"><a href="/opinion/1595144/united-states-v-dalia/" aria-description="Citation for case: United States v. Dalia">426 F. Supp. 862</a></span> (1977). Indeed, in the court's view, "implicit in the court's order [authorizing electronic surveillance] is concomitant authorization for agents to covertly enter the premises in question and install the necessary equipment." <span class="citation" data-id="1595144"><a href="/opinion/1595144/united-states-v-dalia/#866" aria-description="Citation for case: United States v. Dalia"><i>Id.,</i> at 866</a></span>. As the court concluded that the FBI agents who had installed the electronic device were executing a lawful warrant issued by the court, the sole question was whether the method they chose for execution was reasonable. Under the circumstances, the court found the covert entry of petitioner's office to have been "the safest and most successful method of accomplishing the installation." <i><span class="citation" data-id="1595144"><a href="/opinion/1595144/united-states-v-dalia/" aria-description="Citation for case: United States v. Dalia">Ibid.</a></span></i> Indeed, noting that petitioner himself had indicated that such a device could only have been installed through such an entry, the court observed that "[i]n most cases the only form of installing such devices is through breaking and entering. The nature of the act is such that entry must be surreptitious and must not arouse suspicion, and the installation must be done without the knowledge of the residents or occupants." <i><span class="citation" data-id="1595144"><a href="/opinion/1595144/united-states-v-dalia/" aria-description="Citation for case: United States v. Dalia">Ibid.</a></span></i></p>
<p>The Court of Appeals for the Third Circuit affirmed petitioner's conviction. <span class="citation" data-id="355846"><a href="/opinion/355846/united-states-v-lawrence-dalia/" aria-description="Citation for case: United States v. Lawrence Dalia">575 F. 2d 1344</a></span> (1978). Agreeing with the District Court, it rejected petitioner's contention that separate court authorization was necessary for the covert entry of petitioner's office, although it noted that "the more prudent or preferable approach for government agents would be to include a statement regarding the need of a surreptitious entry in a request for the interception of oral communications when a break-in is contemplated." <span class="citation" data-id="355846"><a href="/opinion/355846/united-states-v-lawrence-dalia/#1346" aria-description="Citation for case: United States v. Lawrence Dalia"><i>Id.,</i> at 1346-1347</a></span>.</p>
<p></p>
<h2>II</h2>
<p>Petitioner first contends that the Fourth Amendment prohibits covert entry of private premises in all cases, irrespective of the reasonableness of the entry or the approval of a court. <span class="star-pagination">*247</span> He contends that Title III is unconstitutional insofar as it enables courts to authorize covert entries for the installation of electronic bugging devices.</p>
<p>In several cases this Court has implied that in some circumstances covert entry to install electronic bugging devices would be constitutionally acceptable if done pursuant to a search warrant. Thus, for example, in <i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">347 U. S. 128</a></span> (1954), the plurality stated that in conducting electronic surveillance, state police officers had "flagrantly, deliberately, and persistently violated the fundamental principle declared by the Fourth Amendment as a restriction on the Federal Government." <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#132" aria-description="Citation for case: Irvine v. California"><i>Id.,</i> at 132</a></span>. It emphasized that the bugging equipment was installed through a covert entry of the defendant's home "<i>without a search warrant</i> or other process." <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Ibid.</a></span></i> (emphasis added). Similarly, in <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 511-512</a></span> (1961), it was noted that "[t]his Court has never held that a federal officer may <i>without warrant</i> and without consent physically entrench into a man's office or home, there secretly observe or listen, and relate at the man's subsequent criminal trial what was seen or heard." (Emphasis added.) Implicit in decisions such as <i><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">Silverman</a></span></i> and <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Irvine</a></span></i> has been the Court's view that covert entries are constitutional in some circumstances, at least if they are made pursuant to warrant.</p>
<p>Moreover, we find no basis for a constitutional rule proscribing all covert entries. It is well established that law officers constitutionally may break and enter to execute a search warrant where such entry is the only means by which the warrant effectively may be executed. See, <i>e. g., </i><i>Payne</i> v. <i>United States,</i> <span class="citation" data-id="324480"><a href="/opinion/324480/charles-edward-payne-v-united-states/#1394" aria-description="Citation for case: Charles Edward Payne v. United States">508 F. 2d 1391, 1394</a></span> (CA5 1975); cf. <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#28" aria-description="Citation for case: Ker v. California">374 U. S. 23, 28, 38</a></span> (1963); <span class="citation no-link">18 U. S. C. § 3109</span>. Petitioner nonetheless argues that covert entries are unconstitutional for their lack of notice. This argument is frivolous, as was indicated in <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span>, 355 n. 16 (1967), where the Court stated that "officers need not <span class="star-pagination">*248</span> announce their purpose before conducting an otherwise [duly] authorized search if such an announcement would provoke the escape of the suspect or the destruction of critical evidence."<sup>[7]</sup> In <i>United States</i> v. <i>Donovan,</i> <span class="citation" data-id="9426645"><a href="/opinion/109584/united-states-v-donovan/" aria-description="Citation for case: United States v. Donovan">429 U. S. 413</a></span>, 429 n. 19 (1977), we held that Title III provided a constitutionally adequate substitute for advance notice by requiring that once the surveillance operation is completed the authorizing judge must cause notice to be served on those subjected to surveillance. See <span class="citation no-link">18 U. S. C. § 2518</span> (8) (d). There is no reason why the same notice is not equally sufficient with respect to electronic surveillances requiring covert entry. We make explicit, therefore, what has long been implicit in our decisions dealing with this subject: The Fourth Amendment does not prohibit <i>per se</i> a covert entry performed for the purpose of installing otherwise legal electronic bugging equipment.<sup>[8]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*249</span> III</h2>
<p>Petitioner's second contention is that Congress has not given the courts statutory authority to approve covert entries for the purpose of installing electronic surveillance equipment, even if constitutionally it could have done so. Petitioner emphasizes that although Title III sets forth with meticulous care the circumstances in which electronic surveillance is permitted, there is no comparable indication in the statute that covert entry ever may be ordered. Accord, <i>United States</i> v. <i>Santora,</i> <span class="citation" data-id="359575"><a href="/opinion/359575/united-states-v-ronald-santora-earl-rardin-maurice-eugene-lickteig/#457" aria-description="Citation for case: United States v. Ronald Santora, Earl Rardin, Maurice...">583 F. 2d 453, 457-458</a></span> (CA9 1978).</p>
<p>Title III does not refer explicitly to covert entry. The language, structure, and history of the statute, however, demonstrate that Congress meant to authorize courtsin certain specified circumstancesto approve electronic surveillance without limitation on the means necessary to its accomplishment, so long as they are reasonable under the circumstances. Title III provides a comprehensive scheme for the regulation of electronic surveillance, prohibiting all secret interception of communications except as authorized by certain state and federal judges in response to applications from specified federal and state law enforcement officials. See <span class="citation no-link">18 U. S. C. §§ 2511</span>, 2515, and 2518; <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#301" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 301-302</a></span> (1972). Although Congress was fully aware of the distinction between bugging and wiretapping, see S. Rep. No. 1097, 90th Cong., 2d Sess., 68 (1968), Title III by its terms deals with each form of surveillance in essentially the same manner. See <span class="citation no-link">18 U. S. C. §§ 2510</span> (1) and (2); n. 1, <i>supra.</i> Orders authorizing interceptions of either wire or oral communications may be entered only after the court has made specific determinations concerning the likelihood that the interception will disclose evidence of criminal conduct. See <span class="citation no-link">18 U. S. C. § 2518</span> (3). Moreover, with respect to both wiretapping and bugging, an authorizing court must <span class="star-pagination">*250</span> specify the exact scope of the surveillance undertaken, enumerating the parties whose communications are to be overheard (if they are known), the place to be monitored, and the agency that will do the monitoring. See <span class="citation no-link">18 U. S. C. § 2518</span> (4).</p>
<p>The plain effect of the detailed restrictions of § 2518 is to guarantee that wiretapping or bugging occurs only when there is a genuine need for it and only to the extent that it is needed.<sup>[9]</sup> Once this need has been demonstrated in accord with the requirements of § 2518, the courts have broad authority to "approv[e] interception of wire or oral communications," <span class="citation no-link">18 U. S. C. §§ 2516</span> (1), (2), subject of course to constitutional limitations. See Part II, <i>supra.</i><sup>[10]</sup> Nowhere in Title III is there any indication that the authority of courts under § 2518 is to be limited to approving those methods of interception that do not require covert entry for installation of the intercepting equipment.<sup>[11]</sup></p>
<p><span class="star-pagination">*251</span> The legislative history of Title III underscores Congress' understanding that courts would authorize electronic surveillance in situations where covert entry of private premises was necessary. Indeed, a close examination of that history reveals that Congress did not explicitly address the question of covert entries in the Act, only because it did not perceive surveillance requiring such entries to differ in any important way from that performed without entry. Testimony before subcommittees considering Title III and related bills indicated that covert entries were a necessary part of most electronic bugging operations. See, <i>e. g.,</i> Anti-Crime Program: Hearings on H. R. 5037, etc., before Subcommittee No. 5 of the House Committee on the Judiciary, 90th Cong., 1st Sess., 1031 (1967). Moreover, throughout the Senate Report on Title III indiscriminate reference is made to the types of surveillance this Court reviewed in <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967), and <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967). See, <i>e. g.,</i> S. Rep. No. 1097, <i>supra,</i> at 74-75, 97, 101-102, 105. Apparently Committee members did not find it significant that <i><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span></i> involved a covert entry, whereas <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> did not. Compare <i>Berger</i> v. <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#45" aria-description="Citation for case: Berger v. New York"><i>New York, supra,</i> at 45</a></span>, with <i>Katz</i> v. <i>United States, supra,</i> at 348.<sup>[12]</sup></p>
<p>It is understandable, therefore, that by the time Title III <span class="star-pagination">*252</span> was discussed on the floor of Congress, those Members who referred to covert entries indicated their understanding that such entries would necessarily be a part of bugging authorized under Title III. Thus, for example, in voicing his support for Title III Senator Tydings emphasized the difficulties attendant upon installing necessary equipment:</p>
<blockquote>"[S]urveillance is very difficult to use. Tape [<i>sic</i>] must be installed on telephones, and wires strung. <i>Bugs are difficult to install in many places since surreptitious entry is often impossible. Often, more than one entry is necessary to adjust equipment.</i>" 114 Cong. Rec. 12989 (1968) (emphasis added).</blockquote>
<p>In the face of this record, one simply cannot assume that Congress, aware that most bugging requires covert entry, nonetheless wished to except surveillance requiring such entries from the broad authorization of Title III, and that it resolved to do so by remaining silent on the subject. On the contrary, the language and history of Title III convey quite a different explanation for Congress' failure to distinguish between surveillance that requires covert entry and that which does not: Those considering the surveillance legislation understood that, by authorizing electronic interception of oral communications in addition to wire communications, they were necessarily authorizing surreptitious entries.</p>
<p>Finally, Congress' purpose in enacting the statute would be largely thwarted if we were to accept petitioner's invitation to read into Title III a limitation on the courts' authority under § 2518. Congress permitted limited electronic surveillance under Title III because it concluded that both wiretapping and bugging were necessary to enable law enforcement authorities to combat successfully certain forms of crime.<sup>[13]</sup><span class="star-pagination">*253</span> Absent covert entry, however, almost all electronic bugging would be impossible.<sup>[14]</sup> See <i>United States</i> v. <i>Ford,</i> <span class="citation" data-id="1442699"><a href="/opinion/1442699/united-states-v-ford/#882" aria-description="Citation for case: United States v. Ford">414 F. Supp. 879, 882</a></span> (DC 1976), aff'd, 180 U. S. App. D. C. 1, <span class="citation" data-id="344771"><a href="/opinion/344771/united-states-v-carroll-d-ford-united-states-of-america-v-wesley/" aria-description="Citation for case: United States v. Carroll D. Ford. United States of...">553 F. 2d 146</a></span> (1977); McNamara, The Problem of Surreptitious Entry <span class="star-pagination">*254</span> to Effectuate Electronic Eavesdrops: How Do You Proceed After the Court Says "Yes"?, <span class="citation no-link">15 Am. Crim. L. Rev. 1</span>, 3 (1977). As recently as 1976, a congressional commission established to study and evaluate the effectiveness of Title III concluded that in most cases electronic surveillance cannot be performed without covert entry into the premises being monitored. See U. S. National Commission for Review of Federal and State Laws Relating to Wiretapping and Electronic Surveillance, Electronic Surveillance 15, 43, and n. 19, 86 (1976). The same conclusion was reached by the American Bar Association committee charged with formulating standards governing use of electronic surveillance. See ABA Project on Minimum Standards for Criminal Justice, Electronic Surveillance 65 n. 175, 149 (App. Draft 1971).<sup>[15]</sup></p>
<p>In sum, we conclude that Congress clearly understood that it was conferring power upon the courts to authorize covert entries ancillary to their responsibility to review and approve surveillance applications under the statute. To read the statute otherwise would be to deny the "respect for the policy of Congress [that] must save us from imputing to it a self-defeating, if not disingenuous purpose." <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span> (1939).<sup>[16]</sup></p>
<p></p>
<h2>IV</h2>
<p>Petitioner's final contention is that, if covert entries are to be authorized under Title III, the authorizing court must <span class="star-pagination">*255</span> explicitly set forth its approval of such entries before the fact. In this case, as is customary, the court's order constituted the sole written authorization of the surveillance of petitioner's office. As it did not state in terms that the surveillance was to include a covert entry, petitioner insists that the entry violated his Fourth Amendment privacy rights. Accord, <i>United States</i> v. <i><span class="citation" data-id="1442699"><a href="/opinion/1442699/united-states-v-ford/" aria-description="Citation for case: United States v. Ford">Ford</a></span>,</i> 180 U. S. App. D. C., at 25, <span class="citation" data-id="344771"><a href="/opinion/344771/united-states-v-carroll-d-ford-united-states-of-america-v-wesley/#170" aria-description="Citation for case: United States v. Carroll D. Ford. United States of...">553 F. 2d, at 170</a></span>; <i>Application of United States,</i> <span class="citation" data-id="349546"><a href="/opinion/349546/application-of-the-united-states-for-an-order-authorizing-the-interception/#644" aria-description="Citation for case: Application of the United States for an Order Authorizing...">563 F. 2d 637, 644</a></span> (CA4 1977).<sup>[17]</sup></p>
<p>The Fourth Amendment requires that search warrants be issued only "upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." Finding these words to be "precise and clear," <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481</a></span> (1965), this Court has interpreted them to require only three things. First, warrants must be issued by neutral, disinterested magistrates. See, <i>e. g., </i><i>Connally</i> v. <i>Georgia,</i> <span class="citation" data-id="109572"><a href="/opinion/109572/connally-v-georgia/#250" aria-description="Citation for case: Connally v. Georgia">429 U. S. 245, 250-251</a></span> (1977) (<i>per curiam</i>); <i>Shadwick</i> v. <i>Tampa,</i> <span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/#350" aria-description="Citation for case: Shadwick v. City of Tampa">407 U. S. 345, 350</a></span> (1972); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#459" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 459-460</a></span> (1971). Second, those seeking the warrant must demonstrate to the magistrate their probable cause to believe that "the evidence sought will aid in a particular apprehension or conviction" for a particular offense. <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#307" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 307</a></span> (1967). Finally, "warrants must particularly describe the `things to be seized,' " as well as the place to be searched. <i>Stanford</i> v. <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas"><i>Texas, supra,</i> at 485</a></span>.</p>
<p><span class="star-pagination">*256</span> In the present case, the April 5 court order authorizing the interception of oral communications occurring within petitioner's office was a warrant issued in full compliance with these traditional Fourth Amendment requirements. It was based upon a neutral magistrate's independent finding of probable cause to believe that petitioner had been and was committing specifically enumerated federal crimes, that petitioner's office was being used "in connection with the commission of [these] offenses," and that bugging the office would result in the interception of "oral communications concerning these offenses." App. 6a-7a. Moreover, the exact location and dimensions of petitioner's office were set forth, see n. 4, <i>supra,</i> and the extent of the search was restricted to the "[i]ntercept[ion of] oral communications of Larry Dalia and others as yet unknown, concerning the above-described offenses at the business office of Larry Dalia . . . ." App. 8a.<sup>[18]</sup></p>
<p>Petitioner contends, nevertheless, that the April 5 order was insufficient under the Fourth Amendment for its failure to specify that it would be executed by means of a covert <span class="star-pagination">*257</span> entry of his office. Nothing in the language of the Constitution or in this Court's decisions interpreting that language suggests that, in addition to the three requirements discussed above, search warrants also must include a specification of the precise manner in which they are to be executed. On the contrary, it is generally left to the discretion of the executing officers to determine the details of how best to proceed with the performance of a search authorized by warrant<sup>[19]</sup>subject of course to the general Fourth Amendment protection "against unreasonable searches and seizures."</p>
<p>Recognizing that the specificity required by the Fourth Amendment does not generally extend to the means by which warrants are executed, petitioner further argues that warrants for electronic surveillance are unique because often they impinge upon two different Fourth Amendment interests: The surveillance itself interferes only with the right to hold private conversations, whereas the entry subjects the suspect's property to possible damage and personal effects to unauthorized examination. This view of the Warrant Clause parses too finely the interests protected by the Fourth Amendment. Often in executing a warrant the police may find it necessary to interfere with privacy rights not explicitly considered by the judge who issued the warrant. For example, police executing an arrest warrant commonly find it necessary to enter <span class="star-pagination">*258</span> the suspect's home in order to take him into custody, and they thereby impinge on both privacy and freedom of movement. See, <i>e. g., </i><i>United States</i> v. <i>Cravero,</i> <span class="citation" data-id="8900306"><a href="/opinion/8912462/united-states-v-cravero/#421" aria-description="Citation for case: United States v. Cravero">545 F. 2d 406, 421</a></span> (CA5 1976) (on petition for rehearing). Similarly, officers executing search warrants on occasion must damage property in order to perform their duty. See, <i>e. g., </i><i>United States</i> v. <i>Brown,</i> <span class="citation" data-id="345743"><a href="/opinion/345743/united-states-v-henry-joie-brown/#305" aria-description="Citation for case: United States v. Henry Joie Brown">556 F. 2d 304, 305</a></span> (CA5 1977); <i>United States</i> v. <i>Gervato,</i> <span class="citation" data-id="308678"><a href="/opinion/308678/united-states-v-frank-gervato/#41" aria-description="Citation for case: United States v. Frank Gervato">474 F. 2d 40, 41</a></span> (CA3), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/864/">414 U. S. 864</a></span> (1973).</p>
<p>It would extend the Warrant Clause to the extreme to require that, whenever it is reasonably likely that Fourth Amendment rights may be affected in more than one way, the court must set forth precisely the procedures to be followed by the executing officers. Such an interpretation is unnecessary, as we have heldand the Government concedesthat the manner in which a warrant is executed is subject to later judicial review as to its reasonableness. See <i>Zurcher</i> v. <i>Stanford Daily,</i> <span class="citation" data-id="9427224"><a href="/opinion/109876/zurcher-v-stanford-daily/#559" aria-description="Citation for case: Zurcher v. Stanford Daily">436 U. S. 547, 559-560</a></span> (1978).<sup>[20]</sup> More important, we would promote empty formalism were we to require magistrates to make explicit what unquestionably is implicit in bugging authorizations:<sup>[21]</sup> that a covert entry, with its attendant interference with Fourth Amendment interests, may be necessary for the installation of the surveillance equipment. See <i>United States</i> v. <i>London,</i> <span class="citation" data-id="1444545"><a href="/opinion/1444545/united-states-v-london/#560" aria-description="Citation for case: United States v. London">424 F. Supp. 556, 560</a></span> (Md. 1976). We conclude, therefore, that the Fourth Amendment does not require that a Title III electronic surveillance order include a <span class="star-pagination">*259</span> specific authorization to enter covertly the premises described in the order.<sup>[22]</sup></p>
<p>The judgment of the Court of Appeals is</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE BRENNAN, with whom MR. JUSTICE STEWART joins except as to Part I, concurring in part and dissenting in part.</p>
<p>I concur in Parts I and II of the Court's opinion.</p>
<p></p>
<h2>I</h2>
<p>I dissent from Part III for the reasons stated in the dissenting opinion of MR. JUSTICE STEVENS which I join.</p>
<p></p>
<h2>II</h2>
<p>I also dissent from Part IV. In my view, even reading Title III to authorize covert entries, the Justice Department's present practice of securing specific authorization for covert entries is not only preferable, see <i>ante,</i> this page n. 22, but also constitutionally required.</p>
<p>Breaking and entering into private premises for the purpose of planting a bug cannot be characterized as a mere mode of warrant execution to be left to the discretion of the executing officer. See <i>ante,</i> at 257. The practice entails an invasion <span class="star-pagination">*260</span> of privacy of constitutional significance distinct from that which attends nontrespassory surveillance; indeed, it is tantamount to an independent search and seizure. First, rooms may be bugged without the need for surreptitious entry and physical invasion of private premises. See <i>Lopez</i> v. <i>United States,</i> <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#467" aria-description="Citation for case: Lopez v. United States">373 U. S. 427, 467-468</a></span> (1963) (BRENNAN, J., dissenting). Second, covert entry, a practice condemned long before we condemned unwarranted eavesdropping, see <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961), breaches physical as well as conversational privacy. The home or office itself, that "inviolate place which is a man's castle," <i><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">id.,</a></span></i> at 512 n. 4, is invaded. Third, the practice is particularly intrusive and susceptible to abuse since it leaves naked to the hands and eyes of government agents items beyond the reach of simple eavesdropping.</p>
<p>Because of these additional intrusions attendant to covert entries, the Constitution requires that government agents who wish to break into private premises first secure specific judicial authorization for the surreptitious entry. Authority for the physical invasion cannot be derived from a Title III order authorizing only electronic surveillance.</p>
<p>"[T]he Fourth Amendment confines an officer executing a search warrant strictly within the bounds set by the warrant," <i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span>, 394 n. 7 (1971), in order to assure that those "searches deemed necessary [remain] as limited as possible." <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#467" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 467</a></span> (1971). See <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 485</a></span> (1965); <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 196</a></span> (1927).<sup>[*]</sup> As a consequence, a warrant that describes <span class="star-pagination">*261</span> only the seizure of conversations cannot be read expansively to authorize constitutionally distinct physical invasions of privacy at the discretion of the executing officer. Rather, the Constitution demands that the necessity for home invasion be decided "by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948).</p>
<p>I cannot agree that adherence to this principle would amount to "specification of the precise manner" in which Title III orders are executed. See <i>ante,</i> at 257. The warrant could, consistent with the command of the Fourth Amendment, leave the details of how best to proceed with the covert entry to the discretion of the executing officers. The warrant need only state, as under the present Justice Department practice, that "surreptitious entry for the purpose of installing and removing any electronic interception devices [is] to be utilized in accomplishing the oral interception." <i>Ante,</i> at 259 n. 22.</p>
<p>Nor can I agree that adherence to the strictures of the Warrant and Particularity Clauses of the Fourth Amendment would amount to "empty formalism." See <i>ante,</i> at 258. Since premises may be bugged through means less drastic than home invasion, requiring police to secure prior approval for covert entries may well prevent unnecessary and improper intrusions. In any event, that the present case may not appear particularly abusive cannot justify the Court's crabbed interpretation of the Fourth Amendment. Mr. Justice Bradley's <span class="star-pagination">*262</span> admonition almost a century ago has even greater cogency in today's world of ever more intrusive governmental invasions of privacy:</p>
<blockquote>"It may be that it is the obnoxious thing in its mildest and least repulsive form; but illegitimate and unconstitutional practices get their first footing in that way, namely, by silent approaches and slight deviations from legal modes of procedure. This can only be obviated by adhering to the rule that constitutional provisions for the security of person and property should be liberally construed. A close and literal construction deprives them of half their efficacy, and leads to gradual depreciation of the right, as if it consisted more in sound than in substance. It is the duty of courts to be watchful for the constitutional rights of the citizen, and against any stealthy encroachments thereon." <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 635</a></span> (1886).</blockquote>
<p>MR. JUSTICE STEVENS, with whom MR. JUSTICE BRENNAN and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>At midnight on the night of April 5-6, 1973, three persons pried open a window to petitioner's business office and secretly entered the premises. During the next three hours they moved freely about the building, eventually implanting a listening device in the ceiling. Several weeks later, they again broke into the office at night and removed the device.</p>
<p>The perpetrators of these break-ins were agents of the Federal Bureau of Investigation. Their office, however, carries with it no general warrant to trespass on private property. Without legislative or judicial sanction, the conduct of these agents was unquestionably "unreasonable" and therefore prohibited by the Fourth Amendment.<sup>[1]</sup> Moreover, that conduct <span class="star-pagination">*263</span> violated the Criminal Code of the State of New Jersey unless it was duly authorized.<sup>[2]</sup></p>
<p>The only consideration that arguably might legitimate these "otherwise tortious and possibly criminal" invasions of petitioner's private property,<sup>[3]</sup> is the fact that a federal judge had entered an order authorizing the agents to use electronic equipment to intercept oral communications at petitioner's office. The order, however, did not describe the kind of equipment to be used and made no reference to an entry, covert or otherwise, into private property. Nor does any statute expressly permit such activity or even authorize a federal judge to enter orders granting federal agents a license to commit criminal trespass. The initial question this case raises, therefore, is whether this kind of power should be read into a statute that does not expressly grant it.</p>
<p>In my opinion, there are three reasons, each sufficient by itself, for refusing to do so. First, until Congress has stated otherwise, our duty to protect the rights of the individual should hold sway over the interest in more effective law enforcement. Second, the structural detail of this statute precludes a reading that converts silence into thunder. Third, the legislative history affirmatively demonstrates that Congress never contemplated the situation now before the Court.</p>
<p></p>
<h2>I</h2>
<p>"Congress, like this Court, has an obligation to obey the mandate of the Fourth Amendment." <i>Marshall</i> v. <i>Barlow's Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#334" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 334</a></span> (STEVENS, J., dissenting). But Congress is better equipped than the Judiciary to make the empirical <span class="star-pagination">*264</span> judgment that a previously unauthorized investigative technique represents a "reasonable" accommodation between the privacy interests protected by the Fourth Amendment and effective law enforcement.<sup>[4]</sup> Throughout our history, therefore, it has been Congress that has taken the lead in granting new authority to invade the citizen's privacy.<sup>[5]</sup> It is appropriate to accord special deference to Congress whenever it has expressly balanced the need for a new investigatory technique against the undesirable consequences of any intrusion on constitutionally protected interests in privacy. See <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#334" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><i>id.,</i> at 334-339</a></span>.</p>
<p>But no comparable deference should be given federal intrusions on privacy that are not expressly authorized by Congress.<sup>[6]</sup> In my view, a proper respect for Congress' important <span class="star-pagination">*265</span> role in this area, as well as our tradition of interpreting statutes to avoid constitutional issues,<sup>[7]</sup> compels this conclusion.</p>
<p>The Court does not share this view. For this is the third time in as many years that it has condoned a serious intrusion on privacy that was not explicitly authorized by statute and that admittedly raised a substantial constitutional question. In <i>United States</i> v. <i>Ramsey,</i> <span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">431 U. S. 606</a></span>, the Court upheld an Executive regulation authorizing postal inspectors to open private letters without probable cause to believe they contained contraband.<sup>[8]</sup> In <i>United States</i> v. <i>New York Telephone Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S. 159</a></span>, the Court upheld orders authorizing the surreptitious pen-register surveillance of an individual and directing a private company to lend its assistance in that endeavor. Again, no explicit statutory authority existed for either order, despite Congress' otherwise comprehensive treatment of wire surveillance in Title III of the Omnibus Crime Control and Safe Streets Act of 1968 (Title III).<sup>[9]</sup></p>
<p><span class="star-pagination">*266</span> Today the Court has gone even further in finding an implicit grant of Executive power in Title III. That Title "does not refer explicitly to covert entry" of any kind, much less to entries that are tortious or criminal. <i>Ante,</i> at 249. Nevertheless, the Court holds that Congress, without having said so explicitly, has authorized the agents of a national police force in carrying out a surveillance order to break into private premises<sup>[10]</sup> in violation of state law. Moreover, the Court finds in the silent statute an open-ended authorization to effect such illegal entries without an explicit judicial determination that there is probable cause to believe they are necessary or even appropriate. In my judgment, it is most unrealistic to assume that Congress granted such broad and controversial authority to the Executive without making its intention to do so unmistakably plain. This is the paradigm case in which "the exact words of the statute provide the surest guide to determining Congress' intent."<sup>[11]</sup> I would not enlarge the coverage of the statute beyond its plain meaning.</p>
<p></p>
<h2>II</h2>
<p>The Court's conclusion that the statute implicitly authorizes breaking and entering is especially anomalous because the statutory scheme in all other respects is exhaustive and explicit.<sup>[12]</sup><span class="star-pagination">*267</span> "It simply does not make sense"<sup>[13]</sup> to conclude that Congresshaving minutely detailed (1) the process that "[t]he Attorney General, or any Assistant Attorney General specially designated by the Attorney General" must follow in authorizing federal police officers to seek an electronic surveillance order,<sup>[14]</sup> (2) the limited number of suspected offenses that will justify such an order,<sup>[15]</sup> (3) the showing that must be made to "a Federal judge" before he issues the order,<sup>[16]</sup> (4) the <span class="star-pagination">*268</span> standard the judge must apply in approving, and the format he must follow in preparing, the order,<sup>[17]</sup> (5) the time frame of execution and the manner of execution with respect to <span class="star-pagination">*269</span> minimizing the interception of communications not likely to involve criminal activity,<sup>[18]</sup> and even having more recently specified (6) certain "unobtrusive" means by which those <span class="star-pagination">*270</span> orders might be carried out without the awareness of the suspect<sup>[19]</sup>was content to leave national police officers with unbounded authority to carry out the resulting orders in any unspecified and obtrusive fashion they chose "subject of course to constitutional limitations." <i>Ante,</i> at 250.<sup>[20]</sup></p>
<p><span class="star-pagination">*271</span> In my view, it is the opposite conclusion that is true to the statutory structure. For "one simply cannot assume that Congress," see <i>ante,</i> at 252, wished to erect various procedural barriers against poor judgment on the part of the Attorney General and his subordinates in seeking, and on the part of federal district judges in issuing, eavesdropping orders only to commit their execution, even through illegal means, entirely to "the judgment and moderation of officers whose own interests and records are often at stake in the search." <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#182" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 182</a></span> (Jackson, J., dissenting). The detailed timing and minimization restrictions on the executing officer, see n. 18, <i>supra,</i> as well as the 1970 amendment to Title III concerning "unobtrusive" execution, see n. 19, <i>supra,</i> lead inescapably to the conclusion that Congress withheld authority to trespass on private property except through the limited means expressly dealt with in the statute.<sup>[21]</sup></p>
<p></p>
<h2>III</h2>
<p>Only one relevant conclusion can be drawn from a review of the entire legislative history of Title III. The legislators never even considered the possibility that they were passing a statute that would authorize federal agents to break into private premises without any finding of necessity by a neutral and detached magistrate.</p>
<p></p>
<h2>A</h2>
<p>The meager legislative remarks that are said to demonstrate that Title III's supporters implicitly endorsed breaking and <span class="star-pagination">*272</span> entering in order to install listening devices actually provide no support for that conclusion.</p>
<p>The reference to "judicial warrants authorizing [police] to hide bugs in the premises of criminal suspects," see <i>ante,</i> at 251 n. 12, was a comment by an <i>opponent</i> of the bill on investigative techniques that he believed this Court had ruled <i>illegal</i> in <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span>.<sup>[22]</sup> Since neither he, nor any supporter of the bill, suggested that those techniques would be authorized by Title III, his comment is hardly indicative of a legislative endorsement of such practices. Moreover, there is a marked difference between the judicially warranted "hid[ing of] bugs in the premises of criminal suspects" and a forcible entry that has not been expressly authorized by any judge. The difference between subterfuge and forcible trespass should not be ignored.</p>
<p>That difference explains why the Court's reliance on two statements by proponents of Title III that emphasize the technological limitations on "bugs" and "taps" is misplaced. The proponents believed these limitations would discourage the frequent use and abuse of electronic surveillance. Thus, in answer to repeated charges that passage of Title III would recreate Hitler's Germany or anticipate Orwell's "1984," Senator Tydings, in a passage partially quoted by the Court, <i>ante,</i> at 252, argued:</p>
<blockquote>"Contrary to what we have heard, electronic surveillance is not a lazy way to conduct an investigation. <i>It</i> <span class="star-pagination">*273</span> <i>will not be used wholesale as a substitute for physical investigation.</i>
</blockquote>
<p></p>
<h2>.....</h2>
<blockquote>"The reason[s] for such sparing use are simple. First, electronic surveillance is really useful only in conspiratorial activities. . . .</blockquote>
<blockquote>"Second, surveillance is very difficult to use. Tape must be installed on telephones and wires strung. <i>Bugs are difficult to install in many places since surreptitious entry is often impossible.</i> Often, more than one entry is necessary to adjust equipment. . . .</blockquote>
<blockquote>"Third, monitoring this equipment requires the expenditure of a great amount of law enforcement's time. . . ." 114 Cong. Rec. 12988-12989 (1968) (emphasis added).<sup>[23]</sup></blockquote>
<p>Read in context, this and like commentary are inconsistent with, rather than an endorsement of, unauthorized break-ins. For although it is of course true that surreptitious entry is often "impossible" when it must be accomplished without violating the law, surreptitious entry is by no means impossible (indeed, it is hardly "difficult") if it may be effected by whatever means the policeunhampered by the provisions of the criminal lawcan bring to their disposal. Despite the Court's understanding of it, I read Senator Tydings' remark as only one of many expressions by Title III's supporters of their belief that authorized electronic surveillance would be "carefully circumscribed," <i>id.,</i> at 13203 (Sen. Scott) and "rigidly controlled," <i>id.,</i> at 14715 (Sen. Tydings), not only by technology but also by "strict court supervision," <i>id.,</i> at 13200 (Sen. Scott), the "strictest guidelines," <i>id.,</i> at 16076 <span class="star-pagination">*274</span> (Rep. Harsha), and "an elaborate system of checks and safeguards." <i>Id.,</i> at 13204 (Sen. Scott).<sup>[24]</sup></p>
<p>Even the opponents of Title III, in parading before Congress the various invasions of privacy that they felt would accompany the passage of the statute, never once referred to breaking and entering private property. <i>E. g., id.,</i> at 14710 (Sen. Cooper); <i>id.,</i> at 14732 (Sen. Yarborough); <i>id.,</i> at 16066 (Rep. Celler). That they omitted such references while decrying far less aggravated invasions is strong evidence that they, at least, never thought about the issue that this case raises.<sup>[25]</sup> And since the sponsors of the legislation expressly stated that they had specified "every possible constitutional safeguard for the rights of individual privacy," <i>id.,</i> at <span class="star-pagination">*275</span> 14469 (Sen. McClellan),<sup>[26]</sup> their omission of any significant reference to these aggravated intrusions surely demonstrates that they did not consider this issue either.</p>
<p>In sum, as far as my research reveals, during the debates on Title III neither the proponents nor the opponents of the bill directly or indirectly expressed the view that the statute would authorize uninvited forcible trespasses by police officers as a means of implanting a listening device.</p>
<p></p>
<h2>B</h2>
<p>Because the drafters of Title III made "indiscriminate reference. . . to the types of surveillance this Court reviewed" in prior cases, <i>ante,</i> at 251, the Court draws the conclusion that Congress meant to authorize all "types of surveillance" discussed in those cases. The premise does not support the conclusion.</p>
<p>Many of those cases, including the two specifically cited by the Court,<sup>[27]</sup> held that the police conduct involved was unlawful. Rather than endorsing all of the techniques discussed in those cases, Congress was quite clearly trying to <i>avoid</i> the incidents of unconstitutionality those cases had <span class="star-pagination">*276</span> identified.<sup>[28]</sup> Moreover, in drafting Title III, the Senate Judiciary Committee did more than merely isolate and exclude from the bill the illegal elements of the police activity involved in those cases. Thus, the Chairman of the Committee, in answer to a colleague's question whether Title III was drafted in conformity with the Fourth Amendment, stated:</p>
<blockquote>"Completely so, let me say to my friend. Completely so, and it is <i>even more restrictive.</i> We have gone to every length which is proper, we think, to protect people's privacy." 114 Cong. Rec. 14470 (1968).</blockquote>
<p>It is of greater importance, however, that although Congress was concerned with the "types of <i>surveillance</i>" involved in our prior cases, none of the congressional references to those cases discussed the type of <i>entry</i> made to effectuate the surveillance. Not a word in any of those pre-1968 opinions, save one, described an illegal entry or even implied that such an entry had occurred. Those opinions instead described situations in which a listening device had been surreptitiously placed: against an office wall in order to hear conversations in the next office, <i>Goldman</i> v. <i>United States,</i> <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">316 U. S. 129</a></span>; on the person of a federal agent who recorded a conversation in the defendant's laundry, <i>On Lee</i> v. <i>United States,</i> <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/" aria-description="Citation for case: On Lee v. United States">343 U. S. 747</a></span>; in a cabaret, <i>Lopez</i> v. <i>United States,</i> <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">373 U. S. 427</a></span>; in a law office, <i>Osborn</i> v. <i>United States,</i> <span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/" aria-description="Citation for case: Osborn v. United States">385 U. S. 323</a></span>; against a spike inserted under a party wall, <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span>; on the outside of a public telephone booth, <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span>; and inside a private office, <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span>. It is, of course, true that the conduct in each cited case was surreptitious, but there is a vast difference between detective work that is merely clandestine and work that involves breaking and entering into private property. Before the decisions in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> and <i><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span>,</i> the former technique was considered to be lawful, warrant or <span class="star-pagination">*277</span> no warrant,<sup>[29]</sup> whereas the latter was considered unlawful.<sup>[30]</sup> The fact that Congress was prepared to enact a statute authorizing practices previously thought to be lawful surely does not justify the conclusion that it was equally prepared to authorize conduct that had always been made unlawful by the criminal laws of the various States.</p>
<p><i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">347 U. S. 128</a></span>, was the only pre-1968 case in which this Court had actually confronted the implantation of an electronic listening device by way of a "trespass, and probably a burglary, for which any unofficial person should be, and probably would be, severely punished." <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#132" aria-description="Citation for case: Irvine v. California"><i>Id.,</i> at 132</a></span>.<sup>[31]</sup> The plurality of four, speaking through Mr. Justice Jackson, had this to say about the police conduct in that case:</p>
<blockquote>"That officers of the law would break and enter a home, secrete such a device even in a bedroom, and listen to the conversations of the occupants for over a month would be incredible if it were not admitted. Few police measures have come to our attention that more flagrantly, deliberately, and persistently violated the fundamental <span class="star-pagination">*278</span> principle declared by the Fourth Amendment . . . ." <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Ibid.</a></span></i>
</blockquote>
<p>No Member of the Court disagreed with this assessment, although a majority refused to overturn the conviction because the exclusionary rule did not then apply to the States. While it is true, as the Court points out, <i>ante,</i> at 247, that four Members of the <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Irvine</a></span></i> Court adverted to the lack of a "search warrant or other process" to support the entry, <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#132" aria-description="Citation for case: Irvine v. California">347 U. S., at 132</a></span> (while the other three Members who discussed the issue found the police activity "offensive" and "revolting" without relying on the lack of a warrant<sup>[32]</sup>), it is also true that no Justice condoned a break-in absent some court order explicitly contemplating physical entry on the premises. Under any reading of the case, it cannot be taken as condoning official trespass and burglary absent specific authorization.</p>
<p>More importantly, the fact that Congress cited <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Irvine</a></span>,</i> without comment or explanation, when it was considering Title III cannot fairly be interpreted as an endorsement of the questionable police behavior that had been condemned so thunderously by Mr. Justice Jackson 14 years earlier. My respect for the lawmaking process forecloses the inference that Congress authorized burglarious conduct by such stealthy legislative history.</p>
<p></p>
<h2>IV</h2>
<p>Because it is not supported by either the text of the statute or the scraps of relevant legislative history,<sup>[33]</sup> I fear that the <span class="star-pagination">*279</span> Court's holding may reflect an unarticulated presumption that national police officers have the power to carry out a surveillance order by whatever means may be necessary unless explicitly prohibited by the statute or by the Constitution.</p>
<p>But surely the presumption should run the other way. Congressional silence should not be construed to authorize the Executive to violate state criminal laws or to encroach upon constitutionally protected privacy interests. Before confronting the serious constitutional issues raised by the Court's reading of Title III,<sup>[34]</sup> we should insist upon an unambiguous statement by Congress that this sort of police conduct may be authorized by a court and that a specific showing of necessity, or at least probable cause, must precede such an authorization. Without a legislative mandate that is both explicit and specific, I would presume that this flagrant invasion of the citizen's privacy is prohibited. Cf. <i>United States</i> v. <i>New York Telephone Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/#178" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S., at 178-179</a></span> (STEVENS, J., dissenting <span class="star-pagination">*280</span> in part); <i>United States</i> v. <i>Ramsey,</i> <span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#632" aria-description="Citation for case: United States v. Ramsey">431 U. S., at 632</a></span> (STEVENS, J., dissenting).<sup>[35]</sup></p>
<p>I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[1]  All types of electronic surveillance have the same purpose and effect: the secret interception of communications. As the Court set forth in <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#45" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 45-47</a></span> (1967), however, this surveillance is performed in two quite different ways. Some surveillance is performed by "wiretapping," which is confined to the interception of communication by telephone and telegraph and generally may be performed from outside the premises to be monitored. For a detailed description, see Note, Minimization of Wire Interception: Presearch Guidelines and Postsearch Remedies, <span class="citation no-link">26 Stan. L. Rev. 1411</span>, 1414 n. 18 (1974). At issue in the present case is the form of surveillance commonly known as "bugging," which includes the interception of all oral communication in a given location. Unlike wiretapping, this interception typically is accomplished by installation of a small microphone in the room to be bugged and transmission to some nearby receiver. See McNamara, The Problem of Surreptitious Entry to Effectuate Electronic Eavesdrops: How Do You Proceed After the Court Says "Yes"?, <span class="citation no-link">15 Am. Crim. L. Rev. 1</span>, 2 (1977); Blakey, Aspects of the Evidence Gathering Process in Organized Crime Cases: A Preliminary Analysis, reprinted in the President's Commission on Law Enforcement and Administration of Justice, Task Force Report: Organized Crime, App. C, 92, 97 (1967). Both wiretapping and bugging are regulated under Title III. See <span class="citation no-link">18 U. S. C. §§ 2510</span> (1) and (2).</p>
<p>[2]  Every electronic surveillance necessarily is "covert" in the sense that it must be "hidden; secret; disguised" to be effective. Webster's New International Dictionary 613 (2d ed. 1953). As used here, "covert entry" refers to the physical entry by a law enforcement officer into private premises without the owner's permission or knowledge in order to install bugging equipment. Generally, such an entry will require a breaking and entering. See discussion <i>infra,</i> at 253-254.</p>
<p>[3]  The Federal Courts of Appeals have given conflicting answers to these questions. See <i>United States</i> v. <i>Finazzo,</i> <span class="citation" data-id="9465129"><a href="/opinion/359662/united-states-v-salvatore-finazzo-dominic-j-licavoli/" aria-description="Citation for case: United States v. Salvatore Finazzo, Dominic J. Licavoli">583 F. 2d 837</a></span> (CA6 1978); <i>United States</i> v. <i>Santora,</i> <span class="citation" data-id="359575"><a href="/opinion/359575/united-states-v-ronald-santora-earl-rardin-maurice-eugene-lickteig/" aria-description="Citation for case: United States v. Ronald Santora, Earl Rardin, Maurice...">583 F. 2d 453</a></span> (CA9 1978); <i>United States</i> v. <i>Scafidi,</i> <span class="citation" data-id="8903769"><a href="/opinion/8915597/united-states-v-scafidi/" aria-description="Citation for case: United States v. Scafidi">564 F. 2d 633</a></span> (CA2 1977), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./436/903/">436 U. S. 903</a></span> (1978); <i>United States</i> v. <i>Ford,</i> 180 U. S. App. D. C. 1, <span class="citation multiple-matches"><a href="/c/F.%202d/553/146/">553 F. 2d 146</a></span> (1977); <i>United States</i> v. <i>Agrusa,</i> <span class="citation" data-id="9463064"><a href="/opinion/339006/united-states-v-salvatore-ross-agrusa/" aria-description="Citation for case: United States v. Salvatore Ross Agrusa">541 F. 2d 690</a></span> (CA8 1976), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./429/1045/">429 U. S. 1045</a></span> (1977).</p>
<p>[4]  In relevant part, the Title III order of April 5 provided:
</p>
<p>"[T]he Court finds:</p>
<p>"(a) There is probable cause to believe that Larry Dalia and others as yet unknown, have committed and are committing offenses involving theft from interstate shipments, in violation of Title <span class="citation no-link">18, United States Code, Section 659</span>; sale or receipt of stolen goods, in violation of Title <span class="citation no-link">18, United States Code, Section 2315</span>; and interference with commerce by threats or violence, in violation of Title <span class="citation no-link">18, United States Code, Section 1951</span>; and are conspiring to commit such offenses in violation of Section 371 of Title 18, United States Code.</p>
<p>"(b) There is probable cause to believe that particular wire and oral communications concerning these offenses will be obtained through these interceptions, authorization for which is herewith applied. In particular, these wire and oral communications will concern the theft or robbery of goods moving in interstate commerce, and the transportation, sale, receipt, storage, or distribution of these stolen goods, and the participants in the commission of said offenses.</p>
<p>"(c) Normal investigative procedures reasonably appear to be unlikely to succeed and are too dangerous to be used.</p>
<p>.....</p>
<p>"(e) There is probable cause to believe that the business office of Larry Dalia, consisting of an enclosed room, approximately fifteen (15) by eighteen (18) feet in dimension, and situated in the northwesterly corner of a one-story building housing Wrap-O-Matic Machinery Company, Ltd., and Precise Packaging, and located at 1105 West St. George Avenue, Linden, New Jersey, has been used, and is being used by Larry Dalia and others as yet unknown in connection with the commission of the above-described offenses.</p>
<p>"WHEREFORE, it is hereby ordered that:</p>
<p>"Special Agents of the Federal Bureau of Investigation, United States Department of Justice, are authorized . . . to:</p>
<p>.....</p>
<p>"(b) Intercept oral communications of Larry Dalia, and others as yet unknown, concerning the above-described offenses at the business office of Larry Dalia, consisting of an enclosed room, approximately fifteen (15) by eighteen (18) feet in dimension, and situated in the northwesterly corner of a one-story building housing Wrap-O-Matic Machinery Company, Ltd., and Precise Packaging, and located at 1105 West St. George Avenue, Linden, New Jersey.</p>
<p>"(c) Such interceptions shall not automatically terminate when the type of communication described above in paragraphs (a) and (b) have first been obtained, but shall continue until communications are intercepted which reveal the manner in which Larry Dalia and others as yet unknown participate in theft from interstate shipments; sale or receipt of stolen goods; and interference with commerce by threats or violence; and which reveal the identities of his confederates, their places of operation, and the nature of the conspiracy involved therein, or for a period of twenty (20) days from the date of this Order, whichever is earlier.</p>
<p>.....</p>
<p>"PROVIDING THAT, this authorization to intercept oral and wire communications shall be executed as soon as practicable after signing of this Order and shall be conducted in such a way as to minimize the interception of communications not otherwise subject to interception under Chapter 119 of Title 18 of the United States Code, and must terminate upon attainment of the authorized objective, [or] in any event, at the end of twenty (20) days from the date of this Order.</p>
<p>"PROVIDING ALSO, that Special Attorney James M. Deichert shall provide the Court with a report on the fifth, tenth, and fifteenth day following the date of this Order showing what progress has been made toward achievement of the authorized objective and the need for continued interception."</p>
<p>[5]  Count one charged petitioner and others with conspiring to transport, receive, and possess stolen goods in violation of <span class="citation no-link">18 U. S. C. §§ 2</span>, 2314, 2115, and 659. Count two charged petitioner and others with conspiring to obstruct interstate commerce in violation of <span class="citation no-link">18 U. S. C. § 1951</span> (b) (1). Count three charged that petitioner had transported stolen goods; count four charged that he had received stolen goods; and count five charged petitioner with possession of stolen goods.</p>
<p>[6]  Petitioner was convicted of receiving stolen goods and conspiring to transport, receive, and possess stolen goods. See n. 5, <i>supra.</i></p>
<p>[7]  One authority has said that the constitutional validity of covert entries to install bugs "is plainly the consequence of [the] reasoning" of <i>Katz</i> v. <i>United States</i><i>.</i> T. Taylor, Two Studies in Constitutional Interpretation 114 (1969).</p>
<p>[8]  Petitioner argues that, even if a covert entry would be constitutional in some cases, it was not in the present case, as there was no need for such entry. The District Court, however, specifically found that the "safest and most successful method of accomplishing the installation of the wiretapping device was through breaking and entering [the office]." <span class="citation" data-id="1595144"><a href="/opinion/1595144/united-states-v-dalia/#866" aria-description="Citation for case: United States v. Dalia">426 F. Supp. 862, 866</a></span> (1977). Moreover, in issuing the Title III order, the court found that "[n]ormal investigative procedures reasonably appear to be unlikely to succeed and are too dangerous to be used." App. 7a. And in his opinion denying petitioner's subsequent suppression motion, the same judge stated:
</p>
<p>"The affidavits which supported the application for the warrant in question indicated that resort to electronic surveillance, to overhear meetings at Dalia's office and conversations on Dalia's telephones, was required to identify the sources of Dalia's stolen goods, those working with him to transport and store stolen property, and the scope of the conspiracy. Oral evidence of this criminal enterprise was only available inside Dalia's business premises." <span class="citation" data-id="1595144"><a href="/opinion/1595144/united-states-v-dalia/#866" aria-description="Citation for case: United States v. Dalia">426 F. Supp., at 866</a></span>.</p>
<p>The District Court, therefore, concluded that the circumstances required the approach used by the officers, and nothing in the record brings this conclusion into question.</p>
<p>[9]  It is clear that Title III serves a substantial public interest. See n. 13, <i>infra.</i> Congress and this Court have recognized, however, that electronic surveillance can be a threat to the "cherished privacy of law-abiding citizens" unless it is subjected to the careful supervision prescribed by Title III. See <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#312" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 312</a></span> (1972).</p>
<p>[10]  Congress explicitly confirmed the breadth of the power it had conferred on courts acting under Title III when it amended the Act in 1970. <span class="citation no-link">Pub. L. 91-358, </span>Title II, § 211 (b), <span class="citation no-link">84 Stat. 654</span>. Section 2518 (4) now empowers a court authorizing electronic surveillance to "direct that a . . . landlord, custodian or other person shall furnish the applicant forthwith all information, facilities, and technical assistance necessary to accomplish the interception <i>unobtrusively</i> . . . ." (Emphasis added.) Thus, it appears that Congress anticipated that landlords and custodians may be enlisted to aid law enforcement officials covertly to enter and place the necessary equipment in private areas.</p>
<p>[11]  The only limitation Title III places on the manner in which these court orders are to be executed is in its requirements that no order extend beyond 30 days, and that every order must include provisions that it is to be executed as soon as practicable and in a manner that will minimize the interception of communications not within the purview of the order. See <span class="citation no-link">18 U. S. C. § 2518</span> (5).</p>
<p>[12]  Indeed, the nature of electronic surveillance involved in <i>Berger</i> v. <i><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">New York</a></span></i> was mentioned on the floor of the Senate, when Senator Long observed that under the New York law, police could "obtain judicial warrants authorizing them to hide bugs in the premises of criminal suspects." 114 Cong. Rec. 14708 (1968). To be sure, in his comments Senator Long did not explicitly suggest that Title III would authorize such covert entries. See <i>post,</i> at 272. His statement confirmed, however, what had been strongly indicated prior to the bill's consideration by the full Congress: Members of Congress simply saw no distinction between electronic surveillance which required covert entry and that which required covert tapping of one's telephone. The invasion of the privacy of conversation is the same in both situations.</p>
<p>[13]  Title <span class="citation no-link">18 U. S. C. § 2516</span> specifies that authorization for electronic surveillance may be sought only with respect to certain enumerated crimes. These include espionage, sabotage, treason, kidnaping, robbery, extortion, murder, various corrupt practices, and counterfeiting. According to the Senate Report concerning Title III, "[e]ach offense has been chosen either because it is intrinsically serious or because it is characteristic of the operations of organized crime." S. Rep. No. 1097, 90th Cong., 2d Sess., 97 (1968). The need for use of electronic surveillance against organized crime had been thoroughly considered and documented, shortly before Congress began considering Title III, by a special organized-crime Task Force of a Presidential Commission charged with considering crime in the United States. The President's Commission on Law Enforcement and Administration of Justice, Task Force Report: Organized Crime 91-104 (1967); see <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S., at 310</a></span> n. 9. A summary of the Task Force's conclusions appeared in the Commission's report, which was repeatedly referred to during consideration of Title III. See The President's Commission on Law Enforcement and Administration of Justice, The Challenge of Crime in a Free Society 200-203 (1967). In Congress, proponents of Title III, after hearing numerous witnesses testify concerning the importance of electronic surveillance in fighting organized crime, recommended the bill to their colleagues as "[l]egislation meeting the constitutional standards set out in [Supreme Court] decisions, and granting law enforcement officers the authority to tap telephone wires and install electronic surveillance devices in the investigation of major crimes." S. Rep. No. 1097, <i>supra,</i> at 75; see <i>id.,</i> at 74. Indeed, the Senate Report on Title III unequivocally stated that "[t]he major purpose of title III is to combat organized crime." <i>Id.,</i> at 70. The rapid developments in technology available to the criminal underworld make it all the more imperative that the Government not "deny to itself the prudent and lawful employment of those very techniques which are employed against the Government and its law-abiding citizens." <i>United States</i> v. <i>United States District Court, supra,</i> at 312.</p>
<p>[14]  Although he cites no authority, MR. JUSTICE STEVENS apparently believes that a practicable alternative to covert entry would be installation of bugging devices through subterfuge. See <i>post,</i> at 272. Nowhere in the legislative history of Title III is there any indication that Congress wished to limit its authorization to bugs installed through subterfuge. Moreover, it is difficult to perceive why one means of gaining entry would be less intrusive than another. See, <i>e. g., </i><i>United States</i> v. <i>Ford,</i> <span class="citation" data-id="1442699"><a href="/opinion/1442699/united-states-v-ford/" aria-description="Citation for case: United States v. Ford">414 F. Supp. 879</a></span> (DC 1976), aff'd, 180 U. S. App. D. C. 1, <span class="citation" data-id="344771"><a href="/opinion/344771/united-states-v-carroll-d-ford-united-states-of-america-v-wesley/" aria-description="Citation for case: United States v. Carroll D. Ford. United States of...">553 F. 2d 146</a></span> (1977) (bombscare ruse).</p>
<p>[15]  Those few available devices that intercept conversation from outside of a building in many cases are impractical, either because of cost, reliability, or the configuration of the area being monitored. See U. S. National Commission for Review of Federal and State Laws Relating to Wiretapping and Electronic Surveillance, Commission Studies 168-183 (1976); see, <i>e. g., </i><i>United States</i> v. <i>Ford,</i> <span class="citation" data-id="1442699"><a href="/opinion/1442699/united-states-v-ford/#881" aria-description="Citation for case: United States v. Ford">414 F. Supp., at 881</a></span>.</p>
<p>[16]  As we have concluded that Title III authorizes courts to approve covert entries to install electronic surveillance equipment, we do not consider whether such authority also is conferred by other federal enactments, such as Fed. Rule Crim. Proc. 41 or the All Writs Act, <span class="citation no-link">28 U. S. C. § 1651</span>.</p>
<p>[17]  There is no requirement in Title III that explicit authorization of covert entries be set forth in the court's order. The statutory requirement that the surveillance "should remain under the control and supervision of the authorizing court" <span class="citation no-link">82 Stat. 211</span>, § 801 (d), merely emphasizes that courts acting under <span class="citation no-link">18 U. S. C. § 2518</span> should utilize their power under § 2518 (6) to require periodic progress reports after the installation of the wiretap or bug. If there is a requirement of explicit judicial authorization for covert entry, therefore, it must come from the Fourth Amendment alone.</p>
<p>[18]  Because of the strict requirements of Title III, all of the indicia of a warrant necessarily are present whenever an order under Title III is issued. Accord, <i>United States</i> v. <i>Scafidi,</i> <span class="citation" data-id="8903769"><a href="/opinion/8915597/united-states-v-scafidi/#644" aria-description="Citation for case: United States v. Scafidi">564 F. 2d, at 644</a></span> (Gurfein, J., concurring). Indeed, it was Congress' express design to create under Title III a mechanism by which search warrants valid under the Fourth Amendment would be issued for electronic surveillance. See S. Rep. No. 1097, <i>supra</i> n. 13, at 105; Controlling Crime Through More Effective Law Enforcement: Hearings on S. 300, etc., before the Subcommittee on Criminal Laws and Procedures of the Senate Committee on the Judiciary, 90th Cong., 1st Sess., 176, 570, 919 (1967); Hearings on H. R. 5037, etc., before Subcommittee No. 5 of the House Committee on the Judiciary, 90th Cong., 1st Sess., 917, 934 (1967). No less would be required for the court authorization of electronic surveillance under Title III to be constitutional, as electronic surveillance undeniably is a Fourth Amendment intrusion requiring a warrant. See, <i>e. g., </i><i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 352-353, 356-357</a></span> (1967). And we have explicitly recognized the necessity of a warrant in cases of electronic surveillance. See <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#316" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S., at 316-320</a></span>.</p>
<p>[19]  For example, courts have upheld the use of forceful breaking and entering where necessary to effect a warranted search, even though the warrant gave no indication that force had been contemplated. See, <i>e. g., </i><i>United States</i> v. <i>Gervato,</i> <span class="citation" data-id="308678"><a href="/opinion/308678/united-states-v-frank-gervato/#41" aria-description="Citation for case: United States v. Frank Gervato">474 F. 2d 40, 41</a></span> (CA3), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/864/">414 U. S. 864</a></span> (1973). To be sure, often it is impossible to anticipate when these actions will be necessary. See Note, Covert Entry in Electronic Surveillance: The Fourth Amendment Requirements, 47 Ford. L. Rev. 203, 214 (1978). Nothing in the decisions of this Court, however, indicates that officers requesting a warrant would be constitutionally required to set forth the anticipated means for execution even in those cases where they know beforehand that unannounced or forced entry likely will be necessary. See 2 W. LaFave, Search and Seizure 140 (1978).</p>
<p>[20]  The District Court found that covert entry in the present case was reasonable. The officers entered petitioner's office only twice: once to install the bug and once to remove it. There is no indication that their intrusion went beyond what was necessary to install and remove the equipment. See n. 8, <i>supra.</i></p>
<p>[21]  In the present case, the District Court specifically noted that its order implicitly had authorized covert entry. See <i>supra,</i> at 246. Thus, contrary to the suggestion of the dissent, see <i>post,</i> at 270 n. 20, there is no question in this case "of the <i>Executive's</i> authority to break and enter at will <i>without</i> any judicial authorization."</p>
<p>[22]  Although explicit authorization of the entry is not constitutionally required, we do agree with the Court of Appeals that the "preferable approach" would be for Government agents in the future to make explicit to the authorizing court their expectation that some form of surreptitious entry will be required to carry out the surveillance. Indeed, the Solicitor General has informed us that the Department of Justice has adopted a policy requiring its officers "[to] include [in applications for Title III orders] a request that the order providing for the interception specifically authorize surreptitious entry for the purpose of installing and removing any electronic interception devices to be utilized in accomplishing the oral interception." See Brief for United States 56.</p>
<p>[*]  The Court's reliance upon <i>United States</i> v. <i>Cravero,</i> <span class="citation" data-id="8900306"><a href="/opinion/8912462/united-states-v-cravero/#421" aria-description="Citation for case: United States v. Cravero">545 F. 2d 406, 421</a></span> (CA5 1976) (on petition for rehearing), for the opposite proposition is misplaced. In <i><span class="citation" data-id="8900306"><a href="/opinion/8912462/united-states-v-cravero/" aria-description="Citation for case: United States v. Cravero">Cravero</a></span>,</i> police could not have anticipated the need to arrest the suspect at his home at the time the arrest warrant was issued. It would have been unreasonable, therefore, to require the warrant to specify a home arrest. Here, by contrast, the covert entry was easily foreseeable. There is no reason why the federal agents who secured the warrant could not have advised the judge who issued the warrant that they contemplated covert entry. Indeed, the current Justice Department practice of securing specific prior authorization for covert entries demonstrates the practicability of a constitutional prior-authorization requirement.
</p>
<p><i>United States</i> v. <i>Gervato,</i> <span class="citation" data-id="308678"><a href="/opinion/308678/united-states-v-frank-gervato/#41" aria-description="Citation for case: United States v. Frank Gervato">474 F. 2d 40, 41</a></span> (CA3 1973), is distinguishable for the same reason and also because <i><span class="citation" data-id="308678"><a href="/opinion/308678/united-states-v-frank-gervato/" aria-description="Citation for case: United States v. Frank Gervato">Gervato</a></span></i> involved a mere mode of warrant execution (forcible entry) rather than an invasion of two separate expectations of privacy.</p>
<p>[1]  See <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297</a></span>. The Fourth Amendment provides:
</p>
<p>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</p>
<p>[2]  N. J. Stat. Ann. §§ 2A:94-1, 2A:94-3 (West 1969).</p>
<p>[3]  T. Taylor, Two Studies in Constitutional Interpretation 110 (1969).</p>
<p>[4]  Cf. <i>G. M. Leasing Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#353" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 353</a></span>; <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span>; <i>Colonnade Catering Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#76" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72, 76</a></span>.</p>
<p>[5]  "Beginning with the Act of July 31, 1789, <span class="citation no-link">1 Stat. 29</span>, 43, and concluding with the Omnibus Crime Control and Safe Streets Act of 1968, <span class="citation no-link">82 Stat. 197</span>, 219, 238, Congress has enacted a series of over 35 different statutes granting federal judges the power to issue search warrants of one form or another. These statutes have one characteristic in common: they are specific in their grants of authority and in their inclusion of limitations on either the places to be searched, the objects of the search, or the requirements for the issuance of a warrant." <i>United States</i> v. <i>New York Telephone Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/#179" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S. 159, 179-180</a></span> (STEVENS, J., dissenting in part) (footnote omitted).
</p>
<p>Mr. Justice Frankfurter gathered the pre-1945 statutes in his dissenting opinion in <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/#616" aria-description="Citation for case: Davis v. United States">328 U. S. 582, 616-623</a></span>. He commented that "[w]hat is significant about this legislation is the recognition by Congress of the necessity for specific Congressional authorization even for the search of vessels and other moving vehicles and the seizures of goods technically contraband." <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/#616" aria-description="Citation for case: Davis v. United States"><i>Id.,</i> at 616</a></span>, n.</p>
<p>[6]  I realize that since <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, the Court has applied the same Fourth Amendment principles to state and federal law enforcement officers alike. Nonetheless, I purposely limit my discussion here to the federal context. For purposes of discussing the necessity of statutory authority, it seems useful to me to treat the Fourth Amendment concept of reasonableness as flexible enough to recognize differences between state and federal courts and police forces. Thus, because the power of the Federal Government to combat crime, like the jurisdiction of its courts, is more limited than the comparable power and jurisdiction inhering in the States, it is logical in the federal context to assume that governmental authority is lacking unless expressly mandated by legislation. See, <i>e. g., </i><i>Palmore</i> v. <i>United States,</i> <span class="citation" data-id="9425255"><a href="/opinion/108767/palmore-v-united-states/#396" aria-description="Citation for case: Palmore v. United States">411 U. S. 389, 396</a></span>; <i>Cheng Fan Kwok</i> v. <i>INS,</i> <span class="citation" data-id="9423777"><a href="/opinion/107735/cheng-fan-kwok-v-immigration-naturalization-service/" aria-description="Citation for case: Cheng Fan Kwok v. Immigration &amp; Naturalization Service">392 U. S. 206</a></span>; <i>United States</i> v. <i>Five Gambling Devices,</i> <span class="citation" data-id="9421009"><a href="/opinion/105172/united-states-v-five-gambling-devices/" aria-description="Citation for case: United States v. Five Gambling Devices">346 U. S. 441</a></span>.</p>
<p>[7]  See <i>McCulloch</i> v. <i>Sociedad Nacional de Marineros de Honduras,</i> <span class="citation" data-id="9422521"><a href="/opinion/106525/mcculloch-v-sociedad-nacional-de-marineros-de-honduras/" aria-description="Citation for case: McCulloch v. Sociedad Nacional De Marineros De Honduras">372 U. S. 10</a></span>; <i>Machinists</i> v. <i>Street,</i> <span class="citation" data-id="9422287"><a href="/opinion/106288/international-assn-of-machinists-v-street/" aria-description="Citation for case: International Ass&#x27;n of MacHinists v. Street">367 U. S. 740</a></span>; <i>Hannah</i> v. <i>Larche,</i> <span class="citation" data-id="9422021"><a href="/opinion/106078/hannah-v-larche/#430" aria-description="Citation for case: Hannah v. Larche">363 U. S. 420, 430</a></span>; <i>Murray</i> v. <i>The Charming Betsy,</i> <span class="citation" data-id="84778"><a href="/opinion/84778/murray-v-schooner-charming-betsy/" aria-description="Citation for case: Murray v. Schooner Charming Betsy">2 Cranch 64</a></span>.</p>
<p>[8]  It found authority for those searches in the Postal Service's recent reinterpretation of an awkwardly drawn 1866 statute that authorized certain border searches of "vessels" but that could not reasonably be read to authorize either the mail openings themselves or the regulation allowing them. Moreover, its adoption of that interpretation left it no choice but to resolve a troublesome constitutional question without any considered guidance from Congress. See <span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#625" aria-description="Citation for case: United States v. Ramsey">431 U. S., at 625-632</a></span> (STEVENS, J., dissenting).</p>
<p>[9]  See <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/#178" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S., at 178-190</a></span> (STEVENS, J., dissenting in part).</p>
<p>[10]  Although this case involves an office, the invasion of a home would raise precisely the same statutory issue.</p>
<p>[11]  "Congress drafted [Title III] with exacting precision. As its principal sponsor, Senator McClellan, put it:
</p>
<p>" `[A] bill as controversial as this . . . requires close attention to the dotting of every "i" and the crossing of every "t" . . . .' [114 Cong. Rec. 14751 (1968).]</p>
<p>"Under these circumstances, the exact words of the statute provide the surest guide to determining Congress' intent, and we would do well to confine ourselves to that area." <i>United States</i> v. <i>Donovan,</i> <span class="citation" data-id="9426645"><a href="/opinion/109584/united-states-v-donovan/#441" aria-description="Citation for case: United States v. Donovan">429 U. S. 413, 441</a></span> (BURGER, C. J., concurring in part and dissenting in part).</p>
<p>[12]  See <i>ante,</i> at 249-250; nn. 13-18, <i>infra,</i> and text accompanying.</p>
<p>[13]  As Judge Merritt, writing for the Sixth Circuit, cogently observed:
</p>
<p>"It simply does not make sense to imply Congressional authority for official break-ins when not a single line or word of the statute even mentions the possibility, much less limits or defines the scope of the power or describes the circumstances under which such conduct, normally unlawful, may take place. As the dissents of Holmes and Brandeis in <i>Olmstead</i> [v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span>] suggest, this is a serious, if not a `dirty,' business; and we do not believe we should imply the power to break in under the statute, as the government argues, when Congress has not confronted and debated the issue and expressed such an intention clearly.</p>
<p>.....</p>
<p>"In some circumstances, the installation of an electronic bug may not be possible without a forcible breaking and entering of the suspect's premises, but that does not imply that the power to break and enter is subsumed in the warrant to seize the words. The breaking and entering aggravates the search, and it intrudes upon property and privacy interests not weighed in the statutory scheme, interests which have independent social value unrelated to confidential speech. We are not inclined to give the government the right by implication to intrude upon these interests by conducting official break-ins, especially when the purpose is secretly to monitor and record private conversations, a dangerous power otherwise carefully limited and defined by statute." <i>United States</i> v. <i>Finazzo,</i> <span class="citation" data-id="9465129"><a href="/opinion/359662/united-states-v-salvatore-finazzo-dominic-j-licavoli/#841" aria-description="Citation for case: United States v. Salvatore Finazzo, Dominic J. Licavoli">583 F. 2d 837, 841-842</a></span> (CA6 1978). See also <i>United States</i> v. <i>Santora,</i> <span class="citation" data-id="359575"><a href="/opinion/359575/united-states-v-ronald-santora-earl-rardin-maurice-eugene-lickteig/#456" aria-description="Citation for case: United States v. Ronald Santora, Earl Rardin, Maurice...">583 F. 2d 453, 456-466</a></span> (CA9 1978).</p>
<p>[14]  <span class="citation no-link">18 U. S. C. § 2516</span> (1).</p>
<p>[15]  <span class="citation no-link">18 U. S. C. §§ 2516</span> (1) (a)-(g).</p>
<p>[16]  "Each application for an order authorizing or approving the interception of a wire or oral communication shall be made in writing upon oath or affirmation to a judge of competent jurisdiction and shall state the applicant's authority to make such application. Each application shall include the following information:
</p>
<p>"(a) the identity of the investigative or law enforcement officer making the application, and the officer authorizing the application;</p>
<p>"(b) a full and complete statement of the facts and circumstances relied upon by the applicant, to justify his belief that an order should be issued, including (i) details as to the particular offense that has been, is being, or is about to be committed, (ii) a particular description of the nature and location of the facilities from which or the place where the communication is to be intercepted, (iii) a particular description of the type of communications sought to be intercepted, (iv) the identity of the person, if known, committing the offense and whose communications are to be intercepted;</p>
<p>"(c) a full and complete statement as to whether or not other investigative procedures have been tried and failed or why they reasonably appear to be unlikely to succeed if tried or to be too dangerous;</p>
<p>"(d) a statement of the period of time for which the interception is required to be maintained. If the nature of the investigation is such that the authorization for interception should not automatically terminate when the described type of communication has been first obtained, a particular description of facts establishing probable cause to believe that additional communications of the same type will occur thereafter;</p>
<p>"(e) a full and complete statement of the facts concerning all previous applications known to the individual authorizing and making the application, made to any judge for authorization to intercept, or for approval of interceptions of, wire or oral communications involving any of the same persons, facilities or places specified in the application, and the action taken by the judge on each such application; and</p>
<p>"(f) where the application is for the extension of an order, a statement setting forth the results thus far obtained from the interception, or a reasonable explanation of the failure to obtain such results." <span class="citation no-link">18 U. S. C. § 2518</span> (1).</p>
<p>[17]  "(3) Upon such application the judge may enter an ex parte order, as requested or as modified, authorizing or approving interception of wire or oral communications within the territorial jurisdiction of the court in which the judge is sitting, if the judge determines on the basis of the facts submitted by the applicant that
</p>
<p>"(a) there is probable cause for belief that an individual is committing, has committed, or is about to commit a particular offense enumerated in section 2516 of this chapter;</p>
<p>"(b) there is probable cause for belief that particular communications concerning that offense will be obtained through such interception;</p>
<p>"(c) normal investigative procedures have been tried and have failed or reasonably appear to be unlikely to succeed if tried or to be too dangerous;</p>
<p>"(d) there is probable cause for belief that the facilities from which, or the place where, the wire or oral communications are to be intercepted are being used, or are about to be used, in connection with the commission of such offense, or are leased to, listed in the name of, or commonly used by such person.</p>
<p>"(4) Each order authorizing or approving the interception of any wire or oral communication shall specify</p>
<p>"(a) the identity of the person, if known, whose communications are to be intercepted;</p>
<p>"(b) the nature and location of the communications facilities as to which, or the place where, authority to intercept is granted;</p>
<p>"(c) a particular description of the type of communication sought to be intercepted, and a statement of the particular offense to which it relates;</p>
<p>"(d) the identity of the agency authorized to intercept the communications, and of the person authorizing the application; and</p>
<p>"(e) the period of time during which such interception is authorized, including a statement as to whether or not the interception shall automatically terminate when the described communication has been first obtained. . . ." <span class="citation no-link">18 U. S. C. §§ 2518</span> (3), (4).</p>
<p>[18]  "No order entered under this section may authorize or approve the interception of any wire or oral communication for any period longer than is necessary to achieve the objective of the authorization, nor in any event longer than thirty days. Extensions of an order may be granted, but only upon application for an extension made in accordance with subsection (1) of this section and the court making the findings required by subsection (3) of this section. The period of extension shall be no longer than the authorizing judge deems necessary to achieve the purposes for which it was granted and in no event for longer than thirty days. Every order and extension thereof shall contain a provision that the authorization to intercept shall be executed as soon as practicable, shall be conducted in such a way as to minimize the interception of communications not otherwise subject to interception under this chapter, and must terminate upon attainment of the authorized objective, or in any event in thirty days." <span class="citation no-link">18 U. S. C. § 2518</span> (5).
</p>
<p>The statute also details procedures for the storage and protective custody of the resulting tapes, <span class="citation no-link">18 U. S. C. §§ 2518</span> (8) (a)-(c), for authorized disclosures and uses of the tapes both in and out of court, <span class="citation no-link">18 U. S. C. §§ 2517</span>, 2518 (9), and for after-the-fact notice to persons whose conversations were overheard. <span class="citation no-link">18 U. S. C. § 2518</span> (8) (d).</p>
<p>[19]  The following provision was added to Title III in 1970:
</p>
<p>"An order authorizing the interception of a wire or oral communication shall, upon request of the applicant, direct that a communication common carrier, landlord, custodian or other person shall furnish the applicant forthwith all information, facilities, and technical assistance necessary to accomplish the interception unobtrusively and with a minimum of interference with the services that such carrier, landlord, custodian, or person is according the person whose communications are to be intercepted. Any communication common carrier, landlord, custodian or other person furnishing such facilities or technical assistance shall be compensated therefor by the applicant at the prevailing rates." <span class="citation no-link">18 U. S. C. § 2518</span> (4).</p>
<p>[20]  The Court analyzes this problem as simply one of <i>Judicial</i> authority under the statute. <i>Ante,</i> at 250, and n. 10. Even if I could agree that Title III afforded judges "broad" and unconfined authority with respect to break-ins, I would still be left with the problem, never mentioned by the Court, of the <i>Executive's</i> authority to break and enter at will <i>without</i> any judicial authorization.
</p>
<p>Indeed, I am not at all certain that the Court puts any confines on either Judicial or Executive authority in this area, despite the lip service it pays to "constitutional limitations." For, having stated that "breaking and entering" in execution of a search warrant is constitutionally permissible "where such entry is the <i>only</i> means by which the warrant effectively may be executed," <i>ante,</i> at 247 (emphasis added), the Court then equates a surveillance order with a search warrant, but see Taylor, <i>supra</i> n. 3, at 84-85, and allows a break-in under the former upon a showing merely that the break-in was "the safest and most successful," rather than the "only," method of installing the device. <span class="citation" data-id="1595144"><a href="/opinion/1595144/united-states-v-dalia/#866" aria-description="Citation for case: United States v. Dalia">426 F. Supp. 862, 866</a></span>.</p>
<p>[21]  A Congress that was careful to limit the temporal extent of electronic surveillance and the opportunity for it to infringe on protected (<i>i. e.,</i> noncriminal) conversations, and one so quick to amend the statute to provide for "unobtrusive" entry through the aid of private persons (<i>i. e.,</i> "custodians" and "landlords") who already have a degree of access to the property, surely cannot have condoned unlimited and unauthorized breaking and entering by police officers with the aid of nothing but a burglar's tools.</p>
<p>[22]  In full, the paragraph excerpted by the Court is as follows:
</p>
<p>"In Berger against the State of New York, decided on June 12, 1967, the majority of the Court, speaking through Mr. Justice Clark, threw out the New York State court-approved eavesdropping statute, declaring it to be unconstitutional. The New York statute permitted the police to obtain judicial warrants authorizing them to hide bugs in the premises of criminal suspects. The Court's majority opinion outlawed this bugging statute because, it said, the procedures did not contain specific safeguards against violations of the fourth amendment, which limited police searches." 114 Cong. Rec. 14708 (1968) (Sen. Long of Missouri).</p>
<p>[23]  See also Anti-Crime Programs: Hearings on H. R. 5037, etc., before Subcommittee No. 5 of the House Committee on the Judiciary, 90th Cong., 1st Sess., 1031 (1967), cited <i>ante,</i> at 251.</p>
<p>[24]  "[Title III] sets forth in the most elaborate and precise detail the safeguards surrounding the application to a court of competent jurisdiction for authority to make a wiretap. I am satisfied that it is fully designed to guard against any unwarranted invasion of the precious right of privacy." 114 Cong. Rec. 16296 (1968) (Rep. MacGregor). See also <i>id.,</i> at 14763 (Sen. Percy); <i>id.,</i> at 16296 (Rep. Boland); S. Rep. No. 1097, 90th Cong., 2d Sess., 66 (1968).
</p>
<p>On at least two occasions the Court has commented on the circumspection with which Title III was drafted:</p>
<p>"[Title III] sets forth the detailed and particularized application necessary to obtain such an order as well as the <i>carefully circumscribed conditions for its use.</i> The Act represents a comprehensive attempt by Congress to promote more effective control of crime while protecting the privacy of individual thought and expression." <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#302" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S., at 302</a></span> (emphasis added). See also <i>Gelbard</i> v. <i>United States,</i> <span class="citation" data-id="9424980"><a href="/opinion/108596/gelbard-v-united-states/#48" aria-description="Citation for case: Gelbard v. United States">408 U. S. 41, 48</a></span>. See also n. 8, <i>supra.</i></p>
<p>[25]  Had Congress expressly considered the issue, I am confident that it would not have granted the Executive the broad authority to break and enter that is conferred by the Court in today's decision. Illustrative of its probable reaction to such investigative techniques are the responses of some Members to the officially sanctioned break-in committed against the office of Daniel Ellsberg's psychiatrist, and to the possibility of official participation in the Watergate break-in <i>E. g.,</i> 119 Cong. Rec. 14607-14608 (1973) (Sen. Edwards); <i>id.,</i> at 15332 (Rep. Sarasin).</p>
<p>[26]  The dimensions of the constitutional protection of privacy were certainly not underestimated by the supporters of Title III. Senator Lausche, for example, had this to say about the intent of the Framers of the Fourth Amendment:
</p>
<p>"[T]hey also knew that the innocent individual would be protected in his home; that no one shall enter. Even though it is a hovel, to him it is a palace. So they wrote into the Constitution, regardless of how poor one's home may be, that it shall not be entered by the government without the law-enforcement official having first obtained a warrant for search and seizure issued on the basis of evidence establishing probable cause." 114 Cong. Rec. 14729 (1968).</p>
<p>[27]  <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span>; <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span>. See also <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span>; <i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">347 U. S. 128</a></span>.</p>
<p>[28]  See S. Rep. No. 1097, <i>supra,</i> at 66, 75, 101.</p>
<p>[29]  <i>E. g., </i><i>On Lee</i> v. <i>United States,</i> <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/" aria-description="Citation for case: On Lee v. United States">343 U. S. 747</a></span>; <i>Goldman</i> v. <i>United States,</i> <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">316 U. S. 129</a></span>; <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span>.</p>
<p>[30]  <i>E. g., </i><i>Silverman</i> v. <i>United States, supra</i><i>; </i><i>Irvine</i> v. <i>California, supra</i><i>.</i></p>
<p>[31]  Mr. Justice Jackson described the entry as follows:
</p>
<p>"On December 1, 1951, while Irvine and his wife were absent from their home, an officer arranged to have a locksmith go there and make a door key. Two days later, again in the absence of occupants, officers and a technician made entry into the home by the use of this key and installed a concealed microphone in the hall. A hole was bored in the roof of the house and wires were strung to transmit to a neighboring garage whatever sounds the microphone might pick up. Officers were posted in the garage to listen. On December 8, police again made surreptitious entry and moved the microphone, this time hiding it in the bedroom. Twenty days later, they again entered and placed the microphone in a closet, where the device remained until its purpose of enabling the officers to overhear incriminating statements was accomplished." <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#130" aria-description="Citation for case: Irvine v. California">347 U. S., at 130-131</a></span>.</p>
<p>[32]  <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#145" aria-description="Citation for case: Irvine v. California"><i>Id.,</i> at 145</a></span> (Frankfurter, J., dissenting, joined by Burton, J.); <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#150" aria-description="Citation for case: Irvine v. California"><i>id.,</i> at 150</a></span> (Douglas, J., dissenting).</p>
<p>[33]  The Court argues that Congress' goals in enacting the statute would be frustrated if Title III were not read to include the authority exercised by the Government in this case. <i>Ante,</i> at 252-254. Of course, if Congress intended to sanction "even the most reprehensible means for securing a conviction," <i>Irvine,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#146" aria-description="Citation for case: Irvine v. California">347 U. S., at 146</a></span> (Frankfurter, J., dissenting), then withholding some of those means would indeed frustrate the legislative purpose. But there is no reason to impute such an intent to Congress or to ignore its conscientious attention to the importance of safeguarding the rights of individual privacy. See 114 Cong. Rec. 14469-14470 (1968) (Sen. McClellan); see <i>supra,</i> at 272-273, 276.
</p>
<p>Congress quite clearly expected exterior <i>wiretaps</i> to provide the most effective means of electronic surveillance authorized by Title III. The unavailability of certain interior <i>"bugs"</i><i>i. e.,</i> those implanted by means of forcible trespasscan hardly be seen as frustrating the entire law enforcement scheme. <i>E. g.,</i> S. Rep. No. 1097, supra n. 24, at 72; 114 Cong. Rec. 12988 (1968) (Sen. Tydings); <i>id.,</i> at 13206 (Sen. Scott); <i>id.,</i> at 14481 (Sen. McClellan); <i>id.,</i> at 14714 (Sen. Murphy).</p>
<p>Congress' prediction proved correct:</p>
<p>"Telephone taps apparently account for most instances of electronic surveillance, and this can be accomplished in most circumstances by placing a tap on the line outside the premises of the suspect. According to the final report of the National Commission for Review of Federal and State Laws Relating to Wiretapping and Electronic Surveillance, only 26 out of some 1,220 electronic surveillance orders executed between 1968 and 1973 involved a trespassory intrusion. <i>National Wiretap Commission, Electronic Surveillance</i> 15 (1967) . . . ." <i>United States</i> v. <i>Finazzo,</i> <span class="citation" data-id="9465129"><a href="/opinion/359662/united-states-v-salvatore-finazzo-dominic-j-licavoli/" aria-description="Citation for case: United States v. Salvatore Finazzo, Dominic J. Licavoli">583 F. 2d, at 841</a></span> n. 13.</p>
<p>[34] 

[...TRUNCATED 1376 of 121376 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
