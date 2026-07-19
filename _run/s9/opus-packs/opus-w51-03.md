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

## GROUP: content/cases/United States v. Arvizu.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Arvizu"
type: case
citation: "534 U.S. 266 (2002)"
parallel_cite: "122 S. Ct. 744; 151 L. Ed. 2d 740"
neutral_cite: 2002 U.S. LEXIS 490
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2002
date_decided: 2002-01-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2002-01-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Arvizu
  varies_by_point: false
  scope_note: "Good law; reaffirms the totality-of-the-circumstances reasonable-suspicion standard."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118474/united-states-v-arvizu/"
  cluster_id: 118474
  opinion_id: 118474
  identity_checked: true
homes:
  - page: "[[Reasonable Suspicion]]"
    role: "Key — Progeny / Refinement"
related: ["[[Terry v. Ohio]]", "[[United States v. Cortez]]", "[[Illinois v. Wardlow]]", "[[Ornelas v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "reasonable-suspicion"]
holding: "Reasonable suspicion is judged on the totality of the circumstances — the \"whole picture\" — and reviewing courts may NOT use a…"
lake:
  record_id: United States v. Arvizu
  status: verified
  projected_at: 2026-07-06
---

# United States v. Arvizu

*534 U.S. 266 (2002)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Border Patrol agent on a remote Arizona back road stopped a minivan after a sensor alert and a series of observations: the route avoided a checkpoint, the timing coincided with a shift change, the driver was rigid and avoided eye contact, and the children in the back waved in an oddly mechanical way as if instructed, with their knees raised over what turned out to be packages. The agent found over 100 pounds of marijuana. The Ninth Circuit had rejected several of the factors as individually innocent and reversed.

## Issue
Whether reasonable suspicion is assessed by examining each factor in isolation and discarding those susceptible to innocent explanation, or by evaluating the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]].

## Rule
Reasonable suspicion is judged on the whole picture, not factor-by-factor: reviewing courts "must look at the 'totality of the circumstances' of each case to see whether the detaining officer has a 'particularized and objective basis' for suspecting legal wrongdoing." — 534 U.S. at 273. ^pin-273

The Court rejected the appellate court's approach of evaluating each factor in isolation: "*Terry*, however, precludes this sort of divide-and-conquer analysis." — *Id.* at 274. ^pin-274

## Application
Viewing the agent's observations together — and giving due weight to his specialized training and experience with the area's smuggling patterns — the combination of the avoided checkpoint, the suspicious timing, the driver's stiff demeanor, and the children's choreographed waving with their feet propped on the cargo supplied a particularized and objective basis to suspect criminal activity. The Ninth Circuit erred by dismissing factors individually; assessed as a whole, the stop was supported by reasonable suspicion.

## Conclusion
The stop was supported by reasonable suspicion; the Ninth Circuit's reversal was itself reversed. Courts must assess reasonable suspicion under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], not by isolating and discounting individual factors.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Arvizu* applies the reasonable-suspicion standard of [[Terry v. Ohio]] and the "whole picture"/"particularized and objective basis" formulation of [[United States v. Cortez]]; it parallels the totality approach approved in [[Illinois v. Wardlow]] and the deference to officer inferences in [[Ornelas v. United States]].

