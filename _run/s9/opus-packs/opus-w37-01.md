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

## GROUP: content/cases/Georgia v. Randolph.md  (`case`, 5 assertions)

### content_page

```
---
title: "Georgia v. Randolph"
type: case
citation: "547 U.S. 103 (2006)"
parallel_cite: "126 S. Ct. 1515; 164 L. Ed. 2d 208"
neutral_cite: 2006 U.S. LEXIS 2498
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2006
date_decided: 2006-03-22
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2006-03-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Georgia v. Randolph
  varies_by_point: false
  scope_note: "Confined to a physically present objector by Fernandez v. California (2014)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145669/georgia-v-randolph/"
  cluster_id: 145669
  opinion_id: 145669
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Key — Anchor"
related: ["[[Fernandez v. California]]", "[[Illinois v. Rodriguez]]", "[[United States v. Matlock]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent", "co-occupant", "third-party-consent", "present-objector"]
holding: "A PHYSICALLY PRESENT co-occupant's express refusal to consent prevails over another occupant's consent, rendering the warrantless search…"
lake:
  record_id: Georgia v. Randolph
  status: verified
  projected_at: 2026-07-06
---

# Georgia v. Randolph

*547 U.S. 103 (2006)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Scott Randolph's estranged wife told police that he used cocaine and that there was drug evidence in their home. When officers asked Randolph for consent to search, he expressly refused; his wife, present at the scene, then consented and led the officers to the evidence. Randolph moved to suppress, arguing that his present, express refusal made the search unreasonable as to him.

## Issue
Whether one occupant's consent to a warrantless search of a shared home is valid against a co-occupant who is physically present and expressly refuses consent.

## Rule
No. A physically present co-occupant's express refusal defeats another occupant's consent. "We therefore hold that a warrantless search of a shared dwelling for evidence over the express refusal of consent by a physically present resident cannot be justified as reasonable as to him on the basis of consent given to the police by another resident." — 547 U.S. at 120. ^pin-120

## Application
Randolph stood at the door and expressly told the officers they could not search, and only then did his wife consent. Because Randolph was physically present and expressly refused, his co-tenant's consent could not make the search reasonable as to him, and the evidence found in the home had to be suppressed.

## Conclusion
The warrantless search was unreasonable as to the present, objecting co-occupant; the suppression was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- **Confined to a physically present objector** by [[Fernandez v. California]]: once the objecting occupant is lawfully removed (e.g., by arrest), the remaining occupant's consent again controls. *Randolph*'s core present-objector rule is otherwise undisturbed.

## Appears on
- [[Consent Searches]] — *Key — Anchor*

## Sources
- *Georgia v. Randolph*, 547 U.S. 103 (2006) — https://www.courtlistener.com/opinion/145669/georgia-v-randolph/ — pinpoint: 120.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0cfec3574486aeb6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "547 U.S. 103 (2006)", "court": "U.S. Supreme Court", "neutral_cite": "2006 U.S. LEXIS 2498", "official_citation_present": true, "parallel_cite": "126 S. Ct. 1515; 164 L. Ed. 2d 208", "title": "Georgia v. Randolph", "year": "2006"}}
{"assertion_id": "359628d21ccb5613", "dimension": "support", "kind": "home_role", "locator": {"home": "Consent Searches"}, "payload": {"home": "Consent Searches", "role": "Key — Anchor", "title": "Georgia v. Randolph"}}
{"assertion_id": "767d4147978bf473", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A PHYSICALLY PRESENT co-occupant's express refusal to consent prevails over another occupant's consent, rendering the warrantless search…", "title": "Georgia v. Randolph"}}
{"assertion_id": "60805f12658de88f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Georgia v. Randolph"}}
{"assertion_id": "8a132e083d647528", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2006-03-22", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Georgia v. Randolph", "field_i_validity": "good_law", "scope_note": "Confined to a physically present objector by Fernandez v. California (2014).", "title": "Georgia v. Randolph", "varies_by_point": "false"}}
```

### lake record — Georgia v. Randolph

