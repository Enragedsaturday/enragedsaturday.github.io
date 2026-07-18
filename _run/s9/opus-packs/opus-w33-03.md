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

## GROUP: content/cases/Lange v. California.md  (`case`, 6 assertions)

### content_page

```
---
title: "Lange v. California"
type: case
citation: "594 U.S. 295 (2021)"
parallel_cite: ""
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2021
date_decided: 2021-06-23
docket: 20-18
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2021-06-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Lange v. California
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4894407/lange-v-california/"
  cluster_id: 4894407
  opinion_id: 4698186
  identity_checked: true
homes:
  - page: "[[Exigent Circumstances and Hot Pursuit]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Arrest in the Home]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Santana]]", "[[Welsh v. Wisconsin]]", "[[Kentucky v. King]]", "[[Payton v. New York]]"]
aliases: []
tags: ["case", "fourth-amendment", "exigent-circumstances", "hot-pursuit", "misdemeanor", "home-entry"]
holding: "Pursuit of a fleeing MISDEMEANOR suspect does not categorically justify warrantless home entry; courts apply a case-by-case exigency…"
lake:
  record_id: Lange v. California
  status: verified
  projected_at: 2026-07-09
---

# Lange v. California

*594 U.S. 295 (2021)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A California highway patrol officer began following Lange, who was playing loud music and honking, and turned on his overhead lights to signal a stop when Lange was about a hundred feet from home. Rather than stopping, Lange drove into his attached garage. The officer followed him in, questioned him, observed signs of intoxication, and a later blood test showed Lange was over the legal limit. He was charged with the misdemeanor of driving under the influence.

## Issue
Whether the pursuit of a fleeing misdemeanor suspect categorically (always) qualifies as an exigent circumstance justifying a warrantless entry into the home.

## Rule
No — there is no categorical rule; [[Exigent Circumstances and Hot Pursuit|exigency]] is judged case by case. "The question presented here is whether the pursuit of a fleeing misdemeanor suspect always — or more legally put, categorically — qualifies as an exigent circumstance. We hold it does not." — *Lange v. California*, 594 U.S. 295 (2021) (slip op., at 1). ^pin-op1

"A great many misdemeanor pursuits involve exigencies allowing warrantless entry. But whether a given one does so turns on the particular facts of the case." — *Id.* (slip op., at [1](https://www.courtlistener.com/opinion/4894407/lange-v-california/#:~:text=A%20great%20many%20misdemeanor%20pursuits)). ^pin-op1a

## Application
The California Court of Appeal had upheld the entry on the theory that pursuit of a suspected misdemeanant is always permissible under the exigent-circumstances exception. Because that categorical approach was wrong — flight for a misdemeanor does not automatically create an [[Exigent Circumstances and Hot Pursuit|exigency]] — the officer's warrantless entry into Lange's garage could not be sustained on a categorical basis. The judgment was [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]] so the lower court could decide, on the totality of these particular circumstances, whether an [[Exigent Circumstances and Hot Pursuit|exigency]] (such as imminent harm or destruction of evidence) actually justified the entry.

## Conclusion
[[Reading and Citing Cases#vacated|Vacated]] and [[Reading and Citing Cases#on-remand|remanded]]: warrantless home entry in pursuit of a fleeing misdemeanant requires a case-specific [[Exigent Circumstances and Hot Pursuit|exigency]], not a categorical hot-pursuit rule.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Lange* **cabins** the hot-pursuit [[Exigent Circumstances and Hot Pursuit|exigency]] for misdemeanors, distinguishing the felony-flight situation addressed in [[United States v. Santana]] and building on [[Welsh v. Wisconsin]]'s reluctance to find [[Exigent Circumstances and Hot Pursuit|exigency]] for minor offenses. It applies [[Kentucky v. King]]'s case-specific "compelling need" framing to the misdemeanor-pursuit context.

## Appears on
- [[Exigent Circumstances and Hot Pursuit]] — *Key — Progeny / Refinement*
- [[Arrest in the Home]] — *Key — Progeny / Refinement*

## Sources
- *Lange v. California*, 594 U.S. 295 (2021) — https://www.courtlistener.com/opinion/4894407/lange-v-california/ — pinpoint given as slip-opinion page (slip op., at 1); CourtListener carries the slip opinion (cluster 4894407 → opinion 4698186).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d3ce8922dfad2b06", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "594 U.S. 295 (2021)", "court": "U.S. Supreme Court", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Lange v. California", "year": "2021"}}
{"assertion_id": "05b68dee43cd4682", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Key — Progeny / Refinement", "title": "Lange v. California"}}
{"assertion_id": "5edd0338f85e8f36", "dimension": "support", "kind": "home_role", "locator": {"home": "Exigent Circumstances and Hot Pursuit"}, "payload": {"home": "Exigent Circumstances and Hot Pursuit", "role": "Key — Progeny / Refinement", "title": "Lange v. California"}}
{"assertion_id": "f4e75f92b9c5a485", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Pursuit of a fleeing MISDEMEANOR suspect does not categorically justify warrantless home entry; courts apply a case-by-case exigency…", "title": "Lange v. California"}}
{"assertion_id": "1eb96e4bcbdc7130", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Lange v. California"}}
{"assertion_id": "3b8684db9ecb57b4", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2021-06-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Lange v. California", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Lange v. California", "varies_by_point": "false"}}
```