## Appears on
- [[Reasonable Suspicion]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Arvizu*, 534 U.S. 266 (2002) — https://www.courtlistener.com/opinion/118474/united-states-v-arvizu/ — pinpoints: 273, 274.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d05ef01473c9f322", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "534 U.S. 266 (2002)", "court": "U.S. Supreme Court", "neutral_cite": "2002 U.S. LEXIS 490", "official_citation_present": true, "parallel_cite": "122 S. Ct. 744; 151 L. Ed. 2d 740", "title": "United States v. Arvizu", "year": "2002"}}
{"assertion_id": "6b4d5fde4a37aef6", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Suspicion"}, "payload": {"home": "Reasonable Suspicion", "role": "Key — Progeny / Refinement", "title": "United States v. Arvizu"}}
{"assertion_id": "cb1c17c3ff2bd018", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Reasonable suspicion is judged on the totality of the circumstances — the \\\"whole picture\\\" — and reviewing courts may NOT use a…", "title": "United States v. Arvizu"}}
{"assertion_id": "94c2dedbb11eb1c8", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Arvizu"}}
{"assertion_id": "b22d3103c6e37bec", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2002-01-15", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Arvizu", "field_i_validity": "good_law", "scope_note": "Good law; reaffirms the totality-of-the-circumstances reasonable-suspicion standard.", "title": "United States v. Arvizu", "varies_by_point": "false"}}
```

### lake record — United States v. Arvizu

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Arvizu",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Arvizu",
    "case_name_short": "Arvizu",
    "case_name_full": "United States v. Arvizu",
    "input_case_name": "United States v. Arvizu",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2002-01-15",
    "year": 2002,
    "docket": null,
    "cluster_id": 118474,
    "lead_opinion_id": 118474,
    "sibling_ids": [
      118474,
      9434181,
      9434182
    ],
    "absolute_url": "/opinion/118474/united-states-v-arvizu/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "534 U.S. 266",
      "volume": "534",
      "reporter": "U.S.",
      "page": "266",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "122 S. Ct. 744",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "744",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "151 L. Ed. 2d 740",
        "volume": "151",
        "reporter": "L. Ed. 2d",
        "page": "740",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2002 U.S. LEXIS 490",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "490",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "534 U.S. 266",
        "volume": "534",
        "reporter": "U.S.",
        "page": "266",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "122 S. Ct. 744",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "744",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "151 L. Ed. 2d 740",
        "volume": "151",
        "reporter": "L. Ed. 2d",
        "page": "740",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 U.S. LEXIS 490",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "490",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "534 U.S. 266",
    "official_selection": {
      "court_class": "scotus",
      "selected": "534 U.S. 266",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-273",
      "page": null,
      "quote": "--- # United States v. Arvizu *534 U.S. 266 (2002)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Border Patrol agent on a remote Arizona back road stopped a minivan after a sensor alert and a series of observations: the route avoided a checkpoint, the timing coincided with a shift change, the driver was rigid and avoided eye contact, and the children in the back waved in an oddly mechanical way as if instructed, with their knees raised over what turned out to be packages. The agent found over 100 pounds of marijuana. The Ninth Circuit had rejected several of the factors as individually innocent and reversed. ## Issue Whether reasonable suspicion is assessed by examining each factor in isolation and discarding those susceptible to innocent explanation, or by evaluating the totality of the circumstances. ## Rule Reasonable suspicion is judged on the whole picture, not factor-by-factor: reviewing courts",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-274",
      "page": null,
      "quote": "*Terry*, however, precludes this sort of divide-and-conquer analysis.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2002-01-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Arvizu",
    "varies_by_point": false,
    "scope_note": "Good law; reaffirms the totality-of-the-circumstances reasonable-suspicion standard.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Marlon Juan Lall v. the State of Texas",
          "cluster_id": 10046849,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane1_negative"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460854,
          "cite": [
            "583 U.S. 48",
            "138 S. Ct. 577",
            "199 L. Ed. 2d 453",
            "2018 U.S. LEXIS 760"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rodriguez v. United States",
          "cluster_id": 2795278,
          "cite": [
            "575 U.S. 348",
            "135 S. Ct. 1609",
            "191 L. Ed. 2d 492",
            "2015 U.S. LEXIS 2807",
            "83 U.S.L.W. 4241",
            "25 Fla. L. Weekly Fed. S 191"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shrestha v. Holder",
          "cluster_id": 1434187,
          "cite": [
            "590 F.3d 1034",
            "2010 U.S. App. LEXIS 138",
            "2010 WL 10982"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ford v. State",
          "cluster_id": 1355298,
          "cite": [
            "158 S.W.3d 488",
            "2005 Tex. Crim. App. LEXIS 399",
            "2005 WL 544796"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wiede v. State",
          "cluster_id": 1404049,
          "cite": [
            "214 S.W.3d 17",
            "2007 Tex. Crim. App. LEXIS 100",
            "2007 WL 257624"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Prado Navarette v. California",
          "cluster_id": 2670795,
          "cite": [
            "188 L. Ed. 2d 680",
            "134 S. Ct. 1683",
            "2014 U.S. LEXIS 2930",
            "82 U.S.L.W. 4282",
            "572 U.S. 393",
            "24 Fla. L. Weekly Fed. S 690",
            "2014 WL 1577513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460811,
          "cite": [
            "583 U.S. 48"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Madden v. State",
          "cluster_id": 1404569,
          "cite": [
            "242 S.W.3d 504",
            "2007 Tex. Crim. App. LEXIS 1802",
            "2007 WL 4404270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
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
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Letner and Tobin",
          "cluster_id": 2630926,
          "cite": [
            "235 P.3d 62",
            "50 Cal. 4th 99",
            "112 Cal. Rptr. 3d 746",
            "2010 Cal. LEXIS 7290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
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
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thomas L. Feathers Kathleen Feathers v. William Aey J.P. Donohue, City of Akron",
          "cluster_id": 780866,
          "cite": [
            "319 F.3d 843",
            "2003 U.S. App. LEXIS 2642",
            "2003 WL 296924"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Banks",
          "cluster_id": 131146,
          "cite": [
            "157 L. Ed. 2d 343",
            "124 S. Ct. 521",
            "540 U.S. 31",
            "2003 U.S. LEXIS 8966"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Branch",
          "cluster_id": 1026476,
          "cite": [
            "537 F.3d 328",
            "2008 U.S. App. LEXIS 17710",
            "2008 WL 3854500"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Eleuterio Lopez-Moreno, Also Known as Eleuterio Lopez",
          "cluster_id": 791593,
          "cite": [
            "420 F.3d 420",
            "2005 U.S. App. LEXIS 16564",
            "2005 WL 1864257"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yul Darnell Givan, United States of America v. Wayne Torrence",
          "cluster_id": 780959,
          "cite": [
            "320 F.3d 452"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Pedro Luis Christopher Tinoco",
          "cluster_id": 75998,
          "cite": [
            "304 F.3d 1088",
            "59 Fed. R. Serv. 3d 1146",
            "2002 U.S. App. LEXIS 18479",
            "2002 WL 2013777"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brigham",
          "cluster_id": 35972,
          "cite": [
            "382 F.3d 500",
            "2004 WL 1854552"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ricky A. Caruthers",
          "cluster_id": 795277,
          "cite": [
            "458 F.3d 459",
            "2006 U.S. App. LEXIS 20569",
            "2006 WL 2320942"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shepherd v. State",
          "cluster_id": 2190342,
          "cite": [
            "273 S.W.3d 681",
            "2008 Tex. Crim. App. LEXIS 855",
            "2008 WL 4149707"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Pack",
          "cluster_id": 150729,
          "cite": [
            "612 F.3d 341",
            "2010 U.S. App. LEXIS 14562",
            "2010 WL 2777061"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Chase",
          "cluster_id": 1563033,
          "cite": [
            "960 A.2d 108",
            "599 Pa. 80",
            "2008 Pa. LEXIS 2180",
            "2008 WL 5002958"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Barbeau",
          "cluster_id": 4543099,
          "cite": [
            "301 Neb. 293",
            "917 N.W.2d 913"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James W. Smoak v. Eric Hall, David Bush Jeff Phann Tim McHood Brian Brock Jerry Andrews, Lieutenant",
          "cluster_id": 795446,
          "cite": [
            "460 F.3d 768",
            "2006 U.S. App. LEXIS 21661",
            "2006 WL 2455321"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
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
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118474 OR 9434181 OR 9434182) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjcwMzcxMjAwMDAwJnM9OTMyODM0NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118474+OR+9434181+OR+9434182%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118474 OR 9434181 OR 9434182)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTQmcz03Nzk1NjEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118474+OR+9434181+OR+9434182%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118474 OR 9434181 OR 9434182)",
        "reviewed": 192,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 192,
        "triage_read": 1,
        "triage_snippet_classified": 191
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118474 OR 9434181 OR 9434182)",
    "indexed_citing_opinions": 2098,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118474,
        "count": 1638,
        "count_source": "search"
      },
      {
        "opinion_id": 9434181,
        "count": 489,
        "count_source": "search"
      },
      {
        "opinion_id": 9434182,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3942,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-arvizu.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MTcwODgmcz0xMDYxODc3OSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118474+OR+9434181+OR+9434182%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118474,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118474,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118474,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118474,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118474,
        "cited_id": 112239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118474,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118474,
        "cited_id": 118326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118474,
        "cited_id": 771188,
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
    "date_created": "2026-07-05T22:11:48Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:12:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:12:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:17:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:12:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Arvizu

```
<div>
<center><b><span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/" aria-description="Citation for case: United States v. Arvizu">534 U.S. 266</a></span> (2002)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
ARVIZU</h1></center>
<center>No. 00-1519.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued November 27, 2001.</center>
<center>Decided January 15, 2002.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
<p><span class="star-pagination">*268</span> Rehnquist, C. J., delivered the opinion for a unanimous Court. Scalia, J., filed a concurring opinion, <i>post,</i> p. 278.</p>
<p><i>Austin C. Schlick</i> argued the cause for the United States. With him on the briefs were <i>Solicitor General Olson, Assistant Attorney General Chertoff, Deputy Solicitor General Dreeben,</i> and <i>Deborah Watson.</i> </p>
<p><i>Victoria A. Brambl</i> argued the cause for respondent. With her on the brief was <i>Fredric F. Kay.</i><sup>[*]</sup></p>
<p><span class="star-pagination">*268</span> Chief Justice Rehnquist delivered the opinion of the Court.</p>
<p>Respondent Ralph Arvizu was stopped by a border patrol agent while driving on an unpaved road in a remote area of southeastern Arizona. A search of his vehicle turned up more than 100 pounds of marijuana. The District Court for the District of Arizona denied respondent's motion to suppress, but the Court of Appeals for the Ninth Circuit reversed. In the course of its opinion, it categorized certain factors relied upon by the District Court as simply out of bounds in deciding whether there was "reasonable suspicion" for the stop. We hold that the Court of Appeals' methodology was contrary to our prior decisions and that it reached the wrong result in this case.</p>
<p>On an afternoon in January 1998, Agent Clinton Stoddard was working at a border patrol checkpoint along U. S. Highway 191 approximately 30 miles north of Douglas, Arizona. App. 22, 24. See Appendix, <i>infra</i> (containing a map of the area noting the location of the checkpoint and other points important to this case). Douglas has a population of about 13,000 and is situated on the United States-Mexico border in the southeastern part of the State. Only two highways lead north from Douglas. See App. 157. Highway 191 leads north to Interstate 10, which passes through Tucson and Phoenix. State Highway 80 heads northeast through less populated areas toward New Mexico, skirting south and east of the portion of the Coronado National Forest that lies approximately 20 miles northeast of Douglas.<sup>[1]</sup></p>
<p>The checkpoint is located at the intersection of 191 and Rucker Canyon Road, an unpaved east-west road that connects 191 and the Coronado National Forest. When the checkpoint is operational, border patrol agents stop the traffic <span class="star-pagination">*269</span> on 191 as part of a coordinated effort to stem the flow of illegal immigration and smuggling across the international border. See <i>id.,</i> at 20-21. Agents use roving patrols to apprehend smugglers trying to circumvent the checkpoint by taking the backroads, including those roads through the sparsely populated area between Douglas and the national forest. <i>Id.,</i> at 21-22, 26, 80. Magnetic sensors, or "intrusion devices," facilitate agents' efforts in patrolling these areas. See <i>id.,</i> at 25. Directionally sensitive, the sensors signal the passage of traffic that would be consistent with smuggling activities. <i>Ibid.;</i> Tr. of Oral Arg. 23-24.</p>
<p>Sensors are located along the only other northbound road from Douglas besides Highways 191 and 80: Leslie Canyon Road. Leslie Canyon Road runs roughly parallel to 191, about halfway between 191 and the border of the Coronado National Forest, and ends when it intersects Rucker Canyon Road. It is unpaved beyond the 10-mile stretch leading out of Douglas and is very rarely traveled except for use by local ranchers and forest service personnel. App. 26. Smugglers commonly try to avoid the 191 checkpoint by heading west on Rucker Canyon Road from Leslie Canyon Road and thence to Kuykendall Cutoff Road, a primitive dirt road that leads north approximately 12 miles east of 191. <i>Id.,</i> at 29-30. From there, they can gain access to Tucson and Phoenix. <i>Id.,</i> at 30.</p>
<p>Around 2:15 p.m., Stoddard received a report via Douglas radio that a Leslie Canyon Road sensor had been triggered. <i>Id.,</i> at 24. This was significant to Stoddard for two reasons. First, it suggested to him that a vehicle might be trying to circumvent the checkpoint. <i>Id.,</i> at 27. Second, the timing coincided with the point when agents begin heading back to the checkpoint for a shift change, which leaves the area unpatrolled. <i>Id.,</i> at 26, 47. Stoddard knew that alien smugglers did extensive scouting and seemed to be most active when agents were en route back to the checkpoint. Another border patrol agent told Stoddard that the same <span class="star-pagination">*270</span> sensor had gone off several weeks before and that he had apprehended a minivan using the same route and witnessed the occupants throwing bundles of marijuana out the door. <i>Id.,</i> at 27.</p>
<p>Stoddard drove eastbound on Rucker Canyon Road to investigate. As he did so, he received another radio report of sensor activity. <i>Id.,</i> at 29. It indicated that the vehicle that had triggered the first sensor was heading westbound on Rucker Canyon Road. He continued east, passing Kuykendall Cutoff Road. He saw the dust trail of an approaching vehicle about a half mile away. <i>Id.,</i> at 31. Stoddard had not seen any other vehicles and, based on the timing, believed that this was the one that had tripped the sensors. <i>Id.,</i> at 31-32. He pulled off to the side of the road at a slight slant so he could get a good look at the oncoming vehicle as it passed by. <i>Id.,</i> at 32.</p>
<p>It was a minivan, a type of automobile that Stoddard knew smugglers used. <i>Id.,</i> at 33. As it approached, it slowed dramatically, from about 50-55 to 25-30 miles per hour. <i>Id.,</i>  at 32, 57. He saw five occupants inside. An adult man was driving, an adult woman sat in the front passenger seat, and three children were in the back. <i>Id.,</i> at 33-34. The driver appeared stiff and his posture very rigid. He did not look at Stoddard and seemed to be trying to pretend that Stoddard was not there. <i>Id.,</i> at 33. Stoddard thought this suspicious because in his experience on patrol most persons look over and see what is going on, and in that area most drivers give border patrol agents a friendly wave. <i>Id.,</i> at 59. Stoddard noticed that the knees of the two children sitting in the very back seat were unusually high, as if their feet were propped up on some cargo on the floor. <i>Id.,</i> at 34.</p>
<p>At that point, Stoddard decided to get a closer look, so he began to follow the vehicle as it continued westbound on Rucker Canyon Road toward Kuykendall Cutoff Road. <i>Id.,</i>  at 34-35. Shortly thereafter, all of the children, though <span class="star-pagination">*271</span> still facing forward, put their hands up at the same time and began to wave at Stoddard in an abnormal pattern. <i>Id.,</i> at 35, 61. It looked to Stoddard as if the children were being instructed. Their odd waving continued on and off for about four to five minutes. <i>Id.,</i> at 35, 73.</p>
<p>Several hundred feet before the Kuykendall Cutoff Road intersection, the driver signaled that he would turn. <i>Id.,</i>  at 36. At one point, the driver turned the signal off, but just as he approached the intersection he put it back on and abruptly turned north onto Kuykendall. The turn was significant to Stoddard because it was made at the last place that would have allowed the minivan to avoid the checkpoint. <i>Id.,</i> at 37. Also, Kuykendall, though passable by a sedan or van, is rougher than either Rucker Canyon or Leslie Canyon Roads, and the normal traffic is four-wheel-drive vehicles. <i>Id.,</i> at 36, 63-64. Stoddard did not recognize the minivan as part of the local traffic agents encounter on patrol, <i>id.,</i>  at 37, and he did not think it likely that the minivan was going to or coming from a picnic outing. He was not aware of any picnic grounds on Turkey Creek, which could be reached by following Kuykendall Cutoff all the way up. <i>Id.,</i>  at 54. He knew of picnic grounds and a Boy Scout camp east of the intersection of Rucker Canyon and Leslie Canyon Roads, <i>id.,</i> at 31, 53, 54, but the minivan had turned west at that intersection. And he had never seen anyone picnicking or sightseeing near where the first sensor went off. <i>Id.,</i> at 53, 75.</p>
<p>Stoddard radioed for a registration check and learned that the minivan was registered to an address in Douglas that was four blocks north of the border in an area notorious for alien and narcotics smuggling. <i>Id.,</i> at 37-38, 66-67. After receiving the information, Stoddard decided to make a vehicle stop. <i>Id.,</i> at 38. He approached the driver and learned that his name was Ralph Arvizu. Stoddard asked if respondent would mind if he looked inside and searched <span class="star-pagination">*272</span> the vehicle. <i>Id.,</i> at 43. Respondent agreed, and Stoddard discovered marijuana in a black duffel bag under the feet of the two children in the back seat. <i>Id.,</i> at 45-46. Another bag containing marijuana was behind the rear seat. <i>Id.,</i>  at 46. In all, the van contained 128.85 pounds of marijuana, worth an estimated $99,080. Brief for United States 8.</p>
<p>Respondent was charged with possession with intent to distribute marijuana in violation of <span class="citation no-link">21 U. S. C. § 841</span>(a)(1) (1994 ed.). He moved to suppress the marijuana, arguing among other things that Stoddard did not have reasonable suspicion to stop the vehicle as required by the Fourth Amendment. After holding a hearing where Stoddard and respondent testified, the District Court for the District of Arizona ruled otherwise. App. to Pet. for Cert. 21a. It pointed to a number of the facts described above and noted particularly that any recreational areas north of Rucker Canyon would have been accessible from Douglas via 191 and another paved road, making it unnecessary to take a 40-to50-mile trip on dirt roads. <i><span class="citation no-link">Id.,</span></i> at 22a.</p>
<p>The Court of Appeals for the Ninth Circuit reversed. <span class="citation" data-id="771188"><a href="/opinion/771188/united-states-v-ralph-arvizu/" aria-description="Citation for case: United States v. Ralph Arvizu">232 F. 3d 1241</a></span> (2000). In its view, fact-specific weighing of circumstances or other multifactor tests introduced "a troubling degree of uncertainty and unpredictability" into the Fourth Amendment analysis. <span class="citation" data-id="771188"><a href="/opinion/771188/united-states-v-ralph-arvizu/#1248" aria-description="Citation for case: United States v. Ralph Arvizu"><i>Id.,</i> at 1248</a></span> (internal quotation marks omitted). It therefore "attempt[ed] . . . to describe and clearly delimit the extent to which certain factors may be considered by law enforcement officers in making stops such as the stop involv[ing]" respondent. <i><span class="citation" data-id="771188"><a href="/opinion/771188/united-states-v-ralph-arvizu/" aria-description="Citation for case: United States v. Ralph Arvizu">Ibid.</a></span></i>  After characterizing the District Court's analysis as relying on a list of 10 factors, the Court of Appeals proceeded to examine each in turn. It held that seven of the factors, including respondent's slowing down, his failure to acknowledge Stoddard, the raised position of the children's knees, and their odd waving carried little or no weight in the reasonable-suspicion calculus. The remaining factorsthe <span class="star-pagination">*273</span> road's use by smugglers, the temporal proximity between respondent's trip and the agents' shift change, and the use of minivans by smugglerswere not enough to render the stop permissible. <span class="citation" data-id="771188"><a href="/opinion/771188/united-states-v-ralph-arvizu/#1251" aria-description="Citation for case: United States v. Ralph Arvizu"><i>Id.,</i> at 1251</a></span>. We granted certiorari to review the decision of the Court of Appeals because of its importance to the enforcement of federal drug and immigration laws. <span class="citation multiple-matches"><a href="/c/U.%20S./532/1065/">532 U. S. 1065</a></span> (2001).</p>
<p>The Fourth Amendment prohibits "unreasonable searches and seizures" by the Government, and its protections extend to brief investigatory stops of persons or vehicles that fall short of traditional arrest. <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#9" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 9</a></span> (1968); <i>United States</i> v. <i>Cortez,</i> <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 417</a></span> (1981). Because the "balance between the public interest and the individual's right to personal security," <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975), tilts in favor of a standard less than probable cause in such cases, the Fourth Amendment is satisfied if the officer's action is supported by reasonable suspicion to believe that criminal activity "`may be afoot,' " <i>United States</i> v. <i>Sokolow,</i> <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#7" aria-description="Citation for case: United States v. Sokolow">490 U. S. 1, 7</a></span> (1989) (quoting <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 30</a></span>). See also <i>Cortez,</i> <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez">449 U. S., at 417</a></span> ("An investigatory stop must be justified by some objective manifestation that the person stopped is, or is about to be, engaged in criminal activity").</p>
<p>When discussing how reviewing courts should make reasonable-suspicion determinations, we have said repeatedly that they must look at the "totality of the circumstances" of each case to see whether the detaining officer has a "particularized and objective basis" for suspecting legal wrongdoing. See, <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez"><i>e. g., id.,</i> at 417-418</a></span>. This process allows officers to draw on their own experience and specialized training to make inferences from and deductions about the cumulative information available to them that "might well elude an untrained person." <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#418" aria-description="Citation for case: United States v. Cortez"><i>Id.,</i> at 418</a></span>. See also <i>Ornelas</i>  v. <i>United States,</i> <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#699" aria-description="Citation for case: Ornelas v. United States">517 U. S. 690, 699</a></span> (1996) (reviewing court must give "due weight" to factual inferences drawn by resident <span class="star-pagination">*274</span> judges and local law enforcement officers). Although an officer's reliance on a mere "`hunch' " is insufficient to justify a stop, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 27</a></span>, the likelihood of criminal activity need not rise to the level required for probable cause, and it falls considerably short of satisfying a preponderance of the evidence standard, <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#7" aria-description="Citation for case: United States v. Sokolow"><i>Sokolow, supra,</i> at 7</a></span>.</p>
<p>Our cases have recognized that the concept of reasonable suspicion is somewhat abstract. <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#696" aria-description="Citation for case: Ornelas v. United States"><i>Ornelas, supra,</i> at 696</a></span> (principle of reasonable suspicion is not a "`finely-tuned standar[d]' "); <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez"><i>Cortez, supra,</i> at 417</a></span> (the cause "sufficient to authorize police to stop a person" is an "elusive concept"). But we have deliberately avoided reducing it to "`a neat set of legal rules,' " <i><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/" aria-description="Citation for case: Ornelas v. United States">Ornelas, supra,</a></span></i> at 695-696 (quoting <i>Illinois</i>  v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#232" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 232</a></span> (1983)). In <i><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">Sokolow</a></span>,</i> for example, we rejected a holding by the Court of Appeals that distinguished between evidence of ongoing criminal behavior and probabilistic evidence because it "create[d] unnecessary difficulty in dealing with one of the relatively simple concepts embodied in the Fourth Amendment." <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#7" aria-description="Citation for case: United States v. Sokolow">490 U. S., at 7-8</a></span>.</p>
<p>We think that the approach taken by the Court of Appeals here departs sharply from the teachings of these cases. The court's evaluation and rejection of seven of the listed factors in isolation from each other does not take into account the "totality of the circumstances," as our cases have understood that phrase. The court appeared to believe that each observation by Stoddard that was by itself readily susceptible to an innocent explanation was entitled to "no weight." See <span class="citation" data-id="771188"><a href="/opinion/771188/united-states-v-ralph-arvizu/#1249" aria-description="Citation for case: United States v. Ralph Arvizu">232 F. 3d, at 1249-1251</a></span>. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> however, precludes this sort of divide-and-conquer analysis. The officer in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> observed the petitioner and his companions repeatedly walk back and forth, look into a store window, and confer with one another. Although each of the series of acts was "perhaps innocent in itself," we held that, taken together, they "warranted further investigation." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 22</a></span>. See also <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#9" aria-description="Citation for case: United States v. Sokolow"><i>Sokolow, supra,</i> at 9</a></span> (holding that factors which by themselves <span class="star-pagination">*275</span> were "quite consistent with innocent travel" collectively amounted to reasonable suspicion).</p>
<p>The Court of Appeals' view that it was necessary to "clearly delimit" an officer's consideration of certain factors to reduce "troubling . . . uncertainty," <span class="citation" data-id="771188"><a href="/opinion/771188/united-states-v-ralph-arvizu/#1248" aria-description="Citation for case: United States v. Ralph Arvizu">232 F. 3d, at 1248</a></span>, also runs counter to our cases and underestimates the usefulness of the reasonable-suspicion standard in guiding officers in the field. In <i>Ornelas</i> v. <i>United States</i><i>,</i> we held that the standard for appellate review of reasonablesuspicion determinations should be <i>de novo,</i> rather than for "abuse of discretion." <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#691" aria-description="Citation for case: Ornelas v. United States">517 U. S., at 691</a></span>. There, we reasoned that <i>de novo</i> review would prevent the affirmance of opposite decisions on identical facts from different judicial districts in the same circuit, which would have been possible under the latter standard, and would allow appellate courts to clarify the legal principles. <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#697" aria-description="Citation for case: Ornelas v. United States"><i>Id.,</i> at 697</a></span>. Other benefits of the approach, we said, were its tendency to unify precedent and greater capacity to provide law enforcement officers with the tools to reach correct determinations beforehand: Even if in many instances the factual "mosaic" analyzed for a reasonable-suspicion determination would preclude one case from squarely controlling another, "two decisions when viewed together may usefully add to the body of law on the subject." <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#697" aria-description="Citation for case: Ornelas v. United States"><i>Id.,</i> at 697-698</a></span>.</p>
<p>But the Court of Appeals' approach would go considerably beyond the reasoning of <i><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/" aria-description="Citation for case: Ornelas v. United States">Ornelas</a></span></i> and seriously undercut the "totality of the circumstances" principle which governs the existence <i>vel non</i> of "reasonable suspicion." Take, for example, the court's positions that respondent's deceleration could not be considered because "slowing down after spotting a law enforcement vehicle is an entirely normal response that is in no way indicative of criminal activity" and that his failure to acknowledge Stoddard's presence provided no support because there were "no `special circumstances' rendering `innocent avoidance . . . improbable.' " <span class="citation" data-id="771188"><a href="/opinion/771188/united-states-v-ralph-arvizu/#1248" aria-description="Citation for case: United States v. Ralph Arvizu">232 F. 3d, at 1248-1249</a></span>. We think it quite reasonable that a driver's <span class="star-pagination">*276</span> slowing down, stiffening of posture, and failure to acknowledge a sighted law enforcement officer might well be unremarkable in one instance (such as a busy San Francisco highway) while quite unusual in another (such as a remote portion of rural southeastern Arizona). Stoddard was entitled to make an assessment of the situation in light of his specialized training and familiarity with the customs of the area's inhabitants. See <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#699" aria-description="Citation for case: Ornelas v. United States"><i>Ornelas, supra,</i> at 699</a></span>. To the extent that a totality of the circumstances approach may render appellate review less circumscribed by precedent than otherwise, it is the nature of the totality rule.</p>
<p>In another instance, the Court of Appeals chose to dismiss entirely the children's waving on grounds that odd conduct by children was all too common to be probative in a particular case. See <span class="citation" data-id="771188"><a href="/opinion/771188/united-states-v-ralph-arvizu/#1249" aria-description="Citation for case: United States v. Ralph Arvizu">232 F. 3d, at 1249</a></span> ("If every odd act engaged in by one's children . . . could contribute to a finding of reasonable suspicion, the vast majority of American parents might be stopped regularly within a block of their homes"). Yet this case did not involve simply any odd act by children. At the suppression hearing, Stoddard testified about the children's waving several times, and the record suggests that he physically demonstrated it as well.<sup>[2]</sup> The District Court Judge, who saw and heard Stoddard, then characterized the waving as "methodical," "mechanical," "abnormal," and "certainly . . . a fact that is odd and would lead a reasonable officer to wonder why they are doing this." App. to Pet. for Cert. 25a. Though the issue of this case does not turn on the children's idiosyncratic actions, the Court of Appeals should not have casually rejected this factor in light of the District Court's superior access to the evidence and the well-recognized inability of reviewing courts to reconstruct what happened in the courtroom.</p>
<p><span class="star-pagination">*277</span> Having considered the totality of the circumstances and given due weight to the factual inferences drawn by the law enforcement officer and District Court Judge, we hold that Stoddard had reasonable suspicion to believe that respondent was engaged in illegal activity. It was reasonable for Stoddard to infer from his observations, his registration check, and his experience as a border patrol agent that respondent had set out from Douglas along a little-traveled route used by smugglers to avoid the 191 checkpoint. Stoddard's knowledge further supported a commonsense inference that respondent intended to pass through the area at a time when officers would be leaving their backroads patrols to change shifts. The likelihood that respondent and his family were on a picnic outing was diminished by the fact that the minivan had turned away from the known recreational areas accessible to the east on Rucker Canyon Road. Corroborating this inference was the fact that recreational areas farther to the north would have been easier to reach by taking 191, as opposed to the 40-to-50-mile trip on unpaved and primitive roads. The children's elevated knees suggested the existence of concealed cargo in the passenger compartment. Finally, for the reasons we have given, Stoddard's assessment of respondent's reactions upon seeing him and the children's mechanical-like waving, which continued for a full four to five minutes, were entitled to some weight.</p>
<p>Respondent argues that we must rule in his favor because the facts suggested a family in a minivan on a holiday outing. A determination that reasonable suspicion exists, however, need not rule out the possibility of innocent conduct. See <i>Illinois</i> v. <i>Wardlow,</i> <span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/#125" aria-description="Citation for case: Illinois v. Wardlow">528 U. S. 119, 125</a></span> (2000) (that flight from police is not necessarily indicative of ongoing criminal activity does not establish Fourth Amendment violation). Undoubtedly, each of these factors alone is susceptible of innocent explanation, and some factors are more probative than others. Taken together, we believe they sufficed to form a particularized and objective basis for Stoddard's <span class="star-pagination">*278</span> stopping the vehicle, making the stop reasonable within the meaning of the Fourth Amendment.</p>
<p>The judgment of the Court of Appeals is therefore reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i> </p>
<p>[Appendix to opinion of the Court follows this page.]</p>
<p>Justice Scalia, concurring.</p>
<p>I join the opinion of the Court, because I believe it accords with our opinion in <i>Ornelas</i> v. <i>United States,</i> <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#699" aria-description="Citation for case: Ornelas v. United States">517 U. S. 690, 699</a></span> (1996), requiring <i>de novo</i> review which nonetheless gives "due weight to inferences drawn from [the] facts by resident judges . . . ." As I said in my dissent in <i><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/" aria-description="Citation for case: Ornelas v. United States">Ornelas</a></span>,</i> however, I do not see how deferring to the District Court's factual inferences (as opposed to its findings of fact) is compatible with <i>de novo</i> review. <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#705" aria-description="Citation for case: Ornelas v. United States"><i>Id.,</i> at 705</a></span>.</p>
<p>The Court today says that "due weight" should have been given to the District Court's determinations that the children's waving was "`methodical,' `mechanical,' `abnormal,' and `certainly . . . a fact that is odd and would lead a reasonable officer to wonder why they are doing this.' " <i>Ante,</i>  at 276. "Methodical," "mechanical," and perhaps even "abnormal" and "odd," are findings of fact that deserve respect. But the inference that this "would lead a reasonable officer to wonder why they are doing this," amounts to the conclusion that their action was suspicious, which I would have thought (if <i>de novo</i> review is the standard) is the prerogative of the Court of Appeals. So we have here a peculiar sort of <i>de novo</i> review.</p>
<p>I may add that, even holding the Ninth Circuit to no more than the traditional methodology of <i>de novo</i> review, its judgment here would have to be reversed.</p>
<p></p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging affirmance were filed for the DKT Liberty Project by <i>Julia M. Carpenter;</i> and for the National Association of Criminal Defense Lawyers et al. by <i>Lawrence S. Lustberg</i> and <i>Risa E. Kaufman.</i> </p>
<p>[1]  Coronado National Forest consists of 12 widely scattered sections of land covering 1,780,000 acres in southeastern Arizona and southwestern New Mexico. The section of the forest near Douglas includes the Chiricahua, Dragoon, and Peloncillo Mountain Ranges.</p>
<p>[2]  At one point during the hearing, Stoddard testified that "[the children's waving] wasn't in a normal pattern. It looked like they were instructed to do so. They kind of stuck their hands up and began waving to me like this." App. 35.</p>

</div>
```

---

## GROUP: content/cases/United States v. Ash.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Ash"
type: case
citation: "413 U.S. 300 (1973)"
parallel_cite: "93 S. Ct. 2568; 37 L. Ed. 2d 619"
neutral_cite: 1973 U.S. LEXIS 45
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1973
date_decided: 1973-06-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1973-06-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Ash
  varies_by_point: false
  scope_note: "Good law; no Sixth Amendment right to counsel at a photographic display."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108846/united-states-v-ash/"
  cluster_id: 108846
  opinion_id: 108846
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Progeny / Refinement"
related: ["[[Kirby v. Illinois]]", "[[Gilbert v. California]]", "[[Manson v. Brathwaite]]", "[[Neil v. Biggers]]", "[[Stovall v. Denno]]"]
aliases: ["United States v. Charles J. Ash, Jr."]
tags: ["case", "sixth-amendment", "eyewitness-identification", "right-to-counsel"]
holding: "The Sixth Amendment does not grant a right to counsel at a post-indictment photographic display (no trial-like confrontation, since the…"
lake:
  record_id: United States v. Ash
  status: verified
  projected_at: 2026-07-06
---

# United States v. Ash

*413 U.S. 300 (1973)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After Ash was indicted for a bank robbery, the prosecutor, preparing for trial, showed witnesses a set of color photographs — including Ash's — to confirm their identifications. Defense counsel was not present at this post-indictment photographic display. Ash argued the procedure was a critical stage at which he was entitled to counsel under the Sixth Amendment.

## Issue
Whether a defendant has a Sixth Amendment right to have counsel present when the government conducts a post-indictment photographic display of the accused to witnesses for identification purposes.

## Rule
No. The Court held that "the Sixth Amendment does not grant the right to counsel at photographic displays conducted by the Government for the purpose of allowing a witness to attempt an identification of the offender." — 413 U.S. at 321. ^pin-321

A photographic display is not a trial-like confrontation: the accused is not present and need not confront witnesses or the prosecution, so the presence of counsel is not required to preserve a fair trial.

## Application
Because Ash was not present when the prosecutor showed the photo array to witnesses, the display was not a trial-like confrontation triggering the right to counsel. The risks of suggestive photographic identification could be exposed through ordinary trial tools — cross-examination of the witnesses and the officers — rather than by counsel's attendance at the display. The absence of defense counsel from the photo identification therefore did not violate the Sixth Amendment.

## Conclusion
There was no Sixth Amendment right to counsel at the post-indictment photographic display; the Court of Appeals' contrary judgment was reversed. The right to counsel attaches to trial-like confrontations at which the accused is present, not to photo arrays shown to witnesses.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Ash* distinguishes the live-lineup right to counsel of [[Gilbert v. California]] and is consistent with [[Kirby v. Illinois]] (right attaches at the initiation of adversary proceedings); suggestive photo identifications are policed instead through the due-process reliability test of [[Neil v. Biggers]] and [[Manson v. Brathwaite]].

## Appears on
- [[Eyewitness Identification]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Ash*, 413 U.S. 300 (1973) — https://www.courtlistener.com/opinion/108846/united-states-v-ash/ — pinpoint: 321.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e8e15366fe44fc3a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "413 U.S. 300 (1973)", "court": "U.S. Supreme Court", "neutral_cite": "1973 U.S. LEXIS 45", "official_citation_present": true, "parallel_cite": "93 S. Ct. 2568; 37 L. Ed. 2d 619", "title": "United States v. Ash", "year": "1973"}}
{"assertion_id": "caaf0fc86c40118f", "dimension": "support", "kind": "home_role", "locator": {"home": "Eyewitness Identification"}, "payload": {"home": "Eyewitness Identification", "role": "Key — Progeny / Refinement", "title": "United States v. Ash"}}
{"assertion_id": "f1c16b23db59c340", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Sixth Amendment does not grant a right to counsel at a post-indictment photographic display (no trial-like confrontation, since the…", "title": "United States v. Ash"}}
{"assertion_id": "45efab7f9d6b6db4", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1973-06-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Ash", "field_i_validity": "good_law", "scope_note": "Good law; no Sixth Amendment right to counsel at a photographic display.", "title": "United States v. Ash", "varies_by_point": "false"}}
{"assertion_id": "e3b11099a3f02d52", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Ash"}}
```

### lake record — United States v. Ash

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Ash",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Ash",
    "case_name_short": "Ash",
    "case_name_full": "United States v. Ash",
    "input_case_name": "United States v. Ash",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1973-06-21",
    "year": 1973,
    "docket": null,
    "cluster_id": 108846,
    "lead_opinion_id": 108846,
    "sibling_ids": [
      108846,
      9425398,
      9425399,
      9425400
    ],
    "absolute_url": "/opinion/108846/united-states-v-ash/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "413 U.S. 300",
      "volume": "413",
      "reporter": "U.S.",
      "page": "300",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "93 S. Ct. 2568",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2568",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 L. Ed. 2d 619",
        "volume": "37",
        "reporter": "L. Ed. 2d",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1973 U.S. LEXIS 45",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "45",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "413 U.S. 300",
        "volume": "413",
        "reporter": "U.S.",
        "page": "300",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 S. Ct. 2568",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2568",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 L. Ed. 2d 619",
        "volume": "37",
        "reporter": "L. Ed. 2d",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. LEXIS 45",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "45",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "413 U.S. 300",
    "official_selection": {
      "court_class": "scotus",
      "selected": "413 U.S. 300",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-321",
      "page": null,
      "quote": "--- # United States v. Ash *413 U.S. 300 (1973)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After Ash was indicted for a bank robbery, the prosecutor, preparing for trial, showed witnesses a set of color photographs \u2014 including Ash's \u2014 to confirm their identifications. Defense counsel was not present at this post-indictment photographic display. Ash argued the procedure was a critical stage at which he was entitled to counsel under the Sixth Amendment. ## Issue Whether a defendant has a Sixth Amendment right to have counsel present when the government conducts a post-indictment photographic display of the accused to witnesses for identification purposes. ## Rule No. The Court held that",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1973-06-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Ash",
    "varies_by_point": false,
    "scope_note": "Good law; no Sixth Amendment right to counsel at a photographic display.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Dew",
          "cluster_id": 9406638,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Craigen",
          "cluster_id": 10160931,
          "cite": [
            "370 Or. 696",
            "524 P.3d 85"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Turner v. United States",
          "cluster_id": 4480399,
          "cite": [
            "885 F.3d 949"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ramirez v. United States",
          "cluster_id": 8719635,
          "cite": [
            "898 F. Supp. 2d 659",
            "2012 U.S. Dist. LEXIS 107824",
            "2012 WL 3115161"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Patrick Henry Murphy v. State",
          "cluster_id": 3127894,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Joseph Van Patten v. Jodine Deppisch",
          "cluster_id": 792984,
          "cite": [
            "434 F.3d 1038",
            "2006 U.S. App. LEXIS 1658",
            "2006 WL 162992"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "LaPointe v. State",
          "cluster_id": 1380200,
          "cite": [
            "166 S.W.3d 287",
            "2005 WL 995371"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Watson v. State",
          "cluster_id": 2333044,
          "cite": [
            "95 S.W.3d 342",
            "2002 WL 1722064"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Franks v. State",
          "cluster_id": 1495257,
          "cite": [
            "90 S.W.3d 771",
            "2002 WL 1592443"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Darnell Hayes",
          "cluster_id": 771010,
          "cite": [
            "231 F.3d 663",
            "2000 Cal. Daily Op. Serv. 8991",
            "2000 Daily Journal DAR 11947",
            "2000 U.S. App. LEXIS 27872",
            "2000 WL 1672631"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Oliver v. State",
          "cluster_id": 5269601,
          "cite": [
            "995 S.W.2d 878",
            "1999 Tex. App. LEXIS 4604",
            "1999 WL 417387"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cronic",
          "cluster_id": 111169,
          "cite": [
            "80 L. Ed. 2d 657",
            "104 S. Ct. 2039",
            "466 U.S. 648",
            "1984 U.S. LEXIS 78",
            "52 U.S.L.W. 4560"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kimmelman v. Morrison",
          "cluster_id": 111724,
          "cite": [
            "91 L. Ed. 2d 305",
            "106 S. Ct. 2574",
            "477 U.S. 365",
            "1986 U.S. LEXIS 63",
            "54 U.S.L.W. 4789"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Evitts v. Lucey",
          "cluster_id": 111302,
          "cite": [
            "83 L. Ed. 2d 821",
            "105 S. Ct. 830",
            "469 U.S. 387",
            "1985 U.S. LEXIS 42"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
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
        "journal_ref": "United States v. Ash:lane2_top_cited"
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
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wheat v. United States",
          "cluster_id": 112074,
          "cite": [
            "100 L. Ed. 2d 140",
            "108 S. Ct. 1692",
            "486 U.S. 153",
            "1988 U.S. LEXIS 2306"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gonzalez-Lopez",
          "cluster_id": 145633,
          "cite": [
            "165 L. Ed. 2d 409",
            "126 S. Ct. 2557",
            "548 U.S. 140",
            "2006 U.S. LEXIS 5165",
            "19 Fla. L. Weekly Fed. S 368",
            "33 A.L.R. Fed. 2d 661",
            "74 U.S.L.W. 4453"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
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
        "journal_ref": "United States v. Ash:lane2_top_cited"
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
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Henry",
          "cluster_id": 110300,
          "cite": [
            "65 L. Ed. 2d 115",
            "100 S. Ct. 2183",
            "447 U.S. 264",
            "1980 U.S. LEXIS 111"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patterson v. Illinois",
          "cluster_id": 112127,
          "cite": [
            "101 L. Ed. 2d 261",
            "108 S. Ct. 2389",
            "487 U.S. 285",
            "1988 U.S. LEXIS 2876",
            "56 U.S.L.W. 4733"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Harvey",
          "cluster_id": 112385,
          "cite": [
            "108 L. Ed. 2d 293",
            "110 S. Ct. 1176",
            "494 U.S. 344",
            "1990 U.S. LEXIS 1229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
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
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Perry v. Leeke",
          "cluster_id": 112168,
          "cite": [
            "102 L. Ed. 2d 624",
            "109 S. Ct. 594",
            "488 U.S. 272",
            "1989 U.S. LEXIS 306",
            "57 U.S.L.W. 4075"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Willie Decoster, Jr.",
          "cluster_id": 314954,
          "cite": [
            "487 F.2d 1197",
            "159 U.S. App. D.C. 326"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robinson v. State",
          "cluster_id": 1448541,
          "cite": [
            "16 S.W.3d 808",
            "2000 Tex. Crim. App. LEXIS 43",
            "2000 WL 369127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rothgery v. Gillespie County",
          "cluster_id": 145785,
          "cite": [
            "171 L. Ed. 2d 366",
            "128 S. Ct. 2578",
            "554 U.S. 191",
            "2008 U.S. LEXIS 5057",
            "21 Fla. L. Weekly Fed. S 429",
            "76 U.S.L.W. 4520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael G. Thevis, Alton Bart Hood, Global Industries, Inc., Anna Jeanette Evans",
          "cluster_id": 397401,
          "cite": [
            "665 F.2d 616",
            "9 Fed. R. Serv. 1025",
            "1982 U.S. App. LEXIS 22706"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rigoberto Moya-Gomez Celestino Orlando Estevez Amado Raphael Leon Adalberto Herrera and Menelao Orlando Estevez",
          "cluster_id": 513458,
          "cite": [
            "860 F.2d 706"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Atwood",
          "cluster_id": 1182224,
          "cite": [
            "832 P.2d 593",
            "171 Ariz. 576"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williamson v. State",
          "cluster_id": 1111870,
          "cite": [
            "512 So. 2d 868"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mitcham",
          "cluster_id": 1203051,
          "cite": [
            "824 P.2d 1277",
            "1 Cal. 4th 1027",
            "5 Cal. Rptr. 2d 230",
            "92 Cal. Daily Op. Serv. 1532",
            "92 Daily Journal DAR 3034",
            "1992 Cal. LEXIS 1269"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Virgil",
          "cluster_id": 844274,
          "cite": [
            "253 P.3d 553",
            "51 Cal. 4th 1210",
            "126 Cal. Rptr. 3d 465",
            "2011 Cal. LEXIS 6538"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jackson",
          "cluster_id": 1838293,
          "cite": [
            "217 N.W.2d 22",
            "391 Mich. 323",
            "1974 Mich. LEXIS 139"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lotter",
          "cluster_id": 2116540,
          "cite": [
            "586 N.W.2d 591",
            "255 Neb. 456",
            "1998 Neb. LEXIS 224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108846 OR 9425398 OR 9425399 OR 9425400) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03OTUyMjU2MDAwMDAmcz02NTc2Nzg2JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108846+OR+9425398+OR+9425399+OR+9425400%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(108846 OR 9425398 OR 9425399 OR 9425400)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzImcz0yNTQzNDU5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108846+OR+9425398+OR+9425399+OR+9425400%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108846 OR 9425398 OR 9425399 OR 9425400)",
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
    "complete_query": "cites:(108846 OR 9425398 OR 9425399 OR 9425400)",
    "indexed_citing_opinions": 590,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108846,
        "count": 551,
        "count_source": "search"
      },
      {
        "opinion_id": 9425398,
        "count": 57,
        "count_source": "search"
      },
      {
        "opinion_id": 9425399,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425400,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 868,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-ash.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc2NjY3MDEmcz02NDUwODQ1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108846+OR+9425398+OR+9425399+OR+9425400%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108846,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 102436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 107354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 108567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 108718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 283186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 284440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 288980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 290782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 292225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 295836,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 299374,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 303766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 303865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1186833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1206841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1241302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1353187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1434555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1534458,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1710337,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1724451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1758004,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1838693,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1911421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 2061648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 2087977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 2133215,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 2172829,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 2178575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 2222943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 2616794,
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
    "date_created": "2026-07-05T22:17:08Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:17:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:17:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:24:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:17:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Ash (truncated)

```
<div>
<center><b><span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/" aria-description="Citation for case: United States v. Ash">413 U.S. 300</a></span> (1973)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
ASH.</h1></center>
<center>No. 71-1255.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued January 10, 1973.</center>
<center>Decided June 21, 1973.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE DISTRICT OF COLUMBIA CIRCUIT
<p><i>Edward R. Korman</i> argued the cause for the United States. With him on the brief were <i>Solicitor General Griswold, Assistant Attorney General Petersen,</i> and <i>Jerome M. Feit.</i></p>
<p><i>Sherman L. Cohn,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./408/942/">408 U. S. 942</a></span>, argued the cause and filed a brief for respondent.</p>
<p>MR. JUSTICE BLACKMUN delivered the opinion of the Court.</p>
<p>In this case the Court is called upon to decide whether <span class="star-pagination">*301</span> the Sixth Amendment<sup>[1]</sup> grants an accused the right to have counsel present whenever the Government conducts a post-indictment photographic display, containing a picture of the accused, for the purpose of allowing a witness to attempt an identification of the offender. The United States Court of Appeals for the District of Columbia Circuit, sitting en banc, held, by a 5-to-4 vote, that the accused possesses this right to counsel. 149 U. S. App. D. C. 1, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d 92</a></span> (1972). The court's holding is inconsistent with decisions of the courts of appeals of nine other circuits.<sup>[2]</sup> We granted certiorari <span class="star-pagination">*302</span> to resolve the conflict and to decide this important constitutional question. <span class="citation multiple-matches"><a href="/c/U.%20S./407/909/">407 U. S. 909</a></span> (1972). We reverse and remand.</p>
<p></p>
<h2>I</h2>
<p>On the morning of August 26, 1965, a man with a stocking mask entered a bank in Washington, D. C., and began waving a pistol. He ordered an employee to hang up the telephone and instructed all others present not to move. Seconds later a second man, also wearing a stocking mask, entered the bank, scooped up money from tellers' drawers into a bag, and left. The gunman followed, and both men escaped through an alley. The robbery lasted three or four minutes.</p>
<p>A Government informer, Clarence McFarland, told authorities that he had discussed the robbery with Charles J. Ash, Jr., the respondent here. Acting on this information, an FBI agent, in February 1966, showed five black-and-white mug shots of Negro males of generally the same age, height, and weight, one of which was of Ash, to four witnesses. All four made uncertain identifications of Ash's picture. At this time Ash was not in custody and had not been charged. On April 1, 1966, an indictment was returned charging Ash and a codefendant, John L. Bailey, in five counts related to this <span class="star-pagination">*303</span> bank robbery, in violation of D. C. Code Ann. § 22-2901 and <span class="citation no-link">18 U. S. C. § 2113</span> (a).</p>
<p>Trial was finally set for May 1968, almost three years after the crime. In preparing for trial, the prosecutor decided to use a photographic display to determine whether the witnesses he planned to call would be able to make in-court identifications. Shortly before the trial, an FBI agent and the prosecutor showed five color photographs to the four witnesses who previously had tentatively identified the black-and-white photograph of Ash. Three of the witnesses selected the picture of Ash, but one was unable to make any selection. None of the witnesses selected the picture of Bailey which was in the group. This post-indictment<sup>[3]</sup> identification provides the basis for respondent Ash's claim that he was denied the right to counsel at a "critical stage" of the prosecution.</p>
<p>No motion for severance was made, and Ash and Bailey were tried jointly. The trial judge held a hearing on the suggestive nature of the pretrial photographic displays.<sup>[4]</sup> The judge did not make a clear ruling on suggestive nature, but held that the Government had demonstrated by "clear and convincing" evidence that in-court identifications would be "based on observation of <span class="star-pagination">*304</span> the suspect other than the intervening observation." App. 63-64.</p>
<p>At trial, the three witnesses who had been inside the bank identified Ash as the gunman, but they were unwilling to state that they were certain of their identifications. None of these made an in-court identification of Bailey. The fourth witness, who had been in a car outside the bank and who had seen the fleeing robbers after they had removed their masks, made positive in-court identifications of both Ash and Bailey. Bailey's counsel then sought to impeach this in-court identification by calling the FBI agent who had shown the color photographs to the witnesses immediately before trial. Bailey's counsel demonstrated that the witness who had identified Bailey in court had failed to identify a color photograph of Bailey. During the course of the examination, Bailey's counsel also, before the jury, brought out the fact that this witness had selected another man as one of the robbers. At this point the prosecutor became concerned that the jury might believe that the witness had selected a third person when, in fact, the witness had selected a photograph of Ash. After a conference at the bench, the trial judge ruled that all five color photographs would be admitted into evidence. The Court of Appeals held that this constituted the introduction of a post-indictment identification at the prosecutor's request and over the objection of defense counsel.<sup>[5]</sup></p>
<p><span class="star-pagination">*305</span> McFarland testified as a Government witness. He said he had discussed plans for the robbery with Ash before the event and, later, had discussed the results of the robbery with Ash in the presence of Bailey. McFarland was shown to possess an extensive criminal record and a history as an informer.</p>
<p>The jury convicted Ash on all counts. It was unable to reach a verdict on the charges against Bailey, and his motion for acquittal was granted. Ash received concurrent sentences on the several counts, the two longest being 80 months to 12 years.</p>
<p>The five-member majority of the Court of Appeals held that Ash's right to counsel, guaranteed by the Sixth Amendment, was violated when his attorney was not given the opportunity to be present at the photographic displays conducted in May 1968 before the trial. The majority relied on this Court's lineup cases, <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), and <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967), and on <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span> (1967).</p>
<p>The majority did not reach the issue of suggestiveness; their opinion implies, however, that they would order a remand for additional findings by the District Court. 149 U. S. App. D. C., at 7, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/#98" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d, at 98</a></span>. The majority refrained from deciding whether the in-court identifications could have independent bases, <i><span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">id.,</a></span></i> at 14-15 and nn. 20, 21, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d, at 105</a></span>-106 and nn. 20, 21, but expressed doubt that the identifications at the trial had independent origins.</p>
<p>Dissenting opinions, joined by four judges, disagreed with the decision of the majority that the photographic identification was a "critical stage" requiring counsel, and criticized the majority's suggestion that the in-court identifications were tainted by defects in the photographic identifications. <i>Id.,</i> at 14-43, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/#106" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d, at 106-134</a></span>.</p>
<p></p>
<h2>
<span class="star-pagination">*306</span> II</h2>
<p>The Court of Appeals relied exclusively on that portion of the Sixth Amendment providing, "In all criminal prosecutions, the accused shall enjoy the right . . . to have the Assistance of Counsel for his defence." The right to counsel in Anglo-American law has a rich historical heritage, and this Court has regularly drawn on that history in construing the counsel guarantee of the Sixth Amendment. We re-examine that history in an effort to determine the relationship between the purposes of the Sixth Amendment guarantee and the risks of a photographic identification.</p>
<p>In <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#60" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45, 60-66</a></span> (1932), the Court discussed the English common-law rule that severely limited the right of a person accused of a felony to consult with counsel at trial. The Court examined colonial constitutions and statutes and noted that "in at least twelve of the thirteen colonies the rule of the English common law, in the respect now under consideration, had been definitely rejected and the right to counsel fully recognized in all criminal prosecutions, save that in one or two instances the right was limited to capital offenses or to the more serious crimes." <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#64" aria-description="Citation for case: Powell v. Alabama"><i>Id.,</i> at 64-65</a></span>. The Sixth Amendment counsel guarantee, thus, was derived from colonial statutes and constitutional provisions designed to reject the English common-law rule.</p>
<p>Apparently several concerns contributed to this rejection at the very time when countless other aspects of the common law were being imported. One consideration was the inherent irrationality of the English limitation. Since the rule was limited to felony proceedings, the result, absurd and illogical, was that an accused misdemeanant could rely fully on counsel, but <span class="star-pagination">*307</span> the accused felon, in theory at least,<sup>[6]</sup> could consult counsel only on legal questions that the accused proposed to the court. See <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#60" aria-description="Citation for case: Powell v. Alabama">287 U. S., at 60</a></span>. English writers were appropriately critical of this inconsistency. See, for example, 4 W. Blackstone, Commentaries *355.</p>
<p>A concern of more lasting importance was the recognition and awareness that an unaided layman had little skill in arguing the law or in coping with an intricate procedural system. The function of counsel as a guide through complex legal technicalities long has been recognized by this Court. Mr. Justice Sutherland's well-known observations in <i><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">Powell</a></span></i> bear repeating here:</p>
<blockquote>"Even the intelligent and educated layman has small and sometimes no skill in the science of law. If charged with crime, he is incapable, generally, of determining for himself whether the indictment is good or bad. He is unfamiliar with the rules of evidence. Left without the aid of counsel he may be put on trial without a proper charge, and convicted upon incompetent evidence, or evidence irrelevant to the issue or otherwise inadmissible. He lacks both the skill and knowledge adequately to prepare his defense, even though he have a perfect one. He requires the guiding hand of counsel at every step in the proceedings against him. Without it, though he be not guilty, he faces the danger of conviction because he does not know how to establish his innocence." <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#69" aria-description="Citation for case: Powell v. Alabama">287 U. S., at 69</a></span>.</blockquote>
<p>The Court frequently has interpreted the Sixth Amendment <span class="star-pagination">*308</span> to assure that the "guiding hand of counsel" is available to those in need of its assistance. See, for example, <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/#344" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335, 344-345</a></span> (1963), and <i>Argersinger</i> v. <i>Hamlin,</i> <span class="citation" data-id="9424926"><a href="/opinion/108567/argersinger-v-hamlin/#31" aria-description="Citation for case: Argersinger v. Hamlin">407 U. S. 25, 31</a></span> (1972).</p>
<p>Another factor contributing to the colonial recognition of the accused's right to counsel was the adoption of the institution of the public prosecutor from the Continental inquisitorial system. One commentator has explained the effect of this development:</p>
<blockquote>"[E]arly in the eighteenth century the American system of judicial administration adopted an institution which was (and to some extent still is) unknown in England: while rejecting the fundamental juristic concepts upon which continental Europe's inquisitorial system of criminal procedure is predicated, the colonies borrowed one of its institutions, the public prosecutor, and grafted it upon the body of English (accusatorial) procedure embodied in the common law. Presumably, this innovation was brought about by the lack of lawyers, particularly in the newly settled regions, and by the increasing distances between the colonial capitals on the eastern seaboard and the ever-receding western frontier. Its result was that, at a time when virtually all but treason trials in England were still in the nature of suits between private parties, the accused in the colonies faced a government official whose specific function it was to prosecute, and who was incomparably more familiar than the accused with the problems of procedure, the idiosyncrasies of juries, and, last but not least, the personnel of the court." F. Heller, The Sixth Amendment 20-21 (1951) (footnote omitted).</blockquote>
<p><span class="star-pagination">*309</span> Thus, an additional motivation for the American rule was a desire to minimize the imbalance in the adversary system that otherwise resulted with the creation of a professional prosecuting official. Mr. Justice Black, writing for the Court in <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#462" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 462-463</a></span> (1938), spoke of this equalizing effect of the Sixth Amendment's counsel guarantee:</p>
<blockquote>"It embodies a realistic recognition of the obvious truth that the average defendant does not have the professional legal skill to protect himself when brought before a tribunal with power to take his life or liberty, wherein the prosecution is presented by experienced and learned counsel."</blockquote>
<p>This historical background suggests that the core purpose of the counsel guarantee was to assure "Assistance" at trial, when the accused was confronted with both the intricacies of the law and the advocacy of the public prosecutor.<sup>[7]</sup> Later developments have led this Court <span class="star-pagination">*310</span> to recognize that "Assistance" would be less than meaningful if it were limited to the formal trial itself.</p>
<p>This extension of the right to counsel to events before trial has resulted from changing patterns of criminal procedure and investigation that have tended to generate pretrial events that might appropriately be considered to be parts of the trial itself. At these newly emerging and significant events, the accused was confronted, just as at trial, by the procedural system, or by his expert adversary, or by both. In <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> the Court explained the process of expanding the counsel guarantee to these confrontations:</p>
<blockquote>"When the Bill of Rights was adopted, there were no organized police forces as we know them today. The accused confronted the prosecutor and the witnesses against him, and the evidence was marshalled, largely at the trial itself. In contrast, today's law enforcement machinery involves critical confrontations of the accused by the prosecution at pretrial proceedings where the results might well settle the accused's fate and reduce the trial itself to a mere formality. In recognition of these realities of modern criminal prosecution, our cases have construed the Sixth Amendment guarantee to apply to `critical' <span class="star-pagination">*311</span> stages of the proceedings." 388 U. S., at 224 (footnote omitted).</blockquote>
<p>The Court consistently has applied a historical interpretation of the guarantee, and has expanded the constitutional right to counsel only when new contexts appear presenting the same dangers that gave birth initially to the right itself.</p>
<p>Recent cases demonstrate the historical method of this expansion. In <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span> (1961), and in <i>White</i> v. <i>Maryland,</i> <span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span> (1963), the accused was confronted with the procedural system and was required, with definite consequences, to enter a plea. In <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964), the accused was confronted by prosecuting authorities who obtained, by ruse and in the absence of defense counsel, incriminating statements. In <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970), the accused was confronted by his adversary at a "critical stage" preliminary hearing at which the uncounseled accused could not hope to obtain so much benefit as could his skilled adversary.</p>
<p>The analogy between the unrepresented accused at the pretrial confrontation and the unrepresented defendant at trial, implicit in the cases mentioned above, was explicitly drawn in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>:</i></p>
<blockquote>"The trial which might determine the accused's fate may well not be that in the courtroom but that at the pretrial confrontation, with the State aligned against the accused, the witness the sole jury, and the accused unprotected against the overreaching, intentional or unintentional, and with little or no effective appeal from the judgment there rendered by the witness`that's the man.'" 388 U. S., at 235-236.</blockquote>
<p><span class="star-pagination">*312</span> Throughout this expansion of the counsel guarantee to trial-like confrontations, the function of the lawyer has remained essentially the same as his function at trial. In all cases considered by the Court, counsel has continued to act as a spokesman for, or advisor to, the accused. The accused's right to the "Assistance of Counsel" has meant just that, namely, the right of the accused to have counsel acting as his assistant. In <i><span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">Hamilton</a></span></i> and <i><span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">White</a></span>,</i> for example, the Court envisioned the lawyer as advising the accused on available defenses in order to allow him to plead intelligently. <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/#54" aria-description="Citation for case: Hamilton v. Alabama">368 U. S., at 54-55</a></span>; <span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/#60" aria-description="Citation for case: White v. Maryland">373 U. S., at 60</a></span>. In <i><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span></i> counsel could have advised his client on the benefits of the Fifth Amendment and could have sheltered him from the overreaching of the prosecution. <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#205" aria-description="Citation for case: Massiah v. United States">377 U. S., at 205</a></span>. Cf. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#466" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 466</a></span> (1966). In <i><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">Coleman</a></span></i> the skill of the lawyer in examining witnesses, probing for evidence, and making legal arguments was relied upon by the Court to demonstrate that, in the light of the purpose of the preliminary hearing under Alabama law, the accused required "Assistance" at that hearing. <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#9" aria-description="Citation for case: Coleman v. Alabama">399 U. S., at 9</a></span>.</p>
<p>The function of counsel in rendering "Assistance" continued at the lineup under consideration in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and its companion cases. Although the accused was not confronted there with legal questions, the lineup offered opportunities for prosecuting authorities to take advantage of the accused. Counsel was seen by the Court as being more sensitive to, and aware of, suggestive influences than the accused himself, and as better able to reconstruct the events at trial. Counsel present at lineup would be able to remove disabilities of the accused in precisely the same fashion that counsel compensated for the disabilities of the layman at trial. Thus, the Court mentioned that the accused's memory might be dimmed by "emotional tension," that the accused's credibility at <span class="star-pagination">*313</span> trial would be diminished by his status as defendant, and that the accused might be unable to present his version effectively without giving up his privilege against compulsory self-incrimination. <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#230" aria-description="Citation for case: United States v. Wade">388 U. S., at 230-231</a></span>. It was in order to compensate for these deficiencies that the Court found the need for the assistance of counsel.</p>
<p>This review of the history and expansion of the Sixth Amendment counsel guarantee demonstrates that the test utilized by the Court has called for examination of the event in order to determine whether the accused required aid in coping with legal problems or assistance in meeting his adversary. Against the background of this traditional test, we now consider the opinion of the Court of Appeals.</p>
<p></p>
<h2>III</h2>
<p>Although the Court of Appeals' majority recognized the argument that "a major purpose behind the right to counsel is to protect the defendant from errors that he himself might make if he appeared in court alone," the court concluded that "other forms of prejudice," mentioned and recognized in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> could also give rise to a right to counsel. 149 U. S. App. D. C., at 10, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/#101" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d, at 101</a></span>. These forms of prejudice were felt by the court to flow from the possibilities for mistaken identification inherent in the photographic display.<sup>[8]</sup></p>
<p><span class="star-pagination">*314</span> We conclude that the dangers of mistaken identification, mentioned in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> were removed from context by the Court of Appeals and were incorrectly utilized as a sufficient basis for requiring counsel. Although <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> did discuss possibilities for suggestion and the difficulty for reconstructing suggestivity, this discussion occurred only after the Court had concluded that the lineup constituted a trial-like confrontation, requiring the "Assistance of Counsel" to preserve the adversary process by compensating for advantages of the prosecuting authorities.</p>
<p>The above discussion of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> has shown that the traditional Sixth Amendment test easily allowed extension of counsel to a lineup. The similarity to trial was apparent, and counsel was needed to render "Assistance" in counterbalancing any "overreaching" by the prosecution.</p>
<p>After the Court in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> held that a lineup constituted a trial-like confrontation requiring counsel, a more difficult issue remained in the case for consideration. The same changes in law enforcement that led to lineups and pretrial hearings also generated other events at which the accused was confronted by the prosecution. The Government had argued in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> that if counsel was required at a lineup, the same forceful considerations would mandate counsel at other preparatory steps in the "gathering of the prosecution's evidence," such as, for <span class="star-pagination">*315</span> particular example, the taking of fingerprints or blood samples. 388 U. S., at 227.</p>
<p>The Court concluded that there were differences. Rather than distinguishing these situations from the lineup in terms of the need for counsel to assure an equal confrontation at the time, the Court recognized that there were times when the subsequent trial would cure a one-sided confrontation between prosecuting authorities and the uncounseled defendant. In other words, such stages were not "critical." Referring to fingerprints, hair, clothing, and other blood samples, the Court explained:</p>
<blockquote>"Knowledge of the techniques of science and technology is sufficiently available, and the variables in techniques few enough, that the accused has the opportunity for a meaningful confrontation of the Government's case at trial through the ordinary processes of cross-examination of the Government's expert witnesses and the presentation of the evidence of his own experts." 388 U. S., at 227-228.</blockquote>
<p>The structure of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> viewed in light of the careful limitation of the Court's language to "confrontations,"<sup>[9]</sup><span class="star-pagination">*316</span> makes it clear that lack of scientific precision and inability to reconstruct an event are not the tests for requiring counsel in the first instance. These are, instead, the tests to determine whether confrontation with counsel at trial can serve as a substitute for counsel at the pretrial confrontation. If accurate reconstruction is possible, the risks inherent in any confrontation still remain, but the opportunity to cure defects at trial causes the confrontation to cease to be "critical." The opinion of the Court even indicated that changes in procedure might cause a lineup to cease to be a "critical" confrontation:</p>
<blockquote>"Legislative or other regulations, such as those of local police departments, which eliminate the risks of abuse and unintentional suggestion at lineup proceedings and the impediments to meaningful confrontation at trial may also remove the basis for regarding the stage as `critical.'" 388 U. S., at 239 (footnote omitted).</blockquote>
<p>See, however, <i>id.,</i> at 262 n. (opinion of Fortas, J.).</p>
<p>The Court of Appeals considered its analysis complete after it decided that a photographic display lacks scientific precision and ease of accurate reconstruction at trial. That analysis, under <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> however, merely carries one to the point where one must establish that the trial itself can provide no substitute for counsel if a pretrial confrontation is conducted in the absence of counsel. Judge Friendly, writing for the Second Circuit in <i>United States</i> v. <i>Bennett,</i> <span class="citation" data-id="284440"><a href="/opinion/284440/united-states-v-charles-t-bennett-wilbert-haywood-elmer-jessup-henry/" aria-description="Citation for case: United States v. Charles T. Bennett, Wilbert Haywood,...">409 F. 2d 888</a></span> (1969), recognized that the "criticality" test of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> if applied outside the confrontation context, would result in drastic expansion of the right to counsel:</p>
<blockquote>"None of the classical analyses of the assistance to be given by counsel, Justice Sutherland's in Powell v. Alabama . . . and Justice Black's in Johnson v. <span class="star-pagination">*317</span> Zerbst . . . and Gideon v. Wainwright . . . suggests that counsel must be present when the prosecution is interrogating witnesses in the defendant's absence even when, as here, the defendant is under arrest; counsel is rather to be provided to prevent the defendant himself from falling into traps devised by a lawyer on the other side and to see to it that all available defenses are proffered. Many other aspects of the prosecution's interviews with a victim or a witness to a crime afford just as much opportunity for undue suggestion as the display of photographs; so, too, do the defense's interviews, notably with alibi witnesses." <i>Id.,</i> at 899-900.</blockquote>
<p>We now undertake the threshhold analysis that must be addressed.</p>
<p></p>
<h2>IV</h2>
<p>A substantial departure from the historical test would be necessary if the Sixth Amendment were interpreted to give Ash a right to counsel at the photographic identification in this case. Since the accused himself is not present at the time of the photographic display, and asserts no right to be present, Brief for Respondent 40, no possibility arises that the accused might be misled by his lack of familiarity with the law or overpowered by his professional adversary. Similarly, the counsel guarantee would not be used to produce equality in a trial-like adversary confrontation. Rather, the guarantee was used by the Court of Appeals to produce confrontation at an event that previously was not analogous to an adversary trial.</p>
<p>Even if we were willing to view the counsel guarantee in broad terms as a generalized protection of the adversary process, we would be unwilling to go so far as to extend the right to a portion of the prosecutor's trial-preparation interviews with witnesses. Although photography <span class="star-pagination">*318</span> is relatively new, the interviewing of witnesses before trial is a procedure that predates the Sixth Amendment. In England in the 16th and 17th centuries counsel regularly interviewed witnesses before trial. 9 W. Holdsworth, History of English Law 226-228 (1926). The traditional counterbalance in the American adversary system for these interviews arises from the equal ability of defense counsel to seek and interview witnesses himself.</p>
<p>That adversary mechanism remains as effective for a photographic display as for other parts of pretrial interviews.<sup>[10]</sup> No greater limitations are placed on defense counsel in constructing displays, seeking witnesses, and conducting photographic identifications than those applicable to the prosecution.<sup>[11]</sup> Selection of the picture of a person other than the accused, or the inability of a witness to make any selection, will be useful to the defense in precisely the same manner that the selection of <span class="star-pagination">*319</span> a picture of the defendant would be useful to the prosecution.<sup>[12]</sup> In this very case, for example, the initial tender of the photographic display was by Bailey's counsel, who sought to demonstrate that the witness had failed to make a photographic identification. Although we do not suggest that equality of access to photographs removes all potential for abuse,<sup>[13]</sup> it does remove any inequality in the adversary process itself and thereby fully satisfies the historical spirit of the Sixth Amendment's counsel guarantee.</p>
<p>The argument has been advanced that requiring counsel might compel the police to observe more scientific procedures or might encourage them to utilize corporeal rather than photographic displays.<sup>[14]</sup> This Court has <span class="star-pagination">*320</span> recognized that improved procedures can minimize the dangers of suggestion. <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span>, 386 n. 6 (1968). Commentators have also proposed more accurate techniques.<sup>[15]</sup></p>
<p>Pretrial photographic identifications, however, are hardly unique in offering possibilities for the actions of the prosecutor unfairly to prejudice the accused. Evidence favorable to the accused may be withheld; testimony of witnesses may be manipulated; the results of laboratory tests may be contrived. In many ways the prosecutor, by accident or by design, may improperly subvert the trial. The primary safeguard against abuses of this kind is the ethical responsibility of the prosecutor,<sup>[16]</sup> who, as so often has been said, may "strike hard blows" but not "foul ones." <i>Berger</i> v. <i>United States,</i> <span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/#88" aria-description="Citation for case: Berger v. United States">295 U. S. 78, 88</a></span> (1935); <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83, 87-88</a></span> (1963). If that safeguard fails, review remains available under due process standards. See <i>Giglio</i> v. <i>United States,</i> <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">405 U. S. 150</a></span> (1972); <i>Mooney</i> v. <i>Holohan,</i> <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#112" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103, 112</a></span> (1935); <i>Miller</i> v. <i>Pate,</i> <span class="citation" data-id="107354"><a href="/opinion/107354/miller-v-pate/" aria-description="Citation for case: Miller v. Pate">386 U. S. 1</a></span> (1967); <i>Chambers</i> v. <i>Mississippi,</i> <span class="citation" data-id="9425169"><a href="/opinion/108718/chambers-v-mississippi/" aria-description="Citation for case: Chambers v. Mississippi">410 U. S. 284</a></span> (1973). These same safeguards apply to misuse of photographs. See <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U. S., at 384</a></span>.</p>
<p><span class="star-pagination">*321</span> We are not persuaded that the risks inherent in the use of photographic displays are so pernicious that an extraordinary system of safeguards is required.</p>
<p>We hold, then, that the Sixth Amendment does not grant the right to counsel at photographic displays conducted by the Government for the purpose of allowing a witness to attempt an identification of the offender. This holding requires reversal of the judgment of the Court of Appeals. Although respondent Ash has urged us to examine this photographic display under the due process standard enunciated in <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U. S., at 384</a></span>, the Court of Appeals, expressing the view that additional findings would be necessary, refused to decide the issue. 149 U. S. App. D. C., at 7, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/#98" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d, at 98</a></span>. We decline to consider this question on this record in the first instance. It remains open, of course, on the Court of Appeals' remand to the District Court.</p>
<p><i>Reversed and remanded.</i></p>
<p>MR. JUSTICE STEWART, concurring in the judgment.</p>
<p>The issue in the present case is whether, under the Sixth Amendment, a person who has been indicted is entitled to have a lawyer present when prosecution witnesses are shown the person's photograph and asked if they can identify him.</p>
<p>The Sixth Amendment guarantees that "[i]n all criminal prosecutions, the accused shall enjoy the right . . . to have the Assistance of Counsel for his defence." This Court's decisions make it clear that a defendant is entitled to the assistance of counsel not only at the trial itself, but at all "critical stages" of his "prosecution." See <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span>; <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span>; <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span>; <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span>. The requirement <span class="star-pagination">*322</span> that there be a "prosecution," means that this constitutional "right to counsel attaches only at or after the time that adversary judicial proceedings have been initiated against [an accused] . . . ." "It is this point . . . that marks the commencement of the `criminal prosecutions' to which alone the explicit guarantees of the Sixth Amendment are applicable." <i>Kirby</i> v. <i>Illinois,</i> <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#688" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682, 688, 690</a></span> (plurality opinion). Since the photographic identification in the present case occurred after the accused had been indicted, and thus clearly after adversary judicial proceedings had been initiated, the only question is whether that procedure was such a "critical stage" that the Constitution required the presence of counsel.</p>
<p>In <i>United States</i> v. <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade, supra</a></span></i><i>,</i> the Court determined that a pretrial proceeding is a "critical stage" if "the presence of . . . counsel is necessary to preserve the defendant's. . . right meaningfully to cross-examine the witnesses against him and to have effective assistance of counsel at the trial itself." 388 U. S., at 227. Pretrial proceedings are "critical," then, if the presence of counsel is essential "to protect the fairness of the trial itself." <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#239" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 239</a></span>; cf. <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#27" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1, 27-28</a></span> (STEWART, J., dissenting).</p>
<p>The Court held in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> that a post-indictment, pretrial lineup at which the accused was exhibited to identifying witnesses was such a critical stage, because of the substantial possibility that the accused's right to a fair trial would otherwise be irretrievably lost. The hazard of unfair suggestive influence at a lineup, which, because of the nature of the proceeding, could seldom be reconstructed at trial, left little doubt, the Court thought, "that for Wade the post-indictment lineup was a critical stage of the prosecution at which he was `as much entitled to such aid [of counsel] . . . as at the trial itself.'" 388 U. S., at 237.</p>
<p><span class="star-pagination">*323</span> The Court stressed in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> that the danger of mistaken identification at trial was appreciably heightened by the "degree of suggestion inherent in the manner in which the prosecution presents the suspect to witnesses for pretrial identification." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#228" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 228</a></span>. There are numerous and subtle possibilities for such improper suggestion in the dynamic context of a lineup. Judge Wilkey, dissenting in the present case, accurately described a lineup as:</p>
<blockquote>"a little drama, stretching over an appreciable span of time. The accused is there in the flesh, three-dimensional and always full-length. Further, he isn't merely there, he acts. He walks on stage, he blinks in the glare of lights, he turns and twists, often muttering asides to those sharing the spotlight. He can be required to utter significant words, to turn a profile or back, to walk back and forth, to doff one costume and don another. All the while the potentially identifying witness is watching, a prosecuting attorney and a police detective at his elbow, ready to record the witness' every word and reaction." 149 U. S. App. D. C. 1, 17, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/#108" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d 92, 108</a></span>.</blockquote>
<p>With no attorney for the accused present at this "little drama," defense counsel at trial could seldom convincingly discredit a witness' courtroom identification by showing it to be based on an impermissibly suggestive lineup. In addition to the problems posed by the fluid nature of a lineup, the Court in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> pointed out that neither the witnesses nor the lineup participants were likely to be alert for suggestive influences or schooled in their detection. "In short, the accused's inability effectively to reconstruct at trial any unfairness that occurred at the lineup may deprive him of his only opportunity meaningfully to attack the credibility of the witness' court-room identification." 388 U. S., at 231-232.</p>
<p><span class="star-pagination">*324</span> The Court held, therefore, that counsel was required at a lineup, primarily as an observer, to ensure that defense counsel could effectively confront the prosecution's evidence at trial. Attuned to the possibilities of suggestive influences, a lawyer could see any unfairness at a lineup, question the witnesses about it at trial, and effectively reconstruct what had gone on for the benefit of the jury or trial judge.<sup>[*]</sup></p>
<p>A photographic identification is quite different from a lineup, for there are substantially fewer possibilities of impermissible suggestion when photographs are used, and those unfair influences can be readily reconstructed at trial. It is true that the defendant's photograph may be markedly different from the others displayed, but this unfairness can be demonstrated at trial from an actual comparison of the photographs used or from the witness' description of the display. Similarly, it is possible that the photographs could be arranged in a suggestive manner, or that by comment or gesture the prosecuting authorities might single out the defendant's picture. But these are the kinds of overt influence that a witness can easily recount and that would serve to impeach the identification testimony. In short, there are few possibilities for unfair suggestivenessand those rather blatant and easily reconstructed. Accordingly, an accused would not be foreclosed from an effective cross-examination of an identification witness simply because his counsel was <span class="star-pagination">*325</span> not present at the photographic display. For this reason, a photographic display cannot fairly be considered a "critical stage" of the prosecution. As the Court of Appeals for the Third Circuit aptly concluded:</p>
<blockquote>"If . . . the identification is not in a live lineup at which defendant may be forced to act, speak or dress in a suggestive way, where the possibilities for suggestion are multiplied, where the ability to reconstruct the events is minimized, and where the effect of a positive identification is likely to be permanent, but at a viewing of immobile photographs easily reconstructible, far less subject to subtle suggestion, and far less indelible in its effect when the witness is later brought face to face with the accused, there is even less reason to denominate the procedure a critical stage at which counsel must be present." <i>United States ex rel. Reed</i> v. <i>Anderson,</i> <span class="citation" data-id="9458303"><a href="/opinion/303865/united-states-of-america-ex-rel-cleveland-reed-v-raymond-anderson/#745" aria-description="Citation for case: United States of America Ex Rel. Cleveland Reed v....">461 F. 2d 739, 745</a></span>.</blockquote>
<p>Preparing witnesses for trial by checking their identification testimony against a photographic display is little different, in my view, from the prosecutor's other interviews with the victim or other witnesses before trial. See <i>United States</i> v. <i>Bennett,</i> <span class="citation" data-id="284440"><a href="/opinion/284440/united-states-v-charles-t-bennett-wilbert-haywood-elmer-jessup-henry/#900" aria-description="Citation for case: United States v. Charles T. Bennett, Wilbert Haywood,...">409 F. 2d 888, 900</a></span>. While these procedures can be improperly conducted, the possibility of irretrievable prejudice is remote, since any unfairness that does occur can usually be flushed out at trial through cross-examination of the prosecution witnesses. The presence of defense counsel at such pretrial preparatory sessions is neither appropriate nor necessary under our adversary system of justice "to preserve the defendant's basic right to a fair trial as affected by his right meaningfully to cross-examine the witnesses against him and to have effective assistance of counsel at the trial itself." <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#227" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 227</a></span>.</p>
<p><span class="star-pagination">*326</span> MR. JUSTICE BRENNAN, with whom MR. JUSTICE DOUGLAS and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>The Court holds today that a pretrial display of photographs to the witnesses of a crime for the purpose of identifying the accused, unlike a lineup, does not constitute a "critical stage" of the prosecution at which the accused is constitutionally entitled to the presence of counsel. In my view, today's decision is wholly unsupportable in terms of such considerations as logic, consistency, and, indeed, fairness. As a result, I must reluctantly conclude that today's decision marks simply another<sup>[1]</sup> step towards the complete evisceration of the fundamental constitutional principles established by this Court, only six years ago, in <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967); <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967); and <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span> (1967). I dissent.</p>
<p></p>
<h2>I</h2>
<p>On the morning of August 26, 1965, two men wearing stocking masks robbed the American Security and Trust Co. in Washington, D. C. The robbery lasted only about three or four minutes and, on the day of the crime, none of the four witnesses was able to give the police a description of the robbers' facial characteristics. Some five months later, on February 3, 1966, an FBI agent showed each of the four witnesses a group of black and white mug shots of the faces of five black males, including respondent, all of generally the same age, height, and weight. Respondent's photograph was included because of information received from a Government informant charged with other crimes.<sup>[2]</sup> None of the witnesses <span class="star-pagination">*327</span> was able to make a "positive" identification of respondent.<sup>[3]</sup></p>
<p>On April 1, 1966, an indictment was returned charging respondent and a codefendant in five counts relating to the robbery of the American Security and Trust Co. Trial was finally set for May 8, 1968, almost three years after the crime and more than two years after the return of the indictment. During the entire two-year period between indictment and trial, although one of the witnesses expressly sought an opportunity to see respondent in person, the Government never attempted to arrange a corporeal lineup for the purposes of identification. Rather, <i>less than 24 hours before trial,</i> the FBI agent, accompanied by the prosecutor, showed five color photographs to the witnesses, three of whom identified the picture of respondent.</p>
<p>At trial, all four witnesses made in-court identifications of respondent, but only one of these witnesses was "positive" of her identification. The fact that three of the witnesses had previously identified respondent from the color photographs, and the photographs themselves, were also admitted into evidence. The only other evidence <span class="star-pagination">*328</span> implicating respondent in the crime was the testimony of the Government informant.<sup>[4]</sup> On the basis of this evidence, respondent was convicted on all counts of the indictment.</p>
<p>On appeal, the United States Court of Appeals for the District of Columbia Circuit, sitting en banc, reversed respondent's conviction. 149 U. S. App. D. C. 1, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d 92</a></span> (1972). Noting that "the dangers of mistaken identification from uncounseled lineup identifications . . . are applicable in large measure to photographic as well as corporeal identifications,"<sup>[5]</sup> the Court of Appeals reasoned that this Court's decisions in <i>Wade, Gilbert,</i> and <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>,</i> compelled the conclusion that a pretrial photographic identification, like a lineup, is a "critical" stage of the prosecution at which the accused is constitutionally entitled to the attendance of counsel. Accordingly, the Court of Appeals held that respondent was denied his Sixth Amendment right to "the Assistance of Counsel for his defence" when his attorney was not given an opportunity to attend the display of the color photographs on the very eve of trial.<sup>[6]</sup> In my view, both the reasoning and conclusion of the Court of Appeals were unimpeachably correct, and I would therefore affirm.</p>
<p></p>
<h2>II</h2>
<p>In June 1967, this Court decided a trilogy of "lineup" cases which brought into sharp focus the problems of <span class="star-pagination">*329</span> pretrial identification. See <i>United States</i> v. <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade, supra</a></span></i><i>; </i><i>Gilbert</i> v. <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">California, supra</a></span></i><i>; </i><i>Stovall</i> v. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Denno, supra</a></span></i><i>.</i> In essence, those decisions held (1) that a pretrial lineup is a "critical stage" in the criminal process at which the accused is constitutionally entitled to the presence of counsel; (2) that evidence of an identification of the accused at such an uncounseled lineup is <i>per se</i> inadmissible; and (3) that evidence of a subsequent in-court identification of the accused is likewise inadmissible unless the Government can demonstrate by clear and convincing evidence that the in-court identification was based upon observations of the accused independent of the prior uncounseled lineup identification. The considerations relied upon by the Court in reaching these conclusions are clearly applicable to photographic as well as corporeal identifications. Those considerations bear repeating here in some detail, for they touch upon the very heart of our criminal justice systemthe right of an accused to a fair trial, including the effective "Assistance of Counsel for his defence."</p>
<p>At the outset, the Court noted that "identification evidence is peculiarly riddled with innumerable dangers and variable factors which might seriously, even crucially, derogate from a fair trial." <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#228" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 228</a></span>. Indeed, "[t]he vagaries of eyewitness identification are well-known; the annals of criminal law are rife with instances of mistaken identification." <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Ibid.</a></span></i> Apart from "the dangers inherent in eyewitness identification," <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><i>id.,</i> at 235</a></span>, such as unreliable memory or perception, the Court pointed out that "[a] major factor contributing to the high incidence of miscarriage of justice from mistaken identification has been the degree of suggestion inherent in the manner in which the prosecution presents the suspect to witnesses for pretrial identification." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#228" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 228</a></span>. The Court recognized that the dangers of suggestion are not necessarily due to "police <span class="star-pagination">*330</span> procedures intentionally designed to prejudice an accused." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 235</a></span>. On the contrary, "[s]uggestion can be created intentionally or unintentionally in many subtle ways." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#229" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 229</a></span>. And the "`fact that the police themselves have, in a given case, little or no doubt that the man put up for identification has committed the offense . . . involves a danger that this persuasion may communicate itself even in a doubtful case to the witness in some way . . . .'" <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 235</a></span>, quoting Williams &amp; Hammelmann, Identification Parades-I, [1963] Crim. L. Rev. 479, 483.</p>
<p>The Court also expressed concern over the possibility that a mistaken identification at a pretrial lineup might itself be conclusive on the question of identity, thereby resulting in the conviction of an innocent man. The Court observed that "`once a witness has picked out the accused at the line-up, he is not likely to go back on his word later on, so that in practice the issue of identity may (in the absence of other relevant evidence) for all practical purposes be determined there and then, before the trial.'" <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#229" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 229</a></span>, quoting Williams &amp; Hammelmann, <i>supra,</i> at 482.</p>
<p>Moreover, "the defense can seldom reconstruct the manner and mode of lineup identification for judge or jury at trial." <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#230" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 230</a></span>. For "as is the case with secret interrogations, there is serious difficulty in depicting what transpires at lineups . . . ." <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Ibid.</a></span></i> Although the accused is present at such corporeal identifications, he is hardly in a position to detect many of the more subtle "improper influences" that might infect the identification.<sup>[7]</sup> In addition, the Court emphasized <span class="star-pagination">*331</span> that "neither witnesses nor lineup participants are apt to be alert for conditions prejudicial to the suspect. And, if they were, it would likely be of scant benefit to the suspect since neither witnesses nor lineup participants are likely to be schooled in the detection of suggestive influences." <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Ibid.</a></span></i> As a result, "even though cross-examination is a precious safeguard to a fair trial, it cannot [in this context] be viewed as an absolute assurance of accuracy and reliability." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 235</a></span>.</p>
<p>With these considerations in mind, the Court reasoned that "the accused's inability effectively to reconstruct at trial any unfairness that occurred at the lineup may deprive him of his only opportunity meaningfully to attack the credibility of the witness' courtroom identification." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#231" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 231-232</a></span>. And "[i]nsofar as the accused's conviction may rest on a courtroom identification in fact the fruit of a suspect pretrial identification which the accused is helpless to subject to effective scrutiny at trial, the accused is deprived of that right of cross-examination which is an essential safeguard to his right to confront the witnesses against him." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 235</a></span>. Thus, noting that "presence of counsel [at the lineup] can often avert prejudice and assure a meaningful confrontation at trial," the Court concluded that a pretrial corporeal identification is "a critical stage of the prosecution at which [the accused is] `as much entitled to such aid [of counsel] . . . as at the trial itself.'" <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#236" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 236, 237</a></span>, quoting <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#57" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45, 57</a></span> (1932).</p>
<p></p>
<h2>
<span class="star-pagination">*332</span> III</h2>
<p>As the Court of Appeals recognized, "the dangers of mistaken identification . . . set forth in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> are applicable in large measure to photographic as well as corporeal identifications." 149 U. S. App. D. C., at 9, 461 F. 2d, at 100. To the extent that misidentification may be attributable to a witness' faulty memory or perception, or inadequate opportunity for detailed observation during the crime, the risks are obviously as great at a photographic display as at a lineup.<sup>[8]</sup> But "[b]ecause of the inherent limitations of photography, which presents its subject in two dimensions rather than the three dimensions of reality, . . . a photographic identification, even when properly obtained, is clearly inferior to a properly obtained corporeal identification." P. Wall, Eye-Witness Identification in Criminal Cases 70 (1965). Indeed, noting "the hazards of initial identification by photograph," we have expressly recognized that "a corporeal identification. . . is normally more accurate" than a photographic identification. <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 384</a></span>, 386 n. 6 (1968).<sup>[9]</sup> Thus, in this sense at <span class="star-pagination">*333</span> least, the dangers of misidentification are even greater at a photographic display than at a lineup.</p>
<p>Moreover, as in the lineup situation, the possibilities for impermissible suggestion in the context of a photographic display are manifold. See <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#383" aria-description="Citation for case: Simmons v. United States"><i>id.,</i> at 383</a></span>. Such suggestion, intentional or unintentional, may derive from three possible sources. First, the photographs themselves might tend to suggest which of the pictures is that of the suspect. For example, differences in age, pose, or other physical characteristics of the persons represented, and variations in the mounting, background, lighting, or markings of the photographs all might have the effect of singling out the accused.<sup>[10]</sup></p>
<p>Second, impermissible suggestion may inhere in the manner in which the photographs are displayed to the witness. The danger of misidentification is, of course, "increased if the police display to the witness . . . the pictures of several persons among which the photograph of a single such individual recurs or is in some way emphasized." <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Ibid.</a></span></i> And, if the photographs are arranged in an asymmetrical pattern, or if they are displayed in a time sequence that tends to emphasize a particular photograph, "any identification of the photograph which stands out from the rest is no more reliable than an identification of a single photograph, exhibited alone." P. Wall, <i>supra,</i> at 81.</p>
<p>Third, gestures or comments of the prosecutor at the time of the display may lead an otherwise uncertain <span class="star-pagination">*334</span> witness to select the "correct" photograph. For example, the prosecutor might "indicate to the witness that [he has] other evidence that one of the persons pictured committed the crime,"<sup>[11]</sup> and might even point to a particular photograph and ask whether the person pictured "looks familiar." More subtly, the prosecutor's inflection, facial expressions, physical motions, and myriad other almost imperceptible means of communication might tend, intentionally or unintentionally, to compromise the witness' objectivity. Thus, as is the case with lineups, "[i]mproper photographic identification procedures,. . . by exerting a suggestive influence upon the witnesses, can often lead to an erroneous identification. . . ." P. Wall, <i>supra,</i> at 89.<sup>[12]</sup> And "[r]egardless of how the initial misidentification comes about, the witness <span class="star-pagination">*335</span> thereafter is apt to retain in his memory the image of the photograph rather than of the person actually seen . . . ." <i>Simmons</i> v. <i>United States, supra,</i> at 383-384.<sup>[13]</sup> As a result, "`the issue of identity may (in the absence of other relevant evidence) for all practical purposes be determined there and then, before the trial.'" <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#229" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 229</a></span>, quoting Williams &amp; Hammelmann, <i>supra,</i> at 482.</p>
<p>Moreover, as with lineups, the defense can "seldom reconstruct" at trial the mode and manner of photographic identification. It is true, of course, that the photographs used at the pretrial display might be preserved for examination at trial. But "it may also be said that a photograph can preserve the record of a lineup; yet this does not justify a lineup without counsel." 149 U. S. App. D. C., at 9-10, 461 F. 2d, at 100-101. Cf. <i>United States</i> v. <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade, supra,</a></span></i> at 239 and n. 30. Indeed, in reality, preservation of the photographs affords little protection to the unrepresented accused. For, although retention of the photographs may mitigate the dangers of misidentification due to the suggestiveness of the photographs themselves, it cannot in any sense reveal to defense counsel the more subtle, and therefore more dangerous, suggestiveness that might derive from the manner in which the photographs were displayed or any accompanying comments or gestures. Moreover, the accused cannot rely upon the witnesses themselves to expose these latter sources of suggestion, for the witnesses are not "apt to be alert for conditions prejudicial to the suspect. And if they were, it would likely be of scant benefit to the suspect" since the witnesses are hardly "likely to be schooled in the detection of suggestive influences." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#230" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 230</a></span>.</p>
<p><span class="star-pagination">*336</span> Finally, and <i>unlike</i> the lineup situation, the accused himself is not even present at the photographic identification, thereby reducing the likelihood that irregularities in the procedures will ever come to light. Indeed, in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> the Government itself observed:<sup>[14]</sup></p>
<blockquote>"When the defendant is presentas he is during a lineuphe may personally observe the circumstances, report them to his attorney, and (if he chooses to take the stand) testify about them at trial. . . . [I]n the absence of an accused, on the other hand, there is no one present to verify the fairness of the interview or to report any irregularities. If the prosecution were tempted to engage in `sloppy or biased or fraudulent' conduct . . ., it would be far more likely to do so when the accused is absent than when he himself is being `used.'"</blockquote>
<p>Thus, the difficulties of reconstructing at trial an uncounseled photographic display are at least equal to, and possibly greater than, those involved in reconstructing an uncounseled lineup.<sup>[15]</sup> And, as the Government argued <span class="star-pagination">*337</span> in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> in terms of the need for counsel, "[t]here is no meaningful difference between a witness' pretrial identification from photographs and a similar identification made at a lineup."<sup>[16]</sup> For, in both situations "the accused's inability effectively to reconstruct at trial any unfairness that occurred at the [pretrial identification] may deprive him of his only opportunity meaningfully to attack the credibility of the witness' courtroom identification." <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#231" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 231-232</a></span>. As <span class="star-pagination">*338</span> a result, both photographic and corporeal identifications create grave dangers that an innocent defendant might be convicted simply because of his inability to expose a tainted identification. This being so, considerations of logic, consistency, and, indeed, fairness compel the conclusion that a pretrial photographic identification, like a pretrial corporeal identification, is a "critical stage of the prosecution at which [the accused is] `as much entitled to such aid [of counsel] . . . as at the trial itself.'" <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#237" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 237</a></span>, quoting <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#57" aria-description="Citation for case: Powell v. Alabama">287 U. S., at 57</a></span>.</p>
<p></p>
<h2>IV</h2>
<p>Ironically, the Court does not seriously challenge the proposition that presence of counsel at a pretrial photographic display is essential to preserve the accused's right to a fair trial on the issue of identification. Rather, in what I can only characterize a triumph of form over substance, the Court seeks to justify its result by engrafting a wholly unprecedentedand wholly unsupportablelimitation on the Sixth Amendment right of "the accused . . . to have the Assistance of Counsel for his defence." Although apparently conceding that the right to counsel attaches, not only at the trial itself, but at all "critical stages" of the prosecution, see <i>ante,</i> at 309-311, the Court holds today that, in order to be deemed "critical," the particular "stage of the prosecution" under consideration must, at the very least, involve the physical "presence of the accused," at a "trial-like confrontation" with the Government, at which the accused requires the "guiding hand of counsel." According to the Court a pretrial photographic identification does not, of course, meet these criteria.</p>
<p>In support of this rather crabbed view of the Sixth Amendment, the Court cites our decisions in <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970), <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964), <i>White</i> v. <i>Maryland,</i> 373 U. S. 59 <span class="star-pagination">*339</span> (1963), and <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span> (1961). Admittedly, each of these decisions guaranteed the assistance of counsel in pretrial proceedings at least arguably involving the physical "presence of the accused," at a "trial-like confrontation" with the Government, at which the accused required the "guiding hand of counsel."<sup>[17]</sup> Moreover, as the Court points out, these decisions are consistent with the view that the Sixth Amendment "embodies a realistic recognition of the obvious truth that the average defendant does not have the professional legal skill to protect himself when brought before a tribunal with power to take his life or liberty, wherein the prosecution is presented by experienced and learned counsel." <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#462" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 462-463</a></span> (1938). But, contrary to the Court's assumption, this is merely one <i>facet</i> of the Sixth Amendment guarantee, and the decisions relied upon by the Court represent, not the boundaries of the right to counsel, but mere applications of a far broader and more reasoned understanding of the Sixth Amendment than that espoused today.</p>
<p>The fundamental premise underlying <i>all</i> of this Court's decisions holding the right to counsel applicable at "critical" pretrial proceedings, is that a "stage" of the prosecution must be deemed "critical" for the purposes of the Sixth Amendment if it is one at which the presence of counsel is necessary "to protect the fairness of <i>the trial itself." </i><i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#239" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., 218, 239</a></span> (1973) (emphasis added). Thus, in <i>Hamilton</i> v. <i>Alabama,</i> <span class="star-pagination">*340</span> <i>supra</i><i>,</i> for example, we made clear that an arraignment under Alabama law is a "critical stage" of the prosecution, not only because the accused at such an arraignment requires "the guiding hand of counsel," but, more broadly, because "[w]hat happens there may affect the whole trial." <i>Id.,</i> at 54. Indeed, to exclude counsel from a pretrial proceeding at which his presence might be necessary to assure the fairness of the subsequent trial would, in practical effect, render the Sixth Amendment guarantee virtually meaningless, for it would "deny a defendant `effective representation by counsel at the only stage when legal aid and advice would help him.'" <i>Massiah</i> v. <i>United States, supra,</i> at 204, quoting <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#326" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 326</a></span> (1959) (DOUGLAS, J., concurring); see <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#484" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478, 484-485</a></span> (1964).</p>
<p>This established conception of the Sixth Amendment guarantee is, of course, in no sense dependent upon the physical "presence of the accused," at a "trial-like confrontation" with the Government, at which the accused requires the "guiding hand of counsel." On the contrary, in <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span> (1932), the seminal decision in this area, we explicitly held the right to counsel applicable at a stage of the pretrial proceedings involving <i>none</i> of the three criteria set forth by the Court today. In <i><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">Powell</a></span>,</i> the defendants in a state felony prosecution were not appointed counsel until the very eve of trial. This Court held, in no uncertain terms, that such an appointment could not satisfy the demands of the Sixth Amendment, for "`[i]t is vain . . . to guarantee [the accused] counsel without giving the latter any opportunity to acquaint himself with the facts or law of the case.'" <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#59" aria-description="Citation for case: Powell v. Alabama"><i>Id.,</i> at 59</a></span>. In other words, <i><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">Powell</a></span></i> made clear that, in order to preserve the accused's right to a fair trial and to "effective and substantial"<sup>[18]</sup> assistance <span class="star-pagination">*341</span> of counsel at that trial, the Sixth Amendment guarantee necessarily encompasses a reasonable period of time before trial during which counsel might prepare the defense. Yet it can hardly be said that this preparatory period of research and investigation involves the physical "presence of the accused," at a "trial-like confrontation" with the Government, at which the accused requires the "guiding hand of counsel."</p>
<p>Moreover, despite the Court's efforts to rewrite <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> so as to suggest a precedential basis for its own analysis,<sup>[19]</sup> the rationale of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> lends no support whatever to today's decision. In <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> after concluding that compelled participation in a lineup does not violate the accused's right against self-incrimination,<sup>[20]</sup> the Court addressed the argument "that the assistance of counsel at the lineup was indispensable to protect Wade's most basic right as a criminal defendanthis right to a fair trial at which the witnesses against him might be meaningfully cross-examined." 388 U. S., at 223-224. The Court then surveyed the history of the Sixth Amendment, and specifically concluded that that Amendment guarantees "counsel's assistance <i>whenever</i> necessary to assure a meaningful `defence.'" <i>Id.,</i> at 225 (emphasis added). <span class="star-pagination">*342</span> Then, after examining this Court's prior decisions concerning the applicability of the counsel guarantee,<sup>[21]</sup> the Court stressed once again that a pretrial proceeding is a "critical stage" of the prosecution if "the presence of his counsel is necessary to preserve the defendant's basic right to a fair trial as affected by his right meaningfully to cross-examine the witnesses against him and to have effective assistance of counsel at the trial itself." <i>Id.,</i> at 227.</p>
<p>The Court next addressed the Government's contention that a lineup is "a mere preparatory step in the gathering of the prosecution's evidence, not differentfor Sixth Amendment purposesfrom various other preparatory steps, such as systematized or scientific analyzing of the accused's fingerprints, blood sample, clothing, hair, and the like." <i>Id.,</i> at 227. If the Court in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> had even the remotest intention of embracing the wooden interpretation of the Sixth Amendment ascribed to it today, it could have rejected the Government's contention simply by pointing out the obvious fact that such "systematized or scientific analyzing" does not in any sense involve the physical "presence of the accused," at a "trial-like confrontation" with the Government, at which the accused requires the "guiding hand of counsel." But the Court offered not even the slightest hint of such <span class="star-pagination">*343</span> an approach. Instead, the Court reasoned that, in light of the scientific nature of such analyses,</p>
<blockquote>"the accused has the opportunity for a meaningful confrontation of the Government's case at trial through the ordinary processes of cross-examination of the Government's expert witnesses and the presentation of the evidence of his own experts. The denial of a right to have his counsel present at such analyses does not therefore violate the Sixth Amendment; <i>they are not critical stages since there is minimal risk that his counsel's absence at such stages might derogate from his right to a fair trial." Id.,</i> at 227-228 (emphasis added).</blockquote>
<p>Finally, after discussing the dangers of misidentification arising out of lineup procedures and the difficulty of reconstructing the lineup at trial, the Court noted that "[i]nsofar as the accused's conviction may rest on a court-room identification in fact the fruit of a suspect pretrial identification which the accused is helpless to subject to effective scrutiny at trial, the accused is deprived of that right of cross-examination which is an essential safeguard to his right to confront the witnesses against him." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 235</a></span>. The Court therefore concluded that "[s]ince it appears that there is grave potential for prejudice, intentional or not, in the pretrial lineup, which may not be capable of reconstruction at trial, and since presence of counsel itself can often avert prejudice and assure a meaningful confrontation at trial, there can be little doubt that for Wade the post-indictment lineup was a critical stage of the prosecution at which he was `as much entitled to such aid [of counsel] . . . as at the trial itself.'" <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#236" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 236-237</a></span>.</p>
<p>Thus, contrary to the suggestion of the Court, the conclusion in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> that a pretrial lineup is a "critical stage" of the prosecution did not in any sense turn on <span class="star-pagination">*344</span> the fact that a lineup involves the physical "presence of the accused" at a "trial-like confrontation" with the Government. And that conclusion most certainly did not turn on the notion that presence of counsel was necessary so that counsel could offer legal advice or "guidance" to the accused at the lineup. On the contrary, <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> envisioned counsel's function at the lineup to be primarily that of a trained observer, able to detect the existence of any suggestive influences and capable of understanding the legal implications of the events that transpire. Having witnessed the proceedings, counsel would then be in a position effectively to reconstruct at trial any unfairness that occurred at the lineup, thereby preserving the accused's fundamental right to a fair trial on the issue of identification.</p>
<p>There is something ironic about the Court's conclusion today that a pretrial lineup identification is a "critical stage" of the prosecution because counsel's presence can help to compensate for the accused's deficiencies as an observer, but that a pretrial photographic identification is not a "critical stage" of the prosecution because the accused is not able to observe at all. In my view, there simply is no meaningful difference, in terms of the need for attendance of counsel, between corporeal and photographic identifications. And applying established and well-reasoned Sixth Amendment principles, I can only conclude that a pretrial photographic display, like a pretrial lineup, is a "critical stage" of the prosecution at which the accused is constitutionally entitled to the presence of counsel.</p>
<h2>NOTES</h2>
<p>[1]  "In all criminal prosecutions, the accused shall enjoy the right . . . to have the Assistance of Counsel for his defence."</p>
<p>[2]  <i>United States</i> v. <i>Bennett,</i> <span class="citation" data-id="284440"><a href="/opinion/284440/united-states-v-charles-t-bennett-wilbert-haywood-elmer-jessup-henry/#898" aria-description="Citation for case: United States v. Charles T. Bennett, Wilbert Haywood,...">409 F. 2d 888, 898-900</a></span> (CA2), cert. denied <i>sub nom. </i><i>Haywood</i> v. <i>United States,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./396/852/">396 U. S. 852</a></span> (1969); <i>United States ex rel. Reed</i> v. <i>Anderson,</i> <span class="citation" data-id="9458303"><a href="/opinion/303865/united-states-of-america-ex-rel-cleveland-reed-v-raymond-anderson/" aria-description="Citation for case: United States of America Ex Rel. Cleveland Reed v....">461 F. 2d 739</a></span> (CA3 1972) (en bane); <i>United States</i> v. <i>Collins,</i> <span class="citation" data-id="9454903"><a href="/opinion/286688/united-states-v-william-francis-collins/" aria-description="Citation for case: United States v. William Francis Collins">416 F. 2d 696</a></span> (CA4 1969), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./396/1025/">396 U. S. 1025</a></span> (1970); <i>United States</i> v. <i>Ballard,</i> <span class="citation" data-id="288980"><a href="/opinion/288980/united-states-v-erwin-edward-ballard-united-states-of-america-v-richard/" aria-description="Citation for case: United States v. Erwin Edward Ballard, United States of...">423 F. 2d 127</a></span> (CA5 1970); <i>United States</i> v. <i>Serio,</i> <span class="citation" data-id="295836"><a href="/opinion/295836/united-states-v-august-serio-also-known-as-delbert-beard/#829" aria-description="Citation for case: United States v. August Serio, Also Known as Delbert Beard">440 F. 2d 827, 829-830</a></span> (CA6 1971); <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="283186"><a href="/opinion/283186/united-states-v-burnell-robinson/#67" aria-description="Citation for case: United States v. Burnell Robinson">406 F. 2d 64, 67</a></span> (CA7), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./395/926/">395 U. S. 926</a></span> (1969); <i>United States</i> v. <i>Long,</i> <span class="citation" data-id="8886509"><a href="/opinion/8899737/united-states-v-long/#301" aria-description="Citation for case: United States v. Long">449 F. 2d 288, 301-302</a></span> (CA8 1971), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./405/974/">405 U. S. 974</a></span> (1972); <i>Allen</i> v. <i>Rhay,</i> <span class="citation" data-id="292225"><a href="/opinion/292225/gordon-m-allen-and-v-b-j-rhay-superintendent-of-the-washington-state/#1166" aria-description="Citation for case: Gordon M. Allen, and v. B. J. Rhay, Superintendent of the...">431 F. 2d 1160, 1166-1167</a></span> (CA9 1970); <i>McGee</i> v. <i>United States,</i> <span class="citation" data-id="282032"><a href="/opinion/282032/floyd-lenox-mcgee-v-united-states/#436" aria-description="Citation for case: Floyd Lenox McGee v. United States">402 F. 2d 434, 436</a></span> (CA10 1968), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./394/908/">394 U. S. 908</a></span> (1969). The en banc decision of the Third Circuit in <i>Anderson</i> overruled in part a panel decision in <i>United States</i> v. <i>Zeiler,</i> <span class="citation" data-id="290782"><a href="/opinion/290782/united-states-v-william-edward-zeiler-united-states-of-america-v-william/" aria-description="Citation for case: United States v. William Edward Zeiler, United States of...">427 F. 2d 1305</a></span> (CA3 1970).
</p>
<p>The question has also produced conflicting decisions in state courts. The majority view, as in the courts of appeals, rejects the claimed right, to counsel. See, <i>e. g., </i><i>McGhee</i> v. <i>State,</i> <span class="citation" data-id="1724451"><a href="/opinion/1724451/mcghee-v-state/" aria-description="Citation for case: McGhee v. State">48 Ala. App. 330</a></span>, <span class="citation" data-id="1724451"><a href="/opinion/1724451/mcghee-v-state/" aria-description="Citation for case: McGhee v. State">264 So. 2d 560</a></span> (Ala. Crim. App. 1972); <i>State</i> v. <i>Yehling,</i> <span class="citation" data-id="1353187"><a href="/opinion/1353187/state-v-yehling/" aria-description="Citation for case: State v. Yehling">108 Ariz. 323</a></span>, <span class="citation" data-id="1353187"><a href="/opinion/1353187/state-v-yehling/" aria-description="Citation for case: State v. Yehling">498 P. 2d 145</a></span> (1972); <i>People</i> v. <i>Lawrence,</i> <span class="citation" data-id="9552312"><a href="/opinion/1186833/people-v-lawrence/" aria-description="Citation for case: People v. Lawrence">4 Cal. 3d 273</a></span>, <span class="citation" data-id="9552312"><a href="/opinion/1186833/people-v-lawrence/" aria-description="Citation for case: People v. Lawrence">481 P. 2d 212</a></span> (1971), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./407/909/">407 U. S. 909</a></span> (1972); <i>Reed</i> v. <i>State,</i> ___ Del. ___, <span class="citation" data-id="2061648"><a href="/opinion/2061648/reed-v-state/" aria-description="Citation for case: Reed v. State">281 A. 2d 142</a></span> (1971); <i>People</i> v. <i>Holiday,</i> <span class="citation" data-id="2087977"><a href="/opinion/2087977/the-people-v-holiday/" aria-description="Citation for case: The PEOPLE v. Holiday">47 Ill. 2d 300</a></span>, <span class="citation" data-id="2087977"><a href="/opinion/2087977/the-people-v-holiday/" aria-description="Citation for case: The PEOPLE v. Holiday">265 N. E. 2d 634</a></span> (1970); <i>Baldwin</i> v. <i>State,</i> <span class="citation" data-id="2172829"><a href="/opinion/2172829/baldwin-v-state/" aria-description="Citation for case: Baldwin v. State">5 Md. App. 22</a></span>, <span class="citation" data-id="2172829"><a href="/opinion/2172829/baldwin-v-state/" aria-description="Citation for case: Baldwin v. State">245 A. 2d 98</a></span> (1968) (dicta); <i>Commonwealth</i> v. <i>Ross,</i> ___ Mass. ___, <span class="citation" data-id="2133215"><a href="/opinion/2133215/commonwealth-v-ross/" aria-description="Citation for case: Commonwealth v. Ross">282 N. E. 2d 70</a></span> (1972), vacated on other grounds and remanded, <span class="citation multiple-matches"><a href="/c/U.%20S./410/901/">410 U. S. 901</a></span> (1973); <i>Stevenson</i> v. <i>State,</i> <span class="citation" data-id="1911421"><a href="/opinion/1911421/stevenson-v-state/" aria-description="Citation for case: Stevenson v. State">244 So. 2d 30</a></span> (Miss. 1971); <i>State</i> v. <i>Brookins,</i> <span class="citation" data-id="1534458"><a href="/opinion/1534458/state-v-brookins/" aria-description="Citation for case: State v. Brookins">468 S. W. 2d 42</a></span> (Mo. 1971) (dicta); <i>People</i> v. <i>Coles,</i> 34 App. Div. 2d 1051, 312 N. Y. S. 2d 621 (1970) (dicta); <i>State</i> v. <i>Moss,</i> <span class="citation" data-id="1710337"><a href="/opinion/1710337/state-v-moss/" aria-description="Citation for case: State v. Moss">187 Neb. 391</a></span>, <span class="citation" data-id="1710337"><a href="/opinion/1710337/state-v-moss/" aria-description="Citation for case: State v. Moss">191 N. W. 2d 543</a></span> (1971); <i>Drewry</i> v. <i>Commonwealth,</i> <span class="citation" data-id="1241302"><a href="/opinion/1241302/dreway-v-commonwealth/" aria-description="Citation for case: DREWAY v. Commonwealth">213 Va. 186</a></span>, <span class="citation" data-id="1241302"><a href="/opinion/1241302/dreway-v-commonwealth/" aria-description="Citation for case: DREWAY v. Commonwealth">191 S. E. 2d 178</a></span> (1972); <i>State</i> v. <i>Nettles,</i> <span class="citation" data-id="9793951"><a href="/opinion/2616794/state-v-nettles/" aria-description="Citation for case: State v. Nettles">81 Wash. 2d 205</a></span>, <span class="citation" data-id="9793951"><a href="/opinion/2616794/state-v-nettles/" aria-description="Citation for case: State v. Nettles">500 P. 2d 752</a></span> (1972); <i>Kain</i> v. <i>State,</i> <span class="citation" data-id="1838693"><a href="/opinion/1838693/kain-v-state/" aria-description="Citation for case: Kain v. State">48 Wis. 2d 212</a></span>, <span class="citation multiple-matches"><a href="/c/N.%20W.%202d/179/777/">179 N. W. 2d 777</a></span> (1970). Cf. <i>State</i> v. <i>Accor,</i> <span class="citation" data-id="1206841"><a href="/opinion/1206841/state-v-accor/" aria-description="Citation for case: State v. Accor">277 N. C. 65</a></span>, <span class="citation" data-id="1206841"><a href="/opinion/1206841/state-v-accor/" aria-description="Citation for case: State v. Accor">175 S. E. 2d 583</a></span> (1970). Several state courts, however, have granted a right to counsel at photographic identifications. See, <i>e. g., </i><i>Cox</i> v. <i>State,</i> <span class="citation" data-id="1758004"><a href="/opinion/1758004/cox-v-state/" aria-description="Citation for case: Cox v. State">219 So. 2d 762</a></span> (Fla. App. 1969) (video tapes); <i>People</i> v. <i>Anderson,</i> <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/" aria-description="Citation for case: People v. Anderson">389 Mich. 155</a></span>, <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/" aria-description="Citation for case: People v. Anderson">205 N. W. 2d 461</a></span> (1973); <i>Thompson</i> v. <i>State,</i> <span class="citation" data-id="9629152"><a href="/opinion/1434555/thompson-v-state/" aria-description="Citation for case: Thompson v. State">85 Nev. 134</a></span>, <span class="citation" data-id="9629152"><a href="/opinion/1434555/thompson-v-state/" aria-description="Citation for case: Thompson v. State">451 P. 2d 704</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./396/893/">396 U. S. 893</a></span> (1969); <i>Commonwealth</i> v. <i>Whiting,</i> <span class="citation" data-id="2178575"><a href="/opinion/2178575/commonwealth-v-whiting/" aria-description="Citation for case: Commonwealth v. Whiting">439 Pa. 205</a></span>, <span class="citation" data-id="2178575"><a href="/opinion/2178575/commonwealth-v-whiting/" aria-description="Citation for case: Commonwealth v. Whiting">266 A. 2d 738</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./400/919/">400 U. S. 919</a></span> (1970).</p>
<p>[3]  Respondent Ash does not assert a right to counsel at the black-and-white photographic display in February 1966 because he recognizes that <i>Kirby</i> v. <i>Illinois,</i> <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682</a></span> (1972), forecloses application of the Sixth Amendment to events before the initiation of adversary criminal proceedings. Tr. of Oral Arg. 21-22; Brief for Respondent 32 n. 21.</p>
<p>[4]  At this hearing both the black-and-white and color photographs were introduced as exhibits. App. 44. The FBI agents who conducted the pretrial displays were called as witnesses and were cross-examined fully. App. 10, 28. Two of the four witnesses who were expected to make in-court identifications also testified and were cross-examined concerning the photographic identifications. App. 55, 65.</p>
<p>[5]  The majority of the Court of Appeals concluded that Ash's counsel properly had preserved his objection to introduction of the photographs. 149 U. S. App. D. C., at 6 n. 6, 461 F. 2d, at 97 n. 6. Although the contrary view of the dissenting judges has been noted here by the Government, the majority's ruling on this issue is not asserted by the Government as a basis for reversal. Pet. for Cert. 4 n. 5; Brief for United States 6 n. 6. Under these circumstances, we are not inclined to disturb the ruling of the Court of Appeals on this close procedural question. App. 104, 126-131.</p>
<p>[6]  Although the English limitation was not expressly rejected until 1836, the rule appears to have been relaxed in practice. 9 W. Holdsworth, History of English Law 235 (1926); 4 W. Blackstone, Commentaries *355-356.</p>
<p>[7]  Similar concerns eventually led to abandonment of the common-law rule in England. That rule originated at a time when counsel was said to be "hardly necessary" because expert knowledge of the law was not required at trial and systematic examination of witnesses had not yet developed. T. Plucknett, A Concise History of the Common Law 410 (4th ed. 1948).
</p>
<p>Confrontation with legal technicalities became common at English trials when complex rules developed for attacking the indictment. <i>Ibid.</i> The English response was not an unlimited right to counsel, however, but was rather a right for counsel to argue only legal questions. See <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#60" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45, 60</a></span> (1932). A plea in abatement directed at insufficiency of the indictment, for example, allowed a prisoner to "pray counsel to be assigned to him to manage his exceptions and take more." 2 M. Hale, Pleas of the Crown 236 (1736).</p>
<p>Confrontation with a professional prosecutor arose in English treason trials before it appeared in ordinary criminal trials. See 1 J. Stephen, History of the Criminal Law of England 348-350 (1883). In 1695 this imbalance in the adversary process was corrected by a statute granting prisoners the right to counsel at treason trials. <span class="citation no-link">7 Win. 3</span>, c. 3 (1695). Hawkins explained that the professional ability of king's counsel motivated this reform because it had "been found by experience that prisoners have been often under great disadvantages from the want of counsel, in prosecutions of high treason against the king's person, which are generally managed for the crown with greater skill and zeal than ordinary prosecutions. . . ." 2 W. Hawkins, Pleas of the Crown 566 (Leach ed. 1787). The 1695 statute weakened the English rule and, after a century of narrowing practical application, see n. 6, <i>supra,</i> the rule was finally abrogated by statute in 1836. The Trials for Felony Act, 6 &amp; 7 Wm. 4, c. 114 (1836).</p>
<p>[8]  "[T]he dangers of mistaken identification from uncounseled lineup identifications set forth in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> are applicable in large measure to photographic as well as corporeal identifications. These include, notably, the possibilities of suggestive influence or mistakeparticularly where witnesses had little or no opportunity for detailed observation during the crime; the difficulty of reconstructing suggestivityeven greater when the defendant is not even present; the tendency of a witness's identification, once given under these circumstances, to be frozen. While these difficulties may be somewhat mitigated by preserving the photograph shown, it may also be said that a photograph can preserve the record of a lineup; yet this does not justify a lineup without counsel. The same may be said of the opportunity to examine the participants as to what went on in the course of the identification, whether at lineup or on photograph. Sometimes this may suffice to bring out all pertinent facts, even at a lineup, but this would not suffice under <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> to offset the constitutional infringement wrought by proceeding without counsel. The presence of counsel avoids possibilities of suggestiveness in the manner of presentation that are otherwise ineradicable." 149 U. S. App. D. C., at 9-10, 461 F. 2d, at 100-101.</p>
<p>[9]  The Court rather narrowly defined the issues under consideration:
</p>
<p>"The pretrial <i>confrontation</i> for purpose of identification may take the form of a lineup, also known as an `identification parade' or `showup,' as in the present case, or presentation of the suspect alone to the witness, as in <i>Stovall</i> v. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Denno, supra</a></span></i><i>.</i> It is obvious that risks of suggestion attend either form of <i>confrontation</i> . . . . But as is the case with secret interrogations, there is serious difficulty in depicting what transpires at lineups and <i>other forms of identification confrontations." </i><i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#229" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 229-230</a></span> (1967) (emphasis added).</p>
<p>The photographic identification could hardly have been overlooked by inadvertence since the Government stressed the similarity between lineups and photographic identifications. Brief for United States in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> No. 334, O. T. 1966, pp. 7, 14, 19, 24.</p>
<p>[10]  Duplication by defense counsel is a safeguard that normally is not available when a formal confrontation occurs. Defense counsel has no statutory authority to conduct a preliminary hearing, for example, and defense counsel will generally be prevented by practical considerations from conducting his own lineup. Even in some confrontations, however, the possibility of duplication may be important. The Court noted this in holding that the taking of handwriting exemplars did not constitute a "critical stage":
</p>
<p>"If, for some reason, an unrepresentative exemplar is taken, this can be brought out and corrected through the adversary process at trial since the accused can make an unlimited number of additional exemplars for analysis and comparison by government and defense handwriting experts." <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#267" aria-description="Citation for case: Gilbert v. California">388 U. S. 263, 267</a></span> (1967).</p>
<p>[11]  We do not suggest, of course, that defense counsel has any greater freedom than the prosecution to abuse the photographic identification. Evidence of photographic identifications conducted by the defense may be excluded as unreliable under the same standards that would be applied to unreliable identifications conducted by the Government.</p>
<p>[12]  The Court of Appeals deemed it significant that a photographic identification is admissible as substantive evidence, whereas other parts of interviews may be introduced only for impeachment. 149 U. S. App. D. C., at 10, 461 F. 2d, at 101. In this case defense counsel for Bailey introduced the inability to identify, and that was received into evidence. Thus defense counsel still received benefits equivalent to those available to the prosecution. Although defense counsel may be concerned that repeated photographic displays containing the accused's picture as the only common characteristic will tend to promote identification of the accused, the defense has other balancing devices available to it, such as the use of a sufficiently large number of photographs to counteract this possibility.</p>
<p>[13]  Although the reliability of in-court identifications and the effectiveness of impeachment may be improved by equality of access, we do not suggest that the prosecution's photographic identification would be more easily reconstructed at trial simply because defense counsel could conduct his own photographic display. But, as we have explained, <i>supra,</i> at 315-316, the possibility of perfect reconstruction is relevant to the evaluation of substitutes for counsel, not to the initial designation of an event as a "critical stage."</p>
<p>[14]  Sobel, Assailing the Impermissible Suggestion: Evolving Limitations on the Abuse of Pre-Trial Criminal Identification Methods, 38 Brooklyn L. Rev. 261, 299 (1971); Comment, 43 N. Y. U. L. Rev. 1019, 1022 (1968); Note, 2 Rutgers Camden L. J. 347, 359 (1970); Note, <span class="citation no-link">21 Syracuse L. Rev. 1235</span>, 1241-1242 (1970). A variant of this argument is that photographic identifications may be used to circumvent the need for counsel at lineups. Brief for Respondent 44-45.</p>
<p>[15]  <i>E. g.,</i> P. Wall, Eye-Witness Identification in Criminal Cases 77-85 (1965); Sobel, <i>supra,</i> n. 14, at 309-310; Comment, <span class="citation no-link">56 Iowa L. Rev. 408</span>, 420-421 (1970).</p>
<p>[16]  Throughout a criminal prosecution the prosecutor's ethical responsibility extends, of course, to supervision of any continuing investigation of the case. By prescribing procedures to be used by his agents and by screening the evidence before trial with a view to eliminating unreliable identifications, the prosecutor is able to minimize abuse in photographic displays even if they are conducted in his absence.</p>
<p>[*]  I do not read <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> as requiring counsel because a lineup is a "trial-type" situation, nor do I understand that the Court required the presence of an attorney because of the advice or assistance he could give to his client at the lineup itself. Rather, I had thought the reasoning of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> was that the right to counsel is essentially a protection for the defendant at trial, and that counsel is necessary at a lineup in order to ensure a meaningful confrontation and the effective assistance of counsel at trial.</p>
<p>[1]  See <i>Kirby</i> v. <i>Illinois,</i> <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682</a></span> (1972).</p>
<p>[2]  At the time of respondent's trial, the informant, one Clarence McFarland, was serving a sentence for bank robbery. According to the Court of Appeals, "McFarland had been before the grand jury with regard to five separate offenses, in addition to his bank robbery, and had not been indicted on any of them, including one in which he had confessed guilt. The Assistant United States Attorney had arranged to have McFarland transferred from the D. C. Jail to a local jail in Rockville, Maryland, and in addition had helped McFarland's wife move from Southeast Washington to an apartment near the parochial school that McFarland's children were due to attend. 149 U. S. App. D. C. 1, 6 n. 7, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d 92</a></span>, 97 n. 7 (1972). The Assistant United States Attorney also testified that he "had indicated he would testify before the parole board in McFarland's behalf." <i>Id.,</i> at 6, 461 F. 2d, at 97.</p>
<p>[3]  Respondent does not contend that he was denied his Sixth Amendment right to counsel at the pre-indictment display of the black and white photographs. Tr. of Oral Arg. 21-22; Brief for Respondent 32 n. 21.</p>
<p>[4]  As the Court of Appeals noted, this testimony was of at least questionable credibility. See n. 2, <i>supra.</i></p>
<p>[5]  149 U. S. App. D. C., at 9, 461 F. 2d, at 100.</p>
<p>[6]  The Court of Appeals also noted "that there are at the very least strong elements of suggestiveness in this color photo confrontation," and that "it is hard to see how the Government can be held to have shown, by clear and convincing evidence, that these color photographs did not affect the in-court identification made one day later." <i>Id.,</i> at 7, 14 n. 20, 461 F. 2d, at 98, 105 n. 20.</p>
<p>[7]  The Court pointed out that "[i]mproper influences may go undetected by a suspect, guilty or not, who experiences the emotional tension which we might expect in one being confronted with potential accusers. Even when he does observe abuse, if he has a criminal record he may be reluctant to take the stand and open up the admission of prior convictions. Moreover, any protestations by the suspect of the fairness of the lineup made at trial are likely to be in vain; the jury's choice is between the accused's unsupported version and that of the police officers present." <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#230" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 230-231</a></span> (1967).</p>
<p>[8]  Thus, "[a] witness may have obtained only a brief glimpse of a criminal, or may have seen him under poor conditions. Even if the police subsequently follow the most correct photographic identification procedures . . . there is some danger that the witness may make an incorrect identification." <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#383" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 383</a></span> (1968).</p>
<p>[9]  See also Sobel, Assailing the Impermissible Suggestion: Evolving Limitations on the Abuse of Pre-Trial Criminal Identification Methods, 38 Brooklyn L. Rev. 261, 264, 296 (1971); Williams, Identification Parades, [1955] Crim. L. Rev. 525, 531; Comment, Photographic Identification: The Hidden Persuader, <span class="citation no-link">56 Iowa L. Rev. 408</span>, 419 (1970); Note, Pretrial Photographic IdentificationA "Critical Stage" of Criminal Proceedings?, <span class="citation no-link">21 Syracuse L. Rev. 1235</span>, 1241 (1970). Indeed, recognizing the superiority of corporeal to photographic identifications, English courts have long held that once the accused is in custody, pre-lineup photographic identification is "indefensible" and grounds for quashing the conviction. <i>Rex</i> v. <i>Haslam,</i> 19 Crim. App. Rep. 59, 60 (1925); <i>Rex</i> v. <i>Goss,</i> 17 Crim. App. Rep. 196, 197 (1923). See also P. Wall, Eye-Witness Identification in Criminal Cases 71 (1965).</p>
<p>[10]  See, <i>e. g.,</i> Comment, <i>supra,</i> n. 9, at 410-411; Note, Criminal ProcedurePhoto-Identification<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> Prospectivity Rule Invoked to Avoid Extension of Right to Counsel, 43 N. Y. U. L. Rev. 1019, 1021 (1968).</p>
<p>[11]  <i>Simmons</i> v. <i>United States, supra,</i> at 383.</p>
<p>[12]  The Court maintains that "the ethical responsibility of the prosecutor" is in itself a sufficient "safeguard" against impermissible suggestion at a photographic display. See <i>ante,</i> at 320. The same argument might, of course, be made with respect to lineups. Moreover, it is clear that the "prosecutor" is not always present at such pretrial displays. Indeed, in this very case, one of the four eyewitnesses was shown the color photographs on the morning of trial by an agent of the FBI, <i>not</i> in the presence of the "prosecutor." See 149 U. S. App. D. C., at 5, 461 F. 2d, at 96. And even though "the ethical responsibility of the prosecutor" might be an adequate "safeguard" against <i>intentional</i> suggestion, it can hardly be doubted that a "prosecutor" is, after all, only human. His behavior may be fraught with wholly <i>unintentional</i> and indeed unconscious nuances that might effectively suggest the "proper" response. See P. Wall, <i>supra,</i> n. 9, at 26-65; Napley, Problems of Effecting the Presentation of the Case for a Defendant, 66 Col. L. Rev. 94, 98-99 (1966); Williams &amp; Hammelmann, Identification Parades-I, [1963] Crim. L. Rev. 479, 483. See also <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#229" aria-description="Citation for case: United States v. Wade"><i>Wade,</i> supra, at 229, 235, 236</a></span>. And, of course, as <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> itself makes clear, unlike other forms of unintentional prosecutorial "manipulation," even unintentional suggestiveness at an identification procedure involves serious risks of "freezing" the witness' mistaken identification and creates almost insurmountable obstacles to reconstruction at trial.</p>
<p>[13]  See also P. Wall, <i>supra,</i> n. 9, at 68; Napley, <i>supra,</i> n. 12, at 98-99; Williams &amp; Hammelmann, <i>supra,</i> n. 12, at 484; Comment, <i>supra,</i> n. 9, at 411-413; Note, <i>supra,</i> n. 10, at 1023.</p>
<p>[14]  Brief for United States 24-25 in <i>United States</i> v. <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i><i>,</i> No. 334, O. T. 1966.</p>
<p>[15]  The Court's assertion, <i>ante,</i> at 317-319 and n. 10, that these difficulties of reconstruction are somehow minimized because the defense can "duplicate" a photographic identification reflects a complete misunderstanding of the issues in this case. Aside from the fact that lineups can also be "duplicated," the Court's assertion is wholly inconsistent with the underlying premises of both <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for cas

[...TRUNCATED 8784 of 128784 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/United States v. Bagley.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Bagley"
type: case
citation: "473 U.S. 667 (1985)"
parallel_cite: "105 S. Ct. 3375; 87 L. Ed. 2d 481; 53 U.S.L.W. 5084"
neutral_cite: 1985 U.S. LEXIS 130
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-07-02
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-07-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Bagley
  varies_by_point: false
  scope_note: "Good law; the controlling Brady/Giglio materiality standard."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111514/united-states-v-bagley/"
  cluster_id: 111514
  opinion_id: 9430189
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brady v. Maryland]]", "[[Giglio v. United States]]", "[[Kyles v. Whitley]]", "[[Strickler v. Greene]]", "[[Turner v. United States]]"]
aliases: []
tags: ["case", "due-process", "brady"]
holding: "Set the unified MATERIALITY standard for Brady (covering no-request, general-request, and specific-request cases) and confirmed…"
lake:
  record_id: United States v. Bagley
  status: verified
  projected_at: 2026-07-06
---

# United States v. Bagley

*473 U.S. 667 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Bagley was convicted of federal narcotics and firearms charges largely on the testimony of two government informants. Although the defense had specifically requested any deals or inducements, the government did not disclose that the informants had signed contracts promising payment contingent on their assistance. Bagley later discovered the arrangements and sought relief, arguing the suppressed impeachment evidence violated *[[Brady v. Maryland|Brady]]*.

## Issue
What standard of materiality governs a *[[Brady v. Maryland|Brady]]* claim, and whether a single materiality standard applies regardless of whether the defense made no request, a general request, or a specific request for the evidence.

## Rule
The Court adopted one unified materiality standard for all *[[Brady v. Maryland|Brady]]* claims, including suppressed impeachment evidence: "The evidence is material only if there is a reasonable probability that, had the evidence been disclosed to the defense, the result of the proceeding would have been different. A 'reasonable probability' is a probability sufficient to undermine confidence in the outcome." — 473 U.S. at 682. ^pin-682

Impeachment evidence, like [[Brady and Giglio|exculpatory]] evidence, falls within the *[[Brady v. Maryland|Brady]]* rule, and the same reasonable-probability test measures materiality whether or not the defense requested the evidence.

## Application
Because the undisclosed contingent-payment contracts bore on the credibility of the government's two key informant witnesses, they were favorable impeachment evidence within *[[Brady v. Maryland|Brady]]*'s reach. The proper question was therefore whether there was a reasonable probability that disclosure would have produced a different result — a determination the Court [[Reading and Citing Cases#on-remand|remanded]] for the lower courts to make under the newly clarified, single materiality standard rather than under any automatic-reversal or request-specific rule.

## Conclusion
A uniform reasonable-probability materiality standard governs *[[Brady v. Maryland|Brady]]* claims, and it reaches impeachment evidence; the case was [[Reading and Citing Cases#on-remand|remanded]] for application of that standard. Suppressed impeachment evidence is material only where its disclosure would create a reasonable probability of a different outcome.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Bagley* supplies the materiality standard for [[Brady v. Maryland]] and extends it to the impeachment evidence of [[Giglio v. United States]]; it was elaborated in [[Kyles v. Whitley]] (cumulative, whole-record review) and applied in [[Strickler v. Greene]] and [[Turner v. United States]].

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Bagley*, 473 U.S. 667 (1985) — https://www.courtlistener.com/opinion/111514/united-states-v-bagley/ — pinpoint: 682.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "36a6e744f52c76a1", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "473 U.S. 667 (1985)", "court": "U.S. Supreme Court", "neutral_cite": "1985 U.S. LEXIS 130", "official_citation_present": true, "parallel_cite": "105 S. Ct. 3375; 87 L. Ed. 2d 481; 53 U.S.L.W. 5084", "title": "United States v. Bagley", "year": "1985"}}
{"assertion_id": "4811bda7ad55c9f5", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Key — Progeny / Refinement", "title": "United States v. Bagley"}}
{"assertion_id": "77ec2d5f19e92d2d", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Set the unified MATERIALITY standard for Brady (covering no-request, general-request, and specific-request cases) and confirmed…", "title": "United States v. Bagley"}}
{"assertion_id": "64dd1b01f92fdee8", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Bagley"}}
{"assertion_id": "a6fe7c4eddcf129e", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1985-07-02", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Bagley", "field_i_validity": "good_law", "scope_note": "Good law; the controlling Brady/Giglio materiality standard.", "title": "United States v. Bagley", "varies_by_point": "false"}}
```

### lake record — United States v. Bagley

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Bagley",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Bagley",
    "case_name_short": "Bagley",
    "case_name_full": "United States v. Bagley",
    "input_case_name": "United States v. Bagley",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-07-02",
    "year": 1985,
    "docket": null,
    "cluster_id": 111514,
    "lead_opinion_id": 9430189,
    "sibling_ids": [
      111514,
      9430189,
      9430190,
      9430191,
      9430192
    ],
    "absolute_url": "/opinion/111514/united-states-v-bagley/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "473 U.S. 667",
      "volume": "473",
      "reporter": "U.S.",
      "page": "667",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 3375",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "3375",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 L. Ed. 2d 481",
        "volume": "87",
        "reporter": "L. Ed. 2d",
        "page": "481",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 5084",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "5084",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 130",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "130",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "473 U.S. 667",
        "volume": "473",
        "reporter": "U.S.",
        "page": "667",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 3375",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "3375",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 L. Ed. 2d 481",
        "volume": "87",
        "reporter": "L. Ed. 2d",
        "page": "481",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 130",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "130",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 5084",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "5084",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "473 U.S. 667",
    "official_selection": {
      "court_class": "scotus",
      "selected": "473 U.S. 667",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-682",
      "page": null,
      "quote": "--- # United States v. Bagley *473 U.S. 667 (1985)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Bagley was convicted of federal narcotics and firearms charges largely on the testimony of two government informants. Although the defense had specifically requested any deals or inducements, the government did not disclose that the informants had signed contracts promising payment contingent on their assistance. Bagley later discovered the arrangements and sought relief, arguing the suppressed impeachment evidence violated *Brady*. ## Issue What standard of materiality governs a *Brady* claim, and whether a single materiality standard applies regardless of whether the defense made no request, a general request, or a specific request for the evidence. ## Rule The Court adopted one unified materiality standard for all *Brady* claims, including suppressed impeachment evidence:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-07-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Bagley",
    "varies_by_point": false,
    "scope_note": "Good law; the controlling Brady/Giglio materiality standard.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Jevric",
          "cluster_id": 10873877,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fields",
          "cluster_id": 10309030,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane1_negative"
      },
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
        "journal_ref": "United States v. Bagley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hale",
          "cluster_id": 9435476,
          "cite": [
            "2023 Ohio 3894"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Schlup v. Delo",
          "cluster_id": 117893,
          "cite": [
            "130 L. Ed. 2d 808",
            "115 S. Ct. 851",
            "513 U.S. 298",
            "1995 U.S. LEXIS 701",
            "1995 WL 20524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray v. Carrier",
          "cluster_id": 111727,
          "cite": [
            "91 L. Ed. 2d 397",
            "106 S. Ct. 2639",
            "477 U.S. 478",
            "1986 U.S. LEXIS 66",
            "54 U.S.L.W. 4820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
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
        "journal_ref": "United States v. Bagley:lane2_top_cited"
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
        "journal_ref": "United States v. Bagley:lane2_top_cited"
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
        "journal_ref": "United States v. Bagley:lane2_top_cited"
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
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dominguez Benitez",
          "cluster_id": 136986,
          "cite": [
            "159 L. Ed. 2d 157",
            "124 S. Ct. 2333",
            "542 U.S. 74",
            "2004 U.S. LEXIS 4177",
            "17 Fla. L. Weekly Fed. S 379",
            "72 U.S.L.W. 4478"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Boyde v. California",
          "cluster_id": 112386,
          "cite": [
            "108 L. Ed. 2d 316",
            "110 S. Ct. 1190",
            "494 U.S. 370",
            "1990 U.S. LEXIS 1180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sawyer v. Whitley",
          "cluster_id": 112773,
          "cite": [
            "120 L. Ed. 2d 269",
            "112 S. Ct. 2514",
            "505 U.S. 333",
            "1992 U.S. LEXIS 3864"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McFarland v. State",
          "cluster_id": 2413967,
          "cite": [
            "928 S.W.2d 482",
            "1996 Tex. Crim. App. LEXIS 19",
            "1996 WL 71513"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
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
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wyatt v. State",
          "cluster_id": 1991912,
          "cite": [
            "23 S.W.3d 18",
            "2000 Tex. Crim. App. LEXIS 46",
            "2000 WL 526330"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
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
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Greer v. Miller",
          "cluster_id": 111956,
          "cite": [
            "97 L. Ed. 2d 618",
            "107 S. Ct. 3102",
            "483 U.S. 756",
            "1987 U.S. LEXIS 2930"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David C. Hughes, the Office of the Federal Public Defender, Amicus Supporting",
          "cluster_id": 789603,
          "cite": [
            "401 F.3d 540",
            "2005 WL 628224"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
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
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William George Bonin v. Arthur Calderon, as Warden of San Quentin State Prison James Rowland, Director of the California Department of Corrections",
          "cluster_id": 699264,
          "cite": [
            "59 F.3d 815",
            "95 Daily Journal DAR 8895",
            "95 Cal. Daily Op. Serv. 5256",
            "1995 U.S. App. LEXIS 16098"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cone v. Bell",
          "cluster_id": 145883,
          "cite": [
            "173 L. Ed. 2d 701",
            "129 S. Ct. 1769",
            "556 U.S. 449",
            "2009 U.S. LEXIS 3298"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McFarland v. State",
          "cluster_id": 2429802,
          "cite": [
            "845 S.W.2d 824",
            "1992 Tex. Crim. App. LEXIS 251",
            "1992 WL 438312"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Osband",
          "cluster_id": 5607850,
          "cite": [
            "13 Cal. 4th 622",
            "919 P.2d 640",
            "96 Daily Journal DAR 9137",
            "96 Cal. Daily Op. Serv. 5583",
            "55 Cal. Rptr. 2d 26",
            "1996 Cal. LEXIS 3814"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Thomas",
          "cluster_id": 2629208,
          "cite": [
            "83 P.3d 970"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Curry v. State",
          "cluster_id": 1638441,
          "cite": [
            "910 S.W.2d 490",
            "1995 Tex. Crim. App. LEXIS 119",
            "1995 WL 688920"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. LaMar",
          "cluster_id": 6890210,
          "cite": [
            "95 Ohio St. 3d 181",
            "767 N.E.2d 166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
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
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Clark",
          "cluster_id": 844247,
          "cite": [
            "52 Cal. 4th 856",
            "261 P.3d 243",
            "131 Cal. Rptr. 3d 225",
            "2011 Cal. LEXIS 8769"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Bagley:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111514 OR 9430189 OR 9430190 OR 9430191 OR 9430192) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjg2NjE0NDAwMDAwJnM9OTQwNjE4MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111514+OR+9430189+OR+9430190+OR+9430191+OR+9430192%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111514 OR 9430189 OR 9430190 OR 9430191 OR 9430192)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NDQmcz0xNjk5OTE2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111514+OR+9430189+OR+9430190+OR+9430191+OR+9430192%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111514 OR 9430189 OR 9430190 OR 9430191 OR 9430192)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjkwNzYxNjAwMDAwJnM9OTQyMDM1MSZ0PW8mZD0yMDI2LTA3LTA2JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111514+OR+9430189+OR+9430190+OR+9430191+OR+9430192%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 4,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111514 OR 9430189 OR 9430190 OR 9430191 OR 9430192)",
    "indexed_citing_opinions": 5258,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111514,
        "count": 4574,
        "count_source": "search"
      },
      {
        "opinion_id": 9430189,
        "count": 761,
        "count_source": "search"
      },
      {
        "opinion_id": 9430190,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430191,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430192,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 8547,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-bagley.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk1NDA0JnM9MTA2NzE2NjUmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28111514+OR+9430189+OR+9430190+OR+9430191+OR+9430192%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111514,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 102436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 103727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 106699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 107361,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 107610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 108589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 108613,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 108974,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 110797,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 110933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 111169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 111206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 111356,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 229184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 236467,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 260996,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 261122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 424868,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 426309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 430624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 439958,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111514,
        "cited_id": 1866817,
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
    "date_created": "2026-07-05T22:25:10Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:25:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:25:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:29:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:25:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Bagley

```
<opinion type="majority">
<author id="ASLC">Justice Blackmun</author>
<p id="AmL">announced the judgment of the Court and delivered an opinion of the Court except as to Part III.</p>
<p id="AgWy">In <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83, 87</a></span> (1963), this Court held that “the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or punishment.” The issue in the present case concerns the standard of materiality to be applied in determining whether a conviction should be reversed because the prosecutor failed to disclose requested evidence that could have been used to impeach Government witnesses.</p>
<p id="AcUM">I-H</p>
<p id="Ab3U">In October 1977, respondent Hughes Anderson Bagley was indicted in the Western District of Washington on 15 charges of violating federal-narcotics and firearms statutes. On November 18, 24 days before trial, respondent filed a discovery motion. The sixth paragraph of that motion requested:</p>
<blockquote id="AP8">“The names and addresses of witnesses that the government intends to call at trial. Also the prior criminal records of witnesses, and any deals, promises or induce<page-number citation-index="1" label="670">*670</page-number>ments made to witnesses in exchange for their testimony.” App. 18.<footnotemark>1</footnotemark></blockquote>
<p id="b708-4">The Government’s two principal witnesses at the trial were James F. O’Connor and Donald E. Mitchell. O’Connor and Mitchell were state law enforcement officers employed by the Milwaukee Railroad as private security guards. Between April and June 1977, they assisted the federal Bureau of Alcohol, Tobacco and Firearms (ATF) in conducting an undercover investigation of respondent.</p>
<p id="b708-5">The Government’s response to the discovery motion did not disclose that any “deals, promises or inducements” had been made to O’Connor or Mitchell. In apparent reply to a request in the motion’s ninth paragraph for “[c]opies of all Jencks Act material,”<footnotemark>2</footnotemark> the Government produced a series of affidavits that O’Connor and Mitchell had signed between April 12 and May 4, 1977, while the undercover investigation was in progress. These affidavits recounted in detail the undercover dealings that O’Connor and Mitchell were having at the time with respondent. Each affidavit concluded with the statement, “I made this statement freely and voluntarily without any threats or rewards, or promises of reward having been made to me in return for it.”<footnotemark>3</footnotemark></p>
<p id="b708-6">Respondent waived his right to a jury trial and was tried before the court in December 1977. At the trial, O’Connor <page-number citation-index="1" label="671">*671</page-number>and Mitchell testified about both the firearms and the narcotics charges. On December 23, the court found respondent guilty on the narcotics charges, but not guilty on the firearms charges.</p>
<p id="b709-5">In mid-1980, respondent filed requests for information pursuant to the Freedom of Information Act and to the Privacy Act of 1974, <span class="citation no-link">5 U. S. C. §§552</span> and 552a. He received in response copies of ATF form contracts that O’Connor and Mitchell had signed on May 3, 1977. Each form was entitled “Contract for Purchase of Information and Payment of Lump Sum Therefor.” The printed portion of the form stated that the vendor “will provide” information to ATF and that “upon receipt of such information by the Regional Director, Bureau of Alcohol, Tobacco and Firearms, or his representative, and upon the accomplishment of the objective sought to be obtained by the use of such information to the satisfaction of said Regional Director, the United States will pay to said vendor a sum commensurate with services and information rendered.” App. 22 and 23. Each form contained the following typewritten description of services:</p>
<blockquote id="b709-6">“That he will provide information regarding T-I and other violations committed by Hughes A. Bagley, Jr.; that he will purchase evidence for ATF; that he will cut <em>[sic] </em>in an undercover capacity for ATF; that he will assist ATF in gathering of evidence and testify against the violator in federal court.” <em><span class="citation no-link">Ibid.</span></em></blockquote>
<p id="b709-7">The figure “$300.00” was handwritten in each form on a line entitled “Sum to Be Paid to Vendor.”</p>
<p id="b709-8">Because these contracts had not been disclosed to respondent in response to his pretrial discovery motion,<footnotemark>4</footnotemark> respondent moved under <span class="citation no-link">28 U. S. C. § 2255</span> to vacate his sentence. He <page-number citation-index="1" label="672">*672</page-number>alleged that the Government’s failure to disclose the contracts, which he could have used to impeach O’Connor and Mitchell, violated his right to due process under <em>Brady </em>v. <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Maryland, supra.</a></span></em></p>
<p id="b710-5">The motion came before the same District Judge who had presided at respondent’s bench trial. An evidentiary hearing was held before a Magistrate. The Magistrate found that the printed form contracts were blank when O’Connor and Mitchell signed them and were not signed by an ATF representative until after the trial. He also found that on January 4, 1978, following the trial and decision in respondent’s case, ATF made payments of $300 to both O’Connor and Mitchell pursuant to the contracts.<footnotemark>5</footnotemark> Although the ATF case agent who dealt with O’Connor and Mitchell testified that these payments were compensation for expenses, the Magistrate found that this characterization was not borne out by the record. There was no documentation for expenses in these amounts; Mitchell testified that his payment was not for expenses, and the ATF forms authorizing the payments treated them as rewards.</p>
<p id="b710-6">The District Court adopted each of the Magistrate’s findings except for the last one to the effect that “[n]either O’Connor nor Mitchell expected to receive the payment of $300 or any payment from the United States for their testimony.” App. to Pet. for Cert. 7a, 12a, 14a. Instead, the court found that it was “probable” that O’Connor and Mitchell expected to receive compensation, in addition to their expenses, for their assistance, “though perhaps not for their testimony.” <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Id.,</a></span> </em>at 7a. The District Court also expressly rejected, <em>ibid., </em>the Magistrate’s conclusion, <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">id.,</a></span> </em>at 14a, that:</p>
<blockquote id="b711-4"><page-number citation-index="1" label="673">*673</page-number>“Because neither witness was promised or expected payment for his testimony, the United States did not withhold, during pretrial discovery, information as to any ‘deals, promises or inducements’ to these witnesses. Nor did the United States suppress evidence favorable to the defendant, in violation of <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963).”</blockquote>
<p id="b711-5">The District Court found beyond a reasonable doubt, however, that had the existence of the agreements been disclosed to it during trial, the disclosure would have had no effect upon its finding that the Government had proved beyond a reasonable doubt that respondent was guilty of the offenses for which he had been convicted. <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Id.,</a></span> at 8a. The District Court reasoned: Almost all of the testimony of both witnesses was devoted to the firearms charges in the indictment. Respondent, however, was acquitted on those charges. The testimony of O’Connor and Mitchell concerning the narcotics charges was relatively very brief. On cross-examination, respondent’s counsel did not seek to discredit their testimony as to the facts of distribution but rather sought to show that the controlled substances in question came from supplies that had been prescribed for respondent’s personal use. The answers of O’Connor and Mitchell to this line of cross-examination tended to be favorable to respondent. Thus, the claimed impeachment evidence would not have been helpful to respondent and would not have affected the outcome of the trial. Accordingly, the District Court denied respondent’s motion to vacate his sentence.</p>
<p id="b711-6">The United States Court of Appeals for the Ninth Circuit reversed. <em>Bagley </em>v. <em>Lumpkin, </em><span class="citation" data-id="426309"><a href="/opinion/426309/hughes-anderson-bagley-v-walter-t-lumpkin-warden/" aria-description="Citation for case: Hughes Anderson Bagley v. Walter T. Lumpkin, Warden">719 F. 2d 1462</a></span> (1983). The Court of Appeals began by noting that, according to precedent in the Circuit, prosecutorial failure to respond to a specific <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>request is properly analyzed as error, and a resulting conviction must be reversed unless the error is harmless beyond a reasonable doubt. The court noted that the District Judge who had presided over the bench trial <page-number citation-index="1" label="674">*674</page-number>concluded beyond a reasonable doubt that disclosure of the ATF agreement would not have affected the outcome. The Court of Appeals, however, stated that it “disagree[d]” with this conclusion. <em>Id., </em>at 1464. In particular, it disagreed with the Government’s — and the District Court’s — premise that the testimony of O’Connor and Mitchell was exculpatory on the narcotics charges, and that respondent therefore would not have sought to impeach “his own witness.” <em>Id., </em>at 1464, n. 1.</p>
<p id="b712-5">The Court of Appeals apparently based its reversal, however, on the theory that the Government’s failure to disclose the requested <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>information that respondent could have used to conduct an effective cross-examination impaired respondent’s right to confront adverse witnesses. The court noted: “In <em>Davis </em>v. <em>Alaska, . . . </em>the Supreme Court held that the denial of the ‘right of <em>effective </em>cross-examination’ was ‘ “constitutional error of the first magnitude” ’ requiring automatic reversal.” <span class="citation" data-id="426309"><a href="/opinion/426309/hughes-anderson-bagley-v-walter-t-lumpkin-warden/" aria-description="Citation for case: Hughes Anderson Bagley v. Walter T. Lumpkin, Warden">719 F. 2d, at 1464</a></span> (quoting <em>Davis </em>v. <em>Alaska, </em><span class="citation" data-id="9425616"><a href="/opinion/108974/davis-v-alaska/#318" aria-description="Citation for case: Davis v. Alaska">415 U. S. 308, 318</a></span> (1974)) (emphasis added by Court of Appeals). In the last sentence of its opinion, the Court of Appeals concluded: “we hold that the government’s failure to provide requested <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>information to Bagley so that he could effectively cross-examine two important government witnesses requires an automatic reversal.” <span class="citation" data-id="426309"><a href="/opinion/426309/hughes-anderson-bagley-v-walter-t-lumpkin-warden/#1464" aria-description="Citation for case: Hughes Anderson Bagley v. Walter T. Lumpkin, Warden">719 F. 2d, at 1464</a></span>.</p>
<p id="b712-6">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./469/1016/">469 U. S. 1016</a></span> (1984), and we now reverse.</p>
<p id="b712-7">II</p>
<p id="b712-8">The holding in <em>Brady </em>v. <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Maryland</a></span> </em>requires disclosure only of evidence that is both favorable to the accused and “material either to guilt or to punishment.” <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>. See also <em>Moore </em>v. <em>Illinois, </em><span class="citation" data-id="9425027"><a href="/opinion/108613/moore-v-illinois/#794" aria-description="Citation for case: Moore v. Illinois">408 U. S. 786, 794-795</a></span> (1972). The Court explained in <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#104" aria-description="Citation for case: United States v. Agurs">427 U. S. 97, 104</a></span> (1976): “A fair analysis of the holding in <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>indicates that implicit in the requirement of materiality is a concern that the suppressed evidence might have affected the outcome of <page-number citation-index="1" label="675">*675</page-number>the trial.” The evidence suppressed in <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>would have been admissible only on the issue of punishment and not on the issue of guilt, and therefore could have affected only Brady’s sentence and not his conviction. Accordingly, the Court affirmed the lower court’s restriction of Brady’s new trial to the issue of punishment.</p>
<p id="b713-5">The <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>rule is based on the requirement of due process. Its purpose is not to displace the adversary system as the primary means by which truth is uncovered, but to ensure that a miscarriage of justice does not occur.<footnotemark>6</footnotemark> Thus, the prosecutor is not required to deliver his entire file to defense counsel,<footnotemark>7</footnotemark> but only to disclose evidence favorable to the accused that, if suppressed, would deprive the defendant of a fair trial:</p>
<blockquote id="b713-6">“For unless the omission deprived the defendant of a fair trial, there was no constitutional violation requiring that the verdict be set aside; and absent a constitutional violation, there was no breach of the prosecutor’s constitutional duty to disclose. . . .</blockquote>
<blockquote id="b713-7">“. . . But to reiterate a critical point, the prosecutor will not have violated his constitutional duty of disclo<page-number citation-index="1" label="676">*676</page-number>sure unless his omission is of sufficient significance to result in the denial of the defendant’s right to a fair trial.” <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#108" aria-description="Citation for case: United States v. Agurs">427 U. S., at 108</a></span>.</blockquote>
<p id="b714-4">In <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>and <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span>, </em>the prosecutor failed to disclose exculpatory evidence. In the present case, the prosecutor failed to disclose evidence that the defense might have used to impeach the Government’s witnesses by showing bias or interest. Impeachment evidence, however, as well as exculpatory evidence, falls within the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>rule. See <em>Giglio </em>v. <em>United States, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 154</a></span> (1972). Such evidence is “evidence favorable to an accused,” <em>Brady, </em>873 U. S., at 87, so that, if disclosed and used effectively, it may make the difference between conviction and acquittal. Cf. <em>Napue </em>v. <em>Illinois, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264, 269</a></span> (1959) (“The jury’s estimate of the truthfulness and reliability of a given witness may well be determinative of guilt or innocence, and it is upon such subtle factors as the possible interest of the witness in testifying falsely that a defendant’s life or liberty may depend”).</p>
<p id="b714-5">The Court of Appeals treated impeachment evidence as constitutionally different from exculpatory evidence. According to that court, failure to disclose impeachment evidence is “even more egregious” than failure to disclose exculpatory evidence “because it threatens the defendant’s right to confront adverse witnesses.” <span class="citation" data-id="426309"><a href="/opinion/426309/hughes-anderson-bagley-v-walter-t-lumpkin-warden/#1464" aria-description="Citation for case: Hughes Anderson Bagley v. Walter T. Lumpkin, Warden">719 F. 2d, at 1464</a></span>. Relying on <em>Davis </em>v. <em>Alaska, </em><span class="citation" data-id="9425616"><a href="/opinion/108974/davis-v-alaska/" aria-description="Citation for case: Davis v. Alaska">415 U. S. 308</a></span> (1974), the Court of Appeals held that the Government’s failure to disclose requested impeachment evidence that the defense could use to conduct an effective cross-examination of important prosecution witnesses constitutues “‘constitutional error of the first magnitude’” requiring automatic reversal. <span class="citation" data-id="426309"><a href="/opinion/426309/hughes-anderson-bagley-v-walter-t-lumpkin-warden/" aria-description="Citation for case: Hughes Anderson Bagley v. Walter T. Lumpkin, Warden">719 F. 2d, at 1464</a></span> (quoting <em>Davis </em>v. <span class="citation" data-id="9425616"><a href="/opinion/108974/davis-v-alaska/#318" aria-description="Citation for case: Davis v. Alaska"><em>Alaska, supra, </em>at 318</a></span>).</p>
<p id="b714-6">This Court has rejected any such distinction between impeachment evidence and exculpatory evidence. In <em>Giglio </em>v. <em>United States, supra, </em>the Government failed to disclose impeachment evidence similar to the evidence at issue in the present case, that is, a promise made to the key Government <page-number citation-index="1" label="677">*677</page-number>witness that he would not be prosecuted if he testified for the Government. This Court said:</p>
<blockquote id="b715-5">“When the ‘reliability of a given -witness may well be determinative of guilt or innocence/ nondisclosure of evidence affecting credibility falls -within th[e] general rule [of <em>Brady]. </em>We do not, however, automatically require a new trial whenever ‘a combing of the prosecutors’ files after the trial has disclosed evidence possibly useful to the defense but not likely to have changed the verdict . . . A finding of materiality of the evidence is required under <em>Brady. ... A </em>new trial is required if ‘the false testimony could ... in any reasonable likelihood have affected the judgment of the jury . . . <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States">405 U. S., at 154</a></span> (citations omitted).</blockquote>
<p id="b715-7">Thus, the Court of Appeals’ holding is inconsistent with our precedents.</p>
<p id="b715-8">Moreover, the court’s reliance on <em>Davis </em>v. <em><span class="citation" data-id="9425616"><a href="/opinion/108974/davis-v-alaska/" aria-description="Citation for case: Davis v. Alaska">Alaska</a></span> </em>for its “automatic reversal” rule is misplaced. In <em><span class="citation" data-id="9425616"><a href="/opinion/108974/davis-v-alaska/" aria-description="Citation for case: Davis v. Alaska">Davis</a></span>, </em>the defense sought to cross-examine a crucial prosecution witness concerning his probationary status as a juvenile delinquent. The defense intended by this cross-examination to show that the witness might have made a faulty identification of the defendant in order to shift suspicion away from himself or because he feared that his probationary status would be jeopardized if he did not satisfactorily assist the police and prosecutor in obtaining a conviction. Pursuant to a state rule of procedure and a state statute making juvenile adjudications inadmissible, the trial judge prohibited the defense from conducting the cross-examination. This Court reversed the defendant’s conviction, ruling that the direct restriction on the scope of cross-examination denied the defendant “the right of effective cross-examination which “‘would be constitutional error of the first magnitude and no amount of showing of want of prejudice would cure it.” <em>Brookhart </em>v. <em>Janis, </em><span class="citation" data-id="107209"><a href="/opinion/107209/brookhart-v-janis/#3" aria-description="Citation for case: Brookhart v. Janis">384 U. S. 1, 3</a></span>.’” <span class="citation" data-id="9425616"><a href="/opinion/108974/davis-v-alaska/" aria-description="Citation for case: Davis v. Alaska">415 U. S., at 318</a></span> (quoting <em>Smith </em><page-number citation-index="1" label="678">*678</page-number>v. <em>Illinois, </em><span class="citation" data-id="9423611"><a href="/opinion/107610/smith-v-illinois/#131" aria-description="Citation for case: Smith v. Illinois">390 U. S. 129, 131</a></span> (1968)). See also <em>United States </em>v. <em>Cronic, </em><span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/#659" aria-description="Citation for case: United States v. Cronic">466 U. S. 648, 659</a></span> (1984).</p>
<p id="b716-5">The present case, in contrast, does not involve any direct restriction on the scope of cross-examination. The defense was free to cross-examine the witnesses on any relevant subject, including possible bias or interest resulting from inducements made by the Government. The constitutional error, if any, in this case was the Government’s failure to assist the defense by disclosing information that might have been helpful in conducting the cross-examination. As discussed above, such suppression of evidence amounts to a constitutional violation only if it deprives the defendant of a fair trial. Consistent with “our overriding concern with the justice of the finding of guilt,” <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#112" aria-description="Citation for case: United States v. Agurs">427 U. S., at 112</a></span>, a constitutional error occurs, and the conviction must be reversed, only if the evidence is material in the sense that its suppression undermines confidence in the outcome of the trial.</p>
<p id="b716-6">Ill</p>
<p id="b716-7">A</p>
<p id="b716-8">It remains to determine the standard of materiality applicable to the nondisclosed evidence at issue in this case. Our starting point is the framework for evaluating the materiality of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>evidence established in <em>United States </em>v. <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span>. </em>The Court in <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>distinguished three situations involving the discovery, after trial, of information favorable to the accused that had been known to the prosecution but unknown to the defense. The first situation was the prosecutor’s knowing use of perjured testimony or, equivalently, the prosecutor’s knowing failure to disclose that testimony used to convict the defendant was false. The Court noted the well-established rule that “a conviction obtained by the knowing use of perjured testimony is fundamentally unfair, and must be set aside if there is any reasonable likelihood that the false testimony could have affected the judgment of the jury.” <page-number citation-index="1" label="679">*679</page-number><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#103" aria-description="Citation for case: United States v. Agurs">427 U. S., at 103</a></span> (footnote omitted).<footnotemark>8</footnotemark> Although this rule is stated in terms that treat the knowing use of perjured testimony as error subject to harmless-error review,<footnotemark>9</footnotemark> it may as <page-number citation-index="1" label="680">*680</page-number>easily be stated as a materiality standard under which the fact that testimony is perjured is considered material unless failure to disclose it would be harmless beyond a reasonable doubt. The Court in <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>justified this standard of materiality on the ground that the knowing use of perjured testimony involves prosecutorial misconduct and, more importantly, involves “a corruption of the truth-seeking function of the trial process.” <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#104" aria-description="Citation for case: United States v. Agurs"><em>Id., </em>at 104</a></span>.</p>
<p id="b718-5">At the other extreme is the situation in <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>itself, where the defendant does not make a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>request and the prosecutor fails to disclose certain evidence favorable to the accused. The Court rejected a harmless-error rule in that situation, because under that rule every nondisclosure is treated as error, thus imposing on the prosecutor a constitutional duty to deliver his entire file to defense counsel.<footnotemark>10</footnotemark> <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#111" aria-description="Citation for case: United States v. Agurs">427 U. S., at 111-112</a></span>. At the same time, the Court rejected a standard that would require the defendant to demonstrate that the evidence if disclosed probably would have resulted in acquittal. <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#111" aria-description="Citation for case: United States v. Agurs"><em>Id., </em>at 111</a></span>. The Court reasoned: “If the standard applied to the usual motion for a new trial based on newly discovered evidence were the same when the evidence was in the State’s possession as when it was found in a neutral source, there would be no special significance to the prosecutor’s obligation to serve the cause of justice.” <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Ibid.</a></span> </em>The <page-number citation-index="1" label="681">*681</page-number>standard of materiality applicable in the absence of a specific <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>request is therefore stricter than the harmless-error standard but more lenient to the defense than the newly-discovered-evidence standard.</p>
<p id="b719-5">The third situation identified by the Court in <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>is where the defense makes a specific request and the prosecutor fails to disclose responsive evidence.<footnotemark>11</footnotemark> The Court did not define the standard of materiality applicable in this situation,<footnotemark>12</footnotemark> but suggested that the standard might be more lenient to the defense than in the situation in which the defense makes no request or only a general request. <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#106" aria-description="Citation for case: United States v. Agurs">427 U. S., at 106</a></span>. The Court also noted: “When the prosecutor receives a specific and relevant request, the failure to make any response is seldom, if ever, excusable.” <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Ibid.</a></span></em></p>
<p id="b719-6">The Court has relied on and reformulated the <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>standard for the materiality of undisclosed evidence in two subsequent cases arising outside the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>context. In neither case did the Court’s discussion of the <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>standard distinguish among the three situations described in <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span>. </em>In <em>United States </em>v. <em>Valenzuela-Bernal, </em><span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/#874" aria-description="Citation for case: United States v. Valenzuela-Bernal">458 U. S. 858, 874</a></span> (1982), the Court held that due process is violated when testimony is made unavailable to the defense by Government deportation of witnesses “only if there is a reasonable likelihood that the testimony could have affected the judgment of the <page-number citation-index="1" label="682">*682</page-number>trier of fact.” And in <em>Strickland </em>v. <em>Washington, </em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">466 U. S. 668</a></span> (1984), the Court held that a new trial must be granted when evidence is not introduced because of the incompetence of counsel only if “there is a reasonable probability that, but for counsel’s unprofessional errors, the result of the proceeding would have been different.” <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#694" aria-description="Citation for case: Strickland v. Washington"><em>Id., </em>at 694</a></span>.<footnotemark>13</footnotemark> The <em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Strickland</a></span> </em>Court defined a “reasonable probability” as “a probability sufficient to undermine confidence in the outcome.” <em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Ibid.</a></span></em></p>
<p id="b720-5">We find the <em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Strickland</a></span> </em>formulation of the <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>test for materiality sufficiently flexible to cover the “no request,” “general request,” and “specific request” cases of prosecu-torial failure to disclose evidence favorable to the accused: The evidence is material only if there is a reasonable probability that, had the evidence been disclosed to the defense, the result of the proceeding would have been different. A “reasonable probability” is a probability sufficient to undermine confidence in the outcome.</p>
<p id="b720-6">The Government suggests that a materiality standard more favorable to the defendant reasonably might be adopted in specific request cases. See Brief for United States 31. The Government notes that an incomplete response to a specific request not only deprives the defense of certain evidence, but also has the effect of representing to the defense that the evidence does not exist. In reliance on this misleading representation, the defense might abandon lines of independent investigation, defenses, or trial strategies that it otherwise would have pursued. <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Ibid.</a></span></em></p>
<p id="b720-7">We agree that the prosecutor’s failure to respond fully to a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>request may impair the adversary process in this manner. And the more specifically the defense requests certain evidence, thus putting the prosecutor on notice of its value, the more reasonable it is for the defense to assume from the <page-number citation-index="1" label="683">*683</page-number>nondisclosure that the evidence does not exist, and to make pretrial and trial decisions on the basis of this assumption. This possibility of impairment does not necessitate a different standard of materiality, however, for under the <em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Strickland</a></span> </em>formulation the reviewing court may consider directly any adverse effect that the prosecutor’s failure to respond might have had on the preparation or presentation of the defendant’s case. The reviewing court should assess the possibility that such effect might have occurred in light of the totality of the circumstances and with an awareness of the difficulty of reconstructing in a post-trial proceeding the course that the defense and the trial would have taken had the defense not been misled by the prosecutor’s incomplete response.</p>
<p id="b721-5">B</p>
<p id="b721-6">In the present case, we think that there is a significant likelihood that the prosecutor’s response to respondent’s discovery motion misleadingly induced defense counsel to believe that O’Connor and Mitchell could not be impeached on the basis of bias or interest arising from inducements offered by the Government. Defense counsel asked the prosecutor to disclose any inducements that had been made to witnesses, and the prosecutor failed to disclose that the possibility of a reward had been held out to O’Connor and Mitchell if the information they supplied led to “the accomplishment of the objective sought to be obtained ... to the satisfaction of [the Government].” App. 22 and 23. This possibility of a reward gave O’Connor and Mitchell a direct, personal stake in respondent’s conviction. The fact that the stake was not guaranteed through a promise or binding contract, but was expressly contingent on the Government’s satisfaction with the end result, served only to strengthen any incentive to testify falsely in order to secure a conviction. Moreover, the prosecutor disclosed affidavits that stated that O’Connor and Mitchell received no promises of reward in return for providing information in the affidavits implicating respondent in <page-number citation-index="1" label="684">*684</page-number>criminal activity. In fact, O’Connor and Mitchell signed the last of these affidavits the very day after they signed the ATF contracts. While the Government is technically correct that the blank contracts did not constitute a “promise of reward,” the natural effect of these affidavits would be misleadingly to induce defense counsel to believe that O’Connor and Mitchell provided the information in the affidavits, and ultimately their testimony at trial recounting the same information, without any “inducements.”</p>
<p id="b722-5">The District Court, nonetheless, found beyond a reasonable doubt that, had the information that the Government held out the possibility of reward to its witnesses been disclosed, the result of the criminal prosecution would not have been different. If this finding were sustained by the Court of Appeals, the information would be immaterial even under the standard of materiality applicable to the prosecutor’s knowing use of perjured testimony. Although the express holding of the Court of Appeals was that the nondisclosure in this case required automatic reversal, the Court of Appeals also stated that it “disagreed” with the District Court’s finding of harmless error. In particular, the Court of Appeals appears to have disagreed with the factual premise on which this finding expressly was based. The District Court reasoned that O’Connor’s and Mitchell’s testimony was exculpatory on the narcotics charges. The Court of Appeals, however, concluded, after reviewing the record, that O’Connor’s and Mitchell’s testimony was in fact inculpatory on those charges. <span class="citation" data-id="426309"><a href="/opinion/426309/hughes-anderson-bagley-v-walter-t-lumpkin-warden/#1464" aria-description="Citation for case: Hughes Anderson Bagley v. Walter T. Lumpkin, Warden">719 F. 2d, at 1464, n. 1</a></span>. Accordingly, we reverse the judgment of the Court of Appeals and remand the case to that court for a determination whether there is a reasonable probability that, had the inducement offered by the Government to O’Connor and Mitchell been disclosed to the defense, the result of the trial would have been different.</p>
<p id="b722-6">
<em>It is so ordered.</em>
</p>
<p id="b722-7">Justice Powell took no part in the decision of this case.</p>
<footnote label="1">
<p id="b708-7"> In addition, ¶ 10(b) of the motion requested “[p]romises or representations made to any persons the government intends to call as witnesses at trial, including but not limited to promises of no prosecution, immunity, lesser sentence, etc.,” and ¶11 requested “[a]ll information which would establish the reliability of the Milwaukee Railroad Employees in this case, whose testimony formed the basis for the search warrant.” App. 18-19.</p>
</footnote>
<footnote label="2">
<p id="b708-8"> The Jencks Act, <span class="citation no-link">18 U. S. C. § 3600</span>, requires the prosecutor to disclose, after direct examination of a Government witness and on the defendant’s motion, any statement of the witness in the Government’s possession that relates to the subject matter of the witness’ testimony.</p>
</footnote>
<footnote label="3">
<p id="b708-9"> Brief for United States 3, quoting Memorandum of Points and Authorities in Support of Pet. for Habeas Corpus, CV80-3592-RJK(M) (CD Cal.) Exhibits 1-9.</p>
</footnote>
<footnote label="4">
<p id="b709-9"> The Assistant United States Attorney who prosecuted respondent stated in stipulated testimony that he had not known that the contracts existed and that he would have furnished them to respondent had he known of them. See App. to Pet. for Cert. 13a.</p>
</footnote>
<footnote label="5">
<p id="b710-7"> The Magistrate found, too, that ATF paid O’Connor and Mitchell, respectively, $90 and $80 in April and May 1977 before trial, but concluded that these payments were intended to reimburse O’Connor and Mitchell for expenses, and would not have provided a basis for impeaching O’Connor’s and Mitchell’s trial testimony. The District Court adopted this finding and conclusion. <em><span class="citation no-link">Id.,</span> </em>at 7a, 13a.</p>
</footnote>
<footnote label="6">
<p id="b713-8"> By requiring the prosecutor to assist the defense in making its ease, the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>rule represents a limited departure from a pure adversary model. The Court has recognized, however, that the prosecutor’s role transcends that of an adversary: he “is the representative not of an ordinary party to a controversy, but of a sovereignty . . . whose interest ... in a criminal prosecution is not that it shall win a case, but that justice shall be done.” <em>Berger </em>v. <em>United States, </em><span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/#88" aria-description="Citation for case: Berger v. United States">295 U. S. 78, 88</a></span> (1935). See <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87-88</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b713-9"> See <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#106" aria-description="Citation for case: United States v. Agurs">427 U. S. 97, 106, 111</a></span> (1976); <em>Moore </em>v. <em>Illinois, </em><span class="citation" data-id="9425027"><a href="/opinion/108613/moore-v-illinois/#795" aria-description="Citation for case: Moore v. Illinois">408 U. S. 786, 795</a></span> (1972). See also <em>California </em>v. <em>Trombetta, </em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/#488" aria-description="Citation for case: California v. Trombetta">467 U. S. 479, 488, n. 8</a></span> (1984). An interpretation of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>to create a broad, constitutionally required right of discovery “would entirely alter the character and balance of our present systems of criminal justice.” <em>Giles </em>v. <em>Maryland, </em><span class="citation" data-id="9423353"><a href="/opinion/107361/giles-v-maryland/#117" aria-description="Citation for case: Giles v. Maryland">386 U. S. 66, 117</a></span> (1967) (dissenting opinion). Furthermore, a rule that the prosecutor commits error by any failure to disclose evidence favorable to the accused, no matter how insignificant, would impose an impossible burden on the prosecutor and would undermine the interest in the finality of judgments.</p>
</footnote>
<footnote label="8">
<p id="b717-5"> In fact, the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>rule has its roots in a series of eases dealing with convictions based on the prosecution’s knowing use of perjured testimony. In <em>Mooney </em>v. <em>Holohan, </em><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103</a></span> (1935), the Court established the rule that the knowing use by a state prosecutor of perjured testimony to obtain a conviction and the deliberate suppression of evidence that would have impeached and refuted the testimony constitutes a denial of due process. The Court reasoned that “a deliberate deception of court and jury by the presentation of testimony known to be perjured” is inconsistent with “the rudimentary demands of justice.” <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#112" aria-description="Citation for case: Mooney v. Holohan"><em>Id., </em>at 112</a></span>. The Court reaffirmed this principle in broader terms in <em>Pyle </em>v. <em>Kansas, </em><span class="citation" data-id="103727"><a href="/opinion/103727/pyle-v-kansas/" aria-description="Citation for case: Pyle v. Kansas">317 U. S. 213</a></span> (1942), where it held that allegations that the prosecutor had deliberately suppressed evidence favorable to the accused and had knowingly used perjured testimony were sufficient to charge a due process violation.</p>
<p id="b717-6">The Court again reaffirmed this principle in <em>Napue </em>v. <em>Illinois, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264</a></span> (1959). In <em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">Napue</a></span>, </em>the principal witness for the prosecution falsely testified that he had been promised no consideration for his testimony. The Court held that the knowing use of false testimony to obtain a conviction violates due process regardless of whether the prosecutor solicited the false testimony or merely allowed it to go uncorrected when it appeared. The Court explained that the principle that a State may not knowingly use false testimony to obtain a conviction — even false testimony that goes only to the credibility of the witness — is “implicit in any concept of ordered liberty.” <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois"><em>Id., </em>at 269</a></span>. Finally, the Court held that it was not bound by the state court’s determination that the false testimony “could not in any reasonable likelihood have affected the judgment of the jury.” <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#271" aria-description="Citation for case: Napue v. Illinois"><em>Id., </em>at 271</a></span>. The Court conducted its own independent examination of the record and concluded that the false testimony “may have had an effect on the outcome of the trial.” <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#272" aria-description="Citation for case: Napue v. Illinois"><em>Id., </em>at 272</a></span>. Accordingly, the Court reversed the judgment of conviction.</p>
</footnote>
<footnote label="9">
<p id="b717-7"> The rule that a conviction obtained by the knowing use of perjured testimony must be set aside if there is any reasonable likelihood that the false testimony could have affected the jury’s verdict derives from <em>Napue </em>v. <em>Illinois, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#271" aria-description="Citation for case: Napue v. Illinois">360 U. S., at 271</a></span>. See n. 8, <em>supra. </em>See also <em>Giglio </em>v. <em>United States, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 154</a></span> (1972) (quoting <em>Napue, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#271" aria-description="Citation for case: Napue v. Illinois">360 U. S., at 271</a></span>). <em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">Napue</a></span> </em>antedated <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967), where the “harmless beyond a reasonable doubt” standard was established. The Court in <em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span> </em>noted that there was little, if any, difference between <page-number citation-index="1" label="680">*680</page-number>a rule formulated, as in <em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">Napue</a></span>, </em>in terms of “ ‘whether there is a reasonable possibility that the evidence complained of might have contributed to the conviction,’ ” and a rule “ ‘requiring the beneficiary of a constitutional error to prove beyond a reasonable doubt that the error complained of did not contribute to the verdict obtained.’” 386 U. S., at 24 (quoting <em>Fahy </em>v. <em>Connecticut, </em><span class="citation" data-id="9422676"><a href="/opinion/106699/fahy-v-connecticut/#86" aria-description="Citation for case: Fahy v. Connecticut">375 U. S. 85, 86-87</a></span> (1963)). It is therefore clear, as indeed the Government concedes, see Brief for United States 20, and 36-38, that this Court’s precedents indicate that the standard of review applicable to the knowing use of perjured testimony is equivalent to the <em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span> </em>harmless-error standard.</p>
</footnote>
<footnote label="10">
<p id="b718-7"> This is true only if the nondisclosure is treated as error subject to harmless-error review, and not if the nondisclosure is treated as error only if the evidence is material under a not “harmless beyond a reasonable doubt” standard.</p>
</footnote>
<footnote label="11">
<p id="b719-7"> The Court in <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>identified <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>as a case in which specific information was requested by the defense. <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#106" aria-description="Citation for case: United States v. Agurs">427 U. S., at 106</a></span>. The request in <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>was for the extrajudicial statements of Brady’s accomplice. See <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#84" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 84</a></span>.</p>
</footnote>
<footnote label="12">
<p id="b719-8"> The Court in <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>noted: “A fair analysis of the holding in <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>indicates that implicit in the requirement of materiality is a concern that the suppressed evidence might have affected the outcome of the trial.” <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#104" aria-description="Citation for case: United States v. Agurs">427 U. S., at 104</a></span>. Since the <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>Court identified <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>as a “specific request” case, see n. 11, <em>supra, </em>this language might be taken as indicating the standard of materiality applicable in such a case. It is clear, however, that the language merely explains the meaning of the term “materiality.” It does not establish a standard of materiality because it does not indicate what quantum of likelihood there must be that the undisclosed evidence would have affected the outcome.</p>
</footnote>
<footnote label="13">
<p id="b720-8"> In particular, the Court explained in <em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Strickland</a></span>: </em>“When a defendant challenges a conviction, the question is whether there is a reasonable probability that, absent the errors, the factfinder would have had a reasonable doubt respecting guilt.” 466 U. S., at 695.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Banks.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Banks"
type: case
citation: "540 U.S. 31 (2003)"
parallel_cite: "124 S. Ct. 521; 157 L. Ed. 2d 343"
neutral_cite: 2003 U.S. LEXIS 8966
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2003
date_decided: 2003-12-02
docket: 02-473
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2003-12-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Banks
  varies_by_point: false
  scope_note: "Controlling: in a felony drug case, a 15–20-second wait after knock-and-announce before forcible entry is reasonable where the exigency is imminent destruction of easily disposable evidence; reasonableness turns on the time to dispose of evidence, not travel time to the door."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/131146/united-states-v-banks/"
  cluster_id: 131146
  opinion_id: 131146
  identity_checked: true
homes:
  - page: "[[Knock-and-Announce]]"
    role: "Progeny"
related: ["[[United States v. Ramirez]]", "[[Richards v. Wisconsin]]", "[[Wilson v. Arkansas]]"]
aliases: []
tags: ["case", "fourth-amendment", "knock-and-announce", "warrant-execution", "exigent-circumstances"]
holding: "A 15–20-second wait after knocking and announcing before forcing entry to execute a felony drug warrant is reasonable: when the exigency is the imminent destruction of easily disposable evidence, the relevant time is how long disposal would take, not how long the occupant needs to reach the door."
lake:
  record_id: United States v. Banks
  status: verified
  projected_at: 2026-07-06
---

# United States v. Banks

*540 U.S. 31 (2003)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
With a warrant to search Banks's two-bedroom apartment for cocaine, North Las Vegas police and FBI agents arrived about 2 p.m., called out "police search warrant," and knocked hard on the door. After waiting 15 to 20 seconds with no answer, they broke open the front door with a battering ram. Banks, in the shower, heard nothing until the crash. The search produced weapons, crack cocaine, and other drug-dealing evidence. Banks moved to suppress, arguing the officers waited an unreasonably short time before forcing entry.

## Issue
In executing a felony drug warrant, was the officers' 15-to-20-second wait after knocking and announcing, before forcibly entering, reasonable under the Fourth Amendment?

## Rule
Yes. Reasonableness depends on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] and the particular [[Exigent Circumstances and Hot Pursuit|exigency]] claimed. Where the [[Exigent Circumstances and Hot Pursuit|exigency]] is the imminent destruction of easily disposable drugs, "we think that after 15 or 20 seconds without a response, police could fairly suspect that cocaine would be gone if they were reticent any longer." — 540 U.S. at 38. ^pin-38

"[W]hen circumstances are exigent because a pusher may be near the point of putting his drugs beyond reach, it is imminent disposal, not travel time to the entrance, that governs when the police may reasonably enter." — *Id.* at 40. ^pin-40

"Once the exigency had matured . . . the officers were not bound to learn anything more or wait any longer before going in, even though their entry entailed some harm to the building." — *Id.* ^pin-40b

## Application
The police arrived in the afternoon, when occupants would likely be up and about, announced loudly, and waited 15 to 20 seconds — long enough for someone to begin flushing cocaine down a drain. The relevant question was the risk of imminent disposal, not whether Banks (who was actually in the shower and unheard-from) had time to reach the door; reasonableness is judged on the facts known to the officers. Because that disposal risk had matured by the end of the wait, the forcible entry was reasonable, and the resulting damage to the door did not change the analysis.

## Conclusion
The 15-to-20-second wait and forcible entry were reasonable under the Fourth Amendment; the judgment suppressing the evidence was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Banks* remains the controlling treatment of how long officers must wait after [[Knock-and-Announce|knock-and-announce]] before forcing entry, applying a fact-specific [[Exigent Circumstances and Hot Pursuit|exigency]] analysis. It builds on [[Richards v. Wisconsin]] and [[Wilson v. Arkansas]] and pairs with [[United States v. Ramirez]] on property damage during forced entry. No negative treatment.

## Appears on
- [[Knock-and-Announce]] — *Progeny*

## Sources
- *United States v. Banks*, 540 U.S. 31 (2003) — https://www.courtlistener.com/opinion/131146/united-states-v-banks/ — pinpoints: 38, 40.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d696b0a6e0774c7b", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "540 U.S. 31 (2003)", "court": "U.S. Supreme Court", "neutral_cite": "2003 U.S. LEXIS 8966", "official_citation_present": true, "parallel_cite": "124 S. Ct. 521; 157 L. Ed. 2d 343", "title": "United States v. Banks", "year": "2003"}}
{"assertion_id": "088d71fbe74a7455", "dimension": "support", "kind": "home_role", "locator": {"home": "Knock-and-Announce"}, "payload": {"home": "Knock-and-Announce", "role": "Progeny", "title": "United States v. Banks"}}
{"assertion_id": "62e986bf8a812b51", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A 15–20-second wait after knocking and announcing before forcing entry to execute a felony drug warrant is reasonable: when the exigency is the imminent destruction of easily disposable evidence, the relevant time is how long disposal would take, not how long the occupant needs to reach the door.", "title": "United States v. Banks"}}
{"assertion_id": "5b5d3da198a2c3eb", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Banks"}}
{"assertion_id": "5fb97628aea97172", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2003-12-02", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Banks", "field_i_validity": "good_law", "scope_note": "Controlling: in a felony drug case, a 15–20-second wait after knock-and-announce before forcible entry is reasonable where the exigency is imminent destruction of easily disposable evidence; reasonableness turns on the time to dispose of evidence, not travel time to the door.", "title": "United States v. Banks", "varies_by_point": "false"}}
```

### lake record — United States v. Banks

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Banks",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Banks",
    "case_name_short": "Banks",
    "case_name_full": "United States v. Banks",
    "input_case_name": "United States v. Banks",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2003-12-02",
    "year": 2003,
    "docket": "02-473",
    "cluster_id": 131146,
    "lead_opinion_id": 131146,
    "sibling_ids": [
      131146
    ],
    "absolute_url": "/opinion/131146/united-states-v-banks/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "540 U.S. 31",
      "volume": "540",
      "reporter": "U.S.",
      "page": "31",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "124 S. Ct. 521",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "521",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 343",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "343",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2003 U.S. LEXIS 8966",
        "volume": "2003",
        "reporter": "U.S. LEXIS",
        "page": "8966",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "540 U.S. 31",
        "volume": "540",
        "reporter": "U.S.",
        "page": "31",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 521",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "521",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 343",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "343",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2003 U.S. LEXIS 8966",
        "volume": "2003",
        "reporter": "U.S. LEXIS",
        "page": "8966",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "540 U.S. 31",
    "official_selection": {
      "court_class": "scotus",
      "selected": "540 U.S. 31",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-38",
      "page": null,
      "quote": "and knocked hard on the door. After waiting 15 to 20 seconds with no answer, they broke open the front door with a battering ram. Banks, in the shower, heard nothing until the crash. The search produced weapons, crack cocaine, and other drug-dealing evidence. Banks moved to suppress, arguing the officers waited an unreasonably short time before forcing entry. ## Issue In executing a felony drug warrant, was the officers' 15-to-20-second wait after knocking and announcing, before forcibly entering, reasonable under the Fourth Amendment? ## Rule Yes. Reasonableness depends on the totality of the circumstances and the particular exigency claimed. Where the exigency is the imminent destruction of easily disposable drugs,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-40",
      "page": null,
      "quote": "[W]hen circumstances are exigent because a pusher may be near the point of putting his drugs beyond reach, it is imminent disposal, not travel time to the entrance, that governs when the police may reasonably enter.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-40b",
      "page": null,
      "quote": "Once the exigency had matured . . . the officers were not bound to learn anything more or wait any longer before going in, even though their entry entailed some harm to the building.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2003-12-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Banks",
    "varies_by_point": false,
    "scope_note": "Controlling: in a felony drug case, a 15\u201320-second wait after knock-and-announce before forcible entry is reasonable where the exigency is imminent destruction of easily disposable evidence; reasonableness turns on the time to dispose of evidence, not travel time to the door.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "United States v. Banks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Southerland, Vince",
          "cluster_id": 186774,
          "cite": [
            "373 U.S. App. D.C. 305",
            "466 F.3d 1083",
            "2006 U.S. App. LEXIS 26978",
            "2006 WL 3069122"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Najar",
          "cluster_id": 167674,
          "cite": [
            "451 F.3d 710",
            "2006 U.S. App. LEXIS 15171",
            "2006 WL 1689231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Singleton",
          "cluster_id": 793669,
          "cite": [
            "441 F.3d 290",
            "2006 U.S. App. LEXIS 7201",
            "2006 WL 724800"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Flores v. State",
          "cluster_id": 1790339,
          "cite": [
            "177 S.W.3d 8"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jackie McCraven",
          "cluster_id": 789610,
          "cite": [
            "401 F.3d 693",
            "2005 U.S. App. LEXIS 4450",
            "2005 WL 608263"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Deandre J. Scroggins",
          "cluster_id": 785508,
          "cite": [
            "361 F.3d 1075",
            "2004 WL 574495"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane1_negative"
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
        "journal_ref": "United States v. Banks:lane2_top_cited"
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
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The PEOPLE of the State of Colorado v. Joshua M. AARNESS",
          "cluster_id": 10014025,
          "cite": [
            "150 P.3d 1271",
            "2006 WL 2998823"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Robinson",
          "cluster_id": 1539942,
          "cite": [
            "974 A.2d 1057",
            "200 N.J. 1",
            "2009 N.J. LEXIS 804"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. Deep East Texas Regional Narcotics Trafficking Task Force",
          "cluster_id": 36001,
          "cite": [
            "379 F.3d 293",
            "2004 U.S. App. LEXIS 15493",
            "2004 WL 1662515"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
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
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Aarness",
          "cluster_id": 2632419,
          "cite": [
            "150 P.3d 1271",
            "2006 WL 2998823"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Larry J. Leaf, Individually and as Personal Representative of the Estate of John P. Leaf, Deceased, Martha A. Leaf, John P. Leaf v. Ronald Shelnutt",
          "cluster_id": 789551,
          "cite": [
            "400 F.3d 1070",
            "2005 U.S. App. LEXIS 4513",
            "2005 WL 628217"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Bynum",
          "cluster_id": 785581,
          "cite": [
            "362 F.3d 574",
            "2004 U.S. App. LEXIS 5703",
            "2004 WL 595136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Snipe",
          "cluster_id": 1387263,
          "cite": [
            "515 F.3d 947",
            "2008 U.S. App. LEXIS 1794",
            "2008 WL 216996"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Estrada",
          "cluster_id": 8439099,
          "cite": [
            "430 F.3d 606"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ellen Storck v. City of Coral Springs",
          "cluster_id": 76396,
          "cite": [
            "354 F.3d 1307",
            "2003 U.S. App. LEXIS 26415",
            "2003 WL 23024573"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
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
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark Brown v. Battle Creek Police Dep't",
          "cluster_id": 4331219,
          "cite": [
            "844 F.3d 556",
            "2016 FED App. 0293P",
            "2016 U.S. App. LEXIS 22447",
            "2016 WL 7336612"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. McHugh",
          "cluster_id": 213881,
          "cite": [
            "639 F.3d 1250",
            "2011 U.S. App. LEXIS 6791",
            "2011 WL 1226486"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Estrada",
          "cluster_id": 792578,
          "cite": [
            "430 F.3d 606",
            "2005 U.S. App. LEXIS 25680"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lynch Ex Rel. Lynch v. City of Mount Vernon",
          "cluster_id": 1454597,
          "cite": [
            "567 F. Supp. 2d 459",
            "2008 U.S. Dist. LEXIS 47137",
            "2008 WL 2885118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lopez",
          "cluster_id": 2566898,
          "cite": [
            "116 P.3d 80",
            "138 N.M. 9",
            "2005 NMSC 018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Vargas",
          "cluster_id": 2634395,
          "cite": [
            "181 P.3d 684",
            "143 N.M. 692",
            "2008 NMSC 019"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matylinsky v. Budge",
          "cluster_id": 1232674,
          "cite": [
            "577 F.3d 1083",
            "2009 U.S. App. LEXIS 18414",
            "2009 WL 2501932"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark D. Jones and Theresa A. Jones v. Ron Wilhelm, Cross-Appellee",
          "cluster_id": 792109,
          "cite": [
            "425 F.3d 455",
            "2005 U.S. App. LEXIS 21386",
            "2005 WL 2417087"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Salvador Martinez-Garcia",
          "cluster_id": 789239,
          "cite": [
            "397 F.3d 1205",
            "2005 U.S. App. LEXIS 2236",
            "2005 WL 326844"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Banks:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(131146) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 150,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 7,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 150,
        "triage_read": 8,
        "triage_snippet_classified": 142
      },
      "lane2_top_cited": {
        "query": "cites:(131146)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00OCZzPTIxNjE2OCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28131146%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(131146)",
        "reviewed": 8,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 8,
        "triage_read": 0,
        "triage_snippet_classified": 8
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(131146)",
    "indexed_citing_opinions": 212,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 131146,
        "count": 212,
        "count_source": "search"
      }
    ],
    "citation_count": 343,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-banks.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY2MjI2ODYmcz00NzE0MTY4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28131146%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 131146,
        "cited_id": 13843,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 107718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 118103,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 118180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 118474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 157939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 499820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 510300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 598972,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 609715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 655530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 758684,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 760850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 776811,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131146,
        "cited_id": 779415,
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
    "date_created": "2026-07-05T22:29:51Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:31:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:31:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:35:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:31:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Banks

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b245-8">
<span citation-index="1" class="star-pagination" label="33"> 
   *33
   </span>
  Justice Souter
 </author>
<p id="Ac">
  delivered the opinion of the Court.
 </p>
<p id="b245-9">
  Officers executing a warrant to search for cocaine in respondent Banks’s apartment knocked and announced their authority. The question is whether their 15-to-20-second wait before a forcible entry satisfied the Fourth Amendment and <span class="citation no-link">18 U. S. C. §3109</span>. We hold that it did.
 </p>
<p id="Af_A">
  I
 </p>
<p id="pAKR">
  With information that Banks was selling cocaine at home, North Las Vegas Police Department officers and Federal Bureau of Investigation agents got a warrant to search his two-bedroom apartment. As soon as they arrived there, about 2 o’clock on a Wednesday afternoon, officers posted in front called out “police search warrant” and rapped hard enough on the door to be heard by officers at the back door. Brief for United States 3 (internal quotation marks omitted). There was no indication whether anyone was home, and after waiting for 15 to 20 seconds with no answer, the officers broke open the front door with a battering ram. Banks was in the shower and testified that he heard nothing until the crash of the door, which brought him out dripping to confront the police. The search produced weapons, crack cocaine, and other evidence of drug dealing.
 </p>
<p id="b245-4">
  In response to drug and firearms
  <em>
   charges, Banks moved to
  </em>
  suppress evidence, arguing that the officers executing the search warrant waited an unreasonably short time before forcing entry, and so violated both the Fourth Amendment and <span class="citation no-link">18 U. S. C. § 3109</span>.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The District Court denied the motion, and Banks pleaded guilty, reserving his right to challenge the search on appeal.
 </p>
<p id="b246-3">
<span citation-index="1" class="star-pagination" label="34"> 
   *34
   </span>
  A divided panel of the Ninth Circuit reversed and ordered suppression of the evidence found. <span class="citation" data-id="9494813"><a href="/opinion/776811/united-states-v-lashawn-lowell-banks/" aria-description="Citation for case: United States v. Lashawn Lowell Banks">282 F. 3d 699</a></span> (2002). In assessing the reasonableness of the execution of the warrant, the panel majority set out a nonexhaustive list of “factors that an officer reasonably should consider” in deciding when to enter premises identified in a warrant, after knocking and announcing their presence but receiving no express acknowledgment:
 </p>
<blockquote id="b246-4">
  “(a) size of the residence; (b) location of the residence; (c) location of the officers in relation to the main living or sleeping areas of the residence; (d) time of day; (e) nature of the suspected offense; (f) evidence demonstrating the suspect's guilt; (g) suspect’s prior convictions and, if any, the type of offense for which he was convicted; and (h) any other observations triggering the senses of the officers that reasonably would lead one to believe that immediate entry was necessary.”
  <span class="citation" data-id="9494813"><a href="/opinion/776811/united-states-v-lashawn-lowell-banks/#704" aria-description="Citation for case: United States v. Lashawn Lowell Banks"><em>
   Id.,
  </em>
  at 704</a></span>.
 </blockquote>
<p id="b246-5">
  The majority also defined four categories of intrusion after knock and announcement, saying that the classification “aids in the resolution of the essential question whether the entry made herein was reasonable under the circumstances”:
 </p>
<blockquote id="b246-6">
  “(1) entries in which exigent circumstances exist and non-forcible entry is possible, permitting entry to be made simultaneously with or shortly after announcement; (2) entries in which exigent circumstances exist and forced entry by destruction of property is required, necessitating more specific inferences of exigency; (3) entries in which no exigent circumstances exist and non-forcible entry is possible, requiring an explicit refusal of admittance or a lapse of a significant amount of time; and (4) entries in which no exigent circumstances exist and forced entry by destruction of property is required, mandating an explicit refusal of admittance or a
  <span citation-index="1" class="star-pagination" label="35"> 
   *35
   </span>
  lapse of an even more substantial amount of time.”
  <em>
   <span class="citation" data-id="9494813"><a href="/opinion/776811/united-states-v-lashawn-lowell-banks/" aria-description="Citation for case: United States v. Lashawn Lowell Banks">Ibid.</a></span>
  </em>
</blockquote>
<p id="b247-7">
  The panel majority put the action of the officers here in the last category, on the understanding that they destroyed the door without hearing anything to suggest a refusal to admit even though sound traveled easily through the small apartment. The majority held the 15-to-20-second delay after knocking and announcing to be “[insufficient ... to satisfy the constitutional safeguards.”
  <span class="citation" data-id="9494813"><a href="/opinion/776811/united-states-v-lashawn-lowell-banks/#705" aria-description="Citation for case: United States v. Lashawn Lowell Banks"><em>
   Id.,
  </em>
  at 705</a></span>.
 </p>
<p id="b247-8">
  Judge Fisher dissented, saying that the majority ought to come out the other way based on the very grounds it stressed: Banks’s small apartment, the loud knock and announcement, the suspected offense of dealing in cocaine, and the time of the day. Judge Fisher thought the lapse of 15 to 20 seconds was enough to support a reasonable inference that admittance had been constructively denied.
  <span class="citation" data-id="9494813"><a href="/opinion/776811/united-states-v-lashawn-lowell-banks/#710" aria-description="Citation for case: United States v. Lashawn Lowell Banks"><em>
   Id.,
  </em>
  at 710</a></span>.
 </p>
<p id="b247-9">
  We granted certiorari to consider how to go about applying the standard of reasonableness to the length of time police with a warrant must wait before entering without permission after knocking and announcing their intent in a felony case. <span class="citation multiple-matches"><a href="/c/U.%20S./537/1187/">537 U. S. 1187</a></span> (2003). We now reverse.
 </p>
<p id="AQH">
  II.
 </p>
<p id="pAPl">
  There has never been a dispute that these officers were obliged
  <em>
   to knock and announce their intentions
  </em>
  when
  <em>
   executing
  </em>
  the search warrant, an obligation they concededly honored. Despite this agreement, we start with a word about standards for requiring or dispensing with a knock and announcement, since the same criteria bear on when the officers could legitimately enter after knocking.
 </p>
<p id="b247-4">
  The Fourth Amendment says nothing specific about formalities in exercising a warrant’s authorization, speaking to the manner of searching as well as to the legitimacy of searching at all simply in terms of the right to be “secure . . . against unreasonable searches and seizures.” Although the notion of reasonable execution must therefore be fleshed
  <span citation-index="1" class="star-pagination" label="36"> 
   *36
   </span>
  out, we have done that case by case, largely avoiding categories and protocols for searches. Instead, we have treated reasonableness as a function of the facts of cases so various that no template is likely to produce sounder results than examining the totality of circumstances in a given case; it is too hard to invent categories without giving short shrift to details that turn out to be important in a given instance, and without inflating marginal ones. See,
  <em>
   e. g., Ohio
  </em>
  v.
  <em>
   Robinette,
  </em>
  <span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/#39" aria-description="Citation for case: Ohio v. Robinette">519 U. S. 33, 39</a></span> (1996) (“[W]e have consistently eschewed bright-line rules, instead emphasizing the fact-specific nature of the reasonableness inquiry”);
  <em>
   Ker
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#33" aria-description="Citation for case: Ker v. California">374 U. S. 23, 33</a></span> (1963) (reasonableness not susceptible to Procrustean application);
  <em>
   Go-Bart Importing Co.
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#357" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 357</a></span> (1931) (no formula for determining reasonableness; each case on its own facts and circumstances). We have, however, pointed out factual considerations of unusual, albeit not dispositive, significance.
 </p>
<p id="b248-5">
  In
  <em>
   Wilson
  </em>
  v.
  <em>
   Arkansas,
  </em>
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927</a></span> (1995), we held that the common law knock-and-announce principle is one focus of the reasonableness enquiry; and we subsequently decided that although the standard generally requires the police to announce their intent to search before entering closed premises, the obligation gives way when officers “have a reasonable suspicion that knocking and announcing their presence, under the particular circumstances, would be dangerous or futile, or . . . would inhibit the effective investigation of the crime by, for example, allowing the destruction of evidence,”
  <em>
   Richards
  </em>
  v.
  <em>
   Wisconsin,
  </em>
  <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/#394" aria-description="Citation for case: Richards v. Wisconsin">520 U. S. 385, 394</a></span> (1997). When a warrant applicant gives reasonable grounds to expect futility or to suspect that one or another such exigency already exists or will arise instantly upon knocking, a magistrate judge is acting within the Constitution to authorize a “no-knock” entry.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  And even when executing a warrant silent about
  <span citation-index="1" class="star-pagination" label="37"> 
   *37
   </span>
  that, if circumstances support a reasonable suspicion of exigency when the officers arrive at the door, they may go straight in.
  <em>
   Id,.,
  </em>
  at 394, 396, n. 7.
 </p>
<p id="b249-5">
  Since most people keep their doors locked, entering without knocking will normally do some damage, a circumstance too common to require a heightened justification when a reasonable suspicion of exigency already justifies an unwarned entry. We have accordingly held that police in exigent circumstances may damage premises so far as necessary for a no-knock entrance without demonstrating the. suspected risk in any more detail than the law demands for an unannounced intrusion simply by lifting the latch.
  <em>
   United States
  </em>
  v.
  <em>
   Ramirez, 523
  </em>
  U. S. 65, 70-71 (1998). Either way, it is enough that the officers had a reasonable suspicion of exigent circumstances.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b249-6">
  Ill
 </p>
<p id="b249-7">
  Like
  <em>
   Ramirez,
  </em>
  this case turns on the significance of exigency revealed by circumstances known to the officers, for the only substantive difference between the two situations goes to the time at which the officers reasonably anticipated some danger calling for action without delay.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  Whereas the
  <span citation-index="1" class="star-pagination" label="38"> 
   *38
   </span>
<em>
   Ramirez
  </em>
  Magistrate Judge found in advance that the customary warning would raise an immediate risk that a wanted felon would elude capture or pose a threat to the officers, see
  <span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/#68" aria-description="Citation for case: United States v. Ramirez"><em>
   id.,
  </em>
  at 68</a></span>, here the Government claims that a risk of losing. . evidence arose shortly after knocking and announcing. Although the police concededly arrived at Banks’s door without reasonable suspicion of facts justifying a no-knock entry, they argue that announcing their presence started the clock running toward the moment of apprehension that Banks would flush away the easily disposable cocaine, prompted by knowing the police would soon be coming in. While it was held reasonable for the police in
  <em>
   Ramirez
  </em>
  tó enter forcibly upon arrival, the Government argues it was equally reasonable for the officers to go in with force here as soon as the danger of disposal had ripened.
 </p>
<p id="b250-5">
  Banks does not, of course, deny that exigency may develop in the period beginning when officers with a warrant knock to be admitted, and the issue comes down to whether it was reasonable to suspect imminent loss of evidence after the 15 to 20 seconds the officers waited prior to forcing their way. Though we agree with Judge Fisher’s dissenting opinion that this call is a close one, <span class="citation" data-id="9494813"><a href="/opinion/776811/united-states-v-lashawn-lowell-banks/#707" aria-description="Citation for case: United States v. Lashawn Lowell Banks">282 F. 3d, at 707</a></span>, we think that after 15 or 20 seconds without a response, police could fairly suspect that cocaine would be gone if they were reticent any longer. Courts of Appeals have, indeed, routinely held similar wait times to be reasonable in drug cases with similar facts including easily disposable evidence (and some courts have found even shorter ones to be reasonable enough).
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
</p>
<p id="b251-4">
<span citation-index="1" class="star-pagination" label="39"> 
   *39
   </span>
  A look at Banks’s counterarguments shows why these courts reached sensible results, for each of his reasons for saying that 15 to 20 seconds was too brief rests on a mistake about the relevant enquiry: the fact that he was actually in the shower and did not hear the officers is not to the point, and the same is true of the claim that it might have taken him longer than 20 seconds if he had heard the knock and headed straight for the door. As for the shower, it is enough to say that the facts known to the police are what count in judging reasonable waiting time, cf.,
  <em>
   e. g., Graham
  </em>
  v.
  <em>
   Connor,
  </em>
  <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor">490 U. S. 386, 396</a></span> (1989) (“The ‘reasonableness’ of a particular use of force must be judged from the perspective of a reasonable officer on the scene, rather than with the 20/20 vision of hindsight”), and there is no indication that the police knew that Banks was in the shower and thus unaware of an impending search that he would otherwise have tried to frustrate.
 </p>
<p id="b251-5">
  And the argument that 15 to 20 seconds was too short for Banks to have come to the door ignores the very risk that justified prompt entry. True, if the officers were to justify their timing here by claiming that Banks’s failure to admit them fairly suggested a refusal to let them in, Banks could at least argue that no such suspicion can arise until an occu
  <span citation-index="1" class="star-pagination" label="40"> 
   *40
   </span>
  pant has had time to get to the door,
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
  a time that will vary with the size of the establishment, perhaps five seconds to open a motel room door, or several minutes to move through a townhouse. In this case, however, the police claim exigent need to enter, and the crucial fact in examining their actions is not time to reach the door but the particular exigency claimed. On the record here, what matters is the opportunity to get rid of cocaine, which a prudent dealer will keep near a commode or kitchen sink. The significant circumstances include the arrival of the police during the day, when anyone inside would probably have been up and around, and the sufficiency of 15 to 20 seconds for getting to the bathroom or the kitchen to start flushing cocaine down the drain. That is, when circumstances are exigent because a pusher may be near the point of putting his drugs beyond reach, it is imminent disposal, not travel time to the entrance, that governs when the police may reasonably enter; since the bathroom and kitchen are usually in the interior of a dwelling, not the front hall, there is no reason generally to peg the travel time to the location of the door, and no reliable basis for giving the proprietor of a mansion a longer wait than the resident of a bungalow, or an apartment like Banks’s. And 15 to 20 seconds does not seem an unrealistic guess about the time someone would need to get in a position to rid his quarters of cocaine.
 </p>
<p id="b252-5">
  Once thé exigency had matured, of course, the officers were not bound to learn anything more or wait any longer before going in, even though their entry entailed some harm to the building.
  <em>
   Ramirez
  </em>
  held that the exigent need of law enforcement trumps a resident’s interest in avoiding all property damage, see <span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/#70" aria-description="Citation for case: United States v. Ramirez">523 U. S., at 70-71</a></span>, and there is no reason to treat a post-knock exigency differently from the no-knock counterpart in
  <em>
   Ramirez
  </em>
  itself.
 </p>
<p id="b253-7">
<span citation-index="1" class="star-pagination" label="41"> 
   *41
   </span>
  I
  <em>
   V
  </em>
</p>
<p id="b253-3">
  Our emphasis on totality analysis necessarily rejects positions taken on each side of this case.
  <em>
   Ramirez,
  </em>
  for example, cannot be read with the breadth the Government espouses, as “reflectfing] a general principle that the need to damage property in order to effectuate an entry to execute a search warrant should not be part of the analysis of whether the entry itself was reasonable.” Brief for United States 18; Reply Brief for United States 4. At common law, the knock-and-announce rule was traditionally “justified in part by the belief that announcement generally would avoid ‘the destruction or breaking of any house ... by which great damage and inconvenience might ensue.’”
  <em>
   Wilson,
  </em>
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">514 U. S., at 935</a></span>-936 (quoting
  <em>
   Semayne’s Case,
  </em>
  5 Co. Rep. 91a, 91b, 77 Eng. Rep. 194, 196 (K. B. 1603)). One point in making an officer knock and announce, then, is to give a person inside the chance to save his door. That is why, in the case with no reason to suspect an immediate risk of frustration or futility in waiting at all, the reasonable wait time may well be longer when police make a forced entry, since they ought to be more certain the occupant has had time to answer the door. It is hard to be more definite than that, without turning the notion of a reasonable time under all the . circumstances into a set of sub-rules as the Ninth Circuit has been inclined to do. Suffice it to say that the need to damage property in the course of getting in is a good reason to require more patience than it would be reasonable to expect if the door were open. Police seeking a stolen piano may be able to spend more time to make sure they really need the battering ram.
 </p>
<p id="b253-4">
  On the other side, we disapprove of the Court of Appeals’s four-part scheme for vetting knock-and-announce entries. To begin with, the demand for enhanced evidence of exigency before a door can reasonably be damaged by a warranted no-knock intrusion was already bad law before the Court of Appeals decided this case. In
  <em>
   Ramirez
  </em>
  (a case from the
  <span citation-index="1" class="star-pagination" label="42"> 
   *42
   </span>
  Ninth Circuit), we rejected an attempt to subdivide felony-cases by accepting “mild exigency” for entry without property damage, but requiring “more specific inferences of exigency” before damage would be reasonable. <span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/#69" aria-description="Citation for case: United States v. Ramirez">523 U. S., at 69-71</a></span> (internal quotation marks omitted). The Court of Appeals did not cite
  <em>
   Ramirez.
  </em>
</p>
<p id="b254-5">
  Nor did the appeals court cite
  <em>
   United States
  </em>
  v.
  <em>
   Arvizu,
  </em>
  <span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/" aria-description="Citation for case: United States v. Arvizu">534 U. S. 266</a></span> (2002) (again, from the Ninth Circuit). There, we recently disapproved a framework for making reasonable suspicion determinations that attempted to reduce what the Circuit described as “troubling . . . uncertainty” in reasonableness analysis, by “describing] and clearly delimiting]” an officer’s consideration of certain factors.
  <span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/#272" aria-description="Citation for case: United States v. Arvizu"><em>
   Id.,
  </em>
  at 272, 275</a></span> (internal quotation marks omitted). Here, as in
  <em>
   <span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/" aria-description="Citation for case: United States v. Arvizu">Arvizu</a></span>,
  </em>
  the Court of Appeals’s overlay of a categorical scheme on the general reasonableness analysis threatens to distort the “totality of the circumstances” principle, by replacing a stress on revealing facts with resort to pigeonholes.
  <span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/#274" aria-description="Citation for case: United States v. Arvizu"><em>
   Id.,
  </em>
  at 274</a></span> (internal quotation marks omitted). Attention to cocaine rocks and pianos tells a lot about the chances of their respective disposal and its bearing on reasonable time. Instructions couched in terms like “significant amount of time,” and “an even more substantial amount of time,” <span class="citation" data-id="9494813"><a href="/opinion/776811/united-states-v-lashawn-lowell-banks/#704" aria-description="Citation for case: United States v. Lashawn Lowell Banks">282 F. 3d, at 704</a></span>, tell very little.
 </p>
<p id="b254-6">
  V
 </p>
<p id="b254-7">
  Last, there is Banks’s claim that the entry violated <span class="citation no-link">18 U. S. C. § 3109</span>.
  <em>
   Ramirez
  </em>
  held that the result should be the same under the Fourth Amendment and §3109, permitting an officer to enter by force “if, after notice of his authority and purpose, he is refused admittance.” We explained the statute’s “‘requirement of prior notice . . . before forcing entry . . . [as] codiffying] a tradition embedded in Anglo-American law,’ ” <span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/" aria-description="Citation for case: United States v. Ramirez">523 U. S., at 72</a></span> (quoting
  <em>
   Miller
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#313" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 313</a></span> (1958)); see also
  <em>
   Sabbath
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="107718"><a href="/opinion/107718/sabbath-v-united-states/#591" aria-description="Citation for case: Sabbath v. United States">391 U. S. 585, 591, n. 8</a></span> (1968), and we held that § 3109 implicates the exceptions to the common law knock-and-
  <span citation-index="1" class="star-pagination" label="43"> 
   *43
   </span>
  announce requirement that inform the Fourth Amendment itself, <span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/#73" aria-description="Citation for case: United States v. Ramirez">523 U. S., at 73</a></span>. The upshot is that § 3109 is subject to an exigent circumstances exception,
  <em>
   ibid.,
  </em>
  which qualifies the requirement of refusal after notice, just as it qualifies the obligation to announce in the first place. Absent exigency, the police must knock and receive an actual refusal or wait out the time necessary to infer one. But in a case like this, where the officers knocked and announced their presence, and forcibly entered after a reasonable suspicion of exigency had ripened, their entry satisfied § 3109 as well as the Fourth Amendment, even without refusal of admittance.
 </p>
<p id="b255-5">
  The judgment of the Court of Appeals is reversed.
 </p>
<p id="b255-6">
<em>
   So ordered.
  </em>
</p>






<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b245-6">
   The statute provides: “The officer may break open any outer or inner door or window of a house, or any part of a house, or anything therein, to execute a search warrant, if, after notice of his authority and purpose, he is refused admittance or when necessary to liberate himself or a person aiding him in the execution of the warrant.”
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b248-6">
   Some States give magistrate judges the authority to issue “no-knock” warrants, and some do not. See,
   <em>
    e. g., Richards
   </em>
   v.
   <em>
    Wisconsin,
   </em>
   <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/#396" aria-description="Citation for case: Richards v. Wisconsin">520 U. S. 385, 396, n. 7</a></span> (1997) (collecting state statutes and cases).
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b249-8">
   The standard for a no-knock entry stated in
   <em>
    <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">Richards</a></span>
   </em>
   applies on reasonable suspicion of exigency or futility. Because the facts here go to exigency, not futility, we speak of that alone.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b249-9">
<em>
    Ramirez
   </em>
   and
   <em>
    Richards
   </em>
   v.
   <em>
    Wisconsin,
   </em>
   <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">520 U.S. 385</a></span> (1997), our cases addressing the role of exigency in assessing the reasonableness' of a no-knock entry, involved searches by warrant for evidence of a felony, as does this case. In a different context governed by the Fourth Amendment, we have held that the risk of losing evidence of a minor offense is insufficient to make it reasonable to enter a dwelling to make a warrantless arrest. See
   <em>
    Welsh
   </em>
   v.
   <em>
    Wisconsin,
   </em>
   <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740</a></span> (1984). Courts of Appeals have applied
   <em>
    Welsh
   </em>
   to warrantless entries simply to search for evidence, considering the gravity of the offense in determining whether exigent circumstances exist. See,
   <em>
    e. g., United States
   </em>
   v.
   <em>
    Aquino,
   </em>
   <span class="citation" data-id="499820"><a href="/opinion/499820/united-states-v-luis-raul-aquino/#1271" aria-description="Citation for case: United States v. Luis Raul Aquino">836 F. 2d 1268, 1271-1273</a></span> (CA10 1988);
   <em>
    United States
   </em>
   v.
   <em>
    Clement,
   </em>
   <span class="citation" data-id="9478056"><a href="/opinion/510300/united-states-v-kenneth-clement/#1120" aria-description="Citation for case: United States v. Kenneth Clement">854 F. 2d 1116, 1120</a></span> (CA8 1988)
   <em>
    (per curiam).
   </em>
   We intimate nothing here about such warrantless entry cases. Nor do we express a view on the significance of the existence of a warrant in evaluating whether exigency justifies action in
   <span citation-index="1" class="star-pagination" label="38"> 
    *38
    </span>
   knock-and-armounce cases when the reason for the search is a minor offense.
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b250-8">
   Several Courts of Appeals have explicitly taken into account the risk of disposal of drug evidence as a factor in evaluating the reasonableness of waiting time. See,
   <em>
    e. g., United States
   </em>
   v.
   <em>
    Goodson,
   </em>
   <span class="citation" data-id="760850"><a href="/opinion/760850/united-states-v-terrence-eugene-goodson/#612" aria-description="Citation for case: United States v. Terrence Eugene Goodson">165 F. 3d 610, 612, 614</a></span> (CA8 1999) (holding a 20-second wait after a loud announcement at a one-story ranch reasonable);
   <em>
    United States
   </em>
   v.
   <em>
    Spikes,
   </em>
   <span class="citation" data-id="758684"><a href="/opinion/758684/united-states-v-james-h-spikes-96-3899-marilyn-smith-96-3660/#925" aria-description="Citation for case: United States v. James H. Spikes (96-3899) Marilyn Smith...">158 F. 3d 913, 925-927</a></span> (CA6 1998) (holding a 15-to-30-second wait in midmorning after a loud announcement reasonable);
   <em>
    United States
   </em>
   v.
   <em>
    Spriggs,
   </em>
   <span class="citation" data-id="609715"><a href="/opinion/609715/united-states-v-terrance-kevin-spriggs-aka-bob/" aria-description="Citation for case: United States v. Terrance Kevin Spriggs, A/K/A Bob">996 F. 2d 320</a></span>, 322-
   <span citation-index="1" class="star-pagination" label="39"> 
    *39
    </span>
   323 (CADC 1993) (holding a 15-second wait after a reasonably audible
   <em>
    announcement at
   </em>
   7:45
   <em>
    a.m. on a weekday reasonable); United States v. Garcia,
   </em>
   <span class="citation" data-id="598972"><a href="/opinion/598972/united-states-v-jose-a-garcia-united-states-v-pablo-h-garcia/#1168" aria-description="Citation for case: United States v. Jose A. Garcia, United States v. Pablo...">983 F. 2d 1160, 1168</a></span> (CA1 1993) (holding a 10-second wait after a loud announcement reasonable);
   <em>
    United States
   </em>
   v.
   <em>
    Jones,
   </em>
   <span class="citation" data-id="13843"><a href="/opinion/13843/united-states-v-jones/#361" aria-description="Citation for case: United States v. Jones">133 F. 3d 358, 361-362</a></span> (CA5 1998)
   <em>
    (per curiam,)
   </em>
   (relying specifically on the concept of exigency, holding a 15-to-20-second wait reasonable). See also
   <em>
    United States
   </em>
   v.
   <em>
    Chavez-Miranda,
   </em>
   <span class="citation" data-id="779415"><a href="/opinion/779415/united-states-v-tomas-chavez-miranda/#981" aria-description="Citation for case: United States v. Tomas Chavez-Miranda">306 F. 3d 973, 981-982, n. 7</a></span> (CA9 2002)
   <em>
    (“Banks
   </em>
   appears to be a departure from our prior decisions. . . . [W]e have found a 10 to 20 second wait to be reasonable in similar circumstances, albeit when the police heard sounds after the knock and announcement”);
   <em>
    United States
   </em>
   v.
   <em>
    Jenkins,
   </em>
   175 F 3d 1208, 1215 (CA10 1999) (holding a 14-to-20-second wait at 10 am. reasonable);
   <em>
    United States
   </em>
   v.
   <em>
    Markling,
   </em>
   <span class="citation" data-id="655530"><a href="/opinion/655530/united-states-v-timothy-w-markling/#1318" aria-description="Citation for case: United States v. Timothy W. Markling">7 F. 3d 1309, 1318-1319</a></span> (CA7 1993) (holding a 7-second wait at a small motel room reasonable when officers acted on a specific tip that the suspect was likely to dispose of the drugs).
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b252-6">
   It is probably unrealistic even on its own terms. The apartment was “small,” <span class="citation" data-id="9494813"><a href="/opinion/776811/united-states-v-lashawn-lowell-banks/#704" aria-description="Citation for case: United States v. Lashawn Lowell Banks">282 F. 3d 699, 704</a></span> (CA9 2002), and a man may walk the length of today’s small apartment in 15 seconds.
  </p>
</div></div></opinion>
```

---