```json
{
  "schema_version": "s2.v1",
  "record_id": "Georgia v. Randolph",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Georgia v. Randolph",
    "case_name_short": "Randolph",
    "case_name_full": "Georgia v. Randolph",
    "input_case_name": "Georgia v. Randolph",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2006-03-22",
    "year": 2006,
    "docket": null,
    "cluster_id": 145669,
    "lead_opinion_id": 145669,
    "sibling_ids": [
      145669,
      9434962,
      9434963,
      9434964,
      9434965,
      9434966,
      9434967
    ],
    "absolute_url": "/opinion/145669/georgia-v-randolph/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "547 U.S. 103",
      "volume": "547",
      "reporter": "U.S.",
      "page": "103",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "126 S. Ct. 1515",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "1515",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "164 L. Ed. 2d 208",
        "volume": "164",
        "reporter": "L. Ed. 2d",
        "page": "208",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2006 U.S. LEXIS 2498",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "2498",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "547 U.S. 103",
        "volume": "547",
        "reporter": "U.S.",
        "page": "103",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "126 S. Ct. 1515",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "1515",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "164 L. Ed. 2d 208",
        "volume": "164",
        "reporter": "L. Ed. 2d",
        "page": "208",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2006 U.S. LEXIS 2498",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "2498",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "547 U.S. 103",
    "official_selection": {
      "court_class": "scotus",
      "selected": "547 U.S. 103",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-120",
      "page": null,
      "quote": "--- # Georgia v. Randolph *547 U.S. 103 (2006)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Scott Randolph's estranged wife told police that he used cocaine and that there was drug evidence in their home. When officers asked Randolph for consent to search, he expressly refused; his wife, present at the scene, then consented and led the officers to the evidence. Randolph moved to suppress, arguing that his present, express refusal made the search unreasonable as to him. ## Issue Whether one occupant's consent to a warrantless search of a shared home is valid against a co-occupant who is physically present and expressly refuses consent. ## Rule No. A physically present co-occupant's express refusal defeats another occupant's consent.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2006-03-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Georgia v. Randolph",
    "varies_by_point": false,
    "scope_note": "Confined to a physically present objector by Fernandez v. California (2014).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. White",
          "cluster_id": 4396241,
          "cite": [
            "799 S.E.2d 494",
            "293 Va. 411",
            "2017 WL 2376924",
            "2017 Va. LEXIS 78"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Glenda Smith v. City of Wyoming",
          "cluster_id": 3194781,
          "cite": [
            "821 F.3d 697",
            "2016 FED App. 0094P",
            "2016 U.S. App. LEXIS 6833",
            "2016 WL 1533998"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
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
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Timmie Bradley v. State of Indiana",
          "cluster_id": 2950910,
          "cite": [
            "44 N.E.3d 7",
            "2015 Ind. App. LEXIS 631",
            "2015 WL 5438394"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4288590,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
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
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4287047,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4286131,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States of America v. Frederick Drane",
          "cluster_id": 10697016,
          "cite": [
            "2014 DNH 150"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fadul",
          "cluster_id": 7306139,
          "cite": [
            "16 F. Supp. 3d 270",
            "2014 WL 1584044"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "MacDonald v. Town of Eastham",
          "cluster_id": 2656464,
          "cite": [
            "745 F.3d 8",
            "2014 WL 944707",
            "2014 U.S. App. LEXIS 4618"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Adams",
          "cluster_id": 2648986,
          "cite": [
            "740 F.3d 40",
            "2014 U.S. App. LEXIS 631",
            "113 A.F.T.R.2d (RIA) 522",
            "2014 WL 112937"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Omar Arreguin",
          "cluster_id": 2643845,
          "cite": [
            "735 F.3d 1168",
            "2013 U.S. App. LEXIS 23506"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
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
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
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
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
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
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
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
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ledesma",
          "cluster_id": 2599941,
          "cite": [
            "140 P.3d 657",
            "47 Cal. Rptr. 3d 326",
            "39 Cal. 4th 641",
            "2006 Daily Journal DAR 10936",
            "2006 Cal. LEXIS 9521"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Stone",
          "cluster_id": 4958214,
          "cite": [
            "2021 COA 104"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
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
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 1670023,
          "cite": [
            "755 N.W.2d 664",
            "279 Mich. App. 116"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
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
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gates v. Texas Deparment of Protective & Regulatory Services",
          "cluster_id": 62905,
          "cite": [
            "537 F.3d 404",
            "2008 WL 2875378"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Shover",
          "cluster_id": 2635828,
          "cite": [
            "217 P.3d 901",
            "2009 Colo. App. LEXIS 212",
            "2009 WL 399727"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
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
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
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
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
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
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
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
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fernandez v. California",
          "cluster_id": 2654534,
          "cite": [
            "188 L. Ed. 2d 25",
            "134 S. Ct. 1126",
            "2014 U.S. LEXIS 1636",
            "82 U.S.L.W. 4102",
            "571 U.S. 292",
            "24 Fla. L. Weekly Fed. S 553",
            "2014 WL 700100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Chavez",
          "cluster_id": 2380403,
          "cite": [
            "240 P.3d 448",
            "2010 Colo. App. LEXIS 213",
            "2010 WL 547625"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
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
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stabile",
          "cluster_id": 183984,
          "cite": [
            "633 F.3d 219",
            "2011 U.S. App. LEXIS 1945",
            "2011 WL 294036"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ryburn v. Huff",
          "cluster_id": 622303,
          "cite": [
            "181 L. Ed. 2d 966",
            "132 S. Ct. 987",
            "565 U.S. 469",
            "2012 U.S. LEXIS 910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Karen Fitzgerald v. M. Santoro",
          "cluster_id": 819861,
          "cite": [
            "707 F.3d 725",
            "2013 WL 452446",
            "2013 U.S. App. LEXIS 2600"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wilson",
          "cluster_id": 147086,
          "cite": [
            "605 F.3d 985",
            "390 U.S. App. D.C. 368",
            "82 Fed. R. Serv. 940",
            "2010 U.S. App. LEXIS 10558",
            "2010 WL 2036304"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Glenn v. Com.",
          "cluster_id": 1058555,
          "cite": [
            "654 S.E.2d 910",
            "275 Va. 123",
            "2008 Va. LEXIS 16"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145669 OR 9434962 OR 9434963 OR 9434964 OR 9434965 OR 9434966 OR 9434967) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzcxNjg2NDAwMDAwJnM9OTA0NTQ2JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145669+OR+9434962+OR+9434963+OR+9434964+OR+9434965+OR+9434966+OR+9434967%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 13,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(145669 OR 9434962 OR 9434963 OR 9434964 OR 9434965 OR 9434966 OR 9434967)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05OCZzPTI2NzQ4NDEmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145669+OR+9434962+OR+9434963+OR+9434964+OR+9434965+OR+9434966+OR+9434967%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145669 OR 9434962 OR 9434963 OR 9434964 OR 9434965 OR 9434966 OR 9434967)",
        "reviewed": 40,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 40,
        "triage_read": 0,
        "triage_snippet_classified": 40
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145669 OR 9434962 OR 9434963 OR 9434964 OR 9434965 OR 9434966 OR 9434967)",
    "indexed_citing_opinions": 692,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145669,
        "count": 583,
        "count_source": "search"
      },
      {
        "opinion_id": 9434962,
        "count": 123,
        "count_source": "search"
      },
      {
        "opinion_id": 9434963,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434964,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434965,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434966,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434967,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1204,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/georgia-v-randolph.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4NjY4Njgmcz0xMDYwMDA0NiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145669+OR+9434962+OR+9434963+OR+9434964+OR+9434965+OR+9434966+OR+9434967%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145669,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 108404,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 108608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 108967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 110212,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 110314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 112416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 112475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 112608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 112631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 118226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 118326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 118405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 134746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 162237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 197429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 272739,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 299112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 351740,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 364861,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 552251,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 702612,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 799991,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 1147536,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 1211487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 1298391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 1366935,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 1449748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 3878196,
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
    "date_created": "2026-07-05T05:18:41Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:18:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:18:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:22:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:18:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Georgia v. Randolph

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

                        GEORGIA v. RANDOLPH

        CERTIORARI TO THE SUPREME COURT OF GEORGIA

  No. 04–1067. Argued November 8, 2005—Decided March 22, 2006
Respondent’s estranged wife gave police permission to search the mari-
  tal residence for items of drug use after respondent, who was also
  present, had unequivocally refused to give consent. Respondent was
  indicted for possession of cocaine, and the trial court denied his mo-
  tion to suppress the evidence as products of a warrantless search un-
  authorized by consent. The Georgia Court of Appeals reversed. In
  affirming, the State Supreme Court held that consent given by one
  occupant is not valid in the face of the refusal of another physically
  present occupant, and distinguished United States v. Matlock, 415
  U. S. 164, which recognized the permissibility of an entry made with
  the consent of one co-occupant in the other’s absence.
Held: In the circumstances here at issue, a physically present co-
 occupant’s stated refusal to permit entry renders warrantless entry
 and search unreasonable and invalid as to him. Pp. 4–19.
    (a) The Fourth Amendment recognizes a valid warrantless entry
 and search of a premises when the police obtain the voluntary con-
 sent of an occupant who shares, or is reasonably believed to share,
 common authority over the property, and no present co-tenant ob-
 jects. Matlock, supra, at 170; Illinois v. Rodriguez, 497 U. S. 177,
 186. The constant element in assessing Fourth Amendment reason-
 ableness in such cases is the great significance given to widely shared
 social expectations, which are influenced by property law but not con-
 trolled by its rules. Thus, Matlock not only holds that a solitary co-
 inhabitant may sometimes consent to a search of shared premises,
 but also stands for the proposition that the reasonableness of such a
 search is in significant part a function of commonly held understand-
 ings about the authority that co-inhabitants may exercise in ways
 that affect each other’s interests. Pp. 4–6.
    (b) Matlock’s example of common understanding is readily appar-
2                        GEORGIA v. RANDOLPH

                                  Syllabus

    ent. The assumption tenants usually make about their common au-
    thority when they share quarters is that any one of them may admit
    visitors, with the consequence that a guest obnoxious to one may be
    admitted in his absence. Matlock placed no burden on the police to
    eliminate the possibility of atypical arrangements, absent reason to
    doubt that the regular scheme was in place. Pp. 6–8.
       (c) This Court took a step toward addressing the issue here when it
    held in Minnesota v. Olson, 495 U. S. 91, that overnight houseguests
    have a legitimate expectation of privacy in their temporary quarters.
    If that customary expectation is a foundation of a houseguest’s
    Fourth Amendment rights, it should follow that an inhabitant of
    shared premises may claim at least as much. In fact, a co-inhabitant
    naturally has an even stronger claim. No sensible person would en-
    ter shared premises based on one occupant’s invitation when a fellow
    tenant said to stay out. Such reticence would show not timidity but a
    realization that when people living together disagree over the use of
    their common quarters, a resolution must come through voluntary
    accommodation, not by appeals to authority. Absent some recognized
    hierarchy, e.g., parent and child, there is no societal or legal under-
    standing of superior and inferior as between co-tenants. Pp. 8–10.
       (d) Thus, a disputed invitation, without more, gives an officer no
    better claim to reasonableness in entering than the officer would
    have absent any consent. Disputed permission is no match for the
    Fourth Amendment central value of “respect for the privacy of the
    home,” Wilson v. Layne, 526 U. S. 603, 610, and the State’s other
    countervailing claims do not add up to outweigh it.
       A co-tenant who has an interest in bringing criminal activity to
    light or in deflecting suspicion from himself can, e.g., tell the police
    what he knows, for use before a magistrate in getting a warrant.
    This case, which recognizes limits on evidentiary searches, has no
    bearing on the capacity of the police, at the invitation of one tenant,
    to enter a dwelling over another tenant’s objection in order to protect
    a resident from domestic violence. Though alternatives to disputed
    consent will not always open the door to search for evidence that the
    police suspect is inside, nothing in social custom or its reflection in
    private law argues for placing a higher value on delving into private
    premises to search for evidence in the face of disputed consent, than
    on requiring clear justification before the government searches pri-
    vate living quarters over a resident’s objection. Pp. 10–16.
       (e) There are two loose ends. First, while Matlock’s explanation for
    the constitutional sufficiency of a co-tenant’s consent to enter and
    search recognized a co-inhabitant’s “right to permit the inspection in
    his own right,” 415 U. S., at 171, n. 7, the right to admit the police is
    not a right as understood under property law. It is, instead, the au-
                      Cite as: 547 U. S. ____ (2006)                       3

                                 Syllabus

  thority recognized by customary social usage as having a substantial
  bearing on Fourth Amendment reasonableness in specific circum-
  stances. The question here is whether customary social understand-
  ing accords the consenting tenant authority to prevail over the co-
  tenant’s objection, a question Matlock did not answer. Second, a fine
  line must be drawn to avoid undercutting Matlock—where the defen-
  dant, though not present, was in a squad car not far away—and Rod-
  riguez—where the defendant was asleep in the apartment and could
  have been roused by a knock on the door; if a potential defendant
  with self-interest in objecting is in fact at the door and objects, the co-
  tenant’s permission does not suffice for a reasonable search, whereas
  the potential objector, nearby but not part of the threshold colloquy,
  loses out. Such formalism is justified. So long as there is no evidence
  that the police have removed the potentially objecting tenant from
  the entrance specifically to avoid a possible objection, there is practi-
  cal value in the simple clarity of complementary rules, one recogniz-
  ing the co-tenant’s permission when no fellow occupant is on hand,
  the other according dispositive weight to the fellow occupant’s ex-
  pressed contrary indication. Pp. 16–18.
     (f) Here, respondent’s refusal is clear, and nothing in the record
  justifies the search on grounds independent of his wife’s consent.
  Pp. 18–19.
278 Ga. 614, 604 S. E. 2d 835, affirmed.

   SOUTER, J., delivered the opinion of the Court, in which STEVENS,
KENNEDY, GINSBURG, and BREYER, JJ., joined. STEVENS, J., and BREYER,
J., filed concurring opinions. ROBERTS, C. J., filed a dissenting opinion,
in which SCALIA, J., joined. SCALIA, J., and THOMAS, J., filed dissenting
opinions. ALITO, J., took no part in the consideration or decision of the
case.
                       Cite as: 547 U. S. ____ (2006)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash-
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 04–1067
                                  _________________


 GEORGIA, PETITIONER v. SCOTT FITZ RANDOLPH
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF
                       GEORGIA
                               [March 22, 2006]

   JUSTICE SOUTER delivered the opinion of the Court.
   The Fourth Amendment recognizes a valid warrantless
entry and search of premises when police obtain the vol-
untary consent of an occupant who shares, or is reasona-
bly believed to share, authority over the area in common
with a co-occupant who later objects to the use of evidence
so obtained. Illinois v. Rodriguez, 497 U. S. 177 (1990);
United States v. Matlock, 415 U. S. 164 (1974). The ques-
tion here is whether such an evidentiary seizure is like-
wise lawful with the permission of one occupant when the
other, who later seeks to suppress the evidence, is present
at the scene and expressly refuses to consent. We hold
that, in the circumstances here at issue, a physically
present co-occupant’s stated refusal to permit entry pre-
vails, rendering the warrantless search unreasonable and
invalid as to him.
                            I
  Respondent Scott Randolph and his wife, Janet, sepa-
rated in late May 2001, when she left the marital resi-
dence in Americus, Georgia, and went to stay with her
parents in Canada, taking their son and some belongings.
In July, she returned to the Americus house with the
2                 GEORGIA v. RANDOLPH

                     Opinion of the Court

child, though the record does not reveal whether her object
was reconciliation or retrieval of remaining possessions.
   On the morning of July 6, she complained to the police
that after a domestic dispute her husband took their son
away, and when officers reached the house she told them
that her husband was a cocaine user whose habit had
caused financial troubles. She mentioned the marital
problems and said that she and their son had only recently
returned after a stay of several weeks with her parents.
Shortly after the police arrived, Scott Randolph returned
and explained that he had removed the child to a
neighbor’s house out of concern that his wife might take
the boy out of the country again; he denied cocaine use,
and countered that it was in fact his wife who abused
drugs and alcohol.
   One of the officers, Sergeant Murray, went with Janet
Randolph to reclaim the child, and when they returned
she not only renewed her complaints about her husband’s
drug use, but also volunteered that there were “ ‘items of
drug evidence’ ” in the house. Brief for Petitioner 3. Ser-
geant Murray asked Scott Randolph for permission to
search the house, which he unequivocally refused.
   The sergeant turned to Janet Randolph for consent to
search, which she readily gave. She led the officer up-
stairs to a bedroom that she identified as Scott’s, where
the sergeant noticed a section of a drinking straw with a
powdery residue he suspected was cocaine. He then left
the house to get an evidence bag from his car and to call
the district attorney’s office, which instructed him to stop
the search and apply for a warrant. When Sergeant
Murray returned to the house, Janet Randolph withdrew
her consent. The police took the straw to the police sta-
tion, along with the Randolphs. After getting a search
warrant, they returned to the house and seized further
evidence of drug use, on the basis of which Scott Randolph
was indicted for possession of cocaine.
                  Cite as: 547 U. S. ____ (2006)            3

                      Opinion of the Court

   He moved to suppress the evidence, as products of a
warrantless search of his house unauthorized by his wife’s
consent over his express refusal. The trial court denied
the motion, ruling that Janet Randolph had common
authority to consent to the search.
   The Court of Appeals of Georgia reversed, 264 Ga. App.
396, 590 S. E. 2d 834 (2003), and was itself sustained by
the State Supreme Court, principally on the ground that
“the consent to conduct a warrantless search of a residence
given by one occupant is not valid in the face of the refusal
of another occupant who is physically present at the scene
to permit a warrantless search.” 278 Ga. 614, 604 S. E. 2d
835, 836 (2004). The Supreme Court of Georgia acknowl-
edged this Court’s holding in Matlock, 415 U. S. 164, that
“the consent of one who possesses common authority over
premises or effects is valid as against the absent, noncon-
senting person with whom that authority is shared,” id., at
170, and found Matlock distinguishable just because Scott
Randolph was not “absent” from the colloquy on which the
police relied for consent to make the search. The State
Supreme Court stressed that the officers in Matlock had not
been “faced with the physical presence of joint occupants,
with one consenting to the search and the other objecting.”
278 Ga., at 615, 604 S. E. 2d, at 837. It held that an indi-
vidual who chooses to live with another assumes a risk no
greater than “ ‘an inability to control access to the premises
during [his] absence,’ ” ibid. (quoting 3 W. LaFave, Search
and Seizure §8.3(d), p. 731 (3d ed. 1996) (hereinafter La-
Fave)), and does not contemplate that his objection to a
request to search commonly shared premises, if made, will
be overlooked.
   We granted certiorari to resolve a split of authority on
whether one occupant may give law enforcement effective
consent to search shared premises, as against a co-tenant
4                      GEORGIA v. RANDOLPH

                          Opinion of the Court

who is present and states a refusal to permit the search.1
544 U. S. 973 (2005). We now affirm.
                              II
   To the Fourth Amendment rule ordinarily prohibiting
the warrantless entry of a person’s house as unreasonable
per se, Payton v. New York, 445 U. S. 573, 586 (1980); Coo-
lidge v. New Hampshire, 403 U. S. 443, 454–455 (1971), one
“jealously and carefully drawn” exception, Jones v. United
States, 357 U. S. 493, 499 (1958), recognizes the validity of
searches with the voluntary consent of an individual pos-
sessing authority, Rodriguez, 497 U. S., at 181. That person
might be the householder against whom evidence is sought,
Schneckloth v. Bustamonte, 412 U. S. 218, 222 (1973), or a
fellow occupant who shares common authority over prop-
erty, when the suspect is absent, Matlock, supra, at 170, and
the exception for consent extends even to entries and
searches with the permission of a co-occupant whom the
police reasonably, but erroneously, believe to possess shared
authority as an occupant, Rodriguez, supra, at 186. None of
our co-occupant consent-to-search cases, however, has pre-
sented the further fact of a second occupant physically
present and refusing permission to search, and later moving
to suppress evidence so obtained.2 The significance of such
——————
    1 All
        four Courts of Appeals to have considered this question have
concluded that consent remains effective in the face of an express
objection. See United States v. Morning, 64 F. 3d 531, 533–536 (CA9
1995); United States v. Donlin, 982 F. 2d 31, 33 (CA1 1992); United
States v. Hendrix, 595 F. 2d 883, 885 (CADC 1979) (per curiam); United
States v. Sumlin, 567 F. 2d 684, 687–688 (CA6 1977). Of the state
courts that have addressed the question, the majority have reached
that conclusion as well. See, e.g., Love v. State, 355 Ark. 334, 342, 138
S. W. 3d 676, 680 (2003); Laramie v. Hysong, 808 P. 2d 199, 203–205
(Wyo. 1991); but cf. State v. Leach, 113 Wash. 2d 735, 744, 782 P. 2d
1035, 1040 (1989) (en banc) (requiring consent of all present co-
occupants).
  2 Mindful of the multiplicity of living arrangements, we vary the

terms used to describe residential co-occupancies. In so doing we do not
                    Cite as: 547 U. S. ____ (2006)                  5

                        Opinion of the Court

a refusal turns on the underpinnings of the co-occupant
consent rule, as recognized since Matlock.
                              A
  The defendant in that case was arrested in the yard of a
house where he lived with a Mrs. Graff and several of her
relatives, and was detained in a squad car parked nearby.
When the police went to the door, Mrs. Graff admitted
them and consented to a search of the house. 415 U. S., at
166. In resolving the defendant’s objection to use of the
evidence taken in the warrantless search, we said that
“the consent of one who possesses common authority over
premises or effects is valid as against the absent, noncon-
senting person with whom that authority is shared.” Id.,
at 170. Consistent with our prior understanding that
Fourth Amendment rights are not limited by the law of
property, cf. Katz v. United States, 389 U. S. 347, 352–353
(1967), we explained that the third party’s “common au-
thority” is not synonymous with a technical property
interest:
     “The authority which justified the third-party consent
     does not rest upon the law of property, with its atten-
     dant historical and legal refinement, but rests rather
     on mutual use of the property by persons generally
     having joint access or control for most purposes, so
     that it is reasonable to recognize that any of the co-
     inhabitants has the right to permit the inspection in
     his own right and that the others have assumed the
     risk that one of their number might permit the com-
     mon area to be searched.” 415 U. S., at 171, n. 7 (cita-
     tions omitted).
See also Frazier v. Cupp, 394 U. S. 731, 740 (1969) (“[I]n
allowing [his cousin to share use of a duffel bag] and in
——————
mean, however, to suggest that the rule to be applied to them is simi-
larly varied.
6                  GEORGIA v. RANDOLPH

                      Opinion of the Court

leaving it in his house, [the suspect] must be taken to have
assumed the risk that [the cousin] would allow someone
else to look inside”). The common authority that counts
under the Fourth Amendment may thus be broader than
the rights accorded by property law, see Rodriguez, supra,
at 181–182 (consent is sufficient when given by a person
who reasonably appears to have common authority but
who, in fact, has no property interest in the premises
searched), although its limits, too, reflect specialized
tenancy arrangements apparent to the police, see Chap-
man v. United States, 365 U. S. 610 (1961) (landlord could
not consent to search of tenant’s home).
  The constant element in assessing Fourth Amendment
reasonableness in the consent cases, then, is the great
significance given to widely shared social expectations,
which are naturally enough influenced by the law of prop-
erty, but not controlled by its rules. Cf. Rakas v. Illinois,
439 U. S. 128, 144, n. 12 (1978) (an expectation of privacy is
reasonable if it has “a source outside of the Fourth Amend-
ment, either by reference to concepts of real or personal
property law or to understandings that are recognized and
permitted by society”). Matlock accordingly not only holds
that a solitary co-inhabitant may sometimes consent to a
search of shared premises, but stands for the proposition
that the reasonableness of such a search is in significant
part a function of commonly held understanding about the
authority that co-inhabitants may exercise in ways that
affect each other’s interests.
                               B
  Matlock’s example of common understanding is readily
apparent. When someone comes to the door of a domestic
dwelling with a baby at her hip, as Mrs. Graff did, she
shows that she belongs there, and that fact standing alone
is enough to tell a law enforcement officer or any other
visitor that if she occupies the place along with others, she
                 Cite as: 547 U. S. ____ (2006)            7

                     Opinion of the Court

probably lives there subject to the assumption tenants
usually make about their common authority when they
share quarters. They understand that any one of them
may admit visitors, with the consequence that a guest
obnoxious to one may nevertheless be admitted in his
absence by another. As Matlock put it, shared tenancy is
understood to include an “assumption of risk,” on which
police officers are entitled to rely, and although some
group living together might make an exceptional ar-
rangement that no one could admit a guest without the
agreement of all, the chance of such an eccentric scheme is
too remote to expect visitors to investigate a particular
household’s rules before accepting an invitation to come
in. So, Matlock relied on what was usual and placed no
burden on the police to eliminate the possibility of atypical
arrangements, in the absence of reason to doubt that the
regular scheme was in place.
  It is also easy to imagine different facts on which, if
known, no common authority could sensibly be suspected.
A person on the scene who identifies himself, say, as a
landlord or a hotel manager calls up no customary under-
standing of authority to admit guests without the consent
of the current occupant. See Chapman v. United States,
supra (landlord); Stoner v. California, 376 U. S. 483 (1964)
(hotel manager). A tenant in the ordinary course does not
take rented premises subject to any formal or informal
agreement that the landlord may let visitors into the
dwelling, Chapman, supra, at 617, and a hotel guest cus-
tomarily has no reason to expect the manager to allow
anyone but his own employees into his room, see Stoner,
supra, at 489; see also United States v. Jeffers, 342 U. S.
48, 51 (1951) (hotel staff had access to room for purposes
of cleaning and maintenance, but no authority to admit
police). In these circumstances, neither state-law property
rights, nor common contractual arrangements, nor any
other source points to a common understanding of author-
8                  GEORGIA v. RANDOLPH

                     Opinion of the Court

ity to admit third parties generally without the consent of
a person occupying the premises. And when it comes to
searching through bureau drawers, there will be instances
in which even a person clearly belonging on premises as
an occupant may lack any perceived authority to consent;
“a child of eight might well be considered to have the
power to consent to the police crossing the threshold into
that part of the house where any caller, such as a pollster
or salesman, might well be admitted,” 4 LaFave §8.4(c), at
207 (4th ed. 2004), but no one would reasonably expect
such a child to be in a position to authorize anyone to
rummage through his parents’ bedroom.
                               C
   Although we have not dealt directly with the reason-
ableness of police entry in reliance on consent by one
occupant subject to immediate challenge by another, we
took a step toward the issue in an earlier case dealing
with the Fourth Amendment rights of a social guest ar-
rested at premises the police entered without a warrant or
the benefit of any exception to the warrant requirement.
Minnesota v. Olson, 495 U. S. 91 (1990), held that over-
night houseguests have a legitimate expectation of privacy
in their temporary quarters because “it is unlikely that
[the host] will admit someone who wants to see or meet
with the guest over the objection of the guest,” id., at 99.
If that customary expectation of courtesy or deference is a
foundation of Fourth Amendment rights of a houseguest,
it presumably should follow that an inhabitant of shared
premises may claim at least as much, and it turns out that
the co-inhabitant naturally has an even stronger claim.
   To begin with, it is fair to say that a caller standing at
the door of shared premises would have no confidence that
one occupant’s invitation was a sufficiently good reason to
enter when a fellow tenant stood there saying, “stay out.”
Without some very good reason, no sensible person would
                     Cite as: 547 U. S. ____ (2006)                     9

                          Opinion of the Court

go inside under those conditions. Fear for the safety of the
occupant issuing the invitation, or of someone else inside,
would be thought to justify entry, but the justification
then would be the personal risk, the threats to life or limb,
not the disputed invitation.3
   The visitor’s reticence without some such good reason
would show not timidity but a realization that when peo-
ple living together disagree over the use of their common
quarters, a resolution must come through voluntary ac-
commodation, not by appeals to authority. Unless the
people living together fall within some recognized hierar-
chy, like a household of parent and child or barracks
housing military personnel of different grades, there is no
societal understanding of superior and inferior, a fact
reflected in a standard formulation of domestic property
law, that “[e]ach cotenant . . . has the right to use and
enjoy the entire property as if he or she were the sole
owner, limited only by the same right in the other coten-
ants.” 7 R. Powell, Powell on Real Property §50.03[1],
p. 50–14 (M. Wolf gen. ed. 2005). The want of any recog-
nized superior authority among disagreeing tenants is also
reflected in the law’s response when the disagreements
cannot be resolved. The law does not ask who has the
better side of the conflict; it simply provides a right to any
co-tenant, even the most unreasonable, to obtain a decree
partitioning the property (when the relationship is one of
co-ownership) and terminating the relationship. See, e.g.,
2 H. Tiffany, Real Property §§468, 473, 474, pp. 297, 307–
309 (3d ed. 1939 and 2006 Cum. Supp.). And while a
decree of partition is not the answer to disagreement
among rental tenants, this situation resembles co-
——————
   3 Cf. Mincey v. Arizona, 437 U. S. 385, 393 (1978) (acknowledging the

right of police to respond to emergency situations “threatening life or
limb” and indicating that police may conduct a warrantless search pro-
vided that the search is “ ‘strictly circumscribed by the exigencies which
justify its initiation’ ”).
10                       GEORGIA v. RANDOLPH

                            Opinion of the Court

ownership in lacking the benefit of any understanding
that one or the other rental co-tenant has a superior claim
to control the use of the quarters they occupy together. In
sum, there is no common understanding that one co-
tenant generally has a right or authority to prevail over
the express wishes of another, whether the issue is the
color of the curtains or invitations to outsiders.
                              D
   Since the co-tenant wishing to open the door to a third
party has no recognized authority in law or social practice
to prevail over a present and objecting co-tenant, his
disputed invitation, without more, gives a police officer no
better claim to reasonableness in entering than the officer
would have in the absence of any consent at all. Accord-
ingly, in the balancing of competing individual and gov-
ernmental interests entailed by the bar to unreasonable
searches, Camara v. Municipal Court of City and County of
San Francisco, 387 U. S. 523, 536–537 (1967), the coopera-
tive occupant’s invitation adds nothing to the govern-
ment’s side to counter the force of an objecting individual’s
claim to security against the government’s intrusion into
his dwelling place. Since we hold to the “centuries-old
principle of respect for the privacy of the home,” Wilson v.
Layne, 526 U. S. 603, 610 (1999), “it is beyond dispute that
the home is entitled to special protection as the center of
the private lives of our people,” Minnesota v. Carter, 525
U. S. 83, 99 (1998) (KENNEDY, J., concurring). We have,
after all, lived our whole national history with an under-
standing of “the ancient adage that a man’s home is his
castle [to the point that t]he poorest man may in his cot-
tage bid defiance to all the forces of the Crown,” Miller v.
United States, 357 U. S. 301, 307 (1958) (internal quota-
tion marks omitted).4
——————
 4 In   the dissent’s view, the centuries of special protection for the pri-
                     Cite as: 547 U. S. ____ (2006)                    11

                          Opinion of the Court

  Disputed permission is thus no match for this central
value of the Fourth Amendment, and the State’s other
countervailing claims do not add up to outweigh it.5 Yes,
we recognize the consenting tenant’s interest as a citizen
in bringing criminal activity to light, see Coolidge, 403
U. S., at 488 (“[I]t is no part of the policy underlying the
Fourth . . . Amendmen[t] to discourage citizens from aiding
to the utmost of their ability in the apprehension of crimi-
nals”). And we understand a co-tenant’s legitimate self-
interest in siding with the police to deflect suspicion raised
by sharing quarters with a criminal, see 4 LaFave §8.3(d),
at 162, n. 72 (“The risk of being convicted of possession of
drugs one knows are present and has tried to get the other
occupant to remove is by no means insignificant”); cf.
Schneckloth, 412 U. S., at 243 (evidence obtained pursuant
to a consent search “may insure that a wholly innocent
person is not wrongly charged with a criminal offense”).
  But society can often have the benefit of these interests
without relying on a theory of consent that ignores an
inhabitant’s refusal to allow a warrantless search. The co-
tenant acting on his own initiative may be able to deliver
evidence to the police, Coolidge, supra, at 487–489 (sus-
——————
vacy of the home are over. The principal dissent equates inviting the
police into a co-tenant’s home over his contemporaneous objection with
reporting a secret, post, at 13–14 (opinion of ROBERTS, C. J.), and the
emphasis it places on the false equation suggests a deliberate intent to
devalue the importance of the privacy of a dwelling place. The same
attitude that privacy of a dwelling is not special underlies the dissent’s
easy assumption that privacy shared with another individual is privacy
waived for all purposes including warrantless searches by the police.
Post, at 5.
  5 A generalized interest in expedient law enforcement cannot, without

more, justify a warrantless search. See Mincey, supra, at 393 (“[T]he
privacy of a person’s home and property may not be totally sacrificed in
the name of maximum simplicity in enforcement of the criminal law”);
Coolidge v. New Hampshire, 403 U. S. 443, 481 (1971) (“The warrant
requirement . . . is not an inconvenience to be somehow ‘weighed’ against
the claims of police efficiency”).
12                     GEORGIA v. RANDOLPH

                          Opinion of the Court

pect’s wife retrieved his guns from the couple’s house and
turned them over to the police), and can tell the police
what he knows, for use before a magistrate in getting a
warrant.6 The reliance on a co-tenant’s information in-
stead of disputed consent accords with the law’s general
partiality toward “police action taken under a warrant [as
against] searches and seizures without one,” United States
v. Ventresca, 380 U. S. 102, 107 (1965); “the informed and
deliberate determinations of magistrates empowered to
issue warrants as to what searches and seizures are permis-
sible under the Constitution are to be preferred over the
hurried action of officers,” United States v. Lefkowitz, 285
U. S. 452, 464 (1932).
   Nor should this established policy of Fourth Amendment
law be undermined by the principal dissent’s claim that it
shields spousal abusers and other violent co-tenants who
will refuse to allow the police to enter a dwelling when
their victims ask the police for help, post, at 12 (opinion of
ROBERTS, C. J.) (hereinafter the dissent). It is not that the
——————
   6 Sometimes, of course, the very exchange of information like this in

front of the objecting inhabitant may render consent irrelevant by
creating an exigency that justifies immediate action on the police’s part;
if the objecting tenant cannot be incapacitated from destroying easily
disposable evidence during the time required to get a warrant, see
Illinois v. McArthur, 531 U. S. 326, 331–332 (2001) (denying suspect
access to his trailer home while police applied for a search warrant), a
fairly perceived need to act on the spot to preserve evidence may justify
entry and search under the exigent circumstances exception to the
warrant requirement, cf. Schmerber v. California, 384 U. S. 757, 770–
771 (1966) (warrantless search permitted when “the delay necessary to
obtain a warrant . . . threatened the destruction of evidence” (internal
quotation marks omitted)).
   Additional exigent circumstances might justify warrantless searches.
See, e.g., Warden, Md. Penitentiary v. Hayden, 387 U. S. 294, 298
(1967) (hot pursuit); Chimel v. California, 395 U. S. 752 (1969) (protect-
ing the safety of the police officers); Michigan v. Tyler, 436 U. S. 499
(1978) (imminent destruction to building); Johnson v. United States,
333 U. S. 10, 15 (1948) (likelihood that suspect will imminently flee).
                 Cite as: 547 U. S. ____ (2006)           13

                     Opinion of the Court

dissent exaggerates violence in the home; we recognize
that domestic abuse is a serious problem in the United
States. See U. S. Dept. of Justice, National Institute of
Justice, P. Tjaden & N. Thoennes, Full Report of the
Prevalence, Incidence, and Consequence of Violence
Against Women 25–26 (2000) (noting that over 20 million
women and 6 million men will, in the course of their life-
times, be the victims of intimate-partner abuse); U. S.
Dept. of Health and Human Services, Centers for Disease
Control and Prevention, National Center for Injury Pre-
vention and Control, Costs of Intimate Partner Violence
Against Women in the United States 19 (2003) (finding
that nearly 5.3 million intimate partner victimizations,
which result in close to 2 million injuries and 1300 deaths,
occur among women in the United States each year); U. S.
Dept. of Justice, Bureau of Justice Statistics, Crime Data
Brief, C. Rennison, Intimate Partner Violence, 1993–2001
(Feb. 2003) (noting that in 2001 intimate partner violence
made up 20% of violent crime against women); see also
Becker, The Politics of Women’s Wrongs and the Bill of
“Rights”: A Bicentennial Perspective, 59 U. Chi. L. Rev.
454, 507–508 (1992) (noting that women may feel physical
insecurity in their homes as a result of abuse from domes-
tic partners).
   But this case has no bearing on the capacity of the police
to protect domestic victims. The dissent’s argument rests
on the failure to distinguish two different issues: when the
police may enter without committing a trespass, and when
the police may enter to search for evidence. No question
has been raised, or reasonably could be, about the author-
ity of the police to enter a dwelling to protect a resident
from domestic violence; so long as they have good reason
to believe such a threat exists, it would be silly to suggest
that the police would commit a tort by entering, say, to
give a complaining tenant the opportunity to collect be-
longings and get out safely, or to determine whether vio-
14                     GEORGIA v. RANDOLPH

                          Opinion of the Court

lence (or threat of violence) has just occurred or is about to
(or soon will) occur, however much a spouse or other co-
tenant objected. (And since the police would then be
lawfully in the premises, there is no question that they
could seize any evidence in plain view or take further
action supported by any consequent probable cause, see
Texas v. Brown, 460 U. S. 730, 737–739 (1983) (plurality
opinion).) Thus, the question whether the police might
lawfully enter over objection in order to provide any pro-
tection that might be reasonable is easily answered yes.
See 4 LaFave §8.3(d), at 161 (“[E]ven when . . . two per-
sons quite clearly have equal rights in the place, as where
two individuals are sharing an apartment on an equal
basis, there may nonetheless sometimes exist a basis for
giving greater recognition to the interests of one over the
other. . . . [W]here the defendant has victimized the third-
party . . . the emergency nature of the situation is such
that the third-party consent should validate a warrantless
search despite defendant’s objections” (internal quotation
marks omitted; third omission in original)). The un-
doubted right of the police to enter in order to protect a
victim, however, has nothing to do with the question in
this case, whether a search with the consent of one co-
tenant is good against another, standing at the door and
expressly refusing consent.7
   None of the cases cited by the dissent support its im-
probable view that recognizing limits on merely eviden-
tiary searches would compromise the capacity to protect a
fearful occupant. In the circumstances of those cases,
——————
   7 We understand the possibility that a battered individual will be

afraid to express fear candidly, but this does not seem to be a reason to
think such a person would invite the police into the dwelling to search
for evidence against another. Hence, if a rule crediting consent over
denial of consent were built on hoping to protect household victims, it
would distort the Fourth Amendment with little, if any, constructive
effect on domestic abuse investigations.
                 Cite as: 547 U. S. ____ (2006)          15

                     Opinion of the Court

there is no danger that the fearful occupant will be kept
behind the closed door of the house simply because the
abusive tenant refuses to consent to a search. See United
States v. Donlin, 982 F. 2d 31, 32 (CA1 1992) (victimized
individual was already outside of her apartment when
police arrived and, for all intents and purposes, within the
protective custody of law enforcement officers); United
States v. Hendrix, 595 F. 2d 883, 885–886 (CADC 1979)
(per curiam) (even if the consent of the threatened co-
occupant did not justify a warrantless search, the police
entry    was      nevertheless    allowable   on    exigent-
circumstances grounds); People v. Sanders, 904 P. 2d
1311, 1313–1315 (Colo. 1995) (victimized individual gave
her consent-to-search away from her home and was not
present at the time of the police visit; alternatively, exi-
gent circumstances existed to satisfy the warrantless
exception); Brandon v. State, 778 P. 2d 221, 223–224
(Alaska App. 1989) (victimized individual consented away
from her home and was not present at the time of the
police visit); United States v. Davis, 290 F. 3d 1239, 1241
(CA10 2002) (immediate harm extinguished after husband
“order[ed]” wife out of the home).
   The dissent’s red herring aside, we know, of course, that
alternatives to disputed consent will not always open the
door to search for evidence that the police suspect is in-
side. The consenting tenant may simply not disclose
enough information, or information factual enough, to add
up to a showing of probable cause, and there may be no
exigency to justify fast action. But nothing in social cus-
tom or its reflection in private law argues for placing a
higher value on delving into private premises to search for
evidence in the face of disputed consent, than on requiring
clear justification before the government searches private
living quarters over a resident’s objection. We therefore
hold that a warrantless search of a shared dwelling for
evidence over the express refusal of consent by a physi-
16                    GEORGIA v. RANDOLPH

                         Opinion of the Court

cally present resident cannot be justified as reasonable as
to him on the basis of consent given to the police by an-
other resident.8
                             E
  There are two loose ends, the first being the explanation
given in Matlock for the constitutional sufficiency of a co-
tenant’s consent to enter and search: it “rests . . . on mu-
tual use of the property by persons generally having joint
access or control for most purposes, so that it is reasonable
to recognize that any of the co-inhabitants has the right to
permit the inspection in his own right . . . .” 415 U. S., at
171, n. 7. If Matlock’s co-tenant is giving permission “in
his own right,” how can his “own right” be eliminated by
another tenant’s objection? The answer appears in the
very footnote from which the quoted statement is taken:
the “right” to admit the police to which Matlock refers is
not an enduring and enforceable ownership right as un-
derstood by the private law of property, but is instead the
authority recognized by customary social usage as having
a substantial bearing on Fourth Amendment reasonable-
ness in specific circumstances. Thus, to ask whether the
consenting tenant has the right to admit the police when a
physically present fellow tenant objects is not to question
whether some property right may be divested by the mere
objection of another. It is, rather, the question whether
customary social understanding accords the consenting
tenant authority powerful enough to prevail over the co-
tenant’s objection. The Matlock Court did not purport to
answer this question, a point made clear by another
statement (which the dissent does not quote): the Court
——————
  8 The dissent is critical that our holding does not pass upon the con-

stitutionality of such a search as to a third tenant against whom the
government wishes to use evidence seized after a search with consent of
one co-tenant subject to the contemporaneous objection of another, post,
at 11. We decide the case before us, not a different one.
                  Cite as: 547 U. S. ____ (2006)           17

                      Opinion of the Court

described the co-tenant’s consent as good against “the
absent, nonconsenting” resident.” Id., at 170.
   The second loose end is the significance of Matlock and
Rodriguez after today’s decision. Although the Matlock
defendant was not present with the opportunity to object,
he was in a squad car not far away; the Rodriguez defen-
dant was actually asleep in the apartment, and the police
might have roused him with a knock on the door before
they entered with only the consent of an apparent co-
tenant. If those cases are not to be undercut by today’s
holding, we have to admit that we are drawing a fine line;
if a potential defendant with self-interest in objecting is in
fact at the door and objects, the co-tenant’s permission
does not suffice for a reasonable search, whereas the
potential objector, nearby but not invited to take part in
the threshold colloquy, loses out.
   This is the line we draw, and we think the formalism is
justified. So long as there is no evidence that the police
have removed the potentially objecting tenant from the
entrance for the sake of avoiding a possible objection,
there is practical value in the simple clarity of complemen-
tary rules, one recognizing the co-tenant’s permission
when there is no fellow occupant on hand, the other ac-
cording dispositive weight to the fellow occupant’s con-
trary indication when he expresses it. For the very reason
that Rodriguez held it would be unjustifiably impractical
to require the police to take affirmative steps to confirm
the actual authority of a consenting individual whose
authority was apparent, we think it would needlessly limit
the capacity of the police to respond to ostensibly legiti-
mate opportunities in the field if we were to hold that
reasonableness required the police to take affirmative
steps to find a potentially objecting co-tenant before acting
on the permission they had already received. There is no
ready reason to believe that efforts to invite a refusal
would make a difference in many cases, whereas every co-
18                    GEORGIA v. RANDOLPH

                         Opinion of the Court

tenant consent case would turn into a test about the ade-
quacy of the police’s efforts to consult with a potential
objector. Better to accept the formalism of distinguishing
Matlock from this case than to impose a requirement,
time-consuming in the field and in the courtroom, with no
apparent systemic justification. The pragmatic decision to
accept the simplicity of this line is, moreover, supported by
the substantial number of instances in which suspects who
are asked for permission to search actually consent,9 albeit
imprudently, a fact that undercuts any argument that the
police should try to locate a suspected inhabitant because
his denial of consent would be a foregone conclusion.
                             III
   This case invites a straightforward application of the
rule that a physically present inhabitant’s express refusal
of consent to a police search is dispositive as to him, re-
gardless of the consent of a fellow occupant. Scott
Randolph’s refusal is clear, and nothing in the record
justifies the search on grounds independent of Janet
Randolph’s consent. The State does not argue that she
gave any indication to the police of a need for protection
inside the house that might have justified entry into the
portion of the premises where the police found the pow-
dery straw (which, if lawfully seized, could have been used
when attempting to establish probable cause for the war-
rant issued later). Nor does the State claim that the entry
and search should be upheld under the rubric of exigent
circumstances, owing to some apprehension by the police
——————
  9 See 4 LaFave §8.1, at 4 (“The so-called consent search is frequently
relied upon by police as a means of investigating suspected criminal
conduct” (footnote omitted)); Strauss, Reconstructing Consent, 92 J.
Crim. L. & C. 211, 214 (2001–2002) (“Although precise figures detailing
the number of searches conducted pursuant to consent are not—and
probably can never be—available, there is no dispute that these type of
searches affect tens of thousands, if not hundreds of thousands, of
people every year” (footnote omitted)).
                 Cite as: 547 U. S. ____ (2006)           19

                     Opinion of the Court

officers that Scott Randolph would destroy evidence of
drug use before any warrant could be obtained.
  The judgment of the Supreme Court of Georgia is there-
fore affirmed.
                                           It is so ordered.

  JUSTICE ALITO took no part in the consideration or
decision of this case.
                    Cite as: 547 U. S. ____ (2006)                   1

                       STEVENS, J., concurring

SUPREME COURT OF THE UNITED STATES
                             _________________

                             No. 04–1067
                             _________________


 GEORGIA, PETITIONER v. SCOTT FITZ RANDOLPH
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF
                       GEORGIA
                           [March 22, 2006]

   JUSTICE STEVENS, concurring.
   The study of history for the purpose of ascertaining the
original understanding of constitutional provisions is much
like the study of legislative history for the purpose of ascer-
taining the intent of the lawmakers who enact statutes. In
both situations the facts uncovered by the study are usually
relevant but not necessarily dispositive. This case illus-
trates why even the most dedicated adherent to an ap-
proach to constitutional interpretation that places primary
reliance on the search for original understanding would
recognize the relevance of changes in our society.
   At least since 1604 it has been settled that in the ab-
sence of exigent circumstances, a government agent has no
right to enter a “house” or “castle” unless authorized to do
so by a valid warrant. See Semayne’s Case, 5 Co. Rep.
91a, 77 Eng. Rep. 194 (K.B.). Every occupant of the home
has a right—protected by the common law for centuries
and by the Fourth Amendment since 1791—to refuse
entry. When an occupant gives his or her consent to enter,
he or she is waiving a valuable constitutional right. To be
sure that the waiver is voluntary, it is sound practice—a
practice some Justices of this Court thought necessary to
make the waiver voluntary1—for the officer to advise the
——————
  1 See, e.g., Schneckloth v. Bustamonte, 412 U. S. 218, 284–285 (1973)

(Marshall, J., dissenting) (pointing out that it is hard to comprehend
“how a decision made without knowledge of available alternatives can
2                      GEORGIA v. RANDOLPH

                        STEVENS, J., concurring

occupant of that right.2 The issue in this case relates to
the content of the advice that the officer should provide
when met at the door by a man and a woman who are
apparently joint tenants or joint owners of the property.
  In the 18th century, when the Fourth Amendment was
adopted, the advice would have been quite different from
what is appropriate today. Given the then-prevailing
dramatic differences between the property rights of the
husband and the far lesser rights of the wife, only the
consent of the husband would matter. Whether “the mas-
ter of the house” consented or objected, his decision would
control. Thus if “original understanding” were to govern
the outcome of this case, the search was clearly invalid
because the husband did not consent. History, however, is
not dispositive because it is now clear, as a matter of
constitutional law, that the male and the female are equal
partners. Reed v. Reed, 404 U. S. 71 (1971).
  In today’s world the only advice that an officer could
properly give should make it clear that each of the part-
ners has a constitutional right that he or she may inde-
pendently assert or waive. Assuming that both spouses
are competent, neither one is a master possessing the
power to override the other’s constitutional right to deny
entry to their castle.
  With these observations, I join the Court’s opinion.
——————
be treated as choice at all,” and arguing that “[i]f consent to search
means that a person has chosen to forego his right to exclude the police
from the place they seek to search, it follows that his consent cannot be
considered a meaningful choice unless he knew that he could in fact
exclude the police”).
  2 Such advice is surely preferable to an officer’s expression of his or

her desire to enter and to search in words that may be construed either
as a command or a question. See id., at 275–276 (Douglas, J., dissenting)
(noting that “ ‘[u]nder many circumstances a reasonable person might
read an officer’s “May I” as the courteous expression of a demand
backed by force of law.’ ” (quoting Bustamonte v. Schneckloth, 448 F. 2d
669, 701 (CA9 1971))).
                  Cite as: 547 U. S. ____ (2006)            1

                     BREYER, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 04–1067
                          _________________


 GEORGIA, PETITIONER v. SCOTT FITZ RANDOLPH
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF
                       GEORGIA
                        [March 22, 2006]

   JUSTICE BREYER, concurring.
   If Fourth Amendment law forced us to choose between
two bright-line rules, (1) a rule that always found one
tenant’s consent sufficient to justify a search without a
warrant and (2) a rule that never did, I believe we should
choose the first. That is because, as THE CHIEF JUSTICE’s
dissent points out, a rule permitting such searches can
serve important law enforcement needs (for example, in
domestic abuse cases) and the consenting party’s joint
tenancy diminishes the objecting party’s reasonable expec-
tation of privacy.
   But the Fourth Amendment does not insist upon bright-
line rules. Rather, it recognizes that no single set of legal
rules can capture the ever changing complexity of human
life. It consequently uses the general terms “unreasonable
searches and seizures.” And this Court has continuously
emphasized that “[r]easonableness . . . is measured . . . by
examining the totality of the circumstances.” Ohio v.
Robinette, 519 U. S. 33, 39 (1996); see also Illinois v. Ward-
low, 528 U. S. 119, 136 (2000) (STEVENS, J., concurring in
part and dissenting in part); Florida v. Bostick, 501 U. S.
429, 439 (1991); Michigan v. Chesternut, 486 U. S. 567, 572–
573 (1988); Florida v. Royer, 460 U. S. 491, 506 (1983) (plu-
rality opinion).
   The circumstances here include the following: The
search at issue was a search solely for evidence. The
2                  GEORGIA v. RANDOLPH

                    BREYER, J., concurring

objecting party was present and made his objection known
clearly and directly to the officers seeking to enter the
house. The officers did not justify their search on grounds
of possible evidence destruction. Cf. Thornton v. United
States, 541 U. S. 615, 620–622 (2004); Skinner v. Railway
Labor Executives’ Assn., 489 U. S. 602, 623 (1989); Schmer-
ber v. California, 384 U. S. 757, 770–771 (1966). And, as far
as the record reveals, the officers might easily have se-
cured the premises and sought a warrant permitting them
to enter. See Illinois v. McArthur, 531 U. S. 326 (2001).
Thus, the “totality of the circumstances” present here do
not suffice to justify abandoning the Fourth Amendment’s
traditional hostility to police entry into a home without a
warrant.
   I stress the totality of the circumstances, however,
because, were the circumstances to change significantly,
so should the result. The Court’s opinion does not apply
where the objector is not present “and object[ing].” Ante,
at 17.
   Moreover, the risk of an ongoing crime or other exigent
circumstance can make a critical difference. Consider,
for example, instances of domestic abuse. See ante, at
13. “Family disturbance calls . . . constitute the largest
single category of calls received by police departments
each year.” Mederer & Gelles, Compassion or Control:
Intervention in Cases of Wife Abuse, 4 Journal of
Interpersonal Violence 25 (Mar. 1989) (emphasis deleted);
see also, e.g., Office of the Attorney General, California
Criminal Justice Statistics Center, Domestic Violence
Related Calls for Assistance, 1987–2003, County
by Year, http://ag.ca.gov/cjsc/publications/misc/dvsr/tabs/
8703.pdf (as visited Mar. 1, 2006, and available in Clerk of
Court’s case file) (providing data showing that California
police received an average of 207,848 domestic violence
related calls each year); Cessato, Defenders Against Do-
mestic Abuse, Washington Post, Aug. 25, 2002, p. B8 (“In
                  Cite as: 547 U. S. ____ (2006)            3

                     BREYER, J., concurring

the District [of Columbia], police report that almost half of
roughly 39,000 violent crime calls received in 2000 in-
volved domestic violence”); Zorza, Women Battering: High
Costs and the State of the Law, Clearinghouse Review,
p. 385 (Special Issue 1994) (“One-third of all police time is
spent responding to domestic disturbance calls”). And,
law enforcement officers must be able to respond effec-
tively when confronted with the possibility of abuse.
   If a possible abuse victim invites a responding officer to
enter a home or consents to the officer’s entry request,
that invitation (or consent) itself could reflect the victim’s
fear about being left alone with an abuser. It could also
indicate the availability of evidence, in the form of an
immediate willingness to speak, that might not otherwise
exist. In that context, an invitation (or consent) would
provide a special reason for immediate, rather than later,
police entry. And, entry following invitation or consent by
one party ordinarily would be reasonable even in the face
of direct objection by the other. That being so, contrary to
the THE CHIEF JUSTICE’s suggestion, post, at 13, today’s
decision will not adversely affect ordinary law enforcement
practices.
   Given the case-specific nature of the Court’s holding,
and with these understandings, I join the Court’s holding
and its opinion.
                 Cite as: 547 U. S. ____ (2006)           1

                   ROBERTS, C. J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 04–1067
                         _________________


 GEORGIA, PETITIONER v. SCOTT FITZ RANDOLPH
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF
                       GEORGIA
                       [March 22, 2006]

   CHIEF JUSTICE ROBERTS, with whom JUSTICE SCALIA
joins, dissenting.
   The Court creates constitutional law by surmising what
is typical when a social guest encounters an entirely atypi-
cal situation. The rule the majority fashions does not
implement the high office of the Fourth Amendment to
protect privacy, but instead provides protection on a ran-
dom and happenstance basis, protecting, for example, a co-
occupant who happens to be at the front door when the
other occupant consents to a search, but not one napping
or watching television in the next room. And the cost of
affording such random protection is great, as demon-
strated by the recurring cases in which abused spouses
seek to authorize police entry into a home they share with
a nonconsenting abuser.
   The correct approach to the question presented is clearly
mapped out in our precedents: The Fourth Amendment
protects privacy. If an individual shares information,
papers, or places with another, he assumes the risk that
the other person will in turn share access to that informa-
tion or those papers or places with the government. And
just as an individual who has shared illegal plans or in-
criminating documents with another cannot interpose an
objection when that other person turns the information
over to the government, just because the individual hap-
pens to be present at the time, so too someone who shares
2                  GEORGIA v. RANDOLPH

                   ROBERTS, C. J., dissenting

a place with another cannot interpose an objection when
that person decides to grant access to the police, simply
because the objecting individual happens to be present.
  A warrantless search is reasonable if police obtain the
voluntary consent of a person authorized to give it. Co-
occupants have “assumed the risk that one of their num-
ber might permit [a] common area to be searched.” United
States v. Matlock, 415 U. S. 164, 171, n. 7 (1974). Just as
Mrs. Randolph could walk upstairs, come down, and turn
her husband’s cocaine straw over to the police, she can
consent to police entry and search of what is, after all, her
home, too.
                               I
   In Illinois v. Rodriguez, 497 U. S. 177 (1990), this Court
stated that “[w]hat [a person] is assured by the Fourth
Amendment . . . is not that no government search of his
house will occur unless he consents; but that no such
search will occur that is ‘unreasonable.’ ” Id., at 183. One
element that can make a warrantless government search
of a home “ ‘reasonable’ ” is voluntary consent. Id., at 184;
Schneckloth v. Bustamonte, 412 U. S. 218, 219 (1973).
Proof of voluntary consent “is not limited to proof that
consent was given by the defendant,” but the government
“may show that permission to search was obtained from a
third party who possessed common authority over or other
sufficient relationship to the premises.” Matlock, supra, at
171. Today’s opinion creates an exception to this other-
wise clear rule: A third-party consent search is unreason-
able, and therefore constitutionally impermissible, if the
co-occupant against whom evidence is obtained was pre-
sent and objected to the entry and search.
   This exception is based on what the majority describes
as “widely shared social expectations” that “when people
living together disagree over the use of their common
quarters, a resolution must come through voluntary ac-
                 Cite as: 547 U. S. ____ (2006)            3

                   ROBERTS, C. J., dissenting

commodation.” Ante, at 6, 9. But this fundamental predi-
cate to the majority’s analysis gets us nowhere: Does the
objecting cotenant accede to the consenting cotenant’s
wishes, or the other way around? The majority’s assump-
tion about voluntary accommodation simply leads to the
common stalemate of two gentlemen insisting that the
other enter a room first.
   Nevertheless, the majority is confident in assuming—
confident enough to incorporate its assumption into the
Constitution—that an invited social guest who arrives at
the door of a shared residence, and is greeted by a dis-
agreeable co-occupant shouting “ ‘stay out,’ ” would simply
go away. Ante, at 8. The Court observes that “no sensible
person would go inside under those conditions,” ante, at 8–
9, and concludes from this that the inviting co-occupant
has no “authority” to insist on getting her way over the
wishes of her co-occupant, ante, at 10. But it seems
equally accurate to say—based on the majority’s conclu-
sion that one does not have a right to prevail over the
express wishes of his co-occupant—that the objector has
no “authority” to insist on getting his way over his co-
occupant’s wish that her guest be admitted.
   The fact is that a wide variety of differing social situa-
tions can readily be imagined, giving rise to quite different
social expectations. A relative or good friend of one of two
feuding roommates might well enter the apartment over
the objection of the other roommate. The reason the in-
vitee appeared at the door also affects expectations: A
guest who came to celebrate an occupant’s birthday, or one
who had traveled some distance for a particular reason,
might not readily turn away simply because of a room-
mate’s objection. The nature of the place itself is also
pertinent: Invitees may react one way if the feuding
roommates share one room, differently if there are com-
mon areas from which the objecting roommate could read-
ily be expected to absent himself. Altering the numbers
4                  GEORGIA v. RANDOLPH

                   ROBERTS, C. J., dissenting

might well change the social expectations: Invitees might
enter if two of three co-occupants encourage them to do so,
over one dissenter.
   The possible scenarios are limitless, and slight varia-
tions in the fact pattern yield vastly different expecta-
tions about whether the invitee might be expected to
enter or to go away. Such shifting expectations are not a
promising foundation on which to ground a constitutional
rule, particularly because the majority has no support for
its basic assumption—that an invited guest encountering
two disagreeing co-occupants would flee—beyond a hunch
about how people would typically act in an atypical
situation.
   And in fact the Court has not looked to such expecta-
tions to decide questions of consent under the Fourth
Amendment, but only to determine when a search has
occurred and whether a particular person has standing to
object to a search. For these latter inquiries, we ask
whether a person has a subjective expectation of privacy
in a particular place, and whether “the expectation [is] one
that society is prepared to recognize as ‘reasonable.’ ” Katz
v. United States, 389 U. S. 347, 361 (1967) (Harlan, J.,
concurring); see Minnesota v. Olson, 495 U. S. 91, 95–96,
100 (1990) (extending Katz test to standing inquiry). But
the social expectations concept has not been applied to all
questions arising under the Fourth Amendment, least of
all issues of consent. A criminal might have a strong
expectation that his longtime confidant will not allow the
government to listen to their private conversations, but
however profound his shock might be upon betrayal, gov-
ernment monitoring with the confidant’s consent is rea-
sonable under the Fourth Amendment. See United States
v. White, 401 U. S. 745, 752 (1971).
   The majority suggests that “widely shared social expecta-
tions” are a “constant element in assessing Fourth Amend-
ment reasonableness,” ante, at 6 (citing Rakas v. Illinois,
                  Cite as: 547 U. S. ____ (2006)              5

                    ROBERTS, C. J., dissenting

439 U. S. 128, 144, n. 12 (1978)), but that is not the case; the
Fourth Amendment precedents the majority cites refer
instead to a “legitimate expectation of privacy.” Ibid.
(emphasis added; internal quotation marks omitted).
Whatever social expectation the majority seeks to protect,
it is not one of privacy. The very predicate giving rise to
the question in cases of shared information, papers, con-
tainers, or places is that privacy has been shared with
another. Our common social expectations may well be
that the other person will not, in turn, share what we have
shared with them with another—including the police—but
that is the risk we take in sharing. If two friends share a
locker and one keeps contraband inside, he might trust
that his friend will not let others look inside. But by
sharing private space, privacy has “already been frus-
trated” with respect to the lockermate. United States v.
Jacobsen, 466 U. S. 109, 117 (1984). If two roommates
share a computer and one keeps pirated software on a
shared drive, he might assume that his roommate will not
inform the government. But that person has given up his
privacy with respect to his roommate by saving the soft-
ware on their shared computer.
   A wide variety of often subtle social conventions may
shape expectations about how we act when another
shares with us what is otherwise private, and those con-
ventions go by a variety of labels—courtesy, good man-
ners, custom, protocol, even honor among thieves. The
Constitution, however, protects not these but privacy, and
once privacy has been shared, the shared information,
documents, or places remain private only at the discretion
of the confidant.
                            II
  Our cases reflect this understanding. In United States
v. White, we held that one party to a conversation can
consent to government eavesdropping, and statements
6                  GEORGIA v. RANDOLPH

                   ROBERTS, C. J., dissenting

made by the other party will be admissible at trial. 401
U. S., at 752. This rule is based on privacy: “Inescapably,
one contemplating illegal activities must realize and risk
that his companions may be reporting to the police. . . . [I]f
he has no doubts, or allays them, or risks what doubt he
has, the risk is his.” Ibid.
   The Court has applied this same analysis to objects and
places as well. In Frazier v. Cupp, 394 U. S. 731 (1969), a
duffel bag “was being used jointly” by two cousins. Id., at
740. The Court held that the consent of one was effective
to result in the seizure of evidence used against both: “[I]n
allowing [his cousin] to use the bag and in leaving it in his
house, [the defendant] must be taken to have assumed the
risk that [his cousin] would allow someone else to look
inside.” Ibid.
   As the Court explained in United States v. Jacobsen,
supra:
    “It is well settled that when an individual reveals pri-
    vate information to another, he assumes the risk that
    his confidant will reveal that information to the au-
    thorities, and if that occurs the Fourth Amendment
    does not prohibit governmental use of that informa-
    tion. Once frustration of the original expectation of
    privacy occurs, the Fourth Amendment does not pro-
    hibit governmental use of the now nonprivate infor-
    mation: ‘This Court has held repeatedly that the
    Fourth Amendment does not prohibit the obtaining of
    information revealed to a third party and conveyed by
    him to Government authorities, even if the informa-
    tion is revealed on the assumption that it will be used
    only for a limited purpose and the confidence placed in
    a third party will not be betrayed.’ ” Id., at 117 (quot-
    ing United States v. Miller, 425 U. S. 435, 443 (1976)).
  The same analysis applies to the question whether our
privacy can be compromised by those with whom we share
                 Cite as: 547 U. S. ____ (2006)            7

                   ROBERTS, C. J., dissenting

common living space. If a person keeps contraband in
common areas of his home, he runs the risk that his co-
occupants will deliver the contraband to the police. In
Coolidge v. New Hampshire, 403 U. S. 443 (1971), Mrs.
Coolidge retrieved four of her husband’s guns and the
clothes he was wearing the previous night and handed them
over to police. We held that these items were properly
admitted at trial because “when Mrs. Coolidge of her own
accord produced the guns and clothes for inspection, . . . it
was not incumbent on the police to stop her or avert their
eyes.” Id., at 489.
   Even in our most private relationships, our observable
actions and possessions are private at the discretion of
those around us. A husband can request that his wife not
tell a jury about contraband that she observed in their
home or illegal activity to which she bore witness, but it is
she who decides whether to invoke the testimonial marital
privilege. Trammel v. United States, 445 U. S. 40, 53
(1980). In Trammel, we noted that the former rule prohib-
iting a wife from testifying about her husband’s observable
wrongdoing at his say so “goes far beyond making ‘every
man’s house his castle,’ and permits a person to convert
his house into ‘a den of thieves.’ ” Id., at 51–52 (quoting 5
J. Bentham, Rationale of Judicial Evidence 340 (1827)).
   There is no basis for evaluating physical searches of
shared space in a manner different from how we evaluated
the privacy interests in the foregoing cases, and in fact the
Court has proceeded along the same lines in considering
such searches. In Matlock, police arrested the defendant
in the front yard of a house and placed him in a squad car,
and then obtained permission from Mrs. Graff to search a
shared bedroom for evidence of Matlock’s bank robbery.
415 U. S., at 166. Police certainly could have assumed
that Matlock would have objected were he consulted as he
sat handcuffed in the squad car outside. And in Rodri-
guez, where Miss Fischer offered to facilitate the arrest of
8                     GEORGIA v. RANDOLPH

                       ROBERTS, C. J., dissenting

her sleeping boyfriend by admitting police into an apart-
ment she apparently shared with him, 497 U. S., at 179,
police might have noted that this entry was undoubtedly
contrary to Rodriguez’s social expectations. Yet both of
these searches were reasonable under the Fourth
Amendment because Mrs. Graff had authority, and Miss
Fischer apparent authority, to admit others into areas
over which they exercised control, despite the almost
certain wishes of their present co-occupants.
   The common thread in our decisions upholding searches
conducted pursuant to third-party consent is an under-
standing that a person “assume[s] the risk” that those who
have access to and control over his shared property might
consent to a search. Matlock, 415 U. S., at 171, n. 7. In
Matlock, we explained that this assumption of risk is
derived from a third party’s “joint access or control for
most purposes” of shared property. Ibid. And we con-
cluded that shared use of property makes it “reasonable to
recognize that any of the co-inhabitants has the right to
permit the inspection in his own right.” Ibid.
   In this sense, the risk assumed by a joint occupant is
comparable to the risk assumed by one who reveals pri-
vate information to another. If a person has incriminating
information, he can keep it private in the face of a request
from police to share it, because he has that right under the
Fifth Amendment. If a person occupies a house with
incriminating information in it, he can keep that informa-
tion private in the face of a request from police to search
the house, because he has that right under the Fourth
Amendment. But if he shares the information—or the
house—with another, that other can grant access to the
police in each instance.1
——————
  1 The majority considers this comparison to be a “false equation,” and

even discerns “a deliberate intent to devalue the importance of the
privacy of a dwelling place.” Ante, at 10–11, n. 4. But the differences
                      Cite as: 547 U. S. ____ (2006)                     9

                        ROBERTS, C. J., dissenting

  To the extent a person wants to ensure that his posses-
sions will be subject to a consent search only due to his
own consent, he is free to place these items in an area over
which others do not share access and control, be it a pri-
vate room or a locked suitcase under a bed. Mr. Randolph
acknowledged this distinction in his motion to suppress,
where he differentiated his law office from the rest of the
Randolph house by describing it as an area that “was
solely in his control and dominion.” App. 3. As to a “com-
mon area,” however, co-occupants with “joint access or
control” may consent to an entry and search. Matlock,
supra, at 171, n. 7.
  By emphasizing the objector’s presence and noting an
occupant’s understanding that obnoxious guests might “be
admitted in [one’s] absence,” ante, at 7, the majority ap-
pears to resurrect an agency theory of consent suggested
in our early cases. See Stoner v. California, 376 U. S. 483,
——————
between the majority and this dissent reduce to this: Under the major-
ity’s view, police may not enter and search when an objecting co-
occupant is present at the door, but they may do so when he is asleep in
the next room; under our view, the co-occupant’s consent is effective in
both cases. It seems a bit overwrought to characterize the former
approach as affording great protection to a man in his castle, the latter
as signaling that “the centuries of special protection for the privacy of
the home are over.” Ibid. The Court in United States v. Matlock, 415
U. S. 164 (1974), drew the same comparison the majority faults today,
see id., at 171, n. 7, and the “deliberate intent” the majority ascribes to
this dissent is apparently shared by all Courts of Appeals and the great
majority of State Supreme Courts to have considered the question, see
ante, at 4, n. 1.
   The majority also mischaracterizes this dissent as assuming that
“privacy shared with another individual is privacy waived for all
purposes including warrantless searches by the police.” Ante, at 11,
n. 4. The point, of course, is not that a person waives his privacy by
sharing space with others such that police may enter at will, but that
sharing space necessarily entails a limited yielding of privacy to the
person with whom the space is shared, such that the other person
shares authority to consent to a search of the shared space. See supra,
at 2, 5–10.
10                 GEORGIA v. RANDOLPH

                   ROBERTS, C. J., dissenting

489 (1964) (stating that a hotel clerk could not consent to a
search of a guest’s room because the guest had not waived
his rights “by word or deed, either directly or through an
agent”); Chapman v. United States, 365 U. S. 610, 616–
617 (1961). This agency theory is belied by the facts of
Matlock and Rodriguez—both defendants were present but
simply not asked for consent—and the Court made clear in
those cases that a co-occupant’s authority to consent
rested not on an absent occupant’s delegation of choice to
an agent, but on the consenting co-occupant’s “joint access
or control” of the property. Matlock, supra, at 171, n. 7;
see Rodriguez, supra, at 181; United States v. McAlpine,
919 F. 2d 1461, 1464, n. 2 (CA10 1990) (“[A]gency analysis
[was] put to rest by the Supreme Court’s reasoning in
Matlock”).
  The law acknowledges that although we might not
expect our friends and family to admit the government
into common areas, sharing space entails risk. A person
assumes the risk that his co-occupants—just as they
might report his illegal activity or deliver his contraband
to the government—might consent to a search of areas
over which they have access and control. See United
States v. Karo, 468 U. S. 705, 726 (1984) (O’Connor, J.,
concurring in part and concurring in judgment) (finding it
a “relatively easy case . . . when two persons share identi-
cal, overlapping privacy interests in a particular place,
container, or conversation. Here both share the power to
surrender each other’s privacy to a third party”).
                             III
  The majority states its rule as follows: “[A] warrantless
search of a shared dwelling for evidence over the express
refusal of consent by a physically present resident cannot
be justified as reasonable as to him on the basis of consent
given to the police by another resident.” Ante, at 15–16.
  Just as the source of the majority’s rule is not privacy, so
                  Cite as: 547 U. S. ____ (2006)           11

                   ROBERTS, C. J., dissenting

too the interest it protects cannot reasonably be described as
such. That interest is not protected if a co-owner happens to
be absent when the police arrive, in the backyard gardening,
asleep in the next room, or listening to music through ear-
phones so that only his co-occupant hears the knock on the
door. That the rule is so random in its application confirms
that it bears no real relation to the privacy protected by the
Fourth Amendment. What the majority’s rule protects is
not so much privacy as the good luck of a co-owner who just
happens to be present at the door when the police arrive.
Usually when the development of Fourth Amendment
jurisprudence leads to such arbitrary lines, we take it as a
signal that the rules need to be rethought. See California v.
Acevedo, 500 U. S. 565, 574, 580 (1991). We should not
embrace a rule at the outset that its sponsors appreciate will
result in drawing fine, formalistic lines. See ante, at 17.
   Rather than draw such random and happenstance lines—
and pretend that the Constitution decreed them—the more
reasonable approach is to adopt a rule acknowledging that
shared living space entails a limited yielding of privacy to
others, and that the law historically permits those to whom
we have yielded our privacy to in turn cooperate with the
government. Such a rule flows more naturally from our
cases concerning Fourth Amendment reasonableness and is
logically grounded in the concept of privacy underlying that
Amendment.
   The scope of the majority’s rule is not only arbitrary but
obscure as well. The majority repeats several times that a
present co-occupant’s refusal to permit entry renders the
search unreasonable and invalid “as to him.” Ante, at 1, 15–
16, 18. This implies entry and search would be reasonable
“as to” someone else, presumably the consenting co-occupant
and any other absent co-occupants. The normal Fourth
Amendment rule is that items discovered in plain view are
admissible if the officers were legitimately on the premises;
if the entry and search were reasonable “as to” Mrs.
12                 GEORGIA v. RANDOLPH

                   ROBERTS, C. J., dissenting

Randolph, based on her consent, it is not clear why the
cocaine straw should not be admissible “as to” Mr.
Randolph, as discovered in plain view during a legitimate
search “as to” Mrs. Randolph. The majority’s differentiation
between entry focused on discovering whether domestic
violence has occurred (and the consequent authority to seize
items in plain view), and entry focused on searching for
evidence of other crime, is equally puzzling. See ante, at 13–
14. This Court has rejected subjective motivations of police
officers in assessing Fourth Amendment questions, see
Whren v. United States, 517 U. S. 806, 812–813 (1996), with
good reason: The police do not need a particular reason to
ask for consent to search, whether for signs of domestic
violence or evidence of drug possession.
   While the majority’s rule protects something random, its
consequences are particularly severe. The question pre-
sented often arises when innocent cotenants seek to disasso-
ciate or protect themselves from ongoing criminal activity.
See, e.g., United States v. Hendrix, 595 F. 2d 883, 884
(CADC 1979) (wife asked police “to get her baby and take
[a] sawed-off shotgun out of her house”); People v. Cosme,
48 N. Y. 2d 286, 288–289, 293, 397 N. E. 2d 1319, 1320,
1323 (1979) (woman asked police to remove cocaine and a
gun from a shared closet); United States v. Botsch, 364
F. 2d 542, 547 (CA2 1966). Under the majority’s rule,
there will be many cases in which a consenting co-
occupant’s wish to have the police enter is overridden by
an objection from another present co-occupant. What does
the majority imagine will happen, in a case in which the
consenting co-occupant is concerned about the other’s
criminal activity, once the door clicks shut? The objecting
co-occupant may pause briefly to decide whether to de-
stroy any evidence of wrongdoing or to inflict retribution
on the consenting co-occupant first, but there can be little
doubt that he will attend to both in short order. It is no
answer to say that the consenting co-occupant can depart
                      Cite as: 547 U. S. ____ (2006)                     13

                        ROBERTS, C. J., dissenting

with the police; remember that it is her home, too, and the
other co-occupant’s very presence, which allowed him to
object, may also prevent the consenting co-occupant from
doing more than urging the police to enter.
   Perhaps the most serious consequence of the majority’s
rule is its operation in domestic abuse situations, a context
in which the present question often arises. See Rodriguez,
497 U. S., at 179; United States v. Donlin, 982 F. 2d 31
(CA1 1992); Hendrix, supra; People v. Sanders, 904 P. 2d
1311 (Colo. 1995) (en banc); Brandon v. State, 778 P. 2d
221 (Alaska App. 1989). While people living together
might typically be accommodating to the wishes of their
cotenants, requests for police assistance may well come
from coinhabitants who are having a disagreement. The
Court concludes that because “no sensible person would go
inside” in the face of disputed consent, ante, at 8–9, and
the consenting cotenant thus has “no recognized author-
ity” to insist on the guest’s admission, ante, at 10, a “police
officer [has] no better claim to reasonableness in entering
than the officer would have in the absence of any consent
at all,” ibid. But the police officer’s superior claim to enter
is obvious: Mrs. Randolph did not invite the police to join
her for dessert and coffee; the officer’s precise purpose in
knocking on the door was to assist with a dispute between
the Randolphs—one in which Mrs. Randolph felt the need
for the protective presence of the police. The majority’s
rule apparently forbids police from entering to assist with
a domestic dispute if the abuser whose behavior prompted
the request for police assistance objects.2
——————
   2 In response to this concern, the majority asserts that its rule applies

“merely [to] evidentiary searches.” Ante, at 14. But the fundamental
premise of the majority’s argument is that an inviting co-occupant has
“no recognized authority” to “open the door” over a co-occupant’s objec-
tion. Ante, at 10; see also ante, at 1 (“[A] physically present co-
occupant’s stated refusal to permit entry prevails, rendering the war-
rantless search unreasonable and invalid as to him” (emphasis added));
14                     GEORGIA v. RANDOLPH

                       ROBERTS, C. J., dissenting

   The majority acknowledges these concerns, but dis-
misses them on the ground that its rule can be expected to
give rise to exigent situations, and police can then rely on
an exigent circumstances exception to justify entry. Ante,
at 12, n. 6. This is a strange way to justify a rule, and the
fact that alternative justifications for entry might arise
does not show that entry pursuant to consent is unreason-
able. In addition, it is far from clear that an exception for
emergency entries suffices to protect the safety of occu-
pants in domestic disputes. See, e.g., United States v.
Davis, 290 F. 3d 1239, 1240–1241 (CA10 2002) (finding no
exigent circumstances justifying entry when police re-
sponded to a report of domestic abuse, officers heard no
noise upon arrival, defendant told officers that his wife
was out of town, and wife then appeared at the door seem-
ingly unharmed but resisted husband’s efforts to close the
door).
   Rather than give effect to a consenting spouse’s author-
ity to permit entry into her house to avoid such situations,
the majority again alters established Fourth Amendment
rules to defend giving veto power to the objecting spouse.
In response to the concern that police might be turned
away under its rule before entry can be justified based on
exigency, the majority creates a new rule: A “good reason”
to enter, coupled with one occupant’s consent, will ensure
——————
ante, at 8 (“[A] caller standing at the door of shared premises would
have no confidence . . . to enter when a fellow tenant stood there saying
‘stay out’ ” (emphasis added)); ante, at 10 (“[A] disputed invitation,
without more, gives a police officer no . . . claim to reasonableness in
entering” (emphasis added)). The point is that the majority’s rule
transforms what may have begun as a request for consent to conduct an
evidentiary search into something else altogether, by giving veto power
over the consenting co-occupant’s wishes to an occupant who would
exclude the police from entry. The majority would afford the now quite
vulnerable consenting co-occupant sufficient time to gather her belong-
ings and leave, see ante, at 13, apparently putting to one side the fact
that it is her castle, too.
                 Cite as: 547 U. S. ____ (2006)           15

                   ROBERTS, C. J., dissenting

that a police officer is “lawfully in the premises.” Ante, at
13, 14. As support for this “consent plus a good reason”
rule, the majority cites a treatise, which itself refers only
to emergency entries. Ante, at 14 (citing 4 W. LaFave,
Search and Seizure §8.3(d), p. 161 (4th ed. 2004)). For the
sake of defending what it concedes are fine, formalistic
lines, the majority spins out an entirely new framework
for analyzing exigent circumstances. Police may now
enter with a “good reason” to believe that “violence (or
threat of violence) has just occurred or is about to (or soon
will) occur.” Ante, at 13–14. And apparently a key factor
allowing entry with a “good reason” short of exigency is
the very consent of one co-occupant the majority finds so
inadequate in the first place.
   The majority’s analysis alters a great deal of established
Fourth Amendment law. The majority imports the con-
cept of “social expectations,” previously used only to de-
termine when a search has occurred and whether a par-
ticular person has standing to object to a search, into
questions of consent. Ante, at 6, 8. To determine whether
entry and search are reasonable, the majority considers a
police officer’s subjective motive in asking for consent,
which we have otherwise refrained from doing in assess-
ing Fourth Amendment questions. Ante, at 13–14. And
the majority creates a new exception to the warrant re-
quirement to justify warrantless entry short of exigency in
potential domestic abuse situations. Ibid.
   Considering the majority’s rule is solely concerned with
protecting a person who happens to be present at the door
when a police officer asks his co-occupant for consent to
search, but not one who is asleep in the next room or in
the backyard gardening, the majority has taken a great
deal of pain in altering Fourth Amendment doctrine, for
precious little (if any) gain in privacy. Perhaps one day, as
the consequences of the majority’s analytic approach
become clearer, today’s opinion will be treated the same
16                 GEORGIA v. RANDOLPH

                    ROBERTS, C. J., dissenting

way the majority treats our opinions in Matlock and Rod-
riguez—as a “loose end” to be tied up. Ante, at 17.
   One of the concurring opinions states that if it had to
choose between a rule that a cotenant’s consent was valid or
a rule that it was not, it would choose the former. Ante, at 1
(opinion of BREYER, J.). The concurrence advises, however,
that “no single set of legal rules can capture the ever chang-
ing complexity of human life,” ibid., and joins what becomes
the majority opinion, “[g]iven the case-specific nature of the
Court’s holding,” ante, at 3. What the majority establishes,
in its own terms, is “the rule that a physically present in-
habitant’s express refusal of consent to a police search is
dispositive as to him, regardless of the consent of a fellow
occupant.” Ante, at 18 (emphases added). The concurrence
joins with the apparent “understandin[g]” that the major-
ity’s “rule” is not a rule at all, but simply a “case-specific”
holding. Ante, at 3 (opinion of BREYER, J.). The end result
is a complete lack of practical guidance for the police in the
field, let alone for the lower courts.
                         *     *    *
  Our third-party consent cases have recognized that a
person who shares common areas with others “assume[s]
the risk that one of their number might permit the common
area to be searched.” Matlock, 415 U. S., at 171, n. 7. The
majority reminds us, in high tones, that a man’s home is his
castle, ante, at 10, but even under the majority’s rule, it is
not his castle if he happens to be absent, asleep in the keep,
or otherwise engaged when the constable arrives at the
gate. Then it is his co-owner’s castle. And, of course, it is
not his castle if he wants to consent to entry, but his co-
owner objects. Rather than constitutionalize such an arbi-
trary rule, we should acknowledge that a decision to share
a private place, like a decision to share a secret or a confi-
dential document, necessarily entails the risk that those
with whom we share may in turn choose to share—for their
                 Cite as: 547 U. S. ____ (2006)        17

                   ROBERTS, C. J., dissenting

own protection or for other reasons—with the police.
  I respectfully dissent.
                  Cite as: 547 U. S. ____ (2006)             1

                      SCALIA, J., dissenting

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 04–1067
                          _________________


 GEORGIA, PETITIONER v. SCOTT FITZ RANDOLPH
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF
                       GEORGIA
                        [March 22, 2006]

   JUSTICE SCALIA, dissenting.
   I join the dissent of THE CHIEF JUSTICE, but add these
few words in response to JUSTICE STEVENS’ concurrence.
   It is not as clear to me as it is to JUSTICE STEVENS that,
at the time the Fourth Amendment was adopted, a police
officer could enter a married woman’s home over her
objection, and could not enter with only her consent. Nor
is it clear to me that the answers to these questions de-
pended solely on who owned the house. It is entirely clear,
however, that if the matter did depend solely on property
rights, a latter-day alteration of property rights would also
produce a latter-day alteration of the Fourth Amendment
outcome—without altering the Fourth Amendment itself.
   JUSTICE STEVENS’ attempted critique of originalism
confuses the original import of the Fourth Amendment
with the background sources of law to which the Amend-
ment, on its original meaning, referred. From the date of
its ratification until well into the 20th century, violation of
the Amendment was tied to common-law trespass. See
Kyllo v. United States, 533 U. S. 27, 31–32 (2001); see also
California v. Acevedo, 500 U. S. 565, 581, 583 (1991)
(SCALIA, J., concurring in judgment). On the basis of that
connection, someone who had power to license the search
of a house by a private party could authorize a police
search. See 1 Restatement of Torts §167, and Comment b
(1934); see also Williams v. Howard, 110 S. C. 82, 96 S. E.
2                  GEORGIA v. RANDOLPH

                     SCALIA, J., dissenting

251 (1918); Fennemore v. Armstrong, 29 Del. 35, 96 A. 204
(Super. Ct. 1915). The issue of who could give such con-
sent generally depended, in turn, on “historical and legal
refinements” of property law. United States v. Matlock,
415 U. S. 164, 171, n. 7 (1974). As property law developed,
individuals who previously could not authorize a search
might become able to do so, and those who once could grant
such consent might no longer have that power. But changes
in the law of property to which the Fourth Amendment
referred would not alter the Amendment’s meaning: that
anyone capable of authorizing a search by a private party
could consent to a warrantless search by the police.
   There is nothing new or surprising in the proposition
that our unchanging Constitution refers to other bodies of
law that might themselves change. The Fifth Amendment
provides, for instance, that “private property” shall not “be
taken for public use, without just compensation”; but it
does not purport to define property rights. We have con-
sistently held that “the existence of a property interest is
determined by reference to ‘existing rules or understand-
ings that stem from an independent source such as state
law.’ ” Phillips v. Washington Legal Foundation, 524 U. S.
156, 164 (1998) (quoting Board of Regents of State Colleges
v. Roth, 408 U. S. 564, 577 (1972)). The same is true of the
Fourteenth Amendment Due Process Clause’s protection of
“property.” See Castle Rock v. Gonzales, 545 U. S. ___, ___
(2005). This reference to changeable law presents no prob-
lem for the originalist. No one supposes that the meaning of
the Constitution changes as States expand and contract
property rights. If it is indeed true, therefore, that a wife
in 1791 could not authorize the search of her husband’s
house, the fact that current property law provides other-
wise is no more troublesome for the originalist than the
well established fact that a State must compensate its
takings of even those property rights that did not exist at
the time of the Founding.
                 Cite as: 547 U. S. ____ (2006)          3

                     SCALIA, J., dissenting

  In any event, JUSTICE STEVENS’ panegyric to the equal
rights of women under modern property law does not
support his conclusion that “[a]ssuming . . . both spouses
are competent, neither one is a master possessing the
power to override the other’s constitutional right to deny
entry to their castle.” Ante, at 2–3. The issue at hand is
what to do when there is a conflict between two equals.
Now that women have authority to consent, as JUSTICE
STEVENS claims men alone once did, it does not follow that
the spouse who refuses consent should be the winner of the
contest. JUSTICE STEVENS could just as well have followed
the same historical developments to the opposite conclu-
sion: Now that “the male and the female are equal part-
ners,” ante, at 2, and women can consent to a search of
their property, men can no longer obstruct their wishes.
Men and women are no more “equal” in the majority’s
regime, where both sexes can veto each other’s consent,
than on the dissent’s view, where both sexes cannot.
  Finally, I must express grave doubt that today’s decision
deserves JUSTICE STEVENS’ celebration as part of the
forward march of women’s equality. Given the usual
patterns of domestic violence, how often can police be
expected to encounter the situation in which a man urges
them to enter the home while a woman simultaneously
demands that they stay out? The most common practical
effect of today’s decision, insofar as the contest between
the sexes is concerned, is to give men the power to stop
women from allowing police into their homes—which is,
curiously enough, precisely the power that JUSTICE
STEVENS disapprovingly presumes men had in 1791.
                 Cite as: 547 U. S. ____ (2006)           1

                    THOMAS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 04–1067
                         _________________


 GEORGIA, PETITIONER v. SCOTT FITZ RANDOLPH
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF
                       GEORGIA
                       [March 22, 2006]

  JUSTICE THOMAS, dissenting.
  The Court has long recognized that “[i]t is an act of
responsible citizenship for individuals to give whatever
information they may have to aid in law enforcement.”
Miranda v. Arizona, 384 U. S. 436, 477–478 (1966). Con-
sistent with this principle, the Court held in Coolidge v.
New Hampshire, 403 U. S. 443 (1971), that no Fourth
Amendment search occurs where, as here, the spouse of an
accused voluntarily leads the police to potential evidence
of wrongdoing by the accused. Id., at 486–490. Because
Coolidge squarely controls this case, the Court need not
address whether police could permissibly have conducted a
general search of the Randolph home, based on Mrs.
Randolph’s consent. I respectfully dissent.
  In the instant case, Mrs. Randolph told police respond-
ing to a domestic dispute that respondent was using a
substantial quantity of cocaine. Upon police request, she
consented to a general search of her residence to investi-
gate her statements. However, as the Court’s recitation of
the facts demonstrates, ante, at 2, the record is clear that
no such general search occurred. Instead, Sergeant Brett
Murray asked Mrs. Randolph where the cocaine was
located, and she showed him to an upstairs bedroom,
where he saw the “piece of cut straw” on a dresser. Cor-
rected Tr. of Motion to Suppression Hearing in Case No.
2001R–699 (Super. Ct. Sumter Cty., Ga., Oct. 3, 2002), pp.
2                 GEORGIA v. RANDOLPH

                    THOMAS, J., dissenting

8–9. Upon closer examination, Sergeant Murray observed
white residue on the straw, and concluded the straw had
been used for ingesting cocaine. Id., at 8. He then col-
lected the straw and the residue as evidence. Id., at 9.
   Sergeant Murray’s entry into the Randolphs’ home at
the invitation of Mrs. Randolph to be shown evidence of
respondent’s cocaine use does not constitute a Fourth
Amendment search. Under this Court’s precedents, only
the action of an agent of the government can constitute a
search within the meaning of the Fourth Amendment,
because that Amendment “was intended as a restraint
upon the activities of sovereign authority, and was not
intended to be a limitation upon other than governmental
agencies.” Burdeau v. McDowell, 256 U. S. 465, 475 (1921)
(emphasis added). See also Coolidge, 403 U. S., at 487.
Applying this principle in Coolidge, the Court held that
when a citizen leads police officers into a home shared
with her spouse to show them evidence relevant to their
investigation into a crime, that citizen is not acting as an
agent of the police, and thus no Fourth Amendment search
has occurred. Id., at 488–498.
   Review of the facts in Coolidge clearly demonstrates
that it governs this case. While the police interrogated
Coolidge as part of their investigation into a murder, two
other officers were sent to his house to speak with his
wife. Id., at 485. During the course of questioning Mrs.
Coolidge, the police asked whether her husband owned
any guns. Id., at 486. Mrs. Coolidge replied in the af-
firmative, and offered to retrieve the weapons for the
police, apparently operating under the assumption that
doing so would help to exonerate her husband. Ibid. The
police accompanied Mrs. Coolidge to the bedroom to collect
the guns, as well as clothing that Mrs. Coolidge told them
her husband had been wearing the night of the murder.
Ibid.
   Before this Court, Coolidge argued that the evidence of
                     Cite as: 547 U. S. ____ (2006)                     3

                         THOMAS, J., dissenting

the guns and clothing should be suppressed as the product
of an unlawful search because Mrs. Coolidge was acting as
an “ ‘instrument,’ ” or agent, of the police by complying
with a “ ‘demand’ ” made by them. Id., at 487. The Court
recognized that, had Mrs. Coolidge sought out the guns to
give to police wholly on her own initiative, “there can be no
doubt under existing law that the articles would later
have been admissible in evidence.” Ibid. That she did so
in cooperation with police pursuant to their request did
not transform her into their agent; after all, “it is no part
of the policy underlying the Fourth and Fourteenth
Amendments to discourage citizens from aiding to the
utmost of their ability in the apprehension of criminals.”
Id., at 488. Because the police were “acting normally and
properly” when they asked about any guns, and question-
ing Mrs. Coolidge about the clothing was “logical and in no
way coercive,” the Fourth Amendment did not require
police to “avert their eyes” when Mrs. Coolidge produced
the guns and clothes for inspection.1 Id., at 488–489.
   This case is indistinguishable from Coolidge, compelling
the conclusion that Mrs. Randolph was not acting as an
agent of the police when she admitted Sergeant Murray
into her home and led him to the incriminating evidence.2
——————
  1 Although  the Court has described Coolidge as a “third-party con-
sent” case, United States v. Matlock, 415 U. S. 164, 171 (1974), the
Court’s opinion, by its own terms, does not rest on its conception of Mrs.
Coolidge’s authority to consent to a search of her house or the possible
relevance of Mr. Coolidge’s absence from the scene. Coolidge, 403 U. S.,
at 487 (“[W]e need not consider the petitioner’s further argument that
Mrs. Coolidge could not or did not ‘waive’ her husband’s constitutional
protection against unreasonable searches and seizures”). See also
Walter v. United States, 447 U. S. 649, 660–661, n. 2 (1980) (White, J.,
concurring in part and concurring in judgment) (“Similarly, in Coolidge
v. New Hampshire, the Court held that a wife’s voluntary action in
turning over to police her husband’s guns and clothing did not consti-
tute a search and seizure by the government”).
  2 The Courts of Appeals have disagreed over the appropriate inquiry
4                     GEORGIA v. RANDOLPH

                        THOMAS, J., dissenting

Just as Mrs. Coolidge could, of her own accord, have of-
fered her husband’s weapons and clothing to the police
without implicating the Fourth Amendment, so too could
Mrs. Randolph have simply retrieved the straw from the
house and given it to Sergeant Murray. Indeed, the ma-
jority appears to concede as much. Ante, at 11-12 (“The co-
tenant acting on his own initiative may be able to deliver
evidence to the police, Coolidge, supra, at 487–489 . . . ,
and can tell the police what he knows, for use before a
magistrate in getting a warrant”). Drawing a constitu-
tionally significant distinction between what occurred here
and Mrs. Randolph’s independent production of the rele-
vant evidence is both inconsistent with Coolidge and
unduly formalistic.3
   Accordingly, the trial court appropriately denied re-
spondent’s motion to suppress the evidence Mrs. Randolph
provided to the police and the evidence obtained as a
result of the consequent search warrant. I would therefore
reverse the judgment of the Supreme Court of Georgia.




——————
to be performed in determining whether involvement of the police
transforms a private individual into an agent or instrument of the
police. See United States v. Pervaz, 118 F. 3d 1, 5–6 (CA1 1997) (sum-
marizing approaches of various Circuits). The similarity between this
case and Coolidge avoids any need to resolve this broader dispute in the
present case.
  3 That Sergeant Murray, unlike the officers in Coolidge, may have

intended to perform a general search of the house is inconsequential, as
he ultimately did not do so; he viewed only those items shown to him by
Mrs. Randolph. Nor is it relevant that, while Mrs. Coolidge intended to
aid the police in apprehending a criminal because she believed doing so
would exonerate her husband, Mrs. Randolph believed aiding the police
would implicate her husband.

```

