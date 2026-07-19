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

## GROUP: content/cases/Turner v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Turner v. United States"
type: case
citation: ""
parallel_cite: "582 U.S. 313; 137 S. Ct. 1885; 198 L. Ed. 2d 443; 26 Fla. L. Weekly Fed. S 700; 85 U.S.L.W. 4488"
neutral_cite: "2017 U.S. LEXIS 4041; 2017 WL 2674152"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2017
date_decided: 2017-06-22
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2017-06-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Turner v. United States
  varies_by_point: false
  scope_note: "Good law; applies the Brady/Bagley materiality standard and finds no violation on the record."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4403802/turner-v-united-states/"
  cluster_id: 4403802
  opinion_id: 4181055
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brady v. Maryland]]", "[[United States v. Bagley]]", "[[Kyles v. Whitley]]", "[[Strickler v. Greene]]", "[[Giglio v. United States]]"]
aliases: []
tags: ["case", "due-process", "brady"]
holding: "Counterweight: *Brady* materiality is demanding and judged on the whole record; the suppression here was immaterial — no *Brady* violation."
lake:
  record_id: Turner v. United States
  status: verified
  projected_at: 2026-07-06
---

# Turner v. United States

*582 U.S. 313 (2017)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Seven defendants were convicted of the 1984 group assault, robbery, and murder of Catherine Fuller in Washington, D.C. Decades later they learned the government had withheld several pieces of evidence, including the identity of an alternative suspect (McMillan) seen near the scene and a witness statement (Luchie) suggesting the attack might have involved one or two perpetrators rather than the large group the prosecution proved at trial. They sought relief under *[[Brady v. Maryland|Brady]]*.

## Issue
Whether the withheld evidence was "material" under *[[Brady v. Maryland]]*, such that its suppression deprived the defendants of a fair trial.

## Rule
The materiality test is demanding and is judged against the whole record: "[E]vidence is 'material' within the meaning of *Brady* when there is a reasonable probability that, had the evidence been disclosed, the result of the proceeding would have been different." — 582 U.S. 313, 137 S. Ct. 1885, 1893 (2017) (quoting *Cone v. Bell*). ^pin-1893

Reviewing the suppressed evidence against the entire record, the Court concluded "it is too little, too weak, or too distant from the main evidentiary points to meet *Brady*'s standards." — *Id.* at 1894. ^pin-1894

## Application
On this record the withheld evidence would have supported only an alternative "single attacker" theory, but a group attack was the cornerstone of the government's case and was confirmed by the consistent testimony of numerous eyewitnesses, several of whom admitted participating. Set against that body of evidence, the undisclosed items were too marginal to establish a reasonable probability of a different outcome. Because the suppressed evidence was immaterial, there was no *[[Brady v. Maryland|Brady]]* violation.

## Conclusion
The convictions were affirmed: the suppression, though it occurred, was not material and so worked no *[[Brady v. Maryland|Brady]]* violation. *[[Brady v. Maryland|Brady]]* materiality is measured against the entire trial record, not in isolation.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Turner* applies the unified materiality standard of [[United States v. Bagley]] and the cumulative, whole-record approach of [[Kyles v. Whitley]] to the disclosure duty of [[Brady v. Maryland]]; compare [[Strickler v. Greene]] (materiality not shown) and [[Smith v. Cain]] (materiality shown).

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *Turner v. United States*, 582 U.S. 313 (2017) — https://www.courtlistener.com/opinion/4403802/turner-v-united-states/ — pinpoints: 137 S. Ct. 1893, 1894 (CL text carries S. Ct. page-labels; U.S. Reports interior pages not embedded; cluster 4403802 → opinion 4181055).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c0652f4c25f3b978", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2017 U.S. LEXIS 4041; 2017 WL 2674152", "official_citation_present": false, "parallel_cite": "582 U.S. 313; 137 S. Ct. 1885; 198 L. Ed. 2d 443; 26 Fla. L. Weekly Fed. S 700; 85 U.S.L.W. 4488", "title": "Turner v. United States", "year": "2017"}}
{"assertion_id": "4293f45d663257a0", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Counterweight: *Brady* materiality is demanding and judged on the whole record; the suppression here was immaterial — no *Brady* violation.", "title": "Turner v. United States"}}
{"assertion_id": "8b21c758373a6539", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Key — Progeny / Refinement", "title": "Turner v. United States"}}
{"assertion_id": "479c6403eed7064e", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2017-06-22", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Turner v. United States", "field_i_validity": "good_law", "scope_note": "Good law; applies the Brady/Bagley materiality standard and finds no violation on the record.", "title": "Turner v. United States", "varies_by_point": "false"}}
{"assertion_id": "7ebdc4f4ac98600d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Turner v. United States"}}
```

### lake record — Turner v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Turner v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Turner v. United States",
    "case_name_short": "Turner",
    "case_name_full": "Charles S. TURNER, Et Al., Petitioners v. UNITED STATES. Russell L. Overton, Petitioner v. United States.",
    "input_case_name": "Turner v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2017-06-22",
    "year": 2017,
    "docket": null,
    "cluster_id": 4403802,
    "lead_opinion_id": 4181055,
    "sibling_ids": [
      4181055
    ],
    "absolute_url": "/opinion/4403802/turner-v-united-states/",
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
        "cite": "582 U.S. 313",
        "volume": "582",
        "reporter": "U.S.",
        "page": "313",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 S. Ct. 1885",
        "volume": "137",
        "reporter": "S. Ct.",
        "page": "1885",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "198 L. Ed. 2d 443",
        "volume": "198",
        "reporter": "L. Ed. 2d",
        "page": "443",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 700",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "700",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 U.S.L.W. 4488",
        "volume": "85",
        "reporter": "U.S.L.W.",
        "page": "4488",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2017 U.S. LEXIS 4041",
        "volume": "2017",
        "reporter": "U.S. LEXIS",
        "page": "4041",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 WL 2674152",
        "volume": "2017",
        "reporter": "WL",
        "page": "2674152",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "582 U.S. 313",
        "volume": "582",
        "reporter": "U.S.",
        "page": "313",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 U.S. LEXIS 4041",
        "volume": "2017",
        "reporter": "U.S. LEXIS",
        "page": "4041",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 S. Ct. 1885",
        "volume": "137",
        "reporter": "S. Ct.",
        "page": "1885",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "198 L. Ed. 2d 443",
        "volume": "198",
        "reporter": "L. Ed. 2d",
        "page": "443",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 700",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "700",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 U.S.L.W. 4488",
        "volume": "85",
        "reporter": "U.S.L.W.",
        "page": "4488",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 WL 2674152",
        "volume": "2017",
        "reporter": "WL",
        "page": "2674152",
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
      "id": "pin-1893",
      "page": null,
      "quote": "under *Brady v. Maryland*, such that its suppression deprived the defendants of a fair trial. ## Rule The materiality test is demanding and is judged against the whole record:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1894",
      "page": null,
      "quote": "it is too little, too weak, or too distant from the main evidentiary points to meet *Brady*'s standards.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2017-06-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Turner v. United States",
    "varies_by_point": false,
    "scope_note": "Good law; applies the Brady/Bagley materiality standard and finds no violation on the record.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. J. D. B.",
          "cluster_id": 10143633,
          "cite": [
            "326 Or. App. 237",
            "532 P.3d 99"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Fairley",
          "cluster_id": 4460856,
          "cite": [
            "880 F.3d 198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jabree Williams",
          "cluster_id": 4784203,
          "cite": [
            "974 F.3d 320"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul Browning v. Renee Baker",
          "cluster_id": 4427560,
          "cite": [
            "875 F.3d 444"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray Hooper v. David Shinn",
          "cluster_id": 4846381,
          "cite": [
            "985 F.3d 594"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Spencer",
          "cluster_id": 4421231,
          "cite": [
            "873 F.3d 1",
            "2017 WL 3614222",
            "2017 U.S. App. LEXIS 16129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Demarcus Sears v. Warden GDCP",
          "cluster_id": 9414470,
          "cite": [
            "73 F.4th 1269"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCray v. Capra",
          "cluster_id": 7857399,
          "cite": [
            "45 F.4th 634"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chavez v. State",
          "cluster_id": 10367631,
          "cite": [
            "837 S.E.2d 766",
            "307 Ga. 804"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Brown",
          "cluster_id": 9481052,
          "cite": [
            "2024 Ohio 749"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jeremiah Edwards",
          "cluster_id": 6469003,
          "cite": [
            "34 F.4th 570"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hunter",
          "cluster_id": 6461080,
          "cite": [
            "32 F.4th 22"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "White v. State",
          "cluster_id": 10680302,
          "cite": [
            "903 S.E.2d 891",
            "319 Ga. 367"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jimenez v. Stanford",
          "cluster_id": 9483027,
          "cite": [
            "96 F.4th 164"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sepulveda",
          "cluster_id": 9389969,
          "cite": [
            "64 F.4th 700"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hood v. State",
          "cluster_id": 10367761,
          "cite": [
            "860 S.E.2d 432",
            "311 Ga. 855"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Bruce, II",
          "cluster_id": 4846976,
          "cite": [
            "984 F.3d 884"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Solorio v. Muniz",
          "cluster_id": 9022945,
          "cite": [
            "896 F.3d 914"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Benson v. Kevin Chappell",
          "cluster_id": 4750615,
          "cite": [
            "958 F.3d 801"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony Juniper v. Melvin Davis",
          "cluster_id": 9414861,
          "cite": [
            "74 F.4th 196"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Martinez-Hernandez",
          "cluster_id": 10124638,
          "cite": [
            "118 F.4th 72"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marion Bowman, Jr. v. Bryan Stirling",
          "cluster_id": 7857669,
          "cite": [
            "45 F.4th 740"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Valas",
          "cluster_id": 6622618,
          "cite": [
            "40 F.4th 253"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeffrey Clark v. Louisville-Jefferson Cnty. Metro Gov't",
          "cluster_id": 10352228,
          "cite": [
            "130 F.4th 571"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holberg v. Guerrero",
          "cluster_id": 10352198,
          "cite": [
            "130 F.4th 493"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Turner v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4181055) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 58,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 58,
        "triage_read": 2,
        "triage_snippet_classified": 56
      },
      "lane2_top_cited": {
        "query": "cites:(4181055)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0wJnM9MTA4MDkwMjImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%284181055%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(4181055)",
        "reviewed": 27,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 27,
        "triage_read": 0,
        "triage_snippet_classified": 27
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4181055)",
    "indexed_citing_opinions": 68,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4181055,
        "count": 68,
        "count_source": "search"
      }
    ],
    "citation_count": 197,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/turner-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgzNjE0MjImcz05NDE0ODYxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%284181055%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4181055,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4181055,
        "cited_id": 102436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4181055,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4181055,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4181055,
        "cited_id": 111514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4181055,
        "cited_id": 117923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4181055,
        "cited_id": 118307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4181055,
        "cited_id": 145883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4181055,
        "cited_id": 620666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4181055,
        "cited_id": 1525310,
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
    "date_created": "2026-07-05T21:56:47Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:56:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:56:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:00:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:56:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Turner v. United States

```
(Slip Opinion)              OCTOBER TERM, 2016                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                 TURNER ET AL. v. UNITED STATES

     CERTIORARI TO THE DISTRICT OF COLUMBIA COURT OF 

                         APPEALS 


    No. 15–1503. Argued March 29, 2017—Decided June 22, 2017*

Petitioners—Timothy Catlett, Russell Overton, Levy Rouse, Kelvin
  Smith, Charles and Christopher Turner, and Clifton Yarborough—
  and several others were indicted for the kidnaping, robbery, and
  murder of Catherine Fuller. At trial, the Government advanced the
  theory that Fuller was attacked by a large group of individuals. Its
  evidentiary centerpiece consisted of the testimony of Calvin Alston
  and Harry Bennett, who confessed to participating in a group attack
  and cooperated with the Government in return for leniency. Several
  other Government witnesses corroborated aspects of Alston’s and
  Bennett’s testimony. Melvin Montgomery testified that he was in a
  park among a group of people, heard someone say they were “going to
  get that one,” saw petitioner Overton pointing to Fuller, and saw sev-
  eral persons, including some petitioners, cross the street in her direc-
  tion. Maurice Thomas testified that he saw the attack, identified
  some petitioners as participants, and later overheard petitioner Cat-
  lett say that they “had to kill her.” Carrie Eleby and Linda Jacobs
  testified that they heard screams coming from an alley where a “gang
  of boys” was beating someone near a garage, approached the group,
  and saw some petitioners participating in the attack. Finally, the
  Government played a videotape of petitioner Yarborough’s statement
  to detectives, describing how he was part of a large group that carried
  out the attack. None of the defendants rebutted the prosecution wit-
  nesses’ claims that Fuller was killed in a group attack. The seven pe-
  titioners were convicted.
     Long after their convictions became final, petitioners discovered
——————
  *Together with No. 15–1504, Overton v. United States, also on certio-
rari to the same court.
2                     TURNER v. UNITED STATES

                                 Syllabus

    that the Government had withheld evidence from the defense at the
    time of trial. In postconviction proceedings, they argued that seven
    specific pieces of withheld evidence were both favorable to the de-
    fense and material to their guilt under Brady v. Maryland, 373 U. S.
    83. This evidence included the identity of a man seen running into
    the alley after the murder and stopping near the garage where
    Fuller’s body had already been found; the statement of a passerby
    who claimed to hear groans coming from a closed garage; and evi-
    dence tending to impeach witnesses Eleby, Jacobs, and Thomas. The
    D. C. Superior Court rejected petitioners’ Brady claims, finding that
    the withheld evidence was not material. The D. C. Court of Appeals
    affirmed.
Held: The withheld evidence is not material under Brady. Pp. 9–14.
    (a) The Government does not contest petitioners’ claim that the
 withheld evidence was “favorable to the defense.” Petitioners and the
 Government, however, do contest the materiality of the undisclosed
 Brady information. Such “evidence is ‘material’ . . . when there is a
 reasonable probability that, had the evidence been disclosed, the re-
 sult of the proceeding would have been different.” Cone v. Bell, 556
 U. S. 449, 469–470. “A ‘reasonable probability’ of a different result”
 is one in which the suppressed evidence “ ‘undermines confidence in
 the outcome of the trial.’ ” Kyles v. Whitley, 514 U. S. 419, 434. To
 make that determination, this Court “evaluate[s]” the withheld evi-
 dence “in the context of the entire record.” United States v. Agurs,
 427 U. S. 97, 112. Pp. 9–11.
    (b) Petitioners’ main argument is that, had they known about the
 withheld evidence, they could have challenged the Government’s
 basic group attack theory by raising an alternative theory, namely,
 that a single perpetrator (or two at most) had attacked Fuller. Con-
 sidering the withheld evidence “in the context of the entire record,”
 Agurs, supra, at 112, that evidence is too little, too weak, or too dis-
 tant from the main evidentiary points to meet Brady’s standards.
    A group attack was the very cornerstone of the Government’s case,
 and virtually every witness to the crime agreed that Fuller was killed
 by a large group of perpetrators. It is not reasonably probable that
 the withheld evidence could have led to a different result at trial. Pe-
 titioners’ problem is that their current alternative theory would have
 had to persuade the jury that both Alston and Bennett falsely con-
 fessed to being active participants in a group attack that never oc-
 curred; that Yarborough falsely implicated himself in that group at-
 tack and yet gave a highly similar account of how it occurred; that
 Thomas, an otherwise disinterested witness, wholly fabricated his
 story; that both Eleby and Jacobs likewise testified to witnessing a
 group attack that did not occur; and that Montgomery in fact did not
                     Cite as: 582 U. S. ____ (2017)                    3

                                Syllabus

  see petitioners and others, as a group, identify Fuller as a target and
  leave together to rob her.
    As for the undisclosed impeachment evidence, the record shows
  that it was largely cumulative of impeachment evidence petitioners
  already had and used at trial. This is not to suggest that impeach-
  ment evidence is immaterial with respect to a witness who has al-
  ready been impeached with other evidence, see Wearry v. Cain, 577
  U. S. ___, ___–___. But in the context of this trial, with respect to
  these witnesses, the cumulative effect of the withheld evidence is in-
  sufficient to undermine confidence in the jury’s verdict, see Smith v.
  Cain, 565 U. S. 73, 75–76. Pp. 11–14.
116 A. 3d 894, affirmed.

  BREYER, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and KENNEDY, THOMAS, ALITO, and SOTOMAYOR, JJ., joined. KA-
GAN, J., filed a dissenting opinion, in which GINSBURG, J., joined. GOR-
SUCH, J., took no part in the consideration or decision of the cases.
                        Cite as: 582 U. S. ____ (2017)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                         Nos. 15–1503 and 15–1504
                                   _________________


     CHARLES S. TURNER, ET AL., PETITIONERS
15–1503               v.
                UNITED STATES

           RUSSELL L. OVERTON, PETITIONER
15–1504                   v.
                   UNITED STATES
 ON WRITS OF CERTIORARI TO THE DISTRICT OF COLUMBIA 

                  COURT OF APPEALS

                                 [June 22, 2017] 


  JUSTICE BREYER delivered the opinion of the Court.
  In Brady v. Maryland, 373 U. S. 83 (1963), this Court
held that the government violates the Constitution’s Due
Process Clause “if it withholds evidence that is favorable
to the defense and material to the defendant’s guilt or
punishment.” Smith v. Cain, 565 U. S. 73, 75 (2012)
(emphasis added) (summarizing Brady holding). In 1985
the seven petitioners in these cases were tried together in
the Superior Court for the District of Columbia for the
kidnaping, armed robbery, and murder of Catherine
Fuller. Long after petitioners’ convictions became final, it
emerged that the Government possessed certain evidence
that it failed to disclose to the defense. The only question
before us here is whether that withheld evidence was
“material” under Brady. The D. C. Superior Court, after a
16-day evidentiary hearing, determined that the withheld
2                TURNER v. UNITED STATES

                     Opinion of the Court

evidence was not material. Catlett v. United States, Crim.
No. 8617–FEL–84 etc. (Aug. 6, 2012), App. to Pet. for Cert.
in No. 15–1503, pp. 84a, n. 4, 81a–131a. The D. C. Court
of Appeals reviewed the record, reached the same conclu-
sion, and affirmed the Superior Court. 116 A. 3d 894
(2015). After reviewing the record, we reach the same
conclusion as did the lower courts.
                              I
  In these fact-intensive cases, we set out here only a
basic description of the record facts along with our reasons
for reaching our conclusion. We refer those who wish
more detail to the opinions of the lower courts. App. to
Pet. for Cert. in No. 15–1503, at 81a–131a; 116 A. 3d 894.
                            A
                         The Trial
  On March 22, 1985, a grand jury indicted the seven
petitioners—Timothy Catlett, Russell Overton, Levy
Rouse, Kelvin Smith, Charles Turner, Christopher Turner,
and Clifton Yarborough—and several others for the kid-
naping, robbery, and murder of Catherine Fuller. The
evidence produced at their joint trial showed that on
October 1, 1984, at around 4:30 p.m., Catherine Fuller left
her home to go shopping. At around 6 p.m., William
Freeman, a street vendor, found Fuller’s body inside an
alley garage between Eighth and Ninth Street N. E., just a
few blocks from Fuller’s home. See Appendix, infra (show-
ing a map of the area in which the murder was commit-
ted). Fuller had been robbed, severely beaten, and sodo-
mized with an object that caused extensive internal
injuries.
  The Government advanced the theory at trial that
Fuller had been attacked in the alley by a large group of
individuals, including petitioners; codefendants Steve
Webb, Alfonso Harris, and Felicia Ruffin; as well as by
                 Cite as: 582 U. S. ____ (2017)            3

                     Opinion of the Court

Calvin Alston and Harry Bennett. The Government’s
evidentiary centerpiece consisted of testimony by Alston
and Bennett, who confessed to participating in the offense
and who cooperated with the Government in return for
leniency. Although the testimony of Alston and Bennett
diverged on minor details, it was consistent in stating
that, and describing how, Fuller was attacked by a siz-
able group of individuals, including petitioners and they
themselves.
  Alston testified that at about 4:10 p.m. on the day of the