### lake record — Lange v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Lange v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Lange v. California",
    "case_name_short": "Lange",
    "case_name_full": "",
    "input_case_name": "Lange v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2021-06-23",
    "year": 2021,
    "docket": "20-18",
    "cluster_id": 4894407,
    "lead_opinion_id": 4698186,
    "sibling_ids": [
      4698186
    ],
    "absolute_url": "/opinion/4894407/lange-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 4894054,
        "score": 120,
        "case_name": "Lange v. California"
      },
      {
        "cluster_id": 4894406,
        "score": 20,
        "case_name": "Lange v. California"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "594 U.S. 295",
      "volume": "594",
      "reporter": "U.S.",
      "page": "295",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "594 U.S. 295",
        "volume": "594",
        "reporter": "U.S.",
        "page": "295",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "594 U.S. 295",
    "official_selection": {
      "court_class": "scotus",
      "selected": "594 U.S. 295",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op1",
      "page": null,
      "quote": "--- # Lange v. California *594 U.S. 295 (2021)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A California highway patrol officer began following Lange, who was playing loud music and honking, and turned on his overhead lights to signal a stop when Lange was about a hundred feet from home. Rather than stopping, Lange drove into his attached garage. The officer followed him in, questioned him, observed signs of intoxication, and a later blood test showed Lange was over the legal limit. He was charged with the misdemeanor of driving under the influence. ## Issue Whether the pursuit of a fleeing misdemeanor suspect categorically (always) qualifies as an exigent circumstance justifying a warrantless entry into the home. ## Rule No \u2014 there is no categorical rule; exigency is judged case by case.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op1a",
      "page": null,
      "quote": "A great many misdemeanor pursuits involve exigencies allowing warrantless entry. But whether a given one does so turns on the particular facts of the case.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 7765,
      "fragment": "#:~:text=A%20great%20many%20misdemeanor%20pursuits",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2021-06-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Lange v. California",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4698186) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
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
      },
      "lane2_top_cited": {
        "query": "cites:(4698186)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(4698186)",
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
    "complete_query": "cites:(4698186)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4698186,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/lange-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4698186,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 118180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 131146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 612969,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 856347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 858288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 1140090,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 1575738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 1759759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 1782114,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 1936367,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 1985786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 2641101,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 2692132,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 2693474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 2774855,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 2801435,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 2807378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 2831232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 3214776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 3216391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 3217227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 3372875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 4257309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 6784219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 7263677,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 7268856,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 8052300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 8185477,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9413217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9420240,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9421667,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9423752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9425474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9426490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9427384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9427853,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9427937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9428299,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9428436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9428641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9429117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9429597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9429647,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9429728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9429766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9429990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9431339,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9431933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9431979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9432255,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9433685,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9433881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9434039,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9434645,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9434934,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9434949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9434962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9435077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9435233,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9435413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9441559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9742448,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9795084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9798884,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9841975,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4698186,
        "cited_id": 9871729,
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
    "date_created": "2026-07-05T10:46:31Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:46:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:46:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:47:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:46:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Lange v. California

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

                         LANGE v. CALIFORNIA

    CERTIORARI TO THE COURT OF APPEAL OF CALIFORNIA,
                FIRST APPELLATE DISTRICT

     No. 20–18. Argued February 24, 2021—Decided June 23, 2021
This case arises from a police officer’s warrantless entry into petitioner
  Arthur Lange’s garage. Lange drove by a California highway patrol
  officer while playing loud music and honking his horn. The officer be-
  gan to follow Lange and soon after turned on his overhead lights to
  signal that Lange should pull over. Rather than stopping, Lange drove
  a short distance to his driveway and entered his attached garage. The
  officer followed Lange into the garage. He questioned Lange and, after
  observing signs of intoxication, put him through field sobriety tests. A
  later blood test showed that Lange’s blood-alcohol content was three
  times the legal limit.
     The State charged Lange with the misdemeanor of driving under the
  influence. Lange moved to suppress the evidence obtained after the
  officer entered his garage, arguing that the warrantless entry violated
  the Fourth Amendment. The Superior Court denied Lange’s motion,
  and its appellate division affirmed. The California Court of Appeal
  also affirmed. It concluded that Lange’s failure to pull over when the
  officer flashed his lights created probable cause to arrest Lange for the
  misdemeanor of failing to comply with a police signal. And it stated
  that Lange could not defeat an arrest begun in a public place by re-
  treating into his home. The pursuit of a suspected misdemeanant, the
  court held, is always permissible under the exigent-circumstances ex-
  ception to the warrant requirement. The California Supreme Court
  denied review.
Held: Under the Fourth Amendment, pursuit of a fleeing misdemeanor
 suspect does not always—that is, categorically—justify a warrantless
 entry into a home. Pp. 3–16.
    (a) The Court’s Fourth Amendment precedents counsel in favor of a
2                         LANGE v. CALIFORNIA

                                  Syllabus

    case-by-case assessment of exigency when deciding whether a sus-
    pected misdemeanant’s flight justifies a warrantless home entry. The
    Fourth Amendment ordinarily requires that a law enforcement officer
    obtain a judicial warrant before entering a home without permission.
    Riley v. California, 573 U. S. 373, 382. But an officer may make a
    warrantless entry when “the exigencies of the situation,” considered in
    a case-specific way, create “a compelling need for official action and no
    time to secure a warrant.” Kentucky v. King, 563 U. S. 452, 460; Mis-
    souri v. McNeely, 569 U. S. 141, 149. The Court has found that such
    exigencies may exist when an officer must act to prevent imminent
    injury, the destruction of evidence, or a suspect’s escape.
       The amicus contends that a suspect’s flight always supplies the exi-
    gency needed to justify a warrantless home entry and that the Court
    endorsed such a categorical approach in United States v. Santana, 427
    U. S. 38. The Court disagrees. In upholding a warrantless entry made
    during a “hot pursuit” of a felony suspect, the Court stated that San-
    tana’s “act of retreating into her house” could “not defeat an arrest”
    that had “been set in motion in a public place.” Id., at 42–43. Even
    assuming that Santana treated fleeing-felon cases categorically, that
    statement still does not establish a flat rule permitting warrant-
    less home entry whenever a police officer pursues a fleeing misde-
    meanant. Santana did not resolve the issue of misdemeanor pursuit;
    as the Court noted in a later case, “the law regarding warrantless en-
    try in hot pursuit of a fleeing misdemeanant is not clearly es-
    tablished” one way or the other. Stanton v. Sims, 571 U. S. 3, 8, 10.
       Misdemeanors run the gamut of seriousness, and they may be mi-
    nor. States tend to apply the misdemeanor label to less violent and
    less dangerous crimes. The Court has held that when a minor offense
    (and no flight) is involved, police officers do not usually face the kind
    of emergency that can justify a warrantless home entry. See Welsh v.
    Wisconsin, 466 U. S. 740, 742–743. Add a suspect’s flight and the cal-
    culus changes—but not enough to justify a categorical rule. In many
    cases, flight creates a need for police to act swiftly. But no evidence
    suggests that every case of misdemeanor flight creates such a need.
       The Court’s Fourth Amendment precedents thus point toward as-
    sessing case by case the exigencies arising from misdemeanants’ flight.
    When the totality of circumstances shows an emergency—a need to act
    before it is possible to get a warrant—the police may act without wait-
    ing. Those circumstances include the flight itself. But pursuit of a
    misdemeanant does not trigger a categorical rule allowing a warrant-
    less home entry. Pp. 3–12.
       (b) The common law in place at the Constitution’s founding similarly
    does not support a categorical rule allowing warrantless home entry
    whenever a misdemeanant flees. Like the Court’s modern precedents,
                     Cite as: 594 U. S. ____ (2021)                     3

                                Syllabus

  the common law afforded the home strong protection from government
  intrusion and it generally required a warrant before a government of-
  ficial could enter the home. There was an oft-discussed exception: An
  officer, according to the common-law treatises, could enter a house to
  pursue a felon. But in the misdemeanor context, officers had more
  limited authority to intrude on a fleeing suspect’s home. The commen-
  tators generally agreed that the authority turned on the circum-
  stances; none suggested a rule authorizing warrantless entry in every
  misdemeanor-pursuit case. In short, the common law did not have—
  and does not support—a categorical rule allowing warrantless home
  entry when a suspected misdemeanant flees. Pp. 12–16.
Vacated and remanded.

   KAGAN, J., delivered the opinion of the Court, in which BREYER, SO-
TOMAYOR,    GORSUCH, KAVANAUGH, and BARRETT, JJ., joined, and in which
THOMAS, J., joined as to all but Part II–A. KAVANAUGH, J., filed a concur-
ring opinion. THOMAS, J., filed an opinion concurring in part and concur-
ring in the judgment, in which KAVANAUGH, J., joined as to Part II. ROB-
ERTS, C. J., filed an opinion concurring in the judgment, in which ALITO,
J., joined.
                        Cite as: 594 U. S. ____ (2021)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 20–18
                                    _________________


     ARTHUR GREGORY LANGE, PETITIONER v.
                CALIFORNIA
   ON WRIT OF CERTIORARI TO THE COURT OF APPEAL OF
        CALIFORNIA, FIRST APPELLATE DISTRICT
                                  [June 23, 2021]

  JUSTICE KAGAN delivered the opinion of the Court.
  The Fourth Amendment ordinarily requires that police
officers get a warrant before entering a home without per-
mission. But an officer may make a warrantless entry
when “the exigencies of the situation” create a compelling
law enforcement need. Kentucky v. King, 563 U. S. 452, 460
(2011). The question presented here is whether the pursuit
of a fleeing misdemeanor suspect always—or more legally
put, categorically—qualifies as an exigent circumstance.
We hold it does not. A great many misdemeanor pursuits
involve exigencies allowing warrantless entry.          But
whether a given one does so turns on the particular facts of
the case.
                             I
  This case began when petitioner Arthur Lange drove past
a California highway patrol officer in Sonoma. Lange, it is
fair to say, was asking for attention: He was listening to
loud music with his windows down and repeatedly honking
his horn. The officer began to tail Lange, and soon after-
ward turned on his overhead lights to signal that Lange
should pull over. By that time, though, Lange was only
2                   LANGE v. CALIFORNIA

                      Opinion of the Court

about a hundred feet (some four-seconds drive) from his
home. Rather than stopping, Lange continued to his drive-
way and entered his attached garage. The officer followed
Lange in and began questioning him. Observing signs of
intoxication, the officer put Lange through field sobriety
tests. Lange did not do well, and a later blood test showed
that his blood-alcohol content was more than three times
the legal limit.
  The State charged Lange with the misdemeanor of driv-
ing under the influence of alcohol, plus a (lower-level) noise
infraction. Lange moved to suppress all evidence obtained
after the officer entered his garage, arguing that the war-
rantless entry had violated the Fourth Amendment. The
State contested the motion. It contended that the officer
had probable cause to arrest Lange for the misdemeanor of
failing to comply with a police signal. See, e.g., Cal. Veh.
Code Ann. §2800(a) (West 2015) (making it a misdemeanor
to “willfully fail or refuse to comply with a lawful order, sig-
nal, or direction of a peace officer”). And it argued that the
pursuit of a suspected misdemeanant always qualifies as an
exigent circumstance authorizing a warrantless home en-
try. The Superior Court denied Lange’s motion, and its ap-
pellate division affirmed.
  The California Court of Appeal also affirmed, accepting
the State’s argument in full. 2019 WL 5654385, *1 (2019).
In the court’s view, Lange’s “fail[ure] to immediately pull
over” when the officer flashed his lights created probable
cause to arrest him for a misdemeanor. Id., at *7. And a
misdemeanor suspect, the court stated, could “not defeat an
arrest which has been set in motion in a public place” by
“retreat[ing] into” a house or other “private place.” See id.,
at *6–*8 (internal quotation marks omitted). Rather, an
“officer’s ‘hot pursuit’ into the house to prevent the suspect
from frustrating the arrest” is always permissible under the
exigent-circumstances “exception to the warrant require-
ment.” Id., at *8 (some internal quotation marks omitted).
                      Cite as: 594 U. S. ____ (2021)                     3

                          Opinion of the Court

That flat rule resolved the matter: “Because the officer was
in hot pursuit” of a misdemeanor suspect, “the officer’s war-
rantless entry into [the suspect’s] driveway and garage
[was] lawful.” Id., at *9. The California Supreme Court
denied review.
   Courts are divided over whether the Fourth Amendment
always permits an officer to enter a home without a warrant
in pursuit of a fleeing misdemeanor suspect. Some courts
have adopted such a categorical rule, while others have re-
quired a case-specific showing of exigency.1 We granted cer-
tiorari, 592 U. S. ___ (2020), to resolve the conflict. Because
California abandoned its defense of the categorical rule ap-
plied below in its response to Lange’s petition, we appointed
Amanda Rice as amicus curiae to defend the Court of Ap-
peal’s judgment. She has ably discharged her responsibili-
ties.
                              II
  The Fourth Amendment provides that “[t]he right of the
people to be secure in their persons, houses, papers, and ef-
fects, against unreasonable searches and seizures, shall not
be violated.” As that text makes clear, “the ultimate touch-
stone of the Fourth Amendment is ‘reasonableness.’ ”
Brigham City v. Stuart, 547 U. S. 398, 403 (2006). That

——————
  1 Compare, e.g., 2019 WL 5654385, *7–*8 (case below) (applying a cat-

egorical rule); Bismarck v. Brekhus, 2018 ND 84, ¶ 27, 908 N. W. 2d 715,
719–720 (same); Commonwealth v. Jewett, 471 Mass. 624, 634–635, 31
N. E. 3d 1079, 1089 (2015) (same); People v. Wear, 229 Ill. 2d 545, 568,
571, 893 N. E. 2d 631, 644–646 (2008) (same); Middletown v. Flinchum,
95 Ohio St. 3d 43, 44–45, 765 N. E. 2d 330, 332 (2002) (same); State v.
Ricci, 144 N. H. 241, 244–245, 739 A. 2d 404, 407–408 (1999) (same),
with, e.g., State v. Markus, 211 So. 3d 894, 906–907 (Fla. 2017) (requiring
a case-specific showing); Mascorro v. Billings, 656 F. 3d 1198, 1207
(CA10 2011) (same); Butler v. State, 309 Ark. 211, 216–217, 829 S. W. 2d
412, 415 (1992) (same); State v. Bolte, 115 N. J. 579, 597–598, 560 A. 2d
644, 654–655 (1989) (same); see also Stanton v. Sims, 571 U. S. 3, 6–7
(2013) (per curiam) (noting the split).
4                  LANGE v. CALIFORNIA

                     Opinion of the Court

standard “generally requires the obtaining of a judicial war-
rant” before a law enforcement officer can enter a home
without permission. Riley v. California, 573 U. S. 373, 382
(2014) (internal quotation marks omitted). But not always:
The “warrant requirement is subject to certain exceptions.”
Brigham City, 547 U. S., at 403.
   One important exception is for exigent circumstances. It
applies when “the exigencies of the situation make the
needs of law enforcement so compelling that [a] warrantless
search is objectively reasonable.” King, 563 U. S., at 460
(internal quotation marks omitted). The exception enables
law enforcement officers to handle “emergenc[ies]”—situa-
tions presenting a “compelling need for official action and
no time to secure a warrant.” Riley, 573 U. S., at 402; Mis-
souri v. McNeely, 569 U. S. 141, 149 (2013). Over the years,
this Court has identified several such exigencies. An of-
ficer, for example, may “enter a home without a warrant to
render emergency assistance to an injured occupant[,] to
protect an occupant from imminent injury,” or to ensure his
own safety. Brigham City, 547 U. S., at 403; Riley, 573
U. S., at 388. So too, the police may make a warrantless
entry to “prevent the imminent destruction of evidence” or
to “prevent a suspect’s escape.” Brigham City, 547 U. S., at
403; Minnesota v. Olson, 495 U. S. 91, 100 (1990) (internal
quotation marks omitted). In those circumstances, the de-
lay required to obtain a warrant would bring about “some
real immediate and serious consequences”—and so the ab-
sence of a warrant is excused. Welsh v. Wisconsin, 466 U. S.
740, 751 (1984) (quoting McDonald v. United States, 335
U. S. 451, 460 (1948) (Jackson, J., concurring)).
   Our cases have generally applied the exigent-circumstances
exception on a “case-by-case basis.” Birchfield v. North Da-
kota, 579 U. S. 438, ___ (2016) (slip op., at 16). The excep-
tion “requires a court to examine whether an emergency
justified a warrantless search in each particular case.” Ri-
ley, 573 U. S., at 402. Or put more curtly, the exception is
                  Cite as: 594 U. S. ____ (2021)              5

                      Opinion of the Court

“case-specific.” Id., at 388. That approach reflects the na-
ture of emergencies. Whether a “now or never situation”
actually exists—whether an officer has “no time to secure a
warrant”—depends upon facts on the ground. Id., at 391
(internal quotation marks omitted); McNeely, 569 U. S., at
149 (internal quotation marks omitted). So the issue, we
have thought, is most naturally considered by “look[ing] to
the totality of circumstances” confronting the officer as he
decides to make a warrantless entry. Id., at 149.
   The question here is whether to use that approach, or in-
stead apply a categorical warrant exception, when a sus-
pected misdemeanant flees from police into his home. Un-
der the usual case-specific view, an officer can follow the
misdemeanant when, but only when, an exigency—for ex-
ample, the need to prevent destruction of evidence—allows
insufficient time to get a warrant. The appointed amicus
asks us to replace that case-by-case assessment with a flat
(and sweeping) rule finding exigency in every case of mis-
demeanor pursuit. In her view, those “entries are categori-
cally reasonable, regardless of whether” any risk of harm
(like, again, destruction of evidence) “materializes in a par-
ticular case.” Brief for Court-Appointed Amicus Curiae 31.
The fact of flight from the officer, she says, is itself enough
to justify a warrantless entry. (The principal concurrence
agrees.) To assess that position, we look (as we often do in
Fourth Amendment cases) both to this Court’s precedents
and to the common-law practices familiar to the Framers.
                               A
   The place to start is with our often-stated view of the con-
stitutional interest at stake: the sanctity of a person’s living
space. “[W]hen it comes to the Fourth Amendment, the
home is first among equals.” Florida v. Jardines, 569 U. S.
1, 6 (2013). At the Amendment’s “very core,” we have said,
“stands the right of a man to retreat into his own home and
there be free from unreasonable government intrusion.”
6                   LANGE v. CALIFORNIA

                      Opinion of the Court

Collins v. Virginia, 584 U. S. ___, ___ (2018) (slip op., at 5)
(internal quotation marks omitted). Or again: “Freedom”
in one’s own “dwelling is the archetype of the privacy pro-
tection secured by the Fourth Amendment”; conversely,
“physical entry of the home is the chief evil against which
[it] is directed.” Payton v. New York, 445 U. S. 573, 585,
587 (1980) (internal quotation marks omitted).             The
Amendment thus “draw[s] a firm line at the entrance to the
house.” Id., at 590. What lies behind that line is of course
not inviolable. An officer may always enter a home with a
proper warrant. And as just described, exigent circum-
stances allow even warrantless intrusions. See ibid.; supra,
at 4. But the contours of that or any other warrant excep-
tion permitting home entry are “jealously and carefully
drawn,” in keeping with the “centuries-old principle” that
the “home is entitled to special protection.” Georgia v. Ran-
dolph, 547 U. S. 103, 109, 115 (2006) (internal quotation
marks omitted); see Caniglia v. Strom, 593 U. S. ___, ___
(2021) (slip op., at 4) (“[T]his Court has repeatedly declined
to expand the scope” of “exceptions to the warrant require-
ment to permit warrantless entry into the home”). So we
are not eager—more the reverse—to print a new permission
slip for entering the home without a warrant.
   The amicus argues, though, that we have already created
the rule she advocates. In United States v. Santana, 427
U. S. 38 (1976), the main case she relies on, police officers
drove to Dominga Santana’s house with probable cause to
think that Santana was dealing drugs, a felony under the
applicable law. When the officers pulled up, they saw San-
tana standing in her home’s open doorway, some 15 feet
away. As they got out of the van and yelled “police,” San-
tana “retreated into [the house’s] vestibule.” Id., at 40. The
officers followed her in, and discovered heroin. We upheld
the warrantless entry as one involving a police “hot pur-
suit,” even though the chase “ended almost as soon as it be-
gan.” Id., at 43. Citing “a realistic expectation that any
                  Cite as: 594 U. S. ____ (2021)            7

                      Opinion of the Court

delay would result in destruction of evidence,” we recog-
nized the officers’ “need to act quickly.” Id., at 42–43. But
we framed our holding in broader terms: Santana’s “act of
retreating into her house,” we stated, could “not defeat an
arrest” that had “been set in motion in a public place.” Ibid.
The amicus takes that statement to support a flat rule per-
mitting warrantless home entry when police officers (with
probable cause) are pursuing any suspect—whether a felon
or a misdemeanant. See Brief for Amicus Curiae 11, 26.
For support, she points to a number of later decisions de-
scribing Santana in dicta as allowing warrantless home en-
tries when police are “in ‘hot pursuit’ of a fugitive” or “a
fleeing suspect.” E.g., Steagald v. United States, 451 U. S.
204, 221 (1981); King, 563 U. S., at 460. The concurrence
echoes her arguments.
   We disagree with that broad understanding of Santana,
as we have suggested before. In rejecting the amicus’s view,
we see no need to consider Lange’s counterargument that
Santana did not establish any categorical rule—even one
for fleeing felons. See Brief for Petitioner 7, 25 (contending
that Santana is “entirely consistent” with “case-by-case ex-
igency analysis” because the Court “carefully based [its]
holding on [the] specific facts” and “circumstances”). As-
suming Santana treated fleeing-felon cases categorically
(that is, as always presenting exigent circumstances allow-
ing warrantless entry), see, e.g., Stanton v. Sims, 571 U. S.
3, 8 (2013) (per curiam); McNeely, 569 U. S., at 149; King,
563 U. S., at 450, it still said nothing about fleeing misde-
meanants. We said as much in Stanton, when we approved
qualified immunity for an officer who had pursued a sus-
pected misdemeanant into a home. Describing the same
split of authority we took this case to address, we stated
that “the law regarding warrantless entry in hot pursuit of
a fleeing misdemeanant is not clearly established” (so that
the officer could not be held liable for damages). 571 U. S.,
at 6, 10. In other words, we found that neither Santana nor
8                    LANGE v. CALIFORNIA

                       Opinion of the Court

any other decision had resolved the matter one way or the
other. And we left things in that unsettled state. See 571
U. S., at 10. Santana, we noted, addressed a police pursuit
“involv[ing] a felony suspect,” 571 U. S., at 9; whether the
same approach governed a misdemeanor chase was an is-
sue for a future case.
   Key to resolving that issue are two facts about misde-
meanors: They vary widely, but they may be (in a word)
“minor.” Welsh, 466 U. S., at 750. In California and else-
where, misdemeanors run the gamut of seriousness. As the
amicus notes, some involve violence. California, for exam-
ple, classifies as misdemeanors various forms of assault.
See Cal. Penal Code Ann. §241 (West Cum. Supp. 2021);
Brief for Amicus Curiae 15a–16a. And across the country,
“many perpetrators of domestic violence are charged with
misdemeanors,” despite “the harmfulness of their conduct.”
Voisine v. United States, 579 U. S. 686, ___ (2016) (slip op.,
at 1). So “a ‘felon’ is” not always “more dangerous than a
misdemeanant.” Tennessee v. Garner, 471 U. S. 1, 14
(1985). But calling an offense a misdemeanor usually limits
prison time to one year. See 1 W. LaFave, J. Israel, N. King,
& O. Kerr, Criminal Procedure §1.8(c) (4th ed. Supp. 2020).
States thus tend to apply that label to less violent and less
dangerous crimes. In California, it is a misdemeanor to lit-
ter on a public beach. See Cal. Penal Code Ann. §374.7(a)
(2020). And to “negligently cut” a plant “growing upon pub-
lic land.” §384a(a)(2), (f ). And to “willfully disturb[ ] an-
other person by loud and unreasonable noise.” §415(2).
And (last one) to “artificially color[ ] any live chicks [or] rab-
bits.” §599(b). In forbidding such conduct, California is no
outlier. Most States count as misdemeanors such offenses
as traffic violations, public intoxication, and disorderly con-
duct. See, e.g., Tex. Transp. Code Ann. §545.413(a), (d)
(West 2011) (driving without a seatbelt); Ill. Comp. Stat.,
ch. 610, §90/1 (West 2018) (drinking alcohol in a railroad
                      Cite as: 594 U. S. ____ (2021)                      9

                           Opinion of the Court

car); Ark. Code Ann. §5–71–207(a)(3), (b) (2016) (using ob-
scene language likely to promote disorder). So the amicus’s
(and concurrence’s) rule would cover lawbreakers of every
type, including quite a few hard to think alarming.
   This Court has held that when a minor offense alone is
involved, police officers do not usually face the kind of emer-
gency that can justify a warrantless home entry. In Welsh,
officers responded to a call about a drunk driver only to dis-
cover he had abandoned his vehicle and walked home. See
466 U. S., at 742–743. So no police pursuit was necessary,
hot or otherwise. The officers just went to the driver’s
house, entered without a warrant, and arrested him for a
“nonjailable” offense. Ibid. The State contended that exi-
gent circumstances supported the entry because the
driver’s “blood-alcohol level might have dissipated while the
police obtained a warrant.” Id., at 754. We rejected that
argument on the ground that the driver had been charged
with only a minor offense. “[T]he gravity of the underlying
offense,” we reasoned, is “an important factor to be consid-
ered when determining whether any exigency exists.” Id.,
at 753. “[W]hen only a minor offense has been committed”
(again, without any flight), there is reason to question
whether a compelling law enforcement need is present; so
it is “particularly appropriate” to “hesitat[e] in finding exi-
gent circumstances.” Id., at 750. And we concluded:
“[A]pplication of the exigent-circumstances exception in the
context of a home entry should rarely be sanctioned when
there is probable cause to believe that only a minor offense”
is involved. Id., at 753.2

——————
   2 The concurrence is wrong to say that Welsh applies only to nonjailable

offenses, and not to minor crimes that are labeled misdemeanors. See
post, at 12–13 (ROBERTS, C. J., concurring in judgment). No less than
four times, Welsh framed its holding as applying to “minor offenses” gen-
erally. 466 U. S., at 750, 752–753. (By contrast, the word “nonjailable”
does not appear in its legal analysis.) The decision cited lower court cases
10                      LANGE v. CALIFORNIA

                          Opinion of the Court

  Add a suspect’s flight and the calculus changes—but not
enough to justify the amicus’s categorical rule. We have no
doubt that in a great many cases flight creates a need for
police to act swiftly. A suspect may flee, for example, be-
cause he is intent on discarding evidence. Or his flight may
show a willingness to flee yet again, while the police await
a warrant. But no evidence suggests that every case of mis-
demeanor flight poses such dangers. Recall that misde-
meanors can target minor, non-violent conduct. See supra,
at 8–9. Welsh held that when that is so, officers can proba-
bly take the time to get a warrant. And at times that will
be true even when a misdemeanant has forced the police to
pursue him (especially given that “pursuit” may cover just
a few feet of ground, see supra, at 6). Those suspected of
minor offenses may flee for innocuous reasons and in non-
threatening ways. Consider from the casebooks: the man
with a mental disability who, in response to officers asking
him about “fidgeting with [a] mailbox,” retreated in “a hur-
ried manner” to his nearby home. Carroll v. Ellington, 800
F. 3d 154, 162 (CA5 2015). Or the teenager “driving with-
out taillights” who on seeing a police signal “did not stop
but drove two blocks to his parents’ house, ran inside, and
hid in the bathroom.” Mascorro v. Billings, 656 F. 3d 1198,
1202 (CA10 2011). In such a case, waiting for a warrant is
unlikely to hinder a compelling law enforcement need. See
id., at 1207 (“The risk of flight or escape was somewhere
between low and nonexistent[,] there was no evidence
which could have potentially been destroyed[,] and there
——————
prohibiting warrantless home entries when the defendant had commit-
ted a misdemeanor. See id., at 752. And its essential rationale applies
to all minor crimes, however labeled. As the Court stated (quoting an
earlier Justice Jackson opinion): It would “display[ ] a shocking lack of
all sense of proportion” to say that “private homes, even quarters in a
tenement, may be indiscriminately invaded at the discretion of any sus-
picious police officer engaged in following up offenses that involve no vi-
olence or threats of it.” Id., at 751 (quoting McDonald v. United States,
335 U. S. 451, 459 (1948) (concurring opinion)).
                      Cite as: 594 U. S. ____ (2021)                     11

                           Opinion of the Court

were no officer or public safety concerns”). Those non-
emergency situations may be atypical. But they reveal the
overbreadth—fatal in this context—of the amicus’s (and
concurrence’s) rule, which would treat a dangerous offender
and the scared teenager the same. In misdemeanor cases,
flight does not always supply the exigency that this Court
has demanded for a warrantless home entry.
   Our Fourth Amendment precedents thus point toward
assessing case by case the exigencies arising from misde-
meanants’ flight. That approach will in many, if not most,
cases allow a warrantless home entry. When the totality of
circumstances shows an emergency—such as imminent
harm to others, a threat to the officer himself, destruction
of evidence, or escape from the home—the police may act
without waiting. And those circumstances, as described
just above, include the flight itself.3 But the need to pursue
a misdemeanant does not trigger a categorical rule allowing
home entry, even absent a law enforcement emergency.
When the nature of the crime, the nature of the flight, and
——————
   3 Given that our rule allows warrantless home entry when emergencies

like these exist, we think the concurrence’s alarmism misplaced. See,
e.g., post, at 2 (opinion of ROBERTS, C. J.) (bewailing “danger[ ]” and “ab-
surd[ity]”). The concurrence spends most of its time worrying about
cases in which there are exigencies above and beyond the flight itself:
when, for example, the fleeing misdemeanant will “get a gun and take
aim from inside” or “flush drugs down the toilet.” Post, at 2, 8. But again:
When an officer reasonably believes those exigencies exist, he does not
need a categorical misdemeanor-pursuit rule to justify a warrantless
home entry. (And contrary to the concurrence’s under-explained sugges-
tion, see post, at 7–8, assessing exigencies is no harder in this context
than in any other.) The only cases in which we and the concurrence reach
a different result are cases involving flight alone, without exigencies like
the destruction of evidence, violence to others, or escape from the home.
It is telling that—although they are our sole disagreement—the concur-
rence hardly talks about those “flight alone” cases. Apparently, it taxes
even the concurrence to justify as an “exigency” a warrantless entry
based only on a misdemeanant’s prior retreat into his home—when the
police officers do not reasonably believe anything harmful will happen in
the time it takes to get a warrant.
12                 LANGE v. CALIFORNIA

                     Opinion of the Court

surrounding facts present no such exigency, officers must
respect the sanctity of the home—which means that they
must get a warrant.
                              B
   The common law in place at the Constitution’s founding
leads to the same conclusion. That law, we have many
times said, may be “instructive in determining what sorts
of searches the Framers of the Fourth Amendment re-
garded as reasonable.” E.g., Steagald, 451 U. S., at 217.
And the Framers’ view provides a baseline for our own day:
The Amendment “must provide at a minimum the degree of
protection it afforded when it was adopted.” United States
v. Jones, 565 U. S. 400, 411 (2012); see Jardines, 569 U. S.,
at 5. Sometimes, no doubt, the common law of the time is
hard to figure out: The historical record does not reveal a
limpid legal rule. See, e.g., Payton, 445 U. S., at 592–597.
Here, we find it challenging to map every particular of the
common law’s treatment of warrantless home entries. But
the evidence is clear on the question before us: The common
law did not recognize a categorical rule enabling such an
entry in every case of misdemeanor pursuit.
   Like our modern precedents, the common law afforded
the home strong protection from government intrusion. As
this Court once wrote: “The zealous and frequent repetition
of the adage that a ‘man’s house is his castle’ made it abun-
dantly clear that both in England and in the Colonies ‘the
freedom of one’s house’ was one of the most vital elements
of English liberty.” Id., at 596–597 (footnote omitted); see
Semayne’s Case, 5 Co. Rep. 91a, 91b, 77 Eng. Rep. 194, 195
(K. B. 1604) (“[T]he house of every one is as to him as his
castle and fortress, as well for his defen[s]e against injury
and violence, as for his repose” (footnote omitted)); 3 W.
Blackstone, Commentaries on the Laws of England 288
(1768) (“[E]very man’s house is looked upon by the law to
                      Cite as: 594 U. S. ____ (2021)                      13

                           Opinion of the Court

be his castle of defen[s]e and asylum”).4 To protect that in-
terest, “prominent law lords, the Court of Common Pleas,
the Court of King’s Bench, Parliament,” and leading trea-
tise writers all “c[a]me to embrace” the “understanding”
that generally “a warrant must issue” before a government
official could enter a house. Donohue, The Original Fourth
Amendment, 83 U. Chi. L. Rev. 1181, 1238–1239 (2016); see
Davies, Recovering the Original Fourth Amendment, 98
Mich. L. Rev. 547, 642–646 (1999). That did not mean the
Crown got the message; its officers often asserted power to
intrude into any home they pleased—thus adding to the col-
onists’ list of grievances. See Steagald, 451 U. S., at 220.
But the law on the books offered a different model: “To enter
a man’s house” without a proper warrant, Lord Chief Jus-
tice Pratt proclaimed in 1763, is to attack “the liberty of the
subject” and “destroy the liberty of the kingdom.” Huckle v.
Money, 2 Wils. K. B. 206, 207, 95 Eng. Rep. 768, 769 (K. B.
1763). That was the idea behind the Fourth Amendment.
   There was an oft-discussed exception: An officer, accord-
ing to the day’s treatises, could enter a house to pursue a
felon. The felony category then was a good deal narrower
than now. Many modern felonies were “classified as misde-
meanors” at common law, with the felony label mostly re-
served for crimes “punishable by death.” Garner, 471 U. S.,
at 13–14; see 4 W. Blackstone, Commentaries on the Laws
of England 98 (1791) (Blackstone). In addressing those se-
rious crimes, the law “allow[ed of] extremities” to meet “ne-

——————
  4 In a 1763 Parliamentary debate, about searches made to enforce a

tax, William Pitt the Elder orated as follows: “The poorest man may in
his cottage bid defiance to all the forces of the Crown. It may be frail; its
roof may shake; the wind may blow through it; the storm may enter; the
rain may enter; but the King of England cannot enter—all his force dares
not cross the threshold of the ruined tenement!” Miller v. United States,
357 U. S. 301, 307, and n. 7 (1958) (citing The Oxford Dictionary of Quo-
tations 379 (2d ed. 1953); 15 T. Hansard, Parliamentary History of Eng-
land, col. 1307 (1813)).
14                    LANGE v. CALIFORNIA

                        Opinion of the Court

cessity.” R. Burn, The Justice of the Peace, and Parish Of-
ficer 86 (6th ed. 1758). So if a person suspected “upon prob-
able grounds” of a felony “fly and take house,” Sir Matthew
Hale opined, then “the constable may break open the door,
tho he have no warrant.” 2 Pleas of the Crown 91–92 (1736)
(Hale). Sergeant William Hawkins set out a more restric-
tive rule in his widely read treatise. He wrote that a con-
stable, “with or without a warrant,” could “break open
doors” if “pursu[ing]” a person “known to have committed”
a felony—but not if the person was only “under a probable
suspicion.” 2 Pleas of the Crown 138–139 (1787) (Hawkins).
On the other hand, Sir William Blackstone went broader
than Hale. A constable, he thought, could “break open
doors”—no less than “upon a justice’s warrant”—if he had
“probable suspicion [to] arrest [a] felon,” even absent flight
or pursuit. Blackstone 292. The commentators thus dif-
fered on the scope of the felony exception to the warrant
requirement. But they agreed on one thing: It was indeed
a felony exception. All their rules applied to felonies as a
class, and to no other whole class of crimes.
   In the misdemeanor context, officers had more limited
authority to intrude on a fleeing suspect’s home.5 Once
again, some of the specifics are uncertain, and commenta-
tors did not always agree with each other. But none sug-
gested any kind of all-misdemeanor-flight rule. Instead,
their approval of entry turned on the circumstances. One
set of cases involved what might be called pre-felonies.
Blackstone explained that “break[ing] open doors” was al-
lowable not only “in case of [a] felony” but also in case of “a
dangerous wounding whereby [a] felony is likely to ensue.”
Ibid. In other words, the felony rule extended to crimes that
would become felonies if the victims died. See Hale 94.6
——————
  5 Note, though, that if a person had already been arrested and then

escaped from custody, an officer could always search for him at home.
See 2 W. Hawkins, Pleas of the Crown 87 (1721).
  6 Both felonies and pre-felonies justified the common law’s “hue and
                     Cite as: 594 U. S. ____ (2021)                   15

                          Opinion of the Court

Another set of cases involved crimes, mostly violent them-
selves, liable to provoke felonious acts. Often called “af-
frays” or “breaches of the peace,” a typical example was “the
fighting of two or more persons” to “the terror of his maj-
esty’s subjects.” Blackstone 145, 150.7 Because that con-
duct created a “danger of felony”—because when it oc-
curred, “there is likely to be manslaughter or bloodshed
committed”—“the constable may break open the doors to
keep the peace.” Hale 90, 95 (emphasis deleted); see Haw-
kins 139 (blessing a warrantless entry “where those who
have made an affray in [the constable’s] presence fly to a
house and are immediately pursued”). Hale also approved
a warrantless entry to stop a more mundane form of harm:
He (though not other commentators) thought a constable
could act to “suppress the disorder” associated with “drink-
ing or noise in a house at an unseasonable time of night.”
Hale 95. But differences aside, all the commentators fo-
cused on the facts of cases: When a suspected misdemean-
ant, fleeing or otherwise, threatened no harm, the constable
had to get a warrant.
   The common law thus does not support a categorical rule
allowing warrantless home entry when a misdemeanant
flees. It had a rule of that kind for felonies. But much as

——————
cry”: when a constable or other person “raise[d] the power of the towne”—
“with horn and with voice”—to pursue an offender. 3 E. Coke, Institutes
of the Laws of England 116 (1644); Blackstone 293. Most of the common-
law authorities approved warrantless home entries upon a hue and cry.
But because that process was generally available only to apprehend fel-
ons and those who had “dangerously wounded any person,” it did not en-
large the range of qualifying offenses. Hale 98; see Brief for Constitu-
tional Accountability Center as Amicus Curiae 17–18.
   7 The term “breach of the peace” can today encompass many kinds of

behavior, and even in common-law times it “meant very different things
in different” contexts. Atwater v. Lago Vista, 532 U. S. 318, 327, n. 2
(2001). But “[m]ore often than not, when used in reference to common-
law arrest power, the term seemed to connote an element of violence.”
Id., at 327–328, n. 2.
16                      LANGE v. CALIFORNIA

                          Opinion of the Court

in Welsh centuries later, the common law made distinctions
based on “the gravity of the underlying offense.” 466 U. S.,
at 753. When it came to misdemeanors, flight alone was
not enough. Whether a constable could make a warrantless
entry depended as well on other circumstances suggesting
a potential for harm and a need to act promptly.8 In that
way, the common-law rules (even if sometimes hard to dis-
cern with precision) mostly mirror our modern caselaw.
The former too demanded—and often found—a law enforce-
ment exigency before an officer could “break open” a fleeing
misdemeanant’s doors. Blackstone 292.
                              III
  The flight of a suspected misdemeanant does not always
justify a warrantless entry into a home. An officer must
consider all the circumstances in a pursuit case to deter-
mine whether there is a law enforcement emergency. On
many occasions, the officer will have good reason to enter—
to prevent imminent harms of violence, destruction of evi-
dence, or escape from the home. But when the officer has
time to get a warrant, he must do so—even though the mis-
demeanant fled.
  Because the California Court of Appeal applied the cate-
gorical rule we reject today, we vacate its judgment and re-
mand the case for further proceedings not inconsistent with
this opinion.
                                              It is so ordered.


——————
   8 The concurrence professes to disagree with this conclusion, see post,

at 17–19 (opinion of ROBERTS, C. J.), but its account of the common law
ends up in much the same place as ours. The concurrence recognizes a
categorical rule permitting warrantless home entry in pursuit of fleeing
felons. See post, at 17. But for misdemeanants, the concurrence presents
only discrete circumstances—mostly the same as ours—allowing home
entry without a warrant. Post, at 17–18. Those particular instances of
permissible entry do not create a categorical rule.
                 Cite as: 594 U. S. ____ (2021)            1

                   KAVANAUGH, J., concurring

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 20–18
                         _________________


     ARTHUR GREGORY LANGE, PETITIONER v.
                CALIFORNIA
   ON WRIT OF CERTIORARI TO THE COURT OF APPEAL OF
        CALIFORNIA, FIRST APPELLATE DISTRICT
                        [June 23, 2021]

   JUSTICE KAVANAUGH, concurring.
   The Court holds that an officer may make a warrantless
entry into a home when pursuing a fleeing misdemeanant
if an exigent circumstance is also present—for example,
when there is a risk of escape, destruction of evidence, or
harm to others. I join the Court’s opinion. I also join Part
II of JUSTICE THOMAS’s concurrence regarding how the ex-
clusionary rule should apply to hot pursuit cases.
   I add this brief concurrence simply to underscore that, in
my view, there is almost no daylight in practice between the
Court’s opinion and THE CHIEF JUSTICE’s opinion concur-
ring in the judgment.
   In his thoughtful opinion, THE CHIEF JUSTICE concludes
that pursuit of a fleeing misdemeanant should itself consti-
tute an exigent circumstance. The Court disagrees. As I
see it, however, the difference between THE CHIEF
JUSTICE’s approach and the Court’s approach will be aca-
demic in most cases. That is because cases of fleeing mis-
demeanants will almost always also involve a recognized
exigent circumstance—such as a risk of escape, destruction
of evidence, or harm to others—that will still justify war-
rantless entry into a home. See ante, at 1, 4, 16; see also,
e.g., City and County of San Francisco v. Sheehan, 575 U. S.
600, 612 (2015); Kentucky v. King, 563 U. S. 452, 460 (2011);
2                  LANGE v. CALIFORNIA

                   KAVANAUGH, J., concurring

Brigham City v. Stuart, 547 U. S. 398, 403 (2006); Minne-
sota v. Olson, 495 U. S. 91, 100 (1990). As Lange’s able
counsel forthrightly acknowledged at oral argument, the
approach adopted by the Court today will still allow the po-
lice to make a warrantless entry into a home “nine times
out of 10 or more” in cases involving pursuit of a fleeing
misdemeanant. Tr. of Oral Arg. 34.
   Importantly, moreover, the Court’s opinion does not dis-
turb the long-settled rule that pursuit of a fleeing felon is
itself an exigent circumstance justifying warrantless entry
into a home. See United States v. Santana, 427 U. S. 38,
42–43 (1976); cf. Stanton v. Sims, 571 U. S. 3, 8, 9 (2013)
(per curiam). In other words, the police may make a war-
rantless entry into the home of a fleeing felon regardless of
whether other exigent circumstances are present.
   With those observations, I join the Court’s opinion.
                 Cite as: 594 U. S. ____ (2021)            1

                      HOMAS, of
                    TOpinion J.,Tconcurring
                                  HOMAS, J.


SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 20–18
                         _________________


     ARTHUR GREGORY LANGE, PETITIONER v.
                CALIFORNIA
   ON WRIT OF CERTIORARI TO THE COURT OF APPEAL OF
        CALIFORNIA, FIRST APPELLATE DISTRICT
                        [June 23, 2021]

   JUSTICE THOMAS, with whom JUSTICE KAVANAUGH joins
as to Part II, concurring in part and concurring in the judg-
ment.
   I join the majority opinion, except for Part II–A, which
correctly rejects the argument that suspicion that a person
committed any crime justifies warrantless entry into a
home in hot pursuit of that person. I write separately to
note two things: the general case-by-case rule that the
Court announces today is subject to historical, categorical
exceptions; and under our precedent, the federal exclusion-
ary rule does not apply to evidence discovered in the course
of pursuing a fleeing suspect.
                              I
   The majority sets out a general rule requiring a case-by-
case inquiry when an officer enters a home without a war-
rant in pursuit of a person suspected of committing a mis-
demeanor. But history suggests several categorical excep-
tions to this rule. First, warrantless entry is categorically
allowed when a person is arrested and escapes. E.g., J. Par-
ker, Conductor Generalis 28–29 (1788) (constables may
break into houses without a warrant “[w]herever a person
is lawfully arrested for any cause, and afterwards escapes,
and shelters himself in an house”); ante, at 14, n. 5. This
exception is potentially very broad. See Torres v. Madrid,
2                   LANGE v. CALIFORNIA

                       HOMAS, of
                     TOpinion J.,Tconcurring
                                   HOMAS, J.

592 U. S. ___, ___ (2021) (slip op., at 1) (holding that an ar-
rest occurs whenever an officer applies physical force to the
body with intent to restrain); Genner v. Sparks, 6 Mod. 173,
174, 87 Eng. Rep. 928, 929 (Q. B. 1704). Second, authorities
at common law categorically allowed warrantless entry
when in hot pursuit of a person who committed an affray.
Ante, at 15. Third, those authorities allowed the same for
what the majority calls certain “pre-felonies.” Ante, at 14.
Finally, some authorities appear to have allowed warrant-
less entry when in pursuit of a person who had breached
the peace. See, e.g., 2 M. Hale, Pleas of the Crown 95 (1736)
(Hale); Wilgus, Arrest Without a Warrant, 22 Mich. L. Rev.
798, 802–803 (1924)). What crimes amounted to “breach of
peace” for purposes of warrantless entry is not immediately
clear. The term sometimes was used to refer to violence,
but the majority recognizes historical support for a broader
definition. Ante, at 15 (citing Hale 95). And cases decided
before and after the Fourteenth Amendment was ratified
similarly used the term “breach of peace” in a broad sense.
E.g., State v. Lafferty, 5 Del. 491 (1854) (“blow[ing] a trum-
pet at night through the streets”); Hawkins v. Lutton, 95
Wis. 492, 494, 70 N. W. 483 (1897) (“loud, profane, and in-
decent” language).
  I join the relevant parts of the majority on the under-
standing that its general case-by-case rule does not fore-
close historical, categorical exceptions. Although the ma-
jority unnecessarily leads with doctrine before history, it
does not disturb our regular rule that history—not court-
created standards of reasonableness—dictates the outcome
whenever it provides an answer. See, e.g., Wilson v. Arkan-
sas, 514 U. S. 927, 931 (1995); Virginia v. Moore, 553 U. S.
164, 171 (2008).
  I also join on the understanding that the majority has not
sought to settle the contours of any of these historical ex-
ceptions.
                  Cite as: 594 U. S. ____ (2021)             3

                       HOMAS, of
                     TOpinion J.,Tconcurring
                                   HOMAS, J.

                               II
   I also write to point out that even if the state courts on
remand conclude that the officer’s entry here was unlawful,
the federal exclusionary rule does not require suppressing
any evidence.
   “[O]fficers who violated the Fourth Amendment were tra-
ditionally considered trespassers.” Utah v. Strieff, 579
U. S. 232, 237 (2016). For that reason, “individuals subject
to unconstitutional searches or seizures historically en-
forced their rights through tort suits or self-help.” Ibid.
But beginning in the 20th century, this Court created a new
remedy: exclusion of evidence in criminal trials. Ibid.
   Establishing a violation of the Fourth Amendment,
though, does not automatically entitle a criminal defendant
to exclusion of evidence. Far from it. “[T]he exclusionary
rule is not an individual right.” Herring v. United States,
555 U. S. 135, 141 (2009). It is a “ ‘prudential’ doctrine cre-
ated by this Court,” Davis v. United States, 564 U. S. 229,
236 (2011) (citation omitted), and there is always a “high
obstacle for those urging application of the rule,” Pennsyl-
vania Bd. of Probation and Parole v. Scott, 524 U. S. 357,
364–365 (1998). Relevant here, the rule “does not apply
when the costs of exclusion outweigh its deterrent benefits.”
Strieff, 579 U. S., at 235.
   On the benefits side, “we have said time and again that
the sole” factor courts can consider is “deter[ring] miscon-
duct by law enforcement.” Davis, 564 U. S., at 246. And
not just any misconduct. The exclusionary rule developed
to deter “intentional conduct that was patently unconstitu-
tional.” Herring, 555 U. S., at 143 (emphasis added). For
the past several decades, we have thus declined to exclude
evidence where exclusion would not substantially deter “in-
tentional” and “flagrant” behavior. Id., at 144. For exam-
ple, the exclusionary rule does not apply where “some inter-
vening circumstance” arises between unconstitutional
conduct and discovery of evidence, Strieff, 579 U. S., at 238;
4                   LANGE v. CALIFORNIA

                       HOMAS, of
                     TOpinion J.,Tconcurring
                                   HOMAS, J.

where evidence would inevitably have been discovered,
ibid.; or where officers have acted in good faith, United
States v. Leon, 468 U. S. 897, 908 (1984).
  On the other side of the ledger, we consider all “costs.”
E.g., Davis, 564 U. S., at 237. One cost is especially salient:
excluding evidence under the Fourth Amendment always
obstructs the “ ‘truth-finding functions of judge and jury.’ ”
Leon, 468 U. S., at 907; accord, Nix v. Williams, 467 U. S.
431, 443 (1984) (recognizing “the public interest in having
juries receive all probative evidence”). This interference
with the purpose of the judicial system also creates a down-
stream risk that “some guilty defendants may go free or re-
ceive reduced sentences.” Leon, 468 U. S., at 907.
  By itself, this high cost makes exclusion under our prece-
dent rarely appropriate. “Suppression of evidence . . . has
always been our last resort, not our first impulse.” Hudson
v. Michigan, 547 U. S. 586, 591 (2006). When additional
costs are present, the balance tips decisively against exclu-
sion.
  Cases of fleeing suspects involve more than enough added
costs to render the exclusionary rule inapplicable. First,
our precedents make clear that the exclusionary rule does
not apply when it would encourage bad conduct by criminal
defendants. For example, evidence obtained during an un-
lawful search is still admissible to impeach a witness be-
cause exclusion would create “ ‘a license to use perjury.’ ”
United States v. Havens, 446 U. S. 620, 626 (1980). Here,
exclusion is inappropriate because it would encourage sus-
pects to flee. Second, our precedents similarly make clear
that criminal defendants cannot use the exclusionary rule
as “a shield against” their own bad conduct. Walder v.
United States, 347 U. S. 62, 65 (1954). In most—if not all—
States, fleeing from police after a lawful order to stop is a
crime. All the evidence that petitioner seeks to exclude is
evidence that inevitably would have been discovered had he
                 Cite as: 594 U. S. ____ (2021)            5

                      HOMAS, of
                    TOpinion J.,Tconcurring
                                  HOMAS, J.

complied with the officer’s order to stop. A criminal defend-
ant should “not . . . be put in a better position than [he]
would have been in if no illegality had transpired.” Nix, 467
U. S., at 443–444.
   Aware of the substantial costs created by the exclusion-
ary rule, courts have sometimes narrowed the protections
historically afforded by the Fourth Amendment to avoid
having to exclude evidence. See Collins v. Virginia, 584
U. S. ___, ___ (2018) (THOMAS, J., concurring) (slip op., at
1); A. Amar, The Constitution and Criminal Procedure:
First Principles 30 (1997) (“Judges do not like excluding
bloody knives, so they distort doctrine”). But it should be
the judicially created remedy, not the Fourth Amendment,
that contracts in the face of that pressure. Courts should
follow the plain dictates of our precedent: Officers cannot
chase a fleeing person into a home simply because that per-
son is suspected of having committed any misdemeanor, but
if the officer nonetheless does so, exclusion under the
Fourth Amendment is improper. Criminal defendants
must rely on other remedies.
                  Cite as: 594 U. S. ____ (2021)             1

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

SUPREME COURT OF THE UNITED STATES
                            _________________

                             No. 20–18
                            _________________


     ARTHUR GREGORY LANGE, PETITIONER v.
                CALIFORNIA
   ON WRIT OF CERTIORARI TO THE COURT OF APPEAL OF
        CALIFORNIA, FIRST APPELLATE DISTRICT
                          [June 23, 2021]

   CHIEF JUSTICE ROBERTS, with whom JUSTICE ALITO
joins, concurring in the judgment.
   Suppose a police officer on patrol responds to a report of
a man assaulting a teenager. Arriving at the scene, the of-
ficer sees the teenager vainly trying to ward off the assail-
ant. The officer attempts to place the assailant under ar-
rest, but he takes off on foot. He leads the officer on a chase
over several blocks as the officer yells for him to stop. With
the officer closing in, the suspect leaps over a fence and then
stands on a home’s front yard. He claims it’s his home and
tells the officer to stay away. What is the officer to do?
   The Fourth Amendment and our precedent—not to men-
tion common sense—provide a clear answer: The officer can
enter the property to complete the arrest he lawfully initi-
ated outside it. But the Court today has a different take.
Holding that flight, on its own, can never justify a warrant-
less entry into a home (including its curtilage), the Court
requires that the officer: (1) stop and consider whether the
suspect—if apprehended—would be charged with a misde-
meanor or a felony, and (2) tally up other “exigencies” that
might be present or arise, ante, at 1, 4, before (3) deciding
whether he can complete the arrest or must instead seek a
warrant—one that, in all likelihood, will not arrive for
hours. Meanwhile, the suspect may stroll into the home
and then dash out the back door. Or, for all the officer
2                    LANGE v. CALIFORNIA

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

knows, get a gun and take aim from inside.
   The Constitution does not demand this absurd and dan-
gerous result. We should not impose it. As our precedent
makes clear, hot pursuit is not merely a setting in which
other exigent circumstances justifying warrantless entry
might emerge. It is itself an exigent circumstance. And we
have never held that whether an officer may enter a home
to complete an arrest turns on what the fleeing individual
was suspected of doing before he took off, let alone whether
that offense would later be charged as a misdemeanor or
felony. It is the flight, not the underlying offense, that has
always been understood to justify the general rule: “Police
officers may enter premises without a warrant when they
are in hot pursuit of a fleeing suspect.” Kentucky v. King,
563 U. S. 452, 460 (2011). The Court errs by departing from
that well-established rule.
                               I
                               A
   The Fourth Amendment protects “[t]he right of the people
to be secure in their persons, houses, papers, and effects,
against unreasonable searches and seizures” and provides
that “no Warrants shall issue, but upon probable cause.”
While the Amendment does not specify when a warrant
must be obtained, we have typically required that officers
secure one before entering a home to execute a search or
seizure. King, 563 U. S., at 459. We have also, however,
recognized exceptions to that requirement “because the ul-
timate touchstone of the Fourth Amendment is ‘reasonable-
ness.’ ” Brigham City v. Stuart, 547 U. S. 398, 403 (2006).
   In some instances the Court has determined that this
question of reasonableness can be decided by application of
a rule for a particular type of case. Mitchell v. Wisconsin,
588 U. S. ___, ___, n. 2 (2019) (plurality opinion) (slip op., at
9, n. 2); see Illinois v. McArthur, 531 U. S. 326, 330 (2001)
                  Cite as: 594 U. S. ____ (2021)             3

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

(“[T]his Court has interpreted the Amendment as establish-
ing rules and presumptions.”). This approach reflects our
recognition of the need “to provide clear guidance to law en-
forcement.” Riley v. California, 573 U. S. 373, 398 (2014).
We strive to “draw standards sufficiently clear and simple
to be applied with a fair prospect of surviving judicial
second-guessing months and years after an arrest or search
is made.” Atwater v. Lago Vista, 532 U. S. 318, 347 (2001).
   We have, for example, established general rules giving ef-
fect to the “well-recognized exception [that] applies when
the exigencies of the situation make the needs of law en-
forcement so compelling that [a] warrantless search is ob-
jectively reasonable under the Fourth Amendment.” King,
563 U. S., at 460 (some alterations in original; internal quo-
tation marks omitted). In fact, “our exigency case law is full
of general rules” that provide “guidance on how police
should handle [such] cases.” Mitchell, 588 U. S., at ___,
n. 3 (slip op., at 9, n. 3) (internal quotation marks omitted).
These rules allow warrantless entry into the home when
necessary to “protect individuals who are threatened with
imminent harm, or prevent the imminent destruction of ev-
idence.” Carpenter v. United States, 585 U. S. ___, ___–___
(2018) (slip op., at 21–22). Or—relevant here—“to pursue a
fleeing suspect.” Id., at ___ (slip op., at 21).
   We take a case-by-case approach in deciding whether a
search or seizure was conducted in reaction to an exigent
circumstance, such as whether an officer had an objective
basis to “fear the imminent destruction of evidence.” Birch-
field v. North Dakota, 579 U. S. 438, ___ (2016) (slip op., at
15). But once faced with an exigency, our rule is clear: of-
ficers are “not bound to learn anything more or wait any
longer before going in.” United States v. Banks, 540 U. S.
31, 40 (2003).
   Today, the Court holds that hot pursuit merely sets the
table for other exigencies that may emerge to justify war-
rantless entry, such as imminent harm. This comes as a
4                    LANGE v. CALIFORNIA

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

surprise. For decades we have consistently recognized pur-
suit of a fleeing suspect as an exigency, one that on its own
justifies warrantless entry into a home.
   Almost a half century ago in United States v. Santana,
427 U. S. 38 (1976), we considered whether hot pursuit sup-
ports warrantless home entry. We held that such entry was
justified when Santana “retreat[ed] into her house” after a
drug transaction upon hearing law enforcement “shout[ ]
‘police’ ” and seeing them “display[ ] their identification.”
Id., at 40, 42. As we explained, “a suspect may not defeat
an arrest which has been set in motion in a public place . . .
by the expedient of escaping to a private place.” Id., at 43.
Our interpretation of the Fourth Amendment did not hinge
on whether the offense that precipitated her withdrawal
was a felony or a misdemeanor. See Stanton v. Sims, 571
U. S. 3, 9 (2013) (per curiam).
   We have repeatedly and consistently reaffirmed that hot
pursuit is itself an exigent circumstance. See, e.g., Carpen-
ter, 585 U. S., at ____ (slip op., at 21) (“[E]xigencies include
the need to pursue a fleeing suspect.”); Collins v. Virginia,
584 U. S. ___, ___ (2018) (slip op., at 12) (distinguishing
prior case approving warrantless entry onto the curtilage
as best sounding in “hot pursuit”); Birchfield, 579 U. S., at
___ (slip op., at 15) (exception for exigent circumstances au-
thorizes “the warrantless entry of private property . . .
when police are in hot pursuit of a fleeing suspect”); King,
563 U. S., at 460 (“Police officers may enter premises with-
out a warrant when they are in hot pursuit of a fleeing sus-
pect.”); Brigham City, 547 U. S., at 403 (“We have held, for
example, that law enforcement officers may make a war-
rantless entry onto private property . . . to engage in ‘hot
pursuit’ of a fleeing suspect.” (citations omitted)); Steagald
v. United States, 451 U. S. 204, 221 (1981) (“[W]arrantless
entry of a home would be justified if the police were in ‘hot
pursuit’ of a fugitive.”); see also Mitchell, 588 U. S., at ___
(SOTOMAYOR, J., dissenting) (slip op., at 11) (“ ‘hot pursuit’
                  Cite as: 594 U. S. ____ (2021)             5

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

of a fleeing suspect” qualifies as an exigency); Missouri v.
McNeely, 569 U. S. 141, 176–177 (2013) (THOMAS, J., dis-
senting) (same).
  These cases, it bears repeating, have not viewed hot pur-
suit as merely the background against which other exigen-
cies justifying warrantless entry might arise. See, e.g., Car-
penter, 585 U. S., at ___–___ (slip op., at 21–22) (identifying
destruction of evidence, emergency aid, and hot pursuit as
separate exigencies); Birchfield, 579 U. S., at ___ (slip op.,
at 15) (same); McNeely, 569 U. S., at 148–149 (opinion of
the Court) (same); King, 563 U. S., at 460 (same); Brigham
City, 547 U. S., at 403 (same); see also Mitchell, 588 U. S.,
at ___ (SOTOMAYOR, J., dissenting) (slip op., at 11) (same).
And our decisions do not dismiss the existence of an exi-
gency—including hot pursuit—based on the underlying of-
fense that precipitated law enforcement action, even if
known. To the contrary, until today, we have explicitly re-
jected invitations to do so. See Brigham City, 547 U. S., at
405 (dismissing defendants’ contention that offenses at is-
sue were “not serious enough” to justify reliance on the
emergency aid doctrine); Michigan v. Fisher, 558 U. S. 45,
47 (2009) (per curiam); see also Atwater, 532 U. S., at 354
(rejecting exception for “very minor criminal offense[s]” to
rule allowing warrantless arrests).
  The Court displays little patience for this precedent.
With regard to Santana, the Court concedes that “we
framed our holding in broad[ ] terms.” Ante, at 7. Yet it
narrows those terms based on rationales that played no role
in the decision. The Court then brushes off our slew of cases
reaffirming Santana’s broad holding as nothing more than
“dicta.” Ante, at 7. I would not override decades of guidance
to law enforcement in favor of a new rule that provides no
guidance at all.
                             B
  A proper consideration of the interests at stake confirms
6                    LANGE v. CALIFORNIA

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

the position our precedent amply supports. Pursuit impli-
cates substantial government interests, regardless of the of-
fense precipitating the flight. It is the flight, not the under-
lying offense, that justifies the entry.
   At the start, every hot pursuit implicates the government
interest in ensuring compliance with law enforcement. Cal-
ifornia v. Hodari D., 499 U. S. 621, 627 (1991). Flight is a
direct attempt to evade arrest and thereby frustrate our
“society’s interest in having its laws obeyed.” Terry v. Ohio,
392 U. S. 1, 26 (1968). Disregarding an order to yield to law
enforcement authority cannot be dismissed with a shrug of
the shoulders simply because the underlying offense is re-
garded as “innocuous,” ante, at 10. As the many state
courts to approve of warrantless entry in hot pursuit have
reminded us, “[l]aw enforcement is not a child’s game of
prisoners base, or a contest, with apprehension and convic-
tion depending upon whether the officer or defendant is the
fleetest of foot.” Commonwealth v. Jewett, 471 Mass. 624,
634, 31 N. E. 3d 1079, 1089 (2015) (quoting State v. Ricci,
144 N. H. 241, 245, 739 A. 2d 404, 408 (1999)).
   Flight also always involves the “paramount” government
interest in public safety. Scott v. Harris, 550 U. S. 372, 383
(2007); see Hodari D., 499 U. S., at 627 (“Street pursuits
always place the public at some risk, and compliance with
police orders to stop should therefore be encouraged.”). A
fleeing suspect “intentionally place[s] himself and the pub-
lic in danger.” Scott, 550 U. S., at 384. Vehicular pursuits,
in particular, are often catastrophic. See Dept. of Justice,
Bureau of Justice Statistics, B. Reaves, Police Vehicle Pur-
suits, 2012–2013, p. 6 (May 2017) (average of about one
death per day in the United States from vehicle pursuits
from 1996 to 2015). Affording suspects the opportunity to
evade arrest by winning the race rewards flight and encour-
ages dangerous behavior.
   And the problems do not end there because hot pursuit
                  Cite as: 594 U. S. ____ (2021)             7

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

often gives rise to multiple other exigencies, such as de-
struction of evidence, violence, and escape. The Court
acknowledges this reality, but then posits that not “every
case of misdemeanor flight poses such dangers.” Ante, at
10 (emphasis added). Of course not. But we have never
required such a level of certainty before crafting a general
rule that law enforcement can follow. For example, in
Washington v. Chrisman, 455 U. S. 1 (1982), we held that
an officer may accompany an arrestee into his residence
without any showing of exigency and regardless of the “na-
ture of the offense for which the arrest was made,” because
there “is no way for an officer to predict reliably how a par-
ticular subject will react to arrest” and “the possibility that
an arrested person will attempt to escape if not properly
supervised is obvious.” Id., at 6–7. In Michigan v. Sum-
mers, 452 U. S. 692 (1981), we concluded that, although “no
special danger to the police” was suggested by the evidence
in the record, the execution of a search warrant merited a
categorical rule allowing detention of present individuals
because it was the “kind of transaction” that could give rise
to other exigencies. Id., at 702. And in United States v.
Robinson, 414 U. S. 218 (1973), we held that the search in-
cident to arrest exception applies to all arrests regardless
“what a court may later decide was the probability in a par-
ticular arrest situation that weapons or evidence would in
fact be found,” because arrests require “quick ad hoc judg-
ment[s].” Id., at 235.
   Such concerns are magnified here. The act of pursuing a
fleeing suspect makes simultaneously assessing which
other exigencies might arise especially difficult to ascertain
“on the spur (and in the heat) of the moment.” Atwater, 532
U. S., at 347. The Court disputes this proposition, ante, at
11, n. 3, but the difficulty of discerning hidden weapons or
drugs on a suspect running or driving away seems clear to
us.
   The risks to officer safety posed by the Court’s suggestion
8                    LANGE v. CALIFORNIA

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

that an officer simply abandon pursuit and await a warrant
are severe. We are warned in this case that “attempting
warrant service for an unknown suspect in an unknown
home at night is flat dangerous.” Brief for Sonoma County
District Attorney’s Office et al. as Amici Curiae 33.
Whether at night or during the day, the officer is obviously
vulnerable to those inside the home while awaiting a war-
rant, including danger from a suspect who has already
demonstrated himself to be undeterred by police orders.
See, e.g., Thompson v. Florence, 2019 WL 3220051, *4 (ND
Ala., July 17, 2019) (at fleeing suspect’s urging, resident
grabbed a handgun); State v. Davis, 2000–278, p. 5 (La.
App. 5 Cir. 8/29/00), 768 So. 2d 201, 206 (fleeing suspect
“reached for a handgun” inside home).
   Even if the area outside the home remains tranquil, the
suspect inside is free to destroy evidence or continue his es-
cape. Flight is obviously suggestive of these recognized ex-
igencies, which could materialize promptly once the officer
is compelled to abandon pursuit. The destruction of evi-
dence can take as little as “15 or 20 seconds,” Banks, 540
U. S., at 40; and a suspect can dash out the back door just
as quickly, while the officer must wait outside. Forcing the
officer to wait and predict whether such exigencies will oc-
cur before entry is in practice no different from forcing the
officer to wait for these exigencies to occur.
   Indeed, from the perspective of the officer, many in-
stances of flight leading to further wrongdoing are the sort
of “flight alone” cases the Court deems harmless, ante, at
11, n. 3. Despite the Court’s suggestion to the contrary, ex-
amples of “flight alone” generating exigencies difficult to
identify in advance are not hard to find. See, e.g. State v.
Lam, 2013-Ohio-505, 989 N. E. 2d 100, 101–102 (App.)
(warrantless entry in hot pursuit of someone who commit-
ted turn signal violation revealed heroin on suspect and
suggested attempt to flush drugs down the toilet); State v.
Mitchem, 2014-Ohio-2366, 2014 WL 2565680, *1 (App.,
                  Cite as: 594 U. S. ____ (2021)             9

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

June 4, 2014) (suspect who committed trespass, fled from
the police into private driveway, and stated to officers
“[Y]ou can’t touch me, I’m at my house,” turned out to have
a gun). (And, as we will see, it is apparently hard to decide
which cases qualify as “flight alone” cases, see infra, at 16.)
   If the suspect continues to flee through the house, while
the officer must wait, even the quickest warrant will be far
too late. Only in the best circumstances can one be obtained
in under an hour, see Brief for Respondent 33, and it usu-
ally takes much longer than that, see Brief for Los Angeles
County Police Chiefs’ Association as Amicus Curiae 24–25.
Even electronic warrants may involve “time-consuming for-
malities.” McNeely, 569 U. S., at 155. And some States typ-
ically require that a warrant application be in writing, see,
e.g., Colo. Rev. Stat. §16–3–303 (2020), or that the applicant
appear in person before a judge, see, e.g., Mass. Gen. Laws,
ch. 276, §2B (2019), or permit oral applications only for cer-
tain cases, see, e.g., Iowa Code §321J.10.3 (2019). All of
these factors make it very possible that the officer will never
be able to identify the suspect if he cannot continue the pur-
suit. See Hiibel v. Sixth Judicial Dist. Court of Nev., Hum-
boldt Cty., 542 U. S. 177, 186 (2004) (recognizing identifica-
tion as an “important government interest[ ]”). The Court
today creates “perverse incentives” by imposing an “invita-
tion to impunity-earned-by-recklessness.” Scott, 555 U. S.,
at 385–386.
   Against these government interests we balance the sus-
pect’s privacy interest in a home to which he has voluntarily
led a pursuing officer. If the residence is not his the suspect
has no privacy interest to protect. Rakas v. Illinois, 439
U. S. 128, 141 (1978); see also State v. Walker, 2006–1045,
p. 7 (La. 4/11/07), 953 So. 2d 786, 790–791 (suspect fled into
third person’s residence where he was unwelcome); Ulysse
v. State, 899 So. 2d 1233, 1234 (Fla. App. 2005) (suspect ran
inside the home of “a complete stranger”). The police may
well have no reason to know whether the suspect entered
10                   LANGE v. CALIFORNIA

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

his own or someone else’s home or yard. If the suspect does
escape into his own home, his privacy interest is diminished
because he was the one who chose to move his encounter
with the police there. See State v. Legg, 633 N. W. 2d 763,
773 (Iowa 2001) (nature of intrusion is “slight” in hot pur-
suit because the officer’s entry “was no surprise to [the sus-
pect]; he was following closely on her heels”); 4 W. LaFave,
Search and Seizure §9.2(d), p. 419 (6th ed. 2020) (“the sus-
pect has only himself to blame for the fact that the encoun-
ter has been moved from a public to a private area”). In
cases of hot pursuit, “[t]he offender is then not being both-
ered by the police unexpectedly while in domestic tranquil-
ity. He has gone to his home while fleeing solely to escape
arrest.” R. v. Macooh, [1993] 2 S. C. R. 802, 815. Put dif-
ferently, just as arrestees have “reduced privacy interests,”
Riley, 573 U. S., at 391, so too do those who evade arrest by
leading the police on car chases into their garages.
                                C
   “In determining what is reasonable under the Fourth
Amendment, we have given great weight to the essential
interest in readily administrable rules.” Virginia v. Moore,
553 U. S. 164, 175 (2008) (internal quotation marks omit-
ted). This is particularly true with respect to the rules gov-
erning exceptions to the warrant requirement because of
exigent circumstances. See Mitchell, 588 U. S., at ___, n. 3
(slip op., at 9, n. 3). And contrary to the Court’s suggestion,
the home is not immune from the application of such rules
consistent with the Fourth Amendment. See, e.g., Sum-
mers, 452 U. S., at 705; Chimel v. California, 395 U. S. 752,
763 (1969).
   Like most rules, this one is not without exceptions or
qualifications. The police cannot manufacture an unneces-
sary pursuit to enable a search of a home rather than to
execute an arrest. Cf. Fernandez v. California, 571 U. S.
292, 302 (2014) (“evidence that the police have removed the
                  Cite as: 594 U. S. ____ (2021)          11

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

potentially objecting tenant from the entrance for the sake
of avoiding possible objection” would be probative of the ob-
jective unreasonableness of a warrantless entry based on
the consent of another occupant). Additionally, if a reason-
able officer would not believe that the suspect fled into the
home to “thwart an otherwise proper arrest,” Santana, 427
U. S., at 42, warrantless entry would not be reasonable.
   Additional safeguards limit the potential for abuse. The
officer must in all events effect a reasonable entry. United
States v. Ramirez, 523 U. S. 65, 71 (1998). As the lower
courts have recognized, hot pursuit gives the officer author-
ity to enter a home, but “it does not have any bearing on the
constitutionality of the manner in which he enters the
home.” Trent v. Wade, 776 F. 3d 368, 382 (CA5 2015). And
his authority to search is circumscribed, limited to “those
spaces where a person may be found” for “no longer than it
takes to complete the arrest and depart the premises.”
Maryland v. Buie, 494 U. S. 325, 335–336 (1990). Finally,
arrests conducted “in an extraordinary manner, unusually
harmful to an individual’s privacy or even physical inter-
ests” are subject to even more stringent review. Whren v.
United States, 517 U. S. 806, 818 (1996).
   Courts must also ascertain whether a given set of circum-
stances actually qualifies as hot pursuit. While the flight
need not be reminiscent of the opening scene of a James
Bond film, there must be “some sort of a chase.” Santana,
427 U. S., at 43. The pursuit must be “immediate or con-
tinuous.” Welsh v. Wisconsin, 466 U. S. 740, 753 (1984).
And the suspect should have known the officer intended for
him to stop. Cf. Michigan v. Chesternut, 486 U. S. 567, 573–
574 (1988). Where a suspect, for example, chooses to end a
voluntary conversation with law enforcement and go inside
her home, that does not constitute flight. Florida v. Royer,
460 U. S. 491, 497–498 (1983) (plurality opinion).
   Because the California Court of Appeals assumed that
hot pursuit categorically permits warrantless entry, I
12                   LANGE v. CALIFORNIA

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

would vacate the decision below to allow consideration of
whether the circumstances at issue in this case fall within
an exception to the general rule of the sort outlined above.
Lange would be free to argue that his is the “unusual case,”
Mitchell, 588 U. S., at ____ (plurality opinion) (slip op., at
16), in which the general rule that hot pursuit justifies war-
rantless entry does not apply.
                                II
   Now consider the regime the Court imposes. In rejecting
the amicus’ proposed categorical rule favoring warrantless
home entry, the Court creates a categorical rule of its own:
Flight alone can never justify warrantless entry into a home
or its curtilage. Instead, flight is but one factor of unclear
weight to “consider,” ante, at 16, and it must be supple-
mented with at least one additional exigency. This is nec-
essary, the Court explains, because people “flee for innocu-
ous reasons,” ante, at 10, although the Court offers just two
actual examples of “innocuous” flight, the harmlessness of
which would not have been apparent to the police, see ibid.
(citing Carroll v. Ellington, 800 F. 3d 154, 162 (CA5 2015;
Mascorro v. Billings, 656 F. 3d 1198, 1202 (CA10 2011)).
   In order to create a hot pursuit rule ostensibly specific to
misdemeanors, the Court must turn to a case concerning
neither misdemeanors nor hot pursuit. In Welsh v. Wiscon-
sin, we held that the warrantless entry of a drunk driver’s
home to arrest him for a nonjailable offense violated the
Fourth Amendment. 466 U. S., at 754. The Court relies on
Welsh for the proposition that “when a minor offense alone
is involved . . . officers can probably take the time to get a
warrant” to execute an arrest. Ante, at 9–10. The Court’s
determination that Welsh applies to all cases involving “mi-
nor” offenses—although we never learn what qualifies as a
minor offense—ignores that we have already declined to ap-
ply Welsh to cases involving misdemeanors because of the
“significant” distinction between nonjailable offenses and
                  Cite as: 594 U. S. ____ (2021)           13

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

misdemeanors. McArthur, 531 U. S., at 336. And in any
event, we explicitly differentiated the circumstances at is-
sue in Welsh from “immediate or continuous pursuit of [a
person] from the scene of a crime.” 466 U. S., at 753; see
Brigham City, 547 U. S., at 405 (rejecting Welsh’s applica-
tion to a situation involving exigent circumstance of emer-
gency aid). Accordingly, as we have already held, “nothing
in [Welsh] establishes that the seriousness of the crime is
equally important in cases of hot pursuit.” Stanton, 571
U. S., at 9 (emphasis in original). The Court’s citation to
Justice Jackson’s concurrence in McDonald v. United
States, 335 U. S. 451 (1948), ante, at 11, n. 3, is similarly
inapt. That case involved entry for mere “follow[ ] up,” not
anything resembling hot pursuit. McDonald, 335 U. S., at
459.
   The Court next limits its consideration of the interests at
stake to a balancing of what it perceives to be the govern-
ment’s interest in capturing innocuous misdemeanants
against a person’s privacy interest in his home. The ques-
tion, however, is not whether “litter[ing]” presents risks to
public safety or the potential for escape, ante, at 8, but
whether flight does so. And flight from the police is never
innocuous.
   The Court ultimately decides that, when it comes to mis-
demeanors, States do not have as much of an interest in
seeing such laws enforced. But, as the Court concedes, we
have already rejected as “untenable” the “assumption that
a ‘felon’ is more dangerous than a misdemeanant.” Tennes-
see v. Garner, 471 U. S. 1, 14 (1985). This is so because “nu-
merous misdemeanors involve conduct more dangerous
than many felonies.” Ibid. At any rate, the fact that a sus-
pect flees when suspected of a minor offense could well be
indicative of a larger danger, given that he has voluntarily
exposed himself to much higher criminal penalties in ex-
change for the prospect of escaping or delaying arrest. Cf.
Illinois v. Wardlow, 528 U. S. 119, 124 (2000).
14                   LANGE v. CALIFORNIA

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

   The Court’s rule is also famously difficult to apply. The
difference between the two categories of offenses is esoteric,
to say the least. See Atwater, 532 U. S., at 350; Berkemer
v. McCarty, 468 U. S. 420, 431, n. 13 (1984) (“[O]fficers in
the field frequently have neither the time nor the compe-
tence to determine the severity of the offense for which they
are considering arresting a person.” (internal quotation
marks omitted)). For example, driving while under the in-
fluence is a misdemeanor in many States, but becomes a
felony if the suspect is a serial drunk driver. See, e.g.,
Alaska Stat. §28.35.030(n) (2020). Drug possession may be
a misdemeanor or a felony depending on the weight of the
drugs. See, e.g., Ohio Rev. Code Ann. §2925.11(C) (Lexis
2019) (outlining 50 potential iterations of unlawful drug
possession, some misdemeanors others felonies). Layer on
top of this that for certain offenses the exact same conduct
may be charged as a misdemeanor or felony depending on
the discretionary decisions of the prosecutor and the judge
(what California refers to as a “wobbler”), and we have a
recipe for paralysis in the face of flight. See Cal. Penal Code
Ann. §§486–490.1 (West Cum. Supp. 2021) (classifying
theft as an infraction, misdemeanor, wobbler, or felony de-
pending on the value of the stolen item).
   The Court permits constitutional protections to vary
based on how each State has chosen to classify a given of-
fense. For example, “human trafficking” can be a misde-
meanor in Maryland, Md. Crim. Law Code Ann. §3–
1102(c)(1) (2019), contra, Tex. Penal Code Ann. §20A.02
(West 2021), and in Pennsylvania so can involuntary man-
slaughter, 18 Pa. Cons. Stat. §2504(b) (2015); contra, Ohio
Rev. Code Ann. §2903.04(C). The vehicular flight at issue
in this very case is classified as a felony in several States.
See, e.g., Fla. Stat. §316.1935 (2014); Del. Code Ann., Tit.
21, §4103 (2013). Law enforcement entities and state gov-
ernments across the Nation tell us that they have accord-
                  Cite as: 594 U. S. ____ (2021)            15

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

ingly developed standards for warrantless entry in hot pur-
suit tailored to their respective legal regimes. See Brief for
Los Angeles County Police Chiefs’ Association as Amicus
Curiae 14–20; Brief for State of Ohio et al. as Amici Curiae
25. Given the distinct nature of each State’s legal code,
such an approach is more appropriate than the Court’s
blunt constitutional reform.
   For all these reasons, we have not crafted constitutional
rules based on the distinction between modern day misde-
meanors and felonies. In Tennessee v. Garner, for example,
we held that deadly force could not categorically be used to
seize a fleeing felon, even though the common law supplied
such a rule, because at common law the “gulf between the
felonies and the minor offences was broad and deep,” but
today it is “minor and often arbitrary.” 471 U. S., at 14 (in-
ternal quotation marks omitted).
   Similarly, in Atwater, we held that the general probable-
cause rule for warrantless arrests applied to “even a very
minor criminal offense,” “without the need to balance the
interests and circumstances involved in particular situa-
tions.” 532 U. S., at 354 (internal quotation marks omit-
ted). We explained that we could not expect every police
officer to automatically recall “the details of frequently com-
plex penalty schemes,” and concluded that distinguishing
between “permissible and impermissible arrests for minor
crimes” was a “very unsatisfactory line to require police of-
ficers to draw on a moment’s notice.” Id., at 348, 350 (inter-
nal quotation marks and alteration omitted).
   The Court’s approach is hopelessly indeterminate in
other respects as well. The Court admonishes law enforce-
ment to distinguish between “dangerous offender[s]” and
“scared teenager[s],” ante, at 11, as if an officer can easily
tell one from the other, and as if the two categories are mu-
tually exclusive. See Dept. of Justice, Office of Juvenile
Justice and Delinquency Prevention, Offending by Juve-
niles (Mar. 31, 2020) (about 16% of serious violent crimes in
16                   LANGE v. CALIFORNIA

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

the United States from 2007 to 2017 were committed by ju-
veniles). And police are instructed to wait for a warrant if
there is sufficient “time,” ante, at 16, but they are not told
time before what, how many hours the Court would have
them wait, and what to do if other “pressing needs” arise.
See Mitchell, 588 U. S., at ___ (plurality opinion) (slip op.,
at 9) (“[A]n officer’s duty to attend to more pressing needs
may leave no time to seek a warrant.”).
  The Court tut-tuts that we are making far too much of all
this, and that our “alarmism [is] misplaced.” Ante, at 11,
n. 3. In fact, the Court says, its “approach will in many, if
not most, cases allow a warrantless home entry.” Ante, at
11. In support of that assurance, the Court lists several
“exigencies above and beyond the flight itself ” that would
permit home entry, notably when “the fleeing misdemean-
ant” will “escape from the home.” Ante, at 11, n. 3. If an
officer “reasonably believes” such an exigency exists,” the
Court says, “he does not need a categorical misdemeanor-
pursuit rule to justify a warrantless home entry.” Ibid.
  When a suspect flees into a dwelling there typically will
be another way out, such as a back door or fire escape. See
Cal. Code Regs., tit. 24, §§1113.2, 1114.8 (2019) (apart-
ments, floors of high-rise buildings, and many other homes
must have access to at least two means of egress). If the
officer reasonably believes there are multiple exits, then
surely the officer can conclude that the suspect might well
“escape from the home,” ante, at 11, n. 3, by running out the
back, rather than “slowing down and wiping his brow”
while the officer attempts to get a warrant. Scott, 550 U. S.,
at 385. Under the Court’s rule warrantless entry into a
home in hot pursuit of a fleeing misdemeanant would pre-
sumably be permissible, as long as the officer reasonably
believed the home had another exit. Question: Is that cor-
rect? Police in the field deserve to know.
  But the Court will not answer the question, leaving it to
the officer to figure out in the midst of hot pursuit. The
                  Cite as: 594 U. S. ____ (2021)           17

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

answer apparently depends on whether the police “believe
anything harmful will happen in the time it takes to get a
warrant,” ante, at 11, n. 3, but again, what the police rea-
sonably believe will happen is of course that the suspect will
continue his flight and escape out the back. If that reason-
able belief is an exigency, then it is present in almost every
case of hot pursuit into the home. Perhaps that is why
Lange’s counsel admitted that “nine times out of ten or
more” warrantless entry in hot pursuit of misdemeanants
would be reasonable. Tr. of Oral Arg. 34.
                              III
   Although the Fourth Amendment is not “frozen” in time,
we have used the common law as a reference point for as-
sessing the reasonableness of police activity. Garner, 471
U. S., at 13. The Court errs, however, in concluding with
the suggestion that history supports its novel incentive to
flee.
   The history is not nearly as clear as the Court suggests.
The Court is forced to rely on an argument by negative im-
plication: if common law authorities supported a categorical
rule favoring warrantless entry in pursuit of felons, war-
rantless entry in pursuit of misdemeanants must have been
prohibited. That is wrong. Countless sources support the
proposition that officers could and did pursue into homes
those who had committed all sorts of offenses that the Court
seems to deem “minor.” Ante, at 8.
   For example, common law authorities describe with ap-
proval warrantless home entry in pursuit of those who had
committed an affray (public fighting), 1 W. Hawkins, Pleas
of the Crown 137 (1716), and “disorderly drinking,”
W. Simpson, The Practical Justice of the Peace and the Par-
ish Officer 26 (1761). And the doctrine of “hue and cry” per-
mitted townspeople to pursue those suspected of “misde-
meanor[s]” if the perpetrator “escape[d] into [his] house.”
R. Bevill, Law of Homicide 162–163 (1799). In colonial
18                   LANGE v. CALIFORNIA

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

America, the hue and cry extended to a “great diversity of
crimes,” including stealing livestock and revealing oneself
to be a Quaker. W. Cuddihy, The Fourth Amendment: Or-
igins and Original Meaning 244–246 (2009).
   Finally, at common law an officer could “break open
Doors, in order to apprehend Offenders” whenever a person
was arrested for “any Cause,” and thereafter escaped. 2
Hawkins, Pleas of the Crown, at 86–87 (1787) (emphasis
added). The Court’s attempt to dispose of this awkward re-
ality in a footnote, ante, at 14, n. 5, is unconvincing. Flight
and escape both present attempts to “thwart an otherwise
proper arrest,” Santana, 427 U. S., at 42, and as noted, the
common law did not differentiate among escapees based on
the perceived magnitude of their underlying offense,
R. Burn, The Justice of the Peace 101–103 (14th ed. 1780).
   Clearly the list of offenses that historically justified war-
rantless home entry in hot pursuit of a fleeing suspect were
as broad and varied as those found in a contemporary com-
pilation of misdemeanors. See also Macooh, [1993] 2
S. C. R., at 817 (concluding after review that at common law
“the right to enter in hot pursuit” was not “limited to arrest
for felonies”); Lyons v. R., [1984] 2 S. C. R. 633, 657 (recog-
nizing “right of pursuit” as a longstanding exception to
common law protection of the sanctity of the home).
   In the face of this evidence, the Court fails to cite a single
circumstance in which warrantless entry in hot pursuit was
found to be unlawful at common law. It then acknowledges
that “some of the specifics are uncertain, and commentators
did not always agree with each other.” Ante, at 14. In At-
water, we declined to forbid warrantless arrests for minor
offenses when we found “disagreement, not unanimity,
among both the common-law jurists and the text writers
who sought to pull the cases together.” 532 U. S., at 332.
The historical ambiguity is at least as pervasive here.
   Even if the common law practice surrounding hot pursuit
were unassailably clear, its treatment of the topic before us
                  Cite as: 594 U. S. ____ (2021)            19

              ROBERTS , C. J., ,concurring
                   ROBERTS       C. J., concurring
                                            in judgment

would still be incomplete. That is because the common law
did not recognize the remedy Lange seeks: exclusion of evi-
dence in a criminal case. Collins, 584 U. S., at ___ (slip op.,
at 2) (THOMAS, J., concurring). It is often difficult to con-
ceive of how common law rights were influenced by the ab-
sence of modern remedies. And in this case we have no
guidance from history as to how our doctrines surrounding
the exclusionary rule, such as inevitable discovery, would
map onto situations in which a person attempts to thwart a
public arrest by retreating to a private place. See Nix v.
Williams, 467 U. S. 431, 443–444 (1984).
                         *     *     *
   Recall the assault we started with. The officer was clos-
ing in on the suspect when he hopped the fence and stopped
in a yard. The officer starts to climb over the fence to arrest
him, but wait—was the assault a misdemeanor or a felony?
In Lange’s State of California, it could have been either de-
pending on the identity of the victim, the amount of force
used, and whether there was a weapon involved. See Cal.
Penal Code Ann. §245 (West 2014). How much force was
the man using against the teenager? Is this really the as-
sailant’s home in the first place? Pretty suspicious that he
jumped the fence just as the officer was about to grab him.
If it is his home, are there people inside and, if so, how
many? And why would the man run from a mere fight—
does he have something more serious to hide?
   By this time, of course, the assailant has probably gone
out the back door or down the fire escape and is blocks
away, with the officer unable to give a useful description—
except for how he looks from behind.

```

---

## GROUP: content/cases/Lombardo v. City of St. Louis.md  (`case`, 5 assertions)

### content_page

```
---
title: Lombardo v. City of St. Louis
type: case
citation: "594 U.S. 464 (2021)"
parallel_cite: "210 L. Ed. 2d 609; 141 S. Ct. 2239"
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2021
date_decided: ""
docket: 20-391
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
  opinion_url: "https://www.courtlistener.com/opinion/4895266/lombardo-v-st-louis/"
  cluster_id: 4895266
  opinion_id: null
  identity_checked: true
lake:
  record_id: Lombardo v. City of St. Louis
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Use of Force]]"
    role: Recent development