---

## GROUP: content/cases/Gerstein v. Pugh.md  (`case`, 6 assertions)

### content_page

```
---
title: "Gerstein v. Pugh"
type: case
citation: "420 U.S. 103 (1975)"
parallel_cite: "95 S. Ct. 854; 43 L. Ed. 2d 54; 19 Fed. R. Serv. 2d 1499"
neutral_cite: 1975 U.S. LEXIS 29
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1975
date_decided: 1975-02-18
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1975-02-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Gerstein v. Pugh
  varies_by_point: false
  scope_note: "Good law. The Fourth Amendment requires a prompt judicial determination of probable cause as a prerequisite to extended pretrial detention of a person arrested without a warrant; the determination need not be adversarial. Implemented by County of Riverside v. McLaughlin (48-hour presumption)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109186/gerstein-v-pugh/"
  cluster_id: 109186
  opinion_id: 9425988
  identity_checked: true
homes:
  - page: "[[Prompt Probable-Cause Determination]]"
    role: "Key — Anchor (prompt judicial PC determination after a warrantless arrest)"
  - page: "[[Seizure of the Person]]"
    role: "Related (cross-doctrine)"
related: ["[[County of Riverside v. McLaughlin]]", "[[Coolidge v. New Hampshire]]", "[[Payton v. New York]]"]
aliases: []
tags: ["case", "fourth-amendment", "arrest", "probable-cause", "pretrial-detention", "gerstein-hearing"]
holding: "A person arrested without a warrant is entitled under the Fourth Amendment to a prompt judicial determination of probable cause as a prerequisite to any extended pretrial restraint of liberty; the determination need not be an adversary hearing."
lake:
  record_id: Gerstein v. Pugh
  status: verified
  projected_at: 2026-07-09
---

# Gerstein v. Pugh

*420 U.S. 103 (1975)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Under Florida procedure, a person arrested without a warrant and charged by a prosecutor's information could be jailed or otherwise restrained pending trial without any judicial determination of probable cause. Pugh and other detainees, held on informations without any such hearing, brought a class action challenging the practice. The State defended on the ground that the prosecutor's decision to file an information was itself a sufficient determination of probable cause to justify detention.

## Issue
Whether the Fourth Amendment requires a judicial determination of probable cause before a person arrested without a warrant may be subjected to extended pretrial detention, and if so, whether that determination must take the form of an adversary hearing.

## Rule
A prompt judicial probable-cause determination is required. An officer's on-scene probable cause justifies the arrest and a brief booking detention, but not prolonged custody: "a policeman's on-the-scene assessment of probable cause provides legal justification for arresting a person suspected of crime, and for a brief period of detention to take the administrative steps incident to arrest. Once the suspect is in custody, however, the reasons that justify dispensing with the magistrate's neutral judgment evaporate." — 420 U.S. at 113–114. ^pin-113

"Accordingly, we hold that the Fourth Amendment requires a judicial determination of probable cause as a prerequisite to extended restraint of liberty following arrest." — [*Id.* at 114](https://www.courtlistener.com/opinion/109186/gerstein-v-pugh/#:~:text=Accordingly%2C%20we%20hold%20that%20the). ^pin-114

The hearing may be informal and need not be adversarial, but it must be prompt: "it must provide a fair and reliable determination of probable cause as a condition for any significant pretrial restraint of liberty, and this determination must be made by a judicial officer either before or promptly after arrest." — *Id.* at 125. ^pin-125

## Application
Florida's reliance on the prosecutor's information could not satisfy the Fourth Amendment, because a prosecutor — charged with law enforcement — is not the "neutral and detached" magistrate the Constitution requires (per *[[Coolidge v. New Hampshire|Coolidge]]* and *Shadwick*). A warrantless arrestee held only on an information therefore received no constitutionally adequate probable-cause check. The Court required a prompt judicial determination but rejected the District Court's decree to the extent it demanded a full adversary hearing, holding the probable-cause determination need not afford counsel, confrontation, or cross-examination.

## Conclusion
The Fourth Amendment requires a timely judicial determination of probable cause as a prerequisite to extended pretrial detention of a warrantless arrestee, so Florida's information-only procedure was invalid; but because the determination need not be adversarial, the judgment was affirmed in part and reversed in part. This requirement is the "Gerstein hearing."

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Gerstein*'s "promptly after arrest" requirement is implemented by [[County of Riverside v. McLaughlin]], which set a presumptive 48-hour window for the judicial probable-cause determination. The neutral-magistrate principle traces to [[Coolidge v. New Hampshire]]; *Gerstein* concerns post-arrest detention and is distinct from the in-home arrest-warrant rule of [[Payton v. New York]].

## Appears on
- [[Prompt Probable-Cause Determination]] — *Key — Anchor*
- [[Seizure of the Person]] — *Related (cross-doctrine)*

## Sources
- *Gerstein v. Pugh*, 420 U.S. 103 (1975) — https://www.courtlistener.com/opinion/109186/gerstein-v-pugh/ — pinpoints: 113–114, 125.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1527afdccd054ed2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "420 U.S. 103 (1975)", "court": "U.S. Supreme Court", "neutral_cite": "1975 U.S. LEXIS 29", "official_citation_present": true, "parallel_cite": "95 S. Ct. 854; 43 L. Ed. 2d 54; 19 Fed. R. Serv. 2d 1499", "title": "Gerstein v. Pugh", "year": "1975"}}
{"assertion_id": "5a609c352973ad02", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Related (cross-doctrine)", "title": "Gerstein v. Pugh"}}
{"assertion_id": "66ff711416daec78", "dimension": "support", "kind": "home_role", "locator": {"home": "Prompt Probable-Cause Determination"}, "payload": {"home": "Prompt Probable-Cause Determination", "role": "Key — Anchor (prompt judicial PC determination after a warrantless arrest)", "title": "Gerstein v. Pugh"}}
{"assertion_id": "c51e973e7f547e00", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A person arrested without a warrant is entitled under the Fourth Amendment to a prompt judicial determination of probable cause as a prerequisite to any extended pretrial restraint of liberty; the determination need not be an adversary hearing.", "title": "Gerstein v. Pugh"}}
{"assertion_id": "31c919b9b982f059", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Gerstein v. Pugh"}}
{"assertion_id": "6a5266da72d6af73", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1975-02-18", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Gerstein v. Pugh", "field_i_validity": "good_law", "scope_note": "Good law. The Fourth Amendment requires a prompt judicial determination of probable cause as a prerequisite to extended pretrial detention of a person arrested without a warrant; the determination need not be adversarial. Implemented by County of Riverside v. McLaughlin (48-hour presumption).", "title": "Gerstein v. Pugh", "varies_by_point": "false"}}
```