murder, he arrived in a park located on H Street between
Eighth and Ninth Streets. He said he found a group of
people gathered there. It included petitioners Levy Rouse,
Russell Overton, Christopher Turner, Charles Turner,
Kelvin Smith, Clifton Yarborough, and Timothy Catlett,
as well as several codefendants and others. Those in the
group were talking and singing while Catlett was banging
out a beat. Alston suggested “getting paid” by robbing
someone. App. A467. Catlett, Overton, Rouse, Smith,
Charles Turner, Christopher Turner, Yarborough, and
several others agreed. Alston pointed at Catherine Fuller,
who was walking on the other side of H Street near the
corner of H and Eighth Streets. Those in the group said
they were “game for getting paid.” Id., at A471–A472.
Alston, Rouse, Yarborough, and Charles Turner crossed H
Street moving toward Eighth Street and followed Fuller
down Eighth Street. The rest of the group crossed H
Street and moved toward Ninth Street. When Alston’s
group approached Fuller, Charles Turner shoved her into
an alley that runs between Eighth and Ninth Streets.
Charles Turner, Rouse, and Alston began punching Fuller.
They were soon joined by Christopher Turner, Smith, and
others. All of them continued to hit and kick Fuller until
she fell to the ground. Rouse and Charles Turner then
carried Fuller to the center of the alley and dropped her in
front of a garage located at the point where the alley joins
4               TURNER v. UNITED STATES

                     Opinion of the Court

another, perpendicular alley that runs toward I Street.
Someone dragged Fuller into the garage. Alston, Rouse,
Charles Turner, Overton, Yarborough, and Catlett fol-
lowed. Others stood outside. Members of the group tore
Fuller’s clothes off and struggled over her change purse.
Overton and Charles Turner then held Fuller’s legs, and
Alston, Catlett, Harris, and Yarborough stood around her
while Rouse sodomized her with a foot-long pipe. Shortly
after, the group dispersed and left the alley.
  Harry Bennett’s testimony was similar. Bennett also
described a group attack. He said that he had gone to the
H Street park, where he saw Rouse, Overton, Christopher
Turner, Smith, Catlett, and others gathered. Alston was
talking to the group about “[g]etting paid” and said “let’s
go get that lady.” Id., at A368–A370. At that point Alston,
Rouse, Overton, and Webb crossed H Street and ap-
proached Fuller, while Catlett, Christopher Turner,
Charles Turner, and Harris followed in a separate group.
Bennett added that he himself went to the corner of
Eighth and H Streets to watch for police. He then went
into the alley and joined the group in kicking and beating
Fuller. He testified that at least 12 people were there,
with some beating Fuller and others watching or picking
up her jewelry. Overton then dragged Fuller into the
garage, and Bennett, Rouse, Christopher Turner, Charles
Turner, Catlett, Smith, Harris, and Webb followed, as did
some “girls.” Id., at A402–A405. Alston and Steve Webb
held Fuller’s legs, and Rouse sodomized her with a pole.
The group then dispersed from the garage and alley.
  The Government presented several other witnesses who
corroborated aspects of Alston’s and Bennett’s testimony,
including the fact that Fuller was attacked by a group.
Melvin Montgomery testified that he was in the H Street
park on the afternoon of the murder. He saw Overton,
Catlett, Rouse, Charles Turner, and others gathered there.
The group was being noisy and singing a song about need-
                 Cite as: 582 U. S. ____ (2017)          5

                     Opinion of the Court

ing money. Somebody then said they were “going to get
that one,” and Montgomery saw that Overton was pointing
to a woman standing on the corner of Eighth Street. Id.,
at 77–79. Overton, Catlett, Rouse, Charles Turner, and
others crossed H Street. Some headed toward Eighth
Street while others went toward Ninth Street. Montgom-
ery did not follow them.
  Maurice Thomas, then 14 years old, testified that he
witnessed the attack itself. Thomas lived in the neighbor-
hood and knew many of the defendants. As he was walk-
ing home, he glanced down the Eighth Street alley and
saw a group surrounding Fuller. Thomas saw Catlett pat
Fuller down and then hit her. He then saw everyone in
the group join in hitting her. Thomas said he knew Cat-
lett, Yarborough, Rouse, Charles Turner, Christopher
Turner, and Smith and recognized them in the group.
Thomas heard Fuller calling for help. He ran home where
he found his aunt, who told him not to tell anyone what he
saw. Later that day, Thomas saw Catlett at a corner
store, and heard Catlett say to someone that they “had to
kill her” because “she spotted someone he was with.” Id.,
at 127–128.
  On the afternoon of the murder, Carrie Eleby and Linda
Jacobs were looking for petitioner Smith, who was Eleby’s
boyfriend, near the corner of H and Eighth Streets. They
heard screams coming from where a “gang of boys” was
beating somebody near the garage in the alley. Id., at
A539–A541. Eleby and Jacobs approached the group.
Eleby recognized Christopher Turner, Smith, Catlett,
Rouse, Overton, Alston, and Webb kicking Fuller while
Yarborough stood nearby. Both Eleby and Jacobs testified
that they saw Rouse sodomize Fuller with a pole. Eleby
added that Overton held Fuller’s legs.
  Finally, the Government played a videotape of a recorded
statement that Yarborough, one of the petitioners, had
given to detectives on December 9, 1984, approximately
6                TURNER v. UNITED STATES

                      Opinion of the Court

two months after the murder. Names were redacted. The
video shows Yarborough describing in detail how he was
part of a large group that forced Fuller into the alley,
jointly robbed and assaulted her, and dragged her into the
garage.
   None of the defendants testified, nor did any of them
try, through witnesses or other evidence, to rebut the
prosecution witnesses’ claim that Fuller was killed in a
group attack. Rather, each petitioner pursued what was
essentially a “not me, maybe them” defense, namely, that
he was not part of the group that attacked Fuller. Each
tried to establish this defense by impeaching witnesses
who had placed that particular petitioner at the scene.
Some, for example, provided evidence that Eleby and
Jacobs had used PCP the day of Fuller’s murder. Some
also tried to establish alibis for the time of Fuller’s death.
   The jury convicted all seven petitioners, along with
codefendant Steve Webb (who subsequently died). The
jury acquitted codefendants Alfonso Harris and Felicia
Ruffin. On direct appeal, the D. C. Court of Appeals af-
firmed petitioners’ convictions, though it remanded for
resentencing. 545 A. 2d 1202, 1219 (1988). The trial court
resentenced petitioners to the same amount of prison time.
App. to Pet. for Cert. in No. 15–1503, at 82a, n. 2.
                             B
                     The Brady Claims
   Beginning in 2010, petitioners pursued postconviction
proceedings in which they sought to vacate their convic-
tions or to be granted a new trial. App. to Pet. for Cert. in
No. 15–1503, at 84a, n. 4. After petitioners’ convictions
became final, it emerged that the Government possessed
certain evidence that it had withheld from the defense at
the time of trial. Petitioners discovered other withheld
evidence in their review of the trial prosecutor’s case file,
which the Government turned over to petitioners in the
                 Cite as: 582 U. S. ____ (2017)           7

                     Opinion of the Court

course of the postconviction proceedings. Among other
postconviction claims, petitioners contended that the
withheld evidence was both favorable and material, enti-
tling them to relief under Brady.
   The D. C. Superior Court considered petitioners’ Brady
claims as part of a 16-day evidentiary hearing. It rejected
those claims, finding that “none of the undisclosed infor-
mation was material.” App. to Pet. for Cert. in No. 15–
1503, at 130a. The D. C. Court of Appeals affirmed. 116
A. 3d, at 901. It similarly concluded that the withheld
evidence was not material under Brady. 116 A. 3d, at
913–926. At issue in those proceedings were the following
seven specific pieces of evidence:
   1. The identity of James McMillan. Freeman, the ven-
dor who discovered Fuller’s body in the alley garage,
testified at trial that, while he was waiting for police to
arrive, he saw two men run into the alley and stop near
the garage for about five minutes before running away
when an officer approached. One of the men had a bulge
under his coat. Early in the trial, codefendant Harris’
counsel had requested the identity of the two men to
confirm that her client was not one of them. But the
Government refused to disclose the men’s identity.
   In their postconviction review of the prosecutor’s files,
petitioners learned that Freeman had identified the two
men he saw in the alley as James McMillan and Gerald
Merkerson. McMillan lived in a house which opens in the
back onto a connecting alley. In the weeks following
Fuller’s murder, but before petitioners’ trial, McMillan
was arrested for beating and robbing two women in the
neighborhood. Neither attack included a sexual assault.
Separately, petitioners learned that seven years after
petitioners’ trial, McMillan had robbed, sodomized, and
murdered a young woman in an alley.
   2. The interview with Willie Luchie. The prosecutor’s
notes also recorded an undisclosed interview with Willie
8                TURNER v. UNITED STATES

                     Opinion of the Court

Luchie, who told the prosecutor that he and three others
walked through the alley on their way to an H Street
liquor store between 5:30 and 5:45 p.m. on the evening of
the murder. As the group walked by the garage, Luchie
“heard several groans” and “remembers the doors to the
garage being closed.” App. 25. Another person in the
group recalled “hear[ing] some moans,” while the other
two persons did not recall hearing anything unusual. Id.,
at 27, 53; id., at A992. The group continued walking
without looking into the garage or otherwise investigating
the source of the sounds. They did not see McMillan or
any other person in the alley when they passed through.
   3. The interviews with Ammie Davis. Undisclosed notes
written by a police officer and the prosecutor refer to two
interviews with Ammie Davis, who had been arrested for
disorderly conduct a few weeks after Fuller’s murder.
Davis initially told a police investigator that she had seen
another individual, James Blue, beat Fuller to death in
the alley. Shortly thereafter, she said she only saw Blue
grab Fuller and push her into the alley. Davis also said
that a girlfriend, whom she did not name, accompanied
her. She promised to call the investigator with more
details, but she did not do so.
   About 9 months later (after petitioners were indicted
but approximately 11 weeks before their trial), a prosecu-
tor learned of the investigator’s notes and interviewed
Davis. The prosecutor’s notes state that Davis did not
provide any more details, except to say that the girlfriend
who accompanied her was nicknamed “ ‘Shorty.’ ” Id., at
267–268. About two months later, which was shortly
before petitioners’ trial, Blue murdered Davis in an unre-
lated drug dispute.
   During the postconviction evidentiary hearing, the
prosecutor who interviewed Davis testified that he did not
disclose Davis’ statement because she acted “playful” and
“not serious” during the interview and he found her to be
                 Cite as: 582 U. S. ____ (2017)           9

                     Opinion of the Court

“totally incredible.” Id., at 269–272. Additionally, the
prosecutor stated that he knew Davis had previously
falsely accused Blue of a different murder, and on another
occasion had falsely accused a different individual of a
different murder.
  4. Impeachment of Kaye Porter and Carrie Eleby. Kaye
Porter accompanied Eleby during an initial interview with
homicide detectives. Porter agreed with Eleby that she
had also heard Alston state that he was involved in rob-
bing Fuller. An undisclosed prosecutorial note states that
in a later interview with detectives, Porter stated that she
did not actually recall hearing Alston’s statement and just
went along with what Eleby said. The note also states
that Eleby likewise admitted that she had lied about
Porter being present during Alston’s statement and had
asked Porter to support her.
  5. Impeachment of Carrie Eleby. A prosecutor’s un-
disclosed note revealed that Eleby said she had been
high on PCP during a January 9, 1985, meeting with
investigators.
  6. Impeachment of Linda Jacobs. An undisclosed note of
an interview with Linda Jacobs said that the detective had
“question[ed] her hard,” and that she had “vacillated”
about what she saw. Id., at A1009. The prosecutor re-
called that the detective “kept raising his voice” and was
“smacking his hand on the desk” during the interview.
Id., at A2298–A2299.
  7. Impeachment of Maurice Thomas. An undisclosed
note of an interview with Maurice Thomas’ aunt stated
that she “does not recall Maurice ever telling her anything
such as this.” Id., at A1010; see id., at 295–296.
                           II
                           A
  The Government does not contest petitioners’ claim
that the withheld evidence was “favorable to the accused,
10                TURNER v. UNITED STATES

                      Opinion of the Court

either because it is exculpatory, or because it is impeach-
ing.” Strickler v. Greene, 527 U. S. 263, 281–282 (1999).
Neither does the Government contest petitioners’ claim
that it “suppressed” the evidence, “either willfully or
inadvertently.” Id., at 282. It does, as it must, concede
that the Brady rule’s “ ‘overriding concern [is] with the
justice of the finding of guilt,’ ” United States v. Bagley,
473 U. S. 667, 678 (1985) (quoting United States v. Agurs,
427 U. S. 97, 112 (1976)), and that the Government’s
“ ‘interest . . . in a criminal prosecution is not that it shall
win a case, but that justice shall be done,’ ” Kyles v. Whit-
ley, 514 U. S. 419, 439 (1995) (quoting Berger v. United
States, 295 U. S. 78, 88 (1935)). Consistent with these
principles, the Government assured the Court at oral
argument that subsequent to petitioners’ trial, it has
adopted a “generous policy of discovery” in criminal cases
under which it discloses any “information that a defendant
might wish to use.” Tr. of Oral Arg. 47–48. As we have
recognized, and as the Government agrees, ibid., “[t]his is
as it should be.” Kyles, supra, at 439 (explaining that a
“ ‘prudent prosecutor[’s]’ ” better course is to take care to
disclose any evidence favorable to the defendant (quoting
Agurs, supra, at 108)).
    Petitioners and the Government, however, do contest
the materiality of the undisclosed Brady information.
“[E]vidence is ‘material’ within the meaning of Brady
when there is a reasonable probability that, had the evi-
dence been disclosed, the result of the proceeding would
have been different.” Cone v. Bell, 556 U. S. 449, 469–470
(2009) (citing Bagley, supra, at 682). “A ‘reasonable prob-
ability’ of a different result” is one in which the suppressed
evidence “ ‘undermines confidence in the outcome of the
trial.’ ” Kyles, supra, at 434 (quoting Bagley, supra, at
678). In other words, petitioners here are entitled to a
new trial only if they “establis[h] the prejudice necessary
to satisfy the ‘materiality’ inquiry.” Strickler, supra, at
                 Cite as: 582 U. S. ____ (2017)          11

                     Opinion of the Court

282.
  Consequently, the issue before us here is legally simple
but factually complex. We must examine the trial record,
“evaluat[e]” the withheld evidence “in the context of the
entire record,” Agurs, supra, at 112, and determine in light
of that examination whether “there is a reasonable prob-
ability that, had the evidence been disclosed, the result of
the proceeding would have been different.” Cone, supra,
at 470 (citing Bagley, supra, at 682). Having done so, we
agree with the lower courts that there was no such rea-
sonable probability.
                             B
  Petitioners’ main argument is that, had they known
about McMillan’s identity and Luchie’s statement, they
could have challenged the Government’s basic theory that
Fuller was killed in a group attack. Petitioners contend
that they could have raised an alternative theory, namely,
that a single perpetrator (or two at most) had attacked
Fuller. According to petitioners, the groans that Luchie
and his companion heard when they walked through the
alley between 5:30 and 5:45 p.m. suggest that the attack
was taking place inside the garage at that moment. The
added facts that the garage was small and that Luchie’s
group saw no one in the alley could bolster a “single at-
tacker” theory. Freeman’s recollection that one garage
door was open when he found Fuller’s body at around 6
p.m., combined with Luchie’s recollection that both doors
were shut around 5:30 or 5:45 p.m., could suggest that one
or two perpetrators were in the garage when Luchie
walked by but left before Freeman arrived. McMillan’s
identity as one of the men Freeman saw enter the alley
after Freeman discovered Fuller’s body would have re-
vealed McMillan’s criminal convictions in the months
before petitioners’ trial. Petitioners argue that together,
this evidence would have permitted the defense to knit
12               TURNER v. UNITED STATES

                     Opinion of the Court

together a theory that the group attack did not occur at
all—and that it was actually McMillan, alone or with an
accomplice, who murdered Fuller. They add that they
could have used the investigators’ failure to follow up on
Ammie Davis’ claim about James Blue, and the various
pieces of withheld impeachment evidence, to suggest that
an incomplete investigation had ended up accusing the
wrong persons.
   Considering the withheld evidence “in the context of the
entire record,” however, Agurs, supra, at 112, we conclude
that it is too little, too weak, or too distant from the main
evidentiary points to meet Brady’s standards. As petition-
ers recognize, McMillan’s guilt (or that of any other single,
or near single, perpetrator) is inconsistent with petition-
ers’ guilt only if there was no group attack. But a group
attack was the very cornerstone of the Government’s case.
The witnesses may have differed on minor details, but
virtually every witness to the crime itself agreed as to a
main theme: that Fuller was killed by a large group of
perpetrators. The evidence at trial was such that, even
though petitioners knew that Freeman saw two men enter
the alley after he discovered Fuller’s body, that one ap-
peared to have a bulky object hidden under his coat, and
that both ran when the police arrived, none of the peti-
tioners attempted to mount a defense that implicated
those men as alternative perpetrators acting alone.
   Is it reasonably probable that adding McMillan’s identity,
and Luchie’s ambiguous statement that he heard groans
but saw no one, could have led to a different result at
trial? We conclude that it is not. The problem for peti-
tioners is that their current alternative theory would have
had to persuade the jury that both Alston and Bennett
falsely confessed to being active participants in a group
attack that never occurred; that Yarborough falsely impli-
cated himself in that group attack and, through coordinated
effort or coincidence, gave a highly similar account of
                 Cite as: 582 U. S. ____ (2017)           13

                     Opinion of the Court

how it occurred; that Thomas, a disinterested witness who
recognized petitioners when he happened upon the attack
and heard Catlett refer to it later that night, wholly fabri-
cated his story; that both Eleby and Jacobs likewise testi-
fied to witnessing a group attack that did not occur; and
that Montgomery in fact did not see petitioners and oth-
ers, as a group, identify Fuller as a target and leave the
park to rob her.
   With respect to the undisclosed impeachment evidence,
the record shows that it was largely cumulative of im-
peachment evidence petitioners already had and used at
trial. For example, the jury heard multiple times about
Eleby’s frequent PCP use, including Eleby’s own testimony
that she and Jacobs had smoked PCP shortly before they
witnessed Fuller’s attack. In this context, it would not
have surprised the jury to learn that Eleby used PCP on
yet another occasion. Porter was a minor witness who was
also impeached at trial with evidence about changes in her
testimony over time, leaving little added significance to
the note that she changed her mind about having agreed
with Eleby’s claims. The jury was also well aware of
Jacobs’ vacillation, as she was impeached on the stand
with her shifting stories about what she witnessed.
Knowledge that a detective raised his voice during an
interview with her would have added little more. Nor do
we see how the note about the statement by Thomas’ aunt
could have mattered much, given the facts that neither
side chose to call the aunt as a witness and that the jury
already knew, from Thomas’ testimony, that his aunt had
told him not to tell anyone what he saw. As for James
Blue, petitioners argue that the investigators’ delay in
following up on Ammie Davis’ statement could have led
the jury to doubt the thoroughness of the investigation.
But this likelihood is seriously undercut by notes about
Davis’ demeanor and lack of detail, and by her prior false
accusations that Blue committed a different murder and
14                TURNER v. UNITED STATES

                      Opinion of the Court

that yet another person committed yet a different murder.
   We of course do not suggest that impeachment evidence
is immaterial with respect to a witness who has already
been impeached with other evidence. See Wearry v. Cain,
577 U. S. ___, ___–___ (2016) (per curiam) (slip op., at 7–9).
We conclude only that in the context of this trial, with
respect to these witnesses, the cumulative effect of the
withheld evidence is insufficient to “ ‘undermine confi-
dence’ ” in the jury’s verdict, Smith, 565 U. S., at 75–76
(quoting Kyles, 514 U. S., at 434; brackets omitted).
                              III
   On the basis of our review of the record, we agree with
the lower courts that there is not a “reasonable probabil-
ity” that the withheld evidence would have changed the
outcome of petitioners’ trial, id., at 434 (internal quotation
marks omitted). The judgment of the D. C. Court of Ap-
peals, accordingly, is affirmed.
                                               It is so ordered.

  JUSTICE GORSUCH took no part in the consideration or
decision of these cases.
 Cite as: 582 U. S. ____ (2017) 
     15

     Opinion
Appendix      of the of
         to opinion  Court
                        the Court 


         APPENDIX

                 Cite as: 582 U. S. ____ (2017)          1

                     KAGAN, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                  Nos. 15–1503 and 15–1504
                         _________________


     CHARLES S. TURNER, ET AL., PETITIONERS
