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

## GROUP: _overhaul2/lake/cases/United States v. Dunn.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Dunn"
type: case
citation: "480 U.S. 294 (1987)"
parallel_cite: "107 S. Ct. 1134; 94 L. Ed. 2d 326"
neutral_cite: 1987 U.S. LEXIS 1057
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-04-20
docket: 85-998
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-03-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Dunn
  varies_by_point: false
  scope_note: "Good law; the four-factor Dunn test remains the governing framework for determining the extent of a home's curtilage (applied in Jardines and Collins v. Virginia)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111833/united-states-v-dunn/"
  cluster_id: 111833
  opinion_id: 9430862
  identity_checked: true
homes:
  - page: "[[Curtilage]]"
    role: "Key — Anchor"
  - page: "[[Open Fields]]"
    role: "Key"
related: ["[[Oliver v. United States]]", "[[California v. Ciraolo]]", "[[Hester v. United States]]", "[[Florida v. Jardines]]", "[[Collins v. Virginia]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "curtilage", "open-fields", "home"]
holding: "Curtilage is determined by four factors — proximity to the home, whether the area is within an enclosure surrounding the home, the nature of its use, and steps taken to shield it from observation — all bearing on whether the area is so intimately tied to the home as to fall under the home's Fourth Amendment umbrella."
lake:
  record_id: United States v. Dunn
  status: verified
  projected_at: 2026-07-06
---

# United States v. Dunn

*480 U.S. 294 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal agents, investigating a drug-manufacturing operation, crossed perimeter fences onto Dunn's ranch and approached a barn standing about 50 yards beyond the fence surrounding the ranch house. Without entering the barn, agents stood outside it, smelled chemicals associated with drug manufacture, and shined a flashlight inside to observe a suspected drug lab. That observation supported a warrant; Dunn moved to suppress, arguing the barn was within the home's [[Curtilage|curtilage]] and thus protected.

## Issue
Whether the area near the barn — located approximately 50 yards from the fence surrounding the ranch house — was within the [[Curtilage|curtilage]] of the house for Fourth Amendment purposes, such that the agents' warrantless observation invaded a protected area.

## Rule
[[Curtilage]] is determined by reference to four factors: "curtilage questions should be resolved with particular reference to four factors: the proximity of the area claimed to be curtilage to the home, whether the area is included within an enclosure surrounding the home, the nature of the uses to which the area is put, and the steps taken by the resident to protect the area from observation by people passing by." — 480 U.S. at 301. ^pin-301

The factors are not a rigid formula but tools serving one question: "these factors are useful analytical tools only to the degree that, in any given case, they bear upon the centrally relevant consideration — whether the area in question is so intimately tied to the home itself that it should be placed under the home's 'umbrella' of Fourth Amendment protection." — *Id.* ^pin-301a

## Application
Applying the four factors to Dunn's barn: it sat 50 yards from the fence enclosing the house (not in close proximity); it stood outside that fence, so it was not within the enclosure surrounding the home; the agents had objective indications the barn was used to manufacture drugs rather than for intimate activities of the home; and Dunn had done little to shield the barn's interior from observation by anyone standing in the open fields. Together these showed the barn was not so intimately tied to the home as to fall within its [[Curtilage|curtilage]]. Because the barn lay in the open fields, the agents' observation from outside it was not a Fourth Amendment search.

## Conclusion
The barn and its surrounding area lay outside the [[Curtilage|curtilage]] of the ranch house, so the warrantless observation did not violate the Fourth Amendment; the Fifth Circuit was reversed. *Dunn* supplies the controlling four-factor [[Curtilage|curtilage]] test.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Dunn*'s four-factor test remains the governing [[Curtilage|curtilage]] analysis and is applied in later home-privacy cases, including [[Florida v. Jardines]] (front-porch [[Curtilage|curtilage]]) and [[Collins v. Virginia]] (driveway/[[Curtilage|curtilage]] and the automobile exception).

## Appears on
- [[Curtilage]] — *Key — Anchor*

## Sources
- *United States v. Dunn*, 480 U.S. 294 (1987) — https://www.courtlistener.com/opinion/111833/united-states-v-dunn/ — pinpoints: 301.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c43dd2a08925918e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Dunn"}, "payload": {"all": [{"cite": "480 U.S. 294", "page": "294", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "480"}, {"cite": "107 S. Ct. 1134", "page": "1134", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "107"}, {"cite": "94 L. Ed. 2d 326", "page": "326", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "94"}, {"cite": "1987 U.S. LEXIS 1057", "page": "1057", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1987"}], "display": "480 U.S. 294", "official": {"cite": "480 U.S. 294", "page": "294", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "480"}, "official_selection_present": true, "record_id": "United States v. Dunn"}}
{"assertion_id": "2c999415eaee70ae", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-301", "record_id": "United States v. Dunn"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-301", "pinpoint_status": "slip-only", "quote": "--- # United States v. Dunn *480 U.S. 294 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal agents, investigating a drug-manufacturing operation, crossed perimeter fences onto Dunn's ranch and approached a barn standing about 50 yards beyond the fence surrounding the ranch house. Without entering the barn, agents stood outside it, smelled chemicals associated with drug manufacture, and shined a flashlight inside to observe a suspected drug lab. That observation supported a warrant; Dunn moved to suppress, arguing the barn was within the home's curtilage and thus protected. ## Issue Whether the area near the barn — located approximately 50 yards from the fence surrounding the ranch house — was within the curtilage of the house for Fourth Amendment purposes, such that the agents' warrantless observation invaded a protected area. ## Rule Curtilage is determined by reference to four factors:", "quote_fidelity": "mismatch", "record_id": "United States v. Dunn", "star_marker": null}}
{"assertion_id": "9a208099453f56dd", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-301a", "record_id": "United States v. Dunn"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-301a", "pinpoint_status": "slip-only", "quote": "these factors are useful analytical tools only to the degree that, in any given case, they bear upon the centrally relevant consideration — whether the area in question is so intimately tied to the home itself that it should be placed under the home's 'umbrella' of Fourth Amendment protection.", "quote_fidelity": "mismatch", "record_id": "United States v. Dunn", "star_marker": null}}
{"assertion_id": "53029dbf7bcaf542", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Dunn"}, "payload": {"as_of_content": "1987-03-03", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Dunn", "scope_note": "Good law; the four-factor Dunn test remains the governing framework for determining the extent of a home's curtilage (applied in Jardines and Collins v. Virginia).", "varies_by_point": false}}
```

### lake record — United States v. Dunn

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Dunn",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Dunn",
    "case_name_short": "Dunn",
    "case_name_full": "United States v. Dunn",
    "input_case_name": "United States v. Dunn",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-04-20",
    "year": 1987,
    "docket": "85-998",
    "cluster_id": 111833,
    "lead_opinion_id": 9430862,
    "sibling_ids": [
      111833,
      9430862,
      9430863,
      9430864
    ],
    "absolute_url": "/opinion/111833/united-states-v-dunn/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "480 U.S. 294",
      "volume": "480",
      "reporter": "U.S.",
      "page": "294",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 1134",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1134",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 326",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "326",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 1057",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1057",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "480 U.S. 294",
        "volume": "480",
        "reporter": "U.S.",
        "page": "294",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 1134",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1134",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 326",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "326",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 1057",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1057",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "480 U.S. 294",
    "official_selection": {
      "court_class": "scotus",
      "selected": "480 U.S. 294",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-301",
      "page": null,
      "quote": "--- # United States v. Dunn *480 U.S. 294 (1987)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal agents, investigating a drug-manufacturing operation, crossed perimeter fences onto Dunn's ranch and approached a barn standing about 50 yards beyond the fence surrounding the ranch house. Without entering the barn, agents stood outside it, smelled chemicals associated with drug manufacture, and shined a flashlight inside to observe a suspected drug lab. That observation supported a warrant; Dunn moved to suppress, arguing the barn was within the home's curtilage and thus protected. ## Issue Whether the area near the barn \u2014 located approximately 50 yards from the fence surrounding the ranch house \u2014 was within the curtilage of the house for Fourth Amendment purposes, such that the agents' warrantless observation invaded a protected area. ## Rule Curtilage is determined by reference to four factors:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-301a",
      "page": null,
      "quote": "these factors are useful analytical tools only to the degree that, in any given case, they bear upon the centrally relevant consideration \u2014 whether the area in question is so intimately tied to the home itself that it should be placed under the home's 'umbrella' of Fourth Amendment protection.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-03-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Dunn",
    "varies_by_point": false,
    "scope_note": "Good law; the four-factor Dunn test remains the governing framework for determining the extent of a home's curtilage (applied in Jardines and Collins v. Virginia).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Wittey",
          "cluster_id": 9404034,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Sorenson",
          "cluster_id": 4806437,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Fredericq",
          "cluster_id": 4613398,
          "cite": [
            "121 N.E.3d 166",
            "482 Mass. 70"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Dobson",
          "cluster_id": 7174628,
          "cite": [
            "102 N.E.3d 1032",
            "92 Mass. App. Ct. 1128"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri, Plaintiff/Respondent v. Timothy A. Pierce",
          "cluster_id": 4254135,
          "cite": [
            "504 S.W.3d 766",
            "2016 Mo. App. LEXIS 864"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
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
        "journal_ref": "United States v. Dunn:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grice",
          "cluster_id": 2792904,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grice",
          "cluster_id": 2772730,
          "cite": [
            "367 N.C. 753",
            "767 S.E.2d 312",
            "2015 N.C. LEXIS 69"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brown v. State",
          "cluster_id": 2736404,
          "cite": [
            "152 So. 3d 619",
            "2014 Fla. App. LEXIS 14965",
            "2014 WL 4723562"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
      },
      {
        "citing_case": {
          "name": "STATE OF MISSOURI, Plaintiff-Respondent v. TENA D. CADY",
          "cluster_id": 2673768,
          "cite": [
            "425 S.W.3d 234",
            "2014 WL 1328278",
            "2014 Mo. App. LEXIS 372"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane1_negative"
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
        "journal_ref": "United States v. Dunn:lane2_top_cited"
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
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Greenwood",
          "cluster_id": 112067,
          "cite": [
            "100 L. Ed. 2d 30",
            "108 S. Ct. 1625",
            "486 U.S. 35",
            "1988 U.S. LEXIS 2279",
            "56 U.S.L.W. 4409"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
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
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bond v. United States",
          "cluster_id": 118354,
          "cite": [
            "146 L. Ed. 2d 365",
            "120 S. Ct. 1462",
            "529 U.S. 334",
            "2000 U.S. LEXIS 2520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Johnson",
          "cluster_id": 773999,
          "cite": [
            "256 F.3d 895",
            "2001 Daily Journal DAR 7479",
            "2001 Cal. Daily Op. Serv. 6099",
            "2001 U.S. App. LEXIS 16092",
            "2001 WL 817633"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
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
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Pitman",
          "cluster_id": 2234418,
          "cite": [
            "813 N.E.2d 93",
            "211 Ill. 2d 502",
            "286 Ill. Dec. 36",
            "2004 Ill. LEXIS 989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estate Robert Smith v. Marasco",
          "cluster_id": 3013435,
          "cite": [
            "318 F.3d 497"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Albert Lee Purcell, Shon Purcell",
          "cluster_id": 771684,
          "cite": [
            "236 F.3d 1274"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "ESTATE OF",
          "cluster_id": 780724,
          "cite": [
            "318 F.3d 497",
            "2003 U.S. App. LEXIS 1432"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
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
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathan Rogers v. M. L. Pendleton, Officer M. G. Vinyard, Officer",
          "cluster_id": 773125,
          "cite": [
            "249 F.3d 279",
            "2001 U.S. App. LEXIS 8157",
            "2001 WL 473736"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Pace, Anthony Besase, Christ Savides, Donald Smith, John Cialoni, and Robert Wilson",
          "cluster_id": 538544,
          "cite": [
            "898 F.2d 1218",
            "1990 U.S. App. LEXIS 3831"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin C. Reilly",
          "cluster_id": 713016,
          "cite": [
            "76 F.3d 1271",
            "1996 U.S. App. LEXIS 2078",
            "1996 WL 56684"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Elkins Carol Elkins, United States of America v. Carol Elkins James Elkins",
          "cluster_id": 778775,
          "cite": [
            "300 F.3d 638"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Young",
          "cluster_id": 1275885,
          "cite": [
            "957 P.2d 681"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Mierz",
          "cluster_id": 1255546,
          "cite": [
            "901 P.2d 286",
            "127 Wash. 2d 460"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jordan v. State",
          "cluster_id": 1666213,
          "cite": [
            "728 So. 2d 1088",
            "1998 WL 800121"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Basher",
          "cluster_id": 183144,
          "cite": [
            "629 F.3d 1161",
            "2011 U.S. App. LEXIS 1064",
            "2011 WL 167045"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Robinson",
          "cluster_id": 3152697,
          "cite": [
            "303 Kan. 11",
            "363 P.3d 875",
            "2015 Kan. LEXIS 929"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Talkington",
          "cluster_id": 2784485,
          "cite": [
            "301 Kan. 453",
            "345 P.3d 258",
            "2015 Kan. LEXIS 167",
            "2015 WL 968451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Bullock",
          "cluster_id": 883585,
          "cite": [
            "901 P.2d 61",
            "272 Mont. 361",
            "52 State Rptr. 717",
            "1995 Mont. LEXIS 163"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Perea-Rey",
          "cluster_id": 801335,
          "cite": [
            "680 F.3d 1179",
            "2012 U.S. App. LEXIS 10941",
            "2012 WL 1948973"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Dunn:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111833 OR 9430862 OR 9430863 OR 9430864) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzM0MTAyNDAwMDAwJnM9NjI3MTYyJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111833+OR+9430862+OR+9430863+OR+9430864%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111833 OR 9430862 OR 9430863 OR 9430864)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDImcz03NzM4NSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111833+OR+9430862+OR+9430863+OR+9430864%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111833 OR 9430862 OR 9430863 OR 9430864)",
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
    "complete_query": "cites:(111833 OR 9430862 OR 9430863 OR 9430864)",
    "indexed_citing_opinions": 779,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111833,
        "count": 660,
        "count_source": "search"
      },
      {
        "opinion_id": 9430862,
        "count": 134,
        "count_source": "search"
      },
      {
        "opinion_id": 9430863,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430864,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1338,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-dunn.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxNTc5MTcmcz0xMDMxMDQ5NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111833+OR+9430862+OR+9430863+OR+9430864%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111833,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 101118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 109032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 111667,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 232365,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 237417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 238889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 263655,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 270626,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 358699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 388191,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 402220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 404175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 421926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 454693,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 463250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 464634,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1175600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1200960,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1227951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1246385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1263323,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1271682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1287214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1326786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1366121,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1391288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1507253,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1518631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1575755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1671337,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 1688103,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 2123323,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 2455959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111833,
        "cited_id": 3839556,
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
    "date_created": "2026-07-05T23:42:59Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:43:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:43:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:49:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:43:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Dunn

```
<opinion type="majority">
<author id="b342-6">Justice White</author>
<p id="ARz">delivered the opinion of the Court.</p>
<p id="b342-7">We granted the Government’s petition for certiorari to decide whether the area near a barn, located approximately 50 yards from a fence surrounding a ranch house, is, for Fourth Amendment purposes, within the curtilage of the house. The Court of Appeals for the Fifth Circuit held that the barn lay within the house’s curtilage, and that the District Court should have suppressed certain evidence obtained as a result of law enforcement officials’ intrusion onto the area immediately surrounding the barn. <span class="citation" data-id="464634"><a href="/opinion/464634/united-states-v-ronald-dale-dunn/" aria-description="Citation for case: United States v. Ronald Dale Dunn">782 F. 2d 1226</a></span> (1986). We conclude that the barn and the area around it lay outside the curtilage of the house, and accordingly reverse the judgment of the Court of Appeals.</p>
<p id="b342-8">I</p>
<p id="b342-9">Respondent Ronald Dale Dunn and a codefendant, Robert Lyle Carpenter, were convicted by a jury of conspiring to manufacture phenylacetone and amphetamine, and to possess amphetamine with intent to distribute, in violation of <span class="citation no-link">21 U. S. C. § 846</span>. Respondent was also convicted of manufacturing these two controlled substances and possessing amphetamine with intent to distribute. The events giving rise to respondent’s apprehension and conviction began in 1980 when agents from the Drug Enforcement Administration (DEA) discovered that Carpenter had purchased large quantities of chemicals and equipment used in the manufacture of amphetamine and phenylacetone. DEA agents obtained warrants from a Texas state judge authorizing installation of miniature electronic transmitter tracking devices, or “beepers,” in an electric hot plate stirrer, a drum of acetic anhy-dride, and a container holding phenylacetic acid, a precursor to phenylacetone. All of these items had been ordered by <page-number citation-index="1" label="297">*297</page-number>Carpenter. On September 3, 1980, Carpenter took possession of the electric hot plate stirrer, but the agents lost the signal from the “beeper” a few days later. The agents were able to track the “beeper” in the container of chemicals, however, from October 27, 1980, until November 5, 1980, on which date Carpenter’s pickup truck, which was carrying the container, arrived at respondent’s ranch. Aerial photographs of the ranch property showed Carpenter’s truck backed up to a barn behind the ranch house. The agents also began receiving transmission signals from the “beeper” in the hot plate stirrer that they had lost in early September and determined that the stirrer was on respondent’s ranch property.</p>
<p id="b343-5">Respondent’s ranch comprised approximately 198 acres and was completely encircled by a perimeter fence. The property also contained several interior fences, constructed mainly of posts and multiple strands of barbed wire. The ranch residence was situated 14 mile from a public road. A fence encircled the residence and a nearby small greenhouse. Two barns were located approximately 50 yards from this fence. The front of the larger of the two barns was enclosed by a wooden fence and had an open overhang. Locked, waist-high gates barred entry into the barn proper, and netting material stretched from the ceiling to the top of the wooden gates.</p>
<p id="b343-6">On the evening of November 5, 1980, law enforcement officials made a warrantless entry onto respondent’s ranch property. A DEA agent accompanied by an officer from the Houston Police Department crossed over the perimeter fence and one interior fence. Standing approximately midway between the residence and the barns, the DEA agent smelled what he believed to be phenylacetic acid, the odor coming from the direction of the barns. The officers approached the smaller of the barns — crossing over a barbed wire fence— and, looking into the bam, observed only empty boxes. The officers then proceeded to the larger barn, crossing another <page-number citation-index="1" label="298">*298</page-number>barbed wire fence as well as a wooden fence that enclosed the front portion of the barn. The officers walked under the barn’s overhang to the locked wooden gates and, shining a flashlight through the netting on top of the gates, peered into the barn. They observed what the DEA agent thought to be a phenylacetone laboratory. The officers did not enter the barn.<footnotemark>1</footnotemark> At this point the officers departed from respondent’s property, but entered it twice more on November 6 to confirm the presence of the phenylacetone laboratory.</p>
<p id="b344-5">On November 6, 1980, at 8:30 p.m., a Federal Magistrate issued a warrant authorizing a search of respondent’s ranch. DEA agents and state law enforcement officials executed the warrant on November 8, 1980.<footnotemark>2</footnotemark> The officers arrested re<page-number citation-index="1" label="299">*299</page-number>spondent and seized chemicals and equipment, as well as bags of amphetamines they discovered in a closet in the ranch house.</p>
<p id="b345-5">The District Court denied respondent’s motion to suppress all evidence seized pursuant to the warrant and respondent and Carpenter were convicted. In a decision rendered in 1982, the Court of Appeals reversed respondent’s conviction. <em>United States </em>v. <em>Dunn, </em><span class="citation" data-id="402220"><a href="/opinion/402220/united-states-v-ronald-dale-dunn-and-robert-lyle-carpenter/" aria-description="Citation for case: United States v. Ronald Dale Dunn and Robert Lyle Carpenter">674 F. 2d 1093</a></span>. The court concluded that the search warrant had been issued based on information obtained during the officers’ unlawful warrantless entry onto respondent’s ranch property and, therefore, all evidence seized pursuant to the warrant should have been suppressed. Underpinning this conclusion was the court’s reasoning that “the barn in question was within the curtilage of the residence and was within the protective ambit of the fourth amendment.” <span class="citation" data-id="402220"><a href="/opinion/402220/united-states-v-ronald-dale-dunn-and-robert-lyle-carpenter/#1100" aria-description="Citation for case: United States v. Ronald Dale Dunn and Robert Lyle Carpenter"><em>Id., </em>at 1100</a></span>. We granted the Government’s petition for certiorari, vacated the judgment of the Court of Appeals, and remanded the case for further consideration in fight of <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U. S. 170</a></span> (1984). <span class="citation" data-id="9041426"><a href="/opinion/9048025/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">467 U. S. 1201</a></span> (1984). On remand, the Court of Appeals reaffirmed its judgment that the evidence seized pursuant to the warrant should have been suppressed, but altered the legal basis supporting this conclusion: the large barn was not within the curtilage of the house, but by standing outside the barn and peering into the structure, the officers nonetheless violated respondent’s “reasonable expectation of privacy in his barn and its contents.” <span class="citation" data-id="454693"><a href="/opinion/454693/united-states-v-ronald-dale-dunn/#886" aria-description="Citation for case: United States v. Ronald Dale Dunn">766 F. 2d 880, 886</a></span> (1985). The Government again filed a petition for certiorari. On January 17, 1986, before this Court acted on the petition, the Court of Appeals recalled and vacated its judgment issued on remand, stating that it would enter a new judgment in due course. <span class="citation multiple-matches"><a href="/c/F.%202d/781/52/">781 F. 2d 52</a></span>. On February 4, 1986, the Court of Appeals reinstated the original opinion rendered in 1982, asserting that “[u]pon studied reflection, we now conclude and hold that the barn was inside the protected curtilage.” <span class="citation" data-id="464634"><a href="/opinion/464634/united-states-v-ronald-dale-dunn/#1227" aria-description="Citation for case: United States v. Ronald Dale Dunn">782 F. 2d, at 1227</a></span>. The Government thereupon submitted a supplement to its petition for certiorari, revising the question pre<page-number citation-index="1" label="300">*300</page-number>sented to whether the barn lay within the curtilage of the house. We granted the petition, <span class="citation multiple-matches"><a href="/c/U.%20S./477/903/">477 U. S. 903</a></span>, and now reverse.</p>
<p id="b346-5">II</p>
<p id="b346-6">The curtilage concept originated at common law to extend to the area immediately surrounding a dwelling house the same protection under the law of burglary as was afforded the house itself. The concept plays a part, however, in interpreting the reach of the Fourth Amendment. <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#59" aria-description="Citation for case: Hester v. United States">265 U. S. 57, 59</a></span> (1924), held that the Fourth Amendment’s protection accorded “persons, houses, papers, and effects” did not extend to the open fields, the Court observing that the distinction between a person’s house and open fields “is as old as the common law. 4 Bl. Comm. 223, 225, 226.”<footnotemark>3</footnotemark></p>
<p id="b346-7">We reaffirmed the holding of <em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">Hester</a></span> </em>in <em>Oliver </em>v. <em>United States, supra. </em>There, we recognized that the Fourth Amendment protects the curtilage of a house and that the extent of the curtilage is determined by factors that bear upon whether an individual reasonably may expect that the area in question should be treated as the home itself. <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#180" aria-description="Citation for case: Oliver v. United States">466 U. S., at 180</a></span>. We identified the central component of this inquiry as whether the area harbors the “intimate activity associated with the ‘sanctity of a man’s home and the privacies of life.’” <em>Ibid, </em>(quoting <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span> (1886)).</p>
<p id="b347-3"><page-number citation-index="1" label="301">*301</page-number>Drawing upon the Court’s own cases and the cumulative experience of the lower courts that have grappled with the task of defining the extent of a home’s curtilage, we believe that curtilage questions should be resolved with particular reference to four factors: the proximity of the area claimed to be curtilage to the home, whether the area is included within an enclosure surrounding the home, the nature of the uses to which the area is put, and the steps taken by the resident to protect the area from observation by people passing by. See <em>California </em>v. <em>Ciraolo, </em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#221" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207, 221</a></span> (1986) (Powell, J., dissenting) (citing <em>Care </em>v. <em>United States, </em><span class="citation" data-id="238889"><a href="/opinion/238889/orval-care-v-united-states/#25" aria-description="Citation for case: Orval Care v. United States">231 F. 2d 22, 25</a></span> (CA10), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./351/932/">351 U. S. 932</a></span> (1956); <em>United States </em>v. <em>Van Dyke, </em><span class="citation" data-id="388191"><a href="/opinion/388191/united-states-v-larry-g-van-dyke/#993" aria-description="Citation for case: United States v. Larry G. Van Dyke">643 F. 2d 992, 993-994</a></span> (CA4 1981)).<footnotemark>4</footnotemark> We do not suggest that combining these factors produces a finely tuned formula that, when mechanically applied, yields a “correct” answer to all extent-of-curtilage questions. Rather, these factors are useful analytical tools only to the degree that, in any given case, they bear upon the centrally relevant consideration — whether the area in question is so intimately tied to the home itself that it should be placed under the home’s “umbrella” of Fourth Amendment protection. Applying these factors to respondent’s barn and to the area immediately surrounding it, we have little difficulty in concluding that this area lay outside the curtilage of the ranch house.</p>
<p id="b348-4"><page-number citation-index="1" label="302">*302</page-number><em>First. </em>The record discloses that the barn was located 50 yards from the fence surrounding the house and 60 yards from the house itself. <span class="citation" data-id="454693"><a href="/opinion/454693/united-states-v-ronald-dale-dunn/#882" aria-description="Citation for case: United States v. Ronald Dale Dunn">766 F. 2d, at 882-883</a></span>; <span class="citation" data-id="464634"><a href="/opinion/464634/united-states-v-ronald-dale-dunn/#1228" aria-description="Citation for case: United States v. Ronald Dale Dunn">782 F. 2d, at 1228</a></span>. Standing in isolation, this substantial distance supports no inference that the barn should be treated as an adjunct of the house.</p>
<p id="b348-5"><em>Second. </em>It is also significant that respondent’s barn did not lie within the area surrounding the house that was enclosed by a fence. We noted in <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver, supra,</a></span> </em>that “for most homes, the boundaries of the curtilage will be clearly marked; and the conception defining the curtilage — as the area around the home to which the activity of home life extends —is a familiar one easily understood from our daily experience.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#182" aria-description="Citation for case: Oliver v. United States">466 U. S., at 182, n. 12</a></span>. Viewing the physical layout of respondent’s ranch in its entirety, see <span class="citation" data-id="464634"><a href="/opinion/464634/united-states-v-ronald-dale-dunn/#1228" aria-description="Citation for case: United States v. Ronald Dale Dunn">782 F. 2d, at 1228</a></span>, it is plain that the fence surrounding the residence serves to demark a specific area of land immediately adjacent to the house that is readily identifiable as part and parcel of the house. Conversely, the barn — the front portion itself enclosed by a fence — and the area immediately surrounding it, stands out as a distinct portion of respondent’s ranch, quite separate from the residence.</p>
<p id="b348-6"><em>Third. </em>It is especially significant that the law enforcement officials possessed objective data indicating that the barn was not being used for intimate activities of the home. The aerial photographs showed that the truck Carpenter had been driving that contained the container of phenylacetic acid was backed up to the barn, “apparently,” in the words of the Court of Appeals, “for the unloading of its contents.” <span class="citation" data-id="402220"><a href="/opinion/402220/united-states-v-ronald-dale-dunn-and-robert-lyle-carpenter/#1096" aria-description="Citation for case: United States v. Ronald Dale Dunn and Robert Lyle Carpenter">674 F. 2d, at 1096</a></span>. When on respondent’s property, the officers’ suspicion was further directed toward the barn because of “a very strong odor” of phenylacetic acid. App. 15. As the DEA agent approached the barn, he “could hear a motor running, like a pump motor of some sort . . . .” <em>Id., at </em>17. Furthermore, the officers detected an “extremely strong” odor of phenylacetic acid coming from a small crack in the <page-number citation-index="1" label="303">*303</page-number>wall of the barn. <em>Ibid. </em>Finally, as the officers were standing in front of the barn, immediately prior to looking into its interior through the netting material, “the smell was very, very strong . . . [and the officers] could hear the motor running very loudly.” <em>Id., </em>at 18. When considered together, the above facts indicated to the officers that the use to which the barn was being put could not fairly be characterized as so associated with the activities and privacies of domestic life that the officers should have deemed the barn as part of respondent’s home.</p>
<p id="b349-6"><em>Fourth. </em>Respondent did little to protect the barn area from observation by those standing in the open fields. Nothing in the record suggests that the various interior fences on respondent’s property had any function other than that of the typical ranch fence; the fences were designed and constructed to corral livestock, not to prevent persons from observing what lay inside the enclosed areas.</p>
<p id="b349-7">l — l HH 1 — I</p>
<p id="b349-1">Respondent submits an alternative basis for affirming the judgment below, one that was presented to but ultimately not relied upon by the Court of Appeals. Respondent asserts that he possessed an expectation of privacy, independent from his home’s curtilage, in the barn and its contents, because the barn is an essential part of his business. Brief for Respondent 9. Respondent overlooks the significance of <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U. S. 170</a></span> (1984).</p>
<p id="b349-2">We may accept, for the sake of argument, respondent’s submission that his barn enjoyed Fourth Amendment protection and could not be entered and its contents seized without a warrant. But it does not follow on the record before us that the officers’ conduct and the ensuing search and seizure violated the Constitution. <em>Oliver </em>reaffirmed the precept, established in <em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">Hester</a></span>, </em>that an open field is neither a “house” nor an “effect,” and, therefore, “the government’s intrusion upon the open fields is not one of those ‘unreasonable searches’ <page-number citation-index="1" label="304">*304</page-number>proscribed by the text of the Fourth Amendment.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#177" aria-description="Citation for case: Oliver v. United States">466 U. S., at 177</a></span>. The Court expressly rejected the argument that the erection of fences on an open field — at least of the variety involved in those cases and in the present case — creates a constitutionally protected privacy interest. <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#182" aria-description="Citation for case: Oliver v. United States"><em>Id., </em>at 182-183</a></span>. “[T]he term ‘open fields’ may include any unoccupied or undeveloped area outside of the curtilage. An open field need be neither ‘open’ nor a ‘field’ as those terms are used in common speech.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#180" aria-description="Citation for case: Oliver v. United States"><em>Id., </em>at 180, n. 11</a></span>. It follows that no constitutional violation occurred here when the officers crossed over respondent’s ranch-style perimeter fence, and over several similarly constructed interior fences, prior to stopping at the locked front gate of the barn. As previously mentioned, the officers never entered the barn, nor did they enter any other structure on respondent’s premises. Once at their vantage point, they merely stood, outside the curti-lage of the house and in the open fields upon which the barn was constructed, and peered into the barn’s open front. And, standing as they were in the open fields, the Constitution did not forbid them to observe the phenylacetone laboratory located in respondent’s barn. This conclusion flows naturally from our previous decisions.</p>
<p id="b350-5">Under <em>Oliver </em>and <em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">Hester</a></span>, </em>there is no constitutional difference between police observations conducted while in a public place and while standing in the open fields. Similarly, the fact that the objects observed by the officers lay within an area that we have assumed, but not decided, was protected by the Fourth Amendment does not affect our conclusion. Last Term, in <em>California </em>v. <em>Ciraolo, </em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207</a></span> (1986), we held that warrantless naked-eye aerial observation of a home’s curtilage did not violate the Fourth Amendment. We based our holding on the premise that the Fourth Amendment “has never been extended to require law enforcement officers to shield their eyes when passing by a home on public thoroughfares.” <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#213" aria-description="Citation for case: California v. Ciraolo"><em>Id., </em>at 213</a></span>. Importantly, we deemed it irrelevant that the police observation at issue <page-number citation-index="1" label="305">*305</page-number>was directed specifically at the identification of marijuana plants growing on an area protected by the Fourth Amendment. <em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ibid.</a></span> </em>Finally, the plurality opinion in <em>Texas </em>v. <em>Brown, </em><span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#739" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 739-740</a></span> (1983), notes that it is “beyond dispute” that the action of a police officer in shining his flashlight to illuminate the interior of a car, without probable cause to search the car, “trenched upon no right secured . . . by the Fourth Amendment.” The holding in <em>United States </em>v. <em>Lee, </em><span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/#563" aria-description="Citation for case: United States v. Lee">274 U. S. 559, 563</a></span> (1927) is of similar import. Here, the officers’ use of the beam of a flashlight, directed through the essentially open front of respondent’s barn, did not transform their observations into an unreasonable search within the meaning of Fourth Amendment.</p>
<p id="b351-5">The officers lawfully viewed the interior of respondent’s barn, and their observations were properly considered by the Magistrate in issuing a search warrant for respondent’s premises. Accordingly, the judgment of the Court of Appeals is reversed.</p>
<p id="b351-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b344-6"> In denying respondent’s motion to suppress all evidence obtained as a result of the search warrant, the District Court Judge stated that the law enforcement officials, during their incursions onto respondent’s property, “did not invade the premises, that is, the houses or the barns . . . .” Tr. 216. The Court of Appeals did not disturb this finding. At the suppression hearing, the DEA agent described the officers’ approach to the large barn on November 5:</p>
<p id="b344-7">“A. We came back around, we crossed a small wooden type fence here, which put us right underneath a type of a tin overhang and in front of us was a wooden locked gate ....</p>
<p id="b344-8">“Q. How high was that gate?</p>
<p id="b344-9">“A. It probably came up to my waist, estimated.</p>
<p id="b344-10">“Q. Was that gate open or shut?</p>
<p id="b344-11">“A. It was shut and it was locked.</p>
<p id="b344-12">“Q. Was there anything above that gate?</p>
<p id="b344-13">“A. Yes, there was.</p>
<p id="b344-14">“Q. What was that?</p>
<p id="b344-15">“A. A fish netting, kind of a netting, that was hanging from the ceiling down to the gate.</p>
<p id="b344-16">“Q. Did you cross over that gate and go into the barn?</p>
<p id="b344-17">“A. No.</p>
<p id="b344-18">“Q. Did you stand outside the gate?</p>
<p id="b344-19">“A. We stood right at the gate.”</p>
<p id="b344-20">App. 17-18.</p>
</footnote>
<footnote label="2">
<p id="b344-21"> Prior to the actual search of the barn and ranch house, the agents entered the property for further observations.</p>
</footnote>
<footnote label="3">
<p id="b346-8"> In the section of Blaekstone’s Commentaries which the Court cited, Blackstone described the elements of common-law burglary, and elaborated on the element that a breaking occur in a mansion or dwelling house. In defining the terms “mansion or dwelling-house,” Blackstone wrote that “no distant barn, warehouse, or the like are under the same privileges, nor looked upon as a man’s castle of defence . . . .” 4 W. Blackstone, Commentaries *225. Blackstone observed, however, that “if the barn, stable, or warehouse, be parcel of the mansion-house, and within the same common fence, though not under the same roof or contiguous, a burglary may be committed therein; for the capital house protects and privileges all its branches and appurtenances, if within the curtilage or homestall.” <em><span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/" aria-description="Citation for case: United States v. Lee">Ibid.</a></span></em></p>
</footnote>
<footnote label="4">
<p id="b347-4"> We decline the Government’s invitation to adopt a “bright-line rule” that “the curtilage should extend no farther than the nearest fence surrounding a fenced house.” Brief for United States 14. Fencing configurations are important factors in defining the curtilage, see <em>infra, </em>at 302, but, as we emphasize above, the primary focus is whether the area in question harbors those intimate activities associated with domestic life and the privacies of the home. Application of the Government’s “first fence rule” might well lead to diminished Fourth Amendment protection in those cases where a structure lying outside a home’s enclosing fence was used for such domestic activities. And, in those cases where a house is situated on a large parcel of property and has no nearby enclosing fence, the Government’s rule would serve no utility; a court would still be required to assess the various factors outlined above to define the extent of the curtilage.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Edwards.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Edwards"
type: case
citation: "415 U.S. 800 (1974)"
parallel_cite: "94 S. Ct. 1234; 39 L. Ed. 2d 771"
neutral_cite: 1974 U.S. LEXIS 120
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1974
date_decided: 1974-03-26
docket: 73-88
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1974-03-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Edwards
  varies_by_point: false
  scope_note: "Still controlling on the timing of a search incident to arrest: effects subject to search at arrest may be seized at the jail after a reasonable delay."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108995/united-states-v-edwards/"
  cluster_id: 108995
  opinion_id: 108995
  identity_checked: true