### lake record — Gerstein v. Pugh

```json
{
  "schema_version": "s2.v1",
  "record_id": "Gerstein v. Pugh",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Gerstein v. Pugh",
    "case_name_short": "Gerstein",
    "case_name_full": "GERSTEIN v. PUGH Et Al.",
    "input_case_name": "Gerstein v. Pugh",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1975-02-18",
    "year": 1975,
    "docket": null,
    "cluster_id": 109186,
    "lead_opinion_id": 9425988,
    "sibling_ids": [
      109186,
      9425988,
      9425989
    ],
    "absolute_url": "/opinion/109186/gerstein-v-pugh/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "420 U.S. 103",
      "volume": "420",
      "reporter": "U.S.",
      "page": "103",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "95 S. Ct. 854",
        "volume": "95",
        "reporter": "S. Ct.",
        "page": "854",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "43 L. Ed. 2d 54",
        "volume": "43",
        "reporter": "L. Ed. 2d",
        "page": "54",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "19 Fed. R. Serv. 2d 1499",
        "volume": "19",
        "reporter": "Fed. R. Serv. 2d",
        "page": "1499",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1975 U.S. LEXIS 29",
        "volume": "1975",
        "reporter": "U.S. LEXIS",
        "page": "29",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "420 U.S. 103",
        "volume": "420",
        "reporter": "U.S.",
        "page": "103",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "95 S. Ct. 854",
        "volume": "95",
        "reporter": "S. Ct.",
        "page": "854",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "43 L. Ed. 2d 54",
        "volume": "43",
        "reporter": "L. Ed. 2d",
        "page": "54",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1975 U.S. LEXIS 29",
        "volume": "1975",
        "reporter": "U.S. LEXIS",
        "page": "29",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "19 Fed. R. Serv. 2d 1499",
        "volume": "19",
        "reporter": "Fed. R. Serv. 2d",
        "page": "1499",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "420 U.S. 103",
    "official_selection": {
      "court_class": "scotus",
      "selected": "420 U.S. 103",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-113",
      "page": null,
      "quote": "--- # Gerstein v. Pugh *420 U.S. 103 (1975)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Under Florida procedure, a person arrested without a warrant and charged by a prosecutor's information could be jailed or otherwise restrained pending trial without any judicial determination of probable cause. Pugh and other detainees, held on informations without any such hearing, brought a class action challenging the practice. The State defended on the ground that the prosecutor's decision to file an information was itself a sufficient determination of probable cause to justify detention. ## Issue Whether the Fourth Amendment requires a judicial determination of probable cause before a person arrested without a warrant may be subjected to extended pretrial detention, and if so, whether that determination must take the form of an adversary hearing. ## Rule A prompt judicial probable-cause determination is required. An officer's on-scene probable cause justifies the arrest and a brief booking detention, but not prolonged custody:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-114",
      "page": null,
      "quote": "Accordingly, we hold that the Fourth Amendment requires a judicial determination of probable cause as a prerequisite to extended restraint of liberty following arrest.",
      "star_marker": "114",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 17194,
      "fragment": "#:~:text=Accordingly%2C%20we%20hold%20that%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-125",
      "page": null,
      "quote": "it must provide a fair and reliable determination of probable cause as a condition for any significant pretrial restraint of liberty, and this determination must be made by a judicial officer either before or promptly after arrest.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1975-02-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Gerstein v. Pugh",
    "varies_by_point": false,
    "scope_note": "Good law. The Fourth Amendment requires a prompt judicial determination of probable cause as a prerequisite to extended pretrial detention of a person arrested without a warrant; the determination need not be adversarial. Implemented by County of Riverside v. McLaughlin (48-hour presumption).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Winegarner",
          "cluster_id": 9372588,
          "cite": [
            "208 N.E.3d 88",
            "2023 Ohio 319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Preston P., a juvenile",
          "cluster_id": 4692950,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane1_negative"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Salerno",
          "cluster_id": 111891,
          "cite": [
            "95 L. Ed. 2d 697",
            "107 S. Ct. 2095",
            "481 U.S. 739",
            "1987 U.S. LEXIS 2259",
            "55 U.S.L.W. 4663"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hewitt v. Helms",
          "cluster_id": 110829,
          "cite": [
            "74 L. Ed. 2d 675",
            "103 S. Ct. 864",
            "459 U.S. 460",
            "1983 U.S. LEXIS 3",
            "51 U.S.L.W. 4124"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Middlesex County Ethics Committee v. Garden State Bar Ass'n",
          "cluster_id": 110750,
          "cite": [
            "73 L. Ed. 2d 116",
            "102 S. Ct. 2515",
            "457 U.S. 423",
            "1982 U.S. LEXIS 2638",
            "50 U.S.L.W. 4712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ingraham v. Wright",
          "cluster_id": 109635,
          "cite": [
            "51 L. Ed. 2d 711",
            "97 S. Ct. 1401",
            "430 U.S. 651",
            "1977 U.S. LEXIS 74"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilkinson v. Austin",
          "cluster_id": 799975,
          "cite": [
            "162 L. Ed. 2d 174",
            "125 S. Ct. 2384",
            "545 U.S. 209",
            "2005 U.S. LEXIS 4839"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reno v. Flores",
          "cluster_id": 112833,
          "cite": [
            "123 L. Ed. 2d 1",
            "113 S. Ct. 1439",
            "507 U.S. 292",
            "1993 U.S. LEXIS 2399"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States Parole Commission v. Geraghty",
          "cluster_id": 110228,
          "cite": [
            "63 L. Ed. 2d 479",
            "100 S. Ct. 1202",
            "445 U.S. 388",
            "1980 U.S. LEXIS 12",
            "29 Fed. R. Serv. 2d 20"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murphy v. Hunt",
          "cluster_id": 110660,
          "cite": [
            "71 L. Ed. 2d 353",
            "102 S. Ct. 1181",
            "455 U.S. 478",
            "1982 U.S. LEXIS 77"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vasquez v. Hillery",
          "cluster_id": 111552,
          "cite": [
            "88 L. Ed. 2d 598",
            "106 S. Ct. 617",
            "474 U.S. 254",
            "1986 U.S. LEXIS 40",
            "54 U.S.L.W. 4068"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County of Riverside v. McLaughlin",
          "cluster_id": 112585,
          "cite": [
            "114 L. Ed. 2d 49",
            "111 S. Ct. 1661",
            "500 U.S. 44",
            "1991 U.S. LEXIS 2528"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Castaneda v. Partida",
          "cluster_id": 109627,
          "cite": [
            "51 L. Ed. 2d 498",
            "97 S. Ct. 1272",
            "430 U.S. 482",
            "1977 U.S. LEXIS 67"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moore v. Sims",
          "cluster_id": 110105,
          "cite": [
            "60 L. Ed. 2d 994",
            "99 S. Ct. 2371",
            "442 U.S. 415",
            "1979 U.S. LEXIS 110"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109186 OR 9425988 OR 9425989) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTI3NTUyMDAwMDAwJnM9NDUwMjIxMCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109186+OR+9425988+OR+9425989%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109186 OR 9425988 OR 9425989)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05ODcmcz0xMTE1OTgmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109186+OR+9425988+OR+9425989%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109186 OR 9425988 OR 9425989)",
        "reviewed": 83,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 83,
        "triage_read": 0,
        "triage_snippet_classified": 83
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109186 OR 9425988 OR 9425989)",
    "indexed_citing_opinions": 2518,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109186,
        "count": 2222,
        "count_source": "search"
      },
      {
        "opinion_id": 9425988,
        "count": 333,
        "count_source": "search"
      },
      {
        "opinion_id": 9425989,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4362,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/gerstein-v-pugh.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxNzAwMjcmcz0xMDMxNDQ2MCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109186+OR+9425988+OR+9425989%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109186,
        "cited_id": 91470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 91772,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 97944,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 98209,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 100977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 101974,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 104937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 104977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 105594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 106087,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 106391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 106534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 107058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 107394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108266,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108341,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108772,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108785,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 109023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 109097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 109128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 109136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 109137,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 279699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 286155,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 296631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 306786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 313021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1447830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1624670,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1628605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1720793,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1724472,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1725389,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1764878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1795762,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1807359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1843924,
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
    "date_created": "2026-07-05T05:22:22Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:22:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:22:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:27:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:22:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Gerstein v. Pugh

```
<opinion type="majority">
<author id="b191-4"><page-number citation-index="1" label="105">*105</page-number>Mr. Justice Powell</author>
<p id="AnR">delivered the opinion of the Court.</p>
<p id="b191-5">The issue in this case is whether a person arrested and held for trial under a prosecutor’s information is constitutionally entitled to a judicial determination of probable cause for pretrial restraint of liberty.</p>
<p id="b191-6">I</p>
<p id="b191-7">In March 1971 respondents Pugh and Henderson were arrested in Dade County, Fla. Each was charged with several offenses under a prosecutor’s information.<footnotemark>1</footnotemark> Pugh was denied bail because one of the charges against him carried a potential life sentence, and Henderson remained in custody because he was unable to post a $4,500 bond.</p>
<p id="b191-8">In Florida, indictments are required only for prosecution of capital offenses. Prosecutors may charge all other crimes by information, without a prior preliminary hearing and without obtaining leave of court. Fla. Rule Crim. Proc. 3.140 (a); <em>State </em>v. <em>Hernandez, </em><span class="citation" data-id="1628605"><a href="/opinion/1628605/state-v-hernandez/" aria-description="Citation for case: State v. Hernandez">217 So. 2d 109</a></span> (Fla. 1968); <em>Di Bona </em>v. <em>State, </em><span class="citation" data-id="1720793"><a href="/opinion/1720793/di-bona-v-state/" aria-description="Citation for case: Di Bona v. State">121 So. 2d 192</a></span> (Fla. App. 1960). At the time respondents were arrested, a Florida rule seemed to authorize adversary preliminary hearings to test probable cause for detention in all cases. Fla. Rule Crim. Proc. 1.122 (before amendment in 1972). <page-number citation-index="1" label="106">*106</page-number>But the Florida courts had held that the filing of an information foreclosed the suspect’s right to a preliminary-hearing. See <em>State ex rel. Hardy </em>v. <em>Blount, </em><span class="citation" data-id="1764878"><a href="/opinion/1764878/state-ex-rel-hardy-v-blount/" aria-description="Citation for case: State Ex Rel. Hardy v. Blount">261 So. 2d 172</a></span> (Fla. 1972).<footnotemark>2</footnotemark> They had also held that habeas corpus could not be used, except perhaps in exceptional circumstances, to test the probable cause for detention under an information. See <em>Sullivan </em>v. <em>State ex rel. McCrory, </em><span class="citation" data-id="1843924"><a href="/opinion/1843924/sullivan-v-state-ex-rel-mccrory/#797" aria-description="Citation for case: Sullivan v. State Ex Rel. McCrory">49 So. 2d 794, 797</a></span> (Fla. 1951). The only possible methods for obtaining a judicial determination of probable cause were a special statute allowing a preliminary hearing after 30 days, <span class="citation no-link">Fla. Stat. Ann. §907.045</span> (1973),<footnotemark>3</footnotemark> and arraignment, which the District Court found was often delayed a month or more after arrest. <em>Pugh </em>v. <em>Rainwater, </em><span class="citation" data-id="1624670"><a href="/opinion/1624670/pugh-v-rainwater/#1110" aria-description="Citation for case: Pugh v. Rainwater">332 F. Supp. 1107, 1110</a></span> (SD Fla. 1971).<footnotemark>4</footnotemark> As a result, a person charged by information could be detained for a substantial period solely on the decision of a prosecutor.</p>
<p id="b192-5">Respondents Pugh and Henderson filed a class action against Dade County officials in the Federal District <page-number citation-index="1" label="107">*107</page-number>Court,<footnotemark>5</footnotemark> claiming a constitutional right to a judicial hearing on the issue of probable cause and requesting declaratory and injunctive relief.<footnotemark>6</footnotemark> Respondents Turner and Faulk, also in custody under informations, subsequently intervened.<footnotemark>7</footnotemark> Petitioner Gerstein, the State Attorney for Dade County, was one of several defendants.<footnotemark>8</footnotemark></p>
<p id="b193-5">After an initial delay while the Florida Legislature considered a bill that would have afforded preliminary hearings to persons charged by information, the District Court granted the relief sought. <em>Pugh </em>v. <em><span class="citation" data-id="1624670"><a href="/opinion/1624670/pugh-v-rainwater/" aria-description="Citation for case: Pugh v. Rainwater">Rainwater, supra.</a></span> </em>The court certified the case as a class action under Fed. Rule Civ. Proc. 23 (b) (2), and held that the Fourth and Fourteenth Amendments give all arrested persons charged by information a right to a judicial hearing on the question of probable cause. The District Court ordered the Dade County defendants to give the named plaintiffs an immediate preliminary hearing to determine probable <page-number citation-index="1" label="108">*108</page-number>cause for further detention.<footnotemark>9</footnotemark> It also ordered them to submit a plan providing preliminary hearings in all cases instituted by information.</p>
<p id="b194-5">The defendants submitted a plan prepared by Sheriff E. Wilson Purdy, and the District Court adopted it with modifications. The final order prescribed a detailed post-arrest procedure. <span class="citation" data-id="1795762"><a href="/opinion/1795762/pugh-v-rainwater/" aria-description="Citation for case: Pugh v. Rainwater">336 F. Supp. 490</a></span> (SD Fla. 1972). Upon arrest the accused would be taken before a magistrate for a “first appearance hearing.” The magistrate would explain the charges, advise the accused of his rights, appoint counsel if he was indigent, and proceed with a probable cause determination unless either the prosecutor or the accused was unprepared. If either requested more time, the magistrate would set the date for a “preliminary hearing,” to be held within four days if the accused was in custody and within 10 days if he had been released pending trial. The order provided sanctions for failure to hold the hearing at prescribed times. At the “preliminary hearing” the accused would be entitled to counsel, and he would be allowed to confront and cross-examine adverse witnesses, to summon favorable witnesses, and to have a transcript made on request. If the magistrate found no probable cause, the accused would be discharged. He then could not be charged with the same offense by complaint or information, but only by indictment returned within 30 days.</p>
<p id="b195-4"><page-number citation-index="1" label="109">*109</page-number>The Court of Appeals for the Fifth Circuit stayed the District Court's order pending appeal, but while the case was awaiting decision, the Dade County judiciary voluntarily adopted a similar procedure of its own. Upon learning of this development, the Court of Appeals remanded the case for specific findings on the constitutionality of the new Dade County system. Before the District Court issued its findings, however, the Florida Supreme Court amended the procedural rules governing preliminary hearings statewide, and the parties agreed that the District Court should direct its inquiry to the new rules rather than the Dade County procedures.</p>
<p id="b195-5">Under the amended rules every arrested person must be taken before a judicial officer within 24 hours. Fla. Rule Crim. Proc. 3.130 (b). This “first appearance” is similar to the “first appearance hearing” ordered by the District Court in all respects but the crucial one: the magistrate does not make a determination of probable cause. The rule amendments also changed the procedure for preliminary hearings, restricting them to felony charges and codifying the rule that no hearings are available to persons charged by information or indictment. Rule 3.131; see <em>In re Rule 3.131 </em>(b), <em>Florida Rules of Criminal Procedure, </em><span class="citation" data-id="1724472"><a href="/opinion/1724472/in-re-rule-3131-b-florida-rules-of-criminal-pro/" aria-description="Citation for case: In Re Rule 3.131 (B), Florida Rules of Criminal Pro.">289 So. 2d 3</a></span> (Fla. 1974).</p>
<p id="b195-6">In a supplemental opinion the District Court held that the amended rules had not answered the basic constitutional objection, since a defendant charged by information still could be detained pending trial without a judicial determination of probable cause. <span class="citation" data-id="1447830"><a href="/opinion/1447830/pugh-v-rainwater/" aria-description="Citation for case: Pugh v. Rainwater">355 F. Supp. 1286</a></span> (SD Fla. 1973). Reaffirming its original ruling, the District Court declared that the continuation of this practice was unconstitutional.<footnotemark>10</footnotemark> The Court of Appeals <page-number citation-index="1" label="110">*110</page-number>affirmed, <span class="citation multiple-matches"><a href="/c/F.%202d/483/778/">483 F. 2d 778</a></span> (1973), modifying the District Court’s decree in minor particulars and suggesting that the form of preliminary hearing provided by the amended Florida rules would be acceptable, as long as it was provided to all defendants in custody pending trial. <em>Id., </em>at 788-789.</p>
<p id="b196-5">State Attorney Gerstein petitioned for review, and we granted certiorari because of the importance of the issue.<footnotemark>11</footnotemark> <page-number citation-index="1" label="111">*111</page-number><span class="citation multiple-matches"><a href="/c/U.%20S./414/1062/">414 U. S. 1062</a></span> (1973). We affirm in part and reverse in part.</p>
<p id="b197-5">II</p>
<p id="b197-6">As framed by the proceedings below, this case presents two issues: whether a person arrested and held for trial on an information is entitled to a judicial determination of probable cause for detention, and if so, whether the adversary hearing ordered by the District Court and approved by the Court of Appeals is required by the Constitution.</p>
<p id="b197-7">A</p>
<p id="b197-8">Both the standards and procedures for arrest and detention have been derived from the Fourth Amendment and its common-law antecedents. See <em>Cupp </em>v. <em>Murphy, </em><span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#294" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291, 294-295</a></span> (1973); <em>Ex parte Bollman, </em><span class="citation" data-id="9416259"><a href="/opinion/84842/ex-parte-bollman-and-swartwout/" aria-description="Citation for case: Ex Parte Bollman and Swartwout">4 Cranch 75</a></span> (1807); <em>Ex parte Burford, </em><span class="citation" data-id="84827"><a href="/opinion/84827/ex-parte-burford/" aria-description="Citation for case: Ex Parte Burford">3 Cranch 448</a></span> (1806). The standard for arrest is probable cause, defined in terms of facts and circumstances “sufficient to warrant a prudent man in believing that the [suspect] had committed or was committing an offense.” <page-number citation-index="1" label="112">*112</page-number><em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#91" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 91</a></span> (1964). See also <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span> (1959); <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175-176</a></span> (1949). This standard, like those for searches and seizures, represents a necessary accommodation between the individual’s right to liberty and the State’s duty to control crime.</p>
<blockquote id="b198-5">“These long-prevailing standards seek to safeguard citizens from rash and unreasonable interferences with privacy and from unfounded charges of crime. They also seek to give fair leeway for enforcing the law in the community’s protection. Because many situations which confront officers in the course of executing their duties are more or less ambiguous, room must be allowed for some mistakes on their part. But the mistakes must be those of reasonable men, acting on facts leading sensibly to their conclusions of probability. The rule of probable cause is a practical, nontechnical conception affording the best compromise that has been found for accommodating these often opposing interests. Requiring more would unduly hamper law enforcement. To allow less would be to leave law-abiding citizens at the mercy of the officers’ whim or caprice.” <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States"><em>Id., </em>at 176</a></span>.</blockquote>
<p id="b198-6">To implement the Fourth Amendment’s protection against unfounded invasions of liberty and privacy, the Court has required that the existence of probable cause be decided by a neutral and detached magistrate whenever possible. The classic statement of this principle appears in <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-14</a></span> (1948):</p>
<blockquote id="b198-7">“The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its pro<page-number citation-index="1" label="113">*113</page-number>tection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime.”</blockquote>
<p id="b199-5">See also <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20-22</a></span> (1968).<footnotemark>12</footnotemark></p>
<p id="b199-6">Maximum protection of individual rights could be assured by requiring a magistrate’s review of the factual justification prior to any arrest, but such a requirement would constitute an intolerable handicap for legitimate law enforcement. Thus, while the Court has expressed a preference for the use of arrest warrants when feasible, <em>Beck </em>v. <em>Ohio, supra, </em>at 96; <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#479" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 479-482</a></span> (1963), it has never invalidated an arrest supported by probable cause solely because the officers failed to secure a warrant. See <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963); <em>Draper </em>v. <em>United States, </em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959); <em>Trupiano </em>v. <em>United States, </em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/#705" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699, 705</a></span> (1948).<footnotemark>13</footnotemark></p>
<p id="b199-7">Under this practical compromise, a policeman’s on-the-scene assessment of probable cause provides legal justifi<page-number citation-index="1" label="114">*114</page-number>cation for arresting a person suspected of crime, and for a brief period of detention to take the administrative steps incident to arrest. Once the suspect is in custody, however, the reasons that justify dispensing with the magistrate's neutral judgment evaporate. There no longer is any danger that the suspect will escape or commit further crimes while the police submit their evidence to a magistrate. And, while the State's reasons for taking summary action subside, the suspect's need for a neutral determination of probable cause increases significantly. The consequences of prolonged detention may be more serious than the interference occasioned by arrest. Pretrial confinement may imperil the suspect’s job, interrupt his source of income, and impair his family relationships. See R. Goldfarb, Ransom 32-91 (1965); L. Katz, Justice Is the Crime 51-62 (1972). Even pretrial release may be accompanied by burdensome conditions that effect a significant restraint of liberty. See, <em>e. g., </em><span class="citation no-link">18 U. S. C. §§ 3146</span> (a)(2), (5). When the stakes are this high, the detached judgment of a neutral magistrate is essential if the Fourth Amendment is to furnish meaningful protection from unfounded interference with liberty. Accordingly, we hold that the Fourth Amendment requires a judicial determination of probable cause as a prerequisite to extended restraint of liberty following arrest.</p>
<p id="b200-5">This result has historical support in the common law that has guided interpretation of the Fourth Amendment. See <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 149</a></span> (1925). At common law it was customary, if not obligatory, for an arrested person to be brought before a justice of the peace shortly after arrest. 2 M. Hale, Pleas of the Crown 77, 81, 95, 121 (1736); 2 W. Hawkins, Pleas of the Crown 116-117 (4th ed. 1762). See <em>siso Kurtz v. Moffitt, </em><span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/#498" aria-description="Citation for case: Kurtz v. Moffitt">115 U. S. 487, 498-499</a></span> (1885).<footnotemark>14</footnotemark> The justice of the peace <page-number citation-index="1" label="115">*115</page-number>would “examine” the prisoner and the witnesses to determine whether there was reason to believe the prisoner had committed a crime. If there was, the suspect would be committed to jail or bailed pending trial. If not, he would be discharged from custody. 1 M. Hale, <em>supra, </em>at 583-586; 2 W. Hawkins, <em>supra, </em>at 116-119; 1 J. Stephen, History of the Criminal Law of England 233 (1883).<footnotemark>15</footnotemark> The initial determination of probable cause also could be reviewed by higher courts on a writ of habeas corpus. 2 W. Hawkins, <em>supra, </em>at 112-115; 1 J. Stephen, <em>supra, </em>at 243; see <em>Ex parte Bollman, </em><span class="citation" data-id="9416259"><a href="/opinion/84842/ex-parte-bollman-and-swartwout/#97" aria-description="Citation for case: Ex Parte Bollman and Swartwout">4 Cranch, at 97-101</a></span>. This practice furnished the model for criminal procedure in America immediately following the adoption of the <page-number citation-index="1" label="116">*116</page-number>Fourth Amendment, see <span class="citation" data-id="9416259"><a href="/opinion/84842/ex-parte-bollman-and-swartwout/" aria-description="Citation for case: Ex Parte Bollman and Swartwout"><em>Ex parte Bollman, </em>supra;</a></span><footnotemark>16</footnotemark> <em>Ex parte Burford, </em><span class="citation" data-id="84827"><a href="/opinion/84827/ex-parte-burford/" aria-description="Citation for case: Ex Parte Burford">3 Cranch 448</a></span> (1806); <em>United States </em>v. <em>Hamilton, </em><span class="citation" data-id="84684"><a href="/opinion/84684/united-states-v-hamilton/" aria-description="Citation for case: United States v. Hamilton">3 Dall. 17</a></span> (1795), and there are indications that the Framers of the Bill of Rights regarded it as a model for a “reasonable” seizure. See <em>Draper </em>v. <em>United States, </em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#317" aria-description="Citation for case: Draper v. United States">358 U. S., at 317-320</a></span> (Douglas, J., dissenting).<footnotemark>17</footnotemark></p>
<p id="b202-5">B</p>
<p id="b202-6">Under the Florida procedures challenged here, a person arrested without a warrant and charged by information may be jailed or subjected to other restraints pending trial without any opportunity for a probable cause determination.<footnotemark>18</footnotemark> Petitioner defends this practice on the <page-number citation-index="1" label="117">*117</page-number>ground that the prosecutor's decision to file an information is itself a determination of probable cause that furnishes sufficient reason to detain a defendant pending trial. Although a conscientious decision that the evidence warrants prosecution affords a measure of protection against unfounded detention, we do not think prosecutorial judgment standing alone meets the requirements of the Fourth Amendment. Indeed, we think the Court's previous decisions compel disapproval of the Florida procedure. In <em>Albrecht </em>v. <em>United States, </em><span class="citation" data-id="100977"><a href="/opinion/100977/albrecht-v-united-states/#5" aria-description="Citation for case: Albrecht v. United States">273 U. S. 1, 5</a></span> (1927), the Court held that an arrest warrant issued solely upon a United States Attorney’s information was invalid because the accompanying affidavits were defective. Although the Court’s opinion did not explicitly state that the prosecutor’s official oath could not furnish probable cause, that conclusion was implicit in the judgment that the arrest was illegal under the Fourth Amendment.<footnotemark>19</footnotemark> More recently, in <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#449" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 449-453</a></span> (1971), the Court held that a prosecutor’s responsibility to law enforcement is inconsistent with the constitutional role of a neutral and detached magistrate. We reaffirmed that principle in <em>Shad-</em><page-number citation-index="1" label="118">*118</page-number><em>wick </em>v. <em>City of Tampa, </em><span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/" aria-description="Citation for case: Shadwick v. City of Tampa">407 U. S. 345</a></span> (1972), and held that probable cause for the issuance of an arrest warrant must be determined by someone independent of police and prosecution. See also <em>United States </em>v. <em>United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#317" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 317</a></span> (1972).<footnotemark>20</footnotemark> The reason for this separation of functions was expressed by Mr. Justice Frankfurter in a similar context:</p>
<blockquote id="b204-5">“A democratic society, in which respect for the dignity of all men is central, naturally guards against the misuse of the law enforcement process. Zeal in tracking down crime is not in itself an assurance of soberness of judgment. Disinterestedness in law enforcement does not alone prevent disregard of cherished liberties. Experience has therefore counseled that safeguards must be provided against the dangers of the overzealous as well as the despotic. The awful instruments of the criminal law cannot be entrusted to a single functionary. The complicated process of criminal justice is therefore divided into different parts, responsibility for which is separately vested in the various participants upon whom the criminal law relies for its vindication.” <em>McNabb </em>v. <em>United States, </em><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#343" aria-description="Citation for case: McNabb v. United States">318 U. S. 332, 343</a></span> (1943).</blockquote>
<p id="b204-6">In holding that the prosecutor’s assessment of probable <page-number citation-index="1" label="119">*119</page-number>cause is not sufficient alone to justify restraint of liberty pending trial, we do not imply that the accused is entitled to judicial oversight or review of the decision to prosecute. Instead, we adhere to the Court’s prior holding that a judicial hearing is not prerequisite to prosecution by information. <em>Beck </em>v. <em>Washington, </em><span class="citation" data-id="9422400"><a href="/opinion/106391/beck-v-washington/#545" aria-description="Citation for case: Beck v. Washington">369 U. S. 541, 545</a></span> (1962); <em>Lem Woon </em>v. <em>Oregon, </em><span class="citation" data-id="97944"><a href="/opinion/97944/lem-woon-v-oregon/" aria-description="Citation for case: Lem Woon v. Oregon">229 U. S. 586</a></span> (1913). Nor do we retreat from the established rule that illegal arrest or detention does not void a subsequent conviction. <em>Frisbie </em>v. <em>Collins, </em><span class="citation" data-id="104977"><a href="/opinion/104977/frisbie-v-collins/" aria-description="Citation for case: Frisbie v. Collins">342 U. S. 519</a></span> (1952); <em>Ker </em>v. <em>Illinois, </em><span class="citation" data-id="91772"><a href="/opinion/91772/ker-v-illinois/" aria-description="Citation for case: Ker v. Illinois">119 U. S. 436</a></span> (1886). Thus, as the Court of Appeals noted below, although a suspect who is presently detained may challenge the probable cause for that confinement, a conviction will not be vacated on the ground that the defendant was detained pending trial without a determination of probable cause. 483 F. 2d, at 786-787. Compare <em>Scarbrough </em>v. <em>Dutton, </em><span class="citation" data-id="9453521"><a href="/opinion/279699/charlie-h-scarbrough-v-a-l-dutton-warden-georgia-state-prison/" aria-description="Citation for case: Charlie H. Scarbrough v. A. L. Dutton, Warden, Georgia...">393 F. 2d 6</a></span> (CA5 1968), with <em>Brown </em>v. <em>Fauntleroy, </em>143 U. S. App. D. C. 116, <span class="citation" data-id="9456898"><a href="/opinion/296631/larry-daniel-brown-v-honorable-john-fauntleroy/" aria-description="Citation for case: Larry Daniel Brown v. Honorable John Fauntleroy">442 F. 2d 838</a></span> (1971), and <em>Cooley </em>v. <em>Stone, </em>134 U. S. App. D. C. 317, <span class="citation" data-id="286155"><a href="/opinion/286155/ronald-clifton-cooley-v-william-j-stone/" aria-description="Citation for case: Ronald Clifton Cooley v. William J. Stone">414 F. 2d 1213</a></span> (1969).</p>
<p id="b205-5">Ill</p>
<p id="b205-6">Both the District Court and the Court of Appeals held that the determination of probable cause must be accompanied by the full panoply of adversary safeguards — counsel, confrontation, cross-examination, and compulsory process for witnesses. A full preliminary hearing of this sort is modeled after the procedure used in many States to determine whether the evidence justifies going to trial under an information or presenting the case to a grand jury. See <em>Coleman </em>v. <em>Alabama, </em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970); Y. Kamisar, W. LaFave &amp; J. Israel, Modern Criminal Procedure 957-967, 996-1000 (4th ed. 1974). The standard of proof required of the prosecution is usually referred to as “probable cause,” but in some jurisdictions it may approach a prima facie case of guilt. <page-number citation-index="1" label="120">*120</page-number>ALI, Model Code of Pre-arraignment Procedure, Commentary on Art. 330, pp. 90-91 (Tent. Draft No. 5, 1972). When the hearing takes this form, adversary procedures are customarily employed. The importance of the issue to both the State and the accused justifies the presentation of witnesses and full exploration of their testimony on cross-examination. This kind of hearing also requires appointment of counsel for indigent defendants. <em>Coleman </em>v. <em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">Alabama, supra.</a></span> </em>And, as the hearing assumes increased importance and the procedures become more complex, the likelihood that it can be held promptly after arrest diminishes. See ALI, Model Code of Pre-arraignment Procedure, <em>supra, </em>at 33-34.</p>
<p id="b206-5">These adversary safeguards are not essential for the probable cause determination required by the Fourth Amendment. The sole issue is whether there is probable cause for detaining the arrested person pending further proceedings. This issue can be determined reliably without an adversary hearing. The standard is the same as that for arrest.<footnotemark>21</footnotemark> That standard — probable cause to believe the suspect has committed a crime — traditionally has been decided by a magistrate in a nonadversary proceeding on hearsay and written testimony, and the Court has approved these informal modes of proof.</p>
<blockquote id="b206-6">“Guilt in a criminal case must be proved beyond a reasonable doubt and by evidence confined to that which long experience in the common-law tradition, <page-number citation-index="1" label="121">*121</page-number>to some extent embodied in the Constitution, has crystallized into rules of evidence consistent with that standard. These rules are historically grounded rights of our system, developed to safeguard men from dubious and unjust convictions, with resulting forfeitures of life, liberty and property.</blockquote>
<blockquote id="b207-5">“In dealing with probable cause, however, as the very name implies, we deal with probabilities. These are not technical; they are the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act. The standard of proof is accordingly correlative to what must be proved.” <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#174" aria-description="Citation for case: Brinegar v. United States">338 U. S., at 174-175</a></span>.</blockquote>
<p id="b207-6">Cf. <em>McCray </em>v. <em>Illinois, </em><span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300</a></span> (1967).</p>
<p id="b207-7">The use of an informal procedure is justified not only by the lesser consequences of a probable cause determination but also by the nature of the determination itself. It does not require the fine resolution of conflicting evidence that a reasonable-doubt or even a preponderance standard demands, and credibility determinations are seldom crucial in deciding whether the evidence supports a reasonable belief in guilt. See F. Miller, Prosecution: The Decision to Charge a Suspect with a Crime 64— 109 (1969).<footnotemark>22</footnotemark> This is not to say that confrontation and <page-number citation-index="1" label="122">*122</page-number>cross-examination might not enhance the reliability of probable cause determinations in some cases. In most cases, however, their value would be too slight to justify holding, as a matter of constitutional principle, that these formalities and safeguards designed for trial must also be employed in making the Fourth Amendment determination of probable cause.<footnotemark>23</footnotemark></p>
<p id="b208-5">Because of its limited function and its nonadversary character, the probable cause determination is not a “critical stage” in the prosecution that would require appointed counsel. The Court has identified as “critical stages” those pretrial procedures that would impair defense on the merits if the accused is required to proceed without counsel. <em>Coleman </em>v. <em>Alabama, </em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970); <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#226" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 226-227</a></span> (1967). In <em>Coleman </em>v. <em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">Alabama</a></span>, </em>where the Court held that a preliminary hearing was a critical stage of an Alabama prosecution, the majority and concurring opinions identified two critical factors that distinguish the Alabama preliminary hearing from the probable cause determination required by the Fourth Amendment. First, <page-number citation-index="1" label="123">*123</page-number>under Alabama law the function of the preliminary hearing was to determine whether the evidence justified charging the suspect with an offense. A finding of no probable cause could mean that he would not be tried at.all. The Fourth Amendment probable cause determination is addressed only to pretrial custody. To be sure, pretrial custody may affect to some extent the defendant’s ability to assist in preparation of his defense, but this does not present the high probability of substantial harm identified as controlling in <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>and <em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">Coleman</a></span>. </em>Second, Alabama allowed the suspect to confront and cross-examine prosecution witnesses at the preliminary hearing. The Court noted that the suspect’s defense on the merits could be compromised if he had no legal assistance for exploring or preserving the witnesses’ testimony. This consideration does not apply when the prosecution is not required to produce witnesses for cross-examination.</p>
<p id="b209-5">Although we conclude that the Constitution does not require an adversary determination of probable cause, we recognize that state systems of criminal procedure vary widely. There is no single preferred pretrial procedure, and the nature of the probable cause determination usually will be shaped to accord with a State’s pretrial procedure viewed as a whole. While we limit our holding to the precise requirement of the Fourth Amendment, we recognize the desirability of flexibility and experimentation by the States. It may be found desirable, for example, to make the probable cause determination at the suspect’s first appearance before a judicial officer,<footnotemark>24</footnotemark> <page-number citation-index="1" label="124">*124</page-number>see <em>McNabb </em>v. <em>United States, </em><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#342" aria-description="Citation for case: McNabb v. United States">318 U. S., at 342-344</a></span>, or the determination may be incorporated into the procedure for setting bail or fixing other conditions of pretrial release. In some States, existing procedures may satisfy the requirement of the Fourth Amendment. Others may require only minor adjustment, such as acceleration of existing preliminary hearings. Current proposals for criminal procedure reform suggest other ways of testing probable cause for detention.<footnotemark>25</footnotemark> Whatever <page-number citation-index="1" label="125">*125</page-number>procedure a State may adopt, it must provide a fair and reliable determination of probable cause as a condition for any significant pretrial restraint of liberty,<footnotemark>26</footnotemark> and this determination must be made by a judicial officer either before or promptly after arrest.<footnotemark>27</footnotemark></p>
<p id="b212-4"><page-number citation-index="1" label="126">*126</page-number>IV</p>
<p id="b212-5">We agree with the Court of Appeals that the Fourth Amendment requires a timely judicial determination of probable cause as a prerequisite to detention, and we accordingly affirm that much of the judgment. As we do not agree that the Fourth Amendment requires the adversary hearing outlined in the District Court’s decree, we reverse in part and remand to the Court of Appeals for further proceedings consistent with this opinion.</p>
<p id="b212-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b191-10"> Respondent Pugh was arrested on March 3, 1971. On March 16 an information was filed charging him with robbery, carrying a concealed weapon, and possession of a firearm during commission of a felony. Respondent Henderson was arrested on March 2, and charged by information on March 19 with the offenses of breaking and entering and assault and battery. The record does not indicate whether there was an arrest warrant in either case.</p>
</footnote>
<footnote label="2">
<p id="b192-6"> Florida law also denies preliminary hearings to persons confined under indictment, see <em>Sangaree </em>v. <em>Hamlin, </em><span class="citation" data-id="1807359"><a href="/opinion/1807359/sangaree-v-hamlin/" aria-description="Citation for case: Sangaree v. Hamlin">235 So. 2d 729</a></span> (Fla. 1970) ; Fla. Rule Crim. Proc. 3.131 (a); but that procedure is not challenged in this case. See <em>infra, </em>at 117 n. 19.</p>
</footnote>
<footnote label="3">
<p id="b192-7"> This statute may have been construed to make the hearing permissive instead of mandatory. See <em>Evans </em>v. <em>State, </em><span class="citation" data-id="1725389"><a href="/opinion/1725389/evans-v-state/" aria-description="Citation for case: Evans v. State">197 So. 2d 323</a></span> (Fla. App. 1967); Fla. Op. Atty. Gen. 067-29 (1967). But cf. <em>Karz </em>v. <em>Overton, </em><span class="citation" data-id="7444015"><a href="/opinion/7520111/karz-v-overton/" aria-description="Citation for case: Karz v. Overton">249 So. 2d 763</a></span> (Fla. App. 1971). It may also have been superseded by the subsequent amendments to the Rules of Criminal Procedure. <em>In re Florida Rules of Criminal Procedure, </em><span class="citation" data-id="1917909"><a href="/opinion/1917909/in-re-florida-rules-of-criminal-procedure/" aria-description="Citation for case: In Re Florida Rules of Criminal Procedure">272 So. 2d 65</a></span> (1972).</p>
</footnote>
<footnote label="4">
<p id="b192-8"> The Florida rules do not suggest that the issue of probable cause can be raised at arraignment, Fla. Rule Crim. Proc. 3.160, but counsel for petitioner represented at oral argument that arraignment affords the suspect an opportunity to “attack the sufficiency of the evidence to hold him.” Tr. of Oral Arg. 17 (Mar. 25, 1974). The Court of Appeals assumed, without deciding, that this was true. <span class="citation multiple-matches"><a href="/c/F.%202d/483/778/">483 F. 2d 778</a></span>, 781 n. 8 (CA5 1973).</p>
</footnote>
<footnote label="5">
<p id="b193-6"> The complaint was framed under <span class="citation no-link">42 U. S. C. § 1983</span>, and jurisdiction in the District Court was based on <span class="citation no-link">28 U. S. C. § 1343</span> (3).</p>
</footnote>
<footnote label="6">
<p id="b193-7"> Respondents did not ask for release from state custody, even as an alternative remedy. They asked only that the state authorities be ordered to give them a probable cause determination. This was also the only relief that the District Court ordered for the named respondents. <span class="citation" data-id="1624670"><a href="/opinion/1624670/pugh-v-rainwater/#1115" aria-description="Citation for case: Pugh v. Rainwater">332 F. Supp. 1107, 1115-1116</a></span>, (SD Fla. 1971). Because release was neither asked nor ordered, the lawsuit did not come within the class of cases for which habeas corpus is the exclusive remedy. <em>Preiser </em>v. <em>Rodriguez, </em><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">411 U. S. 475</a></span> (1973); see <em>Wolff </em>v. <em>McDonnell, </em><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#55" aria-description="Citation for case: Wolff v. McDonnell">418 U. S. 539, 55-555</a></span> (1974).</p>
</footnote>
<footnote label="7">
<p id="b193-8"><em> </em>Turner was being held on a charge of auto theft, following arrest on March 11, 1971. Faulk was arrested on March 19 on charges of soliciting a ride and possession of marihuana.</p>
</footnote>
<footnote label="8">
<p id="b193-9"> The named defendants included justices of the peace and judges of small-claims courts, who were authorized to hold preliminary hearings in criminal cases, and a group of law enforcement officers with power to make arrests in Dade County. Gerstein was the only one who petitioned for certiorari.</p>
</footnote>
<footnote label="9">
<p id="b194-6"> The District Court correctly held that respondents’ claim for relief was not barred by the equitable restrictions on federal intervention in state prosecutions, <em>Younger </em>v. <em>Harris, </em><span class="citation" data-id="9424435"><a href="/opinion/108263/younger-v-harris/" aria-description="Citation for case: Younger v. Harris">401 U. S. 37</a></span> (1971). The injunction was not directed at the state prosecutions as such, but only at the legality of pretrial detention without a judicial hearing, an issue that could not be raised in defense of the criminal prosecution. The order to hold preliminary hearings could not prejudice the conduct of the trial on the merits. See <em>Conover </em>v. <em>Montemuro, </em><span class="citation" data-id="8890009"><a href="/opinion/8903008/conover-v-montemuro/#1082" aria-description="Citation for case: Conover v. Montemuro">477 F. 2d 1073, 1082</a></span> (CA3 1972); cf. <em>Perez </em>v. <em>Ledesma, </em><span class="citation" data-id="9424442"><a href="/opinion/108266/perez-v-ledesma/" aria-description="Citation for case: Perez v. Ledesma">401 U. S. 82</a></span> (1971); <em>Stefanelli </em>v. <em>Minard, </em><span class="citation" data-id="9420643"><a href="/opinion/104937/stefanelli-v-minard/" aria-description="Citation for case: Stefanelli v. Minard">342 U. S. 117</a></span> (1951).</p>
</footnote>
<footnote label="10">
<p id="b195-7"> Although this ruling held a statewide “legislative rule” unconstitutional, it was not outside the jurisdiction of a single judge by virtue of <span class="citation no-link">28 U. S. C. §2281</span>. The original complaint did not ask for <page-number citation-index="1" label="110">*110</page-number>an injunction against enforcement of any state statute or legislative rule of statewide application, since the practice of denying preliminary hearings to persons charged by information was then embodied only in judicial decisions. The District Court therefore had jurisdiction to issue the initial injunction, and the Court of Appeals had jurisdiction over the appeal. On remand, the constitutionality of a state “statute” was drawn into question for the first time when the criminal rules were amended. The District Court’s supplemental opinion can fairly be read as a declaratory judgment that the amended rules were unconstitutional; the injunctive decree was never amended to incorporate that holding; and the opinion in the Court of Appeals is not inconsistent with the conclusion that the District Court did not enjoin enforcement of the statewide rule. See 483 F. 2d, at 788-790. Accordingly, a district court of three judges was not required for the issuance of this order. See <em>Kennedy </em>v. <em>Mendoza-Martinez, </em><span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/#152" aria-description="Citation for case: Kennedy v. Mendoza-Martinez">372 U. S. 144, 152-155</a></span> (1963); <em>Flemming </em>v. <em>Nestor, </em><span class="citation" data-id="9422032"><a href="/opinion/106087/flemming-v-nestor/#606" aria-description="Citation for case: Flemming v. Nestor">363 U.S. 603, 606-608</a></span> (1960).</p>
</footnote>
<footnote label="11">
<p id="b196-7"> At oral argument counsel informed us that the named respondents have been convicted. Their pretrial detention therefore has ended. This case belongs, however, to that narrow class of cases in which the termination of a class representative’s claim does not moot the claims of the unnamed members of the class. See <em>Sosna </em>v. <em>Iowa, </em><span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/" aria-description="Citation for case: Sosna v. Iowa">419 U. S. 393</a></span> (1975). Pretrial detention is by nature temporary, and it is most unlikely that any given individual could have his constitutional claim decided on appeal before he is either released or convicted. The individual could nonetheless suffer repeated deprivations, and it is certain that other persons similarly situated will be detained under the allegedly unconstitutional procedures. The claim, in short, is one that is distinctly “capable of repetition, yet evading review.”</p>
<p id="b196-8">At the time the complaint was filed, the named respondents were <page-number citation-index="1" label="111">*111</page-number>members of a class of persons detained without a judicial probable cause determination, but the record does not indicate whether any of them were still in custody awaiting trial when the District Court certified the class. Such a showing ordinarily would be required to avoid mootness under <em><span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/" aria-description="Citation for case: Sosna v. Iowa">Sosna</a></span>. </em>But this case is a suitable exception to that requirement. See <em><span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/" aria-description="Citation for case: Sosna v. Iowa">Sosna, supra,</a></span> </em>at 402 n. 11; cf. <em>Rivera </em>v. <em>Freeman, </em><span class="citation" data-id="306786"><a href="/opinion/306786/rosa-rivera-v-the-honorable-marvin-a-freeman-judge-of-the-superior-court/#1162" aria-description="Citation for case: Rosa Rivera v. The Honorable Marvin A. Freeman, Judge of...">469 F. 2d 1159, 1162-1163</a></span> (CA9 1972). The length of pretrial custody cannot be ascertained at the outset, and it may be ended at any time by release on recognizance, dismissal of the charges, or a guilty plea, as well as by acquittal or conviction after trial. It is by no means certain that any given individual, named as plaintiff, would be in pretrial custody long enough for a district judge to certify the class. Moreover, in this case the constant existence of a class of persons suffering the deprivation is certain. The attorney representing the named respondents is a public defender, and we can safely assume that he has other clients with a continuing live interest in the case.</p>
</footnote>
<footnote label="12">
<p id="b199-8"> We reiterated this principle in <em>United States </em>v. <em>United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297</a></span> (1972). In terms that apply equally to arrests, we described the “very heart of the Fourth Amendment directive” as a requirement that “where practical, a governmental search and seizure should represent both the efforts of the officer to gather evidence of wrongful acts and the judgment of the magistrate that the collected evidence is sufficient to justify invasion of a citizen's private premises or conversation.” <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#316" aria-description="Citation for case: United States v. United States District Court for the..."><em>Id., </em>at 316</a></span>.</p>
</footnote>
<footnote label="13">
<p id="b199-9"> Another aspect of <em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span> </em>was overruled in <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span> (1950), which was overruled in turn by <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969).</p>
<p id="b199-10">The issue of warrantless arrest that has generated the most controversy, and that remains unsettled, is whether and under what circumstances an officer may enter a suspect’s home to make a war-rantless arrest. See <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#474" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 474-481</a></span> (1971); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#510" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 510-512</a></span>, and n. 1 (White, J., <em>dissenting); Jones </em>v. <em>United States, </em><span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499-500</a></span> (1958).</p>
</footnote>
<footnote label="14">
<p id="b200-6"> The primary motivation for the requirement seems to have been the penalty for allowing an offender to escape, if he had in fact <page-number citation-index="1" label="115">*115</page-number>committed the crime, and the fear of liability for false imprisonment, if he had not. But Hale also recognized that a judicial warrant of commitment, called a <em>mittimus, </em>was required for more than brief detention.</p>
<p id="b201-6">“When a private person hath arrested a felon, or one suspected of felony, he may detain him in custody till he can reasonably dismiss himself of him; but with as much speed as conveniently he can, he may do either of these things.</p>
<p id="b201-7">“1. He may carry him to the common gaol, . . . but that is now rarely done.</p>
<p id="b201-8">“2. He may deliver him to the constable of the vill, who may either carry him to the common gaol, ... or to a justice of peace to be examined, and farther proceeded against as case shall require. . . .</p>
<p id="b201-9">“3. Or he may carry him immediately to any justice of peace of the county where he is taken, who upon examination may discharge, bail, or commit him, as the case shall require.</p>
<p id="b201-10">“And the bringing the offender either by the constable or private person to a justice of peace is most usual and safe, because a gaoler will expect a <em>Mittimus </em>for his warrant of detaining.” 1 M. Hale, Pleas of the Crown 589-590 (1736).</p>
</footnote>
<footnote label="15">
<p id="b201-11"> The examination of the prisoner was inquisitorial, and the witnesses were questioned outside the prisoner’s presence. Although this method of proceeding was considered quite harsh, 1 J. Stephen, <em>supra, </em>at 219-225, it was well established that the prisoner was entitled to be discharged if the investigation turned up insufficient evidence of his guilt. <em>Id., </em>at 233.</p>
</footnote>
<footnote label="16">
<p id="b202-7"> In <em>Ex parte Bollman, </em>two men charged in the Aaron Burr case were committed following an examination in the Circuit Court of the District of Columbia. They filed a petition for writ of habeas corpus in the Supreme Court. The Court, in an opinion by Mr. Chief Justice Marshall, affirmed its jurisdiction to issue habeas corpus to persons in custody by order of federal trial courts. Then, following arguments on the Fourth Amendment requirement of probable cause, the Court surveyed the evidence against the prisoners and held that it did not establish probable cause that they were guilty of treason. The prisoners were discharged.</p>
</footnote>
<footnote label="17">
<p id="b202-8"> See also N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 15-16 (1937). A similar procedure at common law, the warrant for recovery of stolen goods, is said to have furnished the model for a “reasonable” search under the Fourth Amendment. The victim was required to appear before a justice of the peace and make an oath of probable cause that his goods could be found in a particular place. After the warrant was executed, and the goods seized, the victim and the alleged thief would appear before the justice of the peace for a prompt determination of the cause for seizure of the goods and detention of the thief. 2 M. Hale, <em>supra, </em>at 149-152; T. Taylor, Two Studies in Constitutional Interpretation 2A-25, 39-40 (1969); see <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#626" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 626-629</a></span> (1886).</p>
</footnote>
<footnote label="18">
<p id="b202-9"> A person arrested under a warrant would have received a prior judicial determination of probable cause. Under Fla. Rule Crim. <page-number citation-index="1" label="117">*117</page-number>Proc. 3.120, a warrant may be issued upon a sworn complaint that states facts showing that the suspect has committed a crime. The magistrate may also take testimony under oath to determine if there is reasonable ground to believe the complaint is true.</p>
</footnote>
<footnote label="19">
<p id="b203-6"> By contrast, the Court has held that an indictment, “fair upon its face,” and returned by a “properly constituted grand jury,” conclusively determines the existence of probable cause and requires issuance of an arrest warrant without further inquiry. <em>Ex parte United States, </em><span class="citation" data-id="101974"><a href="/opinion/101974/ex-parte-united-states/#250" aria-description="Citation for case: Ex Parte United States">287 U. S. 241, 250</a></span> (1932). See also <em>Giordenello </em>v. <em>United States, </em><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#487" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 487</a></span> (1958). The willingness to let a grand jury’s judgment substitute for that of a neutral and detached magistrate is attributable to the grand jury’s relationship to the courts and its historical role of protecting individuals from unjust prosecution. See <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#342" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 342-346</a></span> (1974).</p>
</footnote>
<footnote label="20">
<p id="b204-7"> The Court had earlier reached a different result in <em>Ocampo </em>v. <em>United States, </em><span class="citation" data-id="98209"><a href="/opinion/98209/ocampo-v-united-states/" aria-description="Citation for case: Ocampo v. United States">234 U. S. 91</a></span> (1914), a criminal appeal from the Philippine Islands. Interpreting a statutory guarantee substantially identical to the Fourth Amendment, Act of July 1, 1902, § 5, <span class="citation no-link">32 Stat. 693</span>, the Court held that an arrest warrant could issue solely upon a prosecutor’s information. The Court has since held that interpretation of a statutory guarantee applicable to the Philippines is not conclusive for interpretation of a cognate provision in the Federal Constitution, <em>Green </em>v. <em>United States, </em><span class="citation" data-id="9421521"><a href="/opinion/105594/green-v-united-states/#194" aria-description="Citation for case: Green v. United States">355 U. S. 184, 194-198</a></span> (1957). Even if it were, the result reached in <em><span class="citation" data-id="98209"><a href="/opinion/98209/ocampo-v-united-states/" aria-description="Citation for case: Ocampo v. United States">Ocampo</a></span> </em>is incompatible with the later holdings of <em>Albrecht, Coolidge, </em>and <em>Shadwick.</em></p>
</footnote>
<footnote label="21">
<p id="b206-7"> Because the standards are identical, ordinarily there is no need for further investigation before the probable cause determination can be made.</p>
<blockquote id="b206-8">“Presumably, whomever the police arrest they must arrest on 'probable cause.' It is not the function of the police to arrest, as it were, at large and to use an interrogating process at police headquarters in order to determine whom they should charge before a committing magistrate on 'probable cause.’ ” <em>Mallory </em>v. <em>United States, </em><span class="citation" data-id="105545"><a href="/opinion/105545/mallory-v-united-states/#456" aria-description="Citation for case: Mallory v. United States">354 U. S. 449, 456</a></span> (1957).</blockquote>
</footnote>
<footnote label="22">
<p id="b207-8"> In <em>Morrissey </em>v. <em>Brewer, </em><span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/" aria-description="Citation for case: Morrissey v. Brewer">408 U. S. 471</a></span> (1972), and <em>Gagnon </em>v. <em>Scarpelli, </em><span class="citation" data-id="9425285"><a href="/opinion/108785/gagnon-v-scarpelli/" aria-description="Citation for case: Gagnon v. Scarpelli">411 U. S. 778</a></span> (1973), we held that a parolee or probationer arrested prior to revocation is entitled to an informal preliminary hearing at the place of arrest, with some provision for live testimony. <span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#487" aria-description="Citation for case: Morrissey v. Brewer">408 U. S., at 487</a></span>; 411 U. S., at 786. That preliminary hearing, more than the probable cause determination required by the Fourth Amendment, serves the purpose of gathering and preserving live testimony, since the final revocation hearing frequently is held at some distance from the place where the violation occurred. <span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#485" aria-description="Citation for case: Morrissey v. Brewer">408 U. S., at 485</a></span>; 411 U. S., at 782-783, n. 5. Moreover, revocation <page-number citation-index="1" label="122">*122</page-number>proceedings may offer less protection from initial error than the more formal criminal process, where violations are defined by statute and the prosecutor has a professional duty not to charge a suspect with crime unless he is satisfied of probable cause. See ABA Code of Professional Responsibility DR 7-103 (A) (Final Draft 1969) (a prosecutor “shall not institute or cause to be instituted criminal charges when he knows or it is obvious that the charges are not supported by probable cause”); American Bar Association Project on Standards for Criminal Justice, The Prosecution Function §§ 1.1, 3.4, 3.9 (1974); American College of Trial Lawyers, Code of Trial Conduct, Rule 4 (c) (1963).</p>
</footnote>
<footnote label="23">
<p id="b208-7"> Criminal justice is already overburdened by the volume of cases and the complexities of our system. The processing of misdemeanors, in particular, and the early stages of prosecution generally are marked by delays that can seriously affect the quality of justice. A constitutional doctrine requiring adversary hearings for all persons detained pending trial could exacerbate the problem of pretrial delay.</p>
</footnote>
<footnote label="24">
<p id="b209-6"> Several States already authorize a determination of probable cause at this stage or immediately thereafter. See, <em>e. g., </em>Hawaii Rev. Stat. §§ 708-9 (5), 710-7 (1968); Vt. Rules Crim. Proc. 3 (b), 5 (c). This Court has interpreted the Federal Rules of Criminal Procedure to require a determination of probable cause at the first appearance. <em>Jaben </em>v. <em>United States, </em><span class="citation" data-id="9423037"><a href="/opinion/107058/jaben-v-united-states/#218" aria-description="Citation for case: Jaben v. United States">381 U. S. 214, 218</a></span> (1965); <em>Mallory </em>v. <em>United States, </em><span class="citation" data-id="105545"><a href="/opinion/105545/mallory-v-united-states/#454" aria-description="Citation for case: Mallory v. United States">354 U. S., at 454</a></span>.</p>
</footnote>
<footnote label="25">
<p id="b210-5"> Under the Uniform Rules of Criminal Procedure (Proposed Final Draft 1974), a person arrested without a warrant is entitled, “without unnecessary delay,” to a first appearance before a magistrate and a determination that grounds exist for issuance of an arrest warrant. The determination may be made on affidavits or testimony, in the presence of the accused. Rule 311. Persons who remain in custody for inability to qualify for pretrial release are offered another opportunity for a probable cause determination at the detention hearing, held no more than five days after arrest. This is an adversary hearing, and the parties may summon witnesses, but reliable hearsay evidence may be considered. Rule 344.</p>
<p id="b210-6">The ALI Model Code of Pre-arraignment Procedure (Tent. Draft No. 5, 1972, and Tent. Draft No. 5A, 1973) also provides a first appearance, at which a warrantless arrest must be supported by a reasonably detailed written statement of facts. §310.1. The magistrate may make a determination of probable cause to hold the accused, but he is not required to do so and the accused may request an attorney for an “adjourned session” of the first appearance to be held within two “court days.” At that session, the magistrate makes a determination of probable cause upon a combination of written and live testimony:</p>
<blockquote id="b210-7">“The arrested person may present written and testimonial evidence and arguments for his discharge and the state may present additional written and testimonial evidence and arguments that there is reasonable cause to believe that he has committed the crime of which he is accused. The state’s submission may be made by means of affidavits; and no witnesses shall be required to appear unless the court, in the light of the evidence and arguments submitted by the parties, determines that there is a basis for believing that the appearance of one or more witnesses for whom the arrested person seeks <page-number citation-index="1" label="125">*125</page-number>subpoenas might lead to a finding that there is no reasonable cause.” § 310.2 (2) (Tent. Draft No. 5A, 1973).</blockquote>
</footnote>
<footnote label="26">
<p id="b211-6"> Because the probable cause determination is not a constitutional prerequisite to the charging decision, it is required only for those suspects who suffer restraints on liberty other than the condition that they appear for trial. There are many kinds of pretrial release and many degrees of conditional liberty. See <span class="citation no-link">18 U. S. C. § 3146</span>; American Bar Association Project on Standards for Criminal Justice, Pretrial Release § 5.2 (1974); Uniform Rules of Criminal Procedure, Rule 341 (Proposed Final Draft 1974). We cannot define specifically those that would require a prior probable cause determination, but the key factor is significant restraint on liberty.</p>
</footnote>
<footnote label="27">
<p id="b211-7"> In his concurring opinion, Mr. Justice Stewart objects to the Court's choice of the Fourth Amendment as the rationale for decision and suggests that the Court offers less procedural protection to a person in jail than it requires in certain civil cases. Here we deal with the complex procedures of a criminal case and a threshold right guaranteed by the Fourth Amendment. The historical basis of the probable cause requirement is quite different from the relatively recent application of variable procedural due process in debtor-creditor disputes and termination of government-created benefits. The Fourth Amendment was tailored explicitly for the criminal justice system, and its balance between individual and public interests always has been thought to define the “process that is due” for seizures of person or property in criminal cases, including the detention of suspects pending trial. Part II-A, <em>supra. </em>Moreover, the Fourth Amendment probable cause determination is in fact only the <em>first </em>stage of an elaborate system, unique in jurisprudence, designed to safeguard the rights of those accused of criminal conduct. The relatively simple civil procedures (e. <em>g., </em>prior interview with school principal before suspension) presented in the cases cited in the concurring opinion are inapposite and irrelevant in the wholly different context of the criminal justice system.</p>
<p id="b211-8">It would not be practicable to follow the further suggestion implicit in Mr. Justice Stewart’s concurring opinion that we leave for <page-number citation-index="1" label="126">*126</page-number>another day determination of the procedural safeguards that are required in making a probable cause determination under the Fourth Amendment. The judgment under review both declares the right not to be detained without a probable cause determination and affirms the District Court’s order prescribing an adversary hearing for the implementation of that right. The circumstances of the case thus require a decision on both issues.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Giglio v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Giglio v. United States"
type: case
citation: "405 U.S. 150 (1972)"
parallel_cite: "92 S. Ct. 763; 31 L. Ed. 2d 104"
neutral_cite: 1972 U.S. LEXIS 83
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1972
date_decided: 1972-02-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1972-02-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Giglio v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108471/giglio-v-united-states/"
  cluster_id: 108471
  opinion_id: 108471
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Anchor"
related: ["[[Brady v. Maryland]]", "[[Napue v. Illinois]]", "[[Benn v. Lambert]]"]
aliases: ["Giglio v. US"]
tags: ["case", "brady", "giglio", "impeachment", "disclosure", "witness-credibility"]
holding: "Impeachment evidence falls within the Brady rule: nondisclosure of evidence affecting a key witness's credibility — including a promise…"
lake:
  record_id: Giglio v. United States
  status: verified
  projected_at: 2026-07-06