15–1503               v.
                UNITED STATES

          RUSSELL L. OVERTON, PETITIONER
15–1504                  v.
                  UNITED STATES
 ON WRITS OF CERTIORARI TO THE DISTRICT OF COLUMBIA 

                  COURT OF APPEALS

                        [June 22, 2017] 


  JUSTICE KAGAN, with whom JUSTICE GINSBURG joins,
dissenting.
  Consider two criminal cases. In the first, the govern-
ment accuses ten defendants of acting together to commit
a vicious murder and robbery. At trial, each defendant
accepts that the attack occurred almost exactly as the
government describes—contending only that he wasn’t
part of the rampaging group. The defendants thus un-
dermine each other’s arguments at every turn. In the
second case, the government makes the same arguments
as before. But this time, all of the accused adopt a com-
mon defense, built around an alternative account of the
crime. Armed with new evidence that someone else perpe-
trated the murder, the defendants vigorously dispute the
government’s gang-attack narrative and challenge the
credibility of its investigation. The question this case
presents is whether such a unified defense, relying on
evidence unavailable in the first scenario, had a “reason-
able probability” (less than a preponderance) of shifting
2                TURNER v. UNITED STATES

                     KAGAN, J., dissenting

even one juror’s vote. Cone v. Bell, 556 U. S. 449, 452, 470
(2009); see Kyles v. Whitley, 514 U. S. 419, 434 (1995).
   That is the relevant question because the Government
here knew about but withheld the evidence of an alterna-
tive perpetrator—and so prevented the defendants from
coming together to press that theory of the case. If the
Government’s non-disclosure was material, in the sense
just described, this Court’s decision in Brady v. Maryland,
373 U. S. 83 (1963), demands a new trial. The Court today
holds it was not material: In light of the evidence the
Government offered, the majority argues, the transformed
defense stood little chance of persuading a juror to vote to
acquit. That conclusion is not indefensible: The Govern-
ment put on quite a few witnesses who said that the de-
fendants committed the crime. But in the end, I think the
majority gets the answer in this case wrong. With the
undisclosed evidence, the whole tenor of the trial would
have changed. Rather than relying on a “not me, maybe
them” defense, ante, at 6, all the defendants would have
relentlessly impeached the Government’s (thoroughly
impeachable) witnesses and offered the jurors a way to
view the crime in a different light. In my view, that could
well have flipped one or more jurors—which is all Brady
requires.
   Before explaining that view, I note that the majority
and I share some common ground. We agree on the uni-
verse of exculpatory or impeaching evidence suppressed in
this case: The majority’s description of that evidence, and
of the trial held without it, is scrupulously fair. See ante,
at 2–6, 7–9. We also agree—as does the Government—
that such evidence ought to be disclosed to defendants as a
matter of course. See ante, at 10. Constitutional require-
ments aside, turning over exculpatory materials is a core
responsibility of all prosecutors—whose professional inter-
est and obligation is not to win cases but to ensure justice
is done. See Kyles, 514 U. S., at 439. And finally, we
                 Cite as: 582 U. S. ____ (2017)           3

                     KAGAN, J., dissenting

agree on the legal standard by which to assess the materi-
ality of undisclosed evidence for purposes of applying the
constitutional rule: Courts are to ask whether there is a
“reasonable probability” that disclosure of the evidence
would have led to a different outcome—i.e., an acquittal or
hung jury rather than a conviction. See ante, at 10.
  But I part ways with the majority in applying that
standard to the evidence withheld in this case. That
evidence falls into three basic categories, discussed below.
Taken together, the materials would have recast the trial
significantly—so much so as to “undermine[] confidence”
in the guilty verdicts reached in their absence. Kyles, 514
U. S., at 434.
  First, the Government suppressed information identify-
ing a possible alternative perpetrator. The defendants
knew that, shortly before the police arrived, witnesses had
observed two men acting suspiciously near the alleyway
garage where Catherine Fuller’s body was found. But
they did not know—because the Government never told
them—that a witness had identified one of those men as
James McMillan. Equipped with that information, the
defendants would have discovered that in the weeks fol-
lowing Fuller’s murder, McMillan assaulted and robbed
two other women of comparable age in the same neighbor-
hood. And using that information, the defendants would
have united around a common defense. They would all
have pointed their fingers at McMillan (rather than at
each other), arguing that he committed Fuller’s murder as
part of a string of similar crimes.
  Second, the Government suppressed witness statements
suggesting that one or two perpetrators—not a large
group—carried out the attack. Those statements were
given by two individuals who walked past the garage
around the time of Fuller’s death. They told the police
that they heard groans coming from inside the garage; and
one remarked that the garage’s doors were closed at the
4                TURNER v. UNITED STATES

                     KAGAN, J., dissenting

time. Introducing that evidence at trial would have sown
doubt about the Government’s group-attack narrative,
because that many people (as everyone agrees) couldn’t
have fit inside the small garage. And the questions thus
raised would have further supported the defendants’
theory that McMillan (and perhaps an accomplice) had
committed the murder.
   Third and finally, the Government suppressed a raft of
evidence discrediting its investigation and impeaching its
witnesses. Undisclosed files, for example, showed that the
police took more than nine months to look into a witness’s
claim that a man named James Blue had murdered Fuller.
Evidence of that kind of negligence could easily have led
jurors to wonder about the competence of all the police
work done in the case. Other withheld documents re-
vealed that one of the Government’s main witnesses was
high on PCP when she met with investigators to identify
participants in the crime—and that she also encouraged a
friend to lie to the police to support her story. Using that
sort of information, see also ante, at 9, the defendants
could have undercut the Government’s witnesses—even
while presenting their own account of the murder.
   In reply to all this, the majority argues that “none of the
[accused] attempted to mount [an alternative-perpetrator]
defense” and that such a defense would have challenged
“the very cornerstone of the Government’s case.” Ante, at
12. But that just proves my point. The defendants didn’t
offer an alternative-perpetrator defense because the Gov-
ernment prevented them from learning what made it
credible: that one of the men seen near the garage had a
record of assaulting and robbing middle-aged women, and
that witnesses would back up the theory that only one or
two individuals had committed the murder. Moreover,
that defense had game-changing potential exactly because
it challenged the cornerstone of the Government’s case.
Without the withheld evidence, each of the defendants had
                 Cite as: 582 U. S. ____ (2017)           5

                     KAGAN, J., dissenting

little choice but to accept the Government’s framing of the
crime as a group attack—and argue only that he wasn’t
there. That meant the defendants often worked at cross-
purposes. In particular, each defendant not identified by a
Government witness sought to bolster that witness’s
credibility, no matter the harm to his co-defendants. As
one defense lawyer remarked after another’s supposed
cross-examination of a Government witness: “They’ve got
[an extra] prosecutor[ ] in the courtroom now.” Saperstein
& Walsh, 10 Defendants Complicate Trial, Washington
Post, Nov. 17, 1985, p. A14, col. 1. Credible alternative-
perpetrator evidence would have allowed the defendants
to escape this cycle of mutually assured destruction. By
enabling the defendants to jointly attack the Govern-
ment’s “cornerstone” theory, the withheld evidence would
have reframed the case presented to the jury.
   Still, the majority claims, an alternative-perpetrator
defense would have had no realistic chance of changing
the outcome because the Government had ample evidence
of a group attack, including five witnesses who testified
that they had participated in it or seen it happen. See
ante, at 12–13. But the Government’s case wasn’t nearly
the slam-dunk the majority suggests. No physical evi-
dence tied any of the defendants to the crime—a highly
surprising fact if, as the Government claimed, more than
ten people carried out a spur-of-the-moment, rampage-like
attack in a confined space. And as even the majority
recognizes, the Government’s five eyewitnesses had some
serious credibility deficits. See ibid. Two had been
charged as defendants, and agreed to testify only in ex-
change for favorable plea deals. See 116 A. 3d 894, 902
(D. C. 2015). Two admitted they were high on PCP at the
time. See id., at 903, 911; App. A535–A536, A649. (As
noted above, one was also high when she later met with
police to identify the culprits.) One was an eighth-grader
whose own aunt contradicted parts of his trial testimony.
6                TURNER v. UNITED STATES

                     KAGAN, J., dissenting

See 116 A. 3d, at 903, 911. Even in the absence of an
alternative account of the crime, the jury took more than a
week—and many dozens of votes—to reach its final ver-
dict. Had the defendants offered a unified counter-
narrative, based on the withheld evidence, one or more
jurors could well have concluded that the Government had
not proved its case beyond a reasonable doubt.
   Again, the issue here concerns the difference between
two criminal cases. The Government got the case it most
wanted—the one in which the defendants, each in an
effort to save himself, formed something of a circular firing
squad. And the Government avoided the case it most
feared—the one in which the defendants acted jointly to
show that a man known to assault women like Fuller
committed her murder. The difference between the two
cases lay in the Government’s files—evidence of obvious
relevance that prosecutors nonetheless chose to suppress.
I think it could have mattered to the trial’s outcome. For
that reason, I respectfully dissent.

```

---

## GROUP: content/cases/United States v. Aigbekaen.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Aigbekaen
type: case
citation: "943 F.3d 713 (2019)"
parallel_cite: ""
neutral_cite: ""
court: 4th Cir. 2019
court_level: coa
circuit: ca4
year: 2019
date_decided: 2019-11-21
docket: 17-4109
authority_weight: "Binding in-circuit — 4th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4680725/united-states-v-raymond-aigbekaen/"
  cluster_id: 4680725
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Aigbekaen
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Border Searches]]"
    role: Key
related:
  - "[[Border Searches]]"
  - "[[Riley v. California]]"
  - "[[United States v. Cotterman]]"
tags:
  - case
  - fourth-amendment
  - search
  - border-search
  - digital-privacy
  - good-faith-exception
holding: "The border-search exception does not authorize a warrantless, nonroutine forensic search of a returning traveler's electronic devices unless the government's individualized suspicion bears some nexus to the exception's historic purposes — protecting national security, collecting duties, blocking unwanted entrants, or intercepting contraband; suspicion of purely domestic crimes is not enough, so the forensic searches of Aigbekaen's devices violated the Fourth Amendment, though the good-faith exception barred suppression."
---

# United States v. Aigbekaen

*943 F.3d 713 (4th Cir. 2019)* (No. 17-4109) · U.S. Court of Appeals for the Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 4680725 → opinion 4457978 (943 F.3d 713, decided 2019-11-21); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
A sixteen-year-old runaway told police that Raymond Aigbekaen and another man had trafficked her for sex across Maryland, Virginia, and New York. Homeland Security Investigations built a case tying Aigbekaen to the trafficking. When Aigbekaen returned to the United States from abroad in May 2015, agents seized his MacBook Pro, iPhone, and iPod at the airport and conducted warrantless forensic searches of all three devices under the border-search exception. He was charged with sex trafficking and related crimes and convicted after a nine-day trial; he appealed the denial of his motion to suppress the device evidence.

## Issue
Whether the border-search exception permits warrantless, nonroutine forensic searches of a returning traveler's electronic devices when the government's individualized suspicion concerns purely domestic crimes with no nexus to the historic rationales of the border-search doctrine.

## Rule
Building on *[[United States v. Kolsuz]]*, the Fourth Circuit held that to conduct an intrusive, nonroutine border search without a warrant, the government must have individualized suspicion of an offense bearing some nexus to the exception's purposes — protecting national security, collecting duties, blocking the entry of unwanted persons, or disrupting the import or export of contraband: "where a search at the border is so intrusive as to require some level of individualized suspicion, the object of that suspicion must bear some nexus to the purposes of the border search exception in order for the exception to apply. Because no such nexus existed here, the warrantless, nonroutine forensic searches violated the Fourth Amendment." — slip op. at 14.

## Application
HSI had probable cause to suspect Aigbekaen of grave domestic crimes, but that suspicion was "entirely unmoored" from the sovereign interests underlying the border-search exception. The Government's fallback theories failed: no affidavit ever alleged the devices held child pornography, and treating any "criminal" who carries the "instrumentalities" of a domestic offense across the border as supplying a nexus would erase the exception's distinction from a "generalized interest in law enforcement." Because no border nexus existed, the forensic searches were unconstitutional. The court nonetheless affirmed under the [[The Good-Faith Exception|good-faith exception]], since the agents had reasonably relied on then-unsettled law.

## Conclusion
Convictions **affirmed**: the warrantless forensic device searches violated the Fourth Amendment, but suppression was barred by the [[The Good-Faith Exception|good-faith exception]]. Motz, J., wrote for the majority (Motz, Wynn, JJ.); Richardson, J., concurred in the judgment, disagreeing with the nexus holding.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Aigbekaen* sharpens the digital border-search doctrine within the Fourth Circuit: even a highly intrusive forensic device search must be tethered to the border-search exception's own purposes, so probable cause to suspect a domestic crime — without any transnational or contraband nexus — does not bring the search within the exception.

## Appears on
- [[Border Searches]] — *Key*

## Sources
- [*United States v. Aigbekaen*, 943 F.3d 713 (4th Cir. 2019)](https://www.courtlistener.com/opinion/4680725/united-states-v-raymond-aigbekaen/) — pinpoint: slip op. at 14 (nexus requirement / Fourth Amendment holding); the CL opinion text carries the slip-opinion page numbers rather than 943 F.3d star pagination, so the pin is slip-style per S2 A3. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "59de5adcbc705733", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "943 F.3d 713 (2019)", "court": "4th Cir. 2019", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Aigbekaen", "year": "2019"}}
{"assertion_id": "2bf881d116de34c9", "dimension": "support", "kind": "home_role", "locator": {"home": "Border Searches"}, "payload": {"home": "Border Searches", "role": "Key", "title": "United States v. Aigbekaen"}}
{"assertion_id": "dc2dd81bba9cb40c", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The border-search exception does not authorize a warrantless, nonroutine forensic search of a returning traveler's electronic devices unless the government's individualized suspicion bears some nexus to the exception's historic purposes — protecting national security, collecting duties, blocking unwanted entrants, or intercepting contraband; suspicion of purely domestic crimes is not enough, so the forensic searches of Aigbekaen's devices violated the Fourth Amendment, though the good-faith exception barred suppression.", "title": "United States v. Aigbekaen"}}
{"assertion_id": "08e0a8b2ff323fe9", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 4th Cir.", "title": "United States v. Aigbekaen"}}
{"assertion_id": "4bf7b1dbf7e762b7", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Aigbekaen", "varies_by_point": "false"}}
```