homes:
  - page: "[[SIA Persons]]"
    role: "Progeny"
related: ["[[United States v. Robinson]]", "[[Chimel v. California]]", "[[Abel v. United States]]", "[[Illinois v. Lafayette]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "custodial-arrest", "booking"]
holding: "A search incident to arrest may extend in time: clothing and effects in an arrestee's possession that were subject to search at the time of arrest may be seized and examined without a warrant at the jail, even after a substantial, reasonable delay."
lake:
  record_id: United States v. Edwards
  status: verified
  projected_at: 2026-07-06
---

# United States v. Edwards

*415 U.S. 800 (1974)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Edwards was lawfully arrested shortly after 11 p.m. for attempting to break into a post office and was jailed. Investigation at the scene revealed the entry had been pried open, leaving paint chips. The next morning, substitute clothing was purchased for Edwards; his own clothing — worn at and since the arrest, about 10 hours earlier — was then taken and held as evidence. Laboratory examination revealed paint chips matching the window. Edwards objected that the warrantless seizure of his clothing violated the Fourth Amendment.

## Issue
Does the Fourth Amendment bar the warrantless seizure of an arrestee's clothing at the jail roughly 10 hours after his arrest, once the administrative mechanics of arrest are complete and the prisoner is incarcerated?

## Rule
No. Searches and seizures "that could be made on the spot at the time of arrest may legally be conducted later when the accused arrives at the place of detention." — 415 U.S. at 803. ^pin-803

More broadly, "once the accused is lawfully arrested and is in custody, the effects in his possession at the place of detention that were subject to search at the time and place of his arrest may lawfully be searched and seized without a warrant even though a substantial period of time has elapsed between the arrest and subsequent administrative processing . . . and the taking of the property for use as evidence." — *Id.* at 807. ^pin-807

The legal arrest "does — for at least a reasonable time and to a reasonable extent — take [the arrestee's] own privacy out of the realm of protection from police interest in weapons, means of escape, and evidence." — *Id.* at 808–09 (quoting *United States v. DeLeo*). ^pin-808

## Application
Edwards was lawfully arrested, and the police were entitled to seize the clothing in his immediate possession as evidence of the crime; probable cause linked the clothing to the burglary. They could have taken it the night of the arrest, but it was late, no substitute clothing was available, and it would have been unreasonable to strip him and leave him exposed in his cell overnight. Waiting until morning, when substitutes were purchased, was a reasonable delay in effectuating a normal incident of custodial arrest; the lapse of time did not render the warrantless seizure unreasonable.

## Conclusion
The warrantless seizure and examination of Edwards' clothing were valid; the Court of Appeals was reversed. The Court did not hold that the Warrant Clause is never applicable to post-arrest seizures of an arrestee's effects.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Edwards* remains the controlling authority that a [[Search Incident to Arrest|search incident to arrest]] may extend in time — effects subject to search at arrest may be seized and examined at the place of detention after a reasonable delay. It builds on [[United States v. Robinson]] and [[Chimel v. California]] and is paired with station-house cases like [[Illinois v. Lafayette]]. No negative treatment.

## Appears on
- [[SIA Persons]] — *Progeny*

## Sources
- *United States v. Edwards*, 415 U.S. 800 (1974) — https://www.courtlistener.com/opinion/108995/united-states-v-edwards/ — pinpoints: 803, 807, 808–809.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f69f7eea540dd980", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Edwards"}, "payload": {"all": [{"cite": "415 U.S. 800", "page": "800", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "415"}, {"cite": "94 S. Ct. 1234", "page": "1234", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "94"}, {"cite": "39 L. Ed. 2d 771", "page": "771", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "39"}, {"cite": "1974 U.S. LEXIS 120", "page": "120", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1974"}], "display": "415 U.S. 800", "official": {"cite": "415 U.S. 800", "page": "800", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "415"}, "official_selection_present": true, "record_id": "United States v. Edwards"}}
{"assertion_id": "7ae747bda1af71d1", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-808", "record_id": "United States v. Edwards"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-808", "pinpoint_status": "slip-only", "quote": "does — for at least a reasonable time and to a reasonable extent — take [the arrestee's] own privacy out of the realm of protection from police interest in weapons, means of escape, and evidence.", "quote_fidelity": "mismatch", "record_id": "United States v. Edwards", "star_marker": null}}
{"assertion_id": "823a0dd55db502da", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-803", "record_id": "United States v. Edwards"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-803", "pinpoint_status": "slip-only", "quote": "--- # United States v. Edwards *415 U.S. 800 (1974)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Edwards was lawfully arrested shortly after 11 p.m. for attempting to break into a post office and was jailed. Investigation at the scene revealed the entry had been pried open, leaving paint chips. The next morning, substitute clothing was purchased for Edwards; his own clothing — worn at and since the arrest, about 10 hours earlier — was then taken and held as evidence. Laboratory examination revealed paint chips matching the window. Edwards objected that the warrantless seizure of his clothing violated the Fourth Amendment. ## Issue Does the Fourth Amendment bar the warrantless seizure of an arrestee's clothing at the jail roughly 10 hours after his arrest, once the administrative mechanics of arrest are complete and the prisoner is incarcerated? ## Rule No. Searches and seizures", "quote_fidelity": "mismatch", "record_id": "United States v. Edwards", "star_marker": null}}
{"assertion_id": "b1a84bccf2a82774", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-807", "record_id": "United States v. Edwards"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-807", "pinpoint_status": "slip-only", "quote": "once the accused is lawfully arrested and is in custody, the effects in his possession at the place of detention that were subject to search at the time and place of his arrest may lawfully be searched and seized without a warrant even though a substantial period of time has elapsed between the arrest and subsequent administrative processing . . . and the taking of the property for use as evidence.", "quote_fidelity": "mismatch", "record_id": "United States v. Edwards", "star_marker": null}}
{"assertion_id": "cac1bb8ef545e490", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Edwards"}, "payload": {"as_of_content": "1974-03-26", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Edwards", "scope_note": "Still controlling on the timing of a search incident to arrest: effects subject to search at arrest may be seized at the jail after a reasonable delay.", "varies_by_point": false}}
```

### lake record — United States v. Edwards

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Edwards",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Edwards",
    "case_name_short": "Edwards",
    "case_name_full": "UNITED STATES v. EDWARDS Et Al.",
    "input_case_name": "United States v. Edwards",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1974-03-26",
    "year": 1974,
    "docket": "73-88",
    "cluster_id": 108995,
    "lead_opinion_id": 108995,
    "sibling_ids": [
      108995,
      9425658,
      9425659
    ],
    "absolute_url": "/opinion/108995/united-states-v-edwards/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "415 U.S. 800",
      "volume": "415",
      "reporter": "U.S.",
      "page": "800",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "94 S. Ct. 1234",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "1234",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "39 L. Ed. 2d 771",
        "volume": "39",
        "reporter": "L. Ed. 2d",
        "page": "771",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1974 U.S. LEXIS 120",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "120",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "415 U.S. 800",
        "volume": "415",
        "reporter": "U.S.",
        "page": "800",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 S. Ct. 1234",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "1234",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "39 L. Ed. 2d 771",
        "volume": "39",
        "reporter": "L. Ed. 2d",
        "page": "771",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1974 U.S. LEXIS 120",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "120",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "415 U.S. 800",
    "official_selection": {
      "court_class": "scotus",
      "selected": "415 U.S. 800",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-803",
      "page": null,
      "quote": "--- # United States v. Edwards *415 U.S. 800 (1974)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Edwards was lawfully arrested shortly after 11 p.m. for attempting to break into a post office and was jailed. Investigation at the scene revealed the entry had been pried open, leaving paint chips. The next morning, substitute clothing was purchased for Edwards; his own clothing \u2014 worn at and since the arrest, about 10 hours earlier \u2014 was then taken and held as evidence. Laboratory examination revealed paint chips matching the window. Edwards objected that the warrantless seizure of his clothing violated the Fourth Amendment. ## Issue Does the Fourth Amendment bar the warrantless seizure of an arrestee's clothing at the jail roughly 10 hours after his arrest, once the administrative mechanics of arrest are complete and the prisoner is incarcerated? ## Rule No. Searches and seizures",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-807",
      "page": null,
      "quote": "once the accused is lawfully arrested and is in custody, the effects in his possession at the place of detention that were subject to search at the time and place of his arrest may lawfully be searched and seized without a warrant even though a substantial period of time has elapsed between the arrest and subsequent administrative processing . . . and the taking of the property for use as evidence.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-808",
      "page": null,
      "quote": "does \u2014 for at least a reasonable time and to a reasonable extent \u2014 take [the arrestee's] own privacy out of the realm of protection from police interest in weapons, means of escape, and evidence.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1974-03-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Edwards",
    "varies_by_point": false,
    "scope_note": "Still controlling on the timing of a search incident to arrest: effects subject to search at arrest may be seized at the jail after a reasonable delay.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Rosario-Santiago",
          "cluster_id": 4666565,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane1_negative"
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
        "journal_ref": "United States v. Edwards:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Tremblay",
          "cluster_id": 4428704,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Matter of Jamal S.",
          "cluster_id": 2757696,
          "cite": [
            "123 A.D.3d 429",
            "999 N.Y.S.2d 7"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Douglas A. Guilmette v. State of Indiana",
          "cluster_id": 2718767,
          "cite": [
            "14 N.E.3d 38",
            "2014 WL 3953636",
            "2014 Ind. LEXIS 650"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Oles v. State",
          "cluster_id": 1722157,
          "cite": [
            "965 S.W.2d 641",
            "1998 Tex. App. LEXIS 1367",
            "1998 WL 95098"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Contreras v. State",
          "cluster_id": 1747151,
          "cite": [
            "838 S.W.2d 594",
            "1992 WL 142198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane1_negative"
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
        "journal_ref": "United States v. Edwards:lane1_negative"
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
        "journal_ref": "United States v. Edwards:lane2_top_cited"
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
        "journal_ref": "United States v. Edwards:lane2_top_cited"
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
        "journal_ref": "United States v. Edwards:lane2_top_cited"
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
        "journal_ref": "United States v. Edwards:lane2_top_cited"
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
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Lafayette",
          "cluster_id": 110976,
          "cite": [
            "77 L. Ed. 2d 65",
            "103 S. Ct. 2605",
            "462 U.S. 640",
            "1983 U.S. LEXIS 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
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
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oles v. State",
          "cluster_id": 1762668,
          "cite": [
            "993 S.W.2d 103",
            "1999 Tex. Crim. App. LEXIS 53",
            "1999 WL 330266"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Bible",
          "cluster_id": 1154894,
          "cite": [
            "858 P.2d 1152",
            "175 Ariz. 549",
            "145 Ariz. Adv. Rep. 3",
            "1993 Ariz. LEXIS 73"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Young v. State",
          "cluster_id": 1860086,
          "cite": [
            "283 S.W.3d 854",
            "2009 Tex. Crim. App. LEXIS 979",
            "2009 WL 1066912"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Johns",
          "cluster_id": 111305,
          "cite": [
            "83 L. Ed. 2d 890",
            "105 S. Ct. 881",
            "469 U.S. 478",
            "1985 U.S. LEXIS 45",
            "53 U.S.L.W. 4126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McGee v. State",
          "cluster_id": 1960022,
          "cite": [
            "105 S.W.3d 609",
            "2003 Tex. Crim. App. LEXIS 75",
            "2003 WL 1918091"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carmine Tramunti",
          "cluster_id": 326798,
          "cite": [
            "513 F.2d 1087"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
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
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Menotti v. City of Seattle",
          "cluster_id": 3032002,
          "cite": [
            "409 F.3d 1113",
            "2005 WL 1300994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Caraher",
          "cluster_id": 1188275,
          "cite": [
            "653 P.2d 942",
            "293 Or. 741",
            "1982 Ore. LEXIS 1190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ernest Raymond Basurto",
          "cluster_id": 319510,
          "cite": [
            "497 F.2d 781"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bruce Carneil Webster, A/K/A B-Love",
          "cluster_id": 759707,
          "cite": [
            "162 F.3d 308"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Russell v. State",
          "cluster_id": 1505440,
          "cite": [
            "665 S.W.2d 771",
            "1983 Tex. Crim. App. LEXIS 1111"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marquez v. State",
          "cluster_id": 2391915,
          "cite": [
            "725 S.W.2d 217",
            "1987 Tex. Crim. App. LEXIS 500"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tommie T. Childs",
          "cluster_id": 776249,
          "cite": [
            "277 F.3d 947",
            "2002 U.S. App. LEXIS 760",
            "2002 WL 63798"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hill",
          "cluster_id": 1388061,
          "cite": [
            "528 P.2d 1",
            "12 Cal. 3d 731",
            "117 Cal. Rptr. 393"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Swain v. Spinney",
          "cluster_id": 197434,
          "cite": [
            "117 F.3d 1",
            "1997 WL 339126"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carl Bailey",
          "cluster_id": 410253,
          "cite": [
            "691 F.2d 1009"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Nuccio",
          "cluster_id": 1088486,
          "cite": [
            "454 So. 2d 93"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108995 OR 9425658 OR 9425659) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MDgzMDcyMDAwMDAmcz0xNDQ3MzcyJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108995+OR+9425658+OR+9425659%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108995 OR 9425658 OR 9425659)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzgmcz0xMTg1ODc5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108995+OR+9425658+OR+9425659%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108995 OR 9425658 OR 9425659)",
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
    "complete_query": "cites:(108995 OR 9425658 OR 9425659)",
    "indexed_citing_opinions": 600,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108995,
        "count": 546,
        "count_source": "search"
      },
      {
        "opinion_id": 9425658,
        "count": 68,
        "count_source": "search"
      },
      {
        "opinion_id": 9425659,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 917,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-edwards.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY0Nzg5Njgmcz00NjY2NTY1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108995+OR+9425658+OR+9425659%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108995,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 104314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 108288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 237906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 250962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 252159,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 265378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 268259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 271127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 272209,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 272272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 272441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 272841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 274387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 276677,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 277074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 278241,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 280000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 285514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 285576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 286531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 288700,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 290365,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 301119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 308901,
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
    "date_created": "2026-07-05T23:49:51Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:50:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:50:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:53:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:50:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Edwards

```
<div>
<center><b><span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/" aria-description="Citation for case: United States v. Edwards">415 U.S. 800</a></span> (1974)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
EDWARDS ET AL.</h1></center>
<center>No. 73-88.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 15, 1974.</center>
<center>Decided March 26, 1974.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SIXTH CIRCUIT.
<p><span class="star-pagination">*801</span> <i>Edward R. Korman</i> argued the cause for the United States. With him on the brief were <i>Solicitor General Bork, Assistant Attorney General Petersen,</i> and <i>Jerome M. Feit.</i></p>
<p><i>Thomas R. Smith,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1125/">414 U. S. 1125</a></span>, argued the cause and filed a brief for respondents.<sup>[*]</sup></p>
<p>MR. JUSTICE WHITE delivered the opinion of the Court.</p>
<p>The question here is whether the Fourth Amendment should be extended to exclude from evidence certain clothing taken from respondent Edwards while he was in custody at the city jail approximately 10 hours after his arrest.</p>
<p>Shortly after 11 p. m. on May 31, 1970, respondent Edwards was lawfully arrested on the streets of Lebanon, Ohio, and charged with attempting to break into that city's Post Office.<sup>[1]</sup> He was taken to the local jail and placed in a cell. Contemporaneously or shortly thereafter, investigation at the scene revealed that the attempted entry had been made through a wooden window which apparently had been pried up with a pry bar, leaving paint chips on the window sill and wire mesh <span class="star-pagination">*802</span> screen. The next morning, trousers and a T-shirt were purchased for Edwards to substitute for the clothing which he had been wearing at the time of and since his arrest. His clothing was then taken from him and held as evidence. Examination of the clothing revealed paint chips matching the samples that had been taken from the window. This evidence and his clothing were received at trial over Edwards' objection that neither the clothing nor the results of its examination were admissible because the warrantless seizure of his clothing was invalid under the Fourth Amendment.</p>
<p>The Court of Appeals reversed. Expressly disagreeing with two other Courts of Appeals,<sup>[2]</sup> it held that although the arrest was lawful and probable cause existed to believe that paint chips would be discovered on respondent's clothing, the warrantless seizure of the clothing carried out "after the administrative process and the mechanics of the arrest have come to a halt" was nevertheless unconstitutional under the Fourth Amendment. <span class="citation" data-id="308901"><a href="/opinion/308901/united-states-v-eugene-howard-edwards/#1211" aria-description="Citation for case: United States v. Eugene Howard Edwards">474 F. 2d 1206, 1211</a></span> (CA6 1973). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./414/818/">414 U. S. 818</a></span>, and now conclude that the Fourth Amendment should not be extended to invalidate the search and seizure in the circumstances of this case.</p>
<p>The prevailing rule under the Fourth Amendment that searches and seizures may not be made without a warrant is subject to various exceptions. One of them permits warrantless searches incident to custodial arrests, <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973); <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#755" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 755</a></span> (1969); <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span> (1914), and has traditionally been justified by the reasonableness of searching for weapons, instruments of escape, and evidence of crime <span class="star-pagination">*803</span> when a person is taken into official custody and lawfully detained. <i>United States</i> v. <i><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson, supra.</a></span></i><sup></sup>[3]</p>
<p>It is also plain that searches and seizures that could be made on the spot at the time of arrest may legally be conducted later when the accused arrives at the place of detention. If need be, <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span> (1960), settled this question. There the defendant was arrested at his hotel, but the belongings taken with him to the place of detention were searched there. In sustaining the search, the Court noted that a valid search of the property could have been made at the place of arrest and perceived little difference</p>
<blockquote>"when the accused decides to take the property with him, for the search of it to occur instead at the first place of detention when the accused arrives there, especially as the search of property carried by an accused to the place of detention has additional justifications, similar to those which justify a search of the person of one who is arrested." <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#239" aria-description="Citation for case: Abel v. United States"><i>Id.,</i> at 239</a></span>.</blockquote>
<p>The courts of appeals have followed this same rule, holding that both the person and the property in his immediate possession may be searched at the station house after the arrest has occurred at another place and if evidence of crime is discovered, it may be seized and admitted in evidence.<sup>[4]</sup> Nor is there any doubt <span class="star-pagination">*804</span> that clothing or other belongings may be seized upon arrival of the accused at the place of detention and later subjected to laboratory analysis or that the test results are admissible at trial.<sup>[5]</sup></p>
<p>Conceding all this, the Court of Appeals in this case nevertheless held that a warrant is required where the search occurs after the administrative mechanics of arrest have been completed and the prisoner is incarcerated. But even on these terms, it seems to us that the normal processes incident to arrest and custody had not been completed when Edwards was placed in his cell on the night of May 31. With or without probable cause, the authorities were entitled at that point not only to search Edwards' clothing but also to take it from him and keep it in official custody. There was testimony that this was the standard practice in this city.<sup>[6]</sup> The police <span class="star-pagination">*805</span> were also entitled to take from Edwards any evidence of the crime in his immediate possession, including his clothing. And the Court of Appeals acknowledged that contemporaneously with or shortly after the time Edwards went to his cell, the police had probable cause to believe that the articles of clothing he wore were themselves material evidence of the crime for which he had been arrested. <span class="citation" data-id="308901"><a href="/opinion/308901/united-states-v-eugene-howard-edwards/#1210" aria-description="Citation for case: United States v. Eugene Howard Edwards">474 F. 2d, at 1210</a></span>. But it was late at night; no substitute clothing was then available for Edwards to wear, and it would certainly have been unreasonable for the police to have stripped respondent of his clothing and left him exposed in his cell throughout the night. Cf. <i>United States</i> v. <i>Caruso,</i> <span class="citation" data-id="271127"><a href="/opinion/271127/united-states-v-ciro-michael-caruso/#185" aria-description="Citation for case: United States v. Ciro Michael Caruso">358 F. 2d 184, 185-186</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./385/862/">385 U. S. 862</a></span> (1966). When the substitutes were purchased the next morning, the clothing he had been wearing at the time of arrest was taken from him and subjected to laboratory analysis. This was no more than taking from respondent the effects in his immediate possession that constituted evidence of crime. This was and is a normal incident of a custodial arrest, and reasonable delay in effectuating it does not change the fact that Edwards was no more imposed upon than he could have been at the time and place of the arrest or immediately upon arrival at the place of detention. The police did no more on June 1 than they were entitled to do incident to the usual custodial arrest and incarceration.</p>
<p><span class="star-pagination">*806</span> Other closely related considerations sustain the examination of the clothing in this case. It must be remembered that on both May 31 and June 1 the police had lawful custody of Edwards and necessarily of the clothing he wore. When it became apparent that the articles of clothing were evidence of the crime for which Edwards was being held, the police were entitled to take, examine, and preserve them for use as evidence, just as they are normally permitted to seize evidence of crime when it is lawfully encountered. <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969); <i>Frazier</i> v. <i>Cupp,</i> <span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731</a></span> (1969); <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967); <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963) (plurality opinion); <i>Zap</i> v. <i>United States,</i> <span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/" aria-description="Citation for case: Zap v. United States">328 U. S. 624</a></span> (1946), vacated on other grounds, <span class="citation multiple-matches"><a href="/c/U.%20S./330/800/">330 U. S. 800</a></span> (1947). Surely, the clothes could have been brushed down and vacuumed while Edwards had them on in the cell, and it was similarly reasonable to take and examine them as the police did, particularly in view of the existence of probable cause linking the clothes to the crime. Indeed, it is difficult to perceive what is unreasonable about the police's examining and holding as evidence those personal effects of the accused that they already have in their lawful custody as the result of a lawful arrest.</p>
<p>In <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span> (1967), an accused had been arrested for a narcotics offense and his automobile impounded preparatory to institution of forfeiture proceedings. The car was searched a week later without a warrant and evidence seized that was later introduced at the defendant's criminal trial. The warrantless search and seizure were sustained because they were "closely related to the reason petitioner was arrested, the reason his car had been impounded, and the reason it was being retained. . . . It would be unreasonable to hold that the police, having to retain the car in their <span class="star-pagination">*807</span> custody for such a length of time, had no right, even for their own protection, to search it." <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California"><i>Id.,</i> at 61-62</a></span>. It was no answer to say that the police could have obtained a search warrant, for the Court held the test to be, not whether it was reasonable to procure a search warrant, but whether the search itself was reasonable, which it was. <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#62" aria-description="Citation for case: Cooper v. California"><i>Id.,</i> at 62</a></span>. <i>United States</i> v. <i><span class="citation" data-id="271127"><a href="/opinion/271127/united-states-v-ciro-michael-caruso/" aria-description="Citation for case: United States v. Ciro Michael Caruso">Caruso, supra</a></span></i><i>,</i> expresses similar views. There, defendant's clothes were not taken until six hours after his arrival at a place of detention. The Court of Appeals properly held that no warrant was required:</p>
<blockquote>"He and his clothes were constantly in custody from the moment of his arrest, and the inspection of his clothes and the holding of them for use in evidence were, under the circumstances, reasonable and proper." <span class="citation" data-id="271127"><a href="/opinion/271127/united-states-v-ciro-michael-caruso/#185" aria-description="Citation for case: United States v. Ciro Michael Caruso">358 F. 2d, at 185</a></span> (citations omitted).</blockquote>
<p><i>Caruso</i> is typical of most cases in the courts of appeals that have long since concluded that once the accused is lawfully arrested and is in custody, the effects in his possession at the place of detention that were subject to search at the time and place of his arrest may lawfully be searched and seized without a warrant even though a substantial period of time has elapsed between the arrest and subsequent administrative processing, on the one hand, and the taking of the property for use as evidence, on the other. This is true where the clothing or effects are immediately seized upon arrival at the jail, held under the defendant's name in the "property room" of the jail, and at a later time searched and taken for use at the subsequent criminal trial.<sup>[7]</sup> The result is the <span class="star-pagination">*808</span> same where the property is not physically taken from the defendant until sometime after his incarceration.<sup>[8]</sup></p>
<p>In upholding this search and seizure, we do not conclude that the Warrant Clause of the Fourth Amendment is never applicable to postarrest seizures of the effects of an arrestee.<sup>[9]</sup> But we do think that the Court of Appeals for the First Circuit captured the essence of situations like this when it said in <i>United States</i> v. <i>DeLeo,</i> <span class="citation" data-id="288700"><a href="/opinion/288700/united-states-v-ralph-f-deleo/#493" aria-description="Citation for case: United States v. Ralph F. Deleo">422 F. 2d 487, 493</a></span> (1970) (footnote omitted):</p>
<blockquote>"While the legal arrest of a person should not destroy the privacy of his premises, it doesfor at <span class="star-pagination">*809</span> least a reasonable time and to a reasonable extent take his own privacy out of the realm of protection from police interest in weapons, means of escape, and evidence."</blockquote>
<p>The judgment of the Court of Appeals is reversed.</p>
<p><i>So ordered.</i></p>
<p>MR. JUSTICE STEWART, with whom MR. JUSTICE DOUGLAS, MR. JUSTICE BRENNAN, and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>The Court says that the question before us "is whether the Fourth Amendment should be extended" to prohibit the warrantless seizure of Edwards' clothing. I think, on the contrary, that the real question in this case is whether the Fourth Amendment is to be ignored. For in my view the judgment of the Court of Appeals can be reversed only by disregarding established Fourth Amendment principles firmly embodied in many previous decisions of this Court.</p>
<p>As the Court has repeatedly emphasized in the past, "the most basic constitutional rule in this area is that `searches conducted outside the judicial process, without prior approval by judge or magistrate, are <i>per se</i> unreasonable under the Fourth Amendmentsubject only to a few specifically established and well-delineated exceptions.' " <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#454" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 454-455</a></span>; <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span>. Since it is conceded here that the seizure of Edwards' clothing was not made pursuant to a warrant, the question becomes whether the Government has met its burden of showing that the circumstances of this seizure brought it within one of the "jealously and carefully drawn"<sup>[1]</sup> exceptions to the warrant requirement.</p>
<p><span class="star-pagination">*810</span> The Court finds a warrant unnecessary in this case because of the custodial arrest of the respondent. It is, of course, well settled that the Fourth Amendment permits a warrantless search or seizure incident to a constitutionally valid custodial arrest. <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span>; <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>. But the mere fact of an arrest does not allow the police to engage in warrantless searches of unlimited geographic or temporal scope. Rather, the search must be spatially limited to the person of the arrestee and the area within his reach, <i>Chimel</i> v. <i>California, supra</i><i>,</i> and must, as to time, be "substantially contemporaneous with the arrest," <i>Stoner</i> v. <i>California,</i> <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#486" aria-description="Citation for case: Stoner v. California">376 U. S. 483, 486</a></span>; <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367-368</a></span>.</p>
<p>Under the facts of this case, I am unable to agree with the Court's holding that the search was "incident" to Edwards' custodial arrest. The search here occurred fully 10 hours after he was arrested, at a time when the administrative processing and mechanics of arrest had long since come to an end. His clothes were not seized as part of an "inventory" of a prisoner's effects, nor were they taken pursuant to a routine exchange of civilian clothes for jail garb.<sup>[2]</sup> And the considerations that typically justify a warrantless search incident to a lawful arrest were wholly absent here. As Mr. Justice <span class="star-pagination">*811</span> Black stated for a unanimous Court in <i>Preston</i> v. <i>United States, supra,</i> at 367:</p>
<blockquote>"The rule allowing contemporaneous searches is justified, for example, by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the destruction of evidence of the crimethings which might easily happen where the weapon or evidence is on the accused's person or under his immediate control. But these justifications are absent where a search is remote in time or place from the arrest."<sup>[3]</sup></blockquote>
<p>Accordingly, I see no justification for dispensing with the warrant requirement here. The police had ample time to seek a warrant, and no exigent circumstances were present to excuse their failure to do so. Unless the exceptions to the warrant requirement are to be "enthroned into the rule," <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#80" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 80</a></span> (Frankfurter, J., dissenting), this is precisely the sort of situation where the Fourth Amendment requires a magistrate's prior approval for a search.</p>
<p>The Court says that the relevant question is "not whether it was reasonable to procure a search warrant, but whether the search itself was reasonable." <i>Ante,</i> at 807. Precisely such a view, however, was explicitly rejected in <i>Chimel</i> v. <i>California, supra,</i> at 764-765, where the Court characterized the argument as "founded on little more than a subjective view regarding the acceptability of certain sorts of police conduct, and not on considerations relevant to Fourth Amendment interests." As <span class="star-pagination">*812</span> they were in <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>,</i> the words of Mr. Justice Frank-further are again most relevant here:</p>
<blockquote>"To say that the search must be reasonable is to require some criterion of reason. It is no guide at all either for a jury or for district judges or the police to say that an `unreasonable search' is forbidden that the search must be reasonable. What is the test of reason which makes a search reasonable? The test is the reason underlying and expressed by the Fourth Amendment: the history and the experience which it embodies and the safeguards afforded by it against the evils to which it was a response. There must be a warrant to permit search, barring only inherent limitations upon that requirement when there is a good excuse for not getting a search warrant . . . ." <i>United States</i> v. <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#83" aria-description="Citation for case: United States v. Rabinowitz"><i>Rabinowitz, supra,</i> at 83</a></span> (dissenting opinion).</blockquote>
<p>The intrusion here was hardly a shocking one, and it cannot be said that the police acted in bad faith. The Fourth Amendment, however, was not designed to apply only to situations where the intrusion is massive and the violation of privacy shockingly flagrant. Rather, as the Court's classic admonition in <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 635</a></span>, put the matter:</p>
<blockquote>"It may be that it is the obnoxious thing in its mildest and least repulsive form; but illegitimate and unconstitutional practices get their first footing in that way, namely, by silent approaches and slight deviations from legal modes of procedure. This can only be obviated by adhering to the rule that constitutional provisions for the security of person and property should be liberally construed. A close and literal construction deprives them of half their efficacy, and leads to gradual depreciation of the right, <span class="star-pagination">*813</span> as if it consisted more in sound than in substance. It is the duty of courts to be watchful for the constitutional rights of the citizen, and against any stealthy encroachments thereon."</blockquote>
<p>Because I believe that the Court today unjustifiably departs from well-settled constitutional principles, I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]  <i>Frank G. Carrington, Jr., Wayne W. Schmidt, Fred E. Inbau, Glen Murphy, Paul Keller,</i> and <i>Courtney A. Evans</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging reversal.</p>
<p>[1]  Edwards (hereafter also referred to as respondent) had an alleged confederate, William T. Livesay, who was corespondent in this case, but died after the petition for certiorari was granted. We therefore vacate the judgment as to him and remand the case to the District Court with directions to dismiss the indictment. <i>Durham</i> v. <i>United States,</i> <span class="citation" data-id="9424482"><a href="/opinion/108288/durham-v-united-states/" aria-description="Citation for case: Durham v. United States">401 U. S. 481</a></span> (1971).</p>
<p>[2]  The Court stated that it could not agree with <i>United States</i> v. <i>Williams,</i> <span class="citation" data-id="286531"><a href="/opinion/286531/united-states-v-leslie-edward-williams-joseph-anthony-butera-and/" aria-description="Citation for case: United States v. Leslie Edward Williams, Joseph Anthony...">416 F. 2d 4</a></span> (CA5 1969), and <i>United States</i> v. <i>Caruso,</i> <span class="citation" data-id="271127"><a href="/opinion/271127/united-states-v-ciro-michael-caruso/" aria-description="Citation for case: United States v. Ciro Michael Caruso">358 F. 2d 184</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./385/862/">385 U. S. 862</a></span> (1966).</p>
<p>[3]  "A custodial arrest of a suspect based on probable cause is a reasonable intrusion under the Fourth Amendment; that intrusion being lawful, a search incident to the arrest requires no additional justification. It is the fact of the lawful arrest which establishes the authority to search, and we hold that in the case of a lawful custodial arrest a full search of the person is not only an exception to the warrant requirement of the Fourth Amendment, but is also a `reasonable' search under that Amendment." <i>United States</i> v. <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#235" aria-description="Citation for case: United States v. Robinson"><i>Robinson, supra,</i> at 235</a></span>.</p>
<p>[4]  <i>United States</i> v. <i>Manar,</i> <span class="citation" data-id="301119"><a href="/opinion/301119/united-states-v-lendon-howard-manar/" aria-description="Citation for case: United States v. Lendon Howard Manar">454 F. 2d 342</a></span> (CA7 1971); <i>United States</i> v. <i>Gonzalez-Perez,</i> <span class="citation" data-id="290365"><a href="/opinion/290365/united-states-v-ricardo-antonio-gonzalez-perez-ana-soria-prieto-antonio/" aria-description="Citation for case: United States v. Ricardo Antonio Gonzalez-Perez, Ana...">426 F. 2d 1283</a></span> (CA5 1970); <i>United States</i> v. <i>DeLeo,</i> <span class="citation" data-id="288700"><a href="/opinion/288700/united-states-v-ralph-f-deleo/" aria-description="Citation for case: United States v. Ralph F. Deleo">422 F. 2d 487</a></span> (CA1 1970); <i>United States</i> v. <i><span class="citation" data-id="286531"><a href="/opinion/286531/united-states-v-leslie-edward-williams-joseph-anthony-butera-and/" aria-description="Citation for case: United States v. Leslie Edward Williams, Joseph Anthony...">Williams, supra</a></span></i><i>; </i><i>United States</i> v. <i>Miles,</i> <span class="citation" data-id="285576"><a href="/opinion/285576/united-states-v-jerry-edgar-miles-wilbert-theodore-vaughn-and-george/" aria-description="Citation for case: United States v. Jerry Edgar Miles, Wilbert Theodore...">413 F. 2d 34</a></span> (CA3 1969); <i>Ray</i> v. <i>United States,</i> <span class="citation" data-id="285514"><a href="/opinion/285514/leroy-herbert-ray-v-united-states/" aria-description="Citation for case: Leroy Herbert Ray v. United States">412 F. 2d 1052</a></span> (CA9 1969); <i>Westover</i> v. <i>United States,</i> <span class="citation" data-id="280000"><a href="/opinion/280000/carl-calvin-westover-v-united-states/" aria-description="Citation for case: Carl Calvin Westover v. United States">394 F. 2d 164</a></span> (CA9 1968); <i>United States</i> v. <i>Frankenberry,</i> <span class="citation" data-id="278241"><a href="/opinion/278241/united-states-v-james-robert-frankenberry-jr/" aria-description="Citation for case: United States v. James Robert Frankenberry, Jr.">387 F. 2d 337</a></span> (CA2 1967); <i>Evalt</i> v. <i>United States,</i> <span class="citation" data-id="277074"><a href="/opinion/277074/anton-vaughn-evalt-v-united-states/" aria-description="Citation for case: Anton Vaughn Evalt v. United States">382 F. 2d 424</a></span> (CA9 1967); <i>Malone</i> v. <i>Crouse,</i> <span class="citation" data-id="276677"><a href="/opinion/276677/dick-malone-v-sherman-h-crouse-warden-kansas-state-penitentiary/" aria-description="Citation for case: Dick Malone v. Sherman H. Crouse, Warden, Kansas State...">380 F. 2d 741</a></span> (CA10 1967); <i>Cotton</i> v. <i>United States,</i> <span class="citation" data-id="274387"><a href="/opinion/274387/gary-leland-cotton-v-united-states/" aria-description="Citation for case: Gary Leland Cotton v. United States">371 F. 2d 385</a></span> (CA9 1967); <i>Miller</i> v. <i>Eklund,</i> <span class="citation" data-id="272841"><a href="/opinion/272841/glenn-roy-miller-v-r-l-eklund-etc/" aria-description="Citation for case: Glenn Roy Miller v. R. L. Eklund, Etc.">364 F. 2d 976</a></span> (CA9 1966); <i>Hancock</i> v. <i>Nelson,</i> <span class="citation" data-id="9451942"><a href="/opinion/272441/parker-l-hancock-warden-v-russell-nelson/" aria-description="Citation for case: Parker L. Hancock, Warden v. Russell Nelson">363 F. 2d 249</a></span> (CA1 1966); <i>Golliher</i> v. <i>United States,</i> <span class="citation" data-id="272272"><a href="/opinion/272272/richard-lee-golliher-v-united-states-of-america-harry-richard-holmes-v/" aria-description="Citation for case: Richard Lee Golliher v. United States of America, Harry...">362 F. 2d 594</a></span> (CA8 1966); <i>Rodgers</i> v. <i>United States,</i> <span class="citation" data-id="272209"><a href="/opinion/272209/john-wesley-rodgers-v-united-states/" aria-description="Citation for case: John Wesley Rodgers v. United States">362 F. 2d 358</a></span> (CA8), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./385/993/">385 U. S. 993</a></span> (1966); <i>United States</i> v. <i><span class="citation" data-id="271127"><a href="/opinion/271127/united-states-v-ciro-michael-caruso/" aria-description="Citation for case: United States v. Ciro Michael Caruso">Caruso, supra</a></span></i><i>; </i><i>Whalem</i> v. <i>United States,</i> 120 U. S. App. D. C. 331, <span class="citation" data-id="9450802"><a href="/opinion/268259/thomas-w-whalem-v-united-states/" aria-description="Citation for case: Thomas W. Whalem v. United States">346 F. 2d 812</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./382/862/">382 U. S. 862</a></span> (1965); <i>Grillo</i> v. <i>United States,</i> <span class="citation" data-id="265378"><a href="/opinion/265378/henry-grillo-v-united-states-of-america-saul-glassman-v-united-states-of/" aria-description="Citation for case: Henry Grillo v. United States of America, Saul Glassman...">336 F. 2d 211</a></span> (CA1 1964), cert. denied <i>sub nom. </i><i>Gorin</i> v. <i>United States,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./379/971/">379 U. S. 971</a></span> (1965); <i>Robinson</i> v. <i>United States,</i> 109 U. S. App. D. C. 22, <span class="citation" data-id="252159"><a href="/opinion/252159/james-w-robinson-v-united-states-of-america-thomas-f-dawson-v-united/" aria-description="Citation for case: James W. Robinson v. United States of America, Thomas F....">283 F. 2d 508</a></span> (1960); <i>Baskerville</i> v. <i>United States,</i> <span class="citation" data-id="237906"><a href="/opinion/237906/drury-reinhardt-baskerville-v-united-states/" aria-description="Citation for case: Drury Reinhardt Baskerville v. United States">227 F. 2d 454</a></span> (CA10 1955).</p>
<p>[5]  See, <i>e. g., </i><i>United States</i> v. <i><span class="citation" data-id="271127"><a href="/opinion/271127/united-states-v-ciro-michael-caruso/" aria-description="Citation for case: United States v. Ciro Michael Caruso">Caruso, supra</a></span></i><i>; </i><i>United States</i> v. <i>Williams, supra</i><i>; </i><i>Golliher</i> v. <i>United States, supra</i><i>; </i><i>Whalem</i> v. <i>United States, supra</i><i>; </i><i>Robinson</i> v. <i>United States, supra</i><i>; </i><i>Evalt</i> v. <i>United States, supra</i><i>; </i><i>Hancock</i> v. <i><span class="citation" data-id="9451942"><a href="/opinion/272441/parker-l-hancock-warden-v-russell-nelson/" aria-description="Citation for case: Parker L. Hancock, Warden v. Russell Nelson">Nelson, supra</a></span></i><i>.</i></p>
<p>[6]  App. 6. Historical evidence points to the established and routine custom of permitting a jailer to search the person who is being processed for confinement under his custody and control. See, <i>e. g.,</i> T. Gardner &amp; V. Manian, Principles and Cases of the Law of Arrest, Search, and Seizure 200 (1974); E. Fisher, Search and Seizure 71 (1970). While "[a] rule of practice must not be allowed . . . to prevail over a constitutional right," <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#313" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 313</a></span> (1921), little doubt has ever been expressed about the validity or reasonableness of such searches incident to incarceration. T. Taylor, Two Studies in Constitutional Interpretation 50 (1969).</p>
<p>[7]  See <i>Evalt</i> v. <i>United States,</i> <span class="citation" data-id="277074"><a href="/opinion/277074/anton-vaughn-evalt-v-united-states/" aria-description="Citation for case: Anton Vaughn Evalt v. United States">382 F. 2d 424</a></span> (CA9 1967); <i>Westover</i> v. <i>United States,</i> <span class="citation" data-id="280000"><a href="/opinion/280000/carl-calvin-westover-v-united-states/" aria-description="Citation for case: Carl Calvin Westover v. United States">394 F. 2d 164</a></span> (CA9 1968); <i>Baskerville</i> v. <i>United States,</i> <span class="citation" data-id="237906"><a href="/opinion/237906/drury-reinhardt-baskerville-v-united-states/" aria-description="Citation for case: Drury Reinhardt Baskerville v. United States">227 F. 2d 454</a></span> (CA10 1955). In <i><span class="citation" data-id="237906"><a href="/opinion/237906/drury-reinhardt-baskerville-v-united-states/" aria-description="Citation for case: Drury Reinhardt Baskerville v. United States">Baskerville</a></span>,</i> the effects were taken for safekeeping on December 23 but re-examined and taken as evidence on January 6. <i>Brett</i> v. <i>United States,</i> <span class="citation" data-id="9454652"><a href="/opinion/285354/robert-brett-v-united-states/" aria-description="Citation for case: Robert Brett v. United States">412 F. 2d 401</a></span> (CA5 1969), is <i>contra.</i> There the defendant's clothes were taken from him shortly after arrival at the jail, as was the custom, and held in the property room of the jail. Three days later the clothing was searched and incriminating evidence found. A divided panel of the Court of Appeals held the evidence inadmissible for want of a warrant authorizing the search.</p>
<p>[8]  <i>Hancock</i> v. <i>Nelson,</i> <span class="citation" data-id="9451942"><a href="/opinion/272441/parker-l-hancock-warden-v-russell-nelson/" aria-description="Citation for case: Parker L. Hancock, Warden v. Russell Nelson">363 F. 2d 249</a></span> (CA1 1966); <i>Malone</i> v. <i>Crouse,</i> <span class="citation" data-id="276677"><a href="/opinion/276677/dick-malone-v-sherman-h-crouse-warden-kansas-state-penitentiary/" aria-description="Citation for case: Dick Malone v. Sherman H. Crouse, Warden, Kansas State...">380 F. 2d 741</a></span> (CA10 1967); <i>United States</i> v. <i>Caruso,</i> <span class="citation" data-id="271127"><a href="/opinion/271127/united-states-v-ciro-michael-caruso/" aria-description="Citation for case: United States v. Ciro Michael Caruso">358 F. 2d 184</a></span> (CA2 1966). In <i><span class="citation" data-id="9451942"><a href="/opinion/272441/parker-l-hancock-warden-v-russell-nelson/" aria-description="Citation for case: Parker L. Hancock, Warden v. Russell Nelson">Hancock</a></span>,</i> the defendant was first taken into custody at 12:51 a. m. His clothes were taken at 2 p. m. on the same day, two hours after probable cause to do so eventuated.</p>
<p>[9]  Holding the Warrant Clause inapplicable in the circumstances present here does not leave law enforcement officials subject to no restraints. This type of police conduct "must [still] be tested by the Fourth Amendment's general proscription against unreasonable searches and seizures." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20</a></span> (1968). But the Court of Appeals here conceded that probable cause existed for the search and seizure of respondent's clothing, and respondent complains only that a warrant should have been secured. We thus have no occasion to express a view concerning those circumstances surrounding custodial searches incident to incarceration which might "violate the dictates of reason either because of their number or their manner of perpetration." <i>Charles</i> v. <i>United States,</i> <span class="citation" data-id="250962"><a href="/opinion/250962/james-d-charles-v-united-states/#389" aria-description="Citation for case: James D. Charles v. United States">278 F. 2d 386, 389</a></span> (CA9), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./364/831/">364 U. S. 831</a></span> (1960). Cf. <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966); <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952).</p>
<p>[1]  <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499</a></span>.</p>
<p>[2]  The Government conceded at oral argument that the seizure of the respondent's clothing was not a matter of routine jail procedure, but was undertaken solely for the purpose of searching for the incriminating paint chips.
</p>
<p>No contention is made that the warrantless seizure of the clothes was necessitated by the exigencies of maintaining discipline or security within the jail system. There is thus no occasion to consider the legitimacy of warrantless searches or seizures in a penal institution based upon that quite different rationale.</p>
<p>[3]  No claim is made that the police feared that Edwards either possessed a weapon or was planning to destroy the paint chips on his clothing. Indeed, the Government has not even suggested that he was aware of the presence of the paint chips on his clothing.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Evans.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Evans"
type: case
citation: "937 F.2d 1534 (1991)"
parallel_cite: ""
neutral_cite: "1991 U.S. App. LEXIS 14383; 1991 WL 118519"
court: "U.S. Court of Appeals, Tenth Circuit"
court_level: coa
circuit: 10th
year: 1991
date_decided: 1991-07-08
docket: 90-6234
authority_weight: "Binding in-circuit — 10th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 1991-07-08
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Evans
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/564407/united-states-v-daryl-lee-evans/"
  cluster_id: 564407
  opinion_id: 564407
  identity_checked: true
