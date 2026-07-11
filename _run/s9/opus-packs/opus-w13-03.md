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

## GROUP: _overhaul2/lake/cases/Torres v. Madrid.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Torres v. Madrid"
type: case
citation: "592 U.S. 306 (2021)"
parallel_cite: "141 S. Ct. 989; 209 L. Ed. 2d 190"
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2021
date_decided: 2021-03-25
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2021-03-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Torres v. Madrid
  varies_by_point: false
  scope_note: "Recent SCOTUS holding; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4867542/torres-v-madrid/"
  cluster_id: 4867542
  opinion_id: 4671321
  identity_checked: true
homes:
  - page: "[[Seizure of the Person]]"
    role: "Key — Progeny / Refinement"
related: ["[[California v. Hodari D.]]", "[[Tennessee v. Garner]]", "[[Graham v. Connor]]", "[[Brendlin v. California]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure"]
holding: "Physical force applied with intent to restrain is a seizure at the moment of application, even if the person does not submit and is not subdued."
lake:
  record_id: Torres v. Madrid
  status: verified
  projected_at: 2026-07-06
---

# Torres v. Madrid

*592 U.S. 306 (2021)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
New Mexico State Police officers approached Torres in an apartment-complex parking lot to execute an arrest warrant for someone else. Torres, who was experiencing methamphetamine withdrawal, got into her car; the officers, believing she was reaching for a weapon, fired thirteen shots, striking her twice in the back. She nonetheless drove away, eluding capture that day, and later sued under § 1983, claiming the shooting was an unreasonable seizure.

## Issue
Whether the application of physical force to a person with intent to restrain is a Fourth Amendment seizure when the force does not succeed in subduing the person and she temporarily eludes capture.

## Rule
Yes. Adopting the common-law rule that the slightest application of force to effect an arrest is an arrest, the Court held: "The application of physical force to the body of a person with intent to restrain is a seizure, even if the force does not succeed in subduing the person." — slip op., at 1. ^pin-op1

A seizure by force is complete at the moment force is applied with intent to restrain; submission is not required. The Court cautioned that such a seizure is only the first step in the analysis — only unreasonable seizures violate the Fourth Amendment.

## Application
Because the officers shot Torres with the intent to restrain her, the bullets that struck her effected a seizure at the moment of impact — notwithstanding that she managed to drive away and was not subdued or apprehended until the next day. The shooting was therefore a seizure of her person, and the lower court erred in holding that her escape defeated any seizure; whether that seizure was reasonable remained for remand.

## Conclusion
The shooting was a seizure even though Torres temporarily eluded capture; the judgment was [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]]. Physical force applied with intent to restrain seizes the person at the instant of application.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Torres* distinguishes [[California v. Hodari D.]], where an unsubmitting suspect chased but not touched was not seized; the force/intent rule traces to the deadly-force seizure framework of [[Tennessee v. Garner]], with reasonableness governed by [[Graham v. Connor]].

## Appears on
- [[Seizure of the Person]] — *Key — Progeny / Refinement*