### lake record — United States v. Aigbekaen

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Aigbekaen",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Raymond Aigbekaen",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Aigbekaen",
    "court": "4th Cir. 2019",
    "court_id": "ca4",
    "court_level": "coa",
    "circuit": "ca4",
    "state": null,
    "date_decided": "2019-11-21",
    "year": 2019,
    "docket": "17-4109",
    "cluster_id": 4680725,
    "lead_opinion_id": 4457978,
    "sibling_ids": [],
    "absolute_url": "/opinion/4680725/united-states-v-raymond-aigbekaen/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "943 F.3d 713",
      "volume": "943",
      "reporter": "F.3d",
      "page": "713",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "943 F.3d 713",
        "volume": "943",
        "reporter": "F.3d",
        "page": "713",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "943 F.3d 713",
    "official_selection": {
      "court_class": "state",
      "selected": "943 F.3d 713",
      "reason": "selected_rank_3"
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
    "date_created": "2026-07-06T05:49:23Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:49:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:49:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:49:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:49:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-aigbekaen--4680725",
      "to_record_id": "United States v. Aigbekaen",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Aigbekaen

```
                                     PUBLISHED

                      UNITED STATES COURT OF APPEALS
                          FOR THE FOURTH CIRCUIT


                                      No. 17-4109


UNITED STATES OF AMERICA,

                    Plaintiff – Appellee,

             v.

RAYMOND IDEMUDIA AIGBEKAEN,

                    Defendant – Appellant.



Appeal from the United States District Court for the District of Maryland, at Baltimore.
James K. Bredar, Chief District Judge. (1:15-cr-00462-JKB-2)


Argued: May 8, 2019                                       Decided: November 21, 2019


Before MOTZ, WYNN, and RICHARDSON, Circuit Judges.


Affirmed by published opinion. Judge Motz wrote the majority opinion, in which Judge
Wynn joined. Judge Richardson wrote an opinion concurring in the judgment.


ARGUED: Michael Lawlor, BRENNAN, MCKENNA & LAWLOR, CHTD., Greenbelt,
Maryland, for Appellant. Matthew James Maddox, OFFICE OF THE UNITED STATES
ATTORNEY, Baltimore, Maryland, for Appellee. ON BRIEF: Robert K. Hur, United
States Attorney, Ayn B. Ducao, Assistant United States Attorney, OFFICE OF THE
UNITED STATES ATTORNEY, Baltimore, Maryland, for Appellee.
DIANA GRIBBON MOTZ, Circuit Judge:

       In April of 2015, a minor alerted law enforcement officers that Raymond Idemudia

Aigbekaen and another man had trafficked her for sex in three mid-Atlantic states. As part

of the investigation that followed, when Aigbekaen returned to the United States from

traveling abroad, the Government seized his MacBook Pro laptop, iPhone, and iPod at the

airport and conducted warrantless forensic searches of the data on all three devices. The

Government subsequently charged Aigbekaen with sex trafficking and related crimes, and

at the conclusion of a nine-day trial, the jury convicted him of these crimes.

       Aigbekaen appeals, arguing primarily that the warrantless forensic searches of his

digital devices violated the Fourth Amendment.         The Government counters that the

searches fell within the “border search” exception to the warrant requirement and that, in

any event, suppression is not appropriate. We agree with Aigbekaen that the border search

exception does not extend to the challenged searches, rendering them unconstitutional. But

we agree with the Government that the good-faith exception to the exclusionary rule bars

suppression. Accordingly, we affirm.



                                             I.

       On April 12, 2015, a sixteen-year-old girl (to whom we, like the parties, refer

pseudonymously as “L.”) called 911 from a Homewood Suites hotel in Bel Air, Maryland.

L. reported that she had run away from home and was looking for help. When an officer

arrived on the scene and spoke with L., she claimed not to remember with whom she had

traveled or where she had been. But after some equivocation, L. disclosed that two men,

                                             2
one named Marcell Greene and another of Nigerian ethnicity named “Raymond,” had

transported her around Maryland, Virginia, and Long Island, New York; had posted ads of

her on Backpage.com; and had trafficked her for sex. L. provided phone numbers for these

men and identified Greene and Raymond Aigbekaen in hotel surveillance footage. She

also recognized images of herself from online prostitution ads on Backpage.com.

Homewood Suites records showed that Aigbekaen had rented L.’s hotel room. Officers

searched the room and found used condoms. 1

       Local law enforcement officers then sent their complete case file to Homeland

Security Investigations (HSI), an investigative arm of the U.S. Department of Homeland

Security.   After receiving the case file, HSI subpoenaed Verizon Wireless and

Backpage.com; the companies’ responses confirmed that the phone number L. had

provided indeed belonged to Aigbekaen, and that this number was listed as a contact on

the Backpage.com prostitution ads. The Backpage.com ads were also linked to two Yahoo!

email addresses, each of which contained portions of Aigbekaen’s name. HSI further

uncovered rental car and hotel records that showed Aigbekaen had traveled to hotels in

Maryland, Virginia, and Long Island.




       1
          By the time of Aigbekaen’s trial, L. was able to testify more fully that she and two
other girls had fled a group home in Dix Hills, New York in January 2015 to live with a
man named Y.P., who trafficked them for sex. L. was able to escape Y.P. with Greene’s
sister, Jasmine. But Jasmine relocated L. to Greene’s home, where Greene and Jasmine
decided to continue trafficking her. Greene then contacted Aigbekaen, who joined the
scheme. Greene and Aigbekaen proceeded to transport L. around Maryland, Virginia, and
Long Island, where she had sex for pay with as many as five men each day. Greene and
Aigbekaen kept all of the proceeds.
                                              3
        HSI agents learned that Aigbekaen had left the country and was set to return through

John F. Kennedy International Airport. The agents asked U.S. Customs and Border

Protection officers to seize any electronic media devices in Aigbekaen’s possession at the

airport upon his return. On May 19, 2015, the officers honored this request and, without

warrants, seized Aigbekaen’s MacBook Pro laptop computer, iPhone, and iPod. The

officers transported the devices to Baltimore, where an HSI agent created and reviewed a

forensic image of each device. HSI did not return the devices to Aigbekaen until June 2,

2015.       The forensic search 2 of the laptop revealed temporary backups of Facebook

Messenger conversations between Aigbekaen and another user that apparently related to

sex trafficking.

        A few months after the warrantless forensic searches, the Government secured and

executed search warrants for the same MacBook Pro and iPhone, Aigbekaen’s Facebook

and Yahoo! accounts, his vehicle, five additional cell phones, his DNA, and Greene’s

residence. A magistrate judge also granted the Government’s application to procure cell

site location information (“CSLI”) under the Stored Communications Act (“SCA”) without

obtaining a warrant.




        2
          A “forensic search” is “a powerful tool” capable of not only viewing data that a
user has intentionally saved on a digital device, but also “unlocking password-protected
files, restoring deleted material, and retrieving images viewed on websites.” United States
v. Cotterman, 709 F.3d 952, 957 (9th Cir. 2013). Unlike a “manual” search of a digital
device, a forensic search generally entails the connection of external equipment and/or the
use of specialized software. United States v. Kolsuz, 890 F.3d 133, 146 & n.6 (4th Cir.
2018).
                                             4
       In the midst of these warrant and SCA applications, a grand jury indicted Greene

and Aigbekaen on six counts, all of which related to interstate sex trafficking of L. and

transportation of her for the purpose of prostitution. Prior to trial, Aigbekaen moved to

suppress various pieces of evidence, including (as relevant here) any evidence recovered

from the May 2015 warrantless forensic searches.

       Aigbekaen argued that the May 2015 forensic searches were unconstitutional

because they were conducted without warrants and did not fall within the border search

exception to the warrant requirement. Aigbekaen maintained that “there has to be a point

at which the nature of the government investigation is so separated and so divorced from

anything related to the border” that the exception becomes inapplicable. He explained that

the Government’s “general interest in enforcing [domestic] criminal laws” does not

constitute an interest justifying “border searches.” The Government responded that, at the

time of the forensic searches, it had reasonable suspicion both that Aigbekaen had

trafficked L. for sex domestically and that he “might be bringing contraband in the form of

child pornography into the country,” citing for the latter argument only an “allegation from

the manager of the hotel where the victim was recovered.”

       At the close of the suppression hearing, the district court dismissed the

Government’s child pornography argument as “a lot weaker” but held that under “the

traditional border search analysis,” “the circumstances of where the property was and

where the person was when the search occurred” “trump[ed]” any need to justify the

specific search. As a result, the court found that no warrants were required for the May

2015 searches. The court further reasoned that if any individualized suspicion was needed

                                             5
to justify the “intrusive” forensic searches of Aigbekaen’s devices, the Government met

this standard because HSI had “at least” reasonable suspicion, if not probable cause, that

the warrantless searches would reveal evidence of domestic sex trafficking. 3

       The court thus denied the suppression motion, and Aigbekaen proceeded to trial.

After considering testimony from over twenty witnesses, a jury found Aigbekaen guilty on

all six counts. Aigbekaen timely noted this appeal.



                                             II.

       Aigbekaen’s principal argument on appeal is that the May 2015 warrantless forensic

searches of his laptop, iPhone, and iPod violated the Fourth Amendment. Although the

Government contends (and we ultimately agree) that the good-faith exception to the

exclusionary rule requires affirmance in any event, “when a Fourth Amendment case

presents a novel question of law whose resolution is necessary to guide future action by

law enforcement officers and magistrates, there is sufficient reason for [a court] to decide

the violation issue before turning to the good-faith question.” United States v. Bosyk, 933




       3
        Prior to trial, Aigbekaen also moved to suppress the CSLI on the ground that the
Government’s procurement of it constituted a search and so required a warrant. He later
conceded, and the district court held, that then-controlling circuit precedent foreclosed his
claim. See United States v. Graham, 824 F.3d 421, 424–25 (4th Cir. 2016) (en banc),
abrogated by Carpenter v. United States, 138 S. Ct. 2206, 2223 (2018). During the
pendency of this appeal, the Supreme Court vindicated Aigbekaen’s position. See
Carpenter, 138 S. Ct. at 2223. But as Aigbekaen acknowledges, binding circuit precedent
nevertheless precludes suppression of the CSLI because the Government obtained it in
good-faith reliance on a federal statutory scheme — namely, the SCA. United States v.
Chavez, 894 F.3d 593, 608 (4th Cir. 2018).
                                             6
F.3d 319, 332 n.10 (4th Cir. 2019) (alterations in original) (quoting Illinois v. Gates, 462

U.S. 213, 264 (1983) (White, J., concurring)).

       We review the district court’s legal conclusions de novo and its factual findings for

clear error, considering the record evidence in the light most favorable to the Government.

Kolsuz, 890 F.3d at 141–42. Because the Government conducted the challenged searches

without warrants, it bears the burden of proving, by a preponderance of the evidence, that

an exception to the warrant requirement applies. United States v. Davis, 690 F.3d 226, 262

(4th Cir. 2012).

                                             A.

       The Fourth Amendment requires that governmental searches and seizures be

reasonable. In most cases, this requires a warrant based on probable cause. See, e.g., Riley

v. California, 573 U.S. 373, 382 (2014). 4 “In the absence of a warrant, a search is

reasonable only if it falls within a specific exception to the warrant requirement.” Riley,

573 U.S. at 382.

       One such exception applies at our nation’s borders, where the Supreme Court has

long recognized the federal Government’s substantial sovereign interests in “protect[ing]

. . . territorial integrity” and national security, United States v. Flores-Montano, 541 U.S.



       4
         Aigbekaen maintains that Riley, which held the search incident to arrest exception
inapplicable to modern cell phones, similarly renders the border search exception
categorically inapplicable to modern cell phones and analogous digital devices. See id. at
403. However, we have held after Riley that law enforcement officers may conduct a
warrantless forensic search of a cell phone under the border search exception where the
officers possess sufficient individualized suspicion of transnational criminal activity. See
Kolsuz, 890 F.3d at 148. Accordingly, we must reject Aigbekaen’s interpretation of Riley.
                                             7
149, 153 (2004); blocking “the entry of unwanted persons and effects,” id. at 152;

“regulat[ing] the collection of duties,” United States v. Montoya de Hernandez, 473 U.S.

531, 537 (1985); and “prevent[ing] the introduction of contraband,” id. These Government

concerns are “at [their] zenith” at the border, whereas an individual’s “expectation of

privacy is less at the border than it is in the interior.” Flores-Montano, 541 U.S. at 152,

154. Thus, “[a]t a border” or its “functional equivalent, like [an] international airport . . .

government agents may conduct routine searches and seizures of persons and property

without a warrant or any individualized suspicion.” Kolsuz, 890 F.3d at 137 (internal

quotation marks omitted).

       Although this “border search” exception to the warrant requirement is broad, it is

not boundless. Even when the exception applies, the Supreme Court has explained that

certain “highly intrusive searches” may qualify as “‘nonroutine’” and so require some level

of individualized suspicion. Flores-Montano, 541 U.S. at 152 (quoting Montoya de

Hernandez, 473 U.S. at 541 n.4). Just last year, we applied this principle in the context of

an intrusive forensic search of a cell phone at the border. Given the “unparalleled breadth

of private information” that such a search could reveal, we held that “a forensic search of

a digital phone must be treated as a nonroutine border search, requiring some form of

individualized suspicion” even if not a warrant. Kolsuz, 890 F.3d at 145–46. 5 If the border

exception applies to the May 2015 forensic searches of Aigbekaen’s devices, these searches




       5
        We declined to decide whether reasonable suspicion was sufficient to justify such
a search or whether, instead, probable cause was required. Id. at 148.
                                              8
(like the forensic searches in Kolsuz) were sufficiently intrusive to be “nonroutine” and so

required some level of individualized suspicion. Id. at 137.

       But this raises another question: Does the border exception even apply to the May

2015 forensic searches?      Phrased differently, of what must the Government have

individualized suspicion for the border search exception to apply? Again, precedent offers

a clear answer. As the Supreme Court and this court have repeatedly explained, “the scope

of a warrant exception should be defined by its justifications.” Id. at 143 (citing Riley, 573

U.S. at 385–91); accord, e.g., Arizona v. Gant, 556 U.S. 332, 351 (2009) (“When the[]

justifications” underlying an exception to the warrant requirement “are absent, a

[warrantless] search . . . will be unreasonable . . . .”). That is to say, a warrant exception

will not excuse a warrantless search where applying the exception “would untether the rule

from the justifications underlying [it].” Riley, 573 U.S. at 386 (internal quotation marks

omitted).

       The same limitation applies to the border search exception. Indeed, neither the

Supreme Court nor this court has ever authorized a warrantless border search unrelated to

the sovereign interests underpinning the exception, let alone nonroutine, intrusive searches

like those at issue here. Rather, our decision in Kolsuz teaches that the Government may

not “invoke[] the border exception on behalf of its generalized interest in law enforcement

and combatting crime.” 890 F.3d at 143. This restriction makes particularly good sense

as applied to intrusive, nonroutine forensic searches of modern digital devices, which store

vast quantities of uniquely sensitive and intimate personal information, id. at 145 (citing

Riley, 573 U.S. at 393–97), yet cannot contain many forms of contraband, like drugs or

                                              9
firearms, the detection of which constitutes “the strongest historic rationale for the border-

search exception,” United States v. Molina-Isidoro, 884 F.3d 287, 295 (5th Cir. 2018)

(Costa, J., concurring).

       Accordingly, as we explained in Kolsuz, 890 F.3d at 143, to conduct such an

intrusive and nonroutine search under the border search exception (that is, without a

warrant), the Government must have individualized suspicion of an offense that bears some

nexus to the border search exception’s purposes of protecting national security, collecting

duties, blocking the entry of unwanted persons, or disrupting efforts to export or import

contraband. See also United States v. Ramsey, 431 U.S. 606, 620 (1977) (“The border-

search exception is grounded in the recognized right of the sovereign to control, subject to

substantive limitations imposed by the Constitution, who and what may enter the

country.”). If a nonroutine search becomes too “attenuated” from these historic rationales,

it “no longer [will] fall under” the exception.       Kolsuz, 890 F.3d at 143.       In such

circumstances, the search will be unconstitutional unless accompanied by a warrant or

justified under a different exception to the warrant requirement.

       Applying these principles to the facts at hand, we can only conclude that the

warrantless forensic searches of Aigbekaen’s devices in May of 2015 lacked the requisite

nexus to the recognized historic rationales justifying the border search exception. Of

course, when Aigbekaen landed at the airport with his MacBook Pro, iPhone, and iPod in

tow, HSI agents had not only reasonable suspicion but probable cause to suspect that he

had previously committed grave domestic crimes. But these suspicions were entirely

unmoored from the Government’s sovereign interests in protecting national security,

                                             10
collecting or regulating duties, blocking Aigbekaen’s own entry, or excluding contraband.

Thus, holding the border search exception applicable here, based simply on the

Government’s knowledge of domestic crimes, would “untether” that exception from its

well-established justifications. Riley, 573 U.S. at 386.

       Resisting this result, the Government asserts that Aigbekaen’s crime “clearly was

one that is the proper subject of a border search, because [sex trafficking] is a crime

‘commonly involving cross-border movements.’” Supp. Response Br. at 13 (quoting

United States v. Caballero, 178 F. Supp. 3d 1008, 1017 n.7 (S.D. Cal. 2016)). Of course,

the general character of a crime may be relevant to an officer’s reasonable suspicion that it

involves a transnational component. But inherent in the notion of individualized suspicion

is some evidentiary basis for what a specific crime does involve in the individual case at

hand, not just what it “commonly involves” as a general matter. Here, the Government has

offered no reasonable basis to suspect that Aigbekaen’s domestic crimes had any such

transnational component.

       We also must reject the district court’s conclusion that a nonroutine, intrusive

search’s physical and temporal proximity to an international border “trumps everything”

under the Fourth Amendment. To be sure, the Supreme Court has stated that routine border

searches “are reasonable simply by virtue of the fact that they occur at the border.” Ramsey,

431 U.S. at 616. But in the context of “highly intrusive” nonroutine border searches,

Flores-Montano, 541 U.S. at 152, the Court has explicitly struck a “balance between the

interests of the Government and the privacy right of the individual,” Montoya de

Hernandez, 473 U.S. at 540; see also Riley, 573 U.S. at 385 (instructing courts to evaluate

                                             11
any exception to the warrant requirement by weighing individual privacy interests against

“legitimate governmental interests” (quoting Wyoming v. Houghton, 526 U.S. 295, 300

(1999))). Consistent with this balancing, we clarified in Kolsuz that a nonroutine search’s

location is not dispositive of whether the border search exception applies; rather, it is the

search’s relation to the Government’s sovereign interests that is paramount. 890 F.3d at

142–43.

       Moreover, “the ultimate touchstone of the Fourth Amendment is reasonableness.”

Riley, 573 U.S. at 381 (internal quotation marks omitted). And on the facts of this case,

the reasonableness of requiring law enforcement to secure a warrant before conducting an

intrusive forensic search of a traveler’s digital device, solely to seek evidence of crimes

with no transnational component, is readily apparent. By the time Aigbekaen arrived at

the airport with his devices, and prior to any searches of those devices, HSI agents had

probable cause to believe that Aigbekaen’s laptop, at least, contained evidence of domestic

sex trafficking. Indeed, in August of 2015, HSI secured warrants to search both the

MacBook Pro and the iPhone, relying almost exclusively on evidence that was in agents’

possession before Aigbekaen arrived at the airport in May. Given the information in its

possession at the time, it is only reasonable to expect the Government to have procured

these warrants prior to the May searches. 6


       6
        Of course, if HSI agents were unable to timely secure such warrants and reasonably
feared that Aigbekaen would destroy the evidence in the meantime, the exigent
circumstances exception might apply. See Riley, 573 U.S. at 402 (noting that Fourth
Amendment “exigencies could include the need to prevent the imminent destruction of
evidence in individual cases”). But the Government does not even suggest that exigency
played any role here.
                                              12
       In contrast, it would be patently unreasonable to permit highly intrusive forensic

Government searches of travelers’ digital devices, without warrants, on bases unrelated to

the United States’s sovereign authority over its borders. To be clear, we do not question

the import of the Government’s general interest in combatting crime. But we cannot agree

that this interest categorically eclipses individuals’ privacy interests in the vast troves of

data contained on their digital devices when the suspected offenses have little or nothing

to do with the border.

       As the Supreme Court explained in Riley, “[m]odern cell phones, as a category,

implicate privacy concerns far beyond those implicated” by physical searches. Id. at 393.

This is so because cell phones and other modern digital devices feature “an element of

pervasiveness” that distinguishes them from physical records; these days, “it is the person

who is not carrying a cell phone, with all that it contains, who is the exception.” Id. at 395.

At the same time, these devices have “immense storage capacity,” as well as cloud storage

capabilities, which they use to collect “in one place many distinct types of information . . .

that reveal much more in combination than any isolated record.” Id. at 393–94, 397. These

include unusually sensitive data regarding one’s relationships, personal interests and

preferences, prior internet searches, location history, and much more. Id. at 395–96. To

adopt the Government’s position, we would need to hold that it could conduct a warrantless

forensic search of any traveler’s cell phone — uncovering all of this data, including

“password-protected” and “deleted material[s],” Cotterman, 709 F.3d at 957 — on

suspicion that the phone may contain evidence of any prior domestic crime.



                                              13
       Because Aigbekaen does not challenge any routine border searches, we need not

decide whether or how the interests that underpin the border search exception constrain, in

practice, the Government’s broad and historic authority to conduct suspicionless searches

of individuals and their effects at the border. Ramsey, 431 U.S. at 616. Similarly, we need

not determine what quantum of individualized suspicion, if any, beyond the familiar

reasonable-suspicion standard is needed to justify a warrantless forensic search of a device

at the border.

       We simply apply the teaching of Kolsuz: where a search at the border is so intrusive

as to require some level of individualized suspicion, the object of that suspicion must bear

some nexus to the purposes of the border search exception in order for the exception to

apply. Because no such nexus existed here, the warrantless, nonroutine forensic searches

violated the Fourth Amendment.

                                            B.

       The Government briefly presses two secondary arguments in an attempt to establish

that the May 2015 searches were constitutional. Neither is persuasive.

       First, the Government devotes four sentences of briefing to a claim that at the time

of the warrantless searches, it “had a concern” that Aigbekaen’s devices “might” contain

not only evidence of past crimes, but also child pornography. Because of this “concern,”

the Government maintains, the warrantless forensic searches featured both individualized

suspicion and the requisite nexus to a dominant interest underpinning the border search

exception: preventing contraband from entering the country.



                                            14
       Like the district court, we do not find this claim persuasive. Even assuming that a

warrantless forensic search of a digital device at the border could be justified by reasonable

suspicion, 7 we can discern no “particularized and objective basis” in the record for agents

to reasonably suspect that Aigbekaen possessed child pornography on his devices.

Montoya de Hernandez, 473 U.S. at 541 (internal quotation marks omitted).                The

Government’s stated “concern” is based on a local police officer’s brief testimony, during

the suppression hearing, that a hotel manager received a tip from an unnamed employee

that the employee had “overheard one of the gentlem[e]n staying in the room [saying], you

know, let’s hurry up and get this video done.” Suppr. Hr’g Tr., ECF No. 193, at 217–19.

During cross-examination, the officer was asked if the hotel manager “ever g[a]ve [him]

any other indication as to why that [unnamed] employee thought that there was some type

of movie making or video making going on,” to which he replied, “No.” Id. at 217. At

trial, although the hotel manager recounted in detail the events surrounding L.’s 911 call,

he could no longer recall hearing any such statement from an employee or relating it to law

enforcement. 9/23/16 Trial Tr., ECF No. 259, at 69–70, 76. This isolated, vague, and

third-hand allegation does not rise to the level of reasonable suspicion. 8




       7
         See Kolsuz, 890 F.3d at 148 (declining to determine “whether more than reasonable
suspicion is required for a search of this nature”).
       8
         Notably, although the Government asserted at oral argument before us that it had
probable cause (not just reasonable suspicion) to suspect Aigbekaen’s devices contained
child pornography, not one of HSI’s numerous warrant affidavits and CSLI applications
included any such allegations. Nor did the HSI agent who testified at the suppression
hearing mention any suspicion that Aigbekaen’s devices contained child pornography.
                                             15
       Second, the Government suggests that the requisite nexus to the purposes of the

border search exception was present because Aigbekaen was a “criminal[]” seeking to enter

the United States and carried the “instrumentalities” of his domestic crime (that is, his

digital devices) into the country with him. Again, we must disagree. If the border search

exception is to retain any distinction from the Government’s “generalized interest in law

enforcement and combatting crime,” Kolsuz, 890 F.3d at 143, it cannot be invoked to

sanction invasive and nonroutine warrantless searches of all suspected domestic

“criminals,” nor the suspected “instrumentalities” of their domestic crimes. Importantly,

the Government does not contend (save for its unavailing child pornography claim) that

these “instrumentalities” were contraband.

       Because the Government lacked sufficient individualized suspicion of criminal

activity with any nexus to the sovereign interests underlying the border search exception,

its warrantless forensic searches of Aigbekaen’s devices violated the Fourth Amendment.



                                             III.

       In the alternative, the Government argues that any constitutional infirmity in the

May 2015 searches does not justify reversal for several independent reasons. We turn now

to these contentions.

                                             A.

       In its brief, the Government maintains that any dispute over these searches is moot

because no tainted evidence was admitted at trial. However, the record belies this assertion.

At the very least, HSI’s affidavit in support of the warrant to search Aigbekaen’s Facebook

                                             16
account relied on conversations and screen shots uncovered during the May 2015

searches. 9 And the Government introduced the Facebook warrant returns at trial.

       At oral argument before us, the Government did not dispute these facts. Instead, it

sought to refashion its mootness claim, asserting in its place that the August 2015 warrant-

backed searches of Aigbekaen’s devices constituted an “independent source” that cured

any taint from the prior warrantless searches. The record evidence, however, does not

support application of the independent-source doctrine. Under that doctrine, evidence

“initially discovered during, or as a consequence of, an unlawful search, but later obtained

independently from activities untainted by the initial illegality” may be admitted at trial.

Murray v. United States, 487 U.S. 533, 537 (1988). But later activities, like the August

2015 searches, do not qualify as independent sources if “the agents’ decision to seek the

warrant[s] was prompted by what they had seen during the initial [searches].” Id. at 542.

As the Government conceded at oral argument, the district court did not make any factual

findings on this point. Mindful of the Supreme Court’s admonition that “it is the function

of the District Court rather than the Court of Appeals to determine the facts,” id. at 543, we

cannot assume in the first instance that the August 2015 warrants were not prompted by

the May 2015 warrantless searches.

                                             B.

       The Government next contends that the good-faith exception to the exclusionary

rule bars suppression of any evidence tainted by any constitutional defect in the May 2015


       9
        The district court later opined that the probable cause underlying this warrant, even
with these allegations, was “a little thin.”
                                             17
searches. Aigbekaen counters that the lack of a nexus renders the good-faith exception

inapplicable. On this point, we must agree with the Government.

       The evidentiary fruits of Fourth Amendment violations are generally inadmissible

at trial. See Wong Sun v. United States, 371 U.S. 471, 484–85 (1963). But the fruits of “a

search conducted in reasonable reliance on binding precedent [are] not subject to the

exclusionary rule,” as that rule is designed “to deter future Fourth Amendment violations.”

Davis v. United States, 564 U.S. 229, 236–37, 241 (2011) (emphasis added).

       In this case, the HSI agents who searched Aigbekaen’s devices in May of 2015

reasonably relied on an “established and uniform body of precedent allowing warrantless

border searches of digital devices.” Kolsuz, 890 F.3d at 148. Although it has long been

understood that the scope of a warrant exception should be tailored to the purposes

underlying that exception, no court had yet applied that principle to require a warrant “for

any border search, no matter how nonroutine or invasive.” Id. at 147; see also Molina-

Isidoro, 884 F.3d at 294 (Costa, J., concurring) (noting that “no reported federal decision

has required a warrant for any border search”). Only in 2018 did this court recognize that

“a search initiated at the border could become so attenuated from the rationale for the

border search exception that it no longer would fall under that exception” and so require a

warrant. Kolsuz, 890 F.3d at 143. And only today have we applied that principle to hold

unconstitutional such an attenuated, warrantless, nonroutine forensic search at the border.

       Tellingly, Aigbekaen offers almost no argument against application of the good-

faith exception, save for a question-begging allegation that the Government “attempt[ed]

to exploit an exception to the Fourth Amendment warrant requirement.” He may well be

                                            18
correct that even prior to Kolsuz, “the better practice” would have been for the Government

to get a warrant in the first place. But good faith does not mandate best practices. Given

the uniform body of precedent that permitted warrantless searches at the border in May of

2015, we cannot help but conclude that the good-faith exception applies here. 10



                                              IV.

       For the foregoing reasons, the judgment of the district court is

                                                                                  AFFIRMED.




       10
          Aigbekaen also argues, in supplemental briefing, that the multi-week seizures of
his digital devices constituted an unreasonable interference with his possessory interests.
See United States v. Pratt, 915 F.3d 266, 271–73 (4th Cir. 2019). However, Aigbekaen
opted neither to press this claim before the district court nor to raise it in his opening brief
to this court. In fact, when the district court asked Aigbekaen’s counsel whether he
intended to develop a factual record regarding the reasonableness of the seizures, his
counsel chose not to “request[] any further information” on the issue. We decline to
address this forfeited claim. In his pro se brief and supplemental briefs, Aigbekaen also
raises a host of additional challenges to his conviction and sentence. Although “an
appellant who is represented by counsel has no right to file pro se briefs or raise additional
substantive issues in an appeal,” United States v. Cohen, 888 F.3d 667, 682 (4th Cir. 2018),
we have examined Aigbekaen’s contentions and find no reversible error.
                                              19
RICHARDSON, Circuit Judge, concurring in the judgment:

       For the first time in this Circuit, the Majority holds a border search unlawful by

applying a “nexus” requirement tethered to narrowly defined purposes that supposedly

underlie the border-search doctrine: national security, blocking the entry of persons, and

disrupting the trafficking of contraband. And, although my good colleagues agree that law

enforcement reasonably suspected a foreign national of interstate sex trafficking, this

reasonable suspicion is not enough for them. Because interstate sex trafficking—as

“distinguished” from international sex trafficking—lacks the Majority’s requisite nexus to

the perceived purposes of the border-search doctrine, the Majority holds the search of a sex

trafficker’s cell phone at the border violates the Fourth Amendment.

       In my view, the Majority errs in adopting a “nexus” test that is in deep tension with

Supreme Court precedent. And even assuming the “nexus” test were proper, I would find

it satisfied here.

       In the end, the Majority affirms Aigbekaen’s conviction based on the good-faith

exception to the exclusionary rule. And I agree with that judgment. But I respectfully

disagree with the decision to declare this border search unlawful.

                                             I.

       The Fourth Amendment prohibits “unreasonable searches and seizures.” U.S.

CONST. amend. IV. And as the Supreme Court has explained, “reasonableness” is the

“ultimate touchstone of the Fourth Amendment.” Riley v. California, 573 U.S. 373, 381

(2014) (quoting Brigham City v. Stuart, 547 U.S. 398, 403 (2006)). In determining what

is reasonable, courts look to longstanding traditions with an eye towards determining “that


                                            20
degree of privacy against government that existed when the Fourth Amendment was

adopted.” United States v. Jones, 565 U.S. 400, 406 (2012) (quoting Kyllo v. United States,

533 U.S. 27, 34 (2001)); see also Riley, 573 U.S. at 382 (looking to the historical bases for

a search incident to arrest).

       One such tradition, the “border-search doctrine,” gives government agents at

international borders broad discretion to search people and their effects. United States v.

Ramsey, 431 U.S. 606, 616–17 (1977). The border-search doctrine has “a history as old as

the Fourth Amendment itself,” id. at 619, and rests on the principle “that the United States,

as sovereign, has the inherent authority to protect, and a paramount interest in protecting,

its territorial integrity,” United States v. Flores-Montano, 541 U.S. 149, 153 (2004); cf.

United States v. Curtiss-Wright Exp. Corp., 299 U.S. 304, 318 (1936) (describing territorial

integrity as inherent to sovereignty). Thus, the government’s “interest in preventing the

entry of unwanted persons and effects is at its zenith at the international border.” Flores-

Montano, 541 U.S. at 152. And travelers understand that they subject themselves and their

property to some form of search by crossing international boundaries. As a result, “the

expectation of privacy is less at the border than it is in the interior.” Id. at 154.

       Supreme Court jurisprudence purports to reflect the border-search doctrine’s

historical scope. See Ramsey, 431 U.S. at 616–19; see also Boyd v. United States, 116 U.S.

616, 623–24 (1886). But in the three decades since Ramsey, more historical work has been

done to understand the Fourth Amendment. See, e.g., WILLIAM J. CUDDIHY, The Fourth

Amendment: Origins and Original Meaning 602–1791 (2009). And in recent years, some

work has begun to better understand the border-search doctrine itself—analyzing the


                                               21
backdrop English common-law doctrine, the historical understanding of sovereign

prerogatives under international law, the drafting and ratification history of the Fourth

Amendment (and relevant state analogues), and statutes enacted around the time the Bill

of Rights was ratified (such as the Collection Acts of 1789 and 1790). See, e.g., Note, The

Border Search Muddle, 132 HARV. L. REV. 2278, 2287–97 (2019).

       Based on this more recent historical work, one might ask whether Ramsey’s

historical analysis would change (or perhaps be confirmed) if we were to revisit the

relevant historical sources (including those left aside by Ramsey). But this case is neither

the time nor the place to do so. We are an inferior court (to say nothing of the lack of

briefing focused on this historical inquiry and a somewhat limited academic literature

focused on the border-search doctrine). As an inferior court, we take the Supreme Court’s

precedents as we find them.

       And the Supreme Court has repeatedly upheld border agents’ broad discretion to

conduct searches in sweeping terms, requiring particularized suspicion only for especially

intrusive searches.   The distinction between “routine” searches and highly intrusive

“nonroutine” searches provides the analytical linchpin for determining whether

particularized suspicion is required at the border. An agent may undertake routinely

intrusive border searches of international travelers—such as patting them down for

weapons and rummaging through their luggage—with no articulable suspicion. Flores-

Montano, 541 U.S. at 152.

       Highly intrusive searches at the border that are deemed nonroutine are different. For

this limited category, the government must articulate reasonable suspicion. United States


                                            22
v. Montoya de Hernandez, 473 U.S. 531, 542 (1985). 1 In Montoya de Hernandez, border

agents suspected a woman, who had arrived on an international flight, of swallowing

balloons containing illegal drugs. Id. at 534−35. Agents strip searched the woman and

detained her for over sixteen hours so that they could inspect the results of a bowel

movement. Id. at 535. Eventually, a federal magistrate authorized a rectal examination,

which uncovered a balloon filled with cocaine (the first of eighty-eight ultimately

revealed). Id. Even on these facts, the Supreme Court held that only reasonable suspicion

was needed to detain the woman. Id. at 541.

       The Supreme Court has suggested that only three highly intrusive situations may

qualify as nonroutine: (1) “highly intrusive searches of the person,” (2) searches of

property that are “destructive,” and (3) searches carried out in a “particularly offensive”

manner.    Flores-Montano, 541 U.S. at 152–56, 154 n.2; see also United States v.

Cotterman, 709 F.3d 952, 973 (9th Cir. 2013) (en banc) (Callahan, J., concurring in part,

dissenting in part, and concurring in the judgment).

       In making this distinction based on the intrusiveness of a search, the Court considers

whether the subject of a search is a person or property. Despite hinting at the possibility

that a “destructive” search of property might amount to a nonroutine search, see Flores-

Montano, 541 U.S. at 152–56, 154 n.2, the Supreme Court has never actually held that any

search of property—as opposed to persons—was “nonroutine.” See, e.g., United States v.


       1
        The potential that particularized suspicion might be required for more intrusive
searches had been left open by older precedents. See Ramsey, 431 U.S. at 618 n.13 (not
“decid[ing] whether, and under what circumstances, a border search might be deemed
‘unreasonable’ because of the particularly offensive manner in which it is carried out”).

                                             23
Touset, 890 F.3d 1227, 1234 (11th Cir. 2018) (“Property and persons are different.”). And

the Court has set a high bar for when a property search might ever rise to that level. In

Flores-Montano, the Court held that customs officers conducted only a “routine” search

when they stopped and dissembled a vehicle to remove and inspect its gas tank. 541 U.S.

at 155–56. In so holding, the Court instructed that, where border searches of property were

involved, only “destructive” or otherwise “particularly offensive” searches of that property

would be so intrusive as to require any particularized suspicion. See id. at 154 n.2. The

Supreme Court also chastised lower courts for being too quick to undermine the simplicity

of the border-search doctrine for property with “[c]omplex balancing tests to determine

what is a ‘routine’ search,” explaining that such tests “have no place in border searches of

vehicles.” Id. at 152.

       Despite that guidance on searches of property at the border, in United States v.

Kolsuz, 890 F.3d 133 (4th Cir. 2018), we held that a detailed “forensic” search—as opposed

to a “manual” search—of an international traveler’s electronic devices at the border was

“nonroutine” and thus required particularized suspicion. See id. at 144 (relying, in part, on

Riley v. California, 573 U.S. 373 (2014)). That holding may be controversial. See, e.g.,

Touset, 890 F.3d at 1233–36. But whatever one thinks of creating a constitutional

distinction between “forensic” and “manual” searches of property, it is the law of our

circuit. And so I assume that some degree of suspicion was required for the forensic search

of Aigbekaen’s electronic devices.

       Kolsuz also addressed, and rejected, an argument that the search in that case had an

inadequate “nexus” to the purposes of the border-search doctrine. We first observed that,


                                             24
“[a]s a general rule, the scope of a warrant exception should be defined by its

justifications.” Kolsuz, 890 F.3d at 143 (citing Riley, 573 U.S. at 384–92). We then noted,

in general terms, the possibility that a search “could become so attenuated from the

rationale for the border search exception that it would no longer fall under that exception.”

Kolsuz, 890 F.3d at 143 (emphasis added). We held that the search before us in that case

did not fail “on any account of a ‘nexus’ requirement” because the crime being investigated

had a “transnational” nature. Id. That is, Kolsuz held that suspicion of transnational crime

was sufficient to satisfy any potential “nexus” requirement.

       Kolsuz did not hold that such suspicion was necessary for a border search. Nor did

Kolsuz explain the rationale for the border-search doctrine or otherwise explore the bounds

of what constitutes an adequate transnational “nexus.” And so the Majority overstates the

case when it claims that Kolsuz held that “where a search at the border is so intrusive as to

require some level of individualized suspicion, the object of that suspicion must bear some

nexus to the purposes of the border search exception in order for the exception to apply.”

Majority Op. at 14. Kolsuz merely noted the possible existence of a “nexus” requirement

and, assuming it existed, concluded that it was satisfied.

                                             II.

       In this case, the Majority goes beyond Kolsuz by imposing this transnational

“nexus” requirement to hold a border search unlawful for the first time in our circuit.

                                             A.

       Before evaluating the Majority’s “nexus” requirement, I briefly note what I

understand it to be, and not to be. The Majority opinion does not cast doubt on non-


                                             25
invasive searches (like going through someone’s luggage) that happen every day at the

border. If such “routine” searches could be challenged as having an inadequate “nexus” to

the border, the border-search doctrine would be eviscerated. Thankfully, the Majority does

not go there (although it does not rule out the possibility of going there in the future, and it

may be challenging to maintain a principled reason for not doing so). 2

       Instead, the Majority’s “nexus” requirement comes into play (for now) only for the

more intrusive “nonroutine” searches that already require objective, particularized

suspicion. It seeks to regulate what kind of particularized suspicion is required. In the

Majority’s view, the grounds for suspicion must dovetail with the ultimate purposes of the




       2
         The Ninth Circuit has gone there. United States v. Cano, 934 F.3d 1002, 1016 (9th
Cir. 2019) (holding that “border searches are limited in scope to searches for contraband
and do not encompass searches for evidence of past or future border-related crimes”). In
that case, the court held that agents could conduct a “manual” search of a phone without
any suspicion but that the search exceeded the permissible scope of a border search when
agents recorded phone numbers and messages. Id. at 1019. The Ninth Circuit reasoned
that recording numbers and messages went beyond what was reasonably necessary to
search for contraband. Id. I find the Ninth Circuit’s reasoning on that point hard to accept,
both for the reasons I explain below and under the plain-view doctrine: surely, if officers
have discovered information during a lawful search, recording that information does not
render the search unlawful.

                                              26
border-search doctrine. 3       Having reason to believe that the search will uncover

contraband—for example, that the person’s cell phone contains child pornography—

necessarily corresponds to the Majority’s purposes of the border-search doctrine. The

Majority is also willing to permit searches for evidence of “transnational” criminal activity.

But when agents seek evidence of domestic crimes, my colleagues decide they need

probable cause and a warrant.

                                                      B.

         This “nexus” requirement is inconsistent with the Supreme Court’s border-search

cases.       Those cases consistently describe the government’s powers at the border in

sweeping terms:

                 Time and again, we have stated that “searches made at the
                 border, pursuant to the longstanding right of the sovereign to
                 protect itself by stopping and examining persons and property
                 crossing into this country, are reasonable simply by virtue of
                 the fact that they occur at the border.” . . . It is axiomatic that
                 the United States, as sovereign, has the inherent authority to
                 protect, and a paramount interest in protecting, its territorial
                 integrity.

Flores-Montano, 541 U.S. at 152–53 (quoting Ramsey, 531 U.S. at 616). The Supreme

Court has limited the border-search doctrine only when the intrusiveness of the search

makes it unreasonable without particularized suspicion—not based on the government’s


         3
         The precise type of “reasonable suspicion” required to establish a nexus has
divided courts. Compare United States v. Cano, 934 F.3d at 1020 (narrower: reasonable
suspicion that searched item contains contraband), with Majority Op. at 9–11 (broader:
reasonable suspicion of prohibited transnational activity). Of course, in the context of
border searches involving child pornography stored in cell phones, the suspicion of
contraband (child pornography) and of ongoing prohibited transnational activity
(smuggling of child pornography) will overlap.

                                                 27
interests or a “nexus” between these interests and the specific search conducted. See id.

The Court has authorized no further exceptions to the near-absolute description of the

doctrine in Flores-Montano and Ramsey. In fact, it has cautioned lower courts against

creating them. Id.

       The Majority’s innovation is to limit the border-search doctrine based not on the

intrusiveness of the search, but on the nature of the government’s interests at stake. Not

only is there no support for this innovation in the Supreme Court’s border-search cases, but

this also ignores the Court’s admonitions to interpret the doctrine broadly and avoid

creating new limitations.

       Now there is an argument that the border-search doctrine should be limited in this

way—or perhaps even more narrowly. Some jurists have taken the view that the border-

search doctrine is concerned solely with detection of contraband. See, e.g., Cano, 934 F.3d

at 1016−19; United States v. Vergara, 884 F.3d 1309, 1317 (11th Cir. 2018) (Pryor, J.,

dissenting). And this narrow reading has some historical support. After all, the Supreme

Court has mainly grounded the border-search doctrine in founding-era statutes that

authorized warrantless customs inspections. Ramsey, 431 U.S. at 616–17 (citing Act of

July 31, 1789, ch. 5, § 24, 1 Stat. 29, 43); see also Act of Aug. 4, 1790, ch. 35, § 31, 1 Stat.

145, 164–65 (permitting revenue collectors to board and search vessels in coastal waters

without suspicion); id. at §§ 47–48, 1 Stat. at 169–70 (permitting revenue collectors to open

containers on vessels “on suspicion of fraud” without a warrant).

       On the other hand, there are reasons to conclude that this “contraband-only” view

might be too narrow given the interests of the United States, as sovereign, at its territorial


                                              28
borders. As we observed in Kolsuz, the government has a broader national-security interest

at the border that goes beyond the immediate search for contraband. 890 F.3d at 143. So

we noted that the doctrine should encompass searches for evidence of “ongoing efforts to

export contraband illegally, through searches initiated at the border,” id. at 143−44, not just

“direct interception of contraband,” id. at 143. Thus construed, the purposes of the border-

search doctrine overlap to some degree with general law enforcement.

       And the Supreme Court has described the border-search doctrine as being concerned

with regulating the movement not only of goods, but also of people. Carroll v. United

States, 267 U.S. 132, 154 (1925). It is “‘without doubt’ that the power to exclude aliens

‘can be effectuated by routine inspections and searches of individuals or conveyances

seeking to cross our borders.’” Ramsey, 431 U.S. at 619 (quoting Almeida-Sanchez v.

United States, 413 U.S. 266, 272 (1973)); see also United States v. Oriakhi, 57 F.3d 1290,

1296 (4th Cir. 1995) (“From the sovereign’s power to protect itself is derived its power to

exclude harmful influences, including undesirable aliens, from the sovereign’s territory.”).

And the Supreme Court has articulated the federal government’s control over migration—

and the nation’s borders—as near-plenary. See, e.g., Ramsey, 431 U.S. at 619; see also

U.S. ex rel. Knauff v. Shaughnessy, 338 U.S. 537, 542 (1950).

       But no matter how we, as lower-court judges, might wish to shape the doctrine, we

are not free to rewrite the Supreme Court’s case law based on our own ideas. And that law

is sweeping in its deference to the authority of the government to conduct searches at the

border.




                                              29
       Without support in the Court’s border-search cases, the Majority bases its “nexus”

requirement on the Court’s analysis of the search-incident-to-arrest exception in Riley v.

California, 573 U.S. 373 (2014). Like the Kolsuz panel, my colleagues read Riley to say

that, “[a]s a general rule, the scope of a warrant exception should be defined by its

justifications.” Kolsuz, 890 F.3d at 143. But transplanting Riley’s “general rule” into the

specific context of border searches to support the “nexus” requirement raises at least two

problems.

       First, Riley said nothing about border searches; it concerned the far different context

of searches incident to arrest. We cannot, as lower-court judges, strain to insert the

Supreme Court’s reasoning from one line of cases into another where it does not fit.

Particularly where two areas of case law point in different directions, we must follow the

cases that are most on point. 4 And as I have explained, the Court has never held that the

border-search doctrine should be “defined by its justifications.” Id. at 143. To the contrary,

it has articulated the doctrine in sweeping terms and told us to apply it accordingly.




       4
         There are, moreover, important differences between a search incident to arrest and
a border search. These differences undermine any reliance on Riley’s search-incident-to-
arrest analysis to support the “nexus” requirement in the border-search context. For one,
the two doctrines have different justifications. The border-search doctrine, unlike the
search-incident-to-arrest doctrine, implicates the sovereign’s paramount interest in
protecting its territorial integrity—suggesting a far broader scope than the narrower
rationales justifying the search-incident-to-arrest doctrine. And unlike searches incident to
arrest, border searches are based in part on implied consent. Just as airline passengers
understand that having their bodies scanned and their bags x-rayed is part of the price of
admission to modern airports, so travelers at international crossings have long understood
that they are subjecting themselves to search at the border.

                                             30
       And second, Riley itself does not support the Majority’s approach. Riley made clear

that we should be looking categorically at the type of search—not the suspicion motivating

the search. Riley considered whether the search-incident-to-arrest doctrine, which permits

warrantless and suspicionless searches of an arrestee’s person and immediate surroundings,

should apply to cell-phone searches. In addressing that issue, the Court noted that it had

limited the scope of searches falling within this doctrine. For example, the “extensive

warrantless search of [an arrestee’s] home” cannot be justified as an incident to arrest. 573

U.S. at 383 (citing Chimel v. California, 395 U.S. 752, 763, 768 (1969)). This doctrine

also does not justify the search of a car once the arrestee has been secured or otherwise

brought beyond reach of the vehicle’s passenger compartment. Id. at 374 (citing Arizona

v. Gant, 556 U.S. 332 (2009)). The Riley Court determined that, for similar reasons, the

“particular category of effects” before it (i.e., cell phones) fell outside the search-incident-

to-arrest doctrine. Id. at 386. In doing so, the Court insisted that the availability of the

exception must turn categorically on the type of search. It expressly rejected the prospect

of “case-by-case adjudication” resting on “the probability in a particular arrest situation

that weapons or evidence would in fact be found.” Id. at 384 (quoting United States v.

Robinson, 414 U.S. 218, 235 (1973)).

       The Majority takes the very approach that Riley rejected, making the scope of the

border-search doctrine turn not just on the type of the search as a categorical matter but

also on a case-by-case analysis of the probability of finding contraband or evidence of a

“transnational” crime in the context of a specific search. If the Majority wants to rely on

Riley’s search-incident-to-arrest analysis, it should take the bitter with the sweet.


                                              31
       Thus, even if Riley has relevance for border searches, it teaches us to adopt a simpler

test, one unconcerned with the type of misconduct under investigation. Rather than look

at the type of governmental interest, the Supreme Court has already instructed us to look

at the type of search to determine what, if any, requirements should apply. Montoya de

Hernandez has given us a two-step analysis based on the type of border search: if the

search is routinely intrusive, then no suspicion is required; if the search is highly intrusive

and thus nonroutine, then some particularized suspicion is required. See United States v.

Oriakhi, 57 F.3d 1290, 1297 (4th Cir. 1995) (citing Montoya de Hernandez, 473 U.S. 531,

541 (1985)). 5 Instead of looking to the degree of intrusion, the Majority’s “nexus”

approach focuses on the purpose of the search. This approach fails to faithfully follow

either the Supreme Court’s border-search cases or Riley. I, therefore, respectfully disagree

with the Majority’s decision to hold the search unlawful on that basis.

                                              C.

       Despite my reservations, the Majority has made its “nexus” requirement the law of

this circuit. Having created it, how should it be applied? While apparently leaving the

details to another day, the Majority does require that officers have some basis to believe

that the border search will uncover (1) contraband or (2) evidence of a “transnational”



       5
         Perhaps there should be a third category for the most intrusive searches, like body-
cavity searches, where more than reasonable suspicion is required. But the Supreme Court
has not yet adopted one in its border-search cases (admittedly without ruling one out, see
Montoya de Hernandez, 473 U.S. at 541 n.4). And in evaluating its intrusiveness, a cell-
phone search surely cannot require more than the reasonable suspicion needed to justify
the “long, uncomfortable, indeed, humiliating” detention in Montoya de Hernandez. Id. at
544.

                                              32
crime. Applying that test here, the Majority concludes that the agents’ suspicion at the

time of the search failed to meet this requirement because, while Aigbekaen was suspected

of being an interstate sex trafficker, he was not suspected of being an international sex

trafficker. In my view, the Majority’s application of its “nexus” requirement is too narrow.

       Consider the evidence that the agents had against Aigbekaen when they conducted

the search. On April 12, 2015, a sixteen-year-old girl called 911 from a hotel in Bel Air,

Maryland. J.A. 53. She told police that “Raymond” and another man had taken her from

New York to Maryland and Virginia, where they had sold her to over one hundred men for

sex over the course of a few weeks.          She also explained that the men had used

Backpage.com to advertise her services.           Based on her statement and additional

information (a review of Backpage.com postings and hotel records), police identified both

men. J.A. 67. They learned that “Raymond” meant Aigbekaen, a Nigerian national, who

had paid for the room. J.A. 66. A search of the hotel room revealed used condoms. J.A.

272. Police also spoke to a manager at the hotel, who overheard the two men referring to

a “movie” they were making. J.A. 270. Officers learned that Aigbekaen had left the

country but would be returning to the United States at JFK International Airport. J.A. 107.

They alerted border agents, who stopped Aigbekaen at customs on May 19, 2015, and

searched his electronic devices. J.A. 108.

       As the Majority agrees, officers had probable cause to believe that Aigbekaen was

engaged in interstate sex trafficking of underage girls. Police had the underage victim’s

statement. They also found evidence that Aigbekaen rented a hotel room used for sex with

the girl. And there was evidence that Aigbekaen had used the internet to commit his crimes


                                             33
by posting advertisements on Backpage.com. This meant, of course, that there was

probable cause to believe that searching Aigbekaen’s electronic devices would turn up

relevant evidence. And it would beggar belief to claim that Aigbekaen’s crimes were

purely historical. Police knew that Aigbekaen had recently sold one underage victim to

over one hundred men over a short time. The reasonable inference was that his criminal

activity was professional and ongoing.

       These facts also supported reasonable suspicion that Aigbekaen’s interstate crimes

had an international component. Police knew he was a foreign national who trafficked

underage girls across state lines for profit and that, while engaged in that business, he

traveled abroad. There was at least some reason to suspect that Aigbekaen’s foreign travels

were not purely personal, but professional as well.

       Police also reasonably suspected that Aigbekaen was a foreign national traveling

from abroad into the United States with the intent to continue his criminal activity. Cf.

United States v. Oriakhi, 57 F.3d 1290, 1296 (4th Cir. 1995) (“From the sovereign’s power

to protect itself is derived its power to exclude harmful influences, including undesirable

aliens, from the sovereign’s territory.”).

       And despite the Majority’s suggestion, we may view the facts particular to

Aigbekaen against the background understanding that many sex crimes have a

transnational component. The trafficking of women across international lines is well

documented. So is the phenomenon of international “sex tourism.” These suspicions about

international misconduct may not have risen to the level of probable cause. But they did




                                             34
rise to the level of reasonable suspicion, which is all we should require to find an adequate

“nexus.” 6

       There were also reasonable grounds to suspect that Aigbekaen’s electronic devices

contained child pornography—a type of contraband. Aigbekaen had posted suggestive

photos of the underage victim on Backpage.com. While these photos apparently did not

constitute child pornography, there was reason to suspect that Aigbekaen might also have

more explicit pictures of his victims. (Indeed, given how widely used cell-phone cameras

are, one might reasonably guess that very few sex traffickers of underage girls do not have

child pornography on their phones.) But there was even more direct evidence: the hotel

manager had overheard Aigbekaen and his co-conspirator referring to a “movie” they were

making. Child pornography is contraband, and reasonable suspicion at the border that

someone’s electronic devices possess child pornography should be enough for a forensic

search under any theory.

       The Majority strains to conclude that there was no such reasonable suspicion. But

the Majority simply misapplies the law, in effect applying a standard tantamount to

probable cause (or perhaps something even more demanding). Reasonable suspicion

merely means, under “the totality of the circumstances,” there is “a particularized and

objective basis for suspecting legal wrongdoing.” United States v. Bernard, 927 F.3d 799,

805 (4th Cir. 2019) (quoting United States v. Vaughan, 700 F.3d 705, 710 (4th Cir. 2012)).


       6
        The Majority holds that the government lacked reasonable suspicion, leaving open
what level of suspicion is generally necessary for this type of search. I would require no
more than reasonable suspicion—assuming, of course, that some type of suspicion of a
nexus-related activity should be required in the first place.

                                             35
For example, if police see someone “driving erratically,” they have reasonable suspicion

that he might be “impaired or fatigued”—despite having no direct evidence. Id. In the

classic case, officers had “reasonable suspicion” that a group of men were planning to rob

a convenience store based on a combination of otherwise “innocent” acts, such as standing

around, walking back and forth, talking to each other, and looking at the store repeatedly.

Terry v. Ohio, 392 U.S. 1, 22–23 (1968). Here, there was a particularized and objective

basis for suspecting that Aigbekaen—a foreign national who trafficked underage girls for

sex across state lines, took photos of them, and was overheard discussing a “movie” with

his accomplice—was engaged in illegal conduct during his foreign travels, was entering

the country to keep engaging in ongoing and future criminal schemes, and had explicit

photos of underage girls on his phone.

       In sum, there was reasonable suspicion that Aigbekaen had contraband and that his

interstate crimes also had the “transnational” component the Majority would require. That

should be more than enough.

                                            ***

       The scope of the border-search doctrine raises difficult questions. But in my view,

the Majority’s “nexus” requirement does not faithfully follow the Supreme Court’s case

law. In any event, this requirement is satisfied here, making it a particularly troubling case

to reach beyond good faith to find the search unlawful.




                                             36

```

---

## GROUP: content/cases/United States v. Al-Azzawy.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Al-Azzawy
type: case
citation: "784 F.2d 890 (1986)"
parallel_cite: ""
neutral_cite: ""
court: 9th Cir.
court_level: coa
circuit: ca9
year: 1986
date_decided: 1986-03-11
docket: 85-5004
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
  opinion_url: "https://www.courtlistener.com/opinion/465254/united-states-v-riad-abed-al-azzawy/"
  cluster_id: 465254
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Al-Azzawy
  status: under_review
  projected_at: 2026-07-08
homes:
  - page: "[[Entry to Arrest]]"
    role: "Key — coerced-emergence pole (arrest location = suspect's position; exit at gunpoint = in-home arrest, 784 F.2d at 893-95)"
  - page: "[[Arrest in the Home]]"
    role: "Related — cross-doctrine (Payton reach)"
---

# United States v. Al-Azzawy

*784 F.2d 890 (9th Cir. 1986)* (No. 85-5004) · U.S. Court of Appeals, 9th Cir. · **Binding in-circuit — 9th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the treatment framing below is authored orientation, not machine-certified. Identity cluster 465254 → 784 F.2d 890, No. 85-5004, decided 1986-03-11 (Beezer, J.). Rule/Application quotes string-matched to the CL opinion text 2026-07-08. Distinct from the earlier 768 F.2d 1141 (1985, No. 84-5367). -->

## Background
Police were summoned to a trailer park after a neighbor reported that Riad Al-Azzawy had threatened to shoot him, to blow up the trailer park, and to burn his trailer, and that Al-Azzawy possessed hand grenades and automatic weapons. Officers "then surrounded appellee's trailer with their guns drawn, and ordered appellee to come outside." When Al-Azzawy appeared he was ordered to his knees, frisked, and questioned; he admitted having firearms inside. The district court suppressed the resulting evidence as the fruit of a warrantless in-home arrest and search; the government appealed.

## Issue
Where officers surround a suspect's dwelling with weapons drawn and order him out over a bullhorn, whether the ensuing arrest occurs "inside" the home for *[[Payton v. New York|Payton]]* purposes even though the suspect physically emerges before being seized.

## Rule
The location of the arrest is fixed by the suspect's position at the moment his freedom is overborne, not by where he happens to be standing when handcuffed. "In the case at bar, the police had completely surrounded appellee's trailer with their weapons drawn and ordered him through a bullhorn to leave the trailer and drop to his knees. Appellee was not free to leave, his freedom of movement was totally restricted, and the officers' show of force and authority was overwhelming." 784 F.2d at 894. ^pin-894

"Moreover, since appellee was in his trailer at the time he was surrounded by armed officers, and since he did not voluntarily expose himself to their view or control outside his trailer but only emerged under circumstances of extreme coercion, the arrest occurred while he was still inside his trailer." *Id.* at 894–95. ^pin-895

## Application
Applying that rule, the court held that "appellee was arrested inside his residence" without a warrant. But the inquiry did not end there: because the reported threats (grenades, automatic weapons, and a threat to blow up the trailer park) established genuine [[Exigent Circumstances and Hot Pursuit|exigent circumstances]], the warrantless in-home arrest was justified, and the district court's suppression order was error. The court therefore **reversed**. ^pin-895b

Al-Azzawy thus establishes *both* poles of the analysis: coerced emergence from a surrounded home is an in-home arrest (the containment/exit-command rule), yet a real, present danger can supply the [[Exigent Circumstances and Hot Pursuit|exigency]] that excuses the warrant.

## Conclusion
Reversed. A suspect who emerges from his surrounded home only under overwhelming coercion is arrested inside it; here, [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] arising from the armed threats justified the warrantless in-home arrest.

## Treatment & subsequent history
- **Status:** ⚪ unverified (frontier stub) — **Binding in-circuit — 9th Cir.** Treatment/progeny not machine-certified until S9 promotion.
- *Al-Azzawy* is the coerced-emergence pole of the Ninth-Circuit surround-and-call-out line. It is the anchor *[[United States v. Nora]]* distinguishes at 894 (Nora had no comparable "agitated and violent state," and the perimeter defeated any flight [[Exigent Circumstances and Hot Pursuit|exigency]]), and the coercion counterpoint to the voluntary-exposure holding of *[[United States v. Vaneaton]]*, 49 F.3d 1423 (9th Cir. 1995).

*Status note (⚪):* authored from a CourtListener-verified identity stub (two-key: cluster 465254 + 784 F.2d 890); renders under the ⚪ banner until S9 promotion.

## Appears on
- [[Entry to Arrest]] — *Key*
- [[Arrest in the Home]] — *Key*

## Sources
- [*United States v. Al-Azzawy*, 784 F.2d 890 (9th Cir. 1986)](https://www.courtlistener.com/opinion/465254/united-states-v-riad-abed-al-azzawy/) — pinpoints: 894 (surround/bullhorn = total restraint), 894–95 (coerced emergence = arrest inside the home; exigency justified the warrantless in-home arrest); quotes string-matched to the CL opinion text 2026-07-08.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "606cbf4c8a1d0ffe", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "784 F.2d 890 (1986)", "court": "9th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Al-Azzawy", "year": "1986"}}
{"assertion_id": "949fa902e60c1c92", "dimension": "support", "kind": "home_role", "locator": {"home": "Entry to Arrest"}, "payload": {"home": "Entry to Arrest", "role": "Key — coerced-emergence pole (arrest location = suspect's position; exit at gunpoint = in-home arrest, 784 F.2d at 893-95)", "title": "United States v. Al-Azzawy"}}
{"assertion_id": "a6d6253a808ec196", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Related — cross-doctrine (Payton reach)", "title": "United States v. Al-Azzawy"}}
{"assertion_id": "42d779464d7bfa66", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 9th Cir.", "title": "United States v. Al-Azzawy"}}
{"assertion_id": "88584113b7fe1074", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Al-Azzawy", "varies_by_point": "false"}}
```

### lake record — United States v. Al-Azzawy

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Al-Azzawy",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Riad Abed Al-Azzawy",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellant, v. Riad Abed AL-AZZAWY, Defendant-Appellee",
    "input_case_name": "United States v. Al-Azzawy",
    "court": "9th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": "1986-03-11",
    "year": 1986,
    "docket": "85-5004",
    "cluster_id": 465254,
    "lead_opinion_id": 465254,
    "sibling_ids": [],
    "absolute_url": "/opinion/465254/united-states-v-riad-abed-al-azzawy/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "784 F.2d 890",
      "volume": "784",
      "reporter": "F.2d",
      "page": "890",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "784 F.2d 890",
        "volume": "784",
        "reporter": "F.2d",
        "page": "890",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "784 F.2d 890",
    "official_selection": {
      "court_class": "coa",
      "selected": "784 F.2d 890",
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
    "date_created": "2026-07-08T16:52:38Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-08T16:52:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T16:52:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T16:52:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-08T16:52:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-al-azzawy--465254",
      "to_record_id": "United States v. Al-Azzawy",
      "as_of": "2026-07-08T22:30:00Z",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Al-Azzawy

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b983-15">
  BEEZER, Circuit Judge:
 </author>
<p id="b983-16">
  The government appeals a district court ruling excluding certain evidence on the ground that it resulted from an unlawful warrantless arrest of appellee in his residence and an unlawful warrantless search. We reverse.
 </p>
<p id="b983-17">
  At approximately 9 a.m. on November 19, 1984, Los Angeles police were summoned to investigate a disturbance at a trailer park. Steven Williams told the officers that Riad Abed Al-Azzawy, a neighbor, had threatened to shoot Williams, to blow up the trailer park and to burn Williams’ trailer. Williams also told the officers that Al-Azzawy had threatened him with a pistol the day before, and that a third party had told Williams that he had seen Al-Azzawy in possession of hand grenades and automatic weapons some days earlier.
 </p>
<p id="b983-19">
  Police officers then surrounded appellee’s trailer with their guns drawn, and ordered appellee to come outside. When Al-Azzawy appeared, he was ordered to get on his knees and place his hands on or above his head, which he did. He was then frisked and questioned about the disturbance. Appellee admitted having firearms in his trailer.
 </p>
<p id="b983-20">
  According to the police, appellee and his wife were asked if their trailer could be searched, and both consented. Both denied ever being asked for their consent.
 </p>
<p id="b983-21">
  During the search the police seized sawed-off weapons, an automatic pistol, three hand grenades, gunpowder, a gallon jug full of gasoline with matches glued to it, and other items. Appellee was charged with possession of unregistered firearms and being an illegal alien in possession of a firearm.
 </p>
<p id="b983-22">
  The district court granted appellee’s motion to exclude the unregistered firearms from evidence, holding that appellee was arrested in his home without a warrant or an exception to the warrant requirement. The court also held that appellee verbally consented to the search of his trailer, but that the consent was invalid, both because of the coercive circumstances and because it was tainted by appellee’s prior illegal arrest. The court also ruled that the search was not justified by exigent circumstances. The government appeals.
 </p>
<p id="b983-23">
  On appeal, the government argues that appellee was initially only subjected to a
  <em>
   Terry
  </em>
  stop when he was ordered out of his trailer, and that the later warrantless arrest occurred outside the trailer.
  <em>
   See Terry v. Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, 20
  <span citation-index="1" class="star-pagination" label="892"> 
   *892
   </span>
  L.Ed.2d 889 (1968). The district court’s decisions to the contrary are questions of law subject to de novo review.
  <em>
   See United States v. McConney,
  </em>
  <span class="citation" data-id="9471865"><a href="/opinion/431931/united-states-v-winston-bryant-mcconney/" aria-description="Citation for case: United States v. Winston Bryant McConney">728 F.2d 1195</a></span> (9th Cir.) (en banc),
  <em>
   cert. denied,
  </em>
  — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./105/101/">105 S.Ct. 101</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/83/46/">83 L.Ed.2d 46</a></span> (1984).
 </p>
<p id="b984-6">
  In
  <em>
   United States v. Morgan,
  </em>
  <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d 1158</a></span> (6th Cir.1984),
  <em>
   cert. denied,
  </em>
  — U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./105/2126/">105 S.Ct. 2126</a></span>, <span class="citation no-link">85 L.Ed.2d 490</span> (1985), the Sixth Circuit decided a case almost identical to the one at bar. While investigating a complaint of target shooting in a public park, a Sheriff was told by an unidentified observer that the suspects had numerous machine guns and other weapons, and that they had threatened to “kill any law that tries to arrest them.” <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1160" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d at 1160</a></span>. The Sheriff broadcast an alert describing the suspects’ car, which was found at the home of defendant Morgan’s mother.
  <em>
   <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">Id.</a></span>
  </em>
  Nine officers converged on the home, surrounded it, flooded it with spotlights, and summoned Morgan from the house with a bullhorn. <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1161" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d at 1161</a></span>. After the suspects left the house, they were arrested, handcuffed and frisked, and the house was searched.
  <em>
   <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">Id.</a></span>
  </em>
</p>
<p id="b984-9">
  The court held that the suspects had been arrested, saying:
 </p>
<blockquote id="b984-10">
  “These circumstances surely amount to a show of official authority such that ‘a reasonable person would have believed he was not free to leave.’ ”
  <em>
   Florida v. Royer,
  </em>
  460 U.S. [491, 501-03, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#1326" aria-description="Citation for case: Florida v. Royer">103 S.Ct. 1319, 1326-27</a></span>, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">75 L.Ed.2d 229</a></span> (1983) ]____ Viewed objectively, Morgan was placed under arrest, without the issuance of a warrant, at the moment the police encircled the Morgan residence.
 </blockquote>
<p id="A-c">
  <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1164" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d at 1164</a></span>.
 </p>
<p id="b984-13">
  Similarly, the court rejected the argument that the actual arrest occurred outside the home because the agents did not cross the threshold:
 </p>
<blockquote id="b984-14">
  We agree with the Ninth Circuit that the important consideration in this type of case “is the location of the arrested person, and not the arresting agent, that determines whether an arrest occurs within a home.”
 </blockquote>
<blockquote id="b984-15">
  Applying this rule here, it is undisputed that Morgan was peacefully residing in his mother’s home until he was aroused by the police activities occurring outside. Morgan was then compelled to leave the house. Thus, as in
  <em>
   Johnson, supra,
  </em>
  “it cannot be said that [Morgan] voluntarily exposed himself to a warrant-less arrest” by appearing at the door. On the contrary, Morgan appeared at the door
  <em>
   only because
  </em>
  o/the coercive police behavior taking place outside of the house____ Viewed in these terms, the arrest of Morgan occurred while he was present inside a private home. Although there was no direct police entry into the Morgan home prior to Morgan’s arrest, the constructive entry accomplished the same thing, namely, the arrest of Morgan. Thus, the warrantless arrest of Morgan, as he stood within the door of a private home, after emerging in response to coercive police conduct, violated Morgan’s fourth amendment rights.
 </blockquote>
<p id="b984-18">
  <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1166" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d at 1166</a></span> (citations omitted).
 </p>
<p id="b984-19">
  The principles set forth in
  <em>
   <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">Morgan</a></span>
  </em>
  are consistent with the law of this circuit. In
  <em>
   United States v. Johnson,
  </em>
  <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">626 F.2d 753</a></span> (9th Cir.1980),
  <em>
   aff'd on other grounds,
  </em>
  <span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">457 U.S. 537</a></span>, <span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">102 S.Ct. 2579</a></span>, <span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">73 L.Ed.2d 202</a></span> (1982), for example, two Secret Service agents approached the door of a suspect’s home, drew their weapons, pointed them downward and knocked, at first identifying themselves by fictitious names. When the suspect opened the door, the agents identified themselves as special agents and asked to talk with the suspect. He told them to come in. This court began its analysis by stating that
 </p>
<blockquote id="AqE">
  whether an arrest has occurred depends upon an objective, not subjective, evaluation of what a person innocent of a crime would have thought of the situation, given all of the factors involved. When an arrest has occurred depends in each case upon an evaluation of all the surrounding circumstances. Primary among these is a determination of whether or not the defendant was free to choose between terminating or continuing the encounter with the law enforcement officers____
  <span citation-index="1" class="star-pagination" label="893"> 
   *893
   </span>
  From a review of all of the circumstances surrounding the encounter between Johnson and the special agents, we find that appellant’s arrest occurred as he stood within his home at the doorway of his home and was first confronted by the agents with their guns drawn____ It is extremely doubtful that Johnson would have believed that he was free to leave at any time or to request the officers to leave after the initial encounter. A reasonable person, under those circumstances, would have thought he was under arrest.
 </blockquote>
<p id="b985-6">
  <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/#755" aria-description="Citation for case: United States v. Raymond Eugene Johnson">626 F.2d at 755-56</a></span>.
  <em>
   See also United States v. Patterson,
  </em>
  <span class="citation" data-id="9467917"><a href="/opinion/390276/united-states-v-edward-d-patterson-richard-l-flintoff-jimmie-r/#632" aria-description="Citation for case: United States v. Edward D. Patterson, Richard L....">648 F.2d 625, 632</a></span> (9th Cir.1981) (“Whether an arrest has occurred ‘depends on all of the surrounding circumstances, including the extent that freedom of movement is curtailed and the degree and type of force or authority used to effectuate the stop.’ ... The question is whether, under all of the circumstances, ‘a reasonable person would conclude he was under arrest.’ ”). Regarding the exact location of the arrest, the court stated:
 </p>
<blockquote id="b985-7">
  In this case, we are confronted with the situation where the suspect was arrested as he stood inside his home and the officers stood outside his home with drawn weapons. In these circumstances, it is the location of the arrested person, and not the arresting agents, that determines whether an arrest occurs within a home. Otherwise, arresting officers could avoid illegal “entry” into a home simply by remaining outside the doorway and controlling the movements of suspects within through the use of weapons that greatly extend the “reach” of the arresting officers.
 </blockquote>
<p id="b985-10">
  <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/#757" aria-description="Citation for case: United States v. Raymond Eugene Johnson">626 F.2d at 757</a></span>. The court distinguished cases upholding arrests at open doorways by noting that Johnson had opened his door only after the agents misrepresented their identities and that he invited them inside only after the door was opened and he was subjected to the coercive effect of their brandished weapons.
  <em>
   <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Id.</a></span>
  </em>
  Since “Johnson’s initial exposure to the view and physical control of the agents [and therefore to warrantless arrest] was not consensual on his part,” this court held that the arrest occurred within a residence.
  <em>
   <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Id.</a></span>
  </em>
<a class="footnote" href="#fn1" id="fn1_ref">
<em>
    1
   </em>
</a>
</p>
<p id="b985-11">
  In the case at bar, the police had completely surrounded appellee’s trailer with their weapons drawn and ordered him through a bullhorn to leave the trailer and drop to his knees. Appellee was not free to leave, his freedom of movement was totally restricted, and the officers’ show of force and authority was overwhelming. Any reasonable person would have believed he was under arrest in these circumstances. Moreover, since appellee was in his trailer at the time he was surrounded by armed officers, and since he did not voluntarily expose himself to their view or control outside his trailer but only emerged under circumstances of extreme coercion, the arrest occurred while he was still inside his trailer.
  <em>
   United States v. Johnson, supra.
  </em>
</p>
<p id="b985-12">
  We affirm the district court’s ruling that appellee was arrested inside his residence without a warrant.
 </p>
<p id="b985-13">
  Appellee next contends that the arrest was not supported by probable cause
  <span citation-index="1" class="star-pagination" label="894"> 
   *894
   </span>
  because the police acted on the information of only one witness who was not previously known to be reliable, they did not attempt to corroborate the information, and the information about the hand grenades and automatic weapons was hearsay.
 </p>
<blockquote id="b986-4">
  There is probable cause for a warrant-less arrest and a search incident to that arrest if, under the totality of the facts and circumstances known to the arresting officer, a prudent person would have concluded that there was a fair probability that the suspect had committed a crime____
 </blockquote>
<p id="b986-5">
<em>
   United States v. Gonzales,
  </em>
  <span class="citation" data-id="445284"><a href="/opinion/445284/united-states-v-esteban-leon-gonzales/#1337" aria-description="Citation for case: United States v. Esteban Leon Gonzales">749 F.2d 1329, 1337</a></span> (9th Cir.1984).
 </p>
<p id="b986-6">
  In the case at bar, Williams told the police that Al-Azzawy had threatened serious violence both aimed at persons and property and that Al-Azzawy possessed the means to carry out the threats. Regardless of whether the police had probable cause to suspect appellee of possessing illegal explosives or automatic weapons, we hold that they had probable cause to arrest him for assault.
 </p>
<p id="b986-7">
  Probable cause alone will not support a warrantless search or arrest in a residence, however, unless some exception to the warrant requirement is also present.
  <em>
   See Payton,
  </em>
  445 U.S. at 590, 100 S.Ct. at 1382;
  <em>
   United States v. Salvador,
  </em>
  <span class="citation" data-id="439305"><a href="/opinion/439305/united-states-v-elias-que-salvador-united-states-of-america-v-katrina/#758" aria-description="Citation for case: United States v. Elias Que Salvador, United States of...">740 F.2d 752, 758</a></span> (9th Cir.1984),
  <em>
   cert. denied,
  </em>
  — U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./105/978/">105 S.Ct. 978</a></span>, <span class="citation" data-id="9045702"><a href="/opinion/9052236/hersom-v-united-states-army/" aria-description="Citation for case: Hersom v. United States Army">83 L.Ed.2d 980</a></span> (1985). The government argues that appellee’s warrantless arrest was justified by the exception of exigent circumstances.
 </p>
<p id="b986-10">
  The Ninth Circuit has defined exigent circumstances as “ ‘those in which a substantial risk of harm to the persons involved or to the law enforcement process would arise if the police were to delay a search [or arrest] until a warrant could be obtained.’ ”
  <em>
   United States v. Salvador,
  </em>
  <span class="citation" data-id="439305"><a href="/opinion/439305/united-states-v-elias-que-salvador-united-states-of-america-v-katrina/" aria-description="Citation for case: United States v. Elias Que Salvador, United States of...">740 F.2d at 758</a></span> (quoting
  <em>
   United States v. Robertson,
  </em>
  <span class="citation" data-id="370365"><a href="/opinion/370365/united-states-v-johnny-bob-robertson/#859" aria-description="Citation for case: United States v. Johnny Bob Robertson">606 F.2d 853, 859</a></span> (9th Cir. 1979)). The burden is on the government to show that exigent circumstances existed and made the warrantless arrest imperative.
  <em>
   Vale v. Louisiana,
  </em>
  <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#34" aria-description="Citation for case: Vale v. Louisiana">399 U.S. 30, 34</a></span>, <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#1972" aria-description="Citation for case: Vale v. Louisiana">90 S.Ct. 1969, 1972</a></span>, <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/" aria-description="Citation for case: Vale v. Louisiana">26 L.Ed.2d 409</a></span> (1970);
  <em>
   United States v. Salvador,
  </em>
  <span class="citation" data-id="439305"><a href="/opinion/439305/united-states-v-elias-que-salvador-united-states-of-america-v-katrina/#758" aria-description="Citation for case: United States v. Elias Que Salvador, United States of...">740 F.2d at 758</a></span>. We review the district court’s ruling that exigent circumstances did not exist in this case de novo.
  <em>
   Id.; United States v. Hicks,
  </em>
  <span class="citation" data-id="446612"><a href="/opinion/446612/united-states-v-victoria-hicks/#383" aria-description="Citation for case: United States v. Victoria Hicks">752 F.2d 379, 383</a></span> (9th Cir.1985);
  <em>
   United States v. McConney,
  </em>
  <span class="citation" data-id="9471865"><a href="/opinion/431931/united-states-v-winston-bryant-mcconney/#1204" aria-description="Citation for case: United States v. Winston Bryant McConney">728 F.2d at 1204-05</a></span>; E.R. 220.
 </p>
<p id="b986-12">
  Whether the facts known to the officers in this case were sufficient to give rise to exigent circumstances is a close question. On the one hand, Williams had told the police that appellee’s threat of violence had been expressly conditioned on Williams somehow bothering his family again, all appeared calm around the Al-Azzawy trailer when the police arrived, there was no indication from appellee that he might be presently violent or try to flee, and the information concerning automatic weapons and explosives was entirely hearsay.
 </p>
<p id="b986-13">
  On the other hand, if the officers reasonably believed that appellee possessed illegal explosives and was in an agitated and violent state, there was a sufficiently substantial risk to human life to justify a warrant-less arrest.
  <em>
   But cf. United States v. Morgan,
  </em>
  <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1161" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d at 1161-63</a></span> (no exigent circumstances in case involving possible automatic weapons in similar circumstances). The district court concluded that there was no indication that Williams was unreliable and that the officers were therefore entitled to rely on his hearsay statements regarding the grenades without obtaining independent confirmation. Since such reliance seems both reasonable and necessary under the facts of this ease, we hold that exigent circumstances justified appellee’s warrantless arrest.
  <em>
   See, e.g., United States v. Doe,
  </em>
  <span class="citation" data-id="9473606"><a href="/opinion/453431/united-states-v-john-doe-minor-phx/" aria-description="Citation for case: United States v. John Doe (Minor, Phx)">764 F.2d 695</a></span> (9th Cir.1985);
  <em>
   United States v. Alfonso,
  </em>
  <span class="citation" data-id="450644"><a href="/opinion/450644/united-states-v-serafin-alfonso-humberto-rayo-fabian-mora-primo-antonio/" aria-description="Citation for case: United States v. Serafin Alfonso, Humberto Rayo, Fabian...">759 F.2d 728</a></span> (9th Cir.1985).
 </p>
<p id="b986-14">
  The district court also ruled that although the Al-Azzawys had verbally consented to the search, the consent was invalid because it was not voluntary and because it was tainted by the illegal arrest.
  <em>
   See Florida v. Royer,
  </em>
  <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U.S. 491</a></span>, 507-OS, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#1329" aria-description="Citation for case: Florida v. Royer">103 S.Ct. 1319, 1329-30</a></span>, 75 L.Ed.2d
  <span citation-index="1" class="star-pagination" label="895"> 
   *895
   </span>
  229 (1983) (illegal detention taints and invalidates consent search). Since we hold that exigent circumstances made the warrantless arrest legal, we need not discuss the latter issue.
 </p>
<p id="b987-4">
  The government has the burden of demonstrating that consent to a warrant-less search was voluntary.
  <em>
   United States v. Ritter,
  </em>
  <span class="citation" data-id="446623"><a href="/opinion/446623/united-states-v-alberto-ritter/#439" aria-description="Citation for case: United States v. Alberto Ritter">752 F.2d 435, 439</a></span> (9th Cir.1985). Voluntariness is a question of fact to be determined from all the surrounding circumstances.
  <em>
   <span class="citation" data-id="446623"><a href="/opinion/446623/united-states-v-alberto-ritter/" aria-description="Citation for case: United States v. Alberto Ritter">Id.</a></span>
  </em>
  A trial court’s finding on voluntariness should not be overturned unless it is clearly erroneous.
  <em>
   United States v. Faherty,
  </em>
  <span class="citation" data-id="9469933"><a href="/opinion/410980/united-states-v-caron-faherty/#1260" aria-description="Citation for case: United States v. Caron Faherty">692 F.2d 1258, 1260-61</a></span> (9th Cir.1982).
 </p>
<p id="b987-5">
  Although the Al-Azzawys did not argue that their consent was coerced, there were sufficient facts to support such a conclusion by the district court. The AlAzzawys had been approached by numerous police officers with their guns drawn while Mr. Al-Azzawy remained on his knees with his hands on his head.
  <em>
   See United States v. Mendenhall,
  </em>
  <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#559" aria-description="Citation for case: United States v. Mendenhall">446 U.S. 544, 559</a></span>, <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">100 S.Ct. 1870</a></span>, <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">64 L.Ed.2d 497</a></span> (1980) (whether suspect entered the coercive surroundings voluntarily found relevant to the validity of consent);
  <em>
   United States v. Perez,
  </em>
  <span class="citation" data-id="388822"><a href="/opinion/388822/united-states-v-jesus-perez-benjamin-ascencion-marquez-and-salomon-de-la/#1303" aria-description="Citation for case: United States v. Jesus Perez, Benjamin Ascencion Marquez...">644 F.2d 1299, 1303</a></span> (9th Cir.1981) (fact that suspects were approached by customs agents with drawn weapons one factor in finding consent involuntary). The Al-Azzawys were never informed of either their
  <em>
   Miranda
  </em>
  rights or their right to refuse consent to the search.
  <em>
   United States v. Mendenhall,
  </em>
  <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#558" aria-description="Citation for case: United States v. Mendenhall">446 U.S. at 558-59</a></span>, <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#1879" aria-description="Citation for case: United States v. Mendenhall">100 S.Ct. at 1879-80</a></span> (knowledge of right to refuse consent “highly relevant” to determination that there was consent);
  <em>
   United States v. Ritter,
  </em>
  <span class="citation" data-id="446623"><a href="/opinion/446623/united-states-v-alberto-ritter/#439" aria-description="Citation for case: United States v. Alberto Ritter">752 F.2d 435, 439</a></span> (9th Cir.1985) (absence of
  <em>
   Miranda
  </em>
  warnings is one factor in determining voluntariness of consent). Under these circumstances, we cannot say that the district court was clearly erroneous in finding that the consent was not voluntary.
 </p>
<p id="b987-8">
  The same factors and analysis apply to the presence of exigent circumstances for the warrantless trailer search that apply to the warrantless arrest. Since the police reasonably believed that the trailer contained explosives and that they were not able to arrest all of the persons entitled to enter the trailer (such as appellee’s two small children), we hold that the warrant-less search of the trailer was justified by exigent circumstances.
  <em>
   See United States v. Williams,
  </em>
  <span class="citation" data-id="380508"><a href="/opinion/380508/united-states-v-webster-williams/#703" aria-description="Citation for case: United States v. Webster Williams">626 F.2d 697, 703</a></span> (9th Cir.) (possibility of bomb in car “is an exigent circumstance sufficient to justify an immediate [warrantless] search”),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./449/1020/">449 U.S. 1020</a></span>,<span class="citation multiple-matches"><a href="/c/S.Ct./101/586/">101 S.Ct. 586</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/66/482/">66 L.Ed.2d 482</a></span> (1980).
 </p>
<p id="b987-9">
  We reverse the district court’s decision to exclude evidence on the grounds that the warrantless arrest and search were justified by exigent circumstances.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  The case is remanded for further proceedings consistent with this opinion.
 </p>


<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b985-8">
<em>
    .
   </em>
   Appellant argues that
   <em>
    <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">Morgan</a></span>
   </em>
   (and, by implication,
   <em>
    Johnson)
   </em>
   are both based on erroneous interpretations of
   <em>
    Payton v. New York,
   </em>
   <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U.S. 573</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980). It is true that
   <em>
    <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
   </em>
   condemned actual physical police intrusion into the home in order to make an arrest. The
   <em>
    <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">Morgan</a></span>
   </em>
   court found
   <em>
    <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
   </em>
   applicable, however, because it considered surrounding the house and ordering the suspect out to be a "constructive entry,” and because the suspect emerged from the house only because of police coercion. <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1166" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d at 1166</a></span>. Similarly, this court in
   <em>
    <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span>
   </em>
   noted the factual difference with
   <em>
    <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
   </em>
   but explained that "[w]e doubt the Supreme Court would have reached a different result had the police stood [just outside] the doorway and immediately placed [the suspect] under arrest with weapons drawn” rather than crossing the threshhold to make the arrest. 626 F.2d at 757. Moreover, the court noted that neither the
   <em>
    <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
   </em>
   nor the
   <em>
    <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span>
   </em>
   suspects
   <em>
    voluntarily
   </em>
   exposed themselves to the possibility of warrantless arrest.
   <em>
    <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Id.</a></span>
   </em>
   Since this court construes
   <em>
    <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
   </em>
   in much the same way the Sixth Circuit does, and since the
   <em>
    <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">Morgan</a></span>
   </em>
   court relied heavily on our
   <em>
    <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span>
   </em>
   decision, we cannot reject
   <em>
    <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">Morgan</a></span>
   </em>
   without at least implicitly overruling
   <em>
    <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span>.
   </em>
   We decline to do so.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b987-6">
   . Our decision makes it unnecessary to address the government’s argument that we should create a good-faith exception to the exclusionary rule for police conduct.
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/United States v. Anchondo.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Anchondo"
type: case
citation: "156 F.3d 1043 (1998)"
parallel_cite: ""
neutral_cite: "1998 U.S. App. LEXIS 21392; 1998 WL 559355"
court: "U.S. Court of Appeals, 10th Circuit"
court_level: coa
circuit: 10th
year: 1998
date_decided: 1998-09-01
docket: ""
authority_weight: "Binding in-circuit — 10th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: null
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Anchondo
  varies_by_point: false
  scope_note: "Good law. Often miscited as an automobile-exception case; its actual holding is search incident to arrest."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/758111/united-states-v-erick-anchondo/"
  cluster_id: 758111
  opinion_id: 758111
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Related (cross-doctrine)"
related: ["[[Chimel v. California]]", "[[Rawlings v. Kentucky]]", "[[Arizona v. Gant]]"]
aliases: ["United States v. Erick Anchondo"]
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "automobile"]
holding: "ACTUAL holding: cocaine found on the defendant's body was the product of a lawful SEARCH INCIDENT TO ARREST, not the automobile…"
lake:
  record_id: United States v. Anchondo
  status: under_review
  projected_at: 2026-07-06
---

# United States v. Anchondo

*156 F.3d 1043 (10th Cir. 1998)* · U.S. Court of Appeals, 10th Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers had probable cause to arrest Anchondo in connection with a drug transaction. They searched his person and found cocaine on his body, and the arrest followed shortly after the search. He moved to suppress the cocaine, and the search's validity turned on the search-incident-to-arrest exception rather than on any search of an automobile.

## Issue
Whether cocaine found on the defendant's person was lawfully obtained as a [[Search Incident to Arrest|search incident to arrest]] where the search preceded, rather than followed, the formal arrest.

## Rule
A search may validly precede the arrest it is incident to: "A warrantless search preceding an arrest is a legitimate 'search incident to arrest' as long as (1) a legitimate basis for the arrest existed before the search, and (2) the arrest followed shortly after the search." — 156 F.3d at 1045. ^pin-1045

Applying that rule, the court held that "the discovery of cocaine on the defendant's person was the result of a lawful search incident to arrest." — *Id.* at 1046. ^pin-1046

## Application
Because the officers had a legitimate basis to arrest Anchondo before they searched him, and the arrest followed shortly after, the search of his person was a lawful [[Search Incident to Arrest|search incident to arrest]] even though it came first; the cocaine found on his body was admissible. The court resolved the case on the search-incident-to-arrest exception — not the automobile exception — making *Anchondo* a frequently miscategorized authority.

## Conclusion
The search of Anchondo's person was a lawful [[Search Incident to Arrest|search incident to arrest]] and the cocaine was admissible; the conviction was affirmed. A [[Search Incident to Arrest|search incident to arrest]] may precede the arrest when probable cause already exists and the arrest follows promptly.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 10th Cir.**
- *Anchondo* applies the search-incident-to-arrest doctrine of [[Chimel v. California]] and the search-may-precede-arrest principle of [[Rawlings v. Kentucky]]. It is listed here on the **Automobile Exception** page as a cautionary cross-reference: despite frequent miscitation, its holding rests on [[Search Incident to Arrest|search incident to arrest]], not the automobile exception (compare [[Arizona v. Gant]] on vehicle [[Search Incident to Arrest|searches incident to arrest]]).

## Appears on
- [[Automobile Exception]] — *Related (cross-doctrine)*

## Sources
- *United States v. Anchondo*, 156 F.3d 1043 (10th Cir. 1998) — https://www.courtlistener.com/opinion/758111/united-states-v-erick-anchondo/ — pinpoints: 1045, 1046.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "489e8c8154118d8d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "156 F.3d 1043 (1998)", "court": "U.S. Court of Appeals, 10th Circuit", "neutral_cite": "1998 U.S. App. LEXIS 21392; 1998 WL 559355", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Anchondo", "year": "1998"}}
{"assertion_id": "150eb33b4cc08ba8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "ACTUAL holding: cocaine found on the defendant's body was the product of a lawful SEARCH INCIDENT TO ARREST, not the automobile…", "title": "United States v. Anchondo"}}
{"assertion_id": "8176215af4c96cae", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Related (cross-doctrine)", "title": "United States v. Anchondo"}}
{"assertion_id": "d150fc5cb9f74d1e", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Anchondo", "field_i_validity": "good_law", "scope_note": "Good law. Often miscited as an automobile-exception case; its actual holding is search incident to arrest.", "title": "United States v. Anchondo", "varies_by_point": "false"}}
{"assertion_id": "f3b5a6481d9c7452", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 10th Cir.", "title": "United States v. Anchondo"}}
```

### lake record — United States v. Anchondo

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Anchondo",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Erick Anchondo",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Erick ANCHONDO, Defendant-Appellant",
    "input_case_name": "United States v. Anchondo",
    "court": "U.S. Court of Appeals, 10th Circuit",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "10th",
    "state": null,
    "date_decided": "1998-09-01",
    "year": 1998,
    "docket": null,
    "cluster_id": 758111,
    "lead_opinion_id": 758111,
    "sibling_ids": [
      758111
    ],
    "absolute_url": "/opinion/758111/united-states-v-erick-anchondo/",
    "identity_method": "pending",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "156 F.3d 1043",
      "volume": "156",
      "reporter": "F.3d",
      "page": "1043",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1998 U.S. App. LEXIS 21392",
        "volume": "1998",
        "reporter": "U.S. App. LEXIS",
        "page": "21392",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 WL 559355",
        "volume": "1998",
        "reporter": "WL",
        "page": "559355",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "156 F.3d 1043",
        "volume": "156",
        "reporter": "F.3d",
        "page": "1043",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 U.S. App. LEXIS 21392",
        "volume": "1998",
        "reporter": "U.S. App. LEXIS",
        "page": "21392",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 WL 559355",
        "volume": "1998",
        "reporter": "WL",
        "page": "559355",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "156 F.3d 1043",
    "official_selection": {
      "court_class": "coa",
      "selected": "156 F.3d 1043",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1045",
      "page": null,
      "quote": "--- # United States v. Anchondo *156 F.3d 1043 (10th Cir. 1998)* \u00b7 U.S. Court of Appeals, 10th Circuit \u00b7 **Binding in-circuit \u2014 10th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers had probable cause to arrest Anchondo in connection with a drug transaction. They searched his person and found cocaine on his body, and the arrest followed shortly after the search. He moved to suppress the cocaine, and the search's validity turned on the search-incident-to-arrest exception rather than on any search of an automobile. ## Issue Whether cocaine found on the defendant's person was lawfully obtained as a search incident to arrest where the search preceded, rather than followed, the formal arrest. ## Rule A search may validly precede the arrest it is incident to:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1046",
      "page": null,
      "quote": "the discovery of cocaine on the defendant's person was the result of a lawful search incident to arrest.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": null,
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Anchondo",
    "varies_by_point": false,
    "scope_note": "Good law. Often miscited as an automobile-exception case; its actual holding is search incident to arrest.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. McKissick",
          "cluster_id": 159263,
          "cite": [
            "204 F.3d 1282",
            "2000 Colo. J. C.A.R. 1203",
            "2000 U.S. App. LEXIS 2719",
            "2000 WL 216949"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rosborough",
          "cluster_id": 164599,
          "cite": [
            "366 F.3d 1145",
            "2004 U.S. App. LEXIS 8651",
            "2004 WL 938459"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Claudio Lugo, AKA Lugo Mano, Joel Logue-Lugo, Joel Lugo Luke",
          "cluster_id": 762490,
          "cite": [
            "170 F.3d 996",
            "51 Fed. R. Serv. 918",
            "1999 Colo. J. C.A.R. 1420",
            "1999 U.S. App. LEXIS 3948",
            "1999 WL 128901"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Victor Manuel Torres-Castro",
          "cluster_id": 796200,
          "cite": [
            "470 F.3d 992",
            "2006 U.S. App. LEXIS 30420",
            "2006 WL 3598365"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Anderson",
          "cluster_id": 2575795,
          "cite": [
            "281 Kan. 896",
            "136 P.3d 406",
            "2006 Kan. LEXIS 355"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gibson",
          "cluster_id": 2626323,
          "cite": [
            "108 P.3d 424",
            "141 Idaho 277",
            "2005 Ida. App. LEXIS 21"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sanchez",
          "cluster_id": 171758,
          "cite": [
            "555 F.3d 910",
            "2009 U.S. App. LEXIS 2474",
            "2009 WL 311267"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cash",
          "cluster_id": 4870403,
          "cite": [
            "483 P.3d 1047"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whitehead v. Com.",
          "cluster_id": 1058299,
          "cite": [
            "683 S.E.2d 299",
            "278 Va. 300"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Howards v. McLaughlin",
          "cluster_id": 212271,
          "cite": [
            "634 F.3d 1131",
            "2011 WL 856275"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Conn",
          "cluster_id": 2582083,
          "cite": [
            "99 P.3d 1108",
            "278 Kan. 387",
            "2004 Kan. LEXIS 651"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Adam Chartier",
          "cluster_id": 2755606,
          "cite": [
            "772 F.3d 539",
            "2014 U.S. App. LEXIS 22323",
            "2014 WL 6678412"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "UNITED STATES v. DAVID D. LEWIS",
          "cluster_id": 4281856,
          "cite": [
            "147 A.3d 236",
            "2016 D.C. App. LEXIS 369",
            "2016 WL 5539892"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ojeda-Ramos",
          "cluster_id": 167867,
          "cite": [
            "455 F.3d 1178",
            "2006 U.S. App. LEXIS 19175",
            "2006 WL 2106801"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mercado-Nava",
          "cluster_id": 2522106,
          "cite": [
            "486 F. Supp. 2d 1271",
            "2007 U.S. Dist. LEXIS 27486",
            "2007 WL 1098203"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Martin",
          "cluster_id": 9484380,
          "cite": [
            "544 P.3d 820"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hoskins v. Withers",
          "cluster_id": 9476608,
          "cite": [
            "92 F.4th 1279"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Chapman",
          "cluster_id": 4649632,
          "cite": [
            "2019 Ohio 3339"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Romero",
          "cluster_id": 2471071,
          "cite": [
            "743 F. Supp. 2d 1281",
            "2010 U.S. Dist. LEXIS 91598",
            "2010 WL 3829636"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Urdiales",
          "cluster_id": 2898078,
          "cite": [
            "2015 Ohio 3632"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Torres-Castro",
          "cluster_id": 2397679,
          "cite": [
            "374 F. Supp. 2d 994",
            "2005 U.S. Dist. LEXIS 13810",
            "2005 WL 1554701"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "STATE v. COUSAN",
          "cluster_id": 4688823,
          "cite": [
            "447 P.3d 481"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whitehead v. Commonwealth",
          "cluster_id": 1062623,
          "cite": [
            "668 S.E.2d 435",
            "53 Va. App. 1",
            "2008 Va. App. LEXIS 503",
            "2008 WL 4862460"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Dudsak",
          "cluster_id": 5289164,
          "cite": [
            "2021 Ohio 3632"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "STATE v. COUSAN",
          "cluster_id": 4689527,
          "cite": [
            "2019 OK CR 16",
            "447 P.3d 481"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(758111) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca10)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(758111)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01JnM9Mjg5ODA3OCZ0PW8mZD0yMDI2LTA3LTA2JnA9Mg%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28758111%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(758111)",
        "reviewed": 4,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 4,
        "triage_read": 0,
        "triage_snippet_classified": 4
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(758111)",
    "indexed_citing_opinions": 33,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 758111,
        "count": 33,
        "count_source": "search"
      }
    ],
    "citation_count": 54,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-anchondo.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjIxOTY2NTkmcz0xMDYyNjIzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28758111%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 758111,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 758111,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 758111,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 758111,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 758111,
        "cited_id": 349459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 758111,
        "cited_id": 518495,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 758111,
        "cited_id": 563786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 758111,
        "cited_id": 658364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 758111,
        "cited_id": 736301,
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
    "date_created": "2026-07-05T22:04:14Z",
    "date_modified": "2026-07-06T08:58:18Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:04:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:04:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:11:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:04:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Anchondo

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b1122-15">
  TACHA, Circuit Judge.
 </author>
<p id="b1122-16">
  The defendant was indicted on one of count of possession with intent to distribute more than 500 grams of cocaine, in violation of <span class="citation no-link">21 U.S.C. § 841</span>(a)(1) and 841(b)(1)(B), and for aiding and abetting, in violation of <span class="citation no-link">18 U.S.C. § 2</span>. After the district court denied his motion to suppress evidence, the defendant entered a conditional guilty plea. He now appeals the denial of his motion to suppress. We take jurisdiction pursuant to <span class="citation no-link">28 U.S.C. § 1291</span> and affirm.
 </p>
<p id="b1122-17">
  1.
 </p>
<p id="b1122-18">
  On the evening of January 9, 1997, the defendant and his passenger, Felipe Garcia, stopped at a fixed checkpoint on Highway I-25, about 26 miles north of Las Cruces, New Mexico. While one border patrol agent asked the men routine questions, another agent walked a drug-sniffing canine around the exterior of the defendant’s sedan. During this canine inspection, the dog “alerted,” indicating the presence of illegal narcotics.
 </p>
<p id="b1122-19">
  Based on the canine alert, the agents asked the defendant to move his car to a secondary inspection area in order to confirm the canine’s alert. The defendant consented, moved the ear, and voluntarily exited the vehicle to allow a more thorough search of the car. The dog again alerted to the inside of the ear and the defendant and Garcia were moved to a nearby trailer.
 </p>
<p id="b1122-20">
  The border patrol agents were unable to locate the presence of any contraband in the vehicle. Agent Alvarado went to the trailer and asked the defendant and Garcia if they had any personal amounts of contraband in the vehicle. Defendant responded by stating: “[yjou’re not going to find anything in that vehicle.” Applt. App. at 11. At the suppression hearing, the defendant denied making this statement. In reviewing a motion to suppress, however, we consider the evidence in the light most favorable to the district court’s ruling,
  <em>
   see United States v. Elliott,
  </em>
  <span class="citation" data-id="736301"><a href="/opinion/736301/united-states-v-asta-m-elliott/#813" aria-description="Citation for case: United States v. Asta M. Elliott">107 F.3d 810, 813</a></span> (10th Cir.1997), md therefore must assume the statement was made.
 </p>
<p id="b1122-21">
  Agent Jose Alvarado then conducted a ‘pat and frisk” of the defendant’s outer cloth
  <span citation-index="1" class="star-pagination" label="1045"> 
   *1045
   </span>
  ing, which he described as “loose.” Applt. App. at 12. During the search, Agent Alvarado felt a hard object in the defendant’s waistline. The agent testified that he believed the object to be the butt of a semiautomatic handgun. The agent removed the object and found that it was a package of cocaine strapped to the defendant’s stomach. Four such packages were recovered from the defendant. Marijuana was found on the body of Garcia.
 </p>
<p id="b1123-5">
  II.
 </p>
<p id="b1123-6">
  When reviewing a district court’s grant or denial of a motion to suppress, we accept the district court’s factual findings unless they are clearly erroneous.
  <em>
   See Elliott,
  </em>
  <span class="citation" data-id="736301"><a href="/opinion/736301/united-states-v-asta-m-elliott/#813" aria-description="Citation for case: United States v. Asta M. Elliott">107 F.3d at 813</a></span>. The ultimate conclusion of whether the Fourth Amendment allowed a particular stop, however, is a legal determination that we review de novo.
  <em>
   See <span class="citation" data-id="736301"><a href="/opinion/736301/united-states-v-asta-m-elliott/" aria-description="Citation for case: United States v. Asta M. Elliott">id.</a></span>
  </em>
</p>
<p id="b1123-7">
  The defendant admits that the officers had probable cause to search the vehicle. He argues, however, that under the totality of the circumstances, the agents had no authority to search the defendant’s person for illegal narcotics. Furthermore, the defendant argues that the agents cannot even make the less onerous showing under
  <em>
   Terry v. Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968), to justify a pat-down search of the defendant for weaponry. According to the defendant, if the agents had truly thought that the defendant posed a threat to their safety, they would have patted him down immediately after moving him to the secondary inspection area.
 </p>
<p id="b1123-8">
  We find it unnecessary to address the parties arguments on the application of
  <em>
   Terry v. Ohio
  </em>
  to this case because the agents were justified in conducting a full, warrant-less search of the defendant under these circumstances. The Fourth Amendment normally requires that law enforcement officers obtain a warrant, based on probable cause, before conducting a search.
  <em>
   See, e.g., New York v. Belton,
  </em>
  <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#457" aria-description="Citation for case: New York v. Belton">453 U.S. 454, 457</a></span>, <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">101 S.Ct. 2860</a></span>, <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">69 L.Ed.2d 768</a></span> (1981). There are limited exceptions to that rule, however, one of which is that officers may conduct a war-rantless search of a person when it is incident to a lawful arrest of that person.
  <em>
   See Chimel v. California,
  </em>
  <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California">395 U.S. 752, 762-63</a></span>, <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">89 S.Ct. 2034</a></span>, <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">23 L.Ed.2d 685</a></span> (1969). In order to be a legitimate “search incident to arrest,” the search need not take place after the arrest. A warrantless search preceding an arrest is a legitimate “search incident to arrest” as long as (1) a legitimate basis for the arrest existed before the search, and (2) the arrest followed shortly after the search.
  <em>
   See United States v. Rivera,
  </em>
  <span class="citation" data-id="518495"><a href="/opinion/518495/united-states-v-jesus-antonio-rivera/#1264" aria-description="Citation for case: United States v. Jesus Antonio Rivera">867 F.2d 1261, 1264</a></span> (10th Cir.1989);
  <em>
   cf. Rawlings v. Kentucky,
  </em>
  <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/#111" aria-description="Citation for case: Rawlings v. Kentucky">448 U.S. 98, 111</a></span>, <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">100 S.Ct. 2556</a></span>, <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">65 L.Ed.2d 633</a></span> (1980) (stating that where the arrest was justified before the search and the arrest “followed quickly on the heels of the challenged search of petitioner’s person, we do not believe it particularly important that the search preceded the arrest rather than vice versa.”). Whether or not the officer intended to actually arrest the defendant at the time of the search is immaterial to this two-part inquiry.
  <em>
   See United States v. Ricard,
  </em>
  <span class="citation" data-id="349459"><a href="/opinion/349459/united-states-v-raymond-ernest-ricard/#49" aria-description="Citation for case: United States v. Raymond Ernest Ricard">563 F.2d 45, 49</a></span> (2d Cir.1977).
 </p>
<p id="b1123-10">
  First, we inquire as to whether the agent had a legitimate basis to arrest the defendant at the time of the search. Arrests must be based on probable cause. Probable cause to arrest exists when an officer has learned of facts and circumstances through reasonably trustworthy information that would lead a reasonable person to believe that an offense has been or is being committed by the person arrested.
  <em>
   See United States v. Morgan,
  </em>
  <span class="citation" data-id="9481753"><a href="/opinion/563786/united-states-v-rodney-lee-morgan/#1568" aria-description="Citation for case: United States v. Rodney Lee Morgan">936 F.2d 1561, 1568</a></span> (10th Cir.1991). A canine alert provides the probable cause necessary for searches and seizures.
  <em>
   See United States v. Ludwig,
  </em>
  <span class="citation" data-id="658364"><a href="/opinion/658364/united-states-v-keith-rudolph-ludwig-national-association-of-criminal/#1527" aria-description="Citation for case: United States v. Keith Rudolph Ludwig, National...">10 F.3d 1523, 1527</a></span> (10th Cir.1993). Here, the canine alerted twice to the inside of the defendant’s car. Under
  <em>
   <span class="citation" data-id="658364"><a href="/opinion/658364/united-states-v-keith-rudolph-ludwig-national-association-of-criminal/" aria-description="Citation for case: United States v. Keith Rudolph Ludwig, National...">Ludwig</a></span>,
  </em>
  that provided the probable cause necessary to arrest the defendant. Even if the subsequent fruitless search of the car diminished the probability of contraband being in the car, it increased the chances that whatever the dog had alerted to was on the defendants’ bodies.
 </p>
<p id="b1123-11">
  Second, we determine whether the actual arrest was too remote from the search. Here, the arrest occurred immediately after
  <span citation-index="1" class="star-pagination" label="1046"> 
   *1046
   </span>
  the drugs were found on the defendant’s body.
 </p>
<p id="b1124-4">
  III.
 </p>
<p id="b1124-5">
  Given the above analysis, the discovery of cocaine on the defendant’s person was the result of a lawful search incident to arrest. We AFFIRM.
 </p>
</opinion>
```

---