homes:
  - page: "[[Inventory Searches]]"
    role: "Recent development (role-based)"
related: ["[[Florida v. Wells]]", "[[Colorado v. Bertine]]", "[[Illinois v. Lafayette]]", "[[South Dakota v. Opperman]]", "[[Nix v. Williams]]"]
aliases: ["United States v. Evans (10th Cir. 1991)", "United States v. Daryl Lee Evans"]
tags: ["case", "fourth-amendment", "inventory-search", "search-incident-to-arrest", "standardized-criteria", "tenth-circuit"]
holding: "UPHELD an inventory search of a carry-on bag (cocaine found in a container) conducted at a bus station: the officer followed the…"
lake:
  record_id: United States v. Evans
  status: verified
  projected_at: 2026-07-06
---

# United States v. Evans

*937 F.2d 1534 (10th Cir. 1991)* · U.S. Court of Appeals, Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Oklahoma City detectives working a drug-interdiction detail at the Union Bus Station approached Daryl Lee Evans after he disembarked from a Los Angeles bus acting nervously. After consent issues with his carry-on bag and a consented pat-down that produced a lump Evans called "weed," he was arrested. Pursuant to department policy, Sergeant Ring pried open the bag's zipper to inventory it before booking and found a taped bundle packaged like the cocaine kilos he had seized before. The search stopped when Evans asked them to get a warrant; warrants were obtained and the bundles tested positive for cocaine.