## Sources
- *Torres v. Madrid*, 592 U.S. 306 (2021) — https://www.courtlistener.com/opinion/4867542/torres-v-madrid/ — pinpoint: slip op., at 1 (CL carries the slip opinion; cluster 4867542 → opinion 4671321).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7d22dd06da1235bc", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Torres v. Madrid"}, "payload": {"all": [{"cite": "592 U.S. 306", "page": "306", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "592"}, {"cite": "141 S. Ct. 989", "page": "989", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "141"}, {"cite": "209 L. Ed. 2d 190", "page": "190", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "209"}], "display": "592 U.S. 306", "official": {"cite": "592 U.S. 306", "page": "306", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "592"}, "official_selection_present": true, "record_id": "Torres v. Madrid"}}
{"assertion_id": "3c6e52e95614a243", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op1", "record_id": "Torres v. Madrid"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op1", "pinpoint_status": "slip-only", "quote": "--- # Torres v. Madrid *592 U.S. 306 (2021)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background New Mexico State Police officers approached Torres in an apartment-complex parking lot to execute an arrest warrant for someone else. Torres, who was experiencing methamphetamine withdrawal, got into her car; the officers, believing she was reaching for a weapon, fired thirteen shots, striking her twice in the back. She nonetheless drove away, eluding capture that day, and later sued under § 1983, claiming the shooting was an unreasonable seizure. ## Issue Whether the application of physical force to a person with intent to restrain is a Fourth Amendment seizure when the force does not succeed in subduing the person and she temporarily eludes capture. ## Rule Yes. Adopting the common-law rule that the slightest application of force to effect an arrest is an arrest, the Court held:", "quote_fidelity": "mismatch", "record_id": "Torres v. Madrid", "star_marker": null}}
{"assertion_id": "6e3928120c590f54", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Torres v. Madrid"}, "payload": {"as_of_content": "2021-03-25", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Torres v. Madrid", "scope_note": "Recent SCOTUS holding; good law.", "varies_by_point": false}}
```

### lake record — Torres v. Madrid

```json
{
  "schema_version": "s2.v1",
  "record_id": "Torres v. Madrid",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Torres v. Madrid",
    "case_name_short": "Torres",
    "case_name_full": "",
    "input_case_name": "Torres v. Madrid",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2021-03-25",
    "year": 2021,
    "docket": null,
    "cluster_id": 4867542,
    "lead_opinion_id": 4671321,
    "sibling_ids": [
      4671321
    ],
    "absolute_url": "/opinion/4867542/torres-v-madrid/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "592 U.S. 306",
      "volume": "592",
      "reporter": "U.S.",
      "page": "306",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "141 S. Ct. 989",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "989",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "209 L. Ed. 2d 190",
        "volume": "209",
        "reporter": "L. Ed. 2d",
        "page": "190",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "592 U.S. 306",
        "volume": "592",
        "reporter": "U.S.",
        "page": "306",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 989",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "989",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "209 L. Ed. 2d 190",
        "volume": "209",
        "reporter": "L. Ed. 2d",
        "page": "190",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "592 U.S. 306",
    "official_selection": {
      "court_class": "scotus",
      "selected": "592 U.S. 306",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op1",
      "page": null,
      "quote": "--- # Torres v. Madrid *592 U.S. 306 (2021)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background New Mexico State Police officers approached Torres in an apartment-complex parking lot to execute an arrest warrant for someone else. Torres, who was experiencing methamphetamine withdrawal, got into her car; the officers, believing she was reaching for a weapon, fired thirteen shots, striking her twice in the back. She nonetheless drove away, eluding capture that day, and later sued under \u00a7 1983, claiming the shooting was an unreasonable seizure. ## Issue Whether the application of physical force to a person with intent to restrain is a Fourth Amendment seizure when the force does not succeed in subduing the person and she temporarily eludes capture. ## Rule Yes. Adopting the common-law rule that the slightest application of force to effect an arrest is an arrest, the Court held:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2021-03-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Torres v. Madrid",
    "varies_by_point": false,
    "scope_note": "Recent SCOTUS holding; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Andrew Lennette, Individually and on behalf of C.L., O.L. and S.L., Minor Children v. State of Iowa, Melody Siver, Amy Howell, and Valerie Lovaglia",
          "cluster_id": 6476611,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jerry Smith, Jr. v. Melvin Finkley",
          "cluster_id": 4970388,
          "cite": [
            "10 F.4th 725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zailey Hess v. Jamie Garcia",
          "cluster_id": 9415232,
          "cite": [
            "72 F.4th 753"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gloria Taylor v. City of Milford",
          "cluster_id": 4982498,
          "cite": [
            "10 F.4th 800"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Devin Jefferson v. George Lias",
          "cluster_id": 5307076,
          "cite": [
            "21 F.4th 74"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
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
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark Campbell v. Cheatham County Sheriff's Dep't",
          "cluster_id": 7860703,
          "cite": [
            "47 F.4th 468"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brittany J. Buckley v. Hennepin County",
          "cluster_id": 4957820,
          "cite": [
            "9 F.4th 757"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. Madrid",
          "cluster_id": 9376547,
          "cite": [
            "60 F.4th 596"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Larry Jones, Jr.",
          "cluster_id": 5428746,
          "cite": [
            "22 F.4th 667"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Keith Smith v. City of Chicago",
          "cluster_id": 4895377,
          "cite": [
            "3 F.4th 332"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rosa Cuevas v. City of Tulare",
          "cluster_id": 9999054,
          "cite": [
            "107 F.4th 894"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "April Sabbe v. Washington Cnty Bd of Comm'rs",
          "cluster_id": 9433444,
          "cite": [
            "84 F.4th 807"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Preston Seidner v. Jonathan De Vries",
          "cluster_id": 6620483,
          "cite": [
            "39 F.4th 591"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Weaver",
          "cluster_id": 4957807,
          "cite": [
            "9 F.4th 129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark Nieters v. Brandon Holtan",
          "cluster_id": 9431950,
          "cite": [
            "83 F.4th 1099"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vardeman v. City of Houston",
          "cluster_id": 9354006,
          "cite": [
            "55 F.4th 1045"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Huff v. Reeves",
          "cluster_id": 4881659,
          "cite": [
            "996 F.3d 1082"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vanessa Dundon v. Kyle Kirchmeier",
          "cluster_id": 9437055,
          "cite": [
            "85 F.4th 1250"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jackson",
          "cluster_id": 9328456,
          "cite": [
            "218 N.E.3d 790",
            "171 Ohio St. 3d 412",
            "2022 Ohio 4365"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dwayne Furlow v. Jon Belmar",
          "cluster_id": 8436813,
          "cite": [
            "52 F.4th 393"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wright",
          "cluster_id": 9368876,
          "cite": [
            "57 F.4th 524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Derrick Sanderlin v. Jason Dwyer",
          "cluster_id": 10104398,
          "cite": [
            "116 F.4th 905"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Timothy Cloud",
          "cluster_id": 4872727,
          "cite": [
            "994 F.3d 233"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stephen Hopkins v. Anthony Nichols",
          "cluster_id": 6478429,
          "cite": [
            "37 F.4th 1110"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4671321) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 73,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 73,
        "triage_read": 1,
        "triage_snippet_classified": 72
      },
      "lane2_top_cited": {
        "query": "cites:(4671321)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01JnM9MTAwMDY2NDUmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%284671321%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(4671321)",
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
    "complete_query": "cites:(4671321)",
    "indexed_citing_opinions": 104,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4671321,
        "count": 104,
        "count_source": "search"
      }
    ],
    "citation_count": 380,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/torres-v-madrid.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3NTcxNTQmcz05NDkzNjE4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%284671321%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4671321,
        "cited_id": 85330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 85464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 88142,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 88824,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 102310,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 112218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 112579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 112919,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 118334,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 145688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 145712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 145738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 145777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 152652,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 622304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 2620702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 3819289,
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
    "date_created": "2026-07-05T21:47:23Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:48:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:48:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:52:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:48:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Torres v. Madrid

```
(Slip Opinion)              OCTOBER TERM, 2020                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                      TORRES v. MADRID ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                 THE TENTH CIRCUIT

    No. 19–292.      Argued October 14, 2020—Decided March 25, 2021
Respondents Janice Madrid and Richard Williamson, officers with the
  New Mexico State Police, arrived at an Albuquerque apartment com-
  plex to execute an arrest warrant and approached petitioner Roxanne
  Torres, then standing near a Toyota FJ Cruiser. The officers at-
  tempted to speak with her as she got into the driver’s seat. Believing
  the officers to be carjackers, Torres hit the gas to escape. The officers
  fired their service pistols 13 times to stop Torres, striking her twice.
  Torres managed to escape and drove to a hospital 75 miles away, only
  to be airlifted back to a hospital in Albuquerque, where the police ar-
  rested her the next day. Torres later sought damages from the officers
  under 42 U. S. C. §1983. She claimed that the officers used excessive
  force against her and that the shooting constituted an unreasonable
  seizure under the Fourth Amendment. Affirming the District Court’s
  grant of summary judgment to the officers, the Tenth Circuit held that
  “a suspect’s continued flight after being shot by police negates a Fourth
  Amendment excessive-force claim.” 769 Fed. Appx. 654, 657.
Held: The application of physical force to the body of a person with intent
 to restrain is a seizure even if the person does not submit and is not
 subdued. Pp. 3–18.
    (a) The Fourth Amendment protects “[t]he right of the people to be
 secure in their persons, houses, papers, and effects, against unreason-
 able searches and seizures.” This Court’s precedents have interpreted
 the term “seizure” by consulting the common law of arrest, the “quin-
 tessential” seizure of the person. Payton v. New York, 445 U. S. 573,
 585; California v. Hodari D., 499 U. S. 621, 624. In Hodari D., this
 Court explained that the common law considered the application of
 physical force to the body of a person with the intent to restrain to be
 an arrest—not an attempted arrest—even if the person does not yield.
2                           TORRES v. MADRID

                                   Syllabus

    Id., at 624–625. A review of the pertinent English and American deci-
    sions confirms that the slightest touching was a constructive detention
    that would complete the arrest. See, e.g., Genner v. Sparks, 6 Mod.
    173, 87 Eng. Rep. 928.
       The analysis does not change because the officers used force from a
    distance to restrain Torres. The required “corporal seising or touching
    the defendant’s body,” 3 W. Blackstone, Commentaries on the Laws of
    England 288 (1768), can be as readily accomplished by a bullet as by
    the end of a finger. The focus of the Fourth Amendment is “the privacy
    and security of individuals,” not the particular form of governmental
    intrusion. Camara v. Municipal Court of City and County of San Fran-
    cisco, 387 U. S. 523, 528.
       The application of force, standing alone, does not satisfy the rule
    recognized in this decision. A seizure requires the use of force with
    intent to restrain, as opposed to force applied by accident or for some
    other purpose. County of Sacramento v. Lewis, 523 U. S. 833, 844. The
    appropriate inquiry is whether the challenged conduct objectively
    manifests an intent to restrain. Michigan v. Chesternut, 486 U. S. 567,
    574. This test does not depend on either the subjective motivation of
    the officer or the subjective perception of the suspect. Finally, a sei-
    zure by force lasts only as long as the application of force unless the
    suspect submits. Hodari D., 499 U. S., at 625. Pp. 3–11.
       (b) In place of the rule that the application of force completes an
    arrest, the officers would assess all seizures under one test: intentional
    acquisition of control. This alternative approach finds support in nei-
    ther the history of the Fourth Amendment nor this Court’s precedents.
    Pp. 11–16.
          (1) The officers attempt to recast the common law doctrine recog-
    nized in Hodari D. as a rule applicable only to civil arrests. But the
    common law did not define the arrest of a debtor any differently from
    the arrest of a felon. Treatises and courts discussing criminal arrests
    articulated a rule indistinguishable from the one applied to civil ar-
    rests at common law. Pp. 11–14.
          (2) The officers’ contrary test would limit seizures of a person to
    “an intentional acquisition of physical control.” Brower v. County of
    Inyo, 489 U. S. 593, 596. While that test properly describes seizures
    by control, seizures by force enjoy a separate common law pedigree
    that gives rise to a separate rule. A seizure by acquisition of control
    involves either voluntary submission to a show of authority or the ter-
    mination of freedom of movement. But as common law courts recog-
    nized, any such requirement of control would be difficult to apply to
    seizures by force. The officers’ test will often yield uncertainty about
    whether an officer succeeded in gaining control over a suspect. For
    centuries, the rule recognized in this opinion has avoided such line-
                     Cite as: 592 U. S. ____ (2021)                      3

                                Syllabus

  drawing problems. Pp. 14–16.
     (c) The officers seized Torres by shooting her with the intent to re-
  strain her movement. This Court does not address the reasonableness
  of the seizure, the damages caused by the seizure, or the officers’ enti-
  tlement to qualified immunity. Pp. 17–18.
769 Fed. Appx. 654, vacated and remanded.

  ROBERTS, C. J., delivered the opinion of the Court, in which BREYER,
SOTOMAYOR, KAGAN, and KAVANAUGH, JJ., joined. GORSUCH, J., filed a
dissenting opinion, in which THOMAS and ALITO, JJ., joined. BARRETT, J.,
took no part in the consideration or decision of the case.
                        Cite as: 592 U. S. ____ (2021)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 19–292
                                    _________________


             ROXANNE TORRES, PETITIONER v.
                 JANICE MADRID, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE TENTH CIRCUIT
                                 [March 25, 2021]

  CHIEF JUSTICE ROBERTS delivered the opinion of the
Court.
  The Fourth Amendment prohibits unreasonable “sei-
zures” to safeguard “[t]he right of the people to be secure in
their persons.” Under our cases, an officer seizes a person
when he uses force to apprehend her. The question in this
case is whether a seizure occurs when an officer shoots
someone who temporarily eludes capture after the shooting.
The answer is yes: The application of physical force to the
body of a person with intent to restrain is a seizure, even if
the force does not succeed in subduing the person.
                             I
  At dawn on July 15, 2014, four New Mexico State Police
officers arrived at an apartment complex in Albuquerque to
execute an arrest warrant for a woman accused of white col-
lar crimes, but also “suspected of having been involved in
drug trafficking, murder, and other violent crimes.” App.
to Pet. for Cert. 11a. What happened next is hotly con-
tested. We recount the facts in the light most favorable to
petitioner Roxanne Torres because the court below granted
summary judgment to Officers Janice Madrid and Richard
2                    TORRES v. MADRID

                      Opinion of the Court

Williamson, the two respondents here. Tolan v. Cotton, 572
U. S. 650, 655–656 (2014) (per curiam).
   The officers observed Torres standing with another per-
son near a Toyota FJ Cruiser in the parking lot of the com-
plex. Officer Williamson concluded that neither Torres nor
her companion was the target of the warrant. As the offic-
ers approached the vehicle, the companion departed, and
Torres—at the time experiencing methamphetamine with-
drawal—got into the driver’s seat. The officers attempted
to speak with her, but she did not notice their presence until
one of them tried to open the door of her car.
   Although the officers wore tactical vests marked with po-
lice identification, Torres saw only that they had guns. She
thought the officers were carjackers trying to steal her car,
and she hit the gas to escape them. Neither Officer Madrid
nor Officer Williamson, according to Torres, stood in the
path of the vehicle, but both fired their service pistols to
stop her. All told, the two officers fired 13 shots at Torres,
striking her twice in the back and temporarily paralyzing
her left arm.
   Steering with her right arm, Torres accelerated through
the fusillade of bullets, exited the apartment complex, drove
a short distance, and stopped in a parking lot. After asking
a bystander to report an attempted carjacking, Torres stole
a Kia Soul that happened to be idling nearby and drove 75
miles to Grants, New Mexico. The good news for Torres was
that the hospital in Grants was able to airlift her to another
hospital where she could receive appropriate care. The bad
news was that the hospital was back in Albuquerque, where
the police arrested her the next day. She pleaded no contest
to aggravated fleeing from a law enforcement officer, as-
sault on a peace officer, and unlawfully taking a motor
vehicle.
   Torres later sought damages from Officers Madrid and
Williamson under 42 U. S. C. §1983, which provides a cause
                  Cite as: 592 U. S. ____ (2021)              3

                      Opinion of the Court

of action for the deprivation of constitutional rights by per-
sons acting under color of state law. She claimed that the
officers applied excessive force, making the shooting an un-
reasonable seizure under the Fourth Amendment. The Dis-
trict Court granted summary judgment to the officers, and
the Court of Appeals for the Tenth Circuit affirmed on the
ground that “a suspect’s continued flight after being shot by
police negates a Fourth Amendment excessive-force claim.”
769 Fed. Appx. 654, 657 (2019). The court relied on Circuit
precedent providing that “no seizure can occur unless there
is physical touch or a show of authority,” and that “such
physical touch (or force) must terminate the suspect’s move-
ment” or otherwise give rise to physical control over the sus-
pect. Brooks v. Gaenzle, 614 F. 3d 1213, 1223 (2010).
   We granted certiorari. 589 U. S. ___ (2019).
                               II
   The Fourth Amendment protects “[t]he right of the people
to be secure in their persons, houses, papers, and effects,
against unreasonable searches and seizures.” This case
concerns the “seizure” of a “person,” which can take the
form of “physical force” or a “show of authority” that “in
some way restrain[s] the liberty” of the person. Terry v.
Ohio, 392 U. S. 1, 19, n. 16 (1968). The question before us
is whether the application of physical force is a seizure if
the force, despite hitting its target, fails to stop the person.
   We largely covered this ground in California v. Hodari
D., 499 U. S. 621 (1991). There we interpreted the term
“seizure” by consulting the common law of arrest, the “quin-
tessential ‘seizure of the person’ under our Fourth Amend-
ment jurisprudence.” Id., at 624. As Justice Scalia ex-
plained for himself and six other Members of the Court, the
common law treated “the mere grasping or application of
physical force with lawful authority” as an arrest, “whether
or not it succeeded in subduing the arrestee.” Ibid.; see id.,
at 625 (“merely touching” sufficient to constitute an arrest).
4                     TORRES v. MADRID

                      Opinion of the Court

Put another way, an officer’s application of physical force to
the body of a person “ ‘for the purpose of arresting him’ ” was
itself an arrest—not an attempted arrest—even if the per-
son did not yield. Id., at 624 (quoting Whithead v. Keyes, 85
Mass. 495, 501 (1862)).
   The common law distinguished the application of force
from a show of authority, such as an order for a suspect to
halt. The latter does not become an arrest unless and until
the arrestee complies with the demand. As the Court ex-
plained in Hodari D., “[a]n arrest requires either physical
force . . . or, where that is absent, submission to the asser-
tion of authority.” 499 U. S., at 626 (emphasis in original).
   Hodari D. articulates two pertinent principles. First,
common law arrests are Fourth Amendment seizures. And
second, the common law considered the application of force
to the body of a person with intent to restrain to be an ar-
rest, no matter whether the arrestee escaped. We need not
decide whether Hodari D., which principally concerned a
show of authority, controls the outcome of this case as a
matter of stare decisis, because we independently reach the
same conclusions.
   At the adoption of the Fourth Amendment, a “seizure”
was the “act of taking by warrant” or “of laying hold on sud-
denly”—for example, when an “officer seizes a thief.” 2 N.
Webster, An American Dictionary of the English Language
67 (1828) (Webster) (emphasis deleted). A seizure did not
necessarily result in actual control or detention. It is true
that, when speaking of property, “[f]rom the time of the
founding to the present, the word ‘seizure’ has meant a ‘tak-
ing possession.’ ” Hodari D., 499 U. S., at 624 (quoting 2
Webster 67). But the Framers selected a term—seizure—
broad enough to apply to all the concerns of the Fourth
Amendment: “persons,” as well as “houses, papers, and ef-
fects.” As applied to a person, “[t]he word ‘seizure’ readily
bears the meaning of a laying on of hands or application of
                   Cite as: 592 U. S. ____ (2021)              5

                       Opinion of the Court

physical force to restrain movement, even when it is ulti-
mately unsuccessful.” 499 U. S., at 626. Then, as now, an
ordinary user of the English language could remark: “She
seized the purse-snatcher, but he broke out of her grasp.”
Ibid.
   The “seizure” of a “person” plainly refers to an arrest.
That linkage existed at the founding. Samuel Johnson, for
example, defined an “arrest” as “[a]ny . . . seizure of the per-
son.” 1 A Dictionary of the English Language 108 (4th ed.
1773). And that linkage persists today. As we have repeat-
edly recognized, “the arrest of a person is quintessentially
a seizure.” Payton v. New York, 445 U. S. 573, 585 (1980)
(internal quotation marks omitted); see Hodari D., 499
U. S., at 624.
   Because arrests are seizures of a person, Hodari D.
properly looked to the common law of arrest for “historical
understandings ‘of what was deemed an unreasonable
search and seizure when the Fourth Amendment was
adopted.’ ” Carpenter v. United States, 585 U. S. ___, ___
(2018) (slip op., at 6) (quoting Carroll v. United States, 267
U. S. 132, 149 (1925); alteration omitted). Sometimes the
historical record will not yield a well-settled legal rule. See,
e.g., Atwater v. Lago Vista, 532 U. S. 318, 327–328 (2001);
Payton, 445 U. S., at 593–596. We do not face that problem
here. The cases and commentary speak with virtual una-
nimity on the question before us today.
   The common law rule identified in Hodari D.—that the
application of force gives rise to an arrest, even if the officer
does not secure control over the arrestee—achieved recog-
nition to such an extent that English lawyers could confi-
dently (and accurately) proclaim that “[a]ll the authorities,
from the earliest time to the present, establish that a cor-
poral touch is sufficient to constitute an arrest, even though
the defendant do not submit.” Nicholl v. Darley, 2 Y. & J.
399, 400, 148 Eng. Rep. 974 (Exch. 1828) (citing Hodges v.
Marks, Cro. Jac. 485, 79 Eng. Rep. 414 (K. B. 1615)). The
6                     TORRES v. MADRID

                      Opinion of the Court

slightest application of force could satisfy this rule. In Gen-
ner v. Sparks, 6 Mod. 173, 87 Eng. Rep. 928 (Q. B. 1704),
the defendant did not submit to the authority of an arrest
warrant, but the court explained that the bailiff would have
made an arrest if he “had but touched the defendant even
with the end of his finger.” Ibid., 87 Eng. Rep., at 929. So
too, if a “bailiff caught one by the hand (whom he had a
warrant to arrest) as he held it out of a window,” that alone
would accomplish an arrest. Anonymus, 1 Vent. 306, 86
Eng. Rep. 197 (K. B. 1677). The touching of the person—
frequently called a laying of hands—was enough. See Dun-
scomb v. Smith, Cro. Car. 164, 79 Eng. Rep. 743 (K. B.
1629). Only later did English law grow to recognize arrest
without touching through a submission to a show of author-
ity. See Horner v. Battyn, Bull. N. P. 62 (K. B. 1738), re-
printed in W. Loyd, Cases on Civil Procedure 798 (1916).
Even so, the traditional rule persisted that all an arrest re-
quired was “corporal seising or touching the defendant’s
body.” 3 W. Blackstone, Commentaries on the Laws of Eng-
land 288 (1768) (Blackstone).
   Early American courts adopted this mere-touch rule from
England, just as they embraced other common law princi-
ples of search and seizure. See Wilson v. Arkansas, 514
U. S. 927, 933 (1995). Justice Baldwin, instructing a jury
in his capacity as Circuit Justice, defined an arrest to in-
clude “touching or putting hands upon [the arrestee] in the
execution of process.” United States v. Benner, 24 F. Cas.
1084, 1086–1087 (No. 14,568) (CC ED Pa. 1830). State
courts agreed that “any touching, however slight, is
enough,” Butler v. Washburn, 25 N. H. 251, 258 (1852), pro-
vided the officer made his intent to arrest clear, see Jones
v. Jones, 35 N. C. 448, 448–449 (1852). Courts continued to
hold that an arrest required only the application of force—
not control or custody—through the framing of the Four-
teenth Amendment, which incorporated the protections of
the Fourth Amendment against the States. See Whithead,
                  Cite as: 592 U. S. ____ (2021)            7

                      Opinion of the Court

85 Mass., at 501; Searls v. Viets, 2 Thomp. & C. 224, 226
(N. Y. Sup. Ct. 1873); State v. Dennis, 16 Del. 433, 436–437,
43 A. 261, 262 (1895); see also H. Voorhees, The Law of Ar-
rest in Civil and Criminal Actions §74, p. 44 (1904).
   Stated simply, the cases “abundantly shew that the
slightest touch [was] an arrest in point of law.” Nicholl, 2
Y. & J., at 404, 148 Eng. Rep., at 976. Indeed, it was not
even required that the officer have, at the time of such an
arrest, “the power of keeping the party so arrested under
restraint.” Sandon v. Jervis, El. Bl. & El. 935, 940, 120 Eng.
Rep. 758, 760 (Q. B. 1858). The consequences would be
“pernicious,” an English judge worried, if the question of
control “were perpetually to be submitted to a jury.” Ibid.;
cf. 3 Blackstone 120 (describing how “[t]he least touching of
another’s person” could satisfy the common law definition
of force to commit battery, “for the law cannot draw the line
between different degrees of violence”).
   This case, of course, does not involve “laying hands,”
Sheriff v. Godfrey, 7 Mod. 288, 289, 87 Eng. Rep. 1247 (K. B.
1739), but instead a shooting. Neither the parties nor the
United States as amicus curiae suggests that the officers’
use of bullets to restrain Torres alters the analysis in any
way. And we are aware of no common law authority ad-
dressing an arrest under such circumstances, or indeed any
case involving an application of force from a distance.
   The closest decision seems to be Countess of Rutland’s
Case, 6 Co. Rep. 52b, 77 Eng. Rep. 332 (Star Chamber
1605). In that case, serjeants-at-mace tracked down Isabel
Holcroft, Countess of Rutland, to execute a writ for a judg-
ment of debt. They “shewed her their mace, and touching
her body with it, said to her, we arrest you, madam.” Id.,
at 54a, 77 Eng. Rep., at 336. We think the case is best un-
derstood as an example of an arrest made by touching with
an object, for the serjeants-at-mace announced the arrest at
the time they touched the countess with the mace. See, e.g.,
8                        TORRES v. MADRID

                          Opinion of the Court

Hodges, Cro. Jac., at 485, 79 Eng. Rep., at 414 (similar an-
nouncement upon laying of hands). Maybe the arrest could
be viewed as a submission to a show of authority, because a
mace served not only as a weapon but also as an insignia of
office. See Kelly, The Great Mace, and Other Corporation
Insignia of the Borough of Leicester, 3 Transactions of the
Royal Hist. Soc. 295, 296–301 (1874). But that view is dif-
ficult to reconcile with the fact that English courts did not
recognize arrest by submission to a show of authority until
the following century. See supra, at 6.*
   However one reads Countess of Rutland, we see no basis
for drawing an artificial line between grasping with a hand
and other means of applying physical force to effect an ar-
rest. The dissent (though not the officers) argues that the
common law limited arrests by force to the literal place-
ment of hands on the suspect, because no court published
an opinion discussing a suspect who continued to flee after
being hit with a bullet or some other weapon. See post, at
18–20 (opinion of GORSUCH, J.). This objection calls to mind
the unavailing defense of the person who “persistently de-
nied that he had laid hands upon a priest, for he had only
cudgelled and kicked him.” 2 S. Pufendorf, De Jure Natu-
rae et Gentium 795 (C. Oldfather & W. Oldfather transl.
1934). The required “corporal seising or touching the de-
fendant’s body” can be as readily accomplished by a bullet
as by the end of a finger. 3 Blackstone 288.
   We will not carve out this greater intrusion on personal
security from the mere-touch rule just because founding-

——————
   *The arrest was not Isabel’s first brush with the law or money trou-
bles. A decade earlier, Elizabeth Charlton sued to recover for the estate
of her husband, the fourth Earl of Rutland, an assortment of jewels al-
legedly taken by Isabel, the widow of the third Earl of Rutland. Eliza-
beth bested Isabel in the clash of the countesses, and Isabel was found
liable for 940 pounds, worth about $400,000 today. Elizabeth Countess
of Rutland v. Isabel Countess of Rutland, Cro. Eliz. 377, 78 Eng. Rep. 624
(C. P. 1595).
                  Cite as: 592 U. S. ____ (2021)            9

                      Opinion of the Court

era courts did not confront apprehension by firearm. While
firearms have existed for a millennium and were certainly
familiar at the founding, we have observed that law en-
forcement did not carry handguns until the latter half of the
19th century, at which point “it bec[a]me possible to use
deadly force from a distance as a means of apprehension.”
Tennessee v. Garner, 471 U. S. 1, 14–15 (1985). So it should
come as no surprise that neither we nor the dissent has lo-
cated a common law case in which an officer used a gun to
apprehend a suspect. Cf. post, at 20 (discussing Dickenson
v. Watson, Jones, T. 205, 84 Eng. Rep. 1218, 1218–1219
(K. B. 1682), in which a tax collector accidentally dis-
charged hailshot into a passerby’s eye). But the focus of the
Fourth Amendment is “the privacy and security of individ-
uals,” not the particular manner of “arbitrary invasion[ ] by
governmental officials.” Camara v. Municipal Court of City
and County of San Francisco, 387 U. S. 523, 528 (1967). As
noted, our precedent protects “that degree of privacy
against government that existed when the Fourth Amend-
ment was adopted,” Kyllo v. United States, 533 U. S. 27, 34
(2001)—a protection that extends to “[s]ubtler and more
far-reaching means of invading privacy” adopted only later,
Olmstead v. United States, 277 U. S. 438, 473 (1928)
(Brandeis, J., dissenting). There is nothing subtle about a
bullet, but the Fourth Amendment preserves personal se-
curity with respect to methods of apprehension old and new.
   We stress, however, that the application of the common
law rule does not transform every physical contact between
a government employee and a member of the public into a
Fourth Amendment seizure. A seizure requires the use of
force with intent to restrain. Accidental force will not qual-
ify. See County of Sacramento v. Lewis, 523 U. S. 833, 844
(1998). Nor will force intentionally applied for some other
purpose satisfy this rule. In this opinion, we consider only
force used to apprehend. We do not accept the dissent’s in-
vitation to opine on matters not presented here—pepper
10                   TORRES v. MADRID

                      Opinion of the Court

spray, flash-bang grenades, lasers, and more. Post, at 23.
   Moreover, the appropriate inquiry is whether the chal-
lenged conduct objectively manifests an intent to restrain,
for we rarely probe the subjective motivations of police of-
ficers in the Fourth Amendment context. See Nieves v.
Bartlett, 587 U. S. ___, ___ (2019) (slip op., at 10). Only an
objective test “allows the police to determine in advance
whether the conduct contemplated will implicate the
Fourth Amendment.” Michigan v. Chesternut, 486 U. S.
567, 574 (1988). While a mere touch can be enough for a
seizure, the amount of force remains pertinent in assessing
the objective intent to restrain. A tap on the shoulder to get
one’s attention will rarely exhibit such an intent. See INS
v. Delgado, 466 U. S. 210, 220 (1984); Jones, 35 N. C., at
448–449.
   Nor does the seizure depend on the subjective perceptions
of the seized person. Here, for example, Torres claims to
have perceived the officers’ actions as an attempted carjack-
ing. But the conduct of the officers—ordering Torres to stop
and then shooting to restrain her movement—satisfies the
objective test for a seizure, regardless whether Torres com-
prehended the governmental character of their actions.
   The rule we announce today is narrow. In addition to the
requirement of intent to restrain, a seizure by force—absent
submission—lasts only as long as the application of force.
That is to say that the Fourth Amendment does not recog-
nize any “continuing arrest during the period of fugitivity.”
Hodari D., 499 U. S., at 625. The fleeting nature of some
seizures by force undoubtedly may inform what damages a
civil plaintiff may recover, and what evidence a criminal de-
fendant may exclude from trial. See, e.g., Utah v. Strieff,
579 U. S. ___, ___ (2016) (slip op., at 4). But brief seizures
are seizures all the same.
   Applying these principles to the facts viewed in the light
most favorable to Torres, the officers’ shooting applied
                  Cite as: 592 U. S. ____ (2021)            11

                      Opinion of the Court

physical force to her body and objectively manifested an in-
tent to restrain her from driving away. We therefore con-
clude that the officers seized Torres for the instant that the
bullets struck her.
                               III
   In place of the rule that the application of force completes
an arrest even if the arrestee eludes custody, the officers
would introduce a single test for all types of seizures: inten-
tional acquisition of control. This alternative rule is incon-
sistent with the history of the Fourth Amendment and our
cases.
                              A
   The officers and their amici stress that common law rules
are not automatically “elevated to constitutional proscrip-
tions,” Hodari D., 499 U. S., at 626, n. 2, especially if they
are “distorted almost beyond recognition when literally ap-
plied,” Garner, 471 U. S., at 15. In their view, the common
law doctrine recognized in Hodari D. is just “a narrow legal
rule intended to govern liability in civil cases involving
debtors.” Brief for National Association of Counties et al.
as Amici Curiae 12. The dissent presses the same argu-
ment. See post, at 14–17.
   But the common law did not define the arrest of a debtor
any differently from the arrest of a felon. Whether the ar-
rest was authorized by a criminal indictment or a civil writ,
“there must be a corporal seizing, or touching the defend-
ant’s person; or, what is tantamount, a power of taking im-
mediate possession of the body, and the party’s submission
thereto, and a declaration of the officer that he makes an
arrest.” 1 J. Backus, A Digest of Laws Relating to the Of-
fices and Duties of Sheriff, Coroner and Constable 115–116
(1812). Treatises on the law governing criminal arrests
cited Genner v. Sparks, 6 Mod. 173, 87 Eng. Rep. 928—the
preeminent mere-touch case involving a debtor—for the
12                    TORRES v. MADRID

                      Opinion of the Court

proposition that, “[i]n making the arrest, the constable or
party making it should actually seize or touch the offender’s
body, or otherwise restrain his liberty.” 1 R. Burn, The Jus-
tice of the Peace 275 (28th ed. 1837). When English courts
confronted arrests for criminal offenses, they too relied on
precedents concerning arrests for civil offenses. See
Bridgett v. Coyney, 1 Man. & Ryl. 1, 5–6 (K. B. 1827); Ar-
rowsmith v. Le Mesurier, 2 Bos. & Pul. 211, 211–212, 127
Eng. Rep. 605, 606 (C. P. 1806). American courts likewise
articulated a materially identical definition in criminal
cases—that “[t]he arrest itself is the laying hands on the
defendant,” State v. Townsend, 5 Del. 487, 488 (Ct. Gen.
Sess. 1854), or that an arrest is “the taking, seizing, or de-
taining of the person of another, either by touching him or
putting hands on him,” McAdams v. State, 30 Okla. Crim.
207, 210, 235 P. 241, 242 (1925).
   This uniform definition also explains why an arrest by
mere touch carried legal consequences in both the criminal
and civil contexts. The point of an arrest was of course to
take custody of a person to secure his appearance at a pro-
ceeding. But some arrests did not culminate in actual con-
trol of the individual, let alone a trip to the gaol or compter.
See Nicholl, 2 Y. & J., at 403–404, 148 Eng. Rep., at 975–
976. When an officer let an arrestee get away, the officer
risked becoming a defendant himself in an action for “es-
cape.” See Perkins, The Law of Arrest, 25 Iowa L. Rev. 201,
204 (1940). The laying of hands constituted a taking cus-
tody and would expose the officer to liability for the escape
of felons and debtors alike. See 1 M. Hale, Pleas of the
Crown 590–591, 597, 603 (1736); 2 id., at 93 (no liability for
escape “if the felon were not once in the hands of an officer”);
see also Perkins, 25 Iowa L. Rev., at 206.
   The tort of false imprisonment, which the dissent rightly
acknowledges as the “ ‘closest analogy’ to an arrest without
probable cause,” post, at 12 (quoting Wallace v. Kato, 549
U. S. 384, 388–389 (2007)), reinforces the conclusion that
                  Cite as: 592 U. S. ____ (2021)            13

                      Opinion of the Court

the common law considered touching to be a seizure. Stated
generally, false imprisonment required “confinement,” such
as “taking a person into custody under an asserted legal au-
thority.” Restatement of Torts §§35, 41 (1934); see 3 Black-
stone 127. But that element of confinement demanded no
more than that the defendant “had for one moment taken
possession of the plaintiff ’s person”—including, “for exam-
ple, if he had tapped her on the shoulder, and said, ‘You are
my prisoner.’ ” Simpson v. Hill, 1 Esp. 431, 431–432, 170
Eng. Rep. 409 (N. P. 1795); see Restatement of Torts §41,
Comment h (noting that “the touching alone of the person
against whom [legal authority] was asserted would be suf-
ficient to constitute” confinement by arrest when the au-
thority was valid). While the dissent emphasizes that “the
court [in Simpson] proceeded to reject the plaintiff ’s claim
for false imprisonment,” post, at 13, that was only because
“the constable never touched the plaintiff, or took her into
custody.” 1 Esp., at 431, 170 Eng. Rep., at 409.
   To be sure, the mere-touch rule was particularly well doc-
umented in cases involving the execution of civil process.
An officer pursuing a debtor could not forcibly enter the
debtor’s home unless the debtor had escaped arrest, such as
by fleeing after being touched. See Semayne’s Case, 5 Co.
Rep. 91a, 91b, 77 Eng. Rep. 194, 196 (K. B. 1604); see also
Miller v. United States, 357 U. S. 301, 307 (1958). Officers
seeking to execute criminal process, on the other hand, pos-
sessed greater pre-arrest authority to enter a felon’s home.
See Payton, 445 U. S., at 598. But the fact that the common
law rules of arrest generated more litigation in the civil con-
text proves only that creditors had ready recourse to the
courts to pursue escape actions for unsatisfactory arrests.
There is no reason to suspect that English jurists silently
adopted a special definition of arrest only for debt collec-
tion—indeed, they told us just the opposite. See supra, at
12. Nothing specific to debt collection elevated escape from
arrest into a justification for entry of the home. Whenever
14                    TORRES v. MADRID

                      Opinion of the Court

a person was “lawfully arrested for any Cause and after-
wards escape[d], and shelter[ed] himself in a House,” the
officer could break open the doors of the house. 2 W. Haw-
kins, Pleas of the Crown 87 (1721) (emphasis added).
   In any event, the officers and the dissent misapprehend
the history of the Fourth Amendment by minimizing the
role of practices in civil cases. “[A]rrests in civil suits were
still common in America” at the founding. Long v. Ansell,
293 U. S. 76, 83 (1934). And questions regarding the legal-
ity of an arrest “typically arose in civil damages actions for
trespass or false arrest.” Payton, 445 U. S., at 592. Accord-
ingly, this Court has not hesitated to rely on such decisions
when interpreting the Fourth Amendment. See, e.g.,
United States v. Jones, 565 U. S. 400, 404–405 (2012); Boyd
v. United States, 116 U. S. 616, 626 (1886). We see no rea-
son to break with our settled approach in this case.
                               B
   The officers and the dissent derive from our cases a dif-
ferent touchstone for the seizure of a person: “an intentional
acquisition of physical control.” Brower v. County of Inyo,
489 U. S. 593, 596 (1989). Under their alternative rule, the
use of force becomes a seizure “only when there is a govern-
mental termination of freedom of movement through means
intentionally applied.” Id., at 597 (emphasis deleted); see
Brief for Respondents 12–15; post, at 6–7.
   This approach improperly erases the distinction between
seizures by control and seizures by force. In all fairness, we
too have not always been attentive to this distinction when
a case did not implicate the issue. See, e.g., Brendlin v. Cal-
ifornia, 551 U. S. 249, 254 (2007). But each type of seizure
enjoys a separate common law pedigree that gives rise to a
separate rule. See Hodari D., 499 U. S., at 624–625; A. Cor-
nelius, The Law of Search and Seizure §47, pp. 163–164 (2d
ed. 1930) (contrasting actual control with “constructive de-
tention” by touching).
                   Cite as: 592 U. S. ____ (2021)             15

                       Opinion of the Court

    Unlike a seizure by force, a seizure by acquisition of con-
trol involves either voluntary submission to a show of au-
thority or the termination of freedom of movement. A prime
example of the latter comes from Brower, where the police
seized a driver when he crashed into their roadblock. 489
U. S., at 598–599; see also, e.g., Scott v. Harris, 550 U. S.
372, 385 (2007) (ramming car off road); Williams v. Jones,
Cas. t. Hard. 299, 301, 95 Eng. Rep. 193, 194 (K. B. 1736)
(locking person in room). Under the common law rules of
arrest, actual control is a necessary element for this type of
seizure. See Wilgus, Arrest Without a Warrant, 22 Mich.
L. Rev. 541, 553 (1924). Such a seizure requires that “a per-
son be stopped by the very instrumentality set in motion or
put in place in order to achieve that result.” Brower, 489
U. S., at 599. But that requirement of control or submission
never extended to seizures by force. See, e.g., Sandon, El.
Bl. & El., at 940–941, 120 Eng. Rep., at 760.
    As common law courts recognized, any such requirement
of control would be difficult to apply in cases involving the
application of force. See supra, at 7. At the most basic level,
it will often be unclear when an officer succeeds in gaining
control over a struggling suspect. Courts will puzzle over
whether an officer exercises control when he grabs a sus-
pect, when he tackles him, or only when he slaps on the
cuffs. Neither the officers nor the dissent explains how long
the control must be maintained—only for a moment, into
the squad car, or all the way to the station house. To cite
another example, counsel for the officers speculated that
the shooting would have been a seizure if Torres stopped
“maybe 50 feet” or “half a block” from the scene of the shoot-
ing to allow the officers to promptly acquire control. Tr. of
Oral Arg. 45. None of this squares with our recognition that
“ ‘[a] seizure is a single act, and not a continuous fact.’ ” Ho-
dari D., 499 U. S., at 625 (quoting Thompson v. Whitman,
18 Wall. 457, 471 (1874)). For centuries, the common law
16                   TORRES v. MADRID

                      Opinion of the Court

rule has avoided such line-drawing problems by clearly fix-
ing the moment of the seizure.
                               IV
   The dissent sees things differently. It insists that the
term “seizure” has always entailed a taking of possession,
whether the officer is seizing a person, a ship, or a promis-
sory note. See post, at 6–7. But the facts of the cases and
the language of the opinions confirm that the concept of pos-
session included the “constructive detention” of persons
“never actually brought within the physical control of the
party making an arrest.” Wilgus, 22 Mich. L. Rev., at 556
(emphasis deleted); see, e.g., Nicholl, 2 Y. & J., at 404, 148
Eng. Rep., at 976 (explaining that the “slightest touch” can
constitute “custody”); Anonymus, 1 Vent., at 306, 86 Eng.
Rep., at 197 (describing a touch as a “taking” of a person).
Even the dissent acknowledges that a touch can establish a
form of constructive possession. See post, at 20.
   The dissent says that “common law courts never contem-
plated” that the touching itself could effect a seizure. Post,
at 18. But one need only look at the many decisions adopt-
ing that definition of arrest. See supra, at 5–8, 12–13. The
dissent can offer no case expressing doubt about the rule
that the touching constitutes an arrest, much less refusing
to apply that rule in any context—felon or debtor. And we
have, as noted, definitively stated that “the arrest of a per-
son is quintessentially a seizure.” Payton, 445 U. S., at 585
(internal quotation marks omitted). The dissent’s attempt
to ignore arrests it appraises as “unfortunate” or “peculiar,”
post, at 15, 16, pays insufficient regard to the complete his-
tory underlying the Fourth Amendment.
   The dissent argues that we advance a “schizophrenic
reading of the word ‘seizure.’ ” Post, at 7. But our cases
demonstrate the unremarkable proposition that the nature
of a seizure can depend on the nature of the object being
seized. It is not surprising that the concept of constructive
                  Cite as: 592 U. S. ____ (2021)             17

                      Opinion of the Court

detention or the mere-touch rule developed in the context
of seizures of a person—capable of fleeing and with an in-
terest in doing so—rather than seizures of “houses, papers,
and effects.”
   The dissent also criticizes us for “posit[ing] penumbras”
of “privacy” and “personal security” in our analysis of the
Fourth Amendment. Post, at 24. But the text of the Fourth
Amendment expressly guarantees the “right of the people
to be secure in their persons,” and our earliest precedents
recognized privacy as the “essence” of the Amendment—not
some penumbral emanation. Boyd, 116 U. S., at 630. We
have relied on that understanding in construing the mean-
ing of the Amendment. See, e.g., Riley v. California, 573
U. S. 373, 403 (2014).
   The dissent speculates that the real reason for today’s de-
cision is an “impulse” to provide relief to Torres, post, at 23,
or maybe a desire “to make life easier for ourselves,” post,
at 22. It may even be, says the dissent, that the Court “at
least hopes to be seen as trying” to achieve particular goals.
Post, at 25. There is no call for such surmise. At the end of
the day we simply agree with the analysis of the common
law of arrest and its relation to the Fourth Amendment set
forth thirty years ago by Justice Scalia, joined by six of his
colleagues, rather than the competing view urged by the
dissent today.
                         *    *     *
  We hold that the application of physical force to the body
of a person with intent to restrain is a seizure even if the
person does not submit and is not subdued. Of course, a
seizure is just the first step in the analysis. The Fourth
Amendment does not forbid all or even most seizures—only
unreasonable ones. All we decide today is that the officers
seized Torres by shooting her with intent to restrain her
movement. We leave open on remand any questions re-
garding the reasonableness of the seizure, the damages
18                    TORRES v. MADRID

                      Opinion of the Court

caused by the seizure, and the officers’ entitlement to qual-
ified immunity.
   The judgment of the Court of Appeals is vacated, and the
case is remanded for further proceedings consistent with
this opinion.
                                              It is so ordered.

   JUSTICE BARRETT took no part in the consideration or de-
cision of this case.
                  Cite as: 592 U. S. ____ (2021)            1

                     GORSUCH, J., dissenting

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 19–292
                          _________________


          ROXANNE TORRES, PETITIONER v.
              JANICE MADRID, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE TENTH CIRCUIT
                        [March 25, 2021]

   JUSTICE GORSUCH, with whom JUSTICE THOMAS and
JUSTICE ALITO join, dissenting.
   The majority holds that a criminal suspect can be simul-
taneously seized and roaming at large. On the majority’s
account, a Fourth Amendment “seizure” takes place when-
ever an officer “merely touches” a suspect. It’s a seizure
even if the suspect refuses to stop, evades capture, and rides
off into the sunset never to be seen again. That view is as
mistaken as it is novel.
   Until today, a Fourth Amendment “seizure” has required
taking possession of someone or something. To reach its
contrary judgment, the majority must conflate a seizure
with its attempt and confuse an arrest with a battery. In
the process, too, the majority must disregard the Constitu-
tion’s original and ordinary meaning, dispense with our
conventional interpretive rules, and bypass the main cur-
rents of the common law. Unable to rely on any of these
traditional sources of authority, the majority is left to lean
on (really, repurpose) an abusive and long-abandoned Eng-
lish debt-collection practice. But there is a reason why, in
two centuries filled with litigation over the Fourth Amend-
ment’s meaning, this Court has never before adopted the
majority’s definition of a “seizure.” Neither the Constitu-
tion nor common sense can sustain it.
2                    TORRES v. MADRID

                    GORSUCH, J., dissenting

                              I
                              A
   This case began when two Albuquerque police officers ap-
proached Roxanne Torres on foot. The officers thought
Ms. Torres was the subject of an arrest warrant and sus-
pected of involvement in murder and drug trafficking. As
it turned out, they had the wrong person; Ms. Torres was
the subject of a different arrest warrant. As she saw the
officers walk toward her, Ms. Torres responded by getting
into her car and hitting the gas. At the time, Ms. Torres
admits, she was “tripping out bad” on methamphetamine.
Fearing the oncoming car was about to hit them, the officers
fired their duty weapons, and two bullets struck Ms. Torres
while others hit her car.
   None of that stopped Ms. Torres. She continued driv-
ing—over a curb, across some landscaping, and into a
street, eventually colliding with another vehicle. Abandon-
ing her car, she promptly stole a different one parked
nearby. Ms. Torres then drove over 75 miles to another city.
When she eventually sought medical treatment, doctors de-
cided she needed to be airlifted back to Albuquerque for
more intensive care. Only at that point, a day after her en-
counter with the officers, was Ms. Torres finally identified
and arrested. Ultimately, she pleaded no contest to assault
on a police officer, aggravated fleeing from an officer, and
the unlawful taking of a motor vehicle.
   More than two years later, Ms. Torres sued the officers
for damages in federal court under 42 U. S. C. §1983. She
alleged that they had violated the Fourth Amendment by
unreasonably “seizing” her. After discovery, the officers
moved for summary judgment. The district court granted
the motion, and the court of appeals affirmed. Individuals
like Ms. Torres are free to sue officers under New Mexico
state law for assault or battery. They may also sue officers
under the Fourteenth Amendment for conduct that “shocks
the conscience.” But under longstanding circuit precedent,
                   Cite as: 592 U. S. ____ (2021)              3

                      GORSUCH, J., dissenting

the courts explained, a Fourth Amendment “seizure” occurs
only when the government obtains “physical control” over a
person or object. Because Ms. Torres “managed to elude the
police for at least a full day after being shot,” the courts rea-
soned, the officers’ bullets had not “seized” her; any seizure
took place only when she was finally arrested back in Albu-
querque the following day. Torres v. Madrid, 769 Fed.
Appx. 654, 657 (CA10 2019).
                               B
   Now before us, Ms. Torres argues that this Court’s deci-
sion in California v. Hodari D., 499 U. S. 621 (1991), “com-
pel[s] reversal.” Brief for Petitioner 25. As she reads it,
Hodari D. held that a Fourth Amendment seizure takes
place whenever an officer shoots or even “mere[ly]
touch[es]” an individual with the intent to restrain. Brief
for Petitioner 15.
   Whatever one thinks of Ms. Torres’s argument, one thing
is certain: Hodari D. has generated considerable confusion.
There, officers chased a suspect on foot. 499 U. S., at 623.
Later, the suspect argued that he was “seized” for purposes
of the Fourth Amendment the moment the chase began.
See id., at 625. Though he fled, the suspect argued, a “rea-
sonable person” would not have felt at liberty given the of-
ficers’ “show of authority,” so a Fourth Amendment seizure
had occurred. Id., at 627–628.
   The Court rejected this argument. In doing so, it ex-
plained that, “[f]rom the time of the founding to the present,
the word ‘seizure’ has meant a ‘taking possession.’ ” Id., at
624. Because the defendant did not submit to the officers’
show of authority, the Court reasoned, the officers’ conduct
amounted at most to an attempted seizure. See id., at 626,
and n. 2. And “neither usage nor common-law tradition
makes an attempted seizure a seizure.” Ibid.
   At the same time, and as Ms. Torres emphasizes, the
4                     TORRES v. MADRID

                     GORSUCH, J., dissenting

Court didn’t end its discussion there. It proceeded to imag-
ine a different and hypothetical case, one in which the offic-
ers not only chased the suspect but also “appl[ied] physical
force” to him. In these circumstances, the Court suggested,
“merely touching” a suspect, even when officers fail to gain
possession, might qualify as a seizure. Id., at 624–625.
   Unsurprisingly, these dueling passages in Hodari D. led
to a circuit split. For the first time, some lower courts began
holding that a “mere touch” constitutes a Fourth Amend-
ment “seizure.” Others, however, continued to adhere to
the view, taken “[f]rom the time of the founding to the pre-
sent,” that the word “seizure” means “taking possession.”
Id., at 624 (internal quotation marks omitted). We took this
case to sort out the confusion.
                               II
   As an initial matter, Ms. Torres is mistaken that Hodari
D.’s discussion of “mere touch” seizures compels a ruling in
her favor. Under the doctrine of stare decisis, we normally
afford prior holdings of this Court considerable respect.
But, in the course of issuing their holdings, judges some-
times include a “witty opening paragraph, the background
information on how the law developed,” or “digressions
speculating on how similar hypothetical cases might be re-
solved.” B. Garner et al., The Law of Judicial Precedent 44
(2016). Such asides are dicta. The label is hardly an epi-
thet: “Dicta may afford litigants the benefit of a fuller un-
derstanding of the court’s decisional path or related areas
of concern.” Id., at 65. Dicta can also “be a source of advice
to successors.” Ibid. But whatever utility it may have, dicta
cannot bind future courts.
   This ancient rule serves important purposes. A passage
unnecessary to the outcome may not be fully considered.
Parties with little at stake in a hypothetical question may
afford it little or no adversarial testing. And, of course, fed-
eral courts possess no authority to issue rulings beyond the
                  Cite as: 592 U. S. ____ (2021)              5

                     GORSUCH, J., dissenting

cases and controversies before them. If the respect we af-
ford past holdings under the doctrine of stare decisis may
be justified in part as an act of judicial humility, respecting
that doctrine’s limits must be too. Fewer things could be
less humble than insisting our every passing surmise con-
stitutes a rule forever binding a Nation of over 300 million
people. No judge can see around every corner, predict the
future, or fairly resolve matters not at issue. See, e.g., Co-
hens v. Virginia, 6 Wheat. 264, 399–400 (1821); Central Va.
Community College v. Katz, 546 U. S. 356, 363 (2006).
   On any account, the passage in Hodari D. Ms. Torres
seeks to invoke was dicta. The only question presented in
that case was whether officers seize a defendant by a show
of authority without touching him. The Court answered
that question in the negative. The separate question
whether a “mere touch” also qualifies as a seizure was not
presented by facts of the case. No party briefed the issue.
And the opinion offered the matter only shallow considera-
tion, resting on just three sources: A state court opinion
from the 1860s, a “comment” in the 1934 Restatement of
Torts, and a 1930s legal treatise. See 499 U. S., at 624–625.
   Already some lower courts, including those below, have
recognized that Hodari D.’s aside does not constitute a
binding holding. See Brooks v. Gaenzle, 614 F. 3d 1213,
1220–1221 (CA10 2010); Henson v. United States, 55 A. 3d
859, 864–865 (D. C. 2012). Today’s majority seems to ac-
cept the point too. It acknowledges that Hodari D. “princi-
pally concerned a show of authority.” Ante, at 4. And it
says it intends to rule for Ms. Torres “independently” of Ho-
dari D. Ante, at 4.
                                III
  Seeking to carry that burden, the majority picks up where
Hodari D.’s dicta left off. It contends that an officer “seizes”
a person by merely touching him with an “intent to re-
strain.” Ante, at 9. We are told that a touch is a seizure
6                           TORRES v. MADRID

                          GORSUCH, J., dissenting

even if the suspect never stops or slows down; it’s a seizure
even if he evades capture. In all the years before Hodari
D.’s dicta, this conclusion would have sounded more than a
little improbable to most lawyers and judges—as it should
still today. A mere touch may be a battery. It may even be
part of an attempted seizure. But the Fourth Amendment’s
text, its history, and our precedent all confirm that “seizing”
something doesn’t mean touching it; it means taking pos-
session.
                              A
    Start with the text. The Fourth Amendment guarantees
that “[t]he right of the people to be secure in their persons,
houses, papers, and effects, against unreasonable searches
and seizures, shall not be violated.” As at least part of Ho-
dari D. recognized, “[f ]rom the time of the founding to the
present,” the key term here—“seizure”—has always meant
“ ‘taking possession.’ ” 499 U. S., at 624.
    Countless contemporary dictionaries define a “seizure” or
the act of “seizing” in terms of possession.1 This Court’s
early cases reflect the same understanding. Just sixteen
——————
   1 N. Bailey, Universal Etymological English Dictionary (22 ed. 1770)

(To seize is “to take into Custody or Possession by Force, or wrongfully;
to distrain, to attack, to lay hold of, or catch”; a seizure is a “seizing, tak-
ing into Custody”); T. Dyche & W. Pardon, A New General English Dic-
tionary (14th ed. 1771) (To seize is “to lay or take hold of violently or at
unawares, wrongfully, or by force”; a seizing or seizure is “a taking pos-
session of any thing by violent, force, &c”); 2 S. Johnson, A Dictionary of
the English Language (6th ed. 1785) (To seize is “1. To take hold of; to
gripe; to grasp.” “2. To take possession of by force.” “3. To take possession
of; to lay hold on; to invade suddenly.” “4. To take forcible possession of
by law.” “5. To make possessed; to put in possession of.” A seizure is “1.
The act of seizing.” “2. The thing seized.” “3. The act of taking forcible
possession.” “4. Gripe; possession.” “5. Catch”); 2 J. Ash, The New and
Complete Dictionary of the English Language (2d ed. 1795) (To seize is
“[t]o grasp, to lay hold on, to fasten on, to take possession of, to take pos-
session by law”; a seizure is “[t]he act of seizing, a gripe, a catch; the act
of taking possession by force of law; the thing seized, the thing pos-
sessed”).
                  Cite as: 592 U. S. ____ (2021)             7

                     GORSUCH, J., dissenting

years after the Fourth Amendment’s adoption, Congress
passed a statute regulating the “seizure” of ships. See The
Josefa Segunda, 10 Wheat. 312, 322 (1825). This Court in-
terpreted the term to require “an open, visible possession
claimed,” so that those previously possessing the ship “un-
derstand that they are dispossessed, and that they are no
longer at liberty to exercise any dominion on board of the
ship.” Id., at 325. Nor did the Court’s view change over
time. In Pelham v. Rose, 9 Wall. 103, 106 (1870), the Court
likewise explained that “[t]o effect [a] seizure” of something,
one needed “to take” the thing “into his actual custody and
control.” Id., at 107.
   Today’s majority disputes none of this. It accepts that a
seizure of the inanimate objects mentioned in the Fourth
Amendment (houses, papers, and effects) requires posses-
sion. Ante, at 4. And when it comes to persons, the majority
agrees (as Hodari D. held) that a seizure in response to a
“show of authority” takes place if and when the suspect sub-
mits to an officer’s possession. Ante, at 15. The majority
insists that a different rule should apply only in cases
where an officer “touches” the suspect. Here—and here
alone—possession is not required. So, under the majority’s
logic, we are quite literally asked to believe the officers in
this case “seized” Ms. Torres’s person, but not her car, when
they shot both and both continued speeding down the
highway.
   The majority’s need to resort to such a schizophrenic
reading of the word “seizure” should be a signal that some-
thing has gone seriously wrong. The Fourth Amendment’s
Search and Seizure Clause uses the word “seizures” once in
connection with four objects (persons, houses, papers, and
effects). The text thus suggests parity, not disparity, in
meaning. It is close to canon that when a provision uses the
same word multiple times, courts must give it the same
meaning each time. Ratzlaf v. United States, 510 U. S. 135,
143 (1994). And it is canonical that courts cannot give a
8                    TORRES v. MADRID

                    GORSUCH, J., dissenting

single word different meanings depending on the happen-
stance of “which object it is modifying.” Reno v. Bossier Par-
ish School Bd., 528 U. S. 320, 329 (2000) (“[W]e refuse to
adopt a construction that would attribute different mean-
ings to the same phrase in the same sentence, depending on
which object it is modifying”). To “[a]scrib[e] various mean-
ings” to a single word, we have observed, is to “render mean-
ing so malleable” that written laws risk “becom[ing] suscep-
tible to individuated interpretation.” Ratzlaf, 510 U. S., at
143 (internal quotation marks omitted). The majority’s con-
clusion that a single use of the word “seizures” bears two
different meanings at the same time—indeed, in this very
case—is truly novel. And when it comes to construing the
Constitution, that kind of innovation is no virtue.
   If more textual evidence were needed, the Fourth Amend-
ment’s neighboring Warrant Clause would seem to provide
it. That Clause states that warrants must describe “the
persons or things to be seized.” Once more, the Amendment
uses the same verb—“seized”—for both persons and objects.
Once more, it suggests parity, not some hidden divergence
between people and their possessions. Nor does anyone dis-
pute that a warrant for the “seizure” of a person means a
warrant authorizing officers to take that person into their
possession.
   Against all these adverse textual clues, the majority of-
fers little in reply. It admits that its interpretation defies
this Court’s teachings in Ratzlaf and Reno by ascribing dif-
ferent meanings to the word “seizure” depending on “the ob-
ject being seized.” Ante, at 16. It says only that we should
overlook the problem because “our cases” in the Fourth
Amendment context compel this remarkable construction.
Ibid. But it is unclear what cases the majority might have
in mind for it cites none.
   Instead, the majority proceeds to reason that the word
“seizure” must carry a different meaning for persons and
objects because persons alone are “capable of fleeing” and
                      Cite as: 592 U. S. ____ (2021)                      9

                         GORSUCH, J., dissenting

have “an interest in doing so.” Ibid. But that reasoning
faces trouble even from Hodari D., which explained that “[a]
ship still fleeing, even though under attack, would not be
considered to have been seized as a war prize.” 499 U. S.,
at 624. Of course, as the majority observes, persons alone
can possess “an interest” in fleeing. But, as Hodari D.’s ex-
ample shows, they can have as much (or more) interest in
fleeing to prevent the seizure of their possessions as they do
their persons. Even today, a suspect driving a car loaded
with illegal drugs may be more interested in fleeing to avoid
the loss of her valuable cargo than to prevent her own de-
tention. Yet the majority offers no reasoned explanation
why the meaning of the word “seizure” changes when offic-
ers hit the suspect and when they hit her drugs and car as
all three speed away.
   Unable to muster any precedent or sound reason for its
reading, the majority finishes its textual analysis with a se-
lective snippet from Webster’s Dictionary and a hypothet-
ical about a purse snatching. The majority notes that Web-
ster equated a seizure with “ ‘the act of taking by warrant’ ”
or “ ‘laying hold on suddenly.’ ” Ante, at 4. But Webster used
the warrant definition to describe “the seizure of contra-
band goods”—a seizure the majority agrees requires posses-
sion. Meanwhile, the phrase “laying hold on” a person con-
notes physical possession, as a look at the dictionary’s
entire definition demonstrates. A “seizure,” Webster con-
tinued, is the “act of taking possession by force,” the “act of
taking by warrant,” “possession,” and “a catching.”2 Read
——————
  2 2 N. Webster, An American Dictionary of the English Language 67

(1828) (To seize is “1. To fall or rush upon suddenly and lay hold on; or
to gripe or grasp suddenly.” “2. To take possession by force, with or with-
out right.” “3. To invade suddenly; to take hold of; to come upon suddenly;
as, a fever seizes a patient.” “4. To take possession by virtue of a warrant
or legal authority.” To be seized is to be “[s]uddenly caught or grasped;
taken by force; invaded suddenly; taken possession of; fastened with a
cord; having possession.” A seizure is “1. The act of seizing; the act of
laying hold on suddenly; as the seizure of a thief. 2. The act of taking
10                        TORRES v. MADRID

                         GORSUCH, J., dissenting

in full, Webster thus lends no support to the majority’s
view.
   The purse hypothetical, borrowed from Hodari D.’s dicta,
turns out to be even less illuminating. It supposes that “an
ordinary user of the English language could remark: ‘She
seized the purse-snatcher, but he broke out of her grasp.’ ”
Ante, at 5 (quoting Hodari D., 499 U. S., at 626). But what
does that prove? The hypothetical contemplates a woman
who takes possession of the purse-snatcher, establishing a
“grasp” for him to “break out of.” One doesn’t “break out of ”
a mere touch.
   Really, the majority’s answer to the Constitution’s text is
to ignore it. The majority stands mute before the consensus
among founding-era dictionaries, this Court’s early cases
interpreting the word “seizure,” and the Warrant Clause.
It admits its interpretation spurns the canonical interpre-
tive principle that a single word in a legal text does not
change its meaning depending on what object it modifies.
All we’re offered is a curated snippet and an unhelpful hy-
pothetical. Ultimately, it’s hard not to wonder whether the
majority says so little about the Constitution’s terms be-
cause so little can be said that might support its ruling.
                             B
  Rather than focus on text, the majority turns quickly to
history. At common law, it insists, a “linkage” existed be-
tween the “seizure” of a person and the concept of an “ar-
rest.” Ante, at 5. Thus, the majority contends, we must
examine how the common law defined that term. But fol-
lowing the majority down this path only leads to another
dead end. Unsurprisingly, an “arrest” at common law ordi-
narily required possession too.
——————
possession by force; as the seizure of lands or goods; the seizure of a town
by an enemy; the seizure of a throne by an usurper. 3. The act of taking
by warrant; as the seizure of contraband goods. 4. The thing taken or
seized.” “5. Gripe; grasp; possession.” “6. Catch; a catching”).
                      Cite as: 592 U. S. ____ (2021)                       11

                          GORSUCH, J., dissenting

                              1
  Consider what some of our usual common law guides say
on the subject. Blackstone defined “an arrest” in the crim-
inal context as “the apprehending or restraining of one’s
person, in order to be forthcoming to answer an alleged or
suspected crime.” 4 Commentaries on the Laws of England
286 (1769). Hale and Hawkins both equated an “arrest”
with “apprehending,” “taking,” and “detain[ing]” a person.
See 1 M. Hale, Pleas of the Crown 89, 93–94 (5th ed. 1716);
2 W. Hawkins, Pleas of the Crown 74–75, 77, 80–81, 86 (3d
ed. 1739). And Hawkins stated that an arrest required the
officer to “actually have” the suspect “in his Custody.” Id.,
at 129. Any number of historical dictionaries attest to a
similar understanding—defining an “arrest” as a “stop,” a
“taking of a person,” and the act “by which a man becomes
a prisoner.”3
  Common law causes of action point to the same common-
sense conclusion. During the founding era, an individual
who was unlawfully arrested could seek redress through
the tort of false imprisonment. See 3 W. Blackstone, Com-
mentaries on the Laws of England 127 (1768); see also Pay-
ton v. New York, 445 U. S. 573, 592 (1980); Wallace v. Kato,

——————
   3 See, e.g., Bailey, Universal Etymological English Dictionary (To ar-

rest is “to stop or stay”; an arrest (in the legal sense) is “a Legal taking
of a Person, and restraining him from Liberty”); Dyche & Pardon, A New
General English Dictionary (An arrest is “the stopping or detaining a
person, by a legal process”); 1 Johnson, A Dictionary of the English Lan-
guage (“1. In law. A stop or stay; as, a man apprehended for debt, is said
to be arrested.” “An arrest is a certain restraint of a man’s person, de-
priving him of his own will, and binding it to become obedient to the will
of the law, and may be called the beginning of imprisonment.” “2. Any
caption, seizure of the person.” “3. A stop” (emphasis deleted)); 1 Ash,
The New and Complete Dictionary of the English Language (To arrest is
“[t]o seize a man for debt, to apprehend by virtue of a writ from any court
of justice, to stop, to hinder”; an arrest is “[t]he act of seizing on a man’s
person for debt, the execution of a writ from any court of justice by which
a man becomes a prisoner, a stop, a hindrance”).
12                    TORRES v. MADRID

                     GORSUCH, J., dissenting

549 U. S. 384, 388–389 (2007) (describing “false arrest and
false imprisonment” as the “closest analogy” to an arrest
without probable cause). That cause of action aimed to rem-
edy “the violation of the right of personal liberty,” 3 Black-
stone, supra, at 127, which was “the power of loco-motion,
of changing situation, or removing one’s person to whatso-
ever place one’s own inclination may direct,” 1 W. Black-
stone, Commentaries on the Laws of England 130 (1765).
Thus, false imprisonment—the violation of the right to
move where one desired—required proof of “[t]he detention
of the person” and “[t]he unlawfulness of such detention.” 3
Blackstone, supra, at 127. That detention could occur “in a
gaol, house, stocks, or in the street,” but it occurred only if
a person was “under the custody of another.” 1 E. East,
Pleas of the Crown 428 (1806) (emphasis added).
   Much the same held true in another related field. At com-
mon law, an officer could be held criminally liable for allow-
ing an individual to escape after being arrested. And to
prove the existence of an arrest in an “Indictment for an
Escape,” a prosecutor had to “expressly shew” that “the
Party was actually in the Defendant’s Custody for a Crime,
Action, or Commitment for it.” 2 Hawkins, supra, at 132
(emphasis added). In other words, to demonstrate an ar-
rest, a prosecutor had to prove the suspect had been “a Pris-
oner in [the officer’s] Custody.” 1 Hale, supra, at 112 (em-
phasis added). Here, too, an arrest required possession.
   Once more, the majority’s primary answer to all this
countervailing evidence is to ignore it. And once more, the
majority’s own sources do more to hurt than help its cause.
Lifting a line from Simpson v. Hill, 1 Esp. 431, 170 Eng.
Rep. 409 (N. P. 1795), the majority suggests that the tort of
false imprisonment at common law required no more than
a “tapping on the shoulder.” Ante, at 13 (citing 1 Esp., at
431–432, 170 Eng. Rep., at 409). But Simpson could not
have stated the possession requirement more plainly:
“[W]ithout any taking possession of the person,” there “is
                  Cite as: 592 U. S. ____ (2021)             13

                     GORSUCH, J., dissenting

not, by law, a false imprisonment.” Id., at 432, 170 Eng.
Rep., at 409 (emphasis added). And the court proceeded to
reject the plaintiff ’s claim for false imprisonment because
the “constable did never take her into custody.” Ibid. (em-
phasis added). The majority offers no case finding the ele-
ments of false imprisonment satisfied by the mere touch of
a fleeing person.
   What remains of the majority’s response follows the same
course. The majority asserts that claims for escape only re-
quired proof that the officer touched a suspect. Ante, at 12.
But to prove its point, the majority quotes a sentence from
Hale stating that no liability for escape exists “ ‘if the felon
were not once in the hands of an officer.’ ” Ibid. (quoting 2
Pleas of the Crown 93 (1736)). And as Hale proceeded to
make plain, a felon “in the hands of an officer” was another
way of saying the officer had “apprehended” or “taken” the
felon into his “custody.” See id., at 89, 93–94 (5th ed. 1716).
   Ultimately, the majority seeks to invoke Samuel John-
son’s dictionary and Payton, 445 U. S., at 585, to confirm
only the anodyne point that some sort of “linkage” existed
at common law between the concepts of “arrests” and “sei-
zures.” Ante, at 5. Yet, even here it turns out there is more
to the story. The majority neglects to mention that Johnson
proceeded to define an “arrest” as a “caption” of the person,
“a stop or stay,” a “restraint of a man’s person, depriving
him of his own will,” and “the beginning of imprisonment.”
1 S. Johnson, A Dictionary of the English Language (6th ed.
1785). “To arrest,” Johnson said, was “[t]o seize,” “to detain
by power,” “[t]o withhold; to hinder,” and “[t]o stop motion.”
Ibid. Meanwhile, the sentence fragment the majority
quotes from Payton turns out to have originated in Justice
Powell’s concurrence in United States v. Watson, 423 U. S.
411, 428 (1976). And looking to that sentence in full, it is
plain Justice Powell, too, understood an arrest not as a
touching, but as “the taking hold of one’s person.” Ibid.
14                   TORRES v. MADRID

                    GORSUCH, J., dissenting

Thus, even the majority’s best sources only wind up point-
ing us back to the traditional possession rule.
                                2
   Unable to identify anything helpful in the main current
of the common law, the majority is forced to retreat to an
obscure eddy. Starting from Hodari D.’s three references to
“mere touch” arrests, the majority traces these authorities
back to their English origins. The tale that unfolds is a cu-
rious one.
   Before bankruptcy reforms in the 19th century, creditors
seeking to induce repayment of their loans could employ
bailiffs to civilly arrest delinquent debtors and haul them
off to debtors prison. See Cohen, The History of Imprison-
ment for Debt and Its Relation to the Development of Dis-
charge in Bankruptcy, 3 J. Legal Hist. 153, 154–155 (1982).
But the common law also offered debtors some tools to avoid
or delay that fate. Relevant here, the common law treated
the home as a “castle of defence and asylum” so no bailiff
could break into a debtor’s home to effect a civil arrest. 3
Blackstone, supra, at 288; see also Treiman, Escaping the
Creditor in the Middle Ages, 43 L. Q. Rev. 230, 233 (1927).
Over time, the practice of “keeping house” became an in-
creasingly popular way for debtors to evade the bailiff. Id.,
at 234. Naturally, too, creditors railed against this “notori-
ous” practice. See ibid. And eventually Parliament re-
sponded to their clamor. The English bankruptcy statutes
of 1542 and 1570 imposed serious penalties on debtors who
“kept house” to avoid imprisonment. Cohen, supra, at 157.
   It was seemingly against this backdrop that the strange
cases Hodari D.’s dicta briefly alluded to and the majority
has now dug up began to appear. Under their terms, a bail-
iff who could manage to touch a person hiding in his home,
often through an open window or door, was deemed to have
effected a civil “arrest.” See Genner v. Sparks, 6 Mod. 173,
87 Eng. Rep. 928 (K. B. 1704). And because this mere touch
                  Cite as: 592 U. S. ____ (2021)            15

                     GORSUCH, J., dissenting

was deemed an “arrest,” the bailiff was then permitted by
law to proceed to “br[eak] the house . . . to seize upon” the
person and render him to prison. Ibid., 87 Eng. Rep., at
929. Of course it was farcical to call a tap through an open
window an “arrest.” But it proved a useful farce, at least
for creditors.
  One of the majority’s lead cases, Sandon v. Jervis, El. Bl.
& El. 935, 120 Eng. Rep. 758 (K. B. 1858), illustrates the
absurdity of it all. There, a bailiff tried and failed “on sev-
eral occasions” to arrest a debtor. Id., at 936, 120 Eng. Rep.,
at 758. Eventually, the bailiff spotted an open window on
“an upper story,” so he ordered an assistant to fetch a lad-
der. Ibid. But the debtor and his daughter noticed the ploy
and “ran to the window,” slamming it closed. Ibid. Unfor-
tunately, in the excitement a window pane broke. Seeing
the opportunity, the bailiff ’s assistant, while perched atop
the ladder, thrust his hand through the opening and man-
aged to touch the debtor. Id., at 936–937, 120 Eng. Rep., at
758. According to the court, this “arrest” was sufficient to
justify the bailiff ’s later forcible entry into the home. Id.,
at 946–948, 120 Eng. Rep., at 762–763.
  By everyone’s account, however, the farce extended only
so far. Yes, the mere-touch arrest was a feature of civil
bankruptcy practice for an unfortunate period. But the ma-
jority has not identified a single founding-era case extend-
ing the mere-touch arrest rule to the criminal context. The
majority points to two nineteenth-century treatises, but
both reference only a case about a debt-collection arrest.
See ante, at 11–12 (citing 1 J. Backus, A Digest of Laws Re-
lating to the Offices and Duties of Sheriff, Coroner and Con-
stable 115–116, n. (c) (1812) (citing Genner v. Sparks, 6
Mod. 173, 87 Eng. Rep. 928 (K. B. 1704)), and 1 R. Burn,
The Justice of the Peace 275 (28th ed. 1837) (citing the
same)). The majority nods to dicta from an 1854 Delaware
state trial court, but that came long after the founding and
the majority does not explain how it sheds light on the
16                    TORRES v. MADRID

                     GORSUCH, J., dissenting

Fourth Amendment’s original meaning. See ante, at 12 (cit-
ing State v. Townsend, 5 Del. 487, 488)). And every remain-
ing early American case the majority cites for its “mere
touch” rule—from the founding through the Civil War—in-
volved only civil debt-collection arrests. See ante, at 4 (cit-
ing Whithead v. Keyes, 85 Mass. 495 (1862)); ante, at 6 (cit-
ing United States v. Benner, 24 F. Cas. 1084 (No. 14,568)
(CC ED Pa. 1830)); ante, at 6 (citing Butler v. Washburn, 25
N. H. 251 (1852) (tax collection)). The same goes for the
majority’s primary English authorities. See ante, at 7 (cit-
ing Nicholl v. Darley, 2 Y. & J. 399, 400, 148 Eng. Rep. 974
(Exch. 1828); Sandon, El. Bl. & El., at 940, 120 Eng. Rep.,
at 760)).
  So what relevance do these obscure and long-abandoned
civil debt-collection practices have for today’s case concern-
ing a criminal arrest and brought under the Fourth Amend-
ment? The answer seems to be not much, for at least three
reasons.
  In the first place, the Amendment speaks of “seizures,”
not “arrests.” To the extent the common law of arrests in-
forms the Amendment’s meaning, we have already seen
that an arrest normally meant taking possession of an ar-
restee. Maybe in one peculiar area, and for less than admi-
rable reasons, the common law deviated from this under-
standing. But this Court usually presumes that those who
wrote the Constitution used words in their ordinary sense,
not in some idiosyncratic way. See District of Columbia v.
Heller, 554 U. S. 570, 576 (2008). And today’s majority sup-
plies no evidence that anyone during the founding era un-
derstood the Fourth Amendment to adopt the specialized
definition of “arrest” from civil debt-collection practice.
  Second, even if we were to hypothesize that people did
understand the Fourth Amendment to incorporate this
quirky rule, what would that tell us? Here, the officers tried
to arrest Ms. Torres in a parking lot on behalf of the State
for serious crimes, not break into her home on behalf of the
                      Cite as: 592 U. S. ____ (2021)                     17

                         GORSUCH, J., dissenting

local credit union for missing a payment. So even if we were
willing to suppose that the founding generation understood
the Constitution to incorporate the majority’s civil debt-
collection arrest rule, nothing before us suggests they con-
templated, let alone endorsed, injecting it into the criminal
law and overriding settled doctrine equating arrests with
possession.
   Finally, even in the civil debt-collection context, the ma-
jority cannot point to even a single case suggesting that hit-
ting a suspect with an object—an arrow, a bullet, a cudgel,
anything—as she flees amounted to an arrest. Instead, the
majority’s cases hold only that the “laying of hands” on an
arrestee constituted an arrest. Ante, at 7. Thus, even if the
Fourth Amendment did transpose the “mere touch” rule
from the context of civil arrests into the criminal arena, it
still would not reach this case.
   How does the majority respond? Again, it does little more
than disregard the difficulties. The majority says there is
“no reason to suspect” the common law defined criminal ar-
rests of felons “any differently” than civil arrests of debtors.
Ante, at 13, 11. But the majority skips over all the evidence
canvassed above showing that a criminal arrest required
possession, not a mere touch. See Part III–B–1, supra. It
sails past its failure to identify any case holding that a mere
touch qualified as a criminal arrest. It ignores the fact
Blackstone defined criminal and civil arrests differently.4
And it claims to find support in Hawkins’s statement that
an officer could break into a house to capture an arrestee
——————
  4 The majority cites only Blackstone’s definition of a civil arrest, which

required a “corporal seising or touching the defendant’s body.” Ante, at
6 (quoting 3 W. Blackstone, Commentaries on the Laws of England 288
(1768)). But flipping from Blackstone’s third volume (discussing “private
wrongs”) to his fourth volume (discussing “public wrongs”) reveals—as
we have already seen but the majority fails to acknowledge—that Black-
stone equated a criminal arrest with “apprehending or restraining . . .
one’s person, in order to be forthcoming to answer an alleged or suspected
crime.” See supra, at 11.
18                   TORRES v. MADRID

                    GORSUCH, J., dissenting

who escaped after being “ ‘lawfully arrested for any Cause.’ ”
Ante, at 13–14 (quoting 2 Pleas of the Crown 87 (1721)).
Yet, the question before us isn’t what an officer might do
after making an arrest; it’s what constitutes an arrest in the
first place.
   Rather than confront shortcomings like these, the major-
ity asks us to glide past them. It suggests that importing
the mere-touch rule into the criminal context is permissible
because “no common law case” had occasion to reject that
idea expressly. See ante, at 16. But this gets things back-
wards. Today, for the first time, the majority seeks to
equate seizures and criminal arrests with mere touches, at-
tempted seizures, and batteries. It is for the majority to
show the Fourth Amendment commands this result. No
amount of rhetorical maneuvering can obscure how flat it
has fallen: Even its own authorities do more to undermine
than support its thesis. If common law courts never con-
templated the majority’s odd definition of a criminal ar-
rest—and this Court didn’t either for more than two centu-
ries—that can only be further proof of its implausibility.
   The majority asks us to glide past another problem too.
It acknowledges that its debt-collection cases required a
“laying on of hands” to complete an arrest. But it says we
should overlook that rule as an accident of antiquity.
“Touchings” by “firearm,” we are told, were unknown to
“founding-era courts,” and no “officer used a gun to appre-
hend a suspect” before 1850. Ante, at 9. Never mind the
shot heard round the world in 1775 and the adoption of the
Second Amendment. Never mind that as early as 1592,
when a bailiff “feared resistance” and thus “brought with
him” a gun “to arrest” someone, a common law court
deemed it lawful because “[t]he sheriff or any of his minis-
ters may for the better execution of justice carry with them
offensive or defensive weapons.” Seint John’s Case, 5 Co.
Rep. 71b, 77 Eng. Rep. 162, 162–163 (K. B. 1592). Never
mind that even tax collectors were carrying guns by the
                 Cite as: 592 U. S. ____ (2021)           19

                    GORSUCH, J., dissenting

1680s. E.g., Dickenson v. Watson, Jones, T. 205, 205–206,
84 Eng. Rep. 1218, 1218–1219 (K. B. 1682). And never
mind, too, that the majority’s problem isn’t limited to guns.
It fails to cite any case in which a touching by any weapon
was deemed sufficient to effect an arrest. Seemingly, the
majority would have us believe that bailiffs wielding any-
thing but their fists were beyond the framers’ imagination.
   Faced with all these problems, the majority tacks. It
scrambles to locate a case—any case—suggesting that com-
mon law courts considered “touchings” by weapon enough
to effect an arrest in the debt-collection context. Ulti-
mately, the majority asks us to dwell at length on the Coun-
tess of Rutland’s case. In at least that lone instance, the
majority promises, we will find bailiffs who arrested a
debtor by touching her with an object (a mace) rather than
a laying on of hands. See ante, at 7–8 (citing Countess of
Rutland’s Case, 6 Co. Rep. 52b, 54a, 77 Eng. Rep. 332 (Star
Chamber 1605)). But it turns out the dispute concerned
whether a countess could be civilly arrested at all, not when
or how the arrest was completed. The court had no reason
to (and did not) decide whether the bailiffs accomplished
their arrest when they “shewed her their mace,” “touch[ed]”
her with the mace, or “compelled the coachman to carry”
her to jail. Id., at 54a, 77 Eng. Rep., at 336. And no one
questions that these things together—a show of authority
followed by compelled detention—have always been enough
to complete an arrest. Not even minor royalty can rescue
the majority.
   So the majority tacks again. Now it asks us to dispense
with the common law’s “laying on of hands” requirement as
an “artificial” rule. Ante, at 8. Distinguishing between
“touchings” by hand and by weapon, it says, “calls to mind
the unavailing defense of the person who ‘persistently de-
nied that he had laid hands upon a priest, for he had only
cudgelled and kicked him.’ ” Ibid. But the quip exposes the
majority’s bind. To get where it wishes to go, the majority
20                        TORRES v. MADRID

                         GORSUCH, J., dissenting

not only must rework the rules found in the cases on which
it relies, it must also abandon their rationale. The debt-
collection cases treated the “laying on of hands” as a sign of
possession.5 Maybe the possession was more “constructive”
or even fictional than “actual.” See ante, at 16. But the idea
was that someone who stood next to a debtor and laid hands
on him could theoretically exercise a degree of control over
his person. Common law courts never said the same of bail-
iffs who fired arrows at debtors, shot them with firearms,
or cudgeled them as they ran away. Such conduct might
have amounted to a battery, but it was never deemed suffi-
cient to constitute an arrest. Doubtless that’s why when a
tax collector shot a man in the eye with a (supposedly una-
vailable) firearm in 1682, the man sued the officer for “as-
sault, battery, and wounding”—not false imprisonment.
See Dickenson, Jones, T., at 205, 84 Eng. Rep., at 1218–
1219.
   The majority implores us to study the common law his-
tory of arrests. But almost immediately, the majority real-
izes it cannot find what it seeks in the history of criminal
arrests. So it is forced to disinter a long-abandoned mere-
touch rule from civil bankruptcy practice. Then it must im-
port that rule into the criminal law. And because even that
isn’t enough to do the work it wishes done, the majority
must jettison both the laying on of hands requirement and
the rationale that sustained it. All of which leaves us con-

——————
  5 That is why the mere-touch cases often discussed the “corporal pos-

session of the debtor.” E.g., Sandon v. Jervis, El. Bl. & El. 935, 941–942,
120 Eng. Rep. 758 (K. B. 1858) (Hill, J.). A “corporal” touch was a legal
term of art and was frequently used in the context of determining the
possession of goods. E.g., Jordan v. James, 5 Ohio 88, 98 (1831) (stating
that an owner “may deliver any chattel he sells, symbolically and con-
structively, as well as by corporal touch”); see also 2 W. Blackstone, Com-
mentaries on the Laws 448–449, n. 16 (J. Chitty ed. 1826); Friedman,
Formative Elements in the Law of Sales: The Eighteenth Century, 44
Minn. L. Rev. 411, 445 (1960).
                  Cite as: 592 U. S. ____ (2021)           21

                     GORSUCH, J., dissenting

fusing seizures with their attempts and arrests with batter-
ies.
  The common law offers a vast legal library. Like any
other, it must be used thoughtfully. We have no business
wandering about and randomly grabbing volumes off the
shelf, plucking out passages we like, scratching out bits we
don’t, all before pasting our own new pastiche into the U. S.
Reports. That does not respect legal history; it rewrites it.
                                C
   If text and history pose challenges for the majority, so do
this Court’s precedents. The majority admits (as it must)
that the seizure of an object occurs only through taking pos-
session. Ante, at 4. The majority also admits (as it must)
that the seizure of a person through a “show of authority”
occurs only if the suspect submits to an officer’s possession.
Ante, at 15. But the majority fails to acknowledge that this
Court has also said the same principle governs the seizure
of persons effected through the use of force.
   In Terry v. Ohio, 392 U. S. 1 (1968), the Court explained
that “[o]nly when the officer, by means of physical force or
show of authority, has in some way restrained the liberty of
a citizen may we conclude that a ‘seizure’ has occurred.” Id.,
at 19, n. 16 (emphasis added). The restraint of liberty Terry
referred to was “interference” with a person’s “freedom of
movement.” United States v. Jacobsen, 466 U. S. 109, 113,
n. 5 (1984). As the Court put it in Brower v. County of Inyo,
489 U. S. 593 (1989), a decision issued just two years before
Hodari D.: “It is clear, in other words, that a Fourth Amend-
ment seizure” occurs “only when there is a governmental
termination of freedom of movement through means inten-
tionally applied.” 489 U. S., at 597 (emphasis deleted).
   Rather than follow these teachings, the majority dispar-
ages them. After highlighting (multiple times) that Justice
Scalia authored Hodari D.’s dicta, the majority turns about
22                    TORRES v. MADRID

                     GORSUCH, J., dissenting

and faults his opinion for the Court in Brower for “improp-
erly eras[ing] the distinction between seizures by control
and seizures by force.” Ante, at 14. The majority continues
on to blame other of our decisions, too, for “hav[ing] not al-
ways been attentive” to this supposedly fundamental dis-
tinction. Ibid. But this Court has not been “[in]attentive”
to a fundamental Fourth Amendment distinction for over
two centuries, let alone sought to “erase” it. In truth, the
majority’s “distinction” is a product of its own invention.
This Court has always recognized that how seizures take
place can differ. Some may take place after a show of au-
thority, others by the application of force, still others after
a polite request. But to be a “seizure,” the same result has
always been required: An officer must acquire possession.
                                IV
   If text, history, and precedent cannot explain today’s re-
sult, what can? The majority seems to offer a clue when it
promises its new rule will help us “avoi[d] . . . line-drawing
problems.” Ante, at 15–16 (internal quotation marks omit-
ted). Any different standard, the majority worries, would
be “difficult to apply.” Ante, at 15.
   But if efficiency in judicial administration is the explana-
tion, it is a troubling one. Surely our role as interpreters of
the Constitution isn’t to make life easier for ourselves. Cf.
Calabresi & Lawson, The Rule of Law as a Law of Law, 90
Notre Dame L. Rev. 483, 488 (2014). Nor, for that matter,
has the majority even tried to show that the traditional pos-
session rule—in use “[f]rom the time of the founding,” Ho-
dari D., 499 U. S., at 624—has proven unreasonably diffi-
cult to administer.        Everyone agrees, too, that the
possession rule will continue to govern when it comes to the
seizures of objects and persons through a show of authority.
So, rather than simplify things, the majority’s new rule for
“mere touch” seizures promises only to add another layer of
complexity to the law.
                  Cite as: 592 U. S. ____ (2021)           23

                     GORSUCH, J., dissenting

   Even within its field of operation, the majority’s rule
seems destined to underdeliver on its predicted efficiencies.
The majority tells us that its new test requires an “objective
intent to restrain.” Ante, at 10. But what qualifies is far
from clear. The majority assures us that a “tap on the
shoulder to get one’s attention will rarely exhibit such an
intent.” Ibid. Suppose, though, the circumstances “objec-
tively” indicate that the tap was “intended” to secure a per-
son’s attention for a minute, a quarter hour, or longer.
Would that be enough?
   Then there’s the question what kind of “touching” will
suffice. Imagine that, with an objective intent to detain a
suspect, officers deploy pepper spray that enters a suspect’s
lungs as he sprints away. Does the application of the pep-
per spray count? Suppose that, intending to capture a flee-
ing suspect, officers detonate flash-bang grenades that are
so loud they damage the suspect’s eardrum, even though he
manages to run off. Or imagine an officer shines a laser
into a suspect’s eyes to get him to stop, but the suspect is
able to drive away with now-damaged retinas. Are these
“touchings”? What about an officer’s bullet that shatters
the driver’s windshield, a piece of which cuts her as she
speeds away? Maybe the officer didn’t touch the suspect,
but he set in motion a series of events that yielded a touch-
ing. Does that count? While assuring us that its new rule
will prove easy to administer, the majority refuses to con-
front its certain complications. Lower courts and law en-
forcement won’t have that luxury.
   If efficiency cannot explain today’s decision, what’s left?
Maybe it is an impulse that individuals like Ms. Torres
should be able to sue for damages. Sometimes police shoot-
ings are justified, but other times they cry out for a remedy.
The majority seems to give voice to this sentiment when it
disparages the traditional possession rule as “artificial” and
promotes its alternative as more sensitive to “personal se-
curity” and “new” policing realities. Ante, at 8–9. It takes
24                    TORRES v. MADRID

                     GORSUCH, J., dissenting

pains to explain, too, that its new rule will provide greater
protection for personal “privacy” interests, which we’re told
make up the “essence” of the Fourth Amendment. Ante, at
16 (internal quotation marks omitted).
   But tasked only with applying the Constitution’s terms,
we have no authority to posit penumbras of “privacy” and
“personal security” and devise whatever rules we think
might best serve the Amendment’s “essence.” The Fourth
Amendment allows this Court to protect against specific
governmental actions—unreasonable searches and seizures
of persons, houses, papers, and effects—and that is the
limit of our license. Besides, it’s hard to see why we should
stretch to invent a new remedy here. Ms. Torres had ready-
made claims for assault and battery under New Mexico law
to test the officers’ actions. See N. M. Stat. Ann §41–4–12
(2020). The only reason this case comes before us under
§1983 and the Fourth Amendment rather than before a
New Mexico court under state tort law seems to be that Ms.
Torres (or her lawyers) missed the State’s two-year statu-
tory filing deadline. See Tr. of Oral Arg. 16–17; Brief for
Respondents 20, n. 4. That may be a misfortune for her,
but it is hardly a reason to upend a 230 year-old under-
standing of our Constitution.
   Nor, if we are honest, does today’s decision promise much
help to anyone else. Like Ms. Torres, many seeking to sue
officers will be able to bring state tort claims. Even for
those whose only recourse is a federal lawsuit, the major-
ity’s new rule seems likely to accomplish little. This Court
has already said that a remedy lies under §1983 and the
Fourteenth Amendment for police conduct that “shocks the
conscience.” County of Sacramento v. Lewis, 523 U. S. 833,
840, 845–847 (1998). At the same time, qualified immunity
poses a daunting hurdle for those seeking to recover for less
egregious police behavior. In our own case, Ms. Torres has
yet to clear that bar and still faces it on remand. So, at the
end of it all, the majority’s new rule will help only those who
                   Cite as: 592 U. S. ____ (2021)             25

                      GORSUCH, J., dissenting

(1) lack a state-law remedy, (2) evade custody, (3) after
some physical contact by the police, (4) where the contact
was sufficient to show an objective intent to restrain, (5)
and where the police acted “unreasonably” in light of clearly
established law, (6) but the police conduct was not “con-
science shocking.” With qualification heaped on qualifica-
tion, that can describe only a vanishingly small number of
cases.
   Even if its holding offers little practical assistance to an-
yone, perhaps the majority at least hopes to be seen as try-
ing to vindicate “personal security” and the “essence” of
“privacy” when it derides the traditional possession rule as
“artificial.” But an attractive narrative cannot obscure the
hard truth. Not only does the majority’s “mere touch” rule
allow a new cause of action in exceedingly few cases (non-
conscience-shocking-but-still-unreasonable batteries in-
tended to result in possession that don’t achieve it). It sup-
plies no path to relief for otherwise identical near-misses
(assaults). A fleeing suspect briefly touched by pursuing
officers may have a claim. But a suspect who evades a hail
of bullets unscathed, or one who endures a series of flash-
bang grenades untouched, is out of luck. That distinction
is no less “artificial” than the one the law has recognized for
centuries. And the majority’s new rule promises such
scarce relief that it can hardly claim more sensitivity to
“personal security” than the rule the Constitution has long
enshrined.
   In the face of these concerns, the majority replies by deny-
ing their relevance. It says there is “no call” to “surmise”
that its decision rests on anything beyond an “analysis of
the common law of arrest.” Ante, at 17. But there is no
surmise about it. The majority itself tells us that its deci-
sion is also justified by the need to “avoi[d] . . . line-drawing
problems,” protect “personal security,” and advance the
“privacy” interests that form the “essence” of the Fourth
Amendment. Having invoked these sundry considerations,
26                    TORRES v. MADRID

                     GORSUCH, J., dissenting

it’s hard to see how the majority might disown them.
                                *
  To rule as it does, the majority must endow the term “sei-
zure” with two different meanings at the same time. It
must disregard the dominant rule of the common law. It
must disparage this Court’s existing case law for erasing
distinctions that never existed. It cannot even guarantee
that its new rule will offer great efficiencies or meaningfully
vindicate the penumbral promises it supposes. Instead, we
are asked to skip from one snippet to another, finally land-
ing on a long-abandoned debt-collection practice that must
be reengineered to do the work the majority wishes done.
Our final destination confuses a battery for a seizure and
an attempted seizure with its completion. All this is miles
from where the standard principles of interpretation lead
and just as far from the Constitution’s original meaning.
And for what? A new rule that may seem tempting at first
blush, but that offers those like Ms. Torres little more than
false hope in the end.
  Respectfully, I dissent.

```

---

## GROUP: _overhaul2/lake/cases/Townsend v. Sain.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Townsend v. Sain"
type: case
citation: "372 U.S. 293 (1963)"
parallel_cite: "83 S. Ct. 745; 9 L. Ed. 2d 770"
neutral_cite: 1963 U.S. LEXIS 1941
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1963
date_decided: 1963-03-18
docket: 8
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1963-03-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Townsend v. Sain
  varies_by_point: false
  scope_note: "Good law on the confession-voluntariness holding (a drug/'truth serum'-induced confession not the product of a free intellect is inadmissible). The separate federal-habeas evidentiary-hearing standard (the Townsend circumstances/deliberate-bypass) was abrogated by Keeney v. Tamayo-Reyes, 504 U.S. 1 (1992), and superseded by AEDPA, 28 U.S.C. §2254(e)(2)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106544/townsend-v-sain/"
  cluster_id: 106544
  opinion_id: 106544
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Rogers v. Richmond]]", "[[Beecher v. Alabama]]", "[[Lynumn v. Illinois]]", "[[Brown v. Mississippi]]"]
aliases: []
tags: ["case", "fifth-amendment", "fourteenth-amendment", "confessions", "voluntariness", "due-process", "coercion", "habeas"]
holding: "A confession that is the product of a drug having the effect of a 'truth serum' (scopolamine/hyoscine), administered to a suspect, is involuntary and inadmissible if it was not the product of a rational intellect and free will — regardless of whether the drug was administered by persons unaware of its properties and regardless of the confession's reliability."
lake:
  record_id: Townsend v. Sain
  status: verified
  projected_at: 2026-07-09
---

# Townsend v. Sain

*372 U.S. 293 (1963)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Townsend, a 19-year-old heroin addict of very low intelligence (described as "near mental defective"), was arrested for murder and robbery. During interrogation he developed narcotic-withdrawal symptoms, and a police physician injected him with phenobarbital and hyoscine — hyoscine being the same as scopolamine, a drug with the claimed properties of a "truth serum." The medication relieved his symptoms and he promptly confessed to several crimes. The identity of hyoscine as scopolamine, and scopolamine's reputation as a "truth serum," were not disclosed at the [[Common Legal Terms#suppression-hearing|suppression hearing]]. The state courts upheld the confession; a federal district court then denied [[Common Legal Terms#habeas-corpus|habeas corpus]] without an evidentiary hearing.

## Issue
Whether a confession produced after a suspect is injected with a drug having "truth serum" properties can be voluntary under the Due Process Clause — and the standards governing when a federal [[Common Legal Terms#habeas-corpus|habeas]] court must hold an evidentiary hearing.

## Rule
A drug-induced confession that is not the product of a free intellect is inadmissible. "If an individual's 'will was overborne' or if his confession was not 'the product of a rational intellect and a free will,' his confession is inadmissible because coerced. These standards are applicable whether a confession is the product of physical intimidation or psychological pressure and, of course, are equally applicable to a drug-induced statement. It is difficult to imagine a situation in which a confession would be less the product of a free intellect, less voluntary, than when brought about by a drug having the effect of a 'truth serum.' . . . Any questioning by police officers which *in fact* produces a confession which is not the product of a free intellect renders that confession inadmissible." — 372 U.S. at 307–308. ^pin-307

Reliability is irrelevant: "whether scopolamine produces true confessions or false confessions, if it in fact caused Townsend to make statements, those statements were constitutionally inadmissible." — [*Id.* at 308](https://www.courtlistener.com/opinion/106544/townsend-v-sain/#:~:text=whether%20scopolamine%20produces%20true%20confessions) n.5. ^pin-308

## Application
On these facts the Court did not itself find the confession involuntary; it held that Townsend's [[Common Legal Terms#habeas-corpus|habeas]] petition alleged facts that, if true, would establish that the hyoscine injection rendered his confession the involuntary product of a debilitated will — a question the district court could not resolve without hearing evidence. Because a material factual dispute existed (whether the drug in fact caused the confessions) and the [[Common Legal Terms#suppression-hearing|suppression hearing]] had not been a full and fair adjudication of it, the district court erred in dismissing the petition without an evidentiary hearing; the case was [[Reading and Citing Cases#on-remand|remanded]] for one.

## Conclusion
A confession caused by a "truth serum" drug, not the product of a free intellect, is inadmissible regardless of reliability; the judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]] for an evidentiary hearing on whether the drug in fact produced Townsend's confessions.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**, on the confession-voluntariness holding.
- **[[Common Legal Terms#habeas-corpus|Habeas]]-procedure caveat (home-by-holding):** *Townsend* also set the standards for when a federal [[Common Legal Terms#habeas-corpus|habeas]] court must hold an evidentiary hearing. That **procedural** holding (the deliberate-bypass branch) was **abrogated** by *Keeney v. Tamayo-Reyes*, 504 U.S. 1 (1992), and superseded by AEDPA, 28 U.S.C. §2254(e)(2). This page homes the case by its **confession-voluntariness** ratio, which remains good law.
- The voluntariness holding extends the coercion-not-reliability principle of [[Rogers v. Richmond]] and the overborne-will test of [[Lynumn v. Illinois]] to drug-induced statements, paralleling the drugged-confession branch of [[Beecher v. Alabama]] in the due-process line anchored by [[Brown v. Mississippi]].

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Townsend v. Sain*, 372 U.S. 293 (1963) — https://www.courtlistener.com/opinion/106544/townsend-v-sain/ — pinpoints: 307–308.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7cd9edf1fad5b526", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Townsend v. Sain"}, "payload": {"all": [{"cite": "372 U.S. 293", "page": "293", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "372"}, {"cite": "83 S. Ct. 745", "page": "745", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "83"}, {"cite": "9 L. Ed. 2d 770", "page": "770", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "9"}, {"cite": "1963 U.S. LEXIS 1941", "page": "1941", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1963"}], "display": "372 U.S. 293", "official": {"cite": "372 U.S. 293", "page": "293", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "372"}, "official_selection_present": true, "record_id": "Townsend v. Sain"}}
{"assertion_id": "00491e78a97f6d35", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-307", "record_id": "Townsend v. Sain"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-307", "pinpoint_status": "slip-only", "quote": "properties can be voluntary under the Due Process Clause — and the standards governing when a federal habeas court must hold an evidentiary hearing. ## Rule A drug-induced confession that is not the product of a free intellect is inadmissible.", "quote_fidelity": "mismatch", "record_id": "Townsend v. Sain", "star_marker": null}}
{"assertion_id": "194c29f3135c9342", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-308", "record_id": "Townsend v. Sain"}, "payload": {"fragment": "#:~:text=whether%20scopolamine%20produces%20true%20confessions", "page": null, "pin_id": "pin-308", "pinpoint_status": "star-verified", "quote": "whether scopolamine produces true confessions or false confessions, if it in fact caused Townsend to make statements, those statements were constitutionally inadmissible.", "quote_fidelity": "matched", "record_id": "Townsend v. Sain", "star_marker": "334"}}
{"assertion_id": "dc3416435dbaa010", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Townsend v. Sain"}, "payload": {"as_of_content": "1963-03-18", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Townsend v. Sain", "scope_note": "Good law on the confession-voluntariness holding (a drug/'truth serum'-induced confession not the product of a free intellect is inadmissible). The separate federal-habeas evidentiary-hearing standard (the Townsend circumstances/deliberate-bypass) was abrogated by Keeney v. Tamayo-Reyes, 504 U.S. 1 (1992), and superseded by AEDPA, 28 U.S.C. §2254(e)(2).", "varies_by_point": false}}
```

### lake record — Townsend v. Sain

```json
{
  "schema_version": "s2.v1",
  "record_id": "Townsend v. Sain",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Townsend v. Sain",
    "case_name_short": "Townsend",
    "case_name_full": "TOWNSEND v. SAIN, SHERIFF, Et Al.",
    "input_case_name": "Townsend v. Sain",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1963-03-18",
    "year": 1963,
    "docket": "8",
    "cluster_id": 106544,
    "lead_opinion_id": 106544,
    "sibling_ids": [
      106544,
      9422545,
      9422546,
      9422547
    ],
    "absolute_url": "/opinion/106544/townsend-v-sain/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "372 U.S. 293",
      "volume": "372",
      "reporter": "U.S.",
      "page": "293",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "83 S. Ct. 745",
        "volume": "83",
        "reporter": "S. Ct.",
        "page": "745",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "9 L. Ed. 2d 770",
        "volume": "9",
        "reporter": "L. Ed. 2d",
        "page": "770",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1963 U.S. LEXIS 1941",
        "volume": "1963",
        "reporter": "U.S. LEXIS",
        "page": "1941",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "372 U.S. 293",
        "volume": "372",
        "reporter": "U.S.",
        "page": "293",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 S. Ct. 745",
        "volume": "83",
        "reporter": "S. Ct.",
        "page": "745",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "9 L. Ed. 2d 770",
        "volume": "9",
        "reporter": "L. Ed. 2d",
        "page": "770",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1963 U.S. LEXIS 1941",
        "volume": "1963",
        "reporter": "U.S. LEXIS",
        "page": "1941",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "372 U.S. 293",
    "official_selection": {
      "court_class": "scotus",
      "selected": "372 U.S. 293",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-307",
      "page": null,
      "quote": "properties can be voluntary under the Due Process Clause \u2014 and the standards governing when a federal habeas court must hold an evidentiary hearing. ## Rule A drug-induced confession that is not the product of a free intellect is inadmissible.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-308",
      "page": null,
      "quote": "whether scopolamine produces true confessions or false confessions, if it in fact caused Townsend to make statements, those statements were constitutionally inadmissible.",
      "star_marker": "334",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 81892,
      "fragment": "#:~:text=whether%20scopolamine%20produces%20true%20confessions",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1963-03-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Townsend v. Sain",
    "varies_by_point": false,
    "scope_note": "Good law on the confession-voluntariness holding (a drug/'truth serum'-induced confession not the product of a free intellect is inadmissible). The separate federal-habeas evidentiary-hearing standard (the Townsend circumstances/deliberate-bypass) was abrogated by Keeney v. Tamayo-Reyes, 504 U.S. 1 (1992), and superseded by AEDPA, 28 U.S.C. \u00a72254(e)(2).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Anthony Juniper v. David Zook",
          "cluster_id": 4443845,
          "cite": [
            "876 F.3d 551"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Halliburton, Inc. v. Administrative Review Board",
          "cluster_id": 2750531,
          "cite": [
            "771 F.3d 254",
            "39 I.E.R. Cas. (BNA) 529",
            "2014 U.S. App. LEXIS 21743",
            "98 Empl. Prac. Dec. (CCH) 45,187",
            "2014 WL 5861790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brandon Dale Woodruff v. State",
          "cluster_id": 3094579,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Love v. Scribner",
          "cluster_id": 8672855,
          "cite": [
            "278 F. App'x 714"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Sedrice Maurice Simpson v. Larry Norris, Director, Arkansas Department of Correction",
          "cluster_id": 798140,
          "cite": [
            "490 F.3d 1029",
            "2007 U.S. App. LEXIS 15229",
            "2007 WL 1827496"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Strickland v. Washington",
          "cluster_id": 111170,
          "cite": [
            "80 L. Ed. 2d 674",
            "104 S. Ct. 2052",
            "466 U.S. 668",
            "1984 U.S. LEXIS 79"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Virginia",
          "cluster_id": 110138,
          "cite": [
            "61 L. Ed. 2d 560",
            "99 S. Ct. 2781",
            "443 U.S. 307",
            "1979 U.S. LEXIS 10"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Preiser v. Rodriguez",
          "cluster_id": 108772,
          "cite": [
            "36 L. Ed. 2d 439",
            "93 S. Ct. 1827",
            "411 U.S. 475",
            "1973 U.S. LEXIS 72"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ex Parte Young",
          "cluster_id": 2464872,
          "cite": [
            "418 S.W.2d 824",
            "1967 Tex. Crim. App. LEXIS 1084"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Denno",
          "cluster_id": 106881,
          "cite": [
            "12 L. Ed. 2d 908",
            "84 S. Ct. 1774",
            "378 U.S. 368",
            "1964 U.S. LEXIS 826",
            "1 A.L.R. 3d 1205",
            "28 Ohio Op. 2d 177"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cuyler v. Sullivan",
          "cluster_id": 110256,
          "cite": [
            "64 L. Ed. 2d 333",
            "100 S. Ct. 1708",
            "446 U.S. 335",
            "1980 U.S. LEXIS 96"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Connelly",
          "cluster_id": 111779,
          "cite": [
            "93 L. Ed. 2d 473",
            "107 S. Ct. 515",
            "479 U.S. 157",
            "1986 U.S. LEXIS 23",
            "55 U.S.L.W. 4043"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. Witt",
          "cluster_id": 111303,
          "cite": [
            "83 L. Ed. 2d 841",
            "105 S. Ct. 844",
            "469 U.S. 412",
            "1985 U.S. LEXIS 43",
            "53 U.S.L.W. 4108"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Browder v. Director, Dept. of Corrections of Ill.",
          "cluster_id": 109761,
          "cite": [
            "54 L. Ed. 2d 521",
            "98 S. Ct. 556",
            "434 U.S. 257",
            "1978 U.S. LEXIS 53"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schriro v. Landrigan",
          "cluster_id": 145734,
          "cite": [
            "167 L. Ed. 2d 836",
            "127 S. Ct. 1933",
            "550 U.S. 465",
            "2007 U.S. LEXIS 5496"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raddatz",
          "cluster_id": 110315,
          "cite": [
            "65 L. Ed. 2d 424",
            "100 S. Ct. 2406",
            "447 U.S. 667",
            "1980 U.S. LEXIS 49"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herrera v. Collins",
          "cluster_id": 112808,
          "cite": [
            "122 L. Ed. 2d 203",
            "113 S. Ct. 853",
            "506 U.S. 390",
            "1993 U.S. LEXIS 1017"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. New Jersey",
          "cluster_id": 107260,
          "cite": [
            "16 L. Ed. 2d 882",
            "86 S. Ct. 1772",
            "384 U.S. 719",
            "1966 U.S. LEXIS 1127",
            "36 Ohio Op. 2d 439",
            "8 Ohio Misc. 324"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sanders v. United States",
          "cluster_id": 106591,
          "cite": [
            "10 L. Ed. 2d 148",
            "83 S. Ct. 1068",
            "373 U.S. 1",
            "1963 U.S. LEXIS 1695"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Washington",
          "cluster_id": 109773,
          "cite": [
            "54 L. Ed. 2d 717",
            "98 S. Ct. 824",
            "434 U.S. 497",
            "1978 U.S. LEXIS 628"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106544 OR 9422545 OR 9422546 OR 9422547) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTM4MTQ3MjAwMDAwJnM9ODQ3MDU3NyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106544+OR+9422545+OR+9422546+OR+9422547%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(106544 OR 9422545 OR 9422546 OR 9422547)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzIxJnM9MTE3ODczJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106544+OR+9422545+OR+9422546+OR+9422547%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106544 OR 9422545 OR 9422546 OR 9422547)",
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
    "complete_query": "cites:(106544 OR 9422545 OR 9422546 OR 9422547)",
    "indexed_citing_opinions": 2834,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106544,
        "count": 2648,
        "count_source": "search"
      },
      {
        "opinion_id": 9422545,
        "count": 270,
        "count_source": "search"
      },
      {
        "opinion_id": 9422546,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9422547,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4499,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/townsend-v-sain.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY2MjEzOTgmcz00NzEzOTY5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106544+OR+9422545+OR+9422546+OR+9422547%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106544,
        "cited_id": 91598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 98441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 101098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 103458,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 104196,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 104557,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 104997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 105683,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 105726,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 105813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 106031,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 106040,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 106218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 235042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 237553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 239867,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 242868,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 247792,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 248755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 250462,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 251564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 251644,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 252544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 254906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 1208179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 2120258,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 2195532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 3416896,
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
    "date_created": "2026-07-05T21:52:00Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:52:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:52:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:56:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:52:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Townsend v. Sain

```
<div>
<center><b><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">372 U.S. 293</a></span> (1963)</b></center>
<center><h1>TOWNSEND<br>
v.<br>
SAIN, SHERIFF, ET AL.</h1></center>
<center>No. 8.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 19, 1962.</center>
<center>Restored to the calendar for reargument April 2, 1962.</center>
<center>Reargued October 8-9, 1962.</center>
<center>Decided March 18, 1963.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SEVENTH CIRCUIT.
<p><span class="star-pagination">*295</span> <i>George N. Leighton</i> reargued the cause and filed a brief for petitioner.</p>
<p><i>Edward J. Hladis</i> reargued the cause for respondents. With him on the brief was <i>Daniel P. Ward.</i></p>
<p>MR. CHIEF JUSTICE WARREN delivered the opinion of the Court.</p>
<p>This case, in its present posture raising questions as to the right to a plenary hearing in federal habeas corpus, comes to us once again after a tangle of prior proceedings. In 1955 the petitioner, Charles Townsend, was tried before a jury for murder in the Criminal Court of Cook County, Illinois. At his trial petitioner, through his court-appointed counsel, the public defender, objected to the <span class="star-pagination">*296</span> introduction of his confession on the ground that it was the product of coercion. A hearing was held outside the presence of the jury, and the trial judge denied the motion to suppress. He later admitted the confession into evidence. Further evidence relating to the issue of voluntariness was introduced before the jury. The charge permitted them to disregard the confession if they found that it was involuntary. Under Illinois law the admissibility of the confession is determined solely by the trial judge, but the question of voluntariness, because it bears on the issue of credibility, may also be presented to the jury. See, <i>e. g., </i><i>People</i> v. <i>Schwartz,</i> <span class="citation" data-id="2195532"><a href="/opinion/2195532/people-v-schwartz/#523" aria-description="Citation for case: People v. Schwartz">3 Ill. 2d 520, 523</a></span>, <span class="citation" data-id="2195532"><a href="/opinion/2195532/people-v-schwartz/#760" aria-description="Citation for case: People v. Schwartz">121 N. E. 2d 758, 760</a></span>; <i>People</i> v. <i>Roach,</i> <span class="citation" data-id="3416896"><a href="/opinion/3420387/the-people-v-roach/" aria-description="Citation for case: The People v. Roach">369 Ill. 95</a></span>, <span class="citation" data-id="3416896"><a href="/opinion/3420387/the-people-v-roach/" aria-description="Citation for case: The People v. Roach">15 N. E. 2d 873</a></span>. The jury found petitioner guilty and affixed the death penalty to its verdict. The Supreme Court of Illinois affirmed the conviction, two justices dissenting. <i>People</i> v. <i>Townsend,</i> <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/" aria-description="Citation for case: The People v. Townsend">11 Ill. 2d 30</a></span>, <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/" aria-description="Citation for case: The People v. Townsend">141 N. E. 2d 729</a></span>. This Court denied a writ of certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./355/850/">355 U. S. 850</a></span>.</p>
<p>Petitioner next sought post-conviction collateral relief in the Illinois State courts. The Cook County Criminal Court dismissed his petition without holding an evidentiary hearing. The Supreme Court of Illinois by order affirmed, holding that the issue of coercion was <i>res judicata,</i> and this Court again denied certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./358/887/">358 U. S. 887</a></span>. The issue of coercion was pressed at all stages of these proceedings.</p>
<p>Having thoroughly exhausted his state remedies, Townsend petitioned for habeas corpus in the United States District Court for the Northern District of Illinois. That court, considering only the pleadings filed in the course of that proceeding and the opinion of the Illinois Supreme Court rendered on direct appeal, denied the writ. The Court of Appeals for the Seventh Circuit dismissed an appeal. <span class="citation" data-id="247792"><a href="/opinion/247792/united-states-of-america-ex-rel-charles-townsend-v-frank-g-sain-sheriff/" aria-description="Citation for case: United States of America Ex Rel. Charles Townsend v....">265 F. 2d 660</a></span>. However, this Court granted a petition for certiorari, vacated the judgment and remanded for a decision as to whether, in the light of the <span class="star-pagination">*297</span> state-court record, a plenary hearing was required. <span class="citation multiple-matches"><a href="/c/U.%20S./359/64/">359 U. S. 64</a></span>.</p>
<p>On the remand, the District Court held no hearing and dismissed the petition, finding only that "Justice would not be served by ordering a full hearing or by awarding any or all of [the] relief sought by Petitioner." The judge stated that he was satisfied from the state-court records before him that the decision of the state courts holding the challenged confession to have been freely and voluntarily given by petitioner was correct, and that there had been no denial of federal due process of law. On appeal the Court of Appeals concluded that "[o]n habeas corpus, the district court's inquiry is limited to a study of the <i>undisputed</i> portions of the record" and that the undisputed portions of this record showed no deprivation of constitutional rights. <span class="citation" data-id="250462"><a href="/opinion/250462/united-states-of-america-ex-rel-charles-townsend-v-frank-g-sain-sheriff/#329" aria-description="Citation for case: United States of America Ex Rel. Charles Townsend v....">276 F. 2d 324, 329</a></span>. We granted certiorari to determine whether the courts below had correctly determined and applied the standards governing hearings in federal habeas corpus. <span class="citation multiple-matches"><a href="/c/U.%20S./365/866/">365 U. S. 866</a></span>. The case was first argued during the October Term 1961. Two of the Justices were unable to participate in a decision, and we subsequently ordered it reargued. <span class="citation multiple-matches"><a href="/c/U.%20S./369/834/">369 U. S. 834</a></span>. We now have it before us for decision.</p>
<p>The undisputed evidence adduced at the trial-court hearing on the motion to suppress showed the following. Petitioner was arrested by Chicago police shortly before or after 2 a. m. on New Year's Day 1954. They had received information from one Campbell, then in their custody for robbery, that petitioner was connected with the robbery and murder of Jack Boone, a Chicago steel-worker and the victim in this case. Townsend was 19 years old at the time, a confirmed heroin addict and a user of narcotics since age 15. He was under the influence of a dose of heroin administered approximately one and one-half hours before his arrest. It was his practice to take injections three to five hours apart. At about 2:30 a. m. <span class="star-pagination">*298</span> petitioner was taken to the second district police station and, shortly after his arrival, was questioned for a period variously fixed from one-half to two hours. During this period, he denied committing any crimes. Thereafter at about 5 a. m. he was taken to the 19th district station where he remained, without being questioned, until about 8:15 p. m. that evening. At that time he was returned to the second district station and placed in a line-up with several other men so that he could be viewed by one Anagnost, the victim of another robbery. When Anagnost identified another man, rather than petitioner, as his assailant, a scuffle ensued, the details of which were disputed by petitioner and the police. Following this incident petitioner was again subjected to questioning. He was interrogated more or less regularly from about 8:45 until 9:30 by police officers. At that time an Assistant State's Attorney arrived. Some time shortly before or after nine o'clock, but before the arrival of the State's Attorney, petitioner complained to Officer Cagney that he had pains in his stomach, that he was suffering from other withdrawal symptoms, that he wanted a doctor, and that he was in need of a dose of narcotics. Petitioner clutched convulsively at his stomach a number of times. Cagney, aware that petitioner was a narcotic addict, telephoned for a police physician. There was some dispute between him and the State's Attorney, both prosecution witnesses, as to whether the questioning continued until the doctor arrived. Cagney testified that it did and the State's Attorney to the contrary. In any event, after the withdrawal symptoms commenced it appears that petitioner was unresponsive to questioning. The doctor appeared at 9:45. In the presence of Officer Cagney he gave Townsend a combined dosage by injection of 1/8-grain of phenobarbital and 1/230-grain of hyoscine. Hyoscine is the same as scopolamine and is claimed by petitioner in this proceeding to have the properties of a "truth serum." <span class="star-pagination">*299</span> The doctor also left petitioner four or five 1/4-grain tablets of phenobarbital. Townsend was told to take two of these that evening and the remainder the following day. The doctor testified that these medications were given to petitioner for the purpose of alleviating the withdrawal symptoms; the police officers and the State's Attorney testified that they did not know what the doctor had given petitioner. The doctor departed between 10 and 10:30. The medication alleviated the discomfort of the withdrawal symptoms, and petitioner promptly responded to questioning.</p>
<p>As to events succeeding this point in time on January 1, the testimony of the prosecution witnesses and of the petitioner irreconcilably conflicts. However, for the purposes of this proceeding both sides agree that the following occurred. After the doctor left, Officer Fitzgerald and the Assistant State's Attorney joined Officer Cagney in the room with the petitioner, where he was questioned for about 25 minutes. They all then went to another room; a court reporter there took down petitioner's statements. The State's Attorney turned the questioning to the Boone case about 11:15. In less than nine minutes a full confession was transcribed. At about 11:45 the questioning was terminated, and petitioner was returned to his cell.</p>
<p>The following day, Saturday, January 2, at about 1 p. m. petitioner was taken to the office of the prosecutor where the Assistant State's Attorney read, and petitioner signed, transcriptions of the statements which he had made the night before. When Townsend again experienced discomfort on Sunday evening, the doctor was summoned. He gave petitioner more 1/4-grain tablets of phenobarbital. On Monday, January 4, Townsend was taken to a coroner's inquest where he was called to the witness stand by the State and, after being advised of his right not to testify, again confessed. At the time of the inquest petitioner was without counsel. The public defender was not <span class="star-pagination">*300</span> appointed to represent him until his arraignment on January 12.</p>
<p>Petitioner testified at the motion to suppress to the following version of his detention. He was initially questioned at the second district police station for a period in excess of two hours. Upon his return from the 19th district and after Anagnost, the robbery victim who had viewed the line-up, had identified another person as the assailant, Officer Cagney accompanied Anagnost into the hall and told him that he had identified the wrong person. Another officer then entered the room, hit the petitioner in the stomach and stated that petitioner knew that he had robbed Anagnost. Petitioner fell to the floor and vomited water and a little blood. Officer Cagney spoke to Townsend 5 or 10 minutes later, Townsend told him that he was sick from the use of drugs, and Cagney offered to call a doctor if petitioner would "cooperate" and tell the truth about the Boone murder. Five minutes later the officer had changed his tack; he told petitioner that he thought him innocent and that he would call the doctor, implying that the doctor would give him a narcotic. The doctor gave petitioner an injection in the arm and five pills. Townsend took three of these immediately. Although he felt better, he felt dizzy and sleepy and his distance vision was impaired. Anagnost was then brought into the room, and petitioner was asked by someone to tell Anagnost that he had robbed him. Petitioner then admitted the robbery, and the next thing he knew was that he was sitting at a desk. He fell asleep but was awakened and handed a pen; he signed his name believing that he was going to be released on bond. Townsend was taken to his cell but was later taken back to the room in which he had been before. He could see "a lot of lights flickering," and someone told him to hold his head up. This went on for a minute or so, and petitioner was then again taken back to his cell. The next morning petitioner's <span class="star-pagination">*301</span> head was much clearer, although he could not really remember what had occurred following the injection on the previous evening. An officer then told petitioner that he had confessed. Townsend was taken into a room and asked about a number of robberies and murders. "I believe I said yes to all of them." He could not hear very well and felt sleepy. That afternoon, after he had taken the remainder of the phenobarbital pills, he was taken to the office of the State's Attorney. Half asleep he signed another paper although not aware of its contents. The doctor gave him six or seven pills of a different color on Sunday evening. He took some of these immediately. They kept him awake all night. The following Monday morning he took more of these pills. Later that day he was taken to a coroner's inquest. He testified at the inquest because the officers had told him to do so.</p>
<p>Essentially the prosecution witnesses contradicted all of the above. They testified that petitioner had been questioned initially for only one-half hour, that he had scuffled with the man identified by Anagnost, and not an officer, and that he had not vomited. The officers and the Assistant State's Attorney also testified that petitioner had appeared to be awake and coherent throughout the evening of the 1st of January and at all relevant times thereafter, and that he had not taken the pills given to him by the doctor on the evening of the 1st. They stated that the petitioner had appeared to follow the statement which he signed and which was read to him at the State's Attorney's office. Finally they denied that any threats or promises of any sort had been made or that Townsend had been told to testify at the coroner's inquest. As stated above counsel was not provided for him at this inquest.</p>
<p>There was considerable testimony at the motion to suppress concerning the probable effects of hyoscine and phenobarbital. Dr. Mansfield, who had prescribed for <span class="star-pagination">*302</span> petitioner on the evening when he had first confessed, testified for the prosecution. He stated that a full therapeutic dose of hyoscine was 1/100 of a grain; that he gave Townsend 1/230 of a grain; that "phenobarbital . . . reacts very well combined with [hyoscine when] . . . you want to quiet" a person; that the combination will "pacify" because "it has an effect on the mind"; but that the dosage administered would not put a person to sleep and would not cause amnesia or impairment of eyesight or of mental condition. The doctor denied that he had administered any "truth serum." However, he did not disclose that hyoscine is the same as scopolamine or that the latter is familiarly known as "truth serum." Petitioner's expert was a doctor of physiology, pharmacology and toxicology. He was formerly the senior toxicological chemist of Cook County and at the time of trial was a professor of pharmacology, chemotherapy and toxicology at the Loyola University School of Medicine. He testified to the effect of the injection upon a hypothetical subject, obviously the petitioner. The expert stated that the effect of the prescribed dosage of hyoscine upon the subject, assumed to be a narcotic addict, "would be of such a nature that it could range between absolute sleep . . . and drowsiness, as one extreme, and the other extreme. . . would incorporate complete disorientation and excitation . . . ." And, assuming that the subject took 1/8-grain phenobarbital by injection and 1/2-grain orally at the same time, the expert stated that the depressive effect would be accentuated. The expert testified that the subject would suffer partial or total amnesia for five to eight hours and loss of near vision for four to six hours.</p>
<p>The trial judge summarily denied the motion to suppress and later admitted the court reporter's transcription of the confession into evidence. He made no findings of fact and wrote no opinion stating the grounds of his decision.<sup>[1]</sup><span class="star-pagination">*303</span> Thereafter, for the purpose of testing the credibility of the confession, the evidence relating to coercion was placed before the jury. At that time additional noteworthy testimony was elicited. The identity of hyoscine and scopolamine was established (but no mention of the drug's properties as a "truth serum" was made). An expert witness called by the prosecution testified that Townsend had such a low intelligence that he was a near mental defective and "just a little above moron." Townsend testified that the officers had slapped him on several occasions and had threatened to shoot him. Finally, Officer Corcoran testified that about 9 p. m., Friday evening before the doctor's arrival, Townsend had confessed to the Boone assault and robbery in response to a question propounded by Officer Cagney in the presence of Officers Fitzgerald, Martin and himself. But although Corcoran, Cagney and Martin had testified extensively at the motion to suppress, none had mentioned any such confession. Furthermore, both Townsend and Officer Fitzgerald at the motion to suppress had flatly said that no statement had been made before the doctor arrived. Although the other three officers testified at the trial, not one of them was asked to corroborate this phase of Corcoran's testimony.</p>
<p><span class="star-pagination">*304</span> It was established that the homicide occurred at about 6 p. m. on December 18, 1953. Essentially the only evidence which connected petitioner with the crime, other than his confession, was the testimony of Campbell, then on probation for robbery, and of the pathologist who performed the autopsy on Boone. Campbell testified that about the "middle" of December at about 8:30 p. m. he had seen Townsend walking down a street in the vicinity of the murder with a brick in his hand. He was unable to fix the exact date, did not know of the Boone murder at the time and, so far as his testimony revealed, had no reason to suspect that Townsend had done anything unlawful previous to their meeting.</p>
<p>The pathologist testified that death was caused by a "severe blow to the top of his [Boone's] head . . . ." Contrary to the statement in the opinion of the Illinois Supreme Court on direct appeal there was no testimony that the wounds were "located in such a manner as to have been inflicted by a blow with a house brick . . . ." <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#45" aria-description="Citation for case: The People v. Townsend">11 Ill. 2d, at 45</a></span>, <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#737" aria-description="Citation for case: The People v. Townsend">141 N. E. 2d, at 737</a></span>. In any event, that court characterized the evidence as meagre and noted that "it was brought out by cross-examination that Campbell had informed on the defendant to obtain his own release from custody." <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#44" aria-description="Citation for case: The People v. Townsend">11 Ill. 2d, at 44, 45</a></span>, <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#737" aria-description="Citation for case: The People v. Townsend">141 N. E. 2d, at 737</a></span>. Prior to petitioner's trial Campbell was placed on probation for robbery. Justice Schaefer, joined by Chief Justice Klingbiel in dissent, found Campbell's testimony "inherently incredible." <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#49" aria-description="Citation for case: The People v. Townsend">11 Ill. 2d, at 49</a></span>, <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#739" aria-description="Citation for case: The People v. Townsend">141 N. E. 2d, at 739</a></span>.</p>
<p>The theory of petitioner's application for habeas corpus did not rest upon allegations of physical coercion. Rather, it relied upon the hitherto undisputed testimony and alleged: (1) that petitioner vomited water and blood at the police station when he became ill from the withdrawal of narcotics; (2) that scopolamine is a "truth serum" and that this fact was not brought out at the motion to suppress <span class="star-pagination">*305</span> or at the trial; (3) that scopolamine "either alone or combined with Phenobarbital, is not the proper medication for a narcotic addict [and that] . . . [t]he effect of the intravenous injection of hyoscine and phenobarbital. . . is to produce a physiological and psychological condition adversely affecting the mind and will . . . [and] a psychic effect which removes the subject thus injected from the scope of reality; so that the person so treated is removed from contact with his environment, he is not able to see and feel properly, he loses proper use of his eye-sight, his hearing and his sense of perception and his ability to withstand interrogation"; (4) that the police doctor willfully suppressed this information and information of the identity of hyoscine and scopolamine, of his knowledge of these things, and of his intention to inject the hyoscine for the purpose of producing in Townsend "a physiological and psychological state . . . susceptible to interrogation resulting in . . . confessions . . ."; (5) that the injection caused Townsend to confess; (6) that on the evening of January 1, immediately after the injection of scopolamine, petitioner confessed to three murders and one robbery other than the murder of Boone and the robbery of Anagnost. Although there was some mention of other confessions at the trial, only the confession to the Anagnost robbery was specifically testified to.</p>
<p>Initially, in their answer, respondents stated: "Respondents admit the factual allegations of the petition well pleaded, but deny that Petitioner is held in custody by Respondents in violation of the constitution or laws of the United States . . . ." However, in the course of the first argument before the District Court it appeared that respondents admitted nothing alleged in the petition but merely took the position that the petition, on its face, was insufficient to entitle Townsend either to a hearing or to his release. In the course of the second argument, after the remand by this Court, respondents admitted <span class="star-pagination">*306</span> that "if the allegations of the petition are taken as true, then the petitioner is entitled to the relief he seeks . . . ," and that Townsend had confessed to at least five crimes after the injection of hyoscine. But respondents denied that "petitioner was adversely influenced by its [the hyoscine's] administration to the extent that his confession was obtained involuntarily"; that "Hyoscine is the truth serum"; that "the police surgeon or the prosecution concealed pertinent, material and relevant facts"; or that hyoscine was an improper medication under the circumstances. Despite respondents' concession that a dispute as to these facts existed, the district judge denied Townsend the opportunity to call witnesses or to produce other evidence in support of his allegations and dismissed the petition.</p>
<p>Before we granted the most recent petition for certiorari we requested respondents to submit an additional response directed to certain of the allegations of the petition for habeas corpus. Respondents submitted an "additional answer to petition for habeas corpus" in which they again admitted that Townsend had made confessions immediately after the injection of drugs. Specifically they admitted that petitioner confessed to the robberies of Anagnost and one Joseph Martin and to the murders of Boone, Thomas Johnson, Johnny Stinson, and Willis Thompson. The additional answer revealed the following additional information respecting Townsend's confessions to these crimes. Anagnost had identified another person, rather than petitioner, as his assailant. Thomas Johnson, before his death, had stated that his injury had been an accident. The Assistant State's Attorney did not even bother to transcribe Townsend's statement with respect to Thompson's murder "because the defendant could not recall the details of the assault which led to the death . . . ." At the Thompson coroner's inquest, when <span class="star-pagination">*307</span> the deputy coroner noted that Townsend was then unable to remember even that he had committed the crime, Officer Cagney complained: "Why shouldn't we be given credit for these Clean-ups." Despite these circumstances which made conviction for the Anagnost robbery and the Johnson and Thompson murders, at best, a remote possibility, petitioner was indicted for all of the crimes to which he had confessed. However, after a jury trial, he was acquitted of the murder of Johnny Stinson, and on the very day that he was sentenced to death for the Boone murder, on the motion of the prosecutor, the indictments for the murders of Johnson and Thompson and for the robberies of Anagnost and Martin were dismissed.</p>
<p>Although the petition for habeas corpus contains allegations which would constitute a claim that the police doctor, at the trial, had perjured himself, the heart of Townsend's claim is that his confession was inadmissible simply because it was caused by the injection of hyoscine. We must first determine whether petitioner's allegations, if proved, would establish the right to his release.</p>
<p></p>
<h2>I.</h2>
<p>Numerous decisions of this Court have established the standards governing the admissibility of confessions into evidence. If an individual's "will was overborne"<sup>[2]</sup> or if his confession was not "the product of a rational intellect and a free will,"<sup>[3]</sup> his confession is inadmissible because coerced. These standards are applicable whether a confession is the product of physical intimidation or psychological pressure and, of course, are equally applicable to a drug-induced statement. It is difficult to imagine a situation in which a confession would be less the product of a free intellect, less voluntary, than when brought <span class="star-pagination">*308</span> about by a drug having the effect of a "truth serum."<sup>[4]</sup> It is not significant that the drug may have been administered and the questions asked by persons unfamiliar with hyoscine's properties as a "truth serum," if these properties exist. Any questioning by police officers which <i>in fact</i> produces a confession which is not the product of a free intellect renders that confession inadmissible.<sup>[5]</sup> The <span class="star-pagination">*309</span> Court has usually so stated the test. See, <i>e. g., </i><i>Stroble</i> v. <i>California,</i> <span class="citation" data-id="9420722"><a href="/opinion/104997/stroble-v-california/" aria-description="Citation for case: Stroble v. California">343 U. S. 181</a></span>, 190: "If the confession which petitioner made . . . was in fact involuntary, the conviction cannot stand . . . ." And in <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199</a></span>, we held irrelevant the absence of evidence of improper purpose on the part of the questioning officers. There the evidence indicated that the interrogating officers thought the defendant sane when he confessed, but we judged the confession inadmissible because the probability was that the defendant was in fact insane at the time.</p>
<p>Thus we conclude that the petition for habeas corpus alleged a deprivation of constitutional rights. The remaining question before us then is whether the District Court was required to hold a hearing to ascertain the facts which are a necessary predicate to a decision of the ultimate constitutional question.</p>
<p>The problem of the power and duty of federal judges, on habeas corpus, to hold evidentiary hearingsthat is, to try issues of fact<sup>[6]</sup> anewis a recurring one. The Court last dealt at length with it in <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">344 U. S. 443</a></span>, in opinions by Justices Reed and Frankfurter, both speaking for a majority of the Court. Since then, <span class="star-pagination">*310</span> we have but touched upon it.<sup>[7]</sup> We granted certiorari in the 1959 Term to consider the question, but ultimately disposed of the case on a more immediate ground. <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#540" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 540</a></span>. It has become apparent that the opinions in <i>Brown</i> v. <i><span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">Allen, supra</a></span></i><i>,</i> do not provide answers for all aspects of the hearing problem for the lower federal courts, which have reached widely divergent, in fact often irreconcilable, results.<sup>[8]</sup> We mean to express no opinion on the correctness of particular decisions. But we think that it is appropriate at this time to elaborate the considerations which ought properly to govern the grant or denial of evidentiary hearings in federal habeas corpus proceedings.</p>
<p></p>
<h2>II.</h2>
<p>The broad considerations bearing upon the proper interpretation of the power of the federal courts on habeas corpus are reviewed at length in the Court's opinion in <i>Fay</i> <span class="star-pagination">*311</span> v. <i>Noia</i><i>, post,</i> p. 391, and need not be repeated here. We pointed out there that the historic conception of the writ, anchored in the ancient common law and in our Constitution as an efficacious and imperative remedy for detentions of fundamental illegality, has remained constant to the present day. We pointed out, too, that the Act of February 5, 1867, c. 28, § 1, <span class="citation no-link">14 Stat. 385</span>-386, which in extending the federal writ to state prisoners described the power of the federal courts to take testimony and determine the facts <i>de novo</i> in the largest terms, restated what apparently was the common-law understanding. <i>Fay</i> v. <i>Noia</i><i>, post,</i> p. 416, n. 27. The hearing provisions of the 1867 Act remain substantially unchanged in the present codification. <span class="citation no-link">28 U. S. C. § 2243</span>. In construing the mandate of Congress, so plainly designed to afford a trial-type proceeding in federal court for state prisoners aggrieved by unconstitutional detentions, this Court has consistently upheld the power of the federal courts on habeas corpus to take evidence relevant to claims of such detention. "Since <i>Frank</i> v. <i>Mangum,</i> <span class="citation" data-id="9418283"><a href="/opinion/98441/frank-v-mangum/#331" aria-description="Citation for case: Frank v. Mangum">237 U. S. 309, 331</a></span>, this Court has recognized that habeas corpus in the federal courts by one convicted of a criminal offense is a proper procedure `to safeguard the liberty of all persons within the jurisdiction of the United States against infringement through any violation of the Constitution,' even though the events which were alleged to infringe did not appear upon the face of the record of his conviction." <i>Hawk</i> v. <i>Olson,</i> <span class="citation" data-id="104196"><a href="/opinion/104196/hawk-v-olson/#274" aria-description="Citation for case: Hawk v. Olson">326 U. S. 271, 274</a></span>. <i>Brown</i> v. <i><span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">Allen</a></span></i> and numerous other cases have recognized this.</p>
<p>The rule could not be otherwise. The whole history of the writits unique developmentrefutes a construction of the federal courts' habeas corpus powers that would assimilate their task to that of courts of appellate review. The function on habeas is different. It is to test by way of an original civil proceeding, independent of the normal <span class="star-pagination">*312</span> channels of review of criminal judgments, the very gravest allegations. State prisoners are entitled to relief on federal habeas corpus only upon proving that their detention violates the fundamental liberties of the person, safeguarded against state action by the Federal Constitution. Simply because detention so obtained is intolerable, the opportunity for redress, which presupposes the opportunity to be heard, to argue and present evidence, must never be totally foreclosed. See <i>Frank</i> v. <i>Mangum,</i> <span class="citation" data-id="9418283"><a href="/opinion/98441/frank-v-mangum/#345" aria-description="Citation for case: Frank v. Mangum">237 U. S. 309, 345-350</a></span> (dissenting opinion of Mr. Justice Holmes). It is the typical, not the rare, case in which constitutional claims turn upon the resolution of contested factual issues. Thus a narrow view of the hearing power would totally subvert Congress' specific aim in passing the Act of February 5, 1867, of affording state prisoners a forum in the federal trial courts for the determination of claims of detention in violation of the Constitution. The language of Congress, the history of the writ, the decisions of this Court, all make clear that the power of inquiry on federal habeas corpus is plenary. Therefore, where an applicant for a writ of habeas corpus alleges facts which, if proved, would entitled him to relief, the federal court to which the application is made has the power to receive evidence and try the facts anew.</p>
<p></p>
<h2>III.</h2>
<p>We turn now to the considerations which in certain cases may make exercise of that power mandatory. The appropriate standardwhich must be considered to supersede, to the extent of any inconsistencies, the opinions in <i>Brown</i> v. <i><span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">Allen</a></span></i>is this: Where the facts are in dispute, the federal court in habeas corpus must hold an evidentiary hearing if the habeas applicant did not receive a full and fair evidentiary hearing in a state court, either at the time of the trial or in a collateral proceeding. In other words a federal evidentiary hearing is required <span class="star-pagination">*313</span> unless the state-court trier of fact has after a full hearing reliably found the relevant facts.<sup>[9]</sup></p>
<p>It would be unwise to overly particularize this test. The federal district judges are more intimately familiar with state criminal justice, and with the trial of fact, than are we, and to their sound discretion must be left in very large part the administration of federal habeas corpus. But experience proves that a too general standardthe "exceptional circumstances" and "vital flaw" tests of the opinions in <i>Brown</i> v. <i><span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">Allen</a></span></i>does not serve adequately to explain the controlling criteria for the guidance of the federal habeas corpus courts. Some particularization may therefore be useful. We hold that a federal court must grant an evidentiary hearing to a habeas applicant under the following circumstances: If (1) the merits of the factual dispute were not resolved in the state hearing; (2) the state factual determination is not fairly supported by the record as a whole; (3) the fact-finding procedure employed by the state court was not adequate to afford a full and fair hearing; (4) there is a substantial allegation of newly discovered evidence; (5) the material facts were not adequately developed at the state-court hearing; or (6) for any reason it appears that the state trier of fact did not afford the habeas applicant a full and fair fact hearing.</p>
<p>(1) There cannot even be the semblance of a full and fair hearing unless the state court actually reached and <span class="star-pagination">*314</span> decided the issues of fact tendered by the defendant. Thus, if no express findings of fact have been made by the state court, the District Court must initially determine whether the state court has impliedly found material facts. No relevant findings have been made unless the state court decided the constitutional claim tendered by the defendant on the merits. If relief has been denied in prior state collateral proceedings after a hearing but without opinion, it is often likely that the decision is based upon a procedural issuethat the claim is not collaterally cognizableand not on the merits. On the other hand, if the prior state hearing occurred in the course of the original trialfor example, on a motion to suppress allegedly unlawful evidence, as in the instant caseit will usually be proper to assume that the claim was rejected on the merits.</p>
<p>If the state court has decided the merits of the claim but has made no express findings, it may still be possible for the District Court to reconstruct the findings of the state trier of fact, either because his view of the facts is plain from his opinion or because of other indicia. In some cases this will be impossible, and the Federal District Court will be compelled to hold a hearing.</p>
<p>Reconstruction is not possible if it is unclear whether the state finder applied correct constitutional standards in disposing of the claim. Under such circumstances the District Court cannot ascertain whether the state court found the law or the facts adversely to the petitioner's contentions. Since the decision of the state trier of fact may rest upon an error of law rather than an adverse determination of the facts, a hearing is compelled to ascertain the facts. Of course, the possibility of legal error may be eliminated in many situations if the fact finder has articulated the constitutional standards which he has applied. Furthermore, the coequal responsibilities of state and federal judges in the administration of federal <span class="star-pagination">*315</span> constitutional law are such that we think the district judge may, in the ordinary case in which there has been no articulation, properly assume that the state trier of fact applied correct standards of federal law to the facts, in the absence of evidence, such as was present in <i>Rogers</i> v. <i><span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">Richmond</a></span>,</i> that there is reason to suspect that an incorrect standard was in fact applied.<sup>[10]</sup> Thus, if third-degree methods of obtaining a confession are alleged and the state court refused to exclude the confession from evidence, the district judge may assume that the state trier found the facts against the petitioner, the law being, of course, that third-degree methods necessarily produce a coerced confession.</p>
<p>In any event, even if it is clear that the state trier of fact utilized the proper standard, a hearing is sometimes required if his decision presents a situation in which the "so-called facts and their constitutional significance [are] . . . so blended that they cannot be severed in consideration." <i>Rogers</i> v. <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#546" aria-description="Citation for case: Rogers v. Richmond"><i>Richmond, supra,</i> at 546</a></span>. See <i>Frank</i> v. <span class="citation" data-id="9418283"><a href="/opinion/98441/frank-v-mangum/#347" aria-description="Citation for case: Frank v. Mangum"><i>Mangum, supra,</i> at 347</a></span> (Holmes, J., dissenting). Unless the district judge can be reasonably certain that the state trier would have granted relief if he had believed petitioner's allegations, he cannot be sure that the state trier in denying relief disbelieved these allegations. If any combination of the facts alleged would prove a violation of constitutional rights and the issue of law on those facts presents a difficult or novel problem for decision, any hypothesis as to the relevant factual determinations of the state trier involves the purest speculation. The federal <span class="star-pagination">*316</span> court cannot exclude the possibility that the trial judge believed facts which showed a deprivation of constitutional rights and yet (erroneously) concluded that relief should be denied. Under these circumstances it is impossible for the federal court to reconstruct the facts, and a hearing must be held.</p>
<p>(2) This Court has consistently held that state factual determinations not fairly supported by the record cannot be conclusive of federal rights. <i>Fiske</i> v. <i>Kansas,</i> <span class="citation" data-id="101098"><a href="/opinion/101098/fiske-v-kansas/#385" aria-description="Citation for case: Fiske v. Kansas">274 U. S. 380, 385</a></span>; <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#208" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 208-209</a></span>. Where the fundamental liberties of the person are claimed to have been infringed, we carefully scrutinize the state-court record. See, <i>e. g., </i><i>Blackburn</i> v. <i><span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/" aria-description="Citation for case: Blackburn v. Alabama">Alabama, supra</a></span></i><i>; </i><i>Moore</i> v. <i>Michigan,</i> <span class="citation" data-id="9841953"><a href="/opinion/105589/moore-v-michigan/" aria-description="Citation for case: Moore v. Michigan">355 U. S. 155</a></span>. The duty of the Federal District Court on habeas is no less exacting.</p>
<p>(3) However, the obligation of the Federal District Court to scrutinize the state-court findings of fact goes farther than this. Even if all the relevant facts were presented in the state-court hearing, it may be that the fact-finding procedure there employed was not adequate for reaching reasonably correct results. If the state trial judge has made serious procedural errors (respecting the claim pressed in federal habeas) in such things as the burden of proof, a federal hearing is required. Even where the procedure employed does not violate the Constitution, if it appears to be seriously inadequate for the ascertainment of the truth, it is the federal judge's duty to disregard the state findings and take evidence anew. Of course, there are procedural errors so grave as to require an appropriate order directing the habeas applicant's release unless the State grants a new trial forthwith. Our present concern is with errors which, although less serious, are nevertheless grave enough to deprive the state evidentiary hearing of its adequacy as a means of finally determining facts upon which constitutional rights depend.</p>
<p><span class="star-pagination">*317</span> (4) Where newly discovered evidence is alleged in a habeas application, evidence which could not reasonably have been presented to the state trier of facts, the federal court must grant an evidentiary hearing. Of course, such evidence must bear upon the constitutionality of the applicant's detention; the existence merely of newly discovered evidence relevant to the guilt of a state prisoner is not a ground for relief on federal habeas corpus. Also, the district judge is under no obligation to grant a hearing upon a frivolous or incredible allegation of newly discovered evidence.</p>
<p>(5) The conventional notion of the kind of newly discovered evidence which will permit the reopening of a judgment is, however, in some respects too limited to provide complete guidance to the federal district judge on habeas. If, for any reason not attributable to the inexcusable neglect of petitioner, see <i>Fay</i> v. <i>Noia</i><i>, post,</i> p. 438 (Part V), evidence crucial to the adequate consideration of the constitutional claim was not developed at the state hearing, a federal hearing is compelled. The standard of inexcusable default set down in <i>Fay</i> v. <i>Noia</i> adequately protects the legitimate state interest in orderly criminal procedure, for it does not sanction needless piecemeal presentation of constitutional claims in the form of deliberate by-passing of state procedures. Compare <i>Price</i> v. <i>Johnston,</i> <span class="citation" data-id="9420168"><a href="/opinion/104557/price-v-johnston/" aria-description="Citation for case: Price v. Johnston">334 U. S. 266</a></span>, 291: "The primary purpose of a <i>habeas corpus</i> proceeding is to make certain that a man is not unjustly imprisoned. And if for some justifiable reason he was previously unable to assert his rights or was unaware of the significance of relevant facts, it is neither necessary nor reasonable to deny him all opportunity of obtaining judicial relief."</p>
<p>(6) Our final category is intentionally open-ended because we cannot here anticipate all the situations wherein a hearing is demanded. It is the province of the district judges first to determine such necessities in accordance <span class="star-pagination">*318</span> with the general rules. The duty to try the facts anew exists in every case in which the state court has not after a full hearing reliably found the relevant facts.</p>
<p></p>
<h2>IV.</h2>
<p>It is appropriate to add a few observations concerning the proper application of the test we have outlined.</p>
<p><i>First.</i> The purpose of the test is to indicate the situations in which the holding of an evidentiary hearing is mandatory. In all other cases where the material facts are in dispute, the holding of such a hearing is in the discretion of the district judge. If he concludes that the habeas applicant was afforded a full and fair hearing by the state court resulting in reliable findings, he may, and ordinarily should, accept the facts as found in the hearing. But he need not. In every case he has the power, constrained only by his sound discretion, to receive evidence bearing upon the applicant's constitutional claim. There is every reason to be confident that federal district judges, mindful of their delicate role in the maintenance of proper federal-state relations, will not abuse that discretion. We have no fear that the hearing power will be used to subvert the integrity of state criminal justice or to waste the time of the federal courts in the trial of frivolous claims.</p>
<p><i>Second.</i> Although the district judge may, where the state court has reliably found the relevant facts, defer to the state court's findings of fact, he may not defer to its findings of law. It is the district judge's duty to apply the applicable federal law to the state court fact findings independently. The state conclusions of law may not be given binding weight on habeas. That was settled in <i>Brown</i> v. <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#506" aria-description="Citation for case: Brown v. Allen"><i>Allen, supra,</i> at 506</a></span> (opinion of Mr. Justice Frankfurter).</p>
<p><span class="star-pagination">*319</span> <i>Third.</i> A District Court sitting in habeas corpus clearly has the power to compel production of the complete state-court record. Ordinarily such a record including the transcript of testimony (or if unavailable some adequate substitute, such as a narrative record), the pleadings, court opinions, and other pertinent documents is indispensable to determining whether the habeas applicant received a full and fair state-court evidentiary hearing resulting in reliable findings. See <i>United States ex rel. Jennings</i> v. <i>Ragan,</i> <span class="citation" data-id="105813"><a href="/opinion/105813/united-states-ex-rel-jennings-v-ragen/" aria-description="Citation for case: United States Ex Rel. Jennings v. Ragen">358 U. S. 276</a></span>; <i>Townsend</i> v. <i>Sain,</i> <span class="citation" data-id="1208179"><a href="/opinion/1208179/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">359 U. S. 64</a></span>. Of course, if because no record can be obtained the district judge has no way of determining whether a full and fair hearing which resulted in findings of relevant fact was vouchsafed, he must hold one. So also, there may be cases in which it is more convenient for the district judge to hold an evidentiary hearing forthwith rather than compel production of the record. It is clear that he has the power to do so.</p>
<p><i>Fourth.</i> It rests largely with the federal district judges to give practical form to the principles announced today. We are aware that the too promiscuous grant of evidentiary hearings on habeas could both swamp the dockets of the District Courts and cause acute and unnecessary friction with state organs of criminal justice, while the too limited use of such hearings would allow many grave constitutional errors to go forever uncorrected. The accommodation of these competing factors must be made on the front line, by the district judges who are conscious of their paramount responsibility in this area.</p>
<p></p>
<h2>V.</h2>
<p>Application of the foregoing principles to the particular litigation before us is not difficult. Townsend received an evidentiary hearing at his original trial, where his confession was held to be voluntary. Having exhausted his <span class="star-pagination">*320</span> state remedies without receiving any further such hearing, he turned to the Federal District Court. Twice now, habeas corpus relief has been denied without an evidentiary hearing. On appeal from the second denial, the Court of Appeals held that "[o]n habeas corpus, the district court's inquiry is limited to a study of the <i>undisputed</i> portions of the record." That formulation was error. And we believe that on this record it was also error to refuse Townsend an evidentiary hearing in the District Court. The state trial judge rendered neither an opinion, conclusions of law, nor findings of fact. He made no charge to the jury setting forth the constitutional standards governing the admissibility of confessions. In short, there are no indicia which would indicate whether the trial judge applied the proper standard of federal law in ruling upon the admissibility of the confession. The Illinois Supreme Court opinion rendered at the time of direct appeal contains statements which might indicate that the court thought the confession was admissible if it satisfied the "coherency" standard. Under that test the confession would be admissible "[s]o long as the accused [was] . . . capable of making a narrative of past events or of stating his own participation in the crime . . . ." <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#43" aria-description="Citation for case: The People v. Townsend">11 Ill. 2d, at 43</a></span>, <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#736" aria-description="Citation for case: The People v. Townsend">141 N. E. 2d, at 736</a></span>. As we have indicated in Part I of this opinion, this test is not the proper one. Possibly the state trial judge believed that the admissibility of allegedly drug-induced confessions was to be judged by the "coherency" standard.<sup>[11]</sup> However, even if this possibility could be eliminated, and it could be ascertained <span class="star-pagination">*321</span> that correct standards of law were applied, it is still unclear whether the state trial judge would have excluded Townsend's confession as involuntary if he had believed the evidence which Townsend presented at the motion to suppress. The problem which the trial judge faced was novel and by no means without difficulty. We believe that the Federal District Court could not conclude that the state trial judge admitted the confession because he disbelieved the evidence which would show that it was involuntary. We believe that the findings of fact of the state trier could not be successfully reconstructed. We hold that, for this reason, an evidentiary hearing was compelled.<sup>[12]</sup></p>
<p>Furthermore, a crucial fact was not disclosed at the state-court hearing: that the substance injected into Townsend before he confessed has properties which may trigger statements in a legal sense involuntary.<sup>[13]</sup> This fact was vital to whether his confession was the product of a free will and therefore admissible. To be sure, there was medical testimony as to the general properties of hyoscine, from which might have been inferred the conclusion <span class="star-pagination">*322</span> that Townsend's power of resistance had been debilitated. But the crucially informative characterization of the drug, the characterization which would have enabled the judge and jury, mere laymen, intelligently to grasp the nature of the substance under inquiry, was inexplicably omitted from the medical experts' testimony. Under the circumstances, disclosure of the identity of hyoscine as a "truth serum" was indispensable to a fair, rounded, development of the material facts. And the medical experts' failure to testify fully cannot realistically be regarded as Townsend's inexcusable default. See <i>Fay</i> v. <i>Noia</i><i>, post,</i> p. 438 (Part V).</p>
<p>On the remand it would not, of course, be sufficient for the District Court merely to hear new evidence and to read the state-court record. Where an unresolved factual dispute exists, demeanor evidence is a significant factor in adjudging credibility. And questions of credibility, of course, are basic to resolution of conflicts in testimony. To be sure, the state-court record is competent evidence,<sup>[14]</sup> and either party may choose to rely solely upon the evidence contained in that record, but the petitioner, and the State, must be given the opportunity to present other testimonial and documentary evidence relevant to the disputed issues. This was not done here.</p>
<p>In deciding this case as we do, we do not mean to prejudge the truth of the allegations of the petition for habeas corpus. We decide only that on this record the federal district judge was obliged to hold a hearing.</p>
<p><i>Reversed and remanded.</i></p>
<p>MR. JUSTICE GOLDBERG, concurring.</p>
<p>I join in the opinion and judgment of the Court and add a few words by way of comment on the dissenting opinion of my Brother STEWART.</p>
<p><span class="star-pagination">*323</span> I cannot agree with MR. JUSTICE STEWART that the instructions given to the jury by the trial judge on the issue of credibility indicate the application of a proper constitutional test to measure the voluntarinessand hence the admissibilityof the petitioner's disputed confession of the Boone murder. In my view, the very portions of the instructions excerpted by my Brother STEWART support, if anything, the contrary conclusion that an improper and constitutionally impermissible standard was utilized by the trial judge himself in the suppression hearing.</p>
<p>If, as suggested by my Brother STEWART, these instructions are taken to evidence the exclusionary standard applied by the trial judge in ruling on the petitioner's motion to suppress, they reflect error of constitutional dimension, as does the standard of admissibility contained in the affirming opinion of the Illinois Supreme Court. While the appellate court, as pointed out in the opinion of THE CHIEF JUSTICE, see <i>ante,</i> pp. 319-321, appears to have adopted a test of "coherency" to measure the admissibility of the confession, the trial court seemingly concluded that inducement of amnesia was a prerequisite to disregard of the confession. Both standards, whether or not intended to incorporate similar elements, fail to conform to the requisite test.</p>
<p>The third paragraph of the instructions quoted by my Brother STEWART in footnote 2, <i>post,</i> p. 330, advises the jury that it might discount the confession if it found that administration of the drug caused the petitioner to "lose his memory," to suffer "a state of amnesia" during the period of questioning, <i>and</i> to be unable "to control his answers or to assert his will by denying the crime charged." By use of the conjunctive to incorporate the requirement of loss of control, this instruction indicates the trial court's apparent view that if the drug had the effect of overbearing the petitioner's will but did not also cause loss of <span class="star-pagination">*324</span> memory, the confession would nonetheless remain acceptable evidence of guilt. This conclusion is buttressed by the instruction quoted in the concluding paragraph of note 2 in my Brother STEWART'S dissenting opinion, in which the trial court indicates that the confession might be disregarded by the jury not simply if the drug had the effect asserted by the petitioner's expert in response to a hypothetical question, but only if, <i>in addition,</i> the drug so affected the petitioner's consciousness that "he did not know what he was doing." The petitioner may have been fully aware of what he was doing in confessing and may have suffered no loss of memory, but that is not the issue. The crucial question, and the measure of evidentiary propriety under the Constitution, is whether the drug whatever label was or was not affixed to itso overbore the petitioner's will that he was unable to resist confessing. Whether or not he was conscious of what he was doing, the petitioner could, because of the drug, have been wholly unable to stop himself from admitting guilt.<sup>[*]</sup></p>
<p>In the absence of contrary indications, I think we must recognize that the misconception of the constitutional standard evidenced by these instructions may well have infected the trial judge's ruling at the suppression hearing. The inference of error is not negatived by the remainder of the instructions, which permit disregard of the confession if induced by force, physical or mental, duress, or promise of reward. In the context of the instructions as a whole, these references to "voluntariness" do not meet the problems raised by the administration of the drug to the petitioner and do not vitiate the crucial inference that <span class="star-pagination">*325</span> the trial judge viewed exclusion as dependent upon the presence of facts in addition to a drug-induced sterilization of the petitioner's will.</p>
<p>For the reasons contained in the opinion of the Court, and on the basis of what I believe to be the wholly fair inference that the trial court misconceived the proper constitutional measure of admissibility of the petitioner's confession, the lack of any indication that the trial court did utilize the correct test, and the state appellate court's apparent application of a similarly erroneous standard, I agree that a hearing must be held below.</p>
<p>Finally, the Court's opinion does not warrant my Brother STEWART'S criticism as to the propriety or wisdom of articulating standards to govern the grant of evidentiary hearings in habeas corpus proceedings. The setting of certain standards is essential to disposition of this case and a definition of their scope and application is an appropriate exercise of this Court's adjudicatory obligations. Particularly when, as here, the Court is directing the federal judiciary as to its role in applying the historic remedy in a difficult and sensitive area involving large issues of federalism, the careful discharge of our function counsels that, "in order to preclude individualized enforcement of the Constitution in different parts of the Nation, [we] . . . lay down as specifically as the nature of the problem permits the standards or directions that should govern the District Judges in the disposition of applications for habeas corpus by prisoners under sentence of State courts." <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#501" aria-description="Citation for case: Brown v. Allen">344 U. S. 443, 501-502</a></span> (separate opinion of Mr. Justice Frankfurter).</p>
<p>MR. JUSTICE STEWART, whom MR. JUSTICE CLARK, MR. JUSTICE HARLAN, and MR. JUSTICE WHITE join, dissenting.</p>
<p>The basis for my disagreement with the Court can perhaps best be explained if I define at the outset the several areas in which I am entirely in accord with the Court's <span class="star-pagination">*326</span> opinion. First, as to the underlying issue of constitutional law, I completely agree that a confession induced by the administration of drugs is constitutionally inadmissible in a criminal trial. Secondly, I agree that the Court of Appeals in this case stated an erroneous standard when it said that "[o]n habeas corpus, the district court's inquiry is limited to a study of the <i>undisputed</i> portions of the record. . . ." <span class="citation" data-id="250462"><a href="/opinion/250462/united-states-of-america-ex-rel-charles-townsend-v-frank-g-sain-sheriff/#329" aria-description="Citation for case: United States of America Ex Rel. Charles Townsend v....">276 F. 2d 324, 329</a></span>. Thirdly, I agree that where an applicant for a writ of habeas corpus alleges facts which, if proved, would entitle him to relief, the federal court to which the application is made has the <i>power</i> to receive evidence and try the facts anew.<sup>[1]</sup></p>
<p>I differ with the Court's disposition of this case in two important respects. First, I strongly doubt the wisdom of using this caseor any otheras a vehicle for cataloguing in advance a set of standards which are inflexibly to compel district judges to grant evidentiary hearings in habeas corpus proceedings. Secondly, I think that a <i>de novo</i> evidentiary hearing is not required in the present case, even under the very standards which the Court's opinion elaborates.</p>
<p></p>
<h2>I.</h2>
<p>I have no quarrel with the Court's statement of the basic governing principle which should determine whether a hearing is to be had in a federal habeas corpus <span class="star-pagination">*327</span> proceeding: "Where the facts are in dispute, the federal court in habeas corpus must hold an evidentiary hearing if the habeas applicant did not receive a full and fair evidentiary hearing in a state court, either at the time of the trial or in a collateral proceeding." <i>Ante,</i> p. 312. But the Court rightly says that "[i]t would be unwise to overly particularize this test," and I think that in attempting to erect detailed hearing standards for the myriad situations presented by federal habeas corpus applications, the Court disregards its own wise admonition.</p>
<p>The Court has done little more today than to supply new phrasesimprecise in scope and uncertain in meaning for the habeas corpus vocabulary of District Court judges. And because they purport to establish mandatory requirements rather than guidelines, the tests elaborated in the Court's opinion run the serious risk of becoming talismanic phrases, the mechanistic invocation of which will alone determine whether or not a hearing is to be had.</p>
<p>More fundamentally, the enunciation of an elaborate set of standards governing habeas corpus hearings is in no sense required, or even invited, in order to decide the case before us, and the many pages of the Court's opinion which set these standards forth cannot, therefore, be justified even in terms of the normal function of dictum. The reasons for the rule against advisory opinions which purport to decide questions not actually in issue are too well established to need repeating at this late date. See, <i>e. g., </i><i>Marine Cooks</i> v. <i>Panama S. S. Co.,</i> <span class="citation" data-id="9421959"><a href="/opinion/106031/marine-cooks-stewards-v-panama-steamship-co/#368" aria-description="Citation for case: Marine Cooks &amp; Stewards v. Panama Steamship Co.">362 U. S. 365, 368, n. 5</a></span>; <i>Machinists Local</i> v. <i>Labor Board,</i> <span class="citation" data-id="9421969"><a href="/opinion/106040/local-lodge-no-1424-international-assn-of-machinists-v-national-labor/#415" aria-description="Citation for case: Local Lodge No. 1424, International Ass&#x27;n of MacHinists...">362 U. S. 411, 415, n. 5</a></span>. I regard these reasons as peculiarly persuasive in the present context. We should not try to hedge in with inflexible rules what is essentially an extraordinary writ, designed to do justice in extraordinary and often unpredictable situations.</p>
<p></p>
<h2>
<span class="star-pagination">*328</span> II.</h2>
<p>Even accepting the Court's detailed hearing standards <i>in toto,</i> however, I cannot agree that any one of them requires the District Court to hold a new evidentiary hearing in the present case. And I think, putting these rigid formulations to one side, that accepted principles governing the fair and prompt administration of criminal justice within our federal system affirmatively counsel <i>against</i> a <i>de novo</i> federal court hearing in this case.</p>
<p>The Court refers to two specific defects which it feels compel a hearing in the District Court: the absence of "indicia which would indicate whether the trial judge applied the proper standard of federal law in ruling upon the admissibility of the confession" and the fact that it was not disclosed in the state hearing that "the substance injected into Townsend before he confessed has properties which may trigger statements in a legal sense involuntary." Since the lengthy extracts from the testimony and pleadings in the Court's opinion do not seem to me to bear on these issues, it becomes necessary to sketch the prior proceedings in this case to indicate why I think the Court is mistaken in concluding that a new hearing is required.</p>
<p>During the early morning hours of January 1, 1954, the petitioner was arrested by the Chicago police. He admitted having given himself an injection of heroin 90 minutes before his arrest. Within an hour of his arrest, he was questioned for 30 minutes about various crimes, all of which he denied having committed. He was not questioned again until that evening.</p>
<p>Shortly after the evening questioning began, the petitioner complained of stomach pains and requested a doctor. A police surgeon was summoned, and he administered an injection consisting of 2 cc.'s of a saline solution in which 1/230 grain of hyoscine hydrobromide and 1/8 <span class="star-pagination">*329</span> grain of phenobarbital were dissolved. Slightly more than an hour later, the petitioner confessed to the murder of Boone. The following day, 15 hours after the police surgeon had administered the hyoscine, the petitioner initialed a copy of his previous night's statement in the offices of the State's Attorney General. At the coroner's hearing on January 4, the petitioner again confessed to the Boone killing.</p>
<p></p>
<h2>A. THE STANDARD OF FEDERAL LAW APPLIED BY THE STATE TRIAL COURT IN RULING UPON THE ADMISSIBILITY OF THE CONFESSION.</h2>
<p>At the trial, the petitioner's lawyer objected to introduction of the confession on the ground that it was involuntary. In accordance with Illinois practice, the motion to suppress was argued before the judge in the absence of the jury. During this proceeding, the petitioner testified that the injection had produced a temporary state of amnesia, that he could not remember making any confession, and that various other physical effects were produced. The police officers present at the petitioner's questioning stated that no change in the petitioner's demeanor suggesting any loss of his mental faculties had taken place as a result of the injection. On the question of the possible effects of the injection administered to the petitioner, Dr. Mansfield, the police surgeon and a licensed physician, testified for the State that he had treated thousands of narcotics addicts suffering from withdrawal symptoms, that in about 50% of such cases he had used the same treatment administered to the petitioner, and that he could recall no case in his experience where his use of hyoscine had produced loss of memory. A doctor of pharmacology (who was not a licensed physician) testified on behalf of the petitioner, and in answer to a hypothetical question stated that a person in the petitioner's condition at the time of interrogation could have <span class="star-pagination">*330</span> been suffering amnesia and partial loss of consciousness as the result of the treatment which had been administered to relieve the narcotic withdrawal symptoms. On cross-examination, this witness revealed that he had never actually seen the effects of hyoscine on a human and admitted that he was unfamiliar with its use in treating drug addicts. It is evident that a finder of fact could with reason have accorded more credibility to the evidence offered by the prosecution than to that offered by the defense.</p>
<p>It is true, as the Court today says, that in overruling the motion to suppress the confession, the trial judge did not explicitly spell out the exclusionary standards he was applying. The instructions to the jury at the end of the case, however, although directed to the question of credibility since that was the issue before the jury under Illinois procedurewere couched in terms of voluntariness, and they clearly established that the trial judge was aware of the correct constitutional standards to be applied.<sup>[2]</sup><span class="star-pagination">*331</span> Nothing in the record indicates that an incorrect standard was applied at the suppression hearing. Given these circumstances, I think it completely impermissible for us to assume that the trial judge did not apply "the proper standard of federal law in ruling upon the admissibility of the confession." Where, as here, a record is totally devoid of any indication that a state trial judge employed an erroneous constitutional standard, the presumption should surely be that the judge knew the law and correctly applied it. Certainly it is improper to presume that the trial judge did <i>not</i> know the law which the Constitution commands him to follow. Yet that is precisely the presumption which the Court makes in this case.</p>
<p></p>
<h2>
<span class="star-pagination">*332</span> B. DISCLOSURE OF THE "PROPERTIES" OF THE MEDICINE ADMINISTERED TO THE PETITIONER.</h2>
<p>Much of the evidence which had been presented to the judge alone was subsequently brought before the jury by defense counsel in an attempt to diminish the weight to be given to the confession. Additional evidence was also adduced by the prosecution, including testimony by another licensed physician, who made clear that hyoscine was identical with scopolamine. The case was submitted to the jury under unexceptionable instructions,<sup>[3]</sup> and the petitioner was convicted and sentenced to death. The Illinois Supreme Court, after reviewing in detail the evidence bearing on the voluntariness of the confession, affirmed the conviction. <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/" aria-description="Citation for case: The People v. Townsend">11 Ill. 2d 30</a></span>, <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/" aria-description="Citation for case: The People v. Townsend">141 N. E. 2d 729</a></span>. This Court denied certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./355/850/">355 U. S. 850</a></span>; rehearing denied, <span class="citation multiple-matches"><a href="/c/U.%20S./355/886/">355 U. S. 886</a></span>.</p>
<p>The petitioner then instituted post-conviction proceedings in the state trial court. His claim in these proceedings was that the confession had been procured as a result of the administration of scopolamine, that the witnesses for the State were aware of the identity of scopolamine and hyoscine and had deliberately withheld the fact of this identity at trial, and that the petitioner had consequently not been afforded an opportunity to make clear the basis for his claim that his confession had been coerced. The trial court dismissed the petition, and the Supreme Court of Illinois affirmed. In an unpublished opinion, that court concluded as follows:</p>
<blockquote>"A study of our opinion on [the original appeal] discloses that all of the evidence with respect to the injection of hyoscine and phenobarbital was carefully considered by us in resolving the issue of the validity of petitioner's confession. (People vs. <span class="star-pagination">*333</span> Townsend, <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#35" aria-description="Citation for case: The People v. Townsend">11 Ill. 2d, 30, 35, 44</a></span>). Thus, it is clear that the issue of the effect of the drug on the confession was before us . . . . The only matter which was not presented then was the fact that hyoscine and scopolamine are identical. In an attempt to escape from the doctrine of <i>res judicata,</i> the present petition for a writ of error contends that this fact could not have been presented to us because it was unknown to petitioner and his counsel at the time. Assuming for the moment the truth of this statement, we are of the opinion that the mere fact that the drug which was administered to petitioner is known by two different names presents no constitutional issue. At the original trial there was extensive medical testimony as to the properties and effects of hyoscine. If hyoscine and scopolamine are, in fact, identical, the medical testimony as to these properties and effects would be the same, regardless of the name of the drug. In determining the effect of the drug on the validity of petitioner's confession, the vital issue was its nature and its effect, rather than its name. This issue was thoroughly presented, both in the trial court and in this Court. Furthermore, the claim by petitioner now that the State `suppressed' this identity of hyoscine and scopolamine at the trial is destroyed by reference to the bill of exceptions from the original trial. A State medical witness, on cross-examination by petitioner's counsel stated: `Scopolamine or hyoscine are the same.' "</blockquote>
<p>Even under the detailed hearing requirements announced today by the Court, therefore, I think it is clear that the district judge had no choice but to conclude, on the basis of his examination of the full record of the state proceedings, that a new hearing on habeas corpus would <span class="star-pagination">*334</span> not be proper. For the record of the state proceedings clearly shows that the petitioner received a full and fair hearing as to the factual foundation for his constitutional claim<i>i. e.,</i> as to the properties of the drug which had been administered to him and the circumstances surrounding his confession. A total of 3 medical experts and 17 lay witnesses testified. Their testimony was in conflict. The trial court determined upon this conflicting evidence that there was no factual basis for the petitioner's claim that his confession had been involuntary. There is nothing whatever in the record to support an inference that the trial court did not scrupulously apply a completely correct constitutional standard in determining that the confession was admissible.<sup>[4]</sup> The trial court's determination was fully reviewed by the Supreme Court of Illinois on appeal, and reviewed again in state post-conviction proceedings. To be sure, no witness at the trial used the phrase "truth serum"a phrase which has no precise medical or scientific meaning. Yet I cannot but agree with the Supreme Court of Illinois that the mere fact that a drug may be known by more than one name hardly presents a constitutional issue.</p>
<p>Under our Constitution the State of Illinois has the power and duty to administer its own criminal justice. In carrying out that duty, Illinois must, as must each State, conform to the Due Process Clause of the Fourteenth Amendment. I think Illinois has clearly accorded the petitioner due process in this case. To require a federal court now to hold a new trial of factual claims which were long ago fully and fairly determined in the courts of Illinois is, I think, to frustrate the fair and prompt administration of criminal justice, to disrespect the fundamental structure of our federal system, and to debase the Great Writ of Habeas Corpus.</p>
<p>I would affirm.</p>
<h2>NOTES</h2>
<p>[1]  The final defense witness who testified at the motion to suppress was excused. The following then transpired:
</p>
<p>"MR. BRANION [a defense attorney]: That's all we have, if the Court please.</p>
<p>"The COURT: The defense rests on this hearing?</p>
<p>"MR. BRANION: Defense rests.</p>
<p>"The COURT: Anything further from the State?</p>
<p>"MR. McGOVERN: The State rests for the purpose of this hearing, Judge.</p>
<p>"The COURT: Gentlemen, the Court will deny the motion to suppress and admit the statement into evidence and we will proceed with the presentation of the evidence [to the jury]."</p>
<p>[2]  <i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/#440" aria-description="Citation for case: Reck v. Pate">367 U. S. 433, 440</a></span>.</p>
<p>[3]  <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#208" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 208</a></span>.</p>
<p>[4]  Of course, there are many relevant circumstances in this case which a district judge would be required to consider in determining whether the injection of scopolamine caused Townsend to confess. Among these are his lack of counsel at the time, his drug addiction, the fact that he was a "near mental defective," and his youth and inexperience.</p>
<p>[5]  Respondents do not dispute this. In fact at the time of the second argument before the District Court respondents stated:
</p>
<p>"If it was a factto put it very bluntly as we will very shortly, and elaborate upon itif a truth serum was administered to the petitioner and he was influenced by the truth serum and gave an involuntary confession, upon which his conviction was obtained, then that is it."</p>
<p>It is at least generally recognized that the administration of sufficient doses of scopolamine will break down the will. Thus, it is stated in The Dispensatory of the United States (25th ed. 1955) 1223: "Many persons are excessively susceptible to scopolamine and toxic symptoms may occur; such symptoms are often very alarming. There are marked disturbances of intellection, ranging from complete disorientation to an active delirium . . . ." The early literature on the subject designated scopolamine as a "truth serum." It was thought to produce true confessions by criminal suspects. <i>E. g.,</i> House, Why Truth Serum Should be Made Legal, 42 Medico-Legal Journal 138 (1925). And as recently as 1940 Dean Wigmore suggested that scopolamine might be useful in criminal interrogation. 3 Wigmore on Evidence (3d ed. 1940) § 998, at 642. However, some more recent commentators suggest that scopolamine's use is not likely to produce true confessions. On the contrary it is said:</p>
<p>"Unfortunately, persons under the influence of drugs are very suggestible and may confess to crimes which they have not committed. False or misleading answers may be given, especially when questions are improperly phrased. For example, if the police officer asserted in a confident tone `You did steal the money, didn't you?', a suggestible suspect might easily give a false affirmative answer." MacDonald, Truth Serum, 46 J. Crim. L. 259, 259-260 (1955). We make no findings as to either the medical properties of scopolamine or the likely effect of the dosage administered to Townsend. However, whether scopolamine produces true confessions or false confessions, if it in fact caused Townsend to make statements, those statements were constitutionally inadmissible.</p>
<p>[6]  By "issues of fact" we mean to refer to what are termed basic, primary, or historical facts: facts "in the sense of a recital of external events and the credibility of their narrators . . . ." <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#506" aria-description="Citation for case: Brown v. Allen">344 U. S. 443, 506</a></span> (opinion of Mr. Justice Frankfurter). So-called mixed questions of fact and law, which require the application of a legal standard to the historical-fact determinations, are not facts in this sense.</p>
<p>[7]  See <i>Thomas</i> v. <i>Arizona,</i> <span class="citation" data-id="105683"><a href="/opinion/105683/thomas-v-arizona/" aria-description="Citation for case: Thomas v. Arizona">356 U. S. 390</a></span>; <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="105726"><a href="/opinion/105726/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">357 U. S. 220</a></span> (denial of certiorari with accompanying statement); <i>United States ex rel. Jennings</i> v. <i>Ragen,</i> <span class="citation" data-id="105813"><a href="/opinion/105813/united-states-ex-rel-jennings-v-ragen/" aria-description="Citation for case: United States Ex Rel. Jennings v. Ragen">358 U. S. 276</a></span> (<i>per curiam</i>); <i>Townsend</i> v. <i>Sain,</i> <span class="citation" data-id="1208179"><a href="/opinion/1208179/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">359 U. S. 64</a></span> (<i>per curiam</i>) (vacating judgment on authority of <i>Jennings</i> v. <i><span class="citation" data-id="105813"><a href="/opinion/105813/united-states-ex-rel-jennings-v-ragen/" aria-description="Citation for case: United States Ex Rel. Jennings v. Ragen">Ragen, supra</a></span></i>).</p>
<p>[8]  See, <i>e. g., </i><i>United States ex rel. Tillery</i> v. <i>Cavell,</i> <span class="citation" data-id="254906"><a href="/opinion/254906/united-states-of-america-ex-rel-donald-tillery-v-angelo-c-cavell/" aria-description="Citation for case: United States of America Ex Rel. Donald Tillery v. Angelo...">294 F. 2d 12</a></span> (C. A. 3d Cir.); <i>Schlette</i> v. <i>People,</i> <span class="citation" data-id="252544"><a href="/opinion/252544/schlette-v-people-of-state-of-california/" aria-description="Citation for case: Schlette v. People of State of California">284 F. 2d 827</a></span> (C. A. 9th Cir.); <i>Bolling</i> v. <i>Smyth,</i> <span class="citation" data-id="251644"><a href="/opinion/251644/joe-bolling-v-w-frank-smyth-jr-superintendent-of-the-virginia-state/" aria-description="Citation for case: Joe Bolling v. W. Frank Smyth, Jr., Superintendent of the...">281 F. 2d 192</a></span> (C. A. 4th Cir.); <i>Chavez</i> v. <i>Dickson,</i> <span class="citation" data-id="6919807"><a href="/opinion/7018836/chavez-v-dickson/" aria-description="Citation for case: Chavez v. Dickson">280 F. 2d 727</a></span> (C. A. 9th Cir.); <i>Gay</i> v. <i>Graham,</i> <span class="citation" data-id="248755"><a href="/opinion/248755/frank-delano-gay-oliver-townsend-and-willie-olen-scott-v-marcell-graham/" aria-description="Citation for case: Frank Delano Gay, Oliver Townsend and Willie Olen Scott...">269 F. 2d 482</a></span> (C. A. 10th Cir.); <i>United States ex rel. Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9446051"><a href="/opinion/244398/united-states-ex-rel-harold-d-rogers-relator-appellee-v-mark-s/" aria-description="Citation for case: United States Ex Rel. Harold D. Rogers, Relator-Appellee...">252 F. 2d 807</a></span> (C. A. 2d Cir.), cert. denied with accompanying statement, <span class="citation" data-id="105726"><a href="/opinion/105726/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">357 U. S. 220</a></span>; <i>United States ex rel. Alvarez</i> v. <i>Murphy,</i> <span class="citation" data-id="242868"><a href="/opinion/242868/united-states-of-america-ex-rel-george-alvarez-v-robert-murphy-warden-of/" aria-description="Citation for case: United States of America Ex Rel. George Alvarez v. Robert...">246 F. 2d 871</a></span> (C. A. 2d Cir.); <i>Tyler</i> v. <i>Pepersack,</i> <span class="citation" data-id="239867"><a href="/opinion/239867/clarence-e-tyler-v-v-l-pepersack-warden-maryland-penitentiary/" aria-description="Citation for case: Clarence E. Tyler v. V. L. Pepersack, Warden, Maryland...">235 F. 2d 29</a></span> (C. A. 4th Cir.); <i>Cranor</i> v. <i>Gonzales,</i> <span class="citation" data-id="237553"><a href="/opinion/237553/john-r-cranor-superintendent-of-the-washington-state-penitentiary-at/" aria-description="Citation for case: John R. Cranor, Superintendent of the Washington State...">226 F. 2d 83</a></span> (C. A. 9th Cir.); <i>United States ex rel. De Vita</i> v. <i>McCorkle,</i> <span class="citation" data-id="235042"><a href="/opinion/235042/united-states-of-america-ex-rel-silvio-de-vita-v-lloyd-w-mccorkle/" aria-description="Citation for case: United States of America Ex Rel. Silvio De Vita v. Lloyd...">216 F. 2d 743</a></span> (C. A. 3d Cir.). See also Note, Habeas Corpus: Developments Since Brown v. Allen: A Survey and Analysis, <span class="citation no-link">53 Nw. U. L. Rev. 765</span>; Comment, Federal Habeas Corpus Review of State Convictions: An Interplay of Appellate Ambiguity and District Court Discretion, 68 Yale L. J. 98.</p>
<p>[9]  In announcing this test we do not mean to imply that the state courts are required to hold hearings and make findings which satisfy this standard, because such hearings are governed to a large extent by state law.
</p>
<p>The existence of the exhaustion of state remedies requirement (announced in <i>Ex parte Royall,</i> <span class="citation" data-id="91598"><a href="/opinion/91598/ex-parte-royall/" aria-description="Citation for case: Ex Parte Royall">117 U. S. 241</a></span>, and now codified in <span class="citation no-link">28 U. S. C. § 2254</span>) lends support to the view that a federal hearing is not always required. It presupposes that the State's adjudication of the constitutional issue can be of aid to the federal court sitting in habeas corpus.</p>
<p>[10]  Of course, under <i>Rogers</i> v. <i>Richmond,</i> a new trial is required if the trial judge or the jury, in finding the facts, has been guided by an erroneous standard of law. However, there will be situations in which statements of the trier of fact will do no more than create doubt as to whether the correct standard has been applied. In such situations a District Court hearing to determine the constitutional issue will be necessary.</p>
<p>[11]  The charge to the jury dealt only with the issues of credibility so far as the confession was concerned. Even accepting the relevance of the instructions, there is nothing in the charge to the jury to show that the trial judge, like the Supreme Court, did not think that voluntariness was conclusively established by a showing that the defendant was coherent.</p>
<p>[12]  The dissent fails to say why a hearing was not required for this reason. And "accepting the Court's . . . hearing standards" as the dissent does, it cannot seriously be argued that a hearing was not compelled. True the state trial judge instructed the jury that it <i>could</i> disregard the confession on grounds of credibility if it believed the petitioner's expert. But this hardly indicates whether the trial judge, at the motion to suppress, himself disbelieved the expert or whether he thought that, notwithstanding the truth of the expert's testimony, the confession was voluntary.</p>
<p>[13]  It appears that at the suppression hearing it was not disclosed that hyoscine (the substance injected, along with phenobarbital, into Townsend) was identical to scopolamine, and neither was it disclosed that scopolamine is familiarly known as "truth serum." Later on in the trial, there was testimony that hyoscine is identical to scopolamine, but not that scopolamine (or hyoscine) is a "truth serum."</p>
<p>[14]  Cf. <span class="citation no-link">28 U. S. C. §§ 2245</span>, 2247.</p>
<p>[*]  The petitioner's initial resistance to admitting guilt, his sudden change in attitude, and the veritable flood of confessions succeeding immediately upon administration of the drug to him, see <i>ante,</i> pp. 306-307, all indicate the real possibility that his will was so overborne. Moreover, the reliability of a number of these confessions is seriously impaired. See <i><span class="citation no-link">ibid.</span></i></p>
<p>[1]  Indeed, the original version of <span class="citation no-link">28 U. S. C. § 2243</span> directed the court to "proceed in a summary way to <i>determine the facts</i> of the case, <i>by hearing the testimony</i> and arguments, and thereupon to dispose of the party as law and justice require." See <i>Walker</i> v. <i>Johnston,</i> <span class="citation" data-id="103458"><a href="/opinion/103458/walker-v-johnston/#283" aria-description="Citation for case: Walker v. Johnston">312 U. S. 275, 283-284</a></span>. (Emphasis added.) The statute was later revised so that it now provides that "The court shall summarily hear and determine the facts, and dispose of the matter as law and justice require." The Revisers' notes indicate that the change was one of "phraseology" and not substance.
</p>
<p>Where the state court has reliably found facts relevant to any issue, the district judge in such a hearing should, of course, give appropriate deference to such findings. See <i>ante,</i> p. 318.</p>
<p>[2]  Among the instructions given were the following:
</p>
<p>"There has been admitted into evidence a written confession alleged to have been made freely and voluntarily by the defendant.</p>
<p>"You are further instructed that a confession made freely and voluntarily by a person charged with a crime may be considered by you, but if you find from the evidence that any force, physically or mentally, has been exerted upon the defendant by those having the defendant in charge after his arrest in order to obtain a confession, or that those persons made any promises to reward him if he would make such a confession, then you may totally disregard such confession.</p>
<p>"You are further instructed that if you find from the evidence that the defendant was given drugs and that said drugs caused him to lose his memory and create a state of amnesia in the defendant during the questioning of this defendant by the police or State's Attorney and that the defendant was not able to control his answers or to assert his will by denying the crime charged, then you may totally disregard such confession.</p>
<p>"You are instructed that if you find from the evidence that any influence was used on the defendant which amounted to duress upon his mind or body which caused him to make the confession, then you may totally disregard the confession.</p>
<p>.....</p>
<p>"You are further instructed that if you believe from the evidence in this case that duress or influence either physically or mentally, was exerted upon the defendant which caused him to make the written confession which has been introduced into evidence, then you may further consider whether this influence was still in existence at the time the defendant appeared at the coroner's inquest and is alleged to have made a confession there.</p>
<p>"There has been introduced into evidence the testimony of a witness, who is in the category known as an `Expert Witness,' who testified as to what influence or effect certain drugs had upon a hypothetical person.</p>
<p>"You are further instructed that you may take this testimony into consideration in determining whether the drugs alleged to have been administered to the defendant by Dr. Mansfield would have the same effect upon the defendant that the drug in the opinion of the `Expert Witness' had upon the hypothetical person, and if you believe from all the evidence in this case that the drugs had the effect upon the defendant to cause his consciousness to be impaired to the extent that he did not know what he was doing while he was being questioned by police officers or the Assistant State's Attorney, then you may totally disregard any statement or confession that he is alleged to have made during the time such influence, if any, was exerted upon him."</p>
<p>[3]  See footnote <span class="citation" data-id="9421969"><a href="/opinion/106040/local-lodge-no-1424-international-assn-of-machinists-v-national-labor/" aria-description="Citation for case: Local Lodge No. 1424, International Ass&#x27;n of MacHinists...">2, <i>supra.</i></a></span></p>
<p>[4]  See pp. 330-331, <i>supra.</i></p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Trupiano v. United States.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Trupiano v. United States
type: case
citation: "334 U.S. 699 (1948)"
parallel_cite: "68 S. Ct. 1229; 92 L. Ed. 2d 1663; 92 L. Ed. 1663"
neutral_cite: 1948 U.S. LEXIS 1986
court: U.S.
court_level: scotus
circuit: ""
year: 1948
date_decided: 1948-06-14
docket: 427
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
  opinion_url: "https://www.courtlistener.com/opinion/104576/trupiano-v-united-states/"
  cluster_id: 104576
  opinion_id: null
  identity_checked: true
lake:
  record_id: Trupiano v. United States
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[SIA Persons]]"
    role: Historical / origin
related:
  - "[[Chimel v. California]]"
  - "[[SIA Persons]]"
tags:
  - case
  - fourth-amendment
  - search-incident-to-arrest
  - warrant-requirement
  - seizure
  - overruled
  - historical
holding: "Even incident to a lawful arrest, officers who had ample time and opportunity to obtain a search warrant must do so before seizing contraband — the 'whenever reasonably practicable' warrant rule, rejected two years later in United States v. Rabinowitz (1950) and superseded by the modern Chimel framework."
---

# Trupiano v. United States

*334 U.S. 699 (1948)* (No. 427) · Supreme Court of the United States · **Historical** · Treatment: **Overruled — rendered as history (⚪ unverified, pending S9)** — superseded by [[Chimel v. California]] (1969)
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the subsequent-history treatment below is authored orientation, not machine-certified. Identity cluster 104576 → 334 U.S. 699, decided 1948-06-14; Rule quote string-matched to the CL opinion text 2026-07-07. -->

## Background
Federal agents, aided by an informer working inside the operation, surveilled an illegal distillery on a New Jersey farm for weeks. They knew every detail of its construction and operation and had abundant time to obtain warrants. Instead, they entered without a warrant, arrested an operator caught running the still, and seized the distillery equipment and contraband. Trupiano and his codefendants moved to suppress the seized property.

## Issue
Whether contraband and equipment may be seized without a search warrant as incident to a lawful arrest, where the officers had ample opportunity to obtain a warrant beforehand.

## Rule
The Court (Murphy, J.) sustained the warrantless arrest but held the warrantless seizure of the still unlawful. It announced a strong warrant-preference rule for searches and seizures of property: "It is a cardinal rule that, in seizing goods and articles, law enforcement agents must secure and use search warrants wherever reasonably practicable." — 334 U.S. at 705. ^pin-705

A lawful arrest does not, by itself, dispense with that requirement when there is no reason the officers could not have obtained a warrant.

## Application
Because the agents had known the facts for weeks and had every chance to present them to a magistrate, nothing made a warrant impracticable; their failure to get one could not be excused by the fortuity that the seizure coincided with an arrest. The mere presence of a lawful arrest could not, by itself, legalize a warrantless search or seizure, lest the exception swallow the rule.

## Conclusion
The judgment was **reversed** as to the seizure of the contraband; Murphy, J., delivered the opinion of the Court.

## Treatment & subsequent history
**Overruled — the framework has twice been remade.** *Trupiano*'s "whenever reasonably practicable" warrant rule was rejected just two years later in *United States v. Rabinowitz*, 339 U.S. 56 (1950), which held that the test is whether a [[Search Incident to Arrest|search incident to arrest]] is *reasonable*, not whether it was practicable to get a warrant. The Court then reversed course again in *[[Chimel v. California]]* (1969), overruling *Rabinowitz* and confining a [[Search Incident to Arrest|search incident to arrest]] to the arrestee's person and the area within his immediate control — the rule that governs today.

*Status note (⚪):* authored from a CourtListener-verified identity stub; the subsequent-history above is well-settled but has not completed the project's two-key certification, so the page renders under the ⚪ banner until S9 promotion. *United States v. Rabinowitz* is not yet in the corpus and is named in plain text to avoid a dangling link. Preserved as **history**, never as live law.

## Appears on
- [[SIA Persons]] — *Historical / origin*

## Sources
- [*Trupiano v. United States*, 334 U.S. 699 (1948)](https://www.courtlistener.com/opinion/104576/trupiano-v-united-states/) — pinpoint: 705 (Opinion of the Court; Murphy, J.); Rule quote string-matched to the CL opinion text 2026-07-07. Superseded line: *United States v. Rabinowitz*, 339 U.S. 56 (1950); *Chimel v. California*, 395 U.S. 752 (1969) (successor page: [[Chimel v. California]]).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "34727629658d7ac9", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Trupiano v. United States"}, "payload": {"all": [{"cite": "334 U.S. 699", "page": "699", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "334"}, {"cite": "68 S. Ct. 1229", "page": "1229", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "68"}, {"cite": "92 L. Ed. 2d 1663", "page": "1663", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "92"}, {"cite": "1948 U.S. LEXIS 1986", "page": "1986", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1948"}, {"cite": "92 L. Ed. 1663", "page": "1663", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "92"}], "display": "334 U.S. 699", "official": {"cite": "334 U.S. 699", "page": "699", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "334"}, "official_selection_present": true, "record_id": "Trupiano v. United States"}}
{"assertion_id": "9d6bfdaab55b0769", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Trupiano v. United States"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Trupiano v. United States", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Trupiano v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Trupiano v. United States",
  "status": "under_review",
  "identity": {
    "case_name": "Trupiano v. United States",
    "case_name_short": "Trupiano",
    "case_name_full": "TRUPIANO Et Al. v. UNITED STATES",
    "input_case_name": "Trupiano v. United States",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1948-06-14",
    "year": 1948,
    "docket": "427",
    "cluster_id": 104576,
    "lead_opinion_id": 9420205,
    "sibling_ids": [],
    "absolute_url": "/opinion/104576/trupiano-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "334 U.S. 699",
      "volume": "334",
      "reporter": "U.S.",
      "page": "699",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "68 S. Ct. 1229",
        "volume": "68",
        "reporter": "S. Ct.",
        "page": "1229",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 2d 1663",
        "volume": "92",
        "reporter": "L. Ed. 2d",
        "page": "1663",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 1663",
        "volume": "92",
        "reporter": "L. Ed.",
        "page": "1663",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1948 U.S. LEXIS 1986",
        "volume": "1948",
        "reporter": "U.S. LEXIS",
        "page": "1986",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "334 U.S. 699",
        "volume": "334",
        "reporter": "U.S.",
        "page": "699",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 S. Ct. 1229",
        "volume": "68",
        "reporter": "S. Ct.",
        "page": "1229",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 2d 1663",
        "volume": "92",
        "reporter": "L. Ed. 2d",
        "page": "1663",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1948 U.S. LEXIS 1986",
        "volume": "1948",
        "reporter": "U.S. LEXIS",
        "page": "1986",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 1663",
        "volume": "92",
        "reporter": "L. Ed.",
        "page": "1663",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "334 U.S. 699",
    "official_selection": {
      "court_class": "scotus",
      "selected": "334 U.S. 699",
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
    "date_created": "2026-07-07T01:38:46Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:38:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:38:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:38:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:38:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "trupiano-v-united-states--104576",
      "to_record_id": "Trupiano v. United States",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Trupiano v. United States

```
<opinion type="majority">
<author id="b772-11">Mr. Justice Murphy</author>
<p id="ASv">delivered the opinion of the Court.</p>
<p id="b772-12">This case adds another chapter to the body of law growing out of the Fourth Amendment to the Constitution of the United States. That Amendment provides: “The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no warrants shall issue, but upon probable cause, supported by oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.” In other words, the Fourth Amendment is a recognition of the fact that in this nation individual liberty depends in large part upon freedom from unreasonable intrusion by those in authority. It is the duty of this Court to give effect to that freedom.</p>
<p id="b773-4"><page-number citation-index="1" label="701">*701</page-number>In January, 1946, the petitioners sought to lease part of the Kell farm in Monmouth County, New Jersey, and to erect a building thereon. Kell suspected that they intended to build and operate an illegal still. He accordingly reported the matter to the appropriate federal authority, the Alcohol Tax Unit of the Bureau of Internal Revenue. The federal agents told Kell to accept the proposition, provided he did nothing to entice or encourage the petitioners into going ahead with their plans and provided he kept the agents informed of all developments. Nilsen, one of the agents, was assigned in February to work on the farm in the disguise of a “dumb farm hand” and to accept work at the still if petitioners should offer it.</p>
<p id="b773-5">Toward the end of March, 1946, Kell agreed with petitioners to let them rent part of his farm for $300 a month. Kell and Nilsen assisted petitioners in the erection of the building, a roughly constructed barn about 200 yards from the Kell farmhouse. Nilsen also assisted in the erection of the still and the vats.</p>
<p id="b773-6">Operation of the still began about May 13, 1946. Nil-sen thereafter worked as “mash man” at a salary of $100 a week, which he turned over to the Government. During this period he was in constant communication with his fellow agents. By prearrangement, he would meet one or more of the agents at various places within a few miles of the Kell <em>farm; </em>at these meetings “the conversation would be about the still building I had assisted in erecting or about the illicit distillery that I was working at on the Kell farm.” On May 20 he met with one of his superior officers and gave him samples of alcohol, several sugar bags, a yeast wrapper and an empty five-gallon can which had been taken from the still premises.</p>
<p id="b773-7">On May 26 Nilsen received a two-way portable radio set from his superiors. He used this set to transmit frequent bulletins on the activities of the petitioners. On <page-number citation-index="1" label="702">*702</page-number>the basis of radio intelligence supplied by Nilsen, a truckload of alcohol was seized on May 31 about an hour after it had left the farm.</p>
<p id="b774-6">At about 9 p. m. in the evening of June 3, 1946, Nilsen radioed his superior that the still operators were awaiting the arrival of a load of sugar and that alcohol was to be taken from the farm when the sugar truck arrived. Nil-sen apparently knew then that a raid was scheduled for that night, for he told Kell during the evening that “tonight is the night.” He radioed at 11 p. m. that the truck had been delayed but that petitioners Roett and Antoniole were at the still.</p>
<p id="b774-7">Three federal agents then drove to within three miles of the farm, at which point they were met by Kell. The remainder of the distance was traversed in Kell’s automobile. They arrived at the farm at about 11:45 p. m. The agents stated that the odor of fermenting mash and the sound of a gasoline motor were noticeable as the car was driven onto the farm premises; the odor became stronger and the noise louder as they alighted from the car and approached the building containing the still. Van De Car, one of the agents, went around one end of the building. Looking through an open door into a dimly lighted interior he could see a still column, a boiler and a gasoline pump in operation. He also saw Antoniole bending down near the pump. He entered the building and placed Antoniole under arrest. Thereupon he “seized the illicit distillery.”</p>
<p id="b774-8">After this arrest and seizure, Van De Car looked about further and observed a large number of five-gallon cans which he later found to contain alcohol and some vats which contained fermenting mash. Another agent, Casey, testified that he could see several of these cans through the open door before he entered; he subsequently counted the cans and found that there were 262 of them. After he entered he saw the remainder of the distillery <page-number citation-index="1" label="703">*703</page-number>equipment, including four large mash vats. The third agent, Gettel, proceeded to a small truck standing in the yard and “searched it thoroughly for papers and things of an evidentiary nature.” It does not appear whether he was successful in his search or whether he took anything from the truck.</p>
<p id="b775-5">A few minutes later Roett was arrested outside the building. Petitioners Trupiano and Riccardelli apparently were arrested later that night by other agents, the place and the circumstances not being revealed by the record before us. In addition, three other persons were arrested that night because of their connections with the illegal operations; one of them, who was unknown to Nilsen, was arrested when he arrived at the farm with a truck loaded with coke.</p>
<p id="b775-6">The agents engaged in this raid without securing a search warrant or warrants of arrest. It is undenied that they had more than adequate opportunity to obtain such warrants before the raid occurred, various federal judges and commissioners being readily available.</p>
<p id="b775-7">All of the persons arrested were charged with various violations of the Internal Revenue Code arising out of their ownership and operation of the distillery. Prior to the return of an indictment against them, the four petitioners filed in the District Court for the District of New Jersey a motion alleging that the federal agents had illegally seized “a still, alcohol, mash and other equipment,” and asking that “all such evidence” be excluded and suppressed at any trial and that “all of the aforesaid property” be returned. The District Court denied the motion after a hearing, holding that the seizure was reasonable and hence constitutional. <span class="citation" data-id="8898850"><a href="/opinion/8911109/united-states-v-trupiano/" aria-description="Citation for case: United States v. Trupiano">70 F. Supp. 764</a></span>. The Circuit Court of Appeals for the Third Circuit affirmed <em>per curiam </em>the order of the District Court. <span class="citation multiple-matches"><a href="/c/F.%202d/163/828/">163 F. 2d 828</a></span>.</p>
<p id="b775-8">Thus we have a case where contraband property was seized by federal agents without a search warrant under <page-number citation-index="1" label="704">*704</page-number>circumstances where such a warrant could easily have been obtained. The Government, however, claims that the failure to secure the warrant has no effect upon the validity of the seizure. Reference is made to the well established right of law enforcement officers to arrest without a warrant for a felony committed in their presence, <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 156-167</a></span>, a right said to be unaffected by the fact that there may have been adequate time to procure a warrant of arrest. Since one of the petitioners, Antoniole, was arrested while engaged in operating an illegal still in the presence of agents of the Alcohol Tax Unit, his arrest was valid under this view even though it occurred without the benefit of a warrant. And since this arrest was valid, the argument is made that the seizure of the contraband open to view at the time of the arrest was also lawful. Reliance is here placed on the long line of cases recognizing that an arresting officer may look around at the time of the arrest and seize those fruits and evidences of crime or those contraband articles which are in plain sight and in his immediate and discernible presence. <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span>; <em>Carroll </em>v. <em>United States, supra, </em>158; <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span>; <em>United States </em>v. <em>Lee, </em><span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/#563" aria-description="Citation for case: United States v. Lee">274 U. S. 559, 563</a></span>; <em>Marron </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#198" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 198-199</a></span>; <em>Go-Bart Co. </em>v. <em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#358" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 358</a></span>; <em>United States </em>v. <em>Lefkowits, </em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#465" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 465</a></span>; <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#150" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 150-151</a></span>.</p>
<p id="b776-5">We sustain the Government’s contention that the arrest of Antoniole was valid. The federal agents had more than adequate cause, based upon the information supplied by Nilsen, to suspect that Antoniole was engaged in felonious activities on the farm premises. Acting on that suspicion, the agents went to the farm and entered onto the premises with the consent of Kell, the owner. There Antoniole was seen through an open doorway by one of the agents to be operating an illegal still, an act <page-number citation-index="1" label="705">*705</page-number>felonious in nature. His arrest was therefore valid on the theory that he was committing a felony in the discernible presence of an agent of the Alcohol Tax Unit, a peace officer of the United States. The absence of a warrant of arrest, even though there was sufficient time to obtain one, does not destroy the validity of an arrest under these circumstances. Warrants of arrest are designed to meet the dangers of unlimited and unreasonable arrests of persons who are not at the moment committing any crime. Those dangers, obviously, are not present where a felony plainly occurs before the eyes of an officer of the law at a place where he is lawfully present. Common sense then dictates that an arrest in that situation is valid despite the failure to obtain a warrant of arrest.</p>
<p id="b777-5">But we cannot agree that the seizure of the contraband property was made in conformity with the requirements of the Fourth Amendment. It is a cardinal rule that, in seizing goods and articles, law enforcement agents must secure and use search warrants wherever reasonably practicable. <em>Carroll </em>v. <em>United States, supra, </em>156; <em>Go-Bart Co. </em>v. <em>United States, supra, </em>358; <em>Taylor </em>v. <em>United States, </em><span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/#6" aria-description="Citation for case: Taylor v. United States">286 U. S. 1, 6</a></span>; <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14-15</a></span>. This rule rests upon the desirability of having magistrates rather than police officers determine when searches and seizures are permissible and what limitations should be placed upon such activities. <em>United States </em>v. <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#464" aria-description="Citation for case: United States v. Lefkowitz"><em>Lefkowitz, supra, </em>464</a></span>. In their understandable zeal to ferret out crime and in the excitement of the capture of a suspected person, officers are less likely to possess the detachment and neutrality with which the constitutional rights of the suspect must be viewed. To provide the necessary security against unreasonable intrusions upon the private lives of individuals, the framers of the Fourth Amendment required adherence to judicial processes wherever possible. And subsequent history has confirmed the wisdom of that requirement.</p>
<p id="b778-5"><page-number citation-index="1" label="706">*706</page-number>The facts of this case do not measure up to the foregoing standard. The agents of the Alcohol Tax Unit knew every detail of the construction and operation of the illegal distillery long before the raid was made. One of them was assigned to work on the farm along with the illicit operators, making it possible for him to secure and report the minutest facts. In cooperation with the farm owner, who served as an informer, this agent was in a position to supply information which could easily have formed the basis for a detailed and effective search warrant. Concededly, there was an abundance of time during which such a warrant could have been secured, even on the night of the raid after the odor and noise of the distillery confirmed their expectations. And the property was not of a type that could have been dismantled and removed before the agents had time to secure a warrant; especially is this so since one of them was on hand at all times to report and guard against such a move. See <em>United States </em>v. <em>Kaplan, </em><span class="citation" data-id="1472811"><a href="/opinion/1472811/united-states-v-kaplan/#871" aria-description="Citation for case: United States v. Kaplan">89 F. 2d 869, 871</a></span>.</p>
<p id="b778-6">What was said in <em>Johnson </em>v. <em>United States, supra, </em>15, is equally applicable here: “No reason is offered for not obtaining a search warrant except the inconvenience to the officers and some slight delay necessary to prepare papers and present the evidence to a magistrate. These are never very convincing reasons and, in these circumstances, certainly are not enough to by-pass the consti-tutionál requirement. ... If the officers in this case were excused from the constitutional duty of presenting their evidence to a magistrate, it is difficult to think of a case in which it should be required.”</p>
<p id="b778-7">And so when the agents of the Alcohol Tax Unit decided to dispense with a search warrant <em>and to </em>take matters into their own hands, they did precisely what the Fourth Amendment was designed to outlaw. Uninhibited by any limitations that might have been contained in a warrant, they descended upon the distillery in a mid<page-number citation-index="1" label="707">*707</page-number>night raid. Nothing circumscribed their activities on that raid except their own good senses, which the authors of the Amendment deemed insufficient to justify a search or seizure except in exceptional circumstances not here present. The limitless possibilities afforded by the absence of a warrant were epitomized by the one agent who admitted searching “thoroughly” a small truck parked in the farmyard for items of an evidentiary character. The fact that they actually seized only contraband property, which would doubtless have been described in a warrant had one been issued, does not detract from the illegality of the seizure. See Amos v. <em>United States, </em><span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span>; <em>Byars </em>v. <em>United States, </em><span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U. S. 28</a></span>; <em>Taylor </em>v. <em>United States, supra.</em></p>
<p id="b779-5">Moreover, the proximity of the contraband property to the person of Antoniole at the moment of his arrest was a fortuitous circumstance which was inadequate to legalize the seizure. As we have seen, the existence of this property and the desirability of seizing it were known to the agents long before the seizure and formed one of the main purposes of the raid. Likewise, the arrest of An-toniole and the other petitioners in connection with the illicit operations was a foreseeable event motivating the raid. But the precise location of the petitioners at the time of their arrest had no relation to the foreseeability or necessity of the seizure. The practicability of obtaining a search warrant did not turn upon whether Antoniole and the others were within the distillery building when arrested or upon whether they were then engaged in operating the illicit equipment. Antoniole just happened to be working amid the contraband surroundings at 11:45 p. m. on the night in question, while the other three petitioners chanced to be some place else. But Antoniole might well have been outside the building at that particular time. If that had been the case and he had been arrested in the farmyard, the entire argument advanced <page-number citation-index="1" label="708">*708</page-number>by the Government in support of the seizure without warrant would collapse. We do not believe that the applicability of the Fourth Amendment to the facts of this case depends upon such a fortuitous factor as the precise location of Antoniole at the time of the raid.</p>
<p id="b780-5">In other words, the presence or absence of an arrestee at the exact time and place of a foreseeable and anticipated seizure does not determine the validity of that seizure if it occurs without a warrant. Rather the test is the apparent need for summary seizure, a test which clearly is not satisfied by the facts before us.</p>
<p id="b780-6">A search or seizure without a warrant as an incident to a lawful arrest has always been considered to be a strictly limited right. It grows out of the inherent necessities of the situation at the time of the arrest. But there must be something more in the way of necessity than merely a lawful arrest. The mere fact that there is a valid arrest does not <em>ipso facto </em>legalize a search or seizure without a warrant. <em>Carroll </em>v. <em>United States, supra, </em>158. Otherwise the exception swallows the general principle, making a search warrant completely unnecessary wherever there is a lawful arrest. And so there must be some other factor in the situation that would make it unreasonable or impracticable to require the arresting officer to equip himself with a search warrant. In the case before us, however, no reason whatever has been shown why the arresting officers could not have armed themselves during all the weeks of their surveillance of the locus with a duly obtained search warrant — no reason, that is, except indifference to the legal process for search and seizure which the Constitution contemplated.</p>
<p id="b780-7">We do not take occasion here to reexamine the situation involved in <em>Harris </em>v. <em>United States, supra. </em>The instant case relates only to the seizure of contraband the existence and precise nature and location of which the law enforcement officers were aware long before making the lawful arrest. That circumstance was wholly lacking in the <page-number citation-index="1" label="709">*709</page-number><em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>case, which was concerned with the permissible scope of a general search without a warrant as an incident to a lawful arrest. Moreover, the <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>case dealt with the seizure of Government property which could not have been the subject of a prior search warrant, it having been found unexpectedly during the course of a search. In contrast, the contraband seized in this case could easily have been specified in a prior search warrant. These factual differences may or may not be of significance so far as general principles are concerned. But the differences are enough to justify confining ourselves to the precise facts of this case, leaving it to another day to test the <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>situation by the rule that search warrants are to be obtained and used wherever reasonably practicable.</p>
<p id="b781-5">What we have here is a set of facts governed by a principle indistinguishable from that recognized and applied in <em>Taylor </em>v. <em>United States, supra. </em>The Court there held that the seizure of illicit whiskey was unreasonable, however well-grounded the suspicions of the federal agents, where there was an abundant opportunity to obtain a search warrant and to proceed in an orderly, judicial way. True, the <em><span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">Taylor</a></span> </em>case did not involve a seizure in connection with an arrest. And the officers there made an unlawful entry onto the premises. But those factors had no relation to the practicability of obtaining a search warrant before making the seizure. It was the time element and the foreseeability of the need for a search and seizure that made the warrant essential. The <em><span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">Taylor</a></span> </em>case accordingly makes plain the illegality of the seizure in the instant proceeding.</p>
<p id="b781-6">The Fourth Amendment was designed to protect both the innocent and the guilty from unreasonable intrusions upon their right of privacy while leaving adequate room for the necessary processes of law enforcement. The people of the United States insisted on writing the Fourth Amendment into the Constitution because sad experience had taught them that the right to search and <page-number citation-index="1" label="710">*710</page-number>seize should not be left to the mere discretion of the police, but should as a matter of principle be subjected to the requirement of previous judicial sanction wherever possible. The effective operation of government, however, could hardly be embarrassed by the requirement that arresting officers who have three weeks or more within which to secure the authorization of judicial authority for making search and seizure should secure such authority and not be left to their own discretion as to what is to be searched and what is to be seized. Such a requirement partakes of the very essence of the orderly and effective administration of the law.</p>
<p id="b782-4">It is a mistake to assume that a search warrant in these circumstances would contribute nothing to the preservation of the rights protected by the Fourth Amendment. A search warrant must describe with particularity the place to be searched and the things to be seized. Without such a warrant, however, officers are free to determine for themselves the extent of their search and the precise objects to be seized. This is no small difference. It is a difference upon which depends much of the potency of the right of privacy. And it is a difference that must be preserved even where contraband articles are seized in connection with a valid arrest.</p>
<p id="b782-5">It follows that it was error to refuse petitioners’ motion to exclude and suppress the property which was improperly seized. But since this property was contraband, they have no right to have it returned to them.</p>
<p id="b782-6">
<em>Reversed.</em>
</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Turner v. United States.json  (`lake-record`, 4 assertions)

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
{"assertion_id": "72d0d9cf501187eb", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Turner v. United States"}, "payload": {"all": [{"cite": "582 U.S. 313", "page": "313", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "582"}, {"cite": "2017 U.S. LEXIS 4041", "page": "4041", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2017"}, {"cite": "137 S. Ct. 1885", "page": "1885", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "137"}, {"cite": "198 L. Ed. 2d 443", "page": "443", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "198"}, {"cite": "26 Fla. L. Weekly Fed. S 700", "page": "700", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "26"}, {"cite": "85 U.S.L.W. 4488", "page": "4488", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "85"}, {"cite": "2017 WL 2674152", "page": "2674152", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2017"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Turner v. United States"}}
{"assertion_id": "7d6377a6dd9208d4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1894", "record_id": "Turner v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1894", "pinpoint_status": "slip-only", "quote": "it is too little, too weak, or too distant from the main evidentiary points to meet *Brady*'s standards.", "quote_fidelity": "mismatch", "record_id": "Turner v. United States", "star_marker": null}}
{"assertion_id": "d2a9384b14f15f30", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1893", "record_id": "Turner v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1893", "pinpoint_status": "slip-only", "quote": "under *Brady v. Maryland*, such that its suppression deprived the defendants of a fair trial. ## Rule The materiality test is demanding and is judged against the whole record:", "quote_fidelity": "mismatch", "record_id": "Turner v. United States", "star_marker": null}}
{"assertion_id": "41a3ec45384eeb88", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Turner v. United States"}, "payload": {"as_of_content": "2017-06-22", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Turner v. United States", "scope_note": "Good law; applies the Brady/Bagley materiality standard and finds no violation on the record.", "varies_by_point": false}}
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