---

# Giglio v. United States

*405 U.S. 150 (1972)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Giglio was convicted of passing forged money orders almost entirely on the testimony of an accomplice, Robert Taliento, who had not been indicted. After trial, the defense learned that a prosecutor had promised Taliento he would not be prosecuted if he cooperated and testified — a promise the trial prosecutor never disclosed, and which had been denied at trial.

## Issue
Whether the Government's failure to disclose a promise of leniency made to its key witness — evidence going only to the witness's credibility — violates due process and requires a new trial.

## Rule
Impeachment evidence is governed by the Brady disclosure rule when the witness's credibility is central to the case. "When the 'reliability of a given witness may well be determinative of guilt or innocence,' nondisclosure of evidence affecting credibility falls within this general rule." — 405 U.S. at 154. ^pin-154

Because the prosecutor's office speaks as one for the Government, a promise made by one prosecutor is attributed to the Government even if the trial attorney was unaware of it; a new trial is required where the undisclosed evidence was material — that is, where it could in any reasonable likelihood have affected the jury's judgment.

## Application
Taliento was the Government's essential witness, so his reliability could well determine guilt or innocence. The undisclosed promise not to prosecute him gave him a powerful motive to testify favorably, and the jury was entitled to know of it. That one prosecutor made the promise while the trial prosecutor was unaware did not excuse the nondisclosure, and on this record the evidence was material — so Giglio was entitled to a new trial.