## Issue
Whether the warrantless opening of an arrestee's locked carry-on bag at the arrest scene, conducted under a written department inventory policy, was a lawful inventory search rather than a ruse for investigatory rummaging.

## Rule
An inventory search conducted pursuant to standardized department procedures, and not as a ruse for general investigatory rummaging, is a lawful exception to the warrant requirement. The Tenth Circuit held: "we hold the search conducted at the bus station of the carry-on bag was a lawful inventory search, and the evidence discovered subsequently (pursuant to valid search warrants) was not the fruit of an illegality, but was lawfully obtained." — 937 F.2d at 1539. ^pin-1539

The validity turns on adherence to a governing policy rather than the officer's location: "Section 239.29 of the Oklahoma City Police Department policy does not require officers to conduct their inventory at a particular place." — *Id.* The court read [[Florida v. Wells]] as cautioning only "against inventory searches being used as a ruse for investigatory purposes," and distinguished it because *[[Florida v. Wells|Wells]]* "dealt with the specific problem of the absence of a department policy or standardized criteria governing such searches." — *Id.* ^pin-1539a

## Application
On these facts the search satisfied the inventory exception. A written policy (Section 239.29) directed that locked containers "must be opened and the contents inventoried before booking," and the court found no probable cause to believe contraband was inside when Sergeant Ring first opened the bag, so the policy's competing "obtain a warrant" directive was not triggered. Conducting the inventory at the bus station rather than the station house did not invalidate it, because the policy did not fix a location; and the officer's failure to take notes and his cessation of the search after the first bundle did not show a ruse, given that he was "at the very outset of the inventory" and stopped out of caution when Evans demanded a warrant. Because Sergeant Ring adhered to the standardized procedure and there was no evidence he intended any purpose other than inventory, the search was lawful and the later warranted openings were not fruit of an illegality.