related:
  - "[[Graham v. Connor]]"
  - "[[Use of Force]]"
tags:
  - case
  - excessive-force
  - use-of-force
  - section-1983
  - fourteenth-amendment
holding: "A § 1983 excessive-force challenge to a fatal prone restraint of a handcuffed, leg-shackled detainee must be analyzed under the fact-specific Kingsley reasonableness factors — including the force's kind, intensity, and duration — rather than treated as per se constitutional whenever a detainee appears to resist; summary judgment for the officers was vacated and remanded."
---

# Lombardo v. City of St. Louis

*594 U.S. 464 (2021)* (No. 20-391) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4895266 → opinion 4699045 (per curiam); quote string-matched to the CL opinion text 2026-07-07 (CL carries the slip opinion, 594 U.S. ___; pin cited slip-style per S2 A3). S9 promotes. -->

## Background
Nicholas Gilbert was arrested on a minor charge and held in a St. Louis police station cell. After officers saw him acting as though he might harm himself, they entered to restrain him; a struggle ensued, and the officers handcuffed and leg-shackled Gilbert and then moved him to a prone (face-down) position on the floor. Three officers held his limbs while at least one pressed on his back and torso for roughly fifteen minutes; Gilbert said "It hurts. Stop," stopped moving, and died. His parents sued the officers under 42 U.S.C. § 1983 for excessive force. The District Court granted the officers summary judgment, and the Eighth Circuit affirmed, holding that the use of a prone restraint was not objectively unreasonable given Gilbert's resistance.