## Conclusion
The failure to disclose the leniency promise to a key witness required a new trial; the conviction was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Giglio* extends [[Brady v. Maryland]] to impeachment evidence and charges the prosecution with knowledge held by any of its attorneys; the framework is applied in [[Benn v. Lambert]].

## Appears on
- [[Brady and Giglio]] — *Key — Anchor*

## Sources
- *Giglio v. United States*, 405 U.S. 150 (1972) — https://www.courtlistener.com/opinion/108471/giglio-v-united-states/ — pinpoint: 154.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2a703d06e486940d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "405 U.S. 150 (1972)", "court": "U.S. Supreme Court", "neutral_cite": "1972 U.S. LEXIS 83", "official_citation_present": true, "parallel_cite": "92 S. Ct. 763; 31 L. Ed. 2d 104", "title": "Giglio v. United States", "year": "1972"}}
{"assertion_id": "3ed3343bbfd1d260", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Impeachment evidence falls within the Brady rule: nondisclosure of evidence affecting a key witness's credibility — including a promise…", "title": "Giglio v. United States"}}
{"assertion_id": "49e2fe8507ec42ec", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Key — Anchor", "title": "Giglio v. United States"}}
{"assertion_id": "27d7bde2797602d8", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Giglio v. United States"}}
{"assertion_id": "559337a43f3a4dbb", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1972-02-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Giglio v. United States", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Giglio v. United States", "varies_by_point": "false"}}
```

### lake record — Giglio v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Giglio v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Giglio v. United States",
    "case_name_short": "Giglio",
    "case_name_full": "Giglio v. United States",
    "input_case_name": "Giglio v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1972-02-24",
    "year": 1972,
    "docket": null,
    "cluster_id": 108471,
    "lead_opinion_id": 108471,
    "sibling_ids": [
      108471
    ],
    "absolute_url": "/opinion/108471/giglio-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "405 U.S. 150",
      "volume": "405",
      "reporter": "U.S.",
      "page": "150",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "92 S. Ct. 763",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "763",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "31 L. Ed. 2d 104",
        "volume": "31",
        "reporter": "L. Ed. 2d",
        "page": "104",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1972 U.S. LEXIS 83",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "83",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "405 U.S. 150",
        "volume": "405",
        "reporter": "U.S.",
        "page": "150",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 S. Ct. 763",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "763",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "31 L. Ed. 2d 104",
        "volume": "31",
        "reporter": "L. Ed. 2d",
        "page": "104",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1972 U.S. LEXIS 83",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "83",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "405 U.S. 150",
    "official_selection": {
      "court_class": "scotus",
      "selected": "405 U.S. 150",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-154",
      "page": null,
      "quote": "--- # Giglio v. United States *405 U.S. 150 (1972)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Giglio was convicted of passing forged money orders almost entirely on the testimony of an accomplice, Robert Taliento, who had not been indicted. After trial, the defense learned that a prosecutor had promised Taliento he would not be prosecuted if he cooperated and testified \u2014 a promise the trial prosecutor never disclosed, and which had been denied at trial. ## Issue Whether the Government's failure to disclose a promise of leniency made to its key witness \u2014 evidence going only to the witness's credibility \u2014 violates due process and requires a new trial. ## Rule Impeachment evidence is governed by the Brady disclosure rule when the witness's credibility is central to the case.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1972-02-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Giglio v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State Ex Rel. Darrell J. Robinson v. Darrel Vannoy, Warden, Louisiana State Penitentiary, Angola, Louisiana",
          "cluster_id": 10292764,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Graham v. District Attorney for the Hampden District",
          "cluster_id": 9468079,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Bagley",
          "cluster_id": 111514,
          "cite": [
            "87 L. Ed. 2d 481",
            "105 S. Ct. 3375",
            "473 U.S. 667",
            "1985 U.S. LEXIS 130",
            "53 U.S.L.W. 5084"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Imbler v. Pachtman",
          "cluster_id": 109387,
          "cite": [
            "47 L. Ed. 2d 128",
            "96 S. Ct. 984",
            "424 U.S. 409",
            "1976 U.S. LEXIS 25"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Agurs",
          "cluster_id": 109506,
          "cite": [
            "49 L. Ed. 2d 342",
            "96 S. Ct. 2392",
            "427 U.S. 97",
            "1976 U.S. LEXIS 72"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Strickler v. Greene",
          "cluster_id": 118307,
          "cite": [
            "144 L. Ed. 2d 286",
            "119 S. Ct. 1936",
            "527 U.S. 263",
            "1999 U.S. LEXIS 4191"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Phillips",
          "cluster_id": 110645,
          "cite": [
            "71 L. Ed. 2d 78",
            "102 S. Ct. 940",
            "455 U.S. 209",
            "1982 U.S. LEXIS 69"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Trombetta",
          "cluster_id": 111206,
          "cite": [
            "81 L. Ed. 2d 413",
            "104 S. Ct. 2528",
            "467 U.S. 479",
            "1984 U.S. LEXIS 103",
            "52 U.S.L.W. 4744"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCleskey v. Zant",
          "cluster_id": 112573,
          "cite": [
            "113 L. Ed. 2d 517",
            "111 S. Ct. 1454",
            "499 U.S. 467",
            "1991 U.S. LEXIS 2218",
            "59 U.S.L.W. 4288",
            "91 Cal. Daily Op. Serv. 2680",
            "91 Daily Journal DAR 4340"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Ritchie",
          "cluster_id": 111822,
          "cite": [
            "94 L. Ed. 2d 40",
            "107 S. Ct. 989",
            "480 U.S. 39",
            "1987 U.S. LEXIS 558",
            "55 U.S.L.W. 4180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kastigar v. United States",
          "cluster_id": 108541,
          "cite": [
            "32 L. Ed. 2d 212",
            "92 S. Ct. 1653",
            "406 U.S. 441",
            "1972 U.S. LEXIS 57"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hinkson",
          "cluster_id": 1191667,
          "cite": [
            "585 F.3d 1247",
            "2009 U.S. App. LEXIS 24358",
            "2009 WL 3645003"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Coleman",
          "cluster_id": 2115945,
          "cite": [
            "701 N.E.2d 1063",
            "183 Ill. 2d 366",
            "233 Ill. Dec. 789",
            "1998 Ill. LEXIS 938"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heckler v. Community Health Services of Crawford County, Inc.",
          "cluster_id": 111187,
          "cite": [
            "81 L. Ed. 2d 42",
            "104 S. Ct. 2218",
            "467 U.S. 51",
            "1984 U.S. LEXIS 87",
            "52 U.S.L.W. 4621"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Valenzuela-Bernal",
          "cluster_id": 110797,
          "cite": [
            "73 L. Ed. 2d 1193",
            "102 S. Ct. 3440",
            "458 U.S. 858",
            "1982 U.S. LEXIS 159",
            "50 U.S.L.W. 5108"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Pettit",
          "cluster_id": 1250971,
          "cite": [
            "171 Wis. 2d 627",
            "492 N.W.2d 633"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moore v. Illinois",
          "cluster_id": 108613,
          "cite": [
            "33 L. Ed. 2d 706",
            "92 S. Ct. 2562",
            "408 U.S. 786",
            "1972 U.S. LEXIS 23"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ruiz",
          "cluster_id": 121166,
          "cite": [
            "153 L. Ed. 2d 586",
            "122 S. Ct. 2450",
            "536 U.S. 622",
            "2002 U.S. LEXIS 4650"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Banks v. Dretke",
          "cluster_id": 131165,
          "cite": [
            "157 L. Ed. 2d 1166",
            "124 S. Ct. 1256",
            "540 U.S. 668",
            "2004 U.S. LEXIS 1621",
            "72 U.S.L.W. 4193",
            "17 Fla. L. Weekly Fed. S 153"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Roberson",
          "cluster_id": 112100,
          "cite": [
            "100 L. Ed. 2d 704",
            "108 S. Ct. 2093",
            "486 U.S. 675",
            "1988 U.S. LEXIS 2726",
            "56 U.S.L.W. 4590"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Van de Kamp v. Goldstein",
          "cluster_id": 145911,
          "cite": [
            "172 L. Ed. 2d 706",
            "129 S. Ct. 855",
            "555 U.S. 335",
            "2009 U.S. LEXIS 1003"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ash",
          "cluster_id": 108846,
          "cite": [
            "37 L. Ed. 2d 619",
            "93 S. Ct. 2568",
            "413 U.S. 300",
            "1973 U.S. LEXIS 45"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haley v. City of Boston",
          "cluster_id": 613874,
          "cite": [
            "657 F.3d 39",
            "2011 U.S. App. LEXIS 19223",
            "2011 WL 4347027"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Marshall",
          "cluster_id": 1969802,
          "cite": [
            "690 A.2d 1",
            "148 N.J. 89",
            "1997 N.J. LEXIS 70"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Blake v. State",
          "cluster_id": 9423249,
          "cite": [
            "485 Md. 265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane3_recency"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108471) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjQ5Mjg5NjAwMDAwJnM9NjQ1ODQxOCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108471%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108471)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MTQmcz03MDUyNTc4JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108471%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108471)",
        "reviewed": 187,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 187,
        "triage_read": 3,
        "triage_snippet_classified": 184
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108471)",
    "indexed_citing_opinions": 4151,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108471,
        "count": 4151,
        "count_source": "search"
      }
    ],
    "citation_count": 7011,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/giglio-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MzU1MyZzPTEwNjI0NTY2JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108471%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108471,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108471,
        "cited_id": 103727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108471,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108471,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108471,
        "cited_id": 279213,
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
    "date_created": "2026-07-05T05:27:48Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:28:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:28:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:31:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:28:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Giglio v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b294-12">
  Mr. Chief Justice Burger
 </author>
<p id="AL2">
  delivered the opinion of the Court.
 </p>
<p id="b294-13">
  Petitioner was convicted of passing forged money orders and sentenced to five years’ imprisonment. While appeal was pending in the Court of Appeals, defense counsel discovered new evidence indicating that the Government
  <span citation-index="1" class="star-pagination" label="151"> 
   *151
   </span>
  had failed to disclose an alleged promise made to its key-witness that he would not be prosecuted if he testified for the Government. We granted certiorari to determine whether the evidence not disclosed was such as to require a new trial under the due process criteria of
  <em>
   Napue
  </em>
  v.
  <em>
   Illinois,
  </em>
  <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264</a></span> (1959), and
  <em>
   Brady
  </em>
  v.
  <em>
   Maryland,
  </em>
  <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963).
 </p>
<p id="b295-5">
  The controversy in this case centers around the testimony of Robert Taliento, petitioner’s alleged cocon-spirator in the offense and the only witness linking petitioner with the crime. The Government’s evidence at trial showed that in June 1966 officials at the Manufacturers Hanover Trust Co. discovered that Taliento, as teller at the bank, had cashed several forged money orders. Upon questioning by FBI agents, he confessed supplying petitioner with one of the bank’s customer signature cards used by Giglio to forge $2,300 in money orders; Taliento then processed these money orders through the regular channels of the bank. Taliento related this story to the grand jury and petitioner was indicted; thereafter, he was named as a coconspirator with petitioner but was not indicted.
 </p>
<p id="b295-6">
  Trial commenced two years after indictment. Taliento testified, identifying petitioner as the instigator of the scheme. Defense counsel vigorously cross-examined, seeking to discredit his testimony by revealing possible agreements or arrangements for prosecutorial leniency:
 </p>
<blockquote id="b295-7">
  “[Counsel.] Did anybody tell you at any time that if you implicated somebody else in this case that you yourself would not be prosecuted?
 </blockquote>
<blockquote id="b295-8">
  “[Taliento.] Nobody told me I wouldn’t be prosecuted.
 </blockquote>
<blockquote id="b295-9">
  “Q. They told you you might not be prosecuted?
 </blockquote>
<blockquote id="b295-10">
  “A. I believe I still could be prosecuted.
 </blockquote>
<blockquote id="b296-4">
<span citation-index="1" class="star-pagination" label="152"> 
   *152
   </span>
  “Q. Were you ever arrested in this case or charged with anything in connection with these money orders that you testified to?
 </blockquote>
<blockquote id="b296-5">
  “A. Not at that particular time.
 </blockquote>
<blockquote id="b296-6">
  “Q. To this date, have you been charged with any crime?
 </blockquote>
<blockquote id="b296-7">
  “A. Not that I know of, unless they are still going to prosecute.”
 </blockquote>
<p id="b296-8">
  In summation, the Government attorney stated, “[Tali-ento] received no promises that he would not be indicted.”
 </p>
<p id="b296-9">
  The issue now before the Court arose on petitioner’s motion for new trial based on newly discovered evidence. An affidavit filed by the Government as part of its opposition to a new trial confirms petitioner’s claim that a promise was made to Taliento by one assistant, DiPaola,
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  that if he testified before the grand jury and at trial he would not be prosecuted.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  DiPaola presented the Government’s case to the grand jury but did not try the case in the District Court, and Golden, the assistant who took over the case for trial, filed an affidavit stating that DiPaola assured him before the trial that no promises of immunity had been made to Taliento.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  The United
  <span citation-index="1" class="star-pagination" label="153"> 
   *153
   </span>
  States Attorney, Hoey, filed an affidavit stating that he had personally consulted with Taliento and his attorney shortly before trial to emphasize that Taliento would definitely be prosecuted if he did not testify and that if he did testify he would be obliged to rely on the “good judgment and conscience of the Government” as to whether he would be prosecuted.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
</p>
<p id="b297-5">
  The District Court did not undertake to resolve the apparent conflict between the two Assistant United States Attorneys, DiPaola and Golden, but proceeded on the theory that even if a promise had been made by DiPaola it was not authorized and its disclosure to the jury would not have affected its verdict. We need not concern ourselves with the differing versions of the events as described by the two assistants in their affidavits. The heart of the matter is that one Assistant United States Attorney — the first one who dealt with Taliento— now states that he promised Taliento that he would not be prosecuted if he cooperated with the Government.
 </p>
<p id="b297-6">
  As long ago as
  <em>
   Mooney
  </em>
  v.
  <em>
   Holohan,
  </em>
  <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#112" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103, 112</a></span> (1935), this Court made clear that deliberate deception of a. court and jurors by the presentation of known false evidence \s&gt; incompatible with “rudimentary demands of justice.” This was reaffirmed in
  <em>
   Pyle
  </em>
  v.
  <em>
   Kansas,
  </em>
  <span class="citation" data-id="103727"><a href="/opinion/103727/pyle-v-kansas/" aria-description="Citation for case: Pyle v. Kansas">317 U. S. 213</a></span> (1942). In
  <em>
   Napue
  </em>
  v.
  <em>
   Illinois,
  </em>
  <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264</a></span> (1959), we said, “[t]he same result obtains when the State, although not soliciting false evidence, allows it to go uncorrected when it appears.”
  <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois"><em>
   Id.,
  </em>
  at 269</a></span>. Thereafter
  <em>
   Brady
  </em>
  v.
  <em>
   Maryland,
  </em>
  <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>, held that suppression of material evidence justifies a new trial “irrespective of the good faith or bad faith of the prosecution.” See Ameri
  <span citation-index="1" class="star-pagination" label="154"> 
   *154
   </span>
  can Bar Association, Project on Standards for Criminal Justice, Prosecution Function and the Defense Function §3.11 (a). When the “reliability of a given witness may well be determinative of guilt or innocence,” nondisclosure of evidence affecting credibility falls within this general rule.
  <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois"><em>
   Napue, supra,
  </em>
  at 269</a></span>. We do not, however, automatically require a new trial whenever “a combing of the prosecutors’ files after the trial has disclosed evidence possibly useful to the defense but not likely to have changed the verdict . . . .”
  <em>
   United States
  </em>
  v.
  <em>
   Keogh,
  </em>
  <span class="citation" data-id="279213"><a href="/opinion/279213/united-states-v-james-vincent-keogh/#148" aria-description="Citation for case: United States v. James Vincent Keogh">391 F. 2d 138, 148</a></span> (CA2 1968). A finding of materiality of the evidence is required under
  <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland"><em>
   Brady, supra,
  </em>
  at 87</a></span>. A new trial is required if “the false testimony could ... in any reasonable likelihood have affected the judgment of the jury . . . .”
  <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#271" aria-description="Citation for case: Napue v. Illinois"><em>
   Napue, supra,
  </em>
  at 271</a></span>.
 </p>
<p id="b298-5">
  In the circumstances shown by this record, neither DiPaola’s authority nor his failure to inform his superiors or his associates is controlling. Moreover, whether the nondisclosure was a result of negligence or design, it is the responsibility of the prosecutor. The prosecutor’s office is an entity and as such it is the spokesman for the Government. A promise made by one attorney must be attributed, for these purposes, to the Government. See Restatement (Second) of Agency § 272. See also American Bar Association, Project on Standards for Criminal Justice, Discovery and Procedure Before Trial §2.1 (d). To the extent this places a burden on the large prosecution offices, procedures and regulations can be established to carry that burden and to insure communication of all relevant information on each case to every lawyer who deals with it.
 </p>
<p id="b298-6">
  Here the Government’s case depended almost entirely on Taliento’s testimony; without it there could have been no indictment and no evidence to carry the case to the jury. Taliento’s credibility as a witness was therefore
  <span citation-index="1" class="star-pagination" label="155"> 
   *155
   </span>
  an important issue in the case, and evidence of any-understanding or agreement as to a future prosecution would be relevant to his credibility and the jury was entitled to know of it.
 </p>
<p id="b299-5">
  For these reasons, the due process requirements enunciated in
  <em>
   <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">Napue</a></span>
  </em>
  and the other cases cited earlier require a new trial, and the judgment of conviction is therefore reversed and the case is remanded for further proceedings consistent with this opinion.
 </p>
<p id="b299-6">
<em>
   Reversed and remanded.
  </em>
</p>
<p id="b299-7">
  Mr. Justice Powell and Mr. Justice Rehnquist took no part in the consideration or decision of this case.
 </p>




<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b296-10">
   During oral argument in this Court it was stated that DiPaola was on the staff of the United States Attorney when he made the affidavit in 1969 and remained on that staff until recently.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b296-11">
   DiPaola’s affidavit reads, in part, as follows :
  </p>
<blockquote id="b296-12">
   “It was agreed that if ROBERT EDWARD TALIENTO would testify before the Grand Jury as a witness for the Government, . . . he would not be . . . indicted. ... It was further agreed and understood that he, ROBERT EDWARD TALIENTO, would sign a Waiver of Immunity from prosecution before the Grand Jury, and that if he eventually testified as a witness for the Government at the trial of the defendant, JOHN GIGLIO, he would not be prosecuted.”
  </blockquote>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b296-13">
   Golden’s affidavit reads, in part, as follows:
  </p>
<blockquote id="b296-14">
   “Mr. DiPaola . . . advised that Mr. Taliento had not been granted immunity but that he had not indicted him because Robert Taliento was very young at the time of the alleged occurrence and obviously had been overreached by the defendant Giglio.”
  </blockquote>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b297-7">
   The Hoey affidavit, standing alone, contains at least an implication that the Government would reward the cooperation of the witness, and hence tends to confirm rather than refute the existence of some understanding for leniency.
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Gilbert v. California.md  (`case`, 5 assertions)

### content_page

```
---
title: "Gilbert v. California"
type: case
citation: "388 U.S. 263 (1967)"
parallel_cite: "87 S. Ct. 1951; 18 L. Ed. 2d 1178"
neutral_cite: 1967 U.S. LEXIS 1086
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-06-12
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-06-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Gilbert v. California
  varies_by_point: false
  scope_note: "Wade-Gilbert right to counsel attaches only at/after initiation of adversary judicial proceedings (Kirby v. Illinois)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107487/gilbert-v-california/"
  cluster_id: 107487
  opinion_id: 107487
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Anchor"
related: ["[[United States v. Wade]]", "[[Stovall v. Denno]]", "[[Kirby v. Illinois]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "lineup", "eyewitness-identification", "per-se-exclusion"]
holding: "Testimony that a witness identified the accused at an uncounseled post-indictment lineup must be excluded per se — a strict rule (no…"
lake:
  record_id: Gilbert v. California
  status: verified
  projected_at: 2026-07-06
---

# Gilbert v. California

*388 U.S. 263 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Gilbert was convicted of armed robbery and the murder of a police officer. Sixteen days after his indictment and the appointment of counsel, police conducted a lineup in a Los Angeles auditorium — without notice to his counsel — before roughly 100 eyewitnesses to various robberies. At trial, several witnesses identified Gilbert in court, and the State also elicited testimony that they had identified him at the uncounseled lineup.

## Issue
What relief is required when the State introduces (1) in-court identifications by witnesses who viewed an uncounseled post-indictment lineup and (2) testimony that those witnesses identified the accused at that lineup.

## Rule
The two categories are treated differently. In-court identifications require a [[United States v. Wade]] hearing to determine whether they rest on an [[Inevitable Discovery and Independent Source|independent source]] untainted by the illegal lineup. But testimony that a witness identified the accused at the uncounseled lineup is the direct product of the constitutional violation and is subject to automatic exclusion: "Only a per se exclusionary rule as to such testimony can be an effective sanction to assure that law enforcement authorities will respect the accused's constitutional right to the presence of his counsel at the critical lineup." — 388 U.S. at 273. ^pin-273

## Application
The lineup occurred after Gilbert's indictment and the appointment of counsel, yet counsel received no notice — a Sixth Amendment violation under *[[United States v. Wade|Wade]]*. The in-court identifications therefore had to be [[Reading and Citing Cases#on-remand|remanded]] for an independent-source determination, but the testimony that the apartment manager and the eight penalty-stage witnesses had identified Gilbert at that very lineup was the direct result of the illegal lineup, so its admission was error subject to [[Common Legal Terms#per-se|per se]] exclusion rather than an independent-source inquiry.

## Conclusion
Admission of the witnesses' testimony about their uncounseled-lineup identifications was constitutional error requiring reversal under a [[Common Legal Terms#per-se|per se]] exclusionary rule; the in-court identifications were [[Reading and Citing Cases#on-remand|remanded]] for a *[[United States v. Wade|Wade]]* independent-source hearing.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of *Gilbert*'s holding. The *[[United States v. Wade|Wade]]*-*Gilbert* right to counsel attaches only at or after the initiation of adversary judicial proceedings ([[Kirby v. Illinois]]); *Gilbert*'s own lineup was post-indictment and remains within the rule.

## Appears on
- [[Eyewitness Identification]] — *Key — Anchor*

## Sources
- *Gilbert v. California*, 388 U.S. 263 (1967) — https://www.courtlistener.com/opinion/107487/gilbert-v-california/ — pinpoint: 273.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "14ab3dea1d79e995", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "388 U.S. 263 (1967)", "court": "U.S. Supreme Court", "neutral_cite": "1967 U.S. LEXIS 1086", "official_citation_present": true, "parallel_cite": "87 S. Ct. 1951; 18 L. Ed. 2d 1178", "title": "Gilbert v. California", "year": "1967"}}
{"assertion_id": "ced6d2fbe6272ae7", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Testimony that a witness identified the accused at an uncounseled post-indictment lineup must be excluded per se — a strict rule (no…", "title": "Gilbert v. California"}}
{"assertion_id": "dcb7c0e6014b2974", "dimension": "support", "kind": "home_role", "locator": {"home": "Eyewitness Identification"}, "payload": {"home": "Eyewitness Identification", "role": "Key — Anchor", "title": "Gilbert v. California"}}
{"assertion_id": "90c45220f0ed0b26", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1967-06-12", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Gilbert v. California", "field_i_validity": "good_law", "scope_note": "Wade-Gilbert right to counsel attaches only at/after initiation of adversary judicial proceedings (Kirby v. Illinois).", "title": "Gilbert v. California", "varies_by_point": "false"}}
{"assertion_id": "be853db20fda9ec3", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Gilbert v. California"}}
```

### lake record — Gilbert v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Gilbert v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Gilbert v. California",
    "case_name_short": "",
    "case_name_full": "Gilbert v. California",
    "input_case_name": "Gilbert v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-06-12",
    "year": 1967,
    "docket": null,
    "cluster_id": 107487,
    "lead_opinion_id": 107487,
    "sibling_ids": [
      107487,
      9423477,
      9423478,
      9423479,
      9423480,
      9423481
    ],
    "absolute_url": "/opinion/107487/gilbert-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "388 U.S. 263",
      "volume": "388",
      "reporter": "U.S.",
      "page": "263",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 1951",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1951",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 1178",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "1178",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 1086",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1086",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "388 U.S. 263",
        "volume": "388",
        "reporter": "U.S.",
        "page": "263",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 1951",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1951",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 1178",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "1178",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 1086",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1086",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "388 U.S. 263",
    "official_selection": {
      "court_class": "scotus",
      "selected": "388 U.S. 263",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-273",
      "page": null,
      "quote": "--- # Gilbert v. California *388 U.S. 263 (1967)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gilbert was convicted of armed robbery and the murder of a police officer. Sixteen days after his indictment and the appointment of counsel, police conducted a lineup in a Los Angeles auditorium \u2014 without notice to his counsel \u2014 before roughly 100 eyewitnesses to various robberies. At trial, several witnesses identified Gilbert in court, and the State also elicited testimony that they had identified him at the uncounseled lineup. ## Issue What relief is required when the State introduces (1) in-court identifications by witnesses who viewed an uncounseled post-indictment lineup and (2) testimony that those witnesses identified the accused at that lineup. ## Rule The two categories are treated differently. In-court identifications require a [[United States v. Wade]] hearing to determine whether they rest on an independent source untainted by the illegal lineup. But testimony that a witness identified the accused at the uncounseled lineup is the direct product of the constitutional violation and is subject to automatic exclusion:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1967-06-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Gilbert v. California",
    "varies_by_point": false,
    "scope_note": "Wade-Gilbert right to counsel attaches only at/after initiation of adversary judicial proceedings (Kirby v. Illinois).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Minnesota v. Matthew Vaughn Diamond",
          "cluster_id": 4338873,
          "cite": [
            "890 N.W.2d 143",
            "2017 Minn. App. LEXIS 9",
            "2017 WL 163710"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dickson",
          "cluster_id": 4244499,
          "cite": [
            "141 A.3d 810",
            "322 Conn. 410",
            "2016 Conn. LEXIS 236"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Guzman-Rincon",
          "cluster_id": 4247752,
          "cite": [
            "2015 COA 166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Longoria v. State",
          "cluster_id": 1397963,
          "cite": [
            "154 S.W.3d 747",
            "2004 WL 2851775"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gary Allen Lott, United States of America v. Johnny Marton Lott, AKA Johnny Martin Lott",
          "cluster_id": 779902,
          "cite": [
            "310 F.3d 1231",
            "2002 U.S. App. LEXIS 23050"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Cervantes",
          "cluster_id": 2633363,
          "cite": [
            "29 P.3d 225",
            "111 Cal. Rptr. 2d 148",
            "26 Cal. 4th 860",
            "2001 Cal. Daily Op. Serv. 7469",
            "2001 Daily Journal DAR 9125",
            "2001 Cal. LEXIS 5597"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane1_negative"
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
        "journal_ref": "Gilbert v. California:lane1_negative"
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
        "journal_ref": "Gilbert v. California:lane2_top_cited"
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
        "journal_ref": "Gilbert v. California:lane2_top_cited"
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
        "journal_ref": "Gilbert v. California:lane2_top_cited"
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
        "journal_ref": "Gilbert v. California:lane2_top_cited"
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
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Young",
          "cluster_id": 111353,
          "cite": [
            "84 L. Ed. 2d 1",
            "105 S. Ct. 1038",
            "470 U.S. 1",
            "1985 U.S. LEXIS 49",
            "53 U.S.L.W. 4159"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
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
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kirby v. Illinois",
          "cluster_id": 108554,
          "cite": [
            "32 L. Ed. 2d 411",
            "92 S. Ct. 1877",
            "406 U.S. 682",
            "1972 U.S. LEXIS 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
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
        "journal_ref": "Gilbert v. California:lane2_top_cited"
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
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estelle v. Smith",
          "cluster_id": 110474,
          "cite": [
            "68 L. Ed. 2d 359",
            "101 S. Ct. 1866",
            "451 U.S. 454",
            "1981 U.S. LEXIS 95",
            "49 U.S.L.W. 4490"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fisher v. United States",
          "cluster_id": 109432,
          "cite": [
            "48 L. Ed. 2d 39",
            "96 S. Ct. 1569",
            "425 U.S. 391",
            "1976 U.S. LEXIS 98",
            "37 A.F.T.R.2d (RIA) 1244"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coleman v. Alabama",
          "cluster_id": 108182,
          "cite": [
            "26 L. Ed. 2d 387",
            "90 S. Ct. 1999",
            "399 U.S. 1",
            "1970 U.S. LEXIS 17"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williams v. Florida",
          "cluster_id": 108186,
          "cite": [
            "26 L. Ed. 2d 446",
            "90 S. Ct. 1893",
            "399 U.S. 78",
            "1970 U.S. LEXIS 98",
            "53 Ohio Op. 2d 55"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nobles",
          "cluster_id": 109292,
          "cite": [
            "45 L. Ed. 2d 141",
            "95 S. Ct. 2160",
            "422 U.S. 225",
            "1975 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
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
        "journal_ref": "Gilbert v. California:lane2_top_cited"
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
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dionisio",
          "cluster_id": 108709,
          "cite": [
            "35 L. Ed. 2d 67",
            "93 S. Ct. 764",
            "410 U.S. 1",
            "1973 U.S. LEXIS 110"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Harris",
          "cluster_id": 2411822,
          "cite": [
            "839 S.W.2d 54",
            "1992 Tenn. LEXIS 348"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
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
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Desist v. United States",
          "cluster_id": 107875,
          "cite": [
            "22 L. Ed. 2d 248",
            "89 S. Ct. 1030",
            "394 U.S. 244",
            "1969 U.S. LEXIS 2159"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harper v. Virginia Department of Taxation",
          "cluster_id": 112890,
          "cite": [
            "125 L. Ed. 2d 74",
            "113 S. Ct. 2510",
            "509 U.S. 86",
            "1993 U.S. LEXIS 4212",
            "7 Fla. L. Weekly Fed. S 456",
            "16 Employee Benefits Cas. (BNA) 2313",
            "93 Daily Journal DAR 7730",
            "93 Cal. Daily Op. Serv. 4491",
            "61 U.S.L.W. 4664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. State",
          "cluster_id": 1577216,
          "cite": [
            "790 S.W.2d 568",
            "1989 Tex. Crim. App. LEXIS 151",
            "1989 WL 69709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gouveia",
          "cluster_id": 111193,
          "cite": [
            "81 L. Ed. 2d 146",
            "104 S. Ct. 2292",
            "467 U.S. 180",
            "1984 U.S. LEXIS 91",
            "52 U.S.L.W. 4659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107487 OR 9423477 OR 9423478 OR 9423479 OR 9423480 OR 9423481) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04OTgxMjgwMDAwMDAmcz0xNTM1MTQyJnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107487+OR+9423477+OR+9423478+OR+9423479+OR+9423480+OR+9423481%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(107487 OR 9423477 OR 9423478 OR 9423479 OR 9423480 OR 9423481)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01Nzcmcz0xMDgzMDMmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107487+OR+9423477+OR+9423478+OR+9423479+OR+9423480+OR+9423481%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107487 OR 9423477 OR 9423478 OR 9423479 OR 9423480 OR 9423481)",
        "reviewed": 10,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 10,
        "triage_read": 0,
        "triage_snippet_classified": 10
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107487 OR 9423477 OR 9423478 OR 9423479 OR 9423480 OR 9423481)",
    "indexed_citing_opinions": 2609,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107487,
        "count": 2461,
        "count_source": "search"
      },
      {
        "opinion_id": 9423477,
        "count": 235,
        "count_source": "search"
      },
      {
        "opinion_id": 9423478,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423479,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423480,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423481,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3797,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/gilbert-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY4MzA0Nzgmcz0xMDM2NzQ0NCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28107487+OR+9423477+OR+9423478+OR+9423479+OR+9423480+OR+9423481%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107487,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 105440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 105859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 106699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 107279,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 107342,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 107439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 273233,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 1160583,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 1193668,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 1421049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 1801408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
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
    "date_created": "2026-07-05T05:31:03Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:31:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:31:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:35:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:31:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Gilbert v. California

```
<div>
<center><b><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U.S. 263</a></span> (1967)</b></center>
<center><h1>GILBERT<br>
v.<br>
CALIFORNIA.</h1></center>
<center>No. 223.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 15-16, 1967.</center>
<center>Decided June 12, 1967.</center>
CERTIORARI TO THE SUPREME COURT OF CALIFORNIA.
<p><span class="star-pagination">*264</span> <i>Luke McKissack</i> argued the cause and filed briefs for petitioner.</p>
<p><i>Norman H. Sokolow,</i> Deputy Attorney General of California, and <i>William E. James,</i> Assistant Attorney General, argued the cause for respondent. With them on the brief was <i>Thomas C. Lynch,</i> Attorney General.</p>
<p>MR. JUSTICE BRENNAN delivered the opinion of the Court.</p>
<p>This case was argued with <i>United States</i> v. <i>Wade, ante,</i> p. 218, and presents the same alleged constitutional error in the admission in evidence of in-court identifications there considered. In addition, petitioner alleges constitutional <span class="star-pagination">*265</span> errors in the admission in evidence of testimony of some of the witnesses that they also identified him at the lineup, in the admission of handwriting exemplars taken from him after his arrest, and in the admission of out-of-court statements by King, a co-defendant, mentioning petitioner's part in the crimes. which statements, on the co-defendant's appeal decided with petitioner's, were held to have been improperly admitted against the co-defendant. Finally, he alleges that his Fourth Amendment rights were violated by a police seizure of photographs of him from his locked apartment after entry without a search warrant, and the admission of testimony of witnesses that they identified him from those photographs within hours after the crime.</p>
<p>Petitioner was convicted in the Superior Court of California of the armed robbery of the Mutual Savings and Loan Association of Alhambra and the murder of a police officer who entered during the course of the robbery. There were separate guilt and penalty stages of the trial before the same jury, which rendered a guilty verdict and imposed the death penalty. The California Supreme Court affirmed, <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/" aria-description="Citation for case: People v. Gilbert">63 Cal. 2d 690</a></span>, <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/" aria-description="Citation for case: People v. Gilbert">408 P. 2d 365</a></span>. We granted certiorari, <span class="citation" data-id="107279"><a href="/opinion/107279/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">384 U. S. 985</a></span>, and set the case for argument with <i>Wade</i> and with <i>Stovall</i> v. <i>Denno, post,</i> p. 293. If our holding today in <i>Wade</i> is applied to this case, the issue whether admission of the in-court and lineup identifications is constitutional error which requires a new trial could be resolved on this record only after further proceedings in the California courts. We must therefore first determine whether petitioner's other contentions warrant any greater relief.</p>
<p></p>
<h2>I.</h2>
<p></p>
<h2>THE HANDWRITING EXEMPLARS.</h2>
<p>Petitioner was arrested in Philadelphia by an FBI agent and refused to answer questions about the Alhambra <span class="star-pagination">*266</span> robbery without the advice of counsel. He later did answer questions of another agent about some Philadelphia robberies in which the robber used a handwritten note demanding that money be handed over to him, and during that interrogation gave the agent the handwriting exemplars. They were admitted in evidence at trial over objection that they were obtained in violation of petitioner's Fifth and Sixth Amendment rights. The California Supreme Court upheld admission of the exemplars on the sole ground that petitioner had waived any rights that he might have had not to furnish them. "[The agent] did not tell Gilbert that the exemplars would not be used in any other investigation. Thus, even if Gilbert believed that his exemplars would not be used in California, it does not appear that the authorities improperly induced such belief." <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/#708" aria-description="Citation for case: People v. Gilbert">63 Cal. 2d, at 708</a></span>. <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/#376" aria-description="Citation for case: People v. Gilbert">408 P. 2d, at 376</a></span>. The court did not, therefore, decide petitioner's constitutional claims.</p>
<p>We pass the question of waiver since we conclude that the taking of the exemplars violated none of petitioner's constitutional rights.</p>
<p><i>First.</i> The taking of the exemplars did not violate petitioner's Fifth Amendment privilege against self-incrimination. The privilege reaches only compulsion of "an accused's communications, whatever form they might take, and the compulsion of responses which are also communications, for example, compliance with a subpoena to produce one's papers," and not "compulsion which makes a suspect or accused the source of `real or physical evidence' . . . ." <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#763" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 763-764</a></span>. One's voice and handwriting are, of course, means of communication. It by no means follows, however, that every compulsion of an accused to use his voice or write compels a communication within the cover of the privilege. A mere handwriting exemplar, in contrast to the content of what is <span class="star-pagination">*267</span> written, like the voice or body itself, is an identifying physical characteristic outside its protection. <i>United States</i> v. <i>Wade, supra</i><i>,</i> at 222-223. No claim is made that the content of the exemplars was testimonial or communicative matter. Cf. <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>.</p>
<p><i>Second.</i> The taking of the exemplars was not a "critical" stage of the criminal proceedings entitling petitioner to the assistance of counsel. Putting aside the fact that the exemplars were taken before the indictment and appointment of counsel, there is minimal risk that the absence of counsel might derogate from his right to a fair trial. Cf. <i>United States</i> v. <i>Wade, supra</i><i>.</i> If, for some reason, an unrepresentative exemplar is taken, this can be brought out and corrected through the adversary process at trial since the accused can make an unlimited number of additional exemplars for analysis and comparison by government and defense handwriting experts. Thus, "the accused has the opportunity for a meaningful confrontation of the [State's] case at trial through the ordinary processes of cross-examination of the [State's] expert [handwriting] witnesses and the presentation of the evidence of his own [handwriting] experts." <i>United States</i> v. <i>Wade, supra</i><i>,</i> at 227-228.</p>
<p></p>
<h2>II.</h2>
<p></p>
<h2>ADMISSION OF CO-DEFENDANT'S STATEMENTS.</h2>
<p>Petitioner contends that he was denied due process of law by the admission during the guilt stage of the trial of his accomplice's pretrial statements to the police which referred to petitioner 159 times in the course of reciting petitioner's role in the robbery and murder. The statements were inadmissible hearsay as to petitioner, and were held on King's aspect of this appeal to be improperly obtained from him and therefore to be inadmissible against him under California law. <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/#699" aria-description="Citation for case: People v. Gilbert">63 Cal. 2d, at 699-701</a></span>, <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/#370" aria-description="Citation for case: People v. Gilbert">408 P. 2d, at 370-371</a></span>.</p>
<p><span class="star-pagination">*268</span> Petitioner would have us reconsider <i>Delli Paoli</i> v. <i>United States,</i> <span class="citation" data-id="9421359"><a href="/opinion/105440/delli-paoli-v-united-states/" aria-description="Citation for case: Delli Paoli v. United States">352 U. S. 232</a></span> (where the Court held that appropriate instructions to the jury would suffice to prevent prejudice to a defendant from the references to him in a co-defendant's statement), at least as applied to a case, as here, where the co-defendant gained a reversal because of the improper admission of the statements. We have no occasion to pass upon this contention. The California Supreme Court has rejected the <i><span class="citation" data-id="9421359"><a href="/opinion/105440/delli-paoli-v-united-states/" aria-description="Citation for case: Delli Paoli v. United States">Delli Paoli</a></span></i> rationale, and relying at least in part on the reasoning of the <i><span class="citation" data-id="9421359"><a href="/opinion/105440/delli-paoli-v-united-states/" aria-description="Citation for case: Delli Paoli v. United States">Delli Paoli</a></span></i> dissent, regards cautionary instructions as inadequate to cure prejudice. <i>People</i> v. <i>Aranda,</i> <span class="citation" data-id="9542298"><a href="/opinion/1160583/people-v-aranda/" aria-description="Citation for case: People v. Aranda">63 Cal. 2d 518</a></span>, <span class="citation" data-id="9542298"><a href="/opinion/1160583/people-v-aranda/" aria-description="Citation for case: People v. Aranda">407 P. 2d 265</a></span>. The California court applied <i><span class="citation" data-id="9542298"><a href="/opinion/1160583/people-v-aranda/" aria-description="Citation for case: People v. Aranda">Aranda</a></span></i> in this case but held that any error as to Gilbert in the admission of King's statements was harmless. The harmless-error standard applied was that "there is no reasonable possibility that the error in admitting King's statements and testimony might have contributed to Gilbert's conviction," a standard derived by the court from our decision in <i>Fahy</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422676"><a href="/opinion/106699/fahy-v-connecticut/" aria-description="Citation for case: Fahy v. Connecticut">375 U. S. 85</a></span>.<sup>[1]</sup><i>Fahy</i> was the basis of our holding in <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span>, and the standard applied by the California court satisfies the standard as defined in <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span>.</i></p>
<p>It may be that the California Supreme Court will review the application of its harmless-error standard to King's statements if on the remand the State presses harmless error also in the introduction of the in-court and lineup identifications. However, this at best implies an ultimate application of <i><span class="citation" data-id="9542298"><a href="/opinion/1160583/people-v-aranda/" aria-description="Citation for case: People v. Aranda">Aranda</a></span></i> and only confirms that petitioner's argument for reconsideration of <i><span class="citation" data-id="9421359"><a href="/opinion/105440/delli-paoli-v-united-states/" aria-description="Citation for case: Delli Paoli v. United States">Delli Paoli</a></span></i> need not be considered at this time.</p>
<p></p>
<h2>
<span class="star-pagination">*269</span> III.</h2>
<p></p>
<h2>THE SEARCH-AND-SEIZURE CLAIM.</h2>
<p>The California Supreme Court rejected Gilbert's challenge to the admission of certain photographs taken from his apartment pursuant to a warrantless search. The court justified the entry into the apartment under the circumstances on the basis of so-called "hot pursuit" and "exigent circumstances" exceptions to the warrant requirement. We granted certiorari to consider the important question of the extent to which such exceptions may permit warrantless searches without violation of the Fourth Amendment. A closer examination of the record than was possible when certiorari was granted reveals that the facts do not appear with sufficient clarity to enable us to decide that question. See Appendix to this opinion; compare <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span>. We therefore vacate certiorari on this issue as improvidently granted. <i>The Monrosa</i> v. <i>Carbon Black Export, Inc.,</i> <span class="citation" data-id="9421781"><a href="/opinion/105859/the-monrosa-v-carbon-black-export-inc/#184" aria-description="Citation for case: The Monrosa v. Carbon Black Export, Inc.">359 U. S. 180, 184</a></span>.</p>
<p></p>
<h2>IV.</h2>
<p></p>
<h2>THE IN-COURT AND LINEUP IDENTIFICATIONS.</h2>
<p>Since none of the petitioner's other contentions warrants relief, the issue becomes what relief is required by application to this case of the principles today announced in <i>United States</i> v. <i>Wade, supra</i><i>.</i></p>
<p>Three eyewitnesses to the Alhambra crimes who identified Gilbert at the guilt stage of the trial had observed him at a lineup conducted without notice to his counsel in a Los Angeles auditorium 16 days after his indictment and after appointment of counsel. The manager of the apartment house in which incriminating evidence was found, and in which Gilbert allegedly resided, identified Gilbert in the courtroom and also testified, in substance, to her prior lineup identification on examination by the <span class="star-pagination">*270</span> State. Eight witnesses who identified him in the courtroom at the penalty stage were not eyewitnesses to the Alhambra crimes but to other robberies allegedly committed by him. In addition to their in-court identifications, these witnesses also testified that they identified Gilbert at the same lineup.</p>
<p>The lineup was on a stage behind bright lights which prevented those in the line from seeing the audience. Upwards of 100 persons were in the audience, each an eyewitness to one of the several robberies charged to Gilbert. The record is otherwise virtually silent as to what occurred at the lineup.<sup>[2]</sup></p>
<p><span class="star-pagination">*271</span> At the guilt stage, after the first witness, a cashier of the savings and loan association, identified Gilbert in the courtroom, defense counsel moved, out of the presence of the jury, to strike her testimony on the ground that she identified Gilbert at the pretrial lineup conducted in the absence of counsel in violation of the Sixth Amendment made applicable to the States by the Fourteenth Amendment. <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>. He requested a hearing outside the presence of the jury to present evidence supporting his claim that her in-court identification was, and others to be elicited by the State from other eyewitnesses would be, "predicated at least in large part upon their identification or purported identification of Mr. Gilbert at the showup . . . ." The trial judge denied the motion as premature. Defense counsel then elicited the fact of the cashier's lineup identification on cross-examination and again moved to strike her identification testimony. Without passing on the merits of the Sixth Amendment claim, the trial judge denied the motion on the ground that, assuming a violation, it would not in any event entitle Gilbert to suppression of the in-court identification. Defense counsel thereafter elicited the fact of lineup identifications from two other eyewitnesses who on direct examination identified Gilbert in the courtroom. Defense counsel unsuccessfully objected at the penalty stage, to the testimony of the eight witnesses to the other robberies that they identified Gilbert at the lineup.</p>
<p><span class="star-pagination">*272</span> The admission of the in-court identifications without first determining that they were not tainted by the illegal lineup but were of independent origin was constitutional error. <i>United States</i> v. <i>Wade, supra</i><i>.</i> We there held that a post-indictment pretrial lineup at which the accused is exhibited to identifying witnesses is a critical stage of the criminal prosecution; that police conduct of such a lineup without notice to and in the absence of his counsel denies the accused his Sixth Amendment right to counsel and calls in question the admissibility at trial of the in-court identifications of the accused by witnesses who attended the lineup. However, as in <i>Wade,</i> the record does not permit an informed judgment whether the in-court identifications at the two stages of the trial had an independent source. Gilbert is therefore entitled only to a vacation of his conviction pending the holding of such proceedings as the California Supreme Court may deem appropriate to afford the State the opportunity to establish that the in-court identifications had an independent source, or that their introduction in evidence was in any event harmless error.</p>
<p>Quite different considerations are involved as to the admission of the testimony of the manager of the apartment house at the guilt phase and of the eight witnesses at the penalty stage that they identified Gilbert at the lineup.<sup>[3]</sup> That testimony is the direct result of the illegal <span class="star-pagination">*273</span> lineup "come at by exploitation of [the primary] illegality." <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 488</a></span>. The State is therefore not entitled to an opportunity to show that that testimony had an independent source. Only a <i>per se</i> exclusionary rule as to such testimony can be an effective sanction to assure that law enforcement authorities will respect the accused's constitutional right to the presence of his counsel at the critical lineup. In the absence of legislative regulations adequate to avoid the hazards to a fair trial which in-here in lineups as presently conducted, the desirability of deterring the constitutionally objectionable practice must prevail over the undesirability of excluding relevant evidence. Cf. <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>. That conclusion is buttressed by the consideration that the witness' testimony of his lineup identification will enhance the impact of his in-court identification on the jury and <span class="star-pagination">*274</span> seriously aggravate whatever derogation exists of the accused's right to a fair trial. Therefore, unless the California Supreme Court is "able to declare a belief that it was harmless beyond a reasonable doubt," <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#24" aria-description="Citation for case: Chapman v. California">386 U. S. 18, 24</a></span>, Gilbert will be entitled on remand to a new trial or, if no prejudicial error is found on the guilt stage but only in the penalty stage, to whatever relief California law affords where the penalty stage must be set aside.</p>
<p>The judgment of the California Supreme Court and the conviction are vacated, and the case is remanded to that court for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>THE CHIEF JUSTICE joins this opinion except for Part III, from which he dissents for the reasons expressed in the opinion of MR. JUSTICE DOUGLAS.</p>
<p></p>
<h2>APPENDIX TO OPINION OF THE COURT.</h2>
<p>Photographs of Gilbert introduced at the guilt stage of the trial had been viewed by eyewitnesses within hours after the robbery and murder. Officers had entered his apartment without a warrant and found them in an envelope on the top of a bedroom dresser. The envelope was of the kind customarily used in delivering developed prints, with the words "Marlboro Photo Studio" imprinted on it. The officers entered the apartment because of information given by an accomplice which led them to believe that one of the suspects might be inside the apartment. Assuming that the warrantless entry into the apartment was justified by the need immediately to search for the suspect, the issue remains whether the subsequent search was reasonably supported by those same exigent circumstances. If the envelope <span class="star-pagination">*275</span> were come upon in the course of a search for the suspect, the answer might be different from that where it is come upon, even though in plain view, in the course of a general, indiscriminate search of closets, dressers, etc., after it is known that the occupant is absent. Still different considerations may be presented where officers, pursuing the suspect, find that he is absent from the apartment but conduct a limited search for suspicious objects in plain view which might aid in the pursuit. The problem with the record in the present case is that it could reasonably support any of these factual conclusions upon which our constitutional analysis should rest, and the trial court made no findings on the scope of search. The California Supreme Court, which had no more substantial basis upon which to resolve the conflict than this Court, stated that the photos were come upon "while the officers were looking through the apartment for their suspect . . . ." As will appear, a contrary conclusion is equally reasonable.</p>
<p>(1) Agent Schlatter testified that immediately upon entering the apartment which he put at "approximately 1:05," the officers made a quick search for the occupant, which took at most a minute, and that the continued presence of the officers became "a matter of a stake-out under the assumption that the person or persons involved would come back." He testified that the officer who found the photographs, Agent Crowley, had entered the apartment with him. Agent Schlatter's testimony might support the California Supreme Court's view of the scope of search; (2) Agent Crowley testified that he arrived within five minutes <i>after</i> Agent Schlatter, "around 1:30, give or take a few minutes either way," that the apartment had already been searched for the suspects, and that he was instructed "to look through the apartment for anything we could find that we could use to identify or continue the pursuit of this person <span class="star-pagination">*276</span> without conducting a detailed search." Crowley's further testimony was that the search, pursuant to which the photos were found, was limited in this manner, and that he merely inspected objects in plain sight which would aid in identification. He stated that a detailed search for guns and money was not conducted until after a warrant had issued over three hours later. (3) Agent Townsend said he arrived at the apartment "sometime between perhaps 1:30 and 2:00," and that "well within an hour" he, Agent Crowley, another agent and a local officer conducted a detailed search of the bedroom. He stated that they "looked through the bedroom closet and dresser and I think . . . the headstand." A substantial sum of money was found in the dresser. Townsend could not "specifically say" whether Crowley was in the bedroom at the time the money was found. This testimony might support a finding that the officers were engaged in a general search of the bedroom at the time the photos were found.</p>
<p>The testimony of the agents concerning their time of arrival in the apartment is not inconsistent with any of the three possible conclusions as to the scope of search. Taking Townsend's testimony together with Crowley's, it can be concluded that the two arrived at about the same time. Agent Schlatter's testimony that Crowley arrived with him at 1:05, however, supports a conclusion that Crowley had begun his activities before Townsend arrived. Then there is the testimony of Agent Kiel, who did not enter the apartment, that he obtained the photos while talking with the landlady "approximately 1:25 to 1:30," about the same time that both Crowley and Townsend testified they arrived. In sum, the testimony concerning the timing of the events surrounding the search is both approximate and itself contradictory.</p>
<p><span class="star-pagination">*277</span> MR. JUSTICE BLACK, concurring in part and dissenting in part.</p>
<p>Petitioner was convicted of robbery and murder partially on the basis of handwriting samples he had given to the police while he was in custody without counsel and partially on evidence that he had been identified by eyewitnesses at a lineup identification ceremony held by California officers in a Los Angeles auditorium without notice to his counsel. The Court's opinion shows that the officers took Gilbert to the auditorium while he was a prisoner, formed a lineup of Gilbert and other persons, required each one to step forward, asked them certain questions, and required them to repeat certain phrases, while eyewitnesses to this and other crimes looked at them in efforts to identify them as the criminals. At his trial, Gilbert objected to the handwriting samples and to the identification testimony given by witnesses who saw him at the auditorium lineup on the ground that the admission of this evidence would violate his Fifth Amendment privilege against self-incrimination and Sixth Amendment right to counsel. It is well-established now that the Fourteenth Amendment makes both the Self Incrimination Clause of the Fifth Amendment and the Right to Counsel Clause of the Sixth Amendment obligatory on the States. See, <i>e. g., </i><i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span>; <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>.</p>
<p></p>
<h2>I.</h2>
<p>(a) Relying on <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span>, the Court rejects Gilbert's Fifth Amendment contention as to both the handwriting exemplars and the lineup identification. I dissent from that holding. For reasons set out in my separate opinion in <i>United State</i> v. <i>Wade, ante,</i> p. 243, as well as in my dissent to <i>Schmerber,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#773" aria-description="Citation for case: Schmerber v. California">384 U. S., at 773</a></span>, I think that case wholly unjustifiably detracts from the protection against compelled self-incrimination <span class="star-pagination">*278</span> the Fifth Amendment was designed to afford. It rests on the ground that compelling a suspect to submit to or engage in conduct the sole purpose of which is to supply evidence against himself nonetheless does not compel him to be a witness against himself. Compelling a suspect or an accused to be "the source of `real or physical evidence' . . . ," so says <i>Schmerber,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#764" aria-description="Citation for case: Schmerber v. California">384 U. S., at 764</a></span>, is not compelling him to be a witness against himself. Such an artificial distinction between things that are in reality the same is in my judgment wholly out of line with the liberal construction which should always be given to the Bill of Rights. See <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>.</p>
<p>(b) The Court rejects Gilbert's right-to-counsel contention in connection with the handwriting exemplars on the ground that the taking of the exemplars "was not a `critical' stage of the criminal proceedings entitling petitioner to the assistance of counsel." In all reality, however, it was one of the most "critical" stages of the government proceedings that ended in Gilbert's conviction. As to both the State's case and Gilbert's defense, the handwriting exemplars were just as important as the lineup and perhaps more so, for handwriting analysis, being, as the Court notes, "scientific" and "systematized," <i>United States</i> v. <i>Wade, ante,</i> at 227, may carry much more weight with the jury than any kind of lineup identification. The Court, however, suggests that absence of counsel when handwriting exemplars are obtained will not impair the right of cross-examination at trial. But just as nothing said in our previous opinions "links the right to counsel only to protection of Fifth Amendment rights." <i>United States</i> v. <i>Wade, ante,</i> at 226, nothing has been said which justifies linking the right to counsel only to the protection of other Sixth Amendment rights. And there is nothing in the Constitution to justify considering the right to counsel as a second-class, <span class="star-pagination">*279</span> subsidiary right which attaches only when the Court deems other specific rights in jeopardy. The real basis for the Court's holding that the stage of obtaining handwriting exemplars is not "critical," is its statement that "there is minimal risk that the absence of counsel might derogate from his right to a fair trial." The Court considers the "right to a fair trial" to be the overriding "aim of the right to counsel," <i>United States</i> v. <i>Wade, ante,</i> at 226, and somehow believes that this Court has the power to balance away the constitutional guarantee of right to counsel when the Court believes it unnecessary to provide what the Court considers a "fair trial." But I think this Court lacks constitutional power thus to balance away a defendant's absolute right to counsel which the Sixth and Fourteenth Amendments guarantee him. The Framers did not declare in the Sixth Amendment that a defendant is entitled to a "fair trial," nor that he is entitled to counsel on the condition that this Court thinks there is more than a "minimal risk" that without a lawyer his trial will be "unfair." The Sixth Amendment settled that a trial without a lawyer is constitutionally unfair, unless the court-created balancing formula has somehow changed it. <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458</a></span>, and <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>, I thought finally established the right of an accused to counsel without balancing of any kind.</p>
<p>The Court's holding here illustrates the danger to Bill of Rights guarantees in the use of words like a "fair trial" to take the place of the clearly specified safeguards of the Constitution. I think it far safer for constitutional rights for this Court to adhere to constitutional language like "the accused shall . . . have the Assistance of Counsel for his defence" instead of substituting the words not mentioned, "the accused shall have the assistance of counsel only if the Supreme Court thinks it necessary to assure a fair trial." In my judgment the guarantees <span class="star-pagination">*280</span> of the Constitution with its Bill of Rights provide the kind of "fair trial" the Framers sought to protect. Gilbert was entitled to have the "assistance of counsel" when he was forced to supply evidence for the Government to use against him at his trial. I would reverse the case for this reason also.</p>
<p></p>
<h2>II.</h2>
<p>I agree with the Court that Gilbert's case should not be reversed for state error in admitting the pretrial statements of an accomplice which referred to Gilbert. But instead of squarely rejecting petitioner's reliance on the dissent in <i>Delli Paoli</i> v. <i>United States,</i> <span class="citation" data-id="9421359"><a href="/opinion/105440/delli-paoli-v-united-states/#246" aria-description="Citation for case: Delli Paoli v. United States">352 U. S. 232, 246</a></span>, the Court avoids the issue by pointing to the fact that the California Supreme Court, even assuming the error to be a federal constitutional one, applied a harmless-error test which measures up to the one we subsequently enunciated in <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span>. And the Court then goes on to suggest that the California Supreme Court may desire to reconsider whether that is so upon remand.</p>
<p>I think the Court should clearly indicate that neither <i><span class="citation" data-id="9421359"><a href="/opinion/105440/delli-paoli-v-united-states/" aria-description="Citation for case: Delli Paoli v. United States">Delli Paoli</a></span></i> nor <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span></i> has any relevance here. <i><span class="citation" data-id="9421359"><a href="/opinion/105440/delli-paoli-v-united-states/" aria-description="Citation for case: Delli Paoli v. United States">Delli Paoli</a></span></i> rested on the admissibility of evidence in federal, not state, courts. The introduction of evidence in state courts is exclusively governed by state law unless its introduction would violate some federal constitutional provision and there is no such federal provision here. See <i>Spencer</i> v. <i>Texas,</i> <span class="citation" data-id="9423324"><a href="/opinion/107342/spencer-v-texas/" aria-description="Citation for case: Spencer v. Texas">385 U. S. 554</a></span>. That being so, any error in admitting the accomplice's pretrial statements is only an error of state law, and <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span>,</i> providing a federal constitutional harmless-error rule, has absolutely no relevance here. Instead of looking at the harmless-error test applied by the California Supreme Court in order to ascertain whether it comports with <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span>,</i> I would make it clear that this Court is leaving to the <span class="star-pagination">*281</span> States their unbridled power to control their own state courts in the absence of conflicting federal constitutional provisions.</p>
<p></p>
<h2>III.</h2>
<p>One witness who identified Gilbert at the guilt stage of his trial and eight witnesses who identified him at the penalty stage testified on direct examination that they had identified him in the auditorium lineup. I agree with the Court that the admission of this testimony was constitutional error and that Gilbert is entitled to a new trial unless the state courts, applying <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span>,</i> conclude that this error was harmless. However, these witnesses also identified Gilbert in the courtroom and two other witnesses at the guilt stage identified him solely in the courtroom. As to these, the Court holds that "[t]he admission of the in-court identifications without first determining that they were not tainted by the illegal lineup . . . was constitutional error." I dissent from this holding in this case and in <i>United States</i> v. <i>Wade, ante,</i> p. 243, for the reasons there given.</p>
<p>For the reasons here stated, I would vacate the judgment of the California Supreme Court and remand for consideration of whether the admission of the handwriting exemplars and the out-of-court lineup identification was harmless error.<sup>[*]</sup></p>
<p>MR. JUSTICE DOUGLAS, concurring in part and dissenting in part.</p>
<p>While I agree with the Court's opinion except for Part I,<sup>[]</sup> I would reverse and remand for a new trial on <span class="star-pagination">*282</span> the search and seizure point. The search of the petitioner's home is sought to be justified by the doctrine of "hot pursuit," even though the officers conducting the search knew that petitioner, the suspected criminal, was not at home.</p>
<p>At about 10:30 a. m. on January 3, 1964, a California bank was robbed by two armed men; a police officer was killed by one of the robbers. Another officer shot one of the robbers. Weaver, who was captured a few blocks from the scene of the crime. Weaver told the police that he had participated in the robbery and that a person known to him as "Skinny" Gilbert was his accomplice. He told the officers that Gilbert lived in Apartment 28 of "a Hawaiian sounding named apartment house" on Los Feliz Boulevard. This information was given to the Federal Bureau of Investigation and was broadcast to a field agent, Kiel, who was instructed to find the apartment. Kiel located the "Lanai," an apartment on Los Feliz Boulevard, at about 1 p. m., informed the radio control, and engaged the apartment manager in conversation. While they were talking, a man gave a key to the manager and told her that he was going to San Francisco for a few days. Agent Kiel learned from the manager that Flood, one of the two men who had rented Apartment 28 the previous day, was the man who had just turned in the key and left by the rear exit. The agent ran out into the alleyway but saw no one.</p>
<p>In the meantime, the federal officers learned from Weaver that Gilbert was registered under the name of Flood. They also learned that three men may have been involved in the robberythe two who entered the bank and a third driving the getaway car. About 1:10 p. m., additional federal agents arrived at the apartment, in response to Agent Kiel's radio summons. Kiel told them that the resident of Apartment 28 was a Robert Flood who had just left. The agents obtained a key from the <span class="star-pagination">*283</span> manager, entered the apartment and searched for a person or a hiding place for a person. They found no one. But they did find an envelope containing pictures of petitioner; the pictures were seized and shown to bank employees for identification. The agents also found a notebook containing a diagram of the area surrounding the bank, a clip from an automatic pistol, and a bag containing rolls of coins bearing the marking of the robbed bank. On the basis of this information, a search warrant was issued, and the automatic clip, notebook, and coin rolls were seized. Petitioner was arrested in Pennsylvania on February 26. The items seized during the search of his apartment were introduced in evidence at his trial for murder.</p>
<p>The California Supreme Court justified the search on the ground that the police were in hot pursuit of the suspected bank robbers. The entry of the apartment was lawful. The subsequent search and seizure was lawful since the officers were trying to further identify suspects and to facilitate continued pursuit. <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/" aria-description="Citation for case: People v. Gilbert">63 Cal. 2d 690</a></span>, <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/" aria-description="Citation for case: People v. Gilbert">408 P. 2d 365</a></span>.</p>
<p>I have set forth the testimony relating to the search more fully in the Appendix to this opinion. For the reasons stated there, I cannot agree that "the facts do not appear with sufficient clarity to enable us to decide" the serious question presented.</p>
<p>Since the search and seizure took place without a warrant, it can stand only if it comes within one of the narrowly defined exceptions to the rule that a search and seizure must rest upon a validly executed search warrant. See, <i>e. g., </i><i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span>; <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">357 U. S. 493</a></span>; <i>Rios</i> v. <i>United States,</i> <span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/#261" aria-description="Citation for case: Rios v. United States">364 U. S. 253, 261</a></span>; <i>Stoner</i> v. <i>California,</i> <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#486" aria-description="Citation for case: Stoner v. California">376 U. S. 483, 486</a></span>. One of these exceptions is that officers having probable cause to arrest may enter a dwelling to make the arrest and conduct a contemporaneous <span class="star-pagination">*284</span> search of the place of arrest "in order to find and seize things connected with the crime as its fruits or as the means by which it was committed, as well as weapons and other things to effect an escape from custody." <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span>. This, of course, assumes that an arrest has been made, and that the search "is substantially contemporaneous with the arrest and is confined to the immediate vicinity of the arrest." <i>Stoner</i> v. <i>California, supra,</i> at 486. In this case, the exemption is not applicable since the arrest was made many days after the search and at a location far removed from the search.</p>
<p>Here, the officers entered the apartment, searched for petitioner and did not find him. Nevertheless, they continued searching the apartment and seized the pictures; the inescapable conclusion is that they were searching for evidence linking petitioner to the bank robbery, not for the suspected robbers. The court below said that, having legally entered the apartment, the officers "could properly look through the apartment for anything that could be used to identify the suspects or to expedite the pursuit." 63 Cal. 2d, at 707, <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/#375" aria-description="Citation for case: People v. Gilbert">408 P. 2d, at 375</a></span>.</p>
<p>Prior to this case, police could enter and search a house without a warrant only incidental to a valid arrest. If this judgment stands, the police can search a house for evidence, even though the suspect is not arrested. The purpose of the search is, in the words of the California Supreme Court, "limited to and incident to the purpose of the officers' entry"that is, to apprehend the suspected criminal. Under that doctrine, the police are given license to search for any evidence linking the home-owner with the crime. Certainly such evidence is well calculated "to identify the suspects," and will "expedite the pursuit" since the police can then concentrate on the person whose home has been ransacked. <i><span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/" aria-description="Citation for case: People v. Gilbert">Ibid.</a></span></i></p>
<p><span class="star-pagination">*285</span> The search and seizure in this case violates another limitation, which concededly the ill-starred decision in <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span>, flouted, <i>viz.,</i> that a general search for evidence, even when the police are in "hot pursuit" or have a warrant of arrest, does not make constitutional a general search of a room or of a house (<i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#463" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 463-464</a></span>). If it did, then the police, acting without a search warrant, could search more extensively than when they have a warrant. For the warrant must, as prescribed by the Fourth Amendment, "particularly" describe the "things to be seized." As stated by the Court in <i>United States</i> v. <i><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">Lefkowitz, supra,</a></span></i> at 464:</p>
<blockquote>"The authority of officers to search one's house or place of business contemporaneously with his lawful arrest therein upon a valid warrant of arrest certainly is not greater than that conferred by a search warrant issued upon adequate proof and sufficiently describing the premises and the things sought to be obtained. Indeed, the informed and deliberate determinations of magistrates empowered to issue warrants as to what searches and seizures are permissible under the Constitution are to be preferred over the hurried action of officers and others who may happen to make arrests. Security against unlawful searches is more likely to be attained by resort to search warrants than by reliance upon the caution and sagacity of petty officers while acting under the excitement that attends the capture of persons accused of crime."</blockquote>
<p>Indeed, if at the very start, there had been a search warrant authorizing the seizure of the automatic clip, notebook, and coin rolls, the envelope containing pictures of petitioner could not have been seized. "The requirement that warrants shall particularly describe the things <span class="star-pagination">*286</span> to be seized . . . prevents the seizure of one thing under a warrant describing another. As to what is to be taken, nothing is left to the discretion of the officer executing the warrant." <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 196</a></span>.</p>
<p>The modern police technique of ransacking houses, even to the point of seizing their entire contents as was done in <i>Kremen</i> v. <i>United States,</i> <span class="citation" data-id="8931353"><a href="/opinion/8940894/kremen-v-united-states/" aria-description="Citation for case: Kremen v. United States">353 U. S. 346</a></span>, is a shocking departure from the philosophy of the Fourth Amendment. For the kind of search conducted here was indeed a general search. And if the Fourth Amendment was aimed at any particular target it was aimed at that. When we take that step, we resurrect one of the deepest-rooted complaints that gave rise to our Revolution. As the Court stated in <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, 625:</p>
<blockquote>"The practice had obtained in the colonies of issuing writs of assistance to the revenue officers, empowering them, in their discretion, to search suspected places for smuggled goods, which James Otis pronounced `the worst instrument of arbitrary power, the most destructive of English liberty, and the fundamental principles of law, that ever was found in an English law book'; since they placed `the liberty of every man in the hands of every petty officer.' This was in February, 1761, in Boston, and the famous debate in which it occurred was perhaps the most prominent event which inaugurated the resistance of the colonies to the oppressions of the mother country. `Then and there,' said John Adams, `then and there was the first scene of the first act of opposition to the arbitrary claims of Great Britain. Then and there the child Independence was born.' "</blockquote>
<p>I would not allow the general search to reappear on the American scene.</p>
<p></p>
<h2>
<span class="star-pagination">*287</span> APPENDIX TO OPINION OF MR. JUSTICE DOUGLAS.</h2>
<p>As the Court notes, there is some confusion in the record respecting the timing of events surrounding the search and the breadth of purpose with which the search was conducted. The confusion results from the testimony of the agents involved.</p>
<p>Agent Kiel testified that Agents Schlatter and Onsgaard arrived at the apartment at about 1:10 and entered the apartment a minute or two after their arrival. Kiel received the photographs from Agent Schlatter between 1:25 and 1:30.</p>
<p>Agent Schlatter testified that he, Agent Onsgaard and some local police arrived at the apartment about 1:05 and that Agent Crowley and one or two local police officers arrived in another car at the same time. Schlatter briefly talked to Kiel and the apartment manager and then entered the apartment. Upon entering he saw no one. He "made a very fast search of the apartment for a person or a hiding place of a person and . . . found none." This search took "a matter of seconds or a minute at the outside" and "[a]fter we had searched for [a] person or persons, and no one was there, it then became a matter of a stake-out under the assumption that the person or persons involved would come back." It seemed to Schlatter that "an agent had [the photograph] in his hand," when he first saw it, that it "was in the hands of an agent or an officer," and Schlatter had "a vague recollection that [the agent or officer told him he had found it] in the bedroom . . . ." There were a number of photographs. Schlatter took the photographs out to Kiel and instructed him to take one of them to the savings and loan association and see if anyone there could recognize the photograph. Schlatter testified that he was in the apartment for about 30 minutes after making the search and left other agents behind when he left.</p>
<p><span class="star-pagination">*288</span> Agent Crowley testified that he entered the apartment "around 1:30, give or take a few minutes either way" and that he would say that the other officers had been in the apartment less than five minutes before he entered. He believed that "the officers and the other agent who had been with [him] at the rear of the building when the first entry was made, entered with [him]." When Crowley entered the apartment it "had already been searched for people." He received "instructions . . . to look through the apartment for anything we could find that we could use to identify or continue the pursuit of this person without conducting a detailed search." In the bedroom, on the dresser, Crowley saw an envelope bearing the name "Marlboro Photo Studio"; it appeared to him to be an envelope containing photos and he could see that there was something inside. Crowley opened the envelope and saw several copies of photographs. He discussed the matter with "Onsgaard who was in charge in the building and he instructed [Crowley] to give it to another agent for him to utilize in pursuing the investigation, and [he was] reasonably certain that that agent was Mr. Schlatter." This was about 1:30 according to Crowley. In the course of his search which turned up the photographs, Crowley "turned over [items] to see what was on the reverse, such as business cards, sales slips from local stores, that sort of item which might have been folded and would appear to possibly contain information of value to pursuit." He relayed the information obtained in this manner to the man coordinating the operation. Crowley remained in the apartment until the next morning.</p>
<p>Agent Townsend testified that he arrived at the apartment "[s]ometime between perhaps 1:30 and 2:00." Within an hour of his arrival, he began a search. Townsend testified that he, Agent Crowley, another agent and a local officer "looked through the bedroom closet and <span class="star-pagination">*289</span> the dresser and I think the headstand." This was after it was known that no one, other than agents and police officers, was in the apartment. Townsend stated that the agents and officers were "[i]n and out of the bedroom," that he found money in the bedroom dresser about an hour after he arrived in the apartment, and that he could not "say specifically" whether Crowley was there at that time.</p>
<p>Thus, there is some conflict regarding the times at which the events took place and with respect to the nature of the searches conducted by the various officers. The way I read the record, however, it is not in such a state "that the facts do not appear with sufficient clarity to enable us to decide" the question presented. Crowley's testimony that he came upon the photographs while searching "for anything . . . that we could use to identify or continue the pursuit" stands uncontradicted, as does his testimony that the apartment had already been searched for a person prior to his search uncovering the photographs. Schlatter's testimony that the operation "became a matter of a stake-out" after the unsuccessful search for a person does not contradict Crowley's testimony. A search for identifying evidence is certainly compatible with a "stake-out." And Crowley best knew what he was doing when he discovered the photographs. Nor does Townsend's testimony that he and others, perhaps including Crowley, conducted a detailed search conflict with Crowley's testimony. First, the record indicates that the detailed search was conducted after the photographs had been found. According to the testimony of Kiel and Schlatter, Schlatter gave the photographs to Kiel at about 1:30; according to Townsend, he arrived sometime between 1:30 and 2. Second, even if the detailed search took place before Crowley found the photographs and Crowley participated in that search, that does not indicate that Crowley's search which turned <span class="star-pagination">*290</span> up the photographs was more limited than Crowley claimed. If anything, it would indicate that his search was more general than he stated. Finally, Townsend's testimony as to the general search does not conflict with Schlatter's testimony that the operation became a "stake-out" after the suspect was not found. As I have said, a "stake-out" does not preclude a detailed search for evidence. And, the record indicates that Schlatter was not in the apartment when Townsend and the others conducted the detailed search.</p>
<p>The way I read the record, the photographs were discovered in the course of a general search for evidence. But even if Crowley is not believed and his testimony relating to the nature of his search is thrown out and it is simply assumed that he came upon the envelope in the course of a search for the suspect, there was no reason to pry into the envelope and seize the picturesother than to obtain evidence. An envelope would contain neither the suspect nor the weapon.</p>
<p>MR. JUSTICE WHITE, whom MR. JUSTICE HARLAN and MR. JUSTICE STEWART join, concurring in part and dissenting in part.</p>
<p>I concur in Parts I, II, and III of the Court's opinion, but for the reasons stated in my separate opinion in <i>United States</i> v. <i>Wade, ante,</i> p. 250, I dissent from Part IV of the Court's opinion and would therefore affirm the judgment of the Supreme Court of California.</p>
<p>MR. JUSTICE FORTAS, with whom THE CHIEF JUSTICE joins, concurring in part and dissenting in part.</p>
<p>I concur in the resultthe vacation of the judgment of the California Supreme Court and the remand of the casebut I do not believe that it is adequate. I would reverse and remand for a new trial on the additional ground that petitioner was entitled by the Sixth and <span class="star-pagination">*291</span> Fourteenth Amendments to be advised that he had a right to counsel before and in connection with his response to the prosecutor's demand for a handwriting exemplar.</p>
<p>1. The giving of a handwriting exemplar is a "critical stage" of the proceeding, as my Brother BLACK states. It is a "critical stage" as much as is a lineup. See <i>United States</i> v. <i>Wade, ante,</i> p. 218. Depending upon circumstances, both may be inoffensive to the Constitution, totally fair to the accused, and entirely reliable for the administration of justice. On the other hand, each may be constitutionally offensive, totally unfair to the accused, and prejudicial to the ascertainment of truth. An accused whose handwriting exemplar is sought needs counsel: Is he to write "Your money or your life?" Is he to emulate the holdup note by using red ink, brown paper, large letters, etc.? Is the demanded handwriting exemplar, in effect, an inculpationa confession? Cf. the eloquent arguments as to the need for counsel, in the Court's opinion in <i>United States</i> v. <i>Wade, supra</i><i>.</i></p>
<p>2. The Court today appears to hold that an accused may be compelled to give a handwriting exemplar. Cf. <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966). Presumably, he may be punished if he adamantly refuses. Unlike blood, handwriting cannot be extracted by a doctor from an accused's veins while the accused is subjected to physical restraint, which <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i> permits. So presumably, on the basis of the Court's decision, trial courts may hold an accused in contempt and keep him in jail indefinitelyuntil he gives a handwriting exemplar.</p>
<p>This decision goes beyond <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>.</i> Here the accused, in the absence of any warning that he has a right to counsel, is compelled to cooperate, not merely to submit; to engage in a volitional act, not merely to suffer the inevitable consequences of arrest and state custody; to take affirmative action which may not merely identify <span class="star-pagination">*292</span> him, but tie him directly to the crime. I dissented in <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>.</i> For reasons stated in my separate opinion in <i>United States</i> v. <i>Wade, supra</i><i>,</i> I regard the extension of <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i> as impermissible.</p>
<p>In <i>Wade,</i> the accused, who is compelled to utter the words used by the criminal in the heat of his act, has at least the comfort of counseleven if the Court denies that the accused may refuse to speak the wordsbecause the compelled utterance occurs in the course of a lineup. In the present case, the Court deprives him of even this source of comfort and whatever protection counsel's ingenuity could provide in face of the Court's opinion. This is utterly insupportable, in my respectful opinion. This is not like fingerprinting, measuring, photographing or even blood-taking. It is a process involving the use of discretion. It is capable of abuse. It is in the stream of inculpation. Cross-examination can play only a limited role in offsetting false inference or misleading coincidence from a "stacked" handwriting exemplar. The Court's reference to the efficacy of cross-examination in this situation is much more of a comfort to an appellate court than a source of solace to the defendant and his counsel.</p>
<p>3. I agree with the Court's condemnation of the lineup identifications here and the consequent in-court identifications, and I join in this part of its opinion. I would also reverse and remand for a new trial because of the use of the handwriting exemplars which were unconstitutionally obtained in the absence of advice to the accused as to the availability of counsel. I could not conclude that the violation of the privilege against self-incrimination implicit in the facts relating to the exemplars was waived in the absence of advice as to counsel. <i>In re Gault,</i> <span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/#41" aria-description="Citation for case: In Re GAULT">387 U. S. 1, 41-42</a></span> (1967); <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966).</p>
<h2>NOTES</h2>
<p>[1]  The California Supreme Court also held that ". . . the erroneous admission of King's statements at the trial on the issue of guilt was not prejudicial on the question of Gilbert's penalty," again citing <i>Fahy,</i> 63 Cal. 2d, at 702, <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/#372" aria-description="Citation for case: People v. Gilbert">408 P. 2d, at 372</a></span>.</p>
<p>[2]  The record in <i>Gilbert</i> v. <i>United States,</i> <span class="citation" data-id="9452205"><a href="/opinion/273233/jesse-james-gilbert-v-united-states/" aria-description="Citation for case: Jesse James Gilbert v. United States">366 F. 2d 923</a></span>, involving the federal prosecutions of Gilbert, apparently contains many more details of what occurred at the lineup. The opinion of the Court of Appeals for the Ninth Circuit states, <span class="citation" data-id="9452205"><a href="/opinion/273233/jesse-james-gilbert-v-united-states/" aria-description="Citation for case: Jesse James Gilbert v. United States">366 F. 2d, at 935</a></span>:
</p>
<p>"The lineup occurred on March 26, 1964, after Gilbert had been indicted and had obtained counsel. It was held in an auditorium used for that purpose by the Los Angeles police. Some ten to thirteen prisoners were placed on a lighted stage. The witnesses were assembled in a darkened portion of the room, facing the stage and separated from it by a screen. They could see the prisoners but could not be seen by them. State and federal officers were also present and one of them acted as `moderator' of the proceedings.</p>
<p>"Each man in the lineup was identified by number, but not by name. Each man was required to step forward into a marked circle, to turn, presenting both profiles as well as a face and back view, to walk, to put on or take off certain articles of clothing. When a man's number was called and he was directed to step into the circle, he was asked certain questions: where he was picked up, whether he owned a car, whether, when arrested, he was armed, where he lived. Each was also asked to repeat certain phrases, both in a loud and in a soft voice, phrases that witnesses to the crimes had heard the robbers use: `Freeze, this is a stickup; this is a holdup; empty your cash drawer; this is a heist; don't anybody move.'</p>
<p>"Either while the men were on the stage, or after they were taken from it, it is not clear which, the assembled witnesses were asked if there were any that they would like to see again, and told that if they had doubts, now was the time to resolve them. Several gave the numbers of men they wanted to see, including Gilbert's. While the other prisoners were no longer present, Gilbert and 2 or 3 others were again put through a similar procedure. Some of the witnesses asked that a particular prisoner say a particular phrase, or walk a particular way. After the lineup, the witnesses talked to each other; it is not clear that they did so during the lineup. They did, however, in each other's presence, call out the numbers of men they could identify."</p>
<p>[3]  There is a split among the States concerning the admissibility of prior extrajudicial identifications, as independent evidence of identity, both by the witness and third parties present at the prior identification. See <span class="citation no-link">71 ALR 2d 449</span>. It has been held that the prior identification is hearsay, and, when admitted through the testimony of the identifier, is merely a prior consistent statement. The recent trend, however, is to admit the prior identification under the exception that admits as substantive evidence a prior communication by a witness who is available for cross-examination at trial. See 5 ALR 2d Later Case Service 1225-1228. That is the California rule. In <i>People</i> v. <i>Gould,</i> <span class="citation" data-id="1801408"><a href="/opinion/1801408/people-v-gould/#626" aria-description="Citation for case: People v. Gould">54 Cal. 2d 621, 626</a></span>, <span class="citation" data-id="1801408"><a href="/opinion/1801408/people-v-gould/#867" aria-description="Citation for case: People v. Gould">354 P. 2d 865, 867</a></span>, the Court said:
</p>
<p>"Evidence of an extrajudicial identification is admissible, not only to corroborate an identification made at the trial (<i>People</i> v. <i>Slobodion,</i> <span class="citation" data-id="1193668"><a href="/opinion/1193668/people-v-slobodion/#560" aria-description="Citation for case: People v. Slobodion">31 Cal. 2d 555, 560</a></span> [<span class="citation" data-id="1193668"><a href="/opinion/1193668/people-v-slobodion/" aria-description="Citation for case: People v. Slobodion">191 P. 2d 1</a></span>]), but as independent evidence of identity. Unlike other testimony that cannot be corroborated by proof of prior consistent statements unless it is first impeached . . . evidence of an extrajudicial identification is admitted regardless of whether the testimonial identification is impeached, because the earlier identification has greater probative value than an identification made in the courtroom after the suggestions of others and the circumstances of the trial may have intervened to create a fancied recognition in the witness' mind. . . . The failure of the witness to repeat the extrajudicial identification in court does not destroy its probative value, for such failure may be explained by loss of memory or other circumstances. The extrajudicial identification tends to connect the defendant with the crime, and the principal danger of admitting hearsay evidence is not present since the witness is available at the trial for cross-examination."</p>
<p>New York deals with the subject in a statute. See N. Y. Code Crim. Proc. § 393-b.</p>
<p>[*]  The Court dismisses as improvidently granted the Fourth Amendment search-and-seizure question raised by Gilbert in this case. I dissent from this, because I would decide that question against Gilbert. However, since the Court refuses to decide that question, I see no reason for expressing my views at length.</p>
<p>[]  On that phase of the case I agree with MR. JUSTICE BLACK and MR. JUSTICE FORTAS.</p>

</div>
```

---