## Conclusion
The bus-station opening of the carry-on bag was a valid inventory search; the denial of the motion to suppress was affirmed. The court did not reach the district court's alternative inevitable-discovery ground.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 10th Cir.**
- No negative subsequent treatment identified. The decision applies the SCOTUS inventory-search line — [[South Dakota v. Opperman]], [[Illinois v. Lafayette]], [[Colorado v. Bertine]], and [[Florida v. Wells]] — to a locked carry-on bag opened under standardized policy.

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Evans*, 937 F.2d 1534 (10th Cir. 1991) — https://www.courtlistener.com/opinion/564407/united-states-v-daryl-lee-evans/ — pinpoint: 1539.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "17cff1521c403f45", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Evans"}, "payload": {"all": [{"cite": "937 F.2d 1534", "page": "1534", "reporter": "F.2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "937"}, {"cite": "1991 U.S. App. LEXIS 14383", "page": "14383", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1991"}, {"cite": "1991 WL 118519", "page": "118519", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "1991"}], "display": "937 F.2d 1534", "official": {"cite": "937 F.2d 1534", "page": "1534", "reporter": "F.2d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "937"}, "official_selection_present": true, "record_id": "United States v. Evans"}}
{"assertion_id": "94ffeb5da05ff030", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1539a", "record_id": "United States v. Evans"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1539a", "pinpoint_status": "slip-only", "quote": "Section 239.29 of the Oklahoma City Police Department policy does not require officers to conduct their inventory at a particular place.", "quote_fidelity": "mismatch", "record_id": "United States v. Evans", "star_marker": null}}
{"assertion_id": "c756e1fc80813ce5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1539", "record_id": "United States v. Evans"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1539", "pinpoint_status": "slip-only", "quote": "he was arrested. Pursuant to department policy, Sergeant Ring pried open the bag's zipper to inventory it before booking and found a taped bundle packaged like the cocaine kilos he had seized before. The search stopped when Evans asked them to get a warrant; warrants were obtained and the bundles tested positive for cocaine. ## Issue Whether the warrantless opening of an arrestee's locked carry-on bag at the arrest scene, conducted under a written department inventory policy, was a lawful inventory search rather than a ruse for investigatory rummaging. ## Rule An inventory search conducted pursuant to standardized department procedures, and not as a ruse for general investigatory rummaging, is a lawful exception to the warrant requirement. The Tenth Circuit held:", "quote_fidelity": "mismatch", "record_id": "United States v. Evans", "star_marker": null}}
{"assertion_id": "2c65fc6bb1661eb9", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Evans"}, "payload": {"as_of_content": "1991-07-08", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Evans", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Evans

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Evans",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Daryl Lee Evans",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Daryl Lee EVANS, Defendant-Appellant",
    "input_case_name": "United States v. Evans",
    "court": "U.S. Court of Appeals, Tenth Circuit",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "10th",
    "state": null,
    "date_decided": "1991-07-08",
    "year": 1991,
    "docket": "90-6234",
    "cluster_id": 564407,
    "lead_opinion_id": 564407,
    "sibling_ids": [
      564407
    ],
    "absolute_url": "/opinion/564407/united-states-v-daryl-lee-evans/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "937 F.2d 1534",
      "volume": "937",
      "reporter": "F.2d",
      "page": "1534",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1991 U.S. App. LEXIS 14383",
        "volume": "1991",
        "reporter": "U.S. App. LEXIS",
        "page": "14383",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 WL 118519",
        "volume": "1991",
        "reporter": "WL",
        "page": "118519",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "937 F.2d 1534",
        "volume": "937",
        "reporter": "F.2d",
        "page": "1534",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 U.S. App. LEXIS 14383",
        "volume": "1991",
        "reporter": "U.S. App. LEXIS",
        "page": "14383",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 WL 118519",
        "volume": "1991",
        "reporter": "WL",
        "page": "118519",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "937 F.2d 1534",
    "official_selection": {
      "court_class": "coa",
      "selected": "937 F.2d 1534",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1539",
      "page": null,
      "quote": "he was arrested. Pursuant to department policy, Sergeant Ring pried open the bag's zipper to inventory it before booking and found a taped bundle packaged like the cocaine kilos he had seized before. The search stopped when Evans asked them to get a warrant; warrants were obtained and the bundles tested positive for cocaine. ## Issue Whether the warrantless opening of an arrestee's locked carry-on bag at the arrest scene, conducted under a written department inventory policy, was a lawful inventory search rather than a ruse for investigatory rummaging. ## Rule An inventory search conducted pursuant to standardized department procedures, and not as a ruse for general investigatory rummaging, is a lawful exception to the warrant requirement. The Tenth Circuit held:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1539a",
      "page": null,
      "quote": "Section 239.29 of the Oklahoma City Police Department policy does not require officers to conduct their inventory at a particular place.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1991-07-08",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Evans",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Hansen",
          "cluster_id": 2630631,
          "cite": [
            "2002 UT 125",
            "63 P.3d 650",
            "463 Utah Adv. Rep. 5",
            "2002 Utah LEXIS 215",
            "2002 WL 31845283"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Steven Curtis Waupekenay",
          "cluster_id": 590024,
          "cite": [
            "973 F.2d 1533",
            "1992 U.S. App. LEXIS 20488",
            "1992 WL 207624"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKinstrey",
          "cluster_id": 1372825,
          "cite": [
            "852 P.2d 467",
            "17 Brief Times Rptr. 893",
            "1993 Colo. LEXIS 470",
            "1993 WL 189812"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re JM",
          "cluster_id": 2264984,
          "cite": [
            "619 A.2d 497",
            "1992 D.C. App. LEXIS 348",
            "1992 WL 387505"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Oscar Arzaga",
          "cluster_id": 656678,
          "cite": [
            "9 F.3d 91",
            "1993 U.S. App. LEXIS 29057",
            "1993 WL 461577"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Morales",
          "cluster_id": 2604608,
          "cite": [
            "935 P.2d 936",
            "1997 Colo. LEXIS 166",
            "1997 WL 86035"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Welch",
          "cluster_id": 1209950,
          "cite": [
            "873 P.2d 601",
            "1994 Wyo. LEXIS 56",
            "1994 WL 147907"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. T.H.",
          "cluster_id": 1163445,
          "cite": [
            "892 P.2d 301",
            "19 Brief Times Rptr. 452",
            "1995 Colo. LEXIS 51",
            "1995 WL 117069"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilcher v. City of Wilmington",
          "cluster_id": 1471789,
          "cite": [
            "924 F. Supp. 613",
            "1996 U.S. Dist. LEXIS 5970",
            "1996 WL 224204"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jim",
          "cluster_id": 10702082,
          "cite": [
            "508 P.3d 937"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Little",
          "cluster_id": 2081478,
          "cite": [
            "862 F. Supp. 334",
            "1994 U.S. Dist. LEXIS 12833",
            "1994 WL 487950"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Woodard",
          "cluster_id": 1466244,
          "cite": [
            "873 F. Supp. 535",
            "1994 U.S. Dist. LEXIS 18705",
            "1994 WL 723964"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Manuel",
          "cluster_id": 1503195,
          "cite": [
            "791 F. Supp. 265",
            "1992 U.S. Dist. LEXIS 6844",
            "1992 WL 94094"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Armijo",
          "cluster_id": 1411372,
          "cite": [
            "781 F. Supp. 1551",
            "1991 U.S. Dist. LEXIS 19017",
            "1991 WL 285732"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hanks",
          "cluster_id": 1510418,
          "cite": [
            "821 F. Supp. 1425",
            "1993 U.S. Dist. LEXIS 7541",
            "1993 WL 185573"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Baker",
          "cluster_id": 4398905,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cruz-Mendez",
          "cluster_id": 168346,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(564407) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca10)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(564407)",
        "reviewed": 18,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 17,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(564407)",
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
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(564407)",
    "indexed_citing_opinions": 18,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 564407,
        "count": 18,
        "count_source": "search"
      }
    ],
    "citation_count": 50,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-evans.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 18,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 564407,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 564407,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 564407,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 564407,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 564407,
        "cited_id": 112412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 564407,
        "cited_id": 112631,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "RU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T23:53:39Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:53:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:53:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:56:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:53:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Evans

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b1635-26">
  BRORBY, Circuit Judge.
 </author>
<p id="b1635-27">
  This appeal arises from the district court’s denial of Defendant Daryl Lee Evans’s, motion to suppress evidence. Defendant states the issues presented for review as follows: “Whether the district court erred in denying appellant’s motion to suppress evidence seized pursuant to an un
  <span citation-index="1" class="star-pagination" label="1536"> 
   *1536
   </span>
  lawful employment of a drug courier profile and unlawful
  <em>
   Terry
  </em>
  investigation;” and “[w]hether the district court erred when it denied appellant’s motion to suppress evidence seized pursuant to an unlawful search of the carry-on luggage without a search warrant.” We affirm.
 </p>
<p id="b1636-4">
  I.
 </p>
<p id="b1636-5">
  On April 25, 1990, Detective Sergeants Gary Eastridge and Glenn Ring of the Oklahoma City Police Department were working at the Union Bus Station in Oklahoma City as part of an interdiction program to detect and deter the arrival of drugs into the area. At approximately 2:00 p.m. that day, the officers observed a bus, which had originated in Los Angeles, arrive at the station and its passengers disembark. Among the passengers observed by the officers was Daryl Lee Evans. Mr. Evans was carrying a gray, soft sided bag. As Mr. Evans proceeded through the terminal, the officers noticed him scanning the area and acting in a very nervous manner. Mr. Evans then placed the gray bag he was carrying between his feet as he watched the luggage being unloaded from the bus.
 </p>
<p id="b1636-6">
  Based on these observations and Sergeant Ring’s experience and training in detecting drug couriers, the officers approached Mr. Evans, identifying themselves as narcotics officers, asked Mr. Evans for identification, and explained their reason for speaking with him.
 </p>
<p id="b1636-7">
  Mr. Evans produced his identification while the conversation ensued but became increasingly nervous. Sergeant Ring then asked if Mr. Evans would allow the officers to search his carry-on bag. Mr. Evans told the officers he did not have the keys to the bag but subsequently produced two claim tags for other luggage that he claimed contained the keys. Mr. Evans gave the tags to Sergeant Eastridge, who attempted, but was unable, to locate the other luggage. The officers continued their conversation with Mr. Evans. Sergeant Ring stated he thought it was unusual that Mr. Evans did not have the keys to the bag on his person, whereupon Sergeant Ring asked Mr. Evans if he could pat him down to try and find the keys, and Mr. Evans consented. Both officers then proceeded to pat down Mr. Evans, and Sergeant Eas-tridge discovered a lump near the calf of Mr. Evans’s leg. When Sergeant Eas-tridge inquired about the lump, Mr. Evans responded that it was “weed.”
 </p>
<p id="b1636-9">
  Following this, Mr. Evans was advised he was under arrest and was taken to an interior office at the bus station. Sergeant Ring then informed Mr. Evans that due to his arrest his carry-on bag would be inventoried before submitting it to the Oklahoma City property room according to department policy. Sergeant Ring then pried open a zipper on the bag and removed from the compartment a taped plastic bundle. Sergeant Ring noticed the bundle was sealed and packaged like kilograms of cocaine he had seized in the past. Sergeant Ring then asked Mr. Evans if there were any additional narcotics, and Mr. Evans said there were two other packages similar to the one already discovered. Sergeant Ring then asked Mr. Evans if he would consent to the officers opening the taped bundle. At this point, Mr. Evans advised that he wanted the search to cease until the officers obtained a search warrant, and the search ceased.
 </p>
<p id="b1636-10">
  Mr. Evans was then transported to the police station, and Sergeant Ring and Sergeant Eastridge sought and secured two search warrants — one for the taped bundle, and one for the other compartment of the bag. After obtaining these warrants, all three bundles were opened. The contents tested positive for the substance cocaine hydrochloride.
 </p>
<p id="b1636-11">
  II.
 </p>
<p id="b1636-12">
  In reviewing the denial of a defendant’s motion to suppress evidence, we accept the trial court’s findings of fact, unless clearly erroneous, and consider all the evidence in a light most favorable to the Government.
  <em>
   United States v. McAlpine,
  </em>
  <span class="citation" data-id="552251"><a href="/opinion/552251/united-states-v-william-james-mcalpine/#1463" aria-description="Citation for case: United States v. William James McAlpine">919 F.2d 1461, 1463</a></span> (10th Cir.1990). However, ultimate determinations of reasonableness under the Fourth Amendment, and other questions of law, are reviewed de
  <span citation-index="1" class="star-pagination" label="1537"> 
   *1537
   </span>
  novo.
  <em>
   United States v. Butler,
  </em>
  <span class="citation" data-id="9480414"><a href="/opinion/542920/united-states-v-ricky-e-butler/#1484" aria-description="Citation for case: United States v. Ricky E. Butler">904 F.2d 1482, 1484</a></span> (10th Cir.1990).
 </p>
<p id="b1637-4">
  Mr. Evans first contends his Fourth Amendment rights were violated when the officers at the Union Bus Station approached him based on a drug courier profile. Before addressing the lawfulness of using a drug courier profile, we must determine whether any Fourth Amendment protection is due Mr. Evans under these circumstances. This court has previously identified three categories of encounters between police and citizens, each representing different levels of Fourth Amendment entitlement. We described these categories as follows:
 </p>
<blockquote id="b1637-5">
  The first is referred to as a police-citizen encounter and is characterized by the voluntary cooperation of a citizen in response to non-coercive questioning. This has been held to raise no constitutional issues because this type of contract [sic] is not a seizure within the meaning of the Fourth Amendment....
 </blockquote>
<blockquote id="b1637-6">
  The second type of encounter is the Terry-type of stop. The standards here are set forth in
  <em>
   Terry v. Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968). Most courts characterize this as a “brief, non-intrusive detention during a frisk for weapons or preliminary questioning * * This is considered a.seizure of the person within the meaning of the Fourth Amendment, but need not be supported by probable cause. In order to justify an investigatory stop, the officer need have only “specific and articulable facts sufficient to give rise to reasonable suspicion that a person has committed or is committing a crime.”
 </blockquote>
<blockquote id="b1637-7">
  The final category is an arrest which is characterized by highly intrusive or lengthy search or detention. An arrest is justified only when there is probable cause to believe that a person has committed or is committing a crime.
 </blockquote>
<p id="b1637-8">
<em>
   United States v. Cooper,
  </em>
  <span class="citation" data-id="9472135"><a href="/opinion/435289/united-states-v-vanessa-elaine-cooper-and-darryl-keith-threat/#1363" aria-description="Citation for case: United States v. Vanessa Elaine Cooper, and Darryl Keith...">733 F.2d 1360, 1363</a></span> (10th Cir.) (citations omitted),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./467/1255/">467 U.S. 1255</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./104/3543/">104 S.Ct. 3543</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/82/847/">82 L.Ed.2d 847</a></span> (1984).
 </p>
<p id="b1637-11">
  In the present case, the district court found the initial questioning of Mr. Evans prior to the pat down fell within the first category of police/citizen encounters, rendering any Fourth Amendment claims unwarranted.
  <em>
   See id.
  </em>
  Merely approaching an individual in a public place and asking questions of the individual, including asking to examine the person’s identification or requesting the person’s consent to search his or her luggage is not a seizure implicating the Fourth Amendment.
  <em>
   Florida v. Bostick,
  </em>
  — U.S. --, -, <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#2386" aria-description="Citation for case: Florida v. Bostick">111 S.Ct. 2382, 2386</a></span>, <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">115 L.Ed.2d 389</a></span> (1991). As long as the police have not, by means of physical force or show of authority, in some way restrained the liberty of the citizen, such a consensual encounter will not constitute a seizure for purposes of the Fourth Amendment.
  <em>
   <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Id.</a></span>
  </em>
  at- — -, <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#2386" aria-description="Citation for case: Florida v. Bostick">111 S.Ct. at 2386</a></span>. The district court found, inter alia: “the encounter was a cooperative one”; “[t]he defendant was engaged in conversations ... [and] was approached in a friendly conversational manner”; and “[t]here were no threats made to the defendant ... [nor] promises ... given.” Our review of the record reveals these findings are fully supported and not clearly erroneous. Therefore, no Fourth Amendment concerns were implicated during this initial non-coercive questioning.
 </p>
<p id="b1637-15">
  The pat down of Mr. Evans, as it involved more than mere cooperative questioning, is entitled to Fourth Amendment scrutiny. In regard to the pat down, the district court made the following findings: “that this pat down was consented to by the defendant”; “that the consent was not limited to Detective Ring”; “that it was not limited to the pockets only”; and that “defendant was well aware of these two officers” and “[t]he fact that the defendant was looking at Officer Ring when this consent was made does not serve to limit the consent.”
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  Consent to search is valid if given voluntarily.
  <em>
   Schneckloth v. Busta
  </em>
<span citation-index="1" class="star-pagination" label="1538"> 
   *1538
   </span>
<em>
   monte,
  </em>
  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#222" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218, 222-23</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#2045" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041, 2045-46</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L.Ed.2d 854</a></span> (1973). The volun-tariness of consent is a question of fact to be determined from the totality of all the circumstances.
  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#227" aria-description="Citation for case: Schneckloth v. Bustamonte"><em>
   Id.
  </em>
  at 227</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#2047" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. at 2047</a></span>. We have previously set forth the following three-tiered analysis to be used in determining whether consent was voluntary:
 </p>
<blockquote id="Ajsn">
  First, there must be clear and positive testimony that the consent was unequivocal and specific, and freely and intelligently given. Second, the Government must establish that consent was given without duress or coercion. Finally, we evaluate the first two standards with the traditional indulgence of the courts against a presumption of waiver of constitutional rights.
 </blockquote>
<p id="b1638-4">
<em>
   United States v. Corral,
  </em>
  <span class="citation" data-id="538919"><a href="/opinion/538919/united-states-v-silverio-corral-united-states-of-america-v-jesus-valdez/#994" aria-description="Citation for case: United States v. Silverio Corral, United States of...">899 F.2d 991, 994</a></span> (10th Cir.1990) (quoting
  <em>
   United States v. Recalde,
  </em>
  <span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1453" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d 1448, 1453</a></span> (10th Cir.1985) (citations omitted)).
 </p>
<p id="b1638-5">
  The record herein clearly indicates Mr. Evans gave a voluntary and unequivocal consent to the pat down. There is no evidence the officers used any threats or other forms of coercive conduct in obtaining this consent. Moreover, after the pat down by both officers had commenced, Mr. Evans did not request the officers to cease the pat down, nor did he manifest any conduct indicating he wanted the pat down to be ceased. Therefore, we find the district court’s findings on this issue were supported by the record and not clearly erroneous. Based on the totality of the circumstances and giving the appropriate indulgence to the presumption against waiver, we nevertheless conclude the consent given by Mr. Evans was voluntary and not restricted to a search by Sergeant Ring only.
 </p>
<p id="b1638-6">
  Mr. Evans next argues the district court erred in not suppressing the evidence because it was “fruit of the poisonous tree” of the unlawful search of the carry-on bag, and cites
  <em>
   Wong Sun v. United States,
  </em>
  <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U.S. 471</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">9 L.Ed.2d 441</a></span> (1963). The search complained of was upheld by the district court pursuant to the inventory search exception to the warrant requirement, and alternatively, under the inevitable discovery doctrine. Mr. Evans contests both rulings.
 </p>
<p id="b1638-8">
  First, in regard to its ruling that the initial search of the carry-on bag was conducted as a legitimate inventory search, the district court made the following findings: “Section 239.29 is the policy provision that governed or should have governed Officer Ring’s conduct in this case”; “pursuant to this policy, the case in which the cocaine was found was directed to have been opened by Officer Ring and inventoried before booking”; and “there was not probable cause at that time to believe that contraband or evidence was within and, as a result, there was no requirement for the officer at that stage to follow the second directive with respect to Section 239.29.”
 </p>
<p id="b1638-9">
  Oklahoma City Police Department Policy, Section 239.29, states in pertinent part:
 </p>
<blockquote id="b1638-10">
  [1] Locked containers such as suitcases or briefcases must be opened and the contents inventoried before booking. [2] If probable cause exists to believe that contraband or evidence is within, care should be taken to obtain legal authority before opening to ensure the admissibility of that evidence in court.
 </blockquote>
<p id="b1638-11">
  The first directive indicated above clearly advises the officer to open and inventory the contents of locked containers, unless the second directive is activated by the existence of probable cause. We are convinced, based on the record before us, that probable cause to believe further contraband would be found in the bag did
  <em>
   not
  </em>
  exist at the time Sergeant Ring first opened the bag at the bus station. Therefore, his search was in accordance with departmental policy directing him to open locked containers
  <em>
   before booking.
  </em>
  While Defendant argues the location of the search (at the bus station rather than the police station) mandates a finding that its purpose was merely a “ruse for a general rummaging,”
  <em>
   see Florida v. Wells,
  </em>
  — U.S. -, —, <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/#1635" aria-description="Citation for case: Florida v. Wells">110 S.Ct. 1632, 1635</a></span>, <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/" aria-description="Citation for case: Florida v. Wells">109 L.Ed.2d 1</a></span> (1990), we find this argument without merit. Section 239.29 of the Oklahoma City Police Department policy does not require officers to conduct their inventory at a particular place, but “specifically
  <span citation-index="1" class="star-pagination" label="1539"> 
   *1539
   </span>
  envisions otherwise.” Nor is there any directive in the law imposing such a requirement. We find the officers’ explanation for conducting the search at the bus station reasonable, and conclude the search was not invalidated because it was not done at the police station.
 </p>
<p id="b1639-4">
  Defendant also claims the absence of note-taking by the officers and the cessation of the “inventory” search after finding the first suspicious package further indicates the search was a ruse. The district court acknowledged these concerns but was persuaded that Sergeant Ring’s failure to take notes was not improper, since he was at the very outset of the inventory when he encountered the suspicious, taped bundle. The court also declined to fault the officers for acting out of an abundance of caution in heeding Defendant’s request that a search warrant be obtained.
 </p>
<p id="b1639-5">
  In
  <em>
   <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/" aria-description="Citation for case: Florida v. Wells">Wells</a></span>,
  </em>
  the case relied on by Mr. Evans, the Supreme Court cautioned against inventory searches being used as a ruse for investigatory purposes. — U.S. at-, <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/#1635" aria-description="Citation for case: Florida v. Wells">110 S.Ct. at 1635</a></span>. Our review of the record leads us to conclude that the district court’s findings on this matter are not clearly erroneous, and the initial search into Mr. Evans’s carry-on bag was not a mere ruse for investigation.
  <em>
   <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/" aria-description="Citation for case: Florida v. Wells">Wells</a></span>
  </em>
  dealt with the specific problem of the absence of a department policy or standardized criteria governing such searches.
  <em>
   <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/" aria-description="Citation for case: Florida v. Wells">Id.</a></span>
  </em>
  We do not have such a void in this case. Section 239.29 of the Oklahoma City Police Department Policy clearly provides procedures to be followed. Sergeant Ring adhered to these procedures, and there is no evidence in the record that he anticipated or intended the search to serve any purpose other than that of an inventory of the contents of the bag. Accordingly, we hold the search conducted at the bus station of the carry-on bag was a lawful inventory search, and the evidence discovered subsequently (pursuant to valid search warrants) was not the fruit of an illegality, but was lawfully obtained.
 </p>
<p id="b1639-8">
  Having decided the search of the carry-on bag was a lawful inventory search, we uphold the district court’s decision to deny Mr. Evans’s motion to suppress on this basis. Therefore, we need not address the district court’s alternate holding that the search was justified and lawful under the inevitable discovery doctrine.
  <em>
   See Nix v. Williams,
  </em>
  <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">467 U.S. 431</a></span>, <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">104 S.Ct. 2501</a></span>, <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">81 L.Ed.2d 377</a></span> (1984).
 </p>
<p id="b1639-10">
  III.
 </p>
<p id="b1639-11">
  For the aforementioned reasons, we AFFIRM the district court’s decision to deny Mr. Evans’s motion to suppress evidence.
 </p>

<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b1637-9">
   . The district court also found on this point that two statements made in the Defendant’s affidavit relating to an alleged restriction of his consent, were unsupported in the record and otherwise not credible. We agree with these findings.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Flores-Montano.json  (`lake-record`, 6 assertions)

### content_page

```
---
title: "United States v. Flores-Montano"
type: case
citation: ""
parallel_cite: "541 U.S. 149; 124 S. Ct. 1582; 158 L. Ed. 2d 311; 72 U.S.L.W. 4263; 17 Fla. L. Weekly Fed. S 207"
neutral_cite: 2004 U.S. LEXIS 2548
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-03-30
docket: 02-1794
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2004-03-30
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Flores-Montano
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/134729/united-states-v-flores-montano/"
  cluster_id: 134729
  opinion_id: 134729
  identity_checked: true
homes:
  - page: "[[Border Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Montoya de Hernandez]]", "[[United States v. Martinez-Fuerte]]", "[[Carroll v. United States]]", "[[Almeida-Sanchez v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "border-searches", "vehicle-search", "gas-tank", "suspicionless-search"]
holding: "The government's authority to conduct suspicionless searches of vehicles at the border includes disassembling and reassembling a gas…"
lake:
  record_id: United States v. Flores-Montano
  status: verified
  projected_at: 2026-07-09
---

# United States v. Flores-Montano

*541 U.S. 149 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
At the Otay Mesa Port of Entry, customs inspectors sent Manuel Flores-Montano's station wagon to secondary inspection. A second inspector tapped the gas tank, found it sounded solid, and had a contract mechanic remove the tank; the inspector then hammered off bondo, opened an access plate, and found 37 kilograms of marijuana. The Government did not rely on reasonable suspicion; the Ninth Circuit (following its *Molina-Tarazon* decision) had held the fuel-tank disassembly required reasonable suspicion.

## Issue
Whether the Fourth Amendment requires reasonable suspicion before customs officers may remove, disassemble, and reassemble a vehicle's fuel tank in a search at the international border.

## Rule
No. A suspicionless border search of a vehicle, including disassembly of its fuel tank, is reasonable. The Court held at the outset: "We hold that the search in question did not require reasonable suspicion." — 541 U.S. at 150. ^pin-150

The border is a special context: "The Government's interest in preventing the entry of unwanted persons and effects is at its zenith at the international border," and searches there "are reasonable simply by virtue of the fact that they occur at the border." — *Id.* at 152–53. ^pin-152

The intrusiveness analysis that may attend highly invasive *person* searches does not transfer to vehicles: "Complex balancing tests to determine what is a 'routine' search of a vehicle, as opposed to a more 'intrusive' search of a person, have no place in border searches of vehicles." — *Id.* at 152. ^pin-152a

## Application
On these facts the disassembly was reasonable without any suspicion. The Court rejected Flores-Montano's privacy argument because the expectation of privacy is diminished at the border and "the search of a gas tank, which should be solely a repository for fuel," is no greater an invasion than a search of the passenger compartment. It rejected his property argument because the removal, disassembly, and reassembly is "a brief procedure that can be reversed without damaging the safety or operation of the vehicle," with no record evidence of serious damage; any interference was "justified by the Government's paramount interest in protecting the border." The Court therefore "conclude[d] that the Government's authority to conduct suspicionless inspections at the border includes the authority to remove, disassemble, and reassemble a vehicle's fuel tank." — [*Id.* at 155](https://www.courtlistener.com/opinion/134729/united-states-v-flores-montano/#:~:text=the%20search%20of%20a%20gas). ^pin-155

## Conclusion
No reasonable suspicion was required; the Ninth Circuit's judgment suppressing the marijuana was reversed. The Court reserved that "some searches of property [may be] so destructive as to require a different result," but this was not one.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment. *Flores-Montano* confines the "routine vs. non-routine" distinction drawn for *person* searches in [[United States v. Montoya de Hernandez]] and instead applies the plenary suspicionless-search rule to vehicles; it expressly leaves open only searches so destructive as to require a different result.

## Appears on
- [[Border Searches]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Flores-Montano*, 541 U.S. 149 (2004) — https://www.courtlistener.com/opinion/134729/united-states-v-flores-montano/ — pinpoints: 150, 152–53, 155.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "64d101589f335b4f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Flores-Montano"}, "payload": {"all": [{"cite": "541 U.S. 149", "page": "149", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "541"}, {"cite": "124 S. Ct. 1582", "page": "1582", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "124"}, {"cite": "158 L. Ed. 2d 311", "page": "311", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "158"}, {"cite": "2004 U.S. LEXIS 2548", "page": "2548", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2004"}, {"cite": "72 U.S.L.W. 4263", "page": "4263", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "72"}, {"cite": "17 Fla. L. Weekly Fed. S 207", "page": "207", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "17"}], "display": null, "official": null, "official_selection_present": false, "record_id": "United States v. Flores-Montano"}}
{"assertion_id": "1b421a2f96cc636a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-155", "record_id": "United States v. Flores-Montano"}, "payload": {"fragment": "#:~:text=the%20search%20of%20a%20gas", "page": null, "pin_id": "pin-155", "pinpoint_status": "star-verified", "quote": "the search of a gas tank, which should be solely a repository for fuel,", "quote_fidelity": "matched", "record_id": "United States v. Flores-Montano", "star_marker": "154"}}
{"assertion_id": "453786718913ea8f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-150", "record_id": "United States v. Flores-Montano"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-150", "pinpoint_status": "slip-only", "quote": "--- # United States v. Flores-Montano *541 U.S. 149 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background At the Otay Mesa Port of Entry, customs inspectors sent Manuel Flores-Montano's station wagon to secondary inspection. A second inspector tapped the gas tank, found it sounded solid, and had a contract mechanic remove the tank; the inspector then hammered off bondo, opened an access plate, and found 37 kilograms of marijuana. The Government did not rely on reasonable suspicion; the Ninth Circuit (following its *Molina-Tarazon* decision) had held the fuel-tank disassembly required reasonable suspicion. ## Issue Whether the Fourth Amendment requires reasonable suspicion before customs officers may remove, disassemble, and reassemble a vehicle's fuel tank in a search at the international border. ## Rule No. A suspicionless border search of a vehicle, including disassembly of its fuel tank, is reasonable. The Court held at the outset:", "quote_fidelity": "mismatch", "record_id": "United States v. Flores-Montano", "star_marker": null}}
{"assertion_id": "83d7d10a5d7cfe7d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-152a", "record_id": "United States v. Flores-Montano"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-152a", "pinpoint_status": "slip-only", "quote": "Complex balancing tests to determine what is a 'routine' search of a vehicle, as opposed to a more 'intrusive' search of a person, have no place in border searches of vehicles.", "quote_fidelity": "mismatch", "record_id": "United States v. Flores-Montano", "star_marker": null}}
{"assertion_id": "9350115e438f4f1c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-152", "record_id": "United States v. Flores-Montano"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-152", "pinpoint_status": "slip-only", "quote": "The Government's interest in preventing the entry of unwanted persons and effects is at its zenith at the international border,", "quote_fidelity": "mismatch", "record_id": "United States v. Flores-Montano", "star_marker": null}}
{"assertion_id": "4f4fa5ed83e4aa76", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Flores-Montano"}, "payload": {"as_of_content": "2004-03-30", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Flores-Montano", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Flores-Montano

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Flores-Montano",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Flores-Montano",
    "case_name_short": "Flores-Montano",
    "case_name_full": "United States v. Flores-Montano",
    "input_case_name": "United States v. Flores-Montano",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-03-30",
    "year": 2004,
    "docket": "02-1794",
    "cluster_id": 134729,
    "lead_opinion_id": 134729,
    "sibling_ids": [
      134729,
      9434573,
      9434574
    ],
    "absolute_url": "/opinion/134729/united-states-v-flores-montano/",
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
        "cite": "541 U.S. 149",
        "volume": "541",
        "reporter": "U.S.",
        "page": "149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 1582",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "1582",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "158 L. Ed. 2d 311",
        "volume": "158",
        "reporter": "L. Ed. 2d",
        "page": "311",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 U.S.L.W. 4263",
        "volume": "72",
        "reporter": "U.S.L.W.",
        "page": "4263",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fla. L. Weekly Fed. S 207",
        "volume": "17",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "207",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 2548",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "2548",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "541 U.S. 149",
        "volume": "541",
        "reporter": "U.S.",
        "page": "149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 1582",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "1582",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "158 L. Ed. 2d 311",
        "volume": "158",
        "reporter": "L. Ed. 2d",
        "page": "311",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 2548",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "2548",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 U.S.L.W. 4263",
        "volume": "72",
        "reporter": "U.S.L.W.",
        "page": "4263",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fla. L. Weekly Fed. S 207",
        "volume": "17",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "207",
        "type": 1,
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
      "id": "pin-150",
      "page": null,
      "quote": "--- # United States v. Flores-Montano *541 U.S. 149 (2004)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background At the Otay Mesa Port of Entry, customs inspectors sent Manuel Flores-Montano's station wagon to secondary inspection. A second inspector tapped the gas tank, found it sounded solid, and had a contract mechanic remove the tank; the inspector then hammered off bondo, opened an access plate, and found 37 kilograms of marijuana. The Government did not rely on reasonable suspicion; the Ninth Circuit (following its *Molina-Tarazon* decision) had held the fuel-tank disassembly required reasonable suspicion. ## Issue Whether the Fourth Amendment requires reasonable suspicion before customs officers may remove, disassemble, and reassemble a vehicle's fuel tank in a search at the international border. ## Rule No. A suspicionless border search of a vehicle, including disassembly of its fuel tank, is reasonable. The Court held at the outset:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-152",
      "page": null,
      "quote": "The Government's interest in preventing the entry of unwanted persons and effects is at its zenith at the international border,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-152a",
      "page": null,
      "quote": "Complex balancing tests to determine what is a 'routine' search of a vehicle, as opposed to a more 'intrusive' search of a person, have no place in border searches of vehicles.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-155",
      "page": null,
      "quote": "the search of a gas tank, which should be solely a repository for fuel,",
      "star_marker": "154",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 13434,
      "fragment": "#:~:text=the%20search%20of%20a%20gas",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2004-03-30",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Flores-Montano",
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
        "journal_ref": "United States v. Flores-Montano:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Levy",
          "cluster_id": 8442407,
          "cite": [
            "803 F.3d 120",
            "2015 U.S. App. LEXIS 17154",
            "2015 WL 5692332"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane1_negative"
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
        "journal_ref": "United States v. Flores-Montano:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Perez-Diaz",
          "cluster_id": 8473264,
          "cite": [
            "172 F. App'x 717"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Julio Cortez-Rocha",
          "cluster_id": 788904,
          "cite": [
            "394 F.3d 1115",
            "2005 U.S. App. LEXIS 1014",
            "2005 WL 107088"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Julio Cortez-Rocha",
          "cluster_id": 787787,
          "cite": [
            "383 F.3d 1093",
            "2004 U.S. App. LEXIS 19583",
            "2004 WL 2093451"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane1_negative"
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
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
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
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
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
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
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
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Al Otro Lado v. Chad Wolf",
          "cluster_id": 4732848,
          "cite": [
            "952 F.3d 999"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
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
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ray Askins v. Usdhs",
          "cluster_id": 4526305,
          "cite": [
            "899 F.3d 1035"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Howard Cotterman",
          "cluster_id": 854692,
          "cite": [
            "709 F.3d 952",
            "2013 WL 856292",
            "2013 U.S. App. LEXIS 4731"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "International Refugee Assistance Project v. Trump",
          "cluster_id": 4394639,
          "cite": [
            "857 F.3d 554",
            "2017 U.S. App. LEXIS 9109",
            "2017 WL 2273306"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Guzman-Padilla",
          "cluster_id": 1448445,
          "cite": [
            "573 F.3d 865",
            "2009 U.S. App. LEXIS 16298",
            "2009 WL 2182818"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vincent Franklin Bennett",
          "cluster_id": 785723,
          "cite": [
            "363 F.3d 947",
            "64 Fed. R. Serv. 467",
            "2004 U.S. App. LEXIS 6935"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carlyle Bryan v. United States",
          "cluster_id": 4582985,
          "cite": [
            "913 F.3d 356"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Abbouchi",
          "cluster_id": 1235958,
          "cite": [
            "502 F.3d 850",
            "2007 U.S. App. LEXIS 21280",
            "2007 WL 2493507"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Theodore Stewart",
          "cluster_id": 1039561,
          "cite": [
            "729 F.3d 517",
            "2013 WL 4711054",
            "2013 U.S. App. LEXIS 18224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Troy",
          "cluster_id": 204022,
          "cite": [
            "583 F.3d 20",
            "2009 U.S. App. LEXIS 21186",
            "2009 WL 3050901"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Denson v. United States",
          "cluster_id": 78422,
          "cite": [
            "574 F.3d 1318",
            "2009 U.S. App. LEXIS 15634",
            "2009 WL 2031036"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anas Elhady v. Unidentified CBP Agents",
          "cluster_id": 5299118,
          "cite": [
            "18 F.4th 880"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Miguel Cano",
          "cluster_id": 4649091,
          "cite": [
            "934 F.3d 1002"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Manuel Flores-Montano",
          "cluster_id": 792061,
          "cite": [
            "424 F.3d 1044",
            "2005 U.S. App. LEXIS 19768",
            "2005 WL 2218952"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tabbaa v. Chertoff",
          "cluster_id": 2661,
          "cite": [
            "509 F.3d 89",
            "2007 U.S. App. LEXIS 27258",
            "2007 WL 4150299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karl Touset",
          "cluster_id": 4500452,
          "cite": [
            "890 F.3d 1227"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anas Elhady v. Charles Kable, IV",
          "cluster_id": 4869134,
          "cite": [
            "993 F.3d 208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hamza Kolsuz",
          "cluster_id": 4496513,
          "cite": [
            "890 F.3d 133"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Molina-Gomez",
          "cluster_id": 2788117,
          "cite": [
            "781 F.3d 13",
            "2015 WL 1283956"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(134729 OR 9434573 OR 9434574) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 105,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 6,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 105,
        "triage_read": 8,
        "triage_snippet_classified": 97
      },
      "lane2_top_cited": {
        "query": "cites:(134729 OR 9434573 OR 9434574)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNSZzPTc4NjMwMyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28134729+OR+9434573+OR+9434574%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(134729 OR 9434573 OR 9434574)",
        "reviewed": 12,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 12,
        "triage_read": 0,
        "triage_snippet_classified": 12
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(134729 OR 9434573 OR 9434574)",
    "indexed_citing_opinions": 145,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 134729,
        "count": 109,
        "count_source": "search"
      },
      {
        "opinion_id": 9434573,
        "count": 39,
        "count_source": "search"
      },
      {
        "opinion_id": 9434574,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 217,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-flores-montano.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcxOTE4NjEmcz00ODY5MTM0JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28134729+OR+9434573+OR+9434574%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 134729,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134729,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134729,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134729,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134729,
        "cited_id": 112795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134729,
        "cited_id": 521938,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134729,
        "cited_id": 686763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134729,
        "cited_id": 776460,
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
    "date_created": "2026-07-05T23:56:13Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:56:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:56:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:00:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:56:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Flores-Montano

```
<div>
<center><b><span class="citation" data-id="9434573"><a href="/opinion/134729/united-states-v-flores-montano/" aria-description="Citation for case: United States v. Flores-Montano">541 U.S. 149</a></span> (2004)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
FLORES-MONTANO</h1></center>
<center>No. 02-1794.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 25, 2004.</center>
<center>Decided March 30, 2004.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><span class="star-pagination">*150</span> REHNQUIST, C. J., delivered the opinion for a unanimous Court. BREYER, J., filed a concurring opinion, <i>post,</i> p. 156.</p>
<p><i>Lisa S. Blatt</i> argued the cause for the United States. With her on the briefs were <i>Solicitor General Olson, Assistant Attorney General Wray, Deputy Solicitor General Dreeben, Daniel S. Goodman,</i> and <i>Alfonso Robles.</i></p>
<p><i>Steven F. Hubachek,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./540/1043/">540 U. S. 1043</a></span>, argued the cause for respondent. With him on the brief were <i>Vincent J. Brunkow</i> and <i>John C. Lemon.</i><sup>[*]</sup></p>
<p>CHIEF JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>Customs officials seized 37 kilograms  a little more than 81 pounds  of marijuana from respondent Manuel Flores-Montano's gas tank at the international border. The Court of Appeals for the Ninth Circuit, relying on an earlier decision by a divided panel of that court, <i>United States</i> v. <i>Molina-Tarazon,</i> <span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/" aria-description="Citation for case: United States v. Jose Molina-Tarazon">279 F. 3d 709</a></span> (2002), held that the Fourth Amendment forbade the fuel tank search absent reasonable suspicion. No. 02-50306, <span class="citation no-link">2003 WL 22410705</span> (Mar. 14, 2003). We hold that the search in question did not require reasonable suspicion.</p>
<p>Respondent, driving a 1987 Ford Taurus station wagon, attempted to enter the United States at the Otay Mesa Port of Entry in southern California. A customs inspector conducted an inspection of the station wagon, and requested respondent to leave the vehicle. The vehicle was then taken to a secondary inspection station.</p>
<p><span class="star-pagination">*151</span> At the secondary station, a second customs inspector inspected the gas tank by tapping it, and noted that the tank sounded solid. Subsequently, the inspector requested a mechanic under contract with Customs to come to the border station to remove the tank. Within 20 to 30 minutes, the mechanic arrived. He raised the car on a hydraulic lift, loosened the straps and unscrewed the bolts holding the gas tank to the undercarriage of the vehicle, and then disconnected some hoses and electrical connections. After the gas tank was removed, the inspector hammered off bondo (a putty-like hardening substance that is used to seal openings) from the top of the gas tank. The inspector opened an access plate underneath the bondo and found 37 kilograms of marijuana bricks. The process took 15 to 25 minutes.</p>
<p>A grand jury for the Southern District of California indicted respondent on one count of unlawfully importing marijuana, in violation of <span class="citation no-link">21 U. S. C. § 952</span>, and one count of possession of marijuana with intent to distribute, in violation of § 841(a)(1). Relying on <i><span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/" aria-description="Citation for case: United States v. Jose Molina-Tarazon">Molina-Tarazon</a></span>,</i> respondent filed a motion to suppress the marijuana recovered from the gas tank. In <i><span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/" aria-description="Citation for case: United States v. Jose Molina-Tarazon">Molina-Tarazon</a></span>,</i> a divided panel of the Court of Appeals held, <i>inter alia,</i> that removal of a gas tank requires reasonable suspicion in order to be consistent with the Fourth Amendment. <span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/#717" aria-description="Citation for case: United States v. Jose Molina-Tarazon">279 F. 3d, at 717</a></span>.</p>
<p>The Government advised the District Court that it was not relying on reasonable suspicion as a basis for denying respondent's suppression motion, but that it believed <i><span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/" aria-description="Citation for case: United States v. Jose Molina-Tarazon">Molina-Tarazon</a></span></i> was wrongly decided. The District Court, relying on <i><span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/" aria-description="Citation for case: United States v. Jose Molina-Tarazon">Molina-Tarazon</a></span>,</i> held that reasonable suspicion was required to justify the search and, accordingly, granted respondent's motion to suppress. The Court of Appeals, citing <i><span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/" aria-description="Citation for case: United States v. Jose Molina-Tarazon">Molina-Tarazon</a></span>,</i> summarily affirmed the District Court's judgment. No. 02-50306, <span class="citation no-link">2003 WL 22410705</span> (CA9, Mar. 14, 2003). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./540/945/">540 U. S. 945</a></span> (2003), and now reverse.</p>
<p><span class="star-pagination">*152</span> In <i><span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/" aria-description="Citation for case: United States v. Jose Molina-Tarazon">Molina-Tarazon</a></span>,</i> the Court of Appeals decided a case presenting similar facts to the one at bar. It asked "whether [the removal and dismantling of the defendant's fuel tank] is a `routine' border search for which no suspicion whatsoever is required." <span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/#711" aria-description="Citation for case: United States v. Jose Molina-Tarazon">279 F. 3d, at 711</a></span>. The Court of Appeals stated that "[i]n order to conduct a search that goes beyond the routine, an inspector must have reasonable suspicion," and the "critical factor" in determining whether a search is "routine" is the "degree of intrusiveness." <span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/#712" aria-description="Citation for case: United States v. Jose Molina-Tarazon"><i>Id.,</i> at 712-713</a></span>.</p>
<p>The Court of Appeals seized on language from our opinion in <i>United States</i> v. <i>Montoya de Hernandez,</i> <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S. 531</a></span> (1985), in which we used the word "routine" as a descriptive term in discussing border searches. <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#538" aria-description="Citation for case: United States v. Montoya De Hernandez"><i>Id.,</i> at 538</a></span> ("Routine searches of the persons and effects of entrants are not subject to any requirement of reasonable suspicion, probable cause, or warrant"); <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#541" aria-description="Citation for case: United States v. Montoya De Hernandez"><i>id.,</i> at 541, n. 4</a></span> ("Because the issues are not presented today we suggest no view on what level of suspicion, if any, is required for nonroutine border searches such as strip, body-cavity, or involuntary x-ray searches"). The Court of Appeals took the term "routine," fashioned a new balancing test, and extended it to searches of vehicles. But the reasons that might support a requirement of some level of suspicion in the case of highly intrusive searches of the person  dignity and privacy interests of the person being searched  simply do not carry over to vehicles. Complex balancing tests to determine what is a "routine" search of a vehicle, as opposed to a more "intrusive" search of a person, have no place in border searches of vehicles.</p>
<p>The Government's interest in preventing the entry of unwanted persons and effects is at its zenith at the international border. Time and again, we have stated that "searches made at the border, pursuant to the longstanding right of the sovereign to protect itself by stopping and examining persons and property crossing into this country, are reasonable simply by virtue of the fact that they occur at the <span class="star-pagination">*153</span> border." <i>United States</i> v. <i>Ramsey,</i> <span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#616" aria-description="Citation for case: United States v. Ramsey">431 U. S. 606, 616</a></span> (1977). Congress, since the beginning of our Government, "has granted the Executive plenary authority to conduct routine searches and seizures at the border, without probable cause or a warrant, in order to regulate the collection of duties and to prevent the introduction of contraband into this country." <i>Montoya de <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/" aria-description="Citation for case: United States v. Montoya De Hernandez">Hernandez, supra,</a></span></i> at 537 (citing <i><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">Ramsey, supra,</a></span></i> at 616-617 (citing Act of July 31, 1789, ch. 5, <span class="citation no-link">1 Stat. 29</span>)). The modern statute that authorized the search in this case, <span class="citation no-link">46 Stat. 747</span>, <span class="citation no-link">19 U. S. C. § 1581</span>(a),<sup>[1]</sup> derived from a statute passed by the First Congress, the Act of Aug. 4, 1790, ch. 35, § 31, <span class="citation no-link">1 Stat. 164</span>, see <i>United States</i> v. <i>Villamonte-Marquez,</i> <span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/#584" aria-description="Citation for case: United States v. Villamonte-Marquez">462 U. S. 579, 584</a></span> (1983), and reflects the "impressive historical pedigree" of the Government's power and interest, <span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/#585" aria-description="Citation for case: United States v. Villamonte-Marquez"><i>id.,</i> at 585</a></span>. It is axiomatic that the United States, as sovereign, has the inherent authority to protect, and a paramount interest in protecting, its territorial integrity.</p>
<p>That interest in protecting the borders is illustrated in this case by the evidence that smugglers frequently attempt to penetrate our borders with contraband secreted in their automobiles' fuel tank. Over the past 5½ fiscal years, there have been 18,788 vehicle drug seizures at the southern California ports of entry. App. to Pet. for Cert. 12a. Of those 18,788, gas tank drug seizures have accounted for 4,619 of the vehicle drug seizures, or approximately 25%. <i><span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/" aria-description="Citation for case: United States v. Villamonte-Marquez">Ibid.</a></span></i> In addition, instances of persons smuggled in and around gas tank compartments are discovered at the ports of entry of <span class="star-pagination">*154</span> San Ysidro and Otay Mesa at a rate averaging 1 approximately every 10 days. <i><span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/" aria-description="Citation for case: United States v. Villamonte-Marquez">Id.,</a></span></i> at 16a.</p>
<p>Respondent asserts two main arguments with respect to his Fourth Amendment interests. First, he urges that he has a privacy interest in his fuel tank, and that the suspicionless disassembly of his tank is an invasion of his privacy. But on many occasions, we have noted that the expectation of privacy is less at the border than it is in the interior. <i>Montoya de Hernandez, supra,</i> at 538. We have long recognized that automobiles seeking entry into this country may be searched. See <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#154" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 154</a></span> (1925) ("Travellers may be so stopped in crossing an international boundary because of national self protection reasonably requiring one entering the country to identify himself as entitled to come in, and his belongings as effects which may be lawfully brought in"). It is difficult to imagine how the search of a gas tank, which should be solely a repository for fuel, could be more of an invasion of privacy than the search of the automobile's passenger compartment.</p>
<p>Second, respondent argues that the Fourth Amendment "protects property as well as privacy," <i>Soldal</i> v. <i>Cook County,</i> <span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/#62" aria-description="Citation for case: Soldal v. Cook County">506 U. S. 56, 62</a></span> (1992), and that the disassembly and reassembly of his gas tank is a significant deprivation of his property interest because it may damage the vehicle. He does not, and on the record cannot, truly contend that the procedure of removal, disassembly, and reassembly of the fuel tank in this case or any other has resulted in serious damage to, or destruction of, the property.<sup>[2]</sup> According to <span class="star-pagination">*155</span> the Government, for example, in fiscal year 2003, 348 gas tank searches conducted along the southern border were negative (<i>i. e.,</i> no contraband was found), the gas tanks were reassembled, and the vehicles continued their entry into the United States without incident. Brief for United States 31.</p>
<p>Respondent cites not a single accident involving the vehicle or motorist in the many thousands of gas tank disassemblies that have occurred at the border. A gas tank search involves a brief procedure that can be reversed without damaging the safety or operation of the vehicle. If damage to a vehicle were to occur, the motorist might be entitled to recovery. See, <i>e. g.,</i> <span class="citation no-link">31 U. S. C. § 3723</span>; <span class="citation no-link">19 U. S. C. § 1630</span>. While the interference with a motorist's possessory interest is not insignificant when the Government removes, disassembles, and reassembles his gas tank, it nevertheless is justified by the Government's paramount interest in protecting the border.<sup>[3]</sup></p>
<p>For the reasons stated, we conclude that the Government's authority to conduct suspicionless inspections at the border includes the authority to remove, disassemble, and reassemble a vehicle's fuel tank. While it may be true that some <span class="star-pagination">*156</span> searches of property are so destructive as to require a different result, this was not one of them. The judgment of the United States Court of Appeals for the Ninth Circuit is therefore reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE BREYER, concurring.</p>
<p>I join the Court's opinion in full. I also note that Customs keeps track of the border searches its agents conduct, including the reasons for the searches. Tr. of Oral Arg. 53-54. This administrative process should help minimize concerns that gas tank searches might be undertaken in an abusive manner.</p>
<h2>NOTES</h2>
<p>[*]   <i>Daniel J. Popeo</i> and <i>Richard A. Samp</i> filed a brief for the Washington Legal Foundation et al. as <i>amici curiae</i> urging reversal.
</p>
<p><i>John Wesley Hall, Jr., David M. Siegel,</i> and <i>Lisa B. Kemler</i> filed a brief for the National Association of Criminal Defense Lawyers as <i>amicus curiae</i> urging affirmance.</p>
<p>[1]  Section 1581(a) provides:
</p>
<p>"Any officer of the customs may at any time go on board of any vessel or vehicle at any place in the United States or within the customs waters or, as he may be authorized, within a customs-enforcement area established under the Anti-Smuggling Act, or at any other authorized place, without as well as within his district, and examine the manifest and other documents and papers and examine, inspect, and search the vessel or vehicle and every part thereof and any person, trunk, package, or cargo on board, and to this end may hail and stop such vessel or vehicle, and use all necessary force to compel compliance."</p>
<p>[2]  Respondent's reliance on cases involving exploratory drilling searches is misplaced. See <i>United States</i> v. <i>Rivas,</i> <span class="citation" data-id="6976386"><a href="/opinion/7071868/united-states-v-rivas/" aria-description="Citation for case: United States v. Rivas">157 F. 3d 364</a></span> (CA5 1998) (drilling into body of trailer required reasonable suspicion); <i>United States</i> v. <i>Robles,</i> <span class="citation" data-id="686763"><a href="/opinion/686763/united-states-v-jose-robles/" aria-description="Citation for case: United States v. Jose Robles">45 F. 3d 1</a></span> (CA1 1995) (drilling into machine part required reasonable suspicion); <i>United States</i> v. <i>Carreon,</i> <span class="citation" data-id="521938"><a href="/opinion/521938/united-states-v-enrique-carreon/" aria-description="Citation for case: United States v. Enrique Carreon">872 F. 2d 1436</a></span> (CA10 1989) (drilling into camper required reasonable suspicion). We have no reason at this time to pass on the reasonableness of drilling, but simply note the obvious factual difference that this case involves the procedure of removal, disassembly, and reassembly of a fuel tank, rather than potentially destructive drilling. We again leave open the question "whether, and under what circumstances, a border search might be deemed `unreasonable' because of the particularly offensive manner in which it is carried out." <i>United States</i> v. <i>Ramsey,</i> <span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#618" aria-description="Citation for case: United States v. Ramsey">431 U. S. 606, 618, n. 13</a></span> (1977).</p>
<p>[3]  Respondent also argued that he has some sort of Fourth Amendment right not to be subject to delay at the international border and that the need for the use of specialized labor, as well as the hour actual delay here and the potential for even greater delay for reassembly are an invasion of that right. Respondent points to no cases indicating the Fourth Amendment shields entrants from inconvenience or delay at the international border.
</p>
<p>The procedure in this case took about an hour (including the wait for the mechanic). At oral argument, the Government advised us that, depending on the type of car, a search involving the disassembly and reassembly of a gas tank may take one to two hours. Tr. of Oral Arg. 10. We think it clear that delays of one to two hours at international borders are to be expected.</p>

</div>
```

---