## Issue
Whether the Eighth Circuit properly analyzed the excessive-force claim under the fact-specific reasonableness factors of *[[Kingsley v. Hendrickson]]*, or instead applied a categorical rule treating prone restraint of a resisting detainee as constitutional regardless of the surrounding circumstances.

## Rule
Excessive-force reasonableness turns on a careful, case-specific balancing of the relevant *[[Kingsley v. Hendrickson|Kingsley]]* factors — including the relationship between the need for force and the amount used, the severity of the security problem, the threat reasonably perceived, and any effort to temper the force. A court may not short-circuit that inquiry with a categorical rule. As the Court put it: "Although the Eighth Circuit cited the Kingsley factors, it is unclear whether the court thought the use of a prone restraint — no matter the kind, intensity, duration, or surrounding circumstances — is per se constitutional so long as an individual appears to resist officers' efforts to subdue him." — 594 U.S. 464 (slip op., at 3). ^pin-3

## Application
Facts the Eighth Circuit had brushed aside as "insignificant" were potentially decisive under *[[Kingsley v. Hendrickson|Kingsley]]*: Gilbert was already handcuffed and leg-shackled when moved to the prone position, was held there for fifteen minutes, and was subjected to back pressure even though St. Louis trains its officers that pressing on a prone subject's back can cause suffocation — and that a prone subject's struggles may reflect oxygen deprivation rather than defiance. Because it was unclear whether the court below had weighed these facts or instead applied a [[Common Legal Terms#per-se|per se]] rule, the Court declined to resolve the excessive-force question itself and returned the case for a proper, fact-specific analysis.

## Conclusion
The judgment was **[[Reading and Citing Cases#vacated|vacated]]** and the case **[[Reading and Citing Cases#on-remand|remanded]]** for the lower courts to apply the *[[Kingsley v. Hendrickson|Kingsley]]* reasonableness inquiry to the specific facts. The opinion was **[[Common Legal Terms#per-curiam|per curiam]]**; Alito, J., joined by Thomas and Gorsuch, JJ., dissented, arguing the Court should have decided the question rather than remand.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Lombardo* is a pretrial-detainee (Fourteenth Amendment) excessive-force decision governed by *[[Kingsley v. Hendrickson|Kingsley]]*'s objective-reasonableness standard, the detention analog to *[[Graham v. Connor]]*; it reaffirms that prone-restraint reasonableness is fact-specific, not categorical.

## Appears on
- [[Use of Force]] — *Recent development*

## Sources
- [*Lombardo v. City of St. Louis*, 594 U.S. 464 (2021)](https://www.courtlistener.com/opinion/4895266/lombardo-v-st-louis/) — pinpoint: slip op., at 3 (per curiam); quote string-matched to the CL slip-opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "787b7c007d973346", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "594 U.S. 464 (2021)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "210 L. Ed. 2d 609; 141 S. Ct. 2239", "title": "Lombardo v. City of St. Louis", "year": "2021"}}
{"assertion_id": "21158884664329d3", "dimension": "support", "kind": "home_role", "locator": {"home": "Use of Force"}, "payload": {"home": "Use of Force", "role": "Recent development", "title": "Lombardo v. City of St. Louis"}}
{"assertion_id": "8714c0161abfa238", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A § 1983 excessive-force challenge to a fatal prone restraint of a handcuffed, leg-shackled detainee must be analyzed under the fact-specific Kingsley reasonableness factors — including the force's kind, intensity, and duration — rather than treated as per se constitutional whenever a detainee appears to resist; summary judgment for the officers was vacated and remanded.", "title": "Lombardo v. City of St. Louis"}}
{"assertion_id": "9014be813384f8e9", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Lombardo v. City of St. Louis"}}
{"assertion_id": "cc22282fb5c57a46", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Lombardo v. City of St. Louis", "varies_by_point": "false"}}
```

### lake record — Lombardo v. City of St. Louis

```json
{
  "schema_version": "s2.v1",
  "record_id": "Lombardo v. City of St. Louis",
  "status": "under_review",
  "identity": {
    "case_name": "Lombardo v. St. Louis",
    "case_name_short": "Lombardo",
    "case_name_full": "",
    "input_case_name": "Lombardo v. City of St. Louis",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2021,
    "docket": "20-391",
    "cluster_id": 4895266,
    "lead_opinion_id": 4699045,
    "sibling_ids": [],
    "absolute_url": "/opinion/4895266/lombardo-v-st-louis/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "594 U.S. 464",
      "volume": "594",
      "reporter": "U.S.",
      "page": "464",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "210 L. Ed. 2d 609",
        "volume": "210",
        "reporter": "L. Ed. 2d",
        "page": "609",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 2239",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "2239",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "594 U.S. 464",
        "volume": "594",
        "reporter": "U.S.",
        "page": "464",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "210 L. Ed. 2d 609",
        "volume": "210",
        "reporter": "L. Ed. 2d",
        "page": "609",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 2239",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "2239",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "594 U.S. 464",
    "official_selection": {
      "court_class": "scotus",
      "selected": "594 U.S. 464",
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
    "date_created": "2026-07-06T12:10:28Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:10:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:10:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:10:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:10:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "lombardo-v-city-of-st-louis--4895266",
      "to_record_id": "Lombardo v. City of St. Louis",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Lombardo v. City of St. Louis

```
                      Cite as: 594 U. S. ____ (2021)                     1

                                Per Curiam

SUPREME COURT OF THE UNITED STATES
    JODY LOMBARDO, ET AL. v. CITY OF ST. LOUIS,
               MISSOURI, ET AL.
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED
   STATES COURT OF APPEALS FOR THE EIGHTH CIRCUIT
                  No. 20–391.    Decided June 28, 2021

   PER CURIAM.
   On the afternoon of December 8, 2015, St. Louis police
officers arrested Nicholas Gilbert for trespassing in a con-
demned building and failing to appear in court for a traffic
ticket.1 Officers brought him to the St. Louis Metropolitan
Police Department’s central station and placed him in a
holding cell. At some point, an officer saw Gilbert tie a piece
of clothing around the bars of his cell and put it around his
neck, in an apparent attempt to hang himself. Three offic-
ers responded and entered Gilbert’s cell. One grabbed Gil-
bert’s wrist to handcuff him, but Gilbert evaded the officer
and began to struggle. The three officers brought Gilbert,
who was 5’3” and 160 pounds, down to a kneeling position
over a concrete bench in the cell and handcuffed his arms
behind his back. Gilbert reared back, kicking the officers
and hitting his head on the bench. After Gilbert kicked one
of the officers in the groin, they called for more help and leg
shackles. While Gilbert continued to struggle, two officers
shackled his legs together. Emergency medical services
personnel were phoned for assistance.
   Several more officers responded. They relieved two of the
original three officers, leaving six officers in the cell with


——————
  1 Because this case was decided by summary judgment, the evidence

here recounted is viewed “ ‘in the light most favorable’ ” to the nonmoving
party (here, Gilbert’s parents, the petitioners). Tolan v. Cotton, 572
U. S. 650, 655–656 (2014) (per curiam).
2                     LOMBARDO v. ST. LOUIS

                              Per Curiam

Gilbert, who was now handcuffed and in leg irons. The of-
ficers moved Gilbert to a prone position, face down on the
floor. Three officers held Gilbert’s limbs down at the shoul-
ders, biceps, and legs. At least one other placed pressure
on Gilbert’s back and torso. Gilbert tried to raise his chest,
saying, “ ‘It hurts. Stop.’ ” Lombardo v. Saint Louis City,
361 F. Supp. 3d 882, 898 (ED Mo. 2019).
   After 15 minutes of struggling in this position, Gilbert’s
breathing became abnormal and he stopped moving. The
officers rolled Gilbert onto his side and then his back to
check for a pulse. Finding none, they performed chest com-
pressions and rescue breathing. An ambulance eventually
transported Gilbert to the hospital, where he was pro-
nounced dead.
   Gilbert’s parents sued, alleging that the officers had used
excessive force against him. The District Court granted
summary judgment in favor of the officers, concluding that
they were entitled to qualified immunity because they did
not violate a constitutional right that was clearly estab-
lished at the time of the incident. Id., at 895. The U. S.
Court of Appeals for the Eighth Circuit affirmed on differ-
ent grounds, holding that the officers did not apply uncon-
stitutionally excessive force against Gilbert. 956 F. 3d
1009, 1014 (2020).
   In assessing a claim of excessive force, courts ask
“whether the officers’ actions are ‘objectively reasonable’ in
light of the facts and circumstances confronting them.”
Graham v. Connor, 490 U. S. 386, 397 (1989).2 “A court

——————
  2 Petitioners brought their excessive force claims under both the

Fourth and Fourteenth Amendments. See, e.g., First Amended Com-
plaint in No. 4:16–cv–01637, ECF Doc. 28 (ED Mo.), p. 46. We need not
address whether the Fourth or Fourteenth Amendment provides the
proper basis for a claim of excessive force against a pretrial detainee in
Gilbert’s position. Whatever the source of law, in analyzing an excessive
force claim, a court must determine whether the force was objectively
unreasonable in light of the “ ‘facts and circumstances of each particular
                     Cite as: 594 U. S. ____ (2021)                    3

                              Per Curiam

(judge or jury) cannot apply this standard mechanically.”
Kingsley v. Hendrickson, 576 U. S. 389, 397 (2015). Rather,
the inquiry “requires careful attention to the facts and cir-
cumstances of each particular case.” Graham, 490 U. S., at
396. Those circumstances include “the relationship be-
tween the need for the use of force and the amount of force
used; the extent of the plaintiff ’s injury; any effort made by
the officer to temper or to limit the amount of force; the se-
verity of the security problem at issue; the threat reasona-
bly perceived by the officer; and whether the plaintiff was
actively resisting.” Kingsley, 576 U. S., at 397.
   Although the Eighth Circuit cited the Kingsley factors, it
is unclear whether the court thought the use of a prone re-
straint—no matter the kind, intensity, duration, or sur-
rounding circumstances—is per se constitutional so long as
an individual appears to resist officers’ efforts to subdue
him. The court cited Circuit precedent for the proposition
that “the use of prone restraint is not objectively unreason-
able when a detainee actively resists officer directives and
efforts to subdue the detainee.” 956 F. 3d, at 1013. The
court went on to describe as “insignificant” facts that may
distinguish that precedent and appear potentially im-
portant under Kingsley, including that Gilbert was already
handcuffed and leg shackled when officers moved him to the
prone position and that officers kept him in that position for
15 minutes. See 956 F. 3d, at 1013–1015.
   Such details could matter when deciding whether to
grant summary judgment on an excessive force claim.
Here, for example, record evidence (viewed in the light most
favorable to Gilbert’s parents) shows that officers placed
pressure on Gilbert’s back even though St. Louis instructs
its officers that pressing down on the back of a prone subject
can cause suffocation. The evidentiary record also includes
——————
case.’ ” Kingsley v. Hendrickson, 576 U. S. 389, 397 (2015) (quoting Gra-
ham, 490 U. S., at 396).
4                      LOMBARDO v. ST. LOUIS

                               Per Curiam

well-known police guidance recommending that officers get
a subject off his stomach as soon as he is handcuffed be-
cause of that risk. The guidance further indicates that the
struggles of a prone suspect may be due to oxygen defi-
ciency, rather than a desire to disobey officers’ commands.
Such evidence, when considered alongside the duration of
the restraint and the fact that Gilbert was handcuffed and
leg shackled at the time, may be pertinent to the relation-
ship between the need for the use of force and the amount
of force used, the security problem at issue, and the
threat—to both Gilbert and others—reasonably perceived
by the officers. Having either failed to analyze such evi-
dence or characterized it as insignificant, the court’s opin-
ion could be read to treat Gilbert’s “ongoing resistance” as
controlling as a matter of law.3 Id., at 1014. Such a per se
rule would contravene the careful, context-specific analysis
required by this Court’s excessive force precedent.
   We express no view as to whether the officers used un-
constitutionally excessive force or, if they did, whether Gil-
bert’s right to be free of such force in these circumstances
was clearly established at the time of his death. We instead
grant the petition for certiorari, vacate the judgment of the
Eighth Circuit, and remand the case to give the court the
opportunity to employ an inquiry that clearly attends to the
facts and circumstances in answering those questions in the
first instance.
                                               It is so ordered.




——————
   3 While the dissent suggests we should give the Eighth Circuit the ben-

efit of the doubt, in assessing the appropriateness of review in this fact-
bound context, it is more prudent to afford the Eighth Circuit an oppor-
tunity to clarify its opinion rather than to speculate as to its basis.
                  Cite as: 594 U. S. ____ (2021)            1

                      ALITO, J., dissenting

SUPREME COURT OF THE UNITED STATES
   JODY LOMBARDO, ET AL. v. CITY OF ST. LOUIS,
              MISSOURI, ET AL.
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED
   STATES COURT OF APPEALS FOR THE EIGHTH CIRCUIT
               No. 20–391.   Decided June 28, 2021

   JUSTICE ALITO, with whom JUSTICE THOMAS and
JUSTICE GORSUCH join, dissenting.
   I cannot approve the Court’s summary disposition be-
cause it unfairly interprets the Court of Appeals’ decision
and evades the real issue that this case presents: whether
the record supports summary judgment in favor of the de-
fendant police officers and the city of St. Louis. The Court
of Appeals held that the defendants were entitled to sum-
mary judgment because a reasonable jury would neces-
sarily find that the police officers used reasonable force in
attempting to subdue petitioner Lombardo’s son, Nicholas
Gilbert, when he was attempting to hang himself in his cell.
In reaching this conclusion, the Court of Appeals applied
the correct legal standard and made a judgment call on a
sensitive question. This case, therefore, involves the appli-
cation of “a properly stated rule of law” to a particular fac-
tual record, and our rules say that we “rarely” review such
questions. See this Court’s Rule 10. But “rarely” does not
mean “never,” and if this Court is unwilling to allow the de-
cision below to stand, the proper course is to grant the peti-
tion, receive briefing and argument, and decide the real
question that this case presents.
   That is the course I would take. I do not think that this
Court is above occasionally digging into the type of fact-
bound questions that make up much of the work of the
lower courts, and a decision by this Court on the question
presented here could be instructive.
   The Court, unfortunately, is unwilling to face up to the
2                  LOMBARDO v. ST. LOUIS

                      ALITO, J., dissenting

choice between denying the petition (and bearing the criti-
cism that would inevitably elicit) and granting plenary re-
view (and doing the work that would entail). Instead, it
claims to be uncertain whether the Court of Appeals actu-
ally applied the correct legal standard, and for that reason
it vacates the judgment below and remands the case.
   This course of action may be convenient for this Court,
but it is unfair to the Court of Appeals. If we expect the
lower courts to respect our decisions, we should not twist
their opinions to make our job easier.
   When the Court of Appeals’ opinion is read in the way we
hope our opinions will be interpreted, it is clear that the
Court of Appeals understood and applied the correct stand-
ard for excessive-force claims. The per curiam acknowl-
edges that the Court of Appeals correctly cited the factors
that must be taken into account in determining whether the
officers’ actions were objectively reasonable. Ante, at 3; see
956 F. 3d 1009, 1013 (CA8 2020). But the per curiam finds
it “unclear whether the [Court of Appeals] thought the use
of a prone restraint—no matter the kind, intensity, dura-
tion, or surrounding circumstances—is per se constitutional
so long as an individual appears to resist officers’ efforts to
subdue him.” Ante, at 3.
   Can the Court seriously think that the Eighth Circuit
adopted such a strange and extreme position—that the use
of prone restraint on a resisting detainee is always reason-
able no matter how much force is used, no matter how long
that force is employed, no matter the physical condition of
the detainee, and no matter whether the detainee is obvi-
ously suffering serious or even life-threatening harm? Sup-
pose officers with a combined weight of 1,000 pounds knelt
on the back of a frail and infirm detainee, used all their
might to press his chest and face into a concrete floor for
over an hour, did not desist when the detainee cried, “You’re
killing me,” and ended up inflicting fatal injuries. Does the
Court really believe that the Court of Appeals might have
                 Cite as: 594 U. S. ____ (2021)            3

                     ALITO, J., dissenting

thought that this extreme use of force would be reasonable?
Is there any support for that interpretation in the Court of
Appeals’ opinion?
  The per curiam latches onto this sentence in the opinion
below: “This Court has previously held that the use of prone
restraint is not objectively unreasonable when a detainee
actively resists officer directives and efforts to subdue the
detainee.” 956 F. 3d, at 1013; see ante, at 3. Read in con-
text, its meaning is apparent.
  The sentence recounts and cites to what the Eighth Cir-
cuit had held in an earlier case, Ryan v. Armstrong, 850
F. 3d 419 (2017), in which a resisting detainee had been
held in a prone position for a period of time. In order to
understand the sentence in the opinion below, it is neces-
sary to look at that prior decision. And when the language
in the decision below is read in that way, what it obviously
means is that the use of prone restraint is not objectively
unreasonable per se when a detainee is actively resisting.
That is exactly what the appellees, citing Ryan, had argued:
“No court has held that placing a resisting prisoner in a
prone position while restrained is per se unreasonable.”
Brief for Appellees in No. 19–1469 (CA8), p. 24. That is a
correct reading of Ryan, and that is how the opinion below
interpreted it.
  Ryan held only that the use of force in that case was rea-
sonable based on “the totality of th[e] circumstances,” in-
cluding the detainee’s resistance. 850 F. 3d, at 428. The
Ryan court explained:
    “Several factors support the foregoing conclusion.
    Among the most important is the observation that [the
    detainee] was actively resisting the extraction proce-
    dure by ignoring directives to lie down on his bunk and
    resisting the defendants’ efforts to subdue him once
    they entered his cell.” Ibid. (emphasis added).
  Thus, Ryan clearly did not adopt any sort of blanket rule,
4                      LOMBARDO v. ST. LOUIS

                          ALITO, J., dissenting

and the sentence in this case that the per curiam seizes
upon did not purport to go beyond Ryan.
  This Court’s per curiam refers to one other statement in
the opinion below. The per curiam states:
     “The [Eighth Circuit] went on to describe as ‘insignifi-
     cant’ facts that may distinguish [Ryan] and appear po-
     tentially important under Kingsley, including that Gil-
     bert was already handcuffed and leg shackled when
     officers moved him to the prone position and that offic-
     ers kept him in that position for 15 minutes.” Ante, at
     3 (quoting 956 F. 3d, at 1014).
  Here, again, the per curiam strains to give the Eighth
Circuit’s opinion a possible interpretation that can justify a
remand. But when this sentence is read in context, what it
plainly means is not that the duration of the officers’ use of
force or the fact that Gilbert had been handcuffed and
shackled were irrelevant but that certain factual differ-
ences between this case and Ryan were not significant in
the sense that they did not call for a different result.
  The court used the term “insignificant” in responding to
Lombardo’s efforts to distinguish Ryan. Lombardo argued
that this case is different because Gilbert was restrained for
a longer period and, unlike the detainee in Ryan, had al-
ready been handcuffed and shackled. See 956 F. 3d, at
1014; Brief for Plaintiffs-Appellants in No. 19–1469 (CA8),
pp. 14–15. What the Eighth Circuit characterized as “in-
significant” were these factual differences between the two
cases.*

——————
  *The Eighth Circuit wrote:
  “Lombardo argues that Ryan is not on point. Specifically, Lombardo
argues that, unlike Ryan, in which the detainee was held in prone re-
straint for approximately three minutes until he was handcuffed, . . . Gil-
bert was held in prone restraint for fifteen minutes and was placed in
this position only after he had been handcuffed and leg-shackled. Lom-
bardo also argues that she presented expert testimony that Gilbert’s
                      Cite as: 594 U. S. ____ (2021)                      5

                           ALITO, J., dissenting

  Without carefully studying the record, I cannot be certain
whether I would have agreed with the Eighth Circuit panel
that summary judgment for the defendants was correct.
The officers plainly had a reasonable basis for using some
degree of force to restrain Gilbert so that he would not harm
himself, and it appears that Gilbert, despite his slight stat-
ure, put up a fierce and prolonged resistance. See 956 F. 3d,
at 1011–1014. On the other hand, the officers’ use of force
inflicted serious injuries, and the medical evidence on the
cause of death was conflicting. See id., at 1012.
  We have two respectable options: deny review of the fact-
bound question that the case presents or grant the petition,
have the case briefed and argued, roll up our sleeves, and
decide the real issue. I favor the latter course, but what we
should not do is take the easy out that the Court has chosen.




——————
cause of death was forcible restraint inducing asphyxia whereas the un-
disputed cause of death in Ryan was sudden unexpected death during
restraint. . . . We find these differences to be insignificant. This Court
has previously noted that ‘[h]andcuffs limit but do not eliminate a per-
son’s ability to perform harmful acts.’ United States v. Pope, 910 F. 3d
413, 417 (8th Cir. 2018), cert. denied, [589 U. S. ___ (2019)]. As discussed
above, the undisputed facts show that Gilbert continued to violently
struggle even after being handcuffed and leg-shackled. Specifically, after
being handcuffed, he thrashed his head on the concrete bench, causing
him to suffer a gash on his forehead, and he continued to violently thrash
and kick after being leg-shackled. Because of this ongoing resistance,
the Officers moved Gilbert to the prone position so as to minimize the
harm he could inflict on himself and others.” 956 F. 3d, at 1014.

```

---

## GROUP: content/cases/Martin v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: Martin v. United States
type: case
citation: "605 U.S. 395 (2025)"
parallel_cite: ""
neutral_cite: ""
court: U.S.
court_level: scotus
circuit: ""
year: 2025
date_decided: 2025-06-12
docket: 24-362
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
  opinion_url: "https://www.courtlistener.com/opinion/10776839/martin-v-united-states/"
  cluster_id: 10776839
  opinion_id: null
  identity_checked: true
lake:
  record_id: Martin v. United States
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Suing Federal Officers]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Bivens v. Six Unknown Named Agents]]"
tags:
  - case
  - ftca
  - federal-officer-liability
  - section-1983
  - wrong-house-raid
holding: "In an FTCA suit arising from a wrong-house raid, the § 2680(h) law-enforcement proviso overrides only that subsection's intentional-tort exception (not the discretionary-function exception), and the Supremacy Clause affords the United States no defense; the Eleventh Circuit's contrary rulings were vacated and remanded."
---

# Martin v. United States

*605 U.S. 395 (2025)* (No. 24-362) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10776839 → opinion 11243426; quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
An FBI SWAT team executing a warrant raided the wrong Atlanta house — the home of Curtrina Martin, her partner Hilliard Toi Cliatt, and her seven-year-old son — detonating a flash-bang, breaking down the door, and detaining the occupants before realizing the mistake. The family sued the United States under the Federal Tort Claims Act for the officers' negligent and intentional torts. The Eleventh Circuit affirmed summary judgment for the government on two grounds: it dismissed the negligence claims under the FTCA's discretionary-function exception, and it held the remaining intentional-tort claims defeated by a Supremacy Clause defense that shields officers whose conduct has some nexus with furthering federal policy.

## Issue
Whether the FTCA's § 2680(h) law-enforcement proviso overrides the discretionary-function exception (so that intentional-tort claims automatically proceed), and whether the Supremacy Clause affords the United States a defense in FTCA suits.

## Rule
The § 2680(h) law-enforcement proviso is textually confined: it overrides only the intentional-tort exception within that same subsection, not the discretionary-function exception or the other § 2680 exceptions — so a proviso claim must still clear those other bars. And the Supremacy Clause supplies no separate defense: because the FTCA makes the United States liable under the "law of the place" on the same terms as a private party, "in most cases there is no conflict for the Supremacy Clause to resolve." The Court held that "we find the government's concession commendable and correct: The FTCA does not permit the Eleventh Circuit's Supremacy Clause defense." — 605 U.S. at 409. ^pin-409

## Application
The Eleventh Circuit had inverted the statute — treating the proviso as automatically defeating the discretionary-function exception, then offsetting that plaintiff-friendly reading with a novel Supremacy Clause defense found nowhere in § 2674's enumerated defenses. Both moves were wrong. Georgia law (the "law of the place") would let a homeowner sue a private person who mistakenly raided and assaulted him, and no federal statute or constitutional text displaced that liability rule. [[Reading and Citing Cases#on-remand|On remand]] the Eleventh Circuit must decide whether the discretionary-function exception bars any of the claims — without the mistaken premise that the proviso overrides it — and, for surviving claims, apply Georgia's private-analog standard subject only to the § 2674 defenses.

## Conclusion
The judgment was **[[Reading and Citing Cases#vacated|vacated]]** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. Gorsuch, J., delivered the opinion of a unanimous Court; Sotomayor, J., joined by Jackson, J., filed a [[Common Legal Terms#concurring-opinion|concurring opinion]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Martin* is an FTCA decision rather than a *[[Bivens v. Six Unknown Named Agents|Bivens]]* or § 1983 case, but it is central to the remedies available against federal officers for wrong-house raids: it removes two barriers the Eleventh Circuit had erected and returns the wrong-house-raid liability question to the lower courts.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Martin v. United States*, 605 U.S. 395 (2025)](https://www.courtlistener.com/opinion/10776839/martin-v-united-states/) — pinpoint: 409–413 (Supremacy Clause holding, Opinion of the Court); quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "04a05a60bc19dda6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "605 U.S. 395 (2025)", "court": "U.S.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Martin v. United States", "year": "2025"}}
{"assertion_id": "57e2d387293b5baf", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "In an FTCA suit arising from a wrong-house raid, the § 2680(h) law-enforcement proviso overrides only that subsection's intentional-tort exception (not the discretionary-function exception), and the Supremacy Clause affords the United States no defense; the Eleventh Circuit's contrary rulings were vacated and remanded.", "title": "Martin v. United States"}}
{"assertion_id": "7315ec918122a60a", "dimension": "support", "kind": "home_role", "locator": {"home": "Suing Federal Officers"}, "payload": {"home": "Suing Federal Officers", "role": "Recent development", "title": "Martin v. United States"}}
{"assertion_id": "6ddf20518c68961f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Martin v. United States"}}
{"assertion_id": "efb507da3dae2c89", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Martin v. United States", "varies_by_point": "false"}}
```

### lake record — Martin v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Martin v. United States",
  "status": "under_review",
  "identity": {
    "case_name": "Martin v. United States",
    "case_name_short": "Martin",
    "case_name_full": "",
    "input_case_name": "Martin v. United States",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2025-06-12",
    "year": 2025,
    "docket": "24-362",
    "cluster_id": 10776839,
    "lead_opinion_id": 11243426,
    "sibling_ids": [],
    "absolute_url": "/opinion/10776839/martin-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 10603452,
        "score": 120,
        "case_name": "Martin v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "605 U.S. 395",
      "volume": "605",
      "reporter": "U.S.",
      "page": "395",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "605 U.S. 395",
        "volume": "605",
        "reporter": "U.S.",
        "page": "395",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "605 U.S. 395",
    "official_selection": {
      "court_class": "scotus",
      "selected": "605 U.S. 395",
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
    "date_created": "2026-07-07T01:37:28Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:37:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:37:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:37:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:37:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "martin-v-united-states--10776839",
      "to_record_id": "Martin v. United States",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Martin v. United States

```
                   PRELIMINARY PRINT

              Volume 605 U. S. Part 2
                             Pages 395–421




       OFFICIAL REPORTS
                                     OF


   THE SUPREME COURT
                                June 12, 2025


Page Proof Pending Publication


                    REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D. C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
                         OCTOBER TERM, 2024                              395

                                  Syllabus


   MARTIN, individually and as parent and next
    friend of G. W., a minor, et al. v. UNITED
                  STATES et al.
certiorari to the united states court of appeals for
                the eleventh circuit
       No. 24–362. Argued April 29, 2025—Decided June 12, 2025
On October 18, 2017, the FBI raided the wrong house in suburban Atlanta.
  Offcers meant to execute search and arrest warrants at a suspected
  gang hideout at 3741 Landau Lane but instead stormed 3756 Denville
  Trace, a quiet family home occupied by petitioners Hilliard Toi Cliatt,
  his partner Curtrina Martin, and her 7-year-old son. A six-member
  SWAT team breached the front door, detonated a fash-bang grenade,
  and assaulted the innocent occupants before realizing their mistake.
  The cause of the error was Special Agent Guerra's reliance on a personal
  GPS device, combined with the team's failure to notice the street sign
  for “Denville Trace” and the house number visible on the mailbox. Left
  with personal injuries and property damage, petitioners sued the United
Page Proof Pending Publication
  States under the Federal Tort Claims Act (FTCA), 28 U. S. C. § 2671
  et seq., seeking damages resulting from the offcers' alleged negligent
  and intentional actions during the raid. The district court granted
  summary judgment to the government. The Eleventh Circuit affrmed,
  applying a unique approach to FTCA claims.
The FTCA waives the federal government's sovereign immunity from suit
  as to certain torts committed by federal employees acting within the
  scope of their employment. But that waiver is subject to statutory ex-
  ceptions, including two relevant to a law enforcement misconduct case
  like this one. The frst is the intentional-tort exception in § 2680(h),
  which bars claims against the government for 11 enumerated intentional
  torts. The second is the discretionary-function exception in § 2680(a),
  which bars claims against the government that are based on an offcial's
  exercise of discretionary functions. Section 2680(h) also contains a
  “law enforcement proviso” which countermands the intentional-tort ex-
  ception, allowing suits for six specifed torts (including assault, battery,
  false imprisonment, and false arrest) to proceed against the United
  States when the torts are committed by “investigative or law enforce-
  ment offcers.” While most courts hold that the law enforcement pro-
  viso applies only to the intentional-tort exception, the Eleventh Circuit's
  approach is different in two key respects. First, the Eleventh Circuit
  alone holds that the proviso overrides all exceptions in § 2680, including
396                  MARTIN v. UNITED STATES

                                  Syllabus

  the discretionary-function exception, meaning that intentional-tort
  claims covered by the proviso automatically proceed to the merits with-
  out further analysis of other applicable § 2680 exceptions. Second, to
  compensate for this plaintiff-friendly approach, the Eleventh Circuit
  permits the government to assert a restrictive Supremacy Clause de-
  fense at the liability stage, allowing the government to escape liability
  when an offcer's actions have “some nexus with furthering federal pol-
  icy” and reasonably “compl[y] with the full range of federal law.” Den-
  son v. United States, 574 F. 3d 1318, 1348.
     Applying its distinctive approach, the Eleventh Circuit held that the
  law enforcement proviso protected petitioners' intentional-tort claims
  from both the intentional-tort and discretionary-function exceptions.
  The court dismissed petitioners' negligence claims under the
  discretionary-function exception, reasoning that Special Agent Guerra
  enjoyed discretion in preparing for the warrant execution. On the mer-
  its of the remaining intentional-tort claims, the court found the gov-
  ernment had a valid Supremacy Clause defense and granted summary
  judgment for the United States.
Held:
    1. The law enforcement proviso in § 2680(h) overrides only the
Page Proof Pending Publication
 intentional-tort exception in that subsection, not the discretionary-
 function exception or other exceptions throughout § 2680. Pp. 403–408.
      (a) The text and structure of § 2680 demonstrate that the law en-
 forcement proviso applies only to the intentional-tort exception. The
 proviso appears within the same subsection and sentence as the
 intentional-tort exception, refecting the established principle that stat-
 utory provisos generally modify only the provisions in which they ap-
 pear. Section 2680 contains 13 discrete exceptions. Coupled with the
 lead-in clause, each exception forms a separate sentence and operates
 as a structurally distinct provision. The proviso addresses the same
 subject matter as subsection (h)—intentional torts—while other excep-
 tions cover entirely different topics like lost mail, combat injuries, and
 quarantine impositions. Further, the proviso's defnitional sentence ex-
 pressly limits the defnition of “investigative or law enforcement offcer”
 to “this subsection” (i. e., subsection (h)), even though the phrase “law
 enforcement offcer” appears elsewhere in § 2680. Congress's choice to
 embed the proviso within subsection (h) rather than place it at the end
 of the full list of exceptions, as it sometimes does with broadly applicable
 provisos, further confrms the proviso's limited application to subsection
 (h) alone. Pp. 404–407.
      (b) Petitioners' arguments for broader application of the proviso
 are unpersuasive. While the proviso mirrors the language of § 2680's
                      Cite as: 605 U. S. 395 (2025)                      397

                                 Syllabus

 lead-in clause by stating that § 1346(b) “shall apply” rather than “shall
 not apply,” this textual similarity does not demonstrate that the proviso
 applies to all exceptions, which form discrete instructions that may be
 understood completely without reference to other provisions. The ab-
 sence of limiting language in the proviso's frst sentence does not expand
 its scope beyond subsection (h), as Congress accomplished that limita-
 tion through the proviso's placement within the same sentence as the
 intentional-tort exception. Legislative history suggesting Congress in-
 tended to address wrong-house raids broadly cannot displace what the
 law's terms clearly direct, as legislative history is not the law and Mem-
 bers of Congress may have had multiple purposes in mind when crafting
 the proviso. Pp. 407–408.
    2. The Supremacy Clause does not afford the United States a defense
 in FTCA suits. The FTCA is the “supreme” federal law governing
 the United States' tort liability and serves as the exclusive remedy for
 damages claims arising from federal employees' offcial conduct. The
 statute generally makes the government liable under state law on the
 same terms as a private individual would be liable under the law of the
 place where the tortious conduct occurred. Because the FTCA incor-
 porates state law as the liability standard, there is typically no confict
 between federal and state law for the Supremacy Clause to resolve.
Page Proof Pending Publication
 While federal law may sometimes displace state law in FTCA suits
 where a constitutional text or federal statute supplies controlling liabil-
 ity rules, the Eleventh Circuit identifed no such federal statute or con-
 stitutional provision displacing Georgia tort law in this case. The
 court's reliance on In re Neagle, 135 U. S. 1, is misplaced, as that 19th-
 century decision involved a federal offcer's immunity from state crimi-
 nal prosecution for acts necessary and proper in discharging federal
 duties, not the federal government's liability under a statute that ex-
 pressly subjects it to state tort law on the same terms as private parties.
 Section 2674 specifes the defenses available to the government, includ-
 ing judicial or legislative immunity and other defenses to which the
 United States is entitled, but these do not include the Eleventh Circuit's
 novel Supremacy Clause defense. Pp. 409–413.
    3. On remand, the Eleventh Circuit should consider whether subsec-
 tion (a)'s discretionary-function exception bars either the plaintiffs' neg-
 ligent- or intentional-tort claims—undertaking that assessment without
 reference to the mistaken view that the law enforcement proviso applies
 to subsection (a). The court must then ask of any surviving claims
 whether, under Georgia state law, a “private individual under like cir-
 cumstances” would be liable for the acts and omissions the plaintiffs
 allege, subject to the defenses discussed in § 2674—not a Supremacy
 Clause defense.
398                  MARTIN v. UNITED STATES

                          Opinion of the Court

     Remaining questions surrounding whether and under what circum-
  stances the discretionary-function exception may ever foreclose a suit
  like this one lie well beyond the two questions the Court granted certio-
  rari to address, and their resolution would beneft from the Eleventh
  Circuit's careful reexamination of this case in the first instance.
  Pp. 413–415.
Vacated and remanded.

   Gorsuch, J., delivered the opinion for a unanimous Court. Soto-
mayor, J., fled a concurring opinion, in which Jackson, J., joined, post,
p. 415.

  Patrick Jaicomo argued the cause for petitioners. With
him on the briefs were Anya Bidwell and Jared McClain.
  Frederick Liu argued the cause for respondents. With
him on the brief were Acting Solicitor General Harris, Act-
ing Assistant Attorney General Roth, Deputy Solicitor Gen-
eral Kneedler, and Joshua M. Salzman.
  Christopher Mills, by invitation of the Court, 604 U. S.
Page Proof Pending Publication
1115, argued the cause and fled a brief as amicus curiae in
support of the judgment below on Question 1.*

  Justice Gorsuch delivered the opinion of the Court.
  If federal offcers raid the wrong house, causing property
damage and assaulting innocent occupants, may the home-
owners sue the government for damages? The answer is

  *Briefs of amici curiae urging reversal were fled for America's Future
et al. by William J. Olson, Jeremiah L. Morgan, Robert J. Olson, and
Jeffrey C. Tuomala; for the Constitutional Accountability Center by Eliz-
abeth B. Wydra and Brianne J. Gorod; for Members of Congress by Jona-
than C. Bond, Jeff Liu, and Lavi M. Ben Dor; for the National Police
Accountability Project et al. by Charles A. Rothfeld, Paul W. Hughes,
Eugene R. Fidell, and John W. Whitehead; for the New Civil Liberties
Alliance by Casey Norman, Jenin Younes, and Mark Chenoweth; for the
North Central Pennsylvania Trial Lawyers Association by Paul Koster;
for Public Accountability et al. by Athul K. Acharya, Clark M. Neily III,
Cecillia D. Wang, Brett M. Kaufman, Scott Michelman, and Cory Isaac-
son; for Public Citizen by Scott L. Nelson and Allison M. Zieve; and for
Gregory C. Sisk by Geoffrey M. Pipoly and Matthew Stanford.
                  Cite as: 605 U. S. 395 (2025)           399

                     Opinion of the Court

not as obvious as it might be. All agree that the Federal
Tort Claims Act permits some suits for wrong-house raids.
But the scope of the Act's permission is much less clear.
This case poses two questions about the Act's application:
one concerning the FTCA's sovereign-immunity waiver, and
the other touching on the defenses the United States may
assert.
                            I
                               A
   In the predawn hours of October 18, 2017, the Federal Bu-
reau of Investigation raided the wrong house in suburban
Atlanta. Offcers meant to execute search and arrest war-
rants at a suspected gang hideout, 3741 Landau Lane. In-
stead, they stormed a quiet family home, 3756 Denville
Trace, occupied by Hilliard Toi Cliatt, his partner Curtrina
Martin, and her 7-year-old son G. W. App. to Pet. for Cert.
3a–4a.
Page Proof Pending Publication
   A six-member SWAT team, led by FBI Special Agent
Lawrence Guerra, breached the front door and detonated a
fash-bang grenade. Id., at 7a–8a. Fearing a home inva-
sion, Mr. Cliatt and Ms. Martin hid in a bedroom closet. Id.,
at 8a. But the SWAT team soon found the couple's hiding
spot, dragged Mr. Cliatt from the closet, “threw [him] down
on the foor,” handcuffed him, and began “bombarding [him]
with . . . questions.” Id., at 79a. Meanwhile, another off-
cer trained his weapon on Ms. Martin, who was lying on the
foor half-naked, having fallen inside the closet. Id., at 8a,
89a. Only then did another offcer stumble across some mail
with the home's address on it and realize the team had the
wrong house. Id., at 8a.
   The cause of the offcers' mistake? In preparation for the
raid, Agent Guerra visited the correct house to document its
features and identify a staging area for the SWAT team.
Id., at 5a. But, he says, when he used his personal GPS to
navigate to 3741 Landau Lane on the day of the raid, it led
400               MARTIN v. UNITED STATES

                       Opinion of the Court

him to 3756 Denville Trace. 631 F. Supp. 3d 1281, 1287 (ND
Ga. 2022). No one could confrm as much later because
Agent Guerra “threw . . . away” his GPS device “not long
after” the raid. Id., at 1288. And it seems the agents no-
ticed neither the street sign for “Denville Trace” nor the
house number, which was visible on the mailbox at the end
of the driveway. Ibid.; Tr. of Oral Arg. 38. Apparently,
too, Agent Guerra failed to appreciate that a different car
was parked in the driveway, one “not present . . . during [his]
previous visit.” 631 F. Supp. 3d, at 1288.
   Left with personal injuries and property damage—but few
explanations and no compensation—Mr. Cliatt and Ms. Mar-
tin sued the United States. They did so under the Federal
Tort Claims Act, 28 U. S. C. § 2671 et seq., alleging that the
offcers had committed various negligent and intentional
torts, App. 8–14.
                               B

Page       Proof
  After discovery  andPending
                        motions practice, Publication
                                            the district court
rejected each of the plaintiffs' claims and granted summary
judgment to the government. The Eleventh Circuit af-
frmed and, in doing so, relied on an understanding of the
FTCA that no other circuit has adopted. To appreciate
what sets the Eleventh Circuit apart and how its approach
affected its analysis of the plaintiffs' claims, it helps to begin
by outlining how this suit would have proceeded elsewhere.
   The FTCA allows those injured by federal employees to
sue the United States for damages. The statute achieves
that end by waiving, in 28 U. S. C. § 1346(b), the federal gov-
ernment's sovereign immunity for “certain torts committed
by federal employees acting within the scope of their
employment.” Brownback v. King, 592 U. S. 209, 212
(2021) (internal quotation marks omitted). But the statute's
waiver is subject to 13 exceptions that claw back the govern-
ment's immunity in certain circumstances. Set out in § 2680,
most of these 13 exceptions are obviously inapplicable to
suits alleging police misconduct within the United States.
                    Cite as: 605 U. S. 395 (2025)             401

                       Opinion of the Court

But two in particular—the discretionary-function exception
and the intentional-tort exception—sometimes come into
play.
   In a suit like this one, most courts begin by assessing the
intentional-tort exception. Located in subsection (h) of
§ 2680, it prohibits claims alleging any of 11 enumerated
torts. But the exception is itself subject to a “law enforce-
ment proviso.” Millbrook v. United States, 569 U. S. 50, 55
(2013). That proviso countermands the exception with re-
spect to six intentional torts (including assault, battery, false
imprisonment, and false arrest) by “investigative or law en-
forcement offcers.” § 2680(h). So if a plaintiff alleges that
a federal law enforcement offcer committed one or more of
those six torts, the proviso will ensure those claims survive
an encounter with the intentional-tort exception. Id., at
55–56.
   Next, most courts turn to the discretionary-function ex-
Page Proof Pending Publication
ception. Housed in subsection (a) of § 2680, this exception
bars “[a]ny claim” based on the exercise of an offcial's “dis-
cretionary function.” Faced with that instruction, most
courts ask whether the exception precludes any of the plain-
tiff's remaining tort claims. And here, the answer is often
less clear cut. The discretionary-function exception, this
Court has said, forbids suits challenging decisions that “in-
volv[e] an element of judgment or choice” of a “kind that
the . . . exception was designed to shield.” United States v.
Gaubert, 499 U. S. 315, 322–323 (1991) (alteration in original;
internal quotation marks omitted). But several of our lower
court colleagues report that they have “struggl[ed]” to dis-
cern what this direction requires of them. See, e. g., Xi v.
Haugen, 68 F. 4th 824, 842 (CA3 2023) (Bibas, J., concurring).
So, for example, some lower courts have held that the
discretionary-function exception does not shield “careless” or
“unconstitutional” police conduct from judicial scrutiny, but
others have taken a contrary view and read the exception
much more broadly. Id., at 843; Pet. for Cert. 28–34.
402              MARTIN v. UNITED STATES

                      Opinion of the Court

   Finally, if any of the plaintiff 's claims survive the
discretionary-function exception and thus fall within the
FTCA's waiver of sovereign immunity, courts turn to a third
question: Is the government liable to the plaintiff on the mer-
its? When it comes to that question, the FTCA provides that
the government will usually be liable to the plaintiff if a
“private individual under like circumstances,” § 2674, would
be liable under “the law of the place” where the government
employee's wrongful “act or omission occurred,” § 1346(b)(1).
Ordinarily, then, courts will fnd for the plaintiff if he can
demonstrate that federal offcials committed a tort under ap-
plicable state law. See Brownback, 592 U. S., at 218.
   Now compare that approach to the Eleventh Circuit's.
That court begins much as others do, asking whether the
law enforcement proviso permits a plaintiff's intentional-tort
claims to advance past subsection (h)'s intentional-tort ex-
ception. See Nguyen v. United States, 556 F. 3d 1244, 1260
Page Proof Pending Publication
(2009).
   But from there, the Eleventh Circuit proceeds quite differ-
ently. Rather than asking whether the discretionary-
function exception bars either the plaintiff's negligent-tort
claims or his intentional-tort claims, as most courts do, the
Eleventh Circuit applies that exception only to the plaintiff's
negligence claims. The Eleventh Circuit does so because, in
its view, the law enforcement proviso does not just override
the intentional-tort exception, it also overrides all the other
exceptions in § 2680, the discretionary-function exception in-
cluded. Id., at 1257. Under that approach, any intentional-
tort claim covered by the proviso automatically proceeds to
the merits—no matter what any other exception has to say.
   To compensate for its expansive and plaintiff-friendly
reading of the proviso, the Eleventh Circuit then takes a re-
strictive and defendant-friendly view at the FTCA's liability
stage. In other courts, an FTCA plaintiff will usually pre-
vail if he can show a “private individual under like circum-
stances,” § 2674, would be liable under “the law of the place”
                    Cite as: 605 U. S. 395 (2025)             403

                       Opinion of the Court

where the government employee's wrongful “act or omission
occurred,” § 1346(b)(1). But in the Eleventh Circuit, the
government may assert a particular affrmative defense
under the Constitution's Supremacy Clause. See Denson v.
United States, 574 F. 3d 1318, 1347 (2009). And that de-
fense, the Eleventh Circuit holds, defeats a claim whenever a
law enforcement offcer's contested actions bear “some nexus
with furthering federal policy and can reasonably be charac-
terized as complying with the full range of federal law.” Id.,
at 1348; accord, Kordash v. United States, 51 F. 4th 1289,
1293 (CA11 2022).
   Applying its unique approach to this case, the Eleventh
Circuit held that the law enforcement proviso spared the
plaintiffs' intentional-tort claims from both the intentional-
tort and the discretionary-function exceptions. It dismissed
the plaintiffs' negligence claims under the discretionary-
function exception because, in its view, Agent Guerra “en-
joyed discretion in how he prepared for the warrant execu-
Page Proof Pending Publication
tion.” App. to Pet. for Cert. 17a–18a. And on the merits
of the plaintiffs' (remaining) intentional-tort claims, the court
held that the government had a winning Supremacy Clause
defense. As a result, the Eleventh Circuit concluded, the
United States was entitled to summary judgment. Id., at
18a–19a.
   We agreed to take this case to examine the distinctive
features of the Eleventh Circuit's approach—namely (1)
whether the law enforcement proviso overrides not just the
intentional-tort exception but also the discretionary-function
exception, and (2) whether the Supremacy Clause affords the
United States a defense in FTCA suits. Pet. for Cert. 16,
25. 604 U. S. 1103 (2025).
                                II
  Begin with the law enforcement proviso. Does it counter-
mand only § 2680(h)'s intentional-tort exception, as most cir-
cuits have concluded and the government argues? Brief for
Respondents 25; Xi, 68 F. 4th, at 842 (Bibas, J., concurring)
404                MARTIN v. UNITED STATES

                        Opinion of the Court

(collecting cases). Or does the proviso also override the
other exceptions in § 2680, including the discretionary-
function exception in subsection (a), as the Eleventh Circuit
has held and the plaintiffs contend? Nguyen, 556 F. 3d, at
1257; Brief for Petitioners 40.

                                A
   To answer that question, we turn to the relevant statutory
text. Recall that § 1346(b) waives the federal government's
sovereign immunity, subject to a list of 13 exceptions housed
in § 2680. Those exceptions are lettered (a) through (n),
with one letter unused. Rather than setting the law en-
forcement proviso apart as a discrete provision at the end of
that list, Congress folded it into subsection (h)'s intentional-
tort exception. Here's a sense of how the proviso (under-
lined below) appears in context.
         “The provisions of this chapter and section 1346(b) of
Page Proof Pending Publication
      this title shall not apply to—
         “(a) Any claim based upon an act or omission of an
      employee of the Government, exercising due care, in the
      execution of a statute or regulation, whether or not such
      statute or regulation be valid, or based upon the exer-
      cise or performance or the failure to exercise or perform
      a discretionary function or duty on the part of a federal
      agency or an employee of the Government, whether or
      not the discretion involved be abused.
      .              .             .             .              .
         “(h) Any claim arising out of assault, battery, false im-
      prisonment, false arrest, malicious prosecution, abuse of
      process, libel, slander, misrepresentation, deceit, or in-
      terference with contract rights: Provided, That, with re-
      gard to acts or omissions of investigative or law enforce-
      ment offcers of the United States Government, the
      provisions of this chapter and section 1346(b) of this title
      shall apply to any claim arising, on or after the date of
      the enactment of this proviso, out of assault, battery,
                   Cite as: 605 U. S. 395 (2025)            405

                      Opinion of the Court

    false imprisonment, false arrest, abuse of process, or ma-
    licious prosecution. For the purpose of this subsection,
    `investigative or law enforcement offcer' means any of-
    fcer of the United States who is empowered by law to
    execute searches, to seize evidence, or to make arrests
    for violations of Federal law.
.               .              .              .              .
       “(n) Any claim arising from the activities of a Federal
    land bank, a Federal intermediate credit bank, or a bank
    for cooperatives.”
   The proviso's placement supplies an immediate clue about
the scope of its application. It appears in the same subsec-
tion (and the same sentence) as the intentional-tort excep-
tion. Given that arrangement, an ordinary reader would
naturally presume that the proviso modifes only subsection
(h). An everyday example helps illustrate the point. Sup-
pose a wife leaves her husband a shopping list: “Please buy—
Page Proof Pending Publication
Apples. Carrots. Steak: If there is a sale. Bread. Milk.”
The wife, we think, would be understandably frustrated if
her husband returned home with only steak in hand because
he could fnd nothing else discounted. Refecting that intu-
ition about ordinary meaning, our cases recognize that, ab-
sent reason to think otherwise, statutory provisos generally
modify only the provisions in which they sit. See McDon-
ald v. United States, 279 U. S. 12, 20–21 (1929); Alaska v.
United States, 545 U. S. 75, 106 (2005); A. Scalia & B. Garner,
Reading Law 154–155 (2012) (Scalia & Garner).
   Nothing about § 2680(h)'s proviso gives us reason to think
it works differently. To the contrary, one textual clue after
another confrms that it follows the general rule. Start with
the statute's grammatical structure. Section 2680 contains
a lead-in clause (“The provisions of this chapter and section
1346(b) of this title shall not apply to—”) followed by a list
of exceptions. In conjunction with the lead-in clause, each
exception forms a stand-alone sentence ending with a period,
operating as a “distinct,” “structurally discrete” provision.
406               MARTIN v. UNITED STATES

                       Opinion of the Court

Jama v. Immigration and Customs Enforcement, 543 U. S.
335, 344, and n. 4 (2005). And, given that, it is hard to see
how the law enforcement proviso might apply beyond sub-
section (h), modifying exceptions housed in separate subsec-
tions (and separate sentences) elsewhere in § 2680.
   Notice, too, that subsection (h) and its proviso work to-
gether to address the same category of claims: intentional
torts. Subsection (h)'s intentional-tort exception excludes
from the FTCA's sovereign-immunity waiver claims for torts
like “assault, battery, false imprisonment, [and] false arrest.”
The proviso then undoes that assertion of sovereign immu-
nity for some of those same torts when committed by “inves-
tigative or law enforcement offcers.” By contrast, the pro-
viso does not so much as mention the issues addressed by
§ 2680's other exceptions, like claims for lost mail, combat
injuries, or the imposition of quarantines. § 2680(b), (f), ( j).
That the proviso is “confned” to the same “subject-matter”
Page Proof Pending Publication
as subsection (h)'s “principal clause” stands as more evidence
yet that it “refers only to the provision to which it is
attached.” United States v. Morrow, 266 U. S. 531, 535
(1925).
   The proviso's second sentence is telling as well. It defnes
the phrase “investigative or law enforcement offcer.” In
doing so, the sentence tells us that the defnition applies only
to “this subsection” (i. e., subsection (h)), even though the
phrase “law enforcement offcer” also appears in subsection
(c)'s exception for claims arising from tax and customs collec-
tion. § 2680(c), (h). If Congress had wished the proviso to
modify each of the exceptions in § 2680, it might have pro-
vided a section-wide defnition, rather than a limited defni-
tion just for subsection (h).
   If more evidence were needed, comparing this statute with
others would supply it. Often, Congress drafts statutory
lists followed by a proviso in a separate paragraph at the
end. See, e. g., 42 U. S. C. §§ 1383(a)(2)(F)(ii)(II), 6928(f)(2).
Sometimes, that placement can suggest that a proviso relates
                   Cite as: 605 U. S. 395 (2025)             407

                      Opinion of the Court

to all the preceding subparts, not just the nearest one.
Scalia & Garner 156. But here Congress chose a different
course, folding the proviso into a single exception, rather
than appending it to the end of the full list of exceptions.
And that choice, too, suggests this proviso applies to subsec-
tion (h) alone. See Ysleta del Sur Pueblo v. Texas, 596 U. S.
685, 704 (2022).
                              B
   Seeking to defend the Eleventh Circuit's view that the
proviso applies broadly across all of § 2680's exceptions, the
plaintiffs offer a number of thoughtful arguments. But, to
our eyes, none can overcome the textual evidence we have
just laid out.
   First, the plaintiffs ask us to focus on how the proviso mir-
rors § 2680's lead-in clause. Brief for Petitioners 42. The
lead-in clause, they observe, preserves the government's sov-
ereign immunity by instructing that § 1346(b)'s waiver “shall
Page Proof Pending Publication
not apply to” claims covered by the exceptions. § 2680 (em-
phasis added). Meanwhile, the proviso countermands that
direction by instructing that § 1346(b)'s waiver “shall apply”
to certain claims. § 2680(h) (emphasis added). Because the
language of the proviso mirrors the language of the lead-in
clause, the plaintiffs submit, Congress must have meant for
the proviso to have the last word with respect to each of the
FTCA's exceptions. Id., at 42. That conclusion, however,
does not follow from its premise. Yes, the proviso and lead-
in clause contain similar language. And, yes, the proviso
surely countermands the lead-in clause for purposes of sub-
section (h). But none of that means the proviso speaks to
other exceptions that work together with the lead-in lan-
guage to form discrete instructions that “may be understood
completely without reading any further.” Jama, 543 U. S.,
at 344.
   Second, the plaintiffs remind us that the proviso's second,
defnitional sentence applies to “this subsection,” but the
proviso's frst, substantive part contains no such limiting lan-
408               MARTIN v. UNITED STATES

                      Opinion of the Court

guage. Brief for Petitioners 42–43 (quoting § 2680(h)).
And that difference, the plaintiffs say, suggests that the frst,
substantive part applies throughout § 2680. Id., at 42–43.
Again, however, we do not see it. Congress had no need to
include similar limiting language in the frst part of the pro-
viso to confne its application to subsection (h). Congress
accomplished just that by placing the proviso's frst part in
the same sentence as the intentional-tort exception. Mean-
while, in the proviso's second sentence, Congress arguably
needed to confne the defnition of “investigative or law en-
forcement offcer” to “this subsection” to ensure that the
phrase “law enforcement offcer” carries a different meaning
when it appears in subsection (c).
   Third, the plaintiffs resort to legislative history. They
point to a committee report discussing how Congress
enacted the proviso in response to two wrong-house raids
much like their own. Id., at 8–10, 44; see S. Rep. No. 93–
Page Proof Pending Publication
588, p. 3 (1973). And, the plaintiffs argue, unless the proviso
is given broad effect across § 2680, it will not fulfll Con-
gress's purpose of ensuring that wrong-house-raid cases may
proceed. But this argument stumbles, too. Few pieces of
legislation pursue any single “purpos[e] at all costs.” Amer-
ican Express Co. v. Italian Colors Restaurant, 570 U. S. 228,
234 (2013) (internal quotation marks omitted). And Mem-
bers of Congress may well have had more than one purpose
in mind when adding the proviso to the FTCA. Perhaps
some thought amending subsection (h) alone and leaving oth-
ers untouched would strike a suitable balance between im-
munity and liability. Perhaps others concluded there was no
need to apply the proviso more broadly because no other
exception would shield the government from liability for
wrong-house raids. Whatever the reason, no amount of
guesswork about the purposes behind legislation can displace
what the law's terms clearly direct. “[L]egislative history
is not the law.” Epic Systems Corp. v. Lewis, 584 U. S. 497,
523 (2018).
                   Cite as: 605 U. S. 395 (2025)            409

                      Opinion of the Court

                               III
   That takes us to the Eleventh Circuit's second outlier posi-
tion and the second question presented. May the United
States defeat an FTCA suit by invoking the Supremacy
Clause and showing that a federal offcer's acts had “some
nexus with furthering federal policy” and “compl[ied] with
the full range of federal law”? App. to Pet. for Cert. 17a
(internal quotation marks omitted). Because the govern-
ment now concedes that it enjoys no such defense, the Court
appointed Christopher Mills as amicus to represent the
Eleventh Circuit's views. 604 U. S. 1115 (2025). He has
ably discharged his responsibilities. But in the end, we fnd
the government's concession commendable and correct: The
FTCA does not permit the Eleventh Circuit's Supremacy
Clause defense.
   The Supremacy Clause supplies a rule of decision when
federal and state laws confict. It provides that the “Consti-
Page Proof Pending Publication
tution, and the Laws of the United States which shall be
made in Pursuance thereof . . . shall be the supreme Law of
the Land . . . any Thing in the Constitution or Laws of any
state to the Contrary notwithstanding.” Art. VI, cl. 2. So,
for example, when a regulated party cannot comply with
both federal and state directives, the Supremacy Clause tells
us the state law must yield. See, e. g., Virginia Uranium,
Inc. v. Warren, 587 U. S. 761, 767 (2019) (opinion of Gor-
such, J.).
   The FTCA is the “supreme” federal law addressing the
United States' liability for torts committed by its agents. It
supplies the “exclusive remedy” for damages claims arising
out of federal employees' offcial conduct. See Hui v. Cas-
taneda, 599 U. S. 799, 806 (2010). And, as we have seen, the
government will usually be liable if a “private individual
under like circumstances,” § 2674, “would be liable to the
claimant in accordance with the law of the place where the
act or omission occurred,” § 1346(b)(1). Accordingly, a plain-
tiff may generally prevail in an FTCA suit by demonstrating
410               MARTIN v. UNITED STATES

                       Opinion of the Court

that “the State in which the alleged misconduct occurred
would permit a cause of action for that misconduct to go
forward.” Carlson v. Green, 446 U. S. 14, 23 (1980).
   Because the FTCA's liability rule incorporates state law,
in most cases there is no confict for the Supremacy Clause to
resolve. Take this case. Georgia law supplies the relevant
“law of the place” where the offcers' tortious conduct oc-
curred. § 1346(b)(1). And Georgia law would permit a
homeowner to sue a private person for damages if that per-
son intentionally or negligently raided his house and as-
saulted him. See App. 10–13 (citing Hendricks v. Southern
Bell Tel. & Tel. Co., 193 Ga. App. 264, 264–265, 387 S. E. 2d
593, 594–595 (1989), for assault and battery and Lyttle v.
United States, 867 F. Supp. 2d 1256, 1301 (MD Ga. 2012), for
negligence). So when the FTCA, the relevant federal law
in this feld, instructs courts to apply those same state rules
to decide whether the United States is liable to the plaintiffs,
there is no discord between the two.
Page Proof Pending Publication
   To be sure, it is possible (though rare) for federal and state
law to confict in an FTCA suit. So, for example, in Hess
v. United States, this Court held that federal maritime law
supplied the “law of the place” governing an FTCA suit in-
volving an accident on the Columbia River. 361 U. S. 314,
318, and n. 7 (1960). Though the accident “occurred within
the State of Oregon,” it happened “on navigable waters . . .
within the reach of admiralty jurisdiction.” Id., at 318. As
a result, federal maritime law displaced state tort law, just
as it would in “an action between private parties.” Ibid,
n. 7. In much the same way, federal law will control other
FTCA suits where “a litigant [can] point specifcally to a con-
stitutional text or a federal statute” that supplies controlling
liability rules, displacing contrary state law. Virginia Ura-
nium, 587 U. S., at 767 (internal quotation marks omitted);
see, e. g., PLIVA, Inc. v. Mensing, 564 U. S. 604, 618 (2011).
   In this case, however, the Eleventh Circuit did not identify
any federal statute or constitutional provision displacing
Georgia tort law. Instead, the court of appeals pointed to a
                      Cite as: 605 U. S. 395 (2025)                  411

                          Opinion of the Court

line of cases stemming from this Court's decision in In re
Neagle, 135 U. S. 1, 75 (1890). App. to Pet. for Cert. 16a–
17a (citing Denson, 574 F. 3d, at 1336–1337). Those cases,
the Eleventh Circuit has observed, hold that federal offcers
may sometimes defeat state prosecutions against them by
demonstrating that their actions, though criminal under
state law, were “necessary and proper” in the discharge of
their federal responsibilities. Id., at 1346–1347 (discussing
In re Neagle). In the Eleventh Circuit's view, that same
logic works to foreclose FTCA suits like the plaintiffs'. 574
F. 3d, at 1346–1347; Kordash, 51 F. 4th, at 1293–1294.
   To appreciate why that view is mistaken, a little history
helps. In re Neagle involved an affair, a homicide, and a
habeas petition. In 1883, Sarah Althea Hill claimed to be
the wife of U. S. Senator William Sharon and sought a share
of his fortune in acrimonious California divorce proceedings.
Sharon admitted an affair but insisted that Hill had forged
Page Proof Pending Publication
the pair's handwritten marriage contract. Hill hired David
Terry to represent her. A former Chief Justice of the Cali-
fornia Supreme Court, Terry had resigned that post after
killing (another) U. S. Senator in a duel. As the litigation
wore on, lawyer and client married.
   Eventually, the dispute between Hill and Sharon wound
up before U. S. Supreme Court Justice Stephen Field while
he was riding circuit. Terry and Justice Field were no
strangers, having served together on the California Supreme
Court. Even so, Justice Field issued a devastating ruling
against Hill. As he announced his decision, Hill leapt from
her seat, denounced the Justice as “bought,” and had to be
carried from the courtroom. Joining the fracas, Terry
punched a marshal and brandished a bowie knife. Even
after the couple spent time in jail for contempt, they contin-
ued to issue threats against Justice Field.1

  1
   For a full account of the saga, see In re Neagle, 135 U. S., at 42–55;
W. Lewis, The Supreme Court and a Six-Gun: The Extraordinary Story of
In re Neagle, 43 A. B. A. J. 415 (1957) (Lewis).
412              MARTIN v. UNITED STATES

                      Opinion of the Court

  Those events found their way into the U. S. Reports this
way. Aware of the threat Hill and Terry posed, the U. S.
Attorney General ordered Deputy Marshal David Neagle, a
former chief of police in Tombstone, Arizona, to accompany
Justice Field when he next rode circuit in California. Lewis
478; In re Neagle, 135 U. S., at 51–52. That decision proved
prescient, for Terry soon cornered the Justice on a train and
attacked him. Id., at 52–54. Intervening to protect the
Justice, Neagle shot and killed Terry. Ibid. After the
shooting, California authorities arrested Neagle and began
prosecuting him for murder. Neagle countered by fling a
petition for a writ of habeas corpus in federal court seeking
his release. Ibid.
  When Neagle's petition reached this Court, it agreed the
writ should issue, reasoning that the Supremacy Clause
shielded him from state criminal charges. Without some
such protection, the Court concluded, California could frus-
Page Proof Pending Publication
trate federal law by prosecuting a federal marshal “for an
act which he was authorized to do by the law of the United
States,” an act “which it was his duty to do,” and in circum-
stances where he “did no more than what was necessary and
proper.” Id., at 75–76.
  Memorable as In re Neagle may be, we do not see how it
informs the prosaic task of applying the FTCA. The Court's
decision may stand for the proposition that federal law will
sometimes preempt a state criminal law when it conficts
with a federal offcer's duties—and do so even in the absence
of express federal legislation overriding the state law in
question. But In re Neagle does not speak to a situation
where, as here, Congress has entered the feld and expressly
bound the federal government to accept liability under state
tort law on the same terms as a “private individual.” § 2674.
After all, no private individual could deploy In re Neagle to
his advantage. It has only ever worked to shield “[f]ederal
offcers who are discharging their duties.” Ohio v. Thomas,
173 U. S. 276, 283 (1899); see also In re Neagle, 135 U. S., at
                        Cite as: 605 U. S. 395 (2025)                       413

                            Opinion of the Court

62 (“offcers and agents . . . acting . . . within the scope of
their authority”); Davis v. Burke, 179 U. S. 399, 402 (1900)
(“an offcer of the United States [who] has been arrested
under state process for acts done under the authority of the
Federal government”).2
   To be sure, the government may raise other defenses
against tort liability, and some may be uniquely federal in
nature. After setting forth the general rule that the gov-
ernment can be held liable under state tort law on the same
terms as a “private individual,” § 2674 adds that the govern-
ment may “assert any defense based upon judicial or legisla-
tive immunity which otherwise would have been available to
the employee of the United States whose act or omission
gave rise to the claim, as well as any other defenses to which
the United States is entitled.” But none of these defenses
include In re Neagle. That decision did not recognize a “ju-
dicial or legislative immunity.” Nor has it been understood
Page Proof Pending Publication
as a “defens[e] to which the United States is entitled,” but
instead (and again) as a shield “[f]ederal offcers” may assert.
Thomas, 173 U. S., at 283. Had Congress wanted to refash-
ion In re Neagle into a new defense the government itself
can assert under the FTCA, it might have said so. Yet it
did not.
                              IV
  Where does all that leave the case before us? We can say
this much: The plaintiffs' intentional-tort claims survive

  2
    To date at least, this Court has also generally understood In re Neagle
as providing federal offcers a shield against only state criminal prosecu-
tion, not (as here) state tort liability. See, e. g., Thomas, 173 U. S., at 283–
285 (favorably citing In re Waite, a case holding that the defense would
permit “a civil action for damages,” even where it barred “a criminal
prosecution,” because a damages action, unlike a prosecution, would not
bring the “federal and state governments into confict,” 81 F. 359, 363–364
(ND Iowa 1897)); Johnson v. Maryland, 254 U. S. 51, 56 (1920) (suggesting
that the defense would not foreclose “liability under the common law of a
State” for “negligence”).
414               MARTIN v. UNITED STATES

                      Opinion of the Court

their encounter with subsection (h) thanks to the law en-
forcement proviso, as the Eleventh Circuit recognized. But
it remains for that court on remand to consider whether sub-
section (a)'s discretionary-function exception bars either the
plaintiffs' negligent- or intentional-tort claims. As we have
explained, the Eleventh Circuit must undertake that assess-
ment without reference to its mistaken view that the law
enforcement proviso applies to subsection (a). Should some
or all of the plaintiffs' claims survive the discretionary-
function exception, the Eleventh Circuit must then ask
whether, under Georgia state law, a “private individual
under like circumstances” would be liable for the acts and
omissions the plaintiffs allege, subject to the defenses dis-
cussed in § 2674—not a Supremacy Clause defense nowhere
mentioned there.
   Having resolved that much, the plaintiffs ask us to decide
more still. See Brief for Petitioners 19–40. In particular,
Page Proof Pending Publication
they call on us to determine whether and under what circum-
stances the discretionary-function exception bars suits for
wrong-house raids and similar misconduct. Unless we take
up that further question, they worry, the Eleventh Circuit
on remand may take too broad a view of the exception and
dismiss their claims again. After all, the plaintiffs observe,
in the past that court has suggested that the discretionary-
function exception bars any claim “unless a source of federal
law `specifcally prescribes' a course of conduct” and thus de-
prives an offcial of all discretion. Id., at 36 (quoting Shivers
v. United States, 1 F. 4th 924, 931 (CA11 2021)). And that
approach, the plaintiffs insist, is both seriously mistaken and
at odds with how other circuits understand the exception.
Brief for Petitioners 36. Some courts, for instance, have
held that the discretionary-function exception does not pro-
tect conduct “marked by individual carelessness or laziness,”
rather than “policy considerations.” Rich v. United States,
811 F. 3d 140, 147 (CA4 2015). Some courts do not apply the
exception when law enforcement offcers violate the plain-
                   Cite as: 605 U. S. 395 (2025)             415

                    Sotomayor, J., concurring

tiffs' constitutional rights. Xi, 68 F. 4th, at 839 (“govern-
ment offcials never have discretion to violate the Constitu-
tion”). And some have indicated that the exception does not
protect “ministerial” tasks. See id., at 843 (Bibas, J., con-
curring). The plaintiffs ask us to endorse decisions like
these, apply their reasoning to this case, and hold it survives
the discretionary-function exception. Brief for Petitioners
39–40.
   We readily acknowledge that different lower courts have
taken different views of the discretionary-function exception.
We acknowledge, too, that important questions surround
whether and under what circumstances that exception may
ever foreclose a suit like this one. But those questions lie
well beyond the two we granted certiorari to address. And
before addressing them, we would beneft from the Eleventh
Circuit's careful reexamination of this case in the frst in-
stance. It is work enough for the day to answer the ques-
tions we took this case to resolve, clear away the two faulty
Page Proof Pending Publication
assumptions on which that court has relied in the past, and
redirect it to the proper inquiry.
   The judgment of the Eleventh Circuit is vacated, and the
case is remanded for further proceedings consistent with
this opinion.
                                              It is so ordered.

  Justice Sotomayor, with whom Justice Jackson joins,
concurring.
  I join in full the Court's opinion, which holds that the Elev-
enth Circuit's distinctive approach to suits under the Federal
Tort Claims Act (FTCA) is wrong in two respects. See ante,
at 403–404, 413–414. The law enforcement proviso modifes
only the subsection in which it is located: Section 2680(h)'s
intentional-tort exception. Ante, at 403–408. The United
States, moreover, may not defeat an FTCA suit simply by
“showing that a federal offcer's acts had `some nexus with
furthering federal policy' and `compl[ied] with the full range
416              MARTIN v. UNITED STATES

                    Sotomayor, J., concurring

of federal law.' ” Ante, at 409 (alteration in original). With
those two principles clarifed, I also agree that the Eleventh
Circuit must now consider on remand whether the
FTCA's discretionary-function exception bars plaintiffs'
negligent- and intentional-tort claims. Ante, at 414–415. I
write separately to underscore that there is reason to think
the discretionary-function exception may not apply to these
claims.
                               I
   The FTCA shields the United States from liability for
claims “based upon” a federal employee's “exercise or per-
formance” (or failure to exercise or perform) “a discretionary
function or duty,” “whether or not the discretion involved be
abused.” 28 U. S. C. § 2680(a). This Court has set forth a
two-part test that governs the application of § 2680(a), known
as the discretionary-function exception. First, courts must
consider the nature of the offcial's conduct and decide
Page Proof Pending Publication
whether it “ `involv[es] an element of judgment or choice.' ”
United States v. Gaubert, 499 U. S. 315, 322 (1991) (quoting
Berkovitz v. United States, 486 U. S. 531, 536 (1988)). “The
requirement of judgment or choice,” this Court has ex-
plained, “is not satisfed if a `federal statute, regulation, or
policy specifcally prescribes a course of action for an em-
ployee to follow.' ” 499 U. S., at 322. In such circum-
stances, “ `the employee has no rightful option but to adhere
to the directive.' ” Ibid.
   Even where a federal employee retains an element of
choice, however, the exception does not apply refexively.
After all, it is rare for statutes or regulations to prescribe
an offcial's required course of conduct down to the very last
detail, so some degree of choice will almost invariably re-
main. Thus, this Court has required lower courts to deter-
mine, at the second step, whether “th[e] judgment is of the
kind that the discretionary function exception was designed
to shield.” Berkovitz, 486 U. S., at 536. Because “[t]he
basis for the discretionary function exception was Congress'
                   Cite as: 605 U. S. 395 (2025)             417

                    Sotomayor, J., concurring

desire to `prevent judicial “second-guessing” of legislative
and administrative decisions grounded in social, economic,
and political policy through the medium of an action in tort,' ”
this Court has clarifed that the exception protects only those
governmental actions and decisions that are themselves
“based on considerations of public policy.” Id., at 536–537
(quoting United States v. S. A. Empresa De Viacao Aerea
Rio Grandense, 467 U. S. 797, 814 (1984)); see Gaubert, 499
U. S., at 323.
   To that end, this Court has said, it is “obviou[s]” that some
discretionary acts performed by Government agents “are
within the scope of [their] employment but not within the
discretionary function exception.” Id., at 325, n. 7. If a
federal banking regulator “drove an automobile on a mission
connected with his offcial duties and negligently collided
with another car,” for example, the Court has made clear
that “the exception would not apply.” Ibid. That is be-
Page Proof Pending Publication
cause, while “driving requires the constant exercise of dis-
cretion, the offcial's decisions in exercising that discretion
can hardly be said to be grounded in regulatory policy.”
Ibid.
   It has been 34 years since this Court last weighed in on
the discretionary-function exception, see Gaubert, 499 U. S.
315, and despite substantial percolation in the courts of ap-
peals, the “exact boundaries of the exception remain un-
clear,” 14 C. Wright, A. Miller, & H. Hershkoff, Federal Prac-
tice and Procedure § 3658.1 (4th ed. Supp. 2025). The Court
today resolves one of the Circuit splits regarding the excep-
tion's application: whether claims that fall within the FTCA's
law enforcement proviso must necessarily fall outside of the
discretionary-function exception. Yet, as the Court recog-
nizes, ante, at 414–415, several additional points of disagree-
ment remain, including whether allegedly “unconstitutional
conduct necessarily falls outside the exception” because off-
cials lack discretion to violate the Constitution, and “whether
the exception applies when the challenged act was careless
418               MARTIN v. UNITED STATES

                     Sotomayor, J., concurring

rather than a considered exercise of discretion.” Xi v.
Haugen, 68 F. 4th 824, 843 (CA3 2023) (Bibas, J., concurring)
(describing these Circuit splits). Given the enduring ques-
tions about how to apply the discretionary-function excep-
tion, and the divergent approaches taken by the Circuits, it
is long past time for this Court to weigh in on the excep-
tion's scope.
   Even without further intervention by this Court, however,
there is reason to question the Eleventh Circuit's suggestion
in the decision below that the discretionary-function excep-
tion might apply “ `unless a source of federal law “specifcally
prescribes” a [federal employee's] course of conduct.' ” 2024
WL 1716235, *6 (2024) (quoting Shivers v. United States, 1
F. 4th 924, 931 (CA11 2021); emphasis in original). That ap-
proach, which even the Government does not defend before
this Court, would run headlong into this Court's precedents.
Gaubert, after all, applies the discretionary-function excep-
tion only where an offcial's actions both involve an element
Page Proof Pending Publication
of judgment and rely on public policy considerations. See
499 U. S., at 322–323; see also Berkovitz, 486 U. S., at 536–
537. Whether federal law prescribes a particular course of
action resolves only the frst of Gaubert's two questions.
The second question (whether an offcer's decisions were
“ `based on considerations of public policy,' ” 499 U. S., at 323)
remains live. Were it otherwise, a federal offcial's negli-
gent driving decisions would fall beyond the reach of the
discretionary-function exception only if federal law or policy
specifcally prescribed an offcer's permissible maneuvers on
the road. Cf. id., at 325, n. 7.

                                II
  Agent Guerra's preparation to execute search and arrest
warrants at 3741 Landau Lane, and his subsequent decision
to raid Martin and Cliatt's home at 3756 Denville Trace, bear
some resemblance to Gaubert's negligent driving hypotheti-
cal. Like driving, executing a warrant always involves
                   Cite as: 605 U. S. 395 (2025)           419

                   Sotomayor, J., concurring

some measure of discretion. Yet it is hard to see how Guer-
ra's conduct in this case, including his allegedly negligent
choice to use his personal GPS and his failure to check the
street sign or house number on the mailbox before breaking
down Martin's door and terrorizing the home's occupants, in-
volved the kind of policy judgments that the discretionary-
function exception was designed to protect.
   The FTCA's history, too, confrms Congress's intention to
subject the United States to liability for intentional torts
committed by law enforcement offcers like Agent Guerra.
The relevant context is as follows: For several decades after
the FTCA's enactment, Congress retained the United States'
sovereign immunity for myriad intentional torts committed
by federal employees, including assault, battery, and false
arrest. See 28 U. S. C. § 2680(h). That changed, however,
in response to an episode that will sound familiar to readers
of the majority opinion. See ante, at 399–400.
Page Proof Pending Publication
   In April 1973, Herbert and Evelyn Giglotto awoke in their
Collinsville, Illinois, townhouse “to the sound of someone
smashing down their door and bursting into their home.” J.
Boger, M. Gitenstein, & P. Verkuil, The Federal Tort Claims
Act Intentional Torts Amendment: An Interpretative Analy-
sis, 54 N. C. L. Rev. 497, 500 (1976). After 15 state and
federal offcers ransacked the Giglottos' home, tied them up
at gunpoint, and threatened to shoot Mr. Giglotto if he
moved, the offcers realized they “ `ha[d] the wrong people.' ”
Ibid. The offcers eventually moved on to the home of Don-
ald Askew, where they terrorized yet another innocent cou-
ple before confessing they had acted on a “ `bad tip.' ” Id.,
at 501.
   The Collinsville raids garnered national attention, includ-
ing from the United States Senate. See S. Rep. No. 93–588,
pp. 2–3 (1973); see also Brief for Members of Congress as
Amici Curiae 8–12. Noting that “[t]here [was] no effective
legal remedy against the Federal Government for the actual
physical damage, much less the pain, suffering and humilia-
420               MARTIN v. UNITED STATES

                    Sotomayor, J., concurring

tion to which the Collinsville families ha[d] been subjected,”
the Senate Committee on Government Operations proposed
an amendment to the FTCA. See S. Rep. No. 93–588, at 2.
The solution was to add a proviso to the end of the
intentional-tort exception that “deprive[s] the Federal Gov-
ernment of the defense of sovereign immunity” for FTCA
suits arising out of the state-law torts of “assault, battery,
false imprisonment, false arrest, malicious prosecution, or
abuse of process” by federal law enforcement offcers. Id.,
at 3; see § 2680(h). The Committee designed the proviso to
ensure “innocent individuals who are subjected to raids of
the type conducted in Collinsville, Illinois, will have a cause
of action against the individual Federal agents [via suits
under Bivens v. Six Unknown Fed. Narcotics Agents, 403
U. S. 388 (1971)] and the Federal Government [through the
FTCA].” Id., at 3 (emphasis added).
   Of course, the majority correctly holds that the proviso
Page Proof Pending Publication
does not altogether trump the discretionary-function excep-
tion: Even if an intentional-tort claim “survive[s its] en-
counter with subsection (h) thanks to the law enforcement
proviso,” courts must nevertheless consider whether “sub-
section (a)'s discretionary-function exception bars . . . the
plaintiffs' negligent- or intentional-tort claims.” Ante, at
413–414. Courts, however, should not ignore the existence
of the law enforcement proviso, or the factual context that
inspired its passage, when construing the discretionary-func-
tion exception. Whatever else is true of that exception, any
interpretation should allow for liability in the very cases
Congress amended the FTCA to remedy. See Van Buren v.
United States, 593 U. S. 374, 393 (2021) (“ `When Congress
amends legislation, courts must presume it intends the
change to have real and substantial effect' ”); see also Hun-
gary v. Simon, 604 U. S. 115, 132 (2025) (relying on a statute's
“ `historical backdrop' ” to “ `permit adjudication of claims' ”
that an earlier decision of this Court had avoided).
                  Cite as: 605 U. S. 395 (2025)           421

                   Sotomayor, J., concurring

                        *      *      *
  On remand, the court should approach the discretionary-
function exception with an eye to both steps of the Gaubert
analysis and to the existence and context of the intentional-
tort exception's law enforcement proviso.




Page Proof Pending Publication
                           Reporter’s Note

  The attached opinion has been revised to refect the usual publication
and citation style of the United States Reports. The revised pagination
makes available the offcial United States Reports citation in advance of
publication. The syllabus has been prepared by the Reporter of Decisions
for the convenience of the reader and constitutes no part of the opinion of
Page Proof Pending Publication
the Court. A list of counsel who argued or fled briefs in this case, and
who were members of the bar of this Court at the time this case was
argued, has been inserted following the syllabus. Other revisions may
include adjustments to formatting, captions, citation form, and any errant
punctuation. The following additional edits were made:

p. 401, line 11: “against” is changed to “by”
p. 419, line 20: “house” is changed to “home”

```

---

## GROUP: content/cases/Nance v. Ward.md  (`case`, 5 assertions)

### content_page

```
---
title: Nance v. Ward
type: case
citation: "597 U.S. 159 (2022)"
parallel_cite: "142 S. Ct. 2214; 213 L. Ed. 2d 499"
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2022
date_decided: ""
docket: 21-439
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
  opinion_url: "https://www.courtlistener.com/opinion/6480697/nance-v-ward/"
  cluster_id: 6480697
  opinion_id: null
  identity_checked: true
lake:
  record_id: Nance v. Ward
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Martin v. United States]]"
tags:
  - case
  - section-1983
  - habeas
  - eighth-amendment
  - method-of-execution
holding: "Section 1983 remains an appropriate procedural vehicle for a prisoner's Eighth Amendment method-of-execution claim even where the alternative method the prisoner proposes is not authorized by the executing State's death-penalty statute, because such relief does not necessarily prevent the State from carrying out the sentence and so falls outside the core of habeas corpus."
---

# Nance v. Ward

*597 U.S. 159 (2022)* (No. 21-439) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 6480697 → opinion 6352830; quote string-matched to the CL slip-opinion text 2026-07-07 (CL carries the slip opinion "597 U. S. ____ (2022)"; U.S.-reporter page equality not asserted per S2 A3). S9 promotes. -->

## Background
Michael Nance, a Georgia death-row inmate, sued under 42 U.S.C. § 1983 to enjoin the State from executing him by lethal injection — the sole method Georgia law authorizes — alleging that his compromised veins would make that method create a substantial risk of severe pain in violation of the Eighth Amendment. As the required readily-available alternative, Nance proposed death by firing squad, a method authorized by four other States but not by Georgia. The Eleventh Circuit did not reach the merits: it recharacterized his § 1983 complaint as a second-or-successive [[Common Legal Terms#habeas-corpus|habeas]] petition, reasoning that because Georgia law (treated as "fixed") authorized only lethal injection, enjoining that method would necessarily invalidate his death sentence.

## Issue
Whether a prisoner may bring an Eighth Amendment method-of-execution claim under § 1983 — rather than in [[Common Legal Terms#habeas-corpus|habeas]] — when the alternative method he identifies is not authorized by the executing State's death-penalty statute.

## Rule
A prisoner may generally sue under § 1983 unless his claim falls within that statute's implicit exception for actions lying at the core of [[Common Legal Terms#habeas-corpus|habeas corpus]] — that is, where the relief sought would "necessarily imply the invalidity of his conviction or sentence." Because a method-of-execution claim requires the prisoner to identify an available alternative, granting relief does not necessarily prevent the State from carrying out the sentence; it merely requires the State to switch methods. That the proposed alternative would require Georgia to amend its statute does not change the vehicle: "one of the 'main aims' of § 1983 is to 'override'—and thus compel change of—state laws when necessary to vindicate federal constitutional rights." The Court framed and answered the question directly: "The question presented is whether § 1983 is still a proper vehicle. We hold that it is." — 597 U.S. 159 (slip op., at 1). ^pin-op

## Application
Nance's requested relief left his execution in Georgia's control: if the State wished to carry out the sentence, it could enact legislation authorizing the firing squad, a method a court had found fairly easy to employ. Any incidental delay from a statutory change was irrelevant to the vehicle question, which turns on whether the relief would *necessarily* invalidate the sentence. Reading state-by-state statutory variation into the § 1983-versus-[[Common Legal Terms#habeas-corpus|habeas]] line would make the federal vehicle turn on "the vagaries of state law" and would turn the Court's promise in *Bucklew* — that a prisoner may propose an out-of-state alternative — "into a sham."

## Conclusion
The judgment of the Eleventh Circuit was **reversed** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. Kagan, J., delivered the opinion of the Court, joined by Roberts, C.J., and Breyer, Sotomayor, and Kavanaugh, JJ.; Barrett, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], joined by Thomas, Alito, and Gorsuch, JJ.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Nance* is a vehicle-selection decision at the § 1983/[[Common Legal Terms#habeas-corpus|habeas]] boundary rather than a liability-standard case: it confirms that § 1983 reaches claims whose remedy would compel a change in state law, so long as the relief does not necessarily bar the sentence's enforcement.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Nance v. Ward*, 597 U.S. 159 (2022)](https://www.courtlistener.com/opinion/6480697/nance-v-ward/) — pinpoint: slip op., at 1 (Opinion of the Court, holding; Kagan, J.). CL carries the slip opinion ("597 U. S. ____ (2022)"; cluster 6480697 → opinion 6352830); slip-only per S2 A3 — quote string-matched to the CL opinion text 2026-07-07, U.S.-reporter page equality not asserted.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3835ec73f66f14e3", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "597 U.S. 159 (2022)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "142 S. Ct. 2214; 213 L. Ed. 2d 499", "title": "Nance v. Ward", "year": "2022"}}
{"assertion_id": "5abde71c474d60ce", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Section 1983 remains an appropriate procedural vehicle for a prisoner's Eighth Amendment method-of-execution claim even where the alternative method the prisoner proposes is not authorized by the executing State's death-penalty statute, because such relief does not necessarily prevent the State from carrying out the sentence and so falls outside the core of habeas corpus.", "title": "Nance v. Ward"}}
{"assertion_id": "f359596e8680fa19", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Recent development", "title": "Nance v. Ward"}}
{"assertion_id": "6719ff10b069fcb1", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Nance v. Ward"}}
{"assertion_id": "79622d8bfc724257", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Nance v. Ward", "varies_by_point": "false"}}
```

### lake record — Nance v. Ward

```json
{
  "schema_version": "s2.v1",
  "record_id": "Nance v. Ward",
  "status": "under_review",
  "identity": {
    "case_name": "Nance v. Ward",
    "case_name_short": "Nance",
    "case_name_full": "",
    "input_case_name": "Nance v. Ward",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2022,
    "docket": "21-439",
    "cluster_id": 6480697,
    "lead_opinion_id": 6352830,
    "sibling_ids": [],
    "absolute_url": "/opinion/6480697/nance-v-ward/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "597 U.S. 159",
      "volume": "597",
      "reporter": "U.S.",
      "page": "159",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "142 S. Ct. 2214",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "2214",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "213 L. Ed. 2d 499",
        "volume": "213",
        "reporter": "L. Ed. 2d",
        "page": "499",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "597 U.S. 159",
        "volume": "597",
        "reporter": "U.S.",
        "page": "159",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "142 S. Ct. 2214",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "2214",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "213 L. Ed. 2d 499",
        "volume": "213",
        "reporter": "L. Ed. 2d",
        "page": "499",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "597 U.S. 159",
    "official_selection": {
      "court_class": "scotus",
      "selected": "597 U.S. 159",
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
    "date_created": "2026-07-06T12:11:17Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:11:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:11:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:11:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:11:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "nance-v-ward--6480697",
      "to_record_id": "Nance v. Ward",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Nance v. Ward

```
(Slip Opinion)              OCTOBER TERM, 2021                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

       NANCE v. WARD, COMMISSIONER, GEORGIA
         DEPARTMENT OF CORRECTIONS, ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                THE ELEVENTH CIRCUIT

       No. 21–439.      Argued April 25, 2022—Decided June 23, 2022
A prisoner who challenges a State’s proposed method of execution under
  the Eighth Amendment must identify a readily available alternative
  method that would significantly reduce the risk of severe pain. If the
  prisoner proposes a method already authorized under state law, the
  Court has held that his claim can go forward under 42 U. S. C. §1983,
  rather than in habeas. See Nelson v. Campbell, 541 U. S. 637, 644–
  647. But the prisoner is not confined to proposing a method already
  authorized under state law; he may ask for a method used in other
  States. See Bucklew v. Precythe, 587 U. S. ___, ___. The question pre-
  sented is whether a prisoner who does so may still proceed under
  §1983.
     Petitioner Michael Nance brought suit under §1983 to enjoin Geor-
  gia from using lethal injection to carry out his execution. Lethal injec-
  tion is the only method of execution that Georgia law now authorizes.
  Nance alleges that applying that method to him would create a sub-
  stantial risk of severe pain. As an alternative to lethal injection,
  Nance proposes death by firing squad—a method currently approved
  by four other States. The District Court dismissed Nance’s §1983 suit
  as untimely. The Eleventh Circuit rejected it for a different reason:
  that Nance should have advanced his method-of-execution claim by
  way of a habeas petition rather than a §1983 suit. A habeas petition,
  that court stated, is appropriate when a prisoner seeks to invalidate
  his death sentence. And the Eleventh Circuit thought that was what
  Nance was doing. It asserted that Georgia law—which again, only au-
  thorizes execution by lethal injection—had to be taken as “fixed.” 981
  F. 3d 1201, 1211. Under that “fixed” law, the court said, enjoining
  Georgia from executing Nance by lethal injection would mean that he
2                            NANCE v. WARD

                                 Syllabus

    could not be executed at all. The court therefore “reconstrued” Nance’s
    §1983 complaint as a habeas petition. Id., at 1203. Having done so,
    the court then dismissed Nance’s petition as “second or successive,”
    because he had previously sought federal habeas relief. 28 U. S. C.
    §2244(b).
Held: Section 1983 remains an appropriate vehicle for a prisoner’s
 method-of-execution claim where, as here, the prisoner proposes an al-
 ternative method not authorized by the State’s death-penalty statute.
    Both §1983 and the federal habeas statute enable a prisoner to com-
 plain of “unconstitutional treatment at the hands of state officials.”
 Heck v. Humphrey, 512 U. S. 477, 480. A prisoner may generally sue
 under §1983, unless his claim falls into that statute’s “implicit excep-
 tion” for actions that lie “within the core of habeas corpus.” Wilkinson
 v. Dotson, 544 U. S. 74, 79. When a prisoner seeks relief that would
 “necessarily imply the invalidity of his conviction or sentence,” he
 comes within the core and must proceed in habeas. Heck, 512 U. S., at
 487.
    The Court has twice held that prisoners could bring method-of-
 execution claims under §1983. See Nelson, 541 U. S., at 644–647; Hill
 v. McDonough, 547 U. S. 573, 580–583. Although these cases predated
 the Court’s requirement that prisoners identify alternative methods of
 execution, each prisoner had still said enough to leave the Court con-
 vinced that alternatives to the challenged procedures were available.
 See Nelson, 541 U. S., at 646; Hill, 547 U. S., at 580–581. Because
 alternatives were available, the prisoners’ challenges would not “nec-
 essarily prevent [the State] from carrying out [their] execution[s].”
 Nelson, 541 U. S., at 647 (emphasis in original); see Hill, 547 U. S., at
 583. That made §1983 a proper vehicle.
    In Nelson and Hill, the Court observed that using a different method
 required only a change in an agency’s uncodified protocol. Here, Geor-
 gia would have to change its statute to carry out Nance’s execution by
 firing squad. Except for that fact, this case would even more clearly
 than Nelson and Hill be fit for §1983. Since those cases, the Court has
 required a prisoner bringing a method-of-execution claim to propose
 an alternative way of carrying out his death sentence. Thus, an order
 granting the prisoner relief does not, as required for habeas, “neces-
 sarily prevent” the State from implementing the execution. Nelson,
 541 U. S., at 647 (emphasis in original). Rather, the order gives the
 State a pathway forward.
    That remains true even where, as here, the proposed alternative is
 one unauthorized by present state law. Nance’s requested relief still
 places his execution in Georgia’s control. If Georgia wants to carry out
 the death sentence, it can enact legislation approving what a court has
 found to be a fairly easy-to-employ method of execution. Although that
                     Cite as: 597 U. S. ____ (2022)                     3

                                Syllabus

  may take more time and effort than changing an agency protocol, Hill
  explained that the “incidental delay” involved in changing a procedure
  is irrelevant to the vehicle question—which focuses on whether the re-
  quested relief would “necessarily” invalidate the death sentence. 547
  U. S., at 583. And anyway, Georgia has given no reason to think that
  passing new legislation would be a substantial impediment.
     The Court of Appeals could reach the contrary conclusion only by
  wrongly treating Georgia’s statute as immutable. In its view, granting
  Nance relief would necessarily imply the invalidity of his death sen-
  tence because Georgia law must be taken as “fixed.” 981 F. 3d, at 1211.
  But one of the “main aims” of §1983 is to “override”—and thus compel
  change of—state laws when necessary to vindicate federal constitu-
  tional rights. Monroe v. Pape, 365 U. S. 167, 173. Indeed, courts not
  uncommonly entertain prisoner suits under §1983 that may, if success-
  ful, require changing state law.
     Under the contrary approach, the federal vehicle for bringing a fed-
  eral method-of-execution claim would depend on the vagaries of state
  law. Consider how Nance’s claim would fare in different States. In
  Georgia (and any other State with lethal injection as the sole author-
  ized method), he would have to bring his claim in a habeas petition.
  But in States authorizing other methods when a court holds injection
  unlawful, he could file a §1983 suit. It would be strange to read state-
  by-state discrepancies into the Court’s understanding of how §1983
  and the habeas statute apply to federal constitutional claims. That is
  especially so because the use of the vehicles can lead to different out-
  comes: An inmate in one State could end up getting his requested re-
  lief, while an inmate in another might have his case thrown out.
     The approach of the Court of Appeals raises one last problem: It
  threatens to undo the commitment this Court made in Bucklew. The
  Court there told prisoners they could identify an alternative method
  not “presently authorized” by the executing State’s law. 587 U. S., at
  ___. But under the approach of the Court of Appeals, a prisoner who
  presents an out-of-state alternative is relegated to habeas—and once
  there, he will almost inevitably collide with the second-or-successive
  bar. That result, precluding claims like Nance’s, would turn Bucklew
  into a sham.
     Finally, recognizing that §1983 is a good vehicle for a claim like
  Nance’s does not countenance “last-minute” claims to forestall an exe-
  cution. Id., at ___. Courts must consider delay in deciding whether to
  grant a stay of execution, and outside the stay context, courts have
  tools to streamline §1983 actions and protect a sentence’s timely en-
  forcement. Pp. 5–13.
981 F. 3d 1201, reversed and remanded.

  KAGAN, J., delivered the opinion of the Court, in which ROBERTS, C. J.,
and BREYER, SOTOMAYOR, and KAVANAUGH, JJ., joined. BARRETT, J., filed
a dissenting opinion, in which THOMAS, ALITO, and GORSUCH, JJ., joined.
                        Cite as: 597 U. S. ____ (2022)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 21–439
                                    _________________


   MICHAEL NANCE, PETITIONER v. TIMOTHY C.
    WARD, COMMISSIONER, GEORGIA DEPART-
        MENT OF CORRECTIONS, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
          APPEALS FOR THE ELEVENTH CIRCUIT
                                  [June 23, 2022]

  JUSTICE KAGAN delivered the opinion of the Court.
   In several recent decisions, this Court has set out rules
for challenging a State’s proposed method of execution un-
der the Eighth Amendment. To prevail on such a claim, a
prisoner must identify a readily available alternative
method of execution that would significantly reduce the risk
of severe pain. In doing so, the prisoner is not confined to
proposing a method authorized by the executing State’s
law; he may instead ask for a method used in other States.
See Bucklew v. Precythe, 587 U. S. ___, ___ (2019) (slip op.,
at 19).
   This case concerns the procedural vehicle appropriate for
a prisoner’s method-of-execution claim. We have held that
such a claim can go forward under 42 U. S. C. §1983, rather
than in habeas, when the alternative method proposed is
already authorized under state law. See Nelson v. Camp-
bell, 541 U. S. 637, 644–647 (2004). Here, the prisoner has
identified an alternative method that is not so authorized.
The question presented is whether §1983 is still a proper
vehicle. We hold that it is.
2                          NANCE v. WARD

                          Opinion of the Court

                             I
                             A
  States choosing to impose capital punishment have over
time sought out “more humane way[s] to carry out death
sentences.” Glossip v. Gross, 576 U. S. 863, 868 (2015). In
the 27 States with the death penalty, lethal injection is by
far the most common method of execution. See ibid. Fif-
teen States, including Georgia, authorize only the use of le-
thal injection.1 Nine States authorize lethal injection plus
one or more other specified methods; of those (to use an ex-
ample relevant here), four approve the firing squad.2 And
three States provide that if their authorized methods (in-
cluding lethal injection) are found unconstitutional, then
they may carry out a death sentence by any constitutional
means.3
  A death row inmate may attempt to show that a State’s
planned method of execution, either on its face or as applied
to him, violates the Eighth Amendment’s prohibition on

——————
  1 Ariz. Rev. Stat. Ann. §13–757(A) (2020); Ga. Code Ann. §17–10–38(a)

(2020); Idaho Code Ann. §19–2716 (2017); Ind. Code §35–38–6–1(a)
(2021); Kan. Stat. Ann. §22–4001(a) (2007); La. Rev. Stat. Ann.
§15:569(B) (West 2022); Mont. Code Ann. §46–19–103(3) (2021); Neb.
Rev. Stat. §83–964 (2020 Cum. Supp.); Nev. Rev. Stat. §176.355(1)
(2017); N. C. Gen. Stat. Ann. §15–188 (2021); Ohio Rev. Code Ann.
§2949.22(A) (Lexis 2021); Ore. Rev. Stat. §137.473(1) (2021); 61 Pa. Cons.
Stat. §4304(a) (2015 Special Edition); S. D. Codified Laws §23A–27A–32
(2016); Tex. Code Crim. Proc. Ann., Art. §43.14(a) (Vernon 2018).
  2 Mississippi, Oklahoma, South Carolina, and Utah authorize the fir-

ing squad among other methods of execution. H. B. 1479, 2022 Leg., Reg.
Sess. (Miss.); Okla. Stat., Tit. 22, §1014 (2020 Supp.); S. C. Code Ann.
§24–3–530 (2021 Cum. Supp.); Utah Code §77–18–113 (2021). The rest
of the States in this bucket most commonly authorize electrocution or
lethal gas. See Ark. Code Ann. §§5–4–617(a), (l) (Supp. 2021); Cal. Penal
Code Ann. §3604(a) (West Supp. 2022); Ky. Rev. Stat. Ann.
§§431.220(1)(a), 431.223 (Lexis 2021); Mo. Rev. Stat. §546.720(1) (2016);
Wyo. Stat. Ann. §7–13–904 (2021).
  3 Ala. Code §15–18–82.1(c) (2018); Fla. Stat. §922.105(3) (2018); Tenn.

Code Ann. §40–23–114(d) (2018).
                  Cite as: 597 U. S. ____ (2022)            3

                      Opinion of the Court

“cruel and unusual” punishment. To succeed on that claim,
the Court held in Glossip, he must satisfy two require-
ments. First, he must establish that the State’s method of
execution presents a “substantial risk of serious harm”—
severe pain over and above death itself. Id., at 877. Second,
and more relevant here, he “must identify an alternative
[method] that is feasible, readily implemented, and in fact
significantly reduce[s]” the risk of harm involved. Ibid. (in-
ternal quotation marks omitted). Only through a “compar-
ative exercise,” we have explained, can a judge “decide
whether the State has cruelly ‘superadded’ pain to the pun-
ishment of death.” Bucklew, 587 U. S., at ___ (slip op., at
15).
   In identifying an alternative method, the Court in Buck-
lew held, an inmate is “not limited to choosing among those
presently authorized by a particular State’s law.” Id., at ___
(slip op., at 19). The prisoner may, for example, “point to a
well-established protocol in another State as a potentially
viable option.” Ibid. The Eighth Amendment, Bucklew ex-
plained, “is the supreme law of the land, and the compara-
tive assessment it requires can’t be controlled by the State’s
choice of which methods to authorize.” Id., at ___ (slip op.,
at 20); see Arthur v. Dunn, 580 U. S. ___, ___ (2017) (slip
op., at 10) (SOTOMAYOR, J., dissenting from denial of certi-
orari). In addition, Bucklew stated, allowing an inmate to
propose a method not authorized by the State keeps his
“burden” within reasonable bounds. 587 U. S., at ___ (slip
op., at 19). Because the inmate can look beyond the State’s
current law, we saw “little likelihood” that he would “be un-
able to identify an available alternative.” Id., at ___ (slip
op., at 20); see id., at ___ (slip op., at 2) (KAVANAUGH, J.,
concurring).
                            B
  While trying to flee a bank robbery, petitioner Michael
4                        NANCE v. WARD

                        Opinion of the Court

Nance shot and killed a bystander. A Georgia jury con-
victed Nance of murder, and the trial court sentenced him
to death. Nance challenged his conviction and sentence—
first on direct appeal, next in state collateral proceedings,
and finally in federal habeas—but without success.
   Nance later brought suit under §1983 to enjoin Georgia
from using lethal injection to carry out his death sentence.
As stated above, lethal injection is the only method of exe-
cution Georgia law now authorizes. See supra, at 2.4 In his
complaint, Nance alleges that applying that method to him
would create a substantial risk of severe pain. See App. to
Pet. for Cert. 86a. According to Nance, his veins are “se-
verely compromised and unsuitable for sustained intrave-
nous access.” Ibid. They are, Nance says, likely to “blow”
during the execution, “leading to the leakage of the lethal
injection drug into the surrounding tissue” and thereby
causing “intense pain and burning.” Ibid. On top of that,
Nance asserts, his longtime use of a prescription drug for
back pain creates a risk that the sedative used in the State’s
lethal injection protocol will fail to “render him unconscious
and insensate.” Ibid. Nance proposes, as a “readily availa-
ble alternative” method of execution, “death by firing
squad.” Ibid. As noted earlier, four other States have ap-
proved that method. See supra, at 2, and n. 2. Use of a
firing squad, Nance says, will lead to “swift and virtually
painless” death. App. to Pet. for Cert. 102a. And imple-
menting that method, he says, would be simple: Georgia
has enough qualified personnel and could borrow specific
protocols from another State. Ibid.
   After the District Court dismissed Nance’s suit as un-
timely, the Court of Appeals for the Eleventh Circuit re-
jected it for a different reason—that Nance had used the

——————
   4 See Ga. Code Ann. §17–10–38(a) (“All persons who have been con-

victed of a capital offense and have had imposed upon them a sentence
of death shall suffer such punishment by lethal injection”).
                 Cite as: 597 U. S. ____ (2022)            5

                     Opinion of the Court

wrong procedural vehicle. In the panel majority’s view,
Nance should have brought his method-of-execution claim
by way of a habeas petition rather than a §1983 suit. A
habeas petition, the court stated, is appropriate when a
prisoner seeks to “invalidate” a death sentence. 981 F. 3d
1201, 1209 (2020). And the court thought that was what
Nance was doing: The injunction he requested, preventing
the use of lethal injection, “necessarily impl[ies] the inva-
lidity of his death sentence.” Id., at 1203. That was so, the
court reasoned, because Georgia law “must [be taken] as
fixed”—and under that “fixed” law, if Nance could not be
executed by lethal injection, then he could not be executed
at all. Id., at 1211. The court therefore “reconstrued”
Nance’s complaint as a habeas petition. Id., at 1203. And
having done so, the court dismissed the petition as “second
or successive” because Nance had already sought federal
habeas relief. 28 U. S. C. §2244(b); see supra, at 4. Judge
Martin dissented, arguing that Nance could proceed under
§1983. In her view, Nance was not challenging his death
sentence; all he wanted was an order telling “the State to
execute him by a different method.” 981 F. 3d, at 1215. The
Eleventh Circuit denied Nance’s petition for rehearing en
banc over the dissent of three judges. See 994 F. 3d 1335
(2021).
   We granted certiorari, 595 U. S. ___ (2022), and now re-
verse.
                              II
  This Court has often considered, when evaluating state
prisoners’ constitutional claims, the dividing line between
§1983 and the federal habeas statute. Each law enables a
prisoner to complain of “unconstitutional treatment at the
hands of state officials.” Heck v. Humphrey, 512 U. S. 477,
480 (1994). But there the resemblance stops. The habeas
statute contains procedural requirements (like the second-
6                     NANCE v. WARD

                     Opinion of the Court

or-successive rule) nowhere found in §1983; the former stat-
ute may therefore require dismissal of a claim when the lat-
ter statute would not. See id., at 480–481. Still more per-
tinent here, the scope of the two laws also differs. Section
1983 broadly authorizes suit against state officials for the
“deprivation of any rights” secured by the Constitution.
Read literally, that language would apply to all of a pris-
oner’s constitutional claims, thus swamping the habeas
statute’s coverage of claims that the prisoner is “in custody
in violation of the Constitution.” 28 U. S. C. §2254(a); see
Wilkinson v. Dotson, 544 U. S. 74, 78–79 (2005). So we have
not read §1983 literally in the prisoner context. To the con-
trary, we have insisted that §1983 contains an “implicit ex-
ception” for actions that lie “within the core of habeas cor-
pus.” Id., at 79.
   In defining that core, this Court has focused on whether
a claim challenges the validity of a conviction or sentence.
See Preiser v. Rodriguez, 411 U. S. 475, 489 (1973). The
simplest cases arise when an inmate, alleging a flaw in his
conviction or sentence, seeks “immediate or speedier re-
lease” from prison. Heck, 512 U. S., at 481. The analogue
in the capital punishment context, also clear-cut, is when
an inmate seeks to overturn his death sentence, thus pre-
venting the State from executing him. Slightly less obvious,
this Court has held that an inmate must proceed in habeas
when the relief he seeks would “necessarily imply the inva-
lidity of his conviction or sentence.” Id., at 487 (barring
§1983 suits for money damages when prevailing would im-
ply a conviction was wrongful). In doing so, though, we
have underscored that the implication must be “neces-
sar[y].” Wilkinson, 544 U. S., at 81 (emphasis in original);
see Nelson, 541 U. S., at 647. On the opposite end of the
spectrum, the Court has held that a prison-conditions claim
may be brought as a §1983 suit. See Preiser, 411 U. S., at
498–499. Such a suit—for example, challenging the ade-
quacy of a prison’s medical care—does not go to the validity
                     Cite as: 597 U. S. ____ (2022)                     7

                          Opinion of the Court

of a conviction or sentence, and thus falls outside habeas’s
core.
   In Nelson v. Campbell and Hill v. McDonough, this Court
held two method-of-execution claims to fall on the §1983
side of the divide. See Nelson, 541 U. S., at 644–647; Hill,
547 U. S. 573, 580–583 (2006). Both cases involved chal-
lenges to a State’s lethal injection protocol—the first to the
use of a “cut-down” procedure to access the prisoner’s veins,
the second to a particular three-drug sequence. The cases
predated our requirement that prisoners identify alterna-
tive methods, but each prisoner had said enough to leave
the Court convinced that alternatives to the challenged pro-
cedures were available. See Nelson, 541 U. S., at 646; Hill,
547 U. S., at 580–581. And that made the difference in both
cases. A claim should go to habeas, the Court held, only if
granting the prisoner relief “would necessarily prevent [the
State] from carrying out its execution.” Nelson, 541 U. S.,
at 647 (emphasis in original); see Hill, 547 U. S., at 583.5
In neither case would it have done so. Each prisoner had
asked only for a change in implementing the death penalty,
and an order granting that relief would not prevent the
State from executing him. So the claims could proceed un-
der §1983.
   Both Nelson and Hill, though, reserved the question at
issue here: whether the result should be different when a
State’s death-penalty statute does not authorize the alter-
native method of execution. See Nelson, 541 U. S., at 645;
Hill, 547 U. S., at 580. In each case, the Court observed
that using a different method required no change in the
State’s statute, but only a change in an agency’s uncodified
——————
  5 In both cases, the Court made clear that its formulation (again, would

granting relief necessarily prevent the execution) merely adapted to the
capital punishment context the question the Court had formerly asked
in choosing between §1983 and habeas: Would granting relief necessarily
imply the invalidity of a conviction or sentence? See Nelson, 541 U. S.,
at 646; Hill, 547 U. S., at 583; supra, at 6.
8                      NANCE v. WARD

                      Opinion of the Court

protocols. Here, all parties agree that Georgia would have
to change its statute to carry out Nance’s execution by
means of a firing squad. They dispute whether that fact
switches Nance’s claim to the habeas track.
   Except for the Georgia statute, this case would even more
clearly than Nelson and Hill be fit for §1983. Since those
two cases, we have compelled a prisoner bringing a method-
of-execution claim to propose an alternative way for the
State to carry out his death sentence. He must, we have
said, present a “proposal” that is “sufficiently detailed” to
show that an alternative method is both “feasible” and
“readily implemented.” Bucklew, 587 U. S., at ___ (slip op.,
at 21); see supra, at 3. In other words, he must make the
case that the State really can put him to death, though in a
different way than it plans. The substance of the claim, now
more than ever, thus points toward §1983. The prisoner is
not challenging the death sentence itself; he is taking the
validity of that sentence as a given. And he is providing the
State with a veritable blueprint for carrying the death sen-
tence out. If the inmate obtains his requested relief, it is
because he has persuaded a court that the State could read-
ily use his proposal to execute him. The court’s order there-
fore does not, as required for habeas, “necessarily prevent”
the State from carrying out its execution. Nelson, 541 U. S.,
at 647 (emphasis in original). Rather, the order gives the
State a pathway forward.
   That remains true, we hold today, even if the alternative
route necessitates a change in state law. Nance’s requested
relief still places his execution in Georgia’s control. Assum-
ing it wants to carry out the death sentence, the State can
enact legislation approving what a court has found to be a
fairly easy-to-employ method of execution. To be sure,
amending a statute may require some more time and effort
than changing an agency protocol, of the sort involved in
Nelson and Hill. But in Hill, we explained that the “inci-
dental delay” involved in changing a procedure—which
                     Cite as: 597 U. S. ____ (2022)                    9

                          Opinion of the Court

even when uncodified may take some real work6—is not rel-
evant to the vehicle question. 547 U. S., at 583. Instead,
that inquiry (as described earlier) focuses on whether the
requested relief would “necessarily” invalidate, or foreclose
the State from implementing, the death sentence. Ibid.; see
supra, at 6. And anyway, Georgia has given us no reason
to think that the amendment process would be a substan-
tial impediment. The State has legislated changes to its
execution method several times before. See Dept. of Cor-
rections, Office of Planning and Analysis, A History of the
Death Penalty in Georgia: Executions by Year 1924–2014
(Jan. 2015) (describing how Georgia moved from hanging to
electrocution to lethal injection). Other States have regu-
larly done the same, often in an effort to make executions
more humane. See S. Banner, The Death Penalty: An
American History 296–297 (2002); see supra, at 2. That
Nance’s claim would require such action does not turn it
from one contesting a method of execution into one disput-
ing the underlying death sentence.
   The Court of Appeals could reach the contrary conclusion
only by wrongly treating Georgia’s statute as immutable.
Recall the court’s reasoning: Granting Nance relief would
“necessarily imply[] the invalidity” of his death sentence be-
cause Georgia law (presumably both statutes and regula-
tions) “must [be taken] as fixed.” 981 F. 3d, at 1210–1211;
see supra, at 5; post, at 3–4 (BARRETT, J., dissenting) (agree-
ing that we must “take state law as we find it”). But why
must it be so taken—when as a matter of fact Georgia could
change its law and execute Nance? And when Nance ac-
cepts the validity of the State’s taking that course? The
Court of Appeals posited that “it is not [a federal court’s]
place to entertain complaints under section 1983” that
——————
  6 In a recent case, Texas described to this Court the complexity of

changing uncodified execution protocols, given the number of state actors
who need to reach agreement. See Respondents’ Rule 32.3 Material in
Ramirez v. Collier, O. T. 2021, No. 21–5592, p. 14a.
10                    NANCE v. WARD

                     Opinion of the Court

would compel a State to change its capital punishment law.
981 F. 3d, at 1211; see post, at 3. Except that sometimes it
is. One of the “main aims” of §1983 is to “override”—and
thus compel change of—state laws when necessary to vin-
dicate federal constitutional rights. Monroe v. Pape, 365
U. S. 167, 173 (1961); see Zinermon v. Burch, 494 U. S. 113,
124 (1990). Or said otherwise, the ordinary and expected
outcome of many a meritorious §1983 suit is to declare un-
enforceable (whether on its face or as applied) a state stat-
ute as currently written. See, e.g., Cedar Point Nursery v.
Hassid, 594 U. S. ___ (2021). And in turn, the unsurprising
effect of such a judgment may be to send state legislators
back to the drawing board. See, e.g., Kolender v. Lawson,
461 U. S. 352, 358 (1983). A prisoner, no less than any
other §1983 litigant, can bring a suit of that ilk—can seek
relief that would preclude a State from achieving some re-
sult unless and until it amends a statute.
   And indeed, courts not uncommonly entertain prisoner
suits under §1983 that may, if successful, require changing
state law. As noted earlier, the classic prisoner §1983 suit
is one challenging prison conditions—say, overcrowding or
inadequate medical care. See supra, at 6–7. Those suits
can be brought under §1983 because—just like this one—
they attack not the validity of a conviction or sentence, but
only a way of implementing the sentence. (They concern, in
other words, how the prescribed incarceration is being car-
ried out.) And the suits do not get diverted into habeas if,
as sometimes is true, a judgment for the inmate would re-
quire a new statutory appropriation for the prison—to hire
more doctors, for example. See, e.g., Stafford v. Carter, No.
1:17–cv–00289 (SD Ind.), ECF Docs. 268, 282. Similarly, no
one would think an action of that kind should go to habeas
if the prison policy challenged (say, each facility’s maximum
population) were specified in a statute or regulation. Or
consider another kind of prisoner §1983 suit this Court has
recently considered—one by a death row inmate seeking to
                  Cite as: 597 U. S. ____ (2022)            11

                      Opinion of the Court

compel the State to open the execution chamber to his spir-
itual advisor. See Dunn v. Ray, 586 U. S. ___ (2019); Mur-
phy v. Collier, 587 U. S. ___ (2019); Gutierrez v. Saenz, 592
U. S. ___ (2021); Ramirez v. Collier, 595 U. S. ___ (2022).
Here too, the claim belongs in §1983 because—just like this
one—it challenges not the validity of a death sentence, but
only the State’s mode of carrying it out. And again, we can-
not think it would matter if a State codified its no-spiritual-
advisor protocol in a regulation. The State, assuming it lost
the suit, would then have to modify its law to go forward
with the execution. But the nature of the suit would still be
the same. The complaint would still ask to adjust only a
matter of implementation, so it still could be filed under
§1983.
   Under the contrary approach, the federal vehicle for
bringing a federal claim—and with that, the viability of the
claim—would depend on the vagaries of state law. Consider
how Nance’s own method-of-execution claim would fare in
different States. In Georgia (and any other State with le-
thal injection as the sole authorized method), he would have
to bring his claim in a habeas petition. But in some other
States primarily using lethal injection, he could file a §1983
suit—because their statutes include back-up plans for when
a court holds injection unconstitutional. See supra, at 2.
Oklahoma’s statute, for example, provides in that event for
several alternative methods, including a firing squad. See
Okla. Stat., Tit. 22, §§1014(B)–(D). And Alabama’s statute,
in addition to listing alternatives, provides for execution “by
any constitutional method.” Ala. Code §15–18–82.1(c).
Similar issues of non-uniformity could arise when inmates
challenge, as in Nelson and Hill, specific ways of carrying
out a lethal injection. See supra, at 7. That is because some
States have codified injection protocols in their statutes or
regulations, while others (like Georgia) have not. Compare,
e.g., Ark. Code Ann. §§5–4–617(c)–(f ) with, e.g., Ga. Code
Ann. §17–10–38(a). It would be strange to read such state-
12                    NANCE v. WARD

                     Opinion of the Court

by-state discrepancies into our understanding of how §1983
and the habeas statute apply to federal constitutional
claims. And that is especially so because the use of those
vehicles can lead to different outcomes: An inmate in one
State could end up getting his requested relief, while a sim-
ilarly situated inmate in another would have his suit
thrown out. We cannot agree with the dissent that such a
disparity would be “unremarkable.” Post, at 3. Its ac-
ceptance would mean that the Eighth Amendment is en-
forceable in federal court in one State, but not in another.
Again, this case tells the tale: Having reconstrued Nance’s
complaint as a habeas petition, the court below dismissed it
as second or successive—a bar existing in habeas alone. See
supra, at 5–6.
   That part of the circuit court’s opinion raises one last
problem, because it threatens to undo the commitment this
Court made in Bucklew. See post, at 4 (acknowledging the
point, though finding it irrelevant). Recall that the Court
there told inmates they could identify an alternative
method of execution not “presently authorized” by the exe-
cuting State’s law. 587 U. S., at ___ (slip op., at 19); see
supra, at 3. That option would ensure state law does not
“control[ ]” the Eighth Amendment inquiry; and it would
keep manageable the inmate’s “burden” to identify an alter-
native. 587 U. S., at ___–___ (slip op., at 19–20). Under the
circuit court’s approach, however, that option is no option
at all. Once an inmate presents an out-of-state alternative,
he is relegated to habeas. And once he is in habeas, he will
(according to the circuit court) almost inevitably collide
with the second-or-successive bar (because a method-of-ex-
ecution claim typically postdates a first habeas petition by
many years). We do not here decide whether that view of
the second-or-successive bar is correct. But the two aspects
of the circuit court’s ruling, when taken together, turn
Bucklew into a sham. On the Eleventh Circuit’s view, Geor-
                 Cite as: 597 U. S. ____ (2022)           13

                     Opinion of the Court

gia law effectively prevents an inmate like Nance from put-
ting forward an out-of-state alternative. And Georgia law
thereby precludes the kind of method-of-execution claim
this Court told prisoners they could bring.
  One last point from Bucklew—this one about “dilatory”
tactics—bears repeating here. Id., at ___ (slip op., at 30).
In recognizing that §1983 is a good vehicle for a claim like
Nance’s, we do not for a moment countenance “last-minute”
claims relied on to forestall an execution. Ibid. “Courts
should police carefully against attempts to use [method-of-
execution] challenges as tools to interpose unjustified de-
lay.” Ibid. In deciding whether to grant a stay of execution,
courts must consider whether such a challenge “could have
been brought earlier” or otherwise reflects a prisoner’s “at-
tempt at manipulation.” Ibid. (internal quotation marks
omitted). And outside the stay context, courts have a vari-
ety of tools—including the “substantive [and] procedural
limitations” that the Prison Litigation Reform Act im-
poses—to streamline §1983 actions and protect “the timely
enforcement of a sentence.” Nelson, 541 U. S., at 650 (list-
ing PLRA limitations); Bucklew, 587 U. S., at ___ (slip op.,
at 29). Finally, all §1983 suits must be brought within a
State’s statute of limitations for personal-injury actions.
See Wallace v. Kato, 549 U. S. 384, 387 (2007). Here, the
District Court held Nance’s suit untimely under that limi-
tations period. See No. 20–cv–00107 (ND Ga., Mar. 13,
2020), ECF Doc. 26, p. 12; supra, at 4. The Eleventh Circuit
did not review that holding because it instead reconstrued
the action as a habeas petition. Now that we have held that
reconstruction unjustified, the court on remand can address
the timeliness question, as well as any others that remain.
                        *     *    *
   For the reasons stated, we reverse the judgment of the
Court of Appeals for the Eleventh Circuit and remand the
case for further proceedings consistent with this opinion.
14    NANCE v. WARD

     Opinion of the Court


                            It is so ordered.
                   Cite as: 597 U. S. ____ (2022)              1

                      BARRETT, J., dissenting

SUPREME COURT OF THE UNITED STATES
                           _________________

                            No. 21–439
                           _________________


    MICHAEL NANCE, PETITIONER v. TIMOTHY C.
     WARD, COMMISSIONER, GEORGIA DEPART-
         MENT OF CORRECTIONS, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
          APPEALS FOR THE ELEVENTH CIRCUIT
                          [June 23, 2022]

  JUSTICE BARRETT, with whom JUSTICE THOMAS, JUSTICE
ALITO, and JUSTICE GORSUCH join, dissenting.
  An inmate must bring a method-of-execution challenge in
a federal habeas application, rather than under 42 U. S. C.
§1983, if “a grant of relief to the inmate would necessarily
bar the execution.” Hill v. McDonough, 547 U. S. 573, 583
(2006). Under this criterion, Michael Nance must proceed
in habeas because a judgment in his favor would “neces-
sarily bar” the State from executing him. Ibid. Nance
asked the District Court to “enjoin the Defendants from pro-
ceeding with [his] execution . . . by a lethal injection,” claim-
ing that the use of such method would violate the Eighth
Amendment as applied to him. App. to Pet. for Cert. 103a–
104a. But lethal injection is the only method of execution
authorized under Georgia law. See Ga. Code Ann. §17–10–
38(a) (2020). Thus, if Nance is successful, the defendants
in this case—the commissioner of the Georgia Department
of Corrections and the warden—will be powerless to carry
out his sentence. That makes habeas the right vehicle for
Nance’s Eighth Amendment challenge.
  The Court sees things differently. True, Nance is arguing
that the Eighth Amendment renders his sentence invalid
under current Georgia law. But the Court points out that
2                      NANCE v. WARD

                     BARRETT, J., dissenting

the law could change: The legislature could authorize exe-
cution by firing squad, the alternative method that Nance
has proposed. In fact, the Court says that Nance’s proposal
offers Georgia a “veritable blueprint for carrying the death
sentence out.” Ante, at 8. So an order in Nance’s favor
would not “necessarily bar” the State from ever executing
Nance, in the Court’s view. Instead, the order would “giv[e]
the State a pathway forward” if the legislature chooses to
pursue the amendment process. Ibid.
   The Court is looking too far down the road. In my view,
the consequence of the relief that a prisoner seeks depends
on state law as it currently exists. And under existing state
law, there is no question that Nance’s challenge necessarily
implies the invalidity of his lethal injection sentence: He
seeks to prevent the State from executing him in the only
way it lawfully can.
   In this respect, Nance’s method-of-execution challenge
differs from those brought in Nelson v. Campbell, 541 U. S.
637 (2004), and Hill, 547 U. S. 573. In Nelson, the inmate
challenged the use of a “cut-down” procedure to access his
veins. 541 U. S., at 640–642. We held that the suit sounded
in §1983 because it would not “necessarily prevent Alabama
from carrying out its execution.” Id., at 647. We reasoned
that, though venous access was an indispensable prerequi-
site to lethal injection, “a particular means of gaining such
access” was not. Id., at 645. Notably, “[n]o Alabama statute
require[d] use of the cut-down,” and the State did not put
forward any “duly-promulgated regulations to the con-
trary.” Id., at 646. So even a successful challenge on these
grounds “would have allowed the State to proceed with the
execution as scheduled.” Ibid.
   The same was true in Hill, which involved an inmate’s
challenge to Florida’s three-drug protocol. 547 U. S., at 578.
We held that the inmate could proceed under §1983 because
his “action if successful would not necessarily prevent the
State from executing him by lethal injection.” Id., at 580.
                  Cite as: 597 U. S. ____ (2022)            3

                     BARRETT, J., dissenting

We emphasized that the complaint did “not challenge the
lethal injection sentence as a general matter” but instead
only “the anticipated protocol.” Ibid. As in Nelson, we
stressed that Florida law did “not require the department
of corrections to use the challenged procedure.” 547 U. S.,
at 580. The State was “free to use an alternative lethal in-
jection procedure,” and so we explained that “[u]nder these
circumstances a grant of injunctive relief could not be seen
as barring the execution of Hill’s sentence.” Id., at 580–581.
   Here, by contrast, the warden and the commissioner are
not free to use an alternative to lethal injection—so if Nance
succeeds, they cannot carry out his sentence. And though
the Court contends otherwise, that consequence “switches
Nance’s claim to the habeas track.” Ante, at 8. An inmate
can use §1983 actions to challenge many, if not most, as-
pects of prison administration. But when a challenge would
prevent a State from enforcing a conviction or sentence, the
more rigorous, federalism-protective requirements of ha-
beas apply. The Court finds a way around those require-
ments with a theory at odds with the very federalism inter-
ests they are designed to protect: that an injunction barring
the State from enforcing a sentence according to state law
does not really bar the State from enforcing the sentence
because the State can pass a new law.
   Unlike the Court, I would take state law as we find it in
determining whether a suit sounds in habeas or §1983. The
Court worries that this approach would make the appropri-
ate federal vehicle “depend on the vagaries of state law.”
Ante, at 11. Some States, like Georgia, provide for a single
method of execution by statute; other States, like Alabama,
allow for more flexibility. See ibid. So if state law deter-
mined the vehicle, an inmate in Georgia would have to chal-
lenge the lethal injection method in habeas, while an in-
mate in Alabama could use §1983. But that does not
illustrate “the vagaries of state law”; it is an unremarkable
consequence of federalism. States make different choices in
4                      NANCE v. WARD

                     BARRETT, J., dissenting

exercising their power to define punishment, and the law
has long recognized a sovereign’s interest in mandating a
particular form of capital punishment. Cf. 4 W. Blackstone,
Commentaries on the Laws of England 397 (1769) (a sheriff
would be “guilty of felony” if he “alter[ed] the manner of the
execution”). Habeas is appropriate in Georgia because un-
der Georgia law, to enjoin execution by lethal injection is to
enjoin enforcement of the sentence itself. See Ga. Code
Ann. §17–10–38(a) (“All persons who have been convicted
of a capital offense and have had imposed upon them a sen-
tence of death shall suffer such punishment by lethal injec-
tion”). In Alabama, enjoining execution by lethal injection
does not have the same effect. See Ala. Code §15–18–82.1(c)
(2018) (permitting execution “by any constitutional method
of execution” if the other methods provided for by statute
are held unconstitutional). The two sovereigns have made
different choices about how to define punishment, and fed-
eral law is designed to respect the choice of each.
   I understand the impulse to find a way out of habeas and
into §1983. In States like Georgia, a claim under Bucklew
v. Precythe, 587 U. S. ___ (2019), alleging an alternative
method of execution not presently authorized by state law
would be difficult to assert in a federal habeas application
because it would “almost inevitably collide with the second-
or-successive bar.” Ante, at 12. But we acknowledged that
very possibility in Bucklew. 587 U. S., at ___ (slip op., at
19). And more importantly, the unavailability of federal ha-
beas relief does not justify recourse to §1983. Cf. Wilkinson
v. Dotson, 544 U. S. 74, 87–88 (2005) (Scalia, J., concurring)
(“[A] prisoner who wishes to challenge the length of his con-
finement, but who cannot obtain federal habeas relief be-
cause of the statute of limitations or the restrictions on suc-
cessive petitions, cannot use the unavailability of federal
habeas relief in his individual case as grounds for proceed-
ing under §1983” (citations omitted)). The habeas statutes
funnel such challenges to the state courts—which are, after
                 Cite as: 597 U. S. ____ (2022)           5

                    BARRETT, J., dissenting

all, “the principal forum” for them. Harrington v. Richter,
562 U. S. 86, 103 (2011).
  For these reasons, I respectfully dissent.

```

---
